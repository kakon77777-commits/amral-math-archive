# NS-DCRP-28 — Type-II Double-Level Crossing, Normalized Viscous Residue, Coarse Euler–Reynolds Transfer, and the Genuine Euler Barrier

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. sharpen the DCRP-27 kinetic Type-II Euler–Reynolds reprofile by selecting a genuine two-level energy transition;
  2. separate a surviving Navier--Stokes viscous payment from a genuinely inviscid Type-II limit;
  3. prove that a finite Euler-time level crossing cannot become a silent Euler/Euler--Reynolds profile;
  4. distinguish temporal concentration, backward-time escape, trace/SGS defects, stress/backscatter work, and spatial pressure/transport influx;
  5. audit which Euler subbranches are known to be rigid and prove that no general finite-energy Euler Liouville theorem can close the remaining branch.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - G. Seregin, *On potential Type II blowups for the Navier--Stokes equations*, arXiv:2606.29468;
  - G. Seregin, *Remarks on Type II blowups of solutions to the Navier--Stokes equations*, arXiv:2304.04045;
  - P. Constantin, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570;
  - A. V. Gavrilov, *A steady Euler flow with compact support*, arXiv:1810.08020;
  - P. Constantin, J. La, V. Vicol, *Remarks on a paper by Gavrilov...*, arXiv:1903.11699;
  - L. De Rosa, T. D. Drivas, M. Inversi, *Intermittency and lower dimensional dissipation in incompressible fluids: quantifying Landau*, arXiv:2212.08176.
- internal dependencies:
  - DCRP-27 amplitude--shape / Euler--Reynolds reprofiling;
  - DCRP-25/26 SGS energy and recurrence identities;
  - MORP selected-trace / pressure / spatial / transition defect architecture.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-27 proved the structural Type-II reprofile

$$
A_n\to\infty
\Longrightarrow
\text{Euler state}
\ \vee\
\text{Euler--Reynolds/trace defect}
\ \vee\
\text{time-face escape}.
$$

The first correction of DCRP-28 is that the small coefficient

$$
\nu/a_n
$$

in the Euler-scaled PDE does **not** by itself imply that viscosity is negligible in the normalized energy ledger.

Let

$$
a_n^2=L_n
$$

be the selected kinetic-energy level and define

$$
v_n(y,\tau)
=
a_n^{-1}
u_n
\left(
y,
t_n+\tau/a_n
\right).
$$

Then

$$
\partial_\tau v_n
+
(v_n\cdot\nabla)v_n
+
\nabla q_n
=
\frac{\nu}{a_n}
\Delta v_n.
$$

The normalized viscous payment on a physical interval

$$
[s_n,t_n]
$$

is

$$
\boxed{
\mathfrak V_n^{II}
=
\frac{\nu}{a_n^2}
\iint_{
[s_n,t_n]\times B
}
|\nabla u_n|^2dxdt.
}
\tag{1.1}
$$

Equivalently,

$$
\boxed{
\mathfrak V_n^{II}
=
\frac{\nu}{a_n}
\iint_{
[-T_n,0]\times B
}
|\nabla v_n|^2dyd\tau,
}
\tag{1.2}
$$

where

$$
\boxed{
T_n
=
a_n
(t_n-s_n).
}
\tag{1.3}
$$

Thus Type-II has a genuine first dichotomy:

$$
\boxed{
\liminf_n
\mathfrak V_n^{II}
>
0
}
\tag{1.4}
$$

or

$$
\boxed{
\mathfrak V_n^{II}
\to0.
}
\tag{1.5}
$$

The first branch retains a fixed normalized **Navier--Stokes viscous tax** even though the PDE coefficient tends to zero.

Only the second branch is truly inviscid.

The second main result is a two-level first-crossing normalization.

Let

$$
\mathcal K_n(t)
=
\frac12
\int
\chi(x)
|u_n(x,t)|^2dx
$$

for one fixed normalized local cutoff.

Choose

$$
L_n\to\infty
$$

and let

$$
t_n
$$

be the first selected time at which

$$
\boxed{
\mathcal K_n(t_n)=L_n.
}
\tag{1.6}
$$

If the left time face already has

$$
\mathcal K_n\ge L_n/2,
$$

record a time-face reservoir defect.

Otherwise let

$$
s_n<t_n
$$

be the last/first controlled crossing with

