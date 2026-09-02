# NS-DCRP-54 — Finite-Annulus Dual Moments, Toroidal Strain Supplier, and Return-Vorticity Matching Rigidity

- date: 2026-08-17
- status: research proof checkpoint / finite matching-annulus moment reduction
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. turn the DCRP-53 finite matching annulus into a quantitative vorticity-moment ledger;
  2. derive the exact Biot--Savart representer of the canonical pancake strain coefficient;
  3. compute its exact $L^2$ norm on a centered spherical annulus;
  4. prove an annular enstrophy lower bound for any vorticity field supplying the Gaussian-core pancake strain;
  5. show that thin annular suppliers become more expensive in enstrophy;
  6. encode localization of the Gaussian shear as a Stokes/circulation return-vorticity alternative;
  7. separate return-vorticity flux from continued circulation export, without assuming the return occurs in the first strain-supplier shell;
  8. formulate a bounded linear return moment and prove a two-moment Gram-matrix lower bound;
  9. prove exact orthogonality of the centered spherical strain-supplier mode and the constant mean-return mode;
  10. derive a Pythagorean matching-enstrophy lower bound;
  11. identify the zero-excess matching vorticity as a two-mode moment minimizer;
  12. prove that the canonical strain representer is itself an axisymmetric toroidal divergence-free vorticity mode away from the origin;
  13. record the important NO-GO that dual moments are kinematically compatible and therefore do not by themselves close the branch;
  14. identify the next frontier as dynamical invariance/reproduction of the two-mode annular equality manifold together with inward PFET.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1;
  - P. E. Hamlington, J. Schumacher, W. J. A. Dahm, *Local and Nonlocal Strain Rate Fields and Vorticity Alignment in Turbulent Flows*, arXiv:0801.1248;
  - A. Castro, D. Córdoba, F. Gancedo, *A naive parametrization for the vortex-sheet problem*, arXiv:0810.0731.
- internal dependencies:
  - DCRP-31 inward finite-radius PFET matching;
  - DCRP-35/36 finite-annulus affine-strain supplier/reproduction;
  - DCRP-53 local Batchelor--Gaussian core and finite matching radius.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-53 reduced the strongest coherent zero-excess viscous branch to

$$
\boxed{
\textbf{
local Batchelor--Gaussian sheet core}
}
$$

coupled to

$$
\boxed{
\textbf{
a finite normalized matching region}.
}
$$

The core cannot generate its own canonical diagonal pancake strain, and the global Gaussian shear/affine field is incompatible with the strict sublinear Type-II kinetic-energy tail.

DCRP-54 quantifies what the matching region must carry.

Let

$$
\boxed{
T
=
\operatorname{diag}(1,1,-2),
\qquad
|T|_F^2=6.
}
\tag{1.1}
$$

The core requires the strain

$$
\boxed{
A_{\rm pan}
=
aT.
}
\tag{1.2}
$$

For a centered spherical annulus

$$
\boxed{
\mathcal A
=
\left\{
R_-<|y|<R_+
\right\},
}
\tag{1.3}
$$

the contribution of annular vorticity

$$
\omega_{\mathcal A}
$$

to the pancake coefficient is the bounded linear moment

$$
\boxed{
a_{\mathcal A}
=
\int_{\mathcal A}
K_a(y)\cdot
\omega_{\mathcal A}(y)\,dy,
}
\tag{1.4}
$$

where the exact representer is

$$
\boxed{
K_a(y)
=
\frac1{
8\pi|y|^3
}
\left[
(T\widehat y)\times\widehat y
\right].
}
\tag{1.5}
$$

For

$$
T=\operatorname{diag}(1,1,-2),
$$

this becomes

$$
\boxed{
K_a(y)
=
\frac{
3
}{
8\pi
}
\frac{
y_3(y_2,-y_1,0)
}{
|y|^5
}.
}
\tag{1.6}
$$

This is the first central object of DCRP-54.

Its exact annular norm is

$$
\boxed{
\|K_a\|_{L^2(\mathcal A)}^2
=
\frac1{
40\pi
}
\left(
R_-^{-3}
-
R_+^{-3}
\right).
}
\tag{1.7}
$$

Therefore every annular vorticity field contributing the strain coefficient

$$
a_{\mathcal A}
$$

satisfies

$$
\boxed{
\int_{\mathcal A}
|\omega_{\mathcal A}|^2dy
\ge
\frac{
40\pi
a_{\mathcal A}^2
}{
R_-^{-3}-R_+^{-3}
}.
}
\tag{1.8}
$$

For a dyadic annulus

$$
R<|y|<2R,
$$

$$
\boxed{
\int_{\mathcal A}
|\omega_{\mathcal A}|^2dy
\ge
\frac{
320\pi
}{7}
a_{\mathcal A}^2
R^3.
}
\tag{1.9}
$$

For a thin shell

$$
R<|y|<R+w,
\qquad
w\ll R,
$$

$$
\boxed{
\int_{\mathcal A}
|\omega_{\mathcal A}|^2dy
\gtrsim
\frac{
40\pi
}{3}
a_{\mathcal A}^2
\frac{
R^4
}{
w
}.
}
\tag{1.10}
$$

