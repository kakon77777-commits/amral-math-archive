# Center-Generated Kakeya-Moser Bridging Families: Round 4

## ——Fourier Curvature Function Spaces, Adjoint Sensitivity, and Non-Convex Container Reduction

**Version:** v0.4  
**Date:** July 27, 2026  
**Status:** Finite-dimensional function space candidates + semi-verified curvature boxes + finite-family non-convex container candidates

---

# 1. Research Questions

Fix:

\[
(L,\rho,\tau)
=
(1,0.04,\pi).
\]

This round simultaneously investigates:

1. Whether increasing the degrees of freedom of the curvature function can break through the Round 3 convex container;
2. How much of the previously measured container pressure is caused by convexification itself.

---

# 2. Fourier Curvature Function Space

\[
g_M(s)
=
\sum_{m=1}^M
\left[
a_m\cos(2\pi ms)
+
b_m\sin(2\pi ms)
\right],
\]

\[
\kappa_M(s)
=
\frac{
\pi e^{g_M(s)}
}{
\int_0^1e^{g_M(u)}du
}.
\]

This parameterization automatically satisfies:

\[
\kappa_M(s)>0,
\qquad
\int_0^1\kappa_M(s)ds=\pi.
\]

---

# 3. Dimension Progression

For the Round 3 convex container:

\[
E_6=0.042842089939,
\]

\[
E_8=0.044261255904,
\]

\[
E_{10}=0.045871358626.
\]

From the 8-mode to the 10-mode, it still increases by:

\[
3.6377%.
\]

Therefore, the Fourier dimension has not yet shown clear convergence.

![Mode Tension](../figures/01_tension_vs_modes.png)

---

# 4. Fourier-10 Candidate

Complete congruence branches:

\[
E_+=0.045871364037,
\]

\[
E_-=0.045871358626.
\]

Chirality difference:

\[
5.410603673428e-09.
\]

Sampled maximum curvature:

\[
24.500033481718.
\]

Outward-style curvature box:

\[
\max\kappa
\in
[
24.478974504951,
24.521117582109
].
\]

Therefore:

\[
\frac1{\max\kappa}
\ge
0.040781175517
>
0.04.
\]

Tubular area replay error:

\[
-9.320805660629e-08.
\]

![Curvature Profiles](../figures/02_fourier_curvature_profiles.png)

---

# 5. Spectrum and Sensitivity

All 10 modes have non-zero coefficient amplitudes; the adjoint sensitivity of the active width branch is also distributed across multiple modes.

The coefficient amplitude of the 1st mode is not large, but its gradient sensitivity is very high; the 2nd mode has the largest amplitude, yet it is not the one with the largest marginal gradient.

Therefore:

\[
\text{Coefficient amplitude}
\not\Rightarrow
\text{Container tension sensitivity}.
\]

![Coefficient Spectrum](../figures/03_mode_amplitudes.png)

![Gradient Spectrum](../figures/04_mode_sensitivity.png)

---

# 6. Adjoint Gradient

\[
\delta\kappa(s)
=
\kappa(s)
\left[
\delta g(s)
-
\frac1\pi
\int_0^1\kappa(u)\delta g(u)du
\right].
\]

\[
\delta\gamma(s)
=
\int_0^s
N(u)
\left[
\int_0^u\delta\kappa(v)dv
\right]du.
\]

If the support point \(s_\ast\) in direction \(n\) is unique:

\[
\delta h_\gamma(n)
=
n\cdot\delta\gamma(s_\ast).
\]

Numerical verification:

\[
\max|D^{\mathrm{FD}}-D^{\mathrm{adj}}|
=
7.537290719695e-05,
\]

Relative \(L^2\) error:

\[
1.194240584988e-03.
\]

![Adjoint Verification](../figures/08_adjoint_verification.png)

---

# 7. Convex Finite-Family Container

After adding Fourier-10, the active skeleton is:

\[
\text{Round 3 dual-frequency logarithmic curvature curve}
+
\text{Round 4 Fourier-10 curve}.
\]

The constant-curvature semicircle and the remaining old families all have negative support tension.

Common convex thickened container:

\[
A_{\mathrm{convex}}
=
0.305379358034.
\]

![Convex Container](../figures/05_convex_pair_container.png)

---

# 8. Non-Convex Finite-Family Container

After incorporating all seven test families:

\[
A_{\mathrm{raw}}
=
0.191049126345
\]

It is a connected union with one small hole.

After filling the hole:

\[
A_{\mathrm{sc}}
=
0.191444211669.
\]

Reduction relative to the convex container:

\[
37.3094%.
\]

![Non-Convex Container](../figures/06_nonconvex_all_families.png)

![Area Comparison](../figures/07_container_area_comparison.png)

---

# 9. Structural Assessment

The active families in the convex and non-convex problems are different.

The support function only records the convex hull; the non-convex container must also record:

- Grooves;
- Narrow channels;
- Local voids;
- Complementary interlocking between tubular boundaries.

Therefore:

\[
\text{Convex support redundancy}
\not\Rightarrow
\text{Non-convex container redundancy}.
\]

The Round 1 finite-width family is already redundant in the convex problem, but still has a non-zero contribution in the non-convex container leave-one-out analysis; the Archimedean family, however, can be completely absorbed by the other six families.

---

# 10. Honest Bounds

This round does not prove:

1. The 10-mode is the global optimum in the Fourier space;
2. The Fourier dimension has converged;
3. The convex dual-skeleton container is the global minimum;
4. The non-convex seven-family container is the global minimum;
5. The seven families represent the complete bridging curve family;
6. The floating-point boxes are Arb/MPFI interval certificates;
7. This round forms a new bound for the Kakeya or Moser problem.

---

# 11. Next Natural Milestone

Round 5 should establish an alternating adversarial system:

\[
\kappa^{(n+1)}
=
\arg\max_\kappa
\inf_g
\mathcal E
(T_\rho(\gamma_\kappa),C^{(n)}),
\]

\[
C^{(n+1)}
=
\operatorname{Prune}
\left[
C^{(n)}
\cup
gT_\rho(\gamma_{\kappa^{(n+1)}})
\right].
\]

Specifically including:

1. Fourier/B-spline adjoint gradient updates;
2. Non-convex container signed-distance or level-set updates;
3. Using the eroded set \(C\ominus\rho B\) to determine the placement of thickened curves;
4. Establishing local distance tension for the active boundaries of grooves;
5. Synchronous refinement of the Fourier dimension and container grid;
6. Migrating the final finite certificates to interval arithmetic.

---

# 12. Conclusion

Round 4 yields two complementary facts:

\[
\text{Increasing the curvature function dimension can still increase the convex support tension},
\]

but at the same time:

\[
\text{The convexification cost is approximately } 37.31\% \text{ of the current finite-family container area}.
\]

Therefore, the subsequent true hard case should not merely be maximizing the convex support gap, but rather searching for:

\[
\boxed{
\text{New curvature functions that cannot be placed using existing non-convex grooves, channels, and local complementary structures}.
}
\]