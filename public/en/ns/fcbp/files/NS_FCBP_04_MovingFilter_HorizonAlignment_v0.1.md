---
title: "Navier–Stokes Forest Coercive Budget Program 04: Moving-Filter Telescoping, Continuous Filter Drift, Horizon Alignment, Time-Thickness Barrier and Borderline Critical Lift"
short_title: "NS-FCBP 04"
series: "Navier–Stokes Forest Coercive Budget Program"
cycle: "VI"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Moving-filter compatibility / horizon-alignment audit / thin-window criticality"
epistemic_status: "Closes one major compatibility gap and uncovers a deeper temporal one. For the smooth compact mollifiers used in the pressure-flux framework, proves an L2 filter-scale derivative estimate and derives the exact coarse Navier-Stokes equation for a continuously time-dependent filter. On the full-thickness slow schedule r_k=r_0(k+1)^(-beta), 1/2<beta<=1, a linearly moving relative filter ell_k=sigma r_k has finite total L_t^2 filter speed, and the resulting filter-drift work is universally controlled by the Leray energy/dissipation budget; hence discrete Filter-Switch Packing can be bypassed by continuous filter drift. However, proves a Parabolic Alignment Summability theorem: if adjacent full-parabolic slabs accumulate at T* and remain within O(1) local parabolic ages of the horizon, then sum r_k is necessarily finite, so a non-summable slow schedule must lose fixed parabolic horizon alignment. A second route uses horizon-aligned thin slabs tau_k=T*-c r_k^2. For a co-moving heat-semigroup filter s(t)=a(T*-t), 0<a<nu, the filter drift is exactly absorbed into a reduced positive viscosity nu-a, restoring exact endpoint compatibility at fixed relative horizon resolution. Yet a universal Time-Thickness theorem shows sum w_k delta_k<infinity for the normalized slab thickness delta_k, so bounded normalized work rate remains summable even when sum w_k diverges. A true horizon Critical Lift therefore requires inverse-thickness work amplification, long-age observability, or an equivalent recurrent source/defect mechanism. This matches recent moving-window defect theory, which leaves non-effective observability or an NS-realizable combined-invisible defect cascade. Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, and Navier-Stokes regularity remain OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Forest Coercive Budget Program 04

# Moving-Filter Telescoping, Continuous Filter Drift, Horizon Alignment, Time-Thickness Barrier and Borderline Critical Lift

## 0. Positioning of this Paper

FCBP-03 produced the first non-summable pressure--flux scale schedule:

$$
r_k
=
r_0(k+1)^{-\beta},
\qquad
\frac12<\beta\le1,
$$

for which:

$$
\sum_k r_k^2<\infty,
$$

but:

$$
\sum_k r_k/r_0=\infty.
$$

That result proved a genuine **Schedule Lift**.

However Schedule Lift is not yet Horizon Critical Lift.

The present paper addresses two compatibility problems:

1. the filter must move with the physical scale;
2. the slabs must genuinely approach the singular horizon at the correct parabolic geometry.

The first problem can be substantially closed.

The second reveals a new time-thickness barrier.

---

# 1. Smooth spatial filter

Let:

$$
\rho\in C_c^\infty(B_1),
\qquad
\rho\ge0,
\qquad
\int\rho=1.
$$

Set:

$$
\rho_\ell(x)
=
\ell^{-3}
\rho(x/\ell),
$$

and:

$$
\boxed{
S_\ell f
=
\rho_\ell*f.
}
$$

Define:

$$
q(z)
=
3\rho(z)
+
z\cdot\nabla\rho(z).
$$

Integration by parts gives:

$$
\boxed{
\int q(z)dz=0.
}
$$

---

# 2. Filter derivative

Direct differentiation gives:

$$
\boxed{
\partial_\ell
\rho_\ell(x)
=
-\ell^{-4}
q(x/\ell).
}
$$

Equivalently:

$$
\boxed{
\partial_\ell
S_\ell f
=
-\ell^{-1}
q_\ell*f,
}
$$

where:

$$
q_\ell(x)
=
\ell^{-3}
q(x/\ell).
$$

---

# 3. CIV/VI-4.1 — Filter-Scale Derivative Lemma

## Theorem 3.1

For:

$$
f\in H^1(\mathbb R^3),
$$

