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
      background:
        image:
          filename: welcome.png
          filters:
            brightness: 0.55
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['3rem', '1.5rem', '3rem', '1.5rem']
      css_class: fullscreen lab-hero-section
  
  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="导师团队" more="全部" href="people/" >}}'
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
      text: '{{< lab-section-head title="研究方向" more="全部" href="research/" >}}'
    design:
      columns: '1'
      css_class: lab-block-head

  - block: markdown
    content:
      title:
      subtitle: ''
      text: '{{< lab-research-cards >}}'
    design:
      columns: '1'
      css_class: lab-major

  - block: markdown
    content:
      title: 学术成果
      subtitle: ''
      text: ''
    design:
      columns: '1'
      css_class: lab-major lab-pubs-title

  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="论文" more="全部" href="publication/" >}}'
    design:
      columns: '1'
      css_class: lab-row-head

  - block: collection
    content:
      title:
      count: 3
      filters:
        folders:
          - publication
    design:
      view: card
      columns: '1'
      css_class: lab-row-body

  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="专利" more="全部" href="patent/" >}}'
    design:
      columns: '1'
      css_class: lab-row-head

  - block: collection
    content:
      title:
      count: 3
      filters:
        folders:
          - patent
    design:
      view: card
      columns: '1'
      css_class: lab-row-body

  - block: markdown
    content:
      title:
      text: '{{< lab-section-head title="奖项" more="全部" href="award/" >}}'
    design:
      columns: '1'
      css_class: lab-row-head

  - block: collection
    content:
      title:
      count: 3
      filters:
        folders:
          - award
    design:
      view: card
      columns: '1'
      css_class: lab-row-body lab-last
---
