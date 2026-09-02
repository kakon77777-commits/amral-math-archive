---
title: "Navier–Stokes C5-K: Chain-Time Stitching, Window-Persistent Sign Defects, and Dynamic-Interpolation Closure Audit"
subtitle: "The Published Type-A/Type-B Mechanism Already Stitches Order-Dependent Times; the True Residual is Persistent Failure Across an Entire Admissible Chain Window"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style timing audit / persistent-window defect reduction / dynamic-interpolation interface"
epistemic_status: "Exact interval-overlap algebra + inherited C5-I/J same-time inequalities + faithful audit of Grujić–Xu 2024 Lemmas 3.16–3.17 and Theorem 3.14. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-K
# Chain-Time Stitching, Window-Persistent Sign Defects, and Dynamic-Interpolation Closure Audit

## 0. Current Round Positioning

C5-I proved:

$$
\boxed{
\text{Sign Geometry Failure}_k
\Rightarrow
\text{Lower-Order Descent Toll}_{k\to k-1}.
}
$$

C5-J further proved:

$$
\boxed{
\text{Line Fragmentation}
\Rightarrow
\text{Upper-Order Roughness}_{k\to k+1},
}
$$

and formed the same-time inequality:

$$
\boxed{
A_{k-1}(s)A_{k+1}(s)
\gtrsim
(N_k(s)-1)
A_k(s)^2.
}
$$

The main hard guard left at that time:

> Grujić–Xu Theorem 3.14 generally allows different theorem-admissible later times
> for different derivative orders;
> therefore, same-time order inequalities cannot be
> unconditionally multiplied across $k$.

Following a fresh audit in C5-K, it is found that:

$$
\boxed{
\textbf{This "different theorem times" itself
is not a loophole in the published theorem.}
}
$$

Because the proof of Theorem 3.14:

- inherently allows order-dependent later times;
- inherently allows switching between Type-$\mathcal A$/Type-$\mathcal B$ strings;
- Lemmas 3.16 and 3.17 respectively control A/B strings until a switch occurs;
- the theorem proof then alternates switch intervals;
- controls the incremental growth of derivative-root maxima;
- if the maxima attempt to grow again,
  they must also pay a positive temporal span;
- ultimately pushing regularity to $T^\ast$.

Therefore:

$$
\boxed{
\textbf{TYPE-SWITCH}
}
$$

should no longer serve as an independent residual motif in C5.

A true spatial survivor must be stronger:

$$
\boxed{
\textbf{The entire admissible window of a certain theorem pair }(k,t)
\textbf{ has no spatial pass.}
}
$$

This document refers to it as:

$$
\boxed{
\textbf{Window-Persistent Sign Defect}.
}
$$

Main results of this round:

1. faithful audit of Grujić–Xu Theorem 3.14 / Lemmas 3.16–3.17;
2. the published theorem already externally closes Type-switch stitching;
3. defines the exact theorem chain clock:
   $$
   \tau_k(t)
   =
   \left[
   \widetilde{\mathcal C}_k
   A_k(t)^{2/(k+1)}
   \right]^{-1};
   $$
4. admissible window:
   $$
   I_k(t)
   =
   [t+\tau_k/4,t+\tau_k];
   $$
5. if the theorem spatial condition truly fails at $(k,t)$,
   then the sign-thick failure must persist on **all**:
   $$
   s\in I_k(t);
   $$
6. C5-I descent is therefore upgraded to:
   $$
   \boxed{
   \text{Window-Persistent Descent Strip};
   }
   $$
7. two adjacent windows at the same base time overlap iff:
   $$
   1/4
   \le
   \tau_{k+1}/\tau_k
   \le
   4;
   $$
8. a whole derivative block shares a common theorem time iff:
   $$
   \max\tau_k/\min\tau_k\le4;
   $$
9. on such a common-time block,
   C5-I/J same-time inequalities can be legally iterated;
10. if clocks fail factor-4 synchronization,
    this is not a free timing defect:
    it forces a large adjacent derivative-root clock jump;
11. therefore strong Type-A-like ascent can avoid a same-time harmonic puncture only by:
    $$
    \boxed{
    \text{Harmonic Pass}
    \vee
    \text{Chain-Clock Separation};
    }
    $$
12. window failure has two limits:
    - strong persistent sign thickness;
    - harmonic-temporal critical saturation;
13. the correct remaining theorem interface is now:
    $$
    \boxed{
    \text{Theorem Setup Defect}
    \vee
    \text{Window-Persistent Sign Defect};
    }
    $$
14. Type switching and order-dependent theorem times,
    once Theorem 3.14 hypotheses hold,
    are already handled externally and should not be reinvented in C5.

---

# 1. Fresh primary-source audit

## 1.1 Theorem 3.14 quantifiers

Grujić–Xu 2024 Theorem 3.14:

for any:

$$
k\ge\ell
$$

and temporal point:

$$
t
$$

satisfying the theorem chain/setup assumptions and enough remaining time:

$$
\boxed{
t+
\frac1{
\mathcal C_k^2
A_k(t)^{2/(k+1)}
}
<
T^\ast,
}
$$

assumes the existence of:

$$
\boxed{
s=s(t)
}
$$

inside:

$$
\boxed{
I_k(t)
=
\left[
t+
\frac1{
4\widetilde{\mathcal C}_k
A_k(t)^{2/(k+1)}
},
\ 
t+
\frac1{
\widetilde{\mathcal C}_k
A_k(t)^{2/(k+1)}
}
\right],
}
$$

such that the component/sign superlevel set has the required 1D sparseness at scale:

$$
\boxed{
\rho
\le
\frac1{
2\widetilde{\mathcal C}_k
A_k(s)^{1/(k+1)}
}.
}
$$

If this holds for all required:

$$
k\ge\ell,
$$

