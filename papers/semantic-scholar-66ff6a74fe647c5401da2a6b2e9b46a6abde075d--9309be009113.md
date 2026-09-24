---
identifier: semantic_scholar:66ff6a74fe647c5401da2a6b2e9b46a6abde075d
title: Improving Transducer-Based Spoken Language Understanding With Self-Conditioned CTC and Knowledge Transfer
authors:
- Vishal Sunder
- E. Fosler-Lussier
published: '2024-12-02T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/66ff6a74fe647c5401da2a6b2e9b46a6abde075d
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

In this paper, we propose to improve end-to-end (E2E) spoken language understand (SLU) in an RNN transducer model (RNN-T) by incorporating a joint self-conditioned CTC automatic speech recognition (ASR) objective. Our proposed model is akin to an E2E differentiable cascaded model which performs ASR and SLU sequentially and we ensure that the SLU task is conditioned on the ASR task by having CTC self conditioning. This novel joint modeling of ASR and SLU improves SLU performance significantly over just using SLU optimization. We further improve the performance by aligning the acoustic embeddings of this model with the semantically richer BERT model. Our proposed knowledge transfer strategy makes use of a bag-of-entity prediction layer on the aligned embeddings and the output of this is used to condition the RNN-T based SLU decoding. These techniques show significant improvement over several strong baselines and can perform at par with large models like Whisper with significantly fewer parameters.
