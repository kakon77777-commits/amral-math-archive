---
# NS-DCRP-35 — DSS Enstrophy Replenishment, Finite-Annulus Strain Supply, and External Affine-Jet Reduction

- date: 2026-08-17
- status: research proof checkpoint / correction-and-reduction round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. replace the heuristic "Kelvin--Oseen equality" language of DCRP-34 by an exact vorticity/enstrophy dynamical ledger;
  2. prove a period-averaged DSS enstrophy replenishment identity;
  3. show that a nonzero strict DSS core must be sustained by positive vortex stretching or inward enstrophy transport;
  4. prove that, on a smooth critical-tail profile, arbitrarily near self-strain and arbitrarily remote tail-strain can both be made small;
  5. localize the unavoidable stretching source to a finite intermediate annulus;
  6. reduce that finite-annulus source, on a sufficiently small core, to a finite-dimensional symmetric trace-free affine strain jet;
  7. identify the next same-parent problem as reproduction of that annular affine strain without external forcing.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1;
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.
- internal dependencies:
  - DCRP-30 strict same-parent DSS exponent window;
  - DCRP-31 radial PFET matching-layer theorem;
  - DCRP-34 quotient-corrected Kelvin/circulation audit.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction and result

DCRP-34 observed the exact scaling coincidence

$$
\rho_\Gamma
=
\rho_{\nu}
=
\rho_{\perp}
$$

in the strict same-parent DSS normalization and interpreted this as a candidate critical Kelvin--Oseen strain--diffusion equality.

The scaling coincidence is exact.

However:

$$
\boxed{
\textbf{
equal return multipliers}
\not\Rightarrow
\textbf{
actual Burgers/Oseen PDE balance}.
}
\tag{1.1}
$$

An actual strain--diffusion equality requires a dynamical vorticity balance.

DCRP-35 supplies the missing exact dynamical ledger.

Let

$$
V(y,s+S_0)=V(y,s)
$$

be a smooth Euler DSS similarity profile.

Let

$$
\boxed{
\gamma
=
\frac1{\alpha+1},
\qquad
\frac25<\gamma<\frac12.
}
\tag{1.2}
$$

Define

$$
\boxed{
W(y,s)
=
\gamma y+V(y,s),
}
\tag{1.3}
$$

and

$$
\boxed{
\Omega
=
\nabla\times V,
\qquad
S
=
\frac12
\left(
\nabla V+\nabla V^T
\right).
}
\tag{1.4}
$$

The similarity vorticity equation is

$$
\boxed{
\partial_s\Omega
+
W\cdot\nabla\Omega
+
\Omega
=
\Omega\cdot\nabla V.
}
\tag{1.5}
$$

Set

$$
\boxed{
w
=
\frac12|\Omega|^2.
}
\tag{1.6}
$$

Then

$$
\boxed{
\partial_sw
+
\nabla\cdot(Ww)
+
(2-3\gamma)w
=
\Omega\cdot S\Omega.
}
\tag{1.7}
$$

Because

$$
V
$$

and

$$
\Omega
$$

are periodic in

$$
s,
$$

integration over one DSS period and one fixed ball gives

$$
\boxed{
\mathcal S(R)
=
(2-3\gamma)
\mathcal O(R)
+
\mathcal J_\omega(R),
}
\tag{1.8}
$$

where

$$
\boxed{
\mathcal O(R)
=
\int_0^{S_0}
\int_{B_R}
\frac12|\Omega|^2
dyds,
}
\tag{1.9}
$$

$$
\boxed{
\mathcal S(R)
=
\int_0^{S_0}
\int_{B_R}
\Omega\cdot S\Omega
dyds,
}
\tag{1.10}
$$

and

$$
\boxed{
\mathcal J_\omega(R)
=
\int_0^{S_0}
\int_{\partial B_R}
\frac12|\Omega|^2
W\cdot n
dSds.
}
\tag{1.11}
$$

Since

$$
\gamma<1/2,
$$

$$
\boxed{
2-3\gamma>\frac12.
}
\tag{1.12}
$$

Define the inward enstrophy transport

$$
\boxed{
\mathcal J_{\omega,\mathrm{in}}(R)
=
\left(
-\mathcal J_\omega(R)
\right)_+.
}
\tag{1.13}
$$

Then

$$
\boxed{
(2-3\gamma)
\mathcal O(R)
\le
\mathcal S_+(R)
+
\mathcal J_{\omega,\mathrm{in}}(R),
}
\tag{1.14}
$$

where

$$
\boxed{
\mathcal S_+(R)
=
\int_0^{S_0}
\int_{B_R}
\left(
\Omega\cdot S\Omega
\right)_+
dyds.
}
\tag{1.15}
$$

Thus every nonzero strict DSS vorticity core satisfies the exact alternative

$$
\boxed{
\textbf{
positive vortex stretching}
\ \vee\
\textbf{
inward enstrophy/material turnover}.
}
\tag{1.16}
$$

