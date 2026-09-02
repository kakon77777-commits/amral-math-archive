# DCRP68 / X72-R51 — Axisymmetric Director Integrability Collapse and Mandatory Cofactor-Shape Activity

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / axisymmetric self-lock integrability round  
**Immediate predecessor:** `NS_DCRP67_X72R50_AlignedTwoStress_SelfLockGeometry_2026-08-18.md`

**Primary internal dependencies**
- DCRP-38 — finite-compensation isotropic vorticity covariance
- DCRP-61–67 — aligned/no-turnover X branch and two-stress spectral reduction
- X72 Round36 — cofactor self-angular rate / axisymmetric self-lock classification
- X72 Round38–41 — cofactor transport–Riesz correlation and Piola–vorticity reduction

**External calibration**
- B. Galanti, J. D. Gibbon, M. Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.
- D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782.

The external papers calibrate the geometric importance of vorticity/strain alignment and pancake-type Euler structures. The integrability calculations below are direct.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP67 showed that the only aligned strain spectra with zero **self-induced cofactor angular rate** are:

### Type A

$$
\boxed{
\operatorname{spec}S
=
\left(
\lambda,-\frac{\lambda}{2},-\frac{\lambda}{2}
\right),
\qquad
\Omega\parallel \text{simple }\lambda\text{-axis},
}
$$

and

### Type B

$$
\boxed{
\operatorname{spec}S
=
(\lambda,\lambda,-2\lambda),
\qquad
\Omega
\text{ lies in the repeated }\lambda\text{-plane}.
}
$$

These were the last low-defect candidates for an X72-silent two-stress geometry.

DCRP68 puts back a constraint not visible in the pointwise spectral calculation:

$$
\boxed{
L=S+R
=
\nabla V
}
$$

must actually be a **Euclidean velocity gradient**.

Therefore its first derivatives satisfy the exact compatibility equations

$$
\boxed{
\partial_kL_{ij}
=
\partial_jL_{ik}.
}
$$

This extra lift kills both self-lock types on the finite-compensation isotropic-covariance branch.

---

## Type A result

Write

$$
\boxed{
\Omega=r\xi,
\qquad
r>0,
}
$$

and

$$
\boxed{
S
=
\frac{3\lambda}{2}
\left(
\xi\otimes\xi-\frac13I
\right),
}
$$

where $\lambda=\lambda(s)$ is spatially uniform.

The velocity gradient is

$$
\boxed{
L
=
-\frac{\lambda}{2}I
+
\frac{3\lambda}{2}\xi\otimes\xi
+
\frac r2J_\xi,
}
$$

with

$$
J_\xi v=\xi\times v.
$$

At any point rotate coordinates so

$$
\xi=e_3.
$$

The nine first-order compatibility equations act on the nine jet variables

$$
\boxed{
\partial_j\xi_1,\quad
\partial_j\xi_2,\quad
\partial_jr,
\qquad j=1,2,3.
}
$$

The exact determinant of this linear jet system is

$$
\boxed{
\det\mathcal M_A
=
\frac1{256}
(r^2-9\lambda^2)
(r^2+9\lambda^2)^2.
}
$$

Thus if

$$
r^2\neq9\lambda^2,
$$

then

$$
\boxed{
\nabla r=0,
\qquad
\nabla\xi=0.
}
$$

At the only real resonance

$$
\boxed{
r=3\sigma\lambda,
\qquad
\sigma=\pm1,
}
$$

the compatibility kernel is one-dimensional.

Writing

$$
\boxed{
\tau=\xi\cdot\nabla\times\xi,
}
$$

the resonant jet is exactly

$$
\boxed{
\nabla r
=
3\lambda\tau\,\xi,
}
$$

$$
\boxed{
(\xi\cdot\nabla)\xi=0,
}
$$

$$
\boxed{
\nabla\times\xi=\tau\xi,
}
$$

$$
\boxed{
\nabla\cdot\xi=-\sigma\tau,
}
$$

and on the transverse plane

$$
\boxed{
P_\xi(\nabla\xi)P_\xi
=
-\frac{\sigma\tau}{2}P_\xi
+
\frac{\tau}{2}J_\xi.
}
$$

But on an open resonant region,

$$
r=3\sigma\lambda
$$

