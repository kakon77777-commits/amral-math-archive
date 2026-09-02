# NS × X Integration × 24/72 Paradigm Practice
## Round 37 — Pure Continuous Pressure-Response Defect Energy / Affine-Lock Budget Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Pressure-Response-Defect Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round36_PureContinuous_CofactorPressure_CoherenceDynamics_v0.1_2026-08-17.md`
- Objective of this round: Round 36 has proved that the cofactor–pressure replenishing coherence does not exhibit universal dephasing, and that the affine stationary strain can achieve a perfect response
  $$
  H_p^0=-C_S^0.
  $$
  This round uses
  $$
  E_p=H_p^0+C_S^0
  $$
  as the affine-response defect to establish its exact PDE and global / moving-domain defect-energy budget, identifying the true forcing sources and critical regularity costs of the near-affine pressure lock.
- Non-claims: This document does not prove that $E_p$ decays unconditionally, nor does it prove that finite-energy NS cannot maintain a small $E_p$ for a long time. Conversely, this round proves that the local strain coupling of the defect equation is not coercive, and that the true forcing still contains higher gradients and the transport–Riesz commutator.

---

# 0. Round 36 handoff

Let:

$$
C
=
C_S^0
=
S^2-\frac13|S|^2I,
$$

and:

$$
H
=
H_p^0.
$$

negative determinant reserve domain:

$$
A_-(t)
=
\{x:-\det S<0\}.
$$

Round 36 pressure replenishing coherence:

$$
\boxed{
\rho_p^-
=
-
\frac{
\langle C,H\rangle_{A_-}
}{
\|C\|_{2,A_-}
\|H\|_{2,A_-}
}.
}
\tag{0.1}
$$

stationary affine structural witness:

$$
u(x)=S_0x,
$$

$$
p(x)
=
-\frac12x^\top S_0^2x
$$

gives:

$$
\boxed{
H_p^0=-C_S^0,
\qquad
\rho_p^-=1.
}
\tag{0.2}
$$

Thus, universal dephasing is false.

Round 36 STOP:

$$
\boxed{
\text{STOP-C40}
=
\text{Cofactor–Pressure Lock / Moving-Domain Commutator Gap}.
}
$$

---

# 1. Affine-response defect

Define:

$$
\boxed{
E
=
E_p
=
H+C.
}
\tag{1.1}
$$

perfect affine pressure response:

$$
H=-C
$$

is equivalent to:

$$
\boxed{
E=0.
}
\tag{1.2}
$$

Therefore:

$$
E
$$

simultaneously measures:

- anisotropic pressure amplitude mismatch;
- tensor orientation mismatch;
- nonlocal departure from affine local response.

---

# 2. Defect energy is exactly the replenishment loss

In:

$$
A_-,
$$

let:

$$
\boxed{
U
=
\|C\|_{2,A_-},
\qquad
V
=
\|H\|_{2,A_-}.
}
\tag{2.1}
$$

From:

$$
\rho
=
-\frac{
\langle C,H\rangle
}{
UV
},
$$

we have:

$$
\boxed{
\begin{aligned}
\mathcal D_p^-
:=
\|E\|_{2,A_-}^2
&=
U^2+V^2-2\rho UV
\\
&=
(U-V)^2
+
2UV(1-\rho).
\end{aligned}
}
\tag{2.2}
$$

Round 35 anisotropic pressure replenishment:

$$
\mathcal P_{\rm aniso}
=
2\rho UV.
$$

Therefore:

$$
\boxed{
\mathcal P_{\rm aniso}
=
U^2+V^2
-
\mathcal D_p^-.
}
\tag{2.3}
$$

Named:

$$
\boxed{
\textbf{Affine-Response Defect Identity}.
}
$$

Thus:

> relative to the available cofactor/pressure amplitude $U^2+V^2$, every loss of anisotropic replenishment is exactly measured by $\|E\|^2$.

---

# 3. Pressure-response efficiency

If:

$$
U^2+V^2>0,
$$

define:

$$
\boxed{
\eta_{\rm aff}^-
=
\frac{
\mathcal P_{\rm aniso}
}{
U^2+V^2
}
=
1-
\frac{
\mathcal D_p^-
}{
U^2+V^2
}.
}
\tag{3.1}
$$

Then:

$$
\boxed{
-1
\le
\eta_{\rm aff}^-
\le
1.
}
\tag{3.2}
$$

Interpretation:

$$
\eta_{\rm aff}^-=1
$$

represents:

$$
H=-C
$$

perfect response;

$$
\eta_{\rm aff}^-\approx1
$$

represents:

- amplitudes nearly matched;
- tensors nearly anti-aligned.

Therefore:

$$
\boxed{
E
}
$$

is stronger than the single coherence:

$$
\rho
$$

because it simultaneously captures both amplitude and angle.

---

# 4. Viscous cofactor decomposition

Round 36:

$$
\mathcal A_\nu
=
\nu
\left[
(\Delta S)S
+
S(\Delta S)
-
\frac23
(S:\Delta S)I
\right].
$$

But:

$$
C
=
S^2-\frac13|S|^2I.
$$

direct Laplacian:

$$
\boxed{
\begin{aligned}
\Delta C
={}&
(\Delta S)S
+
S(\Delta S)
-
\frac23
(S:\Delta S)I
\\
&+
2
\sum_k
\left[
(\partial_kS)^2
-
\frac13
|\partial_kS|^2I
\right].
\end{aligned}
}
\tag{4.1}
$$

Define the trace-free quadratic gradient tensor:

$$
\boxed{
Q_C
=
\sum_k
\left[
(\partial_kS)^2
-
\frac13
|\partial_kS|^2I
\right].
}
\tag{4.2}
$$

Thus:

$$
\boxed{
\mathcal A_\nu
=
\nu\Delta C
-
2\nu Q_C.
}
\tag{4.3}
$$

---

# 5. Pressure substitution into cofactor dynamics

Round 36 pressure contribution:

$$
\mathcal A_p
=
-
(H_pS+SH_p)
+
\frac23
(S:H_p)I.
$$

Write:

$$
\boxed{
H_p
=
H
+
\frac{\Delta p}{3}I
=
E-C-\frac q3I,
}
\tag{5.1}
$$

where:

$$
\boxed{
q
=
|S|^2-\frac12|\omega|^2
=
-\Delta p.
}
\tag{5.2}
$$

Using:

$$
C=S^2-\frac13|S|^2I,
$$

$$
S:C=3\det S,
$$

and Cayley–Hamilton,

it simplifies to:

$$
\boxed{
\mathcal A_p
=
-
(ES+SE)
+
\frac23
(S:E)I
+
|S|^2S
-
\frac13|\omega|^2S.
}
\tag{5.3}
$$

---

# 6. Exact cancellation of pure strain self-amplification in the defect frame

Round 36 self term:

$$
\mathcal A_{\rm self}
=
-|S|^2S.
$$

Adding to (5.3):

$$
\boxed{
\mathcal A_{\rm self}
+
\mathcal A_p
=
-
(ES+SE)
+
\frac23
(S:E)I
-
\frac13|\omega|^2S.
}
\tag{6.1}
$$

Therefore:

$$
\boxed{
\textbf{
once pressure is measured relative to the affine response }H=-C,
\textbf{ the pure strain self-amplification cancels exactly from the cofactor defect dynamics.}
}
\tag{6.2}
$$

This is the first core structural cancellation of this round.

---

# 7. Reduced vorticity forcing

Round 36:

$$
\begin{aligned}
\mathcal A_\omega
={}&
-\frac14
[
(\omega\otimes\omega)S
+
S(\omega\otimes\omega)
]
\\
&+
\frac12|\omega|^2S
+
\frac16
(\omega^\top S\omega)I.
\end{aligned}
$$

Combined with (6.1)'s:

$$
-\frac13|\omega|^2S
$$

, define:

$$
\boxed{
\begin{aligned}
V_C
={}&
-\frac14
[
(\omega\otimes\omega)S
+
S(\omega\otimes\omega)
]
\\
&+
\frac16|\omega|^2S
+
\frac16
(\omega^\top S\omega)I.
\end{aligned}
}
\tag{7.1}
$$

Thus, the exact cofactor equation is:

$$
\boxed{
D_tC
-
\nu\Delta C
=
-
L_S(E)
-
2\nu Q_C
+
V_C,
}
\tag{7.2}
$$

where:

$$
\boxed{
L_S(E)
=
ES+SE
-
\frac23
(S:E)I.
}
\tag{7.3}
$$

---

# 8. Pressure-source equation in defect variables

Round 36:

$$
D_tq
=
\nu\Delta q
-
2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
-
6\det S
-
\frac32\omega^\top S\omega
-
2S:H_p.
$$

Since:

$$
S:H_p
=
S:H
=
S:(E-C)
=
S:E
-
3\det S,
$$

we have:

$$
\boxed{
-6\det S
-
2S:H_p
=
-2S:E.
}
\tag{8.1}
$$

Therefore:

$$
\boxed{
D_tq
=
\nu\Delta q
+
N_0
-
2S:E,
}
\tag{8.2}
$$

where:

$$
\boxed{
N_0
=
-2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
-
\frac32
\omega^\top S\omega.
}
\tag{8.3}
$$

This is the second exact cancellation:

$$
\boxed{
\textbf{
the explicit determinant source cancels from the pressure-source equation
when written in affine-response defect variables.
}
}
\tag{8.4}
$$

---

# 9. Anisotropic pressure response equation

Let the trace-free pressure operator be:

$$
\boxed{
\mathcal T_0
=
\nabla^2(-\Delta)^{-1}
+
\frac13I.
}
\tag{9.1}
$$

Then:

$$
H=\mathcal T_0q.
$$

Round 36:

$$
\boxed{
D_tH
-
\nu\Delta H
=
\mathcal T_0
(
N_0-2S:E
)
+
\mathcal C_{u,\mathcal T_0}[q],
}
\tag{9.2}
$$

where:

$$
\boxed{
\mathcal C_{u,\mathcal T_0}[q]
=
[u\cdot\nabla,\mathcal T_0]q.
}
\tag{9.3}
$$

---

# 10. Exact affine-response defect equation

Add (7.2) and (9.2).

Define the linear defect operator:

$$
\boxed{
\mathscr L_S[E]
=
L_S(E)
+
2
\mathcal T_0(S:E).
}
\tag{10.1}
$$

Define the external defect forcing:

$$
\boxed{
\mathcal F_E
=
-2\nu Q_C
+
V_C
+
\mathcal T_0N_0
+
\mathcal C_{u,\mathcal T_0}[q].
}
\tag{10.2}
$$

We obtain:

$$
\boxed{
D_tE
-
\nu\Delta E
=
-
\mathscr L_S[E]
+
\mathcal F_E.
}
\tag{10.3}
$$

Named:

$$
\boxed{
\textbf{Affine-Response Defect Equation}.
}
$$

This is the most important exact equation of this round.

---

# 11. What actually forces departure from affine pressure response

Equation (10.3) shows that:

$$
E=0
$$

near $E=0$, the defect sources are divided into:

## F1 — local strain-gradient quadratic mismatch

$$
\boxed{
-2\nu Q_C.
}
$$

## F2 — vorticity/cofactor forcing

$$
\boxed{
V_C.
}
$$

## F3 — transformed pressure-source mismatch

$$
\boxed{
\mathcal T_0N_0.
}
$$

where:

$$
N_0
=
-2\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
-
\frac32\omega^\top S\omega.
$$

## F4 — transport–Riesz mismatch

$$
\boxed{
[u\cdot\nabla,\mathcal T_0]q.
}
$$

Therefore, neither the pure $S^2$ self-amplification nor the explicit determinant source are independent defect forcings anymore.

---

# 12. Global defect-energy identity

In the whole-space smooth decaying branch:

$$
\nabla\cdot u=0.
$$

From (10.3):

$$
\boxed{
\begin{aligned}
\frac12
\frac d{dt}
\|E\|_2^2
+
\nu
\|\nabla E\|_2^2
={}&
-
\langle
E,
\mathscr L_S[E]
\rangle
\\
&+
\langle
E,
\mathcal F_E
\rangle.
\end{aligned}
}
\tag{12.1}
$$

local part:

$$
\boxed{
\langle
E,
L_S(E)
\rangle
=
2
\int
\operatorname{tr}
(
SE^2
)dx.
}
\tag{12.2}
$$

Since:

$$
E
$$

is trace-free.

Therefore:

$$
\boxed{
\begin{aligned}
\frac12
(\|E\|_2^2)'
+
\nu\|\nabla E\|_2^2
={}&
-2
\int
\operatorname{tr}(SE^2)dx
\\
&-
2
\langle
E,
\mathcal T_0(S:E)
\rangle
\\
&+
\langle
E,\mathcal F_E\rangle.
\end{aligned}
}
\tag{12.3}
$$

---

# 13. Local defect-strain term has no coercive sign

Take:

$$
S
=
a
\operatorname{diag}
(-2,1,1),
\qquad
a>0.
$$

Let:

$$
E_1
=
\operatorname{diag}
(2,-1,-1).
$$

Then:

$$
\operatorname{tr}
(
SE_1^2
)
=
-6a,
$$

Thus:

$$
\boxed{
-2
\operatorname{tr}
(
SE_1^2
)
=
12a>0.
}
\tag{13.1}
$$

This amplifies the defect energy.

Alternatively, take:

$$
E_2
=
\operatorname{diag}
(0,1,-1),
$$

Then:

$$
\operatorname{tr}
(
SE_2^2
)
=
2a,
$$

Thus:

$$
\boxed{
-2
\operatorname{tr}
(
SE_2^2
)
=
-4a<0.
}
\tag{13.2}
$$

This dissipates the defect.

Therefore:

$$
\boxed{
\textbf{
the local strain action on the affine-response defect is sign-indefinite.
}
}
\tag{13.3}
$$

There is no purely algebraic defect damping.

---

# 14. Critical estimate for the linear defect operator

Sobolev:

$$
\|E\|_6
\lesssim
\|\nabla E\|_2.
$$

local term:

$$
\boxed{
\left|
\int
\operatorname{tr}(SE^2)dx
\right|
\le
C
\|S\|_3
\|E\|_2
\|\nabla E\|_2.
}
\tag{14.1}
$$

For the Riesz linear part,

$\mathcal T_0$ is bounded on:

$$
L^{6/5},
$$

Thus:

$$
\boxed{
\left|
\langle
E,
\mathcal T_0(S:E)
\rangle
\right|
\le
C
\|S\|_3
\|E\|_2
\|\nabla E\|_2.
}
\tag{14.2}
$$

Therefore:

$$
\boxed{
\left|
\langle
E,
\mathscr L_S[E]
\rangle
\right|
\le
C
\|S\|_3
\|E\|_2
\|\nabla E\|_2.
}
\tag{14.3}
$$

---

# 15. Conditional defect-energy inequality

If:

$$
\mathcal F_E
\in
L^{6/5},
$$

Then:

$$
\left|
\langle
E,\mathcal F_E
\rangle
\right|
\le
C
\|\nabla E\|_2
\|\mathcal F_E\|_{6/5}.
$$

Young's inequality gives:

$$
\boxed{
\frac d{dt}
\|E\|_2^2
+
\nu
\|\nabla E\|_2^2
\le
\frac{
C
}{
\nu
}
\|S\|_3^2
\|E\|_2^2
+
\frac{
C
}{
\nu
}
\|\mathcal F_E\|_{6/5}^2.
}
\tag{15.1}
$$

So if:

$$
\boxed{
\int_0^T
\|S\|_3^2dt
<\infty
}
\tag{15.2}
$$

and:

$$
\boxed{
\int_0^T
\|\mathcal F_E\|_{6/5}^2dt
<\infty,
}
\tag{15.3}
$$

then:

$$
\|E(t)\|_2
$$

is controlled by Gronwall's inequality.

---

# 16. Criticality of the strain coefficient

NS scaling:

$$
S_\Lambda
=
\Lambda^2
S(\Lambda x,\Lambda^2t).
$$

Therefore:

$$
\|S_\Lambda\|_3
=
\Lambda
\|S\|_3.
$$

Thus:

$$
\boxed{
\int
\|S\|_3^2dt
}
\tag{16.1}
$$

is scale invariant.

That is, the defect-energy closure naturally hits the gradient Serrin critical line:

$$
\boxed{
S
\in
L_t^2L_x^3.
}
$$

Therefore, (15.2) cannot be treated as a free global-regularity hypothesis.

Named:

$$
\boxed{
\textbf{Affine-Defect Criticality Barrier}.
}
$$

---

# 17. External defect forcing is higher-order

From:

$$
Q_C
=
O(|\nabla S|^2),
$$

