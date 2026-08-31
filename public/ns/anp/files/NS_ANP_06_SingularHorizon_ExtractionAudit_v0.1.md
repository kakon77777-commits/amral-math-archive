---
title: "Navier–Stokes Ancestry Necessity Program 06：Singular-Horizon Infinite Ancestry Extraction、Dual-Propagator Correction、Horizon Persistence 與 Chain-Necessity Closure Audit"
short_title: "NS-ANP 06"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Chain-Necessity extraction audit / horizon-persistence reduction"
epistemic_status: "Corrects the ANP-05 inheritance criterion by replacing mere positivity of earlier weighted shell energy with an exact dual-propagator Duhamel contribution. Proves a genuine forward causal inheritance/source dichotomy and a corrected finite-depth continuation theorem in a dual/footprint causal node class. Proves abstractly that arbitrary finite-depth realizability does not imply an infinite branch without finite branching, compactness, or horizon persistence. Separates trivial full-solution causal spines from the strong marked/source-provenance formation chain sought by Chain Necessity. Defines horizon-persistent nodes and proves a sufficient recursive persistence criterion for an actual singular-horizon chain. Identifies the missing theorem as preservation/extraction of a horizon-persistent marked C3 branch, not local source-parent existence. Critical-space profile-decomposition literature is used only as compactness calibration; it does not currently prove closure of the ANP nonlinear weighted C3 edge. Full Chain Necessity, Finite Obstruction, and Navier-Stokes regularity remain OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 06

# Singular-Horizon Infinite Ancestry Extraction、Dual-Propagator Correction、Horizon Persistence 與 Chain-Necessity Closure Audit

## 0. 本文定位

ANP-05 claimed:

$$
\boxed{
\forall N
\quad
\exists
\text{ a compatible finite C3 ancestry path of depth }N.
}
$$

It also correctly stated that this does not imply:

$$
\boxed{
\exists
\Gamma_\infty^{NS}.
}
$$

Before attempting infinite extraction, however, one inheritance step requires correction.

The condition:

$$
e_k^\chi(a)>0
$$

proves that an earlier state exists.

It does **not** by itself prove that this earlier state makes a positive propagated contribution to the later child observable.

The state could be dissipated/cancelled and later rebuilt by forcing.

Therefore ANP-06 first repairs the causal ledger.

---

# 1. Shell equation as a linear propagator plus forcing

Fix one dyadic shell:

$$
\omega_k
=
\Delta_k\omega.
$$

Its exact equation is:

$$
\boxed{
\partial_t\omega_k
+
u\cdot\nabla\omega_k
-
\nu\Delta\omega_k
=
F_k,
}
$$

where:

$$
\boxed{
F_k
=
\Delta_k(S\omega)
-
[
\Delta_k,u\cdot\nabla
]\omega.
}
$$

Let:

$$
\mathsf U_u(t,s)
$$

be the linear evolution operator solving:

$$
\partial_tv
+
u\cdot\nabla v
-
\nu\Delta v
=
0.
$$

Then:

$$
\boxed{
\omega_k(t)
=
\mathsf U_u(t,a)
\omega_k(a)
+
\int_a^t
\mathsf U_u(t,s)
F_k(s)ds.
}
$$

All times satisfy:

$$
a<s<t<T_\ast.
$$

---

# 2. Terminal weighted child amplitude

Let the child node at time:

$$
t_c
$$

have nonnegative weight:

$$
0\le\chi_c\le1
$$

and shell:

$$
k_c.
$$

Define:

$$
\boxed{
A_c
=
\left(
\int
\chi_c
|\omega_{k_c}(t_c)|^2dx
\right)^{1/2}
>
0.
}
$$

Define the terminal norming functional:

$$
\boxed{
\Phi_c
=
\frac{
\chi_c
\omega_{k_c}(t_c)
}{
A_c
}.
}
$$

Then:

$$
\boxed{
\langle
\omega_{k_c}(t_c),
\Phi_c
\rangle
=
A_c.
}
$$

Also:

$$
\|\Phi_c\|_2
\le1.
$$

---

# 3. Backward dual propagator

For:

$$
s<t_c,
$$

define:

$$
\boxed{
\Phi(s)
=
\mathsf U_u(t_c,s)^\ast
\Phi_c.
}
$$