Thus a fixed core strain cannot be supplied by an arbitrarily weak annular vorticity reservoir.

Making the supplier shell thinner increases its $L^2$ vorticity cost.

The second central result applies the Gaussian strain-action rigidity from DCRP-53.

If one finite annulus carries the full canonical strain demand during a period,

$$
a_{\mathcal A}(s)=a(s),
$$

then on a dyadic shell

$$
\boxed{
\int_0^{S_0}
\int_{\mathcal A}
|\omega|^2
dyds
\ge
\frac{
320\pi
}{7}
R^3
\int_0^{S_0}
a(s)^2ds.
}
\tag{1.11}
$$

Since

$$
\boxed{
\int_0^{S_0}
a(s)^2ds
\ge
\frac{
(2-3\gamma)^2
}{4}
S_0,
}
\tag{1.12}
$$

one obtains

$$
\boxed{
\int_0^{S_0}
\int_{\mathcal A}
|\omega|^2
dyds
\ge
\frac{
80\pi
}{7}
(2-3\gamma)^2
S_0
R^3.
}
\tag{1.13}
$$

Every nonconstant Gaussian width waveform increases this minimum through the DCRP-53 breathing penalties.

Thus the annular harmonic strain supplier carries a quantitative vorticity reservoir.

The third central result identifies the angular character of the supplier.

In cylindrical coordinates

$$
(\rho,\phi,z),
$$

$$
\boxed{
K_a
=
-
\frac{
3
}{
8\pi
}
\frac{
\rho z
}{
(\rho^2+z^2)^{5/2}
}
e_\phi.
}
\tag{1.14}
$$

It is:

- axisymmetric;
- azimuthal/toroidal;
- odd in the sheet-normal variable;
- zero-mean on every centered sphere.

Moreover

$$
\boxed{
\nabla\cdot K_a=0
}
\tag{1.15}
$$

away from the origin.

Hence the minimum-norm strain representer is itself a kinematically admissible divergence-free annular vorticity mode.

The fourth central result treats shear localization.

Let

$$
C_{\rm in}
\subset
C_{\rm out}
$$

be nested loops in a coherent cross-sectional surface, with spanning annular surface

$$
S_{\rm match}.
$$

Stokes gives the exact identity

$$
\boxed{
\Gamma_{\rm out}
-
\Gamma_{\rm in}
=
\int_{S_{\rm match}}
\omega\cdot n_S\,dA.
}
\tag{1.16}
$$

Thus a nonzero inner Gaussian-core shear circulation has only two possibilities across the matching region:

$$
\boxed{
\textbf{
return-vorticity flux}
}
$$

or

$$
\boxed{
\textbf{
circulation export to the outer flow}.
}
\tag{1.17}
$$

DCRP-54 does **not** assume that the first strain-supplier annulus must already cancel all core circulation.

The return may occur in a later finite matching layer.

If the outer flow remains in the same coherent one-dimensional shear-jump geometry, DCRP-53's $R^3$ kinetic-energy lower bound prevents that geometry from persisting to normalized infinity under the strict

$$
R^\kappa,
\qquad
\kappa<1
$$

tail.

If the geometry changes before a return, that change is a localization / plane / rank / multilayer transition.

Thus, on the zero-transition coherent branch, the shear circulation must eventually enter a finite return-vorticity layer.

The fifth central result packages the two annular duties into a Hilbert-space moment theorem.

Let

$$
H
=
L^2(
\mathcal A;
\mathbb R^3
).
$$

Define two bounded linear functionals:

$$
\boxed{
L_S(\omega)
=
\langle K_a,\omega\rangle_H
}
\tag{1.18}
$$

and a declared averaged return-vorticity moment

$$
\boxed{
L_R(\omega)
=
\langle G_R,\omega\rangle_H.
}
\tag{1.19}
$$

If the Riesz representers

$$
K_a,
\qquad
G_R
$$

are linearly independent, define the Gram matrix

$$
\boxed{
\mathbb G
=
\begin{pmatrix}
\langle K_a,K_a\rangle
&
\langle K_a,G_R\rangle
\\
\langle G_R,K_a\rangle
&
\langle G_R,G_R\rangle
\end{pmatrix}.
}
\tag{1.20}
$$

For constraints

$$
\boxed{
L_S(\omega)=a,
\qquad
L_R(\omega)=J,
}
\tag{1.21}
$$

one has

$$
\boxed{
\|\omega\|_H^2
\ge
\begin{pmatrix}
a & J
\end{pmatrix}
\mathbb G^{-1}
\binom{
a
}{
J
}.
}
\tag{1.22}
$$

This is the exact minimum-norm dual-moment cost.

The sixth central result specializes to a centered spherical shell.

Take a fixed unit return direction

$$
e
$$

and define the annular mean return component

$$
\boxed{
J_e
=
\frac1{
|\mathcal A|
}
\int_{\mathcal A}
\omega\cdot e\,dy.
}
\tag{1.23}
$$

Its Riesz representer is

$$
\boxed{
G_e
=
e/|\mathcal A|.
}
\tag{1.24}
$$

The Calderón--Zygmund strain kernel has zero spherical mean.

Therefore

