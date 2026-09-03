工程紀錄 · 第三弧線 v2.5 · 2026-09-03 · CAUCHY_POISSON_SCALARIZATION · RESOLVENT_GREEN_ENERGY · RH_CLAIM_FALSE

# Cauchy–Poisson Twist Scalarization 與 Canonical Resolvent Green Energy

**RH-CauchyPoisson-TwistScalarization v2.5**

本節點承接：

- `RH-MellinSymmetry-PNTFilterBridge v1.9`
- `RH-TwistedLocalCorrelation-ExponentDrop v2.1`
- `RH-SensitivityNormalized-MultiscaleReconstruction v2.3`
- `RH-BandlimitedTwist-AveragingGate v2.4`

v2.4 把 twisted local energy 的 vertical dependence 組織成固定 bandwidth 的 unit twist bands。

v2.5 首先修正 v2.4 的 canonical target：

> 要求所有 twists 同時具有 uniform fixed power saving 太強；對每一個 finite arithmetic block，極大 twist 可用 simultaneous Diophantine approximation 讓有限 prime phases 幾乎重新對齊，而 twisted deterministic main term在 $|\tau|\to\infty$ 時衰減。故 $\sup_{\tau\in\mathbb R}$ 可以重新接近 raw prime scale，不能作為 RH 自然要求。

本節點改用固定 Cauchy probability weight：

$$
\boxed{
\omega(\tau)
=
\frac1{\pi(1+\tau^2)}.
}
$$

定義單一 weighted twist energy：

$$
\boxed{
\mathscr W_h(T)
=
\int_{\mathbb R}
\omega(\tau)
\mathcal Q_{h,\tau}(T)\,d\tau.
}
$$

由 Cauchy characteristic function：

$$
\boxed{
\int_{\mathbb R}
\omega(\tau)e^{-i\tau d}\,d\tau
=
e^{-|d|},
}
$$

twist continuum 精確消去，得到：

$$
\boxed{
\mathscr W_h(T)
=
\iint
K_{h,T}(u,v)
e^{-|u-v|}
\,d\nu(u)d\nu(v).
}
$$

更進一步，對每個 local center $t$ 定義：

$$
d\mu_t(u)
=
T_h(t-u)\,d\nu(u).
$$

令：

$$
G(u)
=
\frac12e^{-|u|}.
$$

則：

$$
(1-\partial_u^2)G=\delta_0.
$$

若：

$$
y_t=G\ast\mu_t,
$$

則：

$$
\boxed{
(1-\partial_u^2)y_t=\mu_t,
}
$$

且 Cauchy energy 精確為：

$$
\boxed{
\int_{\mathbb R}
\omega(\tau)
|\mathcal F_{h,\tau}(t)|^2d\tau
=
2
\int_{\mathbb R}
\left(
|y_t(u)|^2+|y_t'(u)|^2
\right)du.
}
$$

所以整個 twisted family 被壓成一個 canonical 1D Helmholtz / resolvent Green energy。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

V2_4_UNIFORM_ALL_TWISTS_TARGET = REJECTED_AS_OVERSTRONG
CAUCHY_WEIGHTED_TWIST_SCALAR = DEFINED

CAUCHY_PAIR_KERNEL_IDENTITY = CLOSED
RESOLVENT_GREEN_IDENTITY = CLOSED
CAUCHY_SCALAR_CONTROLS_FIXED_TWIST = CLOSED

RH_IMPLIES_BOUNDED_CAUCHY_SCALAR = CLOSED_FROM_ZERO_SIDE
POLYNOMIAL_CAUCHY_SCALAR_GROWTH_IMPLIES_RH = CLOSED_AS_REDUCTION

CAUCHY_SCALAR_RH_EQUIVALENCE = CLOSED_AS_REDUCTION
FINITE_LOCAL_RESOLVENT_SOURCE = TRUE

GENERIC_CAUCHY_DIRICHLET_MEAN = NOT_SUFFICIENT
GLOBAL_ARITHMETIC_CANCELLATION = OPEN

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Relative twisted local observable

Use the log-coordinate prime–archimedean discrepancy measure:

$$
d\nu(u)
=
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}\mathbf1_{u\ge0}\,du.
$$

