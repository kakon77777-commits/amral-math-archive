工程紀錄 · 第五弧線 v3.12 · 2026-09-03 · UMP4_COUNTEREXAMPLE · CONSTRAINT_ADAPTED_CENTERING · DOUBLE_AXIS_REMOVAL · RH_CLAIM_FALSE

# Modulated Pairing Uniformity：UMP4 反例、Parallelogram Constraint-Adapted Centering 與 Double-Axis Remainder

**RH-ModulatedPairingUniformity v3.12**

本節點承接：

- `RH-Parallelogram-AddingFractionsRestriction v3.11`
- `RH-Parallelogram-SobolevTailTransfer v3.10`
- Montgomery–Soundararajan fourth-moment pairing method
- Kuperberg smooth weighted pairing theorem

v3.11 提出：

$$
\operatorname{UMP4}(\delta)
$$

作為 candidate：

> 將 smooth fourth-order pairing theorem 對 modulation sign pattern
> $$
> (+\lambda,-\lambda,-\lambda,+\lambda)
> $$
> uniformize，並保留：
> $$
> H^{2-\delta}
> $$
> pairing-free error。

v3.12 完成 proof-portability audit。

結果不是：

```text
UMP4 still open
```

而是：

$$
\boxed{
\operatorname{UMP4}(\delta)
\text{ is false for every }\delta>0.
}
$$

甚至 normalized finite-character averaging後，標準 three-pairing subtraction仍留下：

$$
\boxed{
\Theta(H^3)
}
$$

resonant remainder。

核心 exact counterexample只需要 finite conductor：

$$
\boxed{q=2}
$$

與：

$$
\boxed{\lambda=\frac12}.
$$

這個 failure 精確對應 Montgomery–Soundararajan proof 中原本被視為 lower-order 的：

$$
\boxed{
\text{three-or-more equal denominators}
}
$$

stratum。

在 unshifted setting，frequency：

$$
\frac12
$$

遠離 integer，smooth exponential sum有 cancellation。

modulation：

$$
\lambda=\frac12
$$

將它平移至：

$$
0,
$$

使同一 stratum resonance 到：

$$
H^4.
$$

因此 local shift-uniform two-point lemmas不能推出 global modulation-uniform pairing theorem。

---

更深一層，v3.12 發現：

$$
\boxed{
\text{global Wick centering}
\neq
\text{parallelogram constraint-adapted centering}.
}
$$

對：

$$
\mu_x=\mathfrak S(x)-1,
$$

full Wick-connected fourth cumulant可寫成：

$$
\boxed{
\mathfrak C_4(h,d)
=
\mathfrak S_0(0,h,d,h+d)
-
\mu_h^2
-
\mu_d^2
-
\mu_{h+d}\mu_{h-d}.
}
$$

但 v3.6 canonical covariance是：

$$
\boxed{
\mathfrak K_4(h,d)
=
\mathfrak S_0(0,h,d,h+d)
-
\mu_h^2.
}
$$

在 finite squarefree modulus $q$ 上，令：

$$
A(q)
=
\prod_{p\mid q}
\left(
1+\frac1{(p-1)^3}
\right).
$$

則：

$$
\boxed{
\mathbb E_{h,d}
\mathfrak S_{0,q}(0,h,d,h+d)
=
A(q)-1,
}
$$

$$
\boxed{
\mathbb E_h\mu_q(h)^2
=
A(q)-1,
}
$$

而：

$$
\boxed{
\mathbb E_{h,d}
\mu_q(h+d)\mu_q(h-d)
=
\mathbf1_{2\mid q}.
}
$$

所以：

$$
\boxed{
\mathbb E\mathfrak C_{4,q}
=
-
[A(q)-1]
-
\mathbf1_{2\mid q},
}
$$

通常不是零。

反而：

$$
\boxed{
\mathbb E\mathfrak K_{4,q}=0
}
$$

exactly。

所以在 parallelogram slice 上，第二與第三 pairing channels不是可獨立丟掉的 nuisance terms。

