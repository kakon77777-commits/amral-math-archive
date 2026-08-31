---
title: "Navier–Stokes Dynamic Reservoir Closure Program 03：Source Amplification、Interaction Utilization、Spectral State Share 與 Dissipation-Range Coupling"
short_title: "NS-DRC 03"
series: "Navier–Stokes Dynamic Reservoir Closure Program"
cycle: "III"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Theorem-style amplification correction / utilization decomposition / dissipation coupling"
epistemic_status: "Refines the DRC-02 source-to-enstrophy amplification variable by separating deterministic frequency scaling from genuine source/state mismatch. Proves a scale-local cluster envelope bound with the natural 2^{5h/2} Hdot1-vorticity weight, proves a high-low dissipation-range absorption estimate relative to the Cheskidov-Shvydkoy dissipation wavenumber, and decomposes utilization exactly into temporal-sign, dual-witness, and geometric-overlap factors. A spatial-separation construction shows utilization collapse can occur purely from parent non-overlap, so utilization is reclassified as depletion/certificate inefficiency rather than a primitive dangerous mechanism. R_AMP is absorbed into scale-corrected finite-cluster state support or dissipation/driver geometry. Navier–Stokes regularity is NOT proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Dynamic Reservoir Closure Program 03

# Source Amplification、Interaction Utilization、Spectral State Share 與 Dissipation-Range Coupling

## 0. 本文定位

DRC-02 compressed the generalized source residual to:

$$
\boxed{
R_{\rm CAN},
\quad
R_{\rm UTIL},
\quad
R_{\rm MULT},
\quad
R_{\rm AMP}.
}
$$

The quantity:

$$
\mathfrak A_{J,h}^{SE}
=
\frac{s_{J,h}}{e_{J,h}}
$$

compared source-envelope share to an **unweighted** time-integrated high-parent enstrophy share.

The present paper shows that this comparison mixes two different effects:

1. genuine source/state mismatch;
2. deterministic derivative/Bernstein frequency weighting.

The correct first step is therefore to remove the latter.

---

# 1. Renewal packet notation

Fix a quadratic-vorticity renewal packet on:

$$
I=[a,b].
$$

Let:

$$
J
$$

be the high-frequency output threshold.

For parent shells:

$$
p,q,
$$

let:

$$
h=\max\{p,q\},
\qquad
\ell=\min\{p,q\}.
$$

Let:

$$
E_{J,h}
=
\int_a^b
\vartheta_J(s)
\|\omega_h(s)\|_2^2ds,
$$

where:

$$
\vartheta_J(s)
=
e^{-c_02^{2J}(b-s)}.
$$

---

# 2. Local parent cluster

Fix:

$$
L\ge1.
$$

Call a parent pair:

$$
(p,q)
$$

**L-local** if:

$$
\boxed{
h-L
\le
\ell
\le
h.
}
$$

Let:

$$
Q_{J,h}^{loc,L}
$$

denote the portion of the DRC-02 parent-state envelope:

$$
Q_{J,h}
$$

coming from:

- canonical high parent:
  $$
  h;
  $$
- L-local partner;
- all admissible outputs:
  $$
  k\ge J.
  $$

---

# 3. Output support upper bound

For a quadratic dyadic interaction:

$$
\Delta_k
P_{st}
(
\omega_p\otimes\omega_q
)
\neq0,
$$

standard Fourier support gives:

$$
\boxed{
k
\le
h+C_{\rm LP}.
}
$$

Thus on an L-local interaction:

$$
2^k
\lesssim
2^h,
$$

and:

$$
2^{\frac32\ell}
\lesssim_L
2^{\frac32h}.
$$

---

# 4. Natural local source weight

Recall the DRC-02 envelope:

$$
M_{k;p,q}
=
C
\int_a^b
e^{-c2^{2k}(b-s)}
2^k
2^{\frac32\ell}
\|\omega_h(s)\|_2
\|\omega_\ell(s)\|_2ds.
$$

For:

$$
\ell\in[h-L,h],
$$

the deterministic scale factor satisfies:

$$
\boxed{
2^k
2^{\frac32\ell}
\lesssim_L
2^{\frac52h}.
}
$$

