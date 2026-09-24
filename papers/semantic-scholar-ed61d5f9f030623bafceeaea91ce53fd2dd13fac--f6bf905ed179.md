---
arxiv_id: s2:ed61d5f9f030623bafceeaea91ce53fd2dd13fac
title:
  Model-Internal Slot-triggered Biasing for Domain Expansion in Neural Transducer
  ASR Models
authors:
  - Yiting Lu
  - Philip Harding
  - Kanthashree Mysore Sathyendra
  - Sibo Tong
  - Xuandi Fu
  - Jing Liu
  - Feng-Ju Chang
  - Simon Wiesler
  - Grant P. Strimel
submitted: "2023-08-20"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/ed61d5f9f030623bafceeaea91ce53fd2dd13fac
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:08:27+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Personal rare word recognition is an important yet challenging task for end-to-end speech recognition. Contextual biasing has demonstrated success in tackling this problem. Though effective in improving rare word recognition, these mechanisms can lead to errors due to false-biasing while facing further challenges when attempting to expand them to many domains. To address these limitations, in this work we propose a neural biasing design with a streaming model-internal slot classifier, trained to categorise the domain of each word piece before it is emitted. The neural biasing module can therefore be triggered in a controlled way, permitting natural scaling to many domains while reducing false-biasing and computational cost. Experiments on diverse domain slot types of application names, communications and playlist names demonstrate the proposed architecture results in 26% to 58% relative improvements on personal rare word recognition with minimal impact (0.6% rel.) on general data.
