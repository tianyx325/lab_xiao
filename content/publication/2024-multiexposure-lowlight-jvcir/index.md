---
title: "Learn to enhance the low-light image via a multi-exposure generation and fusion method"
authors:
- "Haiyan Jin"
- "Long Li"
- "su-haonan"
- "Yuanlin Zhang"
- "admin"
- "Bin Wang"
date: "2024-04-01T00:00:00Z"
doi: "10.1016/j.jvcir.2024.104127"
publication_types: ["article-journal"]
publication: "Journal of Visual Communication and Image Representation"
publication_short: "JVCIR"
volume: "100"
pages: "104127"
summary: "由单张弱光图像生成多曝光图像，并用感知重要性选择曝光良好的特征，再做曲线调整。"
abstract: |
  In low-light image enhancement, single-exposure images contain a limited dynamic range, which hinders the restoration of contrast and texture. To address these problems, we propose a multi-exposure generation and fusion method (MEGF), which simulates multi exposure images and performs feature fusion for low light image enhancement. First, we propose a Multi-Exposure Generation (MEG) block, which generates images with different exposure levels based on the input low-light images. The MEG block employs information entropy as an evaluation measure to prevent the underexposed or overexposed image generation. Then, the Perceptual Importance based Multi-Exposure Feature Enhancement (PIMEFE) module has been developed to fuse the multi-exposure features using the Perceptual Importance-based Feature Fusion (PIFF) module. The PIFF module selects the well-exposed features from the multi-exposure features processed by the Multi Scale Recursive Feature Enhancement (MSRFE) block. Finally, the fused features are input to the Curve Adjustment (CA) block for fine-tuning and provide color enhancement to the fused features. Moreover, we propose the Multiple Exposure Recursive Fusion (MERF) module which estimates the adjustment factors for the CA block with the guidance of multi-exposure features. Experimental results demonstrate that our method outperforms other techniques in terms of image signal-to-noise ratio, structural similarity, and color accuracy on both real and synthetic datasets.
featured: false
url_html: "https://doi.org/10.1016/j.jvcir.2024.104127"
---
