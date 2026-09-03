工程紀錄 · 第五弧線 v3.9 · 2026-09-03 · UNIFORM_CONDUCTOR_SOBOLEV · FINITE_MODEL_N4 · BESICOVITCH_TRANSFER_GAP · RH_CLAIM_FALSE

# Parallelogram Sobolev Conductor：Uniform $d$-Antiderivative Bound、Finite-Conductor $N^4$ Scale 與 Besicovitch Transfer Gap

**RH-Parallelogram-SobolevConductor v3.9**

本節點承接：

- `RH-Parallelogram-RamanujanTail v3.8`
- `RH-RefinedSingularSeries-Parallelogram v3.7`

v3.8 已證，對每個 finite squarefree modulus $q$：

$$
\widehat{\mathfrak K}_{4,q}(\alpha,0)=0
$$

for every $\alpha$。

因此可以定義 $d$-方向 periodic antiderivative。

v3.8 的主要 quantitative GAP 是：

$$
\mathfrak H_d(q)
=
\sum_{\substack{\alpha,\beta\in G_q\\\beta\ne0}}
\frac{
|\widehat{\mathfrak K}_{4,q}(\alpha,\beta)|^2
}{
|1-e(\beta)|^2
}.
$$

當時只知道 finite numerics grow slowly。

v3.9 closes this finite-conductor problem completely：

## Main Theorem

There exists an absolute constant：

$$
\boxed{
C_{\rm Sob}<\infty
}
$$

such that for every squarefree：

$$
q,
$$

$$
\boxed{
\mathfrak H_d(q)
\le
C_{\rm Sob}.
}
$$

No：

$$
q^\varepsilon
$$

loss is required。

Consequently the zero-$d$-mean antiderivative：

$$
\Delta_d\mathfrak G_q
=
\mathfrak K_{4,q}
$$

satisfies：

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
|\mathfrak G_q(h,d)|^2
\le
C_{\rm Sob}.
}
$$

This gives an improved finite-conductor weighted model estimate：

for：

$$
q\le N,
$$

$$
\boxed{
\left|
\sum_{h,d}
\Omega_N(h,d)
\mathfrak K_{4,q}(h,d)
\right|
\ll
N^4.
}
$$

After deleting the lower-dimensional collision line：

$$
h=d,
$$

the genuine four-distinct model is：

$$
\boxed{
O_\varepsilon(N^{4+\varepsilon}).
}
$$

Thus the v3.7 finite-conductor estimate：

$$
N^4q
\left(
\frac q{\phi(q)}
\right)^3
$$

is sharpened to essentially the natural quartic lower-order scale：

$$
\boxed{
N^{4+o(1)}.
}
$$

The remaining obstruction is no longer finite-conductor Sobolev growth。

It is the quantitative passage from finite Euler approximants to the **actual full singular-series sequence on finite boxes**。

v3.8 established：

$$
\mathfrak K_{4,q_y}
\to
\mathfrak K_4
$$

in two-dimensional Besicovitch：

$$
B^2.
$$

v3.9 uniform Sobolev control implies the antiderivatives：

$$
\mathfrak G_{q_y}
$$

are uniformly bounded in the Besicovitch Hilbert space。

Hence a weak limit exists and the full covariance has a $B^2$ antiderivative：

$$
\boxed{
\Delta_d\mathfrak G_4
=
\mathfrak K_4
\quad
\text{in }B^2.
}
$$

But this is a mean-square equivalence-class statement。

It does **not** by itself imply a pointwise identity on every integer lattice point, nor a quantitative finite-box estimate：

$$
\sum_{h,d\le O(N)}
\Omega_N(h,d)
\mathfrak K_4(h,d)
=
O(N^4).
$$

Therefore：

```text
FINITE-CONDUCTOR SOBOLEV
    CLOSED

FULL B^2 SOBOLEV CLOSURE
    CLOSED

QUANTITATIVE FINITE-BOX TRANSFER
    OPEN
```

No RH claim is made。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

BETA_ZERO_AXIS = CLOSED_FROM_V3_8

