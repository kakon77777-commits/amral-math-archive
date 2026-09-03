工程紀錄 · 第五弧線 v3.8 · 2026-09-03 · RAMANUJAN_AXIS_CANCELLATION · LIMIT_PERIODIC_SUBPOWER_CLOSURE · HIGH_CONDUCTOR_QUANTITATIVE_GAP · RH_CLAIM_FALSE

# Parallelogram Ramanujan Tail：整條 Spectral Axis 消失、Limit-Periodic Subpower Closure 與 High-Conductor Quantitative Gap

**RH-Parallelogram-RamanujanTail v3.8**

本節點承接：

- `RH-RefinedSingularSeries-Parallelogram v3.7`
- `RH-CenteredShift-FourierGap v3.6`
- Montgomery–Soundararajan refined singular-series rational-frequency expansion
- Bloom–Kuperberg adding-fractions framework
- limit-periodic harmonic analysis

v3.7 已證：

$$
\widehat{\mathfrak K}_{4,q}(0,0)=0
$$

for every finite squarefree modulus $q$。

v3.8 將這個結果大幅加強：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(\alpha,0)=0
\qquad
\forall\alpha\in\frac1q\mathbb Z/\mathbb Z.
}
$$

也就是整條：

$$
\boxed{\beta=0}
$$

spectral axis完全消失。

等價地，對每個 fixed：

$$
h\bmod q,
$$

都有：

$$
\boxed{
\sum_{d\bmod q}
\mathfrak K_{4,q}(h,d)=0.
}
$$

這不是 asymptotic。

這是 coefficient-level identity。

本輪第二個結果是 full deterministic singular-series model的 **subpower closure**：

$$
\boxed{
\mathfrak M_{4,N}=o(N^5).
}
$$

因此 high-conductor tail不能恢復一個非零 $cN^5$ deterministic main term。

但是：

$$
o(N^5)
$$

仍可能是：

$$
\frac{N^5}{\log N},
\qquad
N^{5-o(1)},
$$

所以 fixed：

$$
\eta_M>0
$$

仍未證明。

本輪第三個結果是 exact two-dimensional weight transform：

$$
\boxed{
\widehat\Omega_N(\alpha,\beta)
=
\sum_{2\le n<m<2N}
w_N(n)w_N(m)
e((m-n)\beta)
E_{n-1}(\alpha),
}
$$

其中：

$$
E_M(\alpha)
=
\sum_{j=1}^{M}e(j\alpha).
$$

由 Abel summation：

$$
\boxed{
|\widehat\Omega_N(\alpha,\beta)|
\ll
N^3
M_N(\alpha)
M_N(\beta),
}
$$

where：

$$
\boxed{
M_N(\theta)
=
\min
\left(
N,
\|\theta\|_{\mathbb R/\mathbb Z}^{-1}
\right).
}
$$

因為所有 deterministic covariance modes都具有：

$$
\beta\ne0,
$$

每個 surviving rational mode都必須在 $d$ 方向支付 oscillation。

所以 v3.8 後的 canonical deterministic GAP不再是：

```text
does the tail have nonzero mean?
```

而是：

```text
can the nonzero-beta rational spectrum be summed
with a fixed power of oscillatory gain?
```

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

PARALLELOGRAM_PHASE = h alpha + d beta
FINITE_Q_COEFFICIENT_FORMULA = CLOSED

BETA_ZERO_AXIS = ZERO EXACTLY
ROW_MEAN_IN_d = ZERO EXACTLY

ALPHA_ZERO_AXIS = SECOND_PAIRING_SPECTRUM
WEIGHT_FOURIER_FORMULA = CLOSED
WEIGHT_FOURIER_BOUND = CLOSED

FULL_K4_B2_LIMIT_PERIODIC = CLOSED_AS_STANDARD_EULER_PRODUCT_ARGUMENT
FULL_MODEL_MEAN_N5_CONSTANT = ZERO
FULL_MODEL = o(N^5)

