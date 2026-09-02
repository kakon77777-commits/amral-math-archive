# NS-DCRP-30 — Same-Parent Euler Scaling Recurrence, Atom-Free Exponent Window, and Mandatory Global-Energy Tail Escape

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit the spacetime normalization of the DCRP-29 backward-ancient Type-II branch;
  2. derive the exact relation between two Type-II profiles extracted from the same physical Navier--Stokes parent;
  3. prove that a compact nondegenerate recurrent same-parent branch is an Euler generalized/discrete self-similar branch;
  4. use raw-energy vanishing and record-amplitude selection to derive the similarity-exponent window;
  5. prove that the atom-free branch necessarily loses the normalized **global** kinetic-energy distribution to spatial infinity;
  6. distinguish unavoidable global-energy tail escape from obstruction-carrier escape;
  7. intersect the new exponent/tail normal form with known Euler DSS/self-similar rigidity theorems.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - D. Chae, T.-P. Tsai, *On discretely self-similar solutions of the Euler equations*, arXiv:1304.7414;
  - D. Chae, *Euler's equations and the maximum principle*, arXiv:1308.1051;
  - L. Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619;
  - D. Chae, J. Wolf, *On the Discretely Self-similar Solutions to the Euler Equations in R^3*, Journal of Nonlinear Science 33 (2023), article 115;
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3;
  - G. Seregin, *On potential Type II blowups for the Navier--Stokes equations*, arXiv:2606.29468.
- internal dependencies:
  - DCRP-27 Type-II Euler--Reynolds reprofiling;
  - DCRP-28 double-level crossing and viscous residue;
  - DCRP-29 raw-energy atom/material crossing split;
  - MORP translation/scale/pressure/transition normalization.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-29 left the strongest kinetic Type-II state normal form as

$$
\boxed{
\beta_n\to0,
\qquad
T_n\to\infty,
\qquad
\mathfrak V_n^{II}\to0,
}
\tag{1.1}
$$

with no finite-time material-transition defect and with an ancient/recurrent Euler profile appearing on every fixed terminal Euler-time window.

This round first corrects one spacetime interpretation.

The two-step Type-II normalization is

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

followed by

$$
v_n(y,\tau)
=
a_n^{-1}
u_n
\left(
y,
\tau/a_n
\right).
$$

Equivalently in physical variables,

$$
\boxed{
v_n(y,\tau)
=
\frac{r_n}{a_n}
U
\left(
x_n+r_ny,
t_n+\frac{r_n^2}{a_n}\tau
\right).
}
\tag{1.2}
$$

Thus:

- physical velocity scale:

  $$
  \boxed{
  U_{\rm amp}^{(n)}
  =
  a_n/r_n;
  }
  \tag{1.3}
  $$

- physical Euler-time scale:

  $$
  \boxed{
  t_{\rm Euler}^{(n)}
  =
  r_n^2/a_n;
  }
  \tag{1.4}
  $$

- material displacement during one normalized Euler time:

  $$
  \boxed{
  U_{\rm amp}^{(n)}
  t_{\rm Euler}^{(n)}
  =
  r_n.
  }
  \tag{1.5}
  $$

Therefore the Euler-time amplitude normalization is spatially consistent with the same physical core scale:

$$
r_n.
$$

There is no missing extra transport length:

$$
a_nr_n.
$$

That quantity does **not** have the interpretation assigned to it in the preliminary DCRP-30 scratch route.

The second main result is an exact same-parent transition identity.

For two Type-II profiles from the same physical solution define

$$
\boxed{
\lambda_n
=
\frac{r_{n+1}}{r_n},
}
\tag{1.6}
$$

$$
\boxed{
\mu_n
=
\frac{a_{n+1}}{a_n},
}
\tag{1.7}
$$

$$
\boxed{
c_n
=
\frac{\lambda_n}{\mu_n},
}
\tag{1.8}
$$

$$
\boxed{
b_n
=
\frac{x_{n+1}-x_n}{r_n},
}
\tag{1.9}
$$

and

$$
\boxed{
d_n
=
\frac{a_n}{r_n^2}
\left(
t_{n+1}-t_n
\right).
}
\tag{1.10}
$$

Then exactly,

$$
\boxed{
v_{n+1}(y,\tau)
=
c_n
v_n
\left(
b_n+\lambda_ny,
d_n+c_n\lambda_n\tau
\right).
}
\tag{1.11}
$$

No PDE estimate is used.

It is a pure identity resulting from the fact that both profiles come from the **same parent solution**.

Therefore a sequence cannot independently choose:

- spatial scaling;
- amplitude scaling;
- time scaling;
- center drift;
- time-origin drift.

They are linked.

If a same-parent branch is compact and recurrent with

$$
\lambda_n\to\lambda_\ast
\in(0,1),
$$

$$
\mu_n\to\mu_\ast
\in(0,\infty),
$$

$$
b_n\to b_\ast,
$$

and

$$
d_n\to d_\ast,
$$

and both the current and next normalized states converge to the same nonzero strong Euler profile:

$$
v,
$$

then:

$$
\boxed{
v(y,\tau)
=
c_\ast
v
\left(
b_\ast+\lambda_\ast y,
d_\ast+c_\ast\lambda_\ast\tau
\right),
}
\tag{1.12}
$$

where

$$
c_\ast
=
\lambda_\ast/\mu_\ast.
$$

After translating to the fixed point of the affine spatial/time map, this becomes:

$$
\boxed{
v(y,\tau)
=
c_\ast
v
\left(
\lambda_\ast y,
c_\ast\lambda_\ast\tau
\right).
}
\tag{1.13}
$$

Write

$$
\boxed{
c_\ast
=
\lambda_\ast^\alpha.
}
\tag{1.14}
$$

Then:

$$
\boxed{
v(y,\tau)
=
\lambda_\ast^\alpha
v
\left(
\lambda_\ast y,
\lambda_\ast^{\alpha+1}\tau
\right).
}
\tag{1.15}
$$

