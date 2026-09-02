# NS-DCRP-33 — Circulation Replenishment, Backward Filamentation, and Navier–Stokes Kelvin Shadowing

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. convert DCRP-32 material-circulation replenishment from a qualitative statement into an exact backward-preimage theorem;
  2. prove that nonzero DSS circulation must be supplied either from spatially remote material labels or by exponential backward filamentation;
  3. quantify the associated line-stretching exponent;
  4. derive the similarity Cauchy vorticity formula and a conditional periodic-vortex hyperbolicity theorem;
  5. derive the exact Kelvin correction for the prelimit Type-II Navier--Stokes profiles;
  6. isolate a second-order viscous circulation residue as the only missing bridge between Euler holonomy and the same physical Navier--Stokes parent.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.
- internal dependencies:
  - DCRP-30 same-parent DSS recurrence;
  - DCRP-31 radial PFET matching-layer rigidity;
  - DCRP-32 Kelvin-holonomy rigidity.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-32 proved that for a nonzero strict DSS Euler profile

$$
\boxed{
\frac25<\gamma<\frac12
}
\tag{1.1}
$$

the similarity-material circulation obeys

$$
\boxed{
\Gamma_{ss}(s+S_0)
=
\rho_\Gamma
\Gamma_{ss}(s),
}
\tag{1.2}
$$

with

$$
\boxed{
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}
\in(0,1).
}
\tag{1.3}
$$

Let

$$
\Phi
$$

be the one-period similarity Poincare map.

Then for every smooth closed loop

$$
C,
$$

$$
\boxed{
\Gamma(\Phi(C))
=
\rho_\Gamma
\Gamma(C).
}
\tag{1.4}
$$

The first main result of DCRP-33 is obtained by iterating **backward**.

Define

$$
\boxed{
C_{-m}
=
\Phi^{-m}(C).
}
\tag{1.5}
$$

Then exactly

$$
\boxed{
\Gamma(C_{-m})
=
\rho_\Gamma^{-m}
\Gamma(C).
}
\tag{1.6}
$$

Thus if

$$
\Gamma(C)\neq0,
$$

the circulation carried by the material ancestors of the present core loop grows exponentially backward in similarity time.

This gives the exact replenishment theorem.

Let

$$
\mathcal T_m
$$

be the full material orbit tube swept out by

$$
C_{-m}
$$

during the next:

$$
m
$$

DSS periods until it reaches:

$$
C.
$$

Then at least one of the following occurs:

### material-tail escape

For every compact:

$$
K\Subset\mathbb R^3,
$$

the material tube:

$$
\mathcal T_m
$$

eventually leaves:

$$
K.
$$

### compact-core filamentation

There is a compact:

$$
K
$$

containing the full tube for infinitely many:

$$
m,
$$

and the backward loop lengths satisfy

$$
\boxed{
\operatorname{Length}(C_{-m})
\ge
\frac{
|\Gamma(C)|
}{
\|V\|_{L^\infty(K\times[0,S_0])}
}
\rho_\Gamma^{-m}.
}
\tag{1.7}
$$

Therefore:

$$
\boxed{
\textbf{
nonzero strict DSS circulation}
\Longrightarrow
\textbf{
backward material tail escape}
\ \vee\
\textbf{
exponential material filamentation}.
}
}
\tag{1.8}
$$

This is the exact answer to the DCRP-32 replenishment question:

> the normalized state can replace circulation-bearing material labels only by importing them from farther material regions or by generating increasingly filamentary preimage geometry.

The second main result converts filamentation into a stretching exponent.

The similarity material velocity is

$$
\boxed{
W(y,s)
=
\gamma y
+
V(y,s).
}
\tag{1.9}
$$

Let

$$
C(s)
$$

be a material loop and let

$$
L(s)
$$

be its length.

Then

$$
\boxed{
\left|
\frac d{ds}
\log L(s)
\right|
\le
\|
\nabla W(\cdot,s)
\|_{
L^\infty(
\mathcal T
)
}
}
\tag{1.10}
$$

on any material tube

$$
\mathcal T.
$$

If the backward orbit tube remains inside a fixed compact set, (1.7) implies

