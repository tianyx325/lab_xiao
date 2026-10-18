---
title: "油画相似度的表面光场特征点分布鉴别"
authors:
- "admin"
- "孙彤鑫"
- "张晶瑞"
- "金海燕"
date: "2023-10-19T00:00:00Z"
doi: "10.11834/jig.220774"
publication_types: ["article-journal"]
publication: "中国图象图形学报"
publication_short: "中国图象图形学报"
volume: "28"
issue: "10"
pages: "3123-3135"
summary: "用微透镜阵列编码油画表面的角度变化，再按特征点分布多边形的边长和夹角度量表面光场相似度。"
abstract: |
  **目的**　油画区别于其他绘画形式的重要特征之一是其颜料图层存在厚度变化。因此，油画相似度鉴别不仅关注油画的纹理色彩细节，也需考虑其表面颜料厚度的差异。针对颜料厚度的细微变化，提出一种油画相似度的表面光场特征点分布鉴别方法。采用光场成像技术观测由于油画表面厚度起伏导致的不同角度成像的差异，以量化计算油画表面光场的相似性。

  **方法**　该方法采用一块微透镜阵列板对油画表面的角度域变化进行光场编码，利用光场相机采集编码后的油画表面光场。在此基础上，选取油画表面光场中角度域差异大的特征点集合，采用K-Means方法对该特征点集合的二维分布进行多边形向量化描述。进而提出计算关键点连接线的欧氏距离与线段夹角，以度量表面光场特征点分布多边形的相似性。

  **结果**　采用Illum光场相机拍摄了多组真实油画的表面光场实验数据，实验结果表明本文方法可对存在细微颜料厚度差别的油画相似度进行鉴别。在对油画表面光场的识别区分度以及检测精度方面，本文方法显著优于现有图像特征匹配鉴别方法。

  **结论**　实验分析表明，相比于经典交并比及相似度系数，所提出油画相似性度量具有更优的相似性度量精度。通过调整编码板与测试油画表面距离的反复实验，验证所提方法能够有效检测0.5 mm以上厚度变化的表面光场差异。
tags:
- "surface light field"
- "oil painting identification"
- "light field feature"
- "similarity computation"
- "feature extraction"
featured: false
url_html: "http://cjig.ijournals.cn/jig/ch/reader/view_abstract.aspx?file_no=220774"
url_pdf: "http://cjig.ijournals.cn/jig/ch/reader/create_pdf.aspx?file_no=220774&flag=1&year_id=2023&quarter_id=10"
---
