---
identifier: semantic_scholar:7c0c9d8c446c1619912b1f543fdc3a15955e1ac2
title: Knowledge Distillation via Module Replacing for Automatic Speech Recognition with Recurrent Neural Network Transducer
authors:
- Kaiqi Zhao
- H. Nguyen
- Animesh Jain
- Nathan Susanj
- A. Mouchtaris
- Lokesh
- A Gupta
- Ming Zhao
published: '2022-09-18T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/7c0c9d8c446c1619912b1f543fdc3a15955e1ac2
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Automatic Speech Recognition (ASR) is increasingly used by edge applications such as intelligent virtual assistants. However, state-of-the-art ASR models such as Recurrent Neural Network - Transducer (RNN-T) are computationally intensive on resource-constrained edge devices. Knowledge Distillation (KD) is a promising approach to compress large models by us-ing a large model (”teacher”) to train a small model (”student”). This paper proposes a novel KD method called Log-Curriculum based Module Replacing (LCMR) for RNN-T. LCMR compresses RNN-T and addresses its unique characteristics by re-placing teacher modules including multiple LSTM/Dense layers with substitutional student modules that contain less Long Short Term Memory (LSTM)/Dense layers. LCMR employs a novel nonlinear Curriculum Learning driven replacement strategy to further improve the performance by updating replacing rates with a dynamic, smoothing mechanism. Under LCMR, the student and teacher are able to interact at gradient level, and tranfser knowledge more effectively than conventional KD. Evaluation shows that LCMR reduces word-error-rate (WER) by 14.47%-33.24% relative compared to conventional KD.
