# NS-DCRP-29 — Raw-Energy Atomicity, Material Euler Transfer, and the Atom-Free Backward-Ancient Type-II Survivor

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. split the Type-II kinetic reservoir by the amount of actual physical kinetic energy trapped in the shrinking Navier--Stokes core;
  2. prove that a fixed positive raw-energy fraction forces an atom of the terminal energy measure;
  3. connect the atomic branch to the new full-tail Oseen-rigidity theorem in the periodic setting;
  4. eliminate ordinary advection from the finite Euler-time crossing by a materially transported cutoff;
  5. show that a finite atom-free inviscid crossing must retain pressure work, Reynolds/SGS work, or material-window deformation;
  6. isolate the true remaining Type-II state as an atom-free backward-ancient Euler recurrence branch.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - T. M. Leslie, R. Shvydkoy, *The Energy Measure for the Euler and Navier--Stokes Equations*, arXiv:1705.04420;
  - H. Huang, *Full-Tail Dynamical Rigidity Forced by Atomic Navier--Stokes Energy Concentration*, arXiv:2608.04138v1;
  - G. Seregin, *On potential Type II blowups for the Navier--Stokes equations*, arXiv:2606.29468;
  - A. V. Gavrilov, *A steady Euler flow with compact support*, arXiv:1810.08020.
- internal dependencies:
  - DCRP-27 Critical-Reservoir / Euler--Reynolds Reprofiling;
  - DCRP-28 Double-Level Type-II Crossing / Viscous Residue;
  - DCRP-25/26 SGS Energy / Recurrence Rigidity;
  - MORP selected-trace, pressure, spatial, temporal, and transition defect architecture.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-28 reduced the kinetic Type-II branch to:

$$
A_n\to\infty
$$

together with a double-level Euler-time crossing and a normalized viscous-residue dichotomy.

DCRP-29 introduces one additional scalar that is not merely scale critical.

Let:

$$
r_n\downarrow0
$$

be the physical Navier--Stokes spatial scale from which the normalized Type-II package is extracted.

Let:

$$
A_n
$$

be the selected scale-invariant local kinetic-energy reservoir:

$$
\boxed{
A_n
=
r_n^{-1}
\int_{
B_{r_n}(x_n)
}
|u(x,t_n)|^2dx
}
\tag{1.1}
$$

up to the fixed cutoff convention.

Define the **raw core energy**

$$
\boxed{
\beta_n
=
r_nA_n.
}
\tag{1.2}
$$

Thus:

$$
\boxed{
\beta_n
=
\int_{
B_{r_n}(x_n)
}
|u(x,t_n)|^2dx
}
\tag{1.3}
$$

for the sharp-ball model.

The global smooth-preterminal energy identity gives:

$$
\boxed{
0\le
\beta_n
\le
K_0,
}
\tag{1.4}
$$

where:

$$
K_0
=
\sup_{t<T}
\|u(t)\|_2^2.
$$

Hence every kinetic Type-II subsequence has, after extraction:

$$
\boxed{
\beta_n\to\beta_\ast
\in
[0,K_0].
}
\tag{1.5}
$$

This creates the fundamental split:

$$
\boxed{
\textbf{
raw-energy atomic branch}
:
\beta_\ast>0,
}
\tag{1.6}
$$

or:

$$
\boxed{
\textbf{
raw-energy vanishing branch}
:
\beta_\ast=0.
}
\tag{1.7}
$$

The first new theorem is elementary but strong.

Suppose:

$$
t_n\uparrow T,
\qquad
x_n\to x_\ast,
\qquad
r_n\downarrow0,
$$

and the preterminal kinetic-energy measures satisfy the full-time endpoint convergence:

$$
\boxed{
|u(t,x)|^2dx
\stackrel{\ast}{\rightharpoonup}
\mu_\ast
\qquad
(t\uparrow T).
}
\tag{1.8}
$$

If:

$$
\boxed{
\liminf_n
\int_{B_{r_n}(x_n)}
|u(x,t_n)|^2dx
\ge
\beta_\ast
>
0,
}
\tag{1.9}
$$

then:

$$
\boxed{
\mu_\ast(\{x_\ast\})
\ge
\beta_\ast.
}
\tag{1.10}
$$

Therefore:

$$
\boxed{
\beta_\ast>0
\Longrightarrow
\textbf{
endpoint kinetic-energy atom}.
}
\tag{1.11}
$$

This uses only the endpoint energy measure and weak-star convergence.

No Type-I assumption is needed.

The second main input is external and new.

For a smooth unforced Navier--Stokes parent on the flat torus approaching a finite terminal time, Huang (2026) proves:

$$
\boxed{
\textbf{
one endpoint energy atom}
\Longrightarrow
\textbf{
one same-parent full-tail saturated Oseen family}.
}
\tag{1.12}
$$

The same atom further forces every sufficiently late fixed-root descendant to have:

- infinite delayed second-order action;
- nonintegrable positive enstrophy production;
- failure of a parent-only delayed second-order Oseen budget.

