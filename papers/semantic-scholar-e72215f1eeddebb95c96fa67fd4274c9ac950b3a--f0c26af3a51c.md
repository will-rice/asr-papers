---
arxiv_id: s2:e72215f1eeddebb95c96fa67fd4274c9ac950b3a
title: Streaming On-Device End-to-End ASR System for Privacy-Sensitive Voice-Typing
authors:
  - Abhinav Garg
  - Gowtham P. Vadisetti
  - Dhananjaya N. Gowda
  - Sichen Jin
  - Aditya Jayasimha
  - Young-Kyu Han
  - Jiyeon Kim
  - Junmo Park
  - Kwangyoun Kim
  - Sooyeon Kim
  - Young-Yoon Lee
  - Kyung-Joong Min
  - Chanwoo Kim
submitted: "2020-10-25"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/e72215f1eeddebb95c96fa67fd4274c9ac950b3a
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:52:51+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

In this paper, we present our streaming on-device end-to-end speech recognition solution for a privacy sensitive voice-typing application which primarily involves typing user private details and passwords. We highlight challenges speciﬁc to voice-typing scenario in the Korean language and propose solutions to these problems within the framework of a streaming attention-based speech recognition system. Some important challenges in voice-typing are the choice of output units, coupling of multiple characters into longer byte-pair encoded units, lack of sufﬁcient training data. Apart from customizing a high accuracy open domain streaming speech recognition model for voice-typing applications, we retain the performance of the model for open domain tasks without signiﬁcant degradation. We also explore domain biasing using a shallow fusion with a weighted ﬁnite state transducer (WFST). We obtain approximately 13 % relative word error rate (WER) improvement on our internal Korean voice-typing dataset without a WFST and about 30% additional WER improvement with a WFST fusion.
