---
title: Depth Estimation
date: 2026-10-13
weight: 30
placeholder_art: depth
summary: "Addressing both standard and degraded scenarios, this direction studies depth estimation under monocular, low-light, and event-camera conditions, exploring semantic guidance, multimodal fusion, and robust 3D perception methods."
tags:
  - depth estimation
---

Addressing both standard and degraded scenarios, this direction studies depth estimation methods that recover 3D structure from 2D observations, covering monocular vision, low-light conditions, and emerging sensing modalities such as event cameras, serving the front end of 3D perception, reconstruction, and decision-making.

### Direction Overview

Depth estimation is the key link between 2D perception and 3D understanding. The lab focuses on depth models that remain stable under difficult conditions such as missing texture, poor illumination, and fast motion, and explores how semantic information and multimodal sensing complement geometric estimation, providing reliable 3D cues for subsequent reconstruction, navigation, and interaction.

### Research Topics

- **Estimate monocular depth**: monocular depth estimation with semantically guided geometric reasoning
- **Handle degraded scenarios**: robust depth estimation under low light and low texture
- **Fuse event cameras**: event-camera depth estimation and multimodal fusion with conventional cameras
- **Constrain depth consistency**: scale recovery and uncertainty modeling for depth results
- **Validate downstream tasks**: application validation for reconstruction, focusing, and scene understanding

### Key Challenges

- **Scale ambiguity**: geometric ambiguity in monocular settings
- **Boundary degradation**: detail loss caused by low light and motion blur
- **Heterogeneous alignment**: spatio-temporal alignment and fusion strategies across RGB / event sensors
- **Error propagation**: propagation and controllability of depth errors in downstream tasks

### Technical Approach

- **Introduce semantic priors**: improve estimation quality at structural boundaries and in planar regions
- **Design robust features**: build feature representations and training strategies for low-light and event data
- **Joint multi-task learning**: enhance stability and transferability of depth estimation through consistency losses
