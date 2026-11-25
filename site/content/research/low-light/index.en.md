---
title: Low-Light Vision Enhancement
date: 2026-10-13
weight: 20
placeholder_art: lowlight
summary: Addressing low illumination and complex lighting, this direction studies
  image/video enhancement, denoising, and feature representation, improving the usability
  of downstream tasks such as focusing, matching, and reconstruction under low-light
  conditions.
tags:
- Low-light enhancement
---

Targeting degraded scenarios such as low illumination, high noise, and complex lighting, this direction studies the restoration, enhancement, and robust feature representation of visual information, so that enhanced results are not only "better looking" but also serve downstream tasks such as focusing, matching, optical flow, and reconstruction.

### Direction Overview

Low-light imaging commonly suffers from low signal-to-noise ratio, drowned-out details, and color distortion. The lab advances along two lines: enhancement-reconstruction and task-driven research. One line improves the visual quality of images/videos; the other learns feature representations that are more friendly to downstream geometric and motion estimation. Related work covers low-light optical flow (e.g., CEDFlow, latent-feature-supervised siamese networks) and the National Natural Science Foundation of China (NSFC) General Program project "Research on Light Field Feature Computation Enhancement Theory and Methods for Low-Light Autofocusing".

### Research Topics

- **Restore image quality**: low-light image / video enhancement, denoising, and color correction
- **Represent low-light features**: feature representation, optical flow, and motion estimation under low light
- **Serve downstream tasks**: enhancement and feature computation methods for autofocusing, matching, and reconstruction
- **Combine computational imaging**: integrating light fields and other modalities with low-light scenarios
- **Customize deployable systems**: tailored enhancement algorithms and system validation for practical applications

### Key Challenges

- **Balance detail and noise**: extreme low illumination risks over-smoothing or introducing artifacts
- **Align enhancement with tasks**: objective mismatch leads to "better visuals, worse tasks"
- **Ensure evaluation generalization**: complex distributions of real low-light data challenge evaluation and transfer

### Technical Approach

- **Joint dual-domain modeling**: strengthen contour, texture, and motion consistency across image and latent spaces
- **Apply task losses**: constrain enhancement networks with focusing, optical flow, and matching objectives to achieve task-oriented enhancement
- **Incorporate multi-dimensional imaging**: improve feature separability and stability under low-light conditions with light-field information
