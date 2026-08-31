# DCRP62 / X72-R45 — Aligned-Neutral Pressure Compatibility and the Collapse of the N Branch

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / aligned-neutral pressure-compatibility round  
**Immediate predecessor:** `NS_DCRP61_X72R44_StressProjection_AlignedNeutralFloquet_2026-08-18.md`

**Primary internal dependencies**
- DCRP-35 — positive vortex-stretching / inward-turnover dichotomy
- DCRP-38 — covariance ledger and same-parent residual split
- DCRP-59/60 — signed non-affine-work branch and rank-two closure handoff
- DCRP-61 — actual vorticity-stress projection dynamics and Aligned-Neutral Floquet Mode
- X72 Round36–37 — cofactor–pressure lock and affine pressure-response defect
- X72 Round42–43 — actual vorticity-stress visibility / realizability

**External calibration**
- Galanti, Gibbon, Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.
- Gibbon, Holm, Kerr, Roulstone, *Quaternions and particle dynamics in the Euler fluid equations*, arXiv:nlin/0512034.
- Chevillard, Meneveau, Biferale, Toschi, *Modeling the pressure Hessian and viscous Laplacian in Turbulence*, arXiv:0712.0900.

These references confirm that vorticity/strain alignment dynamics are naturally controlled by the pressure Hessian. The similarity-Euler identities and all quantitative conclusions below are derived directly here.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP61 discovered the only equality direction invisible to the first stress-projection attack:

$$
\boxed{
S\Omega=\lambda\Omega,
}
$$

with positive recurrent stretching and the exact neutral Floquet mean

$$
\boxed{
\bar\lambda
=
\frac{2-3\gamma}{2}.
}
$$

If $\lambda$ is spatially uniform and the X72 transport/projection commutator is silent, positive stretching can preserve the visible/invisible stress identity.

DCRP62 asks whether that exceptional mode can also remain **pressure-perfect**.

It cannot.

Let

$$
Y=\gamma y+V,
$$

$$
D_s=\partial_s+Y\cdot\nabla,
$$

and let the similarity Euler profile satisfy

$$
\boxed{
D_s\Omega+\Omega=S\Omega.
}
$$

The velocity-gradient equation is

$$
\boxed{
D_s(\nabla V)
+
\nabla V
+
(\nabla V)^2
+
\nabla^2P
=
0.
}
$$

Writing

$$
\nabla V=S+R,
$$

with

$$
R x=\frac12\Omega\times x,
$$

the strain equation is

$$
\boxed{
D_sS
+
S
+
S^2
+
R^2
+
H_P
=
0,
}
$$

where

$$
H_P=\nabla^2P.
$$

Now impose the aligned mode

$$
\boxed{
S\Omega=\lambda\Omega.
}
$$

The alignment is assumed to persist materially.

Differentiating the eigenvector relation gives

$$
\boxed{
(D_sS)\Omega
=
(D_s\lambda)\Omega.
}
$$

Since

$$
R^2\Omega=0,
$$

the strain equation yields the exact pressure-Hessian compatibility:

$$
\boxed{
H_P\Omega
=
-
\left(
D_s\lambda+\lambda+\lambda^2
\right)\Omega.
}
$$

Thus a materially preserved strain eigenvector is necessarily also a pressure-Hessian eigenvector.

This is the similarity-Euler analogue of the classical vorticity-alignment pressure-Hessian relation.

Now introduce the exact X72 Round36–37 affine pressure-response defect

$$
\boxed{
E_p
=
H_P^0+C_S^0,
}
$$

with

$$
\boxed{
H_P^0
=
H_P-\frac{\Delta P}{3}I,
}
$$

and

$$
\boxed{
C_S^0
=
S^2-\frac13|S|^2I.
}
$$

The similarity pressure Poisson identity is

$$
\boxed{
\Delta P
=
-|S|^2+\frac12|\Omega|^2.
}
$$

