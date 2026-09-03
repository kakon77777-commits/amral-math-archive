工程紀錄 · 第五弧線 v3.17 · 2026-09-03 · PRIME_STRUCTURED_APPROXIMATION · PAIR_ADAPTED_NORM · SINGLE_ENDPOINT_PAIR_GATE · RH_CLAIM_FALSE

# Prime Structured Approximation Gap：$\Lambda^\sharp$、Selberg $\Lambda_R$、Pair-Variance Adapted Norm 與 Character Interface

**RH-PrimeStructuredApproximationGap v3.17**

本節點承接：

- `RH-FourPointPrimeDeviation v3.16`
- Matomäki–Radziwiłł–Shao–Tao–Teräväinen higher-uniformity framework
- Chou–Haag–Huryn–Ledoan prime-pair error variance

v3.15 closed the deterministic four-point model：

$$
\boxed{
\mathfrak M_{4,N}
\ll_\varepsilon
N^{9/2+\varepsilon}.
}
$$

v3.16 isolated the actual-prime endpoint residual：

$$
\boxed{
Q_j(h)
=
r_j(h)-E(j)-E(j-h)+E(h)
}
$$

and the sufficient endpoint gate：

$$
\mathcal V_N
\le
N
\sum_{j=N}^{2N-1}
\sum_{h<j}
|Q_j(h)|^2.
$$

v3.17 asks：

> What kind of approximation to $\Lambda$ is actually strong enough to yield a fixed-power upper bound for prime-pair variance？

The answer is：

$$
\boxed{
\text{ordinary function approximation is not the right norm.}
}
$$

The correct object is a **quadratic pair-variance adapted Fourier approximation**。

This node establishes：

1. the exact pair-variance Fourier identity；
2. an exact three-term structured/pseudorandom decomposition；
3. a sufficient pair-adapted approximation gate；
4. a no-go audit for simply using the current $\Lambda^\sharp$ cutoff；
5. a no-go audit for using Selberg $\Lambda_R$ through ordinary $L^2$ smallness；
6. a direct reduction from a single-endpoint fixed-power prime-pair variance upper bound to a fixed zeta zero strip；
7. the exact rational-character interface for the next major-arc node。

No fixed-power actual-prime theorem is proved。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DETERMINISTIC_ETA_M = 1/2

PAIR_VARIANCE_FOURIER_IDENTITY = CLOSED
STRUCTURED_PAIR_DECOMPOSITION = CLOSED
PVAA_GATE = CLOSED_AS_SUFFICIENT_REDUCTION

MRSTT_LAMBDA_SHARP = EXTERNAL_PUBLISHED
MRSTT_PSEUDORANDOM_SAVING = LOG_POWER / o(1)
MRSTT_STRUCTURED_CUTOFF = X^(o(1))

LAMBDA_SHARP_FIXED_POWER_FROM_CUTOFF_ALONE = NO
SELBERG_LAMBDA_R_L2_FIXED_POWER_APPROXIMATION = NO

SINGLE_ENDPOINT_PAIR_VARIANCE_GATE = CLOSED_AS_SUFFICIENT
PAIR_VARIANCE_FIXED_SAVING_DIRECTLY_ZERO_SENSITIVE = TRUE

UNCONDITIONAL_PAIR_VARIANCE_ETA_POSITIVE = OPEN
UNCONDITIONAL_PVAA_ETA_POSITIVE = OPEN
FPD_ETA_POSITIVE = OPEN
ETA_Q_POSITIVE = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Endpoint prime exponential sum

For：

$$
j\ge1,
$$

define：

$$
\boxed{
S_j(\alpha)
=
\sum_{n\le j}
\Lambda(n)e(n\alpha).
}
$$

Then：

$$
\boxed{
|S_j(\alpha)|^2
=
\sum_{|h|<j}
\psi_2(j,h)e(h\alpha),
}
$$

where for：

$$
h\ge0,
$$

$$
\boxed{
\psi_2(j,h)
=
\sum_{n\le j-h}
\Lambda(n+h)\Lambda(n).
}
$$

---

# 2. Hardy–Littlewood pair model polynomial

