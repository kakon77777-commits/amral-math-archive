# NS-DCRP-42 — Planar Potential–Shear Scalar Reduction, Canonical Pancake Amplification, and Mandatory Shear Turnover

- date: 2026-08-17
- status: research proof checkpoint / rank-two PDE reduction
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. derive the actual scalar PDE hidden inside the DCRP-40/41 planar potential--shear representation;
  2. prove the functional dependence of the normal velocity on the planar shear scalar;
  3. isolate the canonical moving-pancake normal-compression contribution;
  4. define a non-affine normal-shear residual;
  5. show that the exact canonical pancake eigenmode reduces to a scalar material amplification equation;
  6. derive a full family of positive $L^p$ turnover identities;
  7. prove that a periodic nonzero fixed-core pancake scalar cannot be materially closed;
  8. obtain a conditional global $L^p$ Liouville theorem for the exact pancake eigenmode;
  9. identify the remaining rank-two obstruction as shear turnover, normal-shear residual, moving-plane action, or rank lifting.
- no full Navier--Stokes regularity claim is made.
- external calibration:
  - D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782;
  - A. Enciso, A. J. Fernández, D. Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233.
- internal dependencies:
  - DCRP-40 planar potential--shear representation;
  - DCRP-41 moving pancake-jet normal form.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-40 showed that on a fixed rank-two vorticity plane, after choosing coordinates

$$
n=e_3,
$$

the velocity can be written locally as

$$
\boxed{
V
=
\left(
\nabla_h\phi,
w
\right),
}
\tag{1.1}
$$

where

$$
\nabla_h
=
(\partial_1,\partial_2).
$$

Define the planar shear scalar

$$
\boxed{
q
=
w-\partial_3\phi.
}
\tag{1.2}
$$

Then

$$
\boxed{
\Omega
=
\left(
\partial_2q,
-\partial_1q,
0
\right)
=
J\nabla_hq.
}
\tag{1.3}
$$

DCRP-42 proves that the rank-two PDE is much more constrained than this kinematic representation suggests.

The normal component of the DSS vorticity equation is

$$
\boxed{
\Omega_h\cdot\nabla_hw=0.
}
\tag{1.4}
$$

Therefore on every connected regular patch where

$$
\nabla_hq\neq0,
$$

$$
\boxed{
w
=
F(q,z,s)
}
\tag{1.5}
$$

for a local scalar constitutive function

$$
F.
$$

Thus the normal velocity cannot vary independently along planar vorticity level sets.

The planar shear scalar

$$
q
$$

labels those level sets.

The second main result is an exact scalar transport law.

Let

$$
\boxed{
W
=
\gamma y+V
}
\tag{1.6}
$$

be the DSS similarity material velocity and

$$
\boxed{
D_s
=
\partial_s+W\cdot\nabla.
}
\tag{1.7}
$$

On a regular planar-vorticity patch,

$$
\boxed{
\nabla_h
\left[
D_sq
+
\mathscr H(q,z,s)
\right]
=
0,
}
\tag{1.8}
$$

where

$$
\boxed{
\partial_q\mathscr H
=
1-\gamma
+
\partial_zF(q,z,s).
}
\tag{1.9}
$$

The additive

$$
(z,s)
$$

normalization of

$$
\mathscr H
$$

may be chosen so that

$$
\boxed{
D_sq
+
\mathscr H(q,z,s)
=
0.
}
\tag{1.10}
$$

This is the exact **planar potential--shear scalar reduction**.

The rank-two PDE has therefore been reduced locally to:

1. one scalar:

   $$
   q;
   $$

2. one constitutive function:

   $$
   F(q,z,s);
   $$

3. the finite-dimensional moving pancake parameters from DCRP-41.

The third main result isolates the canonical pancake strain.

On the zero-shape-action rank-two branch, DCRP-41 gives

$$
\boxed{
A_{\rm pan}
=
a(s)
\left(
P_{n^\perp}
-
2n\otimes n
\right)
-
\left(
n'\otimes n+n\otimes n'
\right).
}
\tag{1.11}
$$

The strict periodic pseudo-determinant condition gives

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
a(s)ds
=
\frac{
2-3\gamma
}{2}.
}
\tag{1.12}
$$

On the fixed-plane subbranch

$$
n'=0,
$$

the canonical affine normal velocity is

