---
title: "Navier–Stokes C3-N: Localized Betchov Boundary Current and Strain Self-Amplification Local Balance"
subtitle: "Localized Betchov Currents, Boundary Compensation, and the Exact Local Strain Self-Amplification Balance"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Contains exact kinematic divergence identities and localized strain-energy balance. Uses external primary literature for Betchov divergence structure and strain dynamics. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-N
# Localized Betchov Boundary Current and Strain Self-Amplification Local Balance

## 0. Positioning of this Round

C3-M has established:

1. pointwise vortex stretching:

$$
\alpha
=
\xi\cdot S\xi
=
\lambda_2
+
(\lambda_3-\lambda_2)c_3
-
(\lambda_2-\lambda_1)c_1;
$$

2. global Betchov relation:

$$
\int
\omega\cdot S\omega\,dx
=
-4
\int
\det S\,dx;
$$

3. thus, global integration collapses the vorticity–strain orientation information;

4. the truly worthwhile quantity to study is the localized one:

$$
\int
\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)dx.
$$

In the previous round, it was only known that:

> local surplus must be globally compensated outside the core.

This round formally closes this issue:

$$
\boxed{
\text{the localized Betchov mismatch itself is an exact spatial divergence current}.
}
$$

Therefore, it is not merely "compensated somewhere else",

but rather:

$$
\boxed{
\text{it must pass through the localization boundary}.
}
$$

Furthermore, the localized full strain equation can be exactly written as:

$$
\boxed{
\text{bulk strain self-amplification}
+
\text{boundary/gauge corrections}.
}
$$

This transforms the geometry debt of C3-M into a true local balance law for the first time.

---

# 1. Setup

Consider a smooth divergence-free velocity:

$$
u:\mathbb R^3\times[0,T)\to\mathbb R^3,
$$

$$
\nabla\cdot u=0.
$$

Define the velocity gradient:

$$
\boxed{
A_{ij}
=
\partial_j u_i.
}
$$

Decomposition:

$$
A=S+\Omega,
$$

where:

$$
S
=
\frac12(A+A^\top),
$$

$$
\Omega
=
\frac12(A-A^\top).
$$

vorticity:

$$
\omega=\nabla\times u.
$$

Due to incompressibility:

$$
\operatorname{tr}A
=
\operatorname{tr}S
=
0.
$$

---

# 2. Pointwise algebra: $A^3$ and Betchov density

The antisymmetric part satisfies:

$$
\Omega^2
=
\frac14
\left(
\omega\otimes\omega
-
|\omega|^2I
\right).
$$

Thus:

$$
\operatorname{tr}(S\Omega^2)
=
\frac14
\omega\cdot S\omega
$$

Since:

$$
\operatorname{tr}S=0.
$$

Expanding:

$$
\operatorname{tr}(A^3)
=
\operatorname{tr}(S^3)
+
3\operatorname{tr}(S\Omega^2).
$$

For a trace-free $3\times3$ symmetric matrix:

$$
\operatorname{tr}(S^3)
=
3\det S.
$$

Hence:

$$
\boxed{
\operatorname{tr}(A^3)
=
3\det S
+
\frac34
\omega\cdot S\omega.
}
$$

Therefore:

$$
\boxed{
\omega\cdot S\omega
+
4\det S
=
\frac43
\operatorname{tr}(A^3).
}
$$

Define:

$$
\boxed{
b_B
=
\omega\cdot S\omega
+
4\det S.
}
$$

---

# 3. External kinematic input: $\operatorname{tr}(A^3)$ is a divergence

Carbone–Wilczek's analysis of the Betchov constraints explicitly states:

$$
\boxed{
\operatorname{tr}(A^3)
=
\nabla\cdot F_B,
}
$$

where:

$$
\boxed{
F_B
=
\left(
A^2
-
\frac12
\operatorname{tr}(A^2)I
\right)u.
}
$$

in component form:

$$
\boxed{
(F_B)_i
=
u_k
\partial_j u_i
\partial_k u_j
-
\frac12
u_i
\partial_k u_j
\partial_j u_k.
}
$$

Therefore:

$$
\boxed{
b_B
=
\frac43
\nabla\cdot F_B.
}
$$

This is a pointwise kinematic identity.

It does not use the Navier–Stokes time evolution.

---

# 4. C3-N.1: Localized Betchov Boundary Theorem

## Theorem 4.1

Let:

$$
\chi\in C_c^\infty(\mathbb R^3).
$$

Then:

$$
\boxed{
\int_{\mathbb R^3}
\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)dx
=
-\frac43
\int_{\mathbb R^3}
\nabla\chi\cdot F_B\,dx.
}
$$

### Proof

From:

$$
b_B
=
\frac43\nabla\cdot F_B,
$$

