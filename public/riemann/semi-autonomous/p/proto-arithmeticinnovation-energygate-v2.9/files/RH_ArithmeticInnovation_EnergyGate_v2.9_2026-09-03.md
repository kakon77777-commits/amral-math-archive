工程紀錄 · 第三弧線 v2.9 · 2026-09-03 · ARITHMETIC_INNOVATION · ENERGY_GATE · RH_CLAIM_FALSE

# Arithmetic Innovation：單一 Prime-Flux 驅動、$H^{-1}$ Energy Gate 與 $\sigma=\frac12$ Baseline

**RH-ArithmeticInnovation-EnergyGate v2.9**

本節點承接：

- `RH-MellinSymmetry-PNTFilterBridge v1.9`
- `RH-CauchyPoisson-TwistScalarization v2.5`
- `RH-CausalState-MovingWindowRecurrence v2.7`
- `RH-CriticalCenteredState-LyapunovGate v2.8`

v2.8 已指出，raw 18-state 不適合直接做 coercive Lyapunov；正確 state 必須先 subtract PNT backbone，並保留 energy / pair information。

v2.9 把剩餘 arithmetic forcing 壓成一條 scalar innovation measure：

$$
\boxed{
d\mathfrak I(u)
=
\sum_{q=p^k}
\frac{\Lambda(q)}{\sqrt q}
\delta_{\log q}(du)
-
e^{u/2}du.
}
$$

其 cumulative innovation 是：

$$
\boxed{
\mathfrak b(t)
=
\sum_{n\le e^t}
\frac{\Lambda(n)}{\sqrt n}
-
2e^{t/2}.
}
$$

因此：

$$
\boxed{
d\mathfrak b=d\mathfrak I.
}
$$

本輪核心結論：

1. v2.8 的全部 14 個 critical-centered moments都是同一條 $\mathfrak I$ 的 shifted compact linear filters；
2. ENTER / CENTER / EXIT 三條 event streams只是同一 innovation measure的平移；
3. local Cauchy energy有直接 innovation-primitive bound：
   $$
   \boxed{
   \mathcal C_h(t)
   \le
   4(h^2+1)
   \int_{t-h}^{t+h}
   |\mathfrak b(u)|^2du;
   }
   $$
4. block Cauchy scalar因此滿足：
   $$
   \boxed{
   \mathscr W_h(T)
   \le
   4(h^2+1)
   \int_{T-h}^{T+1+h}
   |\mathfrak b(u)|^2du;
   }
   $$
5. 若 innovation primitive在 local mean-square 上達到：
   $$
   e^{2\sigma T}\operatorname{poly}(T),
   $$
   則 AMRAL energy也達到同一 $\sigma$；
6. 目前 2026 audited PNT / zero-free technology仍只給 fixed exponent：
   $$
   \boxed{
   \sigma=\frac12;
   }
   $$
7. 因此 hybrid algebra已經不是主要 barrier；要得到 $\sigma<1/2$，必須證明 arithmetic innovation的真正 cancellation；
8. pointwise bound on $\mathfrak b$ 是一條足夠但偏強的 classical-PNT route；更有希望的 AMRAL route是只證 energy / mean-square innovation work，而允許 pointwise spikes。

本節點不證 RH。

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

SCALAR_INNOVATION_MEASURE = CLOSED
SHIFTED_ENTER_CENTER_EXIT_INNOVATIONS = CLOSED
CENTERED_MOMENT_IMPULSIVE_SYSTEM = CLOSED

INNOVATION_PRIMITIVE_IDENTITY = CLOSED
MOMENT_INTEGRATION_BY_PARTS = CLOSED
INNOVATION_TO_CAUCHY_H_MINUS_1_BOUND = CLOSED
BLOCK_INNOVATION_ENERGY_BOUND = CLOSED

SIGMA_HALF_BASELINE = CLOSED_AT_STRENGTH_LEVEL
CURRENT_2026_FIXED_EXPONENT = 1/2

POINTWISE_INNOVATION_ROUTE = CLASSICAL_PNT_STRENGTH
ENERGY_AWARE_INNOVATION_ROUTE = STRICTLY_WEAKER_TARGET_IN_PRINCIPLE

ANY_RIGOROUS_SIGMA_LT_1_OVER_2 = OPEN
SIGMA_ZERO = OPEN_RH_COMPLETE

GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Weighted prime log measure

For each prime power:

$$
q=p^k,
$$

define:

$$
x_q=\log q,
$$

$$
c_q
=
\frac{\Lambda(q)}{\sqrt q}.
$$

Define the positive weighted prime log measure:

$$
\boxed{
d\Pi(u)
=
\sum_{q=p^k}
c_q
\delta_{x_q}(du).
}
$$

The smooth continuum main density is:

$$
\boxed{
e^{u/2}du.
}
$$

So the centered arithmetic innovation is:

$$
\boxed{
d\mathfrak I(u)
=
d\Pi(u)-e^{u/2}du.
}
$$

This is exactly the prime-event flux minus its PNT continuum flux.

---

# 2. Cumulative innovation primitive

Define:

$$
\boxed{
\mathfrak b(t)
=
\Pi((-\infty,t])
-
2e^{t/2}.
}
$$

Equivalently:

$$
\boxed{
\mathfrak b(t)
=
\sum_{n\le e^t}
\frac{\Lambda(n)}{\sqrt n}
-
2e^{t/2}.
}
$$

Since:

$$
d(2e^{t/2})
=
e^{t/2}dt,
$$

we obtain in the distributional / Stieltjes sense:

$$
\boxed{
d\mathfrak b=d\mathfrak I.
}
$$

Thus every local centered arithmetic observable in this line is driven by one scalar cumulative error process.

---

# 3. Shifted innovation streams

Define three time-axis innovation measures.

### CENTER innovation

$$
\boxed{
d\mathfrak I_0(t)
=
\sum_q
c_q\delta_{x_q}(dt)
-
e^{t/2}dt.
}
$$

### ENTER innovation

The ENTER event occurs at:

$$
t=x_q-h.
$$

Define:

$$
\boxed{
d\mathfrak I_+(t)
=
\sum_q
c_q
\delta_{x_q-h}(dt)
-
e^{(t+h)/2}dt.
}
$$

### EXIT innovation

The EXIT event occurs at:

$$
t=x_q+h.
$$

Define:

$$
\boxed{
d\mathfrak I_-(t)
=
\sum_q
c_q
\delta_{x_q+h}(dt)
-
e^{(t-h)/2}dt.
}
$$

These are translations of the same underlying arithmetic innovation.

There are not three independent random inputs.

---

# 4. Critical-centered moment bank

For:

$$
S\in\{L,R\},
$$

define fixed relative domains:

$$
D_L=(-h,0),
$$

$$
D_R=(0,h).
$$

Let:

$$
\phi_{\lambda,j}(d)
=
e^{\lambda d}d^j.
$$

The critical-centered moments are:

$$
\boxed{
R^S_{\lambda,j}(t)
=
\int_{D_S}
\phi_{\lambda,j}(d)
\,d\mathfrak I(t+d).
}
$$

This is exactly equivalent to the v2.8 definition:

$$
\text{prime relative moment}
-
\text{PNT continuum backbone}.
$$

---

# 5. Exact right-side impulsive system

Use the convention:

$$
R^R_{\lambda,-1}=0.
$$

For the right side:

$$
D_R=(0,h),
$$

the exact distributional dynamics is:

$$
\boxed{
\begin{aligned}
dR^R_{\lambda,j}
&=
\left(
-\lambda R^R_{\lambda,j}
-
jR^R_{\lambda,j-1}
\right)dt
\\
&\quad
+
e^{\lambda h}h^j
\,d\mathfrak I_+(t)
-
\mathbf1_{j=0}
\,d\mathfrak I_0(t).
\end{aligned}
}
$$

The two impulses are exactly:

```text
ENTER at d=h
CENTER at d=0
```

after continuum centering.

---

# 6. Exact left-side impulsive system

Use:

$$
R^L_{\lambda,-1}=0.
$$

For:

$$
D_L=(-h,0),
$$

the exact dynamics is:

$$
\boxed{
\begin{aligned}
dR^L_{\lambda,j}
&=
\left(
-\lambda R^L_{\lambda,j}
-
jR^L_{\lambda,j-1}
\right)dt
\\
&\quad
+
\mathbf1_{j=0}
\,d\mathfrak I_0(t)
\\
&\quad
-
e^{-\lambda h}
(-h)^j
\,d\mathfrak I_-(t).
\end{aligned}
}
$$

The impulses are:

```text
CENTER at d=0
EXIT at d=-h
```

after continuum centering.

---

