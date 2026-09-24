---
arxiv_id: s2:b1fbd422136f7dfb1a14fed40342c87b20d5b909
title:
  Performance Analysis of a Modular Framework for Edge-Based Generative Conversational
  AI
authors:
  - Lorenzo Mazzone
  - D. Pau
submitted: "2026-08-16"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b1fbd422136f7dfb1a14fed40342c87b20d5b909
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-27T09:14:41+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

This study presents a multi-tier framework for deploying multi-modal Conversational AI on edge devices, spanning from constrained ultra-low-power systems to high-performance edge workstations. Utilizing an automated model discovery process and a modular benchmarking testbed, the research demonstrates that real-time, fully edge AI execution is feasible through strategic model selection and hardware acceleration. Key outcomes from the performance analysis are as follows. Speech-to-Text: Fun-ASR-Nano achieved the highest transcription accuracy with a Word Error Rate of 0.026, while Moonshine Tiny was the most efficient, recording a Real-Time Factor of 0.036 on the CPU. Scaling up to the high-performance tier, Whisper Large-V3 Turbo demonstrated high speed and robustness on a dedicated GPU, achieving an RTF of 0.093. Language Modeling: The Qwen 2.5 (1.5B Instruct) model, optimized for the Intel edge NPU, delivered robust constrained edge performance with an average generation speed of 20.15 tokens per second and a high semantic accuracy score of 0.86. The non-transformer Liquid LFM-24B model showcased server-level reasoning capabilities on the high-performance edge, reaching an impressive 39.2 tokens per second when fully offloaded to a dedicated GPU, despite its massive VRAM requirements. Text-to-Speech: Piper TTS emerged as the most efficient model for constrained environments (RTF of 0.034). However, Kokoro TTS redefined high-fidelity zero-shot synthesis on the GPU tier, achieving a groundbreaking RTF of 0.024 and far outperforming larger autoregressive audio models like OuteTTS, which remained too slow for real-time use without significant acceleration. Hardware Acceleration and Energy Efficiency: The use of Intel OpenVINO 2026.0 for hardware offloading significantly reduced energy consumption; for example, Whisper Large-V3 Turbo’s energy per audio second dropped from 52.68 Joules on the CPU to just 3.24 Joules on the integrated GPU. Furthermore, dedicated GPU acceleration revealed a critical “race-to-sleep” paradigm, where higher peak wattage is offset by drastically reduced processing times. The study concludes by identifying two optimal cascaded pipelines: a constrained edge tier (Moonshine, Qwen 1.5B, Piper) running on a Khadas NUC (Khadas Technology, Shenzhen, China powered by an Intel processor (Intel Corporation, Santa Clara, CA, USA) maximizing energy efficiency, and a high-performance tier (Whisper V3 Turbo, Liquid LFM-24B, Kokoro) running on an NVIDIA 5060ti, delivering uncompromising accuracy and subsecond latency for privacy-preserving, advanced edge AI.
