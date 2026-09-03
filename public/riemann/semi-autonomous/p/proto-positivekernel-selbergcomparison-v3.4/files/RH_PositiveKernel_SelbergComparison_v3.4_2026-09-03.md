工程紀錄 · 第四弧線 v3.4 · 2026-09-03 · ELLIPTIC_MEANSQUARE_EQUIVALENCE · LOCAL_ONE_SIDED_COMPARISON · REPRESENTATION_CLOSURE · RH_CLAIM_FALSE

# Positive Kernel–Selberg Comparison：Elliptic Mean-Square Equivalence 與 Representation Closure

**RH-PositiveKernel-SelbergComparison v3.4**

本節點承接：

- `RH-MellinSymmetry-PNTFilterBridge v1.9`
- `RH-ArithmeticInnovation-EnergyGate v2.9`
- `RH-PositiveKernel-InnovationSpectrum v3.3`

v3.3 已證明：

> 固定 positive spectral slicing不會自動產生較弱的 RH theorem。

v3.4 因此直接比較 canonical Cauchy/tent energy與 classical normalized PNT mean square。

令：

$$
E(x)
=
\psi(x)-x,
$$

以及 log-normalized PNT error：

$$
\boxed{
e(t)
=
e^{-t/2}E(e^t).
}
$$

Recall：

$$
\boxed{
d\nu
=
de+\frac12e\,dt.
}
$$

local Cauchy source：

$$
\boxed{
d\mu_t(u)
=
T_h(t-u)\,d\nu(u).
}
$$

pointwise Cauchy energy：

$$
\boxed{
\mathcal C_h(t)
=
\iint
e^{-|u-v|}
\,d\mu_t(u)d\mu_t(v).
}
$$

本輪核心結果有四層。

---

## Result A · Local positive upper comparison

對每個 fixed center：

$$
\boxed{
\mathcal C_h(t)
\le
2(h+1)^2
\int_{t-h}^{t+h}
|e(u)|^2du.
}
$$

所以 canonical Cauchy energy可由 classical normalized PNT mean square正值上界，且沒有 fixed-exponent loss。

---

## Result B · Local two-sided coercivity no-go

單一 fixed center不可能有 structure-blind lower bound：

$$
\mathcal C_h(t)
\ge
c_h
\int_{t-h}^{t+h}|e(u)|^2du
$$

for all local $e$。

原因：

若在該 window：

$$
e'(u)+\frac12e(u)=0,
$$

則：

$$
d\nu=0
$$

於 window 中，所以：

$$
\mathcal C_h(t)=0,
$$

但：

$$
e\not\equiv0.
$$

因此 fixed-center Cauchy observable具有一個 local homogeneous blind direction：

$$
e(u)=Ce^{-u/2}.
$$

---

## Result C · Full moving-center elliptic equivalence

把所有 moving centers積分後：

$$
\boxed{
\mathcal A_h[e]
=
\int_{\mathbb R}
\mathcal C_h(t)dt.
}
$$

則對 compactly supported test error $e$：

$$
\boxed{
m_h\|e\|_2^2
\le
\mathcal A_h[e]
\le
M_h\|e\|_2^2,
}
$$

for some：

$$
0<m_h\le M_h<\infty.
$$

也就是：

$$
\boxed{
\text{full moving-center Cauchy/tent energy}
\asymp
\text{classical normalized PNT }L^2\text{ energy}.
}
$$

---

## Result D · Exponentially weighted equivalence

更一般，對任意 fixed：

$$
\sigma\ge0,
$$

$$
\boxed{
m_{h,\sigma}
\int
e^{-2\sigma t}|e(t)|^2dt
\le
\int
e^{-2\sigma t}\mathcal C_h(t)dt
\le
M_{h,\sigma}
\int
e^{-2\sigma t}|e(t)|^2dt.
}
$$

所以兩個 positive objects具有相同的 Abel / exponential convergence abscissa。

