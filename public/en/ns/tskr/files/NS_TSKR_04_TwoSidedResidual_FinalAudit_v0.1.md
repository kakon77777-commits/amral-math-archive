---
title: "Navier–Stokes Tangent Singular Kernel Rigidity Program 04: Two-Sided Mismatch Stress, Second-Order Zero-Base Recovery, Harmonic-Pressure Tail Rigidity, Adjoint Compatibility, Amplitude Tax and Cycle-X Closure Audit"
short_title: "NS-TSKR 04"
series: "Navier–Stokes Tangent Singular Kernel Rigidity Program"
cycle: "X"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Cycle-X final audit / hyperbolic mismatch fiber / second-order recovery / harmonic-tail routing"
epistemic_status: "Closes Cycle X as a tangent/residual-kernel rigidity cycle without excluding the final residual phantom. Linearizes the exact quadratic tangent constraint at a reproduced zero-covariance nonzero base and proves that energy-invisible two-sided mismatch stress has the special trace-free hyperbolic form H=u tensor w+w tensor u with w perpendicular to u; its nonzero eigenvalues are exactly plus-or-minus |u||w|. Flux invisibility further forces w perpendicular to S u, so at generic 3D points where u and S u are linearly independent the entire two-sided mismatch kernel is at most the one-dimensional line w parallel to u cross S u. Thus the former arbitrary sign-changing stress sector collapses to a hyperbolic mismatch fiber before pressure/trace/model-cone/increment tests are applied. Proves that zero-base quadratic degeneracy is only a first-order failure: under the natural second-order blow-up u_epsilon=epsilon a+o(epsilon), U_epsilon=epsilon b+o(epsilon), R_epsilon=epsilon^2 H+o(epsilon^2), exact tangent geometry re-enters the rank-one attenuation theorem a tensor a=b tensor b+H, H>=0. Second-order covariance-energy invisibility then forces H=0 and b=plus-or-minus a, with canonical covariance/trace anchoring selecting the plus branch. Proves an interior harmonic-pressure tail estimate: a fixed nonzero harmonic pressure gradient on an inner ball requires a quantitative outer harmonic-pressure oscillation, routing any nontrivial harmonic-pressure-supported tangent recurrence into the explicit harmonic-tail ledger already retained by finite-window recursive audits. Proves a smooth reduced-generator synchronization compiler: if the linearized coarse-grained generators depend Lipschitz-continuously on the reproduced state, then state reproduction controls causal/audit generator mismatch and hence the adjoint synchronization debt; exact reproduction makes the equation-level adjoints identical. Certificate preservation remains open. Shows that intrinsic residual normalization and one-dimensional hyperbolic-kernel classification do not solve the physical amplitude problem: a decaying two-sided residual still enters any real depletion law with its physical amplitude power. Cycle X therefore reduces TRSK to a Two-Sided Residual Phantom (TSRP): a hyperbolic mismatch line or second-order zero-base fiber, possibly sustained by harmonic-pressure/localization tails or adjoint-certificate failure, whose physical amplitude remains summable. No TSRP exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Tangent Singular Kernel Rigidity Program 04

# Two-Sided Mismatch Stress, Second-Order Zero-Base Recovery, Harmonic-Pressure Tail Rigidity, Adjoint Compatibility, Amplitude Tax and Cycle-X Closure Audit

## 0. Document Positioning

TSKR-03 reduced the surviving Tangent Residual Singular Kernel to:

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

The present paper performs the Cycle-X closure audit.

Its main purpose is to determine which of these are genuine primitive residuals.

---

# 1. Reproduced nonzero base

Consider the exact quadratic tangent constraint:

$$
\boxed{
u\otimes u
-
U\otimes U
-
R
=
0.
}
$$

Linearize at a reproduced zero-covariance base:

$$
\boxed{
U=u,
\qquad
R=0,
\qquad
u\neq0.
}
$$

Let:

$$
a=\dot u,
\qquad
b=\dot U,
\qquad
H=\dot R.
$$

