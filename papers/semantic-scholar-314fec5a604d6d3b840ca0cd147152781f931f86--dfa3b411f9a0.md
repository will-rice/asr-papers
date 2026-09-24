---
identifier: semantic_scholar:314fec5a604d6d3b840ca0cd147152781f931f86
title: Cumulative Attention Based Streaming Transformer ASR with Internal Language Model Joint Training and Rescoring
authors:
- Mohan Li
- Cong-Thanh Do
- R. Doddipatla
published: '2023-06-04T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/314fec5a604d6d3b840ca0cd147152781f931f86
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

This paper presents an approach to improve the performance of streaming Transformer ASR by introducing an internal language model (ILM) as a part of the decoder layers. In the recently pro- posed cumulative attention (CA) based streaming ASR system, only the last or top few decoder layers are equipped with the CA module. Thus in this work, we propose to train the bottom (non-CA) layers as an ILM using an auxiliary LM loss jointly with the rest of the system. During inference, the outputs of the ILM are interpolated with those of the entire Transformer decoder as done in the conventional external language model (ELM) rescoring. The paper also proposes a refinement to the CA algorithm known as CTC look-ahead, in order to improve the precision of endpoint detection. Experiments conducted on AIShell-1, Aidatatang and Librispeech datasets show that the proposed ILM rescoring method achieves on par or better ASR performance when compared to the ELM rescoring baseline. Also, the CTC look-ahead strategy effectively alleviates the early end-of- speech (EOS) triggering issue suffered by the CA module, without bringing noticeable latency degradation.
