# DCRP58 — Cylindrical Transparent-Tail Elimination and Outer-Compensation Equality Closure

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / transparent-tail elimination round  
**Immediate predecessor:** `NS_DCRP57_IsotropicResidual_StraightCylinderNoGo_TwistTail_2026-08-17.md`

**Primary internal dependencies**
- DCRP-30 — strict Type-II DSS exponent window and sublinear divergent period-averaged velocity-energy tail
- DCRP-42 — fixed-plane planar-vorticity scalar representation and normal-vorticity preservation
- DCRP-54 — unavoidable localized X72 visibility leakage
- DCRP-55 — finite rank-lift / noncompact transparent-tail alternative
- DCRP-56 — global fixed-plane transparent tail is horizontally cylindrical
- DCRP-57 — finite isotropic rank-three branch requires nonzero covariance residual

**External calibration**
- Liutang Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619.
- Dongho Chae & Tai-Peng Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414.

The external literature is used only to calibrate the DSS Euler tail/integrability context already adopted in DCRP-30. No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP55–57 left one apparent no-rank-lift escape:

$$
\boxed{
\text{global fixed-plane transparent cylindrical tail}.
}
$$

DCRP57 excluded only the globally straight-cylinder subclass and left twisting cylindrical tails / affine-hinge chains open.

DCRP58 closes the **entire** globally fixed-plane transparent cylindrical-tail branch under the DCRP30/Xue sublinear period-averaged velocity-energy bound

$$
\boxed{
\mathcal E(R)
:=
\int_0^{S_0}
\int_{B_R}
|V(y,s)|^2\,dy\,ds
\le
CR^\kappa,
}
$$

where

$$
\boxed{
\kappa=3-2\alpha\in(0,1).
}
$$

The argument is insensitive to twisting of the cylinder direction.

DCRP56 gives, on every horizontal slice,

$$
\boxed{
q(y_h,z,s)
=
f(r,z,s)
+
\beta(z,s)t
+
c(z,s),
}
$$

after absorbing the affine component parallel to the active cylinder direction into $f$, where

$$
r=\xi(z,s)\cdot y_h,
$$

$$
t=\eta(z,s)\cdot y_h,
\qquad
\eta=J\xi.
$$

The vorticity is

$$
\boxed{
\Omega_h
=
f_r(r,z,s)\eta(z,s)
-
\beta(z,s)\xi(z,s).
}
$$

There are exactly two cases.

---

## Case A — nonzero affine transverse vorticity offset

If

$$
\beta(z_0,s_0)\neq0,
$$

then on a nearby $(z,s)$ patch,

$$
\boxed{
\Omega_h\cdot\xi=-\beta
}
$$

is a nonzero quantity independent of the entire horizontal variable $y_h$.

A compact curl-duality test over horizontal disks of radius $R$ yields

$$
\boxed{
\mathcal E(CR)\gtrsim R^2.
}
$$

This contradicts

$$
\mathcal E(R)=O(R^\kappa),
\qquad
\kappa<1.
$$

Therefore every admissible transparent cylindrical tail must satisfy

$$
\boxed{
\beta\equiv0.
}
$$

---

## Case B — pure cylindrical shear

Now

$$
\boxed{
q=f(r,z,s)+c(z,s),
}
$$

and

$$
\boxed{
\Omega_h=f_r\eta.
}
$$

DCRP42 normal-vorticity preservation gives

$$
\boxed{
\Omega_h\cdot\nabla_hw=0.
}
$$

On every active region where

$$
f_r\neq0,
$$

this becomes

$$
\boxed{
\partial_tw=0.
}
$$

Thus the vertical velocity is constant along every complete cylinder line inside the active region.

If $w$ were nonzero at one active point, continuity plus $\partial_tw=0$ would produce a fixed $(r,z,s)$ patch on which $|w|\ge\varepsilon$ for all $|t|<R$, giving

