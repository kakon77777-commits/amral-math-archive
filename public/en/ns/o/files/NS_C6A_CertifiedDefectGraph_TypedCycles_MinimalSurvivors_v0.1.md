---
title: "Navier–Stokes C6-A: Certified Defect Graph, Typed Cycle Composition, and Minimal Survivor Candidates"
subtitle: "Why Projected SCCs Are Only Over-Approximations, How to Define Composable PDE Defect Cycles, and Which Recurrent Loops Are Actually Certified After C5"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "C6 opening paper / certified transition semantics / cycle-composition audit"
epistemic_status: "Finite graph/hypergraph theory + C5 routing audit + external theorem gates. No nontrivial Navier–Stokes recurrent defect cycle is claimed as constructed or certified. Global regularity remains open."
---

# Navier–Stokes C6-A
# Certified Defect Graph, Typed Cycle Composition, and Minimal Survivor Candidates

## 0. Formal Launch of C6

C5-M compressed the residual state space of C5 into:

$$
\boxed{
\mathfrak D_{C5}
=
\{
\mathsf A,
\mathsf T,
\mathsf G,
\mathsf P,
\mathsf H,
\mathsf F
\}.
}
$$

where:

- $\mathsf A$: ancestry / legality / theorem setup;
- $\mathsf T$: temporal phase oscillation / concentration;
- $\mathsf G$: strain-vorticity field geometry;
- $\mathsf P$: pressure compensation / provenance;
- $\mathsf H$: high-order harmonic / theorem-window defect;
- $\mathsf F$: forcing / order variation debt.

The task of C5 was:

$$
\boxed{
\text{state construction}
+
\text{compactification}
+
\text{debt routing}.
}
$$

The task of C6 shifts to:

$$
\boxed{
\text{cycle extraction}
+
\text{cycle compatibility}
+
\text{cycle elimination}.
}
$$

The first objective of this C6-A round appears simple:

> Perform SCC extraction on the C5 finite defect graph.

However, a crucial correction emerges immediately:

$$
\boxed{
\textbf{Ordinary label-level SCCs are insufficient to prove PDE recurrent cycles.}
}
$$

Reasons:

- A coarse edge may only hold for a specific subtype within a class;
- Edge sources/targets possess additional metadata;
- Two individually valid edges are not necessarily compatible end-to-end;
- A `not ruled out` self-loop is not a transition theorem;
- External regularity gates are sinks, not ordinary transitions;
- Many C5 routings are inherently disjunctive hyperedges.

Therefore, C6-A must first establish:

$$
\boxed{
\textbf{Certified Typed Defect Transition System}.
}
$$

---

# 1. Fresh primary-source audit

## 1.1 Current PDE status

Navier–Stokes existence/smoothness remains a Clay Millennium Prize open problem.

Thus, C6 cycle analysis remains a necessary-condition/defect-compatibility study within the research program,

not a known global proof.

## 1.2 Grujić–Xu 2024

The formal 2024 framework of Grujić–Xu:

- higher derivative component/sign superlevel sparseness;
- harmonic-measure majorization;
- ascending / descending derivative chains;
- dynamic interpolation;
- asymptotically vanishing scaling gap.

This serves in C6 as:

$$
\mathsf H\to\mathrm{REG}
$$

the primary external kill gate.

## 1.3 Miller strain geometry

The Miller middle-eigenvalue criterion restricts the strain geometry of hypothetical finite-time blow-ups.

Miller's strain-vorticity work further provides:

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0
}
$$

and strain-vorticity operator regularity interfaces.

These are:

$$
\mathsf G,\mathsf P,\mathsf F
$$

important external/structural anchors for.

## 1.4 Bradshaw–Tsai pressure provenance

The whole-space local pressure expansion provides:

- local pressure;
- far pressure;
- harmonic far-field;

with rigorous provenance.

Therefore:

$$
\mathsf P
$$

is not a purely phenomenological graph node.

---

# 2. C5 six-class state space

Let:

$$
\boxed{
V_6
=
\{
T,G,P,H,F
\}
}
$$

denote the five physical residual classes after entering the physical/legal regime.

$A$ is temporarily excluded from physical SCC extraction,

because:

$$
\boxed{
A
}
$$

may indicate a proof/theorem-entry failure,

and is not necessarily an actual physical singularity mechanism.

---

# 3. C5-M projected may graph

