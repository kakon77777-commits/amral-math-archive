# DCRP51 — Central Wave–Pseudo-Eikonal Rigidity, Logistic Amplitude Window, and the Null-Hessian Survivor Cone

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / central perfect-response realizability round  
**Immediate predecessor:** `NS_DCRP50_CentralResponse_AffineNoGo_WaveEikonal_2026-08-17.md`

**Primary internal dependencies**
- DCRP-41 — fixed-plane zero-shape canonical pancake tensor
- DCRP-44 — unique periodic gauge-flat scalar eigenmode
- DCRP-49 — central response reduction
- DCRP-50 — three-component pressure-response defect and exact-affine central NO-GO
- X72 Round43 — full-wave-cone / vorticity-realizability frontier

**External calibration**
- Frittelli–Newman–Silva-Ortigoza, *The Eikonal Equation in Flat Space: Null Surfaces and Their Singularities I*, arXiv:gr-qc/9809019. Flat-space eikonal equations possess rich nonlinear characteristic geometry, so eikonal structure alone must not be confused with affine rigidity.
- Agafontsev–Kuznetsov–Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782. Exact pancake-like Euler geometry remains an important local realizability calibration.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP50 reduced the maximally rigid central perfect-pressure-response branch to

$$
\boxed{
q_{zz}=\Delta_h q,
}
$$

and

