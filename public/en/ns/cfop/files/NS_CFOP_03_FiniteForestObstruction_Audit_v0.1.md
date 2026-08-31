---
title: "Navier–Stokes Causal Forest Obstruction Program 03: Finite Forest Obstruction, Universal Budget Audit, Negative-Sobolev Forcing, Sparse/Dense Geometry and Cycle-V Closure"
short_title: "NS-CFOP 03"
series: "Navier–Stokes Causal Forest Obstruction Program"
cycle: "V"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Cycle-V closure / finite forest obstruction audit / missing-coercivity theorem"
epistemic_status: "Audits every remaining CFOP forest residual against genuinely universal Navier-Stokes a priori budgets. Proves an energy-class negative-Sobolev nonlinear forcing budget: the velocity nonlinearity belongs to L_t^{4/3}H_x^{-1}, and the vorticity forcing to L_t^{4/3}H_x^{-2}, with a bound controlled by kinetic energy and dissipation. Rewrites source-dominated forest cuts as a finite weak-forcing / high-dual-congestion alternative and proves infinitely many disjoint source-dominated cuts force divergence of quartic H^2 dual congestion rather than forcing-action divergence. Reclassifies weighted state-tail escape as adaptive spatial-capacity growth. Performs a scaling audit showing both the Leray enstrophy-time budget and the energy-class H^{-2} forcing budget have summable per-parabolic-scale costs (respectively O(R) and O(R^{4/3})) and therefore cannot by themselves exclude an infinite geometric cascade. Partial-regularity and geometric-sparseness results are imported only as external conditional guards/calibration. The paper concludes that the current standard finite budgets do not yield a complete Finite Forest Obstruction. The missing theorem is a forest-level coercive budget with near-critical scaling and a universal finite Navier-Stokes bound. No Navier-Stokes regularity claim is made."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Causal Forest Obstruction Program 03

# Finite Forest Obstruction, Universal Budget Audit, Negative-Sobolev Forcing, Sparse/Dense Geometry and Cycle-V Closure

## 0. Problem Statement

CFOP-02 reduced a horizon-unbounded diffuse causal forest to the residual ledger:

$$
\boxed{
R_{F\mbox{-}ACT}
\vee
R_{F\mbox{-}CONG}
\vee
R_{F\mbox{-}CAP}
\vee
R_{F\mbox{-}TAIL}
\vee
R_{F\mbox{-}NSPARSE}.
}
$$

The present paper asks the decisive question:

> Does standard Navier--Stokes theory provide universal finite budgets that close all five classes?

The answer is:

$$
\boxed{
\textbf{No.}
}
$$

However the audit does eliminate several residuals as primitive and isolates the missing form of estimate.

---

# 1. Velocity nonlinearity

Write Navier--Stokes as:

$$
\boxed{
\partial_tu
-
\nu\Delta u
=
\mathcal N,
}
$$

where:

$$
\boxed{
\mathcal N
=
-
\mathbb P
\nabla\cdot
(
u\otimes u
).
}
$$

For:

$$
\varphi\in H^1(\mathbb R^3),
$$

$$
|
\langle
\mathcal N,\varphi
\rangle
|
\le
C
\|u\|_4^2
\|\nabla\varphi\|_2.
$$

Therefore:

$$
\boxed{
\|\mathcal N\|_{H^{-1}}
\le
C
\|u\|_4^2.
}
$$

---

# 2. Energy interpolation

The three-dimensional Gagliardo--Nirenberg inequality gives:

$$
\boxed{
\|u\|_4
\le
C
\|u\|_2^{1/4}
\|\nabla u\|_2^{3/4}.
}
$$

Hence:

$$
\boxed{
\|\mathcal N\|_{H^{-1}}
\le
C
\|u\|_2^{1/2}
\|\nabla u\|_2^{3/2}.
}
$$

Raise to:

$$
4/3:
$$

$$
\boxed{
\|\mathcal N\|_{H^{-1}}^{4/3}
\le
C
\|u\|_2^{2/3}
\|\nabla u\|_2^2.
}
$$

---

