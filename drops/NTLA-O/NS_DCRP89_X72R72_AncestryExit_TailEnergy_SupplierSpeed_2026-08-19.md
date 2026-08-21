# DCRP89 / X72-R72 — Finite-Depth Ancestry Exit, Resolved Tail Energy Atoms, and the Supplier-Speed/Multiplicity Normal Form

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / finite-depth ancestry escape packing round  
**Immediate predecessor:** `NS_DCRP88_X72R71_KelvinRegeneration_AncestryDepth_2026-08-19.md`

**Primary internal dependencies**
- DCRP31 — native global Morrey profile bound
- DCRP32–33 — Kelvin holonomy / material replenishment
- DCRP81–85 — Kelvin residual, line-trace, line-atom, and scale-gap absorption
- DCRP88 — uniform finite backward ancestry depth for circulation atoms

**Fresh primary-source calibration**
- J. Bedrossian, P. Germain, B. Harrop-Griffiths, *Vortex filament solutions of the Navier-Stokes equations*, arXiv:1809.04109. Navier–Stokes admits solutions originating from vorticity concentrated on smooth curves with arbitrary circulation. This is a warning that **circulation alone does not supply an unconditional volumetric kinetic-energy lower bound**; a filter-scale resolution or another regularity input is essential.
- J. Bedrossian, W. Golding, *Uniqueness Criteria for the Oseen Vortex in the 3d Navier-Stokes Equations*, arXiv:2004.07302. The Oseen column corresponds to idealized filament vorticity of arbitrary circulation.
- G. L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159. Coarse-grained circulation naturally exposes scale-local circulation fluxes and possible Kelvin anomalies.

No external theorem is used to prove the exact first-exit alternatives below.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP88 proved that on the compact residual-free resolved-bad class there are finitely many loop templates with a uniform circulation floor

\[
\boxed{
|\Gamma|\ge c_\Gamma>0,
}
\]

and that strict Type-II Kelvin holonomy

\[
\Gamma_{n+1}
=
\rho_\Gamma\Gamma_n,
\qquad
0<\rho_\Gamma<1,
\]

forces every such atom to leave any compact material-loop state class within at most

\[
\boxed{
N_*<\infty
}
\]

backward DSS periods.

DCRP89 quantifies the **first exit**.

Choose a compact loop-state box defined by:

- support radius:
  \[
  |C|\subset B_{R_*};
  \]
- loop length:
  \[
  L(C)\le L_*;
  \]
- tubular reach:
  \[
  \operatorname{reach}(C)\ge\tau_*;
  \]
- curvature and regularity bounds;
- declared packet/state topology.

Choose one fixed filter scale

\[
\boxed{
0<\ell_*
<
c\tau_*.
}
\]

For the first backward ancestor \(C^{\rm ex}\) that leaves this compact box, at least one of the following occurs:

1. **Kelvin-shadowing / SGS / scale defect becomes active** before the exit;
2. **support exits first** while geometry remains tame;
3. **loop geometry exits first** through length / curvature / reach loss;
4. **state/packet shadowing exits first**.

The new result concerns case 2.

Suppose:

\[
|\Gamma(C^{\rm ex})|
\ge
c_\Gamma
\]

and the loop is still geometrically tame:

\[
L(C^{\rm ex})\le L_*,
\qquad
\operatorname{reach}(C^{\rm ex})\ge\tau_*.
\]

Let

\[
U_{\ell_*}
=
\varphi_{\ell_*}*U.
\]

Decompose the circulation:

\[
\boxed{
\Gamma
=
\Gamma_{\rm filt}
+
\Gamma_{\rm inc},
}
\]

where

\[
\Gamma_{\rm filt}
=
\oint_CU_{\ell_*}\cdot dy,
\]

and

\[
\Gamma_{\rm inc}
=
\oint_C(U-U_{\ell_*})\cdot dy.
\]

Then:

## Tail first-exit dichotomy

Either:

\[
\boxed{
|\Gamma_{\rm inc}|
\ge
\frac12c_\Gamma,
}
\]

which is a material-line increment trace and routes back to the already-developed D82–85 increment/scale/state compiler;

or:

\[
\boxed{
|\Gamma_{\rm filt}|
\ge
\frac12c_\Gamma.
}
\]

On the second branch,

\[
|\Gamma_{\rm filt}|
\le
L_*
\|U_{\ell_*}\|_{L^\infty(C)}.
\]

Young's inequality gives:

\[
\|U_{\ell_*}\|_{L^\infty(C)}
\le
C_\varphi
\ell_*^{-3/2}
\|U\|_{L^2(T_{\ell_*}(C))}.
\]

Therefore:

# Main tail-energy atom theorem

\[
\boxed{
\int_{T_{\ell_*}(C)}
|U|^2dy
\ge
c_E
:=
\frac{
c_\Gamma^2
\ell_*^3
}{
4C_\varphi^2L_*^2
}
>0.
}
\]

Thus every geometrically tame support-first exit carries either:

- an already-known increment/scale trace defect;
- or a **fixed positive resolved tail-energy atom**.

This avoids the invalid direct implication

\[
\text{circulation}
\Longrightarrow
\text{volume energy}
\]

by inserting the explicit filter-scale dichotomy.

---

# 1. Why filtering is essential

A circulation atom can be concentrated on a very thin vortex filament.

The vortex-filament literature shows that arbitrary circulation is compatible with vorticity concentrated on smooth curves.

Therefore one must not assert:

\[
|\Gamma(C)|\ge c
\Longrightarrow
\int_{T_\ell(C)}|U|^2\ge c'
\]

without a scale-resolution input.

D89 uses exactly the missing input:

\[
\Gamma
=
\Gamma_{\rm filt}
+
\Gamma_{\rm inc}.
\]

If the circulation lives below the declared filter scale, that is detected by:

\[
\Gamma_{\rm inc}.
\]

If it does not, the filtered field supplies the volumetric energy lower bound.

This is the correct trace-safe statement.

---

# 2. Exact filtering-error representation

For:

\[
U_\ell
=
\varphi_\ell*U,
\]

\[
U(x)-U_\ell(x)
=
\int
\varphi_\ell(z)
[
U(x)-U(x-z)
]dz.
\]

Therefore:

\[
\boxed{
|\Gamma_{\rm inc}|
\le
\int_C
\int
\varphi_\ell(z)
|
\delta_zU(x)
|
\,dz\,ds.
}
\tag{2.1}
\]

Define:

\[
M_{\ell,1}(x)
=
\int
\varphi_\ell(z)
|\delta_zU(x)|dz.
\]

Then:

\[
|\Gamma_{\rm inc}|
\le
\int_C
M_{\ell,1}\,ds.
\]

If:

\[
|\Gamma_{\rm inc}|
\ge
\frac12c_\Gamma,
\]

Hölder gives:

\[
\boxed{
\int_C
M_{\ell,1}^4ds
\ge
\frac{
c_\Gamma^4
}{
16L_*^3
}.
}
\tag{2.2}
\]

Thus the filtering-error branch has a positive material-line quartic increment trace.

This is precisely the kind of codimension-two line detector already treated in D82–84.

---

# 3. Filtered circulation gives a local energy atom

Assume:

\[
|\Gamma_{\rm inc}|
<
\frac12c_\Gamma.
\]

Then:

\[
|\Gamma_{\rm filt}|
\ge
\frac12c_\Gamma.
\]

Also:

\[
|\Gamma_{\rm filt}|
\le
L(C)
\|U_\ell\|_{L^\infty(C)}
\le
L_*
\|U_\ell\|_\infty.
\]

For each:

\[
x\in C,
\]

the convolution samples only:

\[
B_{\ell}(x).
\]

Hence:

\[
\boxed{
\|U_\ell\|_{L^\infty(C)}
\le
\|\varphi_\ell\|_2
\|U\|_{L^2(T_\ell(C))}.
}
\tag{3.1}
\]

In three dimensions:

\[
\boxed{
\|\varphi_\ell\|_2
=
\ell^{-3/2}
\|\varphi\|_2.
}
\tag{3.2}
\]

Therefore:

\[
\frac12c_\Gamma
\le
L_*
\|\varphi\|_2
\ell^{-3/2}
E_{\rm tube}^{1/2}.
\]

So:

## Theorem D89.1 — Resolved Tail-Energy Atom

\[
\boxed{
E_{\rm tube}
:=
\int_{T_\ell(C)}|U|^2dy
\ge
\frac{
c_\Gamma^2\ell^3
}{
4\|\varphi\|_2^2L_*^2
}.
}
\tag{3.3}
\]

At the fixed exit filter:

\[
\ell=\ell_*,
\]

this is the uniform constant \(c_E>0\).

---

# 4. First support exit is quantitatively paid

Let:

\[
n_{\rm ex}\le N_*
\]

be the first backward period for which the loop support exits:

\[
B_{R_*},
\]

while the geometric loop bounds remain valid.

Because backward Kelvin ancestry amplifies circulation,

\[
|\Gamma(C^{\rm ex})|
\ge
|\Gamma(C_0)|
\ge
c_\Gamma.
\]

Therefore:

## Theorem D89.2 — Support-First Exit Payment

Every geometrically tame support-first exit satisfies at least one of:

\[
\boxed{
\text{positive line-increment trace}
}
\]

or:

\[
\boxed{
E_{\rm tube}\ge c_E>0.
}
\]

No unpriced tame support exit exists.

---

# 5. Length-first exit has a strain-action floor

Let a material loop evolve by the similarity advecting field:

\[
Y=\gamma y+U.
\]

Let:

\[
t
\]

be the unit tangent.

The material line element satisfies:

\[
\frac d{ds}
d\ell
=
\left(
\gamma+t^\top St
\right)d\ell,
\]

where:

\[
S=\frac12(\nabla U+\nabla U^\top).
\]

Thus:

\[
\boxed{
\frac d{ds}\log L(s)
=
\gamma
+
\langle
t^\top St
\rangle_{C_s},
}
\tag{5.1}
\]

where the average is weighted by arc length.

Suppose the backward ancestor exits because:

\[
L(-T)=L_*,
\]

while the regenerated atom has:

\[
L(0)\le L_0<L_*.
\]

Then:

\[
\log
\frac{L(0)}{L(-T)}
=
\int_{-T}^{0}
\left[
\gamma
+
\langle t^\top St\rangle
\right]ds.
\]

Hence:

\[
\int_{-T}^{0}
\langle t^\top St\rangle ds
\le
-
\log\frac{L_*}{L_0}
-
\gamma T.
\]

Therefore:

## Theorem D89.3 — Backward Length-Escape Strain Action

\[
\boxed{
\int_{-T}^{0}
\|S(s)\|_{L^\infty(C_s)}
ds
\ge
\log\frac{L_*}{L_0}.
}
\tag{5.2}
\]

So a length-first ancestry escape pays a uniform normalized strain/filamentation action.

---

# 6. Curvature / reach exit

If support and length remain bounded but:

\[
\sup_C|\kappa_C|
\]

exceeds the compact threshold or:

\[
\operatorname{reach}(C)
\downarrow\tau_*,
\]

the loop leaves the geometric compactum through:

\[
\boxed{
R_{\rm fil}.
}
\]

No new terminal coordinate is needed.

At this stage D89 does not claim a universal positive \(L^2\)-strain cost for curvature escape.

That would require a material curvature evolution estimate.

The exit is retained as an explicit filamentation coordinate.

---

# 7. State / packet first exit

If the geometric loop remains inside the declared compact bounds but the:

- packet label;
- return map;
- topology;
- material shadowing map;
- finite loop template state

