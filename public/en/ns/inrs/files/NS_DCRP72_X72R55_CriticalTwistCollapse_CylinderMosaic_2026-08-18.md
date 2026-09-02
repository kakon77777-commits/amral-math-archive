# DCRP72 / X72-R55 — Critical Twist Collapse and the Multi-Axis Vacuum-Corridor Endpoint

**Date:** 2026-08-18  
**Status:** Proof-development checkpoint  
**Predecessor:** DCRP71 / X72-R54

## 0. Result

DCRP71 left one native endpoint not covered by the stronger Xue-type sublinear class:

\[
\boxed{\mathsf C_{\rm twist}^{\rm crit}}
\]

a transparent cylindrical tail that could saturate the native Morrey law

\[
\boxed{\int_{B_R}|V(y,s)|^2\,dy\lesssim R.}
\]

DCRP72 proves that a genuinely smooth **active twist** cannot realize this endpoint.

Let

\[
\xi(z,s)=(\cos\theta,\sin\theta),\qquad \eta=J\xi,
\]

and define rotating horizontal coordinates

\[
r=\xi\cdot y_h,\qquad t=\eta\cdot y_h.
\]

After the D58 affine-offset elimination,

\[
q_{\rm cyl}=f(r,z,s)+c_0(z,s),\qquad a=f_r,
\]

so

\[
\boxed{\Omega=a(r,z,s)\eta(z,s).}
\]

Write

\[
V_h=A\xi+B\eta,\qquad w=V_3.
\]

On the active set \(a\neq0\), D42 gives

\[
\boxed{w_t=0.}
\]

Define the cylinder-angle material rate

\[
\boxed{\Theta=\theta_s+(\gamma z+w)\theta_z.}
\]

A direct calculation of

\[
D_s\Omega+\Omega=(\Omega\cdot\nabla)V
\]

gives

\[
\boxed{A_t=-\Theta}
\]

and

\[
\boxed{
aB_t
=
a_s+(\gamma r+A)a_r+(\gamma z+w)a_z+\Theta\,t\,a_r+a.
}
\]

If \(\Theta\neq0\), then \(A\) grows linearly in \(t\), which produces

\[
E(R)\gtrsim R^3,
\]

contradicting the native \(E(R)\lesssim R\). Hence

\[
\boxed{\Theta=0.}
\]

Then the \(B_t\) equation is independent of \(t\); any nonzero \(B_t\) again yields cubic energy growth. Therefore

\[
\boxed{A_t=B_t=w_t=0,}
\]

and

\[
\boxed{
a_s+(\gamma r+A)a_r+(\gamma z+w)a_z+a=0.
}
\]

Thus every active critical cylinder is already velocity-translation-invariant along its instantaneous axis.

Now use the D42 potential representation

\[
V_h=\nabla_h\phi,\qquad q_{\rm cyl}=w-\phi_z.
\]

Since \(q_r=a\),

\[
\partial_zV_h=\nabla_h(w-q_{\rm cyl})=(w_r-a)\xi.
\]

But in the rotating frame, with \(A_t=B_t=0\),

\[
\partial_zV_h
=
[A_z+\theta_z tA_r-\theta_zB]\xi
+
[B_z+\theta_z tB_r+\theta_zA]\eta.
\]

If \(\theta_z\neq0\), equality for all \(t\) forces

\[
\boxed{A_r=B_r=0.}
\]

Incompressibility then gives

\[
w_z+\theta_z t\,w_r=0,
\]

hence

\[
\boxed{w_r=w_z=0.}
\]

The \(\xi\)-equation becomes

\[
\boxed{a=\theta_zB-A_z,}
\]

so \(a\) is independent of \(r\).

Therefore:

\[
\boxed{
\theta_z\neq0
\Longrightarrow
\Omega(y_h,z,s)=a(z,s)\eta(z,s)
}
\]

is uniform across the entire horizontal plane.

A nonzero plane-uniform vorticity component on a positive \(z\)-interval yields by curl duality

\[
\boxed{E(R)\gtrsim R^2,}
\]

again contradicting the native Morrey bound.

Hence the main theorem:

\[
\boxed{a\neq0\Longrightarrow \theta_z=0.}
\]

Since \(\Theta=0\), on the same active set

\[
\boxed{\theta_s=0.}
\]

So the cylinder direction is locally constant in both \(z\) and \(s\) wherever vorticity is nonzero.

Equivalently,

\[
\boxed{
\operatorname{supp}(\theta_z,\theta_s)\subseteq\{a=0\}.
}
\]

Axis changes can occur only through zero-vorticity corridors.

Because the similarity vorticity equation is linear homogeneous along material trajectories,

\[
D_s\Omega=(S-I)\Omega,
\]

the zero-vorticity set is materially preserved:

\[
\boxed{\Omega(s_0)=0\iff \Omega(s)=0.}
\]

Thus the reset corridors are genuine material vacuum separators.

If all active sectors share one axis, the global vorticity is translation invariant in that direction. D71 then makes the flow global 2D3C and finite-energy-per-unit-length, forcing by DSS energy scaling

\[
\boxed{\alpha=1,}
\]

contradicting

\[
1<\alpha<3/2.
\]

Therefore the only native transparent tail left is:

\[
\boxed{
\textbf{a multi-axis straight-cylinder mosaic separated by material vacuum corridors}.
}
\]

The former “critical twisting cylinder” is gone.

---

## 1. Cylindrical material derivative

At fixed physical \(y_h\),

\[
r_z=\theta_z t,\qquad t_z=-\theta_z r,
\]

\[
r_s=\theta_s t,\qquad t_s=-\theta_s r.
\]

