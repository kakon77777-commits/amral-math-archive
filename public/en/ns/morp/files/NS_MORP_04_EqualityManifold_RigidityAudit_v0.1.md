---
title: "Navier–Stokes Minimal Obstruction Rigidity Program 04: Ancient-State Liouville Cuts, Local-Energy-Slack Rigidity, Zero-Tax Splitting and Equality-Manifold Exclusion Audit"
short_title: "NS-MORP 04"
series: "Navier–Stokes Minimal Obstruction Rigidity Program"
cycle: "VII"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en-US"
status: "Equality-manifold rigidity audit / partial normal-form exclusion"
epistemic_status: "Audits the first MORP equality-manifold normal forms against primary Navier-Stokes rigidity results and derives new internal rigidity consequences. Proves that any dissipation defect measure arising under the MORP-02 strong local L3 state compactness is quantitatively dominated by the local-energy-inequality slack of the limiting suitable weak solution. Hence zero local-energy slack forces zero dissipation defect, and in particular a state-trivial interior limit cannot carry a nonzero pure dissipation defect. This eliminates the pure parabolic degree-one dissipation-defect fixed point from the kernel-saturated minimal-invisible branch once local-energy slack is included as a native nonnegative cost. Proves a model-cone equality theorem: on a finite-H1 return interval, if the Miller residual ratio is at most one and the endpoint strain H1 norms agree, then equality holds in the Cauchy-Schwarz step, forcing R_SV=Delta S and a reduced strain evolution. Imports Albritton-Barker's Type-I ancient-solution equivalence and backward-sequence L3 Liouville theorem as an external state-visible exclusion cut; continuous/backward self-similar and selected asymptotically discretely self-similar subbranches are further excluded under external integrability hypotheses, while the general three-dimensional bounded ancient Liouville problem remains open. Proves a zero-tax profile-support reduction: in a minimal equality split, any component belonging to a rigidity-excluded kernel subclass must have zero carrier mass. The surviving equality manifold is reduced to ancient states outside known Liouville classes, trace/scale/spatial escape carriers, transition/recurrence residuals, or zero-tax equality splitting composed only of such surviving carriers. No universal native extraction, full transition realization, equality-manifold exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Minimal Obstruction Rigidity Program 04

# Ancient-State Liouville Cuts, Local-Energy-Slack Rigidity, Zero-Tax Splitting and Equality-Manifold Exclusion Audit

## 0. Context and Positioning

MORP-03 reduced recurrent minimal obstructions, under explicit compactness/transition hypotheses, to normal forms including:

$$
\boxed{
\text{state-visible recurrent/ancient profile},
}
$$

$$
\boxed{
\text{minimal equality splitting},
}
$$

and:

$$
\boxed{
\text{defect-only parabolic degree-one measure}.
}
$$

The present paper asks:

> which of these equality-manifold objects are already incompatible with suitable-weak Navier--Stokes structure or known Liouville theorems?

The main new internal result is that the simplest dissipation-defect-only branch is excluded by the local energy inequality once the MORP-02 strong-state compactness is used correctly.

---

# 1. Suitable-weak local energy slack

Let:

$$
(u,p)
$$

be a suitable weak solution on an interior cylinder:

$$
Q.
$$

Fix viscosity:

$$
\nu>0.
$$

For:

$$
0\le\phi\in C_c^\infty(Q),
$$

define the distributional local-energy slack:

$$
\boxed{
\begin{aligned}
\mathscr S_{\rm LEI}
(
u,p;\phi
)
={}&
\int_Q
|u|^2
(
\partial_t\phi
+
\nu\Delta\phi
)
\,dxdt
\\
&+
\int_Q
(
|u|^2+2p
)
u\cdot\nabla\phi
\,dxdt
\\
&-
2\nu
\int_Q
\phi
|\nabla u|^2
\,dxdt.
\end{aligned}
}
$$

Suitability gives:

