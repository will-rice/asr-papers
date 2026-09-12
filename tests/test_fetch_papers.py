"""Tests for Semantic Scholar fetching behavior in scripts/fetch_papers.py."""

from __future__ import annotations

from datetime import date

import pytest

from scripts.fetch_papers import SourceRateLimitedError, _collect_from_source, _fetch_s2_page


def _http_429(url: str) -> Exception:
    import urllib.error

    return urllib.error.HTTPError(url=url, code=429, msg="Too Many Requests", hdrs=None, fp=None)


def test_fetch_s2_page_raises_rate_limit_without_retry_sleep(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        raise _http_429(req.full_url)

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    monkeypatch.setattr(
        "scripts.fetch_papers.time.sleep",
        lambda *_: (_ for _ in ()).throw(AssertionError("sleep should not be called for HTTP 429")),
    )

    with pytest.raises(SourceRateLimitedError):
        _fetch_s2_page("speech recognition", "2026", offset=0)


def test_collect_from_source_stops_after_rate_limit(monkeypatch) -> None:
    seen_keywords: list[str] = []

    def fake_fetch(keywords: str, start_date: date, end_date: date) -> list[dict]:  # noqa: ARG001
        seen_keywords.append(keywords)
        raise SourceRateLimitedError("rate limited")

    monkeypatch.setattr("scripts.fetch_papers.time.sleep", lambda *_: None)
    new_count = _collect_from_source(
        source_name="Semantic Scholar",
        fetch_fn=fake_fetch,
        keywords_list=["speech recognition", "speech-to-text", "RNN transducer"],
        start_date=date(2026, 1, 1),
        end_date=date(2026, 1, 2),
        existing={},
    )

    assert new_count == 0
    assert seen_keywords == ["speech recognition"]
