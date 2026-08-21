# DCRP97 / X72-R80 — Dual-Lock PSD Cone, Increment–Vorticity Scope Repair, and the Quantitative Pancake-Equality Gap

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / dual-lock rank-two compatibility round  
**Immediate predecessor:** `NS_DCRP96_X72R79_CirculationYoung_NematicLock_2026-08-20.md`

## Primary internal dependencies

- DCRP24–26 — increment covariance / pressure-compatible kernel / SGS recurrence.
- DCRP40–41 — rank-two **vorticity** covariance, normal-compression Floquet rigidity, canonical pancake affine jet.
- DCRP50–60 — rank-two closure package and X72 frontier.
- DCRP95–96 — sign-coherent SGS Kelvin phase slip and dual covariance lock.

## Fresh primary-source calibration

- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560 (2026).
  - Critical derivative-compatible increment defects admit cylindrical generalized Young profiles.
  - The differentiated SGS stress is controlled by increment defects.
  - The source does **not** supply the additional identification used in older DCRP rank-two geometry between a velocity-increment covariance kernel and a filtered-vorticity covariance plane.
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570 (2026).

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP96 reduced the compact phase-slip survivor to a covariance satisfying two positive linear projections:

\[
\boxed{
\sigma_\Gamma A_\Gamma:Q^0
\ge
c_\Gamma^*>0,
}
\]

and, on the pure recurrent strong-increment branch,

\[
\boxed{
-S:Q^0
=
-S:Q
\ge
c_E^*>0.
}
\]

Here:

- \(Q\ge0\) is the **velocity-increment** Reynolds/Young covariance;
- \(A_\Gamma\) is the trace-free oriented circulation-current detector;
- \(S\) is the resolved strain.

The originally proposed D97 step tried to impose:

\[
Qn=0
\]

using the normal \(n\) of the old D40 rank-two **vorticity covariance**.

That identification is not currently proved.

D97 therefore begins with a scope repair.

Let:

\[
B_\omega
\]

be the rank-two filtered-vorticity covariance from D40, with:

\[
B_\omega n=0.
\]

Let:

\[
Q
\]

be the increment covariance from D24/D96.

They are different objects.

Define the normalized increment normal share:

\[
\boxed{
\theta_Q
=
\frac{
n^TQn
}{
\operatorname{tr}Q
}
\in[0,1].
}
\tag{0.1}
\]

Then:

- \(\theta_Q=0\) means the increment covariance is supported in the vorticity plane;
- \(\theta_Q>0\) means increment–vorticity carrier unlock / normal increment spread.

Now insert the canonical D40 pancake affine strain:

\[
\boxed{
A_*
=
\frac{c_\gamma}{2}
(I-n\otimes n)
-
c_\gamma n\otimes n
=
\frac{c_\gamma}{2}I
-
\frac{3c_\gamma}{2}
n\otimes n,
}
\tag{0.2}
\]

where:

\[
c_\gamma=2-3\gamma>0.
\]

Write:

\[
\boxed{
S
=
A_*+\Delta S.
}
\tag{0.3}
\]

For every positive semidefinite \(Q\) with:

\[
\tau=\operatorname{tr}Q>0,
\]

one has the exact identity:

\[
\boxed{
-S:Q
=
-\frac{c_\gamma}{2}\tau
+
\frac{3c_\gamma}{2}
n^TQn
-
\Delta S:Q.
}
\tag{0.4}
\]

Since:

\[
|\Delta S:Q|
\le
\|\Delta S\|_{\rm op}
\operatorname{tr}Q
=
\tau\|\Delta S\|_{\rm op},
\]

a forward SGS lock:

\[
-S:Q\ge c_E^*>0
\]

forces:

# Main quantitative equality-gap theorem

\[
\boxed{
\frac{3c_\gamma}{2}
\theta_Q
+
\|\Delta S\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+
\frac{c_E^*}{\tau}.
}
\tag{0.5}
\]

