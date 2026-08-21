# DCRP56 — Covariance Rank-Three Lift and the Cylindrical-Shear Infinite-Enstrophy Tail

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / finite-rank-lift vs transparent-tail classification  
**Immediate predecessor:** `NS_DCRP55_MultipoleCompensation_RankLift_TailEscape_2026-08-17.md`

**Primary internal dependencies**
- DCRP-30 — strict DSS exponent window and critical-tail escape
- DCRP-31 — finite PFET / critical tail
- DCRP-35 — finite annular vorticity/strain supplier
- DCRP-54 — localized X72 visibility leakage
- DCRP-55 — positive-stress multipole compensation and normal-vorticity lower bound

**External calibration**
- Dongho Chae & Tai-Peng Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414. Their vorticity-based Liouville criteria exclude periodic DSS Euler profiles under specified vorticity integrability/decay hypotheses; the tail class isolated below escapes these hypotheses maximally rather than contradicting them.
- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468. Recent Type-II analysis continues to use Euler-scale local limits plus Liouville-type exclusion classes.
- Philip Hartman & Louis Nirenberg, *On Spherical Image Maps Whose Jacobians Do Not Change Sign*, Amer. J. Math. 81 (1959), 901–920. Complete flat entire graphs are generalized cylinders.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP55 reduced the outer visibility-compensation problem to:

$$
\boxed{
\text{finite rank/plane lift}
\quad\vee\quad
\text{noncompact non-}L^2\text{ tail}.
}
$$

DCRP56 sharpens **both** alternatives.

---

## Finite compensation branch

Let

$$
M^{\rm in}
=
\int
\chi_{\rm in}
\Omega\otimes\Omega\,dy
$$

be the positive semidefinite dyadic moment of the recurrent inner fixed-plane null-envelope core.

Let

$$
M^{\rm out}
=
\int
\chi_{\rm out}
\Omega\otimes\Omega\,dy
$$

be a finite compact outer actual-vorticity compensator.

DCRP55 proves that complete leading $r^{-3}$ X72 visibility cancellation in all angular directions is equivalent to

$$
\boxed{
M^{\rm in}+M^{\rm out}=cI.
}
$$

Therefore the cumulative covariance is not merely “not rank two.”

It is **exactly isotropic rank three**:

$$
\boxed{
\lambda_1=\lambda_2=\lambda_3=c>0.
}
$$

Moreover

$$
\boxed{
c\ge\lambda_{\max}(M^{\rm in})
\ge\frac12Z_{\rm in},
}
$$

where

$$
Z_{\rm in}
=
\operatorname{tr}M^{\rm in}.
$$

Hence:

$$
\boxed{
\lambda_{\min}
(M^{\rm in}+M^{\rm out})
\ge
\frac12Z_{\rm in}.
}
$$

The outer package must also satisfy

$$
\boxed{
\operatorname{tr}M^{\rm out}
=
3c-Z_{\rm in}
\ge
\frac12Z_{\rm in}.
}
$$

Thus finite transparent compensation activates a **quantitative rank-three covariance reservoir** whose smallest eigenvalue and total outer enstrophy are both at least half of the inner localized enstrophy.

This is stronger than DCRP55's statement that some normal vorticity must appear.

Consequently a truly global “rank-two equality branch” cannot remain rank two through a finite transparent compensation zone:

$$
\boxed{
\text{finite X72 transparency}
\Rightarrow
\text{rank-three covariance lift}.
}
$$

That branch has therefore exited the final rank-two survivor class.

---

## Noncompact fixed-plane tail branch

Suppose instead that no finite rank lift is allowed and the compensation is deferred to a global fixed-plane transparent tail.

Take coordinates with fixed plane normal $n=e_3$ and write

$$
\boxed{
\Omega
=
(q_{y_2},-q_{y_1},0).
}
$$

Then

$$
\boxed{
\nabla\cdot\Omega=0.
}
$$

