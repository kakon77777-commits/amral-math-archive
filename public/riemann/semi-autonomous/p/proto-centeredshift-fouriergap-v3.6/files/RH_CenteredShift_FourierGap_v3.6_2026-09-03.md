工程紀錄 · 第五弧線 v3.6 · 2026-09-03 · CENTERED_QUARTIC_GAP · FOUR_DISTINCT_COVARIANCE · REFINED_SINGULAR_SERIES · RH_CLAIM_FALSE

# Centered Shift Fourier Gap：四點等距 Covariance、Refined Singular Series 與真正 $N^5$ Barrier

**RH-CenteredShift-FourierGap v3.6**

本節點承接：

- `RH-MeanSquare-ArithmeticGap v3.5`
- `RH-PositiveKernel-SelbergComparison v3.4`

v3.5 將第一個直接 arithmetic $L^2$ gate壓成：

$$
\boxed{
\mathcal V_N
=
\sum_{h=1}^{2N-2}
|\mathcal R_N(h)|^2
}
$$

其中：

$$
\boxed{
\mathcal R_N(h)
=
\sum_{n=h+1}^{2N-1}
w_N(n)
b_{n,h},
}
$$

以及：

$$
\boxed{
b_{n,h}
=
(\Lambda(n)-1)
(\Lambda(n-h)-1)
-
[
\mathfrak S(h)-1
].
}
$$

若：

$$
\boxed{
\mathcal V_N
\ll
N^{5-\eta+o(1)}
}
$$

for any fixed：

$$
\eta>0,
$$

則：

$$
I(N)
\ll
N^{3-\eta/2+o(1)},
$$

從而：

$$
\Theta
\le
1-\frac{\eta}{4}.
$$

v3.6 對 $\mathcal V_N$ 做真正 quartic 展開，回答：

> 到底哪一類 quadruples 可以產生 $N^5$？

本輪 exact 結論：

1. same-pair quartic diagonal只有：
   $$
   N^{4+o(1)};
   $$
2. 共用一個 prime index 的 semi-diagonal / 3-term arithmetic-progression configurations也只有：
   $$
   N^{4+o(1)};
   $$
3. 唯一自然具有：
   $$
   N^{5+o(1)}
   $$
   combinatorial capacity 的，是四個 index全不同的 equal-gap covariance：
   $$
   n,\ n-h,\ m,\ m-h;
   $$
4. 因此對任何：
   $$
   0<\eta<1,
   $$
   Gate B 的 fixed-power problem exponent-equivalent to：
   $$
   \boxed{
   |\mathfrak Q_N|
   \ll
   N^{5-\eta+o(1)},
   }
   $$
   其中 $\mathfrak Q_N$ 是 genuine four-distinct covariance；
5. 但 pair-level singular-series subtraction還不夠：四點 covariance有自己的 deterministic Hardy–Littlewood / refined-singular-series backbone；
6. 對 offsets：
   $$
   \{0,h,d,d+h\},
   $$
   正確的 predicted connected covariance是：
   $$
   \boxed{
   \mathfrak K_4(h,d)
   =
   \mathfrak S_0(0,h,d,d+h)
   -
   [
   \mathfrak S(h)-1
   ]^2;
   }
   $$
7. 所以下一階 arithmetic theorem必須同時處理：
   - structured refined-singular-series four-point model；
   - actual prime deviation from that model；
8. 現有 almost-all / higher-uniformity results主要提供 logarithmic / $o(1)$ savings，尚未提供本 gate 所需的 fixed:
   $$
   N^{-\eta}.
   $$

這是 representation closure 後，第一個真正四點 arithmetic barrier。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

CENTERED_PAIR_VARIABLE = CLOSED
QUARTIC_EXPANSION = CLOSED

SAME_PAIR_DIAGONAL = O(N^(4+o(1)))
SHARED_INDEX_SEMIDIAGONAL = O(N^(4+o(1)))

GENUINE_FOUR_DISTINCT_COVARIANCE = DEFINED
V_N = Q_N + O(N^(4+o(1)))

