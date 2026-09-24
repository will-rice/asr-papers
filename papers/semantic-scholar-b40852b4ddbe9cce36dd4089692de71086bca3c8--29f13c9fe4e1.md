---
arxiv_id: s2:b40852b4ddbe9cce36dd4089692de71086bca3c8
title:
  Multilingual Self-Supervised Fine-Tuning for Low-Resource Telugu Automatic
  Speech Recognition
authors:
  - Srivarthin Vaddepalli
  - Renjith Prabhavathi Neelakandan
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b40852b4ddbe9cce36dd4089692de71086bca3c8
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-13T07:18:11+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Low-resource language Automatic Speech Recognition (ASR) remains a difficult problem due to the unavailability of training data, extreme pronunciation variation, and the sophistication in word structure. These obstacles continue to affect Telugu language, one of the major Dravidian languages with many users. This paper determines a multilingual self-supervised transfer learning system of statistical language modeling as the basis of an end-to-end Telugu ASR system. This method includes fine-tuning a pre-trained Wav2Vec2-Large-XLSR-53 model on a Telugu subset of the IndicTTS corpus with a character-level Connectionist Temporal Classification (CTC) task and a custom Telugu tokenizer with Unicode normalization. They have speaker-independent data partitioning, dynamic batch padding, gradient accumulation, and mixed-precision training, which help them to achieve stable learning in low-resource. In order to enhance transcription fluency, a 5-gram KenLM language model, which is trained on a large text corpus of Telugu, is introduced under beam-search decoding through shallow fusion. Extensive preprocessing like audio normalization, duration filtering and transcript normalization is carried out to minimize disparities within the acoustic and textual data. System evaluation based on Word Error Rate (WER) and Character Error Rate (CER) yields a Word Error Rate of 17.8 and Character Error rate of 6.9 and hence an improvement compared to some of the published Telugu ASR systems. The impact of multilingual pretraining, area-specific fine-tuning, and external language modeling is raised in ablation studies. The outcome of qualitative error analysis is the resolution to achieve improved awareness of agglutinative word forms, as well as long-range phonetic patterns. These findings suggest that self-supervised acoustic models combined with statistical language models are a practical and scalable solution to achieve accurate ASR using a low-resource language and that the vision of inclusive speech technologies is approaching.
