# DCRP94 / X72-R77 — Finite-State Kelvin Reset Graph and the Nonpositive-Homogeneity Sidecar Theorem

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / nonpositive-homogeneity regeneration witness round  
**Immediate predecessor:** `NS_DCRP93_X72R76_HomogeneitySign_CriticalReplacementConveyor_2026-08-19.md`

**Primary internal dependencies**
- DCRP32–33 — DSS Kelvin holonomy / circulation replenishment
- DCRP81–85 — mesoscopic Kelvin decomposition / SGS circulation / trace / scale absorption
- DCRP88 — finite circulation-atom family and finite ancestry depth
- DCRP92 — finite joint detector / positive-density recurrence
- DCRP93 — homogeneity-sign principle / positive-homogeneity work conveyor

**Fresh primary-source calibration**
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570.
- G. L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159.
- G. L. Eyink, *Turbulent Cascade of Circulations*, arXiv:physics/0605014.
- D. W. Boutros, E. S. Titi, *On the conservation of helicity by weak solutions of the 3D Euler and inviscid MHD equations*, arXiv:2410.00813.

The first source supplies the self-similar Kelvin scaling law.  
Eyink's work calibrates the interpretation of coarse-grained SGS circulation flux.  
The helicity source is used only to audit the secondary helicity candidate; D94 does not assume unconditional helicity conservation in the present singular/vanishing-viscosity branch.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP93 isolated the last compact accounting survivor:

\[
\boxed{
\mathsf C_{\rm work}^{+h}
}
\]

= a positive-homogeneity critical replacement conveyor.

Its defining feature is that normalized work/residual badness can recur at positive generation density while the corresponding physical work cost scales like:

\[
\ell_n^p,
\qquad
p>0,
\]

and is therefore geometrically summable.

DCRP94 proves that **a pure positive-homogeneity conveyor cannot be the full same-parent regeneration mechanism**.

The missing sidecar is circulation reset.

D88 supplies a finite family of circulation-observing loop states and:

\[
\boxed{
c_\Gamma>0.
}
\]

Strict Type-II Kelvin holonomy has:

\[
\boxed{
0<\rho_\Gamma
=
e^{-(1-2\gamma)S_0}
<1.
}
\]

Whenever one active loop state is material-shadowed to the next active loop state, define the normalized one-generation Kelvin reset:

\[
\boxed{
\delta_n
:=
\Gamma_{n+1}
-
\rho_\Gamma\Gamma_n.
}
\tag{0.1}
\]

If no state/carrier replacement occurs, an infinite material-state path lives in a **finite** active-loop graph.

Every sufficiently short block therefore contains a repeated state.

On a repeated-state cycle of length:

\[
1\le q\le M,
\]

one has:

\[
\boxed{
\Gamma_{n+q}
=
\rho_\Gamma^q\Gamma_n
+
\sum_{j=0}^{q-1}
\rho_\Gamma^{q-1-j}
\delta_{n+j}.
}
\tag{0.2}
\]

If the same loop state returns exactly, then:

\[
\Gamma_{n+q}=\Gamma_n.
\]

Hence:

\[
\boxed{
(1-\rho_\Gamma^q)\Gamma_n
=
\sum_{j=0}^{q-1}
\rho_\Gamma^{q-1-j}
\delta_{n+j}.
}
\tag{0.3}
\]

Since:

\[
|\Gamma_n|\ge c_\Gamma,
\]

\[
1-\rho_\Gamma^q
\ge
1-\rho_\Gamma,
\]

we obtain:

\[
\boxed{
\sum_{j=0}^{q-1}
|\delta_{n+j}|
\ge
(1-\rho_\Gamma)c_\Gamma.
}
\tag{0.4}
\]

Therefore one reset in the cycle satisfies:

\[
\boxed{
|\delta_{n+j_*}|
\ge
\delta_*
:=
\frac{
(1-\rho_\Gamma)c_\Gamma
}{
M
}
>0.
}
\tag{0.5}
\]

Thus:

# Main theorem — finite-state Kelvin reset sidecar

\[
\boxed{
\text{infinite compact same-parent regeneration}
\Longrightarrow
R_{\rm rep/state}
\vee
\mathsf C_{\Gamma{\rm -reset}}^0.
}
\tag{0.6}
\]

Here:

\[
\boxed{
\mathsf C_{\Gamma{\rm -reset}}^0
}
\]

means a **uniform normalized circulation reset event** occurring at positive generation density.

This is the nonpositive-homogeneity witness requested by D93.

