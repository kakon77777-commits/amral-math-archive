# DCRP90 / X72-R73 — Finite-Time Material Transport No-Go for the Linear-Speed Tail Supplier

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / far-tail material-supplier round  
**Immediate predecessor:** `NS_DCRP89_X72R72_AncestryExit_TailEnergy_SupplierSpeed_2026-08-19.md`

**Primary internal dependencies**
- DCRP21 — Eulerian far-field annular vorticity amplification
- DCRP31 — finite-radius inward PFET
- DCRP71 — native time-slice Morrey bound
- DCRP82–85 — material-worldsheet increment / trace / scale compiler
- DCRP88–89 — finite ancestry depth and tame-tail supplier packing

**Fresh primary-source calibration**
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560.
- L. Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619.
- J. Bedrossian, P. Germain, B. Harrop-Griffiths, *Vortex filament solutions of the Navier-Stokes equations*, arXiv:1809.04109.

The vortex-filament literature is again a warning: circulation can be carried on very thin structures, so no direct circulation-to-volume-energy estimate is used below.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP89 left one explicit tame-tail survivor:

\[
\boxed{
\mathsf S_{\rm tail}^{\rm lin}
}
\]

with:

1. one resolved circulation/energy supplier per regeneration;
2. bounded geometry;
3. bounded supplier overlap;
4. supplier radius at least linear in the number of regeneration events.

DCRP90 proves that this normal form is **not dynamically compatible with the finite ancestry depth from D88**.

The key fact is that the supplier is not merely an Eulerian remote source.

It is a **material ancestor** that must return from the tail to the compact bad core within the uniformly bounded similarity time

\[
\boxed{
T_*
=
N_*S_0.
}
\]

The similarity material flow satisfies:

\[
\boxed{
\dot X
=
\gamma X+U(X,s).
}
\tag{0.1}
\]

If a tame material loop worldsheet reaches radius

\[
R\gg1
\]

and later returns to a fixed core ball in time at most \(T_*\), variation of constants forces an \(O(R)\) material velocity action:

\[
\boxed{
\int |U(X(s),s)|\,ds
\gtrsim
R.
}
\tag{0.2}
\]

Apply this not to one point but to a fixed-length arc of the tame material loop.

At one fixed filter scale

\[
0<\ell_*<c\,\tau_*,
\]

split:

\[
\boxed{
U
=
U_{\ell_*}
+
(U-U_{\ell_*}).
}
\]

Then exactly one of the following carries at least half of the \(O(R)\) worldsheet action.

---

## A. subfilter/increment transport

If:

\[
\iint_{\mathcal W}
|U-U_{\ell_*}|
\gtrsim R,
\]

then the material-worldsheet quartic increment trace satisfies:

\[
\boxed{
\iint_{\mathcal W}
\mathfrak M_{\ell_*,4}^{\,4}
\gtrsim
R^4.
}
\tag{0.3}
\]

This is already an active D82-type line/worldsheet increment defect.

If it tries to hide volumetrically, D82–85 route it into:

\[
R_{\rm scale}
\vee
R_{\rm state}
\vee
\text{increment concentration}.
\]

---

## B. resolved filtered transport

If instead:

\[
\iint_{\mathcal W}
|U_{\ell_*}|
\gtrsim R,
\]

then Cauchy–Schwarz gives:

\[
\boxed{
\iint_{\mathcal W}
|U_{\ell_*}|^2
\gtrsim
R^2.
}
\tag{0.4}
\]

For a tame curve with reach bounded below and \(\ell_*<c\tau_*\),

\[
\boxed{
\int_{C_s}
|U_{\ell_*}|^2d\sigma
\le
C
\ell_*^{-2}
\int_{T_{\ell_*}(C_s)}
|U|^2dy.
}
\tag{0.5}
\]

Therefore:

\[
\boxed{
\int_{s_*}^{0}
\int_{T_{\ell_*}(C_s)}
|U|^2dyds
\gtrsim
\ell_*^2R^2.
}
\tag{0.6}
\]

But DCRP71 gives the native time-slice Morrey bound:

\[
\boxed{
\int_{B_Q}
|U(y,s)|^2dy
\le
C_MQ
\qquad
\forall s.
}
\tag{0.7}
\]

The entire worldsheet lies inside a ball of radius \(R+O(1)\).

Since the transit time is at most \(T_*\),

\[
\boxed{
\int_{s_*}^{0}
\int_{B_{R+O(1)}}
|U|^2dyds
\lesssim
T_*C_MR.
}
\tag{0.8}
\]

