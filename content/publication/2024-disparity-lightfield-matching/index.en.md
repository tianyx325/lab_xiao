---
title: "A Disparity-Guided Feature Matching Metric for Light Fields (Invited)"
authors:
- "张萌"
- "金海燕"
- "admin"
- "左逢源"
date: "2024-01-01T00:00:00Z"
doi: "10.3788/lop241287"
publication_types: ["article-journal"]
publication: "激光与光电子学进展"
publication_short: "激光与光电子学进展"
volume: "61"
issue: "16"
pages: "1611012"
summary: "The Fourier disparity layer is used to construct a scale-disparity space, and projection transformations across viewpoints are learned by minimizing the reprojection error to measure light field feature matching."
abstract: |
  Existing image feature matching methods still have considerable limitations when dealing with complex scenes such as illumination changes and geometric deformations, because the metric of feature matching lacks depth information and global constraints. To address this problem, a disparity-guided feature matching metric method for light fields is proposed. The Fourier disparity layer decomposition is applied to light field data to construct a scale-disparity space, from which light field features containing disparity information are extracted. Based on the projection transformation relationship model of light field features across different viewpoints, a feature matching metric model relying on light field depth cues is constructed. An artificial neural network is employed to learn the solution of the projection transformation model parameters with the minimization of the reprojection error as the objective function, and an iterative optimization approach is adopted to accurately solve for the optimal projection transformation model, ultimately achieving accurate measurement of feature point matching. Experimental results on light field feature matching datasets show that, compared with existing mainstream feature matching methods, the proposed disparity-guided light field feature matching metric model achieves better matching accuracy and robustness for scenes with illumination changes, geometric deformations, non-Lambertian reflective surfaces, repeated textures, and significant depth variations.
featured: false
url_html: "https://doi.org/10.3788/lop241287"
research:
  - depth
---
