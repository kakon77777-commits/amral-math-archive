# DCRP93 / X72-R76 — Homogeneity-Sign Principle, Positive-Density No-Go, and the Critical Replacement Conveyor

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / positive-density detector recurrence round  
**Immediate predecessor:** `NS_DCRP92_X72R75_FiniteScaleConfluence_JointDetector_2026-08-19.md`

**Primary internal dependencies**
- DCRP31 — finite inward PFET
- DCRP74–75 — similarity energy / centered material pressure-work ledgers
- DCRP87 — work visibility versus weighted depletion
- DCRP88 — Kelvin finite ancestry depth
- DCRP92 — finite joint detector and positive-density recurrence

**Fresh primary-source calibration**
- R. Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322.
- R. Yu, *Finite-Window Recursive Audit Chains for Navier-Stokes Generated Packages*, arXiv:2606.20899.
- R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier-Stokes*, arXiv:2606.13887.
- R. Yu, *A Structural Audit of Navier-Stokes Obstruction Calculus*, arXiv:2606.25341.
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570.

The external recursive-audit framework explicitly does not prove scale-uniformity or summability of its one-step mismatch ledger.  
The structural audit explicitly rules out an unconditional single-scale domination of all badness by one signed combined-work scalar.

DCRP93 therefore performs a **homogeneity audit** rather than adding another positive energy/work tax.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP92 proves that, after compactness reduction, one fixed finite detector coordinate recurs at positive generation density:

\[
\boxed{
\overline{\operatorname{dens}}
\{
n:
J_{i_*}^{(n)}
\ge
c_J
\}
\ge
\delta_*
>0.
}
\tag{0.1}
\]

The immediate temptation is:

> positive density + fixed positive detector cost should force an infinite physical budget.

DCRP93 proves that this is false for every detector whose physical homogeneity exponent is positive.

Let:

\[
\ell_n
=
\ell_0 q^n,
\qquad
0<q<1,
\]

and let a normalized detector satisfy:

\[
0\le J_n\le J_*.
\]

Suppose its physical realization has homogeneity:

\[
\boxed{
\mathcal C_n^{\rm phys}
=
\ell_n^pJ_n.
}
\tag{0.2}
\]

Then:

## Theorem D93.1 — Homogeneity-Sign Principle

### Positive homogeneity

If:

\[
p>0,
\]

then for **every** subset:

\[
A\subseteq\mathbb N,
\]

including density-one sets,

\[
\boxed{
\sum_{n\in A}
\mathcal C_n^{\rm phys}
\le
J_*
\ell_0^p
\frac1{1-q^p}
<
\infty.
}
\tag{0.3}
\]

Thus positive generation density provides **zero extra raw-budget coercivity**.

### Zero homogeneity

If:

\[
p=0
\]

and:

\[
J_n\ge c>0
\]

on a positive-density set, then the unweighted event sum diverges:

\[
\boxed{
\sum_{n\in A}J_n
=
\infty.
}
\tag{0.4}
\]

But this is useful only if one has an independently finite \(p=0\) global budget.

### Negative homogeneity

If:

\[
p<0
\]

and:

\[
J_n\ge c>0
\]

along any infinite subsequence, then the individual physical amplitudes satisfy:

\[
\boxed{
\ell_n^pJ_n
\to
\infty.
}
\tag{0.5}
\]

This is the only homogeneity sign that can defeat shrinking-scale summability **without** first summing over generations.

---

# 1. Strict Type-II exponent table

Recall:

\[
1<\alpha<\frac32,
\]

\[
\gamma=\frac1{\alpha+1},
\]

and:

\[
\boxed{
\kappa=3-2\alpha\in(0,1).
}
\]

The relevant physical homogeneities are:

## energy / PFET / energy-equivalent turnover

D74 gives:

\[
\boxed{
p_E
=
\kappa
=
3-2\alpha
>
0.
}
\tag{1.1}
\]

Thus:

\[
\sum_n
\ell_n^\kappa
<
\infty.
\]

## standard coarse-work finite-chain weight

The pressure–flux work depletion theorem uses:

\[
\boxed{
w_n
=
\frac{r_n}{r_0},
}
\]

so its effective physical chain exponent is:

\[
\boxed{
p_{\rm CG}
=
1
>
0.
}
\tag{1.2}
\]

Again:

\[
\sum_nw_n<\infty.
\]

## circulation

Velocity scales as:

\[
|u|
\sim
\ell^{-\alpha}.
\]

A loop element scales as:

\[
dy\sim\ell.
\]

Hence:

\[
\boxed{
\Gamma_{\rm phys}
\sim
\ell^{1-\alpha}.
}
\tag{1.3}
\]

Therefore:

\[
\boxed{
p_\Gamma
=
1-\alpha
<
0.
}
\tag{1.4}
\]

This sign difference is decisive.

---

# 2. Why Kelvin succeeded where work summation failed

D74 had already proved:

\[
\boxed{
\text{positive PFET + positive energy-equivalent turnover at every scale}
\not\Rightarrow
\text{raw energy exhaustion}.
}
\]

The reason is now transparent:

\[
p_E=\kappa>0.
\]

D87 likewise found a finite normalized work gap but a geometrically summable physical work theorem because:

\[
p_{\rm CG}=1>0.
\]

By contrast, D88 used Kelvin circulation.

The circulation carrier has:

\[
p_\Gamma=1-\alpha<0.
\]

Moreover physical Euler circulation has a conservation/holonomy law.

Thus a scale-matched nonzero circulation atom cannot simply become cheaper at smaller scales.

Its corresponding scale amplitude becomes larger.

This yields:

\[
\boxed{
\text{negative homogeneity}
+
\text{conservation / compact capacity}
\Longrightarrow
\text{finite ancestry depth}.
}
\tag{2.1}
\]

This is the structural reason Kelvin produced a genuine ancestry obstruction while energy/work did not.

---

# 3. Sign is necessary, not sufficient

Negative homogeneity alone is not enough.

For example, a quantity may grow toward small scales but have no conserved or globally bounded capacity.

Therefore the useful template is:

\[
\boxed{
p\le0
+
\text{conservation / monotone capacity / finite total variation}.
}
\tag{3.1}
\]

For:

\[
p>0,
\]

a bounded normalized detector can never yield raw non-summability by generation counting alone.

This is the principal methodological result of D93.

---

# 4. Positive density does not rescue a positive-homogeneity tax

Let:

\[
A
=
\{
n:
J_n\ge c
\}.
\]

Suppose:

\[
\overline{\operatorname{dens}}A
\ge
\delta>0.
\]

For:

\[
p>0,
\]

we still have:

\[
\sum_{n\in A}
\ell_n^pJ_n
\le
\sum_{n=0}^{\infty}
\ell_n^pJ_*
<
\infty.
\]

Therefore:

## Theorem D93.2 — Positive-Density Budget NO-GO

\[
\boxed{
\text{positive detector density}
+
p>0
\not\Rightarrow
\text{physical budget exhaustion}.
}
\tag{4.1}
\]

In fact the result is stronger:

> even activation on **every** generation is insufficient.

---

# 5. Regeneration efficiency blow-up

Define the detector-to-physical-cost quotient:

\[
\boxed{
\mathfrak Q_{\rm reg}^{(p)}(n)
=
\frac{
J_n
}{
\ell_n^pJ_n
}
=
\ell_n^{-p}
}
\]

on an active event.

For:

\[
p>0,
\]

\[
\boxed{
\mathfrak Q_{\rm reg}^{(p)}(n)
\to\infty.
}
\tag{5.1}
\]

Thus the same normalized event becomes arbitrarily cheap in physical units as the cascade descends.

This is not a paradox.

It is exactly what self-similar renormalization permits.

---

# 6. Exact similarity-dilation conveyor

D74 gives, for a similarity-material domain \(D(s)\),

\[
\boxed{
K_D'
=
\gamma\kappa K_D
-
\Pi_P.
}
\tag{6.1}
\]

Suppose the same normalized material packet returns after one DSS period:

\[
\boxed{
K_D(S_0)
=
K_D(0).
}
\tag{6.2}
\]

Integrating (6.1):

## Theorem D93.3 — Periodic Similarity-Dilation Balance

\[
\boxed{
\int_0^{S_0}
\Pi_P(s)ds
=
\gamma\kappa
\int_0^{S_0}
K_D(s)ds.
}
\tag{6.3}
\]

For a nonzero packet, the right side is positive.

Therefore a positive normalized pressure-work payment is **compatible with exact normalized recurrence**.

It is not automatically depletion.

The similarity dilation source replenishes it.

---

# 7. Centered conveyor

D75 removes bulk translation and affine pressure.

The centered material energy satisfies:

\[
\boxed{
(K^\circ)'
=
\gamma\kappa K^\circ
-
\Pi_P^\circ.
}
\tag{7.1}
\]

If:

\[
K^\circ(S_0)=K^\circ(0)>0,
\]

then:

## Theorem D93.4 — Centered Similarity-Dilation Conveyor

\[
\boxed{
\int_0^{S_0}
\Pi_P^\circ ds
=
\gamma\kappa
\int_0^{S_0}
K^\circ ds
>
0.
}
\tag{7.2}
\]

So the conveyor cannot be dismissed as a bulk-translation artifact.

It can require genuine centered / non-affine pressure work.

D93 does **not** identify this pressure-work functional with D87's combined coarse work or with D26's SGS forward work.

Its role is structural:

> the similarity equations themselves admit exact periodic positive-work balance at positive physical homogeneity.

This is a rigorous NO-GO against a naive “positive normalized work every generation implies exhaustion” argument.

---

# 8. Detector-by-detector audit

D92 leaves one fixed recurrent detector coordinate.

We now classify each possibility.

## A. endpoint-return mismatch

If:

\[
J_{\rm ret}
\ge
c_{\rm ret}>0
\]

on positive generation density, then the normalized package does not approach exact same-parent return along those events.

Therefore:

\[
\boxed{
J_{\rm ret}^{+\rm dens}
\Longrightarrow
R_{\rm state}.
}
\tag{8.1}
\]

This is not a compact equality conveyor.

---

## B. localization / pressure residual

If:

\[
J_{\rm loc/press}
\ge
c_{\rm loc}>0
\]

on positive density, the branch is financed by a persistent explicit residual ledger.

The finite-window recursive-audit literature treats exactly such localization, harmonic-tail, projection, synchronization, detector, and chart mismatches as named ledger entries.

It does not prove their infinite-scale summability automatically.

Thus define:

\[
\boxed{
\mathsf C_{\rm res}
=
\text{positive-density residual-financed conveyor}.
}
\tag{8.2}
\]

This is explicit, not invisible.

---

## C. subfilter residual

If:

\[
\Omega^\ell
\ge
c_{\rm sub}>0
\]

on positive density, the survivor continually stores normalized badness below the chosen coarse scale.

On the strong compact velocity-increment branch this re-enters D24–26.

A pressure-dominant remainder is already a pressure/subfilter residual.

Thus:

\[
\boxed{
\mathsf C_{\rm sub}
}
\]

is an unresolved-reservoir conveyor, not a new equality kernel.

---

## D. SGS forward work

If one D26 forward SGS coordinate recurs:

\[
W^{\rm SGS}_{+}
\ge
c_S
\]

at positive density, the normalized recurrence is visibly paying forward interscale work.

But its physical payment has positive homogeneity.

Therefore raw summation remains finite.

Define:

\[
\boxed{
\mathsf C_{\rm SGS+}
=
\text{positive-homogeneity SGS-forward conveyor}.
}
\tag{8.3}
\]

---

## E. combined forward pressure-flux work

Similarly, if:

\[
G_+
\ge
c_G
\]

at positive density, the exact coarse depletion theorem sees forward work, but its physical chain weight is geometric.

Define:

\[
\boxed{
\mathsf C_{G+}
=
\text{combined-forward critical conveyor}.
}
\tag{8.4}
\]

The D93 similarity-dilation ledger demonstrates why positive normalized work can be compatible with recurrent normalized state.

---

## F. combined backscatter

If:

\[
G_-
\ge
c_G
\]

at positive density, the resolved scale is repeatedly financed by negative combined work / backscatter.

This is not a depletion channel.

It requires recurrent energy or pressure supply from another sector.

Define:

\[
\boxed{
\mathsf C_{G-}
=
\text{backscatter-funded regeneration conveyor}.
}
\tag{8.5}
\]

A nonzero SGS backscatter component requires active subgrid stress; a pressure-dominant negative combined work requires active pressure transport.

Either way, the financing source is explicit.

---

# 9. Positive-density normal form

Combine D92 with the detector audit.

## Theorem D93.5 — Positive-Density Regeneration Normal Form

On the compact bounded-reservoir late branch, a positive-density recurrent finite detector implies at least one of:

\[
\boxed{
R_{\rm state}
\vee
R_{\rm crit}
\vee
\mathsf C_{\rm res}
\vee
\mathsf C_{\rm sub}
\vee
\mathsf C_{\rm SGS+}
\vee
\mathsf C_{G+}
\vee
\mathsf C_{G-}.
}
\tag{9.1}
\]

The first two are explicit noncompactness.

The next two are explicit residual financing.

The last three are the genuine signed-work critical conveyors.

No generic invisible detector branch remains.

---

# 10. Compress the signed-work conveyors

At the physical-budget level, the three work conveyors share one decisive property:

\[
\boxed{
p_{\rm work}>0.
}
\]

Therefore they can be compressed into:

\[
\boxed{
\mathsf C_{\rm work}^{+h}
}
\]

= **positive-homogeneity work conveyor**.

Its defining properties are:

1. one fixed normalized work coordinate has:
   \[
   J_n\ge c>0
   \]
   on positive generation density;

2. normalized reservoirs stay bounded;

3. the physical cost is:
   \[
   \mathcal C_n^{\rm phys}
   \sim
   \ell_n^pJ_n,
   \qquad
   p>0;
   \]

4. hence:
   \[
   \sum_n
   \mathcal C_n^{\rm phys}
   <
   \infty;
   \]

5. same-parent regeneration continually resets the normalized state.

This is the precise **critical replacement conveyor** left by D93.

---

# 11. Why this is not a constructed singular solution

The normal form is an accounting/dynamical compatibility class.

D93 does not construct a Navier–Stokes singularity satisfying it.

It proves only:

> existing positive-homogeneity depletion ledgers cannot exclude such a survivor by summation alone.

Additional cross-coordinate rigidity is required.

---

# 12. Recursive-audit calibration

The 2026 finite-window recursive-audit framework proves that one-step detector certificates propagate through finite renormalized chains after every mismatch is charged.

It also explicitly states that its insertion theorem does **not** prove scale-uniformity or summability of the residual ledger.

This matches D93 exactly.

D92 supplied the finite detector family.

D93 shows why recursive finite detection still needs a nonpositive-homogeneity or otherwise non-summable regeneration witness for a true infinite-chain contradiction.

---

# 13. The homogeneity target for the endgame

The new design rule is:

## Do not add another \(p>0\) budget.

A useful next-generation ledger must satisfy at least one of:

### A. nonpositive physical homogeneity

\[
\boxed{
p\le0;
}
\]

### B. a scale-normalized total variation with a globally finite capacity;

### C. a conserved/topological quantity whose scale-matched amplitude cannot be regenerated freely;

### D. a monotone ancestry count that cannot be reset by changing carriers.

Kelvin circulation succeeds because it has:

\[
p_\Gamma<0
\]

and a conservation/holonomy law.

---

# 14. Secondary candidate: helicity sign audit

For a Type-II scale:

\[
u\sim\ell^{-\alpha},
\qquad
\omega\sim\ell^{-\alpha-1},
\qquad
dx\sim\ell^3.
\]

A scale-local helicity quantity has homogeneity:

\[
\boxed{
p_H
=
2-2\alpha
<
0.
}
\tag{14.1}
\]

This makes helicity structurally interesting.

However D93 does **not** use it because:

- the strict DSS survivor need not have finite global helicity;
- helicity is signed and can cancel;
- Navier–Stokes viscosity introduces helicity dissipation/production terms.

It is only a candidate for later audit, not a proved closure route.

---

# 15. Why enstrophy is not automatically enough

Raw enstrophy-type quantities can also have negative homogeneity.

But 3D enstrophy is not conserved and can grow strongly.

Thus:

\[
p<0
\]

without a finite capacity does not close the proof.

Again the correct template is:

\[
\boxed{
\text{nonpositive homogeneity}
+
\text{conservation / compact capacity}.
}
\]

---

# 16. Updated late architecture

The late same-parent branch is now:

\[
\boxed{
\mathcal O_{\rm PFET}
}
\]

simultaneously with:

\[
\boxed{
R_{\rm state}
\vee
R_{\rm crit}
\vee
\mathsf C_{\rm res}
\vee
\mathsf C_{\rm sub}
\vee
\mathsf C_{\rm work}^{+h}.
}
\tag{16.1}
\]

Remote Eulerian FAR remains separately in its D20–21 annular-amplification architecture.

The only equality-like compact survivor in the present material/work branch is:

\[
\boxed{
\mathsf C_{\rm work}^{+h}.
}
\]

It is no longer vague.

It is a positive-homogeneity, finite-detector, recurrent replacement conveyor.

---

# 17. Status ledger

## PROVED this round

### D93-P1 — homogeneity-sign trichotomy for geometrically shrinking generations.

### D93-P2 — every bounded normalized \(p>0\) detector has finite physical sum on **every subset** of generations.

### D93-P3 — positive generation density adds no raw-budget coercivity for \(p>0\).

### D93-P4 — Type-II energy/PFET exponent:

\[
p_E=\kappa>0.
\]

### D93-P5 — standard coarse-work chain exponent:

\[
p_{\rm CG}=1>0.
\]

### D93-P6 — circulation exponent:

\[
p_\Gamma=1-\alpha<0.
\]

### D93-P7 — homogeneity sign explains the Kelvin-versus-work difference.

### D93-P8 — exact periodic similarity-dilation work balance from D74.

### D93-P9 — exact centered similarity-dilation work balance from D75.

### D93-P10 — positive-density endpoint mismatch is state noncompactness.

### D93-P11 — residual/subfilter recurrence becomes explicit residual financing.

### D93-P12 — fixed-sign work recurrence reduces to explicit positive-homogeneity forward/backscatter conveyors.

### D93-P13 — the late compact work survivor is compressed to one critical replacement-conveyor normal form.

---

# 18. What is not proved

D93 does not prove:

- \(\mathsf C_{\rm work}^{+h}\) is impossible;
- forward work dominates backscatter;
- residual conveyors have a finite global total variation;
- helicity is finite or useful on the strict DSS branch;
- one fixed detector event necessarily carries a new \(p\le0\) invariant;
- global Navier–Stokes regularity.

The next target must **change homogeneity class**, not merely add another positive energy tax.

---

# 19. New STOP

\[
\boxed{
\textbf{
STOP-D93:
Positive detector density cannot solve the remaining depletion problem whenever the physical detector has positive homogeneity. For }\ell_n=\ell_0q^n\textbf{ and any bounded normalized detector with physical cost }\ell_n^pJ_n\textbf{, }p>0\textbf{ implies a finite total cost even if the detector fires on every generation. This explains both D74's Type-II energy/PFET summability, where }p=\kappa=3-2\alpha>0\textbf{, and D87's coarse-work summability, whose finite-chain weight has }p=1\textbf{. Kelvin circulation is different: }\Gamma_{\rm phys}\sim\ell^{1-\alpha}\textbf{ has }p_\Gamma=1-\alpha<0\textbf{ and is constrained by conservation/holonomy, which is why D88 obtained finite ancestry depth. The exact D74/D75 material-energy ledgers further prove that positive normalized pressure work can coexist with exact periodic normalized recurrence by balancing the similarity-dilation source, so a recurrent positive work detector is not itself a contradiction. After auditing the finite D92 coordinates, endpoint mismatch is state escape, localization/pressure and subfilter activity are explicit residual-financed conveyors, and the genuinely compact signed survivor is a positive-homogeneity forward/backscatter replacement conveyor. The next closure attempt must therefore use a nonpositive-homogeneity conserved/finite-capacity regeneration witness, not another energy/work sum.}
}
\]

---

# 20. Next autonomous step

## DCRP94 / X72-R77 — Nonpositive-Homogeneity Regeneration Witness

**Working title**

> **Can Every Positive-Homogeneity Replacement Event Be Coupled to a Nonpositive-Homogeneity Conserved/Finite-Capacity Reset Witness?**

Primary tasks:

1. start from:
   \[
   \mathsf C_{\rm work}^{+h};
   \]
2. retain the D88 circulation atom:
   \[
   |\Gamma|\ge c_\Gamma;
   \]
3. quantify the circulation reset required after one Kelvin contraction:
   \[
   \Delta_\Gamma
   \sim
   (1-\rho_\Gamma)c_\Gamma;
   \]
4. ask whether one fixed D92 detector event must carry that reset through a scale-uniform efficiency inequality;
5. if the reset is supplied through SGS circulation, reuse D81–85;
6. if supplied through state replacement, count carrier replacement and test compact capacity;
7. audit scale-local helicity only as a secondary \(p_H<0\) candidate;
8. seek:
   \[
   \mathsf C_{\rm work}^{+h}
   \Longrightarrow
   \text{nonpositive-homogeneity reset debt}
   \vee
   R_{\rm state}
   \vee
   R_{\rm crit}.
   \]

Desired endpoint:

\[
\boxed{
\text{critical replacement conveyor}
\Longrightarrow
\text{one conserved/finite-capacity non-summable witness}
\vee
\text{explicit replacement noncompactness}.
}
\]

---

# 21. One-line checkpoint

The remaining endgame is now governed by homogeneity sign: every known energy/work tax has positive physical homogeneity and is summable regardless of recurrence density, while Kelvin succeeded precisely because circulation has negative homogeneity plus conservation; the next proof step must couple each replacement event to another witness of that non-summable type.

---

**End checkpoint:** DCRP93 / X72-R76  
**Next:** DCRP94 / X72-R77 — Nonpositive-Homogeneity Regeneration Witness.
