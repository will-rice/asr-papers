---
arxiv_id: s2:1e9a3c8b6bc1c81aa1ca706da188bff5349f2d3c
title:
  "Att2RAG: A Double-Condition Framework for Knowledge Poisoning Attacks on RAG
  Systems"
authors:
  - Zhize Hao
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/1e9a3c8b6bc1c81aa1ca706da188bff5349f2d3c
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-09-03T06:24:34+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Modern retrieval-augmented generation (RAG) and memoryaugmented LLM applications are widely deployed in knowledge-intensive settings. These systems ground model outputs on external knowledge stores and may persist interaction traces in vector memory. If the underlying store is compromised, poisoned content can be retrieved repeatedly and thereby shape downstream responses, yielding confident yet harmful outputs supported by seemingly plausible evidence. Recent studies have shown that RAG pipelines and LLM agents are vulnerable to knowledge poisoning and prompt injection, but many formulations treat attack success as a single end-to-end outcome and do not separate retrieval and generation failure modes in a retrievalâ€“generation aligned manner. Moreover, although long-horizon memory writes can introduce cumulative risks, these effects are not empirically evaluated under our benchmark setting. We present Att2RAG, a double-condition framework for knowledge poisoning attacks on RAG systems. Att2RAG decomposes a successful poisoning event into a retrieval condition and a generation condition, and casts poisoning as maximizing attack success subject to satisfying both conditions. We instantiate the framework with (i) a white-box variant that applies projected gradient descent (PGD) in embedding space, serving as an approximate upper bound under strong attacker assumptions, and (ii) a black-box attack based on a Q âŠ• I construction that combines problem self-similarity with adversarial instruction injection using only query access. We evaluate Att2RAG on representative QA benchmarks under several common RAG configurations and consider practical defenses such as paraphrasing and duplicate filtering. Attack success is measured by ASR and Target-F1 relative to an attacker-specified target response. Across the evaluated configurations, Att2RAG attains attack success rates in the mid-90% range without defenses; paraphrasing plus duplicate filtering reduce ASR only modestly, and many attacks remain successful. These results highlight limitations of semantic-similarity-driven retrieval and suggest that strengthening RAG systems requires defenses beyond surface-form rewriting and naive duplicate removal.
