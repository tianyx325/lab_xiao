---
title: Low-Light Vision Enhancement
date: 2026-10-13
weight: 20
summary: "Addressing low illumination and complex lighting, this direction studies image/video enhancement, denoising, and feature representation, improving the usability of downstream tasks such as focusing, matching, and reconstruction under low-light conditions."
tags:
  - low-light enhancement
---

Targeting degraded scenarios such as low illumination, high noise, and complex lighting, this direction studies the restoration, enhancement, and robust feature representation of visual information, so that enhanced results are not only "better looking" but also serve downstream tasks such as focusing, matching, optical flow, and reconstruction.

### Direction Overview

Low-light imaging commonly suffers from low signal-to-noise ratio, drowned-out details, and color distortion. The lab advances along two lines: enhancement-reconstruction and task-driven research. One line improves the visual quality of images/videos; the other learns feature representations that are more friendly to downstream geometric and motion estimation. Related work covers low-light optical flow (e.g., CEDFlow, latent-feature-supervised siamese networks) and the National Natural Science Foundation of China (NSFC) General Program project "Research on Light Field Feature Computation Enhancement Theory and Methods for Low-Light Autofocusing".

### Research Topics

- Low-light image / video enhancement, denoising, and color correction
- Feature representation, optical flow, and motion estimation under low-light conditions
- Enhancement and feature computation methods for autofocusing, matching, and reconstruction
- Combining low-light scenarios with computational imaging such as light fields
- Customized low-light enhancement algorithms and system validation for practical applications

### Key Challenges

- Under extreme low illumination, details and noise are hard to balance, prone to over-smoothing or artifacts
- Misalignment between enhancement and downstream task objectives, leading to "better visuals, worse tasks"
- Complex distribution of real low-light data; evaluation and generalization remain challenging

### Technical Approach

- Joint modeling in the image domain and latent space, strengthening contour, texture, and motion consistency
- Constraining enhancement networks with task losses (focusing, optical flow, matching, etc.) to achieve task-oriented enhancement
- Incorporating multi-dimensional imaging information such as light fields to improve feature separability and stability under low-light conditions
