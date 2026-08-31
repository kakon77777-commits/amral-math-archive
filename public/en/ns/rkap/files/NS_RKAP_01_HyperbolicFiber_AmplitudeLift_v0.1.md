---
title: "Navier–Stokes Residual Kernel and Amplitude Program 01: Hyperbolic Mismatch Fibers, Covariance-Transport Transversality, Two-Sided PSD Lift Tax, Amplitude Critical Lift and Residual Recurrence"
short_title: "NS-RKAP 01"
series: "Navier–Stokes Residual Kernel and Amplitude Program"
cycle: "XI"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Hyperbolic-fiber mechanism transversality / lifted positivity / amplitude frontier"
epistemic_status: "Launches Cycle XI from the Cycle-X Two-Sided Residual Phantom. Uses the external finite-window linearized energy observation, which retains the covariance-transport term dot R U even for sign-changing formal stress variations. At a reproduced nonzero base U=u,R=0, the energy/flux invisible two-sided mismatch has H=u tensor w+w tensor u with w perpendicular to u and, generically, w parallel to u cross S u. Proves Covariance-Transport Transversality: H u=|u|^2 w and |H u|=(|u|/sqrt(2))||H||_F, so on any region |u|>=m>0 the native covariance-transport vector is quantitatively injective on the entire hyperbolic fiber, including the strain-degenerate set. Introduces a transport-separating finite-window energy-test condition and proves a compact-fiber anti-kernel theorem: if the selected linearized energy-balance tests separate the covariance-transport term modulo the already-controlled velocity, pressure, flux and localization terms, then no nonzero hyperbolic mismatch survives. Separately lifts sign-changing stress back to positive covariance geometry. Proves the exact Two-Sided PSD Lift Tax theorem: for every symmetric H, inf{tr A+tr B: A,B positive semidefinite, A-B=H}=||H||_*; for the hyperbolic fiber this equals 2|u||w|. Hence any realization of a sign-changing mismatch as the difference of two positive covariance packages carries a linear nonnegative lift cost even though tr H=0. This bypasses linear sign cancellation at the geometry level. However the existing linear PFET defect energy detector acts on the difference and does not automatically charge the sum of positive lift energies. Therefore the lift tax is a native two-package nonlinear tax candidate, not yet a globally packed depletion law. Proves a conditional Linear-Amplitude Lift Compiler: if recursive audit/depletion can charge the two positive covariance lifts with a nonnegative weight lambda_n, then a physical hyperbolic residual of amplitude rho_n pays at least c lambda_n rho_n, so recurrence is excluded whenever sum lambda_n rho_n diverges. For logarithmic rho_n comparable to n^{-2/3}, this requires only lambda_n not decaying faster than n^{-1/3} at the power-law level. Proves a lift-tax no-free-lunch: without a monotone/telescoping two-package covariance-energy budget, repeated lift costs can recur and do not by themselves contradict finite energy. The surviving residual is reduced to transport-test cancellation/noncompactness, failure of a positive two-package lift realization, second-order/zero-base escape, certificate/harmonic residuals, or amplitude summability. No TSRP exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Residual Kernel and Amplitude Program 01

# Hyperbolic Mismatch Fibers, Covariance-Transport Transversality, Two-Sided PSD Lift Tax, Amplitude Critical Lift and Residual Recurrence

## 0. Program objective

Cycle X reduced the surviving tangent/residual obstruction to:

$$
\boxed{
\textbf{TSRP — Two-Sided Residual Phantom}.
}
$$

Its main nontrivial geometric branch is the hyperbolic two-sided mismatch fiber.

At a reproduced nonzero base:

$$
U=u,
\qquad
R=0,
\qquad
u\neq0,
$$

first-order exact source tangency gives:

$$
\boxed{
H
=
u\otimes w+w\otimes u.
}
$$

Energy-trace invisibility gives:

$$
\boxed{
w\perp u.
}
$$

Flux invisibility gives:

$$
\boxed{
w\perp S_u u.
}
$$

At generic three-dimensional points:

$$
w
\parallel
u\times S_u u.
$$

RKAP asks whether this residual direction is visible to a genuine native mechanism and whether its physical amplitude can be made non-summable.