$$
\boxed{
\|\partial_\ell S_\ell f\|_2
\le
C_\rho
\|\nabla f\|_2,
}
$$

uniformly for:

$$
\ell>0.
$$

### Proof

Since:

$$
\int q_\ell=0,
$$

$$
q_\ell*f(x)
=
\int
q_\ell(y)
(
f(x-y)-f(x)
)
dy.
$$

Use:

$$
f(x-y)-f(x)
=
-\int_0^1
y\cdot\nabla f(x-\theta y)
d\theta.
$$

Minkowski gives:

$$
\|q_\ell*f\|_2
\le
\left(
\int
|q_\ell(y)|
|y|
dy
\right)
\|\nabla f\|_2.
$$

By scaling:

$$
\int
|q_\ell(y)|
|y|
dy
=
\ell
\int
|q(z)|
|z|
dz.
$$

Divide by:

$$
\ell.
$$

$\square$

---

# 4. Time-dependent filter

Let:

$$
\ell=\ell(t)>0
$$

be absolutely continuous.

Define:

$$
U(t)
=
S_{\ell(t)}u(t),
$$

$$
P(t)
=
S_{\ell(t)}p(t),
$$

and:

$$
R(t)
=
S_{\ell(t)}(u\otimes u)
-
U\otimes U.
$$

Set:

$$
\Pi
=
-R:\nabla U.
$$

---

# 5. CIV/VI-4.2 — Moving-Filter Coarse Navier--Stokes Equation

## Theorem 5.1

For a smooth pre-singularity Navier--Stokes solution with viscosity:

$$
\nu>0,
$$

the moving coarse field satisfies:

$$
\boxed{
\partial_tU
-
\nu\Delta U
+
\nabla\cdot(U\otimes U)
+
\nabla P
=
-\nabla\cdot R
+
\dot\ell
\partial_\ell U.
}
$$

Moreover:

$$
\nabla\cdot U=0.
$$

### Proof

Differentiate:

$$
U(t)=S_{\ell(t)}u(t):
$$

$$
\partial_tU
=
S_\ell\partial_tu
+
\dot\ell
\partial_\ell S_\ell u.
$$

Apply:

$$
S_\ell
$$

to the Navier--Stokes equation and use commutation of spatial convolution with:

$$
\nabla,
\Delta.
$$

$\square$

---

# 6. Moving-filter energy identity

Let:

$$
e_U
=
|U|^2/2.
$$

The exact local energy identity becomes:

$$
\boxed{
\partial_te_U
-
\nu\Delta e_U
+
\nu|\nabla U|^2
+
\nabla\cdot
\left[
(e_U+P)U
+
RU
\right]
=
-\Pi
+
\dot\ell
U\cdot\partial_\ell U.
}
$$

Thus the only new term relative to the fixed-filter pressure--flux ledger is the signed filter-drift work.

---

# 7. Moving-filter normalized work ledger

On slab:

$$
I_k=[\tau_k,\tau_{k+1}],
$$

radius:

$$
r_k,
$$

and admissible nonnegative weight:

$$
\phi_k,
$$

define:

$$
\boxed{
\mathcal Q_k^{drift}
=
r_k^{-1}
\int_{I_k}
\int
\phi_k
\dot\ell
U\cdot\partial_\ell U
dxdt.
}
$$

The fixed-filter local identity becomes:

$$
\boxed{
\mathcal W_k
+
\nu\mathcal D_k
=
\mathcal E_k^-
-
\mathcal E_k^+
+
\mathcal L_k
+
\mathcal Q_k^{drift}.
}
$$

---

# 8. Slow full-thickness schedule

Let:

$$
r_k
=
r_0(k+1)^{-\beta},
\qquad
\frac12<\beta\le1.
$$

Use full parabolic slab lengths:

$$
\boxed{
\tau_{k+1}-\tau_k
=
r_k^2.
}
$$

Set endpoint filters:

$$
\boxed{
\ell_k
=
\sigma r_k,
}
$$

and interpolate:

$$
\ell(t)
$$

linearly between:

$$
\ell_k
$$

and:

$$
\ell_{k+1}
$$

on:

$$
I_k.
$$

Then:

$$
\boxed{
\int_{I_k}
|\dot\ell|^2dt
=
\frac{
(\ell_k-\ell_{k+1})^2
}{
r_k^2
}.
}
$$