If the full vorticity dyadic is transparent,

$$
\boxed{
\operatorname{divdiv}
(\Omega\otimes\Omega)=0,
}
$$

a direct calculation yields

$$
\boxed{
\det D_h^2q=0
}
$$

for every $(z,s)$.

Thus every horizontal graph

$$
y_h\mapsto q(y_h,z,s)
$$

is an entire flat surface.

By the complete-flat-surface cylinder theorem, each non-affine horizontal slice has the form

$$
\boxed{
q(y_h,z,s)
=
f_{z,s}
\bigl(
\xi(z,s)\cdot y_h
\bigr)
+
b(z,s)\cdot y_h
+
c(z,s).
}
$$

Hence its vorticity is

$$
\boxed{
\Omega_h
=
J
\left[
f'_{z,s}(\xi\cdot y_h)\xi+b
\right],
}
$$

which is invariant along the horizontal direction orthogonal to $\xi$.

Therefore every nonzero such slice has infinite horizontal $L^p$ norm for **every**

$$
p>0.
$$

Smooth nontriviality then implies

$$
\boxed{
\Omega\notin L^p(\mathbb R^3)
\qquad
\forall p>0.
}
$$

More quantitatively, on any nonzero smooth cylindrical-shear patch there exists $c_p>0$ such that for all sufficiently large $R$,

$$
\boxed{
\int_{B_R}|\Omega|^p\,dy
\ge
c_pR.
}
$$

Thus the no-rank-lift transparent escape is not an arbitrary non-$L^2$ tail.

It is a **maximally nonintegrable cylindrical-shear tail**.

This explains exactly how the branch evades the known Chae–Tsai vorticity-integrability Liouville classes: it fails every finite positive $L^p$ condition, not merely $L^2$.

---

## New dichotomy

The outer equality problem is now:

$$
\boxed{
\textbf{
finite isotropic rank-three covariance lift}
}
$$

or

$$
\boxed{
\textbf{
global fixed-plane cylindrical-shear tail with }
\Omega\notin L^p
\textbf{ for every }p>0.
}
$$

The finite branch has left rank two.

The tail branch remains rank two only by becoming maximally noncompact.

The next frontier is to test whether this cylindrical-shear tail can coexist with:

- the strict DSS velocity-energy growth
  $$
  E(R)\sim R^{3-2\alpha},
  \qquad
  0<3-2\alpha<1;
  $$
- inward PFET;
- finite-energy same-parent ancestry;
- the scalar/pressure constraints already accumulated in DCRP.

---

# 1. Finite full-angular compensation

Let

$$
M^{\rm in}\succeq0,
$$

$$
M^{\rm out}\succeq0.
$$

DCRP55 gives the necessary and sufficient leading-multipole transparency condition

$$
\boxed{
M^{\rm in}+M^{\rm out}=cI.
}
\tag{1.1}
$$

The inner core is nonzero, so

$$
c>0.
$$

Immediately:

## Theorem D56.1 — Exact Isotropic Rank-Three Lift

Any finite actual-vorticity outer carrier that completely cancels the leading D54 angular visibility multipole produces

$$
\boxed{
M^{\rm tot}
:=
M^{\rm in}+M^{\rm out}
=
cI.
}
$$

Therefore

$$
\boxed{
\operatorname{rank}M^{\rm tot}=3.
}
$$

All three covariance eigenvalues equal $c$.

Finite transparent compensation is an exact rank-three covariance lift.

---

# 2. Smallest eigenvalue lower bound

Because

$$
M^{\rm out}
=
cI-M^{\rm in}
\succeq0,
$$

we require

$$
\boxed{
c\ge
\lambda_{\max}(M^{\rm in}).
}
\tag{2.1}
$$

Since the inner moment is supported in a two-dimensional vorticity plane,

$$
\operatorname{rank}M^{\rm in}\le2.
$$

Let its nonzero eigenvalues be

$$
\lambda_1\ge\lambda_2\ge0.
$$