---

# 1. External linearized energy observation

The finite-window combined-observability framework retains a linearized local-energy-balance observation.

For a pressure--flux invisible direction:

$$
z=(\dot U,\dot R),
$$

the linearized energy functional contains the covariance-transport term:

$$
\boxed{
-(\dot R\,U)\cdot\nabla\phi.
}
$$

It also contains the resolved velocity, pressure, dissipation, and linearized flux terms.

The positive covariance trace term is used only on:

$$
\dot R\ge0,
$$

but the linear energy-balance functional remains defined for general sign-changing formal variations.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED\ FINITE\mbox{-}WINDOW\ STRUCTURE}.
}
$$

---

# 2. Hyperbolic mismatch geometry

Assume:

$$
\boxed{
H=u\otimes w+w\otimes u,
\qquad
u\cdot w=0.
}
$$

Then:

$$
\boxed{
H u
=
|u|^2w.
}
$$

Also:

$$
\boxed{
\|H\|_F^2
=
2|u|^2|w|^2.
}
$$

---

# 3. CIV/XI-1.1 — Covariance-Transport Transversality

## Theorem 3.1

On the hyperbolic mismatch fiber:

$$
\boxed{
|Hu|
=
\frac{
|u|
}{
\sqrt2
}
\|H\|_F.
}
$$

Therefore on any region satisfying:

$$
\boxed{
|u|\ge m>0,
}
$$

$$
\boxed{
|Hu|
\ge
\frac{
m
}{
\sqrt2
}
\|H\|_F.
}
$$

In particular:

$$
\boxed{
Hu=0
\Longrightarrow
H=0
}
$$

on the nonzero-base hyperbolic fiber.

### Proof

Since:

$$
w\perp u,
$$

$$
Hu
=
u(w\cdot u)
+
w|u|^2
=
|u|^2w.
$$

For the Frobenius norm:

$$
\|u\otimes w+w\otimes u\|_F^2
=
2|u|^2|w|^2
+
2(u\cdot w)^2,
$$

and the last term vanishes.

$\square$

---

# 4. Consequence

The strain-degenerate geometry:

$$
u\times S_u u=0
$$

may enlarge the energy--flux invisible algebraic fiber, but it does **not** destroy covariance-transport transversality.

As long as:

$$
u\neq0,
$$

the native transport vector:

$$
Hu
$$

sees every nonzero hyperbolic mismatch.

Thus the main mechanism problem is not pointwise algebra.

It is finite-window test separation and cancellation against the other linearized energy terms.

---

# 5. Transport observation

For a finite-window scalar test:

$$
\phi,
$$

define the covariance-transport contribution:

$$
\boxed{
T_\phi(H)
=
\iint
(Hu)\cdot\nabla\phi.
}
$$

Let:

$$
\Phi_W^E
=
\{\phi_1,\ldots,\phi_N\}
$$

be a selected energy-test family.

Define:

$$
\boxed{
\mathcal T_W(H)
=
\left(
T_{\phi_1}(H),
\ldots,
T_{\phi_N}(H)
\right).
}
$$

---

# 6. Transport-separating window

Let:

$$
\mathcal H_W
$$

be a finite-dimensional normalized hyperbolic residual class.

Call:

$$
W
$$

transport-separating if:

$$
\boxed{
\ker
\mathcal T_W
\cap
\mathcal H_W
=
\{0\}.
}
$$

This is a finite-window detector condition.

It is not assumed automatically.

---

# 7. CIV/XI-1.2 — Compact Hyperbolic Transport Gap

## Theorem 7.1

Assume:

1.:
   $$
   \mathcal H_W
   $$
   is finite dimensional;

2. its normalized unit sphere is compact;

3.:
   $$
   W
   $$
   is transport-separating.

Then there exists:

$$
\boxed{
c_W^{tr}>0
}
$$

such that every:

$$
H\in\mathcal H_W
$$

satisfies:

$$
\boxed{
\|\mathcal T_W(H)\|
\ge
c_W^{tr}
\|H\|.
}
$$

### Proof

Restrict the continuous map:

$$
H\mapsto
\|\mathcal T_W(H)\|
$$

