---
title: "一种结合图像语义与坐标关系的特征误匹配检测方法"
summary: "面向特征匹配纠错，提出结合图像语义与坐标关系的误匹配检测方法，融合语义与几何约束筛选不可靠对应点。"
date: 2025-03-28
application_date: 2021-12-27
authors:
  - admin
  - 李锐源
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202111614081.0"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN114359600B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/05/be/df/575ad094cce228/CN114359600B.pdf"
---

SIFT、SURF 等匹配在视角、尺度或光照变化较大时仍会产生误匹配。只靠坐标离群点或 RANSAC 拟合基础矩阵，又容易漏掉语义上明显不合理的对应。

公开说明书把每个匹配点对的 32×32 邻域图像块和全部匹配点的坐标一起送入网络。语义支路提取邻域特征，坐标支路描述点对之间的几何关系，两者融合后做正确匹配与错误匹配的二分类。另一路参数化网络由图像块生成部分坐标网络的权重。训练样本由自动匹配加人工标注得到，每个样本包含两幅图像上的一批匹配点对。
