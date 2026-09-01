---
title: "Navier–Stokes C3-O: Adjoint Core Balance, Cancellation Corridor, and Balance–Dynamics Separation"
subtitle: "Gauge-Clean Local Strain Balance, Asymptotic Boundary/Self-Amplification Regimes, and Why Energy-Balance Closeness Is Not Dynamical Closeness"
version: "v0.2"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / audited no-go note"
epistemic_status: "Exact adjoint-localized strain balance + pointwise current identities + asymptotic ratio classification + balance-versus-operator non-identifiability. Does NOT prove Navier–Stokes regularity or singularity."
---

# Navier–Stokes C3-O
# Adjoint Core Balance, Cancellation Corridor, and Balance–Dynamics Separation

## v0.2 audit delta

The core revisions in this version relative to v0.1 are not mere stylistic polishes, but rather theorem-safety enhancements:

- Eliminated the notational collision between the velocity gradient $G=\nabla u$ and the integrated amplification $A_I$;
- Formulated the Betchov current and pressure current relied upon by C3-N as pointwise divergence lemmas, allowing the main balance of C3-O to be directly verified within this text;
- Added regularity, maximum-principle, and stochastic/transition-kernel interpretations for the adjoint cutoff, explicitly pointing out that the earlier-time cutoff is a soft ancestry tube with tails, rather than a compactly supported hard tube;
- Refined the cancellation-precision debt into an exact residual trichotomy, avoiding statements like "does not vanish proportionally" which are insufficient to imply divergence;
- Revised the conclusion for $\rho\to0$ to a **non-identifiability/no-go** statement: scalar balance information alone is insufficient to control the omitted operator, rather than labeling a statement without an explicit counterexample as an unconditional false theorem;
- Explicitly marked $\mathfrak P_I$ as a whole-space/window diagnostic, and proposed a cutoff-weighted multiplicative candidate;
- Corrected the asymptotic notation for the cancellation component debt: what is needed is a lower bound $\Omega(A_I)$, not an upper-bound notation $O(A_I)$;
- Updated the reference to Miller's conditional blow-up theorem to reflect the current paper numbering and provide a precise description of the actual perturbative ratio, explicitly distinguishing it from the $\dot H^{-1}$ diagnostic proposed in this text.

---

## 0. Current Positioning

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
G^2
-\frac12\operatorname{tr}(G^2)I
\right)u,
\qquad
G=\nabla u,
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

This can be achieved simply by using the backward adjoint cutoff of the strain transport-diffusion operator.

The second question:

> If only the bulk strain self-amplification and the true boundary current remain, which of the three asymptotic ratio regimes can be excluded?

Answer:

- Excessively negative boundary:
  $$
  \boxed{\rho\le-1}
  $$
  Cannot support positive local strain-energy growth;
- $\rho\to-1^+$:
  Not excluded, but must pay an increasingly precise gross cancellation;
- $\rho\to0$:
  Also cannot be excluded, and **cannot** be interpreted as the full dynamics approaching the strain self-amplification model;
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

# 1A. Scope, convention, and regularity assumptions

Unless otherwise stated, this text works in $\mathbb R^3$, letting

$$
G_{ij}=\partial_j u_i,
\qquad
S=\frac12(G+G^\top),
\qquad
\omega=\nabla\times u.
$$

To ensure that all integration by parts, homogeneous Sobolev norms, and terminal-value adjoint constructions are free of technical ambiguities, each identity can first be understood within the class of smooth rapidly decaying solutions; subsequently, if extension to standard strong/mild solution classes is desired, it must be done term-by-term via density/approximation.

For the terminal cutoff, this text takes

$$
\chi_1\in C_c^\infty(\mathbb R^3),
\qquad
0\le\chi_1\le1.
$$

This compact support holds only at the terminal time; as long as $\nu>0$, the earlier-time adjoint cutoff will generally immediately develop noncompact tails.

---

# 1B. Pointwise current identities behind C3-N

## Lemma 1B.1 — Betchov current identity

Define

$$
F_B
=
\left(
G^2-\frac12\operatorname{tr}(G^2)I
\right)u.
$$

From $\nabla\cdot u=0$ and the commutativity of mixed derivatives, we obtain

