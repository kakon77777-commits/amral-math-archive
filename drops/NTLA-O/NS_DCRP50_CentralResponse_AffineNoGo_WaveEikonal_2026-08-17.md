# DCRP50 — Central Response Reduction, Exact-Affine NO-GO, and the Three-Component Pressure-Realizability Frontier

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / central invisible-mode round  
**Immediate predecessor:** `NS_DCRP49_PFET_Neumann_Independence_OffCentral_ResponseDefect_2026-08-17.md`

**Primary internal dependencies**
- DCRP-38 — affine/non-affine strain residual and covariance-turnover split
- DCRP-41 — zero-shape fixed-plane canonical pancake tensor
- DCRP-42 — planar potential–shear scalar reduction
- DCRP-44 — gauge-flat scalar connection
- DCRP-48 — pressure-driven response slope
- DCRP-49 — off-central response defect-energy law
- X72 Round37 — affine pressure-response defect
- X72 Round42–43 — vorticity-stress / realizability frontier

**External calibration checked before this round**
- Agafontsev–Kuznetsov–Mailybaev, arXiv:1609.07782: exact Euler pancake solutions combine shear with asymmetric strain, so generic pancake geometry is not locally contradictory by itself.
- Seregin, arXiv:2606.29468: contemporary Type-II analysis continues to use Euler-scale local limits and Liouville-type exclusions.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP49 reduced the most rigid non-transitioning rank-two pancake branch to the unique mixed-cofactor-invisible response slope

$$
\boxed{
c=B_q=\frac12.
}
$$

DCRP50 completely substitutes this central value back into the flat scalar representation.

The central branch satisfies the exact constitutive laws

$$
\boxed{
w
=
\frac12q+b(s)-2a(s)z,
}
$$

$$
\boxed{
\phi_z
=
-\frac12q+b(s)-2a(s)z,
}
$$

and therefore

$$
\boxed{
q_{zz}
=
\Delta_hq.
}
$$

The mixed pressure Hessian vanishes automatically:

$$
\boxed{
\nabla_hP_z=0,
}
$$

and

