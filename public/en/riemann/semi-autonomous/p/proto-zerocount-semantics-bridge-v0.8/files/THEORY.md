# Theory

## 1. Three Different Objects

Fix a band $A_j$, the multiset of zeros $\Gamma_j$ within it, and

$$
H_A(x)=\operatorname{Tr}(P_xA)\ge0.
$$

We must distinguish between:

### Actual Sum over Zeros

$$
Z_j(A;\Gamma_j)
=
\sum_{\gamma\in\Gamma_j}H_A(\gamma).
$$

### Supremum Upper Envelope

$$
E_j^{\sup}(A;U_j)
=
U_j\sup_{x\in A_j}H_A(x).
$$

### Infimum Lower Envelope

$$
E_j^{\inf}(A;L_j)
=
L_j\inf_{x\in A_j}H_A(x).
$$

These three cannot be interchanged simply because the coefficients are non-negative.

## 2. Counting Upper Bound Theorem

If

$$
n_j=|\Gamma_j|\le U_j,
$$

then

$$
\begin{aligned}
Z_j(A;\Gamma_j)
&=
\sum_{\gamma\in\Gamma_j}H_A(\gamma)\\
&\le
n_j\sup_{x\in A_j}H_A(x)\\
&\le
U_j\sup_{x\in A_j}H_A(x).
\end{aligned}
$$

This is the direction required for the zero-position-free leakage majorant in v0.2.

## 3. Counting Lower Bound Theorem

If

$$
n_j\ge L_j,
$$

then

$$
\begin{aligned}
Z_j(A;\Gamma_j)
&\ge
n_j\inf_{x\in A_j}H_A(x)\\
&\ge
L_j\inf_{x\in A_j}H_A(x).
\end{aligned}
$$

Note that the right-hand side is an infimum, not an arbitrary probability average.

## 4. Exact Counterexample for Arbitrary Measure Transfer

Suppose the band consists of only two points $x_0,x_1$, the actual multiset of zeros is

$$
\Gamma=\{x_0\},
$$

and take

$$
H(x_0)=0,\qquad H(x_1)=1.
$$

In this case,

$$
n=L=U=1,
$$

but for

$$
\mu=\delta_{x_1},
$$

we have

$$
Z(H;\Gamma)=0
<
1
=
L\int H\,d\mu.
$$

Therefore,

$$
n\ge L
$$

does not imply that

$$
Z(H;\Gamma)\ge L\int H\,d\mu
$$

holds for an arbitrary $\mu$.

## 5. Operator Version

In $\mathbb R^2$, take

$$
P_{x_0}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
P_{x_1}
=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$

If $Q\succeq0$ and

$$
Q\preceq P_{x_0},
\qquad
Q\preceq P_{x_1},
$$

then

$$
\operatorname{ran}Q
\subseteq
\operatorname{span}(e_1)
\cap
\operatorname{span}(e_2)
=
\{0\}.
$$

Thus $Q=0$. This shows that when we only know "there is at least one zero in the band", if the position can move arbitrarily, there generally does not exist a non-zero configuration-independent rank-one operator common lower bound.

In a continuous RKHS, the ranges of different $p_x\otimes p_x$ are generally not collinear either, so the same obstacle persists.

## 6. Upper-Envelope No-Go Theorem

Let

$$
\mathcal E_U(A)
=
\operatorname{Tr}(TA)
+
\sum_jU_js_j,
$$

where

$$
s_j\ge
\sup_{x\in A_j}\operatorname{Tr}(P_xA).
$$

If a dual witness proves that every target-feasible $A$ satisfies

$$
\mathcal E_U(A)\ge\alpha,
$$

then we can deduce:

> In this function space and with this upper envelope rule, the sufficient condition
> $\mathcal E_U(A)<\alpha$ has no feasible witness.

This is a method-level no-go theorem.

However, even if we additionally have

$$
Z_\Gamma(A)\le\mathcal E_U(A),
$$

it does not conversely imply

$$
Z_\Gamma(A)\ge\alpha.
$$

## 7. Correct Preservation Method for v0.7

v0.7 has interval-certified the fixed abstract operator

$$
W_{21/20}\succ0.
$$

This algebraic proposition remains unchanged.

Its zeta-facing interpretation is split into two paths:

1. If the upper count profiles and tail envelope complete the source theorem
   certification, it can be upgraded to an upper-envelope method no-go;
2. If it is to be upgraded to an actual zero-side positive obstruction, there must additionally be a
   location/occupancy operator family; scalar counts are insufficient.

## 8. Dual Directions of the Tail Coefficient

If the goal is to prove that a candidate succeeds, i.e.,

$$
\text{actual tail}\le E_{\mathrm{model}},
$$

the model coefficients must be theorem-backed upper coefficients.

If the goal is to prove a no-go, and it is known that the coefficients of the true conservative envelope $E_{\mathrm{true}}$ are no less than $E_{\mathrm{small}}$, then

$$
E_{\mathrm{small}}(A)\ge\alpha
$$

implies

$$
E_{\mathrm{true}}(A)\ge\alpha.
$$

Therefore, the downward rationalization of the tail scale in v0.7 might be suitable for the no-go direction, but directed certification of the source theorems is still required.