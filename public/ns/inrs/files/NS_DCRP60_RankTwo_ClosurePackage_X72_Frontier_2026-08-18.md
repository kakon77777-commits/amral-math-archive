# DCRP60 — Formal Rank-Two Closure Package, Residual-Loop Audit, and the X72 Global Frontier Selection

**Series:** Independent Navier–Stokes Research Series  
**Date:** 2026-08-18  
**Status:** Closure checkpoint / RMRM handoff / frontier selection  
**Immediate predecessor:** `NS_DCRP59_SignedResidual_Confluence_RankTwoClosure_2026-08-17.md`

**Primary internal dependencies**
- DCRP-30 — strict Type-II DSS exponent window and sublinear Euler-profile energy tail
- DCRP-31 — finite inward PFET matching
- DCRP-35 — enstrophy dichotomy: positive stretching or inward turnover
- DCRP-38 — exact vorticity covariance ledger and residual split
- DCRP-40–42 — rank-two planar/pancake reduction
- DCRP-43–59 — quotient correction, scalar-connection repair, pressure-response reduction, null-envelope/X72 lift, localization leakage, multipole compensation, tail elimination, residual confluence
- RMRM checkpoint v42 — pre-NTLA rank-two frontier
- X72 Round37 — affine pressure-response defect / STOP-C41
- X72 Round42–43 — visible/invisible vorticity stress / STOP-C47

**External calibration**
- Chae–Tsai, arXiv:1304.7414.
- Xue, arXiv:1408.6619.
- Galanti–Gibbon–Heritage, arXiv:chao-dyn/9709003.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP38–59 now support a formal closure statement for the **maximally rigid rank-two equality route**.

A nonzero strict same-parent DSS rank-two branch cannot continue globally while keeping all of:

$$
\boxed{
\text{fixed rank-two plane},
}
$$

$$
\boxed{
\text{zero shape / plane-motion defect},
}
$$

$$
\boxed{
\text{gauge-flat canonical scalar connection},
}
$$

$$
\boxed{
\text{perfect central pressure response},
}
$$

$$
\boxed{
\text{global X72 visibility transparency},
}
$$

and

$$
\boxed{
R_B^{na}=R_B^{tr}=0.
}
$$

The route has no remaining zero-defect continuation.

Every global continuation enters at least one of three channels:

$$
\boxed{
\mathsf X
\vee
\mathsf N
\vee
\mathsf T,
}
$$

where

### X — X72 projection / realizability defect

The DCRP54 localization leak is not globally canceled, or actual vorticity-stress projection fails the required global transparency.

### N — positive non-affine vortex-stretching work

$$
\boxed{
\int_0^{S_0}
\int
\phi\,
\Omega\cdot E\Omega
\,dy\,ds
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)\,ds.
}
$$

### T — positive inward enstrophy turnover

$$
\boxed{
\int_0^\infty
[-\phi'(R)]
\mathcal J_{\omega,\rm in}(R)
\,dR
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)\,ds.
}
$$

The central audit of DCRP60 is that **N and T are not genuinely new terminal branches**.

They are precisely the two old DCRP35 enstrophy-supply mechanisms, now recovered with stronger rank-two/X72-generated quantitative lower bounds.

The only structurally new coordinate that does not immediately return to the earlier DCRP35 dichotomy is:

$$
\boxed{
\mathsf X:
\text{X72 visibility / pressure-response / realizability defect}.
}
$$

Therefore the next proof work should not continue to refine rank-two pancake geometry.

It should leave DCRP rank-two local analysis and attack the X72 defect globally.

The selected next frontier is:

$$
\boxed{
\textbf{
Actual Vorticity-Stress Visibility Defect /
Non-Affine Stretching Coupling.
}
}
$$

The strategic objective is to prove a theorem of the form

$$
\boxed{
\mathsf N>0
\Longrightarrow
\mathsf X>0
\ \vee\
\mathsf T>0,
}
$$

or a stronger quantitative version.

If successful, the rank-two confluence reduces from three channels to:

$$
\boxed{
\mathsf X
\vee
\mathsf T,
}
$$

and the proof can then concentrate entirely on one nonlocal projection defect versus one material-turnover escape.

---

# 1. Canonical hypotheses of the closed rank-two route

Define the rank-two equality package $\mathcal R_2^{eq}$ by the following hypotheses.

## H1 — strict same-parent DSS / Type-II branch

