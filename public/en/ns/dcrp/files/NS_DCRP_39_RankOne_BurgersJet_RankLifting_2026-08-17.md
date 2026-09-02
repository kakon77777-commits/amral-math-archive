# NS-DCRP-39 — Rank-One Vorticity Core Decomposition, Burgers-Jet Normal Form, and Finite-Radius Rank Lifting

- date: 2026-08-17
- status: research proof checkpoint / low-rank rigidity round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. attack the rank-one branch left by DCRP-38;
  2. prove that a spatially common vorticity direction forces axial invariance of the vorticity magnitude;
  3. derive the exact local velocity decomposition into a two-dimensional vortical carrier plus a finite-dimensional affine strain jet;
  4. show that all three-dimensional vortex stretching in the rank-one core is carried by the affine jet;
  5. prove a global rank-one Liouville theorem under the strict DSS sublinear energy-tail growth;
  6. conclude that every nonzero rank-one core must undergo finite-radius vorticity-direction spreading or directional tail escape;
  7. reduce the remaining low-rank problem to rank-two planar covariance and the rank-lifting annulus.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - P. Constantin, C. Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier--Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775--789;
  - Y. Maekawa, H. Miura, C. Prange, *On stability of blow-up solutions of the Burgers vortex type for the Navier--Stokes equations with a linear strain*, arXiv:1807.10341;
  - E. Miller, *A locally anisotropic regularity criterion for the Navier--Stokes equation in terms of vorticity*, arXiv:2002.02152.
- internal dependencies:
  - DCRP-35 finite-annulus affine strain supplier;
  - DCRP-38 covariance determinant rigidity and rank-one/rank-two collapse.
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

The strongest low-rank branch is

$$
\boxed{
\operatorname{rank}B=1.
}
\tag{1.3}
$$

On any connected active core on which

$$
\phi>0
$$

and the vorticity is nonzero, rank one implies the existence of a spatially constant unit vector

$$
\boxed{
e=e(s)
}
\tag{1.4}
$$

such that

$$
\boxed{
\Omega(y,s)
=
\omega(y,s)e(s).
}
\tag{1.5}
$$

The first main result is immediate but decisive.

Since

$$
\nabla\cdot\Omega=0,
$$

$$
\boxed{
e(s)\cdot\nabla\omega(y,s)=0.
}
\tag{1.6}
$$

Thus the vorticity magnitude is constant along the common vorticity axis.

The second main result uses the DSS vorticity equation.

Let

$$
\boxed{
W=\gamma y+V.
}
\tag{1.7}
$$

The vorticity equation is

$$
\boxed{
D_s\Omega+\Omega
=
(\Omega\cdot\nabla)V,
\qquad
D_s
=
\partial_s+W\cdot\nabla.
}
\tag{1.8}
$$

Because

$$
\Omega=\omega e,
$$

$$
\boxed{
(\Omega\cdot\nabla)V
=
\omega\,\partial_eV.
}
\tag{1.9}
$$

Also

$$
\boxed{
\operatorname{curl}
(
\partial_eV
)
=
\partial_e\Omega
=
0,
}
\tag{1.10}
$$

and

$$
\boxed{
\nabla\cdot
(
\partial_eV
)
=
0.
}
\tag{1.11}
$$

Therefore

$$
\partial_eV
$$

is a harmonic, curl-free, divergence-free vector field on the active core.

Comparing perpendicular and parallel components in the vorticity equation gives

$$
\boxed{
P_{e^\perp}
\partial_eV
=
e'(s).
}
\tag{1.12}
$$

On a connected nonzero-vorticity component write

$$
\partial_eV
=
e'
+
a(y,s)e.
$$

Since

$$
\operatorname{curl}
(
\partial_eV
)=0,
$$

$$
\nabla a\times e=0.
$$

Since

$$
\nabla\cdot
(
\partial_eV
)=0,
$$

$$
e\cdot\nabla a=0.
$$

Hence

$$
\boxed{
\nabla a=0.
}
\tag{1.13}
$$

Thus

$$
\boxed{
\partial_eV
=
e'(s)
+
a(s)e(s)
}
\tag{1.14}
$$

is spatially constant on every connected rank-one vortical component.

This is the central local rigidity of DCRP-39.

Define

$$
\boxed{
P_\perp
=
I-e\otimes e.
}
\tag{1.15}
$$

Define the symmetric trace-free affine tensor

$$
\boxed{
A_{\rm ax}(s)
=
a(s)
\left[
e\otimes e
-
\frac12P_\perp
\right]
+
e'(s)\otimes e
+
e\otimes e'(s).
}
\tag{1.16}
$$

