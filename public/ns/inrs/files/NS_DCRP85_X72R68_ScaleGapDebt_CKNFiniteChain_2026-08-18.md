# DCRP85 / X72-R68 — Relative-Scale Escape as UV/IR Endpoint and the Finite-Chain Scale-Gap Debt

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-18  
**Status:** Proof-development checkpoint / relative-scale escape round  
**Immediate predecessor:** `NS_DCRP84_X72R67_LogCapacity_MatchedAtom_ScaleEscape_2026-08-18.md`

**Primary internal dependencies**
- DCRP02 — cross-scale interaction graph / shell-span / dissipation-driver debt
- DCRP18–20 — two-sided relative-frequency completion and diffusion/IR dichotomy
- DCRP21 — far-field annular escape
- DCRP24 — increment-fiber escape
- DCRP84 — Kelvin/trace route reduced to relative-scale escape

**Fresh primary-source calibration**
- R. Yu, *Finite-Chain CKN-Bad Scale Counting for Navier-Stokes: Standard PDE Closure and Canonical Detector Realization*, arXiv:2606.21783 (2026). It proves a single-scale standard-channel concentration theorem and weighted/unweighted finite-chain counting for CKN-bad scales under a uniform full local critical bound, and separately constructs an amended canonical detector using energy, flux, pressure-tail, low-pressure-mode, and finite-dimensional residual coordinates.
- R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier-Stokes*, arXiv:2606.13887 (2026). Persistent scale-critical badness across finite chains must pay untaxed supply or leakage/tax channels.
- R. Yu, *Invisible Defect Cascades for Navier-Stokes Regularity*, arXiv:2606.12756 (2026). Scale-critical survival is organized as a recurrence/defect-cascade problem rather than an energy-only concentration problem.
- I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the \(L^\infty_t(L^3_x)\) Navier-Stokes regularity criterion*, arXiv:1012.0145. Used only as background calibration that asymptotically separated scales are a genuine critical-profile noncompactness coordinate.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP84 reduced the entire Kelvin / material-line trace route to the old scale-escape coordinate

\[
\boxed{
R_{\rm scale}.
}
\]

Write an infinite nested carrier chain as

\[
\boxed{
r_0>r_1>r_2>\cdots\downarrow0.
}
\]

The silent matched-line route of D84 requires

\[
\boxed{
q_j:=\frac{r_{j+1}}{r_j}\to0
}
\]

along a subsequence.

Define the dyadic gap depth

\[
\boxed{
m_j
:=
\left\lfloor
\log_2\frac{r_j}{r_{j+1}}
\right\rfloor.
}
\tag{0.1}
\]

Then

\[
\boxed{
q_j\to0
\iff
m_j\to\infty.
}
\tag{0.2}
\]

DCRP85 proves that this is not a new terminal geometric mechanism.

It has two exact interpretations.

---

## Interpretation I — two-observer UV/IR endpoint

At the parent scale \(r_j\), the child frequency is

\[
\frac{r_j}{r_{j+1}}
\sim
2^{m_j}
\to\infty.
\]

So the child is a **relative UV/shell-label escape**.

At the child scale \(r_{j+1}\), the parent frequency is

\[
\frac{r_{j+1}}{r_j}
\sim
2^{-m_j}
\to0.
\]

So the same gap is a **relative IR escape**.

Thus:

\[
\boxed{
R_{\rm scale}
=
R_{\rm UV}^{\rm(parent)}
=
R_{\rm IR}^{\rm(child)}
}
\tag{0.3}
\]

in the two-sided relative-frequency compactification.

This is exactly the old DCRP18–20 scale endpoint, seen from opposite rerootings.

---

## Interpretation II — CKN scale-gap debt

Fix one gap:

\[
[r_{j+1},r_j].
\]

Define the intermediate dyadic scales

\[
\boxed{
\rho_{j,k}
=
2^{-k}r_j,
\qquad
k=0,\ldots,m_j.
}
\tag{0.4}
\]