$$
\boxed{
\mathcal E(CR)\gtrsim R.
}
$$

Again this contradicts

$$
\kappa<1.
$$

Therefore

$$
\boxed{
w=0
}
$$

on every active cylindrical region.

But then

$$
q=w-\phi_z=-\phi_z,
$$

and incompressibility gives

$$
\Delta_h\phi+w_z=0.
$$

Since $w=0$ on the open active region,

$$
w_z=0,
$$

so

$$
\Delta_h\phi=0.
$$

Differentiate in $z$:

$$
\Delta_h\phi_z=0.
$$

Since

$$
\phi_z=-q,
$$

we obtain

$$
\boxed{
\Delta_hq=0.
}
$$

For

$$
q=f(r,z,s)+c,
$$

this means

$$
\boxed{
f_{rr}=0
}
$$

wherever

$$
f_r\neq0.
$$

Smoothness now forces, on every horizontal slice, either

$$
f_r\equiv0
$$

or

$$
f_r\equiv K(z,s)\neq0
$$

for all $r$.

In the latter case,

$$
\boxed{
\Omega_h=K(z,s)\eta(z,s)
}
$$

is uniform over the entire horizontal plane.

The same curl-duality argument used in Case A again gives

$$
\boxed{
\mathcal E(CR)\gtrsim R^2,
}
$$

contradicting $\kappa<1$.

Hence

$$
\boxed{
f_r\equiv0.
}
$$

Therefore

$$
\boxed{
\Omega\equiv0.
}
$$

---

## Main tail theorem

The two cases exhaust the entire DCRP56 cylindrical normal form.

Thus:

$$
\boxed{
\textbf{
A nonzero DSS Euler profile in the DCRP30 sublinear-energy tail class cannot remain globally fixed-plane and satisfy }
\operatorname{divdiv}(\Omega\otimes\Omega)=0.
}
$$

Equivalently, the noncompact no-rank-lift transparent escape isolated in DCRP55/56 is removed.

This is stronger than DCRP57's straight-cylinder NO-GO:

- twisting the cylinder direction does not save the tail;
- affine-hinge chains do not save the tail;
- infinite vorticity $L^p$ mass does not save the tail.

The sublinear **velocity** energy law, combined with the fixed-plane Euler structure, kills the entire branch.

---

## Outer-compensation equality closure

DCRP55 now has only one finite transparent alternative:

$$
\boxed{
M^{\rm in}+M^{\rm out}=cI,
}
$$

which DCRP56 identifies as an exact isotropic rank-three covariance lift.

But DCRP57 proves that a recurrent isotropic covariance must satisfy the quantitative residual gap

$$
\boxed{
\int_0^{S_0}
\|R_B\|_Fds
\ge
\frac{\sqrt3}{2}
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)\,ds
>0.
}
$$

Therefore it cannot lie in the DCRP38 zero-residual affine/no-turnover equality branch.

Combining D54–D58:

> A nonzero inner rank-two null-envelope core cannot have its X72 visibility leak globally neutralized while remaining in the zero-defect rank-two equality class.

Any global continuation must activate at least one already-declared defect mechanism:

$$
\boxed{
\text{rank-three covariance lift}
}
$$

with

$$
\boxed{
R_B^{na}\neq0
\quad\vee\quad
R_B^{tr}\neq0,
}
$$

or leave exact X72 visibility compensation and retain a nonzero global projection defect.

The entire “transparent rank-two tail” equality route is closed.

This is a substantial closure of the final rank-two survivor tree.

It is **not yet** a proof of Navier–Stokes regularity: the nonzero defect/rank-lift branches remain to be closed or absorbed by the larger RMRM/X72 argument.

---

# 1. Period-averaged sublinear energy class

The DCRP30/Xue survivor obeys the period-averaged local energy upper bound

$$
\boxed{
\mathcal E(R)
=
\int_0^{S_0}
\int_{B_R}
|V(y,s)|^2\,dy\,ds
\le
C R^\kappa
}
\tag{1.1}
$$