$$
V_C
=
O(|S||\omega|^2),
$$

and:

$$
N_0
=
O(
\nu|\nabla S|^2
+
\nu|\nabla\omega|^2
+
|S||\omega|^2
),
$$

we obtain the schematic:

$$
\boxed{
\begin{aligned}
\|\mathcal F_E\|_{6/5}
\lesssim{}&
\nu
\||\nabla S|^2\|_{6/5}
+
\nu
\||\nabla\omega|^2\|_{6/5}
\\
&+
\||S||\omega|^2\|_{6/5}
+
\|
[u\cdot\nabla,\mathcal T_0]q
\|_{6/5}.
\end{aligned}
}
\tag{17.1}
$$

For example:

$$
\boxed{
\||\nabla S|^2\|_{6/5}
=
\|\nabla S\|_{12/5}^2
}
\tag{17.2}
$$

is already higher than the basic energy level.

and:

$$
\boxed{
\||S||\omega|^2\|_{6/5}
\le
\|S\|_3
\|\omega\|_4^2.
}
\tag{17.3}
$$

Thus, the external defect forcing still burns:

- higher derivatives;
- quartic strain/vorticity;
- transport commutator.

---

# 18. Transport–Riesz commutator kernel

Let:

$$
K_0(z)
$$

be the trace-free singular kernel of:

$$
\mathcal T_0
$$

For smooth decaying data,

using:

$$
\nabla\cdot u=0,
$$

we can write:

$$
\boxed{
\begin{aligned}
\mathcal C_{u,\mathcal T_0}[q](x)
=
\operatorname{p.v.}
\int
[
u(x)-u(y)
]
\cdot
\nabla K_0(x-y)
q(y)dy.
\end{aligned}
}
\tag{18.1}
$$

where:

$$
\boxed{
|\nabla K_0(z)|
\sim
|z|^{-4}.
}
\tag{18.2}
$$

If:

$$
u
$$

is Lipschitz,

the velocity increment:

$$
u(x)-u(y)
=
O(|x-y|)
$$

recovers one power,

bringing the effective singularity back to:

$$
|z|^{-3}
$$

the Calderón–Zygmund level.

Therefore:

$$
\boxed{
\textbf{
the pressure-response commutator is controlled by velocity-increment regularity,
not by pressure amplitude alone.
}
}
\tag{18.3}
$$

---

# 19. Commutator budget is not automatically low-order

In the strong regularity branch, one can expect the schematic:

$$
\boxed{
\|
[u\cdot\nabla,\mathcal T_0]q
\|_p
\lesssim
\|\nabla u\|_\infty
\|q\|_p.
}
\tag{19.1}
$$

But:

$$
\|\nabla u\|_\infty
$$

is far above the energy level.

Riesz-type transport commutator estimates under weaker velocity regularity are inherently delicate.

Therefore, affine-response lock maintenance / dephasing once again translates to:

$$
\boxed{
\text{critical velocity increment / commutator budget}.
}
$$

---

# 20. Moving negative-domain defect energy

Define:

$$
\boxed{
\mathcal D_-(t)
=
\int_{A_-(t)}
|E|^2dx.
}
\tag{20.1}
$$

Round 36 sign-boundary relative speed:

$$
\boxed{
\beta_d
=
\frac{
D_td
}{
|\nabla d|
}
}
\tag{20.2}
$$

with:

$$
V_n-u\cdot\eta=-\beta_d.
$$

From moving-domain transport and the defect PDE:

$$
\boxed{
\begin{aligned}
\frac12
\mathcal D_-'
+
\nu
\int_{A_-}
|\nabla E|^2dx
={}&
-
\int_{A_-}
E:\mathscr L_S[E]dx
\\
&+
\int_{A_-}
E:\mathcal F_Edx
\\
&+
\mathcal B_E,
\end{aligned}
}
\tag{20.3}
$$

where the boundary leakage is:

$$
\boxed{
\mathcal B_E
=
\int_{\partial A_-}
\left[
\nu
E:\partial_\eta E
-
\frac12
\beta_d
|E|^2
\right]dS.
}
\tag{20.4}
$$

Thus, the negative-reserve pressure lock also requires controlling the moving sign boundary.

---

# 21. Global defect versus reserve-domain defect

