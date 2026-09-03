工程紀錄 · 第五弧線 v3.16 · 2026-09-03 · ACTUAL_PRIME_DEVIATION · ENDPOINT_PAIR_VARIANCE_GATE · LOG_UNIFORMITY_BARRIER · RH_CLAIM_FALSE

# Four-Point Prime Deviation：Actual $\Lambda$ Barrier、Endpoint Pair Variance Gate 與 Log-Uniformity Limitation

**RH-FourPointPrimeDeviation v3.16**

本節點承接：

- `RH-AxisFree-MixedRamanujanTail v3.15`
- `RH-MeanSquare-ArithmeticGap v3.5`
- `RH-CenteredShift-FourierGap v3.6`

v3.15 closed the entire deterministic refined-singular-series contribution：

$$
\boxed{
\mathfrak M_{4,N}
\ll_\varepsilon
N^{9/2+\varepsilon}.
}
$$

Thus：

$$
\boxed{
\eta_M=\frac12.
}
$$

The remaining quartic object is：

$$
\boxed{
\mathfrak Q_N
=
\mathfrak M_{4,N}
+
\mathfrak E_{4,N},
}
$$

where：

$$
\boxed{
\mathfrak E_{4,N}
}
$$

is the **actual-prime deviation** from the correctly centered four-point Hardy–Littlewood / refined-singular-series model。

v3.16 does not prove a fixed power saving for：

$$
\mathfrak E_{4,N}.
$$

Instead it completes three reductions：

1. derives the exact local actual-prime deviation field；
2. identifies an endpoint prime-pair variance theorem that is sufficient for the entire RH progress gate；
3. audits current 2026 prime-correlation / higher-uniformity technology and finds no unconditional fixed：
   $$
   N^{-\eta}
   $$
   gain。

The new canonical status is：

```text
DETERMINISTIC MODEL
    CLOSED AT eta_M = 1/2

ACTUAL PRIME DEVIATION
    OPEN

CURRENT GENERAL HIGHER UNIFORMITY
    LOG-POWER / o(1) SAVING

FIXED POWER PRIME VARIANCE
    OPEN
```

No RH claim is made。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DETERMINISTIC_MODEL_ETA_M = 1/2

LOCAL_PRIME_DEVIATION_IDENTITY = CLOSED
ENDPOINT_PAIR_RESIDUAL_IDENTITY = CLOSED
EPV_GATE = CLOSED_AS_SUFFICIENT_REDUCTION

GRH_PAIR_VARIANCE_CALIBRATION = EXTERNAL_CONDITIONAL
GRH_EPV_ETA = 1/2_UP_TO_LOGS

HIGHER_UNIFORMITY_PSEUDORANDOM_SAVING = LOG_POWER
HIGHER_UNIFORMITY_FIXED_POWER_ETA = NOT_OBTAINED

UNCONDITIONAL_EPV_ETA_POSITIVE = OPEN
UNCONDITIONAL_FPD_ETA_POSITIVE = OPEN
COMPLETE_QUARTIC_ETA_Q_POSITIVE = OPEN

MEANSQUARE_KAPPA_I_POSITIVE = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Centered prime sequence

Define：

$$
\boxed{
a_n
=
\Lambda(n)-1.
}
$$

For：

$$
h\ge1,
$$

write：

$$
\boxed{
\mu_h
=
\mathfrak S(h)-1.
}
$$

Define the pointwise centered pair fluctuation：

$$
\boxed{
P_h(r)
=
a_r a_{r+h}
-
\mu_h.
}
$$

---

# 2. Refined four-point main term

For：

$$
h,d\ge1,
\qquad
h\ne d,
$$

define the parallelogram：

$$
\boxed{
\mathcal H_{h,d}
=
\{0,h,d,h+d\}.
}
$$

Let：

$$
\boxed{
\mathfrak S_0(\mathcal H_{h,d})
}
$$

be the refined / centered Hardy–Littlewood four-point singular-series main term。

Define the pointwise four-point prime-pattern error：

$$
\boxed{
T_{h,d}(r)
=
a_r
a_{r+h}
a_{r+d}
a_{r+h+d}
-
\mathfrak S_0(
0,h,d,h+d
).
}
$$

---

# 3. Deterministic covariance model

v3.6 defines：

$$
\boxed{
\mathfrak K_4(h,d)
=
\mathfrak S_0(
0,h,d,h+d
)
-
\mu_h^2.
}
$$

The actual pair-pair product is：

