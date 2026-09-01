---
title: "Navier–Stokes Ancestry Necessity Program 04: Non-Type-I Ancestry Entry, Adaptive Weak-L3 Seeds, UV Square-Tail Extraction and Universal Causal-State Initialization"
short_title: "NS-ANP 04"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style non-Type-I causal entry / universal pre-singularity seed initialization"
epistemic_status: "Treats the branch sup_{t<T*} ||u(t)||_{L^{3,infty}}=infty without assuming a uniform Type-I constant. From weak-L3 superlevel geometry and the global finite-energy bound, extracts times t_n->T*, amplitude levels lambda_n->infty, shrinking effective-volume scales r_n, and dyadic thresholds J_n->infty for which low frequencies cannot account for the superlevel amplitude. This yields a quantitative global ultraviolet vorticity square-tail lower bound of order M_n^4/E_2^2. A controlled terminal ball/weight capturing a fixed fraction of this square-tail defines a canonical Footprint Seed Node with bounded initial aperture. Although no uniform weak-L3 bound exists globally, every pre-singularity seed admits an adaptive backward causal window Delta_n ~ R_n^2/(1+Mbar_n) on which the ANP-02 footprint aperture remains uniformly controlled. Hence non-Type-I failure does not block causal-state initialization; it only makes the causal time step adaptive. Combining this with the Type-I core entry gives a universal two-branch causal-state entry theorem. This does NOT prove arbitrary-depth compatible C3 paths, Full Chain Necessity, Finite Obstruction, or Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 04

# Non-Type-I Ancestry Entry, Adaptive Weak-L3 Seeds, UV Square-Tail Extraction and Universal Causal-State Initialization

## 0. Positioning of this paper

ANP-00--03 built a recursively legal weighted C3 causal edge in the Type-I branch, conditional on a strong selected source atom.

The remaining universal-entry problem is:

$$
\boxed{
\sup_{t<T_\ast}
\|u(t)\|_{L^{3,\infty}}
=
\infty.
}
$$

In this branch there is no single finite constant:

$$
M
$$

with which to define one uniform Type-I core geometry.

The present paper proves that this does **not** prevent causal-state initialization.

The correct replacement is adaptive:

$$
\boxed{
\text{adaptive amplitude}
+
\text{adaptive frequency}
+
\text{adaptive footprint}
+
\text{adaptive causal time step}.
}
$$

---

# 1. Pre-singularity setting

Let:

$$
u
$$

be a smooth finite-energy Navier--Stokes solution on:

$$
[0,T_\ast)
$$

with candidate first singular time:

$$
T_\ast<\infty.
$$

Let:

$$
\boxed{
E_2
=
\sup_{0\le t<T_\ast}
\|u(t)\|_2
<
\infty.
}
$$

By the energy inequality one may take:

$$
E_2
\le
\|u_0\|_2.
$$

Define the weak-L3 quasi-norm:

$$
\boxed{
M(t)
=
\|u(t)\|_{L^{3,\infty}}
=
\sup_{\lambda>0}
\lambda
\,
\left|
\{
x:
|u(t,x)|>\lambda
\}
\right|^{1/3}.
}
$$

Assume the non-Type-I branch:

$$
\boxed{
\sup_{t<T_\ast}M(t)
=
\infty.
}
$$

---

# 2. Non-Type-I times approach the singular horizon

For every:

$$
\varepsilon>0,
$$

the solution is smooth on the compact interval:

$$
[0,T_\ast-\varepsilon].
$$

Hence:

$$
\|u(t)\|_\infty
$$

is uniformly finite there.

Interpolation with the uniform:

$$
L^2
$$

bound gives a finite uniform:

$$
L^{3,\infty}
$$

bound on that compact interval.

Therefore any sequence:

$$
M(t_n)\to\infty
$$

must satisfy:

$$
\boxed{
t_n\uparrow T_\ast.
}
$$

---

# 3. Adaptive Lorentz level

Choose:

$$
t_n<T_\ast
$$

