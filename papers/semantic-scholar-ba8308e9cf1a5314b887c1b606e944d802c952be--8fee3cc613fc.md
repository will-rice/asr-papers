---
arxiv_id: s2:ba8308e9cf1a5314b887c1b606e944d802c952be
title: Mixed approach speech-to-text translation for endangered language
authors:
  - B. L. Sinaga
  - Stephanie Pamela Adithama
  - J. Nugraha
  - Martinus Maslim
  - Albert William Wibisono
  - Y. Prabowo
  - Yohanes Sigit Purnomo W.P.
  - Vinindita Citrayasa
submitted: "2026-07-20"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/ba8308e9cf1a5314b887c1b606e944d802c952be
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-23T07:05:07+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This study aims to address the technological marginalization of endangered regional languages by evaluating speech-to-text translation for Dayak Ma’anyan, an extremely low-resource Austronesian language. In particular, it seeks to examine whether cascaded multilingual automatic speech recognition and machine translation models can provide effective Ma’anyan–Indonesian translation despite severe data scarcity. This study employs a cascaded speech-to-text translation framework that combines two multilingual automatic speech recognition models, Whisper Large-v3 and SeamlessM4T v2, with two LoRA-adapted multilingual machine translation models, NLLB-200 3.3B and distilled 600M. Experiments are conducted in an extremely low-resource setting using limited parallel speech and text data. The proposed pipelines are evaluated at three levels: ASR transcription quality, machine translation performance and end-to-end semantic preservation. The results show that cascaded pipelines can produce semantically meaningful Ma’anyan–Indonesian translations even under high transcription error conditions. Whisper substantially outperforms SeamlessM4T at the ASR stage, achieving a lower WER (0.464 vs 0.812) and yielding better downstream translation quality. Among the machine translation models, LoRA-adapted NLLB-200 3.3B achieves the best performance, with BLEU 31.00, chrF 58.91 and the highest end-to-end semantic similarity (SBERT 0.722). The findings further indicate that ASR quality is the dominant determinant of overall speech translation performance, while larger LoRA-adapted MT models provide stronger robustness against noisy ASR outputs. This study provides, to the best of the authors’ knowledge, the first empirical benchmark for Ma’anyan–Indonesian speech-to-text translation. It contributes a systematic evaluation of multilingual ASR and LoRA-adapted MT combinations for endangered-language technology and offers empirical insight into the relative impact of ASR quality and MT model capacity in extremely low-resource cascaded speech translation.
