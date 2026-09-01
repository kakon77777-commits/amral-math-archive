---
title: "Navier–Stokes Ancestry Necessity Program 03: Source-Parent Recapture, Kernel-Inflated Footprints, Weighted Parent-State Extraction and C3 Causal Upgrade"
short_title: "NS-ANP 03"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style weighted source-parent recapture / conditional C3 causal upgrade"
epistemic_status: "Absorbs Littlewood-Paley spatial nonlocality into an explicit kernel-inflated causal footprint with conserved mass, preserved centroid, and controlled aperture. Proves a projected-source localization inequality that bounds a child shell source contribution by the child weighted state and a parent-product state measured on the inflated footprint. For a dyadic bilinear source atom, a strong source contribution plus bounded child residence and bounded partner-amplitude action yields a quantitatively nontrivial earlier weighted high-parent state. The parent weight is an explicit provenance-preserving translation of the child footprint and remains recursively admissible; thus such source atoms upgrade from C2+REC-F to a genuine weighted C3 causal parent edge. If the partner-amplitude action is large, the edge enters an already tracked driver/dissipation action branch rather than a provenance failure. Hard-ball compact parent localization is not proved; the C3 upgrade is for the weighted pseudolocal Footprint Node class. Full Chain Necessity, non-Type-I entry, Finite Obstruction, and Navier-Stokes regularity remain OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 03

# Source-Parent Recapture, Kernel-Inflated Footprints, Weighted Parent-State Extraction and C3 Causal Upgrade

## 0. Context of this Paper

ANP-02 proved:

$$
\boxed{
\mathrm{REC\mbox{-}F}
:
\text{footprint/state representation recursion}
=
\mathrm{PROVED},
}
$$

and reduced geometric parent localization to:

$$
\boxed{
\text{LOCAL-PARENT}
\vee
R_{\rm PLEAK}.
}
$$

The unresolved issue was:

> can the nonlinear source packet itself produce an earlier quantitatively nontrivial parent state that belongs to the same causal branch and can be recursively reused?

This paper proves a weighted version of that statement.

The key conceptual move is:

$$
\boxed{
\text{do not force the parent into the identical hard ball};
}
$$

instead, absorb the finite spatial nonlocality of the dyadic projector into an explicit **kernel-inflated causal footprint**.

This converts pseudolocal leakage from an untyped external defect into a controlled representation map.

---

# 1. Dyadic kernel envelope

Let:

$$
\Delta_k f
=
K_k*f,
$$

where:

$$
K_k(x)
=
2^{3k}K(2^kx)
$$

is a real even Schwartz kernel.

Choose an even nonnegative Schwartz function:

$$
\kappa
$$

with:

$$
\int\kappa=1,
$$

finite second moment:

$$
\sigma_\kappa^2
=
\int|z|^2\kappa(z)dz
<
\infty,
$$

and:

$$
\boxed{
|K(z)|
\le
C_K
\kappa(z).
}
$$

Set:

$$
\kappa_k(x)
=
2^{3k}\kappa(2^kx).
$$

---

# 2. Kernel-inflation map

For any nonnegative footprint:

$$
0\le\chi\le1,
$$

define:

$$
\boxed{
\mathsf I_k[\chi]
=
\chi^{[k]}
=
\kappa_k*\chi.
}
$$

Since:

$$
\kappa_k
$$

is a probability kernel:

$$
\boxed{
0\le
\chi^{[k]}
\le1.
}
$$

---

# 3. CIV-3.1 — Kernel-Inflation Geometry

## Theorem 3.1

Let:

$$
m
=
\int\chi dx,
$$

and let:

$$
c_\chi
=
\frac1m
\int x\chi dx.
$$

Then:

$$
\boxed{
\int\chi^{[k]}dx
=
m,
}
$$

$$
\boxed{
c_{\chi^{[k]}}
=
c_\chi,
}
$$

and:

$$
\boxed{
\int
|x-c_\chi|^2
\chi^{[k]}(x)dx
=
\int
|x-c_\chi|^2
\chi(x)dx
+
m
\sigma_\kappa^2
2^{-2k}.
}
$$

### Proof

Mass follows from Fubini and:

$$
\int\kappa_k=1.
$$

The centroid is preserved because:

$$
\kappa_k
$$

is even and has zero first moment.

The second-moment identity follows by expanding:

$$
|y+z-c_\chi|^2
$$

under convolution and using the zero first moment.

$\square$

---

# 4. Aperture consequence

Suppose:

$$
m\asymp R^3,
$$

and:

$$
A_\chi^2
=
\frac1{mR^2}
\int
|x-c_\chi|^2\chi dx.
$$

Then:

$$
\boxed{
A_{\chi^{[k]}}^2
=
A_\chi^2
+
\sigma_\kappa^2
(2^kR)^{-2}.
}
$$

Thus whenever:

$$
\boxed{
2^kR
\ge
c_0>0,
}
$$

kernel inflation preserves a uniformly controlled footprint aperture.

---

# 5. Why this changes the leakage problem

ANP-02 treated source parent outside a hard enlarged ball as possible:

$$
R_{\rm PLEAK}.
$$

But a dyadic projector is not compactly supported in physical space.

Its actual locality object is its Schwartz kernel.

The canonical parent footprint should therefore be:

$$
\boxed{
\chi^{[k]},
}
$$

not the original hard cutoff.

Remote influence is then not hidden.

It is weighted by exactly the spatial envelope required by the projector.

---

# 6. Child shell weighted energy

For:

$$
\omega_k
=
\Delta_k\omega,
$$

define:

$$
\boxed{
e_k^\chi(s)
=
\frac12
\int
\chi(s,x)
|\omega_k(s,x)|^2dx.
}
$$

Let:

$$
F
$$

be any source field entering a projected shell:

$$
\Delta_kF.
$$

---

# 7. CIV-3.2 — Projected Source / Inflated-Footprint Inequality

## Theorem 7.1

For every time:

$$
s<T_\ast,
$$

$$
\boxed{
\left|
\int
\chi
\,
\omega_k
\cdot
\Delta_kF
\,dx
\right|
\le
C_K
\left(
2e_k^\chi
\right)^{1/2}
\left(
\int
\chi^{[k]}
|F|^2dx
\right)^{1/2}.
}
$$

### Proof

By self-adjointness:

$$
\int
\chi\omega_k\cdot\Delta_kF
=
\int
F\cdot
\Delta_k(\chi\omega_k).
$$

The kernel envelope gives:

$$
|\Delta_k(\chi\omega_k)(x)|
\le
C_K
\int
\kappa_k(x-y)
\chi(y)
|\omega_k(y)|dy.
$$

Cauchy--Schwarz inside the convolution gives:

$$
|\Delta_k(\chi\omega_k)(x)|
\le
C_K
\left(
\chi^{[k]}(x)
\right)^{1/2}
\left(
\kappa_k*
(
\chi|\omega_k|^2
)
(x)
\right)^{1/2}.
$$

Apply Cauchy--Schwarz in:

$$
x.
$$

Finally:

$$
\int
\kappa_k*
(
\chi|\omega_k|^2
)
dx
=
\int
\chi|\omega_k|^2dx
=
2e_k^\chi.
$$

$\square$

---

# 8. Meaning of Theorem 7.1

A projected source contribution to a terminal-core shell does not require a hard support statement about its parent source.

It is exactly controlled by a parent-product state measured on the kernel-inflated footprint:

$$
\boxed{
\chi^{[k]}.
}
$$

Thus Littlewood--Paley nonlocality is translated into a controlled footprint enlargement.

---

# 9. Bilinear parent source

Consider a dyadic bilinear source atom:

$$
\boxed{
F_{p,q}
=
A_pB_q,
}
$$

where:

- $A_p$ is one dyadic parent field;
- $B_q$ is the partner field.

For vortex stretching one may take:

$$
A_p=S_p,
\qquad
B_q=\omega_q,
$$

or reverse the role of the two factors in the envelope estimate.

The scale-transfer commutator is decomposed into analogous dyadic paraproduct atoms.

---

# 10. Canonical high parent

Let:

$$
\boxed{
h
=
\max\{p,q\}.
}
$$

Fourier support for an output shell:

$$
k
$$

implies:

$$
\boxed{
h
\ge
k-C_{\rm LP}.
}
$$

The parent state node will be attached to this high frequency.

---

# 11. High-parent weighted state

If the high parent is already a vorticity block:

$$
\omega_h,
$$

define:

$$
\boxed{
E_h^{\psi}(s)
=
\frac12
\int
\psi(s,x)
|\omega_h(s,x)|^2dx.
}
$$

If the high parent is a strain block:

$$
S_h,
$$

band-passed strain/vorticity equivalence is implemented by one additional kernel inflation.

Namely, for a positive footprint:

$$
\psi,
$$

there exists a positive even Schwartz envelope:

$$
\widetilde\kappa_h
$$

such that:

$$
\boxed{
\int
\psi
|S_h|^2
\le
C
\int
\mathsf I_h[\psi]
|\omega_h|^2.
}
$$

Thus in both cases a high parent is represented by vorticity energy under at most two explicit kernel inflations.

---

# 12. Parent footprint

Define:

$$
\boxed{
\psi_{k,h}
=
\mathsf I_h
\mathsf I_k
[\chi].
}
$$

Since:

$$
h\ge
k-C_{\rm LP},
$$

if:

$$
2^kR
\gtrsim1,
$$

then:

$$
2^{-h}
\lesssim
R.
$$

By Theorem 3.1:

$$
\boxed{
A_{\psi_{k,h}}^2
\le
A_\chi^2
+
C.
}
$$

Mass and centroid remain unchanged.

Thus the high-parent weight belongs to the same controlled footprint class.

---

# 13. Partner amplitude

For a bilinear source atom choose the lower/amplifying factor as:

$$
L_{p,q}(s)
$$

so that:

$$
\boxed{
\left(
\int
\chi^{[k]}
|F_{p,q}|^2
\right)^{1/2}
\le
C
L_{p,q}(s)
\left(
E_h^{\psi_{k,h}}(s)
\right)^{1/2}.
}
$$

Typical choices are:

$$
L_{p,q}
=
\|S_p\|_\infty
$$

or:

$$
L_{p,q}
=
\|\omega_q\|_\infty,
$$

depending on which factor is assigned as the high-parent state.

---

# 14. Pointwise parent envelope

Theorems 7.1 and Section 13 give:

$$
\boxed{
\left|
\int
\chi
\omega_k\cdot
\Delta_kF_{p,q}
\right|
\le
C
\left(
e_k^\chi
\right)^{1/2}
L_{p,q}
\left(
E_h^{\psi_{k,h}}
\right)^{1/2}.
}
$$

This is the adjoint-footprint analogue of the DRC source/state envelope.

---

# 15. Source atom over a causal interval

Let:

$$
I=[t_i,t_j].
$$

Define the realized signed source atom:

$$
\boxed{
\Lambda_{k;p,q}^{\chi}
=
\int_I
\int
\chi
\omega_k\cdot
\Delta_kF_{p,q}
\,dx\,ds.
}
$$

Let the child endpoint energy be:

$$
\boxed{
E_c
=
e_k^\chi(t_j)
>
0.
}
$$

---

# 16. Child residence ratio

Define:

$$
\boxed{
\mathfrak H_c
=
\operatorname*{ess\,sup}_{s\in I}
\frac{
e_k^\chi(s)
}{
E_c
}.
}
$$

