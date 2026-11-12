---
title: Human Action Recognition
date: 2026-10-13
weight: 40
summary: "Focusing on human behavior understanding, this direction studies skeleton-based and visual-feature-based action recognition methods, covering spatio-temporal modeling, robust representation, and behavior understanding applications in real-world scenarios."
tags:
  - action recognition
---

Focusing on human behavior understanding, this direction studies methods for recognizing and analyzing actions from videos and skeleton sequences, emphasizing spatio-temporal modeling and robustness in real-world scenarios, serving applications such as human-computer interaction, intelligent surveillance, and behavior analysis.

### Direction Overview

Human action recognition requires jointly characterizing appearance, posture, and temporal dynamics. The lab works along two paths: skeleton-based representation and visual features. Skeleton sequences are computationally efficient and relatively robust to appearance changes, while visual features retain richer scene and interaction information. The two can be modeled independently or fused complementarily to improve recognition under complex actions and occlusion.

### Research Topics

- Skeleton-based human action recognition with graph convolution / temporal modeling
- Spatio-temporal feature learning and long-term dependency modeling for action sequences
- Fusion frameworks combining visual and skeleton features
- Robust behavior understanding under occlusion, viewpoint changes, and noise
- Data collection, evaluation, and system demonstrations for real-world scenarios

### Key Challenges

- Inter-class similarity between actions makes fine-grained discrimination difficult
- Occlusion, multiple viewpoints, and background clutter destabilize representations
- Long-term actions span wide time ranges with sparse key frames
- Distribution gap between laboratory data and real deployment environments

### Technical Approach

- Model joint relations with skeleton graph structures, combined with temporal networks to capture action dynamics
- Introduce attention and keyframe selection to improve long-sequence modeling efficiency
- Enhance generalization in real-world scenarios through multimodal fusion and data augmentation
