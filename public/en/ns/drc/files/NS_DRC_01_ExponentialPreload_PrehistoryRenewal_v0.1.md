---
title: "Navier–Stokes Dynamic Reservoir Closure Program 01: Exponential Preload, Prehistory Renewal, Viscous-Age Slabs and High-Parent Source Genealogy"
short_title: "NS-DRC 01"
series: "Navier–Stokes Dynamic Reservoir Closure Program"
cycle: "III"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style dynamic reservoir genealogy / Cycle-III opening paper"
epistemic_status: "Refines the Cycle-II EXP-PRELOAD branch to the actual high-frequency strain tail required by a later middle-strain spike. It proves that high-frequency old-stock survival across the post-escape interval requires exponential high-tail preload, and then proves that such preload cannot be an unforced remnant of fixed smooth initial data: it must itself be created by prehistory Duhamel forcing. A viscous-age slab argument localizes a source-renewal packet unless the earlier high-tail stock grows exponentially backward. The prehistory forcing splits into strain-vorticity model residual forcing or quadratic-vorticity forcing, and the latter requires genuine high-frequency vorticity parent state. Thus EXP-PRELOAD is removed as an independent residual mechanism and recompiled into source renewal. The remaining source-efficiency, dissipation-range, and dilution problems remain open. Navier–Stokes regularity is NOT proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Dynamic Reservoir Closure Program 01

# Exponential Preload, Prehistory Renewal, Viscous-Age Slabs and High-Parent Source Genealogy

## 0. Cycle-III launch point

Cycle II closed with four residual mechanisms:

$$
\boxed{
R_{\rm EXP},
\qquad
R_{\rm DISS},
\qquad
R_{\rm DIL},
\qquad
R_{\rm SRC}.
}
$$

The present paper attacks:

$$
\boxed{
R_{\rm EXP}.
}
$$

Cycle II proved that a high-frequency strain reservoir surviving many viscous ages from a half-level Besov escape time:

$$
\tau_t
$$

to a later middle-strain spike:

$$
t
$$

must either be dynamically replenished after:

$$
\tau_t,
$$

or have exponentially large preload amplitude.

The remaining question is:

> Can this exponentially large preload be a genuinely old, source-free reservoir inherited from the initial data?

For fixed smooth initial data and sufficiently high dangerous frequencies, the answer is:

$$
\boxed{
\textbf{No.}
}
$$

An exponentially large preload must itself have a prehistory forcing genealogy.

---

# 1. Exact strain equation

Normalize viscosity:

$$
\nu=1.
$$

Let:

$$
S
=
\nabla_{\rm sym}u,
$$

and:

$$
\omega
=
\nabla\times u.
$$

Following Miller define:

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

Then the exact projected strain equation is:

$$
\boxed{
\partial_tS
-
\Delta S
=
\mathcal F_S,
}
$$

where:

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

Therefore for:

$$
0\le a<b<T,
$$

$$
\boxed{
S(b)
=
e^{(b-a)\Delta}S(a)
+
\int_a^b
e^{(b-s)\Delta}
\mathcal F_S(s)\,ds.
}
$$

---

# 2. Later middle-strain spike

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

Cycle II proved that a sufficiently large middle-strain spike forces a high-frequency strain-gradient tail.

Choose:

$$
J_g(t)
$$

so:

$$
\boxed{
2^{2J_g(t)}
\asymp
\frac{
g(t)
}{
E_2^2
}.
}
$$

Then:

$$
\boxed{
\|
P_{\ge J_g(t)}
S(t)
\|_{\dot H^1}
\ge
c_g
\frac{
g(t)
}{
E_2
}.
}
$$

For brevity write:

$$
\boxed{
J=J_g(t),
\qquad
\lambda=2^J.
}
$$

---

# 3. Half-level escape time

Let:

$$
B(t)
=
\|u(t)\|_{\dot B^{-1/2}_{\infty,\infty}}.
$$

For a sufficiently high dangerous spike define:

$$
\boxed{
\tau
=
\tau_t
=
\tau
\left(
\frac{B(t)}2
\right).
}
$$

Cycle II gives:

$$
\boxed{
B(\tau)
=
\frac{B(t)}2,
}
$$