Its normalized generation exponent is:

\[
\boxed{
p_{\rm reset}^{\rm norm}=0,
}
\]

while the corresponding physical circulation scale is:

\[
\boxed{
p_\Gamma=1-\alpha<0.
}
\]

So a pure \(p>0\) work conveyor is impossible.

It must be accompanied by:

- material/carrier replacement noncompactness;
- or a \(p\le0\) circulation-reset conveyor.

---

# 1. Finite active-loop state family

D88 proves on a compact resolved-bad class that there exist finitely many loop templates:

\[
C_1,\ldots,C_M
\]

and:

\[
c_\Gamma>0
\]

such that every normalized phase package has some active loop satisfying:

\[
\boxed{
\max_{1\le i\le M}
\left|
\oint_{C_i}U\cdot dy
\right|
\ge
c_\Gamma.
}
\tag{1.1}
\]

Call the selected active loop state at generation \(n\):

\[
a_n\in\{1,\ldots,M\}.
\]

This is a finite observable state alphabet.

---

# 2. Material-shadowed edge versus replacement edge

Let:

\[
\Phi_n
\]

be the one-period similarity material map at generation \(n\).

A transition:

\[
a_n\to a_{n+1}
\]

is called **material-shadowed** if the selected successor loop is identified, within the declared compact loop-state tolerance, with:

\[
\Phi_n(C_{a_n}).
\]

If this fails, record:

\[
\boxed{
R_{\rm rep}.
}
\tag{2.1}
\]

This includes:

- new carrier selection;
- packet replacement;
- loop-topology mismatch;
- failure of material labeling;
- finite-state shadowing failure.

At the terminal compiler level:

\[
\boxed{
R_{\rm rep}
\subseteq
R_{\rm state}.
}
\tag{2.2}
\]

D94 therefore studies only the complementary material-shadowed path.

---

# 3. Exact normalized reset recurrence

On a material-shadowed edge define algebraically:

\[
\boxed{
\delta_n
=
\Gamma_{n+1}
-
\rho_\Gamma\Gamma_n.
}
\tag{3.1}
\]

For exact Euler Kelvin shadowing:

\[
\delta_n=0.
\]

For the prelimit Navier–Stokes sequence, \(\delta_n\) measures exactly the failure of ideal DSS Kelvin contraction after the phase/scale renormalization.

Iterating gives:

## Theorem D94.1 — Reset Duhamel Formula

For every \(q\ge1\),

\[
\boxed{
\Gamma_{n+q}
=
\rho_\Gamma^q\Gamma_n
+
\sum_{j=0}^{q-1}
\rho_\Gamma^{q-1-j}
\delta_{n+j}.
}
\tag{3.2}
\]

This is purely algebraic.

---

# 4. Repeated loop state forces reset

Suppose:

\[
a_{n+q}=a_n
\]

and the normalized same-parent state is exact at the two endpoints.

Then:

\[
\Gamma_{n+q}=\Gamma_n.
\]

Use (3.2):

\[
(1-\rho_\Gamma^q)\Gamma_n
=
\sum_{j=0}^{q-1}
\rho_\Gamma^{q-1-j}\delta_{n+j}.
\]

Take absolute values:

\[
(1-\rho_\Gamma^q)|\Gamma_n|
\le
\sum_{j=0}^{q-1}
|\delta_{n+j}|.
\]

Since:

\[
|\Gamma_n|\ge c_\Gamma,
\]

we obtain:

## Theorem D94.2 — Cycle Reset Debt

\[
\boxed{
\sum_{j=0}^{q-1}
|\delta_{n+j}|
\ge
(1-\rho_\Gamma^q)c_\Gamma.
}
\tag{4.1}
\]

In particular:

\[
\boxed{
\sum_{j=0}^{q-1}
|\delta_{n+j}|
\ge
(1-\rho_\Gamma)c_\Gamma.
}
\tag{4.2}
\]

---

# 5. One uniform reset event per finite-state cycle

Because:

\[
q\le M,
\]

(4.2) implies:

## Corollary D94.3 — Uniform Reset Atom

There exists:

\[
j_*\in\{0,\ldots,q-1\}
\]

such that:

\[
\boxed{
|\delta_{n+j_*}|
\ge
\frac{
(1-\rho_\Gamma)c_\Gamma
}{
M
}
=:
\delta_*.
}
\tag{5.1}
\]

The lower bound is independent of the physical generation scale.

---

# 6. Positive-density reset theorem

Consider disjoint blocks of:

\[
M+1
\]

successive active states.

Inside every block:

- either at least one transition is not material-shadowed:
  \[
  R_{\rm rep};
  \]
- or all transitions are shadowed.

In the second case the block contains \(M+1\) states in an \(M\)-state alphabet, so some state repeats.

The subpath between the repeated occurrences has length:

\[
q\le M,
\]

and D94.3 produces:

\[
|\delta|\ge\delta_*.
\]

Therefore:

## Theorem D94.4 — Replacement/Reset Density Dichotomy

Along an infinite active-loop chain, at least one of:

\[
\boxed{
R_{\rm rep}
}
\]

or:

\[
\boxed{
|\delta_n|\ge\delta_*
}
\]

occurs with upper generation density at least:

\[
\boxed{
\frac1{M+1}.
}
\tag{6.1}
\]

After finite-type pigeonholing, one fixed replacement or reset coordinate recurs infinitely often at positive density.

---

# 7. Robust approximate-state version

Exact equality of the repeated loop state is stronger than necessary.

Suppose a repeated finite-state cell satisfies:

\[
\boxed{
|\Gamma_{n+q}-\Gamma_n|
\le
\varepsilon_{\rm cyc}.
}
\tag{7.1}
\]

Then:

\[
\sum_{j=0}^{q-1}
|\delta_{n+j}|
\ge
(1-\rho_\Gamma^q)|\Gamma_n|
-
\varepsilon_{\rm cyc}.
\]

If the state cover is chosen so that:

\[
\boxed{
\varepsilon_{\rm cyc}
\le
\frac12
(1-\rho_\Gamma)c_\Gamma,
}
\tag{7.2}
\]

then:

## Theorem D94.5 — Robust Reset Gap

\[
\boxed{
\sum_{j=0}^{q-1}
|\delta_{n+j}|
\ge
\frac12
(1-\rho_\Gamma)c_\Gamma.
}
\tag{7.3}
\]

Hence one event satisfies:

\[
\boxed{
|\delta|
\ge
\frac{
(1-\rho_\Gamma)c_\Gamma
}{
2M
}.
}
\tag{7.4}
\]

Thus the result survives finite compact-state discretization.

---

# 8. Mesoscopic Navier–Stokes meaning of \(\delta_n\)

D81 filtered the normalized Navier–Stokes sequence at a mesoscopic scale and obtained the exact filtered Kelvin law:

\[
\frac d{d\tau}
\Gamma_{n,\ell}
=
\varepsilon_n
\oint_{C_{n,\ell}}
\Delta U_{n,\ell}\cdot dy
-
\oint_{C_{n,\ell}}
\nabla\cdot R_{n,\ell}\cdot dy.
\]

After one normalized period and phase/scale matching, the deviation from the ideal holonomy can only be carried by:

1. filtered viscous circulation;
2. SGS circulation flux;
3. loop/state shadowing mismatch.

Therefore schematically:

\[
\boxed{
\delta_n
=
\delta_n^{\rm fvisc}
+
\delta_n^{\rm SGS}
+
\delta_n^{\rm shadow}.
}
\tag{8.1}
\]

This is not used as a universal pointwise equality outside the declared mesoscopic shadowing setup.

It is the D81 prelimit interpretation of the normalized reset.

---

# 9. If shadowing carries the reset

If:

\[
|\delta_n^{\rm shadow}|
\ge
c>0
\]

on positive density, then material/loop phase matching repeatedly fails.

Therefore:

\[
\boxed{
\delta^{\rm shadow}
\Longrightarrow
R_{\rm state}.
}
\tag{9.1}
\]

No compact equality conveyor exists in this branch.

---

# 10. If filtered viscosity carries the reset

D81 chose mesoscopic filters for which the explicit filtered viscous circulation term vanishes under the compact branch assumptions.

If that vanishing fails, the sequence has entered the already-declared:

- second-order viscous Kelvin residue;
- filter-ratio;
- gradient concentration;
- state/scale escape

architecture.

D81–85 have already absorbed those possibilities.

Therefore no new terminal is introduced here.

---

# 11. SGS reset branch

On the compact mesoscopic branch, a persistent reset gap therefore forces:

\[
\boxed{
|\delta_n^{\rm SGS}|
\ge
c_{\rm SGS}>0
}
\tag{11.1}
\]

along a positive-density subsequence.

D81 identifies the SGS circulation as:

\[
\boxed{
-\int
\oint_{C_{n,\ell}}
\nabla\cdot R_{n,\ell}\cdot dy\,d\tau,
}
\]