This is the shellwise weighted-state analogue of the DRC residence ratio.

---

# 17. Partner action

Define:

$$
\boxed{
\mathcal A_{p,q}(I)
=
\int_I
L_{p,q}(s)ds.
}
$$

This is dimensionless for the vorticity/strain amplitude factors used above.

Large:

$$
\mathcal A_{p,q}
$$

is not a provenance failure.

It is an amplitude/driver action branch.

---

# 18. CIV-3.3 — Weighted Parent-State Extraction

## Theorem 18.1

Assume:

$$
\boxed{
|\Lambda_{k;p,q}^{\chi}|
\ge
\eta
E_c
}
$$

for some:

$$
\eta>0.
$$

If:

$$
0<
\mathcal A_{p,q}(I)
<
\infty,
$$

then there exists:

$$
s_p\in I
$$

such that:

$$
\boxed{
E_h^{\psi_{k,h}}(s_p)
\ge
c
\frac{
\eta^2
}{
\mathfrak H_c
\mathcal A_{p,q}(I)^2
}
E_c.
}
$$

### Proof

The pointwise parent envelope gives:

$$
|\Lambda|
\le
C
\int_I
\sqrt{
e_k^\chi
}
L_{p,q}
\sqrt{
E_h^{\psi}
}
ds.
$$

Use:

$$
e_k^\chi(s)
\le
\mathfrak H_cE_c.
$$

Then:

$$
|\Lambda|
\le
C
\sqrt{
\mathfrak H_cE_c
}
\int_I
L_{p,q}
\sqrt{
E_h^\psi
}
ds.
$$

Cauchy--Schwarz with measure:

$$
L_{p,q}(s)ds
$$

gives:

$$
|\Lambda|^2
\le
C
\mathfrak H_cE_c
\mathcal A_{p,q}
\int_I
L_{p,q}
E_h^\psi ds.
$$

Using:

$$
|\Lambda|
\ge
\eta E_c,
$$

$$
\int_I
L_{p,q}
E_h^\psi ds
\ge
c
\frac{
\eta^2
}{
\mathfrak H_c
\mathcal A_{p,q}
}
E_c.
$$

Divide by:

$$
\mathcal A_{p,q}
$$

and select a time:

$$
s_p
$$

above the weighted average.

$\square$

---

# 19. Quantitative parent ratio

Define:

$$
\boxed{
\eta_{\rm par}
=
\frac{
E_h^{\psi_{k,h}}(s_p)
}{
E_c
}.
}
$$

Then:

$$
\boxed{
\eta_{\rm par}
\ge
c
\frac{
\eta^2
}{
\mathfrak H_c
\mathcal A_{p,q}^2
}.
}
$$

Thus bounded child residence and bounded partner action convert a strong source atom into a quantitatively nontrivial earlier high-parent state.

---

# 20. Parent Footprint Node

Define:

$$
\boxed{
\mathsf P
=
(
s_p,
\psi_{k,h}(s_p),
\omega(s_p),
\mathbf e^{\psi_{k,h}}(s_p),
h,
\operatorname{Prov}_{child\to parent}
).
}
$$

The provenance identifier records:

1. terminal-core provenance inherited from:
   $$
   \chi;
   $$
2. dyadic source shell:
   $$
   k;
   $$
3. explicit kernel-inflation maps:
   $$
   \mathsf I_k,
   \mathsf I_h;
   $$
4. selected parent scale:
   $$
   h.
   $$

No hidden representation switch occurs.

---

# 21. CIV-3.4 — Parent Footprint Legality

## Theorem 21.1

Assume:

$$
2^kR
\gtrsim1,
$$

and:

$$
h\ge k-C_{\rm LP}.
$$

Then the Parent Footprint Node:

$$
\mathsf P
$$

has:

1. finite conserved footprint mass;
2. the same centroid as the child footprint at:
   $$
   s_p;
   $$
