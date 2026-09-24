---
identifier: semantic_scholar:581280ae8d65eb65e75afbae7af05debce28e844
title: 'Learning How Long to Wait: Adaptively-Constrained Monotonic Multihead Attention for Streaming ASR'
authors:
- Jae-gyun Song
- Hajin Shim
- Eunho Yang
published: '2021-12-13T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/581280ae8d65eb65e75afbae7af05debce28e844
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Monotonic Multihead Attention, which allows multiple heads to learn their own alignments per head, shows great performance on simultaneous machine translation and streaming speech recognition. However, it causes high latency waiting for the slowest head. Some recent advances such as Head-Synchronous Beam Search Decoding and its learnable version Mutually-Constrained Monotonic Multihead Attention, try to address this issue by restricting the difference in times of chosen frames among multi-heads to a fixed waiting time threshold. In this paper, we hypothesis that the optimal threshold for high performance with low latency depends on the input sequence, and propose an adaptive algorithm that learns how long to wait depending on input tokens by introducing a threshold prediction module. We evaluate our approach on two benchmark datasets for online Automatic Speech Recognition task and demonstrate that our method reduces the latency together with even improving the recognition accuracy.
