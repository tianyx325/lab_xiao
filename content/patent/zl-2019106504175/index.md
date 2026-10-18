---
title: "基于生成对抗网络的光场图像轴向超分辨方法"
summary: "面向光场轴向成像，提出基于生成对抗网络的光场图像轴向超分辨方法，改善重聚焦结果的细节清晰度与观感质量。"
date: 2022-10-04
application_date: 2019-07-18
authors:
  - admin
  - 刘崟海
  - 金海燕
  - 蔡磊
  - 杨秀红
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201910650417.5"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN110490968B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/74/9c/72/eb771e39a294ce/CN110490968B.pdf"
---

数字重聚焦通常只能落在整数倍深度上，两个焦面之间的图像无法直接得到。

公开说明书先由光场积分得到一串不同相对深度的重聚焦图像，奇数帧用于训练、偶数帧用于测试。生成网络以连续三帧为输入，学习它们中间深度的图像；多个生成器的结果再交给判别网络做对抗训练，损失同时包含像素误差、VGG 特征和对抗项。训练完成后，用相邻重聚焦帧即可插出非整数深度的图像，使轴向重聚焦更连续。说明书中的测试平均 PSNR 为 30.69。