Thus, in the periodic setting:

$$
\boxed{
\beta_\ast>0
\Longrightarrow
\textbf{
full-tail Oseen second-order obstruction}.
}
\tag{1.13}
$$

This is significantly stronger than merely recording the atom as a terminal trace defect.

The theorem is presently stated and proved on:

$$
\mathbb T^3.
$$

It must **not** be silently imported as a theorem on:

$$
\mathbb R^3.
$$

The whole-space endpoint atom still exists by Theorem 4.1 below; a corresponding same-parent local Oseen full-tail theorem is a separate extension problem.

The third main result treats the raw-energy vanishing branch:

$$
\beta_n\to0.
$$

This is the truly scale-critical Type-II regime:

$$
A_n\to\infty
$$

while the actual physical kinetic energy stored in the shrinking core goes to zero.

The Euler-time normalization can still produce unit local energy because it divides by the diverging amplitude:

$$
a_n^2=A_n.
$$

Hence the Euler profile is not an ordinary fixed-energy atom inherited by the terminal Navier--Stokes energy measure.

For finite Euler-time double crossings:

$$
T_n\to T_\ast\in(0,\infty),
$$

DCRP-29 replaces the fixed spatial cutoff by a **materially transported coarse cutoff**.

At fixed filter scale:

$$
\sigma>0,
$$

let:

$$
U_{n,\sigma}
=
S_\sigma v_n,
$$

and let:

$$
\chi_{n,\sigma}(y,\tau)
$$

solve:

$$
\boxed{
\partial_\tau
\chi_{n,\sigma}
+
U_{n,\sigma}
\cdot
\nabla
\chi_{n,\sigma}
=
0,
}
\tag{1.14}
$$

with terminal condition:

$$
\boxed{
\chi_{n,\sigma}(\cdot,0)
=
\chi_0.
}
\tag{1.15}
$$

For the resolved energy:

$$
e_{n,\sigma}
=
|U_{n,\sigma}|^2/2,
$$

the ordinary resolved advection cancels **exactly**.

The exact material-cutoff energy identity is:

$$
\boxed{
\begin{aligned}
&
E_{n,\sigma}^{mat}(0)
-
E_{n,\sigma}^{mat}(-T_n)
+
\nu_n
\iint
\chi_{n,\sigma}
|\nabla U_{n,\sigma}|^2
\\
&\qquad
=
\iint
\chi_{n,\sigma}
R_{n,\sigma}:
\nabla U_{n,\sigma}
+
\iint
\left(
P_{n,\sigma}U_{n,\sigma}
+
R_{n,\sigma}U_{n,\sigma}
\right)
\cdot
\nabla
\chi_{n,\sigma}
\\
&\qquad\qquad
+
\nu_n
\iint
e_{n,\sigma}
\Delta
\chi_{n,\sigma}.
\end{aligned}
}
\tag{1.16}
$$

Thus local energy growth in a **co-moving coarse material window** cannot be financed by ordinary advection.

It can only come from:

1. resolved Reynolds/SGS work;
2. pressure work through the material boundary;
3. SGS stress transport through the material boundary;
4. a viscous cutoff term, which vanishes at fixed filter scale in the inviscid Type-II limit.

Now compare the fixed endpoint crossing of DCRP-28 with the material window.

Define the material mismatch:

$$
\boxed{
\mathcal M_{n,\sigma}^{mat}
=
\left|
\int
\left(
\chi_{n,\sigma}(y,-T_n)
-
\chi_0(y)
\right)
e_{n,\sigma}(y,-T_n)dy
\right|.
}
\tag{1.17}
$$

If:

$$
\mathcal M_{n,\sigma}^{mat}
$$

is a fixed positive amount, then the crossing contains a genuine **material-centering / deformation / transport defect**.

If:

$$
\mathcal M_{n,\sigma}^{mat}
$$

is small, the fixed resolved energy crossing persists in the material window.

Equation (1.16) therefore gives:

$$
\boxed{
c_\ast
\le
\left(
W_{n,\sigma}^{mat}
\right)_+
+
\left|
P_{n,\sigma}^{mat}
\right|
+
\left|
T_{n,\sigma}^{mat}
\right|
+
\mathcal M_{n,\sigma}^{mat}
+
o(1),
}
\tag{1.18}
$$

where:

$$
W_{n,\sigma}^{mat}
=
\iint
\chi_{n,\sigma}
R_{n,\sigma}:\nabla U_{n,\sigma},
$$

$$
P_{n,\sigma}^{mat}
=
\iint
P_{n,\sigma}
U_{n,\sigma}
\cdot
\nabla\chi_{n,\sigma},
$$

and:

$$
T_{n,\sigma}^{mat}
=
\iint
R_{n,\sigma}U_{n,\sigma}
\cdot
\nabla\chi_{n,\sigma}.
$$

Hence:

$$
\boxed{
\textbf{
finite atom-free inviscid Type-II crossing}
\Longrightarrow
\textbf{
material Reynolds work}
\ \vee\
\textbf{
material pressure work}
\ \vee\
\textbf{
material SGS transport}
\ \vee\
\textbf{
material-window deformation}.
}
\tag{1.19}
$$

This is stronger than the fixed-cutoff result of DCRP-28 because ordinary coarse advection has been removed from the source side.

In the exact Euler limit with a smooth enough profile and vanishing subfilter stress as:

$$
\sigma\downarrow0,
$$

the material identity formally reduces to:

$$
\boxed{
\frac d{d\tau}
\int
\chi
\frac{|v|^2}{2}
=
\int
p\,v\cdot\nabla\chi.
}
\tag{1.20}
$$

Thus a material blob changes its kinetic energy only by pressure work.

This does **not** imply pressure work is globally dissipative.

It identifies the exact dynamical carrier of a local material energy transition.

After DCRP-29 the strongest Type-II state survivor is therefore no longer a generic Euler concentration profile.

All finite-time crossings either:

- retain raw endpoint atomic energy;
- retain viscous residue;
- retain material pressure/SGS work;
- retain material-window deformation;
- retain trace/localization/Reynolds defects.

The remaining defect-free state branch is:

$$
\boxed{
\beta_n\to0,
\qquad
T_n\to\infty,
}
\tag{1.21}
$$

with all spatial/scale/trace/viscous/Reynolds/material-transition defects removed.

This produces an:

$$
\boxed{
\textbf{
atom-free backward-ancient Euler recurrence profile}.
}
\tag{1.22}
$$

The lower kinetic level disappears to:

$$
\tau=-\infty,
$$

while every fixed terminal Euler-time window can converge to a recurrent or steady Euler state.

General Euler theory does not exclude this.

Indeed nontrivial smooth compactly supported steady 3D Euler flows exist.

Therefore the new exact frontier is:

$$
\boxed{
\textbf{
Atom-Free Backward-Ancient Type-II Euler Recurrence /
Same-Parent Material Rigidity.
}
}
\tag{1.23}
$$

This is substantially narrower than the DCRP-28 "genuine Euler concentration" branch.

---

# 2. Physical versus scale-critical kinetic energy

Let:

$$
U(x,t)
$$

denote the original physical Navier--Stokes velocity.

Under the standard parabolic normalization:

$$
u_n(y,s)
=
r_n
U
\left(
x_n+r_ny,
t_n+r_n^2s
\right),
$$

one has:

$$
\boxed{
\int_{B_1}
|u_n(y,s)|^2dy
=
r_n^{-1}
\int_{
B_{r_n}(x_n)
}
|U(x,t)|^2dx.
}
\tag{2.1}
$$

Thus the scale-critical local kinetic coordinate is larger than the raw physical energy by:

$$
r_n^{-1}.
$$

If:

$$
A_n\sim
\int_{B_1}|u_n|^2,
$$

then:

$$
\boxed{
\beta_n
=
r_nA_n
}
\tag{2.2}
$$

is exactly the physical kinetic energy in the shrinking core, up to the fixed cutoff convention.

Therefore Type-II:

$$
A_n\to\infty
$$

does **not** determine whether the shrinking core contains a fixed amount of real kinetic energy.

That is what:

$$
\beta_n
$$

measures.

---

# 3. Endpoint energy measure

For a smooth finite-energy Navier--Stokes branch on:

$$
[t_b,T),
$$

the kinetic-energy densities have a terminal energy measure:

$$
\boxed{
|U(t,x)|^2dx
\stackrel{\ast}{\rightharpoonup}
\mu_\ast
\qquad
(t\uparrow T).
}
\tag{3.1}
$$

On:

$$
\mathbb R^3,
$$

this is the standard energy-measure object of Leslie--Shvydkoy.

On:

$$
\mathbb T^3,
$$

Huang (2026) proves a quantitative full-time version for smooth preterminal Navier--Stokes flow.

The measure captures failure of strong:

$$
L^2
$$

compactness at the terminal time.

---

# 4. NEW THEOREM — Shrinking Raw Energy Forces an Endpoint Atom

## Theorem 4.1

Assume:

$$
\mu_{t_n}
=
|U(t_n,x)|^2dx
\stackrel{\ast}{\rightharpoonup}
\mu_\ast,
$$

with:

$$
t_n\uparrow T.
$$

Assume:

$$
x_n\to x_\ast,
\qquad
r_n\downarrow0,
$$

and:

$$
\boxed{
\mu_{t_n}
(
B_{r_n}(x_n)
)
\ge
\beta
>
0.
}
\tag{4.1}
$$

Then:

$$
\boxed{
\mu_\ast(\{x_\ast\})
\ge
\beta.
}
\tag{4.2}
$$

### Proof

Fix:

$$
\varepsilon>0.
$$

For all sufficiently large:

$$
n,
$$

$$
B_{r_n}(x_n)
\subset
\overline B_\varepsilon(x_\ast).
$$

