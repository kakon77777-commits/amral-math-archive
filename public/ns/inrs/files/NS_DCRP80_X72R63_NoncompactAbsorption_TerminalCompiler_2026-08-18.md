# DCRP80 / X72-R63 — Noncompact T Escape Absorption Audit and the Finite Terminal Defect Compiler

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-architecture checkpoint / terminal compiler audit  
**Immediate predecessor:** `NS_DCRP79_X72R62_SecularCompactChainNoGo_NoncompactCatalogue_2026-08-18.md`

**Primary internal dependencies**
- DCRP31 — mandatory finite-radius inward PFET
- DCRP33 — circulation replenishment / material tail / filamentation / viscous Kelvin shadowing
- DCRP59–60 — inward enstrophy turnover and X/T confluence
- DCRP62 — aligned pressure-response gap
- DCRP77–79 — dynamic T selection, coherent-return closure, secular compact-chain NO-GO

**Fresh external calibration**
- Gregory Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468 (2026): current Type-II analysis continues to use Euler scaling plus Liouville-type restrictions on extracted Euler objects.
- Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560 (2026): filtered stretching is controlled through direction defects, diffusion, commutator forcing, localization residuals, and critical generalized profiles.
- Runlong Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341 (2026): obstruction decompositions are not by themselves regularity theorems; the surviving defect must eventually be coupled to a coercive finite-scale estimate.

No external theorem is used to prove the internal absorption map below.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP79 proved that no \(E_p=0\), \(2\gamma\)-resonant infinite material chain can remain in a compact nonaligned normalized shape class.

Therefore any genuinely X-free continuation must lose compactness explicitly through one of the D79 modes:

1. alignment-boundary escape;
2. tilt blow-up;
3. strain-shape blow-up;
4. support/tail escape;
5. material filamentation / director oscillation;
6. packet multiplicity explosion;
7. singular/new-material injection;
8. or, when lifted back to the Navier–Stokes parent, a nonzero second-order viscous Kelvin residue.

DCRP80 audits whether these are genuinely new terminal mechanisms.

They are not.

Every D79 mode is absorbed by the pre-existing same-parent replenishment compiler of DCRP33.

Define four terminal coordinates:

\[
\boxed{
\mathsf R_{\rm tail}
}
\]

= normalized material support / ancestry escapes every finite supplier depth;

\[
\boxed{
\mathsf R_{\rm fil}
}
\]

= material filamentation / loss of spatial equicontinuity / direction-field complexity;

\[
\boxed{
\mathsf R_{\rm state}
}
\]

= state, loop, packet, shape, or multiplicity compactness fails;

\[
\boxed{
\mathsf R_K
}
\]

= nonvanishing second-order viscous Kelvin/circulation residue in the prelimit Navier–Stokes sequence.

Then the complete D79 absorption map is:

\[
\boxed{
\begin{array}{rcl}
\rho\to0
&\Longrightarrow&
\mathsf X\ \vee\ \mathsf R_{\rm state},
\\[1mm]
\rho\to\infty
&\Longrightarrow&
\mathsf R_{\rm fil}\ \vee\ \mathsf R_{\rm state},
\\[1mm]
|\lambda|+|a|+|b|\to\infty
&\Longrightarrow&
\mathsf R_{\rm state},
\\[1mm]
\text{support / ancestry escape}
&\Longrightarrow&
\mathsf R_{\rm tail},
\\[1mm]
\text{director oscillation / filamentation}
&\Longrightarrow&
\mathsf R_{\rm fil},
\\[1mm]
\text{packet multiplicity explosion}
&\Longrightarrow&
\mathsf R_{\rm state},
\\[1mm]
\text{singular/new-material injection}
&\Longrightarrow&
\mathsf R_{\rm state},
\\[1mm]
\limsup|\mathfrak K_n^{\rm visc}|>0
&\Longrightarrow&
\mathsf R_K.
\end{array}
}
\]

Thus no fifth late T terminal coordinate is created by D71–79.

