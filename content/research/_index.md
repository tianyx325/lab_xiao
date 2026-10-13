---
title: 研究方向
date: 2026-10-13
type: landing
# lead ← lab-research-lead shortcode（seo_description）
summary: ''

sections:
  - block: markdown
    content:
      title:
      text: |
        <div class="lab-list-page">
          <header class="lab-list-header">
            <div class="container">
              <h1 class="lab-list-title">研究方向</h1>
              <p class="lab-list-lead">{{< lab-research-lead >}}</p>
            </div>
          </header>
          <div class="lab-list-body container">
            <div class="lab-list-grid lab-list-grid--research">
              {{< lab-research-cards count="99" >}}
            </div>
          </div>
        </div>
    design:
      columns: '1'
      css_class: lab-list-section lab-list-shell
---
