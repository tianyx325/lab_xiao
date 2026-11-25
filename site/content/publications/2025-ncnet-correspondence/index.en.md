---
title: 'NCNet: Learning to Find Non-Consistent Correspondence Using Learnable Frequency
  Response Function'
authors:
- Ruiyuan Li
- admin
- Meng Zhang
- Haiyan Jin
- su-haonan
date: '2025-01-01T00:00:00Z'
publication_types:
- paper-conference
publication:
  name: ICASSP
  pages: 1-5
summary: Fits both consistent and inconsistent true matches with learnable frequency
  responses, avoiding discarding valid correspondences based solely on motion consistency.
abstract: 'False correspondence removal is a persistent challenge in image feature-matching-based
  applications, especially in complex scenes. Traditional methods often rely on the
  consistency assumption to model the motion of correct correspondences, which neglects
  non-consistent correct correspondences, resulting in suboptimal performance. In
  this paper, we introduce the NCNet, a novel network designed to address this limitation
  by fitting the motion of both consistent and non-consistent correct correspondences
  using the learnable frequency response function. Unlike conventional approaches
  that focus on pixel-based 2D movements, NCNet utilizes the Motion Fitting Residual
  Module to estimate the high-dimensional motion, capturing the intricate 3D geometrical
  variations of matching pairs. To further enhance performance, we propose a loss
  function that balances the performance between the two types of correct correspondences.
  Extensive experiments demonstrate that NCNet significantly outperforms existing
  methods in terms of precision for false correspondence removal. The implementation
  of our approach is publicly available at: https://github.com/Livsdjo/NCNet-Code.

  '
featured: false
tags:
- Feature matching
- Deep learning
hugoblox:
  ids:
    doi: 10.1109/icassp49660.2025.10887571
links:
- type: url
  url: https://doi.org/10.1109/icassp49660.2025.10887571
- type: code
  url: https://github.com/Livsdjo/NCNet-Code
ccf: C
publication_short: ICASSP
---
