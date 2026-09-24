---
identifier: semantic_scholar:364c49cbcf5850ed33b7894e1ccb23f8a40fda3c
title: Uncertainty-Based Streaming ASR With Evidential Deep Learning
authors:
- Hiroaki Sato
- Asahi Sakuma
- Ryuga Sugano
- Tadashi Kumano
- Yoshihiko Kawai
- Shinji Watanabe
- Tetsuji Ogawa
published: '2026-01-01T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/364c49cbcf5850ed33b7894e1ccb23f8a40fda3c
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Attention-based encoder-decoder (AED) models achieve high accuracy in offline automatic speech recognition (ASR), but their application to streaming remains challenging due to the lack of mechanisms for regulating token emission. Existing approaches include monotonic attention, forced alignment with external models providing token-level boundaries, and encoder-based emission control methods. However, these methods either require structural modifications, complicate the training pipeline, or show limited accuracy. In addition, local agreement has been proposed as a method enabling streaming without retraining, but it incurs fixed delays corresponding to the input window size and premature commitments. To address these limitations, we propose Evidential Streaming TRAnsformer (ESTRA), a framework that leverages evidential deep learning (EDL) to estimate uncertainty. ESTRA models token probabilities with a Dirichlet distribution and introduces hierarchical and direct Kullback–Leibler divergence losses to ensure uncertainty decreases progressively as more speech is observed. During inference, token emission is controlled by comparing uncertainty against a threshold, suppressing premature outputs without fixed delays. Experiments on the LibriSpeech benchmark show that ESTRA achieves streaming performance comparable to offline AED models, surpasses local agreement in robustness under small input windows, and reduces 50th-percentile latency by avoiding fixed window-size delays, while leaving room for improvement at the 90th percentile. Furthermore, it provides more reliable control of token emission than probability- or entropy-based baselines, demonstrating the effectiveness of uncertainty as an indicator. ESTRA offers a promising approach to streaming ASR, with results supporting the effectiveness of uncertainty-driven token emission.
