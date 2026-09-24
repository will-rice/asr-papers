---
arxiv_id: s2:4db2063a3bd0ae621a1b8d177d098e84c0a45844
title: Streaming End-to-End Speech Recognition for Hybrid RNN-T/Attention Architecture
authors:
  - Takafumi Moriya
  - Tomohiro Tanaka
  - Takanori Ashihara
  - Tsubasa Ochiai
  - Hiroshi Sato
  - Atsushi Ando
  - Ryo Masumura
  - Marc Delcroix
  - Taichi Asami
submitted: "2021-08-30"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/4db2063a3bd0ae621a1b8d177d098e84c0a45844
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

We present a novel architecture with its decoding approach for improving recurrent neural network-transducer (RNN-T) performance. RNN-T is promising for building time-synchronous automatic speech recognition (ASR) systems and thus enhancing streaming ASR applications. We note that encoder-decoder-based sequence-to-sequence models (S2S) have been also used successfully by the ASR community. In this paper, we integrate these popular models in the RNN-T+S2S approach; higher recognition performance than either is achieved due to their integration. However, it is generally deemed to be complicated to use S2S in streaming systems, because the attention mechanism can use arbitrarily long past and future contexts during decoding. Our RNN-T+S2S is composed of the shared encoder, an RNN-T decoder and a triggered attention-based decoder which uses time restricted encoder outputs for attention weight computation. By using the trigger points generated from RNN-T outputs, the S2S branch of RNN-T+S2S activates only when the triggers are detected, which makes streaming ASR practical. Experiments on public and private datasets created to research various tasks demonstrate that our proposal can yield superior recognition performance.
