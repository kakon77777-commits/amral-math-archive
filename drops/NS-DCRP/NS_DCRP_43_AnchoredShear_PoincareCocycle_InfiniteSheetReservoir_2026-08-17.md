# NS-DCRP-43 — Gauge-Completed Anchored Shear, Poincaré Amplification, Finite Residence, and Infinite-Sheet Reservoir Rigidity

- date: 2026-08-17
- status: research proof checkpoint / scalar-turnover gauge completion
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit the gauge dependence of the DCRP-42 planar shear scalar;
  2. replace absolute scalar amplitude by an anchor-relative, gauge-completed shear potential;
  3. define the exact residual measuring failure of the canonical pancake scalar eigenmode;
  4. derive the one-period affine Poincaré cocycle;
  5. prove finite residence / no recurrent nonzero material-label theorems on the pure cocycle branch;
  6. prove a global superlevel-set functional equation;
  7. show that every nonzero global pure-cocycle mode requires infinite-measure scalar superlevel reservoirs;
  8. strengthen the previous conditional $L^p$ Liouville statement to an $L^\infty$/weak-$L^p$/finite-superlevel no-go on the global pure branch;
  9. identify the remaining physical problem as conversion of the gauge-completed scalar reservoir into a gauge-invariant vorticity/sheet carrier.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - D. S. Agafontsev, E. A. Kuznetsov, A. A. Mailybaev, *Asymptotic solution for high vorticity regions in incompressible 3D Euler equations*, arXiv:1609.07782;
  - A. Enciso, A. J. Fernández, D. Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233.
- internal dependencies:
  - DCRP-40 planar potential--shear representation;
  - DCRP-41 moving pancake jet;
  - DCRP-42 planar shear scalar reduction and turnover identity.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction

DCRP-42 introduced

$$
\boxed{
q
=
w-\partial_z\phi,
}
\tag{1.1}
$$

where

$$
V_h=\nabla_h\phi,
$$

and proved

$$
\boxed{
\Omega_h
=
J\nabla_hq.
}
\tag{1.2}
$$

However

$$
\phi
$$

is determined only up to

$$
\boxed{
\phi
\mapsto
\phi+C(z,s).
}
\tag{1.3}
$$

Therefore

$$
\boxed{
q
\mapsto
q-\partial_zC(z,s).
}
\tag{1.4}
$$

The horizontal differential

$$
\boxed{
d_hq
}
\tag{1.5}
$$

and hence

$$
\Omega_h
$$

are invariant.

The absolute value of

$$
q
$$

is not.

Consequently the DCRP-42 statements involving

$$
|q|^p
$$

or

$$
|r|^p
$$

must be interpreted as **gauge-fixed scalar statements**, not as fully coordinate-free physical taxes unless a gauge completion is declared.

Status:

$$
\boxed{
\textbf{CORRECTION / QUOTIENT-SAFETY AUDIT OF DCRP-42}.
}
$$

DCRP-43 supplies such a completion.

---

# 2. Anchor-relative shear potential

Let the normalized recurrent center be fixed once and for all.

In the fixed-plane chart write

$$
y=(x_h,z),
$$

and choose a fixed horizontal anchor point

$$
\boxed{
x_{\star,h}.
}
\tag{2.1}
$$

For every

$$
z,s,
$$

define the anchor-relative shear potential

$$
\boxed{
\widetilde q(x_h,z,s)
=
q(x_h,z,s)
-
q(x_{\star,h},z,s).
}
\tag{2.2}
$$

Under the full slice gauge transformation

$$
q\mapsto q-h(z,s),
$$

both terms shift by the same amount.

Therefore

$$
\boxed{
\widetilde q
\ \text{is gauge invariant for the declared anchor}.
}
\tag{2.3}
$$

Also

$$
\boxed{
\nabla_h\widetilde q
=
\nabla_hq,
}
\tag{2.4}
$$

so

$$
\boxed{
\Omega_h
=
J\nabla_h\widetilde q.
}
\tag{2.5}
$$

Thus

$$
\widetilde q
$$

