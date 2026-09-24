---
arxiv_id: s2:b504e76dace098261d0b0a5bfff1c51db2aa8a8b
title:
  Development of Real-Time Oral Error Correction System for College English Classrooms
  Based on BERT
authors:
  - Y. M. Wu
submitted: "2026-08-13"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b504e76dace098261d0b0a5bfff1c51db2aa8a8b
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-20T06:22:37+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This paper presents a real-time oral error correction system for college English classrooms based on an acoustic-semantic fusion DistilBERT+Adapter architecture. Whisper-small is used for speech transcription, and ASR confidence scores and word-duration features are embedded directly into the BERT representation space to improve robustness against speech-recognition noise. The model jointly performs error localization through a CRF layer and error-type classification, and the resulting outputs guide a constrained decoding mechanism that generates Top-3 correction candidates. These candidates are subsequently re-ranked using a KenLM language model. The system is lightweight and efficient, containing only 44M parameters and achieving an inference latency of 190 ms. End-to-end evaluation shows a latency of 438 ± 52 ms, Accuracy@Top1 of 73.1%, F0.5 of 0.692, and a teacher rating of 4.2. Through adapter fine-tuning, knowledge distillation, and ONNX runtime optimization, the proposed system achieves strong noise robustness and generalization, offering a deployable solution for personalized oral English instruction and real-time acoustic-semantic signal processing.