and:

$$
\tau\uparrow T
$$

along sufficiently high escape levels.

Define:

$$
\boxed{
\Delta
=
t-\tau.
}
$$

---

# 4. Actual high-tail preload

Define:

$$
\boxed{
A_J(s)
=
\|
P_{\ge J}S(s)
\|_{\dot H^1}.
}
$$

Define the **actual high-tail preload ratio**:

$$
\boxed{
\mathfrak P_{\rm hi}(t)
=
\frac{
E_2 A_J(\tau)
}{
g(t)
}.
}
$$

This refines the coarse Cycle-II total-Hdot1 preload ratio.

Only:

$$
A_J(\tau)
$$

can directly survive by heat flow into the final:

$$
P_{\ge J}
$$

tail.

---

# 5. Post-escape source debt

Define:

$$
\boxed{
\mathfrak D_{\rm post}(t)
=
\int_\tau^t
e^{-c_h\lambda^2(t-s)}
\|
P_{\ge J}
\mathcal F_S(s)
\|_{\dot H^1}
\,ds.
}
$$

The high-frequency heat estimate gives:

$$
\boxed{
A_J(t)
\le
C_h
e^{-c_h\lambda^2\Delta}
A_J(\tau)
+
C_h
\mathfrak D_{\rm post}(t).
}
$$

---

# 6. CIII-1.1 — Actual High-Tail Survival / Replenishment

## Theorem 6.1

There exist universal constants:

$$
c_1,c_2>0
$$

such that every sufficiently large middle-strain spike satisfies at least one of:

### POST-REP

$$
\boxed{
\mathfrak D_{\rm post}(t)
\ge
c_1
\frac{
g(t)
}{
E_2
};
}
$$

### EXP-HI

$$
\boxed{
\mathfrak P_{\rm hi}(t)
\ge
c_2
\exp
\left(
c_h
\lambda^2\Delta
\right).
}
$$

### Proof

The final state extraction gives:

$$
A_J(t)
\ge
c_g
g/E_2.
$$

If the Duhamel term contributes at least half this lower bound, POST-REP holds.

Otherwise the heat-propagated high-tail term must contribute the remaining fixed fraction:

$$
C_h
e^{-c_h\lambda^2\Delta}
A_J(\tau)
\gtrsim
g/E_2.
$$

Rearrange. $\square$

---

# 7. Significance of EXP-HI

The old Cycle-II EXP-PRELOAD could, in principle, be caused by large:

$$
\dot H^1
$$

stock far below:

$$
J.
$$

Theorem 6.1 removes this ambiguity.

The actual surviving old-stock branch requires exponential inflation of the **same high-frequency tail** needed by the later spike:

$$
\boxed{
P_{\ge J}S(\tau).
}
$$

This is the correct reservoir variable for the dynamic closure problem.

---

# 8. Prehistory Duhamel debt

For:

$$
0\le a<\tau,
$$

define:

$$
\boxed{
\mathfrak D_{\rm pre}(a,\tau;J)
=
\int_a^\tau
e^{-c_h\lambda^2(\tau-s)}
\|
P_{\ge J}
\mathcal F_S(s)
\|_{\dot H^1}
\,ds.
}
$$

The Duhamel formula gives:

$$
\boxed{
A_J(\tau)
\le
C_h
e^{-c_h\lambda^2(\tau-a)}
A_J(a)
+
C_h
\mathfrak D_{\rm pre}(a,\tau;J).
}
$$

---

# 9. Fixed smooth initial data

Assume:

$$
S(0)\in\dot H^1.
$$

Then:

$$
\boxed{
A_J(0)
\le
\|S(0)\|_{\dot H^1}
<
\infty.
}
$$

For a dangerous middle-strain sequence:

$$
t_n\uparrow T,
$$

with:

$$
g(t_n)\to\infty,
$$

one has:

$$
J_g(t_n)\to\infty.
$$

Also:

$$
\tau_{t_n}\uparrow T>0.
$$

Therefore:

$$
\boxed{
e^{-c_h2^{2J_g(t_n)}\tau_{t_n}}
A_{J_g(t_n)}(0)
\to0.
}
$$

---

