# NS-DCRP-41 — Planar Covariance Shape Disk, Hyperbolic Shear Action, and the Moving Pancake-Jet Normal Form

- date: 2026-08-17
- status: research proof checkpoint / rank-two shape-rigidity round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. refine the DCRP-40 rank-two planar Floquet equality by separating covariance magnitude, shape anisotropy, and in-plane orientation;
  2. derive an exact two-dimensional disk equation for the normalized in-plane covariance;
  3. invert that equation to reconstruct the in-plane deviatoric strain from covariance-shape motion;
  4. derive a positive hyperbolic shape/phase action;
  5. prove that zero shape-action forces pointwise isotropic affine extension on the vorticity plane;
  6. reconstruct the full three-dimensional affine tensor on that equality branch as a moving pancake jet;
  7. obtain a universal periodic reproduction-action lower bound from the strict DSS normal-compression condition;
  8. calibrate, but not identify, the final branch against exact Euler pancake/vortex-sheet mechanisms;
  9. identify the next frontier as the scalar/potential--shear dynamics inside the moving pancake jet.
- no full Navier--Stokes regularity claim is made.
- principal external primary calibration:
  - D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782;
  - A. Enciso, A. J. Fernández, D. Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233.
- internal dependencies:
  - DCRP-36 affine-jet reproduction action;
  - DCRP-38 covariance matrix ledger;
  - DCRP-40 rank-two planar covariance / Floquet compression.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-40 reduced the exact rank-two zero-covariance-residual branch to

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
\tag{1.1}
$$

where

$$
\boxed{
c_\gamma
=
2-3\gamma
>
0,
}
\tag{1.2}
$$

and

$$
\boxed{
\operatorname{rank}B=2.
}
\tag{1.3}
$$

Let

$$
n(s)
$$

be the unit normal spanning

$$
\ker B(s).
$$

Then

$$
\boxed{
n'
=
-An
+
(n\cdot An)n.
}
\tag{1.4}
$$

The period-averaged normal compression is

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
n\cdot An\,ds
=
-c_\gamma.
}
\tag{1.5}
$$

DCRP-41 now separates the **in-plane covariance shape** from its magnitude.

Choose a Fermi--Walker orthonormal frame

$$
E(s)
=
(e_1(s),e_2(s))
$$

for the plane

$$
n(s)^\perp,
$$

satisfying

$$
\boxed{
E^TE=I_2,
\qquad
E^Tn=0,
\qquad
E^TE'=0.
}
\tag{1.6}
$$

Define the positive in-plane covariance

$$
\boxed{
C
=
E^TBE.
}
\tag{1.7}
$$

Then the Fermi-frame connection drops out of the covariance equation and

$$
\boxed{
C'
=
A_EC
+
CA_E
-
c_\gamma C,
}
\tag{1.8}
$$

where

$$
\boxed{
A_E
=
E^TAE.
}
\tag{1.9}
$$

Let

$$
\boxed{
m
=
\operatorname{tr}C
}
\tag{1.10}
$$

and define the normalized planar covariance

$$
\boxed{
P
=
\frac{C}{m}.
}
\tag{1.11}
$$

Then

$$
P>0,
\qquad
\operatorname{tr}P=1.
$$

Decompose the in-plane affine strain as

$$
\boxed{
A_E
=
a I_2
+
S,
}
\tag{1.12}
$$

where

$$
\boxed{
a
=
\frac12
\operatorname{tr}A_E
=
-\frac12
n\cdot An,
}
\tag{1.13}
$$

and

$$
\boxed{
\operatorname{tr}S=0.
}
\tag{1.14}
$$

The normalized covariance satisfies the exact equation

$$
\boxed{
P'
=
SP
+
PS
-
2(S:P)P.
}
\tag{1.15}
$$

Thus:

$$
\boxed{
\textbf{
normal compression and isotropic planar extension do not change covariance shape.
}
}
\tag{1.16}
$$

Only the in-plane deviatoric strain

$$
S
$$

changes the normalized planar covariance.

This is the first main result.

The second main result identifies the shape space with the open unit disk.

Every positive symmetric

$$
2\times2
$$

matrix of trace one can be written uniquely as

$$
\boxed{
P
=
\frac12
\left[
I_2
+
Z
\right],
}
\tag{1.17}
$$

