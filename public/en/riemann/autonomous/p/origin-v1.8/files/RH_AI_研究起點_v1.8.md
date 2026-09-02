# RH AI Research Starting Point v1.8: Interval-Taylor Parameter Tube

**Date:** 2026-07-23  
**Research Node:** RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION  
**Batch 01 Progress:** 15/20

## New in This Version

Fixing

$$
h=\frac{1797}{10000},
$$

expands the 2D parameter tube of RH-W-14 from

$$
\rho_d=\rho_\sigma=4\times10^{-12}
$$

to

$$
\boxed{
\rho_d=\rho_\sigma=10^{-7}
}.
$$

For every point in the new rectangle, the purely rational verifier proves:

$$
\boxed{
10^{-8}<\lambda_{\min}(M(d,\sigma),G(d,\sigma))<5\times10^{-8}.
}
$$

The radius in each direction is expanded by a factor of $25{,}000$, and the area is expanded by a factor of $6.25\times10^8$.

## Method Upgrade

RH-W-14 converted all first-order variations into global absolute value perturbations. RH-W-15 changes this to:

$$
\boxed{
\text{Strict corner matrices}
+\text{Bilinear convex combination}
+\text{Second-order Taylor remainder}.
}
$$

First-order signs, Toeplitz/block structures, and cross-regularity cancellations are preserved by the corner matrices; only the curvature remainder is bounded by absolute values.

## Important Retrospective Correction

The Archimedean first-derivative bounds in RH-W-14 missed the $-2f(0)$ normalization tail that still exists outside the spline support. The exact tail is

$$
\int_R^\infty\frac{dx}{e^x-e^{-x}}
=\operatorname{artanh}(e^{-R}).
$$

After correction, the first-order bounds are updated from

$$
(175,215,253)
$$

to

$$
\boxed{(179,218,255)}.
$$

After re-executing the exact $LDL^T$, the original parameter tube conclusion of RH-W-14 still holds; the old derivation is replaced by the corrected version.

## W-15 Second-Order Bounds

The integer second-order upper bounds for correlation degrees $3,5,7$ are:

$$
\boxed{2494,3110,3697}.
$$

The full-matrix second-order combined row remainder for the new tube is

$$
1.0988000004025753\times10^{-9}.
$$

## Chamber

The entire new rectangle still maintains:

- active prime powers: $\{2,3,4\}$;
- $R_{\max}<\log5$;
- minimum sample-to-knot margin of approximately $0.0212523$;
- spline pieces and activation graph remain unchanged.

## Boundary of Claims

This version only proves a continuous finite-dimensional near-zero positive spectral band on a fixed ten-dimensional mixed B-spline dictionary. It does not prove or disprove the RH.

## Next Node

$$
\boxed{
\texttt{RH-W-16-THREE-PARAMETER-TUBE}
}
$$

The next round will introduce the scale $h$ to establish the first $(h,d,\sigma)$ three-dimensional parameter box, while simultaneously controlling knot movements, Gram scale variations, prime-power sample normalizations, and the Archimedean tail.