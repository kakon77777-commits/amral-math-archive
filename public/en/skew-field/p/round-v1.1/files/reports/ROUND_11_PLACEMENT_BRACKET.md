# Round 11 Congruent Placement Upper and Lower Bounds Ledger

## 1. Feasible Upper Bound

The best configuration found by the multi-seed congruent search gives:

\[
\inf_{g\in E(2)}
\mu_2
\left[
(gT_\rho(\gamma_{11}))\setminus C_{10}
\right]
\le
U,
\]

where:

\[
U
=
0.001780655490.
\]

## 2. Rigid Body Motion Lipschitz Bound

If two rigid body configurations yield a maximum point displacement of the tubular set not exceeding \(\delta\), we conservatively use:

\[
|f(g)-f(h)|
\le
2P\delta+2\pi\delta^2,
\]

where the perimeter of the tubular boundary is:

\[
P
=
2.251320599486.
\]

To keep the local lower bound positive, it requires:

\[
\delta
<
3.952511050594e-04.
\]

## 3. Local Certificate of the Optimal Basin

Taking around the optimal configuration:

\[
|\Delta x|,|\Delta y|
\le5\times10^{-5},
\]

\[
|\Delta\phi|
\le10^{-4},
\]

the maximum point displacement does not exceed:

\[
1.192189760546e-04.
\]

Therefore, within this local cell:

\[
\boxed{
f(g)
\ge
0.001243765913.
}
\]

This proves that it is impossible to collapse to zero exposure near the optimal numerical basin.

## 4. Global Lower Bound Remains Zero

If the same perimeter-type Lipschitz bound is used to uniformly cover the entire configuration domain, it is estimated that at least:

\[
1,109,189,611,664
\]

three-dimensional configuration cells are required so that the motion radius of each cell is small enough to possibly yield a positive lower bound.

Thus, currently we can only record:

\[
\boxed{
0
\le
\inf_{g\in E(2)}f(g)
\le
0.001780655490.
}
\]

A local basin certificate cannot replace a global placement certificate.

## 5. Methodological Conclusions

Simply using the perimeter-type Hausdorff-Lipschitz bound suffers from a severe curse of dimensionality.

The next step requires stronger branching lower bounds, such as:

- Directional support exclusion;
- Container erosion distance boxes;
- Local area lower bounds for exposed connected components;
- Interval signed-distance in the configuration space.