Then

$$
Z_{\rm in}
=
\lambda_1+\lambda_2.
$$

Hence

$$
\boxed{
\lambda_1\ge\frac12Z_{\rm in}.
}
\tag{2.2}
$$

Thus:

## Theorem D56.2 — Quantitative Third-Eigenvalue Gap

$$
\boxed{
\lambda_{\min}(M^{\rm tot})
=
c
\ge
\frac12Z_{\rm in}.
}
\tag{2.3}
$$

The rank-three lift is quantitative, not merely topological.

---

# 3. Outer total-enstrophy cost

Taking traces in (1.1),

$$
\boxed{
Z_{\rm in}
+
Z_{\rm out}
=
3c,
}
\tag{3.1}
$$

where

$$
Z_{\rm out}
=
\operatorname{tr}M^{\rm out}
=
\int
\chi_{\rm out}|\Omega|^2.
$$

Therefore

$$
\boxed{
Z_{\rm out}
=
3c-Z_{\rm in}.
}
\tag{3.2}
$$

Using

$$
c\ge Z_{\rm in}/2,
$$

we get

$$
\boxed{
Z_{\rm out}
\ge
\frac12Z_{\rm in}.
}
\tag{3.3}
$$

So any full finite compensation carries at least half as much total outer enstrophy as the inner core, in addition to the normal-vorticity lower bound already proved in DCRP55.

---

# 4. Isotropic cumulative covariance is stronger than a local normal excursion

DCRP55 showed

$$
\int
\chi_{\rm out}(\Omega\cdot n)^2
\ge
\frac12Z_{\rm in}.
$$

D56 adds:

$$
\boxed{
M^{\rm tot}=cI.
}
$$

Thus full transparent compensation does not merely require “some vorticity outside the plane.”

It requires complete second-moment isotropization of the cumulative inner+outer vorticity population.

In particular the final finite package has no rank-two null direction at covariance level.

This is exactly the previously isolated **rank-three covariance lift branch**.

---

# 5. Consequence for the rank-two survivor tree

Suppose the DCRP argument is currently following the strict equality route in which the relevant recurrent vorticity covariance remains rank two.

Then Theorem D56.1 implies:

$$
\boxed{
\text{finite full X72 multipole compensation}
}
$$

is not an equality mechanism inside that branch.

It is an **exit**:

$$
\boxed{
\text{rank two}
\longrightarrow
\text{rank three}.
}
$$

Therefore the only way to remain in a globally fixed rank-two identity class is to refuse finite full compensation and move to the noncompact tail alternative.

---

# 6. Fixed-plane transparent tail ansatz

Take the global fixed plane to be

$$
n=e_3.
$$

Write

$$
\boxed{
\Omega
=
(\Omega_1,\Omega_2,0).
}
\tag{6.1}
$$

Because

$$
\nabla\cdot\Omega=0,
$$

$$
\boxed{
\partial_1\Omega_1
+
\partial_2\Omega_2
=
0.
}
\tag{6.2}
$$

On each simply connected horizontal slice one may write

$$
\boxed{
\Omega
=
(\partial_2q,-\partial_1q,0)
}
\tag{6.3}
$$

for a scalar stream/shear function $q(y_1,y_2,z,s)$.

This is exactly the planar-vorticity representation used throughout the DCRP rank-two branch.

---

# 7. Double divergence becomes a horizontal Monge–Ampère determinant

Set

$$
Q
=
\Omega\otimes\Omega.
$$

Since the third row and column vanish,

$$
\operatorname{divdiv}Q
=
\partial_a\partial_b
(\Omega_a\Omega_b),
\qquad
a,b\in\{1,2\}.
$$

Substituting

$$
\Omega_1=q_2,
\qquad
\Omega_2=-q_1,
$$

a direct differentiation gives

$$
\boxed{
\operatorname{divdiv}
(\Omega\otimes\Omega)
=
2q_{12}^2
-
2q_{11}q_{22}.
}
\tag{7.1}
$$

