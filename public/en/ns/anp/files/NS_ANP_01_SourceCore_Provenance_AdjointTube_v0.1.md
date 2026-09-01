---
title: "Navier–Stokes Ancestry Necessity Program 01: Source–Core Provenance, Adjoint Causal Tubes, Scale-Resolved Vorticity Renewal and the C2→C3 Gap"
short_title: "NS-ANP 01"
series: "Navier–Stokes Ancestry Necessity Program"
cycle: "IV"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style weighted source-core provenance / geometric-parent provenance reduction"
epistemic_status: "Constructs a terminal-core-anchored adjoint causal footprint for the vorticity equation and proves exact forward localized enstrophy and high-pass enstrophy identities. These identities provide a genuine C2 PDE-causal contribution from earlier vortex-stretching/scale-transfer source to a later Type-I core observable, or else force backward inheritance/re-rooting of earlier weighted state. Under the Type-I weak-L3 bound, the adjoint footprint has conserved mass, core-scale high-influence volume, and a centroid that remains within O_M(R) of the singular center over one parabolic time. Thus output-local source-core provenance is proved in a weighted adjoint sense. What remains open is geometric parent-source localization into a controlled same-core ball/tube, suppression of diffuse low-influence source contribution, and recursive reuse of the selected parent as the next canonical core node. Full C3 provenance, Chain Necessity, Finite Obstruction, and Navier-Stokes regularity are NOT proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Ancestry Necessity Program 01

# Source–Core Provenance, Adjoint Causal Tubes, Scale-Resolved Vorticity Renewal and the C2→C3 Gap

## 0. Goal of this paper

ANP-00 defined a proved recursive causal ancestry edge as a C3 edge:

$$
\boxed{
\text{forward PDE contribution}
+
\text{same-branch provenance}
+
\text{recursive parent legality}.
}
$$

The Type-I DRC architecture already gives:

- a later singular-core state;
- a local absolute ultraviolet lower bound;
- a global high-pass state;
- node-wise global source ancestry.

The unresolved question is:

> Can the source ancestry be tied to the later singular core itself?

This paper proves a first rigorous provenance bridge by changing the dynamical representation.

Instead of localizing the pressure-containing strain equation directly, we use the pressure-free vorticity equation and a terminal-core-anchored adjoint cutoff.

The result is an exact **weighted forward causal provenance identity**.

---

# 1. Pre-singularity Type-I setting

Normalize a candidate Type-I singular point to:

$$
(x_\ast,T_\ast)
=
(0,0).
$$

Assume:

$$
\boxed{
\|u\|_{L_t^\infty L_x^{3,\infty}}
\le
M
}
$$

on the pre-singularity interval under consideration.

Fix a later time:

$$
t_j<0
$$

and a Type-I core radius:

$$
R_j
\asymp_M
(-t_j)^{1/2}.
$$

Choose a smooth terminal cutoff:

$$
\chi_j(x)
=
\phi
\left(
\frac{x}{R_j}
\right),
$$

where:

$$
0\le\phi\le1,
$$

$$
\phi=1
\quad
\text{on }B_1,
$$

and:

$$
\operatorname{supp}\phi
\subset
B_2.
$$

Thus:

$$
\chi_j=1
\quad
\text{on }B_{R_j},
$$

and:

$$
\operatorname{supp}\chi_j
\subset
B_{2R_j}.
$$

---

# 2. Vorticity dynamics

For a smooth pre-singularity Navier--Stokes solution:

$$
\omega
=
\nabla\times u
$$

satisfies:

$$
\boxed{
\partial_t\omega
+
(u\cdot\nabla)\omega
=
S\omega
+
\nu\Delta\omega,
}
$$

where:

$$
S
=
\nabla_{\rm sym}u.
$$

The antisymmetric part of:

$$
\nabla u
$$

annihilates:

$$
\omega,
$$

so:

$$
(\omega\cdot\nabla)u
=
S\omega.
$$

This equation contains no pressure.

---

# 3. Terminal-core adjoint cutoff

For:

$$
t_i<t_j<T_\ast,
$$

solve:

$$
\boxed{
\partial_s\chi
+
u(s)\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
\qquad
\chi(t_j)=\chi_j.
}
$$

Equivalently, in reverse time:

$$
\tau=t_j-s,
$$

this is a forward advection--diffusion equation.

