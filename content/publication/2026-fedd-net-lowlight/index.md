---
title: "FEDD-Net: A Frequency Diagonal Feature Enhanced Dual-Branch Diffusion Network for Low-Light Image Enhancement"
authors:
- "li-wen-gai"
- "admin"
- "su-haonan"
- "Qifeng Guo"
date: "2026-04-21T00:00:00Z"
doi: "10.1109/icassp55912.2026.11462537"
publication_types: ["paper-conference"]
publication: "2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)"
pages: "8757-8761"
publication_short: "ICASSP"
summary: "用双树复小波分开高低频，并在频域对不同方向做交叉注意力以增强对角特征，再由两条扩散路径分别生成低频结构和高频细节。"
abstract: |
  Mainstream diffusion-based low-light image enhancement (LLIE) still suffers from feature noises, induced blur, and color distortion, especially in the presence of directional feature deterioration. To address these limitations, we propose a Frequency diagonal feature-Enhanced Dual-branch Diffusion network (FEDD-Net) for low-light image enhancement. Unlike existing methods, FEDD-Net employs the dual-tree complex wavelet transform (DTCWT) to separate high-frequency details from the low-frequency background. Most importantly, the DTCWT enables an effective diagonal feature latent enhancement via computing cross-attention between features in different directions in the frequency domain. Another important finding is that the low-frequency and high-frequency components can be well generated with two separate diffusion paths, enabling targeted enhancement of global structures and local details, and effectively suppressing blur and color distortions. Compared to state-of-the-art methods, FEDD-Net yields notable improvements in both visual quality and quantitative performance. Ablation studies further validate the effectiveness and generalization of the proposed modules. The code and supplementary material are available at https://github.com/CodeSet1/FEDD-Net.
featured: false
url_html: "https://doi.org/10.1109/icassp55912.2026.11462537"
url_code: "https://github.com/CodeSet1/FEDD-Net"
---
