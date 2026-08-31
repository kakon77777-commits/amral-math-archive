---
title: "Navier–Stokes Tangent Singular Kernel Rigidity Program 03：Localized Quadratic Fixed Points、Harmonic Rank-One Rigidity、Nodal Sign Fibers、One-Sided Covariance Tangents 與 Residual Fixed-Orbit Classification"
short_title: "NS-TSKR 03"
series: "Navier–Stokes Tangent Singular Kernel Rigidity Program"
cycle: "X"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Localized fixed-point and one-sided residual-kernel rigidity"
epistemic_status: "Continues Cycle X after the global quadratic fixed-point rigidity of TSKR-02. Proves a localized coarse-graining commutator theorem: after multiplying by an interior cutoff, the high-frequency part of a locally tangent quadratic source is controlled by the local fixed-point mismatch plus an explicit O(ell grad chi) boundary/localization commutator. Thus localized approximate tangency can hide only in low-frequency/nonlocal boundary sectors once high-frequency source mismatch is small. Shows that a naive localization of the global fixed-point theorem is false: for a radial spatial averaging kernel every componentwise harmonic tensor is an exact local fixed point. Proves a Rank-One Harmonic Matrix Rigidity theorem: a nonzero componentwise harmonic positive-semidefinite rank-one matrix field on a connected region has a fixed spatial direction F=h v tensor v with h>0 harmonic. Consequently a continuous quadratic velocity realization is a fixed-direction shear u=sigma sqrt(h) v, and incompressibility forces v dot grad h=0. Gives explicit nonconstant local examples, so local fixed-point rigidity has a genuine harmonic branch. Proves a Dynamic Harmonic Shear Rigidity theorem for clean projected Navier-Stokes/heat evolution: if a fixed-direction divergence-free shear evolves without harmonic-pressure drive and its quadratic tensor remains componentwise harmonic through a time interval, then it is spatially constant; finite-energy whole-space or zero-mean periodic branches are trivial. Hence a recurrent nontrivial harmonic tangent branch must use localization, boundary/harmonic-pressure leakage, or failure of clean projected evolution. Proves analytic nodal-sign rigidity: for real-analytic u and U on a connected region, u tensor u=U tensor U forces one global sign U=plus-or-minus u; one trace anchor fixes the plus sign. This is compatible with classical spatial analyticity of smooth Navier-Stokes solutions but is not asserted for singular limit packages. On the residual side, proves PSD-cone closure under intrinsic normalization and an energy-collapse estimate ||R||<=tr R: an actual nonnegative Reynolds covariance cannot produce a nonzero sign-changing normalized residual if its relative covariance-energy observation vanishes. Linearizing exact tangent geometry at a reproduced zero-covariance base U=u,R=0 yields dR=u tensor w+w tensor u. If dR is a one-sided positive-semidefinite tangent, then w=alpha u with alpha>=0; first-order covariance-energy invisibility forces alpha=0, so du=dU and dR=0 away from the zero-velocity set. Therefore a surviving sign-changing stress kernel must be a two-sided mismatch/quotient direction, localization/harmonic residual, zero-base quadratic degeneracy, or another non-covariance residual. The remaining TRSK is compressed to localized low-frequency/harmonic fixed orbits, nodal/zero-base degeneracy, two-sided mismatch stress, ASC failure, and amplitude summability. No complete TRSK exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Tangent Singular Kernel Rigidity Program 03

# Localized Quadratic Fixed Points、Harmonic Rank-One Rigidity、Nodal Sign Fibers、One-Sided Covariance Tangents 與 Residual Fixed-Orbit Classification

## 0. 本文定位

TSKR-02 proved:

$$
\boxed{
u\otimes u
=
U\otimes U+R,
\quad
R\ge0
}
$$

forces a rank-one attenuation fiber.

It also proved global exact coarse-graining fixed-point rigidity.

The remaining problem is local.

A finite-window branch may exploit:

- cutoff localization;
- low frequencies;
- harmonic modes;
- nodal sign changes;
- linearized sign-changing residuals.

This paper separates those mechanisms.

---

# 1. Spatial coarse-graining operator

For the localization results in Sections 1--15, use a spatial convolution:

$$
\boxed{
S_\ell f
=
\rho_\ell*f,
}
$$

where:

$$
\rho\ge0,
\qquad
\int\rho=1,
$$

and:

$$
\rho_\ell(x)
=
\ell^{-d}\rho(x/\ell).
$$

The radial/harmonic results will additionally assume:

$$
\rho(x)=\varrho(|x|).
$$

### Safety

These sections concern a spatial coarse source coordinate or time-slice spatial filtering.

A genuinely spacetime mollifier requires a corresponding parabolic fixed-point analysis.

---

# 2. Localized fixed-point mismatch

Let:

$$
f=u\otimes u.
$$

Define:

$$
\boxed{
m_\ell
=
f-S_\ell f.
}
$$

Let:

$$
\chi
$$

be a smooth compactly supported spatial cutoff.

Set:

$$
g=\chi f.
$$

---

# 3. Exact cutoff identity

A direct calculation gives:

$$
\boxed{
g-S_\ell g
=
\chi m_\ell
+
[\chi,S_\ell]f,
}
$$

where:

$$
\boxed{
[\chi,S_\ell]f
=
\chi S_\ell f
-
S_\ell(\chi f).
}
$$

This identity separates interior source mismatch from localization leakage.

---

# 4. Cutoff commutator estimate

Let:

$$
m_1(\rho)
=
\int
|z|
\rho(z)dz.
$$

Then:

$$
\boxed{
\|
[\chi,S_\ell]f
\|_2
\le
\ell
m_1(\rho)
\|\nabla\chi\|_\infty
\|f\|_2.
}
$$

### Proof

Use:

$$
[\chi,S_\ell]f(x)
=
\int
\rho_\ell(y)
\left[
\chi(x)-\chi(x-y)
\right]
f(x-y)dy.
$$

The mean-value bound gives:

$$
|
\chi(x)-\chi(x-y)
|
\le
\|\nabla\chi\|_\infty
|y|.
$$

Apply Minkowski and translation invariance of:

$$
L^2.
$$

$\square$

---

# 5. High-frequency spectral gap

Fix:

$$
\kappa>0.
$$

Let:

$$
P_{\ge\kappa/\ell}
$$

project to:

$$
|\xi|\ge\kappa/\ell.
$$

Define:

$$
q_\kappa
=
\sup_{|\eta|\ge\kappa}
|\widehat\rho(\eta)|.
$$

For a nondegenerate smooth probability kernel:

$$
q_\kappa<1.
$$

---

# 6. CIV/X-3.1 — Localized High-Frequency Tangency Rigidity

## Theorem 6.1

Under Sections 1--5:

$$
\boxed{
\|
P_{\ge\kappa/\ell}
(
\chi f
)
\|_2
\le
\frac{
1
}{
1-q_\kappa
}
\left[
\|
\chi
(
f-S_\ell f
)
\|_2
+
\ell
m_1(\rho)
\|\nabla\chi\|_\infty
\|f\|_2
\right].
}
$$

### Proof

Apply the global spectral gap to:

$$
g=\chi f.
$$

Then use the cutoff identity and Section 4.

$\square$

---

# 7. Meaning

If:

$$
\|\nabla\chi\|_\infty
\lesssim
R^{-1},
$$

with:

$$
R\gg\ell,
$$

then the localization error is:

$$
O(\ell/R).
$$

Therefore a locally tangent quadratic source with small interior mismatch has small relative high-frequency mass unless it pays boundary/localization leakage.

The surviving local tangent sector is:

$$
\boxed{
\text{LOW FREQUENCY}
\vee
\text{BOUNDARY/LOCALIZATION}.
}
$$

---

# 8. Why global fixed-point rigidity does not localize directly

Suppose now:

$$
\rho
$$

is radial.

If a scalar:

$$
h
$$

is harmonic on a neighborhood containing every ball reached by the kernel support, the mean-value property gives:

$$
\boxed{
S_\ell h=h.
}
$$

Thus componentwise harmonic tensors are exact local fixed points.

---

# 9. CIV/X-3.2 — Harmonic Local Fixed-Point No-Go

## Theorem 9.1

For radial spatial averaging, a local equation:

$$
\boxed{
f=S_\ell f
}
$$

does not imply:

$$
f
$$

is constant.

Every componentwise harmonic tensor is an exact local fixed point on interior points whose averaging support remains inside the harmonicity region.

### Meaning

The global whole-space fixed-point theorem cannot be naively localized.

The local fixed-point kernel contains a genuine harmonic sector.

$\square$