Therefore:

$$
\mu_{t_n}
(
\overline B_\varepsilon(x_\ast)
)
\ge
\beta.
$$

For the closed set:

$$
\overline B_\varepsilon(x_\ast),
$$

Portmanteau gives:

$$
\limsup_{n\to\infty}
\mu_{t_n}
(
\overline B_\varepsilon(x_\ast)
)
\le
\mu_\ast
(
\overline B_\varepsilon(x_\ast)
).
$$

Hence:

$$
\mu_\ast
(
\overline B_\varepsilon(x_\ast)
)
\ge
\beta.
$$

Let:

$$
\varepsilon\downarrow0.
$$

By continuity from above of finite measures:

$$
\mu_\ast(\{x_\ast\})
\ge
\beta.
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

# 5. Corollary — raw Type-II atomicity

If:

$$
\boxed{
\beta_n
=
r_nA_n
\to
\beta_\ast
>
0,
}
\tag{5.1}
$$

then:

$$
\boxed{
\mu_\ast(\{x_\ast\})
\ge
c\beta_\ast
>
0
}
\tag{5.2}
$$

with:

$$
c=1
$$

for the sharp-ball convention and a fixed cutoff-comparison constant for smooth cutoff normalization.

Thus:

$$
\boxed{
\textbf{
Type-II critical growth carrying fixed raw energy}
=
\textbf{
endpoint atomic concentration}.
}
\tag{5.3}
$$

---

# 6. New external theorem — atomic full-tail rigidity

Huang's 2026 theorem is formulated for:

$$
\Omega=\mathbb T^3,
$$

with a smooth unforced Navier--Stokes parent on:

$$
[t_b,T_\ast).
$$

If:

$$
\boxed{
\mu_\ast(\{a\})=m>0,
}
\tag{6.1}
$$

then one point atom forces a same-parent full-tail saturated family.

The principal structural consequences include:

1. one backward adjoint extracted from the **entire** late packet tail;
2. full-time Cauchy saturation;
3. uniform forward/backward Oseen transport saturation over the late ordered triangle;
4. vanishing first-order dissipation along the saturated packet mechanism;
5. infinite delayed second-order action for every sufficiently late fixed-root descendant;
6. nonintegrable positive enstrophy production;
7. failure of a parent-only delayed second-order Oseen budget.

Symbolically:

$$
\boxed{
\text{endpoint atom}
\Longrightarrow
\text{full-tail Oseen saturation}
\Longrightarrow
\text{infinite delayed second-order action}.
}
\tag{6.2}
$$

Status:

$$
\boxed{
\textbf{EXTERNAL PRIMARY THEOREM ON }\mathbb T^3.
}
$$

---

# 7. Periodic Type-II atomic branch

Combining Theorem 4.1 with the external theorem:

$$
\boxed{
\beta_\ast>0
}
$$

implies:

$$
\boxed{
\text{endpoint atom}
}
$$

and, on the flat torus:

$$
\boxed{
\text{same-parent full-tail Oseen rigidity}
+
\text{second-order budget failure}.
}
\tag{7.1}
$$

Thus the periodic raw-energy Type-II branch is no longer merely an Euler-profile branch.

It has an intrinsically Navier--Stokes preterminal full-tail signature.

This signature survives even though a later amplitude normalization may produce an Euler-type equation.

---

# 8. Whole-space safety boundary

Huang's proof uses periodic ingredients including:

- periodic pressure representation;
- periodic Nash estimates;
- the global Oseen evolution family on the torus.

The paper explicitly states that analogues on other domains or local-energy settings require corresponding replacements.

Therefore DCRP-29 does **not** claim:

$$
\boxed{
\text{endpoint atom on }\mathbb R^3
\Longrightarrow
\text{Huang full-tail theorem}.
}
$$

The whole-space atom is proved by Theorem 4.1.

A same-parent local Oseen saturation extension on:

$$
\mathbb R^3
$$

is a distinct research problem.

Status:

$$
\boxed{
\textbf{NO OVERCLAIM}.
}
$$

---

# 9. Raw-energy vanishing branch

Assume:

$$
\boxed{
A_n\to\infty,
\qquad
\beta_n=r_nA_n\to0.
}
\tag{9.1}
$$

Then:

$$
\boxed{
\int_{
B_{r_n}(x_n)
}
|U(x,t_n)|^2dx
\to0.
}
\tag{9.2}
$$

Yet the scale-normalized local energy diverges.

This is a genuinely critical amplification phenomenon.

The selected shrinking cores do not themselves carry a fixed endpoint energy atom.

This is the correct setting for the strongest atom-free Type-II Euler branch.

---

# 10. Finite Euler-time crossing recalled

Choose two selected kinetic levels:

$$
L_n/2
\longrightarrow
L_n,
$$

with:

$$
a_n^2=L_n.
$$

Let:

$$
s_n<t_n
$$

be the selected crossing times.

Define:

$$
T_n
=
a_n(t_n-s_n).
$$

In the finite branch:

$$
\boxed{
T_n\to T_\ast\in(0,\infty).
}
\tag{10.1}
$$

After the amplitude-time normalization:

$$
v_n(y,\tau)
=
a_n^{-1}
u_n
\left(
y,
t_n+\tau/a_n
\right),
$$

the local normalized kinetic gap is fixed.

DCRP-28 showed that a fixed spatial cutoff forces coarse Reynolds work or boundary/transport activity.

The present round removes ordinary advection by a material cutoff.

---

# 11. Material coarse cutoff

Fix:

$$
\sigma>0.
$$

Define:

$$
U_{n,\sigma}
=
S_\sigma v_n.
$$

Because:

$$
U_{n,\sigma}
$$

is spatially smooth, the transport equation:

$$
\boxed{
\partial_\tau
\chi_{n,\sigma}
+
U_{n,\sigma}\cdot\nabla
\chi_{n,\sigma}
=
0
}
\tag{11.1}
$$

has a classical solution on every finite normalized time interval.

Choose:

$$
\boxed{
\chi_{n,\sigma}(y,0)
=
\chi_0(y),
}
\tag{11.2}
$$

where:

$$
\chi_0
$$

is the terminal core cutoff.

Thus:

$$
\chi_{n,\sigma}
$$

moves with the resolved coarse flow.

Pure resolved advection is built into the window.

---

# 12. Exact resolved material-energy identity

The fixed-filter resolved equation is:

$$
\partial_\tau U
-
\nu_n\Delta U
+
\nabla\cdot(U\otimes U)
+
\nabla P
=
-\nabla\cdot R.
$$

Set:

$$
e=|U|^2/2.
$$

Then:

$$
\partial_\tau e
+
\nabla\cdot
\left[
(e+P)U+RU
\right]
=
\nu_n\Delta e
-
\nu_n|\nabla U|^2
+
R:\nabla U.
$$

Multiply by:

$$
\chi
$$

with:

$$
\partial_\tau\chi+U\cdot\nabla\chi=0.
$$

The terms:

$$
e\partial_\tau\chi
$$

and:

$$
eU\cdot\nabla\chi
$$

cancel exactly.

Therefore:

$$
\boxed{
\begin{aligned}
\frac d{d\tau}
\int
\chi e
+
\nu_n
\int
\chi
|\nabla U|^2
&=
\int
\chi
R:\nabla U
\\
&\quad
+
\int
(PU+RU)\cdot\nabla\chi
+
\nu_n
\int
e\Delta\chi.
\end{aligned}
}
\tag{12.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. Interpretation of the material identity

The right side has only:

### local Reynolds/SGS work

$$
\boxed{
W^{mat}
=
\int
\chi
R:\nabla U;
}
\tag{13.1}
$$

### pressure work through the material boundary

$$
\boxed{
P^{mat}
=
\int
PU\cdot\nabla\chi;
}
\tag{13.2}
$$

### SGS transport through the material boundary

$$
\boxed{
T^{mat}
=
\int
RU\cdot\nabla\chi;
}
\tag{13.3}
$$

### vanishing fixed-filter viscous cutoff correction

$$
\boxed{
\nu_n
\int
e\Delta\chi.
}
\tag{13.4}
$$

The ordinary kinetic advection term has disappeared.

Thus:

$$
\boxed{
\textbf{
material energy growth cannot be blamed on sweeping.
}
}
\tag{13.5}
$$

---

# 14. Fixed-to-material mismatch

Let the resolved fixed-cutoff energy be:

$$
\boxed{
E_{\rm fix}(\tau)
=
\int
\chi_0
e(y,\tau)dy.
}
\tag{14.1}
$$

Let the material energy be:

$$
\boxed{
E_{\rm mat}(\tau)
=
\int
\chi(y,\tau)
e(y,\tau)dy.
}
\tag{14.2}
$$

At terminal time:

$$
\boxed{
E_{\rm mat}(0)
=
E_{\rm fix}(0).
}
\tag{14.3}
$$

Define:

$$
\boxed{
\mathcal M^{mat}
=
\left|
E_{\rm mat}(-T)
-
E_{\rm fix}(-T)
\right|.
}
\tag{14.4}
$$

If:

$$
\mathcal M^{mat}
$$

is large, the fixed core and the material core have genuinely separated.

This may represent:

- translation of the energy packet;
- deformation of the packet;
- resolved material transport relative to the fixed singular chart.

The pure translation component belongs to the declared moving-center quotient.

The residual mismatch is a native material-deformation / transition coordinate.

---

# 15. NEW THEOREM — Material First-Crossing Transfer Gap

## Theorem 15.1

Assume a finite Euler-time Type-II crossing has, at fixed filter scale:

$$
\boxed{
E_{\rm fix}(0)
-
E_{\rm fix}(-T)
\ge
c_0
>
0.
}
\tag{15.1}
$$

Then:

$$
\boxed{
c_0
\le
\mathcal M^{mat}
+
\left(
\int_{-T}^{0}
W^{mat}d\tau
\right)_+
+
\left|
\int_{-T}^{0}
P^{mat}d\tau
\right|
+
\left|
\int_{-T}^{0}
T^{mat}d\tau
\right|
+
\mathcal V_{\sigma}^{res},
}
\tag{15.2}
$$

where:

$$
\mathcal V_{\sigma}^{res}
$$

contains the fixed-filter resolved viscous/cutoff terms and tends to zero in the inviscid Type-II limit.

### Proof

From (14.3):

$$
\begin{aligned}
E_{\rm mat}(0)-E_{\rm mat}(-T)
&=
E_{\rm fix}(0)-E_{\rm fix}(-T)
\\
&\quad
+
E_{\rm fix}(-T)-E_{\rm mat}(-T).
\end{aligned}
$$

Hence:

$$
E_{\rm mat}(0)-E_{\rm mat}(-T)
\ge
c_0-\mathcal M^{mat}.
$$

Integrate the exact identity (12.1).

The positive resolved viscous dissipation stays on the left.

Move the vanishing cutoff correction into:

$$
\mathcal V_{\sigma}^{res}.
$$

Bound the signed right-hand terms by their positive/absolute parts.

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

# 16. Pure Euler material limit

Suppose:

-:

  $$
  R_E=0;
  $$

- the limiting Euler state is smooth enough for the unfiltered local energy identity;
-:

  $$
  \sigma\downarrow0
  $$

  along a compact strong branch.

Then:

$$
R_\sigma\to0.
$$

The material identity becomes:

$$
\boxed{
\frac d{d\tau}
\int
\chi
\frac{|v|^2}{2}
=
\int
p
v\cdot\nabla\chi.
}
\tag{16.1}
$$

Thus a material fluid packet changes kinetic energy only through pressure work.

This is compatible with ordinary Euler dynamics.

It is **not** a contradiction.

The gain is structural:

$$
\boxed{
\textbf{
no pressure work}
+
\textbf{
no material mismatch}
\Longrightarrow
\textbf{
no local material energy crossing}.
}
\tag{16.2}
$$

---

# 17. Material centering versus translation symmetry

A translating coherent structure can make:

$$
E_{\rm fix}
$$

change while:

$$
E_{\rm mat}
$$

does not.

This is not physical energy production.

It is chart mismatch.

Therefore a correct obstruction package must quotient:

- rigid translation;
- declared moving-center motion;

before interpreting:

$$
\mathcal M^{mat}
$$

as deformation.

After this quotient, the residual material mismatch measures genuine shape/transport change.

This is the Euler analogue of the DCRP-26 translation-tangent NO-GO.

---

# 18. Atom-free finite-crossing consequence

Assume:

$$
\beta_n\to0,
$$

$$
T_n\to T_\ast\in(0,\infty),
$$

and:

$$
\mathfrak V_n^{II}\to0.
$$

Assume also that:

- endpoint trace defects vanish;
- cutoff-shell defects vanish;
- Euler--Reynolds concentration defects vanish.

Then the fixed-filter coarse crossing persists.

Theorem 15.1 gives:

$$
\boxed{
\textbf{
material Reynolds work}
\ \vee\
\textbf{
material pressure work}
\ \vee\
\textbf{
material SGS transport}
\ \vee\
\textbf{
material deformation/centering mismatch}.
}
\tag{18.1}
$$

Hence:

$$
\boxed{
\textbf{
finite atom-free inviscid Type-II crossing cannot be completely silent.
}
}
\tag{18.2}
$$

This closes the finite-time state branch at the native transition level.

---

# 19. Atomic branch versus material branch

The two mechanisms are qualitatively different.

### raw-energy atom

$$
\beta_\ast>0
$$

means a fixed amount of **physical** kinetic energy survives in a shrinking spatial ball.

This is visible in the terminal energy measure.

### atom-free Type-II

$$
\beta_\ast=0
$$

means no fixed raw kinetic energy survives in the selected shrinking core.

The Type-II amplification exists only after critical/amplitude normalization.

Its finite-time dynamics must therefore be detected through:

- material transfer;
- pressure;
- subgrid stress;
- trace/transition defects;

not through endpoint atomic mass.

---

# 20. Backward-time escape

Now assume:

$$
\boxed{
\beta_n\to0,
}
\tag{20.1}
$$

and:

$$
\boxed{
T_n\to\infty.
}
\tag{20.2}
$$

The lower selected kinetic level moves to:

$$
-\infty_\tau.
$$

For every fixed:

$$
T<\infty,
$$

the terminal window:

$$
[-T,0]
$$

may converge to an Euler state whose local energy appears stationary or recurrent.

The finite-crossing theorem cannot recover the missing level because it lies outside every compact time window.

This is a genuine **backward-time escape** rather than a finite transition.

---

# 21. Strongest defect-free survivor

Impose the strongest zero-defect conditions:

-:

  $$
  \beta_n\to0;
  $$

-:

  $$
  \mathfrak V_n^{II}\to0;
  $$

- no Euler--Reynolds defect;
- no selected-trace concentration;
- no spatial/scale/fiber escape;
- no material pressure/SGS work on every fixed terminal window after the moving-center quotient;
- no material deformation after moving-center quotient;
-:

  $$
  T_n\to\infty.
  $$

Then the terminal Type-II reprofile approaches an ancient/recurrent Euler state on:

$$
(-\infty,0].
$$

The state carries no endpoint energy atom from the selected shrinking physical cores.

Thus:

$$
\boxed{
\textbf{
atom-free backward-ancient Euler recurrence}
}
\tag{21.1}
$$

is the strongest remaining Type-II state normal form.

---

# 22. Why general Euler theory does not kill this survivor

Smooth compactly supported nonzero steady 3D Euler flows exist.

Such a flow is:

- ancient;
- recurrent;
- finite energy;
- spatially localized.

Therefore none of those properties alone gives a Liouville theorem.

The remaining Type-II survivor must be attacked using structure inherited specifically from the Navier--Stokes extraction, not by generic Euler finite-energy arguments.

---

# 23. New periodic shortcut for atomic concentration

In the periodic formulation, Theorem 6.2 gives a very strong additional route.

An atom-free endpoint measure is necessary for finiteness of the parent-only delayed second-order Oseen budget.

Thus a periodic Type-II proof may attempt to establish an a priori finite terminal-tail bound:

$$
\boxed{
\mathfrak R_u(s,r)<\infty
}
\tag{23.1}
$$

for at least one sufficiently late root.

By Huang's contrapositive:

$$
\boxed{
\mathfrak R_u(s,r)<\infty
\Longrightarrow
\text{no endpoint atom}.
}
\tag{23.2}
$$

This does not eliminate atom-free Type-II.

It cleanly removes the raw-energy atomic subbranch.

---

# 24. Whole-space atomic extension problem

For:

$$
\mathbb R^3,
$$

the endpoint measure theorem already gives the static atom.

A useful future theorem would localize Huang's same-parent construction:

$$
\boxed{
\text{whole-space/local endpoint atom}
\Longrightarrow
\text{local same-parent Oseen full-tail saturation}
}
\tag{24.1}
$$

under finite-energy smooth-preterminal hypotheses.

The main missing replacements are:

- a local pressure decomposition compatible with the Oseen evolution;
- local/global Nash control;
- treatment of energy escaping to spatial infinity.

MORP/DCRP already contain pressure-tail and spatial-escape coordinates that are naturally suited to this extension.

This is a technically concrete side frontier.

---

# 25. Updated Type-II normal form

The kinetic Type-II branch now satisfies:

$$
\boxed{
A_n\to\infty
\Longrightarrow
\begin{cases}
\beta_\ast>0
&
\Rightarrow
\text{endpoint atom},
\\
\beta_\ast=0
&
\Rightarrow
\text{atom-free Type-II}.
\end{cases}
}
\tag{25.1}
$$

The atom-free branch satisfies:

$$
\boxed{
\begin{aligned}
&
T_n\to0
&&\Rightarrow
\text{temporal concentration},
\\
&
T_n\to T_\ast\in(0,\infty)
&&\Rightarrow
\text{material pressure/SGS/deformation transfer},
\\
&
T_n\to\infty
&&\Rightarrow
\text{backward-time escape / ancient Euler recurrence}.
\end{aligned}
}
\tag{25.2}
$$

Additionally:

$$
\boxed{
\liminf
\mathfrak V_n^{II}>0
}
$$

is a real Navier--Stokes viscous payment in any of the time branches.

Thus the truly defect-free Type-II survivor is:

$$
\boxed{
\beta_n\to0,
\quad
T_n\to\infty,
\quad
\mathfrak V_n^{II}\to0,
}
\tag{25.3}
$$

plus zero spatial/scale/trace/Reynolds/material-transfer defects.

---

# 26. Relation to Seregin's Type-II Euler route

Seregin's Type-II analysis produces nontrivial Euler objects under scenario-specific rescalings and assumptions.

The recent 2026 paper explicitly obtains nontrivial Euler limits satisfying a local energy inequality under its Type-II hypotheses.

DCRP-29 adds two project-specific filters before accepting such an Euler object as the final survivor:

1. does the original shrinking core carry a fixed raw physical energy atom?
2. does the finite Euler-time crossing survive in a material window?

Only if the answers are:

$$
\boxed{
\text{no atom}
}
$$

and:

$$
\boxed{
\text{no finite material crossing}
}
$$

does the branch enter the backward-ancient Euler recurrence frontier.

---

# 27. Exact zero-cost consequence

A transition-complete Type-II package may include:

- raw endpoint atomic mass;
- normalized viscous residue;
- temporal concentration;
- backward-time escape;
- material pressure work;
- material SGS work/transport;
- material deformation after translation quotient;
- trace/Reynolds/localization defects.

Then:

### atomic finite branch

has positive atomic/full-tail carrier;

### finite atom-free branch

has positive material-transition carrier;

### ultrafast branch

has positive temporal-concentration carrier.

Therefore an exact zero-cost Type-II state can survive only through the backward-time recurrence branch, provided backward-time escape itself is not assigned a strict tax by fiat.

This is the strongest project-internal normal form to date for the kinetic Type-II sector.

---

# 28. Why backward-time escape cannot simply be taxed

The fact:

$$
T_n\to\infty
$$

is a compactness/transition statement.

A recurrent ancient Euler profile may genuinely exist.

Declaring every:

$$
-\infty_\tau
$$

carrier to have positive cost would manufacture coercivity from the compactification boundary.

That would repeat the amplitude-tax no-go of DCRP-27.

Therefore backward-time escape must be attacked dynamically.

---

# 29. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Atom-Free Backward-Ancient Type-II Euler Recurrence /
Same-Parent Material Rigidity Lemma}.
}
$$

