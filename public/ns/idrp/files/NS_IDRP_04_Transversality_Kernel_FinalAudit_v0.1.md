---
title: "Navier–Stokes Impulsive Defect Recurrence Program 04：Source Transversality、Adjoint Synchronization、Singular Limit Kernels、Physical Burst Amplitude 與 Cycle-IX Closure Audit"
short_title: "NS-IDRP 04"
series: "Navier–Stokes Impulsive Defect Recurrence Program"
cycle: "IX"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Cycle-IX closure audit / transversality no-go / adjoint synchronization / singular-kernel reduction"
epistemic_status: "Closes Cycle IX as a burst-realization and relative-kernel reduction cycle without excluding the final impulsive obstruction. Proves a Pressure-Only Source Visibility No-Go by constructing smooth Fourier-localized symmetric source tensors with zero active-pressure symbol but nonzero Leray-projected forcing; therefore pressure compatibility alone cannot supply universal source transversality. Proves the stronger Universal Forcing-Pairing-to-Source-Defect No-Go: a large causal forcing pairing can occur for a source lying entirely in the chosen clean/model source subspace, so no theorem based solely on forcing-pairing size can imply native source-quotient distance. Establishes an Adjoint Synchronization theorem: two backward finite-window duals with the same terminal datum and nearby linearized generators differ by an explicit Duhamel-Gronwall generator-drift bound; exact synchronization makes the causal and audit duals coincide. Thus the DUAL problem is reduced to whether the ANP causal certificate can be realized with the PFET linearized adjoint or with quantitatively small generator mismatch. Imports the finite-window positive-energy anti-kernel theorem and proves a Positive-Cone Limit-Kernel Reduction: under compact normalized windows and stable positive-cone/energy-separation hypotheses, a nonzero singular PFET limit kernel cannot carry resolved energy, resolved dissipation, or nonnegative Reynolds covariance; it must lie in sign-changing stress, localization/harmonic leakage, or another residual NS-realizability sector. Finally proves a Weak-Source-Action Critical-Lift No-Go by scaling: a scale-critical Navier-Stokes nonlinear forcing burst costs O(r^{4/3}) in L_t^{4/3} H_x^{-1} action over a parabolic scale-r window, so fixed normalized bursts at every geometric scale remain globally summable. Intrinsic residual normalization therefore cannot solve the physical amplitude problem. Cycle IX reduces the surviving obstruction to a tangent/desynchronized/singular-kernel/amplitude-summable impulsive phantom. No universal BDR, Relative Invisible Burst exclusion, Impulsive Diffuse Recurrence exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Impulsive Defect Recurrence Program 04

# Source Transversality、Adjoint Synchronization、Singular Limit Kernels、Physical Burst Amplitude 與 Cycle-IX Closure Audit

## 0. 本文定位

IDRP-03 reduced the remaining impulsive-burst problem to four PDE obligations:

$$
\boxed{
TRAN,
\qquad
DUAL,
\qquad
KERN,
\qquad
AMP.
}
$$

The present paper performs the Cycle-IX closure audit.

The result is not a full closure.

Instead it proves:

1. pressure-only source transversality is impossible in general;
2. forcing-pairing size alone can never imply source-quotient distance without transversality;
3. dual compatibility is exact when the causal and audit adjoints are synchronized, and perturbatively controlled otherwise;
4. positive-covariance/energy directions cannot populate a stable singular PFET limit kernel under the external anti-kernel hypotheses;
5. the universal weak source-action budget is scale-summable and therefore cannot by itself provide the physical Critical Lift.

The final obstruction is a much narrower impulsive phantom.

---

# 1. Pressure-source map and forcing map

On whole-space Fourier variables define the pressure-source map:

$$
\boxed{
\mathcal P_{\rm src}F
=
R_iR_jF_{ij}.
}
$$

Its symbol is, up to sign convention:

$$
\boxed{
\widehat{
\mathcal P_{\rm src}F
}
(\xi)
=
-
\frac{
\xi_i\xi_j
}{
|\xi|^2
}
\widehat F_{ij}(\xi).
}
$$

The projected velocity forcing map is:

$$
\boxed{
\mathcal BF
=
-
\mathbb P
\nabla\cdot F,
}
$$

with symbol:

$$
\boxed{
\widehat{\mathcal BF}(\xi)
=
-i
\mathbb P_\xi
\widehat F(\xi)
\xi.
}
$$

---

# 2. Pressure-invisible forcing-visible polarization

Fix a conic frequency patch avoiding the origin.

Choose a smooth unit vector field:

$$
a(\xi)
$$

on the patch satisfying:

$$
\boxed{
a(\xi)\cdot\xi=0.
}
$$

Let:

$$
\widehat\xi=\xi/|\xi|.
$$

Choose a nonzero smooth compactly supported scalar Fourier amplitude:

$$
\chi(\xi).
$$

Define the symmetric tensor:

$$
\boxed{
\widehat F(\xi)
=
\chi(\xi)
\left[
a(\xi)\otimes\widehat\xi
+
\widehat\xi\otimes a(\xi)
\right].
}
$$

---

# 3. CIV/IX-4.1 — Pressure-Only Source Visibility No-Go

## Theorem 3.1

The tensor of Section 2 satisfies:

$$
\boxed{
\mathcal P_{\rm src}F=0,
}
$$

while:

$$
\boxed{
\mathcal BF\neq0.
}
$$

### Proof

Since:

$$
a\cdot\widehat\xi=0,
$$

$$
\widehat\xi^{\top}
\widehat F
\widehat\xi
=
0.
$$

Hence the pressure-source symbol vanishes.

But:

$$
\widehat F(\xi)\xi
=
|\xi|
\chi(\xi)
a(\xi).
$$

Because:

$$
a(\xi)\perp\xi,
$$

the Leray projector leaves this vector unchanged:

$$
\mathbb P_\xi a=a.
$$

Therefore:

$$
\widehat{\mathcal BF}
=
-i
|\xi|
\chi(\xi)
a(\xi),
$$

which is nonzero.

$\square$

---

# 4. Meaning

Pressure-source observability cannot detect every forcing-relevant source direction.

Thus:

$$
\boxed{
\text{pressure compatibility}
\not\Rightarrow
\text{source transversality}.
}
$$

This matches the external finite-window framework, where pressure-source observability is an additional structural input or must be built into an enhanced quotient/residual geometry.

---

# 5. Clean/model source subspace

Let:

$$
S_{\rm cl}
\subset
X_{\rm src}
$$

be a nontrivial clean/model source subspace.

Let:

$$
\delta_{\rm src}(F)
=
\operatorname{dist}(F,S_{\rm cl}).
$$

Let:

$$
\Phi
$$

be a forcing dual and:

$$
\psi=\mathcal B^\ast\Phi.
$$

---

# 6. CIV/IX-4.2 — Forcing-Pairing-to-Source-Defect No-Go

## Theorem 6.1

No universal lower bound of the form:

$$
\boxed{
\delta_{\rm src}(F)
\ge
c
|
\langle
\mathcal BF,\Phi
\rangle
|
}
$$

with:

$$
c>0
$$

can hold for every:

$$
F
$$

and every forcing dual:

$$
\Phi.
$$

### Proof

Choose:

$$
0\neq F\in S_{\rm cl}
$$

with:

$$
\mathcal BF\neq0.
$$

Choose:

$$
\Phi
$$

so that:

$$
\langle
\mathcal BF,\Phi
\rangle
\neq0.
$$

Then:

$$
\delta_{\rm src}(F)=0,
$$

while the right-hand side is positive.

$\square$

---

# 7. Consequence for TRAN

Source transversality is not a technical convenience.

It is logically necessary for a source-quotient BDR theorem.