Combining all of these identities gives the central theorem:

$$
\boxed{
E_p\Omega
=
-
\left(
D_s\lambda
+
\lambda
+
\frac16|\Omega|^2
\right)\Omega.
}
$$

Equivalently, if

$$
\xi=\frac{\Omega}{|\Omega|},
$$

then

$$
\boxed{
\xi^\top E_p\xi
=
-
\left(
D_s\lambda
+
\lambda
+
\frac16|\Omega|^2
\right).
}
$$

The $\lambda^2$ term cancels **exactly** between the pressure-Hessian eigenvalue and the cofactor response.

This cancellation is crucial.

The remaining defect has a sign obstruction over one same-parent period.

Take a nonzero material trajectory that remains inside the aligned-neutral equality class for one full DSS period.

If the stretching scalar returns,

$$
\boxed{
\lambda(s_0+S_0)=\lambda(s_0),
}
$$

then

$$
\begin{aligned}
\int_{s_0}^{s_0+S_0}
\xi^\top E_p\xi\,ds
&=
-
\int_{s_0}^{s_0+S_0}\lambda\,ds
\\
&\quad
-\frac16
\int_{s_0}^{s_0+S_0}
|\Omega|^2\,ds.
\end{aligned}
$$

For the aligned-neutral Floquet mode,

$$
\boxed{
\int_{s_0}^{s_0+S_0}\lambda\,ds
=
\frac{2-3\gamma}{2}S_0.
}
$$

Therefore

$$
\boxed{
\int_{s_0}^{s_0+S_0}
\xi^\top E_p\xi\,ds
=
-
\frac{2-3\gamma}{2}S_0
-
\frac16
\int_{s_0}^{s_0+S_0}
|\Omega|^2ds
<0.
}
$$

Consequently:

$$
\boxed{
\int_{s_0}^{s_0+S_0}
|E_p|_F\,ds
\ge
\frac{2-3\gamma}{2}S_0
+
\frac16
\int_{s_0}^{s_0+S_0}
|\Omega|^2ds.
}
$$

In particular,

$$
\boxed{
\int_{s_0}^{s_0+S_0}
|E_p|_F\,ds
>
\frac{2-3\gamma}{2}S_0.
}
$$

Thus:

> **The Aligned-Neutral Floquet Mode can be X72 visibility-silent, but it cannot be X72 pressure-response-perfect.**

This closes the exceptional equality mode found in DCRP61.

There is an exact material alternative:

- if a positive-measure family of particles remains aligned-neutral for a full period, it pays a strictly positive pressure-response-defect action;
- if no such material family survives one full period, the aligned state is replenished by material replacement/turnover.

Hence:

$$
\boxed{
\mathsf A_{\rm neutral}
\Longrightarrow
\mathsf X_p
\vee
\mathsf T.
}
$$

Combining this with DCRP61's generic decomposition of the N branch gives the desired confluence:

$$
\boxed{
\mathsf N
\Longrightarrow
\mathsf X
\vee
\mathsf T.
}
$$

Therefore the DCRP60 rank-two handoff finally collapses from

$$
\boxed{
\mathsf X
\vee
\mathsf N
\vee
\mathsf T
}
$$

to the genuine two-branch frontier

$$
\boxed{
\mathsf X
\vee
\mathsf T.
}
$$

Here:

- $\mathsf X$ contains X72 visibility/modulation/tilt/transport-commutator **or pressure-response defect**;
- $\mathsf T$ is material covariance/enstrophy turnover.

The non-affine stretching branch is no longer an independent terminal escape.

This is the main DCRP62 closure.

---

# 1. Similarity Euler velocity-gradient equation

Use the similarity Euler equation in the normalization underlying DCRP:

$$
\boxed{
\partial_sV
+
(\gamma y+V)\cdot\nabla V
+
(1-\gamma)V
+
\nabla P
=
0.
}
\tag{1.1}
$$

Set