is a gauge-completed relative potential whose horizontal differential is the physical planar vorticity.

---

# 3. Periodicity of the anchored scalar

If the DSS state is periodic:

$$
V(y,s+S_0)=V(y,s),
$$

then

$$
\Omega_h(y,s+S_0)
=
\Omega_h(y,s).
$$

The anchor-relative primitive is uniquely fixed by:

$$
\widetilde q(x_{\star,h},z,s)=0.
$$

Therefore

$$
\boxed{
\widetilde q(y,s+S_0)
=
\widetilde q(y,s)
}
\tag{3.1}
$$

on every recurrent fixed-plane chart.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. Periodic renormalization factor

DCRP-42 defines

$$
\boxed{
k(s)
=
1-\gamma-2a(s),
}
\tag{4.1}
$$

with

$$
\boxed{
\bar k
=
2\gamma-1.
}
\tag{4.2}
$$

Define

$$
\boxed{
\eta(s)
=
\exp
\left[
\int_0^s
(k(\tau)-\bar k)d\tau
\right].
}
\tag{4.3}
$$

Then

$$
\boxed{
\eta(s+S_0)=\eta(s).
}
\tag{4.4}
$$

Set the anchored renormalized shear scalar

$$
\boxed{
\widetilde r
=
\eta(s)
\widetilde q.
}
\tag{4.5}
$$

Then

$$
\boxed{
\widetilde r(y,s+S_0)
=
\widetilde r(y,s).
}
\tag{4.6}
$$

---

# 5. Gauge-completed pancake residual

Set

$$
\boxed{
\lambda_\gamma
=
1-2\gamma
>
0.
}
\tag{5.1}
$$

Define the **anchored shear residual**

$$
\boxed{
\mathcal R_{\rm sh}
=
D_s\widetilde r
-
\lambda_\gamma
\widetilde r.
}
\tag{5.2}
$$

This is defined entirely from:

- the physical velocity/vorticity field;
- the fixed rank-two chart;
- the declared recurrent center/anchor;
- the DCRP-41 affine pancake coefficient.

It is invariant under the discarded slice gauge

$$
q\mapsto q-h(z,s).
$$

Thus it is the correct quotient-completed replacement for the unanchored DCRP-42 scalar eigenmode.

The rank-two scalar branch is:

$$
\boxed{
\mathcal R_{\rm sh}\neq0
}
$$

or

$$
\boxed{
\mathcal R_{\rm sh}=0.
}
\tag{5.3}
$$

The second is the **pure anchored pancake cocycle branch**.

---

# 6. Relation to the DCRP-42 gauge equation

DCRP-42 showed that, after a suitable primitive normalization and on the canonical fixed-plane normal-shear branch,

$$
D_sq+k(s)q=0.
$$

Transforming to the anchor-relative scalar need not preserve this homogeneous equation.

The anchor subtraction introduces an actual relative-source term.

Thus:

$$
\boxed{
\textbf{
DCRP-42 pure scalar eigenmode}
}
$$

is a convenient potential gauge representation, while

$$
\boxed{
\mathcal R_{\rm sh}=0
}
$$

is the stronger gauge-completed equality branch.

If:

$$
\mathcal R_{\rm sh}\neq0,
$$

the mismatch is retained as a native chart/source residual.

Status:

$$
\boxed{
\textbf{CORRECTED LOGICAL ROLE}.
}
$$

---

# 7. Similarity material flow

Let

$$
\boxed{
\partial_sY(a,s)
=
W(Y(a,s),s),
\qquad
W=\gamma y+V.
}
\tag{7.1}
$$

Define the one-period Poincaré map

$$
\boxed{
\Phi(a)
=
Y(a,S_0).
}
\tag{7.2}
$$

Since

$$
\nabla\cdot V=0,
$$

$$
\boxed{
\nabla\cdot W
=
3\gamma.
}
\tag{7.3}
$$

Hence

$$
\boxed{
\det D\Phi
=
J_\Phi
=
e^{3\gamma S_0}
>
1.
}
\tag{7.4}
$$

---