---

# 9. CIV/VI-4.3 — Slow-Schedule Filter-Speed Packing

## Theorem 9.1

For:

$$
r_k=r_0(k+1)^{-\beta},
$$

$$
\boxed{
\sum_k
\int_{I_k}
|\dot\ell|^2dt
<
\infty.
}
$$

More precisely:

$$
\boxed{
\sum_k
\frac{
(\ell_k-\ell_{k+1})^2
}{
r_k^2
}
\le
C_{\beta,\sigma}
\sum_k
(k+1)^{-2}
<
\infty.
}
$$

### Proof

Use:

$$
\frac{
r_k-r_{k+1}
}{
r_k
}
=
1-
\left(
\frac{k+1}{k+2}
\right)^\beta
\le
\frac{C_\beta}{k+1}.
$$

$\square$

---

# 10. Universal drift budget

Assume:

$$
0\le\phi_k\le C_\phi.
$$

Since:

$$
\|U(t)\|_2
\le
\|u(t)\|_2
\le
E_2,
$$

Theorem 3.1 gives:

$$
\left|
\int
\phi_k
U\cdot\partial_\ell U
dx
\right|
\le
C_{\phi,\rho}
E_2
\|\nabla u(t)\|_2.
$$

Use telescope weights:

$$
w_k=r_k/r_0.
$$

Then:

$$
w_k
r_k^{-1}
=
r_0^{-1}.
$$

---

# 11. CIV/VI-4.4 — Continuous Filter-Drift Packing

## Theorem 11.1

On the full-thickness slow schedule:

$$
\boxed{
\sum_k
w_k
|
\mathcal Q_k^{drift}
|
\le
\frac{
C_{\phi,\rho}
E_2
}{
r_0
}
\left(
\int
|\dot\ell|^2dt
\right)^{1/2}
\left(
\int
\|\nabla u\|_2^2dt
\right)^{1/2}
<
\infty.
}
$$

Thus scale-relative moving filters are compatible with the non-summable slow telescope at finite filter-drift cost.

### Meaning

The discrete Filter-Switch Packing problem from FCBP-03 can be bypassed on the full-thickness slow schedule by using continuous filter motion.

$\square$

---

# 12. Drift-closed slow telescope

The pressure--flux endpoint telescope is unchanged because:

$$
U(t)
$$

is continuous through slab interfaces and the same:

$$
\ell(t)
$$

is used from both sides.

Therefore:

$$
\boxed{
\begin{aligned}
\sum_{k<N}
w_k
(
\mathcal W_k^+
+
\nu\mathcal D_k
)
\le\;&
\mathcal E_0^-
+
\sum_{k<N}
w_k
|\mathcal L_k|
+
\sum_{k<N}
w_k
\mathcal W_k^-
\\
&+
B_{\rm drift},
\end{aligned}
}
$$

where:

$$
\boxed{
B_{\rm drift}<\infty
}
$$

is universal in the energy class for the chosen slow schedule.

---

# 13. First correction: Schedule Lift is not Horizon Lift

The full-thickness slow slabs satisfy:

$$
\tau_{k+1}-\tau_k=r_k^2.
$$

Let:

$$
\tau_k\uparrow T_\ast.
$$

Then:

$$
\boxed{
T_\ast-\tau_k
=
\sum_{j=k}^{\infty}
r_j^2.
}
$$

A slab is uniformly parabolically aligned with the horizon if:

$$
\boxed{
T_\ast-\tau_k
\le
C_H
r_k^2
}
$$

for all sufficiently large:

$$
k.
$$

---

# 14. CIV/VI-4.5 — Parabolic Alignment Summability Theorem

## Theorem 14.1

Let:

$$
r_k
$$

be positive and nonincreasing.

Assume:

$$
\sum_k r_k^2<\infty
$$

and:

$$
\boxed{
\sum_{j=k}^{\infty}
r_j^2
\le
C_Hr_k^2
}
$$

for all sufficiently large:

$$
k.
$$

Then:

$$
\boxed{
\sum_k r_k<\infty.
}
$$

### Proof

Choose an integer:

$$
m>4C_H.
$$

Since:

$$
r_j
$$

is nonincreasing:

$$
m
r_{k+m}^2
\le
\sum_{j=k+1}^{k+m}
r_j^2
\le
\sum_{j=k}^{\infty}
r_j^2
\le
C_Hr_k^2.
$$

Hence:

$$
r_{k+m}
\le
\sqrt{
C_H/m
}
r_k
\le
\frac12
r_k.
$$

Thus the sequence decays geometrically every:

$$
m
$$

indices.

Sum blockwise.

$\square$

---

# 15. Consequence

Uniform parabolic horizon alignment implies:

$$
\boxed{
\sum_kw_k
=
\frac1{r_0}
\sum_kr_k
<
\infty.
}
$$

Therefore:

$$
\boxed{
\text{full-thickness adjacent slabs}
+
\text{fixed horizon alignment}
\Longrightarrow
\text{summable telescope weight}.
}
$$

The non-summable slow Schedule Lift must violate fixed parabolic alignment.

---

# 16. Slow power-law horizon age

For:

$$
r_k
=
r_0(k+1)^{-\beta},
\qquad
\frac12<\beta\le1,
$$

$$
\sum_{j=k}^{\infty}
r_j^2
\asymp
k^{1-2\beta}.
$$

Since:

$$
r_k^2
\asymp
k^{-2\beta},
$$

$$
\boxed{
\frac{
T_\ast-\tau_k
}{
r_k^2
}
\asymp
k.
}
$$

Thus the slow full-thickness chain lies:

$$
O(k)
$$

local parabolic ages before the horizon at generation:

$$
k.
$$

---

# 17. Long-Age Observability Problem

To use the full-thickness slow telescope as a singular-horizon obstruction, one must propagate dangerous information across an increasing number of normalized parabolic ages.

Define:

$$
\boxed{
\textbf{LAO — Long-Age Observability}.
}
$$

> Show that dangerous horizon data continue to generate a quantitatively detectable pressure/flux/energy/trace signal on slow slabs whose normalized age from the horizon diverges.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 18. External moving-window calibration

Recent moving-window defect theory defines a combined observation strength using:

- pressure;
- flux;
- positive energy;
- adjoint trace.

It defines an observability constant:

$$
M_n,
$$

and depletion-effective observability requires a divergent series of the form:

$$
\boxed{
\sum
\lambda_n
M_n^{-q}
=
\infty.
}
$$

It proves a conditional alternative:

$$
\boxed{
\text{non-effective moving-window observability}
\vee
\text{NS-realizable combined-invisible defect cascade}.
}
$$

This is an EXTERNAL reduction theorem.

It confirms that long/moving-window observability is an independent mathematical issue rather than a bookkeeping artifact.

---

# 19. Second route: horizon-aligned thin slabs

Instead of full parabolic slabs, choose slow radii:

$$
r_k\downarrow0
$$

and force exact horizon alignment:

$$
\boxed{
\tau_k
=
T_\ast
-
c
r_k^2.
}
$$

Then:

$$
\boxed{
\tau_{k+1}-\tau_k
=
c
(
r_k^2-r_{k+1}^2
).
}
$$

Define normalized slab thickness:

$$
\boxed{
\delta_k
=
\frac{
\tau_{k+1}-\tau_k
}{
r_k^2
}
=
c
\left[
1-
\left(
\frac{r_{k+1}}{r_k}
\right)^2
\right].
}
$$

For slow radii:

$$
r_{k+1}/r_k\to1,
$$

thus:

$$
\boxed{
\delta_k\to0.
}
$$

---

# 20. Moving compact filter on aligned thin slabs

If:

$$
\ell_k=\sigma r_k
$$

and the filter is linearly moved across:

$$
I_k,
$$

the minimum:

$$
L^2
$$

filter-speed cost satisfies:

$$
\boxed{
\int_{I_k}
|\dot\ell|^2dt
\ge
\frac{
(\ell_k-\ell_{k+1})^2
}{
\tau_{k+1}-\tau_k
}.
}
$$

For small relative radius decrement this behaves like:

$$
\boxed{
C_{\sigma,c}
\frac{
r_k-r_{k+1}
}{
r_k
}.
}
$$

Since:

$$
r_k\to0,
$$

$$
\sum_k
\frac{
r_k-r_{k+1}
}{
r_k
}
$$

need not be finite and is logarithmically divergent for the standard slow schedules.

Thus the simple Leray:

$$
L_t^2
$$

filter-speed estimate no longer gives a universal aligned-chain drift closure.

This motivates a different filter family.

---

# 21. Heat-semigroup coarse graining

Let:

$$
\boxed{
S_s
=
e^{s\Delta},
\qquad
s>0.
}
$$

The heat kernel is nonnegative and has unit mass.

Define:

$$
U(t)
=
S_{s(t)}u(t),
$$

$$
P(t)
=
S_{s(t)}p(t),
$$

and:

$$
R(t)
=
S_{s(t)}(u\otimes u)
-
U\otimes U.
$$

By positivity of the heat kernel:

$$
\boxed{
R(t)\ge0
}
$$

as a covariance tensor.

---

# 22. CIV/VI-4.6 — Co-Moving Heat-Filter Equation

## Theorem 22.1

The heat-filtered velocity satisfies:

$$
\boxed{
\partial_tU
-
(
\nu+s'(t)
)
\Delta U
+
\nabla\cdot(U\otimes U)
+
\nabla P
=
-\nabla\cdot R.
}
$$

### Proof

Since:

$$
\partial_sS_s
=
\Delta S_s,
$$

$$
\partial_tU
=
S_s\partial_tu
+
s'(t)\Delta U.
$$

Apply:

$$
S_s
$$

to Navier--Stokes and rearrange.

$\square$

---

# 23. Horizon co-moving heat filter

Choose:

$$
\boxed{
s(t)
=
a
(
T_\ast-t
),
}
$$

with:

$$
\boxed{
0<a<\nu.
}
$$

Then:

$$
s'(t)=-a,
$$

and Theorem 22.1 becomes:

$$
\boxed{
\partial_tU
-
(
\nu-a
)
\Delta U
+
\nabla\cdot(U\otimes U)
+
\nabla P
=
-\nabla\cdot R.
}
$$

Thus the moving-filter correction is absorbed exactly into a reduced but strictly positive viscosity.

There is no separate filter-switch or filter-drift forcing term.

---

# 24. Critical horizon resolution

At horizon-aligned time:

$$
\tau_k
=
T_\ast-cr_k^2,
$$

the heat-filter length is:

$$
\ell_k
\sim
\sqrt{s(\tau_k)}
=
\sqrt{ac}
r_k.
$$

Therefore:

$$
\boxed{
\ell_k/r_k
=
\sqrt{ac}
}
$$

is constant at the slab entrance.

Across one thin slab the ratio stays uniformly comparable.

Hence:

$$
\boxed{
\text{exact endpoint compatibility}
+
\text{scale-relative horizon resolution}
}
$$

can coexist using the co-moving heat filter.

---

# 25. Co-moving heat pressure--flux ledger

The fixed-filter local resolved-energy identity extends with viscosity:

$$
\nu-a.
$$

Thus on each horizon-aligned slab:

$$
\boxed{
\mathcal W_k
+
(
\nu-a
)
\mathcal D_k
=
\mathcal E_k^-
-
\mathcal E_k^+
+
\mathcal L_k.
}
$$

Because the same time-dependent heat-filter trajectory:

$$
s(t)
$$

is used on both sides of every interface, endpoint energies belong to one common moving resolved system and telescope with nested cutoffs.

---

# 26. CIV/VI-4.7 — Horizon-Aligned Heat-Filter Telescope

## Theorem 26.1

For arbitrary decreasing horizon-aligned radii:

$$
\tau_k=T_\ast-cr_k^2,
$$

and weights:

$$
w_k=r_k/r_0,
$$

the co-moving heat package satisfies:

$$
\boxed{
\sum_{k<N}
w_k
(
\mathcal W_k^+
+
(
\nu-a
)
\mathcal D_k
)
\le
\mathcal E_0^-
+
\sum_{k<N}
w_k|\mathcal L_k|
+
\sum_{k<N}
w_k\mathcal W_k^-.
}
$$

### Status

This is an INTERNAL theorem for the global:

$$
\mathbb R^3
$$

finite-energy setting.

It is not attributed to the compact-mollifier external pressure--flux theorem.

$\square$

---

# 27. Time-thickness weight

For horizon-aligned adjacent slabs define:

$$
\delta_k
=
c
\left[
1-
(r_{k+1}/r_k)^2
\right].
$$

Recall:

$$
w_k=r_k/r_0.
$$

Then:

$$
w_k\delta_k
=
\frac c{r_0}
\left(
r_k
-
\frac{
r_{k+1}^2
}{
r_k
}
\right).
$$

---

# 28. CIV/VI-4.8 — Time-Thickness Summability Theorem

## Theorem 28.1

For every positive decreasing sequence:

$$
r_k,
$$

$$
\boxed{
\sum_k
w_k
\delta_k
\le
2c.
}
$$

### Proof

Since:

$$
r_{k+1}\le r_k,
$$

$$
r_k
-
\frac{
r_{k+1}^2
}{
r_k
}
=
(r_k-r_{k+1})
\left(
1+
\frac{r_{k+1}}{r_k}
\right)
\le
2
(r_k-r_{k+1}).
$$

Therefore:

$$
\sum_k
w_k\delta_k
\le
\frac{
2c
}{
r_0
}
\sum_k
(r_k-r_{k+1})
\le
2c.
$$

$\square$

---

# 29. Time-Thickness Barrier

Define normalized positive work rate:

$$
\boxed{
\mathfrak j_k
=
\frac{
\mathcal W_k^+
}{
\delta_k
}
}
$$

when:

$$
\delta_k>0.
$$

Then:

$$
\boxed{
w_k
\mathcal W_k^+
=
w_k
\delta_k
\mathfrak j_k.
}
$$

If:

$$
\sup_k
\mathfrak j_k
<
\infty,
$$

Theorem 28.1 gives:

$$
\boxed{
\sum_k
w_k
\mathcal W_k^+
<
\infty.
}
$$

Thus a non-summable scale weight does not produce a horizon obstruction when the normalized work rate remains bounded.

---

# 30. CIV/VI-4.9 — Thin-Slab Criticality No-Go

## Theorem 30.1

On any horizon-aligned adjacent slow-scale chain, a pressure--flux obstruction based only on:

$$
\boxed{
\mathcal W_k^+
\gtrsim
\delta_k
}
$$

cannot force divergence of:

$$
\sum_kw_k\mathcal W_k^+.
$$

A horizon Critical Lift requires stronger activity, such as:

$$
\boxed{
\mathfrak j_k
\to\infty
}
$$

on a sufficiently large weighted set.

$\square$

---

# 31. Borderline inverse-thickness amplification

The strongest natural thin-window rate is:

$$
\boxed{
\mathfrak j_k
\gtrsim
\delta_k^{-1}.
}
$$

Then:

$$
\boxed{
\mathcal W_k^+
\gtrsim1,
}
$$

and:

$$
\boxed{
\sum_k
w_k
\mathcal W_k^+
\gtrsim
\sum_kw_k.
}
$$

Hence any non-summable slow radius schedule produces divergent active work.

---

# 32. CIV/VI-4.10 — Borderline Horizon Work Compiler

## Theorem 32.1

Assume a horizon-aligned co-moving heat-filter chain satisfies:

1.:
   $$
   \sum_kw_k=\infty;
   $$

2. on an active index set:
   $$
   \mathcal I_{\rm act},
   $$
   one has:
   $$
   \mathfrak j_k
   \ge
   c_0
   \delta_k^{-1};
   $$

3.:
   $$
   \sum_{k\in\mathcal I_{\rm act}}w_k=\infty;
   $$

4. paid residuals satisfy:
   $$
   \sum_kw_k|\mathcal L_k|
   +
   \sum_kw_k\mathcal W_k^-
   <
   \infty.
   $$

Then the chain is impossible.

### Proof

On:

$$
\mathcal I_{\rm act},
$$

$$
\mathcal W_k^+
\ge c_0.
$$

Therefore the left side of Theorem 26.1 diverges while the right side remains finite.

$\square$

---

# 33. Relation to causal fresh-renewal rate

Earlier ANP/CFOP dual-ledger results proved:

> if a fixed fraction of a dangerous terminal state is not propagated across a shrinking cut, the normalized fresh-source rate is at least inverse in the cut width.

This has the same dimensional form as the inverse-thickness requirement:

$$
\mathfrak j_k
\gtrsim
\delta_k^{-1}.
$$

However:

$$
\boxed{
\text{fresh causal source rate}
}
$$

has not been quantitatively identified with:

$$
\boxed{
\text{signed pressure--flux work rate}.
}
$$

This is now a concrete cross-observable bridge problem.

---

# 34. Causal-Renewal / Work Bridge

Define:

$$
\boxed{
\textbf{CRW — Causal-Renewal to Work Bridge}.
}
$$

Target:

> convert inverse-window fresh causal renewal, or an equivalent dangerous source packet, into inverse-thickness pressure--flux/energy/model-cone activity on a horizon-aligned slow slab.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 35. Moving-window observability interpretation

The recent combined finite-window framework defines an observability constant:

$$
M_n
$$

for pressure, flux, energy, and adjoint-trace channels.

A moving family is depletion-effective when:

$$
\boxed{
\sum
\lambda_n
M_n^{-q}
=
\infty.
}
$$

It also proves a conditional alternative:

$$
\boxed{
\text{non-effective moving-window observability}
\vee
\text{NS-realizable combined-invisible defect cascade}.
}
$$

Thus the current FCBP thin-window problem matches an independently identified moving-window obstruction class.

---

# 36. Why observability may deteriorate on thin slabs

A horizon-aligned slow schedule has:

$$
\delta_k\to0.
$$

A finite-dimensional space-time detector restricted to a thinner normalized interval may lose sensitivity.

Therefore a uniform active-work lower bound independent of:

$$
\delta_k
$$

is highly nontrivial.

The inverse-thickness work requirement makes this explicit.

---

# 37. Two horizon strategies after FCBP-04

### Strategy H1 — full-thickness slow slabs

Advantages:

- non-summable weights;
- continuous compact-filter drift has finite Leray cost;
- normalized slab thickness:
  $$
  1.
  $$

Cost:

- parabolic age from:
  $$
  T_\ast
  $$
  grows like:
  $$
  k.
  $$

Need:

$$
\boxed{
LAO.
}
$$

### Strategy H2 — horizon-aligned thin slabs

Advantages:

- actual horizon alignment;
- co-moving heat filter has exact scale-relative resolution;
- exact non-summable pressure--flux telescope.

Cost:

-:
  $$
  \delta_k\to0;
  $$
- bounded work-rate signals are summable.

Need:

$$
\boxed{
\text{inverse-thickness amplification / CRW}.
}
$$

---

# 38. Horizon Compatibility Dichotomy

## Theorem 38.1

Within the current adjacent-slab pressure--flux architecture, a non-summable slow-scale obstruction must solve at least one of:

$$
\boxed{
\textbf{Long-Age Observability}
}
$$

or:

$$
\boxed{
\textbf{Thin-Window Amplification}.
}
$$

### Meaning

The scale-weight problem has been solved, but a temporal criticality problem necessarily remains.

$\square$

---

# 39. Paid-side residuals remain

Even if LAO or CRW is proved, the pressure--flux telescope retains:

$$
\boxed{
\sum_kw_k|\mathcal L_k|
}
$$

and:

$$
\boxed{
\sum_kw_k\mathcal W_k^-.
}
$$

No universal finite slow-scale budget for these quantities is proved.

Thus the full Critical Lift still requires a paid-side closure or a further recurrence classification.

---

# 40. Combined-invisible branch

If pressure--flux work is not depletion-effective, the external finite-window hierarchy tests:

- pressure;
- flux;
- positive energy;
- adjoint trace.

A surviving branch must either have non-effective moving-window constants or enter an NS-realizable combined-invisible defect cascade.

This is a more precise target than pressure--flux observability alone.

FCBP does not yet exclude the combined-invisible cascade.

---

# 41. Updated obligations

After FCBP-04:

### Filter endpoint compatibility

$$
\boxed{
\mathrm{SUBSTANTIALLY\ CLOSED}.
}
$$

- full-thickness slow compact filters:
  continuous drift is finite;
- horizon-aligned filters:
  co-moving heat filtering absorbs filter motion into viscosity.

### Scale-weight non-summability

$$
\boxed{
\mathrm{PROVED}.
}
$$

### Horizon temporal compatibility

$$
\boxed{
\mathrm{OPEN}.
}
$$

as:

$$
LAO
\vee
CRW.
$$

### Paid-side closure

$$
\boxed{
\mathrm{OPEN}.
}
$$

### Combined invisible recurrence

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 42. What FCBP-04 corrects

