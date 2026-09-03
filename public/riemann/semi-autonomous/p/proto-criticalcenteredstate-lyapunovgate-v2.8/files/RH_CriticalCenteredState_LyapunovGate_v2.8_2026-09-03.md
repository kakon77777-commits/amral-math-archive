工程紀錄 · 第三弧線 v2.8 · 2026-09-03 · CRITICAL_CENTERING · LYAPUNOV_GATE · RAW_QUADRATIC_NO_GO · RH_CLAIM_FALSE

# Critical-Centered State、Lyapunov Strength Ladder 與 Raw-State No-Go

**RH-CriticalCenteredState-LyapunovGate v2.8**

本節點承接：

- `RH-CauchyPoisson-TwistScalarization v2.5`
- `RH-CauchyResolvent-CausalStateFactorization v2.6`
- `RH-CausalState-MovingWindowRecurrence v2.7`

v2.7 已把 moving-window Cauchy energy寫成固定 18 維 hybrid state。

v2.8 不直接宣稱找到 Lyapunov function。

本輪先回答更基本、但對 autonomous research 非常重要的問題：

> 哪些 state coordinates 與 Lyapunov candidate 類型在結構上就不可能產生 RH-scale polynomial certificate？

本輪得到四個核心結果：

1. raw 18-state 的 coercive quadratic Lyapunov 是錯誤 target，因為 raw moment coordinates本身含有 exponentially large deterministic PNT backbone；
2. 相對座標 + continuum centering後，所有 moment channels 的 nontrivial-zero horizontal exponent精確對齊成：
   $$
   \Re\rho-\frac12;
   $$
3. 只保留 14 個 centered moments仍不可能控制完整 Cauchy energy；有限 moments有 exact nullspace，而 exponential kernel energy在該 nullspace仍可嚴格正值；
4. 正確的 Lyapunov search應使用：
   $$
   \boxed{
   \text{critical-centered moments}
   +
   \text{energy/pair state}
   }
   $$
   並把 candidate strength用：
   $$
   \sigma
   $$
   分級。

Canonical Lyapunov template：

$$
\boxed{
V_{\sigma,P}(t)
=
e^{-2\sigma t}
\left[
\mathcal C_h(t)
+
R(t)^\top P R(t)
\right],
}
$$

其中：

$$
P\succeq0.
$$

Interpretation：

```text
sigma = 1/2
    structure-blind / critical-strip baseline

0 < sigma < 1/2
    genuine fixed zero-strip progress

sigma = 0
    RH scale
```

所以 autonomous AI 的 Lyapunov objective不應是：

```text
find any stable-looking V
```

而應是：

$$
\boxed{
\min \sigma_{\rm rigorously\ certified}.
}
$$

**RH_CLAIM = False.**

---

# 0. Claim register

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE

RAW_COERCIVE_QUADRATIC_LYAPUNOV = STRUCTURALLY_WRONG_TARGET
PNT_BACKBONE_ASYMPTOTIC = CLOSED_FROM_PNT

CRITICAL_RELATIVE_MOMENTS = DEFINED
ZERO_MODE_EXPONENT_ALIGNMENT = CLOSED

MOMENT_ONLY_ENERGY_COERCIVITY = FALSE
FINITE_MOMENT_NULLSPACE_COUNTEREXAMPLE = CLOSED

STRUCTURE_BLIND_SIGMA_BASELINE = 1/2
SIGMA_LT_1_OVER_2 = ARITHMETIC_BREAKTHROUGH_GATE
SIGMA_ZERO = RH_SCALE

COMMON_QUADRATIC_ARBITRARY_SWITCHING_SEARCH = TOO_CONSERVATIVE_AS_CANONICAL_TARGET
ARITHMETIC_INNOVATION_INPUT = REQUIRED