Define：

$$
\boxed{
V_j(\alpha)
=
\sum_{0<|h|<j}
\mathfrak S(h)
(j-|h|)
e(h\alpha).
}
$$

The diagonal：

$$
h=0
$$

may be handled separately。

Define：

$$
\boxed{
D_j(\alpha)
=
|S_j(\alpha)|^2
-
V_j(\alpha).
}
$$

For nonzero：

$$
h,
$$

the Fourier coefficient of：

$$
D_j
$$

is：

$$
\boxed{
r_j(h)
=
\psi_2(j,h)
-
\mathfrak S(h)(j-|h|).
}
$$

---

# 3. Pair-variance Parseval identity

Let：

$$
E_{\rm pair}^{+}(j)
=
\sum_{h=1}^{j-1}
|r_j(h)|^2.
$$

Then：

## Theorem 3.1

$$
\boxed{
2E_{\rm pair}^{+}(j)
=
\int_0^1
|D_j(\alpha)-\widehat D_j(0)|^2
d\alpha.
}
$$

Thus standard prime-pair error variance is a quadratic approximation problem for：

$$
|S_j|^2,
$$

not merely a linear approximation problem for：

$$
S_j.
$$

---

# 4. General structured approximation

Let：

$$
\boxed{
S_j=A_j+B_j,
}
$$

where：

- $A_j$ is any proposed structured approximation；
- $B_j=S_j-A_j$。

Then：

## Theorem 4.1 · Exact Pair Approximation Decomposition

$$
\boxed{
|S_j|^2-V_j
=
\left(
|A_j|^2-V_j
\right)
+
2\Re(
A_j\overline{B_j}
)
+
|B_j|^2.
}
$$

---

# 5. Three pair-adapted energies

Define：

$$
\boxed{
\mathcal M_j(A)
=
\int_0^1
\left|
|A_j|^2-V_j
\right|^2
d\alpha,
}
$$

$$
\boxed{
\mathcal X_j(A,B)
=
\int_0^1
|A_j|^2|B_j|^2
d\alpha,
}
$$

and：

$$
\boxed{
\mathcal U_j(B)
=
\int_0^1
|B_j|^4
d\alpha.
}
$$

---

# 6. Pair-Variance Adapted Approximation gate

Using elementary quadratic inequalities：

## Theorem 6.1

$$
\boxed{
\int_0^1
|
|S_j|^2-V_j
|^2
\le
3\mathcal M_j
+
12\mathcal X_j
+
3\mathcal U_j.
}
$$

Define：

## PVAA$(\eta)$

There exists a family：

$$
A_j
$$

such that：

$$
\boxed{
\sum_{j=N}^{2N-1}
[
\mathcal M_j
+
\mathcal X_j
+
\mathcal U_j
]
\ll
N^{4-\eta+o(1)}.
}
$$

Then the integrated standard pair-error variance has the same fixed saving。

---

# 7. Why ordinary $L^2$ approximation is insufficient

An estimate：

$$
\int
|B_j|^2
\ll
j^{1-\eta}
$$

does not by itself control：

$$
\int|B_j|^4
$$

or：

$$
\int|A_j|^2|B_j|^2.
$$

Therefore：

$$
\boxed{
\|\Lambda-\text{approximant}\|_2
}
$$

is not the primary norm for this problem。

---

# 8. The MRSTT structured approximant

Matomäki–Radziwiłł–Shao–Tao–Teräväinen define：

$$
\boxed{
\Lambda^\sharp(n)
=
\frac{
P(R)
}{
\phi(P(R))
}
1_{(n,P(R))=1},
}
$$

where：

$$
P(R)=\prod_{p<R}p,
$$

and：

$$
\boxed{
R=\exp((\log X)^{1/10}).
}
$$

Their 2026 almost-all short-interval theorem gives arbitrary logarithmic-power discorrelation of：

$$
\Lambda-\Lambda^\sharp
$$

with nilsequences when：

$$
H\ge X^{1/3+\varepsilon},
$$

and asymptotically small short-interval Gowers norms。

---

# 9. Meaning for parallelogram pseudorandom terms