for sufficiently large $R$, where

$$
\boxed{
\kappa
=
3-2\alpha.
}
\tag{1.2}
$$

The strict Type-II exponent window is

$$
\boxed{
1<\alpha<\frac32.
}
\tag{1.3}
$$

Therefore

$$
\boxed{
0<\kappa<1.
}
\tag{1.4}
$$

The only property used below is the strict sublinear upper bound

$$
\boxed{
\mathcal E(R)=o(R).
}
\tag{1.5}
$$

---

# 2. Global cylindrical normal form

DCRP56 proves that a globally fixed-plane transparent vorticity field satisfies

$$
\det D_h^2q=0.
$$

Every complete horizontal slice is therefore cylindrical.

After absorbing the affine component of the horizontal gradient parallel to the active cylinder direction into the one-variable profile, write

$$
\boxed{
q(y_h,z,s)
=
f(r,z,s)
+
\beta(z,s)t
+
c(z,s),
}
\tag{2.1}
$$

where

$$
\boxed{
r
=
\xi(z,s)\cdot y_h,
}
\tag{2.2}
$$

$$
\boxed{
t
=
\eta(z,s)\cdot y_h,
}
\tag{2.3}
$$

$$
\boxed{
\eta=J\xi.
}
\tag{2.4}
$$

The direction fields may twist with $z$ and $s$.

No straight-cylinder assumption is made.

---

# 3. Vorticity decomposition

Since

$$
\Omega_h
=
J\nabla_hq,
$$

we have

$$
\nabla_hq
=
f_r\xi+\beta\eta.
$$

Therefore

$$
\boxed{
\Omega_h
=
f_r\eta
-
\beta\xi.
}
\tag{3.1}
$$

In particular,

$$
\boxed{
\Omega_h\cdot\xi=-\beta,
}
\tag{3.2}
$$

and

$$
\boxed{
\Omega_h\cdot\eta=f_r.
}
\tag{3.3}
$$

Both identities hold across the whole horizontal plane at fixed $(z,s)$.

---

# 4. Curl-duality lemma for a uniform horizontal vorticity component

We first isolate a general energy lemma.

## Lemma D58.1 — Uniform-Plane Vorticity Forces Superlinear Energy

Suppose there exist:

- compact intervals
  $$
  J_z,\ I_s;
  $$
- a smooth horizontal unit vector field
  $$
  e(z,s);
  $$
- a continuous scalar
  $$
  b(z,s);
  $$

such that on

$$
\mathbb R^2_{y_h}\times J_z\times I_s
$$

one has

$$
\boxed{
\Omega(y_h,z,s)\cdot e(z,s)=b(z,s),
}
\tag{4.1}
$$

and

$$
\boxed{
|b(z,s)|\ge b_0>0.
}
\tag{4.2}
$$

Then there is $c>0$ such that

$$
\boxed{
\mathcal E(CR)\ge cR^2
}
\tag{4.3}
$$

for all large $R$.

### Proof

Choose smooth compact cutoffs

$$
\zeta(z,s)
$$

supported in $J_z\times I_s$ and with sign chosen so that

$$
\zeta b\ge c_0>0
$$

on a smaller positive-measure set.

Let

$$
\chi\in C_c^\infty(\mathbb R^2),
\qquad
0\le\chi\le1,
$$

with

$$
\chi=1
$$

on the unit disk.

Define

$$
\boxed{
\chi_R(y_h)=\chi(y_h/R),
}
\tag{4.4}
$$

and the spacetime test vector

$$
\boxed{
\psi_R(y,s)
=
\zeta(z,s)\chi_R(y_h)e(z,s).
}
\tag{4.5}
$$

For each $s$,

$$
\int
\Omega\cdot\psi_Rdy
=
\int
V\cdot(\nabla\times\psi_R)dy.
$$

Integrate in $s$.