在 AMRAL 既有 zero-exponent bridge下：

$$
\boxed{
\sigma_{\rm abscissa}
=
\Delta_\zeta.
}
$$

因此 Cauchy/Green formulation在 fixed-exponent theorem strength上，是 classical PNT mean-square的一個 elliptic positive repackaging。

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

LOCAL_CAUCHY_TO_PNT_L2_UPPER = CLOSED
LOCAL_STRUCTURE_BLIND_LOWER_BOUND = FALSE

FULL_CENTER_KERNEL = CLOSED
FULL_CENTER_SYMBOL = CLOSED
SYMBOL_STRICT_POSITIVITY = CLOSED
SYMBOL_HIGH_FREQUENCY_POSITIVE_LIMIT = CLOSED

FULL_CENTER_L2_EQUIVALENCE = CLOSED_FOR_COMPACT_TESTS
EXP_WEIGHTED_L2_EQUIVALENCE = CLOSED_FOR_COMPACT_TESTS

PNT_TAIL_APPLICATION = CLOSED_AT_ABSCISSA_LEVEL
BPT_DYADIC_POSITIVE_COMPARISON = CLOSED

SHRINKING_SELBERG_DIRECT_TWO_SIDED_COMPARISON = NOT_AVAILABLE
APERTURE_SENSITIVITY_AUDIT_STILL_REQUIRED

REPRESENTATION_CLOSURE = REACHED_AT_FIXED_EXPONENT_LEVEL
ARITHMETIC_MEANSQUARE_BOUND = STILL_OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Cauchy norm convention

For a real compact signed measure $\alpha$ define：

$$
\boxed{
\|\alpha\|_K^2
=
\iint
e^{-|u-v|}
\,d\alpha(u)d\alpha(v).
}
$$

Under：

$$
\widehat f(\xi)
=
\int_{\mathbb R}
f(u)e^{-i\xi u}du,
$$

we have：

$$
\boxed{
\|\alpha\|_K^2
=
\frac1\pi
\int_{\mathbb R}
\frac{
|\widehat\alpha(\xi)|^2
}{
1+\xi^2
}d\xi.
}
$$

---

# 2. Local source in terms of the classical PNT error

Let：

$$
a_t(u)=T_h(t-u).
$$

Then：

$$
d\nu
=
de+\frac12e\,du.
$$

For regularized test functions：

$$
\mu_t
=
a_t
\left(
e'+\frac12e
\right).
$$

Set：

$$
g_t=a_te.
$$

Because：

$$
a_t'(u)
=
-T_h'(t-u),
$$

we obtain：

$$
\boxed{
\mu_t
=
\left(
\partial_u+\frac12
\right)g_t
+
T_h'(t-u)e(u).
}
$$

This identity extends distributionally by approximation.

---

# 3. Two elementary operator bounds

For：

$$
f\in L^2,
$$

$$
\begin{aligned}
\left\|
\left(
\partial+\frac12
\right)f
\right\|_K^2
&=
\frac1\pi
\int
\frac{
\xi^2+\frac14
}{
1+\xi^2
}
|\widehat f(\xi)|^2d\xi
\\
&\le
2\|f\|_2^2.
\end{aligned}
$$

Also：

$$
\boxed{
\|f\|_K^2
\le
2\|f\|_2^2.
}
$$

Therefore：

$$
\|\mu_t\|_K
\le
\sqrt2
\left(
\|g_t\|_2
+
\|T_h'(t-\cdot)e\|_2
\right).
$$

---

# 4. Local positive upper comparison

Since：

$$
|T_h|\le h,
$$

and：

$$
|T_h'|=1
$$

almost everywhere on：

$$
(-h,h),
$$

we have：

$$
\|g_t\|_2
\le
h
\left(
\int_{t-h}^{t+h}|e|^2
\right)^{1/2},
$$