This is exactly the two-parameter Euler discrete self-similarity law.

Hence:

$$
\boxed{
\textbf{
same-parent compact recurrence}
\Longrightarrow
\textbf{
Euler DSS/generalized self-similarity}.
}
\tag{1.16}
$$

If any of the transition parameters fails to have a nondegenerate compact subsequence, the failure is itself one of:

- relative-scale escape;
- amplitude-ratio escape;
- spatial-center escape;
- Euler-time origin escape;
- transition residual.

Thus the DSS conclusion is the compact alternative, not an imposed ansatz.

The third main result is the atom-free exponent window.

Choose the Type-II sequence to be a record-amplitude subsequence so that:

$$
\boxed{
a_{n+1}\ge a_n,
}
\tag{1.17}
$$

hence:

$$
\mu_n\ge1.
$$

The raw physical core energy is:

$$
\boxed{
\beta_n
=
r_na_n^2.
}
\tag{1.18}
$$

Its consecutive ratio is:

$$
\boxed{
\frac{\beta_{n+1}}{\beta_n}
=
\lambda_n\mu_n^2
=
\frac{\lambda_n^3}{c_n^2}.
}
\tag{1.19}
$$

In the nondegenerate recurrent limit:

$$
\boxed{
q_\ast
=
\lim
\frac{\beta_{n+1}}{\beta_n}
=
\lambda_\ast^{3-2\alpha}.
}
\tag{1.20}
$$

Because:

$$
\mu_\ast\ge1,
$$

one has:

$$
\boxed{
\alpha\ge1.
}
\tag{1.21}
$$

If:

$$
\beta_n\to0
$$

and the ratio limit exists, necessarily:

$$
q_\ast\le1.
$$

Since:

$$
0<\lambda_\ast<1,
$$

this gives:

$$
\boxed{
\alpha\le\frac32.
}
\tag{1.22}
$$

Therefore:

$$
\boxed{
1
\le
\alpha
\le
\frac32.
}
\tag{1.23}
$$

Let the standard Euler spatial similarity exponent be:

$$
\boxed{
\gamma
=
\frac1{\alpha+1}.
}
\tag{1.24}
$$

Then:

$$
\boxed{
\frac25
\le
\gamma
\le
\frac12.
}
\tag{1.25}
$$

If the amplitude grows by a genuinely nontrivial geometric factor:

$$
\mu_\ast>1,
$$

then:

$$
\boxed{
\alpha>1
\quad\Longleftrightarrow\quad
\gamma<1/2.
}
\tag{1.26}
$$

If the raw-energy ratio is strictly contractive:

$$
q_\ast<1,
$$

then:

$$
\boxed{
\alpha<3/2
\quad\Longleftrightarrow\quad
\gamma>2/5.
}
\tag{1.27}
$$

Thus the strict geometric atom-free Type-II recurrence lies in:

$$
\boxed{
\frac25
<
\gamma
<
\frac12.
}
\tag{1.28}
$$

The endpoints:

$$
\gamma=1/2
$$

and:

$$
\gamma=2/5
$$

are marginal slow-ratio cases and require separate treatment.

This exponent window is not invented by dimensional guesswork.

It follows from:

- same-parent transition kinematics;
- monotone record amplitude;
- vanishing raw physical core energy.

It coincides with the difficult sub-parabolic Euler similarity window highlighted by recent Euler/Type-II work.

The fourth main result is a mandatory global-energy tail escape.

The Type-II normalized field has global kinetic energy

$$
\boxed{
\|v_n(\tau)\|_2^2
=
\frac{
\|U(t)\|_2^2
}{
r_na_n^2
}
=
\frac{
\|U(t)\|_2^2
}{
\beta_n
}.
}
\tag{1.29}
$$

Thus:

$$
\boxed{
\beta_n\to0
\Longrightarrow
\|v_n\|_2^2\to\infty
}
\tag{1.30}
$$

whenever the physical parent still has nonzero total energy.

Normalize the global kinetic-energy distribution:

$$
\boxed{
d\pi_n(y)
=
\frac{
|v_n(y,0)|^2dy
}{
\|v_n(0)\|_2^2
}.
}
\tag{1.31}
$$

Then for every fixed:

$$
R<\infty,
$$

$$
\boxed{
\pi_n(B_R)
=
\frac{
\displaystyle
\int_{
B_{Rr_n}(x_n)
}
|U(x,t_n)|^2dx
}{
\|U(t_n)\|_2^2
}.
}
\tag{1.32}
$$

If:

-:

  $$
  t_n\uparrow T;
  $$

-:

  $$
  x_n\to x_\ast;
  $$

- the terminal energy measure has no atom at:

  $$
  x_\ast;
  $$

then for every fixed:

$$
R,
$$

$$
\boxed{
\pi_n(B_R)\to0.
}
\tag{1.33}
$$

Therefore in the one-point compactification of normalized physical space:

$$
\boxed{
\pi_n
\stackrel{\ast}{\rightharpoonup}
\delta_{\infty_x}.
}
\tag{1.34}
$$

Hence:

$$
\boxed{
\textbf{
atom-free Type-II}
\Longrightarrow
\textbf{
mandatory global kinetic-energy escape to normalized spatial infinity}.
}
\tag{1.35}
$$

This corrects one phrase in DCRP-29.

The strongest atom-free branch **cannot** satisfy "no spatial escape" if spatial escape refers to the entire globally normalized kinetic-energy distribution.

The correct zero-defect condition is:

$$
\boxed{
\textbf{
no escape of the selected obstruction carrier beyond the explicitly required global-energy tail}.
}
}
\tag{1.36}
$$

The global tail is unavoidable.

It must not be confused with disappearance of the local Type-II obstruction.

The fifth main result is a finite-energy DSS NO-GO for the atom-free recurrent branch.

Suppose:

$$
v
$$