This statement does not require a periodic material point.

It is a fixed-core Eulerian balance.

The second main result localizes the stretching source.

Assume the strict profile belongs to the fixed-source Biot--Savart representation class used below and satisfies a critical tail-energy envelope

$$
\boxed{
\sup_{s\in[0,S_0]}
\int_{B_R}
|V(y,s)|^2dy
\le
C_E R^\kappa,
\qquad
\kappa=3-2\alpha\in(0,1).
}
\tag{1.17}
$$

The strain kernel is homogeneous of degree

$$
-3
$$

and has zero spherical average.

For a smooth core one obtains

$$
\boxed{
\|S_{<\delta}\|_{L^\infty(K\times[0,S_0])}
\le
C
\delta
\|\nabla\Omega\|_{L^\infty(K_{2\delta}\times[0,S_0])}.
}
\tag{1.18}
$$

Thus the arbitrarily near self-strain can be made uniformly small by

$$
\delta\downarrow0.
$$

For the remote exterior source, integrating

$$
\Omega=\nabla\times V
$$

by parts against the differentiated strain kernel yields

$$
\boxed{
\|S_{>L}\|_{L^\infty(K\times[0,S_0])}
\le
C
C_E^{1/2}
L^{(\kappa-5)/2}.
}
\tag{1.19}
$$

Since

$$
0<\kappa<1,
$$

$$
\boxed{
S_{>L}\to0
}
\tag{1.20}
$$

uniformly on every fixed core as

$$
L\to\infty.
$$

Hence:

$$
\boxed{
\textbf{
arbitrarily near self-strain can be small}
}
$$

and

$$
\boxed{
\textbf{
arbitrarily remote tail-strain can be small}.
}
$$

Therefore if the inward enstrophy transport is small, the stretching needed by (1.14) must be supplied at a **finite intermediate relative radius**.

More precisely, choose a vortical core

$$
B_{r_0}
$$

with

$$
\mathcal O(r_0)>0.
$$

Choose

$$
\delta>4r_0
$$

small enough and

$$
L\gg\delta
$$

large enough so that the near and remote contributions together account for at most one quarter of the required positive stretching.

Then either

$$
\boxed{
\mathcal J_{\omega,\mathrm{in}}(r_0)
\ge
c_\gamma
\mathcal O(r_0)
}
\tag{1.21}
$$

or the finite-annulus strain contribution satisfies

$$
\boxed{
\mathcal S_{\mathrm{ann}}^+(r_0;\delta,L)
\ge
c_\gamma
\mathcal O(r_0),
}
\tag{1.22}
$$

for a positive constant

$$
c_\gamma
$$

depending only on the compact exponent window and the chosen decomposition constants.

Thus:

$$
\boxed{
\textbf{
nonzero strict DSS core}
\Longrightarrow
\textbf{
inward enstrophy turnover}
\ \vee\
\textbf{
finite-annulus external strain supplier}.
}
\tag{1.23}
$$

This is the central result of DCRP-35.

The third main result reduces the annular supplier to a finite-dimensional affine strain jet.

Use a **fixed annular source partition** centered at the recurrent core.

Let

$$
\psi_{\delta,L}
$$

be supported in

$$
\left\{
\delta/2<|y|<2L
\right\}
$$

and equal to one on the principal supplier annulus.

Define the annular strain field

$$
\boxed{
H_{\delta,L}(x,s)
=
\int
K(x-y)
\psi_{\delta,L}(y)
\Omega(y,s)dy.
}
\tag{1.24}
$$

Because the source is outside

$$
B_{\delta/2},
$$

$$
H_{\delta,L}
$$

is smooth and harmonic componentwise on

$$
B_{\delta/4}.
$$

Define the leading strain jet

$$
\boxed{
A_{\delta,L}(s)
=
H_{\delta,L}(0,s).
}
\tag{1.25}
$$

The tensor

$$
A_{\delta,L}(s)
$$

is symmetric and trace free.

For

$$
r_0\ll\delta,
$$

Taylor expansion gives

$$
\boxed{
H_{\delta,L}(x,s)
=
A_{\delta,L}(s)
+
\mathcal R_{\delta,L}(x,s),
}
\tag{1.26}
$$

with

$$
\boxed{
\|\mathcal R_{\delta,L}\|_{L^\infty(B_{r_0})}
\le
C
\frac{r_0}{\delta}
\mathcal A_{\delta,L}(s),
}
\tag{1.27}
$$

where

$$
\mathcal A_{\delta,L}
$$

is a fixed annular strain-source norm.

By shrinking

$$
r_0/\delta
$$

inside a compact normalized profile class, the Taylor remainder can be made a fixed small fraction of the annular stretching gap.

Hence the finite-annulus supplier alternative reduces to

$$
\boxed{
\int_0^{S_0}
\int_{B_{r_0}}
\left(
\Omega\cdot
A_{\delta,L}(s)
\Omega
\right)_+
dyds
\ge
c_A
\mathcal O(r_0).
}
\tag{1.28}
$$