FOR_0_LT_ETA_LT_1:
    V_N << N^(5-eta)
    EQUIVALENT_AT_EXPONENT_LEVEL_TO
    |Q_N| << N^(5-eta)

PAIR_CENTERING_REMOVES_ALL_HIGHER_ARITHMETIC_BACKBONE = FALSE

REFINED_SINGULAR_SERIES_S0 = DEFINED
FOUR_POINT_COVARIANCE_BACKBONE_K4 = DEFINED

K4_IDENTICALLY_ZERO = FALSE
K4_SIGN_DEFINITE = FALSE

FOUR_POINT_MODEL_POWER_SAVING = OPEN
FOUR_POINT_PRIME_DEVIATION_POWER_SAVING = OPEN

CURRENT_FIXED_ETA_POSITIVE = NOT_PROVED
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Endpoint weight and centered pair variable

Recall：

$$
\boxed{
w_N(n)
=
\begin{cases}
N,
&
1\le n\le N,
\\
2N-n,
&
N<n<2N,
\\
0,
&
n\ge2N.
\end{cases}
}
$$

Let：

$$
\boxed{
a_n=\Lambda(n)-1.
}
$$

Set：

$$
\boxed{
\mu_h
=
\mathfrak S(h)-1.
}
$$

Define the pointwise centered pair variable：

$$
\boxed{
b_{n,h}
=
a_na_{n-h}
-
\mu_h.
}
$$

Then：

$$
\boxed{
\mathcal R_N(h)
=
\sum_{n=h+1}^{2N-1}
w_N(n)b_{n,h}.
}
$$

---

# 2. Exact quartic expansion

Square and sum over shifts：

$$
\begin{aligned}
\mathcal V_N
&=
\sum_h
\left(
\sum_n
w_N(n)b_{n,h}
\right)^2
\\
&=
\sum_h
\sum_{n,m}
w_N(n)w_N(m)
b_{n,h}b_{m,h}.
\end{aligned}
$$

This is a centered quartic prime correlation.

---

# 3. Same-pair diagonal

Define：

$$
\boxed{
\mathcal D_N^{(4)}
=
\sum_{h=1}^{2N-2}
\sum_{n=h+1}^{2N-1}
w_N(n)^2
b_{n,h}^2.
}
$$

This is the contribution：

$$
n=m.
$$

---

# 4. Uniform subpower bound on $b_{n,h}$

For：

$$
n\le2N,
$$

$$
|\Lambda(n)-1|
\ll
\log N.
$$

Also the prime-pair singular series satisfies for every fixed：

$$
\varepsilon>0,
$$

$$
\boxed{
\mathfrak S(h)
\ll_\varepsilon
h^\varepsilon.
}
$$

Therefore：

$$
\boxed{
b_{n,h}
\ll_\varepsilon
N^\varepsilon.
}
$$

Here logarithmic factors are absorbed into：

$$
N^\varepsilon.
$$

---

# 5. Diagonal size

There are：

$$
O(N^2)
$$

valid：

$$
(n,h)
$$

pairs.

Since：

$$
w_N(n)^2\le N^2,
$$

Theorem 4 gives：

## Theorem 5.1

For every：

$$
\varepsilon>0,
$$

$$
\boxed{
\mathcal D_N^{(4)}
\ll_\varepsilon
N^{4+\varepsilon}.
}
$$

Thus same-pair quartic diagonal is not the $N^5$ barrier.

---

# 6. Shared-index semi-diagonal

For：

$$
m<n,
$$

the two equal-gap pairs：

$$
\{n,n-h\},
\qquad
\{m,m-h\}
$$

share one index iff：

$$
\boxed{
m=n-h.
}
$$

This produces the three-point arithmetic progression：

$$
n-2h,
\qquad
n-h,
\qquad
n.
$$

Define：

$$
\boxed{
\mathcal S_N^{(3)}
=
2
\sum_{h=1}^{N-1}
\sum_{n=2h+1}^{2N-1}
w_N(n)
w_N(n-h)
b_{n,h}
b_{n-h,h}.
}
$$