and $\lambda$ is spatially uniform, so $r$ is spatially constant.

Hence

$$
\nabla r=0,
$$

forcing

$$
\tau=0,
$$

and therefore

$$
\nabla\xi=0.
$$

Combining resonant and nonresonant sets by continuity gives:

## Type-A spatial rigidity

For every connected smooth active Type-A region at a time with

$$
\lambda(s)\neq0,
$$

$$
\boxed{
\nabla r=0,
\qquad
\nabla\xi=0.
}
$$

Therefore all vorticity vectors in the covariance observer are parallel.

The covariance has rank at most one:

$$
\boxed{
B
=
\int\phi r^2\xi\otimes\xi
=
Z\,\xi\otimes\xi.
}
$$

But the finite transparent compensation branch requires

$$
\boxed{
B=\rho I,
\qquad
\rho>0.
}
$$

Contradiction.

Thus:

$$
\boxed{
\textbf{Type A cannot occur at any nonzero-}\lambda\textbf{ time on the isotropic compensation branch.}
}
$$

---

## Type B result

Write

$$
\boxed{
\Omega=r\xi,
}
$$

and let $\zeta$ be the simple $-2\lambda$ strain axis:

$$
\boxed{
\xi\perp\zeta,
}
$$

$$
\boxed{
S
=
-3\lambda
\left(
\zeta\otimes\zeta-\frac13I
\right).
}
$$

Define the right-handed frame

$$
\boxed{
\eta=\zeta\times\xi.
}
$$

The first-order velocity-gradient compatibility system has exactly three local scalar degrees of freedom.

Set

$$
\boxed{
\alpha=\frac{6\lambda}{r},
}
$$

and define

$$
\boxed{
k
=
\eta\cdot(\xi\cdot\nabla)\zeta,
}
$$

$$
\boxed{
u=\eta\cdot\nabla r,
\qquad
v=\zeta\cdot\nabla r.
}
$$

Then the complete first-order director system is:

$$
\boxed{
\xi\cdot\nabla r=0,
}
$$

$$
\boxed{
(\xi\cdot\nabla)\xi=0,
}
$$

$$
\boxed{
(\xi\cdot\nabla)\zeta=k\eta,
}
$$

$$
\boxed{
(\eta\cdot\nabla)\xi=\alpha k\,\eta,
}
$$

$$
\boxed{
(\eta\cdot\nabla)\zeta
=
-\frac{u}{6\lambda}\eta,
}
$$

$$
\boxed{
(\zeta\cdot\nabla)\xi
=
-\alpha^2k\,\eta
-\alpha k\,\zeta,
}
$$

$$
\boxed{
(\zeta\cdot\nabla)\zeta
=
\alpha k\,\xi
+
\frac{v}{6\lambda}\eta.
}
$$

Two immediate consequences are already striking:

$$
\boxed{
\nabla\cdot\xi=0,
}
$$

and

$$
\boxed{
(\Omega\cdot\nabla)\Omega=0.
}
$$

So the Type-B self-lock geometry consists of straight vortex lines carrying constant vorticity magnitude along each line.

However, this first-order system still has the twist scalar $k$.

DCRP68 now uses the fact that $(\xi,\eta,\zeta)$ is an actual orthonormal frame in flat Euclidean space.

Its Levi-Civita curvature must vanish.

From the first-order system:

$$
\boxed{
\nabla_\xi\xi=0,
}
$$

$$
\boxed{
\nabla_\eta\xi=\alpha k\,\eta,
}
$$

$$
\boxed{
\nabla_\xi\eta=-k\zeta,
}
$$

and

$$
\boxed{
[\xi,\eta]
=
-\alpha k\,\eta-k\zeta.
}
$$

Compute the Euclidean curvature:

$$
\boxed{
R(\xi,\eta)\xi
=
\nabla_\xi\nabla_\eta\xi
-
\nabla_\eta\nabla_\xi\xi
-
\nabla_{[\xi,\eta]}\xi.
}
$$

Since

$$
\xi\cdot\nabla r=0,
$$

we also have

$$
\xi\cdot\nabla\alpha=0.
$$

The exact result is

$$
\boxed{
R(\xi,\eta)\xi
=
\alpha(\xi\cdot\nabla k)\eta
-
2\alpha k^2\zeta.
}
$$

