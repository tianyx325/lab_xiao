---
title: "A Multi-Exposure Generation and Fusion Method for Low-Light Image Enhancement"
authors:
- "Haiyan Jin"
- "Long Li"
- "su-haonan"
- "Yuanlin Zhang"
- "admin"
- "Bin Wang"
date: "2024-06-30T00:00:00Z"
doi: "10.1109/ijcnn60899.2024.10650454"
publication_types: ["paper-conference"]
publication: "IJCNN"
publication_short: "IJCNN"
pages: "1-7"
summary: "按多曝光分布生成不同曝光图像，再用感知重要性和曲线调整做特征融合，以增强弱光图像。"
abstract: |
  In the low light image enhancement, single exposure images contains a limited dynamic range, which hinders the restoration of contrast and texture. To address these problems, we propose a multi exposure generation and fusion method (MEGF) which simulates multi exposure images and perform feature fusion and enhancement on these images. First, we propose a Multi-Exposure Generation (MEG) method, which constructs the Gaussian Distribution for each exposure level based on multi exposure datasets. MEG can generate images with different exposure levels based on the constructed distribution. Then, the Perceptual Importance based Multi-Exposure Feature Enhancement (PIMEFE) block is developed to fuse the feature of generated multi exposure images using VGG-16 network. Before fusion, the generated images are input to Multi Scale Recursive Feature Enhancement (MSRFE) blocks and obtain the denoised and enhanced features. Finally, the fused feature are input to Curve Adjustment (CA) block for fine tuning and provide the color enhancement on fusion features. We propose the Multiple Exposure Recursive Fusion (MERF) block which estimates the adjusting factors for CA block. Experimental results demonstrate that our method outperforms other techniques in both subjective and objective evaluations on real and synthetic datasets.
featured: false
url_html: "https://doi.org/10.1109/ijcnn60899.2024.10650454"
---
