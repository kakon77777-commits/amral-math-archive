# DCRP82 / X72-R65 — Codimension-Two Trace Barrier and the Material-Loop Increment Concentration Defect

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / Kelvin-to-volumetric visibility audit  
**Immediate predecessor:** `NS_DCRP81_X72R64_KelvinResidue_SGSCommBridge_2026-08-18.md`

**Primary internal dependencies**
- DCRP20–26 — filtered-vorticity commutator detector
- DCRP33 — viscous Kelvin residue
- DCRP80–81 — terminal compiler and Kelvin-to-SGS reduction

**Fresh external calibration**
- Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560. In particular, the differentiated stress forcing
  \[
  -\nabla\times\nabla\cdot R_\ell
  \]
  is controlled volumetrically through the derivative-compatible increment envelope
  \[
  \widetilde{\mathcal S}^{(3)}.
  \]
- Gregory L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159, and *Turbulent Cascade of Circulations*, arXiv:physics/0605014. Coarse-grained circulation exposes an interscale circulation flux and may fail to obey Kelvin conservation when sufficiently singular small-scale structure survives.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP81 reduced the second-order viscous Kelvin residue to the SGS circulation term

\[
\boxed{
\mathfrak K_{\ell}^{\rm sgs}
=
-
\int
\oint_{C_\ell(t)}
\nabla\cdot R_\ell\cdot dy\,dt
}
\]

plus already-declared material-loop/shadowing defects.

The proposed next step was to absorb this singular material-loop functional into the already-existing **volumetric** derivative-compatible commutator detector.

DCRP82 shows:

> **this absorption is not unconditional.**

There is a genuine codimension-two trace barrier.

Let

\[
\boxed{
B_\ell
=
\nabla\cdot R_\ell.
}
\]

The filtered-vorticity source gives the exact increment estimate

\[
\boxed{
|B_\ell|
\le
\frac{C_\varphi}{\ell}
\mathfrak M_{\ell,4}^{\,2},
}
\tag{0.1}
\]

where \(\mathfrak M_{\ell,4}\) is the derivative-compatible velocity-increment envelope.

Therefore

\[
\boxed{
|\mathfrak K_\ell^{\rm sgs}|
\le
\frac{C_\varphi}{\ell}
\int
\int_{C_\ell(t)}
\mathfrak M_{\ell,4}^{\,2}
\,ds\,dt.
}
\tag{0.2}
\]

For a normalized cylinder of spatial radius \(r\) and time length \(O(r^2)\), assume

\[
\boxed{
\sup_t
\operatorname{Length}(C_\ell(t))
\le
L_* r.
}
\tag{0.3}
\]

Cauchy–Schwarz gives

\[
\boxed{
|\mathfrak K_\ell^{\rm sgs}|^2
\le
C
\frac{r^3}{\ell^2}
\int
\int_{C_\ell(t)}
\mathfrak M_{\ell,4}^{\,4}
\,ds\,dt.
}
\tag{0.4}
\]

Define the **line-trace derivative-compatible increment detector**

\[
\boxed{
\widetilde{\mathcal S}_{C;r,\ell}^{(4)}
:=
r
\int
\int_{C_\ell(t)}
\mathfrak M_{\ell,4}^{\,4}
\,ds\,dt.
}
\tag{0.5}
\]

Then

\[
\boxed{
|\mathfrak K_\ell^{\rm sgs}|^2
\le
C
\left(\frac r\ell\right)^2
\widetilde{\mathcal S}_{C;r,\ell}^{(4)}.
}
\tag{0.6}
\]

At fixed relative filter ratio

\[
\ell=\sigma r,
\]

\[
\boxed{
|\mathfrak K_\ell^{\rm sgs}|^2
\le
C_\sigma
\widetilde{\mathcal S}_{C;r,\ell}^{(4)}.
}
\tag{0.7}
\]

Thus a nonzero SGS Kelvin circulation requires a nonzero **material-loop increment trace**.

But the existing detector is volumetric:

\[
\boxed{
\widetilde{\mathcal S}_{V;r,\ell}^{(4)}
=
\frac r{\ell^2}
\iint_{Q_r}
\mathfrak M_{\ell,4}^{\,4}
\,dxdt.
}
\tag{0.8}
\]

There is no unconditional inequality

\[
\widetilde{\mathcal S}_{C}
\lesssim
\widetilde{\mathcal S}_{V}.
\]

That is the new audit result.

---

# 1. Tube-localized volumetric detector

Let

\[
\boxed{
T_\ell(C(t))
=
\{
x:
\operatorname{dist}(x,C(t))<c\ell
\}.
}
\]

Define the tube-localized volumetric increment mass

\[
\boxed{
\widetilde{\mathcal S}_{T;r,\ell}^{(4)}
=
\frac r{\ell^2}
\int
\int_{T_\ell(C(t))}
\mathfrak M_{\ell,4}^{\,4}
\,dxdt.
}
\tag{1.1}
\]

Clearly

\[
\boxed{
\widetilde{\mathcal S}_{T;r,\ell}^{(4)}
\le
\widetilde{\mathcal S}_{V;r,\ell}^{(4)}
}
\]

provided the tube lies inside the declared volumetric cutoff.

Now define the dimensionless material-loop trace ratio

\[
\boxed{
\Theta_{\rm tr}(r,\ell;C)
:=
\frac{
\ell^2
\displaystyle
\int
\int_{C(t)}
\mathfrak M_{\ell,4}^{\,4}
\,dsdt
}{
\displaystyle
\int
\int_{T_\ell(C(t))}
\mathfrak M_{\ell,4}^{\,4}
\,dxdt
}.
}
\tag{1.2}
\]

Then exactly:

## Theorem D82.1 — Trace/Volume Factorization

\[
\boxed{
\widetilde{\mathcal S}_{C;r,\ell}^{(4)}
=
\Theta_{\rm tr}
\,
\widetilde{\mathcal S}_{T;r,\ell}^{(4)}.
}
\tag{1.3}
\]

Therefore:

## Theorem D82.2 — Kelvin Trace Visibility Bound

\[
\boxed{
|\mathfrak K_\ell^{\rm sgs}|^2
\le
C
\left(\frac r\ell\right)^2
\Theta_{\rm tr}
\,
\widetilde{\mathcal S}_{T;r,\ell}^{(4)}.
}
\tag{1.4}
\]

At fixed \(\ell=\sigma r\):

\[
\boxed{
|\mathfrak K_\ell^{\rm sgs}|^2
\le
C_\sigma
\Theta_{\rm tr}
\,
\widetilde{\mathcal S}_{V;r,\ell}^{(4)}.
}
\tag{1.5}
\]

This is the correct bridge.

---

# 2. Conditional absorption theorem

Suppose along a same-parent sequence:

\[
\boxed{
\sup_n
\Theta_{{\rm tr},n}
<\infty.
}
\tag{2.1}
\]

Then:

## Theorem D82.3 — Bounded-Trace Kelvin Absorption

If

\[
\widetilde{\mathcal S}_{V,n}^{(4)}
\to0,
\]

then

\[
\boxed{
\mathfrak K_{n,\ell_n}^{\rm sgs}
\to0.
}
\tag{2.2}
\]

Therefore, on a bounded-trace class,

\[
\boxed{
\mathsf R_{\rm SGS\mbox{-}circ}
\Longrightarrow
\widetilde{\mathcal S}^{(4)}_{\rm active}.
}
\tag{2.3}
\]

The Kelvin terminal coordinate is absorbed into an already-existing derivative-compatible increment defect.

---

# 3. The only way to hide from the volumetric detector

Suppose instead:

\[
\limsup_n
|\mathfrak K_{n,\ell_n}^{\rm sgs}|
>0,
\]

while:

\[
\widetilde{\mathcal S}_{V,n}^{(4)}
\to0.
\]

Then (1.5) forces:

## Theorem D82.4 — Trace-Concentration Necessity

\[
\boxed{
\Theta_{{\rm tr},n}
\to\infty.
}
\tag{3.1}
\]