such that:

$$
\boxed{
M_n
=
M(t_n)
\to
\infty.
}
$$

By the definition of the weak-L3 quasi-norm choose:

$$
\lambda_n>0
$$

with:

$$
\boxed{
\lambda_n
m_n^{1/3}
\ge
\frac12
M_n,
}
$$

where:

$$
\boxed{
m_n
=
\left|
E_n
\right|,
\qquad
E_n
=
\{
x:
|u(t_n,x)|>\lambda_n
\}.
}
$$

Define the effective-volume radius:

$$
\boxed{
r_n
=
m_n^{1/3}.
}
$$

---

# 4. Energy restriction on the Lorentz atom

On:

$$
E_n,
$$

$$
|u(t_n)|>\lambda_n.
$$

Hence:

$$
E_2^2
\ge
\int_{E_n}
|u(t_n)|^2dx
\ge
\lambda_n^2m_n.
$$

Since:

$$
\lambda_nm_n^{1/3}
\ge
M_n/2,
$$

$$
\lambda_n^3m_n
\ge
M_n^3/8.
$$

Combining:

$$
\lambda_n^3m_n
\le
\lambda_nE_2^2.
$$

---

# 5. CIV-4.1 — Adaptive Amplitude/Volume Compression

## Theorem 5.1

For the Lorentz atom:

$$
(\lambda_n,E_n),
$$

$$
\boxed{
\lambda_n
\ge
\frac{
M_n^3
}{
8E_2^2
},
}
$$

and:

$$
\boxed{
r_n
\le
4
\frac{
E_2^2
}{
M_n^2
}.
}
$$

Moreover:

$$
\boxed{
\lambda_nr_n
\ge
M_n/2.
}
$$

Therefore:

$$
\boxed{
\lambda_n\to\infty,
\qquad
r_n\to0.
}
$$

### Meaning

Non-Type-I weak-L3 growth forces simultaneous amplitude inflation and effective-volume compression.

$\square$

---

# 6. Important spatial warning

The scale:

$$
r_n
=
|E_n|^{1/3}
$$

is a volume-equivalent radius.

It does **not** imply:

$$
E_n
$$

is contained in one ball of radius:

$$
O(r_n).
$$

The high-amplitude set may be spatially fragmented.

Thus:

$$
\boxed{
\text{volume compression}
\neq
\text{hard-ball concentration}.
}
$$

This distinction is preserved.

---

# 7. Low-frequency exclusion

Let:

$$
P_{\le J}
$$

be a smooth Littlewood--Paley low-pass projector.

Bernstein gives:

$$
\boxed{
\|P_{\le J}u(t_n)\|_\infty
\le
C_B
2^{3J/2}
E_2.
}
$$

Choose the largest integer:

$$
J_n
$$

such that:

$$
\boxed{
C_B
2^{3J_n/2}
E_2
\le
\lambda_n/2.
}
$$

Then:

$$
\boxed{
2^{J_n}
\asymp
\left(
\frac{
\lambda_n
}{
E_2
}
\right)^{2/3}
}
$$

up to fixed LP constants.

By Theorem 5.1:

$$
\boxed{
J_n\to+\infty.
}
$$

---

# 8. CIV-4.2 — Non-Type-I UV Velocity Extraction

## Theorem 8.1

On:

$$
E_n,
$$

$$
\boxed{
|P_{>J_n}u(t_n)|
\ge
\lambda_n/2.
}
$$

Consequently:

$$
\boxed{
\int_{E_n}
|P_{>J_n}u(t_n)|^2dx
\ge
\frac14
\lambda_n^2m_n.
}
$$

In scale-invariant effective-volume form:

$$
\boxed{
r_n^{-1}
\int_{E_n}
|P_{>J_n}u(t_n)|^2dx
\ge
c
M_n^2.
}
$$

### Proof

Use:

$$
u
=
P_{\le J_n}u
+
P_{>J_n}u
$$

and the low-frequency bound.

For the final inequality:

$$
r_n^{-1}
\lambda_n^2m_n
=
(\lambda_nr_n)^2.
$$

$\square$

---

# 9. Velocity-to-vorticity ultraviolet conversion

For divergence-free:

$$
u,
$$

Fourier space gives:

$$
|\widehat\omega(\xi)|
=
|\xi|
|\widehat u(\xi)|.
$$

Hence for a smooth high-pass cutoff:

$$
\boxed{
\|P_{>J_n-C}\omega(t_n)\|_2^2
\ge
c
2^{2J_n}
\|P_{>J_n}u(t_n)\|_2^2.
}
$$

Since the global high-pass velocity norm dominates its norm on:

$$
E_n,
$$

Theorem 8.1 applies.

---

# 10. CIV-4.3 — Global UV Vorticity Seed

## Theorem 10.1

There exists a fixed LP offset:

$$
C_{\rm LP}
$$

such that:

$$
\boxed{
\|P_{>J_n-C_{\rm LP}}\omega(t_n)\|_2^2
\ge
c
\frac{
M_n^4
}{
E_2^2
}.
}
$$

Equivalently, by Littlewood--Paley square-function equivalence:

$$
\boxed{
\sum_{
k>J_n-C_{\rm LP}
}
\|\omega_k(t_n)\|_2^2
\ge
c
\frac{
M_n^4
}{
E_2^2
}.
}
$$

### Proof

From Theorem 8.1:

$$
\|P_{>J_n}u\|_2^2
\ge
c
\lambda_n^2m_n.
$$

The Lorentz atom gives:

$$
m_n
\ge
c
\frac{
M_n^3
}{
\lambda_n^3
}.
$$

Thus:

$$
2^{2J_n}
\lambda_n^2m_n
\ge
c
\left(
\frac{
\lambda_n
}{
E_2
}
\right)^{4/3}
\frac{
M_n^3
}{
\lambda_n
}
=
c
\frac{
M_n^3
\lambda_n^{1/3}
}{
E_2^{4/3}
}.
$$

Use:

$$
\lambda_n
\ge
c
M_n^3/E_2^2.
$$

$\square$

---

# 11. Meaning of Theorem 10.1

The non-Type-I branch forces a sequence of global UV vorticity states with:

$$
\boxed{
J_n\to\infty,
}
$$

and:

$$
\boxed{
\text{UV square-tail enstrophy}
\to
\infty.
}
$$

Thus failure of a uniform weak-L3 Type-I bound does not remove high-frequency state structure.

It strengthens it.

---

# 12. UV square-function density

Define:

$$
\boxed{
G_n(x)
=
\sum_{
k>J_n-C_{\rm LP}
}
|\omega_k(t_n,x)|^2.
}
$$

Then:

$$
G_n\in L^1(\mathbb R^3),
$$

and Theorem 10.1 gives:

$$
\boxed{
\int
G_n(x)dx
\ge
c
\frac{
M_n^4
}{
E_2^2
}.
}
$$

---

# 13. Adaptive spatial capture radius

Define the half-mass concentration radius:

$$
\boxed{
R_n^{50}
=
\inf
\left\{
R>0:
\sup_{x\in\mathbb R^3}
\int_{B(x,R)}
G_n(y)dy
\ge
\frac12
\int G_n
\right\}.
}
$$

Since:

$$
G_n\in L^1,
$$

$$
\boxed{
R_n^{50}<\infty.
}
$$

Choose:

$$
x_n
$$

and a radius at most:

$$
2R_n^{50}
$$

capturing one half of the total square-tail mass.

Set:

$$
\boxed{
R_n
=
\max
\{
2R_n^{50},
2^{-J_n+C_{\rm LP}}
\}.
}
$$

Then:

$$
\boxed{
2^{J_n-C_{\rm LP}}
R_n
\ge
1.
}
$$

---

# 14. Spatial fragmentation coordinate

Define:

$$
\boxed{
\Xi_n
=
2^{J_n-C_{\rm LP}}
R_n
\ge
1.
}
$$