A useful theorem would start with an ancient Euler profile:

$$
v:
\mathbb R^3\times(-\infty,0]
\to
\mathbb R^3
$$

generated by a same-parent Navier--Stokes Type-II sequence and satisfying:

- no raw endpoint energy atom;
- no anomalous viscous residue;
- no Euler--Reynolds defect;
- no spatial/scale/fiber escape;
- material pressure/SGS work vanishing on every fixed terminal window after the moving-center quotient;
- a nontrivial terminal normalized energy trace;
- the lower kinetic level occurring only at:

  $$
  -\infty_\tau.
  $$

Then prove either:

$$
\boxed{
v
\text{ is a rigid/steady recurrence mode compatible with a finite-dimensional quotient}
}
\tag{29.1}
$$

or:

$$
\boxed{
\text{some same-parent material/pressure/deformation carrier is nonzero}.
}
\tag{29.2}
$$

A further theorem would then have to exclude the rigid recurrence modes using their precise Navier--Stokes ancestry.

This is now the true inviscid Type-II frontier.

---

# 30. Source-status audit

## Leslie--Shvydkoy

The energy measure is the weak-star terminal limit of:

$$
|u(t)|^2dx
$$

at the first possible blowup time.

It measures concentration/oscillation associated with possible failure of strong energy compactness.

