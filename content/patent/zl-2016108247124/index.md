---
title: "多视环境中基于水平集函数演化的非刚性目标场景流估计方法"
summary: "面向多视计算机视觉，提出基于水平集函数演化的非刚性目标场景流估计方法，提升复杂形变场景下的运动与结构估计能力。"
date: 2019-06-14
application_date: 2016-09-14
authors:
  - 李秀秀
  - 郑江滨
  - 金海燕
  - admin
  - 赵明华
tags:
  - 发明专利
  - 已授权
patent_number: "ZL201610824712.4"
patent_status: "granted"
url_patent: "https://patents.google.com/patent/CN106384361B/zh"
url_pdf: "https://patentimages.storage.googleapis.com/55/60/aa/d9be7be638f4db/CN106384361B.pdf"
---

把各摄像机的光流分别算完再拼成场景流，标定误差和噪声容易造成断裂和空洞。

公开说明书用环绕摄像机采集同步视频，经背景减法和体素着色得到初始外形，并用水平集表示该曲面。下一时刻的演化同时受三类约束：体素运动前后在各视角中的颜色一致、投影必须落在侧影内，以及水平集保持为符号距离函数。曲面停在新外形上时，对应的速度场就是场景流。演化只在零水平集附近的窄带内进行，避免每次重新初始化。