For fixed aperture:

$$
h>0,
$$

let:

$$
T_h(v)
=
(h-|v|)_+.
$$

Define:

$$
\boxed{
\mathcal F_{h,\tau}(t)
=
\int_{\mathbb R}
T_h(t-u)
e^{-i\tau(u-t)}
\,d\nu(u).
}
$$

At:

$$
\tau=0,
$$

this is exactly the local prime discrepancy:

$$
\mathcal F_{h,0}(t)
=
\mathfrak E_h(e^t).
$$

Define the unit-log block energy:

$$
\boxed{
\mathcal Q_{h,\tau}(T)
=
\int_T^{T+1}
|\mathcal F_{h,\tau}(t)|^2dt.
}
$$

---

# 2. Scope correction to v2.4

For a fixed finite $T$ block, only finitely many prime powers occur in:

$$
e^{T-h}
<
q
<
e^{T+1+h}.
$$

Write their logarithms:

$$
\ell_1,\ldots,\ell_N.
$$

Simultaneous Diophantine approximation on the torus gives arbitrarily large $\tau$ for which:

$$
e^{-i\tau\ell_j}
$$

are simultaneously arbitrarily close to $1$ for all finite $j$.

The relative global phase:

$$
e^{i\tau t}
$$

does not affect absolute value.

Meanwhile the twisted deterministic main factor:

$$
A_h(\tau)
=
2
\frac{
\cosh((1/2-i\tau)h)-1
}{
(1/2-i\tau)^2
}
$$

satisfies:

$$
\boxed{
A_h(\tau)=O_h(\tau^{-2}).
}
$$

Therefore sufficiently large phase-alignment twists can suppress the continuous main term while making the finite prime phases almost coherent.

By the prime number theorem, the untapered local prime mass in a fixed multiplicative aperture is of order:

$$
e^{t/2}.
$$

Thus:

$$
\boxed{
\sup_{\tau}
\mathcal Q_{h,\tau}(T)
}
$$

can return to the raw:

$$
e^T
$$

energy scale.

So a theorem demanding:

$$
\sup_{\tau}
\mathcal Q_{h,\tau}(T)
\ll
e^{(1-\kappa)T}
$$

for fixed:

$$
\kappa>0
$$

is not the natural RH target.

This formally replaces the v2.4 canonical target.

---

# 3. Cauchy probability weight

Define:

$$
\boxed{
\omega(\tau)
=
\frac1{\pi(1+\tau^2)}.
}
$$

It is positive and normalized:

$$
\int_{\mathbb R}
\omega(\tau)d\tau
=
1.
$$

Its Fourier transform is:

$$
\boxed{
\int_{\mathbb R}
\omega(\tau)
e^{-i\tau d}d\tau
=
e^{-|d|}.
}
$$

This is the characteristic function of the standard Cauchy distribution.

Cauchy means of Dirichlet polynomials are a known research topic; Weber and earlier Wilf studied precisely integrals with the weight:

$$
\frac{d\tau}{\pi(1+\tau^2)}.
$$

v2.5 does not claim the Cauchy weighting technique itself is new.

---

# 4. Single weighted twist scalar

Define:

$$
\boxed{
\mathscr W_h(T)
=
\int_{\mathbb R}
\omega(\tau)
\mathcal Q_{h,\tau}(T)
\,d\tau.
}
$$

This is one nonnegative scalar for each $T$.

No vertical supremum remains.

No countable unit-band family remains.

The entire twist axis is compressed by one fixed probability measure.

---

# 5. Exact Cauchy pair kernel

From v2.4:

$$
\mathcal Q_{h,\tau}(T)
=
\iint
K_{h,T}(u,v)
e^{-i\tau(u-v)}
\,d\nu(u)d\nu(v),
$$

where:

$$
K_{h,T}(u,v)
=
\int_T^{T+1}
T_h(t-u)T_h(t-v)\,dt.
$$

Integrating against $\omega$ and using Fubini gives:

## Theorem 5.1 · Cauchy pair scalarization

$$
\boxed{
\mathscr W_h(T)
=
\iint
K_{h,T}(u,v)
e^{-|u-v|}
\,d\nu(u)d\nu(v).
}
$$

