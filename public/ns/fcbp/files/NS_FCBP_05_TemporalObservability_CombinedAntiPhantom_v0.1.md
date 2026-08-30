---
title: "Navier–Stokes Forest Coercive Budget Program 05：Long-Age Observability、Sharp Half-Exponent Window Threshold、Combined Anti-Phantom Detection 與 Paid-Side Recurrence"
short_title: "NS-FCBP 05"
series: "Navier–Stokes Forest Coercive Budget Program"
cycle: "VI"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Temporal criticality / combined-observability compiler / paid-side audit"
epistemic_status: "Proves that a direct universal bridge from fresh vorticity source to one signed kinetic-energy-work channel is impossible: the Navier-Stokes nonlinearity is globally energy-orthogonal while its curl can be nonzero. Replaces the single-channel CRW target by combined pressure/flux/positive-energy/adjoint-trace/model-cone observability. Proves a sharp sequence theorem for finite-time horizon schedules: if r_k decreases and sum r_k^2 is finite, with normalized horizon thickness delta_k=1-(r_{k+1}/r_k)^2, then sum r_k delta_k^a is finite for every a>1/2; the exponent a=1/2 is sharp, with explicit logarithmic schedules for which the series diverges. Consequently, for moving-window observability growth M_k less than or comparable to delta_k^{-gamma} and depletion exponent q, gamma q=1/2 is the sharp temporal threshold for schedule-based depletion effectiveness: gamma q<1/2 admits power schedules, gamma q=1/2 admits logarithmic borderline schedules, while gamma q>1/2 cannot be forced effective from this growth law alone on any finite-time monotone schedule. Integrates Tao's quantitative L^3 back-propagation as an external strong-critical Long-Age State Propagation module with parabolic scale migration, and recent finite-window anti-phantom/recursive-audit results as conditional combined detector modules. Proves an abstract signed-telescope total-variation no-go showing endpoint-energy control alone cannot bound weighted backscatter. The remaining Horizon Critical Lift is reduced to causal-to-audit realization, combined-window growth at or below the half-exponent threshold, invisible-cascade exclusion, and paid-side sign/leakage control. No Forest Coercive Budget, Finite Forest Obstruction, atomic CN3, or Navier-Stokes regularity is proved."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Forest Coercive Budget Program 05

# Long-Age Observability、Sharp Half-Exponent Window Threshold、Combined Anti-Phantom Detection 與 Paid-Side Recurrence

## 0. 本文定位

FCBP-04 separated the horizon temporal problem into:

$$
\boxed{
\text{LAO}
\vee
\text{Thin-Window Amplification}.
}
$$

It also showed that the filter endpoint problem is no longer the principal obstruction.

The current questions are:

1. can dangerous information remain observable over many local parabolic ages?;
2. on horizon-aligned thin windows, how fast may observability constants deteriorate while a non-summable depletion schedule remains possible?;
3. can fresh vorticity renewal be forced into one signed pressure--flux work channel?;
4. can the paid-side backscatter/leakage be controlled by endpoint energy alone?

The answers produce a sharper temporal phase diagram.

---

# 1. Velocity nonlinearity and global energy orthogonality

Let:

$$
\boxed{
\mathcal N
=
-\mathbb P\nabla\cdot(u\otimes u).
}
$$

For smooth divergence-free finite-energy velocity:

$$
\boxed{
\langle
\mathcal N,u
\rangle_{L^2}
=
0.
}
$$

### Proof

Since the Leray projector is self-adjoint and:

$$
\mathbb Pu=u,
$$

$$
\langle\mathcal N,u\rangle
=
-
\langle
\nabla\cdot(u\otimes u),
u
\rangle.
$$

Integrate by parts:

$$
=
\int
u_i u_j
\partial_j u_i
dx
=
\frac12
\int
u_j
\partial_j
|u|^2
dx
=
0.
$$

$\square$

---

# 2. Vorticity forcing may remain nonzero

Define:

$$
\boxed{
\mathcal G
=
-\nabla\times\mathcal N.
}
$$

Consider the explicit Schwartz divergence-free field:

$$
\boxed{
u(x,y,z)
=
\left(
-2y e^{-R^2},
2x e^{-R^2},
0
\right),
\qquad
R^2=x^2+y^2+z^2.
}
$$

A direct computation gives:

$$
\boxed{
\mathcal G
=
\left(
16yz e^{-2R^2},
-16xz e^{-2R^2},
0
\right),
}
$$