$$
P_h(r)P_h(r+d).
$$

---

# 4. Exact actual-prime deviation field

Expand：

$$
P_h(r)P_h(r+d).
$$

Then：

$$
\begin{aligned}
&P_h(r)P_h(r+d)
-
\mathfrak K_4(h,d)
\\
&=
a_ra_{r+h}a_{r+d}a_{r+h+d}
-
\mathfrak S_0
\\
&\quad
-
\mu_h
\left[
P_h(r)
+
P_h(r+d)
\right].
\end{aligned}
$$

Therefore：

## Theorem 4.1 · Prime Deviation Identity

$$
\boxed{
P_h(r)P_h(r+d)
-
\mathfrak K_4(h,d)
=
T_{h,d}(r)
-
\mu_h
\left[
P_h(r)
+
P_h(r+d)
\right].
}
$$

This splits the actual-prime deviation into：

```text
GENUINE FOUR-POINT PRIME PATTERN ERROR
+
PAIR-ERROR CORRECTION.
```

---

# 5. Exact weighted FPD object

Recall the v3.6 four-distinct coordinates：

$$
r,
\quad
r+h,
\quad
r+d,
\quad
r+d+h.
$$

Define：

$$
\boxed{
W_N(r,h,d)
=
2
w_N(r+h)
w_N(r+d+h).
}
$$

The valid region is：

$$
r,h,d\ge1,
$$

$$
h\ne d,
$$

$$
r+h+d\le2N-1.
$$

Then：

## Theorem 5.1

$$
\boxed{
\begin{aligned}
\mathfrak E_{4,N}
&=
\sum_{r,h,d}
W_N(r,h,d)
T_{h,d}(r)
\\
&\quad
-
\sum_{r,h,d}
W_N(r,h,d)
\mu_h
\left[
P_h(r)
+
P_h(r+d)
\right].
\end{aligned}
}
$$

Thus the remaining v3.15 obstruction is genuinely prime-specific。

---

# 6. Endpoint pair residual

For：

$$
1\le h<j,
$$

define：

$$
\boxed{
Q_j(h)
=
\sum_{n=h+1}^{j}
a_n a_{n-h}
-
\mu_h(j-h).
}
$$

This is the cumulative centered pair fluctuation。

---

# 7. Interface with the standard prime-pair error

Define：

$$
\boxed{
\psi_2(j,h)
=
\sum_{n=h+1}^{j}
\Lambda(n)\Lambda(n-h).
}
$$

Define standard Hardy–Littlewood pair error：

$$
\boxed{
r_j(h)
=
\psi_2(j,h)
-
\mathfrak S(h)(j-h).
}
$$

Also：

$$
\boxed{
E(x)
=
\psi(x)-x.
}
$$

Direct expansion gives：

## Theorem 7.1

$$
\boxed{
Q_j(h)
=
r_j(h)
-
E(j)
-
E(j-h)
+
E(h).
}
$$

This is the exact prime-pair interface。

---

# 8. Endpoint accumulation

v3.5 gives：

$$
\boxed{
\mathcal R_N(h)
=
\sum_{j=N}^{2N-1}
\mathbf1_{h<j}
Q_j(h).
}
$$

The centered shift variance is：

$$
\boxed{
\mathcal V_N
=
\sum_h
|
\mathcal R_N(h)
|^2.
}
$$

---

# 9. Endpoint Cauchy gate

For each fixed：

$$
h,
$$

there are at most：

$$
N
$$

endpoint terms。

Thus：

$$
\left|
\mathcal R_N(h)
\right|^2
\le
N
\sum_{j=N}^{2N-1}
\mathbf1_{h<j}
|Q_j(h)|^2.
$$

Summing over：

$$
h
$$

gives：

## Theorem 9.1 · Endpoint Pair Variance Reduction

$$
\boxed{
\mathcal V_N
\le
N
\sum_{j=N}^{2N-1}
\sum_{h=1}^{j-1}
|Q_j(h)|^2.
}
$$

---

# 10. Canonical prime gate

Define：

$$
\boxed{
\mathcal P_N
=
\sum_{j=N}^{2N-1}
\sum_{h=1}^{j-1}
|Q_j(h)|^2.
}
$$

## Definition 10.1 · EPV$(\eta)$

There exists：

$$
\eta>0
$$

such that：

$$
\boxed{
\mathcal P_N
\ll
N^{4-\eta+o(1)}.
}
$$

Then Theorem 9.1 gives：

