---
title: "Navier–Stokes Reverse Formation Program 03: Dual-Witness Parent Ledger, Exact Triadic Provenance, and Carrier-Depth Escape"
short_title: "NS-RFP 03"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural advance / partial Exact Parent Resolution"
epistemic_status: "Constructs an exact signed dyadic parent-output ledger for every source-paid first-passage edge using a dual norming witness; proves parent cancellation and multiplicity debts, Fourier-support ancestry guards, and subsequential parent-gap/carrier-depth concentration-escape classifications. Does NOT prove uniform parent tightness, spatial-core ancestry, full Chain Necessity, Finite Obstruction, or Navier–Stokes regularity."
canonical_source: "UTF-8 Markdown"
---

# Navier–Stokes Reverse Formation Program 03

# Dual-Witness Parent Ledger, Exact Triadic Provenance, and Carrier-Depth Escape

## 0. Positioning of this Paper

NS-RFP 02 has elevated

$$
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{critical UV escape}
$$

to

$$
\boxed{
\operatorname{Blowup}(T_\ast)
\Longrightarrow
\text{canonical adjacent-scale first-passage skeleton}.
}
$$

For each fixed threshold

$$
M>0,
$$

there exists

$$
\tau_J(M)\uparrow T_\ast,
$$

and

$$
\tau_J(M)\le\tau_{J+1}(M).
$$

Each edge

$$
J\to J+1
$$

has a first-passage deficit

$$
d_J=M-\mathcal B_{J+1}(\tau_J)\ge0.
$$

RFP-02 obtained

$$
d_J>0
\Longrightarrow
\text{positive aggregate nonlinear Duhamel source debt}.
$$

However, two main gaps remain:

$$
\boxed{\textbf{PF-A: Exact Parent Resolution}}
$$

and

$$
\boxed{\textbf{PF-B: Synchronous / Deep-Tail Bypass}}.
$$

The core advances of this paper are:

1. Linearizing the aggregate source debt of PF-A into an exact signed dyadic parent-output ledger;
2. Proving the exact parent witness / parent multiplicity debt;
3. Proving that far upward generation is impossible in a single quadratic interaction;
4. Proving that a large parent-to-output downshift can only originate from near-resonant high--high parents;
5. Compressing the remaining gap of PF-A into parent-gap tightness vs. resonant downshift escape;
6. Compressing PF-B into a carrier-depth tight / split / escape profile.

This paper still does not constitute full Chain Necessity.

---

# 1. Setting

Consider

$$
\partial_tu-\nu\Delta u+\mathbb P\nabla\cdot(u\otimes u)=0,
$$

$$
\nabla\cdot u=0,
$$

smooth on

$$
0\le t<T_\ast.
$$

To allow term-by-term exchange of the dyadic sums in the parent ledger, this paper adopts a smooth rapid-decay hypothesis on compact pre-singular windows for the theorem-level parent decomposition. Equivalently, sufficiently high Sobolev regularity combined with spatial decay can be used to guarantee the absolute convergence of the following series and Bochner integrals.

---

# 2. Littlewood–Paley Convention

Take the standard inhomogeneous decomposition

$$
u=\sum_{j\ge-1}u_j,
$$

where

$$
u_j=\Delta_j u.
$$

The UV first-passage construction of RFP-02 only uses sufficiently large $J$, so the finite low-frequency convention does not alter

$$
\mathcal B_J(t)
=
\left(
\sum_{j>J}\|u_j(t)\|_3^2
\right)^{1/2}.
$$

---

# 3. RFP-02 Input

Fix

$$
M>0.
$$

Let

$$
s_J=\tau_J(M),
\qquad
t_J=\tau_{J+1}(M).
$$

And let

$$
\eta_J
=
\frac{\mathcal B_{J+1}(s_J)}{M},
$$

$$
d_J=M(1-\eta_J).
$$

RFP-02 has proven: if

$$
d_J>0,
$$

then

$$
s_J<t_J,
$$

and the increase of the deeper-tail burden from $\mathcal B_{J+1}(s_J)$ to

$$
\mathcal B_{J+1}(t_J)=M
$$

must pay a positive nonlinear Duhamel source debt.

---

# 4. Tail Banach Space

Define

$$
\boxed{
X_J
=
\ell^2_{k>J}
\left(L^3(\mathbb R^3;\mathbb R^3)\right).
}
$$

with norm

$$
\|(f_k)_{k>J}\|_{X_J}
=
\left(
\sum_{k>J}\|f_k\|_3^2
\right)^{1/2}.
$$

Therefore,

