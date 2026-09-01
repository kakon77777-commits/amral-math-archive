---
title: "Navier–Stokes Reverse Formation Program 09: Pressure/Far-Field, Adjoint Distortion, Interaction Efficiency, and Unified Tax Ledger"
short_title: "NS-RFP 09"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style escape compression / tax-compactness architecture"
epistemic_status: "Defines a finite scale-invariant core tax vector for the surviving RFP escape mechanisms; proves uniform selector bounds, collapses commutator and band-passed far-field escape into adjoint-distortion/interaction-efficiency taxes, derives parent-gap and plateau-gap bounds from earlier RFP estimates, and proves a bounded-tax certificate-compactness/path-closure theorem conditional on representation completeness and arbitrarily deep finite realizability. Does NOT prove that the core taxes are universally bounded, that every tax divergence is dynamically dangerous, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 09

# Pressure/Far-Field, Adjoint Distortion, Interaction Efficiency, and Unified Tax Ledger

## 0. Positioning of this Document

RFP-01 through RFP-08 have progressively decomposed the possible singularity-formation escapes from the vague:

$$
\text{high-frequency blow-up}
$$

into:

- first-passage source debt;
- exact parent provenance;
- parent-gap escape;
- spacetime tube leakage;
- witness atomization;
- persistence bottleneck;
- packet amplification;
- packet output-depth escape;
- memory-depth escape;
- temporal congestion;
- pressure/far-field leakage;
- adjoint distortion;
- interaction inefficiency.

Up to RFP-08, the main question is no longer:

> What other escape names are there?

but rather:

> Are these escapes actually just different projections of a few scale-compatible loss-of-control variables?

This document answers:

$$
\boxed{
\textbf{YES, at the level of the current RFP certificate architecture.}
}
$$

We establish a finite core tax vector:

$$
\boxed{
\mathbf T_n^{core}
}
$$

and prove that the current multitude of secondary escape coordinates can be uniformly controlled or reclassified by it.

---

# 1. Tax is Not Synonymous with Blow-up Driver

In this document, calling:

$$
\mathfrak T
$$

a tax,

merely indicates:

$$
\boxed{
\text{the quantitative cost that a certain ancestry closure step must pay to maintain uniform legality}.
}
$$

Therefore:

$$
\mathfrak T_n\to\infty
$$

primarily indicates:

$$
\boxed{
\text{the corresponding closure mechanism loses uniform control}.
}
$$

It does not automatically imply:

$$
\boxed{
\text{this mechanism causes singularity}.
}
$$

In particular:

- interaction inefficiency may arise from nonlinear depletion;
- large omitted operator activity may have a regularizing effect;
- pressure / localization tax may simply be representation or certificate degradation.

We introduce a new theorem-safety principle:

$$
\boxed{
\text{tax divergence}
\neq
\text{blow-up mechanism}.
}
$$

---

# 2. Typed Tax Classes

This document classifies taxes into four types.

## Geometry Taxes

Controlling scale / carrier / parent geometry:

$$
\mathfrak T^{par},
\qquad
\mathfrak T^{depth}.
$$

## Provenance Taxes

Controlling witness / bridge / packet attribution:

$$
\mathfrak T^{atom},
\quad
\mathfrak T^{bridge},
\quad
\mathfrak T^{amp},
\quad
\mathfrak T^{int}.
$$

## Localization Taxes

Controlling moving tubes and spatial leakage:

$$
\mathfrak T^{adj},
$$

and those derived from it:

$$
\mathfrak T^{com},
\quad
\mathfrak T^{far}.
$$

## History Taxes

Controlling old / fresh source history:

$$
\mathfrak T^{mem},
\qquad
\mathfrak T^{time}.
$$

---

# 3. Macro-Edge Convention

Following the RFP-07 / 08 plateau-compressed PF-A macro skeleton:

$$
I_n=[T_n,T_{n+1}],
$$

and the plateau-end base scale:

$$
K_n.
$$

Each macro edge possesses:

- positive local-source witness ledger;
- field packet family;
- packet bridge scores;
- age ledger;
- fresh-source lag ledger;
- adjoint spacetime tubes.

---

# 4. Strong-Node Atom

Let the RFP-05 positive local-source probability be:

$$
\pi_n(w),
$$

and:

$$
\sum_w\pi_n(w)=1.
$$

Define the maximal node atom:

$$
\boxed{
a_n
=
\max_w
\pi_n(w).
}
$$

---

# 5. Core Tax 1 — Atomization Tax

Define:

$$
\boxed{
\mathfrak T_n^{atom}
=
\frac1{a_n}.
}
$$

Since:

$$
0<a_n\le1,
$$

we have:

$$
\boxed{
1\le
\mathfrak T_n^{atom}
<
\infty
}
$$

on each finite smooth edge.

And:

$$
\mathfrak T_n^{atom}\to\infty
$$

is precisely the RFP-05 node atomization escape.

---

# 6. Canonical Strong-Node Class

Define:

$$
\boxed{
\mathcal W_n^\star
=
\left\{
w:
\pi_n(w)\ge\frac{a_n}{2}
\right\}.
}
$$

This set is non-empty.

---

# 7. C9.1 — Strong-Node Cardinality Bound

## Theorem 7.1

We have:

$$
\boxed{
|\mathcal W_n^\star|
\le
2\mathfrak T_n^{atom}.
}
$$

### Proof

Each:

$$
w\in\mathcal W_n^\star
$$

has at least probability:

$$
a_n/2.
$$

and the sum is:

$$
1.
$$

$\square$

---

# 8. Best Predecessor Bridge Floor

For:

$$
w\in\mathcal W_{n+1}^\star,
$$

let:

$$
\boxed{
\beta_n(w)
=
\sup_v
\mathfrak b_n(v,w),
}
$$

where the supremum is taken over the RFP-08 field packets.

Then define:

$$
\boxed{
\beta_n^\star
=
\inf_{w\in\mathcal W_{n+1}^\star}
\beta_n(w).
}
$$

---

# 9. Core Tax 2 — Bridge Bottleneck Tax

Define:

$$
\boxed{
\mathfrak T_n^{bridge}
=
\begin{cases}
1/\beta_n^\star,
&
\beta_n^\star>0,
\\
+\infty,
&
\beta_n^\star=0.
\end{cases}
}
$$

Thus, a bounded:

$$
\mathfrak T_n^{bridge}
$$

is equivalent to:

> Every canonical strong child has a field packet predecessor with a uniform positive bridge floor.

---

# 10. Active Bridge Class

If:

$$
\beta_n^\star>0,
$$

define:

$$
\boxed{
\mathscr B_n^\star
=
\left\{
(v,w):
w\in\mathcal W_{n+1}^\star,
\quad
\mathfrak b_n(v,w)
\ge
\frac{\beta_n^\star}{2}
\right\}.
}
$$

For each:

$$
w\in\mathcal W_{n+1}^\star
$$

there exists at least one active predecessor.

---

# 11. Packet Amplification Input

RFP-08 defines:

$$
\mathfrak A_n(v,w)
=
\frac{
\mathfrak b_n(v,w)
}{
q_n(v)
}.
$$

---

# 12. Core Tax 3 — Packet Amplification Tax

Define:

$$
\boxed{
\mathfrak T_n^{amp}
=
1+
\sup_{(v,w)\in\mathscr B_n^\star}
\mathfrak A_n(v,w).
}
$$

If:

$$
\mathscr B_n^\star=\varnothing,
$$

let:

$$
\mathfrak T_n^{amp}=+\infty.
$$

---

# 13. C9.2 — Active Packet Strength

## Theorem 13.1

For:

$$
(v,w)\in\mathscr B_n^\star,
$$

we have:

$$
\boxed{
q_n(v)
\ge
\frac{
1
}{
2
\mathfrak T_n^{bridge}
\mathfrak T_n^{amp}
}.
}
$$

### Proof

The active bridge gives:

$$
\mathfrak b_n(v,w)
\ge
\frac1{
2\mathfrak T_n^{bridge}
}.
$$

And:

$$
\mathfrak A_n(v,w)
\le
\mathfrak T_n^{amp}.
$$

From:

$$
q_n(v)
=
\mathfrak b_n(v,w)
/\mathfrak A_n(v,w).
$$

$\square$

---

# 14. C9.3 — Uniform Predecessor Packet Count

## Theorem 14.1

All active predecessor packets fall within:

$$
\boxed{
\mathcal V_n^{pkt}
\left(
\frac1{
2
\mathfrak T_n^{bridge}
\mathfrak T_n^{amp}
}
\right).
}
$$

Therefore, the number of distinct active predecessor packets is at most:

$$
\boxed{
2
\mathfrak T_n^{bridge}
\mathfrak T_n^{amp}.
}
$$

### Proof

Apply the RFP-08 packet-level finite cardinality theorem. $\square$

---

# 15. Core Tax 4 — Parent-Tightness Tax

Following RFP-04:

$$
\mathfrak V_n
$$

and:

$$
1-C_n^{par}(L)
\le
C2^{-L}\mathfrak V_n.
$$

Define:

$$
\boxed{
\mathfrak T_n^{par}
=
1+\mathfrak V_n.
}
$$

---

# 16. C9.4 — Uniform Parent-Gap Selector

## Theorem 16.1

If:

$$
\mathfrak T_n^{par}\le K,
$$

then for any:

$$
0<\varepsilon<1
$$

choosing:

$$
\boxed{
L_\varepsilon(K)
=
\left\lceil
\log_2
\left(
\frac{CK}{\varepsilon}
\right)
\right\rceil,
}
$$

guarantees:

$$
\boxed{
C_n^{par}
\left(
L_\varepsilon(K)
\right)
\ge
1-\varepsilon.
}
$$

$\square$

---

# 17. Core Tax 5 — Packet Output-Depth Tax

Following RFP-08:

$$
\mathfrak O_n^{pkt}.
$$

Define:

$$
\boxed{
\mathfrak T_n^{depth}
=
1+\mathfrak O_n^{pkt}.
}
$$

---

# 18. C9.5 — Plateau Gap Bound from Taxes

## Theorem 18.1

Assume:

$$
\mathfrak T_n^{bridge}
\le
K_B,
$$

$$
\mathfrak T_n^{amp}
\le
K_A,
$$

and:

$$
\mathfrak T_n^{depth}
\le
K_O.
$$

If:

$$
w\in\mathcal W_{n+1}^\star
$$

crosses the macro plateau gap via an active direct packet bridge:

$$
G_n,
$$

then:

$$
\boxed{
G_n
\le
C_\ast
+
\log_2
\left(
2K_BK_AK_O
\right).
}
$$

### Proof

The RFP-08 strong direct plateau bridge theorem gives:

$$
\mathfrak O_n^{pkt}
\ge
\frac{\gamma}{A_0}
2^{G_n-C_\ast}.
$$

For an active bridge, we can choose:

$$
\gamma
=
\frac1{2K_B},
$$

and:

$$
A_0\le K_A,
$$

$$
\mathfrak O_n^{pkt}\le K_O.
$$

Rearranging the terms yields the result. $\square$

---

# 19. Consequence: Plateau Depth is Not an Independent Primitive Tax

If:

$$
G_n\to\infty
$$

along a strong direct-bridge branch,

then at least one of:

$$
\boxed{
\mathfrak T_n^{bridge},
\quad
\mathfrak T_n^{amp},
\quad
\mathfrak T_n^{depth}
}
$$

must diverge.

Therefore, unbounded plateau crossing does not require establishing a tenth primitive tax.

---

# 20. Core Tax 6 — Adjoint Distortion

Following RFP-04:

$$
\mathfrak D_n^{adj}
=
\exp
\left(
\int_{I_n}
\|\nabla u(t)\|_\infty
dt
\right).
$$

Define:

$$
\boxed{
\mathfrak T_n^{adj}
=
\mathfrak D_n^{adj}.
}
$$

We have:

$$
\mathfrak T_n^{adj}\ge1.
$$

---

# 21. Scaling Audit of Adjoint Tax

Navier–Stokes scaling:

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t)
$$

gives:

$$
\nabla u_\lambda
=
\lambda^2
\nabla u(\lambda x,\lambda^2t),
$$

and:

$$
dt_\lambda
=
\lambda^{-2}dt.
$$

Thus:

$$
\boxed{
\int
\|\nabla u\|_\infty dt
}
$$

is scale invariant.

Hence:

$$
\boxed{
\mathfrak T^{adj}
}
$$

is scale invariant.

---

# 22. Interaction Efficiency

RFP-06 defines the interaction envelope for the selected bridge entry:

$$
\mathcal Q_n(v,w)
$$

and the positive bridge:

$$
[B_n(v\to w)]_+.
$$

Define:

$$
\boxed{
\mathfrak e_n(v,w)
=
\frac{
[B_n(v\to w)]_+
}{
\mathcal Q_n(v,w)
}
}
$$

when:

$$
\mathcal Q_n(v,w)>0.
$$

We have:

$$
0\le
\mathfrak e_n(v,w)
\le1.
$$

---

# 23. Core Tax 7 — Interaction-Inefficiency Tax

For the active bridge class, define:

$$
\boxed{
\mathfrak T_n^{int}
=
\sup_{(v,w)\in\mathscr B_n^\star}
\frac1{
\mathfrak e_n(v,w)
}.
}
$$

If for some active bridge:

$$
\mathfrak e_n=0,
$$

let:

$$
\mathfrak T_n^{int}=+\infty.
$$

A bounded:

$$
\mathfrak T^{int}
$$

indicates:

> a fixed fraction of the canonical interaction envelope genuinely enters the selected positive bridge direction.

---

# 24. Tax Type Warning

$$
\mathfrak T_n^{int}\to\infty
$$

can indicate:

- cancellation;
- dual misalignment;
- transport depletion;
- interaction geometry unfavorable to the selected source direction.

It is not necessarily a singularity-danger tax.

Therefore:

$$
\boxed{
\mathfrak T^{int}
\text{ is a provenance-efficiency tax, not a monotone danger index}.
}
$$

---

# 25. Commutator Envelope

Following the RFP-04 canonical operator:

$$
\mathcal T_k
=
\Delta_k
\mathbb P\nabla\cdot.
$$

For the tube width parameter:

$$
A_{tube}\ge1,
$$

the RFP-04 commutator estimate and adjoint gradient bound give:

$$
\boxed{
\mathcal Q_n^{com}
\le
C
A_{tube}^{-1}
\mathfrak T_n^{adj}
\mathcal Q_n.
}
$$

Here:

$$
\mathcal Q_n
$$

is the canonical main interaction envelope of the selected source.

---

# 26. C9.6 — Derived Commutator Share Bound

## Theorem 26.1

For an active bridge:

$$
(v,w),
$$

we have:

$$
\boxed{
\frac{
\mathcal Q_n^{com}
}{
[B_n(v\to w)]_+
}
\le
C
A_{tube}^{-1}
\mathfrak T_n^{adj}
\mathfrak T_n^{int}.
}
$$

### Proof

From:

$$
[B]_+
=
\mathfrak e_n\mathcal Q_n
$$

and Section 25:

$$
\frac{
\mathcal Q^{com}
}{
[B]_+
}
\le
C
A_{tube}^{-1}
\mathfrak T^{adj}
\frac1{\mathfrak e_n}.
$$

Then using:

$$
1/\mathfrak e_n
\le
\mathfrak T^{int}.
$$

$\square$

---

# 27. Corollary: Commutator Escape is Not an Independent Primitive Branch

If:

$$
\mathfrak T_n^{adj}
\le K_D,
$$

and:

$$
\mathfrak T_n^{int}
\le K_I,
$$

then for any:

$$
\varepsilon>0
$$

we only need to fix:

$$
\boxed{
A_{tube}
\ge
\frac{
CK_DK_I
}{
\varepsilon
}
}
$$

to ensure the commutator envelope does not exceed the selected positive bridge's:

$$
\varepsilon
$$

fraction.

Therefore:

$$
\boxed{
\text{persistent order-one commutator escape}
}
$$

must force:

$$
\boxed{
\mathfrak T^{adj}
\to\infty
\quad\vee\quad
\mathfrak T^{int}
\to\infty
}
$$

if a sufficiently wide tube is allowed to be chosen once.

---

# 28. Band-Passed Far-Field Envelope

RFP-04 pseudolocality gives:

For any:

$$
N_{dec}>0,
$$

if the source region is at least:

$$
R
$$

output wavelengths away from the output tube,

then:

$$
\boxed{
\mathcal Q_n^{far}(R)
\le
C_{N_{dec}}
(1+R)^{-N_{dec}}
\mathcal Q_n.
}
$$

---

# 29. C9.7 — Derived Far-Field Share Bound

## Theorem 29.1

For an active bridge:

$$
(v,w),
$$

we have:

$$
\boxed{
\frac{
\mathcal Q_n^{far}(R)
}{
[B_n(v\to w)]_+
}
\le
C_{N_{dec}}
(1+R)^{-N_{dec}}
\mathfrak T_n^{int}.
}
$$

$\square$

---

# 30. Corollary: Band-Passed Pressure/Far Escape is Compressed Back into Interaction Tax

If:

$$
\mathfrak T_n^{int}\le K_I,
$$

then for any:

$$
\varepsilon>0
$$

choosing a fixed dimensionless buffer:

$$
\boxed{
R_\varepsilon
\ge
\left(
\frac{
C_{N_{dec}}K_I
}{
\varepsilon
}
\right)^{1/N_{dec}}
}
$$

ensures the canonical band-passed far-source envelope is below the selected positive bridge's:

$$
\varepsilon
$$

share.

Therefore, in the:

$$
\Delta_k\mathbb P\nabla\cdot
$$

packet ledger,

far pressure/source escape is not an independent primitive tax.

---

# 31. Raw Pressure Warning

Section 30 does not imply:

$$
\boxed{
\text{raw pressure is local}.
}
$$

Raw pressure is determined non-locally by:

$$
-\Delta p
=
\partial_i\partial_j(u_iu_j)
$$

far pressure can retain a harmonic component in the local core.