YOUNG_4_OVER_3_BOUND = CLOSED
REDUCED_DENOMINATOR_CORRELATION_MAJORANT = CLOSED
COPRIME_CSC2_IDENTITY = CLOSED

UNIFORM_FINITE_Q_SOBOLEV = CLOSED
SUP_Q H_d(q) < INFINITY

FINITE_Q_ANTIDERIVATIVE_B2 = UNIFORMLY_BOUNDED
FINITE_Q_WEIGHTED_MODEL_Q_LE_N = O(N^4)

FOUR_DISTINCT_FINITE_Q_MODEL = O_epsilon(N^(4+epsilon))

FULL_K4_B2_ANTIDERIVATIVE = CLOSED_IN_HILBERT_COMPLETION
POINTWISE_FULL_ANTIDERIVATIVE = NOT_PROVED

FULL_FINITE_BOX_N4_BOUND = NOT_PROVED
FULL_FIXED_ETA_M_POSITIVE = NOT_PROVED

ACTUAL_PRIME_DEVIATION = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Finite spectral coefficient

From v3.8：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(\cdot,\beta)
=
B_{-\beta}
\ast
B_\beta,
}
$$

for：

$$
\beta\ne0,
$$

where：

$$
\boxed{
B_\beta(t)
=
\rho_q(t)
\rho_q(t+\beta).
}
$$

Convolution is on：

$$
G_q=\mathbb Z/q\mathbb Z.
$$

---

# 2. Young $\ell^{4/3}$ inequality

Young's convolution inequality gives：

$$
\boxed{
\|
B_{-\beta}
\ast
B_\beta
\|_2
\le
\|
B_{-\beta}
\|_{4/3}
\|
B_\beta
\|_{4/3}.
}
$$

Translation and reflection preserve the norm, so：

$$
\boxed{
\|
\widehat{\mathfrak K}_{4,q}
(\cdot,\beta)
\|_2^2
\le
\|
B_\beta
\|_{4/3}^4.
}
$$

This choice of exponent is the key improvement over the cruder $\ell^1\ast\ell^2$ estimate。

---

# 3. Extended multiplicative coefficient

Define：

$$
F_q(t)
=
\frac{\mu(r(t))}{\phi(r(t))}
$$

for all：

$$
t\in G_q,
$$

including：

$$
F_q(0)=1.
$$

Here：

$$
r(t)
=
\frac q{(t,q)}.
$$

Then：

$$
\boxed{
\rho_q
=
F_q-\delta_0.
}
$$

For：

$$
u(t)
=
|F_q(t)|^{4/3},
$$

the function $u$ factors exactly under CRT。

---

# 4. Reduced denominator of $\beta$

Let：

$$
r=r(\beta)
$$

be the reduced denominator of：

$$
\beta\in G_q.
$$

Equivalently, for：

$$
p\mid q,
$$

$$
p\mid r
\Longleftrightarrow
\beta\not\equiv0\pmod p.
$$

Because：

$$
|\rho_q|\le|F_q|,
$$

we obtain：

$$
\begin{aligned}
\|B_\beta\|_{4/3}^{4/3}
&=
\sum_t
|\rho_q(t)\rho_q(t+\beta)|^{4/3}
\\
&\le
\sum_t
u(t)u(t+\beta).
\end{aligned}
$$

The right side factors prime-by-prime。

---

# 5. Local factor when $p\nmid r$

If：

$$
\beta\equiv0\pmod p,
$$

then the local correlation is：

$$
\boxed{
A_{0,p}
=
1+
(p-1)^{-5/3}.
}
$$

Indeed the zero residue contributes $1$ and the remaining $p-1$ residues each contribute：

$$
(p-1)^{-8/3}.
$$

---

# 6. Local factor when $p\mid r$

If：

$$
\beta\not\equiv0\pmod p,
$$

two residues contain one zero coordinate, while the remaining：

$$
p-2
$$

contain two nonzero coordinates。

Thus：

$$
\boxed{
A_{1,p}
=
(p-1)^{-4/3}
\left[
2+
(p-2)(p-1)^{-4/3}
\right].
}
$$

