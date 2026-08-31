---
title: "Navier–Stokes Causal Forest Obstruction Program 02: Spatial–Scale Atomization, Forest Capacity, Enstrophy Cutsets, Driver Interfaces and Diffuse-Cascade Rigidity"
short_title: "NS-CFOP 02"
series: "Navier–Stokes Causal Forest Obstruction Program"
cycle: "V"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Spatial-scale forest capacity / propagated-state budget / diffuse-cut rigidity"
epistemic_status: "Introduces wavelength-cell and space-scale forest capacities for canonical weighted vorticity states and dual causal loads. Proves that a state whose weighted mass is tight in a radius-R footprint and W dyadic shells has a strongest space-scale atom of relative size at least c(1-epsilon)/(W(1+2^J R)^3); hence absence of a strong atom forces shell-span/scale-span growth or state-tail escape. Defines effective space-scale multiplicity and entropy ceilings. Localizes the CFOP-01 dual congestion to wavelength cells and proves both source Action–Congestion Duality and a propagated State–Congestion Duality. The latter couples directly to the Leray finite enstrophy-time budget, yielding a universal measure bound for low-congestion propagated-dominant cuts. For source-dominated cuts, high effective dual capacity under a total-load ceiling forces forcing action proportional to capacity per unit cut duration. Introduces a SPARSE-GUARD interface: if spatial atomization meets established one-dimensional sparseness/analyticity regularity criteria, the branch is regularizing; otherwise it remains a non-sparse capacity branch. The paper does not prove that all diffuse forests satisfy the sparseness guard, does not prove a finite global nonlinear forcing-action budget, and does not establish a complete Forest Finite Obstruction or Navier-Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Causal Forest Obstruction Program 02

# Spatial–Scale Atomization, Forest Capacity, Enstrophy Cutsets, Driver Interfaces and Diffuse-Cascade Rigidity

## 0. Positioning of this Paper

CFOP-01 proved the forest cutset inequality:

$$
\boxed{
\mathfrak A_F
\mathfrak K_C
\ge
\sigma^2
}
$$

on source-dominated dangerous cuts.

It also showed that fresh-source atomization forces effective multiplicity and branching entropy growth.

The next question is:

> Can the forest make causal congestion arbitrarily small simply by spreading itself over more and more positions and scales?

The present paper quantifies the spatial--scale capacity available to the forest.

The main conclusions are:

1. bounded spatial--scale capacity forces a strong atom;
2. high dual capacity lowers congestion and therefore raises source-action cost;
3. propagated causal flow with low congestion consumes the finite Navier--Stokes enstrophy-time budget;
4. spatial atomization which reaches established sparseness/analyticity conditions enters a regularizing geometric guard;
5. the unresolved diffuse branch must therefore pay capacity growth, source action, congestion, or a non-sparse spatial/profile escape.

---

# 1. Wavelength scale

For a dyadic shell:

$$
k\in\mathbb Z,
$$

define the wavelength:

$$
\boxed{
\ell_k
=
2^{-k}.
}
$$

Let:

$$
\psi(x)
$$

be a nonnegative canonical Footprint Node weight.

Let:

$$
c_\psi
$$

be its centroid and:

$$
R
$$

a physical footprint radius coordinate.

Define:

$$
\boxed{
\Xi_k
=
2^kR
=
R/\ell_k.
}
$$

This is the number of wavelengths across one footprint radius.

---

# 2. Weighted shell state

Define:

$$
\boxed{
E_k^\psi
=
\int
\psi(x)
|\omega_k(x)|^2dx.
}
$$

For a finite shell set:

$$
\mathcal K
\subset\mathbb Z,
$$

define:

$$
\boxed{
E_{\mathcal K}^\psi
=
\sum_{k\in\mathcal K}
E_k^\psi.
}
$$

Assume:

$$
E_{\mathcal K}^\psi>0.
$$

---

# 3. Weighted-state tightness

For:

$$
A\ge1,
$$

define the state tail fraction:

$$
\boxed{
\varepsilon_{\rm st}(A)
=
\frac{
\displaystyle
\sum_{k\in\mathcal K}
\int_{
|x-c_\psi|>AR
}
\psi|\omega_k|^2dx
}{
E_{\mathcal K}^\psi
}.
}
$$

The state is:

$$
\boxed{
(A,\varepsilon)\text{-tight}
}
$$

if:

$$
\boxed{
\varepsilon_{\rm st}(A)
\le
\varepsilon<1.
}
$$

This is stronger than tightness of the footprint weight alone.

---

# 4. Wavelength-cell cover

For each:

$$
k\in\mathcal K,
$$

cover:

$$
B(c_\psi,AR)
$$

by cubes:

$$
Q_{k,a}
$$

of side:

$$
L\ell_k
$$

with bounded overlap, where:

$$
L
$$

is a fixed geometric constant.

The number of cells obeys:

$$
\boxed{
N_k
\le
C_L
\left(
1+A\Xi_k
\right)^3.
}
$$

---

# 5. Local cell energies

Choose a smooth partition of unity:

$$
\{
\zeta_{k,a}
\}_a
$$

subordinate to the wavelength-cell cover.

Define:

$$
\boxed{
E_{k,a}^\psi
=
\int
\zeta_{k,a}(x)
\psi(x)
|\omega_k(x)|^2dx.
}
$$

Let:

$$
\mathcal A_{ss}
=
\{
(k,a):
k\in\mathcal K
\}.
$$

---

# 6. Total geometric capacity

Let:

$$
\boxed{
W
=
|\mathcal K|.
}
$$

Let:

$$
\boxed{
\Xi_\ast
=
\max_{
k\in\mathcal K
}
\Xi_k.
}
$$

Define the geometric space--scale capacity:

$$
\boxed{
\operatorname{Cap}_{ss}
(
A,\mathcal K,\Xi_\ast
)
=
C_L
W
\left(
1+A\Xi_\ast
\right)^3.
}
$$

This is an upper bound for the number of wavelength-scale spatial cells across the selected shell band inside the recapture region.

---

# 7. CIV/V-2.1 — Strong Space–Scale Atom Theorem

## Theorem 7.1

Assume the weighted state is:

$$
(A,\varepsilon)\text{-tight}.
$$

Then there exists one:

$$
(k_\ast,a_\ast)
\in
\mathcal A_{ss}
$$

such that:

$$
\boxed{
\frac{
E_{k_\ast,a_\ast}^\psi
}{
E_{\mathcal K}^\psi
}
\ge
\frac{
1-\varepsilon
}{
\operatorname{Cap}_{ss}
}.
}
$$

### Proof

At least:

$$
(1-\varepsilon)
E_{\mathcal K}^\psi
$$

lies inside:

$$
B(c_\psi,AR).
$$

This mass is distributed among at most:

$$
\operatorname{Cap}_{ss}
$$

space--scale cells.

Apply the pigeonhole principle.

$\square$

---

# 8. Meaning of Theorem 7.1

A forest cannot erase all strong local carriers while keeping:

- shell width:
  $$
  W;
  $$
- scale span:
  $$
  \Xi_\ast;
  $$
- state tail:
  $$
  \varepsilon;
  $$

uniformly bounded.

If all cell shares tend to zero, at least one of those capacity coordinates must escape.

---

# 9. Space–scale atomization

Define normalized cell shares:

$$
\boxed{
p_{k,a}
=
\frac{
E_{k,a}^\psi
}{
\displaystyle
\sum_{
(k',a')
\in\mathcal A_{ss}^{in}
}
E_{k',a'}^\psi
},
}
$$

where:

$$
\mathcal A_{ss}^{in}
$$

contains cells inside the recapture region.

Define effective space--scale multiplicity:

$$
\boxed{
\mathfrak M_{ss}
=
\left(
\sum_{k,a}
p_{k,a}^2
\right)^{-1}.
}
$$

Define conditional space--scale entropy:

$$
\boxed{
\mathfrak H_{ss}
=
-
\sum_{k,a}
p_{k,a}
\log p_{k,a}.
}
$$

---