The local Euler limit is $S_0$-periodic and lies in the strict exponent window

$$
\boxed{
1<\alpha<\frac32,
}
$$

equivalently

$$
\boxed{
\frac25<\gamma<\frac12.
}
$$

## H2 — nonzero recurrent rank-two vorticity covariance

There is a recurrent inner core with

$$
\boxed{
\operatorname{rank}B=2,
}
$$

and

$$
\boxed{
Z_{\rm in}>0.
}
$$

## H3 — no rank-one collapse

The rank-one Burgers-jet branch is not active.

## H4 — no rank-three lift in the equality interior

The core remains in the rank-two identity class before the outer compensation stage.

## H5 — fixed vorticity plane / zero plane-motion action

The active covariance plane has a fixed normal $n$.

## H6 — zero covariance-shape action

The DCRP41 shape tensor is static, selecting the canonical pancake affine jet.

## H7 — gauge-flat scalar connection

The DCRP44 flatness defects vanish:

$$
\boxed{
\mathcal C_{qz}=0,
\qquad
\mathcal F_{sz}=0.
}
$$

## H8 — perfect central scalar response

After DCRP49–50 reduction,

$$
\boxed{
c=B_q=\frac12.
}
$$

## H9 — perfect local X72 pressure response

The relevant X72 affine pressure-response defect vanishes on the maximally rigid local chart.

## H10 — zero covariance residual

$$
\boxed{
R_B^{na}=R_B^{tr}=0.
}
$$

The long DCRP39–59 program tests whether this package has a nonzero global continuation.

It does not.

---

# 2. Closure dependency chain

The closure can be summarized as:

$$
\boxed{
\mathcal R_2^{eq}
}
$$

$$
\Downarrow
$$

### DCRP42–44

rank-two PDE

$$
\rightarrow
$$

gauge-correct flat scalar connection.

$$
\Downarrow
$$

### DCRP45–49

finite supplier / pressure-response geometry

$$
\rightarrow
$$

central response or finite defect.

$$
\Downarrow
$$

### DCRP50–53

central perfect-response branch

$$
\rightarrow
$$

local null-envelope geometry

$$
\rightarrow
$$

no global entire perfect-response state.

$$
\Downarrow
$$

### DCRP54

any compact observation of the inner null-envelope stress has unavoidable X72 visibility leakage.

$$
\Downarrow
$$

### DCRP55–56

global cancellation requires:

$$
\boxed{
\text{finite rank-three isotropization}
}
$$

or

$$
\boxed{
\text{fixed-plane transparent noncompact tail}.
}
$$

$$
\Downarrow
$$

### DCRP58

transparent fixed-plane tail is impossible under the sublinear DSS velocity-energy law.

$$
\Downarrow
$$

### DCRP57 / 59

finite isotropic rank-three compensation cannot have zero covariance residual and must enter:

$$
\boxed{
\mathsf N
\vee
\mathsf T.
}
$$

If compensation is not performed:

$$
\boxed{
\mathsf X.
}
$$

Therefore:

## Theorem D60.1 — Formal Rank-Two Equality Closure

Under H1–H10, a nonzero global continuation does not exist.

Every nonzero continuation exits at least one equality hypothesis and enters

$$
\boxed{
\mathsf X
\vee
\mathsf N
\vee
\mathsf T.
}
$$

This is a branch-closure theorem, not a global NS regularity theorem.

---

# 3. Exact meaning of the N branch

Recall

$$
\boxed{
S=A+E,
}
$$

where $A$ is the affine jet and $E$ is the non-affine strain remainder.

The covariance observer is

$$
\boxed{
B
=
\int
\phi
\Omega\otimes\Omega.
}
$$

On the finite transparent compensation state,

$$
\boxed{
B=\rho I.
}
$$

Therefore

$$
\begin{aligned}
\int
\phi
\Omega\cdot A\Omega
\,dy
&=
A:B
\\
&=
\rho\operatorname{tr}A
\\
&=
0.
\end{aligned}
$$

Hence:

## Theorem D60.2 — Isotropic-Covariance Stretching Identity

On the finite isotropic compensation branch,

$$
\boxed{
\int
\phi
\Omega\cdot E\Omega\,dy
=
\int
\phi
\Omega\cdot S\Omega\,dy.
}
$$

Thus DCRP59's positive **non-affine** work is exactly the total vortex-stretching work seen by the isotropic covariance observer.

This is important.

