# NS-DCRP-44 — Coarea No-Go, Slice-Mean Gauge Completion, and the Sheet-Interface / Plateau-Escape Dichotomy

- date: 2026-08-17
- status: research proof checkpoint / sheet-interface correction-and-reduction round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. test whether the DCRP-43 infinite scalar reservoir alone forces infinite physical planar vorticity;
  2. prove a kinematic NO-GO showing that infinite scalar superlevel measure can coexist with finite horizontal-gradient cost;
  3. audit point-anchor gauge coercivity in horizontal dimension two;
  4. replace the point anchor as the coercive local gauge by a slice-mean-zero projection;
  5. derive exact Poincaré control by the physical planar vorticity;
  6. derive a relative-isoperimetric/coarea lower bound for balanced scalar plateaus;
  7. obtain a finite sheet-interface enstrophy gap on compact strong-profile classes;
  8. classify all escapes from the interface gap as plateau domination, interface escape, interface concentration, or slice intermittency;
  9. derive an exact level-set coarea-density cocycle for the global pure Poincaré scalar branch;
  10. identify the next frontier as cocycle-aware interface replication rather than raw coarea.
- no full Navier--Stokes regularity claim is made.
- external calibration:
  - A. Enciso, A. J. Fernández, D. Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233;
  - E. Miller, *A locally anisotropic regularity criterion for the Navier--Stokes equation in terms of vorticity*, arXiv:2002.02152.
- internal dependencies:
  - DCRP-40 planar potential--shear representation;
  - DCRP-42 planar shear scalar turnover;
  - DCRP-43 anchored shear Poincaré cocycle and infinite-superlevel reservoir.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction

DCRP-43 proved that on the global pure anchored pancake cocycle branch, for every positive scalar threshold

$$
\tau>0,
$$

the superlevel set

$$
\boxed{
E_\tau
=
\left\{
|\widetilde r|>\tau
\right\}
}
\tag{1.1}
$$

satisfies

$$
\boxed{
|E_\tau|
\in
\{0,\infty\}.
}
\tag{1.2}
$$

For every nonzero continuous pure scalar profile, every sufficiently small positive threshold has

$$
\boxed{
|E_\tau|=\infty.
}
\tag{1.3}
$$

DCRP-43 proposed the next bridge:

$$
\boxed{
\text{infinite scalar reservoir}
\stackrel{?}{\Longrightarrow}
\text{large sheet-interface / planar-vorticity cost}.
}
\tag{1.4}
$$

DCRP-44 proves that this implication is false without additional geometric information.

The scalar reservoir can have infinite measure while the horizontal gradient remains finite in both

$$
L^1
$$

and

$$
L^2.
$$

Thus:

$$
\boxed{
\textbf{
raw coarea alone cannot close the infinite-sheet reservoir.
}
}
\tag{1.5}
$$

This is the first central correction.

The correct local coercive gauge is not the point anchor.

It is the **slice-mean-zero projection**.

For a fixed horizontal disk

$$
D_R\subset\mathbb R^2,
$$

define

$$
\boxed{
\Pi_R q
=
q
-
\fint_{D_R}q\,dx_h.
}
\tag{1.6}
$$

Under the slice gauge

$$
q\mapsto q-h(z,s),
$$

$$
\Pi_R q
$$

is unchanged.

Moreover

$$
\boxed{
\nabla_h\Pi_Rq
=
\nabla_hq
=
-J\Omega_h.
}
\tag{1.7}
$$

Poincaré gives

$$
\boxed{
\|\Pi_Rq\|_{L^2(D_R)}
\le
C R
\|\Omega_h\|_{L^2(D_R)}.
}
\tag{1.8}
$$

Thus the nonconstant scalar content on a fixed recurrent slice is genuinely controlled by the physical planar vorticity.

The second central result is a balanced-interface theorem.

Let

$$
u=\Pi_Rq
$$

on one horizontal disk and suppose

$$
\boxed{
\fint_{D_R}u=0,
\qquad
\|u\|_{L^\infty(D_R)}
\le
M.
}
\tag{1.9}
$$

If for some

$$
0<\tau\le M
$$

the positive plateau occupies a fixed fraction

$$
\boxed{
\left|
\{u>\tau\}
\right|
\ge
\theta
|D_R|,
\qquad
0<\theta<1,
}
\tag{1.10}
$$

then mean zero forces a nontrivial opposite-sign set.

Relative isoperimetry plus coarea gives

$$
\boxed{
\int_{D_R}
|\Omega_h|
dx_h
=
\int_{D_R}
|\nabla_hu|
dx_h
\ge
c
R\tau
\sqrt{
\theta
\min
\left(
1,\frac{\tau}{M}
\right)
}.
}
\tag{1.11}
$$

