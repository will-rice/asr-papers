---
arxiv_id: s2:d9cae53b0fec598b1b9c4c3fe2a0fbe06123591d
title:
  Inference-Configuration Robust Backdoor Attacks on Diffusion Models via Cross-Timestep
  Consistent Trigger
authors:
  - Zhiyuan Shen
  - Zuonan Xiao
  - Bing Li
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/d9cae53b0fec598b1b9c4c3fe2a0fbe06123591d
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-18T06:52:45+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Backdoor attacks on diffusion models are commonly evaluated under fixed inference settings, yet practical diffusion services routinely change schedulers, denoising-step budgets, and classifier-free guidance scales for acceleration and control. Such deployment-side configuration drift can substantially alter the reverse diffusion trajectory, making existing evaluations insufficient for characterizing real backdoor risk. This paper studies inference-configuration robust backdoor attacks on diffusion models and identifies worst-case attack success rate (WC-ASR) across heterogeneous inference settings as a key security metric. To improve robustness under configuration drift, a cross-timestep consistent trigger mechanism is proposed to enforce malicious target alignment over multiple denoising stages, allowing the attack effect to accumulate throughout the reverse process. To further improve concealment and pipeline compatibility, a stealth-oriented trigger family is designed in the noise, Fourier, and latent domains. Extensive experiments on CIFAR-10 and MS-COCO 2017 demonstrate that the proposed method consistently outperforms recent diffusion backdoor baselines under scheduler replacement, denoising-step variation, and guidance-scale drift. On CIFAR-10, the proposed method achieves a WC-ASR of 84.2%, substantially exceeding the strongest baseline (62.5%), while reducing the RobustGap from 18.2 to 6.6. On MS-COCO 2017, it attains a WC-ASR of 78.6%, compared with 58.4% for the strongest competitor, and reduces the RobustGap from 20.7 to 8.7, while preserving competitive clean generation fidelity and semantic alignment. These results suggest that diffusion-model security should be analyzed not only at the model level, but also from the perspective of inference configuration integrity and end-to-end deployment trust.