---

# 7. Semi-diagonal size

The number of：

$$
(n,h)
$$

terms in Section 6 is：

$$
O(N^2).
$$

Each weight product is at most：

$$
N^2.
$$

Hence：

## Theorem 7.1

For every：

$$
\varepsilon>0,
$$

$$
\boxed{
\mathcal S_N^{(3)}
\ll_\varepsilon
N^{4+\varepsilon}.
}
$$

So the entire three-index overlap family is also below every first：

$$
N^{5-\eta},
\qquad
0<\eta<1.
$$

target.

---

# 8. Genuine four-distinct covariance

Define：

$$
\boxed{
\begin{aligned}
\mathfrak Q_N
&=
2
\sum_{h=1}^{2N-2}
\sum_{\substack{
h+1\le m<n\le2N-1
\\
m\ne n-h
}}
w_N(n)
w_N(m)
\\
&\qquad\qquad\qquad
\times
b_{n,h}
b_{m,h}.
\end{aligned}
}
$$

Every summand has four distinct positions：

$$
\boxed{
n,\quad n-h,\quad m,\quad m-h.
}
$$

---

# 9. Exact quartic decomposition

Sections 3, 6, 8 partition all：

$$
(n,m)
$$

pairs.

Therefore：

## Theorem 9.1

$$
\boxed{
\mathcal V_N
=
\mathcal D_N^{(4)}
+
\mathcal S_N^{(3)}
+
\mathfrak Q_N.
}
$$

Using Sections 5 and 7：

$$
\boxed{
\mathcal V_N
=
\mathfrak Q_N
+
O_\varepsilon(
N^{4+\varepsilon}
).
}
$$

---

# 10. First fixed-power equivalence

Fix：

$$
0<\eta<1.
$$

Choose：

$$
0<\varepsilon<1-\eta.
$$

Then：

$$
N^{4+\varepsilon}
=
o(
N^{5-\eta}
).
$$

Hence：

## Theorem 10.1 · Genuine-four-point Gate

For：

$$
0<\eta<1,
$$

$$
\boxed{
\mathcal V_N
\ll
N^{5-\eta+o(1)}
}
$$

is exponent-equivalent to：

$$
\boxed{
|\mathfrak Q_N|
\ll
N^{5-\eta+o(1)}.
}
$$

Thus the first power-saving barrier in Gate B is a genuine four-distinct equal-gap covariance.

---

# 11. Difference parameter

Write：

$$
d=n-m>0.
$$

For four-distinct configurations：

$$
d\ne h.
$$

Let：

$$
r=m-h.
$$

Then the four positions are：

$$
\boxed{
r,\quad
r+h,\quad
r+d,\quad
r+d+h.
}
$$

This is a parallelogram / equal-gap additive configuration.

The free arithmetic parameters are：

$$
(r,h,d).
$$

There are：

$$
O(N^3)
$$

such configurations.

Together with：

$$
w_N(n)w_N(m)\asymp N^2
$$

at bulk scale, this is the unique family with natural combinatorial capacity：

$$
N^5.
$$

---

# 12. Why pair centering is not enough at fourth order

The pair variable：

$$
b_{n,h}
$$

has its two-point Hardy–Littlewood backbone removed.

But：

$$
b_{r+h,h}
b_{r+d+h,h}
$$

is a four-point object.

Local congruence constraints can correlate all four forms：

$$
r,\quad
r+h,\quad
r+d,\quad
r+d+h.
$$

Therefore：

$$
\boxed{
\mathbb E[
b_{r+h,h}
b_{r+d+h,h}
]
}
$$

has a nontrivial four-point arithmetic model.

Pair centering does not imply fourth-order independence.

---

# 13. Refined singular series

For a finite set of distinct integers：

$$
\mathcal H,
$$

let：

$$
\mathfrak S(\mathcal H)
$$

denote the Hardy–Littlewood singular series.

Use conventions：

$$
\mathfrak S(\varnothing)=1,
$$

and：

$$
\mathfrak S(\{a\})=1.
$$

