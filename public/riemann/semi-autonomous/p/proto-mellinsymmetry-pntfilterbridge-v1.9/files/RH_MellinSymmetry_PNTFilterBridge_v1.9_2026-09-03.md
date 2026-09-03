工程紀錄 · 第三弧線 v1.9 · 2026-09-03 · MELLIN_SYMMETRY_BRIDGE · FIR_PNT_FILTER · RH_CLAIM_FALSE

# Mellin Symmetry Integral、Normalized PNT Error 與 Compact FIR Filter Bridge

**RH-MellinSymmetry-PNTFilterBridge v1.9**

本節點承接：

- `RH-FixedAperture-LocalPrimeDiscrepancy v1.6`
- `RH-FixedAperture-v1.65-IndependentAudit`
- `RH-LocalPrime-MeanEnergyBridge v1.7`
- `RH-LocalEnergy-CorrelationApertureTradeoff v1.8`

v1.8 已確認，若直接把 local-prime energy 展成 raw prime–prime / prime–background / background–background，會看到遠大於 RH 目標尺度的項；任何逐項 absolute-value estimate 都會失敗。

v1.9 的目標是先把這些 deterministic large terms 在**表示層**完成 renormalization，再辨識真正需要控制的 covariance object。

本輪核心結果是：

$$
\boxed{
\mathfrak E_h(e^t)
=
T_h\ast dB
=
\kappa_h\ast b
=
K_h\ast e,
}
$$

其中：

- $T_h$ 是 triangular / Cesàro tent；
- $\kappa_h=T_h'$ 是左右反對稱 sign window；
- $B(x)$ 是 weighted cumulative PNT error；
- $e(t)$ 是 classical PNT error 的 critical normalization；
- $K_h=T_h'+\frac12T_h$ 是 fixed compact finite-impulse-response filter。

因此 v1.6–v1.8 的 local discrepancy同時具有三個完全等價的 arithmetic representations：

```text
TRIANGULAR PRIME DISCREPANCY
    =
MELLIN SYMMETRY INTEGRAL OF CUMULATIVE ERROR
    =
COMPACT FIR FILTER OF NORMALIZED CLASSICAL PNT ERROR.
```

這把 AMRAL local-prime energy 精確放入：

- Cramér / Pintz / Brent–Platt–Trudgian mean-square PNT framework；
- Coppola / Laporta symmetry-integral framework；
- Gallagher / weighted-Cesàro smoothing framework。

但這個對齊同時帶來一個重要的 strength audit：

> uniform block mean-square control of這個 filtered observable本身已經是 RH-complete；因此現有 symmetry / Gallagher / short-interval工具不能只靠常規強度直接關閉 v1.9，否則就已經證明 RH。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

WEIGHTED_PNT_ERROR_IDENTITY = CLOSED
MELLIN_SYMMETRY_IDENTITY = CLOSED
COMPACT_FIR_PNT_FILTER_IDENTITY = CLOSED

FILTER_SUPPORT_RADIUS = h
FILTER_PAIR_RADIUS = 2h

CLASSICAL_PNT_MEANSQUARE_BRIDGE = REFERENCE_CLOSED
FILTERED_BLOCK_ENERGY_RH_COMPLETENESS = CLOSED_AS_REDUCTION

VERTICAL_SMOOTHING_HORIZONTAL_SENSITIVITY = CLOSED
RAW_CORRELATION_RENORMALIZATION = CLOSED_AT_REPRESENTATION_LEVEL

GALLAGHER_DIRECT_CLOSURE = NOT_AVAILABLE
GLOBAL_FILTERED_ENERGY_BOUND = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Classical PNT error

Let

$$
\psi(x)
=
\sum_{n\le x}\Lambda(n).
$$

Define the classical PNT error:

$$
\boxed{
E(x)
=
\psi(x)-x.
}
$$

Introduce logarithmic coordinates:

$$
x=e^t
$$

and the critical normalization:

$$
\boxed{
e(t)
=
e^{-t/2}E(e^t).
}
$$

