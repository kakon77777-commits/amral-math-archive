---
title: "Navier–Stokes Forest Coercive Budget Program 02: Filtered Stretching Coercivity, Comparable-Annulus Barrier, Signed Affine-Jet Lift, Commutator Recurrence and Critical-Lift No-Go"
short_title: "NS-FCBP 02"
series: "Navier–Stokes Forest Coercive Budget Program"
cycle: "VI"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Filtered critical-lift attempt / far-field and commutator audit"
epistemic_status: "Uses the 2026 filtered-vorticity finite-scale coercive framework as an external structural module and proves several internal lift/no-go results around it. The singular positive near-field stretching is externally absorbed by filtered diffusion at fixed relative filter scale. The principal localization residual is externally cancelled by a filtered adjoint cutoff. The reassigned far-field annular term has a conditional unweighted Carleson closure under conjugate sequence-space summability, but the current annular inequality contains an unsuppressed comparable-scale diagonal channel; off-diagonal gap decay or harmonic Taylor remainder gains cannot by themselves create global unweighted summability from bounded scale-invariant reservoirs. Harmonic/affine structure alone also cannot cancel positive-part stretching; a signed formulation is necessary. An internal signed-to-positive lift lemma shows that signed telescoping plus finite negative/backscatter work would suffice to convert affine-jet work into positive-work packing. The differentiated commutator branch externally recovers the scale loss through a scale-invariant derivative-compatible increment defect, so the derivative gap is locally repaired, but no universal unweighted packing of this critical defect is available. Persistent post-near-field surplus forces persistent critical increment defect after the other residuals are removed. The current filtered inequalities therefore reduce Critical Lift to comparable-annulus signed packing, commutator recurrence/packing, exterior-tail control, and residual localization; they do not prove a universal Forest Coercive Budget or Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Forest Coercive Budget Program 02

# Filtered Stretching Coercivity, Comparable-Annulus Barrier, Signed Affine-Jet Lift, Commutator Recurrence and Critical-Lift No-Go

## 0. Context of this Paper

FCBP-01 proved that generic energy/Sobolev duality misses the critical vorticity forcing topology by one spatial derivative.

It also identified a second obstruction:

$$
\boxed{
\text{a summably weighted scale ledger cannot exclude order-one dangerous cost at every geometric scale}.
}
$$

The filtered-vorticity framework is a serious candidate because it does two things generic estimates do not:

1. absorbs the singular positive near-field stretching into diffusion;
2. replaces a scale-worse differentiated commutator estimate by a scale-invariant increment defect.

The present paper tests whether these local gains can be upgraded to an **unweighted global forest budget**.

The answer is:

$$
\boxed{
\text{not from the currently proved filtered inequalities alone}.
}
$$

The exact remaining barriers are identified below.

---

# 1. Filtered variables

Fix:

$$
0<\ell\le\rho r,
$$

and define:

$$
U_\ell
=
\varphi_\ell*u,
$$

$$
\Omega_\ell
=
\nabla\times U_\ell,
$$

and the filtered strain:

$$
\mathbb S_\ell
=
\frac12
(
\nabla U_\ell+\nabla U_\ell^T
).
$$

The filtered vorticity equation contains:

- filtered stretching;
- filtered diffusion;
- differentiated commutator/subgrid forcing.

Use the scale-normalized filtered enstrophy:

$$
\boxed{
\mathcal O_{r,\ell}
=
r^{-1}
\iint_{Q_r}
\chi
|\Omega_\ell|^2,
}
$$

and diffusion:

$$
\boxed{
\mathcal P_{r,\ell}^{\rho}
=
r
\int_{I_r}
\int_{B_{(1+\rho)r}}
|\nabla\Omega_\ell|^2.
}
$$

---

# 2. External near-field coercive module

At fixed relative filter length:

$$
\boxed{
\ell=\sigma r,
}
$$

the 2026 filtered-vorticity theorem gives a scale-normalized estimate of the form:

$$
\boxed{
\mathcal V_{r,\ell}^{+,\mathrm{near}}
\lesssim
\mathcal A_{r,\ell}^{pair}
\le
\eta
\mathcal P_{r,\ell}^{\rho}
+
C_{\eta}
M_{r,\rho}(u)
\sigma^{-5}
\mathcal O_{r,\ell}.
}
$$

