# Clearance Fields, Morphological Erosion, and Area Exposure Tension

## 1. Inclusion Conditions for Thickened Curves

Let:

\[
T_\rho(\gamma)
=
\gamma\oplus B_\rho
\]

be the full tubular neighborhood of the centerline, and \(C\subset\mathbb R^2\) be a closed container.

Define the morphological erosion:

\[
C\ominus B_\rho
=
\left\{
x:
x+B_\rho\subseteq C
\right\}.
\]

Then:

\[
\boxed{
T_\rho(\gamma)\subseteq C
\iff
\gamma\subseteq C\ominus B_\rho.
}
\]

Equivalently, if:

\[
d_C(x)
=
\operatorname{dist}(x,C^c),
\qquad x\in C,
\]

then:

\[
T_\rho(\gamma)\subseteq C
\iff
\inf_{s}d_C(\gamma(s))\ge\rho.
\]

## 2. Why Not Directly Use Polygonal Negative Buffers

When directly computing:

\[
C.\operatorname{buffer}(-\rho)
\]

on discretized boundaries, circular arc approximations, concave corners, and narrow channels can cause additional shrinkage.

The seven known valid centerlines from Round 4 all have a pointwise minimum clearance in the original container of approximately:

\[
0.04,
\]

but the polygonal negative buffer incorrectly classifies several of these centerlines as exposed.

Therefore, the fast search in Round 5 adopts the clearance field:

\[
d_C(x)-\rho,
\]

while the final determination directly computes the exposed area of the full tubular neighborhood.

## 3. Area Exposure Tension

Define:

\[
\boxed{
\mathcal A_C(\gamma)
=
\inf_{g\in E(2)}
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
}
\]

When the minimum is attainable:

\[
\mathcal A_C(\gamma)=0
\iff
\exists g\in E(2):
gT_\rho(\gamma)\subseteq C.
\]

This differs from the convex support gap:

- The support gap only observes the convex hull directions;
- The area exposure tension directly observes non-convex grooves, channels, and local gaps;
- The same curve might be redundant in the sense of convex support, yet still contribute in the sense of non-convex exposure.

## 4. Fast Proxies and Final Recomputation

The search layer uses the clearance violation:

\[
v_C(x)
=
\max\{0,\rho-d_C(x)\},
\]

and sorts using a mixture of the maximum value and higher-order \(L^p\) norms.

The final candidates must recompute:

\[
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
\]

Data from Round 5 shows that the clearance proxy can find candidates, but cannot reliably sort all candidates; therefore, it can only serve as a search layer, not as a certificate layer.