$$
\|T_h'e\|_2
\le
\left(
\int_{t-h}^{t+h}|e|^2
\right)^{1/2}.
$$

Hence：

## Theorem 4.1 · Local PNT mean-square upper bound

$$
\boxed{
\mathcal C_h(t)
\le
2(h+1)^2
\int_{t-h}^{t+h}
|e(u)|^2du.
}
$$

This is sharper than the earlier generic innovation-primitive $H^{-1}$ upper bound because it compares directly to the normalized PNT error.

---

# 5. Unit-block positive comparison

Define：

$$
\boxed{
\mathscr W_h(T)
=
\int_T^{T+1}
\mathcal C_h(t)dt.
}
$$

Integrating Theorem 4.1 and using Fubini：

$$
\boxed{
\mathscr W_h(T)
\le
2(h+1)^2
\min(1,2h)
\int_{T-h}^{T+1+h}
|e(u)|^2du.
}
$$

For：

$$
h=\log2,
$$

we have：

$$
2h>1,
$$

so：

$$
\boxed{
\mathscr W_{\log2}(T)
\le
2(1+\log2)^2
\int_{T-\log2}^{T+1+\log2}
|e(u)|^2du.
}
$$

---

# 6. Return to $x$-coordinates

Let：

$$
X=e^T.
$$

Since：

$$
e(u)
=
\frac{
E(e^u)
}{
e^{u/2}
},
$$

and：

$$
du=\frac{dx}{x},
$$

we obtain：

$$
\boxed{
|e(u)|^2du
=
\frac{
|E(x)|^2
}{
x^2
}dx.
}
$$

Therefore：

$$
\boxed{
\mathscr W_{\log2}(\log X)
\le
2(1+\log2)^2
\int_{X/2}^{2eX}
\frac{
|E(x)|^2
}{
x^2
}dx.
}
$$

---

# 7. Brent–Platt–Trudgian dyadic mean square

Define：

$$
\boxed{
I(X)
=
\int_X^{2X}
|E(x)|^2dx.
}
$$

For：

$$
x\in[X,2X],
$$

$$
\frac1{4X^2}
\le
\frac1{x^2}
\le
\frac1{X^2}.
$$

Thus：

$$
\boxed{
\frac{
I(X)
}{
4X^2
}
\le
\int_X^{2X}
\frac{
|E(x)|^2
}{
x^2
}dx
\le
\frac{
I(X)
}{
X^2
}.
}
$$

So the log-normalized PNT mean square is dyadically equivalent to：

$$
I(X)/X^2.
$$

---

# 8. Explicit local BPT-to-AMRAL bound

The interval：

$$
[X/2,2eX]
$$

is contained in：

$$
[X/2,8X].
$$

Cover it by：

$$
[X/2,X],
\quad
[X,2X],
\quad
[2X,4X],
\quad
[4X,8X].
$$

Therefore：

## Theorem 8.1

$$
\boxed{
\begin{aligned}
\mathscr W_{\log2}(\log X)
&\le
2(1+\log2)^2
\Bigg[
\frac{
I(X/2)
}{
(X/2)^2
}
\\
&\qquad
+
\frac{
I(X)
}{
X^2
}
+
\frac{
I(2X)
}{
(2X)^2
}
+
\frac{
I(4X)
}{
(4X)^2
}
\Bigg].
\end{aligned}
}
$$

Thus any fixed-power improvement in the classical PNT mean square transfers to the AMRAL Cauchy block with no exponent tax.

---

# 9. Fixed-center lower bound no-go

Consider any interval containing：

$$
[t-h,t+h].
$$

Take：

$$
e(u)=Ce^{-u/2}
$$

on that interval.

Then：

$$
e'+\frac12e=0.
$$

Therefore：

$$
d\nu=0
$$

inside the local window and：

$$
\boxed{
\mathcal C_h(t)=0.
}
$$

But：

$$
\boxed{
\int_{t-h}^{t+h}|e(u)|^2du>0.
}
$$