then:

$$
\boxed{
T^\ast
\text{ is not a blow-up time}.
}
$$

### Key audit

The theorem does **not** require:

$$
s_k=s_{k+1}.
$$

---

# 2. Definition 3.15

Published derivative orders are split:

$$
\ell_0<\ell_1<\cdots,
$$

with:

$$
\ell_{i+1}\ge2\ell_i.
$$

For each section:

$$
[\ell_i,\ell_{i+1}],
$$

one picks a time-dependent maximizer:

$$
m_i(t)
$$

of:

$$
\mathcal R(j,c(\ell_i),t).
$$

A section/string can be:

$$
\boxed{
\mathcal A
}
$$

or:

$$
\boxed{
\mathcal B,
}
$$

according to the published conditions (3.43)/(3.44).

---

# 3. Lemma 3.16 — Type-A control

Published Lemma 3.16 says:

if a string:

$$
[\ell_i,\ell_{i+q}]
$$

starts Type-$\mathcal A$,

and the theorem's spatial hypothesis (3.41) is available for the required orders/times,

then derivative roots:

$$
\mathcal R
$$

throughout the string remain bounded up to the first A-to-B switch by:

$$
\boxed{
(1+\widetilde\epsilon)^{1/\ell_{i+q}}
\times
\Theta
\times
\text{initial string maximum}.
}
$$

So Type-A ascent is dynamically stabilized until switch.

---

# 4. Lemma 3.17 — Type-B control

Published Lemma 3.17:

if the string starts Type-$\mathcal B$,

then until the first B-to-A switch:

$$
\boxed{
\sup_t
\mathcal R
\le
\text{initial section/string maximum}.
}
$$

So descending/tail-dominating behavior is also stabilized.

---

# 5. Published switch-time stitching

The proof of Theorem 3.14 defines alternating switch times:

$$
\widehat t_n(i),
\qquad
\widetilde t_n(i),
$$

for B-to-A and A-to-B transitions.

It repeatedly applies:

- Lemma 3.16 on A intervals;
- Lemma 3.17 on B intervals.

The proof obtains bounds of the form:

$$
\boxed{
\mathcal R_{\max}(t)
\le
(1+\widetilde\epsilon)^{\#\text{cycles}/\ell}
\times
\text{controlled initial maximum}.
}
$$

---

# 6. Switch recovery has a time cost

In the theorem proof,

after harmonic/intermittency contraction at a high derivative level:

$$
k_q,
$$

if the relevant root maximum does not stay decreased,

it must recover by a fixed multiplicative factor:

$$
M_{k_q}>1.
$$

The local-in-time derivative estimate then forces a minimum time span:

$$
\boxed{
T_{k_q}^{\ast}
\gtrsim
2^{-2k_q}
\|D^{k_q}u\|_\infty^{-d/(k_q+d/2)}
}
$$

up to theorem constants.

Thus:

$$
\boxed{
\textbf{switch/recovery is not a free Zeno mechanism}
}
$$

under the published hypotheses.

---

# 7. C5-K.1: Type-Switch Defect Removal

## Research-program conclusion

Assume the complete Grujić–Xu Theorem 3.14 setup and spatial condition (3.41) hold for every required:

$$
(k,t).
$$

Then:

$$
\boxed{
\text{Type-A/B switching}
}
$$

is already handled by published dynamic interpolation,

and:

$$
\boxed{
T^\ast
}
$$

is not a blow-up time.

Therefore:

$$
\boxed{
\textbf{TYPE-SWITCH cannot be retained as an independent hypothetical singular survivor.}
}
$$

### Important

This is an **external theorem-backed closure**,

not a new proof of Theorem 3.14.

---

# 8. What must fail if a hypothetical survivor remains?

Under the rest of the theorem setup,

a hypothetical singular survivor must fail at least one required theorem condition.

Spatially,

this means:

there exists some theorem pair:

$$
(k,t)
$$

for which no admissible:

$$
s\in I_k(t)
$$

satisfies the required 1D sparseness condition.

This is stronger than:

> the good time is different from the neighboring order's good time.

There is **no good time anywhere in the whole window**.

---

# 9. Chain clock

Define:

$$
\boxed{
\tau_k(t)
=
\frac1{
\widetilde{\mathcal C}_k
A_k(t)^{2/(k+1)}
}.
}
$$

Then:

$$
\boxed{
I_k(t)
=
[t+\tau_k/4,t+\tau_k].
}
$$

Call:

$$
\boxed{
\Omega_k(t)
=
\tau_k(t)^{-1}
=
\widetilde{\mathcal C}_k
A_k(t)^{2/(k+1)}
}
$$

the:

$$
\boxed{
\textbf{Chain Clock Frequency}.
}
$$

---

# 10. Spatial defect score

At time:

$$
s,
$$

for each:

$$
x_0,
$$

let:

$$
V_{\lambda,k}(x_0,s)
$$

denote the theorem-selected component/sign superlevel set:

selected so that the corresponding component/sign realizes:

$$
|D^ku(x_0,s)|.
$$

Define:

$$
\boxed{
\beta_k(s)
=
\sup_{x_0}
\inf_{
0<\rho\le r_k(s)
}
\inf_{
[\nu]\in\mathbb{RP}^2
}
b_{
V_{\lambda,k}(x_0,s)
}
(x_0,\rho,[\nu]).
}
$$

with:

$$
r_k(s)
=
\frac1{
2\widetilde{\mathcal C}_k
A_k(s)^{1/(k+1)}
}.
$$

### Interpretation

- $\beta_k(s)<\delta$: strict spatial pass;
- $\beta_k(s)>\delta$: strict spatial fail;
- $\beta_k(s)=\delta$: critical boundary requiring attainment care.

---

# 11. Window spatial score

Define:

$$
\boxed{
\beta_k^{win}(t)
=
\inf_{
s\in I_k(t)
}
\beta_k(s).
}
$$

Then:

## K-WPASS

there exists theorem-admissible spatial pass in:

$$
I_k(t).
$$

## K-WFAIL

no:

$$
s\in I_k(t)
$$

passes.

For strict failure:

$$
\boxed{
\beta_k^{win}(t)>\delta.
}
$$

---

# 12. Window-Persistent Sign Defect

If K-WFAIL holds,

then for **every**:

$$
s\in I_k(t),
$$

there exists a dangerous basepoint:

$$
x_k(s)
$$

such that the selected sign-high set is too thick in every admissible direction/scale.

Thus C5-I's bad-core argument applies for every:

$$
s\in I_k(t).
$$

This is:

$$
\boxed{
\textbf{Window-Persistent Sign Defect}.
}
$$

The spatial carrier:

$$
x_k(s)
$$

may move with:

$$
s.
$$

The amplitude consequence is global and does not require a fixed carrier.

---

# 13. C5-K.2: Window-Persistent Descent Strip

Let:

$$
\kappa_{\lambda,\delta}
=
(1+\lambda)\delta-1>0.
$$

If the theorem spatial condition fails throughout:

$$
I_k(t),
$$

then for every:

$$
s\in I_k(t),
$$

$$
\boxed{
A_{k-1}(s)
\ge
\kappa_{\lambda,\delta}
r_k(s)
A_k(s).
}
$$

Therefore:

$$
\boxed{
A_{k-1}(s)
\ge
\frac{
\kappa_{\lambda,\delta}
}{
2\widetilde{\mathcal C}_k
}
A_k(s)^{k/(k+1)}
\qquad
\forall s\in I_k(t).
}
$$

---

# 14. Chain-root strip

In a fixed section normalization:

$$
c,
$$

C5-I gives:

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k(c)
\mathcal R(k,c,s)
\qquad
\forall s\in I_k(t).
}
$$

