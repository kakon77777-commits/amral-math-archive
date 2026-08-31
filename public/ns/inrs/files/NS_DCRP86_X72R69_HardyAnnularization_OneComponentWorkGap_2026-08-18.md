# DCRP86 / X72-R69 — Hardy Annularization of Bad-Scale Debt and the One-Component-to-Signed-Work Bottleneck

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / forest-budget audit  
**Immediate predecessor:** `NS_DCRP85_X72R68_ScaleGapDebt_CKNFiniteChain_2026-08-18.md`

**Primary internal dependencies**
- DCRP02 — shell-span / interaction-degree compiler
- DCRP20–26 — filtered residual / increment / pressure compatibility compiler
- DCRP31 — mandatory inward PFET
- DCRP62–85 — late X/T/Kelvin/trace/scale reductions

**Fresh primary-source calibration**
- Runlong Yu, *Finite-Chain CKN-Bad Scale Counting for Navier-Stokes: Standard PDE Closure and Canonical Detector Realization*, arXiv:2606.21783.
- Runlong Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322.
- Runlong Yu, *Critical Ledgers and Scale-Defect Cascades for Navier-Stokes*, arXiv:2606.13887.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP85 converted relative-scale escape into a linear finite-chain bad-scale debt.

DCRP86 performs the planned forest-budget audit and finds an important correction.

The 2026 finite-chain theorem defines the standard cost

\[
\mathfrak C_{{\rm std},k}
=
C_{3,k}
+
\mathcal L_k^{\rm ann}
+
\mathcal P_k^{\rm tail}
+
\mathcal R_k^{\rm PFE},
\]

but its actual closing proof uses only

\[
\boxed{
C_{3,k}
=
\int_{Q_1}|(u_k)_3|^3.
}
\]

The source explicitly states that the leakage, pressure-tail, and PFE coordinates are honest nonnegative ledger entries, but are **not proved to close CKN badness independently**.

Thus on a bounded critical class,

\[
\boxed{
\text{CKN-bad scale}
\Longrightarrow
C_{3,k}
\ge
\varepsilon_3(M)>0.
}
\tag{0.1}
\]

This is stronger and cleaner than merely saying the four-term standard package is positive.

DCRP86 then solves the overlap problem for these nested core one-component costs exactly.

Let

\[
r_k=\lambda^kr_0,
\qquad
0<\lambda<1,
\]

and define the physical one-component core mass

\[
\boxed{
F_k
=
\int_{Q_{r_k}}
|u_3|^3\,dxdt.
}
\tag{0.2}
\]

Then

\[
\boxed{
C_{3,k}
=
r_k^{-2}F_k.
}
\tag{0.3}
\]

Define disjoint parabolic-shell masses

\[
\boxed{
A_k
=
F_k-F_{k+1}
=
\int_{Q_{r_k}\setminus Q_{r_{k+1}}}
|u_3|^3.
}
\tag{0.4}
\]

The exact discrete Hardy identity is

\[
\boxed{
\sum_{k=0}^{K}
\frac{F_k}{r_k^2}
=
\sum_{j=0}^{K}
A_j
\sum_{k=0}^{j}\frac1{r_k^2}
+
F_{K+1}
\sum_{k=0}^{K}\frac1{r_k^2}.
}
\tag{0.5}
\]

Since

\[
\frac1{r_j^2}
\le
\sum_{k=0}^{j}\frac1{r_k^2}
\le
\frac1{1-\lambda^2}
\frac1{r_j^2},
\]

we obtain:

## Finite-chain Hardy annularization

\[
\boxed{
\sum_{j=0}^{K}
\frac{A_j}{r_j^2}
\ge
(1-\lambda^2)
\sum_{k=0}^{K}C_{3,k}
-
\frac{F_{K+1}}{r_K^2}.
}
\tag{0.6}
\]

If the full normalized critical bound at the next scale is

\[
\Psi_{K+1}(1)\le M,
\]

then

\[
C_{3,K+1}\le M
\]

and

\[
\frac{F_{K+1}}{r_K^2}
=
\lambda^2 C_{3,K+1}
\le
\lambda^2M.
\]