Consequently

$$
\boxed{
\int_{D_R}
|\Omega_h|^2dx_h
\ge
c
\tau^2
\theta
\min
\left(
1,\frac{\tau}{M}
\right).
}
\tag{1.12}
$$

When

$$
\tau\le M,
$$

this may be written

$$
\boxed{
\int_{D_R}
|\Omega_h|^2dx_h
\ge
c
\theta
\frac{\tau^3}{M}.
}
\tag{1.13}
$$

Thus a nontrivial plateau which occupies a fixed slice fraction cannot have a free interface.

It carries a finite physical planar-vorticity gap.

The third central result is the corrected sheet-reservoir branch tree.

An infinite scalar reservoir can avoid the balanced interface gap only if, on the relevant recurrent slices, it becomes **plateau dominated**.

That degeneration can occur only through one or more of:

1. **interface escape**:

   the active level-set boundary moves to arbitrarily large normalized horizontal radius;

2. **interface concentration**:

   the transition layer becomes arbitrarily thin or geometrically concentrated;

3. **slice intermittency**:

   the active interface occupies a vanishing fraction of the normal/time slices;

4. **zero-mode domination**:

   most of the scalar amplitude is carried by a nearly constant slice mode, with the physical vorticity confined to a small compensating interface set.

Thus the correct conclusion is

$$
\boxed{
\textbf{
infinite scalar reservoir}
\Longrightarrow
\textbf{
finite sheet-interface carrier}
\ \vee\
\textbf{
plateau/interface degeneration}.
}
\tag{1.14}
$$

This is substantially weaker than a direct coarea contradiction, but it is quotient-safe and physically meaningful.

The fourth result supplies a cocycle-aware geometric observable.

On the global pure DCRP-43 branch,

$$
\boxed{
\widetilde r(\Phi a)
=
\mu_r
\widetilde r(a),
}
\tag{1.15}
$$

with

$$
\boxed{
\mu_r
=
e^{(1-2\gamma)S_0}
>
1,
}
\tag{1.16}
$$

and

$$
\boxed{
J_\Phi
=
\det D\Phi
=
e^{3\gamma S_0}.
}
\tag{1.17}
$$

For a regular positive level

$$
\Sigma_\tau
=
\{\widetilde r=\tau\},
$$

one has

$$
\boxed{
\Phi(\Sigma_\tau)
=
\Sigma_{\mu_r\tau}.
}
\tag{1.18}
$$

Differentiating the scalar cocycle gives

$$
\boxed{
\nabla\widetilde r(\Phi a)
=
\mu_r
D\Phi(a)^{-T}
\nabla\widetilde r(a).
}
\tag{1.19}
$$

The surface Jacobian is

$$
\boxed{
J_{\Sigma}\Phi
=
J_\Phi
\left|
D\Phi^{-T}n_\Sigma
\right|.
}
\tag{1.20}
$$

Therefore the distortion factors cancel in the coarea density:

$$
\boxed{
\frac{
d\mathcal H^2
}{
|\nabla\widetilde r|
}
\Bigg|_{
\Sigma_{\mu_r\tau}
}
=
\frac{
J_\Phi
}{
\mu_r
}
\,
\Phi_\ast
\left[
\frac{
d\mathcal H^2
}{
|\nabla\widetilde r|
}
\Bigg|_{
\Sigma_\tau
}
\right].
}
\tag{1.21}
$$

Hence, whenever the level-set coarea capacity is finite,

$$
\boxed{
\mathcal C(\tau)
=
\int_{\Sigma_\tau}
\frac{
d\mathcal H^2
}{
|\nabla\widetilde r|
},
}
\tag{1.22}
$$

it obeys the exact scaling

$$
\boxed{
\mathcal C(\mu_r\tau)
=
\frac{
J_\Phi
}{
\mu_r
}
\mathcal C(\tau).
}
\tag{1.23}
$$

The factor is

$$
\boxed{
\frac{
J_\Phi
}{
\mu_r
}
=
e^{(5\gamma-1)S_0}
>
1.
}
\tag{1.24}
$$

Thus higher-amplitude scalar sheets must increase their coarea capacity by a fixed factor.

They can do so through:

- increasing sheet area;
- weakening the scalar gradient;
- increasing geometric multiplicity/folding;
- or entering an infinite-capacity branch.

This is the exact **sheet coarea cocycle**.

It is more informative than raw coarea, but it still does not by itself yield an energy contradiction.

The new exact frontier is therefore

$$
\boxed{
\textbf{
Cocycle-Aware Sheet Interface /
Plateau-Degeneration Rigidity.
}
}
\tag{1.25}
$$