Thus the D96 dual-lock survivor cannot approach the canonical rank-two pancake equality manifold.

It must pay at least one of:

1. **increment–vorticity carrier unlock**
   \[
   \theta_Q\ge c_{\rm unlock}>0;
   \]

2. **uniform non-affine/pancake strain gap**
   \[
   \|\Delta S\|_{\rm op}
   \ge
   c_{\rm pan}>0.
   \]

In particular, if the increment covariance is exactly plane-locked:

\[
Qn=0,
\]

and the strain is exactly canonical:

\[
S=A_*,
\]

then:

\[
\boxed{
\Pi_{\rm SGS}
=
-S:Q
=
-\frac{c_\gamma}{2}
\operatorname{tr}Q
<
0.
}
\tag{0.6}
\]

The canonical pancake equality mode is therefore **strictly backscatter-only** for every plane-supported positive increment covariance.

It can never realize the D96 positive-forward dual lock.

---

# 1. Scope repair — two covariance fields

The old D40–60 rank-two object is:

\[
\boxed{
B_\omega
=
\int
\phi
\,
\Omega\otimes\Omega.
}
\]

It is a filtered-vorticity covariance.

The D24/D96 Young-profile object is schematically:

\[
\boxed{
Q_u
=
\int
(\xi-m)\otimes(\xi-m)
\,d\nu
+
Q^c.
}
\]

It is a velocity-increment covariance.

There is currently no theorem:

\[
\boxed{
\ker Q_u
=
\ker B_\omega.
}
\]

Therefore D97 does **not** silently write:

\[
Q_un=0.
\]

Instead it defines the cross-covariance normal-support coordinate:

\[
\boxed{
\theta_Q
=
\frac{
n^TQ_un
}{
\operatorname{tr}Q_u
}.
}
\]

If:

\[
\theta_Q
\not\to0,
\]

the increment microstructure is not locked to the vorticity plane.

This is an explicit:

\[
\boxed{
R_{\rm IV\mbox{-}unlock}
}
\]

state/covariance transition coordinate.

Only on:

\[
\theta_Q=0
\]

does the old planar rank-two geometry become directly applicable to the increment covariance.

---

# 2. Rank audit for the increment covariance

Normalize:

\[
\tau
=
\operatorname{tr}Q>0.
\]

For a compact covariance family there are four structural possibilities.

## A. rank one / spectral collapse

\[
\lambda_2(Q)\to0.
\]

This returns to a one-direction increment microstructure and is aligned with the old low-rank/fiber branch.

## B. rank three

\[
\lambda_3(Q)\ge b_3>0.
\]

Then automatically:

\[
\theta_Q>0
\]

for every vorticity-plane normal outside a special eigenconfiguration.

This is an increment-covariance spread/rank-lift coordinate.

## C. rank two but wrong plane

\[
\operatorname{rank}Q=2,
\]

with kernel:

\[
m_Q
\neq\pm n.
\]

Then:

\[
\theta_Q>0.
\]

This is cross-covariance plane unlock.

## D. locked rank two

\[
\boxed{
Qn=0,
\qquad
\operatorname{rank}Q=2.
}
\]

Only this branch enters the planar dual-cone calculation below.

---

# 3. Exact D40 pancake tensor

D40 proves on the frozen-affine zero-residual equality branch that the normal eigenvalue is:

\[
-c_\gamma,
\]

while periodicity of the positive in-plane covariance forces the two in-plane eigenvalues to be:

\[
\frac{c_\gamma}{2}.
\]

Thus in a basis with:

\[
n=e_3,
\]

\[
\boxed{
A_*
=
\begin{pmatrix}
c_\gamma/2&0&0\\
0&c_\gamma/2&0\\
0&0&-c_\gamma
\end{pmatrix}.
}
\tag{3.1}
\]

Equivalently:

\[
A_*
=
\frac{c_\gamma}{2}I
-
\frac{3c_\gamma}{2}
n\otimes n.
\]

This is the canonical axisymmetric planar-extension / normal-compression pancake strain.

