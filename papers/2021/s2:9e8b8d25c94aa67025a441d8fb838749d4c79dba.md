---
arxiv_id: s2:9e8b8d25c94aa67025a441d8fb838749d4c79dba
title:
  Improving RNN-T for Domain Scaling Using Semi-Supervised Training with Neural
  TTS
authors:
  - Yan Deng
  - Rui Zhao
  - Zhong Meng
  - Xie Chen
  - Bing Liu
  - Jinyu Li
  - Yifan Gong
  - Lei He
submitted: "2021-08-30"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/9e8b8d25c94aa67025a441d8fb838749d4c79dba
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:39:20+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Recurrent neural network transducer (RNN-T) has shown to be comparable with conventional hybrid model for speech recognition. However, there is still a challenge in out-of-domain scenarios with context or words different from training data. In this paper, we explore the semi-supervised training which optimizes RNN-T jointly with neural text-to-speech (TTS) to better generalize to new domains using domain-speciﬁc text data. We apply the method to two tasks: one with out-of-domain context and the other with signiﬁcant out-of-vocabulary (OOV) words. The results show that the proposed method signiﬁcantly improves the recognition accuracy in both tasks, resulting in 61.4% and 53.8% relative word error rate (WER) reductions respectively, from a well-trained RNN-T with 65 thousand hours of training data. We do further study on the semi-supervised training methodology: 1) which modules of RNN-T model to be updated; 2) the impact of using different neural TTS models; 3) the performance of using text with different relevancy to target domain. Finally, we compare several RNN-T customization methods, and conclude that semi-supervised training with neural TTS is comparable and complementary with Internal Language Model Estimation (ILME) or biasing.
