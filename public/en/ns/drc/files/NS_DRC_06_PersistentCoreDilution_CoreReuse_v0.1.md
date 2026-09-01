---
title: "Navier–Stokes Dynamic Reservoir Closure Program 06: Persistent Core Dilution, Backward Concentration, Absolute UV Core Carriers and Core-Reuse Rigidity"
short_title: "NS-DRC 06"
series: "Navier–Stokes Dynamic Reservoir Closure Program"
cycle: "III"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style Type-I core normalization correction / reservoir-layer closure"
epistemic_status: "Uses Barker-Prange Type-I enstrophy concentration and backward propagation to replace global-share normalized core carriers by absolute scale-invariant local core carriers. Combines this with the CSP-02 local low-frequency exclusion to obtain an absolute ultraviolet core carrier at parabolic frequency or above. Proves a geometric same-center backward core-reuse chain and shows that vanishing global enstrophy share does not erase this local ancestry. A total-core dilution budget remains a useful diagnostic but is no longer needed for the existence of a state carrier. Barker-Prange's finite Type-I singular-point bound supplies finite final spatial-center branching. Consequently R_DIL is reclassified from a principal dynamic reservoir escape to a global-normalization/certificate defect within the Type-I branch. This does NOT rule out Type-I singularities, does NOT cover non-Type-I singularities, and does NOT prove Chain Necessity, Finite Obstruction, or Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Dynamic Reservoir Closure Program 06

# Persistent Core Dilution, Backward Concentration, Absolute UV Core Carriers and Core-Reuse Rigidity

## 0. Context of this Paper

DRC-05 reduced the principal unexplained dynamic reservoir core to:

$$
\boxed{
R_{\rm DIL}.
}
$$

This residual arose from the following situation.

A Type-I singular core may contain a shell or high-frequency state with strong **absolute local** vorticity mass, while its **global normalized share** tends to zero because much more enstrophy exists elsewhere.

The earlier program encoded this by a quantity such as:

$$
\beta_c(t)
=
\frac{
\text{global state mass assigned to the selected core shell}
}{
\text{total global enstrophy}
}.
$$

Small:

$$
\beta_c
$$

was then treated as a possible local/global ancestry failure.

The present paper identifies a normalization mistake in that interpretation.

For a singular-core ancestry, the primary state variable need not be a global probability share.

Barker--Prange already provide an absolute scale-invariant local enstrophy carrier at the singular point.

Therefore:

$$
\boxed{
\textbf{global dilution does not imply local core disappearance}.
}
$$

The correct Type-I core genealogy should be built from absolute local stock.

---

# 1. Type-I normalization

By translation and parabolic scaling set:

$$
\boxed{
(x_\ast,T_\ast)
=
(0,0).
}
$$

Assume:

$$
u
$$

is a suitable finite-energy Navier--Stokes solution on:

$$
\mathbb R^3\times[-1,0],
$$

satisfying the Type-I bound:

$$
\boxed{
\|u\|_{
L_t^\infty
L_x^{3,\infty}
(\mathbb R^3\times(-1,0))
}
\le
M.
}
$$

Assume:

$$
(0,0)
$$

is singular.

All Type-I statements in this paper retain these hypotheses.

---

# 2. Barker--Prange singular-core radius

Let:

$$
S^\sharp(M)
\in
(0,1/4]
$$

be the constant in Barker--Prange's concentration theorem.

Define:

$$
\boxed{
R_I(t)
=
4
(S^\sharp(M))^{-1/2}
(-t)^{1/2}.
}
$$

Thus:

$$
R_I(t)
\asymp_M
(-t)^{1/2}.
$$

---

# 3. External absolute enstrophy concentration

Barker--Prange prove that on a full-measure set:

$$
\Sigma
\subset
[-1,0),
$$

for every:

$$
t\in\Sigma,
$$

