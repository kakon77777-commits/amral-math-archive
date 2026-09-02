# DCRP52 — Null-Hessian Envelope Integrability, Finite Caustic/Transition, and the X72 Vorticity-Realizability Lift

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / null-Hessian integrability + X72 handoff  
**Immediate predecessor:** `NS_DCRP51_WavePseudoEikonal_NullHessian_Rigidity_2026-08-17.md`

**Primary internal dependencies**
- DCRP-50 — central perfect-response wave–pseudo-eikonal system and exact-affine NO-GO
- DCRP-51 — positive pseudo-eikonal sector, rank-one null-Hessian survivor cone
- X72 Round43 — vorticity-stress nonlinear realizability cone / STOP-C47

**Literature calibration**
A current web search was attempted before this round but the search service returned an availability error. The round therefore uses only the already-established internal equations and classical local differential-geometric arguments; no new external novelty claim is made.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP51 left the maximally rigid central perfect-pressure-response survivor at each fixed similarity time in the system

$$
\boxed{
u_{zz}=\Delta_hu,
}
$$

$$
\boxed{
|\nabla_hu|^2-\frac32u_z^2=C(s)>0,
}
$$

with every genuinely non-affine point satisfying

$$
\boxed{
D_y^2u
=
\kappa\,\ell\otimes\ell,
}
$$

where

$$
\boxed{
\ell^\top G\ell=0,
\qquad
G=\operatorname{diag}(1,1,-1),
}
$$

and

$$
\boxed{
\ell^\top M\nabla u=0,
\qquad
M=\operatorname{diag}\left(1,1,-\frac32\right).
}
$$

DCRP52 asks whether Hessian integrability kills this rank-one null cone.

It does **not** kill it locally.

Instead, the spatial system admits an exact local envelope normal form.

On every connected non-affine rank-one patch there exist:

- a scalar parameter $\tau$;
- a gradient curve
  $$
  g:I\to\mathbb R^3;
  $$
- a support function
  $$
  h:I\to\mathbb R;
  $$

such that

$$
\boxed{
u(y)
=
g(\tau)\cdot y+h(\tau),
}
$$

with $\tau$ determined implicitly by

$$
\boxed{
g'(\tau)\cdot y+h'(\tau)=0.
}
$$

The gradient and Hessian are

$$
\boxed{
\nabla u=g(\tau),
}
$$

and

$$
\boxed{
D^2u
=
-
\frac{
g'(\tau)\otimes g'(\tau)
}{
g''(\tau)\cdot y+h''(\tau)
}.
}
$$

The wave–pseudo-eikonal system is then **exactly equivalent** to the two gradient-space constraints

$$
\boxed{
g^\top Mg=C,
}
$$

and

$$
\boxed{
g'^\top Gg'=0.
}
$$

Thus the nonlinear spatial survivors are precisely developable envelopes of tangent planes whose normal/gradient curve:

1. lies on the pseudo-eikonal hyperboloid;
2. moves along a wave-null direction.

This proves that unconditional local affine rigidity is false in the positive-$C$ sector.

For $\beta=3/2$, a convenient parameterization is

$$
\boxed{
g(\eta)
=
\left(
\sqrt C\cosh\eta\cos\theta(\eta),
\sqrt C\cosh\eta\sin\theta(\eta),
\sqrt{\frac{2C}{3}}\sinh\eta
\right),
}
$$

with null-tangent condition