Therefore：

## Theorem 6.1

$$
\boxed{
\|B_\beta\|_{4/3}^{4/3}
\le
\prod_{\substack{p\mid q\\p\nmid r}}
A_{0,p}
\prod_{p\mid r}
A_{1,p}.
}
$$

---

# 7. Coefficient $\ell^2$ bound

Raise Theorem 6.1 to the third power and use Section 2：

$$
\boxed{
\|
\widehat{\mathfrak K}_{4,q}
(\cdot,\beta)
\|_2^2
\le
\prod_{\substack{p\mid q\\p\nmid r}}
A_{0,p}^3
\prod_{p\mid r}
A_{1,p}^3.
}
$$

This bound depends only on the reduced denominator：

$$
r.
$$

---

# 8. Coprime reciprocal-sine identity

For：

$$
r>1,
$$

define：

$$
\boxed{
S_2(r)
=
\sum_{\substack{1\le a<r\\ \gcd(a,r)=1}}
\frac1{
|1-e(a/r)|^2
}.
}
$$

Since：

$$
|1-e(x)|^2
=
4\sin^2(\pi x),
$$

and：

$$
\sum_{a=1}^{r-1}
\csc^2\left(\frac{\pi a}{r}\right)
=
\frac{r^2-1}{3},
$$

Möbius inversion over reduced denominators gives：

## Theorem 8.1

$$
\boxed{
S_2(r)
=
\frac{
J_2(r)
}{12},
}
$$

where：

$$
\boxed{
J_2(r)
=
r^2
\prod_{p\mid r}
\left(
1-\frac1{p^2}
\right)
}
$$

is the second Jordan totient。

---

# 9. Group the Sobolev sum by denominator

Every nonzero：

$$
\beta\in G_q
$$

has a unique reduced denominator：

$$
r\mid q,
\qquad
r>1.
$$

For fixed $r$, the reduced fractions are：

$$
\frac ar,
\qquad
(a,r)=1.
$$

Hence Sections 7–8 give：

$$
\begin{aligned}
\mathfrak H_d(q)
&\le
\frac1{12}
\sum_{\substack{r\mid q\\r>1}}
J_2(r)
\\
&\quad\times
\prod_{\substack{p\mid q\\p\nmid r}}
A_{0,p}^3
\prod_{p\mid r}
A_{1,p}^3.
\end{aligned}
$$

---

# 10. Euler-product majorant

Because $q$ is squarefree, the divisor sum in Section 9 factors：

$$
\boxed{
\mathfrak H_d(q)
\le
\frac1{12}
\prod_{p\mid q}
\left[
A_{0,p}^3
+
(p^2-1)A_{1,p}^3
\right].
}
$$

We harmlessly retain the：

$$
r=1
$$

term to obtain an upper bound。

---

# 11. Convergence of the universal product

As：

$$
p\to\infty,
$$

$$
A_{0,p}^3
=
1+
O(p^{-5/3}),
$$

while：

$$
(p^2-1)A_{1,p}^3
=
O(p^{-2}).
$$

Therefore：

$$
\boxed{
\sum_p
\left[
A_{0,p}^3-1
+
(p^2-1)A_{1,p}^3
\right]
<
\infty.
}
$$

Hence：

## Theorem 11.1 · Uniform Conductor Sobolev Bound

The infinite Euler product：

$$
\boxed{
C_{\rm Sob}
=
\frac1{12}
\prod_p
\left[
A_{0,p}^3
+
(p^2-1)A_{1,p}^3
\right]
}
$$

converges to a finite positive constant and：

$$
\boxed{
\mathfrak H_d(q)
\le
C_{\rm Sob}
}
$$

for every squarefree $q$。

This is the main v3.9 theorem。

---

# 12. Periodic antiderivative

Since：

$$
\widehat{\mathfrak K}_{4,q}(\alpha,0)=0,
$$

define：

$$
\boxed{
\widehat{\mathfrak G}_q(\alpha,\beta)
=
\frac{
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
}{
e(\beta)-1
}
}
$$

for：

$$
\beta\ne0,
$$

and：

