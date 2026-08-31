---
title: "Navier–Stokes Dynamic Reservoir Closure Program 04：Cancellation Rigidity、Many-Parent Aggregation、Net-Shell Coherence 與 Dissipation-Span Compression"
short_title: "NS-DRC 04"
series: "Navier–Stokes Dynamic Reservoir Closure Program"
cycle: "III"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style cancellation bypass / many-parent compression"
epistemic_status: "Shows that signed cancellation need not be bounded in order to extract a high-parent state carrier: after grouping an exact renewal ledger by canonical high-parent shell, finite shell support alone forces a positive net shell contribution. Completes the dissipation-wavenumber forcing split by proving scale-local high-high interactions far above the dissipation boundary are viscosity-small. Hence every non-absorbable non-driver transition parent lies in a finite dyadic interval whose width is controlled by the dissipation-boundary span above the output threshold. Parent multiplicity therefore implies dissipation-span escape. Combining these facts removes R_CAN and R_MULT as independent residual classes, conditional on the established DRC-03 driver/absorption decomposition. Signed cancellation remains real phase/coherence geometry but no longer blocks net-shell genealogy. Navier–Stokes regularity is NOT proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Dynamic Reservoir Closure Program 04

# Cancellation Rigidity、Many-Parent Aggregation、Net-Shell Coherence 與 Dissipation-Span Compression

## 0. 本文定位

DRC-03 reduced the dangerous source residual to:

$$
\boxed{
R_{\rm CAN},
\qquad
R_{\rm MULT},
}
$$

plus the already separated:

$$
R_{\rm DISS},
\qquad
R_{\rm DIL},
\qquad
R_{\rm ALIGN}^{src}.
$$

The present paper changes the strategy.

We do **not** try to prove:

$$
\mathfrak C^{can}
$$

is uniformly bounded.

Signed cancellation is a genuine feature of nonlinear transfer.

Instead we ask:

> Can arbitrarily large cancellation actually prevent a finite parent carrier once the number of possible high-parent shells is finite?

The answer is:

$$
\boxed{
\textbf{No.}
}
$$

The correct object is the **net shell contribution**, not positive gross alone.

The remaining question is therefore whether the set of dynamically non-absorbable parent shells can itself become arbitrarily large.

This is controlled by the dissipation-wavenumber span.

---

# 1. Renewal interval

Fix one high-frequency vorticity renewal slab:

$$
I=[a,b].
$$

Let:

$$
J
$$

be the replenished output threshold.

Let:

$$
Q(s)
$$

be the Cheskidov--Shvydkoy dissipation-wavenumber index.

Define:

$$
\boxed{
Q_I^+
=
\sup_{s\in I}
Q(s).
}
$$

For integer bookkeeping take the ceiling when needed.

---

# 2. Parent geometry

For dyadic vorticity parents:

$$
\omega_p,
\qquad
\omega_q,
$$

define:

$$
h=\max\{p,q\},
\qquad
\ell=\min\{p,q\}.
$$

High output:

$$
k\ge J
$$

implies:

$$
\boxed{
h\ge J-C_{\rm LP}.
}
$$

Fix a relative-gap threshold:

$$
L\ge1.
$$

---

# 3. Three parent sectors

At time:

$$
s,
$$

classify a high-output vorticity interaction into:

### DRIVER

$$
\boxed{
\ell\le Q(s).
}
$$

At least one parent lies in the low-mode driver sector.

### TRANSITION-LOCAL

$$
\boxed{
h-L\le\ell\le h,
\qquad
h\le Q(s)+L+C_{\rm LP}.
}
$$

The parent cluster is scale-local and lies within a fixed band of the dissipation boundary.

### DEEP-DISSIPATIVE

All parent shells lie above:

$$
Q(s)
$$

and the high parent is separated from the boundary by more than a fixed number of shells.

This includes both:

- scale-local high-high;
- far high-low with low parent still above:
  $$
  Q(s).
  $$

DRC-03 handled the far high-low part.

This paper completes the scale-local high-high part.

---

# 4. Dissipation-range pointwise shell bound

For:

$$
r>Q(s),
$$

