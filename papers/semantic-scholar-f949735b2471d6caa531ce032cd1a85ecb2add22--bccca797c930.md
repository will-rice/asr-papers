---
identifier: semantic_scholar:f949735b2471d6caa531ce032cd1a85ecb2add22
title: Regarding the Existence of the Internal Language Model in CTC-Based E2E ASR
authors:
- Zeyu Zhao
- Peter Bell
published: '2025-04-06T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/f949735b2471d6caa531ce032cd1a85ecb2add22
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Some End-to-End (E2E) Automatic Speech Recognition (ASR) models, such as Attention-based Encoder-Decoder (AED) and Recurrent Neural Network Transducer (RNN-T) are known to have components that effectively act as internal language models (ILM), implicitly modelling the prior probability of the output sequence. However, the existence of an ILM in pure Connectionist Temporal Classification (CTC) ASR systems remains debated. In this paper, we investigate the existence and strength of an ILM in CTC systems. Since CTC posterior probabilities cannot be analytically factorised, we propose a novel empirical method to probe the ILM. After validating our method on a hybrid DNN model with various external language models, we apply it to CTC models trained under different conditions, examining the effects of training data, modelling units, and training or pre-training methods. Our results show no strong evidence of an ILM in CTC-based ASR systems, even with the largest training dataset in our experiments. However, we make the surprising finding that when a CTC encoder is jointly trained with an AED loss, an ILM emerges, even when only the CTC component is used in decoding.
