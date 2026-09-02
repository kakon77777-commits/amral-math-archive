# Semi-Autonomous Study of the Moser Skew Field: Round 7

## ——Polygonal-Circular Arc Hybrid Families, Curvature Concentration, and the Value of Discrete Vertices

**Date:** July 26, 2026  
**Status:** Exploratory numerical study; non-formal proof; non-interval certificate  
**Continuation:** Moser Skew Lab v0.6  
**Container:** Wetzel certified triangle  
**Research Question:** Are the nearly parallel bilateral wings from Rounds 3 to 6 coarse discrete approximations of smooth, low-curvature wings, or are they finite contact skeletons relying on discrete vertices?

---

# 1. Control Model

The event 5-link from Round 5 serves as the explicit control:

$$
s_{\mathrm{event}}
=
0.998903757132509.
$$

It has two nearly parallel segments on each side and a horizontal segment in the center.

This round compares two types of extensions:

1. Segmented curvature wings, where each side is split into $m=2,3,4,6,8$ segments;
2. A continuous model, where each side is replaced by a circular arc of constant curvature.

All models maintain mirror symmetry, thus preventing any single-chirality false elevations.

---

# 2. Segmented Curvature Wings

The direction on each side transitions monotonically from:

$$
\alpha\longrightarrow\beta
$$

Segment lengths are allocated using an exponential bias parameter, and the directional transition is controlled by a curvature power law. The entire curve consists of:

$$
2m+1
$$

segments.

| Segments per side $m$ | Total segments | Critical scale | Relative to event root | Distance to 1 | $\alpha$ | $\beta$ |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 0.998530736905809 | -3.730e-04 | 1.469e-03 | 83.330319 | 80.407857 |
| 3 | 7 | 0.998735916360649 | -1.678e-04 | 1.264e-03 | 82.925851 | 81.607056 |
| 4 | 9 | 0.998695140056995 | -2.086e-04 | 1.305e-03 | 84.392977 | 78.728097 |
| 6 | 13 | 0.998839177646286 | -6.458e-05 | 1.161e-03 | 83.588284 | 80.656043 |
| 8 | 17 | 0.998808279772033 | -9.548e-05 | 1.192e-03 | 83.636154 | 81.387381 |

The best segmented extension found so far is:

$$
m=6,
$$

$$
s_{\mathrm{seg}}
=
0.998839177646286.
$$

Relative to event root:

$$
s_{\mathrm{seg}}-s_{\mathrm{event}}
=
-6.457948622285e-05.
$$

Contact signature:

```json
{
  "left": [
    3,
    4
  ],
  "bottom": [
    0
  ],
  "hypotenuse": [
    7
  ]
}
```

This signature differs from the four-event skeleton of Round 5, indicating that the multi-segment curvature wing has indeed entered a different local placement mechanism; however, the pressure remains relatively low at present.

---

# 3. Necessary Search Audit

The segmented parameter family for $m=2$ theoretically contains the event 5-link.

However, the unified heuristic search in this round only found:

$$
0.998530736905809,
$$

which is significantly lower than the explicit event control:

$$
0.998903757132509.
$$

Therefore:

$$
\boxed{
\text{Heuristic search failed to return to the known control solution}
}
$$

is a warning in itself.

Thus, the results for each $m$ in this round cannot be claimed as the global optimum for that segmented family, but only as:

> The best candidates found under a unified, low-compute search budget.

All conclusions use the event control as a hard baseline, rather than mistaking the heuristic failure of $m=2$ for a curvature effect.

---

# 4. Continuous Constant Curvature Wings

Each side wing is replaced by a circular arc of length $w$, with the tangent angle varying linearly from:

$$
\alpha\longrightarrow\beta
$$

The central horizontal straight segment is retained:

$$
l_0=1-2w.
$$

Final equalized parameters:

$$
w=0.335463343870,
$$

$$
l_0=0.329073312260,
$$

$$
\beta=80.129063238^\circ,
$$

$$
\alpha=84.460551713^\circ,
$$

$$
\alpha-\beta=4.331488475^\circ.
$$

Constant curvature:

$$
\kappa=-0.225356173125.
$$

---

# 5. Analytic Verification of Arc Supports

The outer search phase used high-density arc sampling to reduce computational costs.

The final candidate no longer relies on sampling points, but instead computes the three linear functionals of the triangle individually:

1. Arc endpoints;
2. Intra-arc stationary points where the normal is perpendicular to the tangent;
3. Central straight segment endpoints.

Therefore, the final fixed-phase scale is an analytic support calculation within the circular arc model.

The control branches are:

- Low-phase cusp;
- $120^\circ$;
- $270^\circ$.

After equalization:

$$
m_1=0.998862397495093,
$$

$$
m_2=0.998862397495092,
$$

$$
m_3=0.998862397495093.
$$

Branch gap:

$$
9.992007221626e-16.
$$

The complete analytic phase audit yields:

$$
\boxed{
s_{\mathrm{arc}}
=
0.998862397495093
}.
$$

Relative to event root:

$$
s_{\mathrm{arc}}-s_{\mathrm{event}}
=
-4.135963741603e-05.
$$

Distance to certification scale:

$$
1-s_{\mathrm{arc}}
=
1.137602504907e-03.
$$

---

# 6. Final Ranking

