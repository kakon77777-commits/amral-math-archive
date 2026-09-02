---
title: "Navier–Stokes C3-O: Adjoint Core Balance, Cancellation Corridor, and Balance–Dynamics Separation"
subtitle: "Gauge-Clean Local Strain Balance, Asymptotic Boundary/Self-Amplification Regimes, and Why Energy-Balance Closeness Is Not Dynamical Closeness"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Exact adjoint-localized strain balance + asymptotic ratio classification + balance-versus-operator no-go. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-O
# Adjoint Core Balance, Cancellation Corridor, and Balance–Dynamics Separation

## 0. Positioning of this Round

C3-N has established the exact localized strain balance:

$$
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\mathcal C_\chi,
$$

where:

$$
\begin{aligned}
\mathcal C_\chi
={}&
\frac12\int
|S|^2
(
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
)
\\
&+
\frac13\int\nabla\chi\cdot F_B
+
\int\nabla\chi\cdot F_p.
\end{aligned}
$$

and:

$$
F_B
=
\left(
A^2
-\frac12\operatorname{tr}(A^2)I
\right)u,
\qquad
A=\nabla u,
$$

as well as:

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

The first question of this round:

> Can the gauge/advection/diffusion terms caused by the cutoff itself be completely stripped away?

Answer:

$$
\boxed{\textbf{YES}.}
$$

Simply use the backward adjoint cutoff of the strain transport-diffusion operator.

The second question:

> If only the bulk strain self-amplification and the true boundary current remain, which of the three asymptotic ratio regimes can be excluded?

Answer:

- Excessively negative boundary:
  $$
  \boxed{\rho\le-1}
  $$
  cannot support positive local strain-energy growth;
- $\rho\to-1^+$:
  Not excluded, but must pay for an increasingly precise gross cancellation;
- $\rho\to0$:
  Also not excluded, and **cannot** be interpreted as the full dynamics approaching the strain self-amplification model;
- $\rho\to+\infty$:
  The boundary/pressure current becomes the primary growth carrier.

The most important conclusion:

$$
\boxed{
\text{balance closeness}
\neq
\text{dynamical/operator closeness}.
}
$$

---

# 1. Full strain equation

For the smooth incompressible Navier–Stokes equations:

$$
\partial_tu
-\nu\Delta u
+
(u\cdot\nabla)u
+
\nabla p
=
0,
$$

$$
\nabla\cdot u=0,
$$

the strain:

$$
S
=
\frac12
(\nabla u+\nabla u^\top)
$$

satisfies:

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
(u\cdot\nabla)S
+
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
\nabla^2p
=
0.
}
$$

---

# 2. Adjoint cutoff

Fix the ancestry window:

$$
I=[t_0,t_1].
$$

Take the terminal cutoff:

$$
\chi_1(x)
$$

satisfying:

$$
0\le\chi_1\le1,
$$

and localized near the child ancestry core.

Let:

$$
\boxed{
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0
}
$$

for:

$$
t_0<t<t_1,
$$

with the terminal condition:

$$
\boxed{
\chi(t_1,x)=\chi_1(x).
}
$$

Let:

$$
\tau=t_1-t.
$$

Then it becomes a forward parabolic equation:

$$
\partial_\tau\chi
=
u(t_1-\tau)\cdot\nabla\chi
+
\nu\Delta\chi.
$$

Thus, in a smooth pre-singular window, this is a standard parabolic adjoint construction.

---

# 3. Adjoint ancestry tube

This cutoff is not a fixed ball.

It will:

- backward follow the velocity drift;
- backward diffuse over a parabolic distance;
- automatically absorb the moving-core gauge and advection cutoff terms.

In this document, it is called the:

$$
\boxed{
\textbf{Adjoint Ancestry Tube}.
}
$$

---

# 4. C3-O.1: Adjoint Core Balance Theorem

## Theorem 4.1

If:

$$
\chi
$$

solves the adjoint cutoff equation:

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
$$

then:

$$
\boxed{
\frac12
\frac d{dt}
\int
\chi|S|^2
+
\nu
\int
\chi|\nabla S|^2
=
-2
\int
\chi\det S
+
\int
\nabla\chi\cdot J_{\rm corr},
}
$$

where:

$$
\boxed{
J_{\rm corr}
=
\frac13F_B+F_p.
}
$$

### Proof

Substitute directly into the localized strain balance from C3-N.

Since:

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0,
$$

the first entire set of scalar cutoff terms exactly vanishes. $\square$

---

# 5. Gauge-clean variables

Define:

$$
E_\chi(t)
=
\frac12
\int
\chi|S|^2dx,
$$

$$
D_\chi(t)
=
\nu
\int
\chi|\nabla S|^2dx,
$$

$$
A_\chi(t)
=
-2
\int
\chi\det S\,dx,
$$

and:

$$
B_\chi(t)
=
\int
\nabla\chi\cdot J_{\rm corr}\,dx.
$$

Then:

$$
\boxed{
E_\chi'
+
D_\chi
=
A_\chi+B_\chi.
}
$$

---

# 6. Window-integrated balance

For:

$$
I=[t_0,t_1],
$$

define:

$$
\Delta E_I
=
E_\chi(t_1)-E_\chi(t_0),
$$

$$
D_I
=
\int_I
D_\chi(t)\,dt,
$$

$$
A_I
=
\int_I
A_\chi(t)\,dt,
$$

$$
B_I
=
\int_I
B_\chi(t)\,dt.
$$

Then:

$$
\boxed{
\Delta E_I+D_I
=
A_I+B_I.
}
$$

and:

$$
D_I\ge0.
$$

---

# 7. Growth window

Call:

$$
I
$$

a positive local strain-growth window, if:

$$
\Delta E_I>0.
$$

Then:

$$
A_I+B_I
=
\Delta E_I+D_I
>
0.
$$

---

# 8. C3-O.2: Growth-Carrier Dichotomy

## Theorem 8.1

For any positive local strain-growth window, one of the following must hold:

### Branch A — Positive SSA-supported

$$
A_I>0
$$

and:

$$
B_I>-A_I.
$$

### Branch B — Boundary-current-driven

$$
A_I\le0
$$

and necessarily:

$$
\boxed{
B_I>
|A_I|+D_I.
}
$$

More precisely:

$$
B_I
=
\Delta E_I+D_I-A_I.
$$

$\square$

---

# 9. Boundary ratio

In a window where:

$$
A_I>0
$$

define:

$$
\boxed{
\rho_I
=
\frac{B_I}{A_I}.
}
$$

From the growth condition:

$$
A_I+B_I>0,
$$

we obtain:

$$
\boxed{
\rho_I>-1.
}
$$

---

# 10. C3-O.3: Hard Depletion Barrier

## Theorem 10.1

If:

$$
A_I>0
$$

and:

$$
\rho_I\le-1,
$$

then:

$$
\boxed{
\Delta E_I\le-D_I\le0.
}
$$

Therefore, this window cannot be a positive strain-growth window. $\square$

---

# 11. Cancellation corridor

For:

$$
A_I>0,
$$

define:

$$
\boxed{
\kappa_I
=
1+\rho_I
=
\frac{\Delta E_I+D_I}{A_I}.
}
$$

A growth window satisfies:

$$
\kappa_I>0.
$$

---

# 12. C3-O.4: Cancellation-Precision Debt

If:

$$
\rho_I\to-1^+
$$

along some growth windows,

then:

$$
\kappa_I\to0^+.
$$

and:

$$
\boxed{
A_I
=
\frac{\Delta E_I+D_I}{\kappa_I}.
}
$$

So if:

$$
\Delta E_I+D_I
$$

does not tend to zero at the same rate,

then:

$$
A_I\to\infty,
$$

and:

$$
|B_I|\sim A_I.
$$

That is:

$$
\boxed{
\text{large SSA}
+
\text{large opposite boundary current}
+
\text{small residual}.
}
$$

---

# 13. Fixed fractional growth version

If:

$$
\Delta E_I
\ge
\gamma E_\chi(t_0)
$$