where

$$
\boxed{
Z
=
\begin{pmatrix}
z_1&z_2\\
z_2&-z_1
\end{pmatrix},
}
\tag{1.18}
$$

and

$$
\boxed{
|z|^2
=
z_1^2+z_2^2
<
1.
}
\tag{1.19}
$$

Likewise write

$$
\boxed{
S
=
\begin{pmatrix}
s_1&s_2\\
s_2&-s_1
\end{pmatrix}.
}
\tag{1.20}
$$

Then (1.15) becomes the exact two-dimensional equation

$$
\boxed{
z'
=
2
\left[
s
-
(s\cdot z)z
\right].
}
\tag{1.21}
$$

Equivalently,

$$
\boxed{
z'
=
2
\left(
I_2-zz^T
\right)s.
}
\tag{1.22}
$$

Because

$$
|z|<1,
$$

the matrix

$$
I_2-zz^T
$$

is positive definite.

Therefore

$$
\boxed{
s
=
\frac12
\left(
I_2-zz^T
\right)^{-1}
z'.
}
\tag{1.23}
$$

This is the central inversion formula of DCRP-41.

It means:

$$
\boxed{
\textbf{
inside the rank-two interior, the in-plane deviatoric affine strain is completely determined by covariance-shape motion.
}
}
\tag{1.24}
$$

The planar shear is not an independent hidden degree of freedom.

The third main result is the hyperbolic shape action.

Define the rank-two anisotropy parameter

$$
\boxed{
\vartheta_2
=
\frac{
4\det C
}{
(\operatorname{tr}C)^2
}.
}
\tag{1.25}
$$

In disk coordinates,

$$
\boxed{
\vartheta_2
=
1-|z|^2.
}
\tag{1.26}
$$

Thus:

-:

  $$
  |z|=0
  $$

  is isotropic covariance in the plane;

-:

  $$
  |z|\uparrow1
  $$

  is rank-one collapse.

Parameterize

$$
\boxed{
z
=
r
\left(
\cos2\theta,
\sin2\theta
\right),
\qquad
0\le r<1.
}
\tag{1.27}
$$

The angle

$$
\theta
$$

is the principal-axis angle of the covariance tensor, modulo the usual

$$
\pi
$$

axis symmetry.

Using (1.23),

