---
title: "ZEPI-Net: Light Field Super Resolution via Internal Cross-Scale Epipolar Plane Image Zero-Shot Learning"
authors:
- "admin"
- "Yinhai Liu"
- "Haiyan Jin"
- "Christine Guillemot"
date: "2023-04-01T00:00:00Z"
doi: "10.1007/s11063-022-10955-x"
publication_types: ["article-journal"]
publication: "Neural Processing Letters"
publication_short: "Neural Processing Letters"
volume: "55"
issue: "2"
pages: "1649-1662"
summary: "在极平面图像上学习可复用的跨尺度特征，不依赖外部光场和深度估计，同时提升光场的空间与角度分辨率。"
abstract: |
  Many applications of light field (LF) imaging have been limited by the spatial-angular resolution problem, hence the need for efficient super-resolution techniques. Recently, learning-based solutions have achieved remarkably better performances than traditional super-resolution (SR) techniques. Unfortunately, the learning or training process relies heavily on the training dataset, which could be limited for most LF imaging applications. In this paper, we propose a novel LF spatial-angular SR algorithm based on zero-shot learning. We suggest learning cross-scale reusable features in the epipolar plane image (EPI) space, and avoiding explicitly modeling scene priors or implicitly learning that from a large number of LFs. Most importantly, without using any external LFs, the proposed algorithm can simultaneously super-resolve a LF in both spatial and angular domains. Moreover, the proposed solution is free of depth or disparity estimation, which is usually employed by existing LF spatial and angular SR. By using a simple 8-layers fully convolutional network, we show that the proposed algorithm can generate comparable results to the state-of-the-art spatial SR. Our algorithm outperforms the existing methods in terms of angular SR on multiple groups of public LF datasets. The experiment results indicate that the cross-scale features can be well learned and be reused for LF SR in the EPI space.
tags:
- "Cross-scale feature"
- "Epipolar plane image"
- "Zero-shot learning"
- "Super resolution"
- "Light field imaging"
featured: false
url_html: "https://doi.org/10.1007/s11063-022-10955-x"
---
