---
title: "Navier–Stokes Reverse Formation Program 02: Critical UV First-Passage Skeleton, Shell Carrier/Bypass Dichotomy, and Nonlinear Source Debt"
short_title: "NS-RFP 02"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural advance / partial Chain-Necessity bridge"
epistemic_status: "Proves that critical UV escape generates a canonical adjacent-scale first-passage skeleton and an equation-level nonlinear source debt on every non-synchronous edge. Does NOT yet prove source-resolved ancestry, spatial-core ancestry, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 02

# Critical UV First-Passage Skeleton, Shell Carrier/Bypass Dichotomy, and Nonlinear Source Debt

## 0. Positioning of this Paper

NS-RFP 01 rewrites the Navier–Stokes singularity problem as:

$$
\boxed{
\text{State}
+
\text{Edge}
+
\text{Guard}
+
\text{Escape}
+
\text{Closure}.
}
$$

and proposes two ultimate proof obligations:

$$
\boxed{
\textbf{Chain Necessity}
+
\textbf{Finite Obstruction}.
}
$$

The first obligation is:

$$
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\exists
\Gamma_\infty
\in
\mathfrak A_{NS}^{\infty}.
$$

The previously known internal reduction only reaches:

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{critical UV escape}.
}
$$

This paper attacks the first bridge between the two.

The main result is not the full Chain Necessity.

This paper proves:

$$
\boxed{
\text{critical UV escape}
\Longrightarrow
\text{canonical adjacent-scale first-passage skeleton}
}
$$

and further proves:

$$
\boxed{
\text{every non-synchronous first-passage edge carries a positive nonlinear Duhamel source debt}.
}
$$

Therefore:

$$
\boxed{
\text{high-frequency presence}
}
$$

is elevated for the first time to:

$$
\boxed{
\text{time-ordered scale crossing}
+
\text{equation-level source burden}.
}
$$

The information still missing is:

$$
\boxed{
\text{which parent interaction generated the child?}
}
$$

and:

$$
\boxed{
\text{where is the physical-space ancestry core?}
}
$$

---

# 1. Setting

Consider the three-dimensional incompressible Navier–Stokes equations:

$$
\partial_tu
-\nu\Delta u
+
\mathbb P\nabla\cdot(u\otimes u)
=
0,
$$

$$
\nabla\cdot u=0,
$$

smooth on:

$$
0\le t<T_\ast.
$$

$\mathbb P$ is the Leray projector.

Assume:

$$
T_\ast<\infty
$$

is the maximal smooth existence time.

Take the standard smooth homogeneous Littlewood–Paley decomposition:

$$
u
=
\sum_{j\in\mathbb Z}
u_j,
$$

where:

$$
u_j
=
\Delta_j u.
$$

All high-frequency quantities in this paper are used on the smooth pre-singular interval, thus avoiding distribution-level low-frequency ambiguity.

---

# 2. Critical UV Input

Previously proven reduction:

## Proposition 2.1 — Critical UV Necessity

If:

$$
T_\ast
$$

is a genuine finite singular time,

then for any fixed dyadic cutoff:

$$
J<\infty,
$$

we have:

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\|P_{>J}u(t)\|_{L^3}
=
\infty.
}
$$

The proof only uses:

- the critical $L^3$ blow-up criterion;
- the energy bound;
- the Bernstein inequality.

This paper takes Proposition 2.1 as an internal proved input.

---

# 3. Why is using $\|P_{>J}u\|_3$ directly not clean enough?

For:

$$
H_J(t)
=
\|P_{>J}u(t)\|_3,
$$

there is no pointwise norm monotonicity as $J$ increases:

$$
H_{J+1}(t)
\le
H_J(t)
$$

does not hold in general.

The reason is that:

$$
L^3
$$

is not a frequency-orthogonal norm.

If we directly use:

$$
H_J
$$

to define the first-passage time,

we cannot automatically obtain:

$$
\tau_J
\le
\tau_{J+1}.
$$

Therefore, we need a replacement that is:

- critical;
- dyadic;
- high-tail;
- monotonic with respect to $J$.

---

# 4. Critical Shell Burden

Define:

$$
\boxed{
\mathcal B_J(t)
=
\left(
\sum_{j>J}
\|u_j(t)\|_{L^3}^2
\right)^{1/2}.
}
$$

referred to as the:

$$
\boxed{
\textbf{critical shell burden}.
}
$$

Each:

$$
\|u_j\|_3
$$

is a critical amplitude under the Navier–Stokes scaling.

$\mathcal B_J$ is the $\ell^2$ aggregation of high-frequency shell amplitudes.

---

# 5. Scale Monotonicity of $\mathcal B_J$

By definition:

$$
\mathcal B_{J+1}(t)^2
=
\sum_{j>J+1}
\|u_j(t)\|_3^2
\le
\sum_{j>J}
\|u_j(t)\|_3^2.
$$

Therefore:

$$
\boxed{
\mathcal B_{J+1}(t)
\le
\mathcal B_J(t).
}
$$

This is exact.

---

# 6. Littlewood–Paley Domination

The Littlewood–Paley square-function inequality gives:

$$
\|P_{>J}u\|_3
\le
C_{\rm LP}
\left\|
\left(
\sum_{j>J}
|u_j|^2
\right)^{1/2}
\right\|_3.
$$

Also, from:

$$
\left\|
\sum_{j>J}|u_j|^2
\right\|_{3/2}
\le
\sum_{j>J}
\||u_j|^2\|_{3/2},
$$

we have:

$$
\left\|
\left(
\sum_{j>J}|u_j|^2
\right)^{1/2}
\right\|_3
\le
\left(
\sum_{j>J}
\|u_j\|_3^2
\right)^{1/2}.
$$

Therefore:

$$
\boxed{
\|P_{>J}u(t)\|_3
\le
C_{\rm LP}\mathcal B_J(t).
}
$$

---

# 7. C2.1 — Shell-Burden UV Necessity

## Theorem 7.1

If:

$$
T_\ast
$$

is a finite singular time,

then for any fixed:

$$
J<\infty,
$$

we have:

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\mathcal B_J(t)
=
\infty.
}
$$

### Proof

If for some fixed $J$ we have:

$$
\sup_{t<T_\ast}\mathcal B_J(t)<\infty,
$$

then by Littlewood–Paley domination:

$$
\sup_{t<T_\ast}
\|P_{>J}u(t)\|_3
<
\infty,
$$

which contradicts Proposition 2.1. $\square$

---

# 8. Pre-Singular Compact-Window Tail Vanishing

## Lemma 8.1

For any:

$$
t_0<T_\ast,
$$

we have:

$$
\boxed{
\sup_{0\le t\le t_0}
\mathcal B_J(t)
\to0
\qquad
(J\to\infty).
}
$$

### Proof

Since the solution is smooth on the compact pre-singular interval:

$$
[0,t_0],
$$

for any sufficiently large:

$$
m>1/2
$$

we have:

$$
\sup_{0\le t\le t_0}
\|u(t)\|_{H^m}
<
\infty.
$$

Bernstein and dyadic Sobolev estimates give:

$$
\|u_j(t)\|_3
\le
C2^{j/2}\|u_j(t)\|_2
\le
C2^{-j(m-1/2)}
\|u(t)\|_{H^m}.
$$

Therefore:

$$
\mathcal B_J(t)^2
\le
C
\|u(t)\|_{H^m}^2
\sum_{j>J}
2^{-2j(m-1/2)}.
$$

The right-hand side converges to zero uniformly on:

$$
[0,t_0].
$$

$\square$

---

# 9. Continuity

## Lemma 9.1

For each fixed:

$$
J,
$$

the function:

$$
t\mapsto\mathcal B_J(t)
$$

is continuous on:

$$
[0,T_\ast).
$$

### Proof sketch

Each:

$$
u_j(t)
$$

is continuous in $L^3$.

For any compact:

$$
[0,t_0]\subset[0,T_\ast),
$$

the same Sobolev domination from Lemma 8.1 makes the dyadic $\ell^2$ tail converge uniformly.

Thus, the finite part is continuous, and combined with the uniformly small tail, we obtain the continuity of $\mathcal B_J$. $\square$

---

# 10. First-Passage Time

Fix a critical threshold:

$$
M>0.
$$

From the smooth initial data:

$$
\mathcal B_J(0)\to0.
$$

Thus there exists:

$$
J_0(M)
$$

such that:

$$
\mathcal B_J(0)<M
$$

for all:

$$
J\ge J_0(M).
$$

Define:

$$
\boxed{
\tau_J(M)
=
\inf
\left\{
t\in[0,T_\ast):
\mathcal B_J(t)\ge M
\right\}.
}
$$

By Theorem 7.1, this set is non-empty.

By continuity:

$$
\boxed{
\mathcal B_J(\tau_J(M))
=
M.
}
$$

---

# 11. C2.2 — UV First-Passage Skeleton Theorem

## Theorem 11.1

Assume finite-time blow-up.

For any fixed:

$$
M>0,
$$

and all sufficiently large:

$$
J,
$$

the first-passage times satisfy:

$$
\boxed{
\tau_J(M)
\le
\tau_{J+1}(M)
<
T_\ast,
}
$$

and:

$$
\boxed{
\tau_J(M)
\uparrow
T_\ast
\qquad
(J\to\infty).
}
$$

### Proof

From:

$$
\mathcal B_{J+1}(t)
\le
\mathcal B_J(t),
$$

if the deeper tail has reached the threshold:

$$
\mathcal B_{J+1}(t)\ge M,
$$

then:

$$
\mathcal B_J(t)\ge M.
$$

Therefore:

$$
\tau_J(M)
\le
\tau_{J+1}(M).
$$

Let:

$$
\tau_\infty
=
\lim_{J\to\infty}\tau_J(M)
\le
T_\ast.
$$

If:

$$
\tau_\infty<T_\ast,
$$

take:

$$
t_0
$$

satisfying:

$$
\tau_\infty<t_0<T_\ast.
$$

Then for all sufficiently large $J$:

$$
\tau_J(M)<t_0.
$$

Therefore:

$$
\sup_{0\le t\le t_0}
\mathcal B_J(t)
\ge
M.
$$

But Lemma 8.1 gives:

$$
\sup_{0\le t\le t_0}
\mathcal B_J(t)\to0.
$$

Contradiction.

Hence:

$$
\tau_\infty=T_\ast.
$$

$\square$

---

# 12. The First Genuine Bounded-Gap Skeleton

Theorem 11.1 gives a canonical sequence:

$$
\boxed{
\mathfrak S_M
=
\left\{
(\tau_J(M),J)
\right\}_{J\ge J_0(M)}.
}
$$

It satisfies the exact adjacent-scale progression of:

$$
J\to J+1.
$$

Therefore:

$$
\boxed{
\text{blow-up}
\Longrightarrow
\text{an adjacent-dyadic-scale, time-ordered UV crossing skeleton}.
}
$$

This is stronger than arbitrarily extracting:

$$
j_n\to\infty.
$$

But:

$$
\boxed{
\mathfrak S_M
\neq
\text{source-traceable ancestry}.
}
$$

Currently we only obtain:

$$
\text{crossing order},
$$

without obtaining:

$$
\text{parent identity}.
$$

---

# 13. First-Passage Shell Decomposition

By definition:

$$
\mathcal B_J(t)^2
=
\|u_{J+1}(t)\|_3^2
+
\mathcal B_{J+1}(t)^2.
$$

At:

$$
t=\tau_J(M)
$$

we have:

$$
M^2
=
\|u_{J+1}(\tau_J)\|_3^2
+
\mathcal B_{J+1}(\tau_J)^2.
$$

Define:

$$
\boxed{
\eta_J(M)
=
\frac{
\mathcal B_{J+1}(\tau_J(M))
}{
M
},
}
$$

and:

$$
\boxed{
\beta_J(M)
=
\frac{
\|u_{J+1}(\tau_J(M))\|_3
}{
M
}.
}
$$

Then:

$$
\boxed{
\eta_J(M)^2+\beta_J(M)^2=1.
}
$$

---

# 14. C2.3 — Shell Carrier / Deep-Tail Bypass Dichotomy

## Theorem 14.1

Each first-passage scale:

$$
J
$$

exactly satisfies:

$$
\boxed{
\beta_J
=
\sqrt{1-\eta_J^2}.
}
$$

Thus it can be divided into:

## Branch SC — Shell-carrier

If there exists:

$$
\delta>0
$$

such that:

$$
\eta_J\le1-\delta,
$$

then:

$$
\boxed{
\|u_{J+1}(\tau_J)\|_3
\ge
M\sqrt{1-(1-\delta)^2}.
}
$$

So the crossing has an immediate-shell carrier of order-$M$.

## Branch DB — Deep-tail bypass

If:

$$
\eta_J\to1,
$$

then:

$$
\beta_J\to0.
$$

That is:

$$
\boxed{
\text{threshold is already carried mainly by scales deeper than }J+1.
}
$$

---

# 15. Important No-Go: Adjacent Crossing Does Not Equal Adjacent Source

Even if:

$$
\tau_J
\le
\tau_{J+1}
$$

and the scale index only differs by:

$$
1,
$$

it still does not imply:

$$
u_{J+1}
\text{ generated }
u_{J+2}.
$$

Especially when:

$$
\eta_J\approx1,
$$

the child threshold might already be supported by a much deeper tail.

Therefore:

$$
\boxed{
\text{adjacent first-passage skeleton}
\neq
\text{adjacent nonlinear cascade}.
}
$$

This is the second core no-go of this paper.

---

# 16. Edge Delay

Define:

$$
\boxed{
\Delta\tau_J(M)
=
\tau_{J+1}(M)-\tau_J(M)
\ge0.
}
$$

and the parabolically normalized delay:

$$
\boxed{
\Theta_J(M)
=
2^{2J}
\Delta\tau_J(M).
}
$$

Under the dyadic Navier–Stokes rescaling:

$$
u^{(m)}(x,t)
=
2^m
u(2^m x,2^{2m}t),
$$

the threshold:

$$
M
$$

remains invariant,

while the index shifts.

Therefore:

$$
\boxed{
\Theta_J
}
$$

is a dyadic scale-covariant diagnostic.

---

# 17. Delay Regime

Currently, no theorem excludes:

$$
\Theta_J\to0,
$$

$$
\Theta_J\sim1,
$$

or:

$$
\Theta_J\to\infty.
$$

They correspond respectively to:

- faster-than-parabolic crossing;
- parabolic-scale crossing;
- slower-than-parabolic crossing.

But:

$$
\sum_J\Delta\tau_J
=
T_\ast-\tau_{J_0}
$$

only controls the unnormalized total delay.

It does **not** individually control:

$$
\Theta_J.
$$

Therefore:

$$
\boxed{
\text{finite terminal time}
\not\Rightarrow
\text{parabolic edge timing}.
}
$$

---

# 18. Duhamel Representation

For:

$$
s<t<T_\ast,
$$

each dyadic block:

$$
u_j(t)
=
e^{\nu(t-s)\Delta}u_j(s)
-
\int_s^t
e^{\nu(t-r)\Delta}
\Delta_j
\mathbb P\nabla\cdot(u\otimes u)(r)
\,dr.
$$

The heat semigroup is contractive on:

$$
L^3
$$

$$
\|e^{\nu(t-s)\Delta}f\|_3
\le
\|f\|_3.
$$

---

# 19. Damped Nonlinear Tail Source

For:

$$
s<t,
$$

define:

$$
\boxed{
\mathcal N_J(r;t)
=
\left(
\sum_{j>J}
\left\|
e^{\nu(t-r)\Delta}
\Delta_j
\mathbb P\nabla\cdot(u\otimes u)(r)
\right\|_3^2
\right)^{1/2}.
}
$$

By Duhamel, $L^3$ heat contraction, and Minkowski's inequality in $\ell^2$:

$$
\boxed{
\mathcal B_J(t)
\le
\mathcal B_J(s)
+
\int_s^t
\mathcal N_J(r;t)\,dr.
}
$$

Here, the heat flow is not treated as a source.

Heat evolution can only transport / dissipate the existing shell burden;

the positive increment of the critical tail burden must be paid by the nonlinear Duhamel term.

---

# 20. C2.4 — Nonlinear Source Debt Theorem

## Theorem 20.1

Let:

$$
s_J
=
\tau_J(M),
$$