$$
\boxed{
(\theta')^2
=
\frac23-\tanh^2\eta.
}
$$

Hence local nonlinear gradient curves genuinely exist for

$$
\boxed{
|\tanh\eta|<\sqrt{\frac23}.
}
$$

The second major result is a global-extension obstruction.

A nonzero wave-null tangent direction cannot remain constant along a non-affine pseudo-eikonal gradient curve.

Therefore every non-affine gradient curve must bend.

At any parameter value where $g'$ and $g''$ are independent, the envelope equations

$$
g'\cdot y+h'=0,
$$

$$
g''\cdot y+h''=0
$$

have an affine line of finite solutions.

On that line the envelope denominator vanishes:

$$
\boxed{
g''\cdot y+h''=0.
}
$$

Hence the implicit envelope chart loses regularity there.

Therefore:

> **A genuinely non-affine central perfect-response null-Hessian chart cannot extend as one smooth single-valued rank-one envelope over all of $\mathbb R^3$.**

Any global continuation must encounter at finite normalized position at least one of:

- rank drop;
- branch/chart transition;
- loss of perfect pressure response;
- loss of central scalar flatness;
- loss of the rank-two planar representation.

This converts the null-Hessian survivor from a possible global equality state into a **local developable chart with a mandatory finite transition/caustic frontier**.

The third result is the X72 realizability audit.

For the central branch,

$$
\boxed{
\Omega
=
(\partial_2u,-\partial_1u,0).
}
$$

Therefore:

$$
\boxed{
\nabla\cdot\Omega=0
}
$$

identically, and because $C>0$,

$$
\boxed{
|\Omega|^2
=
|\nabla_hu|^2
\ge C>0.
}
$$

The associated X72 vorticity stress

$$
\boxed{
W_\Omega
=
\Omega\otimes\Omega
-
\frac13|\Omega|^2I
}
$$

automatically satisfies the full pointwise axisymmetric realizability identities

$$
\boxed{
|W_\Omega|^2
=
\frac23|\Omega|^4,
}
$$

$$
\boxed{
\det W_\Omega
=
\frac2{27}|\Omega|^6,
}
$$

and

$$
\boxed{
54(\det W_\Omega)^2
=
|W_\Omega|^6.
}
$$

Thus the DCRP central null-Hessian branch **passes** the X72 Round43 pointwise vorticity-stress algebraic cone and the divergence-free-generator test by construction.

The X72 STOP-C47 gap therefore does not kill this survivor at the pointwise algebraic level.

The first remaining lift is higher:

$$
\boxed{
\textbf{
local developable vorticity realization}
\rightarrow
\textbf{
global/same-parent dynamic realization across the finite caustic transition}.
}
}
$$

This is the new frontier.

---

# 1. Fixed-time spatial system

Fix a similarity time $s$ in the active central perfect-response branch.

DCRP51 gives

$$
\boxed{
C=C(s)=12M_a(s)>0.
}
\tag{1.1}
$$

The shifted scalar

$$
u=q-4a(s)z
$$

satisfies

$$
\boxed{
L_Gu=0,
}
\tag{1.2}
$$

where

$$
L_G
=
\partial_1^2+\partial_2^2-\partial_z^2,
$$

and

$$
\boxed{
\nabla u^\top M\nabla u=C,
}
\tag{1.3}
$$

with

$$
M
=
\operatorname{diag}
\left(
1,1,-\frac32
\right).
$$

At every genuinely non-affine point,

$$
\boxed{
\operatorname{rank}D^2u=1.
}
\tag{1.4}
$$

---

# 2. Constant-rank gradient image

Let

$$
\Omega_0
$$

be a connected open region on which

$$
\operatorname{rank}D^2u=1.
$$

The gradient map

$$
\boxed{
\nabla u:\Omega_0\to\mathbb R^3
}
$$

has rank one.

By the constant-rank theorem, locally its image is a smooth curve.

Thus there exist a scalar parameter

$$
\tau=\tau(y)
$$

and a regular curve

$$
\boxed{
g(\tau)\in\mathbb R^3
}
$$

such that

$$
\boxed{
\nabla u(y)=g(\tau(y)).
}
\tag{2.1}
$$

---

# 3. Symmetry forces one-dimensional differential variation

Differentiate (2.1):

$$
D^2u
=
g'(\tau)\otimes\nabla\tau.
$$

Because $D^2u$ is symmetric and nonzero, the two vectors must be parallel.

Hence there exists a nonzero scalar field $\lambda(y)$ such that

$$
\boxed{
\nabla\tau
=
\lambda(y)g'(\tau).
}
\tag{3.1}
$$

Therefore

$$
\boxed{
D^2u
=
\lambda(y)
g'(\tau)\otimes g'(\tau).
}
\tag{3.2}
$$

This is the integrability origin of the DCRP51 rank-one factorization.

---

# 4. Support function and envelope representation

Consider the scalar

$$
u(y)-g(\tau)\cdot y.
$$

Along a tangent vector $v$ to a level set of $\tau$,