It satisfies the adjoint equation associated with the homogeneous shell dynamics.

This is a dual provenance object.

The physical causal arrow remains:

$$
s\to t_c.
$$

---

# 4. CIV-6.1 — Exact Dual Causal Ledger

## Theorem 4.1

For every:

$$
a<t_c<T_\ast,
$$

$$
\boxed{
A_c
=
\mathcal I_c(a)
+
\mathcal Q_c[a,t_c],
}
$$

where:

$$
\boxed{
\mathcal I_c(a)
=
\left\langle
\omega_{k_c}(a),
\Phi(a)
\right\rangle,
}
$$

and:

$$
\boxed{
\mathcal Q_c[a,t_c]
=
\int_a^{t_c}
\left\langle
F_{k_c}(s),
\Phi(s)
\right\rangle ds.
}
$$

### Proof

Pair the exact Duhamel formula with:

$$
\Phi_c.
$$

Move the homogeneous propagator to the dual side.

$\square$

---

# 5. Why this ledger is stronger than the ANP-05 energy test

The quantity:

$$
e_k^\chi(a)>0
$$

only means an earlier weighted state is present.

The quantity:

$$
\boxed{
\mathcal I_c(a)>0
}
$$

means the homogeneous advection--diffusion propagation of that earlier state has a positive realized contribution to the terminal child witness.

Thus:

$$
\boxed{
\mathcal I_c(a)>0
}
$$

is a genuine forward causal inheritance criterion.

---

# 6. Dual causal node

Define a positive Dual Causal Node:

$$
\boxed{
\mathsf D
=
(
t,
k,
\omega_k(t),
\Phi_t,
A_t,
\operatorname{Prov}
),
}
$$

where:

$$
\boxed{
A_t
=
\langle
\omega_k(t),
\Phi_t
\rangle
>
0.
}
$$

The node retains:

- the actual shell state;
- the dual witness;
- a positive causal observable;
- the provenance identifier.

Its dual witness is recursively propagated by:

$$
\mathsf U_u^\ast.
$$

Thus this node type is semantically closed under causal inheritance.

---

# 7. CIV-6.2 — Genuine Inheritance/Source Dichotomy

## Theorem 7.1

For every positive terminal Dual/Footprint child node and every earlier:

$$
a<t_c,
$$

at least one of:

### PROPAGATED-INHERITANCE

$$
\boxed{
\mathcal I_c(a)>0;
}
$$

### POSITIVE-SOURCE

$$
\boxed{
\mathcal Q_c[a,t_c]>0
}
$$

holds.

### Proof

Since:

$$
A_c>0
$$

and:

$$
A_c
=
\mathcal I_c+\mathcal Q_c,
$$

the two terms cannot both be nonpositive.

$\square$

---

# 8. Source atom extraction

On a compact smooth pre-singularity interval, the source:

$$
F_k
$$

admits the same absolutely convergent dyadic/paraproduct decomposition used in ANP-03/05:

$$
F_k
=
\sum_{\alpha}
F_{k,\alpha}.
$$

Hence:

$$
\mathcal Q_c
=
\sum_\alpha
\Lambda_\alpha^{dual},
$$

where:

$$
\boxed{
\Lambda_\alpha^{dual}
=
\int_a^{t_c}
\langle
F_{k,\alpha}(s),
\Phi(s)
\rangle ds.
}
$$

If:

$$
\mathcal Q_c>0,
$$

at least one atom satisfies:

$$
\boxed{
\Lambda_{\alpha_\ast}^{dual}>0.
}
$$

---

# 9. Parent extraction on the source branch

The ANP-03 kernel-inflation argument applies after replacing the scalar terminal weight by the positive envelope naturally generated from the dual witness.

On a finite smooth interval:

- the dual field is smooth;
- the required positive envelope has finite mass/moments;
- the partner action is finite.

Therefore a positive source atom yields a positive earlier weighted parent state and an explicit recursively legal source-parent translation.

This is the source-parent branch.

---

# 10. CIV-6.3 — Corrected No-Terminal-Node

## Theorem 10.1

Let:

$$
\mathsf C
$$

be a positive canonical Footprint or Dual Causal Node at:

$$
t_c>0.
$$

For every earlier:

$$
a\in(0,t_c),
$$

there exists a legal earlier causal parent at some:

$$
t_p\in[a,t_c)
$$

such that the parent-to-child edge is either:

$$
\boxed{
C3_{\rm PROP}
}
$$

or:

$$
\boxed{
C3_W.
}
$$

Here:

- $C3_{\rm PROP}$ is a positive homogeneous propagated contribution certified by the dual ledger;
- $C3_W$ is the weighted pseudolocal source-parent edge of ANP-03.

### Safety

Mere positivity of:

$$
e_k^\chi(a)
$$

is no longer used as an inheritance criterion.

$\square$

---

# 11. ANP-05 correction

The original ANP-05 Theorem 5.1 / inheritance branch is replaced by the dual-propagator criterion:

$$
\boxed{
e_k^\chi(a)>0
}
$$

is insufficient,

while:

$$
\boxed{
\langle
\mathsf U_u(t_c,a)\omega_k(a),
\Phi_c
\rangle
>0
}
$$

is sufficient for a propagated causal inheritance edge.

All later finite-depth recursion statements are to be read with this corrected criterion.

A separate correction note is included with this release.

---

# 12. Corrected finite-depth realizability

The corrected No-Terminal-Node theorem still permits recursive finite-depth construction.

At each generation:

1. choose a positive terminal causal observable;
2. choose a positive earlier interval;
3. apply Theorem 7.1;
4. follow either propagated inheritance or a positive source atom;
5. obtain a recursively legal parent node.

Thus:

$$
\boxed{
\forall N<\infty
\quad
\exists
\text{ a compatible corrected C3 path of depth }N.
}
$$

No uniform transmission constant is claimed.

---

# 13. Weak solution spine versus strong formation ancestry

There is a trivial causal object that must not be confused with Chain Necessity.

Because the pre-singularity solution is smooth and unique on:

$$
[0,T_\ast),
$$

the full states:

$$
u(t_1),
u(t_2),
\ldots
$$

for:

$$
t_1<t_2<\cdots<T_\ast
$$

lie on one deterministic solution trajectory.

Call this:

$$
\boxed{
\textbf{CN0 — full-solution causal spine}.
}
$$

CN0 is not the target of ANP.

---

# 14. Strong marked formation chain

The target chain must additionally preserve:

1. a dangerous local/spectral mark;
2. quantitative source provenance of that mark;
3. recursive causal parent semantics;
4. unbounded singular scale;
5. forward approach to:
   $$
   T_\ast.
   $$

Call this:

$$
\boxed{
\textbf{CN3 — strong formation ancestry}.
}
$$

The program explicitly forbids replacing CN3 by the trivial CN0 full-state trajectory.

---

# 15. Chain-Necessity hierarchy

Define:

### CN0 — Solution spine

Same full solution at increasing times.

Status:

$$
\boxed{
\mathrm{PROVED/TRIVIAL}.
}
$$

### CN1 — Universal dangerous-state entry

Arbitrarily late/high-frequency legal ANP state nodes.

Status:

$$
\boxed{
\mathrm{PROVED}.
}
$$

### CN2 — Arbitrary finite-depth marked C3 ancestry

Corrected finite C3 paths of arbitrary depth.

Status:

$$
\boxed{
\mathrm{PROVED}.
}
$$

### CN3 — Horizon-directed infinite marked C3 chain

One actual chain whose forward dangerous nodes approach:

$$
T_\ast
$$

with unbounded singular scale.

Status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

### CN4 — Finite obstruction

Every legal CN3 chain hits finite-stage dynamical impossibility.

Status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 16. Abstract finite-depth no-go

Arbitrary finite-depth paths do not imply an infinite branch in an infinitely branching tree.

Consider the rooted tree whose first-level children are indexed by:

$$
n\in\mathbb N,
$$

and whose descendants under child:

$$
n
$$

are strictly decreasing finite sequences:

$$
n
>
n_1
>
n_2
>
\cdots
\ge0.
$$

For every finite depth:

$$
N,
$$

choose:

$$
n\ge N
$$

and obtain a path of depth:

$$
N.
$$

But no infinite strictly decreasing sequence of natural numbers exists.

Therefore:

$$
\boxed{
\forall N\,\exists\Gamma_N
\not\Rightarrow
\exists\Gamma_\infty
}
$$

without an additional finite-branching, compactness, or persistence hypothesis.

---

# 17. Why the ANP horizon problem has this form

ANP-05 finite paths may terminate at different late seeds.

The late seeds may have:

- different centers;
- different scales;
- different terminal footprints;
- different parent choices;
- different source/action regimes.

Thus a hypothetical singular horizon behaves like an infinitely branching boundary rather than one classical root node.

Kőnig's lemma cannot be invoked merely from arbitrary finite depth.

---

# 18. Horizon gates

Define the $q$-th singular-horizon gate:

$$
\boxed{
\mathcal H_q
=
\left\{
\mathsf F:
T_\ast-2^{-q}
<
t(\mathsf F)
<
T_\ast,
\quad
k(\mathsf F)
\ge q
\right\}.
}
$$

Universal entry gives:

$$
\boxed{
\mathcal H_q
\neq\varnothing
}
$$

for arbitrarily large:

$$
q.
$$

---

# 19. Horizon reach of a node

For a causal node:

$$
\mathsf P,
$$

define its marked C3 horizon reach:

$$
\boxed{
\mathfrak R_H(\mathsf P)
=
\sup
\left\{
t(\mathsf C):
\mathsf P
\leadsto_{C3}
\mathsf C
\text{ and }
k(\mathsf C)\text{ is in the dangerous entry class}
\right\}.
}
$$

Define:

$$
\boxed{
\mathsf P
\text{ is horizon-persistent}
}
$$

if:

$$
\boxed{
\mathfrak R_H(\mathsf P)
=
T_\ast.
}
$$

This means the same causal branch has marked descendants arbitrarily close to the singular horizon.

---

# 20. Horizon-persistent child property

Suppose a horizon-persistent node has a set of admissible marked causal children:

$$
\mathcal C(\mathsf P).
$$

The key missing recursive property is:

$$
\boxed{
\mathsf P\text{ horizon-persistent}
\Longrightarrow
\exists
\mathsf C\in\mathcal C(\mathsf P)
\text{ horizon-persistent}.
}
$$

Call this:

$$
\boxed{
\textbf{HPC — Horizon-Persistent Child}.
}
$$

---

# 21. CIV-6.4 — Horizon Persistence Sufficiency

## Theorem 21.1

Assume there exists one horizon-persistent node:

$$
\mathsf F_0
$$

and HPC holds recursively for every horizon-persistent node.

Then there exists an infinite marked C3 chain:

$$
\boxed{
\mathsf F_0
\overset{C3}{\longrightarrow}
\mathsf F_1
\overset{C3}{\longrightarrow}
\mathsf F_2
\overset{C3}{\longrightarrow}
\cdots
}
$$

such that each:

$$
\mathsf F_n
$$

is horizon-persistent.

If the child selection additionally enforces a sequence of horizon gates:

$$
\mathcal H_{q_n},
\qquad
q_n\to\infty,
$$

then:

$$
\boxed{
t_n\uparrow T_\ast,
\qquad
k_n\to\infty.
}
$$

### Proof

Apply dependent choice to the nonempty horizon-persistent child relation.

The horizon-gate condition gives the stated limits.

$\square$

---

# 22. Meaning of Theorem 21.1

The remaining Chain-Necessity gap is not another source-parent theorem.

It is:

$$
\boxed{
\textbf{prove HPC or an equivalent compactness/persistence principle}.
}
$$

---

# 23. Compact-child sufficient condition

A standard route to HPC is compactness.

Suppose for each horizon-persistent parent:

$$
\mathsf P,
$$

the admissible child set:

$$
\mathcal C(\mathsf P)
$$

is compact in a topology:

$$
\tau_C,
$$

and the horizon-reach property is closed under:

$$
\tau_C.
$$

If descendants approaching:

$$
T_\ast
$$

are generated through children in:

$$
\mathcal C(\mathsf P),
$$

a convergent child subsequence can yield a horizon-persistent child.

This motivates renormalized branch compactness.

---

# 24. Profile-decomposition calibration

Critical Navier--Stokes compactness is naturally obstructed by:

- scaling;
- translation;
- profile splitting.

