工程紀錄 · 第五弧線 v3.14 · 2026-09-03 · PAIR_SQUARE_RAMANUJAN_EXPANSION · APST_CLOSED · AXIS_FIXED_POWER_CLOSED · RH_CLAIM_FALSE

# Pair-Square Axis Ramanujan Tail：Exact Coefficients、APST$(1)$ 與 $N^{17/4}$ Axis Closure

**RH-PairSquareAxis-RamanujanTail v3.14**

本節點承接：

- `RH-Parallelogram-ConstraintAdaptedPairing v3.13`
- Goldston–Hunts–Ngotiaoco prime-pair singular-series tail framework

v3.13 isolated the one-dimensional deterministic axis：

$$
\boxed{
\mathfrak A(d)
=
[\mathfrak S(d)-1]^2
-
\mathbb E[
(\mathfrak S-1)^2
].
}
$$

The v3.13 open gate was：

## APST$(\delta)$

Find：

$$
\delta>0
$$

such that the Ramanujan denominator tail：

$$
\widetilde{\mathfrak A}_{>Q}(d)
$$

satisfies：

$$
\sum_{d\le N}
|
\widetilde{\mathfrak A}_{>Q}(d)
|^2
\ll_\varepsilon
N^{1+\varepsilon}
Q^{-2\delta}.
$$

v3.14 closes this gate essentially at the natural exponent：

$$
\boxed{
\delta=1.
}
$$

More precisely：

$$
\boxed{
\sum_{d\le N}
|
\widetilde{\mathfrak A}_{>Q}(d)
|^2
\ll_\varepsilon
N^{1+\varepsilon}
Q^{-2+\varepsilon}.
}
$$

The proof begins by deriving the exact Ramanujan coefficients of the squared singular series。

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

PRIME_PAIR_RAMANUJAN_EXPANSION = CLASSICAL
SQUARE_LOCAL_RAMANUJAN_IDENTITY = CLOSED
PAIR_SQUARE_AXIS_COEFFICIENT = CLOSED

AXIS_COEFFICIENT_DECAY = q^(-2+epsilon)
APST_DELTA_1_MINUS_EPSILON = CLOSED

WEIGHTED_AXIS_LOW_DENOMINATOR = CLOSED
WEIGHTED_AXIS_HIGH_DENOMINATOR = CLOSED

OPTIMAL_SPLIT_Q = N^(3/4)
FULL_AXIS_WEIGHTED_EXPONENT = 17/4 + epsilon
AXIS_FIXED_SAVING_ETA = 3/4

FULL_1D_AXIS = CLOSED_AT_FIXED_POWER
AXIS_IS_MAIN_DETERMINISTIC_BARRIER = FALSE

2D_AXIS_FREE_MSTT = OPEN
FULL_DETERMINISTIC_ETA_M_POSITIVE = NOT_PROVED
ACTUAL_PRIME_DEVIATION = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Classical prime-pair Ramanujan expansion

The Hardy–Littlewood prime-pair singular series has the classical Ramanujan expansion：

$$
\boxed{
\mathfrak S(d)
=
\sum_{q=1}^{\infty}
\frac{
\mu(q)^2
}{
\phi(q)^2
}
c_q(d).
}
$$

Because：

$$
\mu(q)^2
$$

restricts to squarefree：

$$
q,
$$

the series has Euler product：

$$
\boxed{
\mathfrak S(d)
=
\prod_p
\left[
1+
\frac{
c_p(d)
}{
(p-1)^2
}
\right].
}
$$

For fixed：

$$
d,
$$

this Euler product is absolutely convergent after the finitely many primes dividing $d$ are separated。

---

# 2. Prime Ramanujan square identity

For a prime：

$$
p,
$$

$$
c_p(d)
=
\begin{cases}
p-1,
&
p\mid d,
\\
-1,
&
p\nmid d.
\end{cases}
$$

Therefore：

## Lemma 2.1

$$
\boxed{
c_p(d)^2
=
(p-2)c_p(d)
+
(p-1).
}
$$

This identity is exact in both residue cases。

---

# 3. Square one Euler factor

Let：

$$
a_p
=
\frac1{(p-1)^2}.
$$

Then：