# 8. General affine one-period cocycle

Along a material trajectory,

$$
\boxed{
\frac d{ds}
\widetilde r(Y(a,s),s)
=
\lambda_\gamma
\widetilde r(Y(a,s),s)
+
\mathcal R_{\rm sh}(Y(a,s),s).
}
\tag{8.1}
$$

Variation of constants gives

$$
\boxed{
\widetilde r(\Phi(a),0)
=
\mu_r
\widetilde r(a,0)
+
\mathcal Z(a),
}
\tag{8.2}
$$

where

$$
\boxed{
\mu_r
=
e^{\lambda_\gamma S_0}
=
e^{(1-2\gamma)S_0}
>
1,
}
\tag{8.3}
$$

and

$$
\boxed{
\mathcal Z(a)
=
\int_0^{S_0}
e^{\lambda_\gamma(S_0-\tau)}
\mathcal R_{\rm sh}
(
Y(a,\tau),\tau
)
d\tau.
}
\tag{8.4}
$$

The periodicity of

$$
\widetilde r
$$

has been used at the endpoint.

This is the exact **anchored shear Poincaré cocycle**.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. Source-versus-pure cocycle dichotomy

The one-period return therefore contains:

### additive source branch

$$
\boxed{
\mathcal Z\neq0
}
\tag{9.1}
$$

generated by the anchored shear residual.

### pure multiplicative branch

$$
\boxed{
\mathcal R_{\rm sh}=0
}
\tag{9.2}
$$

and hence

$$
\boxed{
\widetilde r(\Phi(a),0)
=
\mu_r\widetilde r(a,0).
}
\tag{9.3}
$$

Only the second branch is used in the strong residence/superlevel theorems below.

---

# 10. Iterated pure cocycle

Assume

$$
\mathcal R_{\rm sh}=0
$$

on the full material tube of interest.

Then for every integer

$$
m\ge0,
$$

$$
\boxed{
\widetilde r(\Phi^m(a),0)
=
\mu_r^m
\widetilde r(a,0).
}
\tag{10.1}
$$

Thus the same nonzero material label amplifies geometrically under every DSS return.

---

# 11. NEW THEOREM — No Nonzero Recurrent Material Shear Label

## Theorem 11.1

Let

$$
K\Subset\mathbb R^3
$$

be compact and suppose the pure anchored pancake cocycle holds for all iterates of a material point that enter

$$
K.
$$

If

$$
\widetilde r(a,0)\neq0,
$$

then the forward orbit

$$
\{\Phi^m(a)\}_{m\ge0}
$$

can enter

$$
K
$$

only finitely many times.

### Proof

Let

$$
M_K
=
\sup_K
|\widetilde r(\cdot,0)|
<
\infty.
$$

Whenever

$$
\Phi^m(a)\in K,
$$

(10.1) gives

$$
\mu_r^m
|\widetilde r(a,0)|
\le
M_K.
$$

Since

$$
\mu_r>1,
$$

this can hold for only finitely many

$$
m.
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

# 12. Quantitative finite-return bound

If

$$
|\widetilde r(a,0)|
\ge
\delta>0,
$$

then every return index

$$
m
$$

with

$$
\Phi^m(a)\in K
$$

satisfies

$$
\boxed{
m
\le
\frac{
\log(M_K/\delta)
}{
\log\mu_r
}.
}
\tag{12.1}
$$

Thus for every fixed nonzero amplitude threshold there is a uniform maximal number of DSS returns to a bounded core.

This is a **finite residence / finite recurrence theorem**.

---

# 13. Periodic material points

If

$$
\Phi^m(a)=a
$$

for some

$$
m\ge1,
$$

then

$$
\widetilde r(a)
=
\mu_r^m
\widetilde r(a).
$$

Since

$$
\mu_r>1,
$$

$$
\boxed{
\widetilde r(a)=0.
}
\tag{13.1}
$$

Hence every periodic material point of the pure pancake cocycle lies on the anchored zero-shear set.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Recurrent material points

More generally, suppose

$$
\Phi^{m_j}(a)
$$

