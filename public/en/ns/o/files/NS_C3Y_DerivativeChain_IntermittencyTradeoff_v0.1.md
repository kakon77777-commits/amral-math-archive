---
title: "Navier–Stokes C3-Y: Derivative-Chain / Intermittency Tradeoff, Direct-vs-Chain Gap Closure, and Joint-Concentration Routing"
subtitle: "A Quantitative Tradeoff Between Derivative-Chain Dynamics and Uniform-Local Intermittency, with Direct and Chain-Assisted Geometric Closure Thresholds"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / conditional regularity interface"
epistemic_status: "Exact algebraic scale bridge + direct application templates for published geometric regularity theorems, under their full hypotheses. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-Y
# Derivative-Chain / Intermittency Tradeoff, Direct-vs-Chain Gap Closure, and Joint-Concentration Routing

## 0. Source audit correction

In this iteration, we realign with the primary source:

Z. Grujić and L. Xu,

*Asymptotic Criticality of the Navier–Stokes Regularity Problem*,

Journal of Mathematical Fluid Mechanics 26, Article 53 (2024).

Official version of record:

$$
\boxed{
2024\text{-}07\text{-}27.
}
$$

Therefore, all theorem numbering in this iteration is based on the 2024 journal version.

Main external interfaces:

- Theorem 3.5 — direct geometric regularity criterion at a fixed derivative level;
- Theorem 3.7 — energy-level a-priori volumetric sparseness;
- Theorem 3.8 — ascending derivative chain;
- Theorem 3.9 — descending derivative chain;
- Theorem 3.14 — derivative-chain-assisted asymptotic-criticality regularity theorem.

For C3-X's:

$$
\boxed{
\phi_2\lesssim A_2^{-1/7}
}
$$

its positioning is now formally corrected:

It is:

$$
\boxed{
\textbf{chain-assisted scale-gap closure exponent at }k=2,
}
$$

not a standalone $k=2$ regularity theorem.

---

# 1. Normalization

In this iteration, the external theorem section adopts:

$$
\boxed{
\nu=1,
}
$$

consistent with the Grujić–Xu paper.

In general,

$$
\nu>0
$$

can be recovered in nondimensional variables.

Let:

$$
\boxed{
A_k(s)
=
\|D^ku(s)\|_\infty.
}
$$

---

# 2. Three level-$k$ scales

For the velocity derivative level:

$$
k,
$$

there exist three distinct scales.

---

## 2.1 Energy a-priori scale

Theorem 3.7 gives in three dimensions:

$$
\boxed{
R_{\rm apr}^{(k)}
=
C_{\rm apr}(u_0,k)
A_k^{-1/(k+3/2)}.
}
$$

Its scaling exponent is:

$$
\boxed{
a_{\rm apr}(k)
=
\frac1{k+3/2}.
}
$$

The size constant in the actual theorem is primarily determined by fixed data such as:

$$
\|u_0\|_2.
$$

---

## 2.2 Direct finite-$k$ regularity scale

Theorem 3.5 requires the component/sign superlevel set to possess local 1D sparseness at an admissible scale of the order of or smaller than:

$$
\boxed{
R_{\rm dir}^{(k)}
=
C_{\rm dir}(k,M,u_0)
A_k^{-\,\frac{3/2}{k+3/2}}.
}
$$

Its exponent is:

$$
\boxed{
a_{\rm dir}(k)
=
\frac{
3/2
}{
k+3/2
}.
}
$$

---

## 2.3 Chain-assisted regularity scale

Theorem 3.14 improves the target to the following, provided that level $k$ lies in an admissible ascending chain and the time/constant hypotheses hold:

$$
\boxed{
R_{\rm chain}^{(k)}
=
C_{\rm chain}(\ell,k,u_0)
A_k^{-1/(k+1)}.
}
$$

Its exponent is:

$$
\boxed{
a_{\rm chain}(k)
=
\frac1{k+1}.
}
$$

---

# 3. Scale ordering

For:

$$
k>0,
$$

we have:

$$
a_{\rm apr}
<
a_{\rm chain}
<
a_{\rm dir}.
$$

Thus, when:

$$
A_k\gg1,
$$

$$
\boxed{
R_{\rm dir}^{(k)}
<
R_{\rm chain}^{(k)}
<
R_{\rm apr}^{(k)}
}
$$

up to size constants.

Therefore:

- the energy a-priori bound only guarantees sparseness at a coarser scale;
- the direct finite-$k$ theorem requires the finest scale;
- derivative-chain dynamics pulls the required scale back to an intermediate level.

---

# 4. C3-Y.1: Two Scaling Gaps

Define:

$$
\boxed{
\Delta a_{\rm dir}
=
a_{\rm dir}
-
a_{\rm apr},
}
$$

$$
\boxed{
\Delta a_{\rm chain}
=
a_{\rm chain}
-
a_{\rm apr}.
}
$$

Direct calculation yields:

$$
\boxed{
\Delta a_{\rm dir}
=
\frac{
1
}{
2(k+3/2)
}.
}
$$