$$
\boxed{
\liminf_{m\to\infty}
\frac1{
mS_0
}
\int_{-mS_0}^{0}
\|
\nabla W
\|_{
L^\infty(
\mathcal T_m
)
}
ds
\ge
1-2\gamma.
}
\tag{1.11}
$$

Thus the strict DSS replenishment mechanism carries a nonzero dimensionless material-deformation rate.

The third result gives a stronger vorticity-side calibration.

The self-similar Cauchy formula is

$$
\boxed{
\Omega(
Y(a,s),s
)
=
e^{-(1+\gamma)s}
D_aY(a,s)
\Omega(a,0).
}
\tag{1.12}
$$

The corresponding one-period formula is

$$
\boxed{
\Omega(
\Phi(a),0
)
=
e^{-(1+\gamma)S_0}
D\Phi(a)
\Omega(a,0),
}
\tag{1.13}
$$

where profile periodicity is used.

If:

$$
a
$$

is a material point periodic under:

$$
\Phi
$$

with period:

$$
m,
$$

and:

$$
\Omega(a,0)\neq0,
$$

then:

$$
\boxed{
D\Phi^m(a)
\Omega(a,0)
=
e^{(1+\gamma)mS_0}
\Omega(a,0).
}
\tag{1.14}
$$

Hence the vorticity direction is an expanding eigendirection of the material return map.

Also:

$$
\boxed{
\det
D\Phi^m(a)
=
e^{3\gamma mS_0}.
}
\tag{1.15}
$$

Therefore the product of the two transverse multipliers is:

$$
\boxed{
e^{-(1-2\gamma)mS_0}.
}
\tag{1.16}
$$

For:

$$
\gamma<1/2,
$$

the transverse area is strictly contracting.

Thus every recurrent nonzero-vorticity material point in the strict branch is necessarily hyperbolic:

$$
\boxed{
\textbf{
vortex-line stretching}
+
\textbf{
transverse area contraction}.
}
\tag{1.17}
$$

The contraction exponent is precisely the Kelvin-holonomy exponent.

This is a conditional theorem because periodic material vortex points need not exist.

The fourth and most important result returns to the actual Navier--Stokes parent.

The Type-II normalized prelimit satisfies

$$
\boxed{
\partial_\tau v_n
+
(v_n\cdot\nabla)v_n
+
\nabla q_n
=
\varepsilon_n
\Delta v_n,
}
\tag{1.18}
$$

with

$$
\boxed{
\varepsilon_n
=
\nu/a_n
\to0.
}
\tag{1.19}
$$

Let

$$
C_n(\tau)
$$

be a material loop transported by:

$$
v_n.
$$

For the smooth pre-singularity Navier--Stokes flow one has the exact Kelvin correction

$$
\boxed{
\frac d{d\tau}
\oint_{
C_n(\tau)
}
v_n\cdot dy
=
\varepsilon_n
\oint_{
C_n(\tau)
}
\Delta v_n\cdot dy.
}
\tag{1.20}
$$

Integrating over one normalized return window:

$$
[0,S_0],
$$

$$
\boxed{
\Gamma_n(S_0)
-
\Gamma_n(0)
=
\mathfrak K_n^{visc}(C_n),
}
\tag{1.21}
$$

where

$$
\boxed{
\mathfrak K_n^{visc}(C_n)
=
\varepsilon_n
\int_0^{S_0}
\oint_{
C_n(\tau)
}
\Delta v_n\cdot dy
d\tau.
}
\tag{1.22}
$$

The small coefficient:

$$
\varepsilon_n\to0
$$

does **not** imply:

$$
\mathfrak K_n^{visc}\to0.
$$

This is the circulation analogue of the DCRP-28 anomalous viscous energy residue.

It is one derivative higher than the ordinary energy dissipation coordinate.

Therefore the exact same-parent bridge has the trichotomy:

$$
\boxed{
\textbf{
Euler Kelvin holonomy shadows to the NS parent}
}
$$

or:

$$
\boxed{
\limsup
|
\mathfrak K_n^{visc}
|
>0,
}
\tag{1.23}
$$

or:

$$
\boxed{
\textbf{
material-loop / state transition compactness fails}.
}
}
\tag{1.24}
$$