$$
\begin{aligned}
[
1+a_pc_p
]^2
&=
1
+
2a_pc_p
+
a_p^2c_p^2
\\
&=
C_p
\left[
1+g_pc_p
\right],
\end{aligned}
$$

where：

$$
\boxed{
C_p
=
1+
\frac1{(p-1)^3},
}
$$

and：

$$
\boxed{
g_p
=
\frac{
2p-3
}{
(p-1)
(
p^2-3p+3
)
}.
}
$$

---

# 4. Exact squared singular-series expansion

Define：

$$
\boxed{
\mathcal A_*
=
\prod_p
\left(
1+
\frac1{(p-1)^3}
\right).
}
$$

The product converges。

For squarefree：

$$
q,
$$

define：

$$
\boxed{
g(q)
=
\prod_{p\mid q}g_p,
}
$$

with：

$$
g(1)=1,
$$

and set：

$$
g(q)=0
$$

if：

$$
q
$$

is not squarefree。

Multiplying Section 3 prime-by-prime gives：

## Theorem 4.1

$$
\boxed{
\mathfrak S(d)^2
=
\mathcal A_*
\sum_{q=1}^{\infty}
g(q)c_q(d).
}
$$

The constant Ramanujan coefficient is：

$$
\mathcal A_*.
$$

This agrees with the classical mean-square constant occurring in weighted averages of：

$$
\mathfrak S(d)^2.
$$

---

# 5. Mean of the centered pair-square

Let：

$$
\mu(d)
=
\mathfrak S(d)-1.
$$

Then：

$$
\mu(d)^2
=
\mathfrak S(d)^2
-
2\mathfrak S(d)
+
1.
$$

The constant coefficient is：

$$
\boxed{
\mathcal A_*-1.
}
$$

Therefore：

$$
\boxed{
\mathbb E\mu^2
=
\mathcal A_*-1.
}
$$

This is the infinite-conductor form of the finite $A(q)-1$ from v3.12–v3.13。

---

# 6. Exact axis coefficients

Define：

$$
\boxed{
\mathfrak A(d)
=
\mu(d)^2
-
(
\mathcal A_*-1
).
}
$$

Then：

$$
\boxed{
\mathfrak A(d)
=
\sum_{q=2}^{\infty}
B_qc_q(d),
}
$$

where：

## Theorem 6.1

For squarefree：

$$
q>1,
$$

$$
\boxed{
B_q
=
\mathcal A_*g(q)
-
2
\frac1{\phi(q)^2},
}
$$

and：

$$
B_q=0
$$

for nonsquarefree $q$。

The $q=1$ coefficient is exactly zero by centering。

---

# 7. Coefficient decay

For every prime：

$$
p,
$$

one has：

$$
\boxed{
0<g_p
\le
\frac3{(p-1)^2}.
}
$$

Hence：

$$
\boxed{
g(q)
\le
\frac{
3^{\omega(q)}
}{
\phi(q)^2
}.
}
$$

Using the standard subpower estimates：

$$
3^{\omega(q)}
\ll_\varepsilon
q^\varepsilon,
$$

and：

$$
\frac1{\phi(q)}
\ll_\varepsilon
q^{-1+\varepsilon},
$$

we obtain：

## Theorem 7.1

For every：

$$
\varepsilon>0,
$$

$$
\boxed{
|B_q|
\ll_\varepsilon
q^{-2+\varepsilon}.
}
$$

---

# 8. Define the Ramanujan denominator tail

For：

$$
Q\ge1,
$$

define：

$$
\boxed{
\widetilde{\mathfrak A}_{>Q}(n)
=
\sum_{q>Q}
B_qc_q(n).
}
$$

This is a **Ramanujan denominator cutoff**。

It is different from the finite-Euler-prime conductor cutoff used in v3.7–v3.10。

---

# 9. Divisor identity for Ramanujan sums

Use the exact formula：

$$
\boxed{
c_q(n)
=
\sum_{d\mid(q,n)}
d\,
\mu(q/d).
}
$$

Since the axis coefficients are absolutely summable against：

$$
|c_q(n)|
$$

for fixed：

$$
n,
$$

the tail may be rearranged：

$$
\boxed{
\widetilde{\mathfrak A}_{>Q}(n)
=
\sum_{d\mid n}
d
\sum_{m>Q/d}
B_{dm}\mu(m).
}
$$