$$
-2a(s)z.
$$

Define the **non-affine normal-shear residual**

$$
\boxed{
G(q,z,s)
=
\partial_zF(q,z,s)
+
2a(s).
}
\tag{1.13}
$$

Then the scalar potential in (1.10) may be decomposed as

$$
\boxed{
\mathscr H(q,z,s)
=
\left[
1-\gamma-2a(s)
\right]q
+
\mathscr N(q,z,s),
}
\tag{1.14}
$$

with

$$
\boxed{
\partial_q\mathscr N
=
G.
}
\tag{1.15}
$$

Thus the rank-two fixed-plane branch satisfies

$$
\boxed{
D_sq
+
\left[
1-\gamma-2a(s)
\right]q
+
\mathscr N(q,z,s)
=
0.
}
\tag{1.16}
$$

The term

$$
\mathscr N
$$

is the exact residual measuring departure from the canonical pancake normal-strain relation.

The fourth central result concerns the exact pancake eigenmode

$$
\boxed{
G=0.
}
\tag{1.17}
$$

Then the

$$
q
$$

-dependent part of

$$
\mathscr N
$$

vanishes and its remaining

$$
(z,s)
$$

component is absorbed into the allowed primitive normalization.

Hence

$$
\boxed{
D_sq
+
k(s)q
=
0,
}
\tag{1.18}
$$

where

$$
\boxed{
k(s)
=
1-\gamma-2a(s).
}
\tag{1.19}
$$

Using (1.12),

$$
\boxed{
\bar k
=
\frac1{S_0}
\int_0^{S_0}
k(s)ds
=
2\gamma-1
<
0.
}
\tag{1.20}
$$

Define the positive periodic integrating factor

$$
\boxed{
\eta(s)
=
\exp
\left[
\int_0^s
\left(
k(\tau)-\bar k
\right)d\tau
\right].
}
\tag{1.21}
$$

Because

$$
k-\bar k
$$

has zero period mean,

$$
\boxed{
\eta(s+S_0)=\eta(s).
}
\tag{1.22}
$$

Define the renormalized shear scalar

$$
\boxed{
r
=
\eta(s)q.
}
\tag{1.23}
$$

Then

$$
\boxed{
D_sr
=
(1-2\gamma)r.
}
\tag{1.24}
$$

Set

$$
\boxed{
\lambda_\gamma
=
1-2\gamma.
}
\tag{1.25}
$$

In the strict Type-II window,

$$
\boxed{
\lambda_\gamma>0.
}
\tag{1.26}
$$

Thus the same material shear label amplifies exponentially in similarity coordinates:

$$
\boxed{
r(Y(a,s),s)
=
e^{\lambda_\gamma s}
r(a,0).
}
\tag{1.27}
$$

This is not a contradiction.

It is the scalar analogue of the earlier similarity Kelvin scaling.

The fifth main result is a full family of exact turnover identities.

For every

$$
p>0,
$$

define

$$
\boxed{
f_p
=
|r|^p.
}
\tag{1.28}
$$

Then

$$
\boxed{
D_sf_p
=
p\lambda_\gamma f_p.
}
\tag{1.29}
$$

Since

$$
\boxed{
\nabla\cdot W
=
3\gamma,
}
\tag{1.30}
$$

one gets

$$
\boxed{
\partial_sf_p
+
\nabla\cdot
\left(
Wf_p
\right)
=
\sigma_p
f_p,
}
\tag{1.31}
$$

where

$$
\boxed{
\sigma_p
=
3\gamma
+
p(1-2\gamma).
}
\tag{1.32}
$$

For

$$
\frac25<\gamma<\frac12
$$

and every

$$
p>0,
$$

$$
\boxed{
\sigma_p>0.
}
\tag{1.33}
$$

Let

$$
K
$$

be a fixed smooth similarity core and assume the chosen potential gauge makes

$$
r
$$

periodic in

$$
s.
$$

Integrating one DSS period gives

$$
\boxed{
\int_0^{S_0}
\int_{\partial K}
|r|^p
W\cdot n
dSds
=
\sigma_p
\int_0^{S_0}
\int_K
|r|^p
dyds.
}
\tag{1.34}
$$

Therefore every nonzero exact pancake scalar core has strictly positive **net outward shear-scalar flux**.

Thus

$$
\boxed{
\textbf{
nonzero fixed-plane canonical pancake eigenmode}
\Longrightarrow
\textbf{
mandatory scalar/material turnover}.
}
\tag{1.35}
$$

A self-contained periodic fixed core with zero scalar turnover is impossible.

This is the principal rigidity theorem of DCRP-42.

The sixth main result is a conditional global Liouville theorem.

Suppose the exact pancake scalar eigenmode holds globally and for some

$$
p>0
$$

one has

$$
\boxed{
r\in
L^p
\left(
\mathbb R^3\times[0,S_0]
\right)
}
\tag{1.36}
$$

with a sequence of radii

$$
R_j\to\infty
$$

along which the boundary flux in (1.34) vanishes.

Then

$$
\boxed{
r\equiv0.
}
\tag{1.37}
$$

Consequently

$$
\boxed{
\nabla_hq=0
}
\tag{1.38}
$$

and the rank-two planar vorticity vanishes.

Thus a nonzero exact pancake eigenmode must evade global scalar integrability/flux decay through a tail or sheet-type structure.

This is consistent with the external calibration:

- exact Euler pancake solutions combine shear and straining and have infinite global energy on:

  $$
  \mathbb R^3;
  $$

- recent exact vortex-sheet desingularizations produce thin layered Euler vorticities organized around time-dependent sheets.

Therefore thin/pancake scalar turnover is a legitimate Euler mechanism and cannot be excluded by local geometry alone.

The seventh result is the corrected rank-two master branch.

A nonzero strict rank-two core must enter at least one of:

$$
\boxed{
\textbf{
covariance shape/phase action}
}
$$

or

$$
\boxed{
\textbf{
moving-plane action}
}
$$

or

$$
\boxed{
\textbf{
non-affine normal-shear residual }G
}
$$

or, on the exact fixed-plane canonical eigenmode,

$$
\boxed{
\textbf{
positive planar-shear scalar turnover}.
}
$$

In addition, DCRP-38/40 retain:

- rank-one collapse;
- rank-three lifting;
- covariance/plane transition residual.

Thus the most rigid rank-two equality branch is no longer a closed pancake state.

It is a:

$$
\boxed{
\textbf{
periodic Eulerian pancake pattern sustained by scalar/material throughput}.
}
\tag{1.39}
$$

This is closely analogous in logic to the earlier Kelvin conclusion:

- the Eulerian pattern returns;
- the same material scalar labels do not return unchanged;
- recurrence requires continual replacement/turnover.

The new exact frontier is therefore

$$
\boxed{
\textbf{
Pancake Scalar Turnover /
Same-Parent Sheet-Replenishment Rigidity.
}
}
\tag{1.40}
$$

The next question is:

> can the required outward planar-shear throughput be replenished indefinitely from the same-parent DSS tail while also satisfying:
>
> - the DCRP-31 inward PFET matching layer;
> - the DCRP-35 enstrophy/strain supplier;
> - raw-energy vanishing;
> - zero rank-three lifting;
> - zero non-affine normal-shear residual?

If not, the rank-two equality branch closes.

---

# 2. Fixed-plane potential--shear representation

Choose coordinates

$$
y=(x_1,x_2,z).
$$

Assume

$$
\Omega_3=0.
$$

Then

$$
\partial_1V_2-\partial_2V_1=0.
$$

On a simply connected horizontal patch there exists

$$
\phi
$$

with

$$
\boxed{
V_h
=
\nabla_h\phi.
}
\tag{2.1}
$$

Set

$$
\boxed{
w=V_3.
}
\tag{2.2}
$$

Define

$$
\boxed{
q
=
w-\phi_z.
}
\tag{2.3}
$$

Then

$$
\boxed{
\Omega_h
=
\left(
q_2,-q_1
\right)
=
J\nabla_hq.
}
\tag{2.4}
$$

Status:

$$
\boxed{
\textbf{PROVED / inherited from DCRP-40}.
}
$$

---

# 3. Normal-vorticity preservation

The DSS vorticity equation is

$$
\partial_s\Omega
+
W\cdot\nabla\Omega
+
\Omega
=
(\Omega\cdot\nabla)V.
$$

The normal component gives

$$
\boxed{
0
=
\Omega_h\cdot\nabla_hw.
}
\tag{3.1}
$$

Using

