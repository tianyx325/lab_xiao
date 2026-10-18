---
title: "CEDFlow++: Latent Contour Enhancement for Dark Optical Flow Estimation"
authors:
- "Fengyuan Zuo"
- "Haiyan Jin"
- "admin"
- "su-haonan"
- "Meng Zhang"
date: "2025-07-15T00:00:00Z"
doi: "10.1007/s11263-025-02528-x"
publication_types: ["article-journal"]
publication: "International Journal of Computer Vision"
publication_short: "IJCV"
volume: "133"
issue: "10"
pages: "7222-7241"
summary: "在 CEDFlow 上增加分解式特征编码、双代价体推理和轮廓引导注意力，以处理暗光中的大尺度退化场景。"
abstract: |
  CEDFlow introduces a latent contour enhancement method into dark optical flow estimation and achieves advanced performance. Nevertheless, it largely focuses on addressing the motion boundary in a local manner. Unfortunately, it falls short in performance when addressing significant variations or large-scale degraded scenes. This paper introduces CEDFlow++, which features three innovative modules to address the key challenges of CEDFlow. Firstly, we introduce a decomposition-based feature encoder (DBFE), which captures both fine-grained and large-scale features through its local encoder and a uniquely designed sparse attention-based global encoder that suppresses noise and interference that only exist in the dark. Secondly, for reliable motion analysis, we propose a customized dual cost-volume reasoning (DCVR), which integrates important high-contrast feature correlations of the global cost volume into the local cost volume, effectively capturing salient yet holistic motion information while mitigating motion ambiguity caused by darkness. Importantly, we present a contour-guided attention (CGA) which enables context-adaptive extraction of contour features by modifying the sign properties of the Sobel kernel parameters in latent space, specifically targeting large-scale contours that are suitable for motion boundaries. Experimental results on the FCDN and VBOF datasets show that CEDFlow++ outperforms state-of-the-art methods in terms of the EPE index and produces more accurate and robust optical flow.
featured: false
url_html: "https://doi.org/10.1007/s11263-025-02528-x"
url_dataset: "https://github.com/mf-zhang/Optical-Flow-in-the-Dark"
---