---

# 10. Pointwise axis-tail bound

Fix a small：

$$
\varepsilon>0.
$$

From Theorem 7.1：

$$
|B_{dm}|
\ll_\varepsilon
(dm)^{-2+\varepsilon}.
$$

Hence：

$$
\begin{aligned}
\sum_{m>Q/d}
|B_{dm}|
&\ll_\varepsilon
d^{-2+\varepsilon}
\sum_{m>Q/d}
m^{-2+\varepsilon}
\\
&\ll_\varepsilon
d^{-1}
Q^{-1+\varepsilon}.
\end{aligned}
$$

The estimate remains valid when：

$$
d>Q
$$

because then the full convergent $m$-sum is even smaller than the displayed right side。

Therefore：

## Theorem 10.1 · Pointwise Pair-Square Tail

$$
\boxed{
|
\widetilde{\mathfrak A}_{>Q}(n)
|
\ll_\varepsilon
\tau(n)
Q^{-1+\varepsilon}.
}
$$

---

# 11. APST closure

The classical divisor-square estimate：

$$
\boxed{
\sum_{n\le N}
\tau(n)^2
\ll
N(\log N)^3
}
$$

and Theorem 10.1 give：

$$
\boxed{
\sum_{n\le N}
|
\widetilde{\mathfrak A}_{>Q}(n)
|^2
\ll_\varepsilon
N^{1+\varepsilon}
Q^{-2+\varepsilon}.
}
$$

Thus：

## Theorem 11.1 · APST

The v3.13 axis gate holds at the natural tail power：

$$
\boxed{
\operatorname{APST}(1-o(1)).
}
$$

Equivalently, for every fixed：

$$
\delta<1,
$$

$$
\boxed{
\operatorname{APST}(\delta)
}
$$

holds。

---

# 12. Weighted mean-square version

Since：

$$
(N-n)^2\le N^2,
$$

Theorem 11.1 also gives：

$$
\boxed{
\sum_{n\le N}
(N-n)^2
|
\widetilde{\mathfrak A}_{>Q}(n)
|^2
\ll_\varepsilon
N^{3+\varepsilon}
Q^{-2+\varepsilon}.
}
$$

This has the same denominator exponent as the Goldston–Hunts–Ngotiaoco prime-pair tail theorem。

Their theorem is substantially sharper because it gives an asymptotic main constant for the ordinary singular-series tail。

v3.14 only needs the upper bound。

---

# 13. Axis antiderivative coefficients

For：

$$
q>1,
$$

define the frequency-level antiderivative coefficient：

$$
\boxed{
\frac{
B_q
}{
e(a/q)-1
},
\qquad
\gcd(a,q)=1.
}
$$

The exact identity：

$$
\boxed{
\sum_{\substack{
1\le a<q\\
\gcd(a,q)=1
}}
\frac1{
|1-e(a/q)|^2
}
=
\frac{
J_2(q)
}{12}
}
$$

gives the global coefficient energy：

$$
\boxed{
\mathcal C_{\rm axis}
=
\frac1{12}
\sum_{q\ge2}
|B_q|^2
J_2(q).
}
$$

Theorem 7.1 implies：

$$
|B_q|^2J_2(q)
\ll_\varepsilon
q^{-2+\varepsilon}.
$$

Hence：

## Theorem 13.1

$$
\boxed{
\mathcal C_{\rm axis}<\infty.
}
$$

So the infinite pair-square axis has a square-summable rational antiderivative spectrum。

---

# 14. Collapsed exact Cesàro weight

From v3.13：

$$
\boxed{
\Xi_N(d)
=
\sum_h
\Omega_N(h,d)
=
\sum_{n=2}^{2N-1-d}
(n-1)
w_N(n)
w_N(n+d).
}
$$

The support length is：

$$
O(N).
$$

Since：

$$
0\le w_N\le N,
$$

we have：

$$
\boxed{
\|\Xi_N\|_\infty
\ll
N^4,
}
$$

and therefore：

$$
\boxed{
\|\Xi_N\|_2
\ll
N^{9/2}.
}
$$

---

# 15. Difference of the collapsed weight

Changing：

$$
d
$$

