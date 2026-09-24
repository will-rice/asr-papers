---
arxiv_id: s2:6393db2985169ccbe328095e13887b25aa660a9f
title: "ADASTT: Adaptive Speech-to-Text Algorithm Selection via Meta-Learning"
authors:
  - A. Namlı
  - Onurhan Çelik
  - Eray Yapagci
  - S. Kozat
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/6393db2985169ccbe328095e13887b25aa660a9f
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-13T07:18:10+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

We introduce ADASTT, an adaptive meta-learning framework that selects, in real time, the most suitable speech-to-text (STT) model for each incoming audio input. Factors such as background noise, speaker accent, speaking rate, and recording quality cause different STT models to perform better on different inputs. Exhaustively running every model is computationally expensive and inefficient, whereas committing to a single model degrades accuracy. ADASTT addresses this trade-off by computing a lightweight feature vector for each audio input capturing noise level, speaker traits, temporal dynamics, and signal quality and passing it to a probabilistic meta-learner. The meta-learner assigns a probability distribution over candidate STT models and samples a single model to transcribe the audio input. Experiments show that ADASTT consistently reduces the Word Error Rate (WER) across heterogeneous conditions. On the AMI Meeting corpus, which exhibits high acoustic variability, ADASTT achieves a relative WER reduction of 10.6% over traditional fusion methods while being 2.7× faster than standard ROVER fusion. End-to-end ADASTT is approximately 26.5% faster on average than Whisper Large v3 using much smaller S2T algorithms. The framework is learner-agnostic and meta learner or base STT models can be used. We also present boosting-based and neural learners and provide proofs of convergence to a first-order stationary point under mild regularity conditions.
