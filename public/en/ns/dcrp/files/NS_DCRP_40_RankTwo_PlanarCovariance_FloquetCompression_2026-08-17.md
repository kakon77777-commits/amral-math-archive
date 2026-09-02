# NS-DCRP-40 — Rank-Two Planar Covariance, Normal-Compression Floquet Rigidity, and the Planar Potential–Shear Frontier

- date: 2026-08-17
- status: research proof checkpoint / rank-two low-rank rigidity round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. attack the rank-two branch left by DCRP-38/39;
  2. derive the exact evolution of the common vorticity-plane normal;
  3. derive the pseudo-determinant evolution of the in-plane covariance;
  4. prove the periodic normal-compression balance;
  5. classify the frozen-affine zero-residual branch as an axisymmetric planar-extension/normal-compression mode;
  6. derive the local planar potential--shear representation for a fixed vorticity plane;
  7. prove that a purely kinematic global planar-vorticity Liouville theorem is false;
  8. identify the genuine remaining branch as a planar conformal Floquet mode coupled to the full DSS dynamics;
  9. separate rank-one collapse, rank-three lifting, moving-plane residual, and exact planar equality.
- no full Navier--Stokes regularity claim is made.
- external calibration:
  - E. Miller, *A locally anisotropic regularity criterion for the Navier--Stokes equation in terms of vorticity*, arXiv:2002.02152;
  - P. Rajamanickam, A. D. Weiss, *Steady axisymmetric vortices in radial stagnation flows*, arXiv:2406.15147v2.
- internal dependencies:
  - DCRP-35 annular affine-strain supplier;
  - DCRP-38 covariance determinant rigidity;
  - DCRP-39 rank-one Burgers-jet / finite-rank-lifting theorem.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-38 proved that the exact zero-covariance-residual strict DSS branch satisfies

$$
\boxed{
\operatorname{rank}B\le2,
}
\tag{1.1}
$$

where

$$
\boxed{
B(s)
=
\int
\phi(y)
\Omega(y,s)\otimes\Omega(y,s)\,dy.
}
\tag{1.2}
$$

DCRP-39 substantially reduced the rank-one branch.

DCRP-40 therefore assumes

$$
\boxed{
\operatorname{rank}B=2
}
\tag{1.3}
$$

on the active strict-DSS core.

Let

$$
\boxed{
n(s)
}
\tag{1.4}
$$

be the unit normal spanning

$$
\ker B(s).
$$

Then

$$
\boxed{
n(s)\cdot\Omega(y,s)=0
}
\tag{1.5}
$$

throughout the support of the active covariance cutoff.

The exact covariance equality branch is

$$
\boxed{
B'
=
AB
+
BA
-
c_\gamma B,
}
\tag{1.6}
$$

where

$$
\boxed{
c_\gamma
=
2-3\gamma
>
0.
}
\tag{1.7}
$$

The first central theorem of DCRP-40 is the normal-direction equation:

$$
\boxed{
n'
=
-A n
+
(n\cdot A n)n.
}
\tag{1.8}
$$

Thus the plane normal is not a free phase variable.

For frozen symmetric

$$
A,
$$

the Rayleigh quotient

$$
q_n=n\cdot A n
$$

satisfies

$$
\boxed{
q_n'
=
-2
\left|
(A-q_nI)n
\right|^2
\le0.
}
\tag{1.9}
$$

Hence the normal is dynamically driven toward compressive eigendirections of the affine strain.

The vorticity plane therefore tends toward the corresponding extensional invariant plane.

The second central theorem concerns the product of the two positive covariance eigenvalues.

Define the rank-two pseudo-determinant

$$
\boxed{
D_2(B)
=
\det_+B
=
\lambda_1(B)\lambda_2(B),
}
\tag{1.10}
$$

where

$$
\lambda_1,\lambda_2>0
$$

are the nonzero eigenvalues.

Then on the zero-residual rank-two branch

$$
\boxed{
\frac d{ds}
\log D_2(B)
=
-2
\left[
c_\gamma
+
n\cdot A n
\right].
}
\tag{1.11}
$$

DSS periodicity gives

$$
D_2(B(S_0))
=
D_2(B(0)).
$$

Therefore

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
n(s)\cdot A(s)n(s)\,ds
=
-c_\gamma.
}
\tag{1.12}
$$

Thus the exact rank-two zero-residual branch must maintain a fixed **average compressive normal strain**.

Equivalently, because

$$
\operatorname{tr}A=0,
$$