by one changes one $w_N$ factor by at most one and changes only endpoint terms of the same natural size。

Therefore：

$$
\boxed{
\|\Delta_d\Xi_N\|_\infty
\ll
N^3.
}
$$

On a support of length：

$$
O(N),
$$

this gives：

## Lemma 15.1

$$
\boxed{
\|\Delta_d\Xi_N\|_2
\ll
N^{7/2}.
}
$$

---

# 16. Low Ramanujan denominators

Let：

$$
\mathfrak A_{\le Q}(d)
=
\sum_{2\le q\le Q}
B_qc_q(d).
$$

Define its rational antiderivative：

$$
\mathfrak B_{\le Q}.
$$

The reduced fractions：

$$
a/q,
\qquad
q\le Q,
$$

have Farey spacing：

$$
\gg Q^{-2}.
$$

The one-dimensional large sieve and Theorem 13.1 give：

$$
\boxed{
\|
\mathfrak B_{\le Q}
\|_{L^2([1,2N])}
\ll
(N+Q^2)^{1/2}.
}
$$

---

# 17. Low-denominator weighted contribution

By summation by parts：

$$
\sum_d
\Xi_N(d)
\mathfrak A_{\le Q}(d)
=
-
\sum_d
\Delta_d^-\Xi_N(d)
\mathfrak B_{\le Q}(d).
$$

Thus Sections 15–16 give：

## Theorem 17.1

$$
\boxed{
\left|
\sum_d
\Xi_N(d)
\mathfrak A_{\le Q}(d)
\right|
\ll
N^{7/2}
(N+Q^2)^{1/2}.
}
$$

---

# 18. High-denominator weighted contribution

Cauchy–Schwarz, Section 14 and Theorem 11.1 give：

$$
\begin{aligned}
\left|
\sum_d
\Xi_N(d)
\widetilde{\mathfrak A}_{>Q}(d)
\right|
&\le
\|\Xi_N\|_2
\|
\widetilde{\mathfrak A}_{>Q}
\|_2
\\
&\ll_\varepsilon
N^{9/2}
\cdot
N^{1/2+\varepsilon}
Q^{-1+\varepsilon}.
\end{aligned}
$$

Hence：

## Theorem 18.1

$$
\boxed{
\left|
\sum_d
\Xi_N(d)
\widetilde{\mathfrak A}_{>Q}(d)
\right|
\ll_\varepsilon
N^{5+\varepsilon}
Q^{-1+\varepsilon}.
}
$$

---

# 19. Optimize the denominator split

Write：

$$
Q=N^\theta.
$$

For：

$$
\theta\ge\frac12,
$$

Theorem 17.1 has exponent：

$$
\boxed{
\frac72+\theta.
}
$$

Theorem 18.1 has exponent：

$$
\boxed{
5-\theta.
}
$$

Balance them：

$$
\frac72+\theta
=
5-\theta.
$$

Therefore：

$$
\boxed{
\theta=\frac34.
}
$$

So the canonical split is：

$$
\boxed{
Q=N^{3/4}.
}
$$

---

# 20. Full infinite-conductor axis bound

Substituting：

$$
Q=N^{3/4}
$$

into Sections 17–18 gives：

## Theorem 20.1 · Axis Fixed-Power Closure

For every：

$$
\varepsilon>0,
$$

$$
\boxed{
\left|
\sum_d
\Xi_N(d)
\mathfrak A(d)
\right|
\ll_\varepsilon
N^{17/4+\varepsilon}.
}
$$

Equivalently：

$$
\boxed{
\left|
\sum_{h,d}
\Omega_N(h,d)
\mathfrak A(d)
\right|
\ll_\varepsilon
N^{17/4+\varepsilon}.
}
$$

Relative to the original quartic：

$$
N^5
$$

scale, the axis saving is：

$$
\boxed{
\eta_{\rm axis}
=
5-\frac{17}{4}
=
\frac34.
}
$$

Thus the one-dimensional axis is no longer a first fixed-power obstruction。

---

# 21. Comparison with the ordinary singular-series tail

Goldston–Hunts–Ngotiaoco define：

$$
\widetilde{\mathfrak S}_y(k)
=
\sum_{q>y}
\frac{
\mu(q)^2
}{
\phi(q)^2
}
c_q(-k).
$$

