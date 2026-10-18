---
title: "基于孪生卷积网络和特征混合的 sift 误匹配检测方法"
summary: "面向特征匹配可靠性，提出基于孪生卷积网络与特征混合的 SIFT 误匹配检测方法，降低错误对应关系对后续几何估计的影响。"
date: 2023-04-07
application_date: 2021-03-30
authors:
  - admin
  - 李锐源
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202110339794.4"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN113128518B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/38/34/97/48272fde239e59/CN113128518B.pdf"
---

SIFT 匹配之后常用 RANSAC 或函数拟合剔除外点，但单一几何模型容易把正确对应一并删掉，图匹配方法又往往计算过重。

公开说明书在 SIFT 对应点上增加一步误匹配判别。孪生卷积网络分别查看一对匹配点的局部图像，再与坐标、描述子等特征混合，判断该对应是内点还是外点。目标是减少只靠几何残差造成的误判，让后续单应或基础矩阵估计用到更干净的匹配集。