# 3. CIV/V-3.1 — Universal Negative-Sobolev Forcing Budget

## Theorem 3.1

Let:

$$
E_2
=
\sup_{0<t<T_\ast}
\|u(t)\|_2.
$$

For every Leray--Hopf solution:

$$
\boxed{
\int_0^{T_\ast}
\|\mathcal N(t)\|_{H^{-1}}^{4/3}dt
\le
C
E_2^{2/3}
\int_0^{T_\ast}
\|\nabla u(t)\|_2^2dt
<
\infty.
}
$$

Using the energy inequality:

$$
\boxed{
\int_0^{T_\ast}
\|\mathcal N\|_{H^{-1}}^{4/3}dt
\le
C_\nu
E_2^{8/3}.
}
$$

### Status

This is a universal finite nonlinear forcing budget in the energy class.

$\square$

---

# 4. Vorticity forcing

The vorticity equation may be written:

$$
\boxed{
\partial_t\omega
-
\nu\Delta\omega
=
\mathcal G,
}
$$

with:

$$
\boxed{
\mathcal G
=
-
\nabla\times
\mathcal N.
}
$$

Therefore:

$$
\boxed{
\|\mathcal G\|_{H^{-2}}
\le
C
\|\mathcal N\|_{H^{-1}}.
}
$$

---

# 5. Corollary — Universal vorticity-source budget

## Corollary 5.1

$$
\boxed{
\mathfrak B_{-2}
=
\int_0^{T_\ast}
\|\mathcal G(t)\|_{H^{-2}}^{4/3}dt
<
\infty.
}
$$

Moreover:

$$
\boxed{
\mathfrak B_{-2}
\le
C_\nu
E_2^{8/3}.
}
$$

$\square$

---

# 6. Why CFOP-01 used a stronger action

CFOP-01/02 used:

$$
\int
\sum_k
\|F_k\|_2^2dt.
$$

This is a much stronger forcing topology.

No universal finite energy-class bound for that action is available.

The present paper replaces it, where appropriate, by the genuinely finite:

$$
L_t^{4/3}H_x^{-2}
$$

vorticity-forcing budget.

The price is a stronger dual congestion norm.

---

# 7. H2 dual load

Let:

$$
\mathcal T
=
\{
T_r
\}
$$

be a finite dangerous-terminal ensemble with weights:

$$
w_r,
\qquad
\sum_rw_r=1.
$$

Let:

$$
\Psi_r(s)
$$

be the normalized terminal dual witness used in the causal cut ledger.

Define:

$$
\boxed{
\mathfrak C_2(s)
=
\sum_{
r:
s<t_r
}
w_r
\|
\Psi_r(s)
\|_{H^2}.
}
$$

Define quartic dual congestion:

$$
\boxed{
\mathfrak K_2(I)
=
\int_I
\mathfrak C_2(s)^4ds.
}
$$

---

# 8. Weak-forcing source demand

Let:

$$
I=[\tau,t_{\max}].
$$

The ensemble normalized source demand obeys:

$$
\overline S(I)
\le
\int_I
\|\mathcal G(s)\|_{H^{-2}}
\mathfrak C_2(s)ds.
$$

Use Hölder with exponents:

$$
4/3
\quad\text{and}\quad
4.
$$

---

# 9. CIV/V-3.2 — Weak-Forcing / Strong-Dual Congestion Duality

## Theorem 9.1

If:

$$
\overline S(I)
\ge
\sigma>0,
$$

then:

$$
\boxed{
\left(
\int_I
\|\mathcal G\|_{H^{-2}}^{4/3}dt
\right)^3
\mathfrak K_2(I)
\ge
\sigma^4.
}
$$

Equivalently, with:

$$
\mathfrak B_{-2}(I)
=
\int_I
\|\mathcal G\|_{H^{-2}}^{4/3}dt,
$$

$$
\boxed{
\mathfrak K_2(I)
\ge
\frac{
\sigma^4
}{
\mathfrak B_{-2}(I)^3
}.
}
$$

$\square$

---

# 10. Infinite source cuts

Let:

$$
I_n
$$

be pairwise disjoint source-dominated cut intervals with one fixed:

$$
\sigma>0.
$$

Since:

$$
\sum_n
\mathfrak B_{-2}(I_n)
\le
\mathfrak B_{-2}
<
\infty,
$$

one has:

$$
\boxed{
\mathfrak B_{-2}(I_n)
\to0.
}
$$

Therefore Theorem 9.1 gives:

$$
\boxed{
\mathfrak K_2(I_n)
\to\infty
}
$$

along the source-cut sequence.

---

# 11. CIV/V-3.3 — Source-Action Reclassification

## Theorem 11.1

For infinitely many pairwise disjoint source-dominated dangerous cuts:

$$
\boxed{
\text{unbounded strong }L^2\text{ forcing action}
}
$$

is not required.

Instead the universal energy-class source budget forces:

$$
\boxed{
\text{quartic }H^2\text{ dual congestion}\to\infty.
}
$$

Thus:

$$
\boxed{
R_{F\mbox{-}ACT}
}
$$

is not primitive when forcing is measured in the natural energy-class negative topology.

It is reclassified as:

$$
\boxed{
R_{F\mbox{-}HCONG}.
}
$$

### Safety

This does not show the forest is impossible.

High-frequency dual witnesses may naturally have large:

$$
H^2
$$

norms.

$\square$

---

# 12. Interpretation of strong dual congestion

A dangerous terminal witness is a fine-scale observable.

The weaker the source norm used to obtain a finite universal PDE budget, the stronger the dual norm needed to detect that source.

Thus the action/congestion tradeoff is partly a Sobolev-duality phenomenon:

$$
\boxed{
\text{weaker universally finite source topology}
\Longleftrightarrow
\text{stronger dual congestion}.
}
$$

This is not an artifact to be silently normalized away.

---

# 13. Adaptive capture radius

Let:

$$
g(x)
=
\sum_{k\in\mathcal K}
\psi(x)
|\omega_k(x)|^2.
$$

Assume:

$$
g\in L^1,
\qquad
\int g>0.
$$

For every:

$$
\varepsilon\in(0,1),
$$

there exists finite:

$$
R_\varepsilon
$$

such that:

$$
\boxed{
\int_{
B(c_\psi,R_\varepsilon)
}
g(x)dx
\ge
(1-\varepsilon)
\int g.
}
$$

---

# 14. Minimal adaptive span

Define:

$$
\boxed{
R_\varepsilon^\ast
=
\inf
\left\{
R:
\int_{
B(c_\psi,R)
}
g
\ge
(1-\varepsilon)\int g
\right\}.
}
$$

For a reference shell:

$$
J,
$$

define:

$$
\boxed{
\Xi_\varepsilon
=
2^J
R_\varepsilon^\ast.
}
$$

---

# 15. CIV/V-3.4 — State-Tail / Capacity Reclassification

## Theorem 15.1

For every fixed finite weighted state:

$$
\boxed{
R_\varepsilon^\ast<\infty.
}
$$

Hence failure of one **uniform** controlled recapture radius along a forest sequence means:

$$
\boxed{
\Xi_\varepsilon\to\infty
}
$$

or shell-reference drift.

Therefore:

$$
\boxed{
R_{F\mbox{-}TAIL}
\subset
R_{F\mbox{-}CAP}.
}
$$

State-tail escape is not a primitive forest residual once adaptive capture radius is included in the node capacity coordinates.

$\square$

---

# 16. Updated primitive forest residual

After Theorems 11.1 and 15.1:

$$
\boxed{
\mathfrak R_{\rm Forest}^{(3)}
=
R_{F\mbox{-}HCONG}
\vee
R_{F\mbox{-}CAP}
\vee
R_{F\mbox{-}NSPARSE}.
}
$$

The earlier strong forcing-action and state-tail labels are no longer primitive.

---

# 17. Scaling of the Leray budget

Under Navier--Stokes scaling:

$$
u^{(\lambda)}(x,t)
=
\lambda
u(\lambda x,\lambda^2t),
$$

a physical scale:

$$
R
$$

corresponds to:

$$
\lambda=R^{-1}.
$$

