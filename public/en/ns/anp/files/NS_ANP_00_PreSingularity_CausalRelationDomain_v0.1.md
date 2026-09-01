---
title: "Navier–Stokes Ancestry Necessity Program 00: Pre-Singularity Causal Relation Domain, Hybrid Continuity, Legality, Phase-Like Transitions and Causal Interpretation"
short_title: "NS-ANP 00"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Foundational causal-domain specification / pre-ANP-01"
epistemic_status: "Defines a pre-singularity causal relation domain for the Navier-Stokes ancestry program. Separates forward PDE causality from backward inferential/provenance search; introduces a canonical Causal Atom containing spacetime, relation, existence, definition, judgment, dynamics, numericalization, continuity, discreteness, coupling, legality, phase-like transition, causality, predictability, and interpretability fields; proves basic forward-time/Duhamel causality and hybrid continuity-discreteness legality statements; defines quantitative edge coordinates and a legality matrix; and recompiles the Source-Core Provenance Bridge as a fully typed causal obligation. This is a formal research framework, not a proof of Chain Necessity, Finite Obstruction, singularity prediction, or Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 00

# Pre-Singularity Causal Relation Domain, Hybrid Continuity, Legality, Phase-Like Transitions and Causal Interpretation

## 0. Purpose

Cycle III closed the Type-I **reservoir-mechanism classification layer** but exposed the deeper problem:

$$
\boxed{
\text{state ancestry}
+
\text{node-wise source ancestry}
\not\Rightarrow
\text{one compatible causal formation history}.
}
$$

The missing object is not another reservoir tax.

It is a formal **causal relation domain**.

The present paper therefore defines the semantic, dynamical, numerical, and logical rules that every future ancestry edge must satisfy.

The domain is explicitly:

$$
\boxed{
\textbf{pre-singularity}.
}
$$

All physical/PDE causal nodes satisfy:

$$
\boxed{
t<T_\ast.
}
$$

The candidate singular time:

$$
T_\ast
$$

is a terminal horizon/boundary.

It is not treated as a classical state node unless a separate theorem supplies a meaningful state there.

---

# 1. Pre-singularity phase-space domain

Define:

$$
\boxed{
\mathfrak D_{T_\ast}^{-}
=
\left\{
(t,x,R,\lambda):
0\le t<T_\ast,\ 
x\in\mathbb R^3,\ 
R>0,\ 
\lambda>0
\right\}.
}
$$

For Littlewood--Paley representation write:

$$
\lambda
=
2^j,
\qquad
j\in\mathbb Z.
$$

A concrete event cell is:

$$
\boxed{
\mathfrak P
=
(
I,
B(x,R),
\mathcal J
),
}
$$

where:

- $I\subset[0,T_\ast)$ is a time interval;
- $B(x,R)$ is a physical region;
- $\mathcal J$ is a frequency band or high-pass region.

Thus the ancestry domain is a joint:

$$
\boxed{
\text{time}
\times
\text{space}
\times
\text{scale/frequency}
}
$$

domain.

---

# 2. Two arrows, not one

The program must preserve two fundamentally different orientations.

## 2.1 Forward PDE causal arrow

Write:

$$
\boxed{
A
\overset{\rm PDE}{\longrightarrow}
B
}
$$

only when:

$$
t_A<t_B<T_\ast
$$

and an exact or quantitatively controlled forward Navier--Stokes evolution/source relation connects:

$$
A
$$

to:

$$
B.
$$

## 2.2 Backward inferential arrow

Write:

$$
\boxed{
B
\overset{\rm infer}{\dashrightarrow}
A
}
$$

when a later dangerous state implies or suggests the existence of an earlier necessary structure.

Examples include:

- backward concentration propagation;
- reverse formation search;
- proof by contradiction from a later singular configuration.

This is an inference/provenance direction.

It is **not backward physical causation**.

---

# 3. Causal Direction Legality Axiom

## Axiom 3.1

A physical Navier--Stokes causal edge must satisfy:

$$
\boxed{
t_{\rm cause}
<
t_{\rm effect}
<
T_\ast.
}
$$

A theorem whose proof reasons backward from:

$$
t_{\rm effect}
$$

to:

$$
t_{\rm cause}
$$

does not reverse the causal arrow.

It only establishes a backward inferential arrow.

---

# 4. Exact forward strain dynamics

For the strain tensor:

$$
S
=
\nabla_{\rm sym}u,
$$

Miller's decomposition gives:

$$
\boxed{
\partial_tS
-
\nu\Delta S
=
\frac12
P_{st}
(
\omega\otimes\omega
)
-
\mathcal R_{SV},
}
$$

where:

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

Hence for:

$$
t_i<t_j<T_\ast,
$$

$$
\boxed{
S(t_j)
=
e^{\nu(t_j-t_i)\Delta}
S(t_i)
+
\int_{t_i}^{t_j}
e^{\nu(t_j-s)\Delta}
\mathcal F_S(s)\,ds,
}
$$

with:

$$
\mathcal F_S
=
\frac12P_{st}(\omega\otimes\omega)
-
\mathcal R_{SV}.
$$

The integral contains only:

$$
s<t_j.
$$

This is the canonical forward source-causality template.

---

# 5. Causal Atom

Every ancestry edge:

$$
E_{i\to j}
$$

is represented by a **Causal Atom**:

$$
\boxed{
\mathfrak A(E_{i\to j})
=
(
\mathsf{ST},
\mathsf{REL},
\mathsf{EX},
\mathsf{DEF},
\mathsf{JUD},
\mathsf{DYN},
\mathsf{NUM};
\mathsf{CONT},
\mathsf{DISC},
\mathsf{COUP},
\mathsf{LEGAL},
\mathsf{PHASE},
\mathsf{CAUSE},
\mathsf{PRED},
\mathsf{INTERP}
).
}
$$

The first seven entries are the primary causal coordinates.

The final eight entries are structural/epistemic attributes.

No future ANP edge may be called a **proved causal ancestry edge** unless these fields are explicitly typed.

---

# 6. Primary coordinate I — Spacetime

Define:

$$
\boxed{
\mathsf{ST}(E)
=
(
t_i,
t_j,
T_\ast,
x_i,
x_j,
R_i,
R_j,
J_i,
J_j
).
}
$$

Required data include:

1. cause time:
   $$
   t_i;
   $$
2. effect time:
   $$
   t_j;
   $$
3. singular horizon:
   $$
   T_\ast;
   $$
4. physical centers/regions;
5. spatial radii;
6. frequency bands or thresholds.

Mandatory ordering:

$$
\boxed{
0\le t_i<t_j<T_\ast.
}
$$

---

# 7. Time-to-singularity coordinate

Define:

$$
\boxed{
\tau(t)
=
T_\ast-t.
}
$$

For an edge:

$$
E_{i\to j},
$$

define horizon contraction:

$$
\boxed{
\Theta_T(E)
=
\frac{
T_\ast-t_j
}{
T_\ast-t_i
}
\in(0,1).
}
$$

A pre-singularity formation chain approaching:

$$
T_\ast
$$

has:

$$
\boxed{
\Theta_T^{(n)}
\to
1
}
$$

locally if consecutive times become dense, while the cumulative product drives:

$$
T_\ast-t_n
\to0.
$$

For geometric Type-I sampling:

$$
T_\ast-t_n
=
\rho
(
T_\ast-t_{n-1}
),
$$

one has:

$$
\Theta_T=\rho.
$$

---

# 8. Primary coordinate II — Relation

Every edge receives one or more relation types.

Define:

$$
\boxed{
\mathsf{REL}(E)
\subset
\{
\mathrm{EVO},
\mathrm{SRC},
\mathrm{LOC},
\mathrm{SCALE},
\mathrm{PROV},
\mathrm{DRV},
\mathrm{DEPL},
\mathrm{INFER}
\}.
}
$$

### EVO

Same-solution evolution.

### SRC

A Duhamel source contribution.

### LOC

Spatial localization or concentration inheritance.

### SCALE

Scale/frequency inheritance.

### PROV

Provenance: an earlier state/source is certified as belonging to the same ancestry branch.

### DRV

A low-mode or other dynamical driver relation.

### DEPL

A depletion/regularization relation.

### INFER

Backward logical inference only.

Important:

$$
\boxed{
\mathrm{INFER}
\neq
\mathrm{SRC}.
}
$$

---

# 9. Primary coordinate III — Existence

Existence must be typed at four levels:

$$
\boxed{
\mathsf{EX}
=
(
E_{\rm sol},
E_{\rm node},
E_{\rm edge},
E_{\rm chain}
).
}
$$

## $E_{\rm sol}$

Does the solution exist in the required class on the interval?

## $E_{\rm node}$

Does the state node exist quantitatively?

Example:

$$
\|P_{>J}S(t)\|_{\dot H^1}>0.
$$

## $E_{\rm edge}$

Does a nontrivial legal source/evolution edge exist?

## $E_{\rm chain}$

Can the edge be recursively embedded in one compatible ancestry chain?

Status values:

$$
\boxed{
\mathrm{DEFINED},
\mathrm{CONDITIONAL},
\mathrm{PROVED},
\mathrm{OPEN},
\mathrm{FAIL}.
}
$$

This prevents the common error:

$$
\boxed{
E_{\rm node}=\mathrm{PROVED}
\not\Rightarrow
E_{\rm chain}=\mathrm{PROVED}.
}
$$

---

# 10. Primary coordinate IV — Definition

Every node and edge must have a stable canonical type.

Define node classes:

$$
\boxed{
\mathcal N_{\rm type}
=
\{
\mathrm{CORE},
\mathrm{UVSTATE},
\mathrm{SOURCE},
\mathrm{DRIVER},
\mathrm{ACTION},
\mathrm{TRANSITION}
\}.
}
$$

Examples:

### CORE

$$
(
t,x,R,
R\|\omega\|_{L^2(B_R)}^2
).
$$

### UVSTATE

$$
(
t,J,
\|P_{>J}S(t)\|_{\dot H^1}
).
$$

### SOURCE

A time-integrated Duhamel packet.

### DRIVER

For example:

$$
\Omega_Q(t)
=
\|\nabla u_{\le Q(t)}\|_\infty.
$$

A node may be translated from one representation to another only by an explicit translation map:

$$
\boxed{
T_{\alpha\to\beta}.
}
$$

Silent semantic switching is illegal.

---

# 11. Definition stability condition

## Axiom 11.1

If:

$$
N_i
\in
\mathcal N_\alpha
$$

is recursively reused as:

$$
N_{i-1}
\in
\mathcal N_\beta,
$$

then either:

$$
\alpha=\beta,
$$

or an explicit map:

$$
T_{\alpha\to\beta}
$$

