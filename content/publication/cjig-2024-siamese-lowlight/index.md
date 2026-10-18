---
title: "隐特征监督的孪生网络弱光光流估计"
authors:
- admin
- 苏展
- Fengyuan Zuo
- Haiyan Jin
date: "2024-01-01T00:00:00Z"
publishDate: "2024-01-01T00:00:00Z"
doi: "10.11834/jig.230093"
publication_types: ["article-journal"]
publication: "*中国图象图形学报*, 29(1):231-242"
publication_short: "中国图象图形学报"
volume: "29"
issue: "1"
pages: "231-242"
abstract: |
  **目的**　弱光照条件下成像存在信噪比低、运动模糊等问题，这对光流估计带来了极大挑战。与现有“先增强—再估计”的光流估计方法不同，为了避免在弱光图像增强阶段损失场景的运动信息，提出一种隐特征监督的弱光光流估计孪生网络学习方法。

  **方法**　首先，该方法采用权重共享的孪生网络提取可映射的弱光光流和正常光照光流特征；进而，计算弱光邻帧图像的 K 近邻相关性卷表，以解决计算 4D 全对相关性卷表的高时空复杂度问题；在全局运动聚合模块中引入针对二维运动特征的注意力机制，以降低弱光条件下强噪声、运动模糊及低对比度对光流估计的不利影响。最后，提出隐特征监督的光流估计模块，采用正常光照光流特征监督弱光照光流特征的学习，实现高精度的光流估计。

  **结果**　与 3 种最新光流估计方法的对比实验表明，在正常光照条件下，本文方法取得了与现有最佳光流估计方法相近的性能。在 FCDN（flying chairs dark noise）数据集上，本文方法光流估计性能最优，相较于次优方法端点误差精度提升了 0.16；在多亮度光流估计（various brightness optical flow，VBOF）数据集上，本文方法端点误差精度提升了 0.08。

  **结论**　本文采用权重共享的双分支孪生网络，实现了对正常光照和弱光照光流特征的准确编码，并采用监督学习方式实现了高精度的弱光照光流估计。实验结果表明，本文方法在弱光光流估计精度及泛化性方面均具有显著优势。本文代码可在 https://github.com/suzhansz/LLCV-net.git 下载。
summary: "提出隐特征监督的孪生网络，以正常光照运动特征监督弱光光流学习，避免先增强再估计时丢失运动信息。"
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
projects: []
---

{{< figure src="framework.png" alt="论文框架图" caption="论文框架图" >}}