Therefore an all-bad chain satisfies:

## Main theorem — disjoint shell debt

\[
\boxed{
\sum_{j=0}^{K}
\frac1{r_j^2}
\int_{Q_{r_j}\setminus Q_{r_{j+1}}}
|u_3|^3
\ge
(1-\lambda^2)\varepsilon_3(M)(K+1)
-
\lambda^2M.
}
\tag{0.7}
\]

So **nested-core overlap is not the obstruction**.

It can be removed exactly.

The bad-scale debt may be represented by mutually disjoint parabolic shells.

---

# 1. Audit correction to D85

D85 used the four-term standard package:

\[
C_{3,k}
+
\mathcal L_k^{\rm ann}
+
\mathcal P_k^{\rm tail}
+
\mathcal R_k^{\rm PFE}.
\]

This is valid as a nonnegative lower-bound package.

But the source proof is more specific.

For every \(M<\infty\), the one-component compactness theorem provides:

\[
\varepsilon_3(M)>0
\]

such that:

\[
\boxed{
\Psi_k(1)\le M,
\quad
C_{3,k}\le\varepsilon_3(M)
\Longrightarrow
\Phi_k(\rho_M)<\varepsilon_{\rm CKN}.
}
\tag{1.1}
\]

Therefore contraposition gives:

## Theorem D86.1 — Pure One-Component Bad-Scale Floor

\[
\boxed{
\Phi_k(\rho_M)\ge\varepsilon_{\rm CKN}
\Longrightarrow
C_{3,k}>\varepsilon_3(M).
}
\tag{1.2}
\]

No leakage/PFE/pressure-tail lower bound is needed for this conclusion.

---

# 2. Why this matters

A proposed forest proof should not pretend that the finite-chain theorem already proves:

\[
\text{bad scale}
\Longrightarrow
\text{positive PFE work}
\]

or:

\[
\text{bad scale}
\Longrightarrow
\text{positive pressure-tail payment}.
\]

It does not.

The actual proved channel is an unsigned one-component concentration.

Thus the correct forest question is:

\[
\boxed{
\text{persistent one-component critical mass}
\stackrel{?}{\Longrightarrow}
\text{coercive signed / leaking / residual payment}.
}
\]

This is narrower than the D85 formulation.

---

# 3. Exact Hardy shell identity

Let

\[
F_k
=
\int_{Q_{r_k}}|u_3|^3.
\]

Because the cylinders are nested,

\[
F_{k+1}\le F_k.
\]

Set

\[
A_k=F_k-F_{k+1}\ge0.
\]

For \(0\le k\le K\),

\[
F_k
=
\sum_{j=k}^{K}A_j
+
F_{K+1}.
\]

Therefore:

\[
\begin{aligned}
\sum_{k=0}^{K}\frac{F_k}{r_k^2}
&=
\sum_{k=0}^{K}
\frac1{r_k^2}
\left(
\sum_{j=k}^{K}A_j+F_{K+1}
\right)
\\
&=
\sum_{j=0}^{K}
A_j
\sum_{k=0}^{j}\frac1{r_k^2}
+
F_{K+1}
\sum_{k=0}^{K}\frac1{r_k^2}.
\end{aligned}
\]

This proves (0.5).

---

# 4. Geometric Hardy constants

Since

\[
r_k=\lambda^kr_0,
\]

\[
\sum_{k=0}^{j}\frac1{r_k^2}
=
\frac1{r_j^2}
\sum_{h=0}^{j}\lambda^{2h}.
\]

Thus:

## Theorem D86.2 — Exact Geometric Weight Bounds

\[
\boxed{
\frac1{r_j^2}
\le
\sum_{k=0}^{j}\frac1{r_k^2}
\le
\frac1{1-\lambda^2}
\frac1{r_j^2}.
}
\tag{4.1}
\]

The nested core and disjoint-shell critical sums are therefore equivalent up to the fixed geometric factor \(1-\lambda^2\), plus the finite terminal core.

---

# 5. Linear shell debt

If:

\[
C_{3,k}\ge\varepsilon_3(M)
\qquad
k=0,\ldots,K,
\]

then:

\[
\sum_{k=0}^{K}C_{3,k}
\ge
\varepsilon_3(M)(K+1).
\]

Use (0.6).

If:

\[
C_{3,K+1}\le M,
\]

then:

\[
\boxed{
\sum_{j=0}^{K}
\frac{A_j}{r_j^2}
\ge
(1-\lambda^2)\varepsilon_3(M)(K+1)
-
\lambda^2M.
}
\tag{5.1}
\]

Thus the average shell debt satisfies:

\[
\boxed{
\frac1{K+1}
\sum_{j=0}^{K}
\frac{A_j}{r_j^2}
\ge
(1-\lambda^2)\varepsilon_3(M)
-
\frac{\lambda^2M}{K+1}.
}
\tag{5.2}
\]

For large \(K\), the average is uniformly positive.

---

# 6. Parabolic shell decomposition

Each parabolic shell decomposes disjointly as:

\[
Q_{r_j}\setminus Q_{r_{j+1}}
=
\mathcal S_j^{\rm time}
\dot\cup
\mathcal S_j^{\rm space},
\]

where:

\[
\boxed{
\mathcal S_j^{\rm time}
=
B_{r_j}
\times
(-r_j^2,-r_{j+1}^2),
}
\tag{6.1}
\]

and:

\[
\boxed{
\mathcal S_j^{\rm space}
=
(B_{r_j}\setminus B_{r_{j+1}})
\times
(-r_{j+1}^2,0).
}
\tag{6.2}
\]

Define:

\[
A_j^{\rm time}
=
\int_{\mathcal S_j^{\rm time}}|u_3|^3,
\]

\[
A_j^{\rm space}
=
\int_{\mathcal S_j^{\rm space}}|u_3|^3.
\]

Then:

\[
A_j=A_j^{\rm time}+A_j^{\rm space}.
\]

Therefore:

## Corollary D86.3 — Spatial/Temporal Shell Debt Dichotomy

At least one of:

\[
\boxed{
\sum_{j=0}^{K}
\frac{A_j^{\rm space}}{r_j^2}
}
\]

or:

\[
\boxed{
\sum_{j=0}^{K}
\frac{A_j^{\rm time}}{r_j^2}
}
\]

carries at least half of the lower bound (5.1).

So the bad-scale debt is forced into:

- spatial annular one-component mass;
- temporal inter-generation one-component mass;
- or both.

This is a true disjoint-support decomposition.

---

# 7. Forest-overlap problem solved at the mass level

The original forest worry was:

> every normalized core \(Q_{r_k}\) contains all smaller cores, so summing \(C_{3,k}\) may repeatedly count the same physical mass.

D86 proves:

\[
\boxed{
\text{nested core debt}
\asymp
\text{disjoint parabolic shell debt}
}
\]

up to fixed constants and one terminal core.

Thus **overlap multiplicity is not the final difficulty for the one-component channel**.

The physical shells are pairwise disjoint.

---

# 8. But disjoint shells are still critical

This does not produce a global contradiction.

Consider the exact critical model:

\[
\boxed{
F(r)
=
c r^2.
}
\tag{8.1}
\]

Then:

\[
\boxed{
C_3(r)
=
r^{-2}F(r)
=
c.
}
\tag{8.2}
\]

For:

\[
r_{j+1}=\lambda r_j,
\]

the shell mass is:

\[
A_j
=
c(r_j^2-r_{j+1}^2)
=
c(1-\lambda^2)r_j^2.
\]

Therefore:

\[
\boxed{
\frac{A_j}{r_j^2}
=
c(1-\lambda^2)
}
\tag{8.3}
\]

at every scale.

The physical total mass is nevertheless finite:

\[
\boxed{
\sum_j A_j
=
cr_0^2.
}
\tag{8.4}
\]

So:

## Theorem D86.4 — Critical Shell Summability NO-GO

A linear divergence of the **normalized** disjoint-shell debt is compatible with a finite physical \(L^3\) mass.

