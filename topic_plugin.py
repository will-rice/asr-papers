"""ASR relevance gate ported from the legacy fetch script.

A paper is accepted when its title and abstract match no negative keyword, at
least one ML keyword, and at least one ASR keyword. Matching is
case-insensitive and word-bounded so short keywords like ``asr`` do not match
inside unrelated words (e.g. "Basra"). The declarative ``topic`` gates cannot
express this: they match substrings and have no "any of A and any of B" rule.
"""

import re

from papers_pipeline.models import Paper
from papers_pipeline.topics import TopicDecision

# Papers whose title or abstract contain any of these phrases are excluded.
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

# Papers must contain at least one of these ASR signals.
ASR_KEYWORDS = [
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

# Papers must also look like ML research.
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


def compile_keywords(keywords: list[str]) -> re.Pattern[str]:
    """Compile keywords into one case-insensitive, word-bounded pattern."""
    return re.compile(r"\b(?:" + "|".join(re.escape(kw) for kw in keywords) + r")\b")


NEGATIVE_PATTERN = compile_keywords(NEGATIVE_KEYWORDS)
ASR_PATTERN = compile_keywords(ASR_KEYWORDS)
ML_PATTERN = compile_keywords(ML_KEYWORDS)


def accept_topic(paper: Paper) -> TopicDecision:
    """Accept ML papers about ASR that match no negative keyword."""
    text = f"{paper.title} {paper.abstract}".lower()
    negative = NEGATIVE_PATTERN.search(text)
    if negative:
        return TopicDecision(False, f"matched excluded term: {negative[0]}")
    if not ML_PATTERN.search(text):
        return TopicDecision(False, "missing ML term")
    if not ASR_PATTERN.search(text):
        return TopicDecision(False, "missing ASR term")
    return TopicDecision(True, "accepted")
