# NS-DCRP-18 — Trace-Erasure Action, Re-root Infrared Escape, and Two-Sided Scale-Carrier Completion

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. test the DCRP-17 Supplier Excursion Irreversibility proposal rigorously;
  2. prove the strongest valid fixed-frame trace-erasure action inequality;
  3. audit whether that inequality survives the scale-changing MORP return normalization;
  4. complete the relative-frequency package in the missing infrared direction;
  5. identify the correct next closure target.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - MORP-02 relative-frequency defect completion;
  - MORP-03 actual return/re-root semantics and return depletion ledger;
  - DCRP-14 finite-dimensional solenoidal supplier trace window;
  - DCRP-15 finite-window trace/residual realization;
  - DCRP-16 local supplier capture;
  - DCRP-17 supplier stopping-time synchronization.
- external primary calibration:
  - Runlong Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier-Stokes*, arXiv:2606.15086v1;
  - Runlong Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322v1.
- no novelty / priority claim is made without independent audit.

---

# 1. Executive result

DCRP-17 proposed the following closure strategy:

$$
\boxed{
\text{supplier trace }c\nu
\longrightarrow
\text{later invisible trace }0
\Longrightarrow
\text{strict irreversible return tax}.
}
\tag{1.1}
$$

The first implication can be made rigorous **only in a fixed normalization frame**.

The trace space from DCRP-14 may be chosen to be a finite Stokes spectral window

$$
\boxed{
H_\ast
=
\operatorname{span}
\{
\psi_1,\ldots,\psi_N
\},
}
\tag{1.2}
$$

where the

$$
\psi_j
$$

are divergence-free Dirichlet Stokes eigenfunctions on the fixed observation ball:

$$
\boxed{
A_S\psi_j
=
\mu_j\psi_j,
\qquad
0<\mu_1\le\cdots\le\mu_N.
}
\tag{1.3}
$$

For a supplier nonlinear increment

$$
h
$$

satisfying a forced Stokes equation, define trace coefficients

$$
\boxed{
a_j(\tau)
=
\langle
h(\tau),
\psi_j
\rangle.
}
\tag{1.4}
$$

Then exactly:

$$
\boxed{
a'(\tau)
+
\nu M a(\tau)
=
f(\tau),
}
\tag{1.5}
$$

where

$$
M
=
\operatorname{diag}
(
\mu_1,\ldots,\mu_N
)
$$

and

$$
f
$$

is the finite-dimensional projection of the actual nonlinear stress forcing.

If

$$
|a(\tau_s)|
\ge
A_0
$$

and

$$
|a(\tau_r)|
\le
\varepsilon<A_0,
$$

then:

$$
\boxed{
\nu
\int_{\tau_s}^{\tau_r}
a^TMa\,d\tau
+
\nu^{-1}
\int_{\tau_s}^{\tau_r}
f^TM^{-1}f\,d\tau
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
}
\tag{1.6}
$$

Thus:

$$
\boxed{
\textbf{
fixed-frame supplier trace erasure carries a uniform positive action.
}
}
\tag{1.7}
$$

However the crucial audit result of this round is:

$$
\boxed{
\textbf{
fixed-frame trace erasure}
\neq
\textbf{
scale-re-root trace erasure}.
}
}
\tag{1.8}
$$

If a supplier shell is physically unchanged but the next MORP window re-roots at a scale larger by

$$
\Gamma>1,
$$

then its normalized representation changes from

$$
w(y)
$$

to

$$
\boxed{
w_\Gamma(y)
=
\Gamma^{-1}
w
\left(
\Gamma^{-1}y
\right).
}
\tag{1.9}
$$

Its normalized frequency moves from order one to order

$$
\Gamma^{-1},
$$

and every fixed unit-frequency trace detector sees it vanish as

$$
\Gamma\to\infty,
$$

even though the physical supplier has not dissipated.

Therefore the DCRP-17 plan

$$
\text{trace disappears}
\Rightarrow
\text{physical irreversible tax}
$$

is false for a scale-changing return unless the old supplier scale is explicitly retained.

This exposes a concrete incompleteness in the current MORP-02 scale compactification.

MORP-02 defines relative-frequency shells only for

$$
m\ge0
$$

relative to the terminal reference shell and compactifies

$$
\mathbb N_0
$$

by one point

$$
+\infty.
$$

It detects ultraviolet scale escape.

It does **not** retain an older supplier that, after a higher-frequency re-root, moves to

$$
m<0
$$

and eventually

$$
m\to-\infty.
$$

The missing coordinate is an **infrared relative-scale defect**.

This round introduces the two-sided compactification

$$
\boxed{
\overline{\mathbb Z}
=
\mathbb Z
\cup
\{
-\infty,+\infty
\}.
}
\tag{1.10}
$$

The scale-critical kinetic shell carrier is