$$
\mathcal B_J(t)=\|U_J(t)\|_{X_J},
$$

where

$$
U_J(t)=(u_k(t))_{k>J}.
$$

Its dual is

$$
\boxed{
X_J^*
=
\ell^2_{k>J}
\left(L^{3/2}(\mathbb R^3;\mathbb R^3)\right).
}
$$

using the pairing

$$
\langle F,\Phi\rangle
=
\sum_{k>J}\int_{\mathbb R^3}f_k(x)\cdot\phi_k(x)\,dx.
$$

---

# 5. Tail Heat Operator

Define the diagonal heat operator

$$
\mathsf H_\sigma(f_k)_{k>J}
=
\left(e^{\nu\sigma\Delta}f_k\right)_{k>J}.
$$

Since the heat semigroup is contractive in $L^3$,

$$
\boxed{
\|\mathsf H_\sigma F\|_{X_J}
\le
\|F\|_{X_J}.
}
$$

---

# 6. Nonlinear Tail Increment

For a PF-A edge $d_J>0$, use the tail space $X_{J+1}$.

Define

$$
\boxed{
W_J
=
U_{J+1}(t_J)
-
\mathsf H_{t_J-s_J}U_{J+1}(s_J).
}
$$

By the Duhamel formula,

$$
W_J
=
-
\int_{s_J}^{t_J}
\mathsf H_{t_J-r}F_J^{tail}(r)\,dr,
$$

where

$$
F_J^{tail}(r)
=
\left(
\Delta_k\mathbb P\nabla\cdot(u\otimes u)(r)
\right)_{k>J+1}.
$$

---

# 7. C3.1 — Tail Increment Debt

## Theorem 7.1

For each PF-A edge, let

$$
R_J:=\|W_J\|_{X_{J+1}}.
$$

Then

$$
\boxed{R_J\ge d_J>0.}
$$

### Proof

By the reverse triangle inequality and heat contraction,

$$
\begin{aligned}
R_J
&\ge
\|U_{J+1}(t_J)\|_{X_{J+1}}
-
\|\mathsf H_{t_J-s_J}U_{J+1}(s_J)\|_{X_{J+1}}
\\
&\ge
M-\mathcal B_{J+1}(s_J)
\\
&=d_J.
\end{aligned}
$$

$\square$

---

# 8. Why Track $W_J$ Instead?

RFP-02 used the positive quantity

$$
\int\mathcal N_{J+1}
$$

which is sufficient to prove that a nonlinear source must exist, but it takes the magnitude first, thus failing to preserve sign, cancellation, and exact parent contribution.

This paper instead tracks

$$
\boxed{W_J}
$$

itself, because $W_J$ is linear with respect to the Duhamel source.

---

# 9. Constructive Norming Witness

Write

$$
W_J=(w_k)_{k>J+1},
$$

$$
b_k=\|w_k\|_3,
\qquad
R_J=\left(\sum_{k>J+1}b_k^2\right)^{1/2}.
$$

If $w_k\neq0$, define

$$
\psi_k(x)
=
\frac{|w_k(x)|w_k(x)}{\|w_k\|_3^2},
$$

then

$$
\|\psi_k\|_{3/2}=1,
\qquad
\langle w_k,\psi_k\rangle=\|w_k\|_3.
$$

Let

$$
\boxed{
\phi_k
=
\frac{b_k}{R_J}\psi_k
}
$$

and when $w_k=0$, let $\phi_k=0$.

Denote

$$
\Phi_J=(\phi_k)_{k>J+1}.
$$

---

# 10. C3.2 — Dual-Witness Theorem

## Theorem 10.1

We have

$$
\boxed{\|\Phi_J\|_{X_{J+1}^*}=1,}
$$

and

$$
\boxed{\langle W_J,\Phi_J\rangle=R_J.}
$$

### Proof

By definition,

$$
\|\phi_k\|_{3/2}=\frac{b_k}{R_J},
$$

hence

$$
\|\Phi_J\|_{X_{J+1}^*}^2
=
\sum_{k>J+1}\frac{b_k^2}{R_J^2}=1.
$$

And

$$
\begin{aligned}
\langle W_J,\Phi_J\rangle
&=
\sum_{k>J+1}
\frac{b_k}{R_J}
\langle w_k,\psi_k\rangle
\\
&=
\frac1{R_J}\sum_{k>J+1}b_k^2
\\
&=R_J.
\end{aligned}
$$

$\square$

---

# 11. The Role of the Dual Witness

$\Phi_J$ is neither a physical field nor a new invariant.

It is