$$
\boxed{
\langle K_a,G_e\rangle=0.
}
\tag{1.25}
$$

Hence the two duties are $L^2$-orthogonal.

The Pythagorean lower bound is

$$
\boxed{
\|\omega\|_{L^2(\mathcal A)}^2
\ge
\frac{
40\pi a^2
}{
R_-^{-3}-R_+^{-3}
}
+
|\mathcal A|
J_e^2.
}
\tag{1.26}
$$

Equivalently, if

$$
\boxed{
F_e
=
\int_{\mathcal A}
\omega\cdot e\,dy,
}
\tag{1.27}
$$

then

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
40\pi a^2
}{
R_-^{-3}-R_+^{-3}
}
+
\frac{
F_e^2
}{
|\mathcal A|
}.
}
\tag{1.28}
$$

For a dyadic shell

$$
R<|y|<2R,
$$

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
320\pi
}{7}
a^2R^3
+
\frac{
3
}{
28\pi
}
F_e^2
R^{-3}.
}
\tag{1.29}
$$

If the return datum is expressed as an annular mean

$$
J_e,
$$

both moment costs scale as

$$
R^3
$$

for fixed normalized amplitudes.

The seventh central result is the exact two-mode Pythagorean decomposition.

Define

$$
\boxed{
\omega_{\min}
=
\frac{
a
}{
\|K_a\|_2^2
}
K_a
+
J_e e.
}
\tag{1.30}
$$

Then every

$$
\omega
$$

satisfying

$$
L_S(\omega)=a
$$

and

$$
L_R(\omega)=J_e
$$

has

$$
\boxed{
\omega
=
\omega_{\min}
+
\omega_\perp,
}
\tag{1.31}
$$

where

$$
\boxed{
\langle\omega_\perp,K_a\rangle=0,
\qquad
\int_{\mathcal A}
\omega_\perp\cdot e\,dy=0.
}
\tag{1.32}
$$

Therefore

$$
\boxed{
\|\omega\|_2^2
=
\frac{
a^2
}{
\|K_a\|_2^2
}
+
|\mathcal A|J_e^2
+
\|\omega_\perp\|_2^2.
}
\tag{1.33}
$$

Define the matching-moment excess

$$
\boxed{
\mathfrak X_{\rm match}
=
\|\omega_\perp\|_2^2.
}
\tag{1.34}
$$

This gives an exact nonnegative annular coordinate.

The zero-excess matching state is therefore finite-dimensional:

$$
\boxed{
\omega_{\rm match}
\in
\operatorname{span}
\left\{
K_a,e
\right\}.
}
\tag{1.35}
$$

The eighth central conclusion is a necessary NO-GO against overclaiming.

The two moment duties are independent, but they are **kinematically compatible**.

Both:

$$
K_a
$$

and the constant vector mode

$$
e
$$

are divergence free in the annular interior.

Therefore

$$
\boxed{
\textbf{
dual-moment positivity does not itself rule out an unforced matching annulus.
}
}
\tag{1.36}
$$

The matching region may, at the purely kinematic moment level, carry both jobs simultaneously.

The actual remaining question is dynamical:

> is the two-mode zero-excess annular moment manifold invariant/reproducible under the unforced Navier--Stokes return dynamics while also supplying the DCRP-31 inward PFET and matching smoothly to the Gaussian core and outer recurrent flow?

That is the new frontier.

The ninth central conclusion is that the final coherent equality architecture is now

$$
\boxed{
\textbf{
Gaussian core}
}
\longleftrightarrow
\boxed{
\textbf{
finite annular two-moment supplier}
}
\longleftrightarrow
\boxed{
\textbf{
outer recurrent flow}.
}
\tag{1.37}
$$

On the zero-excess ideal branch the annular vorticity must lie in a two-mode moment span:

- toroidal quadrupolar strain supplier;
- return-vorticity/circulation mode.

The DCRP-31 inward PFET is an additional nonlinear matching duty.

The next frontier is therefore

$$
\boxed{
\textbf{
Two-Mode Matching Manifold /
Navier--Stokes Reproduction and PFET Compatibility.
}
}
\tag{1.38}
$$

---

# 2. Exact strain kernel

For a divergence-free velocity field

$$
U,
$$

with vorticity

$$
\Omega=\nabla\times U,
$$

the strain tensor is

$$
\boxed{
S_{ij}(x)
=
\operatorname{p.v.}
\int_{\mathbb R^3}
K_{ijm}(z)
\Omega_m(x-z)dz,
}
\tag{2.1}
$$

with

$$
\boxed{
K_{ijm}(z)
=
\frac{
3
}{
8\pi|z|^5
}
\left(
z_j\varepsilon_{ikm}z_k
+
z_i\varepsilon_{jkm}z_k
\right).
}
\tag{2.2}
$$

Equivalently,

$$
\boxed{
S(x)
=
\frac{
3
}{
8\pi
}
\operatorname{p.v.}
\int
\frac{
(\widehat z\times\Omega)\otimes\widehat z
+
\widehat z\otimes(\widehat z\times\Omega)
}{
|z|^3
}
dz.
}
\tag{2.3}
$$

The kernel is homogeneous of degree

