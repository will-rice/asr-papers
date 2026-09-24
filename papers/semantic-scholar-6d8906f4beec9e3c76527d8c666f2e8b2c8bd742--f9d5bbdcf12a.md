---
arxiv_id: s2:6d8906f4beec9e3c76527d8c666f2e8b2c8bd742
title:
  "LCMA-SRT: Language-Conditional Mixture-of-Experts Adapters for Joint Multilingual
  Speech Recognition and Translation"
authors:
  - Nan Li
  - Xiaoyong Guo
  - Hao Huang
  - Haihua Xu
  - Wei Shi
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/6d8906f4beec9e3c76527d8c666f2e8b2c8bd742
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-15T06:57:36+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Neural transducers offer an alignment-free framework for speech-to-text modeling, and hierarchical transducer architectures further improve multilingual joint automatic speech recognition (ASR) and speech translation (ST) by stacking a translation-focused encoder on top of an ASR encoder. However, extending hierarchical transducers to multilingual many-to-many settings remains challenging: fully shared models often suffer from negative transfer and unstable target-language generation, while training separate models for each direction is computationally prohibitive. We propose LCMA-SRT (Language-Conditional Mixture-of-Experts Adapters for Speech Recognition and Translation), which augments a hierarchical transducer with language-conditional Mixture-of-Experts (MoE) adapters. A source-conditioned MoE adapter (SRC-MoE) uses source-language embeddings to reduce cross-language interference and improve multilingual ASR. A target-conditioned MoE adapter (TGT-MoE) uses the desired target language to reduce cross-target interference and stabilize target-language generation in many-to-many ST. Experiments on Europarl-ST (9 languages, 72 directions) show that LCMA-SRT improves both ASR and ST within a single joint model, reducing average WER and improving BLEU and COMET over strong hierarchical transducer baselines. We release our code and models at https:
