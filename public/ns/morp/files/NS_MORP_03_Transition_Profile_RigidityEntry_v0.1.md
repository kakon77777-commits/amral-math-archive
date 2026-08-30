---
title: "Navier–Stokes Minimal Obstruction Rigidity Program 03：Normalized Return Transitions、Profile Carrier Saturation、Ancient/Defect Normal Forms 與 Rigidity Entry"
short_title: "NS-MORP 03"
series: "Navier–Stokes Minimal Obstruction Rigidity Program"
cycle: "VII"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Transition-invariance compiler / profile-splitting equality analysis / first rigidity normal forms"
epistemic_status: "Replaces overly strong fixed-step transition invariance by a normalized return/re-root transition on native-separated windows. Proves that minimal recurrent obstructions have zero net return depletion and remain in the minimal level set. Introduces a homogeneous native carrier/cost ratio and proves a Minimal Profile Splitting Saturation theorem: under additive profile-carrier and cost decoupling, every nonzero component of a minimizing split must itself be minimal; a positive strict splitting tax therefore excludes multi-profile minimality. This shows minimality alone does not select a single profile without strict subadditivity, uniqueness, or interaction rigidity. Gives a conditional state-visible Type-I route to a nontrivial bounded mild ancient solution, calibrated by Albritton-Barker, and proves that a unique return-fixed ancient state becomes a discrete renormalization fixed point modulo symmetry. For defect-only minimizers, computes the exact Navier-Stokes scaling of the dissipation defect measure and proves that a return-fixed pure-scaling defect is parabolically degree-one homogeneous; in particular it cannot be a point atom at the singular center. Distinguishes profile transition invariance from actual original-solution transition realization, and keeps the shadowing gap explicit. No universal M-XTR, full profile-decomposition theorem for the custom package, actual return-map realization, equality-manifold exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Minimal Obstruction Rigidity Program 03

# Normalized Return Transitions、Profile Carrier Saturation、Ancient/Defect Normal Forms 與 Rigidity Entry

## 0. 本文定位

MORP-01 proved the abstract principle:

$$
\boxed{
\text{minimality}
\Longrightarrow
\text{zero strict transition tax}.
}
$$

MORP-02 substantially closed ordinary local state/active-pressure compactness and built a defect-completed package topology.

The remaining problem is dynamical:

> what is the correct Navier--Stokes transition acting on a minimal obstruction package?

A fixed-time-step invariance condition is too strong.

A real dangerous trajectory may temporarily deplete and later regenerate/re-root.

The correct object is a **return transition on native-separated windows**.

---

# 1. External transition calibration

Critical-element/profile-decomposition Navier--Stokes theory does not use static compactness alone.

The nonlinear Navier--Stokes evolution of the extracted profiles is part of the compactness mechanism.

Finite-window recursive-audit theory likewise propagates certificates along an explicitly selected finite renormalized chain once one-step admissibility is supplied.

Type-I singular rescaling provides another model: suitable weak solutions may be rescaled around a Type-I singularity to obtain a nontrivial bounded mild ancient solution.

These are EXTERNAL calibration modules.

They motivate, but do not prove, the MORP transition below.

---

# 2. Defect-completed normalized package

Write a MORP package as:

$$
\boxed{
D
=
\left(
u,
[p]_{\mathcal H},
[h],
\nu_{\rm diss},
\sigma^{sc},
\tau^{sel},
\mathcal R^{tr}
\right).
}
$$

Let:

$$
d_{\rm nat}(D)
$$

be the native obstruction separation.

Let:

$$
\mathscr O_1
=
\{
D:
d_{\rm nat}(D)\ge1,
\ \mathcal N_{\rm pkg}(D)\le C_\ast
\}.
$$

All coordinates are understood in the defect-completed topology of MORP-02.

---

# 3. Actual evolution and normalization

Let:

$$
\mathsf E_{s\to t}
$$

denote actual Navier--Stokes evolution/restriction of one package from time:

$$
s
$$

to a later admissible window time:

$$
t.
$$

Let:

$$
\mathsf N_{\rm norm}
$$

denote the declared normalization:

- recentering;
- parabolic rescaling;
- pressure/harmonic quotient normalization;
- terminal/reference-scale normalization;
- selected-trace normalization.

Define a candidate normalized transition:

$$
\boxed{
\mathsf T
=
\mathsf N_{\rm norm}
\circ
\mathsf E.
}
$$

### Safety

The existence of:

$$
\mathsf E
$$

on one profile-limit package is not the same as realization by one actual original-solution branch.

---

# 4. Why fixed-step invariance is too strong

It is not necessary that:

$$
d_{\rm nat}(\mathsf E_tD)\ge1
$$

at every intermediate time/window.

A legitimate obstruction may:

- partially deplete;
- transfer across channels;
- become source-dominated;
- later re-root into a new dangerous window.

Therefore MORP uses a return/re-root transition.

---

# 5. Native recurrent window

A later window:

$$
W'
$$

is a native return of:

$$
D
$$

if the actual/reconstructed package:

$$
D(W')
$$

satisfies:

$$
\boxed{
d_{\rm nat}
(
D(W')
)
\ge1.
}
$$

A canonical return rule may choose:

- the first later native-separated window;
- the first later dangerous-certified native-separated window;
- the next member of a fixed admissible extraction sequence.

The rule must be stated before compactness/minimality is used.

---

# 6. Return transition

Define:

$$
\boxed{
\mathsf T_{\rm ret}(D)
=
\mathsf N_{\rm norm}
\left(
D(W_{\rm ret})
\right).
}
$$

The return transition is **actual** only when:

$$
W_{\rm ret}
$$

comes from the original same Navier--Stokes solution/history.

A profile return map may also be defined on the compact closure.

These two maps are kept distinct.

---

# 7. Profile versus actual transition

Write:

$$
\boxed{
\mathsf T_{\rm prof}
}
$$

for a transition defined on the compact/profile closure, and:

$$
\boxed{
\mathsf T_{\rm act}
}
$$

for an actual original-solution return.

A valid shadowing theorem would imply compatibility:

$$
\boxed{
\mathsf T_{\rm prof}
\text{ is realized by }
\mathsf T_{\rm act}.
}
$$

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 8. Return invariance obligation

The correct M-TR condition is:

$$
\boxed{
\text{native recurrence}
\Longrightarrow
\mathsf T_{\rm ret}
(
\mathscr O_1
)
\subset
\mathscr O_1.
}
$$

This is weaker and more physically faithful than fixed-step invariance.

---

# 9. Return depletion ledger

Suppose one return interval carries a nonnegative net tax:

$$
\boxed{
\Delta_{\rm ret}(D)\ge0.
}
$$

Assume:

$$
\boxed{
\mathfrak J
(
\mathsf T_{\rm ret}D
)
+
\Delta_{\rm ret}(D)
\le
\mathfrak J(D).
}
$$

The tax may include:

- net detector depletion;
- unabsorbed diffusion;
- paid-side sign-coherent loss;
- model-cone contraction;
- filtered-defect depletion;
- other declared nonnegative return costs.

---

# 10. CIV/VII-3.1 — Minimal Return Rigidity

## Theorem 10.1

Assume:

1.:
   $$
   D_\ast\in\mathscr O_1
   $$
   minimizes:
   $$
   \mathfrak J;
   $$
2.:
   $$
   \mathsf T_{\rm ret}D_\ast
   \in
   \mathscr O_1;
   $$
3. the return depletion ledger of Section 9 holds.

Then:

$$
\boxed{
\Delta_{\rm ret}(D_\ast)=0,
}
$$

and:

$$
\boxed{
\mathfrak J
(
\mathsf T_{\rm ret}D_\ast
)
=
\mathfrak J(D_\ast)
=
m_\ast.
}
$$

### Proof

Minimality gives:

$$
m_\ast
\le
\mathfrak J
(
\mathsf T_{\rm ret}D_\ast
).
$$

The return ledger gives:

$$
\mathfrak J
(
\mathsf T_{\rm ret}D_\ast
)
+
\Delta_{\rm ret}(D_\ast)
\le
m_\ast.
$$

Combine.

$\square$

---

# 11. Meaning

A minimal recurrent obstruction is a **zero-net-depletion return orbit**.

This is the first dynamical equality-manifold normal form of MORP.

A minimal obstruction is not required to stay large continuously.

It is required to return with no strictly positive net tax.

---

# 12. Recurrent minimal set

Define:

$$
\boxed{
\mathscr M_\ast^{ret}
=
\{
D\in\mathscr O_1:
\mathfrak J(D)=m_\ast,
\ \mathsf T_{\rm ret}D
\text{ exists}
\}.
}
$$

Under the hypotheses of Theorem 10.1:

$$
\boxed{
\mathsf T_{\rm ret}
(
\mathscr M_\ast^{ret}
)
\subset
\mathscr M_\ast^{ret},
}
$$

and:

$$
\boxed{
\Delta_{\rm ret}=0
}
$$

on the recurrent minimal set.

---

# 13. Native carrier for profile splitting

The native distance:

$$
d_{\rm nat}
$$

need not be additive under profile decomposition.

Therefore introduce a nonnegative homogeneous **native carrier mass**:

$$
\boxed{
\mathfrak a(D)\ge0.
}
$$

Require:

$$
\boxed{
\mathfrak a(cD)
=
c
\mathfrak a(D)
}
$$

for:

$$
c\ge0,
$$

in the linearized/native package coordinates where this normalization is meaningful.

The carrier is acceptable only if:

$$
\mathfrak a(D)>0
$$

implies native nontriviality.

It may be obtained from a finite component carrier lemma or a non-tautological extraction coordinate.

---

# 14. Homogeneous obstruction ratio

For:

$$
\mathfrak a(D)>0,
$$

define:

$$
\boxed{
\mathfrak Q(D)
=
\frac{
\mathfrak J(D)
}{
\mathfrak a(D)
}.
}
$$

Normalize a minimizing sequence by:

$$
\boxed{
\mathfrak a(D_n)=1.
}
$$

Let:

$$
\boxed{
q_\ast
=
\inf
\mathfrak Q.
}
$$

This ratio is designed for profile-splitting analysis.

---

# 15. Profile decomposition hypothesis

Assume a normalized sequence admits profiles:

$$
D^{(1)},
D^{(2)},\ldots
$$

with carrier masses:

$$
a_j
=
\mathfrak a
(
D^{(j)}
)
\ge0.
$$

Assume carrier decoupling:

$$
\boxed{
1
=
\sum_j
a_j
+
a_{\rm rem},
}
$$

and cost lower decoupling:

$$
\boxed{
\liminf_n
\mathfrak J(D_n)
\ge
\sum_j
\mathfrak J(D^{(j)})
+
J_{\rm rem}.
}
$$

Here:

$$
a_{\rm rem},J_{\rm rem}\ge0.
$$

This is a MORP profile-decomposition hypothesis, not a theorem yet for the full custom package.

---

# 16. CIV/VII-3.2 — Minimal Profile Splitting Saturation

## Theorem 16.1

Assume:

1.:
   $$
   D_n
   $$
   is a minimizing sequence:
   $$
   \mathfrak a(D_n)=1,
   \qquad
   \mathfrak J(D_n)\to q_\ast;
   $$
2. Section 15 holds;
3. every nonzero profile satisfies:
   $$
   \mathfrak J(D^{(j)})
   \ge
   q_\ast
   a_j;
   $$
4. the remainder satisfies:
   $$
   J_{\rm rem}
   \ge
   q_\ast
   a_{\rm rem}.
   $$

Then all inequalities saturate:

$$
\boxed{
\mathfrak J(D^{(j)})
=
q_\ast a_j
}
$$

for every:

$$
a_j>0,
$$

and:

$$
\boxed{
J_{\rm rem}
=
q_\ast a_{\rm rem}.
}
$$

### Proof

Section 15 and the lower bounds give:

$$
q_\ast
\ge
q_\ast
\left(
\sum_ja_j+a_{\rm rem}
\right)
=
q_\ast.
$$

Hence equality holds at every nonnegative stage.

$\square$

---

# 17. Interpretation

Minimality alone does **not** exclude multi-profile splitting.

Instead it forces:

$$
\boxed{
\text{every surviving profile is itself minimal}.
}
$$

Therefore a minimal split cannot contain an inefficient profile.

This is a rigidity statement, but not yet single-carrier selection.

---

# 18. Strict splitting tax

Suppose the cost decomposition improves to:

$$
\boxed{
\liminf_n
\mathfrak J(D_n)
\ge
\sum_j
\mathfrak J(D^{(j)})
+
J_{\rm rem}
+
\Theta_{\rm split},
}
$$

where:

$$
\boxed{
\Theta_{\rm split}\ge0.
}
$$

The term:

$$
\Theta_{\rm split}
$$

measures an interaction/localization/transition tax generated by genuine profile dichotomy.

---

# 19. CIV/VII-3.3 — Strict-Dichotomy Exclusion

## Theorem 19.1

Under Theorem 16.1, if every genuine multi-profile split satisfies:

$$
\boxed{
\Theta_{\rm split}>0,
}
$$

then a minimizing sequence cannot genuinely split into two or more nonzero profiles.

### Proof

For a genuine split:

$$
\liminf_n
\mathfrak J(D_n)
\ge
q_\ast
+
\Theta_{\rm split}
>
q_\ast,
$$

contradicting minimizing convergence.

$\square$

---

# 20. What can replace a strict splitting tax

Single-carrier minimality may also follow from:

- uniqueness of the minimizer modulo symmetry;
- strict convexity of a native carrier/cost component;
- a nonlinear profile interaction theorem;
- a transition rule incompatible with simultaneous minimal profiles;
- an actual-branch shadowing theorem selecting one recurrent carrier.

None is proved universally here.

---

# 21. Diffuse minimal splitting

If:

$$
\Theta_{\rm split}=0,
$$

minimality permits a collection of mutually orthogonal minimal carriers.

The resulting object is a **minimal equality splitting**.

This is the profile analogue of the diffuse causal forest encountered in ANP/CFOP.

Therefore MORP does not assume that minimality automatically restores one atomic lineage.

---

# 22. State-visible minimal profile

Suppose:

$$
D_\ast
$$

has a nontrivial state component:

$$
u_\ast\not\equiv0.
$$

Assume it arises from Type-I singular rescaling around:

$$
(x_\ast,T_\ast)
$$

with the uniform hypotheses required by the external Type-I compactness theorem.

Then a subsequence may generate a nontrivial bounded mild ancient solution:

$$
\boxed{
U:
\mathbb R^3\times(-\infty,0)
\to
\mathbb R^3.
}
$$

### Status

$$
\boxed{
\mathrm{EXTERNAL/CONDITIONAL\ TYPE\mbox{-}I\ ROUTE}.
}
$$

---

# 23. Ancient-profile safety

The external Type-I theorem produces an ancient Navier--Stokes state.

It does not prove:

$$
\boxed{
\text{all MORP audit/mechanism kernel coordinates}
}
$$

pass to that ancient state.

A compatibility theorem is required to transport:

- PFET invisibility;
- model-cone saturation;
- filtered increment saturation;
- paid-side equality;
- native transition equality.

---

# 24. Renormalized fixed point

Suppose the recurrent minimal set has one element modulo residual symmetry:

$$
\boxed{
\mathscr M_\ast^{ret}/\mathcal G
=
\{
[D_\ast]
\}.
}
$$

Then:

$$
\boxed{
\mathsf T_{\rm ret}D_\ast
\simeq_{\mathcal G}
D_\ast.
}
$$

This is a renormalization fixed point.

---

# 25. State component of a fixed return

Suppose:

$$
\mathsf T_{\rm ret}
$$

corresponds to:

1. Navier--Stokes evolution between two horizon-related windows;
2. parabolic rescaling by a fixed factor:
   $$
   \lambda>1;
   $$
3. a fixed normalized time translation;
4. recentering by the allowed symmetry.

Then the state component satisfies a discrete renormalization relation.

Schematically:

$$
\boxed{
U
\simeq
\mathcal S_\lambda
\mathcal E_{\tau}
U.
}
$$

When the windows are centered at one singular horizon and the ancient extension is valid, this becomes a discrete self-similar/renormalized-periodic ancient normal form modulo the declared symmetries.

### Status

$$
\boxed{
\mathrm{CONDITIONAL}.
}
$$

---

# 26. State-visible rigidity target

The next rigidity theorem may therefore attempt to exclude:

$$
\boxed{
\text{nontrivial bounded ancient solution}
+
\text{mechanism-augmented kernel saturation}
+
\text{zero return tax}
}
$$

or classify it into an already understood special family.

This is substantially narrower than excluding arbitrary ancient solutions.

---

# 27. Defect-only minimal profile

Suppose instead:

$$
u_\ast
$$

is state-trivial in the selected compact topology, while:

$$
\boxed{
\nu_\ast^{diss}\neq0.
}
$$

Assume the return transition is pure parabolic scaling by:

$$
\lambda>1
$$

after the defect package has been recentered at the singular point.

---

# 28. Dissipation-measure scaling

Under Navier--Stokes scaling:

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2t),
$$

$$
\nabla u_\lambda
=
\lambda^2
\nabla u(\lambda x,\lambda^2t).
$$

Hence for the dissipation measure:

$$
\mu_u
=
|\nabla u|^2dxdt,
$$

$$
\boxed{
\mu_{u_\lambda}(E)
=
\lambda^{-1}
\mu_u
(
\Phi_\lambda(E)
),
}
$$

where:

$$
\boxed{
\Phi_\lambda(x,t)
=
(\lambda x,\lambda^2t).
}
$$

The same scaling law is imposed on a dissipation defect measure inherited as a weak-star limit.

---

# 29. CIV/VII-3.4 — Defect Fixed-Point Homogeneity

## Theorem 29.1

Assume a defect-only minimal profile is fixed by the pure scaling transition:

$$
\boxed{
\mathcal S_\lambda^{diss}
\nu_\ast
=
\nu_\ast.
}
$$

Then:

$$
\boxed{
\nu_\ast
(
\Phi_\lambda(E)
)
=
\lambda
\nu_\ast(E)
}
$$

for every admissible Borel set:

$$
E.
$$

Thus the defect is discretely parabolically homogeneous of degree one.

$\square$

---

# 30. Parabolic cylinder law

Let:

$$
Q_r
$$

be a parabolic cylinder centered at the scaling fixed point.

Then:

$$
\Phi_\lambda(Q_r)=Q_{\lambda r}.
$$

Therefore:

$$
\boxed{
\nu_\ast(Q_{\lambda r})
=
\lambda
\nu_\ast(Q_r).
}
$$

Along the discrete scaling orbit:

$$
\boxed{
\nu_\ast(Q_{\lambda^nr})
=
\lambda^n
\nu_\ast(Q_r).
}
$$

This is a one-dimensional parabolic mass law.

---

# 31. CIV/VII-3.5 — No Point-Atom Defect Fixed Point

## Theorem 31.1

Under Theorem 29.1:

$$
\boxed{
\nu_\ast(\{(0,0)\})=0.
}
$$

### Proof

The singular center is fixed by:

$$
\Phi_\lambda.
$$

Therefore:

$$
\nu_\ast(\{0\})
=
\lambda
\nu_\ast(\{0\}).
$$

Since:

$$
\lambda>1,
$$

the mass must vanish.

$\square$

---

# 32. Meaning of the defect normal form

A defect-only transition-fixed obstruction cannot be merely a point mass at the singular center.

It must occupy a scale-extended parabolic structure compatible with degree-one homogeneity.

This is a first genuine rigidity statement about the defect-only branch.

It does not exclude non-atomic one-dimensional parabolic defect measures.

---

# 33. Defect profile and CKN geometry

The parabolic degree-one law is structurally compatible with the critical one-dimensional scaling that appears in partial-regularity geometry.

This is a scaling analogy only.

MORP does not identify:

$$
\nu_\ast
$$

with the CKN singular-set measure or claim existence of a singular solution.

---

# 34. Relative-scale defect under return

The compactified relative-frequency measure:

$$
\sigma^{sc}
$$

must also be transported by:

$$
\mathsf T_{\rm ret}.
$$

For a true fixed point, its push-forward under the declared scale/reference-shell normalization must equal itself.

The exact induced map depends on the re-root/reference-shell rule.

Therefore no universal shift-invariance theorem is claimed here.

This is retained as part of M-TR.

---

# 35. Profile transition invariance

On the defect-completed closure, a profile transition is acceptable if:

1. the evolved state remains a suitable weak package;
2. harmonic pressure stays in the declared quotient/tail class;
3. dissipation defect measures push forward under the correct scaling law;
4. selected traces or trace defects are re-extracted;
5. scale/spatial defect measures are pushed forward by the declared normalization;
6. native separation is recovered at the chosen return;
7. the compactness norm remains bounded.

Proving these items gives:

$$
\boxed{
\mathsf T_{\rm prof}
(
\mathscr O_1
)
\subset
\mathscr O_1.
}
$$

Current status:

$$
\boxed{
\mathrm{OPEN/PARTIAL}.
}
$$

---

# 36. Actual transition realization

Even if:

$$
\mathsf T_{\rm prof}
$$

is well defined and compact, MORP still needs:

$$
\boxed{
\mathsf T_{\rm act}
}
$$

to exist on one actual original-solution obstruction history.

Finite-window recursive-audit theory provides finite renormalized chains once one-step admissibility is supplied.

It does not prove one infinite actual minimal return orbit.

Thus:

$$
\boxed{
\text{profile recurrence}
\neq
\text{actual recurrent branch}.
}
$$

---

# 37. Transition alternatives

For a minimal obstruction sequence, the dynamic possibilities are now:

### TR-A — single recurrent carrier

A compact/minimal carrier returns and saturates zero tax.

### TR-B — minimal equality splitting

Multiple orthogonal carriers survive, each individually minimal, with zero splitting tax.

### TR-C — state-visible ancient normal form

Under Type-I/actual-rescaling hypotheses, the recurrent state component extends to a nontrivial bounded ancient solution.

### TR-D — defect-only homogeneous normal form

The state disappears but a parabolically degree-one defect measure survives.

These are not yet exhaustive in the absence of a full custom profile decomposition.

---

# 38. CIV/VII-3.6 — Transition-Rigidity Entry Dichotomy

## Theorem 38.1

Assume:

1. M-XTR provides a nonempty normalized obstruction class;
2. MORP-02 compactness/attainment holds;
3. a return transition exists on the minimal class;
4. the return depletion law holds;
5. a carrier profile decomposition satisfies Section 15.

Then every recurrent minimizing sequence enters at least one of the following normal forms:

$$
\boxed{
\text{single minimal return carrier}
}
$$

or:

$$
\boxed{
\text{minimal equality splitting}.
}
$$

In a state-visible Type-I subbranch, any compact singular rescaling limit may additionally enter the ancient-state route.

In a defect-only pure-scaling fixed branch, the defect measure satisfies Theorem 29.1.

### Safety

The theorem is conditional on the listed extraction, compactness, transition, and profile-decomposition hypotheses.

$\square$

---

# 39. Rigidity entry

MORP is now ready to ask not:

> does a minimal profile exist?

but:

> what objects can live in the zero-tax, mechanism-kernel equality manifold?

The next program step should test:

- bounded ancient state + kernel saturation;
- degree-one defect measure + kernel saturation;
- zero-tax multi-profile splitting;
- return-map uniqueness/compact invariant sets.

---

# 40. Updated M-TR status

### return-map semantics

$$
\boxed{
\mathrm{DEFINED}.
}
$$

### abstract minimal return rigidity

$$
\boxed{
\mathrm{PROVED\ CONDITIONAL}.
}
$$

### profile transition invariance

$$
\boxed{
\mathrm{OPEN/PARTIAL}.
}
$$

### actual return realization

$$
\boxed{
\mathrm{OPEN}.
}
$$

### profile splitting

$$
\boxed{
\text{minimal equality structure identified;}
}
$$

full NS package decomposition remains open.

---

# 41. Updated M-RIG status

The first equality-manifold normal forms are:

$$
\boxed{
\text{zero-return-tax state profile},
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
\text{degree-one parabolic defect measure}.
}
$$

No universal exclusion theorem is proved.

Thus:

$$
\boxed{
M\mbox{-}RIG
:
\mathrm{ENTERED/OPEN}.
}
$$

---

# 42. Next paper

The next paper should finally attack the equality manifold:

$$
\boxed{
\textbf{
NS-MORP 04 —
Ancient-State Kernel Rigidity、
Degree-One Defect Measures、
Zero-Tax Splitting
與 Minimal Obstruction Exclusion Audit
}.
}
$$

Primary tasks:

1. intersect the Type-I ancient state class with PFET/model-cone/filtered-increment kernel conditions;
2. test Liouville/backward-uniqueness theorems on the state-visible minimal branch;
3. classify parabolically degree-one dissipation defect measures compatible with suitable-weak local energy inequalities;
4. test whether zero filtered-increment recurrence forces local spatial rigidity;
5. determine whether minimal equality splitting can survive transition uniqueness or a strict splitting tax;
6. decide whether any nonzero equality-manifold obstruction remains.

---

# 43. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{normalized return transition semantics}
&:\ \mathrm{DEFINED},\\
\text{Minimal Return Rigidity}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Minimal Profile Splitting Saturation}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Strict-Dichotomy Exclusion}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Type-I ancient-state route}
&:\ \mathrm{EXTERNAL/CONDITIONAL},\\
\text{renormalized fixed-point state normal form}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{Defect Fixed-Point Homogeneity}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{No Point-Atom Defect Fixed Point}
&:\ \mathrm{PROVED},\\
\text{profile transition invariance}
&:\ \mathrm{OPEN/PARTIAL},\\
\text{actual return realization}
&:\ \mathrm{OPEN},\\
\text{full custom-package profile decomposition}
&:\ \mathrm{OPEN},\\
M\mbox{-}XTR
&:\ \mathrm{OPEN},\\
M\mbox{-}COM
&:\ \mathrm{PARTIAL/SUBSTANTIAL},\\
M\mbox{-}TR
&:\ \mathrm{OPEN/PARTIAL},\\
M\mbox{-}RIG
&:\ \mathrm{ENTERED/OPEN},\\
\text{unconditional minimal NS obstruction existence}
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

