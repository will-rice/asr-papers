---
arxiv_id: s2:669dad3e0ac9bc7af58b7e3b3ab28254bddd167f
title:
  A Hybrid Acoustic Model for Automatic Speech Recognition Based on Discriminative
  Learning
authors:
  - M. K. Rohil
  - Ishant Gupta
submitted: "2026-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/669dad3e0ac9bc7af58b7e3b3ab28254bddd167f
github_repo: ""
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-14T06:57:43+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

: The much researched probabilistic speech recognition systems decompose the problem of automatic speech recognition into language modeling and acoustic modeling. Once these two models are defined and their parameters are learnt, a Hidden Markov Model can be built to make predictions on new audio signals. Our work proposes a novel acoustic model inspired by a significant advantage of fitting a single one-dimensional discrete probability distribution over fitting multiple multi-dimensional continuous distributions. Mathematically if y is a multidimensional continuous random variable and x is a discrete random variable, then modeling P(x|y) using a classification algorithm and P(x) using proportions can be used to model P(y|x) as P(x|y) / P(x) up to a constant factor. This is as opposed to fitting probability densities e.g. multivariate Gaussians to each of the labeled portions of the dataset. Since the proposed approach does not assume a (multidimensional) parametric probability distribution for P(y|x), it has two main advantages, first reduced training time, and second, since P(x|y) can be modeled quite powerfully using complex models such as neural networks, it is arguably a more accurate fit to the training data. The proposed model has advantages in the terms of speed, accuracy and memory requirements.
