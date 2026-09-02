# NS-DCRP-27 — Critical-Reservoir Absorption, Amplitude–Shape Completion, and Type-II Euler–Reynolds Reprofiling

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. remove "critical-reservoir blowup" as an undifferentiated escape label;
  2. prove that bounded local energy and pressure reservoirs force an eventual uniform dissipation bound along a nested chain;
  3. split every remaining compactness-guard failure into kinetic-energy amplitude, gradient/dissipation amplitude, or harmonic-pressure-tail amplitude;
  4. compactify these divergent reservoirs by native amplitude–shape coordinates;
  5. reprofile the kinetic-energy Type-II branch by an Euler-time normalization into a local Euler or Euler–Reynolds defect object;
  6. identify why compactness completion alone still does not supply coercive taxation.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - G. Seregin, *Remarks on Type II blowups of solutions to the Navier--Stokes equations*, arXiv:2304.04045;
  - D. Albritton, T. Barker, *On local Type I singularities of the Navier--Stokes equations and Liouville theorems*, arXiv:1811.00502;
  - T. Barker, C. Prange, *Localized smoothing for the Navier--Stokes equations and concentration of critical norms near singularities*, arXiv:1812.09115.
- principal internal calibration:
  - NS-MORP-02 defect-completed compactness package;
  - DCRP-23 through DCRP-26.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

MORP-02 does not assume an abstract compactness norm alone.

On a normalized cylinder it explicitly requires a uniform local suitable-weak bound of the form

$$
\boxed{
\|u\|_{L_t^\infty L_x^2}
+
\|\nabla u\|_{L^2}
+
\|p-(p)_B(t)\|_{L^{3/2}}
\le
M.
}
\tag{1.1}
$$

DCRP-23 introduced the bounded-reservoir branch using the scale-invariant local-energy and pressure coordinates

$$
A_k,
\qquad
D_k.
$$

A possible concern remained:

> bounded $A_k+D_k$ does not explicitly contain the gradient coordinate needed by MORP-02.

The first main result of DCRP-27 removes this concern.

Let

$$
r_{k+1}
=
\theta r_k,
\qquad
0<\theta<1
$$

be a fixed nested CKN chain.

If

$$
\boxed{
A_k
+
D_k
\le
M
\qquad
\forall k\ge k_0,
}
\tag{1.2}
$$

then the standard local interpolation and local energy inequality give

$$
\boxed{
E_{k+1}
\le
K_{M,\theta,\nu}
\left(
1
+
E_k^{3/4}
\right).
}
\tag{1.3}
$$

This recurrence is sublinear.

Therefore there exists a finite absorbing constant

$$
\boxed{
E_\ast
=
E_\ast(M,\theta,\nu)
<\infty
}
\tag{1.4}
$$

and an index

$$
k_1\ge k_0
$$

such that

$$
\boxed{
E_k\le E_\ast
\qquad
\forall k\ge k_1.
}
\tag{1.5}
$$

Consequently the cubic reservoir also becomes uniformly bounded:

$$
\boxed{
C_k
\le
C_\ast(M,E_\ast).
}
\tag{1.6}
$$

Thus

$$
\boxed{
\textbf{
bounded }A+D\textbf{ on every sufficiently late scale}
\Longrightarrow
\textbf{
the full local state compactness guard becomes bounded after finite lag}.
}
}
\tag{1.7}
$$

This upgrades DCRP-23--26:

the bounded-reservoir branch is genuinely compatible with the local state/pressure compactness theorem of MORP-02 after a finite number of descendant steps.

The remaining compactness-guard failure cannot be an independent hidden $E$ blowup while both $A$ and $D$ remain uniformly bounded.

The second main result is a pressure-reservoir split.

On an enlarged ball decompose

$$
\boxed{
p
=
p^{act}
+
h,
}
\tag{1.8}
$$

where

$$
p^{act}
=
\mathcal R_i\mathcal R_j
(
\eta u_i u_j
)
$$

and

$$
\Delta h=0
$$

in the inner ball.

Define the harmonic-pressure reservoir

$$
\boxed{
H(r)
=
r^{-2}
\iint_{Q_r}
|
h-(h)_{B_r}(t)
|^{3/2}
dxdt.
}
\tag{1.9}
$$

Then Calderon--Zygmund gives

$$
\boxed{
D(r)
\le
C
\left[
C(2r)
+
H(r)
\right].
}
\tag{1.10}
$$

Therefore, if

$$
D_n\to\infty
$$

while

$$
A_n
$$

remains bounded, then either

$$
\boxed{
H_n\to\infty
}
\tag{1.11}
$$

or

$$
\boxed{
E_n\to\infty.
}
\tag{1.12}
$$

Indeed a bounded $A_n$ and bounded $E_n$ would bound $C_n$ by interpolation and therefore bound the active pressure.

Hence every true local compactness-guard escape is reduced to

