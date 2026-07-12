---
arxiv_id: s2:82241d2062ffef8e99f4d5e22b5ce690c8f6a122
title: MLLP-VRAIN Spanish ASR Systems for the Albayzin-RTVE 2020 Speech-To-Text Challenge
authors:
  - Javier Jorge
  - Adrià Giménez
  - Pau Baquero-Arnal
  - Javier Iranzo-Sánchez
  - A. Pérez
  - Gonçal V. Garcés Díaz-Munío
  - J. Silvestre-Cerdà
  - Jorge Civera Saiz
  - A. Sanchís
submitted: "2021-03-24"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/82241d2062ffef8e99f4d5e22b5ce690c8f6a122
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:46:56+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This paper describes the automatic speech recognition (ASR) systems built by the MLLP-VRAIN research group of Universitat Polit`ecnica de Val`encia for the Albayzin-RTVE 2020 Speech-to-Text Challenge. The primary system ( p-streaming 1500ms nlt ) was a hybrid BLSTM-HMM ASR system using streaming one-pass decoding with a context window of 1.5 seconds and a linear combination of an n-gram, a LSTM, and a Transformer language model (LM). The acoustic model was trained on nearly 4,000 hours of speech data from different sources, using the MLLP’s transLectures-UPV toolkit (TLK) and TensorFlow; whilst LMs were trained using SRILM (n-gram), CUED-RNNLM (LSTM), and Fairseq (Transformer), with up to 102G tokens. This system achieved 11.6% and 16.0% WER on the test-2018 and test-2020 sets, respectively. As it is streaming-enabled, it could be put into production environments for automatic captioning of live media streams, with a theoretical delay of 1.5 seconds. Along with the primary system, we also submitted three contrastive systems. From these, we highlight the system c2-streaming 600ms t that, following the same conﬁguration of the primary one, but using a smaller context window of 0.6 seconds and a Transformer LM, scored 12.3% and 16.9% WER points respectively on the same test sets, with a measured empirical latency of 0.81 ± 0.09 seconds (mean ± stdev). This is, we ob- tained state-of-the-art latencies for high-quality automatic live captioning with a small WER degradation of 6% relative.