Then

$$
\boxed{
A_{\rm ax}^T
=
A_{\rm ax},
\qquad
\operatorname{tr}A_{\rm ax}=0,
}
\tag{1.17}
$$

and

$$
\boxed{
A_{\rm ax}e
=
e'+ae.
}
\tag{1.18}
$$

Therefore, after subtracting the affine field,

$$
\boxed{
U
=
V
-
A_{\rm ax}(s)y,
}
\tag{1.19}
$$

one has

$$
\boxed{
\partial_eU=0.
}
\tag{1.20}
$$

Moreover

$$
\operatorname{curl}(A_{\rm ax}y)=0
$$

because

$$
A_{\rm ax}
$$

is symmetric.

Hence

$$
\boxed{
\nabla\times U
=
\omega e.
}
\tag{1.21}
$$

Since

$$
\partial_eU=0
$$

and the perpendicular vorticity components vanish, the axial component

$$
U\cdot e
$$

is spatially constant on the connected core.

Absorb that constant into a translation

$$
b(s).
$$

The remaining velocity

$$
U_{2D}
$$

is tangent to

$$
e^\perp,
$$

independent of the axial coordinate, and divergence free in the transverse plane.

Thus the exact rank-one local normal form is

$$
\boxed{
V(y,s)
=
U_{2D}
(
P_\perp y,s
)
+
A_{\rm ax}(s)y
+
b(s).
}
\tag{1.22}
$$

Here

$$
\boxed{
U_{2D}\cdot e=0,
\qquad
\partial_eU_{2D}=0,
\qquad
\nabla\cdot U_{2D}=0,
}
\tag{1.23}
$$

and

$$
\boxed{
\nabla\times U_{2D}
=
\omega e.
}
\tag{1.24}
$$

Therefore the rank-one core is exactly:

$$
\boxed{
\textbf{
two-dimensional vortical carrier}
+
\textbf{
finite-dimensional three-dimensional affine strain}.
}
}
\tag{1.25}
$$

This is substantially stronger than a qualitative statement that the vorticity directions are aligned.

The third main result identifies the stretching.

The two-dimensional part satisfies

$$
\partial_eU_{2D}=0.
$$

Hence

$$
\boxed{
(\Omega\cdot\nabla)U_{2D}=0.
}
\tag{1.26}
$$

All vortex stretching is supplied by

$$
A_{\rm ax}.
$$

Indeed

$$
\boxed{
(\Omega\cdot\nabla)V
=
\omega
A_{\rm ax}e
=
\omega
(e'+ae).
}
\tag{1.27}
$$

The scalar vorticity magnitude obeys

$$
\boxed{
D_s\omega
=
(a(s)-1)
\omega.
}
\tag{1.28}
$$

The stretching work is

$$
\boxed{
\Omega\cdot S\Omega
=
a(s)
|\Omega|^2.
}
\tag{1.29}
$$

Thus the whole rank-one stretching geometry is encoded by:

- one scalar axial stretch:

  $$
  a(s);
  $$

- two components of axis rotation:

  $$
  e'(s)\in e^\perp.
  $$

The full five-dimensional affine strain fiber of DCRP-35 collapses to a three-dimensional rank-one Burgers-jet fiber.

If

$$
\boxed{
e'(s)=0,
}
\tag{1.30}
$$

then

$$
\boxed{
A_{\rm ax}
=
a(s)
\left[
e\otimes e-\frac12P_\perp
\right].
}
\tag{1.31}
$$

In coordinates with

$$
e=e_3,
$$

$$
\boxed{
A_{\rm ax}
=
\operatorname{diag}
\left(
-a/2,
-a/2,
a
\right).
}
\tag{1.32}
$$

This is precisely the local linear strain geometry associated with Burgers-type axial vortex models.

DCRP-39 does **not** identify the rank-one Type-II profile with an actual Burgers vortex.

The external Burgers-vortex literature is used only as calibration that:

$$
\boxed{
\textbf{
2D vorticity}
+
\textbf{
3D linear strain}
}
$$

is a mathematically legitimate local Navier--Stokes mechanism.

The fourth main result is a global Liouville theorem.

Let

$$
V:
\mathbb R^3\times[0,S_0]
\to
\mathbb R^3
$$

be smooth and suppose that for each

$$
s
$$

there is a spatially constant unit vector

$$
e(s)
$$

such that

$$
\boxed{
\Omega(y,s)
=
\omega(y,s)e(s)
}
\tag{1.33}
$$

globally.

Assume the strict DSS critical-tail bound

$$
\boxed{
\sup_{s\in[0,S_0]}
\int_{B_R}
|V(y,s)|^2dy
\le
C
R^\kappa,
\qquad
0<\kappa<1.
}
\tag{1.34}
$$

Then

$$
\boxed{
V\equiv0.
}
\tag{1.35}
$$

The proof is elementary and does not use a Navier--Stokes regularity criterion.

Fix

$$
s
$$

and suppress time.

Set

$$
\boxed{
Z
=
\partial_eV.
}
\tag{1.36}
$$

Since

$$
\partial_e\Omega=0,
$$

$$
\boxed{
\nabla\times Z=0.
}
\tag{1.37}
$$

Since

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot Z=0.
}
\tag{1.38}
$$

