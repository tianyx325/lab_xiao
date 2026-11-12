---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
first_name: ""   # 可选，拼音/英文，用于排序与 SEO
last_name: ""
superuser: false
role: 研一
# 入学年份（研究生填，如 2025）：lint 每年自动提醒学籍与分组是否一致
enroll_year:
weight: 1
bio: "研究方向为……。"
# 所属研究方向（可多选）：agent | low-light | depth | action
# 卡片展示文字由方向页标题自动派生，无需另填短句
research:
  - depth
user_groups:
  - 研一
# 个人主页（可选）：GitHub / 个人学术页
personal_url: ""
# 毕业去向（可选，仅毕业生填）：如「华为 · 算法工程师」「读博 @ 西安交通大学」
destination: ""
# email: ""
# social:   # 仅放 GitHub / Scholar / 主页等，邮箱信封由 email 自动生成
#   - icon: github
#     icon_pack: fab
#     link: 'https://github.com/xxx'
---

**姓名**，西安理工大学计算机科学与技术学院**硕士研究生**（研一），导师：肖照林教授。

**研究方向：** （同学自填表述，与上方 research 标签可不同）
