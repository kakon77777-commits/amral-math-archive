---
title: "Navier–Stokes Impulsive Defect Recurrence Program 01: Impulse Persistence, Trace Thickening, Temporal Action Packing, Moving-Window Visibility and Recurrent Defect Normal Forms"
short_title: "NS-IDRP 01"
series: "Navier–Stokes Impulsive Defect Recurrence Program"
cycle: "IX"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Temporal persistence foundation / burst-packing audit / Type-I thickening module"
epistemic_status: "Launches the Impulsive Defect Recurrence Program from the Cycle-VIII normal form K_IDR. Imports Barker-Prange's Type-I concentration theorem and derives a parabolic-thick critical L3 spacetime packet on every late horizon slab in the strong L3 Type-I branch. Proves an abstract trace persistence-or-variation theorem and applies it to localized filtered-enstrophy balances: a selected-time filtered atom either persists or pays a fixed total-variation/mechanism debt. Proves the universal energy-class temporal regularity u_t in L_t^{4/3} H_x^{-1}. For dyadic velocity-shell atoms, proves a spectral impulse-action lower bound: if a local scale-r critical kinetic atom of strength a drops by a fixed factor within physical time tau=delta r^2, then the H^{-1} temporal action costs at least c a^{2/3} r^{4/3} delta^{-1/3}. Pairwise-disjoint impulses therefore satisfy a global burst-packing inequality. This yields an energy-class persistence floor: infinitely many disjoint atoms cannot all disappear on times tau <= c a^2 r^6. It also proves a no-go: the generic energy-class modulus is far too weak to force parabolic r^2 thickening; geometric scale sequences can have much shorter normalized persistence while keeping the temporal-action budget summable. Applying the result to the logarithmic FAR atoms from DCRP-04 shows that energy-class regularity alone does not upgrade the selected-time logarithmic atom floor to a fixed moving-window packet. The remaining bridge is therefore structural: causal/source impulses, filtered ledger variation, or combined moving-window observability must convert rapid trace loss into a scale-critical visible burst. No Impulsive Diffuse Recurrence exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Impulsive Defect Recurrence Program 01

# Impulse Persistence, Trace Thickening, Temporal Action Packing, Moving-Window Visibility and Recurrent Defect Normal Forms

## 0. Program objective

DCRP Cycle VIII ended with the surviving normal form:

$$
\boxed{
\mathcal K_{\rm IDR}
}
$$

— Impulsive Diffuse Recurrence.

Its branches were:

- asymptotically propagated high-shell impulses;
- super-height fresh-source bursts;
- logarithmically weak FAR atoms;
- recurrent commutator defect work/microstructure;
- combined-invisible WORK/RES recurrence.

The central new question is temporal:

> can every positive carrier exist only at isolated times, so that every spacetime budget remains summable?

IDRP begins by separating:

$$
\boxed{
\text{PERSISTENCE}
\vee
\text{BURST DEBT}.
}
$$

---

# 1. External Type-I concentration module

Barker--Prange prove a concentration theorem near a possible Type-I blow-up.

Under their Type-I hypotheses, if:

$$
(0,T_\ast)
$$

is singular, then for late times:

$$
\boxed{
\|u(\cdot,t)\|_{L^3(B_{R(t)}(0))}
\ge
\gamma_{\rm univ},
}
$$

where:

$$
\boxed{
R(t)
\le
C
\sqrt{
T_\ast-t
}.
}
$$

Their framework also treats critical Lorentz/Besov variants.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED}.
}
$$

---

# 2. Horizon slab

Fix small:

$$
r>0.
$$

Define:

$$
\boxed{
J_r
=
[
T_\ast-2r^2,
T_\ast-r^2
].
}
$$

For:

$$
t\in J_r,
$$

$$
R(t)
\le
C\sqrt2\,r.
$$

Therefore the external concentration theorem gives:

$$
\boxed{
\int_{
B_{C\sqrt2\,r}
}
|u(x,t)|^3dx
\ge
\gamma_{\rm univ}^3.
}
$$

for every admissible late:

$$
t\in J_r.
$$

---

# 3. CIV/IX-1.1 — Type-I Parabolic Thickening Corollary

## Theorem 3.1

Under the external Barker--Prange Type-I concentration hypotheses:

$$
\boxed{
r^{-2}
\int_{J_r}
\int_{
B_{C\sqrt2\,r}
}
|u(x,t)|^3dxdt
\ge
\gamma_{\rm univ}^3.
}
$$

Thus every sufficiently small horizon scale carries a full normalized parabolic-thickness critical:

$$
L^3
$$

spacetime packet.

### Proof

The pointwise-in-time lower bound holds for every time in:

$$
J_r,
$$

whose length is:

$$
r^2.
$$

Integrate in time and divide by:

$$
r^2.
$$

$\square$

---

# 4. Meaning for IDRP

In this strong Type-I critical branch:

$$
\boxed{
\text{selected-time state impulse}
}
$$

is not the correct normal form.

The critical state concentration is already persistent on a full:

$$
O(r^2)
$$

horizon window.

Thus the hardest impulse-persistence problem lies in:

- non-Type-I branches;
- weak trace carriers not covered by the strong:
  $$
  L^3
  $$
  packet;
- filtered/commutator/WORK residual carriers.

---

# 5. Abstract trace observable

Let:

$$
A:
[t_0,t_0+\tau]
\to
[0,\infty)
$$

be absolutely continuous.

Assume:

$$
\boxed{
A(t_0)\ge a>0.
}
$$

Define total variation:

$$
\boxed{
\operatorname{Var}_I(A)
=
\int_I
|A'(t)|dt.
}
$$

---

# 6. CIV/IX-1.2 — Trace Persistence-or-Variation

## Theorem 6.1

Exactly one of the following broad alternatives holds.

### persistence

$$
\boxed{
A(t)\ge a/2
\qquad
\forall t\in I;
}
$$

### variation debt

$$
\boxed{
\operatorname{Var}_I(A)
\ge
a/2.
}
$$

### Proof

If persistence fails, choose:

$$
t_1
$$

with:

$$
A(t_1)<a/2.
$$

Absolute continuity gives:

$$
\operatorname{Var}_I(A)
\ge
|A(t_1)-A(t_0)|
>
a/2.
$$

$\square$

---

# 7. Persistent trace gives a spacetime packet

Suppose:

$$
A_r(t)
=
r
\int_Q
|\Omega_r(x,t)|^2dx,
$$

where:

$$
Q
$$

is an:

$$
r
$$

scale cell.

If:

$$
A_r(t)\ge a/2
$$

for an interval of length:

$$
\tau=\delta r^2,
$$

then:

$$
\boxed{
r^{-1}
\int_I
\int_Q
|\Omega_r|^2dxdt
\ge
\frac{
a\delta
}{
2
}.
}
$$

This is a scale-invariant spacetime enstrophy packet.

---

# 8. Filtered enstrophy ledger

The external filtered-vorticity theory supplies a localized filtered-enstrophy balance of schematic exact form:

$$
\boxed{
A_r'(t)
+
D_r(t)
=
V_r^{near}(t)
+
V_r^{far}(t)
+
C_r^{com}(t)
+
L_r(t).
}
$$

The terms denote:

- filtered diffusion;
- near-field stretching;
- far-field strain;
- commutator forcing;
- localization residual.

### Status

$$
\boxed{
\mathrm{EXTERNAL\ IDENTITY/FRAMEWORK}.
}
$$

---

# 9. Mechanism variation action

Define:

$$
\boxed{
\mathfrak B_r(I)
=
\int_I
\left[
D_r
+
|V_r^{near}|
+
|V_r^{far}|
+
|C_r^{com}|
+
|L_r|
\right]dt.
}
$$