for a fixed:

$$
\gamma>0,
$$

then:

$$
\boxed{
A_I
\ge
\frac{
\gamma E_\chi(t_0)
}{
\kappa_I
}.
}
$$

Therefore, when:

$$
\kappa_I\to0
$$

the gross self-amplification must increase relative to the local stock.

---

# 14. Ratio subsequence classification

Consider infinitely many positive growth windows:

$$
I_n
$$

with:

$$
A_{I_n}>0.
$$

Since:

$$
\rho_n>-1,
$$

we can extract a subsequence falling into:

## O-A — Cancellation corridor

$$
\rho_n\to-1^+.
$$

## O-B — Finite balance regime

There exist:

$$
-1+\delta
\le
\rho_n
\le
M
$$

for some:

$$
\delta>0,
\quad
M<\infty.
$$

## O-C — Boundary-driven regime

$$
\rho_n\to+\infty.
$$

If there are infinitely many:

$$
A_{I_n}\le0
$$

growth windows,

they automatically belong to the boundary-current-driven branch.

---

# 15. Miller operator decomposition

Miller writes the full strain equation as:

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
+
\mathcal P_{NS}
=
0,
}
$$

where:

$$
\boxed{
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right).
}
$$

The strain self-amplification model is:

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
\frac23P_{st}(S^2)
=
0.
}
$$

---

# 16. Orthogonality

For the full-space strain:

$$
S\in L^2_{st},
$$

we have:

$$
\boxed{
\langle
\mathcal P_{NS},
S
\rangle
=
0.
}
$$

Thus, the full N–S and the SSA model share the same global strain-enstrophy growth identity:

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu\|S\|_{\dot H^1}^2
-
4\int\det S.
}
$$

---

# 17. C3-O.5: Balance–Dynamics Separation No-Go

## Proposition 17.1

$$
\langle\mathcal P_{NS},S\rangle=0
$$

does not imply:

$$
\mathcal P_{NS}=0.
$$

Therefore:

$$
\boxed{
\text{the perturbation can be dynamically large while energy-orthogonal}.
}
$$

In particular:

the whole-space balance for all full N–S solutions satisfies:

$$
B_{\chi\equiv1}=0,
$$

but the full N–S strain equation does not thereby equal the SSA model.

Therefore:

$$
\boxed{
\rho\to0
\not\Rightarrow
\text{dynamical closeness to SSA model}.
}
$$

$\square$

---

# 18. Why is this no-go important?

Miller's SSA model:

- lies in the same strain constraint space;
- possesses the same enstrophy-growth identity;
- has a similar middle-eigenvalue regularity structure;
- can blow up in finite time for a class of initial data.

Therefore:

$$
\boxed{
\text{strain-energy balance itself is insufficient to distinguish
the full N--S from the blow-up capable SSA model}.
}
$$

---

# 19. Conditional full-N–S warning

Miller's SSA-model work also proves a conditional full-N–S blow-up result:

If the terms dropped from the full equation relative to the model satisfy the perturbative smallness hypothesis in that paper,

then under the corresponding initial-data conditions, the full N–S will also blow up in finite time.

This document will not restate the full technical hypothesis.

The retained structural conclusion is:

$$
\boxed{
\text{"depletion/orthogonal perturbation is small" itself is not a direction for regularity.}
}
$$

---

# 20. Operator-level defect

Therefore, what truly needs to be tracked in parallel with:

$$
\rho_I
$$

is:

$$
\mathcal P_{NS}
$$

itself.

A scale-compatible candidate is:

$$
\boxed{
\mathfrak P_I
=
\frac{
\int_I
\|\mathcal P_{NS}(t)\|_{\dot H^{-1}}^2dt
}{
\nu^2
\int_I
\|S(t)\|_{\dot H^1}^2dt
}
}
$$

when the denominator is non-zero.

---

# 21. Scaling audit

N–S scaling:

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t).
$$

equation-level perturbation:

$$
(\mathcal P_{NS})_\lambda
=
\lambda^4
\mathcal P_{NS}(\lambda x,\lambda^2t).
$$