Flat Euclidean space requires

$$
R(\xi,\eta)\xi=0.
$$

At every active time with

$$
\lambda\neq0,
\qquad
r>0,
$$

we have

$$
\alpha\neq0.
$$

Hence:

$$
\boxed{
k=0.
}
$$

But every spatial derivative of $\xi$ in the first-order compatibility system is proportional to $k$.

Therefore:

$$
\boxed{
\nabla\xi=0.
}
$$

Again:

$$
\boxed{
B
=
\int\phi r^2\xi\otimes\xi
}
$$

has rank at most one, contradicting

$$
B=\rho I.
$$

Thus:

$$
\boxed{
\textbf{Type B also cannot occur at any nonzero-}\lambda\textbf{ time on the isotropic compensation branch.}
}
$$

---

## Final consequence

DCRP61 gives the turnover-free periodic covariance condition

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}\lambda(s)\,ds
=
\lambda_*
=
\frac{2-3\gamma}{2}
>0.
}
$$

Hence $\lambda$ is nonzero on a positive-measure set of similarity times.

But D68 shows that neither Type A nor Type B can exist at such a time.

Therefore the entire axisymmetric self-lock branch of DCRP67 is impossible.

The aligned/no-turnover X branch is forced into the **shape-active sector**

$$
\boxed{
d\notin
\left\{
0,\pm\frac{3\lambda}{2}
\right\}
}
$$

whenever $\lambda\neq0$.

Consequently:

$$
\boxed{
\Omega_{C,\rm self}>0
}
$$

on the nonzero-stretching part of every surviving aligned/no-turnover period.

The last low-angular-motion equality geometry is gone.

The X branch is no longer:

$$
\boxed{
\text{shape-active}
\vee
\text{axisymmetric orientation-amplitude silence}.
}
$$

It is simply:

$$
\boxed{
\textbf{mandatory cofactor-shape activity}
}
$$

plus the final possibility that pressure/vorticity forcing and the transport–Riesz correlation dynamically cancel that activity.

This is a substantial reduction.

---

# 1. Velocity-gradient compatibility

For a smooth velocity field

$$
V:\mathbb R^3\to\mathbb R^3,
$$

let

$$
L=\nabla V.
$$

Then mixed derivatives commute:

$$
\boxed{
\partial_kL_{ij}
=
\partial_jL_{ik}.
}
\tag{1.1}
$$

This is stronger than using only:

$$
\nabla\cdot S
=
-\frac12\nabla\times\Omega
$$

and

$$
\nabla\cdot\Omega=0.
$$

DCRP68 uses the full first-jet integrability of $L$.

---

# 2. Type A velocity gradient

For Type A:

$$
S
=
\frac{3\lambda}{2}U_\xi,
$$

$$
\Omega=r\xi.
$$

With

$$
J_\xi v=\xi\times v,
$$

$$
R=\frac r2J_\xi.
$$

Therefore:

$$
\boxed{
L
=
-\frac{\lambda}{2}I
+
\frac{3\lambda}{2}\xi\otimes\xi
+
\frac r2J_\xi.
}
\tag{2.1}
$$

At a fixed similarity time:

$$
\boxed{
\nabla\lambda=0.
}
\tag{2.2}
$$

---

# 3. Type A adapted jet

At a point choose coordinates so

$$
\xi=e_3.
$$

Because $|\xi|=1$,

$$
\partial_j\xi_3=0
$$

at that point.

Define:

$$
p_j=\partial_j\xi_1,
$$

$$
q_j=\partial_j\xi_2,
$$

$$
g_j=\partial_jr.
$$

There are exactly nine unknown first derivatives.

The nine equations (1.1) form a homogeneous linear system

$$
\boxed{
\mathcal M_A(\lambda,r)
\begin{pmatrix}
p\\q\\g
\end{pmatrix}
=0.
}
\tag{3.1}
$$

Direct exact elimination gives:

## Theorem D68.1 — Type-A First-Jet Determinant

$$
\boxed{
\det\mathcal M_A
=
\frac{
(r-3\lambda)(r+3\lambda)
(r^2+9\lambda^2)^2
}{
256
}.
}
\tag{3.2}
$$

