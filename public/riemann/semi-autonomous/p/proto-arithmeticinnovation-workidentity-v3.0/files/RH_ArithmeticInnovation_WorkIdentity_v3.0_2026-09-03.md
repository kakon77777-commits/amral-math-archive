工程紀錄 · 第四弧線 v3.0 · 2026-09-03 · WORK_ENERGY_IDENTITY · LIFECYCLE_NEUTRALITY · EXTERNAL_WORK_GATE · RH_CLAIM_FALSE

# Arithmetic Innovation Work Identity、Lifecycle Neutrality 與 External-Work Gate

**RH-ArithmeticInnovation-WorkIdentity v3.0**

本節點承接：

- `RH-ArithmeticInnovation-EnergyGate v2.9`
- `RH-CauchyPoisson-TwistScalarization v2.5`
- `RH-CausalState-MovingWindowRecurrence v2.7`

v2.9 已把所有 arithmetic forcing 壓成單一 scalar innovation：

$$
d\mathfrak I(u)
=
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}du.
$$

v3.0 不再問：

```text
innovation 本身有多大？
```

而問：

```text
innovation 對 Cauchy causal state 做了多少 work？
```

本輪得到一個 exact Hilbert-space work–energy identity。

令 $K$ 為 exponential kernel：

$$
K(u,v)=e^{-|u-v|}.
$$

對任意 compact signed finite source $\eta$，定義 moving tent source：

$$
\boxed{
d\mu_t(u)
=
T_h(t-u)\,d\eta(u).
}
$$

令：

$$
\boxed{
\mathcal C(t)
=
\|\mu_t\|_K^2
=
\iint
K(u,v)\,d\mu_t(u)d\mu_t(v).
}
$$

以及 kinetic action density：

$$
\boxed{
\mathcal K(t)
=
\|\dot\mu_t\|_K^2
\ge0.
}
$$

則在 distribution sense：

$$
\boxed{
\frac12\mathcal C''(t)
=
\mathcal K(t)
+
\langle\mu_t,\ddot\mu_t\rangle_K.
}
$$

而完整 lifecycle 上：

$$
\boxed{
\int_{\mathbb R}
\langle\mu_t,\ddot\mu_t\rangle_Kdt
=
-
\int_{\mathbb R}
\mathcal K(t)dt.
}
$$

這個 net-work cancellation 對**任何** compact signed source成立。

因此：

> `ENTER/CENTER/EXIT net work = 0` 並不是 prime-specific theorem，也不是 RH progress。它是 tent + Hilbert geometry 的 universal identity。

真正的 arithmetic object是：

$$
\boxed{
\text{unfinished / external lifecycle work}
}
$$

而不是 complete lifecycle net work。

對單一 prime power $q$：

$$
x_q=\log q,
$$

$$
c_q=\Lambda(q)/\sqrt q,
$$

其 lifecycle acceleration work是：

$$
\boxed{
\mathcal W_q
=
c_q
\left[
F_{x_q-h}(x_q)
-
2F_{x_q}(x_q)
+
F_{x_q+h}(x_q)
\right],
}
$$

其中：

$$
F_t(x)
=
\int
e^{-|x-u|}
\,d\mu_t(u).
$$

self part精確是：

$$
\boxed{
\mathcal W_q^{\rm self}
=
-2hc_q^2,
}
$$

而該 prime 自己的 kinetic action是：

$$
\boxed{
\mathcal A_q^{\rm self}
=
2hc_q^2.
}
$$

兩者精確抵消。

剩餘：

$$
\boxed{
\mathcal W_q^{\rm ext}
=
\mathcal W_q
+
2hc_q^2
}
$$

才是真正和其他 primes / archimedean background 的 local arithmetic interaction。

更重要的是，lifecycle kernel可精確寫成：

$$
\boxed{
L_h(d)
=
T_h(d-h)-2T_h(d)+T_h(d+h)
=
-A_h(d),
}
$$

其中 $A_h$ 正是 v1.9 的 sign-window autocorrelation kernel。

所以 work route精確回到：

```text
SYMMETRY / SIGN-WINDOW CORRELATION
```