FULL_MODEL_FIXED_ETA_POSITIVE = NOT_PROVED

FINITE_Q_d_SOBOLEV_NORM = DEFINED
FINITE_Q_REFERENCE_GROWTH = SLOW_NUMERIC_ONLY

HIGH_CONDUCTOR_NONZERO_BETA_TAIL = OPEN
ACTUAL_PRIME_DEVIATION = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Rational-frequency expansion

For a finite squarefree modulus $q$, define：

$$
G_q
=
\frac1q\mathbb Z/\mathbb Z.
$$

For：

$$
\theta=\frac{k}{q}\in G_q,
$$

write its reduced denominator：

$$
r(\theta)
=
\frac q{(k,q)}.
$$

Define：

$$
\boxed{
\rho_q(\theta)
=
\begin{cases}
\displaystyle
\frac{\mu(r(\theta))}{\phi(r(\theta))},
&
r(\theta)>1,
\\
0,
&
r(\theta)=1.
\end{cases}
}
$$

This is the finite-modulus coefficient appearing in the refined singular-series expansion with all individual denominators $>1$。

---

# 2. Montgomery–Soundararajan / Kuperberg expansion

The standard finite refined singular series has the form：

$$
\boxed{
\begin{aligned}
\mathfrak S_{0,q}(d_1,\ldots,d_k)
&=
\sum_{
\substack{
q_1,\ldots,q_k>1\\
q_i\mid q
}
}
\prod_{i=1}^k
\frac{\mu(q_i)}{\phi(q_i)}
\\
&\quad\times
\sum_{
\substack{
(a_i,q_i)=1\\
\sum_i a_i/q_i\in\mathbb Z
}
}
e\left(
\sum_i
\frac{d_i a_i}{q_i}
\right).
\end{aligned}
}
$$

For the parallelogram：

$$
(d_1,d_2,d_3,d_4)
=
(0,h,d,h+d),
$$

define：

$$
\theta_i
=
\frac{a_i}{q_i}.
$$

The constraint is：

$$
\theta_1+\theta_2+\theta_3+\theta_4=0.
$$

The phase becomes：

$$
\boxed{
h\alpha+d\beta,
}
$$

where：

$$
\boxed{
\alpha=\theta_2+\theta_4,
}
$$

$$
\boxed{
\beta=\theta_3+\theta_4.
}
$$

This is the canonical two-dimensional rational spectrum。

---

# 3. Four-point spectral coefficient

Fix：

$$
\alpha,\beta\in G_q.
$$

Set：

$$
t=\theta_4.
$$

Then：

$$
\theta_2=\alpha-t,
$$

$$
\theta_3=\beta-t,
$$

$$
\theta_1=t-\alpha-\beta.
$$

Therefore the finite four-point coefficient is：

## Theorem 3.1

$$
\boxed{
C_q(\alpha,\beta)
=
\sum_{t\in G_q}
\rho_q(t)
\rho_q(\alpha-t)
\rho_q(\beta-t)
\rho_q(t-\alpha-\beta).
}
$$

---

# 4. Pair spectral coefficient

For the pair：

$$
\{0,h\},
$$

the constraint gives：

$$
\theta_1=-\theta_2.
$$

Since：

$$
\rho_q(-\theta)=\rho_q(\theta),
$$

the centered pair singular series is：

$$
\boxed{
\mu_q(h)
=
\sum_{\theta\in G_q}
\rho_q(\theta)^2e(h\theta).
}
$$

Thus its square has spectral coefficient：

$$
\boxed{
P_q(\alpha)
=
\sum_{t\in G_q}
\rho_q(t)^2
\rho_q(\alpha-t)^2.
}
$$

and is independent of $d$。

---

# 5. Finite covariance spectrum

Define：