Therefore

$$
\boxed{
\Delta Z=0
}
\tag{1.39}
$$

componentwise on all of

$$
\mathbb R^3.
$$

Fix a point

$$
x.
$$

For large

$$
R,
$$

coarea gives a radius

$$
r\in[R,2R]
$$

such that

$$
\boxed{
\int_{\partial B_r(x)}
|V|^2dS
\le
C
R^{\kappa-1}.
}
\tag{1.40}
$$

Because

$$
Z
$$

is harmonic, its mean-value property gives

$$
Z(x)
=
\frac1{|B_r|}
\int_{B_r(x)}
Z(y)dy.
$$

Since

$$
Z=\partial_eV,
$$

the divergence theorem gives

$$
\boxed{
Z(x)
=
\frac1{|B_r|}
\int_{\partial B_r(x)}
V(y)
(e\cdot n)
dS.
}
\tag{1.41}
$$

Therefore

$$
\begin{aligned}
|Z(x)|
&\le
C
r^{-3}
|\partial B_r|^{1/2}
\left(
\int_{\partial B_r}
|V|^2dS
\right)^{1/2}
\\
&\le
C
R^{-3}
R
R^{(\kappa-1)/2}
\\
&=
C
R^{(\kappa-5)/2}.
\end{aligned}
$$

Let

$$
R\to\infty.
$$

Thus

$$
\boxed{
\partial_eV=0.
}
\tag{1.42}
$$

Hence

$$
V
$$

is invariant along the direction

$$
e.
$$

If

$$
V
$$

is nonzero, continuity provides a bounded transverse disk

$$
D\subset e^\perp
$$

with

$$
\boxed{
\int_D
|V|^2
dA
=
c_D>0.
}
\tag{1.43}
$$

By axial invariance, a cylinder of length

$$
R
$$

contains energy

$$
\boxed{
\ge
c_D R.
}
\tag{1.44}
$$

Such a cylinder lies in a ball of radius

$$
CR.
$$

Therefore

$$
\boxed{
\int_{B_{CR}}
|V|^2
\ge
c_D R.
}
\tag{1.45}
$$

But

$$
\kappa<1
$$

gives

$$
R^\kappa=o(R).
$$

Contradiction.

Thus

$$
V=0.
$$

Hence:

$$
\boxed{
\textbf{
nonzero strict DSS profile}
\notin
\textbf{
global rank-one vorticity class}.
}
\tag{1.46}
$$

This is the strongest result of DCRP-39.

The fifth main result is the finite-radius rank-lifting consequence.

Suppose a nonzero strict DSS profile has a rank-one core:

$$
\Omega
=
\omega e(s)
$$

on

$$
B_{r_0}.
$$

Define the directional-spreading function

$$
\boxed{
\mathcal D_e(R)
=
\int_0^{S_0}
\int_{B_R}
|
\Omega(y,s)
\times
e(s)
|^2
dyds.
}
\tag{1.47}
$$

Then

$$
\boxed{
\mathcal D_e(r_0)=0.
}
\tag{1.48}
$$

If

$$
\mathcal D_e(R)=0
$$

for every finite

$$
R,
$$

the vorticity is globally rank one and the global Liouville theorem forces

$$
V=0.
$$

Therefore every nonzero rank-one core has

$$
\boxed{
\exists
R_\ast<\infty:
\quad
\mathcal D_e(R_\ast)>0.
}
\tag{1.49}
$$

Thus:

$$
\boxed{
\textbf{
nonzero rank-one core}
\Longrightarrow
\textbf{
finite-radius vorticity-direction spreading}.
}
\tag{1.50}
$$

For a sequence of normalized profiles, there are two possibilities.

