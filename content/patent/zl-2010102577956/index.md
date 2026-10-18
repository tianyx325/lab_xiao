---
title: "高分辨率实时全景高动态范围图像获取装置与方法"
summary: "面向虚拟现实与图像处理需求，提出高分辨率实时全景高动态范围图像获取装置与方法，实现 360° 全景数字图像的高效采集与合成。"
date: 2011-11-30
application_date: 2010-08-19
authors:
  - 王庆
  - 周果清
  - admin
  - 吴文杰
  - 李磊
  - 纪超
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201010257795.6"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN101963751B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/17/6c/a3/d4f68612b4d87d/CN101963751B.pdf"
---

单台鱼眼相机做全景高动态范围成像时，边缘分辨率下降，也无法一次覆盖无畸变的 360° 场景。

装置把不少于五台水平朝外的相机均匀固定在工作台圆周上，光轴交于圆心，另有一台相机在中心垂直向上。每台相机使用水平视角不小于 150° 的超广角镜头，相邻视角保持重叠。先测光，再以正确曝光为中心生成九档曝光序列并同步快门。图像用棋盘格上的 Harris 角点求畸变系数，按相机位置拼接成全景，再由多曝光全景合成一张高动态范围图像。
