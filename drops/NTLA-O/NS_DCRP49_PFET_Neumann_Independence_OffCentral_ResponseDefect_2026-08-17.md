# DCRP49 — PFET/Neumann Independence, Pressure-Response Mixed Defect, and Off-Central Pancake Enstrophy Rigidity

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-17  
**Status:** Proof-development checkpoint / pressure-coupling correction + DCRP–X72 bridge  
**Immediate predecessor:** `NS_DCRP48_PressureDriven_ResponseSlope_Telescoping_2026-08-17.md`

**Primary internal dependencies**
- DCRP-31 — finite-radius inward PFET matching layer
- DCRP-35 — enstrophy turnover / finite-annulus vortex-stretching supplier
- DCRP-44 — gauge-flat scalar connection
- DCRP-48 — pressure-driven response-slope dynamics
- X72 Round 36 — cofactor/pressure response coherence
- X72 Round 37 — affine pressure-response defect
- X72 Round 41–43 — special cofactor / vorticity-stress / pressure-realizability frontier

**External calibration checked before this round**
- G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468.
- D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782.
- S. Shkoller, *Incompressible Euler Blowup at the $C^{1,\frac13}$ Threshold*, arXiv:2603.10945.

These are calibration references only. No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP48 left two pressure observables on the finite supplier package:

1. DCRP31 inward pressure–kinetic-energy flux (PFET);
2. DCRP48 pressure-Neumann / mixed-Hessian response information.

The first task was to test whether these pressure channels are universally tied.

They are not.

For every nonzero constant symmetric trace-free matrix $S_0$, the exact incompressible affine Euler solution

$$
u(x)=S_0x,
$$

$$
p(x)=-\frac12x^\top S_0^2x
$$

satisfies

$$
\frac12|u|^2+p=0
$$

pointwise.

Therefore its physical pressure–kinetic flux is identically zero across every surface:

$$
\boxed{
\int_{\partial D}
\left(
\frac12|u|^2+p
\right)
u\cdot n\,dS
=
0.
}
$$

But

$$
-\Delta p
=
|S_0|^2,
$$

so

$$
\boxed{
-\int_{\partial D}
\partial_np\,dS
=
|S_0|^2|D|
>0.
}
$$

Thus:

$$
\boxed{
\textbf{
PFET and pressure-Neumann flux are genuinely different observables; no universal algebraic sign/size coupling exists.
}
}
$$

This closes the naive DCRP49 route.

The useful progress comes from combining DCRP48 with the X72 affine pressure-response defect.

Let

$$
\boxed{
E_p
=
H_P^0
+
C_S^0,
}
$$

where

$$
H_P^0
=
\nabla^2P-\frac{\Delta P}{3}I,
$$

and

$$
C_S^0
=
S^2-\frac13|S|^2I.
$$

On the fully flat rank-two scalar patch define

$$
p_h=\nabla_hq,
$$

$$
\Omega_h=Jp_h,
$$

$$
c=B_q,
$$

and

$$
\delta_c
=
c-\frac12.
$$

The local strain has block form

$$
S
=
\begin{pmatrix}
H & \delta_c p_h\\
\delta_c p_h^\top & d
\end{pmatrix},
$$

where

$$
H=D_h^2\phi,
$$

$$
d=w_z,
$$

and incompressibility gives

$$
\operatorname{tr}H+d=0.
$$

DCRP48 gives

$$
\nabla_hP_z
=
-(D_sc)p_h.
$$

A direct cofactor calculation then yields the exact mixed-defect identity

$$
\boxed{
(D_sc)|\Omega_h|^2
+
\left(c-\frac12\right)
\Omega_h\cdot S\Omega_h
=
-
p_h\cdot
(E_p)_{hn}.
}
$$

This is the main theorem of DCRP49.

It unifies three previously separate objects:

- DCRP48 response-slope drift;
- DCRP35 vortex stretching;
- X72 Round37 affine pressure-response defect.

Define the **off-central response enstrophy**

$$
\boxed{
X_c
=
\left(c-\frac12\right)^2
|\Omega_h|^2.
}
$$

Using the similarity-vorticity equation

$$
D_s\Omega+\Omega
=
(\Omega\cdot\nabla)V,
$$

one obtains the exact defect-energy law

$$
\boxed{
D_sX_c+2X_c
=
-2
\left(c-\frac12\right)
p_h\cdot(E_p)_{hn}.
}
$$