Thus the only way a Kelvin circulation defect can hide from the volumetric commutator detector is for the derivative-compatible increment mass to concentrate increasingly strongly on the moving material loop relative to its \(\ell\)-tube.

This is the precise remaining gap.

---

# 4. Why codimension two matters

A space-time material loop has:

- one spatial dimension;
- one time dimension.

The volumetric filtered detector lives in:

- three spatial dimensions;
- one time dimension.

The transverse codimension is two.

An \(\ell\)-tube around a length-\(O(r)\) loop has spatial volume:

\[
\boxed{
O(r\ell^2).
}
\]

Thus the natural tube-to-line conversion has exactly the factor

\[
\boxed{
\ell^{-2}.
}
\]

This is why the volumetric detector contains the same \(\ell^{-2}\) normalization but still needs a **trace nonconcentration hypothesis**.

---

# 5. Kinematic trace countermodel

The failure of unconditional trace control can be seen without any PDE claim.

Take a fixed smooth curve \(C\) of length \(1\).

Let:

\[
f_\delta(x)
=
\psi\!\left(
\frac{\operatorname{dist}(x,C)}{\delta}
\right),
\]

where:

\[
0\le\psi\le1,
\qquad
\psi(0)=1,
\]

and \(\psi\) is supported in the unit disk of the two transverse variables.

Then:

\[
\boxed{
\int_C f_\delta\,ds
\sim1,
}
\tag{5.1}
\]

but:

\[
\boxed{
\int_{T_\ell(C)}
f_\delta\,dx
\sim
\delta^2
}
\tag{5.2}
\]

for:

\[
\delta\ll\ell.
\]

Hence:

\[
\boxed{
\Theta_{\rm tr}
\sim
\left(
\frac{\ell}{\delta}
\right)^2
\to\infty.
}
\tag{5.3}
\]

At the same time:

\[
\boxed{
\frac1{\ell^2}
\int_{T_\ell(C)}
f_\delta\,dx
\sim
\left(
\frac{\delta}{\ell}
\right)^2
\to0.
}
\tag{5.4}
\]

Thus a smooth codimension-two concentration can have:

- order-one line trace;
- vanishing tube-normalized volumetric mass.

Therefore no inequality of the form

\[
\boxed{
\int_C f
\le
C\ell^{-2}
\int_{T_\ell(C)}f
}
\]

holds uniformly for arbitrary smooth nonnegative \(f\).

This is only a functional-analytic countermodel.

It is **not** asserted that every such \(f_\delta\) is realizable as the actual Navier–Stokes derivative-compatible increment envelope.

---

# 6. Important correction to the D81 plan

D81 proposed:

> tube-thicken the surface/loop and apply the existing volumetric commutator detector.

D82 shows that this requires one extra input:

\[
\boxed{
\Theta_{\rm tr}\lesssim1.
}
\]

Without such an input, tube thickening is not a proof.

The reason is not merely surface curvature.

Even a perfectly straight, fixed material loop can support an arbitrary smooth trace concentration in a general field.

Therefore:

\[
\boxed{
\text{bounded loop geometry}
\not\Rightarrow
\text{bounded commutator trace ratio}.
}
\]

This distinction is essential.

---

# 7. Relation to the exact filtered-vorticity commutator estimate

The external/current filtered-vorticity theorem gives:

\[
\boxed{
|\nabla\cdot R_\ell|
\le
\frac{C_\varphi}{\ell}
\mathfrak M_{\ell,p}^2,
}
\]

and the volumetric scale-invariant detector:

\[
\boxed{
\widetilde{\mathcal S}_{r,\ell}^{(p)}
=
\frac r{\ell^2}
\iint
\mathfrak M_{\ell,p}^4.
}
\]

Its commutator insertion theorem controls volumetric pairings such as:

\[
\boxed{
r
\left|
\iint
\chi
\Omega_\ell
\cdot
(\nabla\times\nabla\cdot R_\ell)
\right|.
}
\]

D82 does not contradict that theorem.

It identifies a different functional:

\[
\boxed{
\int
\oint_C
\nabla\cdot R_\ell\cdot dy.
}
\]

The missing step is exactly a trace theorem from the volumetric increment envelope to the moving curve.

---

# 8. New minimal Kelvin visibility coordinate

Define:

\[
\boxed{
\mathsf R_{\rm tr}
}
\]

to mean:

\[
\boxed{
\Theta_{{\rm tr},n}\to\infty
}
\]

along a nonvanishing SGS-circulation branch.

Then the D81 Kelvin reduction becomes:

## Theorem D82.5 — Corrected Kelvin Terminal Reduction

\[
\boxed{
\mathsf R_K
\Longrightarrow
\widetilde{\mathcal S}^{(4)}_{\rm active}
\vee
\mathsf R_{\rm tr}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm tail}.
}
\tag{8.1}
\]

Here \(\mathsf R_{\rm tr}\) is not a new PDE force.

It is a **codimension-two visibility / concentration defect**.

---

# 9. Is \(\mathsf R_{\rm tr}\) already \(\mathsf R_{\rm fil}\)?

Not automatically.

If:

\[
\Theta_{\rm tr}\to\infty
\]

because the velocity-increment envelope narrows around the material loop at a transverse scale:

\[
\delta_n\ll\ell_n,
\]

then physically this resembles:

- vortex filament concentration;
- high-gradient tube formation;
- adaptive material-line selection.

But D82 does not yet prove the equivalence:

\[
\mathsf R_{\rm tr}
\subseteq
\mathsf R_{\rm fil}.
\]

The material loop itself may remain geometrically regular while the increment field concentrates around it.

Thus \(\mathsf R_{\rm tr}\) must be retained explicitly until a concentration/filamentation theorem is proved.

This is the principal correction of the round.

---

# 10. A sufficient transverse nonconcentration condition

Suppose there exists:

\[
C_{\rm nc}<\infty
\]

such that for every relevant \(n,t\):

\[
\boxed{
\ell_n^2
\int_{C_n(t)}
\mathfrak M_{\ell_n,4}^4\,ds
\le
C_{\rm nc}
\int_{T_{\ell_n}(C_n(t))}
\mathfrak M_{\ell_n,4}^4\,dx.
}
\tag{10.1}
\]

Then:

\[
\boxed{
\Theta_{{\rm tr},n}\le C_{\rm nc}.
}
\]

Consequently:

\[
\boxed{
\mathsf R_K
\Longrightarrow
\widetilde{\mathcal S}^{(4)}_{\rm active}
\vee
\text{known material noncompactness}.
}
\]

Therefore the entire Kelvin terminal branch is closed under one explicit transverse nonconcentration estimate.

This is now a sharply stated missing lemma.

---

# 11. Equivalent Morrey-trace formulation

Let:

\[
f_n
=
\mathfrak M_{\ell_n,4}^4.
\]

The desired estimate can be interpreted as a codimension-two material Morrey trace bound:

\[
\boxed{
\ell^2
\int_C f
\lesssim
\int_{T_\ell(C)}f.
}
\]

Equivalently, the average value of \(f\) on the material centerline is controlled by the average over its natural filter-scale cross section.

Failure means:

\[
\boxed{
\text{increment mass is more concentrated than the filter-scale tube}.
}
\]

Thus the Kelvin problem has now become a **transverse concentration problem**, not a second-order viscosity problem.

---

# 12. Relation to the native Morrey velocity bound

The native project Morrey law controls:

\[
\boxed{
\int_{B_R}|V|^2
\lesssim R.
}
\]

It does **not** directly control:

\[
\mathfrak M_{\ell,4}^4
\]

on a codimension-two moving trace.

Therefore D82 does not use the velocity Morrey bound to assert (10.1).

A new argument is needed.

Possible sources:

1. filtered diffusion;
2. direction-coherence / filament geometry;
3. local suitable-weak compactness;
4. a tube-Carleson estimate for derivative-compatible increments.

---

# 13. Candidate tube-Carleson detector

Define the material-tube concentration number:

\[
\boxed{
\mathfrak C_{\rm tube}
=
\sup_{C,\ell}
\frac{
\ell^2
\displaystyle\int\!\!\int_C
\mathfrak M_{\ell,4}^4
}{
\displaystyle\int\!\!\int_{T_\ell(C)}
\mathfrak M_{\ell,4}^4
}.
}
\]

A uniform theorem:

\[
\boxed{
\mathfrak C_{\rm tube}<\infty
}
\]

on the same-parent bounded-reservoir class would close \(\mathsf R_{\rm tr}\).

But D82 does not claim this theorem.

It identifies it as the exact missing trace compactness statement.

---

# 14. Better next attack than generic trace Sobolev theory

A generic Sobolev trace theorem from:

\[
L^2(\mathbb R^3)
\]

to a one-dimensional curve is impossible.

Even \(H^1\) is not enough for a generic codimension-two trace without stronger structure.

Therefore the next round should **not** try to prove (10.1) from generic \(L^2\) regularity.

The useful extra structure is:

\[
f_n
=
\mathfrak M_{\ell_n,4}^4,
\]

coming from actual velocity increments.

Possible exact routes:

- relate centerline increment concentration to transverse velocity-gradient energy;
- use Fubini on two-dimensional cross disks;
- prove that \(\Theta_{\rm tr}\to\infty\) forces a smaller transverse scale \(\delta_n\ll\ell_n\);
- reroot at \(\delta_n\);
- test whether the rerooted state creates:
  \[
  \mathsf R_{\rm fil},
  \quad
  \mathsf X,
  \quad
  \text{or a new bounded-reservoir descendant}.
  \]

This is the natural recursive-scale route.

---

# 15. Subfilter rerooting heuristic

If:

\[
\Theta_{{\rm tr},n}\to\infty,
\]

then the line sees much more increment mass than the \(\ell_n\)-tube average.

One expects the active transverse width:

\[
\delta_n
\]

to satisfy:

\[
\boxed{
\delta_n/\ell_n\to0.
}
\]

If such a \(\delta_n\) can be selected quantitatively, reroot at:

\[
\boxed{
r_n^{\rm new}\sim\delta_n.
}
\]

Then one of two things should happen:

1. the subfilter descendant has a nontrivial bounded normalized increment profile;
2. compactness fails through filamentation/concentration.

This is only the next program.

It is not yet proved.

---

# 16. Updated terminal compiler after the correction

D81 suggested:

\[
\mathsf O_{\rm PFET}
\wedge
(
\mathsf X
\vee
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_{\rm SGS\mbox{-}circ}
).
\]

D82 resolves \(\mathsf R_{\rm SGS\mbox{-}circ}\) into:

\[
\boxed{
\widetilde{\mathcal S}^{(4)}_{\rm active}
\vee
\mathsf R_{\rm tr}.
}
\]

Therefore the corrected late compiler is:

## Theorem D82.6 — Corrected Terminal Compiler

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\widetilde{\mathcal S}^{(4)}_{\rm active}
\vee
\mathsf R_{\rm tr}
\vee
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\right).
}
\tag{16.1}
\]

The Kelvin residue no longer appears as an independent second-order viscosity coordinate.

The genuinely unresolved new item is only the trace-concentration coordinate \(\mathsf R_{\rm tr}\).

---

# 17. Why this is still a major narrowing

The old terminal question was:

\[
\boxed{
\varepsilon_n
\int
\oint
\Delta v_n
\stackrel{?}{\longrightarrow}0.
}
\]

That involves second derivatives of the prelimit Navier–Stokes velocity and had no direct critical detector.

After D81–82 the question is:

\[
\boxed{
\text{can actual derivative-compatible velocity increment mass concentrate on a moving material line at a transverse scale }\ll\ell?
}
\]

This is a first-order increment / concentration question.

The differential order and the space of possibilities have both been reduced.

---

# 18. Status ledger

## PROVED this round

### D82-P1 — exact line-trace increment control

\[
|\mathfrak K_\ell^{\rm sgs}|^2
\lesssim
(r/\ell)^2
\widetilde{\mathcal S}_{C;r,\ell}^{(4)}.
\]