$$
\boxed{
\text{a norm-attaining linear certificate for the actual nonlinear tail increment}.
}
$$

Therefore, the norm-level fact

$$
\|W_J\|_{X_{J+1}}
$$

can be recast as a linear pairing against the exact N--S source.

---

# 12. Dyadic Parent-Output Source

For $p,q\ge-1$ and output $k>J+1$, define the ordered dyadic parent-output source

$$
\boxed{
F_{k;p,q}(r)
=
\Delta_k\mathbb P\nabla\cdot(u_p\otimes u_q)(r).
}
$$

Under the smooth/rapid-decay hypotheses of this paper,

$$
\Delta_k\mathbb P\nabla\cdot(u\otimes u)
=
\sum_{p,q\ge-1}F_{k;p,q}
$$

is absolutely convergent in the required finite-window topology.

---

# 13. Exact Signed Triad Ledger

Define

$$
\boxed{
\Lambda^{(J)}_{k;p,q}
=
-
\int_{s_J}^{t_J}
\left\langle
 e^{\nu(t_J-r)\Delta}F_{k;p,q}(r),
 \phi_k
\right\rangle dr.
}
$$

This is a signed quantity; it can be positive, zero, or negative.

---

# 14. C3.3 — Exact Parent Ledger Identity

## Theorem 14.1

For each PF-A edge,

$$
\boxed{
\sum_{k>J+1}\sum_{p,q\ge-1}
\Lambda^{(J)}_{k;p,q}
=R_J.
}
$$

Therefore,

$$
\boxed{
\sum_{k,p,q}\Lambda^{(J)}_{k;p,q}
\ge d_J.
}
$$

### Proof

By Duhamel's formula, dyadic source decomposition, and Theorem 10.1,

$$
\begin{aligned}
R_J
&=\langle W_J,\Phi_J\rangle
\\
&=-\int_{s_J}^{t_J}
\sum_{k>J+1}
\left\langle
 e^{\nu(t_J-r)\Delta}F_k(r),
 \phi_k
\right\rangle dr
\\
&=\sum_{k>J+1}\sum_{p,q\ge-1}
\Lambda^{(J)}_{k;p,q}.
\end{aligned}
$$

Absolute convergence guarantees the validity of the exchange. Then use $R_J\ge d_J$. $\square$

---

# 15. Exact Ledger Does Not Equal Unique Causal Parent

What this paper obtains is the exact label

$$
(k;p,q),
$$

but the semantics of $\Lambda^{(J)}_{k;p,q}$ are: the signed contribution of this ordered dyadic parent pair to the actual nonlinear increment direction identified by $\Phi_J$.

Therefore,

$$
\boxed{
\text{exact ledger entry}
\neq
\text{unique causal parent}.
}
$$

---

# 16. Positive / Negative Parent Ledgers

Let

$$
[\lambda]_+=\max\{\lambda,0\},
\qquad
[\lambda]_- =\max\{-\lambda,0\}.
$$

Define

$$
\boxed{
P_J
=
\sum_{k,p,q}[\Lambda^{(J)}_{k;p,q}]_+,
}
$$

$$
\boxed{
N_J
=
\sum_{k,p,q}[\Lambda^{(J)}_{k;p,q}]_-.
}
$$

By absolute convergence,

$$
P_J<\infty,
\qquad
N_J<\infty.
$$

---

# 17. C3.4 — Parent Cancellation Debt

## Theorem 17.1

We have

$$
\boxed{P_J-N_J=R_J\ge d_J.}
$$

Therefore,

$$
\boxed{P_J\ge d_J+N_J.}
$$

$\square$

Define the parent cancellation ratio

$$
\boxed{
\zeta_J=\frac{N_J}{P_J}.
}
$$

Then

$$
0\le\zeta_J<1,
$$

and

$$
\boxed{
P_J=\frac{R_J}{1-\zeta_J},
\qquad
N_J=\frac{\zeta_JR_J}{1-\zeta_J}.
}
$$

If $\zeta_J\to1^-$, the gross positive/negative parent activity must diverge relative to the net increment.

---

# 18. Exact Parent Witness

Fix

$$
0<\theta<1.
$$

A triple $(k;p,q)$ is called a $\theta$-debt-paying parent witness if

$$
\boxed{
[\Lambda^{(J)}_{k;p,q}]_+
\ge
\theta R_J.
}
$$

Since $R_J\ge d_J$, it pays at least $\theta d_J$ of the first-passage debt.

---

# 19. C3.5 — Parent Witness / Multiplicity Dichotomy

## Theorem 19.1

For each PF-A edge and any $0<\theta<1$, at least one of the following holds:

### Branch W — Exact parent witness

There exists $(k;p,q)$ such that

$$
[\Lambda^{(J)}_{k;p,q}]_+
\ge\theta R_J.
$$

### Branch M — Parent multiplicity debt

If no such witness exists, the positive ledger has at least

$$
\boxed{
\left\lceil
\frac1{\theta(1-\zeta_J)}
\right\rceil
}
$$

nonzero parent-output triples.

### Proof

If the positive support is finite and consists of $m$ terms, with each term being less than $\theta R_J$, then

$$
P_J<m\theta R_J.
$$

Using

$$
P_J=\frac{R_J}{1-\zeta_J}
$$

yields

$$
m>\frac1{\theta(1-\zeta_J)}.
$$

If the support is infinite, the conclusion holds automatically. $\square$

---

# 20. The Significance of Multiplicity Debt

Exact Parent Resolution is no longer binary

$$
\text{found}
\vee
\text{not found}.
$$

It now becomes

$$
\boxed{
\text{single strong witness}
\vee
\text{quantified parent multiplicity}.
}
$$

Furthermore, the more severe the cancellation corridor, the larger the required multiplicity lower bound if there is no single strong witness.

---

# 21. Fourier-Support Guard

Littlewood--Paley parent labels are not arbitrary graph labels. There exist constants $C_0,C_1<\infty$, depending only on the chosen LP partition, such that nonzero parent-output interactions obey a fixed support geometry.

---

# 22. C3.6 — No Far Up-Jump Lemma

## Lemma 22.1

If

$$
F_{k;p,q}\neq0,
$$

then

$$
\boxed{
k\le\max\{p,q\}+C_0.
}
$$

Equivalently,

$$
\boxed{
\max\{p,q\}\ge k-C_0.
}
$$

### Proof

In Fourier space, there exist parent frequencies $\eta,\zeta$ and output frequency $\xi$ satisfying

$$
\xi=\eta+\zeta,
$$

and

$$
|\eta|\sim2^p,
\qquad
|\zeta|\sim2^q,
\qquad
|\xi|\sim2^k.
$$

The triangle inequality gives

$$
|\xi|
\le
|\eta|+|\zeta|
\lesssim
2^{\max\{p,q\}}.
$$

Converting to dyadic indices yields the result. The Leray projection, derivative, and heat multiplier do not enlarge the Fourier support. $\square$

---

# 23. No Spontaneous Distant UV Jump

Lemma 22.1 excludes:

$$
p,q\ll k
$$

two parent shells far below the child directly generating $k$ in a single quadratic interaction.

Therefore, every high-frequency source event must contain:

$$
\boxed{
\text{at least one parent within bounded distance below the output, or a parent already above it}.
}
$$

This is an equation-level ancestry restriction.

---

# 24. C3.7 — Resonant Downshift Lemma

## Lemma 24.1

There exists $C_1<\infty$ such that if

$$
F_{k;p,q}\neq0
$$

and

$$
\max\{p,q\}-k>C_1,
$$

then

$$
\boxed{|p-q|\le C_1.}
$$

### Proof

If, for example, $p\gg q$, then the low parent $q$ cannot cancel the Fourier magnitude of the high parent $p$, thus

$$
|\eta+\zeta|\sim2^p,
$$

forcing

$$
k=p+O(1).
$$

Hence, a large downward separation can only be produced by comparable high--high frequencies. $\square$

---

# 25. Parent-Output Gap

For a nonzero candidate triple, define

$$
\boxed{
g(k;p,q)=\max\{p,q\}-k.}
$$

Lemma 22.1 gives

$$
g(k;p,q)\ge-C_0.
$$

If

$$
g(k;p,q)\gg1,
$$

then Lemma 24.1 forces

$$
|p-q|=O(1).
$$

Therefore,

$$
\boxed{
\text{large positive parent-output gap}
\Longrightarrow
\text{near-resonant high--high downshift}.
}
$$

---

# 26. Positive Parent-Gap Ledger

Fix

$$
L>C_1.
$$

Define

$$
P_J^{near}(L)
=
\sum_{g(k;p,q)\le L}
[\Lambda^{(J)}_{k;p,q}]_+,
$$

and

$$
P_J^{down}(L)
=
\sum_{g(k;p,q)>L}
[\Lambda^{(J)}_{k;p,q}]_+.
$$

Then

$$
P_J^{near}(L)+P_J^{down}(L)=P_J.
$$

---

# 27. C3.8 — Near-Parent / Resonant-Downshift Gross Dichotomy

## Theorem 27.1

