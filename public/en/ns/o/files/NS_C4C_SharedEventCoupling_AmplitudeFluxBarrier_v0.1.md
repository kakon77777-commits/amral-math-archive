---
title: "Navier–Stokes C4-C: Carrier Relay, Shared-Event Coupling, and Amplitude-to-Flux Barrier"
subtitle: "Exact Same-Event Couplings for Helical Triads, Local Strain Growth, Pressure Rotation, and Operator Sources — and the Remaining Barrier from Critical Amplitude to Energy Flux"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style shared-event closure graph / structural reduction"
epistemic_status: "Exact finite-dimensional triad algebra + exact local strain identities + operator triangle decompositions + explicit information no-go. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C4-C
# Carrier Relay, Shared-Event Coupling, and Amplitude-to-Flux Barrier

## 0. Positioning of this Round

C4-B has proven:

$$
\boxed{
\text{generic turnover cost is insufficient to force temporal synchronization}.
}
$$

The survivor can utilize:

- Pulse Capacity;
- Carrier Relay;
- Inter-Generation Routing;
- Summable Weights;

to keep different mandatory channels continuously asynchronous.

Therefore, the C4 strategy is shifted to:

$$
\boxed{
\textbf{Shared-Event Synchronization}.
}
$$

That is, instead of asking:

> Can A and B recur separately?

we ask:

> Does there exist a genuine N–S event whose same source / same balance / same triad algebra already forces A and B to be paid simultaneously?

This round audits four sets of couplings:

1. UV high-mode energy gain ↔ critical helical pair production;
2. UV amplitude ↔ strain / helicity critical stock;
3. local strain growth ↔ SSA / Betchov / pressure / vortex stretching;
4. Miller operator escape ↔ advection / strain-square / vorticity-quadratic operator sources.

Main results:

$$
\boxed{
\text{Shared-event edges indeed exist,
but they are currently branching edges, not single-path implications.}
}
$$

The most critical new gap among them is:

$$
\boxed{
\textbf{critical amplitude}
\not\Rightarrow
\textbf{positive energy flux}.
}
$$

Thus, the first-crossing UV anchor of C1/C3-G cannot yet be directly connected to the helical triad energy-transfer algebra.

---

# 1. Fresh primary-source audit

This round of fresh audit uses the following primary sources.

## Waleffe 1992

Helical decomposition splits each Fourier wavevector into two helicity eigenmodes,

and triadic interactions are divided into different energy-transfer classes based on helical signs.

The original analysis shows:

- Different helicity combinations have different forward / reverse transfer tendencies;
- The transfer properties of local and nonlocal triads are different;
- The helical sign structure of a single triad possesses genuine dynamical content.

## Lei–Lin–Zhou 2015

A critical helical energy identity exists for the 3D incompressible N–S equations.

This is the external anchor for the C3-A/B critical helical stock / pair-production architecture.

## Biferale–Titi 2013

The single-helicity-sign decimated N–S is globally regular because the sign-definite helicity provides critical positive control.

It demonstrates that the homochiral / sign-definite helical structure is indeed fundamentally different from the heterochiral pair-production problem in the full N–S equations.

## Miller 2024/2026

The strain–vorticity interaction model and the full N–S operator decomposition provide an operator-level source classification.

## Cheskidov–Dai 2015

The frequency-localized critical vorticity toll provides a UV regularity interface.

---

# 2. Shared-event edge

Define an event:

$$
\mathcal E
$$

and two channel loads:

$$
L^A,
\qquad
L^B.
$$

If we can prove:

$$
\boxed{
\mathcal E
\Rightarrow
L^A\ge a_0
}
$$

and:

$$
\boxed{
\mathcal E
\Rightarrow
L^B\ge b_0,
}
$$

and both are:

- At the same time;
- At the same scale;
- On the same carrier / bounded cluster;

then we call:

$$
\boxed{
A
\stackrel{\mathcal E}{\Longleftrightarrow}
B
}
$$

a strong shared-event coupling.

---

# 3. Branching shared-event edge

More generally:

$$
\boxed{
\mathcal E
\Rightarrow
B_1\vee B_2\vee\cdots\vee B_m.
}
$$

This is still valuable.

Because although carrier relay can switch carriers,

it cannot cause:

$$
\boxed{
\text{all algebraic outcomes of the same event completely disappear}.
}
$$

The C4 closure graph therefore allows:

$$
\boxed{
\textbf{branching edges}.
}
$$

---

# 4. Helical triad algebra

Consider a single Fourier triad:

$$
k\le p\le q,
$$

modal energies:

$$
e_k,e_p,e_q,
$$

helicity signs:

$$
s_k,s_p,s_q\in\{\pm1\}.
$$

energy conservation:

$$
\dot e_k+\dot e_p+\dot e_q=0.
$$

helicity conservation:

$$
s_kk\dot e_k
+
s_pp\dot e_p
+
s_qq\dot e_q
=
0.
$$

Therefore, the derivative vector must be:

$$
\boxed{
(\dot e_k,\dot e_p,\dot e_q)
=
\Theta_\tau
\left(
s_pp-s_qq,\ 
s_qq-s_kk,\ 
s_kk-s_pp
\right).
}
$$

This equation only uses single-triad energy/helicity conservation.

---

# 5. Helical classes

Fix the smallest mode sign as:

$$
+.
$$

A global sign flip does not change the following magnitude relations.

Four classes:

$$
\begin{array}{c|c}
\mathrm{I}&(+++)\\
\mathrm{II}&(+--)\\
\mathrm{III}&(+-+)\\
\mathrm{IV}&(++-)
\end{array}
$$