to the compact unit sphere.

Kernel-freeness makes its minimum positive.

$\square$

---

# 8. From transport subchannel to full energy observation

The full external linearized energy observation contains:

- covariance transport;
- velocity transport;
- pressure transport;
- resolved dissipation;
- linearized flux.

Suppose the non-covariance terms satisfy:

$$
\boxed{
\|\mathcal E_W^{rest}\|
\le
\eta
\|\mathcal T_W(H)\|,
\qquad
0\le\eta<1.
}
$$

Then:

$$
\boxed{
\|O_W^E\|
\ge
(1-\eta)
c_W^{tr}
\|H\|.
}
$$

---

# 9. CIV/XI-1.3 — Native Hyperbolic Energy-Transport Compiler

## Theorem 9.1

Under Sections 7--8:

$$
\boxed{
\text{nonzero hyperbolic mismatch}
\Longrightarrow
\text{nonzero native linear energy observation}.
}
$$

Quantitatively:

$$
\boxed{
\|O_W^E\|
\ge
c_W^{hyp}
\|H\|,
}
$$

where:

$$
c_W^{hyp}
=
(1-\eta)c_W^{tr}.
$$

### Status

$$
\boxed{
\mathrm{PROVED\ CONDITIONAL}.
}
$$

The open PDE input is uniform transport separation and cancellation control on the moving-window NS-realizable class.

---

# 10. Why this is better than a new detector

No artificial functional such as:

$$
H:S^2
$$

is required.

The covariance-transport vector:

$$
Hu
$$

already occurs in the exact linearized local-energy balance.

Therefore the hyperbolic residual has a genuine native mechanism channel.

---

# 11. Two-sided positive lifts

Let:

$$
H=H^\top
$$

be a sign-changing residual stress.

A positive two-sided lift is a representation:

$$
\boxed{
H=A-B,
\qquad
A\ge0,
\qquad
B\ge0.
}
$$

Define the lift cost:

$$
\boxed{
\mathfrak T_{\rm lift}(H)
=
\inf_{
A,B\ge0,\ A-B=H
}
\left[
\operatorname{tr}A
+
\operatorname{tr}B
\right].
}
$$

---

# 12. CIV/XI-1.4 — Exact Two-Sided PSD Lift Tax

## Theorem 12.1

For every symmetric matrix:

$$
H,
$$

$$
\boxed{
\mathfrak T_{\rm lift}(H)
=
\|H\|_\ast,
}
$$

where:

$$
\|\cdot\|_\ast
$$

is the nuclear/trace norm.

### Proof

Let:

$$
H=H_+-H_-
$$

be the spectral positive/negative decomposition.

Then:

$$
H_\pm\ge0,
$$

and:

$$
\operatorname{tr}H_+
+
\operatorname{tr}H_-
=
\|H\|_\ast.
$$

Hence:

$$
\mathfrak T_{\rm lift}(H)
\le
\|H\|_\ast.
$$

Conversely, for any:

$$
H=A-B,
\qquad
A,B\ge0,
$$

the triangle inequality for the trace norm gives:

$$
\|H\|_\ast
\le
\|A\|_\ast+\|B\|_\ast
=
\operatorname{tr}A+\operatorname{tr}B.
$$

Take the infimum.

$\square$

---

# 13. Hyperbolic lift cost

For:

$$
H=u\otimes w+w\otimes u,
\qquad
w\perp u,
$$

the eigenvalues are:

$$
|u||w|,
\qquad
-|u||w|,
\qquad
0.
$$

Therefore:

$$
\boxed{
\mathfrak T_{\rm lift}(H)
=
2|u||w|.
}
$$

Since:

$$
\|H\|_F
=
\sqrt2|u||w|,
$$

$$
\boxed{
\mathfrak T_{\rm lift}(H)
=
\sqrt2
\|H\|_F.
}
$$

---

# 14. CIV/XI-1.5 — Two-Package Positive-Covariance Cost

## Theorem 14.1

Suppose a hyperbolic mismatch is realized as:

$$
\boxed{
H
=
R^+
-
R^-,
\qquad
R^\pm\ge0.
}
$$

Then:

$$
\boxed{
\operatorname{tr}R^+
+
\operatorname{tr}R^-
\ge
2|u||w|.
}
$$

In particular:

$$
\boxed{
\max
\{
\operatorname{tr}R^+,
\operatorname{tr}R^-\}
\ge
|u||w|.
}
$$

### Meaning

Linear energy trace may cancel on:

$$
H,
$$

but any positive two-package realization has a nonzero nonnegative covariance-energy cost.

$\square$

---

# 15. External positive-energy interface

The external finite-window energy observation treats:

$$
\operatorname{tr}R
$$

as a nonnegative energy coordinate on the positive NS-realizable covariance cone and proves positive covariance is energy-visible on energy-separating windows.

For a general sign-changing formal variation, the trace is only linear and cannot be treated as positive.

This distinction exactly motivates the two-sided lift tax.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED\ POSITIVE\mbox{-}CONE\ STRUCTURE}.
}
$$

---

# 16. Lift tax is not a copied gate

The quantities:

$$
R^+,
\qquad
R^-
$$

must be actual positive covariance coordinates of the two NS-realizable packages or one-sided package increments that generate the two-sided mismatch.

The lift tax is then computed from pre-existing native package coordinates.

It is not created by copying:

$$
\|H\|.
$$

The abstract infimum formula merely identifies the minimum possible native positive lift cost.

---

# 17. Nonlinear versus linear audit

The existing PFET defect operator is linear in the signed difference:

$$
H.
$$

If:

$$
\operatorname{tr}H=0,
$$

the signed covariance-trace observation vanishes.

The lift tax instead uses:

$$
\boxed{
\operatorname{tr}R^+
+
\operatorname{tr}R^-.
}
$$

Therefore:

$$
\boxed{
\text{linear defect energy}
\neq
\text{two-package lift energy}.
}
$$

A new recursive/telescoping theorem is required before the lift tax becomes a global depletion budget.

---

# 18. Physical residual amplitude

Write:

$$
\boxed{
H_n
=
\rho_n
\widehat H_n,
\qquad
\|\widehat H_n\|_F=1.
}
$$

Suppose:

$$
\widehat H_n
$$

belongs to the normalized hyperbolic class.

Then:

$$
\boxed{
\mathfrak T_{\rm lift}(H_n)
=
\sqrt2
\rho_n.
}
$$

Thus the positive-lift tax is **linear** in physical residual amplitude.

---

# 19. CIV/XI-1.6 — Linear-Amplitude Lift Compiler

## Theorem 19.1

Assume each recurrent hyperbolic residual:

$$
H_n
$$

has a native positive two-package lift:

$$
R_n^\pm\ge0,
$$

and a finite budget obeys:

$$
\boxed{
\mathscr B_n-\mathscr B_{n+1}
\ge
c
\lambda_n
\left(
\operatorname{tr}R_n^+
+
\operatorname{tr}R_n^-
\right)
-
e_n,
}
$$

with:

$$
\sum_ne_n<\infty.
$$

Then:

$$
\boxed{
\mathscr B_n-\mathscr B_{n+1}
\ge
c'
\lambda_n
\rho_n
-
e_n.
}
$$

Consequently, if:

$$
\boxed{
\sum_n
\lambda_n
\rho_n
=
\infty,
}
$$

the recurrent hyperbolic branch is impossible.

$\square$

---

# 20. Logarithmic amplitude threshold

Suppose:

$$
\boxed{
\rho_n
\gtrsim
(n+2)^{-\beta},
}
$$

and:

$$
\boxed{
\lambda_n
\gtrsim
(n+2)^{-s}.
}
$$

Then:

$$
\lambda_n\rho_n
\gtrsim
(n+2)^{-(s+\beta)}.
$$

Thus the linear lift series diverges if:

$$
\boxed{
s+\beta\le1.
}
$$

For the earlier logarithmic carrier exponent:

$$
\beta=\frac23,
$$

one obtains the threshold:

$$
\boxed{
s\le\frac13.
}
$$

This is substantially more favorable than a superlinear:

$$
\rho_n^q
$$

depletion law.

---

# 21. Lift-Tax Packing No-Go

