---
identifier: semantic_scholar:790cbe493f4ac532cd3dfba5fd75eab02c3ecece
title: A Comprehensive Study of Residual CNNS for Acoustic Modeling in ASR
authors:
- Vitalii Bozheniuk
- Albert Zeyer
- Ralf Schlüter
- H. Ney
published: '2020-05-01T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/790cbe493f4ac532cd3dfba5fd75eab02c3ecece
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Long short-term memory (LSTM) networks are the dominant architecture for large vocabulary continuous speech recognition (LVCSR) acoustic modeling due to their good performance. However, LSTMs are hard to tune and computationally expensive. To build a system with lower computational costs and which allows online streaming applications, we explore convolutional neural networks (CNN). To the best of our knowledge there is no overview on CNN hyper-parameter tuning for LVCSR in the literature, so we present our results explicitly. Apart from recognition performance, we focus on the training and evaluation speed and provide a time-efficient setup for CNNs. We faced an overfitting problem in training and solved it with data augmentation, namely SpecAugment. The system achieves results competitive with the top LSTM results. We significantly increased the speed of CNN in training and decoding approaching the speed of the offline LSTM.