Class I is homochiral.

Classes II–IV are heterochiral.

---

# 6. Critical pair production

Following C3-B:

homochiral:

$$
\boxed{
\mathcal R_\tau=0.
}
$$

heterochiral unique-sign identity:

$$
\boxed{
\mathcal R_\tau
=
r_\tau
\dot e_{\rm uniq}.
}
$$

Specifically:

$$
\boxed{
\mathcal R_{II}
=
k(q-p)\Theta,
}
$$

$$
\boxed{
\mathcal R_{III}
=
p(q-k)\Theta,
}
$$

$$
\boxed{
\mathcal R_{IV}
=
q(k-p)\Theta.
}
$$

---

# 7. Highest-mode energy gain

Define the critical-weighted high-mode gain:

$$
\boxed{
G_\tau^q
=
q[\dot e_q]_+.
}
$$

Only consider:

$$
\dot e_q>0.
$$

---

# 8. C4-C.1: Highest-Mode Gain / Pair-Production Table

## Class I — Homochiral

$$
\dot e_q
=
(k-p)\Theta.
$$

high-mode gain requires:

$$
\Theta<0.
$$

In this case:

$$
\boxed{
G_I^q
=
q(p-k)|\Theta|,
}
$$

But:

$$
\boxed{
\mathcal R_I=0.
}
$$

Therefore:

$$
\boxed{
\text{high-mode energy gain can be helicity-pair-production silent}.
}
$$

---

## Class II

$$
\dot e_q
=
(k+p)\Theta.
$$

high-mode gain:

$$
\Theta>0.
$$

pair production:

$$
\mathcal R_{II}
=
k(q-p)\Theta>0.
$$

Therefore:

$$
\boxed{
\frac{
\mathcal R_{II}
}{
G_{II}^q
}
=
\frac{
k(q-p)
}{
q(k+p)
}.
}
$$

---

## Class III

$$
\dot e_q
=
(k+p)\Theta.
$$

high-mode gain:

$$
\Theta>0.
$$

pair production:

$$
\mathcal R_{III}
=
p(q-k)\Theta>0.
$$

Therefore:

$$
\boxed{
\frac{
\mathcal R_{III}
}{
G_{III}^q
}
=
\frac{
p(q-k)
}{
q(k+p)
}.
}
$$

---

## Class IV

$$
\dot e_q
=
(k-p)\Theta.
$$

high-mode gain requires:

$$
\Theta<0.
$$

Then:

$$
\mathcal R_{IV}
=
q(p-k)|\Theta|.
$$

And:

$$
G_{IV}^q
=
q(p-k)|\Theta|.
$$

Therefore:

$$
\boxed{
\mathcal R_{IV}
=
G_{IV}^q.
}
$$

Class IV is an exact perfect critical coupling.

---

# 9. C4-C.2: Heterochiral High-Mode Gain is Positive Pair Production

From §8:

For all heterochiral classes II–IV,

as long as:

$$
\dot e_q>0,
$$

we have:

$$
\boxed{
\mathcal R_\tau>0.
}
$$

Therefore:

$$
\boxed{
\text{heterochiral highest-mode energy gain}
\Rightarrow
\text{positive critical pair production}
}
$$

holds at the single-triad level.

But the coupling strength can degenerate.

---

# 10. Radial gap degeneration

Class II coupling:

$$
\kappa_{II}
=
\frac{
k(q-p)
}{
q(k+p)
}.
$$

If:

$$
q-p\to0,
$$

then:

$$
\boxed{
\kappa_{II}\to0.
}
$$

Class III:

$$
\kappa_{III}
=
\frac{
p(q-k)
}{
q(k+p)
}.
$$

If:

$$
q-k\to0,
$$

then:

$$
\boxed{
\kappa_{III}\to0.
}
$$

Therefore:

$$
\boxed{
\text{heterochiral}
}
$$

itself is still insufficient to provide a universal positive lower coupling constant.

---

# 11. Robust local gap regime

Assume a local comparable triad:

$$
\boxed{
k,p\ge c_Lq
}
$$

for:

$$
c_L>0.
$$

And for II:

$$
\boxed{
q-p\ge\delta q.
}
$$

Then:

$$
\kappa_{II}
\ge
\frac{
c_L\delta
}{2}.
$$

For III, if:

$$
q-k\ge\delta q,
$$

similarly:

$$
\boxed{
\kappa_{III}
\ge
\frac{
c_L\delta
}{2}.
}
$$

IV:

$$
\boxed{
\kappa_{IV}=1.
}
$$

---

# 12. C4-C.3: Robust Heterochiral Shared-Event Coupling

If a highest-mode gain event is carried by:

- Class IV;
- Or local Class II/III with a radial gap:
  $$
  \ge\delta q
  $$

triads,

then:

$$
\boxed{
\mathcal R_\tau
\ge
c(c_L,\delta)
G_\tau^q.
}
$$

This is a genuine same-triad / same-time shared-event edge.

---

# 13. Aggregate positive-gain decomposition

Work first in a finite Galerkin truncation.

Fix a high shell / high mode family,

sum the:

$$
G_\tau^q
$$

of all triads with:

$$
\dot e_q>0
$$

:

$$
\boxed{
G^+
=
G_{\rm hom}
+
G_{\rm deg}
+
G_{\rm rob}.
}
$$

Where:

## Homochiral

Class I.

## Degenerate heterochiral

Class II/III but with a radial gap less than:

$$
\delta q.
$$

## Robust heterochiral

The remaining heterochiral positive-gain triads.

---

# 14. Positive pair-production variation