$$
d\tau(v)=0.
$$

Then

$$
du(v)
=
g(\tau)\cdot v,
$$

so

$$
d
\left[
u-g(\tau)\cdot y
\right](v)
=
0.
$$

Hence the difference is constant on every connected level set of $\tau$.

Therefore there exists a one-variable function

$$
h(\tau)
$$

such that

$$
\boxed{
u(y)
=
g(\tau(y))\cdot y+h(\tau(y)).
}
\tag{4.1}
$$

Differentiate with respect to $y$.

Since $\nabla u=g(\tau)$, the coefficient multiplying $\nabla\tau$ must vanish:

$$
\boxed{
g'(\tau)\cdot y+h'(\tau)=0.
}
\tag{4.2}
$$

Thus the solution is the envelope of the family of planes

$$
\boxed{
u_\tau(y)=g(\tau)\cdot y+h(\tau).
}
$$

---

# 5. Exact Hessian formula

Differentiate the stationarity condition (4.2):

$$
\left[
g''(\tau)\cdot y+h''(\tau)
\right]
\nabla\tau
+
g'(\tau)
=
0.
$$

Define

$$
\boxed{
D(\tau,y)
=
g''(\tau)\cdot y+h''(\tau).
}
\tag{5.1}
$$

On a regular envelope chart,

$$
D\neq0.
$$

Then

$$
\boxed{
\nabla\tau
=
-\frac{
g'(\tau)
}{
D(\tau,y)
}.
}
\tag{5.2}
$$

Therefore

$$
\boxed{
D^2u
=
-
\frac{
g'(\tau)\otimes g'(\tau)
}{
D(\tau,y)
}.
}
\tag{5.3}
$$

This is the exact local developable-envelope Hessian.

---

# 6. Gradient-space pseudo-eikonal constraint

Because

$$
\nabla u=g(\tau),
$$

the pseudo-eikonal equation becomes simply

$$
\boxed{
g(\tau)^\top Mg(\tau)=C.
}
\tag{6.1}
$$

Differentiate:

$$
\boxed{
g'(\tau)^\top Mg(\tau)=0.
}
\tag{6.2}
$$

Thus the gradient curve lies on the two-dimensional quadric

$$
\boxed{
\mathcal H_C
=
\left\{
g:
g^\top Mg=C
\right\},
}
$$

and $g'$ is tangent to it.

---

# 7. Gradient-space wave-null constraint

Using (5.3),

$$
L_Gu
=
\operatorname{tr}
\left(
GD^2u
\right)
=
-
\frac{
g'^\top Gg'
}{
D
}.
$$

Therefore the wave equation is equivalent to

$$
\boxed{
g'^\top Gg'=0.
}
\tag{7.1}
$$

So the tangent of the gradient curve is null for the wave metric.

This is exactly the DCRP51 null-Hessian condition, now integrated.

---

# Theorem D52.1 — Local Null-Envelope Classification

Let $C>0$.

Every $C^3$ non-affine solution of

$$
L_Gu=0,
$$

$$
\nabla u^\top M\nabla u=C
$$

on a rank-one Hessian patch is locally an envelope

$$
\boxed{
u=g(\tau)\cdot y+h(\tau),
}
$$

where

$$
\boxed{
g^\top Mg=C,
}
$$

$$
\boxed{
g'^\top Gg'=0,
}
$$

and

$$
\boxed{
g'\cdot y+h'=0.
}
$$

Conversely, any regular pair $(g,h)$ satisfying these relations and

$$
D=g''\cdot y+h''\neq0
$$

generates a local solution of the simultaneous wave–pseudo-eikonal system.

Thus the DCRP51 survivor cone is locally integrable and admits a complete one-parameter developable-envelope normal form.

---

# 8. Explicit hyperboloid parameterization

For

$$
M=\operatorname{diag}
\left(
1,1,-\frac32
\right),
$$

write the pseudo-eikonal hyperboloid as

$$
\boxed{
g(\eta)
=
\left(
\rho(\eta)\cos\theta(\eta),
\rho(\eta)\sin\theta(\eta),
r(\eta)
\right),
}
\tag{8.1}
$$

with

$$
\boxed{
\rho(\eta)
=
\sqrt C\cosh\eta,
}
\tag{8.2}
$$

