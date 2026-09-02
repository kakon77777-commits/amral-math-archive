# Trust Boundary

## Completed

1. exact two-point countermodel;
2. exact rank-one common-floor countermodel;
3. logical classification of upper-count, lower-count, and arbitrary-measure transfer;
4. v0.1–v0.7 lineage semantic audit;
5. 10-layer Galerkin convergence under the lower candidate profile;
6. direct Green fixed-measure transfer for three time steps;
7. sampled primal escape diagnostic;
8. recalculation verification of all JSONs and standard-library unit tests.

## E0 exact statements

The following propositions do not depend on floating-point values:

$$
n\le U
\Longrightarrow
\sum_{\gamma\in\Gamma}H(\gamma)
\le
U\sup H,
$$

$$
n\ge L
\Longrightarrow
\sum_{\gamma\in\Gamma}H(\gamma)
\ge
L\inf H.
$$

And:

$$
n\ge L
\not\Longrightarrow
\sum_{\gamma\in\Gamma}H(\gamma)
\ge
L\int H\,d\mu
$$

for any probability measure $\mu$.

## E2 floating objects

The following objects are merely floating diagnostics:

- Riemann–Siegel theta and five-band count profiles;
- SLSQP atomic measure optimization;
- Chebyshev–Gauss Galerkin convergence;
- trapezoid direct Green transfer;
- $101\times101$ core grid primal escape;
- sampled suprema with an axis step of $0.01$.

## Not yet completed

1. formal source encapsulation of inherited $|S(T)|$ versions and constants;
2. directed interval enclosure of theta, log, log-gamma, and $\pi$;
3. band endpoint zero conventions;
4. tail density theorem and tail scale direction certificate;
5. whole-patch continuous primal escape certificate;
6. actual zero-location occupancy certificate;
7. universal uncertain-location Green-Schur family;
8. explicit-formula admissibility and prime-side transfer;
9. global rational rectangular covering;
10. proof or disproof of the RH.

## Prototype restriction

The patch

$$
[20.395,20.42]\times[-0.10625,-0.1]
$$

serves only as a prototype. Platt–Trudgian have rigorously verified the RH up to

$$
3\cdot10^{12},
$$

therefore, this patch is not an unresolved actual off-axis target for $\zeta$.

## Claim flags

```text
exact_semantic_theorems = true
floating_lower_profile_diagnostic = true
abstract_v0_7_interval_certificate_retained = true
upper_envelope_method_nogo_fully_certified = false
actual_zero_side_operator_bridge = false
explicit_formula_transfer = false
global_rh_certificate = false
```