the average trace of the strain restricted to the vorticity plane is

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
\operatorname{tr}
\left(
A|_{n^\perp}
\right)ds
=
c_\gamma.
}
\tag{1.13}
$$

The vorticity plane must, on average, be area-extensional in the affine strain geometry.

The third main result is the frozen-affine classification.

Assume

$$
A
$$

is constant in similarity time and the rank-two covariance is nonzero, positive definite on its support plane, periodic, and zero-residual.

Then the normal flow (1.8) is periodic only if

$$
n
$$

is an eigenvector of

$$
A.
$$

Equation (1.12) forces its eigenvalue to be

$$
\boxed{
-c_\gamma.
}
\tag{1.14}
$$

Let the two in-plane eigenvalues be

$$
a_1,a_2.
$$

Periodicity of the positive in-plane covariance forces

$$
\boxed{
a_1=a_2=\frac{c_\gamma}{2}.
}
\tag{1.15}
$$

Therefore, in a basis with

$$
n=e_3,
$$

$$
\boxed{
A
=
\begin{pmatrix}
c_\gamma/2&0&0\\
0&c_\gamma/2&0\\
0&0&-c_\gamma
\end{pmatrix}.
}
\tag{1.16}
$$

Hence the frozen-affine rank-two equality mode is exactly:

$$
\boxed{
\textbf{
normal compression}
+
\textbf{
isotropic planar extension}.
}
\tag{1.17}
$$

This is a pancake/sheet-type strain normal form.

It is the rank-two analogue of the rank-one Burgers-jet strain geometry.

The fourth main result gives the general time-periodic Floquet interpretation.

Let

$$
X'
=
A(s)X,
\qquad
X(0)=I.
$$

Since

$$
\operatorname{tr}A=0,
$$

$$
\boxed{
\det X(s)=1.
}
\tag{1.18}
$$

The zero-residual covariance is

$$
\boxed{
B(s)
=
e^{-c_\gamma s}
X(s)
B(0)
X(s)^T.
}
\tag{1.19}
$$

Let

$$
M=X(S_0).
$$

Periodicity gives

$$
\boxed{
M B_0 M^T
=
e^{c_\gamma S_0}B_0.
}
\tag{1.20}
$$

On the covariance support plane

$$
E_0=\operatorname{Ran}B_0,
$$

the monodromy is conformal with respect to the metric defined by

$$
B_0.
$$

More precisely, after identifying the plane with

$$
\mathbb R^2,
$$

$$
\boxed{
e^{-c_\gamma S_0/2}
B_0^{-1/2}
M_E
B_0^{1/2}
\in
SO(2)
}
\tag{1.21}
$$

for the orientation-preserving branch.

Thus the exact zero-residual rank-two state is a:

$$
\boxed{
\textbf{
planar conformal Floquet mode}.
}
\tag{1.22}
$$

The plane expands by the exact covariance factor while an allowed in-plane rotation may remain.

This is a much narrower normal form than generic planar vorticity.

The fifth main result gives the fixed-plane local velocity representation.

Assume, on one simply connected core and one time slice, that the plane normal is fixed and choose coordinates

$$
n=e_3.
$$

Then

$$
\Omega_3=0.
$$

Hence

$$
\boxed{
\partial_1V_2-\partial_2V_1=0.
}
\tag{1.23}
$$

On each simply connected horizontal slice there exists a scalar

$$
\phi
$$

such that

$$
\boxed{
V_h
=
\nabla_h\phi.
}
\tag{1.24}
$$

Write

$$
\boxed{
w=V_3.
}
\tag{1.25}
$$

Incompressibility gives

$$
\boxed{
\Delta_h\phi
+
\partial_3w
=
0.
}
\tag{1.26}
$$

Define the shear potential

$$
\boxed{
q
=
w-\partial_3\phi.
}
\tag{1.27}
$$

Then

$$
\boxed{
\Omega
=
\left(
\partial_2q,
-\partial_1q,
0
\right).
}
\tag{1.28}
$$

Thus rank-two planar vorticity admits the exact local representation

$$
\boxed{
V
=
\left(
\nabla_h\phi,
w
\right),
\qquad
\Omega_h
=
J\nabla_hq.
}
\tag{1.29}
$$

This is a **planar potential--shear normal form**.

It is not genuinely two-dimensional because

$$
\phi
$$

and

$$
w
$$

may depend on the normal coordinate.

If the plane normal is also time-independent, preservation of

$$
\Omega_3=0
$$

under the DSS vorticity equation gives

$$
\boxed{
\Omega_h\cdot\nabla_hw=0.
}
\tag{1.30}
$$

