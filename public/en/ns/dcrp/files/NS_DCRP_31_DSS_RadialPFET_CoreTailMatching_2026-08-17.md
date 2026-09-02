# NS-DCRP-31 — DSS Radial PFET Rigidity, Far-Tail Pressure Decoupling, and the Core-to-Tail Matching Flux

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. attack the DCRP-30 critical-tail DSS Euler survivor;
  2. test the proposed idea that the infinite tail must directly force the core through a large far-field pressure multipole;
  3. prove the exact period-averaged radial energy-flux identity for Euler DSS profiles;
  4. show that a smooth nonzero core cannot connect to the critical DSS tail without a finite-radius inward Euler pressure--kinetic flux;
  5. compress the resulting continuum-radius statement to a finite native PFET witness on compact normalized profile classes;
  6. identify the remaining issue as recurrent critical PFET taxation/summability rather than tail invisibility.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - D. Chae, T.-P. Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414;
  - L. Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619v2;
  - D. Chae, *Euler's equations and the maximum principle*, arXiv:1308.1051;
  - D. Chae, J. Wolf, *On the Discretely Self-similar Solutions to the Euler Equations in R^3*, J. Nonlinear Sci. 33 (2023), 115;
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.
- internal dependencies:
  - DCRP-29 raw-energy atomic/material split;
  - DCRP-30 same-parent DSS recurrence and exponent window;
  - MORP/FCBP pressure--flux--energy--trace observation architecture.
- no novelty/priority claim is made without independent audit.
- several identities below are direct reorganizations of the standard DSS local-energy equation and are likely implicit in the existing DSS Euler literature.

---

# 1. Executive result

DCRP-30 reduced the strict compact same-parent Type-II branch to a smooth Euler DSS profile in the exponent window

$$
\boxed{
1<\alpha<\frac32,
}
\tag{1.1}
$$

equivalently

$$
\boxed{
\frac25<\gamma<\frac12,
\qquad
\gamma=\frac1{1+\alpha},
}
\tag{1.2}
$$

with:

- vanishing raw physical core energy;
- infinite normalized global kinetic energy;
- mandatory global-energy escape to normalized spatial infinity;
- non-outgoing/trapped similarity dynamics;
- no finite-time material crossing;
- no anomalous Navier--Stokes viscous residue;
- no Reynolds/trace/localization defect in the strong compact branch.

The initial DCRP-31 proposal was:

> the infinite DSS tail must exert a non-negligible far-field pressure on the core.

That proposal is false in the natural Calderon--Zygmund pressure class.

Let

$$
\boxed{
\kappa
=
3-2\alpha.
}
\tag{1.3}
$$

In the strict window:

$$
\boxed{
0<\kappa<1.
}
\tag{1.4}
$$

Assume the DSS profile satisfies the Xue-type critical energy envelope

$$
\boxed{
\sup_{s\in[0,S_0]}
\int_{B_R}
|V(y,s)|^2dy
\le
C_E R^\kappa
\qquad
(R\ge1).
}
\tag{1.5}
$$

Assume the pressure is represented by the standard Calderon--Zygmund formula, modulo the declared harmonic/gauge class.

For a fixed core

$$
|y|\le R_0
$$

and tail cutoff

$$
L\gg R_0,
$$

the contribution to the pressure from

$$
|z|\ge L
$$

obeys

$$
\boxed{
\|P_{>L}\|_{
L^\infty(
B_{R_0}\times[0,S_0]
)
}
\le
C
C_E
L^{-2\alpha},
}
\tag{1.6}
$$

and

$$
\boxed{
\|\nabla P_{>L}\|_{
L^\infty(
B_{R_0}\times[0,S_0]
)
}
\le
C
C_E
L^{-1-2\alpha}.
}
\tag{1.7}
$$

Hence

$$
\boxed{
\textbf{
the arbitrarily remote infinite-energy tail can be instantaneously pressure-decoupled from a fixed core.
}
}
\tag{1.8}
$$

The required infinite Euler tail does **not** imply a large direct pressure multipole at the core.

This is the main NO-GO of this round.

The actual unavoidable coupling occurs in the finite-radius **core-to-tail matching layer**.

The Euler DSS similarity variables satisfy

$$
\boxed{
\partial_sV
+
\frac{\alpha}{\alpha+1}V
+
\frac1{\alpha+1}
(y\cdot\nabla)V
+
(V\cdot\nabla)V
+
\nabla P
=
0,
}
\tag{1.9}
$$

$$
\boxed{
\nabla\cdot V=0,
}
\tag{1.10}
$$

with period

$$
S_0.
$$

Define the period-averaged local energy

$$
\boxed{
\mathcal E(R)
=
\int_0^{S_0}
\int_{B_R}
\frac{|V(y,s)|^2}{2}
dyds.
}
\tag{1.11}
$$

