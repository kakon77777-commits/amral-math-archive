工程紀錄 · 第五弧線 v3.13 · 2026-09-03 · CONSTRAINT_ADAPTED_PAIRING · AXIS_UNIFORM_SOBOLEV · MIXED_SUBPOWER_SOBOLEV · RH_CLAIM_FALSE

# Parallelogram Constraint-Adapted Pairing：1D Axis、2D Axis-Free Remainder 與 Mixed Sobolev Gate

**RH-Parallelogram-ConstraintAdaptedPairing v3.13**

本節點承接：

- `RH-ModulatedPairingUniformity v3.12`
- `RH-Parallelogram-SobolevConductor v3.9`
- `RH-Parallelogram-SobolevTailTransfer v3.10`

v3.12 證明標準 ambient Wick decomposition不適合直接搬到 parallelogram constraint。

正確 finite-conductor decomposition是：

$$
\boxed{
\mathfrak K_{4,q}(h,d)
=
\mathfrak A_q(d)
+
\mathfrak K_{4,q}^{\perp}(h,d),
}
$$

where：

$$
\boxed{
\mathfrak A_q(d)
=
\mu_q(d)^2
-
[A(q)-1],
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

The axis-free remainder satisfies：

$$
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,0)=0,
$$

and：

$$
\widehat{
\mathfrak K_{4,q}^{\perp}
}(0,\beta)=0.
$$

v3.13 analyzes these two pieces separately。

Main results：

---

## Result A · 1D axis uniform Sobolev

The axis Fourier coefficient is exactly the：

$$
\alpha=0
$$

slice of the v3.9 covariance spectrum。

Therefore：

$$
\boxed{
\sup_{
q\ {\rm squarefree}
}
\sum_{\beta\ne0}
\frac{
|
\widehat{\mathfrak A_q}(\beta)
|^2
}{
|1-e(\beta)|^2
}
<
\infty.
}
$$

Thus the finite-conductor pair-square axis has a uniformly bounded one-dimensional antiderivative。

---

## Result B · Mixed Sobolev is subpower

Define：

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
=
\sum_{\substack{
\alpha\ne0\\
\beta\ne0
}}
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

Then for every：

$$
\varepsilon>0,
$$

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
\ll_\varepsilon
q^\varepsilon.
}
$$

No fixed conductor power appears。

The proof uses a local CRT majorant for the four-point coefficient and groups the two rational frequencies by their reduced denominators。

---

## Result C · Uniform mixed Sobolev is not claimed

Finite reference values：

$$
q=6,30,210,2310
$$

give approximately：

$$
0.19,\quad
4.09,\quad
12.26,\quad
21.18.
$$

These values do not establish divergence, but they warn against promoting：

$$
\sup_q
\mathfrak H_{hd}^{\perp}(q)<\infty
$$

without proof。

The rigorous result is only：

$$
q^{o(1)}.
$$

---

## Result D · Finite-conductor weighted scale

For：

$$
q\le N,
$$

the axis piece contributes：

$$
\boxed{
O(N^4).
}
$$

The exact sharp Cesàro-weight axis-free piece satisfies：

$$
\boxed{
O_\varepsilon(
N^{4+\varepsilon}
).
}
$$

For smooth interior parallelogram weights whose mixed discrete derivative has：

$$
\ell^2
$$

size：

$$
O(N^2),
$$

the axis-free contribution improves to：

$$
\boxed{
O_\varepsilon(
N^{3+\varepsilon}
).
}
$$

The difference comes from hard boundary layers of the exact Cesàro support。

---

Thus the deterministic parallelogram model is now structurally separated into：

```text
1D CENTERED PAIR-SQUARE AXIS
+
2D AXIS-FREE MIXED-SOBOLEV REMAINDER.
```

The two pieces should not be attacked by the same theorem。

No RH claim is made。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

CONSTRAINT_ADAPTED_DECOMPOSITION = CLOSED_FROM_V3_12

AXIS_SOBOLEV_UNIFORM = CLOSED
MIXED_SOBOLEV_Q_EPSILON = CLOSED

MIXED_SOBOLEV_UNIFORM = NOT_PROVED

