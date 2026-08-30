# NS-DCRP-55 — Two-Mode Dynamic Leakage, Boundary Solenoidality, and the Failure of Autonomous Matching Closure

- date: 2026-08-17
- status: research proof checkpoint / annular dynamic-invariance audit
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. test whether the DCRP-54 zero-excess two-mode matching manifold is invariant under the local similarity Navier--Stokes vorticity dynamics;
  2. separate linear interior invariance from nonlinear leakage and finite-annulus boundary leakage;
  3. prove that the toroidal strain-supplier mode is harmonic and is preserved by the linear similarity/diffusion operator in the annular interior;
  4. construct an explicit divergence-free velocity primitive of the supplier mode;
  5. compute its exact nonlinear self-interaction;
  6. prove that this self-interaction leaves the DCRP-54 two-mode span;
  7. compute an exact dyadic-shell orthogonal leakage norm;
  8. show that an aligned constant return mode cannot cancel the supplier self-leakage because the cross interaction lies in a different azimuthal sector;
  9. audit the harmonic-velocity ambiguity and state precisely why the nonlinear leakage is a matching-forcing duty rather than yet an unconditional global contradiction;
  10. prove that finite radial localization of the constant return-vorticity mode violates vorticity solenoidality unless a new boundary correction mode is added;
  11. formulate the exact Helmholtz-distance cost of that solenoidal correction;
  12. conclude that the two-mode interior equality manifold cannot by itself be a complete finite-annulus matching solution;
  13. identify the next frontier as the minimal solenoidal multi-mode matching manifold and its PFET/reproduction dynamics.
- no full Navier--Stokes regularity claim is made.
- external primary calibration:
  - I. Fouxon et al., *General solution of the unsteady Stokes equations in spherical polar coordinates*, arXiv:2110.00387;
  - R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-31 finite-radius inward PFET;
  - DCRP-53 finite Gaussian-core matching radius;
  - DCRP-54 toroidal strain supplier and two-moment annular equality manifold.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-54 reduced the ideal centered matching annulus to the zero-excess moment manifold

$$
\boxed{
\omega_{\rm match}
=
c_S K_a
+
c_R e,
}
\tag{1.1}
$$

where

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
z(y,-x,0)
}{
|y|^5
}
}
\tag{1.2}
$$

is the toroidal strain-supplier mode and

$$
e
$$

is an idealized mean return-vorticity mode.

The two moments are kinematically compatible in the annular interior.

DCRP-55 proves that this does **not** make the two-dimensional span dynamically autonomous.

There are two independent failures.

### nonlinear interior leakage

The supplier mode is linearly perfect but nonlinearly non-closed.

A canonical divergence-free primitive is

$$
\boxed{
V_a(y)
=
\frac{
x^2+y^2-2z^2
}{
16\pi|y|^5
}
(x,y,z).
}
\tag{1.3}
$$

It satisfies

$$
\boxed{
\nabla\times V_a=K_a,
\qquad
\nabla\cdot V_a=0.
}
\tag{1.4}
$$

The vorticity nonlinearity is

$$
\boxed{
\mathcal N_{aa}
=
(K_a\cdot\nabla)V_a
-
(V_a\cdot\nabla)K_a
=
\frac{
x^2+y^2-2z^2
}{
4\pi|y|^5
}
K_a.
}
\tag{1.5}
$$

The extra angular/radial factor means

$$
\boxed{
\mathcal N_{aa}
\notin
\operatorname{span}
\{K_a,e\}
}
\tag{1.6}
$$

on every open spherical annulus.

Thus the strain-supplier mode self-generates a higher toroidal mode.

### finite-annulus solenoidal leakage

For a radial cutoff

$$
\chi(r),
$$

$$
\boxed{
\nabla\cdot(\chi K_a)=0,
}
\tag{1.7}
$$

because

$$
K_a\cdot\widehat r=0.
$$

But

$$
\boxed{
\nabla\cdot(\chi e)
=
\chi'(r)e\cdot\widehat r
\neq0
}
\tag{1.8}
$$

for every nontrivial radial cutoff.