Define the period-averaged **physical Euler pressure--kinetic flux** across the fixed similarity sphere:

$$
\boxed{
\mathcal F(R)
=
\int_0^{S_0}
\int_{\partial B_R}
\left(
\frac{|V|^2}{2}
+
P
\right)
V\cdot n
dSds.
}
\tag{1.12}
$$

Then for almost every

$$
R>0,
$$

one has the exact identity

$$
\boxed{
\mathcal F(R)
=
\frac1{\alpha+1}
\left[
\kappa
\mathcal E(R)
-
R\mathcal E'(R)
\right].
}
\tag{1.13}
$$

Equivalently,

$$
\boxed{
\mathcal F(R)
=
-
\frac1{\alpha+1}
R^{\kappa+1}
\frac d{dR}
\left[
R^{-\kappa}
\mathcal E(R)
\right].
}
\tag{1.14}
$$

This is the central exact identity of DCRP-31.

For a smooth core:

$$
\boxed{
\mathcal E(R)=O(R^3)
\qquad
(R\downarrow0).
}
\tag{1.15}
$$

Since:

$$
0<\kappa<1,
$$

$$
\boxed{
R^{-\kappa}
\mathcal E(R)
\to0
\qquad
(R\downarrow0).
}
\tag{1.16}
$$

If:

$$
V\not\equiv0,
$$

there exists a finite:

$$
R_1
$$

with:

$$
\mathcal E(R_1)>0.
$$

Integrating (1.14) from:

$$
0
$$

to:

$$
R_1
$$

gives

$$
\boxed{
\int_0^{R_1}
\left(
-\mathcal F(R)
\right)
R^{-\kappa-1}
dR
=
\frac{
R_1^{-\kappa}
\mathcal E(R_1)
}{
\alpha+1
}.
}
\tag{1.17}
$$

Consequently

$$
\boxed{
\int_0^{R_1}
\left(
-\mathcal F(R)
\right)_+
R^{-\kappa-1}
dR
\ge
\frac{
R_1^{-\kappa}
\mathcal E(R_1)
}{
\alpha+1
}
>
0.
}
\tag{1.18}
$$

Therefore:

$$
\boxed{
\textbf{
every nonzero smooth DSS profile with }\alpha<3/2
\textbf{ has a finite-radius inward period-averaged Euler energy flux.}
}
\tag{1.19}
$$

The sign convention is:

$$
\mathcal F<0
$$

for inward physical pressure--kinetic energy flux across the outward-oriented sphere.

Thus the critical DSS tail cannot be joined to a regular smooth core with all physical PFET channels zero.

This result does **not** require the very remote tail pressure to be large.

The mandatory flux occurs somewhere in the finite core-to-tail transition region.

The exact identity also supplies a rigidity statement.

If

$$
\boxed{
\mathcal F(R)=0
}
\tag{1.20}
$$

for every

$$
R
$$

in an interval:

$$
I,
$$

then:

$$
\boxed{
\mathcal E(R)
=
C_I R^\kappa
\qquad
(R\in I).
}
\tag{1.21}
$$

Thus **zero physical radial flux is equivalent to exact critical power-law energy scaling** on each connected zero-flux interval.

If:

$$
\mathcal F(R)=0
$$

for every:

$$
R>0,
$$

smoothness at the origin forces:

$$
C_I=0,
$$

and hence:

$$
\boxed{
V\equiv0.
}
\tag{1.22}
$$

This eliminates the exact zero-PFET strict DSS strong profile.

A finite compiler version is available.

Let:

$$
\mathscr C_{\rm DSS}
$$

be a sequentially compact normalized class satisfying:

-:

  $$
  \alpha\in
  [1+\delta,3/2-\delta];
  $$

-:

  $$
  \mathcal E(R_1)\ge e_0>0;
  $$

- a uniform local smoothness bound near the core;
- fixed translation/pressure gauges.

Then there exists:

$$
\boxed{
0<R_0<R_1
}
\tag{1.23}
$$

and:

$$
\boxed{
c_{\rm PFET}>0
}
\tag{1.24}
$$

such that every profile in:

$$
\mathscr C_{\rm DSS}
$$

satisfies

$$
\boxed{
\int_{R_0}^{R_1}
\left(
-\mathcal F(R)
\right)_+
R^{-\kappa-1}
dR
\ge
c_{\rm PFET}.
}
\tag{1.25}
$$

Thus one fixed finite annular radial PFET observation detects every nonzero compact strict DSS strong profile.

No infinite radius family is needed in the compiler.

This gives:

$$
\boxed{
\textbf{
strict compact same-parent DSS}
+
\textbf{
zero PFET}
=
\varnothing.
}
\tag{1.26}
$$