The left side satisfies

$$
\boxed{
\left|
\int
\Omega\cdot\psi_R
\right|
\ge
c_1R^2.
}
\tag{4.6}
$$

For the curl of $\psi_R$:

- horizontal cutoff derivatives are $O(R^{-1})$ on area $O(R^2)$;
- $z$-derivatives of $\zeta e$ are $O(1)$ on area $O(R^2)$.

Therefore

$$
\boxed{
\|\nabla\times\psi_R\|_{L^2_{y,s}}
\le
C_1R.
}
\tag{4.7}
$$

By Cauchy–Schwarz,

$$
c_1R^2
\le
\mathcal E(CR)^{1/2}
C_1R.
$$

Hence

$$
\boxed{
\mathcal E(CR)\ge cR^2.
}
$$

$$
\square
$$

The twisting of $e(z,s)$ only changes the constant through its bounded derivatives on the fixed compact $(z,s)$ patch.

---

# 5. Eliminate the affine transverse component

Suppose

$$
\beta(z_0,s_0)\neq0.
$$

By continuity, after shrinking to a compact $(z,s)$ patch,

$$
|\beta|\ge\beta_0>0.
$$

Take

$$
e=\xi.
$$

Equation (3.2) gives

$$
\Omega\cdot e=-\beta
$$

on the entire horizontal plane.

Lemma D58.1 yields

$$
\boxed{
\mathcal E(CR)\gtrsim R^2.
}
\tag{5.1}
$$

This contradicts

$$
\mathcal E(R)=O(R^\kappa),
\qquad
\kappa<1.
$$

Therefore:

## Theorem D58.2 — No Affine Transverse Vorticity Offset

Every globally fixed-plane transparent tail in the DCRP30 sublinear-energy class must satisfy

$$
\boxed{
\beta(z,s)\equiv0.
}
\tag{5.2}
$$

The affine-hinge offset isolated in DCRP57 is completely removed.

---

# 6. Pure cylindrical shear after $\beta=0$

The only remaining cylindrical representation is

$$
\boxed{
q(y_h,z,s)
=
f(r,z,s)
+
c(z,s).
}
\tag{6.1}
$$

Then

$$
\boxed{
\Omega_h
=
f_r(r,z,s)\eta(z,s).
}
\tag{6.2}
$$

Suppose the vorticity is nonzero.

Then there exists an active point with

$$
f_r\neq0.
$$

By continuity there is an open $(r,z,s)$ neighborhood

$$
U
$$

on which

$$
f_r\neq0.
$$

---

# 7. Normal-vorticity preservation removes transverse dependence of $w$

DCRP42 proves the normal-vorticity preservation identity

$$
\boxed{
\Omega_h\cdot\nabla_hw=0.
}
\tag{7.1}
$$

On the pure cylindrical branch,

$$
\Omega_h=f_r\eta.
$$

Since

$$
f_r\neq0
$$

on $U$,

$$
\boxed{
\eta\cdot\nabla_hw=0.
}
\tag{7.2}
$$

But

$$
\eta\cdot\nabla_h=\partial_t.
$$

Therefore:

$$
\boxed{
\partial_tw=0
}
\tag{7.3}
$$

throughout every active cylindrical component.

Thus $w$ is constant along the complete cylinder direction, regardless of how $\eta(z,s)$ twists between slices.

---

# 8. Sublinear energy forces $w=0$ on every active component

Suppose there is an active point at which

$$
w\neq0.
$$

By continuity in $(r,z,s)$ and the identity $\partial_tw=0$, there exist:

- a compact $r$ interval $I_r$;
- compact $z,s$ intervals $J_z,I_s$;
- $\varepsilon>0$;

such that

$$
\boxed{
|w(r,t,z,s)|
\ge
\varepsilon
}
\tag{8.1}
$$

for all

$$
r\in I_r,
\quad
z\in J_z,
\quad
s\in I_s,
\quad
t\in\mathbb R.
$$

