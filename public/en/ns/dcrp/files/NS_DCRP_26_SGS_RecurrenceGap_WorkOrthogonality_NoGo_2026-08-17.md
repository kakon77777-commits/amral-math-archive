---
title: NS-DCRP-26 — SGS Recurrence Gap, Dual-Work Coercivity No-Go, and Reduction to Critical-Reservoir Compactness
subtitle: null
status: research proof checkpoint
epistemic_status: null
---

# NS-DCRP-26 — SGS Recurrence Gap, Dual-Work Coercivity No-Go, and Reduction to Critical-Reservoir Compactness

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. test the DCRP-25 Active-Stress Work-Orthogonality / Dual-Efficiency proposal;
  2. prove that energy/enstrophy work pairings cannot themselves be coercive because rigid transport tangents are exactly work-orthogonal;
  3. replace dual-work coercivity by an exact SGS-energy recurrence argument;
  4. prove that a nonzero bounded-reservoir recurrent strong increment profile must pay forward SGS work, SGS localization/transport, or SGS endpoint mismatch;
  5. compress the expanding-radius condition back to a finite family of normalized windows under strong-profile compactness;
  6. identify the remaining global branch as critical-reservoir / compactness escape rather than an unresolved stress-angle kernel.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - Gregory L. Eyink and Hussein Aluie, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, arXiv:0909.2386;
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-23 bounded-lag increment activation;
  - DCRP-24 fiber/covariance rigidity;
  - DCRP-25 pressure-compatible SGS energy and affine/Morrey rigidity.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-25 proposed the remaining bounded-reservoir strong-profile frontier:

$$
\boxed{
\textbf{
Active-Stress Work-Orthogonality / Dual-Efficiency Rigidity}.
}
\tag{1.1}
$$

The first result of DCRP-26 is a NO-GO.

Let:

$$
F
=
-\mathbb P\nabla\cdot R
$$

be the divergence-free active SGS force.

On the whole space or torus:

$$
\boxed{
W_0
=
\langle
F,U
\rangle,
}
\tag{1.2}
$$

and the vorticity-side commutator work is:

$$
\boxed{
W_1
=
\langle
\nabla\times F,\Omega
\rangle
=
\langle
F,-\Delta U
\rangle.
}
\tag{1.3}
$$

These two pairings do **not** form a coercive norm on:

$$
F.
$$

A pure translation tangent:

$$
\boxed{
F
=
c\cdot\nabla U
}
\tag{1.4}
$$

satisfies:

$$
\boxed{
\langle
F,U
\rangle
=
0,
}
\tag{1.5}
$$

and, because translations commute with:

$$
-\Delta,
$$

$$
\boxed{
\langle
F,-\Delta U
\rangle
=
0.
}
\tag{1.6}
$$

Yet:

$$
F
$$

can be nonzero and have nonzero curl.

An explicit periodic example is:

$$
\boxed{
U(x)
=
(0,\cos x_1,0),
}
\tag{1.7}
$$

$$
\boxed{
F(x)
=
(0,-c\sin x_1,0)
=
c\partial_1U.
}
\tag{1.8}
$$

Then:

$$
F\neq0,
$$

$$
\nabla\times F\neq0,
$$

but:

$$
\boxed{
W_0=W_1=0.
}
\tag{1.9}
$$

Moreover define:

$$
\boxed{
R_0(x)
=
\begin{pmatrix}
0 & -c\cos x_1 & 0\\
-c\cos x_1 & 0 & 0\\
0&0&0
\end{pmatrix}.
}
\tag{1.10}
$$

Then:

$$
\boxed{
-\nabla\cdot R_0
=
F.
}
\tag{1.11}
$$

For:

$$
C>|c|,
$$

$$
\boxed{
R
=
CI+R_0
}
\tag{1.12}
$$

is symmetric positive definite and has the same divergence.

Thus even positivity of the stress tensor does not make the two signed works coercive at the purely tensorial level.

This example is **not claimed to be the Reynolds covariance of the same filtered velocity**.

Its role is to prove the algebraic limitation of the proposed dual-efficiency inference.