Define the refined / centered singular series：

$$
\boxed{
\mathfrak S_0(\mathcal H)
=
\sum_{
\mathcal T\subseteq\mathcal H
}
(-1)^{
|\mathcal H|-|\mathcal T|
}
\mathfrak S(\mathcal T).
}
$$

This is the Montgomery–Soundararajan centered singular-series object.

For a two-set：

$$
\{0,h\},
$$

$$
\boxed{
\mathfrak S_0(0,h)
=
\mathfrak S(h)-1
=
\mu_h.
}
$$

---

# 14. Four-point centered main term

For：

$$
d>0,
\qquad
d\ne h,
$$

define：

$$
\boxed{
\mathcal H_{h,d}
=
\{0,h,d,d+h\}.
}
$$

Under the four-tuple Hardy–Littlewood model：

$$
\boxed{
\mathfrak S_0(
\mathcal H_{h,d}
)
}
$$

is the predicted main term for：

$$
\prod_{
u\in\mathcal H_{h,d}
}
[
\Lambda(r+u)-1
].
$$

---

# 15. Pair-pair covariance backbone

Both equal-gap pairs have the same pair mean：

$$
\mu_h.
$$

Therefore the predicted covariance of the two centered pair variables is：

## Definition 15.1 · Connected equal-gap four-point model

$$
\boxed{
\mathfrak K_4(h,d)
=
\mathfrak S_0(
0,h,d,d+h
)
-
[
\mathfrak S(h)-1
]^2.
}
$$

This is the correct four-point model after pair centering.

---

# 16. $\mathfrak K_4$ is not zero

There is no identity forcing：

$$
\mathfrak K_4(h,d)=0.
$$

It depends on all local congruence collisions among：

$$
0,\quad h,\quad d,\quad d+h.
$$

Reference finite-Euler-product samples show：

- nonzero positive values；
- nonzero negative values；
- inadmissible four-tuples can still have nonzero refined centered value because lower-order subsets enter $\mathfrak S_0$.

These numerical samples are illustrative only.

---

# 17. Model weight

For：

$$
h,d\ge1,
$$

$$
d\ne h,
$$

define：

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

This is the endpoint-Cesàro weight of a parallelogram with gaps：

$$
h,d.
$$

---

# 18. Four-point model aggregate

Define the formal refined-singular-series contribution：

$$
\boxed{
\mathfrak M_{4,N}
=
2
\sum_{
\substack{
h,d\ge1
\\
h+d\le2N-2
\\
d\ne h
}
}
\Omega_N(h,d)
\mathfrak K_4(h,d).
}
$$

This is the natural deterministic four-point covariance model.

No power-saving theorem for this constrained parallelogram average is asserted here.

---

# 19. Four-point prime-deviation remainder

Define：

$$
\boxed{
\begin{aligned}
\mathfrak E_{4,N}
&=
2
\sum_{
\substack{
h,d\ge1
\\
h+d\le2N-2
\\
d\ne h
}
}
\sum_{
r=1
}^{2N-1-h-d}
w_N(r+h)
w_N(r+h+d)
\\
&\quad\times
\Big[
b_{r+h,h}
b_{r+d+h,h}
-
\mathfrak K_4(h,d)
\Big].
\end{aligned}
}
$$

Then by definition：

## Theorem 19.1 · Model/deviation split

$$
\boxed{
\mathfrak Q_N
=
\mathfrak M_{4,N}
+
\mathfrak E_{4,N}.
}
$$

The decomposition is algebraically exact once：

$$
\mathfrak K_4
$$

is fixed.

Its interpretation as main term plus error uses the Hardy–Littlewood four-tuple model.

---

# 20. Two-stage quartic gate

A sufficient route to：

$$
\eta>0
$$

is therefore to prove, for some：

$$
\eta_1,\eta_2>0,
$$

$$
\boxed{
|\mathfrak M_{4,N}|
\ll
N^{5-\eta_1+o(1)},
}
$$

and：