and

$$
\boxed{
r(\eta)
=
\sqrt{\frac{2C}{3}}\sinh\eta.
}
\tag{8.3}
$$

Then automatically

$$
\rho^2-\frac32r^2=C.
$$

---

# 9. Null-tangent ODE

Compute

$$
g'^\top Gg'
=
\rho'^2+\rho^2(\theta')^2-r'^2.
$$

Using (8.2)–(8.3),

$$
g'^\top Gg'=0
$$

becomes

$$
\boxed{
(\theta')^2
=
\frac23-\tanh^2\eta.
}
\tag{9.1}
$$

Thus real null gradient curves exist whenever

$$
\boxed{
|\tanh\eta|
\le
\sqrt{\frac23}.
}
\tag{9.2}
$$

The strict inequality gives a genuinely rotating horizontal gradient direction.

This explicitly proves that the positive-$C$ local survivor class is nonempty as a spatial wave–pseudo-eikonal system.

---

# 10. DCRP51 bounds recovered exactly

From (8.3),

$$
r^2
=
\frac{2C}{3}\sinh^2\eta.
$$

Condition (9.2) is equivalent to

$$
\boxed{
r^2
\le
\frac{4C}{3}.
}
\tag{10.1}
$$

Also

$$
|\nabla_hu|^2
=
\rho^2
=
C+\frac32r^2.
$$

Therefore

$$
\boxed{
C
\le
|\nabla_hu|^2
\le
3C.
}
\tag{10.2}
$$

This reproduces the DCRP51 non-affine gradient corridor.

Because

$$
\Omega_h=J\nabla_hu,
$$

we obtain:

## Corollary D52.2 — Perfect-Response Vorticity Corridor

On every non-affine central perfect-response null-envelope point,

$$
\boxed{
C
\le
|\Omega_h|^2
\le
3C.
}
\tag{10.3}
$$

Since

$$
C=12M_a,
$$

$$
\boxed{
12M_a
\le
|\Omega_h|^2
\le
36M_a.
}
\tag{10.4}
$$

Thus the temporal logistic margin $M_a$ and local vorticity amplitude are pointwise equivalent up to the fixed factor $3$ on the nonlinear envelope branch.

---

# 11. A constant null direction cannot support non-affinity

Suppose, on a non-affine interval of the gradient curve,

$$
\boxed{
g'(\tau)
=
\lambda(\tau)\ell_0
}
\tag{11.1}
$$

for one fixed nonzero direction $\ell_0$.

The wave constraint gives

$$
\boxed{
\ell_0^\top G\ell_0=0.
}
\tag{11.2}
$$

Because the pseudo-eikonal norm is constant,

$$
g'^\top Mg=0.
$$

Hence

$$
\ell_0^\top Mg=0.
$$

Differentiate in $\tau$:

$$
\boxed{
\lambda
\ell_0^\top M\ell_0=0.
}
\tag{11.3}
$$

But a nonzero $G$-null vector satisfies

$$
|\ell_{0,h}|^2=\ell_{0,z}^2.
$$

Therefore

$$
\begin{aligned}
\ell_0^\top M\ell_0
&=
|\ell_{0,h}|^2
-\frac32\ell_{0,z}^2
\\
&=
-\frac12\ell_{0,z}^2.
\end{aligned}
$$

A nonzero $G$-null vector cannot have $\ell_{0,z}=0$.

Thus

$$
\boxed{
\ell_0^\top M\ell_0<0.
}
\tag{11.4}
$$

Equation (11.3) forces

$$
\lambda=0,
$$

contradicting non-affinity.

---

# Theorem D52.3 — No Constant-Direction Nonlinear Null Envelope

The null tangent direction $g'/|g'|$ of a non-affine central perfect-response gradient curve cannot remain constant on any open parameter interval.

Every genuine nonlinear envelope necessarily bends in gradient space.

This is the key input for the finite caustic/transition result.

---

# 12. Envelope caustic equations

The regular envelope parameter $\tau$ is defined by

$$
\boxed{
F(\tau,y)
=
g'(\tau)\cdot y+h'(\tau)
=
0.
}
\tag{12.1}
$$

The implicit-function denominator is

$$
\boxed{
F_\tau
=
g''(\tau)\cdot y+h''(\tau)
=
D(\tau,y).
}
\tag{12.2}
$$

A fold/caustic candidate satisfies simultaneously

$$
\boxed{
F=0,
}
\tag{12.3}
$$

and

$$
\boxed{
F_\tau=0.
}
\tag{12.4}
$$

At such a point the explicit Hessian formula (5.3) loses regularity.

---

# 13. Finite caustic line for a bending gradient curve

Let $\tau_0$ be a parameter at which

$$
g'(\tau_0)
$$

and

$$
g''(\tau_0)
$$

are linearly independent.

Then (12.3)–(12.4) are two independent affine equations in

$$
y\in\mathbb R^3.
$$

Their solution set is an affine line:

$$
\boxed{
\mathcal K_{\tau_0}
=
\left\{
y:
g'\cdot y=-h',
\quad
g''\cdot y=-h''
\right\}.
}
\tag{13.1}
$$

Every point of this line lies at finite Euclidean position.

On this line,

$$
D=0.
$$

Since

$$
g'\neq0,
$$

the numerator of (5.3) is nonzero.

Thus the same rank-one envelope chart cannot remain regular through $\mathcal K_{\tau_0}$.

---

# 14. Bending is unavoidable somewhere

By Theorem D52.3 the tangent direction cannot remain constant on a non-affine parameter interval.

Hence there exists at least one parameter value where the tangent direction changes.

At such a regular value,

$$
\boxed{
g',g''
\text{ are linearly independent}.
}
$$

Therefore the finite caustic line of Section 13 is unavoidable in the geometric continuation of the same envelope family.

---

# Theorem D52.4 — Finite Caustic / Transition Theorem

Every genuinely non-affine local central perfect-response null-Hessian envelope possesses a finite geometric caustic/transition locus in the continuation of its plane family.

Therefore it cannot extend as one globally regular single-valued non-affine rank-one envelope chart over all of $\mathbb R^3$.

A global continuation must, before or at the finite caustic locus, undergo at least one of:

$$
\boxed{
\text{rank drop}
}
$$

$$
\boxed{
\text{envelope branch change}
}
$$

$$
\boxed{
\text{loss of perfect pressure response}
}
$$

$$
\boxed{
\text{loss of central flat scalar structure}
}
$$

$$
\boxed{
\text{loss of the rank-two planar representation}.
}
$$

This is a finite-transition result, not a singularity theorem.

DCRP52 does **not** claim that the full Euler/NS solution itself becomes singular at the envelope caustic.

It claims that the maximally rigid central perfect-response chart cannot remain the same smooth structural chart globally.

---

# 15. Global single-chart consequence

Suppose a hypothetical same-parent DSS Euler profile remained for all

$$
y\in\mathbb R^3
$$

inside one connected non-affine central perfect-pressure-response rank-one chart.

Theorem D52.4 rules this out.

Therefore:

## Corollary D52.5 — No Global Nonlinear Single-Chart Central Perfect Response

A nonzero global central perfect-response DSS profile cannot be represented everywhere by one non-affine null-Hessian envelope chart.

It must contain a finite normalized transition/rank-change set.

This gives DCRP a finite structural carrier even on the maximally rigid perfect-response branch.

---

# 16. Local nonlinear existence and the correct NO-GO boundary

Theorem D52.4 should not be misread as local nonexistence.

The explicit ODE

$$
(\theta')^2
=
\frac23-\tanh^2\eta
$$

has smooth nonconstant solutions on every sufficiently small interval around $\eta=0$.

Choose such a gradient curve $g$ and any smooth support function $h$.

At any point satisfying

$$
g'\cdot y+h'=0
$$

and

$$
g''\cdot y+h''\neq0,
$$

the implicit-function theorem produces a local nonlinear solution.

Thus:

$$
\boxed{
\text{local nonlinear perfect-response spatial realizability exists}.
}
$$

What fails is global single-chart continuation.

This is the correct strength boundary.

---

# 17. Vorticity reconstruction

Recall

$$
q=u+4az.
$$

The horizontal gradient is unchanged:

$$
\nabla_hq=\nabla_hu.
$$

Therefore the planar vorticity is

$$
\boxed{
\Omega
=
\left(
\partial_2u,
-\partial_1u,
0
\right).
}
\tag{17.1}
$$

Its divergence is identically zero:

$$
\boxed{
\nabla\cdot\Omega
=
\partial_1\partial_2u
-
\partial_2\partial_1u
=
0.
}
\tag{17.2}
$$

Because $C>0$,

$$
\boxed{
|\Omega|^2
=
|\nabla_hu|^2
\ge
C>0.
}
\tag{17.3}
$$

Thus the positive-$C$ perfect-response null-envelope patch is automatically a regular nonzero vorticity patch.

---

# 18. X72 vorticity-stress cone

Define

$$
\boxed{
W_\Omega
=
\Omega\otimes\Omega
-
\frac13|\Omega|^2I.
}
\tag{18.1}
$$

Its eigenvalues are

$$
\boxed{
\frac23|\Omega|^2,
\qquad
-\frac13|\Omega|^2,
\qquad
-\frac13|\Omega|^2.
}
\tag{18.2}
$$

Therefore

$$
\boxed{
|W_\Omega|^2
=
\frac23|\Omega|^4,
}
\tag{18.3}
$$

and

$$
\boxed{
\det W_\Omega
=
\frac2{27}|\Omega|^6.
}
\tag{18.4}
$$

Hence

$$
\boxed{
54
(\det W_\Omega)^2
=
|W_\Omega|^6.
}
\tag{18.5}
$$

These are exactly the X72 Round43 pointwise algebraic vorticity-stress realizability identities.

---

# Theorem D52.6 — DCRP Central Survivor Passes the X72 Pointwise Vorticity Cone

Every positive-$C$ central null-envelope branch produces a genuine divergence-free vorticity generator $\Omega$ and therefore an actual pointwise stress

$$
W_\Omega\in\mathcal M_\omega.
$$

It automatically passes:

1. the axisymmetric rank-one-generated stress cone;
2. the sharp determinant/norm realizability identity;
3. the divergence-free generator constraint;
4. the visible/invisible pointwise coupling requirement, because both are projections of the same actual $W_\Omega$.

Therefore the X72 Round43 STOP-C47 cannot eliminate this DCRP survivor merely by the pointwise algebraic vorticity-realizability test.

---

# 19. X72 lift status

The DCRP52 survivor currently lifts through the following levels.

## R0 — wave-compatible Hessian

Passed:

$$
D^2u=\kappa\ell\otimes\ell,
\qquad
\ell^\top G\ell=0.
$$

## R1 — pseudo-eikonal identity

Passed:

$$
\nabla u^\top M\nabla u=C.
$$

## R2 — nonzero planar vorticity reconstruction

Passed:

$$
\Omega=J\nabla_hu.
$$

## R3 — divergence-free generator

Passed identically:

$$
\nabla\cdot\Omega=0.
$$

## R4 — pointwise X72 stress cone

Passed:

$$
W_\Omega
=
\Omega\otimes\Omega
-\frac13|\Omega|^2I.
$$

## R5 — local central perfect pressure response

Passed by assumption of the maximally rigid DCRP branch:

$$
E_p=0.
$$

## R6 — global smooth single-chart continuation

Failed for every genuinely non-affine envelope:

$$
\boxed{
\text{finite caustic/transition unavoidable}.
}
$$

## R7 — same-parent DSS / finite PFET / global Euler realization across the transition

Open.

This locates the first proven non-liftable level much later than the generic X72 wave-cone stage.

---

# 20. Stress-amplitude corridor

From Corollary D52.2,

$$
C
\le
|\Omega|^2
\le
3C.
$$

Thus

$$
\frac23C^2
\le
|W_\Omega|^2
\le
6C^2.
$$

Because

$$
C=12M_a,
$$

$$
\boxed{
96M_a^2
\le
|W_\Omega|^2
\le
864M_a^2.
}
\tag{20.1}
$$

So the pointwise vorticity-stress magnitude on the nonlinear perfect-response envelope is quantitatively tied to the temporal logistic margin.

This removes arbitrary amplitude freedom from the local X72 stress witness.

---

# 21. Characteristic direction relative to vorticity

At a non-affine point let

$$
\widehat p
=
\frac{\nabla_hu}{|\nabla_hu|},
$$

and

$$
\widehat\Omega
=
J\widehat p.
$$

DCRP51 gives

$$
\boxed{
\ell_\sigma
=
t\widehat p
+
\sigma\sqrt{1-t^2}\widehat\Omega
+
n,
}
\tag{21.1}
$$

where

$$
|t|\le1.
$$

Hence

$$
\boxed{
\ell_\sigma\cdot\Omega
=
\sigma
|\Omega|
\sqrt{1-t^2}.
}
\tag{21.2}
$$

Thus the wave-null Hessian direction is generally neither parallel nor orthogonal to the vorticity direction.

The endpoint

$$
|t|=1
$$

is the only local null-Hessian orientation in which

$$
\ell\cdot\Omega=0.
$$

This gives a concrete geometric variable for the next X72 differential-realizability audit.

---

# 22. Pointwise stress evaluated on the null-Hessian direction

Because the Euclidean norm of a $G$-null vector normalized by $\ell_z=1$ is

$$
|\ell|^2=2,
$$

we obtain

$$
\begin{aligned}
\ell^\top W_\Omega\ell
&=
(\ell\cdot\Omega)^2
-
\frac13|\Omega|^2|\ell|^2
\\
&=
|\Omega|^2
\left[
1-t^2-\frac23
\right].
\end{aligned}
$$

Therefore

$$
\boxed{
\ell^\top W_\Omega\ell
=
|\Omega|^2
\left(
\frac13-t^2
\right).
}
\tag{22.1}
$$

This vanishes exactly at

$$
\boxed{
t^2=\frac13.
}
\tag{22.2}
$$

DCRP52 does **not** identify this pointwise identity with the full X72 $\operatorname{divdiv}$ condition.

However it isolates the unique local orientation at which the actual vorticity stress is longitudinally invisible along the same null-Hessian characteristic direction.

This is a concrete candidate coordinate for the next differential lift.

---

# 23. Why the X72 handoff is now sharper

X72 Round43 showed that arbitrary

$$
\operatorname{divdiv}\text{-free}
$$

stress waves are too flexible.

The missing ingredient was actual nonlinear vorticity realizability.

DCRP52 supplies an actual vorticity-generated stress, but with additional structure:

$$
\boxed{
W_\Omega
\in
\mathcal M_\omega,
}
$$

$$
\boxed{
\nabla\cdot\Omega=0,
}
$$

$$
\boxed{
D^2u
=
\kappa\ell\otimes\ell,
}
$$

$$
\boxed{
\ell^\top M\nabla u=0,
}
$$

$$
\boxed{
C
\le
|\Omega|^2
\le
3C.
}
$$

Therefore the next X72 question is no longer:

> can an arbitrary stress-wave amplitude be realized by vorticity?

It is:

> can this **developable null-envelope vorticity stress** satisfy the required differential/projection transfer structure across its finite caustic transition and still return as the same-parent DSS profile?

That is a much smaller realizability class.

---

# 24. NTLA-O interpretation

The DCRP51 observer saw a pointwise null-Hessian cone.

DCRP52 adds the integrability observer and discovers that pointwise admissibility is not enough.

The pointwise state lifts to a local envelope only if its null directions assemble into a gradient-space curve.

That local envelope then carries a finite caustic frontier because the null tangent direction cannot remain parallel.

Thus the realizability tower is:

$$
\boxed{
\text{pointwise null cone}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{integrable null gradient curve}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{local developable envelope}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{finite caustic/transition}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{global same-parent lift?}
}
$$

This is precisely the NTLA-O distinction between local structural admissibility and global realizability.

---

# 25. Updated final survivor

After DCRP52, the maximally rigid active rank-two branch cannot remain globally in the same perfect-response central chart.

The remaining alternatives are:

$$
\boxed{
\begin{aligned}
&
\text{finite rank/flatness/pressure-response transition}
\\
&\vee
\\
&
\text{branch change across a developable caustic}
\\
&\vee
\\
&
\text{loss of central response}
\\
&\vee
\\
&
\text{same-parent global realization through a transition layer}.
\end{aligned}
}
$$

Inside every non-affine perfect-response chart, however, the vorticity stress is already fully pointwise X72-realizable.

Thus the unresolved obstruction is now genuinely **global/differential**, not algebraic.

---

# 26. Status ledger

## PROVED this round

### D52-P1 — Local envelope normal form

$$
u=g(\tau)\cdot y+h(\tau),
$$

$$
g'\cdot y+h'=0.
$$

### D52-P2 — Exact Hessian formula

$$
D^2u
=
-
\frac{
g'\otimes g'
}{
g''\cdot y+h''
}.
$$

### D52-P3 — Complete gradient-space constraints

$$
g^\top Mg=C,
$$

$$
g'^\top Gg'=0.
$$

### D52-P4 — Explicit null-gradient ODE

$$
(\theta')^2
=
\frac23-\tanh^2\eta.
$$

### D52-P5 — Local nonlinear spatial solutions exist

The positive-$C$ wave–pseudo-eikonal system is not locally affine-rigid.

### D52-P6 — Constant null direction impossible

A genuinely nonlinear pseudo-eikonal null curve must bend in gradient space.

### D52-P7 — Finite caustic/transition

Every bending null-envelope family develops a finite envelope degeneracy locus in its geometric continuation.

### D52-P8 — No global nonlinear single-chart continuation

A global survivor must undergo rank/branch/flatness/pressure-response transition.

### D52-P9 — Divergence-free vorticity reconstruction

$$
\nabla\cdot\Omega=0.
$$

### D52-P10 — X72 pointwise stress realizability passed

$$
54(\det W_\Omega)^2=|W_\Omega|^6.
$$

### D52-P11 — Vorticity/stress amplitude corridor

$$
12M_a
\le
|\Omega|^2
\le
36M_a.
$$

---

# 27. Closed / corrected routes

## Closed

General positive-$C$ local affine rigidity is false.

## Closed

X72 pointwise vorticity-stress algebraic realizability cannot eliminate the DCRP central survivor; the survivor is generated by actual divergence-free vorticity.

## New non-liftable level

A genuinely nonlinear perfect-response envelope cannot remain one smooth global rank-one chart.

## Still open

Whether the full Euler/DSS solution can cross the finite transition set while preserving all same-parent/PFET constraints.

---

# 28. New STOP

$$
\boxed{
\textbf{
STOP-D52:
The central perfect-response null cone is locally integrable and pointwise X72-vorticity-realizable, but every genuinely nonlinear realization is a bending developable envelope with an unavoidable finite caustic/transition frontier. The remaining obstruction is global same-parent continuation across that frontier.
}
}
$$

---

# 29. Next autonomous step

## DCRP53 — Caustic Transition and Differential X72 Realizability

**Working title**

> **Developable Null-Envelope Transition, Vorticity-Stress Differential Constraint, and Same-Parent Crossing**

Primary tasks:

1. analyze the envelope caustic locus
   $$
   g'\cdot y+h'=0,
   \qquad
   g''\cdot y+h''=0;
   $$
2. determine what rank/strain/vorticity quantities blow, vanish, or switch branch as the denominator approaches zero;
3. test whether a smooth full Euler profile can cross by forcing
   $$
   \kappa\to0
   $$
   or a pressure-response defect;
4. compute the actual
   $$
   \operatorname{divdiv}W_\Omega
   $$
   and its projected X72 visible/invisible pieces on the null-envelope family;
5. determine whether the special local orientation
   $$
   t^2=\frac13
   $$
   is the only possible differential stress-wave lift;
6. couple any required transition carrier to DCRP31 PFET / DCRP46 scalar transport.

Desired endpoint:

$$
\boxed{
\text{transition defect}
\ \vee\
\text{smooth rank-drop crossing}
\ \vee\
\text{X72 differential non-liftability}
\ \vee\
\text{explicit crossing model}.
}
$$

---

# 30. One-line checkpoint

The null-Hessian cone survives local integrability and even passes X72's pointwise vorticity-stress cone, but every non-affine realization is a bending developable envelope with an unavoidable finite caustic/transition, so the proof frontier has moved from algebraic realizability to global differential/same-parent continuation across that finite carrier.

---

**End checkpoint:** DCRP52  
**Next:** DCRP53 — Caustic Transition / X72 Differential Realizability.
