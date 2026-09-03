工程紀錄 · 第五弧線 v3.5 · 2026-09-03 · ARITHMETIC_MEANSQUARE_GAP · SINGULAR_SERIES_CENTERING · OFFDIAGONAL_GATE · RH_CLAIM_FALSE

# Mean-Square Arithmetic Gap：Singular-Series Centering 與第一個真正 Off-Diagonal Power-Saving Gate

**RH-MeanSquare-ArithmeticGap v3.5**

本節點承接：

- `RH-PositiveKernel-SelbergComparison v3.4`
- `RH-FilteredPNT-GallagherStrengthAudit v2.0`
- `RH-TwistedLocalCorrelation-ExponentDrop v2.1`

v3.4 已達成：

```text
REPRESENTATION CLOSURE
```

在 fixed-exponent 層：

$$
\text{AMRAL positive Cauchy energy}
\asymp
\text{classical normalized PNT mean square}.
$$

因此 v3.5 停止尋找新的 RH-equivalent representation，固定 arithmetic target：

$$
\boxed{
I(X)
=
\int_X^{2X}
|\psi(x)-x|^2dx
\ll
X^{3-\kappa+o(1)}
}
$$

for any：

$$
\boxed{
\kappa>0.
}
$$

本輪主要成果是把 $I(X)$ 在 prime side exact 展開，並 isolate 第一個真正需要 power saving 的 arithmetic remainder。

核心結論：

1. direct prime expansion 的 diagonal 僅：
   $$
   O(N^2\log N),
   $$
   所以第一個 fixed-power barrier不是 diagonal；
2. raw off-diagonal shift variance也不是正確 target，因為它含有 deterministic Hardy–Littlewood singular-series backbone；
3. subtract：
   $$
   [\mathfrak S(h)-1]W_N(h)
   $$
   後，singular-series aggregate總和只有：
   $$
   O(N^2\log N);
   $$
4. 真正 canonical arithmetic remainder是 centered signed Cesàro shift residual：
   $$
   \mathcal R_N(h);
   $$
5. first minimal signed gap：
   $$
   \boxed{
   \left|
   \sum_h\mathcal R_N(h)
   \right|
   \ll
   N^{3-\kappa}
   }
   $$
   直接推出 fixed zero-strip progress；
6. 一個較強、但適合 $L^2$/dispersion 工具的 sufficient gate是：
   $$
   \boxed{
   \sum_h|\mathcal R_N(h)|^2
   \ll
   N^{5-\eta}
   }
   $$
   for any $\eta>0$，其對應：
   $$
   \boxed{
   \kappa=\frac{\eta}{2}.
   }
   $$
7. 2026 Chou–Haag–Huryn–Ledoan 的 prime-pair error variance提供另一個獨立 additive gate：
   $$
   E_{\rm pair}(N)
   \ll
   N^{3-\eta}
   \Longrightarrow
   \Theta\le1-\frac{\eta}{2}.
   $$

所以 v3.5 正式把主線從：

```text
find a better representation
```

切成：

```text
prove a power saving for a singular-series-centered
off-diagonal arithmetic correlation.
```

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

DISCRETE_PNT_MEANSQUARE_IDENTITY = CLOSED
DISCRETE_CONTINUOUS_EXPONENT_EQUIVALENCE = CLOSED

DIRECT_PRIME_PAIR_EXPANSION = CLOSED
DIAGONAL_SIZE = O(N^2 log N)

RAW_SHIFT_VARIANCE_AS_TARGET = REJECTED
REASON = SINGULAR_SERIES_BACKBONE

SINGULAR_SERIES_AGGREGATE = O(N^2 log N)
CENTERED_SHIFT_RESIDUAL = DEFINED

MINIMAL_SIGNED_AGGREGATE_GATE = CLOSED_AS_REDUCTION
SHIFT_L2_GATE = CLOSED_AS_SUFFICIENT_REDUCTION