$$
\widehat{\mathfrak G}_q(\alpha,0)=0.
$$

Then：

$$
\boxed{
\Delta_d\mathfrak G_q
=
\mathfrak K_{4,q}.
}
$$

Parseval gives：

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
|\mathfrak G_q(h,d)|^2
=
\mathfrak H_d(q)
\le
C_{\rm Sob}.
}
$$

---

# 13. $L^2$ size of the weight derivative

Extend：

$$
\Omega_N(h,d)
$$

by zero outside its triangular support。

v3.7 gives：

$$
|\Delta_d\Omega_N|
\ll
N^2.
$$

The support contains：

$$
O(N^2)
$$

lattice points。

Therefore：

## Lemma 13.1

$$
\boxed{
\sum_{h,d}
|\Delta_d\Omega_N(h,d)|^2
\ll
N^6.
}
$$

So：

$$
\boxed{
\|\Delta_d\Omega_N\|_2
\ll
N^3.
}
$$

---

# 14. Local periodic $L^2$ bound

Suppose：

$$
q\le N.
$$

On an：

$$
O(N)\times O(N)
$$

box, each residue pair modulo $q$ occurs：

$$
O((N/q+1)^2)
$$

times。

Hence：

$$
\begin{aligned}
\sum_{\text{box}}
|\mathfrak G_q|^2
&\ll
\left(
\frac Nq+1
\right)^2
q^2
\mathfrak H_d(q)
\\
&\ll
N^2.
\end{aligned}
$$

Thus：

$$
\boxed{
\|\mathfrak G_q\|_{L^2(\text{box})}
\ll
N.
}
$$

uniformly for：

$$
q\le N.
$$

---

# 15. Finite-conductor weighted summation by parts

Using：

$$
\mathfrak K_{4,q}
=
\Delta_d\mathfrak G_q,
$$

and the compact support of：

$$
\Omega_N,
$$

discrete summation by parts gives：

$$
\boxed{
\sum_{h,d}
\Omega_N(h,d)
\mathfrak K_{4,q}(h,d)
=
-
\sum_{h,d}
\Delta_d^-\Omega_N(h,d)
\mathfrak G_q(h,d).
}
$$

Cauchy–Schwarz with Sections 13–14 yields：

## Theorem 15.1 · Uniform Finite-Conductor Model Bound

For every squarefree：

$$
q\le N,
$$

$$
\boxed{
\left|
\sum_{h,d}
\Omega_N(h,d)
\mathfrak K_{4,q}(h,d)
\right|
\ll
N^4.
}
$$

The implied constant is absolute。

---

# 16. Four-distinct collision deletion

The v3.6 genuine four-point model deletes：

$$
h=d.
$$

This is a one-dimensional set of：

$$
O(N)
$$

points。

Finite singular-series factors satisfy the standard subpower bound：

$$
\|\mathfrak K_{4,q}\|_\infty
\ll_\varepsilon
q^\varepsilon.
$$

For：

$$
q\le N,
$$

the removed line is therefore：

$$
O_\varepsilon(
N^{4+\varepsilon}
).
$$

Hence：

## Corollary 16.1

The finite-conductor genuine four-distinct model satisfies：

$$
\boxed{
\mathfrak M_{4,N}^{(q),\rm dist}
\ll_\varepsilon
N^{4+\varepsilon}
}
$$

uniformly for squarefree：

$$
q\le N.
$$

---

# 17. Improvement over v3.7

v3.7 obtained：

$$
\mathfrak M_{4,N}^{(q)}
\ll
N^4q
\left(
\frac q{\phi(q)}
\right)^3.
$$

v3.9 improves this to：

$$
\boxed{
N^4
}
$$

before collision deletion, uniformly over：

$$
q\le N.
$$

Thus finite conductor is no longer a quantitative obstacle。

---

# 18. Primorial truncation at the full $q\le N$ range

Let：

$$
q_y
=
\prod_{p\le y}p.
$$

For：

$$
y\le
(1-o(1))\log N,
$$

we have：

$$
q_y\le N
$$

for large $N$。

Therefore：