Define the triadwise positive helical variation:

$$
\boxed{
P_+
=
\sum_\tau
[\mathcal R_\tau]_+.
}
$$

From robust coupling:

$$
\boxed{
P_+
\ge
c(c_L,\delta)
G_{\rm rob}.
}
$$

---

# 15. Net helical pair production

Define:

$$
\boxed{
P_-
=
\sum_\tau
[-\mathcal R_\tau]_+.
}
$$

global net:

$$
\boxed{
\mathcal R_{\rm net}
=
P_+-P_-.
}
$$

Therefore, robust positive pair production can still be cancelled by simultaneous negative triads.

---

# 16. C4-C.4: Robust-Gain Helical Cancellation Dichotomy

Fix:

$$
0<\eta<1.
$$

If:

$$
G_{\rm rob}>0,
$$

then at least:

## Net-helicity branch

$$
\boxed{
[\mathcal R_{\rm net}]_+
\ge
\eta
c
G_{\rm rob},
}
$$

or:

## Cancellation branch

$$
\boxed{
P_-
\ge
(1-\eta)
c
G_{\rm rob}.
}
$$

### Proof

If the first inequality fails,

$$
P_+-P_-
<
\eta cG_{\rm rob}.
$$

And:

$$
P_+\ge cG_{\rm rob}.
$$

Therefore:

$$
P_-
>
(1-\eta)cG_{\rm rob}.
$$

$\square$

---

# 17. UV energy-gain shared-event trichotomy

Therefore, for a large high-mode gain:

$$
G^+\ge G_0
$$

If the robust component does not occupy a fixed fraction,

the event must primarily fall into:

$$
\boxed{
G_{\rm hom}
+
G_{\rm deg}.
}
$$

If the robust component occupies a fixed fraction,

then §16 gives helical variation / cancellation.

Therefore:

$$
\boxed{
\textbf{High-Mode Energy Gain}
}
$$

forces:

$$
\boxed{
\text{Homochiral Carrier}
\ \vee\
\text{Radial-Gap Degeneration}
\ \vee\
\text{Positive Helical Net Production}
\ \vee\
\text{Helical Cancellation}.
}
$$

This is the first genuine N–S helical shared-event branching edge in C4.

---

# 18. Why does the Waleffe structure support this classification?

Waleffe's helical triad analysis inherently shows:

- Helical sign combinations change the direction of energy transfer;
- Local / nonlocal geometry changes transfer efficiency;
- 3D forward transfer is closely related to heterochiral structure;
- Certain classes can exhibit reverse / near-cancelling transfer.

The table in C4-C does not use turbulence statistical assumptions.

It only uses single-triad conservation algebra,

and is therefore a deterministic finite-mode identity.

---

# 19. But the UV anchor of C1/C3-G is not energy gain

This is the most important guard of this round.

The nonlinear replenishment in C1 is:

$$
\boxed{
\left\|
\int
e^{\nu(t-s)\Delta}
P_{>J}
\mathbb P\nabla\cdot(u\otimes u)\,ds
\right\|_3
}
$$

being large.

C3-G first crossing controls:

$$
\boxed{
a_q^\sigma
=
\frac{
\|u_q^\sigma\|_\infty
}{
\nu\lambda_q
}.
}
$$

These are:

$$
\boxed{
\text{amplitude / norm events}.
}
$$

While §8–17 are:

$$
\boxed{
\text{modal energy derivative / flux events}.
}
$$

The two cannot be directly equated.

---

# 20. C4-C.5: Phase-Rearrangement Norm–Flux No-Go

Consider within the same dyadic shell:

$$
N
$$

divergence-free Fourier/helical modes:

$$
h_m
e^{ik_m\cdot x}.
$$

Let:

$$
u_\theta(x)
=
\sum_{m=1}^{N}
a_m
h_m
e^{i(k_m\cdot x+\theta_m)}.
$$

Keep:

$$
|a_m|
$$

all fixed,

and only change the phases:

$$
\theta_m.
$$

Then Parseval gives:

$$
\boxed{
\|u_\theta\|_2
\text{ is independent of phase}.
}
$$

But:

$$
\boxed{
\|u_\theta\|_\infty
}
$$

can, due to phases being:

- aligned;
- cancelling;

vary significantly.

Therefore, there exists a smooth phase path:

$$
\theta(t)
$$

such that:

$$
\boxed{
\frac d{dt}
\|u_{\theta(t)}\|_2^2=0
}
$$

but:

$$
\boxed{
\|u_{\theta(t)}\|_\infty
}
$$

increases.

### Status

This is not a Navier–Stokes solution construction.

It proves:

$$
\boxed{
\text{amplitude information alone
cannot algebraically determine the shell energy flux sign}.
}
$$

---

# 21. Amplitude-to-Flux Barrier

Therefore:

$$
\boxed{
a_q^\sigma\uparrow
}
$$

or:

$$
\boxed{
\|P_{>J}u\|_3\uparrow
}
$$

cannot deduce, relying solely on norm algebra:

$$
\boxed{
\dot e_q>0
}
$$

or:

$$
\boxed{
\Phi_q>0.
}
$$

So we cannot yet write:

$$
\boxed{
\text{C1 UV replenishment}
\Rightarrow
\text{C4-C helical shared-event}.
}
$$

What is truly missing is:

$$
\boxed{
\textbf{Amplitude-to-Flux Bridge}.
}
$$

---

# 22. Static UV amplitude can still synchronize critical stock

Although amplitude does not control flux,

it can control the same-time shell stock.

If:

$$
a_q^\sigma
\ge
\beta,
$$

then:

$$
\|u_q^\sigma\|_\infty
\ge
\nu\beta\lambda_q.
$$

Bernstein:

$$
\|u_q^\sigma\|_\infty
\le
C
\lambda_q^{3/2}
\|u_q^\sigma\|_2.
$$

Therefore:

$$
\boxed{
\|u_q^\sigma\|_2^2
\ge
c
\nu^2
\beta^2
\lambda_q^{-1}.
}
$$

---

# 23. C4-C.6: UV Amplitude → Critical Helical Stock

helical critical shell stock:

$$
\boxed{
H_{q,\sigma}
=
\lambda_q
\|u_q^\sigma\|_2^2.
}
$$

Therefore:

$$
\boxed{
a_q^\sigma\ge\beta
\Rightarrow
\frac{
H_{q,\sigma}
}{
\nu^2
}
\ge
c\beta^2.
}
$$

This is an exact same-time shared-state edge:

$$
\boxed{
\text{UV critical amplitude}
\Rightarrow
\text{critical helical stock}.
}
$$

Note:

$$
\boxed{
\text{stock}
\neq
\text{pair-production rate}.
}
$$

---

# 24. C4-C.7: UV Amplitude → Strain/Vorticity Stock

annular support:

$$
|\xi|\sim\lambda_q.
$$

For a divergence-free shell:

$$
\|\nabla u_q^\sigma\|_2^2
\asymp
\lambda_q^2
\|u_q^\sigma\|_2^2.
$$

and:

$$
\|S_q^\sigma\|_2^2
\asymp
\|\nabla u_q^\sigma\|_2^2,
$$

$$
\|\omega_q^\sigma\|_2^2
\asymp
\|\nabla u_q^\sigma\|_2^2.
$$

Therefore:

$$
\boxed{
\|S_q^\sigma\|_2^2
+
\|\omega_q^\sigma\|_2^2
\ge
c
\nu^2
\beta^2
\lambda_q.
}
$$

Let:

$$
R_q=\lambda_q^{-1}.
$$

Then normalized:

$$
\boxed{
\frac{
R_q
}{
\nu^2
}
\|S_q^\sigma\|_2^2
\ge
c\beta^2,
}
$$

and:

$$
\boxed{
\frac{
R_q
}{
\nu^2
}
\|\omega_q^\sigma\|_2^2
\ge
c\beta^2.
}
$$

---

# 25. Static shared-event edge

Therefore, the first-crossing UV amplitude event synchronizes at least:

$$
\boxed{
\text{helical critical stock}
+
\text{strain stock}
+
\text{vorticity stock}.
}
$$

This is the first very important non-asynchronous edge in C4.

But it is still only:

$$
\boxed{
\textbf{stock synchronization},
}
$$

not:

$$
\boxed{
\textbf{production synchronization}.
}
$$

---

# 26. Carrier relay stock toll

Every new high-frequency carrier:

$$
(q_n,\sigma_n)
$$

if it reaches:

$$
a_{q_n}^{\sigma_n}\ge\beta,
$$

carries:

$$
\boxed{
O(1)
}
$$

normalized critical helical / strain / vorticity stock.

But the ordinary kinetic energy cost is only:

$$
O(\lambda_{q_n}^{-1}).
$$

geometric:

$$
\sum_n
\lambda_{q_n}^{-1}
<
\infty.
$$

Therefore:

$$
\boxed{
\text{new-carrier creation has critical stock toll,
but not a finite unweighted energy contradiction}.
}
$$

Carrier Relay can still survive.

---

# 27. Local strain growth edge

Return to the C3-O adjoint cutoff.

Define:

$$
E_\chi'
+
D_\chi
=
A_\chi
+
B_\chi^B
+
B_\chi^P,
$$

where:

$$
A_\chi
=
-2
\int\chi\det S,
$$

$$
B_\chi^B
=
\frac13
\int
\nabla\chi\cdot F_B,
$$

$$
B_\chi^P
=
\int
\nabla\chi\cdot F_p.
$$

Let:

$$
\boxed{
G_\chi
=
E_\chi'
+
D_\chi.
}
$$

---

# 28. C4-C.8: Local Strain-Growth Shared-Event Trichotomy

## Theorem 28.1

If:

$$
\boxed{
G_\chi\ge g>0,
}
$$

then at least:

$$
\boxed{
A_\chi
\ge
\frac g3,
}
$$

or:

$$
\boxed{
B_\chi^B
\ge
\frac g3,
}
$$

or:

$$
\boxed{
B_\chi^P
\ge
\frac g3.
}
$$

### Proof

The sum of the three is:

$$
G_\chi.
$$

If each is less than:

$$
g/3,
$$

the sum is less than:

$$
g.
$$

Contradiction. $\square$

---

# 29. Exact local Betchov relation

C3-N:

$$
\int
\chi
\left(
\omega\cdot S\omega
+
4\det S
\right)
=
-\frac43
\int
\nabla\chi\cdot F_B.
$$

Define local vortex stretching:

$$
\boxed{
V_\chi
=
\int
\chi
\omega\cdot S\omega.
}
$$

Since:

$$
A_\chi
=
-2\int\chi\det S,
$$

and:

$$
B_\chi^B
=
\frac13
\int\nabla\chi\cdot F_B,
$$

we obtain:

$$
\boxed{
V_\chi
=
2A_\chi
-
4B_\chi^B.
}
$$

---

# 30. C4-C.9: SSA → Vortex-Stretching / Betchov-Current Dichotomy

If:

$$
A_\chi\ge a>0,
$$

then at least:

$$
\boxed{
|B_\chi^B|
\ge
\frac a4,
}
$$

