# DCRP48 — Pressure-Driven Response-Slope Dynamics, Mixed-Hessian Telescoping, and the Pressure-Neumann Frontier

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / correction + pressure-coupling round  
**Immediate predecessor:** `NS_DCRP47_DualCurrent_Criticality_CharacteristicWindow_2026-08-17.md`

**Primary internal dependencies**
- DCRP-30 — strict same-parent DSS / Type-II exponent window
- DCRP-31 — finite-radius inward PFET matching
- DCRP-41 — fixed-plane zero-shape pancake tensor
- DCRP-42 — planar potential–shear scalar reduction
- DCRP-44 — gauge-flat scalar connection
- DCRP-46 — finite-annulus scalar-transport gap
- DCRP-47 — response-slope compatibility classification

**External calibration**
- D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782.
- G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.
- D. Chae, T.-P. Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP47 introduced the fully flat response slope

$$
c(q,s)=B_q(q,s)
$$

through the canonical constitutive form

$$
w=B(q,s)-2a(s)z.
$$

It derived

$$
\nabla_h\cdot[(c-1)\nabla_hq]
+
\partial_z(cq_z)
=
0
$$

and used it to identify a response window

$$
0\le c\le1.
$$

The first result of DCRP48 is an important correction.

The DCRP47 current

$$
J_c
=
((c-1)\nabla_hq,cq_z)
$$

is exactly

$$
\boxed{
J_c
=
\partial_zV+2a(s)n.
}
$$

Hence

$$
\nabla\cdot J_c=0
$$

is simply

$$
\partial_z(\nabla\cdot V)=0.
$$

Therefore the DCRP47 divergence equation is **not an independent extra PDE** beyond incompressibility.

Its sign-definite testing identities remain valid and useful, but the equation itself must be downgraded to a constitutive recoding of differentiated incompressibility.

The genuinely new dynamical information comes from the **vertical similarity-Euler momentum equation**.

On the fully flat canonical branch,

$$
\boxed{
D_sc
=
-P_{zq}.
}
$$

Equivalently, on every regular patch where

$$
p=\nabla_hq\neq0,
$$

$$
\boxed{
\nabla_hP_z
=
-(D_sc)\,\nabla_hq.
}
$$

Thus:

1. the mixed pressure Hessian must be parallel to $\nabla_hq$;
2. its longitudinal component is the **only driver** of the response-slope dynamics;
3. the response window is a pressure-Hessian trapping problem.

A second exact identity gives the pressure Poisson source:

$$
\boxed{
-\Delta P
=
|D_h^2\phi|_F^2
+
(cq_z-2a)^2
+
2c(c-1)|\nabla_hq|^2.
}
$$

Outside the interval $[0,1]$ the final term is positive.

Therefore, if on a bounded flat patch

$$
c\ge1+\delta
$$

or

$$
c\le-\delta,
$$

then

$$
\boxed{
-\int_{\partial D}\partial_\nu P\,dS
\ge
2\delta(1+\delta)
\int_D|\Omega_h|^2\,dy.
}
$$

So a nonzero elliptic response sector cannot be pressure-isolated: it necessarily carries a finite pressure-Neumann flux.

The interval

$$
\boxed{
0\le c\le1
}
$$

now receives a more physical meaning.

The cross-plane symmetric strain satisfies

$$
\boxed{
P_hS(V)n
=
\left(c-\frac12\right)\nabla_hq,
}
$$

while

$$
|\Omega_h|=|\nabla_hq|.
$$

Hence

$$
\boxed{
0\le c\le1
\iff
2|P_hS(V)n|
\le
|\Omega_h|.
}
$$

The “characteristic window” is exactly the regime in which cross-plane symmetric strain does not dominate the corresponding rotational shear.

Finally, exact DSS periodicity gives a pressure-Hessian Poincaré/telescoping law.

Let

$$
Q(s;q_0)
=
q_0
\exp\left(
-\int_{s_0}^s k(\tau)d\tau
\right),
$$

and

$$
\mu_q
=
e^{(1-2\gamma)S_0}>1.
$$

Define the one-period mixed-pressure drift

$$
\boxed{
\mathscr P(q_0)
=
\int_{s_0}^{s_0+S_0}
P_{zq}(Q(s;q_0),s)\,ds.
}
$$

Then

