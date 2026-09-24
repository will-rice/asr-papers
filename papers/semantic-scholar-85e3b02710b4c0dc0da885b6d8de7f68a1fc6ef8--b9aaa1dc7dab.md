---
arxiv_id: s2:85e3b02710b4c0dc0da885b6d8de7f68a1fc6ef8
title: Towards Scalable and Robust Multilingual ASR for Indian Languages with MixLoRA-Whisper
authors:
  - Yeseul Park
  - Bowon Lee
submitted: "2025-12-06"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/85e3b02710b4c0dc0da885b6d8de7f68a1fc6ef8
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T18:33:48+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

India exhibits extensive linguistic diversity, with many regional languages and dialects, yet current multilingual automatic speech recognition (ASR) models provide limited support, especially for low-income and rural populations who rely on spoken communication. We apply MixLoRA, a parameterefficient fine-tuning method proposed for large language models, to Whisper to improve ASR performance. MixLoRA employs multiple LoRA experts and dynamically selects the most relevant experts per token, enabling better modeling of linguistic variation. By fine-tuning only up to 25.03 % of the parameters on the RESPIN dataset, which covers eight Indian languages with 33 dialects, it achieves a $4.98 \%$ character error rate (CER) on the read speech, yielding a $7.09 \%$ relative CER reduction over the baseline. Performance improved across all languages in read speech and five in spontaneous speech. These results demonstrate that MixLoRA can effectively enhance ASR for low-resource, dialect-rich languages.