Interpretation:

### $\Xi_n=O(1)$

UV state is concentrated on approximately wavelength/core scale.

### $\Xi_n\gg1$

The half-mass UV state occupies a region containing many wavelengths, or is spatially fragmented enough that a larger capture radius is needed.

Both are legal causal seed geometries.

Large:

$$
\Xi_n
$$

is a numerical spatial-structure coordinate, not failure of node existence.

---

# 15. Canonical terminal cutoff

Choose:

$$
\phi\in C_c^\infty(B_2),
$$

with:

$$
0\le\phi\le1,
\qquad
\phi=1
\text{ on }B_1.
$$

Set:

$$
\boxed{
\chi_n(x)
=
\phi
\left(
\frac{
x-x_n
}{
R_n
}
\right).
}
$$

Then:

$$
\chi_n=1
$$

on the selected half-mass ball.

Define the weighted square-tail:

$$
\boxed{
\mathcal E_n^{seed}
=
\frac12
\sum_{
k>J_n-C_{\rm LP}
}
\int
\chi_n
|\omega_k(t_n)|^2dx.
}
$$

---

# 16. CIV-4.4 — Canonical Non-Type-I Footprint Seed

## Theorem 16.1

The terminal seed satisfies:

$$
\boxed{
\mathcal E_n^{seed}
\ge
c
\frac{
M_n^4
}{
E_2^2
}.
}
$$

Its terminal weight has:

- finite mass:
  $$
  m_{\chi_n}
  \asymp
  R_n^3;
  $$
- center:
  $$
  x_n;
  $$
- bounded dimensionless initial aperture:
  $$
  A_n(0)
  \le
  C_\phi;
  $$
- scale coordinate:
  $$
  \Xi_n
  =
  2^{J_n-C_{\rm LP}}R_n
  \ge1.
  $$

Thus:

$$
\boxed{
\mathsf F_n^{seed}
=
(
t_n,
\chi_n,
\omega(t_n),
\mathbf e^{\chi_n}(t_n),
J_n,
\operatorname{Prov}_n
)
}
$$

is a legal canonical Footprint Node.

$\square$

---

# 17. No singular center is assumed

The center:

$$
x_n
$$

is selected from the actual UV state at:

$$
t_n.
$$

It is not assumed in advance to converge to a singular point.

Thus the non-Type-I entry theorem does not borrow Type-I singular-core provenance.

The future path-coherence problem must determine whether a subsequence of these adaptive centers/footprints belongs to one eventual causal ancestry branch.

---

# 18. Local weak-L3 bound on every pre-singularity compact window

Although:

$$
\sup_{t<T_\ast}
M(t)
=
\infty,
$$

for each fixed:

$$
t_n<T_\ast
$$

and each sufficiently small:

$$
\delta>0,
$$

the solution is smooth on:

$$
[t_n-\delta,t_n].
$$

Therefore:

$$
\boxed{
\overline M_n(\delta)
=
\sup_{
s\in[t_n-\delta,t_n]
}
\|u(s)\|_{L^{3,\infty}}
<
\infty.
}
$$

The constant depends on:

$$
n
$$

and may diverge as:

$$
n\to\infty.
$$

---

# 19. Adaptive causal window

Choose any:

$$
\delta_n^0
\in
(0,t_n]
$$

such that the solution is smooth on:

$$
[t_n-\delta_n^0,t_n].
$$

Set:

$$
\boxed{
\overline M_n
=
\overline M_n(\delta_n^0).
}
$$

For fixed:

$$
\vartheta>0,
$$

define:

$$
\boxed{
\Delta_n
=
\min
\left\{
\delta_n^0,
\frac{
\vartheta R_n^2
}{
1+\overline M_n
}
\right\}.
}
$$

Then:

$$
\boxed{
\Delta_n>0.
}
$$

---

# 20. CIV-4.5 — Adaptive Aperture Renormalization

## Theorem 20.1

Let:

$$
\chi_n(s)
$$

be the adjoint propagation of the terminal seed:

$$
\chi_n(t_n).
$$

For:

$$
t_n-\Delta_n
\le
s
\le
t_n,
$$

ANP-02's aperture estimate gives:

$$
\boxed{
A_n(s)^2
\le
(
1+C_\phi^2
)
e^{C_\phi\vartheta}
-1.
}
$$

The right-hand side is independent of:

$$
\overline M_n.
$$

### Proof

ANP-02 gives:

$$
1+A_n(s)^2
\le
(
1+A_n(t_n)^2
)
\exp
\left(
C_\phi
(1+\overline M_n)
\frac{
t_n-s
}{
R_n^2
}
\right).
$$

The adaptive definition of:

$$
\Delta_n
$$

bounds the exponent by:

$$
C_\phi\vartheta.
$$

$\square$

---

# 21. Meaning of adaptive time

The non-Type-I branch destroys a **uniform** weak-L3 constant.

It does not destroy local causal geometry.

The price is:

$$
\boxed{
\text{large local weak-L3 amplitude}
\Longrightarrow
\text{shorter legal causal time step}.
}
$$

This is a time/amplitude coupling relation.

---

# 22. Adaptive viscous age

Define:

$$
\boxed{
\Pi_{\nu,n}
=
2^{2J_n}
\Delta_n.
}
$$

Unlike the Type-I parabolic core branch, this quantity need not have a uniform positive lower bound.

Thus the non-Type-I entry theorem guarantees causal-state initialization, but not a uniform generation length in viscous-age units.

This distinction becomes important in arbitrary-depth path extraction.

---

# 23. Entry into the ANP source ledger

On:

$$
[t_n-\Delta_n,t_n],
$$

the canonical seed:

$$
\mathsf F_n^{seed}
$$

has:

- an adjoint footprint;
- bounded aperture;
- the full dyadic weighted spectrum;
- exact shellwise vorticity identities;
- the ANP-01 inheritance/source ledger;
- the ANP-03 kernel-inflated source-parent compiler.

Therefore each seed can enter the existing causal alternatives.

---

# 24. Seed causal alternatives

For a selected child shell/source packet, the next causal step is classified as:

### INHERIT

A significant earlier weighted state already exists.

### C3-W STATE-PARENT

A strong selected source atom with bounded residence and partner action yields a weighted C3 parent.

### ACTION-PARENT

A large partner-amplitude action is paid.

### MULTI/DRIVER/DISSIPATION

The source packet enters the already classified DRC finite-carrier/action branches.

The non-Type-I condition introduces no new source-provenance category.

---

# 25. CIV-4.6 — Non-Type-I Causal-State Entry Theorem

## Theorem 25.1

Assume:

$$
\sup_{t<T_\ast}
\|u(t)\|_{L^{3,\infty}}
=
\infty.
$$

Then there exists a sequence:

$$
t_n\uparrow T_\ast
$$

and legal canonical Footprint Seed Nodes:

$$
\boxed{
\mathsf F_n^{seed}
}
$$

such that:

$$
\boxed{
J_n\to+\infty,
}
$$

$$
\boxed{
\mathcal E_n^{seed}
\ge
c
\frac{
M_n^4
}{
E_2^2
}
\to
\infty,
}
$$

and every seed admits a positive adaptive backward causal window:

$$
\Delta_n>0
$$

on which the footprint geometry is uniformly controlled after adaptive time renormalization.

Thus the non-Type-I branch admits pre-singularity causal-state initialization at arbitrarily high frequencies.

$\square$

---

# 26. Type-I / non-Type-I entry merge

For any candidate finite singularity there are two exhaustive branches:

### TYPE-I

$$
\sup_{t<T_\ast}
\|u(t)\|_{L^{3,\infty}}
<
\infty.
$$

The Barker--Prange/DRC/ANP core architecture supplies Type-I state entry.

### NON-TYPE-I

