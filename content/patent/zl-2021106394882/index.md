---
title: "基于 Yolo-v4 网络结构光伏面板暗斑缺陷检测方法"
summary: "面向光伏运维，提出基于 Yolo-v4 的面板暗斑缺陷检测方法，实现红外/可见巡检图像中暗斑目标的自动识别。"
date: 2023-05-02
application_date: 2021-06-08
authors:
  - admin
  - 吴国华
  - 金海燕
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202110639488.2"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN113379703B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/3a/c1/10/9f12d4e33f1ecf/CN113379703B.pdf"
---

光伏组件被遮挡或本身存在缺陷时会出现热斑，红外巡检若仍靠人工判读，效率和一致性都不够。

公开说明书先把红外图像转成灰度图，用 Canny 提取边缘并二值化，再根据连通域特征去掉干扰、框出光伏面板。面板按组串和局部单元编号后，记录存在暗斑的位置、数量和亮度直方图，写成训练标注。检测网络采用 Yolo-v4 结构，在这些标注上学习暗斑目标，从而在巡检图像中直接给出缺陷位置。