The late X72/T chain has **reconverged exactly** to the older same-parent material-replenishment architecture.

---

# 1. Mandatory PFET remains orthogonal to the terminal alternatives

D31 gives, for every nonzero strict compact DSS strong profile in the current branch, a finite-radius inward physical pressure–kinetic energy flux.

Therefore the correct terminal statement is not merely a disjunction.

It is:

\[
\boxed{
\mathsf O_{\rm PFET}
\quad\wedge\quad
\left(
\mathsf X
\vee
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_K
\right).
}
\tag{1.1}
\]

PFET is a simultaneous core-tail matching obligation.

It is not interchangeable with any one material/pressure terminal defect.

This preserves the D49/D59 independence warnings.

---

# 2. Alignment-boundary escape

D79 mode A is:

\[
\boxed{
\rho=|D_s\xi|\to0.
}
\]

There are two possibilities.

## A1. aligned state becomes recurrent/compact

Then the carrier approaches

\[
D_s\xi=0,
\]

and if the aligned same-parent scalar shape returns, D62 gives the signed axial pressure-response obstruction:

\[
\boxed{
\int
\xi^\top E_p\xi\,ds<0.
}
\]

Hence:

\[
\boxed{
\text{compact recurrent alignment boundary}
\Longrightarrow
\mathsf X.
}
\]

## A2. alignment is only approached asymptotically and never closes

Then the local material-state chart degenerates without producing a recurrent aligned state.

This is exactly:

\[
\boxed{
\mathsf R_{\rm state}.
}
\]

So alignment-boundary escape introduces no new branch.

---

# 3. Tilt blow-up

D79 mode B is:

\[
\boxed{
\rho=|D_s\xi|\to\infty.
}
\]

If the blow-up is accompanied by spatial loss of direction-field compactness, it is:

\[
\boxed{
\mathsf R_{\rm fil}.
}
\]

If it is a purely local moving-frame shape blow-up without an identified spatial filament, the normalized packet state still leaves every compact shape set:

\[
\boxed{
\mathsf R_{\rm state}.
}
\]

Therefore:

\[
\boxed{
\rho\to\infty
\Longrightarrow
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}.
}
\tag{3.1}
\]

D77's finite threshold-crossing theorem supplies an additional fact: if the large tilt is dynamically generated while the axial X72 response remains small, a definite tilt action has already been paid.

But D80 does not need to rename that action as a new terminal coordinate.

---

# 4. Strain-shape blow-up

D79 mode C is:

\[
\boxed{
|\lambda|+|a|+|b|\to\infty.
}
\]

These variables are normalized components of the local strain/tilt shape.

Their unboundedness means the material state leaves every declared compact normalized shape class.

Therefore:

## Theorem D80.1 — Shape Blow-up Absorption

\[
\boxed{
\text{normalized strain-shape blow-up}
\Longrightarrow
\mathsf R_{\rm state}.
}
\tag{4.1}
\]

No separate “shape blow-up terminal branch” is required.

---

# 5. Support escape and infinite preselection

D79 mode D is normalized support escape.

D77/D79 also identified the pure-preselection route: if every finite annulus only selects already-high-stretch material, the origin of that high-stretch material is pushed indefinitely upstream.

Both have the same meaning in the same-parent compiler:

\[
\boxed{
\text{material ancestry leaves every finite normalized depth}.
}
\]

That is exactly DCRP33's:

\[
\boxed{
\mathsf R_{\rm tail}
=
\text{material tail escape / tail-fed replenishment}.
}
\]

Therefore:

## Theorem D80.2 — Preselection / Tail Absorption

\[
\boxed{
\mathsf T_{\rm preselect}^{\infty}
\subseteq
\mathsf R_{\rm tail}.
}
\tag{5.1}
\]

This is not a compact equality state.

---

# 6. Material filamentation / director oscillation

D79 mode E is:

\[
\boxed{
\|\nabla\xi_n\|,
\quad
\|\nabla S_n\|,
\quad
\text{or material-line complexity}
\to\infty.
}
\]

This is exactly the existing DCRP33 material-filamentation branch:

\[
\boxed{
\mathsf R_{\rm fil}.
}
\]

The 2026 filtered-vortex-stretching literature is consistent with this classification: direction incoherence, commutators, and localization residuals are natural finite-scale defects, but their existence alone is not a regularity contradiction.

Thus:

## Theorem D80.3 — Filamentation Absorption

\[
\boxed{
\text{director/spatial equicontinuity loss}
\Longrightarrow
\mathsf R_{\rm fil}.
}
\tag{6.1}
\]

---

# 7. Packet multiplicity explosion

D79 mode F is an unbounded number of descendant packets / selector components.

A finite same-parent material compiler cannot identify a single strongly convergent return map when the number of relevant material components diverges.

This is precisely a packet/state compactness failure:

\[
\boxed{
\mathsf R_{\rm state}.
}
\]

Thus:

## Theorem D80.4 — Multiplicity Absorption

\[
\boxed{
N_{\rm packets}\to\infty
\Longrightarrow
\mathsf R_{\rm state}.
}
\tag{7.1}
\]

Multiplicity does not require its own terminal coordinate.

---

# 8. Singular/new-material injection

D77 mode C / D79 mode G occurs when the outgoing carrier measure is not absolutely continuous with respect to the incoming material measure.

This is explicit failure of closed material shadowing.

Hence:

\[
\boxed{
\text{singular material injection}
\Longrightarrow
\mathsf R_{\rm state}.
}
\tag{8.1}
\]

It remains physically a turnover event, but at the terminal compiler level it is already a state/transition mismatch.

---

# 9. Prelimit viscous Kelvin residue

The Navier–Stokes material circulation satisfies:

\[
\boxed{
\frac d{d\tau}
\Gamma_n(\tau)
=
\varepsilon_n
\oint_{C_n(\tau)}
\Delta v_n\cdot dy.
}
\]

The one-period residue is:

\[
\boxed{
\mathfrak K_n^{\rm visc}(C)
=
\varepsilon_n
\int_0^{S_0}
\oint_{C_n(\tau)}
\Delta v_n\cdot dy\,d\tau.
}
\tag{9.1}
\]

Even if:

\[
\varepsilon_n\to0,
\]

the residue need not vanish because the second derivatives can diverge.

Thus:

\[
\boxed{
\limsup_n
|\mathfrak K_n^{\rm visc}|
>0
}
\]

is the already-declared prelimit coordinate:

\[
\boxed{
\mathsf R_K.
}
\]

This is the only D79 terminal coordinate that is genuinely Navier–Stokes-specific rather than an Euler material noncompactness.

---

# 10. Exact D33 compiler recovered

DCRP33's compact same-parent normal form was:

\[
\boxed{
\text{material tail escape}
\vee
\text{material filamentation}
\vee
\text{second-order viscous circulation residue}
\vee
\text{state/loop transition mismatch}.
}
\]

D80 shows that the late D71–79 X72/T sequence produces **exactly the same terminal list**.

Therefore:

## Theorem D80.5 — Late/Old Compiler Confluence

\[
\boxed{
\mathsf T_{\rm noncomp}^{\rm D79}
\subseteq
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_K.
}
\tag{10.1}
\]

Conversely, each right-hand coordinate is already a legitimate way for same-parent material compactness/shadowing to fail.

Thus, at the current taxonomy resolution:

\[
\boxed{
\mathsf T_{\rm noncomp}^{\rm terminal}
=
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_K.
}
\tag{10.2}
\]

No new terminal material mechanism was created by the late X72 analysis.

---

# 11. Terminal rank-two compiler

Combine D31, D62, D79, and D80.

## Theorem D80.6 — Finite Terminal Compiler

