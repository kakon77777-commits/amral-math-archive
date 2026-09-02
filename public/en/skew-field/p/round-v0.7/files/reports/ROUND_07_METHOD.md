# Round 7 Method

## 1. Formal Attack

Directly use the Fourier-14 residual candidate saved from Round 6.

Its optimal congruent configuration was already found in Round 6 via a full tubular exposed area search.

## 2. Container Response

The initial ten-family configuration includes:

- The final nine-family configuration from Round 6;
- The optimal exposed configuration of the Fourier-14 attack curve.

The container objective is the simply connected area of the tubular union after hole-filling.

Coordinate descent is divided into:

1. Three rounds of wide-area adjustment for the six primary skeletons;
2. Two rounds of adjustment for the four secondary families and all skeletons;
3. Two rounds of small-range refinement for the primary skeletons.

Only the rotation and translation of one curve are varied at a time.

## 3. Spatial Exposure Ledger

For the centerline of the optimal configuration, compute:

\[
v_C(s)=[\rho-d_C(s)]_+.
\]

Record:

- Proportion of positive gap arc length;
- Number of continuous gap segments;
- Maximum clearance gap;
- Gap box entropy;
- Number of effective gap boxes.

Simultaneously, decompose the full tubular exposed set into connected components, and record the area of each component.

## 4. Fourier-16 Residual Search

Extend the Round 7 attack coefficients to 16 modes:

- Randomly generate candidates;
- Filter out curves with insufficient radius of curvature, radial regression, or non-simple curves;
- Screen using low-resolution full tubular exposed area;
- Perform high-resolution congruent recomputation with both chiralities for the top five;
- Re-verify the optimal configuration using multiple global seeds.

## 5. High-Resolution Replay

The final container and leave-one-out use:

\[
\texttt{quad\_segs}=192
\]

for the tubular buffer replay.

## 6. Honest Bounds

- Curvature boxes are still outward floating-point boxes, not formal interval arithmetic;
- Rigid body placement is still a finite-seed optimization;
- The non-convex container is still a coordinate descent candidate;
- Fourier-16 is not the complete curvature function space.