Thus the strict zero-turnover branch must contain a nontrivial **external affine strain jet**.

The jet lives in the five-dimensional space

$$
\boxed{
\mathrm{Sym}_0(3)
=
\left\{
A=A^T:
\operatorname{tr}A=0
\right\}.
}
\tag{1.29}
$$

This is a major compression of the tail-strain problem.

The external strain needed to maintain the core is no longer an arbitrary infinite-dimensional field.

At leading order on the core it is a five-component time-periodic tensor generated by a finite same-parent annulus.

The external literature already identifies the same geometry at the filtered level:

- the Calderon--Zygmund strain kernel is homogeneous of degree:

  $$
  -3;
  $$

- singular near-field positive stretching is geometrically depleted and can be absorbed into diffusion in the Navier--Stokes filtered balance;
- every surviving positive surplus is assigned to far-field strain, commutator forcing, or localization;
- fixed exterior-source strain fields are harmonic on the core, and the leading recurrent low-order mode is an affine jet.

DCRP-35 supplies the additional strict-DSS enstrophy ledger and the finite-annulus localization needed by the current Type-II branch.

The fourth result is a correction to the DCRP-34 equality terminology.

The equality

$$
\rho_\Gamma
=
\rho_\nu
=
\rho_\perp
$$

should henceforth be called

$$
\boxed{
\textbf{
Kelvin--viscous scaling compatibility}
}
\tag{1.30}
$$

unless an actual vorticity balance also shows that the strain supplier saturates the viscous core balance.

A genuine Burgers/Oseen-like equality requires at least:

1. a persistent core vorticity carrier;
2. a persistent positive extensional strain supplier;
3. a transverse viscous concentration scale;
4. quantitative balance of stretching and diffusion.

Only the first two are now dynamically localized by the current chain.

The correct strongest strict branch is therefore

$$
\boxed{
\textbf{
tail-fed DSS}
+
\textbf{
inward PFET}
+
\left[
\textbf{
enstrophy turnover}
\ \vee\
\textbf{
finite-annulus affine strain supply}
\right].
}
\tag{1.31}
$$

If circulation cascade, microviscous concentration, and transition defects are also absent, the surviving state is not yet a proven Oseen vortex.

It is an **unforced same-parent DSS core with a recurrent annular affine strain supplier**.

This is the new equality manifold.

The next exact frontier is

$$
\boxed{
\textbf{
Annular Affine-Strain Reproduction /
Unforced Burgers-Jet Closure Lemma}.
}
\tag{1.32}
$$

The question is:

> can one finite same-parent annular vorticity reservoir reproduce, DSS period after DSS period, the extensional affine strain jet required by the core while also supplying the DCRP-31 inward PFET, without generating an additional strain/model-cone, pressure, scale, or transition defect?

This is now the precise meaning of:

> who is pulling the filament?

---

# 2. Similarity vorticity equation

The DSS similarity velocity equation is

$$
\boxed{
\partial_sV
+
(1-\gamma)V
+
\gamma
(y\cdot\nabla)V
+
(V\cdot\nabla)V
+
\nabla P
=
0.
}
\tag{2.1}
$$

Taking curl and using

$$
\nabla\cdot V=0
$$

gives

$$
\boxed{
\partial_s\Omega
+
\Omega
+
\gamma
(y\cdot\nabla)\Omega
+
(V\cdot\nabla)\Omega
-
(\Omega\cdot\nabla)V
=
0.
}
\tag{2.2}
$$

Set

$$
W
=
\gamma y+V.
$$

Then