the result follows by integration by parts. $\square$

---

# 5. Sharp-domain form

If:

$$
\Omega\subset\mathbb R^3
$$

is a smooth bounded domain,

then the divergence theorem gives:

$$
\boxed{
\int_{\Omega}
\left(
\omega\cdot S\omega
+
4\det S
\right)dx
=
\frac43
\int_{\partial\Omega}
F_B\cdot n\,dS.
}
$$

Specifically for a ball:

$$
B_R(x_0),
$$

$$
\boxed{
\int_{B_R(x_0)}
\left(
\omega\cdot S\omega
+
4\det S
\right)dx
=
\frac43
\int_{\partial B_R(x_0)}
F_B\cdot n\,dS.
}
$$

Thus:

$$
\boxed{
\text{local Betchov mismatch = spatial boundary current}.
}
$$

---

# 6. What does this truly close?

C3-M defines:

$$
b_B
=
\omega\cdot S\omega
+
4\det S.
$$

global:

$$
\int b_B=0.
$$

Previously, it was only known that:

$$
\int\chi b_B
=
-
\int(1-\chi)b_B.
$$

This round establishes a stronger result:

$$
\boxed{
\int\chi b_B
}
$$

does not require knowledge of the entire exterior volume.

It is directly determined by:

$$
\boxed{
\nabla\chi\cdot F_B
}
$$

in the cutoff transition layer.

Therefore:

$$
\boxed{
\text{Betchov compensation is boundary-mediated, not arbitrary far-volume bookkeeping}.
}
$$

---

# 7. Boundary-current magnitude

From:

$$
F_B
=
\left(
A^2
-
\frac12\operatorname{tr}(A^2)I
\right)u,
$$

we have:

$$
\boxed{
|F_B|
\le
C
|u|
|\nabla u|^2.
}
$$

Thus:

## Corollary 7.1

$$
\boxed{
\left|
\int
\chi b_B
\right|
\le
C
\|\nabla\chi\|_\infty
\int_{\operatorname{supp}\nabla\chi}
|u|
|\nabla u|^2dx.
}
$$

---

# 8. Ball-scale estimate

Take:

$$
\chi_R(x)
=
\chi_0
\left(
\frac{x-x_0}{R}
\right),
$$

where:

$$
\chi_0=1
$$

on $B_1$,

and supported in:

$$
B_2.
$$

Then:

$$
|\nabla\chi_R|
\lesssim
R^{-1}.
$$

Let the transition annulus be:

$$
\mathcal A_R
=
B_{2R}(x_0)\setminus B_R(x_0).
$$

Then:

$$
\boxed{
\left|
\int
\chi_Rb_B
\right|
\le
\frac{C}{R}
\int_{\mathcal A_R}
|u|
|\nabla u|^2dx.
}
$$

---

# 9. Dimensionless boundary compensation

Define the annular critical velocity amplitude:

$$
\boxed{
a_R
=
\frac{
R
\|u\|_{L^\infty(\mathcal A_R)}
}{
\nu
}.
}
$$

Define the normalized annular gradient stock:

$$
\boxed{
d_R
=
\frac{
R
}{
\nu^2
}
\int_{\mathcal A_R}
|\nabla u|^2dx.
}
$$

Define the normalized localized Betchov defect:

$$
\boxed{
\widehat{\mathfrak B}_R
=
\frac{
R^3
}{
\nu^3
}
\left|
\int
\chi_Rb_Bdx
\right|.
}
$$

Then:

## Theorem 9.1

$$
\boxed{
\widehat{\mathfrak B}_R
\le
C
a_R
d_R.
}
$$

Thus, the local Betchov mismatch requires the boundary layer to simultaneously possess:

- a critical velocity amplitude;
- a gradient stock.

---

# 10. Companion: second Betchov invariant

Similarly:

$$
\operatorname{tr}(A^2)
=
|S|^2
-
\frac12|\omega|^2.
$$

And:

$$
\boxed{
\operatorname{tr}(A^2)
=
\nabla\cdot(Au).
}
$$

Since:

$$
(Au)_i
=
u_j\partial_j u_i.
$$

Thus:

## Theorem 10.1

$$
\boxed{
\int
\chi
\left(
|S|^2
-
\frac12|\omega|^2
\right)dx
=
-
\int
\nabla\chi\cdot(Au)\,dx.
}
$$

Therefore, the local strain/enstrophy magnitude mismatch is also a boundary current.

---

# 11. Localized Betchov pair

We now have two exact local identities:

$$
\boxed{
\int\chi
\left(
|S|^2
-
\frac12|\omega|^2
\right)
=
-\int\nabla\chi\cdot Au,
}
$$

and:

$$
\boxed{
\int\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)
=
-\frac43
\int\nabla\chi\cdot F_B.
}
$$

