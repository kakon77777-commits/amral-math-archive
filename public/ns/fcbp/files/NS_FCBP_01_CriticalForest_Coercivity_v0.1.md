---
title: "Navier–Stokes Forest Coercive Budget Program 01：Critical Forest Coercivity、One-Derivative Gap、Dual Congestion Renormalization 與 Structural Cancellation"
short_title: "NS-FCBP 01"
series: "Navier–Stokes Forest Coercive Budget Program"
cycle: "VI"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Critical-lift audit / structural cancellation program"
epistemic_status: "Proves a scaling theorem for velocity and vorticity nonlinear forcing in Sobolev dual spaces and identifies an exact one-spatial-derivative gap between the universal energy-class forcing bounds and the scale-critical forcing topology at the same time exponent p=4/3. Introduces scale-renormalized weak-source and dual-congestion packets whose product is critical, and proves that global finite weak forcing produces only a geometrically weighted summability statement, insufficient to exclude order-one critical packets at infinitely many geometric scales. Proves a general weighted-to-unweighted critical-lift no-go for every summable positive scale weight. Integrates three external Navier-Stokes-specific cancellation modules: Miller's strain-vorticity orthogonality, recent finite-scale filtered vortex-stretching absorption by diffusion, and recent pressure-flux weighted finite-chain telescoping. These cancellations show genuine structural derivative/coercivity recovery but leave explicit model-cone, far-field/commutator/localization, backscatter, observability, and weighted-packing gaps. The paper defines the Critical Lift Problem: convert a universally finite scale-weighted cancellation ledger into a non-summable near-critical forest cut budget without assuming regularity. No such lift is proved; Finite Forest Obstruction and Navier-Stokes regularity remain OPEN."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Forest Coercive Budget Program 01

# Critical Forest Coercivity、One-Derivative Gap、Dual Congestion Renormalization 與 Structural Cancellation

## 0. Program objective

CFOP Cycle V ended with the Forest Coercive Budget Problem:

> find a forest functional which is simultaneously universally finite, near-critical on dangerous cuts, and stable under branching/fragmentation.

The final CFOP residual was:

$$
\boxed{
R_{F\mbox{-}HCONG}
\vee
R_{F\mbox{-}CAP}
\vee
R_{F\mbox{-}DENSE}.
}
$$

FCBP does not add another forest taxonomy.

It asks whether exact Navier--Stokes structure can **lift** the known finite scale-weak budgets into a critical or non-summable coercive budget.

---

# 1. Navier--Stokes scaling

Use:

$$
\boxed{
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t).
}
$$

Then:

$$
\omega_\lambda
=
\lambda^2
\omega(\lambda x,\lambda^2t).
$$

Let the velocity nonlinearity be:

$$
\boxed{
\mathcal N
=
-
\mathbb P
\nabla\cdot
(u\otimes u).
}
$$

Then:

$$
\boxed{
\mathcal N_\lambda
=
\lambda^3
\mathcal N(\lambda x,\lambda^2t).
}
$$

Let the vorticity forcing be:

$$
\boxed{
\mathcal G
=
-\nabla\times\mathcal N.
}
$$

Then:

$$
\boxed{
\mathcal G_\lambda
=
\lambda^4
\mathcal G(\lambda x,\lambda^2t).
}
$$

---

# 2. Homogeneous Sobolev scaling

If:

$$
f_\lambda(x)
=
\lambda^\alpha
f(\lambda x),
$$

then in three dimensions:

$$
\boxed{
\|f_\lambda\|_{\dot H^r}
=
\lambda^{
\alpha+r-\frac32
}
\|f\|_{\dot H^r}.
}
$$

Therefore:

$$
\boxed{
\|\mathcal N_\lambda\|_{\dot H^{-s}}
=
\lambda^{
\frac32-s
}
\|\mathcal N\|_{\dot H^{-s}},
}
$$

and:

$$
\boxed{
\|\mathcal G_\lambda\|_{\dot H^{-s}}
=
\lambda^{
\frac52-s
}
\|\mathcal G\|_{\dot H^{-s}}.
}
$$

---

