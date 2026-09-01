---
title: "Navier–Stokes Reverse Formation Program 04: Adjoint Spacetime Tube Ledger, Pressure-Compatible Localization, and Quantitative Uniform Parent Tightness"
short_title: "NS-RFP 04"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural advance / frequency-to-spacetime bridge"
epistemic_status: "Builds an exact adjoint spacetime-tube refinement of the RFP-03 parent ledger; proves a pressure-compatible band-passed Leray commutator estimate and pseudolocality; derives a scale-invariant quantitative tail bound that upgrades parent tightness whenever a dissipation-output budget is bounded. Does NOT prove that this budget is universally bounded, witness persistence across all edges, full Chain Necessity, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 04

# Adjoint Spacetime Tube Ledger, Pressure-Compatible Localization, and Quantitative Uniform Parent Tightness

## 0. Context of this Paper

NS-RFP 03 has upgraded the aggregate nonlinear source debt of the PF-A source-paid first-passage edge into an exact signed dyadic parent-output ledger:

$$
\boxed{
R_J
=
\sum_{k,p,q}
\Lambda^{(J)}_{k;p,q}
\ge
d_J.
}
$$

where:

$$
(k;p,q)
$$

are exact dyadic output-parent labels.

RFP-03 also proved that:

$$
\text{far upward quadratic jump}
$$

is impossible, and a large positive parent-output gap:

$$
g(k;p,q)
=
\max\{p,q\}-k
$$

can only be paid by near-resonant high--high parents.

However, RFP-03 leaves two immediate gaps:

$$
\boxed{
\text{per-edge parent tightness}
\not\Rightarrow
\text{uniform chain tightness},
}
$$

and:

$$
\boxed{
\text{global-frequency provenance}
\not\Rightarrow
\text{spacetime provenance}.
}
$$

This paper tackles both of these problems simultaneously.

Core results:

1. Establish the scale-invariant dissipation-output budget:
   $$
   \mathfrak V_J
   =
   \mathfrak E_J\mathfrak O_J;
   $$
2. Prove the quantitative parent-tail estimate:
   $$
   \boxed{
   1-C_J^{par}(L)
   \le
   C2^{-L}\mathfrak V_J;
   }
   $$
3. Consequently:
   $$
   \sup_J\mathfrak V_J<\infty
   \Longrightarrow
   \text{uniform parent tightness};
   $$
4. Conversely, PS / PE parent escape necessarily forces:
   $$
   \mathfrak V_J\to\infty
   $$
   along the corresponding subsequence;
5. Upgrade the C3-O backward adjoint cutoff to a nonnegative partition of unity, establishing the exact:
   $$
   (a;k;p,q)
   $$
   spacetime-tube parent ledger;
6. For the band-passed Leray source:
   $$
   \mathcal T_k
   =
   \Delta_k\mathbb P\nabla\cdot
   $$
   prove the pressure-compatible commutator estimate and spatial pseudolocality;
7. Establish:
   $$
   \boxed{
   \text{tube contribution}
   =
   \text{tube-local source}
   +
   \text{commutator/leakage tax}.
   }
   $$

Thus, this paper pushes the:

$$
\boxed{
\text{frequency parent ledger}
}
$$

to the:

$$
\boxed{
\text{spacetime soft-tube parent ledger}
}
$$

for the first time.

---

# 1. Setting

Consider the three-dimensional incompressible Navier--Stokes equations:

$$
\partial_tu
-
\nu\Delta u
+
\mathbb P\nabla\cdot(u\otimes u)
=
0,
$$

$$
\nabla\cdot u=0,
$$

which are smooth on:

$$
0\le t<T_\ast.
$$

This paper adopts the compact pre-singular smooth/decay assumptions of RFP-03, so that Littlewood--Paley series, Bochner integrals, dyadic parent sums, and dual pairings can be interchanged term by term.

---

# 2. RFP-03 PF-A Edge Input

Fix the threshold:

$$
M>0.
$$

For a PF-A edge:

$$
d_J>0,
$$

let:

$$
s_J=\tau_J(M),
\qquad
t_J=\tau_{J+1}(M).
$$

RFP-03 defines the nonlinear tail increment:

$$
W_J
=
U_{J+1}(t_J)
-
\mathsf H_{t_J-s_J}
U_{J+1}(s_J),
$$

and:

$$
R_J
=
\|W_J\|_{X_{J+1}}
\ge
d_J.
$$

Write:

$$
W_J=(w_k)_{k>J+1},
$$

$$
b_k=\|w_k\|_3.
$$

Then:

$$
R_J^2
=
\sum_{k>J+1}b_k^2.
$$

---

# 3. RFP-03 Dual Witness

RFP-03 constructs:

$$
\Phi_J
=
(\phi_k)_{k>J+1}
\in
X_{J+1}^*,
$$

such that:

$$
\|\Phi_J\|_{X_{J+1}^*}=1,
$$

and:

$$
\boxed{
\langle W_J,\Phi_J\rangle=R_J.
}
$$

Moreover:

$$
\|\phi_k\|_{3/2}
=
\frac{b_k}{R_J}.
$$

This identity is the linear entry point for all spatial refinements in this paper.

---

# 4. Exact Parent Ledger Input

Let:

$$
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot.
$$

For a dyadic parent pair:

$$
(p,q),
$$

let:

$$
F_{p,q}
=
u_p\otimes u_q.
$$

The exact parent ledger of RFP-03 can be written as:

$$
\boxed{
\Lambda^{(J)}_{k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_kF_{p,q}(r),
\varphi_{J,k}(r)
\right\rangle dr,
}
$$

where:

$$
\boxed{
\varphi_{J,k}(r)
=
e^{\nu(t_J-r)\Delta}\phi_k.
}
$$

Since the heat semigroup is self-adjoint,

this is equivalent to the original definition in RFP-03 which left the heat semigroup on the source side.

---

# 5. Backward Dual Contraction

For:

$$
s_J\le r\le t_J,
$$

we have:

$$
\boxed{
\|\varphi_{J,k}(r)\|_{3/2}
\le
\|\phi_k\|_{3/2}
=
\frac{b_k}{R_J}.
}
$$

Therefore, backward heat propagation does not increase the dual norm.

---

# 6. Parent-Gap Escape Input

RFP-03 defines:

$$
g(k;p,q)
=
\max\{p,q\}-k.
$$

and proved the existence of a fixed:

$$
C_1<\infty
$$

depending only on the LP cutoff, such that when:

$$
g(k;p,q)>C_1
$$

and:

$$
\mathcal T_k(u_p\otimes u_q)\neq0
$$

there must be:

$$
\boxed{
|p-q|\le C_1.
}
$$

Therefore, far parent-gap contributions can only proceed via near-resonant high--high downshifts.

---

# 7. Positive Parent-Tail Ratio

Let:

$$
P_J
=
\sum_{k,p,q}
[\Lambda^{(J)}_{k;p,q}]_+.
$$

For:

$$
L>C_1,
$$

define:

$$
P_J^{down}(L)
=
\sum_{g(k;p,q)>L}
[\Lambda^{(J)}_{k;p,q}]_+.
$$

Then:

$$
\boxed{
1-C_J^{par}(L)
=
\frac{P_J^{down}(L)}{P_J}.
}
$$

RFP-03 only proved:

$$
C_J^{par}(L)\to1
$$

for each fixed $J$.

This paper seeks a uniform-in-$J$ estimate.

---

# 8. Interval Dyadic Dissipation Ledger

For each parent shell:

$$
p\ge-1,
$$

define:

$$
\boxed{
D_{p,J}
=
\int_{s_J}^{t_J}
2^{2p}
\|u_p(r)\|_2^2\,dr.
}
$$

and let:

$$
\boxed{
D_J
=
\sum_{p\ge-1}D_{p,J}.
}
$$

By the standard energy inequality and LP equivalence:

$$
D_J
$$

is finite on any single smooth interval.

If the full solution energy inequality is used,

we also have:

$$
D_J
\le
C\nu^{-1}\|u_0\|_2^2.
$$

But what this paper truly needs is the scale-normalized ratio formed by it and:

$$
R_J,
\quad
2^J
$$

---

# 9. Output-Depth First Moment

Define:

$$
\boxed{
\mathfrak O_J
=
\frac1{R_J}
\sum_{k>J+1}
2^{k-J}b_k.
}
$$

The smooth finite-window hypotheses guarantee that this quantity is finite.

$\mathfrak O_J$ measures the weighted depth of the nonlinear tail increment:

$$
W_J
$$

relative to the base first-passage scale:

$$
J
$$

towards deeper output shells.

---

# 10. Scale-Normalized Dissipation/Debt Ratio

Define:

$$
\boxed{
\mathfrak E_J
=
\frac{
2^J D_J
}{
R_J
}.
}
$$

This quantity compares the interval viscous activity with the actual nonlinear increment debt:

$$
R_J
$$

---

# 11. Viscous Downshift Budget

Define:

$$
\boxed{
\mathfrak V_J
=
\mathfrak E_J\mathfrak O_J.
}
$$

Equivalently:

$$
\boxed{
\mathfrak V_J
=
\frac{
D_J
}{
R_J^2
}
\sum_{k>J+1}
2^k b_k.
}
$$

This quantity will become the first quantitative obstruction variable for parent escape.

---

# 12. Scaling Audit

Consider the dyadic Navier--Stokes scaling:

$$
u^{(m)}(x,t)
=
2^m
u(2^mx,2^{2m}t).
$$

Then:

$$
J\mapsto J+m,
\qquad
k\mapsto k+m.
$$

Because $L^3$ is critical:

$$
b_k
$$

and:

$$
R_J
$$

maintain their numerical scales.

On the other hand:

$$
D_J
\mapsto
2^{-m}D_J.
$$

Therefore:

$$
2^JD_J
$$

is scale invariant.

Also:

$$
2^{k-J}
$$

is invariant.

Thus:

$$
\boxed{
\mathfrak E_J,
\quad
\mathfrak O_J,
\quad
\mathfrak V_J
}
$$

are all dyadic scale-invariant diagnostics.

---

# 13. Band-Passed Source Estimate

Standard Bernstein and smooth Fourier multiplier estimates give:

$$
\boxed{
\|
\mathcal T_kF
\|_3
\le
C2^{2k}
\|F\|_{3/2}.
}
$$

The reasons are:

- $\nabla\cdot$ provides a factor of $2^k$;
- output frequency localization causes:
  $$
  L^{3/2}\to L^3
  $$
  providing another factor of $2^k$.

Therefore, for the parent tensor:

$$
F_{p,q}=u_p\otimes u_q,
$$

we have:

$$
\boxed{
\|
\mathcal T_k(u_p\otimes u_q)
\|_3
\le
C2^{2k}
\|u_p\|_3
\|u_q\|_3.
}
$$

---

# 14. Bernstein Parent Estimate

For the dyadic shell:

$$
p,
$$

we have:

$$
\boxed{
\|u_p\|_3
\le
C2^{p/2}
\|u_p\|_2.
}
$$

So:

$$
\|u_p\|_3\|u_q\|_3
\le
C2^{(p+q)/2}
\|u_p\|_2
\|u_q\|_2.
$$

---

# 15. Dissipation Insertion

For:

$$
[s_J,t_J],
$$

Cauchy--Schwarz gives:

$$
\begin{aligned}
\int_{s_J}^{t_J}
\|u_p\|_2\|u_q\|_2\,dr
&=
2^{-p-q}
\int_{s_J}^{t_J}
(2^p\|u_p\|_2)
(2^q\|u_q\|_2)\,dr
\\
&\le
2^{-p-q}
D_{p,J}^{1/2}
D_{q,J}^{1/2}.
\end{aligned}
$$

Therefore:

$$
\boxed{
\int_{s_J}^{t_J}
\|u_p\|_3\|u_q\|_3\,dr
\le
C
2^{-(p+q)/2}
D_{p,J}^{1/2}
D_{q,J}^{1/2}.
}
$$

---

# 16. Single Triad Downshift Estimate

From the dual contraction:

$$
\|\varphi_{J,k}(r)\|_{3/2}
\le
\frac{b_k}{R_J},
$$

so:

$$
\begin{aligned}
|\Lambda^{(J)}_{k;p,q}|
&\le
C
\frac{b_k}{R_J}
2^{2k}
\int_{s_J}^{t_J}
\|u_p\|_3\|u_q\|_3\,dr
\\
&\le
C
\frac{b_k}{R_J}
2^{2k-(p+q)/2}
D_{p,J}^{1/2}D_{q,J}^{1/2}.
\end{aligned}
$$

---

# 17. C4.1 — Resonant Downshift Tail Estimate

## Theorem 17.1

There exists a constant:

$$
C<\infty
$$

depending only on the LP partition, such that for all:

$$
L>C_1,
$$

we have:

$$
\boxed{
P_J^{down}(L)
\le
C
2^{-L}
D_J
\sum_{k>J+1}
2^k\frac{b_k}{R_J}.
}
$$

### Proof

On the support of:

$$
g(k;p,q)>L
$$

the RFP-03 Resonant Downshift Lemma gives:

$$
|p-q|\le C_1.
$$

and:

$$
\max\{p,q\}>k+L.
$$

So:

$$
\frac{p+q}{2}
\ge
k+L-C
$$

for a fixed cutoff-dependent constant.

Therefore:

$$
2^{2k-(p+q)/2}
\le
C2^{k-L}.
$$

Thus, fixing the output shell:

$$
k,
$$

we have:

$$
\sum_{g>L}
|\Lambda^{(J)}_{k;p,q}|
\le
C
\frac{b_k}{R_J}
2^{k-L}
\sum_{|p-q|\le C_1}
D_{p,J}^{1/2}D_{q,J}^{1/2}.
$$

The finite-shift Cauchy estimate gives:

$$
\sum_{|p-q|\le C_1}
D_{p,J}^{1/2}D_{q,J}^{1/2}
\le
CD_J.
$$

Summing over $k$ again:

$$
P_J^{down}(L)
\le
\sum_{g>L}|\Lambda|
\le
C2^{-L}
D_J
\sum_{k>J+1}
2^k\frac{b_k}{R_J}.
$$

$\square$

---

# 18. C4.2 — Quantitative Uniform Parent-Tightness Bound

## Theorem 18.1

For all:

$$
L>C_1,
$$

we have:

$$
\boxed{
1-C_J^{par}(L)
\le
C2^{-L}\mathfrak V_J.
}
$$

### Proof

From:

$$
P_J\ge R_J,
$$

we obtain:

$$
\frac{P_J^{down}(L)}{P_J}
\le
\frac{P_J^{down}(L)}{R_J}.
$$

Plugging into Theorem 17.1:

$$
\frac{P_J^{down}(L)}{R_J}
\le
C2^{-L}
\frac{D_J}{R_J^2}
\sum_{k>J+1}2^kb_k
=
C2^{-L}\mathfrak V_J.
$$

$\square$

---

# 19. The First Uniform Parent Tightness Criterion

## Corollary 19.1

If along some PF-A edge family:

$$
\boxed{
\sup_J\mathfrak V_J
\le
K<\infty,
}
$$

then:

$$
\boxed{
\sup_J
\left(
1-C_J^{par}(L)
\right)
\le
CK2^{-L}.
}
$$

Therefore, the parent-gap ledger is uniformly tight.

In particular:

$$
\boxed{
\sup_J\mathfrak V_J<\infty
\Longrightarrow
PT
}
$$

is no longer just a subsequential classification,

but possesses a quantitative exponential tail.

---

# 20. Parent Escape Must Pay Budget Divergence

## Corollary 20.1

If the classified subsequence of RFP-03 falls into:

$$
PS
$$

or:

$$
PE,
$$

then along this subsequence:

$$
\boxed{
\mathfrak V_J\to\infty.
}
$$

### Proof

If there exists a bounded subsubsequence:

$$
\mathfrak V_J\le K,
$$

Theorem 18.1 gives a uniform bound for all $L$:

$$
1-C_J^{par}(L)
\le
CK2^{-L}.
$$

Taking the subsequential limit first,

and then letting:

$$
L\to\infty,
$$

we obtain:

$$
\alpha_{par}=1,
$$

which contradicts:

$$
PS
\quad\text{or}\quad
PE
$$

$\square$

---

# 21. The Dual Debt of Parent Escape

Since:

$$
\mathfrak V_J
=
\mathfrak E_J\mathfrak O_J,
$$

if:

$$
PS
$$

or:

$$
PE
$$

persists,

there must be:

$$
\boxed{
\mathfrak E_J\to\infty
\quad\vee\quad
\mathfrak O_J\to\infty
}
$$

at least along a further subsequence.

That is:

$$
\boxed{
\text{parent-gap escape}
\Longrightarrow
\text{dissipation/debt escape}
\vee
\text{output-depth escape}.
}
$$

This compresses a frequency-geometry escape further into two scale-invariant budget escapes.

---

# 22. Output-Depth Probability

Define:

$$
\boxed{
\pi_{J,k}
=
\frac{b_k^2}{R_J^2},
\qquad
k>J+1.
}
$$

Then:

$$
\sum_{k>J+1}\pi_{J,k}=1.
$$

Define the cumulative output-depth mass:

$$
\boxed{
C_J^{out}(L)
=
\sum_{J+1<k\le J+L}
\pi_{J,k}.
}
$$

---

# 23. C4.3 — Output-Depth Tail Bound

## Theorem 23.1

For:

$$
L\ge2,
$$

we have:

$$
\boxed{
1-C_J^{out}(L)
\le
2^{-2L}
\mathfrak O_J^2
}
$$

up to a harmless index-shift constant.

### Proof

For:

$$
k>J+L,
$$

we have:

$$
b_k
\le
2^{-L}
2^{k-J}b_k.
$$

So:

$$
\begin{aligned}
\left(
\sum_{k>J+L}b_k^2
\right)^{1/2}
&\le
\sum_{k>J+L}b_k
\\
&\le
2^{-L}
\sum_{k>J+L}
2^{k-J}b_k
\\
&\le
2^{-L}
R_J\mathfrak O_J.
\end{aligned}
$$

Squaring and dividing by:

$$
R_J^2
$$

yields the result. $\square$

---

# 24. Output Escape Must Also Pay $\mathfrak O_J$

If:

$$
\sup_J\mathfrak O_J<\infty,
$$

then the output-depth distribution is uniformly tight.

Therefore, any complete output-depth escape must force:

$$
\boxed{
\mathfrak O_J\to\infty.
}
$$

This explains why:

$$
\mathfrak O_J
$$

naturally appears in the parent tightness criterion.

---

# 25. From Frequency to Spacetime: Do Not Hard-Cut the Primal Equation First

If we directly set:

$$
v=\chi u,
$$

the localized field is generally no longer divergence-free,

and the equation will generate:

- cutoff forcing;
- diffusion commutators;
- advection boundary terms;
- pressure terms;
- divergence correction.

The 2026 quantitative forced N--S localization work once again shows:

$$
\boxed{
\text{localization is not a free operation}.
}
$$

Therefore, this paper adopts a different order:

$$
\boxed{
\text{first localize the dual certificate},
}
$$

instead of first claiming to obtain a new homogeneous local N--S equation.

---

# 26. Terminal Partition of Unity

Fix:

$$
A\ge1.
$$

Let the base core length be:

$$
\boxed{
\ell_J
=
A2^{-J}.
}
$$

Take a terminal smooth partition:

$$
\left\{
\chi^1_{J,a}
\right\}_{a\in\mathbb Z^3}
$$

such that:

$$
0\le
\chi^1_{J,a}
\le1,
$$

$$
\boxed{
\sum_a
\chi^1_{J,a}(x)
=
1,
}
$$

and each terminal cell is localized at diameter:

$$
O(\ell_J),
$$

satisfying:

$$
\|\nabla\chi^1_{J,a}\|_\infty
\le
CA^{-1}2^J.
$$

---

# 27. Backward Adjoint Partition

For each:

$$
a,
$$

let:

$$
\chi_{J,a}(t,x)
$$

solve:

$$
\boxed{
\partial_t\chi_{J,a}
+
u\cdot\nabla\chi_{J,a}
+
\nu\Delta\chi_{J,a}
=
0,
}
$$

for:

$$
s_J<t<t_J,
$$

and:

$$
\chi_{J,a}(t_J,x)
=
\chi^1_{J,a}(x).
$$

This is exactly the adjoint ancestry cutoff of C3-O.

---

# 28. C4.4 — Adjoint Partition Preservation

## Theorem 28.1

For all:

$$
s_J\le t\le t_J,
$$

we have:

$$
\boxed{
0\le\chi_{J,a}(t,x)\le1,
}
$$

and:

$$
\boxed{
\sum_a\chi_{J,a}(t,x)=1.
}
$$

### Proof

Nonnegativity and the upper bound follow from the parabolic maximum principle.

Let:

$$
\Xi_J
=
\sum_a\chi_{J,a}.
$$

The linear equation gives:

$$
\partial_t\Xi_J
+
u\cdot\nabla\Xi_J
+
\nu\Delta\Xi_J
=
0.
$$

terminal condition:

$$
\Xi_J(t_J)=1.
$$

The constant function $1$ is also a solution to the same equation.

By uniqueness:

$$
\Xi_J\equiv1.
$$

$\square$

---

# 29. Soft Ancestry Tube

Each:

$$
\chi_{J,a}
$$

defines a:

$$
\boxed{
\textbf{soft adjoint spacetime tube}.
}
$$

It:

- follows drift backward;
- diffuses backward;
- generally has tails at earlier times;
- does not maintain compact support.

Therefore, this paper does not use the semantics of:

$$
\text{hard material tube}
$$

---

# 30. Adjoint Gradient Distortion

Let:

$$
\boxed{
\mathfrak D_J^{adj}
=
\exp
\left(
\int_{s_J}^{t_J}
\|\nabla u(r)\|_\infty\,dr
\right).
}
$$

This quantity is finite on smooth pre-singular intervals.

The standard gradient maximum estimate gives:

$$
\boxed{
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}2^J
\mathfrak D_J^{adj}.
}
$$