For any $L>C_1$, we have at least

$$
\boxed{P_J^{near}(L)\ge\frac{P_J}{2}}
$$

or

$$
\boxed{P_J^{down}(L)\ge\frac{P_J}{2}}.
$$

All contributing triples in the second branch belong to near-resonant high--high downshifts.

Moreover, since

$$
P_J\ge d_J+N_J,
$$

the dominant branch has a positive gross activity of at least

$$
\frac{d_J+N_J}{2}.
$$

$\square$

---

# 28. Per-Edge Tightness Does Not Equal Chain Tightness

For each fixed PF-A edge, by absolute convergence,

$$
P_J^{down}(L)\to0
\qquad
(L\to\infty).
$$

Therefore, the positive parent-gap ledger of every single edge is tight.

However, the required $L$ may depend on $J$, hence

$$
\boxed{
\text{per-edge tightness}
\not\Rightarrow
\text{uniform ancestry tightness}.
}
$$

This is a new quantifier gap for full Chain Necessity.

---

# 29. Normalized Parent-Gap Profile

Define the positive probability ledger

$$
\mu_J(k,p,q)
=
\frac{[\Lambda^{(J)}_{k;p,q}]_+}{P_J}.
$$

Then

$$
\sum_{k,p,q}\mu_J(k,p,q)=1.
$$

Define the cumulative parent tightness

$$
\boxed{
C_J^{par}(L)
=
\frac{P_J^{near}(L)}{P_J}.
}
$$

For each fixed $J$,

$$
C_J^{par}(L)\uparrow1
\qquad
(L\to\infty).
$$

---

# 30. C3.9 — Parent-Gap Concentration--Escape Theorem

## Theorem 30.1

Take any infinite PF-A edge sequence

$$
J_n\to\infty.
$$

There exists a subsequence, still denoted as $J_n$, such that for each integer $L>C_1$,

$$
c^{par}(L)
=
\lim_{n\to\infty}C_{J_n}^{par}(L)
$$

exists.

And $c^{par}(L)$ is monotonically non-decreasing with respect to $L$, therefore

$$
\boxed{
\alpha_{par}
=
\lim_{L\to\infty}c^{par}(L)
\in[0,1].
}
$$

### Proof

Extract subsequences successively for $L=C_1+1,C_1+2,\ldots$, then perform a diagonal extraction. Each $C_J^{par}(L)$ lies in $[0,1]$, and monotonicity is preserved in the limit. Thus, $c^{par}(L)$, as a bounded monotone sequence, has a limit as $L\to\infty$. $\square$

---

# 31. Three Regimes of Parent-Gap

### PT — Parent-tight

$$
\boxed{\alpha_{par}=1.}
$$

All positive ledger mass in the subsequential limit can ultimately be captured by a finite parent-output gap.

### PS — Parent-split

$$
\boxed{0<\alpha_{par}<1.}
$$

Part of the source activity remains bounded-gap, while part escapes to an arbitrarily large positive parent-output gap.

### PE — Parent-escape

$$
\boxed{\alpha_{par}=0.}
$$

Any fixed parent-output gap window fails to capture any positive ledger mass in the limit.

By Lemma 24.1, if the escaped mass of PS / PE escapes along $g\to+\infty$, it can only be paid by near-resonant high--high parents.

Therefore,

$$
\boxed{
\text{parent-gap escape}
\Longrightarrow
\text{resonant high--high downshift escape}.
}
$$

---

# 32. The True Remaining Gap in PF-A

RFP-03 has rewritten Exact Parent Resolution from the vague "finding a parent" to:

$$
\boxed{
\text{strong exact witness}
\vee
\text{quantified parent multiplicity}
}
$$

multiplied by

$$
\boxed{PT\vee PS\vee PE.}
$$

Therefore, the missing information has been transformed into uniform tightness, witness persistence, and resonant-downshift control.

---

# 33. PF-B: Synchronous Bypass

Now consider

$$
d_J=0.
$$

By RFP-02,

$$
\mathcal B_{J+1}(s_J)=M,
\qquad
\mathcal B_J(s_J)=M,
$$

so

$$
\boxed{\|u_{J+1}(s_J)\|_3=0,}
$$

and

$$
s_J=t_J.
$$

Therefore, the positive-time Duhamel increment of PF-A cannot be used directly.

---

# 34. Zero Interval Debt is Not Zero History

From $s_J=t_J$, one can only deduce: the selected first-passage edge has no positive time interval.

It cannot be deduced that the deeper tail has no earlier nonlinear formation history.

Therefore, what PF-B must track is not the interval source debt, but

