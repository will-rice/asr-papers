---
arxiv_id: s2:376066e9db20d83a106d8746aafcb7d7371ea6cb
title:
  Noise-Invariant Agentic Human–Robot Interaction GenAI System Using a Dual-Encoder
  Contrastive ASR Architecture and VLMs for Robot Control and Navigation in Acoustically
  Challenging Jobsites
authors:
  - Oscar Poudel
  - Rayan H. Assaad
  - Mohamad Awada
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/376066e9db20d83a106d8746aafcb7d7371ea6cb
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-20T06:22:42+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Speech-based human–robot interaction (HRI) offers a natural, hands-free interface for humans and robots to collaborate in construction environments. Construction settings—characterized by acoustically challenging environments with multiple nonstationary noises—pose serious challenges to effective voice-based HRI, highlighting the need for noise-robust HRI systems tailored for acoustically volatile construction settings. This paper proposes an HRI agentic artificial intelligence (AI) system—integrating a construction domain-specific, noise-robust automatic speech recognition (ASR) agent and a vision-language model (VLM)-based robotic control agent—to reliably transcribe speech in noisy environments and parse instructions for robot navigation in acoustically challenging construction jobsites. The ASR agent was developed based on a novel dual-encoder speech transcription deep learning architecture enhanced with a contrastive learning module for noise-invariant representation learning. The ASR agent is trained on a large speech data set augmented with real-world construction noise and synthesized undertones to reflect actual construction site conditions. On top of the developed ASR, the HRI agentic AI system also includes a closed-loop VLM as an application layer that semantically parses transcribed speech into robotic tasks, such as safety inspection, predefined waypoint navigation, and adaptive navigation. The proposed system was validated using different simulated and real-world experiments replicating various cluttered construction scenarios. The results showed that the ASR agent outperforms existing baseline models in noisy conditions and that the closed-loop VLM has a high task success rate across various testing scenarios using vision-only navigation. The primary contribution of this research is the construction-tailored, noise-robust deep learning–based ASR architecture and data set curation, with the VLM control stack demonstrating the feasibility of deploying the developed ASR system in end-to-end voice-based HRI for real-time autonomous robotic and navigation tasks within noisy construction sites.