must be supplied with quantitative error/provenance control.

This is the formal foundation of:

$$
\boxed{
\text{Recursive Edge Compatibility}.
}
$$

---

# 12. Primary coordinate V — Judgment

Every candidate causal edge carries a judgment vector:

$$
\boxed{
\mathsf{JUD}(E)
=
(
J_{\rm time},
J_{\rm hyp},
J_{\rm eq},
J_{\rm rep},
J_{\rm err},
J_{\rm prov},
J_{\rm rec}
).
}
$$

Each component takes:

$$
\boxed{
\mathrm{PASS},
\mathrm{FAIL},
\mathrm{OPEN}.
}
$$

### $J_{\rm time}$

Correct temporal orientation.

### $J_{\rm hyp}$

External/internal theorem hypotheses satisfied.

### $J_{\rm eq}$

Edge is compatible with the exact PDE.

### $J_{\rm rep}$

Representations match.

### $J_{\rm err}$

Localization/projection/commutator errors are controlled.

### $J_{\rm prov}$

Same-branch provenance is established.

### $J_{\rm rec}$

The parent can recursively serve as a legal node.

---

# 13. Primary coordinate VI — Dynamics

Every physical causal edge must name its dynamical law.

Allowed examples include:

1. heat/viscous propagation;
2. exact Duhamel forcing;
3. strain--vorticity interaction;
4. low-mode dissipation-wavenumber driver;
5. localized transport with commutator/error terms;
6. pressure-compatible projected dynamics.

A statement of mere temporal correlation is not a dynamical edge.

---

# 14. Dynamic source decomposition

For a projected target state:

$$
P_{\mathcal J}S(t_j),
$$

define the source packet:

$$
\boxed{
Y_{i\to j}^{\mathcal J}
=
\int_{t_i}^{t_j}
e^{\nu(t_j-s)\Delta}
P_{\mathcal J}
\mathcal F_S(s)\,ds.
}
$$

The source relation is quantitatively meaningful only if:

$$
\boxed{
\|Y_{i\to j}^{\mathcal J}\|_X
}
$$

is compared to the target state in a specified norm:

$$
X.
$$

---

# 15. Primary coordinate VII — Numericalization

The causal relation domain uses a **vector of dimensionless coordinates**, not one arbitrary scalar score.

Define:

$$
\boxed{
\mathsf{NUM}(E)
=
(
\Pi_T,
\Pi_R,
\Pi_{JR},
\Pi_\nu,
\eta_{\rm src},
\kappa_{\rm core},
\chi_{SV},
\delta_Q,
\zeta_{\rm ov},
\mathcal E_{\rm err}
).
}
$$

---

# 16. Parabolic geometry coordinate

Define:

$$
\boxed{
\Pi_R
=
\frac{
R
}{
\sqrt{
\nu(T_\ast-t)
}
}.
}
$$

For Type-I parabolic cores:

$$
\Pi_R
\asymp_M
1.
$$

---

# 17. Frequency--radius coupling

Define:

$$
\boxed{
\Pi_{JR}
=
2^J
R.
}
$$

Interpretation:

### $\Pi_{JR}\ll1$

Frequency wavelength is much larger than the physical core.

### $\Pi_{JR}\asymp1$

Parabolic/wavelength matching.

### $\Pi_{JR}\gg1$

Many wavelengths fit inside the physical core.

This is a canonical spatial--spectral coupling coordinate.

---

# 18. Viscous age

For an edge:

$$
t_i\to t_j
$$

at frequency:

$$
2^J,
$$

define:

$$
\boxed{
\Pi_\nu
=
\nu
2^{2J}
(
t_j-t_i
).
}
$$

This is the number of viscous times elapsed at that scale.

Old high-frequency stock survival is exponentially taxed in:

$$
\Pi_\nu.
$$

---

# 19. Source contribution ratio

Define:

$$
\boxed{
\eta_{\rm src}
=
\frac{
\|
Y_{i\to j}^{\mathcal J}
\|_X
}{
\|
P_{\mathcal J}S(t_j)
\|_X
}
}
$$

when the denominator is nonzero.

This is a **contribution ratio**.

It is not a counterfactual philosophical causal effect.

Large:

$$
\eta_{\rm src}
$$

means the selected source packet is quantitatively relevant to the target state.

---

# 20. Absolute core stock

Define:

$$
\boxed{
\kappa_{\rm core}
=
R
\|
\omega(t)
\|_{L^2(B(x,R))}^2.
}
$$

For a Type-I Barker--Prange core:

$$
\kappa_{\rm core}
$$

has a positive lower bound depending on:

$$
M.
$$

This coordinate does not require normalization by global enstrophy.

---

# 21. Model-cone coordinate

Define:

$$
\boxed{
\chi_{SV}
=
\frac{
\|\mathcal R_{SV}\|_2
}{
\|-\Delta S\|_2
}.
}
$$

The surface:

$$
\boxed{
\chi_{SV}=1
}
$$

is a dynamical regime boundary in the DRC model-cone analysis.

It is not a thermodynamic phase boundary.

---

# 22. Dissipation offset

Define:

$$
\boxed{
\delta_Q
=
J-Q(t).
}
$$

### $\delta_Q<0$

Target frequency lies below the dissipation boundary.

### $\delta_Q=O(1)$

Transition band.

### $\delta_Q\gg1$

Deep dissipative range.

---

# 23. Spatial overlap coordinate