The correct principle is:

$$
\boxed{
\textbf{
rigid/material transport must be quotiented before work efficiency is interpreted.
}
}
\tag{1.13}
$$

The second and main result is that a second work pairing is actually unnecessary on the **actual recurrent strong-profile branch**.

DCRP-25 proved the exact SGS energy equation:

$$
\boxed{
\partial_tk_\ell
+
\nabla\cdot J_\ell
=
\nu\Delta k_\ell
-
\nu d_\ell
+
\Pi_\ell,
}
\tag{1.14}
$$

with:

$$
\boxed{
k_\ell
=
\frac12
\operatorname{tr}R_\ell
\ge0,
}
\tag{1.15}
$$

$$
\boxed{
d_\ell
=
S_\ell|\nabla u|^2
-
|\nabla U_\ell|^2
\ge0,
}
\tag{1.16}
$$

and:

$$
\boxed{
\Pi_\ell
=
-
R_\ell:\nabla U_\ell.
}
\tag{1.17}
$$

For a normalized cutoff:

$$
\chi_R,
$$

define:

$$
\boxed{
K_R(s)
=
\int
\chi_R
k_\sigma(y,s)dy,
}
\tag{1.18}
$$

$$
\boxed{
D_R^{sgs}
=
\nu
\int_{s_0}^{s_1}
\int
\chi_R
d_\sigma
dyds,
}
\tag{1.19}
$$

$$
\boxed{
W_R
=
\int_{s_0}^{s_1}
\int
\chi_R
\Pi_\sigma
dyds,
}
\tag{1.20}
$$

and let:

$$
L_R^{sgs}
$$

be the signed localization/transport contribution.

The exact return ledger is:

$$
\boxed{
K_R(s_1)
-
K_R(s_0)
+
D_R^{sgs}
=
W_R
+
L_R^{sgs}.
}
\tag{1.21}
$$

Therefore:

$$
\boxed{
D_R^{sgs}
\le
W_{R,+}
+
|L_R^{sgs}|
+
|
K_R(s_1)-K_R(s_0)
|,
}
\tag{1.22}
$$

where:

$$
W_{R,+}
=
\left(
W_R
\right)_+.
$$

This yields the central rigidity statement.

Suppose a normalized actual strong-profile sequence satisfies:

- the bounded-reservoir Morrey growth:

  $$
  \int_{B_R}
  |u_\infty|^2
  \lesssim
  R;
  $$

- a persistent nonzero resolved increment defect:

  $$
  \widetilde{\mathcal S}^{(3)}[u_\infty]
  >
  0;
  $$

- for every fixed normalized radius:

  $$
  R<\infty,
  $$

  the recurrence costs vanish:

  $$
  W_{R,+}\to0,
  $$

  $$
  L_R^{sgs}\to0,
  $$

  and:

  $$
  K_R(s_1)-K_R(s_0)\to0.
  $$

Then (1.22) forces:

$$
\boxed{
D_R^{sgs}\to0
\qquad
\forall R<\infty.
}
\tag{1.23}
$$

Passing to the strong profile:

$$
\boxed{
d_\sigma[u_\infty]=0
}
\tag{1.24}
$$

on every compact region.

DCRP-25 then gives:

$$
\boxed{
u_\infty(y,s)
=
A(s)y+b(s)
}
\tag{1.25}
$$

globally in:

$$
y.
$$

The inherited Morrey growth:

$$
O(R)
$$

forces:

$$
\boxed{
A=b=0.
}
\tag{1.26}
$$

Hence:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u_\infty]
=
0,
}
\tag{1.27}
$$

a contradiction.

Thus:

$$
\boxed{
\textbf{
nonzero bounded-reservoir recurrent strong increment profile}
\Longrightarrow
\textbf{
forward SGS work}
\ \vee\
\textbf{
SGS localization/transport}
\ \vee\
\textbf{
SGS endpoint-return mismatch}
\ \vee\
\textbf{
compactness failure}.
}
\tag{1.28}
$$

This closes the **active work-orthogonality kernel** at the recurrence level without requiring:

$$
W_\omega.
$$