For large $R$, the region

$$
I_r
\times
[-R/2,R/2]_t
\times
J_z
$$

lies inside a ball of radius $CR$ because $(r,t)$ are orthonormal horizontal coordinates at each $z$.

Its spacetime volume is $O(R)$.

Therefore

$$
\boxed{
\mathcal E(CR)
\ge
cR.
}
\tag{8.2}
$$

This contradicts $\kappa<1$.

Hence:

## Theorem D58.3 — Active Cylindrical Vertical-Velocity Vanishing

On every active pure cylindrical component,

$$
\boxed{
w=0.
}
\tag{8.3}
$$

---

# 9. Incompressibility forces horizontal harmonicity

On the active component,

$$
w=0.
$$

The scalar definition is

$$
\boxed{
q=w-\phi_z.
}
\tag{9.1}
$$

Therefore

$$
\boxed{
q=-\phi_z.
}
\tag{9.2}
$$

Incompressibility is

$$
\boxed{
\Delta_h\phi+w_z=0.
}
\tag{9.3}
$$

Since $w$ vanishes on an open $(r,z,s)$ component,

$$
w_z=0.
$$

Thus

$$
\boxed{
\Delta_h\phi=0.
}
\tag{9.4}
$$

Differentiate in $z$:

$$
\boxed{
\Delta_h\phi_z=0.
}
\tag{9.5}
$$

Using $q=-\phi_z$,

$$
\boxed{
\Delta_hq=0.
}
\tag{9.6}
$$

But

$$
q=f(r,z,s)+c(z,s),
$$

so

$$
\boxed{
f_{rr}=0
}
\tag{9.7}
$$

on every active component.

---

# 10. Smooth one-dimensional rigidity of $f_r$

Fix $(z,s)$.

Set

$$
\boxed{
g(r)=f_r(r,z,s).
}
\tag{10.1}
$$

Equation (9.7) says

$$
\boxed{
g'(r)=0
}
\tag{10.2}
$$

wherever

$$
g(r)\neq0.
$$

Let $I$ be a connected component of

$$
\{r:g(r)\neq0\}.
$$

Then $g$ is a nonzero constant on $I$.

If $I$ had a finite endpoint $r_\ast$, continuity would give the same nonzero value at $r_\ast$, contradicting maximality of the nonzero component.

Hence every nonempty connected component is all of $\mathbb R$.

Therefore:

## Lemma D58.4 — Cylindrical Harmonic Slice Dichotomy

For each fixed $(z,s)$,

$$
\boxed{
f_r(\cdot,z,s)\equiv0
}
$$

or

$$
\boxed{
f_r(\cdot,z,s)\equiv K(z,s)\neq0
}
$$

on all of $\mathbb R$.

Thus every nonzero slice becomes horizontally uniform vorticity.

---

# 11. Uniform planar vorticity also violates sublinear energy

Suppose the second alternative of Lemma D58.4 occurs at some $(z_0,s_0)$.

By continuity there is a compact $(z,s)$ patch with

$$
|K(z,s)|\ge K_0>0.
$$

Equation (6.2) becomes

$$
\boxed{
\Omega_h(y_h,z,s)
=
K(z,s)\eta(z,s)
}
\tag{11.1}
$$

on the entire horizontal plane.

Apply Lemma D58.1 with

$$
e=\eta,
$$

$$
b=K.
$$

Then

$$
\boxed{
\mathcal E(CR)\gtrsim R^2,
}
\tag{11.2}
$$

contradicting the DCRP30 sublinear upper bound.

Therefore the nonzero alternative is impossible.

Hence:

$$
\boxed{
f_r\equiv0.
}
\tag{11.3}
$$

So

$$
\boxed{
\Omega\equiv0.
}
\tag{11.4}
$$

---

# Theorem D58.5 — Global Fixed-Plane Transparent Tail NO-GO