$$
\boxed{
\mathfrak K_{4,q}(h,d)
=
\mathfrak S_{0,q}(0,h,d,h+d)
-
\mu_q(h)^2.
}
$$

Then：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
=
C_q(\alpha,\beta)
-
\mathbf1_{\beta=0}
P_q(\alpha).
}
$$

The normalization is：

$$
\mathfrak K_{4,q}(h,d)
=
\sum_{\alpha,\beta\in G_q}
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
e(h\alpha+d\beta).
$$

---

# 6. Entire $\beta=0$ axis cancellation

Set：

$$
\beta=0.
$$

Then：

$$
\begin{aligned}
C_q(\alpha,0)
&=
\sum_t
\rho_q(t)
\rho_q(\alpha-t)
\rho_q(-t)
\rho_q(t-\alpha)
\\
&=
\sum_t
\rho_q(t)^2
\rho_q(\alpha-t)^2
\\
&=
P_q(\alpha).
\end{aligned}
$$

Therefore：

## Theorem 6.1 · Spectral Axis Cancellation

For every finite squarefree：

$$
q,
$$

and every：

$$
\alpha\in G_q,
$$

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(\alpha,0)=0.
}
$$

This strictly strengthens the v3.7 zero-mode theorem。

---

# 7. Rowwise mean-zero theorem

By Fourier orthogonality：

## Corollary 7.1

For every：

$$
h\bmod q,
$$

$$
\boxed{
\frac1q
\sum_{d\bmod q}
\mathfrak K_{4,q}(h,d)=0.
}
$$

So pair centering removes every component that is constant in the second parallelogram gap $d$。

---

# 8. The surviving $\alpha=0$ axis

Now set：

$$
\alpha=0,
$$

and：

$$
\beta\ne0.
$$

Then：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(0,\beta)
=
\sum_t
\rho_q(t)^2
\rho_q(\beta-t)^2.
}
$$

This is the spectral form of the second Wick-like pair channel：

$$
(0,d)(h,h+d).
$$

Thus v3.8 does **not** say that all pairing structure disappears。

It says specifically：

```text
h-pair square
    is removed completely

d-pair channel
    survives as beta != 0 spectrum
```

---

# 9. Endpoint-Cesàro parallelogram weight

Recall：

$$
\boxed{
\Omega_N(h,d)
=
\sum_{
r=1
}^{2N-1-h-d}
w_N(r+h)
w_N(r+h+d),
}
$$

with support：

$$
h,d\ge1,
\qquad
h+d\le2N-2.
$$

---

# 10. Exact two-dimensional Fourier transform

Define：

$$
\boxed{
\widehat\Omega_N(\alpha,\beta)
=
\sum_{h,d}
\Omega_N(h,d)
e(h\alpha+d\beta).
}
$$

Set：

$$
n=r+h,
$$

$$
m=n+d.
$$

Then：

$$
1\le h<n<m<2N.
$$

Therefore：

## Theorem 10.1

$$
\boxed{
\widehat\Omega_N(\alpha,\beta)
=
\sum_{
2\le n<m<2N
}
w_N(n)w_N(m)
e((m-n)\beta)
E_{n-1}(\alpha),
}
$$

where：

$$
\boxed{
E_M(\alpha)
=
\sum_{j=1}^{M}e(j\alpha).
}
$$

---

# 11. Geometric-sum bound

For：

$$
\|\alpha\|
=
\operatorname{dist}(
\alpha,\mathbb Z
),
$$

$$
\boxed{
|E_M(\alpha)|
\ll
\min(
M,\|\alpha\|^{-1}
).
}
$$

Define：

$$
\boxed{
M_N(\alpha)
=
\min(
N,\|\alpha\|^{-1}
).
}
$$

Then：

$$
|E_{n-1}(\alpha)|
\ll
M_N(\alpha).
$$

---

# 12. Suffix triangular Fourier bound

For any fixed：

$$
n,
$$

Abel summation and：