$$
\boxed{
\mathcal V_N
\ll
N^{5-\eta+o(1)}.
}
$$

---

# 11. EPV immediately gives PNT mean-square progress

v3.5–v3.6 show that：

$$
\mathcal V_N
\ll
N^{5-\eta}
$$

implies：

$$
\boxed{
I(N)
=
\int_N^{2N}
|\psi(x)-x|^2dx
\ll
N^{3-\eta/2+o(1)}.
}
$$

Therefore：

$$
\boxed{
\Theta
\le
1-\frac{\eta}{4}.
}
$$

Thus：

## Theorem 11.1 · EPV Zero-Strip Gate

Any unconditional：

$$
\boxed{
\operatorname{EPV}(\eta),
\qquad
\eta>0,
}
$$

produces a genuine fixed zero strip。

This is why no known routine prime-correlation estimate can close EPV。

---

# 12. Relation to the deterministic closure

v3.15 has：

$$
\boxed{
\mathfrak M_{4,N}
\ll
N^{9/2+\varepsilon}.
}
$$

If one proves the more targeted：

## FPD$(\eta)$

$$
\boxed{
|\mathfrak E_{4,N}|
\ll
N^{5-\eta+o(1)},
}
$$

then：

$$
\boxed{
|\mathfrak Q_N|
\ll
N^{
5-\min(\eta,1/2)+o(1)
}.
}
$$

Hence：

$$
\boxed{
I(N)
\ll
N^{
3-\frac12
\min(\eta,1/2)
+o(1)
}.
}
$$

EPV is a stronger sufficient prime gate；FPD is the minimal post-v3.15 gate。

---

# 13. Chou–Haag–Huryn–Ledoan variance

For one endpoint：

$$
N,
$$

define：

$$
\boxed{
E_{\rm pair}(N)
=
\sum_{
1\le|h|\le N
}
\left[
\psi_2(N,h)
-
\mathfrak S(h)(N-|h|)
\right]^2.
}
$$

Chou–Haag–Huryn–Ledoan emphasize that obtaining upper bounds for this variance is extremely hard。

Their conjectural scale is：

$$
\boxed{
E_{\rm pair}(N)
\asymp
N^2(\log N)^2.
}
$$

They prove：

$$
\boxed{
E_{\rm pair}(N)
=
\Omega(
N^{1+2\Theta-\varepsilon}
)
}
$$

for every：

$$
\varepsilon>0.
$$

Thus a fixed-power upper bound on this standard pair variance already has zero-strip consequences。

---

# 14. GRH calibration

The same paper records that, assuming the Generalized Riemann Hypothesis for Dirichlet $L$-functions：

$$
\boxed{
E_{\rm pair}(N)
\ll
N^{5/2}
(\log N)^C
}
$$

for some constant：

$$
C.
$$

Under GRH, RH also gives：

$$
\boxed{
E(x)
\ll
x^{1/2}
(\log x)^2.
}
$$

Use Theorem 7.1。

Then：

$$
\begin{aligned}
\sum_{h<j}
|Q_j(h)|^2
&\ll
E_{\rm pair}(j)
\\
&\quad
+
j^2(\log j)^4.
\end{aligned}
$$

The first term dominates at power scale。

Therefore：