Thus the singular positive near-field stretching is absorbed by diffusion up to a lower-order filtered-enstrophy reservoir.

### Status

$$
\boxed{
\text{EXTERNAL/PROVED}.
}
$$

---

# 3. First FCBP consequence

The most singular geometric part of vortex stretching is therefore not the remaining Critical-Lift bottleneck.

At fixed filter ratio:

$$
\boxed{
\textbf{near-field CL-DER}
:
\text{CLOSED at the finite-scale coercive level}.
}
$$

The remaining positive surplus is assigned to:

- far-field strain;
- commutator forcing;
- localization residuals.

---

# 4. External adjoint localization cancellation

The filtered localized enstrophy balance has a principal cutoff/transport residual:

$$
\mathcal L_\chi.
$$

If the weight solves the backward filtered adjoint:

$$
\boxed{
\partial_t\chi
+
\Delta\chi
+
U_\ell\cdot\nabla\chi
=
0,
}
$$

then:

$$
\boxed{
\mathcal L_\chi=0.
}
$$

### Status

$$
\boxed{
\text{EXTERNAL/PROVED}.
}
$$

---

# 5. Localization safety

This does not eliminate every localized-shell cost.

The filtered chain still retains explicit nonnegative budgets generated by:

- enlarged diffusion regions;
- commutator integration by parts;
- shell transition/localization terms.

Thus:

$$
\boxed{
\text{principal localization}
:
\mathrm{CLOSED},
}
$$

while:

$$
\boxed{
\text{residual localization packing}
:
\mathrm{OPEN}.
}
$$

---

# 6. Far-field energy baseline

At dyadic scales:

$$
r_k=2^{-k},
\qquad
\ell_k=\sigma r_k,
$$

the direct energy-level far-field bound is:

$$
\boxed{
V_k^{+,\mathrm{far}}
\le
C
M_E^{3/2}
2^{3k/2}.
}
$$

Thus the unconditional energy-level chain only closes under weights:

$$
w\in\mathcal W_{3/2},
$$

where:

$$
\boxed{
\sum_k
2^{3k/2}w_k
<
\infty.
}
$$

This is strongly summable and is not a critical lift.

---

# 7. Annular reassignment

The filtered far-field is decomposed into annular source shells.

After the reassignment:

$$
j=k-m,
$$

one obtains scale-invariant annular reservoirs:

$$
\mathfrak A_{j,k},
$$

their envelope:

$$
\mathfrak A_j
=
\sup_{k\ge j}
\mathfrak A_{j,k},
$$

and core profiles:

$$
\mathcal Q_k.
$$

The exact external estimate is:

$$
\boxed{
\mu_k^{\mathrm{far,ann}}
\le
C
\sum_{j=0}^{k}
2^{-(k-j)}
\mathfrak A_j
\mathcal Q_k.
}
$$

---

# 8. External discrete Carleson compiler

If:

$$
\boxed{
\mathfrak A\in\ell^p,
\qquad
\mathcal Q\in\ell^q,
\qquad
\frac1p+\frac1q=1,
}
$$

then the external annular theorem gives:

$$
\boxed{
\sum_{k=0}^{N}
\mu_k^{\mathrm{far,ann}}
\le
C
\|\mathfrak A\|_{\ell^p}
\|\mathcal Q\|_{\ell^q}
}
$$

with a constant independent of:

$$
N.
$$

Thus a true **unweighted far-field packing theorem already exists conditionally**.

The FCBP problem is to obtain its sequence-space hypotheses from Navier--Stokes structure.

---

# 9. The diagonal channel

Define the diagonal term in the reassigned **upper-bound ledger**:

$$
\boxed{
D_k^{diag}
=
\mathfrak A_k
\mathcal Q_k.
}
$$

Its convolution coefficient is:

$$
\boxed{
2^{-(k-k)}=1.
}
$$

Therefore the current annular estimate provides no scale-separation decay on this comparable-scale channel.

---

# 10. CIV/VI-2.1 — Comparable-Annulus Barrier

## Theorem 10.1

Consider an estimate of the form:

$$
\mu_k
\le
C
\sum_{j=0}^{k}
K_{k-j}
a_jq_k,
$$

with:

$$
K_0>0
$$

and:

$$
K_m\to0
$$

for:

$$
m\to\infty.
$$

Off-diagonal decay of:

$$
K_m
$$

alone cannot imply:

$$
\sum_k\mu_k<\infty
$$

from only:

$$
\sup_ja_j<\infty,
\qquad
\sup_kq_k<\infty.
$$

### Proof

The estimate contains an undamped diagonal allowance:

$$
K_0a_kq_k.
$$

The hypotheses permit:

$$
a_k=q_k=1.
$$

Then the right-hand side is:

$$
\sum_{m=0}^{k}K_m.
$$

If:

$$
K\in\ell^1
$$

and:

$$
K_0>0,
$$

this remains order one at every:

$$
k.
$$

Therefore the estimate is logically compatible with a non-summable order-one per-scale allowance.

This does not assert that Navier--Stokes realizes equality.

It proves that off-diagonal decay alone cannot yield the desired unweighted conclusion.

$\square$

---

# 11. Application to annular reassignment

For:

$$
K_m=2^{-m},
$$

Theorem 10.1 applies directly.

Hence:

$$
\boxed{
\text{annular reassignment solves relative-scale multiplicity}
}
$$

but:

$$
\boxed{
\text{does not solve comparable-scale critical packing}.
}
$$

This is the **Comparable-Annulus Barrier**.

---

# 12. Why harmonic remainder gains do not remove the barrier

For a fixed exterior annulus at coarse scale:

$$
r_j,
$$

the corresponding exterior-source strain is smooth/harmonic in the finer core:

$$
r_k\ll r_j.
$$

After subtracting a low-order Taylor jet, the remainder gains positive powers of:

$$
r_k/r_j.
$$

This improves:

$$
j<k
$$

off-diagonal interactions.

It does not provide a small parameter when:

$$
j=k+O(1).
$$

Therefore:

$$
\boxed{
\text{harmonic separation gain}
\neq
\text{comparable-annulus packing}.
}
$$

---

# 13. Fixed-annulus harmonic route

Let:

$$
H_{j,k}(x,t)
$$

denote the strain generated by a fixed exterior annulus.

On a finer core it admits a local Taylor decomposition:

$$
\boxed{
H_{j,k}
=
J_{j,k}^{aff}
+
R_{j,k}^{harm},
}
$$

where:

$$
J_{j,k}^{aff}
$$

is the affine Taylor jet and the remainder gains powers of scale separation.

This is an EXTERNAL structural route.

The external filtered paper does not prove a complete unconditional affine-jet cancellation theorem.

---

# 14. Positive-part obstruction

The far-field quantity used in the filtered enstrophy surplus is a positive work:

$$
\boxed{
\int
\chi
(
H\Omega\cdot\Omega
)_+.
}
$$

Harmonicity or affinity of:

$$
H
$$

does not itself make this quantity cancel.

---

# 15. CIV/VI-2.2 — Positive-Part Affine-Jet No-Go

## Theorem 15.1

There exists a constant harmonic trace-free symmetric strain matrix:

$$
J
$$

and a smooth compactly supported vector field:

$$
\Omega
$$

such that:

$$
\boxed{
\int
\chi
(
J\Omega\cdot\Omega
)_+
>
0.
}
$$

### Proof

Take:

$$
J
=
\operatorname{diag}
(
2,-1,-1
).
$$

It is constant, symmetric, trace free, and harmonic componentwise.

Choose:

$$
\Omega
=
\phi e_1
$$

with nonzero smooth compactly supported:

$$
\phi.
$$

Then:

$$
J\Omega\cdot\Omega
=
2\phi^2
\ge0.
$$

Hence the positive work is strictly positive.

$\square$

### Safety

This is an algebraic no-go for a proof based only on the words "harmonic" or "affine".

It does not claim that this exact jet is produced by a specified Navier--Stokes exterior annulus.

---

# 16. Consequence

A useful affine-jet cancellation theorem must retain **signed work** before taking the positive part.

One needs:

- cross-scale cancellation;
- orientation/decorrelation;
- signed telescoping;
- or a separate backscatter/negative-work budget.

This connects the harmonic route to the pressure--flux signed-work route.

---

# 17. Signed work notation

Let:

$$
a_k\in\mathbb R
$$

be a signed affine-jet work contribution.

Write:

$$
a_k^+
=
\max\{a_k,0\},
$$

and:

$$
a_k^-
=
\max\{-a_k,0\}.
$$

Then:

$$
\boxed{
a_k^+
=
a_k
+
a_k^-.
}
$$

---

# 18. CIV/VI-2.3 — Signed-to-Positive Lift Lemma

## Theorem 18.1

Assume:

$$
\boxed{
\sup_N
\sum_{k=0}^{N}
a_k
\le
B_{\rm sign}
}
$$

and:

$$
\boxed{
\sum_{k=0}^{\infty}
a_k^-
\le
B_{\rm back}.
}
$$

Then:

$$
\boxed{
\sum_{k=0}^{\infty}
a_k^+
\le
B_{\rm sign}
+
B_{\rm back}.
}
$$

### Proof

For finite:

$$
N,
$$

$$
\sum_{k=0}^{N}
a_k^+
=
\sum_{k=0}^{N}
a_k
+
\sum_{k=0}^{N}
a_k^-.
$$

Use the two assumed bounds and pass to:

$$
N\to\infty.
$$

$\square$

---

# 19. Interpretation

To turn affine harmonic structure into an **unweighted positive-work bound**, it suffices to prove:

1. a signed telescoping bound;
2. finite negative work/backscatter.

This is exactly the algebraic pattern seen in pressure--flux work depletion.

However the filtered affine-jet work has not yet been identified with a signed quantity satisfying that pressure--flux telescope.

That identification is an open bridge theorem.

---

# 20. Conditional affine-jet critical lift

Suppose the full far-field signed work decomposes as:

$$
\boxed{
W_k^{far}
=
a_k
+
r_k
+
e_k,
}
$$

where:

- $a_k$ is the affine-jet signed work;
- $r_k$ is the harmonic higher-order remainder;
- $e_k$ is the exterior-tail contribution.

Assume:

$$
\sup_N
\sum_{k=0}^{N}a_k
\le
B_{\rm sign},
$$

$$
\sum_ka_k^-
\le
B_{\rm back},
$$

$$
\sum_k|r_k|
\le
B_{\rm rem},
$$

and:

$$
\sum_k|e_k|
\le
B_{\rm ext}.
$$

---

# 21. CIV/VI-2.4 — Conditional Signed Far-Field Lift

## Theorem 21.1

Under Section 20:

$$
\boxed{
\sum_k
(
W_k^{far}
)_+
\le
B_{\rm sign}
+
B_{\rm back}
+
B_{\rm rem}
+
B_{\rm ext}.
}
$$

### Proof

Use:

$$
(a+r+e)_+
\le
a_+
+
|r|
+
|e|,
$$

then Theorem 18.1.

$\square$

### Meaning

This gives a precise path to the missing full unweighted far-field bound.

The missing PDE theorem is now:

$$
\boxed{
\text{signed affine-jet telescope/backscatter control}.
}
$$

---

# 22. Convolution decay does not create coarse-scale summability

Suppose the harmonic remainder has an estimate:

$$
|r_{j,k}|
\le
C
2^{-\beta(k-j)}
d_jq_k,
\qquad
\beta>0.
$$

The gap kernel:

$$
2^{-\beta m}
$$

belongs to:

$$
\ell^1.
$$

This controls relative-scale convolution.

It does not turn:

$$
d\in\ell^\infty,
\qquad
q\in\ell^\infty
$$

into an:

$$
\ell^1
$$

total scale sum.

Thus:

$$
\boxed{
\text{off-diagonal harmonic decay}
\neq
\text{global critical packing}.
}
$$

The coarse-scale sequence still needs:

- summability;
- signed cancellation;
- or another structural budget.

---

# 23. Differentiated commutator

The filtered vorticity equation contains:

$$
\nabla\times\nabla\cdot R_\ell,
$$

where:

$$
R_\ell
=
S_\ell(u\otimes u)
-
U_\ell\otimes U_\ell.
$$

