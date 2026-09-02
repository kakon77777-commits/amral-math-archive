# Trust Boundary

## Certified

- Recomputed the fixed Green model with $90$-decimal directed rounding.
- Established universal interval boxes for $58$ named, mutually independent position variables.
- Verified the Neumann invertibility of the $60$-dimensional positive block at radius $89/50\,000\,000$.
- Verified two Sylvester lower bounds for the final $2\times2$ Schur matrix.
- Verified that an exact rational corner at a distance of $10^{-3}$ from the center remains strictly positive.

## Conditionally Certified Parts

All conclusions hold within the abstract even-clamped Green model inherited from v0.7. Tail scales, five-band coefficients, atomic weights, and core atoms are treated as fixed inputs from the parent witness. v1.0 verifies that the input hashes match the parent certificate, but does not reprove their zeta-facing origins.

## Uncertified

- `actual_zeta_occupancy_family = false`
- `zeta_facing_tail_theorem_certified = false`
- `explicit_formula_transfer_certified = false`
- `global_rh_certificate = false`

In particular, the $58$-dimensional position boxes are local quantifiers for the abstract operator family, not a statement that "all actual zeta zeros fall within these boxes."

## Correct Interpretation of Failure Radii

The failures at $1.8\times10^{-6}$, $10^{-4}$, and $10^{-3}$ are all verification failures of interval lower bounds or candidate inverses. They do not imply the existence of a position where the operator is non-positive. To obtain a point counterexample, one must fix a set of positions and prove that the minimum eigen-direction is non-positive using an independent, strict upper bound; this package contains no such result.

## The Role of Floating-Point Computations

NumPy is only used to generate candidate inverses and candidate solutions. These candidates are serialized into finite decimals, and are therefore treated as exact rational numbers during the verification phase. The final validity is determined solely by directed interval arithmetic.

The floating-point position study of the parent v0.9 is only used to:

- compare possible true scales;
- select a deterministic set of corner signs.

It does not enter into the universal proof of the maximal box.