Therefore:

## Theorem D56.3 — Fixed-Plane Transparency = Degenerate Horizontal Monge–Ampère

For a smooth fixed-plane divergence-free vorticity field,

$$
\boxed{
\operatorname{divdiv}
(\Omega\otimes\Omega)=0
}
$$

if and only if

$$
\boxed{
\det D_h^2q=0.
}
\tag{7.2}
$$

The global transparent tail is therefore horizontally developable on every $(z,s)$ slice.

---

# 8. Entire horizontal slices are complete flat graphs

Fix $(z,s)$.

Assume

$$
q(\cdot,z,s)\in C^2(\mathbb R^2)
$$

and

$$
\det D_h^2q=0.
$$

Consider its graph

$$
\Gamma_{z,s}
=
\left\{
(y_h,q(y_h,z,s))
\right\}
\subset\mathbb R^3.
$$

The induced graph metric dominates the Euclidean base metric, so the entire graph is complete.

For a surface graph, Gaussian curvature is

$$
K
=
\frac{
\det D_h^2q
}{
(1+|\nabla_hq|^2)^2
}.
$$

Hence

$$
\boxed{
K=0.
}
$$

Thus every horizontal slice is a complete flat surface.

---

# 9. Hartman–Nirenberg cylindrical normal form

By the complete flat-surface cylinder theorem, every connected nonplanar entire slice is a generalized cylinder.

Since it is a graph over $\mathbb R^2$, there exist:

- a unit vector
  $$
  \xi(z,s)\in\mathbb S^1;
  $$
- a one-variable function
  $$
  f_{z,s};
  $$
- a vector
  $$
  b(z,s)\in\mathbb R^2;
  $$
- a scalar
  $$
  c(z,s);
  $$

such that

$$
\boxed{
q(y_h,z,s)
=
f_{z,s}
\bigl(
\xi(z,s)\cdot y_h
\bigr)
+
b(z,s)\cdot y_h
+
c(z,s).
}
\tag{9.1}
$$

The affine case is included by taking $f''=0$.

---

# 10. Cylindrical-shear vorticity

Differentiate (9.1):

$$
\boxed{
\nabla_hq
=
f'_{z,s}(\xi\cdot y_h)\xi+b.
}
\tag{10.1}
$$

Hence

$$
\boxed{
\Omega_h
=
J
\left[
f'_{z,s}(\xi\cdot y_h)\xi+b
\right].
}
\tag{10.2}
$$

Let

$$
\eta=J\xi.
$$

Then

$$
\xi\cdot(y_h+t\eta)
=
\xi\cdot y_h.
$$

Therefore

$$
\boxed{
\Omega_h(y_h+t\eta,z,s)
=
\Omega_h(y_h,z,s)
}
\tag{10.3}
$$

for every $t$.

Each transparent horizontal slice is a cylindrical shear: the vorticity is invariant along one complete horizontal direction.

---

# 11. Nonzero cylindrical slices have infinite $L^p$ mass

Fix $p>0$.

Suppose one horizontal slice is nonzero.

Then there exists a point in the one-dimensional longitudinal coordinate

$$
r=\xi\cdot y_h
$$

where

$$
\left|
J
\left[
f'(r)\xi+b
\right]
\right|
>0.
$$

By continuity there is an interval $I$ and $\varepsilon>0$ such that

$$
\boxed{
|\Omega_h|
\ge\varepsilon
}
$$

whenever

$$
r\in I.
$$

But the field is independent of the transverse coordinate

$$
t=\eta\cdot y_h.
$$

Therefore

$$
\boxed{
\int_{\mathbb R^2}
|\Omega_h(y_h,z,s)|^pdy_h
=
\infty.
}
\tag{11.1}
$$

---

# 12. Global nonintegrability

Suppose the full smooth field is nonzero at some point.

