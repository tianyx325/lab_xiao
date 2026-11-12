---
title: "Latent Feature-Supervised Siamese Network for Low-Light Optical Flow Estimation"
authors:
- admin
- 苏展
- Fengyuan Zuo
- Haiyan Jin
date: "2024-01-01T00:00:00Z"
doi: "10.11834/jig.230093"
publication_types: ["article-journal"]
publication: "*中国图象图形学报*, 29(1):231-242"
publication_short: "中国图象图形学报"
volume: "29"
issue: "1"
pages: "231-242"
abstract: |
  **Purpose**　Imaging under low-light conditions suffers from problems such as low signal-to-noise ratio and motion blur, which pose great challenges to optical flow estimation. Unlike existing "enhance-then-estimate" optical flow methods, to avoid losing scene motion information during the low-light image enhancement stage, a Siamese network learning method for low-light optical flow estimation with latent feature supervision is proposed.

  **Methods**　First, a weight-sharing Siamese network extracts mappable low-light and normal-light optical flow features. Then, the K-nearest-neighbor correlation volume of adjacent low-light frames is computed to address the high spatiotemporal complexity of computing the 4D all-pairs correlation volume. An attention mechanism for 2D motion features is introduced into the global motion aggregation module to mitigate the adverse effects of strong noise, motion blur, and low contrast under low-light conditions on optical flow estimation. Finally, a latent feature-supervised optical flow estimation module is proposed, in which normal-light optical flow features supervise the learning of low-light optical flow features to achieve accurate optical flow estimation.

  **Results**　Comparative experiments with three state-of-the-art optical flow estimation methods show that, under normal illumination, the proposed method achieves performance close to the best existing optical flow estimation methods. On the Flying Chairs Dark Noise (FCDN) dataset, the proposed method achieves the best optical flow estimation performance, improving the endpoint error accuracy by 0.16 over the second-best method; on the Various Brightness Optical Flow (VBOF) dataset, the endpoint error accuracy is improved by 0.08.

  **Conclusions**　A weight-sharing dual-branch Siamese network is adopted to accurately encode normal-light and low-light optical flow features, and supervised learning is employed to achieve accurate low-light optical flow estimation. Experimental results show that the proposed method has significant advantages in low-light optical flow estimation accuracy and generalization. The code of this paper is available at https://github.com/suzhansz/LLCV-net.git.
summary: "A latent feature-supervised Siamese network is proposed, in which normal-light motion features supervise the learning of low-light optical flow, avoiding the loss of motion information in the enhance-then-estimate pipeline."
tags:
- 光流估计
- 孪生网络
- 相关性卷表
- 全局运动聚合
- 弱光图像增强
featured: false
url_pdf: "http://cjig.ijournals.cn/jig/ch/reader/create_pdf.aspx?file_no=230093&flag=1&year_id=2024&quarter_id=1"
url_html: "http://cjig.ijournals.cn/jig/ch/reader/view_abstract.aspx?file_no=230093"
url_code: "https://github.com/suzhansz/LLCV-net"
research:
  - low-light
---