If we project all C5-M:

- conditional;
- structural;
- not-yet-excluded;

arrows into ordinary directed edges,

we obtain the schematic:

$$
\boxed{
T\to T,G,P,
}
$$

$$
\boxed{
G\to G,P,H,
}
$$

$$
\boxed{
P\to P,G,
}
$$

$$
\boxed{
H\to H,F,
}
$$

$$
\boxed{
F\to F,H,G,P.
}
$$

---

# 4. Projected may-SCCs

For this ordinary may graph,

the SCC decomposition is:

$$
\boxed{
\{T\},
\qquad
\{G,P,H,F\}.
}
$$

If we retain the conditional:

$$
T\to G/P,
$$

the condensation graph schematic is:

$$
\boxed{
T
\longrightarrow
\{G,P,H,F\}.
}
$$

Thus, a naive graph reading would state:

> The physical survivor ultimately falls into the $\{G,P,H,F\}$ sink SCC.

C6-A determines:

$$
\boxed{
\textbf{This conclusion is currently invalid.}
}
$$

---

# 5. C6-A.1: Projected-SCC No-Go

## Proposition

Let:

$$
\pi:\mathcal K\to V_6
$$

be a projection from full defect states:

$$
\theta\in\mathcal K
$$

to coarse residual labels.

Suppose two typed transition relations:

$$
R_{XY}
\subset
\mathcal K_X\times\mathcal K_Y,
$$

$$
R_{YX}
\subset
\mathcal K_Y\times\mathcal K_X
$$

are nonempty.

Then the coarse graph contains:

$$
X\leftrightarrow Y.
$$

However, this does **not** imply the existence of:

$$
\theta_X,\theta_Y
$$

with:

$$
(\theta_X,\theta_Y)\in R_{XY},
$$

$$
(\theta_Y,\theta_X)\in R_{YX}.
$$

### Reason

The target metadata produced by:

$$
R_{XY}
$$

may lie outside the source antecedent of:

$$
R_{YX}.
$$

Therefore:

$$
\boxed{
X\leftrightarrow Y
\text{ in projected graph}
}
$$

does not imply:

$$
\boxed{
\text{composable two-cycle}.
}
$$

$\square$

---

# 6. Edge semantics must be typed

C6-A uses four edge statuses.

## I — Implication edge

$$
\boxed{
X
\overset{I}{\longrightarrow}
Y
}
$$

means a proved routing theorem with explicit source antecedent and target conclusion.

## C — Conditional implication

$$
\boxed{
X
\overset{C}{\longrightarrow}
Y
}
$$

means the implication is proved only under an extra gate:

- strong-middle cone;
- common far pressure;
- ancestry legality;
- theorem setup;
- bounded turnover;
- etc.

## N — Non-exclusion / possible persistence

$$
\boxed{
X
\overset{N}{\looparrowright}
X
}
$$

means current estimates do not exclude recurrence in $X$.

This is **not** a transition theorem.

## E — External kill edge

$$
\boxed{
X
\overset{E}{\longrightarrow}
\mathrm{REG}
}
$$

means a published regularity theorem closes the route when its antecedents hold.

---

# 7. Why $N$ edges cannot define SCCs

If:

$$
X
\overset{N}{\looparrowright}
X,
$$

all we know is:

> the current proof has not ruled out staying in $X$.

We do not know:

- there exists a Navier–Stokes orbit realizing recurrent $X$;
- one $X$ event dynamically generates another $X$ event;
- the compact limit is dynamically invariant.

Therefore:

$$
\boxed{
\textbf{N-edges are survivor obligations,
not certified dynamics}.
}
$$

---

# 8. Full defect state spaces

For each class, define the compact/compactified metadata space:

$$
\boxed{
\mathcal K_T,
\mathcal K_G,
\mathcal K_P,
\mathcal K_H,
\mathcal K_F.
}
$$

Examples:

## $\mathcal K_T$

- colored Young measure;
- concentration mass;
- phase correlation;
- cumulative ledgers.

## $\mathcal K_G$

- middle-gap coordinate;
- strain-direction measure;
- compressive-axis measure;
- derivative/vorticity stock.

## $\mathcal K_P$

- pressure amplitude;
- far matrix;
- signature;
- provenance / heredity;
- axis locking.

## $\mathcal K_H$

