---
arxiv_id: s2:dd8b6d162afb475bd44fbad52772f597d42699fd
title:
  Self-Adaptive Multilingual ASR Rescoring with Language Identification and Unified
  Language Model
authors:
  - Zhuo Gong
  - D. Saito
  - Longfei Yang
  - T. Shinozaki
  - Sheng Li
  - H. Kawai
  - N. Minematsu
submitted: "2022-06-28"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/dd8b6d162afb475bd44fbad52772f597d42699fd
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:26:11+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Language Models (LM) can be used in automatic speech recognition (ASR) rescoring to select the hypothesis with the fewest errors. While in multilingual ASR, multiple LMs might be used based on language identification (LID) given by the multilingual ASR outputs. However, in the traditional shallow fusion method, a static LM weight is determined by a development set. This static weight might not fulfill the situations of all languages in test data. And for multiple LMs, different weight needs to be searched for each LM. Instead, A unified multilingual LM will receive a LID token at the beginning of its auto-regressive predicting to decide which language to decode, so that merely one weight is necessary for LM rescoring. Then, we propose a multilingual ASR rescoring method which dynamically tunes the LM weight during decoding to optimize the balance between the end-to-end (E2E) multilingual ASR model and the LM according to the LM’s entropy and logits score as model confidence metrics. With this method, resources for search the best hyperparameter LM weight can also be saved. The experiments are mainly conducted on Common voice and Voxforge corpora. The results show that this method can reach the performance of the best static LM weight and even defeat it in several languages with no hyperparameter to be tuned and nearly zero overhead.
