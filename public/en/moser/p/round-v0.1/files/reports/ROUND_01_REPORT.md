# Semi-Autonomous Study of Moser Skewness Fields: Round 1

## — Linear Programming for Support Skewness, Finite Curve Pressure, and the First Adversarial Search

**Date:** July 26, 2026  
**Status:** Exploratory computation; informal proof; non-universal covering certificate  
**Program Scale:** 192 support directions, 60–120 initial rotation phases, linear programming for optimal translation or minimum scale under fixed phase

---

# 1. Content Completed in This Round

This round implements the curve-in-convex-receptacle accommodation problem as two linear programming formulations.

## 1.1 Minimum Receptacle Scale under Fixed Rotation

For a fixed rotation phase $\phi$, find:

$$
\min_{t_x,t_y,s\ge0}s
$$

such that each discrete support direction $\theta_j$ satisfies:

$$
h_\gamma(\theta_j-\phi)
+
t\cdot u_{\theta_j}
\le
s h_C(\theta_j).
$$

Therefore, it is not necessary to brute-force scan translations for each rotation phase; the optimal translation is directly obtained via linear programming.

## 1.2 Minimum Positive Skewness under Fixed Scale

For a fixed $s$ and $\phi$, find:

$$
\min_{t_x,t_y,e\ge0}e
$$

subject to:

$$
h_\gamma(\theta_j-\phi)
+
t\cdot u_{\theta_j}
-
s h_C(\theta_j)
\le e.
$$

This makes $e$ the minimax positive skewness over the discrete angular domain.

---

# 2. Baseline Receptacles

This round compares:

| Receptacle | Area |
|---|---:|
| Radius $1/2$ Disk | 0.785398163 |
| Radius $1$, $30^\circ$ Sector | 0.261799388 |
| $1/1.0048$ Scaled Wetzel Triangle | 0.260956240 |

The Wetzel triangle uses:

$$
a=\frac{3+4\sqrt3}{18},
\qquad
b=\frac{4+\sqrt3}6,
$$

and uses the certified ratio:

$$
s_W=\frac1{1.0048}
$$

for scaling.

---

# 3. Numerical Results of the First Round

A total of 35 baseline and random curves were tested. For each receptacle, the maximum critical scale within the finite curve library is:

$$
s_{\max}^{\mathrm{circle}}
=
0.99986613,
$$

$$
s_{\max}^{\mathrm{sector}}
=
0.99986614,
$$

$$
s_{\max}^{\mathrm{Wetzel}}
=
0.95783224.
$$

These values only represent the pressure exerted by the current finite curve library and cannot serve as a covering proof for all unit arcs.

## 3.1 Highest Pressure Curves for the Wetzel Triangle

| Rank | Curve | Segments | Critical Scale | Active Directions |
|---:|---|---:|---:|---:|
| 1 | U_equal | 3 | 0.95783224 | 50 |
| 2 | arc_270 | 64 | 0.92558266 | 3 |
| 3 | random_18_5s | 5 | 0.91949625 | 3 |
| 4 | random_11_3s | 3 | 0.91790686 | 66 |
| 5 | semicircle | 64 | 0.91463171 | 3 |
| 6 | random_09_7s | 7 | 0.91106549 | 82 |
| 7 | segment | 1 | 0.91086346 | 145 |
| 8 | V_120 | 2 | 0.91086230 | 113 |
| 9 | random_06_12s | 12 | 0.90486549 | 66 |
| 10 | random_16_6s | 6 | 0.90204401 | 82 |

## 3.2 Adversarial Search

Using a population of 18 curves, 5 generations of lightweight mutation search were conducted. The critical scale of the final candidate curve relative to the certified Wetzel triangle is:

$$
s_\ast
=
0.9187329185.
$$

Its optimal placement has approximately 3 discrete active directions.

Shrinking the receptacle to $98\%$ of this candidate's critical scale:

$$
s_{\mathrm{test}}
=
0.9003582601,
$$

the optimal placement still leaves a maximum positive skewness of:

$$
E
=
3.6918923462e-03.
$$

---

# 4. Preliminary Structural Findings

## 4.1 Translation Can Indeed Be Viewed as First-Order Mode Elimination

Under a fixed phase, the translation term is:

$$
t_x\cos\theta+t_y\sin\theta.
$$

It only occupies the first-order sine and cosine modes of the Fourier series. Therefore, the optimal translation can be understood as eliminating the first-order components of the support skewness field.

## 4.2 Rotation is a Phase Shift of the Support Field

Curve rotation only changes:

$$
h_\gamma(\theta-\phi).
$$

Thus, rotation search is not an ordinary two-dimensional geometric search, but rather the phase alignment of periodic support signals.

## 4.3 What Truly Pressurizes the Receptacle are the High-Order Peaks Remaining After Translation

Once the first-order modes are absorbed by translation, the remaining high-order positive skewness peaks correspond to:

- Corners, long edges, and asymmetric structures of the curve's convex hull;
- Mismatches between the normal sectors of the receptacle and the curve;
- Jumps in the optimal contact set.

This provides more research information than merely recording "whether it fits."

## 4.4 The Hardest Finite Curve at This Stage Does Not Equal the Global Hardest Curve

The current curve families are mainly low-segment-count polylines and smooth arc approximations. Existing research has pointed out that restricting to a fixed number of segments is insufficient to solve the full Moser's worm problem. Therefore, the correct purpose of this search is to discover pressure patterns and contact topologies, rather than treating the highest-scoring curve as the global extremum.

---

# 5. Claims Not Made in This Round

1. No new upper or lower bounds for Moser's worm problem are proposed;
2. Not all unit arcs are verified;
3. The 599 SOCP models are not redone;
4. Interval certificates are not used;
5. Formalization is not completed;
6. There is no proof that the current adversarial curve is a critical curve.

---

# 6. Research Nodes for Round 2

The next round will autonomously select the most informative direction from the following:

1. **Classification of Active Contact Topologies**: Cluster active support directions to study the number and sequence of contacts;
2. **Phase Jump Fields**: Scan rotation phases and record when the optimal translation and active directions mutate;
3. **Adversarial Generation of Support Spectra**: Generate curve pressure directly on high-order Fourier modes;
4. **Local Shrinkage Tests of Receptacles**: Search for support directions that have long been unused by the finite curve library;
5. **Stronger Curve Generators**: Introduce variable segment counts, curvature fragments, and branch retention.

The results of this round lean towards prioritizing items 2 and 1: first understanding the phase jumps and contact topologies of optimal placements, and then expanding curve generation.