$$
\boxed{
\mathfrak M_{4,N}^{(\le y)}
\ll_\varepsilon
N^{4+\varepsilon}.
}
$$

So essentially all local prime factors up to：

$$
p\lesssim\log N
$$

may be incorporated without any conductor power tax。

---

# 19. Besicovitch Sobolev closure

v3.8 established, along nested primorial moduli：

$$
q_y,
$$

that：

$$
\mathfrak K_{4,q_y}
\to
\mathfrak K_4
$$

strongly in the two-dimensional Besicovitch Hilbert space：

$$
B^2.
$$

Let：

$$
\mathfrak G_{q_y}
$$

be the zero-$d$-mean antiderivatives from Section 12。

Theorem 11.1 gives：

$$
\boxed{
\sup_y
\|
\mathfrak G_{q_y}
\|_{B^2}
<\infty.
}
$$

By weak compactness in the Hilbert completion, a subsequence converges weakly to some：

$$
\mathfrak G_4\in B^2.
$$

---

# 20. Difference operator closure

The discrete difference：

$$
\Delta_d
$$

is a bounded linear operator on：

$$
B^2.
$$

Therefore：

$$
\Delta_d
\mathfrak G_{q_{y_j}}
\rightharpoonup
\Delta_d
\mathfrak G_4.
$$

But：

$$
\Delta_d
\mathfrak G_{q_{y_j}}
=
\mathfrak K_{4,q_{y_j}}
\to
\mathfrak K_4
$$

strongly in：

$$
B^2.
$$

Hence：

## Theorem 20.1 · Full Besicovitch Sobolev Closure

There exists：

$$
\boxed{
\mathfrak G_4\in B^2
}
$$

such that：

$$
\boxed{
\Delta_d\mathfrak G_4
=
\mathfrak K_4
}
$$

as an equality in the Besicovitch Hilbert completion, with：

$$
\boxed{
\|\mathfrak G_4\|_{B^2}^2
\le
C_{\rm Sob}.
}
$$

---

# 21. What the full $B^2$ antiderivative does not give

The identity：

$$
\Delta_d\mathfrak G_4
=
\mathfrak K_4
$$

holds in：

$$
B^2,
$$

i.e. modulo a sequence of Besicovitch seminorm zero。

It does not automatically give：

$$
\boxed{
\mathfrak K_4(h,d)
=
\mathfrak G_4(h,d+1)
-
\mathfrak G_4(h,d)
}
$$

pointwise for every integer：

$$
(h,d).
$$

Nor does it provide a quantitative rate for the finite Euler approximants。

Therefore one cannot yet apply Section 15 directly to the full pointwise singular series with an absolute：

$$
O(N^4)
$$

error。

---

# 22. Why $B^2$-null is not enough for fixed power

Suppose：

$$
R(h,d)
$$

has：

$$
\|R\|_{B^2}=0.
$$

Then on an：

$$
N\times N
$$

box：

$$
\sum|R|^2
=
o(N^2).
$$

But：

$$
\|\Omega_N\|_2
\asymp
N^4.
$$

Cauchy only gives：

$$
\boxed{
\sum
\Omega_NR
=
o(N^5).
}
$$

This recovers the v3.8 subpower conclusion, but does not force：

$$
N^{5-\eta}
$$

for any fixed：

$$
\eta>0.
$$

So the distinction：

```text
B^2 equality
vs.
quantitative finite-box equality
```

is essential。

---

# 23. New high-conductor GAP

The finite-conductor Sobolev norm is no longer the problem。

The canonical next object is the transfer defect between：

$$
\mathfrak K_4
$$

and a pointwise / quantitatively convergent antiderivative representation。

One possible formulation is：

## Quantitative Sobolev Approximation Transfer $\operatorname{QSAT}(\eta)$

Construct approximants：

$$
\mathfrak G^{(Y)}
$$

such that：

$$
\Delta_d\mathfrak G^{(Y)}
$$

approximates the actual pointwise：

$$
\mathfrak K_4
$$

on the：

$$
O(N)\times O(N)
$$

parallelogram region with weighted error：