$$
\boxed{
\partial_s\Omega
+
W\cdot\nabla\Omega
+
\Omega
=
(\Omega\cdot\nabla)V.
}
\tag{2.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 3. DSS enstrophy equation

Let

$$
w
=
|\Omega|^2/2.
$$

Dot (2.3) with

$$
\Omega.
$$

The antisymmetric part of

$$
\nabla V
$$

does not contribute.

Thus

$$
\boxed{
\partial_sw
+
W\cdot\nabla w
+
2w
=
\Omega\cdot S\Omega.
}
\tag{3.1}
$$

Since

$$
\nabla\cdot W
=
3\gamma,
$$

$$
W\cdot\nabla w
=
\nabla\cdot(Ww)
-
3\gamma w.
$$

Therefore

$$
\boxed{
\partial_sw
+
\nabla\cdot(Ww)
+
(2-3\gamma)w
=
\Omega\cdot S\Omega.
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

# 4. NEW THEOREM — Periodic Core Enstrophy Replenishment

## Theorem 4.1

For almost every

$$
R>0,
$$

a smooth

$$
S_0
$$

-periodic DSS profile satisfies

$$
\boxed{
\mathcal S(R)
=
(2-3\gamma)
\mathcal O(R)
+
\mathcal J_\omega(R).
}
\tag{4.1}
$$

Consequently

$$
\boxed{
(2-3\gamma)
\mathcal O(R)
\le
\mathcal S_+(R)
+
\mathcal J_{\omega,\mathrm{in}}(R).
}
\tag{4.2}
$$

### Proof

Integrate (3.2) over

$$
B_R\times[0,S_0].
$$

The time-endpoint term vanishes by periodicity.

The divergence term gives

$$
\mathcal J_\omega(R).
$$

For the inequality, write

$$
(2-3\gamma)\mathcal O
=
\mathcal S-\mathcal J_\omega
\le
\mathcal S_+
+
(-\mathcal J_\omega)_+.
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

# 5. Strict exponent gap

For

$$
\frac25<\gamma<\frac12,
$$

$$
\boxed{
\frac12
<
2-3\gamma
<
\frac45.
}
\tag{5.1}
$$

Thus the similarity equation contains a fixed positive enstrophy-demand coefficient.

A nonzero periodic core cannot be maintained with both

$$
\mathcal S_+=0
$$

and

$$
\mathcal J_{\omega,\mathrm{in}}=0.
$$

This is a dynamical statement, not a scaling analogy.

---

# 6. Strain kernel

For a smooth divergence-free velocity field in the standard Biot--Savart representation class,

$$
\boxed{
S_{ij}(x)
=
\operatorname{p.v.}
\int
K_{ijm}(z)
\Omega_m(x-z)dz,
}
\tag{6.1}
$$

where

$$
K
$$

is homogeneous of degree

$$
-3
$$

and has zero spherical average.

This is the classical Calderon--Zygmund strain representation.

The zero spherical average is crucial for the small near-field estimate.

---

# 7. NEW LEMMA — Smooth Near-Field Self-Strain Decay

## Lemma 7.1

Let

$$
K_0
$$

be a compact core and suppose

$$
\Omega
$$

is

$$
C^1
$$

on a

$$
2\delta
$$

neighborhood.

Let

$$
S_{<\delta}
$$

be the radially truncated near-field strain.

Then

$$
\boxed{
\|S_{<\delta}\|_{L^\infty(K_0)}
\le
C
\delta
\|\nabla\Omega\|_{L^\infty(K_{2\delta})}.
}
\tag{7.1}
$$

### Proof

Because the strain kernel has zero spherical mean, the constant vorticity may be subtracted:

$$
S_{<\delta}(x)
=
\int
K(z)
\eta_\delta(z)
\left[
\Omega(x-z)-\Omega(x)
\right]dz.
$$

Use

$$
|\Omega(x-z)-\Omega(x)|
\le
|z|
\|\nabla\Omega\|_\infty.
$$

Since

$$
|K(z)|
\lesssim
|z|^{-3},
$$

$$
\int_{|z|<2\delta}
|K(z)|
|z|
dz
\lesssim
\delta.
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

# 8. Interpretation of the near-field lemma

For a smooth vorticity core, the arbitrarily singular-looking local Biot--Savart kernel does not provide a fixed positive stretching source at arbitrarily small radius.

Its leading constant-direction contribution cancels.

This agrees with the geometric-depletion structure of the filtered-vorticity literature.

Thus a smooth Oseen-like core cannot attribute its required order-one extensional strain to an infinitesimal self-neighborhood.

---

# 9. Tail energy envelope

Assume

$$
\boxed{
\sup_s
\int_{B_R}
|V|^2dy
\le
C_E R^\kappa,
}
\tag{9.1}
$$

where

$$
0<\kappa<1.
$$

This is the critical-tail upper envelope used in DCRP-31.

It is stronger than merely stating infinite global normalized energy.

---

# 10. Exterior strain by integration by parts

For a smooth radial cutoff

$$
\chi_L
$$

supported in

$$
|y|>L
$$

and equal to one for

$$
|y|>2L,
$$

consider

$$
\boxed{
S_{>L}(x)
=
\int
K(x-y)
\chi_L(y)
\Omega(y)dy.
}
\tag{10.1}
$$

Use

$$
\Omega
=
\nabla\times V
$$

and integrate by parts on the fixed exterior partition.

The resulting kernel acting on

$$
V
$$

has size

$$
\boxed{
O(|x-y|^{-4})
}
\tag{10.2}
$$

away from the cutoff shell.

The cutoff derivative produces the same order at radius

$$
L.
$$

---

# 11. NEW THEOREM — Remote Tail-Strain Decoupling

## Theorem 11.1

Let

$$
K_0\Subset B_{L/4}.
$$

Under (9.1),

$$
\boxed{
\|S_{>L}\|_{L^\infty(K_0\times[0,S_0])}
\le
C
C_E^{1/2}
L^{(\kappa-5)/2}.
}
\tag{11.1}
$$

### Proof

Decompose the exterior into dyadic shells

$$
A_j
=
\left\{
2^jL<|y|<2^{j+1}L
\right\}.
$$

The differentiated kernel is bounded by

$$
C(2^jL)^{-4}.
$$

Cauchy--Schwarz gives

$$
\begin{aligned}
\int_{A_j}
(2^jL)^{-4}|V|dy
&\le
C
(2^jL)^{-4}
|A_j|^{1/2}
\|V\|_{L^2(A_j)}
\\
&\le
C
C_E^{1/2}
(2^jL)^{-4}
(2^jL)^{3/2}
(2^jL)^{\kappa/2}
\\
&=
C
C_E^{1/2}
(2^jL)^{(\kappa-5)/2}.
\end{aligned}
$$

The dyadic series converges because

$$
\kappa<5.
$$

The cutoff-shell terms have the same order.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED under the fixed-source representation and tail-envelope assumptions}.
}
$$