On a genuine singular same-parent branch, once the scales are sufficiently small, **every** such intermediate scale must be CKN-bad; otherwise one CKN-small scale would give regularity on a smaller cylinder.

Assume the finite chain also satisfies the uniform full local critical bound required by the 2026 finite-chain counting theorem:

\[
\boxed{
\Psi(\rho_{j,k})
\le M
\qquad
\forall k=0,\ldots,m_j.
}
\tag{0.5}
\]

Let

\[
\boxed{
\mathfrak C^{\rm std}_{j,k}
}
\]

denote the non-tautological standard channel package of that theorem:

- vertical one-component concentration;
- annular leakage;
- pressure-tail cost;
- pressure–flux–energy residual.

The single-scale theorem supplies a constant

\[
\boxed{
c_{\rm std}(M)>0
}
\]

such that every CKN-bad scale in the bounded class satisfies

\[
\boxed{
\mathfrak C^{\rm std}_{j,k}
\ge
c_{\rm std}(M).
}
\tag{0.6}
\]

Hence:

## Main theorem — Scale-Gap Debt

\[
\boxed{
\sum_{k=0}^{m_j}
\mathfrak C^{\rm std}_{j,k}
\ge
c_{\rm std}(M)
(m_j+1).
}
\tag{0.7}
\]

Equivalently:

\[
\boxed{
\frac1{m_j+1}
\sum_{k=0}^{m_j}
\mathfrak C^{\rm std}_{j,k}
\ge
c_{\rm std}(M).
}
\tag{0.8}
\]

Thus an arbitrarily large relative-scale jump cannot be a **silent skipped band**.

Every skipped bad shell carries a uniform standard-PDE payment.

---

# 1. Exact dyadic gap geometry

Let:

\[
q_j=\frac{r_{j+1}}{r_j}.
\]

Then:

\[
m_j
=
\left\lfloor
-\log_2q_j
\right\rfloor.
\]

Therefore:

## Theorem D85.1 — Gap/Ratio Equivalence

\[
\boxed{
q_j\to0
\iff
m_j\to\infty.
}
\tag{1.1}
\]

Also:

\[
\boxed{
2^{m_j}
\le
\frac{r_j}{r_{j+1}}
<
2^{m_j+1}.
}
\tag{1.2}
\]

No PDE input is used here.

---

# 2. Parent normalization: UV escape

At parent scale \(r_j\), a physical Fourier frequency associated with the child scale is:

\[
|\xi_{j+1}|
\sim
r_{j+1}^{-1}.
\]

The normalized parent frequency is:

\[
\boxed{
r_j|\xi_{j+1}|
\sim
\frac{r_j}{r_{j+1}}
\sim
2^{m_j}.
}
\tag{2.1}
\]

Hence:

\[
m_j\to\infty
\Longrightarrow
r_j|\xi_{j+1}|\to\infty.
\]

This is a relative ultraviolet endpoint.

---

# 3. Child normalization: IR escape

At child scale \(r_{j+1}\), the parent frequency is:

\[
|\xi_j|
\sim
r_j^{-1}.
\]

The normalized child frequency is:

\[
\boxed{
r_{j+1}|\xi_j|
\sim
\frac{r_{j+1}}{r_j}
\sim
2^{-m_j}.
}
\tag{3.1}
\]

Thus:

\[
m_j\to\infty
\Longrightarrow
r_{j+1}|\xi_j|\to0.
\]

This is a relative infrared endpoint.

---

# 4. Two-sided relative-frequency identity

DCRP18 completed the relative-frequency state space by retaining both frequency endpoints.

D85 gives the exact material rerooting identity:

## Theorem D85.2 — UV/IR Duality of One Scale Gap

\[
\boxed{
R_{\rm UV}^{\rm(parent)}
\Longleftrightarrow
R_{\rm IR}^{\rm(child)}.
}
\tag{4.1}
\]

They are not two independent branches.

They are the same physical scale separation under opposite normalization.

This removes one possible duplication in the terminal compiler.

---