- derivative order;
- theorem-window score;
- sign process;
- root-load measure;
- setup flag.

## $\mathcal K_F$

- viscous turnover;
- projected nonlinear turnover;
- order curvature;
- clock defect measure.

---

# 9. Typed transition relation

A C6 edge is not just:

$$
X\to Y.
$$

It is a relation:

$$
\boxed{
R_e
\subset
\mathcal K_X
\times
\mathcal K_Y.
}
$$

with:

1. source antecedent:
   $$
   \mathcal A_e\subset\mathcal K_X;
   $$
2. target constraint:
   $$
   \mathcal B_e\subset\mathcal K_Y;
   $$
3. proof status:
   $$
   I,C,E;
   $$
4. debt vector:
   $$
   d_e\in[0,\infty]^m;
   $$
5. provenance / scale / time metadata.

---

# 10. Disjunctive routing as hyperedge

Many C5 statements are:

$$
X
\Rightarrow
Y_1
\vee
Y_2
\vee
Y_3.
$$

This should be encoded as:

$$
\boxed{
X
\longrightarrow
\{Y_1,Y_2,Y_3\}
}
$$

a disjunctive hyperedge,

not three simultaneous mandatory ordinary edges.

Example:

root turnover:

$$
\boxed{
\text{TURNOVER}
\Rightarrow
\text{VISC}
\vee
\text{PROJECTED-NL}.
}
$$

---

# 11. Cycle composition

Consider typed edges:

$$
e_1:
X_1\to X_2,
$$

$$
e_2:
X_2\to X_3,
$$

$$
\ldots
$$

$$
e_m:
X_m\to X_1.
$$

Define the cycle compatibility set:

$$
\boxed{
\mathfrak C(e_1,\ldots,e_m)
=
R_{e_1}
\times_{\mathcal K_{X_2}}
R_{e_2}
\times_{\mathcal K_{X_3}}
\cdots
\times_{\mathcal K_{X_1}}
R_{e_m}.
}
$$

Informally:

the target metadata of every edge must satisfy the next edge's source antecedent.

---

# 12. C6-A.2: Composable Cycle Criterion

A projected label cycle:

$$
X_1\to\cdots\to X_m\to X_1
$$

is called:

$$
\boxed{
\textbf{certified composable}
}
$$

only if:

1. every edge has implication/conditional proof status;
2. all conditional antecedents are mutually compatible;
3. cycle compatibility set:
   $$
   \mathfrak C(e_1,\ldots,e_m)
   $$
   is nonempty;
4. no target state automatically triggers an external REG kill gate;
5. recurrent iteration preserves legality / scale / time metadata.

### Consequence

$$
\boxed{
\text{label SCC}
}
$$

is only an over-approximation to the certified cycle structure.

---

# 13. Recurrent closure is stronger than one-cycle composition

Even:

$$
\mathfrak C(e_1,\ldots,e_m)\ne\varnothing
$$

only certifies one compatible loop.

Infinite recurrent cycling needs an invariant or recurrent subset:

$$
\boxed{
\mathcal R_C
\subset
\mathfrak C(e_1,\ldots,e_m)
}
$$

whose image after one cycle intersects itself.

Thus there are three levels:

1. projected cycle;
2. composable cycle;
3. recurrent cycle.

C6 must not collapse them.

---

# 14. Candidate cycle T

C5-C established an abstract scalar-ledger no-go:

temporal middle/operator phases can remain separated while preserving positive record growth.

Thus:

$$
\boxed{
T
}
$$

is **not eliminated**.

But this is only:

$$
\boxed{
T
\overset{N}{\looparrowright}
T.
}
$$

C5-C did not construct a recurrent Navier–Stokes solution orbit carrying that scalar pattern.

Therefore:

$$
\boxed{
\textbf{$T$ is a candidate trap, not a certified PDE self-cycle.}
}
$$

---

# 15. Candidate cycle $G\leftrightarrow P$

Potential forward route:

$$
G\to P
$$

comes from strong-middle coherent geometry:

- Q cancellation excluded;
- mean rotation depleted;
- pressure must re-enter.

Potential reverse route:

$$
P\to G
$$

comes from:

- pressure axis locking;
- signature geometry;
- common far-pressure constraints;
- resulting compressive-axis / gap / dispersion obligations.

---

# 16. C6-A.3: $G/P$ Cycle Is Not Yet Certified