$$
\boxed{
\text{where the threshold burden already resides at the synchronous crossing time}.
}
$$

---

# 35. Carrier Weights

At

$$
t=s_J=\tau_J(M)
$$

define

$$
\boxed{
\omega_{J,r}
=
\frac{\|u_{J+r}(s_J)\|_3^2}{M^2},
\qquad r\ge1.
}
$$

From $\mathcal B_J(s_J)=M$,

$$
\sum_{r\ge1}\omega_{J,r}=1.
$$

PF-B additionally has

$$
\boxed{\omega_{J,1}=0.}
$$

Define the cumulative carrier profile

$$
\boxed{
C_J^{car}(L)
=
\sum_{r=1}^{L}\omega_{J,r}.
}
$$

For a fixed $J$,

$$
C_J^{car}(L)\uparrow1
\qquad
(L\to\infty).
$$

---

# 36. C3.10 — Carrier-Depth Concentration--Escape Theorem

## Theorem 36.1

Take any infinite PF-B subsequence

$$
J_n\to\infty.
$$

There exists a further subsequence such that for each fixed $L$, we have

$$
c^{car}(L)
=
\lim_{n\to\infty}C_{J_n}^{car}(L).
$$

Let

$$
\boxed{
\alpha_{car}
=
\lim_{L\to\infty}c^{car}(L)
\in[0,1].
}
$$

### Proof

Similar to Theorem 30.1, use diagonal extraction and monotonicity. $\square$

---

# 37. Three Regimes of Carrier-Depth

### CT — Carrier-tight

$$
\boxed{\alpha_{car}=1.}
$$

The synchronous threshold burden in the subsequential limit can be captured by finite offset shells.

### CS — Carrier-split

$$
\boxed{0<\alpha_{car}<1.}
$$

Part of the burden remains at a bounded offset, while part escapes to arbitrarily deep shells.

### CE — Carrier-escape

$$
\boxed{\alpha_{car}=0.}
$$

For any fixed $L$,

$$
C_{J_n}^{car}(L)\to0.
$$

Therefore, any fixed number of shells above $J_n$ cannot carry a nontrivial fraction of the threshold burden.

---

# 38. The Difference Between PF-A and PF-B Escapes

$\alpha_{par}$ describes

$$
\text{source provenance geometry},
$$

while $\alpha_{car}$ describes

$$
\text{state occupancy geometry}.
$$

Therefore,

$$
\boxed{\alpha_{par}\neq\alpha_{car}}
$$

is not a numerical inequality, but a reminder that the two fundamentally belong to different typed layers and cannot substitute for each other.

---

# 39. C3.11 — Infinite Edge Subsequence Classification

## Theorem 39.1

Consider any infinite first-passage edge sequence

$$
J_n\to\infty.
$$

There exists a subsequence falling into one of the following:

### A — PF-A source-paid subsequence

$$
d_{J_n}>0
$$

for all $n$, and the parent-gap profile further splits into

$$
PT\vee PS\vee PE.
$$

### B — PF-B synchronous subsequence

$$
d_{J_n}=0
$$

for all $n$, and the carrier-depth profile further splits into

$$
CT\vee CS\vee CE.
$$

### Proof

The binary partition $d_J>0$ and $d_J=0$ has at least one branch containing an infinite subsequence; then apply Theorem 30.1 or 36.1. $\square$

---

# 40. The Branch Closest to Full Ancestry

Currently, the closest to a complete source-traceable ancestry is

$$
\boxed{\mathrm{PF\mbox{-}A}+PT.}
$$

But it still requires:

1. Upgrading subsequential parent tightness to uniform / quantitative tightness;
2. Chaining strong witnesses across edges into a persistent parent-child history;
3. Attaching global frequency labels to physical-space cores;
4. Controlling pressure/localization commutators;
5. Preserving the time direction and source stock/supply separation.

---

# 41. Research Significance of PE / CE

If PE or CE can be persistently realized, the bounded-gap local-cascade proof strategy will fail.

But this does not mean the RFP fails; the escape route has been compressed to

$$
\boxed{
\text{resonant high--high downshift}
}
$$

or

$$
\boxed{
\text{deep carrier escape}.
}
$$

In the future, taxes / obstructions can be specifically established for these two geometries.

---

# 42. Relationship with Classical Dyadic Flux Analysis

Classical Littlewood--Paley energy-flux analysis shows that nonlinear flux can be organized by dyadic shells, and frequency localization provides substantial restrictions on the transfer structure.

This paper does not treat the energy-flux identity directly as an $L^3$ first-passage parent theorem; the main novel operation of this paper is

