---
title: "Navier–Stokes Coercive Synchronization Program 06: Stale-Floor / Model-Cone Synchronization, Preloaded Reservoir Depth and Band-Passed Core Alignment"
short_title: "NS-CSP 06"
series: "Navier–Stokes Coercive Synchronization Program"
cycle: "II"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style model-cone synchronization / core-alignment compression"
epistemic_status: "Uses the exact strain-vorticity perturbative structure of the Navier-Stokes strain equation to prove a model-cone monotonicity principle, a quantitative stale-middle-spike residual-action debt, and a preloaded strain-gradient reservoir alternative. It proves that excessive preload forces ultraviolet Hdot1 depth above the Bradshaw-Grujic lower endpoint. It also proves band-passed pseudolocal equivalence of local strain and vorticity concentration at the same shell, reducing the prior core-alignment defect to shell-index alignment/core dilution rather than Riesz nonlocality. It does NOT exclude the preloaded-reservoir branch, shell-index mismatch, stale-floor separation, or prove Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Coercive Synchronization Program 06

# Stale-Floor / Model-Cone Synchronization, Preloaded Reservoir Depth and Band-Passed Core Alignment

## 0. Positioning of this Paper

CSP-05 reduced the global temporal gap branch to:

$$
\boxed{
\text{bounded parabolic-lag synchronization}
\vee
D_{\rm STALE}.
}
$$

A genuinely stale middle-strain event:

$$
t
$$

has a half-level Besov escape time:

$$
\tau_t
=
\tau
\left(
\frac{B(t)}2
\right),
$$

and its associated frequency recovery packet lies before:

$$
t
$$

by an arbitrarily large number of intrinsic:

$$
B(t)^{-4}
$$

recovery times.

The residual question is:

> What must the true Navier--Stokes strain dynamics do between the old recovery packet and the later middle-strain spike?

This paper answers:

$$
\boxed{
\text{either the solution departs from the globally regular strain--vorticity model cone,}
}
$$

or:

$$
\boxed{
\text{the strain-gradient capacity needed by the later spike was already preloaded at the half-level escape.}
}
$$

The second branch is then converted into a frequency-depth problem.

The paper also revisits the spatial singular-core alignment defect and removes the same-shell Riesz-nonlocality part through band-passed pseudolocality.

---

# 1. Notation

Normalize:

$$
\nu=1.
$$

Let:

$$
S
=
\nabla_{\rm sym}u,
$$

$$
\omega
=
\nabla\times u.
$$

Let:

$$
\lambda_1
\le
\lambda_2
\le
\lambda_3
$$

be the eigenvalues of:

$$
S.
$$

Define:

$$
\boxed{
g(t)
=
\|\lambda_2^+(t)\|_2^2.
}
$$

Define the critical Besov amplitude:

$$
\boxed{
B(t)
=
\|u(t)\|_{\dot B^{-1/2}_{\infty,\infty}}.
}
$$

Let:

$$
E_2
=
\sup_{0<s<T}
\|u(s)\|_2
\le
\|u_0\|_2.
$$

---

# 2. Stale half-level escape data

For a sufficiently high stale event:

$$
t,
$$

set:

$$
\boxed{
b
=
B(t).
}
$$

Let:

$$
\boxed{
\tau_t
=
\tau(b/2)
}
$$

be the continuous half-level escape time from CSP-05.

Then:

$$
\boxed{
B(\tau_t)
=
\frac b2,
}
$$

and:

$$
\boxed{
B(s)
\ge
\frac b2
\qquad
(\tau_t\le s\le t).
}
$$

CSP-05 defines the normalized stale lag:

$$
\boxed{
\mathfrak L(t)
=
b^4
\operatorname{dist}
\left(
t,
I_t^{1/2}
\right).
}
$$

---

# 3. Besov amplitude is bounded by strain enstrophy

For every dyadic block:

$$
u_j,
$$

Bernstein gives:

$$
2^{-j/2}
\|u_j\|_\infty
\le
C
2^j
\|u_j\|_2.
$$