is a nonzero exact Euler DSS solution satisfying:

$$
v(y,\tau)
=
\lambda^\alpha
v
\left(
\lambda y,
\lambda^{\alpha+1}\tau
\right)
$$

and suppose:

$$
v(\tau)
\in L^2(\mathbb R^3)
$$

with conserved nonzero kinetic energy.

Then:

$$
\begin{aligned}
\|v(\tau)\|_2^2
&=
\lambda^{2\alpha}
\int
|
v(
\lambda y,
\lambda^{\alpha+1}\tau
)
|^2dy
\\
&=
\lambda^{2\alpha-3}
\|
v(
\lambda^{\alpha+1}\tau
)
\|_2^2.
\end{aligned}
$$

Energy conservation gives:

$$
\boxed{
1
=
\lambda^{2\alpha-3}.
}
\tag{1.37}
$$

For:

$$
\lambda\neq1,
$$

$$
\boxed{
\alpha=3/2.
}
\tag{1.38}
$$

Therefore every nonzero finite-energy Euler DSS solution must live at the energy-conserving exponent:

$$
\alpha=3/2.
$$

Consequently:

$$
\boxed{
\textbf{
strict atom-free recurrence with }
\alpha<3/2
\Longrightarrow
\textbf{
the Euler profile has infinite global kinetic energy}.
}
\tag{1.39}
$$

This removes compactly supported steady Euler flows from the strict same-parent DSS survivor.

They remain counterexamples to a **generic ancient Euler Liouville theorem**, but they are not models of the strict atom-free DSS branch.

The surviving profile is necessarily tail-fed.

Known Euler DSS rigidity results then prune several subbranches.

- Chae--Tsai and Chae exclude DSS solutions under decay/integrability assumptions on the velocity/vorticity profile.
- Xue proves refined nonexistence/energy-growth alternatives using the local energy inequality and pressure representation.
- Chae--Wolf prove that for:

  $$
  \alpha\ge3/2,
  $$

  a DSS Euler profile with sublinear growth at infinity must be spatially constant.
- Constantin--Ignatova--Vicol prove that a smooth globally self-similar Euler profile with the local outgoing property must satisfy:

  $$
  \gamma\ge1/2.
  $$

Therefore an interior strict Type-II recurrence:

$$
\boxed{
1<\alpha<3/2
}
$$

or:

$$
\boxed{
2/5<\gamma<1/2
}
$$

must evade **all** of the following:

1. the available velocity/vorticity decay/integrability Liouville classes;
2. the energy-conserving:

   $$
   \alpha=3/2
   $$

   regime;
3. the outgoing self-similar Lagrangian regime.

Thus it must be a:

$$
\boxed{
\textbf{
tail-fed, non-outgoing/trapped, infinite-energy DSS Euler recurrence profile}.
}
\tag{1.40}
$$

The final important point is that this tail behavior is not arbitrary.

For profile classes satisfying Xue's global integrability assumptions, a nontrivial DSS profile in:

$$
-1<\alpha<3/2
$$

has the sharp local-energy growth

$$
\boxed{
\int_0^{S_0}
\int_{|y|\le L}
|V(y,s)|^2dyds
\sim
L^{3-2\alpha}.
}
\tag{1.41}
$$

For the Type-II exponent window:

$$
1<\alpha<3/2,
$$

the exponent satisfies:

$$
\boxed{
0
<
3-2\alpha
<
1.
}
\tag{1.42}
$$

Hence the admissible recurrent Euler tail is neither:

- finite energy;
- nor generic volume-filling:

  $$
  O(L^3);
  $$

it is a **sublinear divergent energy tail**.

This gives the new strongest state normal form:

$$
\boxed{
\textbf{
critical tail-fed DSS Euler recurrence}
}
\tag{1.43}
$$

with:

$$
\boxed{
2/5
<
\gamma
<
1/2
}
$$

in the strict geometric regime, together with:

- non-outgoing/trapped Lagrangian behavior;
- infinite global normalized energy;
- vanishing raw physical core energy;
- mandatory normalized global-energy escape to:

  $$
  \infty_x;
  $$

- no finite-time material crossing;
- no anomalous viscous residue;
- no Reynolds/trace/localization defect beyond the required tail.

The next exact frontier is therefore:

$$
\boxed{
\textbf{
Critical-Tail DSS Euler /
Same-Parent Tail-Pressure Rigidity Lemma}.
}
\tag{1.44}
$$

The target is to prove that the required sublinear infinite Euler tail cannot remain dynamically disconnected from the local Type-II core.

One must show that it forces at least one of:

1. nonzero far-field/harmonic pressure work;
2. nonzero material deformation of the core;
3. scale/spatial carrier transport across the same-parent return;
4. a known DSS/outgoing/decay Liouville class;
5. failure of the atom-free/raw-energy normalization.

This is now substantially narrower than a generic ancient Euler problem.

---

# 2. Correction — physical transport length in the Type-II normalization

Start from the physical solution:

$$
U(x,t).
$$

The Type-II profile is:

$$
\boxed{
v_n(y,\tau)
=
\frac{r_n}{a_n}
U
\left(
x_n+r_ny,
t_n+\frac{r_n^2}{a_n}\tau
\right).
}
\tag{2.1}
$$

Therefore:

$$
\boxed{
U
=
\frac{a_n}{r_n}
v_n.
}
\tag{2.2}
$$

A normalized Euler-time interval:

$$
\Delta\tau\sim1
$$

corresponds to:

$$
\boxed{
\Delta t_{\rm phys}
\sim
r_n^2/a_n.
}
\tag{2.3}
$$

The corresponding physical material displacement is:

$$
\boxed{
\frac{a_n}{r_n}
\frac{r_n^2}{a_n}
=
r_n.
}
\tag{2.4}
$$

Thus the material cutoff of DCRP-29 is consistent with the original core radius.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 3. Exact same-parent transition formula

Let:

$$
v_n(y,\tau)
=
\frac{r_n}{a_n}
U
\left(
x_n+r_ny,
t_n+\frac{r_n^2}{a_n}\tau
\right).
$$

At the next extraction:

$$
v_{n+1}(y,\tau)
=
\frac{r_{n+1}}{a_{n+1}}
U
\left(
x_{n+1}+r_{n+1}y,
t_{n+1}
+
\frac{r_{n+1}^2}{a_{n+1}}
\tau
\right).
$$

Define:

$$
\lambda_n
=
r_{n+1}/r_n,
$$

$$
\mu_n
=
a_{n+1}/a_n,
$$

$$
b_n
=
(x_{n+1}-x_n)/r_n,
$$

and:

$$
d_n
=
a_n
(t_{n+1}-t_n)
/r_n^2.
$$

Then the physical point in the second profile corresponds in the first profile to:

$$
\boxed{
y_n
=
b_n+\lambda_ny,
}
\tag{3.1}
$$

and:

$$
\boxed{
\tau_n
=
d_n
+
\frac{
\lambda_n^2
}{
\mu_n
}
\tau.
}
\tag{3.2}
$$

The amplitude ratio is:

$$
\frac{
r_{n+1}/a_{n+1}
}{
r_n/a_n
}
=
\frac{
\lambda_n
}{
\mu_n
}.
$$

Therefore:

$$
\boxed{
v_{n+1}(y,\tau)
=
\frac{
\lambda_n
}{
\mu_n
}
v_n
\left(
b_n+\lambda_ny,
d_n+
\frac{
\lambda_n^2
}{
\mu_n
}
\tau
\right).
}
\tag{3.3}
$$

Set:

$$
c_n
=
\lambda_n/\mu_n.
$$

Then:

$$
\boxed{
v_{n+1}(y,\tau)
=
c_n
v_n
\left(
b_n+\lambda_ny,
d_n+c_n\lambda_n\tau
\right).
}
\tag{3.4}
$$

Status:

$$
\boxed{
\textbf{PROVED EXACTLY}.
}
$$

---

# 4. Transition-parameter compactness alternatives

The same-parent identity shows that a recurrent profile can fail compactness only through explicit transition coordinates.

After subsequence extraction:

### spatial scale

$$
\lambda_n
\to
0
$$

or stays in a compact subset of:

$$
(0,1).
$$

### amplitude ratio

$$
\mu_n
\to
0,
\infty
$$

or stays finite/nonzero.

### center drift

$$
|b_n|
\to\infty
$$

or remains bounded.

### Euler-time origin drift

$$
|d_n|
\to\infty
$$

or remains bounded.

Thus:

$$
\boxed{
\textbf{
same-parent Type-II}
\Longrightarrow
\textbf{
transition escape}
\ \vee\
\textbf{
nondegenerate Euler scaling recurrence}.
}
\tag{4.1}
$$

The escape cases belong to the completed transition package.

---

# 5. Compact recurrence implies generalized DSS

Assume:

$$
\lambda_n\to\lambda_\ast
\in(0,1),
$$

$$
\mu_n\to\mu_\ast
\in(0,\infty),
$$

$$
b_n\to b_\ast,
$$

$$
d_n\to d_\ast.
$$

Assume both:

$$
v_n
$$

and:

$$
v_{n+1}
$$

converge strongly on compact sets to the same nonzero profile:

$$
v.
$$

Pass to the limit in (3.4):

$$
\boxed{
v(y,\tau)
=
c_\ast
v
\left(
b_\ast+\lambda_\ast y,
d_\ast+c_\ast\lambda_\ast\tau
\right).
}
\tag{5.1}
$$

If:

$$
\lambda_\ast\neq1
$$

and:

$$
c_\ast\lambda_\ast\neq1,
$$

the affine map has fixed space/time points:

$$
y_0
=
\frac{
b_\ast
}{
1-\lambda_\ast
},
$$

$$
\tau_0
=
\frac{
d_\ast
}{
1-c_\ast\lambda_\ast
}.
$$

Translate to:

$$
\widetilde y
=
y-y_0,
$$

$$
\widetilde\tau
=
\tau-\tau_0.
$$

Then:

$$
\boxed{
\widetilde v(
\widetilde y,
\widetilde\tau
)
=
c_\ast
\widetilde v
\left(
\lambda_\ast\widetilde y,
c_\ast\lambda_\ast
\widetilde\tau
\right).
}
\tag{5.2}
$$

Set:

$$
c_\ast
=
\lambda_\ast^\alpha.
$$

Then:

$$
\boxed{
\widetilde v(
y,\tau
)
=
\lambda_\ast^\alpha
\widetilde v
\left(
\lambda_\ast y,
\lambda_\ast^{\alpha+1}\tau
\right).
}
\tag{5.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is precisely Euler discrete self-similarity.

---

# 6. Record-amplitude selection

Because:

$$
A_n\to\infty,
$$

one may pass to a subsequence with:

$$
\boxed{
A_{n+1}
\ge
A_n.
}
\tag{6.1}
$$

Let:

$$
a_n
=
A_n^{1/2}.
$$

Then:

$$
\boxed{
\mu_n
=
a_{n+1}/a_n
\ge1.
}
\tag{6.2}
$$

This monotonicity is a selection convention.

It does not assume Type-II growth is monotone on all original scales.

---

# 7. Atom-free exponent window

The raw physical core energy is:

$$
\beta_n
=
r_na_n^2.
$$

Then:

$$
\boxed{
\frac{
\beta_{n+1}
}{
\beta_n
}
=
\lambda_n\mu_n^2.
}
\tag{7.1}
$$

In the recurrent limit:

$$
c_\ast
=
\lambda_\ast^\alpha
=
\lambda_\ast/\mu_\ast.
$$

Hence:

$$
\boxed{
\mu_\ast
=
\lambda_\ast^{1-\alpha}.
}
\tag{7.2}
$$

Since:

$$
0<\lambda_\ast<1
$$

and:

$$
\mu_\ast\ge1,
$$

$$
\boxed{
\alpha\ge1.
}
\tag{7.3}
$$

Also:

$$
\boxed{
q_\ast
=
\lim
\frac{
\beta_{n+1}
}{
\beta_n
}
=
\lambda_\ast^{3-2\alpha}.
}
\tag{7.4}
$$

If:

$$
\beta_n\to0
$$

and:

$$
q_\ast
$$

exists, then:

$$
q_\ast\le1.
$$

Since:

$$
\lambda_\ast<1,
$$

$$
\boxed{
3-2\alpha
\ge0.
}
\tag{7.5}
$$

Therefore:

$$
\boxed{
1
\le
\alpha
\le
3/2.
}
\tag{7.6}
$$

The Euler spatial similarity exponent:

$$
\gamma
=
1/(1+\alpha)
$$

satisfies:

$$
\boxed{
2/5
\le
\gamma
\le
1/2.
}
\tag{7.7}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. Strict geometric window

If:

$$
\mu_\ast>1,
$$

then:

$$
\alpha>1.
$$

If:

$$
q_\ast<1,
$$

then:

$$
\alpha<3/2.
$$

Hence the strict geometric branch lies in:

$$
\boxed{
1<\alpha<3/2,
}
\tag{8.1}
$$

or:

$$
\boxed{
2/5<\gamma<1/2.
}
\tag{8.2}
$$

The two endpoints correspond to marginal ratios:

### parabolic endpoint

$$
\alpha=1,
\qquad
\gamma=1/2,
$$

with asymptotically neutral amplitude ratio:

$$
\mu_\ast=1.
$$

### energy endpoint

$$
\alpha=3/2,
\qquad
\gamma=2/5,
$$

with asymptotically neutral raw-energy ratio:

$$
q_\ast=1.
$$

They require separate slow-drift analysis.

---

# 9. Global normalized energy

The global energy of the Type-II profile is:

$$
\begin{aligned}
\|v_n(\tau)\|_2^2
&=
\int
\left|
\frac{r_n}{a_n}
U(
x_n+r_ny,t
)
\right|^2dy
\\
&=
\frac1{
r_na_n^2
}
\|U(t)\|_2^2.
\end{aligned}
$$

Thus:

$$
\boxed{
\|v_n\|_2^2
=
\frac{
E_{\rm phys}(t)
}{
\beta_n
}.
}
\tag{9.1}
$$

If:

$$
\beta_n\to0
$$

and the parent has positive remaining kinetic energy, then:

$$
\boxed{
\|v_n\|_2^2
\to\infty.
}
\tag{9.2}
$$

Thus the atom-free Type-II Euler profile cannot be globally compact in energy.

---

# 10. Global-energy probability measure

Define:

$$
\boxed{
d\pi_n(y)
=
\frac{
|v_n(y,0)|^2dy
}{
\|v_n(0)\|_2^2
}.
}
\tag{10.1}
$$

This is a probability measure.

For fixed:

$$
R,
$$

$$
\begin{aligned}
\pi_n(B_R)
&=
\frac{
\int_{B_R}|v_n|^2dy
}{
\|v_n\|_2^2
}
\\
&=
\frac{
\int_{
B_{Rr_n}(x_n)
}
|U(x,t_n)|^2dx
}{
\|U(t_n)\|_2^2
}.
\end{aligned}
$$

Therefore:

$$
\boxed{
\pi_n(B_R)
=
\frac{
\mu_{t_n}
(
B_{Rr_n}(x_n)
)
}{
E_{\rm phys}(t_n)
}.
}
\tag{10.2}
$$

---

# 11. NEW THEOREM — Mandatory Global-Energy Tail Escape

## Theorem 11.1

Assume:

$$
t_n\uparrow T,
$$

$$
x_n\to x_\ast,
$$

$$
r_n\to0,
$$

and:

$$
|U(t)|^2dx
\stackrel{\ast}{\rightharpoonup}
\mu_\ast.
$$

Assume:

$$
\boxed{
\mu_\ast(\{x_\ast\})=0.
}
\tag{11.1}
$$

Assume also the total kinetic energy at:

$$
t_n
$$

has a positive lower bound:

$$
\boxed{
E_{\rm phys}(t_n)
\ge
E_0>0.
}
\tag{11.2}
$$

Then for every fixed:

$$
R<\infty,
$$

$$
\boxed{
\pi_n(B_R)\to0.
}
\tag{11.3}
$$

Consequently:

$$
\boxed{
\pi_n
\stackrel{\ast}{\rightharpoonup}
\delta_{\infty_x}
}
\tag{11.4}
$$

on the one-point compactification of normalized physical space.

### Proof

Fix:

$$
R.
$$

Then:

$$
Rr_n\to0
$$

and:

$$
x_n\to x_\ast.
$$

For every:

$$
\varepsilon>0,
$$

for all sufficiently large:

$$
n,
$$

$$
B_{Rr_n}(x_n)
\subset
B_\varepsilon(x_\ast).
$$

Thus:

$$
\limsup_n
\mu_{t_n}
(
B_{Rr_n}(x_n)
)
\le
\mu_\ast(
\overline B_\varepsilon(x_\ast)
).
$$

Let:

$$
\varepsilon\downarrow0.
$$

Since:

$$
\mu_\ast(\{x_\ast\})=0,
$$

the right side tends to zero.

Divide by:

$$
E_{\rm phys}(t_n)\ge E_0.
$$

Hence:

$$
\pi_n(B_R)\to0.
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

# 12. Correction to the DCRP-29 no-escape phrase

DCRP-29 listed a strongest defect-free branch with:

$$
\text{"no spatial escape"}.
$$

This must be refined.

For:

$$
\beta_n\to0
$$

and an atom-free terminal energy measure, Theorem 11.1 shows:

$$
\boxed{
\textbf{
the normalized global energy must escape to spatial infinity.
}
}
$$

Therefore the admissible zero-defect statement is only:

$$
\boxed{
\textbf{
no additional escape of the selected local obstruction carrier
beyond the mandatory global-energy tail}.
}
}
\tag{12.1}
$$