Define:

$$
\boxed{
w=a-b.
}
$$

Then exact first-order tangency gives:

$$
\boxed{
H
=
u\otimes w
+
w\otimes u.
}
$$

---

# 2. Energy-trace invisibility

The covariance trace of:

$$
H
$$

is:

$$
\boxed{
\operatorname{tr}H
=
2u\cdot w.
}
$$

Thus covariance-trace invisibility implies:

$$
\boxed{
u\cdot w=0.
}
$$

---

# 3. CIV/X-4.1 — Hyperbolic Two-Sided Stress Normal Form

## Theorem 3.1

Assume:

$$
u\neq0,
$$

$$
H=u\otimes w+w\otimes u,
$$

and:

$$
\operatorname{tr}H=0.
$$

Then:

$$
w\perp u.
$$

If:

$$
w\neq0,
$$

the eigenvalues of:

$$
H
$$

are exactly:

$$
\boxed{
|u||w|,
\qquad
-|u||w|,
\qquad
0.
}
$$

Hence every nonzero energy-trace-invisible two-sided tangent stress is rank two and sign-indefinite.

### Proof

The orthogonality follows from:

$$
\operatorname{tr}H=2u\cdot w.
$$

On the orthonormal basis:

$$
e_1=u/|u|,
\qquad
e_2=w/|w|,
$$

the restriction of:

$$
H
$$

to:

$$
\operatorname{span}\{u,w\}
$$

has matrix:

$$
\begin{pmatrix}
0 & |u||w|\\
|u||w| & 0
\end{pmatrix}.
$$

The orthogonal complement lies in the kernel.

$\square$

---

# 4. Meaning

The sign-changing residual sector is not an arbitrary symmetric tensor space once the actual quadratic tangent constraint is imposed.

At a reproduced nonzero base and after covariance-energy trace cancellation, it collapses to a hyperbolic shear stress.

---

# 5. Flux linearization

The coarse flux is:

$$
\Pi=-R:S_U.
$$

At:

$$
R=0,
\qquad
U=u,
$$

the first variation is:

$$
\boxed{
\dot\Pi
=
-H:S_u.
}
$$

Since:

$$
S_u
$$

is symmetric:

$$
\boxed{
H:S_u
=
2w\cdot S_u u.
}
$$

---

# 6. CIV/X-4.2 — Energy–Flux Hyperbolic Fiber Reduction

## Theorem 6.1

Assume the hypotheses of Theorem 3.1 and:

$$
\dot\Pi=0.
$$

Then:

$$
\boxed{
w\perp u,
\qquad
w\perp S_u u.
}
$$

If:

$$
u
$$

and:

$$
S_u u
$$

are linearly independent in three dimensions, then:

$$
\boxed{
w
=
\alpha
\,
u\times S_u u
}
$$

for one scalar:

$$
\alpha.
$$

Thus the energy-and-flux-invisible two-sided mismatch fiber is at most one-dimensional at a generic point.

$\square$

---

# 7. Degenerate strain geometry

The one-dimensional conclusion fails when:

$$
S_u u
\parallel u
$$

or:

$$
S_u u=0.
$$

These include:

- strain-eigenvector alignment;
- zero-strain regions;
- constant/shear base geometries.

Define:

$$
\boxed{
\textbf{HDF — Hyperbolic Degenerate Fiber}.
}
$$

HDF is a geometric residual branch, not an automatically invisible branch.

Pressure, trace, LEI, model-cone, and increment tests remain available.

---

# 8. Pressure does not automatically kill the hyperbolic fiber

The active pressure-source observation acts through a differential double-divergence operator.

The algebraic constraints:

$$
w\perp u,
\qquad
w\perp S_u u
$$

do not imply a nonzero active pressure signal.

This is consistent with the pressure-only source-visibility no-go from TSKR-01.

Therefore:

$$
\boxed{
\text{energy+flux reduction}
}
$$

is a geometric compression, not a full PFE kernel exclusion.

---

