---
arxiv_id: s2:af1b479b87afe3718b3bcfb26b917a995c86e53e
title:
  "iRead: A Reading Enhancement Platform with Integrated Small-Vocabulary Speech
  Recognition for English, Filipino, and Hiligaynon"
authors:
  - Jan Carlo T. Arroyo
  - Bon Eric A. Besonia
  - Allemar Jhone P. Delima
  - Felipe P. Vista IV
  - Mark Ronar G. Galagala
  - Marieth Flor M. Bernardez
  - Shiela Mae H. Espora
  - A. Zaragosa
  - Rizzamila R. Superio
submitted: "2026-08-08"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/af1b479b87afe3718b3bcfb26b917a995c86e53e
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-12T06:42:14+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Reading proficiency is considered a critical educational challenge in a highly multilingual nation such as the Philippines. Digital literacy tools available on the market and those that are found in the literature are mostly English-centric and often lack interactive mechanisms. This study shows the design, technical validation, and implementation of the iRead mobile application software. It is a multilingual mobile reading platform with offline speech recognition function available for three languages, specifically English, Filipino, and Hiligaynon. The mobile application was developed specifically for the Android Operating System using the Flutter framework, while the Vosk API was used for the speech recognition engine. Publicly available pretrained speech recognition models were utilized for English and Filipino languages, while a novel baseline small-vocabulary speech recognition model for Hiligaynon was developed and trained from scratch. A Gaussian Mixture Model-Hidden Markov Model (GMM-HMM) pipeline within the Kaldi framework was then used to form the Hiligaynon speech recognition model. Recognition vocabulary was limited to a 380-word phonics-based lexicon that is aligned with early literacy instruction. Cross-speaker generalization for Hiligaynon was evaluated using a leave-one-speaker-out cross-validation technique across four speakers. Recognition stability was further assessed using standard deviation and confidence interval analysis. The overall system evaluation was conducted using 540 utterances across the three languages under controlled conditions. Recognition performance achieved average accuracies of 92.8% for English, 88.3% for Filipino, and 85.6% for Hiligaynon. Category-level analysis demonstrated the highest performance for vowels, followed by consonants, then consonant–vowel blends. Results suggest that a classical small-vocabulary acoustic model combined with grammar-constrained decoding is technically viable and deployment-ready in a multilingual offline speech-supported literacy app for low-resource educational settings.