---

# 4. Exact forward-work identity around the pancake

Let:

\[
S=A_*+\Delta S.
\]

Let:

\[
Q=Q^T\ge0,
\qquad
\tau=\operatorname{tr}Q.
\]

Then:

\[
\begin{aligned}
A_*:Q
&=
\frac{c_\gamma}{2}
\operatorname{tr}Q
-
\frac{3c_\gamma}{2}
n^TQn
\\
&=
\frac{c_\gamma}{2}\tau
-
\frac{3c_\gamma}{2}n^TQn.
\end{aligned}
\]

Hence:

## Theorem D97.1 — Pancake SGS-Work Decomposition

\[
\boxed{
\Pi_{\rm SGS}
=
-S:Q
=
-\frac{c_\gamma}{2}\tau
+
\frac{3c_\gamma}{2}n^TQn
-
\Delta S:Q.
}
\tag{4.1}
\]

No rank assumption on \(Q\) is needed.

---

# 5. Quantitative equality-manifold separation

Because:

\[
Q\ge0,
\]

its nuclear norm is:

\[
\|Q\|_*
=
\operatorname{tr}Q
=
\tau.
\]

Therefore:

\[
-\Delta S:Q
\le
|\Delta S:Q|
\le
\tau
\|\Delta S\|_{\rm op}.
\]

If:

\[
\Pi_{\rm SGS}
\ge
c_E^*,
\]

then D97.1 gives:

\[
c_E^*
\le
-\frac{c_\gamma}{2}\tau
+
\frac{3c_\gamma}{2}n^TQn
+
\tau\|\Delta S\|_{\rm op}.
\]

Divide by:

\[
\tau.
\]

## Theorem D97.2 — Forward Dual-Lock Equality Gap

\[
\boxed{
\frac{3c_\gamma}{2}
\theta_Q
+
\|\Delta S\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+
\frac{c_E^*}{\tau}.
}
\tag{5.1}
\]

This is the main theorem of D97.

It says the positive-forward D96 covariance cannot converge to:

\[
\theta_Q=0,
\qquad
\Delta S=0.
\]

---

# 6. Two-branch quantitative split

Let:

\[
C_*
=
\frac{c_\gamma}{2}
+
\frac{c_E^*}{\tau}.
\]

From:

\[
\frac{3c_\gamma}{2}
\theta_Q
+
\|\Delta S\|_{\rm op}
\ge
C_*,
\]

at least one of:

\[
\boxed{
\theta_Q
\ge
\frac{
C_*
}{
3c_\gamma
}
}
\tag{6.1}
\]

or:

\[
\boxed{
\|\Delta S\|_{\rm op}
\ge
\frac{
C_*
}{
2
}
}
\tag{6.2}
\]

holds.

The constants are intentionally nonoptimal.

Thus every forward dual-lock event has a uniform:

\[
\boxed{
R_{\rm IV\mbox{-}unlock}
\vee
R_{\rm pancake\mbox{-}gap}.
}
\tag{6.3}
\]

---

# 7. Perfect plane lock gives a stronger no-go

If:

\[
Qn=0,
\]

then:

\[
n^TQn=0.
\]

D97.1 becomes:

\[
\Pi_{\rm SGS}
=
-\frac{c_\gamma}{2}\tau
-
\Delta S:Q.
\]

Therefore:

\[
\Pi_{\rm SGS}\ge c_E^*
\]

forces:

\[
\boxed{
\|\Delta S\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+
\frac{c_E^*}{\tau}.
}
\tag{7.1}
\]

In particular:

## Corollary D97.3 — Exact Pancake / Plane-Lock NO-GO

\[
\boxed{
Qn=0,
\quad
S=A_*
\Longrightarrow
\Pi_{\rm SGS}
=
-\frac{c_\gamma}{2}\tau
<0.
}
\tag{7.2}
\]

This holds for **every** plane-supported PSD covariance, independent of its planar anisotropy.

---

