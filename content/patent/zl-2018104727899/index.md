---
title: "小鼠视频多维特征值的提取方法及视频分类方法"
summary: "面向实验动物行为分析，提出小鼠视频多维特征值提取及分类方法，支撑行为量化评估与自动视频分类。"
date: 2021-10-22
application_date: 2018-05-17
authors:
  - admin
  - 刘欢
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201810472789.9"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN108664942B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/e3/b3/35/5284ad9383ab19/CN108664942B.pdf"
---

实验小鼠的活动轨迹若靠人工计时和描点，重复性和可靠性都有限。

公开说明书用空白场景做蒙版，与当前帧差分得到只含小鼠的图像，再计算质心并映射到活动区域。由此提取路径、直线率、转角和各分区停留时间，作为多维行为特征。说明书给出的自动提取可靠性在 95% 以上。这些特征再送入卷积神经网络，对实验组和对照组视频进行分类。边缘使用 Canny，形状描述使用具有平移、尺度和旋转不变性的图像矩。