# 9. External sign-changing stress status

The finite-window combined-observability framework explicitly distinguishes:

- positive NS-realizable covariance directions:
  $$
  \dot R\ge0;
  $$
- general sign-changing formal stress variations.

Positive energy kills the first sector under its energy-separation hypotheses.

The second remains a genuine linear residual sector.

### Status

$$
\boxed{
\mathrm{EXTERNAL/STRUCTURAL}.
}
$$

---

# 10. TSM update

After TSKR-03 and Sections 1--8, a two-sided mismatch stress must satisfy:

$$
\boxed{
H
=
u\otimes w+w\otimes u,
}
$$

with:

$$
\boxed{
w\perp u
}
$$

under covariance-energy invisibility, and:

$$
\boxed{
w\perp S_u u
}
$$

under flux invisibility.

Thus:

$$
\boxed{
\mathrm{TSM}
\to
\textbf{HYPERBOLIC FIBER}
}
$$

before pressure/trace/mechanism constraints are imposed.

---

# 11. Zero-base quadratic degeneracy

At:

$$
u=U=0,
\qquad
R=0,
$$

the first derivative of:

$$
v\mapsto v\otimes v
$$

vanishes.

Thus first-order source tangency contains no velocity information.

This was the ZQD branch.

---

# 12. Natural second-order scaling

Let:

$$
\varepsilon\downarrow0.
$$

Assume:

$$
u_\varepsilon
=
\varepsilon a
+
o(\varepsilon),
$$

$$
U_\varepsilon
=
\varepsilon b
+
o(\varepsilon),
$$

and:

$$
R_\varepsilon
=
\varepsilon^2 H
+
o(\varepsilon^2)
$$

in a topology compatible with multiplication.

Assume:

$$
R_\varepsilon\ge0
$$

and exact quadratic tangency:

$$
u_\varepsilon\otimes u_\varepsilon
=
U_\varepsilon\otimes U_\varepsilon
+
R_\varepsilon.
$$

---

# 13. CIV/X-4.3 — Second-Order Zero-Base Recovery

## Theorem 13.1

Under Section 12:

$$
\boxed{
a\otimes a
=
b\otimes b
+
H,
\qquad
H\ge0.
}
$$

Hence there exists:

$$
\theta\in[-1,1]
$$

such that:

$$
\boxed{
b=\theta a,
}
$$

and:

$$
\boxed{
H
=
(1-\theta^2)
a\otimes a.
}
$$

### Proof

Divide the exact tangent identity by:

$$
\varepsilon^2
$$

and pass to the limit.

Positivity of:

$$
H
$$

is inherited from the one-sided covariance scaling.

Apply Rank-One Attenuation Rigidity from TSKR-02.

$\square$

---

# 14. Second-order energy rigidity

If the second-order covariance-energy trace is invisible:

$$
\boxed{
\operatorname{tr}H=0,
}
$$

then:

$$
\boxed{
H=0,
\qquad
b=\pm a.
}
$$

For a canonical covariance/trace-anchored branch the negative sign is removed, giving:

$$
\boxed{
b=a.
}
$$

Thus ZQD is a failure of first-order coordinates, not a new infinite-dimensional tangent mechanism.

---

# 15. ZQD survivor

The second-order theorem does not apply if:

- no quadratic blow-up limit exists;
- covariance scales at a different rate;
- the residual is two-sided rather than one-sided positive covariance;
- product topology is insufficient;
- physical amplitude disappears before the second-order profile is extracted.

Define the remaining branch:

$$
\boxed{
\textbf{SOF — Second-Order Failure}.
}
$$

---

# 16. Harmonic pressure

Let:

$$
h
$$

be harmonic on:

$$
B_R.
$$

Only functions of time are pressure gauge in the local Navier--Stokes framework.

A spatially harmonic pressure is physical.

Its gradient enters momentum and its pressure work enters local energy.

---

# 17. Interior harmonic estimate

Let:

$$
1\le p<\infty,
$$

and:

$$
0<r<R.
$$

Standard harmonic interior estimates give:

$$
\boxed{
\|\nabla h\|_{L^\infty(B_r)}
\le
C_{p,d}
(R-r)^{-1-d/p}
\|
h-(h)_{B_R}
\|_{L^p(B_R)}.
}
$$

For:

$$
d=3,
$$

the exponent is:

$$
1+3/p.
$$

---

# 18. CIV/X-4.4 — Harmonic-Pressure Tail Visibility

## Theorem 18.1

If:

$$
h
$$

is harmonic on:

$$
B_R\subset\mathbb R^3
$$

and:

$$
\boxed{
\|\nabla h\|_{L^\infty(B_r)}
\ge
a_0>0,
}
$$

then:

$$
\boxed{
\|
h-(h)_{B_R}
\|_{L^p(B_R)}
\ge
c_{p}
a_0
(R-r)^{1+3/p}.
}
$$

### Meaning

A fixed interior harmonic-pressure drive requires a quantitative outer harmonic-pressure oscillation.

$\square$

---

# 19. HPR routing

The external finite-window package explicitly retains:

- harmonic pressure;
- harmonic-tail observations;
- harmonic projection/tail ledger errors.

Therefore:

$$
\boxed{
\text{nontrivial interior HPR drive}
\Longrightarrow
\text{harmonic-tail ledger cost}
}
$$

unless the outer observation geometry itself degenerates.

HPR is no longer a free interior residual.

---

# 20. Dynamic harmonic fixed points

TSKR-03 proved that on a clean projected whole-space/periodic branch, persistent exact rank-one harmonic quadratic tangency collapses to a constant shear.

Combined with Theorem 18.1, a localized nonconstant recurrent harmonic tangent branch must use at least one of:

$$
\boxed{
\text{harmonic-pressure tail},
}
$$

$$
\boxed{
\text{boundary/localization},
}
$$

or:

$$
\boxed{
\text{non-clean reproduction}.
}
$$

---

# 21. Generator synchronization from reproduction

Let:

$$
L[U](t)
$$

be the finite-dimensional linearized coarse-grained Navier--Stokes generator used by the PFET adjoint.

Assume on a bounded smooth reduced class:

$$
\boxed{
\|
L[U_1](t)-L[U_2](t)
\|
\le
C_M
\|
U_1(t)-U_2(t)
\|_{X}
}
$$

for some finite-dimensional/background norm:

$$
X.
$$

Let:

$$
\phi_1,
\phi_2
$$

be backward adjoints with the same terminal datum.

---

# 22. CIV/X-4.5 — Reproduction-to-Adjoint Synchronization Compiler

## Theorem 22.1

Under Section 21:

$$
\boxed{
\|
\phi_1-\phi_2
\|_{L^\infty(I)}
\le
C
e^{CM|I|}
\|\zeta\|
\int_I
\|
U_1-U_2
\|_Xdt.
}
$$

Thus exact state reproduction:

$$
\boxed{
U_1=U_2
}
$$

gives exact equation-level adjoint synchronization.

### Status

$$
\boxed{
\mathrm{PROVED\ CONDITIONAL\ ON\ GENERATOR\ LIPSCHITZNESS}.
}
$$

---

# 23. ASC update

On the positive canonical tangent branch, energy invisibility already gave exact local reproduction.

On smooth/reduced reproduced branches, Theorem 22.1 therefore removes the generator part of ASC.

The remaining ASC issue is:

$$
\boxed{
\textbf{CERT — certificate terminal-data compatibility}.
}
$$

That is, the synchronized PFET adjoint must still preserve the quantitative causal source/ancestry pairing.

This is not supplied by equation synchronization alone.

---

# 24. Two-sided mismatch versus actual covariance

An actual covariance branch obeys:

$$
R_n\ge0.
$$

After intrinsic normalization, every weak limit remains in the PSD cone.

Relative covariance-energy invisibility kills its normalized amplitude.