The conclusions of this document only apply to:

$$
\boxed{
\text{canonical output-band-passed Leray source ledger}.
}
$$

Thus, local pressure legality still requires a Bradshaw–Tsai type local pressure framework.

---

# 32. Full Memory Tail

Fix:

$$
0<\varepsilon_{mem}<1/4.
$$

For the child:

$$
w
$$

define the complete old-history tail:

$$
\boxed{
\operatorname{Tail}_{n,w}^{mem}(m)
=
\chi_n^{init}
+
\sum_{h\ge m}
\chi_{n,h}^{age}.
}
$$

---

# 33. Memory Depth Selector

Define:

$$
\boxed{
m_{n,w}(\varepsilon_{mem})
=
\inf
\left\{
m\ge1:
\operatorname{Tail}_{n,w}^{mem}(m)
\le
\varepsilon_{mem}
\right\}.
}
$$

If it does not exist,

let:

$$
m_{n,w}=+\infty.
$$

---

# 34. Core Tax 8 — Memory-Depth Tax

For the canonical strong child class:

$$
\mathcal W_n^\star
$$

define:

$$
\boxed{
\mathfrak T_n^{mem}
=
1+
\sup_{w\in\mathcal W_n^\star}
m_{n,w}(\varepsilon_{mem}).
}
$$

---

# 35. Relation to RFP-08 Viscous-Age Criterion

RFP-08 has proven:

If:

$$
\sum_{h\ge m}
e^{-c\mathfrak a_{n,h}^{vis}}
\mathfrak G_{n,h}
$$

uniformly tends to:

$$
0,
$$

then:

$$
\mathfrak T_n^{mem}
$$

is uniformly bounded.

Therefore:

$$
\boxed{
\mathfrak T^{mem}\to\infty
}
$$

compresses:

- viscous-age congestion;
- old-generation envelope growth;
- persistent initial reservoir contribution.

---

# 36. Normalized Time-Diagonal Rate

Fix:

$$
0<\delta_{fresh}<1/4.
$$

For a fresh-dominant child slot:

$$
\chi_n^{fresh}\ge\delta_{fresh},
$$

RFP-08 defines:

$$
\mathcal S_{n,r},
\qquad
\mathcal C_{n,w}.
$$

Let:

$$
\boxed{
\mathfrak R_{n,w}^{time}
=
\frac{
\|
\mathcal S_{n,r}
\|_{L^\infty(I_n)}
\|
\mathcal C_{n,w}
\|_{L^1(I_n)}
}{
\nu
2^{2r}
P_n^{age}(w)
}.
}
$$

If the fresh share is below:

$$
\delta_{fresh},
$$

this document sets:

$$
\mathfrak R_{n,w}^{time}=0
$$

for tax purposes.

---

# 37. Core Tax 9 — Temporal-Resolution Tax

Define:

$$
\boxed{
\mathfrak T_n^{time}
=
1+
\sup_{w\in\mathcal W_n^\star}
\mathfrak R_{n,w}^{time}.
}
$$

---

# 38. Scaling Audit of Temporal Tax

RFP-08 near-diagonal estimate:

$$
\frac{
|B_n^{near,\ell}|
}{
P_n^{age}
}
\le
\ell
\frac{
\|\mathcal S\|_\infty
\|\mathcal C\|_1
}{
P_n^{age}
}.
$$

Let the normalized lag be:

$$
\boxed{
\lambda
=
\nu2^{2r}\ell.
}
$$

Then:

$$
\boxed{
\frac{
|B_n^{near,\ell}|
}{
P_n^{age}
}
\le
\lambda
\mathfrak R_{n,w}^{time}.
}
$$

Therefore:

$$
\mathfrak R^{time}
$$

is dimensionless and scale invariant.

---

# 39. C9.8 — Uniform Positive-Lag Selector

## Theorem 39.1

If:

$$
\chi_n^{fresh}\ge\delta_{fresh},
$$

and:

$$
\mathfrak T_n^{time}\le K_T,
$$

choose:

$$
\boxed{
\lambda_0
=
\frac{
\delta_{fresh}
}{
2K_T
}.
}
$$

Let:

$$
\ell_0
=
\frac{
\lambda_0
}{
\nu2^{2r}
}.
$$

Then:

$$
\boxed{
[B_n^{sep,\ell_0}]_+
\ge
\frac{
\delta_{fresh}
}{2}
P_n^{age}.
}
$$

### Proof

The near-diagonal absolute contribution is at most:

$$
\lambda_0K_T
P_n^{age}
=
\frac{
\delta_{fresh}
}{2}
P_n^{age}.
$$

And:

$$
[B_n^{fresh}]_+
\ge
\delta_{fresh}P_n^{age}.
$$

Thus, the separated term retains at least half. $\square$

---

# 40. Temporal Congestion is No Longer an Independent Name

If the fresh share remains:

$$
\ge\delta_{fresh},
$$

but there is no separated source bridge with a fixed positive normalized lag,

then:

$$
\boxed{
\mathfrak T_n^{time}\to\infty.
}
$$

Therefore, near-diagonal temporal congestion is completely absorbed into:

$$
\boxed{
\mathfrak T^{time}.
}
$$

---

# 41. Unified Core Tax Vector

The core definition of this document:

$$
\boxed{
\mathbf T_n^{core}
=
\left(
\mathfrak T_n^{atom},
\mathfrak T_n^{bridge},
\mathfrak T_n^{amp},
\mathfrak T_n^{par},
\mathfrak T_n^{depth},
\mathfrak T_n^{adj},
\mathfrak T_n^{int},
\mathfrak T_n^{mem},
\mathfrak T_n^{time}
\right).
}
$$

Define the max tax:

$$
\boxed{
\mathfrak T_n^{max}
=
\max_i
\mathfrak T_{n,i}^{core}.
}
$$

---

# 42. Scaling Audit Summary

The nine core taxes:

$$
\boxed{
\text{are all dimensionless scale-compatible quantities or dimensionless finite-depth counts}.
}
$$

Specifically:

- atomization: probability inverse;
- bridge: probability inverse;
- amplification: ratio;
- parent tax: RFP-04 scale invariant;
- packet depth: relative dyadic moment;
- adjoint: scale-invariant exponential strain integral;
- interaction: efficiency inverse;
- memory: macro-edge count;
- time: normalized parabolic lag-rate ratio.

---

# 43. Bounded-Tax Corridor

A macro ancestry is said to fall within the:

$$
\boxed{
\textbf{bounded-tax corridor}
}
$$

if there exists:

$$
K<\infty
$$

such that for all sufficiently large:

$$
n
$$

satisfies:

$$
\boxed{
\mathfrak T_n^{max}
\le
K.
}
$$

---

# 44. C9.9 — Tax-to-Selector Compiler

## Theorem 44.1

Assume:

$$
\mathfrak T_n^{max}\le K
$$

for all sufficiently large:

$$
n.
$$

Then for any fixed:

$$
0<\varepsilon<1/4
$$

the following parameters can be chosen independent of $n$:

### Strong-Node Count

$$
\boxed{
B_{node}
=
2K.
}
$$

### Active Predecessor Packet Count

$$
\boxed{
B_{pkt}
=
2K^2.
}
$$

### Parent-Gap Radius

$$
\boxed{
L_\varepsilon
=
\left\lceil
\log_2
\left(
\frac{CK}{\varepsilon}
\right)
\right\rceil.
}
$$

### Direct Plateau-Gap Bound

$$
\boxed{
G_{\max}
=
C_\ast
+
\left\lceil
\log_2(2K^3)
\right\rceil.
}
$$

### Tube Width

$$
\boxed{
A_{tube,\varepsilon}
=
\left\lceil
\frac{
CK^2
}{
\varepsilon
}
\right\rceil.
}
$$

### Far-Source Buffer

for any chosen:

$$
N_{dec}>0,
$$

$$
\boxed{
R_{\varepsilon,N_{dec}}
=
\left(
\frac{
C_{N_{dec}}K
}{
\varepsilon
}
\right)^{1/N_{dec}}.
}
$$

### Memory Depth

$$
\boxed{
m_{\max}
\le
K.
}
$$

up to the additive convention in:

$$
\mathfrak T^{mem}=1+m.
$$

### Fresh-Source Normalized Lag

$$
\boxed{
\lambda_{\min}
=
\frac{
\delta_{fresh}
}{
2K
}.
}
$$

### Proof

The respective items follow sequentially from Theorems:

7.1, 14.1, 16.1, 18.1, 26.1, 29.1, as well as tax definitions 34, 37, and Theorem 39.1. $\square$

---

# 45. Significance: Bounded Taxes Yield Uniform Finite Selectors

Theorem 44.1 compiles:

$$
\boxed{
\text{nine a priori moving escape parameters}
}
$$

into:

$$
\boxed{
\text{one fixed finite collection of scale-independent selectors}.
}
$$

Therefore, in the bounded-tax corridor:

- the parent gap cannot drift away;
- the direct plateau gap cannot drift away;
- the tube width does not need to increase indefinitely;
- the far buffer does not need to increase indefinitely;
- the memory depth does not need to increase;
- the fresh-source lag does not need to collapse;
- strong node / packet branching will not explode.

---

# 46. Certificate Compactness, Not Solution Compactness

This document refers to the above result as:

$$
\boxed{
\textbf{uniform certificate compactness}.
}
$$

It does not imply that:

$$
u_n
$$

is automatically precompact in some Banach space.

It merely indicates:

$$
\boxed{
\text{the discrete/relative localization parameters required for the ancestry certificate can be uniformly chosen}.
}
$$

Thus, it must not be conflated with a PDE compactness theorem.

---

# 47. Derived Tax Dependency Graph

Currently, secondary escapes can be compressed into:

$$
\boxed{
\text{parent-gap escape}
\Rightarrow
\mathfrak T^{par}\to\infty,
}
$$

$$
\boxed{
\text{node atomization}
\Rightarrow
\mathfrak T^{atom}\to\infty,
}
$$

$$
\boxed{
\text{bridge bottleneck collapse}
\Rightarrow
\mathfrak T^{bridge}\to\infty,
}
$$

$$
\boxed{
\text{packet amplification escape}
\Rightarrow
\mathfrak T^{amp}\to\infty,
}
$$

$$
\boxed{
\text{packet / plateau depth escape}
\Rightarrow
\mathfrak T^{depth}
\to\infty
\vee
\mathfrak T^{amp}
\to\infty
\vee
\mathfrak T^{bridge}
\to\infty,
}
$$

$$
\boxed{
\text{commutator escape}
\Rightarrow
\mathfrak T^{adj}
\to\infty
\vee
\mathfrak T^{int}
\to\infty,
}
$$

$$
\boxed{
\text{band-passed far-source escape}
\Rightarrow
\mathfrak T^{int}\to\infty
}
$$

for fixed adjustable buffer semantics,

$$
\boxed{
\text{memory-depth escape}
\Rightarrow
\mathfrak T^{mem}\to\infty,
}
$$

and:

$$
\boxed{
\text{temporal congestion}
\Rightarrow
\mathfrak T^{time}\to\infty.
}
$$

---

# 48. C9.10 — Escape-Name Compression Theorem

## Theorem 48.1

Under the certificate semantics currently established in RFP-01--08,

if all nine core taxes are uniformly bounded,

then the following secondary escape labels cannot persist as independent unbounded mechanisms:

- parent-gap escape;
- strong-node atomization;
- bridge bottleneck collapse;
- packet amplification escape;
- strong direct plateau-depth escape;
- commutator leakage escape;
- canonical band-passed far-source escape;
- infinite memory-depth escape;
- near-diagonal temporal congestion.

If any of these escapes persist at the persistence-level,

at least one core tax must diverge.

$\square$

---

# 49. But the Converse Generally Does Not Hold

For example:

$$
\mathfrak T^{int}\to\infty
$$

may represent nonlinear depletion.

Therefore:

$$
\boxed{
\text{core tax divergence}
\not\Rightarrow
\text{dangerous singularity ancestry}.
}
$$

RFP-10 must further distinguish between:

$$
\boxed{
\text{dangerous dynamical escape}
}
$$