Gallagher--Koch--Planchon develop profile decomposition in critical Besov spaces and use it in the:

$$
L_t^\infty L_x^3
$$

regularity problem.

Bahouri--Chemin--Gallagher develop stability under a notion of rescaled weak convergence, again using profile decompositions propagated by Navier--Stokes dynamics.

These results show that scaling/translation defects can be organized into profiles.

They do not directly prove compactness of the ANP weighted C3 causal-edge relation.

---

# 25. Profile limit versus actual branch

Define:

$$
\boxed{
\Gamma_\infty^{prof}
}
$$

as a possible infinite **renormalized profile-limit** ancestry obtained after scaling/translation and subsequence extraction.

Define:

$$
\boxed{
\Gamma_\infty^{act}
}
$$

as one actual ancestry chain in the original solution.

Then:

$$
\boxed{
\Gamma_\infty^{prof}
\neq
\Gamma_\infty^{act}
}
$$

without an additional shadowing/realization theorem.

Thus a blow-up profile by itself does not close strong Chain Necessity.

---

# 26. Nonlinear edge closure

Even if normalized states converge:

$$
\omega^{(n)}
\rightharpoonup
\omega^\infty,
$$

the source terms:

$$
S^{(n)}\omega^{(n)}
$$

and commutator transfer terms need not converge to the corresponding product of weak limits.

Therefore the topology used for horizon compactness must preserve:

$$
\boxed{
\text{realized C3 source contribution}.
}
$$

Call this requirement:

$$
\boxed{
\textbf{CEC — Causal Edge Closure}.
}
$$

Current status:

$$
\boxed{
\mathrm{CEC}
:
\mathrm{OPEN}.
}
$$

---

# 27. Nontriviality under limits

A compactness limit may also erase the marked causal state if:

$$
\vartheta_n\to0
$$

or source share tends to zero.

Define:

$$
\boxed{
\textbf{NLIM — Nontrivial Limit Condition}.
}
$$

It requires that the normalized dangerous mark and causal transmission remain nonzero in the extracted limit.

Current status:

$$
\boxed{
\mathrm{NLIM}
:
\mathrm{OPEN}.
}
$$

---

# 28. Updated horizon obligations

The ANP-05 compactness list is refined to:

### HP0 — Correct causal continuation

Provided by the dual-propagator correction.

Status:

$$
\mathrm{PROVED}.
$$

### HP1 — Horizon-persistent branch seed

Find an actual node whose marked C3 descendants approach:

$$
T_\ast.
$$

Status:

$$
\mathrm{OPEN}.
$$

### HP2 — Horizon-Persistent Child

Prove HPC.

Status:

$$
\mathrm{OPEN}.
$$

### HP3 — Causal Edge Closure

Preserve C3 under the selected compactness/limit operation.

Status:

$$
\mathrm{OPEN}.
$$

### HP4 — Nontrivial Limit

Prevent the dangerous mark/transmission from disappearing.

Status:

$$
\mathrm{OPEN}.
$$

---

# 29. Relation to quantitative propagation literature

Tao's quantitative critical-$L^3$ program replaces qualitative compactness, unique continuation, and backward uniqueness with quantitative estimates and pays very large explicit losses.

Palasek develops related quantitative backward-uniqueness machinery in critical settings.

Recent work by Barker recursively applies localized concentration/Carleman arguments in a specialized approximately axisymmetric setting and explicitly emphasizes bookkeeping needed to prevent iterative quantitative losses from leaving the regularity region.

These results support the ANP conclusion:

$$
\boxed{
\text{iterative horizon coherence requires quantitative control beyond one-step legality}.
}
$$

They do not directly prove HP1--HP4 for the ANP graph.

---

# 30. Strong Chain-Necessity closure criterion

## Theorem 30.1

Full marked Chain Necessity would follow from:

1. universal causal-state entry;
2. corrected local C3 continuation;
3. existence of a horizon-persistent marked node;
4. HPC;
5. Causal Edge Closure;
6. Nontrivial Limit / unbounded scale realization.

Items 1--2 are now available in the ANP architecture.

Items 3--6 remain open.

$\square$

---

# 31. Why finite obstruction is still premature

Even if CN3 were established, Finite Obstruction would require:

$$
\boxed{
\text{every legal infinite marked C3 chain}
\Longrightarrow
\text{finite-stage dynamical impossibility}.
}
$$

No such theorem is proved here.

Therefore:

$$
\boxed{
\text{Finite Obstruction}
:
\mathrm{OPEN}.
}
$$

---

# 32. Next research target

ANP-06 therefore does not honestly close Cycle IV.

The next paper should attack horizon persistence directly:

$$
\boxed{
\textbf{
NS-ANP 07 —
Horizon-Persistent Branch Extraction、
Critical Profile Compactness、
Causal Edge Closure
與 Strong Chain-Necessity Test
}.
}
$$

Primary tasks:

1. construct HP1 from the family of late entry seeds;
2. prove HPC using finite-carrier or compact child selection;
3. choose a critical scaling/translation normalization;
4. test profile-decomposition compactness for canonical Footprint/Dual Nodes;
5. prove or disprove CEC;
6. preserve a nontrivial marked state;
7. decide whether:
   $$
   \Gamma_\infty^{act}
   $$
   can finally be extracted.

Finite Obstruction moves to ANP-08.

---

# 33. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{ANP-05 inheritance criterion}
&:\ \mathrm{CORRECTED},\\
\text{exact dual causal ledger}
&:\ \mathrm{PROVED},\\
\text{propagated inheritance/source dichotomy}
&:\ \mathrm{PROVED},\\
\text{corrected No-Terminal-Node}
&:\ \mathrm{PROVED\ RELATIVE\ TO\ DUAL/FOOTPRINT\ NODES},\\
\text{corrected arbitrary finite-depth continuation}
&:\ \mathrm{PROVED},\\
\text{CN0 full-solution spine}
&:\ \mathrm{PROVED/TRIVIAL},\\
\text{CN1 universal dangerous-state entry}
&:\ \mathrm{PROVED},\\
\text{CN2 arbitrary finite-depth marked C3 ancestry}
&:\ \mathrm{PROVED},\\
\text{HP1 horizon-persistent node}
&:\ \mathrm{OPEN},\\
\text{HP2 Horizon-Persistent Child}
&:\ \mathrm{OPEN},\\
\text{HP3 Causal Edge Closure}
&:\ \mathrm{OPEN},\\
\text{HP4 Nontrivial Limit}
&:\ \mathrm{OPEN},\\
\text{CN3 strong horizon-directed infinite chain}
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

# 34. Conclusion

ANP-06 performs two necessary corrections.

First, earlier state existence is separated from actual propagated causal contribution.

The correct exact ledger is:

$$
\boxed{
A_c
=
\langle
\omega_k(a),
\Phi(a)
\rangle
+
\int_a^{t_c}
\langle
F_k(s),
\Phi(s)
\rangle ds.
}
$$

This yields a genuine propagated-inheritance/source dichotomy and preserves finite-depth causal continuation.

Second, arbitrary finite-depth realizability is shown to be logically insufficient for an infinite singular-horizon chain without an additional persistence/compactness principle.

The remaining target is now precise:

$$
\boxed{
\textbf{Horizon Persistence}.
}
$$

One needs a marked causal branch whose descendants recur arbitrarily close to:

$$
T_\ast,
$$

and a theorem ensuring that this property survives recursive child selection while the nonlinear C3 edge remains closed.

That is the final strong Chain-Necessity frontier.

---

# References

1. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
2. S. Palasek, *Improved quantitative regularity for the Navier--Stokes equations in a scale of critical spaces*, arXiv:2101.08586.
3. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier--Stokes regularity criterion*, arXiv:1012.0145.
4. H. Bahouri, J.-Y. Chemin, I. Gallagher, *Stability by rescaled weak convergence for the Navier--Stokes equations*, arXiv:1310.0256.
5. T. Barker, *Quantitative classification of potential Navier--Stokes singularities beyond the blow-up time*, arXiv:2510.20757.
6. `NS_ANP_03_SourceParent_Recapture_C3Upgrade_v0.1.md`.
7. `NS_ANP_04_NonTypeI_AdaptiveLorentzEntry_v0.1.md`.
8. `NS_ANP_05_ArbitraryDepth_C3Paths_v0.1.md`.