$$
-3
$$

and has zero spherical average.

This is the external primary strain representation used in DCRP-54.

---

# 3. Pancake coefficient as a linear moment

Let

$$
T=\operatorname{diag}(1,1,-2).
$$

For a pure pancake tensor

$$
A=aT,
$$

$$
\boxed{
a
=
\frac{
T:A
}{
|T|_F^2
}
=
\frac16
T:A.
}
\tag{3.1}
$$

Contracting (2.3) with

$$
T
$$

gives

$$
\boxed{
a_{\mathcal A}
=
\int_{\mathcal A}
K_a(y)\cdot
\omega(y)dy,
}
\tag{3.2}
$$

where

$$
\boxed{
K_a(y)
=
\frac1{
8\pi|y|^3
}
[
(T\widehat y)\times\widehat y
].
}
\tag{3.3}
$$

Status:

$$
\boxed{
\textbf{PROVED FROM THE EXACT STRAIN KERNEL}.
}
$$

---

# 4. Explicit toroidal form

For

$$
\widehat y
=
(n_1,n_2,n_3),
$$

$$
T\widehat y
=
(n_1,n_2,-2n_3).
$$

Thus

$$
\boxed{
(T\widehat y)\times\widehat y
=
3n_3
(n_2,-n_1,0).
}
\tag{4.1}
$$

Therefore

$$
\boxed{
K_a(y)
=
\frac{
3
}{
8\pi
}
\frac{
y_3(y_2,-y_1,0)
}{
|y|^5
}.
}
\tag{4.2}
$$

In cylindrical coordinates:

$$
\boxed{
K_a
=
-
\frac{
3
}{
8\pi
}
\frac{
\rho z
}{
(\rho^2+z^2)^{5/2}
}
e_\phi.
}
\tag{4.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Divergence-free supplier mode

An axisymmetric vector field of the form

$$
F(\rho,z)e_\phi
$$

has zero divergence.

Therefore

$$
\boxed{
\nabla\cdot K_a=0
}
\tag{5.1}
$$

on every annulus away from the origin.

The canonical minimum strain-supplier representer is therefore not excluded by the vorticity divergence constraint.

This fact is important for the final NO-GO audit.

---

# 6. Angular norm

The angular factor satisfies

$$
\boxed{
\left|
(Tn)\times n
\right|^2
=
9n_3^2
(
n_1^2+n_2^2
).
}
\tag{6.1}
$$

Using

$$
\langle n_3^2\rangle_{S^2}=1/3
$$

and

$$
\langle n_3^4\rangle_{S^2}=1/5,
$$

$$
\boxed{
\int_{S^2}
|
(Tn)\times n
|^2dS
=
\frac{
24\pi
}{5}.
}
\tag{6.2}
$$

---

# 7. NEW THEOREM — Exact Annular Strain-Representer Norm

## Theorem 7.1

For

$$
\mathcal A
=
\{R_-<|y|<R_+\},
$$

$$
\boxed{
\|K_a\|_{L^2(\mathcal A)}^2
=
\frac1{
40\pi
}
\left(
R_-^{-3}
-
R_+^{-3}
\right).
}
\tag{7.1}
$$

### Proof

Use:

$$
|K_a|^2
=
\frac1{
64\pi^2
}
|y|^{-6}
|
(Tn)\times n
|^2.
$$

The angular integral is (6.2).

The radial integral is

$$
\int_{R_-}^{R_+}
r^{-4}dr
=
\frac13
(
R_-^{-3}
-
R_+^{-3}
).
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

# 8. NEW THEOREM — Annular Strain-Supplier Enstrophy Gap

By Cauchy--Schwarz,

$$
|a_{\mathcal A}|
\le
\|K_a\|_2
\|\omega\|_2.
$$

Therefore

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
40\pi
a_{\mathcal A}^2
}{
R_-^{-3}-R_+^{-3}
}.
}
\tag{8.1}
$$

For

$$
R_+=2R_-=2R,
$$

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
320\pi
}{7}
a_{\mathcal A}^2
R^3.
}
\tag{8.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. Thin-shell asymptotic

Let

$$
R_-=R,
\qquad
R_+=R+w,
\qquad
w/R\to0.
$$

Then

$$
R^{-3}
-
(R+w)^{-3}
=
3wR^{-4}
+
O(
w^2R^{-5}
).
$$

Therefore

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
40\pi
}{3}
a^2
\frac{
R^4
}{
w
}
[
1+o(1)
].
}
\tag{9.1}
$$

Thus annular strain supply cannot be concentrated into a vanishing radial width at bounded $L^2$ cost.

---

# 10. Periodic Gaussian supplier cost

Suppose the same annulus carries the full Gaussian strain waveform

$$
a(s).
$$

Integrating (8.2),

$$
\boxed{
\int_0^{S_0}
\|\omega_{\mathcal A}(s)\|_2^2ds
\ge
\frac{
320\pi
}{7}
R^3
\int_0^{S_0}
a(s)^2ds.
}
\tag{10.1}
$$

DCRP-53 gives