# 10. CIII-1.2 — Exponential Preload Has Prehistory Source

## Theorem 10.1

Let:

$$
t_n\uparrow T
$$

be sufficiently high EXP-HI events.

Then for all sufficiently large:

$$
n,
$$

$$
\boxed{
\mathfrak D_{\rm pre}
(
0,\tau_{t_n};
J_g(t_n)
)
\ge
c
A_{J_g(t_n)}
(
\tau_{t_n}
).
}
$$

Consequently:

$$
\boxed{
\mathfrak D_{\rm pre}
(
0,\tau_{t_n};
J_g(t_n)
)
\gtrsim
\exp
\left(
c
\mathfrak V_{\rm pre}(t_n)
\right)
\frac{
g(t_n)
}{
E_2
}
}
$$

on the EXP-HI branch.

### Proof

Use Section 8 with:

$$
a=0.
$$

The initial heat contribution tends to zero by Section 9.

For large:

$$
n,
$$

it is at most half of:

$$
A_J(\tau).
$$

Therefore the weighted prehistory source must supply the remaining fixed fraction.

Insert the EXP-HI lower bound. $\square$

---

# 11. Main interpretation

An exponentially inflated high-frequency preload cannot be a source-free remnant of fixed smooth initial data.

It must itself have been generated by earlier nonlinear strain forcing.

Therefore:

$$
\boxed{
\textbf{EXP-PRELOAD is not a primitive reservoir mechanism.}
}
$$

It is a prehistory replenishment mechanism.

---

# 12. Viscous-age slabs

Choose:

$$
\vartheta>0
$$

large enough that:

$$
\boxed{
q_h
=
C_h
e^{-c_h\vartheta}
\le
\frac14.
}
$$

Define one high-frequency viscous-age step:

$$
\boxed{
h_J
=
\vartheta
2^{-2J}.
}
$$

Let:

$$
s_0=\tau,
$$

and:

$$
s_k
=
\tau-kh_J
$$

for all full slabs remaining in:

$$
[0,\tau].
$$

---

# 13. Slab source debt

For:

$$
k\ge1,
$$

define:

$$
\boxed{
D_k
=
\int_{s_k}^{s_{k-1}}
e^{-c_h2^{2J}(s_{k-1}-s)}
\|
P_{\ge J}
\mathcal F_S(s)
\|_{\dot H^1}
\,ds.
}
$$

Duhamel gives:

$$
\boxed{
A_J(s_{k-1})
\le
q_h
A_J(s_k)
+
C_hD_k.
}
$$

---

# 14. CIII-1.3 — Backward Inflation or Source Packet

## Theorem 14.1

For each full viscous-age slab, at least one of:

### SOURCE-PACKET

$$
\boxed{
D_k
\ge
\frac1{
2C_h
}
A_J(s_{k-1});
}
$$

### BACKWARD-INFLATE

$$
\boxed{
A_J(s_k)
\ge
2
A_J(s_{k-1})
}
$$

holds.

### Proof

If SOURCE-PACKET fails, then:

$$
C_hD_k
<
\frac12
A_J(s_{k-1}).
$$

Hence:

$$
\frac12
A_J(s_{k-1})
<
q_hA_J(s_k).
$$

Since:

$$
q_h\le1/4,
$$

BACKWARD-INFLATE follows. $\square$

---

# 15. Multi-slab consequence

If the first:

$$
N
$$

backward slabs contain no SOURCE-PACKET, then:

$$
\boxed{
A_J(s_N)
\ge
2^N
A_J(\tau).
}
$$

Thus source-free backward continuation causes exponential growth of the already exponentially large high-frequency preload.

---

# 16. CIII-1.4 — Prehistory Renewal Packet Theorem

## Theorem 16.1

Fix:

$$
t_0\in(0,T).
$$

Assume the solution is smooth on:

$$
[0,t_0].
$$

For every sufficiently high EXP-HI event with:

$$
\tau>t_0,
$$

there exists at least one viscous-age slab:

$$
I_k
=
[s_k,s_{k-1}]
\subset
[t_0,\tau]
$$

such that:

$$
\boxed{
D_k
\ge
c
A_J(\tau).
}
$$

### Proof