$$
|w_N(m+1)-w_N(m)|
\le1
$$

give：

$$
\boxed{
\left|
\sum_{m>n}
w_N(m)e(m\beta)
\right|
\ll
N
M_N(\beta).
}
$$

This includes the trivial：

$$
N^2
$$

bound when：

$$
\|\beta\|\lesssim N^{-1}.
$$

---

# 13. Weight spectral bound

Use Theorem 10.1 and sum first over $m$。

Since：

$$
\sum_nw_N(n)\ll N^2,
$$

Sections 11–12 give：

## Theorem 13.1 · Parallelogram Weight Multiplier

$$
\boxed{
|\widehat\Omega_N(\alpha,\beta)|
\ll
N^3
M_N(\alpha)
M_N(\beta).
}
$$

In particular：

$$
\boxed{
|\widehat\Omega_N(\alpha,\beta)|
\ll
N^4
M_N(\beta).
}
$$

---

# 14. Why the spectral-axis theorem matters

Without centering, a：

$$
\beta=0
$$

mode receives no $d$-oscillation and can see：

$$
|\widehat\Omega_N|
\asymp N^5.
$$

Theorem 6.1 removes every such mode。

Every surviving deterministic covariance frequency therefore has：

$$
\beta\ne0.
$$

So high-conductor analysis always has at least one genuine rational oscillation direction available。

This is stronger than merely knowing the total mean is zero。

---

# 15. Finite-modulus spectral formula

For a finite squarefree：

$$
q,
$$

$$
\boxed{
\mathfrak M_{4,N}^{(q)}
=
\sum_{
\substack{
\alpha,\beta\in G_q\\
\beta\ne0
}
}
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
\widehat\Omega_N(-\alpha,-\beta),
}
$$

up to the already-lower-order collision lines removed in v3.6。

Hence：

$$
\boxed{
|\mathfrak M_{4,N}^{(q)}|
\ll
N^3
\sum_{
\beta\ne0
}
|
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
|
M_N(\alpha)
M_N(\beta).
}
$$

This is the exact spectral high-conductor interface。

---

# 16. Finite-$q$ $d$-Sobolev diagnostic

Because：

$$
\beta=0
$$

is absent, define：

$$
\boxed{
\mathfrak H_d(q)
=
\sum_{
\alpha,\beta\in G_q
\atop
\beta\ne0
}
\frac{
|
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
|^2
}{
|1-e(\beta)|^2
}.
}
$$

This is the mean-square norm of the periodic $d$-antiderivative。

If：

$$
\mathfrak G_q(h,d+1)-\mathfrak G_q(h,d)
=
\mathfrak K_{4,q}(h,d),
$$

with zero $d$-mean normalization, then Parseval gives：

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
|\mathfrak G_q(h,d)|^2
=
\mathfrak H_d(q).
}
$$

Reference values for primorial-like conductors grow slowly, but no uniform theorem is claimed here。

---

# 17. Finite-modulus coefficient factorization

Let：

$$
B_\beta(t)
=
\rho_q(t)\rho_q(t+\beta).
$$

Then for：

$$
\beta\ne0,
$$

Theorem 3.1 can be rewritten：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(\cdot,\beta)
=
B_{-\beta}
\ast
B_{\beta}.
}
$$

The convolution is on：

$$
G_q.
$$

This gives a concrete entry point for：

- Young inequalities；
- adding-fractions estimates；
- conductor decompositions；
- Sobolev bounds。

---

# 18. Basic coefficient norms

One has：

$$
\boxed{
\|\rho_q\|_2^2
=
\sum_{
r\mid q,\ r>1
}
\frac1{\phi(r)}
=
\frac q{\phi(q)}-1.
}
$$

Also：

$$
\boxed{
\|\rho_q\|_4^4
=
\sum_{
r\mid q,\ r>1
}
\frac1{\phi(r)^3}
\le
\prod_p
\left(
1+\frac1{(p-1)^3}
\right)
-1
<\infty.
}
$$