By the maximum principle:

$$
\boxed{
0\le
\chi(s,x)
\le1.
}
$$

The function:

$$
\chi(s,x)
$$

is called the:

$$
\boxed{
\textbf{adjoint causal footprint}
}
$$

of the later core observable.

---

# 4. Weighted enstrophy observable

Define:

$$
\boxed{
E_\chi(s)
=
\frac12
\int_{\mathbb R^3}
\chi(s,x)
|\omega(s,x)|^2dx.
}
$$

At the later endpoint:

$$
E_\chi(t_j)
\ge
\frac12
\int_{B_{R_j}}
|\omega(t_j,x)|^2dx.
$$

Hence the Barker--Prange Type-I core lower bound gives:

$$
\boxed{
R_j
E_\chi(t_j)
\ge
cM^2.
}
$$

---

# 5. Causal identity for full vorticity

Set:

$$
e_\omega
=
\frac12|\omega|^2.
$$

The vorticity equation gives:

$$
\boxed{
\partial_t e_\omega
+
u\cdot\nabla e_\omega
=
\omega\cdot S\omega
+
\nu\Delta e_\omega
-
\nu|\nabla\omega|^2.
}
$$

---

# 6. CIV-1.1 — Exact Adjoint-Core Enstrophy Provenance

## Theorem 6.1

For every:

$$
t_i<t_j<T_\ast,
$$

$$
\boxed{
E_\chi(t_j)
=
E_\chi(t_i)
+
\mathcal S_\chi[t_i,t_j]
-
\mathcal D_\chi[t_i,t_j],
}
$$

where:

$$
\boxed{
\mathcal S_\chi[t_i,t_j]
=
\int_{t_i}^{t_j}
\int
\chi
\,
\omega\cdot S\omega
\,dx\,ds,
}
$$

and:

$$
\boxed{
\mathcal D_\chi[t_i,t_j]
=
\nu
\int_{t_i}^{t_j}
\int
\chi
|\nabla\omega|^2
\,dx\,ds
\ge0.
}
$$

### Proof

Differentiate:

$$
E_\chi(s)
=
\int
\chi e_\omega.
$$

Use the vorticity enstrophy equation and the adjoint equation.

The advection terms cancel exactly by:

$$
\nabla\cdot u=0.
$$

The two diffusion terms cancel by integration by parts.

The only remaining terms are local vortex stretching and viscous enstrophy dissipation.

$\square$

---

# 7. Why Theorem 6.1 is causal

The identity is forward in physical time:

$$
t_i
<
s
<
t_j
<
T_\ast.
$$

The earlier field:

$$
\omega(s),
S(s)
$$

contributes through the exact Navier--Stokes vorticity dynamics to the later core observable:

$$
E_\chi(t_j).
$$

The fact that:

$$
\chi
$$

was constructed backward from the terminal core is inferential/adjoint bookkeeping.

It does not reverse the physical causal arrow.

Thus:

$$
\boxed{
\text{backward adjoint footprint}
+
\text{forward vorticity dynamics}
}
$$

forms a causal-closure square.

---

# 8. Exact normalized causal accounting

Assume:

$$
E_\chi(t_j)>0.
$$

Define:

$$
\boxed{
\eta_{\rm inh}
=
\frac{
E_\chi(t_i)
}{
E_\chi(t_j)
},
}
$$

$$
\boxed{
\eta_{\rm str}
=
\frac{
\mathcal S_\chi[t_i,t_j]
}{
E_\chi(t_j)
},
}
$$

and:

$$
\boxed{
\eta_{\rm diss}
=
\frac{
\mathcal D_\chi[t_i,t_j]
}{
E_\chi(t_j)
}.
}
$$

Then Theorem 6.1 becomes:

$$
\boxed{
1
=
\eta_{\rm inh}
+
\eta_{\rm str}
-
\eta_{\rm diss}.
}
$$

This is an exact dimensionless causal ledger.

---

# 9. CIV-1.2 — Stretching Source / Inheritance Dichotomy

## Theorem 9.1

Fix:

$$
0<\theta<1.
$$

At least one of:

### INHERIT

$$
\boxed{
\eta_{\rm inh}
>
1-\theta;
}
$$

### STRETCH-SOURCE

$$
\boxed{
\eta_{\rm str}
\ge
\theta
+
\eta_{\rm diss}
\ge
\theta
}
$$

