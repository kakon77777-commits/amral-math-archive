---
title: "Navier–Stokes Causal Forest Obstruction Program 01: Diffuse Horizon Causality, Causal Cutsets, Action–Congestion Duality and Forest Obstruction"
short_title: "NS-CFOP 01"
series: "Navier–Stokes Causal Forest Obstruction Program"
cycle: "V"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Foundational forest-level obstruction / cutset flow theorem"
epistemic_status: "Introduces forest-level causal cutsets for the actual horizon causal forest obtained in ANP Cycle IV. Uses the corrected terminal dual ledger to prove a normalized causal cut-capacity theorem: across every physical-time cut before a dangerous terminal, positive propagated contribution plus absolute nonlinear source contribution is at least one. Extends this to weighted ensembles of dangerous terminals. Defines a dual-witness congestion functional and proves an Action–Congestion Duality inequality: whenever the ensemble-averaged propagated fraction across a cut is deficient by sigma, the shell-forcing L2 action times the forest dual congestion is at least sigma^2. Defines positive source-atom multiplicity and branching entropy and proves carrier-share collapse forces both effective multiplicity and entropy growth. For pairwise disjoint fresh-renewal cut slabs, bounded congestion forces linearly accumulating forcing action, yielding a conditional Forest Cutset Obstruction principle under any finite global action budget. The paper distinguishes path obstruction, atomic-end obstruction, and forest/cutset obstruction. It does not prove that the relevant nonlinear forcing action is finite near a hypothetical singularity, does not exclude diffuse horizon causality, and does not prove Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Causal Forest Obstruction Program 01

# Diffuse Horizon Causality, Causal Cutsets, Action–Congestion Duality and Forest Obstruction

## 0. The Problem of the New Cycle

Cycle IV established, relative to the ANP definitions:

$$
\boxed{
CN_{\rm Forest}
:
\mathrm{PROVED},
}
$$

while:

$$
\boxed{
CN3_{\rm Atomic}
:
\mathrm{OPEN}.
}
$$

Thus the actual pre-singularity causal object attached to a hypothetical singularity may be a horizon-unbounded DAG/forest rather than one persistent atomic lineage.

The obstruction problem must therefore be reformulated.

The question is no longer only:

> can every infinite path be blocked?

The more universal question is:

> can the entire horizon causal forest cross every causal cut without paying an impossible aggregate dynamical cost?

---

# 1. Actual horizon causal forest

Let:

$$
\boxed{
\mathscr G_H
=
(V_H,E_H)
}
$$

be the actual horizon causal forest from ANP-09.

Every:

$$
v\in V_H
$$

is an actual state/dual/footprint node in the same original Navier--Stokes solution.

Every:

$$
e\in E_H
$$

is a corrected pre-singularity:

$$
C3
$$

edge.

Dangerous-certified terminal nodes occur cofinally at:

$$
T_\ast
$$

and at unbounded singular scale.

---

# 2. Why graph cutsets alone are not enough

The forest need not have:

- one root;
- finite branching;
- one atomic end;
- uniform physical-time span per graph generation.

Therefore a combinatorial edge cut in the ancestry DAG is not the most stable primitive.

Instead use the exact PDE relation across a **physical-time cut**.

This cut is defined independently for every dangerous terminal observable.

---

# 3. Terminal dual node

Let:

$$
T
$$

be a dangerous-certified terminal node at:

$$
t_T<T_\ast,
$$

with shell:

$$
k_T,
$$

terminal amplitude:

$$
A_T>0,
$$

and terminal dual witness:

$$
\Phi_T(t_T).
$$

Let:

$$
\Phi_T(s)
$$

be the homogeneous backward dual propagation from:

$$
t_T
$$

to:

$$
s<t_T.
$$

The corrected ANP-06 ledger is:

$$
\boxed{
A_T
=
\mathcal I_T(\tau)
+
\mathcal Q_T(\tau,t_T),
}
$$

for every:

$$
\tau<t_T.
$$

---

# 4. Causal physical-time cut

Define the propagated cut fraction:

$$
\boxed{
P_T(\tau)
=
\frac{
[
\mathcal I_T(\tau)
]_+
}{
A_T
}.
}
$$

Define the absolute source cut fraction:

$$
\boxed{
S_T(\tau)
=
\frac1{
A_T
}
\int_\tau^{t_T}
\left|
\left\langle
F_{k_T}(s),
\Phi_T(s)
\right\rangle
\right|
ds.
}
$$