Let $(V,\Omega)$ be a smooth $S_0$-periodic DSS Euler profile satisfying the DCRP30 period-averaged energy bound

$$
\mathcal E(R)=O(R^\kappa),
\qquad
0<\kappa<1.
$$

Assume globally:

1. the vorticity remains in one fixed plane;
2. the fixed-plane transparency condition holds:
   $$
   \operatorname{divdiv}
   (\Omega\otimes\Omega)=0.
   $$

Then

$$
\boxed{
\Omega\equiv0.
}
\tag{11.5}
$$

Therefore there is no nonzero transparent no-rank-lift cylindrical tail in the admissible strict-Type-II energy-growth class.

This theorem includes:

- straight cylinders;
- twisting cylinders;
- affine-hinge chains;
- all DCRP56 entire cylindrical slice normal forms.

---

# 12. Relation to DCRP57

DCRP57 had proved only:

$$
\boxed{
\text{globally straight cylinder}
\Rightarrow
\Omega=0
}
$$

under the sublinear energy tail.

D58 removes the straightness hypothesis entirely.

The key additional inputs are:

- the affine transverse offset is detected by curl–energy duality;
- the pure cylindrical part is constrained by the Euler normal-vorticity equation;
- sublinear energy forces its vertical velocity to vanish;
- incompressibility then collapses the cylinder to uniform planar vorticity;
- curl–energy duality eliminates that uniform state.

Thus the twisting phase-mixing escape is closed.

---

# 13. Revisit the D55 outer-compensation dichotomy

DCRP55 gives:

$$
\boxed{
\text{finite rank-lift compensation}
\quad\vee\quad
\text{noncompact transparent tail}.
}
$$

D58 eliminates the second alternative if the branch remains globally fixed-plane and belongs to the DCRP30/Xue energy class.

Therefore:

## Corollary D58.6 — Transparent Compensation Forces Finite Rank Lift

Every nonzero globally transparent continuation of the recurrent inner rank-two null-envelope core must leave the fixed-plane rank-two class at finite normalized location.

The only transparent compensation route is the finite rank/plane lift of DCRP55/56.

---

# 14. But finite rank lift is already a residual branch

DCRP56 shows finite full transparency requires

$$
\boxed{
M^{\rm in}+M^{\rm out}
=
\rho I,
}
\tag{14.1}
$$

with

$$
\rho>0.
$$

DCRP57 inserts this isotropic rank-three covariance into the exact DCRP38 covariance ledger and proves