For

\[
\Omega=a\eta,
\]

one gets

\[
\boxed{
\begin{aligned}
D_s\Omega
={}&
[a_s+(\gamma r+A)a_r+(\gamma z+w)a_z+\Theta t a_r]\eta\\
&-a\Theta\xi.
\end{aligned}}
\]

Since \((\Omega\cdot\nabla)V=a\partial_tV\), comparison gives the equations above.

---

## 2. Cubic energy exclusion

If \(A_t=c_0\neq0\) on a fixed positive \((r,z)\) patch, then

\[
A=c_0t+O(1),
\]

and

\[
\int_{|t|\le R}|A|^2dt\sim R^3.
\]

The same applies to \(B_t\neq0\).

Thus native Morrey immediately forces local cylinder-line velocity invariance.

---

## 3. Plane-uniform vorticity exclusion

If \(|a(z,s)|\ge a_0>0\) on a compact \(z\)-interval, choose

\[
\psi_R=\zeta(z)\chi(y_h/R)\operatorname{sgn}(a)\eta(z,s).
\]

Then

\[
\int\Omega\cdot\psi_R\gtrsim R^2,
\]

while

\[
\|\nabla\times\psi_R\|_2\lesssim R.
\]

Using \(\Omega=\nabla\times V\),

\[
R^2\lesssim \|V\|_{L^2(B_{CR})}R,
\]

so

\[
\boxed{\int_{B_{CR}}|V|^2\gtrsim R^2.}
\]

This is incompatible with \(E(R)\lesssim R\).

---

## 4. Material vacuum corridors

Because

\[
D_s\Omega=(S-I)\Omega,
\]

the fundamental matrix along a smooth material trajectory is invertible. Hence zero and nonzero vorticity are preserved along trajectories.

Thus any finite change of cylinder direction requires a material region where the cylindrical vorticity vanishes.

The direction cannot continuously twist through active vorticity.

---

## 5. Single-axis tail is already impossible

If all active components use one direction \(\eta_0\), then

\[
\Omega(y+t\eta_0,s)=\Omega(y,s)
\]

globally, including vacuum regions.

The D57 translation-difference argument under native Morrey yields

\[
V(y+t\eta_0,s)=V(y,s).
\]

Hence the flow is global 2D3C.

Native Morrey implies finite energy per unit invariant length. Smooth Euler conserves that two-dimensional per-length energy, while DSS scaling gives

\[
\mathcal E_2(t)=\Lambda^{2\alpha-2}\mathcal E_2(t').
\]

For nonzero conserved \(\mathcal E_2\),

\[
\boxed{\alpha=1,}
\]

which is outside the strict Type-II interior.

Therefore at least two nonparallel active axes are required.

---

## 6. New endpoint: \(\mathsf C_{\rm mosaic}^{crit}\)

The surviving critical transparent tail satisfies:

1. every nonzero vorticity sector is a straight-cylinder sector;
2. total velocity is translation invariant along that sector's axis on the active support;
3. the axis is constant in \(z\) and \(s\) within each active component;
4. different axes are separated by material zero-vorticity corridors;
5. at least two nonparallel axes occur globally;
6. the overall profile remains at the linear Morrey endpoint.

Denote this endpoint

\[
\boxed{\mathsf C_{\rm mosaic}^{crit}.}
\]

This is substantially narrower than the D71 twisting-cylinder class.

---

## 7. Next interaction problem

Fix one active sector \(A\) with axis \(\eta_A\). Decompose schematically

\[
V=V_A+V_{\rm ext}.
\]

In an open subset of \(A\) disjoint from other vorticity sectors,

\[
\nabla\times V_{\rm ext}=0,\qquad \nabla\cdot V_{\rm ext}=0,
\]

hence

\[
\boxed{\Delta V_{\rm ext}=0.}
\]

But D72 requires

\[
\partial_{\eta_A}V=0
\]

in the active sector. The self field has the same symmetry, so

\[
\boxed{\partial_{\eta_A}V_{\rm ext}=0}
\]

on an open set.

Thus the field generated by all other nonparallel sectors must be harmonic and translation-invariant along \(\eta_A\) on an open subset of \(A\).

That is a strong unique-continuation / multipole constraint.

The next round attacks precisely this mutual compatibility.

---

## Status

### Proved
- exact cylindrical vorticity material equations;
- \(\Theta=0\) by native Morrey;
- \(A_t=B_t=w_t=0\);
- nonzero twist forces horizontal-uniform vorticity;
- horizontal-uniform vorticity forces \(E(R)\gtrsim R^2\);
- therefore \(a\neq0\Rightarrow\theta_z=\theta_s=0\);
- axis change is confined to material vorticity-vacuum corridors;
- global single-axis tail is excluded;
- native endpoint reduces to a multi-axis straight-cylinder/vacuum mosaic.

### Not proved
- two or more nonparallel cylinder sectors are mutually impossible;
- vacuum corridors necessarily create X72 activity;
- the mosaic cannot remain at the linear Morrey endpoint.

---

## STOP-D72

\[
\boxed{
\textbf{
Genuine smooth twisting is eliminated at the native Morrey endpoint. The only transparent critical tail left is a multi-axis mosaic of straight infinite cylindrical vorticity sectors separated by material zero-vorticity corridors.}
}
\]

---

## Next: DCRP73 / X72-R56

**Multi-Axis Cylinder Interaction Rigidity**

Target:

\[
\boxed{
\mathsf C_{\rm mosaic}^{crit}
\Longrightarrow
\text{interaction defect}
\ \vee\
\text{one explicit multi-axis harmonic normal form}.
}
\]