$$
\boxed{
\mathcal K_q(t)
=
\lambda_q
\|u_q(t)\|_2^2.
}
\tag{1.11}
$$

It is exactly invariant under Navier--Stokes parabolic scaling.

At a supplier time:

$$
\boxed{
\mathcal K_q(t_s)
\ge
\kappa_0\nu^2.
}
\tag{1.12}
$$

Let a later supplier/re-root have reference shell

$$
q'=q+L.
$$

Then one of the following must occur.

### Persistence

If:

$$
\mathcal K_q(t_r)
\ge
\frac{
\kappa_0
}{
2
}
\nu^2,
$$

then the old supplier survives as a scale-critical carrier at relative shell

$$
m=-L.
$$

For:

$$
L\to\infty,
$$

it becomes a nonzero infrared escape carrier at

$$
-\infty.
$$

### Depletion

If:

$$
\mathcal K_q(t_r)
<
\frac{
\kappa_0
}{
2
}
\nu^2,
$$

the exact shell-energy equation gives:

$$
\boxed{
\nu\lambda_q
\int_{t_s}^{t_r}
\|\nabla u_q\|_2^2dt
+
\lambda_q
\left(
-\int_{t_s}^{t_r}
\mathcal T_q(t)\,dt
\right)_+
\ge
\frac{
\kappa_0
}{
4
}
\nu^2.
}
\tag{1.13}
$$

Thus actual loss of the old supplier pays a fixed scale-critical viscous/outgoing-transfer action.

### Spatial escape

If the old supplier remains physically nonzero but leaves every bounded normalized spatial neighborhood of the return center, the carrier is a spatial-escape defect of the type already contemplated in MORP-02.

Therefore:

$$
\boxed{
\textbf{
old supplier}
\Longrightarrow
\textbf{
finite-relative / IR carrier}
\ \vee\
\textbf{
critical depletion}
\ \vee\
\textbf{
spatial escape}.
}
}
\tag{1.14}
$$

This is the strongest valid excursion statement obtained in this round.

It also forces a correction to DCRP-17.

DCRP-17 proved compactness of the **fixed finite-dimensional supplier window**.

That is valid windowwise.

But transition-complete compactness of an infinite supplier return chain is not established unless the missing infrared carrier is added.

Hence:

$$
\boxed{
\textbf{
supplier window COM}
\neq
\textbf{
transition-complete supplier COM}.
}
}
\tag{1.15}
$$

The supplier excursion problem therefore does not reduce to trace ODE irreversibility.

The correct closure-facing problem is now:

$$
\boxed{
\textbf{
Two-Sided Scale-Carrier / Critical-Supply Taxation Lemma}.
}
\tag{1.16}
$$

This re-routing is consistent with the unconditional finite-scale critical ledger of arXiv:2606.15086:

a persistent non-CKN branch requires cumulative untaxed critical supply or accumulated leakage.

The supplier analysis has now shown how an individual local critical supplier is:

- state-visible;
- trace-visible or residual-paid;
- actual-history generated;
- and, after re-root, either retained as a two-sided scale carrier or depleted at fixed critical action.

What remains is to prove that the **positive-density critical supply required by a persistent bad branch cannot all evade taxation by passing through scale re-rooting / infrared escape**.

That is the next exact target.

---

# 2. Refinement of the DCRP-14 trace window

DCRP-14 constructed a finite-dimensional space

$$
H_\ast
\subset
C_c^\infty(B_R;\mathbb R^3)
$$

of divergence-free fields satisfying a uniform supplier projection gap.

For the trace-evolution argument it is useful to choose the finite-dimensional space from the spectral decomposition of the Dirichlet Stokes operator on

$$
B_R.
$$

Let:

$$
A_S
$$

denote the positive self-adjoint Stokes operator on the divergence-free

$$
L^2
$$

space with zero boundary condition.

Its eigenfunctions form a complete orthonormal basis:

$$
\boxed{
A_S\psi_j
=
\mu_j\psi_j.
}
\tag{2.1}
$$

The density argument used in DCRP-14 remains valid with the increasing spectral spaces

$$
\boxed{
H_N
=
\operatorname{span}
\{
\psi_1,\ldots,\psi_N
\}.
}
\tag{2.2}
$$

Because the normalized supplier class is locally compact and the full solenoidal projection has a uniform positive lower bound, there exists

$$
N_\ast<\infty
$$

such that:

$$
\boxed{
\|
\Pi_{H_{N_\ast}}
h
\|_2
\ge
c_\ast\nu
}
\tag{2.3}
$$

for every normalized supplier nonlinear increment.

Thus, without loss of the DCRP-14 trace lift, one may take:

$$
\boxed{
H_\ast
=
H_{N_\ast}.
}
\tag{2.4}
$$

Status:

$$
\boxed{
\textbf{PROVED by the same compact finite-dimensional approximation argument as DCRP-14}.
}
$$

---