The global tail is part of the Type-II normal form.

It cannot be taxed merely for existing.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 13. Finite-energy DSS rigidity

Suppose:

$$
v
$$

is a DSS Euler solution:

$$
v(y,\tau)
=
\lambda^\alpha
v(
\lambda y,
\lambda^{\alpha+1}\tau
).
$$

Assume:

$$
0<
\|v(\tau)\|_2^2
<
\infty
$$

and exact Euler energy conservation.

Then:

$$
\begin{aligned}
\|v(\tau)\|_2^2
&=
\lambda^{2\alpha-3}
\|
v(
\lambda^{\alpha+1}\tau
)
\|_2^2
\\
&=
\lambda^{2\alpha-3}
\|v(\tau)\|_2^2.
\end{aligned}
$$

Thus:

$$
\boxed{
\lambda^{2\alpha-3}=1.
}
\tag{13.1}
$$

Because:

$$
\lambda\neq1,
$$

$$
\boxed{
\alpha=3/2.
}
\tag{13.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Consequence for strict atom-free recurrence

In the strict atom-free geometric regime:

$$
q_\ast<1,
$$

one has:

$$
\alpha<3/2.
$$

By Theorem 13.1:

$$
\boxed{
\textbf{
the nonzero DSS Euler profile cannot have finite global kinetic energy}.
}
\tag{14.1}
$$

Thus compactly supported steady Euler solutions are not members of the strict same-parent Type-II DSS class.

They remain a warning against generic ancient-Euler Liouville statements, but they do not model the final strict DSS survivor.

---

# 15. Record-scale Morrey envelope

A useful refinement is to choose:

$$
r_n
$$

as approximate record scales for:

$$
A(r).
$$

Assume:

$$
\boxed{
A(Rr_n)
\le
C_{\rm rec}
A(r_n)
}
\tag{15.1}
$$

for every fixed:

$$
R\ge1
$$

and all sufficiently large:

$$
n.
$$

At the selected Type-II time:

$$
\begin{aligned}
\int_{B_R}
|v_n(y,0)|^2dy
&=
\frac1{
A(r_n)
}
r_n^{-1}
\int_{B_{Rr_n}}
|U(x,t_n)|^2dx
\\
&\le
R
\frac{
A(Rr_n)
}{
A(r_n)
}.
\end{aligned}
$$

Hence:

$$
\boxed{
\int_{B_R}
|v_n(y,0)|^2dy
\le
C_{\rm rec}R.
}
\tag{15.2}
$$

Any strong local profile inherits:

$$
\boxed{
\int_{B_R}
|v(y,0)|^2dy
\le
C_{\rm rec}R
}
\tag{15.3}
$$

for every fixed:

$$
R.
$$

Status:

$$
\boxed{
\textbf{PROVED under record-scale selection}.
}
$$

This is a critical Morrey-type tail upper bound.

---

# 16. Intersection with Xue's DSS energy law

For:

$$
N=3,
$$

Xue proves under global regularity/integrability hypotheses that a nontrivial DSS profile in:

$$
3/p<\alpha<3/2
$$

has:

$$
\boxed{
\int_0^{S_0}
\int_{|y|\le L}
|V(y,s)|^2dyds
\sim
L^{3-2\alpha}.
}
\tag{16.1}
$$

For the strict Type-II exponent window:

$$
1<\alpha<3/2,
$$

$$
\boxed{
0<3-2\alpha<1.
}
\tag{16.2}
$$

Thus the expected admissible DSS tail is:

$$
\boxed{
\textbf{
divergent but sublinear in radius}.
}
\tag{16.3}
$$

This is compatible with the project-internal record-scale Morrey upper bound:

$$
O(R).
$$

It is not a contradiction.

It is a tail normal form.

---

# 17. Known DSS decay/integrability exclusions

Chae--Tsai prove several nonexistence criteria for Euler DSS solutions.

Among them, nontriviality is excluded under suitable:

- velocity integrability;
- vorticity integrability;
- spatial decay of velocity/gradient/vorticity.

Chae's maximum-principle theorem similarly removes DSS profiles with:

$$
|\nabla V(y,s)|\to0
$$

and sufficiently fast vorticity decay.

Therefore the final Type-II DSS survivor cannot belong to these decaying/integrable subclasses unless it is trivial or spatially rigid.

This is external partial rigidity, not a complete exclusion.

---

# 18. Chae--Wolf energy-endpoint exclusion

Chae--Wolf prove that for:

$$
\boxed{
\alpha\ge3/2,
}
\tag{18.1}
$$

a DSS Euler profile with sublinear growth at spatial infinity must be spatially constant.

Thus the energy-conserving endpoint:

$$
\alpha=3/2
$$

is strongly constrained if the profile is sublinear pointwise.

DCRP-30 does not claim that the record-scale Morrey bound alone implies their pointwise sublinear hypothesis.

Therefore this theorem is an external conditional pruning of the marginal endpoint.

---

# 19. Constantin--Ignatova--Vicol outgoing guardrail

For smooth globally self-similar 3D Euler profiles satisfying the local outgoing property, Constantin--Ignatova--Vicol prove:

$$
\boxed{
\gamma\ge1/2.
}
\tag{19.1}
$$

In terms of:

$$
\alpha,
$$

this is:

$$
\boxed{
\alpha\le1.
}
\tag{19.2}
$$

Therefore every strict interior Type-II DSS recurrence:

$$
\boxed{
1<\alpha<3/2
}
\tag{19.3}
$$

must violate the outgoing property.

Equivalently, its self-similar Lagrangian dynamics must contain a non-outgoing/trapped component.

Status:

$$
\boxed{
\textbf{EXTERNAL CONDITIONAL RIGIDITY}.
}
$$

This is a major geometric restriction.

---

# 20. New strongest DSS survivor

Combining Sections 7--19, the compact nondegenerate same-parent Type-II branch is reduced to the following.

### exponent

$$
\boxed{
1
\le
\alpha
\le
3/2,
}
$$

or:

$$
\boxed{
2/5
\le
\gamma
\le
1/2.
}
$$

### strict interior

For geometric amplitude growth and raw-energy decay:

$$
\boxed{
1<\alpha<3/2.
}
$$

### global energy

The strict interior profile has:

$$
\boxed{
\|v\|_2=\infty.
}
$$

### normalized total-energy shape

The parent energy probability escapes to:

$$
\boxed{
\infty_x.
}
$$

### local tail

Under record selection:

$$
\boxed{
\int_{B_R}|v|^2
\lesssim R.
}
$$

Under Xue-type global integrability:

$$
\boxed{
\int_{0}^{S_0}
\int_{B_R}
|V|^2
\sim
R^{3-2\alpha}.
}
$$

### Lagrangian geometry

For:

$$
\alpha>1,
$$

the profile cannot satisfy Constantin's outgoing condition.

Thus it must contain a trapped/non-outgoing self-similar material component.

### decay classes

It must avoid the existing Chae/Chae--Tsai DSS decay/integrability Liouville classes.

Therefore:

$$
\boxed{
\textbf{
final compact Type-II strong state}
=
\textbf{
tail-fed, non-outgoing, infinite-energy critical DSS Euler recurrence}.
}
}
\tag{20.1}
$$