Write：

$$
b(n)=\Lambda(n)-\Lambda^\sharp(n),
$$

and：

$$
s(n)=\Lambda^\sharp(n)-1.
$$

Then：

$$
\Lambda(n)-1=s(n)+b(n).
$$

Every two-point and four-point expression expands into：

```text
all-structured terms
+
terms containing at least one b factor.
```

Higher-uniformity / generalized von Neumann methods are designed to eliminate terms containing at least one pseudorandom factor in averaged finite-complexity linear-pattern problems。

However the published quantitative strength for：

$$
\Lambda-\Lambda^\sharp
$$

is logarithmic / qualitative, not：

$$
X^{-\eta}.
$$

So it does not close PVAA at fixed power。

---

# 10. Structured small-prime cutoff is still subpower

The same framework computes correlations of：

$$
\Lambda_w
$$

and matches the Hardy–Littlewood singular series for most averaging shifts with displayed local-tail strength：

$$
O(w^{-1/2}).
$$

The admissible：

$$
w
$$

can grow subpolynomially, e.g.：

$$
w\le\exp((\log X)^{1/2}).
$$

Hence even：

$$
w^{-1/2}
$$

has size：

$$
\exp(-c\sqrt{\log X})
=
X^{-o(1)},
$$

not：

$$
X^{-\eta}.
$$

Thus the existing small-prime cutoff architecture alone cannot generate a fixed exponent。

---

# 11. Selberg polynomial-cutoff approximation

Define：

$$
\boxed{
\Lambda_R(n)
=
\sum_{\substack{
d\mid n\\
d\le R
}}
\mu(d)
\log(R/d).
}
$$

Let：

$$
S_R(\alpha)
=
\sum_{n\le N}
\Lambda_R(n)e(n\alpha).
$$

Classically：

$$
\sum_{n\le N}\Lambda_R(n)^2
=
N\log R+O(N),
$$

and：

$$
\sum_{n\le N}\Lambda_R(n)\Lambda(n)
=
N\log R+O(R)+O_A(N\log^{-A}N).
$$

Consequently：

## Theorem 11.1

$$
\boxed{
\int_0^1
|S(\alpha)-S_R(\alpha)|^2
d\alpha
=
N\log(N/R)+O(N).
}
$$

---

# 12. Polynomial-cutoff $L^2$ no-go

Take：

$$
R=N^\theta,
\qquad
0<\theta<1.
$$

Then：

$$
\boxed{
\|S-S_R\|_2^2
=
(1-\theta)N\log N+O(N).
}
$$

Thus a polynomial Selberg cutoff does not make the residual power-small in ordinary：

$$
L^2.
$$

This does not rule out pair-adapted bilinear or dispersion uses of：

$$
\Lambda_R.
$$

---

# 13. Single-endpoint pair-variance gate

Define：

$$
\boxed{
E_{\rm pair}(x)
=
\sum_{1\le|h|\le x}
[
\psi_2(x,h)
-
\mathfrak S(h)(x-|h|)
]^2.
}
$$

Define：

## PPEU$(\eta)$

$$
\boxed{
E_{\rm pair}(x)
\ll
x^{3-\eta+o(1)}.
}
$$

---

# 14. PPEU is directly zero-sensitive

Chou–Haag–Huryn–Ledoan prove：

$$
\boxed{
E_{\rm pair}(x)
=
\Omega(
x^{1+2\Theta-\varepsilon}
).
}
$$

Hence PPEU$(\eta)$ implies：

## Theorem 14.1

$$
\boxed{
\Theta
\le
1-\frac{\eta}{2}.
}
$$

So a single-endpoint fixed-power pair-variance improvement already gives a fixed zeta zero strip directly。

---

# 15. Bootstrap from PPEU to EPV

Assume PPEU$(\eta)$。

Then：

$$
E(x)=\psi(x)-x
\ll
x^{1-\eta/2+\varepsilon}.
$$

Recall：

$$
Q_j(h)
=
r_j(h)-E(j)-E(j-h)+E(h).
$$

Therefore：