Equivalently,

$$
\boxed{
J\nabla_hq\cdot\nabla_hw=0.
}
\tag{1.31}
$$

Thus, wherever

$$
\nabla_hq\neq0,
$$

the normal velocity

$$
w
$$

is locally constant along level sets of

$$
q.
$$

This is an additional integrability constraint on the fixed-plane subbranch.

The sixth main result is a safety NO-GO.

The rank-one global Liouville theorem of DCRP-39 does **not** generalize to rank two by pure geometry.

Indeed choose any nontrivial

$$
\chi\in C_c^\infty(\mathbb R^3)
$$

and define

$$
\boxed{
V
=
\left(
\partial_1\partial_3\chi,
\partial_2\partial_3\chi,
-\Delta_h\chi
\right).
}
\tag{1.32}
$$

Then

$$
\boxed{
\nabla\cdot V=0,
}
\tag{1.33}
$$

and

$$
\boxed{
\nabla\times V
=
\left(
-\partial_2\Delta\chi,
\partial_1\Delta\chi,
0
\right).
}
\tag{1.34}
$$

Thus

$$
\Omega_3=0
$$

globally while

$$
V
$$

is smooth, compactly supported, and nonzero.

It therefore satisfies every large-radius upper bound of the form

$$
\int_{B_R}|V|^2
\le
CR^\kappa,
\qquad
\kappa>0,
$$

for sufficiently large

$$
R.
$$

Hence

$$
\boxed{
\textbf{
global planar vorticity}
+
\textbf{
sublinear energy growth}
\not\Rightarrow
V=0
}
\tag{1.35}
$$

at the purely kinematic level.

A genuine rank-two exclusion must use the DSS/Euler/Navier--Stokes dynamics.

This also explains why existing anisotropic Navier--Stokes regularity theorems do not automatically close the branch.

For example, Miller's plane-restricted vorticity criterion requires a scale-critical

$$
L_t^4L_x^2
$$

bound on the vorticity projection together with controlled variation of the plane normal.

The exact geometric condition

$$
n\cdot\Omega=0
$$

alone does not provide that analytic bound.

Thus no external regularity criterion is silently imported.

The seventh result is the corrected rank-two branch tree.

Let

$$
\vartheta_2
=
\frac{
4D_2(B)
}{
(\operatorname{tr}B)^2
}
\in(0,1]
$$

on rank-two covariance.

Then:

### planar anisotropy collapse

$$
\boxed{
\vartheta_2\to0
}
\tag{1.36}
$$

drives the covariance toward rank one and returns to DCRP-39.

### rank lifting

A normal vorticity component appears at finite radius/time:

$$
\boxed{
n\cdot\Omega\neq0.
}
\tag{1.37}
$$

This produces a rank-three/directional-spread carrier or transition defect.

### plane-motion / non-affine residual

The covariance plane cannot be transported by the canonical normal equation or the affine source approximation.

This enters the covariance/transition residual

$$
R_B.
$$

### exact planar Floquet equality

The plane normal obeys

$$
n'
=
-An+(n\cdot An)n,
$$

the pseudo-determinant satisfies the exact compression balance, and the in-plane monodromy is covariance-conformal.

This is the strongest rank-two equality branch.

Therefore:

$$
\boxed{
\textbf{
rank-two strict branch}
\Longrightarrow
\textbf{
rank-one collapse}
\ \vee\
\textbf{
rank-three lifting}
\ \vee\
\textbf{
plane/covariance residual}
\ \vee\
\textbf{
planar conformal Floquet mode}.
}
\tag{1.38}
$$

The final equality mode is not excluded in DCRP-40.

Its most rigid frozen-affine version is the axisymmetric normal-compression / planar-extension tensor (1.16).

This type of strained planar/shear vortex geometry is not intrinsically impossible in Navier--Stokes: exact Burgers-vortex-sheet/layer-type solutions under prescribed linear strain provide external calibration that strained vortex layers are legitimate local viscous structures.

The DCRP problem is harder and more specific:

- the branch is unforced;
- same-parent;
- strict DSS;
- tail-fed;
- PFET active;
- and must reproduce the planar strain internally.

The new exact frontier is therefore

$$
\boxed{
\textbf{
Planar Conformal Floquet Vorticity /
Pancake-Strain Reproduction Rigidity.
}
}
\tag{1.39}
$$

The next question is:

> can an unforced same-parent DSS flow indefinitely reproduce a rank-two vorticity plane whose normal undergoes the exact compressive Floquet dynamics and whose in-plane covariance returns conformally, while simultaneously satisfying the DCRP-31 inward PFET and DCRP-35 strain-supplier ledgers?