Thus:

$$
\boxed{
\text{magnitude balance}
+
\text{production balance}
}
$$

The global identities for both can be understood as the boundary currents vanishing in the whole-space limit.

---

# 12. External numerical interface

Encinar 2023's DNS / filtered velocity-gradient analysis of homogeneous isotropic turbulence found that:

- Betchov's strain/vorticity magnitude balance;
- vortex-stretching / strain-self-amplification production balance;

after local coarse-graining, typically achieve primary cancellation within a physical distance of a few filter widths;

the reported characteristic Betchov scale is approximately:

$$
O(3)
$$

filtered structure widths.

This document does not treat this numerical result as an arbitrary Navier–Stokes theorem.

However, Theorem 4.1 provides its exact kinematic interpretation:

$$
\boxed{
\text{local mismatch can only exist via a localization boundary current}.
}
$$

---

# 13. Strain equation

The full 3D N–S strain equation:

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
(u\cdot\nabla)S
+
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
=
0.
}
$$

Since:

$$
\operatorname{tr}S=0,
$$

the pairing of the $I$ term with $S$ is zero.

---

# 14. Nonlinear strain pairing

We have:

$$
S:S^2
=
\operatorname{tr}(S^3)
=
3\det S.
$$

and:

$$
S:
\left(
\frac14\omega\otimes\omega
\right)
=
\frac14
\omega\cdot S\omega.
$$

Thus:

$$
\boxed{
3\det S
+
\frac14\omega\cdot S\omega
=
2\det S
+
\frac14b_B.
}
$$

---

# 15. Pressure Hessian is also a divergence current

Define:

$$
\boxed{
F_p
=
\left(
\nabla^2p
-
\Delta p\,I
\right)u.
}
$$

Then:

## Lemma 15.1

$$
\boxed{
\nabla\cdot F_p
=
S:\nabla^2p.
}
$$

### Proof

Since:

$$
\nabla\cdot
\left(
\nabla^2p-\Delta p\,I
\right)
=
0,
$$

Thus:

$$
\nabla\cdot F_p
=
\left(
\nabla^2p-\Delta pI
\right):\nabla u.
$$

The Hessian is symmetric,

hence:

$$
\nabla^2p:\nabla u
=
\nabla^2p:S.
$$

And:

$$
\Delta p\,\operatorname{tr}\nabla u
=
0.
$$

$\square$

---

# 16. Moving cutoff

Let:

$$
\chi=\chi(t,x)
$$

be smooth and compactly supported.

Define the local strain energy:

$$
\boxed{
E_S^\chi(t)
=
\frac12
\int
\chi(t,x)
|S(x,t)|^2dx.
}
$$

---

# 17. C3-N.2: Exact Local Strain Self-Amplification Balance

## Theorem 17.1

For a smooth N–S solution:

$$
\boxed{
\frac d{dt}
E_S^\chi
+
\nu
\int
\chi
|\nabla S|^2dx
=
-2
\int
\chi
\det S\,dx
+
\mathcal C_\chi,
}
$$

where:

$$
\boxed{
\begin{aligned}
\mathcal C_\chi
={}&
\frac12
\int
|S|^2
\left(
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
\right)dx
\\
&+
\frac13
\int
\nabla\chi\cdot F_B\,dx
\\
&+
\int
\nabla\chi\cdot F_p\,dx.
\end{aligned}
}
$$

### Proof

Take the $L^2$ pairing of the strain equation with:

$$
\chi S
$$

---

## Time derivative

$$
\int
\chi S:\partial_tS
=
\frac12
\frac d{dt}
\int
\chi|S|^2
-
\frac12
\int
(\partial_t\chi)|S|^2.
$$

---

## Viscosity

$$
-\nu
\int
\chi S:\Delta S
=
\nu
\int
\chi|\nabla S|^2
-
\frac\nu2
\int
(\Delta\chi)|S|^2.
$$

---

## Advection

Since:

$$
\nabla\cdot u=0,
$$

$$
\int
\chi
S:(u\cdot\nabla S)
=
-\frac12
\int
|S|^2
u\cdot\nabla\chi.
$$

---

## Cubic nonlinear terms

$$
\int
\chi
\left[
3\det S
+
\frac14\omega\cdot S\omega
\right]
=
2
\int
\chi\det S
+
\frac14
\int
\chi b_B.
$$

And:

$$
\frac14
\int\chi b_B
=
-\frac13
\int\nabla\chi\cdot F_B.
$$

---

## Pressure

$$
\int
\chi
S:\nabla^2p
=
-
\int
\nabla\chi\cdot F_p.
$$

Rearranging yields the result. $\square$

---

# 18. Core meaning of this identity

In the local strain $L^2$ balance:

$$
\boxed{
-2\int\chi\det S
}
$$

is the only cubic production term retained in the **bulk volume**.

Others:

- the Betchov mismatch of vorticity interaction and self-amplification;
- advection;
- pressure Hessian;
- cutoff motion;
- viscous localization correction;

all enter into:

$$
\boxed{
\mathcal C_\chi
}
$$

this boundary/gauge correction package.

Therefore:

$$
\boxed{
\textbf{Local Strain Growth}
=
\textbf{Bulk Self-Amplification}
+
\textbf{Boundary/Transport Compensation}.
}
$$

---

# 19. Whole-space limit

Formally taking:

$$
\chi\to1
$$

and assuming the fields sufficiently decay,

then:

$$
\nabla\chi,
\quad
\Delta\chi,
\quad
\partial_t\chi
\to0.
$$

Thus:

$$
\mathcal C_\chi\to0.
$$

we recover:

$$
\boxed{
\frac12
\frac d{dt}
\|S\|_2^2
+
\nu
\|\nabla S\|_2^2
=
-2
\int
\det S.
}
$$

Equivalently:

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|\nabla S\|_2^2
-
4
\int\det S.
}
$$

This is the standard global strain-enstrophy identity.

---

# 20. Relationship with Miller strain decomposition

Miller writes the full strain equation as:

$$
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
+
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right)
=
0.
$$

In the global $L^2$ pairing, the second projected nonlinear package is orthogonal to $S$.

The strain self-amplification model:

$$
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
=
0
$$

retains the same global strain-enstrophy growth identity as the full N–S,

and this model can blow up in finite time for a family of initial data.

Theorem 17.1 of this round supplements this:

$$
\boxed{
\text{global orthogonality transforms into a boundary/gauge current after localization}.
}
$$

This does not mean that the local full N–S is equivalent to the self-amplification model.

The boundary package:

$$
\mathcal C_\chi
$$

can be of the same order as the bulk term, or even dominate.

---

# 21. Local production dichotomy

Define:

$$
\boxed{
\mathcal A_\chi
=
-2
\int
\chi\det S\,dx
}
$$

as the local bulk self-amplification.

Then:

$$
\boxed{
\frac d{dt}
E_S^\chi
+
\nu
\int\chi|\nabla S|^2
=
\mathcal A_\chi
+
\mathcal C_\chi.
}
$$

Therefore, if the local strain growth in a certain ancestry core is large,

it must at least be that:

$$
\boxed{
|\mathcal A_\chi|
\text{ large}
}
$$

or:

$$
\boxed{
|\mathcal C_\chi|
\text{ large}.
}
$$

This is merely an exact dichotomy,

not a regularity theorem.

---

# 22. Various forms of the boundary package

$$
\mathcal C_\chi
$$

contains at least:

## C-GAUGE

$$
\frac12
\int
|S|^2\partial_t\chi.
$$

moving core reclassification.

## C-ADV

$$
\frac12
\int
|S|^2u\cdot\nabla\chi.
$$

physical advection through the boundary.

## C-DIFF

$$
\frac\nu2
\int
|S|^2\Delta\chi.
$$

viscous boundary correction.

## C-BETCHOV

$$
\frac13
\int
\nabla\chi\cdot F_B.
$$

vortex-stretching / strain-self-amplification local mismatch current.

## C-PRESS

$$
\int
\nabla\chi\cdot F_p.
$$

pressure-Hessian boundary current.

---

# 23. Ball-scale correction bound

For a fixed:

$$
\chi_R,
$$

we obtain the schematic bound:

$$
\boxed{
\begin{aligned}
|\mathcal C_{\chi_R}|
\lesssim{}&
\frac{\nu}{R^2}
\int_{\mathcal A_R}
|S|^2
\\
&+
\frac1R
\int_{\mathcal A_R}
|u||S|^2
\\
&+
\frac1R
\int_{\mathcal A_R}
|u||\nabla u|^2
\\
&+
\frac1R
\int_{\mathcal A_R}
|u|
\left(
|\nabla^2p|
+
|\Delta p|
\right).
\end{aligned}
}
$$

If the cutoff is moving,

additionally include:

$$
\boxed{
\|\partial_t\chi_R\|_\infty
\int_{\mathcal A_R}
|S|^2.
}
$$

---

# 24. Pressure caveat

Although:

$$
S:\nabla^2p
$$

has been written as a boundary divergence,

$$
F_p
$$

still contains:

$$
\nabla^2p.
$$

and the pressure Hessian is a nonlocal quantity.

Therefore:

$$
\boxed{
\text{vanishing of pressure bulk term}
\not\Rightarrow
\text{pressure influence becomes local}.
}
$$

It is merely moved exactly to the boundary current.