Therefore:

$$
\|\mathcal P_\lambda\|_{\dot H^{-1}}
=
\lambda^{3/2}
\|\mathcal P\|_{\dot H^{-1}},
$$

so:

$$
\int
\|\mathcal P_\lambda\|_{\dot H^{-1}}^2dt
=
\lambda
\int
\|\mathcal P\|_{\dot H^{-1}}^2dt.
$$

At the same time:

$$
\int
\|S_\lambda\|_{\dot H^1}^2dt
=
\lambda
\int
\|S\|_{\dot H^1}^2dt.
$$

Thus:

$$
\boxed{
\mathfrak P_I
}
$$

is scale invariant.

---

# 22. Note: $\mathfrak P_I$ is only a candidate diagnostic

It is currently unproven that:

$$
\mathfrak P_I<\varepsilon
\Rightarrow
\text{SSA approximation theorem},
$$

nor is it proven that:

$$
\mathfrak P_I\gg1
\Rightarrow
\text{regularity}.
$$

Its purpose is to prevent:

$$
\boxed{
\text{zero energy pairing}
}
$$

from being conflated with:

$$
\boxed{
\text{small operator}.
}
$$

---

# 23. Balance–Dynamics plane

A true local state requires at least:

$$
\boxed{
(\rho_I,\mathfrak P_I).
}
$$

which can distinguish:

## BD-1 — Balance-SSA / Operator-small

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I\ll1.
$$

This is the model-like candidate regime that is actually worth testing.

## BD-2 — Balance-SSA / Operator-large

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I\gtrsim1.
$$

The energy balance appears SSA-like,

but the hidden orthogonal dynamics are large.

## BD-3 — Cancellation corridor

$$
\rho_I\to-1^+.
$$

Massive cancellation between the gross SSA and the boundary current.

## BD-4 — Boundary driven

$$
\rho_I\gg1
$$

or:

$$
A_I\le0,\quad B_I>0.
$$

---

# 24. Miller 2024/2026 warning on the operator-large regime

Miller's work on strain–vorticity interaction proves:

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

and establishes global regularity for a model equation isolating the reverse strain–vorticity interaction.

That work also provides regularity criteria used to analyze when advection depletes the nonlinearity.

Therefore:

$$
\boxed{
\text{large omitted/operator terms are not necessarily blow-up drivers;
they may be depletion mechanisms}.
}
$$

Thus:

$$
\mathfrak P_I
$$

must also be further split by type, rather than just looking at magnitude.

---

# 25. X-Integration significance of the Adjoint cutoff

The original moving cutoff has:

- gauge;
- advection;
- diffusion;
- Betchov;
- pressure.

The adjoint cutoff absorbs the first three into the cutoff evolution.

Therefore:

$$
\boxed{
B_\chi
=
\int\nabla\chi\cdot
\left(
\frac13F_B+F_p
\right)
}
$$

is a cleaner correction current.

Newly added:

$$
\boxed{
G_{\rm ADJ}
}
$$

The bulk/boundary ratio should prioritize using the adjoint cutoff, or explicitly subtract the non-adjoint gauge terms.

---

# 26. Gauge-clean does not equal boundary-small

Even if:

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi=0,
$$

it is still possible that:

$$
|B_\chi|
$$

is large.

Especially since:

$$
F_p
$$

contains the nonlocal pressure Hessian.

Therefore:

$$
\boxed{
\text{gauge-clean}
\neq
\text{boundary-small}.
}
$$

---

# 27. Pressure/Betchov correction split

Define:

$$
B_I
=
B_I^B+B_I^p,
$$

where:

$$
B_I^B
=
\frac13
\int_I
\int
\nabla\chi\cdot F_B,
$$

$$
B_I^p
=
\int_I
\int
\nabla\chi\cdot F_p.
$$

If:

$$
|B_I|
$$

is large,

then at least:

$$
|B_I^B|
\ge
\frac12|B_I|
$$

or:

$$
|B_I^p|
\ge
\frac12|B_I|.
$$