但現在知道該研究的是：

```text
PARTIAL / EXTERNAL WORK INVENTORY
```

而不是 universal net lifecycle cancellation。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

HILBERT_WORK_ENERGY_IDENTITY = CLOSED
FULL_LIFECYCLE_WORK_NEUTRALITY = CLOSED
LIFECYCLE_NEUTRALITY_IS_ARITHMETIC_PROGRESS = FALSE

KINETIC_ACTION_KERNEL = CLOSED
LIFECYCLE_WORK_KERNEL = CLOSED
L_h = -A_h = CLOSED

SINGLE_ATOM_SELF_ACTION = 2 h a^2
SINGLE_ATOM_SELF_WORK = -2 h a^2
SELF_CANCELLATION = CLOSED

PRIME_EXTERNAL_LIFECYCLE_WORK = DEFINED
EXTERNAL_WORK_FINITE_RANGE = 2h

FULL_NET_WORK_BOUND_AS_RH_ROUTE = NO_GO
PARTIAL_POSITIVE_EXTERNAL_WORK = OPEN_TARGET

GLOBAL_POLYNOMIAL_CAUCHY_ENERGY = OPEN_RH_COMPLETE
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Kernel Hilbert space

For a real compact signed measure $\alpha$, define:

$$
\boxed{
\|\alpha\|_K^2
=
\iint
e^{-|u-v|}
\,d\alpha(u)d\alpha(v).
}
$$

The exponential kernel is positive definite, so:

$$
\|\alpha\|_K^2\ge0.
$$

Equivalently:

$$
\boxed{
\|\alpha\|_K^2
=
\int_{\mathbb R}
\frac{
|\widehat\alpha(\tau)|^2
}{
\pi(1+\tau^2)
}
d\tau.
}
$$

This is the v2.5 Cauchy / resolvent Hilbert norm.

---

# 2. Moving tent trajectory

Let:

$$
T_h(x)
=
(h-|x|)_+.
$$

Fix any compact signed source:

$$
\eta.
$$

Define:

$$
\boxed{
d\mu_t(u)
=
T_h(t-u)d\eta(u).
}
$$

As a function of $t$, $\mu_t$ is continuous in the kernel Hilbert space and piecewise differentiable.

For almost every $t$:

$$
\boxed{
d\dot\mu_t(u)
=
T_h'(t-u)d\eta(u).
}
$$

The slope kernel is:

$$
T_h'(x)
=
\begin{cases}
+1,&-h<x<0,
\\
-1,&0<x<h,
\\
0,&|x|>h,
\end{cases}
$$

away from the three kink points.

---

# 3. Energy and kinetic action

Define:

$$
\boxed{
\mathcal C(t)
=
\|\mu_t\|_K^2.
}
$$

Define:

$$
\boxed{
\mathcal K(t)
=
\|\dot\mu_t\|_K^2.
}
$$

Then:

$$
\mathcal K(t)\ge0.
$$

The first derivative is:

$$
\boxed{
\mathcal C'(t)
=
2
\langle
\mu_t,\dot\mu_t
\rangle_K.
}
$$

---

# 4. Distributional work–energy identity

Differentiate once more in the distributional sense:

$$
\boxed{
\frac12
\mathcal C''(t)
=
\mathcal K(t)
+
\langle
\mu_t,\ddot\mu_t
\rangle_K.
}
$$

Interpretation:

```text
curvature of stored Cauchy energy
=
positive kinetic action
+
signed acceleration work.
```

The second term contains:

- smooth continuum acceleration;
- ENTER impulses;
- CENTER impulses;
- EXIT impulses.

---

# 5. Finite-interval integrated identity

For any interval $[a,b]$ whose endpoints are not acceleration impulses:

$$
\boxed{
\frac12
\left[
\mathcal C'(b)
-
\mathcal C'(a)
\right]
=
\int_a^b
\mathcal K(t)dt
+
\mathcal W[a,b],
}
$$

where:

$$
\boxed{
\mathcal W[a,b]
=
\int_{[a,b]}
\langle
\mu_t,d\dot\mu_t
\rangle_K.
}
$$