3. aperture bounded by:
   $$
   A_{\rm child}^2+C;
   $$
4. the same underlying Navier--Stokes solution;
5. an explicit representation/provenance transition map;
6. a nontrivial high-parent state lower bound from Theorem 18.1.

Therefore:

$$
\boxed{
\mathsf P
}
$$

is a legal recursively reusable weighted ancestry node.

$\square$

---

# 22. Recursive propagation of the parent node

Once:

$$
\mathsf P
$$

is selected at:

$$
s_p,
$$

use its own footprint:

$$
\psi_{k,h}(s_p)
$$

as terminal data for the adjoint equation on earlier times.

ANP-02's adjoint semigroup theorem then applies from:

$$
s_p
$$

backward.

Thus the parent node has the same canonical recursive semantics as every other Footprint Node.

---

# 23. CIV-3.5 — Weighted REC-S Theorem

## Theorem 23.1

For a strong bilinear source atom satisfying:

$$
|\Lambda_{k;p,q}^{\chi}|
\ge
\eta E_c,
$$

with finite:

$$
\mathfrak H_c,
$$

and finite nonzero:

$$
\mathcal A_{p,q}(I),
$$

there exists an earlier legal Parent Footprint Node:

$$
\mathsf P
$$

with quantitative state ratio:

$$
\eta_{\rm par}>0.
$$

The node is recursively reusable under the ANP Footprint Node semantics.

Define this property as:

$$
\boxed{
\mathrm{REC\mbox{-}S}^{W}.
}
$$

Then:

$$
\boxed{
\mathrm{REC\mbox{-}S}^{W}
:
\mathrm{PROVED}
}
$$

for the selected strong source atom.

$\square$

---

# 24. C3 causal upgrade

ANP-00 defines:

$$
C3
$$

as a forward PDE causal contribution with:

- same-branch provenance;
- recursive parent legality.

For the selected strong source atom:

- forward PDE source relevance: PASS;
- terminal-core provenance: PASS;
- parent scale: PASS;
- kernel-inflated spatial provenance: PASS;
- explicit representation transition: PASS;
- recursive parent legality: PASS.

Therefore:

$$
\boxed{
\mathsf{CAUSE}
=
C3
}
$$

for this weighted source-parent edge.

---

# 25. CIV-3.6 — Weighted C3 Source-Parent Theorem

## Theorem 25.1

Under the hypotheses of Theorem 23.1:

$$
\boxed{
\mathsf P
\overset{C3}{\longrightarrow}
\mathsf C
}
$$

where:

$$
\mathsf C
$$

is the child Footprint Node carrying:

$$
E_c.
$$

The edge is:

- pre-singularity;
- forward in physical time;
- quantitatively source-relevant;
- provenance-certified;
- scale-resolved;
- spatially represented by controlled kernel-inflated footprints;
- recursively reusable.

### Safety

This is a weighted pseudolocal C3 ancestry edge.

It does not assert that the parent is contained in one fixed hard ball.

$\square$

---

# 26. Hard-ball locality versus weighted locality

Define:

### $C3_W$

Weighted pseudolocal C3 provenance.

Status:

$$
\boxed{
\mathrm{PROVED}
}
$$

for strong selected source atoms.

### $C3_B$

Hard-ball compact same-core C3 provenance.

Status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

The ANP causal ontology does not require:

$$
C3_B
$$

if:

$$
C3_W
$$

retains controlled spatial aperture, explicit provenance, and recursive legality.

Hard-ball locality is a stronger optional theorem.

---

# 27. Reclassification of R-PLEAK

The old leakage residual:

$$
R_{\rm PLEAK}
$$

arose from comparing a noncompact dyadic kernel with a hard spatial cutoff.

In the canonical weighted node class, kernel tails are encoded by:

$$
\mathsf I_k[\chi].
$$

Thus:

$$
\boxed{
R_{\rm PLEAK}
}
$$

