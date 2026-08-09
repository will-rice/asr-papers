---
arxiv_id: s2:8519f5e45ab01eef747821be791c6be141808fab
title: A Unified Perspective on CTC and Soft-DTW Using Differentiable DTW
authors:
  - Johannes Zeitler
  - Meinard Müller
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/8519f5e45ab01eef747821be791c6be141808fab
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-09T06:29:37+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Training deep neural networks on unaligned sequence data is fundamental to tasks such as automatic speech recognition, lyrics alignment, and music transcription. Strongly aligned annotations, which provide frame-level correspondences between input and target sequences, are often costly, impractical, or unreliable. In contrast, weakly aligned annotations, which specify only segment-level alignment, are more scalable and easier to obtain, but present challenges for training and supervision. A widely used technique for handling weakly aligned data is Connectionist Temporal Classification (CTC). While CTC enables end-to-end training without explicit alignments, it is difficult to interpret, structurally rigid, and relies on a special blank symbol to handle label repetitions. The main contribution of this work is to explore the relationship between CTC and the less commonly used but conceptually simpler Soft Dynamic Time Warping (SDTW), which offers a more intuitive and flexible approach to weak alignment. We introduce a generalization of SDTW that incorporates cell-wise step weights, variable step sizes, and flexible boundary conditions. We refer to this extended framework as Differentiable Dynamic Time Warping (dDTW), which naturally subsumes CTC and SDTW as special cases and provides a unified perspective on these alignment-based losses. We systematically compare SDTW, CTC, and related variants in two controlled and illustrative tasks from music information retrieval, analyzing prediction accuracy, training stability, alignment behavior, and the implications of the blank symbol, in both single- and multi-label problems.