Since

$$
\nabla\cdot W=3\gamma,
$$

this becomes the conservative balance

$$
\boxed{
\partial_sX_c
+
\nabla\cdot(WX_c)
+
(2-3\gamma)X_c
=
-2
\left(c-\frac12\right)
p_h\cdot(E_p)_{hn}.
}
$$

The damping coefficient is exactly the same positive coefficient

$$
2-3\gamma
$$

that appears in DCRP35's enstrophy balance.

For an $S_0$-periodic fixed domain $D$:

$$
\boxed{
\begin{aligned}
(2-3\gamma)
\int_0^{S_0}\int_DX_c
&=
-\int_0^{S_0}\int_{\partial D}
X_cW\cdot n
\\
&\quad
-2
\int_0^{S_0}\int_D
\left(c-\frac12\right)
p_h\cdot(E_p)_{hn}.
\end{aligned}
}
$$

Therefore every recurrent non-central response core satisfies the exact alternative

$$
\boxed{
\textbf{
inward off-central response turnover}
\ \vee\
\textbf{
nonzero mixed affine pressure-response defect}.
}
}
$$

In particular, if

$$
(E_p)_{hn}=0
$$

and there is no inward $X_c$ flux, then

$$
\boxed{
X_c=0.
}
$$

On the active rank-two set where $|\Omega_h|>0$,

$$
\boxed{
c=\frac12.
}
$$

Thus the response slope

$$
\boxed{
c=\frac12
}
$$

is the unique **mixed-pressure/cofactor invisible central pancake mode**.

A further exact corollary is:

If $c$ is constant, $c\neq1/2$, and the X72 mixed pressure-response defect vanishes, then

$$
\boxed{
\Omega_h\cdot S\Omega_h=0.
}
$$

So DCRP35 forces the core to be maintained by inward enstrophy turnover rather than local vortex stretching.

The final rank-two survivor is therefore compressed to:

$$
\boxed{
c=\frac12
}
$$

or

$$
\boxed{
\text{inward off-central/enstrophy turnover}
}
$$

or

$$
\boxed{
\text{nonzero X72 affine pressure-response defect}
}
$$

or

$$
\boxed{
\text{flat-chart / rank transition}.
}
$$

This is the first exact algebraic bridge between the DCRP rank-two pancake branch and the X72 pressure/cofactor program.

---

# 1. First NO-GO: pressure-Neumann flux is not PFET

Let

$$
S_0=S_0^\top,
\qquad
\operatorname{tr}S_0=0,
\qquad
S_0\neq0.
$$

Define

$$
\boxed{
u(x)=S_0x.
}
\tag{1.1}
$$

Then

$$
\nabla\cdot u=0.
$$

Also

$$
(u\cdot\nabla)u
=
S_0^2x.
$$

Choose

$$
\boxed{
p(x)
=
-\frac12x^\top S_0^2x.
}
\tag{1.2}
$$

Then

$$
\nabla p
=
-S_0^2x.
$$

Therefore

$$
\boxed{
(u\cdot\nabla)u+\nabla p=0.
}
\tag{1.3}
$$

This is an exact steady incompressible Euler solution.

---

# 2. PFET vanishes identically on the affine witness

The kinetic energy density is

$$
e(x)
=
\frac12|u|^2
=
\frac12x^\top S_0^2x.
$$

Hence

$$
\boxed{
e+p=0
}
\tag{2.1}
$$

pointwise.

Therefore for every smooth bounded domain $D$,

$$
\boxed{
\int_{\partial D}
(e+p)u\cdot n\,dS
=
0.
}
\tag{2.2}
$$

In particular every radial PFET channel vanishes.

---

# 3. Pressure-Neumann flux is strictly nonzero

From (1.2),

$$
\boxed{
\Delta p
=
-\operatorname{tr}S_0^2
=
-|S_0|^2.
}
\tag{3.1}
$$

Thus

$$
\boxed{
-\int_{\partial D}
\partial_np\,dS
=
-\int_D\Delta p\,dx
=
|S_0|^2|D|
>0.
}
\tag{3.2}
$$

## Theorem D49.1 — PFET/Neumann Independence Witness

There exists an exact smooth incompressible Euler solution with

$$
\boxed{
\mathrm{PFET}=0
}
$$

on every bounded surface while

$$
\boxed{
-\int_{\partial D}\partial_np>0
}
$$

for every bounded domain of positive volume.