$$
\boxed{
\int_{
B_0(R_I(t))
}
|\omega(x,t)|^2dx
>
M^2
(-t)^{-1/2}
\sqrt{
S^\sharp(M)
}.
}
$$

Multiplying by:

$$
R_I(t)
$$

gives the scale-invariant form:

$$
\boxed{
R_I(t)
\int_{
B_0(R_I(t))
}
|\omega(x,t)|^2dx
>
4M^2.
}
$$

This is an **absolute local carrier theorem**.

No global enstrophy normalization appears.

---

# 4. Absolute Type-I core stock

Define:

$$
\boxed{
\mathcal C_I(t)
=
R_I(t)
\int_{
B_0(R_I(t))
}
|\omega(x,t)|^2dx.
}
$$

Then Barker--Prange gives:

$$
\boxed{
\mathcal C_I(t)
>
4M^2
}
$$

for:

$$
t\in\Sigma.
$$

The quantity:

$$
\mathcal C_I
$$

is invariant under Navier--Stokes scaling.

---

# 5. Why global share is secondary

Define the total-core global fraction:

$$
\boxed{
\beta_I(t)
=
\frac{
\int_{B_0(R_I(t))}
|\omega(x,t)|^2dx
}{
\|\omega(t)\|_2^2
}
}
$$

whenever:

$$
\|\omega(t)\|_2>0.
$$

Then:

$$
0<
\beta_I(t)
\le1.
$$

Small:

$$
\beta_I
$$

says:

> much more global enstrophy exists outside the singular core.

It does **not** say:

> the singular core has become small.

Indeed:

$$
\mathcal C_I(t)
>
4M^2
$$

remains true independently of:

$$
\beta_I(t).
$$

---

# 6. Total-core dilution budget

The absolute concentration implies:

$$
\|\omega(t)\|_2^2
\ge
\frac{
4M^2
}{
\beta_I(t)R_I(t)
}.
$$

The global energy inequality gives:

$$
\int_{-1}^0
\|\omega(t)\|_2^2dt
<
\infty.
$$

Therefore:

$$
\boxed{
\int_\Sigma
\frac{
dt
}{
\beta_I(t)R_I(t)
}
<
\infty.
}
$$

This is the total-core analogue of the earlier shell-dilution budget.

---

# 7. Meaning of the dilution budget

The budget remains useful.

It says extreme global dilution cannot occupy arbitrary weighted time.

However the existence of an absolute local state carrier does not depend on this budget.

Therefore:

$$
\boxed{
\text{dilution budget}
}
$$

is diagnostic rather than genealogically constitutive.

---

# 8. Low-frequency local bound

CSP-02 used the Type-I Lorentz bound and Lorentz--Bernstein estimates to prove:

$$
\boxed{
\|P_{\le J}\omega(t)\|_{
L^\infty
}
\le
C
2^{2J}
M.
}
$$

Hence:

$$
\boxed{
\|P_{\le J}\omega(t)\|_{
L^2(B_{R_I(t)})
}
\le
C
M
R_I(t)^{-1/2}
\left(
2^J
R_I(t)
\right)^2.
}
$$

---

# 9. Parabolic core frequency

Choose:

$$
J_I(t)
$$

so that:

$$
\boxed{
2^{J_I(t)}
R_I(t)
\le
\kappa_0
<
2^{J_I(t)+1}
R_I(t),
}
$$

where:

$$
\kappa_0>0
$$

is sufficiently small.

Thus:

$$
\boxed{
2^{J_I(t)}
\asymp
R_I(t)^{-1}.
}
$$

---

# 10. CIII-6.1 — Absolute UV Core Extraction

## Theorem 10.1

For every:

$$
t\in\Sigma,
$$

with the parabolic cutoff:

$$
J_I(t),
$$

one has:

$$
\boxed{
\|
P_{>J_I(t)}
\omega(t)
\|_{
L^2(B_{R_I(t)})
}
\ge
c
M
R_I(t)^{-1/2}.
}
$$

