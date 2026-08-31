# DCRP99 / X72-R82 — Compact T Absorption, Uniform X-Hitting Horizon, and Bounded-Lag X72–Kelvin Synchronization

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / X–Kelvin joint-recurrence round  
**Immediate predecessor:** `NS_DCRP98_X72R81_MovingPancakeGap_XNTConfluence_2026-08-20.md`

## Primary internal dependencies

- DCRP62 — non-affine stretching absorption:
  \[
  N\Longrightarrow X\vee T.
  \]
- DCRP75–79 — X-free dynamic turnover \(\to\) \(2\gamma\)-resonant material conveyor \(\to\) no compact infinite X-free carrier.
- DCRP80–91 — noncompact T/tail/filament/Kelvin exits absorbed into existing scale/state/critical coordinates.
- DCRP95 — sign-coherent SGS Kelvin phase-slip is syndetic and has linear positive reset variation.
- DCRP96–98 — local/co-located dual-lock analysis; moving-pancake correction; conditional reconvergence to \(X/N/T\).

## Fresh primary-source calibration

- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier–Stokes Equations*, arXiv:2606.27560.
- R. Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322.
- R. Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341.

The external structural audit is consistent with the methodological choice below: do not collapse distinct pressure/work/circulation observables into one unconditional scalar detector.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP98 returned the newest Kelvin/SGS phase-slip branch to the older rank-two compiler:

\[
\mathsf C_{\rm dual}
\Longrightarrow
X\vee N\vee T.
\]

DCRP62 already proves:

\[
\boxed{
N\Longrightarrow X\vee T.
}
\tag{0.1}
\]

Hence:

\[
\boxed{
\mathsf C_{\rm dual}
\Longrightarrow
X\vee T.
}
\tag{0.2}
\]

But D99 goes further and no longer depends on local dual-lock coincidence.

The old D76–79 analysis proves:

\[
\boxed{
\text{there is no infinite compact X-free late-T material chain}.
}
\tag{0.3}
\]

D99 uses compactness to upgrade this qualitative theorem into a **uniform finite X-hitting horizon**.

Let \(\mathcal K_T\) be the compact normalized late-T state class after all declared:

- tail;
- filamentation;
- scale;
- state;
- critical-reservoir

escapes are removed.

Let:

\[
\mathcal R
\subset
\mathcal K_T\times\mathcal K_T
\]

be the closed one-generation same-parent transition relation.

Let the finite X72 detector family be:

\[
X_1,\ldots,X_{M_X}\ge0,
\]

and define:

\[
\boxed{
\mathfrak X(z)
=
\max_j X_j(z).
}
\tag{0.4}
\]

Assume \(\mathfrak X\) is continuous/lower-semicontinuous in the declared strong normalized topology.

Then:

# Uniform X-hitting theorem

There exist:

\[
\boxed{
L_X<\infty,
\qquad
c_X>0
}
\]

such that every \(\mathcal R\)-path of length \(L_X\) in the compact late-T class contains a state \(z_k\) with:

\[
\boxed{
\mathfrak X(z_k)\ge c_X.
}
\tag{0.5}
\]

Thus on the compact branch **T is not an independent recurrent terminal**.

It is a bounded-lag route to X.

Together with D62:

\[
\boxed{
N
\Longrightarrow
X
\quad
\text{within uniformly bounded normalized depth}
}
\tag{0.6}
\]

unless state/critical compactness fails.

Therefore the compact late rank-two frontier is no longer:

\[
X\vee N\vee T.
\]

It is:

\[
\boxed{
X
}
\]

as the only recurrent compact observer coordinate.

D95 independently proves that the sign-coherent SGS Kelvin slip is syndetic: there exists \(B_\Gamma<\infty\) such that every \(B_\Gamma\)-generation block contains an oriented reset:

\[
\boxed{
\sigma_\Gamma\delta^{\rm SGS}\ge c_{\rm slip}>0.
}
\tag{0.7}
\]

The X-hitting theorem gives another syndetic clock: every \(B_X:=L_X+1\) block contains:

\[
\boxed{
X_j\ge c_X
}
\]

for some finite detector \(j\).

Two syndetic event sets need not coincide generation by generation.

But they must occur at **bounded lag**.

After finite lag / detector / orientation pigeonholing, there exist:

\[
\boxed{
\ell_*\in\mathbb Z,
\qquad
|\ell_*|\le B_*-1,
}
\]

