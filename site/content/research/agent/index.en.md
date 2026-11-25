---
title: Large Models and Agent Applications
date: 2026-10-13
weight: 10
placeholder_art: agent
summary: Focusing on large language models and agents, this direction studies task
  planning, tool use, and multi-agent collaboration, promoting application deployment,
  evaluation, and decision-making capabilities in vertical scenarios.
tags:
- Large models
- Agents
---

Focusing on large language models and agents, this direction centers on building decision-making capabilities within the closed loop of "perception — planning — execution": enabling models to understand task goals, invoke external tools and knowledge, and deliver measurable, deployable intelligent applications in vertical scenarios.

### Direction Overview

The lab treats large models as composable cognitive and decision-making components, conducting research on single-agent capability enhancement, multi-agent collaboration, and domain knowledge injection, with systematic validation in scenarios such as culture and tourism and education. Related practice includes application explorations such as the university culture-and-tourism large model "Yijian Boguan: Zhihui Wanxiang" (a large model for culture and tourism).

### Research Topics

- **Model vertical applications**: application modeling, prompt engineering, and effectiveness evaluation of large models
- **Enhance single agents**: task planning, tool use, and external knowledge retrieval augmentation
- **Organize multi-agent collaboration**: role division, task allocation, and negotiation mechanisms
- **Control reasoning processes**: multi-step reasoning, decision trajectories, and controllable generation for complex tasks
- **Integrate deployable systems**: interface specifications, safety boundaries, and human-agent collaboration workflows

### Key Challenges

- **Planning failures**: ambiguous task goals and heterogeneous tool interfaces in open environments
- **Collaboration consistency**: conflict resolution and cost control across multi-agent systems
- **Knowledge fusion**: integrating domain knowledge with general capabilities and suppressing hallucinations
- **Missing evaluation**: lack of unified, reproducible protocols for application effectiveness

### Technical Approach

- **Characterize task graphs**: express planning with task graphs / workflows, reduce hallucinations via retrieval and tool use
- **Build evaluation loops**: design observable execution logs and evaluation metrics to support iterative optimization
- **Construct demonstration systems**: connect data, models, and user interfaces in vertical scenarios