The $G\to P$ route typically requires:

$$
\boxed{
\text{strong-middle pointwise/mean coherence}
}
$$

and low mean rotation.

The $P\to G$ route may require:

$$
\boxed{
\text{common far-pressure dominance}
}
$$

plus pressure signature / axis geometry.

C5 has not proved that the $P$ state produced by the first edge automatically satisfies all antecedents needed for the reverse edge.

Also:

one-negative strong pressure may create an incompatibility rather than a re-entry state.

Therefore:

$$
\boxed{
G\leftrightarrow P
}
$$

is:

$$
\boxed{
\textbf{candidate compositional cycle},
}
$$

not a certified SCC.

---

# 17. $G/P$ cycle composition obligations

To certify:

$$
G\to P\to G,
$$

C6 must prove:

## GP-1 — provenance continuity

the pressure state created by G retains a far/local decomposition compatible with the reverse edge.

## GP-2 — signature compatibility

the pressure signature is not driven directly into an external contradiction.

## GP-3 — axis compatibility

the produced pressure-axis state maps into a legal gap/dispersion G state.

## GP-4 — recurrence

the new G state can re-enter the original strong-middle/pressure-producing antecedent after finite evolution.

None is currently automatic.

---

# 18. Candidate cycle $H\leftrightarrow F$

Forward route:

$$
H\to F
$$

is strongest when a persistent bad theorem window also has:

- unbounded root turnover;
- unbounded line roughness;
- clock/order congestion.

C5-J/L route these to:

$$
\boxed{
\text{VISC}
\vee
\text{PROJECTED-NL}
\subset F.
}
$$

---

# 19. Reverse route $F\to H$

C5 often says:

- viscous $D^{k+2}u$ activity shifts derivative activity upward;
- projected nonlinearity regenerates high-order complexity.

But:

$$
\boxed{
\textbf{high-order forcing activity}
}
$$

does **not** automatically imply:

$$
\boxed{
\textbf{a new legal Window-Persistent Sign Defect}.
}
$$

The new higher-order derivative field might instead satisfy:

- Theorem 3.5;
- Theorem 3.14 harmonic gate;
- another geometry/pressure route;
- no blow-up compatible state.

---

# 20. C6-A.4: $H/F$ Cycle Is Not Yet Certified

Thus:

$$
\boxed{
H\to F
}
$$

has certified subtype routings,

but:

$$
\boxed{
F\to H
}
$$

is currently only structural/candidate unless one proves:

> forcing congestion regenerates a theorem-legal persistent bad window at another derivative generation.

Therefore:

$$
\boxed{
H\leftrightarrow F
}
$$

is not yet a certified SCC.

---

# 21. $H/F$ cycle composition obligations

## HF-1 — forcing-to-amplitude

show F produces a nondegenerate next derivative amplitude on an admissible chain scale.

## HF-2 — amplitude-to-theorem-entry

show the new derivative level/time satisfies Grujić–Xu setup/remaining-time conditions.

## HF-3 — theorem-entry-to-window-failure

show every admissible later time in the new theorem window remains sign-thick.

## HF-4 — external-gate avoidance

show no fixed-$k$ / chain harmonic pass occurs on the re-entry.

## HF-5 — recurrent scaling

show this construction can repeat indefinitely with valid time remaining.

This is much stronger than coarse:

$$
F\to H.
$$

---

# 22. Possible graph SCC vs certified SCC

Define:

$$
\mathcal G^{may}
$$

using all non-excluded/conditional projected edges.

Then:

$$
\boxed{
\mathrm{SCC}(\mathcal G^{may})
=
\{
\{T\},
\{G,P,H,F\}
\}.
}
$$

Define:

$$
\mathcal G^{cert}
$$

using only fully composable implication transitions with verified endpoint compatibility.

Current audit:

$$
\boxed{
\textbf{no nontrivial recurrent SCC has yet been certified.}
}
$$

This does **not** mean cycles are impossible.

It means:

$$
\boxed{
\textbf{cycle existence itself has become a proof obligation.}
}
$$

---

# 23. Minimal survivor cycle certificate

A C6 minimal survivor cycle must include:

## MSC-1 — Typed edge completeness

every step has a legal transition relation.

## MSC-2 — Metadata composition

endpoint/source fiber products are nonempty.

## MSC-3 — External-gate avoidance

no state on the cycle automatically enters REG.