Thus the descent toll is no longer a one-time witness.

It persists throughout the entire theorem window.

---

# 15. Integrated persistent descent toll

Integrating:

$$
\boxed{
\int_{I_k(t)}
A_{k-1}(s)ds
\ge
\frac{
\kappa_{\lambda,\delta}
}{
2\widetilde{\mathcal C}_k
}
\int_{I_k(t)}
A_k(s)^{k/(k+1)}ds.
}
$$

Similarly:

$$
\boxed{
\int_{I_k(t)}
\mathcal R(k-1,c,s)ds
\ge
d_k(c)
\int_{I_k(t)}
\mathcal R(k,c,s)ds.
}
$$

### Meaning

A theorem-window spatial failure pays an entire **temporal strip** of lower-order root support.

---

# 16. Harmonic-temporal critical saturation

A sequence of spatially failing windows can satisfy:

$$
\boxed{
\beta_{k_j}^{win}(t_j)
\downarrow
\delta.
}
$$

No finite event passes,

but the entire-window minimum approaches the harmonic threshold.

Call:

$$
\boxed{
\textbf{Harmonic–Temporal Critical Saturation}.
}
$$

This is stronger than C5-I pointwise saturation:

the closest approach to harmonic pass is measured across the full admissible time window.

---

# 17. Strong window failure

If:

$$
\boxed{
\beta_k^{win}(t)
\ge
\delta+\epsilon_0
}
$$

with:

$$
\epsilon_0>0,
$$

then the descent strip improves to:

$$
\boxed{
A_{k-1}(s)
\ge
\frac{
(1+\lambda)(\delta+\epsilon_0)-1
}{
2\widetilde{\mathcal C}_k
}
A_k(s)^{k/(k+1)}
}
$$

throughout:

$$
I_k(t).
$$

So fixed harmonic defect margin pays a fixed stronger derivative-root toll over the whole window.

---

# 18. Two-window overlap

Consider two orders:

$$
k,m
$$

with the **same base time**:

$$
t.
$$

Their windows:

$$
I_k(t)
=
[t+\tau_k/4,t+\tau_k],
$$

$$
I_m(t)
=
[t+\tau_m/4,t+\tau_m].
$$

They overlap iff:

$$
\boxed{
\max
\left(
\tau_k/4,
\tau_m/4
\right)
\le
\min(\tau_k,\tau_m).
}
$$

---

# 19. C5-K.3: Adjacent Chain-Window Overlap Lemma

For adjacent:

$$
k,k+1,
$$

$$
\boxed{
I_k(t)\cap I_{k+1}(t)\ne\varnothing
}
$$

iff:

$$
\boxed{
\frac14
\le
\frac{
\tau_{k+1}(t)
}{
\tau_k(t)
}
\le
4.
}
$$

Equivalent clock-frequency form:

$$
\boxed{
\frac14
\le
\frac{
\Omega_{k+1}(t)
}{
\Omega_k(t)
}
\le
4.
}
$$

---

# 20. Whole-block common time

For a finite derivative block:

$$
J\le k\le K,
$$

all windows have common left origin:

$$
t.
$$

The intersection:

$$
\bigcap_{k=J}^{K}
I_k(t)
$$

is nonempty iff:

$$
\boxed{
\frac{
\max_{J\le k\le K}\tau_k(t)
}{
\min_{J\le k\le K}\tau_k(t)
}
\le
4.
}
$$

### Proof

The common intersection exists iff:

$$
\max_k \tau_k/4
\le
\min_k\tau_k.
$$

$\square$

---

# 21. C5-K.4: Chain-Window Helly Lemma

Define block clock spread:

$$
\boxed{
\mathfrak S_{J,K}^{clock}(t)
=
\frac{
\max_{J\le k\le K}\tau_k(t)
}{
\min_{J\le k\le K}\tau_k(t)
}.
}
$$

