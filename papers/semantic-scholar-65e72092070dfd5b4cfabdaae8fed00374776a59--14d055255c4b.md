---
arxiv_id: s2:65e72092070dfd5b4cfabdaae8fed00374776a59
title:
  "Post-ASR Correction in Hindi: Comparing Language Models and Large Language
  Models in Low-Resource Scenarios"
authors:
  - Rishabh Kumar
  - Amrith Krishna
  - Ganesh Ramakrishnan
  - P. Jyothi
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/65e72092070dfd5b4cfabdaae8fed00374776a59
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-14T06:57:43+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Automatic Speech Recognition (ASR) systems for low-resource languages like Hindi often produce erroneous transcripts due to limited annotated data and linguistic complexity. Post-ASR correction using language models (LMs) and large language models (LLMs) offers a promising approach to improve transcription quality. In this work, we compare fine-tuned LMs (mT5, ByT5), fine-tuned LLMs (Nanda 10B), and instruction-tuned LLMs (GPT-4o-mini, LLaMA variants) for post-ASR correction in Hindi. Our findings reveal that smaller, fine-tuned models consistently outperform larger LLMs in both fine-tuning and in-context learning (ICL) settings. We observe a n-shaped inverse scaling trend under zero-shot ICL, where mid-sized LLMs degrade performance before marginal recovery at extreme scales, yet still fall short of fine-tuned models. ByT5 is more effective for character-level corrections such as transliteration and word segmentation, while mT5 handles broader semantic inconsistencies. We also identify performance drops in out-of-domain settings and propose mitigation strategies to preserve domain fidelity. In particular, we observe similar trends in Marathi and Tel-ugu, indicating the broader applicability of our findings across low-resource Indian languages.
