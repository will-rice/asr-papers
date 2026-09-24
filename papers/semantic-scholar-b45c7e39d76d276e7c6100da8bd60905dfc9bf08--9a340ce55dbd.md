---
arxiv_id: s2:b45c7e39d76d276e7c6100da8bd60905dfc9bf08
title: AI Powered Educational Video Summarization & Quiz Generation
authors:
  - A. Sawant
  - Vedant Dhamane
  - Ayusha Patil
  - Kishan Chaudhary
  - Eshaan Dasarwar
  - Saif Bichu
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b45c7e39d76d276e7c6100da8bd60905dfc9bf08
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

The growing dependence on video based learning has posed a challenge in content navigation, quick grasp of concepts as well as automated generation of assessment. The available tools usually do transcription, summarization or quiz development as a separate exercise, which restricts their applicability in education processes. The paper has introduced an end-to-end AI-enabled platform, which is capable of automatically transcribing, summarizing, and creating multiple-choice questions (MCQs) through the use of educational videos. The system combines Whisper-based multilingual automatic speech recognition (ASR) [1], MarianMT translation of code-mixed text [2], DistilBART abstractive summarization [4] and Gemini 1.5 Flash generated pedagogically oriented MCQs [8]. Evaluation was done on a synthetic and realistic set of 10 educational videos which included English as well as Hindi-English, Marathi-English. Whisper registered a Word Error Rate (WER) average of 9.6 which is 31 times better than Google ASR. DistilBART scores obtained 0.52, 0.31, and 0.47 on ROUGE-1, ROUGE-2, and ROUGE-L and multilingual sentence embedding averages semantic similarities between transcript and summary of 0.81 [5]. Generated MCQs rated as 4.5/5 in relation to relevance and clarity by expert evaluators. It is entirely implemented in a React.js front end, a Node.js back end, an AI microservice written in Flask and MongoDB Atlas to allow scaling to different institutions. The findings prove that the suggested pipeline is an effective tool in terms of teacher workloads, student understanding, and learning in multilingual settings. The framework is a viable and implementable way of transforming educational content automatically.