or:

$$
\boxed{
V_\chi\ge a.
}
$$

### Proof

If:

$$
|B_\chi^B|<a/4,
$$

then:

$$
V_\chi
=
2A_\chi-4B_\chi^B
>
2a-a
=
a.
$$

$\square$

---

# 31. C4-C.10: Strain Growth Forces Pressure / Betchov / Vortex Stretching

Combining §28–30:

If:

$$
G_\chi\ge g>0,
$$

then at least:

$$
\boxed{
B_\chi^P
\ge
\frac g3,
}
$$

or:

$$
\boxed{
|B_\chi^B|
\ge
\frac{
g
}{
12
},
}
$$

or:

$$
\boxed{
V_\chi
\ge
\frac g3.
}
$$

Therefore:

$$
\boxed{
\textbf{positive local strain-growth event}
}
$$

cannot be completely asynchronous.

The same event must synchronize:

$$
\boxed{
\text{pressure current}
\ \vee\
\text{Betchov current}
\ \vee\
\text{positive vortex stretching}.
}
$$

This is one of the cleanest same-core shared-event branching edges in C4 so far.

---

# 32. Vortex-stretching geometry

pointwise:

$$
[\omega\cdot S\omega]_+
\le
\lambda_2^+
|\omega|^2
+
\sqrt2
|S|
|\xi\cdot e_3|^2
|\omega|^2.
$$

If:

$$
V_\chi\ge v>0,
$$

then:

$$
\int
\chi
[\omega\cdot S\omega]_+
\ge
v.
$$

Therefore at least:

$$
\boxed{
\int
\chi
\lambda_2^+
|\omega|^2
\ge
\frac v2,
}
$$

or:

$$
\boxed{
\int
\chi
|S|
|\xi\cdot e_3|^2
|\omega|^2
\ge
\frac{
v
}{
2\sqrt2
}.
}
$$

---

# 33. C4-C.11: Strain-Growth Geometry Edge

Therefore:

$$
\boxed{
G_\chi\ge g
}
$$

forces the same local event to enter at least:

$$
\boxed{
\text{Pressure}
}
$$

or:

$$
\boxed{
\text{Betchov Boundary}
}
$$

or:

$$
\boxed{
\text{Middle-Strain Weighted Vorticity}
}
$$

or:

$$
\boxed{
\text{Principal-Alignment Weighted Vorticity}.
}
$$

This is the first multi-step exact local edge in the C4 closure graph.

---

# 34. Pressure-active event

adjoint mean-strain transport:

$$
M_\chi'
=
-
Q_\chi
-
P_\chi,
$$

where:

$$
\boxed{
Q_\chi
=
\int
\chi
\left[
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
\right]dx,
}
$$

$$
\boxed{
P_\chi
=
\int
\chi
\nabla^2p\,dx.
}
$$

---

# 35. C4-C.12: Pressure → Mean-Rotation / Quadratic-Cancellation Edge

If:

$$
\boxed{
|P_\chi|\ge p_0,
}
$$

then:

$$
|M_\chi'|
+
|Q_\chi|
\ge
|P_\chi|.
$$

Therefore:

$$
\boxed{
|M_\chi'|
\ge
\frac{
p_0
}{2}
}
$$

or:

$$
\boxed{
|Q_\chi|
\ge
\frac{
p_0
}{2}.
}
$$

Therefore:

$$
\boxed{
\textbf{pressure-active event}
}
$$

simultaneously forces:

$$
\boxed{
\text{mean-strain rotation}
\ \vee\
\text{quadratic strain/vorticity cancellation}.
}
$$

---

# 36. Miller operator decomposition

Take:

$$
\nu=1
$$

normalization.

Miller operator:

$$
\boxed{
\mathcal Q_{SV}
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34\omega\otimes\omega
\right).
}
$$

Define:

$$
\boxed{
\mathcal A_{adv}
=
P_{st}((u\cdot\nabla)S),
}
$$

$$
\boxed{
\mathcal A_{S^2}
=
P_{st}(S^2),
}
$$

$$
\boxed{
\mathcal A_{\omega^2}
=
\frac34
P_{st}(\omega\otimes\omega).
}
$$

Then:

$$
\mathcal Q_{SV}
=
\mathcal A_{adv}
+
\mathcal A_{S^2}
+
\mathcal A_{\omega^2}.
$$

---

# 37. C4-C.13: Operator-Source Shared-Event Trichotomy

## Theorem 37.1

If:

$$
\boxed{
\|\mathcal Q_{SV}\|_2
\ge
d,
}
$$

then at least:

$$
\boxed{
\|\mathcal A_{adv}\|_2
\ge
\frac d3,
}
$$

or:

$$
\boxed{
\|\mathcal A_{S^2}\|_2
\ge
\frac d3,
}
$$

or:

$$
\boxed{
\|\mathcal A_{\omega^2}\|_2
\ge
\frac d3.
}
$$

### Proof

triangle inequality. $\square$

---

# 38. Miller escape version

If:

$$
\boxed{
\|\mathcal Q_{SV}\|_2
\ge
c
\|-\Delta S\|_2,
}
$$

then at least one operator source satisfies:

$$
\boxed{
\|\mathcal A_\bullet\|_2
\ge
\frac c3
\|-\Delta S\|_2.
}
$$

Therefore, operator escape itself cannot be carrier-relayed into "no source".

It must be simultaneously carried by one of:

$$
\boxed{
\text{advection}
\ \vee\
\text{strain square}
\ \vee\
\text{vorticity quadratic}
}
$$

---

# 39. Operator cancellation debt