# 5. Relation to DCRP02 interaction degree

DCRP02 proves:

> inside a bounded relative shell band and bounded normalized spatial span, the cross-scale interaction graph has uniformly bounded partner degree.

Therefore order-one diffuse cross-scale supply cannot remain simultaneously:

- bounded in relative shell offset;
- bounded in normalized spatial span;
- atomless.

It must produce:

\[
\boxed{
\text{ATOM}
\vee
\text{shell-span growth}
\vee
\text{far/spatial span}.
}
\]

The D84 survivor is explicitly atomless in the volumetric detector and keeps pushing the matched atom to a much smaller generation.

Therefore:

## Theorem D85.3 — D84 Scale Escape Is DCRP02 Shell Span

\[
\boxed{
R_{\rm scale}
\subseteq
R_{\rm shellspan}
\vee
R_{\rm tail}
\vee
R_{\rm state}.
}
\tag{5.1}
\]

On the pure nested-scale route with bounded spatial location:

\[
\boxed{
R_{\rm scale}
=
R_{\rm shellspan}.
}
\tag{5.2}
\]

DCRP02 already routes canonical parent-shell multiplicity to:

\[
\boxed{
\text{dissipation-span / driver debt}.
}
\]

So \(R_{\rm scale}\) is not new.

---

# 6. Why shell-span classification alone was insufficient

DCRP02 explicitly warned:

\[
\boxed{
\text{interaction multiplicity}
\not\Rightarrow
\text{contradiction}.
}
\]

The missing item was a strict quantitative debt.

D85 obtains such a debt from a different theorem: finite-chain CKN-bad scale counting.

The shell gap itself supplies the finite chain.

---

# 7. Singular-point badness across the entire skipped band

Take:

\[
\rho_{j,k}
=
2^{-k}r_j.
\]

Suppose some sufficiently small intermediate scale were CKN-small.

Then classical CKN epsilon regularity would make the solution regular in a smaller cylinder around the same point.

That contradicts the assumed singular-point branch.

Therefore, for \(j\) sufficiently deep:

## Theorem D85.4 — No Clean Intermediate Scale

\[
\boxed{
\mathcal B_j
=
\{0,\ldots,m_j\}.
}
\tag{7.1}
\]

Every dyadic shell inside a genuine singular skipped band is CKN-bad.

The carrier cannot “teleport” through a band of regular scales.

---

# 8. Standard finite-chain channel package

Use the non-tautological standard package from the finite-chain counting theorem.

Write schematically:

\[
\boxed{
\mathfrak C_{j,k}^{\rm std}
=
C_{3,j,k}
+
L_{j,k}^{\rm ann}
+
P_{j,k}^{\rm tail}
+
R_{j,k}^{\rm PFE}.
}
\tag{8.1}
\]

Each term is nonnegative.

The theorem excludes the full CKN core norm from the package.

Thus the statement:

\[
\mathfrak C^{\rm std}\ge c_{\rm std}(M)
\]

on a bad scale is not a tautological rewriting of CKN badness.

---

# 9. Linear gap debt

Under the uniform full critical bound:

\[
\Psi\le M
\]

on every intermediate normalized scale, the single-scale concentration theorem gives:

\[
\mathfrak C_{j,k}^{\rm std}
\ge
c_{\rm std}(M).
\]

Sum over:

\[
k=0,\ldots,m_j.
\]

## Theorem D85.5 — Linear CKN Gap Debt

\[
\boxed{
\mathfrak D_{\rm gap}(j)
:=
\sum_{k=0}^{m_j}
\mathfrak C_{j,k}^{\rm std}
\ge
c_{\rm std}(M)
(m_j+1).
}
\tag{9.1}
\]

Hence:

\[
m_j\to\infty
\Longrightarrow
\mathfrak D_{\rm gap}(j)\to\infty.
\]

More importantly:

\[
\boxed{
\frac{
\mathfrak D_{\rm gap}(j)
}{
m_j+1
}
\ge
c_{\rm std}(M).
}
\tag{9.2}
\]