The surviving source branch is:

$$
\boxed{
\textbf{TANG — Clean/Model Tangent Burst}.
}
$$

A tangent burst may be dynamically large while producing no native source quotient defect.

It must be tested by state evolution, reproduction, energy/flux/trace, or another native channel.

---

# 8. External source-coordinate status

The finite-window sharp package theory contains:

- active source:
  $$
  F^{act}=\eta u\otimes u;
  $$
- model source:
  $$
  F^{mod}=\eta(U\otimes U+R);
  $$
- active covariance/source mismatch;
- source reproduction drift/leakage;
- pressure-source mismatch.

The literature explicitly states that pressure-source quotient observability is an additional assumption/decision point unless the quotient geometry or residual norm is enhanced.

### Status

$$
\boxed{
\mathrm{EXTERNAL/CONSTRUCTED\ BUT\ NOT\ UNIVERSALLY\ COERCIVE}.
}
$$

---

# 9. Tangent source reproduction

The external active-source reproduction estimate has the schematic form:

$$
\boxed{
\operatorname{Rep}_{F^{act}}
\le
C
M_U
\operatorname{Rep}_{u}
+
C
\operatorname{Leak}^{F}_{rep}.
}
$$

Thus a source burst which remains in the model/tangent source geometry and has small source leakage is coupled to the velocity reproduction dynamics rather than to a source quotient defect.

### Meaning

TANG is naturally a **model-dynamics/reproduction branch**, not a failed source-defect theorem.

---

# 10. Backward duals

Let:

$$
H
$$

be a finite-dimensional Hilbert trace/dual space.

Consider two backward duals:

$$
\phi_C,
\qquad
\phi_A
$$

on:

$$
I=[t_0,t_1].
$$

They solve:

$$
\boxed{
-\partial_t\phi_C
=
L_C(t)^\ast\phi_C,
}
$$

$$
\boxed{
-\partial_t\phi_A
=
L_A(t)^\ast\phi_A,
}
$$

with common terminal datum:

$$
\boxed{
\phi_C(t_1)
=
\phi_A(t_1)
=
\zeta.
}
$$

Assume:

$$
\boxed{
\|L_C(t)\|
+
\|L_A(t)\|
\le
M.
}
$$

---

# 11. Difference equation

Let:

$$
w=\phi_C-\phi_A.
$$

Then:

$$
\boxed{
-\partial_tw
=
L_C^\ast w
+
(L_C^\ast-L_A^\ast)\phi_A,
\qquad
w(t_1)=0.
}
$$

---

# 12. CIV/IX-4.3 — Adjoint Synchronization Theorem

## Theorem 12.1

Under Sections 10--11:

$$
\boxed{
\|w\|_{L^\infty(I;H)}
\le
e^{M|I|}
\|\zeta\|
\int_I
\|L_C(t)-L_A(t)\|dt.
}
$$

Up to harmless constants depending on the norm convention.

### Proof

Backward Duhamel gives:

$$
w(t)
=
\int_t^{t_1}
U_C(t,s)
(L_C^\ast-L_A^\ast)(s)
\phi_A(s)ds.
$$

The evolution bounds give:

$$
\|U_C(t,s)\|
\le
e^{M(s-t)},
$$

and:

$$
\|\phi_A(s)\|
\le
e^{M(t_1-s)}
\|\zeta\|.
$$

Combine.

$\square$

---

# 13. Exact synchronization

If:

$$
\boxed{
L_C(t)=L_A(t)
}
$$

almost everywhere and the terminal data agree, then:

$$
\boxed{
\phi_C=\phi_A.
}
$$

Thus the causal/audit dual mismatch is exactly zero.

---

# 14. Source-side dual synchronization

If:

$$
\mathcal B^\ast:
H\to X_{\rm src}^\ast
$$

is bounded, then:

$$
\boxed{
\|
\mathcal B^\ast\phi_C
-
\mathcal B^\ast\phi_A
\|
\le
\|\mathcal B^\ast\|
e^{M|I|}
\|\zeta\|
\int_I
\|L_C-L_A\|dt.
}
$$

Hence the IDRP-03 dual mismatch is quantitatively paid by generator drift.

---

# 15. External PFET adjoint interpretation

The finite-window PFET trace map is generated by evolving a selected-time correction through the **linearized coarse-grained Navier--Stokes system around the resolved background**.

Its adjoint is the corresponding backward trace dual.

Therefore exact use of the same resolved background and terminal datum provides a canonical synchronized audit dual.

### Status

$$
\boxed{
\mathrm{EXTERNAL\ DEFINITION}
+
\mathrm{INTERNAL\ SYNCHRONIZATION\ THEOREM}.
}
$$

---

# 16. DUAL update

The DUAL problem is reduced to:

> can the causal-source certificate be represented using the synchronized PFET adjoint without losing its quantitative source pairing?

Define:

$$
\boxed{
\textbf{ASC — Adjoint Synchronization Compatibility}.
}
$$

ASC is the remaining PDE/causal theorem.

If ASC holds, DUAL closes.

If not, the surviving branch is:

$$
\boxed{
\textbf{ADJ — Adjoint-Desynchronized Burst}.
}
$$

---

# 17. Combined finite-window kernel

For a finite window:

$$
W,
$$

let the pressure--flux kernel be:

$$
K_W^{PF}.
$$

The external positive-energy theorem proves, under energy separation on the positive NS-realizable pressure--flux cone:

$$
\boxed{
K_{W,\mathrm{NS}}^{PFE,+}
=
\{0\}.
}
$$

Thus no nonzero positive-covariance NS-realizable pressure--flux kernel direction can remain invisible to energy.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED\ UNDER\ ITS\ HYPOTHESES}.
}
$$

---

# 18. Moving normalized windows

Let:

$$
W_n
$$

be moving finite windows transported to one common normalized model.

Let:

$$
d_n
$$

be normalized NS-realizable defect directions and suppose:

$$
d_n\to d_\ast.
$$

Assume the positive NS-realizable cones:

$$
\mathcal C_n^+
$$

converge/are closed in the chart so that:

$$
d_n\in\mathcal C_n^+
\Longrightarrow
d_\ast\in\mathcal C_\ast^+.
$$

Assume the pressure, flux, and energy observation operators converge.

---

# 19. CIV/IX-4.4 — Positive-Cone Limit-Kernel Reduction

## Theorem 19.1

Suppose:

1.:
   $$
   d_n
   $$
   are positive-cone NS-realizable directions;
2. pressure and flux observations tend to zero;
3. positive energy observations tend to zero;
4. the external positive-energy anti-kernel hypotheses remain valid in the limit window.

Then:

$$
\boxed{
d_\ast=0
}
$$

in the cleaned active quotient.

### Proof

The convergences place:

$$
d_\ast
$$

in the positive NS-realizable PFE kernel of the limit window.

The external positive-energy anti-kernel theorem makes that kernel trivial.

$\square$

---

# 20. Consequence for singular PFET limit kernels

A nonzero singular combined limit kernel cannot remain inside the stable positive-covariance/positive-energy cone.

The external framework identifies the remaining possibilities as including:

- sign-changing formal stress variation;
- localization artifact;
- retained harmonic-pressure leakage;
- residual finite-dimensional directions outside the positive covariance cone;
- NS-realizability failures/limit issues.

Thus:

$$
\boxed{
\textbf{KERN}
}
$$

is reduced to a **sign-changing/residual kernel problem**.

---

# 21. Trace channel does not worsen the reduction

A combined PFET limit kernel is already PFE-invisible before trace invisibility is imposed.

Therefore Theorem 19.1 removes its positive-covariance/energy sector before the trace kernel is analyzed.

The surviving trace-singular kernel must lie in the residual PFE sector.