Every surviving strict same-parent rank-two branch in the present project architecture satisfies:

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\mathsf R_{\rm tail}
\vee
\mathsf R_{\rm fil}
\vee
\mathsf R_{\rm state}
\vee
\mathsf R_K
\right).
}
\tag{11.1}
\]

Interpretation:

### \(\mathsf X\)

finite active pressure/cofactor/tilt/transport defect;

### \(\mathsf R_{\rm tail}\)

material ancestry/support escapes to the mandatory critical tail;

### \(\mathsf R_{\rm fil}\)

material lines/directors filament or lose strong spatial compactness;

### \(\mathsf R_{\rm state}\)

shape, packet, loop, multiplicity, or injection prevents same-state material shadowing;

### \(\mathsf R_K\)

a second-order viscous circulation correction survives the Euler-scaling limit.

This is a finite terminal list.

---

# 12. What has actually been closed by D61–80

The late chain has closed all compact/equality-style material escape routes generated after the X/T split:

- aligned-neutral pressure-perfect recurrence;
- phase-lock pressure-perfect recurrence;
- global phase-lock;
- critical twisting cylinder;
- zero-stretch counterflow conveyor;
- finite \(2\gamma\) material cycles;
- coherent resonant aligned carriers;
- coherent resonant tilted carriers;
- compact infinite pressure-perfect resonant drift.

Therefore:

\[
\boxed{
\textbf{
there is no compact X-free T equality state left in this rank-two chain.
}
}
\]

What remains is explicitly noncompact or prelimit-viscous.

---

# 13. This is classification, not Navier–Stokes regularity

D80 does **not** prove:

\[
\mathsf R_{\rm tail}=\varnothing,
\]

or:

\[
\mathsf R_{\rm fil}=\varnothing,
\]

or:

\[
\mathsf R_{\rm state}=\varnothing,
\]

or:

\[
\mathsf R_K=\varnothing.
\]

The fresh 2026 literature reinforces the same methodological warning:

> identifying an obstruction/defect coordinate is not the same as proving a coercive estimate that excludes it.

The remaining task is now accurately stated as a **finite list of quantitative proof obligations**.

---

# 14. Priority audit

Among the four terminal T coordinates:

## \(\mathsf R_{\rm tail}\)

is an Euler material noncompactness already coupled to mandatory PFET and critical tail geometry.

## \(\mathsf R_{\rm fil}\)

is an Euler material/spatial compactness failure and has modern filtered-vortex-stretching/direction-defect tools available.

## \(\mathsf R_{\rm state}\)

is a generic material return/shadowing failure; by definition it is not a hidden compact equality mode.

## \(\mathsf R_K\)

is different.

It is the only terminal coordinate that may remain nonzero **even when the Euler material object itself is well-behaved**, because:

\[
\varepsilon_n\to0
\]

does not imply:

\[
\varepsilon_n\Delta v_n\to0
\]

on a material loop.

Therefore \(\mathsf R_K\) is the uniquely Navier–Stokes-specific late terminal branch.

---

# 15. Next target: second-order Kelvin residue

DCRP33 already identified the exact formula:

\[
\boxed{
\mathfrak K_n^{\rm visc}(C)
=
\varepsilon_n
\int_0^{S_0}
\oint_{C_n(\tau)}
\Delta v_n\cdot dy\,d\tau.
}
\]

The next question is:

> can a nonvanishing \(\mathfrak K_n^{\rm visc}\) be absorbed into the modern filtered vortex-stretching / commutator / direction-defect coordinates, or does it define a genuinely independent second-order Navier–Stokes obstruction?

Stokes' theorem suggests:

\[
\oint_C
\Delta v\cdot dy
=
\int_{\Sigma_C}
\Delta\omega\cdot n\,dA
\]

for a smoothly spanned material surface.

This creates a direct candidate bridge between:

- Kelvin residue;
- second derivatives of vorticity;
- filtered diffusion;
- direction incoherence / filamentation;
- annular supplier action.

That is now the highest-leverage next calculation.

---

# 16. Status ledger

## PROVED / established by absorption this round