A crude energy estimate loses a scale factor.

The 2026 filtered theorem replaces it by a derivative-compatible increment envelope.

---

# 24. Scale-invariant increment defect

For:

$$
p\in[2,4],
$$

the external scale-invariant defect is:

$$
\boxed{
\widetilde{\mathcal S}_{r,\ell}^{(p)}
=
\frac r{\ell^2}
\iint
\chi_r
\mathfrak M_{\ell,p}^4.
}
$$

At fixed:

$$
\ell=\sigma r,
$$

this is invariant under Navier--Stokes scaling.

---

# 25. External commutator insertion

The differentiated commutator work satisfies:

$$
\boxed{
F_k^{com}
\le
\eta
P_k
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_k^{(p)}
+
L_{k,\mathrm{inc}}^{com}.
}
$$

Thus the scale-worse generic forcing loss is replaced by a genuine critical increment defect.

### FCBP interpretation

$$
\boxed{
\textbf{commutator CL-DER}
:
\text{locally recovered}.
}
$$

But this does not make the critical defect globally summable.

---

# 26. CIV/VI-2.5 — Commutator Packing Barrier

## Theorem 26.1

An estimate of the form:

$$
F_k^{com}
\le
\eta P_k
+
C
S_k
+
L_k,
$$

with:

$$
S_k
$$

scale invariant, cannot yield an unweighted finite-chain bound uniform in:

$$
N
$$

from only:

$$
\sup_kS_k<\infty
$$

and:

$$
\sup_kL_k<\infty.
$$

### Proof

The hypotheses permit:

$$
S_k=s_0>0
$$

for all:

$$
k.
$$

Then:

$$
\sum_{k=0}^{N}
S_k
=
(N+1)s_0.
$$

Therefore a scale-by-scale critical estimate is not a critical packing theorem.

$\square$

---

# 27. Persistent surplus forces critical commutator recurrence

The external filtered theory proves:

after near-field absorption and after far-field/localization/commutator-shell residuals are removed, a normalized persistent positive post-near-field surplus:

$$
\mathfrak B_n
\ge
s_0>0
$$

forces:

$$
\boxed{
\liminf_{n\to\infty}
\widetilde{\mathcal S}_n^{(3)}
\ge
c_{\eta,\varphi}
s_0
>
0.
}
$$

Thus the commutator term does not disappear.

It becomes a scale-critical recurrence object.

---

# 28. Young-profile output

If:

$$
\sup_n
\widetilde{\mathcal S}_n^{(3)}
<
\infty,
$$

the external theorem extracts a cylindrical generalized Young profile of the derivative-compatible increment fields.

This provides a compactness object for:

- oscillation;
- concentration;
- commutator microstructure.

But cylindrical compactness alone does not give a full representation of:

- the increment norm;
- commutator covariance;
- positive recurrent defect work.

Those require additional hypotheses.

---

# 29. Defect-work recurrence test

The filtered theory defines a defect-work ratio which asks:

> can nontrivial increment microstructure repeatedly convert into positive commutator work across scales?

This produces a genuine rigidity/recurrence alternative:

### harmless defect

the defect-work ratio decays;

### recurrent defect

a positive fraction of critical increment defect repeatedly produces positive commutator work.

This is a candidate FCBP critical recurrence mechanism.

It is not presently a finite universal budget.

---

# 30. External filtered surplus theorem

Define the post-near-field surplus:

$$
\mathfrak S_k\ge0.
$$

The external finite-chain theorem gives:

$$
\boxed{
\mathfrak S_k
\lesssim
V_k^{+,\mathrm{far}}
+
C
\widetilde{\mathcal S}_k^{(p)}
+
L_k
+
L_{k,\mathrm{inc}}^{com}.
}
$$

Hence if:

1.:
   $$
   \sum_k
   V_k^{+,\mathrm{far}}
   <
   \infty;
   $$
2.:
   $$
   \sum_k
   \widetilde{\mathcal S}_k^{(p)}
   <
   \infty;
   $$
3.:
   $$
   \sum_k
   (
   L_k
   +
   L_{k,\mathrm{inc}}^{com}
   )
   <
   \infty;
   $$