$$
\boxed{
\mathcal K_n(s_n)=L_n/2.
}
\tag{1.7}
$$

After dividing by

$$
L_n,
$$

the normalized local kinetic energy changes by the fixed amount

$$
\boxed{
1/2.
}
\tag{1.8}
$$

Now exactly one of the following time regimes occurs after subsequence extraction:

$$
\boxed{
T_n\to0,
}
\tag{1.9}
$$

$$
\boxed{
T_n\to T_\ast\in(0,\infty),
}
\tag{1.10}
$$

or

$$
\boxed{
T_n\to\infty.
}
\tag{1.11}
$$

Interpretation:

### ultrafast crossing

$$
T_n\to0
$$

is a normalized temporal concentration defect.

### finite Euler-time crossing

$$
T_n\to T_\ast\in(0,\infty)
$$

produces a genuine finite-window Euler/Euler--Reynolds transition carrying a fixed kinetic-energy gap.

### backward-time escape

$$
T_n\to\infty
$$

moves the lower level to

$$
\tau=-\infty.
$$

The fixed finite windows near the terminal time may then look recurrent or steady.

This is a genuine backward-time escape coordinate and cannot be replaced by a finite-window transition theorem.

The third main result treats the finite crossing.

For fixed spatial filter ratio

$$
\sigma>0,
$$

define

$$
U_{n,\sigma}
=
S_\sigma v_n,
$$

and the actual SGS covariance

$$
R_{n,\sigma}
=
S_\sigma
(
v_n\otimes v_n
)
-
U_{n,\sigma}
\otimes U_{n,\sigma}.
$$

The exact resolved energy equation is

$$
\boxed{
\partial_\tau
\frac{|U_{n,\sigma}|^2}{2}
+
\nabla\cdot
\left[
\left(
\frac{|U_{n,\sigma}|^2}{2}
+
P_{n,\sigma}
\right)
U_{n,\sigma}
+
R_{n,\sigma}U_{n,\sigma}
\right]
=
\frac{\nu}{a_n}
\Delta
\frac{|U_{n,\sigma}|^2}{2}
-
\frac{\nu}{a_n}
|\nabla U_{n,\sigma}|^2
+
R_{n,\sigma}:\nabla U_{n,\sigma}.
}
\tag{1.12}
$$

The exact SGS energy is

$$
k_{n,\sigma}
=
\frac12
\left[
S_\sigma|v_n|^2
-
|U_{n,\sigma}|^2
\right]
\ge0.
$$

At the two selected endpoint times, the fixed full kinetic gap decomposes into:

- resolved coarse-energy change;
- SGS endpoint change;
- a fixed cutoff/filter-shell error.

Hence, unless a fixed **trace/SGS/localization defect** is already present, one may choose a fixed sufficiently small

$$
\sigma
$$

for which the resolved coarse energy still has a fixed nonzero endpoint gap.

Integrating (1.12) then gives the finite-crossing alternative

$$
\boxed{
c_0
\le
\left(
\iint
\chi
R_{n,\sigma}:\nabla U_{n,\sigma}
\right)_+
+
\mathcal B_{n,\sigma}^{ER}
+
\mathcal T_{n,\sigma}^{SGS}
+
\mathcal L_{n,\sigma}^{flt}
+
o(1),
}
\tag{1.13}
$$

where:

-:

  $$
  \mathcal B_{n,\sigma}^{ER}
  $$

  is the absolute pressure/transport boundary influx budget;

-:

  $$
  \mathcal T_{n,\sigma}^{SGS}
  $$

  is the SGS endpoint/trace mismatch;

-:

  $$
  \mathcal L_{n,\sigma}^{flt}
  $$

  is the cutoff/filter-shell localization budget.

The resolved viscous term has the favorable sign and cannot create the energy rise.

Therefore a finite-time Type-II kinetic crossing cannot converge to a completely silent Euler/Euler--Reynolds profile.

It must retain:

$$
\boxed{
\text{backscatter/resolved Reynolds work}
\ \vee\
\text{pressure/spatial influx}
\ \vee\
\text{SGS trace mismatch}
\ \vee\
\text{localization defect}.
}
\tag{1.14}
$$

If the total normalized viscous residue (1.1) is positive, that is an additional physical Navier--Stokes tax.

The fourth main result is an Euler Liouville NO-GO.

There exist nonzero smooth compactly supported steady solutions of the three-dimensional incompressible Euler equations.