Conversely, if:

$$
\mathcal A_{\omega^2}
$$

is large,

but:

$$
\mathcal Q_{SV}
$$

is small,

then:

$$
\boxed{
\|
\mathcal A_{adv}
+
\mathcal A_{S^2}
\|_2
\ge
\|
\mathcal A_{\omega^2}
\|_2
-
\|
\mathcal Q_{SV}
\|_2.
}
$$

Therefore, if the vorticity quadratic source does not become a Miller operator escape,

it must be synchronously cancelled by the advection / strain-square projected source.

This is:

$$
\boxed{
\textbf{Operator Cancellation Debt}.
}
$$

---

# 40. Global vortex-stretching / operator-source bridge

whole space:

$$
S\in L^2_{st}.
$$

Therefore:

$$
\langle
S,
P_{st}(\omega\otimes\omega)
\rangle
=
\langle
S,
\omega\otimes\omega
\rangle
=
\int
\omega\cdot S\omega.
$$

Therefore:

$$
\boxed{
\left|
\int
\omega\cdot S\omega
\right|
\le
\|S\|_2
\|
P_{st}(\omega\otimes\omega)
\|_2.
}
$$

Thus:

$$
\boxed{
\|
P_{st}(\omega\otimes\omega)
\|_2
\ge
\frac{
\left|
\int
\omega\cdot S\omega
\right|
}{
\|S\|_2
}.
}
$$

Large global vortex stretching synchronously generates a large vorticity-quadratic projected source,

but does not yet automatically generate a full Miller operator escape,

because the §39 cancellation can still occur.

---

# 41. Shared-event closure graph v0.1

Current exact / conditional edges:

$$
\boxed{
\text{UV amplitude}
\longrightarrow
\text{critical helical stock}
+
\text{strain/vorticity stock}.
}
$$

$$
\boxed{
\text{Robust heterochiral high-mode gain}
\longrightarrow
\text{positive helical variation}.
}
$$

$$
\boxed{
\text{High-mode gain}
\longrightarrow
\text{homochiral}
\vee
\text{gap-degenerate}
\vee
\text{helical net}
\vee
\text{helical cancellation}.
}
$$

$$
\boxed{
\text{Strain growth}
\longrightarrow
\text{pressure}
\vee
\text{Betchov}
\vee
\text{vortex stretching}.
}
$$

$$
\boxed{
\text{Vortex stretching}
\longrightarrow
\text{middle-strain carrier}
\vee
\text{principal-alignment carrier}.
}
$$

$$
\boxed{
\text{Pressure active}
\longrightarrow
\text{mean rotation}
\vee
\text{quadratic cancellation}.
}
$$

$$
\boxed{
\text{Miller operator escape}
\longrightarrow
\text{advection}
\vee
S^2
\vee
\omega^2.
}
$$

---

# 42. What carrier relay can no longer erase

Carrier relay can:

- Switch shells;
- Switch cores;
- Switch packets.

But once the carrier currently enters a shared-event antecedent,

its consequent branch must exist at the same time.

For example:

$$
\boxed{
\text{robust Class IV high-mode gain}
}
$$

cannot rely on switching shells in the next generation to make the current generation's:

$$
\mathcal R_\tau
$$

disappear.

Therefore, shared-event edges are C4 tools that genuinely constrain the relay.

---

# 43. But branching relay still survives

The survivor can still choose a different outcome each generation:

generation 1:

$$
\text{homochiral}.
$$

generation 2:

$$
\text{gap-degenerate heterochiral}.
$$

generation 3:

$$
\text{helical cancellation}.
$$

generation 4:

$$
\text{pressure branch}.
$$

Therefore, C4 still needs:

$$
\boxed{
\textbf{recurrent branch reduction}
}
$$

and branch-specific rigidity.

---

# 44. Key missing bridge 1: Amplitude → Flux

The true hereditary anchor of C1/C3-G is:

$$
\boxed{
\text{critical amplitude / first crossing}.
}
$$

The strongest helical event theorem in C4-C is:

$$
\boxed{
\text{positive high-mode energy gain}.
}
$$

The two are currently only connected by a static stock edge,

without:

$$
\boxed{
\text{amplitude first crossing}
\Rightarrow
\text{positive shell flux of comparable critical size}.
}
$$

This is the:

$$
\boxed{
\textbf{Amplitude-to-Flux Barrier}.
}
$$

---

# 45. Key missing bridge 2: Stock → Production

UV amplitude now indeed synchronizes:

- helical stock;
- strain stock;
- vorticity stock.

But stock can exist statically.

There is no:

$$
\boxed{
\text{critical stock}
\Rightarrow
\text{positive production / stretching / operator escape}.
}
$$

This is the:

$$
\boxed{
\textbf{Stock-to-Production Barrier}.
}
$$

---

# 46. Key missing bridge 3: Triadwise positive variation → global net production

robust heterochiral high-mode gain gives:

$$
P_+
\gtrsim
G_{\rm rob}.
$$

But:

$$
\boxed{
P_+
}
$$

is not:

$$
\boxed{
[\mathcal R_{\rm net}]_+.
}
$$

It can still be cancelled by:

$$
P_-
$$

.

Therefore:

$$
\boxed{
\textbf{Helical Cancellation Packing}
}
$$

is another C4 frontier.

---

# 47. Key missing bridge 4: Local vortex stretching → global Miller escape

local:

$$
V_\chi
$$

being large only gives:

- local geometry;
- local vorticity quadratic load.

The Miller theorem is global:

$$
\|\mathcal Q_{SV}\|_2
/
\|\Delta S\|_2.
$$