equivalently as the spanning-surface flux of:

\[
\boxed{
-\nabla\times\nabla\cdot R_{n,\ell}.
}
\]

D82–85 then reduce persistent SGS Kelvin circulation to:

\[
\boxed{
\widetilde{\mathcal S}_{\rm active}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{11.2}
\]

D92 already compresses the first two into the finite joint detector.

Thus the Kelvin reset sidecar is not a new infinite-dimensional defect tree.

---

# 12. Nonpositive homogeneity

The normalized reset:

\[
\delta_n
\]

is dimensionless with respect to the generation state graph.

Its generation homogeneity is:

\[
\boxed{
p_{\rm reset}^{\rm norm}=0.
}
\tag{12.1}
\]

The corresponding physical circulation scales as:

\[
\Gamma_{\rm phys}
\sim
\ell^{1-\alpha}\Gamma_{\rm norm}.
\]

Hence:

\[
\boxed{
p_\Gamma
=
1-\alpha
<
0.
}
\tag{12.2}
\]

Therefore a uniform normalized reset:

\[
|\delta_n|\ge\delta_*
\]

does not become physically cheaper at smaller scales.

Its physical circulation amplitude instead scales like:

\[
\boxed{
|\delta_n^{\rm phys}|
\gtrsim
\ell_n^{1-\alpha}\delta_*,
}
\]

which grows as:

\[
\ell_n\downarrow0.
\]

This is qualitatively different from the D93 \(p>0\) work conveyor.

---

# 13. Pure positive-homogeneity conveyor is impossible

D93 allowed an accounting normal form:

\[
\mathsf C_{\rm work}^{+h}
\]

in which the only repeated visible mechanism was positive-homogeneity work.

D94 now adds the circulation state.

If the bad state continues indefinitely:

- either the active circulation carrier repeatedly fails material shadowing:
  \[
  R_{\rm state};
  \]
- or the finite material-state graph forces:
  \[
  \mathsf C_{\Gamma{\rm -reset}}^0.
  \]

Therefore:

## Theorem D94.6 — Nonpositive-Homogeneity Sidecar

\[
\boxed{
\mathsf C_{\rm work}^{+h}
\Longrightarrow
R_{\rm state}
\vee
\mathsf C_{\Gamma{\rm -reset}}^0.
}
\tag{13.1}
\]

The critical replacement conveyor cannot be purely energetic.

It must continually reset a Kelvin quantity or continually replace its material carrier.

---

# 14. Exact algebraic reset conveyor

D94 does **not** claim that a uniform \(p=0\) reset is already a contradiction.

Indeed consider:

\[
\boxed{
\Gamma_{n+1}
=
\rho_\Gamma\Gamma_n
+
(1-\rho_\Gamma)\Gamma_*.
}
\tag{14.1}
\]

If:

\[
\Gamma_0=\Gamma_*,
\]

then:

\[
\boxed{
\Gamma_n=\Gamma_*
\qquad
\forall n.
}
\tag{14.2}
\]

The reset is:

\[
\boxed{
\delta_n
=
(1-\rho_\Gamma)\Gamma_*.
}
\tag{14.3}
\]

Thus:

- the normalized circulation state remains bounded;
- the reset total variation grows linearly in generation number.

This is an exact **Kelvin Reset Conveyor** at the recurrence-equation level.

So:

## STOP

\[
\boxed{
p=0
\text{ reset recurrence}
\not\Rightarrow
\text{contradiction without a finite reset capacity}.
}
\tag{14.4}
\]

D94 has changed the homogeneity class of the final problem, but has not yet supplied the finite global capacity.

---

# 15. Why helicity is not yet the missing capacity

A scale-local helicity quantity has:

\[
\boxed{
p_H
=
2-2\alpha
<
0.
}
\]

This is attractive by the D93 homogeneity criterion.

However the present branch does not provide a uniform nonzero helicity atom from:

\[
|\Gamma|\ge c_\Gamma.
\]

A flow may have:

- nonzero local circulations;
- but zero total helicity through sign cancellation or unlinked geometry.

Moreover:

- global helicity need not be finite on the critical DSS tail;
- weak Euler helicity conservation requires regularity hypotheses;
- zero-viscosity Navier–Stokes helicity conservation also needs additional assumptions.

Therefore:

## Theorem D94.7 — Helicity Candidate STOP

D94 cannot replace the Kelvin reset ledger by helicity without an additional:

\[
\boxed{
\text{linking / sign / finite-helicity capacity hypothesis}.
}
\]

Helicity remains a secondary candidate only.

---

# 16. Reset source graph

The final compact regeneration mechanism may now be represented as:

\[
\boxed{
\text{normalized bad state}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Kelvin contraction by }\rho_\Gamma
}
\]