For real $(r,\lambda)$ with $r>0$, the only nontrivial degeneracy is

$$
r^2=9\lambda^2.
$$

---

# 4. Type A nonresonant rigidity

If

$$
r^2\neq9\lambda^2,
$$

then $\mathcal M_A$ is invertible.

Therefore:

$$
\boxed{
\nabla r=0,
\qquad
\nabla\xi=0.
}
\tag{4.1}
$$

This is pointwise.

---

# 5. Type A resonant jet

Assume

$$
r=3\sigma\lambda,
\qquad
\sigma=\pm1.
$$

The compatibility matrix has nullity one.

Define

$$
\tau
=
\xi\cdot\nabla\times\xi.
$$

Then the null jet is:

## Theorem D68.2 — Type-A Resonant Beltrami Jet

$$
\boxed{
\nabla r
=
3\lambda\tau\,\xi,
}
\tag{5.1}
$$

$$
\boxed{
(\xi\cdot\nabla)\xi=0,
}
\tag{5.2}
$$

$$
\boxed{
\nabla\times\xi
=
\tau\xi,
}
\tag{5.3}
$$

$$
\boxed{
\nabla\cdot\xi
=
-\sigma\tau,
}
\tag{5.4}
$$

and

$$
\boxed{
P_\xi(\nabla\xi)P_\xi
=
-\frac{\sigma\tau}{2}P_\xi
+
\frac{\tau}{2}J_\xi.
}
\tag{5.5}
$$

Thus the only possible first-order Type-A motion is a very specific Beltrami/dilation director jet.

---

# 6. Resonance cannot support an open spatial branch

On an open resonant region:

$$
r=3\sigma\lambda.
$$

But $\lambda$ is spatially uniform.

Hence:

$$
\boxed{
\nabla r=0.
}
$$

Equation (5.1) gives:

$$
\tau=0.
$$

Then (5.5) gives:

$$
\nabla\xi=0.
$$

On the nonresonant set we already have the same conclusion.

At a boundary between the two sets, smoothness gives the result by continuity.

Therefore:

## Theorem D68.3 — Type-A Spatial Rigidity

On every connected active Type-A region at a time with

$$
\lambda\neq0,
$$

$$
\boxed{
r=\text{constant},
\qquad
\xi=\text{constant}.
}
\tag{6.1}
$$

---

# 7. Type A versus isotropic covariance

If $\xi$ is spatially constant,

$$
B
=
\int\phi
r^2\xi\otimes\xi.
$$

Hence:

$$
\boxed{
\operatorname{rank}B\le1.
}
\tag{7.1}
$$

But finite full compensation requires

$$
\boxed{
B=\rho I,
\qquad
\rho>0.
}
\tag{7.2}
$$

Thus:

## Theorem D68.4 — Type-A Self-Lock NO-GO

A nonzero isotropic covariance state cannot realize Type A at any time with $\lambda\neq0$.

---

# 8. Type B setup

For Type B:

$$
\boxed{
S=-3\lambda U_\zeta,
}
\tag{8.1}
$$

$$
\boxed{
\Omega=r\xi,
}
\tag{8.2}
$$

with

$$
\boxed{
\xi\cdot\zeta=0.
}
\tag{8.3}
$$

Define:

$$
\boxed{
\eta=\zeta\times\xi.
}
\tag{8.4}
$$

Then

$$
(\xi,\eta,\zeta)
$$

is a right-handed orthonormal frame.

Set:

$$
\boxed{
\alpha=\frac{6\lambda}{r}.
}
\tag{8.5}
$$

---

# 9. Type B first-jet compatibility

Define:

$$
\boxed{
k
=
\eta\cdot\nabla_\xi\zeta,
}
\tag{9.1}
$$

$$
\boxed{
u=\nabla_\eta r,
\qquad
v=\nabla_\zeta r.
}
\tag{9.2}
$$

Direct solution of the full velocity-gradient compatibility equations gives:

## Theorem D68.5 — Type-B Director-Jet Normal Form

$$
\boxed{
\nabla_\xi r=0,
}
\tag{9.3}
$$

$$
\boxed{
\nabla_\xi\xi=0,
}
\tag{9.4}
$$

$$
\boxed{
\nabla_\xi\zeta=k\eta,
}
\tag{9.5}
$$