Projection / localization / cancellation still prevent a direct implication.

Therefore:

$$
\boxed{
\textbf{Local-to-Operator Bridge}
}
$$

remains open.

---

# 48. C4-C minimum synchronized subsets

Although the full C4 state is not yet synchronized,

there are now at least the following genuine small synchronized subsets.

## Sync subset C1

$$
\boxed{
\{
\text{UV amplitude},
\text{helical critical stock},
\text{strain stock},
\text{vorticity stock}
\}.
}
$$

## Sync subset C2

$$
\boxed{
\{
\text{robust heterochiral high-mode gain},
\text{positive helical variation}
\}.
}
$$

## Sync subset C3

$$
\boxed{
\{
\text{strain growth},
\text{pressure/Betchov/vortex-stretching branch}
\}.
}
$$

## Sync subset C4

$$
\boxed{
\{
\text{Miller operator escape},
\text{one large operator source component}
\}.
}
$$

These are the genuine seed nodes of the C4 closure graph.

---

# 49. C4-C major no-go

### NG-C1

$$
\text{UV amplitude}
\Rightarrow
\text{UV energy gain}.
$$

FALSE from norm information alone.

### NG-C2

$$
\text{high-mode energy gain}
\Rightarrow
\text{net positive helical production}.
$$

FALSE due to:

- homochiral carrier;
- radial-gap degeneration;
- simultaneous negative helical cancellation.

### NG-C3

$$
\text{critical stock}
\Rightarrow
\text{critical production}.
$$

FALSE / not established.

### NG-C4

$$
\text{strain growth}
\Rightarrow
\text{Miller operator escape}.
$$

FALSE from scalar balance alone.

### NG-C5

$$
\text{large vorticity quadratic operator source}
\Rightarrow
\text{large full Miller operator}.
$$

FALSE due to operator cancellation.

---

# 50. X-Integration guards update

## G-AMPFLUX

An amplitude / norm event must not be treated as an energy-flux event.

## G-TRIADSIGN

Highest-mode gain must preserve the helical class and the $\Theta$ sign.

## G-RGAP

II/III coupling must preserve the radial gap.

## G-HVAR

Triadwise positive helical variation must be separated from global net pair-production.

## G-STOCKPROD

Critical stock must not be elevated to production.

## G-SHARED

Same-event branching edges allow branching, but once the antecedent is established, all consequents cannot be deleted.

## G-OPCANCEL

A large projected operator component must not be directly elevated to a large Miller total operator.

---

# 51. True ETN update

Shared-event state:

$$
\boxed{
\Theta^{shared}
=
\left\langle
\mathcal E,
\operatorname{CarrierID},
\operatorname{LoadVector},
\operatorname{BranchSet},
\operatorname{CancellationDebt},
\operatorname{Prov}
\right\rangle.
}
$$

For example, a helical triad:

$$
\boxed{
\Theta_\tau^{gain}
=
\left\langle
(k,p,q),
(s_k,s_p,s_q),
G_\tau^q,
\mathcal R_\tau,
\kappa_\tau,
\operatorname{Gap}
\right\rangle.
}
$$

---

# 52. C4 strategic update

C4-B eliminated:

$$
\boxed{
\text{generic switching-cost synchronization}.
}
$$

C4-C now proves:

$$
\boxed{
\text{true N--S shared-event coupling indeed exists,
but current edges are still branching / typed edges}.
}
$$

The most important bridge gaps are already very clear:

$$
\boxed{
\textbf{Amplitude-to-Flux}
}
$$

and:

$$
\boxed{
\textbf{Helical-Cancellation Packing}.
}
$$

Therefore, the next round should directly attack these two.

---

# 53. New frontier: C4-D

Formal definition:

$$
\boxed{
\textbf{C4-D — Amplitude-to-Flux Bridge and Helical-Cancellation Rigidity}.
}
$$

---

# 54. C4-D proof obligations

## D1 — First-crossing derivative identity

For the:

$$
a_q^\sigma(t)
=
\frac{
\|u_q^\sigma(t)\|_\infty
}{
\nu\lambda_q
}
$$

first crossing,

find the maximizing-point / duality functional,

to write the amplitude derivative as:

$$
\boxed{
\text{nonlinear source}
-
\text{viscous loss}.
}
$$

Do not substitute it with $L^2$ energy flux.

## D2 — Amplitude source decomposition

Decompose the nonlinear source into:

- shell-energy-changing component;
- phase-rearrangement / intra-shell component;
- spatial concentration component.

If amplitude growth is not accompanied by energy gain,

quantify the remaining phase/concentration debt.

## D3 — Flux bridge under coherence

If the phase efficiency:

$$
\eta_q
$$

and packet localization have a lower bound,

can we prove:

$$
\boxed{
\text{amplitude first crossing}
\Rightarrow
\text{positive high-mode energy gain}
}
$$

in a fixed fraction sense?

## D4 — Homochiral relay branch

If UV gain is repeatedly carried by homochiral triads,

connect to the Biferale–Titi sign-definite critical structure,

and study how heterochiral leakage must appear in the full N–S.

## D5 — Radial-gap degeneration

If II/III repeatedly utilize:

$$
q-p\ll q
$$

or:

$$
q-k\ll q,
$$

establish same-shell/radial congestion packing.

## D6 — Helical cancellation

If robust positive pair-production is always cancelled by:

$$
P_-
$$

,

study whether:

$$
\boxed{
P_++P_-
}
$$

total helical variation has a new critical / geometric budget.

## D7 — Pair-production sign switching

Negative pair production requires triad phase reversal.