---

# 22. Model-cone/increment augmentation

MORP/DCRP introduced additional mechanism channels:

- strain model-cone equality/excess;
- critical filtered increment defect;
- local-energy slack.

If those channels extend continuously to the normalized limit package, any singular PFET kernel carrying positive value in one of them is not fully mechanism-invisible.

### Status

$$
\boxed{
\mathrm{CONDITIONAL\ AUGMENTATION}.
}
$$

No theorem currently proves that every sign-changing/residual PFET kernel has positive value in one of these mechanism channels.

---

# 23. Navier--Stokes forcing scaling

Under parabolic scaling:

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t),
$$

the nonlinear velocity forcing scales as:

$$
\boxed{
\mathcal N_\lambda(x,t)
=
\lambda^3
\mathcal N(\lambda x,\lambda^2t).
}
$$

For:

$$
\dot H^{-1}
$$

in three dimensions:

$$
\boxed{
\|
\mathcal N_\lambda(t)
\|_{\dot H^{-1}}
=
\lambda^{1/2}
\|
\mathcal N(\lambda^2t)
\|_{\dot H^{-1}}.
}
$$

---

# 24. CIV/IX-4.5 — Weak-Source-Action Scaling

## Theorem 24.1

On one parabolic scale:

$$
r=\lambda^{-1},
$$

$$
\boxed{
\int_0^{r^2}
\|
\mathcal N_r(t)
\|_{\dot H^{-1}}^{4/3}dt
=
r^{4/3}
\int_0^1
\|
\mathcal N(s)
\|_{\dot H^{-1}}^{4/3}ds
}
$$

after the standard normalized change of variables.

### Proof

The norm contributes:

$$
\lambda^{2/3}
$$

after the:

$$
4/3
$$

power, and:

$$
dt=\lambda^{-2}ds.
$$

Thus the total factor is:

$$
\lambda^{-4/3}
=
r^{4/3}.
$$

$\square$

---

# 25. CIV/IX-4.6 — Weak-Source-Action Critical-Lift No-Go

## Theorem 25.1

Let:

$$
r_k=2^{-k}.
$$

Even if every dyadic scale carries one identical normalized source-action burst:

$$
\boxed{
r_k^{-4/3}
\int_{I_k}
\|
\mathcal N
\|_{\dot H^{-1}}^{4/3}dt
\ge
c_0>0,
}
$$

the physical total action cost may remain finite because:

$$
\boxed{
\sum_k
r_k^{4/3}
<
\infty.
}
$$

### Meaning

The universal:

$$
L_t^{4/3}\dot H_x^{-1}
$$

source-action budget cannot by itself exclude a scale-critical burst at every geometric scale.

$\square$

---

# 26. Vorticity-forcing analogue

For:

$$
\mathcal G=-\nabla\times\mathcal N,
$$

the energy-class weak topology:

$$
\dot H^{-2}
$$

has the same parabolic physical action factor:

$$
\boxed{
r^{4/3}
}
$$

at:

$$
L_t^{4/3}.
$$

Thus the same summability no-go applies.

---

# 27. Logarithmic burst amplitude

If the normalized burst amplitude further decays like:

$$
b_k
\sim
k^{-2/3},
$$

a physical weak-source action cost with an additional:

$$
b_k^{4/3}
$$

factor is even more summable:

$$
\boxed{
\sum_k
r_k^{4/3}
b_k^{4/3}
<
\infty.
}
$$

Therefore the DCRP/IDRP logarithmic burst cannot be closed by the universal weak source-action budget alone.

---

# 28. AMP update

The physical amplitude problem is structural, not a normalization artifact.

It requires:

- a near-critical/non-summable depletion weight;
- a stronger burst topology/action;
- a slow-scale schedule with a compatible horizon theorem;
- or a branch-specific persistence/observability theorem.

Thus:

$$
\boxed{
\textbf{AMP}
:
\mathrm{OPEN}.
}
$$

