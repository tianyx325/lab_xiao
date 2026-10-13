---
title: 成员
date: 2022-10-24
# lead 由 lab.ui.people_lead / lab.name 自动生成；勿在此写死实验室名
summary: ''

type: landing

sections:
  - block: people
    content:
      title: 成员
      subtitle: ''
      # 分组名称需与每位成员 profile 里的 user_groups 一致
      user_groups:
          - 导师
          - 博士生
          - 研三
          - 研二
          - 研一
          - 本科生
          - 毕业生
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: false
      css_class: lab-people-section lab-list-shell
---