# 3. Exact finite-dimensional trace evolution

Let:

$$
h(\tau)
$$

be a normalized divergence-free supplier increment satisfying:

$$
\boxed{
\partial_\tau h
-
\nu\Delta h
+
\nabla\pi
=
-\nabla\cdot T.
}
\tag{3.1}
$$

Let:

$$
\psi_j
$$

be a Dirichlet Stokes eigenfunction.

Define:

$$
\boxed{
a_j(\tau)
=
\int_{B_R}
h(y,\tau)
\cdot
\psi_j(y)
\,dy.
}
\tag{3.2}
$$

Testing (3.1) against:

$$
\psi_j,
$$

the pressure term vanishes because:

$$
\nabla\cdot\psi_j=0
$$

and:

$$
\psi_j|_{\partial B_R}=0.
$$

Also:

$$
\int
\nabla h:\nabla\psi_j
=
\mu_j
\int
h\cdot\psi_j.
$$

Therefore:

$$
\boxed{
a_j'
+
\nu\mu_j a_j
=
f_j,
}
\tag{3.3}
$$

where:

$$
\boxed{
f_j(\tau)
=
\int_{B_R}
T(y,\tau):
\nabla\psi_j(y)
\,dy.
}
\tag{3.4}
$$

Let:

$$
a
=
(a_1,\ldots,a_N)^T,
$$

$$
f
=
(f_1,\ldots,f_N)^T,
$$

and:

$$
\boxed{
M
=
\operatorname{diag}
(
\mu_1,\ldots,\mu_N
).
}
\tag{3.5}
$$

Then:

$$
\boxed{
a'
+
\nu Ma
=
f.
}
\tag{3.6}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. NEW THEOREM — Fixed-Frame Trace-Erasure Action Gap

## Theorem 4.1

Suppose:

$$
a:
[\tau_s,\tau_r]
\to
\mathbb R^N
$$

satisfies:

$$
a'
+
\nu Ma
=
f,
$$

where:

$$
M
$$

is symmetric positive definite.

Assume:

$$
\boxed{
|a(\tau_s)|
\ge
A_0,
}
\tag{4.1}
$$

and:

$$
\boxed{
|a(\tau_r)|
\le
\varepsilon
<
A_0.
}
\tag{4.2}
$$

Then:

$$
\boxed{
\nu
\int_{\tau_s}^{\tau_r}
a^TMa\,d\tau
+
\nu^{-1}
\int_{\tau_s}^{\tau_r}
f^TM^{-1}f\,d\tau
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
}
\tag{4.3}
$$

### Proof

Take the Euclidean inner product of:

$$
a'
+
\nu Ma
=
f
$$

with:

$$
a.
$$

Then:

$$
\frac12
\frac d{d\tau}
|a|^2
+
\nu a^TMa
=
a^Tf.
$$

Integrate from:

$$
\tau_s
$$

to:

$$
\tau_r.
$$

Set:

$$
D
=
\nu
\int
a^TMa,
$$

and:

$$
F
=
\nu^{-1}
\int
f^TM^{-1}f.
$$

Then:

$$
\frac12
\left(
|a(\tau_s)|^2
-
|a(\tau_r)|^2
\right)
=
D
-
\int
a^Tf.
$$

By Cauchy--Schwarz in the

$$
M/M^{-1}
$$

pairing:

$$
\left|
\int
a^Tf
\right|
\le
\sqrt{DF}.
$$

Thus:

$$
\frac12
\left(
A_0^2-\varepsilon^2
\right)
\le
D+\sqrt{DF}.
$$

Since:

$$
\sqrt{DF}
\le
\frac{
D+F
}{
2
},
$$

$$
D+\sqrt{DF}
\le
\frac32
(D+F).
$$

Therefore:

$$
D+F
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Supplier consequence in one fixed normalization frame

At supplier time:

$$
\tau_s,
$$

DCRP-14 gives:

$$
\boxed{
|a(\tau_s)|
\ge
c_\ast\nu.
}
\tag{5.1}
$$

If, in the **same normalized frame and same trace space**,

$$
|a(\tau_r)|
\le
\frac{
c_\ast
}{
2
}
\nu,
$$

Theorem 4.1 gives:

$$
\boxed{
\nu
\int_{\tau_s}^{\tau_r}
a^TMa
+
\nu^{-1}
\int_{\tau_s}^{\tau_r}
f^TM^{-1}f
\ge
c_A\nu^2,
}
\tag{5.2}
$$

where:

$$
c_A
=
\frac{
c_\ast^2
}{
4
}.
$$

Thus the fixed-frame trace cannot disappear without a fixed viscous/forcing action.

This validates one part of the DCRP-17 intuition.

---

# 6. CRITICAL NO-GO — scale re-root can erase a fixed trace for free

The MORP return is not generally a fixed-frame evolution.

It contains parabolic re-rooting.