The N branch is not a new third kind of source.

It is precisely the DCRP35 positive-vortex-stretching branch, with the additional information that the affine jet contributes zero net stretching after covariance isotropization.

---

# 4. Exact meaning of the T branch

DCRP59 gives

$$
\boxed{
\operatorname{tr}R_B^{tr}
=
\int
(W\cdot\nabla\phi)
|\Omega|^2dy.
}
$$

For radial nonincreasing $\phi$,

$$
\boxed{
\int_0^{S_0}
\operatorname{tr}R_B^{tr}ds
=
2
\int_0^\infty
[-\phi'(R)]
[-\mathcal J_\omega(R)]
\,dR.
}
$$

Therefore the positive T branch is exactly a smoothed finite-annulus version of DCRP35's inward enstrophy-turnover alternative.

So:

## Theorem D60.3 — Turnover-Branch Identification

The D59 covariance-turnover branch introduces no new terminal mechanism beyond the already-established DCRP35 inward-enstrophy-turnover route.

Its new content is the quantitative lower bound inherited from the X72/rank-two closure chain.

---

# 5. The residual loop

The previous sections reveal a proof-loop structure:

$$
\boxed{
\text{DCRP35}
}
$$

positive stretching / turnover

$$
\Downarrow
$$

finite annular supplier

$$
\Downarrow
$$

rank-two planar reduction

$$
\Downarrow
$$

DCRP42–58 local/global equality analysis

$$
\Downarrow
$$

DCRP59 finite compensation

$$
\Downarrow
$$

positive stretching / turnover

$$
\boxed{
\text{back to DCRP35}.
}
$$

The loop is not logically circular—the later rounds prove that no zero-defect equality route exists—but continuing to analyze N or T using only the same enstrophy ledger will not create new information.

A new observer coordinate is required to break the loop.

That coordinate is X72's nonlocal stress visibility / pressure-response geometry.

---

# 6. X branch is genuinely transverse to the DCRP35 ledger

DCRP35 uses:

- vorticity magnitude;
- vortex stretching;
- inward enstrophy transport;
- finite annular strain supply.

X72 Round42–43 uses the actual vorticity-generated trace-free stress

$$
\boxed{
W_\Omega
=
\Omega\otimes\Omega
-\frac13|\Omega|^2I,
}
$$

and its nonlocal decomposition

$$
\boxed{
W_\Omega
=
W_L+W_T.
}
$$

The crucial scalar is

$$
\boxed{
\mathcal T_0^\ast W_\Omega,
}
$$

or equivalently the Piola–vorticity visibility coordinate.

This information is not determined by the scalar enstrophy ledger.

DCRP54 provides an explicit example:

a null-envelope interior can have a perfectly legitimate local enstrophy/vorticity state but any compact localization generates the nonlocal X72 commutator defect

$$
\boxed{
\mathcal C_\chi\neq0.
}
$$

Therefore $\mathsf X$ is genuinely transverse to the N/T enstrophy loop.

---

# 7. X72 audit: what has already been proved

## Round37 / STOP-C41

X72 derives the affine pressure-response defect

$$
\boxed{
E_p
=
H_P^0+C_S^0
}
$$

and an exact defect PDE / defect-energy identity.

Two dangerous algebraic sources cancel exactly:

- pure self-amplification forcing;
- explicit determinant pressure-source forcing.

The remaining closure is critical and controlled by:

- defect-linear strain response;
- transport–Riesz commutator;
- higher-gradient forcing.

Unconditional defect closure remains open.

## Round42

X72 separates vorticity stress into visible and invisible components and identifies a nontrivial transfer problem.

## Round43 / STOP-C47

The generic constraint

$$
\operatorname{divdiv}W_T=0
$$

has a full wave cone.

Therefore divdiv-only compensated compactness cannot close the endpoint.

The remaining special structure is the actual nonlinear realization

$$
\boxed{
W_\Omega
=
\Omega\otimes\Omega
-\frac13|\Omega|^2I,
}
$$

with

$$
\boxed{
\nabla\cdot\Omega=0.
}
$$

Thus X72's current frontier is already exactly aligned with the DCRP60 handoff.

---

# 8. Why N should be attacked through X rather than through another strain norm

The N branch gives the signed gap

$$
\boxed{
\mathfrak W_N
=
\int_0^{S_0}
\int
\phi
\Omega\cdot S\Omega
\,dy\,ds
>0.
}
$$

Classical vorticity alignment dynamics show that positive stretching/alignment is not inherently contradictory.

Therefore another estimate of

$$
\Omega\cdot S\Omega
$$

alone is unlikely to close the branch.

The missing information is how a recurrent positive-stretching configuration can simultaneously maintain the pressure/stress projection required by incompressibility.

This is precisely what $E_p$ and the X72 visible/invisible decomposition measure.

Hence the next target should couple:

$$
\boxed{
\mathfrak W_N
}
$$

to

$$
\boxed{
E_p
}
$$

and/or

$$
\boxed{
\mathcal C_\chi.
}
$$

---

# 9. Why T should be temporarily left as the final escape branch

The T branch is an actual material/observer-boundary transport:

$$
\boxed{
\mathfrak T
=
\int
[-\phi']
\mathcal J_{\omega,\rm in}.
}
$$

DCRP31 independently gives inward PFET.

No universal identity between enstrophy turnover and PFET has been proved.

DCRP49 already warns against identifying different pressure/energy boundary observables without a theorem.

Therefore attacking T now would likely reopen another transport/replenishment loop.

A better sequence is:

1. try to absorb N into X or T;
2. then the entire rank-two handoff becomes
   $$
   X\vee T;
   $$
3. only then attack the final material-turnover route.

---

# 10. Defect-absorption audit

The three D60 channels have the following status.

| Branch | New after D59? | Already represented earlier? | Globally closed? | Priority |
|---|---:|---:|---:|---:|
| $\mathsf X$ — X72 visibility / pressure defect | **Yes, transverse coordinate** | X72 C41/C47 | No | **1** |
| $\mathsf N$ — positive non-affine stretching | stronger quantitative version | DCRP35 stretching / DCRP38 $R_B^{na}$ | No | **2, couple to X** |
| $\mathsf T$ — inward enstrophy turnover | stronger quantitative version | DCRP35 turnover / DCRP38 $R_B^{tr}$ | No | **3, final escape** |

Thus DCRP60 does not recommend three parallel attacks.

The mathematically highest-leverage next problem is the N–X coupling.

---

# 11. Selected frontier

Define

$$
\boxed{
\mathfrak N
=
\int_0^{S_0}
\int
\phi
\Omega\cdot E\Omega
\,dy\,ds.
}
$$

D59 gives on the N branch

$$
\boxed{
\mathfrak N
\ge
\frac38
(2-3\gamma)
\int_0^{S_0}
Z_{\rm in}(s)ds.
}
$$

Define an X72 defect observable, for example on a fixed finite observer domain $D$,

$$
\boxed{
\mathfrak X_E
=
\int_0^{S_0}
\int_D
|E_p|^2
\,dy\,ds,
}
$$

and/or the localized stress visibility defect

$$
\boxed{
\mathfrak X_V
=
\int_0^{S_0}
\|\mathcal C_\chi(s)\|_2^2ds.
}
$$

The next desired theorem is a defect-confluence inequality of the schematic form

$$
\boxed{
\mathfrak N
\le
C
\left(
\mathfrak X_E
+
\mathfrak X_V
+
\mathfrak T_{\rm turnover}
+
\text{controlled lower terms}
\right).
}
$$

If the lower terms are already bounded by the compact strict class, the D59 positive lower bound would imply

$$
\boxed{
\mathfrak X_E
+
\mathfrak X_V
+
\mathfrak T_{\rm turnover}
>0.
}
$$

The strongest possible outcome is

$$
\boxed{
\mathfrak N>0
\Rightarrow
\mathfrak X>0
\vee
\mathfrak T>0.
}
$$

That would remove N as an independent terminal branch.

---

# 12. Why a purely algebraic N → X theorem should not be assumed

One must not simply assert:

$$
\Omega\cdot E\Omega>0
\Rightarrow
E_p\neq0.
$$

The pressure Hessian is nonlocal.

X72 Round36–37 explicitly shows that pressure–cofactor alignment may be dynamically maintained and that universal pressure dephasing statements are false.

Therefore the N–X coupling must use:

- the exact defect PDE;
- transport–Riesz commutator;
- recurrent DSS geometry;
- or the localized vorticity-stress projection.

A pointwise tensor inequality is unlikely to be sufficient.

This prevents a false shortcut.

---

# 13. Candidate exact bridge: strain work versus stress evolution

The actual vorticity stress obeys

$$
W_\Omega
=
\Omega\otimes\Omega
-\frac13|\Omega|^2I.
$$

The vorticity equation gives a material evolution of

$$
\Omega\otimes\Omega.
$$

Its scalar trace production is precisely vortex stretching:

$$
\boxed{
D_s|\Omega|^2
=
2\Omega\cdot S\Omega
-
2|\Omega|^2
}
$$

in similarity variables.

Therefore the N branch is the trace-production component of the same nonlinear stress whose visible/invisible X72 projection defines branch X.

This is the structural reason a coupling theorem should exist.

However:

$$
\boxed{
\text{trace production}
}
$$

and

$$
\boxed{
\text{nonlocal longitudinal/transverse projection}
}
$$

are different coordinates.

The next round must derive their exact commutator, rather than assume equivalence.

---

# 14. Candidate D61 operator

Let

$$
\mathbb P_L
$$

and

$$
\mathbb P_T
$$

be the X72 longitudinal/invisible stress projections.

Define

$$
\boxed{
W_L=\mathbb P_LW_\Omega,
\qquad
W_T=\mathbb P_TW_\Omega.
}
$$

Material differentiation does not commute with the nonlocal projection:

$$
\boxed{
[D_s,\mathbb P_L]W_\Omega
\neq0
}
$$

in general.

This is directly analogous to the scalar gauge/localization commutators that became productive in DCRP44 and DCRP54.

The next exact object should be

$$
\boxed{
\mathfrak C_{L}
=
[D_s,\mathbb P_L]W_\Omega.
}
$$

The desired route is:

$$
\boxed{
\text{positive recurrent stress production}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{visible stress change}
+
\text{invisible stress change}
+
\mathfrak C_L.
}
$$

If visible/invisible states return periodically, positive N-work must be balanced by projection commutator or spatial/material turnover.

This is the highest-leverage next calculation.

---

# 15. Formal RMRM handoff theorem

Define:

$$
\boxed{
\mathcal B_{R2}
}
$$

as the complete rank-two equality package H1–H10.

Then:

## Theorem D60.4 — RMRM Rank-Two Closure Handoff

For every nonzero strict same-parent DSS branch satisfying the pre-rank-two RMRM hypotheses,

$$
\boxed{
\mathcal B_{R2}
\Longrightarrow
\mathsf X\vee\mathsf N\vee\mathsf T.
}
$$

Moreover:

$$
\boxed{
\mathsf N
}
$$

is exactly the DCRP35 positive vortex-stretching branch on the isotropic compensation observer,

and

$$
\boxed{
\mathsf T
}
$$

is exactly the DCRP35 inward-enstrophy-turnover branch.

Therefore the rank-two local equality analysis is complete as a separate subproject.

No further rank-two geometric refinement should be undertaken unless a later global branch explicitly requires it.

---

# 16. Canonical rank-two dependency graph

```text
strict Type-II DSS
        |
        v
rank-two covariance
        |
        +--> rank-one collapse ------------------> old branch
        |
        +--> rank-three lift ---------------------> defect branch
        |
        v
fixed plane + zero shape
        |
        v
gauge-flat scalar connection
        |
        v
central response c=1/2
        |
        v
local null-envelope / perfect response
        |
        +--> global entire state -----------------> impossible
        |
        v
finite transition
        |
        v
localized X72 visibility leakage
        |
        +--> not compensated ---------------------> X
        |
        +--> transparent tail --------------------> impossible
        |
        +--> finite compensation
                |
                v
        isotropic rank-three covariance
                |
                v
        exact covariance residual trace
                |
                +--> positive non-affine work ----> N
                |
                +--> inward enstrophy turnover ---> T
```

This is the canonical DCRP rank-two closure map.

---

# 17. What was actually gained by the NTLA rewrite

The original RMRM v42 frontier already knew that the rank-two pancake branch had to pay some combination of:

- rank lift;
- residual;
- turnover;
- PFET;
- sheet replacement.

The NTLA-guided DCRP43–59 work did more than rename these branches.

It supplied the missing refinement sequence:

1. quotient-correct the scalar gauge;
2. separate Eulerian identity from material identity;
3. replace gauge-dependent $G=0$ by invariant connection flatness;
4. classify central response and pressure Hessian;
5. identify the null-envelope local equality class;
6. prove the local equality cannot extend globally;
7. compute the X72 localization leakage;
8. prove finite same-plane compensation impossible;
9. eliminate the noncompact transparent tail using the velocity-energy law;
10. force finite compensation into rank-three isotropy;
11. recover a signed quantitative non-affine/turnover gap.

Thus the rank-two branch did not merely become “more complicated.”

Its equality space was genuinely exhausted.

---

# 18. Remaining global proof architecture

After D60 the proof tree has conceptually moved one level upward.

The important unresolved objects are no longer:

- pancake shape;
- plane motion;
- scalar gauge;
- null-envelope local realizability.

They are:

$$
\boxed{
\text{nonlocal stress projection / pressure response}
}
$$

and

$$
\boxed{
\text{material enstrophy turnover}.
}
$$

These are global transport/projection mechanisms.

The next work should therefore use X72/RMRM global operators rather than construct another local rank-two normal form.

---

# 19. Priority decision

The priority is:

## Priority 1 — N–X defect coupling

Try to show the D59 positive stretching source cannot remain pressure/visibility-perfect.

This has maximum leverage because it can absorb N into X/T.

## Priority 2 — X branch itself

If the first route fails, attack the actual vorticity-stress realizability closure at X72 STOP-C47.

## Priority 3 — T branch

Only after N/X compression should the remaining inward-enstrophy/material-turnover route be attacked jointly with PFET.

This avoids another long transport loop before exploiting the new X72 information.

---

# 20. Status ledger

## CLOSED AS EQUALITY SUBPROJECT

- static rank-two plane;
- zero shape;
- canonical scalar/shear equality;
- perfect central pressure response;
- global null-envelope extension;
- transparent same-plane outer tail;
- finite compensation with zero covariance residual.

## ROUTED, NOT GLOBALLY CLOSED

### X

X72 visibility / pressure-response / realizability defect.

### N

Positive vorticity stretching generated by non-affine strain.

### T

Inward enstrophy turnover.

## NEW IN D60

### D60-P1

On isotropic covariance,

$$
A:B=0.
$$

Therefore non-affine work equals total vortex stretching.

### D60-P2

D59's N and T are exactly the two old DCRP35 supply channels, now with stronger lower bounds.

### D60-P3

The DCRP35 → rank-two → D59 route forms a residual loop; additional enstrophy-only refinement will not break it.

### D60-P4

X72 visibility/pressure response is the unique transverse observer coordinate currently available to break the loop.

---

# 21. New STOP

$$
\boxed{
\textbf{
STOP-D60:
The rank-two equality subproject is formally complete. Its finite residual branches confluence exactly back to the old stretching/turnover dichotomy, so further rank-two geometry would loop. The uniquely prioritized new frontier is the coupling of positive non-affine vortex-stress production to the X72 nonlocal visibility/pressure-response defect, with turnover retained as the final escape.
}
}
$$

---

# 22. Next autonomous step

## DCRP61 / X72-R44 Bridge — Stress-Projection Production Commutator

**Working title**

> **Material Evolution of Actual Vorticity Stress, Longitudinal Projection Commutator, and Non-Affine Work Absorption**

Primary tasks:

1. derive the exact similarity-material equation for
   $$
   W_\Omega
   =
   \Omega\otimes\Omega
   -
   \frac13|\Omega|^2I;
   $$
2. project it with
   $$
   \mathbb P_L,\mathbb P_T;
   $$
3. compute
   $$
   [D_s,\mathbb P_L]W_\Omega;
   $$
4. identify the scalar/tensor component carrying
   $$
   \Omega\cdot S\Omega;
   $$
5. integrate one DSS period and exploit periodic return of the projected stresses;
6. attempt the confluence
   $$
   \mathsf N
   \Longrightarrow
   \mathsf X
   \vee
   \mathsf T;
   $$
7. if the commutator itself is the missing branch, compare it directly with X72 Round38 transport–Riesz commutator estimates.

Desired endpoint:

$$
\boxed{
\text{N absorbed into X/T}
\quad\text{or}\quad
\text{one explicit new global commutator frontier}.
}
$$

---

# 23. One-line checkpoint

DCRP38–59 now form a complete rank-two closure package: the only surviving finite residuals are exactly the old stretching/turnover channels, so the rank-two subproject should stop here and the proof should move to the X72 nonlocal stress-projection commutator, which is the only new coordinate capable of breaking the residual loop.

---

**End checkpoint:** DCRP60  
**Next:** DCRP61 / X72-R44 Bridge — Material Vorticity-Stress Projection Dynamics.