$$
\boxed{
|\mathfrak E_{4,N}|
\ll
N^{5-\eta_2+o(1)}.
}
$$

Then：

$$
\boxed{
\eta
=
\min(
\eta_1,\eta_2
)
}
$$

closes Gate B.

This separates：

```text
LOCAL CONGRUENCE / SINGULAR-SERIES GEOMETRY
```

from：

```text
ACTUAL PRIME DEVIATION.
```

---

# 21. Refined singular-series literature audit

Gallagher proved that ordinary $k$-tuple singular series averages to $1$ over generic $k$-tuples.

Montgomery–Soundararajan introduced：

$$
\mathfrak S_0
$$

to study centered prime moments.

For even：

$$
k,
$$

their averaged refined singular-series sums have nontrivial Gaussian-size main terms rather than vanishing identically.

In particular the fourth-order centered singular-series structure is real arithmetic content.

So a proof that treats：

$$
b_{n,h}
$$

as independent after pair centering ignores a known higher-order congruence structure.

---

# 22. Important limitation of generic singular-series averages

The configuration：

$$
\{0,h,d,d+h\}
$$

is not a generic four-parameter tuple.

It lies on the additive relation：

$$
0+(d+h)=h+d.
$$

So generic average results over all distinct four-tuples do not automatically give the required constrained：

$$
(h,d)
$$

average.

The parallelogram geometry must be audited separately.

This is a genuine specialization issue.

---

# 23. Actual quartic diagonal scale in finite data

Reference computation with：

$$
N=100,250,500,1000
$$

shows：

$$
\mathcal D_N^{(4)},
\quad
\mathcal S_N^{(3)},
\quad
\mathfrak Q_N
$$

all reconstruct：

$$
\mathcal V_N
$$

to floating-point precision.

At these finite scales：

$$
\mathcal V_N
$$

and：

$$
\mathfrak Q_N
$$

are numerically much closer to：

$$
N^4(\log N)^2
$$

than to：

$$
N^5.
$$

This is consistent with substantial four-point decorrelation.

It is **not** a tail theorem and is not used as proof.

---

# 24. Endpoint covariance formulation

Recall from v3.5：

$$
\boxed{
\mathcal R_N(h)
=
\sum_{j=N}^{2N-1}
Q_j(h),
}
$$

where：

$$
Q_j(h)
$$

is the centered pair residual up to endpoint：

$$
j.
$$

Therefore：

$$
\boxed{
\mathcal V_N
=
\sum_{
j,k=N
}^{2N-1}
\sum_h
Q_j(h)
Q_k(h).
}
$$

This is an endpoint covariance matrix.

The diagonal：

$$
j=k
$$

contains standard pair-error-variance-type information.

The off-diagonal：

$$
j\ne k
$$

measures coherence of pair errors across endpoints.

---

# 25. Endpoint-$L^2$ sufficient route

By Cauchy：

$$
\boxed{
\mathcal V_N
\le
N
\sum_{j=N}^{2N-1}
\sum_h
|Q_j(h)|^2.
}
$$

Thus：

## Gate 25.1

If：

$$
\boxed{
\sum_{j=N}^{2N-1}
\sum_h
|Q_j(h)|^2
\ll
N^{4-\eta+o(1)},
}
$$

then：

$$
\boxed{
\mathcal V_N
\ll
N^{5-\eta+o(1)}.
}
$$

This is another exact sufficient interface.

It is stronger than directly estimating the signed endpoint covariance.

---

# 26. Interface with Chou–Haag–Huryn–Ledoan

The standard prime-pair error at endpoint：

$$
j
$$

is：

$$
r_j(h)
=
\psi_2(j,h)
-
\mathfrak S(h)(j-h).
$$

v3.5 proved：

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

So endpoint Gate 25.1 contains：

- standard prime-pair error variance；
- PNT boundary-error covariance.

The 2026 Chou–Haag–Huryn–Ledoan work shows that upper bounds for the standard pair-error variance are themselves extremely difficult; even under GRH their stated bound remains above the conjectural RH-scale variance by a factor of approximately $N^{1/2}$ up to logarithms.