Hence：

## Theorem 9.1

No universal constant：

$$
c_h>0
$$

can satisfy：

$$
\mathcal C_h(t)
\ge
c_h
\int_{t-h}^{t+h}|e(u)|^2du
$$

for arbitrary local test errors.

This is a genuine homogeneous-mode obstruction.

---

# 10. Why moving centers restore coercivity

Although one fixed center can miss the homogeneous mode, the window edges move.

A compactly supported nonzero $e$ cannot satisfy：

$$
e'+\frac12e=0
$$

through every moving window without generating edge innovation.

The full moving-center ensemble therefore regains coercivity.

---

# 11. Full moving-center energy

For compactly supported test $e$, define：

$$
\boxed{
\mathcal A_h[e]
=
\int_{\mathbb R}
\mathcal C_h(t)dt.
}
$$

Use：

$$
\nu=
\left(
\partial+\frac12
\right)e.
$$

From the v3.1 lifecycle integration：

$$
\boxed{
\mathcal A_h[e]
=
\iint
H_h(u-v)
\,d\nu(u)d\nu(v),
}
$$

where：

$$
\boxed{
H_h(d)
=
e^{-|d|}
C_h(d).
}
$$

---

# 12. Full-center Fourier symbol

Because：

$$
C_h
=
T_h\ast\widetilde T_h,
$$

$$
\widehat C_h(\xi)
=
|\widehat T_h(\xi)|^2.
$$

Also：

$$
\widehat{
e^{-|\cdot|}
}(\xi)
=
\frac2{1+\xi^2}.
$$

Therefore：

$$
\boxed{
\widehat H_h(\xi)
=
\frac1{2\pi}
\left[
\frac2{1+\cdot^2}
\ast
|\widehat T_h|^2
\right](\xi).
}
$$

Since the Lorentzian factor is strictly positive and：

$$
|\widehat T_h|^2
$$

is nonnegative and nonzero：

$$
\boxed{
\widehat H_h(\xi)>0
\quad
\forall\xi\in\mathbb R.
}
$$

---

# 13. Elliptic symbol

Fourier transforming：

$$
\nu=
\left(
\partial+\frac12
\right)e
$$

gives：

$$
|\widehat\nu(\xi)|^2
=
\left(
\xi^2+\frac14
\right)
|\widehat e(\xi)|^2.
$$

Hence：

## Theorem 13.1 · Full-center spectral representation

$$
\boxed{
\mathcal A_h[e]
=
\frac1{2\pi}
\int_{\mathbb R}
S_h(\xi)
|\widehat e(\xi)|^2d\xi,
}
$$

where：

$$
\boxed{
S_h(\xi)
=
\left(
\xi^2+\frac14
\right)
\widehat H_h(\xi).
}
$$

---

# 14. High-frequency limit

The kernel：

$$
H_h(d)
=
e^{-|d|}C_h(d)
$$

has a derivative jump at：

$$
d=0.
$$

Since：

$$
C_h(0)=\frac{2h^3}{3},
$$

$$
H_h'(0^+)
=
-C_h(0),
$$

$$
H_h'(0^-)
=
+C_h(0).
$$

Thus the derivative jump is：

$$
-\frac{4h^3}{3}.
$$

Standard Fourier asymptotics for a derivative jump give：

$$
\boxed{
\lim_{|\xi|\to\infty}
\xi^2
\widehat H_h(\xi)
=
\frac{4h^3}{3}.
}
$$

Therefore：

$$
\boxed{
\lim_{|\xi|\to\infty}
S_h(\xi)
=
\frac{4h^3}{3}
>0.
}
$$

---

# 15. Full-center elliptic equivalence

We now have：

1. $S_h$ continuous；
2. $S_h(\xi)>0$ everywhere；
3. $S_h(\xi)\to4h^3/3>0$ at infinity。

Therefore：