$$
\boxed{X_J-X_J^*\text{ dual norming witness},}
$$

whose purpose is to resolve the actual Duhamel increment direction, rather than merely tracking the scalar energy flux.

---

# 43. Relationship with Recent Triadic / Ledger Work

In 2026, there are already preprints establishing deterministic scale-resolved energy-transfer representations using explicit triadic Fourier decomposition, as well as finite-scale critical-ledger works emphasizing that defect, positive cone, and anti-phantom tests must be separated.

This paper views these as contemporary comparisons and does not take any of their global claims as theorem inputs for this paper.

The core requirements for Theorems 7.1--39.1 are only:

- Duhamel formula;
- standard LP decomposition;
- $L^3$ heat contraction;
- explicit Banach dual witness;
- Fourier support geometry;
- smooth finite-window absolute convergence.

---

# 44. New Guards

The following hard guards are added:

### $G_{\rm DUAL}$

When upgrading from norm magnitude to parent contribution, there must be a linear witness / dual certificate or an equivalent bridge.

### $G_{\rm SIGN}$

The signed ledger must be preserved; one cannot merely preserve $|\Lambda_{k;p,q}|$.

### $G_{\rm PMULT}$

When there is no single strong witness, the parent multiplicity debt must be preserved.

### $G_{\rm DOWN}$

A large parent-output downshift must satisfy the near-resonant high--high support condition.

### $G_{\rm PTIGHT}$

Per-edge tightness must not be surreptitiously replaced by uniform chain tightness.

### $G_{\rm CARRIER}$

The zero interval debt of PF-B must not be surreptitiously replaced by a zero historical source; the carrier-depth profile must be preserved.

---

# 45. Guard Library v2

Therefore,

$$
\boxed{
\mathcal G_{NS}^{(2)}
=
\mathcal G_{NS}^{(1)}
\cup
\{
G_{\rm DUAL},
G_{\rm SIGN},
G_{\rm PMULT},
G_{\rm DOWN},
G_{\rm PTIGHT},
G_{\rm CARRIER}
\}.
}
$$

---

# 46. Chain Necessity Update

RFP-02 compressed the full CN gap into

$$
\text{Synchronous-Bypass Resolution}
+
\text{Exact Parent Resolution}
+
\text{Spatial-Core Attachment}.
$$

After RFP-03, Exact Parent Resolution is further split into

$$
\boxed{
\text{Dual Parent Ledger}
+
\text{Witness/Multiplicity}
+
\text{Parent-Gap Tightness}.
}
$$

The first two items are completed in this paper; the third item only achieves the subsequential PT / PS / PE classification.

---

# 47. Remaining Obligations

## O1 — Uniform Parent Tightness

Can PS / PE be excluded, or at least can it be proven that PT contains a sufficient ancestry subsequence?

## O2 — Witness Persistence

Can the strong $(k;p,q)$ witness of each edge be chained across edges into a consistent parent-child history?

## O3 — Parent Cancellation Control

Can the exact N--S structure restrict

$$
\zeta_J\to1^-?
$$

## O4 — Resonant Downshift Control

Can the high--high downshift source of

$$
g\to+\infty,
\qquad
|p-q|=O(1)
$$

be controlled?

## O5 — Carrier Escape Control

Can CE be excluded or rigidified?

## O6 — Spatial Core Attachment

How can the global-frequency dual witness $\Phi_J$ be connected to $\Omega_J$ and the C3-O adjoint ancestry tube?

---

# 48. Why Must the Next Paper Spatialize?

Currently, the exact parent ledger is still

$$
\boxed{\text{global-frequency provenance}.}
$$

True singularity formation must simultaneously preserve

$$
(x,t,\lambda).
$$

Therefore, a localization bridge of

$$
\boxed{
(k;p,q)
\longrightarrow
(\Omega_k;\Omega_p,\Omega_q)
}
$$

is still needed.

However, localization will introduce cutoff commutators, pressure nonlocality, forced N--S terms, and moving-core geometry.

---

# 49. Next Paper

The formal next paper:

$$
\boxed{
\textbf{NS-RFP 04 — Spatial Core Attachment, Pressure-Compatible Localization, and Uniform Parent Tightness}.
}
$$

Core tasks:

1. Establish physical-space localization for $\Phi_J$;
2. Control $[\chi,\Delta_k]$ and $[\chi,\mathbb P]$;
3. Perform a near/far provenance split on the pressure;
4. Connect to the C3-O adjoint ancestry tube;
5. Determine whether PT can be upgraded to spacetime ancestry;
6. Establish nonlocal escape taxes for PE / CE.