# 7. Why this closes the v2.8 arithmetic forcing

The 14-state centered moment process is therefore:

$$
\boxed{
\text{fixed linear flow}
+
\text{three translated copies of one scalar innovation}.
}
$$

Every deterministic PNT backbone term has disappeared from the state equations.

The remaining input is purely:

$$
\boxed{
\text{prime flux}
-
\text{continuum flux}.
}
$$

So the hybrid-system algebra is now exact and closed.

The unresolved mathematics is the strength of the innovation itself.

---

# 8. Integration-by-parts representation of every centered moment

Since:

$$
d\mathfrak b=d\mathfrak I,
$$

for a side interval:

$$
D_S=(a_S,b_S),
$$

we have:

$$
R^S_{\lambda,j}(t)
=
\int_{a_S}^{b_S}
\phi_{\lambda,j}(d)
\,d\mathfrak b(t+d).
$$

At generic $t$ not coinciding with a boundary event, Stieltjes integration by parts gives:

$$
\boxed{
\begin{aligned}
R^S_{\lambda,j}(t)
&=
\left[
\phi_{\lambda,j}(d)
\mathfrak b(t+d)
\right]_{a_S}^{b_S}
\\
&\quad
-
\int_{a_S}^{b_S}
\phi_{\lambda,j}'(d)
\mathfrak b(t+d)\,dd.
\end{aligned}
}
$$

Thus every centered moment is a compact local linear functional of one scalar primitive:

$$
\mathfrak b.
$$

---

# 9. Moment norm consequence

Because:

$$
|d|\le h
$$

and the basis functions are fixed:

$$
\boxed{
|R^S_{\lambda,j}(t)|
\le
C_{h,\lambda,j}
\left[
|\mathfrak b(t-h)|
+
|\mathfrak b(t)|
+
|\mathfrak b(t+h)|
+
\int_{t-h}^{t+h}
|\mathfrak b(u)|du
\right].
}
$$

Hence any local growth theorem for:

$$
\mathfrak b
$$

immediately controls all 14 critical-centered moments.

---

# 10. Local Cauchy source

The v2.5 local source is:

$$
\boxed{
d\mu_t(u)
=
T_h(t-u)
\,d\mathfrak I(u)
=
T_h(t-u)
\,d\mathfrak b(u).
}
$$

The pointwise Cauchy energy is:

$$
\boxed{
\mathcal C_h(t)
=
\iint
e^{-|u-v|}
\,d\mu_t(u)d\mu_t(v).
}
$$

Equivalently:

$$
\boxed{
\mathcal C_h(t)
=
\int_{\mathbb R}
\frac{
|\widehat{\mu_t}(\tau)|^2
}{
\pi(1+\tau^2)
}
d\tau.
}
$$

---

# 11. Product-rule factorization through the innovation primitive

Define:

$$
g_t(u)
=
T_h(t-u)\mathfrak b(u).
$$

Since:

$$
\frac d{du}
T_h(t-u)
=
-
T_h'(t-u),
$$

the Stieltjes product rule gives:

$$
\boxed{
d\mu_t
\equiv
T_h(t-u)d\mathfrak b(u)
=
dg_t(u)
+
T_h'(t-u)
\mathfrak b(u)du.
}
$$

Here $T_h'$ is interpreted almost everywhere; its kinks are harmless in the distributional identity because $T_h$ is continuous.

---

# 12. Innovation-to-$H^{-1}$ energy inequality

Fourier transform Section 11.

Using:

$$
\widehat{dg_t}
=
i\tau\widehat g_t,
$$

and:

$$
|a+b|^2
\le
2|a|^2+2|b|^2,
$$

we obtain:

$$
\begin{aligned}
\mathcal C_h(t)
&\le
4
\int_{\mathbb R}
|g_t(u)|^2du
\\
&\quad
+
4
\int_{\mathbb R}
|T_h'(t-u)|^2
|\mathfrak b(u)|^2du.
\end{aligned}
$$

Since:

$$
|T_h|\le h,
$$

and:

$$
|T_h'|=1
$$

almost everywhere on the interior support:

## Theorem 12.1 · Innovation-to-Cauchy bound

$$
\boxed{
\mathcal C_h(t)
\le
4(h^2+1)
\int_{t-h}^{t+h}
|\mathfrak b(u)|^2du.
}
$$

This is a direct $L^2\to H^{-1}$ bound.

---

# 13. Block energy transfer

