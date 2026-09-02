> **Status Correction:** This appendix initially only calculated orientation-preserving placements. The asymmetric candidates with a scale greater than 1 do not constitute counterexamples to Wetzel's paper, because that paper allows reflections. Please also read `ROUND_02_CHIRALITY_CORRECTION.md`.

# Round 2 Exact Three-Normal Recheck Appendix

## 1. Why More Angle Grids Are Not Needed

The Wetzel container is a right triangle:

$$
T=\left\{(x,y):x\ge0,\ y\ge0,\ \frac{x}{A}+\frac{y}{B}\le1\right\}.
$$

For a rotated polygonal chain with vertices $(x_i,y_i)$, when translations are allowed and it is accommodated in $sT$, the optimal translation places:

$$
\min_i x_i
$$

against the left boundary, and places:

$$
\min_i y_i
$$

against the bottom edge. Therefore, the exact minimum scale for a fixed phase is:

$$
\boxed{
s(\phi)
=
\max_i\left(
\frac{x_i(\phi)}A+\frac{y_i(\phi)}B
\right)
-
\frac{\min_i x_i(\phi)}A
-
\frac{\min_i y_i(\phi)}B.
}
$$

This is not a discrete angle approximation. The three half-space constraints of the triangle completely describe the container; on a line segment, the extrema of a linear function occur at the endpoints, so it is only necessary to check the vertices of the polygonal chain.

---

## 2. Exact Recheck Results

Equal-length U-shape:

$$
s_U=0.957829839129.
$$

The candidate found in Round 2 using $256$ orientations had an original estimate of:

$$
s_{\mathrm{grid}}=0.993310820970.
$$

After switching to the exact three-normal method:

$$
s_{\mathrm{grid,exact}}=1.000837369637.
$$

It can be seen that the hypotenuse normal approximation indeed caused an underestimation of the scale.

---

## 3. Exact Three-Link Re-optimization

This appendix directly searches using the exact scale formula:

$$
(l_1,l_2,l_3),
\qquad
(\alpha_1,0,-\alpha_3).
$$

yielding:

$$
s_{\mathrm{3link}}=1.007315039573.
$$

Parameters:

$$
(l_1,l_2,l_3)
=
(0.2862216771,0.3592562829,0.3545220400),
$$

$$
(\alpha_1,\alpha_3)
=
(80.43065491^\circ,80.63182909^\circ).
$$

Its distance from the certified scale of $1$ is still:

$$
1-s_{\mathrm{3link}}=-7.315039573150e-03.
$$

This is the most important new progress so far: an asymmetric polygonal chain with only three segments, under exact triangle accommodation calculations, has approached the full scale of the certified Wetzel triangle.

However, this result is still only:

- A numerical search within the three-link parameter family;
- A candidate optimized using floating-point arithmetic;
- Not proven to be the global extremum for three links;
- Not establishing a new Moser lower bound;
- Not challenging Wetzel's covering proof, because the result is still less than $1$.

---

## 4. Contact Structure

The exact critical placement is controlled by three factors:

1. One vertex contacting the left edge;
2. One vertex contacting the bottom edge;
3. One vertex contacting the hypotenuse.

The controlling vertex indices are:

```json
{
  "left_edge": 2,
  "bottom_edge": 1,
  "hypotenuse": 3
}
```

This is completely consistent with the three-pressure equilibrium of the dual ledger, but it now no longer relies on the support orientation grid.

---

## 5. Modifications for the Next Round

Round 3 will no longer process the triangle container using dense support angles, but will adopt a two-layer architecture:

- **Exact kernel dedicated to triangles:** Three-normal closed-form scale;
- **General convex container kernel:** Support skewness LP and dual contact ledger.

The contact ledger reverse generator will first rapidly study four- to eight-link chains on the exact triangle kernel, and then move valuable candidates back to the general support field framework.