and:

$$
\boxed{
\text{certificate / depletion escape}.
}
$$

---

# 50. Bounded-Tax Graph

In the bounded-tax corridor,

take the canonical strong nodes:

$$
\mathcal W_n^\star.
$$

For each strong child,

there is a predecessor bridge floor:

$$
\boxed{
\mathfrak b_n(v,w)
\ge
\frac1{2K}.
}
$$

and the active predecessor packet share is:

$$
q_n(v)
\ge
\frac1{2K^2}.
$$

Thus, each layer of the candidate graph is uniformly finite.

If old/fresh channels exist,

Theorem 44.1 further compiles them into:

- at most $K$ macro-edge memory;
- or fixed normalized positive time lag.

Therefore, a bounded-memory augmented graph can be established.

---

# 51. Augmented Node State

Define the augmented ancestry node:

$$
\boxed{
\widehat v_n
=
\left(
v_n,
m_n,
\lambda_n
\right),
}
$$

where:

$$
0\le m_n\le K
$$

denotes the finite memory offset,

and:

$$
\lambda_n=0
$$

indicates a completed-edge packet,

or:

$$
\lambda_n\ge\lambda_{\min}
$$

indicates a hidden positive-lag subedge.

By the bounded-tax selectors,

the effective discrete ancestry choices at each level remain finite up to the declared tube/source packet indexing rules.

---

# 52. C9.11 — Bounded-Tax Path Closure Theorem

## Theorem 52.1

Assume:

1. The macro first-passage ancestry enters the bounded-tax corridor:
   $$
   \mathfrak T_n^{max}\le K;
   $$
2. The RFP packet/tube representation is complete for the considered singularity ancestry class;
3. For any:
   $$
   N<\infty,
   $$
   there exists a depth-$N$ tax-admissible finite realized ancestry;
4. Pressure / localization uses the canonical band-passed Leray semantics of this document.

Then there exists:

$$
\boxed{
\text{one infinite tax-admissible realized ancestry path}.
}
$$

### Proof

Theorem 44.1 gives uniform:

- finite node count;
- finite predecessor packet count;
- finite parent / plateau gap;
- finite memory depth;
- positive time-lag floor;
- fixed localization buffer and tube width.

Thus, the augmented certificate graph is finitely branching.

By assumption 3, there are arbitrarily deep finite paths.

Apply the RFP-05 finite-branching infinite-path extraction theorem. $\square$

---

# 53. The True Status of this Theorem

Theorem 52.1 is not:

$$
\boxed{
\text{Navier--Stokes Chain Necessity proved}.
}
$$

Because:

- the bounded-tax corridor is not yet proven to be universal;
- representation completeness remains open;
- arbitrarily deep tax-admissible finite realized paths need to be fully derived from the actual blow-up hypothesis.

What it accomplishes is:

$$
\boxed{
\text{if the nine taxes do not escape, the remaining quantifier/selector problem closes}.
}
$$

---

# 54. C9.12 — Finite Core-Tax Escape Alternative

## Theorem 54.1

Assume:

- representation completeness holds;
- the blow-up hypothesis has provided arbitrarily deep finite RFP formation candidates;
- but there is no infinite realized ancestry path.

Then at least one core tax cannot remain uniformly bounded:

$$
\boxed{
\limsup_{n\to\infty}
\mathfrak T_n^{max}
=
\infty.
}
$$

### Proof

Assume for contradiction:

$$
\sup_n
\mathfrak T_n^{max}<\infty.
$$

Then by Theorem 52.1 we obtain an infinite path,

a contradiction. $\square$

---

# 55. This is a Finite Escape Census, Not Finite Obstruction

Theorem 54.1 only yields:

$$
\boxed{
\text{no infinite path}
\Longrightarrow
\text{some tax diverges}.
}
$$

True Finite Obstruction also requires:

$$
\boxed{
\text{every tax divergence is proven dynamically impossible}
}
$$

or at least:

$$
\boxed{
\text{every surviving divergence can be further directed toward contradiction / regularity}.
}
$$

Currently, this step has not been achieved at all.

---

# 56. Tax Vector as a Dynamic State

Therefore, the ancestry state in True ETN / X-Integration can be augmented with:

$$
\boxed{
\Theta_n^{tax}
=
\mathbf T_n^{core}.
}
$$

The complete local formation state now has at least:

$$
\boxed{
\Theta_n
=
\left(
\Theta_n^{bal},
\Theta_n^{op},
\Theta_n^{geo},
\Theta_n^{src},
\Theta_n^{prov},
\Theta_n^{tax}
\right).
}
$$

---

# 57. Tax Provenance

Every tax must preserve:

$$
\boxed{
\operatorname{Prov}
\left(
\mathfrak T_{n,i}
\right)
=
\left\langle
\text{definition},
\text{source ledger},
\text{normalization},
\text{scale audit},
\text{thresholds},
\text{status}
\right\rangle.
}
$$

It must not merely preserve the final scalar.

---

# 58. Threshold Dependence

In this document:

$$
\mathfrak T^{mem}
$$

depends on:

$$
\varepsilon_{mem},
$$

and:

$$
\mathfrak T^{time}
$$

depends on:

$$
\delta_{fresh}.
$$

These thresholds must belong to the certificate metadata,

and cannot silently change between different edges.

Added:

$$
\boxed{
G_{\rm TAXTHRESH}.
}
$$

---

# 59. Tax Vector Cannot be Arbitrarily Scalarized

Generally, one cannot assume:

$$
\boxed{
\mathfrak T^{total}
=
\sum_i
\mathfrak T_i
}
$$

possesses intrinsic PDE meaning.

Different taxes:

- have different types;
- have different monotonicities;
- some divergences may be regularizing;
- some are merely certificate loss.

Thus, the first version only preserves the:

$$
\boxed{
\mathbf T_n^{core}
}
$$

vector.

If aggregation is needed,

one can only use a task-specific monotone operator:

$$
\mathcal A_{\rm task}
\left(
\mathbf T_n^{core}
\right).
$$

---

# 60. Tax Partial Order

Define the componentwise order:

$$
\boxed{
\mathbf T
\preceq
\mathbf S
}
$$

if every core coordinate:

$$
T_i\le S_i.
$$

If a certificate theorem is monotone with respect to taxes,

then:

$$
\mathbf S
$$

the parameter choice certified by it also applies to:

$$
\mathbf T.
$$

This equips the tax space with a natural upward-danger / loss-of-control partial order,

but not a blow-up probability order.

---

# 61. Tax Fixed Corridor

For:

$$
K<\infty,
$$

define:

$$
\boxed{
\mathfrak C_K
=
\left\{
\mathbf T:
\mathfrak T^{max}\le K
\right\}.
}
$$

Theorem 44.1 generates for each:

$$
\mathfrak C_K
$$

a set of fixed selectors.

Therefore:

$$
\boxed{
\mathfrak C_K
}
$$

is a certificate-level compact corridor.

---

# 62. Escape to the Boundary

If:

$$
\mathfrak T_n^{max}\to\infty,
$$

we say:

$$
\boxed{
\mathbf T_n
\to
\partial_\infty
\mathfrak T
}
$$

meaning the tax state escapes to the noncompact boundary.

The task of RFP-10 is to study:

$$
\boxed{
\text{which boundary faces are dynamically realizable?}
}
$$

---

# 63. Boundary Faces

The first version of boundary faces:

$$
\boxed{
F_{atom},
F_{bridge},
F_{amp},
F_{par},
F_{depth},
F_{adj},
F_{int},
F_{mem},
F_{time}.
}
$$

Multiple coordinates can diverge simultaneously,

so the true escape may fall on face intersections:

$$
F_i\cap F_j,
$$

or even higher-codimension corners.

---

# 64. Why is this Better than a Long List of Branches?

The old branch language:

$$
\text{pressure escape},
\quad
\text{commutator escape},
\quad
\text{plateau escape},
\quad
\text{memory escape},
\ldots
$$

easily double-counts the same phenomenon.

For example, this document has proven:

$$
\text{commutator escape}
$$

under canonical semantics actually falls into:

$$
F_{adj}
\cup
F_{int}.
$$

And:

$$
\text{far-source escape}
$$

falls into:

$$
F_{int}
$$

or raw-pressure representation outside the canonical packet ledger.

Therefore, tax boundary geometry avoids branch duplication.

---

# 65. Standard PDE Calibration I: Pressure Locality

Bradshaw–Tsai's local pressure expansion theorem demonstrates:

there is a precise relationship between the local pressure expansion and the mildness of whole-space distributional N–S solutions.

This supports the hard rule of this document:

$$
\boxed{
\text{raw pressure localization requires independent legality and cannot be replaced by band-passed pseudolocality.}
}
$$

---

# 66. Standard PDE Calibration II: Localization Forcing

In the 2026 Barker–Popkin forced Navier–Stokes quantitative theory,

localization induces forcing,

and forcing is amplified at the large scales of Carleman estimates,

requiring additional Caccioppoli-type control.

This supports that:

$$
\boxed{
\mathfrak T^{adj}
}
$$

and the localization / commutator tax must be accounted for independently,

and cannot be automatically declared harmless just because the cutoff is smooth.

---

# 67. Standard PDE Calibration III: Interaction Depletion

Miller's work on strain–vorticity interaction proves:

certain nonlinearity components that appear orthogonal to the enstrophy growth pairing can still strongly alter the dynamics,

and advection can deplete nonlinearity under specific criteria.

Therefore:

$$
\boxed{
\mathfrak T^{int}\to\infty
}
$$

may be:

$$
\boxed{
\text{certificate inefficiency}
}
$$

or even:

$$
\boxed{
\text{regularizing depletion},
}
$$

rather than a dangerous escape.

---

# 68. Standard PDE Calibration IV: Frequency Window

Bradshaw–Grujic frequency-localized regularity criteria show:

possible singularity formation involves a relevant frequency window whose lower endpoint drifts toward:

$$
+\infty
$$

This is compatible with:

$$
\mathfrak T^{par},
\quad
\mathfrak T^{depth}
$$

acting as scale-relative taxes,

but this criterion does not provide an ancestry genealogy.

---

# 69. 2026 Finite-Ledger Calibration

The 2026 finite-scale critical-ledger and structural-audit works have written persistent badness as:

$$
\boxed{
\text{supply}
+
\text{tax}
+
\text{leakage}
}
$$

and explicitly pointed out that current obstruction calculus still lacks coercive estimates to rule out surviving obstructions.

RFP-09 is compatible with this:

What this document unifies is:

$$
\boxed{
\text{formation certificate taxes},
}
$$

it does not claim to have obtained a coercive regularity inequality.

---

# 70. New Guards

Added:

### $G_{\rm TAXTYPE}$

Tax divergence must not be automatically termed a dangerous mechanism.

### $G_{\rm TAXTHRESH}$

Tax threshold metadata such as memory / time must not silently change.

### $G_{\rm TAXVEC}$

The tax vector must not be scalarized into a total score without justification.

### $G_{\rm RAWPRESS}$

Band-passed far-field control must not be conflated with raw pressure locality.

### $G_{\rm DERIVED}$

If derived taxes such as commutator / far-field are already controlled by a primitive tax,

they must not be double-counted as independent escape dimensions.

---

# 71. Guard Library v8

Therefore:

$$
\boxed{
\mathcal G_{NS}^{(8)}
=
\mathcal G_{NS}^{(7)}
\cup
\{
G_{\rm TAXTYPE},
G_{\rm TAXTHRESH},
G_{\rm TAXVEC},
G_{\rm RAWPRESS},
G_{\rm DERIVED}
\}.
}
$$

---

# 72. RFP-09 Verdict on Chain Necessity

Up to this document,

if the formation ancestry remains entirely within the finite tax corridor:

$$
\boxed{
\sup_n
\mathfrak T_n^{max}
<
\infty,
}
$$

then:

- scale gaps are uniform;
- packet branching is uniformly finite;
- localization buffers are uniform;
- memory depth is finite;
- fresh time lag is positive;
- pressure/far packet leakage can be uniformly controlled;
- quantifier closure can be handed over to RFP-05.