The debt is not concentrated only at the gap endpoints.

There is a positive average standard-channel payment per skipped bad shell.

---

# 10. Weighted gap debt

The 2026 theorem is actually weighted.

For arbitrary:

\[
w_k\ge0,
\]

one has a finite-chain estimate controlling the weighted bad-scale count by the corresponding weighted standard costs.

Thus one may emphasize:

- the center of the gap;
- one half of the gap;
- selected shell bands.

D85 does not need a particular weight.

The unweighted choice:

\[
w_k=1
\]

is already enough for (9.1).

---

# 11. If the uniform full critical bound fails

The finite-chain theorem requires a uniform critical bound:

\[
\Psi\le M.
\]

Suppose no fixed \(M\) works across the skipped bands.

Then there exists:

\[
\boxed{
\Psi(\rho_{j,k_j})\to\infty.
}
\tag{11.1}
\]

This is not a silent relative-scale jump.

It is a critical-reservoir / pressure / state-amplitude escape.

In the current compiler it belongs to the already-retained:

\[
\boxed{
R_{\rm state}
\vee
R_{\rm tail}
\vee
\text{critical-reservoir escape}.
}
\]

Therefore the scale branch has the complete alternative:

## Theorem D85.6 — Bounded-Window / Reservoir-Escape Dichotomy

\[
\boxed{
R_{\rm scale}
\Longrightarrow
\mathfrak D_{\rm gap}
\ \vee
R_{\rm crit}.
}
\tag{11.2}
\]

Here \(R_{\rm crit}\) denotes failure of the uniform full local critical bound and is an already-known reservoir/state noncompactness, not a new equality state.

---

# 12. Canonical detector realization

The same 2026 paper separately constructs an amended canonical detector using:

- energy;
- flux;
- pressure-tail;
- retained low pressure modes;
- finite-dimensional residuals.

It proves finite-chain counting for that amended detector.

However the finite-window realization constants are not silently assumed uniform in arbitrary chain length.

Therefore D85 uses the **standard-PDE theorem** for the uniform linear gap debt.

The amended canonical detector is used only as a structural calibration:

\[
\boxed{
\text{the gap debt can be represented by named finite-scale PDE observables}.
}
\]

No identification of the two counting theorems is claimed.

---

# 13. Scale escape is no longer a zero-cost terminal branch

D84 ended with:

\[
R_K
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
R_{\rm scale}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm tail}.
\]

Insert D85.6.

Then:

## Theorem D85.7 — Kelvin/Trace/Scale Closure to Paid Channels

\[
\boxed{
R_K
\Longrightarrow
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm crit}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm tail}.
}
\tag{13.1}
\]

The old mysterious chain:

\[
R_K
\to
R_{\rm tr}
\to
R_{\rm atom}
\to
R_{\rm scale}
\]

has terminated in:

\[
\boxed{
\text{existing finite-scale increment activity}
}
\]

or:

\[
\boxed{
\text{linear CKN gap debt}
}
\]

or already-known noncompactness.

There is no further silent geometry in this route.

---

# 14. Corrected terminal compiler

The late rank-two architecture may now be written:

\[
\boxed{
\mathsf O_{\rm PFET}
\wedge
\left(
\mathsf X
\vee
\widetilde{\mathcal S}_{\rm vol}^{\rm active}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
R_{\rm crit}
\right).
}
\tag{14.1}
\]

The important change is conceptual.

There is no longer an unpriced:

\[
R_{\rm scale}.
\]

It has become a **paid finite-chain bad-scale ledger**.

---

# 15. Why this still does not prove regularity

From:

\[
\mathfrak D_{\rm gap}(j)
\ge
c_{\rm std}m_j
\]

one must **not** conclude immediately that an infinite singular chain is impossible.

The standard channel costs across nested cylinders can overlap.

The finite-chain theorem is deliberately a finite-scale counting theorem.

It does not supply a single globally finite measure whose total mass bounds:

\[
\sum_j
\mathfrak D_{\rm gap}(j).
\]