and:

$$
\boxed{
\Delta a_{\rm chain}
=
\frac{
1
}{
2(k+1)(k+3/2)
}.
}
$$

Thus:

$$
\boxed{
\frac{
\Delta a_{\rm dir}
}{
\Delta a_{\rm chain}
}
=
k+1.
}
$$

This is the first core identity of this iteration.

---

# 5. Uniform-local intermittency

C3-W/X utilized the ancestry-local effective volume.

To genuinely plug into the Grujić–Xu theorem,

a stronger uniformly-local condition is required.

Fix:

$$
0<c<1.
$$

Let the magnitude high set be:

$$
\boxed{
\Omega_{k,c}(s)
=
\left\{
x:
|D^ku(x,s)|
>
cA_k(s)
\right\}.
}
$$

For scale:

$$
R,
$$

define:

$$
\boxed{
\Phi_{k,c}(s;R)
=
\sup_{x_0\in\mathbb R^3}
\frac{
|\Omega_{k,c}(s)\cap B_R(x_0)|
}{
|B_R|
}.
}
$$

This is a:

$$
\boxed{
\textbf{uniform-local active-volume factor}.
}
$$

---

# 6. Component/sign interface

The Grujić–Xu geometric criteria use:

$$
\boxed{
S_{k,\lambda}^{i,\pm}
=
\left\{
x:
(D^ku)_i^\pm(x)
>
\lambda A_k
\right\}.
}
$$

If:

$$
\boxed{
c\le\lambda,
}
$$

then:

$$
\boxed{
S_{k,\lambda}^{i,\pm}
\subset
\Omega_{k,c}.
}
$$

Therefore, any uniform-local volume bound on:

$$
\Omega_{k,c}
$$

automatically transfers to all component/sign theorem sets.

This resolves the first layer of the component/sign threshold interface.

---

# 7. Volume-to-line transfer

By the volume-to-one-dimensional-sparseness lemma from C3-W:

If for every:

$$
x_0,
$$

$$
|\Omega_{k,c}\cap B_R(x_0)|
\le
\Phi
|B_R|,
$$

then fixing the theorem-required:

$$
\delta\in(0,1)
$$

,

there exists:

$$
C_\delta>0
$$

such that at every spatial point:

$$
x_0
$$

one can find a direction,

making:

$$
S_{k,\lambda}^{i,\pm}
$$

1D $\delta$-sparse at scale:

$$
\boxed{
r_{\rm vol}
=
C_\delta
\Phi^{1/3}
R
}
$$

provided:

$$
r_{\rm vol}\le R.
$$

---

# 8. Direct finite-$k$ volume bridge

Now let:

$$
R
=
R_{\rm apr}^{(k)}
=
C_{\rm apr}
A_k^{-a_{\rm apr}}.
$$

To ensure:

$$
r_{\rm vol}
\le
R_{\rm dir}^{(k)}
=
C_{\rm dir}
A_k^{-a_{\rm dir}},
$$

it suffices to require:

$$
C_\delta
\Phi^{1/3}
C_{\rm apr}
A_k^{-a_{\rm apr}}
\le
C_{\rm dir}
A_k^{-a_{\rm dir}}.
$$

Therefore:

$$
\boxed{
\Phi
\le
C_k^{\rm dir}
A_k^{-\theta_k^{\rm dir}},
}
$$

where:

$$
\boxed{
\theta_k^{\rm dir}
=
3
\Delta a_{\rm dir}
=
\frac{
3
}{
2(k+3/2)
}.
}
$$

and:

$$
\boxed{
C_k^{\rm dir}
=
\left(
\frac{
C_{\rm dir}
}{
C_\delta C_{\rm apr}
}
\right)^3.
}
$$

---

# 9. C3-Y.2: Direct Intermittency Bridge Theorem

## Theorem 9.1 (conditional application template)

Fix the derivative level:

$$
k.
$$

Assume all hypotheses of Grujić–Xu Theorem 3.5 hold, including:

1. $t$ is the escape time of:
   $$
   D^ku
   $$

2. There exists a theorem-specified later time:
   $$
   s=s(t);
   $$

3. $u_0\in L^\infty\cap L^2$;

4. The threshold pair:
   $$
   (\lambda,\delta)
   $$
   satisfies its harmonic-measure conditions.

If at this:

$$
s
$$

we have:

$$
\boxed{
\Phi_{k,c}
\left(
s;
R_{\rm apr}^{(k)}(s)
\right)
\le
C_k^{\rm dir}
A_k(s)^{
-\frac{
3
}{
2(k+3/2)
}
}
}
$$

for some:

$$
c\le\lambda,
$$

then the volume-to-line lemma provides the component/sign 1D sparseness scale required by Theorem 3.5,

hence:

$$
\boxed{
T_\ast
\text{ is not a singular time}.
}
$$

### Status

This is a:

$$
\boxed{
\textbf{genuine finite-}k\textbf{ conditional regularity bridge}.
}
$$