This is now the principal low-rank equality problem.

---

# 2. Rank-two covariance geometry

Let

$$
B=B^T\ge0,
\qquad
\operatorname{rank}B=2.
$$

Let

$$
n
$$

be a unit vector spanning

$$
\ker B.
$$

Then

$$
\boxed{
Bn=0.
}
\tag{2.1}
$$

If

$$
B
$$

arises from

$$
\int\phi\,\Omega\otimes\Omega
$$

with

$$
\phi>0
$$

on the connected core, then

$$
\boxed{
n\cdot\Omega=0
}
\tag{2.2}
$$

there.

---

# 3. Zero-residual covariance equation

DCRP-38 gives

$$
\boxed{
B'
=
AB
+
BA
-
c_\gamma B
+
R_B.
}
\tag{3.1}
$$

The exact rank-two equality branch assumes

$$
\boxed{
R_B=0.
}
\tag{3.2}
$$

Thus

$$
\boxed{
B'
=
AB
+
BA
-
c_\gamma B.
}
\tag{3.3}
$$

---

# 4. NEW THEOREM — Plane-Normal Replicator Equation

## Theorem 4.1

On the zero-residual rank-two branch,

$$
\boxed{
n'
=
-An
+
(n\cdot An)n.
}
\tag{4.1}
$$

### Proof

Differentiate

$$
Bn=0.
$$

Then

$$
B'n+Bn'=0.
$$

Using (3.3),

$$
B'n
=
BAn.
$$

Hence