one fixed oriented Kelvin-slip coordinate \(i_*\), and one fixed X72 detector \(j_*\), such that on a positive-density generation set \(\mathcal A_*\),

\[
\boxed{
\sigma_*
\delta^{\rm SGS}_{i_*}(n)
\ge
c_{\rm slip},
}
\tag{0.8}
\]

and:

\[
\boxed{
X_{j_*}(n+\ell_*)
\ge
c_X.
}
\tag{0.9}
\]

Here:

\[
B_*=\max(B_\Gamma,B_X).
\]

This is the main new normal form:

\[
\boxed{
\mathsf C_{X\Gamma}^{\ell_*}
=
\textbf{Bounded-Lag X72–Kelvin Locked Conveyor}.
}
\]

The lag is fixed after subsequence/pigeonhole compression.

The conveyor can no longer evade by:

- alternating X/N/T type;
- changing Kelvin-slip orientation;
- changing detector index;
- letting the relative X/slip phase wander without bound.

---

# 1. Important synchronization correction

A statement used informally in D96–98 needs a scope clarification.

From:

\[
\operatorname{dens}A>0,
\qquad
\operatorname{dens}B>0,
\]

one cannot infer:

\[
\operatorname{dens}(A\cap B)>0.
\]

For example:

\[
A=2\mathbb N,
\qquad
B=2\mathbb N+1
\]

both have density \(1/2\) but:

\[
A\cap B=\varnothing.
\]

Therefore:

## Correction D99.1

The D96–98 **pointwise / zero-lag dual-lock covariance cone** is a legitimate **co-located subbranch**, but positive recurrence of Kelvin slip and positive recurrence of SGS work/X72 activity do not by themselves prove zero-lag coincidence.

D99 replaces the unnecessary zero-lag assumption by a provable bounded-lag theorem.

The D97–98 cone calculations remain valid when:

\[
\ell_*=0
\]

or when an additional strong transport/shadowing theorem identifies the two detector windows.

---

# 2. Closed transition relation

The late T branch is naturally relation-valued rather than necessarily represented by one deterministic global map.

Let:

\[
\mathcal K_T
\]

be compact.

Let:

\[
\mathcal R
\subset
\mathcal K_T\times\mathcal K_T
\]

be closed.

A finite T path is:

\[
z_0,z_1,\ldots,z_m
\]

with:

\[
(z_j,z_{j+1})\in\mathcal R.
\]

An X-free path satisfies:

\[
\mathfrak X(z_j)=0
\]

at each state.

D79 says no infinite compact X-free late-T material path exists under the D76–79 equality assumptions.

---

# 3. Compactness upgrades “no infinite path” to a finite horizon

For \(m\ge0\), define the path set:

\[
\boxed{
\mathcal P_m^0
=
\left\{
(z_0,\ldots,z_m)\in\mathcal K_T^{m+1}:
(z_j,z_{j+1})\in\mathcal R,
\ 
\mathfrak X(z_j)=0
\right\}.
}
\tag{3.1}
\]

Because:

- \(\mathcal K_T\) is compact;
- \(\mathcal R\) is closed;
- the zero set of \(\mathfrak X\) is closed;

each:

\[
\mathcal P_m^0
\]

is compact.

Suppose:

\[
\mathcal P_m^0\neq\varnothing
\]

for every \(m\).

Choose one path of every length.

By compactness and diagonal extraction, there exists an infinite sequence:

\[
z_0,z_1,\ldots
\]

such that:

\[
(z_j,z_{j+1})\in\mathcal R,
\]

and:

\[
\mathfrak X(z_j)=0
\qquad
\forall j.
\]

This contradicts D79.

Therefore:

## Theorem D99.2 — Uniform Finite X-Hitting Horizon

There exists:

\[
\boxed{
L_X<\infty
}
\]

such that:

\[
\boxed{
\mathcal P_{L_X}^0=\varnothing.
}
\tag{3.2}
\]

Every compact late-T chain hits X within at most \(L_X\) normalized generations.

This conclusion uses no periodic-orbit theorem.

---

# 4. Uniform X gap

Finite hitting is not enough.

We also need a quantitative detector gap.

Let:

\[
\mathcal P_{L_X}
\]

be the compact space of all admissible length-\(L_X\) paths.

Define:

\[
\boxed{
F_X(z_0,\ldots,z_{L_X})
=
\max_{0\le k\le L_X}
\mathfrak X(z_k).
}
\tag{4.1}
\]

