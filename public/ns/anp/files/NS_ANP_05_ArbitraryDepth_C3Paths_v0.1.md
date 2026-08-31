---
title: "Navier–Stokes Ancestry Necessity Program 05：Arbitrary-Depth Compatible C3 Paths、No-Terminal-Node、Adaptive Generation Renormalization 與 Singular-Horizon Compactness Gap"
short_title: "NS-ANP 05"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style arbitrary finite-depth C3 realizability / infinite-horizon extraction audit"
epistemic_status: "Proves that every positive canonical weighted shell node has an earlier legal C3 parent on any nonzero pre-singularity backward interval: either the same weighted shell state is inherited, or the exact shellwise source ledger contains a positive dyadic source atom which, by ANP-03, yields a recursively legal weighted C3 parent. This gives a No-Terminal-Node theorem and, after adaptive per-generation time renormalization, compatible C3 paths of arbitrary finite depth from arbitrarily late Type-I or non-Type-I entry seeds. A finite-path transmission product remains strictly positive for every finite depth. The theorem does not provide uniform lower bounds on transmission coefficients, normalized time steps, frequency jumps, or horizon-coherence across different terminal seeds. Therefore arbitrary-depth finite realizability is proved, but extraction of one singular-horizon-directed infinite chain remains open. Chain Necessity, Finite Obstruction, and Navier-Stokes regularity are NOT proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 05

# Arbitrary-Depth Compatible C3 Paths、No-Terminal-Node、Adaptive Generation Renormalization 與 Singular-Horizon Compactness Gap

## 0. 本文定位

ANP-04 completed universal causal-state entry:

$$
\boxed{
\text{Type-I entry}
\vee
\text{Non-Type-I adaptive entry}.
}
$$

ANP-03 proved weighted pseudolocal source-parent edges:

$$
\boxed{
C3_W
}
$$

for strong selected source atoms.

The remaining question is:

> can these legal one-step edges actually be iterated to arbitrary finite depth?

The present paper proves:

$$
\boxed{
\textbf{Yes.}
}
$$

However it also identifies the next logical gap:

$$
\boxed{
\text{arbitrary-depth finite paths}
\not\Rightarrow
\text{one singular-horizon-directed infinite path}.
}
$$

The missing step is no longer local parent existence.

It is horizon coherence / compactness.

---

# 1. Canonical child node

Let:

$$
\mathsf C
=
(
t_c,
\chi_c,
\omega(t_c),
\mathbf e^{\chi_c}(t_c),
k_c,
\operatorname{Prov}_c
)
$$

be a legal canonical Footprint Node with:

$$
\boxed{
E_c
=
e_{k_c}^{\chi_c}(t_c)
>
0.
}
$$

Fix any earlier anchor time:

$$
a<t_c.
$$

Assume:

$$
[a,t_c]
\subset
[0,T_\ast)
$$

lies in the smooth pre-singularity region.

Let:

$$
\chi(s)
=
\mathsf A_{s,t_c}\chi_c
$$

be the adjoint provenance footprint.

---

# 2. Exact shellwise ledger

ANP-02 gives:

$$
\boxed{
E_c
=
e_{k_c}^{\chi}(a)
+
\mathcal S_{k_c}^{str}[a,t_c]
+
\mathcal S_{k_c}^{tr}[a,t_c]
-
\mathcal D_{k_c}[a,t_c].
}
$$

Write:

$$
\boxed{
\mathcal S_{k_c}
=
\mathcal S_{k_c}^{str}
+
\mathcal S_{k_c}^{tr}.
}
$$

Since:

$$
\mathcal D_{k_c}\ge0,
$$

$$
\boxed{
E_c
\le
e_{k_c}^{\chi}(a)
+
\mathcal S_{k_c}.
}
$$

---

# 3. Smooth dyadic source ledger admissibility

On every compact pre-singularity interval, smoothness implies finite high Sobolev norms.

Therefore the Littlewood--Paley paraproduct decomposition of:

$$
\Delta_{k_c}(S\omega)
$$

and:

$$
[
\Delta_{k_c},
u\cdot\nabla
]\omega
$$

converges absolutely in the weighted source ledger.

Write:

$$
\boxed{
\mathcal S_{k_c}
=
\sum_{\alpha\in\mathcal I}
\Lambda_\alpha,
}
$$

where each:

$$
\alpha
$$

is a dyadic bilinear source atom.

If:

$$
\mathcal S_{k_c}>0,
$$

then at least one:

$$
\alpha_\ast
$$

satisfies:

$$
\boxed{
\Lambda_{\alpha_\ast}>0.
}
$$

---

# 4. Inheritance parent

Suppose:

$$
\boxed{
e_{k_c}^{\chi}(a)>0.
}
$$

Define the earlier node:

$$
\boxed{
\mathsf P_{\rm inh}
=
(
a,
\chi(a),
\omega(a),
\mathbf e^{\chi(a)}(a),
k_c,
\operatorname{Prov}_c
).
}
$$

By the adjoint semigroup theorem:

$$
\operatorname{Prov}
(
\chi(a)
)
=
\operatorname{Prov}_c.
$$

By REC-F the node is recursively legal.

---

# 5. CIV-5.1 — C3 Inheritance Edge

## Theorem 5.1

If:

$$
e_{k_c}^{\chi}(a)>0,
$$

then:

$$
\boxed{
\mathsf P_{\rm inh}
\overset{C3_{\rm EVO}}{\longrightarrow}
\mathsf C.
}
$$

Define the inheritance transmission coefficient:

$$
\boxed{
\vartheta_{\rm inh}
=
\frac{
e_{k_c}^{\chi}(a)
}{
E_c
}
>
0.
}
$$

The edge is:

- strictly pre-singularity;
- same-solution;
- same-provenance;
- representation stable;
- recursively reusable.

### Safety

The coefficient:

$$
\vartheta_{\rm inh}
$$

need not have a uniform positive lower bound across generations.

$\square$

---

# 6. Source parent when inheritance vanishes

Suppose instead:

$$
\boxed{
e_{k_c}^{\chi}(a)
=
0.
}
$$

Then:

$$
E_c
=
\mathcal S_{k_c}
-
\mathcal D_{k_c},
$$

so:

$$
\boxed{
\mathcal S_{k_c}
\ge
E_c
>
0.
}
$$

Hence there exists a positive dyadic source atom:

$$
\Lambda_{\alpha_\ast}>0.
$$

Define:

$$
\boxed{
\eta_\ast
=
\frac{
\Lambda_{\alpha_\ast}
}{
E_c
}
>
0.
}
$$

---

# 7. Finiteness of one-step source coordinates

For a smooth compact pre-singularity interval:

$$
[a,t_c],
$$

the child weighted shell energy is continuous and bounded.

Since:

$$
E_c>0,
$$

the child residence ratio:

$$
\boxed{
\mathfrak H_c
=
\operatorname*{ess\,sup}_{s\in[a,t_c]}
\frac{
e_{k_c}^{\chi}(s)
}{
E_c
}
}
$$

is finite.

Likewise every dyadic partner-amplitude function entering the selected smooth source atom is bounded on the compact interval.

Hence:

$$
\boxed{
0<
\mathcal A_{\alpha_\ast}
<
\infty.
}
$$

---

# 8. CIV-5.2 — Positive Source Atom Gives a C3 Parent

## Theorem 8.1

Under the source branch of Section 6, ANP-03 applies with:

$$
\eta=\eta_\ast>0.
$$

Therefore there exists:

$$
s_p\in[a,t_c)
$$

and a legal Parent Footprint Node:

$$
\mathsf P_{\rm src}
$$

such that:

$$
\boxed{
\mathsf P_{\rm src}
\overset{C3_W}{\longrightarrow}
\mathsf C.
}
$$

Moreover its weighted parent state satisfies:

$$
\boxed{
E_p
\ge
c
\frac{
\eta_\ast^2
}{
\mathfrak H_c
\mathcal A_{\alpha_\ast}^2
}
E_c
>
0.
}
$$

$\square$

---

# 9. CIV-5.3 — No-Terminal-Node Theorem

## Theorem 9.1

Let:

$$
\mathsf C
$$

be any legal canonical Footprint Node with:

$$
E_c>0,
$$

at time:

$$
t_c>0.
$$

For every earlier anchor:

$$
a\in(0,t_c),
$$

there exists an earlier legal parent node:

$$
\mathsf P
$$

at some:

$$
t_p\in[a,t_c)
$$

such that:

$$
\boxed{
\mathsf P
\overset{C3}{\longrightarrow}
\mathsf C.
}
$$

The edge is either:

$$
C3_{\rm EVO}
$$

or:

$$
C3_W.
$$

### Proof

If:

$$
e_{k_c}^{\chi}(a)>0,
$$

use Theorem 5.1.

If it vanishes, use Theorem 8.1.

$\square$

---

# 10. Meaning of No-Terminal-Node

A positive weighted shell node cannot be a finite-depth dead end while the solution is still smooth at earlier times.

The theorem does **not** provide uniform edge quality.

It proves only:

$$
\boxed{
\text{every finite-generation node has at least one earlier legal C3 parent}.
}
$$

This distinction is central.

---

# 11. Adaptive generation window

For a node at:

$$
t_m,
$$

with footprint radius coordinate:

$$
R_m,
$$

choose a local finite weak-L3 bound:

$$
\overline M_m
<
\infty
$$

on some compact interval preceding:

$$
t_m.
$$

Define:

$$
\boxed{
\Delta_m
=
\min
\left\{
\frac{t_m}{2},
\delta_m^0,
\frac{
\vartheta R_m^2
}{
1+\overline M_m
}
\right\}.
}
$$

Then:

$$
\boxed{
\Delta_m>0.
}
$$

Set:

$$
a_m
=
t_m-\Delta_m.
$$

ANP-02/04 give a uniformly controlled adjoint aperture on this edge after adaptive renormalization.

---

# 12. Strict temporal descent

By Theorem 9.1, the parent time satisfies:

$$
\boxed{
t_{m-1}
\in
[a_m,t_m).
}
$$

Since:

$$
\Delta_m
\le
t_m/2,
$$

$$
\boxed{
t_{m-1}
\ge
t_m/2
>
0.
}
$$

Thus any finite recursive construction remains inside the pre-singularity solution interval.

---

# 13. Generation ledger

For each child-to-parent step define:

$$
\boxed{
\mathfrak G_m
=
(
t_m,
k_m,
R_m,
\chi_m,
E_m,
\Delta_m,
\mathsf T_m,
\vartheta_m,
\mathfrak H_m,
\mathcal A_m,
\operatorname{Prov}_m
),
}
$$

where:

$$
\mathsf T_m
\in
\{
\mathrm{INHERIT},
\mathrm{SOURCE}
\}.
$$

---

# 14. Edge transmission coefficient

For an inheritance edge define:

$$
\boxed{
\vartheta_m
=
\frac{
E_{m-1}
}{
E_m
}
>
0.
}
$$

For a source-parent edge define:

$$
\boxed{
\vartheta_m
=
c
\frac{
\eta_m^2
}{
\mathfrak H_m
\mathcal A_m^2
}
>
0.
}
$$

Then in both cases:

$$
\boxed{
E_{m-1}
\ge
\vartheta_m
E_m.
}
$$

---

# 15. Finite-path transmission

For a path of depth:

$$
N,
$$

$$
\mathsf F_0
\to
\mathsf F_1
\to
\cdots
\to
\mathsf F_N,
$$

with physical time increasing toward the terminal child, define:

$$
\boxed{
\Theta_N
=
\prod_{m=1}^{N}
\vartheta_m.
}
$$