In the second branch the missing Euler circulation conservation is paid by a genuine normalized second-order Navier--Stokes circulation residue.

In the third branch the failure is already a material/transition defect.

Thus the profile-level Kelvin mechanism cannot disappear silently when one returns to the same physical parent.

The fifth result is a finite-compiler version.

DCRP-32 showed that on a compact nonzero strict DSS profile class one may choose finitely many loop templates with a uniform holonomy gap:

$$
c_{\rm hol}>0.
$$

For each such loop, the prelimit NS return satisfies:

$$
\boxed{
\text{DSS state-return gap}
\le
\text{material loop mismatch}
+
|
\mathfrak K_n^{visc}
|
+
o(1).
}
\tag{1.25}
$$

Hence on a compact strongly shadowed same-parent class, there is a uniform alternative:

$$
\boxed{
\textbf{
material tail escape}
\ \vee\
\textbf{
material filamentation}
\ \vee\
\textbf{
second-order viscous circulation residue}
\ \vee\
\textbf{
state/loop transition mismatch}.
}
}
\tag{1.26}
$$

This is the first complete replenishment normal form for the strict compact Type-II branch.

Combined with DCRP-31 and DCRP-32, a nonzero strict compact same-parent Type-II survivor now requires simultaneously:

$$
\boxed{
\text{inward PFET},
}
\tag{1.27}
$$

and one of:

$$
\boxed{
\text{tail-fed material replenishment}
\ \vee\
\text{exponential filamentation}
\ \vee\
\text{second-order viscous Kelvin residue}.
}
\tag{1.28}
$$

The important limitation is that none of these is yet known to have a globally finite budget whose repeated normalized cost yields a contradiction.

In particular:

- exponential material line stretching is compatible with smooth time-periodic/chaotic Euler dynamics in principle;
- a circulation-bearing loop may indeed come from the mandatory Type-II tail;
- the second-order viscous circulation residue is not controlled by the ordinary Navier--Stokes energy inequality.

Thus DCRP-33 closes **replenishment invisibility**, not Navier--Stokes regularity.

The next exact frontier is:

$$
\boxed{
\textbf{
Second-Order Kelvin Shadowing /
Viscous-Holonomy Closure Lemma}.
}
\tag{1.29}
$$

A useful closure theorem would prove that on a same-parent Type-II sequence:

1. if:

   $$
   \mathfrak K_n^{visc}\to0,
   $$

   then the Euler material tail/filamentation alternative produces a native transition carrier with strict return incompatibility;

2. if:

   $$
   \mathfrak K_n^{visc}\not\to0,
   $$

   then the normalized second-order circulation residue forces:

   - positive delayed second-order action;
   - a supplier/enstrophy mechanism already covered by the DCRP viscous/strain package;
   - or a non-summable higher-order same-parent tax.

This is now the shortest bridge back from the Euler DSS barrier to genuinely viscous Navier--Stokes structure.

---

# 2. DSS Kelvin recurrence

Let:

$$
V(y,s+S_0)
=
V(y,s)
$$

and let:

$$
Y(a,s)
$$

be the similarity-material flow.

The one-period map is:

$$
\boxed{
\Phi(a)
=
Y(a,S_0).
}
\tag{2.1}
$$

For a loop:

$$
C,
$$

define:

$$
\boxed{
\Gamma(C)
=
\oint_C
V(y,0)\cdot dy.
}
\tag{2.2}
$$

The self-similar Kelvin theorem gives:

$$
\boxed{
\Gamma(\Phi(C))
=
\rho_\Gamma
\Gamma(C),
}
\tag{2.3}
$$

where:

$$
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}.
$$

In the strict Type-II window:

$$
0<\rho_\Gamma<1.
$$

---

# 3. NEW THEOREM — Backward Circulation Amplification

## Theorem 3.1

Let:

$$
C_{-m}
=
\Phi^{-m}(C).
$$

Then:

$$
\boxed{
\Gamma(C_{-m})
=
\rho_\Gamma^{-m}
\Gamma(C).
}
\tag{3.1}
$$

### Proof

Apply:

$$
\Gamma(\Phi(C_{-1}))
=
\rho_\Gamma
\Gamma(C_{-1})
$$

