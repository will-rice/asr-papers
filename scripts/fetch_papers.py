"""Fetch ASR-related papers from multiple academic sources.

This script queries arXiv and Semantic Scholar for papers
related to automatic speech recognition and related topics.  It is designed
to be run in two modes:

* **Historical (first run)**: pulls everything submitted since the
  end-to-end era began (2015-01-01 onwards, Deep Speech / Listen, Attend
  and Spell).
* **Incremental (scheduled)**: pulls only papers submitted in the last N days
  (default 8, so a weekly cron with a one-day overlap never misses anything).

Results are written to ``papers.csv`` in the repository root and the
``README.md`` table is regenerated from that file.

Usage::

    # Full historical fetch (first-run / back-fill):
    python scripts/fetch_papers.py --full

    # Incremental fetch (last 8 days, for weekly cron):
    python scripts/fetch_papers.py

    # Incremental fetch for the last N days:
    python scripts/fetch_papers.py --days 30
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
README_MD = REPO_ROOT / "README.md"

# arXiv API base URL
ARXIV_API_BASE = "http://export.arxiv.org/api/query"

# Search queries – cast a wide net over ASR and related topics.
SEARCH_QUERIES = [
    "speech recognition",
    "speech-to-text",
    "speech to text",
    "speech transcription",
    "end-to-end ASR",
    "streaming ASR",
    "multilingual ASR",
    "word error rate",
    "speech foundation model",
    "RNN transducer",
]

# Earliest date to consider (start of the end-to-end ASR era: Deep Speech /
# Listen, Attend and Spell).
HISTORY_START = date(2015, 1, 1)

# arXiv namespaces
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

CSV_FIELDNAMES = ["arxiv_id", "title", "authors", "submitted", "categories", "url", "abstract"]

# Negative keywords – papers whose title or abstract contain any of these
# phrases (case-insensitive, word-bounded) are excluded from results.  This
# list grows over time as off-topic papers show up in the feed.
NEGATIVE_KEYWORDS = [
    # Clinical / audiology / hearing science
    "cochlear implant",
    "hearing aid",
    "hearing loss",
    "hearing impairment",
    "audiogram",
    "auditory brainstem",
    "tinnitus",
    "presbycusis",
    "speech therapy",
    "speech-language pathology",
    # Neuroscience / brain decoding
    "eeg",
    "fmri",
    "magnetoencephalography",
    "brain-computer interface",
    "electrocorticography",
    "neural speech tracking",
    "speech neuroprosthesis",
    "imagined speech",
    # Human speech perception / linguistics (non-ML)
    "speech perception in noise",
    "infant-directed speech",
    "second language acquisition",
    # Clinical detection from speech (ASR as a feature extractor, not the subject)
    "alzheimer",
    "dementia",
    # Retail / e-commerce
    "e-commerce",
    # Talking-face synthesis / lipsync (see will-rice/lipsync-papers)
    "talking head",
    "talking face",
    "lip sync",
    "lipsync",
    "lip-sync",
    "face reenactment",
    # Speaker recognition / biometrics / forensics
    "speaker verification",
    "speaker identification",
    "anti-spoofing",
    "deepfake",
    "forensic speaker",
    # Other speech tasks with their own literature
    "speech emotion recognition",
    "voice conversion",
    # Social science / humanities where "speech" is idiomatic
    "hate speech",
    "free speech",
    "speech act theory",
    "political speech",
]

# Positive relevance keywords – papers must contain at least one of these
# ASR signals in title or abstract (word-bounded, case-insensitive).
POSITIVE_RELEVANCE_KEYWORDS = [
    "speech recognition",
    "speech recognizer",
    "speech recogniser",
    "asr",
    "speech-to-text",
    "speech to text",
    "speech transcription",
    "transcribe speech",
    "word error rate",
    "character error rate",
    "rnn transducer",
    "rnn-t",
]

# ML keywords – papers must also look like ML/speech research to pass.
ML_KEYWORDS = [
    "machine learning",
    "deep learning",
    "neural",
    "transformer",
    "attention",
    "encoder",
    "decoder",
    "self-supervised",
    "semi-supervised",
    "end-to-end",
    "acoustic model",
    "language model",
    "sequence-to-sequence",
    "fine-tuning",
    "generative",
    "multimodal",
    "learning-based",
]

# Delay between API requests to respect arXiv's rate-limit guidance (3 s).
API_DELAY_SECONDS = 3

# Number of results to fetch per API page.
PAGE_SIZE = 100

# Maximum pages to fetch per keyword from each external source.
MAX_PAGES_PER_QUERY = 5

# Semantic Scholar API base URL
SEMANTIC_SCHOLAR_API_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"


# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------


def _build_query(keywords: str, start_date: date, end_date: date) -> str:
    """Return a URL-encoded arXiv API query string."""
    # Date range filter: submittedDate:[YYYYMMDD TO YYYYMMDD]
    date_filter = (
        f"submittedDate:[{start_date.strftime('%Y%m%d')}0000 TO {end_date.strftime('%Y%m%d')}2359]"
    )
    # Title + abstract search
    term = f'(ti:"{keywords}" OR abs:"{keywords}") AND {date_filter}'
    return term


def _fetch_page(query: str, start: int, max_results: int) -> ET.Element:
    """Fetch one page of arXiv results and return the parsed XML root."""
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API_BASE}?{params}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = resp.read()
            return ET.fromstring(data)
        except Exception as exc:  # noqa: BLE001
            wait = min(2**attempt * API_DELAY_SECONDS, 30)
            print(f"  [warn] request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch arXiv page after 5 attempts: {url}")


def _parse_entry(entry: ET.Element) -> dict | None:
    """Parse a single <entry> element into a paper dict."""
    arxiv_id_raw = entry.findtext("atom:id", namespaces=NS) or ""
    # e.g. http://arxiv.org/abs/2008.10010v1 → 2008.10010
    arxiv_id = re.sub(r"v\d+$", "", arxiv_id_raw.split("/abs/")[-1]).strip()
    if not arxiv_id:
        return None

    title = re.sub(r"\s+", " ", entry.findtext("atom:title", namespaces=NS) or "").strip()

    authors = ", ".join(
        (a.findtext("atom:name", namespaces=NS) or "").strip()
        for a in entry.findall("atom:author", namespaces=NS)
    )

    published_raw = entry.findtext("atom:published", namespaces=NS) or ""
    submitted = published_raw[:10]  # YYYY-MM-DD

    categories = " ".join(
        cat.get("term", "") for cat in entry.findall("atom:category", namespaces=NS)
    )

    url = f"https://arxiv.org/abs/{arxiv_id}"

    abstract = re.sub(
        r"\s+",
        " ",
        entry.findtext("atom:summary", namespaces=NS) or "",
    ).strip()

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": categories,
        "url": url,
        "abstract": abstract,
    }


def _compile_keywords(keywords: list[str]) -> re.Pattern[str]:
    """Compile keywords into one case-insensitive, word-bounded pattern.

    Word boundaries keep short keywords like ``asr`` from matching inside
    unrelated words (e.g. "Basra").
    """
    return re.compile(r"\b(?:" + "|".join(re.escape(kw.lower()) for kw in keywords) + r")\b")


_NEGATIVE_PATTERN = _compile_keywords(NEGATIVE_KEYWORDS)
_POSITIVE_RELEVANCE_PATTERN = _compile_keywords(POSITIVE_RELEVANCE_KEYWORDS)
_ML_PATTERN = _compile_keywords(ML_KEYWORDS)


def _paper_haystack(paper: dict) -> str:
    """Return lower-cased title+abstract text for keyword matching."""
    return f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()


def _is_excluded(paper: dict) -> bool:
    """Return True if the paper matches any negative keyword."""
    return bool(_NEGATIVE_PATTERN.search(_paper_haystack(paper)))


def _has_positive_relevance_signal(paper: dict) -> bool:
    """Return True if the paper has ASR relevance signals."""
    return bool(_POSITIVE_RELEVANCE_PATTERN.search(_paper_haystack(paper)))


def _has_ml_signal(paper: dict) -> bool:
    """Return True if the paper appears to be ML/speech focused."""
    return bool(_ML_PATTERN.search(_paper_haystack(paper)))


def _is_relevant_asr_paper(paper: dict) -> bool:
    """Return True if paper passes exclusion, ML, and positive relevance gates."""
    return (
        not _is_excluded(paper) and _has_ml_signal(paper) and _has_positive_relevance_signal(paper)
    )


def fetch_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return all papers matching *keywords* within [start_date, end_date]."""
    query = _build_query(keywords, start_date, end_date)
    papers: list[dict] = []
    start = 0

    while True:
        root = _fetch_page(query, start=start, max_results=PAGE_SIZE)

        total_el = root.find(
            "opensearch:totalResults", {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"}
        )
        total = int(total_el.text) if total_el is not None and total_el.text else 0

        entries = root.findall("atom:entry", namespaces=NS)
        if not entries:
            break

        for entry in entries:
            paper = _parse_entry(entry)
            if paper:
                papers.append(paper)

        start += len(entries)
        if start >= total or len(entries) < PAGE_SIZE:
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# Semantic Scholar helpers
# ---------------------------------------------------------------------------

_S2_FIELDS = "paperId,title,authors,year,externalIds,abstract,publicationDate"


def _fetch_s2_page(keywords: str, year_filter: str, offset: int) -> dict:
    """Fetch one page of Semantic Scholar results and return the parsed JSON."""
    params = urllib.parse.urlencode(
        {
            "query": keywords,
            "fields": _S2_FIELDS,
            "year": year_filter,
            "offset": offset,
            "limit": PAGE_SIZE,
        }
    )
    url = f"{SEMANTIC_SCHOLAR_API_BASE}?{params}"
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "asr-papers-bot/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2**attempt * API_DELAY_SECONDS, 30)
            print(f"  [warn] S2 request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch Semantic Scholar page after 5 attempts: {url}")


def _parse_s2_entry(item: dict, start_date: date, end_date: date) -> dict | None:
    """Parse a Semantic Scholar paper item into our paper dict format."""
    title = re.sub(r"\s+", " ", (item.get("title") or "")).strip()
    if not title:
        return None

    # Filter by publicationDate when available; fall back to year.
    pub_date_str = (item.get("publicationDate") or "")[:10]
    submitted = ""
    if pub_date_str:
        try:
            pub_date = date.fromisoformat(pub_date_str)
            if pub_date < start_date or pub_date > end_date:
                return None
            submitted = pub_date_str
        except ValueError:
            pass
    if not submitted:
        year = item.get("year")
        if not year:
            return None
        submitted = f"{year}-01-01"

    external_ids = item.get("externalIds") or {}
    arxiv_id = (external_ids.get("ArXiv") or "").strip()
    s2_id = (item.get("paperId") or "").strip()

    if arxiv_id:
        paper_id = arxiv_id
        url = f"https://arxiv.org/abs/{arxiv_id}"
    elif s2_id:
        paper_id = f"s2:{s2_id}"
        url = f"https://www.semanticscholar.org/paper/{s2_id}"
    else:
        return None

    authors = ", ".join((a.get("name") or "").strip() for a in (item.get("authors") or []))
    abstract = re.sub(r"\s+", " ", (item.get("abstract") or "")).strip()

    return {
        "arxiv_id": paper_id,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": "",
        "url": url,
        "abstract": abstract,
    }


def fetch_semantic_scholar_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return papers from Semantic Scholar matching *keywords* in [start_date, end_date]."""
    start_year = start_date.year
    end_year = end_date.year
    year_filter = f"{start_year}-{end_year}" if start_year != end_year else str(start_year)

    papers: list[dict] = []
    offset = 0

    for _ in range(MAX_PAGES_PER_QUERY):
        try:
            data = _fetch_s2_page(keywords, year_filter, offset)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            break

        items = data.get("data") or []
        if not items:
            break

        for item in items:
            paper = _parse_s2_entry(item, start_date, end_date)
            if paper:
                papers.append(paper)

        if len(items) < PAGE_SIZE or not data.get("next"):
            break

        offset += len(items)
        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------


def load_existing_papers() -> dict[str, dict]:
    """Load papers from CSV, keyed by arxiv_id."""
    if not PAPERS_CSV.exists():
        return {}
    with PAPERS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {row["arxiv_id"]: row for row in reader}


def save_papers(papers_by_id: dict[str, dict]) -> None:
    """Write all papers to CSV sorted by submitted date (newest first)."""
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)
    with PAPERS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# README helpers
# ---------------------------------------------------------------------------

_TABLE_START = "<!-- PAPERS_TABLE_START -->"
_TABLE_END = "<!-- PAPERS_TABLE_END -->"


def _build_table(papers_by_id: dict[str, dict]) -> str:
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)

    # Group by year (newest first).
    by_year: dict[str, list] = defaultdict(list)
    for row in rows:
        year = row.get("submitted", "")[:4] or "Unknown"
        by_year[year].append(row)

    sections: list[str] = []
    for year in sorted(by_year.keys(), reverse=True):
        section_lines = ["<details open>", f"<summary><h3>{year}</h3></summary>", ""]
        for row in by_year[year]:
            # Truncate long author lists for readability
            authors = row.get("authors", "")
            if authors.count(",") >= 4:
                authors = ", ".join(authors.split(", ")[:4]) + " et al."
            date_str = row.get("submitted", "")[:10]
            abstract = row.get("abstract", "").strip()
            title = row["title"]
            url = row["url"]
            arxiv_id = row.get("arxiv_id", "")

            local_md = REPO_ROOT / "papers" / year / f"{arxiv_id}.md"
            local_link = ""
            if local_md.exists():
                local_link = f" · [📄 Read](papers/{year}/{arxiv_id}.md)"

            section_lines.append(f"#### [{title}]({url}){local_link}")
            section_lines.append(f"**{authors}** · {date_str}")
            section_lines.append("")
            if abstract:
                section_lines.append("<details>")
                section_lines.append("<summary>Abstract</summary>")
                section_lines.append("")
                section_lines.append(abstract)
                section_lines.append("")
                section_lines.append("</details>")
                section_lines.append("")
            else:
                section_lines.append("")

        section_lines.append("</details>")
        sections.append("\n".join(section_lines))

    return "\n\n".join(sections)


def update_readme(papers_by_id: dict[str, dict]) -> None:
    """Regenerate the paper table in README.md."""
    if not README_MD.exists():
        return

    content = README_MD.read_text(encoding="utf-8")
    table = _build_table(papers_by_id)
    new_section = f"{_TABLE_START}\n{table}\n{_TABLE_END}"

    if _TABLE_START in content:
        # Replace existing table
        pattern = re.compile(
            re.escape(_TABLE_START) + r".*?" + re.escape(_TABLE_END),
            re.DOTALL,
        )
        content = pattern.sub(lambda _: new_section, content)
    else:
        # Append after the first paragraph
        content = content.rstrip() + "\n\n" + new_section + "\n"

    README_MD.write_text(content, encoding="utf-8")
    print(f"README updated with {len(papers_by_id)} papers.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _collect_from_source(
    source_name: str,
    fetch_fn,
    keywords_list: list[str],
    start_date: date,
    end_date: date,
    existing: dict[str, dict],
) -> int:
    """Query *fetch_fn* for each keyword and merge results into *existing*."""
    new_count = 0
    for keywords in keywords_list:
        print(f"\nQuerying {source_name} for: {keywords!r} …")
        try:
            papers = fetch_fn(keywords, start_date, end_date)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue

        for paper in papers:
            pid = paper["arxiv_id"]
            if pid not in existing and _is_relevant_asr_paper(paper):
                existing[pid] = paper
                new_count += 1
                print(f"  + {pid}: {paper['title'][:70]}")

        time.sleep(API_DELAY_SECONDS)

    return new_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch ASR papers from arXiv and Semantic Scholar."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--full",
        action="store_true",
        help=f"Fetch all papers since {HISTORY_START} (historical back-fill).",
    )
    mode.add_argument(
        "--days",
        type=int,
        default=8,
        metavar="N",
        help="Fetch papers from the last N days (default: 8, for weekly cron).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    today = datetime.now(tz=timezone.utc).date()

    if args.full:
        start_date = HISTORY_START
        end_date = today
        print(f"Full historical fetch: {start_date} → {end_date}")
    else:
        start_date = today - timedelta(days=args.days)
        end_date = today
        print(f"Incremental fetch (last {args.days} days): {start_date} → {end_date}")

    existing = load_existing_papers()
    print(f"Loaded {len(existing)} existing papers from {PAPERS_CSV.name}.")

    # Remove any previously saved papers that no longer pass relevance gates.
    before = len(existing)
    existing = {pid: p for pid, p in existing.items() if _is_relevant_asr_paper(p)}
    removed = before - len(existing)
    if removed:
        print(f"Removed {removed} existing paper(s) failing relevance filters.")

    new_count = 0
    new_count += _collect_from_source(
        "arXiv", fetch_papers, SEARCH_QUERIES, start_date, end_date, existing
    )
    new_count += _collect_from_source(
        "Semantic Scholar",
        fetch_semantic_scholar_papers,
        SEARCH_QUERIES,
        start_date,
        end_date,
        existing,
    )

    print(f"\nFound {new_count} new papers. Total: {len(existing)}.")

    if new_count > 0 or removed > 0 or not PAPERS_CSV.exists():
        save_papers(existing)
        print(f"Saved to {PAPERS_CSV}.")

    update_readme(existing)


if __name__ == "__main__":
    main()