# 10. CIV/V-2.2 — Forest Capacity Ceiling

## Theorem 10.1

For an:

$$
(A,\varepsilon)\text{-tight}
$$

state:

$$
\boxed{
\mathfrak M_{ss}
\le
\operatorname{Cap}_{ss},
}
$$

and:

$$
\boxed{
\mathfrak H_{ss}
\le
\log
\operatorname{Cap}_{ss}.
}
$$

Moreover:

$$
\boxed{
p_{\max}
\ge
\operatorname{Cap}_{ss}^{-1}.
}
$$

for the conditional inside-state distribution.

$\square$

---

# 11. Atom-share collapse

If:

$$
p_{\max}\to0
$$

along a state-tight forest branch, then:

$$
\boxed{
\operatorname{Cap}_{ss}\to\infty.
}
$$

Thus at least one of:

$$
\boxed{
W\to\infty,
}
$$

$$
\boxed{
\Xi_\ast\to\infty,
}
$$

or:

$$
\boxed{
\varepsilon_{\rm st}\not\to0
}
$$

must occur.

This is the basic spatial--scale capacity escape.

---

# 12. Single-shell spatial capacity

For one shell:

$$
W=1.
$$

Then Theorem 7.1 gives:

$$
\boxed{
p_{\max}^{space}
\ge
c
\frac{
1-\varepsilon
}{
(1+A\Xi)^3
}.
}
$$

Therefore absence of a strong wavelength cell forces:

$$
\boxed{
\Xi\to\infty
}
$$

or state-tail escape.

This quantifies:

$$
D_{\rm SCALE}.
$$

---

# 13. Shell-span capacity

If:

$$
\Xi_\ast
$$

is bounded but:

$$
W\to\infty,
$$

the state/source forest is spectrally spread over an increasing number of shell labels.

For source-parent shell marginals, the prior DRC multiplicity/dissipation-span census applies.

For a purely local weighted state marginal, large:

$$
W
$$

is retained as spectral/profile fragmentation unless the global spectral hypotheses of the earlier approximate-eigen-shell criteria are verified.

No automatic state-side:

$$
D_{\rm eig}
$$

claim is made.

---

# 14. Spatial atomization is not spectral atomization

Translations of same-frequency wave packets may create arbitrarily many separated spatial atoms without significantly changing their common Fourier shell.

Therefore:

$$
\boxed{
\text{spatial multiplicity}
\not\Rightarrow
\text{spectral variance}.
}
$$

CFOP does not route:

$$
D_{\rm SATOM}
$$

directly to:

$$
D_{\rm eig}.
$$

---

# 15. Geometric sparseness guard

External geometric regularity work shows that sufficiently sparse super-level sets of intense Navier--Stokes activity can prevent finite-time singularity.

In particular, Grujić's geometric measure-type criterion uses local one-dimensional sparseness of intense super-level sets.

Bradshaw--Farhat--Grujić develop the related sparseness framework in the scaling-gap problem.

Define:

$$
\boxed{
G_{\rm SPARSE}
}
$$

to mean:

> the appropriate intense vorticity/velocity super-level set satisfies an established sparseness-at-analyticity-scale regularity criterion.

Then:

$$
\boxed{
G_{\rm SPARSE}
\Longrightarrow
\text{REGULARIZING BRANCH}
}
$$

as an EXTERNAL implication under the hypotheses of the corresponding theorem.

---

# 16. Sparseness safety

High space--scale multiplicity does not automatically imply:

$$
G_{\rm SPARSE}.
$$

Many cells can be arranged densely or anisotropically.

Therefore the forest branch is classified as:

$$
\boxed{
G_{\rm SPARSE}
\vee
G_{\rm SPARSE}^{fail}.
}
$$

The second branch remains in the forest-capacity census.

---

# 17. Contemporary geometric calibration

Recent specialized work by Grujić shows that for a class of critical-point singularity scenarios, logarithmic geometric depletion of vortex stretching can force super-level-set sparseness below the spatial analyticity scale and avert blow-up.

CFOP uses this as current calibration that geometry can convert extreme spatial complexity into a regularizing mechanism under additional structure.