and:

$$
\Phi(C_{-1})=C.
$$

Thus:

$$
\Gamma(C_{-1})
=
\rho_\Gamma^{-1}
\Gamma(C).
$$

Iterate.

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

# 4. Material orbit tube

For each:

$$
m,
$$

let:

$$
C_m(s)
$$

be the material evolution from:

$$
C_{-m}
$$

at:

$$
s=-mS_0
$$

to:

$$
C
$$

at:

$$
s=0.
$$

Define the full orbit tube:

$$
\boxed{
\mathcal T_m
=
\bigcup_{
-mS_0\le s\le0
}
C_m(s).
}
\tag{4.1}
$$

If:

$$
\mathcal T_m
$$

leaves every fixed compact set as:

$$
m\to\infty,
$$

the circulation-bearing material labels originate from the similarity tail.

This is a genuine material-tail replenishment route.

---

# 5. NEW THEOREM — Tail-or-Filamentation Replenishment

## Theorem 5.1

Let:

$$
C
$$

be a smooth loop with:

$$
\Gamma(C)\neq0.
$$

Then exactly one of the following broad alternatives must occur along a subsequence.

### material-tail escape

The orbit tubes:

$$
\mathcal T_m
$$

are not contained in any fixed compact subset of:

$$
\mathbb R^3.
$$

### compact-core filamentation

There is a compact:

$$
K
$$

such that:

$$
\mathcal T_m\subset K
$$

for infinitely many:

$$
m,
$$

and for those:

$$
m,
$$

$$
\boxed{
\operatorname{Length}(C_{-m})
\ge
\frac{
|\Gamma(C)|
}{
M_K
}
\rho_\Gamma^{-m},
}
\tag{5.1}
$$

where:

$$
\boxed{
M_K
=
\sup_{
(y,s)\in K\times[0,S_0]
}
|V(y,s)|.
}
\tag{5.2}
$$

### Proof

If the orbit tubes do not escape, take a compact:

$$
K
$$

containing the selected subsequence.

Periodicity bounds:

$$
V
$$

on:

$$
K\times[0,S_0].
$$

Then:

$$
\begin{aligned}
|\Gamma(C_{-m})|
&=
\left|
\oint_{
C_{-m}
}
V\cdot dy
\right|
\\
&\le
M_K
\operatorname{Length}(C_{-m}).
\end{aligned}
$$

Use Theorem 3.1.

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

# 6. Exponential line-complexity rate

Because:

$$
\rho_\Gamma^{-m}
=
e^{(1-2\gamma)mS_0},
$$

Theorem 5.1 gives:

$$
\boxed{
\liminf_{
m\to\infty
}
\frac1{
mS_0
}
\log
\operatorname{Length}(C_{-m})
\ge
1-2\gamma
}
\tag{6.1}
$$

on the compact-core branch.

Thus the replenishing material loop must become exponentially filamentary backward in similarity time.

This is a geometric return cost which does not share the raw kinetic-energy dimension.

---

# 7. Material line stretching and similarity strain

Let:

$$
W
=
\gamma y+V.
$$

For a material curve:

$$
C(s)
$$

with unit tangent:

$$
t,
$$

the standard line-element equation gives:

$$
\boxed{
\frac d{ds}
d\ell
=
t\cdot
S_W
t
\,d\ell,
}
\tag{7.1}
$$

where:

$$
S_W
=
\frac12
\left(
\nabla W+\nabla W^T
\right).
$$

Consequently:

$$
\boxed{
\left|
\frac d{ds}
\log
L(s)
\right|
\le
\|
S_W
\|_{L^\infty(C(s))}.
}
\tag{7.2}
$$

---

# 8. NEW THEOREM — Mandatory Material-Strain Action

## Theorem 8.1

On the compact-core filamentation branch:

$$
\boxed{
\liminf_{
m\to\infty
}
\frac1{
mS_0
}
\int_{-mS_0}^{0}
\|
S_W
\|_{
L^\infty(
C_m(s)
)
}
ds
\ge
1-2\gamma.
}
\tag{8.1}
$$

### Proof

Integrate (7.2) from:

$$
-mS_0
$$

to:

$$
0.
$$

Then:

$$
\log
\frac{
L(C_{-m})
}{
L(C)
}
\le
\int_{-mS_0}^{0}
\|
S_W
\|_{
L^\infty(C_m(s))
}
ds.
$$

Use (6.1).

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

# 9. Similarity Cauchy formula

The vorticity profile is:

$$
\Omega
=
\nabla\times V.
$$

For the similarity-material flow:

$$
Y(a,s),
$$

the Cauchy formula is:

$$
\boxed{
\Omega(
Y(a,s),s
)
=
e^{-(1+\gamma)s}
D_aY(a,s)
\Omega(a,0).
}
\tag{9.1}
$$

The similarity Jacobian is:

$$
\boxed{
\det
D_aY(a,s)
=
e^{3\gamma s}.
}
\tag{9.2}
$$

These are the standard self-similar Euler Cauchy formulas.

For time-periodic DSS profiles, the same derivation applies on each period.

---

# 10. One-period Cauchy relation

Using:

$$
\Omega(y,S_0)=\Omega(y,0),
$$

equation (9.1) gives:

$$
\boxed{
\Omega(
\Phi(a),0
)
=
e^{-(1+\gamma)S_0}
D\Phi(a)
\Omega(a,0).
}
\tag{10.1}
$$

This is the vorticity analogue of Kelvin holonomy.

---

# 11. Conditional periodic-vortex hyperbolicity

## Theorem 11.1

Suppose:

$$
a
$$

is a periodic point of:

$$
\Phi
$$

of period:

$$
m,
$$

and:

$$
\Omega(a,0)\neq0.
$$

Then:

$$
\boxed{
D\Phi^m(a)
\Omega(a,0)
=
e^{(1+\gamma)mS_0}
\Omega(a,0).
}
\tag{11.1}
$$

Thus the vorticity direction has multiplier:

$$
\boxed{
\Lambda_\omega
=
e^{(1+\gamma)mS_0}
>1.
}
\tag{11.2}
$$

Because:

$$
\boxed{
\det
D\Phi^m(a)
=
e^{3\gamma mS_0},
}
\tag{11.3}
$$

the product of the other two multipliers is:

$$
\boxed{
\Lambda_\perp^{(1)}
\Lambda_\perp^{(2)}
=
e^{-(1-2\gamma)mS_0}.
}
\tag{11.4}
$$

For:

$$
\gamma<1/2,
$$

the transverse area product is strictly contracting.

### Proof

Iterate (10.1) for:

$$
m
$$

periods and use:

$$
\Phi^m(a)=a.
$$

The determinant formula follows from:

$$
\nabla\cdot W=3\gamma.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED CONDITIONAL ON A PERIODIC MATERIAL VORTEX POINT}.
}
$$

---

# 12. Geometric interpretation

A recurrent material vortex point in the strict branch is forced into a saddle-type geometry:

$$
\boxed{
\text{strong vorticity-line expansion}
}
$$

with rate:

$$
1+\gamma,
$$

and:

$$
\boxed{
\text{transverse material-area contraction}
}
$$

with product exponent:

$$
1-2\gamma.
$$

The latter is exactly the Kelvin-circulation contraction exponent.

This identifies the circulation holonomy with a Cauchy-vorticity stretching mechanism.

---

# 13. Prelimit Type-II Navier--Stokes equation

The normalized Type-II prelimit satisfies:

$$
\boxed{
\partial_\tau v_n
+
(v_n\cdot\nabla)v_n
+
\nabla q_n
=
\varepsilon_n
\Delta v_n,
}
\tag{13.1}
$$

where:

$$
\boxed{
\varepsilon_n
=
\nu/a_n.
}
\tag{13.2}
$$

For each:

$$
n,
$$

the solution is smooth on the selected pre-singularity normalized interval.

---

# 14. Navier--Stokes Kelvin correction

Let:

$$
C_n(\tau)
$$

solve the material-loop transport:

$$
\boxed{
\partial_\tau X_n
=
v_n(
X_n,\tau
).
}
\tag{14.1}
$$

Define:

$$
\boxed{
\Gamma_n(\tau)
=
\oint_{
C_n(\tau)
}
v_n(y,\tau)\cdot dy.
}
\tag{14.2}
$$