Suppose a physical supplier field at scale:

$$
\lambda
$$

is represented in its own normalized coordinates by:

$$
\boxed{
w(y)
=
\lambda^{-1}
u_{\rm sup}
\left(
x_\ast+\lambda^{-1}y
\right).
}
\tag{6.1}
$$

Suppose the next return uses a reference scale:

$$
\lambda'
=
\Gamma\lambda,
\qquad
\Gamma>1.
$$

Represent the **same unchanged physical field** in the new coordinates:

$$
w^{new}(y)
=
(\lambda')^{-1}
u_{\rm sup}
\left(
x_\ast+(\lambda')^{-1}y
\right).
$$

Using (6.1):

$$
u_{\rm sup}
\left(
x_\ast+(\lambda')^{-1}y
\right)
=
\lambda
w
\left(
\lambda(\lambda')^{-1}y
\right).
$$

Therefore:

$$
\boxed{
w^{new}(y)
=
\Gamma^{-1}
w
\left(
\Gamma^{-1}y
\right).
}
\tag{6.2}
$$

The amplitude acquires:

$$
\Gamma^{-1},
$$

and the normalized Fourier support moves from:

$$
|\xi|\sim1
$$

to:

$$
|\xi|\sim\Gamma^{-1}.
$$

Hence for every fixed unit-annulus trace window:

$$
H_\ast,
$$

$$
\boxed{
\|
\Pi_{H_\ast}
w^{new}
\|_2
\to0
\qquad
(\Gamma\to\infty)
}
\tag{6.3}
$$

even though:

- the physical field is unchanged;
- no viscosity acted;
- no nonlinear transfer occurred.

Therefore:

$$
\boxed{
\textbf{
normalized trace disappearance across a scale-changing return
does not imply physical depletion.
}
}
\tag{6.4}
$$

Status:

$$
\boxed{
\textbf{NO-GO PROVED}.
}
$$

This invalidates a direct use of Theorem 4.1 as the complete MORP return-depletion theorem.

---

# 7. What happened to the old supplier?

The old supplier did not disappear.

It moved to a lower **relative** frequency.

If the later reference shell is:

$$
q'=q+L,
$$

then the old shell:

$$
q
$$

has relative index:

$$
\boxed{
m=q-q'=-L.
}
\tag{7.1}
$$

For:

$$
L\to\infty,
$$

$$
\boxed{
m\to-\infty.
}
\tag{7.2}
$$

Thus the correct language is:

$$
\boxed{
\textbf{
re-root visibility loss}
=
\textbf{
infrared relative-scale escape}
}
}
\tag{7.3}
$$

unless the physical supplier itself is depleted.

---

# 8. Audit of MORP-02 relative-scale completion

MORP-02 defines a terminal reference shell:

$$
J_n.
$$

It then defines relative shells only for:

$$
\boxed{
m\ge0,
}
\tag{8.1}
$$

and places the selected-time carrier on:

$$
\boxed{
\overline{\mathbb N}_0
=
\mathbb N_0
\cup
\{
+\infty
\}.
}
\tag{8.2}
$$

The resulting defect completion retains:

$$
\boxed{
\text{UV relative-frequency escape}.
}
\tag{8.3}
$$

But a previous supplier under a later/higher re-root has:

$$
m<0.
$$

Therefore the current one-sided compactification does not retain:

$$
\boxed{
\text{IR relative-frequency escape}.
}
\tag{8.4}
$$

This is a genuine transition-completeness gap.

---

# 9. Two-sided relative-frequency completion

Define:

$$
\boxed{
\overline{\mathbb Z}
=
\mathbb Z
\cup
\{
-\infty,+\infty
\}.
}
\tag{9.1}
$$

Use the order topology / two-point compactification.

For a normalized state whose reference physical shell is:

$$
J_n,
$$

the physical shell:

$$
J_n+m
$$

corresponds to normalized relative frequency:

$$
2^m.
$$

Define the scale-critical kinetic shell carrier:

$$
\boxed{
\kappa_{n,m}
=
2^m
\|
P_mU_n
\|_2^2.
}
\tag{9.2}
$$

For the global normalized state:

$$
U_n(y)
=
2^{-J_n}
u
\left(
x_n+2^{-J_n}y,
t_n
\right),
$$

one has, up to the bounded dyadic partition convention,

$$
\boxed{
\kappa_{n,m}
=
2^{J_n+m}
\|
u_{J_n+m}(t_n)
\|_2^2.
}
\tag{9.3}
$$

Thus:

$$
\boxed{
\kappa_{n,m}
}
$$

is exactly parabolic-scale invariant.

For a localized carrier, the same identity holds modulo the explicit localization/spatial-tail residual.

---

# 10. Supplier critical shell lower bound

At a local supplier event from DCRP-16:

$$
\lambda_q^{-1}
\|u_q\|_\infty
\ge
c_{\rm loc}\nu.
$$

Bernstein yields:

$$
\boxed{
\mathcal K_q
:=
\lambda_q
\|u_q\|_2^2
\ge
\kappa_0\nu^2
}
\tag{10.1}
$$

for:

$$
\kappa_0>0.
$$

This is exactly the carrier:

$$
\kappa_{n,0}
$$

when the supplier shell itself is chosen as the reference scale.

---

# 11. Exact shell-energy ledger

For a fixed physical shell:

$$
q,
$$

the exact kinetic-shell identity is:

$$
\boxed{
\frac12
\frac d{dt}
\|u_q\|_2^2
+
\nu
\|\nabla u_q\|_2^2
=
\mathcal T_q(t),
}
\tag{11.1}
$$

where:

$$
\mathcal T_q
$$

is the signed nonlinear transfer **into** shell:

$$
q.
$$

Multiply by:

$$
\lambda_q
$$

and integrate:

$$
\boxed{
\frac12
\left[
\mathcal K_q(t_1)
-
\mathcal K_q(t_0)
\right]
+
\nu\lambda_q
\int_{t_0}^{t_1}
\|\nabla u_q\|_2^2dt
=
\lambda_q
\int_{t_0}^{t_1}
\mathcal T_q(t)\,dt.
}
\tag{11.2}
$$

Every term has critical scaling.

---

# 12. NEW THEOREM — Tagged Supplier Depletion / IR-Escape Alternative

## Theorem 12.1

Let:

$$
t_s<t_r
$$

be two times on one actual Navier--Stokes history.

Assume shell:

$$
q
$$

is a supplier at:

$$
t_s:
$$

$$
\boxed{
\mathcal K_q(t_s)
\ge
\kappa_0\nu^2.
}
\tag{12.1}
$$

Then exactly one of the following broad alternatives holds.

### Persistent old supplier

$$
\boxed{
\mathcal K_q(t_r)
\ge
\frac{
\kappa_0
}{
2
}
\nu^2.
}
\tag{12.2}
$$

If the return reference shell is:

$$
q_r>q,
$$

the old supplier appears as a nonzero two-sided relative-scale carrier at:

$$
\boxed{
m=q-q_r<0.
}
\tag{12.3}
$$

If:

$$
q_r-q\to\infty,
$$

this is a nonzero IR escape carrier at:

$$
-\infty.
$$

### Depleted old supplier

$$
\boxed{
\mathcal K_q(t_r)
<
\frac{
\kappa_0
}{
2
}
\nu^2.
}
\tag{12.4}
$$

Then:

$$
\boxed{
\nu\lambda_q
\int_{t_s}^{t_r}
\|\nabla u_q\|_2^2dt
+
\left[
-\lambda_q
\int_{t_s}^{t_r}
\mathcal T_q(t)\,dt
\right]_+
\ge
\frac{
\kappa_0
}{
4
}
\nu^2.
}
\tag{12.5}
$$

### Proof of the depletion estimate

From (11.2):

$$
\frac12
\left[
\mathcal K_q(t_s)
-
\mathcal K_q(t_r)
\right]
=
\nu\lambda_q
\int
\|\nabla u_q\|_2^2
-
\lambda_q
\int
\mathcal T_q.
$$

Under (12.1) and (12.4):

$$
\frac12
\left[
\mathcal K_q(t_s)
-
\mathcal K_q(t_r)
\right]
\ge
\frac{
\kappa_0
}{
4
}
\nu^2.
$$

For any:

$$
D\ge0
$$

and:

$$
X\in\mathbb R,
$$

$$
D+(-X)_+
\ge
D-X.
$$

Apply:

$$
D
=
\nu\lambda_q
\int
\|\nabla u_q\|_2^2,
$$

$$
X
=
\lambda_q
\int
\mathcal T_q.
$$

This gives (12.5).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. Spatial completion

Theorem 12.1 uses the global shell carrier.

For a local supplier package, one must also track spatial position.

If:

$$
\mathcal K_q(t_r)
$$

remains large globally but the shell carrier leaves every bounded normalized spatial neighborhood of the return center, then the supplier is not locally depleted.

It has undergone:

$$
\boxed{
\textbf{
spatial carrier escape}.
}
}
\tag{13.1}
$$

MORP-02 already allows one-point compactification of normalized spatial carrier measures.

Thus the local version of Theorem 12.1 is:

$$
\boxed{
\textbf{
old supplier}
\Longrightarrow
\textbf{
finite/IR scale carrier}
\ \vee\
\textbf{
spatial escape}
\ \vee\
\textbf{
critical depletion}.
}
}
\tag{13.2}
$$

---

# 14. Scale re-root no longer counts as "free disappearance"

After adding the infrared scale coordinate:

- a physically persistent old supplier cannot vanish merely because the reference frequency increased;
- if it is no longer visible at finite relative scale, it appears at:

  $$
  -\infty;
  $$

- if it is no longer spatially local, it appears in the spatial escape coordinate;
- if neither carrier remains, Theorem 12.1 gives a fixed critical depletion action.

Thus:

$$
\boxed{
\textbf{
re-root trace disappearance}
\Longrightarrow
\textbf{
IR/spatial defect}
\ \vee\
\textbf{
physical depletion}.
}
}
\tag{14.1}
$$

