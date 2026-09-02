# NS-DCRP-25 — Pressure-Compatible SGS Energy Rigidity, Affine-Kernel Collapse, and the Remaining Work-Orthogonality Branch

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. analyze the pressure-compatible Reynolds-covariance kernel isolated in DCRP-24;
  2. derive the exact subgrid kinetic-energy equation including viscosity;
  3. prove that pressure-compatible covariance has no bulk SGS production;
  4. prove that zero subgrid viscous variance forces an affine velocity profile;
  5. exclude every nonzero affine strong profile on the bounded-reservoir blowup branch by inherited Morrey energy growth;
  6. isolate the genuinely remaining active-stress/work-orthogonality branch.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - Gregory L. Eyink and Hussein Aluie, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, arXiv:0909.2386;
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-23 bounded-lag increment activation;
  - DCRP-24 fiber completion and covariance rigidity;
  - MORP bounded normalized obstruction architecture.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-24 reduced the strong increment-profile branch to a nonzero actual Reynolds covariance:

$$
\boxed{
R_\ell[u]
\neq0.
}
\tag{1.1}
$$

It then isolated the pressure-compatible kernel:

$$
\boxed{
\nabla\times\nabla\cdot R_\ell=0.
}
\tag{1.2}
$$

On a simply connected core:

$$
\boxed{
\nabla\cdot R_\ell
=
\nabla q.
}
\tag{1.3}
$$

Let:

$$
U_\ell
=
S_\ell u,
$$

$$
P_\ell
=
S_\ell p,
$$

and:

$$
R_\ell
=
S_\ell(u\otimes u)
-
U_\ell\otimes U_\ell.
$$

Define the SGS kinetic energy:

$$
\boxed{
k_\ell
=
\frac12
\operatorname{tr}R_\ell
=
\frac12
\left(
S_\ell|u|^2
-
|U_\ell|^2
\right).
}
\tag{1.4}
$$

Define the SGS viscous variance:

$$
\boxed{
d_\ell
=
S_\ell|\nabla u|^2
-
|\nabla U_\ell|^2.
}
\tag{1.5}
$$

Because:

$$
\nabla U_\ell
=
S_\ell\nabla u,
$$

one has:

$$
\boxed{
d_\ell(x,t)
=
\int
\varphi_\ell(z)
\left|
\nabla u(x-z,t)
-
\nabla U_\ell(x,t)
\right|^2
dz
\ge0.
}
\tag{1.6}
$$

The exact SGS kinetic-energy balance is:

$$
\boxed{
\partial_tk_\ell
+
\nabla\cdot J_\ell
=
\nu\Delta k_\ell
-
\nu d_\ell
+
\Pi_\ell,
}
\tag{1.7}
$$

where:

$$
\boxed{
\Pi_\ell
=
-
R_\ell:\nabla U_\ell
}
\tag{1.8}
$$

is the signed coarse energy flux.

If the covariance is pressure-compatible:

$$
\nabla\cdot R_\ell
=
\nabla q,
$$

then:

$$
\boxed{
\Pi_\ell
=
\nabla\cdot
(
qU_\ell
-
R_\ell U_\ell
).
}
\tag{1.9}
$$

Hence:

$$
\boxed{
\partial_tk_\ell
+
\nabla\cdot
J_\ell^{pc}
=
\nu\Delta k_\ell
-
\nu d_\ell.
}
\tag{1.10}
$$

Therefore:

$$
\boxed{
\textbf{
pressure-compatible increment covariance has no bulk SGS-energy production.
}
}
\tag{1.11}
$$

It can only transport SGS energy through the boundary, diffuse SGS energy, or pay the positive viscous SGS variance.

The second main theorem is the affine-kernel rigidity:

> If:
>
> $$
> d_\ell=0
> $$
>
> almost everywhere on a connected interior spacetime region for one positive mollifier scale, then:
>
> $$
> \boxed{
> u(x,t)
> =
> A(t)x+b(t)
> }
> $$
>
> locally in space for almost every time.

Thus the zero-SGS-dissipation kernel is finite dimensional.

The third main theorem removes this affine kernel from the bounded-reservoir singular branch.

Let:

$$
u^{(n)}(y,s)
=
r_n
u
\left(
x_n+r_ny,
t_n+r_n^2s
\right)
$$

be a singular-rooted normalized sequence satisfying the bounded-reservoir condition of DCRP-23 at every late nested scale.

Then for each fixed dyadic:

$$
R\ge1,
$$

$$
\boxed{
\operatorname*{ess\,sup}_{s}
\int_{B_R}
|u^{(n)}(y,s)|^2dy
\le
C
M_0R.
}
\tag{1.12}
$$

Any local strong profile limit therefore inherits:

$$
\boxed{
\int_{B_R}
|u_\infty(y,s)|^2dy
\le
CM_0R.
}
\tag{1.13}
$$

But if:

$$
u_\infty(y,s)
=
A(s)y+b(s),
$$

then:

$$
\boxed{
\int_{B_R}
|A y+b|^2dy
=
c_1
|A|_F^2
R^5
+
c_2
|b|^2
R^3.
}
\tag{1.14}
$$

The growth law:

$$
O(R)
$$

forces:

$$
\boxed{
A=0,
\qquad
b=0.
}
\tag{1.15}
$$

Therefore:

$$
\boxed{
\textbf{
bounded-reservoir strong profile}
+
\textbf{
zero SGS viscous variance}
\Longrightarrow
\textbf{
zero increment profile}.
}
}
\tag{1.16}
$$

Combining with DCRP-24, a nonzero pressure-compatible strong increment profile must satisfy:

$$
\boxed{
\begin{aligned}
&
\textbf{
positive SGS viscous variance}
\\
&\vee\
\textbf{
SGS boundary/localization transport}
\\
&\vee\
\textbf{
critical-reservoir noncompactness}.
\end{aligned}
}
\tag{1.17}
$$

The first alternative is a real physical viscous tax.

The second is an explicit localization/transition channel.

The third is the already-known unbounded-reservoir branch.

This substantially closes the pressure-compatible covariance kernel on the bounded-reservoir compact branch.

The remaining bounded-reservoir strong-profile problem is narrower:

$$
\boxed{
\textbf{
active covariance with vanishing useful work efficiency.
}
}
\tag{1.18}
$$

That means:

$$
\nabla\times\nabla\cdot R_\ell
\neq0,
$$

but its force can remain nearly orthogonal to the filtered vorticity and/or its stress can remain nearly work-orthogonal to the coarse strain.

The next exact frontier is:

$$
\boxed{
\textbf{
Active-Stress Work-Orthogonality / Dual-Efficiency Rigidity Lemma}.
}
\tag{1.19}
$$

---

# 2. Filtered momentum equation

Let:

$$
S_\ell f
=
\varphi_\ell*f,
$$

where:

$$
\varphi_\ell
$$

is a smooth nonnegative spatial mollifier with unit mass.

Define:

$$
U_\ell
=
S_\ell u,
$$

$$
P_\ell
=
S_\ell p,
$$

and:

$$
R_\ell
=
S_\ell(u\otimes u)
-
U_\ell\otimes U_\ell.
$$

The exact filtered Navier--Stokes equation is:

$$
\boxed{
\partial_tU_\ell
-
\nu\Delta U_\ell
+
\nabla\cdot
(
U_\ell\otimes U_\ell
)
+
\nabla P_\ell
=
-\nabla\cdot R_\ell.
}
\tag{2.1}
$$

---

# 3. Fine and coarse kinetic-energy equations

Let:

$$
e
=
\frac12|u|^2.
$$

For a smooth pre-singularity solution:

$$
\boxed{
\partial_te
+
\nabla\cdot
\left[
(e+p)u
\right]
=
\nu\Delta e
-
\nu|\nabla u|^2.
}
\tag{3.1}
$$

Filter:

$$
\boxed{
\partial_tS_\ell e
+
\nabla\cdot
S_\ell
\left[
(e+p)u
\right]
=
\nu\Delta S_\ell e
-
\nu S_\ell|\nabla u|^2.
}
\tag{3.2}
$$

