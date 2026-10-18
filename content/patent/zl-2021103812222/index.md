---
title: "一种证件数字图像的光场防篡改采集装置及防篡改方法"
summary: "面向证件图像安全，提出光场防篡改采集装置及方法，利用光场信息增强证件数字图像的防伪与溯源能力。"
date: 2024-02-02
application_date: 2021-04-09
authors:
  - admin
  - 苏展
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202110381222.2"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN113192008B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/3b/81/90/247f9478316395/CN113192008B.pdf"
---

证件图像被电子修改后，普通扫描件往往只剩二维外观，采集端本身缺少可复核的角度信息。

装置包括光场相机、证件固定架和恒定光源，以及处理与存储单元。采集时先解码出五维光场，抽出子孔径图像并堆成水平、垂直 EPI。随后在 EPI 上检测 SIFT 特征，并用结构张量计算斜线的位置和角度，形成关键信息对比码。再次核验时重复采集，用结构相似性比较两次 EPI；说明书中以相似性达到 0.90 以上作为未篡改的判定。