then:

$$
\boxed{
\sum_k
\mathfrak S_k
<
\infty,
}
$$

and:

$$
\boxed{
\mathfrak S_k\to0.
}
$$

### Status

$$
\boxed{
\text{EXTERNAL/PROVED CONDITIONAL CLOSURE}.
}
$$

---

# 31. FCBP compiler

The external theorem can be read as:

$$
\boxed{
\text{FAR-PACK}
+
\text{COM-PACK}
+
\text{LOC-PACK}
\Longrightarrow
\text{FILTERED SURPLUS DECAY}.
}
$$

Therefore a persistent dangerous filtered surplus must force failure of at least one packing module.

This is already a complete finite-scale **reduction theorem**.

---

# 32. What is unconditionally closed?

### near-field singular stretching

$$
\boxed{
\mathrm{CLOSED}
}
$$

by diffusion absorption.

### principal cutoff localization

$$
\boxed{
\mathrm{CLOSED}
}
$$

by filtered adjoint cancellation.

### differentiated commutator scale loss

$$
\boxed{
\mathrm{CLOSED\ LOCALLY}
}
$$

by conversion to a scale-invariant increment defect.

---

# 33. What remains unclosed?

### far-field critical packing

Requires:

- conjugate sequence-space Carleson control;
- or signed affine-jet cancellation/backscatter;
- plus exterior-tail control.

### commutator critical packing

Requires:

- unweighted summability;
- or a rigidity theorem forcing defect-work recurrence to decay.

### localization packing

Requires summability of:

- enlarged diffusion shells;
- commutator shell residuals;
- any remaining local-cylinder transition terms.

---

# 34. CIV/VI-2.6 — Current Filtered-Ledger Critical-Lift No-Go

## Theorem 34.1

The presently proved unconditional filtered estimates do not imply a universal unweighted bound:

$$
\boxed{
\sup_N
\sum_{k=0}^{N}
\mathfrak S_k
<
\infty.
}
$$

### Proof logic

The unconditional theory supplies:

1. near-field absorption;
2. a weighted energy-level far-field estimate;
3. annular reassignment with an undamped diagonal channel;
4. a scale-invariant but not globally summable commutator defect;
5. explicit localization residuals.

The annular ledger is compatible with bounded non-summable scale-invariant reservoir sequences.

The commutator ledger is compatible with a persistent order-one critical increment defect.

Therefore the present inequalities do not logically force unweighted surplus summability.

This is a sufficiency no-go for the current ledger, not a no-go against future Navier--Stokes structure.

$\square$

---

# 35. Critical-Lift status after FCBP-02

The obligations from FCBP-01 update as follows.

### CL-DER

$$
\boxed{
\mathrm{PARTIALLY\ CLOSED}.
}
$$

The singular near-field and differentiated commutator branches recover the derivative/scale loss structurally.

### CL-REM

$$
\boxed{
\mathrm{OPEN/PARTIAL}.
}
$$

Principal localization is closed, but:

- comparable/exterior far-field;
- annular diffusion;
- commutator shell localization;
- defect-work recurrence

remain.

### CL-PACK

$$
\boxed{
\mathrm{OPEN/DOMINANT}.
}
$$

The main barriers are:

- comparable-annulus diagonal packing;
- signed affine-jet/backscatter control;
- unweighted commutator increment packing.

---

# 36. Strongest positive result

A true unweighted filtered critical lift is already available **conditionally**:

$$
\boxed{
\text{full far-field unweighted packing}
+
\text{critical increment } \ell^1\text{ packing}
+
\text{localization } \ell^1\text{ packing}
}
$$

implies:

$$
\boxed{
\mathfrak S_k\to0.
}
$$

Thus the filtered approach has reached a complete conditional compiler.

The unresolved issue is precisely the origin of those unweighted packings.

---

# 37. Strongest no-go result

Neither:

- annular reassignment;
- harmonic off-diagonal decay;
- scale-invariant commutator control;
- nor affine harmonic structure after taking positive parts

is sufficient by itself to produce the required unweighted packing.

This is the filtered-cancellation version of the FCBP critical-lift barrier.

---

# 38. Bridge to pressure--flux signed work

