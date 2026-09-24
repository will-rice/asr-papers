---
arxiv_id: s2:b90ac0931e6b60662e684a7e92c07d2e3ee84518
title: Dynamic Diffusion Programming and Classification
authors:
  - Jen-Tzung Chien
  - Chia-Kai Yeh
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b90ac0931e6b60662e684a7e92c07d2e3ee84518
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

Connectionist temporal classification (CTC) has been achieving remarkable performance in utilization of neural networks to recognize sequence data like speech signal due to its simplicity, efficiency and stability. The challenging issues in CTC include assuming the conditional temporal independence and tackling the balance between accuracy and efficiency. This paper deals with these two issues by incorporating a probabilistic diffusion model into a non-autoregressive CTC for a new end-to-end automatic speech recognition (ASR). By leveraging the iterative denoising neural network for temporal classification, this method consolidates the dependency modeling in token alignments while maintaining the inference efficiency. In particular, a dynamic diffusion programming algorithm is proposed to implement an efficient computation for optimization where the diffusion objective is calculated over different alignments. Additionally, this study exploits a fast sampling strategy in reverse process, which reduces the latency by skipping those low-confidence diffusion steps. The proposed methods considerably mitigate the computation complexities in diffusion objective and sampling procedure for a discrete-diffusion ASR. The experiments on LibriSpeech and Common Voice datasets show the effectiveness and efficiency in terms of word/character error rates and real-time factors. Non-autoregressive generation and sampling via a token-wise probabilistic diffusion is demonstrated to tradeoff between accuracy and efficiency.