has a convergent subsequence in a compact region on which

$$
\widetilde r
$$

is continuous.

If

$$
m_j\to\infty,
$$

then boundedness of

$$
\widetilde r(\Phi^{m_j}(a))
$$

combined with

$$
\mu_r^{m_j}
|\widetilde r(a)|
$$

forces

$$
\boxed{
\widetilde r(a)=0.
}
\tag{14.1}
$$

Thus the nonzero anchored shear labels lie only on nonrecurrent material trajectories.

---

# 15. Material interpretation

The periodic Eulerian pancake pattern may return every

$$
S_0.
$$

The material labels carrying nonzero

$$
\widetilde r
$$

cannot.

Therefore the exact pure cocycle branch has:

$$
\boxed{
\textbf{
Eulerian recurrence}
+
\textbf{
material transience}.
}
\tag{15.1}
$$

The same shear-carrying material cannot populate a fixed recurrent core indefinitely.

The core must be repopulated by continually different material labels.

This is stronger than the period-averaged outward flux statement of DCRP-42.

---

# 16. Global pure pancake branch

Assume now that:

1. the fixed-plane anchored shear representation exists globally on:

   $$
   \mathbb R^3;
   $$

2.:

   $$
   \mathcal R_{\rm sh}=0
   $$

   globally;

3.:

   $$
   \Phi
   $$

   is the global smooth one-period similarity flow diffeomorphism.

Set

$$
\boxed{
r_0(y)
=
\widetilde r(y,0).
}
\tag{16.1}
$$

For

$$
\tau>0,
$$

define the superlevel set

$$
\boxed{
E_\tau
=
\left\{
y:
|r_0(y)|>\tau
\right\}.
}
\tag{16.2}
$$

---

# 17. NEW THEOREM — Exact Superlevel Renormalization

## Theorem 17.1

For every

$$
\tau>0,
$$

$$
\boxed{
\Phi(E_\tau)
=
E_{\mu_r\tau}.
}
\tag{17.1}
$$

### Proof

For

$$
x=\Phi(a),
$$

the pure cocycle gives

$$
|r_0(x)|
=
\mu_r
|r_0(a)|.
$$

Thus

$$
|r_0(a)|>\tau
$$

if and only if

$$
|r_0(x)|>\mu_r\tau.
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

# 18. Distribution-function equation

Because

$$
\det D\Phi=J_\Phi,
$$

Theorem 17.1 gives, whenever the measure is finite,

$$
\boxed{
|E_{\mu_r\tau}|
=
J_\Phi
|E_\tau|.
}
\tag{18.1}
$$

But

$$
\mu_r>1
$$

implies

$$
\boxed{
E_{\mu_r\tau}
\subset
E_\tau.
}
\tag{18.2}
$$

Since

$$
J_\Phi>1,
$$

finite positive measure is impossible.

---

# 19. NEW THEOREM — Finite-Superlevel No-Go

## Theorem 19.1

On the global pure anchored pancake branch, for every

$$
\tau>0,
$$

$$
\boxed{
|E_\tau|
\in
\{0,\infty\}.
}
\tag{19.1}
$$

### Proof

If

$$
0<|E_\tau|<\infty,
$$

then

$$
|E_{\mu_r\tau}|
=
J_\Phi|E_\tau|
>
|E_\tau|,
$$

contradicting

$$
E_{\mu_r\tau}\subset E_\tau.
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

# 20. Infinite-sheet reservoir theorem

Assume

$$
r_0
$$

is continuous and nonzero.

Then there exists

$$
y_0
$$

with

$$
|r_0(y_0)|>0.
$$

For every

$$
0<\tau<|r_0(y_0)|,
$$

the set

$$
E_\tau
$$

contains an open neighborhood of

$$
y_0.
$$

Hence

$$
|E_\tau|>0.
$$

By Theorem 19.1,

$$
\boxed{
|E_\tau|=\infty.
}
\tag{20.1}
$$

Thus every nonzero global pure pancake scalar requires an **infinite-measure amplitude reservoir** in normalized space.

