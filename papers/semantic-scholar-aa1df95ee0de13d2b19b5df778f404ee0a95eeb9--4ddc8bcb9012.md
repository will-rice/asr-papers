---
identifier: semantic_scholar:aa1df95ee0de13d2b19b5df778f404ee0a95eeb9
title: A Metric-Driven Approach to Conformer Layer Pruning for Efficient ASR Inference
authors:
- Dhanush Bekal
- Karthik Gopalakrishnan
- Karel Mundnich
- S. Ronanki
- S. Bodapati
- K. Kirchhoff
published: '2023-08-20T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/aa1df95ee0de13d2b19b5df778f404ee0a95eeb9
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Conformer-based end-to-end automatic speech recognition (ASR) models have gained popularity in recent years due to their exceptional performance at scale. However, there are significant computation, memory and latency costs associated with running inference on such models. With the aim of mitigating these issues, we evaluate the efficacy of pruning Conformer layers while fine-tuning only on 20% of the data used for the pre-trained model. We score Conformer layers using correlation, energy, and gradient-based metrics and rank them to identify candidate layers for pruning. We also propose an iterative pruning strategy which monitors and prunes layers that are consistently ranked low by the metrics during training. Using our methods, we prune large pre-trained offline and online (streaming) models by 20% and 40% with little impact on performance, while outperforming a strong knowledge distillation baseline.
