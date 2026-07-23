---
arxiv_id: s2:2eb99bc21d5bc64bd6cfc333006204c889c5328d
title:
  "Evaluating ASR Pipeline Configurations for Kazakh: Implications for Low-Resource
  Turkic Languages"
authors:
  - Nursultan Nyssanov
  - L. Rzayeva
  - Alisher Batkuldin
  - Zhaksylyk Kozhakhmet
submitted: "2026-07-15"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/2eb99bc21d5bc64bd6cfc333006204c889c5328d
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-23T07:05:07+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Kazakh automatic speech recognition (ASR) presents a persistent challenge for large-scale multilingual models. This paper presents a systematic evaluation of 27 ASR pipeline configurations (three ASR models × three VAD methods × three post-processing strategies) on the Kazakh Speech Dataset (KSD), examining the contribution of model fine-tuning, voice activity detection (VAD) preprocessing, and large language model (LLM) post-correction and benchmarking the resulting pipelines against two non-Whisper foundation models. Language-specific fine-tuning reduces Word Error Rate (WER) from 43.20% (generic Whisper-large-v3) to 11.88% (Kazakh fine-tuned Whisper-turbo), a 31.32-percentage-point absolute reduction (72.5% relative; p < 0.001, bootstrap test); the effect persists after controlling for model size (generic Whisper-large-v3-turbo, 18.92%, vs. the same architecture after fine-tuning, 11.88%; p < 0.001). VAD preprocessing consistently degrades performance. Zero-shot post-correction with general-purpose LLMs yields no benefit and adds substantial latency: Gemma-2-9B and Qwen2.5-7B raise WER by 5.5 and 7.2 percentage points at real-time factors of 0.52 and 0.30, and a larger 32B model still degrades accuracy (+10.8 points), indicating that scale is not the limiting factor. Among all systems evaluated, a larger multilingual foundation model, SeamlessM4T-v2 (9.72% WER), outperforms the fine-tuned Whisper, showing that for Kazakh model coverage matters more than pipeline engineering. Character-level error analysis identifies systematic confusion between Kazakh-specific and Russian Cyrillic characters as a dominant error source. These findings establish that, for Kazakh under the evaluated conditions, model choice dominates pipeline add-ons: fine-tuning is essential, VAD and zero-shot LLM correction consistently hurt, and a strong multilingual model sets the best result; we further discuss the extent to which these conclusions extend to typologically similar Kipchak-Turkic languages.