VALID_LYAPUNOV_CERTIFICATE = OPEN
GLOBAL_RH_CERTIFICATE = FALSE
```

---

# 1. Why raw v2.7 moments are badly scaled

v2.7 uses absolute arithmetic moments:

$$
M^S_{\lambda,k}(t)
=
\sum_{q\in S(t)}
c_qe^{\lambda x_q}x_q^k,
$$

where:

$$
c_q
=
\frac{\Lambda(q)}{\sqrt q},
$$

$$
x_q=\log q,
$$

and:

$$
\lambda\in
\left\{
-1,\frac12,1
\right\}.
$$

For example:

$$
M^R_{1,0}(t)
=
\sum_{
e^t<q<e^{t+h}
}
\Lambda(q)\sqrt q.
$$

---

# 2. PNT backbone of the raw state

Using Stieltjes partial summation and:

$$
\psi(x)\sim x,
$$

we obtain:

$$
\begin{aligned}
M^R_{1,0}(t)
&\sim
\int_{e^t}^{e^{t+h}}
x^{1/2}dx
\\
&=
\boxed{
\frac23
\left(
e^{3h/2}-1
\right)
e^{3t/2}.
}
\end{aligned}
$$

More generally:

$$
M^S_{\lambda,k}
$$

has deterministic backbone at exponential rate:

$$
\boxed{
\lambda+\frac12
}
$$

up to polynomial factors from $x^k$.

Thus different raw coordinates carry artificial deterministic scales such as:

$$
e^{-t/2},
\qquad
e^t,
\qquad
e^{3t/2}.
$$

These scales are not RH violations.

They are the main prime density.

---

# 3. Raw coercive quadratic Lyapunov no-go

Suppose:

$$
X_{\rm raw}(t)
$$

contains:

$$
M^R_{1,0}(t),
$$

and a candidate quadratic Lyapunov is coercive:

$$
\boxed{
V_{\rm raw}(X)
=
X^\top PX,
\qquad
P\succ0.
}
$$

Then for some:

$$
c_P>0,
$$

$$
V_{\rm raw}(X)
\ge
c_P
\left|
M^R_{1,0}
\right|^2.
$$

By Section 2:

$$
\boxed{
V_{\rm raw}(t)
\gtrsim
e^{3t}.
}
$$

This happens already under the ordinary prime number theorem.

Therefore:

## Theorem 3.1 · Raw quadratic no-go

A coercive positive-definite quadratic form on the uncentered v2.7 state cannot be a polynomial RH certificate.

This is a coordinate obstruction, not evidence against Lyapunov methods themselves.

---

# 4. Control-theory interpretation

Common quadratic Lyapunov functions are a standard constructive sufficient condition for switched / hybrid stability.

But even in ordinary switched linear systems:

```text
COMMON QUADRATIC LYAPUNOV
```

is generally sufficient rather than necessary and can be conservative.

For AMRAL the problem is sharper:

- raw coordinates contain a large deterministic prime-density trajectory;
- the desired theorem concerns a small residual after cancellation;
- demanding coercivity on the full raw state penalizes the deterministic backbone.

So v2.8 rejects:

```text
SEARCH P > 0 ON RAW 18-STATE
```

as the canonical optimization problem.

---

# 5. Relative coordinate system

For every active prime power define:

$$
d_q(t)
=
x_q-t.
$$

Use fixed side domains:

$$
D_L=(-h,0),
$$

$$
D_R=(0,h).
$$

Define relative prime moments:

$$
\boxed{
A^S_{\lambda,j}(t)
=
\sum_{
d_q(t)\in D_S
}
c_q
e^{\lambda d_q(t)}
d_q(t)^j.
}
$$

The same seven channels per side are retained:

$$
\lambda=-1:
\quad
j=0,1,
$$

$$
\lambda=\frac12:
\quad
j=0,1,2,
$$

$$
\lambda=1:
\quad
j=0,1.
$$

Unlike the raw moments, all polynomial factors now depend only on bounded:

$$
|d|\le h.
$$

---

# 6. Exact continuum backbone

Under the main PNT density:

$$
d\psi(x)
\approx
dx.
$$

Write:

$$
x=e^{t+d},
$$

so:

$$
dx=e^{t+d}dd.
$$

The prime coefficient contributes:

$$
x^{-1/2}
e^{\lambda d}
d^j.
$$

Therefore the continuum main term is:

$$
\boxed{
e^{t/2}
b^S_{\lambda,j},
}
$$

where:

$$
\boxed{
b^S_{\lambda,j}
=
\int_{D_S}
e^{(\lambda+1/2)d}
d^j
\,dd.
}
$$

All channels now share the same deterministic exponential scale:

$$
\boxed{
e^{t/2}.
}
$$

---

# 7. Critical-centered moments

Define:

$$
\boxed{
R^S_{\lambda,j}(t)
=
A^S_{\lambda,j}(t)
-
e^{t/2}
b^S_{\lambda,j}.
}
$$

Let:

$$
R(t)\in\mathbb R^{14}
$$

collect all left/right channels.

These are not merely numerically scaled moments.

They are exact local prime-density discrepancies in a fixed relative coordinate basis.

---

# 8. Explicit-formula zero-mode calculation

Formally differentiate the classical explicit formula:

$$
\psi(x)
=
x
-
\sum_\rho
\frac{x^\rho}{\rho}
+
\cdots
$$

against a compact local test.

A nontrivial zero:

$$
\rho
$$

contributes to one relative channel:

$$
\boxed{
R^S_{\lambda,j;\rho}(t)
=
-
e^{(\rho-1/2)t}
I^S_{\lambda,j}(\rho),
}
$$

where:

$$
\boxed{
I^S_{\lambda,j}(\rho)
=
\int_{D_S}
e^{(\lambda+\rho-1/2)d}
d^j
\,dd.
}
$$

The coefficient depends on:

- side;
- aperture;
- $\lambda$;
- polynomial degree;
- zero ordinate.

But the entire $t$-exponent is:

$$
\boxed{
\rho-\frac12.
}
$$

---

# 9. Zero-exponent alignment theorem

For every channel in the 14-dimensional bank:

$$
\boxed{
\text{horizontal exponent}
=
\Re\rho-\frac12.
}
$$

Therefore:

### Critical-line zero

$$
\Re\rho=\frac12
$$

gives exponential type:

$$
0.
$$

### Off-axis zero

$$
\Re\rho
=
\frac12+\delta
$$

gives:

$$
e^{\delta t}.
$$

This is independent of:

$$
\lambda
$$

and:

$$
j.
$$

Thus the critical-centered relative coordinates are spectrally aligned.

---

# 10. Event-free moment dynamics

Between ENTER/CENTER/EXIT events the membership sets are fixed.

For:

$$
j\ge0,
$$

with convention:

$$
A_{\lambda,-1}=0,
$$

we have:

$$
\boxed{
\frac d{dt}
A^S_{\lambda,j}
=
-\lambda
A^S_{\lambda,j}
-
jA^S_{\lambda,j-1}.
}
$$

Define:

$$
b^S_{\lambda,-1}=0.
$$

Then:

$$
\boxed{
\begin{aligned}
\dot R^S_{\lambda,j}
&=
-\lambda
R^S_{\lambda,j}
-
jR^S_{\lambda,j-1}
\\
&\quad
-
e^{t/2}
g^S_{\lambda,j},
\end{aligned}
}
$$

where:

$$
\boxed{
g^S_{\lambda,j}
=
\left(
\lambda+\frac12
\right)
b^S_{\lambda,j}
+
j
b^S_{\lambda,j-1}.
}
$$

---

# 11. Boundary-flux interpretation

By differentiating:

$$
e^{(\lambda+1/2)d}d^j,
$$

we obtain:

$$
\boxed{
g^S_{\lambda,j}
=
\left[
e^{(\lambda+1/2)d}
d^j
\right]_{\partial D_S}.
}
$$

So the deterministic term in Section 10 is exactly a smooth boundary flux.

The prime event stream supplies the corresponding discrete arithmetic boundary events.

The centered moment process is therefore a linear filter driven by:

```text
DISCRETE PRIME BOUNDARY FLUX
-
SMOOTH PNT BOUNDARY FLUX.
```

This difference is the arithmetic innovation.

---

# 12. Exact event jumps of centered moments

The continuum backbone is continuous in $t$, so $R$ has the same jumps as $A$.

Let:

$$
c_q
=
\frac{\Lambda(q)}{\sqrt q}.
$$

### ENTER

At:

$$
t=x_q-h,
$$

the prime enters the right side with:

$$
d=h.
$$

Thus:

$$
\boxed{
\Delta R^R_{\lambda,j}
=
c_q
e^{\lambda h}
h^j.
}
$$

### CENTER

At:

$$
t=x_q,
$$

the prime transfers from right to left.

For:

$$
j=0,
$$

$$
\boxed{
\Delta R^R_{\lambda,0}=-c_q,
}
$$

$$
\boxed{
\Delta R^L_{\lambda,0}=+c_q.
}
$$

For:

$$
j>0,
$$

the moment contribution is zero at:

$$
d=0,
$$

so there is no jump.

### EXIT

At:

$$
t=x_q+h,
$$

$$
d=-h.
$$

Thus:

$$
\boxed{
\Delta R^L_{\lambda,j}
=
-
c_q
e^{-\lambda h}
(-h)^j.
}
$$

---

# 13. Strip-scaled residual state

For a candidate strip half-width:

$$
\sigma\ge0,
$$

define:

$$
\boxed{
Z_\sigma(t)
=
e^{-\sigma t}R(t).
}
$$

Between events:

$$
\boxed{
\begin{aligned}
\dot Z^S_{\sigma;\lambda,j}
&=
-(\lambda+\sigma)
Z^S_{\sigma;\lambda,j}
-
jZ^S_{\sigma;\lambda,j-1}
\\
&\quad
-
e^{(1/2-\sigma)t}
g^S_{\lambda,j}.
\end{aligned}
}
$$

The deterministic forcing exponent is:

$$
\boxed{
\frac12-\sigma.
}
$$

---

# 14. Event-input strength scale

At a center event:

$$
t=x_q,
$$

a raw moment jump is:

$$
c_q
=
\Lambda(q)e^{-t/2}.
$$

After strip scaling:

$$
\boxed{
e^{-\sigma t}c_q
=
\Lambda(q)
e^{-(\sigma+1/2)t}.
}
$$

The number of prime events per unit log-time is asymptotically:

$$
\asymp
\frac{e^t}{t}.
$$

Since typical:

$$
\Lambda(q)
\asymp t
$$

on prime events, the aggregate event-input scale is:

$$
\boxed{
e^{(1/2-\sigma)t}.
}
$$

This matches exactly the continuous boundary-flux scale in Section 13.

Therefore any:

$$
\sigma<\frac12
$$

requires a genuine arithmetic cancellation between discrete event flux and continuum flux.

---

# 15. Structure-blind total-variation baseline

For the localized signed source:

$$
\mu_t,
$$

fixed aperture gives:

$$
\operatorname{supp}\mu_t
\subset
[t-h,t+h].
$$

Using the classical bound:

$$
\psi(x)=O(x),
$$

the prime part satisfies:

$$
\sum_{e^{t-h}<q<e^{t+h}}
\frac{\Lambda(q)}{\sqrt q}
=
O_h(e^{t/2}).
$$

The smooth background has the same scale.

Therefore:

$$
\boxed{
\|\mu_t\|_{\rm TV}
=
O_h(e^{t/2}).
}
$$

Since:

$$
0<
e^{-|u-v|}
\le1,
$$

$$
\boxed{
\mathcal C_h(t)
\le
\|\mu_t\|_{\rm TV}^2
=
O_h(e^t).
}
$$

---

# 16. Structure-blind residual-moment bound

Every relative test function:

$$
e^{\lambda d}d^j
$$

is bounded on:

$$
[-h,h].
$$

Hence:

$$
A^S_{\lambda,j}
=
O_h(e^{t/2}),
$$

and the continuum backbone is also:

$$
O_h(e^{t/2}).
$$

Therefore:

$$
\boxed{
R(t)
=
O_h(e^{t/2})
}
$$

componentwise without using subtle arithmetic cancellation.

Thus:

$$
\boxed{
e^{-t}\,
R(t)^\top P R(t)
=
O_{h,P}(1)
}
$$

for fixed:

$$
P\succeq0.
$$

---

# 17. Canonical Lyapunov strength ladder

Define:

$$
\boxed{
V_{\sigma,P}(t)
=
e^{-2\sigma t}
\left[
\mathcal C_h(t)
+
R(t)^\top P R(t)
\right].
}
$$

### Baseline

For:

$$
\sigma=\frac12,
$$

Sections 15–16 give a structure-blind boundedness scale:

$$
V_{1/2,P}=O(1).
$$

### Fixed-strip progress

If for some:

$$
0<\sigma<\frac12
$$

one proves:

$$
\boxed{
V_{\sigma,P}(t)
=
O(t^A)
}
$$

for finite $A$, then:

$$
\mathcal C_h(t)
\ll
e^{2\sigma t}
t^A.
$$

The earlier AMRAL energy-exponent bridge yields:

$$
\boxed{
\left|
\Re\rho-\frac12
\right|
\le
\sigma.
}
$$

### RH scale

For:

$$
\sigma=0,
$$

any polynomial bound on:

$$
V_{0,P}
$$

implies polynomial Cauchy energy and hence RH by v2.5.

---

# 18. Lyapunov optimization objective

The autonomous search objective should be:

$$
\boxed{
\sigma_\star
=
\inf
\left\{
\sigma:
\exists P,\,
V_{\sigma,P}
\text{ rigorously polynomially bounded}
\right\}.
}
$$

Interpretation:

```text
sigma_star = 1/2
    no fixed-strip improvement