$$
\sup_{t<T_\ast}
\|u(t)\|_{L^{3,\infty}}
=
\infty.
$$

Theorem 25.1 supplies adaptive Lorentz/UV Footprint Seed entry.

---

# 27. CIV-4.7 — Universal Causal-State Entry

## Theorem 27.1

Relative to the two exhaustive weak-L3 branches, every hypothetical finite singularity admits arbitrarily late pre-singularity state entry into the ANP causal ontology.

More precisely:

$$
\boxed{
\operatorname{Blowup}(T_\ast)
}
$$

implies either:

### TYPE-I ENTRY

a quantitative singular-core/UV Footprint Node sequence;

or:

### NON-TYPE-I ENTRY

an adaptive UV Footprint Seed sequence with:

$$
J_n\to\infty.
$$

Thus:

$$
\boxed{
\textbf{universal causal-state entry}
:
\mathrm{PROVED\ RELATIVE\ TO\ THE\ ANP\ ENTRY\ DEFINITIONS}.
}
$$

### Safety

This theorem establishes entry nodes.

It does not establish that the nodes belong to one compatible infinite causal path.

$\square$

---

# 28. Why Lorentz $q<\infty$ results do not replace ANP-04

Quantitative critical-Lorentz regularity results of Feng--He--Wang treat:

$$
L^{3,q},
\qquad
3\le q<\infty.
$$

They do not include the weak endpoint:

$$
L^{3,\infty}.
$$

Thus the present non-Type-I weak-endpoint entry problem is not obtained by directly importing those quantitative finite-$q$ estimates.

---

# 29. Axisymmetric weak-L3 calibration

Ożański--Palasek prove quantitative weak-L3 bounds and a weak-L3 blow-up-rate result for **axisymmetric** strong solutions.

This demonstrates that weak-L3 quantitative control can be developed under additional structure.

ANP-04 does not assume axisymmetry and does not import that theorem into the general branch.

---

# 30. Small weak-L3 regularity calibration

Luo--Tsai prove an endpoint local regularity criterion under sufficiently small:

$$
L_t^\infty L_x^{3,\infty}
$$

velocity and a local pressure hypothesis.

This is compatible with the interpretation that very large weak-L3 states are genuine critical-regime events.

ANP-04's entry theorem, however, is derived directly from the weak-L3 superlevel definition and the global energy bound.

---

# 31. Spacetime status

For the adaptive seed:

$$
\mathsf{ST}_n
=
(
t_n,
T_\ast,
x_n,
R_n,
J_n
).
$$

The exact properties are:

$$
t_n\uparrow T_\ast,
$$

$$
J_n\to\infty,
$$

$$
R_n<\infty.
$$

No universal claim is made that:

$$
R_n\to0.
$$

The effective-volume scale:

$$
r_n
$$

does satisfy:

$$
r_n\to0.
$$

This preserves the distinction between measure compression and geometric concentration radius.

---

# 32. Existence status

### Solution existence

PASS on every pre-singularity interval.

### Seed node existence

PASS.

### Adjoint footprint existence

PASS on the adaptive causal window.

### One-step source edge

Available under the ANP source/inheritance alternatives.

### Arbitrary-depth compatible path

OPEN.

### Infinite chain

OPEN.

---

# 33. Definition status

The non-Type-I branch uses the same canonical Footprint Node semantics as the Type-I branch after initialization.

Thus the two branches merge at:

$$
\boxed{
\mathsf F
=
(
t,\chi,\omega,\mathbf e^\chi,\operatorname{Prov}
).
}
$$

No new recursive node ontology is introduced.

---

# 34. Numerical coordinates

The non-Type-I seed records:

$$
\boxed{
M_n,
\lambda_n,
r_n,
J_n,
R_n,
\Xi_n,
\mathcal E_n^{seed},
\overline M_n,
\Delta_n,
\Pi_{\nu,n}.
}
$$

Key relations:

$$
\lambda_n
\gtrsim
M_n^3/E_2^2,
$$

$$
r_n
\lesssim
E_2^2/M_n^2,
$$

