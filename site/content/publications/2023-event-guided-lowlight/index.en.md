---
title: Event-Guided Attention Network for Low Light Image Enhancement
authors:
- Qiaobin Wang
- Haiyan Jin
- su-haonan
- admin
date: '2023-06-18T00:00:00Z'
publication_types:
- paper-conference
publication:
  name: IJCNN
  pages: 1-8
summary: Reconstructs image gradients from event streams and fuses event and low-light
  image features via spatial and channel attention to enhance structure and suppress
  noise.
abstract: 'In the low-light conditions, images are corrupted by low contrast and severe
  noise, but event cameras can capture event streams with clear edge structures. Therefore,
  we propose an Event-Guided Attention Network for Low-light Image Enhancement (EGAN)
  using a dual branch Network and recover clear structure with the guide of events.
  To overcome the lack of paired training datasets, we first synthesize the dataset
  containing low-light event streams, low-light images, and the ground truth (GT)
  normal-light images. Then, we develop an end-to-end dual branch network consisting
  of a Image Enhancement Branch (IEB) and a Gradient Reconstruction Branch (GRB).
  The GRB branch reconstructs image gradients using events, and the IEB enhances low-light
  images using reconstructed gradients. Moreover, we develops the Attention based
  Event-Image Feature Fusion Module (AEIFFM) which selectively fuses the event and
  low-light image features using the spatial and channel attention mechanism, and
  the fused features are concatenated into the IEB and GRB, which respectively generate
  the enhanced images with clear structure and more accurate gradient images. Extensive
  experiments on synthetic and real datasets demonstrate that the proposed EGAN produces
  visually more appealing enhancement images, and achieves a good performance in structure
  preservation and denoising over state-of-the-arts.

  '
featured: false
tags:
- Low-light enhancement
- Deep learning
hugoblox:
  ids:
    doi: 10.1109/ijcnn54540.2023.10191272
links:
- type: url
  url: https://doi.org/10.1109/ijcnn54540.2023.10191272
ccf: C
publication_short: IJCNN
research:
- low-light
---