Since:

$$
K_{h,T}(u,v)=0
$$

when:

$$
|u-v|\ge2h,
$$

the resulting arithmetic covariance still has finite log-range:

$$
\boxed{
|u-v|<2h.
}
$$

The Cauchy weight adds a fixed positive taper:

$$
e^{-|u-v|}.
$$

---

# 6. Pointwise local source formulation

For each:

$$
t,
$$

define a local signed measure:

$$
\boxed{
d\mu_t(u)
=
T_h(t-u)\,d\nu(u).
}
$$

Then:

$$
\mathcal F_{h,\tau}(t)
=
e^{i\tau t}
\int
e^{-i\tau u}
\,d\mu_t(u).
$$

Thus:

$$
|\mathcal F_{h,\tau}(t)|
=
|\widehat{\mu_t}(\tau)|.
$$

The pointwise Cauchy energy is:

$$
\boxed{
\mathcal C_h(t)
=
\int_{\mathbb R}
\omega(\tau)
|\widehat{\mu_t}(\tau)|^2d\tau.
}
$$

And:

$$
\boxed{
\mathscr W_h(T)
=
\int_T^{T+1}
\mathcal C_h(t)\,dt.
}
$$

---

# 7. Pointwise pair identity

Using the Cauchy Fourier transform:

$$
\boxed{
\mathcal C_h(t)
=
\iint
e^{-|u-v|}
\,d\mu_t(u)d\mu_t(v).
}
$$

This is a positive quadratic form even though $\mu_t$ is signed.

The positivity follows from its Fourier representation.

---

# 8. Helmholtz / resolvent Green kernel

Define:

$$
\boxed{
G(x)
=
\frac12e^{-|x|}.
}
$$

In the distributional sense:

$$
\boxed{
(1-\partial_x^2)G
=
\delta_0.
}
$$

Define:

$$
\boxed{
y_t
=
G\ast\mu_t.
}
$$

Then:

$$
\boxed{
(1-\partial_x^2)y_t
=
\mu_t.
}
$$

Outside the source interval:

$$
[t-h,t+h],
$$

$y_t$ solves the homogeneous equation:

$$
-y_t''+y_t=0
$$

and decays exponentially at both infinities.

---

# 9. Exact resolvent energy identity

Since:

$$
e^{-|u-v|}
=
2G(u-v),
$$

we have:

$$
\mathcal C_h(t)
=
2
\int
y_t(u)
\,d\mu_t(u).
$$

Using:

$$
\mu_t
=
y_t-y_t'',
$$

and integration by parts:

$$
\boxed{
\mathcal C_h(t)
=
2
\int_{\mathbb R}
\left[
|y_t(u)|^2
+
|y_t'(u)|^2
\right]du.
}
$$

Therefore:

## Theorem 9.1 · Canonical resolvent Green form

$$
\boxed{
\mathscr W_h(T)
=
2
\int_T^{T+1}
\int_{\mathbb R}
\left[
|y_t|^2
+
|y_t'|^2
\right]
du\,dt.
}
$$

This is an exact positive Green energy.

---

# 10. Source structure is finite per local center

For fixed $t$:

$$
d\mu_t(u)
=
T_h(t-u)
\left[
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}
-
e^{u/2}du
\right].
$$

Only prime powers satisfying:

$$
e^{t-h}<q<e^{t+h}
$$

occur.

Thus the resolvent equation contains:

- finitely many delta sources;
- one explicit smooth forcing on a compact interval;
- homogeneous exponential tails.

Across a prime point:

$$
u=\log q,
$$

$y_t$ is continuous while its derivative has a finite jump determined by:

$$
\frac{\Lambda(q)}{\sqrt q}
T_h(t-\log q).
$$

So every fixed-$t$ resolvent problem is a finite point-source ODE plus explicit background.

---

# 11. Connection back to the early AMRAL Green program

Earlier AMRAL work studied abstract Green matrices, local interval Green certificates, and arithmetic PSD budgets.

v2.5 produces a different object:

$$
\boxed{
(1-\partial_u^2)y_t=\mu_t,
}
$$

whose Green kernel:

$$
\frac12e^{-|u-v|}
$$