This is a provenance-preserving transformation of X-Integration,

not a physical locality theorem.

---

# 25. Scaling audit

N–S scaling:

$$
u_\lambda(x,t)
=
\lambda u(\lambda x,\lambda^2t).
$$

Then:

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t),
$$

$$
\omega_\lambda
=
\lambda^2\omega(\lambda x,\lambda^2t).
$$

Thus:

$$
b_{B,\lambda}
=
\lambda^6
b_B(\lambda x,\lambda^2t).
$$

For the core radius:

$$
R_\lambda=\lambda^{-1}R,
$$

we have:

$$
\boxed{
\int
\chi_{R_\lambda}
b_{B,\lambda}
dx
=
\lambda^3
\int
\chi_Rb_Bdx.
}
$$

---

# 26. C3-N.3: Boundary Compensation is Same-Scale as Bulk Self-Amplification

Similarly:

$$
\int
\chi_{R_\lambda}
\det S_\lambda\,dx
=
\lambda^3
\int
\chi_R\det S\,dx.
$$

Therefore:

$$
\boxed{
\text{localized Betchov boundary correction}
}
$$

and:

$$
\boxed{
\text{bulk strain self-amplification}
}
$$

have exactly the same instantaneous scaling:

$$
\lambda^3.
$$

Thus:

## No-Go 26.1

$$
\boxed{
R\to0
\text{ does not make the boundary Betchov correction perturbatively small by scaling alone}.
}
$$

---

# 27. Viscous-window scaling

For a scale:

$$
\lambda
$$

the viscous time is:

$$
\tau_\lambda
\sim
(\nu\lambda^2)^{-1}.
$$

The instantaneous Betchov/self-amplification rate is:

$$
\sim
\lambda^3.
$$

Thus, over one viscous window:

$$
\boxed{
\text{integrated contribution}
\sim
\lambda
}
$$

under normalized fixed-shape scaling.

Therefore, the boundary compensation is at the same supercritical level as enstrophy growth.

---

# 28. Boundary-current finite-budget no-go

The global kinetic energy only controls:

$$
\nu
\int
\|\nabla u\|_2^2dt.
$$

It does not control:

$$
\boxed{
\int
\frac1R
\int_{\mathcal A_R}
|u||\nabla u|^2
dxdt
}
$$

uniformly over shrinking:

$$
R.
$$

Therefore:

$$
\boxed{
\text{exact boundary representation}
\neq
\text{finite boundary budget}.
}
$$

This is one of the most important no-gos of this round.

---

# 29. Kinematic current ≠ temporal energy flux

$$
F_B
$$

is the kinematic spatial current that makes:

$$
\nabla\cdot F_B
=
\operatorname{tr}(A^3)
$$

hold.

It is not a:

- kinetic-energy current;
- sign-definite flux;
- conserved temporal charge;
- irreversible expenditure.

Therefore:

$$
\boxed{
\int_{\partial B_R}F_B\cdot n
}
$$

cannot be directly treated as a "finite cost paid per generation".

---

# 30. Local Betchov compensation and C3-J gauge audit

C3-J has pointed out that a moving core generates a:

$$
\partial_t\chi
$$

gauge sweep.

C3-N shows that the Betchov mismatch is formed by:

$$
\nabla\chi\cdot F_B
$$

The two are of different types:

$$
\boxed{
\partial_t\chi
\neq
\nabla\chi\cdot F_B.
}
$$

Thus:

- reclassification caused by the core's own motion;
- local Betchov compensation current;

must not be conflated.

---

# 31. Spatial compensation truly must touch the boundary

Assume:

$$
\chi_R=1
$$

on:

$$
B_R,
$$

with transition only in:

$$
\mathcal A_R.
$$

If:

$$
F_B=0
$$

on:

$$
\mathcal A_R,
$$

Then:

$$
\boxed{
\int
\chi_R
\left(
\omega\cdot S\omega+4\det S
\right)
=
0.
}
$$

Thus, if a Betchov mismatch exists within the weighted core,

the boundary layer must have a nonzero:

$$
F_B.
$$

This is an exact source condition.

---

# 32. But boundary current does not require far-field defect to directly enter the core

$$
F_B
$$

only depends on the following on the boundary layer:

$$
u,\nabla u.
$$

A far-space defect can:

- alter boundary fields through pressure / Biot–Savart-like global influence;
- be transported to the boundary via earlier dynamics;
- or completely decouple.

The localized identity itself cannot distinguish these provenances.

Therefore, an X-certificate is still needed to preserve the provenance of the boundary fields.

---

# 33. Local Betchov current and phase-space ancestry

For an ancestry core:

$$
R_n
\sim
\lambda_n^{-1},
$$

Define:

$$
\boxed{
\mathfrak J_{B,n}
=
\frac43
\int_{\partial B_{R_n}(x_n)}
F_B\cdot n\,dS.
}
$$

Then:

$$
\boxed{
\mathfrak J_{B,n}
=
\int_{B_{R_n}(x_n)}
\left(
\omega\cdot S\omega
+
4\det S
\right)dx.
}
$$

Thus, each generation of the core can be appended with:

$$
\boxed{
\operatorname{XBetchov}_n
=
\left\langle
\mathfrak J_{B,n},
\mathcal V_n,
\mathcal A_n,
\operatorname{ProvBoundary}_n
\right\rangle.
}
$$

where:

- $\mathcal V_n$ = core vortex stretching;
- $\mathcal A_n=-4\int\det S$ = strain self-amplification representation;
- $\operatorname{ProvBoundary}$ = current on boundary.

---

# 34. Betchov sign convention

Define:

$$
\mathcal V_\chi
=
\int
\chi
\omega\cdot S\omega,
$$

$$
\mathcal A_\chi
=
-4
\int
\chi
\det S.
$$

Then:

$$
b_B
=
\omega\cdot S\omega
-
(-4\det S).
$$

Thus:

$$
\boxed{
\mathcal V_\chi
-
\mathcal A_\chi
=
-\frac43
\int
\nabla\chi\cdot F_B.
}
$$

That is:

$$
\boxed{
\text{local VS}
-
\text{local SSA}
=
\text{boundary Betchov current}.
}
$$

In the whole space:

$$
\boxed{
\mathcal V=\mathcal A.
}
$$

---

# 35. Local VS/SSA imbalance theorem

## Theorem 35.1

If:

$$
\mathcal V_\chi
\ge
(1+\delta)
\mathcal A_\chi
$$

and:

$$
\mathcal A_\chi>0,
$$

Then:

$$
\boxed{
\left|
\int
\nabla\chi\cdot F_B
\right|
\ge
\frac34
\delta
\mathcal A_\chi.
}
$$

Similarly, if SSA is significantly greater than VS,

the boundary current magnitude must also be comparable.

Therefore, local production mechanisms can only be significantly imbalanced when the boundary current is sufficiently large.

---

# 36. The position of Encinar 2023

Encinar's DNS results show:

the filtered VS / SSA mismatch is typically largely canceled by spatial averaging within a few filter widths.

The theorem in this round does not provide:

$$
3\times\text{filter width}
$$

this numerical constant.

It only proves:

$$
\boxed{
\text{any cancellation length must be formed via a Betchov boundary current}.
}
$$

Thus:

- exact theorem = divergence/boundary identity;
- numerical evidence = characteristic local cancellation radius.

The two are strictly separated.

---

# 37. Miller self-amplification warning

Miller's strain self-amplification model retains the:

$$
-2\int\det S
$$

bulk growth mechanism,

and blows up in finite time for a family of data.

Therefore:

$$
\boxed{
\text{boundary correction small}
}
$$

cannot be automatically interpreted as a "good thing".

Conversely:

if the local full N–S dynamics is in some sense overly close to the pure self-amplification model,

it might be closer to a dangerous strain-growth route.

However:

$$
\boxed{
\text{small local }\mathcal C_\chi
\Rightarrow
\text{full N--S blow-up}
}
$$

is completely unproven.

It can only serve as a structural warning.

---

# 38. Miller 2024/2026 depletion interface

Miller's strain-vorticity interaction work proves:

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

and establishes a global regular strain-vorticity interaction model.

Its regularity criteria show:

if the full N–S blows up,

certain perturbation packages involving:

$$
(u\cdot\nabla)S,
\quad
S^2,
\quad
\omega\otimes\omega
$$

cannot remain too small relative to the dissipative strain scale.

Therefore:

$$
\boxed{
\text{advection/depletion corrections are not decorations that can be arbitrarily removed}.
}
$$

The C3-N localized balance provides a new physical-space interface to track how these corrections pass through the ancestry boundary.

---

# 39. C3-N Main reduction

Now, if the strain growth of a hypothetical ancestry core enters a singular regime,

there are at least:

## Branch N-A — Bulk self-amplification

$$
\boxed{
-2
\int
\chi_n\det S
}
$$

dominates.

This connects to:

- $\lambda_2^+$ divergence;
- two-positive-eigenvalue geometry;
- strain self-amplification model.

## Branch N-B — Boundary/depletion compensation

$$
\boxed{
|\mathcal C_{\chi_n}|
}
$$

is of the same order as the bulk term or larger.

Then the singular route must continuously generate:

- advection boundary flux;
- pressure-Hessian boundary current;
- Betchov VS/SSA current;
- diffusion/gauge corrections.

---

# 40. Is this a contradiction?

No.