$$
\boxed{
\int
a^2
=
S_0\bar a^2
+
\frac14
\int
\left[
\delta^{-1}
-
\frac32(1-2\gamma)
\right]^2
+
\frac1{16}
\int
[
(\log\delta)'
]^2.
}
\tag{10.2}
$$

Therefore every nonconstant Gaussian width waveform increases the minimum annular vorticity reservoir.

---

# 11. Minimum constant-Gaussian supplier cost

For the DCRP-53 minimum equality,

$$
\boxed{
a(s)
\equiv
a_0
=
\frac{
2-3\gamma
}{2}.
}
\tag{11.1}
$$

Then on a dyadic shell,

$$
\boxed{
\int_0^{S_0}
\|\omega_{\mathcal A}\|_2^2ds
\ge
\frac{
80\pi
}{7}
(2-3\gamma)^2
S_0
R^3.
}
\tag{11.2}
$$

This is the minimum period-integrated annular strain-supplier enstrophy.

---

# 12. Return-vorticity identity from Stokes

Let

$$
C_{\rm in},
\qquad
C_{\rm out}
$$

be homologous loops in a cross-sectional sheet of the matching region.

Let

$$
S_{\rm match}
$$

be the annular surface between them.

Then

$$
\boxed{
\oint_{C_{\rm out}}
V\cdot dl
-
\oint_{C_{\rm in}}
V\cdot dl
=
\int_{S_{\rm match}}
\omega\cdot n_SdA.
}
\tag{12.1}
$$

Define

$$
\boxed{
\Gamma_{\rm in}
=
\oint_{C_{\rm in}}
V\cdot dl,
\qquad
\Gamma_{\rm out}
=
\oint_{C_{\rm out}}
V\cdot dl.
}
\tag{12.2}
$$

Then:

$$
\boxed{
J_{\rm ret}
=
\Gamma_{\rm out}
-
\Gamma_{\rm in}
}
\tag{12.3}
$$

is exactly the return-vorticity flux through the cross-sectional matching surface.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. Return versus circulation export

If the Gaussian core carries a nonzero coherent inner circulation

$$
\Gamma_{\rm in},
$$

the matching system may:

1. generate return flux so that

   $$
   |\Gamma_{\rm out}|<|\Gamma_{\rm in}|;
   $$

2. transmit the circulation outward.

Therefore DCRP-54 records the exact branch

$$
\boxed{
\text{return-vorticity flux}
\ \vee\
\text{circulation export}.
}
\tag{13.1}
$$

No return is forced in the first strain-supplier shell without an additional localization hypothesis.

---

# 14. Why coherent circulation export cannot remain global

DCRP-53 proved that a global one-dimensional shear with nonzero velocity jump has kinetic energy at least

$$
cM^2R^3.
$$

Therefore if the exported circulation remains encoded as the same coherent one-dimensional shear jump to arbitrarily large normalized radius, it contradicts

$$
E(B_R)
\lesssim
R^\kappa,
\qquad
\kappa<1.
$$

Hence on a zero-transition coherent shear branch, the circulation must eventually return at finite radius.

If it does not remain coherent, the loss is one of:

- tangential localization;
- sheet turning/folding;
- plane transition;
- rank lifting;
- multilayer formation.

This is the correct global return statement.

---

# 15. Averaged return moment

To combine return with the volume $L^2$ strain ledger, introduce a bounded averaged return functional

$$
\boxed{
L_R(\omega)
=
\int_{\mathcal A}
G_R(y)\cdot\omega(y)dy.
}
\tag{15.1}
$$

The test field

$$
G_R
$$

is chosen from the declared matching geometry so that

$$
L_R
$$

represents a spatially averaged Stokes-return flux.

Different cross-sectional implementations give different

$$
G_R.
$$

The Gram theorem below is independent of that choice.

---

# 16. NEW THEOREM — Dual-Moment Gram Bound

## Theorem 16.1

Let

$$
g_1=K_a,
\qquad
g_2=G_R
$$

be linearly independent in

$$
H=L^2(\mathcal A;\mathbb R^3).
$$

Let

$$
\mathbb G_{ij}
=
\langle g_i,g_j\rangle_H.
$$

If

$$
\boxed{
\langle g_1,\omega\rangle=a,
\qquad
\langle g_2,\omega\rangle=J,
}
\tag{16.1}
$$

then

$$
\boxed{
\|\omega\|_H^2
\ge
c^T
\mathbb G^{-1}
c,
\qquad
c=
\binom aJ.
}
\tag{16.2}
$$

### Proof

The minimum-norm solution to the two linear constraints lies in

$$
\operatorname{span}
\{g_1,g_2\}.
$$

Writing

$$
\omega_{\min}
=
\lambda_1g_1+\lambda_2g_2,
$$

the constraints give

$$
\mathbb G\lambda=c.
$$

Hence

$$
\lambda=\mathbb G^{-1}c
$$

and

$$
\|\omega_{\min}\|^2
=
c^T\mathbb G^{-1}c.
$$

Orthogonal projection gives the lower bound.

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

# 17. Centered mean-return mode

Take a unit direction

$$
e
$$

and define

$$
\boxed{
J_e
=
\fint_{\mathcal A}
\omega\cdot e\,dy.
}
\tag{17.1}
$$

Then