$$
\boxed{
R_B
=
(\rho'+c_\gamma\rho)I
-
2\rho A,
}
\tag{14.2}
$$

and the period gap

$$
\boxed{
\int_0^{S_0}
\|R_B\|_Fds
\ge
\frac{\sqrt3}{2}
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
\tag{14.3}
$$

Hence

$$
\boxed{
R_B\neq0.
}
\tag{14.4}
$$

So finite transparency exits the zero-residual covariance equality branch.

---

# 15. Outer-compensation equality closure theorem

Combine:

- D54: localized inner null-envelope visibility leakage is nonzero;
- D55: exact compensation requires finite rank lift or transparent tail;
- D57: finite rank-three compensation has nonzero covariance residual;
- D58: transparent fixed-plane tail is impossible in the admissible sublinear-energy class.

Then:

## Theorem D58.7 — Rank-Two Zero-Residual Visibility-Compensation Closure

A nonzero recurrent inner rank-two null-envelope core cannot have its X72 localization/visibility defect globally compensated while simultaneously preserving all of:

$$
\boxed{
\text{fixed rank-two plane},
}
$$

$$
\boxed{
\text{global transparency},
}
$$

and

$$
\boxed{
R_B=0.
}
$$

Any global continuation must activate at least one of:

$$
\boxed{
\text{rank-three covariance lift},
}
$$

$$
\boxed{
R_B^{na}\neq0,
}
$$

$$
\boxed{
R_B^{tr}\neq0,
}
$$

or

$$
\boxed{
\text{nonzero global X72 visibility defect}.
}
$$

The maximally rigid transparent rank-two zero-residual equality route is closed.

---

# 16. What this theorem does not prove

Theorem D58.7 is a **branch-closure theorem**, not a Navier–Stokes regularity theorem.

It does not exclude:

1. a genuine recurrent rank-three transition state;
2. non-affine strain residuals;
3. covariance turnover;
4. a nonzero X72 pressure/visibility defect;
5. other RMRM branches outside the rank-two equality route.

Those branches must be handled by the larger DCRP/RMRM/X72 proof tree.

What is removed is the possibility that the final rank-two survivor remains perfectly transparent and zero-defect all the way through the outer tail.

---

# 17. Why the curl–energy lemma is stronger than vorticity $L^p$ tests

DCRP56 proved that the transparent cylindrical tail lies outside every positive global vorticity $L^p$ class.

That alone did not contradict the DSS survivor because the branch was allowed to escape all known vorticity-integrability Liouville hypotheses.

D58 instead uses the **velocity-energy tail upper bound**.

This matters because the cylindrical geometry contains vorticity components coherent over arbitrarily long spatial directions.

Such coherence creates a nontrivial $H^{-1}$ / curl-duality footprint that cannot coexist with period-averaged velocity energy growing strictly slower than linearly.

Thus D58 closes a branch that ordinary vorticity-integrability criteria deliberately leave open.

---

# 18. The role of twisting

DCRP57 found that if the cylinder direction twists,

$$
\partial_z\Omega
$$

can grow linearly in the transverse coordinate.

One might hope that this increasing spatial frequency allows phase mixing and a small velocity field.

D58 shows why that mechanism is insufficient for the exact transparent Euler branch.

If the cylindrical representation carries the affine transverse component $\beta$, a spatially uniform vorticity projection survives and curl–energy duality kills it.

If $\beta=0$, normal-vorticity preservation makes $w$ exactly constant along the long cylinder lines.

Sublinear energy then forces $w=0$, after which incompressibility destroys the non-affine cylindrical profile.

So twisting cannot save the entire transparent branch.

---

# 19. Relationship to X72 realizability

X72 Round43 asks which actual vorticity-generated stresses can realize the full-wave-cone equality.

D52–D54 showed that the inner null-envelope stress is locally realizable.

D55–D58 now show that its global X72 visibility matching cannot stay in the same fixed rank-two identity class.

The realizability lift therefore fails at the **global transparent fixed-plane continuation** level.

The branch must lift into a different covariance rank or retain a nonzero projection defect.

This locates a concrete first non-liftable global level in the NTLA/X72 realizability tower.

---

# 20. NTLA-O interpretation

The local observer sees a valid rank-two vorticity-generated null-envelope stress.

The nonlocal X72 observer detects its localization leakage.

The global descent problem asks whether the same fixed-plane rank-two state can cover that leakage.

D55 gives two candidate descent mechanisms.

D58 proves:

- the tail descent is impossible under the global energy observer;
- the finite descent changes covariance rank and activates a dynamical residual.

Thus:

$$
\boxed{
\text{local rank-two equality}
}
$$

does not admit a transparent global descent inside the same identity class.

This is a genuine NTLA-O local-to-global realizability obstruction.

---

# 21. Updated branch state

After DCRP58, the outer visibility tree is:

## Transparent finite branch

$$
\boxed{
\text{rank-three isotropic covariance}
}
$$

with

$$
\boxed{
R_B^{na}\neq0
\quad\vee\quad
R_B^{tr}\neq0.
}
$$

## Transparent rank-two tail branch

$$
\boxed{
\text{IMPOSSIBLE under }
\mathcal E(R)=O(R^\kappa),
\quad
\kappa<1.
}
$$

## Nontransparent branch

$$
\boxed{
\text{nonzero X72 visibility/projection defect}.
}
$$

Therefore the final zero-defect rank-two branch has no transparent outer completion.

---

# 22. Status ledger

## PROVED this round

### D58-P1 — Uniform-plane vorticity / velocity-energy duality

A nonzero vorticity projection constant across the entire horizontal plane on a positive $(z,s)$ patch forces

$$
\mathcal E(R)\gtrsim R^2.
$$

### D58-P2 — Affine transverse cylindrical offset elimination

$$
\beta\equiv0.
$$

### D58-P3 — Active pure-cylinder vertical velocity vanishes

$$
f_r\neq0
\Rightarrow
w=0.
$$

### D58-P4 — Active pure-cylinder harmonic collapse

$$
w=0
\Rightarrow
f_{rr}=0.
$$

### D58-P5 — Smooth slice dichotomy

$$
f_r\equiv0
\quad\text{or}\quad
f_r\equiv K\neq0.
$$

### D58-P6 — Uniform planar vorticity elimination

The nonzero constant-$K$ alternative violates the sublinear velocity-energy tail.

### D58-P7 — Full transparent fixed-plane tail NO-GO

$$
\operatorname{divdiv}
(\Omega\otimes\Omega)=0
+
\text{fixed plane}
+
\mathcal E(R)=O(R^\kappa),\ \kappa<1
\Rightarrow
\Omega=0.
$$

### D58-P8 — Rank-two zero-residual visibility-compensation closure

The inner null-envelope leak cannot be globally compensated within the same transparent rank-two zero-residual identity class.

---

# 23. Closed / open routes

## Closed

- straight cylindrical transparent tail;
- twisting cylindrical transparent tail;
- affine-hinge transparent tail;
- any nonzero global fixed-plane transparent tail in the DCRP30 sublinear-energy class.

## Already routed to defect branch

Finite rank-three compensation.

## Still open

- quantitative closure of the resulting $R_B^{na}$ / $R_B^{tr}$ branches;
- nonzero X72 visibility defect branch;
- full rank-three RMRM/DCRP dynamics.

---

# 24. New STOP

$$
\boxed{
\textbf{
STOP-D58:
The no-rank-lift transparent tail is completely eliminated by the sublinear DSS velocity-energy law. The only finite transparent compensation is a rank-three covariance lift, which necessarily carries a nonzero DCRP38 non-affine/turnover residual. Hence the maximally rigid rank-two zero-residual visibility-compensation branch is closed.
}
}
$$

---

# 25. Next autonomous step

## DCRP59 — Residual-Branch Confluence

**Working title**

> **Rank-Three Covariance Residual, X72 Visibility Defect, and the Final DCRP/RMRM Confluence**

Primary tasks:

1. return the finite rank-three branch to the exact DCRP38 residual split
   $$
   R_B=R_B^{na}+R_B^{tr};
   $$
2. derive whether the D57 lower bound forces one residual channel individually to carry a positive period budget;
3. connect $R_B^{na}$ to X72 pressure/cofactor or strain defects;
4. connect $R_B^{tr}$ to DCRP31 PFET / material turnover;
5. formulate the rank-two branch closure as a reusable RMRM theorem;
6. determine whether the remaining residual alternatives are already covered by earlier STOP branches or create one genuinely new frontier.

Desired endpoint:

$$
\boxed{
\text{residual branch absorbed}
\ \vee\
\text{new finite obstruction}
\ \vee\
\text{RMRM rank-two closure theorem}.
}
$$

---

# 26. One-line checkpoint

The infinite transparent-tail escape has vanished entirely: sublinear DSS velocity energy plus the fixed-plane Euler structure kills every cylindrical transparent tail, so the rank-two zero-residual outer equality route is now closed and all surviving continuations are forced back into finite rank-three/non-affine/turnover or nonzero X72-defect branches.

---

**End checkpoint:** DCRP58  
**Next:** DCRP59 — Residual-Branch Confluence / RMRM Closure.