For two nonzero localized parent fields:

$$
f,
g,
$$

define one possible overlap coefficient:

$$
\boxed{
\zeta_{\rm ov}
=
\frac{
\|fg\|_2
}{
\|f\|_\infty
\|g\|_2
}
\in[0,1].
}
$$

Alternative localized overlap coordinates may be used if they are better adapted to the interaction.

The key rule is:

$$
\boxed{
\text{global state norms do not imply spatial overlap}.
}
$$

---

# 24. Error coordinate

For localized/projected dynamics define:

$$
\boxed{
\mathcal E_{\rm err}
=
\frac{
\|\mathrm{commutator/error}\|_X
}{
\|\mathrm{target\ source/state}\|_X
}
}
$$

whenever meaningful.

An edge requiring:

$$
\mathcal E_{\rm err}\ll1
$$

must record the threshold explicitly.

---

# 25. Continuity

Continuity is a vector property:

$$
\boxed{
\mathsf{CONT}
=
(
C_t,
C_x,
C_{\rm scale},
C_{\rm bridge}
).
}
$$

### $C_t$

Temporal regularity on:

$$
[t_i,t_j].
$$

### $C_x$

Spatial regularity/local energy status.

### $C_{\rm scale}$

Whether scale variation is treated continuously or through discrete dyadic representation.

### $C_{\rm bridge}$

Whether a discrete graph edge is embedded in an actual continuous PDE trajectory.

---

# 26. Hybrid Continuity--Discreteness Axiom

## Axiom 26.1

A discrete ancestry edge:

$$
N_i
\to
N_{i+1}
$$

is legal only if it embeds into a continuous or weakly continuous PDE bridge on:

$$
[t_i,t_{i+1}].
$$

Discrete sampling is a representation choice.

It is not evidence that the physical dynamics itself jumps discontinuously between nodes.

---

# 27. Discreteness

The ancestry representation contains genuine discrete structures:

1. dyadic frequency index:
   $$
   j\in\mathbb Z;
   $$
2. selected event times:
   $$
   t_n;
   $$
3. graph nodes and edges;
4. branch labels;
5. threshold crossings.

Define:

$$
\boxed{
\mathsf{DISC}
=
(
D_t,
D_j,
D_{\rm graph},
D_{\rm regime}
).
}
$$

The continuous PDE and the discrete proof graph coexist.

Neither replaces the other.

---

# 28. Coupling

Define a coupling vector:

$$
\boxed{
\mathsf{COUP}
=
(
K_{\rm eq},
K_{\rm amp},
K_{\rm space},
K_{\rm scale},
K_{\rm prov}
).
}
$$

### $K_{\rm eq}$

Do the two quantities appear in the same exact PDE relation?

### $K_{\rm amp}$

Quantitative source/state amplitude coupling, e.g.:

$$
\eta_{\rm src}.
$$

### $K_{\rm space}$

Physical co-localization/overlap.

### $K_{\rm scale}$

Frequency/radius compatibility, e.g.:

$$
\Pi_{JR}.
$$

### $K_{\rm prov}$

Are the cause and effect certified as the same ancestry branch?

A relation can be strongly coupled in one coordinate and weakly coupled in another.

Hence coupling is not reduced to one scalar.

---

# 29. Legality

Define:

$$
\boxed{
\mathsf{LEGAL}(E)
\in
\{
\mathrm{PROVED},
\mathrm{CONDITIONAL},
\mathrm{OPEN},
\mathrm{ILLEGAL}
\}.
}
$$

A causal edge is **PROVED** only when all mandatory judgment components are:

$$
\mathrm{PASS}.
$$

If provenance or recursive compatibility is:

$$
\mathrm{OPEN},
$$

the edge is not illegal as a candidate relation.

But it is not a proved ancestry edge.

---

# 30. Seven legality tests

A future ANP edge must pass:

### L1 — temporal legality

$$
t_i<t_j<T_\ast.
$$

### L2 — solution legality

Same Navier--Stokes solution/class.

### L3 — theorem-hypothesis legality

All imported theorem assumptions hold.

### L4 — representation legality

Node types are unchanged or explicitly translated.

### L5 — localization/error legality

Cutoff/pressure/commutator errors are retained.

### L6 — provenance legality

The source belongs to the claimed core/branch.

### L7 — recursive legality

The parent can be reused under the same ancestry semantics.

---

# 31. Phase-like transition

The word **phase** is used operationally, not thermodynamically.

Define a regime label:

$$
\boxed{
\sigma
=
(
\sigma_Q,
\sigma_{SV},
\sigma_B,
\sigma_{\rm core}
).
}
$$

---

# 32. Dissipation-regime transition

For a scale:

$$
J,
$$

define:

$$
\sigma_Q
=
\begin{cases}
\mathrm{DRIVER}, & J<Q-L,\\
\mathrm{TRANSITION}, & |J-Q|\le L,\\
\mathrm{DISSIPATIVE}, & J>Q+L.
\end{cases}
$$

Crossing:

$$
J-Q(t)=\pm L
$$

is a phase-like regime transition.

---

# 33. Model-cone transition

Define:

$$
\sigma_{SV}
=
\begin{cases}
\mathrm{DEPLETING}, & \chi_{SV}<1-\delta,\\
\mathrm{CROSSING}, & |\chi_{SV}-1|\le\delta,\\
\mathrm{DEPARTED}, & \chi_{SV}>1+\delta.
\end{cases}
$$