Let:

$$
e_\ell
=
\frac12
|U_\ell|^2.
$$

Dot the filtered momentum equation with:

$$
U_\ell.
$$

Then:

$$
\boxed{
\partial_te_\ell
+
\nabla\cdot
\left[
(e_\ell+P_\ell)U_\ell
+
R_\ell U_\ell
\right]
=
\nu\Delta e_\ell
-
\nu|\nabla U_\ell|^2
+
R_\ell:\nabla U_\ell.
}
\tag{3.3}
$$

---

# 4. SGS kinetic energy and positivity

Define:

$$
\boxed{
k_\ell
=
S_\ell e
-
e_\ell.
}
\tag{4.1}
$$

Taking the trace of:

$$
R_\ell
$$

gives:

$$
\boxed{
k_\ell
=
\frac12
\operatorname{tr}R_\ell.
}
\tag{4.2}
$$

Because:

$$
R_\ell
$$

is a covariance tensor for a nonnegative mollifier:

$$
\boxed{
R_\ell
\ge0
}
\tag{4.3}
$$

and:

$$
\boxed{
k_\ell\ge0.
}
\tag{4.4}
$$

---

# 5. SGS viscous variance

Define:

$$
\boxed{
d_\ell
=
S_\ell|\nabla u|^2
-
|\nabla U_\ell|^2.
}
\tag{5.1}
$$

Because convolution commutes with differentiation:

$$
\nabla U_\ell
=
S_\ell\nabla u.
$$

Therefore:

$$
\boxed{
d_\ell
=
\int
\varphi_\ell(z)
\left|
\nabla u(x-z)
-
\nabla U_\ell(x)
\right|^2dz
\ge0.
}
\tag{5.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Exact SGS kinetic-energy balance

Define:

$$
\boxed{
\Pi_\ell
=
-
R_\ell:\nabla U_\ell
}
\tag{6.1}
$$

and:

$$
\boxed{
J_\ell
=
S_\ell
\left[
(e+p)u
\right]
-
(e_\ell+P_\ell)U_\ell
-
R_\ell U_\ell.
}
\tag{6.2}
$$

Subtract (3.3) from (3.2):

$$
\boxed{
\partial_tk_\ell
+
\nabla\cdot J_\ell
=
\nu\Delta k_\ell
-
\nu d_\ell
+
\Pi_\ell.
}
\tag{6.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the standard exact smooth coarse-grained SGS energy structure, here with viscosity retained explicitly.

---

# 7. Pressure-compatible covariance makes the filtered field an exact NSE solution

Assume on a simply connected core:

$$
\boxed{
\nabla\times\nabla\cdot R_\ell=0.
}
\tag{7.1}
$$

Then:

$$
\boxed{
\nabla\cdot R_\ell
=
\nabla q.
}
\tag{7.2}
$$

The filtered momentum equation becomes:

$$
\boxed{
\partial_tU_\ell
-
\nu\Delta U_\ell
+
(U_\ell\cdot\nabla)U_\ell
+
\nabla
(
P_\ell+q
)
=
0.
}
\tag{7.3}
$$

Thus:

$$
\boxed{
\textbf{
the filtered velocity itself solves the exact Navier--Stokes equation locally,
with a modified pressure.
}
}
\tag{7.4}
$$

---

# 8. Pressure-compatible SGS energy reduction

Since:

$$
\nabla\cdot R_\ell
=
\nabla q,
$$

$$
\nabla\cdot
(
R_\ell U_\ell
)
=
\nabla q\cdot U_\ell
+
R_\ell:\nabla U_\ell.
$$

Because:

$$
\nabla\cdot U_\ell=0,
$$

$$
\nabla q\cdot U_\ell
=
\nabla\cdot(qU_\ell).
$$

Therefore:

$$
\boxed{
\Pi_\ell
=
\nabla\cdot
(
qU_\ell
-
R_\ell U_\ell
).
}
\tag{8.1}
$$

Insert in (6.3).

The divergence correction cancels the:

$$
R_\ell U_\ell
$$

piece of:

$$
J_\ell.
$$

Hence:

$$
\boxed{
\partial_tk_\ell
+
\nabla\cdot
J_\ell^{pc}
=
\nu\Delta k_\ell
-
\nu d_\ell,
}
\tag{8.2}
$$

with:

$$
\boxed{
J_\ell^{pc}
=
S_\ell
\left[
(e+p)u
\right]
-
(e_\ell+P_\ell+q)U_\ell.
}
\tag{8.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. Local pressure-compatible SGS ledger

Let:

$$
\chi\ge0
$$

be a smooth compact spacetime cutoff.

Multiply (8.2) by:

$$
\chi
$$

and integrate in space:

$$
\boxed{
\frac d{dt}
\int
\chi k_\ell
+
\nu
\int
\chi d_\ell
=
\int
(
\partial_t\chi
+
\nu\Delta\chi
)
k_\ell
+
\int
\nabla\chi
\cdot
J_\ell^{pc}.
}
\tag{9.1}
$$

Define:

$$
\boxed{
\mathcal D_{r,\ell}^{sgs}
=
\nu
r^{-1}
\iint_{Q_r}
\chi
d_\ell
dxdt.
}
\tag{9.2}
$$

Let:

$$
\boxed{
\mathcal L_{r,\ell}^{sgs}
}
$$

be the corresponding normalized cutoff/transport budget.

Then pressure-compatible recurrence has only:

$$
\boxed{
\text{SGS endpoint change}
+
\mathcal D^{sgs}
=
\text{localization/transport}.
}
\tag{9.3}
$$

There is no bulk SGS source.

---

# 10. SGS viscous tax is physical Navier--Stokes dissipation

Because:

$$
d_\ell
\le
S_\ell|\nabla u|^2,
$$

for a compact filter and core cutoff:

$$
\boxed{
\mathcal D_{r,\ell}^{sgs}
\le
C_{\sigma,\chi}
\nu
r^{-1}
\iint_{Q_r^{+}}
|\nabla u|^2dxdt.
}
\tag{10.1}
$$

Thus any scale-uniform positive SGS viscous variance is a portion of the ordinary physical viscous depletion.

It is not a new artificial cost.

---

# 11. Zero SGS variance is locally affine

Suppose:

$$
d_\ell(x,t)=0.
$$

From (5.2):

$$
\boxed{
\nabla u(x-z,t)
=
\nabla U_\ell(x,t)
}
\tag{11.1}
$$

for:

$$
\varphi_\ell\text{-a.e. }z.
$$

If:

$$
\varphi_\ell>0
$$

on an open filter ball, the gradient is constant almost everywhere on that translated ball.

---

# 12. Zero-SGS-Dissipation Affine Rigidity Theorem

Let:

$$
G^+
$$

be connected.

Assume:

$$
\varphi_\ell>0
$$

almost everywhere on:

$$
B_\ell.
$$

If:

$$
\boxed{
d_\ell=0
}
\tag{12.1}
$$

almost everywhere on:

$$
G^+\times I,
$$

then for almost every:

$$
t\in I,
$$

there are:

$$
A(t)\in\mathbb R^{3\times3},
\qquad
b(t)\in\mathbb R^3,
$$

such that on every connected inner region whose filter balls stay in:

$$
G^+,
$$

$$
\boxed{
u(x,t)
=
A(t)x+b(t).
}
\tag{12.2}
$$

Incompressibility gives:

$$
\boxed{
\operatorname{tr}A(t)=0.
}
\tag{12.3}
$$

### Proof

At almost every point:

$$
x,
$$

the gradient is a.e. constant on:

$$
B_\ell(x).
$$

Overlapping filter balls force their constants to agree.

Connectedness propagates one matrix:

$$
A(t)
$$

across the inner region.

A function with constant weak gradient is affine.

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

# 13. Strong-profile zero-dissipation kernel

Suppose a normalized resolved strong-profile sequence satisfies:

$$
u^{(n)}
\to
u_\infty
$$

locally in a topology sufficient to identify the resolved covariance and the SGS gradient variance.

If:

$$
\boxed{
\mathcal D_{\sigma}^{sgs}[u^{(n)}]
\to0
}
\tag{13.1}
$$

on every fixed compact inner cylinder, then the nonnegative variance passes to the limit:

$$
\boxed{
d_\sigma[u_\infty]=0.
}
\tag{13.2}
$$

Therefore:

$$
\boxed{
u_\infty(y,s)
=
A(s)y+b(s).
}
\tag{13.3}
$$

The zero-SGS-dissipation strong-profile kernel is finite dimensional.

---

# 14. Bounded-reservoir Morrey growth

Normalize:

$$
\boxed{
u^{(n)}(y,s)
=
r_n
u
\left(
x_n+r_ny,
t_n+r_n^2s
\right).
}
\tag{14.1}
$$

Assume the DCRP-23 bounded-reservoir condition holds at every sufficiently late scale of a controlled-drift nested chain:

$$
\boxed{
A_{k,\sigma}^{+}
\le
M_0.
}
\tag{14.2}
$$

Fix a dyadic:

$$
R=\theta^{-m}\ge1.
$$

For:

$$
n
$$

large relative to fixed:

$$
m,
$$

the physical ball:

$$
B_{Rr_n}(x_n)
$$

is contained in a fixed enlargement of the ancestor window at scale:

$$
Rr_n.
$$

Hence:

$$
\boxed{
\int_{B_R}
|
u^{(n)}(y,s)
|^2dy
\le
CM_0R.
}
\tag{14.3}
$$

Any local strong limit inherits:

$$
\boxed{
\int_{B_R}
|u_\infty(y,s)|^2dy
\le
CM_0R
\qquad
\forall R\ge1.
}
\tag{14.4}
$$

Status:

$$
\boxed{
\textbf{PROVED under the DCRP-23 bounded-reservoir controlled-drift hypothesis}.
}
$$

---

# 15. Affine energy growth

For:

$$
u_{\rm aff}(y)
=
Ay+b,
$$

on a centered ball:

$$
\boxed{
\int_{B_R}
|Ay+b|^2dy
=
c_1
|A|_F^2
R^5
+
c_2
|b|^2
R^3.
}
\tag{15.1}
$$

The cross term vanishes by symmetry.

---

# 16. Morrey Exclusion of the Affine Kernel

If:

$$
u_\infty(y,s)
=
A(s)y+b(s)
$$

and:

$$
\boxed{
\int_{B_R}
|u_\infty(y,s)|^2dy
\le
CM_0R
\qquad
\forall R\ge1,
}
\tag{16.1}
$$

then:

$$
\boxed{
A(s)=0,
\qquad
b(s)=0
}
\tag{16.2}
$$

for almost every:

$$
s.
$$

### Proof

Combine (15.1) and (16.1), divide by:

$$
R,
$$

and send:

$$
R\to\infty.
$$

The:

$$
R^4
$$

and:

$$
R^2
$$

growth forces:

$$
A=b=0.
$$

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

# 17. Nonzero affine increment profiles are impossible on the bounded-reservoir branch

If:

$$
u_\infty=0,
$$

then all actual increments vanish:

$$
\delta_zu_\infty=0.
$$

Hence:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u_\infty]=0.
}
\tag{17.1}
$$

Therefore a strong resolved profile with:

$$
\boxed{
\widetilde{\mathcal S}^{(3)}[u_\infty]>0
}
\tag{17.2}
$$

cannot satisfy both:

$$
d_\sigma[u_\infty]=0
$$

and the bounded-reservoir Morrey growth.

Equivalently:

$$
\boxed{
\textbf{
nonzero bounded-reservoir strong increment profile}
\Longrightarrow
\textbf{
positive SGS gradient variance}.
}
}
\tag{17.3}
$$