is not an independent **representation/provenance obstruction**.

It is absorbed into the parent footprint.

A large remote parent state simply appears as large weighted parent stock in the noncompact but controlled footprint.

---

# 28. What may still fail

Theorem 25.1 requires a selected strong source atom.

A complete source packet may instead exhibit:

1. many individually weak parent atoms;
2. large partner-amplitude action;
3. action concentrated in already tracked dissipation/driver regimes.

These are not newly created provenance defects.

They belong to the DRC source/action census.

---

# 29. Partner-action alternative

Fix:

$$
A_0<\infty.
$$

For a strong source atom:

### STATE-PARENT

$$
\boxed{
\mathcal A_{p,q}
\le
A_0
}
$$

gives:

$$
\boxed{
\eta_{\rm par}
\ge
c
\eta^2/
(
\mathfrak H_cA_0^2
).
}
$$

### ACTION-PARENT

$$
\boxed{
\mathcal A_{p,q}
>
A_0.
}
$$

Then the edge has paid a quantitative parent-amplitude action packet.

Depending on its scale relative to:

$$
Q(t),
$$

this is routed to:

- low-mode driver action;
- dissipation-boundary transition;
- or high-frequency state action already classified in DRC.

Thus ACTION-PARENT is not a source-provenance failure.

---

# 30. Finite-carrier interface

DRC-02--04 developed signed parent ledgers and cancellation-robust finite parent-shell extraction outside classified multiplicity/dissipation branches.

When that finite-carrier interface supplies a strong dyadic source atom, Theorem 25.1 upgrades it to a weighted C3 parent edge.

Therefore:

$$
\boxed{
\text{DRC finite source carrier}
+
\text{ANP kernel-inflated recapture}
\Longrightarrow
C3_W.
}
$$

This is a cross-cycle compiler theorem.

---

# 31. CIV-3.7 — DRC-to-ANP C3 Compiler

## Theorem 31.1

Suppose a renewal/source node satisfies:

1. DRC finite-carrier selection provides a strong source atom with:
   $$
   |\Lambda|
   \ge
   \eta E_c;
   $$
2. child residence:
   $$
   \mathfrak H_c
   \le
   H_0;
   $$
3. partner action:
   $$
   \mathcal A_{p,q}
   \le
   A_0;
   $$
4. output scale is at or above the causal core scale:
   $$
   2^kR
   \gtrsim1.
   $$

Then the source edge admits a legal weighted C3 parent node with:

$$
\boxed{
\eta_{\rm par}
\ge
c
\frac{
\eta^2
}{
H_0A_0^2
}.
}
$$

$\square$

---

# 32. Current source-parent semantics

The source-parent problem is therefore no longer:

> can a remote field influence the local projected output?

It can.

The correct question is:

> can that influence be encoded in a controlled recursively legal causal footprint with quantitative parent state?

For strong source atoms the answer is:

$$
\boxed{
\textbf{Yes.}
}
$$

---

# 33. Causal Atom audit

For a weighted C3 source-parent edge:

### ST

PASS.

### REL

SRC / EVO / SCALE / PROV.

### EX

- solution: PASS;
- child node: PASS;
- source atom: PASS;
- parent node: PASS;
- recursive parent legality: PASS.

### DEF

Canonical Footprint Node with explicit kernel-inflation translation.

### JUD

- time: PASS;
- hypotheses: PASS;
- PDE: PASS;
- representation: PASS;
- kernel error: absorbed exactly into footprint envelope;
- provenance: PASS;
- recursion: PASS.

### DYN

Exact vorticity shell/source dynamics.

### NUM

Includes:

$$
\eta,
\quad
\eta_{\rm par},
\quad
\mathfrak H_c,
\quad
\mathcal A_{p,q},
\quad
A_\chi,
\quad
A_{\psi_{k,h}},
\quad
2^kR.
$$

---

# 34. Continuity/discreteness