$$
\boxed{
c(\mu_qq_0,s_0)-c(q_0,s_0)
=
-\mathscr P(q_0).
}
$$

Iterating,

$$
\boxed{
c(\mu_q^Nq)-c(q)
=
-\sum_{j=0}^{N-1}
\mathscr P(\mu_q^jq).
}
$$

If the final survivor remains in

$$
0\le c\le1
$$

along the whole multiplicative scalar orbit, then

$$
\boxed{
\left|
\sum_{j=0}^{N-1}
\mathscr P(\mu_q^jq)
\right|
\le1.
}
$$

Thus a uniform one-signed mixed-pressure gap cannot recur indefinitely inside the characteristic window.

The surviving branch must instead exhibit:

- pressure-Hessian cancellation/telescoping;
- approach to an endpoint or constant response;
- finite pressure/boundary feed;
- or loss of the flat scalar chart.

If

$$
P_{zq}\equiv0,
$$

then $c$ is materially invariant. Exact DSS gives

$$
c(\mu_qq)=c(q).
$$

Continuity at $q=0$ forces

$$
\boxed{
c\equiv c_0
}
$$

on each connected scaling domain containing the origin.

Therefore the zero mixed-pressure branch collapses to the constant-response modes already classified in DCRP47.

This is the new frontier:

$$
\boxed{
\textbf{
pressure-Hessian recurrence / finite pressure boundary feed / constant-response equality mode.
}
}
$$

---

# 1. Similarity-Euler momentum equation

The DSS Euler profile satisfies

$$
\boxed{
\partial_sV
+
(1-\gamma)V
+
\gamma(y\cdot\nabla)V
+
(V\cdot\nabla)V
+
\nabla P
=
0.
}
\tag{1.1}
$$

Define

$$
\boxed{
W=\gamma y+V,
}
\tag{1.2}
$$

and

$$
\boxed{
D_s=\partial_s+W\cdot\nabla.
}
\tag{1.3}
$$

Then

$$
\boxed{
D_sV+(1-\gamma)V+\nabla P=0.
}
\tag{1.4}
$$

---

# 2. Fully flat canonical scalar branch

DCRP44 shows that on the nondegenerate gauge-flat branch there is a unique periodic canonical gauge with

$$
\boxed{
D_sq+k(s)q=0,
}
\tag{2.1}
$$

where

$$
\boxed{
k(s)=1-\gamma-2a(s).
}
\tag{2.2}
$$

The normal velocity has the form

$$
\boxed{
w
=
B(q,s)-2a(s)z.
}
\tag{2.3}
$$

Define the response slope

$$
\boxed{
c(q,s)
=
B_q(q,s).
}
\tag{2.4}
$$

Because the residual scalar gauge is a $q$-translation by a function of $(z,s)$, $c=B_q$ is an intrinsic scalar-response quantity on the canonical flat branch.

---

# 3. Correction to DCRP47: the compatibility current is differentiated incompressibility

Recall

$$
q=w-\phi_z,
$$

and

$$
V_h=\nabla_h\phi.
$$

Since

$$
\nabla_hw
=
c\nabla_hq,
$$

we have

$$
\begin{aligned}
\partial_zV_h
&=
\nabla_h\phi_z
\\
&=
\nabla_h(w-q)
\\
&=
(c-1)\nabla_hq.
\end{aligned}
$$

Also

$$
w_z
=
cq_z-2a.
$$

Therefore

$$
\boxed{
cq_z
=
w_z+2a.
}
\tag{3.1}
$$

The DCRP47 current

$$
J_c
=
\left(
(c-1)\nabla_hq,
cq_z
\right)
$$

becomes

$$
\boxed{
J_c
=
\left(
\partial_zV_h,
w_z+2a
\right)
=
\partial_zV+2an.
}
\tag{3.2}
$$

Because $a=a(s)$ is spatially constant,

$$
\boxed{
\nabla\cdot J_c
=
\partial_z(\nabla\cdot V)
=
0.
}
\tag{3.3}
$$

## Correction D48.C1

The DCRP47 equation

$$
\nabla_h\cdot[(c-1)\nabla_hq]
+
\partial_z(cq_z)=0
$$

is exactly differentiated incompressibility expressed in the flat constitutive variables.

It is not a new independent PDE constraint.

The DCRP47 boundary energy identity remains mathematically correct and its coercive consequences remain available when the boundary flux is controlled.