Therefore:

$$
\boxed{
\textbf{
finite kinetic energy}
+
\textbf{
good spatial decay}
+
\textbf{
Euler}
\not\Rightarrow
\textbf{
zero}.
}
\tag{1.15}
$$

The Type-II branch cannot be closed by a generic finite-energy Euler Liouville theorem.

Known Type-II Euler Liouville arguments require additional structure.

The recent Type-II work of Seregin uses Euler scaling together with Liouville theorems in classes motivated by specific blowup scenarios.

Constantin's 2026 self-similarity analysis also gives strong restrictions only for special self-similar/outgoing classes.

Hence, after all native defects and normalized viscous payment vanish, the final state branch is a genuine **Euler energy-concentration transition problem**.

This is a real mathematical barrier, not an accounting artifact.

The correct next frontier is

$$
\boxed{
\textbf{
Materially Centered Type-II Euler Concentration /
Inviscid Reservoir Rigidity.
}
}
\tag{1.16}
$$

The goal is no longer to classify arbitrary Euler flows.

It is to exploit the inherited first-crossing, concentration-center, trace, and no-escape properties of the Euler profile actually generated by a hypothetical Navier--Stokes Type-II singularity.

---

# 2. Type-II normalized energy equation

The Euler-time amplitude normalization is

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

with

$$
q_n
=
a_n^{-2}p_n.
$$

Then

$$
\boxed{
\partial_\tau v_n
+
(v_n\cdot\nabla)v_n
+
\nabla q_n
=
\nu_n
\Delta v_n,
\qquad
\nu_n
=
\nu/a_n.
}
\tag{2.1}
$$

The normalized local energy equation is

$$
\boxed{
\partial_\tau
\frac{|v_n|^2}{2}
+
\nabla\cdot
\left[
\left(
\frac{|v_n|^2}{2}
+
q_n
\right)
v_n
\right]
=
\nu_n
\Delta
\frac{|v_n|^2}{2}
-
\nu_n
|\nabla v_n|^2.
}
\tag{2.2}
$$

---

# 3. Exact scaling of viscous payment

Since

$$
\nabla v_n
=
a_n^{-1}
\nabla u_n,
$$

and

$$
d\tau
=
a_n\,dt,
$$

one has

$$
\begin{aligned}
\nu_n
\iint
|\nabla v_n|^2dyd\tau
&=
\frac{\nu}{a_n}
\iint
\frac{|\nabla u_n|^2}{a_n^2}
a_n\,dxdt
\\
&=
\frac{\nu}{a_n^2}
\iint
|\nabla u_n|^2dxdt.
\end{aligned}
$$

Thus:

$$
\boxed{
\mathfrak V_n^{II}
=
\frac{\nu}{a_n^2}
\iint
|\nabla u_n|^2
}
\tag{3.1}
$$

is the correct normalized viscous payment.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. Viscosity coefficient versus viscous payment

The fact that

$$
\nu_n=\nu/a_n\to0
$$

does not imply

$$
\mathfrak V_n^{II}\to0.
$$

The gradients may grow fast enough that

$$
\nu_n
|\nabla v_n|^2
$$

has a nonzero measure limit.

Therefore DCRP-27's phrase "viscosity vanishes distributionally" must be separated into:

### equation-level viscous force

$$
\nu_n\Delta v_n
\to0
$$

against fixed smooth compact tests under the local

$$
L^2
$$

bound;

### energy-level viscous defect

$$
\nu_n
|\nabla v_n|^2dyd\tau
$$

may have a nonzero weak measure limit.

Status:

$$
\boxed{
\textbf{CORRECTION / STRENGTHENING}.
}
$$

---

# 5. Type-II viscous-residue dichotomy

After subsequence extraction, exactly one broad case holds.

### viscous-residue branch

There is

$$
\delta_\nu>0
$$

such that

$$
\boxed{
\mathfrak V_n^{II}
\ge
\delta_\nu
}
\tag{5.1}
$$

along a subsequence.

This is a fixed normalized physical dissipation payment.

### inviscid branch

$$
\boxed{
\mathfrak V_n^{II}\to0.
}
\tag{5.2}
$$

Only this branch is eligible for a defect-free Euler limit.

---

# 6. Two-level kinetic selection

Fix a smooth cutoff

$$
0\le\chi\le1
$$