# 44. Conclusion

MORP-03 gives the first genuine dynamical normal forms for a hypothetical minimal obstruction.

The correct transition is a return/re-root map on native-separated windows, not a rigid fixed-time-step map.

If a minimizer returns to the normalized obstruction slice and the PDE ledger has nonnegative net depletion, minimality forces the entire return tax to vanish.

Thus a recurrent minimal obstruction lives on a zero-depletion equality manifold.

Profile splitting is also sharply constrained.

Under additive carrier/cost decoupling, every nonzero profile in a minimizing split must itself attain the same minimal obstruction ratio.

Single-profile selection therefore requires a strict splitting tax, uniqueness, or another rigidity input.

On the state-visible Type-I branch, external singular rescaling theory supplies a route to nontrivial bounded mild ancient solutions.

If the minimal return is unique modulo symmetry, the ancient state becomes a discrete renormalization fixed point.

On the defect-only branch, a pure-scaling return fixed point forces the dissipation defect measure to obey parabolic degree-one homogeneity.

Such a defect cannot be a point atom at the singular center.

Therefore the minimal obstruction problem has moved into an explicit equality-manifold classification problem:

$$
\boxed{
\textbf{
ancient state
\;\vee\;
minimal equality splitting
\;\vee\;
degree-one recurrent defect.
}
}
$$

The next paper attacks those objects directly.

---

# References

1. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier--Stokes regularity criterion*, arXiv:1012.0145.
2. C. E. Kenig, G. S. Koch, *An alternative approach to regularity for the Navier--Stokes equations in critical spaces*, arXiv:0908.3349.
3. W. Rusin, V. Šverák, *Minimal initial data for potential Navier--Stokes singularities*, arXiv:0911.0500.
4. H. Jia, V. Šverák, *Minimal $L^3$-initial data for potential Navier--Stokes singularities*, arXiv:1201.1592.
5. D. Albritton, T. Barker, *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, arXiv:1811.00502.
6. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
7. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
8. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560.
9. `NS_MORP_01_MinimalObstruction_Rigidity_v0.1.md`.
10. `NS_MORP_02_NativeExtraction_Compactness_v0.1.md`.