# 3. CIV/VI-1.1 — Critical forcing scaling theorem

## Theorem 3.1

The norm:

$$
\|\mathcal N\|_{L_t^p\dot H_x^{-s}}
$$

is Navier--Stokes scale invariant exactly when:

$$
\boxed{
\frac2p
=
\frac32-s.
}
$$

The norm:

$$
\|\mathcal G\|_{L_t^p\dot H_x^{-s}}
$$

is scale invariant exactly when:

$$
\boxed{
\frac2p
=
\frac52-s.
}
$$

### Proof

Include the:

$$
dt
\mapsto
\lambda^{-2}dt
$$

time scaling in the Sobolev norm formulas.

$\square$

---

# 4. Energy-class forcing line

Cycle V proved from the Leray energy class:

$$
\boxed{
\mathcal N
\in
L_t^{4/3}H_x^{-1},
}
$$

and:

$$
\boxed{
\mathcal G
\in
L_t^{4/3}H_x^{-2}.
}
$$

Set:

$$
p=\frac43.
$$

Then:

$$
\frac2p
=
\frac32.
$$

For velocity forcing, scale criticality requires:

$$
\boxed{
s=0.
}
$$

For vorticity forcing, scale criticality requires:

$$
\boxed{
s=1.
}
$$

---

# 5. CIV/VI-1.2 — One-Derivative Gap Theorem

## Theorem 5.1

At the energy-class time exponent:

$$
p=\frac43,
$$

the known universal finite forcing spaces lie exactly one spatial derivative below the scale-critical spaces:

$$
\boxed{
L_t^{4/3}H_x^{-1}
\quad
\text{versus}
\quad
L_t^{4/3}L_x^2
}
$$

for:

$$
\mathcal N,
$$

and:

$$
\boxed{
L_t^{4/3}H_x^{-2}
\quad
\text{versus}
\quad
L_t^{4/3}H_x^{-1}
}
$$

for:

$$
\mathcal G.
$$

Thus the generic energy/Sobolev-duality route has an exact one-derivative scaling deficit.

$\square$

---

# 6. Meaning of the gap

The missing Forest Coercive Budget is not obtained by improving a constant in:

$$
L_t^{4/3}H^{-2}.
$$

At fixed time exponent, one full derivative must be recovered.

Therefore any successful FCBP theorem must use:

- structural cancellation;
- geometric depletion;
- pressure/flux telescoping;
- compensated compactness;
- or another Navier--Stokes-specific mechanism.

Generic Sobolev duality alone cannot remove this scaling gap.

---

# 7. Terminal dangerous scale model

Consider a Type-I/parabolic dangerous scale:

$$
R,
$$

with output shell:

$$
2^k
\asymp
R^{-1}.
$$

The absolute local UV certificate gives the canonical terminal vorticity amplitude:

$$
\boxed{
A_R
\asymp
R^{-1/2}
}
$$

at the scaling level.

Let:

$$
\Phi_R
$$

be the terminal:

$$
L^2
$$

norming witness with:

$$
\|\Phi_R\|_2
\lesssim1.
$$

The source-normalized witness is:

$$
\boxed{
\Psi_R
=
\Phi_R/A_R.
}
$$

Thus:

$$
\boxed{
\|\Psi_R\|_2
\sim
R^{1/2}.
}
$$

---

# 8. Canonical shell dual scaling

For a shell-localized endpoint witness:

$$
\boxed{
\|\Psi_R\|_{\dot H^s}
\sim
R^{\frac12-s}.
}
$$

On a parabolic epoch:

$$
|I_R|
\sim
R^2,
$$

the formal quartic dual congestion scales as:

$$
\boxed{
\int_{I_R}
\|\Psi_R\|_{\dot H^s}^{4}dt
\sim
R^{
4-4s
}.
}
$$

Thus:

### critical dual level

For:

$$
s=1,
$$

$$
\boxed{
\int_{I_R}
\|\Psi_R\|_{\dot H^1}^{4}dt
\sim
1.
}
$$

### energy-dual level

For:

$$
s=2,
$$