This is the corrected form of DCRP-17's excursion intuition.

---

# 15. CORRECTION — DCRP-17 supplier compactness claim

DCRP-17 proved compactness of the supplier package after projection to one fixed finite-dimensional normalized supplier window.

That statement remains valid.

However an infinite supplier return chain changes the reference frequency.

The fixed window does not contain all older negative relative shells.

Therefore:

$$
\boxed{
\text{fixed-window supplier COM}
}
$$

does not imply:

$$
\boxed{
\text{transition-complete supplier COM}.
}
$$

Without two-sided relative-scale completion, an infinite amount of old supplier history may escape into:

$$
m\to-\infty.
$$

Accordingly, DCRP-17's phrase:

$$
\boxed{
\text{Supplier COM closed}
}
$$

must be read only as:

$$
\boxed{
\text{Supplier fixed-window COM closed}.
}
$$

Transition-complete compactness remains open.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 16. Why two-sided completion still does not prove a contradiction

Suppose every old supplier is eventually depleted.

Then Theorem 12.1 supplies a fixed critical depletion action for each tag.

However new supplier shells are also generated at later scales.

A forward cascade may have the schematic form:

$$
\boxed{
\text{old supplier depletion}
+
\text{new supplier creation}.
}
\tag{16.1}
$$

The positive loss of one shell can be compensated by positive supply to the next shell.