Equivalently:

$$
\boxed{
R_I(t)
\|
P_{>J_I(t)}
\omega(t)
\|_{
L^2(B_{R_I(t)})
}^2
\ge
c
M^2.
}
$$

### Proof

Barker--Prange gives:

$$
\|\omega(t)\|_{
L^2(B_{R_I})
}
>
2M
R_I^{-1/2}.
$$

By the choice of:

$$
\kappa_0,
$$

the low-frequency estimate gives:

$$
\|P_{\le J_I}\omega(t)\|_{
L^2(B_{R_I})
}
\le
M
R_I^{-1/2}.
$$

Use:

$$
\omega
=
P_{\le J_I}\omega
+
P_{>J_I}\omega
$$

and the triangle inequality.

$\square$

---

# 11. Main consequence

The Type-I singular core contains a uniformly nontrivial scale-invariant ultraviolet state:

$$
\boxed{
\mathcal C_I^{UV}(t)
=
R_I(t)
\|
P_{>J_I(t)}
\omega(t)
\|_{
L^2(B_{R_I(t)})
}^2
\ge
cM^2.
}
$$

This statement is independent of any global shell/enstrophy share.

---

# 12. External backward concentration

Barker--Prange also prove a backward propagation theorem.

There exist universal constants:

$$
C^\sharp\in(0,1/16),
$$

and:

$$
M_3\ge1,
$$

such that for:

$$
M\ge M_3,
$$

if at a time:

$$
t'
$$

the Type-I enstrophy concentration holds, then it also holds at every sufficiently well-separated earlier time:

$$
t''<t'
$$

satisfying:

$$
\boxed{
\frac{
-t'
}{
-t''
}
<
C^\sharp
M^{-548}.
}
$$

The concentration remains centered at:

$$
x=0
$$

with radius proportional to:

$$
(-t'')^{1/2}.
$$

---

# 13. Geometric backward times

Fix:

$$
\boxed{
0<\rho
<
C^\sharp
M^{-548}.
}
$$

Let:

$$
t_n
=
-\rho^n
$$

for all sufficiently large:

$$
n
$$

so:

$$
t_n\in[-1,0).
$$

Then:

$$
t_n\uparrow0,
$$

and:

$$
\boxed{
\frac{
-t_n
}{
-t_{n-1}
}
=
\rho
<
C^\sharp
M^{-548}.
}
$$

Thus:

$$
t_{n-1}
$$

is an admissible well-separated backward time for:

$$
t_n.
$$

---

# 14. CIII-6.2 — Same-Center Core-Reuse Chain

## Theorem 14.1

For the geometric times:

$$
t_n=-\rho^n,
$$

the Type-I singular core yields an arbitrarily deep same-center backward state chain:

$$
\boxed{
\mathcal K_n
=
\left(
t_n,
B_0(R_I(t_n)),
\mathcal C_I(t_n)
\right),
}
$$

with:

$$
\boxed{
\mathcal C_I(t_n)
>
4M^2.
}
$$

The backward parent core:

$$
\mathcal K_{n-1}
$$

has the same center and a larger parabolic radius:

$$
\boxed{
R_I(t_{n-1})
=
\rho^{-1/2}
R_I(t_n).
}
$$

### Proof

Lemma 3.2 provides concentration on the full-measure singular-core time set.

Alternatively, once concentration is chosen at a sufficiently late:

$$
t_n,
$$

Barker--Prange backward propagation gives the same concentration at:

$$
t_{n-1},
$$

and iteration gives arbitrarily deep finite chains.

The radius formula follows from:

$$
R_I(t)\asymp_M(-t)^{1/2}.
$$

$\square$

---

# 15. Core reuse, not core migration

Theorem 14.1 has an important geometric meaning:

$$
\boxed{
\text{the backward Type-I ancestry reuses the same singular center}.
}
$$

The balls expand backward:

$$
B_0(R_I(t_n))
\subset
B_0(R_I(t_{n-1})).
$$

Therefore the Type-I concentration theorem does not force repeated creation of unrelated spatial cores.

It already supplies a nested same-center core genealogy.

---

# 16. CIII-6.3 — Absolute UV Core-Reuse Chain

## Theorem 16.1

At every selected core time:

$$
t_n,
$$

choose:

$$
J_n
=
J_I(t_n)
$$

with:

$$
2^{J_n}
R_I(t_n)
\asymp1.
$$

Then:

$$
\boxed{
R_I(t_n)
\|
P_{>J_n}
\omega(t_n)
\|_{
L^2(B_{R_I(t_n)})
}^2
\ge
cM^2.
}
$$

Moreover:

$$
\boxed{
J_n-J_{n-1}
=
\frac12
\log_2
\left(
\frac1{\rho}
\right)
+
O(1).
}
$$

Thus the same-center backward core chain carries a scale-compatible UV state at every generation.

### Proof

Apply Theorem 10.1 at every:

$$
t_n.
$$

Since:

$$
2^{J_n}
\asymp
R_I(t_n)^{-1},
$$

the frequency increment is the logarithm of the fixed radius ratio.

$\square$

---

# 17. Meaning for ancestry

The state chain:

$$
\boxed{
(t_n,R_n,J_n,\mathcal C_n^{UV})
}
$$

has:

- a fixed spatial center;
- geometric parabolic radii;
- bounded deterministic frequency increment per generation;
- a uniform absolute scale-invariant UV lower bound.

No global enstrophy probability normalization is required.

This is a stronger state carrier for the Type-I branch than:

$$
\beta_c(t).
$$

---

# 18. Global dilution cannot erase the chain

Let:

$$
\beta_I(t_n)\to0
$$

along the core-reuse chain.

Then:

$$
\|\omega(t_n)\|_2^2
$$

must grow relative to the core mass.

But Theorems 14.1 and 16.1 remain unchanged.

Therefore:

$$
\boxed{
\beta_I(t_n)\to0
\not\Rightarrow
\text{loss of local core ancestry}.
}
$$

It only implies increasing global enstrophy outside or beyond the normalized core fraction.

---

# 19. CIII-6.4 — Dilution-Invariant Local Carrier Theorem

## Theorem 19.1

Any ancestry/certificate rule whose state requirement is:

$$
\boxed{
R_I(t)
\|
P_{>J_I(t)}
\omega(t)
\|_{
L^2(B_{R_I(t)})
}^2
\ge
cM^2
}
$$

is invariant under arbitrary values of:

$$
\beta_I(t)\in(0,1].
$$

In particular, global dilution cannot be used as a failure certificate for the existence of the Type-I UV core carrier.

$\square$

---

# 20. Why the old R-DIL appeared

The earlier program normalized a local core shell by a **global** enstrophy total in order to compare it with global spectral carrier probabilities.

That was useful for:

- global shell atomization;
- spectral-variance comparison;
- global finite-carrier bookkeeping.

But it was stronger than necessary for local Type-I ancestry.

Thus:

$$
\boxed{
R_{\rm DIL}
}
$$

was partly produced by demanding a global probability representation for an inherently local singular-core state.

---

# 21. Global normalization remains useful

This correction does not make:

$$
\beta_I
$$

meaningless.

The dilution budget:

$$
\int
\frac{
dt
}{
\beta_I(t)R_I(t)
}
<
\infty
$$

still quantifies how much global enstrophy must exist outside the core.

It may be useful for:

- global multiplicity estimates;
- interaction with multiple cores;
- quantitative energy accounting.

But it is not required to preserve the local dangerous state.

---

# 22. Local shell extraction is optional

The absolute UV core:

$$
P_{>J_I}\omega
$$

may be further decomposed into dyadic shells if a later theorem requires shell resolution.

If no single shell has a fixed local share, one may retain the entire high tail as the state node.