Then:

$$
\boxed{
\operatorname{Var}_I(A_r)
\le
\mathfrak B_r(I).
}
$$

---

# 10. CIV/IX-1.3 — Filtered Trace Thickening-or-Burst

## Theorem 10.1

If:

$$
A_r(t_0)\ge a,
$$

then on every chosen forward interval:

$$
I=[t_0,t_0+\tau]
$$

either:

$$
\boxed{
A_r(t)\ge a/2
\quad
\forall t\in I,
}
$$

or:

$$
\boxed{
\mathfrak B_r(I)
\ge
a/2.
}
$$

### Meaning

A filtered selected-time atom can disappear rapidly only by paying a fixed absolute mechanism-variation debt.

$\square$

---

# 11. Variation-budget barrier

Theorem 10.1 does not close the impulse problem.

The global energy inequality controls signed/net budgets and selected positive actions.

It does not give a universal finite total-variation bound for:

$$
\mathfrak B_r
$$

across infinitely many scales.

This is the temporal analogue of the earlier backscatter total-variation no-go.

Therefore:

$$
\boxed{
\text{trace variation debt}
}
$$

must be routed into separately controlled mechanism channels before it becomes coercive.

---

# 12. Universal temporal regularity of velocity

For a Leray--Hopf energy-class solution on:

$$
[0,T],
$$

$$
\partial_tu
=
\nu\Delta u
-
\mathbb P
\nabla\cdot
(
u\otimes u
).
$$

The viscous term obeys:

$$
\boxed{
\|\Delta u\|_{\dot H^{-1}}
\le
C
\|\nabla u\|_2.
}
$$

The nonlinear term obeys:

$$
\boxed{
\|
\mathbb P
\nabla\cdot
(
u\otimes u
)
\|_{\dot H^{-1}}
\le
C
\|u\|_4^2.
}
$$

---

# 13. Energy interpolation

In three dimensions:

$$
\boxed{
\|u\|_4
\le
C
\|u\|_2^{1/4}
\|\nabla u\|_2^{3/4}.
}
$$

Hence:

$$
\boxed{
\|u\|_4^{8/3}
\le
C
\|u\|_2^{2/3}
\|\nabla u\|_2^2.
}
$$

The right-hand side is integrable in time by finite energy.

---

# 14. CIV/IX-1.4 — Universal Temporal Action

## Theorem 14.1

Every finite-energy Leray--Hopf solution satisfies:

$$
\boxed{
\int_0^T
\|
\partial_tu(t)
\|_{\dot H^{-1}}^{4/3}
dt
<
\infty.
}
$$

### Proof

Use:

$$
(a+b)^{4/3}
\le
C
(
a^{4/3}+b^{4/3}
).
$$

For viscosity:

$$
\int_0^T
\|\nabla u\|_2^{4/3}dt
<
\infty
$$

by Hölder and:

$$
\nabla u\in L_t^2L_x^2.
$$

For the nonlinearity, use Section 13 and:

$$
\sup_t
\|u(t)\|_2<\infty.
$$

$\square$

---

# 15. Dyadic shell

Let:

$$
u_k=P_ku
$$

be supported in an annulus:

$$
|\xi|
\asymp
r^{-1},
\qquad
r=2^{-k}.
$$

Let:

$$
Q
$$

be a fixed spatial cell.

Define the local critical kinetic atom:

$$
\boxed{
\mathcal A_{k,Q}(t)
=
r^{-1}
\int_Q
|u_k(x,t)|^2dx.
}
$$

---

# 16. Spectral norm equivalence

For every band-limited:

$$
g
$$

with frequency:

$$
|\xi|\asymp r^{-1},
$$

$$
\boxed{
\|g\|_{\dot H^{-1}}
\ge
c
r
\|g\|_2.
}
$$

---

# 17. Atom disappearance