Physical kinetic energy permits this because the raw energy per scale is:

$$
O(\lambda_q^{-1}),
$$

which is geometrically summable.

Therefore:

$$
\boxed{
\text{fixed critical depletion per supplier}
\not\Rightarrow
\text{global energy contradiction}.
}
\tag{16.2}
$$

This is the old Critical Barrier Accumulation obstruction in a sharper tagged-shell form.

---

# 17. Why fixed-frame trace action is not a MORP return tax by itself

Theorem 4.1 proves a positive action whenever one fixed trace genuinely decays in one fixed frame.

But an excursion may have:

$$
\boxed{
\text{positive forcing}
\to
\text{visible supplier}
\to
\text{viscous/forward transfer loss}
}
\tag{17.1}
$$

and still return to a new invisible normalized state.

The action is real.

What is not automatic is the MORP inequality:

$$
\boxed{
\mathfrak J(D^+)
+
\Delta_{\rm exc}
\le
\mathfrak J(D^-).
}
\tag{17.2}
$$

The supplier can be created by incoming critical supply.

Therefore:

$$
\boxed{
\textbf{
action cost}
\neq
\textbf{
net return depletion}.
}
}
\tag{17.3}
$$

Status:

$$
\boxed{
\textbf{LOGICAL NO-GO}.
}
$$

This is why the next route must return to the full critical supply/tax ledger.

---

# 18. External finite-scale critical ledger

The finite-window audit theorem of arXiv:2606.15086 proves an unconditional finite-scale survival alternative.

Along a persistent non-CKN scale-window chain:

$$
\boxed{
\sum_{k=0}^{N-1}
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\lambda_0
\varepsilon
N
-
B_0
-
\sum_{k=0}^{N-1}
\mathrm{Leak}^{full}_k.
}
\tag{18.1}
$$

Thus if leakage has vanishing average, a persistent bad branch requires **positive-density untaxed critical supply**.

This theorem identifies the correct global resource problem.

The question is not merely:

> does a supplier excursion pay something?

It is:

> can the positive critical supply required to perpetuate the bad branch remain **untaxed** after the DCRP supplier / PFET / trace / two-sided-scale completion is applied?

This is the correct closure-facing formulation.

---

# 19. What DCRP has already established about critical supply

The current DCRP chain supplies the following modules.

### Local source

DCRP-16:

$$
\boxed{
\text{local singular point}
\Longrightarrow
\text{local critical supplier sequence}.
}
\tag{19.1}
$$

### Actual nonlinear ancestry

DCRP-09:

$$
\boxed{
\text{supplier}
\Longrightarrow
\text{same-history nonlinear forcing}.
}
\tag{19.2}
$$

### Positive net shell supply

DCRP-10:

$$
\boxed{
\lambda_Q
\int_I
\mathcal T_Q
\ge
c\nu^2
}
\tag{19.3}
$$

on first-crossing intervals.

### Heat-filter PFET / backscatter alternative

DCRP-11:

$$
\boxed{
\text{forward heat work}
\ \vee\
\text{backscatter}
}
\tag{19.4}
$$