| Rank | Model | Critical scale | Relative to event root |
|---:|---|---:|---:|
| 1 | event_control | 0.998903757132509 | +2.220e-16 |
| 2 | continuous_circular_wing_equalized | 0.998862397495093 | -4.136e-05 |
| 3 | segmented_m6 | 0.998839177646286 | -6.458e-05 |
| 4 | segmented_m8 | 0.998808279772033 | -9.548e-05 |
| 5 | segmented_m3 | 0.998735916360649 | -1.678e-04 |
| 6 | segmented_m4 | 0.998695140056995 | -2.086e-04 |
| 7 | segmented_m2 | 0.998530736905809 | -3.730e-04 |

The event 5-link remains the highest model in this round.

The constant curvature circular arc wing is higher than the best segmented heuristic candidate, but still lower than the discrete event skeleton:

$$
s_{\mathrm{event}}-s_{\mathrm{arc}}
=
4.135963741603e-05.
$$

---

# 7. Curvature Concentration Working Proposition

The data from this round does not support:

> The 5-link is merely a coarse approximation of a smooth constant curvature wing.

Instead, it supports the following weaker, yet more precise working proposition:

$$
\boxed{
\text{In the mirror-symmetric wing family of this round, continuously flattening the finite turn releases a small amount of congruent accommodation pressure.}
}
$$

The discrete event skeleton concentrates the total turning angle at the vertices between segments; the constant curvature wing distributes the same turning angle across the entire side wing.

The numerical loss is approximately:

$$
4.14\times10^{-5}.
$$

Thus, the effective factor might not be "whether there is curvature," but rather:

$$
\boxed{
\text{The concentration position of curvature on the curve parameter}
}
$$

and how it controls:

- Dual contact at the endpoints and hypotenuse;
- Contact of the internal vertices with the left and bottom edges;
- Simultaneous equalization of multiple phase cusps;
- The timing of active support point switching.

---

# 8. Limits of Inference

This round cannot deduce that:

1. All smooth curves are lower than polygonal chains;
2. All variable curvature wings are lower than the 5-link;
3. The 5-link is the global optimum for the complete 5-segment family or all curves;
4. The heuristic candidates for segmented $m>2$ are the global optima of their respective families;
5. Discrete vertices are absolutely necessary for the Moser problem as a whole.

Constant curvature is only a highly restricted form of smoothing. A more general curvature distribution might concentrate the turn in a small region while keeping the curve smooth.

---

# 9. Resolution Audit of the Best Segmented Candidate

| Initial phase grid | Critical scale | Best phase | Number of local minima |
|---:|---:|---:|---:|
| 4096 | 0.998839177646367 | 0.138875813036 | 7 |
| 8192 | 0.998839177646274 | 0.138875813041 | 7 |
| 16384 | 0.998839177646278 | 0.138875813041 | 7 |
| 32768 | 0.998839177646286 | 0.138875813040 | 7 |
| 65536 | 0.998839177646280 | 0.138875813040 | 7 |
| 131072 | 0.998839177646271 | 0.138875813041 | 7 |

The results remain stable after local refinement, indicating that the numerical value is not a false elevation caused by the phase grid.

---

# 10. Directions for Round 8

The next round will not return to simply increasing the number of polygonal segments, but will investigate:

## 10.1 Controllable Curvature Concentration Families

Let the tangent angle of the side wing be:

$$
\theta(s)
=
\beta
+
(\alpha-\beta)F(s),
$$

where $F$ is no longer fixed as linear, but allows for:

- Sigmoid concentration;
- Piecewise constant curvature;
- Biarc (dual curvature);
- Narrow turning layers that approximate vertices but remain $C^1$.

The research question is:

$$
\text{As the curvature concentration width }\varepsilon\to0,
\qquad
s_\varepsilon
\to
s_{\mathrm{event}}
\ ?
$$

## 10.2 Curvature Concentration Limit

If the smooth family converges to the event 5-link as $\varepsilon\to0$, then discrete vertices can be understood as:

$$
\boxed{
\text{The singular limit of smooth curvature concentration}
}
$$

rather than a completely different type of curve.

## 10.3 New Ledger Fields

The next round will add:

$$
(
\text{Total turning angle},
\text{Peak curvature},
\text{Curvature support width},
\text{Curvature centroid},
\text{Branch scale}
).
$$

This will formally expand the skew field into a triple ledger of "curvature-contact-phase."

---

# 11. Limitations

1. The segmented families use finite heuristic search;
2. The unified search budget failed to reproduce the $m=2$ control solution;
3. The circular arc model only allows constant curvature;
4. The junction between the central straight segment and the circular arcs still has a large turning angle;
5. The global optimum of the curvature family has not been established;
6. No new Moser upper or lower bounds have been proposed;
7. No formalization or interval proofs have been conducted.

---

# 12. Conclusion

Final results of this round:

$$
s_{\mathrm{event}}
=
0.998903757132509,
$$

$$
s_{\mathrm{arc}}
=
0.998862397495093,
$$

$$
s_{\mathrm{seg,best}}
=
0.998839177646286.
$$

The current ranking is:

$$
\boxed{
\text{Discrete event 5-link}
>
\text{Constant curvature circular arc wing}
>
\text{Best multi-segment curvature candidate of this round}.
}
$$

Therefore, what should be investigated in Round 8 is not the dichotomy of "smooth vs. non-smooth," but rather:

$$
\boxed{
\text{How narrow and where the curvature should be concentrated to maintain the minimax balance of the four contact branches.}
}
$$