supported in a controlled normalized ball and equal to one on the core.

Define

$$
\boxed{
\mathcal K_n(t)
=
\frac12
\int
\chi(x)
|u_n(x,t)|^2dx.
}
\tag{6.1}
$$

Assume the kinetic reservoir is unbounded.

Choose

$$
L_n\to\infty.
$$

Let

$$
t_n
$$

be the first selected time in the working time slab with

$$
\boxed{
\mathcal K_n(t_n)=L_n.
}
\tag{6.2}
$$

If the left face has

$$
\mathcal K_n(t_{\rm left})
\ge
L_n/2,
$$

the high kinetic reservoir is already entering through the time boundary.

Record:

$$
\boxed{
\text{time-face reservoir escape}.
}
\tag{6.3}
$$

Otherwise continuity on the smooth pre-singularity interval gives

$$
s_n<t_n
$$

with

$$
\boxed{
\mathcal K_n(s_n)=L_n/2.
}
\tag{6.4}
$$

Set

$$
a_n
=
L_n^{1/2}.
$$

Then normalized local energy satisfies

$$
\boxed{
\mathcal K_n^v(0)=1,
\qquad
\mathcal K_n^v(-T_n)=1/2.
}
\tag{6.5}
$$

---

# 7. Euler-time crossing trichotomy

Define

$$
T_n
=
a_n(t_n-s_n).
$$

After a subsequence:

### T0 — temporal concentration

$$
\boxed{
T_n\to0.
}
\tag{7.1}
$$

### TF — finite Euler-time crossing

$$
\boxed{
T_n\to T_\ast
\in
(0,\infty).
}
\tag{7.2}
$$

### TI — backward-time escape

$$
\boxed{
T_n\to\infty.
}
\tag{7.3}
$$

Status:

$$
\boxed{
\textbf{PROVED by subsequence classification}.
}
$$

---

# 8. Why backward-time escape matters

If

$$
T_n\to\infty,
$$

the lower selected energy level moves to

$$
\tau=-\infty.
$$

A finite normalized terminal window may therefore converge to a recurrent or stationary Euler object even though the original branch previously crossed a much lower kinetic level.

The historical transition is no longer represented in a bounded time window.

It must be retained as a backward-time escape/recurrence coordinate.

---

# 9. Fixed-scale coarse fields

In the finite-crossing branch define

$$
U_{n,\sigma}
=
S_\sigma v_n,
$$

$$
P_{n,\sigma}
=
S_\sigma q_n,
$$

and

$$
R_{n,\sigma}
=
S_\sigma
(
v_n\otimes v_n
)
-
U_{n,\sigma}
\otimes U_{n,\sigma}.
$$

Then

$$
\boxed{
\partial_\tau U_{n,\sigma}
-
\nu_n\Delta U_{n,\sigma}
+
\nabla\cdot
(
U_{n,\sigma}\otimes U_{n,\sigma}
)
+
\nabla P_{n,\sigma}
=
-\nabla\cdot R_{n,\sigma}.
}
\tag{9.1}
$$

---

# 10. Exact resolved energy identity

Let

$$
e_{n,\sigma}
=
|U_{n,\sigma}|^2/2.
$$

Then