Combining (0.6) and (0.8):

\[
\boxed{
c\ell_*^2R^2
\le
CT_*C_MR.
}
\]

Hence:

## Main theorem — tame finite-time tail transport ceiling

\[
\boxed{
R
\le
R_{\rm tame}
<
\infty
}
\tag{0.9}
\]

unless an increment/scale/state/filamentation defect becomes active.

Therefore the linear-speed material supplier conveyor of D89 is eliminated.

---

# 1. Exact similarity material trajectory identity

Let:

\[
s_*\le0,
\qquad
T=-s_*\le T_*.
\]

For one material marker:

\[
\dot X
=
\gamma X+U(X,s).
\]

Variation of constants gives:

\[
\boxed{
X(0)
=
e^{\gamma T}X(s_*)
+
\int_{s_*}^{0}
e^{-\gamma\tau}
U(X(\tau),\tau)d\tau.
}
\tag{1.1}
\]

Hence:

\[
e^{\gamma T}|X(s_*)|
-
|X(0)|
\le
\int_{s_*}^{0}
e^{-\gamma\tau}|U|d\tau.
\]

Since:

\[
e^{-\gamma\tau}
\le
e^{\gamma T}
\qquad
(\tau\in[s_*,0]),
\]

we obtain:

## Theorem D90.1 — Material Return Action

\[
\boxed{
\int_{s_*}^{0}
|U(X(\tau),\tau)|d\tau
\ge
|X(s_*)|
-
e^{-\gamma T}|X(0)|.
}
\tag{1.2}
\]

If:

\[
|X(s_*)|\ge R,
\qquad
|X(0)|\le R_0,
\]

then:

\[
\boxed{
\int_{s_*}^{0}|U|d\tau
\ge
R-R_0.
}
\tag{1.3}
\]

The similarity drift does not help a far-tail ancestor return inward.

It must be countered by \(U\).

---

# 2. Fixed material arc at the farthest excursion

Let:

\[
R
=
\sup_{
s\in[-T_*,0],
\ x\in C_s
}
|x|.
\]

Choose:

\[
(s_*,x_*)
\]

with:

\[
|x_*|=R.
\]

On a geometrically tame loop there exists a fixed arc-length scale:

\[
a_0>0
\]

depending only on the compact loop class.

Choose a material arc:

\[
I_*
\subset C_{s_*}
\]

centered at \(x_*\) with:

\[
|I_*|=a_0.
\]

For every:

\[
x\in I_*,
\]

\[
|x|
\ge
R-a_0.
\]

Suppose the regenerated descendant loop lies in:

\[
B_{R_0}.
\]

Then every marker in \(I_*\) satisfies:

\[
\boxed{
\int_{s_*}^{0}|U(X_x(s),s)|ds
\ge
R-a_0-R_0.
}
\tag{2.1}
\]

---

# 3. Tame worldsheet geometry

Let:

\[
\mathcal W
=
\{
(X_x(s),s):
x\in I_*,
\ s\in[s_*,0]
\}.
\]

Parameterize by arc length \(d\sigma_*\) at \(s_*\).

Assume the material line Jacobian satisfies:

\[
\boxed{
0<J_-\le
J(x,s)
\le
J_+<\infty.
}
\tag{3.1}
\]

If this fails, the branch is already:

\[
\boxed{
R_{\rm fil}
\vee
R_{\rm state}.
}
\]

Under (3.1), the worldsheet measure satisfies:

\[
|\mathcal W|
\le
J_+a_0T_*.
\]

Integrating (2.1) with current arc-length measure gives:

## Theorem D90.2 — Worldsheet Transport Action

For all sufficiently large \(R\),

\[
\boxed{
\iint_{\mathcal W}|U|d\sigma ds
\ge
c_0R,
}
\tag{3.2}
\]

where:

\[
c_0>0
\]

depends only on:

\[
J_-,
a_0,
R_0.
\]

---

# 4. Fixed-scale transport split

Let:

\[
U_\ell
=
\varphi_\ell*U,
\qquad
\ell=\ell_*.
\]

Then:

\[
\iint_{\mathcal W}|U|
\le
\iint_{\mathcal W}|U_\ell|
+
\iint_{\mathcal W}|U-U_\ell|.
\]

Therefore:

## Theorem D90.3 — Transport Split

At least one of:

\[
\boxed{
\iint_{\mathcal W}|U_\ell|
\ge
\frac12c_0R
}
\tag{4.1}
\]