Therefore annularization solves overlap but does not create a coercive global budget.

This is the precise distinction needed for the endgame.

---

# 9. Why ordinary energy/dissipation does not immediately repair it

Scale-critical one-component shell mass is compatible with:

\[
A_j
\sim
r_j^2.
\]

Any physical cost that scales with a positive power of \(r_j\) can remain geometrically summable.

Thus a successful forest closure needs either:

1. a genuinely telescoping signed quantity;
2. a dimensionless non-summable tax;
3. a compactness theorem ruling out the critical equality profile;
4. or a recurrent defect whose normalized payment cannot be concentrated into geometrically shrinking physical mass.

This is why the signed pressure–flux work route matters.

---

# 10. Coarse-grained CKN resolution

The 2026 coarse-grained resolution theorem gives, at every fixed relative filter scale:

\[
\boxed{
\Psi(r)
\le
4\Psi^\ell(r)
+
4\Omega^\ell(r),
}
\tag{10.1}
\]

where:

- \(\Psi^\ell\) = resolved velocity-pressure badness;
- \(\Omega^\ell\) = subfilter velocity-pressure residual.

Therefore any CKN-bad scale has the exact alternative:

\[
\boxed{
\Omega^\ell
\ge
\frac18\varepsilon_{\rm CKN}
}
\]

or:

\[
\boxed{
\Psi^\ell
\ge
\frac18\varepsilon_{\rm CKN}.
}
\tag{10.2}
\]

Constants may be replaced by any fixed split below \(1/4\).

---

# 11. Residual-active scales are already in the old compiler

If the subfilter residual is active at a positive density of bad scales, the forest has already entered:

- velocity-increment / derivative-compatible residual;
- pressure residual;
- scale/fiber escape;
- or unresolved concentration.

Those are precisely the DCRP20–26 coordinates.

Thus the genuinely new forest problem lies on the **resolved branch**:

\[
\boxed{
\Psi^\ell
\ge
c_0>0
}
\]

on many scales.

---

# 12. Signed combined pressure–flux work

Define the coarse-grained Reynolds stress:

\[
R^\ell
=
S_\ell(u\otimes u)-U^\ell\otimes U^\ell,
\]

the interscale work:

\[
\boxed{
\Pi^\ell
=
-R^\ell:\nabla U^\ell,
}
\]

and the combined pressure–flux work:

\[
\boxed{
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
}
\tag{12.1}
\]

The current coarse-grained work theorem proves:

- exact local resolved-energy identities;
- constructive active-work extraction for finite-dimensional test families;
- weighted finite-chain telescoping;
- forward combined work + resolved dissipation are paid by initial kinetic energy, localization leakage, and negative work/backscatter.

This is the correct type of object for a coercive forest budget.

---

# 13. But the critical observability implication is open

The same source explicitly isolates the difficult bridge:

\[
\boxed{
\Psi^\ell(r_k)
\ge
c_0\varepsilon_0
\stackrel{?}{\Longrightarrow}
\mathfrak A_k(G^\ell)
\ge
c_{\rm obs}.
}
\tag{13.1}
\]

It is **not proved**.

The source lists possible failure modes including:

- subfilter residual concentration;
- harmonic pressure tails;
- pressure–flux cancellation;
- coherent low-frequency resolved profiles;
- leakage;
- backscatter.

Many of these already occur in the present terminal compiler.

Thus the forest endgame is now aligned with an independently identified modern Navier–Stokes observability gap.

---

# 14. D86 forest normal form

Combine the new annularization with coarse resolution.

An arbitrarily long bounded-critical bad-scale chain must satisfy:

\[
\boxed{
\text{linear disjoint one-component shell debt}.
}
\]

At fixed relative filter scale, it also splits into:

\[
\boxed{
\text{subfilter residual activity}
}
\]

or:

\[
\boxed{
\text{resolved CKN activity}.
}
\]

The first branch is already covered.

The second can become a genuinely bounded signed-work budget **only if** coarse resolved badness is observable by \(G^\ell\).

Therefore:

## Theorem D86.5 — Forest Reduction

