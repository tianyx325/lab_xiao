---
title: "Event-guided low light image enhancement via a dual branch GAN"
authors:
- "Haiyan Jin"
- "Qiaobin Wang"
- "su-haonan"
- "admin"
date: "2023-09-01T00:00:00Z"
doi: "10.1016/j.jvcir.2023.103887"
publication_types: ["article-journal"]
publication: "Journal of Visual Communication and Image Representation"
publication_short: "JVCIR"
volume: "95"
pages: "103887"
summary: "用双分支生成对抗网络从事件流学习梯度，并经注意力融合事件与弱光图像特征，以保留结构并抑制噪声。"
abstract: |
  In the low light conditions, images are corrupted by low contrast and severe noise, but event cameras capture event streams with clear edge structures. Therefore, we propose an Event-Guided Low Light Image Enhancement method using a dual branch generative adversarial networks and recover clear structure with the guide of events. To overcome the lack of paired training datasets, we first synthesize three datasets containing low-light event streams, low-light images, and the ground truth normal-light images. Then, in the generator network, we develop an end-to-end dual branch network consisting of a image enhancement branch and a gradient reconstruction branch. The image enhancement branch is employed to enhance the low light images, and the gradient reconstruction branch is utilized to learn the gradient from events. Moreover, we develops the attention based event-image feature fusion module which selectively fuses the event and low-light image features, and the fused features are concatenated into the image enhancement branch and gradient reconstruction branch, which respectively generate the enhanced images with clear structure and more accurate gradient images. Extensive experiments on synthetic and real datasets demonstrate that the proposed event guided low light image enhancement method produces visually more appealing enhancement images, and achieves a good performance in structure preservation and denoising over state-of-the-arts.
featured: false
url_html: "https://doi.org/10.1016/j.jvcir.2023.103887"
---