$$
\boxed{
\sum_{h<j}
|Q_j(h)|^2
\ll
j^{5/2}
(\log j)^{C'}.
}
$$

---

# 15. Conditional EPV exponent

Summing Section 14 over：

$$
N\le j<2N
$$

gives：

$$
\boxed{
\mathcal P_N
\ll
N^{7/2}
(\log N)^{C'}.
}
$$

Thus, conditionally：

$$
\boxed{
\eta_{\rm EPV}
=
\frac12
}
$$

up to logarithms。

Theorem 9.1 then gives：

$$
\boxed{
\mathcal V_N
\ll
N^{9/2}
(\log N)^{C'}.
}
$$

This matches the deterministic v3.15 exponent。

This is a **calibration only**；GRH cannot be used in an RH proof。

---

# 16. Trivial unconditional scale

A structure-blind estimate gives：

$$
|r_j(h)|
\ll
j(\log j)^2
$$

and hence：

$$
\sum_{h<j}
|Q_j(h)|^2
\ll
j^{3+o(1)}.
$$

Summing over：

$$
j\asymp N
$$

gives：

$$
\boxed{
\mathcal P_N
\ll
N^{4+o(1)}.
}
$$

Then：

$$
\boxed{
\mathcal V_N
\ll
N^{5+o(1)}.
}
$$

This is exactly the：

$$
\eta=0
$$

baseline。

---

# 17. Higher-uniformity input

Matomäki–Radziwiłł–Shao–Tao–Teräväinen prove for：

$$
\Lambda-\Lambda^\sharp
$$

strong higher-uniformity estimates on almost all short intervals。

For：

$$
H\ge
X^{1/3+\varepsilon},
$$

the nilsequence-correlation error has the form：

$$
\boxed{
H
(\log X)^{-A}
}
$$

for every fixed：

$$
A>0.
$$

They also obtain asymptotically small short-interval Gowers norms and Hardy–Littlewood patterns with a short average over one variable。

---

# 18. What higher uniformity gives here

The parallelogram pattern：

$$
r,
\quad
r+h,
\quad
r+d,
\quad
r+h+d
$$

is a finite-complexity linear system and is naturally controlled by Gowers-uniformity methods after the structured approximation：

$$
\Lambda^\sharp
$$

is removed。

Therefore these results strongly support control of the **pseudorandom component** of the four-point deviation。

However their published quantitative scale is：

$$
\boxed{
(\log N)^{-A}
}
$$

or：

$$
o(1),
$$

not：

$$
N^{-\eta}.
$$

After restoring the：

$$
N^5
$$

quartic weight scale, such bounds remain：

$$
\boxed{
N^{5-o(1)}
}
$$

at fixed-exponent resolution。

Thus：

```text
HIGHER UNIFORMITY
    = major method progress

FIXED ZERO-STRIP ETA
    = still zero
```

---

# 19. Why the parallelogram $U^2$ structure does not automatically solve the gate

The unweighted identity：

$$
\sum_{r,h,d}
f(r)
\overline{f(r+h)}
\overline{f(r+d)}
f(r+h+d)
$$

is a $U^2$ / fourth Fourier-moment object。

But for primes, the relevant Fourier square：

$$
|S(\alpha)|^2
$$

contains the full prime-pair spectrum。

Chou–Haag–Huryn–Ledoan write the pair-error variance exactly as an：

$$
L^2
$$

distance between：

$$
|S(\alpha)|^2
$$

and a singular-series / major-arc model。

Thus the special parallelogram Fourier structure **is exactly where the hard prime-pair variance already lives**。

It does not bypass that barrier。

---

# 20. Major-arc approximation barrier

For the Selberg-type approximation：

$$
\Lambda_R,
$$

Chou et al. record：

$$
\boxed{
\int_0^1
|
S(\alpha)-S_R(\alpha)
|^2d\alpha
=
N\log\left(
\frac NR
\right)
+
O(N).
}
$$

A related Ramanujan major-arc approximation：

$$
\lambda_R(n)
=
\sum_{q\le R}
\frac{\mu(q)}{\phi(q)}
c_q(-n)
$$

has controlled second moment only in the classical regime：

$$
R\le N^{1/2},
$$

up to the standard error terms。

This is another expression of the familiar：

$$
\sqrt N
$$

major-arc / large-sieve threshold。

---

# 21. Why current minor-arc technology is not enough by itself

Classical and modern exponential-sum estimates can give strong cancellation away from structured major arcs。

But the fixed-power EPV problem also requires quantitative control of the structured prime-pair approximation itself across endpoints and shifts。

That structured component is sensitive to Dirichlet $L$-function zeros and cannot be removed merely by a generic minor-arc supremum bound。

This is consistent with the GRH dependence of the best quoted pair-variance upper bound。

---

# 22. Actual-prime problem split

The remaining prime-specific research problem should be separated into：

## A. Four-point pseudorandom error

Control：

$$
\boxed{
T_{h,d}(r)
}
$$

after subtracting the refined four-point model。

Higher uniformity is the main current tool。

## B. Pair correction

Control：

$$
\boxed{
\mu_h
[
P_h(r)+P_h(r+d)
].
}
$$

Endpoint prime-pair variance is the natural current interface。

A proof of FPD must preserve cancellation between these pieces when appropriate。

---

# 23. Strong sufficient endpoint gate

The most concrete next theorem is：

## Integrated Endpoint Pair Variance $\operatorname{IEPV}(\eta)$

$$
\boxed{
\sum_{j=N}^{2N-1}
\sum_{h=1}^{j-1}
\left|
r_j(h)
-
E(j)
-
E(j-h)
+
E(h)
\right|^2
\ll
N^{4-\eta+o(1)}.
}
$$

This is exactly EPV written in standard arithmetic objects。

Any：

$$
\eta>0
$$

would close the first zero-strip gate。

---

# 24. More targeted four-point gate

A weaker theorem than EPV may still suffice：

## Four-Point Prime Deviation $\operatorname{FPD}(\eta)$

$$
\boxed{
\left|
\sum_{r,h,d}
W_N(r,h,d)
\left\{
T_{h,d}(r)
-
\mu_h[
P_h(r)+P_h(r+d)
]
\right\}
\right|
\ll
N^{5-\eta+o(1)}.
}
$$

This preserves the exact signed three-parameter cancellation and is therefore the canonical **minimal** post-v3.15 target。

---

# 25. Current literature strength audit

### Published / established

- deterministic singular-series geometry：
  closed in AMRAL v3.15 at：
  $$
  N^{9/2+\varepsilon};
  $$
- higher uniformity of：
  $$
  \Lambda-\Lambda^\sharp
  $$
  with arbitrary log-power saving；
- Hardy–Littlewood patterns with averaged variables；
- conditional GRH prime-pair variance：
  $$
  N^{5/2}\operatorname{polylog}N.
  $$

### Not currently available

- unconditional：
  $$
  E_{\rm pair}(N)
  \ll
  N^{3-\eta}
  $$
  for any fixed：
  $$
  \eta>0;
  $$
- unconditional EPV$(\eta)$；
- unconditional FPD$(\eta)$。

Therefore：

$$
\boxed{
\eta_{\rm prime}=0
}
$$

remains the rigorous state of the actual-prime branch。

---

# 26. Strategic interpretation

The fifth arc has now separated three fundamentally different layers：

```text
LOCAL CONGRUENCE MODEL
    solved at fixed power

PSEUDORANDOM PRIME PART
    strong log-power control

STRUCTURED PRIME ERROR
    fixed-power barrier open
```

So future agents should not continue improving the deterministic singular-series model unless a prime-specific proof requires it。

The main target is now an actual-prime variance / structured approximation theorem。

---

# 27. False-progress gates

Reject：

### F1 · Log-power pseudorandom saving

$$
N^5(\log N)^{-A}
$$

still has fixed exponent：

$$
5.
$$

### F2 · GRH pair-variance bound used inside an RH proof

Circular / conditional calibration only。

### F3 · Minor-arc fixed power alone

Must also control structured major-arc pair error。

### F4 · Deterministic $\eta_M=1/2$ promoted to prime $\eta_Q$

Actual-prime deviation is additive and unresolved。

### F5 · Generic four-linear Hardy–Littlewood asymptotic

An：

$$
o(1)
$$

relative error is not automatically：

$$
N^{-\eta}.
$$

---

# 28. Autonomous candidate schema

Every prime-side candidate should record：

```text
target
    EPV / FPD / four-point pseudorandom / pair correction

structured approximant
    Lambda^sharp / Lambda_R / lambda_R / other

quantitative saving
    log^(-A) / o(1) / N^(-eta)

endpoint averaging
    yes / no

shift averaging
    yes / no

major-arc error controlled
    yes / no

exceptional-character / zero sensitivity
    yes / no

translation to eta_Q
translation to kappa_I
```

Only a proved：

$$
N^{-\eta}
$$

gain counts as fixed zero-strip progress。

---

# 29. Suggested v3.17 direction

Recommended：

`RH-PrimeStructuredApproximationGap v3.17`

Do not return to deterministic geometry。

Tasks：

1. choose a canonical prime approximant：
   $$
   \lambda_R
   $$
   or：
   $$
   \Lambda^\sharp;
   $$
2. decompose：
   $$
   P_h(r)
   $$
   and：
   $$
   T_{h,d}(r)
   $$
   into structured / pseudorandom pieces；
3. use higher uniformity to remove every term containing at least one pseudorandom factor at logarithmic strength；
4. identify the all-structured residual exactly；
5. express that residual in Dirichlet-character / major-arc data；
6. determine which character-zero estimate would imply EPV$(\eta)$；
7. compare this with Chou et al.'s GRH：
   $$
   N^{5/2}
   $$
   variance；
8. isolate the weakest non-GRH character theorem sufficient for any：
   $$
   \eta>0.
   $$

This is now the canonical actual-prime continuation。

---

# 30. GAP ledger

## CLOSED / REDUCED

### G1. Local FPD identity

```text
CLOSED
```

### G2. Endpoint pair interface

```text
CLOSED
```

### G3. EPV sufficient gate

```text
CLOSED_AS_REDUCTION
```

### G4. Deterministic model

```text
eta_M = 1/2
```

### G5. Higher-uniformity method class

```text
LOG-POWER ONLY AT FIXED-EXPONENT AUDIT
```

---

## OPEN

### G6. EPV$(\eta>0)$

```text
OPEN
```

### G7. FPD$(\eta>0)$

```text
OPEN
```

### G8. Complete quartic：

$$
\eta_Q>0
$$

```text
OPEN
```

### G9. PNT mean-square：

$$
\kappa_I>0
$$

```text
OPEN
```

### G10. RH

```text
OPEN
```

---

# 31. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DETERMINISTIC eta_M = 1/2
ACTUAL PRIME eta = 0 PROVED

GRH eta=1/2
    = CONDITIONAL CALIBRATION ONLY

HIGHER UNIFORMITY LOG SAVING
    !=
FIXED POWER SAVING

NO NEW ZERO STRIP IN V3.16

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\text{GRH pair variance}
\Longrightarrow
\text{unconditional EPV}.
$$

Forbidden：

$$
\log^{-A}N
\Longrightarrow
N^{-\eta}.
$$

Forbidden：

$$
\mathfrak M_{4,N}
\ll
N^{9/2}
\Longrightarrow
\mathfrak Q_N
\ll
N^{9/2}.
$$

---

# 32. One-line status

> v3.16 begins the actual-prime phase after the deterministic refined-singular-series model was closed at $N^{9/2+\varepsilon}$. Writing $a_n=\Lambda(n)-1$, the pointwise pair fluctuation is $P_h(r)=a_ra_{r+h}-(\mathfrak S(h)-1)$ and the genuine four-point error is $T_{h,d}(r)=a_ra_{r+h}a_{r+d}a_{r+h+d}-\mathfrak S_0(0,h,d,h+d)$. The exact identity $P_h(r)P_h(r+d)-\mathfrak K_4(h,d)=T_{h,d}(r)-(\mathfrak S(h)-1)[P_h(r)+P_h(r+d)]$ splits the remaining prime deviation into a genuine four-linear pattern error plus pair-error corrections. At endpoint level, $Q_j(h)=r_j(h)-E(j)-E(j-h)+E(h)$ and the total centered shift variance satisfies $\mathcal V_N\le N\sum_{j\asymp N}\sum_{h<j}|Q_j(h)|^2$. Thus any fixed saving EPV$(\eta)$ on this integrated endpoint pair variance immediately yields $\mathcal V_N\ll N^{5-\eta}$ and a fixed zeta zero strip. Chou–Haag–Huryn–Ledoan show why this is deep: even assuming GRH for Dirichlet $L$-functions their standard prime-pair error variance is only bounded by $N^{5/2}\operatorname{polylog}N$, which corresponds after endpoint accumulation to the conditional EPV scale $\eta=1/2$. Modern higher-uniformity results for $\Lambda-\Lambda^\sharp$ provide extremely strong logarithmic savings and averaged Hardy–Littlewood patterns, but not a fixed $N^{-\eta}$ gain. The special parallelogram/$U^2$ structure does not bypass the problem because the standard prime-pair variance itself is an $L^2$ discrepancy of $|S(\alpha)|^2$ from its singular-series major-arc model. The rigorous unconditional actual-prime state therefore remains $\eta=0$. The next node should split the prime variables into structured and pseudorandom approximants and isolate the exact major-arc/character estimate whose fixed-power improvement would close EPV or the weaker FPD gate.

---

# 33. References

1. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   arXiv: https://arxiv.org/abs/2308.14888

2. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   arXiv: https://arxiv.org/abs/2411.05770

3. Kaisa Matomäki, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals I. All intervals**, *Forum of Mathematics, Pi* 11 (2023), e29.  
   arXiv: https://arxiv.org/abs/2204.03754

4. AMRAL, **RH-AxisFree-MixedRamanujanTail v3.15**.

5. AMRAL, **RH-MeanSquare-ArithmeticGap v3.5**.

---

# 34. Provenance

研究主導：Neo.K

v3.16 exact actual-prime deviation identity、endpoint pair-variance reduction、GRH calibration、higher-uniformity strength audit、prime-side gate architecture、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 actual-prime deviation / structured-prime variance gate。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