FINITE_Q_AXIS_WEIGHTED = O(N^4)
FINITE_Q_AXIS_FREE_SHARP_WEIGHT = O_epsilon(N^(4+epsilon))
FINITE_Q_AXIS_FREE_SMOOTH_INTERIOR = O_epsilon(N^(3+epsilon))

FULL_AXIS_RAMANUJAN_TAIL = OPEN
FULL_AXIS_FREE_FINITE_BOX_TAIL = OPEN

FULL_DETERMINISTIC_ETA_M_POSITIVE = NOT_PROVED
ACTUAL_PRIME_DEVIATION = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Finite rational coefficient

Let：

$$
G_q
=
\mathbb Z/q\mathbb Z.
$$

For squarefree：

$$
q,
$$

define：

$$
\rho_q(t)
=
\begin{cases}
\mu(r(t))/\phi(r(t)),
&
t\ne0,
\\
0,
&
t=0,
\end{cases}
$$

where：

$$
r(t)
=
\frac q{\gcd(t,q)}.
$$

For：

$$
\alpha,\beta\in G_q,
$$

the four-point coefficient is：

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

For：

$$
\alpha\ne0,
\qquad
\beta\ne0,
$$

the double-centered coefficient is simply：

$$
\boxed{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,\beta)
=
C_q(\alpha,\beta).
}
$$

---

# 2. The axis component

Let：

$$
a_q(t)
=
\rho_q(t)^2.
$$

The pair mean：

$$
\mu_q(d)
$$

has Fourier coefficients：

$$
a_q(t).
$$

Hence：

$$
\mu_q(d)^2
$$

has Fourier coefficients：

$$
\boxed{
(a_q\ast a_q)(\beta).
}
$$

After subtracting its mean：

$$
A(q)-1,
$$

the axis coefficient is：

$$
\boxed{
\widehat{\mathfrak A_q}(\beta)
=
(a_q\ast a_q)(\beta),
\qquad
\beta\ne0.
}
$$

---

# 3. Axis is a slice of v3.9

v3.8 identified：

$$
\boxed{
\widehat{\mathfrak K}_{4,q}(0,\beta)
=
\widehat{\mathfrak A_q}(\beta)
}
$$

for：

$$
\beta\ne0.
$$

Therefore：

$$
\begin{aligned}
\sum_{\beta\ne0}
\frac{
|
\widehat{\mathfrak A_q}(\beta)
|^2
}{
|1-e(\beta)|^2
}
&\le
\sum_{\alpha,\beta\ne0\ {\rm or}\ \alpha=0}
\frac{
|
\widehat{\mathfrak K}_{4,q}(\alpha,\beta)
|^2
}{
|1-e(\beta)|^2
}.
\end{aligned}
$$

The right side is bounded uniformly by v3.9。

Thus：

## Theorem 3.1 · Uniform Axis Sobolev

$$
\boxed{
\sup_q
\mathfrak H_{\rm axis}(q)
<
\infty,
}
$$

where：

$$
\boxed{
\mathfrak H_{\rm axis}(q)
=
\sum_{\beta\ne0}
\frac{
|
\widehat{\mathfrak A_q}(\beta)
|^2
}{
|1-e(\beta)|^2
}.
}
$$

---

# 4. Axis antiderivative

Define：

$$
\boxed{
\widehat{\mathfrak B_q}(\beta)
=
\frac{
\widehat{\mathfrak A_q}(\beta)
}{
e(\beta)-1
},
\qquad
\beta\ne0,
}
$$

and：

$$
\widehat{\mathfrak B_q}(0)=0.
$$

Then：

$$
\boxed{
\Delta_d
\mathfrak B_q
=
\mathfrak A_q.
}
$$

Parseval gives：

$$
\boxed{
\frac1q
\sum_{d\bmod q}
|
\mathfrak B_q(d)
|^2
=
\mathfrak H_{\rm axis}(q)
\ll1.
}
$$

---

# 5. Mixed antiderivative candidate

For the axis-free remainder define：

$$
\boxed{
\widehat{
\mathfrak G_q^{(2)}
}(\alpha,\beta)
=
\frac{
\widehat{
\mathfrak K_{4,q}^{\perp}
}(\alpha,\beta)
}{
[e(\alpha)-1]
[e(\beta)-1]
}
}
$$

