# Round 5 Method

## 1. Defending Container

Using the Round 4 seven-family simply connected non-convex container:

\[
A_4=0.191444211669.
\]

## 2. Curvature Families

Expanding the Round 4 Fourier-10 coefficients to 12 modes:

\[
g_{12}(s)
=
\sum_{m=1}^{12}
\left[
a_m\cos(2\pi ms)
+
b_m\sin(2\pi ms)
\right],
\]

\[
\kappa(s)
=
\frac{
\pi e^{g_{12}(s)}
}{
\int_0^1e^{g_{12}(u)}du
}.
\]

## 3. Search Stratification

### Clearance Field Filtering

Establish a clearance field from the interior points of the container to the boundary, using:

\[
v(x)=\max(0,\rho-d_C(x))
\]

for rapid placement and curve ranking.

### Tubular Exposure Recalculation

For high-scoring candidates, calculate using the full tubular neighborhood:

\[
\inf_{g\in E(2)}
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
\]

Search both original and mirrored orientations simultaneously.

## 4. Container Update

First directly add the attacking curves, then sequentially reconfigure:

- Constant curvature semicircles;
- Round 3 dual-frequency curves;
- Round 4 Fourier-10;
- Round 5 Fourier-12;
- Four secondary test families.

Each time targeting the area after simply connected hole-filling.

## 5. High-Resolution Replay

Finally, replay using a higher-resolution buffer:

- Original union area;
- Hole area;
- Simply connected hole-filled area;
- Leave-one-out exposed area.

## 6. Holdout Samples

Additionally generated 50 random 12-mode curves not involved in the container update, of which 30 passed the curvature and radial conditions.

Performing a full tubular recalculation on the top four, we still found an exposed area of approximately:

\[
0.00493418
\]

for a candidate.

Therefore, the Round 5 system has not yet converged.