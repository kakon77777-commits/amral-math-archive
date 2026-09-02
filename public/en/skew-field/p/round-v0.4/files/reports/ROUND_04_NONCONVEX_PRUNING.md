# Round 4 Non-Convex Container Reduction

## Finite Test Family

This round simultaneously incorporates seven thickened curves:

1. Constant curvature semicircle;
2. Round 3 dual-frequency logarithmic curvature curve;
3. Round 4 Fourier-10 curve;
4. Round 2 quadratic exponential curve;
5. Archimedean spiral;
6. Curvature-saturated smooth spiral;
7. Round 1 finite-width curvature layer.

## Convex Container

The common convex thickened container is supported by:

\[
\text{Round 3 dual-frequency curve}
+
\text{Round 4 Fourier-10 curve}
\]

acting as the two active skeletons.

Area:

\[
A_{\mathrm{convex}}
=
0.305379358034.
\]

## Non-Convex Union

The union of the rigid configurations of the seven tubular neighborhoods, re-rendered at high resolution, is:

\[
A_{\mathrm{raw}}
=
0.191049126345.
\]

This union is connected and valid, but contains an area of:

\[
0.000395085324
\]

in the form of a small hole.

The simply connected candidate after filling the hole is:

\[
A_{\mathrm{sc}}
=
0.191444211669.
\]

Reduction relative to the convex container:

\[
37.3094%.
\]

Ratio of the simply connected container area to the single tubular area:

\[
2.251582.
\]

## Leave-one-out

High-resolution auditing shows:

- The Archimedean spiral can be completely placed inside the simply connected container of the other six families;
- The quadratic exponential and curvature-saturated families have only minor exposure;
- The constant curvature, Round 3 curve, and Fourier-10 curve remain significantly indispensable;
- The Round 1 finite-width family still has a non-zero contribution in the non-convex container.

Therefore:

\[
\text{Convex support redundancy}
\not\Rightarrow
\text{Non-convex container redundancy}.
\]

## Honest Bounds

This is a candidate derived from a finite family, discrete curves, and finite-budget coordinate descent; it is not the global minimum non-convex container, nor is it a new bound for the Kakeya or Moser problems.