Suppose no such slab exists.

Then in particular no SOURCE-PACKET occurs with threshold comparable to the current tail.

Repeated application of Theorem 14.1 yields exponential backward inflation:

$$
A_J(s_N)
\ge
2^N
A_J(\tau)
$$

until reaching:

$$
[t_0,t_0+h_J].
$$

But smoothness on:

$$
[0,t_0+h_1]
$$

gives a finite uniform:

$$
\dot H^1
$$

bound independent of sufficiently large:

$$
J.
$$

Meanwhile:

$$
N
\sim
(\tau-t_0)2^{2J}/\vartheta
\to\infty.
$$

This contradicts the exponential lower bound for large:

$$
J.
$$

Therefore a source packet occurs.

Because all earlier no-source slabs only increase the tail backward, the first source packet found has size at least a fixed multiple of:

$$
A_J(\tau).
$$

$\square$

---

# 17. Renewal interpretation

Theorem 16.1 upgrades the global prehistory source debt.

The exponentially large preload is not merely generated somewhere in the remote past.

It has a finite-viscous-age source ancestor:

$$
\boxed{
\text{high-frequency preload stock}
\longleftarrow
\text{high-frequency source packet}.
}
$$

If one repeats the argument for the earlier stock at:

$$
s_k,
$$

one obtains a backward renewal genealogy until:

- a source packet is found;
- or one reaches the smooth initial regime.

The second alternative cannot sustain arbitrarily high EXP-HI events.

---

# 18. Prehistory source split

For any slab define:

$$
D_k^{SV}
=
\int_{I_k}
e^{-c_h2^{2J}(s_{k-1}-s)}
\|
P_{\ge J}
\mathcal R_{SV}(s)
\|_{\dot H^1}
\,ds,
$$

and:

$$
D_k^{\omega}
=
\int_{I_k}
e^{-c_h2^{2J}(s_{k-1}-s)}
\|
P_{\ge J}
P_{st}
(
\omega\otimes\omega
)(s)
\|_{\dot H^1}
\,ds.
$$

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

$$
D_k
\le
\frac12D_k^\omega
+
D_k^{SV}.
$$

---

# 19. CIII-1.5 — Prehistory Replenishment Split

## Theorem 19.1

For the renewal slab in Theorem 16.1, at least one of:

### PRE-SV

$$
\boxed{
D_k^{SV}
\ge
c
A_J(\tau);
}
$$

### PRE-VORT

$$
\boxed{
D_k^\omega
\ge
c
A_J(\tau)
}
$$

holds.

$\square$

---

# 20. High-parent support

Decompose:

$$
\omega
=
\sum_p
\omega_p.
$$

Standard Fourier support implies:

$$
P_{\ge J}
P_{st}
(
\omega_p\otimes\omega_q
)
\neq0
$$

only if:

$$
\boxed{
\max\{p,q\}
\ge
J-C_{\rm LP}.
}
$$

---

# 21. CIII-1.6 — Prehistory High-Parent Genealogy

## Theorem 21.1

On the PRE-VORT branch, the renewal source packet contains genuine vorticity parent state at frequency:

$$
\boxed{
\ge
J-C_{\rm LP}.
}
$$

Therefore the exponential preload has a high-frequency parent-state ancestor in its prehistory.

### Safety

This does not select one fixed-share parent shell.

Parent multiplicity, cancellation and source-to-state efficiency remain open.

$\square$

---

# 22. Two-sided source genealogy

Combining CSP-07 and DRC-01:

the final high-frequency state required by a middle-strain spike satisfies one of:

### POST-REP

source replenishment between:

$$
\tau
$$

and:

$$
t;
$$

### PRE-REP

a high-frequency prehistory source packet before:

$$
\tau.
$$

The apparent third branch:

$$
\text{EXP-PRELOAD}
$$

has been absorbed into PRE-REP.

Thus:

$$
\boxed{
\text{high-frequency dangerous state}
\Longrightarrow
\text{pre-escape source renewal}
\vee
\text{post-escape source renewal}.
}
$$

---

# 23. CIII-1.7 — EXP-PRELOAD Absorption Theorem

## Theorem 23.1

