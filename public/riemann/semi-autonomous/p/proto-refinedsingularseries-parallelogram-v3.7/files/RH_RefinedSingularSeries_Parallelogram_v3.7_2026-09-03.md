工程紀錄 · 第五弧線 v3.7 · 2026-09-03 · PARALLELOGRAM_LOCAL_CENTERING · ZERO_FOURIER_MODE_CLOSED · HIGH_CONDUCTOR_GAP · RH_CLAIM_FALSE

# Refined Singular Series Parallelogram：Local Centering Theorem、零 Fourier Mode 消失與 High-Conductor Gap

**RH-RefinedSingularSeries-Parallelogram v3.7**

本節點承接：

- `RH-CenteredShift-FourierGap v3.6`
- Montgomery–Soundararajan refined singular-series framework
- Kuperberg constrained / smoothly weighted singular-series framework

v3.6 將第一個 $N^5$-capable arithmetic object壓成 genuine four-distinct equal-gap covariance。

對：

$$
h,d\ge1,
\qquad
d\ne h,
$$

parallelogram offsets是：

$$
\boxed{
\mathcal H_{h,d}
=
\{0,h,d,h+d\}.
}
$$

定義：

$$
\boxed{
\mu_h
=
\mathfrak S(h)-1,
}
$$

以及 refined four-point covariance backbone：

$$
\boxed{
\mathfrak K_4(h,d)
=
\mathfrak S_0(0,h,d,h+d)
-
\mu_h^2.
}
$$

v3.7 不碰 actual primes。

本輪只問 deterministic local-congruence model：

> $\mathfrak K_4(h,d)$ 在二維 parallelogram parameter space是否本身具有非零 constant mean，從而強迫 $N^5$ model mass？

答案是：

$$
\boxed{
\text{NO}.
}
$$

而且 zero mean不是漸近，也不是 numerical observation。

對**每一個 finite squarefree Euler modulus $q$** 都精確成立：

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
\mathfrak K_{4,q}(h,d)
=
0.
}
$$

其中：

$$
\mathfrak K_{4,q}
$$

是只使用：

$$
p\mid q
$$

local factors的 truncated refined covariance。

等價地，其二維 Fourier zero mode精確消失：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(0,0)=0.
}
$$

所以 deterministic parallelogram model的 first obstruction不再是：

```text
constant N^5 main term
```

而是：

```text
nonzero arithmetic Fourier modes
+
infinite-conductor tail.
```

本輪進一步得到 elementary weighted discrepancy theorem：

若：

$$
q\le N,
$$

則 v3.6 Cesàro weight下的 finite-modulus model滿足：

$$
\boxed{
\left|
\sum_{
\substack{
h,d\ge1\\
h+d\le2N-2\\
h\ne d
}
}
\Omega_N(h,d)
\mathfrak K_{4,q}(h,d)
\right|
\ll
N^4q
\left(
\frac q{\phi(q)}
\right)^3.
}
$$

因此每個 finite-conductor model都比 $N^5$ 少一個 full power of $N$, up to conductor cost。

若：

$$
q_y
=
\prod_{p\le y}p,
$$

則：

$$
q_y
=
e^{(1+o(1))y},
$$

and：

$$
\frac{q_y}{\phi(q_y)}
\ll
\log y.
$$

所以取：

$$
y=\theta\log N,
\qquad
0<\theta<1,
$$

finite-prime model satisfies：

$$
\boxed{
\mathfrak M_{4,N}^{(\le y)}
\ll
N^{4+\theta+o(1)}.
}
$$

即 truncated fixed-power saving：

$$
\boxed{
\eta_{\rm trunc}
=
1-\theta.
}
$$

但是：

$$
\boxed{
\text{FULL } \mathfrak M_{4,N}
}
$$

還需要控制：

$$
p>y
$$

的 high-conductor tail。

目前沒有證明這個 tail具有任何 fixed：

$$
N^{-\eta}.
$$

所以 v3.7 的 canonical status是：

```text
ZERO MODE = CLOSED
FINITE CONDUCTOR = POWER-SAVED
HIGH CONDUCTOR TAIL = OPEN
```

這是一個真正的 deterministic singular-series reduction，但還不是 RH progress。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

LOCAL_PAIR_MEAN = 1
LOCAL_PAIR_SECOND_MOMENT = 1 + 1/(p-1)^3