It does not require the derivative-chain hypothesis.

---

# 10. Chain-assisted volume bridge

If we instead use the Theorem 3.14 target:

$$
r_{\rm vol}
\le
R_{\rm chain}^{(k)},
$$

then it suffices to have:

$$
\boxed{
\Phi
\le
C_{\ell,k}^{\rm chain}
A_k^{-\theta_k^{\rm chain}},
}
$$

where:

$$
\boxed{
\theta_k^{\rm chain}
=
3
\Delta a_{\rm chain}
=
\frac{
3
}{
2(k+1)(k+3/2)
}.
}
$$

---

# 11. C3-Y.3: Chain-Assisted Intermittency Bridge

## Theorem 11.1 (conditional application template)

Fix:

$$
\ell\le k.
$$

Assume all hypotheses of Grujić–Xu Theorem 3.14 hold, including:

1. data / constant condition;
2. level-$k$ temporal point:
   $$
   t
   $$
   satisfies the ascending-chain condition:
   $$
   \boxed{
   \frac{
   \|D^ju(t)\|_\infty^{1/(j+1)}
   }{
   c^{j/(j+1)}
   (j!)^{1/(j+1)}
   }
   \le
   \frac{
   \|D^ku(t)\|_\infty^{1/(k+1)}
   }{
   c^{k/(k+1)}
   (k!)^{1/(k+1)}
   },
   \quad
   \ell\le j\le k;
   }
   $$

3. theorem time-window condition;
4. theorem later slice:
   $$
   s=s(t);
   $$

5. harmonic-measure tuning conditions.

If:

$$
\boxed{
\Phi_{k,c}
\left(
s;
R_{\rm apr}^{(k)}(s)
\right)
\le
C_{\ell,k}^{\rm chain}
A_k(s)^{
-\frac{
3
}{
2(k+1)(k+3/2)
}
}
}
$$

for:

$$
c\le\lambda,
$$

then the volume-induced one-dimensional sparseness reaches the chain-assisted regularity scale of Theorem 3.14,

thus:

$$
\boxed{
T_\ast
\text{ is not a singular time}.
}
$$

---

# 12. C3-Y.4: Derivative-Chain / Intermittency Tradeoff Identity

The volume exponent required for the direct route is:

$$
\theta_k^{\rm dir}
=
\frac{
3
}{
2(k+3/2)
},
$$

and for the chain-assisted route:

$$
\theta_k^{\rm chain}
=
\frac{
3
}{
2(k+1)(k+3/2)
}.
$$

Therefore:

$$
\boxed{
\frac{
\theta_k^{\rm dir}
}{
\theta_k^{\rm chain}
}
=
k+1.
}
$$

That is:

> **Derivative-chain dynamics precisely reduces the power-law exponent burden required for spatial intermittency by a factor of $k+1$.**

This is the primary new structural result of this iteration.

---

# 13. Threshold gain

The ratio of the power-law parts of the two volume thresholds is:

$$
\frac{
A_k^{-\theta_k^{\rm chain}}
}{
A_k^{-\theta_k^{\rm dir}}
}
=
A_k^{
\theta_k^{\rm dir}
-
\theta_k^{\rm chain}
}.
$$

And:

$$
\boxed{
\theta_k^{\rm dir}
-
\theta_k^{\rm chain}
=
\frac{
3k
}{
2(k+1)(k+3/2)
}.
}
$$

Thus:

$$
\boxed{
\text{chain dynamics allows a significantly larger active-volume fraction}.
}
$$

---

# 14. Large-$k$ asymptotics

direct:

$$
\boxed{
\theta_k^{\rm dir}
\sim
\frac{
3
}{
2k
}.
}
$$

chain:

$$
\boxed{
\theta_k^{\rm chain}
\sim
\frac{
3
}{
2k^2
}.
}
$$

Thus:

$$
\boxed{
\text{direct finite-}k\text{ gap is }O(k^{-1}),
}
$$

while:

$$
\boxed{
\text{chain-assisted residual gap is }O(k^{-2}).
}
$$

This precisely quantifies the additional contribution of derivative-chain dynamics to asymptotic criticality.

---

# 15. $k=2$: Formal correction

For:

$$
k=2,
$$

the a-priori scale exponent is:

$$
\boxed{
a_{\rm apr}
=
\frac2{7}.
}
$$

direct scale:

$$
\boxed{
a_{\rm dir}
=
\frac3{7}.
}
$$

chain scale:

$$
\boxed{
a_{\rm chain}
=
\frac13.
}
$$

Thus:

$$
\boxed{
R_{\rm dir}
\sim
A_2^{-3/7},
\qquad
R_{\rm chain}
\sim
A_2^{-1/3},
\qquad
R_{\rm apr}
\sim
A_2^{-2/7}.
}
$$

---

# 16. $k=2$ direct volume threshold

direct scale gap:

$$
\frac37-\frac27
=
\frac17.
$$

Since the active-volume gives a scale factor:

$$
\Phi^{1/3},
$$