$$
\boxed{
\left|
\sum
\Omega_N
\left[
\mathfrak K_4
-
\Delta_d\mathfrak G^{(Y)}
\right]
\right|
\ll
N^{5-\eta}.
}
$$

Together with：

$$
\|\mathfrak G^{(Y)}\|_{B^2}
=O(1),
$$

this would give a fixed power saving for the deterministic model。

---

# 24. Rational-frequency interpretation

The Sobolev theorem says：

$$
\boxed{
\sum_{\beta\ne0}
\frac{
\|\widehat{\mathfrak K}_{4,q}
(\cdot,\beta)\|_2^2
}{
|1-e(\beta)|^2
}
\le
C_{\rm Sob}.
}
$$

Thus dangerous near-zero rational frequencies cannot carry arbitrary total $L^2$ mass even as conductor grows。

This is much stronger than mere：

$$
\beta\ne0.
$$

The remaining issue is how this globally bounded rational Sobolev mass is sampled by the finite-box multiplier：

$$
\widehat\Omega_N.
$$

That is now the exact adding-fractions / large-sieve interface。

---

# 25. Relation to Farey spacing

Reduced fractions with denominators：

$$
\le Q
$$

are separated by at least：

$$
Q^{-2}.
$$

Classical large-sieve methods exploit exactly this fact to sum Fourier values over rational points。

Bloom–Kuperberg's adding-fractions work develops sharper counting for rational linear relations beyond simple spacing。

v3.9 shows why those tools enter：

> the coefficient Sobolev mass is already uniformly bounded; what remains is a restriction/sampling theorem for the finite-box multiplier over the full rational spectrum。

No existing theorem is asserted here to close that restriction problem。

---

# 26. Numerical checks

For：

$$
q=6,30,210,2310,
$$

the actual：

$$
\mathfrak H_d(q)
$$

values are approximately：

$$
1.46,\quad
5.40,\quad
8.67,\quad
10.01.
$$

The analytic finite-$q$ Young majorants are larger but finite and compatible with the uniform Euler-product theorem。

The reference implementation also checks：

$$
\Delta_d\mathfrak G_q
=
\mathfrak K_{4,q}
$$

to machine precision and verifies the weighted discrete summation-by-parts identity。

These checks are normalization evidence only。

---

# 27. Strategic consequence

The deterministic branch has now crossed three successive barriers：

```text
v3.7
zero scalar mode removed

v3.8
entire beta=0 axis removed
full model o(N^5)

v3.9
all finite-conductor beta!=0 Sobolev mass uniformly bounded
finite q<=N model at N^4 scale
```

So the remaining deterministic obstacle is **not local congruence size**。

It is：

$$
\boxed{
\text{quantitative high-conductor sampling / finite-box transfer}.
}
$$

This is a significantly narrower analytic problem。

---

# 28. Suggested v3.10 direction

Recommended：

`RH-Parallelogram-SobolevTailTransfer v3.10`

Tasks：

1. express the full refined covariance as a rational Fourier series grouped by reduced denominator；
2. retain the uniform Sobolev estimate of v3.9；
3. split rational frequencies at denominator：
   $$
   Q;
   $$
4. use large-sieve / Farey-spacing bounds on：
   $$
   \widehat\Omega_N(\alpha,\beta);
   $$
5. use adding-fractions estimates for collisions between different denominator representations；
6. optimize：
   $$
   Q=N^\theta;
   $$
7. seek any fixed：
   $$
   \eta>0
   $$
   in the full deterministic model；
8. if the restriction step only gives logarithmic gain, record that as a genuine no-go before returning to actual primes。

This is the canonical deterministic continuation。

---

# 29. GAP ledger

## CLOSED / REDUCED

### G1. Entire $\beta=0$ axis

```text
CLOSED
```

### G2. Finite-$q$ Sobolev norm

```text
UNIFORMLY BOUNDED
```

### G3. Finite-$q$ antiderivative

```text
CLOSED
```

### G4. Finite conductor $q\le N$

```text
N^(4+o(1))
```

### G5. Full Besicovitch antiderivative