fails, then the ancestry has entered:

\[
\boxed{
R_{\rm state}.
}
\]

Again no new mechanism is introduced.

---

# 8. Robust Kelvin-shadowing branch

If the prelimit one-period circulation recursion has an error:

\[
\boxed{
|
\Gamma_{k+1}
-
\rho_\Gamma\Gamma_k
|
>
\eta_*,
}
\]

with:

\[
\eta_*
\sim
(1-\rho_\Gamma)c_\Gamma,
\]

then the Kelvin-shadowing defect itself is uniformly active.

D81–85 already reduce that branch to:

- volumetric derivative-compatible increment activity;
- scale-gap debt;
- tail;
- filamentation;
- state compactness failure.

Thus D89 only studies the complementary small-Kelvin-error branch.

---

# 9. First-exit compiler

Combine D88 and Sections 2–8.

## Theorem D89.4 — Finite-Depth First-Exit Compiler

Every regenerated resolved-bad circulation atom satisfies, within at most \(N_*\) backward DSS periods:

\[
\boxed{
R_{\rm inc}
\vee
R_{\rm tailE}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm Kelvin},
}
\tag{9.1}
\]

where:

### \(R_{\rm inc}\)

positive line increment trace, already reduced by D82–85;

### \(R_{\rm tailE}\)

geometrically tame support escape with:

\[
E_{\rm tube}\ge c_E;
\]

### \(R_{\rm fil}\)

length/curvature/reach escape;

### \(R_{\rm state}\)

loop/packet/state transition failure;

### \(R_{\rm Kelvin}\)

prelimit Kelvin-shadowing defect.

No compact and unpaid first-exit mechanism remains.

---

# 10. Repeated tame-tail exits

Now consider \(J\) regenerated circulation atoms and their first support-exit tubes:

\[
T_1,\ldots,T_J.
\]

Assume all non-tail branches are absent.

Then:

\[
\boxed{
\int_{T_i}|U|^2dy
\ge
c_E
}
\]

for every \(i\).

Let:

\[
\boxed{
M_J
=
\left\|
\sum_{i=1}^{J}
1_{T_i}
\right\|_{L^\infty}
}
\tag{10.1}
\]

be the maximal tube overlap multiplicity.

Let:

\[
R_J
\]

be such that:

\[
\bigcup_{i=1}^{J}T_i
\subset
B_{R_J}.
\]

Then:

\[
\begin{aligned}
Jc_E
&\le
\sum_{i=1}^{J}
\int_{T_i}|U|^2dy
\\
&=
\int
|U|^2
\sum_i1_{T_i}
dy
\\
&\le
M_J
\int_{B_{R_J}}
|U|^2dy.
\end{aligned}
\]

Use native Morrey:

\[
\int_{B_R}|U|^2dy
\le
C_MR.
\]

Therefore:

## Theorem D89.5 — Tail Supplier Radius/Multiplicity Trade

\[
\boxed{
R_J
\ge
\frac{
c_E
}{
C_M
}
\frac{
J
}{
M_J
}.
}
\tag{10.2}
\]

Equivalently:

\[
\boxed{
R_JM_J
\ge
c_{\rm sup}J.
}
\tag{10.3}
\]

This is the main packing theorem of D89.

---

# 11. Bounded overlap forces linear tail-speed

If:

\[
\boxed{
M_J\le M_*
}
\]

uniformly, then:

## Corollary D89.6 — Linear Tail-Supplier Escape

\[
\boxed{
R_J
\ge
cJ.
}
\tag{11.1}
\]

Thus repeated tame-tail regeneration requires the normalized supplier radius to move outward at least linearly in the number of resolved regeneration events.

This is a true supplier-speed constraint.

---

# 12. Bounded radius forces multiplicity blow-up

Conversely, if:

\[
R_J
\le R_*
\]

for infinitely many \(J\), then:

\[
\boxed{
M_J
\ge
cJ.
}
\tag{12.1}
\]

