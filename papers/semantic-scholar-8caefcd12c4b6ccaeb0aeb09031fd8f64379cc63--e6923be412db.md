---
arxiv_id: s2:8caefcd12c4b6ccaeb0aeb09031fd8f64379cc63
title:
  Conformer-Based on-Device Streaming Speech Recognition with KD Compression
  and Two-Pass Architecture
authors:
  - Jinhwan Park
  - Sichen Jin
  - Junmo Park
  - Sungsoo Kim
  - Dhairya Sandhyana
  - Chang-heon Lee
  - Myoungji Han
  - Jungin Lee
  - Seokyeong Jung
  - C. Han
  - Chanwoo Kim
submitted: "2023-01-09"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/8caefcd12c4b6ccaeb0aeb09031fd8f64379cc63
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:18:10+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This paper introduces a two-pass on-device automatic speech recognition (ASR) system, which is developed for commercialized devices. The first pass of the system is based on a causal Conformer-transducer model to generate partial results from the input audio stream. After processing an entire input utterance in the first pass, the candidates for the final result are rescored with a full-context attention model in the second pass. To minimize the computational overhead from rescoring, we compress the full-context model by applying knowledge distillation (KD). The total model size is reduced by 35% after KD with a 0.02% absolute loss in word error rate (WER). We also introduce decoding techniques to boost the accuracy on the test cases mismatched with the distribution of the training set. The techniques include on-device personal adaptation, spell correction and handling incorrectly segmented speech, which solve the critical issues for production-grade systems. The whole system including the two-pass end-to-end (E2E) model and a language model (LM) occupies 72MB in storage after 8-bit quantization. We demonstrate the entire system on mobile devices and report results on test sets collected from the production environment. The developed system achieves 5.65% WER which surpasses the baseline system with 39% relative WER improvement.