```text
CLOSED_IN_B2
```

---

## OPEN

### G6. Quantitative pointwise / finite-box Sobolev transfer

```text
OPEN
```

### G7. Full deterministic fixed：

$$
\eta_M>0
$$

```text
OPEN
```

### G8. Actual prime four-point deviation

```text
OPEN
```

### G9. Complete quartic：

$$
\eta_Q>0
$$

```text
OPEN
```

### G10. RH

```text
OPEN
```

---

# 30. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

UNIFORM FINITE-CONDUCTOR SOBOLEV = EXACT
FINITE-Q N^4 WEIGHTED BOUND = EXACT AT STATED LEVEL

FULL B2 ANTIDERIVATIVE = HILBERT-SPACE STATEMENT

B2 ANTIDERIVATIVE != POINTWISE ANTIDERIVATIVE
B2 ZERO DEFECT != FIXED-POWER FINITE-BOX DEFECT

NO FULL ETA_M > 0 PROVED
NO PRIME ETA_Q > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\sup_q\mathfrak H_d(q)<\infty
\Longrightarrow
\mathfrak M_{4,N}=O(N^4)
$$

without a justified full-spectrum finite-box transfer。

Forbidden：

$$
B^2\text{ equality}
\Longrightarrow
\text{pointwise equality}.
$$

Forbidden：

$$
N^{4+o(1)}
\text{ for finite }q\le N
\Longrightarrow
\text{same for infinite conductor}.
$$

---

# 31. One-line status

> v3.9 closes the finite-conductor Sobolev problem completely. For each nonzero rational frequency $\beta$, the finite parallelogram covariance coefficient is the convolution $B_{-\beta}*B_\beta$ with $B_\beta(t)=\rho_q(t)\rho_q(t+\beta)$. Applying Young in the sharp $\ell^{4/3}*\ell^{4/3}\to\ell^2$ form reduces its squared $\ell^2$ norm to a CRT-factorable $4/3$ correlation. Grouping frequencies by reduced denominator $r$ and using the exact identity $\sum_{(a,r)=1}|1-e(a/r)|^{-2}=J_2(r)/12$ produces an Euler-product majorant whose local excess is only $O(p^{-5/3})+O(p^{-2})$. The product converges, proving $\sup_q\mathfrak H_d(q)<\infty$ over all squarefree conductors. Hence the zero-$d$-mean periodic antiderivatives $\mathfrak G_q$ have uniformly bounded $B^2$ norm. Summation by parts against the v3.6 Cesàro weight, whose discrete derivative has $\ell^2$ norm $O(N^3)$, gives an $O(N^4)$ finite-conductor model bound uniformly for $q\le N$, or $N^{4+o(1)}$ after deleting collision lines. Along primorial approximants, weak compactness yields a full Besicovitch $B^2$ antiderivative of the infinite refined covariance. This is a genuine Sobolev closure but not yet a fixed-power theorem for the actual pointwise full singular series: $B^2$ equality lacks the quantitative finite-box rate needed to replace the earlier $o(N^5)$ conclusion by $N^{5-\eta}$. The remaining deterministic GAP is therefore a high-conductor restriction/sampling problem, not conductor growth of the covariance itself.

---

# 32. References

1. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.  
   arXiv: https://arxiv.org/abs/math/0409258

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   arXiv: https://arxiv.org/abs/2301.06095

3. Thomas F. Bloom, Vivian Kuperberg, **Odd moments and adding fractions**, *Proceedings of the London Mathematical Society* 131 (2025), e70068.  
   arXiv: https://arxiv.org/abs/2312.09021

4. Classical large-sieve / Farey-spacing theory of Montgomery and Vaughan.

5. AMRAL, **RH-Parallelogram-RamanujanTail v3.8**.

---

# 33. Provenance

研究主導：Neo.K

v3.9 uniform conductor Sobolev theorem、$\ell^{4/3}$ Young reduction、Jordan-totient frequency grouping、finite-conductor $N^4$ bound、Besicovitch Sobolev closure、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 parallelogram Sobolev conductor / finite-box transfer gate。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