$$
\boxed{
A_n\to\infty
\quad\vee\quad
E_n\to\infty
\quad\vee\quad
H_n\to\infty.
}
\tag{1.13}
$$

The third main result is a new **amplitude--shape completion** for these branches.

For any nonnegative reservoir measure

$$
\mu_n
$$

with total mass

$$
M_n
=
\mu_n(X),
$$

write

$$
\boxed{
\widehat\mu_n
=
M_n^{-1}\mu_n
}
\tag{1.14}
$$

when

$$
M_n>0,
$$

and compactify the amplitude by

$$
\boxed{
\alpha_n
=
\frac{M_n}{1+M_n}
\in[0,1].
}
\tag{1.15}
$$

Then

$$
\boxed{
(
\alpha_n,
\widehat\mu_n
)
}
\tag{1.16}
$$

is compact after weak-star completion on a compactified carrier domain.

The point

$$
\alpha_\ast=1
$$

records infinite reservoir amplitude.

This prevents an unbounded local energy, dissipation, or harmonic-pressure tail from disappearing merely because the standard local suitable-weak bound fails.

The fourth main result treats the kinetic-energy branch

$$
A_n\to\infty.
$$

Choose a first selected time at which the local kinetic-energy level reaches

$$
a_n^2,
\qquad
a_n\to\infty.
$$

Define the Euler-time amplitude normalization

$$
\boxed{
v_n(y,\tau)
=
a_n^{-1}
u_n
\left(
y,
t_n+\frac{\tau}{a_n}
\right).
}
\tag{1.17}
$$

Then

$$
v_n
$$

satisfies, against divergence-free compactly supported tests,

$$
\boxed{
\partial_\tau v_n
+
\mathbb P
\nabla\cdot
(
v_n\otimes v_n
)
=
\frac{\nu}{a_n}
\Delta v_n.
}
\tag{1.18}
$$

Thus

$$
\boxed{
\nu_n^{eff}
=
\nu/a_n
\to0.
}
\tag{1.19}
$$

The first-hitting-time rule gives a uniform backward local

$$
L^\infty_\tau L^2_y
$$

bound before the selected time.

After subsequence extraction:

$$
\boxed{
v_n
\stackrel{\ast}{\rightharpoonup}
v
}
\tag{1.20}
$$

locally in

$$
L^\infty_\tau L^2_y,
$$

while

$$
v_n\otimes v_n
$$

generates a quadratic weak limit

$$
Q.
$$

The viscous term vanishes distributionally.

Therefore the limiting object satisfies the local pressure-free Euler--Reynolds equation

$$
\boxed{
\partial_\tau v
+
\mathbb P\nabla\cdot Q
=
0.
}
\tag{1.21}
$$

After generalized Young-measure decomposition:

$$
\boxed{
Q
=
v\otimes v
+
R_E,
}
\tag{1.22}
$$

with

$$
R_E
$$

a nonnegative Reynolds/concentration defect in the usual quadratic sense.

The selected normalized kinetic-energy trace has a fixed nonzero amount.

Hence at least one of

$$
\boxed{
v\neq0
}
\tag{1.23}
$$

or

$$
\boxed{
R_E
\text{ / selected trace concentration is nonzero}
}
\tag{1.24}
$$

occurs.

Thus

$$
\boxed{
\textbf{
kinetic Type-II reservoir blowup}
\Longrightarrow
\textbf{
local Euler profile}
\ \vee\
\textbf{
Euler--Reynolds / trace concentration defect}.
}
}
\tag{1.25}
$$

This is a defect-completed form of the Euler-scaling philosophy used in the Type-II literature.

The gradient branch

$$
E_n\to\infty
$$

is retained by the amplitude--shape dissipation coordinate

$$
\boxed{
\left(
\frac{E_n}{1+E_n},
\,
\frac{
|\nabla u_n|^2dxdt
}{
\int|\nabla u_n|^2dxdt
}
\right).
}
\tag{1.26}
$$

The harmonic-pressure branch

$$
H_n\to\infty
$$

is retained analogously after the declared harmonic gauge/finite-jet quotient.

Therefore

$$
\boxed{
\textbf{
"critical-reservoir blowup"}
}
$$

is no longer one black-box branch.

It has been resolved into explicit native compactness alternatives.

A final important NO-GO remains.

Amplitude--shape compactification is a **compactness device**, not a free coercive tax.

If the amplitude compactification is

$$
\alpha=M/(1+M),
$$

then a function which is zero for every finite

$$
M
$$

and strictly positive only at

$$
M=\infty
$$

cannot be lower semicontinuous at the compactification point.

Thus one may not simply declare

$$
\boxed{
\text{infinite reservoir}
\Rightarrow
\text{positive minimality tax}
}
\tag{1.27}
$$

without also taxing sufficiently large finite reservoirs or proving a genuine PDE depletion law.

This prevents a tautological closure.

The new exact frontier is therefore