What is downgraded is only the claim of an additional independent field equation.

---

# 4. Physical meaning of the response slope

Let

$$
p
=
\nabla_hq.
$$

Then

$$
\boxed{
\nabla_hw=cp,
}
\tag{4.1}
$$

and

$$
\boxed{
\partial_zV_h=(c-1)p.
}
\tag{4.2}
$$

The cross-plane symmetric strain vector is

$$
\boxed{
s_\times
:=
P_hS(V)n
=
\frac12
\left(
\partial_zV_h+\nabla_hw
\right).
}
\tag{4.3}
$$

Hence

$$
\boxed{
s_\times
=
\left(
c-\frac12
\right)p.
}
\tag{4.4}
$$

Meanwhile the horizontal vorticity satisfies

$$
\boxed{
|\Omega_h|
=
|p|.
}
\tag{4.5}
$$

Thus

$$
\boxed{
2|s_\times|
=
|2c-1|
|\Omega_h|.
}
\tag{4.6}
$$

---

# 5. Strain–rotation interpretation of the response window

Equation (4.6) gives

$$
\boxed{
0\le c\le1
\iff
|2c-1|\le1
}
$$

and therefore

$$
\boxed{
0\le c\le1
\iff
2|s_\times|
\le
|\Omega_h|.
}
\tag{5.1}
$$

Hence:

### central value

$$
\boxed{
c=\frac12
}
$$

means

$$
\boxed{
s_\times=0.
}
$$

The off-diagonal shear is purely rotational.

### endpoint $c=0$

$$
\nabla_hw=0,
$$

while all horizontal vorticity comes from

$$
-\partial_zV_h.
$$

### endpoint $c=1$

$$
\partial_zV_h=0,
$$

while all horizontal vorticity comes from

$$
\nabla_hw.
$$

### outside $[0,1]$

$$
2|s_\times|
>
|\Omega_h|.
$$

The cross-plane symmetric strain dominates the corresponding rotational shear.

Thus the DCRP47 window is better interpreted as a **cross-strain / rotation balance window**.

---

# 6. Vertical similarity-Euler momentum

The normal component of (1.4) is

$$
\boxed{
D_sw+(1-\gamma)w+P_z=0.
}
\tag{6.1}
$$

Using

$$
w=B(q,s)-2az,
$$

$$
D_sq=-kq,
$$

and

$$
D_sz
=
W_3
=
\gamma z+w
=
B+(\gamma-2a)z,
$$

we obtain

$$
\begin{aligned}
D_sw
&=
B_s
+
B_qD_sq
-
2a'z
-
2aD_sz
\\
&=
B_s
-
ckq
-
2aB
+
\left[
-2a'-2a(\gamma-2a)
\right]z.
\end{aligned}
$$

Adding $(1-\gamma)w$ and using

$$
k=1-\gamma-2a,
$$

gives

