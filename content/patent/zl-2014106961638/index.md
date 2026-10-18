---
title: "可变角度采样数的光场采集装置"
summary: "面向计算机视觉与光学工程，提出可变角度采样数的光场采集装置，在灵活采样配置下获取更高质量的光场数据。"
date: 2017-07-21
application_date: 2014-11-26
authors:
  - 王庆
  - 张春萍
  - 周果清
  - 韩舒
  - admin
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201410696163.8"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN104469110B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/cf/6b/be/f17bbaa20bb386/CN104469110B.pdf"
---

聚焦型微透镜光场相机的角度采样数由主镜头、微透镜和传感器的相对位置决定，出厂后通常不能按场景调整。

公开说明书把平凸微透镜阵列装在滑动托盘上，托盘可沿光轴在主镜头和传感器之间移动。外围调节环通过推动杆改变这段距离，弹簧使托盘回位，位移传感器把位置送给 FPGA。控制按角度采样数与高斯成像关系设定微透镜到焦平面的距离，并相应调整光圈。角度采样降低时空间分辨率更高，采样提高时则保留更多三维信息。
