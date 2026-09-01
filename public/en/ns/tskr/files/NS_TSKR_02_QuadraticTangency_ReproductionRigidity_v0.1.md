---
title: "Navier–Stokes Tangent Singular Kernel Rigidity Program 02: Quadratic Source Tangency, Velocity Reproduction Rigidity, Flux/Energy Response, Sign Fibers and Coarse-Graining Fixed-Point Classification"
short_title: "NS-TSKR 02"
series: "Navier–Stokes Tangent Singular Kernel Rigidity Program"
cycle: "X"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "Quadratic tangent rigidity / canonical covariance reproduction / fixed-point classification"
epistemic_status: "Uses the actual quadratic source geometry F_act=eta u tensor u and F_mod=eta(U tensor U+R), together with Reynolds covariance positivity, instead of arbitrary source tensors. Proves a pointwise Rank-One Attenuation Rigidity theorem: exact tangent equality u tensor u=U tensor U+R with R positive semidefinite forces U=theta u, |theta|<=1, and R=(1-theta^2)u tensor u. Under incompressibility of u and U, theta is constant along u-streamlines, and the exact coarse flux reduces to -(1-theta^2)theta u dot grad(|u|^2/2); hence flux invisibility alone does not force R=0. Provides an isotropic-covariance flux-zero no-go. Proves the canonical Reynolds variance identities tr R=S_l(|u|^2)-|S_l u|^2=S_l(|u-S_l u|^2) and the double-increment covariance formula. Therefore zero canonical covariance yields exact local velocity reproduction on the mollifier support. On the exact tangent positive-covariance branch, energy invisibility forces R=0 and reduces U to the pointwise sign fiber U=plus-or-minus u; in the canonical coarse-grained realization the variance identity removes the minus fiber and gives U=u locally. Proves a sign-fiber no-go showing that quadratic source equality alone cannot determine velocity reproduction for general divergence-free measurable fields. Identifies the canonical sharp-package covariance mismatch with u tensor u-S_l(u tensor u) in the exact coarse-grained model and proves global coarse-graining fixed-point rigidity: for a nondegenerate probability mollifier, an L^p whole-space tensor fixed by one convolution scale is zero, while on the torus it is constant. For smooth connected periodic velocity this reduces u tensor u constant to a global sign branch, and zero mean gives u=0. Proves an L^2 high-frequency spectral-gap theorem: approximate quadratic tangency forces the quadratic source into low frequencies. Consequently the actual positive-covariance tangent branch is largely closed to exact/near reproduction; the remaining TRSK obstruction must use localized approximate fixed points, low-frequency/harmonic leakage, sign-changing linearized stress, reproduction-transition residuals, adjoint-certificate mismatch, or amplitude summability. No complete TRSK exclusion, Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Tangent Singular Kernel Rigidity Program 02

# Quadratic Source Tangency, Velocity Reproduction Rigidity, Flux/Energy Response, Sign Fibers and Coarse-Graining Fixed-Point Classification

## 0. Positioning of this Paper

TSKR-01 reduced the surviving tangent singular obstruction to:

$$
\boxed{
\textbf{TRSK}.
}
$$

The present paper now imposes the actual quadratic geometry:

$$
F^{act}
=
\eta u\otimes u,
$$

$$
F^{mod}
=
\eta(U\otimes U+R),
$$

with:

$$
R\ge0
$$

on canonical NS-realizable coarse-grained packages.

---

# 1. External sharp-package covariance mismatch

The finite-window sharp package uses:

$$
F^{act}_{ij}
=
\eta u_i u_j,
$$

$$
F^{mod}_{ij}
=
\eta(U_iU_j+R_{ij}),
$$

and:

$$
\boxed{
\mathcal C^0
=
\eta
\left(
u\otimes u-U\otimes U-R
\right).
}
$$

An additional source residual coordinate is kept separate.

### Status

$$
\boxed{
\mathrm{EXTERNAL/DEFINITION}.
}
$$

---

# 2. Canonical coarse-grained source identity

For a nonnegative normalized mollifier:

$$
S_\ell,
$$

define:

$$
U=S_\ell u.
$$

The canonical Reynolds covariance is:

$$
R
=
S_\ell(u\otimes u)-U\otimes U.
$$

Hence:

$$
\boxed{
U\otimes U+R
=
S_\ell(u\otimes u).
}
$$

Moreover:

$$
\boxed{
R\ge0.
}
$$

### Status

$$
\boxed{
\mathrm{EXTERNAL/EXACT}.
}
$$

---

# 3. Canonical source tangency

Inside an interior region where:

$$
\eta=1,
$$

the sharp covariance mismatch becomes:

$$
\boxed{
\mathcal C^0
=
u\otimes u
-
S_\ell(u\otimes u).
}
$$

Thus canonical source tangency is a quadratic coarse-graining fixed-point condition.

It is not equivalent to:

$$
R\approx0.
$$

---

# 4. Pointwise exact tangent geometry

Assume:

$$
u,U\in\mathbb R^3,
$$

$$
R=R^\top\ge0,
$$

and:

$$
\boxed{
u\otimes u
=
U\otimes U+R.
}
$$

---

# 5. CIV/X-2.1 — Rank-One Attenuation Rigidity

## Theorem 5.1

Either:

$$
u=U=0,
\qquad
R=0,
$$

or there exists:

$$
\theta\in[-1,1]
$$

such that:

$$
\boxed{
U=\theta u,
}
$$

and:

$$
\boxed{
R
=
(1-\theta^2)
u\otimes u.
}
$$

### Proof

Suppose:

$$
u\neq0.
$$

For every:

$$
x\perp u,
$$

$$
0
\le
x^\top Rx
=
-
(U\cdot x)^2.
$$

Hence:

$$
U\cdot x=0
$$

for all:

$$
x\perp u.
$$

Thus:

$$
U=\theta u.
$$

Substitution yields:

$$
R=(1-\theta^2)u\otimes u.
$$

Since:

$$
R\ge0,
$$

$$
|\theta|\le1.
$$

If:

$$
u=0,
$$

then:

$$
-U\otimes U=R\ge0,
$$

so:

$$
U=0,
\quad
R=0.
$$

$\square$

---

# 6. Approximate tangent geometry

Assume:

$$
\|
u\otimes u-U\otimes U-R
\|_{\rm op}
\le
\varepsilon,
\qquad
R\ge0.
$$

Let:

$$
u\neq0.
$$

---

# 7. CIV/X-2.2 — Approximate Rank-One Alignment

## Theorem 7.1

$$
\boxed{
|P_{u^\perp}U|
\le
\varepsilon^{1/2}.
}
$$

Also:

$$
\boxed{
|U|^2
\le
|u|^2+\varepsilon.
}
$$

If:

$$
|u|\ge m>0,
$$

and:

$$
\theta
=
\frac{U\cdot u}{|u|^2},
$$

then:

$$
\boxed{
|U-\theta u|
\le
\varepsilon^{1/2},
}
$$

and:

$$
\boxed{
\theta^2
\le
1+
C\frac{\varepsilon}{m^2}.
}
$$

### Proof

For unit:

$$
x\perp u,
$$

the matrix:

$$
u\otimes u-U\otimes U
=
R+E,
\qquad
\|E\|_{\rm op}\le\varepsilon.
$$

Thus:

$$
-(U\cdot x)^2
\ge
-\varepsilon.
$$

The remaining estimates follow by orthogonal decomposition and testing in the direction of:

$$
U.
$$

$\square$

---

# 8. Divergence-free attenuation fiber

Assume smooth:

$$
U=\theta u,
$$

and:

$$
\nabla\cdot u
=
\nabla\cdot U
=
0.
$$

Then:

$$
\boxed{
u\cdot\nabla\theta=0.
}
$$

So:

$$
\theta
$$

is constant along active streamlines.

---

# 9. CIV/X-2.3 — Tangent Flux Formula

The canonical coarse energy flux is:

$$
\Pi
=
-R:\nabla U.
$$

Using:

$$
R=(1-\theta^2)u\otimes u
$$

and:

$$
u\cdot\nabla\theta=0,
$$

one gets:

$$
\boxed{
\Pi
=
-(1-\theta^2)\theta
u\cdot\nabla
\left(
\frac{|u|^2}{2}
\right).
}
$$

Therefore:

$$
\Pi=0
$$

at a nonzero point implies at least one of:

$$
\theta=0,
$$

$$
|\theta|=1,
$$

or:

$$
u\cdot\nabla|u|^2=0.
$$

---

# 10. Flux-only no-go

For trace-free incompressible strain:

$$
S,
$$

take:

$$
R=\kappa I,
\qquad
\kappa>0.
$$

Then:

$$
R:S
=
\kappa\operatorname{tr}S
=
0.
$$

Thus:

$$
\boxed{
\Pi=0
}
$$

with:

$$
R\neq0.
$$

---

# 11. CIV/X-2.4 — Flux-Zero Covariance No-Go

There is no universal implication:

$$
\boxed{
R\ge0,
\qquad
R:S=0
\Longrightarrow
R=0
}
$$

for trace-free strain.

Thus flux alone cannot remove positive covariance.

---

# 12. Flux-zero cone

Let:

$$
S e_i=\lambda_i e_i,
$$

$$
\lambda_1+\lambda_2+\lambda_3=0.
$$

Define:

$$
r_i=e_i^\top Re_i\ge0.
$$

Then:

$$
\boxed{
R:S
=
\lambda_1r_1+\lambda_2r_2+\lambda_3r_3.
}
$$

Positive and negative strain eigendirections can balance nonzero positive covariance into zero flux.

---

# 13. Canonical variance identity

For:

$$
U=S_\ell u,
$$

$$
R=S_\ell(u\otimes u)-U\otimes U,
$$

one has:

$$
\boxed{
\operatorname{tr}R
=
S_\ell(|u|^2)-|U|^2
=
S_\ell
\left(
|u-U|^2
\right).
}
$$

Here:

$$
U=U(x,t)
$$

is held fixed inside the averaging integral.

---

# 14. Double-increment covariance identity

If:

$$
d\mu
$$

is the translated mollifier probability measure at the observation point, then:

$$
\boxed{
R
=
\frac12
\iint
(u(z)-u(z'))
\otimes
(u(z)-u(z'))
\,d\mu(z)d\mu(z').
}
$$

Therefore Reynolds covariance is exactly a local second-order increment covariance.

---

# 15. CIV/X-2.5 — Zero-Covariance Velocity Reproduction

If:

$$
R(x,t)=0,
$$

then:

$$
\boxed{
u(z)=U(x,t)
}
$$

for mollifier-almost every:

$$
z
$$

in the averaging support.

### Proof

Since:

$$
R\ge0,
$$

$$
R=0
$$

implies:

$$
\operatorname{tr}R=0.
$$

The variance identity gives:

$$
S_\ell(|u-U|^2)=0.
$$

The integrand and kernel are nonnegative.

$\square$

---

# 16. Positive-energy interface

The external positive-energy observation separates:

- resolved selected-time velocity energy;
- resolved dissipation;
- nonnegative covariance trace.

On the positive NS-realizable pressure--flux cone:

$$
R\neq0
$$

is energy-visible under the stated energy-separation hypotheses.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED\ UNDER\ HYPOTHESES}.
}
$$

---

# 17. CIV/X-2.6 — Energy-Rigid Tangent Fiber

Assume exact tangent geometry and that the positive energy channel forces:

$$
\operatorname{tr}R=0.
$$

Then:

$$
\boxed{
R=0,
}
$$

$$
\boxed{
|\theta|=1,
}
$$

and hence:

$$
\boxed{
U=\pm u.
}
$$

If:

$$
U=S_\ell u
$$

and:

$$
R=S_\ell(u\otimes u)-U\otimes U,
$$

then Theorem 15 gives:

$$
\boxed{
U=u
}
$$

on the averaging support.

---

# 18. Quadratic sign fiber

The map:

$$
q(v)=v\otimes v
$$

satisfies:

$$
q(v)=q(-v).
$$

Therefore:

$$
u\otimes u
=
U\otimes U
$$

implies only:

$$
\boxed{
U=\pm u
}
$$

pointwise.

---

# 19. CIV/X-2.7 — Quadratic Source Does Not Determine Velocity

Let:

$$
u(x,y,z)=a(y)e_1,
$$

and:

$$
U(x,y,z)=\sigma(y)a(y)e_1,
$$

where:

$$
\sigma(y)\in\{-1,1\}.
$$

Then distributionally:

$$
\nabla\cdot u
=
\nabla\cdot U
=
0,
$$

and:

$$
\boxed{
u\otimes u
=
U\otimes U.
}
$$

But:

$$
U
$$

need not equal:

$$
u.
$$

Thus quadratic source equality plus divergence-free does not universally imply velocity reproduction.

---

# 20. CIV/X-2.8 — Continuous Sign Rigidity

Let:

$$
\Omega
$$

be connected.

Assume:

$$
u,U
$$

are continuous,

$$
|u|>0
$$

on:

$$
\Omega,
$$

and:

$$
u\otimes u
=
U\otimes U.
$$

Then there is one constant:

$$
\sigma\in\{-1,1\}
$$

such that:

$$
\boxed{
U=\sigma u
}
$$

throughout:

$$
\Omega.
$$

If:

$$
U(x_0)=u(x_0)
$$

at one point, then:

$$
\boxed{
U=u
}
$$

on:

$$
\Omega.
$$

---

# 21. Canonical quadratic fixed point

Let:

$$
f=u\otimes u.
$$

Since:

$$
U\otimes U+R
=
S_\ell f,
$$

exact canonical covariance tangency:

$$
\mathcal C^0=0
$$

means:

$$
\boxed{
f=S_\ell f.
}
$$

---

# 22. Nondegenerate probability mollifier

Let:

$$
\rho\ge0
$$

be a smooth probability kernel whose support contains a nonempty open set.

Then:

$$
\boxed{
|\widehat\rho(\xi)|<1
\qquad
(\xi\neq0).
}
$$

---

# 23. CIV/X-2.9 — Whole-Space Quadratic Fixed-Point Rigidity

Let:

$$
1\le p<\infty,
$$

and:

$$
f\in L^p(\mathbb R^d).
$$

If:

$$
\boxed{
f=\rho_\ell*f,
}
$$

then:

$$
\boxed{
f=0.
}
$$

Consequently:

$$
u\otimes u
=
S_\ell(u\otimes u)
$$

globally with:

$$
u\otimes u\in L^p
$$

implies:

$$
\boxed{
u=0.
}
$$

### Proof

In tempered distributions:

$$
(1-\widehat\rho(\ell\xi))
\widehat f(\xi)=0.
$$

The multiplier is nonzero away from:

$$
\xi=0.
$$

Thus:

$$
\supp\widehat f
\subset
\{0\}.
$$

A tempered distribution with Fourier support at one point is a polynomial.

No nonzero polynomial belongs to finite:

$$
L^p.
$$

$\square$

---

# 24. Periodic fixed-point classification

On:

$$
\mathbb T^d,
$$

assume:

$$
\widehat\rho(\ell k)\neq1
$$

for every nonzero:

$$
k\in\mathbb Z^d.
$$

Then:

$$
f=S_\ell f
$$

implies:

$$
\boxed{
f
\text{ is constant}.
}
$$

---

# 25. CIV/X-2.10 — Smooth Periodic Quadratic Fixed-Point Classification

Let:

$$
u
$$

be continuous on connected:

$$
\mathbb T^d
$$

and:

$$
u\otimes u
=
S_\ell(u\otimes u).
$$

Then:

$$
u\otimes u
$$

is constant.

If it is nonzero, there is a constant vector:

$$
v
$$

with:

$$
u(x)=\pm v.
$$

Continuity forces one global sign, so:

$$
u
$$

is constant.

If:

$$
\int_{\mathbb T^d}u\,dx=0,
$$

then:

$$
\boxed{
u=0.
}
$$

---

# 26. Approximate fixed-point spectral gap

Let:

$$
f\in L^2,
$$

and let:

$$
P_{\ge\kappa/\ell}
$$

project to:

$$
|\xi|\ge\kappa/\ell.
$$

Set:

$$
q_\kappa
=
\sup_{|\eta|\ge\kappa}
|\widehat\rho(\eta)|.
$$

Then:

$$
q_\kappa<1.
$$

---

# 27. CIV/X-2.11 — High-Frequency Tangency Rigidity

$$
\boxed{
\|
P_{\ge\kappa/\ell}
f
\|_2
\le
\frac{1}{1-q_\kappa}
\|
f-S_\ell f
\|_2.
}
$$

Thus small coarse-graining mismatch forces the quadratic source into relative low frequencies.

---

# 28. L2 topology safety

The high-frequency theorem is an:

$$
L^2
$$

spectral statement.

The natural suitable-weak sharp source coordinate is typically:

$$
L^{3/2}.
$$

Therefore the theorem applies directly only on smooth/reduced finite-window sectors or after an explicit topology-transfer estimate.

No such universal transfer is claimed here.

---

# 29. Source reproduction

The external sharp-package reproduction estimate gives:

$$
\boxed{
\operatorname{Rep}_{F^{act}}
\le
C_\eta M_U
\operatorname{Rep}_{u}
+
C
\operatorname{Leak}_{rep}^{F}.
}
$$

Velocity reproduction controls source reproduction.

The converse is false without sign/phase information, as Theorem 19 shows.

---

# 30. Tangent fixed-point classes

### TFP-0

Whole-space finite:

$$
L^p
$$

exact canonical fixed point:

$$
u=0.
$$

### TFP-C

Smooth periodic exact fixed point:

$$
u
$$

constant.

### TFP-R

Exact positive covariance attenuation:

$$
U=\theta u,
\qquad
R=(1-\theta^2)u\otimes u.
$$

Energy invisibility gives:

$$
R=0,
\qquad
U=\pm u.
$$

Canonical covariance gives:

$$
U=u.
$$

### TFP-L

Localized approximate low-frequency/harmonic tangent fixed point.

### TFP-S

Sign/nodal fiber not removed by quadratic source alone.

---

# 31. Positive canonical tangent closure

## Theorem 31.1

Assume a canonical coarse-grained finite-window branch satisfies:

1.:
   $$
   u\otimes u
   =
   U\otimes U+R;
   $$

2.:
   $$
   R\ge0;
   $$

3. the external positive energy channel separates:
   $$
   \operatorname{tr}R;
   $$

4. the branch is energy-invisible.

Then:

$$
\boxed{
R=0.
}
$$

If:

$$
U=S_\ell u,
$$

and:

$$
R=S_\ell(u\otimes u)-U\otimes U,
$$

then:

$$
\boxed{
u=U
}
$$

mollifier-a.e. on the averaging support.

Thus this branch is exact local reproduction rather than a nontrivial positive tangent covariance defect.

---

# 32. TRSK update

A surviving TRSK must therefore exploit at least one of:

$$
\boxed{
\text{LOCALIZED APPROXIMATE FIXED POINT},
}
$$

$$
\boxed{
\text{LOW-FREQUENCY/HARMONIC LEAKAGE},
}
$$

$$
\boxed{
\text{SIGN/NODAL REPRODUCTION FIBER},
}
$$

$$
\boxed{
\text{SIGN-CHANGING LINEARIZED STRESS},
}
$$

$$
\boxed{
\text{ASC FAILURE},
}
$$

or:

$$
\boxed{
\text{AMPLITUDE SUMMABILITY}.
}
$$

---

# 33. Next paper

The next paper should attack the residual fibers:

$$
\boxed{
\textbf{
NS-TSKR 03 —
Localized Quadratic Fixed Points,
Nodal Sign Rigidity,
Low-Frequency/Harmonic Tangency,
Linearized Stress Kernels
and Residual Fixed-Orbit Classification
}.
}
$$

Primary tasks:

1. localize the fixed-point theorem with explicit boundary/harmonic leakage;
2. classify low-frequency approximate:
   $$
   u\otimes u\approx S_\ell(u\otimes u);
   $$
3. determine whether selected trace/reproduction kills the sign/nodal fiber;
4. classify linearized tangent directions to:
   $$
   u\otimes u-U\otimes U-R=0;
   $$
5. intersect sign-changing stress directions with pressure, flux, energy, LEI, model-cone, and increment kernels;
6. test whether TRSK collapses to a renormalized reproduction fixed orbit;
7. search for an amplitude tax on that fixed orbit.

---

# 34. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Rank-One Attenuation Rigidity}
&:\ \mathrm{PROVED},\\
\text{Approximate Rank-One Alignment}
&:\ \mathrm{PROVED},\\
\text{Tangent Flux Formula}
&:\ \mathrm{PROVED},\\
\text{Flux-Zero Covariance exclusion}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{Canonical Variance Identity}
&:\ \mathrm{PROVED},\\
\text{Zero-Covariance Velocity Reproduction}
&:\ \mathrm{PROVED},\\
\text{Energy-Rigid Tangent Fiber}
&:\ \mathrm{PROVED\ WITH\ EXTERNAL\ ENERGY\ SEPARATION},\\
\text{Quadratic-source-to-velocity uniqueness}
&:\ \mathrm{NO\mbox{-}GO\ WITHOUT\ TRACE/REGULARITY},\\
\text{Continuous Sign Rigidity}
&:\ \mathrm{PROVED},\\
\text{Whole-Space Quadratic Fixed-Point Rigidity}
&:\ \mathrm{PROVED},\\
\text{Periodic Quadratic Fixed-Point Classification}
&:\ \mathrm{PROVED},\\
\text{High-Frequency Tangency Rigidity}
&:\ \mathrm{PROVED},\\
\text{localized approximate tangent fixed-point exclusion}
&:\ \mathrm{OPEN},\\
\text{sign-changing linearized kernel exclusion}
&:\ \mathrm{OPEN},\\
ASC
&:\ \mathrm{OPEN},\\
\text{physical amplitude Critical Lift}
&:\ \mathrm{OPEN},\\
\text{TRSK exclusion}
&:\ \mathrm{OPEN/PARTIAL},\\
\text{Forest Coercive Budget}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 35. Conclusion

Exact tangency:

$$
u\otimes u
=
U\otimes U+R,
\qquad
R\ge0,
$$

forces:

$$
U=\theta u,
\qquad
R=(1-\theta^2)u\otimes u.
$$

Thus the model velocity cannot rotate relative to the active velocity.

Incompressibility makes:

$$
\theta
$$

constant along streamlines.

Flux invisibility alone cannot kill positive covariance.

The energy channel is essential.

For canonical Reynolds covariance:

$$
R
=
S_\ell(u\otimes u)
-
S_\ell u\otimes S_\ell u,
$$

the covariance trace is exactly local velocity variance.

Zero covariance means exact local reproduction.

Hence a positive-covariance canonical tangent branch which is also energy-invisible collapses to:

$$
u=U.
$$

The sharp covariance mismatch also becomes a coarse-graining fixed-point equation:

$$
u\otimes u
=
S_\ell(u\otimes u).
$$

Whole-space finite-$L^p$ exact fixed points vanish.

Periodic smooth fixed points are constant.

Approximate tangency cannot hide arbitrary high-frequency quadratic source.

The remaining obstruction is therefore localized, low-frequency, sign/nodal, sign-changing-linearized, adjoint, or amplitude based.

That is the target of TSKR-03.

---

# References

1. R. Yu, *Finite-Window Local-to-Clean Transfer and Anti-Phantom Detection for Sharp Navier--Stokes Packages*, arXiv:2606.18476.
2. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
3. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
4. `NS_TSKR_01_TangentSource_SingularKernel_v0.1.md`.
5. `NS_IDRP_CYCLE_IX_HANDOFF_v1.0.md`.