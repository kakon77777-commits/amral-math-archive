# Center-Generated Kakeya-Moser Bridging Family: Round 3

## ——Normal Injectivity Theorem, Curvature Bounding Boxes, Clarke Boundary Ledger, and the New Dual-Frequency Log-Curvature Skeleton

**Version:** v0.3  
**Date:** July 27, 2026  
**Status:** Analytic normal band theorem + semi-verified curvature box + finite family numerical container experiments

---

# 1. Core Progress

In this round, we fix

\[
(L,\rho,\tau)=(1,0.04,\pi).
\]

achieving progress on two levels:

1. For curves with positive curvature and total turning angle not exceeding \(\pi\), we prove that the local lower bound on the radius of curvature can be elevated to the global injectivity of the direct normal band;
2. In a larger space of curvature functions, we find a new skeleton that is stronger than the quadratic exponential curve from Round 2.

# 2. Normal Injectivity Theorem

If the radius of curvature \(R(v)\ge R_0\), the signed distance to the intersection of two normal lines satisfies

\[
t+u
=
\frac1{\sin((\beta-\alpha)/2)}
\int_\alpha^\beta
R(v)\cos\left(v-\frac{\alpha+\beta}{2}\right)dv
\ge2R_0.
\]

Therefore, the normal map is globally injective within \(|t|<R_0\).

# 3. Curvature Bounding Boxes

Round 2 quadratic exponential curve:

\[
\max\kappa\in[24.949352913573,24.950611058937],
\qquad
1/\max\kappa\ge0.040079178728>0.04.
\]

Round 3 curve:

\[
\max\kappa\in[24.932622547439,24.947380985154],
\qquad
1/\max\kappa\ge0.040084367998>0.04.
\]

These are outward-rounded floating-point boxes, not Arb/MPFI formal interval certificates.

# 4. Clarke Boundary Ledger

The slopes of the left and right projected secant lines of the active curvature boundary in Round 2 are respectively

\[
2.435456746830e-04>0,
\qquad
-2.390447639833e-05<0.
\]

Thus, the projected Clarke box contains zero:

\[
0\in[-3.333836787190e-05,2.435456746830e-04].
\]

This elevates chiral level sets from a visual phenomenon to a reproducible non-smooth stationary point ledger.

# 5. New Curvature Family

The new candidate is defined as

\[
\kappa(s)=\frac{\pi e^{g(s)}}{\int_0^1e^{g(u)}du},
\]

where

\[
g(s)=a_1\cos(2\pi s)+b_1\sin(2\pi s)+a_2\cos(4\pi s)+b_2\sin(4\pi s).
\]

The coefficients are

\[
(a_1,b_1,a_2,b_2)=(2.891051951482,1.235672921127,2.084611650924,-0.561084085900).
\]

Its full congruence tension against the Round 2 dual-skeleton container is

\[
\boxed{E_{\rm cong}=0.029353956446>0}.
\]

Therefore, the Round 2 dual-skeleton is not closed with respect to the larger curvature function space.

# 6. Round 3 Final Dual-Skeleton

After re-optimization, the Round 2 quadratic exponential curve loses all active support directions. The final container consists of

\[
\boxed{\text{Constant Curvature Semicircle}+\text{Mirrored Dual-Frequency Log-Curvature Curve}}
\]

Central convex hull area:

\[
0.191403634548,
\]

Perimeter:

\[
2.125827359528,
\]

Thickened container area:

\[
\boxed{A_3=0.281463277175}.
\]

The active support directions are approximately:

\[
\text{Constant Curvature}=22.1528%,
\qquad
\text{Dual-Frequency Curvature}=77.8819%.
\]

# 7. Total Redundancy of Old Families

Relative to the new dual-skeleton, the optimal full congruence tensions are

\[
E_{\rm qexp}=-0.001730651162,
\quad
E_{\rm Arch}=-0.005662251313,
\quad
E_{\rm sat}=-0.003456227783,
\quad
E_{\rm finite}=-0.010677110003.
\]

All are negative; therefore, the Round 2 quadratic exponential curve is also strictly contained by the new dual-skeleton.

# 8. Both Skeletons are Indispensable

Tension of the new curve against the standalone constant curvature container:

\[
0.155222295708>0.
\]

Tension of the constant curvature semicircle against the standalone new curve container:

\[
0.128284377678>0.
\]

Thus, the new result remains a complementary dual-skeleton, not dominated by a single curve.

# 9. Area Advancement

Round 2 area:

\[
0.269624487989.
\]

Round 3 area:

\[
0.281463277175.
\]

Increase:

\[
0.011838789186
\quad(4.3908%).
\]

The ratio to the full tubular area of a single body is

\[
3.310299.
\]

# 10. Honest Boundaries

This round does not prove:

1. The dual-frequency log-curvature family is the optimal family in the full function space;
2. The four Fourier coefficients constitute the unique local extremum;
3. The full end-cap tubular neighborhood possesses a formal reach certificate;
4. The curvature boxes utilize hardware-level directed rounding;
5. The common convex container is the global minimum;
6. Non-convex containers cannot be smaller;
7. These results constitute a new Kakeya or Moser area bound.

# 11. The Next Natural Milestone

Round 4 should transition from finite formula families to the true curvature function space:

1. Use B-splines or Fourier 6–10 modes;
2. Perform projected optimization directly under \(\int\kappa=\pi\) and \(0<\kappa<\rho^{-1}\);
3. Establish the adjoint gradients for active support directions;
4. Determine whether the optimal curvature forms a sparse spectrum, boundary layer, or bang-bang limit;
5. Simultaneously initiate non-convex container reduction;
6. Convert the end-cap reach into endpoint-interior interval branching.

# 12. Conclusion

This round advances the hard case of the bridging family from specific spiral formulas to

\[
\boxed{\text{an extremal problem in the curvature function space subject to geometric constraints}}.
\]

The area of the new common convex thickened container is

\[
\boxed{0.281463277175}.
\]