Both branches can remain nontrivial under N–S scaling.

Specifically:

$$
\boxed{
\mathcal C_{\chi_n}
}
$$

and:

$$
\boxed{
\int\chi_n\det S
}
$$

at:

$$
R_n\sim\lambda_n^{-1}
$$

are of the same order.

Thus, shrinking the ancestry core itself will not select Branch N-A or N-B.

---

# 41. The truly new rigidity target

To advance, we must study the ratio:

$$
\boxed{
\mathfrak D_n
=
\frac{
\mathcal C_{\chi_n}
}{
-2\int\chi_n\det S
}
}
$$

when the bulk denominator is nonzero.

Possibilities:

### N-R1 — $\mathfrak D_n\to0$

The core gradually becomes self-amplification dominated.

### N-R2 — $\mathfrak D_n\to-1$

boundary/depletion almost completely cancels bulk production.

### N-R3 — $\mathfrak D_n$ oscillatory / unbounded

The core and exterior continuously exchange dominance.

Different branches may require completely different rigidity theorems.

---

# 42. X-Integration hard guards update

## G-B3

Preserves the:

$$
\operatorname{tr}(A^3)
$$

exact Betchov current of:

$$
F_B.
$$

## G-B2

Preserves the:

$$
\operatorname{tr}(A^2)
$$

magnitude current of:

$$
Au.
$$

## G-BULK

bulk self-amplification:

$$
-2\int\chi\det S.
$$

## G-BDRY

boundary package:

$$
\mathcal C_\chi.
$$

## G-PRESS

pressure current:

$$
F_p.
$$

Must not be mistakenly called local just because it is in a boundary integral.

## G-FLUXTYPE

Betchov current is not an energy flux.

## G-SCALE

Boundary and bulk share the same scaling;

it is forbidden to use:

$$
R\to0
$$

to automatically declare the boundary negligible.

---

# 43. True ETN update

The strain tension state of the ancestry core can be written as:

$$
\boxed{
\Theta_n^{strain}
=
\left\langle
E_{S,n},
D_{S,n},
A_{SSA,n},
J_{B,n},
J_{adv,n},
J_{press,n},
J_{diff,n},
J_{gauge,n}
\right\rangle.
}
$$

exact balance:

$$
\boxed{
\dot E_{S,n}
+
D_{S,n}
=
A_{SSA,n}
+
\sum J_{n}.
}
$$

Therefore, True ETN here is not a metaphor for "adding several forces".

It directly corresponds to an exact typed local balance.

---

# 44. New frontier: C3-O

This round has closed:

$$
\boxed{
\text{is localized Betchov compensation truly a boundary term?}
}
$$

Answer:

$$
\boxed{
\textbf{YES, exactly}.
}
$$

But it also proved:

$$
\boxed{
\text{boundary current and bulk self-amplification have the same scaling}.
}
$$

So the new core question is not "does the boundary exist?"

but rather:

> in a hypothetical singular ancestry, what asymptotic ratio must the boundary/depletion package adopt relative to the bulk strain self-amplification?

Formal definition:

$$
\boxed{
\textbf{C3-O — Boundary Depletion versus Strain Self-Amplification Rigidity}.
}
$$

---

# 45. C3-O proof obligations

## O1 — Bulk/boundary ratio classification

Study:

$$
\mathfrak D_n
=
\frac{
\mathcal C_{\chi_n}
}{
A_{SSA,n}
}.
$$

Extract a subsequence such that its:

- convergence;
- sign;
- boundedness;

can be classified.

## O2 — Self-amplification-dominated branch

If:

$$
\mathfrak D_n\to0,
$$

compare the rescaled ancestry core with the Miller strain self-amplification model.

Full dynamical closeness is required,

cannot rely solely on a single energy balance.

## O3 — Depletion-dominated branch

If:

$$
\mathfrak D_n\approx-1,
$$

Prove:

$$
\boxed{
\text{boundary correction must persistently phase-lock with bulk SSA}.
}
$$

Study whether this persistent cancellation is compatible with:

- first-crossing timing;
- phase efficiency;
- spatial direction roughness;
- pressure nonlocality;

## O4 — Pressure current decomposition

For:

$$
F_p
=
(\nabla^2p-\Delta pI)u
$$

perform a near/far pressure decomposition.

Determine how much of the ancestry core's pressure compensation comes from:

- local core;
- far defect;
- moving gauge.

## O5 — Betchov current frequency decomposition

For:

$$
F_B
=
(A^2-\tfrac12\operatorname{tr}(A^2)I)u
$$

perform LP/helical decomposition.

Study:

$$
\boxed{
\text{local heterochiral ancestry}
}
$$

how much it accounts for in the Betchov boundary current.

## O6 — Localized Miller perturbation