Therefore no universal algebraic or sign identity can identify the DCRP31 PFET current with the DCRP48 pressure-Neumann current.

### Remark

This affine witness is not the finite-energy DSS survivor itself.

It is used only to disprove a universal local pressure-current identity.

Any DSS-specific coupling must use additional global/periodic structure.

---

# 4. Relation to the X72 affine pressure witness

X72 Round36 independently uses the same affine geometry as a structural pressure-response witness:

$$
u(x)=S_0x,
$$

$$
p(x)=-\frac12x^\top S_0^2x.
$$

For this witness,

$$
\boxed{
H_p^0=-C_S^0.
}
\tag{4.1}
$$

Thus the X72 affine pressure-response defect

$$
\boxed{
E_p
=
H_p^0+C_S^0
}
\tag{4.2}
$$

vanishes exactly.

Combining Sections 1–3 with (4.1):

$$
\boxed{
E_p=0
}
$$

does not imply nonzero PFET.

This is a second reason not to collapse the DCRP31 and X72 pressure observables into one coordinate.

They detect different structures.

---

# 5. Flat rank-two local variables

Return to the DCRP44/48 fully flat scalar branch.

Fix the vorticity-plane normal

$$
n.
$$

Use coordinates

$$
n=e_3.
$$

Let

$$
\boxed{
p_h
=
\nabla_hq.
}
\tag{5.1}
$$

The planar vorticity is

$$
\boxed{
\Omega_h
=
Jp_h.
}
\tag{5.2}
$$

Hence

$$
\boxed{
|\Omega_h|=|p_h|.
}
\tag{5.3}
$$

Define

$$
\boxed{
c=B_q
}
\tag{5.4}
$$

and

$$
\boxed{
\delta_c
=
c-\frac12.
}
\tag{5.5}
$$

DCRP48 gives

$$
\boxed{
\nabla_hw
=
cp_h,
}
\tag{5.6}
$$

and

$$
\boxed{
\partial_zV_h
=
(c-1)p_h.
}
\tag{5.7}
$$

Thus the cross-plane symmetric strain vector is

$$
\boxed{
s_\times
=
\frac12
\left(
\nabla_hw+\partial_zV_h
\right)
=
\delta_c p_h.
}
\tag{5.8}
$$

---

# 6. Local strain block form

Write the full symmetric strain tensor as

$$
\boxed{
S
=
\begin{pmatrix}
H&s_\times\\
s_\times^\top&d
\end{pmatrix},
}
\tag{6.1}
$$

where

$$
\boxed{
H=D_h^2\phi
}
\tag{6.2}
$$

and

$$
\boxed{
d=w_z.
}
\tag{6.3}
$$

Incompressibility gives

$$
\boxed{
\operatorname{tr}H+d=0.
}
\tag{6.4}
$$

The horizontal vorticity is tangent to the plane and orthogonal to $p_h$.

Because

$$
s_\times\cdot\Omega_h
=
\delta_c p_h\cdot Jp_h
=
0,
$$

the vortex-stretching density is

$$
\boxed{
\Omega_h\cdot S\Omega_h
=
\Omega_h\cdot H\Omega_h.
}
\tag{6.5}
$$

---

# 7. Two-dimensional trace identity

Let

$$
J
$$

denote the $90^\circ$ rotation in the vorticity plane.

For every symmetric $2\times2$ matrix $H$ and vector $p$,

$$
(Jp)^\top H(Jp)
=
(\operatorname{tr}H)|p|^2
-
p^\top Hp.
$$

Using

$$
\operatorname{tr}H=-d,
$$

we obtain

$$
\boxed{
p_h^\top(H+dI_2)p_h
=
-
\Omega_h\cdot H\Omega_h.
}
\tag{7.1}
$$

Therefore, by (6.5),

$$
\boxed{
p_h^\top(H+dI_2)p_h
=
-
\Omega_h\cdot S\Omega_h.
}
\tag{7.2}
$$

This elementary planar identity is the algebraic core of the DCRP–X72 bridge.

---

# 8. Mixed cofactor block

X72 defines

$$
\boxed{
C_S^0
=
S^2-\frac13|S|^2I.
}
\tag{8.1}
$$

The trace correction is diagonal, so its horizontal-normal block is simply

$$
(C_S^0)_{hn}
=
(S^2)_{hn}.
$$

Using the block matrix (6.1),