$$
\boxed{
\int_{I_R}
\|\Psi_R\|_{\dot H^2}^{4}dt
\sim
R^{-4}.
}
$$

### Safety

This is the canonical scaling ledger for a shell-localized dangerous packet.

It is not a theorem that the exact drifted adjoint witness remains band-limited throughout the interval.

---

# 9. Renormalized weak-source packet

For a scale:

$$
R,
$$

define:

$$
\boxed{
\widehat{\mathfrak B}_{-2}(I_R)
=
R^{-4/3}
\int_{I_R}
\|\mathcal G(t)\|_{H^{-2}}^{4/3}dt.
}
$$

This quantity is scale normalized.

Define the renormalized dual congestion:

$$
\boxed{
\widehat{\mathfrak K}_{2}(I_R)
=
R^{4}
\int_{I_R}
\mathfrak C_2(t)^4dt.
}
$$

---

# 10. CIV/VI-1.3 — Critical Renormalized Duality

## Theorem 10.1

The CFOP weak-source/strong-dual inequality:

$$
\mathfrak B_{-2}(I_R)^3
\mathfrak K_2(I_R)
\ge
\sigma^4
$$

is equivalently:

$$
\boxed{
\widehat{\mathfrak B}_{-2}(I_R)^3
\widehat{\mathfrak K}_{2}(I_R)
\ge
\sigma^4.
}
$$

All explicit powers of:

$$
R
$$

cancel.

### Meaning

The cut inequality itself can be written in a scale-critical normalized form.

The obstruction is not local scaling covariance.

It is global summability.

$\square$

---

# 11. Global finite budget after renormalization

For disjoint scale-adapted intervals:

$$
I_n,
$$

with physical scales:

$$
R_n,
$$

the universal weak forcing budget gives:

$$
\boxed{
\sum_n
R_n^{4/3}
\widehat{\mathfrak B}_{-2}(I_n)
\le
C(u_0,\nu).
}
$$

This is a **weighted** critical packet bound.

It is not:

$$
\boxed{
\sum_n
\widehat{\mathfrak B}_{-2}(I_n)
<
\infty.
}
$$

---

# 12. Geometric horizon scales

Let:

$$
\boxed{
R_n
=
R_0\theta^n,
\qquad
0<\theta<1.
}
$$

Then for every:

$$
\alpha>0,
$$

$$
\boxed{
\sum_{n=0}^{\infty}
R_n^\alpha
<
\infty.
}
$$

---

# 13. CIV/VI-1.4 — Summable-Weight Critical-Lift No-Go

## Theorem 13.1

Let:

$$
c_n\ge0
$$

be a scale-invariant dangerous-cut cost.

Suppose the only global estimate is:

$$
\boxed{
\sum_n
w_n c_n
\le
C
}
$$

with:

$$
\boxed{
\sum_nw_n<\infty.
}
$$

Then this estimate cannot exclude:

$$
\boxed{
c_n\ge c_0>0
\quad
\forall n.
}
$$

### Proof

Set:

$$
c_n=c_0.
$$

Then:

$$
\sum_nw_nc_n
=
c_0
\sum_nw_n
<
\infty.
$$

$\square$

---

# 14. Critical weight threshold

Therefore a forest obstruction based on a per-generation lower bound:

$$
c_n\ge c_0
$$

requires a global weight sequence:

$$
w_n
$$

that is not summable.

The ideal case is:

$$
\boxed{
w_n\asymp1.
}
$$

Borderline non-summable logarithmic weights may also suffice.

This is the **critical lift** required by FCBP.

---

# 15. Application to known universal budgets

### enstrophy-time

The effective scale weight is:

$$
\boxed{
w_n\sim R_n.
}
$$

Summable.

### energy-class weak vorticity forcing

The effective scale weight is:

$$
\boxed{
w_n\sim R_n^{4/3}.
}
$$

Summable.

Thus both fail Theorem 13.1's non-summable requirement.

---

# 16. Pure Sobolev-duality no-go

The one-derivative gap and Summable-Weight No-Go imply:

$$
\boxed{
\textbf{
energy-class Sobolev duality alone cannot produce the required critical forest obstruction.
}
}
$$