Therefore:

$$
\boxed{
\text{bounded taxes}
\Longrightarrow
\text{certificate-level ancestry compactness}.
}
$$

If a complete ancestry still cannot form,

under completeness assumptions there must be:

$$
\boxed{
\text{at least one core tax divergence}.
}
$$

---

# 73. The True Next Step

Thus, RFP-10 no longer needs to re-advance the ancestry syntax.

It should perform:

$$
\boxed{
\textbf{Guard Library Consolidation}
+
\textbf{Tax-Boundary Escape Census}
+
\textbf{Finite Obstruction Candidates}.
}
$$

The true question becomes:

> Among the nine boundary faces, which are known to be regularizable?
> Which might be dangerous?
> Which can be ruled out by energy / strain / pressure / viscosity inequalities?
> Does there exist a finite family of dynamically complete obstructions hitting every tax-boundary escape?

---

# 74. Formal Status Ledger

$$
\boxed{
\begin{aligned}
\text{typed core tax vector}
&:\ \mathrm{DEFINED},\\
\text{strong-node finite bound}
&:\ \mathrm{PROVED},\\
\text{active packet strength / count}
&:\ \mathrm{PROVED},\\
\text{uniform parent-gap selector}
&:\ \mathrm{PROVED},\\
\text{plateau-gap tax bound}
&:\ \mathrm{PROVED},\\
\text{adjoint tax scaling}
&:\ \mathrm{PROVED},\\
\text{commutator share from adjoint + efficiency taxes}
&:\ \mathrm{PROVED\ within\ RFP\ envelope\ semantics},\\
\text{band-passed far-source share from efficiency tax}
&:\ \mathrm{PROVED},\\
\text{full memory-depth tax}
&:\ \mathrm{DEFINED},\\
\text{temporal-resolution tax}
&:\ \mathrm{DEFINED/SCALE\ AUDITED},\\
\text{uniform positive-lag selector}
&:\ \mathrm{PROVED},\\
\text{tax-to-selector compiler}
&:\ \mathrm{PROVED},\\
\text{escape-name compression}
&:\ \mathrm{PROVED\ relative\ to\ current\ RFP\ semantics},\\
\text{bounded-tax path closure}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{finite core-tax escape alternative}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{universal boundedness of core taxes}
&:\ \mathrm{OPEN},\\
\text{dynamic meaning of each divergent tax face}
&:\ \mathrm{OPEN},\\
\text{representation completeness}
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

# 75. Conclusion

RFP-09 compresses the massive number of escape branches accumulated in RFP-01--08 into nine core taxes:

$$
\boxed{
\mathbf T_n^{core}
=
\left(
\mathfrak T^{atom},
\mathfrak T^{bridge},
\mathfrak T^{amp},
\mathfrak T^{par},
\mathfrak T^{depth},
\mathfrak T^{adj},
\mathfrak T^{int},
\mathfrak T^{mem},
\mathfrak T^{time}
\right).
}
$$

Among them:

$$
\boxed{
\text{commutator}
}
$$

is no longer an independent primitive escape,

because bounded:

$$
\mathfrak T^{adj},
\quad
\mathfrak T^{int}
$$

allow a fixed tube width to make it uniformly small.

Similarly,

canonical band-passed:

$$
\boxed{
\text{pressure / far-source leakage}
}
$$

under bounded:

$$
\mathfrak T^{int}
$$

can be uniformly suppressed using a fixed wavelength buffer.

Bounded:

$$
\mathfrak T^{par}
$$

gives uniform parent tightness;

Bounded:

$$
\mathfrak T^{bridge},
\quad
\mathfrak T^{amp},
\quad
\mathfrak T^{depth}
$$

gives finite packet branching and bounded direct plateau gap;

Bounded:

$$
\mathfrak T^{mem}
$$

gives finite generation memory;

Bounded:

$$
\mathfrak T^{time}
$$

converts fresh source into a fixed normalized positive-lag ancestry.

Therefore:

$$
\boxed{
\sup_n
\mathfrak T_n^{max}
<
\infty
}
$$

generates a uniform certificate corridor.

When representation completeness and arbitrarily deep finite realization hold,

the RFP-05 compactness engine extracts:

$$
\boxed{
\text{one infinite realized ancestry path}.
}
$$

Thus, if the infinite ancestry still fails,

at least one core tax must escape to:

$$
+\infty.
$$

This is not Finite Obstruction.

But for the first time, it compresses:

$$
\boxed{
\text{"Where else can the singularity formation escape?"}
}
$$

into a finite-dimensional tax-boundary census:

$$
\boxed{
F_{atom},
F_{bridge},
F_{amp},
F_{par},
F_{depth},
F_{adj},
F_{int},
F_{mem},
F_{time}.
}
$$

The next document truly begins to investigate:

$$
\boxed{
\text{which boundary faces are dynamically realizable, regularizing, or excludable?}
}
$$

This is RFP-10.

---

# References

1. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, Journal of Mathematical Fluid Mechanics 24 (2022); arXiv:2001.11526.
2. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026).
3. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263–273; arXiv:1102.1944.
6. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026).
7. R. Yu, *Finite-Window Recursive Audit Chains for Navier–Stokes Generated Packages*, arXiv:2606.20899 (2026).
8. R. Yu, *A Structural Audit of Navier–Stokes Obstruction Calculus*, arXiv:2606.25341 (2026).

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_RFP_03_DualWitness_ParentLedger_CarrierEscape_v0.1.md`
- `NS_RFP_04_SpatialTube_PressureCompatible_UniformParentTightness_v0.1.md`
- `NS_RFP_05_WitnessPersistence_FiniteBranching_InfinitePath_v0.1.md`
- `NS_RFP_06_InterEdgeBridge_SourceStock_Bottleneck_v0.1.md`
- `NS_RFP_07_SynchronousPlateau_CarrierDepth_FastFront_v0.1.md`
- `NS_RFP_08_MemoryDepth_TimeResolution_PacketClosure_PlateauBridge_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 10 — Guard Library Consolidation, Tax-Boundary Escape Census, and Finite Obstruction Candidates}
}
$$