holds.

### Proof

If INHERIT fails:

$$
\eta_{\rm inh}
\le
1-\theta.
$$

Use:

$$
1
=
\eta_{\rm inh}
+
\eta_{\rm str}
-
\eta_{\rm diss}.
$$

$\square$

---

# 10. Interpretation of the dichotomy

If STRETCH-SOURCE holds, the later core enstrophy has a quantitatively nontrivial forward local vortex-stretching source ancestor.

If INHERIT holds, the later core observable is already largely present in the earlier adjoint-weighted state and the ancestry node should be re-rooted backward.

This is the local-core analogue of the DRC old-stock/source-renewal dichotomy.

---

# 11. Scale-resolved Type-I UV state

Choose:

$$
J_j
$$

so:

$$
\boxed{
2^{J_j}
R_j
\asymp
1.
}
$$

Let:

$$
P_H
=
P_{>J_j},
$$

and:

$$
\boxed{
\omega_H
=
P_H\omega.
}
$$

DRC-06 gives:

$$
\boxed{
R_j
\|
\omega_H(t_j)
\|_{L^2(B_{R_j})}^2
\ge
cM^2.
}
$$

Define:

$$
\boxed{
E_{\chi,H}(s)
=
\frac12
\int
\chi(s,x)
|\omega_H(s,x)|^2dx.
}
$$

Then:

$$
\boxed{
R_j
E_{\chi,H}(t_j)
\ge
cM^2.
}
$$

---

# 12. High-pass vorticity equation

Applying:

$$
P_H
$$

to the vorticity equation gives:

$$
\boxed{
\partial_t\omega_H
+
u\cdot\nabla\omega_H
=
P_H(S\omega)
-
[P_H,u\cdot\nabla]\omega
+
\nu\Delta\omega_H.
}
$$

Define:

$$
\boxed{
\mathcal Q_H^{str}
=
P_H(S\omega),
}
$$

and:

$$
\boxed{
\mathcal Q_H^{tr}
=
-
[P_H,u\cdot\nabla]\omega.
}
$$

The second term is a genuine nonlinear scale-transfer/transport term.

It is not discarded as an error.

---

# 13. CIV-1.3 — Exact Scale-Resolved Adjoint Provenance

## Theorem 13.1

For:

$$
t_i<t_j<T_\ast,
$$

$$
\boxed{
E_{\chi,H}(t_j)
=
E_{\chi,H}(t_i)
+
\mathcal S_{\chi,H}^{str}
+
\mathcal S_{\chi,H}^{tr}
-
\mathcal D_{\chi,H},
}
$$

where:

$$
\boxed{
\mathcal S_{\chi,H}^{str}
=
\int_{t_i}^{t_j}
\int
\chi
\,
\omega_H\cdot
P_H(S\omega)
\,dx\,ds,
}
$$

$$
\boxed{
\mathcal S_{\chi,H}^{tr}
=
-
\int_{t_i}^{t_j}
\int
\chi
\,
\omega_H\cdot
[P_H,u\cdot\nabla]\omega
\,dx\,ds,
}
$$

and:

$$
\boxed{
\mathcal D_{\chi,H}
=
\nu
\int_{t_i}^{t_j}
\int
\chi
|\nabla\omega_H|^2
\,dx\,ds.
}
$$

### Proof

Use the high-pass vorticity equation and the same adjoint cancellation as in Theorem 6.1.

$\square$

---

# 14. Scale-resolved causal accounting

Define:

$$
\eta_{\rm inh}^H
=
\frac{
E_{\chi,H}(t_i)
}{
E_{\chi,H}(t_j)
},
$$

$$
\eta_{\rm str}^H
=
\frac{
\mathcal S_{\chi,H}^{str}
}{
E_{\chi,H}(t_j)
},
$$

$$
\eta_{\rm tr}^H
=
\frac{
\mathcal S_{\chi,H}^{tr}
}{
E_{\chi,H}(t_j)
},
$$

and:

$$
\eta_{\rm diss}^H
=
\frac{
\mathcal D_{\chi,H}
}{
E_{\chi,H}(t_j)
}.
$$

Then:

$$
\boxed{
1
=
\eta_{\rm inh}^H
+
\eta_{\rm str}^H
+
\eta_{\rm tr}^H
-
\eta_{\rm diss}^H.
}
$$