$$
\boxed{
m_h
=
\inf_\xi S_h(\xi)
>0,
}
$$

and：

$$
\boxed{
M_h
=
\sup_\xi S_h(\xi)
<\infty.
}
$$

By Parseval：

## Theorem 15.1 · Elliptic mean-square equivalence

$$
\boxed{
m_h
\|e\|_2^2
\le
\mathcal A_h[e]
\le
M_h
\|e\|_2^2.
}
$$

This is a genuine two-sided positive norm equivalence.

---

# 16. Reference symbol for $h=\log2$

Numerically, on a broad reference grid：

$$
h=\log2
$$

gives approximately：

$$
\boxed{
m_h
\approx
0.0428610,
}
$$

$$
\boxed{
M_h
\approx
1.0930.
}
$$

The high-frequency limit is：

$$
\boxed{
\frac{4h^3}{3}
\approx
0.444033.
}
$$

These numerical values are not part of the proof of positivity; only existence of finite positive $m_h,M_h$ is used analytically.

---

# 17. Exponentially weighted moving-center energy

Fix：

$$
\sigma\ge0.
$$

Define：

$$
\boxed{
\mathcal A_{h,\sigma}[e]
=
\int_{\mathbb R}
e^{-2\sigma t}
\mathcal C_h(t)dt.
}
$$

Set：

$$
\boxed{
e_\sigma(u)
=
e^{-\sigma u}e(u).
}
$$

Also define：

$$
\boxed{
g_{h,\sigma}(r)
=
e^{-\sigma r}T_h(r).
}
$$

---

# 18. Weighted autocorrelation kernel

Set：

$$
\boxed{
C_{h,\sigma}(d)
=
\int_{\mathbb R}
g_{h,\sigma}(r)
g_{h,\sigma}(r+d)dr.
}
$$

Then：

$$
\boxed{
C_{h,\sigma}
=
g_{h,\sigma}
\ast
\widetilde g_{h,\sigma}.
}
$$

Thus：

$$
\widehat C_{h,\sigma}
=
|
\widehat g_{h,\sigma}
|^2
\ge0.
$$

Define：

$$
\boxed{
H_{h,\sigma}(d)
=
e^{-|d|}
C_{h,\sigma}(d).
}
$$

---

# 19. Exact exponential-weight factorization

Using：

$$
t=\frac{u+v}{2}+s,
$$

one factors：

$$
e^{-2\sigma t}
=
e^{-\sigma(u+v)}
e^{-2\sigma s}.
$$

Therefore：

$$
\boxed{
\mathcal A_{h,\sigma}[e]
=
\iint
H_{h,\sigma}(u-v)
\,d\widetilde\nu_\sigma(u)
d\widetilde\nu_\sigma(v),
}
$$

where：

$$
d\widetilde\nu_\sigma(u)
=
e^{-\sigma u}d\nu(u).
$$

But：

$$
\boxed{
d\widetilde\nu_\sigma
=
\left(
\partial
+
\sigma
+
\frac12
\right)e_\sigma.
}
$$

---

# 20. Weighted elliptic symbol

Hence：

$$
\boxed{
\mathcal A_{h,\sigma}[e]
=
\frac1{2\pi}
\int
S_{h,\sigma}(\xi)
|
\widehat e_\sigma(\xi)
|^2d\xi,
}
$$

with：

$$
\boxed{
S_{h,\sigma}(\xi)
=
\left[
\xi^2+
\left(
\sigma+\frac12
\right)^2
\right]
\widehat H_{h,\sigma}(\xi).
}
$$

As before：

$$
\widehat H_{h,\sigma}(\xi)>0.
$$

---

# 21. Weighted high-frequency limit

Since：

$$
C_{h,\sigma}(0)
=
\int
e^{-2\sigma r}
T_h(r)^2dr
>0,
$$

the cusp of：

$$
e^{-|d|}
$$

gives：