$$
\boxed{
\mathscr S_{\rm LEI}(u,p;\phi)\ge0.
}
$$

---

# 2. Compact sequence with dissipation defect

Let:

$$
(u_n,p_n)
$$

be suitable weak solutions on:

$$
Q,
$$

such that on compact interior subcylinders:

$$
\boxed{
u_n\to u_\ast
\quad
\text{strongly in }
L^3,
}
$$

$$
\boxed{
p_n\rightharpoonup p_\ast
\quad
\text{weakly in }
L^{3/2},
}
$$

and:

$$
\boxed{
\nabla u_n
\rightharpoonup
\nabla u_\ast
\quad
\text{weakly in }
L^2.
}
$$

Assume:

$$
\boxed{
|\nabla u_n|^2dxdt
\stackrel{\ast}{\rightharpoonup}
|\nabla u_\ast|^2dxdt
+
\nu_{\rm diss},
}
$$

with:

$$
\nu_{\rm diss}\ge0.
$$

This is the MORP-02 compactness setting.

---

# 3. Pressure-work convergence

Strong:

$$
u_n\to u_\ast
\quad
\text{in }
L^3
$$

implies:

$$
|u_n|^2
\to
|u_\ast|^2
\quad
\text{in }
L^{3/2}.
$$

Moreover:

$$
p_nu_n
\rightharpoonup
p_\ast u_\ast
\quad
\text{in the pairing against bounded compactly supported functions}.
$$

Indeed one factor is weak:

$$
L^{3/2},
$$

and the other converges strongly in:

$$
L^3.
$$

Therefore every nondissipative term in the local energy inequality passes to the limit.

---

# 4. CIV/VII-4.1 — LEI-Slack Dominates Dissipation Defect

## Theorem 4.1

Under Sections 1--3, for every nonnegative:

$$
\phi\in C_c^\infty(Q),
$$

$$
\boxed{
2\nu
\int_Q
\phi
\,d\nu_{\rm diss}
\le
\mathscr S_{\rm LEI}
(
u_\ast,p_\ast;\phi
).
}
$$

### Proof

Apply the local energy inequality to:

$$
(u_n,p_n).
$$

Pass to the limit in all velocity and pressure-work terms using Section 3.

The dissipation term converges as a measure to:

$$
|\nabla u_\ast|^2dxdt+\nu_{\rm diss}.
$$

Rearrange the limiting inequality.

$\square$

---

# 5. Zero-slack rigidity

## Corollary 5.1

If:

$$
\boxed{
\mathscr S_{\rm LEI}
(
u_\ast,p_\ast;\phi
)
=
0
}
$$

for every:

$$
0\le\phi\in C_c^\infty(Q),
$$

then:

$$
\boxed{
\nu_{\rm diss}=0
\quad
\text{in }Q.
}
$$

Thus a local-energy-equality limit cannot hide positive interior dissipation defect under the MORP-02 strong-state compactness.

$\square$

---

# 6. State-trivial defect exclusion

Suppose:

$$
\boxed{
u_\ast\equiv0.
}
$$

The distributional momentum equation becomes:

$$
\nabla p_\ast=0.
$$

Hence the pressure is spatially constant and is only a time-dependent gauge.

Therefore all terms in:

$$
\mathscr S_{\rm LEI}
$$

vanish.

---

# 7. CIV/VII-4.2 — Pure Interior Dissipation-Defect Exclusion

## Theorem 7.1

Under Sections 2--6:

$$
\boxed{
u_\ast\equiv0
\Longrightarrow
\nu_{\rm diss}=0
}
$$

on every compact interior cylinder.

### Consequence

A defect-completed limit with zero velocity state cannot be nontrivial solely through an interior dissipation defect measure.

$\square$

---

# 8. Refinement of the MORP obstruction cost

Choose a countable dense family:

$$
\{
\phi_m
\}_{m\ge1}
\subset
C_c^\infty(Q),
\qquad
\phi_m\ge0.
$$

Define the local-energy-slack cost:

$$
\boxed{
\mathsf L_{\rm LEI}(D)
=
\sum_{m=1}^{\infty}
2^{-m}
\min
\left\{
1,
\mathscr S_{\rm LEI}
(
u,p;\phi_m
)
\right\}.
}
$$

Add:

$$
\mathsf L_{\rm LEI}
$$

to the native residual sector of:

$$
\mathfrak J.
$$

Then:

$$
\boxed{
\mathfrak J(D)=0
\Longrightarrow
\mathsf L_{\rm LEI}(D)=0.
}
$$

By continuity/density of the distributional slack, all nonnegative compactly supported tests have zero slack.

---

# 9. CIV/VII-4.3 — Kernel-Saturated Dissipation-Defect Exclusion

## Theorem 9.1

Let:

$$
D_\ast
$$

be a MORP minimal-invisible profile satisfying:

$$
\boxed{
\mathfrak J(D_\ast)=0
}
$$

with:

$$
\mathsf L_{\rm LEI}
$$

included in:

$$
\mathfrak J.
$$

Then:

$$
\boxed{
\nu_{\rm diss,\ast}=0.
}
$$

### Meaning

The pure parabolic degree-one dissipation-defect fixed point from MORP-03 does not survive inside the full kernel-saturated suitable-weak equality manifold.

$\square$

---

# 10. What defect-only obstruction can still mean

After Theorem 9.1, a state-trivial normalized package may remain natively nonzero only through other carriers such as:

$$
\boxed{
\text{selected-time trace defect},
}
$$

$$
\boxed{
\text{relative-scale/spatial escape},
}
$$

$$
\boxed{
\text{transition/reproduction residual},
}
$$

or another native coordinate not annihilated by the equality manifold.

Thus:

$$
\boxed{
\text{defect-only}
}
$$

is refined to:

$$
\boxed{
\text{trace/escape/transition-only}.
}
$$

---

# 11. CKN geometry safety

Classical and quantitative partial regularity constrain the parabolic size of the singular set.

They do not identify the MORP dissipation defect with the singular-set measure.

Therefore the exclusion in Theorem 9.1 comes from the local energy inequality and strong-state compactness, not merely from the one-dimensional CKN Hausdorff bound.

---

# 12. External Type-I ancient-state route

Albritton--Barker prove:

$$
\boxed{
\text{local Type-I singularity}
\Longleftrightarrow
\text{nontrivial bounded mild ancient solution satisfying Type-I decay}.
}
$$

Thus a state-visible Type-I MORP profile may enter an ancient-solution normal form under the corresponding extraction hypotheses.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED}.
}
$$

---

# 13. External backward-sequence $L^3$ Liouville cut

The same work proves a Liouville theorem for bounded ancient Navier--Stokes solutions which are bounded in:

$$
L^3(\mathbb R^3)
$$

along a backward sequence of times.

Thus if:

$$
U
$$

is a bounded ancient MORP state and there exist:

$$
t_j\to-\infty
$$

with:

$$
\boxed{
\sup_j
\|U(t_j)\|_{L^3}
<
\infty,
}
$$

then:

$$
\boxed{
U\equiv0.
}
$$

This contradicts a native-separated nontrivial state-visible minimal profile.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED}.
}
$$

---

# 14. Ancient $L^3$ escape condition

A nontrivial bounded ancient MORP state which survives the Section 13 Liouville theorem must satisfy:

$$
\boxed{
\liminf_{t\to-\infty}
\|U(t)\|_{L^3}
=
\infty
}
$$

in the extended sense that no backward sequence has a uniform finite:

$$
L^3
$$

bound.

This is a rigid escape condition.

It is not a contradiction.

---

# 15. General bounded ancient Liouville problem

The general three-dimensional bounded-ancient Liouville problem is not solved.

Koch--Nadirashvili--Seregin--Šverák explicitly obtain full rigidity in two dimensions and partial/symmetric results in three dimensions, while the general three-dimensional problem remains beyond those methods.

