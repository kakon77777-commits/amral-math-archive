# RH-W-15: Interval–Taylor Parameter Tube Expansion

**Version:** v0.1  
**Date:** 2026-07-23  
**Positioning:** Finite-dimensional Weil quadratic form engineering; does not prove or disprove the Riemann Hypothesis.

## Abstract

At a fixed scale

$$
h=\frac{1797}{10000}
$$

RH-W-14 utilized a global first-order Lipschitz absolute value envelope to prove a two-dimensional near-zero positive spectral parameter tube with a radius of only

$$
\rho_d=\rho_\sigma=4\times10^{-12}.
$$

This iteration switches to a tensor-product linear interpolation of the four corner matrices, preserving the first-order signs and block structure of the parameter variations, and intervalizes only the second-order remainder.

Ultimately proving: for the entire rectangle

$$
\boxed{
\left|d-\frac{893}{5000}\right|\le10^{-7},
\qquad
|\sigma|\le10^{-7}
}
$$

we have

$$
\boxed{
10^{-8}<\lambda_{\min}(M(d,\sigma),G(d,\sigma))<5\times10^{-8}.
}
$$

The radius in each parameter direction is expanded by a factor of $25{,}000$, and the rectangle's area is expanded by a factor of

$$
(25{,}000)^2=625{,}000{,}000.
$$

---

## 1. Dictionary and True Parameters

The two basis channels use degree-$1$ and degree-$3$ centered cardinal B-splines, respectively:

$$
v_j^{(1)}(x)=h^{-1/2}\beta_1\!\left(\frac{x-t_j^{(1)}}h\right),
$$

$$
v_j^{(3)}(x)=h^{-1/2}\beta_3\!\left(\frac{x-t_j^{(3)}}h\right).
$$

with centers at

$$
t_j^{(1)}=(j-2)d-\frac\sigma2,
\qquad
t_j^{(3)}=(j-2)d+\frac\sigma2,
$$

Each channel is five-dimensional, making the total dimension ten.

$d$ controls the intra-channel spacing, and $\sigma$ controls the relative translation between the two channels; both genuinely alter the test subspace. The global channel scaling $\alpha$ remains merely a change-of-basis gauge and is not included in the parameter dimensions.

---

## 2. Four-Corner Linear Interpolation

Let

$$
\Theta=[d_0-\rho_d,d_0+\rho_d]
\times[-\rho_\sigma,\rho_\sigma].
$$

For any matrix element $F(d,\sigma)$, a tensor-product linear interpolation $B_F(d,\sigma)$ is constructed using the four corner values. At the matrix level, this interpolation is a convex combination of the four corner matrices.

If the modified matrices at the four corners are all positive definite, then any convex combination of them remains positive definite. Therefore, it is not necessary to convert all first-order variations into absolute value row radii; one only needs to control the second-order remainder between the true function and its bilinear interpolation.

For the center form

$$
c_{ij}^{ab}=(i-j)d+b_{ab}\sigma,
$$

where $b_{ab}=0$ for intra-channel and $|b_{ab}|=1$ for cross-channel. If

$$
\left|\frac{d^2}{dc^2}W_r(c)\right|\le L_r^{(2)},
$$

then

$$
|W_r-B_{W_r}|
\le
\frac{L_r^{(2)}}2
\left((i-j)^2\rho_d^2+b_{ab}^2\rho_\sigma^2\right).
$$

The same applies to the Gram elements, using

$$
\left|\frac{d^2}{dc^2}G_r(c)\right|
\le\frac4{h^2}.
$$

---

## 3. Modified Second-Order Global Bounds

Using the finite difference relations of cardinal B-splines:

$$
\|\beta_r''\|_\infty\le4,
\qquad
\|\beta_r'''\|_\infty\le8,
$$

and separately controlling the endpoint, constant, prime-power, and Archimedean parts.

This iteration specifically retains the Archimedean constant tail outside the spline support:

$$
\int_R^\infty\frac{dx}{e^x-e^{-x}}
=\operatorname{artanh}(e^{-R}).
$$

yielding the second-order upper bounds for correlation degrees $3,5,7$:

$$
L_3^{(2)}<2494,
\qquad
L_5^{(2)}<3110,
\qquad
L_7^{(2)}<3697.
$$

The certificate adopts the integer upper bounds

$$
\boxed{2494,3110,3697}.
$$

The maximum row bound for the complete second-order remainder is

$$
\boxed{
\epsilon_{\mathrm{Taylor}}
=1.0988000004025753\times10^{-9}.
}
$$

The maximum row bound for the Gram remainder is

$$
4.0257536752808504\times10^{-11}.
$$

---

## 4. Four-Corner Exact Positive Definiteness

The four corners are:

$$
(d_0\pm10^{-7},\ \pm10^{-7}).
$$

Each corner reassembles the complete ten-dimensional Weil interval matrix, including:

- Archimedean background;
- Constant term;
- Endpoint terms;
- Prime-powers $2,3,4$;
- Exact Gram matrix.

For each corner, we construct

$$
C_v-10^{-8}G_v-
(\epsilon_{v,\mathrm{point}}+\epsilon_{\mathrm{Taylor}})I.
$$

All ten pivots of the purely rational $LDL^T$ factorization are strictly positive. By the convexity of the positive definite cone, all bilinear convex combinations of the four corner modified matrices are positive definite, and from the second-order remainder bounds, it follows that within the entire rectangle

$$
M(d,\sigma)-10^{-8}G(d,\sigma)\succ0.
$$

Therefore,

$$
\lambda_{\min}>10^{-8}.
$$

---

## 5. Full Parameter Tube Upper Bound

Continuing to use the integer witness from RH-W-13:

$$
\begin{aligned}
c={}&(
68190193,
137154794,
187700175,
137154794,
68190193,\\
&-3577963013,
-7569824004,
-10000000000,
-7569824004,
-3577963013)^T.
\end{aligned}
$$

First, we take the convex hull of the Rayleigh numerators and denominators at the four corners, then add the quadratic envelope of the second-order remainder. This yields, within the entire tube:

$$
\frac{c^TM(d,\sigma)c}{c^TG(d,\sigma)c}
<4.02178\times10^{-8}
<5\times10^{-8}.
$$

Thus,

$$
\lambda_{\min}<5\times10^{-8}.
$$

---

## 6. Chamber Stability

The maximum correlation support radius of the entire new parameter tube still satisfies

$$
R_{\max}<\log5.
$$

Therefore, the global active von Mangoldt set remains

$$
\boxed{2,3,4}.
$$

The minimum strict distance from all $\pm\log n$ samples to the nearest spline knot is

$$
\boxed{
2.125231944005469\times10^{-2}.
}
$$

which is much larger than the scale of the parameter tube, hence there are no:

- Prime powers entering or exiting;
- Samples crossing knots;
- Changes in polynomial piece identities;
- Changes in the activation graph.

---

## 7. Methodological Significance

RH-W-14 used

$$
\text{first-order global absolute value bounds}.
$$

RH-W-15 switches to

$$
\boxed{
\text{strict four-corner matrices}
+\text{convexity}
+\text{second-order remainder}.
}
$$

First-order variations are no longer treated as adversarial perturbations; instead, the corner matrices themselves preserve their directions, signs, and block cancellations. Only the curvature that genuinely cannot be described by linear interpolation is converted into absolute value errors.

This explains why, under the same near-zero spectral band, the radius can be expanded by a factor of $25{,}000$ at once.

---

## 8. Statement of Boundaries

This iteration proves the finite-dimensional positivity and near-zero spectral bounds of a fixed ten-dimensional mixed dictionary within a continuous two-dimensional parameter rectangle:

$$
10^{-8}<\lambda_{\min}<5\times10^{-8}.
$$

It does not imply the full Weil criterion, does not prove RH, nor does it constitute a counterexample to RH.