---

# 10. Rank-one harmonic matrix

Let:

$$
\Omega
$$

be connected.

Let:

$$
F:
\Omega
\to
\operatorname{Sym}_d
$$

satisfy:

$$
F(x)\ge0,
$$

$$
\operatorname{rank}F(x)\le1,
$$

and suppose every component:

$$
F_{ij}
$$

is harmonic.

Assume:

$$
F\not\equiv0.
$$

---

# 11. CIV/X-3.3 — Rank-One Harmonic Matrix Rigidity

## Theorem 11.1

There exist:

- a constant nonzero vector:
  $$
  v\in\mathbb R^d;
  $$
- a positive harmonic scalar:
  $$
  h>0
  $$

such that:

$$
\boxed{
F(x)
=
h(x)
v\otimes v
}
$$

throughout:

$$
\Omega.
$$

### Proof

Choose:

$$
i
$$

such that:

$$
F_{ii}
$$

is not identically zero.

Since:

$$
F_{ii}\ge0
$$

and harmonic, the strong maximum principle gives:

$$
h:=F_{ii}>0
$$

on:

$$
\Omega.
$$

Define:

$$
q_j
=
F_{ij}/h.
$$

Rank-one positivity gives:

$$
F_{jj}
=
h q_j^2.
$$

Because:

$$
F_{ij}=h q_j
$$

and:

$$
F_{jj}=h q_j^2
$$

are harmonic:

$$
0
=
\Delta(hq_j)
=
h\Delta q_j
+
2\nabla h\cdot\nabla q_j,
$$

and:

$$
0
=
\Delta(hq_j^2)
=
2q_j
\left[
h\Delta q_j
+
2\nabla h\cdot\nabla q_j
\right]
+
2h
|\nabla q_j|^2.
$$

Hence:

$$
2h|\nabla q_j|^2=0.
$$

So every:

$$
q_j
$$

is constant.

Thus all matrix columns have one fixed direction and:

$$
F=h v\otimes v.
$$

$\square$

---

# 12. Velocity realization

If:

$$
F=u\otimes u
$$

with continuous:

$$
u,
$$

then Theorem 11.1 gives:

$$
\boxed{
u(x)
=
\sigma
\sqrt{
h(x)
}
v,
}
$$

where:

$$
\sigma\in\{-1,1\}
$$

is constant on each connected nonzero branch.

If:

$$
\nabla\cdot u=0,
$$

then:

$$
\boxed{
v\cdot\nabla h=0.
}
$$

Thus the harmonic tangent branch is a fixed-direction shear-type geometry.

---

# 13. Nontrivial local harmonic tangent example

Take:

$$
v=e_1,
$$

and on a region where:

$$
2+y>0,
$$

set:

$$
h(y,z)=2+y.
$$

Then:

$$
h
$$

is positive harmonic and:

$$
v\cdot\nabla h=0.
$$

Define:

$$
u
=
\sqrt{
2+y
}
e_1.
$$

Then:

$$
\nabla\cdot u=0,
$$

and:

$$
u\otimes u
=
(2+y)
e_1\otimes e_1
$$

is componentwise harmonic.

For every sufficiently small radial averaging scale:

$$
\ell,
$$

$$
\boxed{
S_\ell(u\otimes u)
=
u\otimes u
}
$$

on interior points.

### Meaning

Localized exact quadratic tangency has genuine nonconstant examples.

---

# 14. Clean shear dynamics

Let:

$$
u(x,t)
=
a(x,t)v,
$$

where:

$$
v
$$

is a constant vector and:

$$
v\cdot\nabla a=0.
$$

Then:

$$
(u\cdot\nabla)u=0.
$$

On a whole-space/periodic clean projected Navier--Stokes branch with no harmonic-pressure drive:

$$
\boxed{
\partial_t a
=
\nu\Delta a.
}
$$

---

# 15. Harmonic-square persistence

Set:

$$
h=a^2.
$$

Assume for every:

$$
t
$$

in a nontrivial time interval:

$$
\boxed{
\Delta h(\cdot,t)=0.
}
$$

Then:

$$
\boxed{
h_t
=
-2\nu
|\nabla a|^2
=
-\frac{\nu}{2}
\frac{
|\nabla h|^2
}{
h
}
}
$$

on the positive branch.

Since:

$$
h_t
$$

is also harmonic, the scalar:

$$
q
=
\frac{
|\nabla h|^2
}{
h
}
$$

is harmonic.

---

# 16. Convexity identity

For positive harmonic:

$$
h,
$$

one has:

$$
\boxed{
\Delta
\left(
\frac{
|\nabla h|^2
}{
h
}
\right)
=
\frac{
2
}{
h
}
\left|
D^2h
-
\frac{
\nabla h\otimes\nabla h
}{
h
}
\right|^2.
}
$$

This is nonnegative.

---

# 17. CIV/X-3.4 — Dynamic Harmonic Shear Rigidity

## Theorem 17.1

Under Sections 14--16, if:

$$
a^2
$$

is spatially harmonic for every time in a nontrivial interval, then:

$$
\boxed{
\nabla h=0.
}
$$

Hence:

$$
a
$$

is spatially constant.

The heat equation then makes:

$$
a
$$

constant in time as well.

### Proof

Because:

$$
q
$$

is harmonic:

$$
\Delta q=0.
$$

Section 16 gives:

$$
D^2h
=
\frac{
\nabla h\otimes\nabla h
}{
h
}.
$$

Taking traces yields:

$$
0
=
\Delta h
=
\frac{
|\nabla h|^2
}{
h
}.
$$

Thus:

$$
\nabla h=0.
$$

$\square$

---

# 18. Harmonic-pressure escape

Theorem 17.1 uses the clean projected heat evolution.

On a localized finite window, spatially harmonic pressure is a physical pressure component and is not gauge.

A local shear may therefore be driven by:

$$
\boxed{
\text{harmonic-pressure/boundary forcing}
}
$$

which is not removed by the clean global argument.

This is consistent with the external finite-window framework, which retains spatially harmonic pressure and pressure-tail coordinates.

Thus a recurrent nontrivial harmonic tangent branch must pay:

$$
\boxed{
\text{LOCALIZATION}
\vee
\text{HARMONIC PRESSURE}
\vee
\text{NON-CLEAN EVOLUTION}.
}
$$

---

# 19. Analytic sign fiber

Let:

$$
\Omega
$$

be connected.

Let:

$$
u,U:
\Omega
\to
\mathbb R^d
$$

be real analytic.

Assume:

$$
\boxed{
u\otimes u
=
U\otimes U.
}
$$

---

# 20. CIV/X-3.5 — Analytic Nodal Sign Rigidity

## Theorem 20.1

If:

$$
u\not\equiv0,
$$

then there is one global:

$$
\boxed{
\sigma\in\{-1,1\}
}
$$

such that:

$$
\boxed{
U=\sigma u
}
$$

throughout:

$$
\Omega.
$$

If a selected trace/reproduction anchor gives:

$$
U(x_0)=u(x_0)
$$

at one point with:

$$
u(x_0)\neq0,
$$

then:

$$
\boxed{
U=u
}
$$

throughout:

$$
\Omega.
$$

### Proof

Choose one component:

$$
u_i
$$

not identically zero.

On a nonempty open component where:

$$
u_i\neq0,
$$

outer-product equality gives one constant local sign:

$$
U=\sigma u.
$$

The analytic vector field:

$$
U-\sigma u
$$

vanishes on a nonempty open set.

Unique continuation for real-analytic functions gives global vanishing.

$\square$

---

# 21. External analyticity calibration

Spatial analyticity is classical for suitable strong/mild Navier--Stokes branches at positive times under the corresponding regularity hypotheses.

Recent quantitative analyticity work and classical Gevrey theory provide this calibration.

### Safety

Theorem 20.1 is not applied automatically to singular limit packages or arbitrary suitable weak profiles.

Analyticity of both compared fields must be available on the branch.

---

# 22. Actual covariance under intrinsic normalization

Let:

$$
R_n(x)\ge0
$$

be actual Reynolds covariance fields.

Let:

$$
\rho_n>0.
$$

Suppose:

$$
\boxed{
\widehat R_n
=
R_n/\rho_n
}
$$

converges weakly as matrix-valued measures or in a topology preserving nonnegative quadratic-form tests.

---

# 23. CIV/X-3.6 — PSD Cone Closure Under Intrinsic Normalization

## Theorem 23.1

Every such limit:

$$
R_\ast
$$

is positive semidefinite in the distributional/measure sense.

If the limit is represented by a matrix-valued function, then:

$$
\boxed{
R_\ast(x)\ge0
}
$$

almost everywhere.

### Proof

For every constant vector:

$$
\xi
$$

and every nonnegative test function:

$$
\phi,
$$

$$
\int
\phi
\xi^\top
\widehat R_n
\xi
\ge0.
$$

Pass to the limit.

$\square$

---

# 24. Covariance trace controls covariance norm

For every positive semidefinite matrix:

$$
R,
$$

$$
\boxed{
\|R\|_F
\le
\operatorname{tr}R.
}
$$

Therefore:

$$
\boxed{
\frac{
\|R_n\|_{L^1}
}{
\rho_n
}
\le
\frac{
\|\operatorname{tr}R_n\|_{L^1}
}{
\rho_n
}.
}
$$

---

# 25. CIV/X-3.7 — Relative Energy Collapse of Actual Covariance

## Theorem 25.1

If:

$$
R_n\ge0
$$

and the normalized covariance-energy trace satisfies:

$$
\boxed{
\frac1{\rho_n}
\int
\operatorname{tr}R_n
\to0,
}
$$

then:

$$
\boxed{
\frac{
\|R_n\|_{L^1}
}{
\rho_n
}
\to0.
}
$$

### Meaning

An actual positive Reynolds covariance cannot leave a nonzero sign-changing normalized residual after relative energy invisibility.

Any surviving sign-changing stress must come from a mismatch/difference/residual coordinate, not from the actual covariance itself.

$\square$

---

# 26. Linearized exact tangent geometry

Linearize:

$$
\boxed{
u\otimes u
-
U\otimes U
-
R
=
0
}
$$

at a reproduced zero-covariance base:

$$
\boxed{
U=u,
\qquad
R=0.
}
$$

Let:

$$
\dot u,
\qquad
\dot U,
\qquad
\dot R
$$

be one-sided variations.

Define:

$$
\boxed{
w
=
\dot u-\dot U.
}
$$

Then first-order tangency gives:

$$
\boxed{
\dot R
=
u\otimes w
+
w\otimes u.
}
$$

---

# 27. One-sided covariance tangent cone

If the variations arise from:

$$
R_\varepsilon\ge0,
\qquad
R_0=0,
\qquad
\varepsilon\downarrow0,
$$

then:

$$
\boxed{
\dot R\ge0.
}
$$

This is the tangent cone of the PSD cone at its vertex.

---

# 28. CIV/X-3.8 — One-Sided Tangent Attenuation Rigidity

## Theorem 28.1

Assume:

$$
u\neq0,
$$

$$
\dot R
=
u\otimes w+w\otimes u,
$$

and:

$$
\dot R\ge0.
$$

Then:

$$
\boxed{
w=\alpha u,
\qquad
\alpha\ge0,
}
$$

and:

$$
\boxed{
\dot R
=
2\alpha
u\otimes u.
}
$$

### Proof

For every:

$$
x\perp u,
$$

$$
x^\top
\dot R
x
=
0.
$$

For a positive semidefinite matrix, zero quadratic form in direction:

$$
x
$$

implies:

$$
\dot R x=0.
$$

Thus:

$$
\dot R
$$

annihilates:

$$
u^\perp
$$

and has range inside:

$$
\operatorname{span}\{u\}.
$$

The formula:

$$
u\otimes w+w\otimes u
$$

then forces:

$$
w
$$

to be parallel to:

$$
u.
$$

Write:

$$
w=\alpha u.
$$

Positivity gives:

$$
\alpha\ge0.
$$

$\square$

---

# 29. CIV/X-3.9 — First-Order Energy-Rigid Reproduction

## Theorem 29.1

Under Theorem 28.1, if the first-order covariance-energy trace is invisible:

$$
\boxed{
\operatorname{tr}\dot R=0,
}
$$

then:

$$
\boxed{
\alpha=0,
}
$$

and hence:

$$
\boxed{
\dot u=\dot U,
\qquad
\dot R=0.
}
$$

### Proof

$$
\operatorname{tr}\dot R
=
2\alpha
|u|^2.
$$

Since:

$$
u\neq0,
$$

the conclusion follows.

$\square$

---

# 30. Zero-base quadratic degeneracy

At points where:

$$
u=0,
$$

the first derivative of:

$$
u\mapsto u\otimes u
$$

vanishes.

Then first-order source tangency does not determine:

$$
\dot u-\dot U.
$$

Thus the nodal/zero-velocity set is a genuine quadratic degeneracy.

Define:

$$
\boxed{
\textbf{ZQD — Zero-Base Quadratic Degeneracy}.
}
$$

This is distinct from the sign fiber on:

$$
u\neq0.
$$

---

# 31. Two-sided stress versus one-sided covariance

A sign-changing formal stress variation may arise as:

- a difference between two positive packages;
- a quotient mismatch coordinate;
- a centered linearized residual around a nonzero covariance base;
- localization/harmonic subtraction.

It does **not** represent a one-sided actual covariance tangent at:

$$
R=0.
$$

Therefore the residual taxonomy must distinguish:

$$
\boxed{
\textbf{ACTUAL PSD COVARIANCE}
}
$$

from:

$$
\boxed{
\textbf{TWO-SIDED MISMATCH STRESS}.
}
$$

---

# 32. Localized residual fixed-orbit classes

After Sections 6--31, a surviving TRSK branch is reduced to the following classes.

### LHF

Localized harmonic/low-frequency fixed point:

$$
f\approx S_\ell f
$$

with high-frequency mass paid away.

### HPR

Harmonic-pressure or boundary/localization-supported tangent branch.

### ZQD

Zero-base/nodal quadratic degeneracy.

### TSM

Two-sided sign-changing mismatch stress, not actual positive covariance.

### ASC

Adjoint synchronization/certificate failure.

### AMP

Physical residual amplitude remains summable.

---

# 33. CIV/X-3.10 — Localized TRSK Compression Theorem

## Theorem 33.1

Assume a recurrent tangent package satisfies:

1. small canonical quadratic source mismatch;
2. a cutoff with:
   $$
   \ell\|\nabla\chi\|_\infty\ll1;
   $$
3. relative energy invisibility of the actual positive covariance;
4. either analytic sign rigidity or a selected trace anchor away from the zero set;
5. one-sided NS-realizable covariance tangency whenever the base covariance vanishes.

Then every nontrivial surviving normalized residual lies in:

$$
\boxed{
\mathrm{LHF}
\vee
\mathrm{HPR}
\vee
\mathrm{ZQD}
\vee
\mathrm{TSM}
\vee
\mathrm{ASC}
\vee
\mathrm{AMP}.
}
$$

### Safety

This is a reduction theorem.

It does not prove these classes empty.

$\square$

---

# 34. Dynamic harmonic branch status

The harmonic local fixed-point sector is partially closed.

### clean whole-space/periodic evolution

Persistent exact harmonic quadratic tangency collapses to a constant shear; finite-energy or zero-mean branches are trivial.

### localized finite-window evolution

Nontrivial harmonic tangent recurrence must be sustained by:

- harmonic pressure;
- boundary/localization;
- non-clean transition/reproduction;
- or approximate rather than exact harmonicity.

Thus harmonic tangency is no longer a free interior mechanism.

---

# 35. Nodal sign status

On analytic nonzero branches:

$$
\boxed{
\text{sign fiber}
\to
\text{one global }\mathbb Z_2\text{ choice}.
}
$$

A single trace anchor removes that choice.

The unresolved sign problem is concentrated near:

$$
\boxed{
u=0
}
$$

or in singular/nonanalytic limit packages.

Thus the nodal problem merges with:

$$
\boxed{
\mathrm{ZQD}.
}
$$

---

# 36. Linearized stress status

The actual covariance channel is no longer a source of sign-changing invisible normalized stress under relative energy invisibility.

The surviving sign-changing stress is:

$$
\boxed{
\mathrm{TSM}
}
$$

— a two-sided mismatch/quotient residual.

It must be attacked using:

- source-reproduction compatibility;
- pressure/flux response;
- LEI slack;
- model-cone;
- increment channels;
- or a direct quotient-kernel theorem.

---

# 37. Next paper

The next paper should attack the remaining two hard residuals:

$$
\boxed{
\textbf{
NS-TSKR 04 —
Two-Sided Mismatch Stress、
Zero-Base Degeneracy、
Harmonic-Pressure Leakage、
Adjoint Compatibility、
Amplitude Tax
與 Cycle-X Closure Audit
}.
}
$$

Primary tasks:

1. classify the two-sided linearized mismatch:
   $$
   \dot{\mathcal C}
   =
   u\otimes\dot u+\dot u\otimes u
   -
   U\otimes\dot U-\dot U\otimes U-\dot R;
   $$

