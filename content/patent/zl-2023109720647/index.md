---
title: "基于 Transformer 的双分支人脸图像关键点检测方法"
summary: "面向人脸分析，提出基于 Transformer 的双分支人脸关键点检测方法，提升复杂姿态与光照条件下的关键点定位精度。"
date: 2025-09-26
application_date: 2023-08-03
authors:
  - admin
  - 魏倩影
  - 郝雯
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202310972064.7"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN117037246B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/ee/78/bd/29ad7b1d81c421/CN117037246A.pdf"
---

人脸关键点在大姿态、遮挡和光照变化下仍然容易偏移。公开说明书指出，卷积网络擅长局部特征，却难以描述规则人脸结构中的远距离关系；直接用全连接层回归坐标又会破坏局部特征。

该方法用双分支同时提取特征。卷积支路经编码器—解码器得到多尺度局部特征，Transformer 支路用窗口自注意力得到全局特征。两路特征按尺度做点乘和通道拼接，再经特征融合模块给出初始关键点。渐进细化模块以这些点为中心裁出局部块，逐次缩小窗口并迭代修正坐标。训练时对初始误差和各次细化误差加权，并用旋转、遮挡和噪声扩充样本。