It is not applied as a universal theorem to all CFOP forests.

---

# 18. Global wavelength-cell partition

For every shell:

$$
k,
$$

fix a global wavelength-scale partition of unity:

$$
\{
\zeta_{k,a}
\}_a
$$

with bounded overlap.

Define the global cell enstrophy:

$$
\boxed{
\mathcal E_{k,a}(t)
=
\int
\zeta_{k,a}(x)
|\omega_k(t,x)|^2dx.
}
$$

Then:

$$
\boxed{
\sum_a
\mathcal E_{k,a}(t)
=
\|\omega_k(t)\|_2^2.
}
$$

---

# 19. Global space–scale occupation

Define:

$$
\boxed{
\mathfrak O_{ss}(t)
=
\sum_{k,a}
\mathcal E_{k,a}(t).
}
$$

Littlewood--Paley square-function equivalence gives:

$$
\boxed{
\mathfrak O_{ss}(t)
\asymp
\|\omega(t)\|_2^2.
}
$$

---

# 20. CIV/V-2.3 — Finite Enstrophy Occupation Budget

## Theorem 20.1

For a finite-energy Leray--Hopf solution, and hence for every smooth pre-singularity segment:

$$
\boxed{
\nu
\int_0^{T_\ast}
\mathfrak O_{ss}(t)dt
\le
C
\|u_0\|_2^2.
}
$$

### Proof

Use:

$$
\mathfrak O_{ss}
\asymp
\|\omega\|_2^2
=
\|\nabla u\|_2^2
$$

for divergence-free velocity in:

$$
\mathbb R^3,
$$

and the Leray energy inequality.

$\square$

---

# 21. Why this budget matters

Unlike the nonlinear shell-forcing action:

$$
\int
\sum_k
\|F_k\|_2^2dt,
$$

the enstrophy-time occupation budget is genuinely finite for Leray--Hopf solutions.

Therefore propagated-state forest cutsets have access to a real global finite resource.

---

# 22. Space–scale localized dual loads

For an ensemble of dangerous terminals:

$$
\mathcal T
=
\{
T_r
\},
$$

with weights:

$$
w_r,
\qquad
\sum_rw_r=1,
$$

and normalized dual witnesses:

$$
\Psi_r(\tau)
=
\Phi_r(\tau)/A_r,
$$

define:

$$
\boxed{
b_{k,a}(\tau)
=
\sum_{
r:
k_r=k
}
w_r
\|
\zeta_{k,a}^{1/2}
\Psi_r(\tau)
\|_2.
}
$$

Define instantaneous spatial--scale dual congestion:

$$
\boxed{
\mathfrak C_{ss}(\tau)^2
=
\sum_{k,a}
b_{k,a}(\tau)^2.
}
$$

---

# 23. Localized propagated cut

The ensemble propagated fraction satisfies:

$$
\overline P(\tau)
\le
\sum_{k,a}
\|
\zeta_{k,a}^{1/2}
\omega_k(\tau)
\|_2
\,
b_{k,a}(\tau).
$$

Cauchy--Schwarz gives:

$$
\boxed{
\overline P(\tau)^2
\le
\mathfrak O_{ss}(\tau)
\,
\mathfrak C_{ss}(\tau)^2.
}
$$

---

# 24. CIV/V-2.4 — State–Congestion Duality

## Theorem 24.1

If:

$$
\boxed{
\overline P(\tau)
\ge
\rho>0,
}
$$

then:

$$
\boxed{
\mathfrak O_{ss}(\tau)
\,
\mathfrak C_{ss}(\tau)^2
\ge
\rho^2.
}
$$

Thus if:

$$
\mathfrak C_{ss}(\tau)^2
\le
K_0,
$$

$$
\boxed{
\|\omega(\tau)\|_2^2
\ge
c
\frac{
\rho^2
}{
K_0
}.
}
$$

$\square$

---

# 25. Propagated-cut time capacity

Let:

$$
J
\subset
(0,T_\ast)
$$

be a measurable set of cut times such that:

$$
\overline P(\tau)\ge\rho,
$$

and:

$$
\mathfrak C_{ss}(\tau)^2
\le K_0
$$

for:

$$
\tau\in J.
$$

Then Theorems 20.1 and 24.1 give:

$$
\boxed{
|J|
\le
C
\frac{
K_0
\|u_0\|_2^2
}{
\nu
\rho^2
}.
}
$$

This is a universal finite measure budget for low-congestion propagated-dominant forest cuts.

---

# 26. Meaning of the time-capacity theorem

An infinite set of propagated cuts is not excluded if its total time measure shrinks.

But a propagated diffuse forest cannot occupy an arbitrarily large amount of physical time with simultaneously:

- fixed propagated fraction;
- uniformly low spatial--scale congestion.

This is a genuine finite Navier--Stokes budget.

---

# 27. Localized source action

For the shell source:

$$
F_k,
$$

define:

$$
\boxed{
\mathfrak A_{F,ss}(I)
=
\int_I
\sum_{k,a}
\|
\zeta_{k,a}^{1/2}
F_k(s)
\|_2^2ds.
}
$$

Because:

$$
\sum_a\zeta_{k,a}=1,
$$

$$
\boxed{
\mathfrak A_{F,ss}(I)
=
\int_I
\sum_k
\|F_k(s)\|_2^2ds.
}
$$

---

# 28. Localized source congestion

Define:

$$
\boxed{
\mathfrak K_{C,ss}(I)
=
\int_I
\sum_{k,a}
b_{k,a}(s)^2ds.
}
$$

The CFOP-01 argument localizes cell-by-cell.

---

# 29. CIV/V-2.5 — Spatial–Scale Action–Congestion Duality

## Theorem 29.1

If an ensemble cut across:

$$
I=[\tau,t_{\max}]
$$

satisfies:

$$
\overline P(\tau)
\le
1-\sigma,
$$

then:

$$
\boxed{
\mathfrak A_{F,ss}(I)
\,
\mathfrak K_{C,ss}(I)
\ge
\sigma^2.
}
$$

### Proof

Partition each shell pairing using:

$$
\sum_a\zeta_{k,a}=1.
$$

Apply spatial cell Cauchy--Schwarz, then shell Cauchy--Schwarz and finally time Cauchy--Schwarz.

$\square$

---

# 30. Effective dual space–scale capacity

Define total instantaneous dual load:

$$
\boxed{
L_{ss}(s)
=
\sum_{k,a}
b_{k,a}(s).
}
$$

When:

$$
L_{ss}(s)>0,
$$

define:

$$
\boxed{
\mathfrak N_{ss}^{dual}(s)
=
\frac{
L_{ss}(s)^2
}{
\displaystyle
\sum_{k,a}
b_{k,a}(s)^2
}.
}
$$

This is the effective number of space--scale cells occupied by normalized dual load.

---

# 31. Congestion–capacity identity

By definition:

$$
\boxed{
\mathfrak C_{ss}(s)^2
=
\frac{
L_{ss}(s)^2
}{
\mathfrak N_{ss}^{dual}(s)
}.
}
$$

Thus higher effective forest capacity lowers congestion when total dual load is held fixed.

---

# 32. CIV/V-2.6 — Diffuse-Capacity Action Rigidity

## Theorem 32.1

Suppose on a source-dominated cut interval:

$$
I,
$$

one has:

$$
L_{ss}(s)
\le
L_0,
$$

and:

$$
\mathfrak N_{ss}^{dual}(s)
\ge
N_0
$$

for almost every:

$$
s\in I.
$$

Then:

$$
\boxed{
\mathfrak K_{C,ss}(I)
\le
\frac{
L_0^2
|I|
}{
N_0
}.
}
$$

Consequently:

$$
\boxed{
\mathfrak A_{F,ss}(I)
\ge
\frac{
\sigma^2
N_0
}{
L_0^2
|I|
}.
}
$$

### Meaning

If the forest reduces congestion by spreading causal dual load over more space--scale cells, it must pay proportionally larger nonlinear forcing action per cut duration.