## MSC-4 — Recurrence

one full cycle returns to a compatible recurrent state set.

## MSC-5 — Time viability

infinite iteration fits below hypothetical:

$$
T^\ast.
$$

## MSC-6 — Debt viability

cycle debts can be paid indefinitely.

---

# 24. Cycle debt vector

For an edge:

$$
e,
$$

assign nonnegative debt vector:

$$
\boxed{
d(e)
=
(
d_T,
d_G,
d_P,
d_H,
d_F,
d_{clock},
d_{time},
\ldots
).
}
$$

For a finite cycle:

$$
C=(e_1,\ldots,e_m),
$$

define:

$$
\boxed{
D(C)
=
\sum_{j=1}^{m}
d(e_j).
}
$$

Debt coordinates may be:

- integral toll;
- defect mass;
- pressure critical mass;
- derivative load;
- root variation;
- clock variation;
- time span.

---

# 25. C6-A.5: Finite-Budget Cycle Exclusion Lemma

Suppose recurrent cycle generations:

$$
C_1,C_2,\ldots
$$

each pay a nonnegative scalar debt:

$$
b_n\ge0.
$$

If:

$$
\boxed{
\sum_{n=1}^{\infty}b_n
\le
B_0<\infty
}
$$

and:

$$
\boxed{
\inf_nb_n
\ge
b_0>0,
}
$$

then only finitely many cycle generations can occur.

### Proof

$$
Nb_0
\le
\sum_{n=1}^{N}b_n
\le
B_0.
$$

So:

$$
N\le B_0/b_0.
$$

$\square$

---

# 26. Critical-saturation cycle

The obstruction to C6-A.5 is exactly:

$$
\boxed{
b_n\downarrow0.
}
$$

A recurrent cycle can survive a finite total budget if the per-cycle toll shrinks fast enough.

This is the cycle-level analogue of:

- temporal load concentration;
- harmonic critical saturation;
- chain-clock critical saturation;
- UV scale-weighted Zeno costs.

Define:

$$
\boxed{
\textbf{Cycle Critical Saturation}
}
$$

when:

$$
D(C_n)\to\partial\mathcal D
$$

so every finite-cycle debt tends to zero in all globally finite-budget coordinates.

---

# 27. Why C5 debts did not already eliminate cycles

Several C5 debts are nondegenerate **within a normalized event**,

but their global weights may shrink with:

- spatial scale;
- derivative order;
- theorem-window length;
- core multiplicity;
- UV frequency.

Thus:

$$
\boxed{
\text{positive normalized debt}
}
$$

does not automatically give:

$$
\boxed{
\text{uniform positive global debt per cycle}.
}
$$

C6 must track both.

---

# 28. Debt coercivity

For cycle family:

$$
\mathcal C,
$$

a global budget functional:

$$
B
$$

is cycle-coercive if:

$$
\boxed{
d_B(C)
\ge
\epsilon_B>0
}
$$

for every cycle instance:

$$
C\in\mathcal C.
$$

If:

$$
B_{total}<\infty,
$$

then no infinite recurrent cycle in:

$$
\mathcal C
$$

exists.

This is the strongest simple route to cycle elimination.

---

# 29. Candidate $T$ debt status

Temporal class $T$ currently has:

- middle/operator normalized tolls;
- concentration masses;
- temporal phase measures.

But C5-C demonstrated scalar temporal compensation can stagger.

No known finite total-variation budget supplies a uniform positive cost for each abstract temporal cycle.

Thus:

$$
\boxed{
T\text{ candidate recurrence survives current budget audit}.
}
$$

---

# 30. Candidate $G/P$ debt status

$G/P$ cycle can incur:

- pressure critical mass;
- mean rotation;
- strain derivative fluctuation;
- vorticity leakage;
- middle-gap cubic intermittency.

However, shrinking/nested cores and provenance fragmentation prevent a currently known universal positive global toll per loop.

Therefore:

$$
\boxed{
G/P\text{ candidate cycle is not budget-excluded}.
}
$$

---

# 31. Candidate $H/F$ debt status

$H/F$ route incurs:

- persistent derivative-load strip;
- viscous $k+2$ toll;
- projected nonlinear turnover;
- order curvature;
- chain-clock variation.

But no known finite all-order global budget controls the sum of these quantities over an infinite derivative-order cascade.

Therefore:

$$
\boxed{
H/F\text{ candidate cycle is not budget-excluded}.
}
$$

---

# 32. Current cycle-certification table

| Candidate | Projected cycle | Typed composition | Recurrent certification | Uniform finite-budget exclusion |
|---|---:|---:|---:|---:|
| $T$ | yes | not applicable/self | no | no |
| $G\leftrightarrow P$ | yes | open | no | no |
| $H\leftrightarrow F$ | yes | open | no | no |
| larger $G/P/H/F$ SCC | yes in may graph | open | no | no |

This table is the key C6-A status.

---

# 33. C6-A.6: No Certified Nontrivial Cycle Yet

## Theorem-status statement

Within the current C5 routing database:

1. several projected/candidate cycles exist;
2. no nontrivial projected cycle has all endpoint/source metadata compatibility and recurrence conditions proved;
3. therefore no nontrivial recurrent PDE defect SCC is presently certified;
4. conversely none of the main candidates has been proved impossible.

Thus:

$$
\boxed{
\textbf{C6 begins at the cycle-composition frontier,
not at cycle elimination proper.}
}
$$

---

# 34. Why this is progress rather than retreat

Before C6-A:

$$
\boxed{
H\leftrightarrow F,\quad
G\leftrightarrow P
}
$$

could be misread as actual dynamical loops.

After C6-A:

each candidate loop comes with a finite checklist of missing composition theorems.

This replaces vague:

> maybe it cycles

with:

$$
\boxed{
\text{prove or refute a finite fiber-product compatibility problem}.
}
$$

---

# 35. Survivor trap vs SCC

A further distinction:

A set:

$$
S\subset V_6
$$

can be **not excluded as a survivor trap** even if it is not an SCC of certified implications.

Example:

$$
T
$$

is not excluded by scalar temporal ledgers,

but no PDE self-transition theorem exists.

Therefore C6 uses two notions:

## candidate trap

current theory does not force exit.

## certified recurrent SCC

actual composable transition relations generate recurrence.

Do not conflate them.

---

# 36. Disjunctive survivor kernel

For a typed state:

$$
\theta,
$$

suppose mandatory routing is:

$$
\theta
\Rightarrow
Y_1\vee\cdots\vee Y_m.
$$

A candidate trap:

$$
S
$$

must contain at least one allowed destination:

$$
\boxed{
S\cap\{Y_1,\ldots,Y_m\}\ne\varnothing.
}
$$

For many states this becomes an AND–OR / hypergraph viability problem rather than an ordinary SCC problem.

This is the correct combinatorial language for C6.

---

# 37. C6-A.7: Ordinary SCC Is an Over-Approximation of the Survivor Kernel

Project every disjunctive hyperedge:

$$
X\to\{Y_1,\ldots,Y_m\}
$$

to ordinary edges:

$$
X\to Y_i.
$$

Any certified recurrent hypergraph cycle projects to an ordinary graph cycle.

The converse fails.

Therefore, ordinary SCC analysis provides:

$$
\boxed{
\textbf{necessary candidate regions},
}
$$

not sufficient recurrent certificates.

---

# 38. Current priority ranking

C6-A ranks candidate cycle programs:

## Priority 1 — $H/F$

Reason:

- strongest theorem-ready interfaces;
- most explicit debt variables;
- $H\to F$ subtype routing already rigorous;
- missing reverse edge is sharply formulated.

## Priority 2 — $G/P$

Reason:

- finite-dimensional matrix obstructions already available;
- pressure provenance remains the main composition uncertainty.

## Priority 3 — $T$

Reason:

- pure temporal scalar no-go is strong;
- but universal temporal-to-spatial PDE coupling is still missing.

---

# 39. Why $H/F$ should be attacked first

To establish or kill:

$$
H\leftrightarrow F,
$$

one can target a concrete implication:

$$
\boxed{
\text{high-order forcing congestion}
\stackrel{?}{\Longrightarrow}
\text{next-generation persistent bad theorem window}.
}
$$

If FALSE:

forcing must exit to:

- harmonic pass;
- pressure/geometry;
- regularity.

If TRUE:

then H/F becomes the first genuinely certified recurrent-cycle candidate and C6 can attack its cycle debt.

Either outcome is high value.

---

# 40. Proposed C6-B

Next paper:

$$
\boxed{
\textbf{C6-B — High-Order Forcing Re-entry,
Bad-Window Regeneration, and the $H/F$ Cycle Test}.
}
$$

---

# 41. C6-B proof obligations

## B1 — Forcing event normalization

Define a next-generation forcing event from:

$$
\mathfrak V_k^{visc}
$$

or:

$$
\mathfrak V_k^{NL}.
$$

## B2 — Generation map

Determine natural target derivative order:

$$
k',
$$

time:

$$
t',
$$

and scale.

## B3 — theorem-entry legality

Check Grujić–Xu setup at:

$$
(k',t').
$$

## B4 — forcing-to-sign geometry

Can forcing alone imply a sign-thick superlevel set?

Likely no without additional coherence.

## B5 — harmonic escape branch

If the regenerated derivative field is sparse,

the external theorem gate closes.

## B6 — geometry/pressure exit

If forcing re-enters strain/pressure instead of H,

the route exits the H/F cycle.

## B7 — persistent-window regeneration

Identify the exact extra condition required for:

$$
F\to H.
$$

## B8 — cycle certification/refutation

Decide whether:

$$
H\leftrightarrow F
$$

fiber-product compatibility is nonempty under recurrent scaling.

---

# 42. C6 later targets

After H/F:

## C6-C

$$
\boxed{
\text{Geometry–Pressure Cycle Composition}
}
$$

## C6-D

$$
\boxed{
\text{Temporal-to-Spatial Universal Coupling}
}
$$

## C6-E

$$
\boxed{
\text{Minimal Certified Cycle Debt Audit}
}
$$

Naming may change depending on the C6-B result.

---

# 43. Edge proof-status ledger

C6 will store every edge as:

$$
\boxed{
e
=
(
X,
Y,
\mathcal A_e,
R_e,
d_e,
\sigma_e
)
}
$$

where:

- $X,Y$ classes;
- $\mathcal A_e$ antecedent;
- $R_e$ transition relation;
- $d_e$ debt;
- $\sigma_e\in\{I,C,N,E\}$ status.

This prevents future accidental promotion of a possibility edge into a theorem edge.

---

# 44. Metadata compatibility guard

For every cycle:

$$
e_1,\ldots,e_m,
$$

C6 must preserve:

- spatial scale;
- derivative order;
- time interval;
- pressure provenance;
- harmonic-sign carrier;
- ancestry;
- theorem setup;
- normalized amplitudes.

A cycle is invalid if any metadata type changes illegally.

This is the cycle-level version of X-Integration type guards.

---

# 45. C6 X-Integration guards

## G-CYCLETYPE

projected class labels are insufficient; store typed state metadata.

## G-EDGESEM

distinguish:

$$
I,C,N,E.
$$

## G-NEDGE

non-exclusion self-loop is not dynamics.

## G-FIBER

cycle certification requires a nonempty typed fiber product.

## G-REC

one compatible loop is weaker than a recurrent invariant loop.

## G-DEBT

cycle debt must distinguish normalized event debt from globally summable debt.

## G-SCCPROJ

ordinary SCCs are may-regions only.

## G-AOUT

$A$ stays outside the physical SCC until theorem-entry legality is proved.

---

# 46. True ETN update

C6 edge state:

$$
\boxed{
\mathfrak E^{C6}
=
(
\text{source state},
\text{antecedent},
\text{target relation},
\text{proof status},
\text{debt},
\text{kill gates}
).
}
$$

Cycle state:

$$
\boxed{
\mathfrak C^{C6}
=
(
e_1,\ldots,e_m,
\text{fiber compatibility},
\text{recurrence map},
D(C),
\text{budget coercivity}
).
}
$$

---

# 47. Formal status