For a Type-I/parabolic dangerous core:

$$
\boxed{
\|\omega\|_2^2
\sim
R^{-1}.
}
$$

A parabolic epoch has length:

$$
\boxed{
\Delta t
\sim
R^2.
}
$$

Thus the enstrophy-time cost per scale is:

$$
\boxed{
R^{-1}R^2
=
R.
}
$$

---

# 18. CIV/V-3.5 — Enstrophy-Budget Scaling No-Go

## Theorem 18.1

For geometric scales:

$$
R_n=2^{-n},
$$

the formal parabolic dangerous-core cost satisfies:

$$
\boxed{
\sum_n
R_n
<
\infty.
}
$$

Therefore the classical finite enstrophy-time budget is **scaling-compatible** with infinitely many geometrically shrinking dangerous epochs.

Consequently:

$$
\boxed{
\text{finite enstrophy-time alone}
}
$$

cannot be a scale-level contradiction to an infinite horizon cascade.

### Safety

This is a scaling compatibility theorem.

It is not a construction of a singular Navier--Stokes solution.

$\square$

---

# 19. External confirmation of the scaling issue

Quantitative partial-regularity work of Lei--Ren recalls that kinetic and dissipation energies are supercritical under Navier--Stokes scaling and therefore too weak, by themselves, to control arbitrarily fine scales.

The same work improves the Caffarelli--Kohn--Nirenberg singular-set gauge but still identifies exclusion of Type-I blow-up under bounded scale-invariant energy as a major open problem.

Thus standard finite energy/dissipation budgets do not presently give full singularity exclusion.

---

# 20. Scaling of the negative-Sobolev forcing budget

Vorticity forcing scales as:

$$
\boxed{
\mathcal G^{(\lambda)}
(x,t)
=
\lambda^4
\mathcal G(
\lambda x,
\lambda^2t
).
}
$$

For the homogeneous norm:

$$
\dot H^{-2},
$$

$$
\boxed{
\|
\mathcal G^{(\lambda)}
\|_{\dot H^{-2}}
=
\lambda^{1/2}
\|
\mathcal G
\|_{\dot H^{-2}}.
}
$$

Therefore the:

$$
L_t^{4/3}\dot H_x^{-2}
$$

action on one parabolic scale transforms as:

$$
\boxed{
\lambda^{2/3}
\lambda^{-2}
=
\lambda^{-4/3}.
}
$$

Equivalently at physical scale:

$$
R=\lambda^{-1},
$$

the canonical per-scale action is:

$$
\boxed{
O(R^{4/3}).
}
$$

---

# 21. CIV/V-3.6 — Weak-Forcing Budget Scaling No-Go

## Theorem 21.1

For geometric scales:

$$
R_n=2^{-n},
$$

$$
\boxed{
\sum_n
R_n^{4/3}
<
\infty.
}
$$

Thus the universal finite:

$$
L_t^{4/3}\dot H_x^{-2}
$$

vorticity-forcing budget is also scaling-compatible with infinitely many geometrically shrinking source-renewal epochs.

Therefore it cannot, by scaling alone, provide a Finite Forest Obstruction.

$\square$

---

# 22. The scaling mismatch

The two strongest genuinely universal budgets identified in CFOP are:

### state budget

$$
\boxed{
\int
\|\omega\|_2^2dt
<
\infty;
}
$$

### weak nonlinear-source budget

$$
\boxed{
\int
\|\mathcal G\|_{H^{-2}}^{4/3}dt
<
\infty.
}
$$

Their per-parabolic-scale costs are:

$$
\boxed{
R
}
$$

and:

$$
\boxed{
R^{4/3}.
}
$$

Both are summable on geometric scales.

This is the main budget obstruction gap.

---

# 23. Critical/coercive quantities

In contrast, known regularity/blow-up criteria often involve scale-critical quantities.

Examples in the current RFP/CSP/DRC architecture include:

- middle-strain critical action;
- critical moving-frequency action;
- low-mode driver action;
- related scale-critical vorticity/strain criteria.

At a hypothetical singularity these quantities may be required to diverge.

