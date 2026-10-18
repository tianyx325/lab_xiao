---
title: "FCRNet: Learning non-linear correspondences variation via a graph-based feature embedding for false correspondence removal"
authors:
- "Ruiyuan Li"
- "admin"
- "Meng Zhang"
- "Haiyan Jin"
- "su-haonan"
date: "2026-01-01T00:00:00Z"
doi: "10.1016/j.patcog.2025.111903"
publication_types: ["article-journal"]
publication: "Pattern Recognition"
publication_short: "Pattern Recognition"
volume: "169"
pages: "111903"
summary: "提出图特征嵌入网络 FCRNet，用可学习频率响应拟合一致与非一致的正确匹配，从而剔除错误对应。"
abstract: |
  This article addresses the critical challenge of false correspondence removal in image feature matching. While existing approaches predominantly rely on the assumption of motion consistency to distinguish correct correspondences, the non-consistent but correct correspondences are frequently disregarded, leading to poor performance in scenes with complex structures. This study proposes an innovative false correspondence removal network (FCRNet), which designs a learnable frequency response function h(λ) to better fit the motion of both consistent and non-consistent correct correspondences. Instead of extracting pixel-based 2D movements, we introduce a graph-based Motion-Fitting Residual Layer (MFRL) to extract high-dimensional motion-fitting residual features, effectively capturing the 3D geometrical variation of matching pairs. Furthermore, an adaptive loss function is adopted to balance and train using the two distinct types of correct correspondences. The principal contribution of FCRNet lies in leveraging a graph-based learning model to fit the non-consistent complex motion patterns of a minority correct correspondences, which are often overlooked by previous methods. Extensive experiments demonstrate that the proposed FCRNet outperforms existing algorithms in terms of precision for false correspondence removal and camera pose estimation. The code for this study is available at https://github.com/Livsdjo/FCRNet-Network-code.
featured: false
url_html: "https://doi.org/10.1016/j.patcog.2025.111903"
url_code: "https://github.com/Livsdjo/FCRNet-Network-code"
---