sigma_star < 1/2
    genuine new zero-strip theorem

sigma_star = 0
    RH scale
```

This is the Lyapunov version of the previous:

$$
\beta
$$

and:

$$
\kappa
$$

progress meters.

---

# 19. Why moment-only Lyapunov cannot be exact

The 14 centered moments are linear functionals of the localized signed measure.

Let the corresponding test functions be:

$$
\phi_1,\ldots,\phi_{14}.
$$

A finite collection of moments cannot determine an arbitrary signed measure on:

$$
[-h,h].
$$

This can be made completely explicit.

---

# 20. Finite-moment nullspace construction

Choose eight distinct points:

$$
0<d_1<\cdots<d_8<h
$$

inside the right half.

There are only seven right-side moment functions:

$$
e^{-d},
\quad
de^{-d},
$$

$$
e^{d/2},
\quad
de^{d/2},
\quad
d^2e^{d/2},
$$

$$
e^d,
\quad
de^d.
$$

Form the:

$$
7\times8
$$

matrix:

$$
A_{ij}
=
\phi_i(d_j).
$$

Its nullspace is nontrivial.

So choose:

$$
a\neq0
$$

such that:

$$
Aa=0.
$$

Define:

$$
\boxed{
\eta
=
\sum_{j=1}^8
a_j\delta_{d_j}.
}
$$

Then every right moment is zero.

All left moments are trivially zero because $\eta$ is supported on the right.

Therefore:

$$
\boxed{
R(\eta)=0.
}
$$

---

# 21. But Cauchy energy remains positive

The energy is:

$$
\boxed{
\mathcal C(\eta)
=
a^\top Ka,
}
$$

where:

$$
K_{ij}
=
e^{-|d_i-d_j|}.
$$

For distinct points the exponential kernel is strictly positive definite.

Equivalently:

$$
a^\top Ka
=
\int_{\mathbb R}
\frac{
\left|
\sum_j
a_je^{-i\tau d_j}
\right|^2
}{
\pi(1+\tau^2)
}
d\tau.
$$

If this were zero, the exponential polynomial:

$$
\sum_j
a_je^{-i\tau d_j}
$$

would vanish identically, forcing:

$$
a=0,
$$

a contradiction.

Hence:

$$
\boxed{
R(\eta)=0
\quad\text{but}\quad
\mathcal C(\eta)>0.
}
$$

---

# 22. Moment-only coercivity no-go

Therefore no function depending only on the 14 moments can distinguish:

$$
\eta
$$

from the zero measure.

In particular:

## Theorem 22.1

There is no finite constant $C$ such that for all compact signed measures:

$$
\boxed{
\mathcal C(\mu)
\le
C
\|R(\mu)\|^2.
}
$$

More generally, no exact energy certificate can depend only on these 14 moments without additional structural assumptions.

Thus the energy / pair state in v2.7 is not redundant.

---

# 23. Structure-blind Lyapunov no-go

Suppose an argument uses only:

- fixed support width;
- positivity of the kernel;
- total-variation scale:
  $$
  \|\mu_t\|_{\rm TV}
  \le
  Ce^{t/2};
  $$
- generic event-rate or dwell-time information.

These data alone cannot imply an exponent below:

$$
1.
$$

Indeed choose any fixed nonzero compact signed measure:

$$
\eta
$$

and define the admissible-size family:

$$
\mu_t
=
e^{t/2}\eta.
$$

Then:

$$
\|\mu_t\|_{\rm TV}
=
e^{t/2}
\|\eta\|_{\rm TV},
$$

but:

$$
\boxed{
\mathcal C(\mu_t)
=
e^t
\mathcal C(\eta).
}
$$

So:

$$
\boxed{
\sigma=\frac12
}
$$

is optimal for structure-blind norm arguments.

Any:

$$
\sigma<\frac12
$$

must exploit arithmetic properties of the actual von Mangoldt event stream.

---

# 24. Why arbitrary-switching stability is the wrong abstraction

The prime event sequence is not an arbitrary switching signal.

Its event times are exactly:

$$
\log(p^k)-h,
\quad
\log(p^k),
\quad
\log(p^k)+h.
$$

Its weights are exactly:

$$
\frac{\Lambda(p^k)}{\sqrt{p^k}}.
$$

A common Lyapunov theorem robust to every switching sequence would intentionally forget:

- prime locations;
- prime-power structure;
- von Mangoldt weights;
- correlations;
- explicit-formula cancellations.

But these are exactly the ingredients needed to improve:

$$
\sigma=\frac12.
$$

So the valid research abstraction is:

```text
ARITHMETICALLY FORCED HYBRID SYSTEM
```

not:

```text
ARBITRARY SWITCHED SYSTEM.
```

---

# 25. Arithmetic innovation formulation

The centered dynamics from Sections 10–12 separate naturally into:

```text
DETERMINISTIC CONTINUUM BOUNDARY FLUX
```

and:

```text
DISCRETE PRIME EVENT FLUX.
```

Define their difference as the arithmetic innovation stream:

$$
\boxed{
d\mathfrak I
=
d\mathfrak I_{\rm prime}
-
d\mathfrak I_{\rm continuum}.
}
$$

The 14 centered moment channels are linear filters of this innovation.

Therefore a successful Lyapunov theorem must ultimately prove one of:

1. the innovation has a strong enough cancellation norm;
2. the event correlations force contraction in the energy-aware state;
3. a number-theoretic invariant bounds cumulative innovation work.

The hybrid-system algebra alone cannot supply that theorem.

---

# 26. Candidate acceptance gate

A future Lyapunov candidate should be rejected before expensive verification if any of the following holds.

## Reject R1 · Raw coercivity

```text
Candidate is positive definite on the uncentered 18-state.
```

## Reject R2 · Moment-only

```text
Candidate ignores the Cauchy energy / pair state
and claims the 14 moments are coercive.
```

## Reject R3 · Structure-blind

```text
Proof uses only support width, positivity, TV size, event count,
or arbitrary-switching stability.
```

## Reject R4 · No sigma

```text
Candidate does not state which fixed-strip exponent it certifies.
```

## Reject R5 · Simulation-only

```text
Candidate is stable on finite prime data but has no analytic flow/jump inequality.
```

---

# 27. Candidate promotion gate

A candidate may be promoted if it contains:

1. critical-centered state definition;
2. explicit:
   $$
   \sigma;
   $$
3. energy-aware coercivity;
4. event-free flow inequality;
5. ENTER/CENTER/EXIT jump inequality;
6. explicit arithmetic hypothesis or proved arithmetic lemma;
7. translated zero-strip consequence;
8. independent symbolic / interval verification.

Only then should:

$$
\sigma<\frac12
$$

be labeled mathematical progress.

---

# 28. Numerical sanity on the centered coordinates

The reference implementation evaluates:

$$
h=\log2.
$$

For moderate $t$:

```text
t = 2,4,6,8,10
```

the largest raw relative prime moment grows from order:

$$
3
$$

to order:

$$
181,
$$

tracking the:

$$
e^{t/2}
$$

continuum backbone.

After exact continuum subtraction, the largest centered residual in the same finite sample stays below approximately:

$$
1.
$$

This finite behavior is consistent with the critical centering.

It is not evidence for RH.

---

# 29. Numerical nullspace sanity

The reference package also chooses eight points in:

$$
(0,h)
$$

and solves for a nonzero weight vector annihilating all seven right moment functions.

Reference residual:

$$
\|Aa\|_\infty
$$

is at floating-point roundoff scale.

Yet the exponential-kernel energy:

$$
a^\top Ka
$$

is strictly positive.

This numerically illustrates Theorem 22.1.

The theorem itself is linear-algebraic and does not depend on the numerical example.

---

# 30. What v2.8 changes in the autonomous research loop

Before v2.8:

```text
TRY QUADRATIC LYAPUNOV ON 18 STATES
```

could waste large compute on structurally invalid coordinates.

After v2.8:

```text
1. CENTER PNT BACKBONE
2. ALIGN ZERO EXPONENTS
3. INCLUDE ENERGY STATE
4. DECLARE SIGMA
5. PROVE ARITHMETIC INNOVATION CONTROL
6. CHECK FLOW
7. CHECK EVENTS
8. TRANSLATE TO ZERO STRIP
```

This is a much narrower search space.

---

# 31. Suggested v2.9 direction

Recommended:

`RH-ArithmeticInnovation-LyapunovSearch v2.9`

Do not search arbitrary quadratic matrices yet.

Use the centered state.

Tasks:

1. build the exact centered event/flow recurrence;
2. represent the discrete-minus-continuum boundary innovation explicitly;
3. derive a baseline:
   $$
   \sigma=\frac12
   $$
   certificate analytically;
4. ask whether any known PNT / zero-density / Selberg input lowers the innovation norm to:
   $$
   \sigma<\frac12;
   $$
5. test energy-aware quadratic forms:
   $$
   \mathcal C+R^\top PR;
   $$
6. use SDP/SOS only to propose $P$, never as proof;
7. convert successful numerical candidates into exact inequalities;
8. reject every candidate whose gain comes only from raw-coordinate scaling.

---

# 32. GAP ledger

## CLOSED / REDUCED

### G1. Raw-state quadratic no-go

```text
CLOSED
```

### G2. Critical relative centering

```text
CLOSED
```

### G3. Zero-mode exponent alignment

```text
CLOSED
```

### G4. Structure-blind $\sigma=1/2$ baseline

```text
CLOSED
```

### G5. Moment-only coercivity no-go

```text
CLOSED
```

### G6. Lyapunov strength ladder

```text
DEFINED
```

---

## OPEN

### G7. Exact centered hybrid recurrence

```text
OPEN_ENGINEERING
```

### G8. Arithmetic innovation norm

```text
OPEN
```

### G9. Any rigorous $\sigma<1/2$

```text
OPEN
```

### G10. Polynomial $\sigma=0$ Lyapunov

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

CRITICAL_CENTERING = EXACT
ZERO_MODE_ALIGNMENT = EXACT_AT_EXPLICIT_FORMULA_MODE LEVEL

FINITE CENTERED NUMERICS = NOT RH EVIDENCE

RAW CQLF FAILURE = COORDINATE NO-GO
NOT A NO-GO FOR LYAPUNOV METHODS

MOMENT-ONLY FAILURE = GENERAL SIGNED-MEASURE NO-GO
ARITHMETIC-SPECIFIC EXTRA CONSTRAINTS MAY ADD INFORMATION

NO SIGMA < 1/2 CERTIFICATE HAS BEEN PROVED

GLOBAL_RH_CERTIFICATE = FALSE
```