Then:

$$
\boxed{
\mathfrak S_{J,K}^{clock}(t)\le4
}
$$

is equivalent to existence of one common:

$$
s
$$

admissible for every order:

$$
J,\ldots,K.
$$

### Remark

This is a special one-dimensional interval-Helly property.

---

# 22. Common-time descent block

Suppose:

1. same base time:
   $$
   t;
   $$
2. every order:
   $$
   J+1,\ldots,K
   $$
   has Window-Persistent Sign Defect;
3. clock spread:
   $$
   \mathfrak S_{J,K}^{clock}(t)\le4.
   $$

Choose:

$$
s_\ast
\in
\bigcap_{k=J}^{K}
I_k(t).
$$

Then every level:

$$
J+1,\ldots,K
$$

is spatially bad at the same:

$$
s_\ast.
$$

---

# 23. C5-K.5: Common-Time Block Descent

At:

$$
s_\ast,
$$

C5-I gives:

$$
\mathcal R(k-1,c,s_\ast)
\ge
d_k(c)
\mathcal R(k,c,s_\ast)
$$

for:

$$
J<k\le K.
$$

Thus:

$$
\boxed{
\mathcal R(J,c,s_\ast)
\ge
\left(
\prod_{k=J+1}^{K}
d_k(c)
\right)
\mathcal R(K,c,s_\ast).
}
$$

Equivalently:

$$
\boxed{
\frac{
\mathcal R(K,c,s_\ast)
}{
\mathcal R(J,c,s_\ast)
}
\le
\prod_{k=J+1}^{K}
d_k(c)^{-1}.
}
$$

---

# 24. C5-K.6: Clock-Synchronized Type-A Puncture

Suppose at common base time:

$$
t
$$

a block:

$$
[J,K]
$$

has:

$$
\mathfrak S_{J,K}^{clock}(t)\le4.
$$

If at every common admissible time:

$$
s
$$

the derivative-root ascent satisfies:

$$
\boxed{
\frac{
\mathcal R(K,c,s)
}{
\mathcal R(J,c,s)
}
>
\prod_{k=J+1}^{K}
d_k(c)^{-1},
}
$$

then it is impossible for every level:

$$
J+1,\ldots,K
$$

to have Window-Persistent Sign Defect.

Therefore at least one level admits a theorem-window harmonic pass.

### Meaning

$$
\boxed{
\textbf{Strong block ascent}
+
\textbf{clock synchronization}
\Rightarrow
\textbf{harmonic puncture}.
}
$$

---

# 25. Chain-clock separation

If:

$$
\mathfrak S_{J,K}^{clock}>4,
$$

no common theorem time is available across the full block.

This is:

$$
\boxed{
\textbf{Chain-Clock Separation}.
}
$$

But this timing defect is not independent of derivative amplitudes.

---

# 26. Adjacent clock ratio in derivative roots

Recall:

$$
\tau_k
=
\frac1{
\widetilde{\mathcal C}_k
A_k^{2/(k+1)}
}.
$$

So:

$$
\boxed{
\frac{
\tau_{k+1}
}{
\tau_k
}
=
\frac{
\widetilde{\mathcal C}_k
}{
\widetilde{\mathcal C}_{k+1}
}
\left(
\frac{
A_k^{1/(k+1)}
}{
A_{k+1}^{1/(k+2)}
}
\right)^2.
}
$$

---

# 27. C5-K.7: Clock Separation = Root-Clock Jump

If:

$$
\boxed{
\tau_{k+1}/\tau_k<1/4,
}
$$

then:

$$
\boxed{
\frac{
A_{k+1}^{1/(k+2)}
}{
A_k^{1/(k+1)}
}
>
2
\sqrt{
\frac{
\widetilde{\mathcal C}_k
}{
\widetilde{\mathcal C}_{k+1}
}
}.
}
$$

This is a strong upward root-clock jump.

If:

$$
\boxed{
\tau_{k+1}/\tau_k>4,
}
$$

then:

$$
\boxed{
\frac{
A_{k+1}^{1/(k+2)}
}{
A_k^{1/(k+1)}
}
<
\frac12
\sqrt{
\frac{
\widetilde{\mathcal C}_k
}{
\widetilde{\mathcal C}_{k+1}
}
}.
}
$$

This is a strong downward root-clock jump.

### Conclusion

$$
\boxed{
\textbf{Chain-clock separation is derivative-order amplitude geometry,
not free temporal noise.}
}
$$

---

# 28. Clock-log variation

Define:

$$
\boxed{
\chi_k^{clock}(t)
=
\log\tau_k(t).
}
$$

Then block common-time failure is:

$$
\boxed{
\operatorname{osc}_{J\le k\le K}
\chi_k^{clock}(t)
>
\log4.
}
$$

So timing separation becomes a compact order-space oscillation statistic.

---

# 29. Compactified clock spread

Define:

$$
\boxed{
\widehat{\mathfrak S}^{clock}
=
\frac{
\log\mathfrak S^{clock}
}{
1+\log\mathfrak S^{clock}
}
\in[0,1).
}
$$

with:

$$
\mathfrak S^{clock}\ge1.
$$

Critical threshold:

$$
\boxed{
\widehat{\mathfrak S}_{crit}
=
\frac{
\log4
}{
1+\log4
}.
}
$$

This creates a compact timing coordinate.

---

# 30. Theorem-time pass flag

For every valid theorem pair:

$$
(k,t),
$$

define:

$$
\boxed{
\mathsf W_k(t)
=
\begin{cases}
1,&\exists s\in I_k(t)\text{ satisfying (3.41)},\\
0,&\text{otherwise}.
\end{cases}
}
$$

Then Theorem 3.14's spatial hypothesis is:

$$
\boxed{
\mathsf W_k(t)=1
}
$$

for all required:

$$
(k,t).
$$

---

# 31. C5-K.8: Published Dynamic-Stitching Closure Audit

Under all other hypotheses of Grujić–Xu Theorem 3.14:

if:

$$
\boxed{
\mathsf W_k(t)=1
}
$$

for every required:

$$
k,t,
$$

then:

$$
\boxed{
T^\ast
\text{ is not a blow-up time}.
}
$$

The published proof already handles:

- $s_k\ne s_{k+1}$;
- Type-A/B changes;
- time-dependent section maximizers;
- repeated switch intervals;
- accumulated small derivative-root increments.

### Conclusion

$$
\boxed{
\textbf{Order-dependent theorem times and Type switching
are not independent survivor defects once }\mathsf W=1.
}
$$

---

# 32. Correct hypothetical-survivor implication

Therefore,

within the full theorem setup,

a hypothetical blow-up must provide at least one:

$$
(k,t)
$$

with:

$$
\boxed{
\mathsf W_k(t)=0.
}
$$

That is:

$$
\boxed{
\textbf{Window-Persistent Sign Defect}.
}
$$

Or the trajectory must fail another explicit theorem setup hypothesis before the spatial question is reached.

---

# 33. Theorem setup defects

Theorem 3.14 is not an unconditional statement about arbitrary:

$$
(k,t).
$$

It uses:

- derivative-chain setup (3.8);
- parameter compatibility (3.9);
- enough remaining time (3.40);
- all theorem constants;
- solution regularity assumptions before $T^\ast$.

Therefore C5 must preserve:

$$
\boxed{
\textbf{Theorem-Setup Defect}.
}
$$

as distinct from:

$$
\boxed{
\textbf{Window-Persistent Sign Defect}.
}
$$

C5-K does not silently assert setup hypotheses are automatic.

---

# 34. Window root-turnover factor

For a failing theorem window:

$$
I_k(t),
$$

define:

$$
\boxed{
\mathfrak T_k^{win}(t)
=
\frac{
\sup_{s\in I_k(t)}
\mathcal R(k,c,s)
}{
\inf_{s\in I_k(t)}
\mathcal R(k,c,s)
}
\in[1,\infty].
}
$$

compactify:

$$
\boxed{
\widehat{\mathfrak T}_k^{win}
=
\frac{
\log\mathfrak T_k^{win}
}{
1+\log\mathfrak T_k^{win}
}.
}
$$

---

# 35. Meaning

If:

$$
\mathfrak T_k^{win}
$$

bounded,

the persistent descent strip acts on a root profile that remains comparable throughout the theorem window.

If:

$$
\mathfrak T_k^{win}\to\infty,
$$

the window contains:

$$
\boxed{
\textbf{Derivative-Root Temporal Turnover}.
}
$$

This is a legitimate residual temporal defect.

Unlike generic "time mismatch",

it is a concrete same-order root variation inside one theorem window.

---

# 36. Persistent descent under bounded turnover

If:

$$
\mathfrak T_k^{win}\le T_0,
$$

then:

$$
\inf_{I_k}
\mathcal R(k,c,s)
\ge
T_0^{-1}
\sup_{I_k}
\mathcal R(k,c,s).
$$

Together with:

$$
\mathcal R(k-1,c,s)
\ge
d_k\mathcal R(k,c,s),
$$

throughout the window:

$$
\boxed{
\inf_{I_k}
\mathcal R(k-1,c,s)
\ge
d_kT_0^{-1}
\sup_{I_k}
\mathcal R(k,c,s).
}
$$

So bounded turnover makes the window-persistent defect even more rigid.

---

# 37. Window-persistent sign-core process

At each:

$$
s\in I_k(t),
$$

choose deterministic bad witness:

$$
x_k(s)
$$

and angular line profile:

$$
b_{k,s}([\nu]).
$$

If roughness is bounded,

C5-J allows compactification of normalized line processes:

$$
\Psi_{k,s}(\nu,\sigma).
$$

Thus a failing theorem window can be represented as a time-indexed family:

$$
\boxed{
s
\mapsto
\Psi_{k,s}.
}
$$

This is a path in a compact line-profile space when spatial/temporal roughness is controlled.

---

# 38. Window sign-profile measure

Normalize theorem time:

$$
\theta
=
\frac{
s-(t+\tau_k/4)
}{
3\tau_k/4
}
\in[0,1].
$$

Push forward Lebesgue measure by:

$$
\theta
\mapsto
\Psi_{k,s(\theta)}.
$$

This gives:

$$
\boxed{
\mathfrak Y_k^{win}
\in
\mathcal P(
\mathcal K_{\rm line}
),
}
$$

for a compact line-profile state space in bounded-roughness branches.

### Future use

This turns persistent theorem-window failure into a recurrent probability distribution over bad line profiles.

---

# 39. Strong window failure vs critical window saturation

Window-persistent failures split:

## K-SIGNSTRONG

$$
\boxed{
\beta_k^{win}
\ge
\delta+\epsilon_0.
}
$$

Pays stronger descent throughout the whole window.

## K-SIGNCRIT

$$
\boxed{
\beta_k^{win}
\downarrow
\delta.
}
$$

Survivor approaches the harmonic threshold in the best time available inside each theorem window.

This is:

$$
\boxed{
\textbf{Harmonic–Temporal Critical Saturation}.
}
$$

---

# 40. Chain-clock synchronized bad block

Suppose an entire section/block:

$$
[J,K]
$$

satisfies:

- setup at same base time $t$;
- $\mathsf W_k(t)=0$ for all relevant $k$;
- clock spread $\le4$.

Then a common:

$$
s_\ast
$$

exists and every bad level's same-time order constraints are simultaneously valid.

Therefore:

- C5-I descent;
- C5-J order-sandwich;
- Type-A puncture inequalities;

can be applied without any time-stitching ambiguity.

---

# 41. Chain-clock separated bad block

If:

$$
\mathfrak S_{J,K}^{clock}>4,
$$

the failure of common time is encoded by:

$$
\boxed{
\text{root-clock oscillation across derivative order}.
}
$$

This replaces vague:

$$
\boxed{
\text{"different k use different times"}.
}
$$

The timing mismatch has become a quantitative order-space state.

---

# 42. C5-K residual timing taxonomy

After published dynamic-stitching audit,

remaining timing objects are:

## K-T1 — Window-Persistent Sign Failure

No spatial pass anywhere in one theorem-admissible interval.

## K-T2 — Harmonic–Temporal Critical Saturation

The best point in the whole window approaches but never crosses:

$$
\delta.
$$

## K-T3 — Root Turnover Inside the Window

$$
\mathfrak T_k^{win}\to\infty.
$$

## K-T4 — Chain-Clock Separation

Across orders:

$$
\mathfrak S^{clock}>4.
$$

## K-T5 — Theorem Setup Failure

The chain/time hypotheses required to invoke Theorem 3.14 are unavailable.

### Removed

$$
\boxed{
\textbf{Generic Type-Switch Defect}
}
$$

is removed as an independent category.

---

# 43. Relation to published switch iteration

The theorem proof obtains for repeated A/B iterations:

$$
\mathcal R_{\max}
\lesssim
(1+\widetilde\epsilon)^{n/\ell}
\times
\text{initial controlled maximum}.
$$

and bounds:

$$
1+\widetilde\epsilon
$$

by a quantity approaching $1$ at high derivative block scale.

It then shows attempts to regain lost high-derivative amplitude require positive time spans.

So:

$$
\boxed{
\textbf{switch accumulation is already part of the published closure mechanism}.
}
$$

C5 should not introduce a parallel switch-count proof unless analyzing failure of the theorem's hypotheses.

---

# 44. A methodological correction to C5-J

C5-J proposed root-transfer factors:

$$
\mathfrak T_{k\to k+1}
=
\max
\left\{
\frac{
\mathcal R_k(s_{k+1})
}{
\mathcal R_k(s_k)
},
\frac{
\mathcal R_k(s_k)
}{
\mathcal R_k(s_{k+1})
}
\right\}.
$$

These remain useful diagnostics,

but:

$$
\boxed{
\textbf{uniform boundedness of these transfer factors
is NOT required by Theorem 3.14}.
}
$$

The published Type-A/B argument provides a different dynamic stitching mechanism.

Thus transfer factors are optional C5 metadata,

not an external theorem hypothesis.

---

# 45. C5-K.9: Strong Ascent–Clock–Harmonic Trichotomy

Consider a same-base derivative block:

$$
[J,K].
$$

Suppose root ascent is strong enough that:

$$
\boxed{
\frac{
\mathcal R(K,c,s)
}{
\mathcal R(J,c,s)
}
>
\prod_{n=J+1}^{K}
d_n(c)^{-1}
}
$$

whenever a common theorem time exists.

Then at least one must hold:

## K-HARM

some level has a theorem-window harmonic pass;

or:

## K-CLOCK

$$
\boxed{
\mathfrak S_{J,K}^{clock}>4.
}
$$

or:

## K-SETUP

the common theorem setup is unavailable.

### Interpretation

strong high-order ascent can avoid harmonic puncture only by leaving the clock-synchronized theorem regime.

---

# 46. Clock separation and chain type

Clock frequency:

$$
\Omega_k
=
\widetilde{\mathcal C}_k
A_k^{2/(k+1)}.
$$

Therefore a strong Type-A adjacent root ascent naturally tends to increase:

$$
\Omega_{k+1}/\Omega_k,
$$

shrinking the higher-order theorem window relative to the lower order.

So:

$$
\boxed{
\text{Type-A ascent}
}
$$

and:

$$
\boxed{
\text{chain-clock separation}
}
$$

are structurally compatible.

But C5-K.7 quantifies the required amplitude jump.

---

# 47. Descending chains and clock separation

Conversely,

strong downward root transition makes:

$$
\tau_{k+1}/\tau_k
$$

large.

Thus both:

- steep ascent;
- steep descent;

can separate adjacent theorem clocks.

This mirrors the published need to handle both Type-A and Type-B strings dynamically.

---

# 48. Why C5-K does not reproduce Lemmas 3.16–3.17

The published lemmas use:

- precise chain constants;
- local-in-time analyticity;
- derivative induction;
- interpolation;
- harmonic-measure contraction.

C5-K only audits their role and adds independent:

- persistent-window sign consequence;
- clock-overlap algebra;
- block common-time condition;
- clock/root-jump interpretation.

No claim is made that C5-K replaces the published dynamic proof.

---

# 49. The corrected C5 high-order frontier

Before C5-K:

$$
\boxed{
\text{Sign}
+
\text{Fragmentation}
+
\text{Type Switch}
+
\text{Time Stitching}.
}
$$

After C5-K:

- fragmentation → derivative roughness / order curvature;
- Type switching → externally closed if theorem spatial hypothesis holds;
- generic order-dependent times → externally handled;
- remaining spatial failure → window-persistent sign defect;
- common-time obstruction → chain-clock separation;
- within-window instability → root turnover.

So the frontier becomes:

$$
\boxed{
\textbf{Persistent Bad Windows}
+
\textbf{Clock/Root Criticality}
+
\textbf{Theorem-Setup Failure}.
}
$$

---

# 50. C5-K compact state

For a theorem pair:

$$
(k,t),
$$

define:

$$
\boxed{
\Theta_k^K(t)
=
\left\langle
\mathsf W_k(t),
\beta_k^{win}(t),
\widehat{\mathfrak T}_k^{win}(t),
\tau_k(t),
\Omega_k(t),
\mathfrak Y_k^{win},
\mathsf{Setup}_k(t)
\right\rangle.
}
$$

For a block:

$$
[J,K],
$$

add:

$$
\boxed{
\mathfrak S_{J,K}^{clock}.
}
$$

---

# 51. Compactification

Use:

$$
\widehat\tau
=
\frac{\tau}{1+\tau},
$$

$$
\widehat\Omega
=
\frac{\Omega}{1+\Omega},
$$

and previous compact coordinates.

Then recurrent theorem-window defect sequences admit subsequential motif limits.

---

# 52. Window-defect limit states

Possible limits:

## K-L1 — Strict Persistent Bad Window

$$
\beta_\ast^{win}>\delta.
$$

## K-L2 — Harmonic–Temporal Critical Boundary

$$
\beta_\ast^{win}=\delta,
\qquad
\mathsf W=0
\text{ at every finite event}.
$$

## K-L3 — Turnover Boundary

$$
\widehat{\mathfrak T}^{win}=1.
$$

## K-L4 — Clock-Separation Boundary

$$
\mathfrak S^{clock}>4
$$

recurrently or diverges.

## K-L5 — Setup Boundary

The theorem chain/setup gate fails recurrently.

---

# 53. Major no-go audit

### NG-K1

$$
s_k\ne s_{k+1}
\Rightarrow
\text{new loophole}.
$$

FALSE.

Published Theorem 3.14 already permits order-dependent times.

### NG-K2

$$
\text{Type-A/B switching}
\Rightarrow
\text{uncontrolled survivor}.
$$

FALSE under theorem hypotheses.

### NG-K3

$$
\text{theorem spatial failure}
\Rightarrow
\text{one isolated bad time}.
$$

FALSE.

Failure of the existence quantifier means an entire admissible window lacks a pass.

### NG-K4

$$
\text{no common block time}
\Rightarrow
\text{pure temporal randomness}.
$$

FALSE.

It is equivalent to chain-clock spread $>4$ and therefore derivative-root clock disparity.

### NG-K5

$$
\text{common-time block descent}
\Rightarrow
\text{full Theorem 3.14}.
$$

FALSE.

It is only a C5 compatibility bridge.

### NG-K6

$$
\mathfrak T_{k\to k+1}
\text{ bounded}
$$

is required by published theorem.

FALSE.

---

# 54. X-Integration guards update

## G-WINDOWQ

Theorem 3.14's existential time condition must be treated as a whole-window question.

## G-SWITCHEXT

Type-A/B switching is externally handled if theorem hypotheses hold.

## G-WFAIL

window failure means no admissible time passes, not merely a mismatched chosen time.

## G-CLOCK

order-time mismatch must preserve chain clock:

$$
\tau_k.
$$

## G-COMMONTIME

cross-order same-time multiplication requires actual common window intersection.

## G-SETUP

Theorem setup conditions remain distinct from spatial defects.

## G-TURNWIN

within-window root turnover is a concrete defect; generic time mismatch is not.

---

# 55. True ETN update

New C5-K edges:

$$
\boxed{
\text{WINDOW-SIGN-FAIL}_k
\longrightarrow
\text{DESCENT-STRIP}_{k\to k-1},
}
$$

$$
\boxed{
\text{CLOCK-SYNC}_{J:K}
+
\text{WINDOW-FAIL}_{J:K}
\longrightarrow
\text{COMMON-TIME BLOCK DESCENT},
}
$$

$$
\boxed{
\text{NO-COMMON-TIME}
\longrightarrow
\text{CHAIN-CLOCK SEPARATION},
}
$$

and external closure edge:

$$
\boxed{
\text{ALL REQUIRED WINDOW PASSES}
\stackrel{\text{Grujić--Xu 3.14}}{\Longrightarrow}
\text{NO BLOW-UP}.
}
$$

---

# 56. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal Young defects}.
$$

C5-C:

$$
\text{cross-curvature ordering}.
$$

C5-D:

$$
\text{spatial–matrix incompatibility}.
$$

C5-E:

$$
Q\to\text{gap/derivative/vorticity}.
$$

C5-F:

$$
\text{axis-pressure / derivative escalation}.
$$

C5-G:

$$
\text{fixed-order theorem-ready gate}.
$$

C5-H:

$$
\text{static all-order volume no-go}.
$$

C5-I:

$$
\text{sign geometry}\to\text{root descent}.
$$

C5-J:

$$
\text{fragmentation}\to\text{upper roughness/order curvature}.
$$

C5-K:

$$
\boxed{
\textbf{published dynamic interpolation already stitches Type switches and order-dependent times};
}
$$

so the true all-order residual becomes:

$$
\boxed{
\textbf{Window-Persistent Sign Defect}
\vee
\textbf{Chain-Clock / Root Turnover Defect}
\vee
\textbf{Theorem-Setup Defect}.
}
$$

---

# 57. New frontier: C5-L

The next natural target is no longer Type-A/B switching.

It is:

$$
\boxed{
\textbf{C5-L — Persistent Bad-Window Rigidity,
Chain-Clock Defect Measures,
and Root-Turnover Compression}.
}
$$

---

# 58. C5-L proof obligations

## L1 — Persistent bad-window path

Compactify:

$$
s\mapsto
\Psi_{k,s}
$$

over the whole normalized admissible theorem window.

## L2 — Bad-window carrier motion

Track:

$$
x_k(s)
$$

relative to chain spatial scale:

$$
r_k(s).
$$

Determine whether fast carrier relay costs spatial/temporal variation.

## L3 — Window-integrated descent

Use:

$$
\int_{I_k}
\mathcal R_{k-1}
\ge
d_k
\int_{I_k}
\mathcal R_k
$$