它們參與 constraint-induced cancellation。

---

v3.12 因此提出新的 exact decomposition。

v3.8 已知：

$$
\widehat{\mathfrak K}_{4,q}(\alpha,0)=0.
$$

又有：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(0,\beta)
=
\widehat{\mu_q^2}(\beta)
\qquad
\beta\ne0.
}
$$

Define：

$$
\boxed{
\mathfrak A_q(d)
=
\mu_q(d)^2
-
[A(q)-1].
}
$$

and：

$$
\boxed{
\mathfrak K_{4,q}^{\perp}(h,d)
=
\mathfrak K_{4,q}(h,d)
-
\mathfrak A_q(d).
}
$$

Then：

## Double-Axis Theorem

$$
\boxed{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,0)
=
0
\quad
\forall\alpha,
}
$$

and：

$$
\boxed{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(0,\beta)
=
0
\quad
\forall\beta.
}
$$

Moreover：

$$
\boxed{
\mathfrak K_{4,q}^{\perp}(h,d)
=
\mathfrak K_{4,q}^{\perp}(d,h).
}
$$

Thus the deterministic parallelogram model now splits into：

```text
one-dimensional centered pair-square axis
+
genuinely two-dimensional axis-free remainder.
```

This is the correct constraint-adapted replacement for UMP4。

No RH claim is made。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

UMP4(delta) = FALSE FOR EVERY delta > 0
AVERAGED_UMP4(delta) = FALSE FOR EVERY delta > 0

Q2_POINTWISE_RESONANCE = CLOSED
Q2_AVERAGED_RESONANCE = CLOSED

MODULATION_PORTABILITY_BLOCKER = HIGHER_DENOMINATOR_MULTIPLICITY_RESONANCE

LOCAL_SHIFT_UNIFORM_LEMMAS = TRUE_EXTERNALLY
GLOBAL_SHIFT_UNIFORM_PAIRING_THEOREM = FALSE

GLOBAL_WICK_CENTERING_IS_PARALLELOGRAM_CENTERING = FALSE

FINITE_Q_CONNECTED_CUMULANT_MEAN = CLOSED
FINITE_Q_K4_MEAN_ZERO = CLOSED_FROM_V3_7

DOUBLE_CENTERING_AXIS_DECOMPOSITION = CLOSED
K4_PERP_BETA_ZERO_AXIS = ZERO
K4_PERP_ALPHA_ZERO_AXIS = ZERO
K4_PERP_H_D_SYMMETRY = CLOSED

MIXED_TWO_DIRECTION_SOBOLEV_UNIFORMITY = OPEN
ONE_DIMENSIONAL_AXIS_TAIL = OPEN

FULL_DETERMINISTIC_ETA_M_POSITIVE = NOT_PROVED
ACTUAL_PRIME_DEVIATION = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Smooth exponential-sum notation

Let：

$$
f:\mathbb R\to\mathbb R
$$

be nonzero, smooth, compactly supported。

Define：

$$
\boxed{
E_{f,H}(\alpha)
=
\sum_{n\in\mathbb Z}
f(n/H)e(n\alpha).
}
$$

If：

$$
\int f\ne0,
$$

then：

$$
\boxed{
E_{f,H}(0)
=
H\int_{\mathbb R}f(x)dx
+
O_f(1).
}
$$

Thus：

$$
E_{f,H}(0)\asymp_f H.
$$

---

# 2. Finite conductor $q=2$

In the finite refined singular-series moment：

$$
V_4(q,H;f_1,\ldots,f_4),
$$

take：

$$
q=2.
$$

The only allowed divisor：

$$
q_i>1,\quad q_i\mid2
$$

is：

$$
q_i=2.
$$

The only reduced numerator is：

$$
a_i=1.
$$

Also：

$$
\frac12+\frac12+\frac12+\frac12=2\in\mathbb Z.
$$

Since：

$$
\frac{\mu(2)}{\phi(2)}=-1,
$$