$$
\boxed{
|S|_F^2
=
\frac{
(r')^2
}{
2(1-r^2)^2
}
+
2r^2
(\theta')^2.
}
\tag{1.28}
$$

Thus the in-plane deviatoric strain pays exactly for:

1. anisotropy-amplitude motion:

   $$
   r';
   $$

2. in-plane covariance-axis rotation:

   $$
   \theta'.
   $$

This is the precise finite-dimensional phase-action formula.

The singular factor

$$
(1-r^2)^{-2}
$$

shows that changing anisotropy near rank-one collapse is increasingly expensive in the shape metric.

The fourth result is the zero-shape-action rigidity.

Define

$$
\boxed{
\mathcal A_{\rm shape}
=
\int_0^{S_0}
|S(s)|_F^2ds.
}
\tag{1.29}
$$

Then

$$
\boxed{
\mathcal A_{\rm shape}=0
}
\tag{1.30}
$$

if and only if

$$
\boxed{
S(s)\equiv0.
}
\tag{1.31}
$$

Equivalently,

$$
\boxed{
A|_{n^\perp}
=
a(s)I_{n^\perp}
}
\tag{1.32}
$$

pointwise in similarity time.

Thus every exact zero-shape-action rank-two branch has **isotropic planar affine extension at every instant**, not merely on average.

The fifth main result reconstructs the full affine tensor.

From the plane-normal equation:

$$
n'
=
-An
+
(n\cdot An)n,
$$

one gets

$$
\boxed{
P_{n^\perp}An
=
-n'.
}
\tag{1.33}
$$

Because

$$
A
$$

is symmetric and trace free, on the zero-shape-action branch it is uniquely determined by:

- one scalar:

  $$
  a(s);
  $$

- the moving plane normal:

  $$
  n(s).
  $$

The exact formula is

$$
\boxed{
A_{\rm pan}(s)
=
a(s)
\left[
P_{n^\perp}
-
2n\otimes n
\right]
-
\left[
n'\otimes n
+
n\otimes n'
\right].
}
\tag{1.34}
$$

This is the **moving pancake-jet normal form**.

It is the rank-two dual of the rank-one Burgers-jet tensor of DCRP-39.

When

$$
n'=0,
$$

$$
\boxed{
A_{\rm pan}
=
a(s)
\left[
P_{n^\perp}
-
2n\otimes n
\right].
}
\tag{1.35}
$$

In coordinates

$$
n=e_3,
$$

$$
\boxed{
A_{\rm pan}
=
\operatorname{diag}
\left(
a,a,-2a
\right).
}
\tag{1.36}
$$

The periodic pseudo-determinant balance (1.5) becomes

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
a(s)\,ds
=
\frac{
c_\gamma
}{2}.
}
\tag{1.37}
$$

Thus the moving pancake jet has a strictly positive mean planar-extension rate.

The sixth result is a universal normalized reproduction-action lower bound.

From (1.34),

$$
\boxed{
|A_{\rm pan}|_F^2
=
6a(s)^2
+
2|n'(s)|^2.
}
\tag{1.38}
$$

By Jensen,

$$
\boxed{
\int_0^{S_0}
a(s)^2ds
\ge
\frac{
c_\gamma^2
}{4}
S_0.
}
\tag{1.39}
$$

Therefore

$$
\boxed{
\int_0^{S_0}
|A_{\rm pan}|_F^2ds
\ge
\frac32
c_\gamma^2
S_0
+
2
\int_0^{S_0}
|n'|^2ds.
}
\tag{1.40}
$$

DCRP-36 proved for any periodic affine jet:

$$
\boxed{
\int_0^{S_0}
|A'+A|^2ds
=
\int_0^{S_0}
|A'|^2ds
+
\int_0^{S_0}
|A|^2ds.
}
\tag{1.41}
$$

Hence the zero-shape-action rank-two branch satisfies the universal reproduction lower bound

$$
\boxed{
\mathcal A_{\rm rep}
\ge
\frac32
c_\gamma^2
S_0.
}
\tag{1.42}
$$

If the plane rotates,

$$
n'\neq0,
$$

the lower bound is strictly larger.

Thus the exact pancake equality state is not a source-free tensor.

Its annular source dynamics must reproduce a fixed positive amount of normalized pancake strain each period.

This is a finite-dimensional visibility theorem.

It is not yet a raw physical depletion theorem.

The seventh main result classifies every rank-two zero-residual profile into:

$$
\boxed{
\textbf{
positive planar shape action}
}
$$

or

$$
\boxed{
\textbf{
moving pancake-jet equality}.
}
$$

More explicitly:

### shape-dynamic branch

$$
\boxed{
\mathcal A_{\rm shape}>0.
}
\tag{1.43}
$$

The in-plane covariance changes anisotropy and/or principal-axis angle.

This produces a finite-dimensional shape/phase source requirement.

### shape-static branch

$$
\boxed{
\mathcal A_{\rm shape}=0.
}
\tag{1.44}
$$

Then the affine tensor is exactly

$$
A_{\rm pan}
$$

and has the universal reproduction-action gap (1.42).

Therefore no rank-two exact branch remains with both:

- zero covariance residual;
- zero planar-shape activity;
- zero affine reproduction activity.

The eighth result is an external calibration NO-GO.

The moving pancake geometry is not intrinsically impossible in Euler or Navier--Stokes.

Agafontsev--Kuznetsov--Mailybaev exhibit an exact three-dimensional Euler solution combining a shear flow and asymmetric straining flow to model high-vorticity pancake evolution.

Their model includes:

- one compressed transverse direction;
- in-plane stretching directions;
- an arbitrary transverse vorticity profile;
- infinite global energy on:

  $$
  \mathbb R^3;
  $$

- a Navier--Stokes extension in which the profile evolves by a heat equation.

The model's vorticity is more specialized than the present rank-two covariance branch and should not be identified with it.

It shows only that compressed sheet/pancake strain geometries can be exact fluid solutions.

Even more strongly, Enciso--Fernández--Meyer (2026) construct exact Euler vorticities in thin tubular neighborhoods of analytic vortex sheets for time intervals uniform in the sheet thickness.

Thus:

$$
\boxed{
\textbf{
thin sheet-like vorticity geometry itself is not a contradiction.
}
}
\tag{1.45}
$$

The DCRP exclusion must use the specific:

- same-parent DSS return;
- critical tail;
- PFET;
- covariance-shape;
- unforced reproduction;

constraints.

The corrected strongest rank-two state is therefore:

$$
\boxed{
\textbf{
planar potential--shear DSS}
+
\left[
\textbf{
shape/phase action}
\ \vee\
\textbf{
moving pancake jet with reproduction action}
\right].
}
\tag{1.46}
$$

The new exact frontier is

$$
\boxed{
\textbf{
Moving Pancake-Jet /
Planar Potential--Shear Reproduction Rigidity.
}
}
\tag{1.47}
$$

The next PDE question is:

> after the covariance-shape dynamics have been removed or quantified, can the local representation
>
> $$
> V=(\nabla_h\phi,w)
> $$
>
> with:
>
> $$
> \Omega_h=J\nabla_hq
> $$
>
> and the moving pancake affine strain satisfy the strict DSS return without producing:
>
> - normal-vorticity rank lifting;
> - non-affine strain residual;
> - material turnover;
> - additional pressure/PFET work;
> - or a sheet/tail transition defect?

This is now the most concrete rank-two PDE frontier.

---

# 2. Fermi--Walker frame on the vorticity plane

Let

$$
n(s)
$$

be a smooth unit normal.

Choose

$$
E(s)
=
(e_1,e_2)
$$

such that

$$
E^TE=I_2,
\qquad
E^Tn=0.
$$

There is an arbitrary in-plane

$$
SO(2)
$$

gauge.

Choose the no-in-plane-rotation/Fermi gauge:

$$
\boxed{
E^TE'=0.
}
\tag{2.1}
$$

Differentiating

$$
E^Tn=0
$$

gives

$$
\boxed{
E'
=
-
n
n'^T
E.
}
\tag{2.2}
$$

Thus every column of

$$
E'
$$

is parallel to

$$
n.
$$

---

# 3. In-plane covariance equation

Since

$$
B=ECE^T
$$

and

$$
Bn=0,
$$

the Fermi-frame derivative terms vanish:

$$
E'^TBE
=
0,
\qquad
E^TBE'
=
0.
$$

Hence

$$
\boxed{
C'
=
E^TB'E.
}
\tag{3.1}
$$

Using

$$
B'=AB+BA-c_\gamma B,
$$

one obtains

$$
\boxed{
C'
=
A_EC
+
CA_E
-
c_\gamma C.
}
\tag{3.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. Magnitude and shape split

Set

$$
m=\operatorname{tr}C,
\qquad
P=C/m.
$$

Decompose

$$
A_E=aI_2+S,
\qquad
\operatorname{tr}S=0.
$$

Then

$$
\boxed{
\frac{m'}m
=
2a
+
2S:P
-
c_\gamma.
}
\tag{4.1}
$$

The normalized shape satisfies

$$
\boxed{
P'
=
SP
+
PS
-
2(S:P)P.
}
\tag{4.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Shape disk

Every positive

$$
P
$$

with

$$
\operatorname{tr}P=1
$$

has

$$
P=\frac12(I+Z),
$$

where

$$
Z
$$

is symmetric trace free.

Write

$$
Z
=
\begin{pmatrix}
z_1&z_2\\
z_2&-z_1
\end{pmatrix}.
$$

The eigenvalues of

$$
P
$$

are

$$
\boxed{
\frac{
1\pm|z|
}{2}.
}
\tag{5.1}
$$

Therefore

$$
\boxed{
P>0
\Longleftrightarrow
|z|<1.
}
\tag{5.2}
$$

The rank-two covariance shape space is the open unit disk.

---

# 6. Exact disk dynamics

Write

$$
S
=
\begin{pmatrix}
s_1&s_2\\
s_2&-s_1
\end{pmatrix}.
$$

Using

$$
SP+PS
=
S
+
(s\cdot z)I,
$$

and

$$
S:P=s\cdot z,
$$

equation (4.2) gives

$$
\boxed{
\frac12Z'
=
S
-
(s\cdot z)Z.
}
\tag{6.1}
$$

Thus in vector form:

$$
\boxed{
z'
=
2
\left[
s-(s\cdot z)z
\right].
}
\tag{6.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Inversion of the planar shear

Equation (6.2) is

$$
z'
=
2
(I-zz^T)s.
$$

For

$$
|z|<1,
$$

the eigenvalues of

$$
I-zz^T
$$

are

$$
1
$$

and

$$
1-|z|^2.
$$

Hence it is invertible.

Therefore

$$
\boxed{
s
=
\frac12
(I-zz^T)^{-1}
z'.
}
\tag{7.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the rank-two analogue of a phase-locking reconstruction theorem.

---

# 8. Anisotropy parameter

The normalized planar pseudo-determinant is

$$
\vartheta_2
=
4\det P.
$$

Since

$$
\det P
=
\frac{
1-|z|^2
}{4},
$$

$$
\boxed{
\vartheta_2
=
1-|z|^2.
}
\tag{8.1}
$$

Thus the disk boundary is exactly the rank-one collapse boundary.

---

# 9. Log-anisotropy equation

Differentiate

$$
\vartheta_2=1-|z|^2.
$$

Using (6.2),

$$
\boxed{
\vartheta_2'
=
-4
\vartheta_2
(s\cdot z).
}
\tag{9.1}
$$

Hence

$$
\boxed{
\frac d{ds}
\log\vartheta_2
=
-4
s\cdot z.
}
\tag{9.2}
$$

For periodic rank-two covariance:

$$
\boxed{
\int_0^{S_0}
s\cdot z\,ds
=
0.
}
\tag{9.3}
$$

Thus the signed in-plane deviatoric stretching has zero logarithmic-anisotropy average over one return.

---

# 10. Polar shape coordinates

Write

$$
z
=
r
(
\cos2\theta,
\sin2\theta
).
$$

The factor

$$
2
$$

reflects that a symmetric-tensor principal axis is unchanged under

$$
\theta\mapsto\theta+\pi.
$$

Then

$$
\vartheta_2=1-r^2.
$$

The radial direction of

$$
z
$$

is the covariance anisotropy axis.

The angular variable

$$
\theta
$$

is the in-plane covariance principal-axis phase.

---

# 11. NEW THEOREM — Hyperbolic Shape/Phase Action

## Theorem 11.1

The in-plane deviatoric strain satisfies

$$
\boxed{
|S|_F^2
=
\frac{
(r')^2
}{
2(1-r^2)^2
}
+
2r^2
(\theta')^2.
}
\tag{11.1}
$$

### Proof

The inverse

$$
(I-zz^T)^{-1}
$$

acts by:

-:

  $$
  (1-r^2)^{-1}
  $$

  on the radial direction;

-:

  $$
  1
  $$

  on the tangent direction.

Also

$$
z'
=
r'e_r
+
2r\theta'e_\theta.
$$

Thus

$$
|s|^2
=
\frac14
\left[
\frac{
(r')^2
}{
(1-r^2)^2
}
+
4r^2
(\theta')^2
\right].
$$

Since

$$
|S|_F^2=2|s|^2,
$$

the formula follows.

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

# 12. Interpretation of the shape metric

The action contains two positive pieces:

$$
\boxed{
\mathcal A_{\rm amp}
=
\int
\frac{
(r')^2
}{
2(1-r^2)^2
}
ds,
}
\tag{12.1}
$$

and

$$
\boxed{
\mathcal A_{\rm ang}
=
2
\int
r^2
(\theta')^2ds.
}
\tag{12.2}
$$

Thus:

- anisotropy changes near:

  $$
  r=1
  $$

  are strongly amplified;

- principal-axis rotation is visible whenever:

  $$
  r>0.
  $$

At:

$$
r=0,
$$

orientation is correctly unobservable because the covariance is isotropic.

This quotient safety is built into the formula.

---

# 13. Shape-action gap

Define

$$
\boxed{
\mathcal A_{\rm shape}
=
\int_0^{S_0}
|S|_F^2ds.
}
\tag{13.1}
$$

Then:

$$
\boxed{
\mathcal A_{\rm shape}
\ge
\frac12
\int_0^{S_0}
|z'|^2ds.
}
\tag{13.2}
$$

If

$$
\vartheta_2\ge\vartheta_0>0,
$$

then

$$
\mathcal A_{\rm shape}
$$

is quantitatively equivalent to the natural covariance-shape path action on the compact disk

$$
|z|^2\le1-\vartheta_0.
$$

Thus any nonconstant shape orbit has positive finite-dimensional action.

---

# 14. Zero shape-action rigidity

If

$$
\mathcal A_{\rm shape}=0,
$$

then

$$
S=0
$$

almost everywhere.

Smoothness gives

$$
\boxed{
S(s)\equiv0.
}
\tag{14.1}
$$

Hence

$$
\boxed{
A_E=aI_2
}
\tag{14.2}
$$

at every time.

Conversely, if

$$
A_E=aI_2,
$$

then

$$
P'=0
$$

in the Fermi frame.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 15. Reconstruction of the moving pancake jet

Let

$$
P_\perp
=
I-n\otimes n.
$$

On the zero-shape-action branch:

$$
A|_{n^\perp}
=
aP_\perp.
$$

Trace free gives

$$
\boxed{
n\cdot An
=
-2a.
}
\tag{15.1}
$$

The normal equation gives

$$
\boxed{
P_\perp An=-n'.
}
\tag{15.2}
$$

Symmetry then uniquely gives

$$
\boxed{
A
=
a
\left(
P_\perp-2n\otimes n
\right)
-
\left(
n'\otimes n+n\otimes n'
\right).
}
\tag{15.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the moving pancake-jet tensor.

---

# 16. Norm of the pancake jet

The tensors

$$
P_\perp-2n\otimes n
$$

and

$$
n'\otimes n+n\otimes n'
$$

are Frobenius orthogonal.

Also

$$
\boxed{
\left|
P_\perp-2n\otimes n
\right|_F^2
=
6,
}
\tag{16.1}
$$

and

$$
\boxed{
\left|
n'\otimes n+n\otimes n'
\right|_F^2
=
2|n'|^2.
}
\tag{16.2}
$$

Therefore

$$
\boxed{
|A|_F^2
=
6a^2
+
2|n'|^2.
}
\tag{16.3}
$$

---

# 17. Mean pancake compression

DCRP-40 gives

$$
\left\langle
n\cdot An
\right\rangle
=
-c_\gamma.
$$

Since

$$
n\cdot An=-2a,
$$

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
a(s)ds
=
\frac{
c_\gamma
}{2}.
}
\tag{17.1}
$$

Hence the planar extension coefficient has strictly positive mean.

---

# 18. Universal pancake strain-action gap

Jensen gives

$$
\boxed{
\int_0^{S_0}
a^2ds
\ge
\frac{
c_\gamma^2
}{4}
S_0.
}
\tag{18.1}
$$

Using (16.3):

$$
\boxed{
\int_0^{S_0}
|A|_F^2ds
\ge
\frac32
c_\gamma^2S_0
+
2
\int_0^{S_0}
|n'|^2ds.
}
\tag{18.2}
$$

Thus even the most rigid shape-static planar equality state carries a fixed normalized affine-strain action.

---

# 19. Universal reproduction-action gap

DCRP-36 established for periodic

$$
A
$$

the identity

$$
\boxed{
\int_0^{S_0}
|A'+A|^2ds
=
\int_0^{S_0}
|A'|^2ds
+
\int_0^{S_0}
|A|^2ds.
}
\tag{19.1}
$$

Therefore the moving pancake branch satisfies

$$
\boxed{
\mathcal A_{\rm rep}
\ge
\frac32
c_\gamma^2S_0.
}
\tag{19.2}
$$

If the plane normal rotates,

$$
n'\neq0,
$$

the lower bound is larger.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is a normalized source/reproduction witness, not a raw-energy contradiction.

---

# 20. Rank-two master dichotomy

Every exact zero-covariance-residual rank-two profile satisfies:

$$
\boxed{
\mathcal A_{\rm shape}>0
}
$$

or

$$
\boxed{
A=A_{\rm pan}.
}
$$

Thus:

$$
\boxed{
\textbf{
rank-two zero-residual}
\Longrightarrow
\textbf{
shape/phase dynamics}
\ \vee\
\textbf{
moving pancake jet}.
}
\tag{20.1}
$$

On the second branch:

$$
\boxed{
\mathcal A_{\rm rep}
\ge
\frac32
c_\gamma^2S_0.
}
\tag{20.2}
$$

No completely source-free planar equality remains.

---

# 21. Relation to the conformal Floquet theorem

DCRP-40 described the rank-two monodromy on the covariance plane as conformal in the covariance metric.

DCRP-41 gives the continuous-time differential version.

The in-plane deviatoric strain:

$$
S
$$

is exactly the generator of covariance-shape deformation.

If

$$
S=0,
$$

the covariance shape is parallel transported in the Fermi frame and the only monodromy left comes from:

- isotropic planar expansion;
- geometric plane holonomy.

Thus the conformal Floquet equality is the integrated form of the moving pancake-jet branch.

---

# 22. Relation to the planar potential--shear field

DCRP-40 showed that for fixed plane normal:

$$
V
=
(\nabla_h\phi,w),
$$

with

$$
q=w-\partial_3\phi,
$$

and

$$
\Omega_h
=
(\partial_2q,-\partial_1q).
$$

DCRP-41 does not yet solve the scalar dynamics of:

$$
q.
$$

It shows that the affine strain seen by the rank-two covariance has only two possibilities:

- explicit finite-dimensional shape/shear action;
- canonical moving pancake strain.

Thus the infinite-dimensional problem has been pushed into the potential--shear carrier rather than the covariance geometry.

---

# 23. External exact Euler pancake calibration

Agafontsev--Kuznetsov--Mailybaev construct an exact Euler solution modeling pancake high-vorticity regions as a superposition of:

- a shear flow;
- an asymmetric irrotational straining flow.

The solution has one compressed direction and growing vorticity and can exhibit arbitrary power-law relations between vorticity amplitude and pancake thickness.

It has infinite energy on:

$$
\mathbb R^3.
$$

The paper also gives a Navier--Stokes extension in which the transverse profile obeys a heat equation.

This shows:

$$
\boxed{
\textbf{
pancake compression + shear + strain}
}
$$

is an exact fluid mechanism.

The DCRP moving pancake jet is not identified with that model.

The external model is used as a NO-GO against excluding the local geometry by appearance alone.

---

# 24. Current vortex-sheet calibration

Enciso--Fernández--Meyer (2026) prove that analytic three-dimensional vortex sheets can be desingularized into exact Euler vorticities supported in tubular neighborhoods of thickness

$$
O(\varepsilon),
$$

on a time interval bounded below independently of

$$
\varepsilon.
$$

The constructed vorticities are organized by foliations of almost parallel surfaces and divergence-free fields tangent to those surfaces.

Therefore:

$$
\boxed{
\textbf{
thin, approximately planar/tangent vorticity organization is compatible with exact Euler dynamics.
}
}
\tag{24.1}
$$

Again, this is calibration rather than identification with the DSS Type-II branch.

---

# 25. Why sheet geometry is not enough

The strict DCRP branch has extra constraints absent from generic pancake/sheet models:

- same-parent DSS recurrence;
- exponent window:

  $$
  2/5<\gamma<1/2;
  $$

- raw-energy vanishing;
- mandatory DCRP-31 inward PFET;
- periodic covariance;
- finite-annulus strain reproduction;
- zero or controlled transition defects.

Thus external exact sheet/pancake solutions do not close or realize the DCRP branch automatically.

---

# 26. Shape-action branch

If

$$
\mathcal A_{\rm shape}>0,
$$

then at least one of:

$$
r'
$$

or

$$
r\theta'
$$

is nonzero.

Hence the planar covariance must continually:

- change its eigenvalue anisotropy;
- or rotate its principal axis relative to the Fermi plane.

The exact source of that motion is the in-plane deviatoric annular strain

$$
S.
$$

Therefore the rank-two phase problem has been reduced to a positive finite-dimensional source action.

No additional abstract phase variable is required.

---

# 27. Near-rank-one cost

As

$$
r\uparrow1,
$$

$$
\vartheta_2=1-r^2\downarrow0.
$$

The radial action contains:

$$
\frac{
(r')^2
}{
(1-r^2)^2
}.
$$

Thus a trajectory which repeatedly approaches rank one and returns to the rank-two interior pays a large shape-metric action unless the approach/recovery rate becomes correspondingly slow.

This creates a quantitative bridge between:

- DCRP-39 rank-one collapse;
- DCRP-41 rank-two shape dynamics.

A full transition lower bound requires a specified distance excursion and is left for later use.

---

# 28. Moving-plane cost

On the shape-static branch, all in-plane shear vanishes, but plane rotation remains through

$$
n'(s).
$$

The affine tensor contains

$$
-
(n'\otimes n+n\otimes n').
$$

Thus moving-plane recurrence is not free at the affine-jet reproduction level.

The strain-action contains the explicit term:

$$
\boxed{
2
\int
|n'|^2ds.
}
\tag{28.1}
$$

This is the rank-two counterpart of the axis-rotation term in the rank-one Burgers jet.

---

# 29. What is still not proved

DCRP-41 does not prove that positive normalized:

$$
\mathcal A_{\rm shape}
$$

or

$$
\mathcal A_{\rm rep}
$$

is non-summable in raw physical variables.

The critical-scaling NO-GOs from earlier rounds still apply.

The new quantities are equality-manifold/source classifiers.

A global contradiction requires a same-parent return-depletion or a PDE Liouville theorem for the final moving pancake state.

---

# 30. Corrected final rank-two state

The DCRP-40 survivor

$$
\text{planar conformal Floquet vorticity}
$$

is now refined to

$$
\boxed{
\textbf{
planar potential--shear DSS}
+
\left[
\textbf{
positive covariance shape/phase action}
\ \vee\
\textbf{
moving pancake jet}
\right].
}
\tag{30.1}
$$

The moving pancake jet is completely described by

$$
\boxed{
a(s)
}
$$

and

$$
\boxed{
n(s)\in S^2.
}
$$

This is a three-dimensional finite parameter fiber coupled to the planar potential--shear PDE.

---

# 31. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Moving Pancake-Jet /
Planar Potential--Shear Reproduction Rigidity.
}
}
$$

A useful theorem should take the zero-shape-action branch

$$
A=A_{\rm pan}
$$

and the local representation

$$
V=(\nabla_h\phi,w)
$$

and derive a scalar/differential-form evolution for

$$
q=w-\partial_n\phi.
$$

The desired classification is:

$$
\boxed{
\text{normal-vorticity rank lifting}
\ \vee\
\text{non-affine strain residual}
\ \vee\
\text{material/sheet turnover}
\ \vee\
\text{pressure/PFET source}
\ \vee\
\text{exact pancake eigenmode}.
}
$$

The last branch should then be compared with:

- exact Euler pancake solutions;
- vortex-sheet-type Euler solutions;
- the strict DSS tail and same-parent finite-energy ancestry.

This is now the principal low-rank PDE frontier.

---

# 32. End state

The normalized planar covariance shape obeys the exact disk equation

$$
\boxed{
z'
=
2
\left(
I-zz^T
\right)s.
}
$$

Therefore

$$
\boxed{
s
=
\frac12
\left(
I-zz^T
\right)^{-1}z'.
}
$$

The in-plane deviatoric strain is exactly the covariance-shape velocity.

In polar tensor coordinates:

$$
\boxed{
|S|_F^2
=
\frac{
(r')^2
}{
2(1-r^2)^2
}
+
2r^2
(\theta')^2.
}
$$

Thus rank-two covariance deformation has a positive hyperbolic amplitude/phase action.

If that action vanishes,

$$
\boxed{
A
=
a
\left(
P_{n^\perp}
-
2n\otimes n
\right)
-
\left(
n'\otimes n+n\otimes n'
\right).
}
$$

DSS periodicity forces

$$
\boxed{
\langle a\rangle
=
\frac{
2-3\gamma
}{2}.
}
$$

Therefore the zero-shape-action branch is a moving pancake jet with universal normalized strain/reproduction activity.

The rank-two problem has now been reduced from a generic planar Floquet covariance to:

$$
\boxed{
\textbf{
a planar potential--shear PDE driven by a three-parameter moving pancake strain.
}
}
$$

The next frontier is:

$$
\boxed{
\textbf{
Moving Pancake-Jet /
Planar Potential--Shear Reproduction Rigidity.
}
}
$$