$$
\Omega_h=J\nabla_hq,
$$

$$
\boxed{
J\nabla_hq
\cdot
\nabla_hw
=
0.
}
\tag{3.2}
$$

Equivalently, the horizontal Jacobian vanishes:

$$
\boxed{
\partial_1q\,\partial_2w
-
\partial_2q\,\partial_1w
=
0.
}
\tag{3.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. Local functional dependence

On a regular patch where

$$
\nabla_hq\neq0,
$$

equation (3.3) says the horizontal gradients of

$$
q
$$

and

$$
w
$$

are parallel.

Therefore locally

$$
\boxed{
w
=
F(q,z,s).
}
\tag{4.1}
$$

The function

$$
F
$$

may depend explicitly on the normal coordinate and similarity time.

This is a local statement on regular level-set patches.

No global single-valued

$$
F
$$

is claimed across critical points or topology changes of the level sets.

---

# 5. Horizontal vorticity equation

Let

$$
g=\nabla_hq.
$$

Then

$$
\Omega_h=Jg.
$$

The horizontal stretching is

$$
(\Omega\cdot\nabla)V_h
=
D_h^2\phi\,
\Omega_h.
$$

Thus

$$
\boxed{
D_s
(
Jg
)
+
Jg
=
D_h^2\phi\,
Jg.
}
\tag{5.1}
$$

Multiplying by

$$
-J
$$

and using the two-dimensional identity

$$
\boxed{
-JHJ
=
(\operatorname{tr}H)I-H
}
\tag{5.2}
$$

for symmetric

$$
H,
$$

one gets

$$
\boxed{
D_sg+g
=
\left[
\Delta_h\phi\,I
-
D_h^2\phi
\right]g.
}
\tag{5.3}
$$

---

# 6. Gradient transport identity

The horizontal gradient of

$$
D_sq
$$

satisfies

$$
\boxed{
D_sg
=
\nabla_h
(
D_sq
)
-
\left[
\gamma I+D_h^2\phi
\right]g
-
q_z\nabla_hw.
}
\tag{6.1}
$$

Insert this into (5.3).

The Hessian terms cancel.

Thus

$$
\boxed{
\nabla_h
(
D_sq
)
=
\left[
\Delta_h\phi-(1-\gamma)
\right]g
+
q_z\nabla_hw.
}
\tag{6.2}
$$

---

# 7. Use of the constitutive function

Since

$$
w=F(q,z,s),
$$

$$
\boxed{
\nabla_hw
=
F_q
\nabla_hq
=
F_qg.
}
\tag{7.1}
$$

Incompressibility gives

$$
\boxed{
\Delta_h\phi
+
w_z
=
0.
}
\tag{7.2}
$$

Because

$$
w=F(q,z,s),
$$

the total normal derivative is

$$
\boxed{
w_z
=
F_qq_z
+
F_z,
}
\tag{7.3}
$$

where

$$
F_z
$$

denotes the partial derivative at fixed

$$
q.
$$

Therefore

$$
\boxed{
\Delta_h\phi
=
-F_qq_z-F_z.
}
\tag{7.4}
$$

Substitute into (6.2).

The

$$
F_qq_z
$$

terms cancel.

Hence

$$
\boxed{
\nabla_h
(
D_sq
)
=
-
\left[
1-\gamma+F_z(q,z,s)
\right]
\nabla_hq.
}
\tag{7.5}
$$

This cancellation is the key scalar reduction.

---

# 8. NEW THEOREM — Planar Shear Scalar Equation

## Theorem 8.1

On every connected regular planar-vorticity patch there exists a scalar primitive

$$
\mathscr H(q,z,s)
$$

with

$$
\boxed{
\partial_q\mathscr H
=
1-\gamma+F_z(q,z,s)
}
\tag{8.1}
$$

such that, after choosing its additive

$$
(z,s)
$$

normalization,

$$
\boxed{
D_sq
+
\mathscr H(q,z,s)
=
0.
}
\tag{8.2}
$$

### Proof

Equation (7.5) is exactly

$$
\nabla_h
\left[
D_sq+\mathscr H(q,z,s)
\right]
=
0.
$$

Thus the bracket is a function only of

$$
z,s.
$$

The primitive

$$
\mathscr H
$$

is defined only up to addition of such a function.

Choose that additive normalization to cancel the bracket.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED LOCALLY ON REGULAR LEVEL-SET PATCHES}.
}
$$