$$
\boxed{
\lim_{|\xi|\to\infty}
\xi^2
\widehat H_{h,\sigma}(\xi)
=
2C_{h,\sigma}(0).
}
$$

Therefore：

$$
\boxed{
\lim_{|\xi|\to\infty}
S_{h,\sigma}(\xi)
=
2C_{h,\sigma}(0)
>0.
}
$$

---

# 22. Weighted norm equivalence

For every fixed：

$$
h>0,
\qquad
\sigma\ge0,
$$

there exist：

$$
0<m_{h,\sigma}
\le
M_{h,\sigma}
<\infty
$$

such that：

## Theorem 22.1

$$
\boxed{
m_{h,\sigma}
\int
e^{-2\sigma t}|e(t)|^2dt
\le
\mathcal A_{h,\sigma}[e]
\le
M_{h,\sigma}
\int
e^{-2\sigma t}|e(t)|^2dt.
}
$$

This is the weighted elliptic equivalence.

---

# 23. Abel convergence abscissa

For an actual PNT tail, compact cutoff / initial-boundary corrections occupy only fixed finite log-time regions and do not change convergence abscissae.

Therefore the quantities：

$$
\int^\infty
e^{-2\sigma t}
\mathcal C_h(t)dt
$$

and：

$$
\int^\infty
e^{-2\sigma t}
|e(t)|^2dt
$$

have the same convergence threshold。

Combined with the previous AMRAL mean-square / zero-exponent bridge：

$$
\boxed{
\sigma_{\rm abscissa}
=
\Delta_\zeta.
}
$$

Thus the canonical Cauchy energy and classical normalized PNT mean square are equivalent at the fixed horizontal-exponent level.

---

# 24. Classical dyadic exponent class

Since：

$$
\int_{\log X}^{\log2X}
|e(t)|^2dt
=
\int_X^{2X}
\frac{
|E(x)|^2
}{
x^2
}dx,
$$

and Section 7 gives dyadic equivalence with：

$$
I(X)/X^2,
$$

the following exponent classes coincide：

```text
AMRAL positive Cauchy block energy

normalized PNT log-mean-square

I(X) / X^2

rightmost-zero quadratic exponent.
```

In v2.1 notation：

$$
\boxed{
\beta
=
\delta_I-2
=
2\Theta-1.
}
$$

---

# 25. Consequence for fixed-power progress

Suppose：

$$
\boxed{
I(X)
\ll
X^{3-\kappa+o(1)}.
}
$$

Then：

$$
\delta_I
\le
3-\kappa,
$$

so：

$$
\boxed{
\beta
\le
1-\kappa.
}
$$

Equivalently：

$$
\boxed{
\Theta
\le
1-\frac{\kappa}{2}.
}
$$

Thus any fixed power saving in classical PNT mean square is already exactly the type of progress sought by the AMRAL Cauchy route.

No extra exponent gain is created by the Green representation.

---

# 26. Relation to Selberg integrals

Zaccagnini studies Selberg-type mean squares：

$$
J(x,\theta)
=
\int_x^{2x}
|
\psi(t)
-
\psi(t-\theta t)
-
\theta t
|^2dt.
$$

At full proportional aperture：

$$
\theta=1,
$$

this is essentially the global PNT mean square：

$$
I(x).
$$

For shrinking：

$$
\theta\to0,
$$

the object becomes a genuine short-interval Selberg integral。

v2.2–v2.3 already showed that shrinking-aperture estimates require sensitivity normalization and can create false fixed-power savings.

Therefore the v3.4 positive equivalence should be read as：

$$
\boxed{
\text{Cauchy energy}
\leftrightarrow
\text{full-aperture normalized PNT/Selberg mean-square},
}
$$

not as a free two-sided comparison with arbitrary short-interval Selberg integrals.

---

# 27. Weighted Selberg / correlation literature