$$
\boxed{
(S^2)_{hn}
=
(H+dI_2)s_\times.
}
\tag{8.2}
$$

Because

$$
s_\times
=
\delta_c p_h,
$$

we obtain

$$
\boxed{
(C_S^0)_{hn}
=
\delta_c
(H+dI_2)p_h.
}
\tag{8.3}
$$

---

# 9. Mixed pressure-Hessian block

DCRP48 proves

$$
\boxed{
D_sc
=
-P_{zq}.
}
\tag{9.1}
$$

Since the horizontal dependence of $P_z$ occurs through $q$,

$$
\boxed{
\nabla_hP_z
=
P_{zq}p_h
=
-(D_sc)p_h.
}
\tag{9.2}
$$

The trace-free correction in

$$
H_P^0
=
\nabla^2P-\frac{\Delta P}{3}I
$$

does not alter mixed components.

Therefore

$$
\boxed{
(H_P^0)_{hn}
=
-(D_sc)p_h.
}
\tag{9.3}
$$

---

# 10. X72 affine pressure-response defect on the pancake patch

Define, as in X72 Round37,

$$
\boxed{
E_p
=
H_P^0+C_S^0.
}
\tag{10.1}
$$

Combining (8.3) and (9.3),

$$
\boxed{
(E_p)_{hn}
=
-(D_sc)p_h
+
\delta_c(H+dI_2)p_h.
}
\tag{10.2}
$$

Take the inner product with $p_h$.

By (7.2),

$$
\boxed{
p_h\cdot(E_p)_{hn}
=
-(D_sc)|\Omega_h|^2
-
\delta_c
\Omega_h\cdot S\Omega_h.
}
\tag{10.3}
$$

Hence:

## Theorem D49.2 — Response-Slope / Stretching / Pressure-Defect Identity

On every regular fully flat rank-two scalar patch,

$$
\boxed{
(D_sc)|\Omega_h|^2
+
\left(c-\frac12\right)
\Omega_h\cdot S\Omega_h
=
-
\nabla_hq\cdot(E_p)_{hn}.
}
\tag{10.4}
$$

This is exact.

No norm estimate, pressure approximation, or annular localization is used.

---

# 11. Interpretation of Theorem D49.2

Equation (10.4) says that three mechanisms are not independent:

### response-slope drift

$$
D_sc;
$$

### vorticity stretching

$$
\sigma_\omega
=
\frac{
\Omega_h\cdot S\Omega_h
}{
|\Omega_h|^2
};
$$

### X72 mixed affine pressure-response defect

$$
(E_p)_{hn}.
$$

On the active set

$$
|\Omega_h|>0,
$$

Theorem D49.2 becomes

$$
\boxed{
D_sc
+
\left(c-\frac12\right)\sigma_\omega
=
-
\frac{
\nabla_hq\cdot(E_p)_{hn}
}{
|\Omega_h|^2
}.
}
\tag{11.1}
$$

Thus a perfect mixed pressure lock gives the autonomous law

$$
\boxed{
D_sc
=
-
\left(c-\frac12\right)\sigma_\omega.
}
\tag{11.2}
$$

Positive vortex stretching drives $c$ toward the central response slope $1/2$.

---

# 12. Central response slope

At

$$
\boxed{
c=\frac12,
}
\tag{12.1}
$$

the cross-plane symmetric strain is

$$
\boxed{
s_\times=0.
}
\tag{12.2}
$$

The two cross derivatives are

$$
\nabla_hw
=
\frac12p_h,
$$

$$
\partial_zV_h
=
-\frac12p_h.
$$

Thus the entire cross-plane shear is antisymmetric.

In other words:

$$
\boxed{
c=\frac12
}
$$

is the unique response slope at which the planar-vorticity shear contributes pure local rotation and no cross-plane symmetric strain.

This explains why $c=1/2$ is invisible to the mixed cofactor factor in (8.3).

---

# 13. Constant-response perfect-lock corollary

Assume:

$$
D_sc=0,
$$

$$
(E_p)_{hn}=0,
$$

and

$$
c\neq\frac12.
$$

Then Theorem D49.2 gives

$$
\boxed{
\Omega_h\cdot S\Omega_h=0.
}
\tag{13.1}
$$

## Corollary D49.3 — Noncentral Constant Pressure-Lock Mode Has Zero Vortex Stretching

A constant-response fully flat pancake with perfect mixed X72 pressure response can sustain positive local vortex stretching only at