Global:

$$
\|E\|_2^2
$$

has no moving-domain boundary term.

Local replenishment defect:

$$
\mathcal D_-
$$

directly corresponds to:

$$
\mathcal P_{\rm aniso}
$$

but has the additional:

$$
\mathcal B_E.
$$

Therefore, there are two proof strategies:

## G — global defect route

First control:

$$
\|E\|_2,
$$

which automatically controls:

$$
\mathcal D_-.
$$

But this incurs costs for all spatial regions.

## L — local reserve-domain route

Only controls:

$$
A_-,
$$

which is sharper,

but must pay for:

$$
\boxed{
\text{sign-boundary leakage}.
}
$$

---

# 22. Near-affine lock is not automatically attracting

The affine witness proves that:

$$
E=0
$$

can be an exact structural lock.

But Section 13 shows that the local linearized defect-strain term can be positive or negative.

Sections 18–19 show that the commutator can also provide sustained forcing.

Therefore:

$$
\boxed{
\textbf{
perfect affine response can be invariant without being universally attracting.
}
}
\tag{22.1}
$$

Proving that finite-energy flow approaches:

$$
E=0
$$

requires genuine defect-energy estimates, rather than relying on geometric intuition.

---

# 23. Defect-source cancellation hierarchy

This round's affine-response choice:

$$
E=H+C
$$

results in two exact cancellations:

## C1

in the cofactor dynamics, the:

$$
\boxed{
\text{pure }-S^2\text{ self-amplification}
}
$$

is cancelled by the affine pressure response part.

## C2

in the pressure-source equation, the:

$$
\boxed{
-6\det S
}
$$

is cancelled by the cofactor component in:

$$
-2S:H_p
$$

Therefore, the remaining defect core is:

$$
\boxed{
\text{vorticity}
+
\text{spatial gradients}
+
\text{transport–Riesz commutator}
+
\text{defect-linear strain response}.
}
\tag{23.1}
$$

This is much cleaner than directly studying:

$$
H_p^0
$$

---

# 24. Affine-response defect state

We can define:

$$
\boxed{
X_{\rm aff}
=
\left\langle
\|E\|_2^2,
\mathcal D_-,
\eta_{\rm aff}^-,
\|S\|_3,
\|\mathcal F_E\|_{6/5},
\mathcal B_E
\right\rangle.
}
\tag{24.1}
$$

where:

- $\|E\|_2^2$: global response mismatch;
- $\mathcal D_-$: replenishment-domain mismatch;
- $\eta_{\rm aff}^-$: pressure replenishment efficiency;
- $\|S\|_3$: critical linear defect rate;
- $\mathcal F_E$: external defect forcing;
- $\mathcal B_E$: sign-boundary leakage.

All of these remain continuous carriers.

---

# 25. Conditional near-affine response theorem

Assume a smooth decaying NS solution on:

$$
[0,T]
$$

and:

$$
\int_0^T
\|S\|_3^2dt
\le
A<\infty,
$$

$$
\int_0^T
\|\mathcal F_E\|_{6/5}^2dt
\le
B<\infty.
$$

Then from (15.1):

$$
\boxed{
\sup_{t\le T}
\|E(t)\|_2^2
\le
C_{\nu,A}
\left[
\|E(0)\|_2^2
+
B
\right].
}
\tag{25.1}
$$

and:

$$
\boxed{
\nu
\int_0^T
\|\nabla E\|_2^2dt
\le
C_{\nu,A}
\left[
\|E(0)\|_2^2
+
B
\right].
}
\tag{25.2}
$$

This is a genuine conditional pressure-response defect estimate.

However, the assumptions precisely expose the critical/higher-order cost.

---

# 26. Why this does not close global regularity

Currently, we have not yet controlled:

$$
\int
\|S\|_3^2dt
$$

or:

$$
\int
\|\mathcal F_E\|_{6/5}^2dt
$$

by the basic energy.

Specifically:

- $\|S\|_{L_t^2L_x^3}$ is already at the critical gradient scale;
- $\mathcal F_E$ contains higher-gradient squares;
- the commutator requires velocity-increment regularity;
- the local $A_-$ route additionally has boundary leakage.

Therefore:

$$
\boxed{
\text{defect equation is structurally cleaner,
but not yet subcritical/coercive enough to close NS regularity}.
}
$$