The next question is not merely:

> is the scalar reservoir infinite?

It is:

> under the exact Poincaré amplitude cocycle, can the sheet interfaces indefinitely realize the required coarea-capacity growth while the physical horizontal vorticity, critical kinetic-energy tail, rank-two geometry, and same-parent transition defects all remain controlled?

---

# 2. Kinematic coarea NO-GO

We first construct an explicit scalar showing that infinite superlevel measure does not force divergent horizontal-gradient cost.

Choose

$$
\psi\in C_c^\infty(\mathbb R^2)
$$

with

$$
0\le\psi\le1,
$$

$$
\psi=1
\quad\text{on }B_1,
$$

and

$$
\operatorname{supp}\psi\subset B_2.
$$

Choose

$$
\chi\in C_c^\infty(\mathbb R)
$$

with analogous properties.

Let

$$
\boxed{
R_j
=
2^{2j},
\qquad
t_j
=
2^{-3j}.
}
\tag{2.1}
$$

Choose horizontal centers

$$
x_j
$$

and vertical centers

$$
z_j
$$

so that all supports below are mutually disjoint and avoid the fixed anchor line.

Define

$$
\boxed{
u_j(x_h,z)
=
\psi
\left(
\frac{x_h-x_j}{R_j}
\right)
\chi
\left(
\frac{z-z_j}{t_j}
\right),
}
\tag{2.2}
$$

and

$$
\boxed{
u
=
\sum_{j=1}^\infty
u_j.
}
\tag{2.3}
$$

The sum is smooth and locally finite.

---

# 3. Infinite scalar reservoir in the counterexample

The set

$$
\{u>1/2\}
$$

contains one core plateau from every

$$
u_j.
$$

Its volume obeys

$$
\boxed{
\left|
\{u>1/2\}
\right|
\ge
c
\sum_j
R_j^2t_j.
}
\tag{3.1}
$$

But

$$
R_j^2t_j
=
2^{4j}
2^{-3j}
=
2^j.
$$

Hence

$$
\boxed{
\left|
\{u>1/2\}
\right|
=
\infty.
}
\tag{3.2}
$$

---

# 4. Finite horizontal $L^1$ gradient in the counterexample

For one block,

$$
|\nabla_hu_j|
\sim
R_j^{-1}
$$

on a horizontal transition region of area

$$
O(R_j^2)
$$

and vertical thickness

$$
O(t_j).
$$

Therefore

$$
\boxed{
\int
|\nabla_hu_j|
\lesssim
R_jt_j.
}
\tag{4.1}
$$

Now

$$
R_jt_j
=
2^{2j}
2^{-3j}
=
2^{-j}.
$$

Hence

$$
\boxed{
\int_{\mathbb R^3}
|\nabla_hu|
<
\infty.
}
\tag{4.2}
$$

---

# 5. Finite horizontal $L^2$ gradient in the counterexample

Similarly,

$$
\boxed{
\int
|\nabla_hu_j|^2
\lesssim
t_j.
}
\tag{5.1}
$$

Since

$$
\sum_jt_j
=
\sum_j2^{-3j}
<
\infty,
$$

$$
\boxed{
\int_{\mathbb R^3}
|\nabla_hu|^2
<
\infty.
}
\tag{5.2}
$$

Thus an infinite scalar reservoir can have finite horizontal

$$
W^{1,1}
$$

and

$$
W^{1,2}
$$

cost.

Status:

$$
\boxed{
\textbf{PROVED KINEMATIC NO-GO}.
}
$$

This counterexample is not claimed to solve the DSS cocycle or the Euler equations.

It invalidates only the raw measure-to-gradient implication.

---

# 6. A simpler unbounded-plateau example

A radial scalar of the form

$$
\boxed{
u(x_h)
=
\log
\log
\left(
e+|x_h|^2
\right)
}
\tag{6.1}
$$

is unbounded and has infinite-measure positive superlevel sets.

At large radius,

$$
|\nabla_hu|
\sim
\frac{
1
}{
r\log r
}.
$$

Therefore

$$
\boxed{
\nabla_hu
\in
L^2(\mathbb R^2).
}
\tag{6.2}
$$

This provides a second simple model of an infinite scalar reservoir with finite planar enstrophy-type cost.

Again, it is not a DSS solution.

---

# 7. Point anchor is not $H^1$ coercive in two dimensions

The DCRP-43 point anchor is quotient-safe:

$$
\widetilde q
=
q-q(x_{\star,h},z,s).
$$

However a point has critical/vanishing

$$
H^1
$$

capacity in horizontal dimension two.

A direct model shows why.

On the unit disk, define a radial function which is:

- zero for:

  $$
  r\le\varepsilon;
  $$

- one for:

  $$
  r\ge r_0;
  $$

- logarithmically interpolated between.

Then its Dirichlet energy obeys

$$
\boxed{
\int_{D_1}
|\nabla u_\varepsilon|^2
\sim
\frac{
1
}{
|\log\varepsilon|
}
\to0.
}
\tag{7.1}
$$

Thus fixing one point value does not produce a uniform planar

$$
H^1
$$

Poincaré gap.

Status:

$$
\boxed{
\textbf{PROVED BY EXPLICIT TEST FAMILY}.
}
$$

Therefore the point anchor should be retained for gauge uniqueness/material-label statements, but not used alone as the coercive bridge to vorticity.

---

# 8. Slice-mean gauge completion

Let

$$
D_R
$$

be a fixed horizontal disk centered on the recurrent core.

Define

$$
\boxed{
q_R^\circ
=
q
-
\fint_{D_R}
q\,dx_h.
}
\tag{8.1}
$$

Under

$$
q\mapsto q-h(z,s),
$$

$$
\boxed{
q_R^\circ
\mapsto
q_R^\circ.
}
\tag{8.2}
$$

Thus the projection is gauge invariant.

Also

$$
\boxed{
\nabla_hq_R^\circ
=
\nabla_hq
=
-J\Omega_h.
}
\tag{8.3}
$$

---

# 9. NEW THEOREM — Poincaré-to-Vorticity Bridge

## Theorem 9.1

For every fixed

$$
z,s,
$$

$$
\boxed{
\|q_R^\circ\|_{L^2(D_R)}
\le
C R
\|\Omega_h\|_{L^2(D_R)}.
}
\tag{9.1}
$$

### Proof

The function

$$
q_R^\circ
$$

has zero mean on

$$
D_R.
$$

Apply the standard Poincaré inequality and use

$$
|\nabla_hq_R^\circ|
=
|\Omega_h|.
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

This is the first direct coercive bridge from the gauge-completed planar scalar to the physical vorticity.

---

# 10. Renormalized mean-zero scalar

Let

$$
\eta(s)
$$

be the periodic DCRP-42/43 factor.

Define

$$
\boxed{
r_R^\circ
=
\eta(s)
q_R^\circ.
}
\tag{10.1}
$$

Since

$$
\eta
$$

is bounded above and below on one period,

$$
\boxed{
\|r_R^\circ\|_{L^2(D_R)}
\le
C_\eta
R
\|\Omega_h\|_{L^2(D_R)}.
}
\tag{10.2}
$$

Define the mean-projected scalar residual

$$
\boxed{
\mathcal R_R^\circ
=
D_s r_R^\circ
-
(1-2\gamma)
r_R^\circ.
}
\tag{10.3}
$$

This residual contains, among other terms, the commutator between the material derivative and the fixed slice-mean projection.

Thus the coercive scalar branch is:

$$
\boxed{
\mathcal R_R^\circ\neq0
}
$$

or

$$
\boxed{
\mathcal R_R^\circ=0.
}
\tag{10.4}
$$

The latter is stronger than the point-anchored pure cocycle branch.

---

# 11. Mean-projected turnover identity

On a fixed cylindrical region

$$
K
=
D_R\times I_z
$$

where

$$
\mathcal R_R^\circ=0,
$$

$$
\boxed{
D_s r_R^\circ
=
(1-2\gamma)
r_R^\circ.
}
\tag{11.1}
$$

For

$$
p=2,
$$

$$
\boxed{
\partial_s
|r_R^\circ|^2
+
\nabla\cdot
\left(
W|r_R^\circ|^2
\right)
=
(2-\gamma)
|r_R^\circ|^2.
}
\tag{11.2}
$$

If the fixed region is compatible with one-period periodicity,

$$
\boxed{
\int_0^{S_0}
\int_{\partial K}
|r_R^\circ|^2
W\cdot n
dSds
=
(2-\gamma)
\int_0^{S_0}
\int_K
|r_R^\circ|^2
dyds.
}
\tag{11.3}
$$

Thus any nonzero pure mean-projected scalar carries positive turnover.

---

# 12. Physical enstrophy backing of mean-projected scalar mass

Integrating (10.2) over

$$
z,s,
$$

$$
\boxed{
\int_0^{S_0}
\int_K
|r_R^\circ|^2
dyds
\le
C_\eta
R^2
\int_0^{S_0}
\int_K
|\Omega_h|^2
dyds.
}
\tag{12.1}
$$

Therefore, on the pure projected branch,