LOCAL_GENERIC_TRIPLE_MEAN = 1
LOCAL_PARALLELOGRAM_FOUR_MEAN = 1 + 1/(p-1)^3

FINITE_MODULUS_RAW_FOUR_MEAN_EQUALS_PAIR_SECOND_MOMENT = CLOSED
FINITE_MODULUS_REFINED_COVARIANCE_MEAN_ZERO = CLOSED

K4_q_ZERO_FOURIER_MODE = CLOSED

CESARO_WEIGHT_SUP = O(N^3)
CESARO_WEIGHT_FIRST_DIFFERENCE = O(N^2)

FINITE_MODULUS_WEIGHTED_DISCREPANCY = O(N^4 q (q/phi(q))^3)

PRIMORIAL_TRUNCATED_POWER_SAVING = CLOSED_AS_REDUCTION
FULL_HIGH_CONDUCTOR_TAIL_POWER_SAVING = OPEN

FULL_MODEL_ETA_POSITIVE = NOT_PROVED
ETA_Q_POSITIVE = NOT_PROVED
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Finite local singular series

Let：

$$
q
$$

be squarefree。

For a labeled $k$-tuple：

$$
\mathcal D=(d_1,\ldots,d_k),
$$

define finite-modulus singular series：

$$
\boxed{
\mathfrak S_q(\mathcal D)
=
\prod_{p\mid q}
\left(
1-\frac{\nu_p(\mathcal D)}p
\right)
\left(
1-\frac1p
\right)^{-k},
}
$$

where：

$$
\nu_p(\mathcal D)
$$

is the number of distinct residue classes modulo $p$ occupied by the labeled offsets。

Use：

$$
\mathfrak S_q(\varnothing)=1.
$$

Define refined finite-modulus series：

$$
\boxed{
\mathfrak S_{0,q}(\mathcal D)
=
\sum_{
X\subseteq[k]
}
(-1)^{k-|X|}
\mathfrak S_q(\mathcal D_X).
}
$$

This is the finite Euler-product analogue of：

$$
\mathfrak S_0.
$$

---

# 2. Local pair factor

For a prime：

$$
p,
$$

let：

$$
L_{2,p}(h)
=
\mathfrak S_p(0,h).
$$

There are two cases。

### $h\equiv0\pmod p$

$$
\nu_p=1,
$$

so：

$$
\boxed{
L_{2,p}(0)
=
\frac p{p-1}.
}
$$

### $h\not\equiv0\pmod p$

$$
\nu_p=2,
$$

so：

$$
\boxed{
L_{2,p}(h)
=
\frac{
p(p-2)
}{
(p-1)^2
}.
}
$$

---

# 3. First pair moment

Average over：

$$
h\bmod p.
$$

Then：

$$
\begin{aligned}
\mathbb E_pL_{2,p}
&=
\frac1p
\frac p{p-1}
+
\frac{p-1}{p}
\frac{p(p-2)}{(p-1)^2}
\\
&=
\boxed{1}.
\end{aligned}
$$

So pair singular series has exact local mean one。

---

# 4. Pair second moment

Similarly：

$$
\begin{aligned}
\mathbb E_p
L_{2,p}^2
&=
\frac1p
\left(
\frac p{p-1}
\right)^2
\\
&\quad
+
\frac{p-1}{p}
\left(
\frac{
p(p-2)
}{
(p-1)^2
}
\right)^2.
\end{aligned}
$$

Simplifying：

## Theorem 4.1

$$
\boxed{
\mathbb E_pL_{2,p}^2
=
1+
\frac1{
(p-1)^3
}.
}
$$

---

# 5. Generic three-form local average

Consider：

$$
\{0,h,d\}.
$$

The local factor can be interpreted as：

$$
\frac{
\Pr_n[
n,n+h,n+d\ne0
]
}{
(1-1/p)^3
}
$$

for fixed：

$$
h,d.
$$

Now average over：

$$
h,d.
$$

The linear map：

$$
(n,h,d)
\mapsto
(n,n+h,n+d)
$$

is invertible over：

$$
\mathbb F_p^3.
$$

Therefore：

$$
n,
\quad
n+h,
\quad
n+d
$$

are jointly uniform when：

$$
n,h,d
$$

are uniform。

Thus：

## Theorem 5.1

$$
\boxed{
\mathbb E_{h,d\bmod p}
\mathfrak S_p(0,h,d)
=
1.
}
$$

Every three-element subset of：

$$
\{0,h,d,h+d\}
$$

