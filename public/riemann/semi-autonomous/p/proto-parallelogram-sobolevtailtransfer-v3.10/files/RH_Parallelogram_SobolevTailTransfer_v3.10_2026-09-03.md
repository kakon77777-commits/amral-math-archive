工程紀錄 · 第五弧線 v3.10 · 2026-09-03 · LOW_CONDUCTOR_RESTRICTION_CLOSED · SQRT_N_THRESHOLD · HIGH_CONDUCTOR_RESTRICTION_GAP · RH_CLAIM_FALSE

# Parallelogram Sobolev Tail Transfer：$\sqrt N$ Restriction Threshold、Denominator Tail 與 Large-Sieve Criticality

**RH-Parallelogram-SobolevTailTransfer v3.10**

本節點承接：

- `RH-Parallelogram-SobolevConductor v3.9`
- `RH-Parallelogram-RamanujanTail v3.8`

v3.9 已證：

$$
\boxed{
\sup_{q\ {\rm squarefree}}
\mathfrak H_d(q)
<
\infty,
}
$$

where：

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

Thus every finite-conductor covariance admits a uniformly bounded $d$-antiderivative。

v3.10 asks：

> Can this global / conductor-uniform Sobolev control be transferred quantitatively to an actual $O(N)\times O(N)$ finite box by standard rational-frequency restriction tools？

The answer has two parts。

---

## Positive result

Joint rational frequencies with both reduced denominators：

$$
\le
Q
$$

are completely controlled at natural scale whenever：

$$
\boxed{
Q\le N^{1/2}.
}
$$

Indeed a two-dimensional large-sieve argument gives：

$$
\boxed{
\sum_{h,d\ll N}
|
\mathfrak G_{\le Q}(h,d)
|^2
\ll
N^2,
}
$$

uniformly for：

$$
Q\le\sqrt N.
$$

Hence their contribution to the deterministic weighted model is：

$$
\boxed{
O(N^4).
}
$$

So the entire joint low-conductor spectrum：

$$
\boxed{
\operatorname{den}(\alpha),
\operatorname{den}(\beta)
\le
\sqrt N
}
$$

is closed。

---

## Negative / barrier result

The classical large sieve has natural cost：

$$
N+Q^2.
$$

At：

$$
Q>\sqrt N,
$$

Farey spacing：

$$
Q^{-2}
$$

is smaller than Fourier resolution：

$$
N^{-1}.
$$

Standard large-sieve restriction therefore loses finite-box resolution。

This is not because the arithmetic coefficients fail to decay。

v3.9 actually implies quantitative denominator-slice decay：

for reduced denominator：

$$
r,
$$

$$
\boxed{
\mathcal E_r
:=
\sum_{
\operatorname{den}(\beta)=r
}
\sum_\alpha
|
\widehat{\mathfrak K}_4(\alpha,\beta)
|^2
\ll_\varepsilon
r^{-3+\varepsilon},
}
$$

and：

$$
\boxed{
\mathcal H_r
:=
\sum_{
\operatorname{den}(\beta)=r
}
\sum_\alpha
\frac{
|
\widehat{\mathfrak K}_4(\alpha,\beta)
|^2
}{
|1-e(\beta)|^2
}
\ll_\varepsilon
r^{-2+\varepsilon}.
}
$$

Therefore：

$$
\boxed{
\sum_{r>Q}
\mathcal E_r
\ll_\varepsilon
Q^{-2+\varepsilon},
}
$$

and：

$$
\boxed{
\sum_{r>Q}
\mathcal H_r
\ll_\varepsilon
Q^{-1+\varepsilon}.
}
$$

So the high-conductor coefficients do decay by a genuine power。

The obstruction is that sufficiently high-denominator rational frequencies can cluster inside one $N^{-1}$ Fourier-resolution cell。

Generic large sieve treats this by the $Q^2$ spacing cost and loses the coefficient gain at the critical scale。

Thus the canonical remaining problem is：

$$
\boxed{
\text{SUPER-}\sqrt N
\text{ RATIONAL RESTRICTION}
}
$$

rather than：

```text
high conductor coefficients are too large.
```

---

## External calibration

Classical Farey large sieve says that fractions of denominator：

$$
\le Q
$$

are：

$$
Q^{-2}
$$

separated, leading to the familiar：

$$
N+Q^2
$$

restriction constant。

Bloom–Kuperberg's adding-fractions machinery obtains near-optimal counts for rational linear equations in settings where simple spacing is not enough。