$$
\boxed{
Y=\gamma y+V.
}
\tag{1.2}
$$

Then

$$
\boxed{
D_s
=
\partial_s+Y\cdot\nabla.
}
\tag{1.3}
$$

Differentiate (1.1).

Because

$$
\nabla(\gamma y)=\gamma I,
$$

the $\gamma\nabla V$ contribution from differentiating the transport term combines with $(1-\gamma)\nabla V$.

Hence:

## Theorem D62.1 — Similarity Velocity-Gradient Equation

$$
\boxed{
D_sL
+
L
+
L^2
+
H_P
=
0,
}
\tag{1.4}
$$

where

$$
\boxed{
L=\nabla V.
}
$$

---

# 2. Strain/rotation decomposition

Write

$$
\boxed{
L=S+R,
}
\tag{2.1}
$$

where

$$
S=S^\top,
$$

$$
R^\top=-R.
$$

For incompressible three-dimensional flow,

$$
\boxed{
Rx
=
\frac12\Omega\times x.
}
\tag{2.2}
$$

Therefore

$$
\boxed{
R^2
=
\frac14
\left(
\Omega\otimes\Omega
-
|\Omega|^2I
\right).
}
\tag{2.3}
$$

In particular,

$$
\boxed{
R^2\Omega=0.
}
\tag{2.4}
$$

The symmetric part of (1.4) is:

## Theorem D62.2 — Similarity Strain Equation

$$
\boxed{
D_sS
+
S
+
S^2
+
R^2
+
H_P
=
0.
}
\tag{2.5}
$$

---

# 3. Pressure Poisson identity

Take the trace of (1.4).

Since

$$
\operatorname{tr}L=0,
$$

and

$$
\operatorname{tr}L^2
=
|S|^2-\frac12|\Omega|^2,
$$

we get:

$$
\boxed{
\Delta P
=
-|S|^2
+
\frac12|\Omega|^2.
}
\tag{3.1}
$$

Equivalently,

$$
\boxed{
-\Delta P
=
|S|^2
-
\frac12|\Omega|^2.
}
\tag{3.2}
$$

This is the same algebraic pressure source used by X72 Round37.

---

# 4. Persistently aligned vorticity

Assume on an active material region

$$
\boxed{
S\Omega=\lambda\Omega.
}
\tag{4.1}
$$

No spatial uniformity of $\lambda$ is required for the next identity.

The vorticity equation is

$$
\boxed{
D_s\Omega+\Omega=S\Omega.
}
\tag{4.2}
$$

Hence under alignment,

$$
\boxed{
D_s\Omega
=
(\lambda-1)\Omega.
}
\tag{4.3}
$$

Therefore the vorticity direction is materially constant:

$$
\boxed{
D_s\xi=0,
}
\tag{4.4}
$$

where

$$
\xi=\Omega/|\Omega|.
$$

---

# 5. Differentiate the strain-eigenvector relation

Apply $D_s$ to

$$
S\Omega=\lambda\Omega.
$$

Then

$$
(D_sS)\Omega
+
S(D_s\Omega)
=
(D_s\lambda)\Omega
+
\lambda D_s\Omega.
$$

Using (4.3),

$$
S(D_s\Omega)
=
(\lambda-1)S\Omega
=
\lambda(\lambda-1)\Omega,
$$

while

$$
\lambda D_s\Omega
=
\lambda(\lambda-1)\Omega.
$$

The two terms cancel.

Therefore:

## Theorem D62.3 — Material Eigenvalue-Preservation Identity

$$
\boxed{
(D_sS)\Omega
=
(D_s\lambda)\Omega.
}
\tag{5.1}
$$

This is the exact condition for persistent strain/vorticity eigen-alignment.

---

# 6. Pressure Hessian must share the vorticity eigenvector

Apply the strain equation (2.5) to $\Omega$.

Using:

$$
(D_sS)\Omega
=
(D_s\lambda)\Omega,
$$