Therefore D85 closes **silent scale skipping**, not Navier–Stokes regularity.

---

# 16. What has actually improved

Before D85, a survivor could say:

> “I will simply jump from \(r_j\) to a much smaller \(r_{j+1}\), avoiding all comparable-scale recurrence.”

After D85 this statement is incomplete.

The skipped dyadic block itself is part of the singular solution.

Every intermediate scale is bad.

Hence an \(m_j\)-shell jump creates:

\[
\boxed{
O(m_j)
}
\]

standard-PDE channel obligations.

So scale sparsity is not free.

---

# 17. Relation to the DCRP02 shell-span debt

DCRP02 routed shell-label multiplicity abstractly to:

\[
\boxed{
\text{dissipation-span / driver debt}.
}
\]

D85 supplies a concrete standard-PDE realization of the same philosophy:

\[
\boxed{
\text{unbounded shell gap}
\Longrightarrow
\text{linear bad-scale channel debt}
}
\]

on a bounded critical class.

Thus the late Kelvin route and the earlier interaction-graph route have reconverged again.

---

# 18. Two-observer summary

One scale gap has three equivalent descriptions.

## material geometry

\[
\boxed{
r_{j+1}/r_j\to0;
}
\]

## parent observer

\[
\boxed{
\text{UV shell-span escape};
}
\]

## child observer

\[
\boxed{
\text{IR relative-frequency escape}.
}
\]

And at a singular point:

## PDE ledger

\[
\boxed{
\text{long finite chain of CKN-bad scales}.
}
\]

Therefore:

## Theorem D85.8 — Four-Language Scale-Gap Equivalence

\[
\boxed{
R_{\rm scale}
=
R_{\rm shellspan}
=
R_{\rm UV/IR}
=
R_{\rm bad\mbox{-}chain}
}
\]

at the level of the declared same-parent scale coordinates, with the final equality interpreted through the dyadic skipped-band construction.

This is the main architecture theorem of the round.

---

# 19. New remaining quantitative problem

The geometry is now exhausted.

The strongest remaining question is:

> can the standard channel payments forced at every bad scale be coupled to a genuinely finite/coercive **forest budget**, rather than merely counted with overlapping finite-window costs?

This is exactly the point DCRP02 had already identified:

\[
\boxed{
\text{turn recurring structures into a strict packing/coherence tax}.
}
\]

The late proof tree has independently returned to the same frontier.

---

# 20. Candidate next aggregate

For a skipped gap define:

\[
\boxed{
\mathfrak A_{\rm gap}
=
\sum_{k=0}^{m_j}
\left[
L_{j,k}^{\rm ann}
+
P_{j,k}^{\rm tail}
+
R_{j,k}^{\rm PFE}
\right].
}
\]

Separate the one-component closing coordinate:

\[
\boxed{
\mathfrak V_{\rm gap}
=
\sum_{k=0}^{m_j}
C_{3,j,k}.
}
\]

Then:

\[
\boxed{
\mathfrak V_{\rm gap}
+
\mathfrak A_{\rm gap}
\ge
c_{\rm std}(M)
(m_j+1).
}
\tag{20.1}
\]

A useful next theorem would prove that at least one of:

1. \(\mathfrak A_{\rm gap}\) maps to existing PFET/X/tail/state costs with bounded overlap;
2. \(\mathfrak V_{\rm gap}\) creates a compact one-component recurrence that contradicts the rank-two/X72 geometry;
3. the overlap multiplicity of the gap ledger itself diverges and becomes a new forest/coherence cost.

That is now a quantitative budget problem, not a branch-classification problem.

---

# 21. Status ledger

## PROVED / established this round

### D85-P1 — exact scale ratio / dyadic gap equivalence

\[
q_j\to0
\iff
m_j\to\infty.
\]

### D85-P2 — parent-UV / child-IR duality.

### D85-P3 — D84 \(R_{\rm scale}\) is the old DCRP02 shell-span coordinate on the bounded-spatial branch.

