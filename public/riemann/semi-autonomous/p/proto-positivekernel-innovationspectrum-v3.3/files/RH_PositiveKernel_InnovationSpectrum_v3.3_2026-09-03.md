工程紀錄 · 第四弧線 v3.3 · 2026-09-03 · POSITIVE_SPECTRAL_IRREDUCIBILITY · RESOLVENT_HIERARCHY · SPECTRAL_FALSE_KAPPA · RH_CLAIM_FALSE

# Positive Kernel Innovation Spectrum：固定正頻窗不可約性、Resolvent Hierarchy 與 Spectral False-$\kappa$

**RH-PositiveKernel-InnovationSpectrum v3.3**

本節點承接：

- `RH-CauchyPoisson-TwistScalarization v2.5`
- `RH-BandlimitedTwist-AveragingGate v2.4`
- `RH-CompletedReward-CorrelationKernel v3.2`

v3.2 已決定：signed completed-reward branch保留作 diagnostics / certificate，但不再作主要 RH closure route。

v3.3 回到 positive spectral energy，問：

> 能否把 RH-complete Cauchy energy切成較弱的 positive spectral pieces，先控制其中一部分，形成真正的 theorem-strength ladder？

本輪答案：

$$
\boxed{
\text{固定 positive spectral slicing 不會自動形成較弱的 RH ladder。}
}
$$

原因是 fixed-aperture zero transfer：

$$
\boxed{
B_h(z)
=
2
\frac{
\cosh(hz)-1
}{
z^2
}
}
$$

對任何 off-axis displacement：

$$
\delta>0
$$

都在整條 vertical line：

$$
z=\delta+iy
$$

上完全無零點。

更精確：

$$
\boxed{
|B_h(\delta+iy)|^2
=
\frac{
4[
\cosh(h\delta)-\cos(hy)
]^2
}{
(\delta^2+y^2)^2
}.
}
$$

因此：

$$
\boxed{
|B_h(\delta+iy)|>0
\quad
\forall y\in\mathbb R.
}
$$

所以任何固定：

$$
w(\tau)\ge0,
\qquad
w\not\equiv0,
$$

都有 off-axis self-mode coefficient：

$$
\boxed{
\Xi_{h,w}(\delta,\gamma)
=
\int_{\mathbb R}
w(\tau)
\left|
B_h(
\delta+i(\gamma-\tau)
)
\right|^2d\tau
>0.
}
$$

也就是任何固定 nonzero positive spectral piece，都保留同一個 horizontal exponent：

$$
e^{2\delta T}.
$$

因此：

```text
FIXED POSITIVE PIECE
    may have tiny coefficient
    but does NOT have weaker fixed exponent.
```

第二個結果是 spectral analogue of v2.2–v2.3 false-$\kappa$：

若固定形狀的 spectral window搬到：

$$
U(T)=e^{\theta T+o(T)},
$$

則固定 zero mode的 transfer coefficient被壓成：

$$
\boxed{
U(T)^{-4}
=
e^{-4\theta T+o(T)}.
}
$$

所以：

$$
\boxed{
\beta_{\rm corrected}
=
\beta_{\rm raw}
+
4\theta.
}
$$

這個 $4\theta$ 是 tent second-difference vertical smoothing的 energy sensitivity tax。

第三個結果是 positive polynomial-tail resolvent hierarchy：

對任意固定：

$$
p>\frac12,
$$

定義：

$$
\boxed{
\omega_p(\tau)
=
c_p
(1+\tau^2)^{-p},
}
$$

$$
\boxed{
c_p
=
\frac{
\Gamma(p)
}{
\sqrt\pi
\Gamma(p-\frac12)
}.
}
$$

則：

$$
\int_{\mathbb R}
\omega_p(\tau)d\tau
=
1.
$$

定義：

$$
\boxed{
\mathscr W_{h,p}(T)
=
\int_T^{T+1}
\int_{\mathbb R}
\omega_p(\tau)
|\mathcal F_{h,\tau}(t)|^2
d\tau\,dt.
}
$$

每一個固定 $p>1/2$ 都滿足：

$$
\boxed{
RH
\Longrightarrow
\mathscr W_{h,p}(T)=O_h(1),
}
$$