---

# 29. Combined Cycle-IX residual

After the present audit, the surviving impulsive obstruction is compressed to four components.

### TANG

The burst source is tangent to the clean/model source space, so source quotient BDR vanishes.

### ADJ

The causal source dual cannot be synchronized with the PFET finite-window adjoint without losing the source certificate.

### SKER

A sign-changing/localization/harmonic/residual singular combined limit kernel survives all positive-energy and mechanism reductions.

### AMP

The physical residual amplitude/depletion weights remain summable even after relative kernel normalization.

These are not four independent physical mechanisms.

They are the four remaining failure modes of the BDR-to-depletion compiler.

---

# 30. Tangent Singular Impulsive Phantom

Define:

$$
\boxed{
\textbf{
TSIP —
Tangent Singular Impulsive Phantom
}
}
$$

as a recurrent normalized branch satisfying, in the relevant subsequences, one or more of:

1. source tangency:
   $$
   \delta_{\rm src}/J\to0;
   $$

2. adjoint desynchronization:
   $$
   \varepsilon_{\rm dual}/J
   \not\to0;
   $$

3. singular residual kernel:
   a normalized sign-changing/residual PFET limit kernel survives;

4. amplitude summability:
   the physical depletion series remains finite.

Cycle IX reduces the impulsive diffuse obstruction to TSIP.

---

# 31. CIV/IX-4.7 — Cycle-IX Conditional Closure Compiler

## Theorem 31.1

Assume along every recurrent impulsive branch:

1. source bursts are either uniformly transverse to the clean source quotient or tangent bursts are uniformly detected by a complementary native state/trace/mechanism channel;
2. ASC holds, so causal/audit dual mismatch is controlled by a summable synchronization ledger;
3. every normalized combined singular-limit kernel is excluded after intersection with NS-realizability and the mechanism-augmented kernel;
4. the physical amplitude-weighted depletion series is non-summable.

Then recurrent impulsive defects are impossible.

### Safety

All four items remain nontrivial PDE hypotheses.

$\square$

---

# 32. Why Cycle IX does not close

The paper proves that two hoped-for shortcuts fail.

First:

$$
\boxed{
\text{forcing burst size alone}
\not\Rightarrow
\text{native source defect}.
}
$$

Second:

$$
\boxed{
\text{fixed normalized weak source action}
\not\Rightarrow
\text{non-summable physical cost}.
}
$$

The middle operator/adjoint geometry can be controlled conditionally, but the endpoints TRAN and AMP remain genuine.

---

# 33. Strongest positive result

The strongest new positive results are:

$$
\boxed{
\text{source-transverse burst}
\Longrightarrow
\text{native BDR},
}
$$

and:

$$
\boxed{
\text{adjoint synchronization}
\Longrightarrow
\text{dual compatibility}.
}
$$

Moreover a stable positive-covariance singular PFET limit kernel is excluded by the external energy anti-kernel theorem.

---

# 34. Strongest remaining obstruction

The unresolved object is no longer a generic invisible burst.

It is a branch which is simultaneously:

- source-tangent or complementary-channel evasive;
- adjoint-desynchronized or residual-ledger expensive;
- supported in a sign-changing/residual singular limit kernel;
- physically amplitude-summable.

This is TSIP.

---

# 35. Cycle-IX final status

$$
\boxed{
\begin{aligned}
\text{pressure-only source transversality}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{forcing-pairing-only BDR}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{source-transverse BDR}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Adjoint Synchronization}
&:\ \mathrm{PROVED},\\
\text{ASC}
&:\ \mathrm{OPEN},\\
\text{positive-cone limit-kernel sector}
&:\ \mathrm{EXCLUDED\ UNDER\ EXTERNAL\ HYPOTHESES},\\
\text{sign-changing/residual limit kernel}
&:\ \mathrm{OPEN},\\
\text{weak source-action Critical Lift}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{physical amplitude lift}
&:\ \mathrm{OPEN},\\
\text{generic BDR}
&:\ \mathrm{OPEN/PARTIAL},\\
\text{Relative Invisible Burst exclusion}
&:\ \mathrm{OPEN/PARTIAL},\\
\text{Impulsive Diffuse Recurrence exclusion}
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

