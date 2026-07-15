---
arxiv_id: s2:3a58394dedf4f02a7ca9f8b9934e8a5fd2f1fd43
title: Trilevel Supervised, Unsupervised, and Distilled Learning for Speech Recognition
authors:
  - Jen-Tzung Chien
  - Yu-chun Lin
  - Xiaodong Cui
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/3a58394dedf4f02a7ca9f8b9934e8a5fd2f1fd43
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

In this paper, we propose TL-SUD, a trilevel learning framework that unifies supervised, unsupervised and distillation objectives for automatic speech recognition. Unlike two-stage approaches that perform unsupervised pre-training followed by joint fine-tuning with supervised and knowledge distillation objectives, TL-SUD jointly optimizes all three loss functions within a unified process. This enables the acoustic model to learn representations that combine the generalization capability from unlabeled data, the task-specific alignment from labeled data, and the knowledge distillation from a teacher model. To solve the trilevel optimization problem, we sequentially apply penalty-based bilevel gradient descent, first collapsing the lower and middle-levels into a single-level problem and then solving the resulting bilevel structure involving the upper-level. The effectiveness of the proposed framework is evaluated on the LibriSpeech and English Common Voice datasets. We adopt FastConformer as the model backbone, with a supervised connectionist temporal classification loss, an unsupervised contrastive loss, and a feature-based distillation loss. The results show that TL-SUD outperforms both the commonly adopted two-stage pre-training and fine-tuning approach and the weighted-sum methods of the three objectives.