# 8. General locked rank-two parameterization

Now impose:

\[
Qn=0,
\]

\[
\operatorname{rank}Q=2,
\]

and normalize:

\[
\operatorname{tr}Q=\tau.
\]

Let:

\[
P=I-n\otimes n.
\]

Then:

\[
\boxed{
Q
=
\frac{\tau}{2}P
+
D,
}
\tag{8.1}
\]

where:

\[
Dn=0,
\qquad
\operatorname{tr}D=0.
\]

Choose an orthonormal basis:

\[
(v,w)
\]

of:

\[
n^\perp.
\]

Then:

\[
\boxed{
D
=
d
(
v\otimes v-w\otimes w
),
}
\tag{8.2}
\]

with eigenvalues:

\[
\lambda_{1,2}
=
\frac{\tau}{2}\pm d.
\]

If:

\[
\lambda_{\min}^+(Q)\ge b_0>0,
\]

then:

\[
\boxed{
|d|
\le
\frac{\tau}{2}-b_0.
}
\tag{8.3}
\]

Equivalently:

\[
\boxed{
\|D\|_F
\le
\sqrt2
\left(
\frac{\tau}{2}-b_0
\right).
}
\tag{8.4}
\]

The planar anisotropy lives in a two-dimensional closed disk.

---

# 9. Extreme points of the spectral-gap slice

Define:

\[
\mathcal K_{b_0}(n,\tau)
=
\left\{
Q\ge0:
Qn=0,
\operatorname{tr}Q=\tau,
Q|_{n^\perp}\ge b_0I
\right\}.
\]

Write:

\[
Q
=
b_0P
+
(\tau-2b_0)\rho,
\]

where:

\[
\rho\ge0,
\qquad
\rho n=0,
\qquad
\operatorname{tr}\rho=1.
\]

The extreme points of the planar density-matrix disk are rank-one projectors:

\[
\rho=v\otimes v.
\]

Therefore:

## Theorem D97.4 — Regularized Rank-One Extremals

The extreme points of:

\[
\mathcal K_{b_0}(n,\tau)
\]

are:

\[
\boxed{
Q_v
=
b_0P
+
(\tau-2b_0)
v\otimes v,
\qquad
v\perp n,
\quad
|v|=1.
}
\tag{9.1}
\]

Their positive eigenvalues are:

\[
\boxed{
\tau-b_0,
\qquad
b_0.
}
\tag{9.2}
\]

As:

\[
b_0\downarrow0,
\]

they converge to the rank-one boundary.

Thus every extremal rank-two dual-lock configuration is a spectral-gap regularization of a rank-one direction.

---

# 10. Detector decomposition in the locked plane

Let:

\[
T=T^T,
\qquad
\operatorname{tr}T=0.
\]

Define:

\[
t_n=n^TTn.
\]

Let:

\[
T_P^0
\]

be the trace-free part of the restriction of \(T\) to \(n^\perp\).

For:

\[
Q=\frac{\tau}{2}P+D,
\]

one has:

## Theorem D97.5 — Trace-Free Detector Formula

\[
\boxed{
T:Q
=
-\frac{\tau}{2}
t_n
+
T_P^0:D.
}
\tag{10.1}
\]

The normal component and planar anisotropy are the only degrees of freedom visible to a trace-free detector.

---

# 11. Dual-lock inequalities as two half-planes in a disk

Let:

\[
G
=
\sigma_\Gamma A_\Gamma,
\]

and:

\[
H
=
-S.
\]

Both are trace-free symmetric tensors.

The D96 dual-lock inequalities are:

\[
G:Q
\ge
c_\Gamma^*,
\]

\[
H:Q
\ge
c_E^*.
\]

Using D97.5:

\[
\boxed{
G_P^0:D
\ge
a_\Gamma,
}
\tag{11.1}
\]

where:

\[
\boxed{
a_\Gamma
=
c_\Gamma^*
+
\frac{\tau}{2}
n^TGn,
}
\tag{11.2}
\]

and:

\[
\boxed{
H_P^0:D
\ge
a_E,
}
\tag{11.3}
\]

where:

\[
\boxed{
a_E
=
c_E^*
+
\frac{\tau}{2}
n^THn.
}
\tag{11.4}
\]

Since:

\[
H=-S,
\]

\[
n^THn=-n^TSn.
\]

The dual-lock problem is therefore a two-half-plane feasibility problem inside the planar anisotropy disk:

\[
\boxed{
\|D\|_F
\le
R_D
:=
\sqrt2
\left(
\frac{\tau}{2}-b_0
\right).
}
\tag{11.5}
\]

---

# 12. Exact minimax / Farkas criterion

Let:

\[
u=G_P^0,
\qquad
v=H_P^0
\]

as vectors in the two-dimensional Hilbert space of planar trace-free symmetric matrices.

There exists:

\[
D,
\qquad
\|D\|_F\le R_D,
\]

satisfying:

\[
u:D\ge a_\Gamma,
\]

\[
v:D\ge a_E
\]

if and only if for every:

\[
\lambda\in[0,1],
\]

one has:

## Theorem D97.6 — Two-Detector Disk Feasibility

\[
\boxed{
R_D
\left\|
\lambda u
+
(1-\lambda)v
\right\|_F
\ge
\lambda a_\Gamma
+
(1-\lambda)a_E.
}
\tag{12.1}
\]

### Proof sketch

If a feasible \(D\) exists, then:

\[
[
\lambda u+(1-\lambda)v
]:D
\ge
\lambda a_\Gamma
+
(1-\lambda)a_E.
\]

Cauchy–Schwarz gives the necessary inequality.

Conversely, if the intersection of the disk with the two half-spaces is empty, the finite-dimensional separation theorem gives nonnegative multipliers \(\mu_1,\mu_2\), not both zero, separating the disk from the constraint set. Normalize:

\[
\lambda
=
\frac{\mu_1}{\mu_1+\mu_2}.
\]

The support function of the Frobenius disk is:

\[
R_D
\|
\lambda u+(1-\lambda)v
\|_F,
\]

contradicting (12.1).

\[
\square
\]

This is an exact finite-dimensional description of the locked rank-two dual cone.

---

# 13. Individual anisotropy thresholds

D97.6 immediately gives the necessary conditions:

\[
\boxed{
R_D
\|G_P^0\|_F
\ge
a_\Gamma
}
\tag{13.1}
\]

when:

\[
a_\Gamma>0,
\]

and:

\[
\boxed{
R_D
\|H_P^0\|_F
\ge
a_E
}
\tag{13.2}
\]

when:

\[
a_E>0.
\]

For the energy detector:

\[
H=-S.
\]

Write:

\[
s_n=n^TSn.
\]

Then:

\[
a_E
=
c_E^*
-
\frac{\tau}{2}s_n.
\]

If the normal remains compressive:

\[
s_n\le-\kappa_0<0,
\]

then:

\[
a_E
\ge
c_E^*
+
\frac{\tau}{2}\kappa_0.
\]

Therefore:

## Theorem D97.7 — Planar-Anisotropic-Strain Threshold

On a locked rank-two branch with normal compression:

\[
\boxed{
\|S_P^0\|_F
\ge
\frac{
c_E^*
+
\frac{\tau}{2}\kappa_0
}{
\sqrt2
\left(
\frac{\tau}{2}-b_0
\right)
}.
}
\tag{13.3}
\]

If:

\[
b_0\to\tau/2,
\]

the covariance becomes planar-isotropic and the required strain anisotropy diverges.

Thus near the planar-isotropic covariance state, forward SGS work is incompatible with persistent normal compression.

---

# 14. Frozen canonical pancake annihilates the forward cone

For the D40 canonical tensor:

\[
S=A_*,
\]

the plane restriction is isotropic:

\[
S_P^0=0.
\]

The normal strain is:

\[
s_n=-c_\gamma.
\]

Therefore:

\[
H_P^0=0,
\]

while:

\[
a_E
=
c_E^*
+
\frac{\tau c_\gamma}{2}
>0.
\]

D97.6 fails already at:

\[
\lambda=0.
\]

Hence:

## Theorem D97.8 — Exact Dual-Lock Empty Cone on the Canonical Pancake

\[
\boxed{
\mathcal C_{\rm dual}^{\rm rank2}
\cap
\{
S=A_*,
\ Qn=0
\}
=
\varnothing
}
\]

for every:

\[
c_E^*>0.
\]

The Kelvin-slip detector does not need to be inspected further.

The forward SGS detector alone empties the cone.

---

# 15. The cone is nonempty away from the equality manifold

The previous theorem is not a universal algebraic no-go.

Take:

\[
n=e_3,
\]

\[
\tau=1,
\]

\[
b_0=0.2,
\]

and the extreme rank-two covariance:

\[
Q
=
\operatorname{diag}(0.8,0.2,0).
\]

Let:

\[
G
=
\operatorname{diag}(1,-1,0).
\]

Then:

\[
G:Q=0.6>0.
\]

Choose a strongly anisotropic trace-free strain:

\[
S
=
\operatorname{diag}(-1,1.2,-0.2).
\]

Then:

\[
-S:Q
=
0.56>0.
\]

Thus:

## Theorem D97.9 — Algebraic Dual-Lock Compatibility Away from Pancake Equality

The locked rank-two dual cone is nonempty for sufficiently anisotropic strain.

Therefore D97 does not prove:

\[
\mathcal C_{\rm dual}^{\rm rank2}
=
\varnothing
\]

in general.

It proves instead a **uniform distance from the canonical rank-two/X72-transparent equality manifold**.

---

# 16. Relation to the old D40–60 rank-two branch

D40 gives the corrected rank-two vorticity branch:

\[
\boxed{
\text{rank-one collapse}
\vee
\text{rank-three lifting}
\vee
\text{plane/covariance residual}
\vee
\text{planar conformal Floquet mode}.
}
\]

D60 packages the strongest equality route with:

- fixed vorticity plane;
- zero covariance-shape action;
- canonical pancake affine jet;
- gauge-flat scalar connection;
- perfect central response;
- perfect local X72 pressure response;
- zero covariance residual.

D60 then proves that a nonzero global continuation cannot remain inside all equality hypotheses and must enter:

\[
\boxed{
\mathsf X
\vee
\mathsf N
\vee
\mathsf T.
}
\]

D97 adds a new independent fact.

A compact D96 **forward dual-lock increment covariance** cannot even approach the canonical pancake interior unless it develops:

\[
\boxed{
R_{\rm IV\mbox{-}unlock}
\vee
R_{\rm pancake\mbox{-}gap}.
}
\]

Thus the phase-slip/forward-work survivor is automatically transverse to the maximally rigid X72-transparent rank-two equality manifold.

D97 does **not** identify which of:

\[
\mathsf X,\mathsf N,\mathsf T
\]

must fire.

That requires the next dynamical compatibility step.

---

# 17. Robust compact-class version

Suppose:

\[
\tau
\in
[\tau_-,\tau_+],
\qquad
\tau_->0,
\]

and:

\[
c_E^*\ge e_0>0.
\]

Then:

\[
\frac{c_E^*}{\tau}
\ge
\frac{e_0}{\tau_+}.
\]

D97.2 gives:

\[
\boxed{
\frac{3c_\gamma}{2}
\theta_Q
+
\|\Delta S\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+
\frac{e_0}{\tau_+}
=:
c_{\rm eq}>0.
}
\tag{17.1}
\]

Hence on any compact normalized dual-lock class:

\[
\boxed{
\operatorname{dist}
(
(Q,S),
\mathcal M_{\rm pancake}
)
\ge
c_{\rm eq}'
>0
}
\]

for a natural product metric controlling:

- increment normal share;
- strain operator deviation.