$$
\boxed{
\textbf{
Type-II Euler--Reynolds Reservoir Rigidity / Reservoir-Taxation Lemma}.
}
\tag{1.28}
$$

The strongest remaining branch is now a nontrivial vanishing-viscosity Euler/Euler--Reynolds reservoir profile or a normalized dissipation/harmonic-tail defect, rather than an undefined failure of compactness.

---

# 2. Scale-invariant local quantities

For a suitable weak solution on

$$
Q_r(z_0)
=
B_r(x_0)
\times
(t_0-r^2,t_0),
$$

define

$$
\boxed{
A(r)
=
r^{-1}
\operatorname*{ess\,sup}_{
t_0-r^2<t<t_0
}
\int_{B_r}
|u|^2dx,
}
\tag{2.1}
$$

$$
\boxed{
E(r)
=
r^{-1}
\iint_{Q_r}
|\nabla u|^2dxdt,
}
\tag{2.2}
$$

$$
\boxed{
C(r)
=
r^{-2}
\iint_{Q_r}
|u|^3dxdt,
}
\tag{2.3}
$$

and

$$
\boxed{
D(r)
=
r^{-2}
\iint_{Q_r}
|
p-(p)_{B_r}(t)
|^{3/2}
dxdt.
}
\tag{2.4}
$$

All four are invariant under the standard Navier--Stokes parabolic scaling.

The compactness guard used in MORP-02 corresponds, after normalization to unit scale, to bounded

$$
A^{1/2},
\qquad
E^{1/2},
\qquad
D^{2/3}.
$$

---

# 3. Local cubic interpolation

On each time slice the local Gagliardo--Nirenberg estimate gives

$$
\|u\|_{L^3(B_r)}^3
\le
C
\|u\|_{L^2(B_r)}^{3/2}
\|\nabla u\|_{L^2(B_r)}^{3/2}
+
C
r^{-3/2}
\|u\|_{L^2(B_r)}^3.
$$

Integrating in time and using Holder:

$$
\boxed{
C(r)
\le
C
\left[
A(r)^{3/4}
E(r)^{3/4}
+
A(r)^{3/2}
\right].
}
\tag{3.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. Local energy descent inequality

Fix

$$
0<\theta<1/2.
$$

Choose a standard parabolic cutoff supported in

$$
Q_r
$$

and equal to one on

$$
Q_{\theta r}.
$$

The local energy inequality yields

$$
\boxed{
A(\theta r)
+
\nu E(\theta r)
\le
C_{\theta,\nu}
\left[
A(r)
+
C(r)
+
C(r)^{1/3}
D(r)^{2/3}
\right].
}
\tag{4.1}
$$

The spatial pressure mean may be subtracted because its contribution to

$$
u\cdot\nabla\phi
$$

vanishes by incompressibility.

Status:

$$
\boxed{
\textbf{STANDARD LEI CONSEQUENCE / USED AS PRIMARY LOCAL ESTIMATE}.
}
$$

---

# 5. NEW THEOREM — Dissipation Absorption under bounded $A+D$

## Theorem 5.1

Let

$$
r_k
=
\theta^k r_0.
$$

Assume

$$
\boxed{
A(r_k)
+
D(r_k)
\le
M
\qquad
\forall k\ge k_0.
}
\tag{5.1}
$$

Then there exist

$$
E_\ast<\infty
$$

and

$$
k_1\ge k_0
$$

depending only on

$$
M,
\theta,
\nu,
$$

and the initial finite

$$
E(r_{k_0}),
$$

such that

$$
\boxed{
E(r_k)
\le
E_\ast
\qquad
\forall k\ge k_1.
}
\tag{5.2}
$$

Moreover one may choose an absorbing value depending only on

$$
M,\theta,\nu,
$$

not on the late value of

$$
E.
$$

### Proof

By (3.1) and (5.1),

$$
C_k
\le
C_M
\left(
1+E_k^{3/4}
\right).
$$

Hence

$$
C_k^{1/3}
D_k^{2/3}
\le
C_M
\left(
1+E_k^{1/4}
\right).
$$

Apply (4.1):

$$
E_{k+1}
\le
K
\left(
1
+
E_k^{3/4}
+
E_k^{1/4}
\right).
$$

Increase

$$
K
$$

so that

$$
K\ge1.
$$

Since

$$
E^{1/4}
\le
1+E^{3/4},
$$

$$
\boxed{
E_{k+1}
\le
K
\left(
1+E_k^{3/4}
\right).
}
\tag{5.3}
$$

Set

$$
\boxed{
B
=
(4K)^4.
}
\tag{5.4}
$$

If

$$
E_k\ge B,
$$

then

$$
1\le E_k^{3/4}
$$

and

$$
2K E_k^{3/4}
\le
\frac12E_k.
$$

Therefore

$$
E_{k+1}
\le
\frac12E_k.
$$

If

$$
E_k\le B,
$$

then

$$
E_{k+1}
\le
K
\left(
1+B^{3/4}
\right)
<
B
$$

after enlarging the numerical constant in the definition of

$$
B
$$

if necessary.

Thus

$$
B
$$

is an absorbing interval.

Every finite initial

$$
E_{k_0}
$$

enters it after finitely many iterations.

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

# 6. Corollary — bounded $A+D$ gives the MORP local compactness guard

Under Theorem 5.1, for all sufficiently late scales:

$$
A_k
\le M,
$$

$$
E_k
\le E_\ast,
$$

$$
D_k
\le M.
$$

Therefore after parabolic normalization to a fixed cylinder:

$$
\boxed{
\|u_k\|_{L_t^\infty L_x^2}
+
\|\nabla u_k\|_{L^2}
+
\|p_k-(p_k)_B(t)\|_{L^{3/2}}
\le
M_\ast.
}
\tag{6.1}
$$

The standard MORP-02 local state and active-pressure compactness theorem applies.

Hence the DCRP-23 bounded-reservoir branch is not missing an independent persistent gradient blowup.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Pressure decomposition

Let

$$
\eta_{2r}
$$

be supported in

$$
B_{2r}
$$

and equal to one on a neighborhood of

$$
B_r.
$$

Define

$$
\boxed{
p^{act}
=
\mathcal R_i\mathcal R_j
(
\eta_{2r}u_i u_j
),
}
\tag{7.1}
$$

and

$$
\boxed{
h
=
p-p^{act}.
}
\tag{7.2}
$$

Then

$$
\boxed{
\Delta h=0
}
\tag{7.3}
$$

in the inner spatial ball.

By Calderon--Zygmund:

$$
\boxed{
r^{-2}
\iint_{Q_r}
|
p^{act}
|^{3/2}
\le
C
C(2r).
}
\tag{7.4}
$$

Define

$$
\boxed{
H(r)
=
r^{-2}
\iint_{Q_r}
|
h-(h)_{B_r}(t)
|^{3/2}.
}
\tag{7.5}
$$

Then

$$
\boxed{
D(r)
\le
C
\left[
C(2r)
+
H(r)
\right].
}
\tag{7.6}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. NEW THEOREM — Compactness-Guard Escape Trichotomy

## Theorem 8.1

Let

$$
(u_n,p_n)
$$

be normalized suitable-weak/pre-singularity packages for which the local suitable-weak compactness guard fails.

After passing to a subsequence, at least one of the following occurs.

### kinetic reservoir escape

$$
\boxed{
A_n\to\infty;
}
\tag{8.1}
$$

### gradient/dissipation reservoir escape

$$
\boxed{
E_n\to\infty;
}
\tag{8.2}
$$

### genuine harmonic-pressure-tail escape

after the declared harmonic gauge/finite-jet quotient:

$$
\boxed{
H_n\to\infty.
}
\tag{8.3}
$$

### Proof

If

$$
A_n
$$

is unbounded, take the first branch.

Suppose

$$
A_n
$$

is bounded.

If

$$
E_n
$$

is unbounded, take the second branch.

Suppose both

$$
A_n
$$

and

$$
E_n
$$

are bounded.

Then interpolation gives bounded

$$
C_n.
$$

If the pressure guard is unbounded, (7.6) forces

$$
H_n\to\infty.
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

This trichotomy is a compactness classification, not yet an exclusion theorem.

---

# 9. Amplitude--shape compactification

Let

$$
X
$$

be a compact carrier domain and let

$$
\mu_n
$$

be nonnegative finite Radon measures on

$$
X.
$$

Define the amplitude:

$$
\boxed{
M_n
=
\mu_n(X).
}
\tag{9.1}
$$

If

$$
M_n>0,
$$

define the normalized shape:

$$
\boxed{
\widehat\mu_n
=
\frac{\mu_n}{M_n}.
}
\tag{9.2}
$$

Then

$$
\widehat\mu_n
$$

is a probability measure.

Compactify the amplitude:

$$
\boxed{
\alpha_n
=
\frac{M_n}{1+M_n}.
}
\tag{9.3}
$$

Since

$$
[0,1]
$$

and

$$
\mathcal P(X)
$$

are compact in their usual/weak-star topologies, after a subsequence:

$$
\boxed{
\alpha_n\to\alpha_\ast,
}
\tag{9.4}
$$

and

$$
\boxed{
\widehat\mu_n
\stackrel{\ast}{\rightharpoonup}
\widehat\mu_\ast.
}
\tag{9.5}
$$

If

$$
M_n\to\infty,
$$

then

$$
\boxed{
\alpha_\ast=1.
}
\tag{9.6}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 10. Native reservoir coordinates

Apply Section 9 to the three escape branches.

## kinetic selected-time carrier

Choose a selected time

$$
t_n
$$

and cutoff

$$
\chi.
$$

Set

$$
\boxed{
\mu_n^{A}
=
\chi(x)
|u_n(x,t_n)|^2dx.
}
\tag{10.1}
$$

## dissipation carrier

Set

$$
\boxed{
\mu_n^{E}
=
\chi(x,t)
|\nabla u_n|^2dxdt.
}
\tag{10.2}
$$

## harmonic-pressure carrier

After the declared harmonic gauge / removable finite-jet quotient, set

$$
\boxed{
\mu_n^{H}
=
\chi(x,t)
|
h_n^{\perp}
|^{3/2}
dxdt.
}
\tag{10.3}
$$

Each divergent total mass produces a compact amplitude--shape defect coordinate.

These are generated by the actual Navier--Stokes state.

They do not copy a singularity certificate.

---

# 11. Why amplitude completion is needed

MORP-02's finite-measure defect completion assumes uniform local suitable-weak bounds.

If

$$
E_n\to\infty,
$$

the measures

$$
|\nabla u_n|^2dxdt
$$

are not bounded in the finite Radon-measure space and Banach--Alaoglu cannot be used directly.

The pair

$$
\boxed{
\left(
\alpha_n^E,
\widehat\mu_n^E
\right)
}
\tag{11.1}
$$

retains both:

- the fact that the total normalized dissipation amplitude diverges;
- the spatial-temporal shape of that divergent mass.

The same applies to:

$$
A_n
$$

and:

$$
H_n.
$$

Thus reservoir divergence becomes an explicit defect-only compactness coordinate.

---

# 12. First-level kinetic selection

Assume the kinetic branch:

$$
A_n\to\infty.
$$

Choose levels:

$$
L_n\to\infty.
$$

On an actual smooth pre-singularity normalized history, choose:

$$
t_n
$$

as the first time in the selected terminal window for which:

$$
\boxed{
\int_{B_1}
|u_n(x,t_n)|^2dx
=
L_n
}
\tag{12.1}
$$

up to an arbitrarily small selection error.

Then for earlier times after the declared left time face:

$$
\boxed{
\int_{B_1}
|u_n(x,t)|^2dx
\le
L_n.
}
\tag{12.2}
$$

Set:

$$
\boxed{
a_n
=
L_n^{1/2}
\to\infty.
}
\tag{12.3}
$$

If the first hitting time approaches the left time face on the Euler scale:

$$
a_n
(t_n-t_{\rm left})
\not\to\infty,
$$

the reservoir is recorded as an explicit temporal-face / transition concentration defect.

Otherwise the backward Euler-time interval expands to:

$$
(-\infty,0].
$$

---

# 13. Euler-time amplitude normalization

Define:

$$
\boxed{
v_n(y,\tau)
=
a_n^{-1}
u_n
\left(
y,
t_n+\frac{\tau}{a_n}
\right).
}
\tag{13.1}
$$

For every fixed:

$$
T<\infty,
$$

and sufficiently large:

$$
n,
$$

the first-hitting construction gives:

$$
\boxed{
\sup_{-T\le\tau\le0}
\int_{B_1}
|v_n(y,\tau)|^2dy
\le
1.
}
\tag{13.2}
$$

At:

$$
\tau=0,
$$

$$
\boxed{
\int_{B_1}
|v_n(y,0)|^2dy
=
1.
}
\tag{13.3}
$$

The Navier--Stokes equation becomes:

$$
\boxed{
\partial_\tau v_n
+
(v_n\cdot\nabla)v_n
+
\nabla q_n
=
\frac{\nu}{a_n}
\Delta v_n,
}
\tag{13.4}
$$

where

$$
q_n
=
a_n^{-2}p_n.
$$

Equivalently, against divergence-free compactly supported tests:

$$
\boxed{
\partial_\tau v_n
+
\mathbb P
\nabla\cdot
(
v_n\otimes v_n
)
=
\frac{\nu}{a_n}
\Delta v_n.
}
\tag{13.5}
$$

---

# 14. Viscosity vanishes distributionally

Let

$$
\phi
$$

be a smooth compactly supported divergence-free test field in an interior spatial ball and a fixed Euler-time interval.

Then:

$$
\left|
\frac{\nu}{a_n}
\iint
v_n\cdot\Delta\phi
\right|
\le
\frac{C_{\phi,T}\nu}{a_n}
\|v_n\|_{L^\infty_\tau L^2_x}.
$$

Hence:

$$
\boxed{
\frac{\nu}{a_n}
\Delta v_n
\to0
}
\tag{14.1}
$$

in distributions.

No gradient compactness is required for this conclusion.

---

# 15. Quadratic weak limit

The bound (13.2) gives:

$$
v_n
$$

bounded in local:

$$
L^\infty_\tau L^2_x.
$$

Therefore after a subsequence:

$$
\boxed{
v_n
\stackrel{\ast}{\rightharpoonup}
v.
}
\tag{15.1}
$$

Also:

$$
v_n\otimes v_n
$$

is bounded in:

$$
L^\infty_\tau L^1_x
$$

and therefore generates, after generalized Young/measure extraction, a quadratic limit:

$$
\boxed{
Q.
}
\tag{15.2}
$$

The limit equation is:

$$
\boxed{
\partial_\tau v
+
\mathbb P
\nabla\cdot Q
=
0.
}
\tag{15.3}
$$

Write:

$$
\boxed{
Q
=
v\otimes v
+
R_E.
}
\tag{15.4}
$$

The quadratic defect:

$$
R_E
$$

is positive semidefinite in the generalized Young / concentration sense.

Thus:

$$
\boxed{
\partial_\tau v
+
\mathbb P
\nabla\cdot
(
v\otimes v+R_E
)
=
0.
}
\tag{15.5}
$$

This is the local Euler--Reynolds limit equation.

---

# 16. NEW THEOREM — Kinetic Type-II Euler–Reynolds Reprofiling

## Theorem 16.1

Under the kinetic reservoir branch and the first-level selection of Section 12, after passing to a subsequence, one of the following occurs.

### temporal-face escape

The first hitting time does not have unbounded backward Euler-time depth and a nontrivial time-face/transition reservoir defect is retained.

### local Euler state profile

There exists a nonzero local weak Euler profile:

$$
\boxed{
v\neq0.
}
\tag{16.1}
$$

### Euler--Reynolds / trace concentration profile

The state may converge weakly to zero or lose part of its energy, but the quadratic Reynolds/concentration defect or selected-time energy trace measure is nonzero:

$$
\boxed{
R_E\neq0
\quad\text{or}\quad
\nu_{\rm tr}^{E}\neq0.
}
\tag{16.2}
$$

### Proof

Sections 13--15 give the Euler--Reynolds limit whenever backward Euler-time depth tends to infinity.

The selected time has normalized energy one.

The selected traces:

$$
|v_n(\cdot,0)|^2dx
$$

are finite positive measures with total mass one on the selected local ball.

After weak-star extraction their limit has nonzero total mass.

If this mass is represented by the strong/weak state, then the state profile is nonzero.

Otherwise a trace concentration/oscillation defect remains.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED as a local defect-completed reprofiling theorem}.
}
$$

