---
arxiv_id: s2:62c0b4f0e55b79fe629bc4b5fb94f34b4c8779fd
title:
  "RVQ-SNER: End-to-End Chinese Speech Named Entity Recognition via Quantized
  Acoustic Bottlenecks and Deep Acousticâ€“Semantic Fusion"
authors:
  - Yaoqiang Zhou
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/62c0b4f0e55b79fe629bc4b5fb94f34b4c8779fd
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-10T06:40:21+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Conventional Speech Named Entity Recognition (SNER) typically relies on cascaded ASR (Automatic Speech Recognition)+NER (Named Entity Recognition) pipelines, which are hindered by error propagation and the underutilisation of acoustic cues. We propose an end-to-end Chinese SNER framework using Residual Vector Quantisation (RVQ) and deep acoustic--semantic fusion. The model extracts speech representations via a frozen Wav2Vec2-XLSR encoder, employing an RVQ-based bottleneck to reconstruct continuous quantized features that regularize the acoustic space and preserve semantic content. A Transformer decoder, trained with a joint CTC-attention objective, performs transcription while a gated deep-fusion mechanism integrates an external GPT model for linguistic consistency. For NER, a bidirectional multimodal fusion module aligns acoustic and semantic features before a GlobalPointer head performs span-level prediction. Experiments on AISHELL-NER and CNERTA yield F1-scores of 90.91\% and 81.44\%, respectively, outperforming pipeline, multimodal, and E2E baselines. These results demonstrate that deep bidirectional interaction between quantized acoustic streams and semantic contexts is essential for mitigating ASR error propagation and achieving robust Chinese SNER.