Therefore:

$$
\boxed{
\text{bounded ancient}
}
$$

alone cannot be used as an exclusion theorem for the MORP state-visible branch.

---

# 16. Backward self-similar subbranches

Known Liouville theorems exclude significant subclasses of backward self-similar profiles.

Chae--Wolf exclude nontrivial self-similar profiles under Lorentz-space hypotheses including:

$$
\boxed{
L^{p,\infty},
\qquad
p>\frac32.
}
$$

Related work excludes additional Morrey-space classes.

Thus a MORP ancient fixed point that upgrades from discrete return invariance to the corresponding continuous self-similar profile and lies in such a class is trivial.

### Status

$$
\boxed{
\mathrm{EXTERNAL/CONDITIONAL\ SUBBRANCH}.
}
$$

---

# 17. Discretely self-similar subbranches

Discrete renormalization fixed points are not automatically covered by continuous self-similar Liouville theorems.

Chae excludes locally asymptotically discretely self-similar blow-up under a time-periodic profile in:

$$
C^1
\left(
\mathbb R;
L^3(\mathbb R^3)
\cap
C^2(\mathbb R^3)
\right).
$$

Recent Pineau--Vicol work proves further Liouville-type results for rotated backwards self-similar and selected rotated discretely self-similar Type-I solutions under additional rotation/scaling assumptions.

These results shrink but do not eliminate the general discrete-return MORP branch.

---

# 18. Ancient state rigidity ledger

The state-visible recurrent branch is therefore partitioned into:

### A-L3

bounded backward-sequence:

$$
L^3
$$

state:

$$
\boxed{
\mathrm{EXCLUDED}.
}
$$

### A-SS

self-similar state satisfying known Lorentz/Morrey Liouville hypotheses:

$$
\boxed{
\mathrm{EXCLUDED}.
}
$$

### A-DSS-controlled

selected discretely/asymptotically self-similar classes satisfying known periodicity/integrability or recent RDSS hypotheses:

$$
\boxed{
\mathrm{EXCLUDED\ IN\ THOSE\ SUBCLASSES}.
}
$$

### A-GEN

general bounded ancient kernel-saturated state outside those hypotheses:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 19. Model-cone equality setting

Set viscosity:

$$
\nu=1
$$

for this section.

Let:

$$
S
$$

be a smooth strain field on:

$$
[a,b].
$$

Let:

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
\right).
$$

The Miller strain balance is:

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

Define:

$$
\boxed{
\chi_{SV}
=
\frac{
\|\mathcal R_{SV}\|_2
}{
\|-\Delta S\|_2
}
}
$$

when the denominator is nonzero.

---

# 20. CIV/VII-4.4 — Model-Cone Equality Rigidity

## Theorem 20.1

Assume:

1.:
   $$
   S
   \in
   L^\infty
   (
   a,b;
   \dot H^1
   )
   $$
   and the balance is integrable;

2.:
   $$
   \chi_{SV}(t)\le1
   $$
   for almost every:
   $$
   t\in[a,b];
   $$

3.:
   $$
   \|S(b)\|_{\dot H^1}
   =
   \|S(a)\|_{\dot H^1}.
   $$

Then for almost every time with:

$$
\|-\Delta S\|_2>0,
$$

$$
\boxed{
\chi_{SV}=1,
}
$$

and equality holds in Cauchy--Schwarz:

$$
\boxed{
\mathcal R_{SV}
=
\Delta S.
}
$$

Consequently the strain equation reduces to:

$$
\boxed{
\partial_tS
=
\frac12
P_{st}
(
\omega\otimes\omega
)
}
$$

on the equality set.

### Proof

Let:

$$
Z=-\Delta S.
$$

The exact balance and Cauchy--Schwarz give:

$$
\frac12
\frac d{dt}
\|S\|_{\dot H^1}^2
\le
-
(
1-\chi_{SV}
)
\|Z\|_2^2
\le0.
$$