$$
\boxed{
\nabla_\eta\xi=\alpha k\eta,
}
\tag{9.6}
$$

$$
\boxed{
\nabla_\eta\zeta
=
-\frac{u}{6\lambda}\eta,
}
\tag{9.7}
$$

$$
\boxed{
\nabla_\zeta\xi
=
-\alpha^2k\eta
-\alpha k\zeta,
}
\tag{9.8}
$$

$$
\boxed{
\nabla_\zeta\zeta
=
\alpha k\xi
+
\frac{v}{6\lambda}\eta.
}
\tag{9.9}
$$

The generic active first jet has only three scalar freedoms:

$$
\boxed{
k,u,v.
}
$$

---

# 10. Straight-vortex consequence

From Theorem D68.5:

$$
\nabla_\xi r=0,
$$

and

$$
\nabla_\xi\xi=0.
$$

Therefore:

## Corollary D68.6 — Straight Constant-Strength Vortex Lines

$$
\boxed{
(\Omega\cdot\nabla)\Omega=0.
}
\tag{10.1}
$$

Also the same jet gives:

$$
\boxed{
\nabla\cdot\xi=0.
}
\tag{10.2}
$$

Thus Type B would consist of straight vortex lines whose direction and magnitude are constant along each individual line.

The remaining texture freedom would be how different straight vortex lines are arranged across space.

---

# 11. Complete frame connection

The derivative formulas imply:

$$
\boxed{
\nabla_\xi\eta=-k\zeta,
}
\tag{11.1}
$$

$$
\boxed{
\nabla_\eta\eta
=
-\alpha k\xi
+
\frac{u}{6\lambda}\zeta,
}
\tag{11.2}
$$

$$
\boxed{
\nabla_\zeta\eta
=
\alpha^2k\xi
-
\frac{v}{6\lambda}\zeta.
}
\tag{11.3}
$$

The frame commutator is:

$$
\boxed{
[\xi,\eta]
=
-\alpha k\eta-k\zeta.
}
\tag{11.4}
$$

Because

$$
\nabla_\xi r=0,
$$

$$
\boxed{
\nabla_\xi\alpha=0.
}
\tag{11.5}
$$

---

# 12. Euclidean zero-curvature kills the twist

Flat Euclidean space has zero Riemann curvature.

Compute:

$$
R(\xi,\eta)\xi
=
\nabla_\xi\nabla_\eta\xi
-
\nabla_\eta\nabla_\xi\xi
-
\nabla_{[\xi,\eta]}\xi.
$$

Use:

$$
\nabla_\eta\xi=\alpha k\eta,
$$

$$
\nabla_\xi\xi=0,
$$

$$
\nabla_\xi\eta=-k\zeta,
$$

and (11.4).

A direct calculation gives:

## Theorem D68.7 — Type-B Twist Curvature Identity

$$
\boxed{
R(\xi,\eta)\xi
=
\alpha(\nabla_\xi k)\eta
-
2\alpha k^2\zeta.
}
\tag{12.1}
$$

Since Euclidean curvature is zero:

$$
\boxed{
\alpha(\nabla_\xi k)=0,
}
$$

and

$$
\boxed{
2\alpha k^2=0.
}
$$

At an active time:

$$
r>0,
\qquad
\lambda\neq0,
$$

so:

$$
\alpha\neq0.
$$

Therefore:

## Theorem D68.8 — Type-B Twist NO-GO

$$
\boxed{
k=0.
}
\tag{12.2}
$$

---

# 13. Type B then has fixed vorticity direction

Every derivative of $\xi$ in Theorem D68.5 is proportional to $k$.

Thus:

$$
\boxed{
k=0
\Longrightarrow
\nabla\xi=0.
}
\tag{13.1}
$$

Therefore:

$$
\boxed{
\operatorname{rank}B\le1.
}
$$

This contradicts

$$
B=\rho I,
\qquad
\rho>0.
$$

Hence:

## Theorem D68.9 — Type-B Self-Lock NO-GO

A nonzero isotropic covariance state cannot realize Type B at any time with $\lambda\neq0$.

---

# 14. Both self-lock normal forms are closed

D67 classified every aligned zero-self-angular-rate spectrum as Type A or Type B.