for：

$$
\alpha\ne0,
\qquad
\beta\ne0.
$$

Both axes are zero, so no singular zero-frequency coefficient is present。

Then：

$$
\boxed{
\Delta_h
\Delta_d
\mathfrak G_q^{(2)}
=
\mathfrak K_{4,q}^{\perp}.
}
$$

---

# 6. Extended multiplicative majorant

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

Then：

$$
|\rho_q(t)|
\le
|F_q(t)|.
$$

Under CRT：

$$
|F_q(t)|
$$

factors prime-by-prime。

For one prime：

$$
p,
$$

set：

$$
f_p(x)
=
\begin{cases}
1,
&
x=0,
\\
(p-1)^{-1},
&
x\ne0.
\end{cases}
$$

---

# 7. Local four-point majorant

Define：

$$
\boxed{
U_p(a,b)
=
\sum_{t\bmod p}
f_p(t)
f_p(a-t)
f_p(b-t)
f_p(t-a-b).
}
$$

If：

$$
a=b=0,
$$

then：

$$
\boxed{
U_p(0,0)
=
1+(p-1)^{-3}.
}
$$

If：

$$
(a,b)\ne(0,0),
$$

at most four values of：

$$
t
$$

are exceptional。

Every exceptional product is at most：

$$
(p-1)^{-2},
$$

while every generic product is：

$$
(p-1)^{-4}.
$$

Therefore：

## Lemma 7.1

$$
\boxed{
U_p(a,b)
\le
\frac6{(p-1)^2}
}
$$

for：

$$
(a,b)\ne(0,0).
$$

---

# 8. Denominator majorant

Let：

$$
r=r(\alpha),
\qquad
s=r(\beta),
$$

and：

$$
\ell=\operatorname{lcm}(r,s).
$$

For：

$$
p\nmid\ell,
$$

the local frequency pair is：

$$
(0,0).
$$

For：

$$
p\mid\ell,
$$

at least one local coordinate is nonzero。

The finite product of：

$$
1+(p-1)^{-3}
$$

is uniformly bounded over all primes。

Hence：

## Theorem 8.1 · Four-Point Denominator Bound

There exists an absolute：

$$
C_0
$$

such that：

$$
\boxed{
|
C_q(\alpha,\beta)
|^2
\le
C_0
\frac{
36^{\omega(\ell)}
}{
\phi(\ell)^4
}.
}
$$

---

# 9. Two coprime sine sums

For squarefree：

$$
r,
$$

v3.9 used：

$$
\boxed{
\sum_{\substack{
1\le a<r\\
\gcd(a,r)=1
}}
\frac1{
|1-e(a/r)|^2
}
=
\frac{
J_2(r)
}{12}
\le
\frac{r^2}{12}.
}
$$

Apply this independently to：

$$
r
$$

and：

$$
s.
$$

---

# 10. Mixed Sobolev divisor sum

Theorem 8.1 and Section 9 give：

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
\ll
\sum_{r,s\mid q}
36^{\omega(\operatorname{lcm}(r,s))}
\frac{
r^2s^2
}{
\phi(\operatorname{lcm}(r,s))^4
}.
}
$$

Because：

$$
q
$$

is squarefree, the divisor sum factors over primes。

---

# 11. Local divisor factor

For one prime：

$$
p\mid q,
$$

there are four possibilities：

### In neither $r$ nor $s$

factor：

$$
1.
$$

### In exactly one

each factor is：

$$
\boxed{
36
\frac{
p^2
}{
(p-1)^4
}.
}
$$

There are two such choices。

### In both

factor：

$$
\boxed{
36
\frac{
p^4
}{
(p-1)^4
}.
}
$$

Thus：

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
\ll
\prod_{p\mid q}
\left[
1+
72\frac{p^2}{(p-1)^4}
+
36\frac{p^4}{(p-1)^4}
\right].
}
$$

---

# 12. Subpower conductor growth

The local factor in Section 11 is bounded by an absolute constant：

$$
C_1.
$$

Therefore：

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
\ll
C_1^{\omega(q)}.
}
$$

The standard maximal-order estimate：