$$
\boxed{
P_z
=
-\bigl(b'+kb\bigr)
+
2\bigl(a'+a-2a^2\bigr)z.
}
$$

Thus the central branch is not pressure-free; rather, the **two mixed components** of the five-dimensional X72 affine pressure-response defect vanish identically.

The remaining X72 defect compresses exactly to three components.

Define

$$
E_p
=
H_P^0+C_S^0.
$$

On the central branch write

$$
H=D_h^2\phi,
\qquad
d=w_z=\frac12q_z-2a,
\qquad
p=\nabla_hq.
$$

Then

$$
\boxed{
(E_p)_{hn}=0,
}
$$

while the remaining defect is determined by

$$
\boxed{
e_n
:=
(E_p)_{nn}
=
P_{zz}+d^2-\frac16|p|^2,
}
$$

and the planar trace-free tensor

$$
\boxed{
T_h
:=
(E_p)_{hh}^0
=
(D_h^2P)^0-dH^0.
}
$$

Moreover

$$
\boxed{
|E_p|^2
=
|T_h|^2
+
\frac32e_n^2.
}
$$

Therefore the central “invisible” mode is only invisible to the mixed pressure/cofactor block; it is still visible to a **three-dimensional normal + planar-deviatoric pressure-response defect**.

If the full X72 affine pressure response is perfect,

$$
E_p=0,
$$

the central branch must satisfy the exact nonlinear realizability system

$$
\boxed{
q_{zz}=\Delta_hq,
}
$$

and

$$
\boxed{
|\nabla_hq|^2
-
\frac32(q_z-4a)^2
=
12(a'+a-2a^2),
}
$$

together with

$$
\boxed{
(D_h^2P)^0
=
dH^0.
}
$$

This is the new central **wave–pseudo-eikonal pressure-realizability system**.

The strongest result of the round is an exact local NO-GO.

DCRP41's pointwise canonical fixed-plane pancake strain is

$$
\boxed{
A_{\rm pan}
=
a(s)\operatorname{diag}(1,1,-2).
}
$$

Assume the actual local strain itself equals this tensor on an open central flat patch.

Then the central constitutive relations force

$$
q_z=0,
$$

and

$$
D_h^2q=0.
$$

Hence

$$
q(y,s)
=
K(s)\cdot y_h+g(s).
$$

But the central cross-shear identity forces

$$
\partial_zV_h=-\frac12K(s).
$$

Substituting into the exact scalar transport equation

$$
D_sq+kq=0
$$

produces the uncancellable term

$$
-\frac12z|K|^2.
$$

Therefore

$$
\boxed{
K=0.
}
$$

Consequently

$$
\boxed{
\Omega_h=J K=0.
}
$$

So:

> **A nonzero central $c=1/2$ rank-two pancake cannot be a pointwise exact canonical affine pancake jet.**

This is stronger than a Floquet-average contradiction and does not require periodicity.

Hence every active central survivor must carry at least one of:

1. pointwise non-affine strain relative to the DCRP41 pancake jet;
2. covariance/core turnover or structured cancellation hiding that non-affinity from the DCRP38 covariance residual;
3. nonzero remaining three-component X72 pressure-response defect;
4. if the pressure defect also vanishes, a genuinely nonlinear/nonlocalized solution of the central wave–pseudo-eikonal realizability system.

The exact pure-affine central escape is closed.

The next target is therefore no longer the five-dimensional pressure defect and no longer generic pancake geometry.

It is:

$$
\boxed{
\textbf{
central perfect-response wave–pseudo-eikonal realizability
}
}
$$

together with the mandatory non-affine strain residual.

---

# 1. Central response branch

DCRP49 identifies the most rigid mixed-pressure/cofactor-invisible branch as

$$
\boxed{
c
=
B_q
=
\frac12.
}
\tag{1.1}
$$

Because $c$ is constant in $q$,

$$
\boxed{
B(q,s)
=
\frac12q+b(s).
}
\tag{1.2}
$$

DCRP44's flat constitutive form is

$$
w=B(q,s)-2a(s)z.
$$

Therefore

$$
\boxed{
w
=
\frac12q+b(s)-2a(s)z.
}
\tag{1.3}
$$

---

# 2. Potential relation

The planar shear scalar is

$$
\boxed{
q=w-\phi_z.
}
\tag{2.1}
$$

Hence

$$
\boxed{
\phi_z
=
w-q
=
-\frac12q+b(s)-2a(s)z.
}
\tag{2.2}
$$

The horizontal velocity is

$$
\boxed{
V_h=\nabla_h\phi.
}
\tag{2.3}
$$

---

# 3. Normal and cross derivatives

Differentiate (1.3).

Because $b$ and $a$ depend only on $s$,

$$
\boxed{
w_z
=
\frac12q_z-2a.
}
\tag{3.1}
$$

Define

$$
\boxed{
d:=w_z.
}
\tag{3.2}
$$

Then

$$
\boxed{
d
=
\frac12q_z-2a.
}
\tag{3.3}
$$

Horizontally,

$$
\boxed{
\nabla_hw
=
\frac12\nabla_hq.
}
\tag{3.4}
$$

From (2.2),

$$
\boxed{
\partial_zV_h
=
\nabla_h\phi_z
=
-\frac12\nabla_hq.
}
\tag{3.5}
$$

Therefore

$$
\boxed{
\frac12
\left(
\nabla_hw+\partial_zV_h
\right)
=
0.
}
\tag{3.6}
$$

The entire cross-plane velocity gradient is antisymmetric.

This is the exact geometric meaning of the central response.

---

# 4. Central incompressibility identity

Incompressibility gives

$$
\boxed{
\Delta_h\phi+w_z=0.
}
\tag{4.1}
$$

Using (3.1),

$$
\boxed{
\Delta_h\phi
=
2a-\frac12q_z.
}
\tag{4.2}
$$

Differentiate in $z$:

$$
\boxed{
\partial_z\Delta_h\phi
=
-\frac12q_{zz}.
}
\tag{4.3}
$$

But derivatives commute and (2.2) gives

$$
\Delta_h\phi_z
=
-\frac12\Delta_hq.
$$

Hence:

## Theorem D50.1 — Central Spatial Wave Identity

Every regular central flat patch satisfies

$$
\boxed{
q_{zz}
=
\Delta_hq.
}
\tag{4.4}
$$

As already recognized in DCRP48, this type of relation is a constitutive recoding of differentiated incompressibility, not an independent extra field equation.

It remains a useful exact realization constraint.

---

# 5. Central pressure structure

DCRP48 gives the exact flat-branch formula

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

For

$$
c=\frac12,
$$

$$
B=\frac12q+b(s).
$$

Because $B_s$ means partial differentiation at fixed $q$,

$$
B_s=b'(s).
$$

The $q$ terms cancel:

$$
\frac12kq
-
k\left(
\frac12q+b
\right)
=
-kb.
$$

Thus

$$
\boxed{
P_z
=
-\bigl(b'+kb\bigr)
+
2M_a(s)z,
}
\tag{5.1}
$$

where

$$
\boxed{
M_a
=
a'+a-2a^2.
}
\tag{5.2}
$$

Therefore:

$$
\boxed{
\nabla_hP_z=0,
}
\tag{5.3}
$$

and

$$
\boxed{
P_{zz}
=
2M_a(s).
}
\tag{5.4}
$$

The pressure separates in the normal direction:

$$
\boxed{
P(y_h,z,s)
=
P_h(y_h,s)
+
M_a(s)z^2
-
\bigl(b'+kb\bigr)z
+
P_0(s).
}
\tag{5.5}
$$

This is an exact central-mode pressure constraint.

---

# 6. Automatic mixed X72 invisibility

Define the X72 affine pressure-response defect

$$
\boxed{
E_p
=
H_P^0+C_S^0.
}
\tag{6.1}
$$

DCRP49 proved

$$
(E_p)_{hn}
=
-(D_sc)p
+
\left(c-\frac12\right)(H+dI)p.
$$

On the central branch,

$$
D_sc=0,
$$

and

$$
c-\frac12=0.
$$

Therefore

$$
\boxed{
(E_p)_{hn}=0.
}
\tag{6.2}
$$

This vanishing is exact and requires no pressure-response assumption.

The central response is therefore invisible to the **two mixed components** of the X72 affine pressure-response defect.

---

# 7. Remaining local strain blocks

The local symmetric strain is

$$
\boxed{
S
=
\begin{pmatrix}
H&0\\
0&d
\end{pmatrix},
}
\tag{7.1}
$$

where

$$
\boxed{
H=D_h^2\phi,
}
\tag{7.2}
$$

and

$$
\boxed{
d=\frac12q_z-2a.
}
\tag{7.3}
$$

Incompressibility gives

$$
\boxed{
\operatorname{tr}H=-d.
}
\tag{7.4}
$$

The planar vorticity is

$$
\boxed{
\Omega_h=J\nabla_hq.
}
\tag{7.5}
$$

Let

$$
\boxed{
m:=|\Omega_h|^2=|\nabla_hq|^2.
}
\tag{7.6}
$$

---

# 8. Pressure Poisson source

On the central branch DCRP48's pressure source becomes

$$
\boxed{
-\Delta P
=
|H|_F^2+d^2-\frac12m.
}
\tag{8.1}
$$

Equivalently,

$$
\boxed{
\Delta P
=
-|H|_F^2-d^2+\frac12m.
}
\tag{8.2}
$$

---

# 9. Remaining X72 normal defect

The normal-normal component of

$$
H_P^0
$$

is

$$
P_{zz}-\frac{\Delta P}{3}.
$$

The normal-normal component of

$$
C_S^0
$$

is

$$
d^2-\frac{|H|^2+d^2}{3}.
$$

Adding and using (8.2) gives the exact cancellation

$$
\boxed{
(E_p)_{nn}
=
P_{zz}
+
d^2
-
\frac16m.
}
\tag{9.1}
$$

Define

$$
\boxed{
e_n
:=
P_{zz}+d^2-\frac16m.
}
\tag{9.2}
$$

Using (5.4) and (7.3),

$$
\boxed{
e_n
=
2(a'+a-2a^2)
+
\left(
\frac12q_z-2a
\right)^2
-
\frac16|\nabla_hq|^2.
}
\tag{9.3}
$$

An expanded form is

$$
\boxed{
e_n
=
2(a'+a)
-
2aq_z
+
\frac14q_z^2
-
\frac16|\nabla_hq|^2.
}
\tag{9.4}
$$

This is the first surviving pressure-response coordinate.

---

# 10. Remaining planar traceless defect

Let

$$
H^0
=
H-\frac12(\operatorname{tr}H)I_2.
$$

For every symmetric $2\times2$ matrix,

$$
\boxed{
(H^2)^0
=
(\operatorname{tr}H)H^0.
}
\tag{10.1}
$$

Since

$$
\operatorname{tr}H=-d,
$$

$$
\boxed{
(H^2)^0
=
-dH^0.
}
\tag{10.2}
$$

The planar trace-free part of $C_S^0$ is therefore

$$
-dH^0.
$$

Hence:

$$
\boxed{
(E_p)_{hh}^0
=
(D_h^2P)^0
-
dH^0.
}
\tag{10.3}
$$

Define

$$
\boxed{
T_h
:=
(D_h^2P)^0-dH^0.
}
\tag{10.4}
$$

This is a two-dimensional trace-free planar tensor.

---

# 11. Exact three-component defect decomposition

The full defect $E_p$ is symmetric and trace free.

On the central branch its mixed block vanishes.

Therefore its planar block has trace

$$
-e_n.
$$

Thus

$$
\boxed{
(E_p)_{hh}
=
T_h-\frac12e_nI_2.
}
\tag{11.1}
$$

The full tensor is

$$
\boxed{
E_p
=
\begin{pmatrix}
T_h-\frac12e_nI_2&0\\
0&e_n
\end{pmatrix}.
}
\tag{11.2}
$$

Since $T_h$ is trace free and orthogonal to $I_2$,

$$
\boxed{
|E_p|_F^2
=
|T_h|_F^2
+
\frac32e_n^2.
}
\tag{11.3}
$$

## Theorem D50.2 — Central X72 Defect Compression

The central $c=1/2$ mode automatically removes the two mixed components of the five-dimensional affine pressure-response defect.

The remaining X72 pressure-realizability defect is exactly the three-component pair

$$
\boxed{
(T_h,e_n).
}
$$

Thus the “cofactor-invisible” central mode is not fully pressure-invisible.

---

# 12. Perfect central pressure-response system

Assume now the full X72 affine pressure response is perfect:

$$
\boxed{
E_p=0.
}
\tag{12.1}
$$

By Theorem D50.2,

$$
\boxed{
e_n=0,
}
\tag{12.2}
$$

and

$$
\boxed{
T_h=0.
}
\tag{12.3}
$$

The normal equation gives

$$
\boxed{
|\nabla_hq|^2
=
6
\left[
P_{zz}+d^2
\right].
}
\tag{12.4}
$$

Using

$$
P_{zz}=2(a'+a-2a^2)
$$

and

$$
d=\frac12(q_z-4a),
$$

we obtain:

## Theorem D50.3 — Central Perfect-Response Pseudo-Eikonal Constraint

A central fully flat perfect-pressure-response patch satisfies

$$
\boxed{
|\nabla_hq|^2
-
\frac32(q_z-4a)^2
=
12(a'+a-2a^2).
}
\tag{12.5}
$$

Together with Theorem D50.1,

$$
\boxed{
q_{zz}=\Delta_hq.
}
\tag{12.6}
$$

The planar defect equation is

$$
\boxed{
(D_h^2P)^0
=
dH^0.
}
\tag{12.7}
$$

Thus the central perfect-response branch is reduced to a nonlinear **wave–pseudo-eikonal pressure-realizability system**.

---

# 13. DCRP41 pointwise canonical pancake tensor

For a fixed plane,

$$
n'=0.
$$

DCRP41's zero-shape canonical affine tensor is

$$
\boxed{
A_{\rm pan}
=
a(s)
\left(
P_h-2n\otimes n
\right).
}
\tag{13.1}
$$

In the coordinates $n=e_3$,

$$
\boxed{
A_{\rm pan}
=
\operatorname{diag}
(a,a,-2a).
}
\tag{13.2}
$$

DCRP38 decomposes the actual local strain as

$$
\boxed{
S
=
A_{\rm pan}
+
E,
}
\tag{13.3}
$$

where $E$ is the non-affine strain residual.

DCRP50 now asks whether the strongest possible equality

$$
\boxed{
E\equiv0
}
\tag{13.4}
$$

can coexist with a nonzero central flat vorticity patch.

---

# 14. Central non-affine residual identities

On the central branch the actual strain has no cross block:

$$
S_{hn}=0.
$$

The canonical tensor also has no cross block.

Therefore

$$
\boxed{
E_{hn}=0.
}
\tag{14.1}
$$

The normal residual is

$$
\begin{aligned}
E_{nn}
&=
d-(-2a)
\\
&=
\frac12q_z.
\end{aligned}
$$

Hence

$$
\boxed{
E_{nn}
=
\frac12q_z.
}
\tag{14.2}
$$

The planar residual is

$$
\boxed{
E_{hh}
=
H-aI_2.
}
\tag{14.3}
$$

Differentiate (14.3) in $z$.

Because $a=a(s)$,

$$
\partial_zE_{hh}
=
\partial_zH.
$$

But

$$
H=D_h^2\phi
$$

and

$$
\phi_z
=
-\frac12q+b-2az.
$$

Therefore

$$
\boxed{
\partial_zE_{hh}
=
-\frac12D_h^2q.
}
\tag{14.4}
$$

These exact identities show that the normal derivative and horizontal curvature of the central scalar are encoded directly by the non-affine strain residual.

---

# 15. Exact affine central subbranch

Assume on a connected open central flat patch

$$
\boxed{
E=0.
}
\tag{15.1}
$$

Then from (14.2),

$$
\boxed{
q_z=0.
}
\tag{15.2}
$$

From (14.4),

$$
\boxed{
D_h^2q=0.
}
\tag{15.3}
$$

Therefore

$$
\boxed{
q(y,s)
=
K(s)\cdot y_h+g(s).
}
\tag{15.4}
$$

The scalar gauge can absorb the purely time-dependent $g(s)$ if desired.

The planar vorticity is spatially constant:

$$
\boxed{
\Omega_h=JK(s).
}
\tag{15.5}
$$

---

# 16. Exact local velocity under $E=0$

Since

$$
H=aI_2,
$$

$$
\nabla_hV_h=aI_2.
$$

Also from the central cross relation,

$$
\partial_zV_h
=
-\frac12\nabla_hq
=
-\frac12K(s).
$$

Therefore locally

$$
\boxed{
V_h
=
a(s)y_h
-
\frac12zK(s)
+
U_0(s),
}
\tag{16.1}
$$

where $U_0(s)$ is a horizontal translation.

Likewise

$$
\boxed{
w
=
\frac12K(s)\cdot y_h
+
b_0(s)
-
2a(s)z.
}
\tag{16.2}
$$

This is the exact central affine shear + canonical pancake strain geometry.

---

# 17. Scalar transport kills the affine central vorticity

The canonical scalar satisfies

$$
\boxed{
D_sq+k(s)q=0.
}
\tag{17.1}
$$

Because

$$
q_z=0,
$$

the normal transport term vanishes.

Using (15.4) and (16.1),

$$
\begin{aligned}
D_sq
={}&
K'\cdot y_h
+
g'
\\
&+
\left[
(\gamma+a)y_h
-\frac12zK
+U_0
\right]\cdot K.
\end{aligned}
$$

The only term proportional to $z$ is

$$
\boxed{
-\frac12z|K|^2.
}
\tag{17.2}
$$

Neither $q_s$ nor $kq$ contains a $z$ term because $q_z=0$.

Therefore the scalar equation can hold on an open $z$ interval only if

$$
\boxed{
|K|^2=0.
}
\tag{17.3}
$$

Hence

$$
\boxed{
K=0.
}
\tag{17.4}
$$

and therefore

$$
\boxed{
\Omega_h=0.
}
\tag{17.5}
$$

---

# Theorem D50.4 — Exact-Affine Central Pancake NO-GO

A regular fully flat central-response patch with

$$
\boxed{
c=\frac12
}
$$

and pointwise actual strain equal to the DCRP41 canonical fixed-plane pancake tensor

$$
\boxed{
S=A_{\rm pan}
}
$$

cannot carry nonzero rank-two vorticity.

Equivalently:

$$
\boxed{
c=\frac12,
\quad
\Omega_h\neq0
\quad\Longrightarrow\quad
S\neq A_{\rm pan}
}
$$

on every open active patch.

This result:

- is local;
- does not use periodicity;
- does not use finite-energy assumptions;
- does not use the X72 pressure-response defect;
- does not use PFET.

The obstruction is the nonlinear self-advection of the central antisymmetric cross shear.

---

# 18. Consequence for the DCRP38 equality route

DCRP38 writes

$$
S=A_{\rm pan}+E.
$$

Theorem D50.4 proves that on every nonzero central active patch,

$$
\boxed{
E\not\equiv0.
}
\tag{18.1}
$$

Thus the central invisible mode cannot be the strongest pointwise affine/no-residual pancake state.

However DCRP38's covariance residual is an **integrated** quantity:

$$
R_B^{na}
=
\int
\phi
\left[
EC_\Omega+C_\Omega E
\right].
$$

Pointwise

$$
E\neq0
$$

does not automatically imply

$$
R_B^{na}\neq0.
$$

The residual may remain hidden through:

- tensor annihilation on the vorticity direction;
- sign/phase cancellation;
- core-window turnover.

Therefore D50 closes the pure pointwise-affine branch but does not yet close every covariance-zero central branch.

---

# 19. New central residual variable

Define the pointwise central non-affinity density

$$
\boxed{
\mathfrak R_c
=
|E_{hh}|_F^2
+
\frac14q_z^2.
}
\tag{19.1}
$$

Because

$$
E_{hn}=0
$$

and

$$
E_{nn}=q_z/2,
$$

this is simply

$$
\boxed{
\mathfrak R_c
=
|E|_F^2.
}
\tag{19.2}
$$

On a nonzero central active patch Theorem D50.4 gives

$$
\boxed{
\mathfrak R_c\not\equiv0.
}
\tag{19.3}
$$

Thus a new exact branch split is available:

$$
\boxed{
\text{visible non-affine residual}
}
$$

versus

$$
\boxed{
\text{non-affinity hidden from the covariance observer by cancellation/turnover}.
}
$$

This is an NTLA-O distinction between pointwise structure and integrated covariance identity.

---

# 20. Perfect-pressure central branch with unavoidable non-affinity

Suppose simultaneously

$$
\boxed{
E_p=0
}
$$

and

$$
\boxed{
\Omega_h\neq0.
}
$$

Then Theorem D50.4 forces

$$
\boxed{
E\neq0,
}
$$

while Theorem D50.3 forces

$$
\boxed{
q_{zz}=\Delta_hq,
}
$$

$$
\boxed{
|\nabla_hq|^2
-
\frac32(q_z-4a)^2
=
12(a'+a-2a^2).
}
$$

Therefore the perfect-response central survivor cannot be the obvious affine shear+pancake model.

It must be genuinely nonlinear/non-affine.

This is substantially sharper than the generic X72 statement that perfect affine response has local witnesses.

---

# 21. Remaining pressure-response geometry

The central branch has already removed

$$
(E_p)_{hn}.
$$

The three remaining coordinates are:

### normal scalar

$$
e_n;
$$

### planar quadrupole

$$
T_h\in\mathrm{Sym}_0(2).
$$

The perfect-response route requires both to vanish.

If either is nonzero, the central branch immediately enters the X72 Round37 pressure-response defect channel.

Thus:

$$
\boxed{
\text{central mode}
}
$$

splits into

$$
\boxed{
E_p^{(3)}\neq0
}
$$

or

$$
\boxed{
E_p^{(3)}=0
\text{ and wave–pseudo-eikonal realizability}.
}
$$

---

# 22. Constant-slope whole-space calibration

The central response is the constant slope

$$
c=\frac12.
$$

DCRP47's constant-slope spatial equation becomes

$$
\boxed{
q_{zz}-\Delta_hq=0.
}
\tag{22.1}
$$

Its Fourier characteristic cone is

$$
\boxed{
\xi_z^2=|\xi_h|^2.
}
\tag{22.2}
$$

A whole-space $L^2$ solution must vanish because its Fourier transform would be supported on a measure-zero cone.

Therefore any nonzero global central mode must be:

- non-$L^2$ in the normalized variables;
- boundary-fed;
- distributional;
- or only local.

This is compatible with the already-known DCRP critical-tail necessity and does not by itself contradict the DSS limit.

---

# 23. Why the exact Euler pancake calibration does not reopen the closed branch

Known exact Euler pancake constructions combine shear and asymmetric strain and show that thin pancake vorticity geometry is locally realizable.

DCRP50 does not claim generic pancake geometry is impossible.

Theorem D50.4 concerns the much narrower simultaneous conditions:

1. fixed rank-two plane;
2. DCRP44 flat scalar connection;
3. central response $c=1/2$;
4. DCRP41 pointwise canonical strain
   $$
   S=A_{\rm pan};
   $$
5. nonzero planar vorticity.

Those five conditions are incompatible.

Thus the external exact pancake examples serve as calibration rather than counterexamples: a surviving exact model must use additional non-affine structure absent from the pointwise canonical central equality jet.

---

# 24. NTLA-O interpretation

DCRP49's mixed observer could not see the central response because

$$
(E_p)_{hn}=0.
$$

A finer observer resolves the remaining pressure defect into

$$
\boxed{
(T_h,e_n).
}
$$

A second observer compares actual strain with the canonical DCRP41 affine tensor:

$$
\boxed{
E=S-A_{\rm pan}.
}
$$

The apparent “invisible direction” therefore decomposes as

$$
\boxed{
\text{mixed invisible}
\rightarrow
\text{three-component pressure visibility}
+
\text{pointwise non-affine visibility}.
}
$$

The central mode is not actually structureless.

It was invisible only at the previous observer resolution.

This is exactly the NTLA-O refinement mechanism.

---

# 25. Updated final rank-two survivor

After DCRP50, an active central survivor must satisfy at least one branch of

$$
\boxed{
\begin{aligned}
&
\text{nonzero pointwise non-affine strain residual}
\\
&\vee
\\
&
\text{covariance/core turnover hiding that residual}
\\
&\vee
\\
&
\text{nonzero three-component X72 pressure-response defect}
\\
&\vee
\\
&
\text{perfect-response nonlinear central realizability system}.
\end{aligned}
}
$$

The pure pointwise canonical affine central pancake branch is gone.

The maximally rigid branch is now:

$$
\boxed{
\begin{gathered}
c=\frac12,
\\
E_p=0,
\\
E\neq0,
\\
q_{zz}=\Delta_hq,
\\
|\nabla_hq|^2
-\frac32(q_z-4a)^2
=
12(a'+a-2a^2),
\\
(D_h^2P)^0=dH^0,
\\
D_sq+kq=0.
\end{gathered}
}
$$

This is a sharply constrained nonlinear realizability problem.

---

# 26. Status ledger

## PROVED this round

### D50-P1 — Central constitutive reduction

$$
w=\frac12q+b-2az.
$$

### D50-P2 — Central spatial wave identity

$$
q_{zz}=\Delta_hq.
$$

### D50-P3 — Mixed pressure Hessian vanishes

$$
\nabla_hP_z=0.
$$

### D50-P4 — Central pressure-response defect compression

$$
|E_p|^2
=
|T_h|^2+\frac32e_n^2.
$$

### D50-P5 — Perfect-response pseudo-eikonal constraint

$$
|\nabla_hq|^2
-
\frac32(q_z-4a)^2
=
12(a'+a-2a^2).
$$

### D50-P6 — Central non-affine residual identities

$$
E_{nn}=\frac12q_z,
$$

$$
\partial_zE_{hh}
=
-\frac12D_h^2q.
$$

### D50-P7 — Exact-affine central pancake NO-GO

If

$$
S=A_{\rm pan}
$$

on an open central flat patch, then

$$
\Omega_h=0.
$$

Therefore every active central branch requires non-affine strain.

---

# 27. Corrected / closed routes

## Closed

$$
\boxed{
\text{central }c=\frac12
+
\text{pointwise canonical affine pancake}
+
\text{nonzero planar vorticity}
}
$$

is impossible.

## Not closed

Pointwise non-affine strain may still have zero integrated DCRP38 covariance residual through cancellation.

## Not closed

The perfect-response nonlinear wave–pseudo-eikonal system has not yet been classified.

---

# 28. New STOP

$$
\boxed{
\textbf{
STOP-D50:
The unique mixed-cofactor-invisible central response cannot realize the pointwise canonical affine pancake jet with nonzero vorticity. Every active central survivor must carry non-affine strain, turnover/cancellation, a remaining three-component pressure-response defect, or solve the fully nonlinear perfect-response wave–pseudo-eikonal system.
}
}
$$

---

# 29. Next autonomous step

## DCRP51 — Central Wave–Pseudo-Eikonal Rigidity

**Working title**

> **Central Perfect-Response Realizability: Wave–Eikonal Intersection, Non-Affine Strain, and Critical-Tail Escape**

Primary tasks:

1. analyze the simultaneous system
   $$
   q_{zz}=\Delta_hq,
   $$
   $$
   |\nabla_hq|^2-\frac32(q_z-4a)^2=C(s);
   $$
2. determine whether smooth connected solutions must be affine under any natural boundedness / local compactness / tail condition;
3. if affine rigidity holds, D50 immediately kills the perfect-response central branch;
4. if nonlinear solutions exist, classify their characteristic geometry and feed them to the X72 vorticity-stress realizability tower;
5. quantify how much non-affine strain residual is required if the wave–pseudo-eikonal branch survives.

Desired endpoint:

$$
\boxed{
\text{affine rigidity and contradiction}
\ \vee\
\text{nonlinear characteristic model}
\ \vee\
\text{critical-tail escape}
\ \vee\
\text{X72 realizability handoff}.
}
$$

---

# 30. One-line checkpoint

The final mixed-invisible $c=1/2$ pancake is not actually an affine escape: exact canonical affine strain forces its vorticity to vanish, while full pressure lock reduces every remaining central survivor to a three-component X72 defect or a nonlinear wave–pseudo-eikonal realizability problem with mandatory non-affine strain.

---

**End checkpoint:** DCRP50  
**Next:** DCRP51 — Central Wave–Pseudo-Eikonal Rigidity.