The normalization $x^{-1/2}$ is the natural RH scale.

---

# 2. Weighted cumulative prime error

Define:

$$
S(x)
=
\sum_{n\le x}
\frac{\Lambda(n)}{\sqrt n}.
$$

Set:

$$
\boxed{
B(x)
=
S(x)-2\sqrt x.
}
$$

By Stieltjes partial summation:

$$
S(x)
=
\frac{\psi(x)}{\sqrt x}
+
\frac12
\int_1^x
\frac{\psi(u)}{u^{3/2}}\,du.
$$

Substitute:

$$
\psi(u)=u+E(u).
$$

Then:

$$
\boxed{
B(x)
=
-1
+
\frac{E(x)}{\sqrt x}
+
\frac12
\int_1^x
\frac{E(u)}{u^{3/2}}\,du.
}
$$

In log coordinates define:

$$
b(t)=B(e^t).
$$

Changing variables $u=e^v$ gives:

$$
\boxed{
b(t)
=
-1
+
e(t)
+
\frac12
\int_0^t e(v)\,dv.
}
$$

This is an exact identity.

---

# 3. Prime–archimedean discrepancy measure

On the log axis define:

$$
d\nu(u)
=
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}\mathbf1_{u\ge0}\,du.
$$

Because $b(t)=B(e^t)$ is the cumulative weighted error:

$$
\boxed{
db=d\nu
}
$$

in the distributional sense.

Differentiating the identity in Section 2 also gives:

$$
\boxed{
\nu
=
e'
+
\frac12e
}
$$

as distributions on the positive log axis.

---

# 4. Tent kernel

For fixed:

$$
h>0,
$$

define:

$$
\boxed{
T_h(v)
=
(h-|v|)_+.
}
$$

For:

$$
t\ge h,
$$

the v1.6 local prime discrepancy is:

$$
\boxed{
\mathfrak E_h(e^t)
=
(T_h\ast\nu)(t).
}
$$

Explicitly:

$$
\begin{aligned}
\mathfrak E_h(e^t)
&=
\sum_{
e^{t-h}<q<e^{t+h}
}
\frac{\Lambda(q)}{\sqrt q}
\left(
h-|t-\log q|
\right)
\\
&\quad
-
8e^{t/2}
\left(
\cosh\frac h2-1
\right).
\end{aligned}
$$

---

# 5. Exact Mellin symmetry integral

Define:

$$
\boxed{
\kappa_h(v)
=
T_h'(v)
=
\begin{cases}
1, & -h<v<0,
\\
-1, & 0<v<h,
\\
0, & |v|>h.
\end{cases}
}
$$

Endpoint values are irrelevant.

Since:

$$
db=d\nu,
$$

distributional integration by parts gives:

$$
\boxed{
T_h\ast db
=
T_h'\ast b
=
\kappa_h\ast b.
}
$$

Hence:

$$
\boxed{
\mathfrak E_h(e^t)
=
(\kappa_h\ast b)(t).
}
$$

Expanding the convolution:

$$
\boxed{
\mathfrak E_h(e^t)
=
\int_0^h
b(t+u)\,du
-
\int_0^h
b(t-u)\,du.
}
$$

This is an exact right-block minus left-block symmetry integral in logarithmic / multiplicative coordinates.

It is the continuous Mellin analogue of the sign-weighted symmetry integrals studied in additive short-interval arithmetic.

---

# 6. Exact compact FIR filter of normalized PNT error

From:

$$
\nu=e'+\frac12e,
$$

we obtain:

$$
T_h\ast\nu
=
T_h\ast e'
+
\frac12T_h\ast e.
$$

Since convolution with a derivative satisfies:

$$
T_h\ast e'
=
T_h'\ast e,
$$

define:

$$
\boxed{
K_h
=
T_h'
+
\frac12T_h.
}
$$

Then:

## Theorem 6.1 · FIR PNT Filter Identity

For:

$$
t\ge h,
$$

$$
\boxed{
\mathfrak E_h(e^t)
=
(K_h\ast e)(t).
}
$$