---

# 12. Remote tail-strain versus remote tail pressure

DCRP-31 proved, under the analogous critical tail assumptions, that the arbitrarily remote pressure contribution decays on a fixed core.

DCRP-35 proves the corresponding strain statement.

Thus neither:

$$
\boxed{
\text{direct pressure}
}
$$

nor

$$
\boxed{
\text{direct strain}
}
$$

from arbitrarily remote normalized infinity is forced to remain order one on the core.

The unavoidable coupling is a finite matching region.

---

# 13. Core choice

Choose a point

$$
y_\ast
$$

with

$$
\Omega(y_\ast,s_\ast)\neq0.
$$

Translate the recurrent core gauge so

$$
y_\ast=0.
$$

By smoothness there exists

$$
r_0>0
$$

such that

$$
\boxed{
\mathcal O(r_0)>0.
}
\tag{13.1}
$$

The radius may be chosen sufficiently small for the uniform near-field/Taylor estimates below.

---

# 14. Stretching-source decomposition

Fix

$$
4r_0<\delta<L/4.
$$

Decompose

$$
\boxed{
S
=
S_{\mathrm{near}}
+
S_{\mathrm{mid}}
+
S_{\mathrm{far}}
}
\tag{14.1}
$$

using a fixed smooth partition compatible with:

- source distance:

  $$
  \lesssim\delta;
  $$

- finite intermediate source region:

  $$
  \delta\lesssim|y|\lesssim L;
  $$

- exterior source:

  $$
  \gtrsim L.
  $$

The exact partition may introduce fixed overlap shells.

These are included in

$$
S_{\mathrm{mid}}.
$$

---

# 15. Uniform smallness of near and far work

Let

$$
c_0
=
2-3\gamma.
$$

For a single smooth profile, choose

$$
\delta
$$

so small that

$$
\boxed{
\int_0^{S_0}
\int_{B_{r_0}}
|
\Omega\cdot
S_{\mathrm{near}}
\Omega
|
\le
\frac{c_0}{8}
\mathcal O(r_0).
}
\tag{15.1}
$$

Then choose

$$
L
$$

large so that

$$
\boxed{
\int_0^{S_0}
\int_{B_{r_0}}
|
\Omega\cdot
S_{\mathrm{far}}
\Omega
|
\le
\frac{c_0}{8}
\mathcal O(r_0).
}
\tag{15.2}
$$

On a compact smooth normalized profile class with uniform

$$
C^1
$$

core bounds and a uniform tail envelope, the choices may be made uniformly.

---

# 16. NEW THEOREM — Turnover-or-Finite-Annulus Strain Supplier

## Theorem 16.1

Let

$$
V
$$

be a nonzero smooth strict DSS profile satisfying the hypotheses above.

Then either

$$
\boxed{
\mathcal J_{\omega,\mathrm{in}}(r_0)
\ge
\frac{c_0}{4}
\mathcal O(r_0)
}
\tag{16.1}
$$

or

$$
\boxed{
\int_0^{S_0}
\int_{B_{r_0}}
\left(
\Omega\cdot
S_{\mathrm{mid}}
\Omega
\right)_+
dyds
\ge
\frac{c_0}{2}
\mathcal O(r_0).
}
\tag{16.2}
$$

### Proof

If the first alternative fails, Theorem 4.1 gives

$$
\mathcal S_+(r_0)
\ge
\frac{3c_0}{4}
\mathcal O(r_0).
$$

For scalars

$$
a,b,c,
$$

$$
(a+b+c)_+
\le
|a|+b_++|c|.
$$

Apply this to the three strain contributions.

Use (15.1)--(15.2).

Then

$$
\mathcal S_{\mathrm{mid}}^+
\ge
\frac{c_0}{2}
\mathcal O(r_0).
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

# 17. Interpretation

The strict DSS core has only two ways to replenish its periodic enstrophy.

### turnover route

Vorticity/enstrophy is transported inward through the fixed similarity core boundary.

### external-strain route

A finite intermediate annular source supplies positive vortex stretching to the core.

The arbitrarily local and arbitrarily remote pieces can be removed from the leading supplier role.

