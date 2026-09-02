# RH AI Research Starting Point v1.6: Cross-Regularity Near-Zero Spectral Band

**Date:** 2026-07-23  
**Research Node:** RH-W-13-CROSS-REGULARITY-CONTINUATION

## New in this Version

RH-W-13 continues the degree-$1/3$ mixed B-spline Weil dictionary, completing four updates:

1. Proved that the full channel scaling $\alpha$ is merely an invertible congruence and does not change the generalized spectrum;
2. Used the relative translation $\sigma$ between the two channels as the true continuation parameter;
3. Discovered and eliminated false negative candidates caused by inconsistent quantization of $M/G$;
4. Used the exact derivative-jump tail formula to prove that the 10-dimensional mixed spectral bottom satisfies

$$
\boxed{10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}}.
$$

## Fixed Candidate

$$
h=\frac{1797}{10000},\qquad
 d=\frac{893}{5000},\qquad
 \sigma=0,
$$

Five basis functions per channel, for a total dimension of ten.

The maximum support radius is less than $\log5$, and the complete prime-power set is

$$
2,3,4.
$$

## Engineering Corrections

The generalized spectrum search must simultaneously generate $M$ and $G$ from the same canonical parameter object. This version retains a reproducible error case: quantizing only $M$ and not $G$ misrepresents approximately $+8.76\times10^{-8}$ as approximately $-3.32\times10^{-7}$.

## Certificate Status

- mixed lower bound: $\lambda_{\min}>10^{-8}$;
- rational witness upper bound: $\lambda_{\min}<5\times10^{-8}$;
- isolated $m=1$: $\lambda_{\min}>4\times10^{-4}$;
- isolated $m=3$: $\lambda_{\min}>10^{-7}$;
- exact verifier: Passed;
- 80-digit mpmath independent check: Passed;
- RH claim: False.

## Claim Boundaries

This version only proves strict positivity and near-zero spectral bounds on a fixed 10-dimensional subspace. It does not prove RH, nor does it provide an RH counterexample.

## Next Node

$$
\boxed{\texttt{RH-W-14-RIGOROUS-PARAMETER-TUBE}}
$$

The next round will not just prove a single parameter point, but will attempt to prove that within a rational parameter box

$$
(h,d,\sigma)\in\mathcal B
$$

the mixed gap remains positive and maintains a low spectrum, establishing the first rigorous "parameter tube / low spectral band" certificate.