$$
t_J
=
\tau_{J+1}(M).
$$

Then:

$$
\mathcal B_{J+1}(t_J)
=
M.
$$

Define the first-passage deficit:

$$
\boxed{
d_J(M)
=
M
-
\mathcal B_{J+1}(s_J)
=
M(1-\eta_J).
}
$$

Then:

$$
\boxed{
\int_{s_J}^{t_J}
\mathcal N_{J+1}(r;t_J)\,dr
\ge
d_J(M).
}
$$

### Proof

By the Duhamel tail inequality:

$$
M
=
\mathcal B_{J+1}(t_J)
\le
\mathcal B_{J+1}(s_J)
+
\int_{s_J}^{t_J}
\mathcal N_{J+1}(r;t_J)\,dr.
$$

Rearranging yields:

$$
\int_{s_J}^{t_J}
\mathcal N_{J+1}(r;t_J)\,dr
\ge
M-\mathcal B_{J+1}(s_J).
$$

$\square$

---

# 21. Significance of the Source Debt

If:

$$
\eta_J<1,
$$

then:

$$
d_J>0.
$$

Therefore:

$$
\boxed{
\text{the deeper-tail threshold cannot be reached by pure heat evolution alone}.
}
$$

There must be a genuine Navier–Stokes nonlinear source:

$$
\mathbb P\nabla\cdot(u\otimes u)
$$

paying an aggregate damped source burden of at least:

$$
d_J
$$

on:

$$
[\tau_J,\tau_{J+1}].
$$

This is the first equation-level bridge in this paper from:

$$
\text{high-frequency presence}
$$

to:

$$
\text{source traceability}.
$$

---

# 22. Synchronous Branch

If:

$$
\tau_{J+1}
=
\tau_J,
$$

then by first-passage continuity:

$$
\mathcal B_{J+1}(\tau_J)=M.
$$

So:

$$
\eta_J=1,
$$

$$
d_J=0,
$$

and:

$$
\beta_J=0.
$$

At this time, the deeper tail and the parent tail first-cross the threshold simultaneously.

This is called:

$$
\boxed{
\textbf{synchronous deep-tail crossing}.
}
$$

This is not source-free dynamics.

It merely indicates that the interval:

$$
[\tau_J,\tau_{J+1}]
$$

collapses to zero,

thus the source of this edge cannot be resolved using a positive-time Duhamel increment.

This is a new escape class.

---

# 23. Sequential Source-Paid Branch

If:

$$
\tau_{J+1}>\tau_J
$$

and:

$$
\eta_J<1,
$$

then:

$$
d_J>0.
$$

This is called:

$$
\boxed{
\textbf{sequential source-paid crossing}.
}
$$

Its necessary condition is:

$$
\boxed{
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}(r;\tau_{J+1})\,dr
\ge
M(1-\eta_J).
}
$$

This is a genuine source burden certificate.

---

# 24. Source Burden Does Not Equal Parent Identification

Theorem 20.1 still cannot imply:

$$
\boxed{
\text{which dyadic parent pair generated the debt}.
}
$$

Because:

$$
\mathbb P\nabla\cdot(u\otimes u)
$$

contains all quadratic interactions.

Therefore:

$$
\boxed{
\text{source existence}
\neq
\text{source identity}.
}
$$

This is the core gap yet to be completed for the full Chain Necessity.

---

# 25. Bony Source Split

Using the paraproduct decomposition:

$$
u\otimes u
=
T_u u
+
T_u^\ast u
+
R(u,u).
$$

Abstractly split into:

$$
\mathsf{LH},
\qquad
\mathsf{HL},
\qquad
\mathsf{HH}.
$$

That is:

- low--high;
- high--low;
- high--high/resonant.

Corresponding to:

$$
\mathcal N_J
\le
\mathcal N_J^{LH}
+
\mathcal N_J^{HL}
+
\mathcal N_J^{HH}.
$$

---

# 26. C2.5 — Coarse Source-Class Debt

## Corollary 26.1

In a sequential source-paid edge:

$$
d_J>0,
$$

there exists at least one source class:

$$
\sigma_J
\in
\{
LH,HL,HH
\}
$$

such that:

$$
\boxed{
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}^{\sigma_J}(r;\tau_{J+1})\,dr
\ge
\frac{d_J}{3}.
}
$$

### Proof

From:

$$
\mathcal N_{J+1}
\le
\mathcal N_{J+1}^{LH}
+
\mathcal N_{J+1}^{HL}
+
\mathcal N_{J+1}^{HH},
$$

and Theorem 20.1,

the time-integrated sum of the three is at least:

$$
d_J.
$$

So at least one term is no less than:

$$
d_J/3.
$$

$\square$

---

# 27. The First Source Typing Obtained So Far

Therefore, a sequential edge can already be labeled as:

$$
\boxed{
e_J^{FP}
=
\left(
J,
J+1,
\tau_J,
\tau_{J+1},
\eta_J,
d_J,
\sigma_J
\right).
}
$$

where:

$$
\sigma_J
$$

can at least be coarse-grained to:

$$
LH,
\quad
HL,
\quad
HH.
$$

This is still not the exact triad provenance of:

$$
(p,q)\to k.
$$

But it is no longer a pure scalar crossing.

---

# 28. Exact Triad Provenance Gap

To upgrade from:

$$
\sigma_J
$$

to the exact parent set:

$$
\mathcal P_J
=
\{
(p,q):
p+q=k,
\text{ significant source}
\},
$$

requires:

- frequency-localized lower bounds;
- cancellation control;
- Leray projection geometry;
- possible helical decomposition;
- source persistence across the interval.

