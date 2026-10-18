---
title: "A Channel-Wise Guidance Sparse Transformer for Effective Dark Image Enhancement"
authors:
- "Haiyan Jin"
- "Yifan Shuai"
- "Fengyuan Zuo"
- "su-haonan"
- "admin"
- "Bin Wang"
- "Yuanlin Zhang"
date: "2024-01-01T00:00:00Z"
doi: "10.1109/icme57554.2024.10687442"
publication_types: ["paper-conference"]
publication: "ICME"
publication_short: "ICME"
pages: "1-6"
summary: "用通道阈值选出关键表示，并只保留有用的自注意力，再用双向门控前馈重建暗光图像。"
abstract: |
  Dark Image Enhancement (DIE) aims to improve contrast and restore details for captured images under low illumination. Currently, traditional Transformer methods have achieved significant performance in the DIE problem; however, all-pairs correlation computation is redundant in learning key properties and restoring high-order representations. To alleviate this problem, we introduce a Channel-wise Guidance Sparse Transformer framework, namely CGSformer, which not only adaptively selects the key channel-wise representations through a threshold operator, but also keeps the most useful self-attention values for feature restoration guided by the selected information. Besides, we introduce a Bidirectional Gate Feed-Forward (BGFF) network to aggregate features to better facilitate high-quality image reconstruction. The experiments are conducted on representative datasets, showing that our CGSformer consistently achieves state-of-the-art performance on widely used benchmarks.
featured: false
url_html: "https://doi.org/10.1109/icme57554.2024.10687442"
---