$$
\omega(q)
=
O\left(
\frac{\log q}{\log\log q}
\right)
$$

gives：

$$
\boxed{
C_1^{\omega(q)}
=
q^{o(1)}.
}
$$

Thus：

## Theorem 12.1 · Mixed Sobolev Subpower Bound

For every：

$$
\varepsilon>0,
$$

$$
\boxed{
\mathfrak H_{hd}^{\perp}(q)
\ll_\varepsilon
q^\varepsilon.
}
$$

---

# 13. What Theorem 12.1 does not say

The proof does not give：

$$
\sup_q
\mathfrak H_{hd}^{\perp}(q)<\infty.
$$

The finite numerical values increase over the tested primorial conductors。

This may reflect：

- genuine slow growth；
- looseness in the tested conductor sequence；
- or eventual stabilization。

No conclusion is made。

The canonical theorem is only：

$$
q^{o(1)}.
$$

---

# 14. Mixed antiderivative $B^2$ norm

Parseval gives：

$$
\boxed{
\frac1{q^2}
\sum_{h,d\bmod q}
|
\mathfrak G_q^{(2)}(h,d)
|^2
=
\mathfrak H_{hd}^{\perp}(q).
}
$$

Hence for every：

$$
\varepsilon>0,
$$

$$
\boxed{
\|
\mathfrak G_q^{(2)}
\|_{B^2(q)}
\ll_\varepsilon
q^{\varepsilon}.
}
$$

Here the exponent can absorb the square root by replacing：

$$
\varepsilon
$$

with：

$$
2\varepsilon.
$$

---

# 15. Exact Cesàro parallelogram weight

Recall：

$$
\boxed{
\Omega_N(h,d)
=
\sum_{
r=1
}^{2N-1-h-d}
w_N(r+h)
w_N(r+h+d).
}
$$

It is supported on：

$$
h,d\ge1,
\qquad
h+d\le2N-2.
$$

The raw scale is：

$$
\Omega_N
=
O(N^3).
$$

---

# 16. Axis-collapsed weight

Define：

$$
\boxed{
\Xi_N(d)
=
\sum_{h\ge1}
\Omega_N(h,d).
}
$$

Equivalently：

$$
\boxed{
\Xi_N(d)
=
\sum_{n=2}^{2N-1-d}
(n-1)
w_N(n)
w_N(n+d).
}
$$

Therefore：

$$
\boxed{
\|\Delta_d\Xi_N\|_\infty
\ll
N^3.
}
$$

Its support length is：

$$
O(N).
$$

Hence：

$$
\boxed{
\|\Delta_d\Xi_N\|_2
\ll
N^{7/2}.
}
$$

---

# 17. Finite-conductor axis weighted bound

For：

$$
q\le N,
$$

periodicity and Theorem 3.1 imply over a length：

$$
O(N)
$$

interval：

$$
\boxed{
\|\mathfrak B_q\|_2
\ll
N^{1/2}.
}
$$

Summation by parts：

$$
\sum_d
\Xi_N(d)
\mathfrak A_q(d)
=
-
\sum_d
\Delta_d^-\Xi_N(d)
\mathfrak B_q(d).
$$

Therefore：

## Theorem 17.1

$$
\boxed{
\left|
\sum_{h,d}
\Omega_N(h,d)
\mathfrak A_q(d)
\right|
\ll
N^4
}
$$

uniformly for：

$$
q\le N.
$$

---

# 18. Mixed difference of the exact weight

Extend：

$$
\Omega_N
$$

by zero to all：

$$
\mathbb Z^2.
$$

Define the backward mixed difference：

$$
\boxed{
\Delta_h^-
\Delta_d^-
\Omega_N(h,d).
}
$$

Inside the open triangular bulk：

$$
h,d\ge2,
\qquad
h+d\le2N-3,
$$

direct finite-difference calculation gives：

$$
\boxed{
|
\Delta_h^-
\Delta_d^-
\Omega_N
|
\ll
N.
}
$$

Since there are：

$$
O(N^2)
$$

interior points：

$$
\boxed{
\|
\Delta_h^-
\Delta_d^-
\Omega_N
\|_{2,\rm interior}
\ll
N^2.
}
$$