TRIVIAL_SHIFT_L2_EXPONENT = 5
ANY_SHIFT_L2_POWER_SAVING_ETA_POSITIVE = FIXED_STRIP_PROGRESS
KAPPA_FROM_SHIFT_L2 = ETA / 2

CHOU_PAIR_VARIANCE_GATE = EXTERNAL_CONFIRMED_ROUTE
ZERO_DENSITY_ALONE = INSUFFICIENT_FOR_ONE_RIGHTMOST_ZERO

ARITHMETIC_KAPPA_POSITIVE = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Integer-scale normalization

Let：

$$
N\in\mathbb N.
$$

Define：

$$
\boxed{
a_n
=
\Lambda(n)-1.
}
$$

Define the centered prime partial sum：

$$
\boxed{
A(j)
=
\sum_{n\le j}a_n
=
\psi(j)-j.
}
$$

Set：

$$
\boxed{
J_N
=
\sum_{j=N}^{2N-1}A(j)^2.
}
$$

---

# 2. Exact discrete–continuous identity

For：

$$
x=j+r,
\qquad
0\le r<1,
$$

we have：

$$
\psi(x)=\psi(j),
$$

so：

$$
\psi(x)-x
=
A(j)-r.
$$

Therefore：

$$
\int_j^{j+1}
|\psi(x)-x|^2dx
=
A(j)^2-A(j)+\frac13.
$$

Summing：

## Theorem 2.1

$$
\boxed{
I(N)
=
J_N
-
\sum_{j=N}^{2N-1}A(j)
+
\frac N3.
}
$$

This is exact.

---

# 3. Fixed-exponent equivalence of $I(N)$ and $J_N$

By Cauchy–Schwarz：

$$
\boxed{
\left|
\sum_{j=N}^{2N-1}A(j)
\right|
\le
N^{1/2}J_N^{1/2}.
}
$$

Hence：

$$
I(N)
=
J_N
+
O(
N^{1/2}J_N^{1/2}
+
N
).
$$

Conversely Theorem 2.1 gives：

$$
J_N
\le
I(N)
+
N^{1/2}J_N^{1/2}
+
N.
$$

Solving the quadratic inequality in：

$$
J_N^{1/2}
$$

gives：

$$
\boxed{
J_N
\ll
I(N)+N.
}
$$

Therefore for every exponent：

$$
\delta>1,
$$

$$
\boxed{
I(N)\ll N^\delta
\Longleftrightarrow
J_N\ll N^\delta
}
$$

at exponent level.

---

# 4. Endpoint multiplicity weight

Expand：

$$
J_N
=
\sum_{j=N}^{2N-1}
\sum_{m,n\le j}
a_ma_n.
$$

For a fixed pair $(m,n)$, the number of endpoints $j$ contributing is：

$$
\boxed{
w_N(\max(m,n)),
}
$$

where：

$$
\boxed{
w_N(r)
=
\begin{cases}
N,
&
1\le r\le N,
\\
2N-r,
&
N<r<2N,
\\
0,
&
r\ge2N.
\end{cases}
}
$$

Hence：

$$
\boxed{
J_N
=
\sum_{m,n<2N}
a_ma_n
w_N(\max(m,n)).
}
$$

---

# 5. Diagonal plus additive shifts

Separate：

$$
m=n
$$

from：

$$
m\ne n.
$$

Define：

$$
\boxed{
D_N
=
\sum_{n<2N}
w_N(n)a_n^2.
}
$$

For：

$$
1\le h\le2N-2,
$$

define：

$$
\boxed{
\mathcal C_N(h)
=
\sum_{n=h+1}^{2N-1}
w_N(n)
a_n
a_{n-h}.
}
$$

Then：

## Theorem 5.1 · Exact additive expansion

$$
\boxed{
J_N
=
D_N
+
2
\sum_{h=1}^{2N-2}
\mathcal C_N(h).
}
$$