is related by an invertible affine change of variables, so the same local mean-one identity holds for all four triples。

---

# 6. Parallelogram four-form count

Now consider：

$$
\boxed{
0,
\quad
h,
\quad
d,
\quad
h+d.
}
$$

For fixed：

$$
h,d,
$$

the raw local singular-series numerator counts：

$$
n,
\quad
n+h,
\quad
n+d,
\quad
n+h+d
$$

avoiding zero modulo $p$。

Set：

$$
x=n,
$$

$$
y=n+h,
$$

$$
z=n+d.
$$

Then：

$$
n+h+d
=
y+z-x.
$$

So the number of triples：

$$
(x,y,z)\in\mathbb F_p^3
$$

such that：

$$
x,
y,
z,
y+z-x
$$

are all nonzero is：

$$
\boxed{
(p-1)
(
p^2-3p+3
).
}
$$

---

# 7. Local raw parallelogram mean

Divide the count in Section 6 by：

$$
p^3
$$

and normalize by：

$$
(1-1/p)^4.
$$

Then：

## Theorem 7.1

$$
\boxed{
\mathbb E_{
h,d\bmod p
}
\mathfrak S_p(
0,h,d,h+d
)
=
1+
\frac1{
(p-1)^3
}.
}
$$

Comparing with Theorem 4.1：

$$
\boxed{
\mathbb E_{h,d}
\mathfrak S_p(
0,h,d,h+d
)
=
\mathbb E_h
\mathfrak S_p(0,h)^2.
}
$$

This is the local parallelogram–pair-second-moment identity。

---

# 8. Chinese remainder factorization

Let：

$$
q
$$

be squarefree。

By CRT：

$$
(h,d)\bmod q
$$

factors independently over：

$$
p\mid q.
$$

Define：

$$
\boxed{
A(q)
=
\prod_{p\mid q}
\left(
1+
\frac1{
(p-1)^3
}
\right).
}
$$

Then：

## Theorem 8.1

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
\mathfrak S_q(
0,h,d,h+d
)
=
A(q).
}
$$

Also：

$$
\boxed{
\frac1q
\sum_{h\bmod q}
\mathfrak S_q(0,h)^2
=
A(q).
}
$$

---

# 9. Lower-order subset means

For every pair subset of the parallelogram：

$$
\boxed{
\mathbb E_{h,d\bmod q}
\mathfrak S_q(\text{pair})
=
1.
}
$$

For every triple subset：

$$
\boxed{
\mathbb E_{h,d\bmod q}
\mathfrak S_q(\text{triple})
=
1.
}
$$

Singleton and empty singular series equal one。

---

# 10. Refined four-point mean

By inclusion–exclusion：

$$
\begin{aligned}
\mathfrak S_{0,q}^{(4)}
&=
\mathfrak S_q^{(4)}
-
\sum_{\text{4 triples}}
\mathfrak S_q^{(3)}
\\
&\quad
+
\sum_{\text{6 pairs}}
\mathfrak S_q^{(2)}
-
4+1.
\end{aligned}
$$

Taking the full $(h,d)\bmod q$ mean and using Sections 8–9：

$$
\boxed{
\mathbb E_q
\mathfrak S_{0,q}(
0,h,d,h+d
)
=
A(q)-1.
}
$$

---

# 11. Pair-centered square mean

Define：

$$
\boxed{
\mu_{q}(h)
=
\mathfrak S_q(0,h)-1.
}
$$

Then：

$$
\begin{aligned}
\mathbb E_q
\mu_q(h)^2
&=
\mathbb E_q
\mathfrak S_q(0,h)^2
\\
&\quad
-
2
\mathbb E_q
\mathfrak S_q(0,h)
+
1.
\end{aligned}
$$

Using Sections 3 and 8：

$$
\boxed{
\mathbb E_q
\mu_q(h)^2
=
A(q)-1.
}
$$

---

# 12. Exact finite-modulus parallelogram centering

Define：

$$
\boxed{
\mathfrak K_{4,q}(h,d)
=
\mathfrak S_{0,q}(
0,h,d,h+d
)
-
\mu_q(h)^2.
}
$$

Sections 10–11 give：

## Theorem 12.1 · Parallelogram Local Centering Theorem

For every squarefree：

$$
q,
$$

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
\mathfrak K_{4,q}(h,d)
=
0.
}
$$

No limit is taken。

No Hardy–Littlewood conjecture is used。

