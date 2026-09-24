---
arxiv_id: s2:f8ae264ceca2cf737de71b1ba59083b9a31e9efc
title:
  Hybrid RNN-T/Attention-Based Streaming ASR with Triggered Chunkwise Attention
  and Dual Internal Language Model Integration
authors:
  - Takafumi Moriya
  - Takanori Ashihara
  - Atsushi Ando
  - Hiroshi Sato
  - Tomohiro Tanaka
  - Kohei Matsuura
  - Ryo Masumura
  - Marc Delcroix
  - T. Shinozaki
submitted: "2022-05-23"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/f8ae264ceca2cf737de71b1ba59083b9a31e9efc
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:27:39+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

In this paper we propose improvements to our recently proposed hybrid RNN-T/Attention architecture that includes a shared encoder followed by recurrent neural network-transducer (RNN-T) and triggered attention-based decoders (TAD). The use of triggered attention enables the attention-based decoder (AD) to operate in a streaming manner. When a trigger point is detected by RNN-T, TAD uses the context from the start-of-speech up to that trigger point to compute the attention weights. Consequently, the computation costs and the memory consumptions are quadratically increased with the duration of the utterances because all input features must be stored and used to re-compute the attention weights. In this paper, we use a short context from a few frames prior to each trigger point for attention weight computation resulting in reduced computation and memory costs. We call the proposed framework triggered chunkwise AD (TCAD). We also investigate the effectiveness of internal language model (ILM) estimation approach using both ILMs of RNN-T and TCAD heads for improving RNN-T performance. We confirm in experiments with public and private datasets covering various scenarios that TCAD achieves superior recognition performance while reducing computation costs compared to TAD.
