---
title: "Navier–Stokes Dynamic Reservoir Closure Program 07：Unified Dynamic Reservoir Cover、Type-I Ancestry Recompilation、Chain-Necessity Audit 與 Cycle-III Closure"
short_title: "NS-DRC 07"
series: "Navier–Stokes Dynamic Reservoir Closure Program"
cycle: "III"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Cycle-III closure / Chain-Necessity audit"
epistemic_status: "Closes Cycle III at the reservoir-mechanism classification layer. Compiles DRC-01--06 into a Type-I state-ancestry skeleton with finite final singular-center branching, same-center backward parabolic core reuse, absolute local ultraviolet stock, and a new local-core-to-global-high-pass state injection. Audits the exact quantifier gap between node-wise reservoir/source ancestry and a single compatible source-traceable infinite chain. Identifies Source-Core Provenance, Recursive Edge Compatibility, and non-Type-I entry as the principal Chain-Necessity gaps. Shows that the accumulated coercive-action cover is not a Finite Obstruction theorem because it maps hypothetical singularity to necessary divergent actions rather than to dynamical impossibility. Cycle III therefore closes with reservoir classification complete only in the Type-I branch and with Full Chain Necessity, Finite Obstruction, and Navier-Stokes regularity still OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Dynamic Reservoir Closure Program 07

# Unified Dynamic Reservoir Cover、Type-I Ancestry Recompilation、Chain-Necessity Audit 與 Cycle-III Closure

## 0. Cycle-III closing question

Cycle II ended with four reservoir/source residual classes:

$$
R_{\rm EXP},
\quad
R_{\rm DISS},
\quad
R_{\rm DIL},
\quad
R_{\rm SRC}.
$$

Cycle III successively absorbed, compressed, or reclassified them.

After DRC-06, in the **Type-I reservoir-mechanism classification layer**:

$$
\boxed{
\mathfrak R_{\rm III,res}^{Type-I,reservoir}
=
\varnothing.
}
$$

The present paper asks the essential logical question:

$$
\boxed{
\text{Does reservoir closure imply Chain Necessity?}
}
$$

The answer is:

$$
\boxed{
\textbf{No.}
}
$$

Reservoir closure establishes that previously identified ways of hiding, delaying, dispersing, preloading, replenishing, cancelling, multiplying, or globally diluting a dangerous state no longer constitute unexplained Type-I reservoir mechanisms.

It does not yet prove that every hypothetical singularity generates one compatible infinite source-traceable ancestry.

---

# 1. Fresh standard-PDE anchors

The Cycle-III audit uses the following external inputs.

## 1.1 Barker--Prange Type-I concentration

Under:

$$
\|u\|_{L_t^\infty L_x^{3,\infty}}
\le
M,
$$

and a Type-I singular point:

$$
(x_\ast,T_\ast),
$$

Barker--Prange give quantitative concentration and backward-propagation technology near the singular point, and a quantitative bound on the number of Type-I singular points.

## 1.2 Miller middle-strain criterion

Finite-time blow-up requires divergence of a scale-critical action involving:

$$
\lambda_2^+.
$$

## 1.3 Miller strain--vorticity residual criterion

The exact residual:

$$
\mathcal R_{SV}
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right)
$$

measures departure from a globally regular strain--vorticity interaction model and provides a scale-critical regularity action.

## 1.4 Bradshaw--Grujic moving frequency window

A finite moving Littlewood--Paley frequency window controls a scale-critical regularity action and captures a fixed share of the critical Besov amplitude on the associated escape intervals.

## 1.5 Cheskidov--Shvydkoy dissipation wavenumber

The dissipation wavenumber:

$$
\Lambda(t)
=
2^{Q(t)}
$$

separates low-mode driver dynamics from high-mode viscous domination and yields a low-mode regularity criterion.

## 1.6 Tao quantitative critical $L^3$ regularity

Uniform critical:

$$
L_x^3
$$

control implies quantitative higher regularity; hence a hypothetical finite-time singularity must exhibit critical:

$$
L^3
$$

growth along a sequence approaching the candidate singular time.

This does not convert the non-Type-I weak-$L^3$ branch into the Type-I core architecture used below.

---

# 2. Cycle-III reservoir reduction ledger

## DRC-01

Exponential old-stock preload is absorbed into source renewal:

$$
\boxed{
R_{\rm EXP}
\subset
R_{\rm SRC}^{pre}.
}
$$

## DRC-02

Source renewal becomes a finite parent-state carrier or explicit cancellation/utilization/multiplicity/amplification defects.

## DRC-03

Scale-corrected state weights absorb:

$$
R_{\rm AMP},
$$

while generic utilization collapse is reclassified as depletion/certificate geometry.

## DRC-04

Cancellation is bypassed by exact net-shell grouping:

$$
R_{\rm CAN}
$$

is not an independent ancestry obstruction.

Parent multiplicity obeys a dissipation-span bound and is absorbed into:

$$
R_{\rm DISS}.
$$

## DRC-05

After viscosity-small sectors are removed, active high-frequency renewal has a low-mode driver-action ancestor or is backward re-rooted.

Thus:

$$
R_{\rm DISS}
$$

is absorbed into a standard driver/model-cone genealogy.

## DRC-06

The final global-dilution residual is removed as a **dynamic** reservoir escape because Type-I ancestry can use absolute scale-invariant local core stock.

Thus:

$$
R_{\rm DIL}
$$

is reclassified as a global normalization / energy-accounting layer.

---

# 3. Type-I absolute core node

Normalize a Type-I singular point to:

$$
(x_\ast,T_\ast)
=
(0,0).
$$

Let:

$$
R_n
=
R_I(t_n)
\asymp_M
(-t_n)^{1/2}.
$$

Choose:

$$
J_n
$$

so:

$$
\boxed{
2^{J_n}
R_n
\asymp
1.
}
$$

DRC-06 gives:

$$
\boxed{
R_n
\|
P_{>J_n}
\omega(t_n)
\|_{
L^2(B_0(R_n))
}^2
\ge
cM^2.
}
$$

Define the absolute Type-I UV core node:

$$
\boxed{
\mathsf K_n
=
(
t_n,
0,
R_n,
J_n,
\mathcal C_n^{UV}
),
}
$$

where:

$$
\mathcal C_n^{UV}
=
R_n
\|
P_{>J_n}
\omega(t_n)
\|_{
L^2(B_0(R_n))
}^2.
$$

---

# 4. CIII-7.1 — Local-Core to Global High-Pass State Injection

## Theorem 4.1

For every Type-I UV core node:

$$
\mathsf K_n,
$$

one has:

$$
\boxed{
\|
P_{>J_n}
\omega(t_n)
\|_2^2
\ge
c
\frac{
M^2
}{
R_n
}.
}
$$

Consequently:

$$
\boxed{
\|
P_{>J_n}
S(t_n)
\|_{\dot H^1}
\ge
c
M
R_n^{-3/2}.
}
$$

### Proof

The global:

$$
L^2
$$

norm dominates the local:

$$
L^2(B_{R_n})
$$

norm.

For divergence-free fields, strain and vorticity are related by zero-order Fourier multipliers and satisfy global band-passed:

$$
L^2
$$

equivalence.

Finally:

$$
\|P_{>J_n}S\|_{\dot H^1}
\ge
c
2^{J_n}
\|P_{>J_n}S\|_2.
$$

Since:

$$
2^{J_n}
\asymp
R_n^{-1},
$$

the result follows.

$\square$

---

# 5. Meaning of Theorem 4.1

The local Type-I singular core does inject into the global high-frequency state space used by the DRC Duhamel renewal machinery.

Thus the following interface is **closed**:

$$
\boxed{
\text{absolute local UV core}
\Longrightarrow
\text{nontrivial global high-pass state}.
}
$$

What remains open is not state existence.

It is source provenance.

---

# 6. Same-center Type-I state chain

Choose:

$$
0<\rho
<
C^\sharp M^{-548}
$$

as in the Barker--Prange backward concentration theorem.

Let:

$$
t_n
=
-\rho^n.
$$

Then DRC-06 gives an arbitrarily deep same-center state chain:

$$
\boxed{
\mathsf K_1,
\mathsf K_2,
\ldots,
\mathsf K_n,
\ldots
}
$$

with:

$$
R_{n-1}
=
\rho^{-1/2}R_n,
$$

and:

$$
J_n-J_{n-1}
=
\frac12
\log_2
\frac1\rho
+
O(1).
$$