The $L^4$ norm is uniformly bounded in $q$。

This is consistent with bounded fourth-order local moments。

---

# 19. Limit-periodic structure of the full model

Each raw singular-series factor for a fixed subset of：

$$
\{0,h,d,h+d\}
$$

is an Euler product of periodic local functions。

For a local factor with $k\le4$ forms：

- outside collision lines：
  $$
  L_p=1+O_k(p^{-2});
  $$
- collision residues occupy only：
  $$
  O_k(p)
  $$
  of the：
  $$
  p^2
  $$
  pairs；
- on collisions：
  $$
  L_p=1+O_k(p^{-1}).
  $$

Therefore：

$$
\boxed{
\mathbb E_{h,d\bmod p}
|L_p-1|^2
=
O_k(p^{-3}).
}
$$

Since：

$$
\sum_p p^{-3}<\infty,
$$

finite-prime Euler products converge in Besicovitch：

$$
B^2(\mathbb Z^2).
$$

---

# 20. Pair-square term

The pair singular series as a function of $h$ has finite moments of every fixed order；in particular finite-prime approximants are bounded in $B^4$。

Therefore：

$$
\mu(h)^2
$$

exists in $B^2$。

Thus：

## Theorem 20.1

The full deterministic covariance：

$$
\boxed{
\mathfrak K_4(h,d)
=
\mathfrak S_0(0,h,d,h+d)
-
[\mathfrak S(h)-1]^2
}
$$

is a two-dimensional $B^2$ limit-periodic function。

---

# 21. Full zero mean

Finite-prime approximants：

$$
\mathfrak K_{4,q_y}
$$

satisfy the stronger rowwise zero-mean theorem。

Passing to the $B^2$ limit gives no：

$$
\beta=0
$$

Besicovitch Fourier component。

In particular：

$$
\boxed{
\mathcal M(
\mathfrak K_4
)=0,
}
$$

where $\mathcal M$ is the two-dimensional Besicovitch mean。

---

# 22. Weighted limit-periodic lemma

Let：

$$
F\in B^2(\mathbb Z^2)
$$

be limit-periodic with mean zero。

Let：

$$
W_N(h,d)
$$

be supported in an：

$$
O(N)\times O(N)
$$

region and satisfy：

$$
\|W_N\|_\infty
\ll
N^3.
$$

Suppose：

$$
\sum_{h,d}|W_N(h,d)|^2
\ll
N^8.
$$

Then periodic approximation plus Cauchy–Schwarz gives：

## Lemma 22.1

If every fixed periodic approximant has weighted discrepancy：

$$
O_q(N^4),
$$

then：

$$
\boxed{
\sum_{h,d}
W_N(h,d)F(h,d)
=
o(N^5).
}
$$

---

# 23. Proof mechanism of Lemma 22.1

Let：

$$
F_q
$$

be a fixed periodic approximation with：

$$
\|F-F_q\|_{B^2}<\varepsilon.
$$

Then：

$$
\sum W_NF_q
=
O_q(N^4)
=
o(N^5).
$$

For the error：

$$
\begin{aligned}
\left|
\sum W_N(F-F_q)
\right|
&\le
\left(
\sum|W_N|^2
\right)^{1/2}
\\
&\quad\times
\left(
\sum|F-F_q|^2
\right)^{1/2}
\\
&\le
O(N^4)
\cdot
O(\varepsilon N)
\\
&=
O(\varepsilon N^5),
\end{aligned}
$$

after taking the large-$N$ Besicovitch average。

First：

$$
N\to\infty,
$$

then：

$$
\varepsilon\to0.
$$

---

# 24. Full deterministic subpower closure

Apply Lemma 22.1 with：

$$
F=\mathfrak K_4,
$$

and：

$$
W_N=\Omega_N.
$$

The diagonal：