---

# 6. The diagonal is not the first power barrier

Classically：

$$
\sum_{n\le x}
\Lambda(n)^2
=
x\log x+O(x).
$$

Therefore：

$$
\sum_{n<2N}
a_n^2
=
O(N\log N).
$$

Since：

$$
0\le w_N(n)\le N,
$$

we have：

## Theorem 6.1

$$
\boxed{
D_N
=
O(N^2\log N).
}
$$

Thus for any first-strip target：

$$
0<\kappa<1,
$$

$$
D_N
=
o(N^{3-\kappa}).
$$

So the direct arithmetic obstruction lies in the off-diagonal aggregate.

---

# 7. Why raw off-diagonal $L^2$ is the wrong target

Hardy–Littlewood predicts：

$$
\sum_{n\le x}
\Lambda(n)\Lambda(n-h)
\sim
\mathfrak S(h)x
$$

after the appropriate endpoint correction.

Since：

$$
a_n=\Lambda(n)-1,
$$

the natural centered pair backbone is：

$$
\boxed{
\mathfrak S(h)-1.
}
$$

For odd $h$：

$$
\mathfrak S(h)=0,
$$

so the backbone is：

$$
-1.
$$

For even $h$ it fluctuates arithmetically around mean $1$.

Hence raw：

$$
\mathcal C_N(h)
$$

is typically of order：

$$
N^2
$$

from deterministic singular-series structure alone.

Squaring over $O(N)$ shifts naturally produces the trivial：

$$
N^5
$$

scale even in an ideal Hardy–Littlewood world.

So：

$$
\boxed{
\sum_h|\mathcal C_N(h)|^2
}
$$

is not the correct residual variance.

---

# 8. Combinatorial shift mass

Define：

$$
\boxed{
W_N(h)
=
\sum_{n=h+1}^{2N-1}
w_N(n).
}
$$

Equivalently：

$$
\boxed{
W_N(h)
=
\sum_{j=N}^{2N-1}
(j-h)_+.
}
$$

Explicitly：

$$
\boxed{
W_N(h)
=
\begin{cases}
N(N-h)+\frac{N(N-1)}2,
&
0\le h\le N,
\\
\frac{
(2N-h-1)(2N-h)
}{2},
&
N<h\le2N-2.
\end{cases}
}
$$

---

# 9. Singular-series-centered shift residual

Define：

$$
\boxed{
\mathcal R_N(h)
=
\mathcal C_N(h)
-
[
\mathfrak S(h)-1
]
W_N(h).
}
$$

This is the canonical v3.5 arithmetic shift residual.

It removes the deterministic two-prime local-density backbone before any absolute value or square is taken.

---

# 10. Cesàro singular-series aggregate

Define：

$$
\boxed{
\mathcal M_N
=
\sum_{h=1}^{2N-2}
[
\mathfrak S(h)-1
]
W_N(h).
}
$$

Using：

$$
W_N(h)
=
\sum_{j=N}^{2N-1}
(j-h)_+,
$$

we obtain：

$$
\boxed{
\mathcal M_N
=
\sum_{j=N}^{2N-1}
\sum_{h=1}^{j-1}
(j-h)
[
\mathfrak S(h)-1
].
}
$$

---

# 11. Average singular-series input

A classical Cesàro average used in the prime-pair literature is：

$$
\boxed{
\sum_{1\le|h|\le x}
(x-|h|)
\mathfrak S(h)
=
x^2
+
O(x\log x).
}
$$

Because：

$$
\mathfrak S(-h)=\mathfrak S(h),
$$

this gives：

$$
2
\sum_{h=1}^{x-1}
(x-h)
[
\mathfrak S(h)-1
]
=
O(x\log x).
$$

Therefore：

## Theorem 11.1

$$
\boxed{
\mathcal M_N
=
O(N^2\log N).
}
$$

