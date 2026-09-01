---
title: "Navier–Stokes Coercive Synchronization Program 07: Preloaded Reservoir Transport, Viscous Survival, Replenishment Debt and Core Dilution"
short_title: "NS-CSP 07"
series: "Navier–Stokes Coercive Synchronization Program"
cycle: "II"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style reservoir transport / replenishment synchronization"
epistemic_status: "Proves that the PRELOAD branch from CSP-06 splits into exponentially amplified old-stock survival or a quantitative high-frequency Duhamel replenishment debt. The replenishment debt further splits into strain-vorticity model residual forcing or high-frequency vorticity-parent forcing, providing a partial source-state synchronization theorem. It derives a viscous turnover law for super-parabolic micro-packing and a Type-I core-dilution energy budget. It does NOT exclude exponential preload inflation, dissipation-range replenishment, residual source-state desynchronization, or prove Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Coercive Synchronization Program 07

# Preloaded Reservoir Transport, Viscous Survival, Replenishment Debt and Core Dilution

## 0. Document Positioning

CSP-06 reduced a stale middle-strain event to:

$$
\boxed{
\text{model-cone departure}
\vee
\text{PRELOAD}.
}
$$

The PRELOAD branch means that the strain-gradient capacity needed to support the later middle-strain spike was already present at the half-level Besov escape time:

$$
\tau_t
=
\tau
\left(
\frac{B(t)}2
\right).
$$

CSP-06 further proved that excess preload must live at ultraviolet depth.

The remaining question is:

> Can an ultraviolet preload reservoir simply survive until the later spike without paying any additional dynamical cost?

The answer is:

$$
\boxed{
\textbf{only if its initial amplitude grows exponentially with its viscous age.}
}
$$

Otherwise the later high-frequency state requires a quantitative Duhamel replenishment debt.

---

# 1. Exact strain forcing

Normalize:

$$
\nu=1.
$$

Following Miller, define:

$$
\boxed{
\mathcal R_{SV}
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
}
$$

The exact projected Navier--Stokes strain equation is:

$$
\boxed{
\partial_tS
-
\Delta S
=
\frac12
P_{st}
(
\omega\otimes\omega
)
-
\mathcal R_{SV}.
}
$$

Define:

$$
\boxed{
\mathcal F_S
=
\frac12
P_{st}
(
\omega\otimes\omega
)
-
\mathcal R_{SV}.
}
$$

Hence:

$$
\boxed{
S(t)
=
e^{(t-\tau)\Delta}S(\tau)
+
\int_\tau^t
e^{(t-s)\Delta}
\mathcal F_S(s)\,ds.
}
$$

---

# 2. Middle-strain state requirement

Define:

$$
\boxed{
g(t)
=
\|\lambda_2^+(t)\|_2^2.
}
$$

Let:

$$
E_2
=
\sup_{0<s<T}
\|u(s)\|_2.
$$

CSP-06 proved:

$$
\boxed{
\|S(t)\|_{\dot H^1}
\ge
c
\frac{
g(t)
}{
E_2
}.
}
$$

Thus a later middle-strain spike requires a definite amount of:

$$
\dot H^1
$$

strain capacity.

---

# 3. Low-frequency Hdot1 capacity

For every frequency cutoff:

$$
\lambda=2^J,
$$

Plancherel and the energy bound give:

$$
\boxed{
\|P_{\le J}S(t)\|_{\dot H^1}
\le
C
2^{2J}
E_2.
}
$$

Choose:

$$
J_g(t)
$$

so that:

$$
\boxed{
2^{2J_g(t)}
\asymp
\frac{
g(t)
}{
E_2^2
}
}
$$

with a sufficiently small fixed proportionality constant.

---

# 4. CII-7.1 — Final High-Frequency State Extraction

## Theorem 4.1

For the cutoff:

$$
J_g(t)
$$

of Section 3:

$$
\boxed{
\|P_{\ge J_g(t)}S(t)\|_{\dot H^1}
\ge
c_g
\frac{
g(t)
}{
E_2
}.
}
$$

### Proof

The total:

$$
\dot H^1
$$