FCBP-03's Slow-Scale Schedule Lift remains mathematically correct.

Its interpretation is refined:

$$
\boxed{
\text{Schedule Lift}
\neq
\text{Horizon Critical Lift}.
}
$$

The missing ingredient is not now filter switching.

It is the relation between:

- slow scale;
- horizon age;
- normalized time thickness;
- observed work density.

---

# 43. Next paper

The next paper should attack temporal criticality and paid-side recurrence directly:

$$
\boxed{
\textbf{
NS-FCBP 05 —
Long-Age Observability,
Thin-Window Renewal-to-Work Bridge,
Backscatter/Leakage Recurrence
and Horizon Critical Lift
}.
}
$$

Primary tasks:

1. compare LAO with known quantitative backward/forward propagation estimates;
2. convert causal fresh-renewal packets into work/energy/model-cone packets;
3. analyze weighted backscatter on slow schedules;
4. seek adjoint or sign-coherent reduction of localization leakage;
5. use the combined pressure--flux--energy--trace hierarchy rather than one detector;
6. determine whether a horizon-aligned non-summable forest budget can finally be made unconditional.

---

# 44. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Filter-Scale Derivative Lemma}
&:\ \mathrm{PROVED},\\
\text{Moving-Filter Coarse NS Equation}
&:\ \mathrm{PROVED},\\
\text{Slow-Schedule Filter-Speed Packing}
&:\ \mathrm{PROVED},\\
\text{Continuous Filter-Drift Packing}
&:\ \mathrm{PROVED},\\
\text{Parabolic Alignment Summability}
&:\ \mathrm{PROVED},\\
\text{Slow Schedule}\Rightarrow\text{fixed horizon alignment}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{Co-Moving Heat-Filter Equation}
&:\ \mathrm{PROVED},\\
\text{Horizon-Aligned Heat-Filter Telescope}
&:\ \mathrm{PROVED},\\
\text{Time-Thickness Summability}
&:\ \mathrm{PROVED},\\
\text{bounded thin-slab work-rate Critical Lift}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{Borderline inverse-thickness compiler}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
LAO
&:\ \mathrm{OPEN},\\
CRW
&:\ \mathrm{OPEN},\\
\text{weighted leakage/backscatter closure}
&:\ \mathrm{OPEN},\\
\text{combined-invisible cascade exclusion}
&:\ \mathrm{OPEN},\\
\text{Critical Lift}
&:\ \mathrm{OPEN},\\
\text{Forest Coercive Budget}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 45. Conclusion

FCBP-04 closes the most concrete endpoint-compatibility problem from FCBP-03.

For smooth compact mollifiers:

$$
\|\partial_\ell S_\ell u\|_2
\lesssim
\|\nabla u\|_2.
$$

On the full-thickness slow schedule, continuous scale-relative filter motion has square-integrable filter speed, so its entire drift work is paid by the finite Leray dissipation budget.

Thus moving filters and the non-summable schedule are compatible.

But that schedule is not uniformly parabolically aligned with the singular horizon.

Indeed fixed horizon alignment for full-parabolic adjacent slabs forces the radii to be summable.

A horizon-aligned alternative exists: use thin adjacent slabs and a co-moving heat-semigroup filter:

$$
s(t)=a(T_\ast-t),
\qquad
0<a<\nu.
$$

The changing filter is then absorbed exactly into an effective viscosity:

$$
\nu-a>0,
$$

and the pressure--flux telescope remains exact at scale-relative horizon resolution.

Yet horizon alignment introduces a new universal cost:

$$
\sum_k
w_k\delta_k
<
\infty.
$$

Hence bounded normalized work rate cannot produce a Critical Lift even when the scale weights themselves are non-summable.

A true horizon obstruction must therefore force inverse-thickness activity or propagate dangerous information across increasingly many local parabolic ages.

The scale problem has become a time problem.

The next frontier is:

$$
\boxed{
\textbf{
Long-Age Observability
\quad\text{or}\quad
Thin-Window Renewal-to-Work Amplification.
}
}
$$

That is FCBP-05.

---

# References

1. R. Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322.
2. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
3. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
4. G. L. Eyink, H. Aluie, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, arXiv:0909.2386.
5. `NS_FCBP_03_SignedWork_SlowScale_Telescoping_v0.1.md`.