is not a heuristic model.

It is forced exactly by the Cauchy twist weight.

Therefore this node creates an exact bridge back to Green-language engineering:

```text
TWISTED PRIME CORRELATION
    ->
CAUCHY MEAN
    ->
POISSON / RESOLVENT KERNEL
    ->
CANONICAL 1D GREEN ENERGY.
```

No identification with earlier abstract AMRAL Green matrices is assumed without a separate normalization audit.

---

# 12. Bandlimited reproduction controls every fixed twist

Let:

$$
q_T(\tau)
=
\mathcal Q_{h,\tau}(T).
$$

v2.4 proved:

$$
\operatorname{supp}
\widehat q_T
\subset[-2h,2h].
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
q_T=q_T\ast\phi.
}
$$

For any fixed:

$$
\tau_0,
$$

$$
q_T(\tau_0)
\le
\int
q_T(s)
|\phi(\tau_0-s)|ds.
$$

Write:

$$
\omega(s)
=
\frac1{\pi(1+s^2)}.
$$

Then:

$$
q_T(\tau_0)
\le
\mathscr W_h(T)
\sup_s
\left[
\pi(1+s^2)
|\phi(\tau_0-s)|
\right].
$$

Because $\phi$ is Schwartz, the supremum is finite.

Thus:

## Theorem 12.1 · Cauchy scalar dominates fixed twists

For every fixed:

$$
\tau_0\in\mathbb R,
$$

there exists:

$$
C_{h,\tau_0}<\infty
$$

independent of $T$, such that:

$$
\boxed{
\mathcal Q_{h,\tau_0}(T)
\le
C_{h,\tau_0}
\mathscr W_h(T).
}
$$

In particular:

$$
\boxed{
\mathcal Q_{h,0}(T)
\le
C_h
\mathscr W_h(T).
}
$$

---

# 13. Polynomial Cauchy-energy growth implies RH

Suppose for some finite:

$$
A
$$

we prove:

$$
\boxed{
\mathscr W_h(T)
=
O(T^A).
}
$$

Then Theorem 12.1 gives:

$$
\mathcal Q_{h,0}(T)
=
O(T^A).
$$

But:

$$
\mathcal Q_{h,0}(T)
=
\int_T^{T+1}
|\mathfrak E_h(e^t)|^2dt.
$$

Therefore the cumulative untwisted energy up to $Y$ is:

$$
O(Y^{A+1}).
$$

v1.7 proved that any finite polynomial cumulative energy growth implies RH.

Hence:

## Theorem 13.1 · Polynomial Cauchy scalar sufficiency

$$
\boxed{
\mathscr W_h(T)=O(T^A)
\text{ for any finite }A
\Longrightarrow
RH.
}
$$

---

# 14. RH implies bounded Cauchy scalar

Assume RH.

The zero-side fixed-aperture twisted observable has the form, up to the explicit exponentially decaying trivial-zero correction:

$$
\boxed{
\mathcal F_{h,\tau}(t)
=
-
\sum_{\gamma}
B_h(i(\gamma-\tau))
e^{i\gamma t}
+
\text{trivial correction},
}
$$

where:

$$
\boxed{
B_h(z)
=
2
\frac{
\cosh(hz)-1
}{
z^2
},
}
$$

and the removable value is:

$$
B_h(0)=h^2.
$$

For real $x$:

$$
\boxed{
|B_h(ix)|
\le
\min
\left(
h^2,
\frac4{x^2}
\right).
}
$$

---

# 15. Local zero count bound

The classical zero-counting formula gives:

$$
N(Y+1)-N(Y)
=
O(\log(2+Y)).
$$

Therefore:

$$
\sum_\gamma
\min
\left(
h^2,
\frac4{(\gamma-\tau)^2}
\right)
=
O_h
\left(
\log(2+|\tau|)
\right).
$$

Hence under RH:

$$
\boxed{
|\mathcal F_{h,\tau}(t)|
\ll_h
\log(2+|\tau|)
}
$$

uniformly in $t$.

Thus:

$$
\mathcal Q_{h,\tau}(T)
\ll_h
\log^2(2+|\tau|).
$$

Since:

$$
\int_{\mathbb R}
\frac{
\log^2(2+|\tau|)
}{
1+\tau^2
}
d\tau
<
\infty,
$$

we obtain:

## Theorem 15.1 · RH boundedness

$$
\boxed{
RH
\Longrightarrow
\mathscr W_h(T)
=
O_h(1).
}
$$

---

# 16. Cauchy scalar RH equivalence

Combine Theorems 13.1 and 15.1.

## Theorem 16.1 · Cauchy–Poisson scalar criterion

For any fixed:

$$
h>0,
$$

$$
\boxed{
RH
\Longleftrightarrow
\sup_{T\ge T_0}
\mathscr W_h(T)
<
\infty.
}
$$

More strongly:

$$
\boxed{
\mathscr W_h(T)=O(T^A)
\text{ for any finite }A
}
$$

is already sufficient for RH.

This is another RH-equivalent reduction, but its main value is vertical quantifier compression and exact Green scalarization.

Novelty priority of this exact criterion has not been established.

---

# 17. Why the Cauchy scalar is preferable to uniform twist supremum

### Uniform supremum

Can be driven toward raw finite-prime phase-alignment scale at enormous twists.

Too strong as a natural RH target.

### Cauchy scalar

Assigns every fixed twist neighbourhood positive weight but suppresses astronomically large phase-alignment twists by:

$$
\tau^{-2}.
$$

At the same time, bandlimited reproduction guarantees that no fixed finite twist can disappear from the scalar at exponent level.

Thus:

$$
\boxed{
\text{fixed resonance sensitivity}
+
\text{far-twist suppression}
}
$$

are achieved simultaneously.

---

# 18. Exact arithmetic kernel

The Cauchy scalar no longer contains a phase parameter.

Its arithmetic kernel is:

$$
\boxed{
\mathcal K_{h,T}^{\rm C}(u,v)
=
K_{h,T}(u,v)e^{-|u-v|}.
}
$$

Therefore the next arithmetic task is simply:

$$
\boxed{
\iint
\mathcal K_{h,T}^{\rm C}(u,v)
\,d\nu(u)d\nu(v)
}
$$

rather than a family indexed by $\tau$.

This is a centered finite-range covariance with a positive Ornstein–Uhlenbeck taper.

---

# 19. Cauchy / OU interpretation

The kernel:

$$
e^{-|u-v|}
$$

is the covariance kernel of a stationary Ornstein–Uhlenbeck process up to normalization.

It is also the resolvent kernel of:

$$
1-\partial_u^2.
$$

Hence v2.5 can be interpreted in three equivalent ways:

```text
CAUCHY MEAN OF MELLIN TWISTS

OU-TAPERED PRIME COVARIANCE

HELMHOLTZ H^{-1}-TYPE ENERGY.
```

This creates possible interfaces with:

- orthogonal Dirichlet polynomials;
- resolvent / Green methods;
- Gaussian / OU covariance algebra;
- finite point-source ODE certification.

---

# 20. Generic raw scale remains large

The Cauchy transform does not magically supply arithmetic cancellation.

For the prime-only part, all source points inside one aperture satisfy:

$$
|u-v|<2h.
$$

Hence:

$$
e^{-|u-v|}
\ge
e^{-2h}.
$$

So the positive prime–prime Cauchy energy is at least a fixed fraction of the square of the local positive prime mass.

That mass is:

$$
\asymp_h
e^{t/2}.
$$

Therefore the raw positive prime-only scale remains:

$$
\boxed{
e^T.
}
$$

The RH target:

$$
O(1)
$$

requires cancellation with the explicit continuous archimedean background.

So the theorem barrier has not disappeared.

It has been placed into one positive centered scalar.

---

# 21. Relation to existing Cauchy means of Dirichlet polynomials

Michel Weber studied Cauchy means:

$$
\int_{\mathbb R}
\left|
\sum_{n\le N}
a_n n^{-it}
\right|^{2q}
\frac{dt}{\pi(1+t^2)}.
$$

For $q=1$, expanding the square yields the kernel:

$$
\boxed{
e^{-|\log(m/n)|}
=
\frac{
\min(m,n)
}{
\max(m,n)
}.
}
$$

