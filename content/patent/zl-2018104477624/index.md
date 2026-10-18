---
title: "一种基于高斯混合模型的宽吻海豚 click 信号检测方法"
summary: "面向水声信号处理，提出基于高斯混合模型的宽吻海豚 click 信号检测方法，提高复杂噪声背景下生物声信号的检出可靠性。"
date: 2020-07-24
application_date: 2018-05-11
authors:
  - 金海燕
  - 张萌
  - admin
  - 李秀秀
tags:
  - 发明专利
  - 已授权
patent_number: "ZL 2018104477624"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN108627241B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/26/86/ea/c1f4cd2c027e4b/CN108627241B.pdf"
---

宽吻海豚的 click 脉冲混在海洋噪声里，固定阈值很难同时保住完整信号和压低背景。

公开说明书对采集声音加滑动汉宁窗并做短时傅里叶变换，得到时间—频率能量图。能量值用两个高斯成分聚类，能量较低的一簇视为噪声，较高的一簇视为 click。阈值取两簇相邻端点的平均值，高于阈值的时频点保留。这样得到的二值时频图用于标出 click 出现的位置，阈值随当前录音自适应，而不是预先写死。