---

# 19. Hard boundary layers

Because the exact weight is cut off sharply at：

$$
h=1,
$$

$$
d=1,
$$

and the triangular outer boundary, zero extension creates boundary jumps。

The largest mixed jump is：

$$
O(N^3).
$$

There are only lower-dimensional boundary layers, but their：

$$
\ell^2
$$

contribution dominates the exact mixed derivative。

Thus：

$$
\boxed{
\|
\Delta_h^-
\Delta_d^-
\Omega_N
\|_2
\ll
N^3.
}
$$

This explains why the sharp geometry loses one power compared with a smooth interior weight。

---

# 20. Exact double summation by parts

Since：

$$
\Delta_h
\Delta_d
\mathfrak G_q^{(2)}
=
\mathfrak K_{4,q}^{\perp},
$$

compact support gives：

$$
\boxed{
\sum_{h,d}
\Omega_N(h,d)
\mathfrak K_{4,q}^{\perp}(h,d)
=
\sum_{h,d}
\Delta_h^-
\Delta_d^-
\Omega_N(h,d)
\mathfrak G_q^{(2)}(h,d).
}
$$

There are no unrecorded boundary terms because the zero extension is included in the discrete differences。

---

# 21. Box norm of the mixed antiderivative

For：

$$
q\le N,
$$

periodicity gives：

$$
\begin{aligned}
\sum_{
|h|,|d|\ll N
}
|
\mathfrak G_q^{(2)}(h,d)
|^2
&\ll_\varepsilon
N^2
q^\varepsilon.
\end{aligned}
$$

Hence：

$$
\boxed{
\|
\mathfrak G_q^{(2)}
\|_{L^2(\text{box})}
\ll_\varepsilon
N
q^\varepsilon.
}
$$

Again：

$$
\varepsilon
$$

absorbs harmless halves。

---

# 22. Sharp-weight finite-conductor bound

Combine Sections 19–21：

## Theorem 22.1

For：

$$
q\le N,
$$

$$
\boxed{
\left|
\sum
\Omega_N
\mathfrak K_{4,q}^{\perp}
\right|
\ll_\varepsilon
N^4
q^\varepsilon.
}
$$

Thus：

$$
\boxed{
\ll_\varepsilon
N^{4+\varepsilon}
}
$$

uniformly for squarefree：

$$
q\le N.
$$

---

# 23. Smooth interior gain

Let：

$$
W_N(h,d)
$$

be a smooth discrete parallelogram weight supported away from hard coordinate boundaries and satisfying：

$$
\boxed{
\|
\Delta_h^-
\Delta_d^-
W_N
\|_2
\ll
N^2.
}
$$

Then the same argument gives：

## Theorem 23.1

$$
\boxed{
\left|
\sum
W_N
\mathfrak K_{4,q}^{\perp}
\right|
\ll_\varepsilon
N^3
q^\varepsilon.
}
$$

For：

$$
q\le N,
$$

this is：

$$
\boxed{
N^{3+\varepsilon}.
}
$$

The improvement is geometric, not arithmetic。

---

# 24. Constraint-adapted scale picture

The finite-conductor deterministic covariance therefore has：

### Axis

$$
\boxed{
N^4
}
$$

natural sharp-weight scale。

### 2D axis-free interior

$$
\boxed{
N^{3+o(1)}
}
$$

under smooth two-direction geometry。

### Exact hard Cesàro weight

boundary layers restore：

$$
\boxed{
N^{4+o(1)}.
}
$$

So the axis and sharp boundaries are the first lower-dimensional structures to resolve before demanding a full two-dimensional restriction theorem。

---

# 25. Relation to the one-dimensional singular-series tail literature

The axis：

$$
\mathfrak A(d)
=
[\mathfrak S(d)-1]^2
-
\mathbb E[
(\mathfrak S-1)^2
]
$$

is a one-dimensional Ramanujan object built from the square of the prime-pair singular-series fluctuation。

Goldston–Hunts–Ngotiaoco prove quantitative finite-box mean-square decay for the ordinary prime-pair singular-series Ramanujan tail。

Their theorem does not directly apply to：

$$
\mathfrak A(d),
$$