provided the native PFET package includes the finite annular radial aggregate above, or an equivalent smooth-cutoff realization.

The remaining difficulty is **not visibility**.

It is taxation/summability.

A DSS cascade may repeat a fixed normalized inward flux while the corresponding raw physical energy transfer decreases geometrically with scale.

Indeed:

$$
\beta_{n+1}
\sim
q_\ast\beta_n,
\qquad
0<q_\ast<1
$$

in the strict geometric atom-free branch.

Therefore:

$$
\boxed{
\sum_n\beta_n<\infty
}
\tag{1.27}
$$

is compatible with infinitely many normalized PFET events.

Thus:

$$
\boxed{
\textbf{
fixed normalized inward PFET per return}
\not\Rightarrow
\textbf{
global physical-energy contradiction}.
}
\tag{1.28}
$$

The old critical-summability barrier survives.

However the final state obstruction has now been reduced from:

$$
\text{tail-fed DSS Euler profile}
$$

to:

$$
\boxed{
\textbf{
scale-recurrent inward-PFET DSS cascade}.
}
\tag{1.29}
$$

The next exact frontier is therefore:

$$
\boxed{
\textbf{
Same-Parent DSS PFET Return-Depletion /
Critical Flux Summability Lemma}.
}
\tag{1.30}
$$

The question is now:

> can the exact same-parent discrete return convert the mandatory inward PFET matching-layer flux into a strict normalized return tax, rather than merely a geometrically summable raw energy transfer?

This is narrower than a tail-pressure or Euler-Liouville problem.

---

# 2. External DSS similarity equation

For backward Euler DSS with exponent:

$$
\alpha>-1,
$$

the similarity variables are:

$$
y
=
(-t)^{-1/(\alpha+1)}x,
$$

and a logarithmic time:

$$
s.
$$

The profile is periodic in:

$$
s
$$

and satisfies:

$$
\boxed{
\partial_sV
+
aV
+
b(y\cdot\nabla)V
+
(V\cdot\nabla)V
+
\nabla P
=
0,
}
\tag{2.1}
$$

where:

$$
\boxed{
a
=
\frac{\alpha}{\alpha+1},
}
\tag{2.2}
$$

and:

$$
\boxed{
b
=
\frac1{\alpha+1}.
}
\tag{2.3}
$$

The profile is divergence free.

This is the standard Chae--Tsai/Xue DSS profile equation.

---

# 3. Tail energy exponent

Define:

$$
\boxed{
\kappa
=
3-2\alpha.
}
\tag{3.1}
$$

In the DCRP strict Type-II window:

$$
1<\alpha<3/2,
$$

so:

$$
\boxed{
0<\kappa<1.
}
\tag{3.2}
$$

Xue's admissible nontrivial DSS profile classes exhibit or are bounded by the critical energy law:

$$
\boxed{
\mathcal E(R)
\sim
R^\kappa
}
\tag{3.3}
$$

under the corresponding global integrability/regularity assumptions.

DCRP-31 does not assume the lower asymptotic unless explicitly stated.

For the pressure-tail NO-GO, only the upper envelope:

$$
\sup_s
\int_{B_R}|V|^2
\le
C_ER^\kappa
$$

is used.

---

# 4. Conditional far-tail pressure decomposition

Assume the pressure is in the standard Calderon--Zygmund representation class:

$$
\boxed{
P(y,s)
=
-\frac13|V(y,s)|^2
+
\operatorname{p.v.}
\int
K_{ij}(y-z)
V_i(z,s)V_j(z,s)dz
}
\tag{4.1}
$$

up to the declared pressure gauge/harmonic class.

The kernel satisfies:

$$
\boxed{
|K(z)|
\le
C|z|^{-3},
}
\tag{4.2}
$$

and:

$$
\boxed{
|\nabla K(z)|
\le
C|z|^{-4}.
}
\tag{4.3}
$$

For a core:

$$
|y|\le R_0
$$

and:

$$
L\ge4R_0,
$$

define the remote tail:

$$
\boxed{
P_{>L}(y,s)
=
\int_{|z|>L}
K_{ij}(y-z)
V_i(z,s)V_j(z,s)dz.
}
\tag{4.4}
$$

Any harmonic/gauge terms are handled separately in the declared pressure package.

---

# 5. NEW THEOREM — Far-Tail Pressure Decoupling

## Theorem 5.1

Assume:

$$
\boxed{
\sup_s
\int_{B_R}
|V(y,s)|^2dy
\le
C_E R^\kappa
}
\tag{5.1}
$$

for all:

$$
R\ge1,
$$

with:

$$
0<\kappa<3.
$$

Then for every fixed:

$$
R_0
$$

and:

$$
L\ge4R_0,
$$