norm is at least:

$$
c g/E_2.
$$

By construction the low-frequency piece is at most a sufficiently small fixed fraction of this quantity.

Use orthogonality of the low/high Fourier decomposition. $\square$

---

# 5. Half-level escape data

For a stale PRELOAD event:

$$
t,
$$

let:

$$
\boxed{
\tau_t
=
\tau
\left(
\frac{B(t)}2
\right).
}
$$

Define the elapsed time:

$$
\boxed{
\Delta_t
=
t-\tau_t.
}
$$

Define the preload amplitude ratio:

$$
\boxed{
\mathfrak P_{\rm pre}(t)
=
\frac{
E_2
\|S(\tau_t)\|_{\dot H^1}
}{
g(t)
}.
}
$$

The PRELOAD branch of CSP-06 implies:

$$
\mathfrak P_{\rm pre}
$$

is bounded below by a positive universal constant.

---

# 6. Viscous preload age

Define:

$$
\boxed{
\mathfrak V_{\rm pre}(t)
=
2^{2J_g(t)}
\Delta_t.
}
$$

By Section 3:

$$
\boxed{
\mathfrak V_{\rm pre}(t)
\asymp
\frac{
g(t)
}{
E_2^2
}
\Delta_t.
}
$$

This is dimensionless under Navier--Stokes scaling.

---

# 7. High-frequency heat decay

For a high-frequency tail:

$$
P_{\ge J},
$$

the heat semigroup satisfies:

$$
\boxed{
\|
e^{\Delta\Delta}
P_{\ge J}f
\|_{\dot H^1}
\le
C_h
e^{-c_h2^{2J}\Delta}
\|
P_{\ge J}f
\|_{\dot H^1}.
}
$$

Therefore the old preload contribution at time:

$$
t
$$

obeys:

$$
\boxed{
\|
e^{\Delta_t\Delta}
P_{\ge J_g}S(\tau_t)
\|_{\dot H^1}
\le
C_h
\mathfrak P_{\rm pre}(t)
e^{-c_h\mathfrak V_{\rm pre}(t)}
\frac{
g(t)
}{
E_2
}.
}
$$

---

# 8. Old-stock survival factor

Define:

$$
\boxed{
\Xi_{\rm old}(t)
=
\mathfrak P_{\rm pre}(t)
e^{-c_h\mathfrak V_{\rm pre}(t)}.
}
$$

If:

$$
\Xi_{\rm old}
$$

is small,

the initial preload cannot account for the final high-frequency state extracted in Theorem 4.1.

---

# 9. Weighted replenishment source

Define:

$$
\boxed{
\mathfrak D_{\rm src}(t)
=
\int_{\tau_t}^t
e^{-c_h2^{2J_g(t)}(t-s)}
\|
P_{\ge J_g(t)}
\mathcal F_S(s)
\|_{\dot H^1}
\,ds.
}
$$

This is the heat-taxed high-frequency source contribution.

---

# 10. CII-7.2 — Preload Survival / Replenishment Dichotomy

## Theorem 10.1

There exist universal constants:

$$
c_\ast,C_\ast>0
$$

such that every sufficiently high PRELOAD event satisfies at least one of:

### OLD-SURVIVE

$$
\boxed{
\mathfrak P_{\rm pre}(t)
\ge
c_\ast
\exp
\left(
c_h
\mathfrak V_{\rm pre}(t)
\right).
}
$$

### REPLENISH

$$
\boxed{
\mathfrak D_{\rm src}(t)
\ge
C_\ast
\frac{
g(t)
}{
E_2
}.
}
$$

### Proof

Apply:

$$
P_{\ge J_g}
$$

to the exact Duhamel formula.

Theorem 4.1 gives a lower bound for the final tail.

Section 7 bounds the old-stock term.

The heat estimate bounds the Duhamel term above by:

$$
\mathfrak D_{\rm src}.
$$

If the old term supplies at least a fixed fraction of the final lower bound, OLD-SURVIVE holds.

Otherwise the Duhamel term must supply the missing fixed fraction, giving REPLENISH. $\square$

