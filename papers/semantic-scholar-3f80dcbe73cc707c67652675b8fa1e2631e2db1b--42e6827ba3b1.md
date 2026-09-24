---
arxiv_id: s2:3f80dcbe73cc707c67652675b8fa1e2631e2db1b
title:
  "ViTSTR-Transducer: Cross-Attention-Free Vision Transformer Transducer for
  Scene Text Recognition"
authors:
  - Rina Buoy
  - M. Iwamura
  - Sovila Srun
  - Koichi Kise
submitted: "2023-12-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/3f80dcbe73cc707c67652675b8fa1e2631e2db1b
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:03:57+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Attention-based encoder–decoder scene text recognition (STR) architectures have been proven effective in recognizing text in the real world, thanks to their ability to learn an internal language model. Nevertheless, the cross-attention operation that is used to align visual and linguistic features during decoding is computationally expensive, especially in low-resource environments. To address this bottleneck, we propose a cross-attention-free STR framework that still learns a language model. The framework we propose is ViTSTR-Transducer, which draws inspiration from ViTSTR, a vision transformer (ViT)-based method designed for STR and the recurrent neural network transducer (RNN-T) initially introduced for speech recognition. The experimental results show that our ViTSTR-Transducer models outperform the baseline attention-based models in terms of the required decoding floating point operations (FLOPs) and latency while achieving a comparable level of recognition accuracy. Compared with the baseline context-free ViTSTR models, our proposed models achieve superior recognition accuracy. Furthermore, compared with the recent state-of-the-art (SOTA) methods, our proposed models deliver competitive results.