---

# 18. Pressure-Compatible Strong-Profile Alternative

Let:

$$
u_\infty
$$

be a nonzero resolved strong increment profile on the bounded-reservoir branch, with:

$$
\widetilde{\mathcal S}^{(3)}[u_\infty]>0.
$$

Assume:

$$
\boxed{
\nabla\times\nabla\cdot
R_\sigma[u_\infty]
=
0.
}
\tag{18.1}
$$

Then at least one of the following occurs along the approximating singular sequence.

### A. positive SGS viscous tax

$$
\boxed{
\liminf_n
\mathcal D_{n,\sigma}^{sgs}
>
0;
}
\tag{18.2}
$$

### B. positive SGS localization/transport

$$
\boxed{
\liminf_n
\mathcal L_{n,\sigma}^{sgs}
>
0;
}
\tag{18.3}
$$

### C. loss of bounded-reservoir compactness

the Morrey/local-energy growth hypothesis fails on some expanding normalized scale.

### Proof

If A and B fail on a compact resolved strong-profile branch, the local SGS gradient variance vanishes in the limit.

The affine-rigidity theorem gives:

$$
u_\infty=Ay+b.
$$

The bounded-reservoir Morrey growth then forces:

$$
u_\infty=0.
$$

This contradicts:

$$
\widetilde{\mathcal S}^{(3)}[u_\infty]>0.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED on the resolved strong-profile branch}.
}
$$