Thus, the boundary-dominated branch is further split into:

$$
\boxed{
\text{Betchov-current dominated}
\quad\vee\quad
\text{pressure-current dominated}.
}
$$

---

# 28. Component debt of the Cancellation corridor

If:

$$
\rho_I\to-1^+
$$

and:

$$
A_I>0,
$$

then:

$$
B_I\sim-A_I.
$$

So at least one of:

$$
B_I^B,
\quad
B_I^p
$$

must have an:

$$
O(A_I)
$$

magnitude.

Near-perfect depletion cannot be achieved by having all correction components be small.

---

# 29. Final verdict on the Ratio route

### $\rho<-1$

Positive growth is impossible.

### $\rho\to-1^+$

Survives, but pays a cancellation-precision debt.

### $\rho\to0$

Survives, and cannot be interpreted as dynamical SSA closeness.

### $\rho\to+\infty$

Survives, with the boundary/pressure current becoming the primary carrier.

Therefore:

$$
\boxed{
\rho
}
$$

can only serve as a:

$$
\boxed{
\text{local strain-energy growth carrier classifier}.
}
$$

It cannot serve as a standalone regularity parameter.

---

# 30. Balance Fixed Point / Dynamics Fixed Point Separation

Even if:

$$
\rho_n\to0
$$

and:

$$
\frac{
\Delta E_n+D_n
}{
A_n
}
\to1,
$$

it only means:

$$
\boxed{
\text{strain-energy balance becomes SSA-like}.
}
$$

It does not mean:

$$
\boxed{
S_n
\text{ approaches an SSA-model solution}.
}
$$

This document calls this:

$$
\boxed{
\textbf{Balance Fixed Point / Dynamics Fixed Point Separation}.
}
$$

This is extremely important for True ETN:

relation-level balance convergence cannot automatically be elevated to operator-level dynamical convergence.

---

# 31. True ETN Update

The local strain state should be divided into two layers.

## Balance layer

$$
\boxed{
\Theta^{bal}
=
(E,D,A,B,\rho,\kappa).
}
$$

## Operator layer

$$
\boxed{
\Theta^{op}
=
\left(
\mathcal N_{SSA},
\mathcal P_{NS},
\mathfrak P,
\operatorname{Prov}
\right),
}
$$

where:

$$
\mathcal N_{SSA}
=
\frac23P_{st}(S^2).
$$

Therefore:

$$
\boxed{
\Theta^{bal}\text{ convergence}
\not\Rightarrow
\Theta^{op}\text{ convergence}.
}
$$

---

# 32. X-Integration hard guards

## G-ADJ

The ratio uses the adjoint cutoff or full gauge subtraction.

## G-GROW

The ratio only determines the growth carrier in:

$$
\Delta E>0
$$

growth windows.

## G-RATIO

If:

$$
A>0,
$$

positive growth requires:

$$
\rho>-1.
$$

## G-CANCEL

If:

$$
\rho\to-1,
$$

the gross terms must be preserved:

$$
A,\ B
$$

and not just the residual:

$$
A+B.
$$

## G-OP

$$
B/A\to0
$$

must not imply:

$$
\mathcal P_{NS}\to0.
$$

## G-PROJ

The global:

$$
\langle\mathcal P_{NS},S\rangle=0
$$

is merely orthogonality, not smallness.

## G-PRESS

The pressure and Betchov corrections must be preserved separately.

---

# 33. New frontier: C3-P

C3-O has answered:

> Can the bulk/boundary ratio itself become a rigidity theorem?

Answer:

$$
\boxed{
\textbf{NO.}
}
$$

The missing information is:

$$
\boxed{
\text{the dynamical effect of the orthogonal perturbation operator itself}.
}
$$

The formal next question:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# 34. C3-P proof obligations

## P1 — Local operator defect

Establish an ancestry-localized scale-critical norm for:

$$
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+
\frac13S^2
+
\frac14\omega\otimes\omega
\right)
$$

## P2 — Small-operator regime

If:

$$
\mathfrak P_n\to0,
$$