Therefore the hyperbolic stress of Theorem 3.1 cannot be an actual positive covariance limit.

It is necessarily:

- a difference of two packages;
- a quotient mismatch;
- a centered tangent at a nontrivial base;
- or another two-sided residual coordinate.

This distinction is essential.

---

# 25. Formal PFE residual warning

A two-sided hyperbolic stress can satisfy several low-order cancellation constraints simultaneously.

The positive-energy anti-kernel theorem does not apply because:

$$
H
$$

is sign-indefinite.

Therefore no conclusion of the form:

$$
\boxed{
\text{PFE invisible}
\Longrightarrow
H=0
}
$$

is available without an additional sign-changing-kernel theorem.

This is the remaining SKER-RIG obligation.

---

# 26. Mechanism intersection

A surviving hyperbolic mismatch fiber must also avoid:

- LEI slack;
- strain model-cone excess;
- critical increment defect;
- selected trace response;
- localization/harmonic tail.

If any one of these has a fixed positive lower bound relative to residual amplitude, the fiber is mechanism-visible.

Thus the fully invisible hyperbolic residual belongs to the intersection:

$$
\boxed{
\mathcal K_{\rm hyp}
=
\mathcal K_{\rm PFE}
\cap
\mathcal K_{\rm trace}
\cap
\mathcal K_{\rm LEI}
\cap
\mathcal K_{\rm SV}
\cap
\mathcal K_{\rm inc}
}
$$

modulo retained harmonic/localization residual coordinates.

### Status

$$
\boxed{
\mathrm{DEFINED/OPEN}.
}
$$

---

# 27. Generic-line transversality observation

At a generic point where:

$$
u\times S_u u\neq0,
$$

the energy-flux invisible tangent fiber is one-dimensional.

Therefore any additional linearized detector functional:

$$
\Lambda_{\rm det}(w)
$$

which does not vanish on:

$$
u\times S_u u
$$

kills the pointwise fiber.

### Meaning

After quadratic, energy, and flux rigidity, the remaining sign-changing kernel is susceptible to a single transverse detector.

### Safety

No theorem is claimed that one existing PFET/model-cone/increment functional is uniformly transverse at every NS-realizable point.

---

# 28. Physical amplitude

Let a native two-sided residual be:

$$
d_n
=
\rho_n
\widehat d_n,
\qquad
\|\widehat d_n\|=1.
$$

Kernel classification concerns:

$$
\widehat d_n.
$$

Any physical linear observation satisfies:

$$
\mathcal O(d_n)
=
\rho_n
\mathcal O(\widehat d_n).
$$

Any physical:

$$
q
$$

-power depletion law retains:

$$
\boxed{
\rho_n^q.
}
$$

Thus making:

$$
\mathcal K_{\rm hyp}
$$

one-dimensional does not create a Critical Lift.

---

# 29. CIV/X-4.6 — Residual-Direction/Amplitude Separation

## Theorem 29.1

Suppose normalized residual directions:

$$
\widehat d_n
$$

belong to a compact kernel class and are uniformly observed:

$$
\boxed{
\|\mathcal O_n(\widehat d_n)\|
\ge
c_0>0.
}
$$

Then the physical observation is only:

$$
\boxed{
\|\mathcal O_n(d_n)\|
\ge
c_0\rho_n.
}
$$

Therefore a depletion law:

$$
\Delta\mathscr B_n
\gtrsim
\lambda_n
\|\mathcal O_n(d_n)\|^q
$$

closes recurrence only if:

$$
\boxed{
\sum_n
\lambda_n
\rho_n^q
=
\infty.
}
$$

### Meaning

Kernel rigidity and amplitude Critical Lift are mathematically separate.

$\square$

---

# 30. Cycle-X residual classes

After TSKR-01--04, the previous classes update as follows.

### LHF

High-frequency localized tangency is paid by mismatch/localization.

The exact local harmonic branch is classified to fixed-direction shear.

### HPR

Nontrivial harmonic-pressure drive pays harmonic-tail oscillation.