---

# 19. Exact recurrent-window corollary

Integrate (9.1) over:

$$
[t_0,t_1].
$$

Then:

$$
\boxed{
K_\ell(t_1)
-
K_\ell(t_0)
+
\mathcal D_\ell^{sgs}
=
\mathcal L_\ell^{sgs},
}
\tag{19.1}
$$

where:

$$
K_\ell(t)
=
\int
\chi
k_\ell.
$$

Thus if a synchronized pressure-compatible return has:

$$
\boxed{
K_\ell(t_1)=K_\ell(t_0),
}
\tag{19.2}
$$

and:

$$
\boxed{
\mathcal L_\ell^{sgs}=0,
}
\tag{19.3}
$$

then:

$$
\boxed{
\mathcal D_\ell^{sgs}=0.
}
\tag{19.4}
$$

The affine/Morrey rigidity applies.

This is the correct irreversibility statement for the pressure-compatible kernel.

---

# 20. Pressure-compatible covariance need not vanish algebraically

The condition:

$$
\nabla\cdot R=\nabla q
$$

alone does not force:

$$
R=0.
$$

For example:

$$
\boxed{
R=fI,
\qquad
f\ge0,
}
\tag{20.1}
$$

satisfies:

$$
\nabla\cdot R=\nabla f.
$$

Also:

$$
R:\nabla U
=
f
\nabla\cdot U
=
0.
$$

Thus nonzero positive-semidefinite pressure-compatible stresses exist algebraically.

The present theorem excludes only a persistent **actual increment realization** of this kernel when:

- physical SGS dissipation vanishes;
- localization vanishes;
- normalized reservoirs remain compact.

---

# 21. Remaining active-stress kernel

The pressure-compatible kernel has now been reduced to paid/noncompact alternatives.

The remaining strong-profile branch has:

$$
\boxed{
\nabla\times\nabla\cdot R
\neq0.
}
\tag{21.1}
$$

There are two signed work pairings.

### coarse energy work

$$
\boxed{
\Pi
=
-R:\nabla U.
}
\tag{21.2}
$$

### coarse vorticity work

$$
\boxed{
W_\omega
=
-\Omega\cdot
\nabla\times\nabla\cdot R.
}
\tag{21.3}
$$

A dynamically active covariance can still have both pairings small through geometric/phase orthogonality.

Thus:

$$
\boxed{
\textbf{
non-pressure-compatible covariance}
\not\Rightarrow
\textbf{
large signed work}.
}
\tag{21.4}
$$

This is the next kernel.

---

# 22. Dual efficiency

Define a candidate joint efficiency:

$$
\boxed{
\mathfrak E_{\rm dual}
=
\frac{
(\Pi)_+
+
(W_\omega)_+
}{
\mathcal S_{\rm inc}
+
\varepsilon
},
}
\tag{22.1}
$$

where:

$$
\mathcal S_{\rm inc}
$$

is a normalized increment/covariance size.

Then:

### efficient active stress