$$
\boxed{
\int_0^{S_0}
\int_K
|\Omega_h|^2
dyds
\ge
\frac{
1
}{
C_\eta
R^2(2-\gamma)
}
\,
\mathcal J_{R,2}^{out},
}
\tag{12.2}
$$

where

$$
\boxed{
\mathcal J_{R,2}^{out}
=
\int_0^{S_0}
\int_{\partial K}
|r_R^\circ|^2
W\cdot n.
}
\tag{12.3}
$$

Thus a nonzero **mean-zero scalar turnover** is backed by actual planar enstrophy.

The point-anchored scalar turnover alone did not provide this coercive implication.

---

# 13. Balanced plateau theorem

Let

$$
u\in W^{1,1}(D_R)
$$

satisfy

$$
\boxed{
\fint_{D_R}u=0,
\qquad
\|u\|_\infty\le M.
}
\tag{13.1}
$$

Assume for some

$$
0<\tau\le M
$$

$$
\boxed{
|\{u>\tau\}|
\ge
\theta|D_R|.
}
\tag{13.2}
$$

Let

$$
N
=
\{u<0\}.
$$

Mean zero gives

$$
\int_N|u|
=
\int_{\{u>0\}}u.
$$

Therefore

$$
\boxed{
M|N|
\ge
\tau
|\{u>\tau\}|
\ge
\tau\theta|D_R|.
}
\tag{13.3}
$$

Hence

$$
\boxed{
|N|
\ge
\frac{
\tau\theta
}{
M
}
|D_R|.
}
\tag{13.4}
$$

---

# 14. Relative isoperimetric lower bound

For every

$$
0<t<\tau,
$$

the set

$$
E_t=\{u>t\}
$$

contains

$$
\{u>\tau\},
$$

while its complement contains

$$
N.
$$

Thus both sides of the interface have a quantitative area fraction.

The relative isoperimetric inequality in the disk gives

$$
\boxed{
\operatorname{Per}
(
E_t;D_R
)
\ge
c
R
\sqrt{
\theta
\min
\left(
1,\frac{\tau}{M}
\right)
}.
}
\tag{14.1}
$$

---

# 15. NEW THEOREM — Balanced Sheet-Interface Gap

## Theorem 15.1

Under Sections 13--14,

$$
\boxed{
\int_{D_R}
|\nabla u|
dx_h
\ge
c
R\tau
\sqrt{
\theta
\min
\left(
1,\frac{\tau}{M}
\right)
}.
}
\tag{15.1}
$$

### Proof

By coarea,

$$
\int_{D_R}
|\nabla u|
=
\int_{-\infty}^{\infty}
\operatorname{Per}
(
\{u>t\};D_R
)
dt.
$$

Restrict to

$$
0<t<\tau
$$

and use (14.1).

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

# 16. $L^2$ interface/enstrophy gap

By Cauchy--Schwarz,

$$
\boxed{
\int_{D_R}
|\nabla u|^2
\ge
\frac{
1
}{
|D_R|
}
\left(
\int_{D_R}
|\nabla u|
\right)^2.
}
\tag{16.1}
$$

Therefore Theorem 15.1 gives

$$
\boxed{
\int_{D_R}
|\nabla u|^2
\ge
c
\tau^2
\theta
\min
\left(
1,\frac{\tau}{M}
\right).
}
\tag{16.2}
$$

For

$$
u=q_R^\circ,
$$

$$
|\nabla u|=|\Omega_h|.
$$

Thus

$$
\boxed{
\int_{D_R}
|\Omega_h|^2
\ge
c
\tau^2
\theta
\min
\left(
1,\frac{\tau}{M}
\right).
}
\tag{16.3}
$$

When

$$
\tau\le M,
$$