$$
\sum_{h<j}|Q_j(h)|^2
\ll
E_{\rm pair}(j)
+
j|E(j)|^2
+
\sum_{m<j}|E(m)|^2.
$$

Each term is：

$$
\ll
j^{3-\eta+o(1)}.
$$

Thus：

## Theorem 15.1

$$
\boxed{
\sum_{j=N}^{2N-1}
\sum_{h<j}|Q_j(h)|^2
\ll
N^{4-\eta+o(1)}.
}
$$

PPEU therefore bootstraps to EPV with essentially the same exponent。

---

# 16. GRH calibration

Under GRH for Dirichlet $L$-functions, the published pair-variance bound is：

$$
E_{\rm pair}(N)
\ll
N^{5/2}(\log N)^C.
$$

This corresponds to：

$$
\eta=\frac12
$$

up to logarithms。

Conditional calibration only。

---

# 17. Exact rational-character interface

For：

$$
(a,q)=1,
$$

and：

$$
(n,q)=1,
$$

character orthogonality gives：

$$
\boxed{
e(an/q)
=
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)\chi(a)\chi(n).
}
$$

Define：

$$
\psi(x,\chi)
=
\sum_{n\le x}\Lambda(n)\chi(n).
$$

Then：

## Theorem 17.1

$$
\boxed{
S_x(a/q)
=
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)\chi(a)\psi(x,\chi)
+
O(
\omega(q)\log x
).
}
$$

The error comes from prime powers with prime dividing：

$$
q.
$$

---

# 18. Zero sensitivity

For nonprincipal：

$$
\chi,
$$

the explicit formula expresses：

$$
\psi(x,\chi)
$$

through zeros：

$$
\rho_\chi
$$

of：

$$
L(s,\chi).
$$

Schematically：

$$
\psi(x,\chi)
=
-
\sum_{\rho_\chi}
\frac{x^{\rho_\chi}}{\rho_\chi}
+
\text{lower terms}.
$$

Thus a fixed-power character-major-arc variance theorem must control rightmost Dirichlet $L$-zero contributions either individually or after the exact variance averaging。

---

# 19. Why generic zero density is not automatic closure

A zero-density theorem may allow a small number of zeros very close to：

$$
\Re s=1.
$$

One such zero can dominate：

$$
\psi(x,\chi)
$$

for its character and survive squaring in pair variance。

Therefore the missing theorem must either：

1. rule out sufficiently rightmost zeros in the relevant conductor range；or
2. prove their exact weighted pair-spectrum contribution is power-small。

The second could be weaker than a uniform Dirichlet zero-free strip。

---

# 20. New pair-adapted hierarchy

The actual-prime branch is now organized as：

```text
minimal:
    FPD(eta)

endpoint:
    EPV(eta)

standard literature-aligned stronger gate:
    PPEU(eta)

approximation architecture:
    PVAA(eta)

next zero-sensitive layer:
    character-major-arc pair variance
```

Each candidate proof must state which gate it actually closes。

---

# 21. Strategic consequence

The remaining problem is not：

```text
find a better deterministic singular-series model
```

and not merely：

```text
make Lambda approximant closer in L2.
```

It is：

$$
\boxed{
\text{approximate the pair spectrum }|S(\alpha)|^2
\text{ at fixed power.}
}
$$

This is the central v3.17 conclusion。

---

# 22. Suggested v3.18 direction

Recommended：

`RH-CharacterMajorArcVariance v3.18`

Tasks：

1. extend the character formula from：
   $$
   a/q
   $$
   to：
   $$
   a/q+\beta
   $$
   by partial summation；
2. insert into：
   $$
   |S_x|^2-V_x;
   $$
3. separate principal-principal, principal-nonprincipal, and nonprincipal-nonprincipal terms；
4. identify the principal term reproducing the singular series；
5. write the structured variance as weighted moments of：
   $$
   \psi(x,\chi);
   $$
6. insert the explicit formula；
7. group zeros by real part, conductor, and height；
8. determine the weakest weighted zero theorem sufficient for PVAA or PPEU；
9. compare with current zero-density estimates；
10. reject any bound that still permits one power-dominant rightmost zero。

---

# 23. GAP ledger