The filter has exact compact support:

$$
\boxed{
\operatorname{supp}K_h
\subset[-h,h].
}
$$

So each output value only reads a fixed-radius log-neighbourhood of the normalized classical PNT error.

---

# 7. Piecewise filter formula

On:

$$
-h<v<0,
$$

$$
K_h(v)
=
1
+
\frac12(h+v).
$$

On:

$$
0<v<h,
$$

$$
K_h(v)
=
-1
+
\frac12(h-v).
$$

Outside:

$$
[-h,h],
$$

it is zero.

A simple universal $L^1$ bound is:

$$
\boxed{
\|K_h\|_1
\le
2h+\frac{h^2}{2}.
}
$$

For small apertures such as:

$$
h=\log2<2,
$$

the signs on the two halves do not flip and the exact value simplifies further.

---

# 8. Fourier transfer function

Use the Fourier convention:

$$
\widehat f(\xi)
=
\int_{\mathbb R}
f(v)e^{-i\xi v}\,dv.
$$

The tent transform is:

$$
\boxed{
\widehat T_h(\xi)
=
\frac{
2(1-\cos(h\xi))
}{
\xi^2
}.
}
$$

Since:

$$
T_h'
\longleftrightarrow
i\xi\widehat T_h,
$$

the FIR transfer function is:

$$
\boxed{
\widehat K_h(\xi)
=
\left(
i\xi+\frac12
\right)
\frac{
2(1-\cos(h\xi))
}{
\xi^2
}.
}
$$

Therefore:

$$
\boxed{
|\widehat K_h(\xi)|^2
=
\left(
\xi^2+\frac14
\right)
\frac{
4(1-\cos(h\xi))^2
}{
\xi^4
}.
}
$$

At zero frequency:

$$
\boxed{
|\widehat K_h(0)|^2
=
\frac{h^4}{4}.
}
$$

So the FIR filter does not erase the macroscopic normalized PNT-error component.

---

# 9. Zero-mode response

A zeta zero:

$$
\rho
$$

contributes to the normalized PNT error with exponential mode:

$$
e^{\lambda t},
\qquad
\lambda=\rho-\frac12.
$$

For an exponential input:

$$
e^{\lambda t},
$$

the filter response is:

$$
\boxed{
M_h(\lambda)
=
2
\left(
\lambda+\frac12
\right)
\frac{
\cosh(\lambda h)-1
}{
\lambda^2
}.
}
$$

Since:

$$
\lambda+\frac12=\rho\neq0,
$$

and:

$$
\cosh(\lambda h)=1
$$

only when:

$$
\lambda h=2\pi ik,
$$

an off-axis mode:

$$
\Re\lambda\neq0
$$

cannot be annihilated.

Thus compact filtering preserves complete horizontal RH sensitivity.

---

# 10. Vertical regularization

Under RH:

$$
\lambda=i\gamma.
$$

The normalized PNT error zero coefficient is of order:

$$
\frac1{\rho}
=
O\left(\frac1{\gamma}\right).
$$

After the filter:

$$
-\frac1{\rho}
M_h(i\gamma)
=
-2
\frac{
1-\cos(\gamma h)
}{
\gamma^2
}.
$$

Hence the local discrepancy zero coefficient is:

$$
\boxed{
O_h(\gamma^{-2}).
}
$$

So the fixed-aperture filter does two useful things simultaneously:

```text
VERTICAL DIRECTION:
high zero ordinates are smoothed by an extra power of gamma

HORIZONTAL DIRECTION:
any nonzero Re(rho)-1/2 remains exponentially detectable.
```

This motivates the description:

$$
\boxed{
\text{vertical regularizer + horizontal off-axis detector}.
}
$$

---

# 11. Autocorrelation kernel of the FIR filter

Define:

$$
\widetilde K_h(v)
=
K_h(-v).
$$

Let:

$$
\boxed{
H_h
=
K_h\ast\widetilde K_h.
}
$$

Because:

$$
K_h=T_h'+\frac12T_h
$$