---

# 21. Why this is not merely another name for the original Euler problem

A generic ancient Euler flow may be:

- steady;
- compactly supported;
- finite energy;
- arbitrary in similarity exponent because no similarity is assumed.

The DCRP-30 survivor must instead satisfy:

- same-parent discrete scaling recurrence;
-:

  $$
  1\le\alpha\le3/2;
  $$

- raw physical core energy:

  $$
  \beta_n\to0;
  $$

- global normalized-energy escape to:

  $$
  \infty_x;
  $$

- critical local Morrey growth;
- no finite Euler-time crossing carrier;
- no NS viscous residue;
- no Reynolds/trace concentration defect;
- non-outgoing/trapped similarity dynamics in the strict interior window.

This is a much narrower Euler class.

---

# 22. Marginal alpha = 1 branch

If:

$$
\alpha=1,
$$

then:

$$
\gamma=1/2.
$$

Also:

$$
\mu_\ast=1.
$$

Thus the amplitude may still diverge, but only through slow non-geometric drift:

$$
a_{n+1}/a_n\to1.
$$

This is the parabolic-endpoint branch.

It is not eliminated by the strict outgoing guardrail because:

$$
\gamma=1/2
$$

is allowed.

A refined transition-rate theorem is required.

---

# 23. Marginal alpha = 3/2 branch

If:

$$
\alpha=3/2,
$$

then:

$$
\gamma=2/5,
$$

and:

$$
q_\ast=1.
$$

Thus raw energy can tend to zero only through slow non-geometric drift.

This is the energy-endpoint branch.

Chae--Wolf exclude this DSS endpoint under sublinear pointwise profile growth.

Without that growth condition, the branch remains a marginal possibility in the present project.

---

# 24. Degenerate transition ratios

If the same-parent ratios fail the nondegenerate assumptions:

$$
\lambda_n
\to0,
$$

or:

$$
\mu_n
\to\infty,
$$

or the center/time shifts escape, then no single finite DSS exponent is obtained.

This is not ignored.

The branch enters:

$$
\boxed{
\text{scale/amplitude/center/time transition escape}.
}
\tag{24.1}
$$

Thus:

$$
\boxed{
\textbf{
Type-II recurrence}
\Longrightarrow
\textbf{
DSS state}
\ \vee\
\textbf{
explicit transition noncompactness}.
}
\tag{24.2}
$$

---

# 25. Tail pressure becomes the next natural object

The atom-free DSS profile has infinite global normalized kinetic energy.

Therefore the Euler pressure cannot be treated as if it were generated by a compactly supported finite-energy state.

The correct pressure decomposition must distinguish:

- active/local pressure generated near the Type-II core;
- far-field/tail pressure generated by the required infinite DSS tail;
- removable harmonic/affine pressure jets.

This mirrors the earlier MORP/DCRP pressure-tail architecture.

The natural next question is:

> can the required DSS tail remain dynamically invisible to every material pressure-work / transition detector on the core?

This is now the direct bridge back from the Euler state to the native Navier--Stokes package.

---

# 26. Candidate tail-pressure rigidity target

Let:

$$
V
$$

be the similarity profile of the strict atom-free DSS branch.

Suppose its energy tail obeys:

$$
\int_{B_R}|V|^2
\lesssim R,
$$

and in an admissible regularity class:

$$
\int_0^{S_0}
\int_{B_R}|V|^2
\sim
R^{3-2\alpha}.
$$

Decompose pressure:

$$
\boxed{
P
=
P_{\rm near}
+
P_{\rm tail}
+
P_{\rm harm}.
}
\tag{26.1}
$$

A useful next theorem would prove:

$$
\boxed{
\text{nontrivial tail-fed DSS}
\Longrightarrow
\text{nonzero material tail-pressure work}
\ \vee\
\text{tail spatial/scale transition defect}
\ \vee\
\text{known DSS Liouville class}.
}
\tag{26.2}
$$

If the tail pressure work vanishes on every recurrent material core, then a rigidity theorem should force the tail into a pressure-compatible/harmonic mode, after which the earlier affine/Morrey mechanisms can be reused.

This is the current preferred route.

---

# 27. Relationship to the Seregin Type-II class