$$
B(n'+An)=0.
$$

Since

$$
\ker B=\operatorname{span}\{n\},
$$

$$
n'+An=\lambda n.
$$

Dot with

$$
n.
$$

Because

$$
|n|=1,
$$

$$
n'\cdot n=0.
$$

Therefore

$$
\lambda=n\cdot An.
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

# 5. Frozen-affine normal alignment

Assume

$$
A
$$

is constant.

Set

$$
q=n\cdot An.
$$

Then from (4.1),

$$
\boxed{
q'
=
-2
\left[
n\cdot A^2n-q^2
\right]
=
-2
|(A-qI)n|^2
\le0.
}
\tag{5.1}
$$

Thus the plane normal moves down the Rayleigh quotient and tends toward compressive eigendirections.

This is the dual of the rank-one vorticity-direction alignment law.

---

# 6. Rank-two pseudo-determinant

Let

$$
e_1,e_2
$$

be an orthonormal basis of

$$
n^\perp.
$$

Let

$$
E
=
(e_1,e_2)
$$

and define the positive in-plane covariance matrix

$$
\boxed{
B_E
=
E^TBE.
}
\tag{6.1}
$$

Define

$$
\boxed{
D_2(B)
=
\det B_E.
}
\tag{6.2}
$$

This is independent of the oriented orthonormal basis of the support plane.

It equals the product of the two positive eigenvalues of

$$
B.
$$

---

# 7. NEW THEOREM — Pseudo-Determinant Evolution

## Theorem 7.1

On the zero-residual rank-two branch,

$$
\boxed{
\frac d{ds}
\log D_2(B)
=
-2
\left[
c_\gamma+n\cdot An
\right].
}
\tag{7.1}
$$

### Proof

Differentiate

$$
B_E=E^TBE.
$$

The moving orthonormal frame contributes skew connection terms.

Their trace contribution to

$$
\operatorname{tr}
\left(
B_E^{-1}B_E'
\right)
$$

vanishes.

Thus only

$$
E^TB'E
$$

contributes to the logarithmic determinant.

Using (3.3),

$$
E^TB'E
=
A_EB_E
+
B_EA_E
-
c_\gamma B_E,
$$

where

$$
A_E=E^TAE.
$$

Hence

$$
\begin{aligned}
\frac d{ds}
\log\det B_E
&=
2\operatorname{tr}A_E
-
2c_\gamma
\\
&=
2
\left[
\operatorname{tr}A
-
n\cdot An
\right]
-
2c_\gamma.
\end{aligned}
$$

Since

$$
\operatorname{tr}A=0,
$$

the result follows.

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

# 8. Periodic normal-compression balance

DSS periodicity gives

$$
D_2(B(S_0))
=
D_2(B(0)).
$$

Integrating (7.1),

$$
\boxed{
\int_0^{S_0}
\left[
c_\gamma+n\cdot An
\right]ds
=
0.
}
\tag{8.1}
$$

Therefore

$$
\boxed{
\left\langle
n\cdot An
\right\rangle_s
=
-c_\gamma.
}
\tag{8.2}
$$

This is the exact rank-two replacement for the full-rank determinant contradiction.

The full-rank branch had no available normal compression direction and was forced to pay

$$
R_B.
$$

The rank-two branch can evade that contradiction precisely by compressing its missing direction.

---

# 9. Planar area interpretation

Because

$$
\operatorname{tr}A=0,
$$

$$
\operatorname{tr}
\left(
A|_{n^\perp}
\right)
=
-n\cdot An.
$$

Thus

$$
\boxed{
\left\langle
\operatorname{tr}
(
A|_{n^\perp}
)
\right\rangle_s
=
c_\gamma.
}
\tag{9.1}
$$

The vorticity plane experiences positive average affine area expansion.

This compensates the similarity covariance damping

$$
c_\gamma.
$$

---

# 10. Frozen-affine periodic classification

Assume

$$
A
$$

is constant and

$$
B
$$

is nonzero, rank two, positive definite on its support plane, and periodic.

By (5.1), periodicity of

$$
n
$$

forces

$$
n
$$

to be an eigenvector of

$$
A.
$$

Equation (8.2) gives its eigenvalue:

$$
\boxed{
a_n=-c_\gamma.
}
\tag{10.1}
$$

Let the plane eigenvalues be

$$
a_1,a_2.
$$

Trace free gives

$$
a_1+a_2=c_\gamma.
$$

In the eigenbasis,

$$
B(s)
=
e^{-c_\gamma s}
\begin{pmatrix}
e^{a_1s}&0\\
0&e^{a_2s}
\end{pmatrix}
B(0)
\begin{pmatrix}
e^{a_1s}&0\\
0&e^{a_2s}
\end{pmatrix}.
$$

Since

$$
B(0)
$$

is positive definite on the plane, both diagonal quadratic forms are nonzero.

Periodicity therefore requires

$$
\boxed{
2a_1=c_\gamma,
\qquad
2a_2=c_\gamma.
}
\tag{10.2}
$$

Hence

$$
\boxed{
a_1=a_2=\frac{c_\gamma}{2}.
}
\tag{10.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 11. Frozen planar-strain normal form

The resulting tensor is

$$
\boxed{
A
=
\frac{c_\gamma}{2}
P_{n^\perp}
-
c_\gamma
n\otimes n.
}
\tag{11.1}
$$

Thus the exact frozen rank-two equality branch has:

- isotropic extension in the vorticity plane;
- compression in the plane-normal direction.

This is a finite-dimensional pancake/planar-strain normal form.

It is not excluded by tensor algebra.

---

# 12. Time-periodic affine cocycle

For general periodic

$$
A(s),
$$

let

$$
X'=AX,
\qquad
X(0)=I.
$$

Then

$$
\det X=1.
$$

The zero-residual covariance is

$$
\boxed{
B(s)
=
e^{-c_\gamma s}
X(s)
B_0
X(s)^T.
}
\tag{12.1}
$$

Set

$$
M=X(S_0).
$$

DSS periodicity gives

$$
\boxed{
MB_0M^T
=
e^{c_\gamma S_0}B_0.
}
\tag{12.2}
$$

---

# 13. Normal Floquet multiplier

Let

$$
n_0
$$

span

$$
\ker B_0.
$$

Using the adjugate transformation under congruence and

$$
\det M=1,
$$

one obtains

$$
\boxed{
M^{-T}n_0
=
\pm
e^{c_\gamma S_0}
n_0.
}
\tag{13.1}
$$

Equivalently,

$$
\boxed{
M^Tn_0
=
\pm
e^{-c_\gamma S_0}
n_0.
}
\tag{13.2}
$$

For the orientation-continuous branch the sign is positive.

Thus the missing covariance direction is an exact contracting Floquet covector.

---

# 14. Planar conformal Floquet theorem

Let

$$
M_E
$$

be the induced monodromy on the covariance support plane.

Equation (12.2) gives

$$
M_EB_0M_E^T
=
e^{c_\gamma S_0}B_0.
$$

Therefore define

$$
\boxed{
Q_E
=
e^{-c_\gamma S_0/2}
B_0^{-1/2}
M_E
B_0^{1/2}.
}
\tag{14.1}
$$

Then

$$
\boxed{
Q_EQ_E^T=I.
}
\tag{14.2}
$$

For orientation-preserving flow on the plane:

$$
\boxed{
Q_E\in SO(2).
}
\tag{14.3}
$$

Thus:

$$
\boxed{
M_E
=
e^{c_\gamma S_0/2}
B_0^{1/2}
Q_E
B_0^{-1/2}.
}
\tag{14.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The exact rank-two equality branch is a conformal expansion in the covariance metric, possibly accompanied by one planar rotation angle.

---

# 15. Planar anisotropy parameter

Define

$$
\boxed{
\vartheta_2
=
\frac{
4D_2(B)
}{
(\operatorname{tr}B)^2
}
\in(0,1].
}
\tag{15.1}
$$

For positive in-plane eigenvalues

$$
\lambda_1,\lambda_2,
$$

$$
\boxed{
\vartheta_2
=
\frac{
4\lambda_1\lambda_2
}{
(\lambda_1+\lambda_2)^2
}.
}
\tag{15.2}
$$

Thus:

### isotropic planar covariance

$$
\vartheta_2=1.
$$

### rank-one collapse

$$
\vartheta_2\to0.
$$

This provides an eigenframe-free scalar separating the rank-two interior from the DCRP-39 boundary.

---

# 16. Fixed-plane local representation

Assume

$$
n=e_3
$$

on one fixed-time simply connected core.

Then

$$
\Omega_3=0.
$$

Therefore

$$
\partial_1V_2-\partial_2V_1=0.
$$

Hence there exists

$$
\phi
$$

with

$$
\boxed{
V_1=\partial_1\phi,
\qquad
V_2=\partial_2\phi.
}
\tag{16.1}
$$

Set

$$
w=V_3.
$$

Incompressibility gives

$$
\boxed{
\Delta_h\phi
=
-\partial_3w.
}
\tag{16.2}
$$

Define

$$
q=w-\partial_3\phi.
$$

Then

$$
\boxed{
\Omega_1=\partial_2q,
\qquad
\Omega_2=-\partial_1q,
\qquad
\Omega_3=0.
}
\tag{16.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 17. Planar potential--shear normal form

The local rank-two field can therefore be written as

$$
\boxed{
V
=
\left(
\nabla_h\phi,
w
\right),
}
\tag{17.1}
$$

with

$$
\boxed{
\Delta_h\phi+\partial_3w=0,
}
\tag{17.2}
$$

and

$$
\boxed{
\Omega_h
=
\left(
\partial_2q,
-\partial_1q
\right),
\qquad
q=w-\partial_3\phi.
}
\tag{17.3}
$$

This is not a two-dimensional velocity field.

It is a three-dimensional potential--shear field with planar vorticity.

---

# 18. Fixed-plane dynamical constraint

Assume in addition that the plane normal is fixed in similarity time:

$$
n'=0.
$$

Then the normal component of the vorticity equation gives

$$
\boxed{
\Omega\cdot\nabla w=0.
}
\tag{18.1}
$$

Since

$$
\Omega_h
=
(\partial_2q,-\partial_1q),
$$

$$
\boxed{
\partial_2q\,\partial_1w
-
\partial_1q\,\partial_2w
=
0.
}
\tag{18.2}
$$

Thus the horizontal gradients of

$$
q
$$

and

$$
w
$$

are parallel.

On a regular level-set patch one may write locally

$$
\boxed{
w=F(q,x_3,s).
}
\tag{18.3}
$$

This is an additional integrability condition for the fixed-plane equality branch.

---

# 19. Kinematic global-planar NO-GO

Choose

$$
\chi\in C_c^\infty(\mathbb R^3)
$$

and define

$$
\boxed{
V
=
\left(
\partial_1\partial_3\chi,
\partial_2\partial_3\chi,
-\Delta_h\chi
\right).
}
\tag{19.1}
$$

Then

$$
\boxed{
\nabla\cdot V=0.
}
\tag{19.2}
$$

Its vorticity is

$$
\boxed{
\Omega
=
\left(
-\partial_2\Delta\chi,
\partial_1\Delta\chi,
0
\right).
}
\tag{19.3}
$$

For generic nonzero

$$
\chi,
$$

the field is nonzero.

It is smooth and compactly supported.

Thus:

$$
\boxed{
\Omega\cdot e_3=0
}
$$

globally does not imply any velocity invariance or triviality.

Status:

$$
\boxed{
\textbf{PROVED KINEMATIC NO-GO}.
}
$$

---

# 20. Why the rank-one Liouville argument fails

DCRP-39 used

$$
\Omega=\omega e
$$

to obtain

$$
\partial_e\Omega=0
$$

and therefore a harmonic axial derivative

$$
\partial_eV.
$$

Rank two only gives

$$
n\cdot\Omega=0.
$$

It does not imply

$$
\partial_n\Omega=0.
$$

Therefore no harmonic normal-derivative Liouville theorem follows.

The compactly supported example of Section 19 proves that no such purely geometric argument can exist.

---

# 21. External anisotropic regularity calibration

There are strong Navier--Stokes regularity criteria based on planar vorticity components.

For example, a locally varying vorticity plane can be controlled if the plane-projected vorticity satisfies an appropriate scaling-critical mixed norm and the plane normal varies regularly.

However the rank-two geometric condition

$$
n\cdot\Omega=0
$$

alone does not provide those analytic bounds.

Therefore:

$$
\boxed{
\textbf{
rank-two geometry}
\neq
\textbf{
automatic application of a planar-vorticity regularity theorem}.
}
}
\tag{21.1}
$$

The DCRP branch must supply the missing norm or use the DSS recurrence more directly.

---

# 22. Strained vortex-layer calibration

Exact and classical Navier--Stokes constructions include vortex layers/sheets maintained in linear stagnation or straining flows.

These examples show that planar/shear vorticity under a linear strain is a legitimate local viscous mechanism.

They do not produce the DCRP singular parent because the DCRP branch is unforced, finite-energy, same-parent, and critical-DSS recurrent.

Thus the planar-strain normal form must be excluded through reproduction/return constraints rather than local existence intuition.

---

# 23. Rank-two residual alternatives

The exact planar Floquet branch assumes:

$$
R_B=0.
$$

If the actual normalized sequence fails any of the following:

-:

  $$
  Bn=0;
  $$

-:

  $$
  n'=-An+(n\cdot An)n;
  $$

- the pseudo-determinant periodic compression balance;

- the conformal in-plane monodromy;

then the failure is a genuine covariance/plane transition residual.

Thus the strongest branch is not "all planar vorticity."

It is the exact planar Floquet equality branch.

---

# 24. Rank-one boundary

If

$$
\vartheta_2\to0,
$$

the two positive covariance eigenvalues become strongly anisotropic and the branch approaches rank one.

That branch has already been reduced by DCRP-39 to:

$$
\boxed{
\text{Burgers-like axial core}
+
\text{finite rank-lifting annulus}
}
$$

or directional tail escape.

Therefore DCRP-40 only needs to study

$$
\boxed{
\vartheta_2\ge\vartheta_0>0
}
$$

for the genuinely rank-two interior.

---

# 25. Rank-three lifting

If the missing vorticity component appears in a fixed finite annulus:

$$
n\cdot\Omega\neq0,
$$

the covariance becomes full rank after enlarging the core.

Then DCRP-38's determinant-residual theorem becomes available.

Thus a bounded rank-three lifting radius is a finite transition carrier rather than a new infinite-dimensional branch.

If the lifting radius escapes to infinity, it is a directional spatial/scale escape defect.

---

# 26. Frozen-affine equality versus Burgers-like models

The rank-one frozen affine tensor was

$$
\operatorname{diag}
(-a/2,-a/2,a),
$$

with axial vorticity.

The rank-two frozen tensor is

$$
\operatorname{diag}
(c_\gamma/2,c_\gamma/2,-c_\gamma),
$$

with vorticity confined to the expanding plane.

The two geometries are dual in orientation.

They should not be conflated.

The rank-two branch is closer to a planar/pancake or strained-layer geometry than to a tubular Burgers vortex.

---

# 27. Planar Floquet equality manifold

The exact rank-two equality branch consists of:

1. a moving plane:

   $$
   E(s)=n(s)^\perp;
   $$

2. normal equation:

   $$
   n'=-An+(n\cdot An)n;
   $$

3. average normal compression:

   $$
   \langle n\cdot An\rangle=-c_\gamma;
   $$

4. positive in-plane covariance:

   $$
   B|_E>0;
   $$

5. conformal covariance monodromy:

   $$
   MBM^T=e^{c_\gamma S_0}B;
   $$

6. one residual in-plane Floquet rotation angle.

This is a finite-dimensional return geometry coupled to the planar potential--shear field.

---

# 28. Why the normal-compression equality is not a tax

The average identity

$$
\langle n\cdot An\rangle=-c_\gamma
$$

is required by exact DSS covariance periodicity.

It is a canonical equality condition.

It should not be declared a positive cost by itself.

A native residual must measure deviation from this equality or the dynamical source needed to reproduce it.

This is the same quotient-safety principle established earlier for Kelvin contraction.

---

# 29. Candidate reproduction observable

Define the normal-compression mismatch

$$
\boxed{
\mathcal R_{\perp}
=
\int_0^{S_0}
\left|
n\cdot An
+
c_\gamma
\right|^2ds.
}
\tag{29.1}
$$

This vanishes for the frozen equality tensor but need not vanish for a time-dependent Floquet orbit whose average is correct.

Therefore it is too strong to use as the final cost.

A better observable should compare the full planar monodromy against the conformal covariance return:

$$
\boxed{
\mathcal R_{\rm Floq}
=
d
\left(
e^{-c_\gamma S_0/2}
B_0^{-1/2}M_EB_0^{1/2},
SO(2)
\right).
}
\tag{29.2}
$$

Exact rank-two equality has

$$
\mathcal R_{\rm Floq}=0.
$$

This is a quotient-correct finite-dimensional return residual.

---

# 30. Remaining dynamical problem

The planar Floquet equality is not a purely matrix-theoretic object.

The same parent must generate:

- the plane normal motion;
- the planar covariance;
- the potential--shear velocity field;
- the annular affine strain;
- the DCRP-31 inward PFET.

Thus the remaining equality question is:

> can the planar potential--shear dynamics reproduce the exact covariance-conformal monodromy without developing a normal vorticity component or a non-affine/turnover residual?

This is the precise rank-two rigidity problem.

---

# 31. New exact frontier

The next target is

$$
\boxed{
\textbf{
Planar Conformal Floquet Vorticity /
Pancake-Strain Reproduction Rigidity.
}
}
$$

A useful theorem would show that a nonzero strict same-parent DSS rank-two profile satisfying:

$$
\vartheta_2\ge\vartheta_0>0
$$

and exact planar Floquet return must enter at least one of:

1.:

   $$
   \text{finite rank-three lifting};
   $$

2.:

   $$
   \text{rank-one anisotropy collapse};
   $$

3.:

   $$
   \text{nonzero plane/covariance transition residual};
   $$

4.:

   $$
   \text{a fixed/rotating planar Floquet eigenmode};
   $$

5. a potential--shear normal form with enough analytic control to trigger a planar-vorticity regularity/Liouville criterion.

The last two are the equality-manifold branches.

---

# 32. Source-status audit

## Miller 2020

The external theorem proves regularity when the vorticity projected onto a plane remains bounded in the scaling-critical space

$$
L_t^4L_x^2,
$$

allowing the plane to vary provided the orthogonal direction has controlled gradient.

It extends earlier fixed-plane/two-component vorticity criteria.

DCRP-40 does not assume the required mixed norm and therefore does not apply the theorem directly.

## Strained vortex-sheet calibration

Rigorous/exact Navier--Stokes literature includes Burgers-vortex-sheet/layer-type solutions in linear stagnation/strain fields.

This prevents a local planar-vorticity/linear-strain normal form from being dismissed solely by geometry.

The unforced same-parent DSS reproduction remains the essential difference.

---

# 33. End state

The exact rank-two zero-residual covariance branch satisfies

$$
\boxed{
n'
=
-An
+
(n\cdot An)n.
}
$$

The in-plane pseudo-determinant obeys

$$
\boxed{
\frac d{ds}
\log\det_+B
=
-2
\left[
c_\gamma+n\cdot An
\right].
}
$$

DSS periodicity forces

$$
\boxed{
\left\langle
n\cdot An
\right\rangle
=
-c_\gamma.
}
$$

For frozen affine strain the only nondegenerate periodic rank-two solution is

$$
\boxed{
A
=
\frac{c_\gamma}{2}P_{n^\perp}
-
c_\gamma n\otimes n.
}
$$

For time-periodic affine strain the support-plane monodromy is covariance-conformal:

$$
\boxed{
e^{-c_\gamma S_0/2}
B_0^{-1/2}
M_E
B_0^{1/2}
\in SO(2).
}
$$

A fixed planar vorticity field has the local representation

$$
\boxed{
V=(\nabla_h\phi,w),
\qquad
\Omega_h=(\partial_2q,-\partial_1q),
\qquad
q=w-\partial_3\phi.
}
$$

Unlike rank one, global planar vorticity is not kinematically trivial; compactly supported counterexamples exist.

Therefore the strongest low-rank survivor is now:

$$
\boxed{
\textbf{
planar potential--shear DSS}
+
\textbf{
conformal covariance Floquet return}.
}
$$

The next frontier is:

$$
\boxed{
\textbf{
Planar Conformal Floquet Vorticity /
Pancake-Strain Reproduction Rigidity.
}
}
$$