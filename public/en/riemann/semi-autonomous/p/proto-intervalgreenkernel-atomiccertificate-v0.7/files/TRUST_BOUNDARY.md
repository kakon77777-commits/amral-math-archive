# Trust Boundary

## Proven

### E0: Analytic Structure

1. The exponential-plus-cubic formula for the clamped $D^4$ representer.
2. The finite recurrence of the exponential moments.
3. The finite-rank projection of the two structural constraints.
4. The Woodbury reduction of positive rank $60$ and negative rank $2$.
5. The Schur equivalence between $B^{-1}-Q$ and the original infinite-dimensional operator.
6. The Neumann residual enclosure theorem.

### E3-A: Directed Certificate of the Abstract Model

1. The directed enclosure of $\pi$, $\exp$, $\sin$, and $\cos$.
2. All unprojected Green pairings.
3. The structural Gram determinant and its inverse.
4. All projected pairings.
5. The regularity of the entire $60\times60$ interval system family.
6. The verified solution enclosure for the two right-hand sides.
7. The final $2\times2$ Sylvester strict positivity.

Therefore,

$$
W_{21/20}\succ0
$$

holds in the abstract model defined by fixed rational coefficients.

## Refuted Legacy Ambiguities

- The conclusion does not depend on the Chebyshev dictionary.
- The conclusion does not depend on time-grid quadrature.
- The conclusion does not depend on the signs of ordinary floating eigenvalues.
- The conclusion does not depend on an unverified $60\times60$ solve.

## Newly Identified Blockers

The existing band coefficients are upper-profile majorants. If the positive axis terms of the zeta-facing operator require lower counts, these coefficients cannot be used directly.

In particular:

$$
\operatorname{floor}_{12}(U)
$$

remains merely a number slightly below $U$, and does not thereby become a lower bound for the true count.

## Not Yet Proven

1. The correct inequality direction of the band coefficients in the derivation of the original explicit formula.
2. The validated lower zero counts of the five bands.
3. An interval certificate or consistent convention ensuring that band endpoints do not fall on zeros.
4. A theorem-backed lower enclosure for the rational tail scale.
5. The density and limit exchange from the clamped $H_0^2$ closure to the admissible class of the explicit formula.
6. The complete directed evaluation of the prime-side cone.
7. The continuous interval certificate family for other off-axis patches.
8. The global budget for unknown leakage regions.
9. The zeta zero presence or winding in the target patch.
10. The local-to-global RH closure.

## Valid Statements

One can say:

> The continuous atomic dual of the fixed rational model has a reproducible interval positivity certificate at $\alpha=21/20$.

One cannot say:

> This has excluded a certain actual zero region of zeta.

Even less can one say:

> The RH has been proven or disproven.

## Flags

- `abstract_continuous_interval_certificate = true`
- `zeta_facing_tail_theorem_certified = false`
- `zeta_facing_count_coefficients_certified = false`
- `explicit_formula_admissibility_certified = false`
- `global_rh_certificate = false`