Forbidden:

$$
\text{centered residuals look bounded numerically}
\Longrightarrow
RH.
$$

Forbidden:

$$
\text{no raw quadratic Lyapunov}
\Longrightarrow
\text{no Lyapunov proof exists}.
$$

Forbidden:

$$
\text{14 moments bounded}
\Longrightarrow
\mathcal C_h
\text{ bounded}.
$$

---

# 34. One-line status

> v2.8 performs the Lyapunov audit required after the v2.7 finite-state reduction. The raw 18-state is not a valid coercive Lyapunov coordinate system because its arithmetic moments contain exponentially large deterministic PNT backbones; for example $M^R_{1,0}\sim \frac23(e^{3h/2}-1)e^{3t/2}$, so any positive-definite raw quadratic necessarily explodes even when the prime number theorem holds. Passing to relative coordinates and subtracting the exact continuum backbone produces 14 critical-centered moments whose individual nontrivial-zero contributions all have the same horizontal exponent $\Re\rho-1/2$, independent of the original moment channel. The structure-blind total-variation bound gives the canonical $\sigma=1/2$ Lyapunov baseline, while any rigorous $\sigma<1/2$ would be a genuine fixed zero-strip improvement and $\sigma=0$ is the RH scale. A second exact no-go shows that the 14 moments alone cannot control the Cauchy energy: eight point masses can annihilate all seven right-side moments while retaining strictly positive exponential-kernel energy. Therefore a legitimate Lyapunov search must include the energy/pair state and exploit arithmetic innovation—the discrepancy between discrete prime boundary flux and smooth PNT flux. The next node should construct that centered impulsive system explicitly and search only energy-aware, sigma-labelled Lyapunov candidates.