So the full singular-series backbone is also below every first fixed-power target：

$$
N^{3-\kappa},
\qquad
0<\kappa<1.
$$

---

# 12. Exact arithmetic remainder identity

Substitute：

$$
\mathcal C_N(h)
=
[
\mathfrak S(h)-1
]W_N(h)
+
\mathcal R_N(h)
$$

into Theorem 5.1.

Then：

## Theorem 12.1 · Canonical arithmetic remainder

$$
\boxed{
J_N
=
D_N
+
2\mathcal M_N
+
2
\sum_{h=1}^{2N-2}
\mathcal R_N(h).
}
$$

Since：

$$
D_N+\mathcal M_N
=
O(N^2\log N),
$$

we have：

$$
\boxed{
J_N
=
2
\sum_h
\mathcal R_N(h)
+
O(N^2\log N).
}
$$

This is the v3.5 representation-closed prime-side identity.

---

# 13. Minimal signed arithmetic gap

Fix：

$$
0<\kappa<1.
$$

If one proves：

$$
\boxed{
\left|
\sum_{h=1}^{2N-2}
\mathcal R_N(h)
\right|
\ll
N^{3-\kappa+o(1)},
}
$$

then Theorem 12.1 gives：

$$
J_N
\ll
N^{3-\kappa+o(1)}.
$$

By Section 3：

