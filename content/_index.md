---
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    id: hero
    content:
      title:
      subtitle: ''
      text: '{{< lab-hero >}}'
    design:
      columns: '1'
      spacing:
        padding: ['3rem', '1.5rem', '2.5rem', '1.5rem']
      css_class: lab-hero-section

  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="导师团队" >}}'
    design:
      columns: '1'
      css_class: lab-block-head

  - block: people
    content:
      title:
      user_groups:
        - 导师
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: false
      css_class: lab-people-section

  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="学术成果" >}}'
    design:
      columns: '1'
      css_class: lab-block-head

  - block: markdown
    content:
      title:
      text: '{{< lab-outcomes-grid count="3" >}}'
    design:
      columns: '1'
      css_class: lab-outcomes-section

  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="新闻动态" >}}'
    design:
      columns: '1'
      css_class: lab-row-head

  - block: markdown
    content:
      title:
      text: '{{< lab-news-list count="6" >}}'
    design:
      columns: '1'
      css_class: lab-news-section lab-last
---