the dissipation-wavenumber definition gives:

$$
\boxed{
2^{-r}
\|u_r(s)\|_\infty
<
c_0.
}
$$

Therefore:

$$
\boxed{
\|\omega_r(s)\|_\infty
\le
C
c_0
2^{2r}.
}
$$

---

# 5. Scale-local high-high cluster

Fix:

$$
h>Q(s)+L+C_{\rm LP}.
$$

For:

$$
p,q\in[h-L,h],
$$

both parents satisfy:

$$
p,q>Q(s).
$$

Fourier support gives:

$$
k=h+O_L(1)
$$

for any high-output contribution.

---

# 6. CIII-4.1 — Deep Local-Cluster Viscous Absorption

## Theorem 6.1

For every fixed:

$$
L<\infty,
$$

the aggregate scale-local high-high forcing with:

$$
p,q\in[h-L,h],
\qquad
h>Q(s)+L+C_{\rm LP},
$$

satisfies:

$$
\boxed{
\left\|
P_{h+O_L(1)}
P_{st}
\left(
\omega_{[h-L,h]}
\otimes
\omega_{[h-L,h]}
\right)
\right\|_{\dot H^1}
\le
C_L
c_0
2^{2h}
\sum_{r=h-L}^{h}
\|S_r(s)\|_{\dot H^1}.
}
$$

### Proof

For one ordered pair:

$$
(p,q),
$$

use:

$$
\|P_k(\omega_p\otimes\omega_q)\|_2
\le
\|\omega_q\|_\infty
\|\omega_p\|_2.
$$

Since:

$$
q>Q(s),
$$

Section 4 gives:

$$
\|\omega_q\|_\infty
\le
Cc_02^{2q}
\lesssim_L
c_02^{2h}.
$$

The output:

$$
\dot H^1
$$

factor is:

$$
2^k
\asymp_L
2^h.
$$

Also:

$$
\|S_p\|_{\dot H^1}
\asymp
2^p
\|\omega_p\|_2
\asymp_L
2^h
\|\omega_p\|_2.
$$

Thus:

$$
\|P_kP_{st}(\omega_p\otimes\omega_q)\|_{\dot H^1}
\le
C_L
c_0
2^{2h}
\|S_p\|_{\dot H^1}.
$$

Sum over the finite parent/output cluster. $\square$

---

# 7. Meaning of Theorem 6.1

The natural viscous rate of a shell-Hdot1 state at scale:

$$
h
$$

is:

$$
\boxed{
2^{2h}
\|S_h\|_{\dot H^1}.
}
$$

Hence scale-local interactions lying sufficiently far above:

$$
Q(s)
$$

are a small:

$$
O_L(c_0)
$$

fraction of the viscous rate.

Together with DRC-03's far high-low estimate, all interactions whose parent cluster lies completely in the deep dissipation range are viscosity-small.

---

# 8. Non-absorbable parent localization

After removing:

- DRIVER contributions;
- the viscosity-small deep-dissipative remainder;

every remaining high-parent shell:

$$
h
$$

must satisfy for some:

$$
s\in I:
$$

$$
\boxed{
J-C_{\rm LP}
\le
h
\le
Q(s)+L+C_{\rm LP}.
}
$$

Therefore:

$$
\boxed{
J-C_{\rm LP}
\le
h
\le
Q_I^+
+
L+C_{\rm LP}.
}
$$

---

# 9. Dissipation-span width

Define:

$$
\boxed{
\mathfrak W_Q(I,J)
=
1+
\left[
Q_I^+
-
J
\right]_+.
}
$$

The number of transition high-parent shell labels is bounded by:

$$
\boxed{
K_{I,J}^{tr}
\le
C_L
\mathfrak W_Q(I,J).
}
$$

Here:

$$
C_L
$$

absorbs the fixed LP and transition padding.

---

# 10. CIII-4.2 — Parent-Multiplicity / Dissipation-Span Theorem

## Theorem 10.1

For the non-driver, non-absorbable transition portion of a high-frequency renewal packet, the effective high-parent source multiplicity satisfies:

$$
\boxed{
\mathfrak M_J^{par,tr}
\le
K_{I,J}^{tr}
\le
C_L
\mathfrak W_Q(I,J).
}
$$