$$
S\Omega=\lambda\Omega,
$$

$$
S^2\Omega=\lambda^2\Omega,
$$

and

$$
R^2\Omega=0,
$$

we obtain:

$$
\boxed{
H_P\Omega
=
-
\left(
D_s\lambda
+
\lambda
+
\lambda^2
\right)\Omega.
}
\tag{6.1}
$$

Therefore:

## Theorem D62.4 — Aligned Pressure-Hessian Eigenvector Compatibility

On every materially persistent aligned vorticity trajectory,

$$
\boxed{
\Omega
}
$$

is simultaneously an eigenvector of:

$$
\boxed{
S
}
$$

and

$$
\boxed{
H_P.
}
$$

The pressure-Hessian eigenvalue is

$$
\boxed{
\mu_P
=
-
\left(
D_s\lambda
+
\lambda
+
\lambda^2
\right).
}
\tag{6.2}
$$

---

# 7. X72 affine pressure-response defect

X72 Round36–37 defines

$$
\boxed{
E_p
=
H_P^0+C_S^0,
}
\tag{7.1}
$$

where

$$
\boxed{
H_P^0
=
H_P-\frac{\Delta P}{3}I,
}
\tag{7.2}
$$

and

$$
\boxed{
C_S^0
=
S^2-\frac13|S|^2I.
}
\tag{7.3}
$$

The perfect affine pressure-response lock is

$$
\boxed{
E_p=0.
}
\tag{7.4}
$$

---

# 8. Action of the cofactor on aligned vorticity

Because

$$
S^2\Omega=\lambda^2\Omega,
$$

we have

$$
\boxed{
C_S^0\Omega
=
\left(
\lambda^2-\frac13|S|^2
\right)\Omega.
}
\tag{8.1}
$$

From the pressure Poisson identity,

$$
\boxed{
-\frac{\Delta P}{3}
=
\frac13|S|^2
-
\frac16|\Omega|^2.
}
\tag{8.2}
$$

Therefore

$$
\boxed{
H_P^0\Omega
=
\left[
-
D_s\lambda
-
\lambda
-
\lambda^2
+
\frac13|S|^2
-
\frac16|\Omega|^2
\right]\Omega.
}
\tag{8.3}
$$

Add (8.1).

The $\lambda^2$ and $|S|^2$ terms cancel exactly.

---

# Theorem D62.5 — Exact Aligned Pressure-Response Defect

$$
\boxed{
E_p\Omega
=
-
\left(
D_s\lambda
+
\lambda
+
\frac16|\Omega|^2
\right)\Omega.
}
\tag{8.4}
$$

Equivalently,

$$
\boxed{
\xi^\top E_p\xi
=
-
\left(
D_s\lambda
+
\lambda
+
\frac16|\Omega|^2
\right).
}
\tag{8.5}
$$

This is the central identity of DCRP62.

---

# 9. Immediate pressure-perfect consequence

Suppose

$$
E_p=0
$$

on a materially persistent aligned region.

Then (8.5) requires

$$
\boxed{
D_s\lambda
+
\lambda
+
\frac16|\Omega|^2
=
0.
}
\tag{9.1}
$$

Thus:

$$
\boxed{
|\Omega|^2
=
-6
\left(
D_s\lambda+\lambda
\right).
}
\tag{9.2}
$$

Since the left side is nonnegative,

$$
\boxed{
D_s\lambda+\lambda\le0.
}
\tag{9.3}
$$

A recurrent positive-mean aligned stretching rate is therefore immediately under tension with perfect pressure response.

---

# 10. One-period material pressure-defect identity

Let

$$
X(a,s)
$$

be a material trajectory of $Y$ that remains in the aligned equality class over

$$
s\in[s_0,s_0+S_0].
$$

Assume the stretching eigenvalue returns after one same-parent period:

$$
\boxed{
\lambda(X(a,s_0+S_0),s_0+S_0)
=
\lambda(X(a,s_0),s_0).
}
\tag{10.1}
$$