The third main result is finite-window compression.

Let:

$$
\mathscr C_{M,s_\ast}
$$

be a sequentially compact class of normalized resolved strong profiles satisfying:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}
\ge
s_\ast>0,
}
\tag{1.29}
$$

the bounded-reservoir Morrey law, and no already-declared fiber/Young/scale/spatial escape.

Take an increasing sequence of fixed radii:

$$
R_m\to\infty.
$$

Define:

$$
\boxed{
G_m(u)
=
W_{R_m,+}(u)
+
|L_{R_m}^{sgs}(u)|
+
|
K_{R_m}(s_1)-K_{R_m}(s_0)
|.
}
\tag{1.30}
$$

Assume these functionals are lower semicontinuous/continuous in the strong-profile topology.

Then there exist:

$$
\boxed{
N_\ast<\infty,
\qquad
c_\ast>0
}
\tag{1.31}
$$

such that:

$$
\boxed{
\max_{1\le m\le N_\ast}
G_m(u)
\ge
c_\ast
\qquad
\forall
u\in
\mathscr C_{M,s_\ast}.
}
\tag{1.32}
$$

Hence an **infinite exhaustion is not needed in the finite compiler**.

A fixed finite family of normalized SGS recurrence windows detects every nonzero compact strong increment profile.

This is a profile-level finite anti-phantom theorem.

The remaining global difficulty is therefore no longer a mysterious work-angle kernel.

The branches that can still escape are:

1. critical-reservoir blowup:

   $$
   A+D\to\infty;
   $$

2. failure of strong compactness:

   - fiber escape;
   - Young oscillation/concentration;
   - covariance defect;
   - UV/IR/spatial escape;
   - transition/profile splitting;

3. positive forward SGS work / localization / endpoint mismatch, which is already visible but still requires global taxation/summability if one wants a direct regularity contradiction.

Thus the next closure-facing frontier is:

$$
\boxed{
\textbf{
Critical-Reservoir Compactness / Escape Rigidity
}
}
\tag{1.33}
$$

together with the already-known global question of converting persistent positive critical costs into a finite physical budget contradiction.

---

# 2. Energy and enstrophy work are two moments of the same active force

Let:

$$
F_R
=
-\mathbb P\nabla\cdot R.
$$

Because:

$$
U
$$

is divergence free:

$$
\boxed{
\langle
F_R,U
\rangle
=
\langle
-\nabla\cdot R,U
\rangle
=
\int
R:\nabla U.
}
\tag{2.1}
$$

Thus the usual signed coarse energy flux:

$$
\Pi=-R:\nabla U
$$

has whole-space integral:

$$
\boxed{
\int\Pi
=
-
\langle
F_R,U
\rangle.
}
\tag{2.2}
$$

Now:

$$
\Omega
=
\nabla\times U.
$$

Integration by parts gives:

$$
\boxed{
\langle
\nabla\times F_R,\Omega
\rangle
=
\langle
F_R,
\nabla\times\Omega
\rangle.
}
\tag{2.3}
$$

For divergence-free:

$$
U,
$$

$$
\boxed{
\nabla\times\Omega
=
-\Delta U.
}
\tag{2.4}
$$

Hence:

$$
\boxed{
\langle
\nabla\times F_R,\Omega
\rangle
=
\langle
F_R,-\Delta U
\rangle.
}
\tag{2.5}
$$

Thus the energy-side and enstrophy-side stress works are merely two Sobolev moments of the same force-state cross pairing.

They are not algebraically independent coordinates.

---

# 3. Translation tangent NO-GO

Let the domain be:

$$
\mathbb T^3.
$$

Set:

$$
U(x)
=
(0,\cos x_1,0).
$$

Then:

$$
\nabla\cdot U=0.
$$

For:

$$
c\neq0,
$$

define:

$$
F(x)
=
c\partial_1U
=
(0,-c\sin x_1,0).
$$

Then:

$$
F\neq0.
$$

Also:

$$
-\Delta U=U.
$$

Therefore:

$$
\boxed{
\int_{\mathbb T^3}
F\cdot U
dx
=
0,
}
\tag{3.1}
$$

