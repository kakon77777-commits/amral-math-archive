# Round 8 Method

## Formal Attack

Directly use the saved Fourier-16 residual candidates from Round 7.

## Container Response

The initial configuration is the final configuration of the ten families from Round 7, plus the best exposed configuration of Fourier-16.

The optimization is divided into:

1. Low-resolution global coordinate descent on the main skeleton;
2. Minor adjustments for all eleven families;
3. High-resolution local refinement of the active skeleton;
4. High-resolution final refinement of all families.

The objective is the simply connected hole-filling area of the complete tubular union.

## Dual-Pool Audit

Two Fourier-18 pools each generate 24 candidates passing:

- Positive curvature;
- Radius of curvature;
- Radial non-degeneracy;
- Simple centerline.

First, perform a quick sorting using inherited placements, then conduct a medium-budget global congruence search on all candidates, and perform multi-seed high-resolution recomputation on the strongest ones.

## B-spline Reserve Pool

Using the values of the logarithmic curvature of Fourier-16 at the control points as a base, add smooth random perturbations to generate 20 natural cubic spline curvatures.

Perform global placement refinement on all candidates with a fast upper bound higher than \(10^{-3}\).

## Verification

- Tubular validity: Half-turn positive curvature normal injectivity theorem + curvature boxes;
- Curvature boxes: Outward-style floating-point boxes;
- Container: High-resolution buffer and union replay;
- Placement: Multiple differential-evolution seeds plus Powell refinement;
- Active families: Leave-one-out tubular exposed area.