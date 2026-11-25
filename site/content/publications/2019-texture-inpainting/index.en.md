---
title: Improved structure tensor for fine-grained texture inpainting
authors:
- Xiuhong Yang
- Baolong Guo
- admin
- Wei Liang
date: '2019-04-01T00:00:00Z'
publication_types:
- article-journal
publication:
  name: 'Signal Processing: Image Communication'
  volume: '73'
  pages: 84-95
summary: Improves the structure tensor with fractional-order differentiation, doubled
  sampling, and non-local regularization, then plugs it into anisotropic PDEs to inpaint
  fine-grained textures.
abstract: 'Partial differential equations (PDEs) have emerged as a useful tool for
  recovering structures when solving image inpainting problems. In the research presented
  in this paper, we extend structure tensor (ST)-based PDE to fine-grained texture
  inpainting by improving the ST with three modifications to enhance its suitability
  to more accurately process fine-grained textures of which the small-scale patterns
  repeat non-locally. These modifications are then inserted into an anisotropic PDE
  to recover damaged textures. The result is a subtly-conducted anisotropic diffusion
  inpainting algorithm free of detail-blurring artifacts produced by the classic tensor
  diffusion model and dislocation deficiencies affecting patch-based completion approaches.
  This is made possible by the following strategies: (1) construct a fractional ST
  (FST Fractional structure tensor. ) composed of the inner product of the fractional
  derivative vector and its transposition to more effectively address complex fractal-like
  texture details because of the characteristics of the fractional differential; (2)
  because FST is composed of the inner product of two vectors, it is necessary to
  represent the tensor at a higher resolution than for the original image to avoid
  spectrum aliasing, which is automatically implemented by the calculation of the
  twofold oversampling fractional derivative (i.e., double-sampling FST, DFST Double-sampling
  fractional structure tensor. ); (3) apply a non-local regularizing method to all
  four channels of the resulting DFST based on the repeatability of textures, which
  integrates non-local geometric characteristics to effectively infer how damaged
  textures extend. Finally, we insert the modified non-locally regularized DFST (NDFST
  Nonlocally-regularized double-sampling fractional structure tensor. ) into an anisotropic
  PDE to effectively guide the diffusion process and design its numerical implementation
  scheme. The experimental results show that, for fine-grained texture images, the
  proposed NDFST is equipped to accurately detect subtle and complex texture features,
  and the resulting NDFST-based PDE is particularly effective not only for recovering
  non-homogeneous structures, but also for the restitution of fine-grained textures.

  '
featured: false
tags:
- Image processing
hugoblox:
  ids:
    doi: 10.1016/j.image.2018.02.006
links:
- type: url
  url: https://doi.org/10.1016/j.image.2018.02.006
publication_short: 'Signal Processing: Image Communication'
---