and $T_h$ is even while $T_h'$ is odd, the cross terms cancel:

$$
\boxed{
H_h
=
A_h
+
\frac14C_h,
}
$$

where:

$$
A_h
=
T_h'\ast\widetilde{T_h'},
$$

and:

$$
C_h
=
T_h\ast T_h.
$$

---

# 12. Sign-kernel autocorrelation

Writing:

$$
r=|d|,
$$

one obtains:

$$
\boxed{
A_h(d)
=
\begin{cases}
2h-3r,
&
0\le r\le h,
\\
r-2h,
&
h\le r\le2h,
\\
0,
&
r\ge2h.
\end{cases}
}
$$

This kernel changes sign but is positive definite because it is an autocorrelation.

Its total integral is zero, reflecting the zero mean of $\kappa_h$.

---

# 13. Tent autocorrelation

From v1.7:

$$
\boxed{
C_h(d)
=
\begin{cases}
\displaystyle
\frac{2h^3}{3}
-
hr^2
+
\frac{r^3}{2},
&
0\le r\le h,
\\
\displaystyle
\frac{(2h-r)^3}{6},
&
h\le r\le2h,
\\
0,
&
r\ge2h.
\end{cases}
}
$$

Therefore the full PNT-error covariance kernel is:

$$
\boxed{
H_h(d)
=
A_h(d)
+
\frac14C_h(d).
}
$$

It has fixed support:

$$
\boxed{
|d|<2h.
}
$$

---

# 14. Positive finite-range covariance form

For a finite log interval $I$, define:

$$
\boxed{
J_{h,I}
=
\int_I
|\mathfrak E_h(e^t)|^2dt.
}
$$

Using the FIR representation:

$$
J_{h,I}
=
\int_I
|(K_h\ast e)(t)|^2dt.
$$

Define the truncated kernel:

$$
\boxed{
H_{h,I}(u,v)
=
\int_I
K_h(t-u)K_h(t-v)\,dt.
}
$$

Then:

$$
\boxed{
J_{h,I}
=
\iint
e(u)e(v)
H_{h,I}(u,v)\,du\,dv.
}
$$

Because $K_h$ has support radius $h$:

$$
\boxed{
H_{h,I}(u,v)=0
\quad
\text{when }
|u-v|\ge2h.
}
$$

Thus the raw prime/background cancellation from v1.8 has been analytically renormalized before estimation.

The remaining object is a finite-range covariance of the centered normalized PNT error.

---

# 15. Classical normalized PNT mean square

Let:

$$
I(X)
=
\int_X^{2X}
|\psi(x)-x|^2dx.
$$

Brent–Platt–Trudgian prove:

- under RH:

$$
I(X)\ll X^2;
$$

- if RH is false:

$$
I(X)/X^2
$$

is unbounded.

Therefore:

$$
\boxed{
RH
\Longleftrightarrow
\sup_{X\ge X_0}
\frac{I(X)}{X^2}
<\infty.
}
$$

This is a known mean-square RH criterion.

---

# 16. Exact comparison with log-block normalized error

Let:

$$
a=\log X,
$$

and:

$$
L=\log2.
$$

Define:

$$
\boxed{
J_e(a)
=
\int_a^{a+L}
|e(t)|^2dt.
}
$$

Since:

$$
e(t)
=
\frac{
E(e^t)
}{
e^{t/2}
},
$$

and:

$$
dt=\frac{dx}{x},
$$

we have:

$$
\boxed{
J_e(a)
=
\int_X^{2X}
\frac{
|E(x)|^2
}{
x^2
}
dx.
}
$$

On:

$$
X\le x\le2X,
$$

$$
\frac1{4X^2}
\le
\frac1{x^2}
\le
\frac1{X^2}.
$$

Hence:

$$
\boxed{
\frac14
\frac{I(X)}{X^2}
\le
J_e(\log X)
\le
\frac{I(X)}{X^2}.
}
$$

Therefore Brent–Platt–Trudgian is equivalent to:

$$
\boxed{
RH
\Longleftrightarrow
\sup_a
J_e(a)
<\infty.
}
$$

---

# 17. Input mean square controls filtered mean square

Let:

$$
I=[a,a+L].
$$

By Minkowski / Young:

$$
\begin{aligned}
\|K_h\ast e\|_{L^2(I)}
&\le
\int_{-h}^h
|K_h(v)|
\|e(\cdot-v)\|_{L^2(I)}
\,dv
\\
&\le
\|K_h\|_1
\|e\|_{L^2([a-h,a+L+h])}.
\end{aligned}
$$

The enlarged interval has fixed finite length:

$$
L+2h.
$$

It can be covered by finitely many dyadic log-blocks of length $\log2$.

Thus:

$$
\boxed{
\sup_aJ_e(a)<\infty
\Longrightarrow
\sup_a
\int_a^{a+L}
|\mathfrak E_h(e^t)|^2dt
<\infty.
}
$$

---

# 18. Filtered block energy is also RH-complete

v1.7 proved the converse at theorem level:

if the fixed-aperture local discrepancy has uniformly bounded block energy, its Laplace transform is holomorphic in the upper half-plane and RH follows.

Therefore:

## Theorem 18.1 · Mean-square bridge

For any fixed:

$$
h>0,
$$

$$
\boxed{
\begin{aligned}
RH
&\Longleftrightarrow
\sup_X
\frac{I(X)}{X^2}
<\infty
\\
&\Longleftrightarrow
\sup_a
\int_a^{a+\log2}
|e(t)|^2dt
<\infty
\\
&\Longleftrightarrow
\sup_a
\int_a^{a+\log2}
|\mathfrak E_h(e^t)|^2dt
<\infty.
\end{aligned}
}
$$

So the v1.6–v1.9 local-prime energy is not logically weaker than the classical normalized PNT mean square.

Its advantage is structural and engineering:

- compact arithmetic memory;
- finite prime data per checkpoint;
- finite covariance radius;
- stronger vertical spectral smoothing;
- direct compatibility with Weil / Suzuki.

---

# 19. Mellin symmetry / weighted Selberg interface

Section 5 gives:

$$
\mathfrak E_h(e^t)
=
\int_0^h
b(t+u)du
-
\int_0^h
b(t-u)du.
$$

This is the exact multiplicative/log-coordinate analogue of a symmetry sum:

```text
right short block
minus
left short block.
```

Coppola and Laporta study sign-weighted symmetry integrals and weighted Selberg integrals for arithmetic functions in additive short intervals.

Their modified / generalized Gallagher lemmas use Cesàro-type weights to connect exponential-sum mean squares, weighted Selberg integrals, and correlations.

The v1.9 dictionary is:

```text
ADDITIVE SHORT-INTERVAL SYMMETRY
    <-> 
LOG-COORDINATE / MELLIN SYMMETRY

SIGN WEIGHT
    <- derivative ->
CESARO / TRIANGULAR TENT

ARITHMETIC CORRELATION
    <- Plancherel / Gallagher ->
MEAN-SQUARE EXPONENTIAL-SUM CONTROL
```

---

# 20. Why existing symmetry theorems do not directly close v1.9

There are important regime differences.

The classical symmetry-integral literature typically studies additive intervals:

$$
[x-H,x+H]
$$

with:

$$
H=o(x)
$$

and specific classes of arithmetic functions.

The AMRAL aperture is fixed in log scale:

$$
[xe^{-h},xe^h],
$$

which has additive width:

$$
\asymp_h x.
$$

The weight is also special:

$$
\frac{\Lambda(n)}{\sqrt n}.
$$

Thus existing bounds cannot be copied without a new normalization / strength proof.

More importantly, Theorem 18.1 shows that an unconditional bound strong enough to give uniform v1.9 block energy would itself imply RH.

Therefore:

$$
\boxed{
\text{Gallagher / symmetry machinery is a method interface,
not an already sufficient theorem import}.
}
$$

---

# 21. Method-strength gate