v2.5 defines:

$$
\boxed{
\mathscr W_h(T)
=
\int_T^{T+1}
\mathcal C_h(t)dt.
}
$$

Integrate Theorem 12.1 and use Fubini.

Every $u$ belongs to at most a fixed amount of the moving support.

Therefore:

## Theorem 13.1 · Block innovation-energy bound

$$
\boxed{
\mathscr W_h(T)
\le
4(h^2+1)
\int_{T-h}^{T+1+h}
|\mathfrak b(u)|^2du.
}
$$

The constant can be slightly sharpened by retaining the exact overlap function, but no exponent improvement is gained.

---

# 14. Innovation mean-square strength transfer

Suppose for some:

$$
\sigma\ge0
$$

and finite:

$$
A,
$$

we prove:

$$
\boxed{
\int_{T-h}^{T+1+h}
|\mathfrak b(u)|^2du
\ll
e^{2\sigma T}
T^A.
}
$$

Then:

$$
\boxed{
\mathscr W_h(T)
\ll
e^{2\sigma T}
T^A.
}
$$

The AMRAL energy-exponent bridge therefore gives:

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le
\sigma.
}
$$

Thus:

```text
sigma = 1/2
    critical-strip class

0 < sigma < 1/2
    fixed zero-strip breakthrough

sigma = 0
    RH scale
```

---

# 15. Exact relation to the classical PNT error

Define:

$$
E(x)
=
\psi(x)-x.
$$

Let:

$$
e(t)
=
e^{-t/2}E(e^t).
$$

Partial summation gives:

$$
\boxed{
\mathfrak b(t)
=
-1
+
e(t)
+
\frac12
\int_0^t
e(v)dv.
}
$$

Therefore pointwise control of the classical normalized PNT error controls the innovation primitive.

This is the exact bridge back to classical PNT technology.

---

# 16. Pointwise strip transfer

Suppose:

$$
\boxed{
E(x)
\ll
x^{1/2+\sigma}
(\log x)^A.
}
$$

Then:

$$
e(t)
\ll
e^{\sigma t}t^A.
$$

Section 15 gives:

$$
\mathfrak b(t)
\ll
e^{\sigma t}
t^{A+1}
$$

for:

$$
\sigma=0,
$$

and the same exponential class for:

$$
\sigma>0.
$$

Hence Theorem 13.1 gives:

$$
\mathscr W_h(T)
\ll
e^{2\sigma T}
\operatorname{poly}(T).
$$

So:

$$
\boxed{
E(x)
\ll
x^{1/2+\sigma}
\operatorname{polylog}x
\Longrightarrow
\left|
\Re\rho-\frac12
\right|
\le\sigma.
}
$$

This is a strong / pointwise route.

---

# 17. Why the pointwise innovation route is not the main new opportunity

A pointwise theorem:

$$
\mathfrak b(t)
=
O(e^{\sigma t}\operatorname{poly}(t))
$$

for:

$$
\sigma<\frac12
$$

already represents fixed-strip-strength PNT progress.

It is not easier merely because we renamed it "innovation."

The v2.9 value is instead that Theorem 13.1 only needs a **local mean-square** bound on $\mathfrak b$.

So the energy-aware route may allow:

- large sparse spikes;
- oscillatory sign changes;
- cancellation in local time;
- causal / resolvent dissipation;

without requiring pointwise PNT control.

This is the strictly more promising Lyapunov direction.

---

# 18. Current 2026 PNT / zero-free baseline

Current audited zero-free technology remains of shrinking-strip type.

Bellotti's zero-density theorem, published in 2026 after the 2025 preprint, obtains the PNT error at the optimal strength associated with a Korobov–Vinogradov-type zero-free region.

At exponential-class level:

$$
\boxed{
E(e^t)
=
\exp[t-o(t)].
}
$$

Therefore:

$$
e(t)
=
\exp\left[
\frac t2-o(t)
\right],
$$

and:

$$
\boxed{
\mathfrak b(t)
=
\exp\left[
\frac t2-o(t)
\right]
}
$$

at the same fixed-exponent scale.

Thus:

$$
\boxed{
\sigma_{\rm current}
=
\frac12.
}
$$

The subexponential improvement is important but does not yield any fixed:

$$
\sigma<\frac12.
$$

---

# 19. 2026 zero-free-region updates do not change the fixed exponent

Bellotti–Trudgian–Yang 2026 improve an explicit classical zero-free region to a form:

$$
\zeta(\sigma+it)\neq0
$$

for:

$$
\sigma
\ge
1-\frac1{4.896\log t}
$$

in the stated range.

Broucke 2026 gives a broad refined connection between zero-free contours and PNT error terms.

These are genuine current advances.

But their zero-free boundary still approaches:

$$
\Re s=1
$$

as height grows.

Therefore they do not imply any fixed:

$$
\Re\rho
\le
\frac12+\sigma,
\qquad
\sigma<\frac12.
$$

Hence the v2.9 Lyapunov strength class remains:

$$
\boxed{
\sigma=\frac12.
}
$$

---

# 20. Classical mean-square warning and opportunity

Brent–Platt–Trudgian study:

$$
I(X)
=
\int_X^{2X}
|\psi(x)-x|^2dx.
$$

Under RH:

$$
I(X)\ll X^2.
$$

If RH is false:

$$
I(X)/X^2
$$

is unbounded.

Thus mean-square PNT error is already an RH-complete diagnostic.

This supports the AMRAL energy route:

> average control can be enough even when pointwise control is unnecessarily strong.

But it also gives the strength warning:

> an unconditional local mean-square innovation theorem with fixed $\sigma<1/2$ would itself be a new zero-strip theorem.

---

# 21. Almost-all short intervals do not automatically cross the gate

Zaccagnini's classical Selberg-integral work obtains:

$$
J(X,H)=o(XH^2)
$$

in a broad unconditional range.

Modern almost-all short-interval results are much stronger in many regimes.

However at fixed-power exponent level:

$$
o(1)
$$

or logarithmic/subpower saving still corresponds to:

$$
\boxed{
\sigma=\frac12
}
$$

unless one obtains a true fixed power saving after the sensitivity-normalization audits of v2.2–v2.3.

So no audited short-interval theorem currently closes:

$$
\sigma<\frac12.
$$

---

# 22. Structure-blind innovation no-go

Suppose we know only:

$$
|\mathfrak b(t)|
\le
Ce^{t/2}.
$$

Then Theorem 12.1 gives:

$$
\mathcal C_h(t)
\ll
e^t.
$$

This is exactly:

$$
\sigma=\frac12.
$$

No hybrid-system manipulation of this norm bound can change its fixed exponent.

Therefore:

$$
\boxed{
\text{structure-blind innovation norm}
\Longrightarrow
\sigma=\frac12
\text{ at best}.
}
$$

To improve $\sigma$, one must use:

- arithmetic sign / phase structure;
- correlation;
- local mean-square cancellation;
- event work cancellation;
- or an equivalent number-theoretic theorem.

---

# 23. Energy-aware innovation candidate

A useful candidate family is:

$$
\boxed{
\mathcal V_{\sigma,P}(t)
=
e^{-2\sigma t}
\left[
\mathcal C_h(t)
+
R(t)^\top PR(t)
\right],
}
$$

but v2.9 adds a critical rule:

> its flow / event proof must use the centered innovation, not merely an upper bound on innovation magnitude.

A candidate whose proof reduces to:

$$
|\mathfrak b(t)|
\le
e^{t/2-o(t)}
$$

cannot certify:

$$
\sigma<\frac12.
$$

---

# 24. Strong route versus weak route

## Route A · Pointwise innovation

Prove:

$$
|\mathfrak b(t)|
\ll
e^{\sigma t}\operatorname{poly}(t).
$$

Pros:

- immediately controls all moments;
- immediately controls Cauchy energy.

Cons:

- essentially classical PNT-strength;
- likely too strong.

## Route B · Energy-aware innovation

Prove only:

$$
\boxed{
\int_{T-h}^{T+1+h}
|\mathfrak b(u)|^2du
\ll
e^{2\sigma T}\operatorname{poly}(T),
}
$$

or prove the still weaker direct output bound:

$$
\boxed{
\mathscr W_h(T)
\ll
e^{2\sigma T}\operatorname{poly}(T).
}
$$

Pros:

- permits pointwise spikes;
- matches mean-square RH phenomena;
- better aligned with causal / Green energy.

This is the recommended AMRAL route.

---

# 25. Why all 14 moment channels are still useful

Although one scalar innovation drives everything, the 14 centered channels remain useful as finite-dimensional state features.

They provide:

- boundary-flux observables;
- event-local recurrence;
- semiseparable kernel summaries;
- candidate Lyapunov coordinates.