$$
\partial_i
\left(
(G^2)_{ij}
-\frac12\operatorname{tr}(G^2)\delta_{ij}
\right)
=0.
$$

Thus,

$$
\nabla\cdot F_B
=
\operatorname{tr}(G^3).
$$

Let $W=(G-G^\top)/2$. In the three-dimensional incompressible case,

$$
\operatorname{tr}(G^3)
=
3\det S
+
\frac34\,\omega\cdot S\omega.
$$

Hence, we have the pointwise identity

$$
\boxed{
\frac14\,\omega\cdot S\omega
=
\frac13\nabla\cdot F_B
-
\det S.
}
$$

This is the precise origin of the localized Betchov conversion in this text; its whole-space averaged version is consistent with the classical Betchov relation [3,5].

## Lemma 1B.2 — Pressure current identity

Define

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

Since

$$
\partial_i
(\partial_i\partial_jp-\Delta p\,\delta_{ij})
=0,
$$

and $\operatorname{tr}G=0$, we have

$$
\boxed{
\nabla\cdot F_p
=
S:\nabla^2p.
}
$$

Furthermore, the pressure Poisson equation is

$$
\boxed{
-\Delta p
=
\operatorname{tr}(G^2)
=
|S|^2-\frac12|\omega|^2.
}
$$

Therefore, although the pressure current enters the local balance in divergence form, its source remains sensitive to the global velocity gradient field via elliptic inversion.

## Corollary 1B.3 — Direct localized strain balance

Contracting the full strain equation with $\chi S$. Using $\operatorname{tr}S=0$,

$$
S:S^2=\operatorname{tr}(S^3)=3\det S,
$$

and then applying Lemma 1B.1 and Lemma 1B.2, we obtain

$$
\boxed{
\frac12\frac d{dt}\int\chi|S|^2
+
\nu\int\chi|\nabla S|^2
=
-2\int\chi\det S
+
\frac12\int|S|^2
(\partial_t\chi+u\cdot\nabla\chi+\nu\Delta\chi)
+
\frac13\int\nabla\chi\cdot F_B
+
\int\nabla\chi\cdot F_p.
}
$$

Thus, the starting identity of C3-O need not merely serve as a black-box input from C3-N; its pointwise current mechanism can be directly verified within this text.

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

In the aforementioned smooth setting, the terminal-value problem becomes a forward uniformly parabolic problem upon time reversal, thus possessing a unique smooth solution. The maximum principle yields

$$
\boxed{
0\le\chi(t,x)\le1.
}
$$

More specifically, if $X_s^{t,x}$ solves

$$
dX_s
=
u(s,X_s)\,ds
+
\sqrt{2\nu}\,dW_s,
\qquad
X_t=x,
$$

then the backward Kolmogorov representation is

$$
\boxed{
\chi(t,x)
=
\mathbb E
\left[
\chi_1(X_{t_1}^{t,x})
\right].
}
$$

Therefore, $\chi$ can be understood as the "diffusive ancestry weight of starting from $(t,x)$ and falling into the child core at the terminal time".

Let:

$$
\tau=t_1-t.
$$

Then it becomes the forward parabolic equation:

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

This text refers to it as the:

$$
\boxed{
\textbf{Adjoint Ancestry Tube}.
}
$$

However, the "tube" here is a **soft weighted tube**. If $\nu>0$ and $\chi_1$ is non-zero, one generally cannot expect $\chi(t,\cdot)$ to maintain compact support for any $t<t_1$. Consequently, the "boundary current" mentioned later in this text should be more precisely understood as the

$$
\boxed{
\text{adjoint cutoff-interface current},
}
$$

not a classical flux across a fixed geometric boundary.

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

Directly substitute into the localized strain balance of C3-N.

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

From the growth:

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

Thus, this window cannot be a positive strain-growth window. $\square$

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

For a growth window, we have:

$$
\kappa_I>0.
$$

---

# 12. C3-O.4: Cancellation-Precision Debt

Let a sequence of positive growth windows $I_n$ satisfy

$$
A_n>0,
\qquad
\rho_n\to-1^+.
$$

Define the exact residual

$$
R_n
:=
\Delta E_n+D_n
=
A_n+B_n
>0,
$$

and

$$
\kappa_n
:=
1+\rho_n
=
\frac{R_n}{A_n}.
$$