The last integral is a scalar Stieltjes / distributional work pairing including both continuous and impulsive acceleration.

---

# 6. Complete-lifecycle neutrality

Because $\eta$ is compactly supported, there exists a finite interval outside which:

$$
\mu_t=0.
$$

Hence:

$$
\mathcal C'(t)=0
$$

before the first lifecycle begins and after the last lifecycle ends.

Integrating Section 5 over the whole real line:

## Theorem 6.1 · Complete-lifecycle work neutrality

$$
\boxed{
\mathcal W_{\rm full}
=
-
\mathcal A_{\rm kin},
}
$$

where:

$$
\boxed{
\mathcal A_{\rm kin}
=
\int_{\mathbb R}
\mathcal K(t)dt
\ge0.
}
$$

Thus:

$$
\boxed{
\mathcal A_{\rm kin}
+
\mathcal W_{\rm full}
=
0.
}
$$

This theorem does **not** use primes.

It holds for every compact signed source.

---

# 7. Why lifecycle neutrality is not RH progress

A candidate argument of the form:

```text
each source enters
then centers
then exits
and the total work cancels
```

is insufficient.

The cancellation in Section 6 is forced by:

- the compact tent lifecycle;
- Hilbert-space calculus.

It contains no special information about:

- prime locations;
- von Mangoldt weights;
- prime correlations;
- zeta zeros.

So autonomous research should classify:

```text
NET LIFECYCLE WORK = 0
```

as:

```text
STRUCTURE_BLIND_IDENTITY
```

not as a theorem candidate.

---

# 8. Kinetic autocorrelation kernel

Define:

$$
\boxed{
A_h(d)
=
\int_{\mathbb R}
T_h'(t)
T_h'(t-d)dt.
}
$$

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

This is exactly the sign-window autocorrelation already appearing in v1.9.

---

# 9. Integrated kinetic action as symmetry energy

Fubini gives:

## Theorem 9.1

$$
\boxed{
\mathcal A_{\rm kin}
=
\iint
e^{-|u-v|}
A_h(u-v)
\,d\eta(u)d\eta(v).
}
$$

Although $A_h$ changes sign pointwise, the quadratic form is nonnegative because it is the time-integral of:

$$
\|\dot\mu_t\|_K^2.
$$

This is a Cauchy-tapered symmetry energy.

---

# 10. Lifecycle acceleration kernel

Define:

$$
\boxed{
L_h(d)
=
T_h(d-h)
-
2T_h(d)
+
T_h(d+h).
}
$$

A direct piecewise calculation gives:

$$
\boxed{
L_h(d)
=
\begin{cases}
3r-2h,
&
0\le r\le h,
\\
2h-r,
&
h\le r\le2h,
\\
0,
&
r\ge2h.
\end{cases}
}
$$

Therefore:

## Theorem 10.1

$$
\boxed{
L_h(d)
=
-A_h(d).
}
$$

This is also the integration-by-parts identity:

$$
\int
T_h(t-u)
T_h''(t-v)dt
=
-
\int
T_h'(t-u)
T_h'(t-v)dt.
$$

---

# 11. Work kernel representation

Using Section 10:

$$
\boxed{
\mathcal W_{\rm full}
=
\iint
e^{-|u-v|}
L_h(u-v)
\,d\eta(u)d\eta(v).
}
$$

Hence:

$$
\boxed{
\mathcal W_{\rm full}
=
-
\mathcal A_{\rm kin}.
}
$$

So the complete work–action balance is visible directly at the pair-kernel level.

---

# 12. Relation to symmetry-integral literature

$T_h'$ is the right-minus-left sign window.

Therefore:

$$
A_h=T_h'\ast\widetilde{T_h'}
$$

is the natural correlation kernel for a symmetry sum.

This connects the kinetic action in v3.0 to the symmetry-integral language studied by Coppola and related short-interval work.

The external literature provides method language and arithmetic estimates for symmetry sums.

But the universal identity:

$$
L_h=-A_h
$$

is geometric and must not be confused with a nontrivial prime symmetry bound.

---

# 13. Finite atomic source

Let:

$$
\eta
=
\sum_{j=1}^N
a_j\delta_{x_j}.
$$

Then:

$$
\mu_t
=
\sum_j
a_j
T_h(t-x_j)
\delta_{x_j}.
$$

Define:

$$
w_j(t)=a_jT_h(t-x_j).
$$

The energy is:

$$
\boxed{
\mathcal C(t)
=
w(t)^\top
K
w(t),
}
$$

where:

$$
K_{ij}
=
e^{-|x_i-x_j|}.
$$

Between events:

$$
d_j=w_j'
$$

is constant.

Therefore:

$$
\boxed{
\mathcal K(t)
=
d^\top Kd
}
$$

is constant between events.

---

# 14. Event work impulse

At an ENTER/CENTER/EXIT event of source $j$, the slope changes:

$$
d_j^+
=
d_j^-
+
\Delta d_j.
$$

The source weight $w$ is continuous.

Define the current field:

$$
\boxed{
F_t(x_j)
=
(Kw(t))_j.
}
$$

Then:

$$
\boxed{
\Delta\mathcal C'
=
2
\Delta d_j
F_t(x_j).
}
$$

The half-energy acceleration-work impulse is therefore:

$$
\boxed{
\Delta\mathcal W_j
=
\Delta d_j
F_t(x_j).
}
$$

For a tent source of amplitude $a_j$:

$$
\Delta d_j
=
\begin{cases}
+a_j,&ENTER,
\\
-2a_j,&CENTER,
\\
+a_j,&EXIT.
\end{cases}
$$

---

# 15. Single-source lifecycle work

For one source at:

$$
x,
$$

with amplitude:

$$
a,
$$

the three event times are:

$$
x-h,
\qquad
x,
\qquad
x+h.
$$

Therefore its full lifecycle acceleration work inside an arbitrary external field is:

$$
\boxed{
\mathcal W_x
=
a
\left[
F_{x-h}(x)
-
2F_x(x)
+
F_{x+h}(x)
\right].
}
$$

This formula remains valid when the field contains:

- the source itself;
- other atoms;
- a continuous background.

---

# 16. Exact self-work cancellation

For the source's own field:

### ENTER

$$
w=0.
$$

### CENTER

$$
w=ah.
$$

### EXIT

$$
w=0.
$$

So:

$$
\boxed{
\mathcal W_x^{\rm self}
=
a
[
0-2(ah)+0
]
=
-2ha^2.
}
$$

Its kinetic action is:

$$
\boxed{
\mathcal A_x^{\rm self}
=
\int_{x-h}^{x+h}
a^2dt
=
2ha^2.
}
$$

Therefore:

$$
\boxed{
\mathcal A_x^{\rm self}
+
\mathcal W_x^{\rm self}
=
0.
}
$$

This is the atomic form of lifecycle neutrality.

---

# 17. Prime-power self budget

For a prime power:

$$
q=p^k,
$$

$$
c_q
=
\frac{\Lambda(q)}{\sqrt q}.
$$

Hence:

$$
\boxed{
\mathcal A_q^{\rm self}
=
2h
\frac{
\Lambda(q)^2
}{
q
},
}
$$

and:

$$
\boxed{
\mathcal W_q^{\rm self}
=
-2h
\frac{
\Lambda(q)^2
}{
q
}.
}
$$

The large prime self budget is therefore exactly canceled at complete lifecycle level.

This is related to the v1.8 observation that raw prime self-energy is much larger than the final centered observable.

---

# 18. External lifecycle work

Define:

$$
\boxed{
\mathcal W_q^{\rm ext}
=
\mathcal W_q
-
\mathcal W_q^{\rm self}
=
\mathcal W_q
+
2hc_q^2.
}
$$

This is the work done by:

- other prime powers;
- the archimedean continuum background;

on the lifecycle of $q$.

This is no longer universal geometry.

It is an arithmetic correlation observable.

---

# 19. Fixed-range kernel for external work

Let the full source be:

$$
\eta.
$$

For a source point:

$$
x,
$$

Section 15 gives:

$$
\begin{aligned}
\mathcal W_x
&=
a
\int
e^{-|x-u|}
L_h(x-u)
\,d\eta(u).
\end{aligned}
$$