The endpoint norms agree, so the nonpositive derivative integrates to zero.

Hence:

$$
(
1-\chi_{SV}
)
\|Z\|_2^2
=
0
$$

almost everywhere and equality holds throughout the Cauchy--Schwarz chain.

The sign in the exact balance then forces:

$$
\mathcal R_{SV}=-Z=\Delta S.
$$

Substitute into the exact strain equation.

$\square$

---

# 21. Meaning of model-cone equality

A finite:

$$
\dot H^1
$$

zero-tax recurrent state inside the closed model cone is not an arbitrary ancient solution.

It lies on an exact nonlinear alignment manifold.

This is a genuine mechanism rigidity.

### Safety

A general bounded mild ancient solution need not possess the global:

$$
\dot H^1
$$

integrability or endpoint equality required here.

Therefore this does not close A-GEN.

---

# 22. Filtered-increment kernel status

The external filtered-vorticity theory proves:

- scale-invariant control by a derivative-compatible increment defect;
- recurrence of that defect under persistent post-near-field surplus;
- Young-profile compactness for bounded critical defects.

It does not provide a universal theorem saying:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}=0
\Longrightarrow
u\equiv0.
}
$$

Therefore the filtered-increment zero set cannot presently be used as a complete Liouville theorem.

This is an important rigidity gap.

---

# 23. Zero-cost profile splitting

Consider a minimal equality split from MORP-03:

$$
D_\ast
\rightsquigarrow
\{
D^{(j)}
\}.
$$

Assume:

$$
q_\ast=0.
$$

Minimal splitting saturation gives:

$$
\boxed{
\mathfrak J(D^{(j)})=0
}
$$

for every surviving component with positive carrier mass.

Thus each component lies in the same mechanism-augmented equality kernel.

---

# 24. Rigidity-excluded profile subclass

Let:

$$
\boxed{
\mathscr E_{\rm rig}
}
$$

be any subclass of normalized profiles for which a theorem proves:

$$
\boxed{
D\in
\mathscr E_{\rm rig}
\cap
\mathcal K_{\rm ext}
\Longrightarrow
D
\text{ is native-trivial}.
}
$$

Examples established in this paper include, under their hypotheses:

- state-trivial pure dissipation-defect profiles;
- bounded ancient states with a backward-sequence:
  $$
  L^3
  $$
  bound;
- selected self-similar/DSS profiles covered by external Liouville theorems.

---

# 25. CIV/VII-4.5 — Zero-Tax Splitting Support Reduction

## Theorem 25.1

Let a zero-cost minimal split have profile carrier masses:

$$
a_j>0.
$$

If:

$$
D^{(j)}
\in
\mathscr E_{\rm rig},
$$

then that profile cannot be a nontrivial carrier.

Equivalently, all positive carrier mass of a zero-tax equality split must lie in:

$$
\boxed{
\mathcal K_{\rm ext}
\setminus
\mathscr E_{\rm rig}.
}
$$

### Proof

Every surviving component has zero obstruction cost by minimal splitting saturation.

If a positive-mass component lies in:

$$
\mathscr E_{\rm rig},
$$

the rigidity theorem makes it native-trivial, contradicting positive carrier mass.

$\square$

---

# 26. Consequence for equality splitting

Rigidity acts componentwise.

As more kernel subclasses are excluded, a zero-tax multi-profile split can survive only by concentrating all carrier mass into the remaining unclassified kernel class.

Thus profile splitting is not an independent escape mechanism forever.

Its support shrinks with the rigidity classification.

---

# 27. Local kernel collapse with zero state

Suppose a kernel-saturated minimal package has:

$$
u_\ast=0,
$$

$$
\nu_{\rm diss}=0,
$$

and zero transition/native residual in every local PDE coordinate.

Then the distributional equation forces the physical pressure gradient to vanish.

Hence the local state/pressure/dissipation sector is trivial.