By continuity it remains nonzero for a positive-measure interval of nearby $z$ values and times.

For each such $z$ slice, Section 11 gives infinite horizontal $L^p$ mass.

Hence:

## Theorem D56.4 — Maximally Nonintegrable Transparent Fixed-Plane Tail

Let a smooth nonzero fixed-plane vorticity field on $\mathbb R^3$ satisfy

$$
\operatorname{divdiv}
(\Omega\otimes\Omega)=0
$$

and remain globally in one fixed vorticity plane.

Then

$$
\boxed{
\Omega\notin L^p(\mathbb R^3)
\qquad
\forall p>0.
}
\tag{12.1}
$$

Thus the no-rank-lift transparent tail escapes **every positive vorticity integrability class**.

This strengthens the DCRP55 conclusion

$$
\Omega\notin L^2.
$$

---

# 13. Linear lower growth of local $L^p$ mass

The cylindrical form gives more than divergence.

Choose a compact longitudinal interval

$$
I
$$

and a compact vertical interval

$$
J
$$

on which

$$
|\Omega|\ge\varepsilon>0.
$$

For sufficiently large $R$, the Euclidean ball $B_R$ contains a transverse segment of length comparable to $R$ above every point of a fixed smaller $(r,z)$ rectangle.

Therefore there is a constant $c_p>0$ such that

$$
\boxed{
\int_{B_R}
|\Omega|^pdy
\ge
c_pR
}
\tag{13.1}
$$

for all sufficiently large $R$.

## Corollary D56.5 — Cylindrical Tail Growth Floor

Any nonzero globally transparent fixed-plane tail has at least linear growth of every local vorticity $L^p$ mass:

$$
\boxed{
\|\Omega\|_{L^p(B_R)}^p
\gtrsim R.
}
\tag{13.2}
$$

This is a geometric, not scaling-assumed, tail lower bound.

---

# 14. Relation to Chae–Tsai DSS Euler exclusions

Chae–Tsai prove several nonexistence criteria for periodic DSS Euler profiles under vorticity integrability and decay assumptions.

For example their Theorem 2.2 excludes nonzero periodic profiles when, among other hypotheses, there exists

$$
0<q<\frac{3}{1+\alpha}
$$

with

$$
\Omega\in L^q(\mathbb R^3\times[0,S_0]).
$$

The D56 transparent fixed-plane tail satisfies the opposite extreme:

$$
\boxed{
\Omega\notin L^q
\qquad
\forall q>0.
}
$$

Therefore D56 does not create a contradiction with the Chae–Tsai theorem.

Instead it classifies **how the survivor must escape it**.

The tail is not barely outside one critical exponent.

It is cylindrical enough to fail every finite positive global vorticity $L^q$ condition.

---

# 15. Relation to DCRP30 critical tail

DCRP30 already forces the strict DSS Euler survivor outside standard global finite-energy and decay classes.

D56 adds a structural alternative.

If the branch insists on global fixed-plane transparency, then its vorticity tail must be cylindrical-shear and at least linearly nonintegrable in every positive power.

This is substantially more rigid than the generic DCRP30 statement

$$
\boxed{
\text{critical nonintegrable tail required}.
}
$$

The tail now carries a geometric translation symmetry on every horizontal slice.

---

# 16. Does the cylindrical tail contradict the DCRP30 velocity-energy exponent?

DCRP30's profile energy grows in the critical survivor like a sublinear power

$$
\boxed{
E_V(R)
\sim
R^{3-2\alpha},
}
\tag{16.1}
$$

with

$$
\boxed{
0<3-2\alpha<1.
}
\tag{16.2}
$$

D56 gives instead the vorticity lower bound

$$
\boxed{
\int_{B_R}|\Omega|^p
\gtrsim R.
}
\tag{16.3}
$$

These quantities are not directly comparable without an additional global inverse-curl/Biot–Savart control valid in the rough DSS tail class.