This is an exact finite Euler-product identity。

---

# 13. Zero Fourier mode

Define normalized two-dimensional Fourier coefficients：

$$
\boxed{
\widehat{
\mathfrak K
}_{4,q}(a,b)
=
\frac1{q^2}
\sum_{h,d\bmod q}
\mathfrak K_{4,q}(h,d)
e\left(
-\frac{
ah+bd
}{q}
\right).
}
$$

Then Theorem 12.1 is exactly：

## Corollary 13.1

$$
\boxed{
\widehat{
\mathfrak K
}_{4,q}(0,0)
=
0.
}
$$

Therefore：

$$
\boxed{
\mathfrak K_{4,q}(h,d)
=
\sum_{
(a,b)\ne(0,0)
}
\widehat{
\mathfrak K
}_{4,q}(a,b)
e\left(
\frac{
ah+bd
}{q}
\right).
}
$$

The deterministic finite-conductor model consists entirely of nonzero arithmetic frequencies。

---

# 14. v3.6 Cesàro parallelogram weight

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

for：

$$
h,d\ge1,
\qquad
h+d\le2N-2.
$$

Outside this triangular region set：

$$
\Omega_N=0.
$$

---

# 15. Weight size

Since：

$$
0\le w_N\le N,
$$

and the inner sum has at most：

$$
2N
$$

terms：

$$
\boxed{
\|\Omega_N\|_\infty
\ll
N^3.
}
$$

---

# 16. Discrete Lipschitz bound

The endpoint weight：

$$
w_N(n)
$$

changes by at most one per unit step。

Changing：

$$
h
$$

or：

$$
d
$$

by one：

- shifts at most two $w_N$ arguments by one；
- changes one boundary term of size at most $N^2$。

Therefore：

## Lemma 16.1

$$
\boxed{
|\Delta_h\Omega_N|
+
|\Delta_d\Omega_N|
\ll
N^2.
}
$$

The bound is uniform on the support。

---

# 17. Periodic mean-zero discrepancy lemma

Let：

$$
F:\mathbb Z^2\to\mathbb C
$$

be $q$-periodic in each coordinate and satisfy：

$$
\sum_{a,b\bmod q}F(a,b)=0.
$$

Assume：

$$
\|F\|_\infty\le B.
$$

Partition the support of：

$$
\Omega_N
$$

into：

$$
q\times q
$$

residue blocks。

On a complete block, subtract a constant value of：

$$
\Omega_N.
$$

The constant term cancels by the zero-mean condition。

Using Lemma 16.1, variation of：

$$
\Omega_N
$$

inside one block is：

$$
O(qN^2).
$$

Summing complete blocks and boundary blocks gives：

## Theorem 17.1 · Two-dimensional Cesàro discrepancy

For：

$$
q\le N,
$$

$$
\boxed{
\left|
\sum_{h,d}
\Omega_N(h,d)F(h,d)
\right|
\ll
BqN^4.
}
$$

For：

$$
q>N,
$$

the trivial estimate is：

$$
O(BN^5).
$$

---

# 18. Diagonal exclusion

The genuine four-distinct model excludes：

$$
h=d.
$$

There are only：

$$
O(N)
$$

such points。

Their total contribution is：

$$
O(
BN^4
).
$$

Therefore Theorem 17.1 remains valid, with the same asymptotic scale, after imposing：

$$
h\ne d.
$$

---

# 19. Sup norm of finite singular-series covariance

Let：

$$
R(q)
=
\frac q{\phi(q)}.
$$

For a $k$-tuple with：

$$
k\le4,
$$

every local factor satisfies：

$$
\mathfrak S_q(\mathcal D)
\le
R(q)^{k-1}.
$$

Hence：

$$
|\mathfrak S_{0,q}^{(4)}|
\ll
R(q)^3.
$$

Also：

$$
|\mu_q(h)|^2
\ll
R(q)^2.
$$

Thus：

## Lemma 19.1

$$
\boxed{
\|
\mathfrak K_{4,q}
\|_\infty
\ll
\left(
\frac q{\phi(q)}
\right)^3.
}
$$

---

# 20. Finite-conductor weighted model theorem

Apply Theorem 17.1 and Lemma 19.1：

## Theorem 20.1

For squarefree：

$$
q\le N,
$$

