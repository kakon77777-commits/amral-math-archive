# DCRP71 / X72-R54 — Morrey-Endpoint Audit, Phase-Lock Residual Geometry, and the Critical Twisting-Cylinder Survivor

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-scope audit + endpoint repair + next-frontier checkpoint  
**Immediate predecessor:** `NS_DCRP70_X72R53_DoubleIntegrability_StraightTubeEnergyNoGo_2026-08-18.md`

**Primary internal dependencies**
- RMRM/DCRP checkpoint v30 — bounded-reservoir Morrey growth and DSS tail classification
- DCRP-56–58 — cylindrical transparent-tail branch
- DCRP-61–70 — aligned/no-turnover X branch and phase-lock integrability
- X72 Round38–43 — transport–Riesz / cofactor / vorticity-stress geometry

**External calibration**
- Liutang Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619.
- L. Biferale, M. Buzzicotti, M. Linkmann, *From two-dimensional to three-dimensional turbulence through two-dimensional three-component flows*, arXiv:1706.02371.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

This round performs an important scope audit before continuing the apparent “endgame.”

The previous rounds used two different energy controls which must not be conflated.

## Native project Morrey control

Under the DCRP bounded-reservoir controlled-drift hypothesis, the normalized strong profile satisfies the **time-slice Morrey bound**

$$
\boxed{
\int_{B_R}
|V(y,s)|^2dy
\le
C M_0 R
\qquad
\forall R\ge1.
}
$$

This is the project-native unconditional energy control on the compact strong-profile branch.

## Xue-type sublinear DSS control

Under additional global integrability assumptions, the DSS Euler profile has the sharper energy behavior

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2
\sim
R^{3-2\alpha},
}
$$

and in Xue's stronger $L_s^3L_y^p$ class one also has a time-uniform upper bound of order

$$
R^{3-2\alpha}.
$$

For

$$
1<\alpha<\frac32,
$$

$$
0<3-2\alpha<1.
$$

This is a **conditional subbranch**.

Therefore all previous eliminations that used only

$$
R^{3-2\alpha}=o(R)
$$

must be marked conditional unless they can be repaired using the native Morrey bound.

DCRP71 does that audit.

---

## Repair 1 — D70 phase-lock NO-GO becomes stronger and native

D70 proves on the exact D69 phase-lock state:

$$
\boxed{
\nabla\xi=0,
}
$$

with

$$
S\xi=\lambda\xi,
$$

and

$$
R\xi=0.
$$

Hence

$$
\boxed{
(\xi\cdot\nabla)V
=
L\xi
=
\lambda\xi.
}
$$

Along every complete phase-lock vortex line:

$$
\boxed{
V(y+t\xi)
=
V(y)+\lambda t\xi.
}
$$

Therefore a phase-lock tube with fixed nonzero transverse cross-section satisfies

$$
\boxed{
\int_{B_R}|V|^2dy
\gtrsim
|\lambda|^2 R^3.
}
$$

This is not merely the earlier linear curl-duality lower bound.

It is cubic.

The native Morrey upper bound is only:

$$
\boxed{
\int_{B_R}|V|^2
\lesssim R.
}
$$

Thus exact globally persistent phase lock is impossible whenever

$$
\lambda\neq0,
$$

without using the Xue sublinear exponent at all.

So D70 is **repaired and strengthened**.

---

## Repair 2 — D65 pressure-source flatness is also native

If

$$
q(y,s)=q_0(s)
$$

is spatially constant, then

$$
q=\partial_i\partial_j(V_iV_j).
$$

Testing with $\chi(y/R)$ at a fixed similarity time gives:

$$
|q_0(s)|R^3
\lesssim
R^{-2}
\int_{B_{CR}}|V(y,s)|^2dy
\lesssim
R^{-1}.
$$

Hence:

$$
\boxed{
q_0(s)=0.
}
$$

Thus the Round38 source-flat null closure does not require the conditional Xue law either.

---

## Correction — D58 full transparent-tail elimination was too strong outside the Xue subbranch

The D56 transparent tail is horizontally cylindrical.

D58 correctly eliminates the affine transverse-vorticity offset because it produces a uniform plane vorticity component and forces:

$$
\boxed{
E(R)\gtrsim R^2,
}
$$

which contradicts the native Morrey bound.

But after that offset is removed, the remaining pure cylindrical branch has vertical velocity constant along the infinite cylinder direction.

If that component is nonzero:

$$
\boxed{
E(R)\gtrsim R.
}
$$

