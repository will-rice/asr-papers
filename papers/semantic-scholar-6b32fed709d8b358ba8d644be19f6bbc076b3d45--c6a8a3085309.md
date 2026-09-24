---
identifier: semantic_scholar:6b32fed709d8b358ba8d644be19f6bbc076b3d45
title: Phonetic RNN-Transducer for Mispronunciation Diagnosis
authors:
- Dan Zhang
- Soumya Saha
- Sarah Campbell
published: '2023-06-04T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/6b32fed709d8b358ba8d644be19f6bbc076b3d45
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Non-autoregressive models and, in particular, Connectionist Temporal Classification (CTC) models have been the most popular approaches towards mispronunciation detection and diagnosis (MDD) task. In this paper, we identify two important knowledge gaps in MDD that have not been well studied in existing MDD research. First, CTC-based MDD models often assume conditional independence in the predicted phonemes, and therefore prominent mispronunciation patterns are underutilized. Second, existing MDD approaches are constrained to use training data from a language-specific phoneme set, and therefore cannot distinguish accented sounds that are not present in the predefined phoneme set. In this paper, we propose a set of autoregressive phonetic Recurrent Neural Network Transducer (RNN-T) MDD models that are capable of capturing temporal dependence of mispronunciation patterns. We further devise an extended phoneme set and weakly supervised training strategy to allow the model to distinguish similar sounding phonemes from different languages. We evaluate the proposed method on the public L2-ARCTIC dataset. Results have shown the proposed phonetic RNN-T model achieves significant improvements in false acceptance rate compared to state-of-the-art methods.
