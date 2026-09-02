# Center-Generated Kakeya-Moser Bridging Family: Round 2

## — Curvature Saturation Terminology Correction, Quadratic Exponential Limit Family, Chirality Equalization, and Dual-Skeleton Container

**Version:** v0.2  
**Date:** July 27, 2026  
**Status:** High-resolution numerical candidate; no interval or global optimality certificates

---

# 1. Objectives of This Round

Fixed:

\[
(L,\rho,\tau)=(1,0.04,\pi).
\]

The main unresolved issues from Round 1 are:

1. Whether the finite-width curvature layer depends on a single chirality;
2. Whether the parameters merely hit the boundary of the search box;
3. Whether a stable supporting skeleton forms after being added to the common container.

This round switches to the full congruence tension:

\[
E_{\mathrm{cong}}=\min(E_+,E_-).
\]

---

# 2. Terminology Correction

What was referred to as "contact saturation" in Round 1 actually only calibrates:

\[
\max\kappa\approx\rho^{-1}.
\]

This is local radius of curvature saturation, not:

\[
\operatorname{reach}(\gamma)=\rho.
\]

Therefore, it is formally renamed to:

\[
\boxed{\text{Curvature-Saturated Smooth Spiral}}.
\]

---

# 3. Quadratic Exponential Limit Family

As \(a\) and \(\varepsilon\) increase simultaneously, the original finite-width family approaches:

\[
\boxed{
r'(\theta)\propto e^{q(\theta-c)^2}
}.
\]

Candidate for this round:

\[
q=1.090073547848,
\qquad
c=0.953844856909.
\]

Terminal polar angle:

\[
\Theta=2.823761070596,
\]

Length normalization scale:

\[
b=0.057263454680.
\]

Curvature range:

\[
0.253909992
\leq
\kappa(s)
\leq
24.949981707.
\]

Minimum local radius of curvature:

\[
\frac1{\max\kappa}=0.040080189707,
\]

Local margin relative to \(\rho=0.04\):

\[
8.018970729117e-05.
\]

![Shape Comparison](../figures/01_old_vs_limit_shape.png)

![Curvature Profiles](../figures/02_curvature_profiles.png)

---

# 4. Dual-Chirality Tension

High-resolution results:

\[
E_+=0.084844199671,
\]

\[
E_-=0.084844204388.
\]

Therefore:

\[
\boxed{
E_{\mathrm{cong}}
=
0.084844199671
}.
\]

Chirality difference:

\[
|E_+-E_-|
=
4.716945736782e-09.
\]

Full congruence replay value of the finite-width candidate from Round 1:

\[
E_{\mathrm{cong}}^{(1)}
=
0.046073023163.
\]

Increase in this round:

\[
0.038771176508,
\]

Multiplier:

\[
1.841516.
\]

![Chirality Phase Landscape](../figures/03_chirality_phase_landscape.png)

---

# 5. Non-Smooth Equalization Structure

Along the active curvature boundary:

\[
\max\kappa=24.95
\]

Adjusting \(c\), the two chirality branches are equalized near the peak.

This is not an ordinary extremum of a single smooth branch, but an epigraph/Clarke-type equilibrium:

\[
E_+\approx E_-.
\]

Exceeds the next phase local minimum in the original direction by:

\[
0.000351148462.
\]

Exceeds the next phase local minimum in the mirrored direction by:

\[
0.000126740211.
\]

![Boundary Equalization](../figures/04_boundary_equalization.png)

---

# 6. Fixed-Phase Dual Ledger

The LP dual pressures in both controlling chiralities are concentrated in a pair of approximately opposite directions:

\[
\lambda_1\approx\lambda_2\approx\frac12,
\]

and satisfy:

\[
\sum_j\lambda_j=1,
\qquad
\sum_j\lambda_j u_{\theta_j}\approx0.
\]

Thus, the control mechanism is primarily:

\[
\boxed{
\text{Candidate Directional Width}
-
\text{Directional Width of the First Three Families' Container}
}.
\]

The hard case in this round is dominated by the width branch, rather than a general three-way contact.

---

# 7. Numerical Audit of Tubular Validity

The polyline approximation satisfies:

- LineString simple: `True`;
- buffer valid: `True`;
- Theoretical tubular area:
  \[
  0.085026542840;
  \]
- Buffer area:
  \[
  0.085026565415;
  \]
- Difference:
  \[
  -2.257445089193e-08.
  \]

For pairs of sample points separated by an arc length of at least \(0.1\), no non-local proximal points were found within a range of \(2\rho+5\times10^{-4}\).

This supports that the reach is controlled by the local radius of curvature, but it is still not an interval reach certificate.

![Tubular Audit](../figures/08_tube_audit.png)

---

# 8. Common Container Degenerates into Dual Skeleton

After re-optimization, the four-family common convex thickened container only requires:

\[
\boxed{
\text{Constant-Curvature Semicircle}
+
\text{Mirrored Quadratic Exponential Limit Curve}
}.
\]

Center convex hull area:

\[
0.184006658575.
\]

Center convex hull perimeter:

\[
2.014782029201.
\]

Thickened container area:

\[
\boxed{
A_2=0.269624487989
}.
\]

Support direction proportions:

\[
\begin{aligned}
\text{Constant-Curvature Semicircle}
&\approx32.8819%,\\
\text{Quadratic Exponential Curve}
&\approx67.1528%.
\end{aligned}
\]

![Dual-Skeleton Container](../figures/06_final_pair_container.png)

![Support Ownership](../figures/07_support_ownership.png)

---

# 9. The Other Two Families Become Redundant

Optimal full congruence tension of the Archimedean spiral against the dual-skeleton container:

\[
-0.006272925748<0.
\]

Optimal tension of the curvature-saturated smooth spiral:

\[
-0.004494710587<0.
\]

Therefore, both can be strictly placed inside the dual-skeleton center container and no longer provide active support.

---

# 10. Area Comparison

First three families' container from Round 1:

\[
A_3=0.244915072937.
\]

Four-family container from Round 1:

\[
A_4^{(1)}=0.256259897110.
\]

Dual-skeleton container from Round 2:

\[
A_2^{(2)}=0.269624487989.
\]

Increase relative to the first three families:

\[
0.024709415052
\quad
(10.0890%).
\]

Increase relative to the four-family container from Round 1:

\[
0.013364590879
\quad
(5.2152%).
\]

Ratio to the single full tubular area:

\[
3.171062.
\]

![Area Progression](../figures/05_container_area_progression.png)

---

# 11. Main Conclusions of This Round

First, the original finite-width parameters are not the natural endpoint; their stable limit is:

\[
r'(\theta)\propto e^{q(\theta-c)^2}.
\]

Second, the full congruence audit did not weaken the candidate, but instead led to:

\[
E_+\approx E_-.
\]

Third, the maximum curvature itself is not the hard-case ordering quantity; more importantly, it is the global redistribution of curvature along the entire centerline and the directional width.

Fourth, the common container no longer requires four active families, but degenerates into:

\[
\boxed{
\text{Global Constant-Curvature Skeleton}
+
\text{Wide-Area Curvature Redistribution Skeleton}
}.
\]

---

# 12. Honest Boundaries

This round does not prove:

1. The quadratic exponential family is the optimal family for the full bridging family;
2. The candidate parameters are the unique local extremum of the continuous problem;
3. \(\max\kappa=24.95\) can replace the full reach constraint;
4. The dual-skeleton convex container is the global minimum convex container;
5. Non-convex containers cannot be smaller;
6. There are no missed support events between discrete directions;
7. These results constitute a new Kakeya or Moser area bound.

---

# 13. Next Natural Milestone

Round 3 should:

1. Directly use reach instead of only using \(\max\kappa\) as the active constraint;
2. Establish interval curvature and interval reach certificates;
3. Establish KKT/Clarke boxes for the chirality equalization points;
4. Elevate the width-dominated formulation into an analytic branch formulation;
5. Search for a fifth family on the dual-skeleton container specifically targeting the switching directions;
6. Begin non-convex container reduction and measure the convexification cost.

---

# 14. Conclusion

Round 2 elevates the finite-width numerical candidate to a more stable limit geometry:

\[
\boxed{
r'(\theta)\propto e^{q(\theta-c)^2}
}.
\]

Under full congruence, it achieves:

\[
\boxed{
E_{\mathrm{cong}}
\approx
0.084844199671
}.
\]

The common convex thickened container is advanced to:

\[
\boxed{
A\approx0.269624487989
}.
\]

The most important theoretical signal of this round is:

\[
\boxed{
\text{The hard case of the bridging family is not determined by a single maximum curvature,}
\text{but jointly by the global curvature redistribution and the directional width.}
}
\]