Assume:

$$
\boxed{
\mathcal A_{k,Q}(t_0)
\ge
a,
}
$$

while at:

$$
t_1=t_0+\tau
$$

$$
\boxed{
\mathcal A_{k,Q}(t_1)
\le
a/4.
}
$$

Then:

$$
\|u_k(t_0)\|_{L^2(Q)}
\ge
\sqrt{
ar
},
$$

and:

$$
\|u_k(t_1)\|_{L^2(Q)}
\le
\frac12
\sqrt{
ar
}.
$$

Thus:

$$
\boxed{
\|
u_k(t_1)-u_k(t_0)
\|_2
\ge
\frac12
\sqrt{
ar
}.
}
$$

---

# 18. CIV/IX-1.5 — Spectral Impulse Action Lower Bound

## Theorem 18.1

Under Sections 15--17:

$$
\boxed{
\int_{t_0}^{t_1}
\|
\partial_tu_k
\|_{\dot H^{-1}}^{4/3}
dt
\ge
c
a^{2/3}
r^2
\tau^{-1/3}.
}
$$

Writing:

$$
\boxed{
\tau
=
\delta r^2,
}
$$

this becomes:

$$
\boxed{
r^{-4/3}
\int_{t_0}^{t_1}
\|
\partial_tu_k
\|_{\dot H^{-1}}^{4/3}
dt
\ge
c
a^{2/3}
\delta^{-1/3}.
}
$$

### Proof

By Section 16:

$$
\|
u_k(t_1)-u_k(t_0)
\|_{\dot H^{-1}}
\ge
c
r
\sqrt{
ar
}
=
c
a^{1/2}
r^{3/2}.
$$

The fundamental theorem in:

$$
\dot H^{-1}
$$

gives:

$$
c
a^{1/2}
r^{3/2}
\le
\int_{t_0}^{t_1}
\|
\partial_tu_k
\|_{\dot H^{-1}}dt.
$$

By Hölder:

$$
\int_I
b(t)dt
\le
\tau^{1/4}
\left(
\int_I
b(t)^{4/3}dt
\right)^{3/4}.
$$

Rearrange.

$\square$

---

# 19. Interpretation

Rapid disappearance of a scale-critical spectral atom has a quantitative temporal-action cost.

The cost grows like:

$$
\boxed{
\delta^{-1/3}
}
$$

in normalized time.

This is the first universal burst-packing mechanism in IDRP.

---

# 20. Pairwise-disjoint impulses

Let:

$$
I_n
$$

be pairwise-disjoint atom-disappearance intervals.

Let:

$$
r_n,
\quad
a_n,
\quad
\delta_n
$$

be their scales, atom strengths, and normalized durations.

Since:

$$
P_{k_n}
$$

is bounded on:

$$
\dot H^{-1},
$$

and the time intervals are disjoint:

$$
\sum_n
\int_{I_n}
\|
\partial_tu_{k_n}
\|_{\dot H^{-1}}^{4/3}dt
\le
C
\int_0^T
\|
\partial_tu
\|_{\dot H^{-1}}^{4/3}dt.
$$

---

# 21. CIV/IX-1.6 — Temporal Burst Packing

## Theorem 21.1

For pairwise-disjoint spectral atom disappearance intervals:

$$
\boxed{
\sum_n
a_n^{2/3}
r_n^{4/3}
\delta_n^{-1/3}
<
\infty.
}
$$

More quantitatively:

$$
\boxed{
\sum_n
a_n^{2/3}
r_n^{4/3}
\delta_n^{-1/3}
\le
C
\int_0^T
\|
\partial_tu
\|_{\dot H^{-1}}^{4/3}dt.
}
$$

$\square$

---

# 22. Energy-class persistence floor

Suppose infinitely many disjoint atoms all disappear within:

$$
\boxed{
\delta_n
\le
c_0
a_n^2
r_n^4.
}
$$