---

# 15. CIV-1.4 — UV Source / Inheritance Dichotomy

## Theorem 15.1

Fix:

$$
0<\theta<1.
$$

At least one of:

### UV-INHERIT

$$
\boxed{
\eta_{\rm inh}^H
>
1-\theta;
}
$$

### UV-SOURCE

$$
\boxed{
\eta_{\rm str}^H
+
\eta_{\rm tr}^H
\ge
\theta
+
\eta_{\rm diss}^H
\ge
\theta
}
$$

holds.

Moreover on UV-SOURCE at least one positive source channel satisfies:

$$
\boxed{
[
\eta_{\rm str}^H]_+
\ge
\theta/2
}
$$

or:

$$
\boxed{
[
\eta_{\rm tr}^H]_+
\ge
\theta/2.
}
$$

$\square$

---

# 16. Causal interpretation of the two UV channels

### Stretching channel

$$
P_H(S\omega)
$$

creates or redistributes high-frequency vorticity through vortex stretching.

### Scale-transfer channel

$$
-[P_H,u\cdot\nabla]\omega
$$

records cross-threshold nonlinear transport that appears because the advective dynamics and high-pass representation do not commute.

Thus UV source ancestry is explicitly split into:

$$
\boxed{
\text{stretching}
\vee
\text{scale transfer}.
}
$$

---

# 17. Adjoint footprint mass

Define:

$$
\boxed{
m_\chi(s)
=
\int_{\mathbb R^3}
\chi(s,x)\,dx.
}
$$

---

# 18. CIV-1.5 — Adjoint Mass Conservation

## Theorem 18.1

For:

$$
s\in[t_i,t_j],
$$

$$
\boxed{
m_\chi(s)
=
m_\chi(t_j)
=
m_j.
}
$$

Since the terminal cutoff is supported in:

$$
B_{2R_j},
$$

$$
\boxed{
m_j
\asymp
R_j^3.
}
$$

### Proof

Integrate the adjoint equation over space and use:

$$
\nabla\cdot u=0.
$$

$\square$

---

# 19. High-influence volume

For:

$$
0<\alpha<1,
$$

define:

$$
\boxed{
\Omega_\alpha(s)
=
\{
x:
\chi(s,x)\ge\alpha
\}.
}
$$

By Markov's inequality:

$$
\boxed{
|\Omega_\alpha(s)|
\le
\frac{
m_j
}{
\alpha
}
\lesssim
\alpha^{-1}
R_j^3.
}
$$

Thus the high-influence part of the causal footprint has core-scale volume.

It need not yet be one connected ball.

---

# 20. Adjoint centroid

Define:

$$
\boxed{
c_\chi(s)
=
\frac1{m_j}
\int
x
\chi(s,x)\,dx.
}
$$

At the terminal time, for a radial cutoff centered at:

$$
0,
$$

$$
c_\chi(t_j)=0.
$$

---

# 21. Centroid evolution

Differentiating the first moment gives:

$$
\boxed{
\frac{d}{ds}
c_\chi(s)
=
\frac1{m_j}
\int
u(s,x)
\chi(s,x)\,dx.
}
$$

The diffusion contribution to the first moment vanishes.

---

# 22. Lorentz estimate for the footprint

For:

$$
0\le\chi\le1
$$

with:

$$
\|\chi\|_1=m_j,
$$

the distribution-function estimate gives:

$$
\boxed{
\|\chi\|_{L^{3/2,1}}
\le
C
m_j^{2/3}.
}
$$

Lorentz Hölder then yields:

$$
\boxed{
\left|
\int
u\chi
\right|
\le
C
\|u\|_{L^{3,\infty}}
m_j^{2/3}.
}
$$

---

# 23. CIV-1.6 — Type-I Adjoint Centroid Control

## Theorem 23.1

Under:

$$
\|u\|_{L_t^\infty L_x^{3,\infty}}
\le
M,
$$

$$
\boxed{
\left|
\frac{d}{ds}
c_\chi(s)
\right|
\le
C
M
m_j^{-1/3}
\lesssim
C_\phi
\frac{
M
}{
R_j
}.
}
$$

Hence if:

$$
0\le
t_j-s
\le
\vartheta
R_j^2,
$$

then:

$$
\boxed{
|c_\chi(s)|
\le
C_\phi
M
\vartheta
R_j.
}
$$

### Meaning

Over one fixed parabolic-time fraction, the centroid of the terminal-core causal footprint remains within a controlled multiple of the terminal core radius.

$\square$

---

# 24. Causal footprint aperture

Define the second-moment aperture:

$$
\boxed{
A_\chi(s)^2
=
\frac1{
m_jR_j^2
}
\int
|x-c_\chi(s)|^2
\chi(s,x)\,dx.
}
$$

This dimensionless quantity measures geometric spread/filamentation of the adjoint footprint.

The current paper does **not** prove a universal bound:

$$
A_\chi(s)
\le
A_0(M)
$$

on all required ancestry intervals.

Thus center control is stronger than full geometric-tube control.

---

# 25. High-influence causal tube

Define:

$$
\boxed{
\mathcal T_{\alpha,j}
=
\{
(s,x):
t_i\le s\le t_j,
\quad
\chi(s,x)\ge\alpha
\}.
}
$$

Its slices have:

- core-scale volume:
  $$
  |\Omega_\alpha(s)|
  \lesssim
  \alpha^{-1}R_j^3;
  $$
- controlled centroid drift over:
  $$
  O(R_j^2)
  $$
  time.

The unresolved geometry is the aperture/connectivity of those slices.

---

# 26. Weighted source-core provenance

The source identities of Theorems 6.1 and 13.1 are already anchored to the later core because:

$$
\chi(t_j)=\chi_j.
$$

Every source term is integrated against the unique adjoint footprint generated by that terminal observable.

Define:

$$
\boxed{
\textbf{SCPB-W}
}
$$

as **weighted output-local Source--Core Provenance**.

---

# 27. CIV-1.7 — Weighted Source--Core Provenance Theorem

## Theorem 27.1

For every later Type-I core observable with terminal cutoff:

$$
\chi_j,
$$

and every earlier:

$$
t_i<t_j,
$$

the Navier--Stokes vorticity equation supplies an exact forward C2 causal relation:

$$
\boxed{
\text{earlier weighted state/source on the adjoint footprint}
\overset{\rm PDE}{\longrightarrow}
\text{later core enstrophy}.
}
$$

At the UV level:

$$
\boxed{
\text{earlier weighted high-pass state}
+
\text{weighted stretching}
+
\text{weighted scale transfer}
\overset{\rm PDE}{\longrightarrow}
\text{later UV core}.
}
$$

The relation is terminal-core provenance anchored by:

$$
\chi(t_j)=\chi_j.
$$

### Status

$$
\boxed{
\text{SCPB-W}
:
\mathrm{PROVED}.
}
$$

$\square$

---

# 28. What SCPB-W does not prove

SCPB-W does not prove that the **parent fields generating the projected source** all lie inside a fixed same-center ball.

The high-pass operator and nonlinear parent decomposition remain spatially nonlocal representations.

It also does not prove that the earlier adjoint-weighted state is itself one of the canonical Barker--Prange core nodes.

These are stronger provenance claims.

---

# 29. Geometric source-core provenance

Define:

$$
\boxed{
\textbf{SCPB-G}
}
$$

as the statement that a fixed fraction of the relevant source contribution can be localized to a controlled enlargement:

$$
B_0(A R_j)
$$

or to a uniformly controlled core-scale tube around the same singular center.

This requires quantitative control of:

- adjoint aperture;
- diffuse low-influence source tails;
- parent-field pseudolocality.

Current status:

$$
\boxed{
\text{SCPB-G}
:
\mathrm{OPEN}.
}
$$

---

# 30. Diffuse-tail ledger

For:

$$
0<\alpha<1,
$$

split a source integrand:

$$
F(s,x)
$$

into:

$$
\chi F
=
\mathbf 1_{
\chi\ge\alpha
}
\chi F
+
\mathbf 1_{
\chi<\alpha
}
\chi F.
$$

Define the positive-gross tail fraction:

$$
\boxed{
\mathfrak L_\alpha^{tail}
=
\frac{
\displaystyle
\int
\mathbf 1_{
\chi<\alpha
}
[
\chi F
]_+
}{
\displaystyle
\int
[
\chi F
]_+
}
}
$$

when the denominator is positive.

A small:

$$
\mathfrak L_\alpha^{tail}
$$