$$
\boxed{
G_e
=
e/|\mathcal A|.
}
\tag{17.2}
$$

The strain kernel has zero spherical average, so

$$
\boxed{
\int_{\mathcal A}
K_a(y)dy=0.
}
\tag{17.3}
$$

Therefore

$$
\boxed{
\langle K_a,G_e\rangle=0.
}
\tag{17.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. NEW THEOREM — Orthogonal Two-Duty Matching Bound

## Theorem 18.1

If

$$
\boxed{
L_S(\omega)=a,
\qquad
\fint_{\mathcal A}
\omega\cdot e=J_e,
}
\tag{18.1}
$$

then

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
40\pi a^2
}{
R_-^{-3}-R_+^{-3}
}
+
|\mathcal A|J_e^2.
}
\tag{18.2}
$$

Equivalently, for

$$
F_e
=
\int_{\mathcal A}
\omega\cdot e,
$$

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
40\pi a^2
}{
R_-^{-3}-R_+^{-3}
}
+
\frac{
F_e^2
}{
|\mathcal A|
}.
}
\tag{18.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The strain and mean-return duties are independent $L^2$ moment costs.

---

# 19. Dyadic-shell formula

For

$$
R<|y|<2R,
$$

$$
|\mathcal A|
=
\frac{
28\pi
}{3}
R^3.
$$

Therefore

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
320\pi
}{7}
a^2R^3
+
\frac{
28\pi
}{3}
J_e^2R^3.
}
\tag{19.1}
$$

Or, using total mean-return moment

$$
F_e,
$$

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
320\pi
}{7}
a^2R^3
+
\frac{
3
}{
28\pi
}
F_e^2R^{-3}.
}
\tag{19.2}
$$

---

# 20. Pythagorean decomposition

Define

$$
\boxed{
\omega_{\min}
=
\frac{
a
}{
\|K_a\|_2^2
}
K_a
+
J_e e.
}
\tag{20.1}
$$

Then

$$
\boxed{
\omega
=
\omega_{\min}
+
\omega_\perp,
}
\tag{20.2}
$$

with

$$
\boxed{
\langle\omega_\perp,K_a\rangle=0,
\qquad
\int_{\mathcal A}
\omega_\perp\cdot e=0.
}
\tag{20.3}
$$

Thus

$$
\boxed{
\|\omega\|_2^2
=
\frac{
a^2
}{
\|K_a\|_2^2
}
+
|\mathcal A|J_e^2
+
\|\omega_\perp\|_2^2.
}
\tag{20.4}
$$

---

# 21. Matching-moment excess

Define

$$
\boxed{
\mathfrak X_{\rm match}
=
\|\omega_\perp\|_2^2.
}
\tag{21.1}
$$

Then

$$
\boxed{
\mathfrak X_{\rm match}\ge0.
}
\tag{21.2}
$$

It vanishes if and only if the annular vorticity lies in the exact two-mode moment span

$$
\boxed{
\operatorname{span}
\left\{
K_a,e
\right\}.
}
\tag{21.3}
$$

This is a new finite-dimensional equality manifold.

---

# 22. Physical meaning of the two modes

The two ideal matching modes have distinct roles.

### toroidal supplier mode

$$
\boxed{
K_a
}
$$

is zero-mean and produces the core pancake strain.

### mean-return mode

$$
\boxed{
e
}
$$

carries a nonzero annular mean vorticity component but has zero pancake strain moment on the centered spherical shell because

$$
\int K_a=0.
$$

Thus the two jobs do not substitute for one another at the linear moment level.

---

# 23. Kinematic compatibility NO-GO

Both ideal modes are divergence free in the annular interior:

$$
\boxed{
\nabla\cdot K_a=0,
\qquad
\nabla\cdot e=0.
}
\tag{23.1}
$$

Therefore their linear combination is also divergence free.

Hence:

$$
\boxed{
\textbf{
the two moment constraints are kinematically compatible.
}
}
\tag{23.2}
$$

A positive dual-moment lower bound is **not** an impossibility theorem.

Status:

$$
\boxed{
\textbf{NO-GO AGAINST OVERCLAIM}.
}
$$

---

# 24. Smooth matching caveat

The minimum moment field

$$
\omega_{\min}
$$

is defined only as an annular $L^2$ profile.

A globally smooth vorticity field must match it to:

- the Gaussian core;
- the outer recurrent flow.

Radial/tangential transition layers may generate additional:

- vorticity-gradient action;
- commutator residual;
- localization;
- rank/plane change.

These costs are not contained in

$$
\mathfrak X_{\rm match}
$$

unless they contribute to the moment-orthogonal annular vorticity.

Thus the next dynamic compiler must keep boundary matching explicit.

---

# 25. Divergence-free constrained minimization

If one declares a smaller admissible Hilbert space

$$
\boxed{
H_{\rm adm}
\subset
L^2(\mathcal A)
}
\tag{25.1}
$$

encoding:

- divergence-free vorticity;
- boundary compatibility;
- symmetry;
- sheet matching;

then the same Gram theorem applies using the Riesz representers of

$$
L_S,
L_R
$$

restricted to

$$
H_{\rm adm}.
$$