---

# 9. Pancake normal-shear split

On the fixed-plane zero-shape-action branch the canonical affine tensor is

$$
A_{\rm pan}
=
a(s)
\left(
P_h
-
2e_3\otimes e_3
\right).
$$

The canonical normal velocity contribution is therefore

$$
-2a(s)z.
$$

Define

$$
\boxed{
G(q,z,s)
=
F_z(q,z,s)
+
2a(s).
}
\tag{9.1}
$$

Then

$$
\boxed{
F_z
=
-2a+G.
}
\tag{9.2}
$$

The scalar primitive may be written

$$
\boxed{
\mathscr H
=
\left[
1-\gamma-2a(s)
\right]q
+
\mathscr N(q,z,s),
}
\tag{9.3}
$$

where

$$
\boxed{
\partial_q\mathscr N
=
G.
}
\tag{9.4}
$$

Thus

$$
\boxed{
D_sq
+
\left[
1-\gamma-2a
\right]q
+
\mathscr N
=
0.
}
\tag{9.5}
$$

---

# 10. Meaning of the normal-shear residual

The residual

$$
G
$$

measures failure of the normal velocity to have the canonical pancake normal derivative

$$
-2a.
$$

Thus:

### exact pancake normal shear

$$
\boxed{
G=0.
}
\tag{10.1}
$$

### non-affine potential--shear branch

$$
\boxed{
G\neq0.
}
\tag{10.2}
$$

The latter is already a genuine scalar source/deformation residual.

It need not be interpreted through covariance geometry.

---

# 11. Exact canonical pancake scalar eigenmode

Assume

$$
\boxed{
G=0.
}
\tag{11.1}
$$

Then

$$
\mathscr N
$$

has no

$$
q
$$

dependence and is absorbed into the primitive normalization.

Therefore

$$
\boxed{
D_sq
+
k(s)q
=
0,
}
\tag{11.2}
$$

where