Therefore, when a terminal wavelength-sized cell is pushed backward to an earlier time,

its boundary steepness may pay a:

$$
\mathfrak D_J^{adj}
$$

distortion debt.

---

# 31. Exact Spacetime-Tube Parent Ledger

Define:

$$
\boxed{
\Lambda^{tube,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_kF_{p,q}(r),
\chi_{J,a}(r)
\varphi_{J,k}(r)
\right\rangle dr.
}
$$

This ledger simultaneously preserves:

$$
\boxed{
a,
\quad
k,
\quad
p,
\quad
q.
}
$$

where:

- $a$: soft spacetime tube;
- $k$: output shell;
- $(p,q)$: ordered dyadic parents.

---

# 32. C4.5 — Exact Tube Refinement Identity

## Theorem 32.1

For all:

$$
k,p,q,
$$

we have:

$$
\boxed{
\sum_a
\Lambda^{tube,(J)}_{a;k;p,q}
=
\Lambda^{(J)}_{k;p,q}.
}
$$

Therefore:

$$
\boxed{
\sum_{a,k,p,q}
\Lambda^{tube,(J)}_{a;k;p,q}
=
R_J.
}
$$

### Proof

From Theorem 28.1:

$$
\sum_a\chi_{J,a}(r,x)=1.
$$

Substituting into the pairing and using absolute convergence:

$$
\begin{aligned}
\sum_a
\Lambda^{tube}_{a;k;p,q}
&=
-
\int
\left\langle
\mathcal T_kF_{p,q},
\left(
\sum_a\chi_{J,a}
\right)
\varphi_{J,k}
\right\rangle dr
\\
&=
-
\int
\left\langle
\mathcal T_kF_{p,q},
\varphi_{J,k}
\right\rangle dr
\\
&=
\Lambda_{k;p,q}.
\end{aligned}
$$

Then sum over:

$$
k,p,q
$$

$\square$

---

# 33. No Localization Forcing in This Step

Theorem 32.1 merely partitions the:

$$
\text{dual test certificate}
$$

It does not claim that:

$$
\chi_{J,a}u
$$

satisfies the homogeneous N--S.

Therefore, currently:

$$
\boxed{
\text{no primal localization forcing has been hidden}.
}
$$

This is an important proof-order choice of this paper.

---

# 34. Tube Positive / Negative Ledger

Define:

$$
P_J^{tube}
=
\sum_{a,k,p,q}
[\Lambda^{tube,(J)}_{a;k;p,q}]_+,
$$

$$
N_J^{tube}
=
\sum_{a,k,p,q}
[\Lambda^{tube,(J)}_{a;k;p,q}]_-.
$$

Then:

$$
\boxed{
P_J^{tube}
-
N_J^{tube}
=
R_J.
}
$$

Let:

$$
\boxed{
\zeta_J^{tube}
=
\frac{N_J^{tube}}{P_J^{tube}}.
}
$$

We have:

$$
0\le\zeta_J^{tube}<1.
$$

---

# 35. C4.6 — Tube Witness / Multiplicity Dichotomy

## Theorem 35.1

Fix:

$$
0<\theta<1.
$$

Each PF-A edge satisfies one of the following:

### TW — Strong spacetime parent witness

There exists:

$$
(a;k;p,q)
$$

such that:

$$
\boxed{
[\Lambda^{tube,(J)}_{a;k;p,q}]_+
\ge
\theta R_J.
}
$$

### TM — Spacetime-parent multiplicity debt

If there is no such witness,

then the positive tube ledger contains at least:

$$
\boxed{
\left\lceil
\frac{
1
}{
\theta
\left(
1-\zeta_J^{tube}
\right)
}
\right\rceil
}
$$

nonzero:

$$
(a;k;p,q)
$$

entries.

### Proof

Same as the RFP-03 Parent Witness / Multiplicity theorem,

only upgrading the parent-output index:

$$
(k;p,q)
$$

to:

$$
(a;k;p,q).
$$

$\square$

---

# 36. Interpretation

Now:

$$
\text{no strong spacetime witness}
$$

is no longer just unresolved.

It must pay a:

$$
\boxed{
\text{spatial-parent multiplicity debt}.
}
$$

Therefore, physical dispersion itself begins to become a quantifiable escape mechanism.

---

# 37. Why Can't $\mathbb P$ Be Treated as a Local Operator Alone?

The Leray projector:

$$
\mathbb P
$$

is a nonlocal order-zero Fourier multiplier.

The raw pressure is also determined by:

$$
-\Delta p
=
\partial_i\partial_j
(u_i u_j)
$$

So:

$$
\boxed{
[\chi,\mathbb P]
}
$$

cannot be unconditionally regarded as a small local error.

The canonical pressure-compatible operator in this paper is not:

$$
\mathbb P
$$

alone,

but:

$$
\boxed{
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot.
}
$$

The output band-pass restores strong kernel localization.

---

# 38. Band-Passed Leray Kernel

The Fourier symbol of $\mathcal T_k$ is:

$$
m_k(\xi)
=
\varphi(2^{-k}\xi)
\mathbb P(\xi)
(i\xi)\cdot.
$$

Because:

$$
\varphi
$$

is smooth and compactly supported away from:

$$
\xi=0,
$$

the scaled symbol is smooth.

Thus:

$$
\mathcal T_k
$$

has the Schwartz kernel:

$$
\boxed{
K_k(x)
=
2^{4k}K(2^kx),
}
$$

where:

$$
K
$$

is a Schwartz tensor kernel.

---

# 39. C4.7 — Pressure-Compatible Pseudolocality

## Theorem 39.1

For any:

$$
N>0,
$$

there exists:

$$
C_N<\infty
$$

such that:

$$
\boxed{
\left\|
\mathbf 1_{\{|x|\ge R2^{-k}\}}
K_k
\right\|_{L^{3/2}}
\le
C_N
2^{2k}
(1+R)^{-N}.
}
$$

Therefore, if sets:

$$
E,
\quad
F
$$

satisfy:

$$
\operatorname{dist}(E,F)
\ge
R2^{-k},
$$

then:

$$
\boxed{
\|
\mathbf 1_E
\mathcal T_k
(\mathbf 1_F G)
\|_3
\le
C_N
2^{2k}
(1+R)^{-N}
\|G\|_{3/2}.
}
$$

### Proof

From:

$$
K_k(x)=2^{4k}K(2^kx)
$$

and Schwartz decay,

changing variables:

$$
y=2^kx
$$

yields the kernel-tail bound.

Then using Young's inequality:

$$
L^{3/2}*L^{3/2}
\to
L^3.
$$

$\square$

---

# 40. Pressure Nonlocality Has Not Disappeared

Theorem 39.1 does not say that:

$$
p
$$

is local.

It says:

$$
\boxed{
\text{after exact output band-pass, the full Leray nonlinear source is pseudolocal at wavelength }2^{-k}.
}
$$

The raw pressure remains nonlocal.

However, after:

$$
\Delta_k
\mathbb P\nabla\cdot
$$

retains the pressure and incompressibility cancellation,

its annular kernel rapidly decays.

---

# 41. Raw Pressure Near/Far Split

For any smooth spatial cutoff:

$$
\eta
$$

define the pair pressure:

$$
p_{p,q}
=
R_iR_j
\left(
u_{p,i}u_{q,j}
\right).
$$

Split:

$$
p_{p,q}
=
p_{p,q}^{near}
+
p_{p,q}^{far},
$$

where:

$$
p_{p,q}^{near}
=
R_iR_j
\left(
\eta
u_{p,i}u_{q,j}
\right),
$$

$$
p_{p,q}^{far}
=
R_iR_j
\left(
(1-\eta)
u_{p,i}u_{q,j}
\right).
$$

In the interior region where:

$$
\eta\equiv1
$$

we have:

$$
\boxed{
\Delta p_{p,q}^{far}=0.
}
$$

That is, the far pressure is harmonic in the core.

---

# 42. The Role of Local Pressure Expansion

The raw local pressure decomposition needs to preserve:

- Calderón--Zygmund near part;
- far-field harmonic / renormalized contribution;
- additive time-dependent pressure gauge.

Therefore:

$$
\boxed{
\text{pressure near/far split}
}
$$

and:

$$
\boxed{
\text{band-passed Leray pseudolocality}
}
$$

are complementary descriptions.

The parent ledger in this paper prioritizes the latter because it is directly compatible with the exact frequency provenance:

$$
(k;p,q)
$$

---

# 43. Combined Commutator

For a Lipschitz cutoff:

$$
\chi,
$$

there is an exact identity:

$$
\boxed{
\chi\mathcal T_kF
=
\mathcal T_k(\chi F)
+
[\chi,\mathcal T_k]F.
}
$$

Here:

$$
[\chi,\mathcal T_k]
=
\chi\mathcal T_k
-
\mathcal T_k\chi.
$$

---

# 44. C4.8 — Band-Passed Leray Commutator Estimate

## Theorem 44.1

For:

$$
F\in L^{3/2},
$$

we have:

$$
\boxed{
\|
[\chi,\mathcal T_k]F
\|_3
\le
C
2^k
\|\nabla\chi\|_\infty
\|F\|_{3/2}.
}
$$

### Proof

From the kernel representation:

$$
[\chi,\mathcal T_k]F(x)
=
\int
K_k(x-y)
\left(
\chi(x)-\chi(y)
\right)
F(y)\,dy.
$$

Lipschitz bound:

$$
|\chi(x)-\chi(y)|
\le
\|\nabla\chi\|_\infty
|x-y|.
$$

And:

$$
\|
|x|K_k(x)
\|_{L^{3/2}}
\le
C2^k.
$$

Young's inequality gives the conclusion. $\square$

---

# 45. Relative Commutator Scale

The main operator estimate is:

$$
\|
\mathcal T_kF
\|_3
\lesssim
2^{2k}
\|F\|_{3/2},
$$

while the commutator is:

$$
\|
[\chi,\mathcal T_k]F
\|_3
\lesssim
2^k
\|\nabla\chi\|_\infty
\|F\|_{3/2}.
$$

So the relative tax is:

$$
\boxed{
2^{-k}
\|\nabla\chi\|_\infty.
}
$$

If the cutoff physical scale is:

$$
\ell,
$$

then:

$$
\|\nabla\chi\|_\infty
\sim
\ell^{-1}.
$$

Therefore, the tax is approximately:

$$
\boxed{
(2^k\ell)^{-1}.
}
$$

which is the inverse number of output wavelengths across the cutoff width.

---

# 46. Adjoint Tube Commutator Factor

For:

$$
\chi=\chi_{J,a}(r),
$$

from Section 30:

$$
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}2^J
\mathfrak D_J^{adj}.
$$