---

# 11. Exponential preload inflation

OLD-SURVIVE means:

$$
\boxed{
\text{a reservoir surviving many viscous ages must have been exponentially larger at the escape time.}
}
$$

In particular, if:

$$
\mathfrak V_{\rm pre}(t)\to\infty
$$

while:

$$
\log
\mathfrak P_{\rm pre}(t)
=
o(
\mathfrak V_{\rm pre}(t)
),
$$

then REPLENISH is forced.

Thus a polynomially large preload cannot survive arbitrarily many viscous ages.

---

# 12. Source decomposition

Since:

$$
\mathcal F_S
=
\frac12
P_{st}
(
\omega\otimes\omega
)
-
\mathcal R_{SV},
$$

the source debt satisfies:

$$
\mathfrak D_{\rm src}
\le
\frac12
\mathfrak D_\omega
+
\mathfrak D_{SV}^{src},
$$

where:

$$
\boxed{
\mathfrak D_\omega(t)
=
\int_{\tau_t}^t
e^{-c_h2^{2J_g}(t-s)}
\|
P_{\ge J_g}
P_{st}
(
\omega\otimes\omega
)(s)
\|_{\dot H^1}
ds,
}
$$

and:

$$
\boxed{
\mathfrak D_{SV}^{src}(t)
=
\int_{\tau_t}^t
e^{-c_h2^{2J_g}(t-s)}
\|
P_{\ge J_g}
\mathcal R_{SV}(s)
\|_{\dot H^1}
ds.
}
$$

---

# 13. CII-7.3 — Replenishment Channel Split

## Theorem 13.1

On the REPLENISH branch, at least one of:

### SV-REP

$$
\boxed{
\mathfrak D_{SV}^{src}(t)
\ge
c
\frac{
g(t)
}{
E_2
};
}
$$

### VORT-REP

$$
\boxed{
\mathfrak D_{\omega}(t)
\ge
c
\frac{
g(t)
}{
E_2
}
}
$$

must hold.

$\square$

---

# 14. Meaning of SV-REP

SV-REP is not merely a large unsigned nonlinear term.

It is direct high-frequency forcing through:

$$
\mathcal R_{SV},
$$

the same residual measuring departure from Miller's globally regular strain--vorticity model.

Thus one PRELOAD escape channel is reabsorbed into:

$$
\boxed{
\text{model-cone replenishment}.
}
$$

---

# 15. Dyadic parent decomposition of vorticity forcing

Write:

$$
\omega
=
\sum_p
\omega_p.
$$

Then:

$$
P_{\ge J}
P_{st}
(
\omega\otimes\omega
)
=
\sum_{p,q}
P_{\ge J}
P_{st}
(
\omega_p\otimes\omega_q
).
$$

Standard Fourier support gives:

$$
\boxed{
P_{\ge J}
P_{st}
(
\omega_p\otimes\omega_q
)
\neq0
\Longrightarrow
\max\{p,q\}
\ge
J-C_{\rm LP}.
}
$$

Thus a high-frequency output cannot be produced entirely by far-lower vorticity parents.

---

# 16. CII-7.4 — High-Parent Source-State Synchronization

## Theorem 16.1

On VORT-REP, the replenishment debt is entirely supported on quadratic interactions having at least one vorticity parent shell:

$$
\boxed{
p\ge
J_g-C_{\rm LP}
\quad
\text{or}
\quad
q\ge
J_g-C_{\rm LP}.
}
$$

Therefore the final high-frequency strain state is synchronized, in the Duhamel source sense, with genuine high-frequency vorticity parent state during:

$$
[\tau_t,t].
$$

### Safety note

This theorem does not select a single parent shell with fixed share unless an additional finite-multiplicity/atomization condition is imposed.

It is a source-state support synchronization theorem, not a finite-carrier theorem.

---

# 17. Residual source-state defect

The old:

$$
D_{\rm SRCSTATE}
$$

is therefore reduced.

For high-frequency PRELOAD replenishment, actual parent-state participation is unavoidable.

The residual source-state problem is now narrower:

$$
\boxed{
\text{parent multiplicity / cancellation}
}
$$

or the older resonant high-high-to-low source/state desynchronization from CSP-03.

---

# 18. Survival threshold frequency

For an interval length:

$$
\Delta>0,
$$

define the viscous survival frequency:

$$
\boxed{
\lambda_{\rm surv}
=
\Delta^{-1/2}.
}
$$

A shell:

$$
\lambda_j=2^j
$$

has viscous age:

$$
\boxed{
\mathfrak V_j
=
\lambda_j^2
\Delta.
}
$$

Thus:

$$
\lambda_j
\gg
\lambda_{\rm surv}
$$

means old stock is exponentially heat-suppressed.

---

# 19. Relation to the Bradshaw--Grujic upper scale

For a stale gap time:

$$
t,
$$

CSP-05's intrinsic Besov scale is:

$$
B(t)^{-4}.
$$

If:

$$
\Delta_t
=
H
B(t)^{-4},
$$

then:

$$
\boxed{
\lambda_{\rm surv}
=
B(t)^2
H^{-1/2}.
}
$$

CSP-04 gives:

$$
2^{J_{\rm high}(t)}
\asymp
B(t)^2.
$$

Hence large stale lag:

$$
H\gg1
$$

pushes the old-stock survival threshold **below** the moving-window upper endpoint by:

$$
\boxed{
\frac12
\log_2H
}
$$

dyadic scales.

Thus progressively more of the relevant upper-frequency reservoir requires replenishment as stale lag grows.

---

# 20. Dissipation-range residence

CSP-04 proved:

$$
Q(t)
\le
J_{\rm high}(t)+O(1),
$$

where:

$$
Q(t)
$$

is the Cheskidov--Shvydkoy dissipation-wavenumber index.

Therefore preload lying far above:

$$
J_{\rm high}
$$

is also deep in the viscosity-dominated range.

Theorem 10.1 now adds:

> deep dissipation-range preload cannot remain an unchanged old reservoir for many viscous ages unless its initial amplitude is exponentially inflated.

If it remains dynamically relevant, it must turn over through REPLENISH.

---

# 21. Dissipation-range replenishment defect

Define:

$$
\boxed{
D_{\rm DISSREP}
}
$$

as the branch where the required REPLENISH source debt is concentrated at scales lying persistently above:

$$
Q(s)+C
$$

during the relevant source window.

Cheskidov--Shvydkoy theory shows nonlinear terms in this region are viscosity-controlled in the standard energy estimate.

However this does not prove:

$$
D_{\rm DISSREP}
$$

impossible.

It is a quantitative tension, not yet an obstruction.

---

# 22. Super-parabolic micro-packing turnover

CSP-02 defined the Type-I micro-packing parameter:

$$
\Theta_I
=
2^j
R_I.
$$

A parabolic core timescale is:

$$
\Delta_I
\asymp
R_I^2.
$$

Therefore the viscous age of shell:

$$
j
$$

over one parabolic core time is:

$$
\boxed{
2^{2j}\Delta_I
\asymp
\Theta_I^2.
}
$$

---

# 23. CII-7.5 — Micro-Packing Turnover Corollary

## Corollary 23.1

Suppose a Type-I core shell with:

$$
\Theta_I\gg1
$$

is required to remain dynamically relevant across a time interval comparable to:

$$
R_I^2.
$$

Then its old-stock contribution is suppressed by:

$$
\boxed{
e^{-c\Theta_I^2}.
}
$$

Hence persistent relevance requires either:

$$
\boxed{
\text{initial shell amplitude inflation of order }e^{c\Theta_I^2}
}
$$

or a nontrivial Duhamel replenishment source.

Thus super-parabolic micro-packing is also a fast-turnover/replenishment geometry.

---

# 24. Type-I core dilution setup

Assume the Barker--Prange Type-I setting.

Let:

$$
R_I(t)
\asymp_M
(T-t)^{1/2}
$$

be the singular-core radius.

Suppose a selected local core shell:

$$
j_c(t)
$$

satisfies on a time set:

$$
E_c
$$