This is a genuine infinite **state skeleton**.

---

# 7. Finite Type-I spatial-center branching

Barker--Prange give a finite bound:

$$
\boxed{
N_{\rm sing}(T_\ast)
\le
N_M
<
\infty
}
$$

depending only on the Type-I bound:

$$
M.
$$

Therefore the final Type-I singular-center layer is finitely branching.

Within one selected branch, the center is reused backward.

---

# 8. Node-wise source ancestry

The DRC machinery provides source alternatives for sufficiently high global high-pass states.

Schematically:

$$
\boxed{
\text{high-frequency state}
}
$$

has ancestry through:

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

or:

$$
\boxed{
\text{low-mode dissipation-wavenumber driver}
}
$$

after old-stock, amplification, cancellation, multiplicity, and deep-dissipation alternatives are absorbed.

Thus for each sufficiently high Type-I core node:

$$
\mathsf K_n,
$$

Theorem 4.1 supplies a global high-pass state to which the DRC source genealogy may be applied.

---

# 9. The quantifier obtained

The present architecture supports a statement of the form:

$$
\boxed{
\forall n
\quad
\exists
\text{ an admissible source/driver ancestry explanation for }
\mathsf K_n.
}
$$

It also supports:

$$
\boxed{
\exists
\text{ an infinite same-center Type-I state skeleton }
\{
\mathsf K_n
\}_{n\ge1}.
}
$$

These are strong statements.

But neither is Full Chain Necessity.

---

# 10. The quantifier required

RFP Chain Necessity requires one compatible infinite source-traceable chain:

$$
\boxed{
\exists
\Gamma_\infty^{NS}
\quad
\forall n
\quad
\text{all states and source edges of depth }n
\text{ are compatible}.
}
$$

The logical gap is:

$$
\boxed{
\forall n\,\exists \Gamma_n
\not\Rightarrow
\exists\Gamma_\infty.
}
$$

Finite branching can repair this only after all finite chains belong to one compatible rooted ancestry system.

That compatibility has not yet been proved.

---

# 11. Source--Core Provenance Bridge

Define the missing property:

$$
\boxed{
\textbf{SCPB — Source--Core Provenance Bridge}.
}
$$

For a Type-I core node:

$$
\mathsf K_n,
$$

SCPB would require that a quantitatively nontrivial Duhamel source ancestor of the global high-pass state can be assigned to:

- the same singular-center branch;
- a controlled enlargement of the same parabolic core;
- a compatible frequency/scale predecessor.

Current DRC theorems prove global source ancestry.

Barker--Prange prove local same-center state persistence.

They do not yet prove these are the same ancestry edge.

Thus:

$$
\boxed{
\text{SCPB}
:
\mathrm{OPEN}.
}
$$

---

# 12. Recursive Edge Compatibility

Define:

$$
\boxed{
\textbf{REC — Recursive Edge Compatibility}.
}
$$

Suppose a source edge is selected for:

$$
\mathsf K_n.
$$

REC requires that its selected parent state can itself be represented as a valid ancestor node from which the next backward source edge may be selected, with uniform bookkeeping semantics.

This includes:

- consistent spatial localization;
- consistent state norm;
- compatible frequency threshold;
- parent-to-child provenance;
- no silent reset of witness or representation class.

Current node-wise renewal results do not prove REC.

Thus:

$$
\boxed{
\text{REC}
:
\mathrm{OPEN}.
}
$$

---

# 13. CIII-7.2 — Type-I State-Ancestry Skeleton Theorem

## Theorem 13.1

Under the Barker--Prange Type-I hypotheses and a Type-I singular point, the current program proves:

1. finite final singular-center branching;
2. an arbitrarily deep same-center parabolic core state chain;
3. a uniform absolute scale-invariant local UV lower bound at every selected generation;
4. a global high-pass strain state lower bound at every generation;
5. node-wise global source/driver ancestry alternatives for sufficiently high generations.

### What is not included

The theorem does not include:

$$
\boxed{
\text{SCPB}
}
$$

or:

$$
\boxed{
\text{REC}.
}
$$

Therefore it is a **state-ancestry skeleton theorem**, not Full Chain Necessity.

$\square$

---

# 14. Conditional Type-I Chain Compiler

## Theorem 14.1