Coppola–Laporta show that weighted Selberg integrals are quadratic means which can be rewritten as averages of arithmetic correlations via dispersion, and Gallagher-type weighted inequalities connect exponential-sum means to such short-interval quadratic forms.

This confirms that changing smooth positive kernels is a natural analytic technique.

But v3.4 shows a limitation：

> generic positive smoothing does not by itself lower the fixed exponent required from the centered prime correlation.

The number-theoretic saving still has to come from the arithmetic input.

---

# 28. Representation closure

The AMRAL line has now passed through：

```text
Weil / Suzuki screw function
-> fixed aperture discrepancy
-> local positive energy
-> PNT FIR filter
-> twisted correlations
-> Cauchy scalar
-> Green / causal state
-> finite-dimensional moving state
-> work / lifecycle decomposition
-> positive spectral hierarchy
-> classical normalized PNT mean square.
```

At fixed-exponent level, the final positive operator is elliptically equivalent to the classical mean-square object.

Therefore：

$$
\boxed{
\text{REPRESENTATION PROBLEM}
}
$$

is no longer the main obstacle.

The main obstacle is now explicitly：

$$
\boxed{
\text{ARITHMETIC MEAN-SQUARE EXPONENT IMPROVEMENT}.
}
$$

---

# 29. Strategic consequence for autonomous AI

Future research agents should reject proposals whose only achievement is another RH-equivalent positive representation unless it supplies at least one of：

1. a strictly stronger known arithmetic theorem applies to the new form；
2. a provable fixed-exponent comparison improves；
3. a formalization / certificate bottleneck is materially removed；
4. a new arithmetic cancellation lemma is introduced。

Otherwise：

```text
NEW REPRESENTATION
WITHOUT ARITHMETIC STRENGTH GAIN
=
DEPRIORITIZE.
```

This prevents autonomous research from endlessly generating equivalent criteria.

---

# 30. New smallest arithmetic GAP

The canonical fixed-power target can now be stated in classical language：

Find any：

$$
\boxed{
\kappa>0
}
$$

such that：

$$
\boxed{
I(X)
=
\int_X^{2X}
|\psi(x)-x|^2dx
\ll
X^{3-\kappa+o(1)}.
}
$$

Equivalently：

$$
\boxed{
\mathscr W_h(T)
\ll
e^{(1-\kappa)T+o(T)}.
}
$$

Either theorem gives：

$$
\boxed{
\Theta
\le
1-\frac{\kappa}{2}.
}
$$

The RH scale is：

$$
\boxed{
I(X)\ll X^{2+o(1)},
}
$$

or：

$$
\boxed{
\mathscr W_h(T)=e^{o(T)}.
}
$$

---

# 31. Suggested v3.5 direction

Recommended：

`RH-MeanSquare-ArithmeticGap v3.5`

Do **not** invent another criterion first.

Tasks：

1. fix the target：
   $$
   I(X)\ll X^{3-\kappa};
   $$
2. expand $I(X)$ through a truncated explicit formula / Dirichlet polynomial；
3. isolate exactly which diagonal term forces the current $\kappa=0$ baseline；
4. isolate the minimal off-diagonal cancellation needed for：
   $$
   \kappa>0;
   $$
5. compare three genuine arithmetic mechanisms：
   - zero-density；
   - dispersion / prime correlations；
   - bilinear Dirichlet-polynomial cancellation；
6. translate every proposed saving back to：
   $$
   \kappa;
   $$
7. reject all logarithmic / subpower improvements as fixed-exponent non-progress；
8. formalize the first arithmetic lemma whose proof would imply：
   $$
   \kappa>0.
   $$

This marks the transition from representation engineering back to direct number-theoretic attack.

---

# 32. GAP ledger

## CLOSED / AUDITED

### G1. Local Cauchy-to-PNT positive upper comparison

```text
CLOSED
```

### G2. Local two-sided coercivity

```text
NO_GO_STRUCTURE_BLIND
```

### G3. Full-center elliptic symbol