D68 proves both are incompatible with full-rank isotropic covariance whenever

$$
\lambda\neq0.
$$

Therefore:

## Theorem D68.10 — Axisymmetric Self-Lock Integrability Collapse

On the aligned/no-turnover isotropic covariance branch,

$$
\boxed{
\lambda\neq0
\Longrightarrow
\Omega_{C,\rm self}>0.
}
\tag{14.1}
$$

Equivalently:

$$
\boxed{
d\notin
\left\{
0,\pm\frac{3\lambda}{2}
\right\}
}
\tag{14.2}
$$

at every nonzero-stretching time.

---

# 15. Periodic consequence

The neutral covariance mean is:

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}\lambda(s)ds
=
\lambda_*
=
\frac{2-3\gamma}{2}
>0.
}
\tag{15.1}
$$

Hence the set

$$
\boxed{
\{s:\lambda(s)\neq0\}
}
$$

has positive measure.

On that set:

$$
\boxed{
\Omega_{C,\rm self}>0.
}
$$

Thus:

## Corollary D68.11 — Mandatory Cofactor-Shape Activity in Time

Every surviving aligned/no-turnover finite-compensation period has a positive-measure time set on which the strain cofactor is intrinsically shape-active.

No axisymmetric zero-self-angular-motion equality mode can carry the period.

---

# 16. What this closes from D67

D67 left:

$$
\mathsf X_{\rm shape}
\vee
\mathsf X_A
\vee
\mathsf X_B.
$$

D68 closes:

$$
\boxed{
\mathsf X_A,
\qquad
\mathsf X_B.
}
$$

Therefore:

$$
\boxed{
\mathsf X_{\rm 2stress}
\Longrightarrow
\mathsf X_{\rm shape}.
}
\tag{16.1}
$$

The generic shape-active branch is no longer merely “one possibility.”

It is mandatory.

---

# 17. Why D68 is stronger than the planned one-dimensional audit

The original D68 plan was to classify:

- constant-axis director fields;
- one-dimensional director textures.

The full velocity-gradient compatibility is much stronger.

### Type A

It gives complete spatial rigidity on every connected active equality patch.

### Type B

It gives a three-scalar first-jet normal form, then Euclidean flatness forces the only director-twist scalar to vanish.

Thus the two axisymmetric self-lock modes fail before any one-dimensional or global-energy classification is needed.

The obstruction is local differential integrability plus the global isotropic-covariance identity.

---

# 18. Relationship to X72 Round36

Round36 computed a positive self-induced cofactor angular rate away from axisymmetric strain shape.

At that stage, axisymmetric shape was a genuine null manifold.

D68 proves that the two aligned axisymmetric points on that null manifold are not compatible with the actual velocity-gradient integrability and the full-rank isotropic covariance required by finite X72 compensation.

Thus the Round36 angular-rate null manifold has been removed **inside the aligned/no-turnover rank-three compensation branch**.

This is a significant strengthening of the X72 branch geometry.

---

# 19. Remaining cancellation mechanism

D68 does not prove the X72 transport–Riesz commutator is nonzero.

The cofactor can be intrinsically shape-active while:

- pressure/vorticity forcing counter-rotates it;
- spatial transport phase-locks the shape;
- principal-value angular sectors cancel.

The remaining equality problem is therefore:

$$
\boxed{
\textbf{
mandatory intrinsic cofactor-shape motion}
}
$$

versus

$$
\boxed{
\textbf{
pressure/vorticity/transport phase locking}.
}
$$

This is much smaller than the previous orientation–amplitude director problem.

---

# 20. Natural next observable

Define the X72 cofactor self-angular action:

$$
\boxed{
\mathfrak A_C
=
\int_0^{S_0}
\int
\phi
\,
\Omega_{C,\rm self}^2
\,dy\,ds.
}
\tag{20.1}
$$

D68 proves:

$$
\boxed{
\mathfrak A_C>0
}
$$

qualitatively on every smooth surviving aligned/no-turnover period, provided the active nonzero-$\lambda$ set intersects the nonzero covariance support.

An unconditional quantitative lower bound still requires compactness/separation from the forbidden self-lock sets.

The next round should derive whether exact periodic cofactor return forces a compensating pressure/vorticity/transport angular action at least as large as $\mathfrak A_C$.