But they should be interpreted as:

$$
\boxed{
\text{finite filters of one scalar innovation},
}
$$

not as 14 independent arithmetic sources.

This reduces the conceptual input dimension from 14 to 1.

---

# 26. Innovation work as the next missing object

The Cauchy energy is:

$$
\mathcal C_h(t)
=
2
\|s_t\|_2^2,
$$

where:

$$
(\partial_u+1)s_t
=
T_h(t-u)d\mathfrak I(u).
$$

So a future Lyapunov proof should identify the work done by:

$$
d\mathfrak I
$$

on the causal state.

The desired statement is not:

```text
innovation is always small.
```

It is closer to:

```text
innovation cannot do exponentially large positive net work
on the centered causal state.
```

That is potentially weaker than pointwise PNT control.

---

# 27. Autonomous candidate rejection rules

Reject a future candidate if:

### R1 · It only renames PNT error

```text
proof reduces to pointwise |b(t)| bound
with no new strength.
```

### R2 · It uses only innovation magnitude

```text
|innovation| <= exp(t/2)
```

and claims:

$$
\sigma<1/2.
$$

### R3 · It uses zero density but permits one rightmost exceptional zero

Energy exponential type is controlled by the rightmost zero.

### R4 · It proves only logarithmic / subpower saving

This does not change fixed:

$$
\sigma.
$$

### R5 · It proves finite-range numerical mean-square only

Finite data is evidence, not a tail theorem.

---

# 28. Candidate promotion rules

Promote a candidate if it proves one of:

### P1

$$
\int_{T-h}^{T+1+h}
|\mathfrak b|^2
\ll
e^{2\sigma T}\operatorname{poly}(T),
\qquad
\sigma<1/2.
$$

### P2

$$
\mathscr W_h(T)
\ll
e^{2\sigma T}\operatorname{poly}(T),
\qquad
\sigma<1/2.
$$

### P3

An energy-aware Lyapunov inequality that implies P2.

Every promoted candidate must record its exact:

$$
\sigma.
$$

---

# 29. Numerical reference checks

The v2.9 reference implementation checks:

1. direct critical-centered moments against the exact integration-by-parts representation through $\mathfrak b$;
2. actual local Cauchy energy against the innovation $L^2\to H^{-1}$ upper bound;
3. several moderate local prime windows at:
   $$
   h=\log2.
   $$

These are identity / inequality sanity checks only.

They are not RH evidence.

---

# 30. What has been reduced by v2.9?

Before:

```text
18-state arithmetic hybrid system
with many prime event channels.
```

After:

```text
fixed linear / hybrid filters
driven by one scalar arithmetic innovation measure.
```

Thus the remaining external mathematical input has scalar dimension:

$$
\boxed{1}.
$$

This does **not** mean the theorem is easy.

The scalar innovation contains the entire prime-distribution difficulty.

---

# 31. New smallest GAP

Fix:

$$
h=\log2.
$$

Find any:

$$
\boxed{
\sigma<\frac12
}
$$

such that one can prove:

$$
\boxed{
\mathscr W_h(T)
\ll
e^{2\sigma T}
\operatorname{poly}(T).
}
$$

Prefer proofs that do **not** first prove the stronger pointwise bound on:

$$
\mathfrak b.
$$

The desired mechanism should exploit:

- local innovation work;
- mean-square cancellation;
- causal dissipation;
- arithmetic correlations.

This is the first genuinely energy-specific tail target.

---

# 32. Suggested v3.0 direction

Recommended:

`RH-ArithmeticInnovation-WorkIdentity v3.0`

Tasks:

1. differentiate / event-update:
   $$
   \mathcal C_h(t)
   $$
   directly against the moving innovation;
2. derive exact innovation-work and dissipation terms;
3. separate positive dissipation from signed prime work;
4. integrate one complete ENTER/CENTER/EXIT lifecycle;
5. test whether lifecycle work has exact cancellations not visible in pointwise PNT;
6. compare lifecycle work to known Selberg / pair-correlation quantities;
7. search for a bound on cumulative positive work rather than on:
   $$
   |\mathfrak b(t)|.
   $$

This is the most promising route if the goal is to exploit the energy formulation rather than return to classical PNT.

---

# 33. GAP ledger

## CLOSED / REDUCED

### G1. Scalar arithmetic innovation measure

```text
CLOSED
```