the four coefficient product is：

$$
1.
$$

Therefore：

$$
\boxed{
V_4(2,H;f_1,\ldots,f_4)
=
\prod_{i=1}^4
E_{f_i,H}\left(\frac12\right).
}
$$

---

# 3. Modulation sign pattern

Introduce the v3.11 modulation：

$$
(\lambda_1,\lambda_2,\lambda_3,\lambda_4)
=
(\lambda,-\lambda,-\lambda,\lambda).
$$

Then：

$$
\boxed{
V_4^{(\lambda)}(2,H)
=
E_1\left(\frac12+\lambda\right)
E_2\left(\frac12-\lambda\right)
E_3\left(\frac12-\lambda\right)
E_4\left(\frac12+\lambda\right).
}
$$

Here：

$$
E_i=E_{f_i,H}.
$$

---

# 4. Every pair term at $q=2$

For any pair：

$$
(i,j),
$$

the finite：

$$
V_2^{(\lambda_i,\lambda_j)}(2,H)
$$

contains exactly the same denominator：

$$
2
$$

and residue：

$$
1.
$$

Hence the product over either member of any perfect matching gives：

$$
\boxed{
\prod_{i=1}^4
E_i\left(
\frac12+\lambda_i
\right).
}
$$

There are：

$$
\boxed{3}
$$

perfect matchings of four labeled slots。

Therefore the standard pairing sum is exactly：

$$
\boxed{
3
\prod_{i=1}^4
E_i\left(
\frac12+\lambda_i
\right).
}
$$

---

# 5. Exact $q=2$ pairing-free remainder

Define：

$$
\mathcal R_{4,2}^{(\lambda)}
=
V_4^{(\lambda)}
-
\sum_{\sigma\in B_4}
\prod_{(i,j)\in\sigma}
V_2^{(\lambda_i,\lambda_j)}(i,j).
$$

Sections 3–4 give：

## Theorem 5.1

$$
\boxed{
\mathcal R_{4,2}^{(\lambda)}
=
-2
E_1\left(\frac12+\lambda\right)
E_2\left(\frac12-\lambda\right)
E_3\left(\frac12-\lambda\right)
E_4\left(\frac12+\lambda\right).
}
$$

This is exact。

---

# 6. Resonant modulation $\lambda=1/2$

Take：

$$
\boxed{
\lambda=\frac12.
}
$$

Modulo one：

$$
\frac12+\lambda=0,
$$

and：

$$
\frac12-\lambda=0.
$$

Therefore：

## Theorem 6.1 · Resonant UMP Counterexample

$$
\boxed{
\mathcal R_{4,2}^{(1/2)}
=
-2
\prod_{i=1}^4
E_{f_i,H}(0).
}
$$

If：

$$
\int f_i\ne0,
$$

then：

$$
\boxed{
\mathcal R_{4,2}^{(1/2)}
=
-2H^4
\prod_{i=1}^4
\left(
\int f_i
\right)
+
O(H^3).
}
$$

Thus：

$$
\boxed{
|
\mathcal R_{4,2}^{(1/2)}
|
\asymp
H^4.
}
$$

---

# 7. UMP4 is false

Any：

$$
\operatorname{UMP4}(\delta)
$$

candidate with：

$$
\delta>0
$$

would demand：

$$
\sup_\lambda
|
\mathcal R_{4}^{(\lambda)}
|
\ll
H^{2-\delta+\varepsilon}.
$$

But Section 6 gives：

$$
H^4.
$$

Therefore：

## Corollary 7.1

$$
\boxed{
\operatorname{UMP4}(\delta)
\text{ is false for every }\delta>0.
}
$$

Indeed even：

$$
O(H^{4-\varepsilon})
$$

uniformity fails at this resonance。

---

# 8. Why this does not contradict the unshifted theorem

At：

$$
\lambda=0,
$$

the problematic factor is：

$$
E_{f,H}\left(\frac12\right).
$$