# 36. Next research program

The remaining problem is now more kernel/geometry-oriented than impulse-oriented.

Define:

$$
\boxed{
\textbf{
NS-TSKR —
Navier--Stokes Tangent Singular Kernel Rigidity Program
}
}
$$

The first paper should be:

$$
\boxed{
\textbf{
NS-TSKR 01 —
Tangent Source Geometry、
Complementary Channel Recovery、
Sign-Changing Stress Kernels、
Adjoint Synchronization Compatibility
與 Residual Rigidity
}.
}
$$

Primary tasks:

1. classify tangent active/model source bursts generated by:
   $$
   u\otimes u
   $$
   and:
   $$
   U\otimes U+R;
   $$

2. determine whether tangent source dynamics necessarily produce state reproduction, flux, energy, or trace visibility;

3. intersect sign-changing PFE/PFET kernels with Reynolds covariance realizability;

4. use local-energy slack, model-cone equality, and increment microstructure channels against singular residual kernels;

5. prove ASC on a canonical synchronized ANP/PFET dual choice or quantify its failure;

6. search for a non-summable amplitude tax once the kernel is rigidified;

7. decide whether TSIP can exist.

---

# 37. Cycle-IX closure theorem

## Theorem 37.1

Cycle IX proves:

$$
\boxed{
\text{Impulsive Diffuse Recurrence}
\Longrightarrow
\text{TSIP}
}
$$

relative to the established IDRP/MORP/DCRP and cited finite-window hypotheses.

Cycle IX does **not** prove:

$$
\boxed{
\text{TSIP}=\varnothing.
}
$$

$\square$

---

# 38. Conclusion

Cycle IX ends by showing exactly why burst visibility and relative normalization do not automatically become a Navier--Stokes regularity proof.

A source burst may be dynamically large yet tangent to the selected clean/model source geometry.

Active pressure cannot universally recover this defect: the pressure-source map has a nontrivial forcing-visible kernel.

Therefore source transversality must be proved or a complementary native channel must see the tangent burst.

The dual mismatch problem is better behaved.

If the causal and audit duals use the same linearized background and terminal datum, they coincide.

If their generators differ, Duhamel--Gronwall explicitly charges the mismatch to the generator drift.

Thus DUAL is reduced to an adjoint synchronization compatibility theorem rather than an abstract semantic gap.

The singular-kernel problem also narrows.

Positive NS-realizable pressure--flux directions carrying resolved energy, dissipation, or positive Reynolds covariance cannot survive the external positive-energy anti-kernel test.

A surviving singular limit must live in a sign-changing/localization/harmonic/residual sector.

Finally, physical amplitude remains a separate barrier.

Scale-critical weak nonlinear-source action costs only:

$$
r^{4/3}
$$

per parabolic geometric scale.

Those costs are summable.

Normalizing a residual makes its direction visible to kernel geometry, but does not make its physical amplitude non-summable.

The surviving object is therefore a tangent, singular, amplitude-summable impulsive phantom.

That is the next rigidity target.

---

# References

1. R. Yu, *Finite-Window Computational Anti-Phantom Theorems for Scale-Critical Navier--Stokes Defects*, arXiv:2606.15456.
2. R. Yu, *Finite-Window Local-to-Clean Transfer and Anti-Phantom Detection for Sharp Navier--Stokes Packages*, arXiv:2606.18476.
3. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
4. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
5. `NS_IDRP_03_RelativeInvisibleBurst_BDR_v0.1.md`.
6. `NS_DCRP_CYCLE_VIII_HANDOFF_v1.0.md`.