Therefore they are not known universal **finite** budgets.

---

# 24. The missing estimate

A complete Finite Forest Obstruction would require a quantity:

$$
\boxed{
\mathfrak B_{\rm forest}^{crit}
}
$$

with all three properties:

### FCB-1 — universal finiteness

$$
\boxed{
\mathfrak B_{\rm forest}^{crit}
\le
C(u_0,\nu)
}
$$

for every relevant Navier--Stokes solution.

### FCB-2 — near-critical scale cost

Every dangerous forest cut pays a scale cost that is non-summable across a horizon cascade, ideally:

$$
\boxed{
\gtrsim1
}
$$

per geometric generation, or an equivalent non-summable gauge.

### FCB-3 — branching stability

The lower cost survives:

- path switching;
- source atomization;
- spatial fragmentation;
- scale fragmentation.

No known quantity in the present program satisfies all three.

---

# 25. Forest Coercive Budget Problem

Define:

$$
\boxed{
\textbf{FCBP — Forest Coercive Budget Problem}.
}
$$

> Construct, or prove impossible, a universally finite Navier--Stokes forest functional with near-critical scaling that lower-bounds every horizon dangerous causal cut independently of atomic lineage selection.

This is the exact missing theorem after Cycle V.

---

# 26. Congestion cannot be bounded by energy alone

The negative-Sobolev forcing budget converts source demand into:

$$
H^2
$$

dual congestion.

Fine-scale terminal observables naturally require increasingly high dual regularity.

The finite kinetic/enstrophy energy budget contains no universal upper control on such:

$$
H^2
$$

dual witness congestion.

Thus:

$$
\boxed{
R_{F\mbox{-}HCONG}
}
$$

survives the current energy-class audit.

---

# 27. Capacity cannot be bounded by energy alone

The geometric capacity:

$$
\operatorname{Cap}_{ss}
\sim
W(1+\Xi)^3
$$

is not bounded by:

$$
\|u\|_2
$$

or:

$$
\int
\|\nabla u\|_2^2dt.
$$

Finite energy controls total state mass, not the number of wavelength cells over which small pieces may be spread.

Thus:

$$
\boxed{
R_{F\mbox{-}CAP}
}
$$

also survives unless accompanied by stronger atom floors or a geometric regularizing condition.

---

# 28. Partial regularity is not a forest-capacity bound

Caffarelli--Kohn--Nirenberg-type theory controls the **singular set**, not every pre-singularity dangerous footprint in the causal forest.

Lei--Ren improve the parabolic Hausdorff gauge of the singular set to a logarithmically stronger gauge.

This is a genuine geometric restriction.

It does not provide a uniform finite upper bound for all pre-singularity forest capacity coordinates:

$$
W,
\quad
\Xi,
\quad
\mathfrak N_{ss}^{dual}.
$$

Thus partial regularity is not, by itself, the missing Forest Finite Obstruction.

---

# 29. Sparse geometry audit

Grujić's geometric regularity theorem provides an external guard under local one-dimensional sparseness of intense super-level sets.

Recent logarithmic-depletion work gives a specialized mechanism forcing such sparseness below the analyticity scale in a critical-point scenario.

Therefore:

$$
\boxed{
G_{\rm SPARSE}
}
$$

is a genuine regularizing route.

But its negation:

$$
\boxed{
G_{\rm SPARSE}^{fail}
}
$$

is not known to violate a universal finite budget.

A dense/non-sparse intense region remains dynamically admissible at the level of present theory.

---

# 30. Non-sparse branch

Define:

$$
\boxed{
R_{F\mbox{-}DENSE}
}
$$

as the branch in which:

1. spatial capacity grows or remains large;
2. no strong compact carrier persists;
3. the hypotheses of known sparseness regularity criteria fail;
4. no universal capacity upper bound is available.

Then:

$$
\boxed{
R_{F\mbox{-}NSPARSE}
}
$$

is renamed:

$$
\boxed{
R_{F\mbox{-}DENSE}.
}
$$

The label emphasizes that failure of a sparseness theorem is not itself a defect.

---

# 31. Final primitive residual

