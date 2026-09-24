---
arxiv_id: s2:505d9f862052756a071871f6c5faf3f6f1c13496
title: Context-Aware Two-Stage Training for Domain Generalization in Speech Separation
authors:
  - Wupeng Wang
  - Zexu Pan
  - Jingru Lin
  - Shuai Wang
  - Haizhou Li
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/505d9f862052756a071871f6c5faf3f6f1c13496
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-16T06:20:16+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Speech separation aims to isolate individual speech signals from multi-talker speech mixtures. Despite the impressive results on synthetic benchmarks, most systems suffer noticeable performance drop in face of real-world speech mixtures due to severe domain mismatch. To address this, we introduce a novel context-aware two-stage training scheme with iterative updates for speech separation models. In this training scheme, the conventional end-to-end architecture is replaced with a framework that contains a context extractor and a segregator. The two modules are trained iteratively to emulate the speech-separation process of the human auditory system. We evaluate the proposed training scheme through cross-domain experiments on both synthetic and real-world speech mixtures, and demonstrate that the proposed scheme effectively boosts separation quality across various domains without adaptation, as measured by signal quality metrics and word error rate (WER). Additionally, our ablation study on the real test set highlights that the perceptual objects, including phoneme and word representations from pretrained self-supervised learning (SSL) models, serve as effective training targets for separation models.