$$
\boxed{
\left|
\sum_{
\substack{
h,d\ge1\\
h+d\le2N-2\\
h\ne d
}
}
\Omega_N(h,d)
\mathfrak K_{4,q}(h,d)
\right|
\ll
N^4q
\left(
\frac q{\phi(q)}
\right)^3.
}
$$

So every finite arithmetic conductor receives a full one-power geometric saving from the vanished zero mode。

---

# 21. Primorial truncation

Let：

$$
\boxed{
q_y
=
\prod_{p\le y}p.
}
$$

By the prime number theorem：

$$
\boxed{
\log q_y
=
(1+o(1))y.
}
$$

By Mertens：

$$
\boxed{
\frac{
q_y
}{
\phi(q_y)
}
\ll
\log y.
}
$$

Therefore：

$$
\boxed{
\mathfrak M_{4,N}^{(\le y)}
\ll
N^4
e^{(1+o(1))y}
(\log y)^3.
}
$$

---

# 22. Truncated fixed-power saving

Choose：

$$
\boxed{
y
=
\theta\log N,
\qquad
0<\theta<1.
}
$$

Then：

$$
q_y
=
N^{\theta+o(1)}.
$$

Theorem 20.1 gives：

$$
\boxed{
\mathfrak M_{4,N}^{(\le y)}
\ll
N^{4+\theta+o(1)}.
}
$$

Relative to the trivial：

$$
N^5
$$

scale：

$$
\boxed{
\eta_{\rm trunc}
=
1-\theta.
}
$$

This is a real power saving for the finite-prime local-congruence model。

It is **not** yet a bound for the full singular series。

---

# 23. High-conductor tail

Define：

$$
\boxed{
\mathfrak T_{4,N}(y)
=
\mathfrak M_{4,N}
-
\mathfrak M_{4,N}^{(\le y)}.
}
$$

Then：

$$
\boxed{
\mathfrak M_{4,N}
=
\mathfrak M_{4,N}^{(\le y)}
+
\mathfrak T_{4,N}(y).
}
$$

v3.7 does not prove a fixed-power upper bound for：

$$
\mathfrak T_{4,N}(y).
$$

This is now the deterministic model bottleneck。

---

# 24. Why crude Euler-product truncation is insufficient

If one only controls the omitted primes by a generic small Euler-product error such as：

$$
O(1/y)
$$

on average，then with：

$$
y\asymp\log N
$$

the resulting weighted error can still be：

$$
\frac{N^5}{\log N}.
$$

This has no fixed：

$$
N^{-\eta}
$$

saving。

Therefore：

$$
\boxed{
\text{finite-conductor zero-mode cancellation}
}
$$

must be combined with a nontrivial high-conductor / Ramanujan-frequency argument。

Simple product truncation is not enough。

---

# 25. Two-dimensional Ramanujan viewpoint

Montgomery–Soundararajan express refined singular series through rational phases。

For the parallelogram offsets：

$$
0,h,d,h+d,
$$

the phase separates into：

$$
\boxed{
h\alpha+d\beta,
}
$$

where：

$$
\alpha,
\beta
$$

are rational combinations of the denominator variables in the refined singular-series expansion。

Theorem 12.1 says the：

$$
(\alpha,\beta)=(0,0)
$$

mode cancels exactly after pair covariance centering。

Thus the full deterministic problem becomes：

$$
\boxed{
\text{sum all nonzero rational frequencies with conductor-dependent coefficients}.
}
$$

This is the correct high-conductor formulation。

---

# 26. Connection to Montgomery–Soundararajan

Montgomery–Soundararajan introduced：

$$
\mathfrak S_0
$$

to study centered prime moments and proved that even-order unrestricted averages are governed by pairings。

Their proofs use rational-frequency expansions and delicate estimates for adding fractions。

v3.7 identifies an additional constrained phenomenon：

> for the two-parameter parallelogram family, the particular pair covariance subtraction removes the complete finite-modulus zero frequency exactly。

This does not follow automatically from the unrestricted $R_4(H)$ asymptotic and must be handled at the constrained-family level。

---

# 27. Connection to Kuperberg constrained sums

Kuperberg's 2025 work studies singular-series sums with congruence restrictions and smooth weights, showing that constrained averages are governed by residue incidences and pairings rather than by the unrestricted Gallagher average alone.

This supports the v3.7 methodological conclusion：

$$
\boxed{
\text{parallelogram constraints require their own local-frequency audit}.
}
$$

The current v3.7 exact local theorem is compatible with that broader framework but is not claimed to be contained verbatim in the cited paper。