---

# 35. References

1. Daniel Liberzon, **Stability Criteria for Switched and Hybrid Systems**, *SIAM Review* 49 (2007), 545–592.  
   https://epubs.siam.org/doi/10.1137/05063516X

2. Shota Nakayama, Koichi Kobayashi, Yuh Yamashita, **A Common Lyapunov Function Approach to Event-Triggered Control with Self-Triggered Sampling for Switched Linear Systems**, *IEICE Transactions on Fundamentals* E108-A (2025), 575–581.  
   DOI: https://doi.org/10.1587/transfun.2024EAP1059

3. NIST Digital Library of Mathematical Functions, **Multiplicative Number Theory: Asymptotic Formulas; Prime Number Theorem background**, §27.11.  
   https://dlmf.nist.gov/27.11

4. G. B. Rybicki, W. H. Press, **A Class of Fast Methods for Processing Irregularly Sampled or Otherwise Inhomogeneous One-Dimensional Data**, *Physical Review Letters* 74 (1995), 1060–1063.

5. AMRAL, **RH-CauchyPoisson-TwistScalarization v2.5**.

6. AMRAL, **RH-CausalState-MovingWindowRecurrence v2.7**.

---

# 36. Provenance

研究主導：Neo.K

v2.8 critical centering、raw-state Lyapunov no-go、zero-mode exponent alignment、moment-nullspace no-go、Lyapunov strength ladder、reference implementation 與 canonical source 整理：ChatGPT / GPT-5.6 Sol

日期：2026-09-03

研究定位：AMRAL 黎曼猜想半自主研究線，第三弧線 critical-centered Lyapunov / arithmetic innovation gate 節點。

本文件是 research source artifact，不是 peer-reviewed publication。

所有 claim 必須依 Claim register、GAP ledger 與 Trust boundary 解讀。