to define a temporal root-load defect.

## L4 — Root-turnover measure

Replace scalar:

$$
\mathfrak T_k^{win}
$$

with variation / Young measure of:

$$
\log\mathcal R(k,c,s)
$$

inside the theorem window.

## L5 — Clock defect measure

Compactify:

$$
k\mapsto\log\tau_k
$$

on derivative sections.

## L6 — Clock synchronization density

Measure how much of a derivative block belongs to a factor-4 synchronized cluster.

## L7 — Persistent critical saturation

If:

$$
\beta_k^{win}\downarrow\delta,
$$

study whether roughness/root-turnover/clock spread must compensate the shrinking harmonic margin.

## L8 — C5 final-phase audit

Determine whether C5 residuals have now all been reduced to compact recurrent defect measures sufficiently finite to close C5 and move to a new phase.

---

# 59. Formal Status

$$
\boxed{
\begin{aligned}
\text{Theorem 3.14 order-dependent time audit}
&:\ \mathrm{VERIFIED},\\
\text{Lemma 3.16 Type-A dynamic control}
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{Lemma 3.17 Type-B dynamic control}
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{published switch-time stitching}
&:\ \mathrm{EXTERNAL/VERIFIED},\\
\text{Type-switch as independent residual}
&:\ \mathrm{REMOVED},\\
\text{window-persistent sign defect}
&:\ \mathrm{DEFINED},\\
\text{window-persistent descent strip}
&:\ \mathrm{PROVED},\\
\text{two-window factor-4 overlap}
&:\ \mathrm{PROVED},\\
\text{block common-time criterion}
&:\ \mathrm{PROVED},\\
\text{common-time block descent}
&:\ \mathrm{PROVED},\\
\text{clock separation}\Leftrightarrow\text{root-clock jump}
&:\ \mathrm{PROVED},\\
\text{harmonic-temporal critical saturation}
&:\ \mathrm{DEFINED},\\
\text{within-window root turnover defect}
&:\ \mathrm{DEFINED},\\
\text{all theorem window passes}\Rightarrow\text{regularity}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 60. Conclusion

C5-J compressed:

$$
\boxed{
\text{line fragmentation}
}
$$

back into derivative-order roughness.

C5-K now re-audits the final:

$$
\boxed{
\text{chain-time stitching}.
}
$$

As a result, the first major correction is:

$$
\boxed{
\textbf{different derivative orders using different theorem times
is not itself a loophole}.
}
$$

Grujić–Xu Theorem 3.14 inherently allows each:

$$
(k,t)
$$

to independently choose:

$$
s=s(t)
\in
I_k(t).
$$

Its Lemmas 3.16 / 3.17 and the theorem proof have already:

- tracked Type-A/B strings;
- tracked switch times;
- bounded root maxima up to each switch;
- controlled small cumulative increments;
- imposed positive temporal cost when a contracted derivative root recovers;
- iterated until $T^\ast$.

So the generic:

$$
\boxed{
\text{TYPE-SWITCH}
}
$$

can be removed from the C5 residual list.

A true spatial failure must be stronger:

$$
\boxed{
\forall s\in I_k(t),
\quad
\text{harmonic spatial gate fails}.
}
$$

This gives:

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k(c)
\mathcal R(k,c,s)
\qquad
\forall s\in I_k(t).
}
$$

That is:

$$
\boxed{
\textbf{Window-Persistent Descent Strip}.
}
$$

Next, the theorem windows themselves possess an exact clock:

$$
\boxed{
\tau_k
=
[
\widetilde{\mathcal C}_k
A_k^{2/(k+1)}
]^{-1}.
}
$$

Two adjacent windows share time iff:

$$
\boxed{
1/4
\le
\tau_{k+1}/\tau_k
\le
4.
}
$$

An entire block shares time iff:

$$
\boxed{
\max\tau/\min\tau
\le4.
}
$$

Once the block clock is synchronized,

C5-I/J same-time inequalities can be legally concatenated across the block.

If there is no common time,

this is no longer vague timing:

$$
\boxed{
\text{Chain-Clock Separation}
}
$$

is exactly equivalent to a derivative-root clock jump.

So what truly remains for C5 at this point is:

$$
\boxed{
\textbf{Persistent Bad Windows}
}
$$

$$
\boxed{
\textbf{Chain-Clock / Root Turnover Criticality}
}
$$

$$
\boxed{
\textbf{Theorem-Setup Defects}.
}
$$

Next article:

$$
\boxed{
\textbf{C5-L — Persistent Bad-Window Rigidity,
Chain-Clock Defect Measures,
and Root-Turnover Compression}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
2. Z. Grujić, *A geometric measure-type regularity criterion for solutions to the 3D Navier–Stokes equations*, Nonlinearity 26 (2013), 289–296.
3. A. Y. Solynin, *Ordering of sets, hyperbolic metrics, and harmonic measure*, Journal of Mathematical Sciences 95 (1999), 2256.
4. T. Ransford, *Potential Theory in the Complex Plane*, London Mathematical Society Student Texts 28, Cambridge University Press (1995).

# Internal dependencies

- `NS_C5J_LineSection_OrderSandwich_HarmonicSaturation_v0.1.md`
- `NS_C5I_SignGeometry_Chain_HarmonicCompatibility_v0.1.md`
- `NS_C5H_AllOrder_EffectiveVolume_AsymptoticCriticality_v0.1.md`
- `NS_C5G_PressureSignature_VorticityComplement_FixedOrderGate_v0.1.md`
- `NS_C5F_AxisPressureSignature_DerivativeGateEscalation_v0.1.md`
- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-L — Persistent Bad-Window Rigidity,
Chain-Clock Defect Measures,
and Root-Turnover Compression}
}
$$