---

# 21. NTLA-O interpretation

At the spectral observer level, Type A and Type B are perfectly admissible zero-angular-rate tensors.

At the velocity-gradient observer level, Type A collapses to a constant director.

At the moving-frame curvature observer level, Type B's only director-twist degree of freedom creates a forbidden Euclidean curvature term

$$
-2\alpha k^2\zeta.
$$

At the covariance observer level, both constant-vorticity-direction outcomes fail the full-rank isotropy requirement.

Thus:

$$
\boxed{
\text{spectral self-lock}
}
$$

does not lift to

$$
\boxed{
\text{gradient-integrable isotropic covariance state}.
}
$$

This is another exact local-to-global realizability failure.

---

# 22. Status ledger

## PROVED this round

### D68-P1 — Type-A compatibility determinant

$$
\det\mathcal M_A
=
\frac{
(r^2-9\lambda^2)
(r^2+9\lambda^2)^2
}{256}.
$$

### D68-P2 — Type-A nonresonant first-jet rigidity.

### D68-P3 — exact Type-A resonant Beltrami jet.

### D68-P4 — open Type-A resonance collapses because $\lambda$ is spatially uniform.

### D68-P5 — Type-A self-lock is incompatible with isotropic covariance.

### D68-P6 — complete Type-B three-scalar director-jet normal form.

### D68-P7 — Type-B straight constant-strength vortex-line identity

$$
(\Omega\cdot\nabla)\Omega=0.
$$

### D68-P8 — Type-B Euclidean curvature identity

$$
R(\xi,\eta)\xi
=
\alpha(\xi k)\eta
-
2\alpha k^2\zeta.
$$

### D68-P9 — Type-B twist vanishes

$$
k=0.
$$

### D68-P10 — Type-B self-lock is incompatible with isotropic covariance.

### D68-P11 — both aligned axisymmetric self-lock modes are closed.

### D68-P12 — mandatory positive-measure cofactor-shape activity over a neutral period.

---

# 23. New STOP

$$
\boxed{
\textbf{
STOP-D68:
Both axisymmetric zero-self-angular-rate stress geometries found in D67 fail the next realizability lift. Type A is first-jet rigid except for a resonance that collapses under spatially uniform stretching; Type B's only vorticity-director twist creates nonzero Euclidean frame curvature and must vanish. Both outcomes leave a fixed vorticity direction and contradict isotropic rank-three covariance. Hence every surviving aligned/no-turnover branch is necessarily cofactor-shape-active.
}
}
$$

---

# 24. Next autonomous step

## DCRP69 / X72-R52 — Cofactor-Shape Action versus Pressure/Transport Phase Lock

**Working title**

> **Mandatory Cofactor Angular Action, Pressure–Vorticity Counter-Rotation, and Periodic Shape Return**

Primary tasks:

1. derive the exact material evolution of the normalized cofactor direction
   $$
   \widehat C
   =
   C/|C|;
   $$
2. split its angular velocity into:
   - self term;
   - pressure-Hessian/vorticity forcing;
   - transport/nonlocal term;
3. integrate over one DSS period;
4. use D68:
   $$
   \Omega_{C,\rm self}>0
   $$
   on every nonzero-stretching time;
5. determine whether periodic return of $\widehat C$ forces a quantitative counter-rotation action;
6. identify that counter-rotation with:
   - X72 pressure defect;
   - transport–Riesz commutator transfer;
   - or material turnover;
7. if an exact phase-lock mode exists, classify its tensor geometry.

Desired endpoint:

$$
\boxed{
\mathsf X_{\rm shape}
\Longrightarrow
\text{positive pressure/transport angular action}
\vee
\text{one explicit phase-lock normal form}.
}
$$

---

# 25. One-line checkpoint

The two axisymmetric X72 self-lock modes are now gone: full velocity-gradient integrability forces Type A spatial rigidity and Type B zero director twist, both incompatible with isotropic rank-three covariance, so every surviving aligned/no-turnover period must carry genuine intrinsic cofactor-shape angular motion.

---

**End checkpoint:** DCRP68 / X72-R51  
**Next:** DCRP69 / X72-R52 — Cofactor-Shape Action / Phase-Lock Rigidity.