with fixed critical amount.

### Local package completion

DCRP-12:

$$
\boxed{
\text{local PFET}
\ \vee\
\text{paid backscatter}
\ \vee\
\text{work escape}.
}
\tag{19.5}
$$

### Supplier trace/residual gap

DCRP-15:

$$
\boxed{
\|
O_W^T
\|
+
C
\mathcal B_{\rm sup}^{res}
\ge
c\nu.
}
\tag{19.6}
$$

### Re-root completion

DCRP-18:

$$
\boxed{
\text{persistent old supplier}
\Longrightarrow
\text{finite/IR scale carrier or spatial escape},
}
\tag{19.7}
$$

while actual loss gives:

$$
\boxed{
\text{critical viscous/outgoing-transfer action}.
}
\tag{19.8}
$$

Thus individual supplier events are no longer structurally invisible.

---

# 20. What is still missing from the finite-scale ledger

The survival theorem (18.1) does not say that every critical supply event must cross the particular supplier threshold:

$$
\lambda_q^{-1}
\|u_q\|_\infty
\gtrsim
\nu.
$$

A persistent bad branch could, in principle, distribute its required critical supply over:

- many frequency shells;
- many spatial cells;
- pressure transport;
- unresolved oscillation;
- long moving windows;

without one individual supply event becoming a DCRP supplier atom at every ledger step.

Therefore:

$$
\boxed{
\textbf{
supplier taxation}
\neq
\textbf{
all critical-supply taxation}.
}
}
\tag{20.1}
$$

This is now the exact remaining global gap.

---

# 21. Corrected next frontier

The DCRP-17 target:

$$
\text{Supplier Excursion Irreversibility}
$$

is replaced by:

$$
\boxed{
\textbf{
Critical Supply Taxation / Untaxed-Supply Capture Lemma}.
}
\tag{21.1}
$$

A sufficient theorem would prove:

> Along every sufficiently late local non-CKN transition whose full critical ledger has
>
> $$
> \left(
> \mathrm{Sup}^{full}
> -
> \mathrm{Tax}^{full}
> \right)_+
> \ge
> \eta>0,
> $$
>
> at least one of the following occurs:
>
> 1. a local supplier atom is produced and therefore enters the DCRP trace/PFET/residual package;
> 2. the supply is spatially or spectrally diffuse and produces a nonzero completed work/scale/spatial defect;
> 3. pressure/localization leakage carries a fixed amount;
> 4. a paid/backscatter channel is already positive.

If the above alternatives have a scale-uniform quantitative lower bound, then the positive-density untaxed supply required by (18.1) cannot remain untaxed.

Combined with vanishing-average leakage, the persistent non-CKN branch would be impossible.

This is now a direct route from an unconditional finite-scale ledger to regularity.

---

# 22. Two-sided relative-scale probability versus absolute carrier

A technical choice remains.

MORP-02 normalizes its scale distribution to a probability measure.

For the old supplier, one has an **absolute** critical lower bound:

$$
\mathcal K_q\ge\kappa_0\nu^2.
$$

Normalizing by a total carrier that may diverge can make this supplier's probability share vanish.

Therefore the two-sided completion should retain both:

1. a normalized probability distribution describing relative carrier geometry;
2. an absolute critical carrier amplitude coordinate.

A useful package is:

$$
\boxed{
\left(
A_n^{sc},
\sigma_n^{sc}
\right),
}
\tag{22.1}
$$

where:

$$
A_n^{sc}
=
\sum_m
\kappa_{n,m}
$$

when finite, or its extended-value defect completion, and:

$$
\sigma_n^{sc}
=
(A_n^{sc})^{-1}
\sum_m
\kappa_{n,m}\delta_m.
$$

This prevents a fixed absolute supplier atom from disappearing merely because the total critical norm diverges.

No compactness claim is made here when:

$$
A_n^{sc}\to\infty.
$$

That divergence itself is a native critical-norm defect.

---

# 23. New compactness boundary

The two-sided completion produces the following alternatives.

### Finite total critical carrier

If:

$$
\sup_n
A_n^{sc}
<
\infty,
$$

the two-sided carrier measures are weak-star compact on:

$$
\overline{\mathbb Z}.
$$

### Divergent critical carrier

If:

$$
A_n^{sc}\to\infty,
$$

the state has a divergent:

$$
\dot H^{1/2}
$$

-type shell carrier.

This is not a contradiction.

It is a noncompact critical-norm branch.

Thus transition-complete supplier compactness itself reduces to:

$$
\boxed{
\text{finite two-sided carrier}
\ \vee\
\text{critical-norm blowup}.
}
\tag{23.1}
$$

The latter is compatible with a hypothetical singularity and therefore must be handled dynamically rather than discarded.

---

# 24. Implication for the "proof-space contraction" assessment

The supplier route has not returned to the original unstructured problem.

