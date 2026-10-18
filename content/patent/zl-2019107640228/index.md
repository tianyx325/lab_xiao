---
title: "一种基于 EPI 的光场图像超分辨的方法"
summary: "面向光场超分辨重建，提出基于 EPI 的光场图像超分辨方法，利用极线图像结构提升空间分辨率与边缘保真。"
date: 2022-10-04
application_date: 2019-08-19
authors:
  - admin
  - 刘崟海
  - 金海燕
  - 杨秀红
  - 蔡磊
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201910764022.8"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN110599400B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/95/9b/88/a20f708e534af6/CN110599400B.pdf"
---

光场相机用空间分辨率换角度分辨率，只增加微透镜数量又会提高硬件成本。

该方法先按相机参数解码光场并抽出子孔径图像，再按行把同一高度的像素拼成 EPI。以中间 EPI 为参考做插值，对其余低分辨率 EPI 估计位移，按残差修正参考图像，完成切片上的超分辨。EPI 重建后会出现伪影，说明书再用去模糊网络处理，最后把像素按提取的逆过程写回子孔径图像，从而同时改善空间和角度方向的细节。