This is the natural Hdot1 source weight for a scale-local vorticity pair.

---

# 5. Scale-corrected local state stock

Define:

$$
\boxed{
Z_{J,h}^{(L)}
=
2^{\frac52h}
\sum_{
r=h-L}^{h}
E_{J,r}.
}
$$

This is a scale-corrected time-integrated local-cluster enstrophy stock.

---

# 6. CIII-3.1 — Local Cluster Envelope Theorem

## Theorem 6.1

For every fixed:

$$
L<\infty,
$$

there exists:

$$
C_L<\infty
$$

such that:

$$
\boxed{
Q_{J,h}^{loc,L}
\le
C_L
Z_{J,h}^{(L)}.
}
$$

### Proof

For every local pair use:

$$
2^k
2^{\frac32\ell}
\lesssim_L
2^{\frac52h}.
$$

Also:

$$
e^{-c2^{2k}(b-s)}
\le
C
\vartheta_J(s)
$$

for:

$$
k\ge J.
$$

Then:

$$
\|\omega_h\|_2
\|\omega_\ell\|_2
\le
\frac12
\left(
\|\omega_h\|_2^2
+
\|\omega_\ell\|_2^2
\right).
$$

Sum over the finite local partner range and the finite output overlap.

$\square$

---

# 7. Meaning of Theorem 6.1

A scale-local source envelope cannot have arbitrarily large importance while the scale-corrected parent-cluster stock vanishes.

Thus:

$$
\boxed{
\text{large source share at one local cluster}
}
$$

already implies:

$$
\boxed{
\text{large }2^{5h/2}\text{-weighted parent-cluster state stock}.
}
$$

The unweighted ratio:

$$
s_h/e_h
$$

can therefore grow simply because:

$$
h
$$

is high.

That deterministic frequency bias must not be mislabeled as anomalous source amplification.

---

# 8. Local cluster carrier corollary

## Corollary 8.1

If an L-local high-parent envelope satisfies:

$$
\boxed{
Q_{J,h}^{loc,L}
\ge
\gamma
R_J^\omega,
}
$$

then:

$$
\boxed{
Z_{J,h}^{(L)}
\ge
c_L
\gamma
R_J^\omega.
}
$$

Hence at least one shell:

$$
r\in[h-L,h]
$$

satisfies:

$$
\boxed{
E_{J,r}
\ge
c_L
\gamma
2^{-\frac52h}
R_J^\omega.
}
$$

This is a genuine parent-state lower bound with the correct deterministic scale weight.

---

# 9. Deep high-low pairs

Now consider:

$$
\ell
\le
h-L.
$$

When the scale gap is sufficiently large, Fourier support forces:

$$
\boxed{
k
=
h+O(1).
}
$$

Thus a high-low pair contributes to a high output near the high parent scale.

---

# 10. Dissipation wavenumber

Let:

$$
Q(s)
$$

be the Cheskidov--Shvydkoy dissipation-wavenumber index.

For:

$$
r>Q(s),
$$

their definition gives:

$$
\boxed{
2^{-r}
\|u_r(s)\|_\infty
<
c_0.
}
$$

Hence by Bernstein:

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

# 11. Deep dissipation partner sum

Suppose:

$$
h
>
Q(s)+L.
$$

Then:

$$
\begin{aligned}
\sum_{
Q(s)<r\le h-L
}
\|\omega_r(s)\|_\infty
&\le
C
c_0
\sum_{
r\le h-L
}
2^{2r}
\\
&\le
C
c_0
2^{2(h-L)}.
\end{aligned}
$$

Therefore:

$$
\boxed{
\sum_{
Q(s)<r\le h-L
}
\|\omega_r(s)\|_\infty
\le
C
c_0
2^{-2L}
2^{2h}.
}
$$

---

# 12. CIII-3.2 — Far High-Low Viscous Absorption

## Theorem 12.1

Let:

$$
h>Q(s)+L+C_{\rm LP}.
$$

The Hdot1 size of the aggregate high-low vorticity forcing with:

$$
Q(s)<\ell\le h-L
$$

and high parent:

$$
h
$$

obeys:

$$
\boxed{
\|
P_{h+O(1)}
P_{st}
[
\omega_h
\otimes
\omega_{
(Q,h-L]}
]
\|_{\dot H^1}
\le
C
c_0
2^{-2L}
2^{2h}
\|
S_h
\|_{\dot H^1}.
}
$$

### Proof

For high-low output:

$$
k=h+O(1).
$$

Use:

$$
\|P_k(\omega_h\otimes\omega_r)\|_2
\le
\|\omega_r\|_\infty
\|\omega_h\|_2.
$$

The Hdot1 output contributes a factor:

$$
2^h.
$$

By Section 11:

$$
\sum_r
\|\omega_r\|_\infty
\le
Cc_02^{-2L}2^{2h}.
$$

Finally:

$$
\|S_h\|_{\dot H^1}
\asymp
2^h
\|\omega_h\|_2.
$$

$\square$

---

# 13. Interpretation

The viscous decay rate of a shell-Hdot1 state is:

$$
\boxed{
2^{2h}
\|S_h\|_{\dot H^1}.
}
$$

Therefore Theorem 12.1 says:

$$
\boxed{
\text{far high-low interactions entirely above }Q(s)
}
$$

are an:

$$
O(
c_0
2^{-2L}
)
$$

fraction of the local viscous scale.

For fixed small:

$$
c_0,
$$

the contribution is arbitrarily absorbable by choosing:

$$
L
$$

large.

---

# 14. Nonlocal partner trichotomy

A deep high-low interaction with high parent:

$$
h
$$

must lie in one of:

### DRIVER

$$
\boxed{
\ell
\le
Q(s),
}
$$

so the interaction is coupled to the low-mode driver sector;

### TRANSITION

$$
\boxed{
h
\le
Q(s)+L+O(1),
}
$$

so the high parent lies within a fixed band of the dissipation boundary;

### ABSORB

$$
\boxed{
Q(s)<\ell\le h-L,
\qquad
h>Q(s)+L+O(1),
}
$$

where Theorem 12.1 makes the aggregate interaction viscosity-absorbable.

---

# 15. CIII-3.3 — Amplification Absorption Theorem

## Theorem 15.1

Fix:

$$
L<\infty.
$$

Every high-frequency quadratic-vorticity source-envelope contribution is contained in the union of:

1. an L-local scale-corrected parent cluster:
   $$
   Z_{J,h}^{(L)};
   $$
2. the Cheskidov--Shvydkoy low-mode driver sector;
3. an:
   $$
   O(L)
   $$
   transition band around:
   $$
   Q(s);
   $$
4. a viscosity-absorbable remainder of relative size:
   $$
   O(
   c_0
   2^{-2L}
   ).
   $$

### Consequence

The DRC-02 unweighted amplification residual:

$$
R_{\rm AMP}
$$

is not a primitive source mechanism.

It is absorbed into:

$$
\boxed{
\text{scale-corrected local state support}
\vee
R_{\rm DISS}.
}
$$

Here:

$$
R_{\rm DISS}
$$

includes the low-mode driver / dissipation-boundary transition geometry already retained from Cycle II.

$\square$

---

# 16. Why this does not prove regularity

A scale-corrected local cluster carrier is a successful genealogy step, not an obstruction.

The low-mode driver sector may diverge in a hypothetical singularity.

The transition band near:

$$
Q(s)
$$

is not known to be dynamically impossible.

Thus Theorem 15.1 removes:

$$
R_{\rm AMP}
$$

as an **independent residual coordinate** but does not close:

$$
R_{\rm DISS}.
$$

---

# 17. Utilization must be decomposed further

DRC-02 defined:

$$
\boxed{
\mathfrak U_J
=
\frac{
P_J
}{
Q_J
}.
}
$$

Here:

- $P_J$ is positive realized signed source gross;
- $Q_J$ is a deterministic Hölder/Bernstein parent-state envelope.

Small:

$$
\mathfrak U_J
$$

can have several unrelated causes.

---

# 18. Absolute dual-interaction gross

Define:

$$
\boxed{
G_J
=
\sum_{k,p,q}
\int_a^b
\left|
\left\langle
e^{(b-s)\Delta}
\Delta_k
P_{st}
(
\omega_p\otimes\omega_q
),
\Psi_J
\right\rangle
\right|
ds.
}
$$