Thus Gate 25.1 is a useful bridge but not currently an unconditional shortcut.

---

# 27. Major-arc model warning

Chou et al. approximate：

$$
|S(\alpha)|^2
$$

by a nonnegative major-arc model：

$$
V_y(\alpha),
$$

whose Fourier coefficients approximate the pair singular series.

For v3.6, pair-level major-arc subtraction corresponds to the existing：

$$
\mu_h
$$

centering.

But once the residual is squared, higher-order singular-series covariance re-enters.

Therefore：

$$
\boxed{
\text{MAJOR-ARC MODEL MUST BE AUDITED AT THE ORDER OF THE NORM BEING TAKEN.}
}
$$

A correct pair model is not automatically a complete quartic model.

---

# 28. Why generic large-value improvements do not yet close the gate

Guth–Maynard's 2026 large-value theorem gives major advances in Dirichlet-polynomial large values, zero density, and primes in short intervals.

These results are highly relevant analytic technology.

But：

$$
\mathfrak Q_N
$$

is a singular-series-centered additive four-point covariance.

A zero-density theorem can still permit one exceptional rightmost zero, while the RH mean-square exponent is controlled by such a zero.

Likewise a generic large-value estimate does not automatically subtract：

$$
\mathfrak K_4(h,d).
$$

So no fixed：

$$
\eta>0
$$

for Gate B follows automatically from current large-value technology.

---

# 29. Higher-uniformity / almost-all audit

Modern higher-uniformity results for：

$$
\Lambda
$$

prove very strong almost-all interval and averaged-variable statements, including Hardy–Littlewood patterns after averaging one variable.

However the audited quantitative gains relevant here are principally：

- arbitrary powers of logarithms；
- $o(1)$ uniformity；
- almost-all statements.

A fixed：

$$
N^{-\eta}
$$

saving in the constrained equal-gap four-point covariance is not supplied by the currently audited theorem statements.

Therefore：

$$
\boxed{
\eta_{\rm quartic}=0
}
$$

remains the rigorous fixed-power state of this line.

---

# 30. The first genuinely new arithmetic lemma

The strongest concise v3.6 target is：

## Quartic Equal-Gap Covariance Lemma $\operatorname{QEGC}(\eta)$

There exists：

$$
\eta>0
$$

such that：

$$
\boxed{
\left|
2
\sum_h
\sum_{
\substack{
h+1\le m<n\le2N-1
\\
m\ne n-h
}
}
w_N(n)
w_N(m)
b_{n,h}
b_{m,h}
\right|
\ll
N^{5-\eta+o(1)}.
}
$$

Then：

$$
\boxed{
\mathcal V_N
\ll
N^{5-\eta+o(1)},
}
$$

hence：