$$
2^{J_n}
\asymp
(\lambda_n/E_2)^{2/3},
$$

$$
\mathcal E_n^{seed}
\gtrsim
M_n^4/E_2^2.
$$

---

# 35. Continuity/discreteness

The sequence:

$$
t_n,J_n
$$

is a discrete sampling of a continuous pre-singularity Navier--Stokes trajectory.

Each seed has a continuous adaptive causal window:

$$
[t_n-\Delta_n,t_n].
$$

Thus hybrid legality remains satisfied.

---

# 36. Coupling

### Amplitude/volume coupling

$$
\lambda_nr_n
\gtrsim
M_n.
$$

### Amplitude/frequency coupling

$$
2^{J_n}
\asymp
(\lambda_n/E_2)^{2/3}.
$$

### Frequency/state coupling

UV vorticity square tail:

$$
\gtrsim
M_n^4/E_2^2.
$$

### Amplitude/time coupling

Large local:

$$
\overline M_n
$$

shrinks the legal causal step:

$$
\Delta_n
\lesssim
R_n^2/(1+\overline M_n).
$$

---

# 37. Phase-like regimes

The non-Type-I entry has operational transitions:

### Lorentz growth

$$
M_n\to\infty.
$$

### Amplitude compression

$$
\lambda_n\to\infty.
$$

### Volume compression

$$
r_n\to0.
$$

### UV transition

$$
J_n\to\infty.
$$

### Spatial compact/diffuse coordinate

$$
\Xi_n
=
O(1)
$$

versus:

$$
\Xi_n\gg1.
$$

These are pre-singularity causal-state regimes, not thermodynamic phases.

---

# 38. Causality status

The weak-L3 to UV-seed implication is:

$$
\boxed{
C1
}
$$

as a necessary same-time structural extraction.

Once the seed is initialized, its subsequent inheritance/source edges use the exact ANP vorticity dynamics and may achieve:

$$
C2
$$

or:

$$
C3_W.
$$

Thus entry extraction itself is not mislabeled as a forward-time source cause.

---

# 39. Predictability

Theorem 5.1 gives a P2 conditional structural forecast:

large:

$$
M_n
$$

forces:

$$
\lambda_n
\gtrsim
M_n^3,
$$

and:

$$
r_n
\lesssim
M_n^{-2}
$$

after energy normalization.

Theorem 10.1 predicts a minimum UV vorticity square-tail magnitude:

$$
\gtrsim
M_n^4/E_2^2.
$$

These are conditional scale/state forecasts.

They do not predict blow-up.

---

# 40. Interpretability

The non-Type-I entry answers:

### WHEN

At times:

$$
t_n\uparrow T_\ast.
$$

### WHERE

At adaptive UV capture balls:

$$
B(x_n,R_n).
$$

### SCALE

Frequency:

$$
J_n\to\infty.
$$

### WHAT

Weighted UV vorticity square-tail state.

### HOW

Weak-L3 superlevel geometry, energy restriction, low-frequency exclusion, velocity-to-vorticity conversion.

### HOW MUCH

Explicit:

$$
M_n^4/E_2^2
$$

state lower bound.

### WHY LEGAL

Finite-energy Navier--Stokes state, Bernstein, LP/Fourier structure, and canonical Footprint Node definitions.

---

# 41. Remaining universal Chain-Necessity gap

After ANP-04, the two branch-entry problem is no longer open.

The remaining issue is:

$$
\boxed{
\textbf{arbitrary-depth compatible C3 path construction}.
}
$$

In the Type-I branch:

- C3_W source-parent edges exist on strong source atoms.

In the non-Type-I branch:

- arbitrarily late UV seeds exist;
- each seed can enter the same adaptive Footprint Node machinery.

What is not proved is that one can recursively select compatible parents through arbitrarily many generations with sufficient quantitative nondegeneracy.

---

# 42. Next paper

The next paper is:

$$
\boxed{
\textbf{
NS-ANP 05 —
Arbitrary-Depth Compatible C3 Paths,
Adaptive Step Renormalization,
Branch Compactness
and Finite-Path Realizability
}.
}
$$

Primary tasks:

1. define generation-wise quantitative budgets:
   $$
   \eta_n,
   \mathfrak H_n,
   \mathcal A_n,
   \Delta_n;
   $$
2. prove a no-terminal-node theorem for dangerous branches or identify the exact terminal escape;
3. combine Type-I and non-Type-I seeds with the same C3_W recursive node class;
4. prove compatible finite C3 paths of arbitrary depth;
5. only then invoke finite/infinite path extraction.

---

# 43. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{non-Type-I time sequence}
&:\ \mathrm{PROVED},\\
\text{weak-L3 Lorentz atom}
&:\ \mathrm{PROVED},\\
\text{amplitude lower bound}
&:\ \mathrm{PROVED},\\
\text{effective-volume compression}
&:\ \mathrm{PROVED},\\
\text{low-frequency exclusion}
&:\ \mathrm{PROVED},\\
\text{UV velocity seed}
&:\ \mathrm{PROVED},\\
\text{global UV vorticity square-tail seed}
&:\ \mathrm{PROVED},\\
\text{canonical non-Type-I Footprint Seed}
&:\ \mathrm{PROVED},\\
\text{adaptive causal-window aperture control}
&:\ \mathrm{PROVED},\\
\text{non-Type-I causal-state entry}
&:\ \mathrm{PROVED},\\
\text{universal Type-I/non-Type-I state entry}
&:\ \mathrm{PROVED\ RELATIVE\ TO\ ANP\ DEFINITIONS},\\
\text{arbitrary-depth compatible C3 paths}
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

# 44. Conclusion

The non-Type-I branch does not destroy ancestry entry.

If:

$$
\|u(t_n)\|_{L^{3,\infty}}
=
M_n
\to\infty,
$$

the finite-energy bound forces a Lorentz superlevel atom with:

$$
\boxed{
\lambda_n
\gtrsim
M_n^3/E_2^2,
}
$$

and effective volume scale:

$$
\boxed{
r_n
\lesssim
E_2^2/M_n^2.
}
$$

Low frequencies cannot generate this amplitude once:

$$
2^{J_n}
\asymp
(\lambda_n/E_2)^{2/3}.
$$

Thus:

$$
J_n\to\infty,
$$

and the vorticity square tail satisfies:

$$
\boxed{
\sum_{k>J_n-C}
\|\omega_k(t_n)\|_2^2
\gtrsim
M_n^4/E_2^2.
}
$$

A controlled terminal ball captures a fixed fraction of that state and initializes the canonical Footprint Node.

The absence of a global Type-I constant only forces the backward causal step to become adaptive:

$$
\boxed{
\Delta_n
\lesssim
\frac{
R_n^2
}{
1+\overline M_n
}.
}
$$

On that window, adjoint aperture remains controlled.

Therefore both Type-I and non-Type-I branches now enter the same ANP causal-state ontology.

The next problem is no longer entry.

It is path depth.

---

# References

1. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487--1541; arXiv:1812.09115.
2. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717.
3. W. Feng, J. He, W. Wang, *Quantitative bounds for critically bounded solutions to the three-dimensional Navier--Stokes equations in Lorentz spaces*, arXiv:2201.04656.
4. Y. Luo, T.-P. Tsai, *Regularity criteria in weak $L^3$ for 3D incompressible Navier--Stokes equations*, arXiv:1310.8307.
5. W. S. Ożański, S. Palasek, *Quantitative control of solutions to the axisymmetric Navier--Stokes equations in terms of the weak $L^3$ norm*, arXiv:2210.10030. Used only as axisymmetric weak-L3 quantitative calibration.
6. `NS_ANP_02_RecursiveEdge_FootprintRecapture_v0.1.md`.
7. `NS_ANP_03_SourceParent_Recapture_C3Upgrade_v0.1.md`.