而：

$$
\boxed{
\mathscr W_{h,p}(T)=O(T^A)
\text{ for any finite }A
\Longrightarrow RH.
}
$$

因此 fixed resolvent smoothing order也不產生 theorem-strength ladder。

對 integer $p=m$：

$$
\omega_m
$$

對應：

$$
(1-\partial_u^2)^{-m}
$$

的 positive Green kernel，並可 causal factor成：

$$
(\partial_u+1)^{-m}.
$$

所以 $m=1$ 的 Cauchy kernel是 fixed positive resolvent hierarchy裡最低 causal order的成員。

結論：

$$
\boxed{
\text{positive spectral decomposition具有診斷 / certificate價值，
但目前沒有提供真正 theorem-strength discount。}
}
$$

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

EXACT_OFFAXIS_B_TRANSFER = CLOSED
OFFAXIS_VERTICAL_ZEROS_OF_B_h = NONE

FIXED_POSITIVE_WINDOW_MODE_COEFFICIENT = STRICTLY_POSITIVE
FIXED_POSITIVE_SPECTRAL_PIECE_EXPONENT_DISCOUNT = NONE

MOVING_BAND_U_MINUS_4_LAW = CLOSED
SPECTRAL_MOVING_BAND_CORRECTION = 4 theta

POLYNOMIAL_TAIL_RESOLVENT_HIERARCHY = CLOSED_AS_REDUCTION
P_GT_HALF_RH_BOUNDEDNESS = CLOSED
P_GT_HALF_POLYNOMIAL_SUFFICIENCY = CLOSED

INTEGER_P_GREEN_ORDER = p
INTEGER_P_CAUSAL_ORDER = p

P_EQUAL_1 = MINIMAL_CAUSAL_ORDER_IN_THIS_HIERARCHY

LITTLEWOOD_PALEY_FIXED_PIECES = DIAGNOSTIC_NOT_STRENGTH_LADDER
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Twisted local observable

Recall:

$$
\boxed{
\mathcal F_{h,\tau}(t)
=
\int
T_h(t-u)
e^{-i\tau(u-t)}
\,d\mathfrak I(u).
}
$$

For a hypothetical zero:

$$
\rho
=
\frac12+\delta+i\gamma,
$$

its normalized zero mode is:

$$
e^{(\delta+i\gamma)t}.
$$

The corresponding twisted tent transfer is:

$$
\boxed{
-
B_h(
\delta+i(\gamma-\tau)
)
e^{(\delta+i\gamma)t}.
}
$$

---

# 2. Exact transfer magnitude

Let:

$$
a=h\delta,
$$

$$
b=hy.
$$

Then:

$$
\begin{aligned}
|
\cosh(a+ib)-1
|^2
&=
(
\cosh(a)\cos b-1
)^2
\\
&\quad
+
\sinh^2(a)\sin^2b.
\end{aligned}
$$

Using:

$$
\sinh^2a
=
\cosh^2a-1,
$$

one obtains:

$$
\boxed{
|
\cosh(a+ib)-1
|^2
=
[
\cosh a-\cos b
]^2.
}
$$

Therefore:

## Theorem 2.1 · Exact off-axis transfer

$$
\boxed{
|B_h(\delta+iy)|^2
=
\frac{
4[
\cosh(h\delta)-\cos(hy)
]^2
}{
(\delta^2+y^2)^2
}.
}
$$

---

# 3. No off-axis vertical zeros

For:

$$
\delta>0,
$$

$$
\cosh(h\delta)>1.
$$

Since:

$$
-1\le\cos(hy)\le1,
$$

$$
\boxed{
\cosh(h\delta)-\cos(hy)
\ge
\cosh(h\delta)-1
>0.
}
$$

Thus:

## Theorem 3.1

$$
\boxed{
B_h(\delta+iy)\neq0
\quad
\forall
\delta>0,\,
y\in\mathbb R.
}
$$

So a fixed-aperture second difference cannot spectrally annihilate an off-axis zero at any twist.

---

# 4. Fixed positive spectral piece

Let:

$$
w\in L^1_{\rm loc}(\mathbb R),
$$

with:

$$
w(\tau)\ge0
$$

almost everywhere and:

$$
w\not\equiv0.
$$

Define:

$$
\boxed{
\Xi_{h,w}(\delta,\gamma)
=
\int
w(\tau)
\left|
B_h(
\delta+i(\gamma-\tau)
)
\right|^2d\tau.
}
$$

Whenever the integral is finite, Theorem 3.1 gives:

## Theorem 4.1 · Strict fixed-piece sensitivity

$$
\boxed{
\Xi_{h,w}(\delta,\gamma)>0
}
$$

for every:

$$
\delta>0,
\qquad
\gamma\in\mathbb R.
$$

No fixed positive spectral piece loses the off-axis horizontal exponent.

---

# 5. Zero-mode piece energy

For one zero mode amplitude:

$$
A,
$$

the self contribution to a fixed positive spectral piece is:

$$
\boxed{
|A|^2
\Xi_{h,w}(\delta,\gamma)
e^{2\delta t}.
}
$$

So even if:

$$
\Xi_{h,w}
$$

is extremely small, it is independent of $t$ for fixed $w$ and fixed zero.

Therefore its exponential rate remains:

$$
\boxed{
2\delta.
}
$$

Coefficient size and exponent strength must not be confused.

---

# 6. Fixed compact band

For example choose:

$$
w_{[a,b]}
=
\mathbf1_{[a,b]},
$$

with:

$$
a<b.
$$

Then:

$$
\boxed{
\Xi_{h,[a,b]}(\delta,\gamma)
>0
}
$$

for every off-axis zero.

If:

$$
|\gamma|
$$

is very large relative to the fixed band, then:

$$
\Xi
$$

can be as small as:

$$
O_{\delta,h,a,b}(\gamma^{-4}).
$$

But:

$$
\gamma^{-4}
$$

is a fixed coefficient for a fixed zero ordinate.

It does not change:

$$
e^{2\delta t}.
$$

---

# 7. Fixed positive Littlewood–Paley pieces

Take any nonnegative partition:

$$
1
=
\sum_{j\in\mathbb Z}
\chi_j(\tau)
$$

on the relevant spectral axis.

Define:

$$
w_j(\tau)
=
\omega(\tau)\chi_j(\tau),
$$

where:

$$
\omega(\tau)
=
\frac1{\pi(1+\tau^2)}.
$$

Then:

$$
\boxed{
\mathscr W_h(T)
=
\sum_j
\mathscr W_{h,j}(T),
}
$$

with:

$$
\mathscr W_{h,j}(T)\ge0.
$$

However every fixed nonzero $j$ satisfies the mode-level strict sensitivity of Theorem 4.1.

Therefore:

$$
\boxed{
\text{fixed LP pieces are positive diagnostics,
not a hierarchy of weaker fixed exponents.}
}
$$

This does not contradict classical Littlewood–Paley theory; square functions are designed to decompose positive $L^2$ energy while preserving frequency information.

---

# 8. Moving positive band

Now let:

$$
w_0
$$

be nonnegative, nonzero, compactly supported.

Define:

$$
\boxed{
w_T(\tau)
=
w_0(\tau-U(T)).
}
$$

Assume:

$$
U(T)\to+\infty.
$$

For:

$$
\tau=U(T)+s
$$

with $s$ in a fixed compact set:

$$
|\gamma-\tau|
=
U(T)(1+o(1)).
$$

The exact transfer gives constants:

$$
0<c_-(\delta,h,w_0)
\le
U(T)^4
\Xi_{h,w_T}(\delta,\gamma)
\le
c_+(\delta,h,w_0)
<\infty.
$$

Therefore:

## Theorem 8.1 · Moving-band attenuation

$$
\boxed{
\Xi_{h,w_T}(\delta,\gamma)
\asymp
U(T)^{-4}.
}
$$

---

# 9. Spectral false-$\kappa$ correction

Suppose:

$$
U(T)
=
e^{\theta T+o(T)}.
$$

Then:

$$
\boxed{
\Xi_{h,w_T}
=
e^{-4\theta T+o(T)}.
}
$$

So an off-axis mode appears in the moving piece with exponent:

$$
\boxed{
2\delta-4\theta.
}
$$

Hence a raw piece estimate:

$$
\mathscr W_{h,w_T}(T)
\ll
e^{\beta_{\rm raw}T+o(T)}
$$

can only imply:

$$
2\delta-4\theta
\le
\beta_{\rm raw}.
$$

Therefore define:

$$
\boxed{
\beta_{\rm corrected}
=
\beta_{\rm raw}
+
4\theta.
}
$$

This is the spectral counterpart of the v2.3 aperture sensitivity correction.

---

# 10. Subexponential spectral motion

If:

$$
\log U(T)=o(T),
$$

then:

$$
\theta=0.
$$

Thus:

$$
U(T)^{-4}
=
e^{-o(T)}.
$$

So subexponentially moving spectral windows preserve fixed-exponent sensitivity.

But they still do not create a weaker exponent problem.

---

# 11. General spectral sensitivity tax

For any $T$-dependent positive weight $w_T$, define for a fixed hypothetical zero:

$$
\boxed{
\chi_{w}(\delta,\gamma)
=
-
\liminf_{T\to\infty}
\frac1T
\log
\Xi_{h,w_T}(\delta,\gamma).
}
$$

Then the observed self-mode exponent is:

$$
\boxed{
2\delta-\chi_w(\delta,\gamma).
}
$$

A safe fixed-exponent comparison must add the sensitivity tax back.

For a translated compact band:

$$
\chi_w=4\theta.
$$

This is the general spectral false-progress audit variable.

---

# 12. Polynomial-tail positive hierarchy

For:

$$
p>\frac12,
$$

define:

$$
\boxed{
c_p
=
\frac{
\Gamma(p)
}{
\sqrt\pi
\Gamma(p-\frac12)
},
}
$$

and:

$$
\boxed{
\omega_p(\tau)
=
c_p
(1+\tau^2)^{-p}.
}
$$

Then:

$$
\boxed{
\int_{\mathbb R}
\omega_p(\tau)d\tau=1.
}
$$

Define:

$$
\boxed{
\mathcal C_{h,p}(t)
=
\int
\omega_p(\tau)
|\mathcal F_{h,\tau}(t)|^2d\tau.
}
$$

and:

$$
\boxed{
\mathscr W_{h,p}(T)
=
\int_T^{T+1}
\mathcal C_{h,p}(t)dt.
}
$$

---

# 13. RH implies bounded $p$-energy

Under RH, v2.5 gives:

$$
\boxed{
|\mathcal F_{h,\tau}(t)|
\ll_h
\log(2+|\tau|)
}
$$

uniformly in $t$.

Therefore:

$$
\mathcal C_{h,p}(t)
\ll
\int
\frac{
\log^2(2+|\tau|)
}{
(1+\tau^2)^p
}d\tau.
$$

The integral converges iff:

$$
p>\frac12.
$$

Thus:

## Theorem 13.1

For every fixed:

$$
p>\frac12,
$$

$$
\boxed{
RH
\Longrightarrow
\mathscr W_{h,p}(T)=O_{h,p}(1).
}
$$

---

# 14. Bandlimited reproducing control

For fixed $t$, define:

$$
q_t(\tau)
=
|\mathcal F_{h,\tau}(t)|^2.
$$

v2.4 established:

$$
\boxed{
\operatorname{supp}
\widehat q_t
\subset[-2h,2h].
}
$$

Choose:

$$
\phi\in\mathcal S(\mathbb R)
$$

such that:

$$
\widehat\phi=1
$$

on a neighbourhood of:

$$
[-2h,2h].
$$

Then:

$$
\boxed{
q_t=q_t\ast\phi.
}
$$

Hence at:

$$
\tau=0,
$$

$$
q_t(0)
\le
\int
q_t(s)
|\phi(s)|ds.
$$

---

# 15. Polynomial tail is enough to recover the untwisted energy

Since $\phi$ is Schwartz:

$$
\boxed{
C_{h,p,\phi}
=
\sup_s
\frac{
|\phi(s)|
}{
\omega_p(s)
}
<\infty
}
$$

for every fixed finite:

$$
p.
$$

Therefore:

$$
\boxed{
q_t(0)
\le
C_{h,p,\phi}
\mathcal C_{h,p}(t).
}
$$

But:

$$
q_t(0)
=
|\mathfrak E_h(e^t)|^2.
$$

So:

$$
\boxed{
\int_T^{T+1}
|\mathfrak E_h(e^t)|^2dt
\le
C_{h,p}
\mathscr W_{h,p}(T).
}
$$

---

# 16. Polynomial $p$-energy implies RH

Suppose:

$$
\boxed{
\mathscr W_{h,p}(T)
=
O(T^A)
}
$$

for some finite:

$$
A.
$$

Then Section 15 gives polynomial untwisted unit-block energy.

Summing unit blocks gives polynomial cumulative untwisted energy.

v1.7 proves that any finite polynomial cumulative fixed-aperture energy bound implies RH.

Therefore:

## Theorem 16.1 · Positive resolvent hierarchy criterion

For every fixed:

$$
h>0,
$$

and:

$$
p>\frac12,
$$

$$
\boxed{
RH
\Longleftrightarrow
\mathscr W_{h,p}(T)=O_{h,p}(1).
}
$$

Moreover:

$$
\boxed{
\mathscr W_{h,p}(T)=O(T^A)
\text{ for any finite }A
\Longrightarrow RH.
}
$$

No novelty priority is claimed for the general weighted-Paley–Wiener mechanism.

---

# 17. Integer resolvent powers

Let:

$$
p=m\in\mathbb N.
$$

The multiplier:

$$
(1+\tau^2)^{-m}
$$

is the Fourier multiplier of:

$$
(1-\partial_u^2)^{-m}.
$$

So the pair kernel:

$$
K_m(d)
=
\int
\omega_m(\tau)e^{-i\tau d}d\tau
$$

is the normalized Green kernel of the $m$-th resolvent power.

Examples:

### $m=1$

$$
\boxed{
K_1(d)
=
e^{-|d|}.
}
$$

### $m=2$

$$
\boxed{
K_2(d)
=
(1+|d|)
e^{-|d|}.
}
$$

### $m=3$

$$
\boxed{
K_3(d)
=
\frac{
d^2+3|d|+3
}{
3
}
e^{-|d|}.
}
$$

All satisfy:

$$
K_m(0)=1.
$$

---

# 18. Causal factorization of integer hierarchy

Let:

$$
s_m
$$

solve:

$$
\boxed{
(\partial_u+1)^m
s_m
=
\mu.
}
$$

Then:

$$
\widehat s_m(\tau)
=
\frac{
\widehat\mu(\tau)
}{
(1+i\tau)^m
}.
$$

Parseval gives:

$$
\boxed{
\int
\omega_m(\tau)
|\widehat\mu(\tau)|^2d\tau
=
2\pi c_m
\|s_m\|_2^2.
}
$$

Thus the integer hierarchy has causal state order:

$$
\boxed{m}.
$$

---

# 19. Why $m=1$ is the engineering Pareto point

Every fixed:

$$
m\ge1
$$

is RH-complete by Theorem 16.1.

Increasing $m$ gives:

- stronger high-twist suppression;
- smoother spatial Green kernel;
- higher causal filter order;
- no fixed-exponent theorem discount.

Therefore:

$$
\boxed{
m=1
}
$$

has the smallest causal state dimension while retaining the same RH theorem strength.

This justifies keeping the v2.5 Cauchy kernel as the canonical main positive kernel unless another arithmetic theorem favors a higher-order kernel.

---

# 20. Gaussian / exponentially decaying spectral weights

A faster-decaying fixed weight such as:

$$
e^{-a\tau^2}
$$

also has strictly positive zero-mode coefficient.

So mode-level exponent sensitivity remains.

However the simple weighted reproducing proof of Section 15 uses the fact that:

$$
1/\omega_p
$$

has only polynomial growth.

For exponentially decaying weights the global point-evaluation domination requires a separate weighted Paley–Wiener theorem.

Therefore v3.3 does not automatically promote every fast-decaying fixed weight to a full RH-equivalent criterion.

The strict mode-level statement remains valid.

---

# 21. Positive-kernel comparison does not automatically create a ladder

If:

$$
0\le w_1\le Cw_2,
$$

then:

$$
\mathscr W_{w_1}
\le
C\mathscr W_{w_2}.
$$

