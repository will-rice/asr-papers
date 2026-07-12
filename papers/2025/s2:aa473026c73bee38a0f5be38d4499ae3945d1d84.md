---
arxiv_id: s2:aa473026c73bee38a0f5be38d4499ae3945d1d84
title:
  Leveraging IPA and Articulatory Features as Effective Inductive Biases for
  Multilingual ASR Training
authors:
  - Jaeyoung Lee
  - M. Mimura
  - Tatsuya Kawahara
submitted: "2025-04-06"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/aa473026c73bee38a0f5be38d4499ae3945d1d84
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:45:01+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

In recent advancements in end-to-end ASR, large-scale self-supervised or weakly supervised models have achieved a significant milestone. However, it remains challenging to train consistently high-performing multilingual models, transferable to languages without much resource. In this study, we propose embedding universal phonological knowledge to multilingual ASR by predicting international phonetic alphabet (IPA) targets and universal articulatory features alongside primary grapheme targets. These additions are expected to provide effective inductive bias or regularization for predicting grapheme targets across various languages. In the experiments, which involve fine-tuning a pre-trained XLS-R model using 10,400 hours of data across 120 languages from the Common Voice corpus, our proposed method achieved a 6.81% relative reduction in character error rate.