$$
\boxed{
c=\frac12.
}
$$

Every constant $c\neq1/2$ perfect-lock branch has zero vorticity stretching.

---

# 14. Stronger geometry of the noncentral constant-lock branch

Assume

$$
c\neq\frac12,
$$

$$
(E_p)_{hn}=0,
$$

and

$$
D_sc=0.
$$

Equation (10.2) gives

$$
\boxed{
(H+dI_2)p_h=0.
}
\tag{14.1}
$$

Since

$$
\operatorname{tr}H=-d,
$$

$p_h$ is an eigenvector of $H$ with eigenvalue $-d$.

The orthogonal planar direction

$$
Jp_h
$$

then has eigenvalue zero.

Hence

$$
\boxed{
H\Omega_h=0.
}
\tag{14.2}
$$

Because

$$
s_\times\cdot\Omega_h=0,
$$

we actually have

$$
\boxed{
S\Omega_h=0.
}
\tag{14.3}
$$

Thus the vorticity direction lies in the kernel of the full local strain tensor.

This is stronger than the scalar stretching identity.

---

# 15. DCRP35 consequence

DCRP35 gives, for every nonzero strict DSS vorticity core,

$$
\boxed{
(2-3\gamma)\mathcal O(R)
\le
\mathcal S_+(R)
+
\mathcal J_{\omega,\mathrm{in}}(R).
}
\tag{15.1}
$$

On the exact noncentral constant-response perfect-lock branch,

$$
\mathcal S_+(R)=0
$$

where the branch fills the active core.

Therefore:

## Corollary D49.4 — Noncentral Perfect-Lock Branch Requires Inward Enstrophy Turnover

If a nonzero periodic rank-two core has constant

$$
c\neq\frac12
$$

and vanishing mixed X72 affine pressure-response defect, then its recurrent enstrophy cannot be sustained by local vortex stretching.

It must satisfy

$$
\boxed{
\mathcal J_{\omega,\mathrm{in}}(R)
\ge
(2-3\gamma)\mathcal O(R)
}
\tag{15.2}
$$

up to the declared localization of the exact branch.

Thus the noncentral pressure-lock branch is automatically routed into the DCRP35 turnover channel.

---

# 16. Quantitative near-lock inequality

The exact identity also yields a stability estimate.

From (10.4),

$$
\left|
\left(c-\frac12\right)
\Omega_h\cdot S\Omega_h
+
(D_sc)|\Omega_h|^2
\right|
\le
|\Omega_h|
|(E_p)_{hn}|.
$$

If

$$
D_sc=0
$$

and

$$
|c-\tfrac12|\ge\delta>0,
$$

then

$$
\boxed{
|\Omega_h\cdot S\Omega_h|
\le
\frac{
|\Omega_h|
|(E_p)_{hn}|
}{
\delta
}.
}
\tag{16.1}
$$

Therefore near-perfect X72 pressure response suppresses local vortex stretching uniformly away from the central slope.

This creates a quantitative bridge to the DCRP35 finite-annulus/turnover lower bound.

---

# 17. Off-central response enstrophy

Define

$$
\boxed{
X_c
=
\left(c-\frac12\right)^2
|\Omega_h|^2.
}
\tag{17.1}
$$

This quantity is:

- zero exactly on the central response mode or zero-vorticity set;
- gauge invariant on the DCRP44 canonical flat branch;
- sensitive to the distance from the pressure/cofactor-invisible slope.

---

# 18. Similarity vorticity amplitude equation

Curl the similarity Euler equation.

The vorticity satisfies

$$
\boxed{
D_s\Omega+\Omega
=
(\Omega\cdot\nabla)V.
}
\tag{18.1}
$$

Taking the squared norm,

$$
\boxed{
D_s|\Omega|^2
=
2\Omega\cdot S\Omega
-
2|\Omega|^2.
}
\tag{18.2}
$$

On the planar active branch,

$$
|\Omega|=|\Omega_h|.
$$

---

# 19. Exact off-central defect-energy law

Let

$$
\delta_c=c-\frac12.
$$

Theorem D49.2 gives

$$
\boxed{
(D_s\delta_c)|\Omega|^2
+
\delta_c
\Omega\cdot S\Omega
=
-
p_h\cdot(E_p)_{hn}.
}
\tag{19.1}
$$

Differentiate

$$
X_c=\delta_c^2|\Omega|^2.
$$

Then