Any remaining native separation must be carried by:

$$
\boxed{
\text{trace defect}
\vee
\text{spatial/scale escape}
\vee
\text{transition/recurrence carrier}.
}
$$

This defines the **escape-only kernel**.

---

# 28. Escape-only kernel

Define:

$$
\boxed{
\mathcal K_{\rm esc}
}
$$

as the class of state-trivial, local-energy-equality packages whose native nontriviality is supported only by:

- selected-time trace defect;
- compactified relative-scale mass at:
  $$
  \infty;
  $$
- spatial mass at:
  $$
  \infty_x;
  $$
- transition/reproduction residual.

MORP-04 does not exclude:

$$
\mathcal K_{\rm esc}.
$$

This becomes one of the primary targets of the next paper.

---

# 29. Partial regularity does not eliminate the escape-only kernel

CKN and quantitative partial regularity constrain the singular set and bad-scale geometry.

They do not automatically remove:

- selected-time trace escape;
- relative-frequency escape;
- transition defects in the normalized obstruction package.

Therefore:

$$
\boxed{
\mathcal K_{\rm esc}
}
$$

requires a native extraction/recurrence rigidity theorem rather than a direct singular-set dimension argument.

---

# 30. Ancient-state plus mechanism-kernel branch

The surviving state-visible equality object has the schematic form:

$$
\boxed{
U
\neq0
}
$$

ancient, together with:

$$
\boxed{
\mathsf O_{\rm PFET}=0,
}
$$

$$
\boxed{
\mathcal M_{SV}=0,
}
$$

$$
\boxed{
\widetilde{\mathcal S}^{(3)}=0,
}
$$

and zero paid/native residual.

Known Liouville theorems eliminate important subbranches but do not prove this full intersection is empty.

This is the surviving **ancient kernel intersection problem**.

---

# 31. Ancient kernel intersection target

Define:

$$
\boxed{
\mathcal K_{\rm anc}
=
\{
\text{bounded Type-I ancient states}
\}
\cap
\mathcal K_{\rm ext}.
}
$$

The next rigidity target is:

$$
\boxed{
\mathcal K_{\rm anc}
=
\varnothing.
}
$$

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

Known external Liouville results prove emptiness only on additional integrability/self-similarity/symmetry subclasses.

---

# 32. Recent rotated self-similar calibration

Recent 2026 work proves Liouville-type triviality for rotated backward self-similar Type-I states in specified rotation regimes and for selected rotated discretely self-similar states when the scaling factor is sufficiently close to one, under the stated Type-I hypotheses.

This confirms that discrete renormalization fixed points can sometimes be attacked by weighted-energy rigidity.

It does not provide a general theorem for all MORP discrete-return ancient states.

---

# 33. Current equality-manifold reduction

After MORP-04, the pure dissipation-defect branch is removed from the kernel-saturated minimal-invisible class.

The remaining normal forms are compressed to:

$$
\boxed{
\textbf{A-KERNEL}
}
$$

— nontrivial ancient states outside known Liouville subclasses and inside the full mechanism kernel;

$$
\boxed{
\textbf{E-KERNEL}
}
$$

— escape-only trace/scale/spatial/transition carriers;

and:

$$
\boxed{
\textbf{S-KERNEL}
}
$$

— zero-tax profile splitting supported entirely on A-KERNEL or E-KERNEL components.

---

# 34. CIV/VII-4.6 — Equality-Manifold Support Theorem

## Theorem 34.1

Assume:

1. MORP minimal-profile existence;
2. zero obstruction cost:
   $$
   \mathfrak J(D_\ast)=0;
   $$
3. the local-energy slack cost of Section 8 is included;
4. the MORP-03 profile-splitting saturation hypotheses.

Then every positive native carrier of the minimal equality object belongs to:

$$
\boxed{
\mathcal K_{\rm anc}
\cup
\mathcal K_{\rm esc}
}
$$

after removal of the external Liouville-excluded ancient subclasses.

