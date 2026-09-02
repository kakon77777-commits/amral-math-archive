# Round 12 Arb/Ball Arithmetic Handoff Interface

## Objects to Recompute

1. `data/exact_contact_boundaries.json`
2. `data/special_branch_interval_certificate.json`
3. `data/phase_derivative_box_certificate.json`
4. `data/stationary_root_boxes.json`
5. `data/boundary_neighborhood_audit.json`

## Passing Criteria

### Special Branch

$$
\inf(s_{120}-s_{270})>0.
$$

### Event Control

$$
\inf s_{270}-\sup s_0>0.
$$

### Derivative Subboxes

For each $X$ that does not contain a root box:

$$
0\notin s'(X).
$$

### Root Boxes

For each $X_r$:

$$
N(X_r)\subset\operatorname{int}X_r.
$$

### Boundary Boxes

Except for $270^\circ$, for each boundary neighborhood $B_k$ that could potentially form a local minimum:

$$
\inf s(B_k)>\sup s_{270}.
$$

## Claims Upon Success

We can only claim that the congruence scale of the fixed-decimal smooth candidate over the complete phase circle is strictly enclosed, and is higher than the fixed-decimal five-bar event control.

A new lower bound for the Moser area still cannot be directly deduced.