\[
\boxed{
\text{long bad-scale forest}
\Longrightarrow
\mathsf R_{\rm subfilter}
\vee
\mathsf R_{\rm OW},
}
\tag{14.1}
\]

where:

\[
\boxed{
\mathsf R_{\rm OW}
=
\text{resolved-badness / signed-work observability problem}.
}
\]

This is not a new physical force.

It is the missing bridge between an unsigned critical reservoir and a signed depletion channel.

---

# 15. What \(R_{\rm OW}\) must classify

A failure of:

\[
\Psi^\ell
\Rightarrow
\text{positive active }G^\ell
\]

must be caused by at least one of:

1. harmonic pressure-tail dominance;
2. pressure–flux cancellation;
3. coherent low-frequency resolved motion;
4. localization leakage;
5. backscatter;
6. active-work test-family invisibility.

The first, fourth, and residual parts are already named terminal costs.

The second, third, fifth, and sixth are the true efficiency/observability geometry.

---

# 16. Relation to D49 independence warning

D86 does **not** identify:

\[
\text{PFET}
=
G^\ell
\]

or:

\[
\text{pressure defect}
=
G^\ell.
\]

D49 already forbids such universal scalar identification.

The desired closure is weaker and correct:

\[
\boxed{
\text{persistent resolved badness}
\Longrightarrow
\text{some signed work visibility}
\vee
\text{explicit cancellation/invisibility defect}.
}
\]

This is a joint-realizability problem.

---

# 17. Relation to X72

If the failure of signed-work observability is carried by pressure–flux cancellation, the next useful question is whether the pressure component can remain X72-perfect:

\[
E_p=0
\]

while the resolved coarse work remains invisible.

The D61–79 chain has already eliminated many coherent pressure-perfect recurrent geometries.

Thus X72 is now relevant **after** the observability failure is classified, not before.

This avoids forcing a false direct \(C_3\to X\) implication.

---

# 18. A discrete Hardy theorem for the infinite chain

If:

\[
F_k\to0
\]

and all quantities are nonnegative, monotone convergence gives:

\[
\boxed{
\sum_{k=0}^{\infty}
\frac{F_k}{r_k^2}
=
\sum_{j=0}^{\infty}
A_j
\sum_{k=0}^{j}
\frac1{r_k^2}.
}
\tag{18.1}
\]

Hence:

## Theorem D86.6 — Infinite Hardy Equivalence

\[
\boxed{
\sum_{j=0}^{\infty}
\frac{A_j}{r_j^2}
\le
\sum_{k=0}^{\infty}
C_{3,k}
\le
\frac1{1-\lambda^2}
\sum_{j=0}^{\infty}
\frac{A_j}{r_j^2}.
}
\tag{18.2}
\]

So divergence of the bad-scale core count is **equivalent** to divergence of the disjoint critical shell measure.

This is an exact structural result.

---

# 19. The correct forest-budget target

The target is no longer:

> “show nested CKN channel costs have bounded overlap.”

For the one-component channel, D86 has already resolved overlap.

The correct target is:

> “show a uniformly positive disjoint-shell critical reservoir cannot recur indefinitely without generating a signed telescoping work, a subfilter residual, a pressure-tail/leakage/backscatter payment, or a coherent invisibility state already forbidden by X72.”

This is substantially more specific.

---

# 20. Status ledger

## PROVED this round

### D86-P1 — source audit correction

The finite-chain standard theorem closes through the vertical one-component channel; additional standard channels are not independently proved closers.

### D86-P2 — pure one-component bad-scale floor

\[
\text{bad}+\Psi\le M
\Longrightarrow
C_3\ge\varepsilon_3(M).
\]

### D86-P3 — exact finite discrete Hardy identity for nested cores.

### D86-P4 — nested core / disjoint parabolic shell equivalence.

### D86-P5 — linear disjoint shell debt

\[
\sum
r_j^{-2}
\int_{Q_{r_j}\setminus Q_{r_{j+1}}}
|u_3|^3
\gtrsim
K.
\]