Then every summand in Theorem 21.1 is bounded below by a positive constant depending only on:

$$
c_0.
$$

Hence this is impossible.

---

# 23. CIV/IX-1.7 — Minimal Spectral Persistence Floor

## Corollary 23.1

For infinitely many pairwise-disjoint critical spectral atoms, it is impossible that every atom disappears by a fixed factor on a time scale:

$$
\boxed{
\tau_n
\lesssim
a_n^2
r_n^6.
}
$$

Equivalently, along an infinite subsequence one must have:

$$
\boxed{
\tau_n
\gtrsim
a_n^2
r_n^6
}
$$

unless the selected impulse intervals cease to be disjoint.

### Safety

This is an extremely subparabolic persistence floor.

It is not:

$$
O(r_n^2).
$$

---

# 24. CIV/IX-1.8 — Energy-Class Parabolic Thickening No-Go

## Theorem 24.1

The universal temporal action of Theorem 14.1 does not force parabolic normalized persistence:

$$
\delta_n\gtrsim1.
$$

### Reason

For a geometric scale sequence:

$$
r_n=2^{-n},
$$

choose, for example:

$$
\delta_n=r_n^\beta,
\qquad
0<\beta<4,
$$

and:

$$
a_n\asymp1.
$$

Then the burst lower-bound series is:

$$
\sum_n
r_n^{(4-\beta)/3},
$$

which converges.

Thus a finite:

$$
L_t^{4/3}\dot H^{-1}
$$

temporal-action budget is compatible with normalized persistence:

$$
\delta_n\to0.
$$

$\square$

---

# 25. Balanced impulse scale

Set:

$$
\boxed{
\delta=a^2.
}
$$

Then Theorem 18.1 gives the scale-critical normalized burst:

$$
\boxed{
r^{-4/3}
\int_I
\|
\partial_tu_k
\|_{\dot H^{-1}}^{4/3}dt
\ge
c.
}
$$

Thus:

$$
\boxed{
\text{drop before }a^2r^2
}
$$

forces order-one **normalized** temporal action.

But the corresponding physical action carries:

$$
r^{4/3}
$$

and is summable over geometric scales.

Therefore:

$$
\boxed{
\text{normalized burst coercivity}
\neq
\text{global Critical Lift}.
}
$$

---

# 26. Persistent branch at the balanced scale

If instead:

$$
\mathcal A_{k,Q}(t)
\ge
a/2
$$

for:

$$
\tau=a^2r^2,
$$

then:

$$
\boxed{
r^{-3}
\int_I
\int_Q
|u_k|^2dxdt
\ge
c
a^3.
}
$$

Thus the balanced impulse scale gives a dichotomy:

$$
\boxed{
\text{critical spacetime packet of size }a^3
}
$$

or:

$$
\boxed{
\text{order-one normalized temporal-action burst}.
}
$$

---

# 27. Application to logarithmic FAR atoms

DCRP-04 produced selected-time FAR atoms of scale-dependent strength:

$$
\boxed{
a_k
\gtrsim
[
1+\log(C/r_k)
]^{-2/3}.
}
$$

If a spectrally compatible atom of comparable strength is available, Corollary 23.1 yields only the persistence floor:

$$
\boxed{
\tau_k
\gtrsim
r_k^6
[
1+\log(C/r_k)
]^{-4/3}
}
$$

along an infinite disjoint subsequence.

This is far below the parabolic scale:

$$
r_k^2.
$$

### Meaning

Energy-class temporal regularity alone cannot convert the DCRP logarithmic FAR atom into a full moving-window carrier.

---

# 28. Filtered versus spectral atom safety

The DCRP-04 FAR atom is a filtered-vorticity cell.

Theorem 18.1 is a dyadic spectral velocity-shell theorem.

The two are not identified automatically.

A spectralization/reprofiling theorem is required to transfer one carrier into the other with comparable native strength.