Since:

$$
\|\nabla u\|_2
=
\sqrt2
\|S\|_2,
$$

we obtain:

$$
\boxed{
B(t)
\le
C_B
\|S(t)\|_2.
}
$$

---

# 4. Strain interpolation into the subcritical Hdot1 norm

For divergence-free:

$$
u,
$$

$$
\|S\|_2^2
=
\frac12
\|\nabla u\|_2^2.
$$

Integration by parts gives:

$$
\|\nabla u\|_2^2
\le
\|u\|_2
\|\Delta u\|_2.
$$

The Fourier identity:

$$
\boxed{
\|\Delta u\|_2^2
=
2
\|S\|_{\dot H^1}^2
}
$$

therefore gives:

$$
\boxed{
\|S(t)\|_2^2
\le
\frac{
E_2
}{
\sqrt2
}
\|S(t)\|_{\dot H^1}.
}
$$

Consequently:

$$
\boxed{
g(t)
\le
\frac{
E_2
}{
\sqrt2
}
\|S(t)\|_{\dot H^1}.
}
$$

---

# 5. CII-6.1 — Stale Strain-Gradient Floor

## Theorem 5.1

On:

$$
[\tau_t,t],
$$

one has:

$$
\boxed{
\|S(s)\|_{\dot H^1}
\ge
c
\frac{
b^2
}{
E_2
}.
}
$$

### Proof

CSP-05 gives:

$$
B(s)\ge b/2.
$$

Section 3 gives:

$$
\|S(s)\|_2
\ge
c b.
$$

Section 4 gives:

$$
\|S(s)\|_{\dot H^1}
\ge
c
b^2/E_2.
$$

$\square$

---

# 6. Meaning of the floor

A stale critical-Besov plateau is not merely a:

$$
B^4
$$

action floor.

It forces a persistent subcritical strain-gradient reservoir:

$$
\boxed{
\dot H^1
\text{ strain capacity}
\gtrsim
b^2/E_2.
}
$$

This is the natural state variable for Miller's strain--vorticity model comparison.

---

# 7. The regular strain--vorticity residual

Following Miller define:

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

The full projected Navier--Stokes strain equation can be written as:

$$
\boxed{
\partial_tS
-
\Delta S
-
\frac12
P_{st}
(
\omega\otimes\omega
)
+
\mathcal R_{SV}
=
0.
}
$$

The first three terms form the globally regular strain--vorticity interaction model.

---

# 8. Miller orthogonality

Miller proves the exact identity:

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

This is the key reason the strain--vorticity model dissipates:

$$
\dot H^1
$$

exactly.

---

# 9. CII-6.2 — Exact Full-N-S Hdot1 Model-Cone Balance

## Theorem 9.1

For a smooth Navier--Stokes solution:

$$
\boxed{
\frac12
\frac d{dt}
\|S(t)\|_{\dot H^1}^2
+
\|-\Delta S(t)\|_2^2
=
-
\left\langle
\mathcal R_{SV}(t),
-\Delta S(t)
\right\rangle.
}
$$

### Proof

Take the:

$$
L^2
$$

inner product of the projected strain equation with:

$$
-\Delta S.
$$

The vorticity term vanishes by Miller's orthogonality.

$\square$

---

# 10. Model-cone ratio

Whenever:

$$
\|-\Delta S(t)\|_2>0,
$$

define:

$$
\boxed{
\chi_{SV}(t)
=
\frac{
\|\mathcal R_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}.
}
$$

Set:

$$
\chi_{SV}=0
$$

when both numerator and denominator vanish.

Miller's finite-time blow-up criterion states:

$$
\boxed{
\limsup_{t\uparrow T}
\chi_{SV}(t)
\ge1.
}
$$

---

# 11. CII-6.3 — Regular-Model Cone Monotonicity

## Theorem 11.1

If on an interval:

$$
I
$$

one has:

$$
\boxed{
\chi_{SV}(s)
\le
1-\delta
}
$$

for some:

$$
\delta>0
$$

and almost every:

$$
s\in I,
$$

then:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
+
\delta
\|-\Delta S\|_2^2
\le
0
}
$$

on:

$$
I.
$$

In particular:

$$
\boxed{
\|S(t)\|_{\dot H^1}
}
$$

is nonincreasing on:

$$
I.
$$

### Proof

By Theorem 9.1 and Cauchy--Schwarz:

$$
-\langle
\mathcal R_{SV},
-\Delta S
\rangle
\le
\|\mathcal R_{SV}\|_2
\|-\Delta S\|_2
\le
(1-\delta)
\|-\Delta S\|_2^2.
$$

$\square$

---

# 12. Pointwise model-cone crossing

## Corollary 12.1

If:

$$
\boxed{
\|S(t_2)\|_{\dot H^1}
>
\|S(t_1)\|_{\dot H^1},
}
$$

then there exists:

$$
s\in(t_1,t_2)
$$

such that:

$$
\boxed{
\chi_{SV}(s)\ge1.
}
$$

### Proof

Otherwise continuity gives a uniform:

$$
1-\delta
$$

upper bound on the compact subinterval after a small endpoint trimming, contradicting Theorem 11.1.

$\square$

---

# 13. Miller perturbative action

For:

$$
\alpha=0,
\qquad
p=2,
$$

define:

$$
\boxed{
\mathcal A_{SV}[a,b]
=
\int_a^b
\frac{
\|\mathcal R_{SV}(s)\|_2^2
}{
\|S(s)\|_{\dot H^1}^2
}
ds.
}
$$

Miller's theorem gives:

$$
\boxed{
\|S(b)\|_{\dot H^1}^2
\le
\|S(a)\|_{\dot H^1}^2
\exp
\left(
C_0
\mathcal A_{SV}[a,b]
\right).
}
$$

---

# 14. Stale preload ratio

Define:

$$
\boxed{
\mathfrak P_{SV}(t)
=
\frac{
E_2
\|S(\tau_t)\|_{\dot H^1}
}{
\sqrt2
g(t)
}.
}
$$

This quantity is dimensionless.

---

# 15. CII-6.4 — Stale Middle-Spike Residual Debt

## Theorem 15.1

If:

$$
\boxed{
\mathfrak P_{SV}(t)<1,
}
$$

then:

$$
\boxed{
\mathcal A_{SV}[\tau_t,t]
\ge
\frac{
2
}{
C_0
}
\log
\frac1{
\mathfrak P_{SV}(t)
}.
}
$$

Moreover there exists:

$$
s\in(\tau_t,t)
$$

with:

$$
\boxed{
\chi_{SV}(s)\ge1.
}
$$

### Proof

Section 4 gives:

$$
\|S(t)\|_{\dot H^1}
\ge
\frac{
\sqrt2
g(t)
}{
E_2
}
=
\frac{
\|S(\tau_t)\|_{\dot H^1}
}{
\mathfrak P_{SV}(t)
}.
$$

Insert this lower bound into Miller's exponential estimate:

$$
\frac1{
\mathfrak P_{SV}(t)^2
}
\le
\exp
\left(
C_0
\mathcal A_{SV}[\tau_t,t]
\right).
$$

This proves the action lower bound.

The same inequality implies:

$$
\|S(t)\|_{\dot H^1}
>
\|S(\tau_t)\|_{\dot H^1},
$$

so Corollary 12.1 gives a pointwise model-cone crossing.

$\square$

---

# 16. The preload branch

If:

$$
\boxed{
\mathfrak P_{SV}(t)\ge1,
}
$$

then:

$$
\boxed{
E_2
\|S(\tau_t)\|_{\dot H^1}
\ge
\sqrt2
g(t).
}
$$

Thus the subcritical strain-gradient capacity needed to support the later middle-strain amplitude was already present at the half-level escape.

Call this:

$$
\boxed{
\textbf{PRELOAD}.
}
$$

---

# 17. Stale/model-cone alternative

Every stale middle-strain event therefore satisfies:

$$
\boxed{
\text{MODEL-CONE DEPARTURE}
\vee
\text{PRELOAD}.
}
$$

The first branch pays:

- positive:
  $$
  \mathcal A_{SV}
  $$
  debt;
- a pointwise:
  $$
  \chi_{SV}\ge1
  $$
  crossing.

The second branch shifts the problem backward to the spectral content already present at:

$$
\tau_t.
$$

---

# 18. Preload excess

Define:

$$
\boxed{
\mathfrak Q(t)
=
\frac{
E_2
\|S(\tau_t)\|_{\dot H^1}
}{
b^2
}.
}
$$

Theorem 5.1 already gives:

$$
\boxed{
\mathfrak Q(t)
\ge
c>0.
}
$$

Large:

$$
\mathfrak Q
$$

means the half-level escape contains much more strain-gradient capacity than the minimal amount forced by its Besov level.

---

# 19. Lower-window frequency at the half-level escape

Let:

$$
J_-(t)
=
J_{\rm low}(\tau_t).
$$

Since:

$$
B(\tau_t)=b/2,
$$

Bradshaw--Grujic gives:

$$
\boxed{
2^{J_-(t)}
\asymp
\frac{
b
}{
E_2
}.
}
$$

---

# 20. Low-frequency Hdot1 capacity

For every:

$$
J,
$$

Bernstein/Plancherel gives:

$$
\boxed{
\|P_{\le J}S\|_{\dot H^1}
\le
C
2^{2J}
E_2.
}
$$

Therefore:

$$
\boxed{
\|P_{\le J_-+L}S(\tau_t)\|_{\dot H^1}
\le
C
2^{2L}
\frac{
b^2
}{
E_2
}.
}
$$

---

# 21. CII-6.5 — Preload Depth Theorem

## Theorem 21.1

Fix:

$$
L\ge0.
$$

If:

$$
\boxed{
\mathfrak Q(t)
\ge
2C
2^{2L},
}
$$

then the high-frequency strain-gradient tail satisfies:

$$
\boxed{
\|P_{>J_-(t)+L}S(\tau_t)\|_{\dot H^1}
\ge
\frac{\sqrt3}{2}
\|S(\tau_t)\|_{\dot H^1}.
}
$$

### Proof

Section 20 and the definition of:

$$
\mathfrak Q
$$

give:

$$
\|P_{\le J_-+L}S(\tau_t)\|_{\dot H^1}
\le
\frac12
\|S(\tau_t)\|_{\dot H^1}.
$$

Orthogonality of sharp/smoothly separated Fourier pieces in:

$$
\dot H^1
$$

up to fixed LP constants gives the high-tail lower bound.

$\square$

---

# 22. Preload depth coordinate

Define:

$$
\boxed{
L_{\rm pre}(t)
=
\left[
\frac12
\log_2
\left(
\frac{
\mathfrak Q(t)
}{
2C
}
\right)
\right]_+.
}
$$

Then a fixed fraction of the escape-time:

$$
\dot H^1
$$

reservoir lies above approximately:

$$
\boxed{
J_-(t)+L_{\rm pre}(t).
}
$$

Thus PRELOAD is not an untyped old reservoir.

It has a quantitative ultraviolet depth.

---

# 23. Relation to the moving window

Let:

$$
W_-(t)
=
J_{\rm high}(\tau_t)
-
J_{\rm low}(\tau_t).
$$

If:

$$
L_{\rm pre}(t)
\ll
W_-(t),
$$

the preload depth may remain inside the Bradshaw--Grujic relevant band.

If:

$$
L_{\rm pre}(t)
>
W_-(t)+C,
$$

a fixed portion of the preload lies above the upper window endpoint.

By CSP-04 this is:

$$
\boxed{
\text{deep dissipation-range overshoot}.
}
$$

Therefore PRELOAD is further split into:

$$
\boxed{
\text{window-scale preload}
\vee
\text{dissipation-range preload}.
}
$$

---

# 24. Why PRELOAD is not yet an obstruction

The existence of a large:

$$
\dot H^1
$$