Hence:

$$
\boxed{
\mathcal W_x^{\rm ext}
=
a
\int_{u\ne x}
e^{-|x-u|}
L_h(x-u)
\,d\eta(u).
}
$$

Since:

$$
L_h(d)=0
$$

for:

$$
|d|\ge2h,
$$

external lifecycle work has exact finite log-range:

$$
\boxed{
2h.
}
$$

For:

$$
h=\log2,
$$

only sources with multiplicative ratio:

$$
\boxed{
\frac14
<
\frac{e^u}{e^x}
<
4
}
$$

can directly contribute.

---

# 20. Prime external-work formula

For the actual arithmetic innovation:

$$
d\eta(u)
=
d\mathfrak I(u),
$$

the prime-power external work is:

$$
\boxed{
\begin{aligned}
\mathcal W_q^{\rm ext}
&=
c_q
\sum_{r\ne q}
c_r
e^{-|x_q-x_r|}
L_h(x_q-x_r)
\\
&\quad
-
c_q
\int_{\mathbb R}
e^{-|x_q-u|}
L_h(x_q-u)
e^{u/2}du.
\end{aligned}
}
$$

Only:

$$
|x_q-u|<2h
$$

contributes.

So the work object is a centered, prime-sampled, finite-range symmetry correlation.

---

# 21. Why external work is a better arithmetic object than net work

Complete lifecycle net work is always determined by geometry.

External work removes the exactly known self term:

$$
-2hc_q^2.
$$

What remains depends on whether the surrounding prime/background configuration generates:

- reinforcing work;
- opposing work;
- cancellation.

Thus:

$$
\boxed{
\mathcal W_q^{\rm ext}
}
$$

contains actual local arithmetic information.

---

# 22. Pairwise lifecycle neutrality

For two fixed source locations $u,v$, their pair contribution to stored energy is:

$$
\boxed{
2a_ua_v
e^{-|u-v|}
T_h(t-u)T_h(t-v)
}
$$

for distinct points.

It is compactly supported in $t$.

Therefore its total second-derivative integral is zero.

Equivalently:

$$
\boxed{
\text{pair kinetic action}
+
\text{pair acceleration work}
=
0
}
$$

over the complete pair lifecycle.

This again holds independently of arithmetic.

---

# 23. Finite-memory interpretation

Every pair interaction exists only while the two tent lifecycles overlap.

For:

$$
|u-v|\ge2h,
$$

there is no overlap.

Therefore:

$$
\boxed{
\mathcal C_h(t)
}
$$

can be viewed as an inventory of **unfinished finite-lifetime pair interactions**.

Complete interactions leave no permanent work debt.

The global difficulty is that the number and magnitude of simultaneously unfinished interactions grow with $t$.

This is a more precise form of the earlier:

```text
finite temporal memory,
infinite event stream.
```

---

# 24. Why net-work estimates are another no-go

Suppose one proves only:

$$
\mathcal W_{\rm full}
=
-\mathcal A_{\rm kin}.
$$

This is already Theorem 6.1.

It yields no quantitative bound on instantaneous:

$$
\mathcal C_h(t).
$$

A source can have:

- huge positive stored energy during its lifecycle;
- exact zero net work after it finishes.

Therefore:

$$
\boxed{
\text{small / zero net lifecycle work}
\not\Longrightarrow
\text{small peak or block energy}.
}
$$

This is the work-theoretic analogue of earlier false-progress warnings.

---

# 25. What must be controlled instead

The next candidate quantities must measure **unfinished** or **one-sided** work.

Possible examples:

### A. Positive work variation

$$
\boxed{
\mathcal W_+([T,T+1])
}
$$

the positive variation of the acceleration-work measure.

### B. External prime lifecycle work

$$
\boxed{
\sum_{x_q\in[T,T+1]}
\left(
\mathcal W_q^{\rm ext}
\right)_+.
}
$$

### C. Incomplete lifecycle inventory

Sum only interactions whose tent lifecycles intersect the current block boundary.

### D. Kinetic-to-work deficit

