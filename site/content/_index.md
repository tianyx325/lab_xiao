---
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: markdown
    id: hero
    content:
      title: 智能感知与决策实验室
      subtitle: IPD Lab · 西安理工大学
      text: |-
        聚焦大模型与智能体、弱光视觉、深度估计，做能落地的感知与决策研究。

        欢迎有志于智能感知与决策研究的同学加入实验室。
    design:
      columns: '1'

  - block: team-showcase
    id: advisors
    content:
      title: 导师团队
      user_groups:
        - 导师
      sort_by: weight
      sort_ascending: true
    design:
      show_role: true
      show_organizations: false
      show_interests: false
      show_social: true
      max_columns: 3
      show_empty_groups: false

  - block: collection
    id: research
    content:
      title: 研究方向
      filters:
        folders:
          - research
    design:
      view: card
      columns: 2

  - block: collection
    id: papers
    content:
      title: 代表性论文
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: recent-papers
    content:
      title: 近期论文
      filters:
        folders:
          - publications
    design:
      view: citation
---