strain reservoir at the half-level escape is not forbidden.

It may encode:

- high-frequency stock;
- shell dispersion;
- spatial fragmentation;
- a coherent concentrated carrier;
- dissipation-range activity.

Thus PRELOAD is a state-placement problem, not a contradiction.

---

# 25. Band-passed strain--vorticity relation

The global strain and vorticity are related by zero-order singular integral operators.

For one dyadic shell, the singularity is removed by band passing.

There exist matrix-valued Schwartz kernels:

$$
K_j,
\qquad
L_j,
$$

with:

$$
K_j(x)
=
2^{3j}K(2^jx),
$$

$$
L_j(x)
=
2^{3j}L(2^jx),
$$

such that:

$$
\boxed{
S_j
=
K_j*\omega_j,
}
$$

and:

$$
\boxed{
\omega_j
=
L_j*S_j.
}
$$

---

# 26. Band-passed pseudolocality

For every:

$$
N<\infty,
$$

there exists:

$$
C_N
$$

such that for every ball:

$$
B_R(x_0)
$$

and every:

$$
A\ge1,
$$

$$
\boxed{
\|\omega_j\|_{L^2(B_R)}
\le
C
\|S_j\|_{
L^2(
B_{R+A2^{-j}}
)
}
+
C_N
A^{-N}
\|S_j\|_2.
}
$$

The reverse estimate also holds:

$$
\boxed{
\|S_j\|_{L^2(B_R)}
\le
C
\|\omega_j\|_{
L^2(
B_{R+A2^{-j}}
)
}
+
C_N
A^{-N}
\|\omega_j\|_2.
}
$$

### Proof sketch

Split the convolution into source points within:

$$
A2^{-j}
$$

of the ball and its complement.

The near piece is bounded by the:

$$
L^1
$$

kernel norm.

The far piece is bounded by the Schwartz tail and Schur's test.

---

# 27. CII-6.6 — Same-Shell Core Alignment Theorem

## Theorem 27.1

Fix:

$$
0<\beta<1.
$$

There exists:

$$
A_\beta<\infty
$$

such that if:

$$
\boxed{
\|\omega_j\|_{L^2(B_R)}
\ge
\beta
\|\omega_j\|_2,
}
$$

then:

$$
\boxed{
\|S_j\|_{
L^2(
B_{R+A_\beta2^{-j}}
)
}
\ge
c\beta
\|S_j\|_2.
}
$$

Conversely, local fixed-fraction strain concentration implies local fixed-fraction vorticity concentration after the same type of wavelength enlargement.

### Proof

Use Section 26 and:

$$
\boxed{
\|\omega_j\|_2
=
\sqrt2
\|S_j\|_2.
}
$$

Choose:

$$
A_\beta
$$

so:

$$
C_NA_\beta^{-N}
$$

is at most a sufficiently small fixed multiple of:

$$
\beta.
$$

Absorb the far-field term.

$\square$

---

# 28. Consequence for the old alignment defect

CSP-02 introduced:

$$
D_{\rm ALIGN}
$$

because global strain/vorticity norm equivalence does not imply local singular-core overlap.

Theorem 27.1 shows:

$$
\boxed{
\text{same-shell strain/vorticity local alignment is automatic after fixed wavelength padding}.
}
$$

Therefore Riesz nonlocality itself is not the residual core-alignment obstruction at one band.

---

# 29. Shell-index alignment defect

Let:

$$
j_{\rm core}(t)
$$

be a shell carrying fixed local Type-I singular-core vorticity fraction.

Let:

$$
j_{\rm car}(t)
$$

be a CSP global middle/frequency carrier shell.

Define:

$$
\boxed{
D_{\rm INDEX}
}
$$

as the branch where:

$$
\boxed{
|j_{\rm core}(t)-j_{\rm car}(t)|
}
$$

cannot be bounded by a fixed constant on the relevant action-carrying times.

The old:

$$
D_{\rm ALIGN}
$$

is therefore reduced to shell-index alignment plus possible global/local dilution.

---