So the basic Cauchy kernel in v2.5 is classical.

The new AMRAL-specific difficulty is the centered source:

$$
\text{von Mangoldt prime measure}
-
\text{archimedean density},
$$

localized by $T_h$ and coupled to RH through Suzuki / Weil.

Existing Cauchy-mean results should therefore be treated as a method interface, not as an automatic RH bound.

---

# 22. Scaled Cauchy weights and another sensitivity warning

More generally define:

$$
\boxed{
\omega_a(\tau)
=
\frac1\pi
\frac{a}{
a^2+\tau^2
}.
}
$$

Then:

$$
\boxed{
\widehat\omega_a(d)
=
e^{-a|d|}.
}
$$

Increasing $a$ narrows the log-ratio pair interaction.

But for a fixed resonance ordinate:

$$
\tau_0,
$$

$$
\omega_a(\tau_0)
\sim
\frac1{\pi a}
$$

as:

$$
a\to\infty.
$$

So taking:

$$
a=X^\theta
$$

creates an apparent:

$$
X^{-\theta}
$$

averaging saving while simultaneously diluting every fixed resonance by the same exponent.

Thus the canonical v2.5 choice keeps:

$$
\boxed{
a=1
}
$$

fixed.

This is the twist-weight analogue of v2.2–v2.3 aperture sensitivity normalization.

---

# 23. Finite certificate architecture

For every fixed $T$ block, a rigorous Cauchy-resolvent certificate can contain:

```text
aperture h
t block [T,T+1]

prime-power list below exp(T+1+h)
prime-power hash

local source representation
continuous background formula

resolvent ODE convention
point-source jump conditions

Cauchy pair-energy interval
H1 resolvent-energy interval
pair-vs-resolvent residual interval

precision
rounding mode
implementation hash
source hash
```

Two independent evaluation channels are natural:

```text
PAIR KERNEL CHANNEL
vs.
RESOLVENT ODE CHANNEL.
```

---

# 24. Formalization target

The finite analytic core is suitable for Lean / Coq.

Priority lemmas:

### F1

$$
\int
\frac{
e^{-i\tau d}
}{
\pi(1+\tau^2)
}
d\tau
=
e^{-|d|}.
$$

### F2

$$
(1-\partial^2)
\left(
\frac12e^{-|x|}
\right)
=
\delta_0.
$$

### F3

For compact signed finite measure $\mu$:

$$
\boxed{
\int
\frac{
|\widehat\mu(\tau)|^2
}{
\pi(1+\tau^2)
}
d\tau
=
2
\int
\left(
|y|^2+|y'|^2
\right)
}
$$

with:

$$
(1-\partial^2)y=\mu.
$$

### F4

Bandlimited weighted domination:

$$
q(\tau_0)
\le
C_{\tau_0}
\int
\omega q.
$$

These do not require formalizing all of zeta theory first.

---

# 25. New smallest GAP

After v2.5 the vertical problem is no longer a twist-family theorem.

Fix:

$$
h=\log2.
$$

Prove any finite polynomial bound:

$$
\boxed{
\mathscr W_h(T)
=
O(T^A)
}
$$

for some:

$$
A<\infty.
$$

Equivalently prove polynomial control of:

$$
\boxed{
2
\int_T^{T+1}
\|y_t\|_{H^1(\mathbb R)}^2dt
}
$$

for the exact point-source / smooth-background Helmholtz problem:

$$
(1-\partial_u^2)y_t
=
T_h(t-u)
\left[
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}
-
e^{u/2}du
\right].
$$

By Theorem 13.1 this closes RH.

This is still RH-complete.

But it is now one scalar positive Green-energy problem with no vertical parameter.

---

# 26. Suggested v2.6 direction

Recommended:

`RH-CauchyResolvent-CenteredCancellation-v2.6`

Tasks:

1. solve the local resolvent exactly between consecutive prime log-points;
2. express the energy through point-source jump data;
3. analytically subtract the smooth density solution;
4. derive a recurrence as prime points enter / leave the tent aperture;
5. test whether the centered resolvent state has a conservation / dissipation law;
6. compare the discrete kernel matrix:
   $$
   e^{-|\log(q/r)|}
   $$
   with known Cauchy-Dirichlet polynomial operator theory;