Therefore a constant return-vorticity mode cannot be localized to a finite spherical matching annulus while remaining a legitimate vorticity field.

A solenoidal boundary correction is mandatory.

These two facts produce the main DCRP-55 conclusion:

$$
\boxed{
\textbf{
the DCRP-54 two-mode span is an interior moment manifold,
not a complete finite-annulus Navier--Stokes matching manifold.
}
}
\tag{1.9}
$$

Even before imposing PFET, a true finite matching system needs at least:

1. the toroidal strain supplier;

2. the return-vorticity duty;

3. nonlinear higher-mode cancellation and/or a harmonic/core--outer forcing;

4. a solenoidal boundary-localization correction.

The next sections quantify these statements.

---

# 2. Linear interior closure

The supplier mode is homogeneous of degree

$$
-3.
$$

Hence

$$
\boxed{
(y\cdot\nabla)K_a
=
-3K_a.
}
\tag{2.1}
$$

Also direct differentiation gives

$$
\boxed{
\nabla\cdot K_a=0,
\qquad
\Delta K_a=0
}
\tag{2.2}
$$

for

$$
y\neq0.
$$

For the constant mode

$$
e,
$$

$$
\boxed{
(y\cdot\nabla)e=0,
\qquad
\Delta e=0.
}
\tag{2.3}
$$

Thus every linear operator assembled from:

- constant multiplication;
- similarity dilation:

  $$
  \gamma y\cdot\nabla;
  $$

- molecular diffusion:

  $$
  \varepsilon\Delta;
  $$

preserves

$$
\boxed{
\operatorname{span}
\{K_a,e\}
}
\tag{2.4}
$$

in the open annular interior.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Therefore the first third-mode generation is genuinely nonlinear or boundary-driven.

---

# 3. Toroidal/poloidal character

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
\tag{3.1}
$$

It is an axisymmetric toroidal vorticity mode.

The primitive

$$
V_a
$$

is axisymmetric and poloidal.

Indeed

$$
\boxed{
V_a
=
\frac{
\rho^2-2z^2
}{
16\pi(\rho^2+z^2)^{5/2}
}
(
\rho e_\rho
+
z e_z
).
}
\tag{3.2}
$$

Thus the toroidal vorticity is generated by a poloidal velocity.

This is consistent with the standard poloidal--toroidal decomposition of solenoidal vector fields in spherical geometry.

---

# 4. Construction of the canonical primitive

Use the axisymmetric no-swirl stream function

$$
\boxed{
\psi_a(\rho,z)
=
-
\frac1{
16\pi
}
\frac{
\rho^2z
}{
(\rho^2+z^2)^{3/2}
}.
}
\tag{4.1}
$$

With the convention

$$
V_\rho
=
-\rho^{-1}\partial_z\psi,
\qquad
V_z
=
\rho^{-1}\partial_\rho\psi,
$$

one obtains

$$
\boxed{
V_\rho
=
\frac{
\rho(\rho^2-2z^2)
}{
16\pi(\rho^2+z^2)^{5/2}
},
}
\tag{4.2}
$$

and

$$
\boxed{
V_z
=
\frac{
z(\rho^2-2z^2)
}{
16\pi(\rho^2+z^2)^{5/2}
}.
}
\tag{4.3}
$$

This is exactly (1.3).

Direct differentiation verifies

