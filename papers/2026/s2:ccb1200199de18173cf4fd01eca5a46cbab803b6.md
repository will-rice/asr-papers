---
arxiv_id: s2:ccb1200199de18173cf4fd01eca5a46cbab803b6
title: Robust End-to-End Spoken Language Understanding in Low-Resource Settings
authors:
  - Andrés Piñeiro-Martín
  - C. García-Mateo
  - Laura Docío-Fernández
  - Maria del Carmen Lopez-Perez
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/ccb1200199de18173cf4fd01eca5a46cbab803b6
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-13T07:18:10+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This paper explores the robustness and generalisation capabilities of foundation speech models, such as Whisper, and Large Language Models (LLMs) with speech encoders, like Phi-4, when fine-tuned for the End-to-End (E2E) Spoken Language Understanding (SLU) task in low-resource languages. We investigate the impact of model scale, language-specific pretraining, and specialised encoding strategies for both Whisper-based and LLM-based SLU, while also exploring prompting techniques that enable LLMs to handle tasks such as intent classification and slot filling, bridging the gap between raw audio and language understanding. Our results demonstrate that a speech-conditioned LLM can perform instruction-driven SLU in a language entirely unseen during pretraining. By adapting only the speech encoder of Phi-4 and keeping the decoder frozen, the system achieves competitive performance in Galician through in-context supervision. In parallel, we show that increasing model scale and applying language-specific ASR pretraining consistently boost performance across all SLU metrics, particularly under the challenging conditions defined in the FalAI dataset. Finally, we present a detailed ablation study, showing that while acoustic redundancy has limited impact beyond a certain threshold, lexical diversity plays a crucial role in supporting robust generalisation. These findings offer new insights into data efficiency and generalisation in low-resource settings.