$$
\boxed{
\int_{D_R}
|\Omega_h|^2
\ge
c
\theta
\frac{
\tau^3
}{
M
}.
}
\tag{16.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The cancellation of the disk radius in the final

$$
L^2
$$

lower bound reflects the horizontal two-dimensional critical scaling.

---

# 17. Period-integrated finite interface compiler

Suppose there is a measurable set

$$
\mathcal T
\subset
I_z\times[0,S_0]
$$

with

$$
|\mathcal T|
\ge
m_0>0
$$

such that for every

$$
(z,s)\in\mathcal T
$$

the hypotheses of Theorem 15.1 hold with common parameters

$$
\tau,\theta,M.
$$

Then

$$
\boxed{
\int_0^{S_0}
\int_{I_z}
\int_{D_R}
|\Omega_h|^2
dx_hdzds
\ge
c
m_0
\theta
\frac{
\tau^3
}{
M
}.
}
\tag{17.1}
$$

Thus a balanced plateau persisting over a positive set of slices/times gives a finite normalized physical enstrophy gap.

This is finite-compiler compatible.

---

# 18. Plateau domination

The balanced theorem can fail even when the point-anchored scalar amplitude is large.

The typical escape is a large nearly constant plateau.

On a large disk,

$$
q
$$

may be approximately constant over most of the slice, while all variation needed to connect to the anchor is confined to a small set.

After subtracting the slice mean,

$$
q_R^\circ
$$

is small over most of the plateau.

Thus the infinite point-anchored reservoir can be dominated by a low horizontal mode while its physical content is concentrated in a thin or remote interface.

This is the correct interpretation of the coarea NO-GO.

---

# 19. Interface escape

Define schematically the first level-interface radius

$$
\boxed{
R_{\rm int}(\tau;z,s)
=
\inf
\left\{
R:
\exists
x_h\in D_R
\text{ with }
|\widetilde q(x_h,z,s)|
\ge\tau
\right\}.
}
\tag{19.1}
$$

If along a same-parent sequence

$$
\boxed{
R_{{\rm int},n}(\tau)
\to\infty,
}
\tag{19.2}
$$

the physical transition from the anchored zero level to the

$$
\tau
$$

plateau escapes to normalized infinity.

This is a directional/sheet-tail transition defect.

It is not a local coarea contradiction.

---

# 20. Interface concentration

If the interface remains at bounded radius but its geometric thickness or active measure tends to zero, the scalar transition is concentrating.

On a compact strong-profile class with uniform

$$
C^1
$$

or stronger bounds, a fixed-amplitude transition cannot collapse arbitrarily without generating a corresponding derivative/concentration signal.

Without such a uniform derivative bound, interface concentration is a genuine independent defect channel.

Thus:

$$
\boxed{
\textbf{
bounded interface radius}
}
$$

does not alone imply a uniform

$$
L^2
$$

gap.

The balanced-occupancy or compact-smoothness hypotheses are needed.

---

# 21. Slice intermittency

The infinite three-dimensional reservoir may be carried by sparse normal/time slabs.

The counterexample of Sections 2--5 uses exactly this mechanism.

The total superlevel volume is infinite because the horizontal plateau areas grow faster than the vertical slab thickness decays.

But the integrated horizontal-gradient cost remains finite.

Therefore the quantity

$$
\boxed{
\text{active slice measure}
}
$$

is an essential part of any physical sheet-interface compiler.

A three-dimensional volume statement alone is too coarse.

---

# 22. Correct reservoir dichotomy

The DCRP-43 infinite scalar reservoir must therefore be refined to

$$
\boxed{
\textbf{
balanced recurrent interface}
}
$$

or

$$
\boxed{
\textbf{
plateau-dominated reservoir}.
}
$$

On the first branch, DCRP-44 gives a physical vorticity gap.

On the second branch, at least one of:

$$
\boxed{
\text{interface escape}
}
$$

or

$$
\boxed{
\text{interface concentration}
}
$$

or

$$
\boxed{
\text{slice intermittency}
}
$$

must account for the missing interface cost.

This is the corrected sheet-reservoir normal form.

---

# 23. Global pure scalar cocycle revisited

Assume the global pure anchored branch

$$
\boxed{
\widetilde r(\Phi a)
=
\mu_r\widetilde r(a).
}
\tag{23.1}
$$

Let

$$
\Sigma_\tau
=
\{
\widetilde r=\tau
\}
$$

for a regular positive value

$$
\tau.
$$

Then

$$
\boxed{
\Phi(\Sigma_\tau)
=
\Sigma_{\mu_r\tau}.
}
\tag{23.2}
$$

This is the level-set version of the amplitude cocycle.

---

# 24. Gradient cocycle

Differentiate

$$
\widetilde r(\Phi(a))
=
\mu_r
\widetilde r(a).
$$

Then

$$
D\Phi(a)^T
\nabla\widetilde r(\Phi(a))
=
\mu_r
\nabla\widetilde r(a).
$$

Therefore

$$
\boxed{
\nabla\widetilde r(\Phi(a))
=
\mu_r
D\Phi(a)^{-T}
\nabla\widetilde r(a).
}
\tag{24.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 25. Surface Jacobian

Let

$$
n_\tau(a)
=
\frac{
\nabla\widetilde r(a)
}{
|\nabla\widetilde r(a)|
}
$$

be the level-set normal.

The surface area formula gives

$$
\boxed{
d\mathcal H^2_{\Sigma_{\mu_r\tau}}
=
J_\Phi
\left|
D\Phi^{-T}n_\tau
\right|
d\mathcal H^2_{\Sigma_\tau}.
}
\tag{25.1}
$$

Meanwhile (24.1) gives

$$
\boxed{
|\nabla\widetilde r(\Phi(a))|
=
\mu_r
\left|
D\Phi^{-T}n_\tau
\right|
|\nabla\widetilde r(a)|.
}
\tag{25.2}
$$

The deformation factor cancels in their ratio.

---

# 26. NEW THEOREM — Coarea-Density Poincaré Cocycle

## Theorem 26.1

For regular levels,

$$
\boxed{
\frac{
d\mathcal H^2
}{
|\nabla\widetilde r|
}
\Bigg|_{
\Sigma_{\mu_r\tau}
}
=
\frac{
J_\Phi
}{
\mu_r
}
\,
\Phi_\ast
\left(
\frac{
d\mathcal H^2
}{
|\nabla\widetilde r|
}
\Bigg|_{
\Sigma_\tau
}
\right).
}
\tag{26.1}
$$

Consequently, if

$$
\mathcal C(\tau)
=
\int_{\Sigma_\tau}
\frac{
d\mathcal H^2
}{
|\nabla\widetilde r|
}
<\infty,
$$

then

$$
\boxed{
\mathcal C(\mu_r\tau)
=
\frac{
J_\Phi
}{
\mu_r
}
\mathcal C(\tau).
}
\tag{26.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 27. Strict factor for coarea capacity

Recall

$$
J_\Phi
=
e^{3\gamma S_0},
$$

and

$$
\mu_r
=
e^{(1-2\gamma)S_0}.
$$

Thus

$$
\boxed{
\frac{
J_\Phi
}{
\mu_r
}
=
e^{(5\gamma-1)S_0}.
}
\tag{27.1}
$$

For

$$
\frac25<\gamma<\frac12,
$$

$$
\boxed{
5\gamma-1>1.
}
\tag{27.2}
$$

Therefore

$$
\boxed{
\frac{
J_\Phi
}{
\mu_r
}
>
1.
}
\tag{27.3}
$$

Every increase of scalar amplitude by the DSS factor forces a larger coarea density.

---

# 28. Interpretation of coarea-capacity growth

The quantity

$$
\mathcal C(\tau)
=
\int_{\Sigma_\tau}
|\nabla\widetilde r|^{-1}
d\mathcal H^2
$$

can increase because:

- the level surface area increases;
- the scalar gradient weakens;
- the surface develops multiplicity/folding;
- or the capacity becomes infinite.

Thus the high-amplitude sheets cannot remain simultaneously:

- uniformly finite area;
- uniformly nondegenerate in gradient;
- uniformly simple in multiplicity.

At least one geometric feature must deteriorate.

This is a cocycle-aware geometric statement.

It does not yet specify which deterioration is incompatible with the Navier--Stokes ancestry.

---

# 29. Amplitude-band replication

Define the amplitude generation band

$$
\boxed{
A_\tau
=
\left\{
\tau
<
|\widetilde r|
<
\mu_r\tau
\right\}.
}
\tag{29.1}
$$

On the global pure branch,

$$
\boxed{
\Phi(A_\tau)
=
A_{\mu_r\tau}.
}
\tag{29.2}
$$

The bands for distinct integer generations are disjoint.

If

$$
0<|A_\tau|<\infty,
$$

then

$$
\boxed{
|A_{\mu_r^m\tau}|
=
J_\Phi^m
|A_\tau|.
}
\tag{29.3}
$$

Thus the infinite reservoir may be viewed as an exponentially expanding hierarchy of disjoint amplitude generations.

This is the scalar-sheet analogue of the earlier critical supplier hierarchy.

---

# 30. Why generation volume still does not close the proof

Equation (29.3) produces exponentially growing normalized volume.

But the strict profile already lives on an infinite normalized domain.

Without a bridge from the amplitude bands to:

- velocity energy;
- vorticity;
- physical sheet thickness;
- or transition cost;

the volume growth is not contradictory.

The kinematic counterexamples show that scalar plateaus can grow much faster than their interface cost.

Thus scalar volume cannot replace a physical norm.

---

# 31. External vortex-sheet calibration

Recent exact Euler theory constructs smooth vorticities supported in tubular neighborhoods of analytic vortex sheets with thickness

$$
O(\varepsilon),
$$

while the lifespan remains bounded below independently of

$$
\varepsilon.
$$

The vorticity is organized by almost parallel material surfaces.

This confirms that thin interface concentration is a legitimate exact Euler mechanism.

Therefore:

$$
\boxed{
\textbf{
interface concentration itself is not a contradiction.
}
}
\tag{31.1}
$$

A DCRP closure must use the additional same-parent DSS, PFET, critical-tail, and transition constraints.

---

# 32. External anisotropic regularity calibration

Planar-vorticity regularity criteria for Navier--Stokes require more than a geometric plane condition.

For example, the locally anisotropic criterion of Miller assumes scale-critical mixed-norm control of the plane-restricted vorticity together with controlled variation of the plane normal.

Thus DCRP-44 does not promote the finite interface gap into a regularity theorem without establishing the required analytic norms.

---

# 33. Compact strong-profile implication

On a compact normalized strict-DSS class with:

- uniform:

  $$
  L^\infty
  $$

  scalar bounds on the fixed slice;

- uniform smoothness;

- fixed nontrivial plateau threshold:

  $$
  \tau;
  $$

- fixed balanced occupancy:

  $$
  \theta;
  $$

- positive slice/time measure:

  $$
  m_0;
  $$

Theorem 17.1 gives a uniform physical planar-enstrophy gap

$$
\boxed{
\int
|\Omega_h|^2
\ge
c_{\rm sheet}>0.
}
\tag{33.1}
$$

Therefore a zero-interface-cost compact sequence must lose at least one of the declared compactness properties.

This is the finite sheet-interface compiler.

---

# 34. Corrected strict rank-two sheet state

After DCRP-43/44, the pure scalar survivor is no longer described merely as:

$$
\text{infinite scalar reservoir}.
$$

It is

$$
\boxed{
\textbf{
an infinite amplitude-generation reservoir whose physical interface is either recurrently visible or geometrically degenerate.
}
}
\tag{34.1}
$$

The visible branch pays physical vorticity.

The degenerate branch enters:

$$
\boxed{
\text{interface escape}
\ \vee\
\text{interface concentration}
\ \vee\
\text{slice intermittency}.
}
\tag{34.2}
$$

This is the correct sheet-replenishment normal form.

---

# 35. What DCRP-44 closes

The following overstrong routes are removed.

### infinite scalar measure implies infinite vorticity

False.

### point anchor alone gives an $H^1$ scalar-to-vorticity gap

False in horizontal dimension two.

### coarea alone closes the pure pancake reservoir

False.

The following corrected routes are proved.

### slice-mean scalar oscillation controls physical vorticity

True by Poincaré.

### balanced finite plateau forces a sheet-interface gap

True by relative isoperimetry plus coarea.

### pure scalar level sheets satisfy an exact coarea-density cocycle

True.

Thus the remaining problem is geometric degeneration under the cocycle.

---

# 36. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Cocycle-Aware Sheet Interface /
Plateau-Degeneration Rigidity.
}
}
$$

A useful theorem would show that the global or same-parent pure pancake cocycle cannot indefinitely realize the required amplitude-band and coarea-capacity growth through:

1. interface escape without triggering the existing tail/spatial transition carrier;

2. interface concentration without producing a vorticity/sheet-curvature concentration defect;

3. slice intermittency without violating the periodic scalar mass/turnover requirement;

4. level-surface folding without producing rank lifting or a non-affine strain residual;

5. an exact sheet eigenmode compatible with all of the above but incompatible with the finite-energy unforced Navier--Stokes ancestry.

This is now the principal rank-two sheet-geometry frontier.

---

# 37. End state

The DCRP-43 infinite superlevel reservoir does **not** force a raw coarea contradiction.

Explicit smooth scalar constructions satisfy

$$
\boxed{
|E_\tau|=\infty
}
$$

while

$$
\boxed{
\nabla_hu
\in
L^1\cap L^2.
}
$$

The coercive local gauge is the slice-mean projection

$$
\boxed{
q_R^\circ
=
q-\fint_{D_R}q.
}
$$

It satisfies

$$
\boxed{
\|q_R^\circ\|_2
\le
CR
\|\Omega_h\|_2.
}
$$

If a nontrivial plateau occupies a fixed fraction of a recurrent slice, then

$$
\boxed{
\int_{D_R}
|\Omega_h|^2
\ge
c
\theta
\frac{
\tau^3
}{
M
}
}
$$

under the declared bounded-amplitude hypotheses.

Therefore the sheet reservoir can avoid a visible finite interface only by geometric degeneration:

$$
\boxed{
\text{interface escape}
\ \vee\
\text{interface concentration}
\ \vee\
\text{slice intermittency}.
}
$$

Meanwhile the global pure scalar Poincaré cocycle forces the exact level-set coarea law

$$
\boxed{
\mathcal C(\mu_r\tau)
=
e^{(5\gamma-1)S_0}
\mathcal C(\tau).
}
$$

Thus high-amplitude sheets must exhibit growing coarea capacity.

The next frontier is:

$$
\boxed{
\textbf{
Cocycle-Aware Sheet Interface /
Plateau-Degeneration Rigidity.
}
}
$$