By D99.2:

\[
F_X>0
\]

on:

\[
\mathcal P_{L_X}.
\]

If the X detectors are continuous, \(F_X\) is continuous.

Compactness gives:

## Theorem D99.3 — Uniform Finite-Horizon X Gap

\[
\boxed{
c_X
:=
\min_{\mathcal P_{L_X}}
F_X
>
0.
}
\tag{4.2}
\]

Thus every compact late-T path contains an order-one normalized X72 event within \(L_X\) generations.

If only lower semicontinuity is available, the same conclusion follows from lower-semicontinuous compact minimization.

---

# 5. N is also only a bounded-lag route to X

D62 proves:

\[
N\Longrightarrow X\vee T.
\]

If \(N\) immediately produces X, done.

If it produces T, D99.2 gives X within \(L_X\) more generations.

Therefore:

## Theorem D99.4 — Compact N Absorption with Finite Lag

\[
\boxed{
N
\Longrightarrow
X
\quad
\text{within at most }L_X+1
\text{ generations}
}
\tag{5.1}
\]

unless:

\[
R_{\rm state}
\vee
R_{\rm crit}
\]

becomes active.

So \(N\) is not a recurrent compact terminal either.

---

# 6. D98 dual-lock branch reaches X in bounded depth

D98 gives:

\[
\mathsf C_{\rm dual}
\Longrightarrow
X\vee N\vee T
\vee R_{\rm state}
\vee R_{\rm crit}.
\]

Use D99.2 and D99.4.

## Theorem D99.5 — Dual-Lock-to-X Finite Horizon

On the compact bounded-reservoir branch:

\[
\boxed{
\mathsf C_{\rm dual}
\Longrightarrow
X
\quad
\text{within at most }L_D:=L_X+1
\text{ generations}.
}
\tag{6.1}
\]

This keeps D97–98 as a useful zero-lag refinement while removing the need to assume zero-lag generically.

---

# 7. T noncompactness does not reopen the branch

If the T path leaves \(\mathcal K_T\) before hitting X, D79–80 route it to:

- alignment degeneration;
- shape blow-up;
- support/tail escape;
- filamentation;
- packet multiplicity;
- injection/replacement;
- prelimit Kelvin residue.

D80 absorbs these into:

\[
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_K.
\]

D81–95 further reduce:

- \(R_K\) into SGS/scale/state coordinates;
- tail into finite-time transport contradiction or state/scale defects;
- filamentation into state/scale/FV defects;
- repeated Kelvin replacement into the sign-coherent phase-slip clock.

Thus on the declared **compact bounded-reservoir branch** no independent T escape remains.

This is why D99 can legitimately treat X as the only compact recurrent X/N/T coordinate.

---

# 8. Kelvin slip is syndetic

D95 gives a finite oriented loop-state alphabet.

There exist:

\[
B_\Gamma<\infty,
\qquad
c_{\rm slip}>0
\]

such that every block of \(B_\Gamma\) generations contains at least one:

\[
\boxed{
\sigma_n
\delta_n^{\rm SGS}
\ge
c_{\rm slip}.
}
\tag{8.1}
\]

This is stronger than positive upper density.

It is a bounded-gap or **syndetic** recurrence statement.

---

# 9. X is also syndetic

D99.2–3 imply:

\[
B_X
=
L_X+1
\]

and:

\[
c_X>0
\]

such that every \(B_X\)-generation compact T/rank-two block contains at least one:

\[
\boxed{
\mathfrak X\ge c_X.
}
\tag{9.1}
\]

Therefore X72 recurrence is also syndetic.

This is new compared with the older D60–80 architecture, which classified X as a surviving terminal but did not need to formulate a generation-gap theorem.

---

# 10. Two syndetic clocks imply bounded lag

Let:

\[
B_*
=
\max(B_\Gamma,B_X).
\]

Partition the generation axis into disjoint blocks:

\[
I_k
=
[kB_*,(k+1)B_*-1].
\]

Each block contains:

- at least one oriented Kelvin-slip event;
- at least one X event.

Choose one of each:

\[
n_k^\Gamma,
\qquad
n_k^X.
\]

Then:

\[
\boxed{
|n_k^X-n_k^\Gamma|
\le
B_*-1.
}
\tag{10.1}
\]

Thus the relative lag belongs to the finite alphabet:

\[
\boxed{
\Lambda_*
=
\{
-(B_*-1),
\ldots,
B_*-1
\}.
}
\tag{10.2}
\]

---

# 11. Finite detector/orientation/lag pigeonhole

Let:

- \(M_\Gamma\) = number of finite oriented Kelvin-slip state/source types;
- \(M_X\) = number of finite X detector types;
- \(|\Lambda_*|=2B_*-1\).

Every disjoint block produces one label:

\[
\boxed{
(\Gamma\text{-type},X\text{-type},\ell)
}
\]

from a finite alphabet of size:

\[
\boxed{
M_{\rm word}
=
M_\Gamma
M_X
(2B_*-1).
}
\tag{11.1}
\]

Among the first \(K\) disjoint blocks, one word occurs at least:

\[
K/M_{\rm word}
\]

times.

Therefore:

## Theorem D99.6 — Positive-Density Fixed X–Kelvin Word

There exist fixed:

\[
i_*,
\qquad
j_*,
\qquad
\ell_*,
\]

with:

\[
|\ell_*|\le B_*-1,
\]

such that along a generation set \(\mathcal A_*\),

\[
\boxed{
\sigma_*
\delta^{\rm SGS}_{i_*}(n)
\ge
c_{\rm slip},
}
\tag{11.2}
\]

and:

\[
\boxed{
X_{j_*}(n+\ell_*)
\ge
c_X,
}
\tag{11.3}
\]

while:

\[
\boxed{
\overline{\operatorname{dens}}
\mathcal A_*
\ge
\frac{
1
}{
B_*
M_\Gamma
M_X
(2B_*-1)
}.
}
\tag{11.4}
\]

The constant is crude but explicit.

The important point is:

\[
\boxed{
\text{one fixed lag, one fixed slip orientation, one fixed X detector}.
}
\]

---

# 12. Definition — bounded-lag X72–Kelvin locked conveyor

Define:

\[
\boxed{
\mathsf C_{X\Gamma}^{\ell_*}
}
\]

by the following properties.

1. strict Type-II same-parent normalized branch;
2. compact bounded reservoirs;
3. one fixed oriented SGS Kelvin reset satisfies:
   \[
   \sigma_*
   \delta^{\rm SGS}(n)
   \ge
   c_{\rm slip};
   \]
4. one fixed X72 detector satisfies:
   \[
   X_*(n+\ell_*)
   \ge
   c_X;
   \]
5. the lag:
   \[
   \ell_*
   \]
   is fixed and bounded;
6. the joint word occurs at positive generation density;
7. all tail/filament/state/critical exits are silent.

This is the new final compact normal form.

---

# 13. Zero-lag subbranch recovers D96–98

If:

\[
\ell_*=0,
\]

and the selected X/work/slip tests genuinely act on the same normalized covariance package, D96–98's local covariance geometry applies.

Then:

- SGS circulation forces deviatoric/nematic covariance locking;
- local forward SGS work adds the second covariance projection;
- D97 gives the pancake-gap / carrier-unlock identity;
- D98 reconnects the co-located dual state to \(X/N/T\).

Therefore D96–98 remain valid and useful as the:

\[
\boxed{
\ell_*=0
}
\]

fine-structure theory.

D99 is the generic synchronization theorem that does not require \(\ell_*=0\).

---

# 14. Signed aligned-neutral X subtype

For the D62 aligned-neutral X subtype, one gets more than an X norm gap.

On a same-parent aligned-neutral material period:

\[
\boxed{
\int
\xi^TE_p\xi\,ds
=
-
\frac{2-3\gamma}{2}S_0
-
\frac16
\int|\Omega|^2ds
<0.
}
\tag{14.1}
\]

Hence:

\[
\boxed{
-\int
\xi^TE_p\xi\,ds
>
\frac{2-3\gamma}{2}S_0.
}
\tag{14.2}
\]

If the recurrent X detector selected by D99.6 is this subtype, the joint word becomes **sign-coherent in both coordinates**:

\[
\boxed{
\text{positive oriented SGS circulation reset}
+
\text{negative axial X72 pressure-response action}.
}
\]

This is a particularly rigid subbranch.

D99 does not claim that every generic X detector has this sign structure.

---

# 15. Why bounded lag is genuinely new information

Before D99 the late architecture gave:

- Kelvin slip recurring at positive density;
- X/N/T defects recurring through the rank-two compiler.