Goldston–Hunts–Ngotiaoco prove in the one-dimensional prime-pair singular-series setting that a Ramanujan tail has weighted mean-square decay of order：

$$
y^{-2},
$$

showing that arithmetic structure can beat a naive generic tail treatment。

v3.10 does not claim these external theorems directly close the present two-dimensional parallelogram restriction problem。

They identify the correct class of missing tools。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

UNIFORM_SOBOLEV = CLOSED_FROM_V3_9

DENOMINATOR_SLICE_RAW_L2 = O_epsilon(r^(-3+epsilon))
DENOMINATOR_SLICE_SOBOLEV = O_epsilon(r^(-2+epsilon))

RAW_COEFFICIENT_TAIL = O_epsilon(Q^(-2+epsilon))
SOBOLEV_COEFFICIENT_TAIL = O_epsilon(Q^(-1+epsilon))

TWO_DIMENSIONAL_LARGE_SIEVE = APPLIED
JOINT_DENOMINATOR_Q_LE_SQRT_N = O(N^4)

SQRT_N_THRESHOLD = EXACT_STANDARD_LARGE_SIEVE_SCALE

STANDARD_LARGE_SIEVE_FULL_HIGH_CONDUCTOR_CLOSURE = NOT_OBTAINED

FULL_SHORT_RECTANGLE_RESTRICTION = OPEN
FULL_FIXED_ETA_M_POSITIVE = NOT_PROVED

ACTUAL_PRIME_DEVIATION = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Rational denominator slices

For a rational：

$$
\beta\in\mathbb Q/\mathbb Z,
$$

let：

$$
r(\beta)
$$

denote its reduced denominator。

From v3.9, for every finite squarefree conductor containing $r$：

$$
\boxed{
\|
\widehat{\mathfrak K}
(\cdot,\beta)
\|_2^2
\le
U(r),
}
$$

where：

$$
\boxed{
U(r)
\ll
\prod_{p\mid r}
p^{-4}
\cdot
C_0^{\omega(r)}
}
$$

for an absolute constant $C_0$。

Thus, for every：

$$
\varepsilon>0,
$$

$$
\boxed{
U(r)
\ll_\varepsilon
r^{-4+\varepsilon}.
}
$$

---

# 2. Raw coefficient mass at exact denominator

There are：

$$
\phi(r)
$$

reduced fractions of denominator：

$$
r.
$$

Therefore：

## Theorem 2.1 · Exact-denominator raw spectral mass

$$
\boxed{
\mathcal E_r
=
\sum_{\substack{
\beta\in\mathbb Q/\mathbb Z\\
r(\beta)=r
}}
\sum_\alpha
|
\widehat{\mathfrak K}_4(\alpha,\beta)
|^2
\ll_\varepsilon
r^{-3+\varepsilon}.
}
$$

---

# 3. Sobolev mass at exact denominator

v3.9 uses：

$$
\sum_{\substack{1\le a<r\\\gcd(a,r)=1}}
\frac1{
|1-e(a/r)|^2
}
=
\frac{J_2(r)}{12}.
$$

Since：

$$
J_2(r)\le r^2,
$$

Theorem 1 gives：

## Theorem 3.1 · Exact-denominator Sobolev mass

$$
\boxed{
\mathcal H_r
=
\sum_{\substack{
r(\beta)=r
}}
\sum_\alpha
\frac{
|
\widehat{\mathfrak K}_4(\alpha,\beta)
|^2
}{
|1-e(\beta)|^2
}
\ll_\varepsilon
r^{-2+\varepsilon}.
}
$$

---

# 4. High-denominator spectral tails

Summing Sections 2–3 gives：

## Theorem 4.1

For every：

$$
\varepsilon>0,
$$

$$
\boxed{
\sum_{r>Q}
\mathcal E_r
\ll_\varepsilon
Q^{-2+\varepsilon},
}
$$

and：

$$
\boxed{
\sum_{r>Q}
\mathcal H_r
\ll_\varepsilon
Q^{-1+\varepsilon}.
}
$$

Thus the full rational spectrum has genuine power-decaying conductor tails in $B^2$ and Sobolev coefficient space。

---

# 5. Farey frequency set

Define：

$$
\boxed{
\mathcal F_Q
=
\{0\}
\cup
\left\{
\frac ar\bmod1:
1\le r\le Q,
\gcd(a,r)=1
\right\}.
}
$$

Distinct nonzero elements of：

$$
\mathcal F_Q
$$

are separated by：

$$
\boxed{
\gg Q^{-2}.
}
$$