---

# 17. Relation to Type-II scaling

The standard Navier--Stokes parabolic scaling preserves viscosity.

The normalization (13.1) instead introduces:

$$
\nu_n^{eff}
=
\nu/a_n
\to0.
$$

Thus the kinetic-reservoir blowup branch naturally enters a vanishing-viscosity / Euler scaling regime.

In physical variables, the relevant time scale is shorter than the parabolic scale by the factor:

$$
a_n.
$$

This is the structural reason Type-II analyses naturally generate Euler-type limiting equations.

DCRP-27 does not assume the limit is a classical Euler solution.

Oscillation and concentration are retained through:

$$
R_E
$$

and the selected trace defect.

---

# 18. Dissipation-amplitude branch

Assume:

$$
E_n\to\infty.
$$

Define:

$$
\boxed{
\widehat\mu_n^E
=
\frac{
\chi
|\nabla u_n|^2dxdt
}{
\iint
\chi
|\nabla u_n|^2dxdt
}.
}
\tag{18.1}
$$

After subsequence extraction:

$$
\boxed{
\widehat\mu_n^E
\stackrel{\ast}{\rightharpoonup}
\widehat\mu_\ast^E.
}
\tag{18.2}
$$

The amplitude coordinate satisfies:

$$
\boxed{
\alpha_n^E
=
\frac{E_n}{1+E_n}
\to1.
}
\tag{18.3}
$$