The DRC renewal machinery already supports high-pass state nodes:

$$
P_{\ge J}S,
$$

rather than requiring one shell at every stage.

Therefore local many-shell distribution does not force reintroduction of a global dilution variable.

---

# 23. Same-shell strain/vorticity pseudolocality

If a dyadic core shell is selected, CSP-06 proved band-passed pseudolocality:

$$
\omega_j
\leftrightarrow
S_j
$$

after fixed wavelength spatial padding.

Thus a local vorticity shell carrier may be converted into a local strain shell carrier without invoking its global share.

This further removes the need for:

$$
\beta_c
$$

in the local alignment step.

---

# 24. Source genealogy from an absolute local core

The DRC-01--05 source genealogy is built from absolute high-frequency state norms and Duhamel source packets.

It does not require the high-frequency state to be a fixed fraction of **total global enstrophy**.

Hence the absolute Type-I UV core can enter the DRC genealogy directly after an appropriate local/global cutoff interface is supplied.

The remaining difficulty is representation/completeness of that interface, not dilution.

---

# 25. Finite final singular-center branching

Barker--Prange additionally prove that, under the same Type-I bound, the number of blow-up points at the final time is finite and admits an explicit bound depending only on:

$$
M.
$$

In their quantitative estimate:

$$
\boxed{
N_{\rm sing}(T_\ast)
\le
\exp
(
\exp
(
M^{1024}
)
).
}
$$

This is an external standard-PDE finite spatial branching theorem for the final Type-I singular set.

---

# 26. CIII-6.5 — Type-I Finite Spatial-Center Branching

## Theorem 26.1

Under the Barker--Prange Type-I hypotheses, the final singular-center set contains at most:

$$
\boxed{
N_M
=
\exp
(
\exp
(
M^{1024}
)
)
}
$$

points.

For each such singular center:

$$
x_\ast,
$$

the concentration theorem supplies a corresponding same-center backward parabolic core chain.

### Status

The finite singular-point count is EXTERNAL.

The combination with Theorem 14.1 is an internal genealogy interpretation.

$\square$

---

# 27. Spatial branching interpretation

At the Type-I singular-center layer:

$$
\boxed{
\text{spatial branching is finite}.
}
$$

Within each branch:

$$
\boxed{
\text{the center is reused backward}.
}
$$

Thus global dilution does not create an unbounded number of singular-center ancestors.

It may still represent large regular/non-singular enstrophy elsewhere.

That extra enstrophy does not erase the chosen singular branch.

---

# 28. Core-reuse versus global enstrophy inflation

If:

$$
\beta_I(t_n)\to0,
$$

then:

$$
\|\omega(t_n)\|_2^2
\ge
\frac{
cM^2
}{
\beta_I(t_n)R_I(t_n)
}.
$$

So dilution converts into global enstrophy inflation.

However this inflation is a cost of the ambient solution, not a failure of the local core carrier.

The energy budget controls its temporal persistence but is not needed for the branch to exist.

---

# 29. CIII-6.6 — R-DIL Reclassification Theorem

## Theorem 29.1

Within the Type-I singular-core branch of the CSP/DRC architecture:

$$
\boxed{
R_{\rm DIL}
}
$$

is not an independent **dynamic reservoir escape**.

More precisely:

1. absolute scale-invariant local enstrophy concentration persists independently of global share;
2. an absolute parabolic-or-higher-frequency UV core carrier exists independently of global share;
3. backward concentration gives an arbitrarily deep same-center parabolic core chain;
4. final singular-center branching is finite;
5. vanishing global share only increases the amount of enstrophy outside the normalized core and is constrained by a secondary energy budget.

Therefore:

$$
\boxed{
R_{\rm DIL}
\longrightarrow
\text{global-normalization / energy-accounting layer},
}
$$

not:

$$
\boxed{
\text{loss of the Type-I dangerous state}.
}
$$