The remaining obstruction is now highly specific.

A hypothetical singular branch must support:

$$
\boxed{
\textbf{
positive-density scale-critical supply that remains profitable after:
}
}
$$

- local supplier capture;
- pressure/flux observation;
- backscatter taxation;
- finite-window trace separation;
- projection/residual cleaning;
- spatial escape completion;
- UV scale completion;
- IR scale completion;
- tagged-shell depletion accounting.

This is a much narrower object than the original generic blowup branch.

But it is also recognizably the central cascade problem:

$$
\boxed{
\textbf{
can Navier--Stokes sustain a profitable critical energy cascade
to arbitrarily small scales without entering a regularity basin?
}
}
\tag{24.1}
$$

That question is not yet answered by the present corpus.

---

# 25. Preferred next attack

The next round should work directly with the unconditional critical ledger rather than with endpoint trace disappearance.

Let:

$$
Q_k\to Q_{k+1}
$$

be one local singular scale transition.

Let:

$$
\mathrm{Sup}^{full}_k
$$

be decomposed into:

- nonlinear flux supply;
- pressure transport supply;
- localization leakage / residual.

The goal is a **supply-to-carrier decomposition**:

$$
\boxed{
\mathrm{Sup}^{full}_k
\le
C
\left[
\mathrm{TaxedSupplier}_k
+
\mathrm{DiffuseDefect}_k
+
\mathrm{Leak}_k
+
\mathrm{Tax}^{full}_k
\right].
}
\tag{25.1}
$$

with constants independent of:

$$
k.
$$

Here:

$$
\mathrm{TaxedSupplier}_k
$$

must be controlled by the already established DCRP PFET/trace/residual modules.

Then:

$$
\boxed{
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
}
$$

can remain large only if:

$$
\mathrm{DiffuseDefect}_k
+
\mathrm{Leak}_k
$$

is large.

If both have vanishing average, Theorem 3.3 of the finite-window audit gives a contradiction with persistent badness.

This is the cleanest current closure target.

---

# 26. Source audit

## Finite-Window Singularity Audits and Local-to-Clean Defect Transfer

Runlong Yu, arXiv:2606.15086v1.

The paper proves unconditionally that along every admissible non-CKN scale-window chain:

$$
B_{k+1}
-
(1-\lambda_0)
B_k
\le
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
+
\mathrm{Leak}^{full}_k,
$$

and consequently:

$$
\sum_{k<N}
\left(
\mathrm{Sup}^{full}_k
-
\mathrm{Tax}^{full}_k
\right)_+
\ge
\lambda_0\varepsilon N
-
B_0
-
\sum_{k<N}
\mathrm{Leak}^{full}_k.
$$

Thus persistent badness requires cumulative untaxed supply or leakage.

The paper explicitly lists uniform taxation/observable depletion of all critical supply as an open input.

DCRP-18 adopts that exact open interface as the next target.

## Coarse-Grained Resolution and Pressure-Flux Work Depletion

Runlong Yu, arXiv:2606.25322v1.

This paper proves an exact fixed-chain pressure--flux work telescope:

- forward combined work;
- resolved dissipation;

are paid by:

- initial localized kinetic energy;
- explicit localization leakage;
- negative combined work/backscatter.

DCRP-11/12 already used this sign structure.

The remaining issue is not the fixed-chain work identity.

It is the quantitative capture of all critical supply appearing in the full singularity ledger.

---

# 27. End state

The strongest new fixed-frame theorem is:

$$
\boxed{
\textbf{
Trace-Erasure Action Gap}
}
$$

$$
\boxed{
\nu
\int
a^TMa
+
\nu^{-1}
\int
f^TM^{-1}f
\ge
\frac{
A_0^2-\varepsilon^2
}{
3
}.
}
$$

But scale re-rooting produces the exact NO-GO:

$$
\boxed{
w^{new}(y)
=
\Gamma^{-1}
w(\Gamma^{-1}y),
}
$$

so a fixed unit-scale trace may vanish with no physical depletion.

The missing object is infrared relative-scale escape.

After two-sided scale completion, every old supplier satisfies:

$$
\boxed{
\text{finite/IR carrier}
\ \vee\
\text{spatial escape}
\ \vee\
\text{critical depletion}.
}
$$

This corrects the transition-complete compactness picture.

The excursion problem is therefore not primarily a trace-irreversibility problem.

It is a **critical supply taxation problem**.

The next single frontier is:

$$
\boxed{
\textbf{
Critical Supply Taxation / Untaxed-Supply Capture Lemma}.
}
$$

If every positive-density critical supply required by the unconditional finite-scale survival theorem can be routed into:

- DCRP supplier/PFET/trace taxation;
- paid backscatter;
- completed diffuse scale/spatial/work defects;
- or localization leakage,

then the persistent non-CKN branch has no untaxed mechanism left.

That is the next exact attack.