This is the strongest new structural conclusion of DCRP-43.

---

# 21. $L^\infty$ Liouville theorem

Assume the global pure branch and:

$$
\boxed{
\widetilde r(\cdot,0)
\in
L^\infty(\mathbb R^3).
}
\tag{21.1}
$$

Pick any point with

$$
\widetilde r(a)\neq0.
$$

Then

$$
|\widetilde r(\Phi^m(a))|
=
\mu_r^m|\widetilde r(a)|
\to\infty,
$$

contradicting boundedness.

Therefore

$$
\boxed{
\widetilde r\equiv0.
}
\tag{21.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 22. Weak-$L^p$ / finite-distribution Liouville theorem

If for some

$$
p>0
$$

$$
\widetilde r
\in
L^{p,\infty}(\mathbb R^3),
$$

then every positive superlevel set has finite measure:

$$
|E_\tau|
\le
C\tau^{-p}.
$$

Theorem 19.1 therefore forces

$$
|E_\tau|=0
$$

for every

$$
\tau>0.
$$

Hence

$$
\boxed{
\widetilde r\equiv0.
}
\tag{22.1}
$$

Thus:

$$
\boxed{
\textbf{
nonzero global pure pancake scalar}
\notin
L^{p,\infty}
\quad
\forall p>0.
}
\tag{22.2}
$$

In particular it is not in any finite

$$
L^p.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This strengthens the conditional global $L^p$ statement of DCRP-42 and removes the separate boundary-flux assumption on the pure global branch.

---

# 23. Decay-at-infinity Liouville theorem

If

$$
\boxed{
\widetilde r(y,0)\to0
\qquad
\text{as }|y|\to\infty,
}
\tag{23.1}
$$

then each positive superlevel set

$$
E_\tau
$$

is bounded and hence finite measure.

Therefore Theorem 19.1 gives

$$
\boxed{
\widetilde r\equiv0.
}
\tag{23.2}
$$

Thus a nonzero global pure pancake scalar cannot decay uniformly at normalized infinity.

---

# 24. Compact support no-go

As a special case:

$$
\boxed{
\operatorname{supp}\widetilde r
\ \text{compact}
}
$$

implies

$$
\boxed{
\widetilde r=0.
}
\tag{24.1}
$$

Therefore an exact global pure pancake eigenmode cannot be localized as a compact scalar sheet in the anchored-potential variable.

---

# 25. Why this is not yet a velocity-energy contradiction

The anchored scalar

$$
\widetilde q
$$

is a relative planar shear potential.

Its horizontal gradient is physical vorticity:

$$
\nabla_h\widetilde q
=
-J\Omega_h.
$$

However the existing strict-DSS kinetic-energy tail bound controls

$$
V,
$$

not directly

$$
\widetilde q.
$$

A broad, slowly varying plateau of

$$
\widetilde q
$$

may have small horizontal gradient while occupying large spatial measure.

Therefore:

$$
\boxed{
\textbf{
infinite scalar superlevel measure}
}
$$

does not automatically contradict the critical kinetic-energy envelope.

The missing bridge is a **sheet-interface / shear-gradient estimate**.

---

# 26. Gauge-invariant physical content

Although

$$
\widetilde q
$$

depends on the declared anchor line, it is invariant under the original slice gauge.

The truly local gauge-free differential is

$$
\boxed{
d_h\widetilde q
=
d_hq
}
$$

and hence

$$
\boxed{
\Omega_h.
}
$$

Therefore the final physical closure must convert the anchored amplitude-reservoir conclusion into one of:

- large vorticity-interface measure;
- rank lifting;
- sheet curvature/folding;
- normal-shear residual;
- material transition.

DCRP-43 does not claim that the scalar amplitude itself is a coordinate-free conserved quantity.

---

# 27. Coarea-facing formulation

For fixed

$$
z,s,
$$

the level-set foliation of

$$
\widetilde q
$$

is independent of the discarded slice gauge.

Formally, the horizontal coarea formula gives

$$
\boxed{
\int
|\nabla_h\widetilde q|
dx_h
=
\int
\mathcal H^1
\left(
\{
\widetilde q=\tau
\}
\right)
d\tau.
}
\tag{27.1}
$$

Since

$$
|\nabla_h\widetilde q|
=
|\Omega_h|,
$$

the boundary geometry of scalar plateaus is directly tied to physical planar vorticity.

This suggests the next bridge:

$$
\boxed{
\textbf{
infinite scalar reservoir}
\Longrightarrow
\textbf{
sheet-interface / vorticity-length requirement}.
}
\tag{27.2}
$$

No quantitative global lower bound is proved in this round.

---

# 28. Material-entry interpretation

For a bounded recurrent core

$$
K,
$$

a nonzero anchored label can return only finitely many times.

Yet the Eulerian anchored scalar field is periodic.

Therefore the same high-amplitude Eulerian region must be populated by different material labels on later periods.

Thus the pure pancake branch has a genuine label-exchange mechanism:

$$
\boxed{
\textbf{
new low-amplitude labels enter}
\to
\textbf{
material amplification}
\to
\textbf{
high-amplitude labels leave}.
}
\tag{28.1}
$$

This is the exact same-parent sheet-replenishment picture.

---

# 29. Counterflow with PFET

DCRP-31 forces inward kinetic-energy PFET through a finite matching region.

DCRP-42/43 force outward/transient anchored shear-label transport on the canonical pancake branch.

Thus the strict rank-two equality state contains a counterflow architecture:

$$
\boxed{
\textbf{
kinetic energy inward}
}
$$

and

$$
\boxed{
\textbf{
amplified shear labels outward / nonrecurrent}.
}
$$

These are different quantities.

No sign contradiction is asserted.

The importance is structural: the same-parent recurrence is an open exchange system, not a closed coherent core.

---

# 30. External pancake calibration

Exact Euler pancake models combine a shear flow with an asymmetric straining flow and permit arbitrary transverse vorticity profiles.

Such constructions demonstrate that strongly anisotropic shear/strain dynamics are legitimate exact Euler mechanisms.

They do not supply the strict same-parent DCRP recurrence or the gauge-completed infinite-reservoir structure derived here.

---

# 31. External vortex-sheet calibration

Recent exact Euler desingularization results construct vorticity supported in tubular neighborhoods of analytic vortex sheets, with thickness

$$
O(\varepsilon)
$$

and lifespan bounded below independently of

$$
\varepsilon.
$$

The vorticity is organized through time-dependent foliations by almost parallel surfaces with tangent divergence-free fields.

This confirms that sheet-like material organization and replenishment geometry are legitimate Euler phenomena.

It does not automatically realize the DCRP scalar cocycle or strict DSS ancestry.

---

# 32. Corrected rank-two scalar branch tree

After gauge completion, the fixed-plane zero-shape rank-two branch is:

$$
\boxed{
\text{anchored shear residual}
}
$$

or

$$
\boxed{
\text{pure anchored scalar cocycle}.
}
$$

On the second branch:

$$
\boxed{
\text{nonzero material labels are nonrecurrent}
}
$$

and, if the branch is global,

$$
\boxed{
\text{every nonempty scalar superlevel has infinite measure}.
}
$$

Thus the pure scalar equality branch requires an infinite normalized sheet/tail reservoir.

---

# 33. Relation to rank lifting

If the anchored scalar cocycle fails because the material trajectory exits the fixed rank-two chart, then one of the following occurs:

- the vorticity plane changes;
- a normal vorticity component appears;
- the potential--shear representation loses its canonical branch;
- the trajectory enters the tail.

These are precisely:

$$
\boxed{
\text{rank lifting}
\ \vee\
\text{plane transition}
\ \vee\
\text{normal-shear residual}
\ \vee\
\text{tail escape}.
}
\tag{33.1}
$$

Thus escape from the scalar cocycle is already represented by existing DCRP transition channels.

---

# 34. Compact-class finite residence compiler

Fix:

- a compact normalized core:

  $$
  K;
  $$

- an anchored amplitude threshold:

  $$
  \delta>0;
  $$

- a uniform scalar bound:

  $$
  M_K.
  $$

Then all pure-cocycle labels satisfying

$$
|\widetilde r|\ge\delta
$$

have no return to

$$
K
$$

after

$$
\boxed{
N_{\rm ret}
=
\left\lfloor
\frac{
\log(M_K/\delta)
}{
(1-2\gamma)S_0
}
\right\rfloor
}
\tag{34.1}
$$

periods.

This gives a finite-horizon material turnover compiler for a compact strong-profile class.

---

# 35. What DCRP-43 closes

The following possibilities are removed on the pure anchored branch.

### recurrent nonzero material shear labels

Impossible.

### periodic nonzero material shear labels

Impossible.

### globally bounded nonzero pure pancake scalar

Impossible.

### globally decaying nonzero pure pancake scalar

Impossible.

### nonzero pure pancake scalar with finite-measure superlevel sets

Impossible.

### nonzero pure pancake scalar in any weak-$L^p$

Impossible.

Thus the only global pure scalar survivor has an intrinsically infinite spatial amplitude reservoir.

---

# 36. What remains open

The infinite anchored-scalar reservoir does not yet imply:

- infinite physical energy;
- non-summable vorticity;
- rank lifting;
- PFET contradiction.

The missing estimate must connect scalar plateau geometry to the physical gradient

$$
\Omega_h
=
J\nabla_h\widetilde q.
$$

This is a sheet-interface/coarea problem.

A slowly varying infinite plateau is not excluded by the scalar theorem alone.

---

# 37. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Infinite-Sheet Reservoir /
Shear-Gradient Coarea Closure.
}
}
$$