This labels a dynamical regime relative to Miller's regular-model cone.

---

# 34. Escape-level transition

For a critical Besov level:

$$
L,
$$

define:

$$
\sigma_B
=
\begin{cases}
\mathrm{BELOW}, & B(t)<L,\\
\mathrm{CROSS}, & B(t)=L,\\
\mathrm{PERSIST}, & B(t)>L.
\end{cases}
$$

The continuous-level escape time is a regime crossing.

---

# 35. Core-state transition

A local region may change between:

- no certified concentration;
- absolute enstrophy core;
- absolute UV core;
- source-backed UV core.

These are proof/dynamical regimes.

They must not be confused with the formation of the final singularity itself.

---

# 36. The singularity is not an ordinary phase transition node

The candidate singular time:

$$
T_\ast
$$

is not inserted as:

$$
N_{\rm singular}
$$

with an assumed classical state.

The chain only approaches:

$$
T_\ast
$$

from below:

$$
\boxed{
t_n\uparrow T_\ast.
}
$$

Thus every proved edge is **pre-singularity**.

---

# 37. Causality

Define four causal statuses.

### C0 — Association

Two quantities co-occur.

No causal statement.

### C1 — Necessary predecessor

A later state implies existence/non-smallness of some earlier quantity.

This may arise from backward inference.

### C2 — PDE causal contribution

An earlier source/state enters an exact forward evolution and contributes quantitatively to a later state.

### C3 — Recursively provenance-certified causal ancestry

A C2 edge which also satisfies:

- source--core provenance;
- recursive edge compatibility.

The current ANP target is to upgrade relevant edges from:

$$
\mathrm{C1/C2}
$$

to:

$$
\boxed{
\mathrm{C3}.
}
$$

---

# 38. No-future-source theorem

## Theorem 38.1

For the mild/strong pre-singularity strain evolution on:

$$
[t_i,t_j],
$$

the state:

$$
S(t_j)
$$

depends through Duhamel only on:

- state at:
  $$
  t_i;
  $$
- forcing at:
  $$
  s\in[t_i,t_j].
  $$

No source at:

$$
s>t_j
$$

enters the exact forward formula.

Therefore a PDE causal source edge is strictly forward-time.

$\square$

---

# 39. Backward inference non-causality theorem

## Theorem 39.1

A backward concentration theorem of the form:

$$
\text{later dangerous state}
\Longrightarrow
\text{earlier concentration}
$$

does not by itself establish:

$$
\text{earlier concentration}
\overset{\rm SRC}{\longrightarrow}
\text{later dangerous state}.
$$

An additional forward dynamic/provenance certificate is required.

### Reason

Logical implication of necessary structure does not identify the quantitatively relevant forward source contribution.

$\square$

---

# 40. Predictability

Predictability is not identified with causality.

Define four levels:

$$
\boxed{
\mathsf{PRED}
\in
\{
P0,P1,P2,P3
\}.
}
$$

### P0 — descriptive

No forward forecast.

### P1 — necessary-risk inference

The present state implies constraints on what must occur if a later singularity forms.

This is a precursor/necessary-condition statement.

### P2 — quantitative conditional forecast

Given current compressed state and hypotheses, one can bound:

- next crossing time;
- minimum source action;
- minimum driver action;
- future norm range.

### P3 — local deterministic full-state forecast

Given a full smooth state in a local well-posed interval, the PDE determines the subsequent solution.

Important:

$$
\boxed{
P1
\neq
\text{singularity prediction}.
}
$$

---

# 41. Prediction horizon

For a certified precursor at:

$$
t_p
$$

and a predicted regime event at:

$$
t_e,
$$

define:

$$
\boxed{
\tau_{\rm lead}
=
t_e-t_p
>0.
}
$$

A numerical/experimental ANP implementation may also record:

- false positive rate;
- false negative rate;
- confidence interval;
- calibration curve.

These are empirical quantities.

They are not substituted for mathematical proof.

---

# 42. Pre-singularity prediction target

The mathematically legitimate near-term targets are not:

$$
\boxed{
\text{predict }T_\ast\text{ exactly}.
}
$$

They are:

1. predict the next regime crossing;
2. predict a required minimum action packet;
3. predict a source-renewal necessity;
4. predict whether a node must re-root backward;
5. predict whether a scale enters the dissipative/driver transition band.

These are local causal predictions.

---

# 43. Interpretability

Define the provenance/explanation tuple:

$$
\boxed{
\mathsf{INTERP}(E)
=
(
\mathrm{WHEN},
\mathrm{WHERE},
\mathrm{SCALE},
\mathrm{WHAT},
\mathrm{HOW},
\mathrm{HOW\ MUCH},
\mathrm{WHY\ LEGAL}
).
}
$$

A fully interpretable ancestry edge must answer:

### WHEN

At what times?

### WHERE

In what physical region?

### SCALE

At what frequency/physical scale?

### WHAT

What state/source variable?

### HOW

Which PDE mechanism?

### HOW MUCH

What quantitative contribution?

### WHY LEGAL

Which theorem/guard proves the relation?

---

# 44. Interpretability completeness mask

Define:

$$
\boxed{
\mathbf I(E)
=
(
i_t,
i_x,
i_\lambda,
i_{\rm var},
i_{\rm dyn},
i_{\rm amp},
i_{\rm legal}
)
\in
\{0,1\}^7.
}
$$

The edge is **causally interpretable** when:

$$
\boxed{
\mathbf I(E)
=
(1,1,1,1,1,1,1).
}
$$

A pretty narrative with missing provenance receives zero in the missing coordinate.

---

# 45. Continuous and discrete causal graphs

Define the physical evolution graph:

$$
\boxed{
\mathcal G_{\rm causal}^{+}
=
(
\mathcal N,
\mathcal E_{\rm PDE}^{+}
).
}
$$

Edges point forward in time.

Define the inferential graph:

$$
\boxed{
\mathcal G_{\rm infer}^{-}
=
(
\mathcal N,
\mathcal E_{\rm infer}^{-}
).
}
$$

Edges point from later observations to earlier candidate causes.

The research task is to identify pairs:

$$
E_{\rm infer}^{-}
$$

and:

$$
E_{\rm PDE}^{+}
$$

that certify the same provenance relation.

---

# 46. Causal closure square

For two nodes:

$$
A,
B,
\qquad
t_A<t_B,
$$

a complete causal relation ideally forms:

$$
\boxed{
\begin{array}{ccc}
B
& \overset{\rm infer}{\dashrightarrow}
& A
\\
\uparrow
&&
\downarrow
\\
\text{effect certificate}
&&
\text{cause certificate}
\\
&
A
\overset{\rm PDE}{\longrightarrow}
B
&
\end{array}
}
$$

The backward theorem says:

$$
B\Rightarrow A.
$$

The forward PDE certificate says:

$$
A
\to
B
$$

with quantitative source relevance.

Their agreement closes a provenance square.

---

# 47. Causal relation tensor

For computational and theorem-audit purposes define:

$$
\boxed{
\mathbf T(E)
=
\begin{bmatrix}
\mathsf{ST}\\
\mathsf{REL}\\
\mathsf{EX}\\
\mathsf{DEF}\\
\mathsf{JUD}\\
\mathsf{DYN}\\
\mathsf{NUM}\\
\mathsf{CONT}\\
\mathsf{DISC}\\
\mathsf{COUP}\\
\mathsf{LEGAL}\\
\mathsf{PHASE}\\
\mathsf{CAUSE}\\
\mathsf{PRED}\\
\mathsf{INTERP}
\end{bmatrix}.
}
$$

This is a heterogeneous tensor/schema, not a Euclidean vector requiring meaningless addition of unlike coordinates.

Numerical subfields may be compared quantitatively.

Logical/categorical subfields retain categorical semantics.

---

# 48. Why no single causal score is used

A single scalar score could hide:

- correct time ordering but absent provenance;
- strong source amplitude but illegal theorem hypotheses;
- perfect spatial overlap but wrong scale;
- strong prediction but no causal mechanism.

Therefore:

$$
\boxed{
\text{causal completeness is multi-axis}.
}
$$

Scalar reduction is allowed only for a clearly defined downstream task.

---

# 49. Legality status of current Type-I core chain

The Barker--Prange/DRC Type-I state skeleton currently has:

### Spacetime

PROVED/EXTERNAL-CALIBRATED.

### Existence of state nodes

PROVED.

### Same-center localization

PROVED under Type-I hypotheses.

### Scale coupling

PROVED:

$$
2^{J_n}R_n\asymp1.
$$

### Global high-pass injection

PROVED.

### Node-wise source ancestry

PROVED relative to DRC architecture.

### Source--core provenance

OPEN.

### Recursive edge compatibility

OPEN.

Thus the current chain is not yet a C3 causal ancestry chain.

---

# 50. Source--Core Provenance Bridge as a typed causal theorem

ANP-01 must prove a statement of the following form.

For a later Type-I core node:

$$
K_j
=
(
t_j,x_j,R_j,J_j,\mathcal C_j
),
$$

there exists an earlier source/core node:

$$
K_i,
\qquad
t_i<t_j,
$$

and a source packet:

$$
Y_{i\to j}
$$

such that:

### SCPB-1 — spacetime

$$
t_i<t_j<T_\ast.
$$

### SCPB-2 — localization

Source support lies in a controlled enlargement of the same core tube.

### SCPB-3 — scale

Parent/output scales satisfy an explicit relation.

### SCPB-4 — source relevance

$$
\eta_{\rm src}
\ge
\eta_0>0.
$$

### SCPB-5 — PDE legality

The edge follows the exact localized/global Duhamel dynamics with controlled errors.

### SCPB-6 — provenance

The source is certified as ancestry of the selected singular-core branch.

### SCPB-7 — recursion

The parent state is a legal node for the next step.

Only then may one write:

$$
\boxed{
K_i
\overset{\rm C3}{\longrightarrow}
K_j.
}
$$

---

# 51. Coupling to the singular horizon

A formation chain:

$$
K_0
\to
K_1
\to
\cdots
$$

is a **pre-singularity formation chain** when:

$$
\boxed{
t_n\uparrow T_\ast,
}
$$

and at least one singular scale indicator diverges:

$$
\boxed{
J_n\to+\infty
}
$$

or equivalently:

$$
\boxed{
R_n\to0
}
$$

on a scale-coupled core branch.

For the Type-I parabolic chain:

$$
2^{J_n}R_n\asymp1,
$$

both occur together.

---

# 52. Continuity and pre-singularity approaching

The chain is discrete:

$$
\{t_n\}.
$$

The physical solution on:

$$
[0,T_\ast)
$$

is not replaced by the sequence.

Instead:

$$
\boxed{
\{K_n\}
}
$$

is a sampled causal skeleton embedded in the pre-singularity continuous trajectory.

The limit:

$$
t_n\uparrow T_\ast
$$

is a limit of legal pre-singularity nodes.

No post-singularity state is assumed.

---

# 53. Causal legality and phase transitions

A phase-like regime transition is legal only if:

1. both sides occur before:
   $$
   T_\ast;
   $$
2. the crossing variable is defined continuously or with a valid trace;
3. the threshold is explicitly stated;
4. the transition is not confused with a singularity proof.

Example:

$$
J-Q(t):
\quad
\mathrm{TRANSITION}
\to
\mathrm{DISSIPATIVE}.
$$

This is a scale-regime change.

It is not blow-up.

---

# 54. Causality and correlation firewall

Add the guard:

$$
\boxed{
G_{\rm CAUSAL}
}
$$

A relation may not be called causal merely because:

- both quantities diverge;
- both occur near:
  $$
  T_\ast;
  $$
- they correlate numerically;
- one theorem says both are necessary.

A physical/PDE causal edge needs:

- correct time direction;
- a dynamical relation;
- quantitative relevance;
- provenance.

---

# 55. Prediction firewall

Add:

$$
\boxed{
G_{\rm PRED}
}
$$

A necessary pre-singularity signal is not called a predictor of blow-up unless it has a proved forward implication or an explicitly empirical predictive validation.

Thus:

$$
\boxed{
\text{precursor}
\neq
\text{predictor}
\neq
\text{cause}.
}
$$

---

# 56. Interpretation firewall

Add:

$$
\boxed{
G_{\rm INTERP}
}
$$

A causal explanation must not omit the mismatch between:

- local and global;
- state and source;
- continuous and discrete;
- physical and inferential arrows;
- theorem-forced and merely defined objects.

---

# 57. Causal Atom legality theorem

## Theorem 57.1

If a candidate edge:

$$
E_{i\to j}
$$

has:

1. temporal order:
   $$
   t_i<t_j<T_\ast;
   $$
2. same-solution PDE evolution;
3. explicit stable node definitions;
4. controlled localization/projection errors;
5. nontrivial quantitative source contribution;
6. established same-branch provenance;
7. recursive parent-node compatibility;

then:

$$
\boxed{
\mathsf{LEGAL}(E_{i\to j})
=
\mathrm{PROVED}
}
$$

and:

$$
\boxed{
\mathsf{CAUSE}(E_{i\to j})
=
\mathrm{C3}.
}
$$

### Proof

This is a direct conjunction of the causal-domain legality definitions.

The mathematical work in future papers is proving each nontrivial component for concrete Navier--Stokes edges.

$\square$

---

# 58. Current ANP status after causal recompilation

The Type-I DRC architecture presently has:

$$
\boxed{
\text{continuous pre-singularity state skeleton}
+
\text{discrete sampled nodes}
+
\text{node-wise source ancestors}.
}
$$

What is missing is the C3 upgrade:

$$
\boxed{
\text{same-core provenance}
+
\text{recursive edge compatibility}.
}
$$

Thus ANP-01 is no longer an ambiguous request to ``connect source and core.''

It is a fully typed causal theorem obligation.

---

# 59. Causal phase table for the Type-I branch

A typical Type-I pre-singularity chain may pass through the following operational regimes:

| Regime | Time | Space | Scale | Dynamical meaning |
|---|---:|---:|---:|---|
| Core detection | $t<T_\ast$ | $B(x,R)$ | $2^J R\asymp1$ | absolute local enstrophy |
| UV extraction | same $t$ | same/expanded core | $>J$ | low frequencies insufficient |
| Renewal | earlier interval $\to t$ | global/local pending provenance | $\ge J$ | Duhamel source needed |
| Driver | earlier time | low modes | relative to $Q(t)$ | non-absorbable forcing |
| Transition | pre-singularity | core/transition region | $J\approx Q(t)$ | viscosity/nonlinearity competition |
| Model-cone crossing | pre-singularity | global/local | strain dynamics | $\chi_{SV}\approx1$ |

This table describes **pre-singularity regimes**, not a thermodynamic phase diagram.

---

# 60. Predictive causal chain target

A future mature ANP chain should be able to answer, at a node:

$$
K_n,
$$

not only:

> where did this node come from?

but also:

> given this causal state, what is the mathematically forced next range of possible states before $T_\ast$?

Define a set-valued predictor:

$$
\boxed{
\mathcal P_\Delta(K_n)
=
\{
\text{legal descendant states in }[t_n,t_n+\Delta]
\}.
}
$$

The theorem-level goal is to shrink:

$$
\mathcal P_\Delta
$$

by dynamical constraints.

This is a safer and more rigorous concept than predicting one exact singular future.

---

# 61. Numerical causal audit record

For every computational or theorem-audit edge store:

```text
edge_id
cause_time
effect_time
T_star
cause_center / effect_center
cause_radius / effect_radius
cause_frequency / effect_frequency
relation_type
existence_status
definition_type
judgment_vector
dynamic_equation
Pi_R
Pi_JR
Pi_nu
eta_src
kappa_core
chi_SV
delta_Q
overlap
error_ratio
continuity_status
discreteness_status
coupling_vector
legality_status
phase_before
phase_after
causality_level
predictability_level
interpretability_mask
provenance_id
recursive_parent_id
```

