# RH-W-14: Lipschitz Certificates and Conservatism Audits

**Version:** v0.1  
**Date:** 2026-07-23

---

## 1. Why Start with a Tiny Parameter Tube

The lowest generalized spectral value of RH-W-13 is only about

$$
4\times10^{-8}.
$$

To prove a continuous parameter region, one cannot merely sample at a few corner points, nor assume that the eigenvalues are monotonic within the box. We must simultaneously control:

- the continuous variation of the Weil matrix;
- the continuous variation of the Gram metric;
- the prime-power activation graph;
- the spline polynomial pieces;
- the Rayleigh upper bound for a fixed witness.

Therefore, this round first uses a global Lipschitz envelope to establish a parameter tube that is very small in size but mathematically truly continuous.

---

## 2. The Certificate is Not Corner Interpolation

The certificate does not use:

$$
\text{"All corners are positive"}\Rightarrow\text{Positive inside the box}
$$

this kind of inference, which does not hold in general.

What is actually used is:

$$
M(\theta)-\delta G(\theta)
=
C-\delta G_0+E(\theta),
$$

and proving for all $\theta\in\mathcal T$:

$$
\|E(\theta)\|_2
\le
\|E(\theta)\|_\infty
\le
\epsilon.
$$

Then, exact $LDL^T$ verification:

$$
C-\delta G_0-\epsilon I\succ0.
$$

Only then is the positivity within the entire parameter tube deduced.

---

## 3. Why $M$ and $G$ Must Vary Together

RH-W-13 already discovered: if $M$ uses quantized parameters while $G$ uses unquantized parameters, positive values might be falsely represented as negative.

From the very beginning, this round controls both using the same parameter box:

$$
M(d,\sigma)
\quad\text{and}\quad
G(d,\sigma).
$$

What is used in the lower bound is:

$$
\Delta M-\delta\Delta G,
$$

rather than controlling only $\Delta M$.

The upper bound witness similarly uses both simultaneously:

$$
q_{\max}
=
q_0+\Delta q,
$$

$$
g_{\min}
=
g_0-\Delta g.
$$

Only when

$$
q_{\max}<Ug_{\min}
$$

is the Rayleigh upper bound for the entire parameter tube accepted.

---

## 4. The Strict Bound and Actual Variation Differ Greatly

80-digit high-precision floating-point sampling yields:

| Sample | $\lambda_0$ |
|---|---:|
| Center | $3.995905931516698\times10^{-8}$ |
| Lower end of $d$ | $3.995905917800754\times10^{-8}$ |
| Upper end of $d$ | $3.995905930007202\times10^{-8}$ |
| Lower end of $\sigma$ | $3.995905936390289\times10^{-8}$ |
| Upper end of $\sigma$ | $3.995905925255308\times10^{-8}$ |
| A negative corner | $3.995905938391824\times10^{-8}$ |
| A positive corner | $3.995905926204950\times10^{-8}$ |

The difference between the maximum and minimum samples is only about:

$$
2.06\times10^{-16}.
$$

However, the full-matrix combined row bound used for the strict lower bound is:

$$
2.30\times10^{-8}.
$$

This is not a contradiction. The former is merely the actual spectral drift of a small number of high-precision samples; the latter is a global absolute value upper bound that holds simultaneously for all matrix elements, all parameter points, and all vector directions.

It reveals the next clear bottleneck:

$$
\boxed{
\text{The currently provable parameter tube width is primarily limited by conservative perturbation bounds,}
\text{ rather than by observed spectral instability.}
}
$$

---

## 5. Why Floating-Point Stationarity Cannot Be Directly Used as a Large-Tube Certificate

Even if high-precision samples show that the lowest spectrum is almost stationary, there may still exist:

- local curvature between samples;
- higher-order cross terms;
- Gram condition number amplification;
- derivative variations near the support or knot boundaries;
- extremely narrow anomalies missed by numerical solvers.

Therefore, this round only claims the rectangle covered by the exact Lipschitz envelope.

---

## 6. Trust Boundary for This Round

### Strict Certificate Path

- Python `int` and `Fraction`;
- rational series intervals for $\log$, $\pi$, and $\gamma$;
- rational square root intervals;
- `Decimal.exp` with documented outward expansion;
- B-spline global derivative inequalities;
- symmetric matrix column-sum perturbation bounds;
- purely rational $LDL^T$;
- fixed integer Rayleigh witness.

### Cross-Check Only

- mpmath 55-digit integration;
- SciPy generalized eigenvalues;
- seven center, boundary, and corner samples.

Floating-point sampling does not participate in the exact certificate.

---

## 7. Next Engineering Direction

The global bounds

$$
\|\beta_r'\|_\infty\le1,
\qquad
\|\beta_r''\|_\infty\le4
$$

are very robust, but do not utilize:

- which spline piece each element is actually located in;
- the signs of the derivatives;
- the Toeplitz/block structure between different elements;
- the direction of the lowest mode;
- the possible cancellation of first-order terms;
- the fact that second-order Taylor remainders are usually much smaller than global Lipschitz bounds.

Therefore, the next round should establish:

$$
\boxed{
\texttt{RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION}
}
$$

upgrading the element-wise global Lipschitz to:

$$
M(\theta)
=
M_0+
\sum_a \partial_aM_0\,\Delta\theta_a+
R_M(\theta),
$$

$$
G(\theta)
=
G_0+
\sum_a \partial_aG_0\,\Delta\theta_a+
R_G(\theta),
$$

preserving the signs and structure for the first-order matrices, and only using absolute value bounds for the second-order remainders.

The goal is not to continue pushing down the central spectral value, but to expand the proven parameter tube by several orders of magnitude.