### G2. Shifted ENTER/CENTER/EXIT innovation system

```text
CLOSED
```

### G3. Centered moment primitive representation

```text
CLOSED
```

### G4. Innovation-to-Cauchy energy inequality

```text
CLOSED
```

### G5. Block mean-square transfer

```text
CLOSED
```

### G6. Current 2026 fixed exponent classification

```text
AUDITED
```

$$
\sigma=1/2.
$$

---

## OPEN

### G7. Any energy-aware $\sigma<1/2$

```text
OPEN
```

### G8. Innovation work identity useful for cancellation

```text
OPEN
```

### G9. Polynomial Cauchy scalar

```text
OPEN_RH_COMPLETE
```

### G10. RH

```text
OPEN
```

---

# 34. Trust boundary

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

SCALAR_INNOVATION_REDUCTION = EXACT
H_MINUS_1_BOUND = EXACT_AS_INEQUALITY

CURRENT_2026_PNT_INPUT DOES NOT GIVE SIGMA < 1/2

POINTWISE INNOVATION IMPROVEMENT WOULD ALREADY BE
A STRONG CLASSICAL PNT / ZERO-STRIP RESULT

NO ENERGY-AWARE SIGMA < 1/2 HAS BEEN PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\mathfrak b=e^{t/2-o(t)}
\Longrightarrow
\sigma<1/2.
$$

Forbidden:

$$
o(1)\text{ relative mean-square saving}
\Longrightarrow
\text{fixed exponent saving}.
$$

Forbidden:

$$
\text{one scalar input}
\Longrightarrow
\text{one easy inequality}.
$$

---

# 35. One-line status

> v2.9 isolates the actual external arithmetic input of the finite-state RH system. The entire 14-channel critical-centered moment bank is driven by one scalar signed log-prime innovation measure $d\mathfrak I=\sum\Lambda(q)q^{-1/2}\delta_{\log q}-e^{u/2}du$, with ENTER/CENTER/EXIT streams given only by translations of this same measure. Its cumulative primitive is $\mathfrak b(t)=\sum_{n\le e^t}\Lambda(n)n^{-1/2}-2e^{t/2}$. Every centered moment is an exact compact Stieltjes transform of $\mathfrak b$, and the local Cauchy energy obeys the direct $H^{-1}$ estimate $\mathcal C_h(t)\le4(h^2+1)\int_{t-h}^{t+h}|\mathfrak b(u)|^2du$. Consequently local mean-square control of the innovation primitive at exponent $\sigma$ transfers to the same zeta zero-strip exponent. Current 2026 zero-free/PNT technology still lies in the fixed class $\sigma=1/2$ despite substantial subexponential and explicit-constant improvements. The state-machine algebra is therefore no longer the main barrier: any $\sigma<1/2$ requires genuine arithmetic innovation cancellation. The pointwise route simply returns to classical PNT strength, so the next AMRAL target should instead derive an exact innovation-work identity and seek energy-specific cancellation that permits pointwise spikes while keeping the causal Cauchy output small.

---

# 36. References

1. Chiara Bellotti, **A new zero-density estimate for $\zeta(s)$ and the error term in the prime number theorem**, *Bulletin of the London Mathematical Society* 58 (2026), article e70442.  
   Preprint: https://arxiv.org/abs/2508.02041

2. Chiara Bellotti, Tim Trudgian, Andrew Yang, **Zero-free regions inspired by work of Heath-Brown**, arXiv:2603.21490, 2026.

3. F. Broucke, **On the connection between zero-free regions and the error term in the prime number theorem**, *Analysis Mathematica* (2026).  
   DOI: https://doi.org/10.1007/s10476-026-00176-y

4. Richard P. Brent, David J. Platt, Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740–762.  
   DOI: https://doi.org/10.1016/j.jnt.2021.09.016

5. Alessandro Zaccagnini, **Primes in almost all short intervals**, *Acta Arithmetica* 84 (1998), 225–244.

6. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.

7. AMRAL, **RH-CriticalCenteredState-LyapunovGate v2.8**.

8. AMRAL, **RH-CauchyPoisson-TwistScalarization v2.5**.

---

# 37. Provenance

研究主導：Neo.K

v2.9 scalar innovation reduction、centered impulsive system、innovation-primitive representation、$H^{-1}$ energy gate、2026 method-strength audit、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 arithmetic innovation / energy-aware Lyapunov gate 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