They prove, for：

$$
1\le y\le\sqrt N,
$$

a weighted mean-square asymptotic：

$$
\sum_{k\le N}
(N-k)^2
\widetilde{\mathfrak S}_y(k)^2
=
\mathcal T(y)
\frac{N^3}{3}
(
1+o(1)
),
$$

with：

$$
\boxed{
\mathcal T(y)
=
\sum_{q>y}
\frac{
\mu(q)^2
}{
\phi(q)^3
}
\sim
\frac{
\mathcal A
}{
y^2
}.
}
$$

Thus the natural：

$$
y^{-2}
$$

tail exponent is classical。

v3.14 shows that squaring and recentering the singular series does **not** destroy this denominator exponent at the upper-bound level。

---

# 22. Why v3.14 is simpler than the sharp tail theorem

The ordinary tail theorem determines：

- the exact asymptotic；
- the arithmetic constant；
- lower-order finite-$N$ terms。

v3.14 only requires：

$$
\boxed{
\text{a fixed-power upper bound}.
}
$$

The explicit axis coefficient decay：

$$
B_q\ll q^{-2+\varepsilon}
$$

plus the divisor formula for：

$$
c_q(n)
$$

is already sufficient。

Therefore no new delicate contour or exact diagonalization is needed for APST。

---

# 23. Finite-prime algebra validation

For any finite prime set：

$$
P,
$$

define：

$$
\mathfrak S_P(d)
=
\prod_{p\in P}
\left[
1+\frac{
c_p(d)
}{
(p-1)^2
}
\right].
$$

Define：

$$
\mathcal A_P
=
\prod_{p\in P}
\left(
1+\frac1{(p-1)^3}
\right).
$$

Then over the squarefree divisors of：

$$
\prod_{p\in P}p,
$$

the coefficient formula of Theorem 6.1 is exact：

$$
\boxed{
[
\mathfrak S_P(d)-1
]^2
-
(
\mathcal A_P-1
)
=
\sum_{\substack{
q\mid\prod_{p\in P}p\\
q>1
}}
B_{q,P}c_q(d).
}
$$

The reference package verifies this identity numerically for several：

$$
d
$$

and finite prime sets。

---

# 24. New deterministic state

After v3.14：

```text
1D axis exact Ramanujan coefficients
    CLOSED

1D axis high-denominator tail
    APST(1-o(1))

1D full sharp-weight contribution
    N^(17/4+epsilon)

1D axis fixed saving
    eta_axis = 3/4

1D axis as first obstruction
    CLOSED / DEPRIORITIZED

2D axis-free mixed tail
    OPEN
```

The deterministic parallelogram problem has now become genuinely two-dimensional。

---

# 25. Suggested v3.15 direction

Recommended：

`RH-AxisFree-MixedRamanujanTail v3.15`

Do not continue optimizing the 1D axis。

Tasks：

1. derive the infinite rational coefficient of：
   $$
   \mathfrak K_4^\perp;
   $$
2. group by the joint reduced conductor：
   $$
   \operatorname{lcm}(r(\alpha),r(\beta));
   $$
3. use the v3.13 mixed Sobolev：
   $$
   q^{o(1)}
   $$
   bound；
4. seek a **pointwise divisor-style tail bound** analogous to Theorem 10.1 but in two rational directions；
5. if direct divisor rearrangement fails, identify the exact shared-prime obstruction；
6. combine low joint conductor by two-dimensional large sieve with high conductor by a new mixed-tail inequality；
7. optimize the conductor split exactly as v3.14 did for the axis；
8. target any full：
   $$
   N^{5-\eta}
   $$
   deterministic bound。

The simpler axis is now closed strongly enough。

---

# 26. GAP ledger

## CLOSED / REDUCED

### G1. Exact pair-square Ramanujan coefficient

```text
CLOSED
```

### G2. APST

```text
CLOSED
```

$$
\delta=1-o(1).
$$

### G3. Low-denominator axis

```text
CLOSED
```

### G4. High-denominator axis

```text
CLOSED
```

### G5. Full axis fixed power

```text
N^(17/4+epsilon)
```

### G6. Axis saving

```text
eta_axis = 3/4
```

---

## OPEN