Therefore:

$$
\boxed{
\text{coarse source class}
\not\Rightarrow
\text{exact parent provenance}.
}
$$

This gap is left for RFP-03 / RFP-05.

---

# 29. Initial-Tail Contamination

The first-passage source theorem has automatically handled an important issue.

In:

$$
[\tau_J,\tau_{J+1}],
$$

the initial stock of the deeper tail:

$$
\mathcal B_{J+1}(\tau_J)
$$

is explicitly deducted.

The source debt only counts:

$$
M-\mathcal B_{J+1}(\tau_J).
$$

Therefore:

$$
\boxed{
\text{old high-frequency stock}
}
$$

and:

$$
\boxed{
\text{new nonlinear supply}
}
$$

are not mixed together.

This is exactly the provenance separation required by the original X-Guard:

$$
G_{\rm source}.
$$

---

# 30. Heat-Tax Refinement

Theorem 20.1 only uses heat contraction:

$$
\|e^{\nu(t-s)\Delta}f\|_3
\le
\|f\|_3.
$$

For frequency-localized blocks, one can actually use:

$$
\|e^{\nu(t-s)\Delta}u_j(s)\|_3
\le
Ce^{-c\nu2^{2j}(t-s)}
\|u_j(s)\|_3.
$$

Thus, one can define the heat-taxed stock:

$$
\boxed{
\mathcal H_J(s,t)
=
\left(
\sum_{j>J}
e^{-2c\nu2^{2j}(t-s)}
\|u_j(s)\|_3^2
\right)^{1/2}.
}
$$

Then a stronger estimate is expected:

$$
\mathcal B_J(t)
\le
C\mathcal H_J(s,t)
+
\int_s^t
\mathcal N_J(r;t)\,dr.
$$

This allows the source debt to further deduct viscous survival.

This paper leaves the sharp constants and exact cutoff conventions to the next version.

---

# 31. Source-Profit Ratio

For:

$$
d_J>0,
$$

define:

$$
\boxed{
\Pi_J^{src}
=
\frac{
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}(r;\tau_{J+1})\,dr
}{
d_J
}.
}
$$

Theorem 20.1 gives:

$$
\boxed{
\Pi_J^{src}\ge1.
}
$$

But:

$$
\Pi_J^{src}\gg1
$$

might represent:

- strong source with cancellation;
- source injected into many deeper shells;
- inefficient transfer;
- repeated generation and dissipation.

Therefore:

$$
\boxed{
\text{large source budget}
\neq
\text{efficient ancestry}.
}
$$

---

# 32. First-Passage Edge State

This paper proposes upgrading the first version of the RFP edge state to:

$$
\boxed{
\Xi_J(M)
=
\left(
\tau_J,
\tau_{J+1},
\Theta_J,
\eta_J,
\beta_J,
d_J,
\Pi_J^{src},
\sigma_J
\right).
}
$$

It preserves:

- crossing time;
- normalized delay;
- immediate-shell carrier fraction;
- deep-tail bypass fraction;
- nonlinear source debt;
- coarse source type.

This is the first concrete upgrade from the C3 scalar state to the formation edge state.

---

# 33. Threshold Family

A single:

$$
M
$$

might still hide the amplitude structure.

Therefore, one can simultaneously consider:

$$
M_1<M_2<\cdots.
$$

obtaining a two-parameter first-passage lattice:

$$
\boxed{
\tau_J(M).
}
$$

It satisfies:

$$
M_1\le M_2
\Longrightarrow
\tau_J(M_1)
\le
\tau_J(M_2),
$$

and:

$$
J_1\le J_2
\Longrightarrow
\tau_{J_1}(M)
\le
\tau_{J_2}(M).
$$

Therefore:

$$
\boxed{
(J,M)
\mapsto\tau_J(M)
}
$$

forms a monotone UV first-passage surface.

---

# 34. Amplitude–Scale Partial Order

Define:

$$
(J,M)\preceq(K,N)
$$

if:

$$
J\le K,
\qquad
M\le N.
$$

Then:

$$
\boxed{
\tau_J(M)
\le
\tau_K(N).
}
$$

This provides a canonical partial order that does not rely on manually selecting a subsequence.

Future ancestry can attempt to select from this first-passage surface:

$$
\text{source-compatible paths}.
$$

---

# 35. Threshold Robustness

If the full Chain Necessity only holds under some specially crafted threshold:

$$
M
$$

it might just be an instrumentation artifact.

Therefore, a truly robust result should study the family:

$$
M\in[M_-,M_+]
$$

and seek:

$$
\boxed{
\text{threshold-uniform source / timing / carrier estimates}.
}
$$

This is the uniformity required for the future Finite Obstruction.

---

# 36. Spatial Core Gap

Currently:

$$
\mathcal B_J(t)
$$

is a global frequency quantity.

It does not specify:

$$
\Omega_J.
$$

So currently it only proves:

$$
\boxed{
\text{frequency ancestry skeleton}.
}
$$

It has not yet proven:

$$
\boxed{
\text{spacetime ancestry tube}.
}
$$

To connect to the RFP-01 state:

$$
X_J
=
(t_J,\lambda_J,\Omega_J,\ldots),
$$

one must also add:

- critical norm concentration;
- local smoothing contrapositive;
- pressure-compatible localization;
- adjoint ancestry tube.

---

# 37. Barker–Prange Interface

Existing localized smoothing / concentration theory provides critical concentration information near:

$$
R(t)
\sim
\sqrt{T_\ast-t}
$$

in specific blow-up regimes.