we require:

$$
\boxed{
\Phi_2
\lesssim
A_2^{-3/7}.
}
$$

Therefore, the true standalone finite-$k=2$ volume bridge exponent is:

$$
\boxed{
\theta_2^{\rm dir}
=
\frac37.
}
$$

---

# 17. $k=2$ chain-assisted threshold

chain scale gap:

$$
\frac13-\frac27
=
\frac1{21}.
$$

Therefore:

$$
\boxed{
\Phi_2
\lesssim
A_2^{-1/7}.
}
$$

That is:

$$
\boxed{
\theta_2^{\rm chain}
=
\frac17.
}
$$

However:

## Critical caveat

The chain machinery of Grujić–Xu Theorem 3.14 requires:

- a sufficiently high derivative baseline:
  $$
  \ell;
  $$
- the derivative-chain condition;
- theorem constants / time gates.

Thus:

$$
\boxed{
\Phi_2\lesssim A_2^{-1/7}
}
$$

cannot generally be treated as a standalone $k=2$ theorem application.

It is a:

$$
\boxed{
\textbf{formal level-2 chain-assisted exponent}
}
$$

and a:

$$
\boxed{
\textbf{scale diagnostic}.
}
$$

Unless the particular solution/data truly satisfies all hypotheses required by the theorem, such as:

$$
\ell\le2
$$

---

# 18. Direct-vs-chain $k=2$ gain

power-law burden:

$$
\boxed{
\frac37
\quad\longrightarrow\quad
\frac17.
}
$$

exact ratio:

$$
\boxed{
3.
}
$$

That is:

$$
k+1=3.
$$

This is the specific version of the general tradeoff identity at:

$$
k=2
$$

---

# 19. The local-to-global barrier

The original:

$$
\phi_{p,R}
$$

in C3-W/X is:

$$
\boxed{
\text{the local effective-volume factor of one ancestry core}.
}
$$

But Theorem 3.5 / 3.14 requires that:

$$
\boxed{
\text{for every spatial point }x_0
}
$$

possesses 1D sparseness of the selected component/sign superlevel set.

Thus:

## No-Go 19.1

$$
\boxed{
\phi_{p,R}(x_{\rm ancestry})\ll1
}
$$

does not imply:

$$
\boxed{
\Phi_{k,c}\ll1.
}
$$

Therefore, strong intermittency of a single ancestry core cannot directly trigger the global geometric regularity theorem.

---

# 20. Uniform-local enhancement is the correct theorem-ready quantity

Therefore, the derivative/intermittency bridge truly needs to track:

$$
\boxed{
\Phi_{k,c}(s;R_{\rm apr})
}
$$

rather than just tracking:

$$
\boxed{
\phi_{p,R}(x_n).
}
$$

This is the:

$$
\boxed{
\textbf{Local Ancestry / Global Criterion Separation}.
}
$$

---

# 21. Possible globalization routes

To upgrade from the ancestry-local:

$$
\phi
$$

to:

$$
\Phi,
$$

there are at least three possible routes:

## Y-G1 — Single dominant active cluster

Prove that the selected derivative superlevel set is entirely supported by the ancestry pressure/nonlinear cluster.

## Y-G2 — Multi-core cover

Use C3-R multi-core cores to cover all selected superlevel regions,

and control the active-volume fraction ball by ball.

## Y-G3 — Localized geometric theorem

Establish a localized harmonic-measure regularity theorem that only requires sparseness within the singular candidate neighborhood.

Currently, all three remain incomplete.

---

# 22. Component/sign threshold matching

The uniform magnitude set:

$$
\Omega_{k,c}
$$

can serve as a safe parent set.

If:

$$
c\le\lambda,
$$

then all:

$$
S_{k,\lambda}^{i,\pm}
$$

are subsets of it.

Thus:

$$
\boxed{
\text{magnitude active-volume control}
\Rightarrow
\text{component/sign volume control}.
}
$$

However, the external theorem also requires:

- selecting a locally dominating component/sign at each $x_0$;
- a fixed tuning pair:
  $$
  (\lambda,\delta);
  $$
- a matching 1D sparsity ratio.

These must be preserved.

---

# 23. Temporal gate

The direct Theorem 3.5 is not a same-time criterion.

It requires:

- an escape time:
  $$
  t;
  $$
- a later time:
  $$
  s=s(t)
  $$
  falling within a specified analytic window.

Schematically:

$$
\boxed{
s-t
\asymp
A_k(t)^{
-\frac{
3
}{
k+3/2
}
}.
}
$$

For the chain theorem:

$$
\boxed{
s-t
\asymp
A_k(t)^{
-\frac{
2
}{
k+1
}
}.
}
$$

Thus:

$$
\boxed{
\text{intermittency at arbitrary time}
}
$$

is insufficient.

It must appear at a theorem-admissible later slice.

---

# 24. Time-gate no-go

Even if:

$$
\Phi_k(t)
$$

is very small at the escape time,

it does not mean that:

$$
\Phi_k(s(t))
$$

remains small at the required later analytic slice.

Thus:

$$
\boxed{
\text{spatial gap closure}
}
$$

and:

$$
\boxed{
\text{temporal gate closure}
}
$$

are two distinct proof obligations.

---

# 25. Direct closure load

Putting the constants back in.

Define:

$$
\boxed{
\mathfrak L_k^{\rm dir}
=
\frac{
\Phi_{k,c}(s;R_{\rm apr})
}{
C_k^{\rm dir}
A_k(s)^{-\theta_k^{\rm dir}}
}.
}
$$

Then:

$$
\boxed{
\mathfrak L_k^{\rm dir}\le1
}
$$

+ Theorem 3.5 full time/component hypotheses

$$
\Longrightarrow
$$

regularity extension.

---

# 26. Chain closure load

Define:

$$
\boxed{
\mathfrak L_{\ell,k}^{\rm chain}
=
\frac{
\Phi_{k,c}(s;R_{\rm apr})
}{
C_{\ell,k}^{\rm chain}
A_k(s)^{-\theta_k^{\rm chain}}
}.
}
$$

If:

$$
\boxed{
\mathfrak L_{\ell,k}^{\rm chain}\le1
}
$$

plus:

- ascending-chain condition;
- time gate;
- theorem constant conditions;

then Theorem 3.14 provides closure.

---

# 27. Adaptive derivative routing

For each candidate derivative level:

$$
k,
$$

one can compute:

- the direct load;
- the chain load (if the chain gate is open).

Define the formal routing score:

$$
\boxed{
\mathfrak L_k^{best}
=
\min
\left\{
\mathfrak L_k^{dir},
\ 
\mathfrak L_{\ell,k}^{chain}
\text{ if admissible}
\right\}.
}
$$

If there exists a theorem-admissible:

$$
k
$$

such that:

$$
\mathfrak L_k^{best}\le1,
$$

then the regularity route closes.

Therefore, a hypothetical singularity must have:

$$
\boxed{
\mathfrak L_k^{best}>1
}
$$

for all admissible derivative gates,

or it must break their time/chain/globality interface.

---

# 28. Derivative-chain dynamics as intermittency substitute

The tradeoff identity:

$$
\theta_k^{dir}
=
(k+1)
\theta_k^{chain}
$$

can be read as:

$$
\boxed{
\text{dynamical derivative ordering}
}
$$

substitutes for a portion of:

$$
\boxed{
\text{spatial active-volume collapse}.
}
$$

Thus, the regularity gap can be jointly reduced by two resources:

1. chain dynamics;
2. spatial intermittency.

This is the:

$$
\boxed{
\textbf{Derivative–Intermittency Dual Routing}.
}
$$

---

# 29. Comparison with C3-X two-axis picture

C3-X previously proposed:

- derivative order:
  $$
  k\uparrow;
  $$
- active volume:
  $$
  \phi\downarrow.
  $$

C3-Y now adds a third axis:

$$
\boxed{
\text{derivative-chain state}.
}
$$

Thus, the true gap reduction coordinates are:

$$
\boxed{
(k,\Phi,\mathsf{Chain}).
}
$$

---

# 30. Pressure concentration channel

A C3-X pressure-active core has:

$$
\boxed{
\int_{B_{2R}}
|p|^{3/2}dx
\gtrsim
b^{3/2}.
}
$$

Shrinking pressure-active cores can therefore form a:

$$
\boxed{
\text{critical pressure uniform-integrability failure}.
}
$$

This is a legitimate survivor channel for a hypothetical singularity.

---

# 31. Pressure cannot rescue a closed derivative bridge

If a certain derivative level/time satisfies:

- direct Theorem 3.5;
- or chain-assisted Theorem 3.14;

all hypotheses,

then full Navier–Stokes regularity is extended.

Pressure concentration cannot 'cancel out' this theorem.

Thus:

## No-Go 31.1

$$
\boxed{
\text{pressure concentration}
}
$$

cannot rescue an:

$$
\boxed{
\text{already closed geometric derivative regularity route}.
}
$$

---

# 32. C3-Y.5: Joint-Concentration Routing Principle

For a hypothetical blow-up,

if the pressure concentration branch holds,

then the derivative side must simultaneously experience at least one of the following for every theorem-admissible candidate:

$$
k
$$

## Y-J1 — Intermittency insufficient

$$
\boxed{
\mathfrak L_k^{best}>1.
}
$$

## Y-J2 — Uniform-local globalization failure

Only the ancestry-local:

$$
\phi
$$

is small,

but:

$$
\Phi
$$

is not small.

## Y-J3 — Temporal gate failure

Enhanced sparsity does not appear at the later slice specified by the external theorem.

## Y-J4 — Chain gate failure

The derivative-chain hypotheses required for the chain-assisted route, such as:

$$
(3.8),(3.9)
$$

do not hold.

## Y-J5 — Threshold/interface failure

The component/sign/tuning/analyticity interfaces are misaligned.