Integrate (8.5) along the trajectory.

Since

$$
\int D_s\lambda\,ds=0,
$$

we obtain:

## Theorem D62.6 — Same-Parent Pressure-Defect Action Identity

$$
\boxed{
\begin{aligned}
\int_{s_0}^{s_0+S_0}
\xi^\top E_p\xi\,ds
={}&
-
\int_{s_0}^{s_0+S_0}
\lambda\,ds
\\
&-
\frac16
\int_{s_0}^{s_0+S_0}
|\Omega|^2ds.
\end{aligned}
}
\tag{10.2}
$$

No Eulerian fixed-point return of the particle itself is required.

Only the same-parent scalar eigenvalue return is used.

---

# 11. Insert the Aligned-Neutral Floquet rate

DCRP61 gives the turnover-free neutral covariance condition

$$
\boxed{
\frac1{S_0}
\int_{s_0}^{s_0+S_0}
\lambda\,ds
=
\frac{2-3\gamma}{2}.
}
\tag{11.1}
$$

In the strict Type-II window,

$$
\boxed{
2-3\gamma>0.
}
\tag{11.2}
$$

Therefore Theorem D62.6 becomes:

## Theorem D62.7 — Aligned-Neutral Pressure Gap

$$
\boxed{
\begin{aligned}
\int_{s_0}^{s_0+S_0}
\xi^\top E_p\xi\,ds
={}&
-
\frac{2-3\gamma}{2}S_0
\\
&-
\frac16
\int_{s_0}^{s_0+S_0}
|\Omega|^2ds
\\
<&0.
\end{aligned}
}
\tag{11.3}
$$

Consequently,

$$
\boxed{
\int_{s_0}^{s_0+S_0}
|E_p|_Fds
\ge
\frac{2-3\gamma}{2}S_0
+
\frac16
\int_{s_0}^{s_0+S_0}
|\Omega|^2ds.
}
\tag{11.4}
$$

In particular,

$$
\boxed{
\int_{s_0}^{s_0+S_0}
|E_p|_Fds
>
\frac{2-3\gamma}{2}S_0.
}
\tag{11.5}
$$

This is a quantitative pressure-response defect gap along every persistent aligned-neutral material trajectory.

---

# 12. Perfect pressure response is impossible

If

$$
E_p\equiv0
$$

along such a trajectory, the left side of (11.3) is zero.

The right side is strictly negative.

Contradiction.

Therefore:

## Corollary D62.8 — Aligned-Neutral Perfect-Pressure NO-GO

A nonzero same-parent Aligned-Neutral Floquet trajectory cannot satisfy

$$
\boxed{
E_p=0
}
$$

through one complete DSS period.

This conclusion is independent of whether the X72 visible/invisible transport commutator is silent.

---

# 13. Pressure defect may exist while visibility remains silent

DCRP61 showed that under:

$$
\tau=0,
$$

spatially uniform $\lambda$, and

$$
[V\cdot\nabla,\mathbb P_L]W=0,
$$

an exact visibility relation may remain unchanged.

D62 shows that even in this maximally silent projection case,

$$
\boxed{
E_p
}
$$

must carry a strictly positive one-period action.

Thus the X72 observables separate:

$$
\boxed{
\text{visibility silence}
}
$$

does not imply

$$
\boxed{
\text{pressure-response lock}.
}
$$

The exceptional mode can hide from one X72 observer but not from the pressure/cofactor observer.

This is a useful observer-resolution distinction.

---

# 14. Positive-measure material tube

Let

$$
A_0
$$

be a positive-measure material set at time $s_0$ such that every trajectory issued from $A_0$ remains aligned-neutral for one period.

The flow of

$$
Y=\gamma y+V
$$

has Jacobian

$$
\boxed{
J(s)
=
e^{3\gamma(s-s_0)},
}
\tag{14.1}
$$

