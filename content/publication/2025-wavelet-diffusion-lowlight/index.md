---
title: "Diffusion Model with Multi-layer Wavelet Transform for Low-Light Image Enhancement"
authors:
- "Haiyan Jin"
- "Jing Wang"
- "Fengyuan Zuo"
- "su-haonan"
- "admin"
- "Bin Wang"
- "Yuanlin Zhang"
date: "2025-01-01T00:00:00Z"
doi: "10.1109/icassp49660.2025.10888098"
publication_types: ["paper-conference"]
publication: "ICASSP"
publication_short: "ICASSP"
pages: "1-5"
summary: "用多层小波变换代替卷积上下采样，在扩散模型中提取多尺度特征并做全局细化，用于弱光增强。"
abstract: |
  Low-light image enhancement methods based on diffusion models, though effective in improving image quality, often overrely on noise sensitivity and neglect the reconstruction deviations due to the naive up- and down-sampling operations. To address this issue, we propose a novel diffusion model, MWT-Diff, which utilizes multi-layer wavelet transforms to replace up-and down-sampling based on convolutions for extracting high-order features of different scales while mitigating representation degradations. Specifically, MWT-Diff is based on the U-Net architecture; it encodes four local features after the frequency-based down-sampling at each layer and fuses the enhanced four components during the up-sampling process. Additionally, we incorporate global refinement branches to mitigate information loss and employ efficient soft gate aggregation for feature fusion and reconstruction. Extensive quantitative and qualitative experiments demonstrate that our model achieves state-of-the-art performance on benchmark datasets. Code is available at: https://github.com/lalalulao/MWT-Diff.
featured: false
url_html: "https://doi.org/10.1109/icassp49660.2025.10888098"
url_code: "https://github.com/lalalulao/MWT-Diff"
---