can we rigorously prove that the rescaled ancestry dynamics approach the SSA model?

This requires a stability theorem, not a balance identity.

## P3 — Large-operator depletion split

Split:

$$
\mathcal P_{NS}
$$

into:

- advection;
- residual strain self-interaction;
- vorticity-to-strain coupling.

## P4 — Pressure current near/far split

For:

$$
F_p
=
(\nabla^2p-\Delta pI)u
$$

use the pressure Poisson equation to perform a core/far source decomposition.

## P5 — Betchov-current helical split

Decompose:

$$
F_B
$$

into local homochiral / heterochiral / nonlocal remainders.

## P6 — Cancellation corridor operator test

If:

$$
\rho_n\to-1^+,
$$

determine whether:

$$
\mathfrak P_n
$$

must also be large.

## P7 — Balance/operator phase diagram

Establish the possible / known-regular / model-like-dangerous / open regions for each branch of:

$$
(\rho_n,\mathfrak P_n)
$$

## P8 — Adjoint cutoff propagation

Analyze the radius, tails, and pressure sensitivity of the terminal ancestry cutoff propagating to earlier times.

---

# 35. Formal status

$$
\boxed{
\begin{aligned}
\text{adjoint cutoff cancellation}
&:\ \mathrm{PROVED},\\
\text{gauge-clean strain balance}
&:\ \mathrm{PROVED},\\
\text{growth-carrier dichotomy}
&:\ \mathrm{PROVED},\\
\rho>-1\text{ necessary for }A>0\text{ growth}
&:\ \mathrm{PROVED},\\
\rho\le-1\text{ growth sector}
&:\ \mathrm{EXCLUDED},\\
\text{cancellation-precision debt}
&:\ \mathrm{PROVED},\\
\rho\to0\Rightarrow\text{SSA dynamical closeness}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\langle\mathcal P_{NS},S\rangle=0
&:\ \mathrm{EXTERNAL/STANDARD},\\
\text{SSA model finite-time blowup}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{conditional full-NS blowup under perturbative condition}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\mathfrak P_I\text{ scale invariance}
&:\ \mathrm{PROVED},\\
\mathfrak P_I\text{ as stability criterion}
&:\ \mathrm{OPEN},\\
\text{balance/operator rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 36. Conclusion

C3-N writes the local strain dynamics as:

$$
\text{bulk SSA}
+
\text{boundary/gauge package}.
$$

C3-O uses the adjoint cutoff to exactly eliminate the gauge/advection/diffusion cutoff terms:

$$
\boxed{
E_\chi'
+
D_\chi
=
A_\chi+B_\chi.
}
$$

For a positive strain-growth window:

If:

$$
A>0,
$$

it is required that:

$$
\boxed{
\rho=\frac BA>-1.
}
$$

Therefore:

$$
\boxed{
\rho\le-1
}
$$

is a true hard depletion sector.

However:

$$
\rho\to-1^+,
\qquad
\rho\to0,
\qquad
\rho\to+\infty
$$

all still survive.

More importantly:

$$
\boxed{
\text{SSA-like balance}
\not\Rightarrow
\text{SSA-like dynamics}.
}
$$

The perturbation dropped by the SSA model from the full N–S is exactly orthogonal to the global strain energy,

so it can "appear to be zero" to the instantaneous enstrophy derivative,

yet still have an order-one effect on the future dynamics.

Thus, the scalar ratio route has reached its limit.

The next round must upgrade to:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# References

1. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, Analysis & PDE 16 (2023), 997–1032; arXiv:1910.05415.
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691.
3. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, Journal of Fluid Mechanics 948 (2022), R2; arXiv:2112.12820.
4. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, Arch. Rational Mech. Anal. 235 (2020).
5. R. Betchov, *An inequality concerning the production of vorticity in isotropic turbulence*, Journal of Fluid Mechanics 1 (1956), 497–504.

# Internal dependencies

- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `NS_C3N_LocalizedBetchov_StrainBoundaryBalance_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3J_GaugeCorrected_Reentry_Hysteresis_NoGo_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}
}
$$