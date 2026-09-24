---
arxiv_id: s2:b05e2df517662bffcd25a396deea07f21855fea3
title: An analog-AI chip for energy-efficient speech recognition and transcription
authors:
  - S. Ambrogio
  - P. Narayanan
  - A. Okazaki
  - A. Fasoli
  - C. Mackin
  - K. Hosokawa
  - A. Nomura
  - Takeo Yasuda
  - An Chen
  - A. Friz
  - M. Ishii
  - J. Luquin
  - Y. Kohda
  - N. Saulnier
  - K. Brew
  - Samuel Choi
  - I. Ok
  - Timothy Philip
  - Victor Chan
  - M. Silvestre
  - I. Ahsan
  - Vijay Narayanan
  - H. Tsai
  - Geoffrey W. Burr
submitted: "2023-08-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b05e2df517662bffcd25a396deea07f21855fea3
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T19:09:02+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

A low-power chip that runs AI models using analog rather than digital computation shows comparable accuracy on speech-recognition tasks but is more than 14 times as energy efficient. Models of artificial intelligence (AI) that have billions of parameters can achieve high accuracy across a range of tasks^ 1 , 2 , but they exacerbate the poor energy efficiency of conventional general-purpose processors, such as graphics processing units or central processing units. Analog in-memory computing (analog-AI)^ 3 – 7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’. However, analog-AI has yet to demonstrate software-equivalent (SW_eq) accuracy on models that require many such tiles and efficient communication of neural-network activations between the tiles. Here we present an analog-AI chip that combines 35 million phase-change memory devices across 34 tiles, massively parallel inter-tile communication and analog, low-power peripheral circuitry that can achieve up to 12.4 tera-operations per second per watt (TOPS/W) chip-sustained performance. We demonstrate fully end-to-end SW_eq accuracy for a small keyword-spotting network and near-SW_eq accuracy on the much larger MLPerf^ 8 recurrent neural-network transducer (RNNT), with more than 45 million weights mapped onto more than 140 million phase-change memory devices across five chips.