Thus the divergent dissipation is retained as:

$$
\boxed{
(
1,
\widehat\mu_\ast^E
).
}
\tag{18.4}
$$

If the shape develops an atom, one may re-root at the atom.

If it is diffuse, the probability measure itself is the retained diffuse dissipation-amplitude defect.

Status:

$$
\boxed{
\textbf{PROVED as compactness completion}.
}
$$

---

# 19. Harmonic-pressure amplitude branch

Assume the declared removable harmonic gauge/finite jet has been fixed.

Let:

$$
h_n^\perp
$$

be the remaining physical harmonic tail and assume:

$$
H_n\to\infty.
$$

Define:

$$
\boxed{
\widehat\mu_n^H
=
\frac{
\chi
|h_n^\perp|^{3/2}dxdt
}{
\iint
\chi
|h_n^\perp|^{3/2}dxdt
}.
}
\tag{19.1}
$$

Then:

$$
\boxed{
\alpha_n^H
\to1,
}
\tag{19.2}
$$

and after a subsequence:

$$
\boxed{
\widehat\mu_n^H
\stackrel{\ast}{\rightharpoonup}
\widehat\mu_\ast^H.
}
\tag{19.3}
$$

Spatial harmonicity gives additional interior regularity in:

$$
x,
$$

but no corresponding strong time compactness is assumed.

Thus the branch is retained as:

$$
\boxed{
\text{harmonic spatial profile}
\ \vee\
\text{time-oscillation/concentration tail shape}.
}
\tag{19.4}
$$

