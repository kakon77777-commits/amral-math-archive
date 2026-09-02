# Trust Boundary

## E0: Analytical Results within this Node

1. The clamped tail space is a Hilbert space, and compact-support Fourier evaluations are bounded functionals.
2. Weak duality between the positive trace-class primal and the probability-measure dual.
3. The rank-two closed form of the one-axis-point, one-core-point extremal.
4. The clamped bi-Laplacian Green kernel formula.
5. The finite-rank kernel projection of the two structural zeros.
6. The Woodbury–Schur PSD equivalence of the finite atomic witness.
7. The two core atoms make the final negative Schur rank exactly 2.

## E1: Automated Structure and Replay Checks

- Nested Galerkin dimension list and row counts.
- Each axis/core probability numerator sums exactly to $10^{12}$.
- Rational atom counts are 58 and 2.
- All cutting-plane final gradient gaps are 0.
- Rational target is $\alpha=21/20$.
- All global and interval flags remain false.

## E2: Floating Continuous-Kernel Evidence

- Chebyshev–Galerkin optimization.
- Gauss–Legendre Fourier quadrature.
- Direct Green ODE representers.
- Galerkin-to-Green atomic measure transfer.
- $60\times60$ positive solve and $2\times2$ Schur matrix.
- Time-step, quadrature-order, and dimension convergence.

## Significant Progress

v0.6 has eliminated the main ambiguity of being "blocked only in some finite dictionary". The fixed atomic measures are placed directly into the continuous clamped Green RKHS, and the resulting safe PSD margin is manifestly positive.

However, this is still a floating reconstruction. `continuous_kernel_floating_obstruction` cannot be written as `continuous_kernel_interval_certificate`.

## Not Yet Established

1. No directed-rounding enclosure of Green-kernel integrals.
2. No interval enclosure of the structural $2\times2$ projection.
3. No interval linear solve for the positive $60\times60$ system.
4. No interval eigenvalue proof for the final $2\times2$ Schur matrix.
5. The inherited tail multiplier has not yet been encapsulated into a theorem-backed lower interval.
6. The count coefficients have not yet been verified with complete endpoint hypotheses and directed rounding.
7. The analytic transfer between this $H_0^2$ continuous model and all explicit-formula admissibility hypotheses has not yet been proven.
8. No continuous obstruction family for the complete 288 refined patches.
9. No global leakage closure for the unknown off-axis regions.
10. No zero presence, winding, or local-to-global RH closure.

## Valid Interpretation

If v0.7 successfully proves that the rational witness satisfies $W_{21/20}\succeq0$ in the abstract continuous model, it will imply:

$$
\Lambda_{16}\ge\frac{21}{20}>1
$$

in the specified patch, five-band, coefficients, and clamped structural-zero domain.

This would rule out the primal branch of the continuous model, but it still does not equate to a proof or disproof of the RH; the zeta-facing coefficient theorems, other regions, and global quantifiers must still be closed independently.