This is a methodological no-go.

It does not exclude a Navier--Stokes-specific compensated/cancelled critical budget.

---

# 17. Structural Cancellation Module I — strain/vorticity orthogonality

A Navier--Stokes-specific identity proved by Miller is:

$$
\boxed{
\left\langle
-\Delta S,
\omega\otimes\omega
\right\rangle
=
0.
}
$$

This is an exact high-derivative cancellation.

Write:

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

Then the strain equation gives the:

$$
\dot H^1
$$

balance:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-
\langle
\mathcal R_{SV},
-\Delta S
\rangle.
}
$$

---

# 18. Model-cone coercivity

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

If:

$$
\boxed{
\chi_{SV}
\le
1-\delta,
}
$$

then:

$$
\boxed{
\frac d{dt}
\|S\|_{\dot H^1}^2
\le
-2\delta
\|-\Delta S\|_2^2.
}
$$

Thus a dangerous strain-growth interval must leave every uniformly subcritical model cone.

### Status

The orthogonality and corresponding regularity/model criteria are EXTERNAL results from Miller.

The displayed coercive estimate is the direct Cauchy--Schwarz consequence used previously in CSP/DRC.

---

# 19. What the orthogonality achieves

The term:

$$
\omega\otimes\omega
$$

looks like a high-order source in the strain dynamics.

Yet its direct pairing with:

$$
-\Delta S
$$

vanishes exactly.

This demonstrates:

$$
\boxed{
\text{structural cancellation can remove a high-derivative source direction}.
}
$$

It is direct evidence that FCBP must search for equation-specific cancellations rather than generic norm estimates.

---

# 20. What the orthogonality does not achieve

The residual:

$$
\mathcal R_{SV}
$$

contains:

- advection;
- strain self-amplification;
- the compensating vorticity contribution.

No universal finite near-critical budget for:

$$
\chi_{SV}
$$

or:

$$
\langle
\mathcal R_{SV},
-\Delta S
\rangle
$$

is known.

Thus the cancellation creates a **coercive cone**, not the final finite forest budget.

---

# 21. Structural Cancellation Module II — filtered vortex stretching

Recent finite-scale work on spatially filtered Navier--Stokes vorticity proves a scale-normalized coercive estimate for the positive singular near-field stretching.

At physical scale:

$$
r,
$$

and filter scale:

$$
\ell,
$$

the structure is:

$$
\boxed{
\mathcal V_{r,\ell}^{+,near}
\lesssim
\mathcal A_{r,\ell}^{pair}
\le
\eta
\mathcal P_{r,\ell}^{\rho}
+
C_\eta
M_{r,\rho}(u)
\left(
\frac r\ell
\right)^5
\mathcal O_{r,\ell}.
}
$$

Here:

- $\mathcal A^{pair}$ is a pairwise filtered-vorticity direction defect;
- $\mathcal P^\rho$ is localized filtered diffusion;
- $\mathcal O$ is a lower-order filtered enstrophy reservoir.

---

# 22. Fixed relative filter

Set:

$$
\boxed{
\ell=\sigma r,
\qquad
0<\sigma<1.
}
$$

Then:

$$
\left(
\frac r\ell
\right)^5
=
\sigma^{-5},
$$

independent of the physical scale:

$$
r.
$$

Thus the positive near-field singular stretching is absorbed by diffusion up to a lower-order reservoir with a scale-uniform coefficient.

### Status

This is an EXTERNAL finite-scale coercive module.

---

# 23. Filtered residuals

After near-field absorption, the filtered localized enstrophy ledger retains explicit residual classes including:

- far-field strain;
- commutator forcing;
- localization terms.

The far-field analysis can be reduced to weighted packing/Carleson-type estimates under additional sequence hypotheses.

The same work explicitly notes that shell reassignment alone does not imply full unweighted packing.

This is directly aligned with the FCBP Critical Lift Problem.

---

# 24. Structural Cancellation Module III — pressure/flux work

Recent coarse-grained suitable-weak-solution work defines the resolved interscale flux:

$$
\Pi^\ell
=
-
R^\ell:\nabla U^\ell
$$