$$
\boxed{
D_sw+(1-\gamma)w
=
B_s
-
ckq
+
kB
-
2(a'+a-2a^2)z.
}
\tag{6.2}
$$

Therefore

$$
\boxed{
P_z
=
-B_s
+
ckq
-
kB
+
2(a'+a-2a^2)z.
}
\tag{6.3}
$$

This formula is exact on the fully flat canonical patch.

---

# 7. Response-slope dynamics

Differentiate (6.3) with respect to $q$ at fixed $(z,s)$.

Because

$$
c=B_q,
$$

$$
\partial_q(-B_s)=-c_s,
$$

and

$$
\partial_q(ckq-kB)
=
k(qc_q+c)-kc
=
kqc_q.
$$

Thus

$$
\boxed{
P_{zq}
=
-c_s
+
kq\,c_q.
}
\tag{7.1}
$$

But because $c=c(q,s)$,

$$
D_sc
=
c_s+c_qD_sq
=
c_s-kq\,c_q.
$$

Hence:

## Theorem D48.1 — Pressure-Driven Response-Slope Equation

On every fully flat regular scalar patch,

$$
\boxed{
D_sc
=
-P_{zq}.
}
\tag{7.2}
$$

The scalar-response slope changes only through the mixed normal/scalar derivative of pressure.

---

# 8. Physical mixed-Hessian form

Since $P_z$ depends horizontally through $q$,

$$
\boxed{
\nabla_hP_z
=
P_{zq}\nabla_hq.
}
\tag{8.1}
$$

Therefore:

$$
\boxed{
\nabla_hP_z
=
-(D_sc)\nabla_hq.
}
\tag{8.2}
$$

On a regular patch,

$$
p=\nabla_hq\neq0.
$$

Thus

$$
\boxed{
D_sc
=
-
\frac{
\nabla_hP_z\cdot\nabla_hq
}{
|\nabla_hq|^2
}.
}
\tag{8.3}
$$

Also

$$
\boxed{
(I-\widehat p\otimes\widehat p)\nabla_hP_z
=
0.
}
\tag{8.4}
$$

where

$$
\widehat p=\frac{p}{|p|}.
$$

---

# Theorem D48.2 — Mixed-Pressure Alignment Defect

A necessary condition for the fully flat scalar chart is

$$
\boxed{
\Omega_h\cdot\nabla_hP_z=0,
}
\tag{8.5}
$$

because $\Omega_h$ is orthogonal to $\nabla_hq$.

Equivalently, the mixed pressure-Hessian vector $\nabla_hP_z$ must be collinear with $\nabla_hq$.

Therefore any nonzero transverse component

$$
\boxed{
\mathfrak P_\perp
=
(I-\widehat p\otimes\widehat p)\nabla_hP_z
}
\tag{8.6}
$$

is a native gauge-invariant defect of the fully flat pancake branch.

This creates an explicit pressure-Hessian exit channel.

---

# 9. Endpoint trapping conditions

Suppose a material response trajectory is required to remain inside

$$
0\le c\le1.
$$

At the lower endpoint

$$
c=0,
$$

forward invariance requires

$$
D_sc\ge0.
$$

By Theorem D48.1,

$$
\boxed{
P_{zq}\le0
\qquad
(c=0).
}
\tag{9.1}
$$

At the upper endpoint

$$
c=1,
$$

forward invariance requires

$$
D_sc\le0,
$$

hence

$$
\boxed{
P_{zq}\ge0
\qquad
(c=1).
}
\tag{9.2}
$$

Thus the pressure mixed Hessian must point inward at the two response-window endpoints.

A sign violation forces immediate exit into a sign-definite response sector.

---

# 10. Pressure Poisson decomposition

Take divergence of the similarity-Euler momentum equation.

Because

$$
\nabla\cdot V=0,
$$

the pressure satisfies the standard Euler Poisson relation

$$
\boxed{
-\Delta P
=
\operatorname{tr}
\left[
(\nabla V)^2
\right].
}
\tag{10.1}
$$

On the flat scalar patch, the velocity gradient has block form

$$
\boxed{
\nabla V
=
\begin{pmatrix}
H
&
(c-1)p
\\
cp^T
&
d
\end{pmatrix},
}
\tag{10.2}
$$

where

$$
H=D_h^2\phi,
$$

$$
p=\nabla_hq,
$$

and

$$
\boxed{
d=w_z=cq_z-2a.
}
\tag{10.3}
$$

Because $H$ is symmetric,

$$
\operatorname{tr}(H^2)=|H|_F^2.
$$

A direct block computation gives

$$
\boxed{
\operatorname{tr}
[(\nabla V)^2]
=
|H|_F^2
+
d^2
+
2c(c-1)|p|^2.
}
\tag{10.4}
$$

Therefore:

## Theorem D48.3 — Flat-Pancake Pressure Source Identity

$$
\boxed{
-\Delta P
=
|D_h^2\phi|_F^2
+
(cq_z-2a)^2
+
2c(c-1)|\nabla_hq|^2.
}
\tag{10.5}
$$

This is an exact pressure-source decomposition on the fully flat scalar branch.

---

# 11. Relation to strain versus rotation

Use

$$
c(c-1)
=
\left(c-\frac12\right)^2
-
\frac14.
$$

Then

$$
2c(c-1)|p|^2
=
2|s_\times|^2
-
\frac12|\Omega_h|^2.
$$

Thus (10.5) becomes

$$
\boxed{
-\Delta P
=
|D_h^2\phi|_F^2
+
(cq_z-2a)^2
+
2|s_\times|^2
-
\frac12|\Omega_h|^2.
}
\tag{11.1}
$$

This is the flat-pancake form of the standard competition between strain and rotation in the Euler pressure source.

The response window

$$
0\le c\le1
$$

is exactly the sector in which the cross-plane shear contribution

$$
2c(c-1)|p|^2
$$

is nonpositive.

Outside the window it is strictly positive.

---

# 12. Pressure-Neumann gap outside the window

Let

$$
D
$$

be a bounded smooth domain contained in a fully flat regular patch.

Integrate (10.5):

$$
\boxed{
-\int_{\partial D}
\partial_\nu P\,dS
=
\int_D
\left[
|H|_F^2
+
d^2
+
2c(c-1)|p|^2
\right]dy.
}
\tag{12.1}
$$

Suppose

$$
\boxed{
c\ge1+\delta
}
\tag{12.2}
$$

throughout $D$.

Then

$$
c(c-1)
\ge
\delta(1+\delta).
$$

Likewise, if

$$
\boxed{
c\le-\delta,
}
\tag{12.3}
$$

then again

$$
c(c-1)
\ge
\delta(1+\delta).
$$

Therefore:

## Theorem D48.4 — Elliptic-Sector Pressure-Neumann Gap

If either

$$
c\ge1+\delta
$$

or

$$
c\le-\delta
$$

throughout $D$, then

$$
\boxed{
-\int_{\partial D}
\partial_\nu P\,dS
\ge
2\delta(1+\delta)
\int_D
|\Omega_h|^2dy.
}
\tag{12.4}
$$

Thus a nonzero sign-definite response sector outside $[0,1]$ necessarily exports a strictly positive integrated pressure-Poisson source through the finite boundary.

No zero compatibility-flux assumption is needed.

This is stronger than the DCRP47 zero-boundary coercivity statement.

---

# 13. Updated meaning of leaving the response window

DCRP47 said:

$$
c\notin[0,1]
$$

leads to an elliptic compatibility sector.

DCRP48 refines this.

A nonzero flat patch with

$$
\operatorname{dist}(c,[0,1])\ge\delta
$$

must carry a finite pressure-Neumann gap:

$$
\boxed{
\mathsf O_{\partial P}
=
-\int_{\partial D}\partial_\nu P\,dS
>0.
}
$$

Therefore leaving the response window is not merely a change of PDE type.

It is a quantitatively visible pressure-boundary event.

The final branch becomes:

$$
\boxed{
c\in[0,1]
}
$$

or

$$
\boxed{
\text{finite pressure-Neumann carrier}
}
$$

or

$$
\boxed{
\text{flat-chart transition}.
}
$$

---

# 14. Scalar characteristics

On the fully flat branch,

$$
D_sq=-k(s)q.
$$

Along a scalar/material characteristic,

$$
\boxed{
\frac{dQ}{ds}
=
-k(s)Q.
}
\tag{14.1}
$$

With initial value

$$
Q(s_0;q_0)=q_0,
$$

the solution is

$$
\boxed{
Q(s;q_0)
=
q_0
\exp
\left[
-\int_{s_0}^s
k(\tau)d\tau
\right].
}
\tag{14.2}
$$

DCRP42 gives

$$
\boxed{
\frac1{S_0}
\int_{s_0}^{s_0+S_0}
k(s)ds
=
2\gamma-1
<0.
}
\tag{14.3}
$$

Therefore after one period,

$$
\boxed{
Q(s_0+S_0;q_0)
=
\mu_q q_0,
}
\tag{14.4}
$$

where

$$
\boxed{
\mu_q
=
e^{(1-2\gamma)S_0}
>1.
}
\tag{14.5}
$$

---

# 15. Response-slope Poincaré law

Along the same characteristic, Theorem D48.1 gives

$$
\frac{d}{ds}
c(Q(s;q_0),s)
=
-
P_{zq}(Q(s;q_0),s).
$$

Integrating one period,

$$
\begin{aligned}
&
c(Q(s_0+S_0;q_0),s_0+S_0)
-
c(q_0,s_0)
\\
&\qquad
=
-
\int_{s_0}^{s_0+S_0}
P_{zq}(Q(s;q_0),s)ds.
\end{aligned}
$$

On the exact periodic constitutive chart,

$$
c(q,s+S_0)=c(q,s).
$$

Define

$$
\boxed{
\mathscr P(q_0)
=
\int_{s_0}^{s_0+S_0}
P_{zq}(Q(s;q_0),s)ds.
}
\tag{15.1}
$$

Then:

## Theorem D48.5 — Mixed-Pressure Poincaré Drift

$$
\boxed{
c(\mu_qq_0,s_0)
-
c(q_0,s_0)
=
-\mathscr P(q_0).
}
\tag{15.2}
$$

This is an exact one-period response-slope return law.

---

# 16. Telescoping pressure-Hessian budget

Apply Theorem D48.5 to

$$
q_0,
\mu_qq_0,
\mu_q^2q_0,
\ldots.
$$

Summing gives

$$
\boxed{
c(\mu_q^Nq_0,s_0)
-
c(q_0,s_0)
=
-
\sum_{j=0}^{N-1}
\mathscr P(\mu_q^jq_0).
}
\tag{16.1}
$$

Suppose the entire multiplicative orbit remains in the characteristic response window:

$$
\boxed{
0\le
c(\mu_q^jq_0,s_0)
\le1
}
\tag{16.2}
$$

for all $j$.

Then

$$
\boxed{
\left|
\sum_{j=0}^{N-1}
\mathscr P(\mu_q^jq_0)
\right|
\le1.
}
\tag{16.3}
$$

## Theorem D48.6 — Characteristic-Window Pressure Telescoping

A response trajectory that remains forever in $[0,1]$ cannot support an indefinitely repeated one-signed mixed-pressure period gap of fixed size.

In particular, if for infinitely many successive returns

$$
\mathscr P(\mu_q^jq_0)
\ge\varepsilon>0,
$$

then the trajectory exits $[0,1]$ after at most $O(\varepsilon^{-1})$ such returns.

The same holds with the opposite sign.

Thus the final characteristic branch requires pressure-Hessian cancellation, decay, or sign alternation.

---

# 17. Same-sign corollary

Suppose

$$
\mathscr P(\mu_q^jq_0)
\ge0
$$

for all $j$ and the response remains in $[0,1]$.

Then (16.3) implies

$$
\boxed{
\sum_{j=0}^{\infty}
\mathscr P(\mu_q^jq_0)
\le1.
}
\tag{17.1}
$$

Hence

$$
\boxed{
\mathscr P(\mu_q^jq_0)
\to0.
}
\tag{17.2}
$$

Similarly for an everywhere nonpositive pressure drift.

So a one-signed pressure mechanism must asymptotically switch off along the multiplicative scalar ladder.

---

# 18. Zero mixed-pressure branch

Assume

$$
\boxed{
P_{zq}=0
}
\tag{18.1}
$$

throughout a connected flat constitutive chart.

Then Theorem D48.1 gives

$$
\boxed{
D_sc=0.
}
\tag{18.2}
$$

Thus $c$ is constant along scalar characteristics.

After one DSS period,

$$
\boxed{
c(\mu_qq,s_0)
=
c(q,s_0).
}
\tag{18.3}
$$

Suppose the $q$-domain contains $0$ and $c$ is continuous there.

For any fixed $q$ in the same positive scaling component,

$$
c(q)
=
c(\mu_q^{-N}q).
$$

As

$$
N\to\infty,
$$

$$
\mu_q^{-N}q\to0.
$$

Hence

$$
c(q)=c(0).
$$

The same argument applies on the negative side.

Continuity at zero identifies the constants.

## Theorem D48.7 — Zero-Pressure-Holonomy Rigidity

On a connected scaling domain containing $q=0$,

$$
\boxed{
P_{zq}\equiv0
}
$$

and exact DSS periodicity imply

$$
\boxed{
c(q,s)\equiv c_0
}
$$

for a constant response slope.

Therefore the zero mixed-pressure branch collapses to the constant-response equality modes already classified in DCRP47.

---

# 19. Constant-response consequences

If

$$
c=c_0,
$$

the flat constitutive law is

$$
B(q,s)
=
c_0q+b(s).
$$

DCRP47 gives the spatial compatibility form

$$
\boxed{
c_0q_{zz}
+
(c_0-1)\Delta_hq
=
0.
}
\tag{19.1}
$$

This equation is now understood as differentiated incompressibility under the constant constitutive shear split.

Nevertheless its classification remains useful.

### $c_0<0$ or $c_0>1$

The sector is sign-definite and DCRP48 gives a positive pressure-Neumann gap for any nonzero bounded patch separated from the endpoints.

### $0<c_0<1$

The constant-slope mode has the real characteristic cone

$$
\boxed{
\xi_z^2
=
\frac{1-c_0}{c_0}
|\xi_h|^2.
}
\tag{19.2}
$$

### $c_0=0$

$$
\Delta_hq=0.
$$

### $c_0=1$

$$
q_{zz}=0.
$$

Thus the pressure-flat response branch becomes an exact endpoint/cone classification rather than an unconstrained scalar state.

---

# 20. Pressure Poisson flux versus PFET

DCRP31 gives an inward pressure–kinetic energy current

$$
\boxed{
\mathcal F_{\rm PFET}(R)
=
\int
(e+P)V\cdot n
}
$$

on finite matching radii.

DCRP48 gives, outside the response window, a pressure-Neumann current

$$
\boxed{
\mathcal N_P(D)
=
-\int_{\partial D}
\partial_\nu P\,dS.
}
$$

These are different boundary observables.

There is no exact identity in the current proof package equating their signs or magnitudes.

Therefore DCRP48 does **not** claim

$$
\mathcal N_P
\sim
-\mathcal F_{\rm PFET}.
$$

The useful result is that pressure now appears in two independent finite-boundary ways:

1. pressure value times velocity in PFET;
2. pressure normal derivative in the elliptic response sector.

The next coupling problem is therefore substantially sharper than “pressure must matter.”

---

# 21. Updated finite-annulus pressure package

The most rigid rank-two survivor now carries the observer tuple

$$
\boxed{
\mathsf O_{48}
=
\left(
\mathsf O_{\rm PFET},
\mathsf O_{\rm scalar\ transport},
c,
\mathfrak P_\perp,
\mathscr P,
\mathcal N_P
\right).
}
\tag{21.1}
$$

The branches are:

### Branch T — transverse mixed-pressure defect

$$
\boxed{
\mathfrak P_\perp\neq0.
}
$$

The fully flat scalar chart fails.

### Branch E — elliptic response excursion

$$
\boxed{
c\notin[0,1].
}
$$

Then a finite pressure-Neumann gap is compulsory.

### Branch C — trapped characteristic response

$$
\boxed{
0\le c\le1.
}
$$

Then mixed-pressure Poincaré drift obeys the bounded telescoping budget.

### Branch Z — zero mixed-pressure drift

$$
\boxed{
P_{zq}=0.
}
$$

Then $c$ collapses to a constant-response mode.

This is a stronger classification than DCRP47.

---

# 22. NTLA-O interpretation

DCRP47 used a coarse constitutive observer and saw an anisotropic divergence equation.

DCRP48 applies a finer structural audit and recognizes that the equation itself is only differentiated incompressibility.

So the apparent new PDE is correctly quotient-collapsed.

The next observer reads:

$$
\boxed{
\text{mixed pressure Hessian}
}
$$

and discovers genuinely new dynamical information:

$$
\boxed{
D_sc=-P_{zq}.
}
$$

The NTLA-O refinement is therefore:

$$
\boxed{
\text{constitutive PDE form}
\rightarrow
\text{identity audit}
\rightarrow
\text{pressure-driven slope dynamics}.
}
$$

This is exactly the desired behavior of the rebuilt framework: false novelty is removed, while a more intrinsic obstruction is exposed.

---

# 23. Updated final rank-two survivor

After DCRP48, a fully flat final survivor must satisfy:

$$
\boxed{
\begin{aligned}
&
\text{strict same-parent DSS}
\\
&+
\text{rank two}
\\
&+
\text{fixed plane / zero shape action}
\\
&+
\text{gauge-flat scalar connection}
\\
&+
\text{finite inward PFET}
\\
&+
\text{finite signed scalar transport}
\\
&+
\Big[
\mathfrak P_\perp\neq0
\\
&\qquad\vee\
c\notin[0,1]\ \text{with finite pressure-Neumann flux}
\\
&\qquad\vee\
0\le c\le1\ \text{with pressure-Hessian telescoping}
\\
&\qquad\vee\
P_{zq}=0\ \text{and constant-response mode}
\Big].
\end{aligned}
}
$$

If the first branch occurs, the fully flat state exits.

The genuinely most rigid branch is therefore:

$$
\boxed{
0\le c\le1,
\qquad
\mathfrak P_\perp=0,
}
$$

with a bounded mixed-pressure telescoping budget.

---

# 24. Status ledger

## PROVED this round

### D48-P1 — DCRP47 compatibility-current correction

$$
J_c
=
\partial_zV+2an.
$$

Thus its divergence equation is differentiated incompressibility.

### D48-P2 — Physical shear interpretation

$$
P_hS(V)n
=
(c-\tfrac12)\nabla_hq.
$$

Hence $[0,1]$ is the cross-strain / rotation balance window.

### D48-P3 — Exact vertical pressure formula

$$
P_z
=
-B_s
+
ckq
-
kB
+
2(a'+a-2a^2)z.
$$

### D48-P4 — Pressure-driven response slope

$$
D_sc=-P_{zq}.
$$

### D48-P5 — Mixed-pressure alignment defect

$$
(I-\widehat p\otimes\widehat p)\nabla_hP_z=0
$$

is necessary on the flat branch.

### D48-P6 — Pressure Poisson decomposition

$$
-\Delta P
=
|D_h^2\phi|^2
+
(cq_z-2a)^2
+
2c(c-1)|\nabla_hq|^2.
$$

### D48-P7 — Elliptic-sector pressure-Neumann gap

For $c$ uniformly outside $[0,1]$,

$$
-\int_{\partial D}\partial_\nu P
\ge
2\delta(1+\delta)
\int_D|\Omega_h|^2.
$$

### D48-P8 — Mixed-pressure Poincaré law

$$
c(\mu_qq)-c(q)
=
-\mathscr P(q).
$$

### D48-P9 — Characteristic-window pressure telescoping

If $c$ stays in $[0,1]$,

$$
\left|
\sum_{j=0}^{N-1}
\mathscr P(\mu_q^jq)
\right|
\le1.
$$

### D48-P10 — Zero mixed-pressure rigidity

$$
P_{zq}\equiv0
$$

plus DSS scaling and continuity at $q=0$ force constant response slope.

---

# 25. Corrected / downgraded statements

## DCRP47 correction

The phrase “new compatibility PDE” should be replaced by:

> **flat constitutive form of differentiated incompressibility.**

The response-window coercivity and constant-slope classification remain valid as consequences of this identity plus boundary assumptions.

## Still NO-GO

No exact PFET / pressure-Neumann equality is available.

Do not merge these two boundary currents without a new theorem.

---

# 26. New STOP

$$
\boxed{
\textbf{
STOP-D48:
The response window is not governed by an independent compatibility PDE; its true dynamics are pressure-Hessian driven. A nonzero survivor must either carry a finite mixed-pressure/Neumann defect or remain in }0\le c\le1\textbf{ under a bounded pressure-Hessian telescoping budget, with the zero-drift branch collapsing to constant response.}
}
$$

---

# 27. Next autonomous step

## DCRP49 — Mixed Pressure Hessian versus Finite PFET

**Working title**

> **Pressure-Hessian Alignment, Neumann/PFET Boundary Duality, and the Constant-Response Escape Classes**

Primary tasks:

1. place the DCRP48 pressure-Neumann gap and DCRP31 PFET gap on one common annulus;
2. use harmonic/nonlocal pressure decomposition to test whether a recurrent inward PFET layer can simultaneously have vanishing mixed-pressure drift;
3. classify the constant-response cases
   $$
   c=0,\quad 0<c<1,\quad c=1
   $$
   against the pressure formula;
4. test whether the characteristic-cone branch necessarily produces a nonzero pressure multipole or finite boundary flux;
5. if the pressure coupling remains critical, feed the mixed-Hessian alignment condition into the X72 pressure/cofactor realizability machinery.

Desired endpoint:

$$
\boxed{
\text{PFET–pressure-Hessian coupling}
\ \vee\
\text{constant-response exact model}
\ \vee\
\text{transition}
\ \vee\
\text{X72 realizability handoff}.
}
$$

---

# 28. One-line checkpoint

The DCRP47 “new PDE” has been correctly reduced to differentiated incompressibility, while the true flat-pancake response dynamics are now exactly pressure-driven: exiting $0\le c\le1$ forces a quantitative finite pressure-Neumann flux, staying inside forces a bounded mixed-pressure telescoping budget, and zero pressure drift collapses the survivor to constant-response modes.

---

**End checkpoint:** DCRP48  
**Next:** DCRP49 — Mixed Pressure Hessian / PFET Coupling.