would upgrade weighted provenance toward a high-influence causal tube.

No universal smallness theorem is proved here.

---

# 31. Parent-locality ledger

For a chosen projected source channel define:

$$
\boxed{
\mathfrak L^{par}
}
$$

as the fraction of its realized source contribution requiring parent state outside the selected controlled core enlargement.

The exact definition depends on the dyadic/physical-space source decomposition used in ANP-02.

Current status:

$$
\boxed{
\mathfrak L^{par}
:
\mathrm{DEFINED\ AS\ TARGET/OPEN}.
}
$$

---

# 32. Recursive core recapture

Define:

$$
\boxed{
\textbf{SCPB-R}
}
$$

as the requirement that the earlier inherited/source-backed state selected by the adjoint provenance identity can be converted into the next canonical core node with:

- controlled center;
- controlled radius;
- controlled frequency;
- nontrivial absolute UV stock.

This is precisely the interface to Recursive Edge Compatibility.

Current status:

$$
\boxed{
\text{SCPB-R}
:
\mathrm{OPEN}.
}
$$

---

# 33. Causal level of the proved edge

Theorem 27.1 has:

### Time legality

PASS.

### Same-solution PDE legality

PASS.

### Terminal-core output provenance

PASS.

### Quantitative source relevance

PASS on the source branch.

### Scale resolution

PASS through the high-pass identity.

### Geometric same-core parent localization

OPEN.

### Recursive parent legality

OPEN.

Therefore:

$$
\boxed{
\mathsf{CAUSE}
=
C2
}
$$

with proved terminal-core provenance, but not:

$$
C3.
$$

---

# 34. Causal Atom for the UV source branch

For a UV-SOURCE edge define:

$$
\boxed{
\mathfrak A_{i\to j}^{UV}
}
$$

with the following fields.

## ST

$$
(
t_i,t_j,T_\ast,
0,c_\chi,
R_j,
J_j
).
$$

## REL

$$
\{
\mathrm{EVO},
\mathrm{SRC},
\mathrm{SCALE},
\mathrm{PROV}
\}.
$$

## EX

- solution: PROVED/assumed smooth pre-singularity;
- later node: PROVED;
- weighted source edge: PROVED;
- recursive chain: OPEN.

## DEF

Terminal-core high-pass vorticity observable with adjoint footprint.

## JUD

$$
(
\mathrm{PASS},
\mathrm{PASS},
\mathrm{PASS},
\mathrm{PASS},
\mathrm{PASS},
\mathrm{PASS\mbox{-}W},
\mathrm{OPEN}
).
$$

## DYN

Exact high-pass vorticity equation.

## NUM

Contains:

$$
\Pi_{JR}
\asymp1,
$$

$$
\Pi_\nu
=
\nu
2^{2J_j}
(t_j-t_i),
$$

source ratios:

$$
\eta_{\rm str}^H,
\eta_{\rm tr}^H,
$$

core stock:

$$
R_jE_{\chi,H}(t_j),
$$

centroid drift:

$$
|c_\chi|/R_j,
$$

aperture:

$$
A_\chi,
$$

and tail ledger:

$$
\mathfrak L_\alpha^{tail}.
$$

---

# 35. Continuity and discreteness status

The edge is embedded in the full continuous pre-singularity vorticity trajectory:

$$
\omega(s),
\qquad
s\in[t_i,t_j].
$$

The graph node:

$$
K_j
$$

and high-pass threshold:

$$
J_j
$$

are discrete proof/representation objects.

Thus:

$$
\boxed{
\mathsf{CONT}
:
\mathrm{PASS},
\qquad
\mathsf{DISC}
:
\mathrm{PASS/HYBRID}.
}
$$

---

# 36. Coupling status

The UV edge has:

### Equation coupling

Exact.

### Amplitude coupling

Quantified by:

$$
\eta_{\rm str}^H+\eta_{\rm tr}^H.
$$

### Spatial output coupling

Exact through:

$$
\chi.
$$

### Scale coupling

Exact at the high-pass representation level.

### Parent spatial coupling

OPEN.

Thus coupling is mixed rather than globally PASS/FAIL.

---

# 37. Phase-like source regimes

For:

$$
0<\theta<1,
$$

define:

### INHERITED-CORE

$$
\eta_{\rm inh}^H
>
1-\theta.
$$

