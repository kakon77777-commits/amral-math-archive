# Curvature Function—Support Function Adjoint Sensitivity

## Curvature Normalization

Let:

\[
g_a(s)=\sum_j a_j\phi_j(s),
\]

\[
\kappa_a(s)
=
\frac{
\tau e^{g_a(s)}
}{
\int_0^1e^{g_a(u)}du
}.
\]

Then:

\[
\delta\kappa(s)
=
\kappa(s)
\left[
\delta g(s)
-
\frac1{\tau}
\int_0^1\kappa(u)\delta g(u)du
\right].
\]

For a single coefficient:

\[
\frac{\partial\kappa(s)}{\partial a_j}
=
\kappa(s)
\left[
\phi_j(s)-\bar\phi_j
\right],
\]

where:

\[
\bar\phi_j
=
\frac1{\tau}
\int_0^1\kappa(u)\phi_j(u)du.
\]

## Centerline Variation

\[
\theta(s)=\int_0^s\kappa(v)dv,
\qquad
\delta\theta(s)=\int_0^s\delta\kappa(v)dv.
\]

From:

\[
\gamma'(s)=T(s),
\qquad
\delta T(s)=N(s)\delta\theta(s),
\]

we obtain:

\[
\delta\gamma(s)
=
\int_0^sN(u)\delta\theta(u)du.
\]

## Support Function Variation

If the support point \(s_\ast\) in direction \(n\) is unique:

\[
h_\gamma(n)=\gamma(s_\ast)\cdot n,
\]

then:

\[
\delta h_\gamma(n)
=
n\cdot\delta\gamma(s_\ast).
\]

Therefore:

\[
\frac{\partial h_\gamma(n)}{\partial a_j}
=
\int_0^{s_\ast}
\left[
n\cdot
\int_v^{s_\ast}N(u)du
\right]
\kappa(v)
\left[
\phi_j(v)-\bar\phi_j
\right]dv.
\]

For the directional width:

\[
w_\gamma(n)=h_\gamma(n)+h_\gamma(-n)
\]

its gradient is the sum of the contributions from the two support points.

If the active support point, direction, or phase is not unique, the Clarke subgradient convex hull is used instead.

## Numerical Verification

For the Round 4 Fourier-10 candidate:

\[
\max_j
\left|
D_j^{\rm FD}-D_j^{\rm adj}
\right|
=
7.537290719695e-05,
\]

Relative \(L^2\) error:

\[
1.194240584988e-03.
\]

This result supports using the adjoint gradient to replace most of the black-box coefficient search in the next round, but it is not yet an interval gradient certificate.