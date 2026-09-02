# Trust Boundary

## Rigorously Verified

- Fraction-based interval arithmetic;
- Piecewise rational enclosure of the Dirichlet Green kernel;
- Count-only exact counterexample;
- Adaptive cover tree and all leaf Sylvester inequalities;
- Algebraic deduction of occupancy selection transfer;
- v0.7 parent hashes, classification, and probability normalization;
- Convex coercivity margin from parent positivity to $\alpha=1$;
- Global Poincaré perturbation budget for clamped Green;
- Exact micro-radius family of $58$ independent closed cells.

## Conditional Dependencies

The clamped $58$-cell conclusion takes v0.7's
`abstract_continuous_interval_certificate = true` as its parent theorem.
v0.9 locks the parent witness and certificate bytes, and recomputes the new deductions; the complete
directed-decimal Green replay is still handled by the v0.7 suite.

Therefore, the correct label for this conclusion is:

`conditional_abstract_operator_family_certificate = true`.

## Floating-Point Diagnostics Only

- Clamped trapezoid reconstruction;
- Threshold gradient;
- Adversarial corner selection;
- Coordinate-flip search;
- Observed transition bracket from $0.016$ to $0.017$.

These results do not have an interval enclosure, nor do they exhaust all corners or interiors.
The floating candidate for `threshold < 1` is not a formal operator counterexample.

## Not Yet Provided

- Cell-by-cell presence theorem for actual $\zeta$ zeros;
- Source hash for the argument principle or Turing certificate;
- Occupancy family for unresolved height intervals;
- Local interval trigonometric/exponential Green derivatives;
- Explicit-formula admissible test-function theorem;
- Prime-side nonnegative cone certificate;
- Local-to-global exhaustion;
- RH proof or disproof.

## Permanent False Flags

The following flags under this node must remain false:

- `zeta_facing_occupancy_certificate`;
- `actual_zero_occupancy_certificate`;
- `explicit_formula_global_transfer`;
- `global_rh_certificate`.

If any subsequent AI wishes to change these to true, it must add replayable dependencies; it must not merely change field names, remove
qualifiers, or rename a synthetic premise to a theorem.