$\square$

---

# 33. Diffuse-capacity cascade

For pairwise disjoint source-dominated cut intervals:

$$
I_n,
$$

with:

$$
L_{ss,n}\le L_0,
$$

and:

$$
\mathfrak N_{ss,n}^{dual}\ge N_n,
$$

Theorem 32.1 gives:

$$
\boxed{
\sum_{n=1}^{N}
\mathfrak A_{F,ss}(I_n)
\ge
\frac{
\sigma^2
}{
L_0^2
}
\sum_{n=1}^{N}
\frac{
N_n
}{
|I_n|
}.
}
$$

Thus increasing diffuse capacity and shrinking horizon windows amplify each other.

No finite total forcing-action budget is currently available to turn this into an unconditional contradiction.

---

# 34. Space–scale forest capacity function

Define:

$$
\boxed{
\mathfrak C_{\rm forest}
=
\operatorname{Cap}_{ss}
\cdot
\mathfrak N_{ss}^{dual}
}
$$

as a diagnostic combined capacity.

The first factor counts available geometric state cells.

The second measures actual effective dual-load dispersion.

This is not a conserved quantity.

It is a capacity diagnostic for the forest.

---

# 35. Strong-cell / capacity-escape trichotomy

For a state-tight shell band and a target atom share:

$$
\eta_0>0,
$$

Theorem 7.1 implies:

$$
\boxed{
\text{STRONG SPACE--SCALE ATOM}
\vee
\text{STATE-TAIL ESCAPE}
\vee
\text{CAPACITY GROWTH}.
}
$$

Where:

### STRONG SPACE--SCALE ATOM

$$
p_{\max}\ge\eta_0.
$$

### STATE-TAIL ESCAPE

$$
\varepsilon_{\rm st}
$$

fails the chosen tightness threshold.

### CAPACITY GROWTH

$$
W(1+\Xi_\ast)^3
\gtrsim
\eta_0^{-1}.
$$

---

# 36. Capacity growth decomposition

Capacity growth splits into:

$$
\boxed{
\text{SHELL-SPAN}
\vee
\text{SPATIAL-SPAN}.
}
$$

### SHELL-SPAN

$$
W\to\infty.
$$

For source-parent shell labels this reconnects to DRC multiplicity/dissipation-span/driver routing.

### SPATIAL-SPAN

$$
\Xi\to\infty.
$$

This is the forest spatial fragmentation branch.

---

# 37. Spatial-span branch

On a weighted-state-tight spatial-span branch:

$$
\Xi\to\infty,
$$

partition the recapture ball into wavelength cells.

Either:

### STRONG-CELL

A wavelength cell carries a fixed state share.

Or:

### $D_{\rm SATOM}$

The maximum wavelength-cell share tends to zero.

By Theorem 7.1:

$$
D_{\rm SATOM}
$$

requires growing geometric capacity.

---

# 38. Sparseness interface

If:

$$
D_{\rm SATOM}
$$

is realized by super-level sets satisfying:

$$
G_{\rm SPARSE},
$$

the corresponding external geometric regularity criterion blocks the singular branch.

If not, the forest remains in:

$$
\boxed{
D_{\rm SATOM}^{nonsparse}.
}
$$

CFOP does not prove that every high-capacity atomized configuration becomes sparse at the analyticity scale.

---

# 39. Driver-action interface

A source-dominated forest cut may be split according to the DRC dissipation wavenumber:

- deep dissipative source;
- transition source;
- low-mode-driver-backed source.

Deep dissipative source is viscosity-small in the prior DRC architecture.

A dangerous non-absorbed source cut is therefore routed toward transition/driver action or source multiplicity.

Thus large shell capacity is not retained as a new mechanism when the DRC hypotheses apply.

---

# 40. Contemporary geometric regularity calibration

Grujić's geometric measure-type theorem gives a regularity mechanism based on local one-dimensional sparseness of intense super-level sets.

Bradshaw--Farhat--Grujić develop a sparseness-class framework reducing the scaling gap.