The Cycle-V forest residual is therefore compressed to:

$$
\boxed{
\mathfrak R_{\rm Forest}^{final}
=
R_{F\mbox{-}HCONG}
\vee
R_{F\mbox{-}CAP}
\vee
R_{F\mbox{-}DENSE}.
}
$$

All three are scale/profile organization mechanisms rather than missing local source ancestry.

---

# 32. Standard-budget completeness theorem

## Theorem 32.1

Using only:

1. Leray kinetic/enstrophy energy budgets;
2. the energy-class:
   $$
   L_t^{4/3}H_x^{-1}
   $$
   velocity-nonlinearity budget;
3. the induced:
   $$
   L_t^{4/3}H_x^{-2}
   $$
   vorticity-forcing budget;
4. current CKN/quantitative partial-regularity geometry;
5. current conditional sparseness regularity guards;

one cannot close all branches of:

$$
\boxed{
\mathfrak R_{\rm Forest}^{final}.
}
$$

### Meaning

The current standard a priori estimates provide a complete **budget audit**, not a complete Forest Finite Obstruction.

$\square$

---

# 33. Why this is not merely a failure to search harder

The obstruction is structural.

The universally finite budgets inherited from the energy class are supercritical/subcritical with respect to fine-scale singular formation.

Their costs on geometrically shrinking parabolic epochs are summable.

The known scale-critical quantities are powerful enough to detect singularity, but are not known to remain universally finite.

Thus the missing estimate lies exactly between:

$$
\boxed{
\text{finite but scale-weak}
}
$$

and:

$$
\boxed{
\text{scale-critical but blow-up-divergent}.
}
$$

---

# 34. Conditional Forest Finite Obstruction theorem

## Theorem 34.1

Suppose there exists a forest functional:

$$
\mathfrak B
$$

satisfying FCB-1--FCB-3.

Then no horizon-unbounded dangerous causal forest can exist.

Consequently:

$$
\boxed{
\operatorname{Blowup}(T_\ast)
}
$$

would contradict:

$$
CN_{\rm Forest}.
$$

Therefore global regularity would follow within the established ANP/CFOP implication chain.

### Safety

No such:

$$
\mathfrak B
$$

has been constructed.

This theorem is only the formal closure criterion.

$\square$

---

# 35. Relation to Miller-type critical criteria

Miller's scale-critical strain criteria demonstrate that critical geometric/dynamical quantities can characterize or constrain finite-time blow-up.

They also illustrate the obstruction:

the relevant critical actions are not a priori finite under a hypothetical blow-up.

Thus they are excellent candidate coordinates for:

$$
\mathfrak B_{\rm forest}^{crit},
$$

but they are not already the required universal finite budget.

---

# 36. Relation to forced quantitative theory

Recent Barker--Popkin work shows that forcing generated by localization must be treated quantitatively; the forcing is amplified in Carleman estimates at large scales and low forcing regularity requires additional estimates.

This reinforces the CFOP conclusion that choosing a weaker, universally finite forcing topology does not erase forcing difficulty.

It moves the burden into stronger dual observability/congestion.

---

# 37. Relation to quantitative partial regularity

Lei--Ren use the finite dissipation energy through a non-overlapping-shell/pigeonhole argument to obtain a logarithmic improvement of partial regularity.

This is directly analogous to a cutset-budget philosophy:

finite total dissipation guarantees some favorable scales.

But the result remains partial regularity, not full exclusion of Type-I or general singular formation.

Thus finite-budget pigeonhole principles are powerful but do not presently yield a universal horizon forest obstruction.

---

# 38. Cycle-V closure theorem

## Theorem 38.1

Cycle V establishes:

1. actual forest cut capacity;
2. action--congestion duality;
3. source multiplicity and entropy debt;
4. space--scale capacity bounds;
5. propagated-state finite enstrophy occupation;
6. a universal energy-class negative-Sobolev nonlinear forcing budget;
7. reclassification of forcing-action and state-tail residuals;
8. conditional sparse-geometric regularization;
9. the exact missing Forest Coercive Budget Problem.

It does **not** establish:

$$
\boxed{
\text{Finite Forest Obstruction}.
}
$$

$\square$

---

# 39. Final status

$$
\boxed{
\begin{aligned}
CN_{\rm Forest}
&:\ \mathrm{PROVED\ RELATIVE\ TO\ ANP},\\
\text{Causal Cut Capacity}
&:\ \mathrm{PROVED},\\
\text{Finite Enstrophy Occupation}
&:\ \mathrm{PROVED},\\
\text{Universal }L_t^{4/3}H^{-2}\text{ vorticity-source budget}
&:\ \mathrm{PROVED},\\
R_{F\mbox{-}ACT}\text{ primitive status}
&:\ \mathrm{REMOVED},\\
R_{F\mbox{-}TAIL}\text{ primitive status}
&:\ \mathrm{REMOVED},\\
G_{\rm SPARSE}
&:\ \mathrm{EXTERNAL/CONDITIONAL},\\
R_{F\mbox{-}HCONG}
&:\ \mathrm{OPEN},\\
R_{F\mbox{-}CAP}
&:\ \mathrm{OPEN},\\
R_{F\mbox{-}DENSE}
&:\ \mathrm{OPEN},\\
\text{Forest Coercive Budget Problem}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 40. Next program

The next research program should not invent another forest taxonomy.

Define:

$$
\boxed{
\textbf{
NS-FCBP —
Navier--Stokes Forest Coercive Budget Program
}
}
$$

The first paper should be:

$$
\boxed{
\textbf{
NS-FCBP 01 —
Critical Forest Coercivity,
Dual Congestion Renormalization,
Scale-Invariant Cut Budgets
and Structural Cancellation
}.
}
$$

Primary tasks:

1. search for a forest cut functional with near-critical scaling;
2. exploit exact incompressibility/pressure/strain-vorticity cancellation rather than generic energy estimates;
3. renormalize:
   $$
   H^2
   $$
   dual congestion by terminal scale and dangerous amplitude;
4. test whether the renormalized congestion is controlled by a finite energy/local-energy quantity;
5. combine geometric depletion and dissipation-range structure;
6. prove a no-go if no energy-class critical finite budget can exist.

---

# 41. Conclusion

Cycle V answers the finite-budget question.

The Navier--Stokes energy class does contain more nonlinear control than the strong source ledger initially displayed:

$$
\boxed{
\mathcal N
\in
L_t^{4/3}H_x^{-1},
\qquad
\mathcal G
\in
L_t^{4/3}H_x^{-2}.
}
$$

Thus fresh source action has a genuine universal finite weak-topology budget.

But this does not close the forest.

It transfers the cost to increasingly singular dual congestion.

Likewise the finite enstrophy-time budget constrains propagated-state occupation but has only:

$$
O(R)
$$

cost per parabolic scale and is compatible with infinitely many geometric scales.

The weak forcing budget has:

$$
O(R^{4/3})
$$

cost per parabolic scale and is also summable.

Partial regularity and geometric sparseness supply powerful conditional geometric guards but do not bound every pre-singularity forest.

Therefore the current obstruction gap is not missing bookkeeping.

It is missing coercivity.

One needs a quantity that is simultaneously:

$$
\boxed{
\text{universally finite}
}
$$

and:

$$
\boxed{
\text{near-critical/non-summable on every dangerous forest cut}.
}
$$

No such forest functional is currently proved.

That is the next problem.

---

# References

1. Z. Lei, X. Ren, *Quantitative partial regularity of the Navier--Stokes equations and applications*, arXiv:2210.01783.
2. Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier--Stokes equations*, arXiv:1111.0217.
3. Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier--Stokes Equations*, arXiv:2607.08866.
4. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier--Stokes equations and applications*, arXiv:2602.09951.
5. E. Miller, *A regularity criterion for the Navier--Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
6. `NS_CFOP_01_DiffuseHorizon_ForestCutsets_v0.1.md`.
7. `NS_CFOP_02_SpatialScale_ForestCapacity_v0.1.md`.
8. `NS_ANP_09_ScaleFragmentation_InverseLimits_CN3FinalAudit_v0.1.md`.