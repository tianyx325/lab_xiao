---
title: "一种面向电力巡检视频的绝缘子缺损自动检测算法"
summary: "面向电力巡检，提出绝缘子缺损自动检测算法，在巡检视频中定位典型缺损，提高巡检效率与一致性。"
date: 2024-02-06
application_date: 2020-05-26
authors:
  - admin
  - 杨志林
  - 金海燕
  - 杨秀红
tags:
  - 发明专利
  - 已授权
patent_number: "ZL202010452724.5"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN111784633B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/a8/85/6d/6bb883447f0850/CN111784633B.pdf"
---

输电线路巡检视频里，绝缘子是否缺损若完全靠人工查看，难以覆盖全部杆塔。

公开说明书先对绝缘子样本分类并做数据增强，再用卷积神经网络做有无缺损的判别。网络由卷积和池化单元提取图像特征，损失稳定后在测试集上检查分类结果。对通过网络的图像继续提取 HOG 特征，用来确定绝缘子在画面中的大致位置，从而从巡检视频中自动标出需要复核的缺损。