Measure whether negative acceleration work tracks the positive kinetic action quickly enough on every finite horizon.

None of these is yet proved to give RH.

They are candidate work-level observables.

---

# 26. Relation to the v2.9 scalar innovation primitive

The source is:

$$
d\eta=d\mathfrak I=d\mathfrak b.
$$

Therefore all work kernels can also be integrated by parts against:

$$
\mathfrak b.
$$

But doing so pointwise risks returning to the stronger PNT-error route.

The purpose of v3.0 is to keep the signed work pairing and exploit lifecycle cancellation before taking absolute values.

This is precisely where the work route may be weaker than pointwise innovation control.

---

# 27. Symmetry-energy bridge

The kinetic action:

$$
\boxed{
\mathcal A_{\rm kin}
=
\iint
e^{-|u-v|}
A_h(u-v)
d\mathfrak I(u)d\mathfrak I(v)
}
$$

is a Cauchy-tapered symmetry quadratic form.

Coppola's prime symmetry integral and related Selberg/symmetry literature study mean-square cancellation of right-minus-left von Mangoldt sums.

So v3.0 gives an exact method bridge:

```text
ARITHMETIC INNOVATION WORK
    <->
CAUCHY-TAPERED SYMMETRY ENERGY.
```

Existing short-interval bounds still require the aperture / sensitivity audits from v2.2–v2.3 before they can be promoted to a zero-strip statement.

---

# 28. Numerical atomic validation

The v3.0 reference package uses finite signed atomic sources and checks independently:

1. direct chronological kinetic action:
   $$
   \int\mathcal K(t)dt;
   $$
2. sum of all ENTER/CENTER/EXIT work impulses;
3. pair-kernel action:
   $$
   \sum_{i,j}
   a_ia_j
   e^{-|x_i-x_j|}
   A_h(x_i-x_j);
   $$
4. lifecycle kernel:
   $$
   L_h=-A_h;
   $$
5. each source's self work:
   $$
   -2ha_i^2.
   $$

The checks are algebraic / normalization tests only.

---

# 29. Actual prime-power lifecycle sample

The package also evaluates a few real prime-power lifecycle works using:

$$
c_q=\Lambda(q)/\sqrt q
$$

and the exact continuous archimedean background.

For each sampled $q$, it records:

- total lifecycle work;
- exact self work;
- external work.

The signs vary across nearby prime configurations.

This is finite evidence that $\mathcal W_q^{\rm ext}$ is a nontrivial local arithmetic observable.

It is not a global theorem.

---

# 30. Candidate acceptance gate

A work-based candidate should only be promoted if it controls a quantity that is **not already universally neutral**.

Reject:

```text
FULL LIFECYCLE NET WORK = 0
```

Reject:

```text
PAIR LIFECYCLE NET WORK = 0
```

Promote for further analysis only if it supplies a rigorous bound on:

- positive work;
- external work;
- unfinished lifecycle inventory;
- finite-horizon work deficit;

and translates that bound into:

$$
\mathscr W_h(T)
$$

or an equivalent energy exponent.

---

# 31. New smallest GAP

The representation problem is now closed far enough that the next arithmetic question can be stated:

> Can the **positive / unfinished external work** of the prime innovation stream be bounded at a fixed exponent smaller than the structure-blind $\sigma=\frac12$ scale?

The target should permit complete lifecycle cancellation.

It must not take absolute values before the prime/background interaction has had a chance to cancel.

This is the work-specific tail barrier.

---

# 32. Suggested v3.1 direction

Recommended:

`RH-ExternalWork-InventoryBound v3.1`

Tasks:

1. derive a block identity for unfinished lifecycle work;
2. separate:
   - completed pairs;
   - left-boundary unfinished pairs;
   - right-boundary unfinished pairs;
3. express the boundary inventory using the v2.7 finite moments / causal state;
4. determine whether the completed interior work cancels exactly from the block budget;
5. identify the minimal positive boundary quantity that dominates:
   $$
   \mathcal C_h(t);
   $$
6. compare that boundary quantity with symmetry / Selberg mean squares;
7. search for a polynomial or fixed-exponent bound without reverting to pointwise $\mathfrak b$.

