---
arxiv_id: s2:6018915a3eae4cfeffc5fdf8bbd939df6edd7bab
title: Children’s Speech Recognition in Slovak
authors:
  - Stanislav Ondáš
  - Ján Staš
  - Matus Pleva
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/6018915a3eae4cfeffc5fdf8bbd939df6edd7bab
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-13T07:18:09+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This paper addresses the challenge of Automatic Speech Recognition (ASR) for Slovak children’s speech, a low-resource scenario characterized by significant linguistic variability and a scarcity of dedicated corpora. We introduce the first Slovak children’s speech dataset, comprising approximately five hours of semi-automatically annotated spontaneous speech, and use it to systematically evaluate state-of-the-art ASR architectures. Specifically, we benchmark Kaldi, Whisper, and Wav2Vec 2.0 models, enriched with data augmentation techniques. Our results demonstrate that the fine-tuned Massively Multilingual Speech (MMS) Wav2Vec 2.0 model, combined with a Slovak language model, achieves a Word Error Rate (WER) of 15.10%. This represents a relative improvement of over 67% compared to our Kaldi baseline (WER $\approx ~45.44$ %). These results are highly competitive with international benchmarks for non-English child corpora, which typically report WERs in the 13.81–30.00% range. Our findings highlight three key insights: 1) dedicated data augmentation is crucial for mitigating acoustic variability in children’s speech; 2) self-supervised multilingual pretraining followed by fine-tuning yields substantial accuracy improvements; and 3) transformer-based models significantly outperform conventional hybrid ASR systems. This work establishes a strong performance baseline for future research and demonstrates the potential of modern ASR systems to support educational, therapeutic, and clinical applications for children in low-resource languages.