$$
\boxed{
\begin{aligned}
\text{C5 may-graph SCC extraction}
&:\ \mathrm{COMPUTED},\\
\mathrm{SCC}_{may}
&:\ \{T\},\{G,P,H,F\},\\
\text{projected SCC}\Rightarrow\text{PDE cycle}
&:\ \mathrm{FALSE},\\
\text{typed transition semantics}
&:\ \mathrm{DEFINED},\\
\text{cycle fiber-product criterion}
&:\ \mathrm{DEFINED/PROVED\ LOGICALLY},\\
\text{ordinary SCC over-approximation}
&:\ \mathrm{PROVED},\\
T\text{ recurrent PDE self-cycle}
&:\ \mathrm{NOT\ CERTIFIED},\\
G\leftrightarrow P\text{ recurrent cycle}
&:\ \mathrm{NOT\ CERTIFIED},\\
H\leftrightarrow F\text{ recurrent cycle}
&:\ \mathrm{NOT\ CERTIFIED},\\
\text{nontrivial certified SCC}
&:\ \mathrm{NONE\ YET},\\
\text{candidate cycles impossible}
&:\ \mathrm{NOT\ PROVED},\\
\text{finite-budget cycle lemma}
&:\ \mathrm{PROVED},\\
\text{cycle critical saturation}
&:\ \mathrm{DEFINED},\\
\text{Navier--Stokes global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 48. Conclusion

After the formal launch of C6,

the first result is not:

> We have found a true SCC.

but rather the more important realization:

$$
\boxed{
\textbf{The coarse SCCs of C5-M can only serve as may-SCCs,
and cannot be directly treated as PDE recurrent SCCs.}
}
$$

If we project all C5 candidate arrows into an ordinary digraph,

we indeed obtain:

$$
\boxed{
\{T\},
\qquad
\{G,P,H,F\}.
}
$$

But:

$$
\boxed{
\text{edge exists}
}
$$

only means routing exists under a certain subtype/condition,

and does not mean all endpoint metadata can connect to the next edge.

Therefore, C6 introduces:

$$
\boxed{
R_e
\subset
\mathcal K_X\times\mathcal K_Y
}
$$

the typed transition relation,

and the cycle compatibility fiber product:

$$
\boxed{
\mathfrak C(e_1,\ldots,e_m).
}
$$

Only if:

$$
\boxed{
\mathfrak C\ne\varnothing
}
$$

and the recurrence / time / external-gate / debt conditions are all valid,

can it be qualified as a:

$$
\boxed{
\textbf{certified recurrent cycle}.
}
$$

Currently:

$$
T,
\qquad
G\leftrightarrow P,
\qquad
H\leftrightarrow F
$$

are all merely candidate traps/cycles.

Most importantly:

$$
\boxed{
\textbf{Currently, no nontrivial recurrent PDE defect cycle has been truly certified.}
}
$$

This precisely reformulates the C6 problem into a finite set of composition obligations.

Among them, the most mature is:

$$
\boxed{
H\leftrightarrow F.
}
$$

$H\to F$ already has the turnover/roughness routing from C5-J/L.

What is truly missing is:

$$
\boxed{
F
\stackrel{?}{\longrightarrow}
H,
}
$$

which is:

> Does high-order viscous / projected nonlinear forcing,
> truly regenerate a theorem-legal,
> next-generation defect that remains sign-thick throughout the entire admissible window?

Thus, the formal next paper is:

$$
\boxed{
\textbf{C6-B — High-Order Forcing Re-entry,
Bad-Window Regeneration, and the $H/F$ Cycle Test}.
}
$$

At this point, C6 has shifted from 'finding cycles' to:

$$
\boxed{
\textbf{proving whether cycles can truly connect end-to-end.}
}
$$

---

# References

1. Clay Mathematics Institute, *Navier–Stokes Equation*, Millennium Prize Problem status.
2. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, J. Math. Fluid Mech. 26, 53 (2024); arXiv:1911.00974.
3. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
4. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Ration. Mech. Anal. 235 (2020).
5. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.

# Internal dependencies

- `NS_C5M_UnifiedDefectGraph_C5PhaseClosure_v0.1.md`
- `NS_C5L_PersistentBadWindow_ClockDefect_RootTurnoverCompression_v0.1.md`
- `NS_C5K_ChainTime_WindowPersistent_DynamicInterpolationAudit_v0.1.md`
- `NS_C5J_LineSection_OrderSandwich_HarmonicSaturation_v0.1.md`
- `NS_C5I_SignGeometry_Chain_HarmonicCompatibility_v0.1.md`
- `NS_C5H_AllOrder_EffectiveVolume_AsymptoticCriticality_v0.1.md`
- `NS_C5G_PressureSignature_VorticityComplement_FixedOrderGate_v0.1.md`
- `NS_C5F_AxisPressureSignature_DerivativeGateEscalation_v0.1.md`
- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C6-B — High-Order Forcing Re-entry,
Bad-Window Regeneration, and the $H/F$ Cycle Test}
}
$$