because

$$
\nabla\cdot Y=3\gamma.
$$

Let

$$
A(s)=X(A_0,s).
$$

Integrate (11.5) over $A_0$.

Using

$$
da
=
e^{-3\gamma(s-s_0)}dy
$$

at time $s$, we get:

## Theorem D62.9 — Material-Tube Pressure-Defect Gap

$$
\boxed{
\begin{aligned}
&
\int_{s_0}^{s_0+S_0}
e^{-3\gamma(s-s_0)}
\int_{A(s)}
|E_p(y,s)|_F\,dy\,ds
\\
&\qquad\ge
|A_0|
\frac{2-3\gamma}{2}
S_0.
\end{aligned}
}
\tag{14.2}
$$

A stronger version retains the positive vorticity term from (11.4).

Therefore no positive-measure aligned-neutral material tube can remain pressure-perfect.

---

# 15. If no material tube survives, turnover has already occurred

The aligned-neutral mode was introduced as a candidate same-parent recurrent equality mechanism.

If no positive-measure collection of material particles remains inside that equality class over one period, then the recurrence is necessarily Eulerian rather than material:

$$
\boxed{
\text{the state is replenished by different material particles}.
}
$$

This is precisely a material replacement / turnover mechanism.

Therefore:

## Theorem D62.10 — Aligned-Neutral X/T Dichotomy

For a recurrent aligned-neutral equality region,

$$
\boxed{
\mathsf A_{\rm neutral}
\Longrightarrow
\mathsf X_p
\vee
\mathsf T.
}
\tag{15.1}
$$

Here:

- $\mathsf X_p$ is the positive pressure-response defect gap of D62.7–9;
- $\mathsf T$ is loss of same-parent material persistence / turnover.

The exceptional D61 equality state has no third continuation.

---

# 16. Return to the generic N branch

DCRP61 decomposed positive stretching into:

$$
\boxed{
\text{stretching-rate modulation}
}
$$

$$
\vee
$$

$$
\boxed{
\text{vorticity-direction tilt}
}
$$

$$
\vee
$$

$$
\boxed{
\text{transport–projection commutator}
}
$$

$$
\vee
$$

$$
\boxed{
\text{Aligned-Neutral Floquet Mode}.
}
$$

The first three are already X72/transport defects.

D62 proves the fourth gives

$$
\mathsf X_p\vee\mathsf T.
$$

Therefore:

## Theorem D62.11 — Non-Affine Stretching Absorption

The DCRP59 positive non-affine stretching branch satisfies

$$
\boxed{
\mathsf N
\Longrightarrow
\mathsf X
\vee
\mathsf T.
}
\tag{16.1}
$$

This is the confluence sought in DCRP60.

---

# 17. Rank-two handoff collapses to two branches

DCRP60 had

$$
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X
\vee
\mathsf N
\vee
\mathsf T.
}
$$

Using Theorem D62.11:

## Theorem D62.12 — Two-Branch Rank-Two Global Frontier

$$
\boxed{
\text{rank-two continuation}
\Longrightarrow
\mathsf X
\vee
\mathsf T.
}
\tag{17.1}
$$

The non-affine stretching branch is no longer independent.

The rank-two closure program has now genuinely reduced the global frontier to:

### X

nonlocal pressure / X72 visibility / modulation / tilt / transport-projection defect;

### T

same-parent material turnover / inward enstrophy replacement.

No third branch remains at this resolution.

---

# 18. Why the pressure gap has the correct sign

The aligned-neutral mean satisfies

$$
\bar\lambda>0.
$$

At the same time,

$$
|\Omega|^2/6>0.
$$

The pressure/cofactor defect eigenvalue is

$$
-\left(
D_s\lambda+\lambda+|\Omega|^2/6
\right).
$$

The derivative term telescopes on a same-parent period.

The two remaining terms have the same sign.

That is why no cancellation can save pressure-perfect response.