Assume in addition to Theorem 13.1:

### H1 — Source--Core Provenance

SCPB holds uniformly.

### H2 — Recursive Edge Compatibility

REC holds uniformly.

### H3 — Uniform finite branching

At each recursive source node, after already-classified depletion/driver alternatives are retained, the number of state-backed parent candidates is uniformly finite.

### H4 — Arbitrarily deep finite source realizability

For every:

$$
N,
$$

there exists a compatible finite source-traceable Type-I ancestry path of depth:

$$
N.
$$

Then:

$$
\boxed{
\exists
\Gamma_\infty^{Type-I}
}
$$

a compatible infinite source-traceable Type-I ancestry path.

### Proof

The compatible finite paths form a rooted uniformly finitely branching tree.

Arbitrarily deep finite paths imply an infinite path by the standard finite-branching tree lemma.

$\square$

---

# 15. Meaning of Theorem 14.1

The missing Type-I Chain-Necessity work is now sharply localized.

The reservoir classification no longer needs additional escape variables.

The main missing statements are:

$$
\boxed{
\text{SCPB}
+
\text{REC}
+
\text{arbitrarily deep compatible source realizability}.
}
$$

---

# 16. General singularity branch split

For a candidate finite singularity define:

$$
\boxed{
\mathcal M_{3,\infty}
=
\sup_{0<t<T_\ast}
\|u(t)\|_{L^{3,\infty}}.
}
$$

Logically there are two exhaustive branches.

## Type-I branch

$$
\boxed{
\mathcal M_{3,\infty}<\infty.
}
$$

This is the branch treated by the Barker--Prange Type-I core architecture.

## Non-Type-I branch

$$
\boxed{
\mathcal M_{3,\infty}
=
\infty.
}
$$

The current Type-I core genealogy does not cover this branch.

---

# 17. Critical $L^3$ fact does not close the split

Tao's quantitative refinement of critical:

$$
L^3
$$

regularity implies that any finite blow-up must exhibit:

$$
L^3
$$

norm growth along a sequence.

But:

$$
L^3
$$

growth is compatible with bounded:

$$
L^{3,\infty}.
$$

Thus it does not remove the Type-I weak-$L^3$ branch.

Nor does it provide the missing source-traceable ancestry for the non-Type-I branch.

---

# 18. CIII-7.3 — Global Chain-Necessity Reduction

## Theorem 18.1

To prove universal Chain Necessity for all hypothetical finite singularities, it is sufficient to close both:

### CN-I — Type-I source compatibility

Prove:

$$
\boxed{
\text{SCPB}
+
\text{REC}
+
\text{arbitrarily deep compatible source realizability}
}
$$

for the Type-I branch.

### CN-II — Non-Type-I ancestry entry

Construct a source-traceable ancestry framework for:

$$
\boxed{
\sup_{t<T_\ast}
\|u(t)\|_{L^{3,\infty}}
=
\infty.
}
$$

### Status

Both are OPEN.

$\square$

---

# 19. Reservoir closure versus Chain Necessity

The Cycle-III conclusion is therefore:

$$
\boxed{
\text{Type-I reservoir mechanism closure}
}
$$

is strictly weaker than:

$$
\boxed{
\text{Type-I Chain Necessity}.
}
$$

The difference is not a missing tax.

It is a missing **edge-compatibility theorem**.

---

# 20. Coercive-action ledger at Cycle-III end

A hypothetical finite singularity must remain compatible with divergence/non-smallness of several standard-PDE quantities, including:

$$
\boxed{
\mathcal A_{mid}
=
\int
\|\lambda_2^+\|_2^4dt,
}
$$

$$
\boxed{
\mathcal A_{SV}
=
\int
\frac{
\|\mathcal R_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}
dt,
}
$$

$$
\boxed{
\mathcal A_{freq}
=
\int
\Phi_{1/2}^4dt,
}
$$

$$
\boxed{
\mathcal A_{eig}
=
\int
D_{\rm eig}(S)^4dt,
}
$$

and the low-mode dissipation-wavenumber driver action.

Terminal high-shell activity is also required by standard shell regularity criteria.

---

# 21. Why these actions do not form Finite Obstruction

A finite obstruction theorem would require a finite family of dynamical guards such that every legal infinite formation chain enters a region incompatible with Navier--Stokes evolution.