### ZQD

First-order zero-base degeneracy is reprofiled at second order when a quadratic blow-up exists.

### TSM

Two-sided sign-changing stress is reduced to a hyperbolic mismatch fiber, generically one-dimensional after energy and flux cancellation.

### ASC

Generator synchronization is controlled by state reproduction; certificate anchoring remains open.

### AMP

Unchanged as the physical amplitude Critical-Lift problem.

---

# 31. Two-Sided Residual Phantom

Define:

$$
\boxed{
\textbf{
TSRP —
Two-Sided Residual Phantom
}
}
$$

as a recurrent normalized residual package whose nontriviality is supported through one or more of:

### HYP

a hyperbolic two-sided mismatch fiber surviving all additional mechanism detectors;

### SOF

failure of the second-order zero-base profile/one-sided covariance recovery;

### HPT

harmonic-pressure/localization tail support;

### CERT

causal/PFET certificate terminal-data incompatibility despite equation-level synchronization;

### AMP

physical residual amplitudes whose depletion series remains summable.

Cycle X reduces:

$$
\boxed{
\text{TRSK}
\Longrightarrow
\text{TSRP}.
}
$$

---

# 32. CIV/X-4.7 — Conditional TSRP Closure Compiler

## Theorem 32.1

Assume every recurrent residual branch satisfies:

1. the hyperbolic mismatch fiber is uniformly transverse to at least one native pressure/trace/LEI/model-cone/increment detector;
2. every zero-base sequence admits the second-order profile of Section 12 and its canonical sign is trace-anchored;
3. harmonic-pressure/localization tail ledgers are globally summable or absorbed;
4. the causal certificate admits synchronized PFET terminal data;
5. the physical amplitude series:
   $$
   \sum_n\lambda_n\rho_n^q
   $$
   diverges.

Then TSRP recurrence is impossible.

### Safety

All five items are nontrivial global/PDE hypotheses.

$\square$

---

# 33. Why Cycle X does not close

Cycle X eliminates several fake residual freedoms but exposes two irreducible gaps.

First, a two-sided sign-changing mismatch is outside the positive covariance cone and can survive the positive-energy anti-kernel theorem.

Second, even uniform normalized detectability does not make a decaying physical residual expensive enough unless the amplitude-weighted series is non-summable.

Thus:

$$
\boxed{
\text{kernel exclusion}
\neq
\text{physical amplitude exclusion}.
}
$$

---

# 34. Strongest Cycle-X positive result

The actual positive-covariance tangent branch is substantially rigid:

$$
\boxed{
\text{energy-invisible canonical tangent}
\Longrightarrow
\text{exact local reproduction}.
}
$$

Actual covariance cannot become a sign-changing normalized residual.

The remaining sign-changing branch is a two-sided hyperbolic mismatch fiber.

Zero-base degeneracy is recoverable at second order.

Nontrivial harmonic pressure is paid by the harmonic-tail ledger.

---

# 35. Strongest Cycle-X remaining obstruction

The hard residual is:

$$
\boxed{
\textbf{
two-sided + hyperbolic + mechanism-kernel + amplitude-summable.
}
}
$$

This is a much narrower object than the original diffuse/invisible carrier.

---

# 36. Next research program

The remaining problem is now a residual-kernel/amplitude problem rather than a tangent-source problem.

Define:

$$
\boxed{
\textbf{
NS-RKAP —
Navier--Stokes Residual Kernel and Amplitude Program
}
}
$$

The first paper should be:

$$
\boxed{
\textbf{
NS-RKAP 01 —
Hyperbolic Mismatch Fibers,
Mechanism Transversality,
Second-Order Residual Profiles,
Amplitude Critical Lift
and Residual Recurrence
}.
}
$$

Primary tasks:

1. test PFET/trace/model-cone/increment transversality on:
   $$
   w\parallel u\times S_u u;
   $$

2. classify degenerate points:
   $$
   u\times S_u u=0;
   $$

3. build second-order residual profiles when first-order base vanishes;