and:

$$
\boxed{
\int_{\mathbb T^3}
F\cdot
(-\Delta U)
dx
=
0.
}
\tag{3.2}
$$

The vorticity is:

$$
\Omega
=
(0,0,-\sin x_1),
$$

while:

$$
F
$$

points in the:

$$
e_2
$$

direction, so:

$$
\boxed{
F\cdot\Omega=0
}
\tag{3.3}
$$

pointwise.

But:

$$
\boxed{
\nabla\times F
=
(0,0,-c\cos x_1)
\neq0.
}
\tag{3.4}
$$

Thus even adding the helicity-type pairing does not make this transport tangent visible as bulk work.

Status:

$$
\boxed{
\textbf{EXACT NO-GO}.
}
$$

---

# 4. Positive symmetric stress realization of the translation example

Define:

$$
R_0(x)
=
\begin{pmatrix}
0 & -c\cos x_1 & 0\\
-c\cos x_1 & 0 & 0\\
0&0&0
\end{pmatrix}.
$$

Then:

$$
\boxed{
-\nabla\cdot R_0
=
F.
}
\tag{4.1}
$$

For:

$$
C>|c|,
$$

set:

$$
R=CI+R_0.
$$

The eigenvalues of the upper:

$$
2\times2
$$

block are:

$$
C\pm c\cos x_1.
$$

Hence:

$$
\boxed{
R>0
}
\tag{4.2}
$$

pointwise.

Since:

$$
\nabla\cdot(CI)=0,
$$

$$
\boxed{
-\nabla\cdot R=F.
}
\tag{4.3}
$$

Thus:

$$
\boxed{
\textbf{
symmetric positive stress}
+
\textbf{
active nonzero force}
+
\textbf{
zero energy/enstrophy bulk work}
}
$$

is algebraically possible.

Again:

$$
R
$$

is not claimed to be the exact Reynolds covariance generated by the same:

$$
U
$$

under a positive mollifier.

The example only invalidates a stress-level coercivity theorem based on symmetry/positivity plus the two works.

---

# 5. Why translation is an exact symmetry tangent

For a constant vector:

$$
a,
$$

define:

$$
\boxed{
\mathcal T_aU
=
a\cdot\nabla U.
}
\tag{5.1}
$$

On the torus or whole space:

$$
\mathcal T_a
$$

is skew-adjoint on:

$$
L^2.
$$

Also:

$$
\boxed{
[
\mathcal T_a,
-\Delta
]
=
0.
}
\tag{5.2}
$$

Therefore for every integer:

$$
m\ge0,
$$

$$
\boxed{
\left\langle
\mathcal T_aU,
(-\Delta)^mU
\right\rangle
=
0.
}
\tag{5.3}
$$

Thus **every Sobolev energy moment** is instantaneously blind to pure translation tangent.

This is not a defect of the chosen two works.

It is a consequence of symmetry.

Accordingly, transport/translation tangents must be handled through:

- moving centers;
- co-moving cutoffs;
- symmetry quotient;

rather than through positive work coercivity.

---

# 6. General SGS energy return identity

The exact SGS energy equation from DCRP-25 is:

$$
\partial_sk_\sigma
+
\nabla\cdot J_\sigma
=
\nu\Delta k_\sigma
-
\nu d_\sigma
+
\Pi_\sigma.
$$

Let:

$$
\chi_R
$$

be a normalized smooth cutoff supported in:

$$
B_{2R}
$$

and equal to one on:

$$
B_R.
$$

Allow:

$$
\chi_R
$$

to depend smoothly on normalized time.

Define:

$$
\boxed{
K_R(s)
=
\int
\chi_R(y,s)
k_\sigma(y,s)dy.
}
\tag{6.1}
$$

Define:

$$
\boxed{
D_R^{sgs}
=
\nu
\int_{s_0}^{s_1}
\int
\chi_R
d_\sigma
dyds.
}
\tag{6.2}
$$

Define:

$$
\boxed{
W_R
=
\int_{s_0}^{s_1}
\int
\chi_R
\Pi_\sigma
dyds.
}
\tag{6.3}
$$