### Meaning

No positive carrier can remain as a pure interior dissipation defect.

Zero-tax splitting only duplicates surviving ancient/escape kernel carriers.

$\square$

---

# 35. Strongest positive result of MORP-04

The equality-manifold obstruction class is substantially smaller than in MORP-03.

In particular:

$$
\boxed{
\text{pure degree-one dissipation defect}
}
$$

is no longer a surviving kernel branch.

State-visible ancient objects are forced into explicit Liouville-escape and/or model-cone equality conditions.

---

# 36. Strongest remaining obstruction

The main unresolved state-visible object is:

$$
\boxed{
\text{nontrivial bounded ancient Type-I state}
}
$$

which:

- has no uniformly bounded:
  $$
  L^3
  $$
  backward sequence;
- avoids the known self-similar/DSS Liouville subclasses;
- remains in the PFET/model-cone/filtered-increment/paid equality kernel.

The main state-trivial object is:

$$
\boxed{
\mathcal K_{\rm esc}.
}
$$

---

# 37. Why no full Liouville claim is possible

General three-dimensional bounded ancient solutions are not classified by existing Liouville theory.

Likewise, current filtered increment theory does not classify the exact zero set of the critical increment defect.

Therefore:

$$
\boxed{
\mathcal K_{\rm anc}
=
\varnothing
}
$$

cannot be claimed.

This is a genuine remaining PDE rigidity problem.

---

# 38. M-RIG status update

### pure interior dissipation defect

$$
\boxed{
\mathrm{CLOSED}
}
$$

inside the zero-LEI-slack kernel.

### ancient backward-sequence $L^3$ branch

$$
\boxed{
\mathrm{EXTERNALLY\ CLOSED}.
}
$$

### selected self-similar/DSS branches

$$
\boxed{
\mathrm{EXTERNALLY\ CLOSED\ UNDER\ STATED\ HYPOTHESES}.
}
$$

### model-cone finite-H1 equality branch

$$
\boxed{
\mathrm{RIGID\ NORMAL\ FORM\ PROVED}.
}
$$

### general ancient kernel intersection

$$
\boxed{
\mathrm{OPEN}.
}
$$

### escape-only kernel

$$
\boxed{
\mathrm{OPEN}.
}
$$

### zero-tax splitting

$$
\boxed{
\mathrm{REDUCED\ TO\ SURVIVING\ KERNEL\ SUPPORT}.
}
$$

---

# 39. What remains of degree-one defect scaling

The degree-one scaling calculation from MORP-03 remains correct as an abstract fixed-measure law.

MORP-04 shows that such a measure cannot arise as a **pure interior dissipation defect** in a kernel-saturated suitable-weak limit with zero LEI slack.

A degree-one measure could still appear in another native transition/escape coordinate, but it is no longer the dissipation-defect normal form considered previously.

---

# 40. Next paper

The next paper should attack the two surviving kernel classes and close Cycle VII if possible:

$$
\boxed{
\textbf{
NS-MORP 05 —
Escape-Only Trace/Scale Rigidity,
Ancient Kernel Intersection,
Native Extraction Closure
and Cycle-VII Final Audit
}.
}
$$

Primary tasks:

1. test whether trace/scale escape can be canonically re-centered/re-scaled into a new state-visible profile;
2. prove a reprofile-or-tax theorem for:
   $$
   \mathcal K_{\rm esc};
   $$
3. intersect ancient states with model-cone equality and filtered increment zero/recurrence conditions;
4. use known ancient Liouville/self-similar/backward-uniqueness results wherever their hypotheses can be derived rather than assumed;
5. determine whether zero-tax equality splitting can persist after reprofile;
6. audit whether M-XTR can be closed by a trace-or-thickening alternative;
7. decide whether Cycle VII yields a genuine minimal obstruction exclusion or only an ancient/escape normal-form reduction.

---

