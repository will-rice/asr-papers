---
identifier: semantic_scholar:618e05ab0c5e51c6d22e760cfa9bb1f3366bdfd0
title: 'Joint ASR and Language Identification Using RNN-T: An Efficient Approach to Dynamic Language Switching'
authors:
- Surabhi Punjabi
- Harish Arsikere
- Zeynab Raeesy
- Chander Chandak
- Nikhil Bhave
- Ankish Bansal
- Markus Müller
- S. Murillo
- A. Rastrow
- A. Stolcke
- J. Droppo
- S. Garimella
- R. Maas
- Mat Hans
- A. Mouchtaris
- S. Kunzmann
published: '2021-06-06T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/618e05ab0c5e51c6d22e760cfa9bb1f3366bdfd0
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Conventional dynamic language switching enables seamless multilingual interactions by running several monolingual ASR systems in parallel and triggering the appropriate downstream components using a standalone language identification (LID) service. Since this solution is neither scalable nor cost- and memory-efficient, especially for on-device applications, we propose end-to-end, streaming, joint ASR-LID architectures based on the recurrent neural network transducer framework. Two key formulations are explored: (1) joint training using a unified output space for ASR and LID vocabularies, and (2) joint training viewed as multi-task optimization. We also evaluate the benefit of using auxiliary language information obtained on-the-fly from an acoustic LID classifier. Experiments with the English-Hindi language pair show that: (a) multi-task architectures perform better overall, and (b) the best joint architecture surpasses monolingual ASR (6.4–9.2% word error rate reduction) and acoustic LID (53.9–56.1% error rate reduction) baselines while reducing the overall memory footprint by up to 46%.
