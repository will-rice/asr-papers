---
identifier: semantic_scholar:f665c1961f53412ca84cdf1b8baa3b86cefd37ea
title: Live Streaming Speech Recognition Using Deep Bidirectional LSTM Acoustic Models and Interpolated Language Models
authors:
- Javier Jorge
- Adrià Giménez
- J. Silvestre-Cerdà
- Jorge Civera Saiz
- A. Sanchís
- A. Juan
published: '2022-01-01T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/f665c1961f53412ca84cdf1b8baa3b86cefd37ea
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Although Long-Short Term Memory (LSTM) networks and deep Transformers are now extensively used in offline ASR, it is unclear how best offline systems can be adapted to work with them under the streaming setup. After gaining considerable experience on this regard in recent years, in this paper we show how an optimized, low-latency streaming decoder can be built in which bidirectional LSTM acoustic models, together with general interpolated language models, can be nicely integrated with minimal perfomance degradation. In brief, our streaming decoder consists of a one-pass, real-time search engine relying on a limited-duration window sliding over time and a number of ad hoc acoustic and language model pruning techniques. Extensive empirical assessment is provided on truly streaming tasks derived from the well-known LibriSpeech and TED talks datasets, as well as from TV shows on a main Spanish broadcasting station.