For fixed smooth initial data and sufficiently high dangerous middle-strain events:

$$
\boxed{
R_{\rm EXP}
\subset
R_{\rm SRC}^{pre}.
}
$$

Consequently the independent Cycle-II residual core:

$$
R_{\rm EXP}
\cup
R_{\rm DISS}
\cup
R_{\rm DIL}
\cup
R_{\rm SRC}
$$

reduces to:

$$
\boxed{
R_{\rm DISS}
\cup
R_{\rm DIL}
\cup
R_{\rm SRC}^{\ast},
}
$$

where:

$$
R_{\rm SRC}^{\ast}
$$

contains both prehistory and posthistory replenishment, including:

- model-cone residual forcing;
- high-parent vorticity forcing;
- multiplicity/cancellation/efficiency escape.

### Status

This is a reduction theorem relative to the Cycle-II dangerous-event architecture.

It is not a regularity theorem. $\square$

---

# 24. Source-age localization

Let:

$$
G_{\rm pre}
=
\int_0^\tau
\|
P_{\ge J}
\mathcal F_S(s)
\|_{\dot H^1}
\,ds.
$$

For:

$$
L>0,
$$

split:

$$
[0,\tau]
$$

into:

$$
[\tau-L2^{-2J},\tau]
$$

and its complement.

The old-source contribution is bounded by:

$$
\boxed{
e^{-c_hL}
G_{\rm pre}.
}
$$

Therefore if the recent:

$$
L
$$

-viscous-age source contribution is less than half:

$$
A_J(\tau),
$$

then:

$$
\boxed{
G_{\rm pre}
\gtrsim
e^{c_hL}
A_J(\tau).
}
$$

So avoiding a recent source ancestor requires exponentially large historical source gross.

---

# 25. Meaning of source-age localization

The source genealogy has the same structural form as the old-stock survival problem:

$$
\boxed{
\text{recent renewal}
\vee
\text{exponentially large old source gross}.
}
$$

Thus viscous age repeatedly converts temporal separation into exponential amplitude/source debt.

This is the central dynamic-reservoir principle exposed by Cycle III.

---

# 26. External quantitative propagation interface

Tao's quantitative critical:

$$
L^3
$$

regularity theory replaces compactness and backward uniqueness arguments by quantitative propagation and Carleman estimates.

A major component of the argument is backward propagation of concentration/frequency activity from a later dangerous configuration.

Barker--Prange similarly develop quantitative spatial concentration and backward propagation technology near possible singularities.

These results provide standard-PDE interfaces for strengthening the simple Duhamel source genealogy obtained here into a spatially localized or critical-norm localized genealogy.

DRC-01 itself does not import those stronger conclusions.

---

# 27. Why static preload no-go is now superseded

CSP-08 proved that energy plus instantaneous critical Besov amplitude cannot bound:

$$
\|S\|_{\dot H^1}.
$$

DRC-01 does not contradict that no-go.

Instead it uses:

$$
\boxed{
\text{the time evolution equation}.
}
$$

The relevant statement is no longer:

> high Hdot1 preload cannot exist.

It is:

> high-frequency preload cannot remain genealogically source-free.

This is a genuinely dynamic statement.

---

# 28. Residual source problem

After absorbing:

$$
R_{\rm EXP},
$$

the principal source residual is:

$$
\boxed{
R_{\rm SRC}^{\ast}.
}
$$

It contains:

1. high-parent multiplicity;
2. cancellation among source contributions;
3. amplification of small parent state into large source share;
4. prehistory versus posthistory source distribution;
5. model-cone residual forcing versus vorticity-parent forcing.

The next source theorem must relate **source share** to **state-energy share**.

---

# 29. Residual Cycle-III frontier

After DRC-01 the minimal residual classes are:

$$
\boxed{
R_{\rm DISS},
\qquad
R_{\rm DIL},
\qquad
R_{\rm SRC}^{\ast}.
}
$$

The original exponential preload class has been absorbed.

These three classes are all forcing/transport classes:

- dissipation-range replenishment;
- local/global reservoir dilution;
- source-to-state efficiency/cancellation.

---

# 30. New guards

Add:

### $G_{\rm HITAIL}$