---

# 27. STOP-C41 — Affine-Response Defect / Critical Commutator–Gradient Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{pressure\text{-}response\ defect\ energy},
\\
\text{defect}
&=
E_p
=
H_p^0+C_S^0,
\\
\text{replenishment loss}
&=
\|E_p\|_{2,A_-}^2,
\\
\text{pure self-amplification defect forcing}
&=
0,
\\
\text{explicit determinant defect forcing}
&=
0,
\\
\text{remaining forcing}
&=
\mathrm{vorticity}
+
\mathrm{gradient\ quadratic}
+
\mathrm{transport\text{-}Riesz\ commutator},
\\
\text{local defect-strain sign}
&=
\mathrm{indefinite},
\\
\text{critical linear coefficient}
&=
S\in L_t^2L_x^3,
\\
\text{external defect budget}
&=
\mathcal F_E\in L_t^2L_x^{6/5},
\\
\text{moving reserve-domain leakage}
&=
\mathcal B_E,
\\
\text{missing}
&=
\mathrm{unconditional\ critical\ control
of\ strain,\ higher\ gradients,\ commutator,\ and\ sign\text{-}boundary\ flux},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Named:

$$
\boxed{
\textbf{STOP-C41:
Affine-Response Defect / Critical Commutator–Gradient Gap}.
}
$$

---

# 28. 24/72 Ledger — Round 37

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C549 | affine-response defect $E_p$ | $\mathsf C$ | tensor relation | relational | $\mathsf F$ | FORM |
| C550 | defect/replenishment identity | $\mathsf C$ | Hilbert geometry | targeted | $\mathsf F$ | EXACT |
| C551 | response efficiency $\eta_{\rm aff}$ | $\mathsf C$ | normalization | scalar | $\mathsf F$ | FORM |
| C552 | viscous cofactor decomposition | $\mathsf C$ | tensor Laplacian | relational | $\mathsf F$ | EXACT |
| C553 | pressure substitution | $\mathsf C$ | tensor algebra | relational | $\mathsf F$ | EXACT |
| C554 | self-amplification defect cancellation | $\mathsf C$ | algebra/PDE | targeted | $\mathsf F$ | EXACT |
| C555 | reduced vorticity forcing $V_C$ | $\mathsf C$ | tensor coupling | relational | $\mathsf F$ | EXACT |
| C556 | pressure-source determinant cancellation | $\mathsf C$ | source PDE | targeted | $\mathsf F$ | EXACT |
| C557 | Affine-Response Defect Equation | $\mathsf C$ | coupled PDE | tensor | $\mathsf F$ | EXACT |
| C558 | global defect-energy identity | $\mathsf C$ | energy | scalar | $\mathsf F$ | EXACT |
| C559 | local defect-strain sign witness | $\mathsf C$ | tensor geometry | targeted | $\mathsf F$ | CONSTRUCTED |
| C560 | critical linear defect estimate | $\mathsf C$ | Sobolev/Riesz | scalar | $\mathsf F$ | PROVED |
| C561 | conditional defect-energy inequality | $\mathsf C$ | Gronwall | targeted | $\mathsf F$ | PROVED |
| C562 | affine-defect criticality barrier | $\mathsf C$ | scaling | scalar | $\mathsf F$ | IDENTIFIED |
| C563 | external forcing hierarchy | $\mathsf C$ | higher derivatives | relational | $\mathsf F$ | IDENTIFIED |
| C564 | transport–Riesz kernel form | $\mathsf C$ | singular integral | relational | $\mathsf F$ | EXACT |
| C565 | moving-domain defect energy | $\mathsf C$ | level-set energy | scalar | $\mathsf F$ | EXACT |
| C566 | conditional near-affine theorem | $\mathsf C$ | defect control | targeted | $\mathsf F$ | CONDITIONAL |
| C567 | unconditional defect closure | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C41 |

---

# 29. Continuous-versus-discrete status

This round entirely uses:

- continuous tensor defect;
- continuous Hilbert energy;
- continuous Riesz operator;
- continuous transport commutator;
- continuous moving sign domain;
- continuous Sobolev critical norms.

It does not use:

- affine-state enumeration;
- pressure mode lattice;
- discrete defect states;
- discrete commutator expansion.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 30. Strongest results of Round 37