Then:

$$
\boxed{
P_J
\le
\sum_{k,p,q}
|\Lambda_{k;p,q}|
\le
G_J.
}
$$

---

# 19. Actual vector-interaction gross

Define:

$$
\boxed{
H_J
=
\sum_{k,p,q}
\int_a^b
\left\|
e^{(b-s)\Delta}
\Delta_k
P_{st}
(
\omega_p\otimes\omega_q
)
\right\|_{\dot H^1}
ds.
}
$$

By duality:

$$
\boxed{
G_J
\le
H_J.
}
$$

By the DRC-02 envelope estimate:

$$
\boxed{
H_J
\le
Q_J.
}
$$

Hence:

$$
\boxed{
P_J
\le
G_J
\le
H_J
\le
Q_J.
}
$$

---

# 20. Three utilization factors

Define:

$$
\boxed{
\mathfrak U_J^{temp}
=
\frac{
P_J
}{
G_J
},
}
$$

$$
\boxed{
\mathfrak U_J^{wit}
=
\frac{
G_J
}{
H_J
},
}
$$

and:

$$
\boxed{
\mathfrak U_J^{geom}
=
\frac{
H_J
}{
Q_J
}.
}
$$

When denominators are nonzero:

$$
\boxed{
\mathfrak U_J
=
\mathfrak U_J^{temp}
\,
\mathfrak U_J^{wit}
\,
\mathfrak U_J^{geom}.
}
$$

---

# 21. Meaning of the three factors

### Temporal / signed utilization

$$
\mathfrak U^{temp}
$$

measures how much absolute-in-time dual interaction survives integration into positive parent ledger mass.

### Witness alignment

$$
\mathfrak U^{wit}
$$

measures how much vector interaction is seen by the selected norming dual direction.

### Geometric utilization

$$
\mathfrak U^{geom}
$$

measures how tight the Hölder/Bernstein parent-state envelope is relative to the actual projected vector interaction.

This includes:

- physical-space overlap;
- tensor orientation;
- Leray / strain projection loss;
- frequency-support geometry.

---

# 22. CIII-3.4 — Utilization Factorization Theorem

## Theorem 22.1

Whenever:

$$
P_J>0,
$$

the DRC-02 utilization admits the exact factorization:

$$
\boxed{
\mathfrak U_J
=
\mathfrak U_J^{temp}
\mathfrak U_J^{wit}
\mathfrak U_J^{geom}.
}
$$

Therefore:

$$
\boxed{
\mathfrak U_J\to0
}
$$

forces at least one of the three factors to collapse.

$\square$

---

# 23. Spatial-separation test

Let:

$$
f,
g
$$

be fixed nonzero smooth divergence-free band-limited vorticity fields.

Let:

$$
x_n\to\infty.
$$

Define:

$$
\boxed{
g_n(x)
=
g(x-x_n).
}
$$

Then:

$$
\|f\|_2,
\qquad
\|g_n\|_2
$$

are constant in:

$$
n.
$$

The DRC-02 Hölder/Bernstein envelope based only on these global parent norms remains uniformly nonzero.

But:

$$
\boxed{
\|f\otimes g_n\|_2
\to0
}
$$

as:

$$
|x_n|\to\infty.
$$

Thus the actual projected vector interaction tends to zero.

---

# 24. CIII-3.5 — Geometric Utilization Collapse No-Go

## Theorem 24.1

There is no universal positive lower bound:

$$
\boxed{
\mathfrak U_J^{geom}
\ge
c>0
}
$$

based only on:

- parent dyadic indices;
- parent global:
  $$
  L^2
  $$
  norms.

### Proof

Use the spatially separated translated parent construction of Section 23.

The global norm envelope remains fixed while the product interaction tends to zero.

$\square$

---

# 25. Meaning for R-UTIL

Utilization collapse can occur because the parent states simply fail to overlap in physical space.

This is a depletion / decoupling mechanism.

Therefore:

$$
\boxed{
R_{\rm UTIL}
}
$$

must not be treated as a primitive monotone-dangerous singularity mechanism.

It is primarily a:

$$
\boxed{
\text{certificate / interaction-geometry failure}
}
$$

until a common spatial core or alignment condition is supplied.