```text
CLOSED
```

### G4. Full-center $L^2$ equivalence

```text
CLOSED
```

### G5. Exponentially weighted equivalence

```text
CLOSED
```

### G6. BPT dyadic positive comparison

```text
CLOSED
```

### G7. Fixed-exponent representation discount

```text
NONE
```

### G8. Representation closure

```text
REACHED
```

---

## OPEN

### G9. Any arithmetic fixed power saving

```text
OPEN
```

$$
\kappa>0.
$$

### G10. RH-scale mean square

```text
OPEN_RH_COMPLETE
```

### G11. RH

```text
OPEN
```

---

# 33. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

ELLIPTIC NORM EQUIVALENCE = EXACT FOR COMPACT TESTS
PNT TAIL ABSCISSA APPLICATION = ASYMPTOTIC / CUTOFF REDUCTION

REFERENCE SYMBOL MIN/MAX = NUMERICAL ONLY

NO FIXED-POWER ARITHMETIC SAVING HAS BEEN PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden：

$$
\text{elliptic equivalence}
\Longrightarrow
\text{new zero strip}.
$$

Forbidden：

$$
\text{better representation}
\Longrightarrow
\text{easier arithmetic theorem}.
$$

Forbidden：

$$
\text{short-interval Selberg saving}
\Longrightarrow
\kappa>0
$$

without aperture sensitivity normalization.

---

# 34. One-line status

> v3.4 closes the positive-kernel representation audit by showing that the canonical Cauchy/tent energy is an elliptic repackaging of the classical normalized PNT mean square. Pointwise, the Cauchy energy admits the positive upper bound $\mathcal C_h(t)\le2(h+1)^2\int_{t-h}^{t+h}|e(u)|^2du$, so Brent–Platt–Trudgian-type mean-square estimates transfer without fixed-exponent loss. A converse at one fixed center is impossible because the homogeneous local mode $e'+e/2=0$ is invisible to the local innovation. But after integrating over all moving centers, the lifecycle kernel $H_h=e^{-|\cdot|}C_h$ yields the elliptic Fourier symbol $S_h(\xi)=(\xi^2+1/4)\widehat H_h(\xi)$; it is continuous and strictly positive, and tends to $4h^3/3$ at high frequency, giving a two-sided $L^2$ norm equivalence. The same construction survives exponential time weighting, so Cauchy energy and classical normalized PNT mean square have the same Abel convergence abscissa and hence the same rightmost-zero fixed exponent. For $h=\log2$, the reference symbol is well conditioned rather than degenerate. The strategic consequence is representation closure: the Green/causal/state-machine formulations remain valuable for AI reasoning and certificates, but no theorem-strength discount has been obtained. The next phase should stop generating RH-equivalent representations and directly attack the arithmetic mean-square target $I(X)\ll X^{3-\kappa}$ for any fixed $\kappa>0$.

---

# 35. References

1. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   DOI: https://doi.org/10.1016/j.jnt.2021.09.016  
   arXiv: https://arxiv.org/abs/2008.06140

2. Alessandro Zaccagnini, **Primes in almost all short intervals**, *Acta Arithmetica* 84 (1998), 225–244.

3. Giovanni Coppola, Maurizio Laporta, **Generations of Correlation Averages**, *Journal of Numbers* (2014), Article ID 140840.  
   DOI: https://doi.org/10.1155/2014/140840

4. Giovanni Coppola, Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, arXiv:1411.1739.

5. AMRAL, **RH-PositiveKernel-InnovationSpectrum v3.3**.

6. AMRAL, **RH-ArithmeticInnovation-EnergyGate v2.9**.

---

# 36. Provenance

研究主導：Neo.K

v3.4 local PNT mean-square comparison、full-center elliptic symbol、weighted equivalence、BPT dyadic bridge、representation-closure audit、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第四弧線 positive-kernel / classical mean-square equivalence 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
