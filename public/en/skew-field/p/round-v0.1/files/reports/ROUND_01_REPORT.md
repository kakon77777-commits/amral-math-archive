# Center-Generated Kakeya-Moser Bridging Families: The First Computational Experiment

## — Comparison of Universal Support Tensions among Constant Curvature, Archimedean, Contact-Saturated, and Finite-Width Curvature Stratum

**Version:** v0.1  
**Date:** July 27, 2026  
**Nature:** First-round finite-family computational experiment  
**Status:** Numerical candidate; no global or interval certificates

---

# 1. Experimental Problem

This document fixes:

\[
\boxed{
(L,\rho,\tau)
=
(1,0.04,\pi)
}.
\]

Where:

- \(L=1\): Centerline length;
- \(\rho=0.04\): Thickness radius;
- \(\tau=\pi\): The normal needle completes all unoriented directions.

All valid capless normal bands have the same area:

\[
2\rho L=0.08.
\]

After adding semicircular caps at both ends:

\[
2\rho L+\pi\rho^2
=
0.085026548246.
\]

Therefore, this round does not compare the total individual areas, but rather compares:

\[
\boxed{
\text{The additional support tension exerted by equiareal heteromorphic curves on a common convex container.}
}
\]

---

# 2. Four Curve Families

1. Constant curvature semicircle;
2. Archimedean spiral;
3. Contact-saturated smooth spiral with a local radius of curvature reaching \(\rho\);
4. Finite-width curvature stratum obtained via finite-budget max-min search.

![Four Centerlines](../../../../skew-field/p/round-v0.1/files/figures/01_centerline_families.png)

![Curvature Profiles](../../../../skew-field/p/round-v0.1/files/figures/02_curvature_profiles.png)

| Curve Family | Max Curvature | Min Local Radius of Curvature | Endpoint Radius | Individual Convexified Thickened Area |
|---|---:|---:|---:|---:|
| Constant curvature semicircle | 3.141593 | 0.318310 | 0.636620 | 0.229646 |
| Archimedean spiral | 6.045121 | 0.165423 | 0.671205 | 0.224205 |
| Contact-saturated smooth spiral | 24.977599 | 0.040036 | 0.675004 | 0.210486 |
| Finite-width curvature stratum | 22.518355 | 0.044408 | 0.773010 | 0.204626 |

The contact-saturated family satisfies numerically:

\[
\max\kappa
\approx
\rho^{-1}
=
25.
\]

The finite-width curvature stratum satisfies:

\[
\max\kappa
\approx
22.518355
<
25.
\]

Thus, it does not generate pressure by exceeding the local curvature upper bound.

---

# 3. Common Convex Thickened Container

For configurations \(g_i\in SE(2)\), let:

\[
H
=
\operatorname{conv}
\left(
\bigcup_i g_i\gamma_i
\right).
\]

The common thickened container is:

\[
C_\rho=H\oplus\rho B.
\]

Its area is:

\[
\mu_2(C_\rho)
=
\mu_2(H)
+
\rho\operatorname{Per}(H)
+
\pi\rho^2.
\]

The finite-budget optimal value for the first three families is:

\[
\boxed{
A_3
\approx
0.244915072937
}.
\]

After adding the finite-width curvature stratum:

\[
\boxed{
A_4
\approx
0.256259897110
}.
\]

Increment:

\[
A_4-A_3
\approx
0.011344824173.
\]

Relative increment:

\[
\boxed{
4.6321%
}.
\]

![Common Container Area](../../../../skew-field/p/round-v0.1/files/figures/04_common_container_area.png)

![Optimized Common Container](../../../../skew-field/p/round-v0.1/files/figures/08_optimized_common_container.png)

---

# 4. Leave-one-out Support Tension

For each family, a common container is first built using the other three families, then the family is placed back to calculate the minimum \(L^\infty\) support gap.

| Removed Curve Family | Positive Support Tension | Area Increment | Proportion of Active Support Directions |
|---|---:|---:|---:|
| Constant curvature semicircle | 0.011591404 | 0.008575538 | 43.1250% |
| Archimedean spiral | 0.000000000 | 0.000000000 | 0.0000% |
| Contact-saturated smooth spiral | 0.000973210 | 0.000274087 | 1.4583% |
| Finite-width curvature stratum | 0.046058168 | 0.011344824 | 55.5556% |

![Leave-one-out Tension](../../../../skew-field/p/round-v0.1/files/figures/05_leave_one_out_tension.png)

![Leave-one-out Area Increment](../../../../skew-field/p/round-v0.1/files/figures/06_leave_one_out_area_increment.png)

---

# 5. Active Support Directions

In the audit of \(1440\) directions for the four-family common container:

\[
\begin{aligned}
\text{Finite-width curvature stratum}
&\approx
55.5556%,\\
\text{Constant curvature semicircle}
&\approx
43.1250%,\\
\text{Contact-saturated spiral}
&\approx
1.4583%,\\
\text{Archimedean spiral}
&=
0.0000%.
\end{aligned}
\]