This provides a possible bridge:

$$
(\tau_J,J)
\Longrightarrow
\Omega_J.
$$

But this paper does not substitute concentration theorems under Type-I or other additional hypotheses for the unrestricted Chain Necessity.

Therefore:

$$
\boxed{
\text{global first-passage skeleton}
+
\text{localized concentration theorem}
}
$$

is currently just the next-step interface, not a completed theorem.

---

# 38. Relationship with the 2026 Critical-Ledger Work

Runlong Yu's 2026 finite-scale critical-ledger work considers an admissible nested parabolic-window chain for suitable weak solutions:

$$
Q_{k+1}\subset Q_k,
$$

and proves that when persistent scale-critical badness survives across finitely many scales, it must pay:

$$
\text{untaxed critical supply}
$$

or:

$$
\text{localization leakage}.
$$

Its theorem is deliberately finite-scale and explicitly does not claim global regularity.

This has high structural similarity with NS-RFP, but the logical entry point is different.

That work starts from:

$$
\boxed{
\text{an admissible parabolic chain is given}
}
$$

NS-RFP 02, on the other hand, addresses:

$$
\boxed{
\text{can a canonical scale-time skeleton be forced by blow-up necessity itself?}
}
$$

The answer in this paper is:

$$
\boxed{
\textbf{YES at global-frequency first-passage level}.
}
$$

But:

$$
\boxed{
\textbf{NOT YET at spatially localized source-resolved ancestry level}.
}
$$

The two paths are therefore complementary.

---

# 39. Interfacing the Yu Ledger with Source Debt

Yu's finite-scale language distinguishes:

$$
\text{supply},
\quad
\text{tax},
\quad
\text{leakage}.
$$

The first-passage identity in this paper naturally generates:

$$
\text{old stock}
=
\mathcal B_{J+1}(\tau_J),
$$

$$
\text{required new burden}
=
d_J,
$$

$$
\text{nonlinear supply}
=
\int\mathcal N_{J+1}.
$$

Therefore, one can expect to build a dictionary in the future:

$$
\boxed{
\text{first-passage debt}
\leftrightarrow
\text{finite-scale untaxed supply ledger}.
}
$$

But currently, the two use different state spaces:

- This paper: global frequency shell burden;
- Yu: localized CKN parabolic-window coordinates.

Formal equivalence has not yet been proven.

---

# 40. Tao Quantitative Interface

Tao's quantitative critical-$L^3$ theory explains:

If:

$$
T_\ast
$$

is a finite blow-up time,

the critical $L^3$ norm not only diverges qualitatively, but must also have quantitative lower growth along certain times.

This might upgrade:

$$
M
$$

from a fixed threshold family to:

$$
M=M(t)
$$

or:

$$
M_J\to\infty.
$$

If one can establish the quantitative relation:

$$
\tau_J(M_J)\to T_\ast
$$

then the source debt:

$$
d_J
$$

can be upgraded to an asymptotic lower bound.

This paper does not complete this quantitative upgrade.

---

# 41. Stronger Moving-Threshold Problem

Consider:

$$
M_J\uparrow\infty.
$$

Define:

$$
\tau_J(M_J).
$$

Question:

Does there exist a scale law:

$$
M_J
$$

such that:

$$
\tau_J(M_J)<T_\ast
$$

for all sufficiently large $J$,

and still have:

$$
\tau_J(M_J)\uparrow T_\ast?
$$

The fixed-$M$ theorem cannot directly imply an arbitrary:

$$
M_J\to\infty.
$$

This is a new quantitative Chain-Necessity obligation.

---

# 42. Distributed-Shell Escape

Even if:

$$
\mathcal B_J\to\infty,
$$

it is also possible that:

$$
\sup_{j>J}
\|u_j\|_3
$$

remains relatively small,

while being jointly supported by many shells:

$$
\mathcal B_J.
$$

Therefore:

$$
\boxed{
\text{UV burden divergence}
}
$$

has two basic geometries:

$$
\boxed{
\text{single/few-shell concentration}
\quad\vee\quad
\text{many-shell distribution}.
}
$$

The carrier/bypass ratio in this paper only begins to distinguish the immediate shell from the deeper tail,

and has not yet completed the entropy / occupancy census of the deeper tail.

---

# 43. Shell Entropy Candidate

Let:

$$
w_j(t;J)
=
\frac{
\|u_j(t)\|_3^2
}{
\mathcal B_J(t)^2
},
\qquad
j>J.
$$

Then:

$$
\sum_{j>J}w_j=1.
$$

One can define:

$$
\boxed{
\mathsf H_J
=
-\sum_{j>J}
w_j\log w_j.
}
$$

It can distinguish:

- low entropy: few-shell carrier;
- high entropy: distributed-shell burden.

But:

$$
\mathsf H_J
$$

is currently just a diagnostic.

It has not yet been proven to have significance as a regularity or singularity criterion.

---

# 44. Source Entropy

Similarly, the nonlinear debt might be jointly paid by:

$$
LH,
\quad
HL,
\quad
HH
$$

One can normalize the integrated source burden of each class to form:

$$
\mathsf H_J^{src}.
$$

In the future, this can measure:

$$
\boxed{
\text{source concentration}
\quad\text{vs}\quad
\text{source diversification}.
}
$$

But no entropy quantity may replace the exact PDE source identity.

---

# 45. What Has RFP-02 Truly Accomplished So Far?

Previously:

$$
\operatorname{Blowup}
\Longrightarrow
\text{UV tail unbounded}.
$$

This paper elevates it to:

$$
\boxed{
\operatorname{Blowup}
\Longrightarrow
\mathfrak S_M
=
\{(\tau_J(M),J)\}_{J\to\infty},
}
$$

where:

$$
\tau_J\le\tau_{J+1},
$$

$$
\tau_J\uparrow T_\ast,
$$

and:

$$
J\to J+1.
$$

Furthermore:

$$
\boxed{
d_J>0
\Longrightarrow
\text{positive nonlinear Duhamel source debt}.
}
$$

and:

$$
\boxed{
\text{at least one of }LH,HL,HH
\text{ pays a fixed fraction of that debt}.
}
$$

---

# 46. What Remains Unproven?

This paper has not proven that:

$$
u_{J+1}
\to
u_{J+2}
$$

is a direct parent-child generation.

It has not proven:

$$
\Omega_{J+1}\subset\Omega_J.
$$

It has not proven that:

$$
\Theta_J
$$

is bounded.

It has not proven that:

$$
d_J
$$

is uniformly positive.

It has not proven that the synchronous branch is impossible.

It has not proven that the deep-tail bypass is impossible.

It has not proven that a finite guard family blocks all skeletons.

Therefore:

$$
\boxed{
\text{First-Passage Skeleton}
\neq
\text{Full Formation Ancestry}.
}
$$

---

# 47. Partial Chain Necessity Theorem

The results of this paper can be compressed into:

## Theorem 47.1 — Partial Chain Necessity

If a finite-time singularity exists,

then for each fixed critical threshold:

$$
M>0
$$

and all sufficiently large dyadic scales $J$,

there exist canonical first-passage states:

$$
Y_J(M)
=
\left(
\tau_J(M),
J,
\mathcal B_J=M,
\eta_J,
\beta_J
\right)
$$

such that:

$$
\tau_J(M)
\uparrow T_\ast,
$$

$$
J\to J+1,
$$

and each edge:

$$
Y_J\to Y_{J+1}
$$

satisfies one of the following:

### PF-A — Sequential source-paid

$$
d_J>0
$$

and:

$$
\int_{\tau_J}^{\tau_{J+1}}
\mathcal N_{J+1}
\ge
d_J.
$$

### PF-B — Synchronous/deep-tail bypass

$$
d_J=0
$$

and the deeper tail already supports the threshold at the same first-passage time.

Therefore:

$$
\boxed{
\operatorname{Blowup}
\Longrightarrow
\text{an infinite adjacent-scale first-passage skeleton with a source-paid / bypass dichotomy at every edge}.
}
$$

$\square$

---

# 48. Why Is This Still Not Full CN?

Full Chain Necessity requires that for:

$$
\Gamma_\infty
\in
\mathfrak A_{NS}^{\infty}
$$

every edge has:

$$
\mathsf{Src},
\quad
\mathsf{Prov},
\quad
\mathsf{Guard}.
$$

PF-A of Theorem 47.1 has an aggregate nonlinear source burden,

but PF-B can still bypass a positive interval debt.

And PF-A only identifies a coarse source class,

and has not yet identified the exact parent interaction.

Therefore, the full CN is compressed into two sharper subproblems:

$$
\boxed{
\textbf{Synchronous-Bypass Resolution}
}
$$

and:

$$
\boxed{
\textbf{Exact Parent Resolution}.
}
$$

---

# 49. New Obligation SB — Synchronous-Bypass Resolution

If infinitely many:

$$
J
$$

satisfy:

$$
d_J\to0
$$

or even:

$$
d_J=0,
$$

then the deeper critical burden almost does not need to be newly generated in:

$$
[\tau_J,\tau_{J+1}].
$$

Possible explanations:

1. pre-existing deep-tail reservoir;
2. many-shell simultaneous buildup;
3. nonlocal scale jump;
4. threshold artifact;
5. true fast cascade.

It is necessary to prove which of these alternatives are N–S realizable.

---

# 50. New Obligation PR — Exact Parent Resolution

For PF-A,

it is known that:

$$
\int
\mathcal N_{J+1}
\ge
d_J.
$$

The next step is to find:

$$
\mathcal P_J
$$

such that:

$$
\boxed{
\mathcal P_J
\to
\text{child debt}
}
$$

has a quantitative lower bound.

Candidate parent classes:

$$
\text{local triad},
$$

$$
\text{high--low},
$$

$$
\text{high--high},
$$

$$
\text{nonlocal pressure-mediated},
$$

$$
\text{vorticity/strain channel}.
$$

This is the core of RFP-03 / RFP-05.

---

# 51. How Should the Roadmap Be Revised in the Next Paper?

RFP-03 in the original roadmap was:

> Local Operator Ancestry Norms and Projection–Cutoff Commutators.

After this paper, it is recommended to keep it, but add a more precise subtitle:

$$
\boxed{
\textbf{NS-RFP 03 — Exact Parent Resolution through Local Operator Ancestry Norms}
}
$$

and require it to directly handle:

$$
\text{PF-A parent resolution}
$$

and:

$$
\text{PF-B synchronous bypass}.
$$

---

# 52. Reconnection with C3-O

C3-O proves:

$$
\text{balance closeness}
\not\Rightarrow
\text{operator closeness}.
$$

RFP-02 now gives:

$$
\text{tail crossing}
\not\Rightarrow
\text{parent identification}.
$$

Both share the same information-loss pattern:

$$
\boxed{
\text{observable event}
\neq
\text{dynamical provenance}.
}
$$

Therefore, what the new series truly needs to preserve is:

$$
\boxed{
\text{event}
+
\text{source debt}
+
\text{parent identity}
+
\text{transition history}.
}
$$

