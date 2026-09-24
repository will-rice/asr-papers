---
identifier: semantic_scholar:eb198d4bddab6c3f542863bd8bb533c3bfcd463d
title: Efficient Cascaded Streaming ASR System Via Frame Rate Reduction
authors:
- Xingyu Cai
- David Qiu
- Shaojin Ding
- Dongseong Hwang
- Weiran Wang
- A. Bruguier
- Rohit Prabhavalkar
- Tara N. Sainath
- Yanzhang He
published: '2023-12-16T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/eb198d4bddab6c3f542863bd8bb533c3bfcd463d
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

In this paper, we explore various frame rate reduction schemes on the two-pass cascaded encoder model to improve its efficiency without scarifying the transcription quality. We conduct extensive studies on frame rate reduction strategies, left and right context window length, trade-offs in quality, latency, computation and power consumption, and performance in short-and long-form datasets. With the proposed schemes, we can lower the 2nd pass frame rate to $120 \mathrm{~ms}$, half of the 1st pass’s. This achieves $20 \%$ RTF reduction / $13 \%$ power saving / $19 \%$ lower final latency, without impact on the word-error-rate nor partial results’ latency. If allowing partial latency increase, we can further reduce the frame rate to $180 \mathrm{~ms}$ or even $240 \mathrm{~ms}$ from the 1st pass, and obtain $45 \%$ RTF / 35% power savings, with a similar or even better (on the short-form testset) recognition accuracy.