$$
\boxed{
I(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

Hence：

$$
\boxed{
\Theta
\le
1-\frac{\kappa}{2}.
}
$$

This is the **minimal signed aggregate gate** of v3.5.

It asks only for cancellation after：

- endpoint averaging；
- shift summation；
- singular-series centering。

It does **not** require every individual shift to be accurately estimated.

---

# 14. Shift-$L^2$ sufficient gate

Define：

$$
\boxed{
\mathcal V_N
=
\sum_{h=1}^{2N-2}
|
\mathcal R_N(h)
|^2.
}
$$

By Cauchy–Schwarz：

$$
\boxed{
\left|
\sum_h
\mathcal R_N(h)
\right|
\le
(2N)^{1/2}
\mathcal V_N^{1/2}.
}
$$

Therefore：

## Theorem 14.1 · Shift variance gate

If：

$$
\boxed{
\mathcal V_N
\ll
N^{5-\eta+o(1)}
}
$$

for some fixed：

$$
\eta>0,
$$

then：

$$
\boxed{
I(N)
\ll
N^{3-\eta/2+o(1)}.
}
$$

Thus：

$$
\boxed{
\kappa
=
\frac{\eta}{2}.
}
$$

and：

$$
\boxed{
\Theta
\le
1-\frac{\eta}{4}.
}
$$

---

# 15. Trivial shift-$L^2$ exponent

By Cauchy：

$$
\sum_n
|a_na_{n-h}|
\le
\left(
\sum a_n^2
\right)^{1/2}
\left(
\sum a_{n-h}^2
\right)^{1/2}
\ll
N\log N.
$$

Since：

$$
w_N\le N,
$$

$$
\mathcal C_N(h)
\ll
N^2\log N.
$$

The singular-series main term is also：

$$
N^{2+o(1)}.
$$

Hence：

$$
\boxed{
\mathcal R_N(h)
\ll
N^{2+o(1)}.
}
$$

Summing $O(N)$ squares gives：

$$
\boxed{
\mathcal V_N
\ll
N^{5+o(1)}.
}
$$

So any fixed：

$$
\eta>0
$$

in Theorem 14.1 is genuinely nontrivial arithmetic progress.

---

# 16. Why the $L^2$ gate is stronger than the minimal gate

The minimal gate preserves signed cancellation over shifts：

$$
\sum_h\mathcal R_N(h).
$$

The $L^2$ gate replaces this by：

$$
\sum_h|\mathcal R_N(h)|^2
$$

and pays a Cauchy factor：

$$
N^{1/2}.
$$

Thus it is easier to interface with：

- dispersion；
- Parseval；
- large sieve；
- pair-error variance；

but it may be too expensive for the full RH scale.

So：

```text
SHIFT L2 GATE
    good for first fixed-strip progress

SIGNED AGGREGATE GATE
    canonical for deeper cancellation
```

---

# 17. Endpoint pair residual

For：

$$
h<j,
$$

define the centered endpoint correlation：

$$
\boxed{
Q_j(h)
=
\sum_{n=h+1}^{j}
a_na_{n-h}
-
[
\mathfrak S(h)-1
]
(j-h).
}
$$

Then：

$$
\boxed{
\mathcal R_N(h)
=
\sum_{j=N}^{2N-1}
\mathbf1_{h<j}
Q_j(h).
}
$$

So $\mathcal R_N$ is an endpoint-Cesàro accumulation of centered pair residuals.

---

# 18. Exact interface with Hardy–Littlewood prime-pair error

Define：

$$
\boxed{
r_j(h)
=
\psi_2(j,h)
-
\mathfrak S(h)(j-h),
}
$$

where：

$$
\psi_2(j,h)
=
\sum_{n=h+1}^{j}
\Lambda(n)\Lambda(n-h).
$$

Let：

$$
E(x)
=
\psi(x)-x.
$$

Expanding：

$$
a_n=\Lambda(n)-1
$$

gives the exact identity：

## Theorem 18.1

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

So the AMRAL centered-shift residual is directly coupled to the standard Hardy–Littlewood pair error plus three PNT-error boundary terms.

This is the precise interface with prime-pair literature.

---

# 19. Chou–Haag–Huryn–Ledoan pair-error variance

Define：

$$
\boxed{
E_{\rm pair}(N)
=
\sum_{1\le|k|\le N}
\left[
\psi_2(N,k)
-
\mathfrak S(k)
(N-|k|)
\right]^2.
}
$$

Their 2026 Journal of Number Theory paper proves：

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

Therefore：

## Gate 19.1 · External prime-pair variance gate

If for some：

$$
\eta>0
$$

one could prove：

$$
\boxed{
E_{\rm pair}(N)
\ll
N^{3-\eta},
}
$$

then necessarily：

$$
\boxed{
\Theta
\le
1-\frac{\eta}{2}.
}
$$

This is an independent published additive-prime route to a fixed zero strip.

Their conjectured：

$$
E_{\rm pair}(N)
\asymp
N^2(\log N)^2
$$

is RH-strength and they explicitly note that it implies RH.

---

# 20. Comparison of the three arithmetic gates

## Gate A · Minimal signed aggregate

$$
\boxed{
\left|
\sum_h
\mathcal R_N(h)
\right|
\ll
N^{3-\kappa}.
}
$$

Strength：

```text
closest to exact I(N) target
preserves all shift cancellation
```

---

## Gate B · Shift residual variance

$$
\boxed{
\sum_h
|\mathcal R_N(h)|^2
\ll
N^{5-\eta}.
}
$$

Translation：

$$
\boxed{
\kappa=\eta/2.
}
$$

Strength：

```text
stronger than Gate A
better analytic-tool interface
```

---

## Gate C · Standard prime-pair error variance

$$
\boxed{
E_{\rm pair}(N)
\ll
N^{3-\eta}.
}
$$

Published zero-strip consequence：

$$
\boxed{
\Theta\le1-\eta/2.
}
$$

Strength：

```text
standard additive-prime object
strong theorem
already known to be very difficult
```

---

# 21. Fourier / exponential-sum interface

Define：

$$
\boxed{
F_N(\alpha)
=
\sum_{n<2N}
a_ne(n\alpha),
}
$$

and：

$$
\boxed{
G_N(\alpha)
=
\sum_{n<2N}
w_N(n)a_ne(n\alpha).
}
$$

Then：

$$
G_N(\alpha)
\overline{
F_N(\alpha)
}
$$

has positive Fourier coefficient at shift $h$ equal to：

$$
\boxed{
\mathcal C_N(h).
}
$$

Define the positive-frequency singular-series model：

$$
\boxed{
M_N^+(\alpha)
=
\sum_{h=1}^{2N-2}
[
\mathfrak S(h)-1
]
W_N(h)
e(h\alpha).
}
$$

Let：

$$
P_+
$$

denote projection onto positive Fourier frequencies.

Then：

## Theorem 21.1

$$
\boxed{
\sum_{h=1}^{2N-2}
\mathcal R_N(h)e(h\alpha)
=
P_+
\left[
G_N\overline F_N
\right]
-
M_N^+(\alpha).
}
$$

Therefore Parseval gives：

$$
\boxed{
\mathcal V_N
=
\int_0^1
\left|
P_+
[
G_N\overline F_N
]
-
M_N^+(\alpha)
\right|^2d\alpha.
}
$$

This is the exact exponential-sum form of the Shift-$L^2$ Gate.

---

# 22. What the first new theorem would actually have to say

A genuine v3.5 advance can now be one of：

### Type 1 · Signed aggregate cancellation

Prove directly：

$$
\sum_h\mathcal R_N(h)
=
O(N^{3-\kappa}).
$$

### Type 2 · Quartic Fourier saving

Prove：

$$
\left\|
P_+[
G_N\overline F_N
]
-
M_N^+
\right\|_2^2
\ll
N^{5-\eta}.
$$

### Type 3 · Prime-pair variance saving

Prove：

$$
E_{\rm pair}(N)
\ll
N^{3-\eta}.
$$

All three are genuine number theory.

No new kernel representation is required.

---

# 23. Why generic Montgomery–Vaughan does not close Gate B

Generic Dirichlet-polynomial mean value controls quadratic norms of one polynomial.

Gate B is a **centered quartic** object：

$$
G_N\overline F_N
-
M_N^+.
$$

Applying coefficient-blind quadratic estimates before subtracting the singular-series model sees：

- the large deterministic pair backbone；
- generic close log-frequency spacing；
- no Hardy–Littlewood cancellation。

Thus generic Montgomery–Vaughan / large-sieve estimates remain structural transfer tools, not the missing arithmetic theorem.

The model subtraction must occur before taking the decisive norm.

---

# 24. Zero-side audit

The rightmost-zero exponent remains：

$$
\boxed{
1+2\Theta.
}
$$

Zaccagnini proved that a bound：

$$
J(x,1)
\ll
x^\delta,
\qquad
2\le\delta\le3,
$$

implies：

$$
\boxed{
\Theta
\le
\frac{\delta-1}{2}.
}
$$

Brent–Platt–Trudgian's RH analysis expands the mean square into a convergent double-zero correlation whose kernel depends on：

$$
\gamma_1-\gamma_2.
$$

Thus：

- pairwise zero correlations matter for sharp constants；
- but one rightmost off-axis zero already fixes the exponential class；
- zero-density information that permits one exceptional rightmost zero cannot by itself give $\kappa>0$.

---

# 25. Why the diagonal-barrier language must now be qualified

Earlier transformed formulations encountered a generic mean-value / spacing barrier which looked diagonal-like.

The direct centered prime expansion shows a sharper arithmetic fact：

$$
\boxed{
D_N
=
O(N^2\log N).
}
$$

Therefore at the classical $I(N)$ level：

```text
FIRST POWER-SAVING BARRIER
    = OFF-DIAGONAL CENTERED CORRELATION

NOT
    = PRIME SELF-DIAGONAL.
```

The two statements are not contradictory.

They refer to different representations before and after arithmetic centering.

This distinction should be preserved in future autonomous audits.

---

# 26. False-progress gates

Reject：

### F1 · Uncentered shift variance

$$
\sum_h|\mathcal C_N(h)|^2
$$

without subtracting：

$$
[\mathfrak S(h)-1]W_N(h).
$$

Reason：

```text
deterministic singular-series backbone.
```

### F2 · Logarithmic saving

$$
N^5/(\log N)^A
$$

does not change fixed exponent.

### F3 · Diagonal improvement only

Diagonal already lies below the first fixed-strip threshold.

### F4 · Zero-density only

Unless it excludes every zero to the right of a fixed line.

### F5 · Numerical shift variance

Finite $N$ is evidence only.

---

# 27. Autonomous progress metric

For Gate B define：

$$
\boxed{
\eta_{\rm shift}
=
5
-
\limsup
\frac{
\log\mathcal V_N
}{
\log N
}.
}
$$

Then：

$$
\boxed{
\eta_{\rm shift}>0
}
$$

is a rigorous arithmetic breakthrough.

Its guaranteed mean-square saving is：

$$
\boxed{
\kappa
\ge
\frac{
\eta_{\rm shift}
}{2}.
}
$$

For the direct target define：

$$
\boxed{
\kappa_I
=
3
-
\limsup
\frac{
\log I(N)
}{
\log N
}.
}
$$

The research optimizer should maximize a **proved** lower bound on：

$$
\kappa_I.
$$

---

# 28. Candidate engineering schema

Every arithmetic candidate should record：

```text
target gate
    A / B / C

singular-series subtraction
    yes / no

aperture normalization
    if relevant

raw exponent
corrected exponent

arithmetic input used
    zero density
    dispersion
    pair correlation
    bilinear form
    exponential sum
    sieve
    other

whether one exceptional zero remains possible

translation to kappa
```

Candidates without a fixed positive exponent gain should remain：

```text
METHOD IMPROVEMENT
```

not：

```text
ZERO-STRIP PROGRESS.
```

---

# 29. Suggested v3.6 direction

Recommended：

`RH-CenteredShift-FourierGap v3.6`

Do not introduce a new RH criterion.

Work directly on Gate B：

$$
\mathcal V_N
=
\left\|
P_+[
G_N\overline F_N
]
-
M_N^+
\right\|_2^2.
$$

Tasks：

1. expand the quartic integral；
2. separate major-arc singular-series contribution before taking absolute values；
3. identify diagonal quadruples and genuinely off-diagonal quadruples；
4. test whether additive-energy / dispersion tools give any:
   $$
   N^{5-\eta}
   $$
   saving；
5. compare the exact model with Chou et al.'s：
   $$
   |S(\alpha)|^2-V_y(\alpha);
   $$
6. identify which part of their major-arc approximation can be reused；
7. test bilinear decompositions of $\Lambda$ only after model subtraction；
8. reject every bound that returns merely：
   $$
   N^{5-o(1)}.
   $$

This is now a direct arithmetic attack.

---

# 30. GAP ledger

## CLOSED / REDUCED

### G1. Discrete–continuous mean-square bridge

```text
CLOSED
```

### G2. Exact additive-shift expansion

```text
CLOSED
```

### G3. Diagonal scale

```text
CLOSED
```

$$
O(N^2\log N).
$$

### G4. Singular-series backbone subtraction

```text
CLOSED
```

### G5. Singular-series aggregate lower order

```text
CLOSED
```

$$
O(N^2\log N).
$$

### G6. Minimal signed aggregate gate

```text
CLOSED_AS_REDUCTION
```

### G7. Shift-$L^2$ gate

```text
CLOSED_AS_SUFFICIENT_REDUCTION
```

### G8. Prime-pair error variance external gate

```text
AUDITED
```

---

## OPEN

### G9. Any：

$$
\eta_{\rm shift}>0
$$

```text
OPEN
```

### G10. Any：

$$
\kappa_I>0
$$

```text
OPEN
```

### G11. RH-scale：

$$
\kappa_I=1
$$

```text
OPEN_RH_COMPLETE
```

### G12. RH

```text
OPEN
```

---

# 31. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

ALL EXACT DECOMPOSITIONS ABOVE
    = ALGEBRAIC / CLASSICAL INPUT

SINGULAR-SERIES AGGREGATE BOUND
    = USES KNOWN CESARO AVERAGE

CHOU PAIR-VARIANCE CONSEQUENCE
    = EXTERNAL PUBLISHED RESULT

NO ETA_SHIFT > 0 HAS BEEN PROVED HERE
NO KAPPA > 0 HAS BEEN PROVED HERE

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\mathcal V_N
=
N^{5-o(1)}
\Longrightarrow
\kappa>0.
$$

Forbidden：

$$
\text{small diagonal}
\Longrightarrow
\text{off-diagonal solved}.
$$

Forbidden：

$$
\text{Hardy–Littlewood model subtracted numerically}
\Longrightarrow
\text{tail theorem}.
$$

---

# 32. One-line status

> v3.5 marks the transition from representation engineering to direct arithmetic attack. For integer $N$, the classical PNT mean square is exponent-equivalent to the discrete sum $J_N=\sum_{j=N}^{2N-1}(\psi(j)-j)^2$. Expanding with $a_n=\Lambda(n)-1$ gives an exact diagonal-plus-shifts formula. The prime self-diagonal is only $O(N^2\log N)$ and is therefore already below every first fixed-strip target; the $N^3$ barrier lies in the off-diagonal aggregate. Raw shift variance is nevertheless the wrong object because each shift carries the deterministic Hardy–Littlewood backbone $\mathfrak S(h)-1$. After subtracting this backbone with its exact endpoint mass $W_N(h)$, its total Cesàro contribution is only $O(N^2\log N)$ by the classical average singular-series formula. The remaining centered residual $\mathcal R_N(h)$ satisfies $J_N=2\sum_h\mathcal R_N(h)+O(N^2\log N)$. Thus the minimal signed arithmetic lemma is any fixed power saving on $\sum_h\mathcal R_N(h)$. A stronger $L^2$ surrogate, $\sum_h|\mathcal R_N(h)|^2\ll N^{5-\eta}$, gives $\kappa=\eta/2$ and a fixed zero strip. This variance is exactly the $L^2$ norm of a singular-series-centered quartic exponential-sum discrepancy. Independently, the 2026 Chou–Haag–Huryn–Ledoan prime-pair error variance obeys an $\Omega(N^{1+2\Theta-\varepsilon})$ lower bound, so any upper bound $N^{3-\eta}$ for that standard additive object also yields a fixed zero strip. No such positive power saving is proved in this node; the next attack is the centered quartic Fourier gap itself.

---

# 33. References

1. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   arXiv: https://arxiv.org/abs/2008.06140

2. Alessandro Zaccagnini, **A conditional density theorem for the zeros of the Riemann zeta-function**, *Acta Arithmetica* 93 (2000), 293–304.  
   https://matwbn.icm.edu.pl/ksiazki/aa/aa93/aa9335.pdf

3. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   arXiv: https://arxiv.org/abs/2308.14888

4. D. A. Goldston, Ade Irma Suriajaya, **The error term in the Cesàro mean of the prime pair singular series**, *Journal of Number Theory* 227 (2021), 144–157.  
   arXiv: https://arxiv.org/abs/2007.14616

5. H. L. Montgomery, R. C. Vaughan, classical mean-value / Hilbert-inequality theory for Dirichlet polynomials and additive prime problems.

6. AMRAL, **RH-PositiveKernel-SelbergComparison v3.4**.

---

# 34. Provenance

研究主導：Neo.K

v3.5 discrete mean-square expansion、singular-series centering、minimal signed aggregate gate、shift-$L^2$ gate、Fourier interface、2026 prime-pair variance audit、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 direct arithmetic mean-square / centered shift-correlation 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