Then:

$$
\boxed{
\frac d{d\tau}
\Gamma_n(\tau)
=
\varepsilon_n
\oint_{
C_n(\tau)
}
\Delta v_n(y,\tau)\cdot dy.
}
\tag{14.3}
$$

### Proof

Differentiate circulation along a material loop.

The transport and nonlinear terms combine into the material derivative.

The pressure gradient integrates to zero around a closed loop.

Only viscosity remains.

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

# 15. Second-order viscous circulation residue

Define over one normalized return interval:

$$
\boxed{
\mathfrak K_{n}^{visc}(C)
=
\varepsilon_n
\int_{0}^{S_0}
\oint_{
C_n(\tau)
}
\Delta v_n\cdot dy
d\tau.
}
\tag{15.1}
$$

Then:

$$
\boxed{
\Gamma_n(S_0)
-
\Gamma_n(0)
=
\mathfrak K_n^{visc}(C).
}
\tag{15.2}
$$

Although:

$$
\varepsilon_n\to0,
$$

the residue need not vanish because:

$$
\Delta v_n
$$

may diverge.

Thus:

$$
\boxed{
\textbf{
vanishing Type-II viscosity coefficient}
\not\Rightarrow
\textbf{
Kelvin shadowing}.
}
\tag{15.3}
$$

This is the circulation-level analogue of DCRP-28's energy-level anomalous viscous residue.

---

# 16. Physical scaling of circulation

For the Type-II normalization:

$$
v_n
=
\frac{
r_n
}{
a_n
}
U,
$$

and:

$$
dy
=
dx/r_n.
$$

Therefore:

$$
\boxed{
\Gamma_n^{norm}
=
\frac1{
a_n
}
\Gamma_n^{phys}.
}
\tag{16.1}
$$

The circulation normalization is amplitude-based, not raw-energy-based.

This is another reason the Kelvin route is not governed by the same geometric:

$$
\beta_n
$$

telescoping law.

---

# 17. Kelvin-shadowing dichotomy

Suppose:

$$
v_n
\to
V
$$

strongly enough on a compact loop tube to pass the material flow and circulation to the Euler DSS profile.

Then for each declared loop template:

### Kelvin-shadowed branch

$$
\boxed{
\mathfrak K_n^{visc}(C)
\to0.
}
\tag{17.1}
$$

The Euler Kelvin holonomy law survives in the limit.

Then Theorem 5.1 gives:

$$
\boxed{
\text{material tail escape}
\ \vee\
\text{exponential filamentation}.
}
\tag{17.2}
$$

### viscous-Kelvin branch

$$
\boxed{
\limsup_n
|
\mathfrak K_n^{visc}(C)
|
>
0.
}
\tag{17.3}
$$

A positive second-order viscous circulation residue remains.

### transition-shadowing failure

The material loops / return maps do not converge strongly enough to identify the same Euler material object.

This is a native material/transition compactness defect.

Thus no circulation holonomy can disappear without entering one of these channels.

---

# 18. Finite-loop compiler

DCRP-32 gives, on a compact normalized strict DSS profile class, finitely many loop templates:

$$
C^{(1)},
\dots,
C^{(N_\ast)}
$$

and:

$$
c_{\rm hol}>0
$$

such that every nonzero profile has at least one:

$$
j
$$

with:

$$
\boxed{
\mathcal H_\Gamma(
C^{(j)}
)
\ge
c_{\rm hol}.
}
\tag{18.1}
$$

Therefore the same-parent prelimit needs only finitely many corresponding NS loop tubes.

For at least one loop:

$$
\boxed{
c_{\rm hol}
\lesssim
\mathcal E_{\rm tail}
+
\mathcal F_{\rm line}
+
|
\mathfrak K_n^{visc}
|
+
\mathcal R_{\rm loop}
+
o(1),
}
\tag{18.2}
$$

where:

-:

  $$
  \mathcal E_{\rm tail}
  $$

  denotes material-tail escape;

-:

  $$
  \mathcal F_{\rm line}
  $$

  denotes filamentation / line-distortion;

-:

  $$
  \mathcal R_{\rm loop}
  $$

  denotes loop/state transition mismatch.

