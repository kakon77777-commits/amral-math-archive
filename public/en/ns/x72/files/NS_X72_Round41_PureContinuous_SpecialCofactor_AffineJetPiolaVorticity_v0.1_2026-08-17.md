# NS × X Integral × 24/72 Paradigm in Practice
## Round 41 — Pure Continuous Special-Cofactor Commutator / Affine-Jet Cancellation and Piola–Vorticity Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Special-Cofactor Branch
- Canonical source: UTF-8 Markdown
- Canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round40_PureContinuous_HardyBMO_DualCommutator_v0.1_2026-08-17.md`
- Current round objective: Round 40 compressed the Hardy–BMO dual route into a special cofactor commutator
  $$
  \mathcal A_C
  =
  [u\cdot\nabla,\mathcal T_0^\ast]C,
  \qquad
  C=S^2-\frac13|S|^2I.
  $$
  This round no longer treats $C$ as an arbitrary tensor, but utilizes:
  - centered parity;
  - incompressibility;
  - cofactor quadratic algebra;
  - Piola null-Lagrangian identity;
  to seek additional cancellations invisible to generic CRW/BMO estimates.
- Non-claims: This document does not prove the closure of the Hardy–BMO endpoint. This document proves:
  1. exact cancellation of the leading affine first-increment interaction;
  2. the second-jet curvature contribution of the generic rotational branch can be nonzero, hence no universal third-order cancellation exists;
  3. the nonlocal scalar projection of the special cofactor can be exactly decomposed into a local pressure-source part + a vorticity-stress Piola defect;
  4. the fractional critical endpoint still requires a Zygmund/Campanato gain.

---

# 0. Round 40 handoff

Round 40 reduced the transport–Riesz defect pairing to:

$$
\boxed{
\langle
E,
[D_u,\mathcal T_0]q
\rangle
=
\langle
\mathcal A_C,
q
\rangle,
}
\tag{0.1}
$$

where:

$$
\boxed{
\mathcal A_C
=
[D_u,\mathcal T_0^\ast]C,
}
\tag{0.2}
$$

$$
\boxed{
C
=
S^2-\frac13|S|^2I.
}
\tag{0.3}
$$

and:

$$
\boxed{
\|q\|_{\mathcal H^1}
\lesssim
\|\nabla u\|_2^2.
}
\tag{0.4}
$$

Thus, the Hardy side can be paid by the energy/enstrophy level.

Leaving:

$$
\boxed{
\mathcal A_C
\stackrel{?}{\in}
\mathrm{BMO}.
}
$$

The generic two-increment kernel from Round 40:

$$
\boxed{
\mathcal A_C(x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
:
[
C(y)-C(x)
]
dy.
}
\tag{0.5}
$$

naive fractional threshold:

$$
\boxed{
s_u+s_C=1.
}
$$

Round 40 STOP:

$$
\boxed{
\text{STOP-C44}
=
\text{Hardy–BMO Transfer / Two-Increment BMO Endpoint Gap}.
}
$$

---

# 1. Centered first and second differences

Let:

$$
z\in\mathbb R^3.
$$

Define the centered first difference:

$$
\boxed{
D_zf(x)
=
\frac{
f(x+z)-f(x-z)
}{2}.
}
\tag{1.1}
$$

Define the centered second difference:

$$
\boxed{
\Delta_z^2f(x)
=
f(x+z)-2f(x)+f(x-z).
}
\tag{1.2}
$$

Furthermore:

$$
\Delta_z^+f
=
f(x+z)-f(x),
$$

$$
\Delta_z^-f
=
f(x)-f(x-z).
$$

Then:

$$
\boxed{
\Delta_z^+f+\Delta_z^-f
=
2D_zf,
}
\tag{1.3}
$$

$$
\boxed{
\Delta_z^+f-\Delta_z^-f
=
\Delta_z^2f.
}
\tag{1.4}
$$

---

# 2. Exact centered symmetrization of the cofactor commutator

Since:

$$
K_0(-z)=K_0(z),
$$

we have:

$$
\nabla K_0(-z)
=
-\nabla K_0(z).
$$

Expressing (0.5) using:

$$
y=x-z
$$

and averaging over:

$$
z
\leftrightarrow
-z,
$$

yields the exact:

$$
\boxed{
\begin{aligned}
\mathcal A_C(x)
=
\frac12
\operatorname{p.v.}
\int
&
\left[
D_zu(x)
\cdot
\nabla K_0(z)
\right]
:
\Delta_z^2C(x)
\,dz
\\
+
\frac12
\operatorname{p.v.}
\int
&
\left[
\Delta_z^2u(x)
\cdot
\nabla K_0(z)
\right]
:
D_zC(x)
\,dz.
\end{aligned}
}
\tag{2.1}
$$

Named:

$$
\boxed{
\textbf{Centered Cofactor-Commutator Identity}.
}
$$

---

# 3. Affine-jet cancellation

If:

$$
u
$$

and:

$$
C
$$

are both affine in a neighborhood,

then:

$$
\Delta_z^2u=0,
$$

$$
\Delta_z^2C=0.
$$

Thus:

$$
\boxed{
\mathcal A_C^{\rm local}=0.
}
\tag{3.1}
$$

For the actual NS cofactor, the result is stronger:

If:

$$
u(x)=Ax+b
$$

is affine,

then:

$$
S=\operatorname{sym}A
$$

is constant,

hence:

$$
C
$$

is constant,

so the commutator local contribution exactly vanishes.

Therefore, the leading affine jet of the naive:

$$
\delta u
\times
\delta C
$$

first-first interaction from Round 40 does not actually exist.

---

# 4. Smooth local order gains one radial power

If:

$$
u,C\in C^2
$$

near:

$$
x,
$$

then:

$$
\boxed{
|D_zu|
\lesssim
|z|
\|\nabla u\|_{\infty,\rm loc},
}
\tag{4.1}
$$

$$
\boxed{
|\Delta_z^2u|
\lesssim
|z|^2
\|\nabla^2u\|_{\infty,\rm loc},
}
\tag{4.2}
$$

and similar estimates hold for:

$$
C.
$$

From:

$$
|\nabla K_0(z)|
\lesssim
|z|^{-4},
$$

and the 3D volume element:

$$
dz
\sim
r^2drd\Omega,
$$

we obtain:

$$
\boxed{
\begin{aligned}
|\mathcal A_C^{<\ell}(x)|
\lesssim{}&
\int_0^\ell
r
\Big[
\|\nabla u\|_{\infty,\rm loc}
\|\nabla^2C\|_{\infty,\rm loc}
\\
&+
\|\nabla^2u\|_{\infty,\rm loc}
\|\nabla C\|_{\infty,\rm loc}
\Big]dr.
\end{aligned}
}
\tag{4.3}
$$

Thus:

$$
\boxed{
|\mathcal A_C^{<\ell}(x)|
=
O(\ell^2)
}
\tag{4.4}
$$

at smooth points.

This is better than the logarithmic first-jet counting of the raw:

$$
\delta u\delta C|z|^{-4}
$$

picture.

---

# 5. Affine cancellation is not automatically fractional gain

Define the first modulus:

$$
\boxed{
\omega_f^{(1)}(r)
=
\sup_{|z|\le r}
\|D_zf\|.
}
\tag{5.1}
$$

and the second modulus:

$$
\boxed{
\omega_f^{(2)}(r)
=
\sup_{|z|\le r}
\|\Delta_z^2f\|.
}
\tag{5.2}
$$

From (2.1), the near field is controlled by:

$$
\boxed{
\mathfrak Z_{u,C}(\ell)
=
\int_0^\ell
\frac{
\omega_u^{(1)}(r)
\omega_C^{(2)}(r)
+
\omega_u^{(2)}(r)
\omega_C^{(1)}(r)
}{
r^2
}
dr.
}
\tag{5.3}
$$

If:

$$
0<s<1,
$$

under general Hölder/Besov regularity:

$$
\omega_f^{(1)}(r)
\sim
r^s,
$$

and the second difference still only has:

$$
\omega_f^{(2)}(r)
\sim
r^s.
$$

Thus:

$$
\boxed{
s_u+s_C>1
}
\tag{5.4}
$$

remains the generic fractional absolute-convergence threshold.

Therefore:

$$
\boxed{
\textbf{
affine-jet cancellation improves smooth-jet order,
but does not automatically move the fractional critical line.
}
}
\tag{5.5}
$$

---

# 6. Zygmund/little-Campanato interpretation

When a field has one full derivative but the endpoint remains critical,

the second difference is better than the first difference at capturing:

$$
\boxed{
\text{departure from affine behavior}.
}
$$

For example, if:

$$
\nabla f
$$

is uniformly continuous,

then:

$$
\boxed{
|\Delta_z^2f(x)|
\le
|z|
\omega_{\nabla f}(2|z|).
}
\tag{6.1}
$$

Thus, the endpoint gain in (5.3) can be provided by:

- little-Zygmund;
- VMO-gradient;
- Campanato affine-defect;
- Dini gradient modulus;

Therefore, the BMO endpoint from Round 40 should be more precisely rewritten as:

$$
\boxed{
\textbf{critical affine-defect / Zygmund endpoint},
}
$$

rather than a simple first-difference Hölder endpoint.

---

# 7. Exact centered cofactor algebra

Let:

$$
S_0=S(x),
$$

$$
A_z
=
D_zS(x),
$$

$$
B_z
=
\frac12
\Delta_z^2S(x).
$$

Define the linearized cofactor map:

$$
\boxed{
L_S(H)
=
SH+HS
-
\frac23
(S:H)I.
}
\tag{7.1}
$$

and the quadratic trace-free map:

$$
\boxed{
Q(H)
=
H^2
-
\frac13|H|^2I.
}
\tag{7.2}
$$

Since:

$$
C(S)=Q(S),
$$

we have the exact:

$$
\boxed{
D_zC
=
L_{S_0}(A_z)
+
A_zB_z
+
B_zA_z
-
\frac23
(A_z:B_z)I.
}
\tag{7.3}
$$

and:

$$
\boxed{
\Delta_z^2C
=
L_{S_0}(\Delta_z^2S)
+
2Q(A_z)
+
\frac12
Q(\Delta_z^2S).
}
\tag{7.4}
$$

This is the second core identity of this round.

---

# 8. What the cofactor special structure actually buys

Equation (7.4) shows that:

$$
\Delta_z^2C
$$

is not a generic second difference.

It consists of:

1. strain affine-defect:
   $$
   L_S(\Delta_z^2S);
   $$

2. quadratic first-strain increment:
   $$
   2Q(D_zS);
   $$

3. quadratic second-strain increment:
   $$
   \frac12Q(\Delta_z^2S);
   $$

Thus, when the strain is near-affine:

$$
\Delta_z^2S\approx0
$$

the dominant cofactor curvature is:

$$
\boxed{
\Delta_z^2C
\approx
2Q(D_zS).
}
\tag{8.1}
$$

Namely:

$$
\boxed{
\text{cofactor curvature}
\sim
(\text{strain increment})^2.
}
$$

This is a special quadratic gain absent in generic tensors.

---

# 9. But the first centered cofactor still contains one strain increment

The leading term of Equation (7.3) is:

$$
\boxed{
D_zC
=
L_S(D_zS)
+
\text{higher order}.
}
\tag{9.1}
$$

Therefore, the second term in (2.1):

$$
\Delta_z^2u
\cdot
\nabla K_0
:
D_zC
$$

can still carry:

$$
\boxed{
\text{velocity affine-defect}
\times
\text{one strain increment}.
}
$$

Thus, the cofactor quadraticity does not automatically elevate the entire commutator to a two-strain-increment order.

---

# 10. Piola decomposition of the cofactor

Let the full velocity gradient be:

$$
A
=
\nabla u.
$$

Decompose:

$$
\boxed{
A
=
S+\Omega,
}
\tag{10.1}
$$

where:

$$
S^\top=S,
$$

$$
\Omega^\top=-\Omega.
$$

incompressibility:

$$
\operatorname{tr}A=0.
$$

For a general trace-free:

$$
A,
$$

the cofactor formula is:

$$
\boxed{
\operatorname{cof}A
=
(A^\top)^2
-
\frac12
\operatorname{tr}(A^2)I.
}
\tag{10.2}
$$

Therefore:

$$
\boxed{
\operatorname{cof}S
-
\operatorname{cof}A
=
S\Omega
+
\Omega S
-
\Omega^2
+
\frac12
\operatorname{tr}(\Omega^2)I.
}
\tag{10.3}
$$

---

# 11. Vorticity simplification

For:

$$
\Omega_{ij}
=
-\frac12
\varepsilon_{ijk}\omega_k,
$$

we have:

$$
\boxed{
\Omega^2
=
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
),
}
\tag{11.1}
$$

and:

$$
\boxed{
\operatorname{tr}(\Omega^2)
=
-\frac12|\omega|^2.
}
\tag{11.2}
$$

Thus:

$$
\boxed{
-\Omega^2
+
\frac12
\operatorname{tr}(\Omega^2)I
=
-\frac14
\omega\otimes\omega.
}
\tag{11.3}
$$

Therefore, the trace-free cofactor:

$$
C
=
\operatorname{cof}S
+
\frac16|S|^2I
$$

can be written as:

$$
\boxed{
C
=
\operatorname{cof}\nabla u
+
S\Omega
+
\Omega S
-
\frac14
\omega\otimes\omega
+
\frac16
|S|^2I.
}
\tag{11.4}
$$

Named:

$$
\boxed{
\textbf{Piola–Vorticity Cofactor Decomposition}.
}
$$

---

# 12. Piola null-Lagrangian cancellation

The classical Piola identity:

$$
\boxed{
\operatorname{div}
\operatorname{cof}\nabla u
=
0
}
\tag{12.1}
$$

for smooth maps.

Furthermore:

$$
S\Omega+\Omega S
$$

is skew-symmetric,

so:

$$
\boxed{
\partial_i\partial_j
(S\Omega+\Omega S)_{ij}
=
0.
}
\tag{12.2}
$$

Therefore, the double divergence of:

$$
C
$$

reduces to:

$$
\boxed{
\partial_i\partial_jC_{ij}
=
-\frac14
\partial_i\partial_j
(
\omega_i\omega_j
)
+
\frac16
\Delta|S|^2.
}
\tag{12.3}
$$

This is the strongest exact null-Lagrangian reduction of the cofactor special structure.

---

# 13. Scalar Riesz projection of the cofactor

Since:

$$
C
$$

is trace-free,

$$
\mathcal T_0^\ast C
=
\partial_i\partial_j
(-\Delta)^{-1}
C_{ij}.
$$

From (12.3):

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16
|S|^2
-
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
\tag{13.1}
$$

where:

$$
\mathcal R_i\mathcal R_j
=
\partial_i\partial_j(-\Delta)^{-1}.
$$

Also:

$$
q
=
|S|^2-\frac12|\omega|^2,
$$

Thus:

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\frac1{12}
|\omega|^2
-
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
\tag{13.2}
$$

Named:

$$
\boxed{
\textbf{Piola–Vorticity Projection Identity}.
}
$$

---

# 14. Irrotational branch

If:

$$
\omega=0,
$$

then:

$$
A=S=\nabla u.
$$

The Piola–Vorticity Projection Identity degenerates to:

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16
q
=
-\frac16|S|^2.
}
\tag{14.1}
$$

Thus, in the irrotational incompressible branch,

the nonlocal scalar projection of the cofactor actually reduces to a local scalar.

This is a genuine null-Lagrangian depletion.

However, the full 3D NS generally has:

$$
\omega\ne0.
$$

Thus:

$$
\boxed{
\text{vorticity stress is the obstruction to exact Piola locality}.
}
\tag{14.2}
$$

---

# 15. Irrotational harmonic second-jet depletion witness

Take the harmonic potential:

$$
\boxed{
\begin{aligned}
\phi(x)
={}&
-\frac12x_1^2
-\frac12x_2^2
+
x_3^2
\\
&+
x_1^3
-
3x_1x_2^2.
\end{aligned}
}
\tag{15.1}
$$

Let:

$$
u=\nabla\phi.
$$

Then:

$$
\nabla\cdot u
=
\Delta\phi
=
0,
$$

and:

$$
\omega=0.
$$

At:

$$
x=0,
$$

$$
S_0
=
\operatorname{diag}
(-1,-1,2).
$$

A direct spherical jet calculation shows:

$$
\boxed{
\text{the leading centered second-jet shell coefficient of }
\mathcal A_C
\text{ vanishes}.
}
\tag{15.2}
$$

This is consistent with the Piola null-Lagrangian depletion.

This witness does not claim that all irrotational higher jets vanish entirely.

---

# 16. Generic rotational second-jet sharpness witness

Now take the divergence-free polynomial field from Round 35:

$$
\boxed{
\begin{aligned}
u_1
&=
-x_1
+
\frac12x_1^2
+
\frac12x_2^2,
\\
u_2
&=
-(1+x_1)x_2,
\\
u_3
&=
2x_3.
\end{aligned}
}
\tag{16.1}
$$

Then:

$$
\nabla\cdot u=0,
$$

and:

$$
\boxed{
S
=
\operatorname{diag}
(
-1+x_1,
-1-x_1,
2
).
}
\tag{16.2}
$$

At:

$$
x=0,
$$

$$
S_0
=
\operatorname{diag}
(-1,-1,2),
$$

$$
\boxed{
C_0
=
\operatorname{diag}
(-1,-1,2).
}
\tag{16.3}
$$

and:

$$
\boxed{
\partial_1C
=
\operatorname{diag}
(-2,2,0),
}
\tag{16.4}
$$

$$
\boxed{
\partial_{11}C
=
\operatorname{diag}
\left(
\frac23,
\frac23,
-\frac43
\right).
}
\tag{16.5}
$$

This field has:

$$
\boxed{
\omega
=
(0,0,-2x_2),
}
\tag{16.6}
$$

thus:

$$
\nabla\omega\ne0.
$$

---

# 17. Exact nonzero curvature shell coefficient

Adopting the standard Newtonian trace-free kernel:

$$
\boxed{
K_{0,ij}(z)
=
\frac{
3e_ie_j-\delta_{ij}
}{
4\pi r^3
},
\qquad
e=z/r.
}
\tag{17.1}
$$

Then:

$$
\boxed{
\partial_kK_{0,ij}
=
\frac3{
4\pi r^4
}
\left[
\delta_{ki}e_j
+
\delta_{kj}e_i
+
\delta_{ij}e_k
-
5e_ie_je_k
\right].
}
\tag{17.2}
$$

Substitute (16.1)–(16.5) into the Centered Cofactor-Commutator Identity.

The cubic jet angular average over the unit sphere is exactly:

$$
\boxed{
-\frac4{15}
}
\tag{17.3}
$$

after removing the kernel normalization factor.

Thus, the full radial shell coefficient is:

$$
\boxed{
-\frac45
r\,dr.
}
\tag{17.4}
$$

Therefore:

$$
\boxed{
\mathcal A_C^{\varepsilon<|z|<\ell}(0)
=
-\frac25
\left(
\ell^2-\varepsilon^2
\right)
}
\tag{17.5}
$$

under this kernel sign convention.

The most important thing is not the sign, but:

$$
\boxed{
\mathcal A_C^{\rm second\ jet}
\ne0.
}
$$

Named:

$$
\boxed{
\textbf{Second-Jet Sharpness Witness}.
}
$$

---

# 18. No universal third-order cancellation

Sections 3–4 proved:

$$
\boxed{
\text{affine first jet cancels exactly}.
}
$$

But Section 17 proved:

$$
\boxed{
\text{generic divergence-free rotational second jet can survive}.
}
$$

Thus, there is no purely algebraic universal:

$$
\boxed{
\mathcal A_C^{<\ell}
=
O(\ell^{2+\alpha})
}
\tag{18.1}
$$

for some fixed:

$$
\alpha>0
$$

based only on:

- incompressibility;
- trace-free strain;
- cofactor structure;
- kernel parity.

That is:

$$
\boxed{
\textbf{special cofactor buys exactly an affine-jet cancellation,
not a universal extra fractional derivative.}
}
\tag{18.2}
$$

---

# 19. Fractional endpoint remains sharp in the rotational branch

In the rough critical branch:

$$
0<s_u,s_C<1,
$$

centered second differences and first differences remain of the same order:

$$
r^{s_u},
\qquad
r^{s_C}.
$$

Thus:

$$
\mathfrak Z_{u,C}
$$

still requires:

$$
\boxed{
s_u+s_C>1
}
$$

for absolute local convergence.

The critical:

$$
\boxed{
s_u+s_C=1
}
$$

still requires:

- little-Zygmund;
- Campanato affine-defect;
- Dini gain;
- or additional vorticity/Piola depletion.

Thus, the Round 40 critical line remains a sharp route obstruction in the generic rotational branch.

---

# 20. Piola–Vorticity commutator resolution

Define the vorticity projection defect:

$$
\boxed{
\mathfrak V_\omega
=
\frac1{12}
|\omega|^2
+
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
\tag{20.1}
$$

From (13.2):

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\mathfrak V_\omega.
}
\tag{20.2}
$$

Round 37 cofactor equation:

$$
\boxed{
D_tC-\nu\Delta C
=
-
L_S(E)
-
2\nu Q_C
+
V_C.
}
\tag{20.3}
$$

Thus:

$$
\boxed{
\begin{aligned}
\mathcal A_C
&=
[D_u,\mathcal T_0^\ast]C
\\
&=
(D_u-\nu\Delta)
(
\mathcal T_0^\ast C
)
+
\mathcal T_0^\ast L_S(E)
+
2\nu
\mathcal T_0^\ast Q_C
-
\mathcal T_0^\ast V_C.
\end{aligned}
}
\tag{20.4}
$$

Round 37 pressure-source equation:

$$
\boxed{
(D_u-\nu\Delta)q
=
N_0
-
2S:E.
}
\tag{20.5}
$$

Therefore:

$$
\boxed{
\begin{aligned}
\mathcal A_C
={}&
-\frac16
(
N_0-2S:E
)
\\
&-
(D_u-\nu\Delta)
\mathfrak V_\omega
\\
&+
\mathcal T_0^\ast L_S(E)
+
2\nu
\mathcal T_0^\ast Q_C
-
\mathcal T_0^\ast V_C.
\end{aligned}
}
\tag{20.6}
$$

Named:

$$
\boxed{
\textbf{Piola–Vorticity Commutator Resolution}.
}
$$

---

# 21. What the Piola resolution changes

Round 40 treated:

$$
\mathcal A_C
$$

as a generic transport commutator.

Round 41 now shows:

$$
\boxed{
\text{its genuinely nonlocal special-cofactor defect
can be pushed into }
\mathfrak V_\omega,
}
$$

plus already-known:

- defect-linear terms;
- viscous cofactor gradients;
- vorticity forcing.

Thus:

$$
\boxed{
\textbf{
the special cofactor commutator is not arbitrary:
its failure to be Piola-local is vorticity-generated.
}
}
\tag{21.1}
$$

This is the most important new route compression of this round.

---

# 22. Why Piola resolution still does not close the problem

$\mathfrak V_\omega$ contains:

$$
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
$$

Therefore:

$$
(D_u-\nu\Delta)
\mathfrak V_\omega
$$

will still generate:

- vorticity stretching;
- vorticity diffusion;
- transport–Riesz commutator of vorticity stress.

So the nonlocality does not disappear.

But it is now no longer borne by:

$$
\boxed{
\text{arbitrary }C
}
$$

but rather by:

$$
\boxed{
\text{vorticity stress}
}
$$

This directly connects back to the strain–vorticity geometry of Rounds 18, 26, and 28.

---

# 23. Endpoint route map after special-cofactor reduction

The Hardy–BMO route now has three branches:

## B1 — generic rotational fractional branch

$$
\boxed{
s_u+s_C=1
}
$$

remains critical.

## B2 — near-affine smooth branch

Centered symmetrization gives:

$$
\boxed{
O(\ell^2)
}
$$

local commutator.

## B3 — Piola/low-vorticity branch

cofactor projection becomes approximately:

$$
\boxed{
\mathcal T_0^\ast C
\approx
-\frac16q,
}
$$

and the remaining nonlocality is vorticity stress.

Thus, the next proof obligation naturally becomes:

$$
\boxed{
\text{control the Piola–vorticity defect rather than generic }C\text{ BMO}.
}
$$

---

# 24. STOP-C45 — Affine-Jet Cancellation / Piola–Vorticity Endpoint Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{special\ cofactor\ commutator},
\\
\text{raw dual kernel}
&=
\delta u
\times
\delta C
\times
\nabla K_0,
\\
\text{centered form}
&=
D_zu\,\Delta_z^2C
+
\Delta_z^2u\,D_zC,
\\
\text{affine first jet}
&=
0,
\\
\text{smooth local order}
&=
O(\ell^2),
\\
\text{generic second jet}
&\ne
0,
\\
\text{universal third-order cancellation}
&=
\mathrm{false},
\\
\text{fractional critical line}
&=
s_u+s_C=1
\text{ remains},
\\
\text{special cofactor projection}
&=
-\frac16q
-
\mathfrak V_\omega,
\\
\text{Piola-local branch}
&=
\omega=0,
\\
\text{nonlocal defect}
&=
\mathrm{vorticity\ stress},
\\
\text{missing}
&=
\mathrm{critical\ control\ of\ Piola\text{-}vorticity\ stress
or\ little\text{-}Zygmund/Campanato\ affine\ defect},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Named:

$$
\boxed{
\textbf{STOP-C45:
Affine-Jet Cancellation / Piola–Vorticity Endpoint Gap}.
}
$$

---

# 25. 24/72 Ledger — Round 41

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C623 | centered first/second differences | $\mathsf C$ | continuous translation | profile | $\mathsf F$ | FORM |
| C624 | centered cofactor-commutator identity | $\mathsf C$ | parity cancellation | targeted | $\mathsf F$ | EXACT |
| C625 | affine-jet cancellation | $\mathsf C$ | local jet | targeted | $\mathsf F$ | PROVED |
| C626 | smooth $O(\ell^2)$ local order | $\mathsf C$ | Taylor / kernel | scalar | $\mathsf F$ | PROVED |
| C627 | Zygmund/Campanato endpoint | $\mathsf C$ | affine defect | profile | $\mathsf F$ | IDENTIFIED |
| C628 | exact centered cofactor algebra | $\mathsf C$ | quadratic tensor | relational | $\mathsf F$ | EXACT |
| C629 | cofactor curvature decomposition | $\mathsf C$ | strain increments | relational | $\mathsf F$ | EXACT |
| C630 | Piola–vorticity cofactor decomposition | $\mathsf C$ | null Lagrangian | relational | $\mathsf F$ | EXACT |
| C631 | Piola double-divergence reduction | $\mathsf C$ | compensated structure | scalar | $\mathsf F$ | EXACT |
| C632 | cofactor scalar projection identity | $\mathsf C$ | Riesz projection | scalar | $\mathsf F$ | EXACT |
| C633 | irrotational Piola-local branch | $\mathsf C$ | vorticity-zero | targeted | $\mathsf F$ | PROVED |
| C634 | harmonic potential depletion witness | $\mathsf C$ | local jet | targeted | $\mathsf F$ | CONSTRUCTED |
| C635 | rotational second-jet witness | $\mathsf C$ | local polynomial | targeted | $\mathsf F$ | CONSTRUCTED |
| C636 | universal third-jet gain | $\mathsf C$ | special algebra | targeted | $\mathsf F$ | REFUTED |
| C637 | Piola–vorticity commutator resolution | $\mathsf C$ | operator/PDE | relational | $\mathsf F$ | EXACT |
| C638 | generic BMO endpoint closure | $\mathsf C$ | Campanato | targeted | $\mathsf F$ | OPEN / STOP-C45 |

---

# 26. Continuous-versus-discrete status

All core objects in this round:

- continuous centered translations;
- continuous second differences;
- continuous Taylor/Campanato affine defect;
- continuous cofactor tensor;
- continuous Piola/null-Lagrangian identity;
- continuous vorticity stress;
- continuous Riesz projection.

Absent are:

- discrete jets;
- dyadic Zygmund shells;
- vorticity cells;
- graph null-Lagrangian representation.

Even if the endpoint is described by Zygmund / Campanato,

everything can be represented by:

$$
r\in(0,\ell)
$$

continuous moduli.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 27. Strongest results of Round 41

## R41-A — Centered Cofactor-Commutator Identity

$$
\boxed{
\mathcal A_C
=
\frac12
\int
(D_zu\cdot\nabla K_0):\Delta_z^2C
+
\frac12
\int
(\Delta_z^2u\cdot\nabla K_0):D_zC.
}
$$

## R41-B — affine first-jet cancellation

$$
\boxed{
\text{leading affine first-first interaction vanishes exactly}.
}
$$

## R41-C — special cofactor centered algebra

$$
\boxed{
\Delta_z^2C
=
L_S(\Delta_z^2S)
+
2Q(D_zS)
+
\frac12Q(\Delta_z^2S).
}
$$

## R41-D — Piola–Vorticity Projection Identity

$$
\boxed{
\mathcal T_0^\ast C
=
-\frac16q
-
\frac1{12}|\omega|^2
-
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
$$

## R41-E — second-jet sharpness

for the explicit divergence-free rotational polynomial witness:

$$
\boxed{
\mathcal A_C^{\varepsilon<|z|<\ell}(0)
=
-\frac25
(
\ell^2-\varepsilon^2
)
}
$$

under the standard kernel sign convention.

Thus, there is no universal higher jet cancellation.

## R41-F — special cofactor nonlocality is vorticity-generated

The Piola resolution rewrites the generic cofactor transport commutator as:

$$
\boxed{
\text{vorticity-stress evolution}
+
\text{already-known defect/higher-gradient terms}.
}
$$

---

# 28. Next round — Piola–Vorticity Stress Defect Dynamics

Round 41 makes the next target very clear:

$$
\boxed{
\mathfrak V_\omega
=
\frac1{12}|\omega|^2
+
\frac14
\mathcal R_i\mathcal R_j
(
\omega_i\omega_j
).
}
$$

The next round will directly investigate:

1. the exact:
   $$
   (D_t-\nu\Delta)\mathfrak V_\omega;
   $$

2. the vorticity equation:
   $$
   D_t\omega=S\omega+\nu\Delta\omega;
   $$

3. the Riesz transport commutator of:
   $$
   \omega\otimes\omega;
   $$

4. whether incompressibility:
   $$
   \nabla\cdot\omega=0
   $$
   provides Hardy/div–curl compensation again;

5. whether $\mathfrak V_\omega$ can be controlled using the Round 18 weighted enstrophy / alignment budget;

6. if the nonlocal commutator of the vorticity stress can be further reduced by pairing-level cancellation, it may further narrow STOP-C45;

7. if not, the Piola–vorticity defect becomes the most stable nonlocal obstruction core at present;

8. continuing to use the continuous Riesz / stress / increment representation.

---

# 29. External primary-source anchors

1. Raz Kupferman, Asaf Shachar, *A geometric perspective on the Piola identity in Riemannian settings*, arXiv:1805.12365.
   - reviews and proves the classical Euclidean Piola identity
     $$
     \operatorname{div}\operatorname{cof}\nabla f=0,
     $$
     and interprets it through null-Lagrangians.

2. André Guerra, Bogdan Raiţă, *Quasiconvexity, null Lagrangians, and Hardy space integrability under constant rank constraints*, arXiv:1909.03923.
   - null-Lagrangians and Hardy-space compensated integrability under differential constraints.

3. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - generic Riesz transport commutators retain delicate endpoint velocity-regularity constraints.

4. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - anisotropic pressure Hessian is a genuinely nonlocal velocity-gradient functional with strong geometric alignment structure.

The Centered Cofactor-Commutator Identity, special centered cofactor algebra, Piola–Vorticity Projection Identity, second-jet sharpness witness, and Piola–Vorticity Commutator Resolution in this round are all directly derived in this document.

---

# 30. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Special\ Cofactor/Affine\text{-}Jet\ Cancellation},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Affine first jet}
&=
\mathrm{exactly\ cancelled},
\\
\text{Smooth local commutator}
&=
O(\ell^2),
\\
\text{Generic second jet}
&=
\mathrm{nonzero},
\\
\text{Universal extra fractional gain}
&=
\mathrm{false},
\\
\text{Cofactor null structure}
&=
\mathrm{Piola},
\\
\text{Piola defect}
&=
\mathrm{vorticity\ stress},
\\
\text{Critical endpoint}
&=
\mathrm{Zygmund/Campanato\ or\ vorticity\text{-}stress\ control},
\\
\text{STOP-C45}
&=
\mathrm{Affine\text{-}Jet\ Cancellation/Piola\text{-}Vorticity\ Endpoint\ Gap},
\\
\text{Next}
&=
\mathrm{Piola\text{-}Vorticity\ Stress\ Defect\ Dynamics}.
\end{aligned}
}
$$