### D86-P6 — spatial-annular / temporal-shell debt dichotomy.

### D86-P7 — critical model \(F(r)=cr^2\) proves normalized shell debt can diverge while physical \(L^3\) mass remains finite.

### D86-P8 — forest overlap is not the final problem.

### D86-P9 — coarse-grained CKN resolution reduces the remaining forest to subfilter residual activity or resolved badness.

### D86-P10 — the final unresolved bridge is resolved-badness-to-signed-work observability.

---

# 21. What is not proved

D86 does not prove:

- one-component shell debt implies positive PFET;
- one-component shell debt implies X72;
- resolved CKN badness forces positive \(G^\ell\);
- signed work has a scale-tree bounded-overlap theorem in the present same-parent geometry;
- pressure–flux cancellation cannot recur;
- backscatter cannot finance the cascade;
- global regularity.

The remaining problem is now an observability/depletion interface.

---

# 22. New STOP

\[
\boxed{
\textbf{
STOP-D86:
The forest-overlap problem can be solved exactly at the channel that actually closes the current finite-chain theorem. A bounded-critical CKN-bad scale forces the vertical one-component cost }C_3\ge\varepsilon_3(M)\textbf{; the source theorem does not independently close through leakage, pressure-tail, or PFE terms. The heavily overlapping nested core costs admit an exact discrete Hardy annularization into pairwise-disjoint parabolic-shell }|u_3|^3\textbf{ masses, giving a linear shell debt across every long bad-scale chain. But this is still a critical unsigned reservoir: the model }F(r)=cr^2\textbf{ has constant normalized shell debt and finite physical mass, so no global coercivity follows from packing alone. Coarse-grained CKN resolution now leaves exactly two routes: an already-known subfilter residual, or persistent resolved badness. Modern pressure--flux work depletion can telescope signed resolved work, but the implication “resolved badness forces observable signed work” is explicitly open. Thus the late forest endgame has reduced to the one-component/resolved-reservoir-to-signed-work observability problem, with pressure-tail, cancellation, coherent low-frequency motion, leakage, and backscatter as the only declared escape mechanisms.}
}
\]

---

# 23. Next autonomous step

## DCRP87 / X72-R70 — Resolved Badness / Signed Pressure–Flux Work Observability

**Working title**

> **Can Persistent Resolved One-Component Badness Remain Orthogonal to Every Signed Pressure–Flux Work Test?**

Primary tasks:

1. start from the D86 disjoint shell debt;
2. filter at fixed relative scale:
   \[
   \ell=\sigma r;
   \]
3. route subfilter residual activity back to the existing increment/pressure-residual compiler;
4. on the resolved branch, construct a finite-dimensional active test family adapted to the one-component shell carrier;
5. compute the combined work:
   \[
   G^\ell
   =
   -R^\ell:\nabla U^\ell
   +
   \nabla\cdot(P^\ell U^\ell);
   \]
6. classify exact zero-work configurations;
7. test whether persistent work-orthogonality forces:
   - harmonic pressure tail;
   - pressure–flux cancellation;
   - coherent affine/low-frequency profile;
   - backscatter;
   - or X72 pressure-response defect;
8. seek:
   \[
   R_{\rm OW}
   \Longrightarrow
   X
   \vee
   R_{\rm tail}
   \vee
   R_{\rm back}
   \vee
   R_{\rm low}
   \vee
   R_{\rm state}.
   \]

Desired endpoint:

\[
\boxed{
\text{long bad-scale forest}
\Longrightarrow
\text{signed telescoping depletion}
\vee
\text{finite explicit invisibility normal form}.
}
\]

---

# 24. One-line checkpoint

The scale-gap forest no longer suffers from nested-core overcounting: its actual one-component bad-scale cost can be exactly annularized into disjoint critical shells, and the only remaining obstruction is converting that unsigned resolved shell reservoir into signed pressure–flux work or one of a finite list of explicit work-invisibility defects.

---

**End checkpoint:** DCRP86 / X72-R69  
**Next:** DCRP87 / X72-R70 — Resolved Badness / Signed Pressure–Flux Work Observability.