This is the next genuinely energy-specific route.

---

# 33. GAP ledger

## CLOSED / REDUCED

### G1. Hilbert work–energy identity

```text
CLOSED
```

### G2. Complete lifecycle neutrality

```text
CLOSED
```

### G3. Kinetic symmetry kernel

```text
CLOSED
```

### G4. Lifecycle kernel

```text
CLOSED
```

$$
L_h=-A_h.
$$

### G5. Self lifecycle cancellation

```text
CLOSED
```

### G6. Prime external lifecycle work

```text
DEFINED
```

---

## OPEN

### G7. Positive external-work bound

```text
OPEN
```

### G8. Unfinished lifecycle inventory bound

```text
OPEN
```

### G9. Any energy-aware fixed exponent $\sigma<1/2$

```text
OPEN
```

### G10. Polynomial Cauchy energy

```text
OPEN_RH_COMPLETE
```

### G11. RH

```text
OPEN
```

---

# 34. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

WORK_ENERGY_IDENTITY = UNIVERSAL
LIFECYCLE_NEUTRALITY = UNIVERSAL

UNIVERSAL WORK CANCELLATION != ARITHMETIC PROGRESS

EXTERNAL WORK = ARITHMETIC OBJECT
BUT NO GLOBAL BOUND HAS BEEN PROVED

FINITE LIFECYCLE NUMERICS = EVIDENCE ONLY

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\mathcal W_{\rm full}=-\mathcal A_{\rm kin}
\Longrightarrow
RH.
$$

Forbidden:

$$
\text{each lifecycle finishes}
\Longrightarrow
\text{simultaneous stored energy bounded}.
$$

Forbidden:

$$
\text{finite external-work cancellation}
\Longrightarrow
\text{global tail theorem}.
$$

---

# 35. One-line status

> v3.0 derives the exact work–energy law for the moving Cauchy source. For $\mu_t=T_h(t-\cdot)\eta$ in the exponential-kernel Hilbert space, $\frac12\mathcal C''=\|\dot\mu_t\|_K^2+\langle\mu_t,\ddot\mu_t\rangle_K$. Over a complete compact lifecycle, the signed acceleration work is exactly the negative of the positive kinetic action. This cancellation is universal and therefore cannot itself be RH progress. The integrated kinetic action is the Cauchy-tapered sign-window symmetry quadratic form with kernel $A_h$, while the lifecycle acceleration kernel is exactly $L_h=-A_h$. For a single prime power, the self kinetic action is $2h\Lambda(q)^2/q$ and the self lifecycle work is its exact negative. Removing that universal self term leaves the external lifecycle work, a finite-range centered prime/background correlation supported only within log-distance $2h$. The remaining work-specific RH problem is therefore not net lifecycle work—which always cancels—but the amount of positive or unfinished external work simultaneously stored in active lifecycles. The next node should derive a boundary-inventory identity and ask whether completed interior lifecycles can be eliminated from the block energy budget.

---

# 36. References

1. Giovanni Coppola, **On the symmetry of primes**, arXiv:1009.6121.  
   https://arxiv.org/abs/1009.6121

2. Giovanni Coppola, **On the Symmetry Integral**, arXiv:1007.1018.

3. Michel J. G. Weber, **Cauchy Means of Dirichlet Polynomials**, *Journal of Approximation Theory* 204 (2016), 61–79.  
   arXiv: https://arxiv.org/abs/1412.7812

4. G. B. Rybicki, W. H. Press, **A Class of Fast Methods for Processing Irregularly Sampled or Otherwise Inhomogeneous One-Dimensional Data**, *Physical Review Letters* 74 (1995), 1060–1063.

5. AMRAL, **RH-ArithmeticInnovation-EnergyGate v2.9**.

6. AMRAL, **RH-CauchyPoisson-TwistScalarization v2.5**.

---

# 37. Provenance

研究主導：Neo.K

v3.0 Hilbert work–energy identity、complete lifecycle neutrality audit、kinetic/sign-window kernel bridge、prime self/external lifecycle work、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第四弧線 arithmetic work / unfinished lifecycle energy 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
