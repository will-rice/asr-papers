---
arxiv_id: s2:97984887c38d47fd7101de0efbdaa167e6c1adc2
title:
  "HIPA-MoE: A Parameter-Efficient Fine-Tuning Architecture with Hierarchical
  Adapter-Based Mixture-Of-Experts for Multilingual ASR"
authors:
  - Xun Lu
  - Xuyang Wang
  - Gaofeng Cheng
  - Lin Zheng
  - Pengyuan Zhang
submitted: "2025-10-22"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/97984887c38d47fd7101de0efbdaa167e6c1adc2
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:35:08+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Multilingual automatic speech recognition (MASR) has advanced significantly with self-supervised pretraining (SSL). However, conventional fine-tuning remains constrained by data imbalance, especially for low-resource languages. Although Mixture-of-Experts(MoE) has provided a promising approach for multilingual automatic speech recognition, expanding feedforward networks (FFNs) into MoE layers often incurs significant parameter overhead. To solve these issues, we propose HIPAMoE, a novel Hierarchical Inverted Pyramid Adapter Mixture-ofExperts (HIPA-MoE) architecture that uses lightweight adapters as experts with language-aware routing. Our model hierarchically organizes experts to capture both universal acoustic features and language-specific phonetic nuances. Specifically, shared adapters in the lower layers model cross-lingual patterns, while the upper layers deploy language-specific adapters for fine-grained specialization. Additionally, we incorporate an auxiliary phoneme-level loss via uroman transliterations to enhance cross-lingual speech representation. Experiments on ML-SUPERB 2.0 demonstrate that HIPA-MoE achieves state-of-the-art performance in lowresource and long-tail languages while maintaining high parameter efficiency and scalability.