Thus a fixed bounded tail region can support infinitely many regenerated circulation atoms only by reusing / overlapping supplier tubes with diverging multiplicity.

This is a supplier-coherence / multiplicity defect.

It is the material-tail analogue of the DCRP02 carrier-multiplicity branch.

---

# 13. No direct contradiction from Morrey packing

The bound:

\[
R_J\gtrsim J
\]

is fully compatible with:

\[
E(R)\lesssim R.
\]

A model with one fixed-energy supplier atom per unit radial distance saturates the estimate.

Therefore:

## Theorem D89.7 — Tail Packing NO-GO

The native Morrey law alone does **not** exclude an infinite sequence of tame circulation suppliers.

It only forces either:

- linear spatial escape;
- or diverging supplier overlap/multiplicity.

This is an important correction against overclaiming.

---

# 14. Infinite supplier normal form

If all other terminal coordinates remain silent, the only tame-tail survivor is now:

\[
\boxed{
\mathsf S_{\rm tail}^{\rm lin}
}
\]

with:

1. one fixed positive resolved tail-energy atom per regeneration;
2. first-exit depth bounded by \(N_*\);
3. supplier tubes with bounded geometry;
4. bounded overlap;
5. supplier radius satisfying:
   \[
   R_J\gtrsim J.
   \]

Call this the:

\[
\boxed{
\textbf{Linear-Speed Tail Supplier Conveyor}.
}
\]

If overlap is unbounded instead, the survivor is:

\[
\boxed{
\mathsf S_{\rm mult}.
}
\]

These are the only new quantitative normal forms produced by repeated support-first exits.

---

# 15. Relation to D21 far-field annular escape

D21 had already reduced a far-field-only stretching survivor to:

\[
\boxed{
\text{spatial-infinity annular vorticity amplification}.
}
\]

D89 arrives independently at a related but circulation-based statement:

\[
\boxed{
\text{repeated resolved circulation regeneration}
\Longrightarrow
\text{linear-speed tail supplier}
\vee
\text{supplier multiplicity}.
}
\]

The next step should compare these two far-field coordinates.

A useful closure would show that a fixed-energy/circulation supplier moving linearly to infinity must either:

- carry diverging normalized annular vorticity amplitude;
- intersect the mandatory D31 PFET supplier annulus;
- or produce a non-summable overlap / interaction cost.

---

# 16. Why circulation does not equal tail vorticity amplitude automatically

By Stokes:

\[
\Gamma(C)
=
\int_\Sigma
\omega\cdot n\,dA
\]

for a spanning surface.

But converting this codimension-one surface integral into a three-dimensional vorticity reservoir requires a trace estimate.

D82 has already shown that such trace steps can hide concentration.

Therefore D89 does **not** identify:

\[
c_\Gamma
\]

with a uniform volumetric enstrophy atom.

The filtered **velocity-energy** argument is used instead because it is trace-safe after the explicit filtering-error split.

---

# 17. Updated late regeneration compiler

D88 gave:

\[
\text{resolved badness regeneration}
\Longrightarrow
\text{finite-depth ancestry escape}.
\]

D89 upgrades it to:

\[
\boxed{
\text{resolved badness regeneration}
\Longrightarrow
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm Kelvin}
\vee
\mathsf S_{\rm tail}^{\rm lin}
\vee
\mathsf S_{\rm mult}.
}
\tag{17.1}
\]

The first four coordinates are already in the existing compiler.

The genuinely new quantitative tail normal forms are:

- linear-speed supplier escape;
- supplier multiplicity/coherence growth.

---

# 18. What is actually closed

D89 closes the possibility:

> “each regenerated circulation atom simply obtains a new tame tail ancestor, with no measurable cost and no growth in supplier complexity.”

That is impossible.

Each tame support-first exit must pay:

\[
c_E>0
\]

in resolved local energy, unless the circulation is already carried by a subfilter increment defect.