7. seek a polynomial energy bound without expanding all raw prime pairs.

This reconnects the new exact object to the original AMRAL Green-engineering strengths.

---

# 27. GAP ledger

## CLOSED / CORRECTED

### G1. v2.4 uniform all-twist target

```text
REJECTED_AS_OVERSTRONG
```

### G2. Cauchy twist scalarization

```text
CLOSED
```

### G3. Pair kernel

```text
CLOSED
```

$$
e^{-|u-v|}.
$$

### G4. Resolvent Green identity

```text
CLOSED
```

### G5. Fixed-twist domination

```text
CLOSED
```

### G6. RH bounded Cauchy energy

```text
CLOSED_AS_REDUCTION
```

### G7. Polynomial Cauchy energy sufficiency

```text
CLOSED_AS_REDUCTION
```

---

## OPEN

### G8. Unconditional polynomial Cauchy scalar bound

```text
OPEN_RH_COMPLETE
```

### G9. Centered resolvent invariant

```text
OPEN
```

### G10. Prime point-source recurrence

```text
OPEN
```

### G11. Finite global proof object

```text
OPEN
```

### G12. RH

```text
OPEN
```

---

# 28. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

CAUCHY_SCALARIZATION = EXACT
RESOLVENT_GREEN_IDENTITY = EXACT

CAUCHY_WEIGHT_TECHNIQUE = KNOWN_IN_DIRICHLET_POLYNOMIAL LITERATURE
EXACT_AMRAL_RH_REDUCTION_NOVELTY = NOT ESTABLISHED

POLYNOMIAL CAUCHY ENERGY BOUND = NOT PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{Cauchy mean is finite for each }T
\Longrightarrow
RH.
$$

Forbidden:

$$
\text{Green ODE is one-dimensional}
\Longrightarrow
\text{global theorem is easy}.
$$

Forbidden:

$$
\text{existing Cauchy mean theorem}
\Longrightarrow
\text{centered von Mangoldt cancellation is solved}.
$$

---

# 29. One-line status

> v2.5 corrects the overstrong v2.4 all-twist target and replaces the entire vertical twist family with one fixed Cauchy-weighted scalar. The standard Cauchy weight $\omega(\tau)=1/[\pi(1+\tau^2)]$ has Fourier transform $e^{-|u-v|}$, so the twisted local covariance becomes one finite-range exponentially tapered prime–archimedean quadratic form. Bandlimited reproduction shows that this single scalar controls every fixed twist with a $T$-independent constant, while under RH the zero-side coefficients imply only logarithmic growth in the twist variable and hence bounded Cauchy energy. Consequently RH is equivalent to bounded Cauchy scalar energy, and any finite polynomial growth of that scalar already suffices for RH. The Cauchy kernel is also the Green kernel of $1-\partial_u^2$: if $(1-\partial_u^2)y_t=\mu_t$ for the localized prime–archimedean source, then the Cauchy mean equals $2\int(|y_t|^2+|y_t'|^2)du$. This returns the research line to a canonical one-dimensional Green/resolvent energy, now derived exactly rather than postulated. The remaining problem is a centered point-source cancellation invariant strong enough to keep this resolvent energy polynomial in the log scale.

---

# 30. References

1. Michel J. G. Weber, **Cauchy Means of Dirichlet Polynomials**, *Journal of Approximation Theory* 204 (2016), 61–79.  
   DOI: https://doi.org/10.1016/j.jat.2016.01.001  
   arXiv: https://arxiv.org/abs/1412.7812

2. Giovanni Coppola, Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, arXiv:1411.1739.

3. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.

4. AMRAL, **RH-BandlimitedTwist-AveragingGate v2.4**.

5. AMRAL, **RH-SensitivityNormalized-MultiscaleReconstruction v2.3**.

6. AMRAL, **RH-MellinSymmetry-PNTFilterBridge v1.9**.

---

# 31. Provenance

研究主導：Neo.K

v2.5 Cauchy twist scalarization、v2.4 scope correction、Poisson / OU pair kernel、resolvent Green identity、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 Cauchy scalar / exact Green resolvent 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
