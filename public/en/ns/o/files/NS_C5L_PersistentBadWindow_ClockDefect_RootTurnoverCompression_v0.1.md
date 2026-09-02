---
title: "Navier–Stokes C5-L: Persistent Bad-Window Rigidity, Chain-Clock Defect Measures, and Root-Turnover Compression"
subtitle: "Carrier Relay Cannot Remove the Window Debt; Root Turnover Routes to Viscous or Projected-Nonlinear Forcing; Clock Separation Becomes an Order-Space Variation Measure"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en-US"
status: "Theorem-style persistent-window compression / root-turnover PDE routing / chain-clock defect measure"
epistemic_status: "Exact consequences of smooth pre-singular Navier–Stokes evolution plus the C5-I/K sign-descent lemmas and theorem-window geometry. Published Grujić–Xu dynamic interpolation is used only as an external closure interface. Does NOT prove global regularity."
---

# Navier–Stokes C5-L
# Persistent Bad-Window Rigidity, Chain-Clock Defect Measures, and Root-Turnover Compression

## 0. Current Phase Positioning

C5-K made an important correction to the high-order temporal interface:

$$
\boxed{
\text{different derivative orders use different theorem times}
}
$$

and:

$$
\boxed{
\text{Type-A/B switching}
}
$$

are themselves not free loopholes left by Grujić–Xu Theorem 3.14.

Published theorem already allows order-dependent:

$$
s=s(t)
$$

and uses Lemmas 3.16–3.17 plus switch-time iteration to stabilize mixed derivative-chain strings.

Therefore, C5-K compresses the true residual into:

$$
\boxed{
\text{Window-Persistent Sign Defect}
}
$$

$$
\boxed{
\text{Chain-Clock Separation}
}
$$

$$
\boxed{
\text{Within-Window Root Turnover}
}
$$

$$
\boxed{
\text{Theorem-Setup Defect}.
}
$$

The tasks of C5-L are:

1. Determine whether a bad spatial carrier can escape the window debt via relay;
2. Elevate persistent window failure into carrier-independent derivative-load inequalities;
3. Reconnect root turnover to the true PDE time derivative;
4. Transform chain-clock separation into a compact order-space defect measure;
5. Determine whether harmonic-temporal critical saturation is a zero-cost boundary;
6. Further compress the C5 high-order residual into a small number of forcing / clock / setup defects;
7. Prepare for the C5 phase final audit.

Main results of this round:

1. Carrier relay cannot remove the persistent descent strip;
2. The bad-core local $L^2$ toll can similarly be integrated into a carrier-independent window toll;
3. Harmonic-temporal critical saturation:
   $$
   \beta_k^{win}\downarrow\delta
   $$
   **does not** make the descent coefficient vanish, because:
   $$
   (1+\lambda)\delta-1>0;
   $$
4. Therefore, harmonic critical saturation is not a zero-cost spatial boundary;
5. For the logarithmic turnover of:
   $$
   A_k(t)=\|D^ku(t)\|_\infty
   $$
   , the smooth N–S equation gives:
   $$
   \boxed{
   \operatorname{Var}_I\log \mathcal R_k
   \le
   \text{Viscous }(k+2)\text{ Toll}
   +
   \text{Projected-Nonlinear Toll};
   }
   $$
6. Thus, unbounded within-window root turnover must imply:
   $$
   \boxed{
   D^{k+2}u\text{ congestion}
   \vee
   \text{projected nonlinear temporal forcing};
   }
   $$
7. If both turnover tolls are bounded, the normalized root paths possess BV compactness;
8. Generic Root-Turnover can be removed from the independent survivor list;
9. Define the order-clock total variation:
   $$
   \mathfrak V^{clock}_{J,K}
   =
   \sum_{k=J}^{K-1}
   |\log\tau_{k+1}-\log\tau_k|;
   $$
10. If:
    $$
    \mathfrak V^{clock}_{J,K}\le\log4,
    $$
    the entire block must be clock synchronized;
11. The lack of a common theorem time must imply:
    $$
    \mathfrak V^{clock}_{J,K}>\log4;
    $$
12. Clock variation can be exactly decomposed into:
    - derivative-root order variation;
    - theorem/factorial normalization drift;
13. A chain-clock defect probability measure can be established;
14. The number of greedy factor-4 synchronized clusters is controlled by the clock total variation;
15. Therefore, clock separation is not a free timing motif, but a finite order-space variation budget;
16. The true remaining high-order residual after C5-L:
    $$
    \boxed{
    \text{Persistent Sign-Window Debt}
    }
    $$
    coupled to:
    $$
    \boxed{
    \text{Viscous/Nonlinear Turnover}
    \vee
    \text{Clock Variation}
    \vee
    \text{Theorem-Setup Defect}.
    }
    $$

---

# 1. Fresh primary-source audit

## 1.1 Grujić–Xu 2024

Theorem 3.14 allows each required derivative order:

$$
k
$$

and temporal point:

$$
t
$$

satisfying the chain setup to choose a possibly order-dependent later time:

$$
s=s(t)
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
\right].
}
$$

The proof explicitly combines:

- ascending-chain stabilization;
- descending-chain stabilization;
- Type-A / Type-B strings;
- switch times;
- harmonic-measure spatial input;
- dynamic interpolation.

Therefore order-dependent evaluation times and Type switching are already part of the published mechanism.

## 1.2 Theorem 3.8

Theorem 3.8 uses the ascending-chain condition:

$$
\boxed{
\mathcal R(j,c,t)
\le
\mathcal R(k,c,t),
\qquad
\ell\le j\le k,
}
$$

to control the wide Leibniz expansion of the nonlinearity on a derivative-dependent time interval.