Thus:

$$
\boxed{
\text{pressure concentration}
}
$$

must coexist with:

$$
\boxed{
\text{all admissible derivative-closure routes failing}
}
$$

---

# 33. This is stronger than simple pressure–strain co-location

C3-X previously distinguished between:

$$
\Theta_{P/S}>0
$$

and:

$$
\Theta_{P/S}\to0.
$$

C3-Y points out:

Even if the pressure and strain active sets are completely spatially segregated,

as long as the global hypotheses of the derivative geometric theorem close,

regularity still holds.

Thus:

$$
\boxed{
\text{co-location is not the most essential logical interface}.
}
$$

What is more essential is:

$$
\boxed{
\text{pressure singular branch}
\cap
\text{derivative-geometry theorem failure}.
}
$$

---

# 34. Direct bridge gives a true finite-$k$ forbidden region

This is an important correction to C3-X.

C3-X treated:

$$
\phi_k
\lesssim
A_k^{-\theta_k^{chain}}
$$

as a finite-$k$ scale bridge,

but lacked theorem closure.

C3-Y now points out:

If one is willing to pay the stronger:

$$
\boxed{
\theta_k^{dir}
=
\frac{
3
}{
2(k+3/2)
},
}
$$

then Theorem 3.5 itself provides a true finite-$k$ conditional closure.

Therefore, finite-$k$ has two levels:

### theorem-level direct threshold

$$
\boxed{
\Phi_k
\lesssim
A_k^{-\theta_k^{dir}}.
}
$$

### chain-assisted weaker threshold

$$
\boxed{
\Phi_k
\lesssim
A_k^{-\theta_k^{chain}},
}
$$

but requires the derivative-chain gate.

---

# 35. At $k=2$

The true theorem-ready direct exponent is:

$$
\boxed{
\frac37.
}
$$

The formal chain-assisted exponent is:

$$
\boxed{
\frac17.
}
$$

Thus:

$$
\boxed{
\text{the missing } \frac{2}{7}
\text{ exponent is supplied by derivative-chain dynamics}.
}
$$

Indeed:

$$
\frac37-\frac17
=
\frac27.
$$

---

# 36. High-$k$ significance

As:

$$
k\to\infty,
$$

the direct volume burden is:

$$
O(k^{-1}),
$$

and the chain burden is:

$$
O(k^{-2}).
$$

Therefore, asymptotic criticality is not solely about the single scale statement:

$$
\boxed{
a_{\rm apr}\to a_{\rm chain}
}
$$

It can also be restated as:

$$
\boxed{
\text{chain dynamics reduces the additional spatial-intermittency exponent
from }O(k^{-1})
\text{ to }O(k^{-2}).
}
$$

---

# 37. Constants matter

All power-law statements only describe the scaling part as:

$$
A_k\to\infty
$$

The actual theorem also involves:

- $2^{-k}$;
- $C(k)$;
- $\widetilde C(\ell,k)$;
- factorial normalized chain quantities;
- harmonic-measure parameters.

In particular, Theorem 3.14 requires:

$$
\widetilde C
\gtrsim
k^2 C.
$$

Thus:

$$
\boxed{
\text{small exponent}
}
$$

does not imply an:

$$
\boxed{
\text{easy finite-}k\text{ numerical threshold}.
}
$$

This is a constant-level guard.

---

# 38. k-selection cannot use exponent alone

Although:

$$
\theta_k^{chain}\downarrow0,
$$

higher derivatives:

$$
A_k
$$

and theorem constants may also grow rapidly.

Therefore, the optimal derivative level cannot simply be chosen by maximizing:

$$
k.
$$

True adaptive routing requires comparing:

$$
\boxed{
\mathfrak L_k^{best}.
}
$$

rather than just comparing:

$$
\theta_k.
$$

---

# 39. Relation to ascending / descending chains

The ascending chain condition of Theorem 3.8 is precisely that:

$$
\boxed{
\text{the factorial-normalized derivative magnitude at level }k
\text{ dominates lower levels}.
}
$$

Theorem 3.9 analyzes the descending chain,

while the main proof routes through high derivative indices via strings / derivative-chain dynamics.

C3-Y does not re-prove those theorems.

This iteration merely proves:

> Once the chain gate provides a larger admissible geometric scale,
> the active-volume burden is precisely reduced by a factor of $k+1$.

---

# 40. New X-Integration guards

## G-SOURCEVER

Formal citation:

$$
\boxed{
\text{Grujić--Xu J. Math. Fluid Mech. 26 (2024), Article 53}.
}
$$

## G-3SCALE

Preserve:

$$
R_{\rm apr},
\quad
R_{\rm chain},
\quad
R_{\rm dir}.
$$

They must not be conflated into a single 'analyticity scale'.

## G-DIRECT

The direct finite-$k$ theorem uses:

$$
\theta_k^{dir}.
$$

## G-CHAINLOAD

The chain-assisted bridge uses:

$$
\theta_k^{chain}
$$

and must preserve chain gates such as:

$$
(3.8),(3.9)
$$

## G-K2

$$
1/7
$$

is the $k=2$ chain-assisted scaling exponent,

not a standalone theorem threshold.

## G-UNILOC

The ancestry-local:

$$
\phi
$$

must not substitute for the theorem-ready:

$$
\Phi.
$$

## G-TGATE

Intermittency must appear at the later analytic slice required by the external theorem.

## G-CONST

Power exponents and theorem constants must be preserved separately.

---

# 41. True ETN Update

Derivative/intermittency state:

$$
\boxed{
\Theta_k^{DI}
=
\left\langle
A_k,
R_{\rm apr}^{(k)},
R_{\rm chain}^{(k)},
R_{\rm dir}^{(k)},
\Phi_k,
\theta_k^{dir},
\theta_k^{chain},
\mathsf{ChainGate}_k,
\mathsf{TimeGate}_k,
\mathfrak L_k^{best}
\right\rangle.
}
$$

Joint pressure state:

$$
\boxed{
\Theta_k^{joint}
=
\left\langle
\Theta_k^{DI},
\text{pressure concentration certificate},
\text{pressure provenance}
\right\rangle.
}
$$

---

# 42. Main survivor after C3-Y

A hypothetical singularity now cannot merely say:

$$
\boxed{
\text{pressure concentrates}
+
\text{strain is intermittent}.
}
$$

It must additionally maintain:

$$
\boxed{
\text{every theorem-admissible derivative route remains scale-open
or interface-inadmissible}.
}
$$

That is:

$$
\boxed{
\textbf{Pressure Concentration}
\cap
\textbf{Derivative-Bridge Failure at Every Admissible Gate}.
}
$$

---

# 43. Major no-go

### NG-Y1

$$
\phi_2\lesssim A_2^{-1/7}
\Rightarrow
\text{regularity}.
$$

FALSE in general.

### NG-Y2

$$
\text{local ancestry intermittency}
\Rightarrow
\text{Grujić--Xu global criterion}.
$$

FALSE.

### NG-Y3

$$
\text{larger }k
\Rightarrow
\text{easier closure}.
$$

FALSE without constants / derivative amplitudes.

### NG-Y4

$$
\text{pressure concentration}
\Rightarrow
\text{geometric criterion irrelevant}.
$$

FALSE.

### NG-Y5

$$
\text{a-priori sparseness at }R_{\rm apr}
\Rightarrow
\text{regularity sparseness at }R_{\rm chain}.
$$

FALSE without enhanced intermittency / chain dynamics.

---

# 44. New frontier: C3-Z

C3-Y has now genuinely inserted the $1/7$ diagnostic of C3-X into the derivative-chain architecture,

and obtained two exact intermittency burdens:

$$
\boxed{
\theta_k^{dir}
=
\frac{
3
}{
2(k+3/2)
},
}
$$

$$
\boxed{
\theta_k^{chain}
=
\frac{
3
}{
2(k+1)(k+3/2)
}.
}
$$

The formal next problem is:

$$
\boxed{
\textbf{C3-Z — Uniform-Local Intermittency Globalization and Chain-Gate Recurrence Rigidity}.
}
$$

---

# 45. C3-Z proof obligations

## Z1 — Local-to-uniform globalization

From the ancestry core quantities:

$$
\phi_{n}
$$

and multi-core packing,

seek an upper bound for:

$$
\Phi_{k,c}
$$

## Z2 — Superlevel cover theorem

Use:

- first-frontier cores;
- operator cores;
- strain-gradient active cores;

to construct a covering of the selected derivative superlevel set.

## Z3 — Dense-core obstruction

If:

$$
\Phi_k
$$

is large,

prove there exists a ball:

$$
B_{R_{\rm apr}}(x)
$$

containing a fixed fraction of derivative-active volume.

Convert this congestion into:

- higher derivative stock;
- multi-core count;
- pressure concentration.

## Z4 — Direct gate recurrence

If $D^ku$ has infinitely many escape times,

investigate whether enhanced intermittency must appear at some Theorem 3.5 later slice.

## Z5 — Chain-gate recurrence

Investigate whether in a hypothetical blow-up:

$$
(3.8)
$$

ascending-chain gates appear infinitely often.

If not, use descending-chain control.

## Z6 — Constant-aware optimization

Preserve:

$$
C_{\rm apr},
C_{\rm dir},
C_{\rm chain}
$$

and explicitly construct:

$$
\mathfrak L_k^{best}.
$$

## Z7 — Pressure concentration routing

If derivative closure consistently fails,

investigate whether pressure-active cores must form a recurrent multi-core structure with derivative-congested balls.

## Z8 — End-of-C3 audit

After C3-Z is completed,

perform a complete:

- theorem;
- conditional;
- no-go;
- open frontier;

dependency audit on C1–C3-Z,

to determine whether to transition to:

$$
\boxed{
\textbf{C4 — unified survivor closure program}.
}
$$

---

# 46. Formal Status