$$
\boxed{
k(s)
=
1-\gamma-2a(s).
}
\tag{11.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. Period-average reaction exponent

DCRP-41 gives

$$
\boxed{
\left\langle
a
\right\rangle
=
\frac{
2-3\gamma
}{2}.
}
\tag{12.1}
$$

Hence

$$
\begin{aligned}
\bar k
&=
1-\gamma
-
2\langle a\rangle
\\
&=
1-\gamma
-
(2-3\gamma)
\\
&=
2\gamma-1.
\end{aligned}
$$

Thus

$$
\boxed{
\bar k
=
-(1-2\gamma)
<0.
}
\tag{12.2}
$$

The canonical planar shear scalar therefore amplifies on average along similarity-material trajectories.

---

# 13. Periodic integrating factor

Define

$$
\boxed{
\eta(s)
=
\exp
\left[
\int_0^s
\left(
k(\tau)-\bar k
\right)d\tau
\right].
}
\tag{13.1}
$$

Then

$$
\boxed{
\eta>0,
}
\tag{13.2}
$$

and

$$
\boxed{
\eta(s+S_0)=\eta(s).
}
\tag{13.3}
$$

Set

$$
\boxed{
r
=
\eta q.
}
\tag{13.4}
$$

Since

$$
\eta
$$

depends only on

$$
s,
$$

$$
D_sr
=
\eta D_sq
+
\eta' q.
$$

Using

$$
D_sq=-kq
$$

and

$$
\eta'/\eta=k-\bar k,
$$

$$
\boxed{
D_sr
=
-\bar k r
=
(1-2\gamma)r.
}
\tag{13.5}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Material amplification

Along a similarity-material trajectory

$$
Y(a,s),
$$

$$
\boxed{
\frac d{ds}
r(
Y(a,s),s
)
=
(1-2\gamma)
r(
Y(a,s),s
).
}
\tag{14.1}
$$

Thus

$$
\boxed{
r(
Y(a,s),s
)
=
e^{(1-2\gamma)s}
r(a,0).
}
\tag{14.2}
$$

For one DSS period:

$$
\boxed{
r(
Y(a,S_0),S_0
)
=
e^{(1-2\gamma)S_0}
r(a,0).
}
\tag{14.3}
$$

Because

$$
1-2\gamma>0,
$$

the same material label carries an increasing normalized shear scalar.

A periodic Eulerian pattern therefore requires material replacement/turnover.

---

# 15. $L^p$ density equation

For

$$
p>0,
$$

set

$$
f_p=|r|^p.
$$

Then

$$
\boxed{
D_sf_p
=
p(1-2\gamma)f_p.
}
\tag{15.1}
$$

Since

$$
\nabla\cdot W=3\gamma,
$$

$$
\boxed{
\partial_sf_p
+
\nabla\cdot(Wf_p)
=
\left[
3\gamma+p(1-2\gamma)
\right]f_p.
}
\tag{15.2}
$$

Define

$$
\boxed{
\sigma_p
=
3\gamma+p(1-2\gamma).
}
\tag{15.3}
$$

For the strict branch:

$$
\boxed{
\sigma_p>0
\qquad
\forall p>0.
}
\tag{15.4}
$$

---

# 16. NEW THEOREM — Periodic Fixed-Core Pancake Turnover

## Theorem 16.1

Let

$$
K
$$

be a fixed smooth bounded similarity core contained in one regular pancake patch.

Assume the periodic potential gauge is chosen so that

$$
r(y,s+S_0)=r(y,s).
$$

Then

$$
\boxed{
\int_0^{S_0}
\int_{\partial K}
|r|^p
W\cdot n
dSds
=
\sigma_p
\int_0^{S_0}
\int_K
|r|^p
dyds.
}
\tag{16.1}
$$

If

$$
r\not\equiv0
$$

on

$$
K\times[0,S_0],
$$

then

$$
\boxed{
\int_0^{S_0}
\int_{\partial K}
|r|^p
W\cdot n
dSds
>
0.
}
\tag{16.2}
$$

### Proof

Integrate (15.2) over

$$
K\times[0,S_0].
$$

The time endpoint vanishes by periodicity.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 17. Interpretation of the sign

The normal

$$
n
$$

points outward from

$$
K.
$$

Therefore (16.2) says the canonical pancake eigenmode has positive **net outward transport** of the scalar density

$$
|r|^p.
$$

This is not energy dissipation.

It is a material/shear-label turnover law.

The strict similarity source amplifies

$$
r
$$

inside the Eulerian chart.

Periodicity can be maintained only by exporting amplified material scalar content through the core boundary.

---

# 18. No materially closed pancake core

If

$$
W\cdot n=0
$$

on

$$
\partial K
$$

for all similarity time, then the left side of (16.1) vanishes.

Thus

$$
\boxed{
r\equiv0
}
\tag{18.1}
$$

inside

$$
K.
$$

Hence

$$
\nabla_hq=0
$$

and the planar vorticity vanishes.

Therefore:

$$
\boxed{
\textbf{
nonzero exact pancake scalar core}
\not\subset
\textbf{
materially closed similarity region}.
}
}
\tag{18.2}
$$

This is a direct local rigidity statement.

---

# 19. Conditional whole-space $L^p$ Liouville theorem

## Theorem 19.1

Assume the exact pancake scalar eigenmode holds globally.

Suppose for some

$$
p>0
$$

$$
\boxed{
r\in
L^p
\left(
\mathbb R^3\times[0,S_0]
\right).
}
\tag{19.1}
$$

Suppose there exists

$$
R_j\to\infty
$$

such that

$$
\boxed{
\int_0^{S_0}
\int_{\partial B_{R_j}}
|r|^p
|W\cdot n|
dSds
\to0.
}
\tag{19.2}
$$

Then

$$
\boxed{
r\equiv0.
}
\tag{19.3}
$$

Consequently

$$
\boxed{
\Omega_h=0.
}
\tag{19.4}
$$

### Proof

Apply Theorem 16.1 to

$$
B_{R_j}.
$$

The left side tends to zero.

The right side is

$$
\sigma_p
\int_{B_{R_j}\times[0,S_0]}
|r|^p.
$$

Monotone convergence gives the result.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED CONDITIONAL}.
}
$$

---

# 20. Why global $L^p$ is not automatic

The strict Type-II DSS profile is already known to be tail-fed and to have infinite global normalized kinetic energy in the strict geometric branch.

The scalar

$$
q
$$

contains a velocity/shear potential component and is not automatically controlled in a global

$$
L^p
$$