Large vorticity can in principle coexist with smaller velocity energy through high-frequency or nonlocal structure.

Therefore:

## STOP-D56-A

No direct contradiction between (16.1) and (16.3) is claimed.

A separate velocity–vorticity tail coupling theorem is required.

---

# 17. A sharper branch diagram

The D54 visibility-matching problem now has the following exact classification.

## Branch F — finite full compensation

$$
\boxed{
M^{\rm in}+M^{\rm out}=cI.
}
$$

Then:

$$
\boxed{
\operatorname{rank}M^{\rm tot}=3,
}
$$

$$
\boxed{
\lambda_{\min}M^{\rm tot}\ge\frac12Z_{\rm in},
}
$$

and

$$
\boxed{
Z_{\rm out}\ge\frac12Z_{\rm in}.
}
$$

The final rank-two branch exits into a quantitative rank-three covariance state.

## Branch T — fixed-plane transparent tail

No finite rank lift is used.

If the branch remains globally fixed-plane and transparent, then every horizontal slice is cylindrical, and

$$
\boxed{
\Omega\notin L^p
\quad
\forall p>0.
}
$$

This is the maximally nonintegrable shear-tail class.

## Branch U — uncancelled visibility

If neither finite isotropization nor transparent tail occurs, the X72 visibility leakage remains nonzero globally.

This is itself a non-equality branch.

---

# 18. Same-parent recurrence

On an exact DSS profile, the normalized covariance moments and cylindrical-tail structure recur after one period.

### Finite branch

The isotropic rank-three covariance package

$$
c(s)I
$$

must recur every period.

Thus the rank-three lift is a recurrent normalized state, not a transient one-time event.

### Tail branch

The cylindrical directions

$$
\xi(z,s)
$$

and one-dimensional shear profiles recur modulo DSS time periodicity.

Thus the maximally nonintegrable tail geometry itself must be reconstructed every period.

The remaining issue is again same-parent realizability/replenishment rather than one-time existence.

---

# 19. NTLA-O interpretation

DCRP55 had two unresolved ways to satisfy the outer observer:

- change orientation finitely;
- escape to infinity.

D56 increases observer resolution.

The finite branch is identified not merely as “normal vorticity exists” but as

$$
\boxed{
\text{isotropic rank-three cumulative covariance}.
}
$$

The tail branch is identified not merely as “non-$L^2$” but as

$$
\boxed{
\text{entire cylindrical-shear developability}.
}
$$

So the new NTLA-O split is:

$$
\boxed{
\text{outer compensation}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{finite isotropic rank lift}
\quad\vee\quad
\text{cylindrical infinite tail}.
}
$$

Both are substantially narrower identity classes than the previous generic alternatives.

---

# 20. X72 interpretation

At the pointwise X72 level, both finite and tail vorticity stresses are realizable.

At the multipole/projection level:

### finite route

global visibility matching demands

$$
M^{\rm tot}=cI.
$$

### fixed-plane tail route

global transparency reduces to

$$
\det D_h^2q=0,
$$

forcing a cylindrical stress-generating geometry.

Thus the X72 realizability tower has produced two very special global lifts:

$$
\boxed{
\text{isotropic covariance lift}
}
$$

or

$$
\boxed{
\text{developable shear tail}.
}
$$

The generic wave-cone freedom is gone.

---

# 21. Updated final survivor

After DCRP56, a globally transparent continuation of the inner rank-two null-envelope core must satisfy

$$
\boxed{
\begin{aligned}
&
\text{recurrent finite isotropic rank-three covariance lift}
\\
&\qquad
\lambda_{\min}
\ge
\frac12Z_{\rm in}
\\[4pt]
&\vee
\\[4pt]
&
\text{recurrent fixed-plane cylindrical-shear tail}
\\
&\qquad
\Omega\notin L^p
\quad
\forall p>0
\\[4pt]
&\vee
\\[4pt]
&
\text{nonzero global X72 visibility defect}.
\end{aligned}
}
$$

