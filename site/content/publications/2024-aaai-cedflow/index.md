---
title: 'CEDFlow: Latent Contour Enhancement for Dark Optical Flow Estimation'
authors:
- Fengyuan Zuo
- admin
- Haiyan Jin
- su-haonan
date: '2024-03-24T00:00:00Z'
publication_types:
- paper-conference
publication:
  name: Proceedings of the AAAI Conference on Artificial Intelligence
  volume: '38'
  issue: '7'
  pages: 7909-7916
summary: 在隐空间用空频分解编码运动，并用二阶高斯差分筛选大尺度轮廓，以估计暗光光流。
abstract: 'Accurately computing optical flow in low-contrast and noisy dark images
  is challenging, especially when contour information is degraded or difficult to
  extract. This paper proposes CEDFlow, a latent space contour enhancement for estimating
  optical flow in dark environments. By leveraging spatial frequency feature decomposition,
  CEDFlow effectively encodes local and global motion features. Importantly, we introduce
  the 2nd-order Gaussian difference operation to select salient contour features in
  the latent space precisely. It is specifically designed for large-scale contour
  components essential in dark optical flow estimation. Experimental results on the
  FCDN and VBOF datasets demonstrate that CEDFlow outperforms state-of-the-art methods
  in terms of the EPE index and produces more accurate and robust flow estimation.
  Our code is available at: https://github.com/xautstuzfy.

  '
featured: true
tags:
- 弱光增强
- 光流估计
- 深度学习
hugoblox:
  ids:
    doi: 10.1609/aaai.v38i7.28627
links:
- type: url
  url: https://ojs.aaai.org/index.php/AAAI/article/view/28627
- type: code
  url: https://github.com/xautstuzfy
ccf: A
publication_short: AAAI
research:
- low-light
aliases:
- /publication/2024-aaai-cedflow/
---