or:

\[
\boxed{
\iint_{\mathcal W}|U-U_\ell|
\ge
\frac12c_0R
}
\tag{4.2}
\]

holds.

No sign information is required.

---

# 5. Increment branch

The filtering error has the exact increment representation:

\[
U(x)-U_\ell(x)
=
\int
\varphi_\ell(z)
[
U(x)-U(x-z)
]dz.
\]

Thus:

\[
\boxed{
|U-U_\ell|
\le
M_{\ell,1}
\le
M_{\ell,4},
}
\tag{5.1}
\]

where:

\[
M_{\ell,4}^4
=
\int
\varphi_\ell(z)
|\delta_zU|^4dz
\]

schematically.

If (4.2) holds, Hölder on the finite worldsheet gives:

## Theorem D90.4 — Far Transport Forces a Quartic Increment Trace

\[
\boxed{
\iint_{\mathcal W}
M_{\ell,4}^{\,4}
d\sigma ds
\ge
c_{\rm inc}R^4.
}
\tag{5.2}
\]

Indeed:

\[
\left(
\iint_{\mathcal W}M_{\ell,4}
\right)^4
\le
|\mathcal W|^3
\iint_{\mathcal W}M_{\ell,4}^4.
\]

The worldsheet measure is uniformly bounded.

Thus an arbitrarily far material return cannot remain increment-silent.

---

# 6. Resolved branch: trace-to-volume conversion is now safe

Assume (4.1).

Cauchy–Schwarz gives:

\[
\boxed{
\iint_{\mathcal W}|U_\ell|^2d\sigma ds
\ge
\frac{
c_0^2R^2
}{
4J_+a_0T_*
}.
}
\tag{6.1}
\]

Unlike the unfiltered trace problems of D82, \(U_\ell\) is already smooth at the fixed scale \(\ell_*\).

For:

\[
x\in C_s,
\]

Young's inequality gives:

\[
|U_\ell(x,s)|^2
\le
\|\varphi_\ell\|_2^2
\int_{B_\ell(x)}
|U(y,s)|^2dy.
\]

Since:

\[
\|\varphi_\ell\|_2^2
=
\ell^{-3}
\|\varphi\|_2^2,
\]

\[
\boxed{
|U_\ell(x,s)|^2
\le
C_\varphi
\ell^{-3}
\int_{B_\ell(x)}
|U(y,s)|^2dy.
}
\tag{6.2}
\]

---

# 7. Curve-ball intersection bound

Assume throughout the transit:

\[
\boxed{
\operatorname{reach}(C_s)
\ge
\tau_*>0,
}
\]

and choose:

\[
\ell_*<\tau_*/4.
\]

Then a standard local geometry estimate gives:

\[
\boxed{
\operatorname{Length}
(
C_s\cap B_\ell(y)
)
\le
C_{\rm geo}\ell.
}
\tag{7.1}
\]

Integrate (6.2) over the material arc:

\[
\begin{aligned}
\int_{I_s}|U_\ell|^2d\sigma
&\le
C_\varphi
\ell^{-3}
\int
|U(y,s)|^2
\operatorname{Length}
(
I_s\cap B_\ell(y)
)
dy
\\
&\le
C
\ell^{-2}
\int_{T_\ell(I_s)}
|U(y,s)|^2dy.
\end{aligned}
\]

Therefore:

## Theorem D90.5 — Fixed-Filter Worldsheet Thickening

\[
\boxed{
\iint_{\mathcal W}|U_\ell|^2d\sigma ds
\le
C_{\rm tg}
\ell^{-2}
\int_{s_*}^{0}
\int_{T_\ell(I_s)}
|U|^2dyds.
}
\tag{7.2}
\]

This trace-to-volume step is legitimate because the field is filtered first and the curve has uniform reach.

---

# 8. Quadratic transport-energy lower bound

Combine (6.1) and (7.2).

## Theorem D90.6 — Resolved Finite-Time Tail Transport Cost

\[
\boxed{
\int_{s_*}^{0}
\int_{T_\ell(I_s)}
|U|^2dyds
\ge
c_{\rm tr}
\ell^2R^2.
}
\tag{8.1}
\]

The constant depends only on the compact geometry and \(T_*\).

This is the key new scaling:

\[
\boxed{
\text{resolved tame tail return cost}
\sim
R^2.
}
\]

---

# 9. Native time-slice Morrey upper bound

DCRP71 audited the native bound and established on the compact strong-profile branch:

\[
\boxed{
\int_{B_Q}
|U(y,s)|^2dy
\le
C_MM_0Q
\qquad
\forall Q\ge1,
\quad
\forall s.
}
\tag{9.1}
\]

The transit worldsheet is contained in:

\[
B_{R+\ell}.
\]

Thus:

\[
\begin{aligned}
\int_{s_*}^{0}
\int_{T_\ell(I_s)}
|U|^2dyds
&\le
\int_{s_*}^{0}
\int_{B_{R+\ell}}
|U|^2dyds
\\
&\le
T_*C_MM_0(R+\ell).
\end{aligned}
\]

Therefore:

## Theorem D90.7 — Linear Morrey Upper Cost

\[
\boxed{
\int_{s_*}^{0}
\int_{T_\ell(I_s)}
|U|^2
\le
C_{\rm Mor}T_*(R+\ell).
}
\tag{9.2}
\]

---

# 10. Tame far-tail return contradiction

Use (8.1) and (9.2):

\[
c_{\rm tr}\ell^2R^2
\le
C_{\rm Mor}T_*(R+\ell).
\]

For:

\[
R\ge2\ell,
\]

\[
R+\ell
\le
\frac32R.
\]

Hence:

\[
\boxed{
R
\le
\frac{
3C_{\rm Mor}T_*
}{
2c_{\rm tr}\ell^2
}.
}
\tag{10.1}
\]

Define:

\[
\boxed{
R_{\rm tame}
=
\max
\left\{
2\ell,
\frac{
3C_{\rm Mor}T_*
}{
2c_{\rm tr}\ell^2
}
\right\}.
}
\tag{10.2}
\]

Then:

## Theorem D90.8 — Finite-Time Material Tail Transport NO-GO

A resolved, fixed-filter, geometrically tame material ancestry satisfying the native Morrey bound cannot:

\[
\boxed{
R\to\infty
}
\]

while returning to the compact core in time:

\[
T\le T_*.
\]

If the ancestry reaches arbitrarily large normalized radius, at least one of:

\[
\boxed{
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}
}
\]

must occur.

---

# 11. Absorption of the D89 linear-speed supplier

D89 proved for \(J\) tame tail suppliers:

\[
\boxed{
R_JM_J
\gtrsim
J.
}
\]

There were two surviving routes:

### bounded radius

\[
R_J\le R_*,
\]

forcing:

\[
M_J\to\infty,
\]

which is already:

\[
\boxed{
R_{\rm state}
\vee
R_{\rm mult}.
}
\]

### bounded overlap

\[
M_J\le M_*,
\]

forcing:

\[
R_J\to\infty.
\]

D90.8 now excludes this route unless:

\[
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\]

becomes active.

Therefore:

## Theorem D90.9 — Linear-Speed Tail Supplier Absorption

\[
\boxed{
\mathsf S_{\rm tail}^{\rm lin}
\Longrightarrow
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}.
}
\tag{11.1}
\]

The explicit D89 infinite tail-supplier normal form is removed.

---

# 12. Important distinction from D21 FAR

D21 studies an **Eulerian far-field strain source**.

Its remote annular vorticity need not be the same material object that later arrives in the core.

D90 studies a **material circulation ancestor**.

These are different mechanisms.

Therefore D90 does **not** say:

\[
\boxed{
\text{all far-field annular vorticity sources are impossible}.
}
\]

Instead:

\[
\boxed{
\text{finite-depth material return from arbitrarily far radius is impossible on the tame resolved branch}.
}
\]

A remote Eulerian source may still influence the core through its induced velocity/strain without being materially transported into the core.

That branch remains exactly the D20–21 FAR architecture.

---

# 13. Confluence with D21

D21 proved that on the far-field-only stretching branch, if the core filtered-enstrophy profile collapses while positive far-field work persists, then the source annulus must escape to normalized spatial infinity and its normalized annular vorticity amplitude diverges.

Thus the remaining remote-tail possibilities now separate cleanly.

## material regeneration supplier

\[
\boxed{
\text{material tail ancestry}
}
\]

is absorbed by D90 into:

\[
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}.
\]

## Eulerian remote interaction supplier

\[
\boxed{
\text{far-field strain source}
}
\]

is already:

\[
\boxed{
R_{\rm far\mbox{-}amp}
}
\]

in D21, or one of its bounded-reservoir comparable-annulus/residual alternatives.

This is a genuine confluence rather than an identification.

---