For smooth compactly supported $f$，Poisson summation gives rapid decay when the frequency remains a fixed positive distance from the integers。

So the all-equal-denominator configuration is small in the unshifted setting。

At：

$$
\lambda=\frac12,
$$

the same frequency is translated to：

$$
0,
$$

and：

$$
E_{f,H}(0)\asymp H.
$$

Therefore modulation changes the strength class of a denominator-multiplicity stratum。

---

# 9. Exact proof-audit blocker

The Montgomery–Soundararajan fourth-moment proof isolates as main terms denominator tuples：

$$
\boxed{
q_i\text{ equal in pairs with no further equalities}.
}
$$

Configurations in which：

$$
\boxed{
\text{three or more }q_i\text{ are equal}
}
$$

are placed inside the lower-order error。

The $q=2$ counterexample lies exactly in this excluded higher-multiplicity stratum。

Hence the proof-portability blocker is：

$$
\boxed{
\text{modulation can resonate a higher-multiplicity denominator collision}.
}
$$

---

# 10. Local shift-uniform estimates are not sufficient

Smooth two-point lemmas can be stated for arbitrary additive shifts。

However a shifted second-moment estimate itself contains resonant spikes。

For example, even modulus and shift near：

$$
\frac12
$$

can retain an：

$$
H^2
$$

main contribution。

Therefore：

$$
\boxed{
\text{local shift-uniform statement}
\not\Longrightarrow
\text{uniform global pairing decomposition}.
}
$$

v3.11's inference direction is rejected。

---

# 11. Averaged modulation does not repair UMP4

Now take：

$$
f_1=f_2=f_3=f_4=f
$$

real。

From Theorem 5.1 and：

$$
E_f(-x)=\overline{E_f(x)},
$$

we get：

$$
\boxed{
\mathcal R_{4,2}^{(\lambda)}
=
-2
\left|
E_{f,H}
\left(
\frac12+\lambda
\right)
\right|^4.
}
$$

Let：

$$
\lambda_j=\frac jM,
$$

and choose：

$$
M
$$

larger than the complete additive diameter of the lattice support of：

$$
f(n/H).
$$

Then finite character orthogonality gives：

## Theorem 11.1

$$
\boxed{
\frac1M
\sum_{j=0}^{M-1}
\left|
E_{f,H}
\left(
\frac12+\frac jM
\right)
\right|^4
=
\sum_{
n_1+n_2=n_3+n_4
}
c_{n_1}c_{n_2}c_{n_3}c_{n_4},
}
$$

where：

$$
c_n=f(n/H).
$$

Equivalently：

$$
\boxed{
=
\sum_s
\left|
(c*c)(s)
\right|^2.
}
$$

---

# 12. The averaged resonance is $H^3$

For nonzero compactly supported continuous：

$$
f,
$$

Riemann-sum scaling gives：

$$
\boxed{
\sum_s
|
(c*c)(s)
|^2
=
H^3
\int_{\mathbb R}
|
(f*f)(x)
|^2dx
+
o(H^3).
}
$$

The convolution is not identically zero when：

$$
f\ne0.
$$

Therefore：

## Theorem 12.1 · Averaged UMP Counterexample

$$
\boxed{
\frac1M
\sum_{j=0}^{M-1}
\mathcal R_{4,2}^{(j/M)}
=
-
2C_fH^3
+
o(H^3),
}
$$

where：

$$
\boxed{
C_f
=
\int
|(f*f)(x)|^2dx
>0.
}
$$

So normalized exact-character averaging still leaves：

$$
\boxed{
\Theta(H^3).
}
$$

---

# 13. Averaged UMP is false

A hoped-for averaged estimate：

$$
\frac1M
\sum_j
\mathcal R_4^{(j/M)}
=
O(
H^{2-\delta}
)
$$

cannot hold for any：

$$
\delta>0.
$$

Thus：

$$
\boxed{
\text{finite Fourier averaging does not rescue standard Wick subtraction}.
}
$$