This remains open.

---

# 29. Type-I versus generic impulses

The program now has a sharp contrast.

### Type-I strong critical state

External localized concentration gives:

$$
\boxed{
\text{full parabolic thickening}.
}
$$

### generic energy-class spectral atom

Universal temporal regularity gives only:

$$
\boxed{
\tau
\gtrsim
a^2r^6
}
$$

in the packing sense.

Thus the missing four powers of:

$$
r
$$

must come from singular-branch structure, not generic energy regularity.

---

# 30. Moving-window observability interface

The external moving-window framework reduces persistent badness to:

$$
\boxed{
\text{effective combined observability}
}
$$

or:

$$
\boxed{
\text{combined-invisible defect recurrence}.
}
$$

IDRP supplies the temporal input:

- persistent packet;
- mechanism variation burst;
- spectral temporal-action burst;
- source impulse.

The missing theorem is to map at least one of these burst classes into a depletion-effective combined detector with controlled moving-window growth.

---

# 31. Burst visibility problem

Define:

$$
\boxed{
\textbf{BVP — Burst Visibility Problem}.
}
$$

BVP asks for a theorem of the form:

$$
\boxed{
\text{rapid loss of native atom}
\Longrightarrow
\text{PFET/model-cone/commutator/source observable}
}
$$

with a lower bound strong enough to enter the moving-window depletion series.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 32. Trace thickening problem

Define:

$$
\boxed{
\textbf{TTP — Trace Thickening Problem}.
}
$$

Given a selected-time native atom:

$$
A_r(t_0)\ge a_r,
$$

prove either:

$$
\boxed{
A_r(t)\ge c a_r
}
$$

on a window of normalized thickness:

$$
\delta_r
$$

large enough for effective observability, or prove a BVP-visible burst.

Type-I strong:

$$
L^3
$$

concentration solves TTP externally on that subbranch with:

$$
\delta_r\asymp1.
$$

General TTP remains open.

---

# 33. Recurrent impulse normal forms

After IDRP-01 a selected-time recurrence falls into:

### IR-P

persistent critical packet;

### IR-V

large filtered ledger variation;

### IR-T

large:

$$
L_t^{4/3}\dot H^{-1}
$$

temporal-action burst;

### IR-S

fresh-source impulse;

### IR-I

combined-invisible moving-window recurrence.

These overlap.

They are not declared independent physical mechanisms.

---

# 34. CIV/IX-1.9 — Impulse Temporalization Compiler

## Theorem 34.1

Consider a selected critical carrier on scale:

$$
r.
$$

Relative to the branch-specific hypotheses developed in this paper, at least one of the following occurs:

1. a critical spacetime packet persists;
2. the filtered mechanism ledger pays fixed variation;
3. a spectralized carrier pays the temporal-action lower bound;
4. the causal ledger pays a fresh-source impulse;
5. the carrier remains in a combined-invisible moving-window residual class.

### Safety

The theorem is a compiler of the prior exact alternatives.

It does not prove that alternatives 2--5 have a globally non-summable budget.

$\square$

---

# 35. Strongest positive result

The strongest full-thickness result is external and branch-specific:

$$
\boxed{
\text{Type-I critical state}
\Longrightarrow
\text{parabolic-thick }L^3\text{ packet}.
}
$$

The strongest universal energy-class result is weaker but unconditional:

$$
\boxed{
\text{rapid spectral atom loss}
\Longrightarrow
\text{quantitative }H^{-1}\text{ temporal-action burst}.
}
$$

---

# 36. Strongest no-go

Generic energy-class temporal regularity cannot bridge the entire impulse gap.

The scaling:

$$
\boxed{
\tau_{\min}
\sim
a^2r^6
}
$$

is much shorter than:

$$
r^2.
$$

Hence an IDRP closure must exploit one of:

- Type-I/localized smoothing structure;
- causal source renewal;
- filtered exact mechanism ledgers;
- moving-window combined observability;
- another singular-branch persistence theorem.

---

# 37. Next paper

The next paper should attack BVP directly:

$$
\boxed{
\textbf{
NS-IDRP 02 —
Source-Impulse Visibility,
Filtered Trace Variation,
PFET Burst Coupling,
Logarithmic Atom Thickening
and Moving-Window Depletion
}.
}
$$

Primary tasks:

1. convert super-height source impulses into pressure/flux/energy/trace or model-cone visibility;
2. separate fast filtered-atom loss into diffusion, far-field, commutator, and localization burst channels;
3. couple logarithmic FAR atom floors to the filtered balance;
4. seek a better-than-energy-class persistence exponent from branch-specific structure;
5. connect burst lower bounds to the FCBP half-exponent moving-window threshold;
6. determine whether an impulsive burst can remain combined-invisible;
7. build a temporal critical-lift compiler or isolate the exact invisible burst normal form.

---

# 38. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Type-I Parabolic Thickening}
&:\ \mathrm{EXTERNAL/PROVED\ COROLLARY},\\
\text{Trace Persistence-or-Variation}
&:\ \mathrm{PROVED},\\
\text{Filtered Trace Thickening-or-Burst}
&:\ \mathrm{PROVED\ FROM\ EXTERNAL\ BALANCE},\\
\text{Universal Temporal Action}
&:\ \mathrm{PROVED},\\
\text{Spectral Impulse Action Lower Bound}
&:\ \mathrm{PROVED},\\
\text{Temporal Burst Packing}
&:\ \mathrm{PROVED},\\
\text{Minimal Spectral Persistence Floor}
&:\ \mathrm{PROVED},\\
\text{generic parabolic thickening}
&:\ \mathrm{NO\mbox{-}GO\ FROM\ ENERGY\ ACTION\ ALONE},\\
\text{FAR filtered-to-spectral transfer}
&:\ \mathrm{OPEN},\\
\text{Burst Visibility Problem}
&:\ \mathrm{OPEN},\\
\text{general Trace Thickening Problem}
&:\ \mathrm{OPEN},\\
\text{Impulsive Diffuse Recurrence exclusion}
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

# 39. Conclusion

IDRP-01 makes the temporal impulse problem quantitative.

In the strong Type-I critical branch, localized concentration already persists on every late parabolic horizon slab.

This gives a genuine scale-critical spacetime packet and shows that "instantaneous only" is not the correct Type-I state normal form.

For a generic energy-class spectral atom, however, the universal temporal modulus is much weaker.

The finite-energy equation gives:

$$
\partial_tu
\in
L_t^{4/3}
\dot H_x^{-1}.
$$

Band localization converts rapid loss of a critical scale-$r$ atom into the lower bound:

$$
r^{-4/3}
\int_I
\|\partial_tu_k\|_{\dot H^{-1}}^{4/3}
\gtrsim
a^{2/3}\delta^{-1/3}.
$$

Disjoint impulses therefore satisfy a true global packing law.

But the induced persistence floor is only:

$$
\tau
\gtrsim
a^2r^6,
$$

not the parabolic:

$$
r^2
$$

scale required by the strongest moving-window arguments.

This four-power gap is the central result of the paper.

It proves that temporal regularity alone cannot solve the impulsive recurrence problem.

The next theorem must use singular-branch structure to convert rapid trace loss into visible source/work/mechanism activity.

Thus IDRP has a precise target:

$$
\boxed{
\textbf{
impulse disappearance}
\Longrightarrow
\textbf{
depletion-effective visible burst}.
}
}
$$

That is the Burst Visibility Problem.

---

# References

1. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115.
2. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
3. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
4. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
5. `NS_DCRP_CYCLE_VIII_HANDOFF_v1.0.md`.
6. `NS_DCRP_04_TemporalRecurrence_FinalAudit_v0.1.md`.