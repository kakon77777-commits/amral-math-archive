# Riemann Hypothesis AI Mathematical Engineering v1.3: Seventh-Order Soft Start at the Prime Boundary

- Date: 2026-07-23
- Positioning: Non-proof research draft, GAP relay engineering
- Original Research Concept: Neo.K
- Engineering Derivation and Implementation: Aletheia (GPT-5.6 Thinking)

## 1. From v1.2 to v1.3

v1.2 pushed the 15-dimensional lowest generalized spectral bottom to approximately $10^{-9}$, and discovered that the nearest arithmetic support boundary is

$$
\log3=d+4h.
$$

v1.3 no longer merely records "approaching the boundary," but analytically resolves the boundary itself.

## 2. Core of this Version

For the degree-$7$ B-spline correlation kernel, let

$$
\mu=d+4h-\log3.
$$

The lag-$1$ prime-$3$ element exactly satisfies

$$
\boxed{
p_3(\mu)
=-\frac{\log3}{\sqrt3}\frac{(\mu_+/h)^7}{7!}
}.
$$

Therefore, the prime layer at this boundary is a

$$
C^6\text{ but not }C^7
$$

seventh-order soft start, rather than a low-order corner.

## 3. Pre- and Post-Boundary Certificates

Take

$$
h=\frac{87}{400},\qquad N=15.
$$

Pre-boundary:

$$
d_-=\frac{117}{512},
$$

Post-boundary:

$$
d_+=\frac{117}{512}+\frac1{5000}.
$$

Both complete explicit formula matrices are proven by a purely rational verifier

$$
\boxed{
Q(c)>10^{-9}c^TGc
\qquad(c\ne0)
}.
$$

The newly emerged prime-$3$ lag-$1$ element after the boundary is only about

$$
-6.88\times10^{-28}.
$$

Thus, it is almost invisible to the current near-zero spectral bottom.

## 4. Interpretation Correction

Previously, it could be said that the lowest mode was pushed toward a prime boundary; now it must be supplemented:

> What the searcher found is the seam between the parameter geometry and the arithmetic support graph, but the local start order of the seam is determined by the test kernel. When using degree-$7$ autocorrelation, the initial entry effect of prime-$3$ is compressed by seventh-order smoothing.

Therefore, "approaching $\log3$" cannot be directly interpreted as prime-$3$ causing the near-zero eigenvalue.

## 5. New GAP

The next step is no longer to blindly chase smaller eigenvalues, but to compare the boundary sensitivities of different test kernels:

$$
\boxed{
\texttt{RH-W-11-KERNEL-SENSITIVITY-ORDER}
}.
$$

To compare:

- Boundary vanishing order;
- Prime layer emergence order;
- Archimedean tail bound cost;
- Gram condition number;
- Sensitivity to negative direction searches;
- Trade-off between smoothness and arithmetic visibility.

## 6. Scope Declaration

This version does not prove or disprove the RH. It only closes the local analytical GAP of the prime-$3$ boundary in the specified B-spline dictionary, and leaves replayable positive margin certificates for the two 15-dimensional spaces before and after the boundary.