$$
h=d
$$

and other collision lines contribute only：

$$
N^{4+o(1)}
$$

by the v3.6 lower-dimensional count。

Therefore：

## Theorem 24.1 · Full Model Subpower Closure

$$
\boxed{
\mathfrak M_{4,N}
=
o(N^5).
}
$$

Thus the full deterministic singular-series model has no persistent $N^5$ main term。

---

# 25. What Theorem 24.1 does not prove

It does **not** imply any fixed：

$$
\eta_M>0.
$$

The bound is compatible with：

$$
\frac{N^5}{\log N},
$$

or：

$$
N^{5-o(1)}.
$$

Therefore it does not yet close the v3.6 Gate B。

---

# 26. High-conductor rational tail norm

The exact surviving spectrum motivates：

$$
\boxed{
\mathfrak C_\beta(N)
=
\sum_{
\substack{
(\alpha,\beta)\in\operatorname{Spec}(\mathfrak K_4)
\\
\beta\ne0
}
}
|
\widehat{\mathfrak K}_4(\alpha,\beta)
|
M_N(\beta),
}
$$

interpreted through finite conductor truncation / a justified summation procedure。

Using：

$$
|\widehat\Omega_N|
\ll
N^4M_N(\beta),
$$

a sufficient deterministic gate is：

## $\operatorname{PRT}(\eta)$ · Parallelogram Rational Tail

$$
\boxed{
\mathfrak C_\beta(N)
\ll
N^{1-\eta+o(1)}
}
$$

for some：

$$
\eta>0.
$$

Then：

$$
\boxed{
\mathfrak M_{4,N}
\ll
N^{5-\eta+o(1)}.
}
$$

This is deliberately stronger than necessary but exposes the remaining conductor problem in one spectral direction。

---

# 27. Two-dimensional stronger gate

Using the sharper Theorem 13.1, define：

$$
\boxed{
\mathfrak C_{\alpha,\beta}(N)
=
\sum_{
\beta\ne0
}
|
\widehat{\mathfrak K}_4(\alpha,\beta)
|
M_N(\alpha)
M_N(\beta).
}
$$

If：

$$
\boxed{
\mathfrak C_{\alpha,\beta}(N)
\ll
N^{2-\eta+o(1)},
}
$$

then again：

$$
\boxed{
\mathfrak M_{4,N}
\ll
N^{5-\eta+o(1)}.
}
$$

---

# 28. Why adding-fractions enters exactly here

The refined singular-series expansion sums reduced fractions：

$$
\theta_i=\frac{a_i}{q_i},
$$

with：

$$
\theta_1+\theta_2+\theta_3+\theta_4=0.
$$

The surviving frequency：

$$
\beta=\theta_3+\theta_4
$$

is nonzero。

The dangerous spectral region is：

$$
\|\beta\|\lesssim N^{-1},
$$

where：

$$
M_N(\beta)\asymp N.
$$

Thus the hard counting problem is precisely：

> how many weighted rational tuples satisfy the integer-sum condition while producing a nonzero but very small two-fraction sum $\theta_3+\theta_4$？

This is an adding-fractions problem。

Bloom–Kuperberg's work supplies strong counting machinery for rational linear equations and denominator separation, but no theorem is asserted here that directly closes $\operatorname{PRT}(\eta)$ for this even four-fraction covariance。

---

# 29. Spectral pairing interpretation

The rational spectrum separates the Wick-like channels cleanly。

### First pairing

$$
(0,h)(d,d+h)
$$

is exactly：

$$
\beta=0.
$$

It is completely removed by the pair-square subtraction。

### Second pairing

$$
(0,d)(h,d+h)
$$

appears on：

$$
\alpha=0,
\qquad
\beta\ne0.
$$

### Third pairing

$$
(0,d+h)(h,d)
$$

occupies genuinely two-dimensional rational frequencies。