4. couple harmonic-tail cost to recursive audit weights;

5. prove or disprove certificate anchoring on synchronized adjoints;

6. search for a non-summable amplitude observable stronger than weak source action;

7. decide whether TSRP can exist.

---

# 37. Cycle-X closure theorem

## Theorem 37.1

Relative to the established TSKR/IDRP/DCRP/MORP modules and the cited finite-window structural hypotheses:

$$
\boxed{
\text{TRSK}
\Longrightarrow
\text{TSRP}.
}
$$

Cycle X does **not** prove:

$$
\boxed{
\text{TSRP}=\varnothing.
}
$$

$\square$

---

# 38. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Hyperbolic Two-Sided Stress Normal Form}
&:\ \mathrm{PROVED},\\
\text{Energy--Flux Hyperbolic Fiber Reduction}
&:\ \mathrm{PROVED},\\
\text{Second-Order Zero-Base Recovery}
&:\ \mathrm{PROVED},\\
\text{Harmonic-Pressure Tail Visibility}
&:\ \mathrm{PROVED},\\
\text{Reproduction-to-Adjoint Synchronization}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Residual-Direction/Amplitude Separation}
&:\ \mathrm{PROVED},\\
\text{HPR as free interior mechanism}
&:\ \mathrm{REMOVED/ROUTED},\\
\text{ZQD as permanent first-order obstruction}
&:\ \mathrm{REMOVED/SECOND\mbox{-}ORDER\ ROUTED},\\
\text{two-sided hyperbolic mechanism-kernel exclusion}
&:\ \mathrm{OPEN},\\
\text{certificate anchoring}
&:\ \mathrm{OPEN},\\
\text{physical amplitude Critical Lift}
&:\ \mathrm{OPEN},\\
\text{TSRP exclusion}
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

Cycle X closes by turning the residual tangent problem into a sharply constrained two-sided kernel problem.

At a reproduced nonzero base, exact first-order source tangency forces every sign-changing two-sided covariance mismatch to have the form:

$$
H=u\otimes w+w\otimes u.
$$

Energy-trace invisibility makes:

$$
w\perp u.
$$

The residual stress then has exactly one positive and one negative eigenvalue.

Flux invisibility further makes:

$$
w\perp S_u u.
$$

At a generic three-dimensional point, the entire residual direction is therefore only the line:

$$
w\parallel u\times S_u u.
$$

The former broad sign-changing tensor kernel has collapsed to a hyperbolic fiber.

The zero-base branch is also less dangerous than it first appeared.

Its first derivative vanishes because the quadratic map has a zero derivative at the origin, but the natural second-order blow-up restores the same rank-one attenuation geometry found at nonzero base.

Thus zero-base degeneracy is a profile-order issue unless the second-order profile itself fails.

Harmonic-pressure recurrence is likewise not free.

A fixed interior harmonic drive forces a quantitative outer harmonic-pressure oscillation and therefore re-enters the explicit harmonic-tail ledger retained by finite-window recursive audits.

State reproduction also controls the generator part of adjoint synchronization on smooth reduced classes.

The remaining dual issue is certificate anchoring, not equation mismatch.

What remains genuinely hard is the combination:

$$
\boxed{
\textbf{
two-sided hyperbolic mismatch
+
full mechanism invisibility
+
physical amplitude summability.
}
}
$$

This is TSRP.

Cycle X does not exclude it.

That is the next problem.

---

# References

1. R. Yu, *Finite-Window Local-to-Clean Transfer and Anti-Phantom Detection for Sharp Navier--Stokes Packages*, arXiv:2606.18476.
2. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
3. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
4. R. Yu, *Finite-Window Computational Anti-Phantom Theorems for Scale-Critical Navier--Stokes Defects*, arXiv:2606.15456.
5. `NS_TSKR_03_LocalizedFixedPoints_LinearizedKernel_v0.1.md`.
6. `NS_IDRP_CYCLE_IX_HANDOFF_v1.0.md`.