This confirms that the high-order projected nonlinearity is a genuine chain-controlled object in the published framework.

C5-L nevertheless keeps its instantaneous projected-nonlinear turnover quantity separate rather than silently identifying it with a theorem estimate.

## 1.3 Time regularity

Bounded mild Navier–Stokes solutions in whole space have quantitative time-analyticity results in the literature.

For the present derivations we need only the weaker fact:

on every compact pre-singular interval,

the classical solution and its spatial derivatives are smooth in time,

so:

$$
t\mapsto D^ku(t)
$$

is differentiable in the required strong norms.

---

# 2. Window-Persistent Sign Failure

Fix one theorem pair:

$$
(k,t).
$$

Define:

$$
A_k(s)
=
\|D^ku(s)\|_\infty.
$$

The chain clock:

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

Theorem window:

$$
\boxed{
I_k(t)
=
[t+\tau_k/4,t+\tau_k].
}
$$

Suppose:

$$
\boxed{
\mathsf W_k(t)=0.
}
$$

That means no:

$$
s\in I_k(t)
$$

has the theorem-required 1D sign sparseness.

---

# 3. Carrier set

For each:

$$
s\in I_k(t),
$$

define bad-carrier set:

$$
\boxed{
\mathcal B_k(s)
=
\left\{
x_0:
\text{the selected component/sign at }x_0
\text{ fails every admissible line/scale test}
\right\}.
}
$$

Window failure means:

$$
\boxed{
\mathcal B_k(s)\ne\varnothing
\qquad
\forall s\in I_k(t).
}
$$

No assertion is made that:

$$
s\mapsto x_k(s)
$$

admits a continuous selection.

---

# 4. C5-L.1: Carrier-Relay Quotient Theorem

For every:

$$
s\in I_k(t),
$$

choose **any** bad carrier:

$$
x_k(s)\in\mathcal B_k(s).
$$

C5-I gives:

$$
\boxed{
A_{k-1}(s)
\ge
\kappa_{\lambda,\delta}
r_k(s)
A_k(s),
}
$$

where:

$$
\boxed{
r_k(s)
=
\frac1{
2\widetilde{\mathcal C}_k
A_k(s)^{1/(k+1)}
},
}
$$

and:

$$
\boxed{
\kappa_{\lambda,\delta}
=
(1+\lambda)\delta-1>0.
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

### Key point

The right-hand side contains no:

$$
x_k(s).
$$

Thus:

$$
\boxed{
\textbf{arbitrary bad-carrier relay cannot remove the descent strip}.
}
$$

Carrier identity is quotientable at the amplitude-chain level.

---

# 5. Carrier relay remains spatial metadata only

Carrier motion can still matter for:

- spatial compactness;
- causal ancestry;
- common-core pressure geometry.

But for:

$$
\boxed{
\text{window root amplitude debt}
}
$$

it is irrelevant.

Therefore C5-L does **not** create a new:

$$
\boxed{
\text{Carrier-Speed Defect}
}
$$

from scalar data.

### No-go

Translation/relay of a localized high-derivative structure can occur without a scalar norm paying a translation-specific cost.

So energy/amplitude data alone do not produce a useful universal carrier-speed bound.

---

# 6. Persistent bad-core local $L^2$ toll

C5-I also gives at every:

$$
s\in I_k(t),
$$

for a bad core:

$$
B_{r_k(s)}(x_k(s)),
$$

$$
\boxed{
\int_{B_{r_k(s)}(x_k(s))}
|D^ku(x,s)|^2dx
\ge
c_{\lambda,\delta}
A_k(s)^2
r_k(s)^3.
}
$$

Therefore globally:

$$
\boxed{
L_k(s)^2
=
\|D^ku(s)\|_2^2
\ge
c_{\lambda,\delta}
A_k(s)^2
r_k(s)^3
}
$$

for every:

$$
s\in I_k(t).
$$

---

# 7. C5-L.2: Window Derivative-Load Strip

Integrating over the theorem window:

$$
\boxed{
\int_{I_k(t)}
L_k(s)^2ds
\ge
c_{\lambda,\delta}
\int_{I_k(t)}
A_k(s)^2
r_k(s)^3ds.
}
$$

At chain scale:

$$
r_k(s)
=
\frac1{
2\widetilde{\mathcal C}_k
A_k(s)^{1/(k+1)}
},
$$

so:

$$
\boxed{
\int_{I_k(t)}
L_k(s)^2ds
\ge
\frac{
c_{\lambda,\delta}
}{
8\widetilde{\mathcal C}_k^3
}
\int_{I_k(t)}
A_k(s)^{2-\frac3{k+1}}ds.
}
$$

This is carrier-independent.

---

# 8. Root-load measure domination

Fix section normalization:

$$
c.
$$

Define root load measures on:

$$
I_k(t):
$$

$$
\boxed{
d\mu_{k}^{R}(s)
=
\mathcal R(k,c,s)\,ds.
}
$$

Window-persistent failure implies pointwise:

$$
\mathcal R(k-1,c,s)
\ge
d_k(c)
\mathcal R(k,c,s).
$$

Therefore as positive measures:

$$
\boxed{
\mu_{k-1}^{R}
\ge
d_k(c)
\mu_k^{R}.
}
$$

### Consequence

The descent strip survives:

- carrier relay;
- weak time limits;
- moving bad cores.

It is a true measure domination relation.

---

# 9. Harmonic-temporal critical saturation

Recall:

$$
\boxed{
\beta_k^{win}(t)
=
\inf_{s\in I_k(t)}
\beta_k(s).
}
$$

A recurrent failing sequence can satisfy:

$$
\boxed{
\beta_k^{win}(t)\downarrow\delta.
}
$$

At first glance this looks like a vanishing spatial defect margin.

But the descent coefficient is:

$$
\boxed{
\kappa_{\lambda,\beta}
=
(1+\lambda)\beta-1.
}
$$

At the theorem threshold:

$$
\boxed{
\kappa_{\lambda,\delta}
=
(1+\lambda)\delta-1
>0.
}
$$

---

# 10. C5-L.3: Critical Harmonic Saturation Has Nonzero Descent Cost

If:

$$
\beta_n^{win}\downarrow\delta
$$

through failing windows,

then:

$$
\boxed{
\kappa_{\lambda,\beta_n^{win}}
\downarrow
\kappa_{\lambda,\delta}
>0.
}
$$

Therefore:

$$
\boxed{
\textbf{Harmonic–Temporal Critical Saturation
does not make the derivative descent toll vanish}.
}
$$

### Interpretation

Only the harmonic-measure safety margin closes.

The order-chain descent pressure remains uniformly nondegenerate.

---

# 11. Consequence for survivor taxonomy

Thus:

$$
\boxed{
\textbf{Harmonic–Temporal Critical Saturation}
}
$$

need not remain an independent zero-cost motif.

It is better recorded as:

$$
\boxed{
\text{critical harmonic boundary}
+
\text{nonvanishing descent strip}.
}
$$

---

# 12. Within-window root turnover

Define:

$$
\boxed{
\mathcal R_k(s)
=
\mathcal R(k,c,s).
}
$$

Because the normalization factors:

$$
c,
\quad
k!
$$

are time independent,

$$
\boxed{
\log\mathcal R_k(s)
=
\frac1{k+1}
\log A_k(s)
+
\text{constant}.
}
$$

Assume:

$$
A_k(s)>0
$$

on the active theorem window.

---

# 13. Root turnover factor

Define:

$$
\boxed{
\mathfrak T_k^{win}
=
\frac{
\sup_{s\in I_k(t)}
\mathcal R_k(s)
}{
\inf_{s\in I_k(t)}
\mathcal R_k(s)
}
\ge1.
}
$$

Then:

$$
\boxed{
\log\mathfrak T_k^{win}
\le
\operatorname{Var}_{I_k(t)}
\log\mathcal R_k.
}
$$

---

# 14. Differentiating the $L^\infty$ norm

On a compact pre-singular interval,

$$
D^ku
$$

is smooth in time.

Thus:

$$
A_k(s)
=
\|D^ku(s)\|_\infty
$$

is locally absolutely continuous and for a.e.:

$$
s,
$$

$$
\boxed{
|A_k'(s)|
\le
\|\partial_tD^ku(s)\|_\infty.
}
$$

Hence:

$$
\boxed{
\left|
\frac{d}{ds}
\log A_k(s)
\right|
\le
\frac{
\|\partial_tD^ku(s)\|_\infty
}{
A_k(s)
}.
}
$$

---

# 15. Projected Navier–Stokes derivative equation

In Leray-projected form:

$$
\boxed{
\partial_tu
=
\nu\Delta u
-
\mathbb P
\big(
(u\cdot\nabla)u
\big).
}
$$

Therefore:

$$
\boxed{
\partial_tD^ku
=
\nu\Delta D^ku
-
D^k
\mathbb P
\big(
(u\cdot\nabla)u
\big).
}
$$

Define actual projected nonlinear source:

$$
\boxed{
\mathcal N_k^{proj}(s)
=
\left\|
D^k
\mathbb P
\big(
(u\cdot\nabla)u
\big)(s)
\right\|_\infty.
}
$$

### Guard

No generic $L^\infty$ Calderón–Zygmund estimate is silently used.

$\mathcal N_k^{proj}$ is retained as the true projected nonlinear source norm.

---

# 16. Temporal derivative bound

With a harmless dimensional Laplacian constant:

$$
C_\Delta,
$$

$$
\boxed{
\|\partial_tD^ku\|_\infty
\le
C_\Delta\nu A_{k+2}
+
\mathcal N_k^{proj}.
}
$$

Hence:

$$
\boxed{
\left|
\frac{d}{ds}
\log\mathcal R_k(s)
\right|
\le
\frac1{k+1}
\frac{
C_\Delta\nu A_{k+2}(s)
+
\mathcal N_k^{proj}(s)
}{
A_k(s)
}.
}
$$

---

# 17. Turnover tolls

Define:

## Viscous two-order turnover toll

$$
\boxed{
\mathfrak V_k^{visc}(I)
=
\frac{
C_\Delta\nu
}{
k+1
}
\int_I
\frac{
A_{k+2}(s)
}{
A_k(s)
}
ds.
}
$$

## Projected nonlinear turnover toll

$$
\boxed{
\mathfrak V_k^{NL}(I)
=
\frac1{k+1}
\int_I
\frac{
\mathcal N_k^{proj}(s)
}{
A_k(s)
}
ds.
}
$$

---

# 18. C5-L.4: Root-Turnover PDE Compression Theorem

For any active pre-singular interval:

$$
I,
$$

$$
\boxed{
\operatorname{Var}_I
\log\mathcal R_k
\le
\mathfrak V_k^{visc}(I)
+
\mathfrak V_k^{NL}(I).
}
$$

Therefore:

$$
\boxed{
\log\mathfrak T_k^{win}
\le
\mathfrak V_k^{visc}(I_k)
+
\mathfrak V_k^{NL}(I_k).
}
$$

### Consequence

If:

$$
\mathfrak T_k^{win}\ge T>1,
$$

then at least:

$$
\boxed{
\mathfrak V_k^{visc}
\ge
\frac12\log T
}
$$

or:

$$
\boxed{
\mathfrak V_k^{NL}
\ge
\frac12\log T.
}
$$

---

# 19. Root turnover is not a free temporal motif

Thus:

$$
\boxed{
\textbf{Within-Window Root Turnover}
}
$$

must be paid by:

## L-VISC

$$
\boxed{
D^{k+2}u\text{ viscous-order congestion};
}
$$

or:

## L-NL

$$
\boxed{
\text{projected nonlinear temporal forcing}.
}
$$

Therefore generic turnover can be removed as an independent category.

---

# 20. Bounded-turnover compactness

If:

$$
\boxed{
\sup_n
\left(
\mathfrak V_{k_n}^{visc}
+
\mathfrak V_{k_n}^{NL}
\right)
<\infty,
}
$$

normalize each theorem interval:

$$
I_{k_n}(t_n)
\to
[0,1].
$$

Define centered root path:

$$
\boxed{
y_n(\theta)
=
\log\mathcal R_{k_n}(s_n(\theta))
-
\log\mathcal R_{k_n}(s_n(0)).
}
$$

Then:

$$
\boxed{
\operatorname{Var}y_n
\le C.
}
$$

and:

$$
y_n(0)=0.
$$

Therefore:

$$
\boxed{
y_n
}
$$

is BV-compact in:

$$
L^1([0,1]).
$$

---

# 21. C5-L.5: Root-Path Compactness or Forcing Congestion

Every recurrent root-turnover sequence admits:

## L-RCOMP

bounded turnover toll:

$$
\Rightarrow
$$

BV-compact normalized root path;

or:

## L-RFORCE

$$
\boxed{
\mathfrak V_k^{visc}
+
\mathfrak V_k^{NL}
\to\infty.
}
$$

So root turnover is converted into:

$$
\boxed{
\text{compact path}
\vee
\text{PDE forcing congestion}.
}
$$

---

# 22. Published ascending-chain relation

Grujić–Xu Theorem 3.8 uses ascending-chain inequalities to control nonlinear derivative expansions over a high-order-dependent time scale.

This supports the interpretation that:

$$
\boxed{
\mathfrak V_k^{NL}
}
$$

should be studied together with:

$$
\boxed{
\mathcal R\text{-chain structure}.
}
$$

### Hard guard

C5-L does not claim Theorem 3.8 automatically bounds:

$$
\mathfrak V_k^{NL}
$$

as defined here.

A future direct identification requires matching its complexified/mild estimates and constants.

---

# 23. Chain-clock process across derivative order

At fixed base time:

$$
t,
$$

define:

$$
\boxed{
c_k^{clock}(t)
=
\log\tau_k(t).
}
$$

For finite derivative block:

$$
[J,K],
$$

define clock total variation:

$$
\boxed{
\mathfrak V_{J,K}^{clock}(t)
=
\sum_{k=J}^{K-1}
\left|
c_{k+1}^{clock}(t)
-
c_k^{clock}(t)
\right|.
}
$$

---

# 24. Clock range bound

Always:

$$
\boxed{
\max_{J\le k\le K}c_k^{clock}
-
\min_{J\le k\le K}c_k^{clock}
\le
\mathfrak V_{J,K}^{clock}.
}
$$

Therefore:

$$
\boxed{
\mathfrak V_{J,K}^{clock}\le\log4
}
$$

implies:

$$
\boxed{
\frac{
\max\tau_k
}{
\min\tau_k
}
\le4.
}
$$

By C5-K:

all theorem windows have a common time.

---

# 25. C5-L.6: Clock-Variation Synchronization Criterion

If:

$$
\boxed{
\mathfrak V_{J,K}^{clock}(t)
\le
\log4,
}
$$

then:

$$
\boxed{
\bigcap_{k=J}^{K}
I_k(t)
\ne\varnothing.
}
$$

Contrapositive:

$$
\boxed{
\bigcap_{k=J}^{K}
I_k(t)
=
\varnothing
\Rightarrow
\mathfrak V_{J,K}^{clock}(t)
>
\log4.
}
$$

### Meaning

No common theorem time requires a fixed positive amount of order-clock variation.

---

# 26. Exact clock/root decomposition

In one derivative section fix:

$$
c.
$$

Recall:

$$
\boxed{
A_k^{1/(k+1)}
=
c^{k/(k+1)}
(k!)^{1/(k+1)}
\mathcal R_k.
}
$$

Thus:

$$
\begin{aligned}
c_k^{clock}
&=
-\log\widetilde{\mathcal C}_k
-
\frac{2k}{k+1}\log c
-
\frac2{k+1}\log(k!)
-
2\log\mathcal R_k.
\end{aligned}
$$

Define deterministic/theorem normalization:

$$
\boxed{
g_k^{th}
=
-\log\widetilde{\mathcal C}_k
-
\frac{2k}{k+1}\log c
-
\frac2{k+1}\log(k!).
}
$$

Then:

$$
\boxed{
c_k^{clock}
=
g_k^{th}
-
2\log\mathcal R_k.
}
$$

---

# 27. Adjacent clock increment

Therefore:

$$
\boxed{
\Delta c_k^{clock}
=
\Delta g_k^{th}
-
2
\Delta\log\mathcal R_k,
}
$$

where:

$$
\Delta f_k=f_{k+1}-f_k.
$$

### Consequence

Chain-clock separation comes from:

$$
\boxed{
\text{order-root variation}
}
$$

and/or:

$$
\boxed{
\text{theorem/factorial normalization drift}.
}
$$

It is not an independent temporal coordinate.

---

# 28. Root vs theorem-constant clock defect

By triangle inequality:

$$
\boxed{
\mathfrak V_{J,K}^{clock}
\le
\mathfrak V_{J,K}^{th}
+
2
\mathfrak V_{J,K}^{root},
}
$$

where:

$$
\boxed{
\mathfrak V_{J,K}^{th}
=
\sum
|\Delta g_k^{th}|,
}
$$

$$
\boxed{
\mathfrak V_{J,K}^{root}
=
\sum
|
\Delta\log\mathcal R_k
|.
}
$$

Conversely:

$$
\boxed{
2\mathfrak V_{J,K}^{root}
\ge
\mathfrak V_{J,K}^{clock}
-
\mathfrak V_{J,K}^{th}.
}
$$

Thus if theorem-normalization drift is controlled and clocks desynchronize strongly,

order-root variation must be large.

---

# 29. Chain-clock defect measure

If:

$$
\mathfrak V_{J,K}^{clock}>0,
$$

define normalized order coordinate:

$$
\theta_k
=
\frac{
k-J
}{
K-J
}.
$$

Define probability measure:

$$
\boxed{
\mu_{J,K}^{clock}
=
\frac1{
\mathfrak V_{J,K}^{clock}
}
\sum_{k=J}^{K-1}
|
\Delta c_k^{clock}
|
\delta_{\theta_k}.
}
$$

Also compactify amplitude:

$$
\boxed{
a_{J,K}^{clock}
=
\frac{
\mathfrak V_{J,K}^{clock}
}{
1+\mathfrak V_{J,K}^{clock}
}
\in[0,1].
}
$$

If variation is zero use a fixed cemetery measure.

---

# 30. C5-L.7: Clock Defect Compactness

For recurrent derivative blocks:

$$
[J_n,K_n],
$$

the states:

$$
\boxed{
\left(
a_{J_n,K_n}^{clock},
\mu_{J_n,K_n}^{clock}
\right)
}
$$

admit subsequential compactification in:

$$
[0,1]
\times
\mathcal P([0,1]).
$$

### Interpretation

Clock separation becomes:

$$
\boxed{
\textbf{an order-space defect measure},
}
$$

not a collection of arbitrary unmatched times.

---

# 31. Factor-4 synchronized cluster decomposition

Given a clock sequence:

$$
c_J,\ldots,c_K,
$$

construct greedily:

- start at the leftmost order;
- extend the current contiguous order block as far as possible while its clock range stays:
  $$
  \le\log4;
  $$
- begin the next block at the following order.

Each resulting block has a common theorem time.

---

# 32. C5-L.8: Clock-Cluster Packing Lemma

Let:

$$
N_{sync}
$$

be the number of greedy factor-4 synchronized contiguous clusters.

Then:

$$
\boxed{
N_{sync}
\le
1+
\frac{
\mathfrak V_{J,K}^{clock}
}{
\log4
}.
}
$$

### Proof

Every completed cluster except the last ends because adding the next order makes the clock range exceed:

$$
\log4.
$$

The total variation on the corresponding disjoint edge segment must therefore exceed:

$$
\log4.
$$

Summing these disjoint variation costs gives the result. $\square$

---

# 33. Meaning of clock-cluster packing

If:

$$
\mathfrak V^{clock}
$$

is bounded,

a long derivative block can be partitioned into only finitely many common-time clusters.

Within each cluster:

- C5-I descent;
- C5-J order-sandwich;
- common-time Type-A puncture;

are all legally same-time.

If many synchronized clusters are needed,

then:

$$
\boxed{
\text{clock total variation must be large}.
}
$$

---

# 34. Clock critical saturation

A block may fail common-time condition but satisfy:

$$
\boxed{
\frac{
\max\tau_k
}{
\min\tau_k
}
\downarrow4
}
$$

from above.

This is:

$$
\boxed{
\textbf{Chain-Clock Critical Saturation}.
}
$$

But even at the critical factor:

$$
4,
$$

the corresponding adjacent/root-clock distortion is nontrivial.

So clock critical saturation is not automatically a zero-cost state either.

---

# 35. Root-clock jump at criticality

For adjacent orders:

$$
\frac{
\tau_{k+1}
}{
\tau_k
}
=
4
$$

implies:

$$
\boxed{
\frac{
A_{k+1}^{1/(k+2)}
}{
A_k^{1/(k+1)}
}
=
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

For ratio:

$$
1/4,
$$

the root factor is:

$$
\boxed{
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

Thus chain-clock boundary remains encoded in finite root geometry.

---

# 36. Persistent sign failure × bounded root turnover

Suppose:

$$
\mathsf W_k(t)=0
$$

and:

$$
\mathfrak V_k^{visc}
+
\mathfrak V_k^{NL}
\le C_0.
$$

Then normalized root path is BV compact,

while persistent descent gives:

$$
\boxed{
\mathcal R(k-1,c,s)
\ge
d_k
\mathcal R(k,c,s)
\quad
\forall s\in I_k(t).
}
$$

Therefore limit root paths satisfy the same pointwise/measure domination at continuity points / a.e. after subsequence.

This produces:

$$
\boxed{
\textbf{Persistent Bad-Window Limit Motif}.
}
$$

---

# 37. Persistent sign failure × unbounded turnover

If:

$$
\mathfrak V_k^{visc}
+
\mathfrak V_k^{NL}
\to\infty,
$$

the bad window cannot compactify as a tame root path.

But the failure is now charged to:

$$
\boxed{
\textbf{Viscous Two-Order Congestion}
}
$$

or:

$$
\boxed{
\textbf{Projected-Nonlinear Turnover}.
}
$$

So:

$$
\boxed{
\text{wild root motion}
}
$$

is no longer an untyped residual.

---

# 38. Persistent sign failure × clock synchronization

For a clock-synchronized derivative cluster:

$$
[J,K],
$$

if every level window persistently fails,

choose common:

$$
s_\ast.
$$

Then:

$$
\boxed{
\mathcal R(J,c,s_\ast)
\ge
\prod_{k=J+1}^{K}
d_k(c)
\,
\mathcal R(K,c,s_\ast).
}
$$

If line fragmentation is also present,

C5-J additionally forces local order curvature.

Thus synchronized persistent failure is a highly constrained same-time chain state.

---

# 39. Persistent sign failure × clock separation

If a derivative block cannot be synchronized,

C5-L records:

$$
\boxed{
\mathfrak V^{clock}>\log4
}
$$

and its defect measure:

$$
\mu^{clock}.
$$

Large clock variation must come from:

$$
\boxed{
\text{root order variation}
}
$$

or:

$$
\boxed{
\text{theorem-normalization drift}.
}
$$

Therefore:

$$
\boxed{
\text{clock separation}
}
$$

also ceases to be a free timing motif.

---

# 40. Theorem-setup residual

C5-K retained:

$$
\boxed{
\textbf{Theorem-Setup Defect}.
}
$$

Fresh audit shows Theorem 3.14 is invoked for temporal/order pairs satisfying:

- ascending-chain condition (3.8);
- parameter relation (3.9);
- initial/section size conditions;
- enough remaining time;
- theorem constants.

Published Definition 3.15 / Type-A/B machinery is designed to organize ascending/descending configurations,

but C5-L does not claim every C5 record event automatically satisfies every Theorem 3.14 antecedent.

So setup remains an explicit residual.

---

# 41. Setup failure should not be merged with spatial failure

Distinguish:

## L-SETUP

The theorem pair:

$$
(k,t)
$$

is not legally inside Theorem 3.14's setup.

## L-WINDOW

The setup is legal,

but:

$$
\boxed{
\forall s\in I_k(t),
\quad
\text{spatial sign gate fails}.
}
$$

These are logically different.

Only L-WINDOW receives the C5-I/K descent strip automatically.

---

# 42. Root-turnover critical saturation

A sequence may have:

$$
\mathfrak T_k^{win}\to T_\ast<\infty.
$$

Then it is BV-compact if turnover tolls bounded.

If:

$$
T_\ast=1,
$$

the root becomes asymptotically flat across the theorem window.

If:

$$
T_\ast>1,
$$

a nontrivial but finite root-turnover profile remains.

No new category is needed beyond the compact root path itself.

---

# 43. Root-turnover divergence

If:

$$
\mathfrak T_k^{win}\to\infty,
$$

then:

$$
\boxed{
\mathfrak V_k^{visc}
+
\mathfrak V_k^{NL}
\to\infty.
}
$$

Thus the old scalar:

$$
\boxed{
\text{ROOT-TURNOVER}
}
$$

can be removed as independent motif.

---

# 44. Harmonic critical saturation divergence does not occur

Unlike root turnover,

harmonic saturation:

$$
\beta^{win}\downarrow\delta
$$

is bounded.

Its importance is not amplitude divergence,

but proximity to the spatial sufficient criterion.

C5-L adds the key fact:

$$
\boxed{
\text{the associated descent toll stays uniformly positive}.
}
$$

So the boundary still constrains derivative order geometry.

---

# 45. Unified window defect state

For legal theorem pair:

$$
(k,t),
$$

define:

$$
\boxed{
\Theta_k^{L}(t)
=
\left\langle
\beta_k^{win},
\mu_{k-1}^{R},
\mu_k^{R},
\mathfrak V_k^{visc},
\mathfrak V_k^{NL},
y_k^{root},
\mathsf W_k
\right\rangle.
}
$$

For an order block add:

$$
\boxed{
\left(
a^{clock},
\mu^{clock},
N_{sync}
\right).
}
$$

---

# 46. Compactness after C5-L

Under bounded turnover tolls and compactified clock amplitudes:

- root paths are BV compact;
- root-load measures are weakly compact after mass compactification;
- clock defect measures are weakly compact;
- bad-window line profiles are compact under C5-J bounded roughness;
- harmonic occupancy is compact;
- carrier identity is unnecessary at the amplitude level.

Thus persistent high-order failure can be represented by a finite family of compact defect objects.

---

# 47. C5-L main compression theorem

## C5-L.9: Persistent Window Compression

For a legal Grujić–Xu theorem pair:

$$
(k,t),
$$

if the spatial gate fails throughout:

$$
I_k(t),
$$

then the event necessarily carries:

1. a nonvanishing lower-order descent strip;
2. a window derivative-$L^2$ load strip;
3. and either:
   - BV-compact root path;
   - viscous $k+2$ turnover congestion;
   - projected-nonlinear turnover congestion.

Carrier relay cannot remove items 1–2.

Harmonic critical saturation cannot make item 1 vanish.

---

# 48. C5-L block compression theorem

## C5-L.10: Clock/Descent Block Alternative

For a legal same-base derivative block:

$$
[J,K],
$$

with Window-Persistent Sign Defect at every required level,

either:

## L-BSYNC

the block can be partitioned into at most:

$$
\boxed{
1+
\mathfrak V_{J,K}^{clock}/\log4
}
$$

clock-synchronized contiguous clusters,

and within each cluster all C5-I/J same-time derivative constraints apply;

or:

## L-BCONG

$$
\boxed{
\mathfrak V_{J,K}^{clock}
}
$$

itself is large and recorded by a clock defect measure.

### Meaning

all-order timing failure reduces to:

$$
\boxed{
\text{few synchronized constrained clusters}
\vee
\text{order-clock variation congestion}.
}
$$

---

# 49. Residual after root-turnover compression

C5-K residual:

$$
\text{Window Sign}
\vee
\text{Clock}
\vee
\text{Turnover}
\vee
\text{Setup}.
$$

C5-L:

$$
\boxed{
\text{Turnover}
\to
\text{Viscous}
\vee
\text{Projected Nonlinear}
\vee
\text{Compact Root Path}.
}
$$

Clock:

$$
\boxed{
\text{Clock}
\to
\text{Root-Order Variation}
\vee
\text{Theorem-Normalization Drift}.
}
$$

Window sign:

$$
\boxed{
\text{Window Sign}
\to
\text{Persistent Descent}
+
\text{Derivative Load}.
}
$$

So the independent high-order motif count drops again.

---

# 50. What has been removed

After C5-L, the following are no longer free independent high-order survivor motifs:

$$
\boxed{
\text{Carrier Relay}
}
$$

at amplitude level;

$$
\boxed{
\text{Harmonic Critical Saturation}
}
$$

as zero-cost boundary;

$$
\boxed{
\text{Generic Root Turnover};
}
$$

$$
\boxed{
\text{Generic Clock Mismatch}.
}
$$

All have been routed into quantitative debts.

---

# 51. What still remains

## L-R1 — Persistent Spatial Sign-Window Debt

Still possible.

It now always carries descent/load debt.

## L-R2 — Viscous High-Order Turnover

$$
\mathfrak V_k^{visc}
$$

may be large.

## L-R3 — Projected Nonlinear Turnover

$$
\mathfrak V_k^{NL}
$$

may be large.

## L-R4 — Order-Clock Variation / Theorem Constant Drift

may remain large.

## L-R5 — Theorem-Setup Defect

still logically external to the spatial pass/fail question.

These are the true remaining high-order interfaces.

---

# 52. Relation to earlier C5 defects

C5-D/F pressure-axis defects,

C5-E middle-gap/vorticity defects,

and C5-G pressure-signature defects remain part of the global C5 state.

But the high-order derivative branch itself has now been reduced to:

$$
\boxed{
\text{persistent sign-window forcing}
+
\text{clock/forcing/setup interfaces}.
}
$$

This is sufficiently compressed for a global C5 phase audit.

---

# 53. C5-L methodological result

The main methodological conclusion:

> Once a published sufficient criterion has an existential time quantifier over an interval,
> the correct survivor is not "time mismatch";
> it is **persistent failure over the entire admissible interval**.

And once such persistent failure is identified,

its consequences should be integrated over the window,

not treated as isolated pulses.

This turns:

$$
\boxed{
\text{timing ambiguity}
}
$$

into:

$$
\boxed{
\text{window-level PDE debt}.
}
$$

---

# 54. Major no-go audit

### NG-L1

$$
\text{moving bad carrier}
\Rightarrow
\text{descent strip disappears}.
$$

FALSE.

### NG-L2

$$
\beta^{win}\downarrow\delta
\Rightarrow
\text{descent coefficient}\to0.
$$

FALSE.

### NG-L3

$$
\text{root turnover can diverge without temporal forcing}.
$$

FALSE.

### NG-L4

$$
\text{no common theorem time}
\Rightarrow
\text{unstructured timing defect}.
$$

FALSE; clock total variation must exceed $\log4$.

### NG-L5

$$
\text{clock variation}
\text{ is independent of derivative-root geometry}.
$$

FALSE; exact clock/root decomposition holds.

### NG-L6

$$
\text{bounded clock variation}
\Rightarrow
\text{one common time for an arbitrarily long block}.
$$

Only if the total variation/range is $\le\log4$.

For larger bounded variation one obtains finitely many synchronized clusters.

### NG-L7

$$
\text{Theorem-Setup Defect}
=
\text{Spatial Sign Defect}.
$$

FALSE.

---

# 55. X-Integration guards update

## G-CARRIERQ

bad-carrier identity can be quotiented only for global amplitude/load consequences, not for local pressure/ancestry geometry.

## G-WROOTMEAS

persistent failure should preserve root-load measure domination.

## G-LOGA

root-turnover log estimates require $A_k>0$ on the active interval.

## G-PROJNL

keep the actual projected nonlinear source norm; do not replace it with an invalid $L^\infty$ Riesz estimate.

## G-CLOCKTV

clock mismatch is tracked by order total variation, not only endpoint spread.

## G-CLOCKTH

separate theorem/factorial clock drift from derivative-root variation.

## G-SETUP2

theorem setup remains a separate gate.

---

# 56. True ETN update

New edges:

$$
\boxed{
\text{WINDOW-FAIL}
\longrightarrow
\text{ROOT-MEASURE DOMINATION},
}
$$

$$
\boxed{
\text{WINDOW-FAIL}
\longrightarrow
\text{DERIVATIVE-LOAD STRIP},
}
$$

$$
\boxed{
\text{ROOT-TURNOVER}
\longrightarrow
D^{k+2}\text{-VISC}
\vee
\text{PROJECTED-NL},
}
$$

$$
\boxed{
\text{CLOCK-SEPARATION}
\longrightarrow
\text{ORDER-CLOCK VARIATION},
}
$$

$$
\boxed{
\text{ORDER-CLOCK VARIATION}
\longrightarrow
\text{ROOT-ORDER VARIATION}
\vee
\text{THEOREM-CONSTANT DRIFT}.
}
$$

---

# 57. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal oscillation/concentration}.
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
Q\to
\text{gap/derivative/vorticity}.
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
\text{published dynamic time/switch stitching audit}.
$$

C5-L:

$$
\boxed{
\textbf{persistent theorem-window failure becomes a carrier-free derivative debt;
root turnover and clock mismatch are compressed into PDE/order-space forcing defects}.
}
$$

---

# 58. New frontier: C5-M

At this point C5 has enough compressed residuals for a global phase audit.

The next natural paper:

$$
\boxed{
\textbf{C5-M — Unified Defect-State Closure,
Compatibility Graph Audit, and C5 Phase Boundary}.
}
$$

---

# 59. C5-M proof obligations

## M1 — Unified residual list

Collect only genuinely independent remaining motifs after C5-A–L.

## M2 — Remove routed pseudo-defects

Explicitly delete:

- generic turnover;
- generic fragmentation;
- Type switching;
- carrier relay at amplitude level;
- free Seven-Point cancellation;
- generic time mismatch.

## M3 — Compatibility graph

Build directed graph among:

- persistent sign windows;
- viscous/nonlinear forcing;
- middle-gap/vorticity;
- pressure signature/axis;
- theorem setup;
- clock normalization defects.

## M4 — Recurrent-cycle audit

Check whether any closed recurrent compensation cycle remains without revisiting an already quantified debt.

## M5 — External theorem gates

Mark precisely which nodes are killed by:

- Miller middle/operator criteria;
- Grujić–Xu Theorem 3.5;
- Grujić–Xu Theorem 3.14;
- pressure criteria.

## M6 — Conditional vs unconditional edges

Separate C3-G ancestry assumptions from unconditional N–S identities.

## M7 — C5 closure criterion

Decide whether C5's task:

$$
\text{motif compactification + compatibility reduction}
$$

is complete.

## M8 — C6 target

If C5 closes,

define the next phase around the remaining unified recurrent defect cycle rather than adding another local estimate.

---

# 60. Formal Status

$$
\boxed{
\begin{aligned}
\text{carrier relay removes descent debt}
&:\ \mathrm{FALSE},\\
\text{window root-measure domination}
&:\ \mathrm{PROVED},\\
\text{window derivative-load strip}
&:\ \mathrm{PROVED},\\
\text{critical harmonic saturation has zero descent cost}
&:\ \mathrm{FALSE},\\
\text{root-turnover PDE bound}
&:\ \mathrm{PROVED},\\
\text{unbounded turnover}\Rightarrow
\text{viscous or projected-NL toll}
&:\ \mathrm{PROVED},\\
\text{bounded turnover}\Rightarrow
\text{BV root-path compactness}
&:\ \mathrm{PROVED},\\
\text{clock-TV}\le\log4
\Rightarrow
\text{common theorem time}
&:\ \mathrm{PROVED},\\
\text{clock defect measure compactness}
&:\ \mathrm{PROVED},\\
\text{clock-cluster packing}
&:\ \mathrm{PROVED},\\
\text{generic root turnover as independent motif}
&:\ \mathrm{REMOVED},\\
\text{generic clock mismatch as independent motif}
&:\ \mathrm{REMOVED},\\
\text{theorem setup automatic}
&:\ \mathrm{NOT\ PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 61. Conclusion

C5-K rewrote the true spatial survivor as:

$$
\boxed{
\text{Window-Persistent Sign Defect}.
}
$$

C5-L now proves:

First,

even if a bad carrier relays arbitrarily within the theorem window,

it must still pay at every time:

$$
\boxed{
A_{k-1}
\gtrsim
A_k^{k/(k+1)}.
}
$$

Therefore, carrier identity cannot eliminate the derivative debt.

Second,

even if the harmonic threshold is asymptotically adhered to:

$$
\beta^{win}\downarrow\delta,
$$

the descent coefficient remains:

$$
\boxed{
(1+\lambda)\delta-1>0.
}
$$

Thus, harmonic critical saturation is not a zero-cost escape.

Third,

within-window root turnover is constrained by the true N–S time evolution:

$$
\boxed{
\operatorname{Var}
\log\mathcal R_k
\le
\frac1{k+1}
\int
\frac{
C\nu A_{k+2}
+
\mathcal N_k^{proj}
}{
A_k
}.
}
$$

So wild turnover must imply:

$$
\boxed{
D^{k+2}u\text{ viscous congestion}
\vee
\text{projected nonlinear forcing}.
}
$$

If these forcing tolls are bounded,

the root path is instead BV compact.

Fourth,

the mismatch of chain clocks:

$$
\tau_k
=
[
\widetilde{\mathcal C}_k
A_k^{2/(k+1)}
]^{-1}
$$

can also be compressed into the order total variation:

$$
\boxed{
\mathfrak V^{clock}
=
\sum
|\Delta\log\tau_k|.
}
$$

If:

$$
\mathfrak V^{clock}\le\log4,
$$

the entire block must have a common theorem time.

If many factor-4 synchronized clusters are needed,

every additional cluster must consume clock variation.

Finally, the clock itself is exact:

$$
\boxed{
\log\tau_k
=
g_k^{th}
-
2\log\mathcal R_k.
}
$$

Therefore:

$$
\boxed{
\text{Clock Defect}
=
\text{Root-Order Variation}
+
\text{Theorem-Normalization Drift}.
}
$$

At this point,

the high-order timing/spatial residuals of C5 have been compressed from many seemingly different escapes

into a truly small number of PDE/order-space debts.

Formally, the next paper is:

$$
\boxed{
\textbf{C5-M — Unified Defect-State Closure,
Compatibility Graph Audit, and C5 Phase Boundary}.
}
$$

---

# References

1. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
2. H. Dong, Q. S. Zhang, *Time analyticity for the heat equation and Navier–Stokes equations*, arXiv:1907.01687.
3. C. Wang, Y. Gao, X. Xue, *Joint space-time analyticity of mild solutions to the Navier–Stokes equations*, arXiv:2112.03079.

# Internal dependencies

- `NS_C5K_ChainTime_WindowPersistent_DynamicInterpolationAudit_v0.1.md`
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
\textbf{C5-M — Unified Defect-State Closure,
Compatibility Graph Audit, and C5 Phase Boundary}
}
$$