Current results instead say:

> if a singularity exists, several coercive actions must diverge or remain non-small.

That is a necessary-dangerous-core description.

It is not a contradiction.

The conjunction:

$$
\boxed{
\mathcal A_{mid}
=
\mathcal A_{SV}
=
\mathcal A_{freq}
=
\mathcal A_{eig}
=
\mathcal A_{\rm drv}
=
\infty
}
$$

has not been proved impossible.

---

# 22. CIII-7.4 — Finite-Obstruction Audit

## Theorem 22.1

The current RFP/CSP/DRC result set does **not** establish Finite Obstruction.

### Reason

Every current generic cover mechanism falls into one of:

1. a standard regularity criterion whose violation is necessary for blow-up;
2. a source/state ancestry reduction;
3. a representation/certificate correction;
4. a depletion alternative;
5. a conditional finite-branching theorem.

None proves that every compatible infinite ancestry reaches finite-stage dynamical impossibility.

Therefore:

$$
\boxed{
\text{Finite Obstruction}
:
\mathrm{OPEN}.
}
$$

$\square$

---

# 23. Candidate Cover v3 status

Candidate Dynamic Cover v2 from Cycle II was incomplete because reservoir classes remained.

Cycle III removes those principal Type-I reservoir classes.

However a new Candidate Cover v3 would still be incomplete because:

$$
\boxed{
\text{reservoir coverage}
\neq
\text{dynamical obstruction}.
}
$$

The remaining failures are no longer reservoir taxonomy.

They are:

- universal entry;
- provenance;
- recursive compatibility;
- obstruction.

---

# 24. Exact Cycle-III achievement

Cycle III proves, relative to the stated hypotheses and internal architecture:

$$
\boxed{
\text{every previously identified Type-I reservoir escape}
}
$$

is one of:

- an already tracked source/driver action;
- a finite state-backed genealogy step;
- a depletion/certificate geometry;
- a global normalization issue.

Thus:

$$
\boxed{
\textbf{no unexplained Type-I reservoir mechanism remains in the DRC census}.
}
$$

This is the correct closure statement.

---

# 25. Exact Cycle-III non-achievement

Cycle III does **not** prove:

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\exists
\Gamma_\infty^{NS}.
}
$$

It does not prove:

$$
\boxed{
\Gamma_\infty^{NS}
\Longrightarrow
\text{finite-stage impossibility}.
}
$$

It therefore does not prove:

$$
\boxed{
\text{global regularity}.
}
$$

---

# 26. Standard-PDE recompilation frontier

The strongest clean standard-PDE statement produced by Cycle III is:

### Type-I state skeleton

A Type-I singular point has:

- quantitative parabolic local enstrophy concentration;
- absolute parabolic-or-higher-frequency UV core stock;
- same-center backward parabolic core reuse;
- finite final singular-center branching;
- nontrivial global high-pass state induced by every local UV core node.

### Dynamic source skeleton

High-frequency state persistence is not source-free:

- old preload requires source renewal;
- scale-local source is state-backed after deterministic frequency correction;
- deep dissipation interactions are viscosity-small;
- many-parent and cancellation do not block finite net-shell ancestry outside dissipation-span escape;
- active dissipation-boundary renewal has low-mode driver ancestry.

### Missing glue

The source skeleton and local Type-I core skeleton are not yet proved to be one compatible recursive ancestry.

---

# 27. Cycle-IV launch problem

The next research cycle should no longer be a reservoir program.

Define:

$$
\boxed{
\textbf{
Navier--Stokes Ancestry Necessity Program
}
}
$$

abbreviated:

$$
\boxed{
\textbf{NS-ANP}.
}
$$

Its central problem is:

$$
\boxed{
\textbf{Formation Chain Necessity}.
}
$$

---

# 28. Proposed Cycle-IV papers

## ANP-01 — Source--Core Provenance

Prove or refute SCPB:

$$
\boxed{
\text{local UV singular core}
\to
\text{localized compatible Duhamel source ancestor}.
}
$$

## ANP-02 — Recursive Edge Compatibility

Construct one stable node/edge category in which parent states may be recursively re-used without changing semantics.

## ANP-03 — Non-Type-I Entry

Treat:

$$
\|u(t)\|_{L^{3,\infty}}
\to\infty
$$

without assuming Type-I weak-$L^3$ boundedness.

## ANP-04 — Infinite-Path Extraction

Prove arbitrary-depth compatible finite source ancestry and then extract:

$$
\Gamma_\infty^{NS}.
$$

## ANP-05 — Finite Obstruction Retest

Only after Chain Necessity is established, return to the question whether all legal infinite chains can be dynamically blocked.

---

# 29. New guards

Add:

### $G_{\rm STATEINJ}$

Local Type-I UV core stock must preserve its induced global high-pass state lower bound.

### $G_{\rm PROV}$

Global source ancestry may not be assigned to a local singular-core branch without an explicit provenance theorem.

### $G_{\rm RECEDGE}$

A selected source parent may not be recursively reused as a node if its representation semantics changed.

### $G_{\rm QUANT}$

Preserve the distinction:

$$
\forall n\,\exists\Gamma_n
$$

versus:

$$
\exists\Gamma_\infty.
$$

### $G_{\rm NONTYPEI}$

Type-I core theorems may not be applied to the branch:

$$
\sup
\|u\|_{L^{3,\infty}}
=
\infty.
$$

### $G_{\rm OBS}$

A necessary divergent action is not a dynamical obstruction.

---

# 30. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Cycle-III reservoir classification}
&:\ \mathrm{CLOSED\ IN\ TYPE\mbox{-}I\ BRANCH},\\
\text{local Type-I UV core}
\Rightarrow
\text{global high-pass state}
&:\ \mathrm{PROVED},\\
\text{same-center Type-I state skeleton}
&:\ \mathrm{PROVED},\\
\text{finite final Type-I spatial-center branching}
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{node-wise global source ancestry}
&:\ \mathrm{PROVED\ RELATIVE\ TO\ DRC\ ARCHITECTURE},\\
\text{Source--Core Provenance Bridge}
&:\ \mathrm{OPEN},\\
\text{Recursive Edge Compatibility}
&:\ \mathrm{OPEN},\\
\text{non-Type-I ancestry entry}
&:\ \mathrm{OPEN},\\
\text{Type-I Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Candidate Dynamical Cover v3 completeness}
&:\ \mathrm{FALSE/INCOMPLETE},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 31. Cycle-III conclusion

Cycle III started with four unexplained reservoir/source classes:

$$
R_{\rm EXP},
R_{\rm DISS},
R_{\rm DIL},
R_{\rm SRC}.
$$

It ends with no unexplained Type-I reservoir mechanism in that census.

But the program now reaches a more fundamental boundary.

The current mathematics supplies:

$$
\boxed{
\text{an infinite Type-I state skeleton}
}
$$

and:

$$
\boxed{
\text{node-wise source/driver ancestry}.
}
$$

What it does not yet supply is:

$$
\boxed{
\textbf{one compatible infinite source-traceable chain}.
}
$$

The remaining difficulty is therefore not reservoir discovery.

It is the quantifier/provenance problem:

$$
\boxed{
\forall n\,\exists
\quad\longrightarrow\quad
\exists\,\forall n.
}
$$

That is the correct launch point for Cycle IV.

---

# References

1. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717.
2. E. Miller, *A regularity criterion for the Navier--Stokes equation involving only the middle eigenvalue of the strain tensor*, Archive for Rational Mechanics and Analysis 235 (2020), 99--139; arXiv:1710.05569.
3. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, Pure and Applied Analysis 8 (2026), 247--270; arXiv:2407.02691.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier--Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125--133; arXiv:1501.01043.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263--273; arXiv:1102.1944.
6. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier--Stokes and MHD equations*, arXiv:1507.06611.
7. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
8. `NS_DRC_01_ExponentialPreload_PrehistoryRenewal_v0.1.md`.
9. `NS_DRC_02_SourceToState_Efficiency_RenewalChain_v0.1.md`.
10. `NS_DRC_03_SourceAmplification_Utilization_DissipationCoupling_v0.1.md`.
11. `NS_DRC_04_Cancellation_ManyParent_Coherence_v0.1.md`.
12. `NS_DRC_05_DissipationRange_DriverClosure_v0.1.md`.
13. `NS_DRC_06_PersistentCoreDilution_CoreReuse_v0.1.md`.