This is the classical Farey-spacing fact。

---

# 6. One-dimensional large sieve

If：

$$
f
$$

is supported on an interval of length：

$$
L,
$$

and：

$$
\xi_j
$$

are：

$$
\delta
$$

-separated frequencies, then：

$$
\boxed{
\sum_j
|
\widehat f(\xi_j)
|^2
\ll
\left(
L+\delta^{-1}
\right)
\sum_n
|f(n)|^2.
}
$$

For：

$$
\mathcal F_Q,
$$

$$
\delta^{-1}
\ll
Q^2.
$$

Hence：

$$
\boxed{
\sum_{\xi\in\mathcal F_Q}
|
\widehat f(\xi)
|^2
\ll
(L+Q^2)
\|f\|_2^2.
}
$$

---

# 7. Two-dimensional product large sieve

Let：

$$
F(h,d)
$$

be supported in a rectangle of side lengths：

$$
O(N).
$$

Apply Section 6 in $h$ and $d$ successively。

Then：

## Theorem 7.1

$$
\boxed{
\sum_{
\alpha,\beta\in\mathcal F_Q
}
|
\widehat F(\alpha,\beta)
|^2
\ll
(N+Q^2)^2
\|F\|_2^2.
}
$$

This is the natural product-Farey restriction inequality。

---

# 8. Apply to the differentiated Cesàro weight

Let：

$$
\boxed{
F_N(h,d)
=
\Delta_d^-\Omega_N(h,d).
}
$$

v3.9 gives：

$$
\boxed{
\|F_N\|_2^2
\ll
N^6.
}
$$

Hence：

$$
\boxed{
\sum_{
\alpha,\beta\in\mathcal F_Q
}
|
\widehat F_N(\alpha,\beta)
|^2
\ll
(N+Q^2)^2
N^6.
}
$$

---

# 9. Low-conductor antiderivative projection

Let：

$$
\widehat{\mathfrak G}
(\alpha,\beta)
=
\frac{
\widehat{\mathfrak K}_4(\alpha,\beta)
}{
e(\beta)-1
}
$$

for：

$$
\beta\ne0.
$$

Define the joint low-conductor projection：

$$
\boxed{
\mathfrak G_{\le Q}
=
\sum_{
\substack{
\alpha,\beta\in\mathcal F_Q\\
\beta\ne0
}
}
\widehat{\mathfrak G}(\alpha,\beta)
e(h\alpha+d\beta).
}
$$

v3.9 gives：

$$
\boxed{
\sum
|
\widehat{\mathfrak G}
|^2
\le
C_{\rm Sob}.
}
$$

---

# 10. Low-conductor weighted model

By summation by parts：

$$
\boxed{
\mathfrak M_{\le Q}(N)
=
-
\sum_{h,d}
F_N(h,d)
\mathfrak G_{\le Q}(h,d).
}
$$

Equivalently in frequency space：

$$
\boxed{
\mathfrak M_{\le Q}(N)
=
-
\sum_{
\substack{
\alpha,\beta\in\mathcal F_Q\\
\beta\ne0
}
}
\widehat{\mathfrak G}(\alpha,\beta)
\widehat F_N(-\alpha,-\beta).
}
$$

Cauchy–Schwarz, Sections 8–9 give：

## Theorem 10.1 · Joint Low-Conductor Restriction

$$
\boxed{
|
\mathfrak M_{\le Q}(N)
|
\ll
N^3
(N+Q^2).
}
$$

---

# 11. The $\sqrt N$ threshold

If：

$$
\boxed{
Q\le N^{1/2},
}
$$

then：

$$
N+Q^2
\ll N.
$$

Therefore：

## Corollary 11.1

$$
\boxed{
|
\mathfrak M_{\le Q}(N)
|
\ll
N^4.
}
$$

Thus all rational modes for which **both** reduced denominators are at most：

$$
\sqrt N
$$

are completely controlled at the natural lower-order scale。

---

# 12. Why $\sqrt N$ is the natural restriction scale

A length-$N$ Fourier polynomial has frequency resolution：

$$
N^{-1}.
$$

Farey fractions denominator：

$$
Q
$$

have minimal spacing：

$$
Q^{-2}.
$$

At：

$$
Q=\sqrt N,
$$

these scales coincide：

$$
\boxed{
Q^{-2}=N^{-1}.
}
$$

For：

$$
Q>\sqrt N,
$$

distinct rational frequencies can lie inside the same finite-box Fourier-resolution cell。

