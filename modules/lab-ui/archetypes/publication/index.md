---
title: "{{ replace .Name "-" " " | title }}"
# 作者：成员填 slug（admin / su-haonan 等），外协填姓名全名
authors:
  - admin
date: {{ .Date.Format "2006-01-02T00:00:00Z" }}
doi: ""
# CCF 等级（可选枚举）：A | B | C
ccf: ""
# 论文获奖（可选）：如 Best Paper Honorable Mention
paper_award: ""
# 所属研究方向（外键，可多选）：agent | low-light | depth | action
research: []
# 类型（枚举，勿自创）：article-journal | paper-conference | preprint | report | thesis
publication_types:
  - paper-conference
publication: ""
publication_short: ""
volume: ""
pages: ""
summary: ""
abstract: |
featured: false
url_pdf: ""
url_html: ""
url_code: ""   # 开源代码仓库（可选）
---