Thus:

$$
\boxed{
\textbf{
who pulls the filament?}
=
\textbf{
material turnover}
\ \vee\
\textbf{
finite-annulus strain}.
}
\tag{17.1}
$$

---

# 18. Fixed annular source field

Choose a fixed smooth source cutoff

$$
\psi_{\delta,L}
$$

supported in

$$
B_{2L}\setminus B_{\delta/2}.
$$

Define

$$
\boxed{
H(x,s)
=
\int
K(x-y)
\psi_{\delta,L}(y)
\Omega(y,s)dy.
}
\tag{18.1}
$$

For

$$
|x|<\delta/4,
$$

the source is separated from the observation point.

Therefore

$$
H
$$

is smooth in

$$
x.
$$

In the exterior-source Biot--Savart formulation it is componentwise harmonic on the core.

This is the fixed-source harmonic route that is distinct from moving-shell absolute-value decompositions.

---

# 19. Affine strain jet

Define

$$
\boxed{
A(s)
=
H(0,s).
}
\tag{19.1}
$$

Since

$$
H
$$

is a rate-of-strain tensor,

$$
\boxed{
A(s)=A(s)^T,
\qquad
\operatorname{tr}A(s)=0.
}
\tag{19.2}
$$

Thus

$$
\boxed{
A(s)\in\mathrm{Sym}_0(3).
}
\tag{19.3}
$$

The space has dimension

$$
5.
$$

---

# 20. Harmonic Taylor reduction

For

$$
r_0\ll\delta,
$$

$$
\boxed{
H(x,s)
=
A(s)
+
\mathcal R_H(x,s).
}
\tag{20.1}
$$

Kernel differentiation or interior harmonic estimates give

$$
\boxed{
\|\mathcal R_H(\cdot,s)\|_{L^\infty(B_{r_0})}
\le
C
\frac{r_0}{\delta}
\mathcal N_H(s),
}
\tag{20.2}
$$

for a finite annular source norm

$$
\mathcal N_H.
$$

On a compact source-profile class,

$$
\mathcal N_H
$$

is uniformly bounded.

Choose

$$
r_0/\delta
$$

small enough that the Taylor remainder carries at most one quarter of the supplier gap.

---

# 21. NEW THEOREM — External Affine-Jet Supplier

## Theorem 21.1

On the finite-annulus branch of Theorem 16.1, after the fixed-source reduction and sufficiently small core selection,

$$
\boxed{
\int_0^{S_0}
\int_{B_{r_0}}
\left(
\Omega\cdot
A(s)
\Omega
\right)_+
dyds
\ge
c_A
\mathcal O(r_0)
}
\tag{21.1}
$$

for some

$$
c_A>0.
$$

Thus the leading recurrent strain supplier is a nonzero time-periodic tensor

$$
\boxed{
A:
[0,S_0]
\to
\mathrm{Sym}_0(3).
}
\tag{21.2}
$$

### Proof

Write

$$
S_{\mathrm{mid}}
=
H+\text{fixed overlap terms}.
$$

Include the overlap terms in the source norm.

Use

$$
H=A+\mathcal R_H.
$$

The remainder work is bounded by

$$
\|\mathcal R_H\|_\infty
\int|\Omega|^2.
$$

Make it a small fraction of the finite-annulus gap.

The positive part of the affine-jet work carries the remaining amount.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED under the fixed-source compactness hypotheses}.
}
$$

---

# 22. Annular source moment

The affine strain jet is explicitly generated by the finite annulus:

$$
\boxed{
A_{ij}(s)
=
\int
K_{ijm}(-y)
\psi_{\delta,L}(y)
\Omega_m(y,s)dy.
}
\tag{22.1}
$$

Thus it is a finite-dimensional moment of the annular vorticity distribution.

A crude bound is

$$
\boxed{
|A(s)|
\le
C_{\delta,L}
\|\Omega(\cdot,s)\|_{L^2(B_{2L}\setminus B_{\delta/2})}.
}
\tag{22.2}
$$

Hence a uniform positive affine-jet work gap implies a nontrivial annular vorticity reservoir on a compact normalized class.

The supplier cannot be generated by an empty annulus.

---

# 23. Relationship to filtered near-field coercivity

The external filtered-vorticity theorem proves, in the viscous finite-scale setting,

$$
\boxed{
\mathcal V_{\rm near}^{+}
\le
(1-\varepsilon)
\mathcal P
+
C_\varepsilon
M
\mathcal O.
}
\tag{23.1}
$$

After insertion into the exact filtered enstrophy balance, every remaining positive surplus is assigned to:

$$
\boxed{
\text{far-field strain}
\ \vee\
\text{commutator forcing}
\ \vee\
\text{localization}.
}
\tag{23.2}
$$

The same paper shows that fixed exterior-source strain is harmonic on the core and identifies affine jets as the low-order recurrent modes.

DCRP-35 is consistent with this external architecture.

