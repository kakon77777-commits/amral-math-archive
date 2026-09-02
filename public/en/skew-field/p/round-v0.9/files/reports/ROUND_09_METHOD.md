# Round 9 Methods

## 1. Formal Attack

Directly use the Fourier-18 hybrid candidates saved from Round 8.

## 2. Container Response

The initial configuration is the final configuration of the eleven families from Round 8, plus the optimal exposed configuration of Fourier-18.

The container objective is the simply connected area of the union of all tubular neighborhoods.

The optimization sequence includes:

1. Global adjustment of the skeletons from Rounds 3, 4, 6, 7, 8, and 9;
2. Local coordinate descent for all twelve families;
3. High-resolution refinement of the main active skeletons;
4. Final high-resolution small-step refinement for all families.

## 3. Three Fourier-20 Pools

Constructed respectively from the coefficients of Rounds 7, 8, and 9:

- Dispersed parent system;
- Local parent system;
- Hybrid parent system.

After expanding to 20 modes, decaying random perturbations are added.

12 geometrically valid candidates are retained in each pool.

Initial screening uses a limited-budget global placement; the top four undergo higher-resolution dual-chirality congruence search and multi-seed recomputation.

## 4. Moving-Knot B-spline

Using the log-curvature from Round 9 as the parent, perturbations are added to 16 movable knots, and a natural cubic spline is used to generate \(g(s)\).

Then, using:

\[
\kappa(s)
=
\frac{\pi e^{g(s)}}{\int e^g}
\]

to generate the curve.

The top five among the 20 valid candidates are refined, and the strongest is recomputed using a multi-seed global congruence search.

## 5. Verification

- Curvature: Outward-style floating-point box;
- Normal strip: Half-turn positive curvature normal injectivity theorem;
- Tubular area: High-resolution buffer;
- Placement: Dual-chirality differential evolution plus Powell's method;
- Container: High-resolution union;
- Active families: Leave-one-out complete tubular exposure.