$$
\boxed{
\sup_s
\|P_{>L}(\cdot,s)\|_{L^\infty(B_{R_0})}
\le
C
C_E
L^{\kappa-3}.
}
\tag{5.2}
$$

Also:

$$
\boxed{
\sup_s
\|\nabla P_{>L}(\cdot,s)\|_{L^\infty(B_{R_0})}
\le
C
C_E
L^{\kappa-4}.
}
\tag{5.3}
$$

For:

$$
\kappa=3-2\alpha,
$$

this becomes:

$$
\boxed{
P_{>L}
=
O(L^{-2\alpha}),
}
\tag{5.4}
$$

and:

$$
\boxed{
\nabla P_{>L}
=
O(L^{-1-2\alpha}).
}
\tag{5.5}
$$

### Proof

Decompose the remote region into dyadic shells:

$$
A_j
=
\left\{
2^jL
<
|z|
\le
2^{j+1}L
\right\}.
$$

For:

$$
|y|\le R_0,
$$

and:

$$
z\in A_j,
$$

$$
|y-z|
\ge
c2^jL.
$$

Therefore:

$$
\begin{aligned}
|P_{>L}(y,s)|
&\le
C
\sum_{j\ge0}
(2^jL)^{-3}
\int_{A_j}
|V(z,s)|^2dz
\\
&\le
C
C_E
\sum_{j\ge0}
(2^jL)^{-3}
(2^{j+1}L)^\kappa
\\
&\le
C
C_E
L^{\kappa-3}
\sum_{j\ge0}
2^{-j(3-\kappa)}.
\end{aligned}
$$

The geometric series converges because:

$$
\kappa<3.
$$

The gradient bound is identical with:

$$
|K|
$$

replaced by:

$$
|\nabla K|.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED under the stated pressure-representation and energy-envelope assumptions}.
}
$$

---

# 6. Consequence — remote tail work is not the unavoidable coupling

Let:

$$
\chi
$$

be a fixed core cutoff.

If:

$$
V
$$

is locally bounded in the core, then:

$$
\boxed{
\left|
\int_0^{S_0}
\int
P_{>L}
V\cdot\nabla\chi
dyds
\right|
\le
C_\chi
L^{-2\alpha}.
}
\tag{6.1}
$$

Thus:

$$
\boxed{
\textbf{
the arbitrarily remote tail cannot be forced to provide a fixed material pressure-work payment.
}
}
\tag{6.2}
$$

This invalidates the strongest form of the DCRP-30 tail-pressure proposal.

The coupling must be sought at finite relative radius or through scale recurrence.

---

# 7. Exact DSS local energy equation

Set:

$$
\boxed{
e
=
\frac12
|V|^2.
}
\tag{7.1}
$$

Dot (2.1) with:

$$
V.
$$

Using:

$$
\nabla\cdot V=0,
$$

$$
V\cdot
(V\cdot\nabla V)
=
\nabla\cdot(eV),
$$

and:

$$
V\cdot\nabla P
=
\nabla\cdot(PV),
$$

one gets:

$$
\partial_se
+
2ae
+
b
y\cdot\nabla e
+
\nabla\cdot
\left[
(e+P)V
\right]
=
0.
$$

Since:

$$
y\cdot\nabla e
=
\nabla\cdot(ye)
-
3e,
$$

$$
\boxed{
\partial_se
+
\nabla\cdot
\left[
bye
+
(e+P)V
\right]
+
(2a-3b)e
=
0.
}
\tag{7.2}
$$

But:

$$
\boxed{
2a-3b
=
-\frac{
3-2\alpha
}{
\alpha+1
}
=
-b\kappa.
}
\tag{7.3}
$$

Thus:

$$
\boxed{
\partial_se
+
\nabla\cdot
\left[
bye
+
(e+P)V
\right]
-
b\kappa e
=
0.
}
\tag{7.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Period-averaged local energy

Define:

$$
\boxed{
\mathcal E(R)
=
\int_0^{S_0}
\int_{B_R}
e
dyds.
}
\tag{8.1}
$$

For almost every:

$$
R,
$$

coarea gives:

$$
\boxed{
\mathcal E'(R)
=
\int_0^{S_0}
\int_{\partial B_R}
e
dSds.
}
\tag{8.2}
$$

Define the physical Euler energy current flux:

$$
\boxed{
\mathcal F(R)
=
\int_0^{S_0}
\int_{\partial B_R}
(e+P)
V\cdot n
dSds.
}
\tag{8.3}
$$

Because the profile is periodic:

$$
e(y,S_0)=e(y,0).
$$

Integrate (7.4) over:

$$
B_R\times[0,S_0].
$$

The time derivative vanishes.

The similarity-drift boundary term is:

$$
\boxed{
bR
\mathcal E'(R).
}
\tag{8.4}
$$

Therefore:

$$
\boxed{
bR
\mathcal E'(R)
+
\mathcal F(R)
-
b\kappa
\mathcal E(R)
=
0.
}
\tag{8.5}
$$

---

# 9. NEW THEOREM — DSS Radial PFET Identity

## Theorem 9.1

For almost every:

$$
R>0,
$$

$$
\boxed{
\mathcal F(R)
=
b
\left[
\kappa
\mathcal E(R)
-
R
\mathcal E'(R)
\right],
}
\tag{9.1}
$$

where:

$$
b
=
1/(\alpha+1).
$$

Equivalently:

$$
\boxed{
\mathcal F(R)
=
-
b
R^{\kappa+1}
\frac d{dR}
\left[
R^{-\kappa}
\mathcal E(R)
\right].
}
\tag{9.2}
$$

### Proof

Equation (9.1) is (8.5).

For:

$$
G(R)
=
R^{-\kappa}
\mathcal E(R),
$$

$$
G'(R)
=
R^{-\kappa-1}
\left[
R\mathcal E'(R)
-
\kappa\mathcal E(R)
\right].
$$

Substitute.

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

# 10. Smooth-core behavior

Suppose:

$$
V
$$

is locally bounded near:

$$
y=0
$$

uniformly over one period.

Then:

$$
\boxed{
\mathcal E(R)
\le
C
R^3.
}
\tag{10.1}
$$

For:

$$
0<\kappa<3,
$$

$$
\boxed{
R^{-\kappa}
\mathcal E(R)
\to0
}
\tag{10.2}
$$

as:

$$
R\downarrow0.
$$

In the DCRP strict DSS window:

$$
0<\kappa<1,
$$

so the conclusion applies.

---

# 11. NEW THEOREM — Core-to-Tail Inward PFET Gap

## Theorem 11.1

Let:

$$
V
$$

be a smooth nonzero:

$$
S_0
$$

-periodic DSS Euler profile with:

$$
\alpha<3/2.
$$

Let:

$$
R_1
$$

satisfy:

$$
\mathcal E(R_1)>0.
$$

Then:

$$
\boxed{
\int_0^{R_1}
\left(
-\mathcal F(R)
\right)_+
R^{-\kappa-1}
dR
\ge
\frac{
R_1^{-\kappa}
\mathcal E(R_1)
}{
\alpha+1
}
>
0.
}
\tag{11.1}
$$

Consequently:

$$
\boxed{
\mathcal F(R)<0
}
\tag{11.2}
$$

on a set of positive measure in:

$$
(0,R_1).
$$

### Proof

By Theorem 9.1:

$$
\frac d{dR}
\left[
R^{-\kappa}
\mathcal E(R)
\right]
=
-(\alpha+1)
\mathcal F(R)
R^{-\kappa-1}.
$$

Integrate from:

$$
0
$$

to:

$$
R_1.
$$

The lower endpoint vanishes by Section 10:

$$
R^{-\kappa}\mathcal E(R)\to0.
$$

Hence:

$$
R_1^{-\kappa}
\mathcal E(R_1)
=
(\alpha+1)
\int_0^{R_1}
\left(
-\mathcal F(R)
\right)
R^{-\kappa-1}
dR.
$$

The positive part of:

$$
-\mathcal F
$$

dominates the signed integral.

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

# 12. Interpretation of the sign

The sphere normal:

$$
n
$$

points outward.

The physical Euler energy current is:

$$
(e+P)V.
$$

Therefore:

$$
\boxed{
\mathcal F(R)<0
}
$$

means net period-averaged **inward** pressure--kinetic energy flux through:

$$
\partial B_R.
$$

Thus a nonzero smooth DSS core in:

$$
\alpha<3/2
$$

cannot be sustained by pure similarity drift alone at every radius.

Some finite matching layer imports physical Euler energy into the core.

---

# 13. Zero-flux rigidity

Suppose:

$$
\boxed{
\mathcal F(R)=0
}
\tag{13.1}
$$

for almost every:

$$
R
$$

in a connected interval:

$$
I.
$$

Then Theorem 9.1 gives:

$$
\boxed{
\frac d{dR}
\left[
R^{-\kappa}
\mathcal E(R)
\right]
=
0
}
\tag{13.2}
$$

on:

$$
I.
$$

Hence:

$$
\boxed{
\mathcal E(R)
=
C_I
R^\kappa
}
\tag{13.3}
$$

on:

$$
I.
$$

Thus zero radial physical PFET is equivalent to exact critical energy scaling on that interval.

If:

$$
\mathcal F(R)=0
$$

for all:

$$
R>0,
$$

smooth-core behavior forces:

$$
C_I=0,
$$

and:

$$
\boxed{
V\equiv0.
}
\tag{13.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Why the critical tail can be asymptotically flux-silent

Suppose formally:

$$
\mathcal E(R)
\sim
C
R^\kappa
$$

at large:

$$
R.
$$

Then the two terms:

$$
\kappa\mathcal E(R)
$$

and:

$$
R\mathcal E'(R)
$$

have the same leading order.

Therefore:

$$
\mathcal F(R)
$$

can be lower order at large radius.

This is compatible with:

- Xue's critical tail energy law;
- the remote pressure-decoupling estimate.

Hence the theorem does **not** force a large PFET at arbitrarily large radius.

It forces a finite **matching transition** between:

$$
O(R^3)
$$

smooth-core energy and:

$$
O(R^\kappa)
$$

critical-tail energy.

---

# 15. Uniform annular gap on a compact DSS class

Let:

$$
\mathscr C_{\rm DSS}
$$

be sequentially compact in a topology giving uniform local:

$$
C^0
$$

control and continuous local energy/flux functionals.

Assume:

$$
\boxed{
\alpha
\in
[1+\delta,3/2-\delta]
}
\tag{15.1}
$$

for a fixed:

$$
\delta>0.
$$

Assume a normalized nontriviality condition:

$$
\boxed{
\mathcal E(R_1)
\ge
e_0>0
}
\tag{15.2}
$$

for one fixed:

$$
R_1.
$$

Uniform local boundedness gives:

$$
\mathcal E(R)
\le
C_0R^3.
$$

Because:

$$
\kappa
\le
1-2\delta
$$

and:

$$
\kappa
\ge
2\delta,
$$

one may choose:

$$
R_0>0
$$

so small that uniformly:

$$
\boxed{
R_0^{-\kappa}
\mathcal E(R_0)
\le
\frac12
R_1^{-\kappa}
e_0.
}
\tag{15.3}
$$

---

# 16. NEW THEOREM — Finite-Annulus PFET Compiler Gap

## Theorem 16.1

Under Section 15 there is:

$$
c_{\rm PFET}>0
$$

such that every:

$$
V\in
\mathscr C_{\rm DSS}
$$

satisfies:

$$
\boxed{
\int_{R_0}^{R_1}
\left(
-\mathcal F(R)
\right)_+
R^{-\kappa-1}
dR
\ge
c_{\rm PFET}.
}
\tag{16.1}
$$

A possible uniform value is:

$$
\boxed{
c_{\rm PFET}
=
\frac{
e_0
}{
2
(\alpha_{\max}+1)
R_1^{\kappa_{\max}}
},
}
\tag{16.2}
$$

after replacing the exponent factors by their compact-interval worst cases.

### Proof

Integrate Theorem 9.1 from:

$$
R_0
$$

to:

$$
R_1.
$$

Then:

$$
(\alpha+1)
\int_{R_0}^{R_1}
(-\mathcal F)
R^{-\kappa-1}dR
=
R_1^{-\kappa}
\mathcal E(R_1)
-
R_0^{-\kappa}
\mathcal E(R_0).
$$

Use:

$$
\mathcal E(R_1)\ge e_0
$$

and (15.3).

The positive part dominates the signed integral.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED under the compact-class hypotheses}.
}
$$

