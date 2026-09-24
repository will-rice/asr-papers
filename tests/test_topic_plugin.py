from pathlib import Path

import pytest
import yaml

from papers_pipeline.config import TopicConfig
from papers_pipeline.models import Paper
from papers_pipeline.topics import TopicDecision, build_topic_gate

CONFIG = Path(__file__).resolve().parents[1] / "papers.yml"


@pytest.fixture
def gate():
    topic = yaml.safe_load(CONFIG.read_text())["topic"]
    return build_topic_gate(TopicConfig.model_validate(topic))


@pytest.mark.parametrize(
    ("title", "abstract", "expected"),
    [
        (
            "Streaming Transformer Transducers",
            "We reduce the word error rate of end-to-end ASR.",
            TopicDecision(True, "accepted"),
        ),
        (
            "Speech Recognition for Hearing Aid Users",
            "A neural speech recognition system.",
            TopicDecision(False, "matched excluded term: hearing aid"),
        ),
        (
            "EEG Decoding",
            "A transformer for speech recognition from EEG.",
            TopicDecision(False, "matched excluded term: eeg"),
        ),
        (
            "A Survey of Speech Recognition",
            "We review hidden Markov model toolkits.",
            TopicDecision(False, "missing ML term"),
        ),
        (
            "Neural Machine Translation",
            "An encoder-decoder model for text.",
            TopicDecision(False, "missing ASR term"),
        ),
    ],
)
def test_gate_applies_legacy_relevance_rule(
    gate, paper: Paper, title: str, abstract: str, expected: TopicDecision
) -> None:
    assert gate(paper.model_copy(update={"title": title, "abstract": abstract})) == (
        expected
    )


def test_gate_matches_whole_words_only(gate, paper: Paper) -> None:
    # "asr" inside "Basra" and "neural" inside "neurally" are not matches.
    candidate = paper.model_copy(
        update={
            "title": "Neurally Inspired Dialect Maps of Basra",
            "abstract": "Transformer features for regional dialects.",
        }
    )

    assert gate(candidate) == TopicDecision(False, "missing ASR term")


def test_gate_is_case_insensitive(gate, paper: Paper) -> None:
    candidate = paper.model_copy(
        update={"title": "MULTILINGUAL ASR", "abstract": "SELF-SUPERVISED pretraining."}
    )

    assert gate(candidate).accepted