The problem is structural centering, not loss from triangle inequality。

---

# 14. Parallelogram finite-$q$ means

Let：

$$
q
$$

be squarefree。

Define：

$$
\boxed{
A(q)
=
\prod_{p\mid q}
\left(
1+\frac1{(p-1)^3}
\right).
}
$$

v3.7 gives：

$$
\boxed{
\mathbb E_{h,d}
\mathfrak S_{0,q}(0,h,d,h+d)
=
A(q)-1.
}
$$

Also：

$$
\boxed{
\mathbb E_h\mu_q(h)^2
=
A(q)-1.
}
$$

---

# 15. The third pairing mean

Use the Fourier expansion：

$$
\boxed{
\mu_q(x)
=
\sum_{\theta\in G_q}
\rho_q(\theta)^2e(x\theta).
}
$$

Then：

$$
\begin{aligned}
&\mathbb E_{h,d}
\mu_q(h+d)
\mu_q(h-d)
\\
&=
\sum_{\theta,\varphi}
\rho_q(\theta)^2
\rho_q(\varphi)^2
\mathbf1_{\theta+\varphi=0}
\mathbf1_{\theta-\varphi=0}.
\end{aligned}
$$

Thus：

$$
2\theta=0.
$$

The zero frequency has：

$$
\rho_q(0)=0.
$$

A nonzero order-two frequency exists iff：

$$
2\mid q,
$$

namely：

$$
\theta=\frac12.
$$

Its reduced denominator is：

$$
2,
$$

so：

$$
\rho_q(1/2)^2=1.
$$

Hence：

## Theorem 15.1

$$
\boxed{
\mathbb E_{h,d}
\mu_q(h+d)
\mu_q(h-d)
=
\mathbf1_{2\mid q}.
}
$$

---

# 16. Global Wick-connected mean on the slice

Define：

$$
\boxed{
\begin{aligned}
\mathfrak C_{4,q}(h,d)
&=
\mathfrak S_{0,q}(0,h,d,h+d)
\\
&\quad
-
\mu_q(h)^2
-
\mu_q(d)^2
\\
&\quad
-
\mu_q(h+d)\mu_q(h-d).
\end{aligned}
}
$$

Sections 14–15 give：

## Theorem 16.1

$$
\boxed{
\mathbb E\mathfrak C_{4,q}
=
-
[A(q)-1]
-
\mathbf1_{2\mid q}.
}
$$

So the globally Wick-connected fourth cumulant is not centered on the parallelogram slice。

---

# 17. Why v3.7 $\mathfrak K_4$ stays centered

Recall：

$$
\boxed{
\mathfrak K_{4,q}
=
\mathfrak S_{0,q}
-
\mu_q(h)^2.
}
$$

Then：

$$
\boxed{
\mathfrak K_{4,q}
=
\mathfrak C_{4,q}
+
\mu_q(d)^2
+
\mu_q(h+d)\mu_q(h-d).
}
$$

The two retained pairing channels have mean：

$$
[A(q)-1]
+
\mathbf1_{2\mid q},
$$

which exactly cancels Theorem 16.1。

Therefore：

$$
\boxed{
\mathbb E\mathfrak K_{4,q}=0.
}
$$

This is the constraint-adapted cancellation identified in v3.7。

---

# 18. Constraint-adapted centering principle

A conditional slice can change which lower-order channels must remain grouped。

Therefore：

$$
\boxed{
\text{unconstrained cumulant decomposition}
}
$$

need not be compatible with：

$$
\boxed{
\text{conditional / constrained centering}.
}
$$

For the parallelogram：

$$
d_1+d_4=d_2+d_3,
$$

separating all three Wick channels destroys an exact deterministic cancellation。

This is the main conceptual correction of v3.12。

---

# 19. The surviving one-dimensional spectral axis

v3.8 proved：

$$
\widehat{\mathfrak K}_{4,q}(\alpha,0)=0.
$$