\[
\downarrow
\]

to restore:

\[
|\Gamma|\ge c_\Gamma,
\]

one needs:

\[
\boxed{
\text{carrier replacement}
\vee
\text{Kelvin reset}.
}
\]

The reset itself must be supplied through:

\[
\boxed{
\text{SGS circulation}
\vee
\text{viscous circulation}
\vee
\text{shadow/state mismatch}.
}
\]

After D81–85:

\[
\boxed{
\text{Kelvin reset}
\Longrightarrow
\text{existing finite joint defect}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

This is the current complete regeneration graph.

---

# 17. Positive-density reset frequency

Let the active loop graph have:

\[
M
\]

states.

Partition generations into disjoint blocks of:

\[
M+1.
\]

Each block contains:

- a replacement transition;
- or a reset event with:
  \[
  |\delta|\ge\delta_*.
  \]

Therefore for the union event set:

\[
\mathcal A_{\rm rep/reset},
\]

\[
\boxed{
\liminf_{N\to\infty}
\frac{
\#(
\mathcal A_{\rm rep/reset}
\cap[0,N)
)
}{
N
}
\ge
\frac1{M+1}.
}
\tag{17.1}
\]

If replacement density vanishes, reset density itself satisfies the same asymptotic lower bound up to the finite-state splitting constants.

Thus the Kelvin sidecar is recurrent, not exceptional.

---

# 18. Relation to D92 joint detector

D92 already proves a positive-density finite joint detector coordinate.

D94 proves independently:

\[
\boxed{
\text{positive-density work/state regeneration}
}
\]

must be accompanied by:

\[
\boxed{
\text{positive-density circulation reset/replacement}.
}
\]

The two recurrence structures need not fire on exactly the same generation.

But their gaps are both uniformly bounded.

Therefore the late survivor now carries two finite recurrence clocks:

1. the finite work/residual detector clock;
2. the finite Kelvin reset/replacement clock.

This is stronger than D92 alone.

---

# 19. What has improved

Before D94 the last compact survivor could be described as:

> the flow repeatedly pays a positive normalized work tax, but the physical tax becomes cheaper at smaller scales.

After D94 that description is incomplete.

The same normalized state also contains a nonzero circulation atom.

Kelvin contraction tries to reduce it each period.

So every finite number of generations the branch must:

- inject/reset circulation through finite-scale SGS/viscous dynamics;
- or replace the material carrier.

This reset has nonpositive homogeneity.

Thus the positive-homogeneity replacement conveyor has acquired a mandatory nonpositive-homogeneity sidecar.

---

# 20. What remains genuinely open

The missing theorem is now:

> can the normalized Kelvin reset total variation be supplied indefinitely by SGS circulation while every reset source remains inside the already-bounded finite defect/state package?

Equivalently:

\[
\boxed{
\sum_n|\delta_n|
=
\infty
}
\]

is now forced on the pure compact reset conveyor.

But no globally finite quantity has yet been proved to dominate this sum.

This is the precise remaining capacity problem.

---

# 21. Status ledger

## PROVED this round

### D94-P1 — finite active circulation-state graph.

### D94-P2 — exact reset Duhamel formula:

\[
\Gamma_{n+q}
=
\rho_\Gamma^q\Gamma_n
+
\sum
\rho_\Gamma^{q-1-j}\delta_{n+j}.
\]

### D94-P3 — repeated active state forces cumulative reset:

\[
\sum|\delta|
\ge
(1-\rho_\Gamma)c_\Gamma.
\]

### D94-P4 — finite cycle gives one uniform reset atom:

\[
|\delta|\ge
(1-\rho_\Gamma)c_\Gamma/M.
\]

### D94-P5 — every \(M+1\) generation block contains either carrier replacement or a uniform reset event.

### D94-P6 — robust approximate-state version with a half-gap.

### D94-P7 — D81 identifies prelimit reset sources as viscous / SGS / shadowing coordinates on the mesoscopic branch.

### D94-P8 — D81–85 reduce persistent SGS reset to existing finite-scale defect/state/critical coordinates.

### D94-P9 — pure positive-homogeneity work conveyor requires a nonpositive-homogeneity reset/replacement sidecar.

### D94-P10 — explicit constant-circulation reset conveyor shows \(p=0\) reset alone is not yet a contradiction.

### D94-P11 — helicity is not yet a valid universal replacement capacity.

---

# 22. What is not proved

D94 does not prove:

- the Kelvin reset conveyor is impossible;
- \(\sum|\delta_n|\) is controlled by a finite global measure;
- SGS circulation reset has a scale-uniform efficiency lower bound against one signed D92 work coordinate;
- physical circulation reset has a finite global capacity;
- helicity is nonzero or finite on the survivor;
- carrier replacement itself has finite total variation;
- global Navier–Stokes regularity.

The final problem is now a **reset-source capacity problem**, not an energy-work summability problem.

---

# 23. New STOP

\[
\boxed{
\textbf{
STOP-D94:
The D93 positive-homogeneity critical replacement conveyor cannot exist as a purely energetic recurrence. The compact resolved-bad state carries a finite observable family of nonzero circulation atoms, while strict Type-II Kelvin holonomy contracts every material circulation by }\rho_\Gamma<1\textbf{ per DSS period. On a finite material-shadowed loop-state graph, every repeated state cycle obeys the reset Duhamel formula, and recurrence of a }c_\Gamma\textbf{-atom forces cumulative normalized Kelvin reset at least }(1-\rho_\Gamma)c_\Gamma\textbf{ on that cycle; hence one reset of size at least }(1-\rho_\Gamma)c_\Gamma/M\textbf{ occurs unless material/carrier shadowing itself fails. Every }M+1\textbf{-generation block therefore contains either a carrier/state replacement or a uniform circulation-reset event. The reset has generation homogeneity }p=0\textbf{ and physical circulation homogeneity }1-\alpha<0\textbf{, so it is precisely the nonpositive-homogeneity sidecar demanded by D93. On the mesoscopic Navier--Stokes branch D81 identifies this reset with filtered viscous circulation, SGS circulation, or shadowing mismatch, and D81--85 route it back to existing finite joint defects/state escape. However a constant-circulation recurrence }\Gamma_{n+1}=\rho_\Gamma\Gamma_n+(1-\rho_\Gamma)\Gamma_*\textbf{ shows that uniform }p=0\textbf{ reset can persist forever algebraically; no finite total reset capacity has yet been established. Helicity has the right negative homogeneity but lacks a universal nonzero/finite-capacity bridge here. Thus the remaining endgame is now the capacity of the Kelvin reset source, not another positive work budget.}
}
\]

---

# 24. Next autonomous step

## DCRP95 / X72-R78 — Kelvin Reset Source Capacity / SGS Phase-Slip Packing

**Working title**

> **Can a Uniform Positive-Density Kelvin Reset Be Supplied Indefinitely by SGS Circulation without Forcing Scale/State Multiplicity or a Finite-Capacity Phase-Slip Debt?**

Primary tasks:

1. start from:
   \[
   |\delta_n|\ge\delta_*
   \]
   on positive generation density;
2. use D81's SGS circulation:
   \[
   -\int\oint\nabla\cdot R_\ell\cdot dy\,dt;
   \]
3. interpret it as a circulation phase-slip / vortex-force event;
4. search for a scale-locality / packing theorem for coarse circulation flux;
5. compare the reset event to:
   - derivative-compatible increment mass;
   - filtered-vorticity flux;
   - loop-surface crossing number;
6. test whether one reset requires a fixed amount of signed/absolute flux through a material spanning surface;
7. seek a finite total-variation or crossing-capacity bound on repeated reset events;
8. if unavailable, isolate one exact:
   \[
   \text{SGS Kelvin phase-slip conveyor}
   \]
   normal form.

Desired endpoint:

\[
\boxed{
\mathsf C_{\Gamma{\rm -reset}}^0
\Longrightarrow
\text{finite-capacity phase-slip debt}
\vee
R_{\rm state}
\vee
R_{\rm crit}
\vee
\text{one explicit SGS reset conveyor}.
}
\]

---

# 25. One-line checkpoint

The positive-homogeneity work conveyor is no longer standalone: finite-state Kelvin contraction forces a uniform circulation reset or carrier replacement in every bounded number of generations, giving the late recurrence a mandatory \(p\le0\) sidecar; the only unresolved issue is whether the SGS/viscous source of that reset has a finite global capacity.

---

**End checkpoint:** DCRP94 / X72-R77  
**Next:** DCRP95 / X72-R78 — Kelvin Reset Source Capacity / SGS Phase-Slip Packing.