Old-stock survival must track the actual high-frequency preload tail, not total Hdot1 preload.

### $G_{\rm PREHIST}$

An EXP-HI preload must preserve its prehistory Duhamel forcing genealogy.

### $G_{\rm VSLAB}$

Prehistory transport must be resolved in fixed viscous-age slabs when local source ancestry is claimed.

### $G_{\rm BACKINF}$

A source-free high-frequency slab forces backward stock inflation; this cannot be silently discarded.

### $G_{\rm PREPARENT}$

Quadratic-vorticity prehistory replenishment must preserve high-frequency parent state.

### $G_{\rm SRCAGE}$

Remote source ancestry must preserve the exponential source-age tax.

---

# 31. Next paper

The natural next target is now:

$$
\boxed{
R_{\rm SRC}^{\ast}.
}
$$

Therefore:

$$
\boxed{
\textbf{
NS-DRC 02 —
Source-to-State Efficiency,
Parent Multiplicity,
Cancellation Geometry
and Renewal-Chain Compression
}.
}
$$

Primary tasks:

1. normalize pre/post replenishment source shares by parent state-energy shares;
2. derive source amplification ratios analogous to the earlier packet amplification tax;
3. prove finite parent-state capture or amplification escape;
4. distinguish cancellation from genuine parent absence;
5. connect repeated prehistory renewal packets into a finite-branching source genealogy;
6. test whether the source residual can be absorbed into:
   $$
   D_{\rm eig},
   \quad
   \mathcal A_{SV},
   \quad
   R_{\rm DISS}.
   $$

---

# 32. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{actual high-tail preload ratio}
&:\ \mathrm{DEFINED},\\
\text{actual high-tail survival/replenishment}
&:\ \mathrm{PROVED},\\
\text{fixed-initial-data heat-remnant decay}
&:\ \mathrm{PROVED},\\
\text{EXP-HI prehistory source theorem}
&:\ \mathrm{PROVED},\\
\text{viscous-age slab dichotomy}
&:\ \mathrm{PROVED},\\
\text{prehistory renewal packet}
&:\ \mathrm{PROVED},\\
\text{prehistory source split}
&:\ \mathrm{PROVED},\\
\text{prehistory high-parent genealogy}
&:\ \mathrm{PROVED},\\
R_{\rm EXP}\text{ as independent residual}
&:\ \mathrm{ABSORBED},\\
\text{source-age localization}
&:\ \mathrm{PROVED},\\
R_{\rm SRC}^{\ast}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm DISS}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm DIL}\text{ closure}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 33. Conclusion

Cycle III begins by eliminating a misleading residual interpretation.

The exponentially large preload required to survive many viscous ages cannot be treated as a source-free old reservoir.

Tracking the actual high-frequency tail gives:

$$
\boxed{
\text{final dangerous high-frequency state}
\Longrightarrow
\text{post-escape replenishment}
\vee
\text{EXP-HI preload}.
}
$$

But fixed smooth initial data and prehistory Duhamel then give:

$$
\boxed{
\text{EXP-HI preload}
\Longrightarrow
\text{prehistory replenishment}.
}
$$

Hence:

$$
\boxed{
\text{final dangerous high-frequency state}
\Longrightarrow
\text{pre-escape source renewal}
\vee
\text{post-escape source renewal}.
}
$$

The prehistory renewal can be localized to a finite viscous-age slab unless one pays exponentially growing backward stock or historical source gross.

Its source is necessarily either:

$$
\boxed{
\mathcal R_{SV}
}
$$

or:

$$
\boxed{
P_{st}(\omega\otimes\omega)
}
$$

with genuine high-frequency vorticity parent participation.

Thus:

$$
\boxed{
R_{\rm EXP}
}
$$

is removed as an independent Cycle-III residual.

The next problem is source efficiency.

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691v2.
2. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier–Stokes equations*, arXiv:1908.04958v2.
3. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717v3.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043v2.
5. `NS_CSP_07_PreloadedReservoir_Transport_Replenishment_v0.1.md`.
6. `NS_CSP_08_UnifiedReservoirCover_CycleIIClosure_v0.1.md`.
7. `NS_CSP_CYCLE_II_HANDOFF_v1.0.md`.