### STRETCH-RENEWAL

$$
[\eta_{\rm str}^H]_+
\ge
\theta/2.
$$

### TRANSFER-RENEWAL

$$
[\eta_{\rm tr}^H]_+
\ge
\theta/2.
$$

### DEPLETION-DOMINANT

Large:

$$
\eta_{\rm diss}^H
$$

must be paid in addition to source renewal.

These are pre-singularity causal regimes.

They are not thermodynamic phases.

---

# 38. Predictability status

The exact accounting gives a P2-type conditional forecast:

if at an earlier time:

$$
\eta_{\rm inh}^H
\le
1-\theta,
$$

and a later UV core reaches the prescribed target level, then the intervening source channels must supply at least:

$$
\theta
$$

of the normalized target, plus dissipation replacement.

This predicts a **minimum required source debt conditional on the target**.

It does not predict that the singularity will occur.

---

# 39. Interpretability status

For the weighted UV source edge:

### WHEN

Known:

$$
[t_i,t_j].
$$

### WHERE

Adjoint causal footprint:

$$
\chi(s,x).
$$

### SCALE

Known:

$$
J_j,
\qquad
2^{J_j}R_j\asymp1.
$$

### WHAT

High-pass vorticity.

### HOW

Vortex stretching and nonlinear scale transfer.

### HOW MUCH

Exact normalized ratios:

$$
\eta_{\rm str}^H,
\eta_{\rm tr}^H,
\eta_{\rm diss}^H.
$$

### WHY LEGAL

Exact vorticity PDE plus adjoint identity.

Thus the edge is highly interpretable, with parent geometric localization explicitly marked OPEN rather than hidden.

---

# 40. Output-local versus parent-local provenance

This distinction is now mandatory.

## Output-local provenance

The source is proven to contribute to the specific later core observable.

Status:

$$
\boxed{
\mathrm{PROVED}.
}
$$

## Parent-local provenance

The parent fields responsible for the source are proven to belong to the same compact/nested core branch.

Status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

The original SCPB problem was ambiguous because it combined these two claims.

---

# 41. Causal provenance decomposition theorem

## Theorem 41.1

The original Source--Core Provenance Bridge decomposes as:

$$
\boxed{
\mathrm{SCPB}
=
\mathrm{SCPB\mbox{-}W}
+
\mathrm{SCPB\mbox{-}G}
+
\mathrm{SCPB\mbox{-}R},
}
$$

where:

- SCPB-W: weighted terminal-core output provenance;
- SCPB-G: geometric same-core parent/source localization;
- SCPB-R: recursive core recapture.

Current status:

$$
\boxed{
\mathrm{SCPB\mbox{-}W}
:
\mathrm{PROVED},
}
$$

$$
\boxed{
\mathrm{SCPB\mbox{-}G}
:
\mathrm{OPEN},
}
$$

$$
\boxed{
\mathrm{SCPB\mbox{-}R}
:
\mathrm{OPEN}.
}
$$

Thus ANP-01 partially closes Source--Core Provenance without overclaiming C3 ancestry.

$\square$

---

# 42. Relation to Barker--Prange

Barker--Prange supply quantitative Type-I spatial concentration and backward propagation of dangerous local structure.

The adjoint provenance identity supplies a complementary forward causal accounting from earlier local/weighted vorticity dynamics to a later core observable.

The two directions now form:

$$
\boxed{
\text{backward necessary core structure}
\quad
\leftrightarrow
\quad
\text{forward weighted causal source}.
}
$$

The remaining mismatch is geometric parent localization and recursive node recapture.

---

# 43. Relation to Tao quantitative propagation

Tao's quantitative critical:

$$
L^3
$$

work demonstrates that backward propagation/unique-continuation arguments can be made quantitative.

ANP-01 uses a different but compatible idea:

the backward object is an **adjoint terminal observable**,

while the causal source relation remains forward through the exact vorticity equation.

No Tao Carleman estimate is imported into Theorems 6.1--41.1.

---

# 44. Why pressure nonlocality is not hidden

The full/filtered vorticity equation avoids an explicit pressure term.

This is one reason it is a better causal representation for Source--Core Provenance than a naively localized strain equation.

However high-pass filtering still introduces a nonlocal representation and a commutator scale-transfer term.

ANP-01 keeps that term explicitly.