### D80-P1

Alignment-boundary escape is \(X\) or \(\mathsf R_{\rm state}\).

### D80-P2

Tilt blow-up is \(\mathsf R_{\rm fil}\) or \(\mathsf R_{\rm state}\).

### D80-P3

Strain-shape blow-up is \(\mathsf R_{\rm state}\).

### D80-P4

Infinite preselection/support escape is \(\mathsf R_{\rm tail}\).

### D80-P5

Director/spatial filamentation is \(\mathsf R_{\rm fil}\).

### D80-P6

Packet multiplicity explosion is \(\mathsf R_{\rm state}\).

### D80-P7

Singular material injection is \(\mathsf R_{\rm state}\).

### D80-P8

Prelimit second-order circulation residue is \(\mathsf R_K\).

### D80-P9

The D79 late noncompact catalogue introduces no new terminal mechanism beyond DCRP33.

### D80-P10

Finite terminal rank-two compiler:

\[
\boxed{
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
\mathsf R_K
).
}
\]

---

# 17. New STOP

\[
\boxed{
\textbf{
STOP-D80:
The late X72/T investigation has now fully reconverged to the pre-existing same-parent replenishment compiler. Every D79 X-free noncompact escape is already one of four terminal coordinates: material-tail/ancestry escape, material filamentation, state/loop/packet compactness failure, or the prelimit second-order viscous Kelvin residue. Thus no compact X-free T equality state and no new fifth terminal material mechanism remain. Every strict rank-two survivor simultaneously carries inward PFET and one of }X\textbf{, }R_{\rm tail}\textbf{, }R_{\rm fil}\textbf{, }R_{\rm state}\textbf{, or }R_K\textbf{. Among these, }R_K\textbf{ is the uniquely Navier–Stokes-specific late branch and is therefore the next highest-leverage target.}
}
\]

---

# 18. Next autonomous step

## DCRP81 / X72-R64 — Second-Order Kelvin Residue / Filtered Diffusion Bridge

**Working title**

> **Can the Viscous Kelvin Residue Be Absorbed into Filtered Vorticity-Diffusion, Direction-Incoherence, or Supplier Defects?**

Primary tasks:

1. start from
   \[
   \mathfrak K_n^{\rm visc}
   =
   \varepsilon_n
   \int
   \oint_{C_n}
   \Delta v_n\cdot dy\,ds;
   \]
2. span \(C_n\) by controlled material surfaces \(\Sigma_n\);
3. use
   \[
   \oint_C\Delta v\cdot dy
   =
   \int_{\Sigma_C}\Delta\omega\cdot n\,dA;
   \]
4. introduce a finite-scale mollifier / tube localization;
5. compare the residue with:
   - filtered vorticity diffusion;
   - filtered vortex-stretching direction defects;
   - differentiated commutator forcing;
   - material filamentation of the loop surface;
6. prove an alternative:
   \[
   |\mathfrak K_n^{\rm visc}|
   \not\to0
   \Longrightarrow
   \mathsf R_{\rm fil}
   \vee
   \mathsf R_{\rm diff}
   \vee
   \mathsf R_{\rm comm}
   \vee
   \text{one explicit second-order equality mode};
   \]
7. test whether every right-hand coordinate is already in the existing finite compiler.

Desired endpoint:

\[
\boxed{
\mathsf R_K
\Longrightarrow
\text{known finite-scale defect}
\vee
\text{one explicit irreducible Kelvin residue mode}.
}
\]

---

# 19. One-line checkpoint

The late material-turnover branch is no longer an open-ended geometry problem: all X-free noncompact exits have been absorbed into the old four-coordinate same-parent compiler, leaving the second-order viscous Kelvin residue as the uniquely Navier–Stokes-specific terminal branch to attack next.

---

**End checkpoint:** DCRP80 / X72-R63  
**Next:** DCRP81 / X72-R64 — Second-Order Kelvin Residue / Filtered Diffusion Bridge.