Status:

$$
\boxed{
\textbf{PROVED as compactness completion}.
}
$$

---

# 20. NEW THEOREM — Critical-Reservoir Completion

## Theorem 20.1

Every normalized suitable-weak/pre-singularity obstruction sequence has, after subsequence extraction, one of the following reservoir normal forms.

### bounded local state/pressure branch

For every sufficiently late scale:

$$
A+D
$$

is uniformly bounded.

Then Theorem 5.1 gives an eventual bound on:

$$
E,
$$

and therefore standard MORP-02 local state/active-pressure compactness applies.

### kinetic Type-II branch

$$
A\to\infty,
$$

and the branch is retained as an amplitude--shape kinetic carrier and, after first-level Euler-time reprofiling, as:

$$
\boxed{
\text{Euler state}
\ \vee\
\text{Euler--Reynolds/trace defect}
\ \vee\
\text{time-face escape}.
}
$$

### dissipation-amplitude branch

$$
E\to\infty,
$$

retained by:

$$
(
\alpha^E,
\widehat\mu^E
).
$$

### harmonic-pressure-amplitude branch

$$
H\to\infty,
$$

retained by:

$$
(
\alpha^H,
\widehat\mu^H
).
$$

Therefore:

$$
\boxed{
\textbf{
critical-reservoir failure no longer means "no compactness object exists".
}
}
\tag{20.1}
$$

It means the compactness object lives in an amplitude-completed defect sector.

Status:

$$
\boxed{
\textbf{PROVED at the package-classification level}.
}
$$

---

# 21. NO-GO — amplitude compactification is not automatically a tax

Let:

$$
\alpha(M)
=
M/(1+M).
$$

Then:

$$
M_n\to\infty
$$

corresponds to:

$$
\alpha_n\to1.
$$

Suppose one wants a defect cost:

$$
f(\alpha)
$$

with:

$$
\boxed{
f(\alpha)=0
\qquad
\forall
\alpha<1,
}
\tag{21.1}
$$

but:

$$
\boxed{
f(1)>0.
}
\tag{21.2}
$$

Take:

$$
\alpha_n\uparrow1
$$

with:

$$
\alpha_n<1.
$$

Then:

$$
\liminf_n
f(\alpha_n)
=
0
<
f(1).
$$

Therefore:

$$
\boxed{
f
\text{ is not lower semicontinuous at }
\alpha=1.
}
\tag{21.3}
$$

Thus one cannot preserve the MORP direct-method/lower-semicontinuity architecture while assigning a positive tax **only** to infinite reservoir amplitude and zero tax to every finite amplitude.

Status:

$$
\boxed{
\textbf{PROVED NO-GO}.
}
$$

---

# 22. Why a continuous amplitude tax would be dangerous

A continuous choice such as:

$$
\boxed{
g(M)
=
\frac{M}{1+M}
}
\tag{22.1}
$$

is lower semicontinuous.

But it is positive for every:

$$
M>0.
$$

If native separation already forces a nonzero local reservoir, adding:

$$
g(M)
$$

directly to:

$$
\mathfrak J
$$

may manufacture a trivial positive gap from generic state size rather than from a genuine depletion/observation mechanism.

Therefore:

$$
\boxed{
\textbf{
amplitude completion}
\neq
\textbf{
permission to tax amplitude by fiat}.
}
}
\tag{22.2}
$$

This keeps the construction non-tautological.

---

# 23. Consequence for the MORP compactness program

MORP-02 already defect-completes:

- bounded dissipation loss;
- harmonic pressure;
- selected traces;
- spatial/scale escape;
- transition residual.

DCRP-27 adds the missing **unbounded-amplitude completion**:

$$
\boxed{
\text{finite reservoir}
\ \vee\
\text{amplitude--shape defect at infinity}.
}
\tag{23.1}
$$

This strengthens the conceptual M-COM picture.

It does not, by itself, prove:

- native separation of the amplitude defect;
- a positive return tax;
- actual shadowing by one singular history;
- exclusion of the Euler--Reynolds profile.

---

# 24. Connection to DCRP-23--26

The full branch structure is now:

### bounded $A+D$

After finite lag:

$$
E,C
$$

are bounded.

Then DCRP-23 gives:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}
\ge
s_\ast>0
}
$$

on every sufficiently late persistent non-CKN scale.

DCRP-24--26 classify and substantially close the compact recurrent strong-profile sector.

### unbounded reservoir

DCRP-27 reduces it to:

$$
\boxed{
\text{Euler--Reynolds kinetic profile}
\ \vee\
\text{dissipation-amplitude defect}
\ \vee\
\text{harmonic-pressure-amplitude defect}.
}
\tag{24.1}
$$

Thus the original two-branch split has become a concrete mechanism split.

---

# 25. What is already physically paid

The branch:

$$
E_n\to\infty
$$

contains arbitrarily large normalized physical viscous dissipation.

This is not a phantom state coordinate.