The strongest safe research question is no longer:

> Can a known generic symmetry-integral estimate be applied?

It is:

> What additional correlation input, beyond currently unconditional prime-distribution estimates, would upgrade a Mellin-symmetry / Gallagher inequality to the RH-complete uniform block bound?

This prevents accidental circularity.

Any proposed theorem should be classified as:

```text
UNCONDITIONAL AND TOO WEAK
CONDITIONAL ON RH
EQUIVALENT TO RH
STRICTLY STRONGER THAN RH
```

before being used as progress.

---

# 22. Why the FIR representation is still useful

Although the theorem barrier is unchanged, the filter changes the conditioning.

The classical normalized PNT error has zero coefficients of size:

$$
O(\gamma^{-1}).
$$

The local filtered observable has coefficients:

$$
O_h(\gamma^{-2}).
$$

Thus high vertical frequencies are more strongly suppressed.

At the same time, any off-axis growth exponent:

$$
\delta
=
\left|
\Re\rho-\frac12
\right|
>0
$$

survives because the transfer multiplier is nonzero.

So the filter improves:

- numerical convergence;
- spectral tail bounds;
- finite-height certificate stability;
- almost-periodic mean-energy evaluation;

without losing horizontal RH sensitivity.

This is a genuine proof-engineering advantage even though it does not by itself prove RH.

---

# 23. v1.8 cancellation reinterpreted

v1.8 found that raw prime self-energy grows like:

$$
\frac{h^3}{3}T^2.
$$

In the FIR representation that huge cancellation is no longer something we should estimate term by term.

It has already been absorbed into:

$$
e(t)
=
e^{-t/2}
[
\psi(e^t)-e^t
].
$$

Thus the correct renormalization order is:

```text
FIRST:
subtract the deterministic PNT background

THEN:
apply the compact FIR / symmetry filter

THEN:
estimate covariance / energy.
```

Not:

```text
expand raw prime pairs
take absolute values
hope large pieces cancel later.
```

This is the principal methodological correction of v1.9.

---

# 24. New smallest GAP

The remaining problem can be stated with no raw prime/background decomposition:

fix any:

$$
h>0.
$$

Prove unconditionally:

$$
\boxed{
\sup_a
\int_a^{a+\log2}
|(K_h\ast e)(t)|^2dt
<\infty.
}
$$

Equivalently:

$$
\boxed{
Q_h(T)=O(T).
}
$$

Or more weakly, prove any polynomial cumulative bound:

$$
Q_h(T)=O(T^A)
$$

for finite $A$.

By v1.7 these are RH-complete targets.

The next useful step is therefore not another criterion, but a **method audit of weighted Gallagher / Dirichlet-polynomial estimates after the PNT-background renormalization**.

---

# 25. Suggested next node

Recommended:

`RH-FilteredPNT-GallagherStrengthAudit-v2.0`

Tasks:

1. derive the exact Mellin-frequency form of the compact FIR filter;
2. define a smoothed finite Dirichlet polynomial for:
   $$
   -\frac{\zeta'}{\zeta}
   \left(
   \frac12+i\tau
   \right)
   $$
   with the deterministic pole/background term removed;
3. apply a weighted Gallagher inequality symbolically;
4. identify the precise local arithmetic square that appears;
5. compare its known unconditional bound to the RH-required bound;
6. quantify the exact missing logarithmic / exponential factor;
7. test whether the extra $\gamma^{-1}$ vertical smoothing of the v1.9 filter materially lowers the needed input.

The output should be a strength table, not a claim of proof.

---

# 26. GAP ledger

## CLOSED / REFERENCE-CLOSED

### G1. Weighted PNT error identity

```text
CLOSED
```

### G2. Mellin symmetry identity

```text
CLOSED
```

### G3. Compact FIR PNT filter

```text
CLOSED
```

### G4. Finite-range covariance kernel

```text
CLOSED
```

### G5. Classical PNT mean-square RH criterion

```text
REFERENCE_CLOSED
```

Brent–Platt–Trudgian.

### G6. Filtered block energy RH completeness

```text
CLOSED_AS_REDUCTION
```

---

## OPEN

### G7. Unconditional filtered block bound

```text
OPEN_RH_COMPLETE
```

### G8. Gallagher-strength upgrade

```text
OPEN
```

### G9. Dirichlet-polynomial renormalized estimate

```text
OPEN
```

### G10. Finite global proof object

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

FIR_FILTER_IDENTITY = EXACT
MEANSQUARE_BRIDGE = EXACT_AS_REDUCTION

GALLAGHER_METHOD_RELEVANT = TRUE
GALLAGHER_EXISTING_THEOREM_SUFFICIENT = FALSE / NOT ESTABLISHED

GLOBAL_FILTERED_ENERGY_BOUND = NOT_PROVED
FINITE_GLOBAL_PROBLEM = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{same symmetry-integral language}
\Longrightarrow
\text{existing theorem closes AMRAL}.
$$

Forbidden:

$$
\text{better vertical smoothing}
\Longrightarrow
RH.
$$

Forbidden:

$$
\text{finite covariance radius}
\Longrightarrow
\text{finite global proof}.
$$

---

# 28. One-line status

> v1.9 completes the renormalization that v1.8 was missing. The fixed-aperture local-prime discrepancy is exactly three things at once: a triangular convolution of the prime–archimedean discrepancy measure, a Mellin/log-coordinate symmetry integral of the weighted cumulative PNT error, and a compact FIR filter of the classical normalized PNT error $e(t)=e^{-t/2}(\psi(e^t)-e^t)$. The filter has support radius $h$, covariance radius $2h$, and transfer function $(i\xi+\frac12)2(1-\cos h\xi)/\xi^2$. It smooths critical-line high-frequency zero modes from $O(\gamma^{-1})$ to $O(\gamma^{-2})$ while preserving every off-axis exponential mode. Brent–Platt–Trudgian's classical normalized PNT mean-square criterion and the AMRAL filtered block-energy criterion are therefore RH-equivalent members of the same filtering chain. Coppola–Laporta symmetry integrals and Gallagher–Cesàro lemmas provide the correct methodological language, but no currently identified unconditional theorem reaches the required uniform block bound; if it did, it would already prove RH. The next task is a strength audit of renormalized Gallagher / Dirichlet-polynomial estimates, not another equivalent criterion.

---

# 29. References

1. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   DOI: https://doi.org/10.1016/j.jnt.2021.09.016  
   arXiv: https://arxiv.org/abs/2008.06140

2. Giovanni Coppola, **On the Symmetry Integral**, arXiv:1007.1018.  
   https://arxiv.org/abs/1007.1018

3. Giovanni Coppola, Maurizio Laporta, **Symmetry and short interval mean-squares**, arXiv:1312.5701.  
   https://arxiv.org/abs/1312.5701

4. Giovanni Coppola, Maurizio Laporta, **A modified Gallagher's Lemma**, arXiv:1301.0008.  
   https://arxiv.org/abs/1301.0008

5. Giovanni Coppola, Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, arXiv:1411.1739.  
   https://arxiv.org/abs/1411.1739

6. Alessandro Zaccagnini, **The Selberg integral and a new pair-correlation function for the zeros of the Riemann zeta-function**, arXiv:1603.02952.  
   https://arxiv.org/abs/1603.02952

7. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: https://doi.org/10.1112/jlms.12785

8. AMRAL, **RH-FixedAperture-LocalPrimeDiscrepancy v1.6**.

9. AMRAL, **RH-FixedAperture-v1.65-IndependentAudit**.

10. AMRAL, **RH-LocalPrime-MeanEnergyBridge v1.7**.

11. AMRAL, **RH-LocalEnergy-CorrelationApertureTradeoff v1.8**.

---

# 30. Provenance

研究主導：Neo.K

v1.9 weighted-PNT renormalization、Mellin-symmetry identity、compact FIR bridge、classical mean-square alignment、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 renormalized symmetry / filtered PNT mean-square 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