### Safety

This theorem does not prove that the Type-I dangerous state is impossible.

It proves that dilution does not remove it.

$\square$

---

# 30. Principal Type-I reservoir residual

Before DRC-06:

$$
\boxed{
\mathfrak R_{\rm III}^{(5)}
=
R_{\rm DIL}.
}
$$

After DRC-06, at the **reservoir-mechanism classification layer**:

$$
\boxed{
\mathfrak R_{\rm III,res}^{Type-I,reservoir}
=
\varnothing.
}
$$

This means:

> every principal reservoir escape introduced in Cycle II/III has either been absorbed into a standard coercive action/source genealogy, or reclassified as a certificate/normalization issue.

It does **not** mean:

$$
\boxed{
\text{Type-I singularity is impossible}.
}
$$

---

# 31. What remains open after reservoir closure?

Several harder obligations remain.

### O1 — Non-Type-I coverage

The Barker--Prange core chain used here assumes:

$$
L_t^\infty
L_x^{3,\infty}
$$

Type-I control.

General hypothetical singularity formation is not reduced to this branch.

### O2 — Full Chain Necessity

The RFP still has not proved that every hypothetical singularity admits the complete source-traceable infinite ancestry required by the program.

### O3 — Local/global source interface

The absolute local UV core must be interfaced with the global/semiglobal Duhamel source genealogy without hidden representation gaps.

### O4 — Finite Obstruction

Even if a dangerous ancestry chain exists, no finite family of dynamical guards has been proved to block every such chain.

### O5 — Realizability

The current necessary mechanisms are not shown mutually inconsistent.

---

# 32. Why this is not a regularity proof

The program has now explained many ways a hypothetical dangerous state can be:

- spatially concentrated;
- spectrally distributed;
- temporally delayed;
- preloaded;
- replenished;
- cancelled;
- multiplied over parents;
- placed near the dissipation boundary;
- globally diluted.

But explaining a mechanism is not excluding it.

A Type-I singularity could, in principle, realize the entire surviving coercive/source genealogy.

Thus:

$$
\boxed{
\text{reservoir mechanism classification closure}
\neq
\text{Navier--Stokes regularity}.
}
$$

---

# 33. Candidate Type-I ancestry skeleton

The current Type-I branch may now be summarized as:

$$
\boxed{
\text{singular point}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{absolute parabolic enstrophy core}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{absolute UV core stock}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{high-frequency Duhamel renewal}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{model-cone residual}
\vee
\text{vorticity-parent renewal}
\vee
\text{low-mode driver ancestry}
}
$$

with:

- scale/shell/spatial defects already typed;
- cancellation bypassed by net-shell grouping;
- parent multiplicity absorbed into dissipation-span geometry;
- global dilution no longer erasing the local state.

This is a candidate ancestry skeleton, not yet Full Chain Necessity.

---

# 34. New guards

Add:

### $G_{\rm ABSCORE}$

Type-I singular-core ancestry must preserve the absolute scale-invariant local enstrophy stock:

$$
R_I
\int_{B_{R_I}}
|\omega|^2.
$$

### $G_{\rm ABSUV}$

The local UV state must be tracked by absolute high-tail mass, not only a global shell share.

### $G_{\rm COREREUSE}$

Backward Type-I concentration preserves the same singular center and parabolic radius scaling.

### $G_{\rm DILSEM}$

Vanishing global core share is a global normalization cost, not disappearance of the local state.

### $G_{\rm FINCENTER}$

Under Type-I control, final singular-center branching is finite.

---

# 35. Cycle-III frontier update

The reservoir program has now reached a natural closure point.

All principal dynamic reservoir residual classes from Cycle II:

$$
R_{\rm EXP},
\quad
R_{\rm DISS},
\quad
R_{\rm DIL},
\quad
R_{\rm SRC}
$$

have been:

- absorbed into source/driver actions;
- compressed into finite state genealogy;
- or reclassified as non-dynamical certificate/normalization geometry.

The next paper should therefore no longer invent a new reservoir defect.

It should perform a full Cycle-III audit.

---

# 36. Next paper

$$
\boxed{
\textbf{
NS-DRC 07 —
Unified Dynamic Reservoir Cover,
Type-I Ancestry Recompilation,
Chain-Necessity Audit
and Cycle-III Closure
}.
}
$$

Primary tasks:

1. compile DRC-01--06 into a standard-PDE theorem/status document;
2. distinguish:
   $$
   \text{reservoir closure}
   $$
   from:
   $$
   \text{Chain Necessity};
   $$
3. audit every local/global transition for hidden representation gaps;
4. state the strongest Type-I ancestry theorem actually proved;
5. identify the non-Type-I frontier;
6. retest Candidate Dynamical Cover / Finite Obstruction;
7. close Cycle III with no regularity overclaim.

---

# 37. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Barker--Prange absolute Type-I enstrophy core}
&:\ \mathrm{EXTERNAL},\\
\text{absolute UV core extraction}
&:\ \mathrm{PROVED},\\
\text{Barker--Prange backward core propagation}
&:\ \mathrm{EXTERNAL},\\
\text{same-center geometric core-reuse chain}
&:\ \mathrm{PROVED},\\
\text{absolute UV core-reuse chain}
&:\ \mathrm{PROVED},\\
\text{total-core dilution budget}
&:\ \mathrm{PROVED},\\
\text{dilution-invariant local carrier}
&:\ \mathrm{PROVED},\\
\text{finite Type-I singular-point count}
&:\ \mathrm{EXTERNAL},\\
R_{\rm DIL}\text{ as principal dynamic reservoir escape}
&:\ \mathrm{RECLASSIFIED/REMOVED},\\
\text{Type-I reservoir residual core}
&:\ \mathrm{EMPTY\ RELATIVE\ TO\ DRC\ CLASSIFICATION},\\
\text{non-Type-I reservoir coverage}
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

# 38. Conclusion

The final principal reservoir residual of Cycle III arose from a normalization choice.

Barker--Prange already prove an absolute Type-I singular-core carrier:

$$
\boxed{
R_I(t)
\int_{B_{R_I(t)}}
|\omega|^2
>
4M^2.
}
$$

CSP/DRC low-frequency exclusion upgrades this to an absolute local UV carrier:

$$
\boxed{
R_I(t)
\|
P_{>J_I(t)}
\omega
\|_{L^2(B_{R_I(t)})}^2
\ge
cM^2,
\qquad
2^{J_I(t)}R_I(t)\asymp1.
}
$$

Barker--Prange backward propagation then supplies an arbitrarily deep same-center parabolic core chain.

None of these statements depends on the core being a fixed fraction of global enstrophy.

Therefore:

$$
\boxed{
\beta_I(t)\to0
}
$$

does not destroy the dangerous local state.

It only means the ambient global enstrophy is even larger.

Thus:

$$
\boxed{
R_{\rm DIL}
}
$$

is reclassified as a global-normalization / energy-accounting issue, not a principal dynamic reservoir escape.

At the Type-I reservoir-classification layer, no unexplained reservoir mechanism remains.

The next question is no longer:

> What other reservoir escape is missing?

It is:

> Have we actually proved that every hypothetical singularity must enter this ancestry architecture, and can any such ancestry be dynamically obstructed?

Those are the Chain Necessity and Finite Obstruction problems.

---

# References

1. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717v3.
2. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487--1541; arXiv:1812.09115v2.
3. `NS_CSP_02_SpatialAtom_TypeI_CoreExtraction_ParabolicPacking_v0.1.md`.
4. `NS_CSP_06_StaleFloor_ModelCone_CoreAlignment_v0.1.md`.
5. `NS_DRC_05_DissipationRange_DriverClosure_v0.1.md`.