Seregin's 2026 theorem extracts nontrivial ancient Euler objects under selected Type-II assumptions and retains a local energy inequality.

DCRP-30 adds a different layer:

if the project-specific same-parent return and transition compactness assumptions hold, the ancient object is forced into generalized DSS or an explicit transition-escape branch.

Thus the DCRP normal form is a **subclass** of general ancient Type-II Euler profiles, conditional on recurrence/transition compactness.

No claim is made that every Seregin Type-II scenario is DSS.

---

# 28. Relationship to Constantin's exponent guardrails

Constantin--Ignatova--Vicol prove:

- finite kinetic energy self-similar Euler blowup requires:

  $$
  \gamma\ge2/5;
  $$

- outgoing smooth global self-similar profiles require:

  $$
  \gamma\ge1/2.
  $$

The DCRP same-parent atom-free kinematics independently yield:

$$
2/5
\le
\gamma
\le
1/2.
$$

Thus the project has landed precisely in the known unresolved similarity window.

The strict branch:

$$
2/5<\gamma<1/2
$$

must be:

- infinite global normalized energy;
- non-outgoing.

This agreement is a calibration of the reduction, not a proof of regularity.

---

# 29. Updated Type-II branch tree

The kinetic Type-II branch is now:

$$
\boxed{
A_n\to\infty.
}
$$

First split:

$$
\boxed{
\beta_\ast>0
\Longrightarrow
\text{endpoint atom},
}
$$

or:

$$
\boxed{
\beta_\ast=0.
}
$$

For:

$$
\beta_\ast=0,
$$

time split:

$$
\boxed{
T_n\to0
\vee
T_n\to T_\ast
\vee
T_n\to\infty.
}
$$

The first two are already assigned to temporal/material-transition carriers.

For:

$$
T_n\to\infty,
$$

same-parent transition split:

$$
\boxed{
\text{transition parameter escape}
\ \vee\
\text{Euler DSS recurrence}.
}
$$

For compact strict DSS recurrence:

$$
\boxed{
2/5<\gamma<1/2,
}
$$

and the state is:

$$
\boxed{
\text{tail-fed}
+
\text{infinite-energy}
+
\text{non-outgoing}.
}
$$

No generic ancient Euler branch remains in the compact same-parent sector.

---

# 30. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Critical-Tail DSS Euler /
Same-Parent Tail-Pressure Rigidity Lemma}.
}
$$

A useful theorem would show that a tail-fed DSS profile in:

$$
2/5<\gamma<1/2
$$

with:

- critical Morrey local energy;
- no raw endpoint atom;
- no anomalous NS dissipation;
- no finite-time material crossing;
- no transition-parameter escape;
- no known DSS decay/integrability class;
- trapped/non-outgoing similarity dynamics;

must produce:

$$
\boxed{
\text{nonzero far-tail pressure work}
}
$$

or:

$$
\boxed{
\text{nonzero spatial/scale return carrier}.
}
$$

If both vanish, one would seek a tail-pressure/harmonic rigidity theorem reducing the profile to a removable or already-excluded mode.

This is now the narrowest Type-II state frontier obtained in the DCRP chain.

---

# 31. Source-status audit

## Chae--Tsai / Chae

Known Euler DSS Liouville criteria exclude profiles under selected velocity/vorticity decay and integrability assumptions.

The maximum-principle result shows that sufficient decay at spatial infinity forces the DSS profile to be spatially constant.

These are conditional subbranch exclusions.

## Xue

For DSS Euler profiles satisfying the paper's global regularity/integrability assumptions, the local energy inequality yields sharp energy-growth laws.

In dimension three and:

$$
\alpha<3/2,
$$

nontrivial profiles in the relevant integrable class carry:

$$
R^{3-2\alpha}
$$

energy growth.

This is used as an external tail calibration.

## Chae--Wolf 2023

The paper excludes nontrivial:

$$
(\alpha,\lambda)
$$

DSS Euler blowup for:

$$
\alpha\ge3/2
$$

under sublinear profile growth.

This constrains the upper endpoint of the DCRP exponent window.

## Constantin--Ignatova--Vicol 2026

Finite physical energy requires:

$$
\gamma\ge2/5
$$

for putative self-similar Euler blowup.

A smooth globally self-similar profile with the local outgoing property must satisfy:

$$
\gamma\ge1/2.
$$

The DCRP strict atom-free recurrence lies between these two exponents and therefore must be non-outgoing.

## Seregin 2026

Selected Type-II Navier--Stokes scenarios produce nontrivial ancient Euler objects.

DCRP-30 further obtains DSS only under the additional project-specific same-parent recurrence / transition-compactness hypothesis.

---

# 32. End state

The exact same-parent transition law is:

$$
\boxed{
v_{n+1}(y,\tau)
=
c_n
v_n
\left(
b_n+\lambda_n y,
d_n+c_n\lambda_n\tau
\right).
}
$$

On a nondegenerate compact recurrent branch:

$$
\boxed{
v(y,\tau)
=
\lambda^\alpha
v
\left(
\lambda y,
\lambda^{\alpha+1}\tau
\right).
}
$$

Raw-energy vanishing and record-amplitude selection force:

$$
\boxed{
1\le\alpha\le3/2,
}
$$

or:

$$
\boxed{
2/5\le\gamma\le1/2.
}
$$

The strict geometric branch lies in:

$$
\boxed{
2/5<\gamma<1/2.
}
$$

Atom-free Type-II also forces the normalized **global** kinetic-energy probability to escape to:

$$
\boxed{
\infty_x.
}
$$

The strict DSS profile cannot have finite global kinetic energy.

Known Euler results then force it outside several decay/integrability/outgoing classes.

Thus the final compact same-parent Type-II state is:

$$
\boxed{
\textbf{
tail-fed, non-outgoing, infinite-energy critical DSS Euler recurrence}.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Critical-Tail DSS Euler /
Same-Parent Tail-Pressure Rigidity.
}
}
$$