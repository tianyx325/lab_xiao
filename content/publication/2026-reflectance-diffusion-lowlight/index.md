---
title: "Reflectance oriented diffusion with normalizing flow illumination enhancement for the low-light images"
authors:
- "Hang Yang"
- "admin"
- "su-haonan"
date: "2026-06-01T00:00:00Z"
doi: "10.1016/j.jvcir.2026.104819"
publication_types: ["article-journal"]
publication: "Journal of Visual Communication and Image Representation"
publication_short: "JVCIR"
volume: "118"
pages: "104819"
summary: "用归一化流增强光照、用扩散模型恢复反射率细节，并在重组后校正饱和度，以兼顾弱光增强与噪声抑制。"
abstract: |
  Balancing illumination enhancement and noise suppression represents a fundamental challenge in low-light image enhancement (LLIE). Existing methods often suffer from artifacts induced during brightness adjustment, including detail loss, spatially varying illumination, and color distortion. Diverging from conventional single-path diffusion-based LLIE approaches, this paper proposes a novel dual-branch framework. It consists of a normalizing flow branch, a diffusion branch, and a saturation post-adjustment module. These components are designed to enhance illumination, recover details, and optimize saturation, respectively. Following Retinex decomposition, the illumination component is enhanced through the invertible mapping of the normalizing flow. This approach provides a deterministic transformation and effectively minimizes artifacts. Concurrently, the diffusion branch recovers reflectance details while effectively suppressing severe noise inherent in dark regions. Then, a saturation post-adjustment module compensates for saturation degradation arising from the multiplicative recombination of illumination and reflectance. Most importantly, the proposed framework achieves an optimal trade-off between illumination enhancement and detail preservation. Extensive experiments demonstrate state-of-the-art performance, achieving 26.62 dB PSNR/0.94 SSIM on LOL and +1.26/+1.96 dB PSNR gains on LSRW, while improving downstream detection on ExDark to 0.60 mAP@0.5/0.31 AP@[0.5:0.95]. Code is available at https://github.com/yangpipi-01/LLIE.
featured: false
url_html: "https://doi.org/10.1016/j.jvcir.2026.104819"
url_code: "https://github.com/yangpipi-01/LLIE"
---