Define the total normalized causal cut capacity:

$$
\boxed{
\operatorname{Cap}_T(\tau)
=
P_T(\tau)
+
S_T(\tau).
}
$$

---

# 5. CIV/V-1.1 — Causal Cut Capacity Theorem

## Theorem 5.1

For every dangerous terminal:

$$
T
$$

and every:

$$
\tau<t_T,
$$

$$
\boxed{
\operatorname{Cap}_T(\tau)
\ge
1.
}
$$

### Proof

Write:

$$
1
=
\frac{
\mathcal I_T
}{
A_T
}
+
\frac{
\mathcal Q_T
}{
A_T
}.
$$

If:

$$
\mathcal I_T\ge0,
$$

then:

$$
P_T
=
\mathcal I_T/A_T.
$$

Since:

$$
S_T
\ge
|
\mathcal Q_T
|/A_T,
$$

$$
P_T+S_T
\ge
x+|1-x|
\ge1,
$$

where:

$$
x=\mathcal I_T/A_T.
$$

If:

$$
\mathcal I_T<0,
$$

then:

$$
P_T=0,
$$

while:

$$
\mathcal Q_T/A_T
=
1-\mathcal I_T/A_T
>
1,
$$

so:

$$
S_T>1.
$$

$\square$

---

# 6. Interpretation

The theorem says:

$$
\boxed{
\text{causal capacity cannot vanish across a physical cut}.
}
$$

It may cross the cut as:

1. propagated state influence;
2. fresh nonlinear source generated after the cut;
3. a mixture.

No atomic path is required to formulate this statement.

---

# 7. Causal cutset rather than path flow

The object:

$$
\operatorname{Cap}_T(\tau)
$$

is called a **terminal causal cutset capacity**.

It is not assumed to be a conserved probability flow.

The absolute source term may exceed one because:

- source terms can cancel;
- propagated contribution can be negative;
- gross causal work can exceed the net terminal amplitude.

Thus:

$$
\boxed{
\text{cut capacity}
\neq
\text{probability}.
}
$$

---

# 8. Weighted terminal ensemble

Let:

$$
\mathcal T
=
\{
T_r
\}_{r=1}^{N}
$$

be a finite family of dangerous terminals with:

$$
t_r>\tau.
$$

Choose weights:

$$
w_r\ge0,
$$

$$
\boxed{
\sum_{r=1}^{N}
w_r=1.
}
$$

Define:

$$
\boxed{
\overline P_{\mathcal T}(\tau)
=
\sum_r
w_rP_{T_r}(\tau),
}
$$

and:

$$
\boxed{
\overline S_{\mathcal T}(\tau)
=
\sum_r
w_rS_{T_r}(\tau).
}
$$

---

# 9. CIV/V-1.2 — Ensemble Cut Capacity

## Theorem 9.1

$$
\boxed{
\overline P_{\mathcal T}(\tau)
+
\overline S_{\mathcal T}(\tau)
\ge
1.
}
$$

Therefore if:

$$
\boxed{
\overline P_{\mathcal T}(\tau)
\le
1-\sigma,
}
$$

then:

$$
\boxed{
\overline S_{\mathcal T}(\tau)
\ge
\sigma.
}
$$

$\square$

---

# 10. Meaning for diffuse causality

A forest may have no persistent atomic lineage.

Nevertheless an ensemble of late dangerous terminals cannot collectively become causally disconnected from the past.

If propagated influence across a physical cut is deficient, a fixed amount of normalized nonlinear source contribution must be generated after the cut.

---

# 11. Normalized dual witnesses

For terminal:

$$
T_r,
$$

define:

$$
\boxed{
\Psi_r(s)
=
\frac{
\Phi_r(s)
}{
A_r
}.
}
$$

Then:

$$
S_{T_r}(\tau)
=
\int_\tau^{t_r}
\left|
\left\langle
F_{k_r}(s),
\Psi_r(s)
\right\rangle
\right|
ds.
$$

---

# 12. Forest dual congestion

For:

$$
s>\tau,
$$

define the shellwise dual load:

$$
\boxed{
c_k(s)
=
\sum_{
\substack{
r:
k_r=k\\
\tau<s<t_r
}
}
w_r
\|
\Psi_r(s)
\|_2.
}
$$

Define the instantaneous forest dual congestion:

$$
\boxed{
\mathfrak C_{\mathcal T,\tau}(s)^2
=
\sum_k
c_k(s)^2.
}
$$

Define its integrated congestion budget:

$$
\boxed{
\mathfrak K_C(
\mathcal T,\tau
)
=
\int_\tau^{t_{\max}}
\mathfrak C_{\mathcal T,\tau}(s)^2ds,
}
$$

where:

$$
t_{\max}
=
\max_r t_r.
$$

---

# 13. Shell forcing action

Define:

$$
\boxed{
\mathfrak A_F(
\mathcal T,\tau
)
=
\int_\tau^{t_{\max}}
\sum_k
\|F_k(s)\|_2^2ds.
}
$$

Only shells represented by the terminal ensemble need be retained; using all shells is a convenient upper action.

On every compact smooth pre-singularity interval this quantity is finite.

No uniform finiteness up to:

$$
T_\ast
$$

is assumed.

---

# 14. Aggregate source demand

By definition:

$$
\overline S_{\mathcal T}(\tau)
=
\sum_r
w_r
\int_\tau^{t_r}
|
\langle
F_{k_r}(s),
\Psi_r(s)
\rangle
|ds.
$$

At each time:

$$
s,
$$

group by terminal shell:

$$
k.
$$

Then:

$$
\boxed{
\overline S_{\mathcal T}(\tau)
\le
\int_\tau^{t_{\max}}
\left(
\sum_k
\|F_k(s)\|_2^2
\right)^{1/2}
\mathfrak C_{\mathcal T,\tau}(s)
ds.
}
$$

---

# 15. CIV/V-1.3 — Action–Congestion Duality

## Theorem 15.1

If:

$$
\overline P_{\mathcal T}(\tau)
\le
1-\sigma,
$$

then:

$$
\boxed{
\mathfrak A_F(
\mathcal T,\tau
)
\,
\mathfrak K_C(
\mathcal T,\tau
)
\ge
\sigma^2.
}
$$

### Proof

Theorem 9.1 gives:

$$
\overline S_{\mathcal T}\ge\sigma.
$$

Use the aggregate source bound and Cauchy--Schwarz in time.

$\square$

---

# 16. Forest obstruction primitive

Theorem 15.1 gives a genuine forest-level alternative:

$$
\boxed{
\text{propagated causal flow}
\vee
\text{source action}
\vee
\text{dual/branch congestion}.
}
$$

A forest can change paths.

It can branch.

It can merge.

But it cannot make all three quantities simultaneously small across a dangerous cut.

---

# 17. Cutset action floor

If:

$$
\boxed{
\mathfrak K_C(
\mathcal T,\tau
)
\le
K_0,
}
$$

and:

$$
\overline P_{\mathcal T}(\tau)
\le
1-\sigma,
$$

then:

$$
\boxed{
\mathfrak A_F(
\mathcal T,\tau
)
\ge
\frac{
\sigma^2
}{
K_0
}.
}
$$

Thus bounded congestion converts a causal cut into a definite forcing-action packet.

---

# 18. Congestion floor

Conversely, if:

$$
\boxed{
\mathfrak A_F(
\mathcal T,\tau
)
\le
A_0,
}
$$

then:

$$
\boxed{
\mathfrak K_C(
\mathcal T,\tau
)
\ge
\frac{
\sigma^2
}{
A_0
}.
}
$$

Thus a low-action forest must pay dual congestion.

---

# 19. Source atom ledger on one cut

Suppose the net source contribution for a terminal/cut is positive:

$$
\mathcal Q_T
\ge
\sigma A_T.
$$

Decompose:

$$
\boxed{
\mathcal Q_T
=
\sum_{\alpha}
\Lambda_\alpha.
}
$$

Let:

$$
a_\alpha
=
[
\Lambda_\alpha
]_+,
$$

and:

$$
\boxed{
P_T^{src}
=
\sum_\alpha
a_\alpha.
}
$$

Then:

$$
\boxed{
P_T^{src}
\ge
\mathcal Q_T
\ge
\sigma A_T.
}
$$

---

# 20. Positive source distribution

Define:

$$
\boxed{
r_\alpha
=
\frac{
a_\alpha
}{
P_T^{src}
}.
}
$$

Then:

$$
r_\alpha\ge0,
$$

and:

$$
\sum_\alpha r_\alpha=1.
$$

Define:

$$
\boxed{
\mathfrak M_T^{src}
=
\left(
\sum_\alpha
r_\alpha^2
\right)^{-1},
}
$$

and Shannon branching entropy:

$$
\boxed{
\mathfrak H_T^{src}
=
-
\sum_\alpha
r_\alpha
\log r_\alpha.
}
$$