# 30. Fixed-index alignment closes local S/omega mismatch

If:

$$
\boxed{
|j_{\rm core}-j_{\rm car}|
\le
C_0,
}
$$

then finite LP padding lets us place both fields in a common:

$$
O(1)
$$

frequency cluster.

Theorem 27.1 then transfers fixed local core concentration between:

$$
S
$$

and:

$$
\omega
$$

up to a fixed number of wavelengths.

Hence:

$$
\boxed{
\text{bounded shell-index mismatch}
}
$$

is not an independent spatial obstruction.

---

# 31. Large index mismatch and spectral dispersion

If:

$$
|j_{\rm core}-j_{\rm car}|
\to\infty
$$

and both shells carry fixed **global** state fractions,

CSP-03's two-cluster theorem forces:

$$
\boxed{
D_{\rm eig}(S)
}
$$

to be quantitatively non-small.

Thus large index mismatch can avoid eigen-residual synchronization only if the local core shell has vanishing global share or the global carrier has vanishing local-core share.

---

# 32. Core dilution

Define the global fraction of a core shell:

$$
\boxed{
\beta_{\rm glob}(t)
=
\frac{
\|\omega_{j_{\rm core}}(t)\|_2^2
}{
\|\omega(t)\|_2^2
}
}
$$

when the denominator is nonzero.

If:

$$
\beta_{\rm glob}\to0
$$

while the shell maintains fixed absolute local singular-core mass,

call this:

$$
\boxed{
D_{\rm DILUTE}.
}
$$

It represents:

> an intense local core carrier that is globally diluted by much larger enstrophy elsewhere.

This is a global/local multiplicity defect rather than a Riesz-alignment defect.

---

# 33. Updated core-alignment decomposition

The old:

$$
D_{\rm ALIGN}
$$

is therefore replaced by:

$$
\boxed{
D_{\rm INDEX}
\vee
D_{\rm DILUTE}.
}
$$

When index separation is large and both global shares stay nontrivial, it is absorbed by:

$$
D_{\rm eig}
$$

synchronization.

Thus the genuinely new local/global escape is narrowed to:

$$
\boxed{
\text{core dilution or shell-index mismatch without simultaneous global state shares}.
}
$$

---

# 34. Stale-floor plus Type-I core

In the Type-I architecture, suppose a stale event:

$$
t
$$

also has a singular-core shell:

$$
j_{\rm core}(t).
$$

The complete current alternatives are:

1. model-cone departure before the spike;
2. PRELOAD at:
   $$
   \tau_t;
   $$
3. shell-index mismatch;
4. core dilution;
5. super-parabolic micro-packing from CSP-02.

This is a much smaller state/geometry frontier than the original:

$$
D_{\rm STALE}
+
D_{\rm ALIGN}
+
D_{\rm SHALIGN}.
$$

---

# 35. Model-cone alignment interpretation

Miller's results distinguish two nonlinear directions.

The regular-model residual:

$$
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
\right)
$$

must be sufficiently large along any finite-time blow-up.

By contrast, the strain self-amplification comparison uses:

$$
\boxed{
\mathcal R_{SSA}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14
\omega\otimes\omega
\right),
}
$$

for which Miller has a conditional finite-time blow-up theorem under additional initial/data inequalities.

Therefore:

$$
\boxed{
\text{departure from the regular model}
}
$$

is necessary,

but:

$$
\boxed{
\text{approach to the SSA cone}
}
$$

is a stronger, differently conditioned statement.

They must not be conflated.

---

# 36. What CSP-06 actually synchronizes

For a stale event that is not PRELOAD:

$$
\boxed{
\text{old Besov recovery packet}
\longrightarrow
\text{model-cone departure}
\longrightarrow
\text{later middle-strain spike}.
}
$$

The first arrow is temporal ordering from CSP-05.

The second is the new model-cone crossing/action debt from Theorem 15.1.

This produces the first three-stage coercive ordering in Cycle II.

---

# 37. The residual PRELOAD geometry

PRELOAD means:

$$
\boxed{
\text{the later middle spike does not require net Hdot1 growth after the half-level escape}.
}
$$

The only remaining freedom is how the already-large:

$$
\dot H^1
$$

reservoir is organized:

- within the relevant window;
- above it in the dissipation range;
- spectrally dispersed;
- spatially fragmented;
- core diluted.

This is now a placement problem, not an unexplained temporal growth problem.

---

# 38. Stale/model-cone synchronization alternative

## Theorem 38.1

Every sufficiently high stale middle-strain event lies in at least one of:

### MC

$$
\boxed{
\mathcal A_{SV}[\tau_t,t]
\ge
\frac2{C_0}
\log
\frac1{
\mathfrak P_{SV}(t)
}
>0,
}
$$

with a pointwise:

$$
\chi_{SV}\ge1
$$

crossing;

### PRELOAD-W

preloaded:

$$
\dot H^1
$$

reservoir at:

$$
\tau_t
$$

whose dominant depth remains within the moving relevant window;

### PRELOAD-D

preloaded reservoir reaching beyond the upper window into the dissipation-range overshoot;

### GEOM

one of the already isolated spectral/spatial/local-global defects:

$$
D_{\rm eig},
\quad
D_{\rm INDEX},
\quad
D_{\rm DILUTE},
\quad
D_{I,\rm micro}.
$$

### Status

This is a structural enclosure assembled from the proved theorems of CSP-02--06.

It is not a finite obstruction theorem.

$\square$

---

# 39. New guards

Add:

### $G_{\rm H1FLOOR}$

A stale critical-Besov floor must preserve the induced:

$$
\dot H^1
$$

strain-gradient floor.

### $G_{\rm SVCONE}$

Growth of:

$$
\|S\|_{\dot H^1}
$$

cannot occur entirely inside:

$$
\chi_{SV}<1.
$$

### $G_{\rm PRELOAD}$

A later middle spike without model-cone departure must preserve the escape-time preloaded strain-gradient reservoir.

### $G_{\rm PREDEPTH}$

Excess preload must preserve its depth relative to:

$$
J_{\rm low}(\tau_t).
$$

### $G_{\rm BANDALIGN}$

At one fixed dyadic band, local strain/vorticity concentration is pseudolocally equivalent after fixed wavelength padding.

### $G_{\rm INDEX}$

Local singular-core alignment problems must distinguish shell-index mismatch from same-shell Riesz nonlocality.

### $G_{\rm DILUTE}$

A locally intense core shell with vanishing global share is a dilution/multiplicity defect, not an alignment failure.

---

# 40. Cycle-II frontier update

Before CSP-06 the principal residuals were:

$$
D_{\rm STALE},
\quad
D_{\rm ALIGN},
\quad
D_{\rm SHALIGN},
\quad
D_{\rm SRCSTATE},
\quad
D_{I,\rm micro}.
$$

After CSP-06:

$$
D_{\rm STALE}
$$

is reduced to:

$$
\boxed{
\text{model-cone departure}
\vee
\text{PRELOAD}.
}
$$

Same-shell local:

$$
S/\omega
$$

alignment is removed.

The residual alignment defects become:

$$
\boxed{
D_{\rm INDEX}
\vee
D_{\rm DILUTE}.
}
$$

Large fixed-share index separation is absorbed by the CSP-03 eigen-residual synchronization.

The remaining core program is therefore concentrated on:

$$
\boxed{
\text{PRELOAD placement}
+
D_{\rm INDEX}
+
D_{\rm DILUTE}
+
D_{\rm SRCSTATE}
+
D_{I,\rm micro}.
}
$$

---

# 41. Next paper

The next paper should attack the preloaded reservoir itself.

$$
\boxed{
\textbf{
NS-CSP 07 —
Preloaded Reservoir Transport,
Dissipation-Range Residence,
Core Dilution
and Source--State Synchronization
}.
}
$$

Main tasks:

1. determine whether preloaded:
   $$
   \dot H^1
   $$
   stock can remain stale for many recovery times without large:
   $$
   \mathcal A_{SV};
   $$