$$
\begin{aligned}
D_sX_c
&=
2\delta_c(D_s\delta_c)|\Omega|^2
+
\delta_c^2D_s|\Omega|^2
\\
&=
-2\delta_c^2
\Omega\cdot S\Omega
-
2\delta_c p_h\cdot(E_p)_{hn}
\\
&\qquad
+
2\delta_c^2
\Omega\cdot S\Omega
-
2\delta_c^2|\Omega|^2.
\end{aligned}
$$

The stretching terms cancel exactly.

Hence:

## Theorem D49.5 — Off-Central Response Defect-Energy Identity

$$
\boxed{
D_sX_c+2X_c
=
-2
\left(c-\frac12\right)
\nabla_hq\cdot(E_p)_{hn}.
}
\tag{19.2}
$$

This exact cancellation is the strongest result of the round.

---

# 20. Conservative form

Because

$$
\nabla\cdot W=3\gamma,
$$

$$
\partial_sX_c+\nabla\cdot(WX_c)
=
D_sX_c+3\gamma X_c.
$$

Using Theorem D49.5,

$$
\boxed{
\partial_sX_c
+
\nabla\cdot(WX_c)
+
(2-3\gamma)X_c
=
-2
\left(c-\frac12\right)
\nabla_hq\cdot(E_p)_{hn}.
}
\tag{20.1}
$$

The coefficient is

$$
\boxed{
2-3\gamma>0.
}
\tag{20.2}
$$

It is exactly the DCRP35 enstrophy-demand coefficient.

This identifies $X_c$ as a refined enstrophy-type density.

---

# 21. Perfect mixed-pressure lock

If

$$
\boxed{
(E_p)_{hn}=0,
}
\tag{21.1}
$$

then Theorem D49.5 reduces to

$$
\boxed{
D_sX_c=-2X_c.
}
\tag{21.2}
$$

Therefore along every material/similarity characteristic contained in the perfect-lock flat patch,

$$
\boxed{
X_c(s)
=
e^{-2(s-s_0)}
X_c(s_0).
}
\tag{21.3}
$$

This is independent of $\gamma$.

In conservative variables,

$$
\boxed{
\partial_sX_c
+
\nabla\cdot(WX_c)
+
(2-3\gamma)X_c
=
0.
}
\tag{21.4}
$$

Thus Eulerian periodic recurrence of nonzero off-central response requires inward transport.

---

# 22. Periodic fixed-domain balance

Let $D$ be a fixed smooth similarity domain contained in the regular flat patch.

Integrate (20.1) over one period.

Periodicity removes the time boundary term:

$$
\boxed{
\begin{aligned}
(2-3\gamma)
\int_0^{S_0}\int_DX_c\,dy\,ds
&=
-\int_0^{S_0}
\int_{\partial D}
X_cW\cdot n\,dS\,ds
\\
&\quad
-2
\int_0^{S_0}\int_D
\delta_c
p_h\cdot(E_p)_{hn}
\,dy\,ds.
\end{aligned}
}
\tag{22.1}
$$

Define

$$
\boxed{
\mathcal J_c(D)
=
\int_0^{S_0}
\int_{\partial D}
X_cW\cdot n\,dS\,ds.
}
\tag{22.2}
$$

Then inward off-central transport corresponds to

$$
\mathcal J_c(D)<0.
$$

---

# 23. Off-central turnover / pressure-defect theorem

From (22.1),

$$
\boxed{
\begin{aligned}
(2-3\gamma)
\int_0^{S_0}\int_DX_c
\le
&
\left(-\mathcal J_c(D)\right)_+
\\
&+
2
\int_0^{S_0}\int_D
|\delta_c|
|\Omega_h|
|(E_p)_{hn}|.
\end{aligned}
}
\tag{23.1}
$$

Therefore:

## Theorem D49.6 — Off-Central Response Turnover / Pressure-Defect Alternative

Every nonzero periodic flat core with

$$
X_c\not\equiv0
$$

must have at least one of:

$$
\boxed{
\text{inward off-central response transport}
}
$$

or

$$
\boxed{
\text{nonzero mixed X72 affine pressure-response defect work}.
}
$$

No third local source appears in the exact balance.

---

# 24. Central-mode rigidity under zero source

If

$$
\boxed{
\mathcal J_c(D)\ge0
}
\tag{24.1}
$$

(no net inward off-central response supply) and