Those could, logically, have lived on unrelated subsequences with drifting phase relation.

D99 removes that freedom.

On the compact branch the event gaps are uniformly bounded.

Therefore after finite compression the relative temporal phase is fixed:

\[
\boxed{
\ell_*.
}
\]

The survivor cannot indefinitely:

- move the X event farther from the reset;
- cycle among X detector types;
- flip Kelvin orientation;
- hide the two mechanisms on unrelated scales/generations.

This is a true reduction of the recurrence state space.

---

# 16. Why this still does not prove contradiction

Two bounded-lag nonzero observables can coexist.

There is currently no theorem of the form:

\[
\boxed{
\sigma\delta_\Gamma^{\rm SGS}>0
\Longrightarrow
\text{forbidden sign of }X
}
\]

or:

\[
\boxed{
|\delta_\Gamma^{\rm SGS}|
+
|X|
\le
\text{one finite global capacity}.
}
\]

The structural obstruction literature also warns against inventing one universal scalar detector from distinct work/pressure/subfilter coordinates.

Therefore D99 does not claim that \(\mathsf C_{X\Gamma}^{\ell_*}\) is impossible.

It isolates it.

---

# 17. The new cross-equation target

The bounded lag suggests the correct next operator.

Let:

\[
\mathcal U_{\ell_*}
\]

denote the normalized material/renormalization propagator over \(\ell_*\) generations.

The joint conveyor requires schematically:

\[
\boxed{
X_*
\left(
\mathcal U_{\ell_*}
z_n
\right)
\ge
c_X
}
\]

whenever:

\[
\boxed{
\Gamma_{\rm SGS}^+(z_n)
\ge
c_{\rm slip}
}
\]

on the recurrent word set.

The next theorem should study the transported response:

\[
\boxed{
X_*\circ\mathcal U_{\ell_*}
}
\]

as a functional of the SGS circulation-reset source.

This is a **finite-lag transfer operator problem**, not another local covariance classification.

---

# 18. Candidate finite-lag identity

At lag zero:

\[
\delta_\Gamma^{\rm SGS}
\]

is generated by:

\[
-\nabla\cdot R_\ell
\]

through a closed-loop current.

X72 pressure response uses:

\[
E_p
=
H_P^0+C_S^0
\]

and the actual vorticity stress / pressure Hessian.

Across nonzero lag, both quantities evolve under the same similarity material dynamics.

Thus a plausible next object is a Duhamel/adjoint transfer pairing:

\[
\boxed{
\mathfrak L_{\Gamma\to X}^{(\ell)}
=
\left\langle
\mathcal U_\ell^*
\Psi_X,
\,
-\nabla\cdot R
\right\rangle.
}
\tag{18.1}
\]

D99 does not assert a coercive inequality for this object.

It identifies it as the exact next frontier.

---

# 19. Updated late compact compiler

D98 gave, conditionally on its local dual package:

\[
X\vee N\vee T.
\]

D62 removes N:

\[
N\to X\vee T.
\]

D79 plus compactness removes indefinitely X-free T.

Therefore, on the full declared compact bounded-reservoir late rank-two class:

## Theorem D99.7 — Compact X/N/T Collapse

\[
\boxed{
\text{late compact rank-two recurrence}
\Longrightarrow
\text{syndetic }X.
}
\tag{19.1}
\]

D95 simultaneously gives:

\[
\boxed{
\text{late compact rank-two recurrence}
\Longrightarrow
\text{syndetic sign-coherent Kelvin slip}.
}
\tag{19.2}
\]

Combining:

## Theorem D99.8 — Final Joint Compact Normal Form