There is no sequence of positive-forward dual-lock states converging to the pancake equality manifold.

---

# 18. Updated D96 compiler

D96 left:

\[
\mathsf C_{\rm slip}
\Longrightarrow
R_{\rm fiber}
\vee
R_{\rm conc}
\vee
R_{\rm state}
\vee
R_{\rm scale}
\vee
\mathsf C_{\rm dual}.
\]

D97 refines the last branch.

On a compact normalized positive-forward recurrence class:

\[
\boxed{
\mathsf C_{\rm dual}
\Longrightarrow
R_{\rm IV\mbox{-}unlock}
\vee
R_{\rm pancake\mbox{-}gap}.
}
\tag{18.1}
\]

If the increment and vorticity covariances are exactly plane-locked:

\[
\boxed{
\mathsf C_{\rm dual}^{\rm locked}
\Longrightarrow
R_{\rm pancake\mbox{-}gap}.
}
\tag{18.2}
\]

The residual locked cone is exactly the finite two-half-plane / disk problem of D97.6 and has one angular extremal parameter after spectral-gap normalization.

---

# 19. What has actually been eliminated

D97 eliminates several possible overclaims and one real equality endpoint.

## Overclaim removed

\[
\ker Q_u
=
\ker B_\omega
\]

is **not** assumed.

## Equality endpoint removed

The canonical rank-two pancake strain with plane-supported increment covariance cannot have positive SGS forward work.

## New quantitative fact

Forward dual lock has a uniform distance from the pancake equality manifold.

## Remaining finite-dimensional survivor

A plane-locked rank-two covariance can support both positive Kelvin-slip and positive SGS work only with sufficiently strong non-axisymmetric planar strain.

Its extremal covariance is:

\[
Q_v
=
b_0P
+
(\tau-2b_0)
v\otimes v.
\]

Thus the remaining compact geometry has only:

- one plane normal \(n\);
- one planar angle \(v\);
- one spectral-gap parameter \(b_0/\tau\);
- one non-axisymmetric strain tensor component;
- the finite Kelvin detector frame.

This is genuinely finite-dimensional.

---

# 20. Status ledger

## PROVED this round

### D97-P1 — increment covariance and vorticity covariance are kept distinct; no unproved kernel identification.

### D97-P2 — exact pancake SGS-work decomposition:

\[
-S:Q
=
-\frac{c_\gamma}{2}\tau
+
\frac{3c_\gamma}{2}n^TQn
-
\Delta S:Q.
\]

### D97-P3 — forward work forces the quantitative unlock/non-affine gap:

\[
\frac{3c_\gamma}{2}\theta_Q
+
\|\Delta S\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+
\frac{c_E^*}{\tau}.
\]

### D97-P4 — exact plane-lock/canonical-pancake state is strictly backscatter:

\[
\Pi_{\rm SGS}
=
-\frac{c_\gamma}{2}\tau<0.
\]

### D97-P5 — locked rank-two covariance parameterization.

### D97-P6 — exact regularized-rank-one extreme points of the spectral-gap covariance slice.

### D97-P7 — trace-free detector decomposition into normal and planar-anisotropy components.

### D97-P8 — exact two-detector disk feasibility / Farkas criterion.

### D97-P9 — quantitative planar-anisotropic strain threshold under normal compression.

### D97-P10 — canonical pancake dual-lock cone is empty.

### D97-P11 — explicit anisotropic example shows the general rank-two dual cone is nonempty away from equality.

### D97-P12 — compact positive-forward dual-lock states stay a uniform distance from the D40–60 pancake/X72-transparent equality manifold.

---

# 21. What is NOT proved

D97 does not prove:

- every increment covariance is rank two;
- every increment covariance shares the vorticity-plane kernel;
- every non-affine strain gap forces X72 immediately;
- every dual-lock anisotropic strain produces positive vorticity-stretching \(N\);
- the two-detector rank-two disk is empty in general;
- the remaining anisotropic cone is dynamically realizable;
- global Navier–Stokes regularity.