This is useful for upper-bound transfer.

But because fixed nonzero positive pieces retain the same off-axis exponent, making the kernel spectrally smaller does not by itself produce a weaker fixed-strip theorem.

The real question remains:

> Is the smaller positive quadratic form arithmetically easier to estimate at a stronger exponent?

That requires a new number-theoretic inequality, not spectral slicing alone.

---

# 22. Method audit against known harmonic analysis

Classical Littlewood–Paley theory uses positive square-function decompositions to encode frequency-localized $L^p/L^2$ information.

Poisson-semigroup square functions likewise decompose positive harmonic energy across scales.

Weighted Paley–Wiener theory studies reproducing / sampling inequalities under nontrivial weights.

These frameworks validate the harmonic-analysis language used here.

But none of these generic theorems supplies the missing centered von-Mangoldt exponent improvement.

The arithmetic barrier remains separate.

---

# 23. What positive slicing is still useful for

Even without theorem-strength discount, spectral pieces are useful for:

1. diagnosing which twist ranges dominate finite data;
2. independent certificate channels;
3. conditioning the numerical resolvent;
4. testing proposed arithmetic estimates;
5. locating false high-frequency savings;
6. formal positive-kernel decomposition.

So the branch remains useful as proof engineering.

---

# 24. Autonomous false-progress gate

For every spectral-piece candidate record:

```text
weight family w_T
fixed or moving
spectral center U(T)
spectral width
normalization
zero-transfer Xi(delta,gamma,T)
sensitivity tax chi
raw beta
corrected beta
```

Reject:

```text
RAW HIGH-FREQUENCY SAVING
```

if its corrected exponent is not improved after:

$$
\chi
$$

is restored.

For translated fixed-shape bands:

$$
\boxed{
\chi=4\theta.
}
$$

---

# 25. Branch decision

The initial v3.3 hope was:

```text
full positive Cauchy energy
    ->
positive pieces
    ->
some easier weaker piece
    ->
progress ladder
```

The audit gives instead:

```text
every fixed nonzero positive piece
    keeps the same off-axis exponent

moving pieces
    require sensitivity correction

fixed polynomial-tail resolvent powers
    remain RH-complete
```

Therefore:

$$
\boxed{
\text{positive spectral slicing alone does not provide the desired theorem-strength ladder.}
}
$$

---

# 26. New smallest positive-kernel question

The next useful question is not:

> Which spectral band should we keep?

It is:

> Is there a positive arithmetic kernel whose quadratic form is provably comparable to a known Selberg / PNT mean-square quantity at a stronger exponent?

That is a number-theoretic comparison problem.

Spectral decomposition is now sufficiently audited.

---

# 27. Suggested v3.4 direction

Recommended:

`RH-PositiveKernel-SelbergComparison v3.4`

Tasks:

1. keep canonical:
   $$
   p=1;
   $$
2. write the Cauchy/tent quadratic form directly in $x$-coordinates;
3. compare it with classical:
   $$
   I(X)
   =
   \int_X^{2X}
   (\psi(x)-x)^2dx;
   $$
4. derive sharp two-sided inequalities, not only the loose v2.9 $H^{-1}$ upper bound;
5. identify exactly how much cancellation is lost in:
   $$
   \mathcal C_h
   \le
   C\int|\mathfrak b|^2;
   $$
6. seek a positive lower/upper comparison with weighted Selberg integrals;
7. test whether a known unconditional theorem controls a nontrivial positive fraction of the RH-complete Cauchy energy;
8. reject any comparison whose constants hide an exponent loss.

This is more promising than further frequency slicing.

---

# 28. GAP ledger

## CLOSED / AUDITED

### G1. Exact off-axis transfer magnitude

```text
CLOSED
```

### G2. Fixed positive piece strict mode sensitivity

```text
CLOSED
```

### G3. Moving-band $U^{-4}$ attenuation

```text
CLOSED
```

### G4. Spectral correction $4\theta$

```text
CLOSED
```

### G5. Polynomial-tail positive resolvent hierarchy

```text
CLOSED_AS_REDUCTION
```

### G6. Fixed spectral slicing theorem discount

```text
NONE FOUND
```