and the combined pressure--flux work distribution:

$$
\boxed{
G^\ell
=
\Pi^\ell
+
\nabla\cdot
(
P^\ell U^\ell
).
}
$$

The combination is the signed work density appearing in the localized resolved-energy balance.

---

# 25. Weighted finite-chain telescoping

For a finite chain of physical scales:

$$
r_k,
$$

the work-depletion framework provides weights:

$$
\boxed{
w_k
=
r_k/r_0,
}
$$

and a weighted telescoping estimate of the form:

$$
\boxed{
\sum_k
w_k
(
W_k^+
+
D_k
)
\le
E_0^-
+
\sum_k
w_k
|L_k|
+
\sum_k
w_k
W_k^-.
}
$$

The right-hand side contains:

- initial localized kinetic energy;
- explicit localization leakage;
- negative combined work/backscatter.

### Status

EXTERNAL finite-chain structural cancellation.

---

# 26. Why weighted telescoping is not yet the critical lift

For geometric scales:

$$
r_k
\sim
\theta^k,
$$

the weights:

$$
w_k
\sim
r_k
$$

are summable.

Therefore Theorem 13.1 applies:

$$
\boxed{
\text{a scale-weighted finite-chain estimate does not by itself exclude order-one normalized work at every geometric scale}.
}
$$

The pressure--flux work framework also explicitly retains an observability/detector bridge and backscatter/leakage alternatives.

Thus it supplies a strong structural module but not yet an unweighted forest obstruction.

---

# 27. Three structural lessons

The three modules show three distinct kinds of Navier--Stokes coercivity.

### SC-1 — exact orthogonality

A dangerous-looking high-derivative term can vanish in the correct pairing.

### SC-2 — geometric absorption

Positive singular stretching can be converted into a direction defect and absorbed by diffusion.

### SC-3 — signed telescoping

Pressure and interscale flux can combine so forward work/dissipation telescope against initial energy, leakage, and backscatter.

These are precisely the kinds of mechanisms generic Sobolev estimates miss.

---

# 28. Common remaining gap

Despite their different forms, all three modules leave one common problem:

$$
\boxed{
\textbf{critical lift}.
}
$$

One must convert:

- residual alignment;
- weighted packing;
- localization/backscatter;
- finite-chain telescoping;

into a horizon-cofinal forest budget with a non-summable per-scale weight.

---

# 29. Critical Lift Problem

Define:

$$
\boxed{
\textbf{CLP — Critical Lift Problem}.
}
$$

Given a structural Navier--Stokes ledger:

$$
\boxed{
\sum_n
w_n
\mathcal C_n
\le
B_{\rm init}
+
B_{\rm rem},
}
$$

where:

$$
\mathcal C_n
$$

is a scale-invariant dangerous-cut cost, construct conditions under which:

$$
\boxed{
\sum_n
\widetilde w_n
\mathcal C_n
\le
\widetilde B
}
$$

with:

$$
\boxed{
\sum_n
\widetilde w_n
=
\infty.
}
$$

The strongest target is:

$$
\widetilde w_n\asymp1.
$$

---

# 30. Allowed sources of lift

A valid critical lift may come from:

1. cancellation between neighboring scales;
2. signed forward/backscatter compensation;
3. Carleson packing with a non-summable measure;
4. affine/harmonic far-field cancellation;
5. geometric depletion;
6. conservation/orthogonality of active modes;
7. a branch-congestion lower bound tied to finite energy;
8. a logarithmic gain strong enough to cross the summability threshold.

---

# 31. Forbidden pseudo-lifts

The following do not solve CLP:

### normalization only

Multiplying each cut by a scale factor and calling it critical without obtaining a corresponding global bound.

### profile quotienting

Compactifying scale/space while losing actual branch/cut identity.

### absolute-value inflation

Replacing signed work by gross work unless the new gross term has a finite critical budget.

### hidden regularity assumption

Assuming the critical norm is finite when that is already a regularity criterion.

---

# 32. CIV/VI-1.5 — Weighted-to-Critical Lift Criterion

## Theorem 32.1