Attempt to establish a:

$$
\boxed{
\text{localized analogue of Miller perturbative criteria}
}
$$

using the boundary/depletion norm to measure the distance of the full local dynamics from:

- the strain self-amplification model;
- the strain-vorticity interaction model;

## O7 — Betchov-current total variation

Although the current is not sign-definite,

study whether the following on the shrinking ancestry boundary:

$$
\int
|J_{B,n}|
$$

can be bounded by critical moment / strain geometry.

## O8 — Experimental audit

Use DNS / synthetic divergence-free fields to measure:

$$
\mathfrak D_n
$$

and its relationship with:

- local VS/SSA ratio;
- $\lambda_2^+$;
- helicity pair-production;
- phase efficiency;

Numerical results are strictly labeled as evidence.

---

# 46. Formal status

$$
\boxed{
\begin{aligned}
b_B=\frac43\operatorname{tr}(A^3)
&:\ \mathrm{PROVED},\\
\operatorname{tr}(A^3)=\nabla\cdot F_B
&:\ \mathrm{EXTERNAL/STANDARD},\\
\text{localized Betchov boundary theorem}
&:\ \mathrm{PROVED},\\
\text{ball surface-current form}
&:\ \mathrm{PROVED},\\
\text{boundary magnitude bound}
&:\ \mathrm{PROVED},\\
\text{dimensionless compensation bound}
&:\ \mathrm{PROVED},\\
\text{localized second Betchov identity}
&:\ \mathrm{PROVED},\\
S:\nabla^2p=\nabla\cdot F_p
&:\ \mathrm{PROVED},\\
\text{exact local strain self-amplification balance}
&:\ \mathrm{PROVED},\\
\text{unique bulk cubic strain production}
&:\ \mathrm{PROVED/STRUCTURAL},\\
\text{boundary correction becomes small as }R\to0
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{Betchov current has finite additive budget}
&:\ \mathrm{NOT\ PROVED},\\
\text{Betchov current is an energy flux}
&:\ \mathrm{FALSE/TYPE\ ERROR},\\
\text{bulk/boundary asymptotic rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 47. Conclusion

C3-M discovered:

$$
\boxed{
\text{the global Betchov identity collapses local orientation}.
}
$$

C3-N now exactly recovers the collapsed information:

$$
\boxed{
\omega\cdot S\omega
+
4\det S
=
\frac43\nabla\cdot F_B.
}
$$

Therefore:

$$
\boxed{
\text{localized VS--SSA mismatch}
=
\text{Betchov boundary current}.
}
$$

It is not an arbitrary far-field compensation.

It must pass through the localization boundary.

Furthermore, the full strain equation gives:

$$
\boxed{
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\mathcal C_\chi.
}
$$

Thus, the local strain balance truly becomes:

$$
\boxed{
\textbf{bulk strain self-amplification}
+
\textbf{boundary/depletion package}.
}
$$

And all:

- vorticity mismatch;
- advection;
- pressure Hessian;
- localization diffusion;
- moving-core gauge;

are explicitly preserved in:

$$
\mathcal C_\chi.
$$

But this is still not a regularity proof.

Since:

$$
\boxed{
\mathcal C_\chi
}
$$

and:

$$
\boxed{
-2\int\chi\det S
}
$$

have the same scaling on a parabolic shrinking core.

Therefore, the truly new frontier is:

$$
\boxed{
\textbf{bulk SSA}
\quad\text{vs}\quad
\textbf{persistent boundary depletion}.
}
$$

Next round:

$$
\boxed{
\textbf{C3-O — Boundary Depletion versus Strain Self-Amplification Rigidity}.
}
$$

---

# References

1. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, Journal of Fluid Mechanics 948 (2022), R2; arXiv:2112.12820.
2. R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, Journal of Fluid Mechanics 1 (1956), 497–504.
3. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, arXiv:1910.05415.
4. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691.
5. M. P. Encinar, *A length scale for non-local multi-scale gradient interactions in isotropic turbulence*, Journal of Fluid Mechanics 971 (2023), A40.
6. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
7. Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866.

# Internal dependencies

- `NS_C1_UV_Replenishment_Chain_v0.2.md`
- `NS_C2_Critical_Toll_Spike_Packing_v0.3.md`
- `NS_C3A_Conservation_Criticality_Helical_Pair_Production_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `NS_C3F_PhaseSpace_Ancestry_Cone_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `NS_C3H_Ancestry_Renormalization_CriticalCompactnessBarrier_v0.1.md`
- `NS_C3I_FrontierUVCap_DefectTrichotomy_v0.1.md`
- `NS_C3J_GaugeCorrected_Reentry_Hysteresis_NoGo_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-O — Boundary Depletion versus Strain Self-Amplification Rigidity}
}
$$