Since every:

$$
\vartheta_m>0,
$$

for finite:

$$
N,
$$

$$
\boxed{
\Theta_N>0.
}
$$

---

# 16. CIV-5.4 — Finite-Path Nondegeneracy

## Theorem 16.1

Along every finite compatible C3 path of depth:

$$
N,
$$

$$
\boxed{
E_0
\ge
\Theta_N
E_N
>
0.
}
$$

Thus no finite path loses state existence through multiplication by a zero transmission coefficient.

### Safety

There is no theorem here that:

$$
\inf_N
\Theta_N
>
0.
$$

The infinite product may vanish.

$\square$

---

# 17. Recursive construction

Start from any terminal positive shell node:

$$
\mathsf F_N.
$$

Apply Theorem 9.1 on the adaptive interval:

$$
[t_N-\Delta_N,t_N].
$$

This yields:

$$
\mathsf F_{N-1}.
$$

Repeat.

At every finite stage:

- the new node is legal;
- its state is positive;
- its time is positive;
- its provenance transition is explicit;
- the next adaptive interval exists.

---

# 18. CIV-5.5 — Arbitrary Finite-Depth C3 Path Theorem

## Theorem 18.1

For every:

$$
N\in\mathbb N,
$$

and every legal positive terminal Footprint shell node:

$$
\mathsf F_N
$$

at:

$$
t_N>0,
$$

there exists a compatible C3 path of depth:

$$
N:
$$

$$
\boxed{
\mathsf F_0
\overset{C3}{\longrightarrow}
\mathsf F_1
\overset{C3}{\longrightarrow}
\cdots
\overset{C3}{\longrightarrow}
\mathsf F_N.
}
$$

Every edge lies strictly before:

$$
T_\ast.
$$

Every node has positive weighted shell state.

Every representation/provenance transition is recursively legal.

$\square$

---

# 19. Universal late terminal seeds

ANP-04 proved that a hypothetical finite singularity has arbitrarily late legal ANP entry nodes in either:

- the Type-I branch;
- the non-Type-I branch.

Each entry has positive ultraviolet square-tail.

Hence at least one dyadic shell:

$$
k_N
$$

has:

$$
\boxed{
e_{k_N}^{\chi_N}(t_N)>0.
}
$$

For arbitrarily late entry nodes:

$$
\boxed{
t_N\uparrow T_\ast,
}
$$

and the available terminal frequency threshold is unbounded:

$$
\boxed{
k_N\to+\infty
}
$$

along an appropriate entry sequence.

---

# 20. CIV-5.6 — Singular-Horizon Arbitrary-Depth Realizability

## Theorem 20.1

For every finite depth:

$$
N,
$$

every:

$$
\varepsilon>0,
$$

and every frequency floor:

$$
K<\infty,
$$

a hypothetical finite singularity admits a compatible C3 path:

$$
\mathsf F_0
\to
\cdots
\to
\mathsf F_N
$$

such that the terminal node satisfies:

$$
\boxed{
T_\ast-\varepsilon
<
t_N
<
T_\ast,
}
$$

and:

$$
\boxed{
k_N>K.
}
$$

Thus:

$$
\boxed{
\text{arbitrarily deep finite C3 paths}
}
$$

exist with terminal nodes approaching the singular horizon at unbounded frequency.

### Safety

The theorem does not say these finite paths are nested as:

$$
N\to\infty.
$$

$\square$

---

# 21. Why this still does not prove Chain Necessity

Full Chain Necessity requires one path:

$$
\boxed{
\Gamma_\infty^{NS}
=
\{
\mathsf F_n
\}_{n\ge0}
}
$$

whose **forward** nodes approach:

$$
T_\ast
$$

with unbounded singular scale.

Theorem 20.1 gives:

$$
\boxed{
\forall N
\quad
\exists
\Gamma_N.
}
$$

It does not yet give:

$$
\boxed{
\exists
\Gamma_\infty
\quad
\forall N.
}
$$

