# Round 11 Methods

## Formal Attack

Directly use the Fourier-22 dispersed parent candidates saved from Round 10.

## Container Response

The initial 14-family configuration is:

- The final 13-family configuration from Round 10;
- The optimal exposed configuration of Fourier-22 against the Round 10 container.

The optimization is divided into three stages:

1. Wide-area curve-by-curve search with rotation ±0.55 and translation ±0.11;
2. Medium-scale search with rotation ±0.25 and translation ±0.055;
3. Local refinement with rotation ±0.10 and translation ±0.025.

Every historical test curve is retained.

## Placement Bounds

Establish local lower bounds for the optimal basin using the perimeter-type symmetric difference Lipschitz bound of tubular sets under rigid body perturbations.

The uniform partition lower bound of the complete configuration domain remains zero, so only local certificates are marked.

## Reserve Pool

Expand the three Fourier-22 parent families to 24 modes, and establish a moving-knot B-spline pool.

For each pool, first perform a global congruence search, then apply the following to the representative candidates:

- Original orientation and mirror image;
- Two differential-evolution seeds;
- Powell refinement;
- High-resolution full tubular exposure replay.

## Verification

- Curvature: Outward-style floating-point box;
- Normal band: Half-turn positive curvature normal injectivity theorem;
- Container: High-resolution tubular union;
- Final state activity: leave-one-out;
- Historical memory: All existing attack curves remain continuously in the test set.