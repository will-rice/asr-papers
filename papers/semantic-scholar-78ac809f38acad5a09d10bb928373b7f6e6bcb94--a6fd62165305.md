---
arxiv_id: s2:78ac809f38acad5a09d10bb928373b7f6e6bcb94
title: "KNN-CTC$+$: Retrieval-Augmented Decoding for Robust CTC-Based ASR"
authors:
  - Jiaming Zhou
  - Shiwan Zhao
  - Hui Wang
  - Haoqin Sun
  - Wenjia Zeng
  - Yong Chen
  - Yong Qin
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/78ac809f38acad5a09d10bb928373b7f6e6bcb94
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-29T07:30:12+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Retrieval-augmented methods complement parametric models with non-parametric memory and have shown strong adaptability in natural language processing. Extending this paradigm to automatic speech recognition (ASR) is appealing but challenging, particularly at the frame level where precise alignments are difficult to obtain and large-scale audio-text datastores impose heavy storage and retrieval costs. We present <bold><inline-formula><tex-math notation="LaTeX">$k$</tex-math></inline-formula>NN-CTC <inline-formula><tex-math notation="LaTeX">$+$</tex-math></inline-formula></bold>, a retrieval-augmented decoding framework for CTC-based ASR that addresses these challenges. To construct fine-grained datastores without external supervision, <inline-formula><tex-math notation="LaTeX">$k$</tex-math></inline-formula> NN-CTC <inline-formula><tex-math notation="LaTeX">$+$</tex-math></inline-formula> leverages CTC encoder embeddings as keys and frame-level pseudo labels as values. To reduce redundancy, we propose a blank-aware pruning strategy that removes <monospace><blank></monospace> frames during both datastore construction and query-time retrieval, improving efficiency while retaining informative evidence. Beyond alignment and scale issues, domain mismatch remains a major obstacle. <inline-formula><tex-math notation="LaTeX">$k$</tex-math></inline-formula> NN-CTC <inline-formula><tex-math notation="LaTeX">$+$</tex-math></inline-formula> introduces a lightweight <italic>unsupervised domain adaptation</italic> (UDA) pipeline: confidence-based filtering discards unreliable pseudo labels when building target-specific datastores, and a dynamic interpolation strategy adaptively balances model predictions and <inline-formula><tex-math notation="LaTeX">$k$</tex-math></inline-formula> NN retrievals based on neighbor confidence. These designs enable robust test-time adaptation without labeled data or parameter updates. Experiments on mandarin, Chinese dialect, child and elderly speech datasets demonstrate consistent accuracy gains and improved robustness under domain shifts. <inline-formula><tex-math notation="LaTeX">$k$</tex-math></inline-formula>NN-CTC<inline-formula><tex-math notation="LaTeX">$+$</tex-math></inline-formula> provides a scalable, effective solution for enhancing CTC-based ASR.