$$
\boxed{
(E_p)_{hn}=0
}
\tag{24.2}
$$

throughout the periodic domain, then (22.1) gives

$$
\boxed{
X_c=0
}
\tag{24.3}
$$

almost everywhere.

On the active rank-two set,

$$
|\Omega_h|>0,
$$

hence:

## Corollary D49.7 — Central Response Rigidity

$$
\boxed{
c=\frac12.
}
\tag{24.4}
$$

Thus the central response slope is forced whenever both the mixed pressure-response defect and inward off-central turnover are removed.

---

# 25. Why $c=1/2$ is an invisible direction

At

$$
c=\frac12,
$$

the cross-plane symmetric strain vanishes:

$$
s_\times=0.
$$

The cofactor mixed block

$$
(C_S^0)_{hn}
=
\delta_c(H+dI)p_h
$$

also vanishes regardless of $H$.

Therefore the X72 mixed affine-response channel cannot detect vortex stretching through this block.

This is a genuine **mixed cofactor invisible direction**.

The remaining strain acting on $\Omega_h$ is entirely the in-plane Hessian block $H$.

Hence future closure of the central mode must use a different pressure/cofactor component, PFET, annular turnover, or the full vorticity-stress realizability machinery.

---

# 26. Relation to DCRP35

DCRP35's enstrophy balance is

$$
\boxed{
(2-3\gamma)\mathcal O(D)
\le
\mathcal S_+(D)
+
\mathcal J_{\omega,\mathrm{in}}(D).
}
\tag{26.1}
$$

DCRP49 now supplies the refined off-central balance

$$
\boxed{
(2-3\gamma)\mathcal O_c(D)
\le
\mathcal J_{c,\mathrm{in}}(D)
+
\mathcal D_{E,\mathrm{mix}}(D),
}
\tag{26.2}
$$

where

$$
\mathcal O_c
=
\int
\left(c-\frac12\right)^2|\Omega|^2,
$$

and

$$
\mathcal D_{E,\mathrm{mix}}
=
2\int
|\delta_c||\Omega||(E_p)_{hn}|.
$$

Thus:

- total enstrophy can be sustained by stretching or turnover;
- **off-central response enstrophy** can be sustained only by turnover or mixed pressure-response defect.

This is a strictly finer observer.

---

# 27. Relation to DCRP48 pressure-Hessian dynamics

DCRP48 gave

$$
D_sc=-P_{zq}.
$$

DCRP49 shows that this pressure-driven slope motion is not independent of strain and the X72 pressure/cofactor mismatch.

Equation (10.4) may be rewritten:

$$
\boxed{
P_{zq}|\Omega|^2
-
\left(c-\frac12\right)
\Omega\cdot S\Omega
=
\nabla_hq\cdot(E_p)_{hn}.
}
\tag{27.1}
$$

Thus the mixed pressure Hessian equals the amount required to reconcile:

- off-central shear response;
- actual vortex stretching;
- non-affine pressure response.

This gives a physical meaning to the DCRP48 mixed-pressure telescoping term.

---

# 28. Relation to X72 Round37

X72 Round37 defines

$$
E_p=H_p^0+C_S^0
$$

as the affine pressure-response defect.

DCRP49 identifies one particular component of that five-dimensional tensor as a direct rank-two pancake closure variable:

$$
\boxed{
\mathsf E_{\rm pan}
=
P_hE_pn.
}
\tag{28.1}
$$

Its longitudinal pairing with

$$
p_h
$$

is exactly the forcing in the off-central response energy law.

Therefore the DCRP branch has now reached a specific X72 coordinate rather than an abstract “pressure matters” handoff.

---

# 29. PFET remains separate

The affine witness of Sections 1–4 proves that no universal identity can merge

$$
\boxed{
\mathsf O_{\rm PFET}
}
$$

and

$$
\boxed{
\mathsf E_{\rm pan}.
}
$$

Hence the final finite-annulus observer package now has at least three distinct coordinates:

$$
\boxed{
\mathsf O_{49}
=
\left(
\mathsf O_{\rm PFET},
\mathcal J_{c,\mathrm{in}},
\mathsf E_{\rm pan}
\right).
}
\tag{29.1}
$$

A complete closure theorem must use their joint realizability, not identify them.

---

# 30. Updated final rank-two branch

After DCRP49 the final regular flat survivor satisfies the following alternative:

$$
\boxed{
\begin{aligned}
&
\text{central response}
\quad
c=\frac12
\\
&\vee
\\
&
\text{inward off-central response turnover}
\\
&\vee
\\
&
\text{nonzero mixed affine pressure-response defect}
\\
&\vee
\\
&
\text{flat-chart / rank transition}.
\end{aligned}
}
$$

In addition DCRP31 still requires finite inward PFET, and DCRP35 still requires total enstrophy replenishment.

The most rigid remaining equality state is therefore:

$$
\boxed{
c=\frac12,
\qquad
(E_p)_{hn}=0,
}
$$

with the cross-plane shear purely rotational.

This is the natural next target.

---

# 31. Status ledger

## PROVED this round

### D49-P1 — PFET/Neumann independence witness

There is an exact affine Euler flow with zero PFET and strictly nonzero pressure-Neumann flux.

### D49-P2 — Exact mixed affine pressure-response identity

$$
(D_sc)|\Omega|^2
+
(c-\tfrac12)\Omega\cdot S\Omega
=
-\nabla_hq\cdot(E_p)_{hn}.
$$

### D49-P3 — Noncentral constant perfect-lock zero stretching

For constant $c\neq1/2$ and $(E_p)_{hn}=0$,

$$
S\Omega=0.
$$

### D49-P4 — DCRP35 turnover consequence

A noncentral constant perfect-lock periodic core must use inward enstrophy turnover.

### D49-P5 — Exact off-central response defect energy

$$
D_sX_c+2X_c
=
-2(c-\tfrac12)\nabla_hq\cdot(E_p)_{hn}.
$$

### D49-P6 — Conservative off-central balance

$$
\partial_sX_c
+
\nabla\cdot(WX_c)
+
(2-3\gamma)X_c
=
-2(c-\tfrac12)\nabla_hq\cdot(E_p)_{hn}.
$$

### D49-P7 — Turnover / pressure-defect alternative

Every recurrent nonzero off-central response requires inward $X_c$ transport or mixed X72 pressure-response defect.

### D49-P8 — Central response rigidity

Removing both sources forces

$$
c=\frac12
$$

on the active vorticity set.

---

# 32. Closed / corrected routes

## Closed

A universal PFET / pressure-Neumann coupling theorem is impossible.

## Closed

A universal identification of the X72 pressure-response defect with PFET is impossible.

## Improved route

The DCRP pressure problem should now use the exact mixed component

$$
P_hE_pn
$$

rather than a generic pressure-Hessian norm.

---

# 33. New STOP

$$
\boxed{
\textbf{
STOP-D49:
The final noncentral flat-pancake response cannot be maintained for free: its off-central response enstrophy has the exact DCRP35 damping coefficient and must be replenished either by inward turnover or by the mixed X72 affine pressure-response defect. With both channels removed, the only active response is the invisible central slope }c=\frac12.
}
$$

---

# 34. Next autonomous step

## DCRP50 — Central Response / Invisible-Direction Closure

**Working title**

> **Central $c=\frac12$ Pancake Mode, Pure Rotational Cross-Shear, and Pressure/Vorticity-Stress Realizability**

Primary tasks:

1. impose
   $$
   c=\frac12
   $$
   and derive the exact reduced flat equations;
2. exploit
   $$
   s_\times=0
   $$
   so the cross-plane velocity gradient is purely antisymmetric;
3. compute the remaining components of
   $$
   E_p=H_p^0+C_S^0;
   $$
4. determine whether the central invisible mode is compatible with:
   - DCRP35 positive stretching requirement;
   - DCRP31 inward PFET;
   - X72 vorticity-stress realizability;
5. if the remaining pressure/cofactor system still has an exact local witness, classify that witness and hand it into X72 Round43's vorticity-realizability tower.

Desired endpoint:

$$
\boxed{
\text{central exact model}
\ \vee\
\text{pressure/cofactor defect}
\ \vee\
\text{turnover}
\ \vee\
\text{X72 realizability obstruction}.
}
$$

---

# 35. One-line checkpoint

PFET and pressure-Neumann flux are provably independent, but the DCRP rank-two branch now couples exactly to X72: every noncentral response carries an off-central enstrophy density whose periodic recurrence requires inward turnover or mixed affine pressure-response defect, leaving $c=1/2$ as the unique pressure/cofactor-invisible central survivor.

---

**End checkpoint:** DCRP49  
**Next:** DCRP50 — Central Response / Invisible-Direction Closure.