$$
\boxed{
\partial_\tau e_{n,\sigma}
+
\nabla\cdot
\left[
(
e_{n,\sigma}
+
P_{n,\sigma}
)
U_{n,\sigma}
+
R_{n,\sigma}U_{n,\sigma}
\right]
=
\nu_n\Delta e_{n,\sigma}
-
\nu_n
|\nabla U_{n,\sigma}|^2
+
R_{n,\sigma}:\nabla U_{n,\sigma}.
}
\tag{10.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 11. Resolved viscous term vanishes at fixed filter scale

For fixed

$$
\sigma
$$

and fixed compact region:

$$
\|\nabla U_{n,\sigma}\|_2
\le
C_\sigma
\|v_n\|_2.
$$

Hence on a finite Euler-time interval:

$$
\boxed{
\nu_n
\iint
|\nabla U_{n,\sigma}|^2
\le
C_{\sigma,T}
\frac{\nu}{a_n}
\to0.
}
\tag{11.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. SGS endpoint energy

Define

$$
\boxed{
k_{n,\sigma}
=
\frac12
\left[
S_\sigma|v_n|^2
-
|U_{n,\sigma}|^2
\right]
\ge0.
}
\tag{12.1}
$$

and

$$
\boxed{
K_{n,\sigma}^{SGS}(\tau)
=
\int
\chi
k_{n,\sigma}(y,\tau)dy.
}
\tag{12.2}
$$

Then

$$
\boxed{
\int
\chi
S_\sigma
\left(
\frac{|v_n|^2}{2}
\right)
=
\int
\chi
e_{n,\sigma}
+
K_{n,\sigma}^{SGS}.
}
\tag{12.3}
$$

Also

$$
\boxed{
\frac12
\int
\chi
S_\sigma|v_n|^2
-
\frac12
\int
\chi
|v_n|^2
=
\frac12
\int
(
S_\sigma\chi-\chi
)
|v_n|^2.
}
\tag{12.4}
$$

The last term is a cutoff-shell trace term.

---

# 13. Endpoint-gap alternative

The original normalized endpoint gap equals

$$
1/2.
$$

For fixed sufficiently small

$$
\sigma,
$$

at least one of the following carries a fixed fraction of this gap:

$$
\boxed{
\text{cutoff-shell trace defect},
}
\tag{13.1}
$$

$$
\boxed{
\left|
K_{n,\sigma}^{SGS}(0)
-
K_{n,\sigma}^{SGS}(-T_n)
\right|
\ge
c_{SGS}>0,
}
\tag{13.2}
$$

or

$$
\boxed{
\left|
E_{n,\sigma}^{res}(0)
-
E_{n,\sigma}^{res}(-T_n)
\right|
\ge
c_{res}>0.
}
\tag{13.3}
$$

Status:

$$
\boxed{
\textbf{PROVED from (12.3)--(12.4)}.
}
$$

---

# 14. Localized coarse transition identity

Integrating (10.1) against

$$
\chi
$$

over

$$
[-T_n,0]
$$

gives

$$
\boxed{
E_{n,\sigma}^{res}(0)
-
E_{n,\sigma}^{res}(-T_n)
+
\nu_n
\iint
\chi
|\nabla U_{n,\sigma}|^2
=
W_{n,\sigma}^{ER}
+
B_{n,\sigma}^{ER},
}
\tag{14.1}
$$

where

$$
\boxed{
W_{n,\sigma}^{ER}
=
\iint
\chi
R_{n,\sigma}:\nabla U_{n,\sigma},
}
\tag{14.2}
$$

and

$$
\boxed{
B_{n,\sigma}^{ER}
=
\iint
\nabla\chi
\cdot
\left[
(
e_{n,\sigma}
+
P_{n,\sigma}
)
U_{n,\sigma}
+
R_{n,\sigma}U_{n,\sigma}
\right]
+
\nu_n
\iint
(\Delta\chi)
e_{n,\sigma}.
}
\tag{14.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 15. Finite Type-II Crossing Cannot Be Silent

Assume

$$
T_n\to T_\ast\in(0,\infty)
$$

and assume time-face, temporal-concentration, backward-time, cutoff-shell, and SGS endpoint defects vanish.

Then for some fixed

$$
\sigma>0
$$

and

$$
c_\ast>0,
$$

$$
\boxed{
\left(
W_{n,\sigma}^{ER}
\right)_+
+
\left|
B_{n,\sigma}^{ER}
\right|
\ge
c_\ast
}
\tag{15.1}
$$

for all sufficiently large

$$
n.
$$

### Proof

The endpoint-gap alternative gives a fixed resolved energy gap.

The resolved viscous term is nonnegative on the left side of (14.1) and tends to zero at fixed

$$
\sigma.
$$

A fixed positive resolved energy increase therefore requires positive resolved Reynolds/backscatter work or a fixed pressure/transport/localization budget.

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

# 16. Sign interpretation

The standard forward SGS flux convention is

$$
\Pi_\sigma
=
-
R_\sigma:\nabla U_\sigma.
$$

Hence

$$
W^{ER}
=
\int
R_\sigma:\nabla U_\sigma
$$

is the **backscatter/source sign** for the resolved field.

A positive resolved kinetic-energy crossing may therefore be financed by:

- backscatter from unresolved scales;
- pressure/advection influx through the boundary;
- SGS endpoint storage mismatch.

This is a transfer theorem, not a global dissipation theorem.

---

# 17. Euler--Reynolds finite-transition limit

On the inviscid branch:

$$
\mathfrak V_n^{II}\to0.
$$

After weak/Young extraction:

$$
v_n
\stackrel{\ast}{\rightharpoonup}
v,
$$

and

$$
v_n\otimes v_n
\rightharpoonup
Q
=
v\otimes v+R_E.
$$

Then

$$
\boxed{
\partial_\tau v
+
\mathbb P\nabla\cdot
(
v\otimes v+R_E
)
=
0.
}
\tag{17.1}
$$

At fixed filter scale:

$$
\boxed{
R_\sigma^{tot}
=
S_\sigma
(
v\otimes v+R_E
)
-
U_\sigma\otimes U_\sigma.
}
\tag{17.2}
$$

The finite crossing retains, modulo the explicit trace/pressure/localization alternatives, nonzero coarse work or boundary/transport flux.

Thus the finite Type-II limit is dynamically active.

---

# 18. General Euler Liouville NO-GO

The strong branch

$$
R_E=0
$$

solves the incompressible Euler equation.

But nonzero smooth compactly supported steady three-dimensional Euler flows exist.

Therefore finite kinetic energy, spatial localization, and smoothness alone do not force triviality.

This is an exact NO-GO to a generic finite-energy Euler Liouville closure.

---

# 19. What first crossing adds

The extracted finite-transition profile is not arbitrary.

It inherits a fixed local kinetic-energy transition between two normalized levels.

A genuinely steady Euler flow cannot itself realize this finite crossing.

Therefore the remaining Euler object must exhibit:

- nonstationary concentration/deformation;
- local boundary/material influx;
- subscale backscatter;
- or an endpoint/trace defect.

This is narrower than the class of all finite-energy Euler solutions.

---

# 20. Known rigid Euler subclasses

The current Type-II literature excludes selected Euler scenarios rather than all Euler profiles.

Seregin's 2023 and 2026 Type-II papers use Euler scaling together with Liouville theorems for classes dictated by specific blowup hypotheses.

Constantin's 2026 self-similarity analysis proves, among other guardrails, that under a local outgoing property a globally self-similar smooth Euler profile must satisfy the parabolic threshold

$$
\gamma\ge1/2.
$$

Selected axisymmetric smooth self-similar classes are similarly restricted.

These results remove important special Type-II routes but do not eliminate the general finite-transition Euler profile extracted here.

---

# 21. Backward-time escape and steady profiles

If

$$
T_n\to\infty,
$$

the lower selected level moves to the remote Euler past.

A terminal finite-window profile may therefore be recurrent or stationary.

This is exactly the regime in which nontrivial steady Euler examples show that finite energy and spatial localization alone cannot provide a Liouville theorem.

Thus backward-time escape is a genuine hard branch.

---

# 22. Anomalous-dissipation measure

The measures

$$
\boxed{
\nu_n
|\nabla v_n|^2dyd\tau
}
\tag{22.1}
$$

may converge weakly to a nonnegative measure

$$
\boxed{
\mu_{\rm diss}^{II}\ge0.
}
\tag{22.2}
$$

If

$$
\mu_{\rm diss}^{II}\neq0,
$$

a real Navier--Stokes viscous defect survives the vanishing-viscosity equation limit.

The strongest inviscid branch therefore imposes

$$
\boxed{
\mu_{\rm diss}^{II}=0.
}
\tag{22.3}
$$

---

# 23. Updated Type-II normal form

The kinetic branch

$$
A_n\to\infty
$$

now yields at least one of:

$$
\boxed{
\begin{aligned}
&
\text{time-face reservoir escape}
\\
&\vee
\text{ultrafast temporal concentration}
\\
&\vee
\text{backward-time escape}
\\
&\vee
\text{positive normalized viscous residue}
\\
&\vee
\text{trace/SGS/localization defect}
\\
&\vee
\text{finite Euler--Reynolds work/transport transition}
\\
&\vee
\text{genuine inviscid Euler concentration profile}.
\end{aligned}
}
\tag{23.1}
$$

No silent generic Euler limit remains.

---

# 24. Exact zero-cost finite-transition consequence

If the completed Type-II native package contains:

- normalized viscous residue;
- selected energy traces;
- SGS endpoint mismatch;
- temporal face / backward-time escape;
- pressure/transport work;
- spatial localization;
- Euler--Reynolds defect,

then an exact zero-cost finite-time Type-II transition would make every right-hand channel in (23.1) vanish.

The finite-crossing theorem forbids this.

Hence

$$
\boxed{
\textbf{
finite Euler-time Type-II energy crossing}
\cap
\textbf{
exact zero-cost completed package}
=
\varnothing.
}
\tag{24.1}
$$

This is a profile-level coercive gap.

It does not solve critical summability over infinitely many scales.

---

# 25. Remaining hard Type-II branches

Two difficult branches remain.

### backward-time escape

$$
T_n\to\infty.
$$

The transition history disappears to

$$
-\infty_\tau.
$$

### genuine inviscid Euler concentration

All normalized NS viscosity, Euler--Reynolds defect, trace concentration, localization, and time-escape channels vanish, leaving a genuine nonstationary Euler profile with inherited first-crossing/concentration structure.

Neither is eliminated by a general theorem in the current corpus.

---

# 26. The genuine Euler barrier

A route that scales viscosity to zero can eventually encounter a problem of genuine Euler dynamics.

That is unavoidable at the present level of generality.

The remaining target must use the special inherited Type-II structure:

- first-crossing normalization;
- concentration-center normalization;
- no spatial/scale escape;
- no anomalous dissipation;
- no Reynolds defect;
- no backward-time escape;
- local energy trace constraints.

The goal is not a Liouville theorem for arbitrary Euler.

It is a rigidity theorem for this special class.

---

# 27. Correct next frontier

The next target is

$$
\boxed{
\textbf{
Materially Centered Type-II Euler Concentration /
Inviscid Reservoir Rigidity Lemma}.
}
$$

A sufficient theorem would show that a genuine Euler profile satisfying all zero-defect and no-escape conditions is either trivial or carries a nonzero material deformation/energy-flux carrier that feeds back into the native PFET/transition package.

---

# 28. Alternative Navier--Stokes-specific route

One may instead try to prove that every genuine Navier--Stokes Type-II kinetic crossing has

$$
\boxed{
\liminf
\mathfrak V_n^{II}
>
0.
}
\tag{28.1}
$$

That would preserve a fixed normalized viscous tax and avoid the Euler barrier.

No unconditional theorem of this form is proved here.

Recent Type-II literature explicitly treats Euler scaling as a serious possible limiting regime, so this cannot be assumed.

---

# 29. Source-status audit

## Seregin 2023 / 2026

These works explicitly use Euler scaling to study selected local Type-II Navier--Stokes blowup scenarios and combine it with Euler Liouville theorems adapted to those scenarios.

## Constantin 2026

The paper proves rigorous constraints on putative self-similar 3D Euler blowup, including the parabolic-threshold restriction under outgoing/axisymmetric assumptions.

## Gavrilov / Constantin--La--Vicol

These works construct or explain nontrivial smooth compactly supported steady 3D Euler flows.

They rule out a universal finite-energy/localization Liouville shortcut.

## anomalous dissipation

Vanishing-viscosity literature treats a nonzero limit of

$$
\nu|\nabla u^\nu|^2
$$

as a genuine possible energy defect.

DCRP-28 therefore separates equation-level vanishing viscosity from energy-level viscous residue.

---

# 30. End state

The key correction is

$$
\boxed{
\nu/a_n\to0
\not\Rightarrow
\mathfrak V_n^{II}\to0.
}
$$

The correct normalized payment is

$$
\boxed{
\mathfrak V_n^{II}
=
\frac{\nu}{a_n^2}
\iint
|\nabla u_n|^2.
}
$$

The kinetic crossing has the Euler-time trichotomy

$$
\boxed{
T_n\to0
\ \vee\
T_n\to T_\ast\in(0,\infty)
\ \vee\
T_n\to\infty.
}
$$

A finite crossing has a fixed native transfer gap:

$$
\boxed{
\text{backscatter/coarse Reynolds work}
\ \vee\
\text{pressure/transport influx}
\ \vee\
\text{SGS endpoint mismatch}
\ \vee\
\text{localization defect}.
}
$$

Thus a finite-time Type-II Euler--Reynolds transition cannot be an exact silent profile.

But generic finite-energy Euler cannot be killed by a general Liouville theorem.

The final hard state is a special inviscid Type-II Euler concentration profile with all defect and escape channels removed.

The next single frontier is

$$
\boxed{
\textbf{
Materially Centered Type-II Euler Concentration /
Inviscid Reservoir Rigidity.
}
}
$$