It also identified：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(0,\beta)
=
\widehat{\mu_q^2}(\beta)
}
$$

for：

$$
\beta\ne0.
$$

Therefore the complete：

$$
\alpha=0
$$

nonconstant axis is exactly the second pair-square channel。

---

# 20. Centered pair-square axis

Define：

$$
\boxed{
\mathfrak A_q(d)
=
\mu_q(d)^2
-
[A(q)-1].
}
$$

Then：

$$
\mathbb E_d\mathfrak A_q(d)=0.
$$

Its Fourier support is：

$$
\boxed{
\alpha=0,
\qquad
\beta\ne0.
}
$$

---

# 21. Double-centered parallelogram remainder

Define：

## Definition 21.1

$$
\boxed{
\mathfrak K_{4,q}^{\perp}(h,d)
=
\mathfrak K_{4,q}(h,d)
-
\mathfrak A_q(d).
}
$$

Equivalently：

$$
\boxed{
\begin{aligned}
\mathfrak K_{4,q}^{\perp}(h,d)
&=
\mathfrak S_{0,q}(0,h,d,h+d)
\\
&\quad
-
\mu_q(h)^2
-
\mu_q(d)^2
+
[A(q)-1].
\end{aligned}
}
$$

This expression is manifestly symmetric in：

$$
h,d.
$$

---

# 22. Double-axis removal theorem

The：

$$
\beta=0
$$

axis of：

$$
\mathfrak K_{4,q}
$$

is already zero。

The subtraction：

$$
\mathfrak A_q(d)
$$

has zero：

$$
\beta=0
$$

coefficient。

Therefore：

$$
\boxed{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,0)=0.
}
$$

For：

$$
\alpha=0,\quad\beta\ne0,
$$

Section 19 and the definition of：

$$
\mathfrak A_q
$$

give exact cancellation。

At：

$$
(0,0),
$$

both objects have mean zero。

Hence：

## Theorem 22.1 · Double-Axis Removal

$$
\boxed{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,0)=0
\quad
\forall\alpha,
}
$$

and：

$$
\boxed{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(0,\beta)=0
\quad
\forall\beta.
}
$$

---

# 23. Symmetry

From Definition 21.1：

## Corollary 23.1

$$
\boxed{
\mathfrak K_{4,q}^{\perp}(h,d)
=
\mathfrak K_{4,q}^{\perp}(d,h).
}
$$

So the genuinely two-dimensional remainder treats the two parallelogram gaps symmetrically。

---

# 24. New deterministic decomposition

The finite covariance is now：

$$
\boxed{
\mathfrak K_{4,q}(h,d)
=
\mathfrak A_q(d)
+
\mathfrak K_{4,q}^{\perp}(h,d).
}
$$

Interpretation：

### Axis component

$$
\boxed{
\mathfrak A_q(d)
}
$$

is a one-dimensional centered pair-square problem。

### Axis-free component

$$
\boxed{
\mathfrak K_{4,q}^{\perp}(h,d)
}
$$

has no one-dimensional Fourier axes。

This is more adapted to v3.10 restriction analysis than the full Wick cumulant。

---

# 25. Potential two-direction Sobolev quantity

Since：

$$
\alpha\ne0,
\qquad
\beta\ne0
$$

for every Fourier mode of：

$$
\mathfrak K_{4,q}^{\perp},
$$

define the mixed candidate：

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
=
\sum_{\alpha\ne0,\beta\ne0}
\frac{
|
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,\beta)
|^2
}{
|1-e(\alpha)|^2
|1-e(\beta)|^2
}.
}
$$

A uniform bound would provide a two-direction periodic antiderivative。

This is **not proved** in v3.12。

---

# 26. Why a mixed Sobolev theorem would matter

If：

$$
\Delta_h\Delta_d
\mathfrak G_q^{(2)}
=
\mathfrak K_{4,q}^{\perp},
$$

with uniformly bounded normalized：

$$
L^2
$$

energy, then two summations by parts would act on：

