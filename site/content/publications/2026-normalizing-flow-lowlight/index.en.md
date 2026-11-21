---
title: A dual-guide aware normalizing flow for low-light enhancement with global illumination
  and cross-channel attention
authors:
- Xue Zhuang
- admin
- su-haonan
date: '2026-03-09T00:00:00Z'
publication_types:
- article-journal
publication:
  name: Multimedia Systems
  volume: '32'
  issue: '3'
  pages: '173'
summary: Proposes a dual-guided normalizing flow that encodes illumination and color
  as separate conditions, mitigating uneven lighting and color distortion in low-light
  enhancement.
abstract: 'Low Light Image Enhancement (LLIE) focuses on improving the quality of
  images captured under insufficient lighting conditions. Recently, normalizing flow
  model has been introduced to LLIE task due to its powerful capability in modeling
  data distribution. However, existing flow-based methods often overlook the importance
  of conditional features in guiding accurate probabilistic modeling, which can lead
  to uneven illumination and unnatural color restoration. To address this issue, we
  propose a Dual-Guide aware Normalizing Flow (DGNF) framework, which enhances encoding
  quality and injects richer conditional features into the flow-based decoder. Specifically,
  the proposed Dual-Guided aware Encoder Module (DGEM) consists of two specialized
  components–the Illumination-Guided Encoder Module (IGEM) and the Color-Guided Encoder
  Module (CGEM), which accurate models the features of illuminance and color of low
  light images respectively. The Illumination and Color aware Normalizing Flow Decoder
  (ICNFD) is designed to inject encoded features into the flow-based decoder, using
  them as conditional inputs to enable high-quality image enhancement. Experimental
  results on the LOL-V1 and LOL-V2 datasets show that our method achieves improvements
  of 1.36 dB in PSNR and 0.005 in SSIM compared to state-of-the-art methods, demonstrating
  the effectiveness of the proposed encoder in content preservation, noise reduction,
  and color restoration.

  '
featured: false
tags:
- 弱光增强
- 深度学习
hugoblox:
  ids:
    doi: 10.1007/s00530-026-02241-w
links:
- type: url
  url: https://doi.org/10.1007/s00530-026-02241-w
ccf: C
publication_short: Multimedia Systems
research:
- low-light
---