The resulting minimum cost can only increase.

This gives a systematic route for strengthening the two-mode lower bound as more matching conditions are added.

---

# 26. Period-integrated two-duty cost

If

$$
a=a(s),
\qquad
J_e=J_e(s),
$$

then

$$
\boxed{
\int_0^{S_0}
\|\omega_{\rm match}(s)\|_2^2ds
\ge
\int_0^{S_0}
\frac{
a(s)^2
}{
\|K_a\|_2^2
}ds
+
|\mathcal A|
\int_0^{S_0}
J_e(s)^2ds.
}
\tag{26.1}
$$

For the constant minimum Gaussian strain,

$$
a=a_0,
$$

the first term is explicit.

If a recurrent return-vorticity amplitude is additionally prescribed, the second term is also positive.

---

# 27. Relation to the DCRP-53 flux-amplitude audit

DCRP-53 proved that the ideal source-free one-dimensional sheet flux amplitude has a strict decay multiplier

$$
\rho_M<1.
$$

However Gaussian-shape recurrence does not automatically imply flux-amplitude recurrence.

Therefore the return moment

$$
J_e
$$

is:

- mandatory on a declared circulation-return/localization branch;
- conditional if only the Gaussian shape is recurrent.

DCRP-54 does not silently elevate this conditional datum into a universal moment.

---

# 28. Relation to finite-energy sheet zero-mean conditions

In two-dimensional finite-energy vortex-sheet theory, zero mean of the sheet amplitude appears as a natural global compatibility condition.

This is consistent with the DCRP intuition that an uncompensated shear jump cannot be localized at finite energy.

The external result is used only as calibration.

The DCRP-54 return theorem is formulated directly through Stokes and the strict Type-II tail alternatives, not by importing the two-dimensional theorem.

---

# 29. Relation to nonlocal/background strain literature

Direct Biot--Savart decompositions of turbulent strain distinguish local vorticity-induced strain from a nonlocal/background strain generated by vorticity outside a chosen neighborhood.

The DCRP-54 toroidal moment is precisely a finite-annulus representation of such a background affine-strain duty.

The current filtered-vorticity primary theory likewise identifies slowly varying far-field affine jets as the low-order modes that can remain visible across nested scales.

Thus the annular strain moment is well aligned with existing nonlocal-strain structure.

---

# 30. DCRP-31 PFET as a third duty

DCRP-31 already forces a finite-radius inward period-averaged kinetic-energy PFET matching layer.

DCRP-54 identifies two linear vorticity moments in a finite matching system.

There are two possibilities:

1. the PFET layer overlaps the dual-moment supplier;

2. the PFET layer is a distinct finite annulus.

In either case the union remains finite in normalized space.

The PFET constraint is nonlinear and is **not** included in the two-by-two Gram matrix.

Therefore the final equality state has at least:

$$
\boxed{
\text{strain moment}
+
\text{return/localization moment}
+
\text{inward PFET}
}
\tag{30.1}
$$

as matching duties.

---

# 31. Zero-excess two-mode equality state

On the ideal centered spherical branch with prescribed return moment, zero matching-moment excess means

$$
\boxed{
\omega_{\rm match}
=
c_S
K_a
+
c_R
e.
}
\tag{31.1}
$$

The coefficients are determined by

$$
a
$$

and

$$
J_e.
$$

For the minimum Gaussian core,

$$
a
$$

is constant.

If the return moment is also recurrent/constant, the ideal annular moment profile is stationary in similarity coordinates.

This is now a concrete dynamic candidate rather than an arbitrary annular supplier.

---

# 32. Why dynamic compatibility is nontrivial

Even if

$$
\omega_{\rm match}
\in
\operatorname{span}
\{K_a,e\},
$$

the unforced Navier--Stokes vorticity equation contains

$$
\boxed{
(W\cdot\nabla)\omega
-
(\omega\cdot\nabla)W
-
\varepsilon\Delta\omega.
}
\tag{32.1}
$$

There is no reason for this nonlinear/diffusive operator to preserve the two-dimensional moment span.

The induced velocity of the annular vorticity also couples:

- to the Gaussian core;
- to the outer flow;
- to pressure/PFET.

Therefore two-mode **kinematic compatibility** is much weaker than two-mode **dynamic invariance**.

This is the exact remaining issue.

---

# 33. Candidate dynamic leakage residual

Let

$$
\Pi_{\rm match}
$$

be the $L^2$ projection onto

$$
\operatorname{span}
\{K_a,e\}.
$$

For the annular vorticity equation define schematically

$$
\boxed{
\mathcal R_{\rm dyn}
=
(I-\Pi_{\rm match})
\left[
\partial_s\omega
+
(W\cdot\nabla)\omega
-
(\omega\cdot\nabla)W
-
\varepsilon\Delta\omega
\right].
}
\tag{33.1}
$$

An exact full solution has zero total vorticity-equation residual, but after projecting the core/outer couplings into the annular subsystem, the corresponding forcing must keep the two-mode manifold invariant.

A more useful implementation will isolate:

- internal two-mode nonlinear leakage;
- boundary/core forcing;
- outer-flow forcing;
- diffusion.

This is the next technical target.