Recent 2026 work of Grujić gives a specialized critical-point mechanism in which logarithmic geometric depletion drives the sparseness scale below the analyticity radius and prevents blow-up.

These results justify retaining:

$$
\boxed{
\text{SPARSE-REGULARIZING}
}
$$

as a serious forest branch rather than treating all spatial fragmentation as dangerous.

---

# 41. Forest cut capacity theorem

## Theorem 41.1

For every dangerous forest cut, at least one of the following mechanisms is present:

1. **PROPAGATED / LOW-CONGESTION**  
   consumes the finite enstrophy-time occupation budget;

2. **PROPAGATED / HIGH-CONGESTION**  
   pays forest dual congestion;

3. **SOURCE / LOW-CONGESTION**  
   pays nonlinear forcing action by Theorem 29.1;

4. **SOURCE / HIGH-CONGESTION**  
   pays forest dual congestion;

5. **SPACE--SCALE ATOMIZATION**  
   produces a strong atom or forces capacity growth/state-tail escape;

6. **SPARSE-GEOMETRIC BRANCH**  
   enters an external regularizing guard when the required sparseness/analyticity hypotheses hold.

### Status

This is a complete accounting theorem relative to the defined cut coordinates.

It is not a finite obstruction theorem because forcing action, congestion, and non-sparse capacity growth are not universally bounded.

$\square$

---

# 42. What is genuinely finite?

The following global quantity is universally finite:

$$
\boxed{
\nu
\int_0^{T_\ast}
\|\omega(t)\|_2^2dt
\le
\frac12
\|u_0\|_2^2.
}
$$

Thus propagated-state occupation has a hard global budget.

The following are **not** presently known to have a finite universal budget under hypothetical blow-up:

$$
\boxed{
\int
\sum_k
\|F_k\|_2^2dt,
}
$$

forest dual congestion,

source entropy,

and non-sparse spatial--scale capacity.

This asymmetry is the present Forest Obstruction frontier.

---

# 43. Conditional finite-capacity obstruction

Suppose a hypothetical horizon forest satisfies all of:

1. low-congestion propagated cuts occupy a time set of positive lower total measure at infinitely many generations;
2. source-dominated cuts have a finite total shell-forcing action;
3. dual congestion is uniformly bounded;
4. state/source space--scale capacity is uniformly bounded;
5. sparse geometric regularity guards fail only finitely often.

Then the forest cannot remain horizon-unbounded.

### Status

This is a conditional obstruction assembled from Theorems 20.1, 25, 29.1, and 7.1.

The assumptions are not established universally.

---

# 44. Updated forest residual

After CFOP-02, the diffuse forest residual can be organized as:

$$
\boxed{
\mathfrak R_{\rm Forest}^{(2)}
=
R_{F\mbox{-}ACT}
\vee
R_{F\mbox{-}CONG}
\vee
R_{F\mbox{-}CAP}
\vee
R_{F\mbox{-}TAIL}
\vee
R_{F\mbox{-}NSPARSE}.
}
$$

Where:

### $R_{F\mbox{-}ACT}$

unbounded fresh/source action;

### $R_{F\mbox{-}CONG}$

unbounded dual/branch congestion;

### $R_{F\mbox{-}CAP}$

unbounded shell/spatial capacity;

### $R_{F\mbox{-}TAIL}$

weighted state escapes every controlled recapture region;

### $R_{F\mbox{-}NSPARSE}$

spatial fragmentation persists without entering the known sparseness regularity guard.

---

# 45. Next paper

The next paper should test whether this residual can be compressed to a finite obstruction ledger:

$$
\boxed{
\textbf{
NS-CFOP 03 —
Finite Forest Obstruction,
Cutset Budget Closure,
Sparse/Dense Geometry Audit
and Cycle-V Closure
}.
}
$$

Primary tasks:

1. search for standard PDE quantities that can globally bound:
   $$
   R_{F\mbox{-}ACT};
   $$
2. determine whether:
   $$
   R_{F\mbox{-}CONG}
   $$
   can be converted into multiplicity/energy cost;
3. combine:
   $$
   R_{F\mbox{-}CAP}
   $$
   with the sparseness/analyticity guard;