$$
\boxed{
|\nabla_hq|^2
-\frac32(q_z-4a)^2
=
12(a'+a-2a^2).
}
$$

The first question of DCRP51 was whether this simultaneous wave–pseudo-eikonal system forces $q$ to be affine.

The correct answer is:

$$
\boxed{
\textbf{not unconditionally.}
}
$$

However it has a strong sign-dependent rigidity.

Define the shifted scalar

$$
\boxed{
u(y,s)
=
q(y,s)-4a(s)z.
}
$$

At every fixed similarity time $s$,

$$
\boxed{
u_{zz}=\Delta_hu,
}
$$

and

$$
\boxed{
|\nabla_hu|^2
-\frac32u_z^2
=
C(s),
}
$$

where

$$
\boxed{
C(s)
=
12M_a(s),
\qquad
M_a(s)
=
a'(s)+a(s)-2a(s)^2.
}
$$

The main spatial rigidity theorem is:

> If $C(s)\le0$ on a connected spatial perfect-response patch, then $u(\cdot,s)$ is spatially affine.

The proof uses a Lorentzian Bochner identity and an exact Hessian factorization.

Combining this with the final DCRP41 fixed-plane zero-shape equality geometry and DCRP50's exact-affine central NO-GO yields:

> On a persistent nonzero central perfect-response rank-two branch, $M_a(s)$ cannot be negative at any time.

Thus every such survivor must satisfy

$$
\boxed{
a'+a-2a^2\ge0
}
$$

for all $s$.

Periodicity then immediately forces the sharp pointwise amplitude window

$$
\boxed{
0\le a(s)\le\frac12.
}
$$

Together with DCRP41's exact period mean,

$$
\boxed{
\frac1{S_0}\int_0^{S_0}a(s)\,ds
=
\frac{2-3\gamma}{2}
\in
\left(
\frac14,\frac25
\right),
}
$$

the central perfect-response pancake amplitude is confined to a compact logistic strip.

The positive-$C$ branch is also highly constrained.

At every point where the spatial Hessian is genuinely nonzero,

$$
D_y^2u\neq0,
$$

one necessarily has

$$
\boxed{
|\nabla_hu|
\ge
\frac32|u_z|,
}
$$

and the Hessian has rank exactly one:

$$
\boxed{
D_y^2u
=
\kappa\,\ell\otimes\ell,
}
$$

where $\ell$ is null for the $2+1$ wave metric

$$
G=\operatorname{diag}(1,1,-1),
$$

and is orthogonal to the pseudo-eikonal normal:

$$
\boxed{
\ell^\top
\operatorname{diag}
\left(
1,1,-\frac32
\right)
\nabla u
=
0.
}
$$

Hence every genuinely nonlinear perfect-response central solution is forced onto a **rank-one null-Hessian wave cone**.

This is the main new survivor classification:

$$
\boxed{
\text{central perfect response}
\Rightarrow
\text{affine contradiction}
\ \vee\
\text{positive logistic amplitude}
+
\text{rank-one null-Hessian characteristic geometry}.
}
$$

The next step should pass this null-Hessian survivor cone directly into the X72 realizability machinery.

---

# 1. Central perfect-response equations

DCRP50 gives, on the fully central branch

$$
c=B_q=\frac12,
$$

the spatial relation

$$
\boxed{
q_{zz}=\Delta_hq.
}
\tag{1.1}
$$

If the remaining three-component X72 affine pressure-response defect also vanishes,

$$
E_p=0,
$$

then the normal defect equation becomes

$$
\boxed{
|\nabla_hq|^2
-
\frac32(q_z-4a)^2
=
12(a'+a-2a^2).
}
\tag{1.2}
$$

All functions $a=a(s)$ depend only on similarity time.

---

# 2. Remove the vertical affine offset

Define

$$
\boxed{
u(y,s)
=
q(y,s)-4a(s)z.
}
\tag{2.1}
$$

Since $a$ is spatially constant,

$$
u_{zz}=q_{zz},
$$

and

$$
\Delta_hu=\Delta_hq.
$$

Therefore

$$
\boxed{
u_{zz}=\Delta_hu.
}
\tag{2.2}
$$

Also

$$
u_z=q_z-4a,
$$

and

$$
\nabla_hu=\nabla_hq.
$$

Thus (1.2) becomes

$$
\boxed{
|\nabla_hu|^2
-
\beta u_z^2
=
C(s),
}
\tag{2.3}
$$

where for later clarity

$$
\boxed{
\beta=\frac32,
}
\tag{2.4}
$$

and

$$
\boxed{
C(s)
=
12M_a(s),
}
\tag{2.5}
$$

$$
\boxed{
M_a
=
a'+a-2a^2.
}
\tag{2.6}
$$

At each fixed $s$, $C(s)$ is a spatial constant.

---

# 3. Matrix notation

Let

$$
x=(x_1,x_2,z).
$$

Define the wave metric matrix

$$
\boxed{
G
=
\operatorname{diag}(1,1,-1),
}
\tag{3.1}
$$

and the pseudo-eikonal matrix

$$
\boxed{
M
=
\operatorname{diag}(1,1,-\beta).
}
\tag{3.2}
$$

Let

$$
g=\nabla u,
$$

and

$$
H=D^2u.
$$

Then the system is

$$
\boxed{
\operatorname{tr}(GH)=0,
}
\tag{3.3}
$$

and

$$
\boxed{
g^\top Mg=C.
}
\tag{3.4}
$$

Differentiate (3.4):

$$
\boxed{
HMg=0.
}
\tag{3.5}
$$

So the pseudo-eikonal normal $Mg$ lies in the kernel of the Hessian.

---

# 4. Lorentzian Bochner identity

Apply the wave operator

$$
L_G
=
\partial_1^2+\partial_2^2-\partial_z^2
$$

to the constant pseudo-eikonal norm

$$
g^\top Mg.
$$

Since

$$
L_Gu=0,
$$

we also have

$$
L_Gu_i=0
$$

for every first derivative.

Therefore

$$
\boxed{
0
=
\frac12
L_G(g^\top Mg)
=
\operatorname{tr}
\left(
GHMH
\right).
}
\tag{4.1}
$$

This is the key second-order identity.

It is the indefinite analogue of the usual Euclidean Bochner calculation for harmonic functions with constant gradient norm.

---

# 5. Adapted pointwise coordinates

At a noncritical point rotate only the horizontal coordinates so that

$$
\boxed{
\nabla_hu=(\rho,0),
\qquad
u_z=r.
}
\tag{5.1}
$$

Thus

$$
g=(\rho,0,r).
$$

Assume first

$$
\rho>0.
$$

Define

$$
\boxed{
t
=
\frac{\beta r}{\rho}.
}
\tag{5.2}
$$

Write the symmetric Hessian as

$$
H=
\begin{pmatrix}
A&B&C_1\\
B&D&E\\
C_1&E&F
\end{pmatrix}.
$$

The differentiated eikonal identity

$$
HMg=0
$$

and wave trace

$$
A+D-F=0
$$

give

$$
\boxed{
A=t^2F,
}
\tag{5.3}
$$

$$
\boxed{
B=tE,
}
\tag{5.4}
$$

$$
\boxed{
C_1=tF,
}
\tag{5.5}
$$

$$
\boxed{
D=(1-t^2)F.
}
\tag{5.6}
$$

Hence

$$
\boxed{
H
=
\begin{pmatrix}
t^2F&tE&tF\\
tE&(1-t^2)F&E\\
tF&E&F
\end{pmatrix}.
}
\tag{5.7}
$$

---

# 6. Exact Bochner factorization

Substitute (5.7) into (4.1).

A direct calculation gives, for general $\beta$,

$$
\boxed{
0
=
\left[
E^2+F^2(t^2-1)
\right]
\left[
2t^2-(\beta+1)
\right].
}
\tag{6.1}
$$

For

$$
\beta=\frac32,
$$

this is

$$
\boxed{
0
=
\left[
E^2+F^2(t^2-1)
\right]
\left[
2t^2-\frac52
\right].
}
\tag{6.2}
$$

This factorization is independently checked in the accompanying symbolic verification script.

---

# 7. Timelike pseudo-eikonal rigidity

Suppose

$$
\boxed{
C<0.
}
\tag{7.1}
$$

Then

$$
\rho^2-\beta r^2<0.
$$

Hence

$$
\beta r^2>\rho^2.
$$

If $\rho>0$,

$$
t^2
=
\frac{\beta^2r^2}{\rho^2}
>
\beta
=
\frac32.
$$

Therefore

$$
t^2>1
$$

and

$$
2t^2-\frac52>0.
$$

The first factor in (6.2) is then nonnegative and vanishes only if

$$
E=F=0.
$$

Thus

$$
H=0.
$$

---

# 8. The case $\rho=0$

If

$$
C<0
$$

and

$$
\rho=0,
$$

then

$$
r\neq0.
$$

Equation

$$
HMg=0
$$

forces the entire third Hessian column to vanish.

Thus

$$
H=
\begin{pmatrix}
A&B&0\\
B&D&0\\
0&0&0
\end{pmatrix}.
$$

The wave trace gives

$$
A+D=0.
$$

The Bochner identity then becomes

$$
\boxed{
0=2(A^2+B^2),
}
$$

hence

$$
A=B=D=0.
$$

So again

$$
\boxed{
H=0.
}
$$

---

# Theorem D51.1 — Negative Pseudo-Eikonal Affine Rigidity

Let $u\in C^3(\Omega)$ on a connected spatial domain satisfy

$$
u_{zz}=\Delta_hu,
$$

and

$$
|\nabla_hu|^2-\frac32u_z^2=C
$$

with a spatial constant

$$
C<0.
$$

Then

$$
\boxed{
D^2u=0
}
$$

throughout $\Omega$.

Therefore

$$
\boxed{
u
\text{ is affine in }(y_h,z).
}
$$

---

# 9. Null pseudo-eikonal rigidity

Now suppose

$$
\boxed{
C=0.
}
\tag{9.1}
$$

At every noncritical point,

$$
\rho^2=\beta r^2,
$$

hence

$$
\boxed{
t^2=\beta=\frac32.
}
\tag{9.2}
$$

Exactly as in the negative case,

$$
t^2>1,
$$

and both factors in (6.2) force

$$
H=0.
$$

If $\nabla u=0$ at a point, either:

1. the critical set has interior, in which case $u$ is locally constant there and $H=0$;
2. or it is approached by noncritical points, where $H=0$, and continuity gives $H=0$ at the critical point.

Thus:

## Theorem D51.2 — Null Pseudo-Eikonal Affine Rigidity

If

$$
C=0,
$$

then every $C^3$ solution of the simultaneous central wave–pseudo-eikonal system is spatially affine on each connected component.

---

# 10. Combined nonpositive rigidity

The previous two theorems give:

## Theorem D51.3 — Nonpositive Central Wave–Eikonal Rigidity

If

$$
\boxed{
C\le0,
}
$$

then

$$
\boxed{
u
\text{ is spatially affine}.
}
$$

In DCRP variables:

$$
\boxed{
M_a(s)
=
a'+a-2a^2
\le0
}
$$

at a fixed time forces the shifted central perfect-response scalar to be affine on every connected spatial perfect-response component.

For an open time interval on which

$$
M_a<0,
$$

this affine structure persists slice by slice.

---

# 11. Why an affine-$u$ interval is fatal on the final equality branch

Suppose an open time interval $I$ satisfies

$$
M_a(s)<0.
$$

By Theorem D51.1,

$$
u(y,s)
$$

and therefore $q(y,s)$ are spatially affine for every

$$
s\in I.
$$

Write

$$
\boxed{
q(y,s)
=
K(s)\cdot y_h
+
m(s)z
+
g(s).
}
\tag{11.1}
$$

Then

$$
\boxed{
\Omega_h=JK(s)
}
\tag{11.2}
$$

is spatially uniform.

Assume the active rank-two patch has

$$
K(s)\neq0
$$

on a subinterval.

---

# 12. Vorticity equation forces the planar strain to be spatially constant

On the central branch the symmetric cross block vanishes.

Write

$$
S=
\begin{pmatrix}
H(y_h,s)&0\\
0&d(s)
\end{pmatrix},
$$

where

$$
d=\frac12m-2a.
$$

Because $q$ is affine,

$$
D_h^2q=0,
$$

so

$$
\partial_zH
=
-\frac12D_h^2q
=
0.
$$

Thus $H$ depends at most on $y_h$ and $s$.

The similarity vorticity equation is

$$
\boxed{
D_s\Omega+\Omega
=
(\Omega\cdot\nabla)V.
}
\tag{12.1}
$$

Since $\Omega_h=JK(s)$ is spatially uniform,

$$
W\cdot\nabla\Omega_h=0.
$$

Also the vertical component of $(\Omega\cdot\nabla)V$ vanishes because

$$
\nabla_hw
=
\frac12K
$$

is orthogonal to

$$
\Omega_h=JK.
$$

Hence

$$
\boxed{
\Omega_h'(s)+\Omega_h(s)
=
H(y_h,s)\Omega_h(s).
}
\tag{12.2}
$$

The left side is independent of $y_h$.

Moreover incompressibility fixes

$$
\operatorname{tr}H=-d,
$$

also independent of $y_h$.

A symmetric $2\times2$ matrix is uniquely determined by:

1. its trace;
2. its action on one fixed nonzero vector.

Therefore

$$
\boxed{
H(y_h,s)
\text{ is spatially constant}.
}
\tag{12.3}
$$

Thus the entire strain tensor $S$ is pointwise affine/constant on the active patch.

---

# 13. DCRP41 equality then selects the canonical affine tensor

The final fixed-plane zero-shape equality branch of DCRP41 admits only the canonical affine strain tensor

$$
\boxed{
A_{\rm pan}
=
a(s)\operatorname{diag}(1,1,-2).
}
\tag{13.1}
$$

Since the actual strain has just been shown spatially constant, it coincides with its affine equality tensor.

Hence

$$
\boxed{
S=A_{\rm pan}
}
\tag{13.2}
$$

on the active patch.

DCRP50's exact-affine central NO-GO then implies

$$
\boxed{
\Omega_h=0.
}
\tag{13.3}
$$

Contradiction.

---

# Theorem D51.4 — Active Central Perfect-Response Sign Constraint

On a persistent nonzero rank-two central perfect-response branch satisfying the final fixed-plane zero-shape DCRP41 equality conditions,

$$
\boxed{
M_a(s)
=
a'(s)+a(s)-2a(s)^2
\ge0
}
\tag{13.4}
$$

for every similarity time $s$.

If $M_a<0$ at any time, continuity gives a negative open interval and the branch collapses by Theorems D51.1 and D50.4.

Thus:

$$
\boxed{
C(s)=12M_a(s)\ge0.
}
$$

The perfect-response central survivor is forced entirely into the spacelike pseudo-eikonal sector.

---

# 14. Logistic amplitude inequality

Theorem D51.4 is equivalent to

$$
\boxed{
a'
\ge
2a^2-a.
}
\tag{14.1}
$$

This is a pointwise logistic differential inequality.

Because $a$ is periodic, it has global minima and maxima.

Let

$$
a_{\min}
=
\min_sa(s).
$$

At a minimum,

$$
a'=0.
$$

If

$$
a_{\min}<0,
$$

then

$$
a_{\min}-2a_{\min}^2<0,
$$

contradicting

$$
M_a\ge0.
$$

Therefore

$$
\boxed{
a(s)\ge0.
}
\tag{14.2}
$$

Likewise let

$$
a_{\max}
=
\max_sa(s).
$$

If

$$
a_{\max}>\frac12,
$$

then

$$
a_{\max}-2a_{\max}^2<0,
$$

again contradicting

$$
M_a\ge0.
$$

Therefore

$$
\boxed{
a(s)\le\frac12.
}
\tag{14.3}
$$

---

# Theorem D51.5 — Central Perfect-Response Amplitude Window

Every persistent nonzero central perfect-response equality branch satisfies

$$
\boxed{
0\le a(s)\le\frac12
}
\tag{14.4}
$$

for all similarity times.

DCRP41 additionally fixes

$$
\boxed{
\bar a
=
\frac1{S_0}
\int_0^{S_0}a(s)\,ds
=
\frac{2-3\gamma}{2}.
}
\tag{14.5}
$$

Since

$$
\frac25<\gamma<\frac12,
$$

$$
\boxed{
\frac14<\bar a<\frac25.
}
\tag{14.6}
$$

So the entire canonical amplitude lies in the compact strip

$$
\boxed{
0\le a\le\frac12
}
$$

with a strictly interior positive period mean.

---

# 15. Variance bound

Integrating

$$
M_a=a'+a-2a^2\ge0
$$

over one period gives

$$
\boxed{
\overline{a^2}
\le
\frac{\bar a}{2}.
}
\tag{15.1}
$$

Therefore

$$
\operatorname{Var}(a)
=
\overline{a^2}-\bar a^2
\le
\bar a
\left(
\frac12-\bar a
\right).
$$

Substitute

$$
\bar a=\frac{2-3\gamma}{2}.
$$

Then

$$
\boxed{
\operatorname{Var}(a)
\le
\frac{
(2-3\gamma)(3\gamma-1)
}{4}.
}
\tag{15.2}
$$

This does not force $a$ to be constant, but it gives a uniform amplitude-oscillation ceiling on the perfect-response central branch.

---

# 16. Positive pseudo-eikonal sector

The only remaining nonlinear spatial branch therefore has

$$
\boxed{
C>0.
}
\tag{16.1}
$$

At a fixed spatial point write again

$$
\nabla_hu=(\rho,0),
$$

$$
u_z=r,
$$

and

$$
t=\frac{\beta r}{\rho}.
$$

Because

$$
C
=
\rho^2-\beta r^2
>0,
$$

we have

$$
\boxed{
t^2<\beta=\frac32.
}
\tag{16.2}
$$

The Bochner factorization remains

$$
0
=
\left[
E^2+F^2(t^2-1)
\right]
\left[
2t^2-\frac52
\right].
$$

---

# 17. The apparent resonant ratio cannot support a non-affine open branch

The second Bochner factor vanishes at

$$
\boxed{
t^2=\frac54.
}
\tag{17.1}
$$

At first sight this appears to be an exceptional unconstrained Hessian ratio.

It is not a genuine nonlinear open branch.

Suppose

$$
H(x_0)\neq0
$$

and

$$
t(x_0)^2=\frac54.
$$

By continuity, $H\neq0$ on a small neighborhood.

At every nearby point with

$$
t^2>1
$$

but

$$
t^2\neq\frac54,
$$

the first Bochner factor is strictly nonnegative and can vanish only with

$$
H=0,
$$

contradicting the chosen neighborhood.

Hence $t^2$ must equal $5/4$ throughout that neighborhood.

But then, since $C$ is spatially constant,

$$
\rho^2
=
\frac{
C
}{
1-\frac{t^2}{\beta}
}
=
6C,
$$

so

$$
|\nabla_hu|
$$

is constant.

Likewise

$$
|u_z|
$$

is constant, and its sign is locally fixed.

Thus $u_z$ is constant and

$$
u(y_h,z)=rz+f(y_h).
$$

The wave equation gives

$$
\Delta_hf=0,
$$

while

$$
|\nabla_hf|
$$

is constant.

The ordinary Euclidean Bochner identity gives

$$
D_h^2f=0.
$$

Hence

$$
H=0,
$$

again a contradiction.

Therefore:

## Lemma D51.6 — Resonant-Ratio Removal

A genuinely non-affine point cannot occur at

$$
t^2=\frac54.
$$

The apparent Bochner resonance is removable by local compatibility.

---

# 18. Non-affine points must be horizontally dominant

Let

$$
H\neq0.
$$

If

$$
t^2>1,
$$

then, except for the removable resonance $5/4$, the first factor in (6.2) is a sum of nonnegative terms and forces

$$
H=0.
$$

Therefore every genuinely non-affine point satisfies

$$
\boxed{
t^2\le1.
}
\tag{18.1}
$$

Since

$$
t
=
\frac{\beta u_z}{|\nabla_hu|},
$$

we obtain:

## Theorem D51.7 — Horizontal-Dominance Constraint

At every non-affine perfect-response central point,

$$
\boxed{
|\nabla_hu|
\ge
\beta|u_z|
=
\frac32|u_z|.
}
\tag{18.2}
$$

Equivalently,

$$
\boxed{
|u_z|
\le
\frac23|\nabla_hu|.
}
\tag{18.3}
$$

Thus genuine non-affinity can occur only in a strictly more horizontal sector than the mere spacelike condition

$$
|\nabla_hu|
>
\sqrt{\frac32}|u_z|.
$$

---

# 19. Rank-one Hessian factorization

At a non-affine point,

$$
t^2\le1,
$$

and the second Bochner factor is strictly nonzero:

$$
2t^2-\frac52<0.
$$

Therefore

$$
\boxed{
E^2
=
F^2(1-t^2).
}
\tag{19.1}
$$

Since $H\neq0$, we have $F\neq0$.

Choose

$$
\sigma\in\{+1,-1\}
$$

so that

$$
\boxed{
E
=
\sigma F\sqrt{1-t^2}.
}
\tag{19.2}
$$

Define

$$
\boxed{
\ell_\sigma
=
\left(
t,
\sigma\sqrt{1-t^2},
1
\right)
}
\tag{19.3}
$$

in the adapted horizontal frame.

Then (5.7) becomes

$$
\boxed{
H
=
F
\ell_\sigma\otimes\ell_\sigma.
}
\tag{19.4}
$$

Therefore:

$$
\boxed{
\operatorname{rank}H=1.
}
\tag{19.5}
$$

All $2\times2$ Hessian minors vanish.

---

# 20. The Hessian direction is wave-null

For the wave metric

$$
G=\operatorname{diag}(1,1,-1),
$$

$$
\ell_\sigma^\top G\ell_\sigma
=
t^2
+
(1-t^2)
-
1
=
0.
$$

Thus

$$
\boxed{
\ell_\sigma
\text{ is wave-null}.
}
\tag{20.1}
$$

Also

$$
M\nabla u
=
(\rho,0,-\beta r).
$$

Hence

$$
\ell_\sigma\cdot M\nabla u
=
t\rho-\beta r
=
0.
$$

Therefore

$$
\boxed{
\ell_\sigma
\perp
M\nabla u.
}
\tag{20.2}
$$

The Hessian bends only along a wave-null direction tangent to the pseudo-eikonal level geometry.

---

# 21. Coordinate-invariant null-Hessian theorem

Let

$$
\widehat p
=
\frac{\nabla_hu}{|\nabla_hu|},
$$

and let

$$
J\widehat p
$$

be its horizontal $90^\circ$ rotation.

Define

$$
\boxed{
t
=
\frac{
\beta u_z
}{
|\nabla_hu|
}.
}
\tag{21.1}
$$

At every genuinely non-affine point,

$$
|t|\le1.
$$

The two candidate null directions are

$$
\boxed{
\ell_\pm
=
t\widehat p
\pm
\sqrt{1-t^2}
J\widehat p
+
n.
}
\tag{21.2}
$$

Then:

## Theorem D51.8 — Null-Hessian Survivor Cone

At every point of a smooth central perfect-pressure-response solution where

$$
D^2u\neq0,
$$

there exists a sign $\sigma$ and scalar $\kappa\neq0$ such that

$$
\boxed{
D^2u
=
\kappa
\ell_\sigma\otimes\ell_\sigma,
}
\tag{21.3}
$$

with

$$
\boxed{
\ell_\sigma^\top G\ell_\sigma=0,
}
\tag{21.4}
$$

and

$$
\boxed{
\ell_\sigma^\top M\nabla u=0.
}
\tag{21.5}
$$

Thus every genuinely nonlinear spatial survivor is confined to a rank-one null-Hessian wave cone.

---

# 22. Quantitative gradient bounds on the nonlinear cone

At a non-affine point,

$$
|\nabla_hu|
\ge
\frac32|u_z|.
$$

Since

$$
C
=
|\nabla_hu|^2
-
\frac32u_z^2,
$$

we obtain

$$
C
\ge
\frac34u_z^2.
$$

Hence

$$
\boxed{
|u_z|^2
\le
\frac43C.
}
\tag{22.1}
$$

Also

$$
|\nabla_hu|^2
=
C+\frac32u_z^2
\le
3C.
$$

Thus

$$
\boxed{
C
\le
|\nabla_hu|^2
\le
3C.
}
\tag{22.2}
$$

So once $a(s)$ is fixed, the perfect-response nonlinear gradient magnitude lies in a finite pointwise corridor.

---

# 23. Interpretation as a developable characteristic geometry

Equation

$$
D^2u
=
\kappa\ell\otimes\ell
$$

means that the gradient map has differential of rank one.

Consequently all directions orthogonal to $\ell$ in the ordinary coordinate pairing lie in the kernel of $D^2u$.

The nonlinear variation of $\nabla u$ is concentrated on one wave-null characteristic direction.

This is a developable/characteristic geometry rather than a generic nonlinear three-dimensional Hessian.

DCRP51 does **not** claim that every such rank-one null-Hessian field globally integrates to a nontrivial smooth solution.

That is the next realizability problem.

---

# 24. Why unconditional affine rigidity is not claimed

The eikonal equation by itself has broad nonlinear characteristic solution families and can form caustics.

The simultaneous wave constraint removes most of that freedom, but DCRP51's local algebra leaves the rank-one null-Hessian cone as a genuine formal survivor.

Without a separate integrability theorem it would be incorrect to replace this surviving cone by an affine-rigidity claim.

Therefore the proved statement is exactly:

$$
\boxed{
C\le0
\Rightarrow
\text{affine},
}
$$

while

$$
\boxed{
C>0,\ D^2u\neq0
\Rightarrow
\text{rank-one null-Hessian cone}.
}
$$

No stronger global classification is asserted.

---

# 25. Connection to X72 Round43

X72 Round43 ended at a realizability gap:

$$
\boxed{
\text{generic continuous wave-cone admissibility}
\not\Rightarrow
\text{vorticity/NS realizability}.
}
$$

DCRP51 produces a much more specific candidate wave-cone object.

The nonlinear central perfect-response survivor satisfies:

$$
\boxed{
D^2u
=
\kappa\ell\otimes\ell,
}
$$

where

$$
\ell
$$

is wave-null and tied algebraically to the vorticity/shear gradient through

$$
\ell^\top M\nabla u=0.
$$

Thus the DCRP survivor is no longer a generic full-wave-cone tensor.

It lies on a constrained rank-one null cone coupled to the planar-vorticity scalar.

This is a natural input for the NTLA/X72 realizability-lift program.

---

# 26. New realizability tower for the central survivor

A first tower is:

### Level R0 — wave admissibility

$$
\boxed{
G:\ell\otimes\ell=0
}
$$

because $\ell$ is wave-null.

### Level R1 — rank-one Hessian realizability

$$
\boxed{
D^2u
=
\kappa\ell\otimes\ell.
}
$$

### Level R2 — pseudo-eikonal tangency

$$
\boxed{
\ell^\top M\nabla u=0.
}
$$

### Level R3 — central planar-vorticity reconstruction

$$
\boxed{
\Omega_h
=
J\nabla_hq
=
J\nabla_hu.
}
$$

### Level R4 — perfect X72 pressure response

$$
\boxed{
E_p=0.
}
$$

### Level R5 — same-parent DSS / finite supplier / PFET

The full DCRP31–50 constraints.

The next objective is to locate the first non-liftable level.

---

# 27. Updated final central survivor

After DCRP51, the maximally rigid central survivor obeys:

$$
\boxed{
\begin{gathered}
c=\frac12,
\\
E_p=0,
\\
0\le a(s)\le\frac12,
\\
a'+a-2a^2\ge0,
\\
\bar a=\frac{2-3\gamma}{2},
\\
u=q-4az,
\\
u_{zz}=\Delta_hu,
\\
|\nabla_hu|^2-\frac32u_z^2=12M_a,
\\
D^2u=0
\quad\text{or}\quad
D^2u=\kappa\ell\otimes\ell.
\end{gathered}
}
$$

The affine option is incompatible with a persistent active final equality branch whenever it occurs on an open time interval.

Therefore the genuine nonlinear survivor is the null-Hessian branch.

---

# 28. Status ledger

## PROVED this round

### D51-P1 — Shifted central wave–pseudo-eikonal system

$$
u_{zz}=\Delta_hu,
$$

$$
|\nabla_hu|^2-\frac32u_z^2=C(s).
$$

### D51-P2 — Lorentzian Bochner identity

$$
\operatorname{tr}(GHMH)=0.
$$

### D51-P3 — Exact pointwise Hessian factorization in adapted coordinates

$$
0=
\left[
E^2+F^2(t^2-1)
\right]
\left[
2t^2-\frac52
\right].
$$

### D51-P4 — Nonpositive affine rigidity

$$
C\le0
\Rightarrow
D^2u=0.
$$

### D51-P5 — Active survivor sign constraint

$$
a'+a-2a^2\ge0.
$$

### D51-P6 — Periodic logistic amplitude window

$$
0\le a\le\frac12.
$$

### D51-P7 — Variance ceiling

$$
\operatorname{Var}(a)
\le
\frac{
(2-3\gamma)(3\gamma-1)
}{4}.
$$

### D51-P8 — Resonant-ratio removal

The apparent pointwise ratio

$$
t^2=\frac54
$$

cannot support a genuinely non-affine open branch.

### D51-P9 — Horizontal-dominance constraint

$$
D^2u\neq0
\Rightarrow
|\nabla_hu|
\ge
\frac32|u_z|.
$$

### D51-P10 — Null-Hessian survivor theorem

$$
D^2u
=
\kappa\ell\otimes\ell,
$$

with

$$
\ell^\top G\ell=0,
$$

and

$$
\ell^\top M\nabla u=0.
$$

---

# 29. Closed / corrected routes

## Closed

An active perfect-response central branch cannot enter a strictly negative pseudo-eikonal RHS interval.

## Closed

A pointwise exact-affine central branch was already removed in DCRP50.

## Not closed

The positive-$C$ rank-one null-Hessian branch may have nontrivial local integrable solutions.

## Not claimed

General wave–pseudo-eikonal affine rigidity.

That statement would exceed the proved algebra.

---

# 30. New STOP

$$
\boxed{
\textbf{
STOP-D51:
The central perfect-response problem is no longer a generic nonlinear PDE. Its active periodic branch must stay in the logistic amplitude strip }0\le a\le\frac12\textbf{ with }a'+a-2a^2\ge0\textbf{, and every genuinely non-affine spatial point lies on a rank-one wave-null Hessian cone.}
}
$$

---

# 31. Next autonomous step

## DCRP52 — Null-Hessian Integrability and X72 Realizability Lift

**Working title**

> **Rank-One Null-Hessian Central Survivors: Characteristic Integrability, Vorticity Reconstruction, and the First Non-Liftable X72 Layer**

Primary tasks:

1. impose
   $$
   D^2u=\kappa\ell\otimes\ell
   $$
   and the Hessian integrability/Codazzi conditions;
2. derive the characteristic evolution of
   $$
   \ell,\quad
   \kappa,\quad
   \nabla u;
   $$
3. determine whether $\ell$ must be constant, which would collapse the branch back to affine;
4. if nonlinear developable solutions survive, reconstruct
   $$
   \Omega_h=J\nabla_hu
   $$
   and test the X72 vorticity-stress algebraic cone;
5. identify the first realizability level that fails under same-parent DSS / finite PFET constraints.

Desired endpoint:

$$
\boxed{
\text{integrability collapse}
\ \vee\
\text{explicit null characteristic model}
\ \vee\
\text{X72 non-liftability}
\ \vee\
\text{critical-tail escape}.
}
$$

---

# 32. One-line checkpoint

The perfect-response central PDE has been reduced to a sign-rigid wave–eikonal system: nonpositive RHS is affine and therefore incompatible with the active final branch, while every nonlinear survivor must live on a rank-one null-Hessian characteristic cone with a periodic canonical amplitude trapped in $0\le a\le1/2$.

---

**End checkpoint:** DCRP51  
**Next:** DCRP52 — Null-Hessian Integrability / X72 Realizability Lift.