---

# 50. Formal Status Ledger

$$
\boxed{
\begin{aligned}
\text{tail Banach-space reformulation}
&:\ \mathrm{PROVED},\\
\text{constructive dual norming witness}
&:\ \mathrm{PROVED},\\
\text{exact signed dyadic parent ledger}
&:\ \mathrm{PROVED\ under\ smooth/decay\ hypotheses},\\
\text{parent cancellation debt}
&:\ \mathrm{PROVED},\\
\text{parent witness/multiplicity dichotomy}
&:\ \mathrm{PROVED},\\
\text{no far upward quadratic jump}
&:\ \mathrm{PROVED},\\
\text{far downshift implies resonant high--high parents}
&:\ \mathrm{PROVED},\\
\text{parent-gap subsequential concentration--escape}
&:\ \mathrm{PROVED},\\
\text{carrier-depth subsequential concentration--escape}
&:\ \mathrm{PROVED},\\
\text{uniform parent tightness}
&:\ \mathrm{OPEN},\\
\text{witness persistence across edges}
&:\ \mathrm{OPEN},\\
\text{resonant downshift exclusion}
&:\ \mathrm{OPEN},\\
\text{carrier escape exclusion}
&:\ \mathrm{OPEN},\\
\text{spatial-core ancestry}
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

# 51. Conclusion

RFP-02 obtained

$$
\boxed{
\text{time order}
+
\text{scale order}
+
\text{aggregate nonlinear source debt}.
}
$$

RFP-03 takes one step further:

$$
\boxed{
\text{aggregate source debt}
\longrightarrow
\text{exact signed parent-output ledger}.
}
$$

For each PF-A edge, there exists a dual witness $\Phi_J$ such that

$$
\boxed{
R_J
=
\sum_{k,p,q}\Lambda^{(J)}_{k;p,q}
\ge d_J.
}
$$

If there is no single strong witness, a quantified parent multiplicity debt must be paid; if the cancellation is near perfect, the multiplicity lower bound is stronger.

Meanwhile, the Fourier support excludes two far-lower parents generating a far-higher child in a single quadratic interaction, and a large downward parent-output gap can only take the near-resonant high--high route.

Therefore, the remaining route of PF-A is compressed into

$$
\boxed{PT\vee PS\vee PE,}
$$

while PF-B is compressed into

$$
\boxed{CT\vee CS\vee CE.}
$$

The new frontier is no longer just "where is the source", but rather:

$$
\boxed{
\text{can exact frequency provenance be made uniformly tight, persistent, and spatially attached?}
}
$$

This is NS-RFP 04.

---

# References

1. J.-M. Bony, *Calcul symbolique et propagation des singularités pour les équations aux dérivées partielles non linéaires*, Annales scientifiques de l'École Normale Supérieure 14 (1981), 209–246.
2. A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy, *Energy conservation and Onsager's conjecture for the Euler equations*, Nonlinearity 21 (2008), 1233–1252; arXiv:0704.0759.
3. Z. Bradshaw, Z. Grujić, *Frequency localized regularity criteria for the 3D Navier–Stokes equations*, Archive for Rational Mechanics and Analysis 224 (2017), 125–133; arXiv:1501.01043.
4. A. Cheskidov, R. Shvydkoy, *A unified approach to regularity problems for the 3D Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*, Journal of Mathematical Fluid Mechanics 16 (2014), 263–273.
5. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, Journal of Mathematical Fluid Mechanics 24 (2022); arXiv:2001.11526.
6. T. Barker, C. Prange, *Localized smoothing for the Navier–Stokes equations and concentration of critical norms near singularities*, Archive for Rational Mechanics and Analysis 236 (2020), 1487–1541; arXiv:1812.09115.
7. R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier–Stokes*, arXiv:2606.13887 (2026). Contemporary comparison only; no global conclusion from this preprint is used as an input theorem here.
8. E. Bertram, *From Triadic Interactions to Kolmogorov Scaling: A Deterministic, Scale-Resolved Formulation of Energy Flux*, arXiv:2607.16381 (2026). Contemporary comparison only; no global conclusion from this preprint is used as an input theorem here.

# Internal dependencies

- `NS_RFP_01_SingularityFormationAncestry_FiniteObstruction_v0.1.md`
- `NS_RFP_02_CriticalUV_FirstPassage_SourceDebt_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.2.md`
- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

# Next

$$
\boxed{
\textbf{NS-RFP 04 — Spatial Core Attachment, Pressure-Compatible Localization, and Uniform Parent Tightness}
}
$$