Therefore:

$$
\boxed{
2^{-k}
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}
2^{J-k}
\mathfrak D_J^{adj}.
}
$$

Since the ledger outputs satisfy:

$$
k>J+1,
$$

we obtain:

$$
\boxed{
2^{-k}
\|\nabla\chi_{J,a}(r)\|_\infty
\le
CA^{-1}
\mathfrak D_J^{adj}.
}
$$

So as long as:

$$
A
$$

is sufficiently large relative to the adjoint distortion,

the commutator can serve as a scale-compatible small tax.

---

# 47. Tube-Local Source Ledger

Define:

$$
\boxed{
\Lambda^{loc,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
\mathcal T_k
\left(
\chi_{J,a}
F_{p,q}
\right),
\varphi_{J,k}
\right\rangle dr.
}
$$

This quantity explicitly requires the parent tensor source to be weighted by the soft tube:

$$
\chi_{J,a}
$$

---

# 48. Commutator Ledger

Define:

$$
\boxed{
\Lambda^{com,(J)}_{a;k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
[\chi_{J,a},\mathcal T_k]
F_{p,q},
\varphi_{J,k}
\right\rangle dr.
}
$$

---

# 49. C4.9 — Exact Local-Source / Leakage Split

## Theorem 49.1

For each:

$$
(a;k;p,q),
$$

there is an exact identity:

$$
\boxed{
\Lambda^{tube,(J)}_{a;k;p,q}
=
\Lambda^{loc,(J)}_{a;k;p,q}
+
\Lambda^{com,(J)}_{a;k;p,q}.
}
$$

### Proof

From:

$$
\langle
\mathcal T_kF,
\chi\varphi
\rangle
=
\langle
\chi\mathcal T_kF,
\varphi
\rangle
$$

and:

$$
\chi\mathcal T_kF
=
\mathcal T_k(\chi F)
+
[\chi,\mathcal T_k]F.
$$

Integrating yields the result. $\square$

---

# 50. Commutator Tax Estimate

From Theorem 44.1 and the dual contraction:

$$
\boxed{
\begin{aligned}
\left|
\Lambda^{com,(J)}_{a;k;p,q}
\right|
\le
C
\frac{b_k}{R_J}
\int_{s_J}^{t_J}
2^k
\|\nabla\chi_{J,a}(r)\|_\infty
\|u_p(r)\|_3
\|u_q(r)\|_3
\,dr.
\end{aligned}
}
$$

This is a completely explicit localization leakage tax.

---

# 51. C4.10 — Spacetime Parent Attachment Certificate

## Theorem 51.1

If a tube-parent-output entry satisfies:

$$
\Lambda^{tube,(J)}_{a;k;p,q}
\ge
\theta R_J
$$

for:

$$
\theta>0,
$$

and its commutator tax satisfies:

$$
\left|
\Lambda^{com,(J)}_{a;k;p,q}
\right|
\le
\varepsilon R_J
$$

with:

$$
0\le\varepsilon<\theta,
$$

then:

$$
\boxed{
\Lambda^{loc,(J)}_{a;k;p,q}
\ge
(\theta-\varepsilon)R_J.
}
$$

### Proof

From the exact split:

$$
\Lambda^{loc}
=
\Lambda^{tube}
-
\Lambda^{com}.
$$

So:

$$
\Lambda^{loc}
\ge
\theta R_J
-
|\Lambda^{com}|
\ge
(\theta-\varepsilon)R_J.
$$

$\square$

---

# 52. To What Extent is This True Spatial Attachment?

Theorem 51.1 proves:

$$
\boxed{
\text{a definite portion of the exact parent contribution is generated by the parent tensor inside one soft adjoint tube}.
}
$$

It is stronger than:

$$
\text{global-frequency parent}
$$

But it has not yet been proven that:

$$
u_p
$$

and:

$$
u_q
$$

each possess a unique nested physical core.

Currently, the attached object is:

$$
\boxed{
\chi_{J,a}
(u_p\otimes u_q).
}
$$

So it is:

$$
\boxed{
\text{source-core attachment},
}
$$

not a complete:

$$
\boxed{
\text{individual-parent-core identity}.
}
$$

---

# 53. Parent Co-Location Debt

By Hölder's inequality:

$$
\|
\chi_{J,a}
u_p\otimes u_q
\|_{3/2}
\le
\|
\chi_{J,a}^{1/2}u_p
\|_3
\|
\chi_{J,a}^{1/2}u_q
\|_3.
$$

Therefore, if:

$$
\Lambda^{loc}_{a;k;p,q}
$$

has a nontrivial lower bound,

then the corresponding weighted parent product cannot be uniformly too small over the entire edge interval.

So we at least obtain:

$$
\boxed{
\text{source-core attachment}
\Longrightarrow
\text{parent co-location burden}.
}
$$

But this paper does not directly upgrade this to the unique ancestry cores of:

$$
\Omega_p,
\Omega_q
$$

---

# 54. Pressure-Compatible No-Go

If we first separate:

$$
\mathbb P
$$

and:

$$
\Delta_k
$$

and then separately claim that:

$$
[\chi,\mathbb P]
$$

and:

$$
[\chi,\Delta_k]
$$

are both small,

we might lose the annular cancellation.

This paper formally adopts:

$$
\boxed{
G_{\rm BP}:
\quad
\text{localize the combined band-passed Leray source }
\Delta_k\mathbb P\nabla\cdot
\text{ before declaring pressure leakage small}.
}
$$

This does not negate classical commutator theory.

It merely specifies the canonical operator unit for the NS-RFP ancestry.

---

# 55. Comparison: Raw Localization Truly Generates Forcing

If we directly set:

$$
v=\chi u,
$$

then formal calculation yields:

$$
\partial_tv
-
\nu\Delta v
+
\nabla\cdot(\chi u\otimes u)
+
\nabla(\chi p)
=
f_\chi,
$$

where:

$$
\boxed{
f_\chi
=
(\partial_t\chi)u
-
2\nu\nabla\chi\cdot\nabla u
-
\nu(\Delta\chi)u
+
(u\cdot\nabla\chi)u
+
p\nabla\chi.
}
$$

And:

$$
\nabla\cdot v
=
u\cdot\nabla\chi.
$$

So:

$$
\boxed{
\text{primal localization}
\neq
\text{homogeneous local Navier--Stokes}.
}
$$

This is exactly why this paper localizes the dual certificate first.

---

# 56. Adjoint Cancellation Only Applies to Specific Balance Layers

The adjoint cutoff of C3-O:

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0
$$

can exactly cancel the scalar:

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
$$

package in the localized strain-energy balance.

But this does not mean:

$$
f_\chi=0
$$

in the velocity localized equation.

Therefore:

$$
\boxed{
\text{adjoint balance cancellation}
\neq
\text{zero primal localization forcing}.
}
$$

---

# 57. Two Adjoints Must Not Be Conflated

This paper simultaneously has:

### Duhamel dual witness

$$
\varphi_{J,k}(r)
=
e^{\nu(t_J-r)\Delta}\phi_k.
$$

### Strain-balance / ancestry cutoff

$$
\partial_t\chi
+
u\cdot\nabla\chi
+
\nu\Delta\chi
=
0.
$$

The former is:

$$
\text{backward heat dual}.
$$

The latter is:

$$
\text{backward transport-diffusion adjoint}.
$$

Their roles are different.

This paper only uses the product:

$$
\chi_{J,a}\varphi_{J,k}
$$

as the source-time test.

Added guard:

$$
\boxed{
G_{\rm 2ADJ}:
\quad
\text{heat dual and transport-diffusion adjoint must not be identified}.
}
$$

---

# 58. Interfacing Pressure Near/Far with Tube Split

In a selected tube:

$$
a,
$$

one can take another smooth spatial cutoff:

$$
\eta_{J,a,R}
$$

which is:

$$
1,
$$

near the tube's effective core, and:

$$
0.
$$

outside a larger buffer.

The parent pressure is split into:

$$
p_{p,q}^{near,R}
+
p_{p,q}^{far,R}.
$$

The far part is harmonic in the inner core.

And the band-passed source:

$$
\mathcal T_k
$$

again has the rapid decay of Theorem 39.1 for sources outside the buffer.

So pressure escape must pay at least one of:

$$
\boxed{
\text{large far-source norm}
}
$$

or:

$$
\boxed{
\text{large tube distortion / commutator tax}.
}
$$

This paper does not claim that these two have been ruled out by a universal bound.

---

# 59. Certified Buffer Radius

If on a selected entry there is a gross source budget:

$$
\mathfrak S_{J,a;k,p,q}
$$

such that the far contribution is estimated as:

$$
C_N
R^{-N}
\mathfrak S_{J,a;k,p,q}R_J,
$$

then to certify that the far leakage does not exceed:

$$
\varepsilon R_J,
$$

a sufficient condition is:

$$
\boxed{
R
\ge
\left(
\frac{
C_N
\mathfrak S_{J,a;k,p,q}
}{
\varepsilon
}
\right)^{1/N}.
}
$$

Therefore:

$$
\boxed{
\text{large gross source budget}
\Longrightarrow
\text{larger certified spatial buffer}.
}
$$

This is the quantitative coupling between source cancellation and spatial localization.

---

# 60. Uniform Parent Tightness + Tube Witness

Currently, the branch closest to a complete spacetime ancestry is upgraded to:

$$
\boxed{
\mathrm{PF\mbox{-}A}
+
\sup_J\mathfrak V_J<\infty
+
TW
+
\text{small commutator tax}.
}
$$

where:

$$
\sup_J\mathfrak V_J<\infty
$$

gives uniform frequency-parent tightness,

and:

$$
TW
$$

plus a small commutator tax gives source-core attachment.

---

# 61. Remaining Escape Branches

If the cleanest branch above fails,

it must enter at least one of the following:

### E-V

$$
\boxed{
\mathfrak V_J\to\infty
}
$$

dissipation-output budget escape.

### E-TM

spacetime-parent multiplicity:

$$
\boxed{
\#\text{positive tube-parent witnesses}\to\infty
}
$$

or at least no uniform strong witness.

### E-COM

$$
\boxed{
\text{commutator/localization leakage is order-one}.
}
$$

### E-ADJ

$$
\boxed{
\mathfrak D_J^{adj}\to\infty
}
$$

leading to severe soft tube distortion.

### E-PRESS

far pressure / far source requires a growing buffer to certify.

### E-PERSIST

Even if every edge has a good tube witness,

they cannot be stitched into a consistent ancestry path across edges.

---

# 62. C4.11 — RFP-04 Proof-Space Enclosure

## Theorem 62.1

For any infinite PF-A first-passage edge sequence,

if:

1. $\mathfrak V_J$ is uniformly bounded;
2. There exist TW witnesses with uniform $\theta>0$;
3. The commutator taxes of selected witnesses are uniformly less than $\varepsilon R_J$, where $\varepsilon<\theta$;

then:

$$
\boxed{
\text{parent frequency gaps are uniformly tight}
}
$$

and for each selected edge there exists:

$$
\boxed{
\text{a positive tube-local parent source contribution}.
}
$$

If this set of conclusions cannot be maintained,

then at least one hypothesis fails,

i.e., it must enter:

$$
\boxed{
E\mbox{-}V
\vee
E\mbox{-}TM
\vee
E\mbox{-}COM
}
$$

or subsequent persistence / pressure / adjoint distortion escapes.

### Proof

Uniform parent tightness follows from Corollary 19.1.

The tube-local positive source follows from Theorem 51.1.

The rest is the exhaustive failure of the stated hypotheses. $\square$

---

# 63. This is Not Full Chain Necessity

Theorem 62.1 has not yet proved that:

$$
\boxed{
X_J
\to
X_{J+1}
}
$$

can be stitched across all $J$ into the same persistent ancestry.

Currently, each edge can select a different:

$$
a,
\quad
k,
\quad
p,
\quad
q.
$$

So the remaining core problem becomes:

$$
\boxed{
\textbf{Witness Persistence / Chain Stitching}.
}
$$

---

# 64. Why Does the Next Paper Become a Graph Compactness Problem?

RFP-02:

$$
\text{first-passage levels}.
$$

RFP-03:

$$
\text{exact parent-output edges}.
$$

RFP-04:

$$
\text{spacetime tube-parent edges}.
$$

So we now naturally obtain a layered directed graph:

$$
\boxed{
\mathcal G^{RFP}
=
(V,E),
}
$$

whose levels are ordered by:

$$
J
$$

Full Chain Necessity next requires:

> Upgrading from the existence of an admissible witness at each layer to the existence of an infinite ancestry path consistent across arbitrarily many layers.

This is not a single PDE estimate.

It is simultaneously:

$$
\boxed{
\text{PDE legality}
+
\text{graph compactness}
+
\text{persistence}.
}
$$

---

# 65. Next Paper

The official next paper is changed to:

$$
\boxed{
\textbf{NS-RFP 05 — Witness Persistence, Finite Branching, and Infinite Ancestry Path Extraction}.
}
$$

Core problems:

1. Define edge compatibility;
2. Stitch parent/output/tube witnesses into a layered ancestry graph;
3. Study whether bounded multiplicity gives finite branching;
4. Use compactness / Kőnig-type infinity principle to extract an infinite path;
5. Determine whether multiplicity blow-up becomes a new escape debt;
6. Incorporate first-passage time ordering and tube overlap into compatibility;
7. Explicitly separate:
   $$
   \text{a witness at every level}
   $$
   and:
   $$
   \text{one persistent witness chain}.
   $$

---

# 66. New Guards

Added:

### $G_{\rm VISC}$

Parent-gap escape must preserve:

$$
\mathfrak V_J
=
\mathfrak E_J\mathfrak O_J.
$$

PS / PE must not be treated as a cost-free frequency jump.

### $G_{\rm OUT}$

Output-depth distribution must preserve:

$$
\pi_{J,k}.
$$

### $G_{\rm TUBE}$

Spatial labels must come from an exact partition / localization certificate,

and ancestry must not be directly claimed by visual proximity.

### $G_{\rm BP}$

Pressure-compatible localization uses:

$$
\Delta_k\mathbb P\nabla\cdot
$$

as the canonical operator unit.

### $G_{\rm COM}$

Tube-local source claims must preserve the commutator ledger.

### $G_{\rm 2ADJ}$

The backward heat dual and transport-diffusion adjoint must not be conflated.

### $G_{\rm FORCE}$

The forcing generated by the primal cutoff equation must not be hidden.

---

# 67. Guard Library v3

Therefore:

$$
\boxed{
\mathcal G_{NS}^{(3)}
=
\mathcal G_{NS}^{(2)}
\cup
\{
G_{\rm VISC},
G_{\rm OUT},
G_{\rm TUBE},
G_{\rm BP},
G_{\rm COM},
G_{\rm 2ADJ},
G_{\rm FORCE}
\}.
}
$$

---

# 68. Standard-Literature Calibration

The framework of this paper interfaces with the following classical / recent facts:

1. Local pressure cannot be treated as a purely local algebraic function; the local pressure expansion itself requires a correct mild/distributional framework;
2. Localized smoothing and critical concentration results provide the standard PDE interface for the true singularity core on parabolic scales;
3. The 2026 forced N--S quantitative work once again explicitly shows that spatial localization introduces forcing, and this forcing requires independent control in quantitative Carleman estimates.

This paper only treats these as:

$$
\boxed{
\text{standard PDE compatibility checks}.
}
$$

The algebraic / harmonic-analysis core of Theorems 17.1--62.1 does not rely on any unverified 2026 global claims.

---

# 69. Formal Status Ledger

$$
\boxed{
\begin{aligned}
\text{scale-invariant }\mathfrak E_J,\mathfrak O_J,\mathfrak V_J
&:\ \mathrm{DEFINED/VERIFIED},\\
\text{resonant downshift tail estimate}
&:\ \mathrm{PROVED},\\
\text{quantitative parent-tightness bound}
&:\ \mathrm{PROVED},\\
\sup_J\mathfrak V_J<\infty
\Rightarrow
\text{uniform parent tightness}
&:\ \mathrm{PROVED},\\
PS/PE
\Rightarrow
\mathfrak V_J\to\infty
&:\ \mathrm{PROVED\ along\ classified\ subsequence},\\
\text{output-depth tail bound}
&:\ \mathrm{PROVED},\\
\text{adjoint partition preservation}
&:\ \mathrm{PROVED},\\
\text{exact spacetime-tube parent ledger}
&:\ \mathrm{PROVED},\\
\text{tube witness/multiplicity dichotomy}
&:\ \mathrm{PROVED},\\
\text{band-passed Leray pseudolocality}
&:\ \mathrm{PROVED},\\
\text{band-passed Leray commutator estimate}
&:\ \mathrm{PROVED},\\
\text{exact local-source/leakage split}
&:\ \mathrm{PROVED},\\
\text{spacetime parent attachment certificate}
&:\ \mathrm{PROVED\ conditionally\ on\ small\ commutator\ tax},\\
\text{universal bound on }\mathfrak V_J
&:\ \mathrm{OPEN},\\
\text{uniform adjoint distortion bound}
&:\ \mathrm{OPEN},\\
\text{uniform strong tube witness}
&:\ \mathrm{OPEN},\\
\text{individual parent-core identity}
&:\ \mathrm{OPEN},\\
\text{witness persistence across levels}
&:\ \mathrm{OPEN},\\
\text{full Chain Necessity}
&:\ \mathrm{OPEN},\\
\text{Finite Obstruction}
&:\ \mathrm{OPEN},\\
\text{Navier--Stokes regularity}
&:\ \mathrm{NOT\ PROVED}.
\end{aligned}
}
$$

---

# 70. Conclusion

The frontier of RFP-03 is:

$$
\boxed{
\text{can exact frequency provenance be made uniformly tight, persistent, and spatially attached?}
}
$$

RFP-04 makes substantial progress on the first and the third of these properties.

First:

$$
\boxed{
1-C_J^{par}(L)
\le
C2^{-L}
\mathfrak E_J\mathfrak O_J.
}
$$

So:

$$
\boxed{
\sup_J
\mathfrak E_J\mathfrak O_J
<
\infty
\Longrightarrow
\text{quantitative uniform parent tightness}.
}
$$

And any:

$$
PS
\quad\text{or}\quad
PE
$$

escape must force:

$$
\boxed{
\mathfrak E_J\mathfrak O_J
\to\infty.
}
$$

This converts the uniform-tightness quantifier gap into a scale-invariant budget obstruction.

Secondly, using the C3-O backward adjoint cutoff as a partition of unity:

$$
\boxed{
\Lambda_{k;p,q}
=
\sum_a
\Lambda^{tube}_{a;k;p,q},
}
$$

Therefore, the exact parent provenance is upgraded for the first time to:

$$
\boxed{
(a;k;p,q)
}
$$

spacetime soft-tube provenance.

Then, utilizing the canonical band-passed Leray operator:

$$
\mathcal T_k
=
\Delta_k\mathbb P\nabla\cdot,
$$

we obtain:

$$
\boxed{
\Lambda^{tube}
=
\Lambda^{loc}
+
\Lambda^{com}.
}
$$

So pressure/localization nonlocality is no longer hidden,

but concentrated into an explicit commutator / leakage tax.

If the tax of a strong tube witness is small,

then:

$$
\boxed{
\text{exact parent frequency witness}
\Longrightarrow
\text{positive tube-local parent source}.
}
$$

Therefore, the truly remaining core of Chain Necessity has now shifted from:

$$
\text{Where is the source?}
$$

to:

$$
\boxed{
\textbf{Can good witnesses at arbitrarily high levels be stitched into one persistent infinite ancestry path?}
}
$$

This is the next paper:

$$
\boxed{
\textbf{NS-RFP 05 — Witness Persistence, Finite Branching, and Infinite Ancestry Path Extraction}.
}
$$

---

# References

1. J.-M. Bony, *Calcul symbolique et propagation des singularités pour les équations aux dérivées partielles non linéaires*, Annales scientifiques de l'École Normale Supérieure 14 (1981), 209–246.
2. L. Escauriaza, G. Seregin, V. Sverak, *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58 (2003), 211–250.
3. A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy, *Energy conservation and Onsager's conjecture for the Euler equations*, Nonlinearity 21 (2008), 1233–1252; arXiv:0704.0759.
4. Z. Bradshaw, Z. Grujic, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
5. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115.
6. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, Journal of Mathematical Fluid Mechanics 24 (2022); arXiv:2001.11526.
7. T. Barker, H. Popkin, *Quantitative estimates for the forced Navier–Stokes equations and applications*, arXiv:2602.09951 (2026). Used as contemporary localization/forcing calibration; no global conclusion is imported into the present theorems.

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_RFP_03_DualWitness_ParentLedger_CarrierEscape_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 05 — Witness Persistence, Finite Branching, and Infinite Ancestry Path Extraction}
}
$$