Define the signed localization/transport term:

$$
\boxed{
L_R^{sgs}
=
\int_{s_0}^{s_1}
\int
\left[
(
\partial_s\chi_R
+
\nu\Delta\chi_R
)
k_\sigma
+
\nabla\chi_R
\cdot
J_\sigma
\right]
dyds.
}
\tag{6.4}
$$

Then:

$$
\boxed{
K_R(s_1)
-
K_R(s_0)
+
D_R^{sgs}
=
W_R
+
L_R^{sgs}.
}
\tag{6.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. One-sided recurrence inequality

Because:

$$
D_R^{sgs}\ge0,
$$

from (6.5):

$$
D_R^{sgs}
=
W_R
+
L_R^{sgs}
-
\left[
K_R(s_1)
-
K_R(s_0)
\right].
$$

Therefore:

$$
\boxed{
D_R^{sgs}
\le
(W_R)_+
+
|L_R^{sgs}|
+
|
K_R(s_1)
-
K_R(s_0)
|.
}
\tag{7.1}
$$

Also:

$$
\boxed{
(W_R)_+
\le
\int
\chi_R
(\Pi_\sigma)_+.
}
\tag{7.2}
$$

Thus any PFET/forward-work detector that controls the positive local SGS work controls the first term.

---

# 8. Expanding-window zero-gap rigidity

Consider a normalized resolved strong profile:

$$
u_\infty
$$

defined on:

$$
\mathbb R^3
\times
[s_0,s_1].
$$

Assume the inherited Morrey bound:

$$
\boxed{
\operatorname*{ess\,sup}_s
\int_{B_R}
|u_\infty(y,s)|^2dy
\le
MR
\qquad
\forall R\ge1.
}
\tag{8.1}
$$

Assume:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u_\infty]
>
0.
}
\tag{8.2}
$$

Assume for every fixed:

$$
R<\infty,
$$

$$
\boxed{
(W_R)_+=0,
}
\tag{8.3}
$$

$$
\boxed{
L_R^{sgs}=0,
}
\tag{8.4}
$$

and:

$$
\boxed{
K_R(s_1)=K_R(s_0).
}
\tag{8.5}
$$

Then (7.1) gives:

$$
\boxed{
D_R^{sgs}=0
}
\tag{8.6}
$$

for every:

$$
R.
$$

Since:

$$
d_\sigma\ge0,
$$

and the cutoffs exhaust:

$$
\mathbb R^3,
$$

$$
\boxed{
d_\sigma[u_\infty]=0
}
\tag{8.7}
$$

almost everywhere.

DCRP-25 gives:

$$
u_\infty(y,s)
=
A(s)y+b(s).
$$

The Morrey bound forces:

$$
A=b=0.
$$

This contradicts (8.2).

Therefore:

$$
\boxed{
\textbf{
no nonzero bounded-reservoir strong increment profile can be
simultaneously SGS-return exact,
forward-work silent,
and localization silent on every normalized radius.
}
}
\tag{8.8}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. Sequence version

Let:

$$
u_n
$$

be a sequence of normalized actual states converging to:

$$
u_\infty
$$

in the resolved strong-profile topology.

Assume:

$$
\widetilde{\mathcal S}^{(3)}[u_\infty]
\ge
s_\ast>0.
$$

Suppose for every fixed:

$$
R,
$$

$$
(W_{n,R})_+\to0,
$$

$$
L_{n,R}^{sgs}\to0,
$$

and:

$$
K_{n,R}(s_1)
-
K_{n,R}(s_0)
\to0.
$$

Then (7.1) gives:

$$
D_{n,R}^{sgs}\to0.
$$

Lower semicontinuity of the nonnegative gradient variance gives:

$$
D_{\infty,R}^{sgs}=0.
$$

Apply Section 8.

Contradiction.

Hence at least one recurrence channel survives on some fixed normalized radius.

---

# 10. Compact strong-profile class

Let:

$$
\mathscr C_{M,s_\ast}
$$

be a class of normalized actual resolved strong profiles satisfying:

1. the Morrey bound:

   $$
   \int_{B_R}|u|^2
   \le
   MR;
   $$

2.:

   $$
   \widetilde{\mathcal S}^{(3)}[u]
   \ge
   s_\ast>0;
   $$

3. fixed relative filter:

   $$
   \ell/r=\sigma;
   $$

4. no fiber/Young/covariance/spatial/scale escape already assigned to other defect branches;

5. sequential compactness in a topology in which:

   -:

     $$
     K_R(s_i)
     $$

     is continuous;
   -:

     $$
     L_R^{sgs}
     $$

     is continuous or lower-semicontinuously controlled;
   -:

     $$
     (W_R)_+
     $$

     is lower semicontinuous.

The compactness assumption is explicit.

It is not claimed to follow from MORP-01's abstract package norm without a separate M-COM theorem.

---

# 11. Recurrence-gap functional

Choose:

$$
1<R_1<R_2<\cdots,
\qquad
R_m\to\infty.
$$

Define:

$$
\boxed{
G_m(u)
=
(W_{R_m}(u))_+
+
|L_{R_m}^{sgs}(u)|
+
|
K_{R_m}(s_1)
-
K_{R_m}(s_0)
|.
}
\tag{11.1}
$$

Every term is nonnegative.

Section 8 proves:

$$
\boxed{
\forall
u\in
\mathscr C_{M,s_\ast},
\qquad
\sup_m
G_m(u)
>
0.
}
\tag{11.2}
$$

---

# 12. NEW THEOREM — Finite-Radius SGS Recurrence Gap

## Theorem 12.1

Under the compactness/semicontinuity assumptions of Section 10, there exist:

$$
\boxed{
N_\ast<\infty,
}
\tag{12.1}
$$

and:

$$
\boxed{
c_\ast>0
}
\tag{12.2}
$$

such that:

$$
\boxed{
\max_{
1\le m\le N_\ast
}
G_m(u)
\ge
c_\ast
}
\tag{12.3}
$$

for every:

$$
u\in
\mathscr C_{M,s_\ast}.
$$

### Proof

Assume the contrary.

Then for every:

$$
N,
$$

there exists:

$$
u_N
\in
\mathscr C_{M,s_\ast}
$$

such that:

$$
\boxed{
\max_{
1\le m\le N
}
G_m(u_N)
<
\frac1N.
}
\tag{12.4}
$$

By sequential compactness, after a subsequence:

$$
u_N\to u_\infty
\in
\mathscr C_{M,s_\ast}.
$$

Fix:

$$
m.
$$

For all sufficiently large:

$$
N\ge m,
$$

$$
G_m(u_N)
<
\frac1N.
$$

By the assumed continuity/lower-semicontinuity structure:

$$
\boxed{
G_m(u_\infty)=0.
}
\tag{12.5}
$$

Since:

$$
m
$$

was arbitrary:

$$
G_m(u_\infty)=0
$$

for every:

$$
m.
$$

The radii exhaust:

$$
\mathbb R^3.
$$

Section 8 then forces:

$$
\widetilde{\mathcal S}^{(3)}[u_\infty]=0,
$$

contradicting:

$$
u_\infty
\in
\mathscr C_{M,s_\ast}.
$$

Therefore some finite:

$$
N_\ast
$$

has:

$$
\inf_{
u\in
\mathscr C_{M,s_\ast}
}
\max_{
m\le N_\ast
}
G_m(u)
>
0.
$$

Set this infimum to:

$$
c_\ast.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED conditional on the stated compact strong-profile class}.
}
$$

---

# 13. Why vorticity-side dual work is unnecessary for recurrence exclusion

The DCRP-25 proposal used:

$$
W_\omega
=
-\Omega\cdot
\nabla\times\nabla\cdot R
$$

as a second work-efficiency channel.

DCRP-26 shows that on the recurrent actual strong-profile branch:

$$
\boxed{
\text{energy-side SGS recurrence identity}
+
\text{positive SGS viscous variance}
}
$$

already gives the necessary rigidity.

If:

$$
\Pi_+
$$

is small, the profile can remain recurrent only by:

- localization/transport;
- SGS endpoint mismatch;
- or zero SGS dissipation.

The last case collapses to the affine/Morrey zero profile.

Thus:

$$
\boxed{
\textbf{
the active-stress work-orthogonality kernel is closed at the exact recurrence level
without requiring a second signed bulk-work pairing.
}
}
\tag{13.1}
$$

This avoids an algebraically false dual-coercivity route.

---

# 14. Relation to symmetry quotient

The translation example in Sections 3--5 is not an obstruction to Theorem 12.1.

A pure translation tangent:

$$
F=a\cdot\nabla U
$$

changes the spatial position/phase of the state but not its intrinsic normalized shape.

MORP/FCBP already treats:

- moving centers;
- spatial translations;
- co-moving windows;

as normalization/transition variables.

Thus the proper handling is:

$$
\boxed{
\textbf{
quotient rigid transport,
do not tax it as deformation.
}
}
\tag{14.1}
$$

The SGS recurrence theorem is formulated after the normalized spatial window is fixed.

If transport moves SGS energy through the window, it appears in:

$$
L_R^{sgs}.
$$

If the window follows it exactly, the transport is removed by the moving-center normalization.

---

# 15. Strong-profile mechanism classification after DCRP-26

On the bounded-reservoir branch:

$$
\widetilde{\mathcal S}^{(3)}
\ge
s_\ast>0.
$$

DCRP-24/25/26 now give:

$$
\boxed{
\begin{aligned}
&
\text{fiber escape}
\\
&\vee
\text{Young oscillation/concentration}
\\
&\vee
\text{covariance defect}
\\
&\vee
\text{spatial/scale escape}
\\
&\vee
\text{positive SGS viscous payment}
\\
&\vee
\text{positive forward SGS work}
\\
&\vee
\text{SGS localization/transport}
\\
&\vee
\text{SGS endpoint-return mismatch}.
\end{aligned}
}
\tag{15.1}
$$

There is no remaining exact compact recurrent strong-profile phantom with all these channels zero.

This is a substantial M-RIG result on the bounded-reservoir resolved strong-profile sector.

---

# 16. Exact MORP zero-cost consequence

MORP-01 already includes:

$$
\widetilde{\mathcal S}^{(3)}
$$

as a nonnegative cost coordinate.

Therefore DCRP-23 alone excludes a bounded-reservoir persistent non-CKN **exact zero-cost** window sequence once coordinate normalization is identified.

DCRP-26 adds a stronger dynamical statement:

even if one studies a positive-cost strong profile rather than the zero-cost kernel, a recurrent nonzero profile cannot make all actual SGS work/transport/return channels vanish.

Thus:

$$
\boxed{
\textbf{
bounded-reservoir strong-profile M-RIG is substantially closed,
conditional on M-COM / strong-profile realization.
}
}
\tag{16.1}
$$

---

# 17. What remains global

The proof is not complete.

The remaining major branches are:

### A. critical-reservoir blowup

$$
\boxed{
\limsup_k
(
A_k+D_k
)
=
+\infty.
}
\tag{17.1}
$$

DCRP-23's bounded-lag increment theorem does not apply uniformly here.

### B. noncompact profile escape

The normalized branch may fail the compact strong-profile assumptions through:

- fiber escape;
- Young concentration;
- profile splitting;
- spatial escape;
- UV/IR scale escape;
- pressure-tail escape;
- transition noncompactness.

Many of these are already explicit native defect coordinates, but a complete M-COM theorem is still required.

### C. positive critical-cost accumulation

Even when every normalized window pays:

$$
c_\ast>0,
$$

one must still relate that scale-invariant cost to a finite physical budget or a strict return depletion.

A geometrically shrinking raw payment may remain summable.

This is the old critical-summability issue.

---

# 18. Audit of the MORP package bound

MORP-01 defines:

$$
\mathcal N_{\rm pkg}
$$

only abstractly as a compactness-control package norm.

It does **not**, at the MORP-01 level, explicitly identify:

$$
\mathcal N_{\rm pkg}\le C_\ast
$$