$$
\boxed{
\begin{aligned}
\text{three scale hierarchy}
&:\ \mathrm{EXTERNAL+DERIVED},\\
\Delta a_{\rm dir}
&:\ \mathrm{PROVED},\\
\Delta a_{\rm chain}
&:\ \mathrm{PROVED},\\
\theta_k^{dir}
&:\ \mathrm{PROVED},\\
\theta_k^{chain}
&:\ \mathrm{PROVED},\\
\theta_k^{dir}/\theta_k^{chain}=k+1
&:\ \mathrm{PROVED},\\
\text{uniform-local volume}\Rightarrow\text{component/sign 1D sparseness}
&:\ \mathrm{PROVED},\\
\text{direct finite-}k\text{ volume bridge}
&:\ \mathrm{PROVED\ CONDITIONAL\ ON\ THEOREM\ 3.5\ GATES},\\
\text{chain-assisted volume bridge}
&:\ \mathrm{PROVED\ CONDITIONAL\ ON\ THEOREM\ 3.14\ GATES},\\
k=2\text{ direct exponent }3/7
&:\ \mathrm{PROVED},\\
k=2\text{ chain exponent }1/7
&:\ \mathrm{PROVED/SCALING},\\
1/7\Rightarrow\text{standalone }k=2\text{ regularity}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{ancestry-local }\phi\Rightarrow\text{uniform-local }\Phi
&:\ \mathrm{OPEN},\\
\text{adaptive derivative closure load}
&:\ \mathrm{DEFINED},\\
\text{pressure concentration + all derivative gates fail}
&:\ \mathrm{STRUCTURAL\ SURVIVOR}.
\end{aligned}
}
$$

---

# 47. Conclusion

C3-X found:

$$
\phi_2
\lesssim
A_2^{-1/7}
$$

this elegant scale threshold.

C3-Y now tells us precisely what it represents.

The three scales are:

$$
\boxed{
R_{\rm dir}
<
R_{\rm chain}
<
R_{\rm apr}.
}
$$

If derivative-chain dynamics are not used,

relying solely on active volume to push the energy a-priori scale to the fixed-$k$ direct regularity scale,

requires:

$$
\boxed{
\Phi_k
\lesssim
A_k^{
-\frac{
3
}{
2(k+3/2)
}
}.
}
$$

If the derivative-chain gate is open,

it only requires:

$$
\boxed{
\Phi_k
\lesssim
A_k^{
-\frac{
3
}{
2(k+1)(k+3/2)
}
}.
}
$$

The exponent ratio between the two is:

$$
\boxed{
k+1.
}
$$

Thus, there exists an exact tradeoff between derivative-chain dynamics and spatial intermittency:

$$
\boxed{
\textbf{Dynamic derivative ordering}
\quad\leftrightarrow\quad
\textbf{spatial volume collapse}.
}
$$

In particular, for

$$
k=2:
$$

the direct theorem-ready burden is:

$$
\boxed{
3/7,
}
$$

and the chain-assisted scaling burden is:

$$
\boxed{
1/7.
}
$$

This corrects the theorem status of $1/7$ from the previous iteration.

More importantly,

the true Grujić–Xu-ready quantity is not the single ancestry core:

$$
\phi,
$$

but rather:

$$
\boxed{
\Phi
=
\text{uniform-local active-volume factor over all spatial points}.
}
$$

Therefore, the missing link has now shifted from:

> 'Is the intermittency sufficient?'

to:

> **Can the local intermittency of a singular ancestry be globalized into theorem-ready uniform-local sparseness, and can it repeatedly appear at the later time gate specified by the direct / chain theorem?**

This is the focus of the next iteration:

$$
\boxed{
\textbf{C3-Z — Uniform-Local Intermittency Globalization and Chain-Gate Recurrence Rigidity}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024); arXiv:1911.00974.
2. Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26 (2013), 289–296; arXiv:1111.0217.
3. Z. Bradshaw, A. Farhat, Z. Grujić, *An Algebraic Reduction of the ‘Scaling Gap’ in the Navier–Stokes Regularity Problem*, Archive for Rational Mechanics and Analysis 231 (2019), 1983–2005.
4. A. Farhat, Z. Grujić, K. Leitmeyer, *The space \(B^{-1}_{\infty,\infty}\), volumetric sparseness, and 3D NSE*, Journal of Mathematical Fluid Mechanics 19 (2017), 515–523.
5. P. Constantin, *Pressure, Intermittency, Singularity*, Journal of Mathematical Fluid Mechanics (2023); arXiv:2301.04489.

# Internal dependencies

- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3U_PressureHeredity_MeanPointwiseRigidity_v0.1.md`
- `NS_C3T_PressureDiversification_ConeEigenvalue_HeredityGap_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3R_MultiCore_PressureHorizon_StrainConvexity_v0.1.md`
- `NS_C3Q_PressureProjection_OperatorLocalization_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-Z — Uniform-Local Intermittency Globalization and Chain-Gate Recurrence Rigidity}
}
$$