---

# 28. Finite-product numerical diagnostics

Reference finite Euler products verify：

$$
\frac1{q^2}
\sum_{h,d\bmod q}
\mathfrak K_{4,q}(h,d)
=
0
$$

for several squarefree：

$$
q.
$$

The package also evaluates truncated weighted parallelogram sums at moderate：

$$
N,q
$$

to confirm：

- the zero mode is absent；
- weighted residual survives only through nonconstant residue structure。

These are normalization checks only。

---

# 29. Large-$N$ actual-prime scale diagnostic

Independent FFT diagnostics of the **actual prime residual variance**：

$$
\mathcal V_N
$$

up to：

$$
N=2\times10^5
$$

show a finite effective exponent around：

$$
4.6.
$$

This is compatible with a genuine power saving but proves nothing asymptotic。

It is not used in Theorem 20.1 and should not be confused with the deterministic singular-series model。

---

# 30. New deterministic model gate

For：

$$
0<\eta<1,
$$

a sufficient deterministic theorem is：

## Parallelogram High-Conductor Tail Gate $\operatorname{PHCT}(\eta)$

Find：

$$
0<\theta<1
$$

such that：

$$
\boxed{
|\mathfrak T_{4,N}(\theta\log N)|
\ll
N^{5-\eta+o(1)}.
}
$$

Then Theorem 22 gives：

$$
\boxed{
|\mathfrak M_{4,N}|
\ll
N^{
\max(
4+\theta,
5-\eta
)
+o(1)
}.
}
$$

Equivalently the deterministic-model saving is at least：

$$
\boxed{
\eta_M
\ge
\min(
1-\theta,
\eta
).
}
$$

The zero-mode part is already solved。

Only the high-conductor tail remains。

---

# 31. Stronger conductor-summed target

Rather than truncating one giant primorial, the preferred next route is a direct rational-frequency expansion：

$$
\boxed{
\mathfrak K_4(h,d)
=
\sum_{
(\alpha,\beta)\in\mathbb Q^2
\setminus\{(0,0)\}
}
c(\alpha,\beta)
e(h\alpha+d\beta).
}
$$

Then one seeks a conductor-weighted estimate：

$$
\boxed{
\sum_{
(\alpha,\beta)\ne(0,0)
}
|c(\alpha,\beta)|
\,
\left|
\widehat\Omega_N(
\alpha,\beta
)
\right|
\ll
N^{5-\eta}.
}
$$

This can exploit coefficient decay together with oscillation, instead of paying the full primorial modulus：

$$
q_y.
$$

That is the recommended high-conductor attack。

---

# 32. False-progress gates

Reject：

### F1 · Generic $R_4(H)$ applied directly

The parallelogram family has only two free difference variables and a linear relation。

### F2 · Wick pairings used as pointwise identity

Pair partitions govern averages, not each fixed：

$$
(h,d).
$$

### F3 · Finite-modulus theorem promoted to full singular series

High-conductor tail is still open。

### F4 · $1/\log N$ tail promoted as fixed power saving

Not sufficient。

### F5 · Actual-prime finite exponent used as deterministic proof

Different object。

### F6 · Zero-mode cancellation interpreted as RH progress

It is a deterministic singular-series model result only。

---

# 33. Autonomous progress state

The deterministic four-point model is now classified：

```text
constant / zero-frequency obstruction
    CLOSED

finite arithmetic conductors
    POWER-SAVED

high-conductor nonzero rational frequencies
    OPEN

actual prime deviation from full four-point model
    OPEN
```

So two independent hard objects remain：

$$
\boxed{
\text{MODEL TAIL}
}
$$

and：

$$
\boxed{
\text{PRIME DEVIATION}.
}
$$

This is much sharper than the v3.6 single object：

$$
\mathfrak Q_N.
$$

---

# 34. Suggested v3.8 direction

Recommended：

`RH-Parallelogram-RamanujanTail v3.8`

Tasks：

1. start from the Montgomery–Soundararajan rational-frequency expansion for：
   $$
   \mathfrak S_0;
   $$
2. specialize the phase to：
   $$
   h\alpha+d\beta;
   $$
3. subtract the pair-square expansion at coefficient level；
4. prove directly that：
   $$
   c(0,0)=0;
   $$
5. classify nonzero frequencies by joint conductor；
6. derive sharp bounds for：
   $$
   \widehat\Omega_N(\alpha,\beta);
   $$