### D85-P4 — no CKN-small intermediate dyadic scale can occur on the singular same-parent branch.

### D85-P5 — under a uniform full local critical bound, every skipped bad scale carries a positive standard channel cost.

### D85-P6 — linear scale-gap debt

\[
\mathfrak D_{\rm gap}
\ge
c_{\rm std}(M)(m_j+1).
\]

### D85-P7 — if the uniform critical bound fails, the gap is already a critical-reservoir/state escape.

### D85-P8 — \(R_{\rm scale}\) is no longer a silent terminal branch.

### D85-P9 — the Kelvin/trace/line-atom route has fully reconverged to existing increment/channel/noncompactness coordinates.

---

# 22. What is not proved

D85 does not prove:

- the cumulative standard channel debt has a globally finite budget;
- different skipped gaps have bounded overlap;
- the one-component standard closing channel maps directly to X72;
- pressure–flux–energy channel payments alone close CKN;
- \(R_{\rm crit}\) is impossible;
- Navier–Stokes regularity.

The remaining gap is a **forest-budget / overlap / coercivity problem**.

---

# 23. New STOP

\[
\boxed{
\textbf{
STOP-D85:
The last relative-scale escape is not a new terminal mechanism and is not free. If }r_{j+1}/r_j\to0\textbf{, the dyadic gap depth }m_j\sim\log_2(r_j/r_{j+1})\textbf{ diverges. In parent normalization this is UV shell-span escape; in child normalization it is the same IR relative-frequency endpoint. At a genuine singular point every sufficiently small intermediate dyadic scale in that skipped band is CKN-bad. Under the uniform full critical bound of the finite-chain counting theorem, each bad scale carries a fixed positive non-tautological standard PDE channel cost, so the total skipped-band debt is at least }c(M)m_j\textbf{. If that full bound fails, the branch has already paid through critical-reservoir/state escape. Thus }R_{\rm scale}\textbf{ has been converted from a silent geometric escape into a linear finite-chain scale-gap debt. The remaining problem is no longer to classify another escape route, but to prove a bounded-overlap/coercive forest budget for these recurring channel payments.}
}
\]

---

# 24. Next autonomous step

## DCRP86 / X72-R69 — Scale-Gap Forest Budget / Channel Confluence

**Working title**

> **Can the Linear CKN Gap Debt Be Packed into PFET/X/Tail/State Budgets with Bounded Overlap?**

Primary tasks:

1. start from:
   \[
   \mathfrak D_{\rm gap}
   \ge
   c(M)m_j;
   \]
2. split the standard gap debt into:
   - one-component concentration;
   - annular leakage;
   - pressure-tail;
   - PFE residual;
3. map annular leakage / pressure-tail into:
   \[
   R_{\rm tail}\vee R_{\rm state};
   \]
4. compare PFE residual with:
   \[
   O_{\rm PFET}\vee X;
   \]
   without violating D49 independence;
5. analyze the one-component channel under the rank-two/X72 geometry;
6. build a dyadic forest of skipped gaps and compute overlap multiplicity of the channel supports;
7. seek a Carleson/packing estimate:
   \[
   \sum_{\text{disjoint gap tree}}
   m_j
   \lesssim
   \text{finite physical budget};
   \]
8. if overlap multiplicity diverges, retain it as an explicit coherence/forest defect.

Desired endpoint:

\[
\boxed{
\text{scale-gap debt}
\Longrightarrow
\text{known bounded-overlap paid channels}
\vee
\text{one explicit forest-coherence defect}.
}
\]

---

# 25. One-line checkpoint

The Kelvin-to-trace-to-line-atom chain has now ended at a quantitative scale ledger: every arbitrarily large skipped scale band is simultaneously a parent-UV/child-IR shell-span endpoint and, at a singular point with bounded critical reservoir, a linearly expensive finite chain of CKN-bad scales.

---

**End checkpoint:** DCRP85 / X72-R68  
**Next:** DCRP86 / X72-R69 — Scale-Gap Forest Budget / Channel Confluence.
