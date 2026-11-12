---
title: "CEDFlow: Latent Contour Enhancement for Dark Optical Flow Estimation"
authors:
- Fengyuan Zuo
- admin
- Haiyan Jin
- su-haonan
date: "2024-03-24T00:00:00Z"
doi: "10.1609/aaai.v38i7.28627"
publication_types: ["paper-conference"]
publication: "Proceedings of the AAAI Conference on Artificial Intelligence"
publication_short: "AAAI"
volume: "38"
issue: "7"
pages: "7909-7916"
summary: "Encodes motion in latent space with spatial–frequency decomposition and filters large-scale contours with second-order difference of Gaussians to estimate low-light optical flow."
abstract: |
  Accurately computing optical flow in low-contrast and noisy dark images is challenging, especially when contour information is degraded or difficult to extract. This paper proposes CEDFlow, a latent space contour enhancement for estimating optical flow in dark environments. By leveraging spatial frequency feature decomposition, CEDFlow effectively encodes local and global motion features. Importantly, we introduce the 2nd-order Gaussian difference operation to select salient contour features in the latent space precisely. It is specifically designed for large-scale contour components essential in dark optical flow estimation. Experimental results on the FCDN and VBOF datasets demonstrate that CEDFlow outperforms state-of-the-art methods in terms of the EPE index and produces more accurate and robust flow estimation. Our code is available at: https://github.com/xautstuzfy.
featured: true
url_html: "https://ojs.aaai.org/index.php/AAAI/article/view/28627"
url_code: "https://github.com/xautstuzfy"
research:
  - low-light
ccf: "A"
---