Suppose dangerous cuts:

$$
\mathcal C_n
\ge
c_0>0
$$

occur at infinitely many scales.

If one proves:

$$
\boxed{
\sum_n
\widetilde w_n
\mathcal C_n
<
\infty
}
$$

with:

$$
\boxed{
\sum_n
\widetilde w_n
=
\infty
}
$$

and a uniform lower comparison:

$$
\widetilde w_n
\ge0,
$$

then the dangerous-cut sequence is impossible.

### Proof

Otherwise:

$$
\sum_n
\widetilde w_n
\mathcal C_n
\ge
c_0
\sum_n
\widetilde w_n
=
\infty.
$$

$\square$

---

# 33. Why logarithmic improvements matter

A weight may tend to zero and still be non-summable.

For example:

$$
\boxed{
\widetilde w_n
\sim
\frac1n
}
$$

gives:

$$
\sum_n
\widetilde w_n
=
\infty.
$$

Therefore FCBP does not require a perfect unweighted estimate.

A sufficiently strong borderline logarithmic lift can be enough.

This is consistent with the general importance of logarithmic improvements in quantitative partial regularity, though no such forest lift is presently proved.

---

# 34. Forest criticality index

For a scale weight:

$$
w(R)
\sim
R^\alpha
$$

define the forest criticality index:

$$
\boxed{
\alpha_{\rm forest}
=
\alpha.
}
$$

### super-summable / scale-weak

$$
\alpha_{\rm forest}>0.
$$

Geometric scales are summable.

### critical

$$
\boxed{
\alpha_{\rm forest}=0.
}
$$

### supercritical obstruction weight

$$
\alpha_{\rm forest}<0.
$$

Every fine scale becomes increasingly expensive.

The energy/enstrophy and weak-forcing budgets currently have:

$$
\boxed{
\alpha_{\rm forest}=1
}
$$

and:

$$
\boxed{
\alpha_{\rm forest}=4/3.
}
$$

respectively.

---

# 35. Structural cancellation score

For a proposed FCBP module record:

$$
\boxed{
\mathfrak S_{\rm cancel}
=
(
d_{\rm rec},
\alpha_{\rm lift},
R_{\rm rem},
B_{\rm univ}
).
}
$$

Where:

### $d_{\rm rec}$

number of recovered derivatives;

### $\alpha_{\rm lift}$

resulting forest scale exponent;

### $R_{\rm rem}$

explicit residual classes;

### $B_{\rm univ}$

whether the resulting budget is universally finite.

A successful final forest coercive module must satisfy:

$$
\boxed{
d_{\rm rec}\ge1
}
$$

or an equivalent compensated gain,

and:

$$
\boxed{
\alpha_{\rm lift}\le0
}
$$

or at least a non-summable borderline weight.

---

# 36. Module audit

### Miller orthogonality

$$
d_{\rm rec}
:
\text{nontrivial exact directional cancellation}.
$$

But no universal finite critical residual budget.

### Filtered vortex stretching

Near-field positive stretching is scale-uniformly diffusion-absorbed at fixed relative filter.

Residual:

- far-field;
- commutator;
- localization;
- weighted packing.

### Pressure--flux telescoping

Exact signed finite-chain depletion.

Residual:

- scale weight;
- leakage;
- backscatter;
- observability.

No module yet satisfies the complete FCBP target.

---

# 37. FCBP residual after Paper 01

Avoid introducing many new taxonomy labels.

The program retains only three aggregate lift gaps:

$$
\boxed{
\textbf{CL-DER}
}
$$

— one-derivative critical forcing gap;

$$
\boxed{
\textbf{CL-REM}
}
$$

— explicit structural remainders such as far-field, commutator, localization, backscatter/model-cone residual;

$$
\boxed{
\textbf{CL-PACK}
}
$$

— weighted-to-non-summable packing/telescoping gap.

These are not new physical mechanisms.

They are theorem-construction obligations.

---

# 38. Current strongest positive statement

Navier--Stokes-specific cancellations do achieve forms of coercivity unavailable to generic functional analysis.

Therefore:

$$
\boxed{
\text{FCBP is not ruled out by the pure Sobolev scaling no-go}.
}
$$

But every presently audited structural module stops before producing:

$$
\boxed{
\text{universal finite}
+
\text{non-summable critical forest cost}.
}
$$

---

# 39. Current strongest no-go statement

Using only:

- Leray energy;
- energy interpolation;
- Sobolev duality;
- scale renormalization;

without a Navier--Stokes-specific cancellation/lift theorem, one cannot close the one-derivative forcing gap or the summable scale-weight gap.

Thus:

$$
\boxed{
\textbf{
generic energy-duality FCBP route
=
NO\mbox{-}GO.
}
}
$$

---

# 40. Next paper

The next paper should attack the most promising structural module rather than create another taxonomy:

$$
\boxed{
\textbf{
NS-FCBP 02 —
Filtered Stretching Coercivity、
Carleson Packing、
Far-Field Affine Cancellation
與 Critical Lift Attempt
}.
}
$$

Primary tasks:

1. adapt scale-uniform filtered near-field absorption to the forest cut ledger;
2. test whether far-field annular reassignment can be upgraded from weighted to non-summable Carleson control;
3. use affine/harmonic cancellation of exterior strain;
4. quantify commutator/localization residuals;
5. determine whether the scale exponent can be lifted from:
   $$
   \alpha>0
   $$
   to:
   $$
   \alpha\le0
   $$
   or a logarithmic non-summable borderline;
6. if not, prove an explicit filtered-cancellation critical-lift no-go.

---

# 41. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{forcing Sobolev scaling law}
&:\ \mathrm{PROVED},\\
\text{one-derivative energy/critical gap}
&:\ \mathrm{PROVED},\\
\text{critical renormalized weak-source/dual inequality}
&:\ \mathrm{PROVED},\\
\text{summable-weight Critical-Lift no-go}
&:\ \mathrm{PROVED},\\
\text{generic energy-duality FCBP route}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{strain--vorticity orthogonality}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{model-cone coercivity}
&:\ \mathrm{PROVED\ CONSEQUENCE},\\
\text{filtered near-field stretching absorption}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{pressure--flux weighted telescoping}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{critical lift}
&:\ \mathrm{OPEN},\\
\text{Forest Coercive Budget}
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

# 42. Conclusion

FCBP-01 identifies the exact scaling obstruction hidden inside the Cycle-V budget audit.

At the energy-class time exponent:

$$
p=\frac43,
$$

the universal vorticity forcing bound is:

$$
\boxed{
L_t^{4/3}H_x^{-2},
}
$$

while the scale-critical forcing topology is:

$$
\boxed{
L_t^{4/3}H_x^{-1}.
}
$$

The gap is one full derivative.

Renormalizing the weak forcing and high-order dual congestion makes the local cut inequality scale invariant, but the global bound still carries a summable factor:

$$
R^{4/3}.
$$

More generally, any global dangerous-cut ledger weighted by a summable geometric factor cannot rule out order-one critical cost at every generation.

Thus normalization alone does not create coercivity.

Equation-specific structure is required.

Three such structures are now visible:

- exact strain--vorticity orthogonality;
- scale-uniform filtered near-field stretching absorption;
- signed pressure--flux finite-chain telescoping.

They prove that Navier--Stokes possesses real cancellation mechanisms strong enough to remove or absorb pieces of critical nonlinear work.

But each leaves a critical-lift gap in residual alignment, far-field/commutator/localization, backscatter/observability, or weighted packing.

The next task is therefore sharply defined:

$$
\boxed{
\textbf{
turn an existing Navier--Stokes cancellation into a non-summable forest budget.
}
}
$$

That is FCBP-02.

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
2. E. Miller, *A regularity criterion for the Navier--Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
3. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
4. R. Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322.
5. Z. Lei, X. Ren, *Quantitative partial regularity of the Navier--Stokes equations and applications*, arXiv:2210.01783.
6. `NS_CFOP_03_FiniteForestObstruction_Audit_v0.1.md`.
7. `NS_CFOP_CYCLE_V_HANDOFF_v1.0.md`.