2. study dissipation-range residence of PRELOAD-D;
3. quantify how:
   $$
   D_{\rm DILUTE}
   $$
   interacts with Type-I singular-core concentration;
4. connect source ledgers to simultaneous state occupancy:
   $$
   D_{\rm SRCSTATE};
   $$
5. decide whether super-parabolic micro-packing can serve as the only remaining carrier of preloaded capacity.

---

# 42. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Besov-to-strain enstrophy bound}
&:\ \mathrm{PROVED},\\
\text{strain interpolation to Hdot1}
&:\ \mathrm{PROVED},\\
\text{stale strain-gradient floor}
&:\ \mathrm{PROVED},\\
\text{exact Hdot1 model-cone balance}
&:\ \mathrm{PROVED/EXTERNALLY\ CALIBRATED},\\
\text{regular-model cone monotonicity}
&:\ \mathrm{PROVED},\\
\text{stale middle-spike residual debt}
&:\ \mathrm{PROVED},\\
\text{pointwise model-cone crossing}
&:\ \mathrm{PROVED},\\
\text{preload depth theorem}
&:\ \mathrm{PROVED},\\
\text{band-passed S/omega pseudolocality}
&:\ \mathrm{PROVED},\\
\text{same-shell core alignment}
&:\ \mathrm{PROVED},\\
\text{large index mismatch/eigen-residual bridge}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{PRELOAD exclusion}
&:\ \mathrm{OPEN},\\
\text{shell-index alignment}
&:\ \mathrm{OPEN},\\
\text{core dilution exclusion}
&:\ \mathrm{OPEN},\\
\text{source/state synchronization}
&:\ \mathrm{OPEN},\\
\text{Coercive Synchronization Problem}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 43. Conclusion

CSP-06 gives the first direct bridge from stale temporal separation to true strain-model geometry.

For a stale middle-strain event:

$$
t,
$$

compare the later middle amplitude:

$$
g(t)
$$

to the strain-gradient reservoir already present at the half-level escape:

$$
\tau_t.
$$

If:

$$
\mathfrak P_{SV}(t)<1,
$$

then Miller's perturbative estimate forces:

$$
\boxed{
\mathcal A_{SV}[\tau_t,t]
\gtrsim
\log
\frac1{
\mathfrak P_{SV}(t)
},
}
$$

and the interval contains a point where:

$$
\boxed{
\frac{
\|\mathcal R_{SV}\|_2
}{
\|-\Delta S\|_2
}
\ge1.
}
$$

Thus the later spike cannot be produced while remaining inside the globally regular strain--vorticity model cone.

If this does not happen, the required:

$$
\dot H^1
$$

capacity was already preloaded at:

$$
\tau_t.
$$

Excess preload necessarily moves into ultraviolet depth above the Bradshaw--Grujic lower endpoint, and sufficiently deep preload becomes dissipation-range overshoot.

At the same time, the old local strain/vorticity alignment defect is reduced:

$$
\boxed{
\text{same shell}
+
\text{fixed local fraction}
\Longrightarrow
\text{local }S/\omega\text{ alignment after fixed wavelength padding}.
}
$$

The remaining alignment difficulty is shell-index selection or global/core dilution, not Riesz nonlocality itself.

The Cycle-II frontier is therefore now centered on the dynamics of a preloaded ultraviolet reservoir.

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691v2.
2. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, Archive for Rational Mechanics and Analysis 235 (2020), 99–139; arXiv:1710.05569.
3. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717–792; arXiv:2003.06717.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
5. `NS_CSP_02_SpatialAtom_TypeI_CoreExtraction_ParabolicPacking_v0.1.md`.
6. `NS_CSP_03_ShellAtom_SpectralVariance_ResonantTransfer_v0.1.md`.
7. `NS_CSP_04_MovingWindow_DissipationWavenumber_EscapeIntervals_v0.1.md`.
8. `NS_CSP_05_EscapeTime_TemporalGap_Rigidity_v0.1.md`.