### bounded rank-lift radius

The first radius where

$$
\mathcal D_e
$$

becomes positive remains bounded in normalized coordinates.

Then the rank-one core has a finite annular **direction-spreading/rank-lifting carrier**.

### escaping rank-lift radius

The first rank-lifting radius tends to

$$
\infty.
$$

Then the rank-one geometry persists on every fixed normalized core and breaks only in the tail.

This is an explicit directional spatial-escape defect.

Therefore:

$$
\boxed{
\textbf{
rank-one core}
\Longrightarrow
\textbf{
finite rank-lifting annulus}
\ \vee\
\textbf{
directional tail escape}.
}
\tag{1.51}
$$

The rank-one branch is therefore globally closed modulo an explicit finite-radius/tail transition.

The next unresolved low-rank branch is

$$
\boxed{
\operatorname{rank}B=2.
}
\tag{1.52}
$$

There the vorticity lies in a common plane but need not be invariant along one direction.

This is substantially less rigid.

The correct next frontier is

$$
\boxed{
\textbf{
Rank-Two Planar Vorticity /
Directional-Spread Matching Rigidity.
}
}
\tag{1.53}
$$

The rank-two analysis should combine:

1. the common-plane vorticity constraint;
2. one-component vorticity / anisotropic regularity mechanisms;
3. the DCRP-31 inward PFET requirement;
4. the DCRP-35 finite-annulus strain supplier;
5. the finite rank-lifting transition found in the rank-one branch.

---

# 2. Rank-one covariance implies a common direction

Let

$$
\phi>0
$$

on a connected active core and

$$
B
=
\int
\phi
\Omega\otimes\Omega.
$$

Assume

$$
\operatorname{rank}B=1.
$$

Let

$$
e
$$

span

$$
\operatorname{Ran}B.
$$

For every

$$
n\perp e,
$$

$$
0
=
n^TBn
=
\int
\phi
|
n\cdot\Omega
|^2.
$$

Therefore

$$
n\cdot\Omega=0
$$

throughout the active core.

Thus