The previous broad “rank lift or infinite tail” escape has become a pair of explicit normal forms.

---

# 22. Status ledger

## PROVED this round

### D56-P1 — Exact finite rank-three covariance lift

$$
M^{\rm tot}=cI.
$$

### D56-P2 — Quantitative smallest-eigenvalue gap

$$
\lambda_{\min}(M^{\rm tot})
\ge
\frac12Z_{\rm in}.
$$

### D56-P3 — Outer total-enstrophy lower bound

$$
Z_{\rm out}\ge\frac12Z_{\rm in}.
$$

### D56-P4 — Fixed-plane transparency equation

$$
\operatorname{divdiv}
(\Omega\otimes\Omega)=0
\iff
\det D_h^2q=0.
$$

### D56-P5 — Entire horizontal cylindrical normal form

$$
q
=
f(\xi\cdot y_h)
+
b\cdot y_h+c
$$

on each complete horizontal slice.

### D56-P6 — Maximally nonintegrable tail

$$
\Omega\notin L^p(\mathbb R^3)
\qquad
\forall p>0.
$$

### D56-P7 — Linear local vorticity-mass growth

$$
\int_{B_R}|\Omega|^p
\gtrsim R.
$$

---

# 23. Closed / limited routes

## Closed

Finite full visibility compensation cannot remain a rank-two covariance state.

## Closed

A nonzero globally fixed-plane transparent tail cannot belong to any positive global vorticity $L^p$ class.

## Not closed

A recurrent isotropic rank-three finite supplier may be dynamically realizable.

## Not closed

A cylindrical-shear infinite-enstrophy tail may coexist with the critical DSS velocity-energy growth.

## Not claimed

The vorticity lower-growth floor directly contradicts the velocity-energy tail exponent.

A new inverse-curl/PFET/tail coupling estimate is required.

---

# 24. New STOP

$$
\boxed{
\textbf{
STOP-D56:
The outer equality routes are now explicit normal forms: finite transparency is a quantitative isotropic rank-three covariance lift, while refusing that lift and remaining fixed-plane transparent forces a cylindrical-shear tail outside every positive vorticity }L^p\textbf{ class.}
}
$$

---

# 25. Next autonomous step

## DCRP57 — Rank-Three Supplier Dynamics versus Cylindrical Tail Energy

**Working title**

> **Isotropic Covariance Reproduction, Cylindrical-Shear Tail Growth, and the Final Rank-Lift/Tail Coupling**

Primary tasks:

1. finite branch:
   derive the evolution/Floquet equation for the isotropic covariance scalar
   $$
   c(s)
   $$
   and test whether DCRP35/DCRP41 dynamics can recurrently generate isotropy from a rank-two inner core;
2. determine whether recurrent isotropization forces a nonzero rank-three/stretching defect already excluded in earlier RMRM/DCRP branches;
3. tail branch:
   combine the cylindrical-shear normal form with Biot–Savart / pressure / PFET information to derive a lower bound for velocity-energy growth;
4. compare any such lower bound with
   $$
   E_V(R)\sim R^{3-2\alpha},
   \qquad
   0<3-2\alpha<1;
   $$
5. if no contradiction follows, classify the exact cylindrical critical-tail equality mode.

Desired endpoint:

$$
\boxed{
\text{rank-three reproduction obstruction}
\ \vee\
\text{velocity-energy tail mismatch}
\ \vee\
\text{explicit rough cylindrical equality class}.
}
$$

---

# 26. One-line checkpoint

Finite X72 compensation has become an exact recurrent isotropic rank-three covariance state, while the only globally transparent no-rank-lift alternative is an entire cylindrical-shear vorticity tail that fails every positive $L^p$ integrability condition; the next problem is now the dynamics of those two explicit normal forms.

---

**End checkpoint:** DCRP56  
**Next:** DCRP57 — Rank-Three Supplier Dynamics / Cylindrical Tail Energy.