Connecting to C3-E phase efficiency and C3-G ancestry,

study whether cancellation requires repeated phase inversion.

## D8 — C4 graph expansion

If the amplitude-to-flux bridge is established,

the closure graph immediately adds:

$$
\boxed{
\text{UV first crossing}
\to
\text{homochiral / degenerate / helical turnover}.
}
$$

This will for the first time directly synchronize the C1/C3-G hereditary ancestry to the C3-A/B helical critical channel.

---

# 55. Formal status

$$
\boxed{
\begin{aligned}
\text{highest-mode triad gain formulas}
&:\ \mathrm{PROVED},\\
\text{heterochiral high-mode gain}\Rightarrow\mathcal R_\tau>0
&:\ \mathrm{PROVED},\\
\text{Class IV critical coupling}
&:\ \mathrm{EXACT},\\
\text{II/III robust-gap coupling}
&:\ \mathrm{PROVED},\\
\text{aggregate robust gain}\Rightarrow\text{positive helical variation}
&:\ \mathrm{PROVED},\\
\text{positive variation}\Rightarrow\text{net positive production}
&:\ \mathrm{FALSE\ without\ cancellation\ control},\\
\text{high-mode gain shared-event trichotomy}
&:\ \mathrm{PROVED},\\
\text{UV amplitude}\Rightarrow\text{helical critical stock}
&:\ \mathrm{PROVED},\\
\text{UV amplitude}\Rightarrow\text{strain/vorticity stock}
&:\ \mathrm{PROVED},\\
\text{UV amplitude}\Rightarrow\text{energy flux}
&:\ \mathrm{NO\mbox{-}GO\ from\ norm\ data},\\
\text{local strain-growth shared-event trichotomy}
&:\ \mathrm{PROVED},\\
\text{SSA}\Rightarrow\text{vortex stretching / Betchov branch}
&:\ \mathrm{PROVED},\\
\text{pressure}\Rightarrow\text{mean rotation / quadratic branch}
&:\ \mathrm{PROVED},\\
\text{Miller escape}\Rightarrow\text{operator-source trichotomy}
&:\ \mathrm{PROVED},\\
\text{full shared-event synchronization graph closure}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 56. Conclusion

C4-B tells us:

$$
\boxed{
\text{generic turnover cannot prevent carrier relay}.
}
$$

C4-C now for the first time finds edges that are truly immune to relay:

because they are:

$$
\boxed{
\textbf{same-event algebra}.
}
$$

The most important helical result:

For a single triad:

$$
\boxed{
\text{heterochiral highest-mode gain}
\Rightarrow
\text{positive critical pair production}.
}
$$

Class IV even has:

$$
\boxed{
\mathcal R_\tau
=
q[\dot e_q]_+.
}
$$

For local II/III, if the radial gap does not degenerate,

we also have:

$$
\boxed{
\mathcal R_\tau
\gtrsim
q[\dot e_q]_+.
}
$$

Therefore, a high-mode energy-gain event can only escape to:

$$
\boxed{
\text{homochiral}
\vee
\text{radial degeneration}
\vee
\text{helical turnover/cancellation}.
}
$$

But:

$$
\boxed{
\text{the C1/C3-G UV anchor is an amplitude event,
not an energy-gain event}.
}
$$

Phase rearrangement proves:

$$
\boxed{
\text{amplitude}
\not\Rightarrow
\text{flux}
}
$$

from norm data alone.

Therefore, the next genuine bridge for C4 is already very precise:

$$
\boxed{
\textbf{Amplitude-to-Flux Bridge}.
}
$$

At the same time,

local strain growth has been compressed by same-event to:

$$
\boxed{
\text{pressure}
\vee
\text{Betchov}
\vee
\text{vortex-stretching geometry},
}
$$

and Miller operator escape has also been compressed to:

$$
\boxed{
\text{advection}
\vee
S^2
\vee
\omega^2.
}
$$

Thus, the C4 closure graph already has seeds.

Next round:

$$
\boxed{
\textbf{C4-D — Amplitude-to-Flux Bridge and Helical-Cancellation Rigidity}.
}
$$

---

# References

1. F. Waleffe, *The nature of triad interactions in homogeneous turbulence*, Physics of Fluids A 4 (1992), 350–363, DOI: 10.1063/1.858309.
2. Z. Lei, F.-H. Lin, Y. Zhou, *Structure of Helicity and Global Solutions of Incompressible Navier–Stokes Equation*, arXiv:1505.00142.
3. L. Biferale, E. S. Titi, *On the Global Regularity of a Helical-decimated Version of the 3D Navier–Stokes Equations*, arXiv:1303.1215.
4. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
5. A. Cheskidov, M. Dai, *Regularity criteria for the 3D Navier–Stokes and MHD equations*, arXiv:1507.06611.

# Internal dependencies

- `NS_C4B_TemporalSynchronization_CarrierRelayNoGo_v0.1.md`
- `NS_C4A_UnifiedSurvivorState_SynchronizationClosure_v0.1.md`
- `NS_C3B_BiHelical_Equalization_UniqueSign_UV_Escape_v0.1.md`
- `NS_C3C_ClassII_Nonlocality_Tax_Radial_Congestion_v0.1.md`
- `NS_C3D_CutoffFlux_HelicalKernel_Nonlocality_v0.1.md`
- `NS_C3E_ViscousWindow_PhaseEfficiency_Zeno_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `NS_C3N_LocalizedBetchov_StrainBoundaryBalance_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3P_OperatorEscape_FarPressureMatrix_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C4-D — Amplitude-to-Flux Bridge and Helical-Cancellation Rigidity}
}
$$