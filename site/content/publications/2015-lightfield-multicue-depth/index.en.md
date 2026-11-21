---
title: Multi-Cue Fused Depth Estimation Based on Light Field Analysis
authors:
- 杨德刚
- admin
- 杨恒
- 王庆
date: '2015-12-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: 计算机学报
  volume: '38'
  issue: '12'
  pages: 2437-2449
summary: Defocus and disparity cues are extracted from the light field captured by
  a camera array and adaptively fused; a Markov random field with adaptive smoothness
  constraints combined with graph cuts is then used to estimate globally consistent
  depth.
abstract: 'Inspired by the depth perception mechanism of human vision and incorporating
  recent advances in light field analysis theory, this paper proposes a globally consistent
  depth estimation method that fuses multiple depth cues. The method first acquires
  light field data with a camera array, then obtains refocused light fields at specified
  depths via synthetic aperture imaging, from which defocus and disparity cues characterizing
  different dimensions of depth variation are extracted. Light field analysis is employed
  to compare the applicability of the defocus and disparity cues, and a multi-cue
  fusion algorithm is designed to achieve complementary advantages of different depth
  cues. Furthermore, to obtain accurate and consistent depth results, a global energy
  function with adaptive smoothness constraints is proposed on the basis of a Markov
  random field model. Finally, the graph cuts algorithm is used to minimize the global
  energy function, yielding smooth and accurate depth estimation results. The proposed
  method is tested on both virtual and real data, and compared with single-cue and
  local depth estimation methods, it combines the advantages of different depth cues
  and produces more robust depth results.

  '
featured: false
tags:
- 光场成像
- 深度估计
- 图像融合
hugoblox:
  ids:
    doi: 10.11897/SP.J.1016.2015.02437
links:
- type: url
  url: http://cjc.ict.ac.cn/online/onlinepaper/ydg-2015112471336.pdf
- type: pdf
  url: http://cjc.ict.ac.cn/online/onlinepaper/ydg-2015112471336.pdf
ccf: A
publication_short: Chinese Journal of Computers
research:
- depth
---