the fixed absolute local enstrophy lower bound:

$$
\boxed{
\|\omega_{j_c(t)}(t)\|_{
L^2(B_{R_I(t)})
}^2
\ge
\theta
\frac{
M^2
}{
R_I(t)
}
}
$$

for fixed:

$$
\theta>0.
$$

---

# 25. Global dilution ratio

Define:

$$
\boxed{
\beta_c(t)
=
\frac{
\|\omega_{j_c(t)}(t)\|_2^2
}{
\|\omega(t)\|_2^2
}.
}
$$

Then:

$$
0<\beta_c(t)\le1.
$$

Small:

$$
\beta_c
$$

means a locally intense singular-core shell is globally diluted by much larger enstrophy elsewhere.

---

# 26. CII-7.6 — Core-Dilution Energy Budget

## Theorem 26.1

On:

$$
E_c,
$$

$$
\boxed{
\|\omega(t)\|_2^2
\ge
\theta
\frac{
M^2
}{
\beta_c(t)
R_I(t)
}.
}
$$

Consequently the energy inequality implies:

$$
\boxed{
\int_{E_c}
\frac{
dt
}{
\beta_c(t)
R_I(t)
}
\le
C
\frac{
\|u_0\|_2^2
}{
\theta M^2
}.
}
$$

### Proof

The global shell norm dominates its local core norm:

$$
\|\omega_{j_c}\|_2^2
\ge
\theta M^2/R_I.
$$

By definition:

$$
\|\omega\|_2^2
=
\beta_c^{-1}
\|\omega_{j_c}\|_2^2.
$$

Integrate and use:

$$
\int_0^T
\|\omega(t)\|_2^2dt
\le
C\|u_0\|_2^2.
$$

$\square$

---

# 27. Logarithmic dilution corollary

Since:

$$
R_I(t)
\asymp_M
(T-t)^{1/2},
$$

Theorem 26.1 gives:

$$
\boxed{
\int_{E_c}
\frac{
dt
}{
\beta_c(t)
(T-t)^{1/2}
}
<
\infty.
}
$$

In particular, on the subregion where:

$$
\boxed{
\beta_c(t)
\le
C
(T-t)^{1/2},
}
$$

one must have finite logarithmic time measure:

$$
\boxed{
\int
\frac{
dt
}{
T-t
}
<
\infty.
}
$$

Thus extreme core dilution cannot persist on a terminal set of infinite logarithmic measure.

---

# 28. Meaning for D-DILUTE

CSP-06 introduced:

$$
D_{\rm DILUTE}.
$$

Theorem 26.1 does not remove it.

It converts it into a weighted temporal sparsity condition.

To maintain fixed absolute singular-core shell mass while its global share collapses, the solution must pay global enstrophy inflation.

Energy limits how persistently this can happen.

---

# 29. PRELOAD transport alternative

Combining Theorems 10.1 and 13.1:

$$
\boxed{
\text{PRELOAD}
\Longrightarrow
\text{EXP-PRELOAD}
\vee
\text{SV-REP}
\vee
\text{VORT-REP}.
}
$$

where:

### EXP-PRELOAD

$$
\boxed{
\mathfrak P_{\rm pre}
\gtrsim
e^{c\mathfrak V_{\rm pre}};
}
$$

### SV-REP

high-frequency source replenishment is supplied by:

$$
\mathcal R_{SV};
$$

### VORT-REP

high-frequency source replenishment is supplied by:

$$
P_{st}(\omega\otimes\omega)
$$

and therefore requires a high-frequency vorticity parent state.

---

# 30. What remains of the old static reservoir picture?

A reservoir that remains at high frequency for many viscous ages without source activity must be exponentially oversized at the earlier escape time.

Therefore:

$$
\boxed{
\text{PRELOAD}
}
$$

should no longer be interpreted as:

> old stock simply waits.

The actual possibilities are:

1. exponentially overprepared stock;
2. repeated nonlinear/model-cone replenishment;
3. rapid turnover of micro-packed state.

---

# 31. Relation to Cheskidov--Dai shell-time criteria