Thus v3.8 gives a coefficient-level explanation of the v3.7 local cancellation theorem。

---

# 30. Finite-conductor Sobolev diagnostics

For：

$$
q=6,30,210,2310,
$$

the reference package computes：

$$
\mathfrak H_d(q).
$$

The values grow slowly in these samples。

This suggests that a quantitative $d$-antiderivative estimate may exist。

But no asymptotic bound such as：

$$
\mathfrak H_d(q)\ll(\log q)^A
$$

or：

$$
\mathfrak H_d(q)\ll q^\varepsilon
$$

is promoted to theorem in this node。

This is a candidate v3.9 direction。

---

# 31. Stronger future Sobolev route

If one can prove that the full limit-periodic covariance possesses a $d$-antiderivative：

$$
\boxed{
\Delta_d\mathfrak G_4
=
\mathfrak K_4
}
$$

with quantitatively controlled Besicovitch $B^2$ norm, then summation by parts can exploit：

$$
\Delta_d\Omega_N=O(N^2)
$$

instead of：

$$
\Omega_N=O(N^3).
$$

This has the potential to gain an additional power of $N$。

The missing point is a quantitative conductor-uniform Sobolev estimate, not the algebraic existence of nonzero frequencies。

---

# 32. Current deterministic status

After v3.8：

```text
constant spectral mode
    CLOSED

entire beta=0 axis
    CLOSED

full deterministic N^5 main term
    EXCLUDED: o(N^5)

fixed power eta_M > 0
    OPEN

dangerous modes
    beta != 0
    and beta very close to an integer

analytic interface
    adding fractions / conductor Sobolev
```

This is a substantially narrower high-conductor GAP than v3.7。

---

# 33. Suggested v3.9 direction

Recommended：

`RH-Parallelogram-SobolevConductor v3.9`

Tasks：

1. use the exact finite-$q$ coefficient：
   $$
   \widehat K_q(\cdot,\beta)
   =
   B_{-\beta}\ast B_\beta;
   $$
2. bound：
   $$
   \mathfrak H_d(q)
   =
   \sum_{\beta\ne0}
   \frac{
   \|\widehat K_q(\cdot,\beta)\|_2^2
   }{
   |1-e(\beta)|^2
   };
   $$
3. exploit：
   $$
   \|\rho_q\|_2^2=q/\phi(q)-1,
   $$
   and uniform：
   $$
   \|\rho_q\|_4;
   $$
4. classify $\beta$ by reduced denominator；
5. use adding-fractions / Farey-spacing estimates to control near-zero $\beta$；
6. determine whether：
   $$
   \mathfrak H_d(q)
   \ll_\varepsilon q^\varepsilon
   $$
   or stronger；
7. convert such a bound into a weighted $\Omega_N$ power saving；
8. only then return to actual prime deviation。

This is the canonical deterministic continuation。

---

# 34. GAP ledger

## CLOSED / REDUCED

### G1. Rational parallelogram phase

```text
CLOSED
```

$$
h\alpha+d\beta.
$$

### G2. Finite four-point coefficient

```text
CLOSED
```

### G3. Entire $\beta=0$ spectral axis

```text
ZERO EXACTLY
```

### G4. Rowwise $d$ mean

```text
ZERO EXACTLY
```

### G5. $\Omega_N$ Fourier formula

```text
CLOSED
```

### G6. $\Omega_N$ multiplier bound

```text
CLOSED
```

### G7. Full deterministic model

```text
o(N^5)
```

### G8. Nonzero constant $N^5$ model term

```text
EXCLUDED
```

---

## OPEN

### G9. Quantitative nonzero-$\beta$ conductor tail

```text
OPEN
```

### G10. Full deterministic fixed $\eta_M>0$

```text
OPEN
```

### G11. Actual prime four-point deviation

```text
OPEN
```

### G12. Complete quartic $\eta_Q>0$

```text
OPEN
```

### G13. RH