---

# 17. Smooth-cutoff realization

The radius-integrated flux functional is native.

By Fubini/coarea, an integral of:

$$
\mathcal F(R)
$$

against a smooth compact radial weight can be rewritten as a spacetime integral of the Euler energy current against the gradient of one radial test function.

Thus the annular aggregate may be compiled as a standard pressure--flux finite-window observable:

$$
\boxed{
\iint
\left(
e+P
\right)
V\cdot\nabla\Phi
dyds.
}
\tag{17.1}
$$

The singular model weight:

$$
R^{-\kappa-1}
$$

is used only to derive the coercive lower bound.

Once:

$$
R_0>0
$$

is fixed, it can be replaced by a smooth equivalent weight on:

$$
[R_0,R_1].
$$

Therefore no continuum of independent detectors is required.

---

# 18. Translation and pressure gauges

Pressure constants do not affect:

$$
\mathcal F(R)
$$

because:

$$
\int_{\partial B_R}
V\cdot n
=
0.
$$

Rigid spatial translations/center drift are handled before the DSS profile is placed in the fixed recurrent chart.

If a moving center does not converge, it belongs to the transition/spatial-escape branch of DCRP-30.

Thus the radial PFET gap is evaluated only after the declared same-parent center gauge has been fixed.

---

# 19. Strict compact zero-PFET DSS branch excluded

Suppose the DCRP strict same-parent DSS profile is:

- compact/strong;
- nonzero;
- smooth on the core;
-:

  $$
  1<\alpha<3/2;
  $$

- transition-parameter tight;
- in the finite PFET compiler class.

If the native pressure--flux observation vanishes on the entire declared annular aggregate:

$$
\boxed{
\mathsf O_{\rm PFET}^{rad}=0,
}
\tag{19.1}
$$

Theorem 16.1 gives a contradiction.

Therefore:

$$
\boxed{
\textbf{
strict compact DSS strong profile}
\cap
\ker
\mathsf O_{\rm PFET}^{rad}
=
\varnothing.
}
\tag{19.2}
$$

Status:

$$
\boxed{
\textbf{PROVED after the radial PFET coordinate is declared in the finite compiler}.
}
$$

This is a genuine M-RIG exclusion of the strict compact DSS zero-observation kernel.

---

# 20. Relation to the existing DSS literature

The local-energy arguments of Chae--Tsai and Xue already show that pressure--velocity flux terms control the radial energy behavior of DSS profiles.

DCRP-31 does not claim priority for the underlying local-energy mechanism.

The project-specific contribution is to package the exact period-averaged radial identity into the MORP/DCRP obstruction compiler and to interpret it as the mandatory core-to-tail matching PFET of the same-parent Type-II branch.

---

# 21. Far-tail pressure NO-GO versus matching-layer PFET

The two new theorems are complementary:

$$
\boxed{
\text{remote tail pressure}
\to0
}
\tag{21.1}
$$

on every fixed core as the tail cutoff tends to infinity,

but:

$$
\boxed{
\text{finite matching-layer inward PFET}
>
0.
}
\tag{21.2}
$$

Thus the final coupling is not:

> the infinite tail acts like a large distant pressure source.

It is:

> the DSS energy geometry forces a finite-radius physical transfer layer connecting the smooth core to the critical tail.

This is a sharper mechanism statement.

---

# 22. Critical raw scaling of the matching payment

In the strict geometric Type-II recurrence:

$$
\boxed{
\beta_{n+1}
=
q_\ast
\beta_n
+
o(\beta_n),
\qquad
0<q_\ast<1.
}
\tag{22.1}
$$

A fixed normalized PFET amount at profile level corresponds to a raw physical kinetic-energy transfer of order:

$$
\boxed{
\beta_n.
}
\tag{22.2}
$$

Hence:

$$
\boxed{
\sum_{n=0}^{\infty}
\beta_n
<
\infty.
}
\tag{22.3}
$$

Therefore infinitely many mandatory normalized inward-flux events are compatible with a finite raw kinetic-energy budget.

This is the same critical-summability phenomenon encountered earlier in shell/supplier form.

Status:

$$
\boxed{
\textbf{NO-GO to a naive global energy summation contradiction}.
}
$$

---

# 23. Visibility versus return depletion revisited

DCRP-31 proves:

$$
\boxed{
\text{strict compact DSS recurrence}
\Longrightarrow
\text{positive normalized PFET visibility}.
}
\tag{23.1}
$$

It does **not** yet prove:

$$
\boxed{
\mathfrak J(
T_{\rm ret}D
)
+
c_{\rm PFET}
\le
\mathfrak J(D).
}
\tag{23.2}
$$

The recurrent DSS state may be continuously refueled from the critical tail.

Thus:

$$
\boxed{
\textbf{
mandatory PFET visibility}
\neq
\textbf{
strict return depletion}.
}
\tag{23.3}
$$

This is the exact remaining global issue.

---

# 24. Marginal exponent branches

The uniform compact gap of Theorem 16.1 was stated away from:

$$
\alpha=1
$$

and:

$$
\alpha=3/2.
$$

The exact radial identity itself remains valid at both endpoints.

However the Type-II interpretation changes.

### alpha = 1

$$
\gamma=1/2
$$

and the amplitude ratio is asymptotically neutral.

### alpha = 3/2

$$
\gamma=2/5,
\qquad
\kappa=0.
$$

The identity becomes:

$$
\boxed{
\mathcal F(R)
=
-\frac{2}{5}
R
\mathcal E'(R)
}
\tag{24.1}
$$

with no positive bulk similarity-energy coefficient.

This is the energy-conserving similarity endpoint and requires separate treatment.

Therefore the strongest new strict result concerns:

$$
\boxed{
1<\alpha<3/2.
}
$$

---

# 25. Noncompact / weak DSS branch

The inward PFET theorem uses a genuine smooth/strong DSS profile.

If the same-parent recurrence produces only:

- a generalized Young profile;
- Reynolds defect;
- spatial/scale splitting;
- transition escape;

then the profile is already in an explicit noncompact defect branch from DCRP-24/30.

No attempt is made to apply the smooth radial identity without the required regularity.

---

# 26. Updated strict Type-II normal form

The DCRP-30 strict compact state:

$$
\boxed{
\text{tail-fed}
+
\text{non-outgoing}
+
\text{infinite-energy}
+
\text{DSS}
}
$$