Cheskidov--Dai prove regularity if sufficiently high vorticity shells have small:

$$
L_t^1L_x^\infty
$$

activity on appropriate terminal intervals.

Therefore the VORT-REP branch, if it persists toward arbitrarily high frequencies, must coexist with recurrent non-small time-integrated high-shell activity.

This is compatible with the replenishment interpretation.

It does not by itself exclude VORT-REP.

---

# 32. Partial source-state closure

The original source/state defect asked whether a source ledger could be dynamically important while its parent states were absent from the relevant state geometry.

For PRELOAD replenishment at high output frequency, Theorem 16.1 answers part of this question:

$$
\boxed{
\text{high output replenishment}
\Longrightarrow
\text{high parent vorticity state participation}
}
$$

in the quadratic-vorticity branch.

What remains open is:

- finite parent-shell concentration;
- cancellation;
- resonant high-high-to-low state synchronization.

---

# 33. New transport guards

Add:

### $G_{\rm VISAGE}$

Every preloaded frequency reservoir must record its viscous age:

$$
2^{2J}\Delta t.
$$

### $G_{\rm OLDSURV}$

Old-stock survival through many viscous ages requires exponential amplitude inflation.

### $G_{\rm REPLEN}$

If old stock cannot survive, preserve the weighted Duhamel replenishment debt.

### $G_{\rm REPSPLIT}$

Replenishment must be split into:

$$
\mathcal R_{SV}
$$

and:

$$
P_{st}(\omega\otimes\omega)
$$

channels.

### $G_{\rm HIGHPAR}$

High-frequency vorticity replenishment must preserve at least one high-frequency parent state.

### $G_{\rm DILBUD}$

Core dilution must preserve the weighted global-enstrophy budget.

---

# 34. Cycle-II frontier compression

Before CSP-07 the principal residuals were:

$$
\text{PRELOAD},
\quad
D_{\rm INDEX},
\quad
D_{\rm DILUTE},
\quad
D_{\rm SRCSTATE},
\quad
D_{I,\rm micro}.
$$

After CSP-07:

$$
\boxed{
\text{PRELOAD}
}
$$

is no longer primitive.

It becomes:

$$
\boxed{
\text{EXP-PRELOAD}
\vee
\text{SV-REP}
\vee
\text{VORT-REP}.
}
$$

Super-parabolic micro-packing is absorbed into the same turnover/replenishment framework.

Core dilution is restricted by an energy-weighted temporal budget.

High-output source/state desynchronization is partially closed by high-parent Fourier support.

The remaining principal defects are now:

$$
\boxed{
\text{EXP-PRELOAD},
\quad
D_{\rm DISSREP},
\quad
D_{\rm INDEX},
\quad
D_{\rm DILUTE},
\quad
D_{\rm SRCSTATE}^{res}.
}
$$

---

# 35. What would close EXP-PRELOAD?

EXP-PRELOAD requires:

$$
\mathfrak P_{\rm pre}
\gtrsim
e^{c\mathfrak V_{\rm pre}}.
$$

A closure theorem could come from any upper bound of the form:

$$
\boxed{
\log
\mathfrak P_{\rm pre}
=
o(
\mathfrak V_{\rm pre}
)
}
$$

along dangerous middle-strain spikes.

No such universal estimate is currently proved.

---

# 36. What would close D-DISSREP?

A closure theorem would need to show that a high-frequency replenishment debt remaining persistently above the dissipation wavenumber is absorbed by viscosity strongly enough to prevent the required final state.

Cheskidov--Shvydkoy provide the relevant high-mode viscosity domination framework,

but CSP-07 does not derive the needed forcing-level coercive inequality.

Thus:

$$
\boxed{
D_{\rm DISSREP}
}
$$

remains OPEN.

---

# 37. What would close core dilution?

Theorem 26.1 shows extreme dilution cannot occupy too much weighted time.

A complete closure would need to combine this budget with the known temporal density/backward persistence of Type-I singular-core concentration.

This suggests an interface with Barker--Prange backward concentration propagation.

It is not completed here.

---

# 38. Candidate Dynamical Cover v2 pre-stage