because squaring convolves Ramanujan frequencies。

But the problem class is now one-dimensional and much closer to their method than the original parallelogram covariance。

---

# 26. Full-axis high-conductor gate

Define a Ramanujan truncation：

$$
\mathfrak A
=
\mathfrak A_{\le Q}
+
\widetilde{\mathfrak A}_{>Q}.
$$

A sufficient axis theorem is：

## Axis Pair-Square Tail $\operatorname{APST}(\delta)$

$$
\boxed{
\sum_{d\le N}
|
\widetilde{\mathfrak A}_{>Q}(d)
|^2
\ll_\varepsilon
N^{1+\varepsilon}
Q^{-2\delta}
}
$$

for some：

$$
\delta>0.
$$

With：

$$
Q=N^\theta,
$$

this produces a fixed-power finite-box axis approximation。

No APST theorem is proved here。

---

# 27. Full 2D high-conductor gate

For the axis-free remainder define finite-conductor approximants：

$$
\mathfrak K_{4,\le Q}^{\perp}.
$$

A natural two-dimensional tail theorem is：

## Mixed Sobolev Tail Transfer $\operatorname{MSTT}(\delta)$

$$
\boxed{
\sum_{
0\le h,d\le2N
}
|
\mathfrak G_{>Q}^{(2)}(h,d)
|^2
\ll_\varepsilon
N^{2+\varepsilon}
Q^{-2\delta}.
}
$$

Any：

$$
\delta>0
$$

would convert the subpower conductor Sobolev theorem into a fixed finite-box saving。

No MSTT theorem is proved here。

---

# 28. Why the two gates should remain separate

The axis term contains the strongest rational near-axis concentration。

The 2D remainder has：

$$
\alpha\ne0,
\qquad
\beta\ne0
$$

on every mode。

Therefore a single generic large-sieve theorem is likely inefficient。

The preferred architecture is：

```text
1D axis
    Ramanujan-tail / arithmetic progression technology

2D axis-free remainder
    mixed Sobolev + two-dimensional restriction
```

This is the central strategic conclusion of v3.13。

---

# 29. Numerical mixed Sobolev diagnostics

For primorial-like squarefree conductors：

$$
q=6,30,210,2310,
$$

reference values are approximately：

$$
\boxed{
0.1914,\quad
4.0852,\quad
12.2619,\quad
21.1815.
}
$$

The axis Sobolev values are smaller and remain covered by the uniform v3.9 theorem。

These data are not used to infer asymptotic growth。

---

# 30. Exact mixed-antiderivative validation

For finite：

$$
q,
$$

the package constructs：

$$
\mathfrak G_q^{(2)}
$$

spectrally and checks：

$$
\boxed{
\Delta_h
\Delta_d
\mathfrak G_q^{(2)}
=
\mathfrak K_{4,q}^{\perp}.
}
$$

It also verifies the exact sharp-weight double summation-by-parts identity。

The numerical residuals are floating-point normalization checks only。

---

# 31. Revised deterministic state

After v3.13：

```text
ambient Wick route
    REJECTED

constraint-adapted decomposition
    CLOSED

1D axis finite conductor
    UNIFORM SOBOLEV

2D axis-free finite conductor
    MIXED SOBOLEV q^(o(1))

sharp finite-q deterministic model
    N^(4+o(1))

smooth axis-free interior
    N^(3+o(1))

full 1D axis tail
    OPEN

full 2D finite-box tail
    OPEN
```

---

# 32. Suggested v3.14 direction

Recommended：

`RH-PairSquareAxis-RamanujanTail v3.14`

Attack the simpler one-dimensional piece first。

Tasks：

1. derive the exact Ramanujan coefficient of：
   $$
   \mu(d)^2;
   $$
2. identify its centered constant term；
3. express the high-denominator tail as a convolution of pair singular-series coefficients；
4. compare with Goldston–Hunts–Ngotiaoco's tail diagonalization；
5. seek：
   $$
   \operatorname{APST}(\delta);
   $$
6. determine whether the one-dimensional axis can be closed at：
   $$
   N^{4+o(1)}
   $$
   or better for the exact collapsed weight；
