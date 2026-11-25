---
title: 'CEDFlow++: Latent Contour Enhancement for Dark Optical Flow Estimation'
authors:
- Fengyuan Zuo
- Haiyan Jin
- admin
- su-haonan
- Meng Zhang
date: '2025-07-15T00:00:00Z'
publication_types:
- article-journal
publication:
  name: International Journal of Computer Vision
  volume: '133'
  issue: '10'
  pages: 7222-7241
summary: Adds factorized feature encoding, dual cost-volume inference, and contour-guided
  attention on top of CEDFlow to handle large-scale degradations in low light.
abstract: 'CEDFlow introduces a latent contour enhancement method into dark optical
  flow estimation and achieves advanced performance. Nevertheless, it largely focuses
  on addressing the motion boundary in a local manner. Unfortunately, it falls short
  in performance when addressing significant variations or large-scale degraded scenes.
  This paper introduces CEDFlow++, which features three innovative modules to address
  the key challenges of CEDFlow. Firstly, we introduce a decomposition-based feature
  encoder (DBFE), which captures both fine-grained and large-scale features through
  its local encoder and a uniquely designed sparse attention-based global encoder
  that suppresses noise and interference that only exist in the dark. Secondly, for
  reliable motion analysis, we propose a customized dual cost-volume reasoning (DCVR),
  which integrates important high-contrast feature correlations of the global cost
  volume into the local cost volume, effectively capturing salient yet holistic motion
  information while mitigating motion ambiguity caused by darkness. Importantly, we
  present a contour-guided attention (CGA) which enables context-adaptive extraction
  of contour features by modifying the sign properties of the Sobel kernel parameters
  in latent space, specifically targeting large-scale contours that are suitable for
  motion boundaries. Experimental results on the FCDN and VBOF datasets show that
  CEDFlow++ outperforms state-of-the-art methods in terms of the EPE index and produces
  more accurate and robust optical flow.

  '
featured: true
tags:
- Low-light enhancement
- Optical flow
- Deep learning
hugoblox:
  ids:
    doi: 10.1007/s11263-025-02528-x
links:
- type: url
  url: https://doi.org/10.1007/s11263-025-02528-x
- type: dataset
  url: https://github.com/mf-zhang/Optical-Flow-in-the-Dark
ccf: A
publication_short: IJCV
research:
- low-light
---
