---
title: Human Action Recognition
date: 2026-10-13
weight: 40
placeholder_art: action
summary: Focusing on human behavior understanding, this direction studies skeleton-based
  and visual-feature-based action recognition methods, covering spatio-temporal modeling,
  robust representation, and behavior understanding applications in real-world scenarios.
tags:
- Action recognition
---

Focusing on human behavior understanding, this direction studies methods for recognizing and analyzing actions from videos and skeleton sequences, emphasizing spatio-temporal modeling and robustness in real-world scenarios, serving applications such as human-computer interaction, intelligent surveillance, and behavior analysis.

### Direction Overview

Human action recognition requires jointly characterizing appearance, posture, and temporal dynamics. The lab works along two paths: skeleton-based representation and visual features. Skeleton sequences are computationally efficient and relatively robust to appearance changes, while visual features retain richer scene and interaction information. The two can be modeled independently or fused complementarily to improve recognition under complex actions and occlusion.

### Research Topics

- **Model skeleton sequences**: skeleton-based action recognition with graph convolution / temporal modeling
- **Learn spatio-temporal features**: spatio-temporal feature learning and long-term dependency modeling for action sequences
- **Fuse dual-path features**: complementary recognition frameworks combining visual and skeleton features
- **Strengthen robust representation**: behavior understanding under occlusion, viewpoint changes, and noise
- **Validate real-world scenarios**: data collection, evaluation, and system demonstrations for deployment

### Key Challenges

- **Fine-grained discrimination**: high inter-class similarity between actions makes separation difficult
- **Representation stability**: occlusion, multiple viewpoints, and background clutter cause drift
- **Long-term dependencies**: wide time spans with sparse key frames
- **Distribution gap**: laboratory data differs from real deployment environments

### Technical Approach

- **Model graph structures**: represent joint relations with skeleton graphs, capture action dynamics with temporal networks
- **Introduce attention**: combine keyframe selection to improve long-sequence modeling efficiency
- **Advance multimodal fusion**: enhance real-world generalization through complementary features and data augmentation