The child and parent Footprint Nodes are connected through:

- continuous Navier--Stokes evolution;
- continuous adjoint propagation;
- discrete dyadic source labels;
- explicit kernel-inflation translation maps.

Thus hybrid legality is preserved.

---

# 35. Coupling

### Equation coupling

Exact.

### Source amplitude coupling

Quantified by:

$$
\eta.
$$

### Parent state coupling

Quantified by:

$$
\eta_{\rm par}.
$$

### Spatial coupling

Kernel-inflated controlled aperture.

### Scale coupling

$$
h\ge k-C_{\rm LP}.
$$

### Provenance coupling

Explicit composition of adjoint provenance and inflation maps.

All mandatory C3_W coupling coordinates are present.

---

# 36. Phase-like regimes

A source-parent edge is classified into:

### STATE-PARENT

Bounded partner action; weighted high-parent state extracted.

### ACTION-PARENT

Large partner amplitude action.

### MULTI-PARENT

No strong atom before DRC finite-carrier compression.

### DRIVER/DISSIPATION

Action branch routed by:

$$
J-Q(t).
$$

These are pre-singularity causal regimes.

---

# 37. Predictability

On the STATE-PARENT branch, if:

$$
\eta,
\mathfrak H_c,
\mathcal A_{p,q}
$$

are known, Theorem 18.1 gives a P2 lower forecast for the earlier parent state:

$$
\boxed{
E_h^{\psi}(s_p)
\ge
c
\frac{
\eta^2
}{
\mathfrak H_c
\mathcal A_{p,q}^2
}
E_c.
}
$$

This is a quantitative backward-necessary parent estimate generated from a forward causal ledger.

It is not a prediction of blow-up.

---

# 38. Interpretability

The weighted C3 edge now answers:

### WHEN

An explicit:

$$
s_p<t_j<T_\ast.
$$

### WHERE

Kernel-inflated causal footprint with bounded aperture.

### SCALE

High parent:

$$
h\ge k-C_{\rm LP}.
$$

### WHAT

A weighted high-parent vorticity state.

### HOW

Bilinear Navier--Stokes source projected into child shell.

### HOW MUCH

Explicit lower ratio:

$$
\eta_{\rm par}.
$$

### WHY LEGAL

Exact projected-source inequality, explicit footprint translation, and adjoint recursive semantics.

Thus the edge is causally interpretable in the ANP-00 sense.

---

# 39. What ANP-03 closes

The following are closed for the weighted footprint class:

$$
\boxed{
R_{\rm PLEAK}
:
\text{removed as an independent representation obstruction},
}
$$

$$
\boxed{
\mathrm{REC\mbox{-}S}^{W}
:
\mathrm{PROVED}
}
$$

for strong selected source atoms,

and:

$$
\boxed{
C3_W
:
\mathrm{PROVED}
}
$$

for those edges.

---

# 40. What remains open in Type-I ancestry

The source-parent edge problem is no longer the main local provenance gap.

The remaining Type-I Chain-Necessity work is:

1. ensure strong C3_W parent selection at arbitrarily many generations;
2. handle branches that repeatedly enter ACTION-PARENT rather than STATE-PARENT;
3. combine the C3_W edges into arbitrary-depth compatible paths;
4. extract one infinite path.

These are path/existence quantifier problems.

---

# 41. Non-Type-I frontier

The current C3_W construction still uses the Type-I architecture for:

- terminal singular-core entry;
- adjoint aperture control;
- parabolic core-scale interpretation.

The branch:

$$
\sup_{t<T_\ast}
\|u(t)\|_{L^{3,\infty}}
=
\infty
$$

remains untreated.

Thus the next program step returns to non-Type-I entry.

---

# 42. Next paper

The next paper is:

$$
\boxed{
\textbf{
NS-ANP 04 —
Non-Type-I Ancestry Entry,
Critical Lorentz Growth,
Adaptive Core Selection
and Causal-State Initialization
}.
}
$$