The remaining problem is no longer generic PSD feasibility.

It is:

> can the **uniform pancake-equality exit** forced by forward phase-slip recurrence remain X72/turnover-invisible under strict DSS dynamics?

---

# 22. STOP-D97

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The D96 dual-lock covariance cannot be inserted into the old rank-two/X72 geometry by silently identifying velocity-increment covariance with filtered-vorticity covariance. D97 repairs that scope error by measuring the increment normal share \(\theta_Q=n^TQn/\operatorname{tr}Q\). Anchoring at D40's canonical pancake strain \(A_*=\frac{c_\gamma}{2}I-\frac{3c_\gamma}{2}n\otimes n\), every PSD increment covariance satisfies the exact identity
\[
\Pi_{\rm SGS}
=
-\frac{c_\gamma}{2}\operatorname{tr}Q
+
\frac{3c_\gamma}{2}n^TQn
-
(S-A_*):Q.
\]
Therefore a positive forward lock \(\Pi_{\rm SGS}\ge c_E^*>0\) forces
\[
\frac{3c_\gamma}{2}\theta_Q+\|S-A_*\|_{\rm op}
\ge
\frac{c_\gamma}{2}
+\frac{c_E^*}{\operatorname{tr}Q}.
\]
The dual-lock survivor can never approach the maximally rigid pancake equality state: it must either unlock the increment covariance from the vorticity plane or develop a uniform non-axisymmetric/non-affine strain gap. Under exact plane lock, the canonical pancake gives \(\Pi_{\rm SGS}=-c_\gamma\operatorname{tr}Q/2<0\) for every PSD planar covariance, independent of anisotropy. On the remaining locked rank-two branch, the covariance is \(Q=\tau P/2+D\) with \(D\) in a two-dimensional anisotropy disk, and the Kelvin/energy locks become two half-space inequalities; an exact Farkas criterion reduces feasibility to a one-parameter extremal family \(Q_v=b_0P+(\tau-2b_0)v\otimes v\). The cone is nonempty for sufficiently anisotropic strain, so pure algebra does not finish the proof. What D97 does prove is that the last phase-slip/forward-work conveyor is uniformly transverse to the old D40–60 X72-transparent rank-two equality manifold. The next step is to convert that forced transverse strain/carrier gap into the existing X72 / non-affine stretching / turnover coordinates.
\end{minipage}
}
\]

---

# 23. Next autonomous step

## DCRP98 / X72-R81 — Pancake-Gap to X72 / Non-Affine Turnover Visibility

**Working title**

> **Does the Uniform Increment–Vorticity Unlock / Non-Axisymmetric Strain Gap Forced by D97 Necessarily Enter X72 Pressure Response, Positive Non-Affine Vorticity Stretching, or Material Turnover?**

Primary tasks:

1. start from:
   \[
   \frac{3c_\gamma}{2}\theta_Q
   +
   \|\Delta S\|_{\rm op}
   \ge c_{\rm eq}>0;
   \]
2. split:
   - increment–vorticity unlock \(\theta_Q\ge c\);
   - plane-locked non-affine strain \(\|\Delta S\|\ge c\);
3. for unlock:
   - compare normal increment covariance with D50 rank-lift / plane-spread coordinates;
4. for non-affine strain:
   - insert \(S=A_*+E\) into the vorticity covariance equation;
   - evaluate \(E:B_\omega\);
5. test whether a nonzero \(E\) can remain vorticity-work orthogonal while also maintaining the dual-lock increment covariance;
6. if \(E:B_\omega=0\), attack the resulting pressure/cofactor compatibility with X72;
7. if \(E:B_\omega\neq0\), route to the old \(N\) branch;
8. if the covariance plane/packet changes, route to \(T/R_{\rm state}\).

Desired endpoint:

\[
\boxed{
\mathsf C_{\rm dual}
\Longrightarrow
\mathsf X
\vee
\mathsf N
\vee
\mathsf T
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP97 / X72-R80.