with a uniform bound on:

$$
A_{k,\sigma}^{+}+D_k.
$$

Indeed MORP-01 records:

$$
\boxed{
\mathrm{M\mbox{-}COM}:\mathrm{OPEN}.
}
\tag{18.1}
$$

Therefore one must not silently infer that every minimal normalized obstruction lies in the DCRP-23 bounded-reservoir branch.

The bounded-reservoir theorem is a genuine branch theorem.

The complementary critical-reservoir escape still requires treatment.

Status:

$$
\boxed{
\textbf{AUDITED}.
}
$$

---

# 19. Corrected next frontier

DCRP-25 proposed:

$$
\text{Dual-Efficiency Rigidity}.
$$

DCRP-26 replaces it by a more structural frontier:

$$
\boxed{
\textbf{
Critical-Reservoir Compactness / Escape Rigidity.
}
}
\tag{19.1}
$$

A useful theorem would prove:

> Given a singular-rooted normalized sequence with:
>
> $$
> A_k+D_k\to\infty,
> $$
>
> either:
>
> 1. after a secondary amplitude/profile normalization one obtains a nontrivial bounded-reservoir descendant to which DCRP-23--26 apply;
> 2. the divergence is carried by a retained concentration/pressure/spatial/scale defect;
> 3. the growing reservoir itself pays a non-summable physical dissipation/pressure tax;
> 4. the branch violates actual suitable-weak compactness or finite-energy scaling.

This is now the most direct next attack.

---

# 20. Source-status audit

## Smooth coarse-graining

Classical smooth coarse-graining establishes:

- the exact Reynolds/subgrid stress:

  $$
  R_\ell
  =
  S_\ell(u\otimes u)
  -
  U_\ell\otimes U_\ell;
  $$

- the signed interscale energy work:

  $$
  \Pi_\ell
  =
  -
  R_\ell:\nabla U_\ell.
  $$

The exact viscous SGS-energy equation used here follows by subtracting the resolved kinetic-energy equation from the spatially filtered fine kinetic-energy equation.

## Filtered Vortex Stretching and Subgrid Defects

The paper proves that:

- near-field filtered stretching is diffusion-coercive;
- differentiated commutator forcing is controlled by:

  $$
  \widetilde{\mathcal S}^{(3)};
  $$

- bounded increment defects have cylindrical Young profiles;
- the remaining obstruction-profile questions involve compactness and work efficiency.

DCRP-26 shows why direct two-work coercivity is not the correct way to close that efficiency problem.

---

# 21. End state

The exact algebraic NO-GO is:

$$
\boxed{
F=c\cdot\nabla U
\neq0
\quad\text{but}\quad
\langle F,U\rangle
=
\langle F,-\Delta U\rangle
=
0.
}
$$

Thus energy/enstrophy work pairings are not coercive on active stress forces.

The correct recurrent identity is:

$$
\boxed{
K_R(s_1)
-
K_R(s_0)
+
D_R^{sgs}
=
W_R
+
L_R^{sgs}.
}
$$

Hence:

$$
\boxed{
D_R^{sgs}
\le
(W_R)_+
+
|L_R^{sgs}|
+
|
K_R(s_1)-K_R(s_0)
|.
}
$$

If the right side vanishes on an exhaustion of normalized radii, the SGS gradient variance vanishes globally.

Then:

$$
\boxed{
u_\infty
\text{ is affine}
}
$$

and the bounded-reservoir Morrey growth forces:

$$
\boxed{
u_\infty=0.
}
$$

Therefore every nonzero recurrent bounded-reservoir strong increment profile has a finite normalized witness in:

$$
\boxed{
\text{forward SGS work}
\ \vee\
\text{localization/transport}
\ \vee\
\text{SGS return mismatch}
\ \vee\
\text{noncompactness}.
}
$$

Under compact strong-profile assumptions, finitely many fixed radii already give a uniform positive recurrence gap.

The active work-orthogonality kernel is therefore substantially closed.

The next single frontier is:

$$
\boxed{
\textbf{
Critical-Reservoir Compactness / Escape Rigidity.
}
}
$$