Then

$$
\boxed{
A_n=\frac{R_n}{\kappa_n},
\qquad
B_n=-A_n+R_n.
}
$$

Thus, there are three precise consequences:

1. If there exists $c>0$ such that $R_n\ge c$, then
   $$
   A_n\to\infty,
   \qquad
   |B_n|\sim A_n.
   $$
2. More generally,
   $$
   A_n\to\infty
   \iff
   \frac{R_n}{\kappa_n}\to\infty.
   $$
3. If $A_n$ remains bounded, one must pay
   $$
   \boxed{
   R_n=O(\kappa_n).
   }
   $$

Therefore, the cancellation corridor itself does not force the gross amplification to diverge; what it forces is: **if the residual growth does not shrink along with $\kappa_n$, the gross terms must amplify.**

In the non-vanishing residual regime, one indeed obtains

$$
\boxed{
\text{large SSA}
+
\text{large opposite interface current}
+
\text{small relative residual}.
}
$$

---

# 13. Fixed fractional growth version

If $E_\chi(t_0)>0$ and

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

Thus, as:

$$
\kappa_I\to0
$$

we have:

$$
\boxed{
\frac{A_I}{E_\chi(t_0)}
\ge
\frac{\gamma}{\kappa_I}.
}
$$

Therefore, the lower bound of the gross self-amplification relative to the local stock diverges.

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

Let $L^2_{st}$ denote the closed strain subspace formed by the symmetric gradients of divergence-free velocity fields, and $P_{st}$ denote the orthogonal projection from $L^2$ to $L^2_{st}$.

After restoring the general viscosity $\nu>0$, Miller's [1] decomposition can be written as:

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

The strain self-amplification model is then:

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

For a smooth rapidly decaying full-space strain $S\in L^2_{st}$, we have

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

This fact can be directly verified in the current language of this text. Since $P_{st}$ is an orthogonal projection and $S\in L^2_{st}$,

$$
\langle P_{st}Q,S\rangle
=
\langle Q,S\rangle.
$$

First, incompressibility yields

$$
\left\langle
(u\cdot\nabla)S,S
\right\rangle
=0.
$$

Second,

$$
\left\langle
\frac13S^2,S
\right\rangle
=
\int\det S.
$$

And Lemma 1B.1, after integration over the whole space, yields the global Betchov cancellation

$$
0
=
\int\nabla\cdot F_B
=
3\int\det S
+
\frac34\int\omega\cdot S\omega,
$$

that is,

$$
\frac14\int\omega\cdot S\omega
=
-\int\det S.
$$

Thus,

$$
\left\langle
P_{st}
\left(
(u\cdot\nabla)S
+\frac13S^2
+\frac14\omega\otimes\omega
\right),
S
\right\rangle
=0.
$$

Therefore, the full Navier–Stokes and the SSA model share the same global strain-enstrophy growth identity:

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

Under the smooth/decay assumptions of this manuscript, this orthogonality is thus not an additional assumption.

---

# 17. C3-O.5: Balance–Dynamics Separation No-Go

## Proposition 17.1 — Orthogonality is not operator control

$$
\langle\mathcal P_{NS},S\rangle=0
$$

only provides a scalar pairing constraint; it does not imply

$$
\mathcal P_{NS}=0,
$$

nor does it imply any standalone norm smallness, such as

$$
\|\mathcal P_{NS}\|_X\ll1.
$$

Therefore, a more precise conclusion is

$$
\boxed{
\text{energy orthogonality imposes no operator-size bound by itself}.
}
$$

In particular, the whole-space constant choice $\chi\equiv1$ is a nonlocalized global solution of the adjoint equation (not the aforementioned compact terminal cutoff class), and yields

$$
B_{\chi\equiv1}=0
$$

identically; however, the full Navier–Stokes strain equation still contains $\mathcal P_{NS}$. Thus, in any whole-space window with $A_I>0$, the ratio is always

$$
\rho_I=0,
$$

yet it contains no information sufficient to recover $\mathcal P_{NS}$.

Therefore, what this text obtains is an information-theoretic / structural no-go:

$$
\boxed{
\rho\to0
\quad\text{alone cannot imply}\quad
\mathcal P_{NS}\to0.
}
$$