A useful theorem would prove that a nonzero global or tail-fed pure anchored scalar cocycle with infinite-measure superlevels must generate at least one of:

1. a nonzero lower bound on planar vorticity/interface measure;

2. a sheet-curvature/folding transition carrier;

3. finite-radius rank lifting;

4. a normal-shear residual;

5. a tail geometry incompatible with the strict DSS kinetic-energy envelope;

6. an exact sheet eigenmode whose same-parent finite-energy ancestry can be excluded separately.

This is now the principal rank-two sheet-replenishment frontier.

---

# 38. End state

The gauge-completed relative potential is

$$
\boxed{
\widetilde q(x_h,z,s)
=
q(x_h,z,s)
-
q(x_{\star,h},z,s).
}
$$

Define

$$
\boxed{
\widetilde r
=
\eta(s)\widetilde q.
}
$$

The exact anchored residual is

$$
\boxed{
\mathcal R_{\rm sh}
=
D_s\widetilde r
-
(1-2\gamma)\widetilde r.
}
$$

The one-period cocycle is

$$
\boxed{
\widetilde r(\Phi a)
=
e^{(1-2\gamma)S_0}
\widetilde r(a)
+
\mathcal Z(a).
}
$$

On the pure branch

$$
\mathcal R_{\rm sh}=0,
$$

$$
\boxed{
\widetilde r(\Phi^m a)
=
e^{m(1-2\gamma)S_0}
\widetilde r(a).
}
$$

Therefore every nonzero material shear label is transient through every bounded recurrent core.

On the global pure branch the superlevel sets satisfy

$$
\boxed{
\Phi(E_\tau)
=
E_{\mu_r\tau},
}
$$

while

$$
\boxed{
|E_{\mu_r\tau}|
=
e^{3\gamma S_0}|E_\tau|.
}
$$

Because

$$
E_{\mu_r\tau}\subset E_\tau
$$

and the Jacobian factor exceeds one, every nonempty scalar superlevel has infinite measure.

Thus the strongest rank-two pure scalar survivor is:

$$
\boxed{
\textbf{
a periodic Eulerian pancake pattern built entirely from transient material labels and an infinite normalized sheet/tail amplitude reservoir.
}
}
$$

The next frontier is:

$$
\boxed{
\textbf{
Infinite-Sheet Reservoir /
Shear-Gradient Coarea Closure.
}
}
$$