### Proof

A probability distribution supported on at most:

$$
K
$$

shell labels has effective multiplicity:

$$
\left(
\sum_hr_h^2
\right)^{-1}
\le
K.
$$

Use Section 9. $\square$

---

# 11. Consequence for R-MULT

If:

$$
\boxed{
\mathfrak M_J^{par,tr}\to\infty,
}
$$

then necessarily:

$$
\boxed{
\mathfrak W_Q(I,J)\to\infty.
}
$$

Thus many-parent transition aggregation requires the dissipation boundary to extend arbitrarily many dyadic scales above the replenished output threshold.

This is a dissipation-range placement/sweep mechanism.

Therefore:

$$
\boxed{
R_{\rm MULT}
}
$$

is absorbed into:

$$
\boxed{
R_{\rm DISS}
}
$$

after DRIVER and absorbable sectors are preserved explicitly.

---

# 12. Transition renewal vector

Let:

$$
Y_J^{tr}
$$

be the Duhamel renewal vector obtained after removing:

- the low-mode DRIVER sector;
- the viscosity-absorbable deep-dissipation sector.

Assume we are outside:

$$
R_{\rm DISS}
$$

in the quantitative sense that these removed sectors contribute at most:

$$
\varepsilon
R_J^\omega
$$

in:

$$
\dot H^1
$$

norm, with:

$$
\varepsilon<1/4.
$$

Then:

$$
\boxed{
R_J^{tr}
=
\|Y_J^{tr}\|_{\dot H^1}
\ge
(1-2\varepsilon)
R_J^\omega.
}
$$

---

# 13. Transition norming witness

Choose:

$$
\Psi_J^{tr}
\in
\dot H^{-1}
$$

such that:

$$
\|\Psi_J^{tr}\|_{\dot H^{-1}}=1,
$$

and:

$$
\boxed{
\langle
Y_J^{tr},
\Psi_J^{tr}
\rangle
=
R_J^{tr}.
}
$$

Group the exact signed transition ledger by canonical high-parent shell:

$$
h.
$$

Define:

$$
\boxed{
n_{J,h}
=
\sum_{
k,p,q:
h(p,q)=h
}
\Lambda_{k;p,q}^{tr}.
}
$$

Then:

$$
\boxed{
\sum_h
n_{J,h}
=
R_J^{tr}.
}
$$

---

# 14. CIII-4.3 — Cancellation-Robust Net-Shell Carrier

## Theorem 14.1

Suppose the transition ledger is supported on at most:

$$
K
$$

high-parent shell labels.

Then, regardless of the positive/negative gross cancellation ratio, there exists:

$$
h_\star
$$

such that:

$$
\boxed{
n_{J,h_\star}
\ge
\frac{
R_J^{tr}
}{
K
}.
}
$$

### Proof

Let:

$$
H_+
=
\{
h:
n_{J,h}>0
\}.
$$

Since:

$$
\sum_hn_{J,h}=R_J^{tr}>0,
$$

$$
\sum_{h\in H_+}
n_{J,h}
\ge
R_J^{tr}.
$$

There are at most:

$$
K
$$

positive shell labels.

Hence one satisfies the stated lower bound. $\square$

---

# 15. Why cancellation no longer blocks ancestry

Theorem 14.1 does not require:

$$
\mathfrak C_J^{can}
$$

to be bounded.

One may have:

$$
\mathfrak C_J^{can}\gg1,
$$

with enormous positive and negative triadic gross.

As long as the possible high-parent shell support is finite, the exact **net** renewal vector still has a positive net high-parent shell carrier.

Thus:

$$
\boxed{
\text{signed cancellation}
}
$$

does not by itself prevent one-step shell ancestry.

---

# 16. Transition state backing

For the shell:

$$
h_\star
$$

of Theorem 14.1, the signed net contribution obeys:

$$
\boxed{
|n_{J,h_\star}|
\le
Q_{J,h_\star}^{tr}.
}
$$

For the scale-local transition piece, DRC-03 gives:

$$
\boxed{
Q_{J,h_\star}^{tr}
\le
C_L
Z_{J,h_\star}^{(L)},
}
$$

where:

$$
Z_{J,h}^{(L)}
=
2^{5h/2}
\sum_{r=h-L}^{h}
E_{J,r}.
$$

Therefore:

$$
\boxed{
Z_{J,h_\star}^{(L)}
\ge
c_L
\frac{
R_J^{tr}
}{
K
}.
}
$$

This is an actual scale-corrected parent-cluster state lower bound.

---

# 17. CIII-4.4 — Cancellation-Robust State-Cluster Carrier

## Theorem 17.1

Outside the DRIVER / deep-dissipation residual sectors, if:

$$
\mathfrak W_Q(I,J)\le W_0,
$$

then there exists a transition high-parent cluster:

$$
[h_\star-L,h_\star]
$$

such that:

$$
\boxed{
Z_{J,h_\star}^{(L)}
\ge
c_{L,W_0}
R_J^\omega.
}
$$

This conclusion is independent of:

$$
\mathfrak C_J^{can}.
$$

### Proof

Theorem 10.1 gives:

$$
K
\le
C_LW_0.
$$

Theorem 14.1 gives:

$$
n_{J,h_\star}
\ge
c_{L,W_0}
R_J^\omega.
$$

Apply Section 16. $\square$

---

# 18. Main cancellation conclusion

Large cancellation may still occur inside the selected cluster.

But it no longer prevents:

$$
\boxed{
\text{net source carrier}
\longrightarrow
\text{state-backed finite parent cluster}.
}
$$

Therefore:

$$
\boxed{
R_{\rm CAN}
}
$$

is removed as an independent ancestry obstruction under bounded dissipation span.

If the shell support needed to bypass Theorem 14.1 becomes unbounded, that is already:

$$
R_{\rm MULT}
\subset
R_{\rm DISS}.
$$

---

# 19. Optional cancellation factorization

Although no cancellation bound is needed, its geometry can be recorded exactly.

For each high-parent shell define:

$$
P_h
=
\sum_{\text{shell }h}
[\Lambda]_+,
$$

$$
N_h
=
\sum_{\text{shell }h}
[-\Lambda]_+,
$$

$$
g_h
=
P_h+N_h,
$$

and:

$$
n_h
=
P_h-N_h.
$$

Let:

$$
G
=
\sum_hg_h
=
P+N,
$$

and:

$$
A
=
\sum_h|n_h|.
$$

Define:

$$
\boxed{
\mathfrak K^{intra}
=
\frac{
A
}{
G
},
}
$$

and:

$$
\boxed{
\mathfrak K^{inter}
=
\frac{
R
}{
A
}.
}
$$

Then:

$$
\boxed{
\frac{
R
}{
G
}
=
\mathfrak K^{intra}
\mathfrak K^{inter}.
}
$$

Since:

$$
G
=
(2\mathfrak C^{can}-1)R,
$$

$$
\boxed{
\frac1{
2\mathfrak C^{can}-1
}
=
\mathfrak K^{intra}
\mathfrak K^{inter}.
}
$$

---

# 20. Meaning of cancellation factorization

Large cancellation can arise from:

### INTRA

positive and negative contributions cancel strongly **inside the same high-parent shell group**;

### INTER

shell-net contributions of opposite sign cancel **between high-parent shell groups**.

This is a coherence/phase classification.

It is not needed for the net-carrier theorem.

---

# 21. Static coherence lower-bound no-go

There is no universal lower bound on:

$$
\mathfrak K^{intra}
$$

or:

$$
\mathfrak K^{inter}
$$

from parent global norms and shell indices alone.

A finite-dimensional band-limited test construction can hold parent amplitudes fixed while varying Fourier phases in time so that a selected signed triadic coefficient oscillates and has arbitrarily small time integral.

This is a functional-analytic phase-coherence no-go, not a Navier--Stokes solution construction.

Thus the program should not attempt to prove cancellation is universally small using static state sizes alone.

---

# 22. External structural calibration

Exact Navier--Stokes triadic decompositions and scale-locality analyses support two points used here:

1. signed transfer contains genuine cancellations;
2. aggregate many-triad transfer must not be replaced by one informal dominant triad without a quantitative carrier theorem.

Tao's averaged Navier--Stokes blow-up construction additionally shows that energy cancellation plus generic harmonic-analysis structure is too coarse to resolve true 3D Navier--Stokes regularity.

Hence the present strategy is deliberately finer:

$$
\boxed{
\text{group exact realized renewal by parent shell and keep the true net vector}.
}
$$

---

# 23. Parent multiplicity as boundary sweep

Theorem 10.1 also gives a new interpretation.

A large number of dynamically relevant parent shells during one renewal slab requires:

$$
\boxed{
Q_I^+-J
}
$$

to be large.

Thus the issue is no longer:

> infinitely many unrelated parents.

It is:

> the dissipation boundary or driver geometry spans many dyadic levels relative to the replenished output.

Define:

$$
\boxed{
R_{\rm QSPAN}
:
\mathfrak W_Q(I,J)\to\infty.
}
$$

Then:

$$
\boxed{
R_{\rm MULT}
\subset
R_{\rm QSPAN}
\subset
R_{\rm DISS}.
}
$$

---

# 24. Conditional finite branching without cancellation control

Suppose along a renewal genealogy:

1. DRIVER/deep-dissipation residual fractions are bounded away from one;
2. dissipation span:
   $$
   \mathfrak W_Q(I,J)\le W_0;
   $$
3. each selected transition cluster is promoted to the next backward state node.

Then every renewal node has at most:

$$
\boxed{
C_LW_0
}
$$

candidate high-parent shell clusters.

No cancellation-ratio bound is required.

Therefore arbitrarily deep finite transition renewal chains yield an infinite state-backed renewal genealogy by standard finite-branching path extraction.

---

# 25. CIII-4.5 — Cancellation-Free Finite-Branching Criterion

## Theorem 25.1

Under the three assumptions of Section 24, renewal genealogy is uniformly finitely branching.

In particular:

$$
\boxed{
\sup
\mathfrak C_J^{can}
=
\infty
}
$$

does not destroy finite branching.

### Safety

This is still a conditional genealogy theorem.

It does not prove arbitrarily deep finite renewal chains exist for a hypothetical singularity.

$\square$

---

# 26. Updated source residual

Before DRC-04 the source-specific dangerous residuals were:

$$
R_{\rm CAN},
\qquad
R_{\rm MULT}.
$$

After DRC-04:

$$
\boxed{
R_{\rm CAN}
}
$$

is removed as an independent ancestry obstruction.

And:

$$
\boxed{
R_{\rm MULT}
}
$$

is absorbed into:

$$
R_{\rm DISS}.
$$

The remaining localized alignment failures from DRC-03 are certificate/depletion geometry unless a later spatial-core theorem promotes them to dynamical obstructions.

---

# 27. Updated Cycle-III residual core

The principal dynamic residual core becomes:

$$
\boxed{
\mathfrak R_{\rm III}^{(4)}
=
R_{\rm DISS}
\cup
R_{\rm DIL}.
}
$$

At the certificate/representation layer one still records:

$$
\boxed{
R_{\rm ALIGN}^{src}.
}
$$

But it is not currently a monotone dangerous mechanism.

This is the first point in the RFP/CSP/DRC program where the **principal dynamic residual core has only two classes**.

---

# 28. What R-DISS now contains

The dissipation residual is no longer one vague high-frequency label.

It contains:

1. low-mode driver dominance;
2. transition-band forcing near:
   $$
   Q(s);
   $$
3. large dissipation-span:
   $$
   Q_I^+-J;
   $$
4. recurrent high-shell replenishment required by the Cycle-II low/high activity sandwich.

These are all forcing-level scale-placement mechanisms.

---

# 29. What R-DIL contains

The dilution residual contains:

1. Type-I singular-core shell with fixed absolute local mass;
2. vanishing global shell share;
3. compatibility with the weighted energy budget:
   $$
   \int
   \frac{dt}{
   \beta_cR_I
   }
   <
   \infty.
   $$

It is a local/global reservoir-distribution mechanism.

---

# 30. Next paper

The next paper should now attack:

$$
\boxed{
R_{\rm DISS}.
}
$$

Therefore:

$$
\boxed{
\textbf{
NS-DRC 05 —
Dissipation-Range Reservoir Closure、
Low-Mode Driver Coupling、
Boundary Sweep
與 Forcing-Level Viscous Coercivity
}.
}
$$

Primary tasks:

1. convert transition-band source debt into a dissipation-wavenumber action;
2. couple:
   $$
   Q_I^+-J
   $$
   boundary sweep to:
   $$
   \Lambda(t)
   $$
   intermittency;
3. combine low-mode driver divergence with high-shell replenishment;
4. derive a forcing-level viscous coercivity inequality;
5. determine whether:
   $$
   R_{\rm DISS}
   $$
   can be closed or reduced to one explicit driver/residence mechanism.

After that only:

$$
R_{\rm DIL}
$$

remains as the principal spatial/core residual.

---

# 31. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{deep local-cluster viscous absorption}
&:\ \mathrm{PROVED},\\
\text{transition parent support bound}
&:\ \mathrm{PROVED},\\
\text{parent multiplicity/dissipation-span theorem}
&:\ \mathrm{PROVED},\\
R_{\rm MULT}\text{ as independent residual}
&:\ \mathrm{ABSORBED\ INTO}\ R_{\rm DISS},\\
\text{cancellation-robust net-shell carrier}
&:\ \mathrm{PROVED},\\
\text{cancellation-robust state-cluster carrier}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
\text{intra/inter cancellation factorization}
&:\ \mathrm{PROVED},\\
\text{static coherence lower-bound route}
&:\ \mathrm{NO\mbox{-}GO},\\
R_{\rm CAN}\text{ as independent ancestry obstruction}
&:\ \mathrm{REMOVED},\\
\text{cancellation-free finite branching}
&:\ \mathrm{PROVED\ CONDITIONALLY},\\
R_{\rm DISS}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm DIL}\text{ closure}
&:\ \mathrm{OPEN},\\
\text{Full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 32. Conclusion

DRC-04 changes the treatment of cancellation.

Large positive/negative source gross does not need to be bounded.

Once the exact transition renewal is grouped by finitely many possible high-parent shells:

$$
\sum_hn_h
=
R>0,
$$

one shell necessarily carries:

$$
\boxed{
n_{h_\star}
\ge
R/K.
}
$$

This survives arbitrary internal signed cancellation.

The only way to lose a finite parent-shell carrier is therefore to let the number of dynamically relevant parent shells diverge.

But dissipation-wavenumber geometry gives:

$$
\boxed{
K
\lesssim_L
1+
[Q_I^+-J]_+.
}
$$

Thus many-parent aggregation is itself a dissipation-boundary-span mechanism.

Consequently:

$$
\boxed{
R_{\rm CAN}
\text{ is removed},
}
$$

and:

$$
\boxed{
R_{\rm MULT}
\subset
R_{\rm DISS}.
}
$$

The principal dynamic residual core is reduced to:

$$
\boxed{
R_{\rm DISS}
\cup
R_{\rm DIL}.
}
$$

The next task is forcing-level dissipation closure.

---

# References

1. T. Tao, *Finite time blowup for an averaged three-dimensional Navier--Stokes equation*, Journal of the American Mathematical Society 29 (2016), 601--674; arXiv:1402.0290.
2. G. L. Eyink, H. Aluie, *Localness of energy cascade in hydrodynamic turbulence, I. Smooth coarse-graining*, Phys. Fluids 21 (2009); arXiv:0909.2386. Used as signed-cancellation/scale-locality calibration under its stated inertial-range assumptions.
3. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, Phys. Fluids 21 (2009); arXiv:0909.2451. Used as aggregate-triad calibration.
4. R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560 (2026). Used as contemporary geometric-depletion calibration.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
6. `NS_DRC_02_SourceToState_Efficiency_RenewalChain_v0.1.md`.
7. `NS_DRC_03_SourceAmplification_Utilization_DissipationCoupling_v0.1.md`.
8. `NS_CSP_08_UnifiedReservoirCover_CycleIIClosure_v0.1.md`.