---

# 21. Strongest positive atom

Let:

$$
\boxed{
a_{\max}
=
\max_\alpha
a_\alpha.
}
$$

Define its child-normalized share:

$$
\boxed{
\eta_{\max}
=
a_{\max}/A_T.
}
$$

Since:

$$
P_T^{src}\ge\sigma A_T,
$$

$$
\boxed{
\max_\alpha r_\alpha
\le
\frac{
\eta_{\max}
}{
\sigma
}.
}
$$

---

# 22. CIV/V-1.4 — Source Atomization Entropy Theorem

## Theorem 22.1

If:

$$
\mathcal Q_T
\ge
\sigma A_T,
$$

then:

$$
\boxed{
\mathfrak M_T^{src}
\ge
\frac{
\sigma
}{
\eta_{\max}
},
}
$$

and:

$$
\boxed{
\mathfrak H_T^{src}
\ge
\log
\left(
\frac{
\sigma
}{
\eta_{\max}
}
\right).
}
$$

### Proof

For effective multiplicity:

$$
\sum_\alpha r_\alpha^2
\le
\max_\alpha r_\alpha,
$$

hence:

$$
\mathfrak M^{src}
\ge
1/\max r_\alpha.
$$

For Shannon entropy:

$$
\mathfrak H^{src}
\ge
-\log
(
\max_\alpha r_\alpha
).
$$

Use Section 21.

$\square$

---

# 23. Meaning of source entropy

If fresh source remains a fixed fraction of a dangerous terminal but no individual causal source carrier keeps a fixed share:

$$
\eta_{\max}\to0,
$$

then:

$$
\boxed{
\mathfrak M^{src}\to\infty,
}
$$

and:

$$
\boxed{
\mathfrak H^{src}\to\infty.
}
$$

Thus diffuse fresh renewal has a measurable branch-complexity cost.

---

# 24. Relation to DRC source multiplicity

DRC-04 grouped source atoms by canonical high-parent shells and showed that large effective transition-shell multiplicity routes into dissipation-boundary span.

DRC-05 then routes the non-absorbed boundary branch into low-mode driver/action ancestry.

Therefore the source entropy theorem provides a forest-level entrance to the earlier DRC multiplicity/action census when the atom labels are chosen compatibly with that shell grouping.

This is a reduction, not a contradiction.

---

# 25. Pairwise disjoint cut slabs

Let:

$$
I_n
=
[\tau_n,t_n]
$$

be pairwise disjoint pre-singularity intervals.

For each:

$$
n,
$$

let:

$$
\mathcal T_n
$$

be a dangerous terminal ensemble supported after:

$$
\tau_n.
$$

Assume:

$$
\overline P_n
\le
1-\sigma,
$$

and:

$$
\boxed{
\mathfrak K_{C,n}
\le
K_0.
}
$$

---

# 26. CIV/V-1.5 — Disjoint Cutset Action Accumulation

## Theorem 26.1

For:

$$
N<\infty,
$$

$$
\boxed{
\sum_{n=1}^{N}
\int_{I_n}
\sum_k
\|F_k(s)\|_2^2ds
\ge
N
\frac{
\sigma^2
}{
K_0
}.
}
$$

### Proof

Apply Theorem 15.1 on each interval.

Use disjointness.

$\square$

---

# 27. Conditional infinite-cut obstruction

If in addition one had the finite global forcing-action budget:

$$
\boxed{
\int_0^{T_\ast}
\sum_k
\|F_k(s)\|_2^2ds
<
\infty,
}
$$

then there cannot exist infinitely many pairwise disjoint horizon cuts with simultaneous:

$$
\overline P_n
\le1-\sigma
$$

and:

$$
\mathfrak K_{C,n}\le K_0.
$$

### Status

This is a valid conditional forest obstruction.

The required global forcing-action finiteness is **not known or assumed** for a hypothetical singular solution.

---

# 28. Forest cutset trichotomy

For any dangerous terminal ensemble and physical cut:

$$
\boxed{
\text{PROPAGATED-CUT}
\vee
\text{ACTION-CUT}
\vee
\text{CONGESTED-CUT}.
}
$$

For chosen thresholds:

$$
\rho\in(0,1),
\qquad
A_0,K_0>0,
$$

define:

### PROPAGATED-CUT

$$
\overline P\ge\rho.
$$

### ACTION-CUT

$$
\mathfrak A_F\ge A_0.
$$

### CONGESTED-CUT