$$
\limsup
\mathfrak E_{\rm dual}>0
$$

feeds the existing PFET / filtered-vorticity work ledgers.

### work-orthogonal active stress

$$
\mathfrak E_{\rm dual}\to0
$$

while:

$$
\nabla\times\nabla\cdot R\neq0.
$$

The latter requires a new rigidity theorem.

---

# 23. Updated branch split

A persistent local singular branch is reduced to:

### Branch I — critical reservoir blowup

$$
\boxed{
\limsup_k
(
A_k+D_k
)
=
+\infty.
}
\tag{23.1}
$$

### Branch II — bounded-reservoir persistent increment structure

$$
\boxed{
\widetilde{\mathcal S}^{(3)}_k
\ge
s_\ast>0.
}
\tag{23.2}
$$

Inside Branch II, after DCRP-24/25:

$$
\boxed{
\begin{aligned}
&
\text{fiber escape}
\\
&\vee
\text{Young oscillation/concentration}
\\
&\vee
\text{covariance defect}
\\
&\vee
\text{SGS viscous/localization payment}
\\
&\vee
\text{active work-orthogonal covariance}.
\end{aligned}
}
\tag{23.3}
$$

The pressure-compatible zero-tax affine kernel is eliminated on the bounded-reservoir compact branch.

---

# 24. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Active-Stress Work-Orthogonality / Dual-Efficiency Rigidity Lemma}.
}
$$

A useful theorem would be:

> Let a bounded-reservoir strong increment profile satisfy:
>
> $$
> \widetilde{\mathcal S}^{(3)}
> \ge
> s_\ast>0,
> $$
>
> with:
>
> - no fiber escape;
> - no Young oscillation/concentration defect;
> - no covariance defect;
> - no pressure-compatible SGS kernel;
> - no UV/IR/spatial escape;
> - vanishing localization.
>
> Then either:
>
> $$
> (\Pi)_+
> +
> (W_\omega)_+
> \ge
> c_\ast
> $$
>
> on a positive-density set of normalized windows, or a finite-dimensional phase/orthogonality defect survives.

The second alternative must then be classified against recurrence.

---

# 25. Source-status audit

Smooth coarse-graining establishes the exact filtered momentum equation, subgrid stress and interscale energy transfer:

$$
\Pi_\ell=-R_\ell:\nabla U_\ell.
$$

The present SGS energy identity is derived directly by subtracting the resolved kinetic-energy equation from the spatially filtered fine kinetic-energy equation.

The filtered-vorticity paper supplies the complementary vorticity-side commutator forcing:

$$
-\nabla\times\nabla\cdot R_\ell,
$$

and motivates the work-efficiency recurrence problem.

DCRP-25 links the pressure-compatible stress kernel to a positive SGS viscous variance and an affine/Morrey rigidity theorem.

---

# 26. End state

The exact pressure-compatible SGS identity is:

$$
\boxed{
\partial_tk_\ell
+
\nabla\cdot J_\ell^{pc}
=
\nu\Delta k_\ell
-
\nu d_\ell.
}
$$

The exact variance is:

$$
\boxed{
d_\ell
=
\int
\varphi_\ell(z)
|
\nabla u(x-z)-\nabla U_\ell(x)
|^2dz.
}
$$

Thus:

$$
\boxed{
d_\ell=0
\Longrightarrow
u
\text{ is locally affine}.
}
$$

The bounded-reservoir blowup scaling gives:

$$
\boxed{
\int_{B_R}
|u_\infty|^2
\lesssim
R.
}
$$

No nonzero affine field satisfies this growth.

Therefore:

$$
\boxed{
\textbf{
nonzero pressure-compatible strong increment profile}
\Longrightarrow
\textbf{
SGS viscous payment}
\ \vee\
\textbf{
boundary/localization payment}
\ \vee\
\textbf{
reservoir noncompactness}.
}
$$

The pressure-compatible covariance kernel is substantially closed on the bounded-reservoir compact branch.

The next single frontier is:

$$
\boxed{
\textbf{
Active-Stress Work-Orthogonality / Dual-Efficiency Rigidity.
}
$$