DCRP-29 uses only this measure structure plus elementary weak-star measure theory for Theorem 4.1.

## Huang 2026-08-04

For smooth unforced Navier--Stokes on the flat torus:

$$
\text{one endpoint atom}
\Longrightarrow
\text{same-parent full-tail saturation}
\Longrightarrow
\text{infinite delayed second-order action}.
$$

The theorem requires no Type-I, self-similar, smallness, or terminal strong-convergence hypothesis.

Its domain is periodic and the whole-space analogue is not claimed here.

## Seregin 2026

Potential Type-II blowup scenarios are analyzed through Euler scaling.

Under the paper's hypotheses a nontrivial Euler object satisfying a local energy inequality is extracted.

This confirms that the Euler limit is a serious Type-II branch rather than a disposable artifact.

## Gavrilov

Nontrivial smooth compactly supported steady 3D Euler flows exist.

Thus ancient/recurrent finite-energy Euler profiles cannot be eliminated by a generic localization-based Liouville theorem.

---

# 31. End state

The new physical-scale discriminator is:

$$
\boxed{
\beta_n
=
r_nA_n.
}
$$

It separates:

$$
\boxed{
\beta_\ast>0
\Rightarrow
\text{endpoint energy atom},
}
$$

from:

$$
\boxed{
\beta_\ast=0
\Rightarrow
\text{raw-energy vanishing Type-II}.
}
$$

The atomic implication is exact:

$$
\boxed{
\liminf
\int_{B_{r_n}(x_n)}
|u(t_n)|^2
\ge\beta>0
\Longrightarrow
\mu_\ast(\{x_\ast\})\ge\beta.
}
$$

In the periodic setting, the newest full-tail theorem upgrades this to:

$$
\boxed{
\text{same-parent Oseen saturation}
+
\text{infinite delayed second-order action}.
}
$$

For the atom-free finite Euler-time branch, a material coarse cutoff removes ordinary sweeping and yields:

$$
\boxed{
\text{material Reynolds work}
\ \vee\
\text{material pressure work}
\ \vee\
\text{material SGS transport}
\ \vee\
\text{material deformation}.
}
$$

Thus the strongest remaining defect-free Type-II state is:

$$
\boxed{
\beta_n\to0,
\qquad
T_n\to\infty,
\qquad
\mathfrak V_n^{II}\to0,
}
$$

with no other retained native defect.

This is the:

$$
\boxed{
\textbf{
atom-free backward-ancient Euler recurrence profile}.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Atom-Free Backward-Ancient Type-II Euler Recurrence /
Same-Parent Material Rigidity.
}
}
$$
