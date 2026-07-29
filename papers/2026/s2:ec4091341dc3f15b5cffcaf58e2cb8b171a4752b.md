---
arxiv_id: s2:ec4091341dc3f15b5cffcaf58e2cb8b171a4752b
title:
  "Measuring Watermarking under Jailbreaking: ASR Inflation and Goal-Compliance
  Mismatch"
authors:
  - Sungwoo Han
  - Sangjun Moon
  - Jingun Kwon
  - Hidetaka Kamigaito
  - Manabu Okumura
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/ec4091341dc3f15b5cffcaf58e2cb8b171a4752b
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-29T07:30:12+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Recently, watermarking has attracted growing attention as a practical technique for source at-tribution of machine-generated text. However, most prior work studies watermarking under benign prompts, while its behavior under jail-breaking prompts remains underexplored. This gap matters because jailbreaking can bypass safety policies and shift the generation regime, raising concerns that watermarking may interact with model alignment under attack. To address this gap, we evaluate six watermarking methods on four LLMs across two jailbreak benchmarks and three settings: Static, Auto-DAN, and DSN. We find that watermarking can inflate judge-based attack success rate, denoted ASR, under jailbreaking, with the largest effects appearing in biased schemes that perturb logits. At the same time, these ASR increases often do not reflect higher harmful-goal compliance when measured by StrongREJECT or by human judgments. This suggests that ASR-only evaluations can be brittle to decoding perturbations and may overestimate harmful-goal compliance, motivating complementary goal-compliance metrics (e.g., StrongREJECT) and human evaluations.