The old quantifier gap has now moved entirely to singular-horizon path coherence.

---

# 22. Different terminal seeds

The finite path:

$$
\Gamma_N
$$

may terminate at a different late entry node for every:

$$
N.
$$

Thus the family:

$$
\{
\Gamma_N
\}
$$

is not yet a single rooted ancestry tree.

The singular horizon:

$$
T_\ast
$$

is a boundary, not a classical root state.

One may not invoke a finite-branching tree lemma until a common rooted/compact causal structure is constructed.

---

# 23. Branching is not the only compactness issue

Even within one finite path the coordinates:

$$
\vartheta_m,
\qquad
\Delta_m,
\qquad
k_{m-1}-k_m,
\qquad
R_m,
\qquad
\chi_m
$$

may vary strongly.

A sequence of finite paths may therefore fail to have a limit preserving the nonlinear source edge.

---

# 24. Quantitative degeneration coordinates

Define:

### Transmission collapse

$$
\boxed{
D_{\rm TRANS}
:
\vartheta_m\to0.
}
$$

### Causal-step collapse

$$
\boxed{
D_{\rm STEP}
:
\frac{
\Delta_m
}{
R_m^2
}
\to0.
}
$$

### Frequency-jump escape

$$
\boxed{
D_{\rm FJUMP}
:
|k_{m-1}-k_m|
\to\infty.
}
$$

### Spatial-scale escape

$$
\boxed{
D_{\rm SPACE}
:
\text{normalized footprint/center/scale family loses compactness}.
}
$$

These do not stop finite path existence.

They may stop singular-horizon limit extraction.

---

# 25. Infinite transmission warning

The finite product:

$$
\Theta_N>0
$$

for every:

$$
N
$$

does not imply:

$$
\boxed{
\prod_{m=1}^{\infty}
\vartheta_m
>
0.
}
$$

Thus:

$$
\boxed{
\text{finite-depth causal nondegeneracy}
\neq
\text{uniform infinite-depth nondegeneracy}.
}
$$

This is not a failure of edge legality.

It is a compactness/qualification issue.

---

# 26. Adaptive-time warning

Every:

$$
\Delta_m>0.
$$

But a sequence may satisfy:

$$
\Delta_m\to0.
$$

This does not prevent arbitrarily many edges.

It may generate a Zeno-type accumulation in physical time.

Whether such accumulation is compatible with a singular-horizon-directed chain depends on the direction and normalization of the extracted path.

No contradiction is claimed.

---

# 27. Frequency-jump warning

ANP-03 only requires for a high parent:

$$
\boxed{
h
\ge
k-C_{\rm LP}.
}
$$

It does not universally bound:

$$
h-k
$$

from above.

Thus backward parent selection may contain large upward frequency jumps.

For finite path legality this is harmless.

For compact normalized profile extraction it may matter.

---

# 28. Causal-branch compactness obligations

Define four requirements for ANP-06.

## HC1 — Horizon coherence

Late terminal seeds must be embedded into one coherent singular-horizon causal family rather than unrelated finite paths.

## HC2 — Node compactness

After legitimate translation/scaling, normalized Footprint Nodes must admit a subsequential limit in a topology strong enough to preserve the required state coordinates.

## HC3 — Edge closure

The C3 source/evolution relation must be closed under the chosen convergence.

Weak state convergence alone is not enough if the nonlinear source term is not stable.

## HC4 — Nontrivial limit

The limiting edge/node must not disappear through transmission/source-share collapse.

Current status:

$$
\boxed{
\mathrm{HC1-HC4}
:
\mathrm{OPEN}.
}
$$

---

# 29. Why ordinary weak compactness is insufficient

Normalized weighted vorticity states may admit weak:

$$
L^2
$$

subsequences under suitable bounds.

But:

$$
S\omega
$$

and the scale-transfer commutator are nonlinear products.

Weak convergence of both factors does not automatically preserve the realized C3 source contribution.