up to the harmless sign convention used in:

$$
\mathcal N.
$$

Thus:

$$
\boxed{
\mathcal G\not\equiv0
}
$$

while the global nonlinear kinetic-energy work is zero.

---

# 3. CIV/VI-5.1 — Single Energy-Work Bridge No-Go

## Theorem 3.1

There is no universal coercive estimate of the form:

$$
\boxed{
|
\langle
\mathcal N,u
\rangle
|
\ge
c
\mathfrak S(\mathcal G)
}
$$

for all smooth divergence-free finite-energy fields, with:

$$
c>0
$$

and any nonnegative source functional:

$$
\mathfrak S
$$

that is strictly positive on every nonzero:

$$
\mathcal G.
$$

### Proof

The left-hand side vanishes identically by Section 1.

Section 2 gives a field with:

$$
\mathcal G\neq0.
$$

$\square$

---

# 4. Meaning for CRW

The FCBP-04 bridge:

$$
\text{fresh causal renewal}
\Longrightarrow
\text{work}
$$

cannot be interpreted as a universal one-channel global kinetic-energy-work inequality.

The correct target is a **combined observation hierarchy**.

Define:

$$
\boxed{
\textbf{CCRW — Combined Causal-Renewal Observability}
}
$$

to mean that a dangerous fresh-renewal package must become visible in at least one of:

- active pressure;
- resolved flux;
- positive energy/dissipation;
- selected adjoint trace;
- model-cone excess;
- or an explicitly paid residual channel.

---

# 5. External combined observability framework

Recent finite-window Navier--Stokes work defines a combined observation map:

$$
\boxed{
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
),
}
$$

with active pressure, flux, positive energy, and adjoint-trace channels.

The corresponding moving-window branch observability constant is:

$$
\boxed{
M_n
=
\sup_{
0\neq d\in Y_n^{NS}
}
\frac{
\|d\|_{Y_n}
}{
\mathsf O_n(d)
}.
}
$$

When:

$$
M_n<\infty,
$$

every normalized NS-realizable defect obeys:

$$
\boxed{
\mathsf O_n(\widehat d)
\ge
M_n^{-1}.
}
$$

### Status

$$
\boxed{
\mathrm{EXTERNAL/CONDITIONAL\ FRAMEWORK}.
}
$$

---

# 6. External observable depletion

On an extraction set:

$$
I=\{n_k\},
$$

the moving-window framework assumes/proves in controlled modules a depletion inequality of the form:

$$
\boxed{
\mathscr B_k
-
\mathscr B_{k+1}
\ge
c
\lambda_{n_k}
\mathsf O_{n_k}(\widehat d_{n_k})^q
-
e_k,
}
$$

with:

$$
\boxed{
\sum_ke_k<\infty.
}
$$

The moving windows are depletion-effective when:

$$
\boxed{
\sum_k
\lambda_{n_k}
M_{n_k}^{-q}
=
\infty.
}
$$

Under the paper's extraction/depletion/finite-window hypotheses, failure of regularity is then reduced to non-effective moving-window observability or an NS-realizable combined-invisible defect cascade.

### Status

$$
\boxed{
\mathrm{EXTERNAL/CONDITIONAL}.
}
$$

---

# 7. Horizon-aligned radius sequence

Let:

$$
r_k>0
$$

be decreasing with:

$$
\boxed{
\sum_k
r_k^2
<
\infty.
}
$$

This is the finite-time requirement for a parabolic horizon schedule.

Define:

$$
\boxed{
d_k
=
1-
\left(
\frac{
r_{k+1}
}{
r_k
}
\right)^2
\in[0,1].
}
$$

The horizon-aligned normalized slab thickness in FCBP-04 is:

$$
\delta_k
=
c\,d_k.
$$

Since constants do not affect summability, the analysis below uses:

$$
d_k.
$$

---

# 8. CIV/VI-5.2 — Sharp Half-Exponent Schedule Theorem

## Theorem 8.1

Let:

$$
r_k
$$

be positive, nonincreasing, and:

$$
\sum_kr_k^2<\infty.
$$

Then for every:

$$
\boxed{
a>\frac12,
}
$$

$$
\boxed{
\sum_k
r_k
d_k^a
<
\infty.
}
$$

Moreover the exponent:

$$
a=\frac12
$$

is sharp: there exist decreasing sequences with:

$$
\sum_kr_k^2<\infty
$$

but:

$$
\boxed{
\sum_k
r_k
d_k^{1/2}
=
\infty.
}
$$

---

# 9. Proof for $a\ge1$

Since:

$$
0\le d_k\le1,
$$

$$
d_k^a\le d_k.
$$

Write:

$$
q_k
=
r_{k+1}/r_k.
$$

Then:

$$
d_k
=
1-q_k^2
=
(1-q_k)(1+q_k)
\le
2(1-q_k).
$$

Therefore:

$$
r_kd_k
\le
2(r_k-r_{k+1}).
$$

Hence:

$$
\boxed{
\sum_kr_kd_k^a
\le
2r_0.
}
$$

---

# 10. Proof for $1/2<a<1$

Set:

$$
s_k=r_k^2.
$$

Normalize:

$$
s_0\le1.
$$

For:

$$
m\ge0,
$$

define the dyadic level block:

$$
\boxed{
B_m
=
\{
k:
2^{-m-1}<s_k\le2^{-m}
\}.
}
$$

Let:

$$
L_m
=
|B_m|.
$$

Since:

$$
\sum_ks_k<\infty,
$$

$$
\boxed{
\sum_m
L_m2^{-m}
<
\infty.
}
$$

For indices whose two endpoints remain inside one block:

$$
\sum
d_k
\le
\sum
-\log(1-d_k)
=
\log
\frac{s_{\rm first}}{s_{\rm last+1}}
\le
\log2.
$$

By concavity:

$$
\sum_{k\in B_m^{int}}
d_k^a
\le
C_a
L_m^{1-a}.
$$

Since:

$$
r_k\le2^{-m/2}
$$

on:

$$
B_m,
$$

the internal block contribution is at most:

$$
C_a
2^{-m/2}
L_m^{1-a}.
$$

Write:

$$
x_m=L_m2^{-m}.
$$

Then:

$$
2^{-m/2}
L_m^{1-a}
=
x_m^{1-a}
2^{-m(a-1/2)}.
$$

The sequence:

$$
x_m
$$

is summable and hence bounded.

Since:

$$
a-\frac12>0,
$$

the remaining exponential factor is summable.

There is at most one block-exit index per level, whose contribution is:

$$
O(2^{-m/2}),
$$

also summable.

Thus:

$$
\sum_kr_kd_k^a<\infty.
$$

$\square$

---

# 11. Sharpness at $a=1/2$

Choose:

$$
\boxed{
r_k
=
\frac1{
\sqrt{k+2}
[
\log(k+2)
]^b
},
\qquad
\frac12<b\le1.
}
$$

Then:

$$
\boxed{
\sum_kr_k^2
=
\sum_k
\frac1{
(k+2)
[
\log(k+2)
]^{2b}
}
<
\infty.
}
$$

A direct expansion gives:

$$
\boxed{
d_k
\asymp
\frac1{k+2}.
}
$$

Therefore:

$$
\boxed{
r_kd_k^{1/2}
\asymp
\frac1{
(k+2)
[
\log(k+2)
]^b
}.
}
$$

For:

$$
b\le1,
$$

this series diverges.

Thus:

$$
\boxed{
a=\frac12
}
$$

is the exact borderline.

---

# 12. Temporal observability growth model

Assume a moving-window combined observability constant satisfies:

$$
\boxed{
M_k
\le
C
d_k^{-\gamma},
}
$$

for:

$$
\gamma\ge0.
$$

Then:

$$
\boxed{
M_k^{-q}
\ge
C^{-q}
d_k^{\gamma q}.
}
$$

Use the slow pressure--flux/forest weight:

$$
\boxed{
\lambda_k
=
w_k
=
r_k/r_0.
}
$$

The effective depletion series has the lower bound:

$$
\boxed{
\sum_k
\lambda_k
M_k^{-q}
\gtrsim
\frac1{r_0}
\sum_k
r_k
d_k^{\gamma q}.
}
$$

---

# 13. CIV/VI-5.3 — Thin-Window Observability Threshold

## Theorem 13.1

Let:

$$
a
=
\gamma q.
$$

### Subcritical temporal deterioration

If:

$$
\boxed{
a<\frac12,
}
$$

there exists a power-law finite-time horizon schedule:

$$
r_k
=
r_0
(k+1)^{-\beta},
$$

with:

$$
\boxed{
\frac12<\beta\le1-a,
}
$$

such that:

$$
\boxed{
\sum_k
\lambda_k
M_k^{-q}
=
\infty.
}
$$

### Borderline temporal deterioration

If:

$$
\boxed{
a=\frac12,
}
$$

there exists a logarithmic finite-time horizon schedule:

$$
\boxed{
r_k
=
\frac{
r_0
}{
\sqrt{k+2}
[
\log(k+2)
]^b
},
\qquad
\frac12<b\le1,
}
$$

such that:

$$
\boxed{
\sum_k
\lambda_k
M_k^{-q}
=
\infty.
}
$$

### Super-borderline deterioration

If:

$$
\boxed{
a>\frac12,
}
$$

Theorem 8.1 shows that the polynomial growth control:

$$
M_k\le C d_k^{-\gamma}
$$

alone cannot force the lower-bound series:

$$
\sum_k
r_kd_k^{a}
$$

to diverge on any monotone finite-time schedule.

### Meaning

$$
\boxed{
\gamma q=\frac12
}
$$

is the sharp schedule-level temporal threshold for this depletion mechanism.

$\square$

---

# 14. Comparison with the single-work thin-slab requirement

FCBP-04's single pressure--flux work compiler required approximately:

$$
\boxed{
\mathcal W_k^+
\gtrsim1
}
$$

on thin slabs, or equivalently an inverse-thickness normalized work rate.

The combined-observability compiler is weaker.

It permits the detector to deteriorate polynomially with window thickness as long as:

$$
\boxed{
\gamma q\le\frac12.
}
$$

Thus:

$$
\boxed{
\text{combined observability changes the temporal critical exponent}.
}
$$

---

# 15. CIV/VI-5.4 — Combined Horizon Depletion Compiler

## Theorem 15.1

Assume a dangerous horizon branch produces NS-realizable normalized defect packages:

$$
\widehat d_k
$$

with:

1. depletion:
   $$
   \mathscr B_k-\mathscr B_{k+1}
   \ge
   c
   w_k
   \mathsf O_k(\widehat d_k)^q
   -
   e_k;
   $$

2.:
   $$
   \sum_ke_k<\infty;
   $$

3. observability:
   $$
   \mathsf O_k(\widehat d_k)
   \ge
   M_k^{-1};
   $$

4.:
   $$
   M_k
   \le
   C
   d_k^{-\gamma};
   $$

5.:
   $$
   \gamma q
   \le
   \frac12;
   $$

6. the horizon schedule is chosen from Theorem 13.1.

Then the branch cannot persist indefinitely.

### Proof

Theorem 13.1 gives:

$$
\sum_k
w_k
M_k^{-q}
=
\infty.
$$

Hence:

$$
\sum_k
(
\mathscr B_k-\mathscr B_{k+1}
)
$$

would diverge after subtracting a summable error, contradicting nonnegativity and finiteness of the initial budget.

$\square$

---

# 16. Causal-to-audit realization

Theorem 15.1 starts with an NS-realizable normalized defect package.

ANP/CFOP starts with a dangerous causal node or a fresh-renewal packet.

Define:

$$
\boxed{
\textbf{CAR — Causal-to-Audit Realization}.
}
$$

CAR is a theorem which maps an ANP/CFOP dangerous causal package into the finite-window quotient geometry used by the combined detector while preserving a uniform nontrivial baseline distance modulo explicitly controlled residuals.

Current status:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 17. External finite-window anti-phantom module

Recent local-to-clean work proves, under synchronized representatives, quotient lifting, component comparisons, residual-ledger closure, detector comparison, chart visibility, and a clean quotient gap:

$$
\boxed{
\text{baseline-visible package}
\Longrightarrow
\text{localized detector}
\vee
\text{explicit residual ledger}.
}
$$

A later recursive-audit paper proves finite-chain anti-phantom lower bounds under explicit synchronization/localization/projection/harmonic/gate/detector/chart ledgers.

### FCBP interpretation

If CAR supplies a nontrivial baseline defect and the anti-phantom residuals are controlled, then the combined detector cannot disappear for free.

### Status

$$
\boxed{
\mathrm{EXTERNAL/CONDITIONAL}.
}
$$

---

# 18. Anti-phantom moving-window route

The combined moving-window paper gives the structural alternative:

$$
\boxed{
\text{non-effective moving-window observability}
\vee
\text{NS-realizable combined-invisible defect cascade}
}
$$

under its extraction/depletion/hierarchy hypotheses.

