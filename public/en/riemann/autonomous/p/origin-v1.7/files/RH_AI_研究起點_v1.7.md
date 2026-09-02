# RH AI Research Starting Point v1.7: Rigorous 2D Parameter Tube

**Date:** 2026-07-23  
**Research Node:** RH-W-14-RIGOROUS-PARAMETER-TUBE

## New in This Version

RH-W-14 expands the 10-dimensional near-zero single-point certificate of v1.6 into the first continuous 2D parameter tube.

Fixing:

$$
h=\frac{1797}{10000},
$$

within

$$
\left|d-\frac{893}{5000}\right|\le4\times10^{-12},
\qquad
|\sigma|\le4\times10^{-12}
$$

a purely rational verifier proves that:

$$
\boxed{
10^{-8}
<
\lambda_{\min}(M(d,\sigma),G(d,\sigma))
<
5\times10^{-8}
}
$$

holds for every point in the parameter rectangle.

## Main Methods

1. Eliminate $\alpha$-channel scaling that does not change the generalized spectrum;
2. Retain only $d$ and $\sigma$, which genuinely change the subspace;
3. Use cardinal B-spline global derivative bounds:

$$
0\le\beta_r\le1,
\qquad
\|\beta_r'\|_\infty\le1,
\qquad
\|\beta_r''\|_\infty\le4;
$$

4. Establish central Lipschitz bounds for the Weil elements:

$$
L_3\le175,
\qquad
L_5\le215,
\qquad
L_7\le253;
$$

5. Simultaneously control $M(d,\sigma)$ and $G(d,\sigma)$;
6. Use row-sum perturbation bounds and purely rational $LDL^T$ to prove the lower bound for the entire tube;
7. Use a fixed integer witness to prove the upper bound for the entire tube.

## Chamber Stability

Throughout the entire parameter tube:

- The maximum correlation support radius remains less than $\log5$;
- The global prime-power set remains $\{2,3,4\}$;
- The minimum sample-to-knot distance is greater than $0.02125$;
- The spline polynomial pieces and activation graph remain unchanged.

## Conservativeness Findings

High-precision samples show that the actual drift of the lowest spectrum within the tube is only about

$$
2\times10^{-16},
$$

but the global exact envelope must reserve a matrix perturbation of about

$$
2.3\times10^{-8}.
$$

Therefore, the current tube width is primarily limited by the conservativeness of the certificate, not by the observed spectral instability.

## Certificate Status

- Central RH-W-13 exact certificate: Passed;
- 2D parameter tube exact certificate: Passed;
- Gram matrix is positive definite throughout the tube: Passed;
- Prime-power chamber is fixed: Passed;
- High-precision floating-point sampling: Passed;
- RH claim: False.

## Scope of Claims

This version only proves a continuous near-zero positive spectral band on a fixed 10-dimensional mixed B-spline subspace. It does not prove the RH, nor does it provide a counterexample to the RH.

## Next Node

$$
\boxed{
\texttt{RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION}
}
$$

The next round will preserve the signs and block structures of the first-order matrix derivatives, and only use interval bounds for the second-order remainder terms, in order to expand the parameter tube and attempt to incorporate the $h$ direction to form the first 3D parameter box.