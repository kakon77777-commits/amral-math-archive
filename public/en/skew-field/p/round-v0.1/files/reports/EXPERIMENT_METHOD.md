# Experimental Methods

## Fixed Parameters

\[
(L,\rho,\tau)=(1,0.04,\pi).
\]

\(\tau=\pi\) indicates that the normal needle covers all unoriented directions.

The area of the capless normal band for each valid centerline is:

\[
2\rho L=0.08.
\]

The area of the tubular neighborhood of the complete open curve is:

\[
2\rho L+\pi\rho^2.
\]

## Curve Families

### Constant Curvature Semicircle

\[
\gamma(s)
=
\left(
\frac{\sin(\pi s)}{\pi},
\frac{1-\cos(\pi s)}{\pi}
\right).
\]

### General Smooth Radially Modulated Spiral

Let

\[
f'(\theta)
=
\exp\left[
-a\exp\left(
-\left(\frac{\theta-c}{\varepsilon}\right)^2
\right)
\right],
\]

\[
f(\theta)
=
\int_0^\theta f'(u)\,du,
\]

\[
r(\theta)=bf(\theta).
\]

The endpoint \(\Theta\) is determined by the total tangential turning angle condition:

\[
\Theta+
\arctan\frac{f(\Theta)}{f'(\Theta)}
=
\pi.
\]

The scale \(b\) is determined by setting the curve length equal to one.

- \(a=0\): Archimedean spiral;
- Contact-saturated family: adjust \(a\) such that the maximum curvature equals \(1/\rho\);
- Finite-width curvature stratum: obtained by a max-min support tension search with a finite budget.

## Common Convex Container Surrogate

Choosing a rigid body configuration \(g_i\in SE(2)\) for each curve, we define the central convex hull:

\[
H
=
\operatorname{conv}
\left(
\bigcup_i g_i\gamma_i
\right).
\]

The thickened common container is:

\[
C_\rho
=
H\oplus \rho B.
\]

By Steiner's formula:

\[
\mu_2(C_\rho)
=
\mu_2(H)
+
\rho\operatorname{Per}(H)
+
\pi\rho^2.
\]

We use differential evolution combined with Powell's method for local correction to search for the rotation and translation of each curve.

## Leave-one-out Support Tension

For the central container \(H_{-i}\) excluding the target curve, we define:

\[
E_\infty(\gamma_i\mid H_{-i})
=
\inf_{\phi,t}
\max_\theta
\left[
h_{\gamma_i}(\theta-\phi)
+
t\cdot u_\theta
-
h_{H_{-i}}(\theta)
\right].
\]

Since both the target and the container are thickened by the same \(\rho\), the \(+\rho\) terms in the support functions cancel out.

Therefore:

- \(E_\infty\le0\): The thickened target curve can be placed inside the existing thickened container;
- \(E_\infty>0\): At least a corresponding isotropic support expansion is required.

## Honest Bounds

This is the first round of experiments under a finite curve family, convex container, discrete directions, and finite search budget. There is no global optimality certificate, nor is there a complete interval verification for the reach.