## CLOSED / REDUCED

### G1. Pair-spectrum Fourier identity

```text
CLOSED
```

### G2. Pair-adapted approximation decomposition

```text
CLOSED
```

### G3. PVAA sufficient gate

```text
CLOSED_AS_REDUCTION
```

### G4. $\Lambda^\sharp$ fixed-power audit

```text
NO
```

### G5. Selberg ordinary-$L^2$ fixed-power audit

```text
NO
```

### G6. PPEU bootstrap

```text
CLOSED_AS_REDUCTION
```

---

## OPEN

### G7. PVAA$(\eta>0)$

```text
OPEN
```

### G8. PPEU$(\eta>0)$

```text
OPEN
```

### G9. Character-major-arc fixed-power variance

```text
OPEN
```

### G10. FPD / EPV fixed power

```text
OPEN
```

### G11. Complete quartic $\eta_Q>0$

```text
OPEN
```

### G12. RH

```text
OPEN
```

---

# 24. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DETERMINISTIC eta_M = 1/2

PVAA = SUFFICIENT ARCHITECTURE ONLY
PPEU = STRONGER PRIME GATE, NOT PROVED

NO FIXED PRIME ETA PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\Lambda-\Lambda^\sharp
\text{ has log-power Gowers saving}
\Longrightarrow
\operatorname{PVAA}(\eta).
$$

Forbidden：

$$
\|\Lambda-\Lambda_R\|_2
\text{ improves as }R\uparrow N
\Longrightarrow
\text{pair variance fixed saving}.
$$

---

# 25. One-line status

> v3.17 identifies the exact approximation norm required on the actual-prime side. The standard prime-pair variance is a Parseval $L^2$ discrepancy between $|S_x(\alpha)|^2$ and the Hardy–Littlewood pair-model Fourier polynomial. For any structured decomposition $S_x=A_x+B_x$, this discrepancy splits exactly into a structured model mismatch $|A_x|^2-V_x$, a cross term $2\Re(A_x\bar B_x)$, and a pure residual term $|B_x|^2$. This yields the Pair-Variance Adapted Approximation gate PVAA, requiring fixed-power control of the three energies $\mathcal M$, $\mathcal X$, and $\mathcal U=\|B\|_4^4$. Current $\Lambda^\sharp$ higher-uniformity is designed to eliminate terms containing a pseudorandom factor, but its quantitative strength is logarithmic and its small-prime cutoff is only $X^{o(1)}$; the resulting structured local tail remains $X^{-o(1)}$, not $X^{-\eta}$. Selberg's polynomial-cutoff $\Lambda_R$ avoids subpolynomial conductor but its ordinary residual Fourier energy is $N\log(N/R)+O(N)$, so $R=N^\theta$ leaves a fixed proportion of the prime $L^2$ energy. Thus the missing theorem must be pair-adapted rather than a better ordinary approximation. A single-endpoint bound $E_{\rm pair}(x)\ll x^{3-\eta}$ is already enough to force $\Theta\le1-\eta/2$ by the Chou–Haag–Huryn–Ledoan lower bound and then bootstraps to the AMRAL endpoint gate. Finally, rational major arcs admit an exact Dirichlet-character representation of $S_x(a/q)$ through $\psi(x,\chi)$, locating the remaining fixed-power obstruction at a zero-sensitive character-major-arc variance.

---

# 26. References

1. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   arXiv: https://arxiv.org/abs/2411.05770

2. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   arXiv: https://arxiv.org/abs/2308.14888

3. D. A. Goldston, **The major arcs approximation for an exponential sum over primes**, *Acta Arithmetica* 92 (2000), 169–179.

4. AMRAL, **RH-FourPointPrimeDeviation v3.16**.

5. AMRAL, **RH-AxisFree-MixedRamanujanTail v3.15**.

---

# 27. Provenance

研究主導：Neo.K

v3.17 pair-variance adapted approximation framework、$\Lambda^\sharp$ fixed-power audit、Selberg $L^2$ no-go、PPEU bootstrap、Dirichlet-character interface、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 structured-prime approximation / pair-spectrum gate。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