This is precisely why the standard large-sieve constant changes from：

$$
O(N)
$$

to：

$$
O(Q^2).
$$

---

# 13. Dyadic high-conductor Sobolev tail

Define：

$$
\boxed{
\mathcal H(R)
=
\sum_{
R<r(\beta)\le2R
}
\sum_\alpha
|
\widehat{\mathfrak G}(\alpha,\beta)
|^2.
}
$$

By Theorem 3.1：

$$
\boxed{
\mathcal H(R)
\ll_\varepsilon
R^{-1+\varepsilon}.
}
$$

Thus each dyadic denominator shell contains rapidly decreasing Sobolev energy。

---

# 14. What standard large sieve pays on a shell

If one combines a shell：

$$
r(\beta)\asymp R
$$

with a low-conductor $\alpha$ set of denominator：

$$
\le\sqrt N,
$$

the product large sieve pays：

$$
\boxed{
N(N+R^2)
}
$$

on the frequency side。

After Cauchy–Schwarz and using：

$$
\mathcal H(R)
\ll
R^{-1+\varepsilon},
$$

the generic shell estimate has scale：

$$
\boxed{
N^{7/2}
(N+R^2)^{1/2}
R^{-1/2+\varepsilon}.
}
$$

For：

$$
R\ge\sqrt N,
$$

this becomes：

$$
\boxed{
N^{7/2}
R^{1/2+\varepsilon}.
}
$$

At：

$$
R=N,
$$

this is already：

$$
N^{4+\varepsilon}.
$$

For：

$$
R>N,
$$

the generic spacing bound worsens。

This identifies the classical large-sieve criticality。

---

# 15. Why coefficient decay alone is not the issue

The raw coefficient tail is stronger：

$$
\sum_{r>Q}
\mathcal E_r
\ll
Q^{-2+\varepsilon}.
$$

Nevertheless, frequencies of denominator：

$$
r\gg N
$$

can be much closer than：

$$
N^{-1}.
$$

A finite box cannot distinguish them by generic harmonic analysis。

Thus：

$$
\boxed{
\text{coefficient decay}
+
\text{generic Farey spacing}
}
$$

is insufficient to close the entire infinite conductor range at a fixed exponent by the current argument。

One needs arithmetic information on how rational representations cluster and cancel。

---

# 16. Analogy with the prime-pair Ramanujan tail

For the one-dimensional prime-pair singular series, write its Ramanujan expansion and truncate denominators at：

$$
y.
$$

Goldston–Hunts–Ngotiaoco prove a weighted mean-square asymptotic for the tail：

$$
\widetilde{\mathfrak S}_y(k).
$$

In the range：

$$
1\le y\le\sqrt N,
$$

their result has the scale：

$$
\boxed{
\sum_{k\le N}
(N-k)^2
|
\widetilde{\mathfrak S}_y(k)
|^2
\asymp
\frac{
N^3
}{
y^2
}
}
$$

up to an explicit arithmetic constant and lower-order terms。

Thus arithmetic Ramanujan structure supplies a power-decaying finite-box tail beyond what a purely qualitative Besicovitch approximation states。

This is the closest classical analogue of the missing v3.10 transfer theorem。

---

# 17. Why the pair-tail theorem does not directly solve the parallelogram case

The current object is：

- two-dimensional；
- refined / centered；
- four-fraction；
- constrained by parallelogram geometry；
- coupled to the $d$-Sobolev denominator。

So the one-dimensional prime-pair tail theorem cannot simply be inserted。

But it establishes an important precedent：

$$
\boxed{
\text{high Ramanujan conductor}
\text{ can have a quantitative finite-box }L^2\text{ tail}.
}
$$

The missing theorem should be a parallelogram/refined analogue。

---

# 18. Adding-fractions interface

The rational-frequency expansion uses：

$$
\theta_1+\theta_2+\theta_3+\theta_4=0,
$$

and：

$$
\beta=\theta_3+\theta_4.
$$

Bloom–Kuperberg obtain near-optimal bounds for rational linear equations, particularly when generic large-sieve spacing is insufficient。

For v3.10 the dangerous configurations are high-denominator solutions for which：

$$
\beta
$$

falls inside an interval of width：

$$
O(N^{-1}).
$$

Thus the missing restriction theorem can be interpreted as a weighted **near-collision counting problem for sums of reduced fractions**。

---

# 19. Short-rectangle restriction gate

Let：

$$
\mathfrak G^{(\le R)}
$$

denote a rational-frequency partial sum ordered by joint conductor, and let：