7. sum conductor ranges dyadically；
8. determine whether the deterministic model alone satisfies：
   $$
   N^{4+o(1)}
   $$
   or at least：
   $$
   N^{5-\eta};
   $$
9. only after this is closed return to actual prime deviation：
   $$
   \mathfrak E_{4,N}.
   $$

This is now the canonical deterministic arithmetic continuation。

---

# 35. GAP ledger

## CLOSED / REDUCED

### G1. Local pair first moment

```text
CLOSED
```

### G2. Local pair second moment

```text
CLOSED
```

### G3. Local parallelogram raw four mean

```text
CLOSED
```

### G4. Finite-modulus refined covariance mean

```text
ZERO EXACTLY
```

### G5. Zero two-dimensional Fourier mode

```text
CLOSED
```

### G6. Finite-conductor weighted discrepancy

```text
CLOSED
```

### G7. Primorial truncated power saving

```text
CLOSED_AS_REDUCTION
```

---

## OPEN

### G8. High-conductor tail

```text
OPEN
```

### G9. Full deterministic model fixed saving

```text
OPEN
```

### G10. Actual prime four-point deviation

```text
OPEN
```

### G11. Any：

$$
\eta_Q>0
$$

for the complete prime covariance

```text
OPEN
```

### G12. RH

```text
OPEN
```

---

# 36. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FINITE-MODULUS ZERO-MEAN THEOREM = EXACT
FINITE-CONDUCTOR DISCREPANCY = EXACT UP TO STATED BIG-O

FULL SINGULAR-SERIES TAIL = NOT CONTROLLED AT FIXED POWER

NO FULL MODEL ETA > 0 PROVED
NO PRIME ETA > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\widehat{\mathfrak K}_{4,q}(0,0)=0
\Longrightarrow
\mathfrak M_{4,N}=O(N^4).
$$

Forbidden：

$$
\text{truncated }\eta>0
\Longrightarrow
\text{full }\eta>0.
$$

Forbidden：

$$
\text{finite conductor}
\Longrightarrow
\text{finite global arithmetic complexity}.
$$

---

# 37. One-line status

> v3.7 isolates the deterministic parallelogram singular-series obstruction and proves that its zero Fourier mode vanishes exactly at every finite arithmetic conductor. For a prime $p$, the local mean of the raw parallelogram four-tuple factor $\mathfrak S_p(0,h,d,h+d)$ equals $1+1/(p-1)^3$, which is exactly the second moment of the pair factor $\mathfrak S_p(0,h)$. All pair and generic triple subset factors have local mean one. CRT therefore gives, for every squarefree modulus $q$, equality between the finite-modulus raw four mean and the pair second moment; after refined inclusion–exclusion and subtraction of $(\mathfrak S_q(h)-1)^2$, the two-dimensional mean of $\mathfrak K_{4,q}$ is exactly zero. Hence its Fourier coefficient at $(0,0)$ vanishes. The v3.6 Cesàro parallelogram weight has size $O(N^3)$ and discrete gradient $O(N^2)$, so a block-discrepancy argument yields an $O(N^4 q(q/\phi(q))^3)$ bound for every finite modulus $q\le N$. Primorial truncation at $y=\theta\log N$ therefore has the genuine saving $N^{4+\theta+o(1)}$. What remains is not a constant $N^5$ local-congruence main term, but the high-conductor nonzero rational-frequency tail. Crude Euler-product truncation cannot turn this into a fixed power saving. The next node should therefore use the Montgomery–Soundararajan rational-frequency expansion directly, keep the exact zero-mode cancellation at coefficient level, and sum all nonzero conductors without paying a full primorial modulus.

---

# 38. References

1. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.  
   arXiv: https://arxiv.org/abs/math/0409258

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   arXiv: https://arxiv.org/abs/2301.06095

3. Thomas F. Bloom, Vivian Kuperberg, **Odd moments and adding fractions**, *Proceedings of the London Mathematical Society* (2025).  
   DOI: https://doi.org/10.1112/plms.70068

4. AMRAL, **RH-CenteredShift-FourierGap v3.6**.

---

# 39. Provenance

研究主導：Neo.K

v3.7 local parallelogram count、finite-modulus zero-mean theorem、two-dimensional zero-mode cancellation、Cesàro discrepancy bound、high-conductor gap classification、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 deterministic refined-singular-series / parallelogram conductor 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
