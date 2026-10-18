---
title: "一种基于光场角度域变化矩阵的特征点检测方法"
summary: "面向光场特征提取，提出基于角度域变化矩阵的特征点检测方法，提升光场数据中稳定特征点的定位能力。"
date: 2024-02-09
application_date: 2021-04-09
authors:
  - admin
  - 张晶瑞
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202110383372.7"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN113191369B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/5d/16/65/b0df6bc51e740f/CN113191369B.pdf"
---

传统角点和斑点检测主要看单幅图像上的梯度，换一个视角后，非朗伯表面的特征往往不稳定。

该方法先按微透镜参数把光场解码成子孔径图像。在中心视角上用边缘检测取出梯度较大的候选点，再在所有视角的同一像素处计算梯度，排成角度域变化矩阵。以中心视角为基准，若绝大多数视角与中心的梯度差都低于阈值，该点才保留为特征点。这样选出的点利用了视角之间的变化，而不是只依赖单一图像。