is now further reduced to:

$$
\boxed{
\textbf{
scale-recurrent DSS state with a mandatory finite-radius inward PFET matching layer}.
}
\tag{26.1}
$$

The arbitrarily remote tail can be pressure-decoupled.

The matching layer cannot.

---

# 27. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Same-Parent DSS PFET Return-Depletion /
Critical Flux Summability Lemma}.
}
$$

A useful theorem would show:

> Let:
>
> $$
> D_n
> $$
>
> be the same-parent strict DSS return chain with mandatory normalized inward PFET:
>
> $$
> \mathsf{PFET}_n
> \ge
> c_\ast>0.
> $$
>
> Then either:
>
> 1. the inward PFET produces a strict nonrecoverable return tax after one full DSS period;
> 2. its replenishment requires a nonzero tail/scale transition carrier already counted in:
>
>    $$
>    \mathsf R_{\rm nat};
>    $$
>
> 3. the recurrence is exactly conservative in a critical tail channel, in which case classify the resulting equality solution and test it against known DSS/pressure/outgoing rigidity.

The third branch is the equality-manifold route.

This is the correct next attack.

---

# 28. A candidate equality quantity

Define:

$$
\boxed{
G(R)
=
R^{-\kappa}
\mathcal E(R).
}
\tag{28.1}
$$

Then:

$$
\boxed{
G'(R)
=
-(\alpha+1)
\mathcal F(R)
R^{-\kappa-1}.
}
\tag{28.2}
$$

Thus:

- inward PFET:

  $$
  \mathcal F<0
  $$

  makes:

  $$
  G'>0;
  $$

- outward PFET:

  $$
  \mathcal F>0
  $$

  makes:

  $$
  G'<0.
  $$

The critical tail corresponds to:

$$
G(R)
$$

approaching or oscillating around a positive scale-recurrent level.

Therefore a full DSS return with zero net depletion requires an exact balance of the signed radial PFET in logarithmic radius.

This suggests a scale-logarithmic transport ledger:

$$
\boxed{
d\log R
}
$$

rather than a raw physical-energy sum.

Whether this can generate a non-summable normalized return tax is the next unresolved calculation.

---

# 29. Source-status audit

## Chae--Tsai

The paper gives the Euler DSS scaling law, the periodic similarity equation, and local-energy identities involving:

$$
|V|^3
+
|P||V|.
$$

It proves several DSS nonexistence criteria under velocity/vorticity integrability and decay assumptions.

## Xue

The paper extends the DSS local-energy analysis to non-decaying profiles and gives pressure representation formulae appropriate to nonstandard spatial asymptotics.

It proves the critical energy behavior:

$$
R^{3-2\alpha}
$$

in its admissible nontrivial profile classes.

DCRP-31 uses this as a tail calibration and derives a conditional remote-pressure estimate from the Calderon--Zygmund kernel.

## Constantin--Ignatova--Vicol

The outgoing self-similar guardrail:

$$
\gamma\ge1/2
$$

continues to force the strict DCRP profile:

$$
\gamma<1/2
$$

into non-outgoing/trapped Lagrangian behavior.

This is compatible with the new matching-layer flux theorem and does not eliminate it.

---

# 30. End state

The tail-pressure proposal has been corrected:

$$
\boxed{
\textbf{
infinite DSS tail}
\not\Rightarrow
\textbf{
large direct far-tail pressure on the core}.
}
$$

Under the critical energy envelope:

$$
\boxed{
P_{>L}
=
O(L^{-2\alpha}),
\qquad
\nabla P_{>L}
=
O(L^{-1-2\alpha}).
}
$$

The unavoidable coupling is instead the exact radial PFET identity:

$$
\boxed{
\mathcal F(R)
=
-
\frac1{\alpha+1}
R^{\kappa+1}
\frac d{dR}
\left[
R^{-\kappa}
\mathcal E(R)
\right].
}
$$

A smooth core has:

$$
R^{-\kappa}\mathcal E(R)\to0,
$$

while a nonzero DSS profile has positive local energy at finite radius.

Hence:

$$
\boxed{
\int
(-\mathcal F)_+
R^{-\kappa-1}dR
>
0.
}
$$

Thus every nonzero strict compact DSS profile has a finite-radius inward physical pressure--kinetic matching flux.

On a compact normalized class this becomes a uniform finite-annulus PFET gap.

Therefore:

$$
\boxed{
\textbf{
strict compact DSS zero-PFET branch is excluded}.
}
$$

But the raw physical payments may be geometrically summable:

$$
\sum_n\beta_n<\infty.
$$

The remaining problem is therefore not tail visibility.

It is:

$$
\boxed{
\textbf{
Same-Parent DSS PFET Return-Depletion /
Critical Flux Summability.
}
}
$$