---

# 53. X-Integration Update

RFP-02 can upgrade the X-formation judgment to:

$$
\frac{
\Gamma\vdash
Y_J
\to
Y_{J+1}
\qquad
d_J>0
\qquad
\Gamma\vdash
\mathsf{Debt}_{NS}(J)\ge d_J
}{
\Gamma\vdash
e_J^{FP}
:
\mathsf{source\mbox{-}paid\ candidate}
}.
$$

But it still cannot imply:

$$
\Gamma\vdash
e_J^{FP}
:
\mathsf{fully\ source\mbox{-}resolved}.
$$

Unless there is also:

$$
G_{\rm parent}
=
\mathrm{PASS}.
$$

New guard:

$$
\boxed{
G_{\rm PARENT}.
}
$$

---

# 54. New Guard — $G_{\rm SYNC}$

A synchronous edge:

$$
d_J=0
$$

cannot be treated as:

$$
\text{no dynamics happened}.
$$

New:

$$
\boxed{
G_{\rm SYNC}:
\quad
\text{zero first-passage interval debt is not zero historical source}.
}
$$

It shares the same no-go structure as C3-O's:

$$
\text{zero pairing}
\neq
\text{zero operator}
$$

---

# 55. New Guard — $G_{\rm STOCK}$

Any child burden must be split into:

$$
\boxed{
\text{old stock}
+
\text{new supply}.
}
$$

One must not misattribute:

$$
\mathcal B_{J+1}(\tau_J)
$$

as a source generated within:

$$
[\tau_J,\tau_{J+1}].
$$

New:

$$
\boxed{
G_{\rm STOCK}.
}
$$

---

# 56. New Guard — $G_{\rm SHELL}$

If:

$$
\eta_J\to1,
$$

one must not mistake the scale label:

$$
J+1
$$

for the actual carrier scale.

New:

$$
\boxed{
G_{\rm SHELL}:
\quad
\text{scale crossing label is not carrier identification}.
}
$$

---

# 57. RFP Guard Library v1

Therefore:

$$
\mathcal G_{NS}^{(1)}
=
\mathcal G_{NS}^{(0)}
\cup
\{
G_{\rm PARENT},
G_{\rm SYNC},
G_{\rm STOCK},
G_{\rm SHELL}
\}.
$$

RFP-02 not only produces theorems.

It also adds four formation-specific no-go guards.

---

# 58. Formal Status

$$
\boxed{
\begin{aligned}
\text{critical shell burden definition}
&:\ \mathrm{DEFINED},\\
\text{shell-burden UV necessity}
&:\ \mathrm{PROVED},\\
\text{compact-window high-tail vanishing}
&:\ \mathrm{PROVED},\\
\text{first-passage time monotonicity}
&:\ \mathrm{PROVED},\\
\tau_J(M)\uparrow T_\ast
&:\ \mathrm{PROVED},\\
\text{adjacent-scale first-passage skeleton}
&:\ \mathrm{PROVED},\\
\text{shell carrier/bypass identity}
&:\ \mathrm{PROVED},\\
\text{nonlinear source debt}
&:\ \mathrm{PROVED},\\
\text{coarse }LH/HL/HH\text{ source-class debt}
&:\ \mathrm{PROVED},\\
\text{parabolic normalized delay boundedness}
&:\ \mathrm{OPEN},\\
\text{synchronous-bypass resolution}
&:\ \mathrm{OPEN},\\
\text{exact parent provenance}
&:\ \mathrm{OPEN},\\
\text{spatial-core ancestry}
&:\ \mathrm{OPEN},\\
\text{full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 59. Conclusion

The previous strongest internal reduction was:

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{critical UV escape}.
}
$$

RFP-02 elevates it for the first time to:

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{canonical adjacent-scale UV first-passage skeleton}.
}
$$

For each fixed critical threshold:

$$
M>0,
$$

there exists:

$$
\tau_J(M)\uparrow T_\ast
$$

and:

$$
J\to J+1.
$$

Each crossing is then exactly decomposed into:

$$
\boxed{
\text{immediate-shell carrier}
+
\text{deeper-tail bypass}.
}
$$

More importantly,

every non-synchronous / deficit-bearing edge must pay:

$$
\boxed{
\text{positive nonlinear Duhamel source debt}.
}
$$

Therefore:

$$
\boxed{
\text{high-frequency appearance}
}
$$

is no longer just an endpoint fact.

It begins to possess:

$$
\boxed{
\text{time order}
+
\text{scale order}
+
\text{source burden}.
}
$$

The full Chain Necessity still lacks:

$$
\boxed{
\text{Synchronous-Bypass Resolution}
+
\text{Exact Parent Resolution}
+
\text{Spatial-Core Attachment}.
}
$$

The next round officially enters:

$$
\boxed{
\textbf{NS-RFP 03 — Exact Parent Resolution through Local Operator Ancestry Norms}
}
$$

---

# References

1. L. Escauriaza, G. Seregin, V. Šverák, *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58 (2003), 211–250.
2. I. Gallagher, G. S. Koch, F. Planchon, *Blow-up of critical Besov norms at a potential Navier–Stokes singularity*, Communications in Mathematical Physics 343 (2016), 39–82; arXiv:1407.4156.
3. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958.
4. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115.
5. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717.
6. W. Tan, *The localized characterization for the singularity formation in the Navier–Stokes equations*, arXiv:2107.04597.
7. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026).
8. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026).

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 03 — Exact Parent Resolution through Local Operator Ancestry Norms}
}
$$