$$
\Omega_N.
$$

The mixed second finite difference of the piecewise-cubic Cesàro weight is smaller than the raw weight。

This may reduce the finite-box restriction burden before any high-conductor large-sieve step。

The axis term：

$$
\mathfrak A_q(d)
$$

would be handled separately with one-dimensional Ramanujan-tail methods。

---

# 27. Reference finite-conductor diagnostics

The package checks：

$$
q=2,3,6,15,30,210.
$$

For each：

- $\mathbb E\mathfrak K_{4,q}=0$；
- $\mathbb E\mathfrak C_{4,q}$ matches Theorem 16.1；
- $\mathbb E\mu(h+d)\mu(h-d)$ matches $\mathbf1_{2\mid q}$；
- both Fourier axes of $\mathfrak K_{4,q}^{\perp}$ vanish；
- $\mathfrak K_{4,q}^{\perp}$ is symmetric。

These are exact-structure normalization checks。

---

# 28. $q=2$ scaling diagnostics

Using a fixed smooth bump：

$$
f(x)
=
\begin{cases}
\exp[-1/(x(1-x))],&0<x<1,\\
0,&\text{otherwise},
\end{cases}
$$

the reference code evaluates：

$$
H=16,32,64,128,256.
$$

It records：

$$
\frac{
\mathcal R_{4,2}^{(1/2)}
}{
H^4
}
$$

and：

$$
\frac{
M^{-1}
\sum_j
\mathcal R_{4,2}^{(j/M)}
}{
H^3
}.
$$

Both rapidly stabilize to nonzero constants, as predicted by Sections 6 and 12。

Numerics are not used to prove those theorems。

---

# 29. New false-progress gates

Reject：

### F1 · Uniform UMP4

Exact $q=2$ counterexample。

### F2 · Average UMP4

Exact character-average $H^3$ counterexample。

### F3 · Local shift uniformity promoted globally

Higher denominator multiplicities can resonate。

### F4 · Full Wick centering before imposing the constraint

It destroys necessary constrained cancellation。

### F5 · Bounding three pair channels separately by absolute value

Their signed means cancel on the parallelogram slice。

### F6 · Treating $\mathfrak K_4^\perp$ mixed Sobolev numerics as theorem

Uniform mixed Sobolev remains open。

---

# 30. Revised autonomous candidate schema

Every pairing-based candidate should record：

```text
ambient unconstrained centering
constraint-adapted centering
resonant denominator multiplicities
modulation parameters
whether a rational residue can shift to zero
pair channels retained together
pointwise vs averaged modulation
spectral axes removed
remaining mixed-frequency object
```

A pairing theorem valid in the ambient problem cannot be transplanted to a constrained slice without this audit。

---

# 31. Suggested v3.13 direction

Recommended：

`RH-Parallelogram-ConstraintAdaptedPairing v3.13`

Do not try to repair UMP4。

Tasks：

1. formalize the exact decomposition：
   $$
   \mathfrak K_4
   =
   \mathfrak A(d)
   +
   \mathfrak K_4^\perp;
   $$
2. analyze the one-dimensional axis：
   $$
   \mathfrak A(d)
   =
   \mu(d)^2-\mathbb E\mu^2;
   $$
3. connect that axis to one-dimensional Ramanujan-tail theorems；
4. derive the finite-$q$ mixed coefficient formula for：
   $$
   \mathfrak K_4^\perp;
   $$
5. test whether：
   $$
   \sup_q
   \mathfrak H_{hd}^{\perp}(q)
   <\infty;
   $$
6. if uniform mixed Sobolev is true, use two-direction summation by parts；
7. then revisit the super-$\sqrt N$ restriction only for the axis-free spectrum；
8. preserve signed cancellation between constraint-induced pairing channels。

This is the new canonical deterministic continuation。

---

# 32. GAP ledger

## CLOSED / REDUCED

### G1. UMP4 portability

```text
FALSE
```

### G2. Average UMP4

```text
FALSE
```

