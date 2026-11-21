---
title: ''
summary: ''
date: 2022-10-24
type: landing

sections:
  - block: markdown
    id: hero
    content:
      title: Intelligent Perception & Decision Lab
      subtitle: IPD Lab · Xi'an University of Technology
      text: |-
        Large models and agents, low-light vision, and depth estimation — perception and decision research that ships.

        We welcome motivated students to join the lab.
    design:
      columns: '1'

  - block: team-showcase
    id: advisors
    content:
      title: Faculty
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
      title: Research
      filters:
        folders:
          - research
    design:
      view: card
      columns: 2

  - block: collection
    id: papers
    content:
      title: Featured Publications
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
      title: Recent Publications
      filters:
        folders:
          - publications
    design:
      view: citation
---