---

# 34. Candidate minimum-supplier reproduction test

For the constant Gaussian equality, the strain moment satisfies

$$
a'=0.
$$

DCRP-36's affine-jet reproduction identity becomes

$$
\boxed{
a
=
J_{\rm dil}
+
J_{\rm adv}
+
J_{\rm str}
}
\tag{34.1}
$$

in the pancake tensor sector.

The two-mode matching profile must therefore generate exactly this fixed supplier moment every period.

A future theorem should compute the contribution of

$$
K_a
$$

and the return mode to these terms and test whether the two-mode span closes.

Status:

$$
\boxed{
\textbf{OPEN}.
}
$$

---

# 35. Combined branch tree after DCRP-54

The strongest coherent minimum Gaussian branch now requires at least one of:

$$
\boxed{
\text{positive matching-moment excess}
}
$$

or

$$
\boxed{
\text{two-mode annular equality}
}
$$

plus the existing possibilities:

$$
\boxed{
\text{circulation export / localization transition}
}
$$

$$
\boxed{
\text{PFET matching}
}
$$

$$
\boxed{
\text{rank/plane transition}
}
$$

$$
\boxed{
\text{commutator/localization residual}.
}
$$

The zero-excess equality branch is finite-dimensional in annular vorticity moments.

---

# 36. What DCRP-54 closes

The phrase

> the finite annulus somehow supplies the Gaussian core

is no longer an undifferentiated statement.

The strain duty alone requires an explicit annular vorticity moment with an exact $L^2$ lower bound.

If circulation return is also required in the same matching system, the return duty is an independent moment and adds a second Pythagorean cost on centered spherical shells.

Thus the matching annulus has a concrete moment geometry.

What DCRP-54 does **not** prove is that these moments are dynamically incompatible.

Indeed the ideal moment representers are kinematically compatible.

---

# 37. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Two-Mode Matching Manifold /
Navier--Stokes Reproduction and PFET Compatibility.
}
}
$$

A useful theorem would:

1. insert

   $$
   \omega_{\rm match}
   =
   c_SK_a+c_Re
   $$

   into the annular similarity vorticity dynamics;

2. project the nonlinear and viscous terms back onto and orthogonal to the two-mode span;

3. determine whether the span is dynamically invariant;

4. if not, obtain a quantitative orthogonal leakage residual;

5. couple the strain-mode coefficient to the DCRP-36 affine reproduction equation;

6. couple the annular velocity/pressure to the DCRP-31 inward PFET;

7. classify any exact invariant two-mode solution that survives.

The desired closure is

$$
\boxed{
\textbf{
Gaussian core + zero-excess two-mode annulus}
\Longrightarrow
\textbf{
dynamic leakage / PFET / reproduction defect}
}
$$

unless a new exact unforced matching solution exists.

That is now the narrowest coherent viscous equality problem.

---

# 38. Source-status audit

The 2026 filtered-vorticity primary source records the exact Calderón--Zygmund strain kernel, its degree $-3$ homogeneity, and zero spherical average. It also develops the far-field annular/harmonic-jet route in which distant vorticity shells generate slowly varying affine strain on a smaller core.

The earlier local/nonlocal strain paper likewise decomposes the strain through direct Biot--Savart integration into local and background contributions.

A finite-energy two-dimensional vortex-sheet paper notes zero mean amplitude as a global compatibility condition. DCRP-54 does not transfer that theorem to 3D; it uses it only as calibration for the return-vorticity interpretation.

The exact pancake representer, annular norm, toroidal formula, dual-moment Gram theorem, and Pythagorean matching excess are derived directly here.

---

# 39. End state

The finite matching annulus supplies the pancake coefficient through

$$
\boxed{
a
=
\int_{\mathcal A}
K_a\cdot\omega,
}
$$

with

$$
\boxed{
K_a(y)
=
\frac{
3
}{
8\pi
}
\frac{
y_3(y_2,-y_1,0)
}{
|y|^5
}.
}
$$

Its exact shell norm is

$$
\boxed{
\|K_a\|_2^2
=
\frac1{
40\pi
}
(
R_-^{-3}-R_+^{-3}
).
}
$$

Therefore

$$
\boxed{
\|\omega\|_2^2
\ge
\frac{
40\pi a^2
}{
R_-^{-3}-R_+^{-3}
}.
}
$$

On a centered spherical shell, a mean return-vorticity mode is orthogonal to the strain supplier.

Thus, when both duties are prescribed,

$$
\boxed{
\|\omega\|_2^2
=
\frac{
a^2
}{
\|K_a\|_2^2
}
+
|\mathcal A|J_e^2
+
\mathfrak X_{\rm match}.
}
$$

The zero-excess annular equality state is

$$
\boxed{
\omega_{\rm match}
\in
\operatorname{span}
\{K_a,e\}.
}
$$

This two-mode state is kinematically compatible.

The unresolved question is whether it is dynamically invariant/reproducible under the unforced Navier--Stokes matching dynamics while carrying the required inward PFET.

The next frontier is

$$
\boxed{
\textbf{
Two-Mode Matching Manifold /
Navier--Stokes Reproduction and PFET Compatibility.
}
}
$$