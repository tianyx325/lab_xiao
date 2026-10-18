---
title: "EDAFormer: Enhancing Low-Light Images with a Dual-Attention Transformer"
authors:
- "Jin Zhang"
- "Haiyan Jin"
- "su-haonan"
- "Yuanlin Zhang"
- "admin"
- "Bin Wang"
date: "2024-09-17T00:00:00Z"
doi: "10.1007/978-3-031-72335-3_25"
publication_types: ["paper-conference"]
publication: "ICANN"
publication_short: "ICANN"
volume: "15017"
pages: "364-378"
summary: "用递归的双重注意力融合全局与局部注意，并加入多尺度上下文卷积自注意力，以增强弱光图像。"
abstract: |
  In low-light conditions, images often suffer from poor quality and unstable noise. Inspired by the global attention mechanism of transformers, most approaches for Low-Light Image Enhancement (LLIE) rely on fusing local and global features. However, this fusion, typically achieved through linear formulas, can lead to feature distortion and the wastage of useful information. Moreover, the contextual information contained in the extracted local and global features remains unchanged, making it challenging for this fusion method to adaptively restore details and remove noise in different regions of the image. Instead of local-global feature fusion, the EDAformer module utilizes a recursive framework and dual attention to fuse global and local attention, thereby realizing a scalable attention mechanism for image enhancement. Furthermore, we propose the Multi-scale Context-aware Convolutional Self-Attention (MCCSA) module, which aggregates local self-attention using a multi-scale approach. Evaluation on LOL-v1, LOL-v2, and SICE datasets demonstrates that our method outperforms existing techniques qualitatively and quantitatively in terms of denoising and detail preservation.
featured: false
url_html: "https://doi.org/10.1007/978-3-031-72335-3_25"
---