![Active Support Shares](../../../../skew-field/p/round-v0.1/files/figures/07_active_support_shares.png)

This indicates that the common container is primarily supported by two complementary geometries:

\[
\boxed{
\text{Constant curvature global skeleton}
+
\text{Finite-width curvature-concentrated skeleton}.
}
\]

---

# 6. First Major Finding

The maximum curvature ordering is not the common container pressure ordering.

The contact-saturated spiral reaches:

\[
\max\kappa\approx25,
\]

but only provides approximately:

\[
1.46%
\]

of the active directions.

The finite-width curvature stratum has a lower maximum curvature, yet it dominates over half of the directions, and its leave-one-out tension reaches:

\[
\boxed{
E_\infty
\approx
0.046058168408.
}
\]

Therefore, this round does not support:

\[
\text{Local reach saturation}
\Rightarrow
\text{Maximum universal container pressure}.
\]

Instead, it supports:

\[
\boxed{
\text{A finite-width curvature distribution and global support configuration,
are more important than a single maximum curvature.}
}
\]

---

# 7. Second Major Finding

The Archimedean spiral is not the largest in individual convexified area, nor does it become an active supporter of the four-family common container.

Its leave-one-out support value is negative:

\[
z
\approx
-0.004327897460,
\]

indicating that it can be strictly placed inside the common central convex hull proxy generated by the other three families.

Therefore, under these parameters and container class:

\[
\boxed{
\text{The Archimedean uniform pitch is not a hard case.}
}
\]

---

# 8. Third Major Finding

The actual area of each complete thickened curve is identical:

\[
0.085026548246.
\]

However, the area of the four-family common convex thickened container is approximately:

\[
0.256259897110.
\]

Its ratio to the individual complete tubular area is:

\[
\boxed{
3.013881.
}
\]

This provides the first concrete numerical example that:

\[
\boxed{
\text{Conservation of individual total measure,
does not imply conservation of universal accommodation cost.}
}
\]

![Equiareal Heteromorphic Comparison](../../../../skew-field/p/round-v0.1/files/figures/03_individual_area_comparison.png)

---

# 9. Feedback to the Meta-Theory

The results of this round provide three points of support for the "Measure-Conserving Skew-Line Fiber—Universal Covering Tension Theory".

## 9.1 The Area Stratum Loses Discriminative Power

The area of all individual normal bands is fixed at:

\[
2\rho L.
\]

Thus, individual areas cannot order the hard cases.

## 9.2 The Skewness Stratum Retains Discriminative Power

Different curvature functions:

\[
\kappa(s)
\]

generate different support functions and different active directions.

## 9.3 The Tension Stratum Completes the Global Ordering

The leave-one-out support tension identifies:

\[
\text{Finite-width curvature stratum}
>
\text{Constant curvature semicircle}
>
\text{Contact-saturated spiral}
>
\text{Archimedean spiral}
\]

as the marginal pressure ordering for this round.

---

# 10. Honest Boundaries

This round has not yet proven:

1. Each of the four curve families is the global optimum within its function family;
2. The common convex container search has reached the global minimum;
3. Non-convex containers would not be smaller;
4. Reflections would not change the ordering;
5. There are no missed support events between the sampled directions;
6. The contact-saturated family possesses a complete interval reach certificate;
7. The finite-width curvature stratum is a hard case for the complete bridging family;
8. These results constitute new bounds for the Kakeya or Moser problems.

This round is the first reproducible experiment under:

\[
\boxed{
\text{Finite curve families}
+
\text{Convex container proxy}
+
\text{Finite-budget search}
}
\]

---

# 11. The Next Natural Node

The second round should proceed with:

1. Parametric KKT / branch contouring for the finite-width curvature stratum;
2. Adding reflections to establish an \(E(2)\) chirality audit;
3. High-precision and interval verification of the reach for the four families;
4. Elevating the directional grid and establishing a support event graph;
5. Testing the area loss caused by convexification using non-convex star-shaped containers;
6. Scanning \(\rho\) and \(\tau\) to study thin-thickness asymptotics;
7. Searching for the existence of a fifth family that simultaneously compresses the remaining directions of the semicircle and the finite-width stratum.

---

# 12. Conclusion

In:

\[
(L,\rho,\tau)=(1,0.04,\pi)
\]

for the first bridging family experiment, all curves possess the same total normal band measure, but their common container pressures are highly different.

The most important result is:

\[
\boxed{
\text{Finite-width curvature concentration}
\text{ generates universal support pressure better than }
\text{local contact saturation.}
}
\]

The primary skeleton of the common container is not a single extreme shape, but rather:

\[
\boxed{
\text{Constant curvature semicircle}
+
\text{Finite-width curvature stratum}
}
\]

acting as complementary active supports.

This is the first concrete computational instance demonstrating that "after total measure is conserved, geometric differences translate into covering tension differences."