FCBP-05 refines the first branch:

a polynomial window-growth model:

$$
M_k
\lesssim
d_k^{-\gamma}
$$

is schedule-compatible with depletion whenever:

$$
\boxed{
\gamma q\le1/2.
}
$$

Thus a surviving non-effective branch must either:

- grow faster than this threshold in the relevant schedule class;
- be extracted too sparsely;
- fail CAR/residual transfer;
- or enter the combined-invisible cascade.

---

# 19. Long-Age State Propagation in the strong $L^3$ subbranch

Tao's quantitative critical:

$$
L_t^\infty L_x^3
$$

theory provides an external iterated back-propagation theorem.

Assume:

$$
\boxed{
\|u\|_{L_t^\infty L_x^3}
\le
A.
}
$$

If a terminal point has a critical frequency bubble:

$$
|P_{N_0}u(t_0,x_0)|
\ge
A_1^{-1}N_0,
$$

then for every admissible longer time scale:

$$
T_1,
$$

there exists an earlier bubble:

$$
(t_1,x_1,N_1),
$$

with:

$$
\boxed{
N_1
=
A^{O(1)}
T_1^{-1/2},
}
$$

and:

$$
\boxed{
|x_1-x_0|
\le
A^{O(1)}
T_1^{1/2},
}
$$

while the critical amplitude threshold is preserved up to the fixed quantitative constants.

### Status

$$
\boxed{
\mathrm{EXTERNAL/PROVED}
}
$$

in the strong:

$$
L_t^\infty L_x^3
$$

branch.

---

# 20. LAO scale migration

Theorem 19 shows that long-age state observability is naturally accompanied by parabolic scale migration:

$$
\boxed{
R_{\rm obs}
\sim
T_1^{1/2}.
}
$$

If the terminal local scale is:

$$
r,
$$

and one propagates over:

$$
K
$$

local parabolic ages:

$$
T_1
\sim
Kr^2,
$$

then:

$$
\boxed{
R_{\rm obs}
\sim
\sqrt K\,r.
}
$$

Thus LAO should not be formulated as "the same tiny scale remains visible far into the past."

The natural state observable coarsens with elapsed parabolic age.

---

# 21. LAO safety

Tao's theorem assumes a uniform strong:

$$
L^3
$$

critical bound.

The ANP Type-I branch was formulated at the weak endpoint:

$$
L^{3,\infty}.
$$

Therefore:

$$
\boxed{
\text{strong }L^3\text{ LAO}
}
$$

cannot be imported as a theorem for the general weak:

$$
L^{3,\infty}
$$

Type-I branch.

It is an external strong-subbranch calibration.

---

# 22. State propagation is not work observability

Even in the strong:

$$
L^3
$$

subbranch, Tao's theorem produces:

- a velocity/frequency bubble;
- spatial displacement control;
- scale migration.

It does not prove:

$$
\boxed{
\text{active pressure--flux work}
}
$$

or the FCBP combined finite-window detector is bounded below.

Thus LAO-state and combined-work observability remain distinct layers.

---

# 23. Signed endpoint budgets do not control backscatter variation

Let:

$$
B_k\ge0
$$

be bounded endpoint budgets and suppose:

$$
\boxed{
B_k-B_{k+1}=a_k.
}
$$

A bound on:

$$
B_k
$$

controls the signed partial sums of:

$$
a_k.
$$

It does not control:

$$
\sum_ka_k^-.
$$

---

# 24. CIV/VI-5.5 — Signed-Telescope Total-Variation No-Go

## Theorem 24.1

There exist bounded nonnegative:

$$
B_k
$$

for which:

$$
a_k=B_k-B_{k+1}
$$

has:

$$
\boxed{
\sum_ka_k^-=\infty
}
$$

and:

$$
\boxed{
\sum_ka_k^+=\infty.
}
$$

### Proof

Take:

$$
B_{2m}=1,
\qquad
B_{2m+1}=0.
$$

Then:

$$
a_{2m}=1,
$$

and:

$$
a_{2m+1}=-1.
$$

Both positive and negative total variations diverge while:

$$
0\le B_k\le1.
$$

$\square$

---

# 25. Meaning for pressure--flux backscatter

The pressure--flux endpoint telescope is a signed budget.

Endpoint kinetic-energy boundedness alone does not imply finite weighted backscatter variation.

Therefore:

$$
\boxed{
\text{weighted backscatter closure}
}
$$

