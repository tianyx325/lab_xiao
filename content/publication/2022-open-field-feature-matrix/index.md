---
title: "面向旷场实验视频分类的特征拼接矩阵学习方法"
authors:
- "admin"
- "杨志林"
- "刘欢"
- "金海燕"
date: "2022-01-01T00:00:00Z"
doi: "10.11834/jig.210606"
publication_types: ["article-journal"]
publication: "中国图象图形学报"
publication_short: "中国图象图形学报"
volume: "27"
issue: "3"
pages: "988-1000"
summary: "从旷场视频提取行为特征并与运动路径图拼接成矩阵，再用卷积神经网络区分两组小鼠。"
abstract: |
  **目的**　旷场实验（open field test，OFT）是行为学与药理实验分析中常用的实验方法。为了对比测试组和参考组被测小鼠的行为特征差异，通常需要耗费大量精力对旷场实验数据进行处理和观测。由于旷场实验数据量大且较依赖观测人员的主观判断，导致对小鼠行为差异观测的精度较低且缺乏量化评价指标。为此，本文提出一种基于卷积神经网络（convolutional neural networks，CNN）的旷场实验视频分类方法，可基于量化特征对两组小鼠的行为差异自动分类。

  **方法**　从视频空域和时域中提取22维的小鼠运动行为特征，经过量化后生成特征矩阵，进而以矩阵拼接方式构造可学习的行为特征矩阵样本，利用不同结构卷积神经网络对提取的行为特征矩阵样本进行训练和分类，并分析网络结构对分类结果的影响，在实现两组小鼠分类的基础上，对不同维度小鼠行为特征对分类精度的重要性进行评价。

  **结果**　在真实旷场实验数据集上的实验分析表明，本文算法的分类准确率为99.25%。此外，由实验结果分析发现小鼠的大角度转向频次、停留区域与时间对小鼠分类的重要性高于其他维度特征。

  **结论**　提出的特征拼接矩阵学习方法能够准确识别两组小鼠旷场实验视频的差异，本文方法的分类准确率明显优于现有人工分析及经典机器学习方法。
tags:
- "open field test (OFT)"
- "behavioral analysis"
- "video classification"
- "spliced feature matrix"
- "convolutional neural network (CNN)"
featured: false
url_html: "http://cjig.ijournals.cn/jig/ch/reader/view_abstract.aspx?file_no=210606"
url_pdf: "https://www.cjig.cn/rc-pub/front/front-article/download/55711408/lowqualitypdf/%E9%9D%A2%E5%90%91%E6%97%B7%E5%9C%BA%E5%AE%9E%E9%AA%8C%E8%A7%86%E9%A2%91%E5%88%86%E7%B1%BB%E7%9A%84%E7%89%B9%E5%BE%81%E6%8B%BC%E6%8E%A5%E7%9F%A9%E9%98%B5%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95.pdf"
---