$$
\boxed{
\nabla\times V_a=K_a.
}
\tag{4.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. NEW THEOREM — Supplier Self-Interaction Leakage

## Theorem 5.1

The canonical supplier pair

$$
(V_a,K_a)
$$

satisfies

$$
\boxed{
(K_a\cdot\nabla)V_a
-
(V_a\cdot\nabla)K_a
=
q_a(y)K_a,
}
\tag{5.1}
$$

where

$$
\boxed{
q_a(y)
=
\frac{
x^2+y^2-2z^2
}{
4\pi|y|^5
}.
}
\tag{5.2}
$$

Since

$$
q_a
$$

is nonconstant on every open spherical annulus,

$$
\boxed{
\mathcal N_{aa}
\notin
\operatorname{span}
\{K_a,e\}.
}
\tag{5.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This proves failure of autonomous two-mode nonlinear closure for the canonical interior primitive.

---

# 6. Angular content

Write

$$
u=\cos\theta.
$$

Then

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
r^{-3}
\sin\theta\cos\theta
\,e_\phi,
}
\tag{6.1}
$$

while

$$
\boxed{
q_a
=
\frac{
1-3u^2
}{
4\pi
}
r^{-3}.
}
\tag{6.2}
$$

Therefore

$$
\boxed{
\mathcal N_{aa}
=
-
\frac{
3
}{
32\pi^2
}
r^{-6}
\sin\theta\cos\theta
(
1-3\cos^2\theta
)
e_\phi.
}
\tag{6.3}
$$

The nonlinear product preserves axisymmetry and toroidal character but generates a higher angular polynomial and a new radial homogeneity.

Thus the leakage is structurally a higher toroidal mode.

---

# 7. Dyadic-shell norms

Let

$$
\boxed{
\mathcal A_R
=
\{
R<|y|<2R
\}.
}
\tag{7.1}
$$

The supplier norm is

$$
\boxed{
\|K_a\|_{L^2(\mathcal A_R)}^2
=
\frac{
7
}{
320\pi R^3
}.
}
\tag{7.2}
$$

The nonlinear self-interaction satisfies

$$
\boxed{
\|\mathcal N_{aa}\|_2^2
=
\frac{
73
}{
245760\pi^3R^9
},
}
\tag{7.3}
$$

and

$$
\boxed{
\langle
\mathcal N_{aa},
K_a
\rangle
=
-
\frac{
9
}{
10240\pi^2R^6
}.
}
\tag{7.4}
$$

Hence the best $L^2$ projection coefficient onto

$$
K_a
$$

is

$$
\boxed{
\beta_R
=
-
\frac{
9
}{
224\pi R^3
}.
}
\tag{7.5}
$$

---

# 8. NEW THEOREM — Exact Orthogonal Supplier Leakage

## Theorem 8.1

On the dyadic shell,

$$
\boxed{
\left\|
\mathcal N_{aa}
-
\beta_RK_a
\right\|_2^2
=
\frac{
1801
}{
6881280\pi^3R^9
}.
}
\tag{8.1}
$$

The right-hand side is strictly positive.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the canonical supplier self-interaction has a quantitative orthogonal leakage gap.

---

# 9. Zero-excess supplier normalization

DCRP-54's zero-moment-excess strain supplier is

$$
\boxed{
\omega_S
=
c_SK_a,
}
\tag{9.1}
$$

where

$$
\boxed{
c_S
=
\frac{
a
}{
\|K_a\|_2^2
}
=
\frac{
320\pi
}{
7
}
aR^3.
}
\tag{9.2}
$$

Its minimum annular enstrophy is

$$
\boxed{
\|\omega_S\|_2^2
=
\frac{
320\pi
}{
7
}
a^2R^3.
}
\tag{9.3}
$$

The canonical nonlinear self-interaction scales as

$$
c_S^2\mathcal N_{aa}.
$$

---

# 10. NEW THEOREM — Quantitative Intrinsic Dynamic Leakage

## Theorem 10.1

For the zero-excess supplier mode on a dyadic shell,

$$
\boxed{
\left\|
(I-\Pi_{K_a})
\mathcal N(
\omega_S
)
\right\|_2^2
=
\frac{
57632000\pi
}{
50421
}
a^4R^3.
}
\tag{10.1}
$$

Moreover,

$$
\boxed{
\frac{
\left\|
(I-\Pi_{K_a})
\mathcal N(
\omega_S
)
\right\|_2^2
}{
\|\omega_S\|_2^2
}
=
\frac{
180100
}{
7203
}
a^2.
}
\tag{10.2}
$$

Numerically,

$$
\boxed{
\frac{
180100
}{
7203
}
\approx
25.00347.
}
\tag{10.3}
$$

Status:

$$
\boxed{
\textbf{PROVED FOR THE CANONICAL INTERIOR PRIMITIVE}.
}
$$

The coefficient is order one in the normalized equality regime.

---

# 11. Constant return-mode primitive

For a constant vorticity direction

$$
e,
$$

a canonical local primitive is the solid rotation

$$
\boxed{
V_e
=
\frac12
e\times y.
}
\tag{11.1}
$$

It satisfies

$$
\boxed{
\nabla\times V_e=e,
\qquad
\nabla\cdot V_e=0.
}
\tag{11.2}
$$

The return mode has zero self-vorticity nonlinearity:

$$
\boxed{
(e\cdot\nabla)V_e
-
(V_e\cdot\nabla)e
=
0.
}
\tag{11.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the first intrinsic nonlinear leakage is generated by the strain-supplier sector.

---

# 12. Aligned return cross interaction

Take the return-vorticity direction aligned with the Gaussian-core tangential vorticity,

$$
\boxed{
e=e_1.
}
\tag{12.1}
$$

Then

$$
V_e
=
\frac12
e_1\times y.
$$

Define the bilinear cross interaction

$$
\boxed{
\mathcal N_{aR}
=
(K_a\cdot\nabla)V_e
+
(e\cdot\nabla)V_a
-
(V_a\cdot\nabla)e
-
(V_e\cdot\nabla)K_a.
}
\tag{12.2}
$$

The supplier self-leakage is axisymmetric:

$$
m=0.
$$

The cross interaction transforms in the first azimuthal sector:

$$
m=1.
$$

Hence on every centered spherical annulus,

$$
\boxed{
\langle
\mathcal N_{aR},
K_a
\rangle=0,
}
\tag{12.3}
$$

and

$$
\boxed{
\left\langle
\mathcal N_{aR},
(I-\Pi_{K_a})\mathcal N_{aa}
\right\rangle
=
0.
}
\tag{12.4}
$$

Status:

$$
\boxed{
\textbf{PROVED BY AZIMUTHAL FOURIER ORTHOGONALITY}.
}
$$

Therefore the physically aligned constant return mode cannot cancel the axisymmetric higher-toroidal supplier self-leakage.

---

# 13. Canonical two-mode nonlinear conclusion

For

$$
\boxed{
\omega
=
c_SK_a+c_Re_1
}
\tag{13.1}
$$

with canonical primitives

$$
V=c_SV_a+c_RV_e,
$$

the nonlinear term contains

$$
\boxed{
c_S^2
(I-\Pi_{K_a})
\mathcal N_{aa}
}
\tag{13.2}
$$

in the axisymmetric higher-toroidal sector.

Neither:

- the constant return self-interaction;
- nor the supplier--return cross interaction;

cancels this sector.

Hence:

$$
\boxed{
\textbf{
the canonical two-mode interior manifold is not invariant under the nonlinear vorticity dynamics whenever }a\neq0.
}
\tag{13.3}
$$

Status:

$$
\boxed{
\textbf{PROVED FOR THE CANONICAL PRIMITIVE MODEL}.
}
$$

---

# 14. Harmonic-velocity ambiguity

A vorticity field on an annulus does not uniquely determine the local velocity without boundary/core/outer data.

If two divergence-free velocities have the same vorticity in a simply connected annulus, their difference

$$
H
$$

satisfies

$$
\boxed{
\nabla\times H=0,
\qquad
\nabla\cdot H=0.
}
\tag{14.1}
$$

Therefore

$$
\boxed{
H=\nabla\phi,
\qquad
\Delta\phi=0.
}
\tag{14.2}
$$

Such a harmonic velocity changes the vorticity nonlinearity by

$$
\boxed{
\mathcal B_H(\omega)
=
(\omega\cdot\nabla)H
-
(H\cdot\nabla)\omega.
}
\tag{14.3}
$$

Thus the core/outer harmonic field can in principle generate an orthogonal contribution that cancels the canonical self-leakage.

This is why Theorem 13.3 is **not** promoted to an unconditional global impossibility theorem.

---

# 15. Harmonic cancellation duty

Exact two-mode annular recurrence requires

$$
\boxed{
(I-\Pi_{\rm match})
[
\mathcal N_{\rm int}
+
\mathcal B_H(\omega)
+
\mathcal R_{\rm bdry}
]
=
0,
}
\tag{15.1}
$$

where:

-:

  $$
  \mathcal N_{\rm int}
  $$

  is the canonical internal nonlinear term;

-:

  $$
  H
  $$

  is the harmonic/core--outer velocity correction;

-:

  $$
  \mathcal R_{\rm bdry}
  $$

  contains finite-annulus matching terms.

Since

$$
\mathcal N_{\rm int}
$$

has a nonzero higher-toroidal component, zero-excess recurrence requires a nonzero cancellation duty.

Thus the annulus has acquired a third dynamical job:

$$
\boxed{
\textbf{
higher-mode cancellation / dynamic reproduction}.
}
\tag{15.2}
$$

---

# 16. Affine-only harmonic correction audit

The simplest harmonic correction is the core pancake affine field

$$
\boxed{
H_{\rm aff}
=
aTy.
}
\tag{16.1}
$$

Its interaction with the unit supplier mode is

$$
\boxed{
\mathcal B_{\rm aff}(K_a)
=
(K_a\cdot\nabla)H_{\rm aff}
-
(H_{\rm aff}\cdot\nabla)K_a.
}
\tag{16.2}
$$

Direct calculation gives

$$
\boxed{
\mathcal B_{\rm aff}(K_a)
=
[
7-15\cos^2\theta
]
K_a
}
\tag{16.3}
$$

for unit coefficient in

$$
H_{\rm aff}=Ty.
$$

This remains in the axisymmetric toroidal angular family but is not proportional to

$$
K_a.
$$

Thus an affine harmonic correction does not generically preserve the two-mode vorticity span either.

---

# 17. Quantitative affine-compensation NO-GO

On the dyadic shell, impose simultaneously:

$$
c_S
=
\frac{
320\pi
}{
7
}
aR^3,
$$

and the affine harmonic field

$$
H_{\rm aff}=aTy.
$$

Let

$$
\mathcal N_{\rm can+aff}
=
c_S^2\mathcal N_{aa}
+
c_Sa
\mathcal B_{\rm aff}(K_a).
$$

Then after best projection onto

$$
K_a,
$$

$$
\boxed{
\left\|
(I-\Pi_{K_a})
\mathcal N_{\rm can+aff}
\right\|_2^2
=
\frac{
158432000\pi
}{
50421
}
a^4R^3
>0.
}
\tag{17.1}
$$

Status:

$$
\boxed{
\textbf{PROVED FOR THE CANONICAL AFFINE-ONLY CORRECTION}.
}
$$

Therefore the required core affine strain alone does not close the supplier's higher-mode dynamics.

Additional harmonic/matching structure is required.

---

# 18. Finite radial localization of the supplier

Let

$$
\chi(r)
$$

be a radial cutoff supported in a finite annular region.

Since

$$
K_a\cdot\widehat r=0,
$$

$$
\boxed{
\nabla\cdot
[
\chi(r)K_a
]
=
0.
}
\tag{18.1}
$$

Thus the toroidal strain-supplier mode can be radially localized without violating

$$
\nabla\cdot\omega=0.
$$

This is a special advantage of the toroidal mode.

---

# 19. NEW THEOREM — Constant Return Cutoff Is Not Solenoidal

For the constant mode,

$$
\boxed{
\nabla\cdot
[
\chi(r)e
]
=
\chi'(r)
e\cdot\widehat r.
}
\tag{19.1}
$$

If

$$
\chi'
\not\equiv0,
$$

the right-hand side is not identically zero.

Therefore:

$$
\boxed{
\textbf{
a nontrivial finite radial localization of the constant return-vorticity mode is not a valid divergence-free vorticity field.
}
}
\tag{19.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

A finite matching annulus must add a boundary correction or use a different divergence-free return representer.

---

# 20. Minimal solenoidal correction

Let

$$
g
=
\chi e.
$$

We seek

$$
q
$$

such that

$$
\boxed{
\nabla\cdot(g+q)=0.
}
\tag{20.1}
$$

In the whole-space Helmholtz decomposition, the minimal $L^2$ correction is

$$
\boxed{
q_{\min}
=
-
\nabla
\Delta^{-1}
(
\nabla\cdot g
).
}
\tag{20.2}
$$

Its squared norm is

$$
\boxed{
\|q_{\min}\|_2^2
=
\|
\nabla\cdot g
\|_{\dot H^{-1}}^2.
}
\tag{20.3}
$$

Since

$$
\nabla\cdot g
=
\chi'(r)e\cdot\widehat r
$$

is nonzero for every nontrivial cutoff,

$$
\boxed{
\|q_{\min}\|_2>0.
}
\tag{20.4}
$$

Status:

$$
\boxed{
\textbf{PROVED AS THE HELMHOLTZ PROJECTION DISTANCE}.
}
$$

This is a precise boundary-localization cost.

---

# 21. Angular character of the return correction

The source

$$
\boxed{
\chi'(r)e\cdot\widehat r
}
\tag{21.1}
$$

belongs to the degree-one spherical harmonic sector.

Therefore the solenoidal correction is an

$$
\ell=1
$$

poloidal/radial mode.

It is not contained in the pure constant-vector annular ansatz.

Thus a globally localized return field naturally upgrades the v54 two-mode manifold to at least a multi-component poloidal--toroidal structure.

---

# 22. Corrected kinematic status of DCRP-54

DCRP-54 correctly showed that

$$
K_a
$$

and

$$
e
$$

are both divergence free **inside** the annulus.

DCRP-55 refines this:

$$
\boxed{
\textbf{
interior kinematic compatibility}
\neq
\textbf{
finite-annulus global solenoidal compatibility}.
}
\tag{22.1}
$$

The constant return mode requires a boundary correction when localized.

This is a correction of scope, not a contradiction of the DCRP-54 interior theorem.

---

# 23. Three distinct matching duties

The finite annular matching system now has at least three independent structural duties.

### strain moment

Generate

$$
aT
$$

in the Gaussian core.

### return/localization

Remove or redistribute the coherent Gaussian shear/circulation before the strict tail is violated.

### dynamic closure

Cancel the higher toroidal nonlinear leakage generated by the strain-supplier mode and the boundary modes.

Additionally DCRP-31 requires:

### PFET

Carry finite-radius inward kinetic-energy flux.

Thus the final matching station is at least a four-duty system.

---

# 24. Why the new leakage is not yet a global contradiction

The full Navier--Stokes solution includes:

- core velocity;
- annular velocity;
- outer recurrent velocity;
- pressure;
- harmonic velocity contributions.

Those fields can force the annulus.

Therefore a nonzero internal leakage does not imply the full vorticity equation fails.

It implies only:

$$
\boxed{
\textbf{
the annular two-mode subsystem is not autonomous.
}
}
\tag{24.1}
$$

Exact recurrence requires nontrivial cross-region/higher-mode coupling.

This is the quotient-safe conclusion.

---

# 25. Relation to vector spherical harmonics

The linear Stokes operator in spherical geometry is naturally diagonalized/decomposed using vector spherical harmonics and poloidal--toroidal components.

DCRP-55's result is consistent with that framework:

- the toroidal supplier is a single low angular sector;
- the constant return/localization correction occupies a degree-one sector;
- nonlinear products generate additional angular sectors.

The external spherical-harmonic literature is used only as calibration.

The explicit supplier and nonlinear formulas are derived directly here.

---

# 26. Dynamic leakage coordinate

Let

$$
\Pi_{\rm 2m}
$$

denote the $L^2$ projection onto the ideal DCRP-54 moment span

$$
\operatorname{span}
\{K_a,e\}.
$$

Define the canonical intrinsic leakage

$$
\boxed{
\mathfrak L_{\rm int}
=
\left\|
(I-\Pi_{\rm 2m})
\mathcal N_{\rm int}
\right\|_2^2.
}
\tag{26.1}
$$

On the pure zero-excess supplier branch,

$$
\boxed{
\mathfrak L_{\rm int}
\ge
\frac{
57632000\pi
}{
50421
}
a^4R^3
}
\tag{26.2}
$$

for the canonical dyadic primitive model.

Define the boundary solenoidal leakage

$$
\boxed{
\mathfrak L_{\rm div}
=
\|
\nabla\cdot(\chi e)
\|_{\dot H^{-1}}^2.
}
\tag{26.3}
$$

Then every finite matching implementation must pay or cancel these two different leakage coordinates.

---

# 27. Minimum expanded matching class

The smallest structurally honest finite-annulus matching class is no longer

$$
\boxed{
\operatorname{span}
\{K_a,e\}.
}
$$

It must contain at least:

1. the toroidal supplier;

2. a divergence-free localized return mode;

3. the nonlinear higher-toroidal response or a harmonic forcing that cancels it.

Thus a candidate minimal class has the schematic form

$$
\boxed{
\mathcal M_{\rm match}^{(3+)}
=
\operatorname{span}
\{
K_a,
R_{\rm sol},
H_{\rm tor}^{(hi)}
\}
}
\tag{27.1}
$$

plus any pressure/PFET-compatible velocity components.

The exact optimal basis remains open.

---

# 28. Relation to matching-moment excess

DCRP-54 defined

$$
\mathfrak X_{\rm match}
$$

as $L^2$ excess orthogonal to the two moment representers.

DCRP-55 shows that a true finite-annulus solution may need

$$
\mathfrak X_{\rm match}>0
$$

even if it is dynamically optimal, because the moment-minimizing two-mode field is not dynamically and globally closed.

Therefore the correct next optimization is not:

$$
\boxed{
\mathfrak X_{\rm match}=0.
}
$$

It is:

$$
\boxed{
\textbf{
minimum excess subject to solenoidality, dynamic closure, boundary matching, and PFET.
}
}
\tag{28.1}
$$

This is a stronger constrained variational problem.

---

# 29. A new equality hierarchy

The matching equality states now form a hierarchy:

### Level 0 — moment equality

$$
\omega
\in
\operatorname{span}
\{K_a,e\}.
$$

### Level 1 — solenoidal finite-annulus equality

Add the minimum return-boundary correction.

### Level 2 — dynamic equality

Add exactly the modes required to cancel nonlinear leakage.

### Level 3 — PFET equality

The velocity/pressure field also carries the required inward PFET.

### Level 4 — same-parent reproduction

The entire constrained matching state returns under one DSS period.

Only the final level is a genuine candidate survivor.

---

# 30. Supplier nonlinear leakage versus Gaussian core

The Gaussian core needs

$$
a\neq0.
$$

Therefore

$$
c_S\neq0.
$$

Hence the canonical supplier self-leakage cannot be removed by setting the strain mode to zero.

Any exact final equality must cancel it dynamically.

Thus the new higher-mode duty is not optional on the Gaussian branch.

---

# 31. Return mode can change the details, not the need for closure

A different divergence-free return representer

$$
R_{\rm sol}
$$

may alter:

- cross-interaction coefficients;
- the Gram matrix;
- boundary correction cost.

It may even share angular sectors with the supplier leakage.

Therefore DCRP-55 does not claim that every possible return geometry has the same orthogonality as the constant aligned mode.

The robust conclusion is:

$$
\boxed{
\textbf{
the strain-supplier self-interaction is outside the pure supplier mode;
some additional dynamic mode/coupling is required.
}
}
\tag{31.1}
$$

The exact cancellation mechanism remains to be optimized.

---

# 32. PFET remains nonlinear and independent

The inward PFET from DCRP-31 is not determined by the vorticity moment constraints alone.

Even after adding the minimal solenoidal and nonlinear correction modes, the pressure/velocity flux must satisfy

$$
\boxed{
\mathcal F_{\rm PFET}<0
}
\tag{32.1}
$$

at a finite matching radius.

Thus PFET is still an additional nonlinear constraint on the expanded matching manifold.

---

# 33. What DCRP-55 closes

The following candidate is removed:

$$
\boxed{
\textbf{
an autonomous two-mode finite-annulus matching solution}.
}
}
\tag{33.1}
$$

It fails because:

1. the supplier mode self-generates a higher toroidal nonlinear mode;

2. the ideal constant return mode cannot be finitely radial-localized while preserving vorticity solenoidality.

The following stronger conclusion is proved:

$$
\boxed{
\textbf{
every genuine finite Gaussian matching annulus needs higher-mode/cross-region structure beyond the two moment minimizers.
}
}
\tag{33.2}
$$

This is a real dynamic reduction.

---

# 34. What remains open

The extra structure may in principle close exactly.

A specially chosen divergence-free return mode and harmonic/core--outer forcing could:

- cancel the supplier higher-mode leakage;
- satisfy finite boundary matching;
- carry PFET;
- reproduce the Gaussian core strain.

DCRP-55 does not prove such a constrained matching state impossible.

The problem has been upgraded from a two-mode kinematic manifold to a minimal multi-mode dynamical manifold.

---

# 35. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Minimal Solenoidal Multi-Mode Matching /
Dynamic Closure and PFET.
}
}
$$