The Positive-Part Affine-Jet No-Go shows that the next step should preserve signs.

The Signed-to-Positive Lift Lemma shows what would suffice:

$$
\boxed{
\text{signed telescope}
+
\text{finite backscatter}
\Longrightarrow
\text{positive-work packing}.
}
$$

The pressure--flux coarse-grained framework already possesses a signed finite-chain telescoping architecture with explicit backscatter and leakage.

The missing theorem is an identification/compatibility bridge between:

- filtered far-field affine-jet stretching work;
- signed pressure/flux work;
- or another signed Navier--Stokes work ledger.

---

# 39. Next paper

The next paper is:

$$
\boxed{
\textbf{
NS-FCBP 03 —
Signed Affine-Jet Work,
Pressure--Flux Telescoping,
Model-Cone Recurrence
and Critical Lift Closure Audit
}.
}
$$

Primary tasks:

1. construct a signed affine-jet work ledger before positive-part extraction;
2. test compatibility with pressure--flux finite-chain telescoping;
3. seek a finite backscatter budget;
4. combine Miller model-cone coercivity with recurrent signed work;
5. determine whether comparable-annulus diagonal work can telescope;
6. test whether the remaining commutator defect-work profile can be absorbed or must become a new critical recurrent object;
7. decide whether any non-summable Critical Lift is available.

---

# 40. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{filtered near-field coercivity}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{principal adjoint localization cancellation}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{annular reassignment}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{conditional unweighted Carleson closure}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{Comparable-Annulus Barrier}
&:\ \mathrm{PROVED},\\
\text{Positive-Part Affine-Jet no-go}
&:\ \mathrm{PROVED},\\
\text{Signed-to-Positive Lift}
&:\ \mathrm{PROVED},\\
\text{Conditional Signed Far-Field Lift}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{derivative-compatible commutator insertion}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{Commutator Packing Barrier}
&:\ \mathrm{PROVED},\\
\text{persistent surplus}\Rightarrow\text{critical increment recurrence}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{conditional full filtered surplus closure}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{current filtered-ledger unconditional critical lift}
&:\ \mathrm{NO\mbox{-}GO},\\
CL\mbox{-}DER
&:\ \mathrm{PARTIALLY\ CLOSED},\\
CL\mbox{-}REM
&:\ \mathrm{OPEN/PARTIAL},\\
CL\mbox{-}PACK
&:\ \mathrm{OPEN/DOMINANT},\\
\text{Forest Coercive Budget}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 41. Conclusion

FCBP-02 tests the most promising local coercive module and finds that the singular part of vortex stretching is no longer the main obstruction.

At fixed relative filter scale:

$$
\boxed{
\text{near-field positive stretching}
}
$$

is absorbed by diffusion.

The differentiated commutator scale loss is also structurally repaired:

$$
\boxed{
\text{scale-worse forcing estimate}
\longrightarrow
\text{scale-invariant increment defect}.
}
$$

But a local critical estimate is not a critical packing theorem.

The far-field reassignment contains a comparable-scale diagonal channel with no gap decay.

Harmonic Taylor remainder gains improve separated scales but do not remove that diagonal.

Moreover harmonic/affine structure alone cannot cancel positive-part work.

To exploit affine cancellation, the signed work must be preserved.

The algebraic route is exact:

$$
\boxed{
\text{signed telescoping}
+
\text{finite negative/backscatter work}
\Longrightarrow
\text{positive-work summability}.
}
$$

The commutator side reaches the same frontier from another direction: persistent surplus forces a persistent scale-critical increment defect, and bounded defect sequences admit a cylindrical Young profile, but no universal unweighted increment packing is available.

Thus the filtered route has achieved a **conditional complete critical-lift compiler** while simultaneously proving that its present unconditional estimates are insufficient.

The next step is no longer another absolute-value estimate.

It is signed work.

---

# References

1. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
2. R. Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322.
3. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
4. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier--Stokes*, arXiv:2606.13887.
5. R. Dascaliuc, Z. Grujić, *Vortex stretching and criticality for the 3D NSE*, arXiv:1205.7080.
6. `NS_FCBP_01_CriticalForest_Coercivity_v0.1.md`.