2. determine which sign-changing directions survive pressure/flux/energy/LEI/model-cone/increment intersection;

3. use quadratic second-order terms near:
   $$
   u=0
   $$
   to resolve ZQD;

4. quantify harmonic-pressure/localization support of nontrivial local harmonic fixed points;

5. combine analytic/trace sign anchoring with moving-window recurrence;

6. revisit ASC on the now-compressed fixed-orbit class;

7. decide whether Cycle X closes TRSK or leaves a canonical two-sided residual phantom.

---

# 38. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Localized High-Frequency Tangency Rigidity}
&:\ \mathrm{PROVED},\\
\text{Harmonic Local Fixed-Point exclusion}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{Rank-One Harmonic Matrix Rigidity}
&:\ \mathrm{PROVED},\\
\text{Dynamic Harmonic Shear Rigidity}
&:\ \mathrm{PROVED\ ON\ CLEAN\ PROJECTED\ BRANCH},\\
\text{Analytic Nodal Sign Rigidity}
&:\ \mathrm{PROVED},\\
\text{PSD Cone Closure}
&:\ \mathrm{PROVED},\\
\text{Relative Energy Collapse of Actual Covariance}
&:\ \mathrm{PROVED},\\
\text{One-Sided Tangent Attenuation Rigidity}
&:\ \mathrm{PROVED},\\
\text{First-Order Energy-Rigid Reproduction}
&:\ \mathrm{PROVED},\\
\text{localized harmonic-pressure branch exclusion}
&:\ \mathrm{OPEN},\\
\text{Zero-Base Quadratic Degeneracy exclusion}
&:\ \mathrm{OPEN},\\
\text{Two-Sided Mismatch Stress exclusion}
&:\ \mathrm{OPEN},\\
ASC
&:\ \mathrm{OPEN},\\
\text{physical amplitude Critical Lift}
&:\ \mathrm{OPEN},\\
\text{TRSK exclusion}
&:\ \mathrm{OPEN/PARTIAL},\\
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

# 39. Conclusion

TSKR-03 localizes the quadratic fixed-point problem and sharply separates true local escape mechanisms from artifacts of an over-broad kernel description.

The global fixed-point theorem cannot simply be copied into a finite window.

Radial averaging has a genuine local harmonic fixed-point sector.

But rank-one positivity makes that sector extremely rigid: every nonzero harmonic quadratic tensor has one fixed spatial direction and one positive harmonic amplitude.

Its velocity realization is a fixed-direction shear.

If such a shear evolves under clean projected Navier--Stokes dynamics while remaining exactly harmonic at the quadratic level through time, viscosity forces it to be constant.

Therefore a nontrivial recurrent harmonic tangent branch must be supported by harmonic pressure, localization/boundary effects, or failure of clean reproduction.

The nodal sign fiber also contracts.

On analytic branches, quadratic equality determines one global sign, and one selected trace anchor fixes the sign.

The unresolved sign problem is concentrated at the zero set or in singular/nonanalytic limits.

Most importantly, actual Reynolds covariance can no longer masquerade as a sign-changing singular kernel.

Positive covariance is preserved under intrinsic normalization, and relative energy invisibility kills its normalized amplitude.

At the reproduced zero-covariance base, one-sided tangent geometry is again rank-one attenuation; first-order energy invisibility forces exact first-order reproduction.

Thus the remaining sign-changing stress is necessarily a two-sided mismatch/quotient residual.

The surviving TRSK is now:

$$
\boxed{
\textbf{
localized low-frequency/harmonic
+
harmonic-pressure/localization
+
zero-base degeneracy
+
two-sided mismatch stress
+
ASC
+
amplitude.
}
}
$$

That is the Cycle-X final-audit frontier.

---

# References

1. R. Yu, *Finite-Window Local-to-Clean Transfer and Anti-Phantom Detection for Sharp Navier--Stokes Packages*, arXiv:2606.18476.
2. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
3. I. Herbst, E. Skibsted, *Analyticity estimates for the Navier--Stokes equations*, arXiv:0907.4351.
4. `NS_TSKR_02_QuadraticTangency_ReproductionRigidity_v0.1.md`.
5. `NS_IDRP_CYCLE_IX_HANDOFF_v1.0.md`.