This is the machine-readable causal ledger for Cycle IV.

---

# 62. New global guards

Add:

### $G_{\rm PRESING}$

Every physical causal edge lies strictly before:

$$
T_\ast.
$$

### $G_{\rm ARROW}$

Backward inference is not backward causation.

### $G_{\rm HYBRID}$

Every discrete edge must embed in a continuous PDE bridge.

### $G_{\rm EXIST}$

Node existence, edge existence, and chain existence are distinct statuses.

### $G_{\rm DEFSTAB}$

Recursive node semantics may not change silently.

### $G_{\rm JUDGE}$

All edge judgments must be explicitly PASS/FAIL/OPEN.

### $G_{\rm NUMVEC}$

Causal numericalization is vector-valued; no arbitrary one-number causal score.

### $G_{\rm PHASESEM}$

Operational regime transitions are not thermodynamic phase transitions or singularity proofs.

### $G_{\rm CAUSAL}$

Correlation/necessary co-divergence is not enough for a causal edge.

### $G_{\rm PRED}$

Precursor, predictor, and cause remain separate categories.

### $G_{\rm INTERP}$

Every causal edge must expose when/where/scale/variable/mechanism/amplitude/legality.

---

# 63. What this framework now says about the singularity

The candidate singularity is treated as a **future boundary of the causal domain**:

$$
\boxed{
T_\ast
=
\sup
\{
t:
\text{classical/specified pre-singularity state exists}
\}.
}
$$

The research task is not to assign a mysterious causal state to:

$$
T_\ast.
$$

It is to determine whether the sequence of pre-singularity causal atoms becomes forced into:

- scale contraction;
- action divergence;
- source renewal;
- core concentration;
- driver/model-cone transitions;

in one recursively compatible ancestry.

---

# 64. ANP-01 revised target

The next paper is now:

$$
\boxed{
\textbf{
NS-ANP 01 —
Source--Core Provenance Bridge
within the Pre-Singularity Causal Relation Domain
}.
}
$$

It must output not merely an implication, but a legal Causal Atom:

$$
\boxed{
\mathfrak A(
K_i\to K_j
)
}
$$

with all fifteen fields populated.

Primary target:

$$
\boxed{
\text{global high-pass source ancestor}
\Longrightarrow
\text{same-core localized provenance}
}
$$

or a precise theorem showing why such localization fails.

---

# 65. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{pre-singularity causal domain}
&:\ \mathrm{DEFINED},\\
\text{forward/inferential arrow separation}
&:\ \mathrm{DEFINED/PROVED\ BY\ PDE\ FORM},\\
\text{Causal Atom schema}
&:\ \mathrm{DEFINED},\\
\text{seven primary causal coordinates}
&:\ \mathrm{DEFINED},\\
\text{eight structural causal attributes}
&:\ \mathrm{DEFINED},\\
\text{hybrid continuity--discreteness legality}
&:\ \mathrm{DEFINED},\\
\text{dimensionless numerical coordinates}
&:\ \mathrm{DEFINED/SCALE\ AUDITED},\\
\text{operational phase-like transitions}
&:\ \mathrm{DEFINED},\\
\text{causality-level taxonomy}
&:\ \mathrm{DEFINED},\\
\text{predictability-level taxonomy}
&:\ \mathrm{DEFINED},\\
\text{interpretability mask}
&:\ \mathrm{DEFINED},\\
\text{Source--Core Provenance Bridge}
&:\ \mathrm{OPEN},\\
\text{Recursive Edge Compatibility}
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

# 66. Conclusion

The Ancestry Necessity Program now has a causal ontology.

The object of study is no longer just:

$$
\text{state}_1
\to
\text{state}_2.
$$

Every relation must specify:

$$
\boxed{
\text{Spacetime}
+
\text{Relation}
+
\text{Existence}
+
\text{Definition}
+
\text{Judgment}
+
\text{Dynamics}
+
\text{Numericalization}.
}
$$

And every relation must expose:

$$
\boxed{
\text{Continuity}
+
\text{Discreteness}
+
\text{Coupling}
+
\text{Legality}
+
\text{Phase-like transition}
+
\text{Causality}
+
\text{Predictability}
+
\text{Interpretability}.
}
$$

Most importantly:

$$
\boxed{
\text{all physical causal edges are pre-singularity and forward in time}.
}
$$

Backward reasoning is retained as an inference/provenance graph.

The central Cycle-IV problem is to make the two graphs close on the same ancestry:

$$
\boxed{
\text{backward necessary predecessor}
\quad
\leftrightarrow
\quad
\text{forward PDE-causal source}.
}
$$

That is the precise mathematical content of the Source--Core Provenance problem.

---

# References

1. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717.
2. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487--1541; arXiv:1812.09115.
3. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
4. E. Miller, *A regularity criterion for the Navier--Stokes equation involving only the middle eigenvalue of the strain tensor*, Archive for Rational Mechanics and Analysis 235 (2020), 99--139; arXiv:1710.05569.
5. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, Pure and Applied Analysis 8 (2026), 247--270; arXiv:2407.02691.
6. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier--Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125--133; arXiv:1501.01043.
7. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263--273; arXiv:1102.1944.
8. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier--Stokes and MHD equations*, arXiv:1507.06611.
9. `NS_DRC_CYCLE_III_HANDOFF_v1.0.md`.
10. `NS_DRC_07_UnifiedReservoirCover_ChainNecessityAudit_v0.1.md`.