This is not a claim to have disproved approximation theorems under all possible additional assumptions using a specific explicit singular/full-NS counterexample; it merely excludes the route of **determining operator closeness solely from $\rho$**. $\square$

---

# 18. Why is this no-go important?

Miller's [1] SSA model:

- Resides in the same strain constraint space;
- Possesses the same enstrophy-growth identity;
- Has a similar middle-eigenvalue regularity structure;
- Can blow up in finite time for a class of initial data.

Therefore:

$$
\boxed{
\text{strain-energy balance itself is insufficient to distinguish the full N--S from the blow-up capable SSA model}.
}
$$

---

# 19. Conditional full-N–S warning

Miller's [1] SSA-model paper indeed proves a conditional full Navier–Stokes blow-up theorem, but v0.2 must separate it from the diagnostic in this text.

In the $\nu=1$ normalization adopted in that paper, let

$$
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+\frac13S^2
+\frac14\omega\otimes\omega
\right).
$$

The perturbative hypothesis of that theorem is not the $\mathfrak P_I$ of this text; it requires a pointwise-in-time $L^2$ ratio to remain controlled, with the denominator containing both $-\Delta S$ and nonlinear terms. In the notation of that paper, its core ratio takes the form

$$
\frac{
\|\mathcal P_{NS}(t)\|_{L^2}
}{
\left\|
-\Delta S
+
P_{st}
\left(
\frac12(u\cdot\nabla)S
+\frac56S^2
+\frac18\omega\otimes\omega
\right)
\right\|_{L^2}
}
\le2,
$$

Coupled with the initial-data sign condition specified in that paper, it deduces finite-time blow-up.

Thus, what C3-O should preserve is not a crude sentence like "small perturbation automatically means danger", but rather:

$$
\boxed{
\text{operator smallness is direction-dependent and theorem-dependent}.
}
$$

A certain specific relative closeness to the SSA dynamics can appear in a conditional blow-up theorem; on the other hand, other interaction/depletion structures might support regularity. Therefore, one cannot treat a "small omitted term" or "large omitted term" itself as a monotonic regularity parameter.

---

# 20. Operator-level defect

Therefore, what truly needs to be tracked in parallel with $\rho_I$ is $\mathcal P_{NS}$ itself.

First, define the whole-space/window diagnostic:

$$
\boxed{
\mathfrak P_I^{\rm glob}
=
\frac{
\int_I
\|\mathcal P_{NS}(t)\|_{\dot H^{-1}}^2dt
}{
\nu^2
\int_I
\|S(t)\|_{\dot H^1}^2dt
}.
}
$$

Here the denominator is non-zero, and both numerator and denominator are finite.

The reason for choosing $\dot H^{-1}$ is

$$
\|\nu\Delta S\|_{\dot H^{-1}}
=
\nu\|S\|_{\dot H^1},
$$

so $\mathfrak P_I^{\rm glob}$ can be understood as the time-integrated squared ratio of the omitted operator relative to the viscous operator.

However, it is **not a spatially localized diagnostic**. Therefore, v0.1 directly calling $(\rho_I,\mathfrak P_I)$ the "true local state" was too strong.

A cutoff-weighted multiplicative candidate is

$$
\boxed{
\mathfrak P_{I,\chi}^{\rm mult}
=
\frac{
\int_I
\|\chi\mathcal P_{NS}\|_{\dot H^{-1}}^2dt
}{
\nu^2
\int_I\int
\chi|\nabla S|^2\,dxdt
}.
}
$$

If the cutoff scales covariantly according to the Navier–Stokes scaling, this ratio remains scale invariant.

But $\dot H^{-1}$ itself is a nonlocal norm, so "cutoff-weighted" still does not equate to true geometric locality. Furthermore, multiplication by $\chi$ does not automatically yield a closed localized evolution equation. Thus, it remains merely a candidate for C3-P; a true stability theorem may require a weighted dual norm, commutator terms, or a localized projected operator.

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

Thus:

$$
\int
\|\mathcal P_\lambda\|_{\dot H^{-1}}^2dt
=
\lambda
\int
\|\mathcal P\|_{\dot H^{-1}}^2dt.
$$

Meanwhile:

$$
\int
\|S_\lambda\|_{\dot H^1}^2dt
=
\lambda
\int
\|S\|_{\dot H^1}^2dt.
$$

Hence:

$$
\boxed{
\mathfrak P_I^{\rm glob}
}
$$

is scale invariant.

---

# 22. Note: operator diagnostics are still merely candidates

Currently unproven:

$$
\mathfrak P_I^{\rm glob}<\varepsilon
\Rightarrow
\text{SSA approximation theorem},
$$

Also unproven:

$$
\mathfrak P_I^{\rm glob}\gg1
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

# 23. Balance–Dynamics diagnostic plane

If performing a whole-space/window diagnostic first, one must at least simultaneously preserve the balance and operator coordinates:

$$
\boxed{
(\rho_I,\mathfrak P_I^{\rm glob}).
}
$$

This allows distinguishing:

## BD-1 — Balance-SSA / Operator-small

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I^{\rm glob}\ll1.
$$

This is the model-like candidate regime truly worth testing.

## BD-2 — Balance-SSA / Operator-large

$$
|\rho_I|\ll1,
\qquad
\mathfrak P_I^{\rm glob}\gtrsim1.
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

# 24. Miller 2024/2026 warning regarding the operator-large regime

Miller's [2] work on strain–vorticity interaction proves:

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
\text{large omitted/operator terms are not necessarily blow-up drivers; they may be depletion mechanisms}.
}
$$

Thus:

$$
\mathfrak P_I^{\rm glob}
$$

even as a magnitude diagnostic, must be further decomposed by interaction type, rather than just looking at the total amount.

---

# 25. The X-Integration significance of the adjoint cutoff

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

The bulk/boundary ratio should preferentially use the adjoint cutoff, or explicitly subtract the non-adjoint gauge terms.

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

Especially since $F_p$ contains the pressure Hessian, and

$$
-\Delta p
=
|S|^2-\frac12|\omega|^2
$$

makes $\nabla^2p$ representable by Riesz-type elliptic operators in the whole space, thus possessing nonlocal source sensitivity.

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

at least:

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

# 28. Component debt of the cancellation corridor

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

at least satisfies:

$$
\boxed{
\max
\left\{
|B_I^B|,|B_I^p|
\right\}
\ge
\frac12|B_I|
\sim
\frac12A_I.
}
$$

Therefore, at least one component has a lower-bound magnitude of $\Omega(A_I)$, rather than merely $O(A_I)$.

Near-perfect depletion cannot be achieved by having all correction components be small.

---

# 29. Final verdict on the ratio route

### $\rho<-1$

Positive growth is impossible.

### $\rho\to-1^+$

Survives, but pays the cancellation-precision debt.

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

This text refers to this as the:

$$
\boxed{
\textbf{Balance Fixed Point / Dynamics Fixed Point Separation}.
}
$$

This is extremely important for True ETN:

Relation-level balance convergence cannot automatically be elevated to operator-level dynamical convergence.

---

# 31. True ETN update

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
\mathfrak P^{\rm glob},
\mathfrak P_{\chi}^{\rm mult},
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

The ratio uses the adjoint cutoff or complete gauge subtraction.

## G-GROW

The ratio is only used in:

$$
\Delta E>0
$$

growth windows to make growth-carrier judgments.

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

one cannot only preserve the residual:

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
\textbf{No.}
}
$$

The missing information is:

$$
\boxed{
\text{the dynamical effect of the orthogonal perturbation operator itself}.
}
$$

Formally, the next topic is:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# 34. C3-P proof obligations

## P1 — Local operator defect

For

$$
\mathcal P_{NS}
=
P_{st}
\left(
(u\cdot\nabla)S
+\frac13S^2
+\frac14\omega\otimes\omega
\right)
$$

establish a truly ancestry-localized scale-critical dual norm, and compare $\mathfrak P_{I,\chi}^{\rm mult}$, the weighted $\dot H^{-1}$ norm, and the projection/cutoff commutator.

## P2 — Small-operator regime

If a certain **localized** operator defect $\mathfrak P_n^{\rm loc}\to0$, can it be rigorously proven that the rescaled ancestry dynamics approach the SSA model?

A stability theorem is needed, not a balance identity.

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

## P5 — Betchov-current spectral/helical split