Primary tasks:

1. construct an ancestry-entry node when:
   $$
   \|u(t)\|_{L^{3,\infty}}
   $$
   is unbounded;
2. define adaptive space/scale cores without a uniform Type-I constant:
   $$
   M;
   $$
3. preserve ANP-00 causal semantics;
4. determine whether the weighted C3 Footprint Node machinery can start from that branch;
5. reduce universal Chain Necessity to arbitrary-depth compatible C3 paths.

---

# 43. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{kernel-inflation geometry}
&:\ \mathrm{PROVED},\\
\text{projected-source inflated-footprint inequality}
&:\ \mathrm{PROVED},\\
\text{weighted high-parent state envelope}
&:\ \mathrm{PROVED},\\
\text{weighted parent-state extraction}
&:\ \mathrm{PROVED},\\
\text{Parent Footprint Node legality}
&:\ \mathrm{PROVED},\\
\mathrm{REC\mbox{-}S}^{W}
&:\ \mathrm{PROVED\ FOR\ STRONG\ SOURCE\ ATOMS},\\
C3_W\text{ source-parent edge}
&:\ \mathrm{PROVED\ FOR\ STRONG\ SOURCE\ ATOMS},\\
R_{\rm PLEAK}\text{ as representation obstruction}
&:\ \mathrm{REMOVED},\\
\text{hard-ball }C3_B
&:\ \mathrm{OPEN/OPTIONAL},\\
\text{arbitrary-depth Type-I C3 paths}
&:\ \mathrm{OPEN},\\
\text{non-Type-I ancestry entry}
&:\ \mathrm{OPEN},\\
\text{Full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 44. Conclusion

ANP-03 resolves the main pseudolocal source-parent representation problem.

A dyadic projector is spatially noncompact.

Instead of forcing its parent into the identical hard core, the program uses an explicit positive kernel envelope:

$$
\chi^{[k]}
=
\kappa_k*\chi.
$$

This inflation:

- preserves mass;
- preserves centroid;
- increases aperture only by:
  $$
  O(2^{-2k});
  $$
- preserves the causal provenance branch through an explicit translation map.

The projected source satisfies:

$$
\boxed{
\left|
\int
\chi\omega_k\cdot\Delta_kF
\right|
\lesssim
\sqrt{
e_k^\chi
}
\left(
\int
\chi^{[k]}|F|^2
\right)^{1/2}.
}
$$

For a strong bilinear source atom, bounded child residence and bounded partner action therefore force a quantitatively nontrivial earlier high-parent state inside a controlled kernel-inflated footprint.

That parent footprint is recursively legal.

Hence the edge upgrades to weighted C3 causality:

$$
\boxed{
\mathsf P
\overset{C3_W}{\longrightarrow}
\mathsf C.
}
$$

Hard-ball parent containment remains a stronger optional question.

The next missing universal-ancestry problem is no longer local Type-I source provenance.

It is entry into the ancestry architecture when the Type-I weak-$L^3$ bound itself fails.

---

# References

1. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487--1541; arXiv:1812.09115.
2. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717.
3. Z. Qian, G. Xi, *Parabolic equations with divergence-free drift in space $L_t^lL_x^q$*, arXiv:1704.02173.
4. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, Pure and Applied Analysis 8 (2026), 247--270; arXiv:2407.02691.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
6. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier--Stokes and MHD equations*, arXiv:1507.06611.
7. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451. Used only as scale-locality calibration.
8. `NS_ANP_01_SourceCore_Provenance_AdjointTube_v0.1.md`.
9. `NS_ANP_02_RecursiveEdge_FootprintRecapture_v0.1.md`.
10. `NS_DRC_04_Cancellation_ManyParent_Coherence_v0.1.md`.
11. `NS_DRC_05_DissipationRange_DriverClosure_v0.1.md`.