$$
\boxed{
\Omega=\omega e.
}
\tag{2.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 3. Axial invariance of vorticity magnitude

Since

$$
\nabla\cdot\Omega=0,
$$

$$
0
=
\nabla\cdot(\omega e)
=
e\cdot\nabla\omega,
$$

because

$$
e=e(s)
$$

is spatially constant.

Thus

$$
\boxed{
\partial_e\omega=0.
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

# 4. Direction equation inside a rank-one core

The vorticity equation is

$$
D_s(\omega e)
+
\omega e
=
\omega\partial_eV.
$$

Expand:

$$
(D_s\omega)e
+
\omega e'
+
\omega e
=
\omega\partial_eV.
$$

On

$$
\omega\neq0,
$$

$$
\boxed{
\partial_eV
=
e'
+
\left[
1
+
D_s\log|\omega|
\right]
e.
}
\tag{4.1}
$$

The perpendicular component is independent of position.

The next sections show that the parallel coefficient is also spatially constant.

---

# 5. Axial derivative is harmonic

Because

$$
\partial_e\Omega=0,
$$

$$
\boxed{
\nabla\times
(
\partial_eV
)
=
0.
}
\tag{5.1}
$$

Because

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot
(
\partial_eV
)
=
0.
}
\tag{5.2}
$$

Thus

$$
\boxed{
\Delta
(
\partial_eV
)
=
0.
}
\tag{5.3}
$$

This holds on every connected rank-one core.

---

# 6. Spatial constancy of the axial stretching vector

Write

$$
\partial_eV
=
e'
+
a(y,s)e.
$$

Curl-free gives

$$
\boxed{
\nabla a\times e=0.
}
\tag{6.1}
$$

Divergence-free gives

$$
\boxed{
e\cdot\nabla a=0.
}
\tag{6.2}
$$

Together:

$$
\boxed{
\nabla a=0.
}
\tag{6.3}
$$

Hence

$$
\boxed{
a=a(s).
}
\tag{6.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Rank-one affine strain tensor

Define

$$
P_\perp
=
I-e\otimes e.
$$

Set

$$
\boxed{
A_{\rm ax}
=
a
\left[
e\otimes e
-
\frac12P_\perp
\right]
+
e'\otimes e
+
e\otimes e'.
}
\tag{7.1}
$$

Because

$$
e\cdot e'=0,
$$

$$
\boxed{
A_{\rm ax}=A_{\rm ax}^T,
}
\tag{7.2}
$$

and

$$
\boxed{
\operatorname{tr}A_{\rm ax}=0.
}
\tag{7.3}
$$

Also

$$
\boxed{
A_{\rm ax}e
=
ae+e'.
}
\tag{7.4}
$$

Thus the affine field

$$
A_{\rm ax}y
$$

has precisely the axial derivative required by the rank-one vorticity equation.

---

# 8. Two-dimensional remainder

Define

$$
\widetilde U
=
V-A_{\rm ax}y.
$$

Then

$$
\boxed{
\partial_e\widetilde U=0.
}
\tag{8.1}
$$

Because

$$
A_{\rm ax}
$$

is symmetric,

$$
\boxed{
\nabla\times
(
A_{\rm ax}y
)
=
0.
}
\tag{8.2}
$$

Thus

$$
\boxed{
\nabla\times\widetilde U
=
\omega e.
}
\tag{8.3}
$$

Also

$$
\operatorname{tr}A_{\rm ax}=0
$$

gives

$$
\boxed{
\nabla\cdot\widetilde U=0.
}
\tag{8.4}
$$

Choose instantaneous coordinates with

$$
e=e_3.
$$

Since

$$
\partial_3\widetilde U=0,
$$

the first two components of

$$
\nabla\times\widetilde U
$$

are

$$
\partial_2\widetilde U_3
$$

and

$$
-\partial_1\widetilde U_3.
$$

They vanish.

Hence

$$
\boxed{
\nabla_\perp\widetilde U_3=0.
}
\tag{8.5}
$$

So

$$
\widetilde U_3
$$

is spatially constant on the connected core.

Absorb it into

$$
b(s).
$$

The remaining field is genuinely two-dimensional.

---

# 9. NEW THEOREM — Local Rank-One Burgers-Jet Normal Form

## Theorem 9.1

On every connected nonzero-vorticity rank-one core,

$$
\boxed{
V(y,s)
=
U_{2D}
(
P_\perp y,s
)
+
A_{\rm ax}(s)y
+
b(s),
}
\tag{9.1}
$$

where:

$$
\boxed{
U_{2D}\cdot e=0,
}
\tag{9.2}
$$

$$
\boxed{
\partial_eU_{2D}=0,
}
\tag{9.3}
$$

$$
\boxed{
\nabla\cdot U_{2D}=0,
}
\tag{9.4}
$$

and

$$
\boxed{
\nabla\times U_{2D}
=
\omega e.
}
\tag{9.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 10. Fixed-axis subbranch

If

$$
e'=0,
$$

then

$$
\boxed{
A_{\rm ax}
=
a
\left[
e\otimes e
-
\frac12P_\perp
\right].
}
\tag{10.1}
$$

In the adapted basis:

$$
\boxed{
A_{\rm ax}
=
\begin{pmatrix}
-a/2&0&0\\
0&-a/2&0\\
0&0&a
\end{pmatrix}.
}
\tag{10.2}
$$

Thus the rank-one core is a two-dimensional vortex embedded in a uniform axisymmetric extensional strain.

This is the exact local Burgers-jet geometry.

---

# 11. Rotating-axis subbranch

If

$$
e'\neq0,
$$

the additional symmetric term

$$
\boxed{
e'\otimes e
+
e\otimes e'
}
\tag{11.1}
$$

rotates the common vorticity axis.

The rank-one 3D geometry is still finite dimensional.

It is determined by:

-:

  $$
  a(s);
  $$

-:

  $$
  e(s)\in S^2.
  $$

Thus the affine fiber has at most three instantaneous degrees of freedom.

---

# 12. Scalar vorticity equation

Insert

$$
\partial_eV=e'+ae
$$

into the vector vorticity equation.

The perpendicular terms

$$
\omega e'
$$

cancel.

The parallel part gives

$$
\boxed{
D_s\omega
=
(a-1)\omega.
}
\tag{12.1}
$$

Therefore the rank-one vorticity carrier is a two-dimensional transport-amplification scalar driven by the single axial strain coefficient

$$
a(s).
$$

---

# 13. Stretching collapse

Because

$$
(\Omega\cdot\nabla)U_{2D}=0,
$$

$$
\boxed{
\Omega\cdot S\Omega
=
a(s)
|\Omega|^2.
}
\tag{13.1}
$$

Thus the positive stretching problem collapses from a tensor phase problem to a scalar sign/amplitude problem:

$$
\boxed{
a(s)>0.
}
\tag{13.2}
$$

This is the strongest phase simplification obtained in the DCRP chain.

---

# 14. Local harmonic interpretation

Equivalently, on a simply connected subcore one may write

$$
V
=
U_{2D}
+
\nabla\phi,
$$

with

$$
\Delta\phi=0.
$$

The rank-one vorticity equation forces the axial derivative of

$$
\nabla\phi
$$

to be the spatially constant vector

$$
e'+ae.
$$

Thus the genuinely three-dimensional part of the harmonic potential is affine.

This is another route to Theorem 9.1.

---

# 15. External Burgers-vortex calibration

Burgers-vortex analysis demonstrates that a two-dimensional/axial vorticity carrier can be maintained in a prescribed linear straining field and that such vortex structures have rigorous stability theories in appropriate strained Navier--Stokes settings.

Therefore:

$$
\boxed{
\textbf{
local rank-one Burgers-jet geometry is not intrinsically impossible.
}
}
\tag{15.1}
$$

The DCRP exclusion must use:

- unforced same-parent reproduction;
- critical DSS tail growth;
- PFET/transition structure;

rather than local geometry alone.

---

# 16. Global rank-one hypotheses

Assume now:

$$
V
$$

is smooth on

$$
\mathbb R^3\times[0,S_0],
$$

and for every

$$
s
$$

there exists a spatially constant unit vector

$$
e(s)
$$

such that

$$
\Omega=\omega e
$$

globally.

Assume:

$$
\boxed{
\sup_s
\int_{B_R}
|V|^2
\le
CR^\kappa
}
\tag{16.1}
$$

for:

$$
R\ge1,
$$

with:

$$
\boxed{
\kappa<1.
}
\tag{16.2}
$$

The strict DCRP tail has

$$
0<\kappa<1.
$$

---

# 17. Entire axial derivative is harmonic

For fixed

$$
s,
$$

let:

$$
Z=\partial_eV.
$$

Since:

$$
\partial_e\Omega=0,
$$

$$
\nabla\times Z=0.
$$

Since:

$$
\nabla\cdot V=0,
$$

$$
\nabla\cdot Z=0.
$$

Hence:

$$
\boxed{
\Delta Z=0
}
\tag{17.1}
$$

on:

$$
\mathbb R^3.
$$

---

# 18. Coarea surface bound

Fix:

$$
x\in\mathbb R^3.
$$

For:

$$
R
$$

large,

$$
\int_R^{2R}
\int_{\partial B_r(x)}
|V|^2dSdr
\le
\int_{B_{3R}(0)}
|V|^2dy
\le
CR^\kappa
$$

after adjusting the ball center by a fixed constant.

Therefore there exists:

$$
r\in[R,2R]
$$

with

$$
\boxed{
\int_{\partial B_r(x)}
|V|^2dS
\le
CR^{\kappa-1}.
}
\tag{18.1}
$$

---

# 19. Harmonic mean-value estimate from the velocity tail

Since:

$$
Z
$$

is harmonic,

$$
Z(x)
=
\frac1{|B_r|}
\int_{B_r(x)}
Z(y)dy.
$$

Using:

$$
Z=\partial_eV
$$

and the divergence theorem:

$$
\boxed{
Z(x)
=
\frac1{|B_r|}
\int_{\partial B_r(x)}
V(y)
(e\cdot n)
dS.
}
\tag{19.1}
$$

Thus:

$$
\begin{aligned}
|Z(x)|
&\le
Cr^{-3}
r
\left(
\int_{\partial B_r(x)}
|V|^2dS
\right)^{1/2}
\\
&\le
C
R^{(\kappa-5)/2}.
\end{aligned}
$$

Since:

$$
\kappa<5,
$$

$$
\boxed{
Z(x)=0.
}
\tag{19.2}
$$

Therefore:

$$
\boxed{
\partial_eV=0
}
\tag{19.3}
$$

globally.

The estimate is much stronger than needed for the strict tail exponent.

---

# 20. Axial-invariance energy lower bound

If:

$$
V
$$

is nonzero, choose a bounded disk

$$
D\subset e^\perp
$$

with:

$$
\boxed{
\int_D
|V|^2dA
=
c_D>0.
}
\tag{20.1}
$$

Because:

$$
\partial_eV=0,
$$

the cylinder

$$
D\times[-R,R]
$$

has energy:

$$
\boxed{
2Rc_D.
}
\tag{20.2}
$$

The cylinder is contained in a ball of radius

$$
CR.
$$

Thus:

$$
\boxed{
\int_{B_{CR}}
|V|^2
\ge
cR.
}
\tag{20.3}
$$

This contradicts:

$$
\int_{B_{CR}}
|V|^2
\lesssim
R^\kappa
$$

when:

$$
\kappa<1.
$$

---

# 21. NEW THEOREM — Global Rank-One Critical-Tail Liouville

## Theorem 21.1

Under Sections 16--20:

$$
\boxed{
V\equiv0.
}
\tag{21.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This theorem is project-internal and uses only:

- global spatially common vorticity direction;
- incompressibility;
- smoothness;
- sublinear kinetic-energy growth.

It does not use a global Navier--Stokes regularity theorem.

---

# 22. Relationship to vorticity-direction regularity theory

The classical Constantin--Fefferman program shows that sufficiently coherent vorticity direction is strongly regularity-favorable for three-dimensional Navier--Stokes.

DCRP-39 does not apply that theorem directly to the prelimit singular branch.

Instead it proves an exact Liouville statement for the final strict DSS rank-one profile using its special sublinear tail growth.

This avoids a profile-to-parent overclaim.

---

# 23. Directional-spreading observable

Let:

$$
e(s)
$$

be the rank-one core axis.

Define:

$$
\boxed{
\mathcal D_e(R)
=
\int_0^{S_0}
\int_{B_R}
|
\Omega(y,s)\times e(s)
|^2
dyds.
}
\tag{23.1}
$$

Then on the rank-one core:

$$
\boxed{
\mathcal D_e(r_0)=0.
}
\tag{23.2}
$$

The quantity is nonnegative and monotone in:

$$
R.
$$

---

# 24. NEW THEOREM — Finite-Radius Rank Lifting

## Theorem 24.1

Let:

$$
V
$$

be a nonzero strict DSS profile satisfying the critical tail bound and having a rank-one core.

Then:

$$
\boxed{
\exists
R_\ast<\infty:
\quad
\mathcal D_e(R_\ast)>0.
}
\tag{24.1}
$$

### Proof

If:

$$
\mathcal D_e(R)=0
$$

for every finite:

$$
R,
$$

then:

$$
\Omega(y,s)\parallel e(s)
$$

globally.

Apply Theorem 21.1.

Then:

$$
V=0,
$$

contradiction.

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

# 25. Rank-lift radius

Define:

$$
\boxed{
R_{\rm lift}
=
\inf
\left\{
R>r_0:
\mathcal D_e(R)>0
\right\}.
}
\tag{25.1}
$$

For every nonzero strict rank-one core:

$$
\boxed{
R_{\rm lift}<\infty.
}
\tag{25.2}
$$

The vorticity-direction collapse must break at finite relative radius.

---

# 26. Sequence-level dichotomy

For a sequence of same-parent normalized profiles:

### tight rank lifting

$$
\boxed{
\sup_n
R_{{\rm lift},n}
<
\infty.
}
\tag{26.1}
$$

Then a fixed finite annular region contains the direction-spreading carrier.

### rank-lift escape

$$
\boxed{
R_{{\rm lift},n}
\to\infty.
}
\tag{26.2}
$$

Then the rank-one core persists on every fixed compact normalized set and loses rank only in the normalized tail.

This is a directional spatial-escape / transition defect.

Thus:

$$
\boxed{
\textbf{
rank-one core}
\Longrightarrow
\textbf{
finite annular rank lifting}
\ \vee\
\textbf{
directional tail escape}.
}
\tag{26.3}
$$

---

# 27. Finite annular direction carrier

On the tight branch define, for fixed:

$$
R_1>r_0,
$$

$$
\boxed{
\mathcal R_{\rm dir}
=
\int_0^{S_0}
\int_{
B_{R_1}\setminus B_{r_0}
}
|
\Omega\times e
|^2
dyds.
}
\tag{27.1}
$$

If the first rank-lift radius is uniformly bounded and the profile class is compact with a fixed nontriviality normalization, a finite annular direction-spreading witness can be extracted.

The exact quantitative uniform lower gap requires a compact-class declaration and is not asserted unconditionally here.

---

# 28. Coupling to the affine supplier

The rank-one core needs axial stretching:

$$
a(s).
$$

The global rank-one theorem shows that the same common direction cannot persist throughout the entire critical tail.

Therefore the external strain supplier eventually couples the axial core to vorticity carrying additional directions.

Thus the Burgers-like rank-one core is necessarily embedded in a genuinely three-dimensional direction-spreading environment.

This is the unforced same-parent replacement for the externally prescribed background strain in classical Burgers models.

---

# 29. Fixed-axis Burgers calibration versus unforced parent

In a classical Burgers-type model, the linear strain is prescribed as part of the background dynamics.

In the DCRP rank-one branch:

$$
A_{\rm ax}
$$

cannot be an independent external field.

It must be reproduced by the same global parent whose vorticity direction necessarily lifts rank outside the core.

Therefore the unresolved coupling is:

$$
\boxed{
\textbf{
2D/axial core}
\leftrightarrow
\textbf{
finite 3D rank-lifting annulus}.
}
\tag{29.1}
$$

This is substantially narrower than a generic three-dimensional strain-supplier problem.

---

# 30. Rank-two branch

If:

$$
\operatorname{rank}B=2,
$$

there exists a spatially constant unit normal:

$$
n(s)
$$

such that:

$$
\boxed{
n(s)\cdot\Omega(y,s)=0
}
\tag{30.1}
$$

throughout the active core.

This is equivalent to vanishing of one vorticity component in a moving orientation frame.

Unlike rank one, it does not imply invariance in any spatial direction.

Therefore the local two-dimensional decomposition used above does not apply.

Rank two is the genuine remaining low-rank geometry.

---

# 31. External anisotropic calibration

One-component/two-component vorticity regularity theory shows that controlling vorticity projected onto selected planes or directions can be regularity-favorable under critical analytic bounds.

This indicates that the rank-two geometry is not arbitrary.

However DCRP-39 does not claim that the exact local rank-two profile automatically satisfies the hypotheses of those global Navier--Stokes criteria.

They are used only to calibrate the next route.

---

# 32. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Rank-Two Planar Vorticity /
Directional-Spread Matching Rigidity.
}
}
$$

A useful theorem would start from:

$$
n(s)\cdot\Omega=0
$$

on the strict DSS core and prove at least one of:

1. a quantitative planar-vorticity depletion/regularity mechanism;
2. a finite-radius rank-three lifting carrier;
3. a nonzero non-affine strain/covariance-turnover residual;
4. a planar DSS normal form incompatible with the DCRP-31 inward PFET;
5. a moving-plane transition defect.

The rank-two branch is now the principal low-rank survivor.

---

# 33. Source-status audit

## Constantin--Fefferman

The 1993 work established a foundational connection between coherence of the vorticity direction and Navier--Stokes regularity.

DCRP-39 uses this only as geometric calibration.

Its global rank-one Liouville theorem is proved independently from the strict DSS sublinear energy tail.

## Maekawa--Miura--Prange

The primary source analyzes Navier--Stokes dynamics in the presence of a time-dependent linear strain and establishes stability results for Burgers-vortex-type blow-up profiles.

This confirms that an axial vorticity carrier embedded in a linear strain is a meaningful mathematical mechanism.

It does not provide an unforced finite-energy same-parent singular solution of the type required by DCRP.

## Miller

The primary source proves a locally anisotropic vorticity regularity criterion in which vorticity restricted to a plane is controlled in a scale-critical space.

This is relevant calibration for the next rank-two planar-vorticity branch.

---

# 34. End state

The rank-one core is exactly:

$$
\boxed{
V
=
U_{2D}
+
A_{\rm ax}y
+
b,
}
$$

with:

$$
\boxed{
A_{\rm ax}
=
a
\left[
e\otimes e-\frac12P_\perp
\right]
+
e'\otimes e
+
e\otimes e'.
}
$$

The vorticity obeys:

$$
\boxed{
\Omega=\omega e,
\qquad
\partial_e\omega=0,
}
$$

and:

$$
\boxed{
D_s\omega=(a-1)\omega.
}
$$

All three-dimensional stretching is carried by the finite-dimensional affine jet:

$$
\boxed{
\Omega\cdot S\Omega
=
a|\Omega|^2.
}
$$

If rank one persists globally, the critical tail bound:

$$
\int_{B_R}|V|^2
\lesssim
R^\kappa,
\qquad
\kappa<1,
$$

forces:

$$
\boxed{
V=0.
}
$$

Therefore every nonzero rank-one strict DSS core must lose the common vorticity direction at a finite normalized radius or through a directional tail-escape sequence.

Thus the rank-one branch is globally reduced to:

$$
\boxed{
\textbf{
Burgers-like 2D/axial core}
+
\textbf{
finite 3D rank-lifting annulus}
}
$$

or:

$$
\boxed{
\textbf{
directional tail escape}.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Rank-Two Planar Vorticity /
Directional-Spread Matching Rigidity.
}
}
$$