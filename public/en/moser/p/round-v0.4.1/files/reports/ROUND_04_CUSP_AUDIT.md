# Round 4 Non-smooth Cusp Review

**Date:** July 26, 2026  
**Nature:** Numerical Audit / Failure-Correction Ledger

## 1. Reason for Review

The branch tracker of SLSQP uses bounded one-dimensional minimization, yielding four tracked branches:

$$
0.998903763498200,\quad
0.998903763495465,\quad
0.998903763495466,\quad
0.998903763495465.
$$

The gap between the tracked values is:

$$
2.734812376559e-12.
$$

However, after locating the full phase landscape using a grid up to $65536$ and refining around all local minima, the true global minimum is obtained:

$$
\boxed{
s_\ast=0.998903750476358
}.
$$

It is located at:

$$
\phi=4.712388980384675,
$$

which is close to the exact:

$$
\frac{3\pi}2.
$$

## 2. Discrepancy

The difference between the lowest value of the tracker and the full phase review is:

$$
1.301910645957e-08.
$$

This is not a resolution drift. From the $2048$ to $65536$ phase grids, the reviewed value remains stable within the display precision.

The reason is that the $270^\circ$ branch forms a non-smooth cusp at the active vertex switching point. The bounded smooth one-dimensional minimization stops at a position extremely close to the cusp, thereby slightly overestimating the branch value.

## 3. Revised Formulation

It cannot be claimed that the four true local minima are leveled to $10^{-12}$.

It can be claimed that:

1. The four epigraph constraints in the branch tracking model are leveled to:

$$
2.734812376559e-12;
$$

2. After the full non-smooth phase audit, the true heights of the four control branches fall within a narrow band of approximately $10^{-8}$;

3. The true global scale is:

$$
\boxed{
0.998903750476358
}.
$$

## 4. Methodological Implications

The next round must not solely use:

$$
\nabla_\eta m_r.
$$

For non-smooth cusps, one should instead use:

- Left and right directional derivatives;
- Clarke subdifferentials;
- Active vertex switching equations;
- Exact special phases;
- Piecewise contact event systems.

Therefore, the shift in Round 5 from black-box smooth optimization to contact event equations is a necessary correction rather than a mere choice.