This is stronger than a generic pressure-Hessian alignment statement.

It is a signed one-period obstruction.

---

# 19. Relation to Galanti–Gibbon–Heritage alignment variables

Classical Euler vorticity-alignment analysis introduces the stretching rate along vorticity and the perpendicular alignment vector, with pressure-Hessian variables controlling their Lagrangian evolution.

D61/D62 recover the same structural hierarchy in the present similarity normalization:

$$
\boxed{
\lambda
}
$$

is the parallel stretching coordinate,

$$
\boxed{
\tau
}
$$

is the tilt coordinate,

and

$$
\boxed{
H_P\Omega
}
$$

controls persistence of exact alignment.

The additional similarity term contributes the extra linear $\lambda$ in

$$
H_P\Omega
=
-(D_s\lambda+\lambda+\lambda^2)\Omega.
$$

The X72 cofactor correction then cancels $\lambda^2$ exactly, leaving the signed defect

$$
D_s\lambda+\lambda+|\Omega|^2/6.
$$

---

# 20. Relationship to X72 Round37

X72 Round37 showed that generic pressure-response defect dynamics remain critical because:

- pure $-S^2$ self-amplification cancels from the defect forcing;
- explicit determinant pressure forcing also cancels;
- higher gradients and transport–Riesz commutators remain.

D62 discovers a complementary exact cancellation on the aligned-neutral state:

$$
\boxed{
\lambda^2
}
$$

also cancels from the **vorticity-direction component** of $E_p$.

But instead of making the defect disappear, the cancellation exposes the strictly signed remainder

$$
\boxed{
D_s\lambda+\lambda+|\Omega|^2/6.
}
$$

Thus the aligned-neutral branch is easier than the generic Round37 defect problem.

It admits a one-period signed lower bound without closing the full critical defect PDE.

---

# 21. Silent projection commutator no longer rescues the mode

D61 left open the possibility:

$$
[V\cdot\nabla,\mathbb P_L]W=0.
$$

D62 shows that even under exact silence of this commutator,

$$
E_p
$$

must be nonzero over the period.

Hence the next global proof does **not** need to solve the silent-commutator classification merely to eliminate the aligned-neutral pressure-perfect branch.

That branch is already routed to X.

This removes one apparently difficult equality subproblem.

---

# 22. Updated global architecture

The long chain is now:

$$
\boxed{
\text{rank-two local equality}
}
$$

$$
\Downarrow
$$

D54 visibility leakage

$$
\Downarrow
$$

D55 finite compensation or tail

$$
\Downarrow
$$

D58 tail impossible

$$
\Downarrow
$$

D59 non-affine work or turnover

$$
\Downarrow
$$

D61 generic projection defect or aligned-neutral exception

$$
\Downarrow
$$

D62 aligned-neutral pressure defect or turnover

$$
\Downarrow
$$

$$
\boxed{
\mathsf X
\vee
\mathsf T.
}
$$

This is the new final rank-two confluence.

---

# 23. What remains genuinely open

The rank-two geometry itself no longer needs additional refinement.

The remaining global branches are:

## X branch

Pressure/visibility/transport defect is nonzero.

The missing theorem is to show that the required recurrent X defect cannot be maintained under the finite-energy same-parent NS ancestry, or that it forces one of the already costly transfer channels.

## T branch

The same-parent equality state is materially replaced each period.

The missing theorem is to couple:

- inward enstrophy turnover;
- DCRP31 PFET;
- finite annular supplier;
- same-parent critical scaling.

This is now the only material escape.

---

# 24. Status ledger

## PROVED this round

### D62-P1 — similarity velocity-gradient equation

$$
D_sL+L+L^2+H_P=0.
$$

### D62-P2 — similarity strain equation

$$
D_sS+S+S^2+R^2+H_P=0.
$$

### D62-P3 — aligned pressure-Hessian eigenvector compatibility

