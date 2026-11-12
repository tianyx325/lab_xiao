---
title: Large Models and Agent Applications
date: 2026-10-13
weight: 10
summary: "Focusing on large language models and agents, this direction studies task planning, tool use, and multi-agent collaboration, promoting application deployment, evaluation, and decision-making capabilities in vertical scenarios."
tags:
  - agent
  - large models
---

Focusing on large language models and agents, this direction centers on building decision-making capabilities within the closed loop of "perception — planning — execution": enabling models to understand task goals, invoke external tools and knowledge, and deliver measurable, deployable intelligent applications in vertical scenarios.

### Direction Overview

The lab treats large models as composable cognitive and decision-making components, conducting research on single-agent capability enhancement, multi-agent collaboration, and domain knowledge injection, with systematic validation in scenarios such as culture and tourism and education. Related practice includes application explorations such as the university culture-and-tourism large model "Yijian Boguan: Zhihui Wanxiang" (a large model for culture and tourism).

### Research Topics

- Application modeling, prompt engineering, and effectiveness evaluation of large models in vertical scenarios
- Task planning, tool use, and external knowledge retrieval augmentation for single agents
- Multi-agent collaboration: role division, task allocation, and negotiation mechanisms
- Multi-step reasoning, decision trajectories, and controllable generation for complex tasks
- System integration for deployment: interface specifications, safety boundaries, and human-agent collaboration workflows

### Key Challenges

- In open environments, task goals are ambiguous and tool interfaces are heterogeneous, making planning prone to failure
- Consistency, conflict resolution, and cost control in multi-agent collaboration
- Effective integration of domain knowledge with general model capabilities and hallucination suppression
- Lack of unified, reproducible evaluation protocols for application effectiveness

### Technical Approach

- Characterize the planning process with task graphs / workflows, combining retrieval and tool use to reduce hallucinations
- Design observable agent execution logs and evaluation metrics to support iterative optimization
- Build demonstration systems in vertical scenarios, connecting data, models, and user interfaces
