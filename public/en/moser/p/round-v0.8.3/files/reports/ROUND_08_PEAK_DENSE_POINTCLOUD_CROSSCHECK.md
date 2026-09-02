# Round 8 Cross-Validation of Peak Candidate Dense Point Cloud

- Number of curve points: 240017
- Candidate width: $\varepsilon=0.037$
- Stationary point support method: $s=0.998914339084632$
- Global value of the point cloud at the exact cusp: $s=0.998914339084602$
- Method difference: $-2.997602166488e-14$
- Relative event root: $1.058195209325e-05$

Previously, if only a smooth bounded minimizer was used to track the $270^\circ$ branch, it would stop near the cusp and slightly overestimate it; this version has directly incorporated the exact special phases of $120^\circ$ and $270^\circ$ into the global comparison.