### G3. Exact resonance mechanism

```text
CLOSED
```

### G4. Constrained connected mean

```text
CLOSED
```

### G5. Double-axis decomposition

```text
CLOSED
```

### G6. Axis-free symmetry

```text
CLOSED
```

---

## OPEN

### G7. One-dimensional centered pair-square tail

```text
OPEN
```

### G8. Uniform mixed Sobolev for $\mathfrak K_4^\perp$

```text
OPEN
```

### G9. Full deterministic：

$$
\eta_M>0
$$

```text
OPEN
```

### G10. Actual prime deviation

```text
OPEN
```

### G11. Complete quartic：

$$
\eta_Q>0
$$

```text
OPEN
```

### G12. RH

```text
OPEN
```

---

# 33. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

UMP4 FALSE = EXACT FINITE-CONDUCTOR COUNTEREXAMPLE
AVERAGED UMP FALSE = EXACT CHARACTER-ORTHOGONALITY ARGUMENT

LITERATURE PAIRING THEOREM REMAINS CORRECT IN ITS STATED SETTING

FAILURE IS IN THE PROPOSED MODULATED TRANSPLANT

CONSTRAINT-ADAPTED DOUBLE CENTERING = EXACT FINITE-Q ALGEBRA

NO MIXED SOBOLEV THEOREM PROVED
NO ETA_M > 0 PROVED
NO ETA_Q > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\text{UMP4 counterexample}
\Longrightarrow
\text{Kuperberg theorem false}.
$$

The published theorem is not being contradicted。

Forbidden：

$$
\text{connected fourth cumulant}
\Longrightarrow
\text{correct constrained residual}.
$$

Forbidden：

$$
\text{both axes removed}
\Longrightarrow
\text{automatic two-dimensional power saving}.
$$

---

# 34. One-line status

> v3.12 disproves the proposed UMP4 route by an exact finite-conductor resonance. At $q=2$, the only residue frequency is $1/2$. Under modulation $(+\lambda,-\lambda,-\lambda,+\lambda)$ with $\lambda=1/2$, all four exponential sums move to zero frequency. The fourth moment is therefore the product of four zero-frequency sums, while each of the three Wick pairings gives the same product; the pairing-free remainder is exactly minus twice that product and has size $\Theta(H^4)$. Even normalized finite-character averaging does not rescue the route: for equal real smooth weights the averaged remainder is minus twice the additive energy of the sampled weight sequence, hence $\Theta(H^3)$. This resonance occurs precisely in the higher-denominator-multiplicity stratum that is lower-order in the original unshifted Montgomery–Soundararajan proof. The deeper correction is centering: the fully Wick-connected fourth cumulant has nonzero mean on the parallelogram slice, whereas the AMRAL covariance $\mathfrak K_4=\mathfrak S_0-\mu_h^2$ remains mean-zero because the other two pairing channels cancel the constraint-induced connected mean. The correct next decomposition is constraint-adapted double centering: subtract the centered $\mu_d^2$ axis from $\mathfrak K_4$, leaving a symmetric remainder whose entire $\alpha=0$ and $\beta=0$ Fourier axes vanish. The deterministic branch should now analyze the one-dimensional axis and the genuinely two-dimensional axis-free remainder separately rather than attempt any global uniform Wick theorem.

---

# 35. References

1. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.  
   arXiv: https://arxiv.org/abs/math/0409258

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   DOI: https://doi.org/10.1142/S1793042125500046  
   arXiv: https://arxiv.org/abs/2301.06095

3. AMRAL, **RH-Parallelogram-AddingFractionsRestriction v3.11**.

4. AMRAL, **RH-Parallelogram-RamanujanTail v3.8**.

---

# 36. Provenance

研究主導：Neo.K

v3.12 exact $q=2$ modulation counterexample、character-averaged resonance、proof-portability blocker、constraint-adapted centering theorem、double-axis decomposition、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 modulated pairing counterexample / constraint-adapted centering 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