Thus:

$$
\boxed{
\text{pressure removed}
\neq
\text{all nonlocality removed}.
}
$$

---

# 45. Recursive edge frontier

The next required theorem is not another weighted identity.

It must convert an earlier adjoint-weighted state/source branch into a canonical reusable ancestry node.

This requires:

1. geometric footprint control;
2. parent localization;
3. stable radius/scale update;
4. preservation of absolute state stock;
5. no semantic reset.

This is:

$$
\boxed{
\textbf{Recursive Edge Compatibility}.
}
$$

---

# 46. ANP-02 target

The next paper should be:

$$
\boxed{
\textbf{
NS-ANP 02 —
Recursive Edge Compatibility,
Adjoint-Footprint Recapture,
Parent Localization
and Canonical Core Transition
}.
}
$$

Primary tasks:

1. control or classify:
   $$
   A_\chi(s);
   $$
2. control:
   $$
   \mathfrak L_\alpha^{tail};
   $$
3. define a parent-locality ledger for filtered source channels;
4. convert an adjoint-weighted earlier state into a canonical core/high-pass node;
5. prove a stable transition map:
   $$
   T_{\rm adjoint\ state\to core};
   $$
6. determine whether the weighted C2 provenance edge upgrades to C3.

---

# 47. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{terminal-core adjoint footprint}
&:\ \mathrm{DEFINED},\\
\text{exact local enstrophy provenance identity}
&:\ \mathrm{PROVED},\\
\text{stretching/inheritance dichotomy}
&:\ \mathrm{PROVED},\\
\text{exact high-pass provenance identity}
&:\ \mathrm{PROVED},\\
\text{UV source/inheritance dichotomy}
&:\ \mathrm{PROVED},\\
\text{adjoint mass conservation}
&:\ \mathrm{PROVED},\\
\text{high-influence core-scale volume}
&:\ \mathrm{PROVED},\\
\text{Type-I adjoint centroid control}
&:\ \mathrm{PROVED},\\
\text{SCPB-W weighted output provenance}
&:\ \mathrm{PROVED},\\
\text{SCPB-G geometric parent localization}
&:\ \mathrm{OPEN},\\
\text{SCPB-R recursive core recapture}
&:\ \mathrm{OPEN},\\
\text{C2 causal source-core edge}
&:\ \mathrm{PROVED},\\
\text{C3 recursive causal ancestry edge}
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

# 48. Conclusion

ANP-01 gives the first genuinely causal Source--Core Provenance theorem in the program.

A later Type-I core defines a terminal observable.

Its backward adjoint cutoff creates a causal footprint.

The forward vorticity equation then gives the exact identity:

$$
\boxed{
\text{later core state}
=
\text{earlier inherited state}
+
\text{vortex-stretching source}
-
\text{viscous depletion}.
}
$$

At the high-pass level:

$$
\boxed{
\text{later UV core}
=
\text{earlier UV state}
+
\text{projected stretching}
+
\text{scale-transfer commutator}
-
\text{viscous depletion}.
}
$$

Thus the source is not merely globally correlated with the core.

It contributes to the exact terminal-core observable through the forward PDE.

Under the Type-I weak-$L^3$ bound, the adjoint footprint additionally has:

- conserved core-scale mass;
- core-scale high-influence volume;
- centroid displacement of only:
  $$
  O_M(R_j)
  $$
  over one parabolic time.

This establishes weighted output-local C2 provenance.

The unresolved step is geometric and recursive:

$$
\boxed{
\text{weighted causal footprint}
\quad\longrightarrow\quad
\text{canonical same-core parent node}.
}
$$

That is the precise target of ANP-02.

---

# References

1. T. Barker, C. Prange, *Quantitative regularity for the Navier--Stokes equations via spatial concentration*, Communications in Mathematical Physics 385 (2021), 717--792; arXiv:2003.06717.
2. T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487--1541; arXiv:1812.09115.
3. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
4. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, Pure and Applied Analysis 8 (2026), 247--270; arXiv:2407.02691.
5. `NS_ANP_00_PreSingularity_CausalRelationDomain_v0.1.md`.
6. `NS_DRC_06_PersistentCoreDilution_CoreReuse_v0.1.md`.
7. `NS_DRC_07_UnifiedReservoirCover_ChainNecessityAudit_v0.1.md`.