This is the finite-loop circulation replenishment compiler.

---

# 19. Profile-level replenishment closure

At the exact Euler DSS profile level:

$$
\boxed{
\textbf{
nonzero circulation}
\Longrightarrow
\textbf{
tail replenishment}
\ \vee\
\textbf{
filamentation}.
}
\tag{19.1}
$$

There is no third profile-level route.

Thus the qualitative DCRP-32 "new loops must arrive" statement is fully quantified.

The new loops come from:

- remote material labels;
- or increasingly folded/elongated local material geometry.

---

# 20. Why filamentation is not yet a contradiction

A smooth time-periodic three-dimensional flow may in principle have:

- chaotic trajectories;
- positive line-stretching exponents;
- complicated material filamentation.

Therefore:

$$
\boxed{
\textbf{
exponential line stretching}
}
$$

is not itself inconsistent with smooth Euler dynamics.

The theorem makes it a mandatory return carrier.

It does not exclude it universally.

---

# 21. Why tail replenishment is not yet a contradiction

DCRP-30 already proved that atom-free Type-II normalized **global energy** must escape to:

$$
\infty_x.
$$

Thus it is structurally plausible that circulation-bearing material labels also originate from the tail.

The remaining issue is whether the same tail can:

- continually replenish circulation;
- maintain the required inward PFET matching layer;
- avoid producing a nonzero pressure/scale/transition tax.

This is a much narrower tail-recurrence question.

---

# 22. Higher-order viscous meaning

Using:

$$
\nabla\cdot v_n=0,
$$

$$
\Delta v_n
=
-
\nabla\times\omega_n.
$$

Therefore:

$$
\boxed{
\oint_C
\Delta v_n\cdot dy
}
$$

is a second-order vorticity/circulation quantity.

By Stokes, for a smooth spanning surface:

$$
S_C,
$$

$$
\boxed{
\oint_C
\Delta v_n\cdot dy
=
\int_{S_C}
\Delta\omega_n\cdot n
dS
}
\tag{22.1}
$$

modulo the standard curl/Laplacian commutation.

Thus:

$$
\mathfrak K_n^{visc}
$$

is genuinely higher-order than the ordinary:

$$
\nu
\int
|\nabla v_n|^2.
$$

It may connect naturally to:

- delayed second-order action;
- enstrophy production;
- supplier/strain activation;
- Oseen second-order budgets.

This connection is not yet quantitatively closed.

---

# 23. Conditional periodic-vortex point route

If the strict DSS profile contains a periodic material point with:

$$
\Omega\neq0,
$$

Theorem 11.1 yields the exact vorticity multiplier:

$$
e^{(1+\gamma)mS_0}.
$$

This gives a much stronger local derivative demand than the loop-length bound:

$$
e^{(1-2\gamma)mS_0}.
$$

A possible future route is to shadow such a periodic hyperbolic vortex point to the Navier--Stokes parent and prove that the required derivative amplification forces a nonzero:

$$
\mathfrak K_n^{visc}
$$

or normalized viscous/enstrophy tax.

No existence theorem for such periodic vortex points is assumed.

---

# 24. Updated strict Type-II normal form

After DCRP-31--33, the compact strong strict Type-II state satisfies:

$$
\boxed{
\text{Euler DSS}
+
\frac25<\gamma<\frac12.
}
$$

It has:

$$
\boxed{
\text{mandatory inward PFET matching layer}
}
$$

and:

$$
\boxed{
\text{mandatory circulation replenishment}.
}
$$

The replenishment is:

$$
\boxed{
\text{material tail}
\ \vee\
\text{exponential filamentation}.
}
$$

When shadowed back to the Navier--Stokes parent, one adds:

$$
\boxed{
\text{second-order viscous Kelvin residue}
}
$$

or:

$$
\boxed{
\text{loop-transition defect}.
}
$$

Thus the remaining strict compact branch is no longer a silent self-similar state.

It is a flux-active, materially replenished, possibly second-order-viscous recurrence.

---

# 25. What has been closed

The following false/ambiguous possibilities are removed.

### energy-only summation

Cannot close the proof because of critical telescoping.

### circulation replenishment from nowhere

Impossible.