The current Cycle-II architecture now has four genuine mechanisms:

1. model-cone residual departure/replenishment;
2. exponentially inflated old-stock survival;
3. high-parent nonlinear replenishment in the relevant/dissipation range;
4. local/global dilution/index mismatch.

This is substantially smaller than the original RFP tax frontier.

The next paper should consolidate these mechanisms rather than introduce new bookkeeping variables.

---

# 39. Next paper

$$
\boxed{
\textbf{
NS-CSP 08 —
Unified Reservoir/Alignment Cover,
Exponential Preload Audit,
Dissipation-Range Replenishment
and Cycle-II Closure
}.
}
$$

Primary tasks:

1. audit whether EXP-PRELOAD is compatible with existing energy/critical-action budgets;
2. combine dissipation-range viscosity domination with the replenishment debt;
3. combine Barker--Prange backward core persistence with the dilution budget;
4. close or isolate residual shell-index/source-state mismatch;
5. construct Candidate Dynamical Cover v2;
6. decide whether Cycle II closes the Coercive Synchronization Problem or must end with a smaller explicit residual core.

---

# 40. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{final high-frequency state extraction}
&:\ \mathrm{PROVED},\\
\text{viscous preload age}
&:\ \mathrm{DEFINED/SCALE\ AUDITED},\\
\text{old-stock heat survival bound}
&:\ \mathrm{PROVED},\\
\text{preload survival/replenishment dichotomy}
&:\ \mathrm{PROVED},\\
\text{replenishment channel split}
&:\ \mathrm{PROVED},\\
\text{high-parent source-state synchronization}
&:\ \mathrm{PROVED},\\
\text{micro-packing turnover}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{Type-I core-dilution energy budget}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{EXP-PRELOAD exclusion}
&:\ \mathrm{OPEN},\\
\text{dissipation-range replenishment exclusion}
&:\ \mathrm{OPEN},\\
\text{core dilution closure}
&:\ \mathrm{OPEN},\\
\text{resonant source/state closure}
&:\ \mathrm{OPEN},\\
\text{Coercive Synchronization Problem}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 41. Conclusion

CSP-07 removes the last static interpretation of PRELOAD.

A later middle-strain spike forces a high-frequency:

$$
\dot H^1
$$

state at a scale:

$$
2^{2J_g}
\asymp
g/E_2^2.
$$

Across the stale interval, the old preload contribution is exponentially taxed by:

$$
e^{-c\mathfrak V_{\rm pre}},
\qquad
\mathfrak V_{\rm pre}
=
2^{2J_g}(t-\tau_t).
$$

Therefore the state can persist only through:

$$
\boxed{
\text{exponentially inflated preload}
}
$$

or:

$$
\boxed{
\text{actual Duhamel replenishment}.
}
$$

The replenishment itself must come from either:

$$
\boxed{
\mathcal R_{SV}
}
$$

model-cone forcing,

or:

$$
\boxed{
P_{st}(\omega\otimes\omega)
}
$$

with genuine high-frequency vorticity parent participation.

Super-parabolic micro-packing has the same structure because its viscous age over one parabolic core time is:

$$
\Theta_I^2.
$$

Finally, Type-I core dilution is not free:

$$
\boxed{
\int
\frac{
dt
}{
\beta_c(t)R_I(t)
}
<
\infty.
}
$$

Thus a locally intense shell cannot become globally invisible too persistently without violating the energy budget.

The Cycle-II frontier has now become a small reservoir-transport problem rather than a large family of unrelated escapes.

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691v2.
2. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263–273; arXiv:1102.1944v2.
3. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611v6.
4. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717v3.
5. `NS_CSP_02_SpatialAtom_TypeI_CoreExtraction_ParabolicPacking_v0.1.md`.
6. `NS_CSP_04_MovingWindow_DissipationWavenumber_EscapeIntervals_v0.1.md`.
7. `NS_CSP_05_EscapeTime_TemporalGap_Rigidity_v0.1.md`.
8. `NS_CSP_06_StaleFloor_ModelCone_CoreAlignment_v0.1.md`.