Therefore ANP-06 needs compactness strong enough to preserve causal edge semantics, not merely state existence.

---

# 30. Finite categorical source compression

The DRC source census remains useful for compactness.

At each finite smooth node, source ancestry can be compressed into finitely typed categories such as:

- inheritance;
- scale-local parent;
- low-mode driver parent;
- dissipation-boundary transition;
- source/action parent.

Within each category the actual dyadic/spatial coordinates may still form a noncompact family.

Thus:

$$
\boxed{
\text{finite mechanism taxonomy}
\neq
\text{compact causal branch space}.
}
$$

---

# 31. Recursive quantitative bookkeeping calibration

Quantitative Navier--Stokes propagation arguments in the literature show that iteration itself is a serious mathematical object.

Tao's quantitative critical-$L^3$ program replaces compactness and backward uniqueness by quantitative estimates with large explicit losses.

Palasek develops related quantitative backward-uniqueness machinery in critical settings.

Recent Barker work on quantitative classification recursively applies localized vorticity concentration/Carleman arguments and explicitly requires careful bookkeeping so repeated iterations stay inside regions of quantitative regularity.

ANP-05 reaches the same structural lesson in a different ancestry language:

$$
\boxed{
\text{one legal step}
\neq
\text{uniformly controlled infinitely many steps}.
}
$$

---

# 32. Path ledger

For a finite path:

$$
\Gamma_N,
$$

store:

$$
\boxed{
\mathcal L(\Gamma_N)
=
\{
\mathfrak G_m
\}_{m=1}^{N}.
}
$$

Derived cumulative coordinates include:

$$
\boxed{
\Theta_N
=
\prod_{m=1}^N
\vartheta_m,
}
$$

$$
\boxed{
\mathcal T_N
=
\sum_{m=1}^N
\Delta_m,
}
$$

$$
\boxed{
\mathcal J_N
=
\max_{1\le m\le N}
|k_{m-1}-k_m|,
}
$$

and the maximal normalized footprint aperture.

This ledger is the input to ANP-06.

---

# 33. Causal interpretation

For every finite path edge the ANP-00 fields remain explicit.

### WHEN

Strictly ordered pre-singularity times.

### WHERE

Adjoint/kernel-inflated causal footprints.

### SCALE

Explicit dyadic child/parent shells.

### WHAT

Weighted vorticity state.

### HOW

Inheritance or exact bilinear source contribution.

### HOW MUCH

Positive transmission:

$$
\vartheta_m.
$$

### WHY LEGAL

ANP-02 REC-F plus ANP-03 REC-S / C3 compiler.

Thus each finite path is genuinely causally interpretable.

---

# 34. Predictability

Given the finite edge ledger, one can propagate a deterministic lower state bound:

$$
\boxed{
E_0
\ge
\Theta_N
E_N.
}
$$

This is a P2 finite-horizon conditional ancestry estimate.

No positive infinite-horizon lower bound is asserted.

---

# 35. CIV-5.7 — Finite-Path Realizability Status

## Theorem 35.1

Within the ANP canonical weighted node class:

$$
\boxed{
\text{arbitrary finite-depth compatible C3 realizability}
:
\mathrm{PROVED}.
}
$$

Moreover, a hypothetical finite singularity admits such paths with terminal time arbitrarily close to:

$$
T_\ast
$$

and terminal frequency arbitrarily high.

What remains open is:

$$
\boxed{
\text{singular-horizon coherent infinite extraction}.
}
$$

$\square$

---

# 36. Exact frontier after ANP-05

The following are no longer the principal gaps:

- Type-I entry;
- non-Type-I entry;
- weighted source-core provenance;
- footprint recursion;
- source-parent recapture;
- finite-depth recursive continuation.

The principal gap is now:

$$
\boxed{
\textbf{Horizon-Coherent Infinite Path Extraction}.
}
$$

---

# 37. Next paper

The next paper is:

$$
\boxed{
\textbf{
NS-ANP 06 —
Singular-Horizon Infinite Ancestry Extraction、
Renormalized Branch Compactness、
Diagonal Coherence
與 Chain-Necessity Closure Audit
}.
}
$$

Primary tasks:

1. define one common horizon-directed family from the finite paths;
2. choose legal Navier--Stokes scaling/translation normalization;
3. obtain compactness of normalized node/edge data;
4. prove closure of C3 source edges under the selected topology;
5. control or explicitly retain:
   $$
   D_{\rm TRANS},
   D_{\rm STEP},
   D_{\rm FJUMP},
   D_{\rm SPACE};
   $$
6. determine whether:
   $$
   \forall N\,\exists\Gamma_N
   $$
   can finally be upgraded to:
   $$
   \exists\Gamma_\infty^{NS}.
   $$

---

# 38. Formal status ledger

$$
\boxed{
\begin{aligned}
C3_{\rm EVO}\text{ inheritance edge}
&:\ \mathrm{PROVED},\\
\text{positive-source-atom C3 parent}
&:\ \mathrm{PROVED},\\
\text{No-Terminal-Node}
&:\ \mathrm{PROVED},\\
\text{adaptive generation window}
&:\ \mathrm{PROVED\ TO\ EXIST},\\
\text{finite edge transmission}
&:\ \mathrm{PROVED\ POSITIVE},\\
\text{arbitrary finite-depth compatible C3 paths}
&:\ \mathrm{PROVED},\\
\text{arbitrarily late/high-frequency terminal realization}
&:\ \mathrm{PROVED},\\
\text{uniform infinite transmission}
&:\ \mathrm{OPEN},\\
\text{horizon coherence}
&:\ \mathrm{OPEN},\\
\text{C3 edge closure under path limits}
&:\ \mathrm{OPEN},\\
\text{singular-horizon infinite ancestry extraction}
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

# 39. Conclusion

ANP-05 answers the finite-depth question.

A positive canonical Footprint shell node cannot terminate at finite ancestry depth.

On every earlier pre-singularity interval either:

$$
\boxed{
\text{positive inherited weighted state}
}
$$

already exists, or the exact source ledger contains:

$$
\boxed{
\text{a positive realized dyadic source atom}.
}
$$

The first gives a recursively legal C3 evolution parent.

The second gives a weighted C3 source parent through ANP-03.

Therefore every finite generation has another earlier legal parent.

Adaptive time renormalization keeps each individual footprint edge geometrically legal even in the non-Type-I branch.

Hence:

$$
\boxed{
\forall N
\quad
\exists
\text{ a compatible C3 path of depth }N.
}
$$

Those paths can terminate arbitrarily close to the candidate singular horizon and at arbitrarily high frequency.

But the terminal seeds may vary with:

$$
N,
$$

and the edge transmission/time/scale coordinates may degenerate.

Thus the final Chain-Necessity problem is now concentrated into:

$$
\boxed{
\forall N\,\exists\Gamma_N
\quad
\stackrel{?}{\Longrightarrow}
\quad
\exists\Gamma_\infty^{NS}
}
$$

under a topology that preserves the actual nonlinear C3 causal edge.

That is ANP-06.

---

# References

1. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
2. S. Palasek, *Improved quantitative regularity for the Navier--Stokes equations in a scale of critical spaces*, arXiv:2101.08586.
3. T. Barker, *Quantitative classification of potential Navier--Stokes singularities beyond the blow-up time*, arXiv:2510.20757. Used as recent calibration for recursive quantitative concentration/Carleman bookkeeping in a more specialized setting.
4. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, arXiv:2003.06717.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
6. `NS_ANP_02_RecursiveEdge_FootprintRecapture_v0.1.md`.
7. `NS_ANP_03_SourceParent_Recapture_C3Upgrade_v0.1.md`.
8. `NS_ANP_04_NonTypeI_AdaptiveLorentzEntry_v0.1.md`.
