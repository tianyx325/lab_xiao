---
title: "{{ replace .Name "-" " " | title }}"
# 获奖人：成员填 slug，外协填姓名全名
authors:
  - admin
# 获奖日期（列表年份取此字段，唯一日期字段）
date: {{ .Date.Format "2006-01-02" }}
summary: ""
# 级别（枚举）：national | provincial | university | society
level: "provincial"
# 等级（可选枚举）：special | first | second | third | excellent
rank: "second"
# 主题标签（可选）：级别与等级已由上方字段表达，勿再填
tags: []
---
