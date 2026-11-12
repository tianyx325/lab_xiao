---
title: Depth Estimation
date: 2026-10-13
weight: 30
summary: "Addressing both standard and degraded scenarios, this direction studies depth estimation under monocular, low-light, and event-camera conditions, exploring semantic guidance, multimodal fusion, and robust 3D perception methods."
tags:
  - depth estimation
---

Addressing both standard and degraded scenarios, this direction studies depth estimation methods that recover 3D structure from 2D observations, covering monocular vision, low-light conditions, and emerging sensing modalities such as event cameras, serving the front end of 3D perception, reconstruction, and decision-making.

### Direction Overview

Depth estimation is the key link between 2D perception and 3D understanding. The lab focuses on depth models that remain stable under difficult conditions such as missing texture, poor illumination, and fast motion, and explores how semantic information and multimodal sensing complement geometric estimation, providing reliable 3D cues for subsequent reconstruction, navigation, and interaction.

### Research Topics

- Monocular depth estimation and semantically guided geometric reasoning
- Robust depth estimation in degraded scenarios such as low light and low texture
- Event-camera depth estimation and multimodal fusion with conventional cameras
- Consistency constraints, scale recovery, and uncertainty modeling for depth results
- Application validation of depth for reconstruction, focusing, and scene understanding

### Key Challenges

- Scale ambiguity and geometric ambiguity in monocular settings
- Boundary and detail degradation caused by low light and motion blur
- Spatio-temporal alignment and fusion strategies for heterogeneous sensors (RGB / event, etc.)
- Propagation and controllability of depth errors in downstream tasks

### Technical Approach

- Combine semantic and geometric priors to improve estimation quality at structural boundaries and in planar regions
- Design robust features and training strategies for low-light and event data
- Enhance the stability and transferability of depth estimation through multi-task learning and consistency losses
