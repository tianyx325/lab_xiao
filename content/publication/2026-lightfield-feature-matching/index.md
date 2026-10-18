---
title: "Robust 2.5D Feature Matching in Light Fields via a Learnable Parameterized Depth-Degraded Projection"
authors:
- "Meng Zhang"
- "Haiyan Jin"
- "admin"
- "Jinglei Shi"
- "Xiaoran Jiang"
date: "2026-01-01T00:00:00Z"
doi: "10.1109/tip.2026.3662579"
publication_types: ["article-journal"]
publication: "IEEE Transactions on Image Processing"
publication_short: "IEEE TIP"
volume: "35"
pages: "2235-2248"
summary: "用光场傅里叶视差层的视差作为粗深度，学习参数化的深度退化投影，以降低特征匹配中的深度歧义。"
abstract: |
  Due to the loss of 3D information, accurate and robust 2D image feature matching remains challenging for many computer vision applications. This paper introduces a 2.5D feature that uses the disparity value from the light field Fourier disparity layer (FDL) as a rough proxy of scene depth. Without explicit depth estimation, a parameterized depth-degraded projection is proposed to construct the geometric transformation of paired features between two light fields. Then, we propose a parameterized learning solution to calculate the depth-degraded projection. This solution estimates a global constant fundamental matrix, a variable disparity-guided translation vector, and a depth compensation term using a very simple network. Although the 0.5D relative disparity provided by the FDL does not represent precise depth, it can also significantly reduce the depth ambiguity in feature matching. Therefore, the proposed solution achieves accurate feature-matching results by minimizing the sum of reprojection errors across all matching candidates. On the public light field feature-matching dataset, the proposed solution outperforms existing 2D image feature-matching solutions and light field feature-matching algorithms in terms of matching accuracy and robustness. The code is available online.
tags:
- "Parameterized projection"
- "Feature matching"
- "Fourier disparity layer"
- "Light field"
featured: false
url_html: "https://doi.org/10.1109/TIP.2026.3662579"
url_pdf: "https://hal.science/hal-05645938v1/document"
---