The present theorem is not a replacement for its viscous coercivity estimate.

It is a DSS Euler-periodic replenishment theorem tailored to the final Type-II state.

---

# 24. Correction to the Kelvin--Oseen phrase

The DCRP-34 phrase:

$$
\boxed{
\text{Critical Kelvin--Oseen Equality}
}
$$

is retained only as a **candidate final normal form**.

The exact proven fact at DCRP-34 is:

$$
\boxed{
\text{Kelvin--viscosity scaling compatibility}.
}
$$

DCRP-35 adds:

$$
\boxed{
\text{periodic enstrophy demand}
}
$$

and:

$$
\boxed{
\text{finite-annulus strain supply or turnover}.
}
$$

A genuine Oseen/Burgers-type PDE equality would additionally require a quantitative microviscous diffusion balance.

That is not yet proved.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 25. Why Burgers vortex remains only a calibration

A classical Burgers vortex is maintained by an externally prescribed linear straining flow.

The current DCRP affine tensor

$$
A(s)
$$

has the same **local leading geometry**:

$$
\boxed{
\text{symmetric trace-free external strain}.
}
$$

But in the DCRP branch there is no external forcing.

The tensor

$$
A(s)
$$

must be generated by a finite annulus of the same Navier--Stokes/Euler parent.

Therefore the unresolved question is not:

> can a vortex live in a linear strain?

It can.

The question is:

> can an unforced finite-energy same-parent flow continually reproduce the required linear strain jet from its own recurrent annulus while simultaneously sustaining the Type-II core?

---

# 26. Coupling to DCRP-31 PFET

DCRP-31 proved that the strict DSS state has a finite-radius inward pressure--kinetic matching flux.

DCRP-35 proves that the same strict state has either:

- inward enstrophy turnover; or
- a finite-annulus external strain supplier.

Therefore every strict compact state has a finite matching region carrying

$$
\boxed{
\text{inward PFET}
}
$$

and one of

$$
\boxed{
\text{enstrophy turnover}
\quad\text{or}\quad
\text{external affine strain}.
}
$$

The two witnesses need not occur at exactly the same radius.

By enlarging to one fixed finite annular package, both are contained in a common finite normalized region.

Thus no infinite-tail detector is required.

---

# 27. Compact-class finite jet witness

Let

$$
\mathscr C_{\rm strict}
$$

be a sequentially compact class of normalized strict DSS profiles satisfying:

-:

  $$
  \gamma\in[2/5+\eta,1/2-\eta];
  $$

- uniform local:

  $$
  C^1
  $$

  vorticity bounds;

- uniform critical tail energy envelope;

- fixed recurrent center and pressure gauges;

- normalized core enstrophy:

  $$
  \mathcal O(r_0)\ge o_0>0.
  $$

Then the choices

$$
r_0,\delta,L
$$

can be made uniformly.

There is a fixed constant

$$
c_\ast>0
$$

such that every profile satisfies

$$
\boxed{
\mathcal J_{\omega,\mathrm{in}}
+
\mathcal W_A
\ge
c_\ast,
}
\tag{27.1}
$$

where

$$
\boxed{
\mathcal W_A
=
\int_0^{S_0}
\int_{B_{r_0}}
\left(
\Omega\cdot A(s)\Omega
\right)_+
dyds.
}
\tag{27.2}
$$

Thus the full strain supplier can be represented by:

- one scalar turnover observable;
- one five-component affine strain jet.

This is finite-compiler compatible.

---

# 28. What the affine jet does not prove

A positive

$$
\mathcal W_A
$$

does not imply a positive energy dissipation tax.

The annulus may supply strain and energy in a scale-recurrent conservative fashion.

Likewise:

$$
A(s)\neq0
$$

does not by itself violate finite physical energy because the normalized affine behavior is only local to a shrinking physical core.

Therefore DCRP-35 is a source localization theorem, not a global contradiction.

---

# 29. Same-parent reproduction problem

Under exact DSS recurrence, the annular source distribution itself is linked from return to return by the same-parent scaling map.

The leading tensor

$$
A(s)
$$

must reproduce the same normalized periodic history.

If its source annulus is not recurrent, the failure enters:

$$
\boxed{
\text{scale/spatial/transition carrier}.
}
$$

If it is recurrent, the annular source must reproduce:

$$
\boxed{
A(s+S_0)=A(s)
}
\tag{29.1}
$$

while feeding the inner vortex and the radial PFET matching layer.

This is the new equality branch.

---

# 30. Candidate next decomposition

Write the annular vorticity as

$$
\boxed{
\Omega_{\rm ann}
=
\Omega_{\rm coherent}
+
\Omega_{\rm residual}.
}
\tag{30.1}
$$

The coherent component is the part detected by the five affine-jet moments:

$$
A(s).
$$

The residual component has zero leading strain moment on the core.

The next theorem should ask whether:

- the coherent source pays a scale/pressure transition tax;
- the residual source is geometrically depleted or summably packed;
- or the annulus itself becomes a recurrent Burgers/Oseen-type larger-scale vortex structure.

This creates a finite-rank-plus-residual induction.

---

# 31. A possible hierarchical obstruction

If the core strain is supplied by a coherent annular vortex structure, that annular structure itself requires a strain source to reproduce its vorticity under DSS recurrence.

Thus one may obtain a hierarchy:

$$
\boxed{
\text{core vortex}
\leftarrow
\text{annular strain source}
\leftarrow
\text{larger annular strain source}
\leftarrow\cdots
}
\tag{31.1}
$$

The critical-tail DSS structure is exactly the setting in which such a hierarchy could persist.

The challenge is to prove that this hierarchy:

- produces a non-summable native scale carrier;
- or terminates in a finite affine/harmonic mode;
- or forces spatial/scale escape already retained by MORP/DCRP.

This hierarchical source chain is the next promising closure route.

---

# 32. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Annular Affine-Strain Reproduction /
Unforced Burgers-Jet Closure Lemma}.
}
$$

A useful theorem would prove:

> Let a strict same-parent DSS core have:
>
> $$
> \mathcal J_{\omega,\mathrm{in}}=0
> $$
>
> and a nonzero recurrent external affine strain jet:
>
> $$
> A(s)\in\mathrm{Sym}_0(3).
> $$
>
> Then either:
>
> 1. the annular source producing:
>
>    $$
>    A(s)
>    $$
>
>    has a nonzero scale/spatial transition residual;
>
> 2. the source has a positive strain/model-cone or pressure/PFET payment;
>
> 3. the annular source itself requires a larger-scale recurrent affine strain supplier;
>
> 4. the hierarchy closes into a finite-dimensional globally affine/harmonic mode, excluded by the critical sub-volume energy growth.
>
> If the hierarchy is infinite, prove that the source moments cannot remain compatible with the finite-energy same-parent ancestry.

This is now the most concrete equality-manifold route.

---

# 33. Source-status audit

## Filtered vortex stretching paper

The primary source records the exact Calderon--Zygmund strain kernel:

$$
K(z)\sim|z|^{-3}
$$

with zero spherical average.

It proves that filtered positive near-field stretching is controlled by vorticity-direction increments and can be absorbed by filtered diffusion up to a lower-order enstrophy reservoir.

After insertion into the exact filtered enstrophy balance, every surviving positive surplus is assigned to far-field strain, commutator forcing, or localization.

The paper also separates moving-shell estimates from the fixed-source harmonic route and explicitly identifies affine jets as the leading low-order modes of an exterior-source strain field on a smaller core.

## Constantin--Ignatova--Vicol

The primary source uses the classical vorticity stretching factor, decomposes it into inner and outer pieces, and obtains:

$$
|\alpha_{\rm in}|
\lesssim
R\|\nabla\omega\|_\infty,
$$

while the exterior contribution is controlled from velocity norms after integrating by parts.

This independently calibrates the DCRP-35 near-versus-exterior strain decomposition.

---

# 34. End state

The strict DSS enstrophy identity is

$$
\boxed{
\partial_s
\frac{|\Omega|^2}{2}
+
\nabla\cdot
\left[
(\gamma y+V)
\frac{|\Omega|^2}{2}
\right]
+
(2-3\gamma)
\frac{|\Omega|^2}{2}
=
\Omega\cdot S\Omega.
}
$$

Period averaging gives

$$
\boxed{
(2-3\gamma)\mathcal O
\le
\mathcal S_+
+
\mathcal J_{\omega,\mathrm{in}}.
}
$$

In the strict window,

$$
2-3\gamma>\frac12.
$$

For a smooth critical-tail profile:

$$
\boxed{
S_{<\delta}
=
O(\delta),
}
$$

while

$$
\boxed{
S_{>L}
=
O
\left(
L^{(\kappa-5)/2}
\right).
}
$$

Thus the required positive stretching cannot hide entirely at zero scale or normalized infinity.

It is supplied by a finite intermediate annulus unless enstrophy itself is transported into the core.

On a sufficiently small core the exterior annular strain becomes

$$
\boxed{
A(s)
+
\text{small remainder},
\qquad
A(s)\in\mathrm{Sym}_0(3).
}
$$

Therefore:

$$
\boxed{
\textbf{
strict DSS core}
\Longrightarrow
\textbf{
inward enstrophy turnover}
\ \vee\
\textbf{
finite-annulus affine strain jet}.
}
$$

Together with DCRP-31:

$$
\boxed{
\textbf{
strict compact Type-II}
\Longrightarrow
\textbf{
inward PFET}
+
\left[
\textbf{
enstrophy turnover}
\vee
\textbf{
annular affine strain}
\right].
}
$$

The next single frontier is

$$
\boxed{
\textbf{
Annular Affine-Strain Reproduction /
Unforced Burgers-Jet Closure.
}
}
$$