space by the existing critical kinetic-energy envelope.

Therefore Theorem 19.1 is a genuine subbranch Liouville theorem, not a universal closure.

---

# 21. Moving-plane branch

DCRP-41 gives the moving pancake tensor

$$
A_{\rm pan}
=
a
(
P_{n^\perp}-2n\otimes n
)
-
(
n'\otimes n+n\otimes n'
).
$$

If

$$
n'\neq0,
$$

the rank-two branch already pays the finite-dimensional plane-motion action

$$
\boxed{
2
\int_0^{S_0}
|n'|^2ds.
}
\tag{21.1}
$$

DCRP-42 therefore derives the scalar reduction on the fixed-plane equality subbranch.

A full co-rotating scalar equation would contain additional finite-dimensional frame terms.

Those terms are not needed for the present dichotomy:

$$
\boxed{
n'\neq0
}
$$

is already an explicit moving-plane activity channel.

---

# 22. Normal-shear residual branch

If

$$
G\neq0,
$$

then

$$
\boxed{
\partial_q\mathscr N=G.
}
$$

The planar scalar equation is nonlinear:

$$
D_sq
+
(1-\gamma-2a)q
+
\mathscr N(q,z,s)
=
0.
$$

This is a genuine non-affine normal-shear mechanism.

Thus the most rigid pancake scalar turnover theorem applies only after:

$$
\boxed{
G=0.
}
$$

The branch classification is explicit rather than hidden.

---

# 23. Rank-two master reduction after DCRP-42

A nonzero strict rank-two profile now satisfies at least one of:

$$
\boxed{
\text{rank-one collapse}
}
$$

or

$$
\boxed{
\text{rank-three lifting}
}
$$

or

$$
\boxed{
\text{covariance/plane residual}
}
$$

or

$$
\boxed{
\text{positive planar shape action}
}
$$

or

$$
\boxed{
\text{moving-plane action}
}
$$

or

$$
\boxed{
\text{non-affine normal-shear residual}
}
$$

or

$$
\boxed{
\text{positive canonical pancake scalar turnover}.
}
$$

Thus no rank-two branch remains which is simultaneously:

- shape static;
- plane static;
- normal-shear canonical;
- materially closed.

---

# 24. Connection to DCRP-31 PFET

DCRP-31 already forces a finite-radius inward Euler pressure--kinetic energy flux.

DCRP-42 forces, on the canonical fixed-plane pancake scalar branch, positive outward

$$
|r|^p
$$

turnover.

Therefore the strict equality state has simultaneous counter-directed transfers:

$$
\boxed{
\text{inward kinetic-energy PFET}
}
$$

and

$$
\boxed{
\text{outward amplified planar-shear scalar throughput}.
}
$$

These quantities are not the same conserved density.

No contradiction is asserted merely from the opposite signs.

But this identifies a nontrivial **core exchange cycle**.

---

# 25. Pancake exchange-cycle normal form

The strongest canonical rank-two state can now be described as:

1. kinetic energy is supplied inward through the DCRP-31 matching layer;

2. the pancake affine strain amplifies the planar shear scalar along material trajectories;

3. the amplified scalar density is exported through the fixed similarity core boundary;

4. DSS recurrence reconstructs the same Eulerian scalar pattern with new material labels.

Thus the final rank-two equality state is not a closed coherent pancake.

It is an open, throughput-driven recurrence.

---

# 26. Exact Euler pancake calibration

Agafontsev--Kuznetsov--Mailybaev construct an exact Euler solution for pancake high-vorticity regions by combining a shear flow with an asymmetric straining flow and an arbitrary transversal vorticity profile.

The solution provides a concrete example in which shear/vorticity profile and strain form a highly structured anisotropic flow.

It has infinite global energy on

$$
\mathbb R^3
$$

and therefore does not realize the finite-energy same-parent DCRP ancestry.

Its role here is to show that the local pancake scalar/strain mechanism is mathematically legitimate and should be excluded only with the additional DSS/return constraints.

---

# 27. Vortex-sheet calibration

Recent exact Euler constructions desingularize analytic three-dimensional vortex sheets into smooth vorticities supported in tubular neighborhoods whose thickness tends to zero.

The vorticities are organized by nearly parallel surfaces with divergence-free tangent fields.

This confirms that layered planar vorticity transport is a genuine Euler mechanism.