# 14. Comparable-annulus recovery does not close material transport

DCRP02 proves for the Eulerian FAR interaction:

\[
\mu_k^{\rm far,ann}
\le
C_0
\sum_{j\le k}
2^{-(k-j)}
\mathfrak A_j
\mathcal Q_k.
\]

Under bounded reservoirs, order-one FAR output must enter a bounded relative annular band or pay amplitude escape.

This theorem is about **interaction strength**.

D90's material transport theorem is about **finite-time ancestry motion**.

Neither implies the other.

The two now cover complementary tail mechanisms.

---

# 15. PFET remains simultaneous and independent

D31 gives a mandatory finite-radius period-averaged inward PFET witness:

\[
\boxed{
\mathcal O_{\rm PFET}>0
}
\]

for every nonzero compact strict DSS profile.

D90 does not use this PFET to prove the material-transport NO-GO.

Therefore the correct statement remains:

\[
\boxed{
\mathcal O_{\rm PFET}
\quad\wedge\quad
\text{ancestry/interaction terminal alternative}.
}
\]

No identity is asserted between:

- tail transport cost;
- far-field strain work;
- PFET.

This preserves the D49 independence warning.

---

# 16. What happened to the “sparse-tail” normal form?

D89 suggested that perhaps one supplier could occupy each increasingly distant radial location, producing a sparse linearly escaping ancestry.

D90 shows that finite ancestry depth destroys this possibility.

To return from radius \(R\) in bounded similarity time, the material worldsheet must pay either:

\[
\boxed{
O(R^4)
}
\]

quartic increment trace,

or:

\[
\boxed{
O(R^2)
}
\]

resolved tube energy.

The native branch only permits:

\[
\boxed{
O(R)
}
\]

time-slice kinetic-energy growth.

Thus:

## Theorem D90.10 — No Sparse Tame Material Tail Conveyor

There is no independent sparse-tail material supplier normal form.

Its only escapes are already-existing increment / filamentation / state noncompactness.

---

# 17. Updated regeneration compiler

D88–89 gave:

\[
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
\]

D81–85 absorbed \(R_{\rm Kelvin}\).

D89 absorbed \(\mathsf S_{\rm mult}\) into state/multiplicity.

D90 absorbs \(\mathsf S_{\rm tail}^{\rm lin}\).

Therefore:

## Theorem D90.11 — Material Regeneration without an Independent Tail Terminal

\[
\boxed{
\text{same-parent resolved badness regeneration}
\Longrightarrow
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}.
}
\tag{17.1}
\]

This theorem is restricted to the declared compact/tame material ancestry setup and the native Morrey branch.

It does not eliminate Eulerian far-field interaction sources.

---

# 18. Late global architecture

The rank-two late architecture now has two orthogonal observations.

## finite core

\[
\boxed{
\mathcal O_{\rm PFET}>0
}
\]

from D31.

## regenerated material ancestry

\[
\boxed{
R_{\rm inc}
\vee
R_{\rm fil}
\vee
R_{\rm state}
}
\]

from D88–90.

## remote Eulerian interaction

if needed independently:

\[
\boxed{
R_{\rm far\mbox{-}amp}
\vee
\text{comparable-annulus / amplitude / residual alternatives}
}
\]

from D20–21 / DCRP02.

Thus the old generic “tail supplier” label has split into two precise, noninterchangeable mechanisms.

---

# 19. Why this is stronger than D89 packing

D89 used only static supplier counting:

\[
R_JM_J\gtrsim J.
\]

That allowed the saturated model:

\[
R_J\sim J,
\qquad
M_J=O(1).
\]

D90 adds the missing dynamical datum:

\[
\boxed{
\text{every supplier must reach the bad core within }T_*<\infty.
}
\]

This changes the required resolved energy from:

\[
O(1)
\]

per supplier to:

\[
\boxed{
O(R^2)
}
\]

for a supplier at radius \(R\).

The native Morrey reservoir grows only as:

\[
O(R).
\]

That is the decisive exponent mismatch.

---

# 20. Status ledger

## PROVED this round

### D90-P1 — exact similarity material return-action lower bound.

### D90-P2 — fixed farthest-arc worldsheet carries \(O(R)\) velocity action.

### D90-P3 — fixed-scale resolved/increment transport dichotomy.

### D90-P4 — increment transport branch forces:

\[
\iint_{\mathcal W}
M_{\ell,4}^4
\gtrsim
R^4.
\]