```text
OPEN
```

---

# 35. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FINITE-Q AXIS CANCELLATION = EXACT
FULL B2 LIMIT-PERIODIC CLOSURE = DETERMINISTIC MODEL RESULT

o(N^5) != N^(5-eta)

FINITE-Q SOBOLEV NUMERICS = DIAGNOSTIC ONLY

NO FULL ETA_M > 0 PROVED
NO PRIME ETA_Q > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\beta=0\text{ axis absent}
\Longrightarrow
\eta_M>0.
$$

Forbidden：

$$
o(N^5)
\Longrightarrow
\text{fixed zero-strip progress}.
$$

Forbidden：

$$
\mathfrak H_d(q)\text{ looks bounded numerically}
\Longrightarrow
\sup_q\mathfrak H_d(q)<\infty.
$$

---

# 36. One-line status

> v3.8 specializes the refined singular-series rational-frequency expansion to the parallelogram and strengthens the finite-modulus centering theorem from one vanished zero mode to an entire vanished spectral axis. Writing the four rational phases under the constraint $\theta_1+\theta_2+\theta_3+\theta_4=0$ gives the two-dimensional phase $h\alpha+d\beta$, with coefficient $C_q(\alpha,\beta)=\sum_t\rho_q(t)\rho_q(\alpha-t)\rho_q(\beta-t)\rho_q(t-\alpha-\beta)$. The pair-square subtraction has coefficient $P_q(\alpha)$ only at $\beta=0$, and $C_q(\alpha,0)=P_q(\alpha)$ identically. Hence $\widehat{\mathfrak K}_{4,q}(\alpha,0)=0$ for every $\alpha$, equivalently every fixed row has zero mean in the $d$ direction. The surviving $\alpha=0,\beta\neq0$ axis is exactly the second Wick-like pairing channel. The endpoint-Cesàro parallelogram weight has exact transform $\widehat\Omega_N=\sum_{n<m}w_N(n)w_N(m)e((m-n)\beta)E_{n-1}(\alpha)$ and satisfies $|\widehat\Omega_N|\ll N^3M_N(\alpha)M_N(\beta)$, so every surviving deterministic mode must pay genuine $d$-oscillation. Independently, local Euler-product $L^2$ defects are $O(p^{-3})$, placing the full covariance in two-dimensional Besicovitch $B^2$ as a limit-periodic function. Periodic approximation, the vanished mean, and Cauchy–Schwarz then imply the full deterministic model is $o(N^5)$: the high-conductor tail cannot restore a nonzero $N^5$ main term. This remains subpower only. The new quantitative gap is to sum nonzero rational $\beta$ modes strongly enough for a fixed $N^{-\eta}$ gain; the natural next target is a conductor-uniform $d$-Sobolev / adding-fractions estimate.

---

# 37. References

1. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.  
   arXiv: https://arxiv.org/abs/math/0409258

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   arXiv: https://arxiv.org/abs/2301.06095

3. Thomas F. Bloom, Vivian Kuperberg, **Odd moments and adding fractions**, *Proceedings of the London Mathematical Society* 131 (2025), e70068.  
   DOI: https://doi.org/10.1112/plms.70068

4. Emmanuel Kowalski, **Averages of Euler products, distribution of singular series and the ubiquity of Poisson distribution**, *Acta Arithmetica* 148 (2011), 153–187.  
   arXiv: https://arxiv.org/abs/0805.4682

5. Eugen Keil, **Limit-periodic functions**, *Acta Arithmetica* 152 (2012), 159–174.

6. AMRAL, **RH-RefinedSingularSeries-Parallelogram v3.7**.

---

# 38. Provenance

研究主導：Neo.K

v3.8 rational-frequency specialization、spectral-axis cancellation、weight Fourier multiplier、limit-periodic subpower closure、Sobolev-conductor gate、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 parallelogram rational spectrum / high-conductor quantitative tail 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
