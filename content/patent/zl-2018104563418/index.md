---
title: "一种基于超像素分割的视频摘要生成方法"
summary: "面向视频理解与摘要生成，提出基于超像素分割的视频摘要方法，在保留关键内容的同时压缩冗余镜头信息。"
date: 2019-07-23
application_date: 2018-05-14
authors:
  - 金海燕
  - 李喻蒙
  - admin
  - 李秀秀
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201810456341.8"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN108600865B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/c1/d6/f7/fad021a64ee810/CN108600865B.pdf"
---

按固定聚类数或只看颜色差挑选关键帧，容易留下冗余镜头，也需要事先指定类别数。

该方法先把视频切成等长片段，用帧间光流估计运动幅度，并在片段边界附近选取运动局部最小的帧作为候选关键帧。每帧转到 CIELAB 与坐标组成的五维空间做超像素分割，再按颜色和边界代价合并区域。相邻关键帧若超像素区域差异低于阈值，则删去其中一帧。说明书在 YouTube 视频集上比较精度、召回率和 F 值，所给方法的平均 F 值为 0.54。