Repeated exits therefore force:

\[
R_JM_J\gtrsim J.
\]

No zero-cost stationary tail supplier exists.

---

# 19. What is not proved

D89 does not prove:

- the linear-speed tail supplier conveyor is impossible;
- supplier multiplicity has a globally finite entropy budget;
- a fixed tail-energy atom forces a fixed volumetric vorticity atom;
- tail-energy atoms must intersect the D31 PFET annulus;
- the D21 annular-vorticity amplification is automatically activated;
- repeated filamentation exits are impossible;
- global Navier–Stokes regularity.

The next problem is a **far-field supplier confluence / packing problem**.

---

# 20. New STOP

\[
\boxed{
\textbf{
STOP-D89:
D88's finite ancestry-depth escape can be quantitatively priced. For a geometrically tame support-first exit carrying circulation }\ge c_\Gamma\textbf{, filter at one fixed tube scale }\ell_*\textbf{. If the filtering error carries at least half the circulation, a positive material-line increment trace appears and the branch returns to the existing increment/scale compiler. Otherwise the filtered circulation remains }\ge c_\Gamma/2\textbf{, and Young's inequality forces a fixed positive local tail-energy atom }E_{\rm tube}\ge c_E>0\textbf{. Length-first exits pay a uniform integrated strain action, while curvature/reach and state exits are already filamentation/state defects. For }J\textbf{ tame tail suppliers with overlap multiplicity }M_J\textbf{ and maximum supplier radius }R_J\textbf{, native Morrey gives the exact packing trade }R_JM_J\gtrsim J\textbf{. Thus repeated regeneration cannot use a stationary zero-cost tail source: bounded overlap forces at least linear spatial supplier escape, while bounded radius forces linearly growing supplier multiplicity. Morrey alone does not exclude the resulting linear-speed tail conveyor, so that explicit supplier normal form is now the next target.}
}
\]

---

# 21. Next autonomous step

## DCRP90 / X72-R73 — Linear-Speed Tail Supplier versus Far-Field Annular Amplification

**Working title**

> **Can a Fixed-Energy/Circulation Supplier Escape Linearly to Spatial Infinity without Triggering the Existing Far-Field Vorticity/PFET/Interaction Debts?**

Primary tasks:

1. assume:
   \[
   \mathsf S_{\rm tail}^{\rm lin};
   \]
2. place each \(c_E\)-energy supplier tube into normalized annular shells;
3. compare supplier count per annulus with:
   - D21 annular vorticity amplification;
   - D31 inward PFET matching;
   - DCRP02 far-field comparable-annulus recovery;
4. derive a circulation-resolved annular reassignment inequality;
5. determine whether bounded annular reservoirs allow:
   \[
   R_J\sim J;
   \]
6. if suppliers occupy distinct annuli, test logarithmic/dyadic density rather than raw radius density;
7. if many suppliers share one annulus, route to supplier multiplicity/coherence;
8. seek:
   \[
   \mathsf S_{\rm tail}^{\rm lin}
   \Longrightarrow
   R_{\rm far\mbox{-}amp}
   \vee
   O_{\rm PFET}
   \vee
   R_{\rm mult}
   \vee
   \text{one explicit sparse-tail normal form}.
   \]

Desired endpoint:

\[
\boxed{
\text{repeated finite-depth ancestry escape}
\Longrightarrow
\text{existing far-field paid coordinates}
\vee
\text{one sparse supplier normal form}.
}
\]

---

# 22. One-line checkpoint

Finite-depth circulation regeneration now has a quantitative first-exit price: every tame tail ancestor either exposes a subfilter increment defect or carries a fixed local energy atom, so infinitely many regenerated atoms force the supplier population to move at least linearly to infinity or to develop diverging overlap/multiplicity.

---

**End checkpoint:** DCRP89 / X72-R72  
**Next:** DCRP90 / X72-R73 — Linear-Speed Tail Supplier / Far-Field Annular Confluence.
