# Methods and Mathematical Boundaries

## 1. What the Prototype Does

For an off-axis rectangle \(K\), the program solves the following in a finite-dimensional real even compactly supported basis:

\[
\min_{c\in\ker E}
\sum_{w_j\in K}
\left|\sum_kc_kG_k(w_j)-i\right|^2
+\lambda\|c\|_2^2,
\]

where the endpoint functional is:

\[
E(c)=G_c(i/2).
\]

The real even property implies:

\[
G_c(-i/2)=G_c(i/2),
\]

so a single real linear condition simultaneously eliminates two Mellin endpoints.

## 2. Why the Block is Negative

Under the real even condition:

\[
G(\bar w)=\overline{G(w)}.
\]

Therefore, the off-axis conjugate block is:

\[
B(w)=2\operatorname{Re}(G(w)^2).
\]

If \(G(w)=u+iv\), then:

\[
B(w)=2(u^2-v^2).
\]

As long as over the entire rectangle:

\[
|v|>|u|,
\]

the block is negative. Approximating \(i\) is a convenient way to achieve this condition, but not the only way.

## 3. Continuous Region Estimation

The program uses:

\[
|G(w)|\le
\int|\psi(t)|e^{|\operatorname{Im}w||t|}\,dt=M_0
\]

and:

\[
|G'(w)|\le
\int|t\psi(t)|e^{|\operatorname{Im}w||t|}\,dt=M_1
\]

to obtain:

\[
\|\nabla B\|_2\le4\sqrt2M_0M_1.
\]

If the grid maximum is \(B_{\max}^{\rm grid}\) and the maximum distance to the nearest grid point is \(r\), then the candidate upper bound is:

\[
B_{\max}^{\rm cont}
\le
B_{\max}^{\rm grid}+4\sqrt2M_0M_1r.
\]

Currently, \(M_0,M_1\) are still obtained via floating-point quadrature, so this is not a rigorous interval certificate.

## 4. Not Yet Handled

This package does not compute:

- zeta zeros;
- winding numbers;
- Gamma distributions;
- prime position matrices;
- other zero leakages;
- the overall sign of the Weil quadratic form.

It only accomplishes:

\[
\text{off-axis rectangle}
\longrightarrow
\text{finite-dimensional Paley–Wiener candidate negative direction}.
\]