### D90-P5 — filtered tame-worldsheet trace converts safely to a volumetric tube energy bound.

### D90-P6 — resolved tame finite-time tail return costs:

\[
E_{\rm tube,time}
\gtrsim
\ell_*^2R^2.
\]

### D90-P7 — native time-slice Morrey gives only:

\[
E_{\rm tube,time}
\lesssim
T_*C_MR.
\]

### D90-P8 — uniform tame tail-radius ceiling \(R_{\rm tame}<\infty\).

### D90-P9 — D89 linear-speed tail supplier is absorbed into increment / filamentation / state defects.

### D90-P10 — material-tail regeneration and Eulerian far-field interaction are formally separated.

### D90-P11 — PFET remains a simultaneous independent finite-core obligation.

---

# 21. What is not proved

D90 does not prove:

- all Eulerian far-field vorticity/strain sources are impossible;
- D21 spatial-infinity annular vorticity amplification is impossible;
- repeated filamentation exits are impossible;
- repeated increment/scale defects have a globally finite budget;
- state-transition multiplicity is impossible;
- PFET equals any tail-transport or far-field work functional;
- global Navier–Stokes regularity.

The material **support-escape** branch is substantially closed; the remaining material ancestry is now forced into geometry/scale/state noncompactness.

---

# 22. New STOP

\[
\boxed{
\textbf{
STOP-D90:
The D89 linear-speed tail supplier is not dynamically viable as a tame same-parent material ancestry. D88 gives a uniform finite return time }T_*=N_*S_0\textbf{. A material loop arc that reaches radius }R\textbf{ and returns to the compact bad core in that time must pay }O(R)\textbf{ velocity action by the exact similarity-flow variation formula. At a fixed filter scale, either the filtering error carries this transport, forcing an }O(R^4)\textbf{ material-worldsheet increment trace and hence an existing increment/scale/state defect, or the filtered velocity carries it. On a bounded-reach/bounded-stretch worldsheet the latter implies an }O(R^2)\textbf{ volumetric tube-energy cost, while the native time-slice Morrey law supplies only }O(R)\textbf{ energy over the same bounded time interval. Hence the resolved tame branch has a uniform radius ceiling. Combining with D89, bounded-radius repeated suppliers force multiplicity/state blow-up, while bounded-overlap suppliers would have to escape to infinity and are now impossible without increment or filamentation. Thus no independent sparse/linear material-tail conveyor remains. This does not eliminate D21's Eulerian remote-strain source; it separates it cleanly from material regeneration, while D31 PFET remains an independent simultaneous finite-core obligation.}
}
\]

---

# 23. Next autonomous step

## DCRP91 / X72-R74 — Kelvin-Forced Filamentation versus Filtered Direction/Diffusion

**Working title**

> **If Material Support Escape Is Closed, Can Repeated Finite-Depth Kelvin Ancestry Exit Only by Filamenting without Paying the Existing Direction-Defect / Diffusion / X72 Coordinates?**

Primary tasks:

1. assume D90 material support transport is silent;
2. follow D88's finite-depth ancestry exit through:
   - loop length growth;
   - curvature/reach collapse;
   - line-stretch Jacobian degeneration;
3. use D89's integrated strain-action floor;
4. compare filamentation with D50–53:
   - thickness-scale folding;
   - vorticity-direction gradients;
   - filtered covariance rank-lifting;
5. insert the external filtered-vorticity direction-defect inequality;
6. determine whether bounded filter ratio gives:
   \[
   R_{\rm fil}
   \Longrightarrow
   P_{\rm diff}
   \vee
   \widetilde{\mathcal S}_{\rm active}
   \vee
   X
   \vee
   R_{\rm scale};
   \]
7. classify shrinking filter-ratio escape separately;
8. seek a finite-depth filamentation compiler.

Desired endpoint:

\[
\boxed{
\text{same-parent material regeneration}
\Longrightarrow
\text{existing finite-scale paid coordinates}
\vee
R_{\rm state}.
}
\]

---

# 24. One-line checkpoint

Finite-depth Kelvin ancestry can no longer escape through a tame far-tail material conveyor: bounded-time return from radius \(R\) costs \(R^2\) resolved tube energy unless an \(R^4\) increment trace or filament/state defect is already active, contradicting the native \(O(R)\) Morrey reservoir for large \(R\).

---

**End checkpoint:** DCRP90 / X72-R73  
**Next:** DCRP91 / X72-R74 — Kelvin-Forced Filamentation / Filtered Direction-Diffusion.