Likewise a harmonic pressure amplitude surviving after the declared gauge is visible to pressure/tail transition channels.

The genuinely difficult new state branch is therefore the kinetic:

$$
A_n\to\infty
$$

sector after Euler-time reprofiling.

Its viscosity vanishes in the reprofiled equation.

That branch is not automatically killed by the Navier--Stokes viscous tax.

---

# 26. Relation to known Type-I / Type-II structure

Classical local Type-I analysis is based on bounded scale-invariant energy quantities and produces compact ancient Navier--Stokes profiles under additional hypotheses.

The complementary Type-II regime is precisely the regime in which such scale-invariant quantities fail to remain bounded.

The Type-II literature uses Euler-type scalings because the effective viscosity then tends to zero.

DCRP-27 uses the same structural fact but refuses to assume strong convergence:

$$
\boxed{
\text{classical Euler profile}
}
$$

is replaced by the defect-complete alternative:

$$
\boxed{
\text{Euler state}
\ \vee\
\text{Euler--Reynolds/concentration profile}.
}
$$

---

# 27. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Type-II Euler--Reynolds Reservoir Rigidity / Reservoir-Taxation Lemma}.
}
$$

A useful theorem would prove:

> Let:
>
> $$
> (v,R_E)
> $$
>
> be a nontrivial local Euler--Reynolds profile extracted from:
>
> $$
> A_n\to\infty.
> $$
>
> Assume all already-completed:
>
> - spatial/scale escape;
> - time-face escape;
> - harmonic-pressure tail;
> - selected-trace concentration;
> - Young/fiber defects
>
> vanish.
>
> Then either:
>
> 1.:
>
>    $$
>    R_E=0
>    $$
>
>    and the state enters a genuine Euler Liouville/rigidity class;
>
> 2.:
>
>    $$
>    R_E\neq0
>    $$
>
>    and the Reynolds defect produces a native positive flux/transition cost;
>
> 3. the Euler profile violates the finite-energy/Morrey inheritance from the original Navier--Stokes branch.

This is the correct Type-II mechanism frontier.

---

# 28. Updated global proof-state diagram

The current route is:

$$
\boxed{
\begin{aligned}
\text{persistent singular branch}
\Longrightarrow\quad
&
\text{bounded }A+D
\\
&\vee
\text{unbounded reservoir}.
\end{aligned}
}
\tag{28.1}
$$

The first branch gives:

$$
\boxed{
\text{eventual }E,C\text{ bounds}
\Longrightarrow
\text{increment activation}
\Longrightarrow
\text{DCRP-24--26 rigidity/paid alternatives}.
}
\tag{28.2}
$$

The second branch gives:

$$
\boxed{
\begin{aligned}
&
\text{Euler--Reynolds kinetic profile}
\\
&\vee
\text{dissipation amplitude defect}
\\
&\vee
\text{harmonic pressure amplitude defect}.
\end{aligned}
}
\tag{28.3}
$$

No generic "critical-reservoir blowup" box remains.

---

# 29. Source-status audit

## MORP-02

The internal source explicitly requires a normalized local bound on:

$$
L_t^\infty L_x^2,
\qquad
L_t^2H_x^1,
\qquad
L^{3/2}
$$

pressure.

Under these bounds it proves strong local velocity compactness and active-pressure compactness.

DCRP-27 proves that a persistent bound on the scale-invariant:

$$
A+D
$$

coordinates generates the missing:

$$
E
$$

bound after finite lag.

## Seregin Type-II analysis

The primary source distinguishes Type-I singularities by bounded scale-invariant local energy quantities and studies Type-II scenarios using Euler scaling.

After Euler scaling the Navier--Stokes viscosity is multiplied by a factor tending to zero.

DCRP-27 adopts this vanishing-viscosity structure but completes weak limits by Euler--Reynolds / concentration defects.

---

# 30. End state

The principal new compactness theorem is:

$$
\boxed{
A_k+D_k\le M
\quad
\forall k\gg1
\Longrightarrow
E_k\le E_\ast
\quad
\forall k\gg1.
}
$$

Therefore the bounded-reservoir branch really enters the MORP-02 local compactness regime after finite lag.

Every remaining local compactness-guard failure satisfies:

$$
\boxed{
A\to\infty
\ \vee\
E\to\infty
\ \vee\
H\to\infty.
}
$$

Each divergent amplitude has a compact native amplitude--shape representation.

The hardest kinetic branch admits the defect-completed vanishing-viscosity reprofile:

$$
\boxed{
A\to\infty
\Longrightarrow
\text{Euler state}
\ \vee\
\text{Euler--Reynolds/trace defect}
\ \vee\
\text{time-face escape}.
}
$$

Thus the former "critical-reservoir blowup" frontier is structurally resolved.

The next single frontier is:

$$
\boxed{
\textbf{
Type-II Euler--Reynolds Reservoir Rigidity / Reservoir Taxation.
}
}
$$