### G7. MSTT / 2D axis-free tail

```text
OPEN
```

### G8. Full deterministic：

$$
\eta_M>0
$$

```text
OPEN
```

### G9. Actual prime four-point deviation

```text
OPEN
```

### G10. Complete quartic：

$$
\eta_Q>0
$$

```text
OPEN
```

### G11. RH

```text
OPEN
```

---

# 27. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

AXIS RAMANUJAN EXPANSION = EXACT
APST UPPER BOUND = EXACT AT STATED EPSILON LEVEL

GHN TAIL THEOREM = EXTERNAL PUBLISHED SHARP ANALOGUE

N^(17/4+epsilon) AXIS BOUND
    = DETERMINISTIC MODEL ONLY

ETA_AXIS = 3/4
    != ETA_M
    != ETA_Q

NO 2D AXIS-FREE FIXED SAVING PROVED HERE
NO PRIME DEVIATION SAVING PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\eta_{\rm axis}=\frac34
\Longrightarrow
\Theta<1.
$$

The full deterministic and actual-prime remainders remain。

Forbidden：

$$
\text{ordinary singular-series tail theorem}
\Longrightarrow
\text{pair-square asymptotic}.
$$

v3.14 proves only an upper bound for the pair-square tail。

Forbidden：

$$
B_q\ll q^{-2+\varepsilon}
\Longrightarrow
\text{absolute convergence of the antiderivative series}.
$$

Only square-summable rational antiderivative coefficients are claimed。

---

# 28. One-line status

> v3.14 closes the one-dimensional constraint-adapted axis at fixed power. Starting from the classical Ramanujan expansion $\mathfrak S(d)=\sum \mu(q)^2\phi(q)^{-2}c_q(d)$, the prime identity $c_p(d)^2=(p-2)c_p(d)+(p-1)$ shows that the square remains in the squarefree Ramanujan basis. Writing $\mathcal A_*=\prod_p(1+(p-1)^{-3})$, one obtains $\mathfrak S(d)^2=\mathcal A_*\sum g(q)c_q(d)$ with local coefficient $g_p=(2p-3)/((p-1)(p^2-3p+3))$. Hence the centered pair-square axis has exact coefficients $B_q=\mathcal A_*g(q)-2/\phi(q)^2$ for squarefree $q>1$, and $B_q\ll_\varepsilon q^{-2+\varepsilon}$. The Ramanujan divisor identity then gives the pointwise tail bound $|\widetilde{\mathfrak A}_{>Q}(n)|\ll_\varepsilon\tau(n)Q^{-1+\varepsilon}$ and mean-square APST bound $N^{1+\varepsilon}Q^{-2+\varepsilon}$, preserving the classical $Q^{-2}$ denominator exponent known sharply for the ordinary singular-series tail. The axis antiderivative coefficients have finite total square energy by the Jordan-$J_2$ reciprocal-sine identity. Splitting Ramanujan denominators at $Q$, one-dimensional large sieve plus summation by parts bounds the low part by $N^{7/2}(N+Q^2)^{1/2}$, while the high tail contributes $N^{5+\varepsilon}Q^{-1+\varepsilon}$. Optimizing at $Q=N^{3/4}$ yields the full infinite-conductor sharp-Cesàro axis bound $N^{17/4+\varepsilon}$, a deterministic fixed saving of $3/4$ relative to the original $N^5$ quartic scale. The one-dimensional axis is therefore no longer the main deterministic obstruction; the next target is the genuinely two-dimensional axis-free mixed Ramanujan tail.

---

# 29. References

1. D. A. Goldston, Julian Ziegler Hunts, Timothy Ngotiaoco, **The Tail of the Singular Series for the Prime Pair and Goldbach Problems**, *Functiones et Approximatio Commentarii Mathematici* 56 (2017), 117–141.  
   arXiv: https://arxiv.org/abs/1409.2151

2. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.

3. AMRAL, **RH-Parallelogram-ConstraintAdaptedPairing v3.13**.

---

# 30. Provenance

研究主導：Neo.K

v3.14 exact pair-square Ramanujan expansion、axis coefficient decay、APST proof、low/high denominator optimization、$N^{17/4}$ full-axis closure、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 one-dimensional pair-square axis / Ramanujan-tail closure 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
