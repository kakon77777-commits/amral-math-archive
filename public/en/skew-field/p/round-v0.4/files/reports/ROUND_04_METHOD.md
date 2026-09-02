# Round 4 Methods

## Curvature Function Space

\[
g_M(s)
=
\sum_{m=1}^M
\left[
a_m\cos(2\pi ms)
+
b_m\sin(2\pi ms)
\right],
\]

\[
\kappa_M(s)
=
\frac{
\pi e^{g_M(s)}
}{
\int_0^1e^{g_M(u)}du
}.
\]

Comparison:

\[
M=6,\;8,\;10.
\]

## Search Layers

The first layer uses a directional width proxy:

\[
w_\gamma(\theta)
=
h_\gamma(\theta)+h_\gamma(\theta+\pi).
\]

The second layer solves a translational linear program for a fixed rotational phase:

\[
h_\gamma(\theta-\phi)
+
t\cdot u_\theta
-
h_C(\theta)
\le z.
\]

The third layer simultaneously computes the original orientation and its mirror image:

\[
E_{\mathrm{cong}}
=
\min(E_+,E_-).
\]

## Convex Container

\[
\mu_2
\left(
\operatorname{conv}
\bigcup_i g_i\gamma_i
\oplus\rho B
\right).
\]

## Non-convex Container

\[
\mu_2
\left(
\bigcup_i
g_iT_\rho(\gamma_i)
\right).
\]

Elements are first added greedily, followed by coordinate descent family by family. The simply connected version uses the area after filling holes within the outer boundary of the union as the objective.

## Verification Layer

- Curvature: outward-style floating-point boxes;
- Direct normal band: Round 3 half-turn positive curvature normal injectivity theorem;
- Tubular area: high-resolution buffer;
- Adjoint gradient: central finite difference;
- Container: high-resolution convex hull/union replay.