\[
\boxed{
\text{late compact survivor}
\Longrightarrow
\mathsf C_{X\Gamma}^{\ell_*}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{19.3}
\]

No independent:

- N;
- T;
- tail;
- filamentation;
- generic Kelvin reset;
- generic dual-lock cone

terminal remains at this resolution.

---

# 20. Status ledger

## PROVED this round

### D99-P1 — synchronization correction:
positive density does not imply zero-lag coincidence.

### D99-P2 — closed-relation compactness theorem:
no infinite compact X-free chain implies a uniform finite X-hitting horizon.

### D99-P3 — compactness upgrades finite hitting to a uniform X detector gap.

### D99-P4 — D62 N branch reaches X within uniformly bounded lag on the compact branch.

### D99-P5 — D98 dual-lock branch reaches X within bounded lag, without assuming pointwise coincidence.

### D99-P6 — T noncompact exits do not reopen a new terminal after D80–95.

### D99-P7 — X72 recurrence is syndetic on the compact late rank-two branch.

### D99-P8 — Kelvin phase slip is syndetic by D95.

### D99-P9 — two syndetic clocks give a bounded relative lag.

### D99-P10 — finite lag/detector/orientation pigeonhole gives one fixed X–Kelvin word at positive generation density.

### D99-P11 — D62 aligned-neutral subtype yields a sign-fixed X pressure-response component when that subtype recurs.

### D99-P12 — the newest compact survivor is reduced to one finite-lag X72–Kelvin locked conveyor.

---

# 21. What is NOT proved

D99 does not prove:

- the X72–Kelvin locked conveyor is impossible;
- the X and Kelvin events must occur in the same generation;
- every X detector has a fixed sign;
- X72 pressure defect and SGS circulation reset share one finite global budget;
- the finite-lag transfer operator is coercive;
- state/critical escape is impossible;
- global Navier–Stokes regularity.

The remaining problem is now a **finite-lag cross-observer compatibility problem**.

---

# 22. STOP-D99

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The old \(X/N/T\) recurrence loop can be compressed substantially once the D95 Kelvin-slip sidecar is included. D62 already proves \(N\Rightarrow X\vee T\), while D76–79 prove that no infinite X-free late-T material conveyor can remain inside a compact normalized state class. D99 upgrades that qualitative no-go by compactness: if arbitrarily long compact X-free T paths existed, a diagonal limit would produce an infinite compact X-free path, contradicting D79. Hence there is a uniform finite X-hitting horizon \(L_X\), and compactness further yields a uniform detector gap \(c_X>0\). Thus N and T are only bounded-lag routes to X on the compact branch. Independently, D95 gives a sign-coherent SGS Kelvin reset in every bounded generation block. X and Kelvin slip are therefore two syndetic clocks. Positive density alone would not imply simultaneous occurrence, so D99 corrects the implicit zero-lag assumption behind the generic reading of D96–98: their covariance cone is the co-located \(\ell=0\) subbranch. Generically, two syndetic clocks imply bounded lag; after finite detector/orientation/lag pigeonholing, one fixed oriented SGS Kelvin-slip coordinate and one fixed X72 detector recur with one fixed lag \(\ell_*\) on a positive-density set. The final compact survivor is therefore a Bounded-Lag X72–Kelvin Locked Conveyor. Eliminating it requires a finite-lag transfer/adjoint identity coupling the SGS circulation-reset source to the later/earlier X72 pressure-response state, not another local covariance normal form.
\end{minipage}
}
\]

---

# 23. Next autonomous step

## DCRP100 / X72-R83 — Finite-Lag Kelvin-to-X72 Transfer Operator

**Working title**

> **Can the Sign-Coherent SGS Circulation Reset at Generation \(n\) Produce a Fixed-Lag X72 Pressure/Projection Defect at \(n+\ell_*\) without Paying a Coercive Cross-Observer Transfer?**

Primary tasks:

1. start from:
   \[
   \sigma_*\delta_\Gamma^{\rm SGS}(n)\ge c_{\rm slip},
   \]
   \[
   X_*(n+\ell_*)\ge c_X;
   \]
2. write the normalized material/renormalization propagator:
   \[
   \mathcal U_{\ell_*};
   \]
3. transport the X72 test backward:
   \[
   \mathcal U_{\ell_*}^*\Psi_X;
   \]
4. pair it with the SGS source:
   \[
   -\nabla\cdot R_\ell;
   \]
5. separate:
   - direct SGS-to-pressure response;
   - material transport;
   - Riesz/pressure projection;
   - state mismatch;
6. derive a finite-lag Duhamel identity;
7. test whether the sign-coherent loop current has a nonzero projection onto the pulled-back X observer;
8. if the projection can vanish, classify the exact orthogonality kernel;
9. seek:
   \[
   \mathsf C_{X\Gamma}^{\ell_*}
   \Longrightarrow
   \text{cross-observer action gap}
   \vee
   R_{\rm state}
   \vee
   R_{\rm crit}
   \vee
   \text{one explicit transfer-orthogonal normal form}.
   \]

Desired endpoint:

\[
\boxed{
\text{late compact survivor}
\Longrightarrow
\text{one finite-lag transfer kernel}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP99 / X72-R82.