$$
\mathfrak G^{(R_1,R_2]}
=
\mathfrak G^{(\le R_2)}
-
\mathfrak G^{(\le R_1)}.
$$

A strong sufficient theorem is：

## Short-Rectangle Restriction $\operatorname{SRR}$

For every：

$$
\varepsilon>0,
$$

uniformly in：

$$
R,
$$

$$
\boxed{
\sum_{
0\le h,d\le2N
}
|
\mathfrak G^{(\le R)}(h,d)
|^2
\ll_\varepsilon
N^{2+\varepsilon}.
}
$$

Then discrete summation by parts gives：

$$
\boxed{
\mathfrak M_{4,N}
\ll_\varepsilon
N^{4+\varepsilon}.
}
$$

This would completely close the deterministic model at the natural quartic scale。

---

# 20. Tail version

A weaker quantitative form is：

## Sobolev Tail Restriction $\operatorname{STR}(\delta)$

For：

$$
Q\ge\sqrt N,
$$

$$
\boxed{
\sum_{
0\le h,d\le2N
}
|
\mathfrak G^{(>Q)}(h,d)
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

combined with the low-conductor $N^4$ theorem yields a fixed-power tail gain。

If the natural B2 conductor decay transferred without loss, one would expect：

$$
\delta=\frac12
$$

at Sobolev level or stronger depending on the conductor ordering。

No such finite-box theorem is proved here。

---

# 21. Abstract criticality warning

The global Sobolev statement：

$$
\sum|\widehat{\mathfrak G}|^2<\infty
$$

alone is not enough for SRR。

A countable set of very high-denominator rational frequencies can cluster inside intervals shorter than：

$$
N^{-1},
$$

and a finite Fourier box cannot separate them without using additional arithmetic structure。

Thus the passage：

```text
B2 bounded
→
short-rectangle L2 bounded
```

is a genuine restriction theorem, not a formal consequence of Hilbert-space convergence。

---

# 22. Model state after v3.10

The deterministic parallelogram branch is now classified：

```text
zero mode
    CLOSED

beta=0 axis
    CLOSED

uniform finite-conductor Sobolev
    CLOSED

joint conductor <= sqrt(N)
    CLOSED AT N^4

coefficient conductor tails
    POWER DECAYING

super-sqrt(N) rational restriction
    OPEN

full deterministic fixed eta
    OPEN
```

The unresolved part is now extremely localized。

---

# 23. Why this is not yet a fixed-zero-strip result

Even if the deterministic singular-series model were fully $O(N^4)$, v3.6 still contains：

$$
\boxed{
\mathfrak E_{4,N}
}
$$

the actual prime deviation from the four-point model。

So deterministic closure is only one half of：

$$
\mathfrak Q_N
=
\mathfrak M_{4,N}
+
\mathfrak E_{4,N}.
$$

No：

$$
\eta_Q>0
$$

has yet been proved for the complete prime covariance。

---

# 24. Suggested v3.11 direction

Recommended：

`RH-Parallelogram-AddingFractionsRestriction v3.11`

Tasks：

1. write the high-conductor antiderivative coefficients directly in terms of the four reduced fractions；
2. localize：
   $$
   |\beta|
   \lesssim N^{-1};
   $$
3. count rational solutions to：
   $$
   \theta_1+\theta_2+\theta_3+\theta_4=0
   $$
   with：
   $$
   |\theta_3+\theta_4|
   \lesssim N^{-1};
   $$
4. exploit relative gcd parameterization / adding-fractions methods；
5. retain the coefficient weights：
   $$
   \prod_i\frac{\mu(q_i)}{\phi(q_i)};
   $$
6. seek an SRR or STR bound；
7. compare with the one-dimensional Goldston–Hunts–Ngotiaoco tail theorem；
8. if only logarithmic restriction is obtained, stop the deterministic branch and return to actual prime deviation。

This is the canonical continuation。

---

# 25. GAP ledger

## CLOSED / REDUCED

### G1. Denominator raw coefficient decay

```text
CLOSED
```

$$
\mathcal E_r
\ll_\varepsilon
r^{-3+\varepsilon}.
$$

### G2. Denominator Sobolev decay

```text
CLOSED
```

$$
\mathcal H_r
\ll_\varepsilon
r^{-2+\varepsilon}.
$$

### G3. Joint low conductor

```text
CLOSED
```

for：

$$
Q\le\sqrt N.
$$

### G4. Standard large-sieve threshold

```text
IDENTIFIED
```

$$
Q\sim\sqrt N.
$$

---

## OPEN

### G5. Super-$\sqrt N$ rational restriction

```text
OPEN
```

### G6. SRR / STR theorem

```text
OPEN
```

### G7. Full deterministic：

$$
\eta_M>0
$$

```text
OPEN
```

### G8. Actual prime deviation

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

# 26. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

LOW-CONDUCTOR LARGE-SIEVE CLOSURE = EXACT
DENOMINATOR TAIL DECAY = EXACT AT STATED EPSILON LEVEL

SQRT_N THRESHOLD = STANDARD FAREY/LARGE-SIEVE SCALE

STANDARD LARGE SIEVE FAILURE TO CLOSE
    = FAILURE OF CURRENT ARGUMENT
    NOT A MATHEMATICAL IMPOSSIBILITY THEOREM

PAIR SINGULAR-SERIES TAIL
    = ANALOGY / EXTERNAL METHOD PRECEDENT

NO SRR PROVED
NO STR(delta>0) PROVED

NO FULL ETA_M > 0 PROVED
NO PRIME ETA_Q > 0 PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
Q^{-2}\text{ coefficient tail}
\Longrightarrow
Q^{-2}\text{ finite-box tail}
$$

without a restriction theorem。

Forbidden：

$$
Q>\sqrt N
\Longrightarrow
\text{large sieve impossible}.
$$

Only the **standard spacing argument** becomes non-sharp there。

Forbidden：

$$
\text{pair Ramanujan tail theorem}
\Longrightarrow
\text{parallelogram tail theorem}.
$$

---

# 27. One-line status

> v3.10 converts the remaining deterministic high-conductor problem into a precise rational restriction threshold. The v3.9 Young/CRT majorant implies that the raw Fourier coefficient mass at exact reduced denominator $r$ is $O_\varepsilon(r^{-3+\varepsilon})$, while the $d$-Sobolev mass is $O_\varepsilon(r^{-2+\varepsilon})$; hence the global coefficient tails decay as $Q^{-2+\varepsilon}$ and $Q^{-1+\varepsilon}$ respectively. Let $\mathcal F_Q$ be the Farey set of reduced fractions with denominator at most $Q$. Iterating the classical large sieve in the two coordinates gives a product restriction constant $(N+Q^2)^2$. Applied to the differentiated Cesàro weight, whose squared $\ell^2$ norm is $O(N^6)$, and to the uniformly bounded Sobolev coefficient mass, this proves that every joint rational mode with both reduced denominators at most $\sqrt N$ contributes only $O(N^4)$. Thus the low-conductor spectrum is closed at the natural quartic scale. The remaining obstruction begins exactly when Farey spacing $Q^{-2}$ falls below the finite-box resolution $N^{-1}$. Standard dyadic large-sieve estimates then pay a spacing cost that becomes critical despite the genuine coefficient decay. This identifies the unresolved object as a super-$\sqrt N$ rational restriction theorem, not a conductor-size problem. The one-dimensional prime-pair singular-series tail theorem of Goldston–Hunts–Ngotiaoco shows that arithmetic Ramanujan structure can yield a power-decaying finite-box tail beyond qualitative Besicovitch convergence, while Bloom–Kuperberg's adding-fractions machinery supplies the natural toolkit for rational near-collisions. No such two-dimensional parallelogram restriction theorem is proved in this node.

---

# 28. References

1. Thomas F. Bloom, Vivian Kuperberg, **Odd moments and adding fractions**, *Proceedings of the London Mathematical Society* 131 (2025), e70068.  
   arXiv: https://arxiv.org/abs/2312.09021

2. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21 (2025), 53–74.  
   arXiv: https://arxiv.org/abs/2301.06095

3. D. A. Goldston, Julian Ziegler Hunts, Timothy Ngotiaoco, **The Tail of the Singular Series for the Prime Pair and Goldbach Problems**, *Functiones et Approximatio Commentarii Mathematici* 56 (2017), 117–141.  
   arXiv: https://arxiv.org/abs/1409.2151

4. Classical Montgomery–Vaughan / Selberg analytic large sieve and Farey-spacing theory.

5. AMRAL, **RH-Parallelogram-SobolevConductor v3.9**.

---

# 29. Provenance

研究主導：Neo.K

v3.10 denominator-slice decay、two-dimensional low-conductor large-sieve closure、$\sqrt N$ restriction threshold、high-conductor criticality audit、SRR/STR gate、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 rational restriction / super-$\sqrt N$ conductor gate。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