## R37-A — Affine-Response Defect Identity

$$
\boxed{
\|H_p^0+C_S^0\|_{2,A_-}^2
=
(U-V)^2
+
2UV(1-\rho_p^-).
}
$$

and:

$$
\boxed{
\mathcal P_{\rm aniso}
=
U^2+V^2
-
\|H_p^0+C_S^0\|_{2,A_-}^2.
}
$$

## R37-B — exact defect PDE

$$
\boxed{
D_tE_p
-
\nu\Delta E_p
=
-
\mathscr L_S[E_p]
+
\mathcal F_E.
}
$$

## R37-C — self-amplification and determinant cancellation

in defect variables:

$$
\boxed{
\text{pure }-S^2\text{ forcing cancels},
}
$$

and:

$$
\boxed{
\text{explicit }-6\det S\text{ pressure-source term cancels}.
}
$$

## R37-D — defect-energy budget

$$
\boxed{
\frac d{dt}
\|E_p\|_2^2
+
\nu\|\nabla E_p\|_2^2
\lesssim
\nu^{-1}
\|S\|_3^2
\|E_p\|_2^2
+
\nu^{-1}
\|\mathcal F_E\|_{6/5}^2.
}
$$

## R37-E — critical obstruction

the natural coefficient:

$$
\boxed{
S\in L_t^2L_x^3
}
$$

is scale-critical, while $\mathcal F_E$ contains higher-gradient and transport–Riesz commutator budgets.

---

# 31. Next round — Transport–Riesz Commutator Depletion

Round 37 has singled out the most independent nonlocal obstruction in the near-affine pressure lock as:

$$
\boxed{
\mathcal C_{u,\mathcal T_0}[q]
=
[u\cdot\nabla,\mathcal T_0]q.
}
$$

The next round will directly investigate:

1. the exact increment kernel:
   $$
   [u(x)-u(y)]\cdot\nabla K_0(x-y);
   $$
2. whether incompressibility can generate additional cancellation;
3. whether the symmetric second-difference / Cancellation-First Principle can be applied once more;
4. what commutator budgets Lipschitz, BMO, and critical Sobolev spaces can respectively provide;
5. whether the commutator pairing
   $$
   \langle E_p,\mathcal C_{u,\mathcal T_0}[q]\rangle
   $$
   can be handled better than a standalone norm estimate;
6. if the pairing possesses a hidden skew/cancellation structure, it might reduce the defect forcing;
7. if not, the commutator will require genuine critical velocity-increment control;
8. maintaining the continuous kernel without performing Fourier shell discretization.

---

# 32. External primary-source anchors

1. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - Primary-source background for whole-space pressure determined by Riesz transforms.

2. Elias Hess-Childs, Matthew Rosenzweig, Sylvia Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326.
   - Velocity-regularity sensitivity of Riesz-type transport commutator estimates; specifically explaining that in general, the Lipschitz-gradient requirement cannot be arbitrarily lowered to BMO.

3. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - Background on strain–vorticity interaction, higher-gradient identities, and nonlinear depletion.

The Affine-Response Defect Identity, defect PDE, two exact source cancellations, critical defect-energy inequality, and transport–Riesz kernel form in this round are all directly derived in this document.

---

# 33. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Pressure\text{-}Response\ Defect\ Energy},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Perfect affine response}
&=
E_p=0,
\\
\text{Pressure replenishment loss}
&=
\|E_p\|_{2,A_-}^2,
\\
\text{Pure strain self forcing}
&=
\mathrm{cancelled\ in\ defect\ coordinates},
\\
\text{Explicit determinant source}
&=
\mathrm{cancelled\ in\ pressure\ source},
\\
\text{Remaining defect forcing}
&=
\mathrm{vorticity}
+
\mathrm{gradient}
+
\mathrm{transport\text{-}Riesz\ commutator},
\\
\text{Defect linear control}
&=
S\in L_t^2L_x^3\text{ critical},
\\
\text{STOP-C41}
&=
\mathrm{Affine\text{-}Response\ Defect/Critical\ Commutator\text{-}Gradient\ Gap},
\\
\text{Next}
&=
\mathrm{Transport\text{-}Riesz\ Commutator\ Depletion}.
\end{aligned}
}
$$