$$
H_P\Omega
=
-(D_s\lambda+\lambda+\lambda^2)\Omega.
$$

### D62-P4 — exact X72 aligned pressure-defect identity

$$
E_p\Omega
=
-
(D_s\lambda+\lambda+|\Omega|^2/6)\Omega.
$$

### D62-P5 — one-period signed pressure-defect action

On neutral same-parent aligned trajectories,

$$
\int
\xi^\top E_p\xi
=
-\frac{2-3\gamma}{2}S_0
-\frac16\int|\Omega|^2.
$$

### D62-P6 — quantitative trajectory pressure gap

$$
\int|E_p|
>
\frac{2-3\gamma}{2}S_0.
$$

### D62-P7 — positive-measure material-tube pressure gap.

### D62-P8 — aligned-neutral perfect-pressure NO-GO.

### D62-P9 — aligned-neutral X/T dichotomy.

### D62-P10 — absorption of the N branch

$$
\mathsf N\Rightarrow\mathsf X\vee\mathsf T.
$$

### D62-P11 — final two-branch rank-two frontier

$$
\boxed{
\text{rank-two continuation}
\Rightarrow
\mathsf X\vee\mathsf T.
}
$$

---

# 25. Closed / corrected routes

## Closed

The D61 Aligned-Neutral Floquet Mode as a simultaneously:

- turnover-free;
- pressure-perfect;
- same-parent recurrent

equality state.

## No longer necessary for this closure

A full classification of silent

$$
[V\cdot\nabla,\mathbb P_L]W=0.
$$

Even if it is silent, the aligned-neutral mode pays pressure defect.

## Closed as independent terminal branch

Positive non-affine stretching $\mathsf N$.

It is absorbed into $\mathsf X\vee\mathsf T$.

---

# 26. New STOP

$$
\boxed{
\textbf{
STOP-D62:
The only visibility-silent stretching equality mode found in D61 cannot also be pressure-response-perfect. Persistent vorticity/strain eigen-alignment forces }
E_p\Omega=-(D_s\lambda+\lambda+|\Omega|^2/6)\Omega,
\textbf{ and the neutral Floquet mean makes its one-period pressure-defect action strictly positive. Hence the non-affine stretching branch collapses into X72 pressure/projection defect or material turnover, leaving only the two global branches }
\mathsf X\vee\mathsf T.
}
$$

---

# 27. Next autonomous step

## DCRP63 — Final X/T Frontier: Pressure-Projection Defect versus Same-Parent Turnover

**Working title**

> **Pressure-Defect Replenishment, Inward Enstrophy/PFET Coupling, and the Two-Branch Global Closure Problem**

Primary tasks:

1. formalize the two remaining global branches:
   $$
   \mathsf X,\qquad\mathsf T;
   $$
2. on X:
   combine the D62 signed pressure-defect action with X72 Round37 defect-energy / Round38 transport–Riesz estimates;
3. determine whether recurrent pressure defect itself requires a finite higher-gradient or commutator budget that scales incompatibly under same-parent ancestry;
4. on T:
   combine the D59 inward enstrophy turnover gap with DCRP31 inward PFET;
5. search for a joint finite annulus inequality coupling enstrophy turnover and energy/pressure flux;
6. decide which of X or T has the sharper immediate obstruction and attack only that branch next.

Desired endpoint:

$$
\boxed{
\mathsf X\text{ closed}
\quad\vee\quad
\mathsf T\text{ closed}
\quad\vee\quad
\text{one uniquely surviving global branch}.
}
$$

---

# 28. One-line checkpoint

The D61 hidden aligned-neutral mode is now closed as a pressure-perfect equality state: its exact pressure/cofactor defect has a strictly negative one-period vorticity-direction integral, so every rank-two continuation has finally collapsed to only two global exits—X72 pressure/projection defect or same-parent material turnover.

---

**End checkpoint:** DCRP62 / X72-R45  
**Next:** DCRP63 — Final X/T Frontier.