# 41. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{LEI-Slack Dominates Dissipation Defect}
&:\ \mathrm{PROVED},\\
\text{Pure Interior Dissipation-Defect Exclusion}
&:\ \mathrm{PROVED},\\
\text{Kernel-Saturated Dissipation-Defect Exclusion}
&:\ \mathrm{PROVED},\\
\text{Type-I ancient solution extraction}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{backward-sequence }L^3\text{ ancient Liouville cut}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{selected self-similar/DSS Liouville cuts}
&:\ \mathrm{EXTERNAL/CONDITIONAL},\\
\text{Model-Cone Equality Rigidity}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{filtered increment zero-set rigidity}
&:\ \mathrm{OPEN},\\
\text{Zero-Tax Splitting Support Reduction}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{general ancient kernel intersection}
&:\ \mathrm{OPEN},\\
\text{escape-only kernel}
&:\ \mathrm{OPEN},\\
M\mbox{-}XTR
&:\ \mathrm{OPEN},\\
M\mbox{-}COM
&:\ \mathrm{PARTIAL/SUBSTANTIAL},\\
M\mbox{-}TR
&:\ \mathrm{OPEN/PARTIAL},\\
M\mbox{-}RIG
&:\ \mathrm{PARTIALLY\ CLOSED/OPEN},\\
\text{minimal obstruction exclusion}
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

MORP-04 begins to exclude equality-manifold normal forms rather than merely naming them.

The strongest new result concerns defect-only profiles.

Strong local:

$$
L^3
$$

state compactness and weak pressure compactness allow the suitable local energy inequality to pass to the limit with the dissipation defect measure retained.

The defect is quantitatively dominated by the local-energy slack.

Therefore a kernel-saturated local-energy-equality minimizer has no dissipation defect.

In particular, a state-trivial profile cannot secretly carry a pure interior dissipation measure.

The state-visible Type-I branch is also narrowed.

Bounded ancient states with a backward sequence of uniformly bounded:

$$
L^3
$$

norm are trivial by the external Liouville theorem.

Continuous self-similar and selected discretely self-similar subclasses are ruled out under known integrability/periodicity/rotation hypotheses.

If a finite-H1 minimal return lies in the closed Miller model cone with equal endpoint strain norm, it must satisfy the exact model-cone equality law:

$$
\mathcal R_{SV}
=
\Delta S.
$$

Nevertheless, general three-dimensional bounded ancient solutions remain beyond current Liouville classification.

The surviving minimal equality manifold has therefore been compressed to:

$$
\boxed{
\textbf{
ancient kernel carriers
\;\vee\;
escape-only trace/scale/transition carriers.
}
}
$$

Any zero-tax profile splitting can only be composed of those surviving carriers.

The next step is to decide whether escape can always be reprofiled into a state-visible carrier, and whether the remaining ancient kernel intersection is empty.

---

# References

1. D. Albritton, T. Barker, *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, arXiv:1811.00502.
2. G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, *Liouville theorems for the Navier--Stokes equations and applications*, arXiv:0709.3599.
3. D. Chae, J. Wolf, *On the Liouville type theorems for self-similar solutions to the Navier--Stokes equations*, arXiv:1609.06962.
4. D. Chae, *Remarks on the asymptotically discretely self-similar solutions of the Navier--Stokes and the Euler equations*, arXiv:1306.0305.
5. Q. Jiu, Y. Wang, W. Wei, *Leray's backward self-similar solutions to the 3D Navier--Stokes equations in Morrey spaces*, arXiv:2006.15776.
6. B. Pineau, V. Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619.
7. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
8. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
9. Z. Lei, X. Ren, *Quantitative partial regularity of the Navier--Stokes equations and applications*, arXiv:2210.01783.
10. R. Yu, *A Structural Audit of Navier--Stokes Obstruction Calculus*, arXiv:2606.25341.
11. `NS_MORP_02_NativeExtraction_Compactness_v0.1.md`.
12. `NS_MORP_03_Transition_Profile_RigidityEntry_v0.1.md`.