A useful next theorem would:

1. solve the minimum-energy divergence-free localization of the return mode in a spherical annulus;

2. obtain its explicit degree-one poloidal--toroidal representation;

3. insert that mode with

   $$
   K_a
   $$

   into the annular vorticity dynamics;

4. identify the lowest new toroidal/poloidal sectors generated by the nonlinear interaction;

5. close or prove non-closure of the smallest finite spherical-harmonic mode set;

6. impose the core strain moment and return moment exactly;

7. test the induced velocity/pressure for the DCRP-31 inward PFET condition.

The desired statement is:

$$
\boxed{
\textbf{
finite Gaussian matching}
\Longrightarrow
\textbf{
unavoidable mode cascade / PFET defect}
}
$$

unless a new exact finite-mode unforced matching solution exists.

That is now the narrowest coherent viscous equality frontier.

---

# 36. Source-status audit

The spherical Stokes literature develops divergence-free solutions through vector spherical harmonics and poloidal--toroidal decompositions. This calibrates the DCRP-55 statement that finite spherical matching should be analyzed by angular sectors rather than by raw Cartesian modes.

The 2026 filtered-vorticity primary source likewise emphasizes that distant annular vorticity leaves a low-order harmonic/affine jet on an inner core while residual annular dynamics and commutator effects remain separate channels.