Therefore the DCRP turnover theorem should be interpreted as a transition requirement, not a local impossibility theorem.

---

# 28. Same-parent replenishment problem

The periodic Eulerian scalar field

$$
r(y,s)
$$

returns every DSS period.

But along the same material label,

$$
r
$$

is amplified by

$$
e^{(1-2\gamma)S_0}>1.
$$

Thus state recurrence requires continual replacement of the scalar-carrying material set.

The next same-parent question is:

> where do the lower-amplitude replacement labels come from, and how are the amplified labels removed while the physical Navier--Stokes parent remains finite-energy and unforced?

This is the pancake analogue of the earlier circulation-replenishment problem, now expressed by an exact scalar continuity equation.

---

# 29. Candidate scalar-capacity ledger

For a fixed core

$$
K,
$$

define

$$
\boxed{
\mathcal Q_{p,K}
=
\int_K
|r|^pdy.
}
\tag{29.1}
$$

The period identity gives

$$
\boxed{
\mathcal J_{p,K}^{out}
=
\sigma_p
\int_0^{S_0}
\mathcal Q_{p,K}(s)ds.
}
\tag{29.2}
$$

Thus a normalized lower bound on

$$
\mathcal Q_{p,K}
$$

gives a normalized lower bound on scalar throughput.

A compact-class finite turnover gap can therefore be obtained if a fixed

$$
p
$$

and fixed core scalar mass are declared.

No claim of raw physical non-summability is made yet.

---

# 30. Why this scalar route is different from energy telescoping

The shear scalar amplification exponent is

$$
1-2\gamma,
$$

while the physical raw kinetic-energy decay is governed by the separate critical exponent

$$
\kappa=3-2\alpha.
$$

The scalar throughput is therefore not simply the same raw-energy difference used in the critical telescoping NO-GO.

However a full physical scaling audit is still required before using the scalar turnover as a non-summable parent-level tax.

DCRP-42 treats it as a native transition/replenishment observable.

---

# 31. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Pancake Scalar Turnover /
Same-Parent Sheet-Replenishment Rigidity.
}
}
$$

A useful theorem would show that the exact canonical scalar turnover must produce at least one of:

1. a finite sheet/material transition carrier;

2. a rank-three vorticity-direction lifting event;

3. a nonzero normal-shear residual:

   $$
   G;
   $$

4. a pressure/PFET coupling visible in the same finite matching annulus;

5. a scalar tail class satisfying enough integrability to trigger Theorem 19.1;

6. a known exact pancake/sheet eigenmode incompatible with the finite-energy unforced same-parent ancestry.

This is now the principal rank-two recurrence frontier.

---

# 32. End state

The fixed-plane rank-two velocity is

$$
\boxed{
V=(\nabla_h\phi,w),
}
$$

with

$$
\boxed{
q=w-\phi_z,
\qquad
\Omega_h=J\nabla_hq.
}
$$

The DSS vorticity equation forces

$$
\boxed{
w=F(q,z,s)
}
$$

locally on regular patches.

The scalar obeys

$$
\boxed{
D_sq+\mathscr H(q,z,s)=0,
\qquad
\partial_q\mathscr H
=
1-\gamma+F_z.
}
$$

After separating the moving-pancake normal strain,

$$
\boxed{
G=F_z+2a
}
$$

is the non-affine normal-shear residual.

On the exact canonical branch

$$
G=0,
$$

the periodic integrating-factor scalar

$$
r
$$

satisfies

$$
\boxed{
D_sr
=
(1-2\gamma)r.
}
$$

Therefore for every

$$
p>0,
$$

$$
\boxed{
\partial_s|r|^p
+
\nabla\cdot(W|r|^p)
=
\left[
3\gamma+p(1-2\gamma)
\right]
|r|^p.
}
$$

The coefficient is strictly positive throughout the strict Type-II exponent window.

Thus every nonzero periodic fixed-core canonical pancake mode has mandatory positive outward scalar turnover.

The strongest rank-two equality state is therefore:

$$
\boxed{
\textbf{
an inward-PFET-fed pancake pattern with outward planar-shear material throughput.
}
}
$$

The next frontier is

$$
\boxed{
\textbf{
Pancake Scalar Turnover /
Same-Parent Sheet-Replenishment Rigidity.
}
}
$$