### G7. $p=1$ minimal causal-order choice

```text
CLOSED_WITHIN_RESOLVENT_HIERARCHY
```

---

## OPEN

### G8. Positive arithmetic kernel comparison

```text
OPEN
```

### G9. Any fixed exponent $\sigma<1/2$

```text
OPEN
```

### G10. Polynomial positive Cauchy energy

```text
OPEN_RH_COMPLETE
```

### G11. RH

```text
OPEN
```

---

# 29. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

FIXED POSITIVE WINDOW MODE SENSITIVITY = EXACT
FULL FIXED-COMPACT-WINDOW RH EQUIVALENCE = NOT CLAIMED GENERALLY

POLYNOMIAL-TAIL p>1/2 HIERARCHY = RH-EQUIVALENT REDUCTION
VIA BANDLIMITED REPRODUCING ARGUMENT

MOVING-BAND CORRECTION = ZERO-MODE SENSITIVITY LAW

NO ARITHMETIC EXPONENT IMPROVEMENT HAS BEEN PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{positive piece is smaller}
\Longrightarrow
\text{weaker RH theorem}.
$$

Forbidden:

$$
\gamma^{-4}\text{ coefficient}
\Longrightarrow
\text{horizontal exponent loss}.
$$

Forbidden:

$$
\text{raw moving-band saving}
\Longrightarrow
\text{fixed-strip progress}
$$

without adding back the spectral sensitivity tax.

---

# 30. One-line status

> v3.3 audits the positive-spectrum strategy and finds a spectral irreducibility phenomenon. The fixed-aperture zero transfer has exact magnitude $|B_h(\delta+iy)|^2=4[\cosh(h\delta)-\cos(hy)]^2/(\delta^2+y^2)^2$, so for every off-axis displacement $\delta>0$ it is nonzero at every vertical frequency. Consequently any fixed nonzero positive spectral window has strictly positive self-mode coefficient and retains the full $e^{2\delta T}$ horizontal exponent, even when the coefficient for a very high zero is only of order $\gamma^{-4}$. Fixed positive Littlewood–Paley pieces therefore do not form a weaker theorem-strength ladder. If a fixed-shape band is moved to frequency $U(T)=e^{\theta T+o(T)}$, its zero sensitivity is attenuated by $U^{-4}$, so any raw exponent gain must be corrected by $4\theta$—the spectral analogue of the aperture false-$\kappa$ law. A polynomial-tail hierarchy $\omega_p=c_p(1+\tau^2)^{-p}$, $p>1/2$, gives positive RH-equivalent weighted energies; for integer $p$ these are Green energies of $(1-\partial^2)^{-p}$ and causal filters of order $p$. Since all fixed orders retain the same RH strength, the original Cauchy case $p=1$ is the minimal-order engineering choice. The next useful attack is therefore not further spectral slicing, but a sharp positive-kernel comparison between the canonical Cauchy energy and classical Selberg/PNT mean-square quantities.

---

# 31. References

1. Michel J. G. Weber, **Cauchy Means of Dirichlet Polynomials**, *Journal of Approximation Theory* 204 (2016), 61–79.  
   DOI: https://doi.org/10.1016/j.jat.2016.01.001  
   arXiv: https://arxiv.org/abs/1412.7812

2. Xuebo Zhai, Kai Wang, Heping Wang, **Inequalities on weighted Paley-Wiener space with respect to doubling weights and $A_\infty$ weights**, *Journal of Mathematical Analysis and Applications* 535 (2024), 128164.  
   DOI: https://doi.org/10.1016/j.jmaa.2024.128164

3. Classical Littlewood–Paley / Poisson-semigroup square-function theory; see standard harmonic-analysis references.

4. AMRAL, **RH-CauchyPoisson-TwistScalarization v2.5**.

5. AMRAL, **RH-BandlimitedTwist-AveragingGate v2.4**.

6. AMRAL, **RH-CompletedReward-CorrelationKernel v3.2**.

---

# 32. Provenance

研究主導：Neo.K

v3.3 fixed-positive-window sensitivity、exact zero-transfer identity、spectral moving-band correction、positive resolvent hierarchy、branch audit、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第四弧線 positive spectral kernel / sensitivity normalization 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