$$
\boxed{
I(N)
\ll
N^{3-\eta/2+o(1)},
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

This is the first direct four-point arithmetic lemma in the post-representation phase.

---

# 31. Model-aware version

A more structured candidate is：

## QEGC-Model

Prove both：

$$
\boxed{
|\mathfrak M_{4,N}|
\ll
N^{5-\eta_1},
}
$$

and：

$$
\boxed{
|\mathfrak E_{4,N}|
\ll
N^{5-\eta_2}.
}
$$

This route explicitly respects refined singular-series structure.

It is preferable to any argument that assumes：

```text
PAIR CENTERED
=> FOUR-POINT RANDOM.
```

---

# 32. False-progress gates

Reject：

### F1 · Diagonal-only quartic improvement

Diagonal is already：

$$
N^{4+o(1)}.
$$

### F2 · Semi-diagonal-only improvement

Also already：

$$
N^{4+o(1)}.
$$

### F3 · Pair centering treated as full independence

Must audit：

$$
\mathfrak K_4(h,d).
$$

### F4 · Generic four-tuple average applied directly to parallelograms

The constrained family has extra additive structure.

### F5 · Logarithmic four-point saving

$$
N^5/\log^A N
$$

still has：

$$
\eta=0.
$$

### F6 · Large-value / zero-density theorem with no covariance translation

No automatic Gate-B progress.

---

# 33. Autonomous progress metrics

Define：

$$
\boxed{
\eta_Q
=
5
-
\limsup
\frac{
\log^+|\mathfrak Q_N|
}{
\log N
}.
}
$$

Then：

$$
\boxed{
\eta_Q>0
}
$$

is a direct arithmetic breakthrough.

At Gate-B strength：

$$
\boxed{
\kappa_I
\ge
\frac{\eta_Q}{2}.
}
$$

Define model and deviation exponents：

$$
\boxed{
\eta_M
=
5-\operatorname{exp}(\mathfrak M_{4,N}),
}
$$

$$
\boxed{
\eta_E
=
5-\operatorname{exp}(\mathfrak E_{4,N}).
}
$$

A model-aware proof certifies：

$$
\boxed{
\eta_Q
\ge
\min(\eta_M,\eta_E).
}
$$

---

# 34. Reference numerical decomposition

The package evaluates：

$$
N=100,250,500,1000.
$$

It independently computes：

- $\mathcal V_N$；
- same-pair diagonal；
- shared-index semi-diagonal；
- genuine four-distinct remainder by exact subtraction.

At：

$$
N=1000,
$$

reference values are approximately：

$$
\mathcal V_N
\approx
4.63\times10^{13},
$$

$$
\mathcal D_N^{(4)}
\approx
2.31\times10^{13},
$$

$$
\mathcal S_N^{(3)}
\approx
1.24\times10^{12},
$$

$$
\mathfrak Q_N
\approx
2.20\times10^{13}.
$$

The equality：

$$
\mathcal V_N
=
\mathcal D_N^{(4)}
+
\mathcal S_N^{(3)}
+
\mathfrak Q_N
$$

holds to floating-point reconstruction precision.

Again：

```text
FINITE SCALE ≠ TAIL THEOREM.
```

---

# 35. Suggested v3.7 direction

Recommended：

`RH-RefinedSingularSeries-Parallelogram v3.7`

Do not return to representations.

First attack the **deterministic four-point model**：

$$
\mathfrak M_{4,N}.
$$

Tasks：

1. derive an Euler/Ramanujan expansion for：
   $$
   \mathfrak K_4(h,d);
   $$
2. exploit the parallelogram offsets：
   $$
   0,h,d,d+h;
   $$
3. evaluate / bound：
   $$
   \sum_{h,d}
   \Omega_N(h,d)
   \mathfrak K_4(h,d);
   $$
4. compare with Montgomery–Soundararajan refined singular-series moment technology；
5. determine whether the constrained parallelogram family has：
   - $N^{5}$ model mass；
   - $N^4\operatorname{polylog}N$ mass；
   - or another scale；
6. only after model scale is rigorously known, attack：
   $$
   \mathfrak E_{4,N};
   $$
7. reject any numerical scale extrapolation as theorem.

This isolates the pure local-congruence component before asking primes to beat it.

---

# 36. GAP ledger

## CLOSED / REDUCED

### G1. Quartic expansion

```text
CLOSED
```

### G2. Same-pair diagonal

```text
LOWER_ORDER
```

$$
N^{4+o(1)}.
$$

### G3. Shared-index semi-diagonal

```text
LOWER_ORDER
```

$$
N^{4+o(1)}.
$$

### G4. Genuine four-distinct Gate

```text
CLOSED_AS_REDUCTION
```

### G5. Refined four-point covariance backbone

```text
DEFINED
```

### G6. Model/deviation split

```text
CLOSED_AS_DEFINITION
```

---

## OPEN

### G7. Parallelogram refined-singular-series aggregate

```text
OPEN
```

### G8. Prime deviation from four-point model

```text
OPEN
```

### G9. Any：

$$
\eta_Q>0
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

### G11. RH

```text
OPEN
```

---

# 37. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

QUARTIC CONFIGURATION DECOMPOSITION = EXACT

O(N^(4+epsilon)) DIAGONAL / SEMIDIAGONAL
    = ELEMENTARY

REFINED SINGULAR SERIES MODEL
    = CLASSICAL HARDY-LITTLEWOOD MODEL LANGUAGE

K4 NUMERICAL VALUES
    = FINITE EULER PRODUCT ILLUSTRATION ONLY

NO PARALLELOGRAM MODEL POWER SAVING PROVED
NO PRIME FOUR-POINT POWER SAVING PROVED

ETA_Q_POSITIVE = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\text{finite }N^4\log^2N\text{ behavior}
\Longrightarrow
\eta>0.
$$

Forbidden：

$$
\mathfrak S_0\text{ average over generic four-tuples}
\Longrightarrow
\text{same bound for parallelogram tuples}.
$$

Forbidden：

$$
\text{pair Hardy–Littlewood centering}
\Longrightarrow
\text{four-point covariance main term}=0.
$$

---

# 38. One-line status

> v3.6 expands the centered shift variance into its genuine quartic arithmetic content. Writing $b_{n,h}=(\Lambda(n)-1)(\Lambda(n-h)-1)-(\mathfrak S(h)-1)$ gives $\mathcal V_N=\sum_{h,n,m}w_N(n)w_N(m)b_{n,h}b_{m,h}$. The same-pair diagonal and the only shared-index semi-diagonal both contain only $O(N^2)$ configurations and are $N^{4+o(1)}$, so for every first saving $0<\eta<1$ the $N^{5-\eta}$ problem is exponent-equivalent to a four-distinct equal-gap covariance over the parallelogram positions $r,r+h,r+d,r+d+h$. Pair-level singular-series subtraction does not make these variables fourth-order independent. Using the Montgomery–Soundararajan refined singular series, the natural connected covariance backbone is $\mathfrak K_4(h,d)=\mathfrak S_0(0,h,d,d+h)-(\mathfrak S(h)-1)^2$, which is generally nonzero and sign-changing. Thus the genuine quartic term splits into a constrained refined-singular-series model plus actual prime deviation from that model. Existing higher-uniformity and almost-all results give powerful logarithmic or $o(1)$ savings, but no audited fixed $N^{-\eta}$ bound for this equal-gap four-point covariance. The first direct arithmetic lemma is therefore QEGC$(\eta)$: any fixed power saving on the genuine four-distinct covariance yields $\mathcal V_N\ll N^{5-\eta}$, hence $I(N)\ll N^{3-\eta/2}$ and the fixed zero strip $\Theta\le1-\eta/4$. The next node should isolate the deterministic parallelogram refined-singular-series aggregate before attempting the prime four-point deviation.

---

# 39. References

1. Hugh L. Montgomery, K. Soundararajan, **Primes in short intervals**, *Communications in Mathematical Physics* 252 (2004), 589–617.  
   arXiv: https://arxiv.org/abs/math/0409258

2. Thomas F. Bloom, Vivian Kuperberg, **Odd moments and adding fractions**, *Proceedings of the London Mathematical Society* (2025).  
   DOI: https://doi.org/10.1112/plms.70068  
   arXiv: https://arxiv.org/abs/2312.09021

3. Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, **Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones mathematicae* 244 (2026), 967–1091.  
   arXiv: https://arxiv.org/abs/2411.05770

4. Leon Chou, Summer Haag, Jake Huryn, Andrew Ledoan, **The error term in counting prime pairs**, *Journal of Number Theory* 278 (2026), 422–450.  
   arXiv: https://arxiv.org/abs/2308.14888

5. Larry Guth, James Maynard, **New large value estimates for Dirichlet polynomials**, *Annals of Mathematics* 203 (2026), 623–675.  
   DOI: https://doi.org/10.4007/annals.2026.203.2.6

6. AMRAL, **RH-MeanSquare-ArithmeticGap v3.5**.

---

# 40. Provenance

研究主導：Neo.K

v3.6 quartic configuration decomposition、four-distinct equal-gap gate、refined singular-series covariance model、endpoint covariance audit、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第五弧線 centered quartic / refined singular-series parallelogram 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