---

# 26. Interaction utilization and the model cone

Miller's strain--vorticity results show that nonlinear interaction alignment can be depleting.

The globally regular strain--vorticity model is precisely a case where an apparently strong nonlinear vorticity/strain interaction does not produce singular growth.

Thus low utilization or poor alignment can be dynamically regularizing.

This provides an external PDE calibration for the semantic reclassification of:

$$
R_{\rm UTIL}.
$$

---

# 27. Localized utilization coordinate

For a wavelength-scale or singular-core region:

$$
\Omega,
$$

define localized parent norms and a localized envelope:

$$
Q_J(\Omega).
$$

Define the localized actual interaction gross:

$$
H_J(\Omega).
$$

Then:

$$
\boxed{
\mathfrak U_J^{geom}(\Omega)
=
\frac{
H_J(\Omega)
}{
Q_J(\Omega)
}.
}
$$

A lower bound for this quantity requires genuine spatial overlap and tensor/projection alignment.

No universal such lower bound is proved here.

---

# 28. Reclassification of utilization

The source genealogy should therefore branch as:

### UTIL-GOOD

localized overlap/alignment is quantitatively nondegenerate;

### UTIL-DEPL

interaction geometry collapses and the available parent state is dynamically depleted/decoupled;

### UTIL-UNKNOWN

state is co-localized but tensor/projection/witness alignment remains unresolved.

Only UTIL-GOOD supports the DRC-02 finite state-parent genealogy without further refinement.

---

# 29. Updated source residuals

DRC-02 had:

$$
R_{\rm CAN},
\quad
R_{\rm UTIL},
\quad
R_{\rm MULT},
\quad
R_{\rm AMP}.
$$

DRC-03 removes:

$$
\boxed{
R_{\rm AMP}
}
$$

as an independent residual by Theorem 15.1.

It also reclassifies generic:

$$
R_{\rm UTIL}
$$

from a dangerous reservoir mechanism into a depletion/certificate-geometry branch.

The genuinely dangerous source residuals are therefore narrowed to:

$$
\boxed{
R_{\rm CAN},
\qquad
R_{\rm MULT},
}
$$

plus unresolved **localized alignment geometry** when one insists on promoting source genealogy to state genealogy.

---

# 30. Updated global residual core

After DRC-03:

$$
\boxed{
\mathfrak R_{\rm III}^{(3)}
=
R_{\rm DISS}
\cup
R_{\rm DIL}
\cup
R_{\rm CAN}
\cup
R_{\rm MULT}
\cup
R_{\rm ALIGN}^{src}.
}
$$

where:

$$
R_{\rm ALIGN}^{src}
$$

denotes unresolved localized tensor/projection/witness alignment after physical overlap has been imposed.

Generic envelope utilization collapse is not itself included as a dangerous class.

---

# 31. Relation to scale-locality literature

Rigorous spectral-flux locality results distinguish local triads from strongly nonlocal triads and show why aggregate many-triad effects must be treated separately from one dominant triad.

This is consistent with:

- the local-cluster treatment in Theorem 6.1;
- preservation of:
  $$
  R_{\rm MULT};
  $$
- the explicit high-low decomposition in Theorem 12.1.

No inertial-range scaling assumption is imported.

---

# 32. Relation to dissipation-range regularity

Cheskidov--Shvydkoy define the dissipation wavenumber precisely so that sufficiently high modes are viscosity dominated.

Theorem 12.1 is a forcing-level companion:

far high-low interactions whose lower parent is already above the dissipation cutoff are a small fraction of the high-shell viscous rate.

Therefore the only nonlocal high-low route which can remain macroscopically important is tied to:

- low-mode driver activity;
- the transition band near the dissipation boundary.

This is exactly the remaining:

$$
R_{\rm DISS}
$$

frontier.

---

# 33. New guards

Add:

### $G_{\rm SCWEIGHT}$

Source-to-state amplification must remove the deterministic:

$$
2^{5h/2}
$$

scale weight before being called anomalous.

### $G_{\rm LOCALCL}$

Scale-local source packets must preserve the associated finite parent-cluster stock.

### $G_{\rm HILOQ}$

Deep high-low source geometry must be split relative to:

$$
Q(s)
$$

into driver, transition and absorbable sectors.

### $G_{\rm UFACT}$

Envelope utilization must be decomposed into temporal, witness and geometric factors.

### $G_{\rm OVERLAP}$

A global-norm parent envelope cannot certify physical interaction without an overlap condition.

### $G_{\rm UTILSEM}$

Utilization collapse is not a monotone dangerous mechanism unless a separate dynamic theorem says so.

---

# 34. Next paper

The source residual has now become sharply concentrated on:

$$
\boxed{
R_{\rm CAN},
\qquad
R_{\rm MULT}.
}
$$

Therefore the next paper should attack signed coherence and many-parent aggregation.

$$
\boxed{
\textbf{
NS-DRC 04 —
Cancellation Rigidity、
Many-Parent Aggregation、
Signed Coherence
與 State-Multiplicity Transfer
}.
}
$$

Primary tasks:

1. quantify positive/negative parent-gross cancellation across viscous-age slabs;
2. seek a signed-coherence lower bound from repeated renewal;
3. combine bounded scale-corrected amplification with parent multiplicity to transfer source multiplicity into actual state-cluster multiplicity;
4. test whether many-parent state multiplicity forces:
   $$
   D_{\rm eig}
   $$
   or spatial multiplicity;
5. determine whether:
   $$
   R_{\rm CAN}
   \vee
   R_{\rm MULT}
   $$
   can be reduced to the already known spectral/spatial guards.

---

# 35. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{natural local }2^{5h/2}\text{ source weight}
&:\ \mathrm{PROVED},\\
\text{scale-corrected local cluster envelope}
&:\ \mathrm{PROVED},\\
\text{local cluster state lower bound}
&:\ \mathrm{PROVED},\\
\text{far high-low viscous absorption}
&:\ \mathrm{PROVED},\\
R_{\rm AMP}\text{ as independent residual}
&:\ \mathrm{ABSORBED},\\
\text{three-factor utilization decomposition}
&:\ \mathrm{PROVED},\\
\text{spatial-separation utilization no-go}
&:\ \mathrm{PROVED},\\
R_{\rm UTIL}\text{ as monotone dangerous class}
&:\ \mathrm{RECLASSIFIED},\\
R_{\rm CAN}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm MULT}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm ALIGN}^{src}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm DISS}\text{ closure}
&:\ \mathrm{OPEN},\\
R_{\rm DIL}\text{ closure}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 36. Conclusion

DRC-03 shows that the source-amplification problem was partly over-parameterized.

For scale-local high-parent interactions, the natural Hdot1-vorticity source weight is:

$$
2^{5h/2}.
$$

After correcting for this deterministic scale factor, a large local source packet already has a finite parent-cluster state reservoir.

The only far high-low interactions that remain macroscopically relevant are tied to the low-mode driver or the dissipation-boundary transition region; high-low interactions entirely inside the deep dissipation range are viscosity-absorbable.

Thus:

$$
\boxed{
R_{\rm AMP}
}
$$

is absorbed into scale-corrected state support or:

$$
R_{\rm DISS}.
$$

The utilization variable also admits the exact factorization:

$$
\boxed{
\mathfrak U
=
\mathfrak U^{temp}
\mathfrak U^{wit}
\mathfrak U^{geom}.
}
$$

A spatial-separation construction proves that geometric utilization may collapse while all parent global norms remain fixed.

Therefore generic:

$$
R_{\rm UTIL}
$$

is a depletion/certificate-geometry failure, not an independent dangerous reservoir mechanism.

The main unresolved source mechanisms are now cancellation and many-parent aggregation.

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691v2.
2. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
3. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.
4. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.
5. E. Bertram, *From Triadic Interactions to Kolmogorov Scaling: A Deterministic, Scale-Resolved Formulation of Energy Flux*, arXiv:2607.16381. Used only as contemporary exact-triad bookkeeping calibration.
6. `NS_DRC_01_ExponentialPreload_PrehistoryRenewal_v0.1.md`.
7. `NS_DRC_02_SourceToState_Efficiency_RenewalChain_v0.1.md`.
8. `NS_CSP_08_UnifiedReservoirCover_CycleIIClosure_v0.1.md`.