### D82-P2 — exact trace/volume factorization

\[
\widetilde{\mathcal S}_C
=
\Theta_{\rm tr}
\widetilde{\mathcal S}_T.
\]

### D82-P3 — bounded trace ratio absorbs Kelvin SGS flux into the existing volumetric increment detector.

### D82-P4 — nonzero SGS Kelvin flux with vanishing volumetric detector forces:

\[
\Theta_{\rm tr}\to\infty.
\]

### D82-P5 — generic unconditional volumetric-to-line trace control is false; explicit smooth codimension-two countermodel.

### D82-P6 — D81 tube-thickening plan requires an additional transverse nonconcentration hypothesis.

### D82-P7 — corrected Kelvin terminal reduction:

\[
R_K
\Longrightarrow
\widetilde{\mathcal S}^{(4)}_{\rm active}
\vee
R_{\rm tr}
\vee
\text{known material noncompactness}.
\]

---

# 19. What is not proved

D82 does not prove:

- \(R_{\rm tr}\) is impossible;
- \(R_{\rm tr}\subset R_{\rm fil}\);
- the native velocity Morrey law controls the line trace;
- a subfilter concentration scale \(\delta_n\) always exists with useful normalization;
- the trace ratio is uniformly bounded for actual Navier–Stokes increment envelopes.

These are the correct remaining statements.

---

# 20. New STOP

\[
\boxed{
\textbf{
STOP-D82:
The naive final absorption of Kelvin circulation into the existing volumetric commutator detector is false without an extra trace input. The exact SGS circulation is controlled by a scale-invariant material-line increment detector, and this detector factors as the ordinary tube-localized volumetric derivative-compatible increment defect times a dimensionless codimension-two trace ratio }\Theta_{\rm tr}\textbf{. Hence a nonzero Kelvin/SGS circulation with a vanishing existing volumetric detector forces }\Theta_{\rm tr}\to\infty\textbf{: derivative-compatible increment mass must concentrate on the moving material loop at a transverse scale below the filter scale. This is the precise remaining Kelvin gap. The second-order viscous residue has therefore been reduced to a first-order material-line trace-concentration problem, but that trace concentration is not yet proved equivalent to ordinary filamentation.}
}
\]

---

# 21. Next autonomous step

## DCRP83 / X72-R66 — Subfilter Rerooting from Material-Line Trace Concentration

**Working title**

> **Does \(\Theta_{\rm tr}\to\infty\) Force a Smaller Active Transverse Scale and a New Bounded-Reservoir Descendant?**

Primary tasks:

1. assume:
   \[
   \Theta_{{\rm tr},n}\to\infty;
   \]
2. examine two-dimensional transverse disks to \(C_n(t)\);
3. use layer-cake / radial maximal arguments to select:
   \[
   \delta_n\ll\ell_n;
   \]
4. prove a quantitative concentration statement for:
   \[
   \mathfrak M_{\ell_n,4}^4;
   \]
5. reroot the flow at \(\delta_n\);
6. test whether the new normalization yields:
   - a bounded nontrivial increment descendant;
   - an X72 pressure/tilt defect;
   - or explicit material filamentation/state compactness failure;
7. seek:
   \[
   R_{\rm tr}
   \Longrightarrow
   X
   \vee
   R_{\rm fil}
   \vee
   R_{\rm state}
   \vee
   \text{new bounded descendant}.
   \]

Desired endpoint:

\[
\boxed{
R_{\rm tr}
\Longrightarrow
\text{already-known finite-scale obstruction after subfilter rerooting}.
}
\]

---

# 22. One-line checkpoint

The Kelvin residue is now no longer a second-order mystery but a codimension-two trace problem: either the existing derivative-compatible commutator detector is active, or its increment mass concentrates increasingly tightly on the moving material loop, and that subfilter trace concentration is the only new minimal gap.

---

**End checkpoint:** DCRP82 / X72-R65  
**Next:** DCRP83 / X72-R66 — Subfilter Rerooting from Material-Line Trace Concentration.
