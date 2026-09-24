---
arxiv_id: s2:8db532fe1ae4fbaec64fa2ec433d216d78d34b47
title: Improved Hybrid Streaming ASR with Transformer Language Models
authors:
  - Pau Baquero-Arnal
  - Javier Jorge
  - Adrià Giménez
  - J. Silvestre-Cerdà
  - Javier Iranzo-Sánchez
  - A. Sanchís
  - Jorge Civera Saiz
  - Alfons Juan-Císcar
submitted: "2020-10-25"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/8db532fe1ae4fbaec64fa2ec433d216d78d34b47
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:52:51+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Streaming ASR is gaining momentum due to its wide applicability, though it is still unclear how best to come close to the accuracy of state-of-the-art off-line ASR systems when the output must come within a short delay after the incoming audio stream. Following our previous work on streaming one-pass decoding with hybrid ASR systems and LSTM language models, in this work we report further improvements by replacing LSTMs with Transformer models. First, two key ideas are discussed so as to run these models fast during inference. Then, empirical results on LibriSpeech and TED-LIUM are provided showing that Transformer language models lead to improved recognition rates on both tasks. ASR systems obtained in this work can be seamlessly transfered to a streaming setup with minimal quality losses. Indeed, to the best of our knowledge, no better results have been reported on these tasks when assessed under a streaming setup.