Backward Kelvin iteration identifies the replenishment source.

### arbitrary hidden material recurrence

Impossible without tail escape or exponential filamentation.

### automatic Euler Kelvin shadowing from small viscosity coefficient

False.

A second-order viscous circulation residue may survive.

Thus each stage now has an explicit native carrier.

---

# 26. Exact remaining gap

The strict same-parent branch still survives if one can realize indefinitely:

$$
\boxed{
\text{inward PFET}
+
\text{tail-fed circulation replenishment}
}
$$

or:

$$
\boxed{
\text{inward PFET}
+
\text{exponential filamentation},
}
$$

while the actual Navier--Stokes circulation correction is either negligible or absorbed into a higher-order residue.

No global finite budget for these dimensionless material mechanisms is presently known.

---

# 27. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Second-Order Kelvin Shadowing /
Viscous-Holonomy Closure Lemma}.
}
$$

A useful theorem would prove one of the following.

### Route A — vanishing Kelvin viscosity

If:

$$
\mathfrak K_n^{visc}\to0,
$$

then the tail/filamentation replenishment required by Euler DSS forces a nonzero existing:

$$
\mathsf O_{\rm PFET}
+
\mathsf R_{\rm nat}
$$

return tax which cannot be hidden by critical energy telescoping.

### Route B — nonvanishing Kelvin viscosity

If:

$$
\limsup
|
\mathfrak K_n^{visc}
|
>0,
$$

then this second-order residue forces:

$$
\boxed{
\text{delayed second-order action}
\ \vee\
\text{enstrophy production}
\ \vee\
\text{supplier/strain payment}.
}
$$

### Route C — failure of loop shadowing

If material loops cannot be shadowed across the Type-II limit, the loop compactness failure itself must be retained as a transition defect.

This is now the shortest genuinely Navier--Stokes-specific frontier after the Euler DSS reduction.

---

# 28. Source-status audit

Constantin--Ignatova--Vicol derive for globally self-similar Euler:

$$
\boxed{
\Omega(
Y(a,\tau)
)
=
e^{-(1+\gamma)\tau}
D_aY(a,\tau)
\Omega(a),
}
$$

and:

$$
\boxed{
\det D_aY
=
e^{3\gamma\tau}.
}
$$

They also derive the self-similar Weber/Kelvin relation:

$$
\boxed{
e^{(1-2\gamma)\tau}
\Gamma_{ss}(\tau)
=
\Gamma_{ss}(0).
}
$$

The source identifies:

$$
\gamma=1/2
$$

as the circulation-neutral similarity exponent and proves an outgoing-property obstruction below that threshold.

DCRP-33 applies the same local differential identities period-by-period to the time-periodic DSS profile generated by the same-parent recurrence.

---

# 29. End state

The exact backward replenishment law is:

$$
\boxed{
\Gamma(
\Phi^{-m}C
)
=
e^{(1-2\gamma)mS_0}
\Gamma(C).
}
$$

Hence:

$$
\boxed{
\textbf{
nonzero strict DSS circulation}
\Longrightarrow
\textbf{
material-tail escape}
\ \vee\
\textbf{
exponential backward filamentation}.
}
$$

On the compact-core branch:

$$
\boxed{
\operatorname{Length}(
\Phi^{-m}C
)
\gtrsim
e^{(1-2\gamma)mS_0}.
}
$$

A recurrent vortex material point, if present, obeys the stronger Cauchy multiplier:

$$
\boxed{
D\Phi^m
\Omega
=
e^{(1+\gamma)mS_0}
\Omega.
}
$$

The actual normalized Navier--Stokes parent obeys:

$$
\boxed{
\Gamma_n(S_0)-\Gamma_n(0)
=
\frac{\nu}{a_n}
\int_0^{S_0}
\oint_{C_n(\tau)}
\Delta v_n\cdot dy
d\tau.
}
$$

Thus Euler Kelvin holonomy either:

- shadows to the same parent;
- leaves a second-order viscous circulation residue;
- or fails through a material-transition compactness defect.

The next single frontier is:

$$
\boxed{
\textbf{
Second-Order Kelvin Shadowing /
Viscous-Holonomy Closure.
}
}
$$