4. test whether state-tail escape has an absolute local-core recapture theorem;
5. decide whether any finite universal forest obstruction is actually available.

---

# 46. Formal status ledger

$$
\boxed{
\begin{aligned}
\text{space--scale geometric capacity}
&:\ \mathrm{DEFINED},\\
\text{strong space--scale atom theorem}
&:\ \mathrm{PROVED},\\
\text{capacity multiplicity/entropy ceiling}
&:\ \mathrm{PROVED},\\
\text{spatial atomization}\not\Rightarrow D_{\rm eig}
&:\ \mathrm{NO\mbox{-}GO/SEMANTIC},\\
G_{\rm SPARSE}
&:\ \mathrm{EXTERNAL\ REGULARIZING\ GUARD},\\
\text{finite enstrophy occupation budget}
&:\ \mathrm{PROVED/CLASSICAL},\\
\text{State--Congestion Duality}
&:\ \mathrm{PROVED},\\
\text{propagated-cut time-capacity bound}
&:\ \mathrm{PROVED},\\
\text{spatial--scale Action--Congestion Duality}
&:\ \mathrm{PROVED},\\
\text{Diffuse-Capacity Action Rigidity}
&:\ \mathrm{PROVED\ CONDITIONAL\ ON\ LOAD/CAPACITY\ BOUNDS},\\
\text{Forest Cut Capacity accounting}
&:\ \mathrm{PROVED},\\
\text{complete Forest Finite Obstruction}
&:\ \mathrm{OPEN},\\
D_{\rm DIFF}\text{ exclusion}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 47. Conclusion

CFOP-02 makes spatial and scale fragmentation quantitative.

A state that remains tight in:

$$
W
$$

shells and a footprint of span:

$$
\Xi
$$

has only:

$$
O(
W(1+\Xi)^3
)
$$

available wavelength-scale cells.

Therefore it must contain a strong space--scale atom of size at least:

$$
\boxed{
c
\frac{
1-\varepsilon
}{
W(1+\Xi)^3
}.
}
$$

If no such atom survives, capacity must diverge or state mass must escape.

At the forest level, localized dual congestion yields two complementary cutset inequalities.

For propagated flow:

$$
\boxed{
\overline P^2
\le
\mathfrak O_{ss}
\mathfrak C_{ss}^2.
}
$$

This directly consumes the finite Leray enstrophy-time budget when congestion is bounded.

For fresh source flow:

$$
\boxed{
\mathfrak A_{F,ss}
\mathfrak K_{C,ss}
\ge
\sigma^2.
}
$$

If causal dual load is spread over more effective cells, congestion falls and required forcing action rises.

Thus diffuse horizon causality cannot fragment for free.

It must pay in:

- finite enstrophy occupation;
- nonlinear source action;
- dual congestion;
- space--scale capacity;
- state-tail escape;
- or a non-sparse geometric branch.

When fragmentation becomes sufficiently sparse at the analyticity scale, established geometric regularity criteria can themselves block the singular scenario.

The remaining question is whether the non-sparse/action/congestion/capacity branches admit a finite universal PDE budget.

That is CFOP-03.

---

# References

1. Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier--Stokes equations*, arXiv:1111.0217.
2. Z. Bradshaw, A. Farhat, Z. Grujić, *An algebraic reduction of the `scaling gap' in the Navier--Stokes regularity problem*, arXiv:1704.05546.
3. R. Dascaliuc, Z. Grujić, *Energy cascades and flux locality in physical scales of the 3D Navier--Stokes equations*, arXiv:1101.2193.
4. H. Aluie, G. L. Eyink, *Localness of energy cascade in hydrodynamic turbulence, II. Sharp spectral filter*, arXiv:0909.2451.
5. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.
6. Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier--Stokes Equations*, arXiv:2607.08866.
7. `NS_CFOP_01_DiffuseHorizon_ForestCutsets_v0.1.md`.
8. `NS_ANP_09_ScaleFragmentation_InverseLimits_CN3FinalAudit_v0.1.md`.