7. only then return to the genuinely two-dimensional：
   $$
   \mathfrak K_4^\perp.
   $$

This sequencing attacks the structurally simpler obstruction first。

---

# 33. GAP ledger

## CLOSED / REDUCED

### G1. Constraint-adapted decomposition

```text
CLOSED
```

### G2. Axis finite-$q$ Sobolev

```text
UNIFORM
```

### G3. Axis-free mixed finite-$q$ Sobolev

```text
q^(o(1))
```

### G4. Sharp finite-$q$ axis

```text
N^4
```

### G5. Sharp finite-$q$ axis-free

```text
N^(4+o(1))
```

### G6. Smooth interior axis-free

```text
N^(3+o(1))
```

---

## OPEN

### G7. APST$(\delta)$

```text
OPEN
```

### G8. MSTT$(\delta)$

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

# 34. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

AXIS UNIFORM SOBOLEV = EXACT CONSEQUENCE OF V3.9
MIXED q^epsilon SOBOLEV = ELEMENTARY FINITE-CONDUCTOR THEOREM

MIXED UNIFORM SOBOLEV = NOT CLAIMED

FINITE-Q N^4 BOUNDS
    !=
FULL INFINITE-CONDUCTOR N^4 BOUND

SMOOTH INTERIOR N^3
    !=
EXACT SHARP CESARO N^3

NO APST PROVED
NO MSTT PROVED

NO ETA_M > 0 PROVED
NO ETA_Q > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
q^{o(1)}
\Longrightarrow
O(1).
$$

Forbidden：

$$
\text{both spectral axes removed}
\Longrightarrow
\text{automatic uniform mixed Sobolev}.
$$

Forbidden：

$$
\text{finite-conductor double antiderivative}
\Longrightarrow
\text{full pointwise double antiderivative}.
$$

---

# 35. One-line status

> v3.13 replaces the failed ambient Wick strategy with a constraint-adapted two-piece decomposition. The deterministic covariance is written exactly as a centered one-dimensional pair-square axis $\mathfrak A_q(d)=\mu_q(d)^2-[A(q)-1]$ plus a symmetric axis-free remainder $\mathfrak K_{4,q}^{\perp}$. The axis Fourier spectrum is precisely the $\alpha=0$ slice of the v3.9 covariance spectrum, so its one-dimensional Sobolev norm is uniformly bounded over all squarefree finite conductors. The axis-free remainder has no $\alpha=0$ or $\beta=0$ modes. A local CRT majorant for its four-point coefficient, combined with the Jordan-$J_2$ reciprocal-sine identity in both rational coordinates, gives a mixed Sobolev bound $\mathfrak H_{hd}^{\perp}(q)\ll_\varepsilon q^\varepsilon$. The proof is subpower rather than uniform because primes dividing both rational denominators create a bounded local loss whose product is $C^{\omega(q)}$. This produces a finite-conductor two-direction antiderivative. Against the exact sharp Cesàro parallelogram weight, hard coordinate boundary layers keep the weighted scale at $N^{4+o(1)}$; for smooth interior weights the same mixed antiderivative yields $N^{3+o(1)}$. The one-dimensional axis and the genuinely two-dimensional remainder therefore have different analytic characters and should be separated permanently. The next canonical target is the one-dimensional centered pair-square Ramanujan tail, where existing prime-pair singular-series tail methods provide the closest external template.

---

# 36. References

1. D. A. Goldston, Julian Ziegler Hunts, Timothy Ngotiaoco, **The Tail of the Singular Series for the Prime Pair and Goldbach Problems**, *Functiones et Approximatio Commentarii Mathematici* 56 (2017), 117–141.  
   arXiv: https://arxiv.org/abs/1409.2151

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   arXiv: https://arxiv.org/abs/2301.06095

3. AMRAL, **RH-ModulatedPairingUniformity v3.12**.

4. AMRAL, **RH-Parallelogram-SobolevConductor v3.9**.

---

# 37. Provenance

研究主導：Neo.K

v3.13 axis/mixed decomposition、uniform 1D Sobolev inheritance、mixed $q^\varepsilon$ Sobolev theorem、finite-conductor weighted estimates、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 constraint-adapted pairing / axis-vs-2D decomposition 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