requires an additional:

- sign-coherence;
- total-variation;
- recurrence;
- or observable-depletion theorem.

It cannot be obtained solely from the endpoint energy telescope.

---

# 26. Paid-side recurrence

If a horizon branch avoids forward depletion by repeatedly generating large negative combined work:

$$
\mathcal W_k^-,
$$

this is not a bookkeeping error.

It is a recurrent backscatter mechanism.

Define:

$$
\boxed{
\textbf{BSR — Backscatter Recurrence}.
}
$$

Likewise persistent localization payment defines:

$$
\boxed{
\textbf{LKR — Leakage Recurrence}.
}
$$

These are paid-side recurrence objects.

Neither is universally excluded.

---

# 27. Temporal criticality trichotomy

After FCBP-05, a persistent dangerous horizon branch must enter at least one of:

### TC-OBS

depletion-effective combined observability;

### TC-INVIS

an NS-realizable combined-invisible defect cascade;

### TC-PAID

backscatter/leakage recurrence or another explicit residual ledger;

### TC-REAL

failure of causal-to-audit realization;

### TC-GROW

moving-window observability deteriorates beyond the schedule-effective threshold.

The first branch is depleting.

The remaining branches are the true temporal obstruction classes.

---

# 28. Sharp temporal threshold

For polynomial thin-window growth:

$$
M_k
\lesssim
d_k^{-\gamma},
$$

and depletion exponent:

$$
q,
$$

the schedule threshold is:

$$
\boxed{
\gamma q
=
\frac12.
}
$$

This exponent comes from only two requirements:

1. finite total parabolic horizon time:
   $$
   \sum r_k^2<\infty;
   $$

2. divergent moving-window depletion:
   $$
   \sum r_kd_k^{\gamma q}
   =
   \infty.
   $$

Thus it is a genuine temporal geometry threshold, not a detector-specific constant.

---

# 29. Relation to logarithmic admissibility

The external moving-window framework allows observability constants with more complicated growth:

$$
M_n
\le
C
N_n^a
\exp(CN_n^b),
$$

and defines logarithmically admissible windows by divergence of the corresponding weighted reciprocal series.

FCBP-05's half-exponent theorem is complementary:

it treats deterioration explicitly as a power of normalized physical window thickness and identifies the exact finite-time horizon threshold.

Both approaches reduce temporal observability to a weighted divergent-series problem.

---

# 30. Combined Horizon Critical-Lift criterion

## Theorem 30.1

Suppose an ANP/CFOP horizon branch satisfies:

1. CAR;
2. finite-window anti-phantom transfer with summable residuals;
3. an observable-depletion ledger with:
   $$
   \lambda_k\asymp r_k/r_0;
   $$
4. moving-window combined observability:
   $$
   M_k\le C d_k^{-\gamma};
   $$
5.:
   $$
   \gamma q\le1/2;
   $$
6. no combined-invisible cascade;
7. no non-summable paid-side backscatter/leakage recurrence.

Then the dangerous horizon branch cannot persist indefinitely.

### Status

$$
\boxed{
\mathrm{PROVED\ CONDITIONAL}.
}
$$

### Proof

Use CAR and anti-phantom transfer to obtain an NS-realizable observed defect.

Use Theorem 13.1 to choose a finite-time horizon schedule with:

$$
\sum w_kM_k^{-q}=\infty.
$$

Observable depletion then exhausts the finite selected budget.

The remaining assumptions exclude the alternate invisible/paid residual branches.

$\square$

---

# 31. What remains open

The scale and filter compatibility problems are no longer the primary barriers.

The unresolved theorems are now:

### CAR

causal renewal/danger to finite-window NS-defect realization;

### MWG

moving-window growth at or below the sharp temporal threshold, or another depletion-effective growth law;

### INV

exclusion of NS-realizable combined-invisible defect cascades;

### PAID

weighted backscatter/leakage recurrence control;

### weak-endpoint LAO

long-age propagation in the general weak:

$$
L^{3,\infty}
$$

Type-I branch.

---

# 32. Next paper

The next paper should attack the last combined-observability objects directly:

$$
\boxed{
\textbf{
NS-FCBP 06 —
Causal-to-Audit Transfer、
Combined-Invisible Cascades、
Backscatter Sign Coherence
與 Cycle-VI Closure Audit
}.
}
$$

Primary tasks:

1. map ANP/CFOP causal renewal packets into the finite-window defect quotient;
2. compare source/provenance coordinates with pressure--flux--energy--trace packages;
3. test clean-gap/anti-phantom hypotheses on the canonical Footprint/Dual Node class;
4. derive or refute a weighted backscatter sign-coherence theorem;
5. classify combined-invisible recurrent objects against model-cone and filtered commutator recurrence;
6. decide whether Cycle VI yields a genuine Forest Coercive Budget or only a final combined-invisible reduction.

---

# 33. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{Single global energy-work CRW}
&:\ \mathrm{NO\mbox{-}GO},\\
\text{combined CRW semantics}
&:\ \mathrm{DEFINED},\\
\text{Sharp Half-Exponent Schedule Theorem}
&:\ \mathrm{PROVED},\\
\text{Thin-Window Observability Threshold}
&:\ \mathrm{PROVED},\\
\text{Combined Horizon Depletion Compiler}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{strong-}L^3\text{ Long-Age State Propagation}
&:\ \mathrm{EXTERNAL/PROVED},\\
\text{general weak-}L^{3,\infty}\text{ LAO}
&:\ \mathrm{OPEN},\\
\text{finite-window anti-phantom detection}
&:\ \mathrm{EXTERNAL/CONDITIONAL},\\
CAR
&:\ \mathrm{OPEN},\\
\text{Signed-Telescope Total-Variation No-Go}
&:\ \mathrm{PROVED},\\
\text{weighted backscatter closure}
&:\ \mathrm{OPEN},\\
\text{combined-invisible cascade exclusion}
&:\ \mathrm{OPEN},\\
\text{Critical Lift}
&:\ \mathrm{OPEN},\\
\text{Forest Coercive Budget}
&:\ \mathrm{OPEN},\\
\text{Finite Forest Obstruction}
&:\ \mathrm{OPEN},\\
CN3_{\rm Atomic}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 34. Conclusion

FCBP-05 resolves the temporal scaling question more sharply than the previous single-work route.

Fresh vorticity source cannot be universally coerced into one signed kinetic-energy-work observable.

The correct target is combined finite-window observability.

For a finite-time horizon schedule:

$$
\sum_kr_k^2<\infty,
$$

define the relative thin-window decrement:

$$
d_k
=
1-
(r_{k+1}/r_k)^2.
$$

Then the exact sequence threshold is:

$$
\boxed{
\sum_kr_kd_k^a<\infty
\quad
\text{for every }
a>1/2,
}
$$

while:

$$
a=1/2
$$

admits explicit logarithmic divergent examples.

Therefore a combined observability constant with polynomial deterioration:

$$
M_k
\lesssim
d_k^{-\gamma}
$$

is compatible with depletion-effective horizon scheduling precisely up to the sharp borderline:

$$
\boxed{
\gamma q\le1/2.
}
$$

This is substantially weaker than requiring order-one signed pressure--flux work on every vanishing window.

In the strong critical:

$$
L_t^\infty L_x^3
$$

subbranch, Tao's quantitative back-propagation shows that long-age state observability can persist, but only with natural parabolic scale migration.

The remaining problem is not whether there exist detectors in principle.

Finite-window anti-phantom and recursive-audit frameworks already show that under explicit structural hypotheses, a baseline-visible NS-generated defect cannot be both detector-silent and residual-cheap.

The missing step is to place the ANP/CFOP causal renewal package inside that quotient/detector architecture with horizon-uniform control.

At the same time, signed endpoint energy alone cannot control total backscatter variation.

Thus the final temporal critical-lift frontier is:

$$
\boxed{
\textbf{
Causal-to-Audit Realization
+
sharp moving-window observability
+
invisible-cascade exclusion
+
paid-side sign control.
}
}
$$

That is FCBP-06.

---

# References

1. T. Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations*, arXiv:1908.04958.
2. R. Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756.
3. R. Yu, *Finite-Window Local-to-Clean Transfer and Anti-Phantom Detection for Sharp Navier--Stokes Packages*, arXiv:2606.18476.
4. R. Yu, *Finite-Window Recursive Audit Chains for Navier--Stokes Generated Packages*, arXiv:2606.20899.
5. R. Yu, *Finite-Window Singularity Audits and Local-to-Clean Defect Transfer for Navier--Stokes*, arXiv:2606.15086.
6. `NS_FCBP_04_MovingFilter_HorizonAlignment_v0.1.md`.