$$
\mathfrak K_C\ge K_0.
$$

If:

$$
(1-\rho)^2>A_0K_0,
$$

Theorem 15.1 guarantees that every cut lies in at least one class.

---

# 29. Action-flow cutset

A causal cut is called an:

$$
\boxed{
\textbf{action-flow cutset}
}
$$

when the forest cannot carry enough propagated causal influence across it and therefore must pay a quantitative nonlinear source-action or congestion debt.

This is the basic obstruction object of CFOP.

---

# 30. Path obstruction

Define:

$$
\boxed{
\textbf{Path Obstruction}
}
$$

as a theorem proving:

> every atomic horizon end contains a finite-stage dynamically impossible edge/node.

This addresses:

$$
CN3_{\rm Atomic}.
$$

It does not address:

$$
D_{\rm DIFF}.
$$

---

# 31. Forest obstruction

Define:

$$
\boxed{
\textbf{Forest Obstruction}
}
$$

as a theorem proving:

> every horizon-unbounded actual causal forest contains a finite causal cutset whose aggregate PDE cost violates a universal dynamical budget.

This target does not require an atomic end.

---

# 32. Finite forest obstruction

A **Finite Forest Obstruction** consists of a finite family of cut functionals:

$$
\boxed{
\mathcal O_1,
\ldots,
\mathcal O_m
}
$$

and finite dynamical budgets:

$$
B_1,
\ldots,B_m
$$

such that every horizon-unbounded dangerous causal forest must, at some finite cut, satisfy:

$$
\boxed{
\mathcal O_j>B_j
}
$$

for some:

$$
j,
$$

while the Navier--Stokes dynamics universally enforce:

$$
\mathcal O_j\le B_j.
$$

No such complete finite family is proved here.

---

# 33. Causal cut entropy

For a source-dominated cut define:

$$
\boxed{
\mathfrak E_{\rm cut}
=
\mathfrak H_T^{src}.
}
$$

Large:

$$
\mathfrak E_{\rm cut}
$$

means the causal source work is spread over many source carriers.

Small entropy forces at least one substantial source atom:

$$
\boxed{
\max_\alpha r_\alpha
\ge
e^{-\mathfrak E_{\rm cut}}.
}
$$

Thus entropy provides an atomic-end/fragmentation coordinate.

---

# 34. Bounded-entropy carrier criterion

## Theorem 34.1

If a source-dominated cut satisfies:

$$
\boxed{
\mathfrak H_T^{src}
\le
H_0,
}
$$

then some positive source atom has:

$$
\boxed{
a_\alpha
\ge
e^{-H_0}
P_T^{src}
\ge
\sigma
e^{-H_0}
A_T.
}
$$

Therefore ANP-03 supplies a quantitative weighted parent provided the residence/action guards are bounded.

$\square$

---

# 35. Diffuse source-cut criterion

Consequently, on a branch where:

- fresh source share:
  $$
  \ge\sigma;
  $$
- residence and partner-action budgets remain bounded;
- no source-parent transmission floor survives;

the source-cut entropy must satisfy:

$$
\boxed{
\mathfrak E_{\rm cut}\to\infty.
}
$$

Thus diffuse horizon causality has an entropy-growth realization when it proceeds through fresh-source atomization.

---

# 36. External flux calibration

The causal cutset quantities introduced here are ANP/CFOP objects, not standard kinetic-energy fluxes.

However rigorous Navier--Stokes/turbulence literature provides useful structural calibration.

Dascaliuc--Grujic derive rigorous physical-space energy-flux bounds and flux-locality results for 3D Navier--Stokes.

Aluie--Eyink rigorously analyze scale-locality of sharp spectral energy flux and show that aggregate local triadic interactions sustain the cascade while suitably nonlocal contributions become subdominant under their inertial-range hypotheses.

Cheskidov--Shvydkoy's dissipation wavenumber separates low-mode nonlinear dynamics from high-mode viscous control.

These results support the general methodological principle:

$$
\boxed{
\text{flux/cascade questions require aggregate cut or scale accounting, not only one trajectory}.
}
$$

They are not used to prove Theorems 5.1--35.1.

---

# 37. External forcing/work calibration

Cheskidov--Luo show in a forced Navier--Stokes energy-balance setting that work of the force is a distinct balance contribution and may display anomalous behavior.

Barker--Popkin's quantitative forced Navier--Stokes work shows that localization-induced forcing must be tracked quantitatively in Carleman propagation and can be amplified at large scales.

This supports the CFOP policy:

$$
\boxed{
\text{fresh/localized source work is retained explicitly as cutset debt}.
}
$$

Again, the internal cut-capacity and action--congestion inequalities are direct consequences of the corrected ANP dual ledger.

---

# 38. Current diffuse-forest frontier

After CFOP-01, a diffuse horizon forest can avoid an atomic carrier only by repeatedly paying some combination of:

$$
\boxed{
\text{source action},
}
$$

$$
\boxed{
\text{dual/branch congestion},
}
$$

$$
\boxed{
\text{source multiplicity/entropy},
}
$$

$$
\boxed{
\text{driver/dissipation action},
}
$$

or the remaining spatial/profile fragmentation classes from ANP-09.

No universal finite budget excluding all of these is proved.

---

# 39. Next paper

The next paper should connect the cutset burden to spatial/scale capacity:

$$
\boxed{
\textbf{
NS-CFOP 02 —
Spatial–Scale Atomization,
Forest Capacity,
Driver-Action Cutsets
and Diffuse-Cascade Rigidity
}.
}
$$

Primary tasks:

1. turn:
   $$
   D_{\rm SATOM}
   $$
   into a quantitative spatial cutset multiplicity;
2. combine source entropy with wavelength-cell packing;
3. connect high multiplicity to:
   $$
   D_{\rm eig},
   $$
   dissipation span, or driver action;
4. define a finite forest-capacity function;
5. test whether diffuse horizon forests require an unbounded sequence of disjoint action-flow cutsets.

---

# 40. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{terminal causal cut capacity}
&:\ \mathrm{PROVED},\\
\text{ensemble cut capacity}
&:\ \mathrm{PROVED},\\
\text{Action--Congestion Duality}
&:\ \mathrm{PROVED},\\
\text{source atomization multiplicity}
&:\ \mathrm{PROVED},\\
\text{source branching entropy lower bound}
&:\ \mathrm{PROVED},\\
\text{disjoint cutset action accumulation}
&:\ \mathrm{PROVED},\\
\text{conditional finite-action forest obstruction}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{bounded-entropy carrier criterion}
&:\ \mathrm{PROVED},\\
\text{complete Forest Finite Obstruction}
&:\ \mathrm{OPEN},\\
D_{\rm DIFF}\text{ exclusion}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 41. Conclusion

CFOP-01 changes the obstruction primitive from paths to cuts.

For every dangerous terminal and every physical-time cut:

$$
\boxed{
P_T(\tau)+S_T(\tau)\ge1.
}
$$

Thus normalized causal capacity cannot vanish.

For an ensemble of dangerous terminals, deficiency of propagated causal flow forces fresh source flow.

The source demand obeys:

$$
\boxed{
\mathfrak A_F
\mathfrak K_C
\ge
\sigma^2.
}
$$

Therefore a diffuse forest cannot simultaneously have:

- weak propagated influence;
- small nonlinear source action;
- low dual/branch congestion.

If the fresh source itself atomizes, the effective parent multiplicity and source branching entropy diverge:

$$
\boxed{
\mathfrak M^{src}
\ge
\sigma/\eta_{\max},
}
$$

$$
\boxed{
\mathfrak H^{src}
\ge
\log(\sigma/\eta_{\max}).
}
$$

Hence diffuse horizon causality is not cost-free.

It must cross the singular horizon through an increasingly expensive sequence of causal cutsets in action, congestion, multiplicity, entropy, or the remaining spatial/profile escape coordinates.

The open problem is whether Navier--Stokes supplies a finite global budget strong enough to make one of those costs impossible.

That is the Forest Obstruction problem.

---

# References

1. R. Dascaliuc, Z. Grujic, *Energy cascades and flux locality in physical scales of the 3D Navier--Stokes equations*, arXiv:1101.2193.
2. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.
3. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
4. A. Cheskidov, X. Luo, *Anomalous dissipation, anomalous work, and energy balance for smooth solutions of the Navier--Stokes equations*, arXiv:1910.04204.
5. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier--Stokes equations and applications*, arXiv:2602.09951.
6. `NS_ANP_06_SingularHorizon_ExtractionAudit_v0.1.md`.
7. `NS_ANP_07_HorizonPersistent_BranchExtraction_v0.1.md`.
8. `NS_ANP_08_HorizonTransmission_FreshSource_Shadowing_v0.1.md`.
9. `NS_ANP_09_ScaleFragmentation_InverseLimits_CN3FinalAudit_v0.1.md`.
