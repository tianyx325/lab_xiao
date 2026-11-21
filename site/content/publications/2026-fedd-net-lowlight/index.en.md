---
title: 'FEDD-Net: A Frequency Diagonal Feature Enhanced Dual-Branch Diffusion Network
  for Low-Light Image Enhancement'
authors:
- li-wen-gai
- admin
- su-haonan
- Qifeng Guo
date: '2026-04-21T00:00:00Z'
publication_types:
- paper-conference
publication:
  name: 2026 IEEE International Conference on Acoustics, Speech and Signal Processing
    (ICASSP)
  pages: 8757-8761
summary: Separates high/low frequencies with dual-tree complex wavelets, applies cross-attention
  across directions in the frequency domain to enhance diagonal features, and generates
  low-frequency structure and high-frequency detail via two diffusion paths.
abstract: 'Mainstream diffusion-based low-light image enhancement (LLIE) still suffers
  from feature noises, induced blur, and color distortion, especially in the presence
  of directional feature deterioration. To address these limitations, we propose a
  Frequency diagonal feature-Enhanced Dual-branch Diffusion network (FEDD-Net) for
  low-light image enhancement. Unlike existing methods, FEDD-Net employs the dual-tree
  complex wavelet transform (DTCWT) to separate high-frequency details from the low-frequency
  background. Most importantly, the DTCWT enables an effective diagonal feature latent
  enhancement via computing cross-attention between features in different directions
  in the frequency domain. Another important finding is that the low-frequency and
  high-frequency components can be well generated with two separate diffusion paths,
  enabling targeted enhancement of global structures and local details, and effectively
  suppressing blur and color distortions. Compared to state-of-the-art methods, FEDD-Net
  yields notable improvements in both visual quality and quantitative performance.
  Ablation studies further validate the effectiveness and generalization of the proposed
  modules. The code and supplementary material are available at https://github.com/CodeSet1/FEDD-Net.

  '
featured: true
tags:
- 弱光增强
- 深度学习
hugoblox:
  ids:
    doi: 10.1109/icassp55912.2026.11462537
links:
- type: url
  url: https://doi.org/10.1109/icassp55912.2026.11462537
- type: code
  url: https://github.com/CodeSet1/FEDD-Net
ccf: C
publication_short: ICASSP
research:
- low-light
---