This **does not contradict**

$$
E(R)\lesssim R.
$$

It exactly saturates the native Morrey endpoint.

Therefore:

$$
\boxed{
\textbf{
D58's complete cylindrical-tail NO-GO is conditional on the stronger sublinear-energy class.
}
}
$$

For the generic native branch, the correct surviving tail is a **critical linear-Morrey cylindrical state**.

---

## New closure — the globally straight critical cylinder is nevertheless impossible

D57 proved that if the cylinder direction is globally fixed, vorticity translation symmetry forces velocity translation symmetry:

$$
\boxed{
V(y+t\eta,s)=V(y,s).
}
$$

The native Morrey bound then implies finite kinetic energy **per unit length** in the transverse plane.

Indeed, with

$$
V=V(y_\perp,s),
$$

$$
\int_{B_R^3}|V|^2
\gtrsim
R
\int_{B_{R/2}^2}|V(y_\perp,s)|^2dy_\perp.
$$

Since the left side is $O(R)$,

$$
\boxed{
\int_{\mathbb R^2}|V(y_\perp,s)|^2dy_\perp<\infty.
}
$$

The physical Euler solution is then a finite-energy-per-unit-length 2D3C flow.

Its per-unit-length kinetic energy is conserved.

Under DSS scaling in two effective spatial dimensions,

$$
\mathcal E_2(t)
=
\Lambda^{2\alpha-2}
\mathcal E_2(t').
$$

For a nonzero conserved $\mathcal E_2$ and $\Lambda\neq1$:

$$
\boxed{
\alpha=1.
}
$$

But the strict Type-II interior has

$$
\boxed{
1<\alpha<\frac32.
}
$$

Contradiction.

Thus:

$$
\boxed{
\textbf{
the globally straight critical cylindrical tail is closed even at the native linear Morrey endpoint.
}
}
$$

---

## True surviving transparent-tail normal form

The only cylindrical transparent tail not yet closed natively is therefore:

$$
\boxed{
\textbf{
a twisting / slice-dependent cylindrical state that saturates }
E(R)\sim R.
}
}
$$

Its cylinder direction cannot be globally fixed.

Its affine transverse-vorticity offset is zero.

Its line-invariant velocity component cannot be discarded merely from Morrey growth.

This is the genuine critical tail endpoint.

---

## New phase-lock transition observable

D71 also records the exact residual measuring departure from the D69 material shape-lock manifold.

On the aligned active set:

$$
\Omega=r\xi,
$$

$$
S
=
\frac{3\lambda}{2}U_\xi
+
dH,
$$

and define:

$$
c=\frac d\lambda.
$$

Let the transverse eigenframe rotate materially about $\xi$ with rate $\vartheta$:

$$
D_sH
=
2\vartheta K.
$$

Define the material shape-lock residual:

$$
\boxed{
\mathscr R_{\rm PL}
=
D_sS
-
\frac{\lambda'}{\lambda}S.
}
$$

Using the exact D69 bridge:

$$
\boxed{
\mathscr R_{\rm PL}
=
-
\left[
E_p
+
\left(
1+\frac{\lambda'}{\lambda}
\right)S
+
\frac14W_\Omega
\right].
}
$$

In spectral coordinates:

$$
\boxed{
\mathscr R_{\rm PL}
=
\lambda
\left[
(D_sc)H
+
2c\vartheta K
\right].
}
$$

Hence:

$$
\boxed{
|\mathscr R_{\rm PL}|^2
=
2\lambda^2
\left[
(D_sc)^2
+
4c^2\vartheta^2
\right].
}
$$

Together with the D61 vorticity-tilt variable

$$
D_s\xi=\frac{\tau}{r},
$$

the exact material phase-state speed is:

$$
\boxed{
\mathfrak a_X
=
\frac{|\tau|^2}{r^2}
+
\frac{|\mathscr R_{\rm PL}|^2}{2\lambda^2}
=
|D_s\xi|^2
+
(D_sc)^2
+
4c^2\vartheta^2.
}
$$

Thus:

$$
\boxed{
\mathfrak a_X=0
}
$$

is precisely the material aligned phase-lock manifold.

Any same-parent escape from D70 without material replacement must activate:

$$
\boxed{
\mathfrak a_X>0.
}
$$

This is the clean native X-transition observable for the next round.

---

## New transverse analytic structure of exact phase-lock patches

The D70 generic first-jet nullspace contains additional exact information.

Define:

$$
\boxed{
\varrho=\frac r\lambda,
}
$$

and:

$$
\boxed{
\beta
=
\frac{1+\lambda'/\lambda}{\lambda},
\qquad
b=\beta-1.
}
$$

On a fixed-time exact phase-lock patch with constant director $\xi$, choose transverse coordinates $(x_2,x_3)$.

D70's double-integrability equations are equivalent to:

$$
\boxed{
4c\,\partial_2c
=
\varrho\,\partial_2\varrho
-
b\,\partial_3\varrho,
}
$$

$$
\boxed{
4c\,\partial_3c
=
b\,\partial_2\varrho
+
\varrho\,\partial_3\varrho.
}
$$

Define:

$$
\boxed{
U
=
2c^2-\frac12\varrho^2.
}
$$

Then:

$$
\boxed{
\partial_2U
=
-b\,\partial_3\varrho,
}
$$

$$
\boxed{
\partial_3U
=
b\,\partial_2\varrho.
}
$$

But the pressure source on the phase-lock state is:

$$
\boxed{
q
=
\lambda^2
\left(
\frac32+U
\right).
}
$$

Therefore:

## Phase-Lock Cauchy–Riemann Law

$$
\boxed{
\partial_2q
=
-\lambda^2b\,\partial_3\varrho,
}
$$

$$
\boxed{
\partial_3q
=
\lambda^2b\,\partial_2\varrho.
}
$$

In particular:

$$
\boxed{
\Delta_\perp q=0.
}
$$

So the pressure source is harmonic on every exact phase-lock transverse section.

If

$$
b\neq0,
$$

then $\varrho$ is harmonic as well and:

$$
\boxed{
F(z)
=
U
-
ib\varrho
}
$$

is holomorphic in

$$
z=x_2+ix_3.
$$

If

$$
b=0,
$$

then:

$$
\boxed{
\nabla_\perp q=0.
}
$$

Thus an exact phase-lock interior is not an arbitrary local texture.

Its source/vorticity-amplitude state is a two-dimensional analytic object driven from its boundary.

This supplies a new finite-transition interpretation:

> nontrivial source complexity in an exact phase-lock patch has no bulk source; it is boundary/transition-fed.

---

## Isotropic covariance forces large director dispersion

Let:

$$
d\mu(y)
=
\phi(y)|\Omega(y)|^2dy,
$$

and:

$$
Z=\mu(\mathbb R^3).
$$

On the finite compensation state:

$$
\boxed{
B
=
\int
\xi\otimes\xi\,d\mu
=
\frac Z3I.
}
$$

Then for every fixed unit vector $n$:

$$
\boxed{
\int
\left[
1-(\xi\cdot n)^2
\right]d\mu
=
\frac{2Z}{3}.
}
$$

And for pairs:

## Exact Director-Dispersion Identity

$$
\boxed{
\iint
\left[
1-(\xi(x)\cdot\xi(y))^2
\right]
d\mu(x)d\mu(y)
=
\frac{2Z^2}{3}.
}
$$

Therefore the full-rank isotropic covariance requires a quantitatively large unoriented director dispersion.

If an exact phase-lock component has constant director $n$ and vorticity mass

$$
Z_n,
$$

then:

$$
\boxed{
Z_n\le\frac Z3.
}
$$

No single exact phase-lock director sector can carry more than one-third of the covariance mass.

Hence if the transition region carries little vorticity mass, the observer must contain at least three distinct phase-lock director sectors separated by finite X-transition regions.

This converts the finite-compensation geometry into a **director mosaic / transition-network problem**.

---

# 1. Proof-scope correction table

| Result | Previous form | Native Morrey status after D71 |
|---|---|---|
| D57 straight-cylinder energy contradiction | used $o(R)$ | **not by exponent alone** |
| D58 affine transverse offset | $R^2$ lower vs $o(R)$ | **still closed** by $R^2$ vs $R$ |
| D58 pure line-invariant $w\neq0$ | $R$ lower vs $o(R)$ | **critical survivor** |
| D58 full transparent-tail NO-GO | claimed in sublinear class | **conditional** |
| D65 constant $q$ | used period sublinear | **repaired natively** by pointwise Morrey |
| D70 phase-lock | earlier linear lower | **strengthened** to $R^3$ lower |
| D70 global phase-lock NO-GO | used sublinear class | **repaired natively** by $R^3$ vs $R$ |
| straight global cylinder | critical $R$ | **closed by 2D per-length DSS scaling** |

This audit is necessary for the global proof tree.

---

# 2. Native Morrey bound

The bounded-reservoir controlled-drift branch gives:

$$
\boxed{
\int_{B_R}
|V(y,s)|^2dy
\le
CM_0R
\qquad
\forall R\ge1.
}
\tag{2.1}
$$

This is inherited by the local strong profile at fixed similarity time.

No Xue global $L^p$ assumption is needed for (2.1).

---

# 3. Phase-lock directional velocity derivative

D70 gives:

$$
\nabla\xi=0.
$$

On the aligned branch:

$$
S\xi=\lambda\xi.
$$

Also:

$$
R\xi
=
\frac12\Omega\times\xi
=
0.
$$

Therefore:

$$
L\xi
=
(S+R)\xi
=
\lambda\xi.
$$

Since:

$$
L=\nabla V,
$$

## Theorem D71.1 — Phase-Lock Affine Velocity Along Vortex Lines

$$
\boxed{
(\xi\cdot\nabla)V
=
\lambda\xi.
}
\tag{3.1}
$$

Thus:

$$
\boxed{
V(y+t\xi)
=
V(y)+\lambda t\xi
}
\tag{3.2}
$$

through every complete exact phase-lock line.

---

# 4. Cubic phase-lock energy floor

Take a fixed transverse disk $D$ on which the phase-lock state is active.

On:

$$
D\times[-R,R]\xi,
$$

equation (3.2) gives:

$$
|V(y+t\xi)|^2
\ge
\frac12\lambda^2t^2
-
|V(y)|^2.
$$

Integrate.

The quadratic term contributes:

$$
\boxed{
\gtrsim
|D|\lambda^2R^3.
}
$$

The base term contributes only:

$$
O(R).
$$

Therefore:

## Theorem D71.2 — Cubic Phase-Lock Velocity-Energy Growth

For every nonzero-$\lambda$ complete phase-lock tube:

$$
\boxed{
\int_{B_{CR}}|V|^2dy
\ge
c_D|\lambda|^2R^3
-
C_DR.
}
\tag{4.1}
$$

Hence for large $R$:

$$
\boxed{
E(R)\gtrsim R^3.
}
$$

This contradicts the native Morrey bound $E(R)\lesssim R$.

---

# 5. Native D70 repair

Theorem D71.2 replaces the earlier reliance on the Xue exponent.

Thus:

## Corollary D71.3 — Native Phase-Lock Global NO-GO

Under the bounded-reservoir Morrey branch, no nonzero exact D69 phase-lock tube can persist globally at a time with:

$$
\lambda\neq0.
$$

The phase-lock state must hit:

$$
\mathfrak a_X>0
$$

or material turnover at finite normalized distance.

---

# 6. Native repair of pressure-source flatness

Suppose:

$$
q(y,s)=q_0(s).
$$

Use:

$$
q
=
\partial_i\partial_j(V_iV_j).
$$

At fixed $s$:

$$
q_0
\int\chi_R
=
\int
V_iV_j
\partial_i\partial_j\chi_R.
$$

The LHS is:

$$
\sim
q_0R^3.
$$

The RHS is:

$$
\lesssim
R^{-2}
\int_{B_{CR}}|V|^2
\lesssim
R^{-1}.
$$

Therefore:

## Theorem D71.4 — Native Pressure-Source Flatness NO-GO

$$
\boxed{
q_0(s)=0.
}
\tag{6.1}
$$

No period-averaged sublinear assumption is needed.

---

# 7. Audit of the cylindrical tail

D56 produces the cylindrical transparent tail:

$$
q_{\rm sh}
=
f(r,z,s)
+
\beta_{\rm cyl}(z,s)t
+
c_0(z,s),
$$

with vorticity:

$$
\Omega_h
=
f_r\eta
-
\beta_{\rm cyl}\xi.
$$

D58's curl-duality test gives:

$$
\beta_{\rm cyl}\neq0
\Longrightarrow
E(R)\gtrsim R^2.
$$

Thus the native Morrey bound forces:

$$
\boxed{
\beta_{\rm cyl}=0.
}
\tag{7.1}
$$

The survivor is:

$$
\boxed{
\Omega_h=f_r\eta.
}
\tag{7.2}
$$

Normal-vorticity preservation gives:

$$
\boxed{
\partial_tw=0
}
\tag{7.3}
$$

on active cylindrical regions.

If:

$$
w\neq0,
$$

then:

$$
E(R)\gtrsim R.
$$

This is compatible with the native upper:

$$
E(R)\lesssim R.
$$

Therefore this branch is critical, not eliminated.

---

# 8. Global straight cylinder gives a 2D3C flow

Assume the cylinder direction is globally fixed:

$$
\eta=\eta_0.
$$

D57's harmonic translation-difference argument only needs sub-cubic energy growth, so the native Morrey bound is enough to conclude:

$$
\boxed{
V(y+t\eta_0,s)
=
V(y,s).
}
\tag{8.1}
$$

Thus the Euler profile is 2D3C.

Choose coordinates:

$$
x=(x_\perp,z),
$$

with $z$ along $\eta_0$.

Then:

$$
\boxed{
\partial_zV=0.
}
\tag{8.2}
$$

---

# 9. Morrey implies finite energy per unit length

Let:

$$
\mathcal E_2(R,s)
=
\int_{|x_\perp|\le R}
|V(x_\perp,s)|^2dx_\perp.
$$

The 3D ball contains a cylinder:

$$
B_{R/2}^2
\times
[-R/2,R/2].
$$

Therefore:

$$
\int_{B_R^3}|V|^2
\ge
R
\mathcal E_2(R/2,s).
$$

Using the Morrey bound:

$$
R\mathcal E_2(R/2,s)
\le
CM_0R.
$$

Hence:

$$
\boxed{
\mathcal E_2(R,s)
\le
CM_0.
}
$$

Let $R\to\infty$:

## Theorem D71.5 — Finite Cross-Sectional Energy

$$
\boxed{
\mathcal E_2(s)
=
\int_{\mathbb R^2}
|V(x_\perp,s)|^2dx_\perp
<
\infty.
}
\tag{9.1}
$$

The globally straight critical cylinder has finite kinetic energy per unit invariant length.

---

# 10. 2D3C energy conservation

For a smooth translation-invariant Euler flow:

$$
V=V(x_\perp,t),
$$

the local energy equation reduces to a two-dimensional divergence:

$$
\partial_t
\frac{|v|^2}{2}
+
\nabla_\perp\cdot
\left[
\left(
\frac{|v|^2}{2}+p
\right)
v_\perp
\right]
=
0.
$$

Under finite per-length energy and the canonical smooth pressure class:

$$
\boxed{
\mathcal E_2(t)
=
\int_{\mathbb R^2}
|v(x_\perp,t)|^2dx_\perp
}
$$

is conserved.

This includes the third velocity component; it is advected by the in-plane incompressible velocity.

---

# 11. DSS scaling in effective dimension two

For a DSS factor:

$$
\Lambda>1,
$$

the physical scaling is:

$$
v(x,t)
=
\Lambda^\alpha
v(
\Lambda x,
t'
).
$$

Because the solution is invariant in one spatial direction, the per-unit-length energy scales only over two coordinates:

$$
\begin{aligned}
\mathcal E_2(t)
&=
\int_{\mathbb R^2}
\Lambda^{2\alpha}
|v(\Lambda x_\perp,t')|^2dx_\perp
\\
&=
\Lambda^{2\alpha-2}
\mathcal E_2(t').
\end{aligned}
$$

Energy conservation and nonzero $\mathcal E_2$ give:

## Theorem D71.6 — Effective-Dimension DSS Energy Rigidity

$$
\boxed{
\Lambda^{2\alpha-2}=1
}
$$

and therefore:

$$
\boxed{
\alpha=1.
}
\tag{11.1}
$$

---

# 12. Straight critical cylinder is excluded in the strict interior

The strict Type-II branch has:

$$
1<\alpha<\frac32.
$$

Thus Theorem D71.6 gives:

## Corollary D71.7 — Global Straight-Cylinder NO-GO at the Morrey Endpoint

A nonzero globally straight transparent cylindrical tail cannot occur in the strict Type-II interior.

This closure uses:

- native linear Morrey;
- finite energy per invariant length;
- 2D3C energy conservation;
- DSS scaling.

It does not use Xue's sublinear exponent.

---

# 13. The true transparent-tail survivor

After the native audit, the transparent tail must satisfy all of:

$$
\boxed{
\beta_{\rm cyl}=0,
}
$$

$$
\boxed{
\partial_tw=0,
}
$$

$$
\boxed{
E(R)\sim R
\text{ at the critical Morrey scale},
}
$$

and:

$$
\boxed{
\text{the cylinder direction is not globally fixed}.
}
$$

Thus the surviving tail is:

## Critical Twisting-Cylinder Tail

$$
\boxed{
\mathsf C_{\rm twist}^{\rm crit}.
}
$$

This is the true generic tail endpoint left by D56–58 after removing the conditional Xue shortcut.

---

# 14. Material phase-lock residual

Return to the finite X branch.

Let:

$$
c=\frac d\lambda.
$$

Let the transverse eigenframe rotate materially around $\xi$ with angular rate $\vartheta$.

Then:

$$
D_sH=2\vartheta K.
$$

Since:

$$
S=\frac{3\lambda}{2}U_\xi+\lambda cH,
$$

and $D_sU_\xi=0$ under alignment,

$$
D_sS
=
\frac{\lambda'}{\lambda}S
+
\lambda(D_sc)H
+
2\lambda c\vartheta K.
$$

Therefore:

## Theorem D71.8 — Exact Phase-Lock Residual

$$
\boxed{
\mathscr R_{\rm PL}
:=
D_sS-\frac{\lambda'}{\lambda}S
=
\lambda(D_sc)H
+
2\lambda c\vartheta K.
}
\tag{14.1}
$$

Using D69:

$$
\boxed{
\mathscr R_{\rm PL}
=
-
\left[
E_p
+
\left(
1+\frac{\lambda'}{\lambda}
\right)S
+
\frac14W_\Omega
\right].
}
\tag{14.2}
$$

And:

$$
\boxed{
|\mathscr R_{\rm PL}|^2
=
2\lambda^2
\left[
(D_sc)^2
+
4c^2\vartheta^2
\right].
}
\tag{14.3}
$$

---

# 15. Full material phase-state action

D61 gives:

$$
D_s\xi=\tau/r.
$$

Define:

$$
\boxed{
\mathfrak a_X
=
|D_s\xi|^2
+
(D_sc)^2
+
4c^2\vartheta^2.
}
\tag{15.1}
$$

Equivalently:

$$
\boxed{
\mathfrak a_X
=
\frac{|\tau|^2}{r^2}
+
\frac{|\mathscr R_{\rm PL}|^2}{2\lambda^2}.
}
\tag{15.2}
$$

Thus:

## Theorem D71.9 — Exact X-Transition Metric

On the nondegenerate active set:

$$
\boxed{
\mathfrak a_X=0
}
$$

if and only if the material state remains:

- strain/vorticity aligned;
- fixed vorticity director;
- fixed transverse shape ratio;
- fixed transverse eigenframe modulo its irrelevant sign/gauge.

D70/D71 prove that this zero-action state cannot continue globally.

Therefore every same-parent non-turnover continuation must activate:

$$
\boxed{
\mathfrak a_X>0
}
$$

somewhere.

---

# 16. D70 transverse first-jet equations

On an exact phase-lock patch define:

$$
\boxed{
\varrho=\frac r\lambda,
}
$$

and:

$$
\boxed{
\beta
=
\frac{1+\lambda'/\lambda}{\lambda},
\qquad
b=\beta-1.
}
$$

The D70 nullspace gives:

$$
\boxed{
4c\,c_2
=
\varrho\varrho_2-b\varrho_3,
}
\tag{16.1}
$$

$$
\boxed{
4c\,c_3
=
b\varrho_2+\varrho\varrho_3.
}
\tag{16.2}
$$

---

# 17. Phase-lock Cauchy–Riemann law

Define:

$$
\boxed{
U
=
2c^2-\frac12\varrho^2.
}
\tag{17.1}
$$

Then:

$$
\boxed{
U_2=-b\varrho_3,
}
$$

$$
\boxed{
U_3=b\varrho_2.
}
\tag{17.2}
$$

The pressure source is:

$$
q
=
\lambda^2
\left(
\frac32+2c^2-\frac12\varrho^2
\right).
$$

Hence:

$$
\boxed{
q
=
\lambda^2
\left(
\frac32+U
\right).
}
\tag{17.3}
$$

Therefore:

## Theorem D71.10 — Transverse Harmonic Source Law

$$
\boxed{
q_2
=
-\lambda^2b\,\varrho_3,
}
$$

$$
\boxed{
q_3
=
\lambda^2b\,\varrho_2.
}
\tag{17.4}
$$

Hence:

$$
\boxed{
\Delta_\perp q=0.
}
\tag{17.5}
$$

If $b\neq0$:

$$
\boxed{
\Delta_\perp\varrho=0,
}
$$

and:

$$
\boxed{
F(z)
=
U-ib\varrho
}
$$

is holomorphic in the transverse complex coordinate.

If $b=0$:

$$
\boxed{
\nabla_\perp q=0.
}
$$

---

# 18. Boundary-fed source interpretation

A harmonic source has no interior creation in the transverse plane.

Therefore every nonconstant phase-lock source profile is determined by transition-boundary data.

If the exact phase-lock domain were a complete transverse plane and $b\neq0$, then:

$$
2c^2
=
U+\frac12\varrho^2
\ge0.
$$

Writing:

$$
F=U+iv,
\qquad
v=-b\varrho,
$$

the image lies in the proper parabolic domain:

$$
\boxed{
U+\frac{v^2}{2b^2}\ge0.
}
$$

An entire holomorphic map from $\mathbb C$ into this proper simply connected domain is constant after conformal mapping to the unit disk and Liouville's theorem.

Thus:

## Theorem D71.11 — Entire Transverse Phase-Lock Rigidity

For $b\neq0$, an exact phase-lock state defined on the complete transverse plane must have:

$$
\boxed{
\varrho,c,q
\text{ spatially constant}.
}
$$

Nontrivial phase-lock texture is therefore intrinsically a bounded-domain / transition-fed phenomenon.

---

# 19. Exact isotropic director dispersion

Let:

$$
d\mu
=
\phi mdy.
$$

Set:

$$
Z=\int d\mu.
$$

Finite compensation gives:

$$
\boxed{
\int
\xi\otimes\xi\,d\mu
=
\frac Z3I.
}
\tag{19.1}
$$

For every unit $n$:

$$
\boxed{
\int
(\xi\cdot n)^2d\mu
=
\frac Z3.
}
\tag{19.2}
$$

Therefore:

$$
\boxed{
\int
\left[
1-(\xi\cdot n)^2
\right]d\mu
=
\frac{2Z}{3}.
}
\tag{19.3}
$$

For pairs:

$$
\begin{aligned}
\iint
(\xi_x\cdot\xi_y)^2
d\mu_xd\mu_y
&=
\operatorname{tr}
\left[
\left(
\int
\xi\otimes\xi\,d\mu
\right)^2
\right]
\\
&=
\frac{Z^2}{3}.
\end{aligned}
$$

Hence:

## Theorem D71.12 — Exact Pair Director-Dispersion Budget

$$
\boxed{
\iint
\left[
1-(\xi_x\cdot\xi_y)^2
\right]
d\mu_xd\mu_y
=
\frac{2Z^2}{3}.
}
\tag{19.4}
$$

The isotropic state is maximally non-single-axis at second moment.

---

# 20. Constant-director component capacity

Let $A$ be a phase-lock component with constant unoriented director $n$:

$$
\xi=\pm n.
$$

Let:

$$
Z_A=\mu(A).
$$

Then:

$$
\frac Z3
=
n^TBn
\ge
Z_A.
$$

Therefore:

## Theorem D71.13 — One-Third Director Capacity

$$
\boxed{
Z_A
\le
\frac Z3.
}
\tag{20.1}
$$

No one exact phase-lock director sector can carry more than one-third of the vorticity covariance mass.

If the transition mass is $Z_T$, and the rest is partitioned among $N$ phase-lock director sectors:

$$
Z-Z_T
\le
N\frac Z3.
$$

Hence:

$$
\boxed{
N
\ge
3
\left(
1-\frac{Z_T}{Z}
\right).
}
\tag{20.2}
$$

In particular, if:

$$
Z_T<\frac Z3,
$$

then at least three distinct director sectors are required.

---

# 21. Corrected global branch tree

After the D71 audit, the strongest native branch statement is:

$$
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X_{\rm active}
\vee
\mathsf T
\vee
\mathsf C_{\rm twist}^{\rm crit}.
}
\tag{21.1}
$$

Where:

### $\mathsf X_{\rm active}$

finite pressure/cofactor/shape/tilt transition with:

$$
\mathfrak a_X>0.
$$

### $\mathsf T$

same-parent material replacement / inward turnover.

### $\mathsf C_{\rm twist}^{\rm crit}$

noncompact transparent twisting-cylinder tail saturating:

$$
E(R)\sim R.
$$

Under the stronger Xue-admissible sublinear class:

$$
\mathsf C_{\rm twist}^{\rm crit}
$$

is excluded and the tree reduces to:

$$
\boxed{
\mathsf X_{\rm active}\vee\mathsf T.
}
$$

This is the correct conditional/unconditional separation.

---

# 22. Why this audit matters

The apparent proof-domain narrowing remains real, but the endpoint must be stated correctly.

The generic project branch is **not yet** reduced to only X/T.

There is one additional critical Morrey tail:

$$
\boxed{
\mathsf C_{\rm twist}^{\rm crit}.
}
$$

This is not a broad unexplored Euler class.

It is already highly constrained:

- fixed-plane transparent stress;
- no affine transverse-vorticity offset;
- line-invariant velocity component;
- non-global cylinder direction;
- exact linear Morrey saturation;
- all global straight-cylinder reductions excluded.

That is a legitimate “endgame problem domain,” not a solved branch.

---

# 23. Status ledger

## REPAIRED / STRENGTHENED

### D70

Global exact phase-lock is excluded by:

$$
E(R)\gtrsim R^3
$$

versus native:

$$
E(R)\lesssim R.
$$

No Xue assumption needed.

### D65 N2

Spatially constant pressure source is excluded pointwise using native Morrey.

### straight cylindrical tail

Closed by finite per-length energy + effective 2D DSS energy scaling:

$$
\alpha=1.
$$

## CORRECTED

### D58 full transparent-tail NO-GO

Unconditional closure was too strong.

The pure line-invariant branch only gives:

$$
E(R)\gtrsim R,
$$

which saturates native Morrey.

Full elimination remains valid only in the stronger sublinear-energy class.

## NEW

### D71-P1

Exact phase-lock residual metric:

$$
\mathfrak a_X
=
|D_s\xi|^2
+
(D_sc)^2
+
4c^2\vartheta^2.
$$

### D71-P2

Exact phase-lock Cauchy–Riemann law and transverse harmonic pressure source.

### D71-P3

Entire transverse holomorphic phase-lock rigidity.

### D71-P4

Exact isotropic director-dispersion budget:

$$
2Z^2/3.
$$

### D71-P5

One-third phase-lock director-sector capacity.

---

# 24. New STOP

$$
\boxed{
\textbf{
STOP-D71:
The endgame survives the audit but its unconditional frontier is slightly wider than D70's previous summary. Native Morrey control is strong enough to kill exact phase lock (indeed phase lock produces cubic, not linear, velocity-energy growth), to kill pressure-source flatness, and—via effective two-dimensional DSS energy conservation—to kill a globally straight cylindrical tail. But a twisting transparent cylinder can still saturate the critical linear Morrey bound. The true generic frontier is therefore active X72 transition, material turnover, or one critical twisting-cylinder tail; exact phase-lock interiors additionally obey a transverse holomorphic pressure/vorticity-amplitude law and isotropic covariance forces a large multi-director transition network.
}
}
$$

---

# 25. Next autonomous step

## DCRP72 / X72-R55 — Critical Twisting-Cylinder Morrey Endpoint

**Working title**

> **Linear-Morrey Saturation, Slice-Dependent Cylinder Direction, and Effective-Dimension Defect**

Primary tasks:

1. take the surviving native tail:

   $$
   \mathsf C_{\rm twist}^{\rm crit};
   $$

2. write its exact cylindrical form after $\beta_{\rm cyl}=0$;
3. use the native Morrey equality scale:

   $$
   E(R)\asymp R;
   $$

4. define kinetic energy per instantaneous cylinder length;
5. quantify the failure of a global invariant direction by the twist $\theta_z$;
6. test whether nonzero $\theta_z$ necessarily produces:
   - extra transverse kinetic energy above the $R$ endpoint;
   - nonzero pressure-source transition;
   - or X72 correlation defect;
7. classify the exact equality case of linear Morrey saturation;
8. if twist must vanish, D71.7 closes the tail and the generic frontier reduces again to:

   $$
   \mathsf X_{\rm active}\vee\mathsf T.
   $$

Desired endpoint:

$$
\boxed{
\mathsf C_{\rm twist}^{\rm crit}
\Longrightarrow
\text{superlinear Morrey growth}
\vee
\text{active X defect}
\vee
\text{straight 2D3C mode}.
}
$$

---

# 26. One-line checkpoint

The proof-tree audit leaves one honest native endpoint beyond X/T: a twisting transparent cylinder that exactly saturates the linear Morrey bound; straight cylinders are already excluded by effective-2D DSS energy conservation, while finite phase-lock branches are natively excluded even more strongly by cubic velocity-energy growth.

---

**End checkpoint:** DCRP71 / X72-R54  
**Next:** DCRP72 / X72-R55 — Critical Twisting-Cylinder Morrey Endpoint.