Investigate the homochiral / heterochiral contributions of $F_B$ and its source $\operatorname{tr}(G^3)$ under Fourier/helical decomposition.

Must retain the guard: helical decomposition is inherently a spectral/nonlocal representation, and cannot be directly termed a physical-space "local helical split".

## P6 — Cancellation corridor operator test

If:

$$
\rho_n\to-1^+,
$$

determine whether the cancellation corridor can imply any localized operator-defect lower bound; currently, one cannot automatically deduce from the scalar balance identity that

$$
\mathfrak P_n^{\rm loc}\to\infty.
$$

## P7 — Balance/operator phase diagram

Establish the:

$$
(\rho_n,\mathfrak P_n^{\rm loc})
$$

possible / known-regular / model-like-dangerous / open regions for each branch.

## P8 — Adjoint cutoff propagation

Analyze the effective radius, Gaussian/Aronson-type tails, drift distortion, and pressure sensitivity of the terminal ancestry cutoff toward earlier times; backward persistence of compact support must not be assumed.

---

# 35. Formal Status

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
\rho_I\le-1\text{ with }A_I>0\text{ growth sector}
&:\ \mathrm{EXCLUDED},\\
\text{cancellation-precision debt}
&:\ \mathrm{PROVED},\\
\rho\to0\Rightarrow\text{SSA operator closeness from }\rho\text{ alone}
&:\ \mathrm{NON\mbox{-}IDENTIFIABLE/NO\mbox{-}GO},\\
\langle\mathcal P_{NS},S\rangle=0
&:\ \mathrm{PROVED\ HERE\ UNDER\ DECAY},\\
\text{SSA model finite-time blowup}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{conditional full-NS blowup under perturbative condition}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\mathfrak P_I^{\rm glob}\text{ scale invariance}
&:\ \mathrm{PROVED},\\
\mathfrak P_I^{\rm glob}\text{ as stability criterion}
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

it must be that:

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

is the true hard depletion sector.

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

The perturbation discarded from the full N–S by the SSA model is exactly orthogonal to the global strain energy,

so its pairing with the instantaneous enstrophy derivative can be exactly zero,

but this scalar zero does not preclude it from having a significant effect on the future dynamics.

Therefore, the scalar ratio route has reached its limit as a **standalone rigidity route**; it can still be retained as a growth-carrier classifier and used in conjunction with operator diagnostics.

The next round must upgrade to:

$$
\boxed{
\textbf{C3-P — Operator-Level Depletion and Pressure/Betchov Current Rigidity}.
}
$$

---

# 37. v0.2 theorem-safety guards

## T-SCOPE

All C3-O ratio theorems are smooth/pre-singular window identities or their algebraic consequences; this text does not elevate them into weak-solution singularity theorems.

## T-RATIO-DOMAIN

$\rho_I=B_I/A_I$ is only used in the ratio branch where $A_I>0$. Positive-growth windows with $A_I\le0$ are separately categorized into the boundary-current-driven branch.

## T-ADJOINT-TAIL

The adjoint cutoff eliminates the scalar cutoff transport/diffusion package; it does not eliminate spatial communication or pressure nonlocality.

## T-ORTHO

$\langle\mathcal P_{NS},S\rangle=0$ is a scalar orthogonality; it must not be translated into $\mathcal P_{NS}$ norm smallness.

## T-MILLER

Miller's conditional blow-up theorem uses a specific $L^2$ relative perturbation hypothesis; it must not be conflated with the $\dot H^{-1}$ diagnostic of this text.

## T-LOCALITY

$\mathfrak P_I^{\rm glob}$ is a whole-space/window diagnostic; $\mathfrak P_{I,\chi}^{\rm mult}$ is merely a cutoff-weighted candidate, because $\dot H^{-1}$ remains nonlocal. The true C3-P local stability route still requires establishing $\mathfrak P^{\rm loc}$ and cutoff/projection commutator control.

---

# References

1. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, Analysis & PDE 16 (2023), 997–1032; arXiv:1910.05415v6. The conditional full Navier–Stokes blow-up statement used here is Theorem 1.14 / Section 6 in the arXiv v6 numbering.
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, Pure and Applied Analysis 8 (2026), 247–270; arXiv:2407.02691v2.
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