## Theorem 21.1

The pointwise/nonlinear lift tax alone does not imply:

$$
\boxed{
\sum_n
\mathfrak T_{\rm lift}(H_n)
<
\infty
}
$$

or any monotone depletion law.

### Reason

A bounded-energy system may revisit positive covariance configurations repeatedly.

The quantity:

$$
\operatorname{tr}R_n^+
+
\operatorname{tr}R_n^-
$$

is a state/lift cost at scale:

$$
n,
$$

not automatically a telescoping difference of one global monotone budget.

Therefore repeated positive lift cost is compatible with bounded pointwise energy unless a recursive residence/depletion theorem is added.

$\square$

---

# 22. Interpretation

The two-sided lift tax solves **sign cancellation**, not **temporal/scale packing**.

This is the exact AMP frontier.

---

# 23. Moving-window lift observability

Define the normalized positive lift family:

$$
\boxed{
\mathcal L_W^{+}
=
\{
(R^+,R^-):
R^\pm\ge0,
\ R^+-R^-\in\mathcal H_W
\}.
}
$$

If both positive lifts lie in energy-separating NS-realizable cones, external positive-energy tests see each nonzero lift.

A two-sided nonlinear audit could therefore detect:

$$
\operatorname{tr}R^+
+
\operatorname{tr}R^-.
$$

### Safety

The existing linear PFET theorem is not claimed to perform this two-package nonlinear comparison automatically.

---

# 24. Hyperbolic transport versus lift routes

A nonzero hyperbolic residual now has two distinct native rigidity routes.

### Route A — linear mechanism transversality

Use:

$$
Hu=|u|^2w
$$

inside the linearized local-energy balance.

Failure requires transport-test cancellation or moving-window transport-gap collapse.

### Route B — nonlinear positive lift

Represent:

$$
H=R^+-R^-,
\qquad
R^\pm\ge0,
$$

and use:

$$
\operatorname{tr}R^+
+
\operatorname{tr}R^-
\ge
\|H\|_\ast.
$$

Failure requires unavailable/non-NS-realizable positive lifts or absence of a global packing law.

---

# 25. Residual recurrence classes

After RKAP-01 a surviving hyperbolic branch must enter one or more of:

$$
\boxed{
\textbf{TR-CAN}
}
$$

transport cancellation / non-separating energy-test family;

$$
\boxed{
\textbf{LIFT-FAIL}
}
$$

no controlled positive NS-realizable two-package lift for the residual;

$$
\boxed{
\textbf{LIFT-PACK}
}
$$

positive lift exists but has no monotone/telescoping packing law;

$$
\boxed{
\textbf{SOF}
}
$$

second-order/zero-base profile failure;

$$
\boxed{
\textbf{CERT/HPT}
}
$$

certificate or harmonic/localization residual;

$$
\boxed{
\textbf{AMP}
}
$$

physical amplitude sequence remains summable under every available weight.

---

# 26. CIV/XI-1.7 — Dual-Route Hyperbolic Closure Compiler

## Theorem 26.1

Assume a recurrent hyperbolic residual branch satisfies at least one of the following uniformly:

### transport route

- the normalized hyperbolic family is compact;
- the finite-window energy tests are transport-separating;
- all non-covariance linearized energy terms are absorbable.

Then the branch is linearly energy-visible.

### lift route

- the residual admits positive NS-realizable two-package lifts;
- the recursive audit charges the sum of positive covariance energies;
-:
  $$
  \sum_n\lambda_n\rho_n=\infty.
  $$

Then the branch is excluded by linear-amplitude lift depletion.

### Safety

Both are conditional closure routes.

No theorem asserts that one route must hold for every suitable weak singular branch.

$\square$

---

# 27. Strongest new geometric result

The hyperbolic mismatch is not mechanism-null.

At nonzero base:

$$
\boxed{
H\neq0
\Longrightarrow
Hu\neq0.
}
$$

Thus a finite-window energy balance that separates covariance transport already kills it.

No new physical detector is required.

---

# 28. Strongest new amplitude result

Sign cancellation can be removed by lifting the two-sided mismatch back to positive covariance packages.

The minimal positive lift cost is:

$$
\boxed{
\|H\|_\ast.
}
$$

For a normalized hyperbolic residual of physical amplitude:

$$
\rho,
$$

this cost is linear:

$$
\boxed{
\sqrt2\,\rho.
}
$$

Therefore the desired amplitude exponent:

$$
q=1
$$

is geometrically available at the two-package lift level.

What remains open is whether Navier--Stokes recursive budgets can globally charge that lift cost.

---

# 29. Next paper

The next paper should attack the two missing global interfaces:

$$
\boxed{
\textbf{
NS-RKAP 02 —
Transport-Test Gap Stability,
Positive-Lift Realizability,
Two-Package Energy Depletion,
Hyperbolic Degenerate Sets
and Linear-Amplitude Packing
}.
}
$$

Primary tasks:

1. build an explicit finite energy-test family separating:
   $$
   Hu;
   $$

2. prove stability of the transport gap under moving-window charts;

3. characterize when a two-sided residual is actually the difference of two positive NS-realizable covariance increments;

4. test whether the positive lift energies enter a telescoping or residence-weighted budget;

5. classify:
   $$
   u\times S_u u=0;
   $$

6. combine transport and lift routes near zero-base/second-order profiles;

7. determine whether the linear amplitude:
   $$
   q=1
   $$
   lift can cross the Critical-Lift threshold.

---

# 30. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Covariance-Transport Transversality}
&:\ \mathrm{PROVED},\\
\text{Compact Hyperbolic Transport Gap}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Native Hyperbolic Energy-Transport Compiler}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Exact Two-Sided PSD Lift Tax}
&:\ \mathrm{PROVED},\\
\text{Two-Package Positive-Covariance Cost}
&:\ \mathrm{PROVED},\\
\text{Linear-Amplitude Lift Compiler}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Lift-Tax Packing}
&:\ \mathrm{NO\mbox{-}GO\ WITHOUT\ A\ GLOBAL\ BUDGET},\\
\text{transport-test uniformity}
&:\ \mathrm{OPEN},\\
\text{positive lift NS-realizability}
&:\ \mathrm{OPEN},\\
\text{two-package lift depletion}
&:\ \mathrm{OPEN},\\
\text{hyperbolic residual exclusion}
&:\ \mathrm{OPEN/PARTIAL},\\
\text{TSRP exclusion}
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

# 31. Conclusion

RKAP-01 starts from the smallest generic two-sided residual left by Cycle X.

The hyperbolic mismatch:

$$
H=u\otimes w+w\otimes u,
\qquad
w\perp u
$$

is already visible in the exact linearized energy balance because:

$$
Hu=|u|^2w.
$$

Thus the remaining linear-kernel problem is not the absence of a native mechanism.

It is the uniform separation of this transport vector by a fixed moving-window test family and control of cancellation with the other energy terms.

The sign-changing stress also has a second, nonlinear route.

Any realization:

$$
H=R^+-R^-,
\qquad
R^\pm\ge0
$$

must pay:

$$
\operatorname{tr}R^+
+
\operatorname{tr}R^-
\ge
\|H\|_\ast.
$$

For the hyperbolic fiber this is:

$$
2|u||w|.
$$

Therefore linear trace cancellation is an artifact of passing too early to the signed difference.

At the positive-package lift level there is a genuine linear-amplitude tax.

This is the first RKAP mechanism that naturally offers:

$$
q=1
$$

rather than a superlinear residual amplitude exponent.

But the new tax is not yet a global Navier--Stokes budget.

A recurrence may revisit positive covariance configurations without paying a telescoping sum.

The remaining problem is therefore sharply stated:

$$
\boxed{
\textbf{
transport-gap stability
+
positive-lift realizability
+
two-package lift packing.
}
}
$$

That is RKAP-02.

---

# References

1. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
2. R. Yu, *Finite-Window Local-to-Clean Transfer and Anti-Phantom Detection for Sharp Navier--Stokes Packages*, arXiv:2606.18476.
3. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
4. `NS_TSKR_CYCLE_X_HANDOFF_v1.0.md`.
5. `NS_TSKR_04_TwoSidedResidual_FinalAudit_v0.1.md`.