DCRP-55's explicit harmonicity of $K_a$, primitive $V_a$, nonlinear self-interaction, dyadic leakage constants, and finite-cutoff solenoidality failure are derived directly in this document.

---

# 37. End state

The DCRP-54 strain supplier is linearly exceptional:

$$
\boxed{
\Delta K_a=0,
\qquad
(y\cdot\nabla)K_a=-3K_a.
}
$$

But its canonical nonlinear self-interaction is

$$
\boxed{
\mathcal N_{aa}
=
\frac{
x^2+y^2-2z^2
}{
4\pi|y|^5
}
K_a,
}
$$

which leaves the two-mode span.

On a dyadic shell, the exact orthogonal unit-supplier leakage is

$$
\boxed{
\left\|
(I-\Pi_{K_a})
\mathcal N_{aa}
\right\|_2^2
=
\frac{
1801
}{
6881280\pi^3R^9
}.
}
$$

For the zero-excess strain coefficient $a$,

$$
\boxed{
\mathfrak L_{\rm int}
=
\frac{
57632000\pi
}{
50421
}
a^4R^3.
}
$$

Meanwhile a finite radial cutoff of the ideal constant return mode satisfies

$$
\boxed{
\nabla\cdot(\chi e)
=
\chi'(r)e\cdot\widehat r,
}
$$

so a positive solenoidal correction is mandatory.

Therefore:

$$
\boxed{
\textbf{
the two-mode annular moment equality is neither nonlinearly autonomous nor globally localizable as a complete finite matching state.
}
}
$$

The next frontier is

$$
\boxed{
\textbf{
Minimal Solenoidal Multi-Mode Matching /
Dynamic Closure and PFET.
}
}
$$
