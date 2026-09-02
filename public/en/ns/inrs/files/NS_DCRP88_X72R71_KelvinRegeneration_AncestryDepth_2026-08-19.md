# DCRP88 / X72-R71 — Kelvin-Holonomy Regeneration Depth and the No-Compact-Ancestry Conveyor Theorem

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / same-parent regeneration round  
**Immediate predecessor:** `NS_DCRP87_X72R70_RecurrentWorkObservability_2026-08-18.md`

**Primary internal dependencies**
- DCRP32–33 — self-similar Kelvin holonomy / circulation replenishment
- DCRP31 — native Morrey profile control
- DCRP81–85 — viscous Kelvin residue reduced to existing SGS/trace/scale defects
- DCRP87 — compact recurrent resolved-badness-to-signed-work observability

**Fresh primary-source calibration**
- P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570 (2026). The self-similar Weber/Kelvin law is
  \[
  e^{(1-2\gamma)\tau}\Gamma_{\rm ss}(\tau)=\Gamma_{\rm ss}(0),
  \]
  and \(\gamma=1/2\) is distinguished by circulation.
- R. Yu, *Coarse-Grained Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness*, arXiv:2606.25322.
- R. Yu, *Critical Ledgers and Scale-Defect Cascades for Navier-Stokes*, arXiv:2606.13887.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

DCRP87 closed the **work-visibility** gap on the same-parent recurrent compact class:

\[
\boxed{
\text{resolved badness}
\Longrightarrow
W_+\vee W_-
}
\]

after the already-declared residual / leakage / return / tail / compactness escapes are removed.

However the exact coarse-work depletion theorem carries geometric physical weights

\[
w_k=\frac{r_k}{r_0},
\]

so even a uniform normalized work gap remains summable.

DCRP88 shows that **compact same-parent regeneration cannot exploit that summability indefinitely**.

The reason is not energy.

It is Kelvin holonomy.

For the strict Type-II similarity window

\[
\boxed{
\frac25<\gamma<\frac12,
}
\]

define

\[
\boxed{
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}
\in(0,1).
}
\]

For every similarity-material loop,

\[
\boxed{
\Gamma_{n+1}
=
\rho_\Gamma\Gamma_n.
}
\]

Equivalently, along backward material ancestry,

\[
\boxed{
\Gamma_{-n}
=
\rho_\Gamma^{-n}\Gamma_0.
}
\]

DCRP88 proves a new bridge:

> **compact resolved badness itself forces a uniform finite family of nonzero circulation atoms.**

Indeed, if a global divergence-free resolved profile had zero circulation on every closed loop, then

\[
\nabla\times U=0.
\]

Since also

\[
\nabla\cdot U=0,
\]

each component of \(U\) is harmonic.

The native global Morrey law

\[
\int_{B_R}|U|^2\le CM_0R
\]

then forces

\[
U\equiv0.
\]

The residual-free similarity momentum equation gives

\[
\nabla P=0.
\]

Hence the resolved CKN badness vanishes.

Therefore a compact class with

\[
\Psi^\ell\ge b_0>0
\]

is uniformly separated from the zero-circulation set.

Compactness gives finitely many loop templates

\[
C_1,\ldots,C_N
\]

and

\[
\boxed{
c_\Gamma>0
}
\]

such that every package in the class has

\[
\boxed{
\max_i
\left|
\oint_{C_i}U\cdot dy
\right|
\ge
c_\Gamma.
}
\]

Now let \(\mathcal L_*\) be any compact material-loop state class on which circulation is continuous.

Set

\[
\boxed{
\Gamma_*
=
\sup_{
U\in\mathcal K,\ C\in\mathcal L_*
}
\left|
\oint_CU\cdot dy
\right|
<\infty.
}
\]

A circulation atom with

\[
|\Gamma_0|\ge c_\Gamma
\]

cannot have all of its backward material ancestors remain inside \(\mathcal L_*\).

Indeed,

\[
\rho_\Gamma^{-n}c_\Gamma
\le
\Gamma_*
\]

would be required.

Thus:

## Main finite-depth ancestry theorem

\[
\boxed{
N_*
=
1+
\left\lfloor
\frac{
\log(\Gamma_*/c_\Gamma)
}{
\log(1/\rho_\Gamma)
}
\right\rfloor
}
\]

has the property that every \(c_\Gamma\)-circulation atom must leave \(\mathcal L_*\) within at most \(N_*\) backward DSS periods.

So:

\[
\boxed{
\text{resolved badness regeneration}
\Longrightarrow
\text{finite-depth material ancestry escape}
}
\]

unless a Kelvin-shadowing defect is already active.

This is **unweighted** and bypasses the geometrically summable signed-work ledger.

---

# 1. Exact Kelvin holonomy in the present normalization

Let

\[
V(y,s)=\gamma y+U(y,s).
\]

Since

\[
\gamma y
=
\nabla\left(
\frac\gamma2|y|^2
\right),
\]

\(V\) and \(U\) have the same circulation on every closed loop.

Let \(C_s\) be a similarity-material loop transported by \(V\).

Physical Euler Kelvin conservation becomes:

## Theorem D88.1 — Time-Dependent Similarity Kelvin Law

\[
\boxed{
e^{(1-2\gamma)s}
\oint_{C_s}
U(y,s)\cdot dy
=
\oint_{C_0}
U(y,0)\cdot dy.
}
\tag{1.1}
\]

This law does not require the similarity profile to be stationary.

For a DSS period \(S_0\),

\[
\boxed{
\Gamma(s+S_0)
=
\rho_\Gamma\Gamma(s),
}
\tag{1.2}
\]

where

\[
\boxed{
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}.
}
\tag{1.3}
\]

Because

\[
\gamma<1/2,
\]

\[
\boxed{
0<\rho_\Gamma<1.
}
\tag{1.4}
\]

---

# 2. Relation to the \(\alpha\) scaling

Use

\[
\gamma=\frac1{\alpha+1},
\]

and DSS spatial factor

\[
\Lambda>1
\]

with

\[
S_0
=
(\alpha+1)\log\Lambda.
\]

Then:

\[
\begin{aligned}
(1-2\gamma)S_0
&=
\left(
1-\frac2{\alpha+1}
\right)
(\alpha+1)\log\Lambda
\\
&=
(\alpha-1)\log\Lambda.
\end{aligned}
\]

Therefore:

## Theorem D88.2 — Exact Circulation Multiplier

\[
\boxed{
\rho_\Gamma
=
\Lambda^{-(\alpha-1)}.
}
\tag{2.1}
\]

In the strict Type-II interval:

\[
1<\alpha<3/2,
\]

so:

\[
\rho_\Gamma<1.
\]

---

# 3. Zero circulation on all loops implies curl-free resolved velocity

Fix one smooth global resolved profile \(U\).

Suppose:

\[
\boxed{
\oint_CU\cdot dy=0
}
\]

for every smooth closed loop \(C\subset\mathbb R^3\).

By Stokes:

\[
\boxed{
\nabla\times U=0.
}
\tag{3.1}
\]

Since:

\[
\nabla\cdot U=0,
\]

the vector Laplacian identity gives:

\[
\boxed{
\Delta U
=
\nabla(\nabla\cdot U)
-
\nabla\times(\nabla\times U)
=
0.
}
\tag{3.2}
\]

Thus every component \(U_j\) is an entire harmonic function.

---

# 4. Native Morrey kills every global curl-free mode

Assume:

\[
\boxed{
\int_{B_R(0)}
|U|^2dy
\le
CM_0R
}
\]

for all sufficiently large \(R\).

Fix:

\[
x_0\in\mathbb R^3.
\]

For \(R>2|x_0|\),

\[
B_R(x_0)
\subset
B_{2R}(0).
\]

The harmonic mean-value estimate gives:

\[
|U(x_0)|^2
\le
C
R^{-3}
\int_{B_R(x_0)}
|U|^2dy.
\]

Hence:

\[
|U(x_0)|^2
\le
C
R^{-3}
\cdot
CM_0(2R)
=
C'M_0R^{-2}.
\]

Let:

\[
R\to\infty.
\]

Therefore:

## Theorem D88.3 — Curl-Free Morrey Rigidity

\[
\boxed{
U\equiv0.
}
\tag{4.1}
\]

This is global and requires no periodic material-loop recurrence.

---

# 5. Pressure also collapses on the residual-free similarity profile

The time-dependent similarity Euler momentum equation is:

\[
\boxed{
\partial_sU
+
(1-\gamma)U
+
(\gamma y+U)\cdot\nabla U
+
\nabla P
=
0.
}
\tag{5.1}
\]

If:

\[
U\equiv0,
\]

then:

\[
\boxed{
\nabla P=0.
}
\tag{5.2}
\]

Thus every resolved velocity-pressure badness coordinate vanishes.

Therefore:

## Theorem D88.4 — Resolved Badness Requires Circulation

On the global residual-free native Morrey class,

\[
\boxed{
\Psi^\ell>0
\Longrightarrow
\exists C:
\oint_CU\cdot dy\neq0.
}
\tag{5.3}
\]

---

# 6. Compactness upgrades existence to a uniform circulation gap

Let:

\[
\mathcal K
\]

be a compact class of smooth global resolved similarity packages satisfying:

\[
\Psi^\ell\ge b_0>0,
\]

and the native Morrey bound.

For each:

\[
X=(U,P)\in\mathcal K,
\]

choose a loop:

\[
C_X
\]

such that:

\[
\Gamma_X
=
\left|
\oint_{C_X}U\cdot dy
\right|
>0.
\]

By continuity of the circulation functional in the profile topology, there exists an open neighborhood:

\[
\mathcal U_X
\]

such that for every:

\[
Y\in\mathcal U_X,
\]

\[
\left|
\oint_{C_X}U_Y\cdot dy
\right|
\ge
\frac12\Gamma_X.
\]

Compactness gives a finite subcover:

\[
\mathcal U_{X_1},
\ldots,
\mathcal U_{X_N}.
\]

Set:

\[
C_i=C_{X_i},
\]

and:

\[
\boxed{
c_\Gamma
=
\frac12
\min_{1\le i\le N}
\Gamma_{X_i}
>0.
}
\tag{6.1}
\]

Then:

## Theorem D88.5 — Finite Circulation-Atom Compiler

\[
\boxed{
\forall X\in\mathcal K,
\qquad
\max_{1\le i\le N}
\left|
\oint_{C_i}U_X\cdot dy
\right|
\ge
c_\Gamma.
}
\tag{6.2}
\]

This is the circulation analogue of D87's finite active-work test compiler.

---

# 7. Backward Kelvin amplification

Fix one phase.

Let:

\[
\Phi
\]

be the one-period similarity Poincaré map on material loops.

For a loop \(C\),

\[
\boxed{
\Gamma(\Phi C)
=
\rho_\Gamma\Gamma(C).
}
\tag{7.1}
\]

Since \(\Phi\) is invertible on the smooth material-flow branch,

\[
\boxed{
\Gamma(\Phi^{-1}C)
=
\rho_\Gamma^{-1}\Gamma(C).
}
\tag{7.2}
\]

Iterating:

## Theorem D88.6 — Backward Circulation Amplification

\[
\boxed{
\left|
\Gamma(\Phi^{-n}C)
\right|
=
\rho_\Gamma^{-n}
|\Gamma(C)|.
}
\tag{7.3}
\]

Because:

\[
\rho_\Gamma^{-1}>1,
\]

backward material ancestry amplifies normalized circulation geometrically.

---

# 8. Finite-depth compact-ancestry escape

Let:

\[
\mathcal L_*
\]

be any compact class of smooth closed loops in a topology for which:

\[
(U,C)
\mapsto
\oint_CU\cdot dy
\]

is continuous on:

\[
\mathcal K\times\mathcal L_*.
\]

Then:

\[
\boxed{
\Gamma_*
=
\sup_{
U\in\mathcal K,\ C\in\mathcal L_*
}
\left|
\oint_CU\cdot dy
\right|
<\infty.
}
\tag{8.1}
\]

Take a circulation atom:

\[
C_0\in\mathcal L_*
\]

with:

\[
|\Gamma(C_0)|\ge c_\Gamma.
\]

Suppose:

\[
\Phi^{-n}C_0\in\mathcal L_*
\]

for:

\[
n=0,\ldots,N.
\]

Then D88.6 gives:

\[
\rho_\Gamma^{-N}c_\Gamma
\le
\Gamma_*.
\]

Therefore:

## Theorem D88.7 — Finite Ancestry Depth Bound

\[
\boxed{
N
\le
\frac{
\log(\Gamma_*/c_\Gamma)
}{
\log(1/\rho_\Gamma)
}.
}
\tag{8.2}
\]

Define:

\[
\boxed{
N_*
=
1+
\left\lfloor
\frac{
\log(\Gamma_*/c_\Gamma)
}{
\log(1/\rho_\Gamma)
}
\right\rfloor.
}
\tag{8.3}
\]

Then every \(c_\Gamma\)-circulation atom exits \(\mathcal L_*\) within at most \(N_*\) backward DSS periods.

This is the main theorem of D88.

---

# 9. What “exit the loop compactum” means

If:

\[
\Phi^{-n}C
\]

leaves every declared compact loop-state class, at least one of the following occurs:

1. normalized support / ancestry escapes:
   \[
   R_{\rm tail};
   \]

2. loop length, curvature, or spatial oscillation loses compactness:
   \[
   R_{\rm fil};
   \]

3. topology / packet / loop-state shadowing fails:
   \[
   R_{\rm state};
   \]

4. prelimit Kelvin shadowing carries a nonzero residual:
   \[
   R_K.
   \]

But D81–85 have already reduced \(R_K\) into:

- existing increment activity;
- scale-gap debt;
- tail / filamentation / state defects.

Thus:

## Theorem D88.8 — No Compact Regeneration Conveyor

On the zero-residual late branch,

\[
\boxed{
\text{resolved badness regeneration}
\Longrightarrow
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
\widetilde{\mathcal S}_{\rm active}
\vee
\mathfrak D_{\rm gap}.
}
\tag{9.1}
\]

There is no indefinitely compact same-parent circulation-regeneration conveyor.

---

# 10. Robust prelimit version

In the prelimit Navier–Stokes sequence, suppose one-period circulation satisfies:

\[
\boxed{
|
\Gamma_{k+1}
-
\rho_\Gamma\Gamma_k
|
\le
\eta.
}
\tag{10.1}
\]

Iterating backward/forward algebra gives:

\[
\boxed{
|
\Gamma_0
-
\rho_\Gamma^n\Gamma_{-n}
|
\le
\eta
\frac{
1-\rho_\Gamma^n
}{
1-\rho_\Gamma
}.
}
\tag{10.2}
\]

Hence if:

\[
|\Gamma_0|\ge c_\Gamma
\]

and:

\[
\boxed{
\eta
\le
\frac12
(1-\rho_\Gamma)c_\Gamma,
}
\tag{10.3}
\]

then:

\[
\boxed{
|\Gamma_{-n}|
\ge
\frac12
c_\Gamma
\rho_\Gamma^{-n}.
}
\tag{10.4}
\]

Therefore the same finite-depth escape theorem survives with:

\[
c_\Gamma
\]

replaced by:

\[
c_\Gamma/2.
\]

If (10.3) fails, the Kelvin-shadowing residual itself has a uniform normalized gap and is already an active terminal defect.

---

# 11. Why this bypasses weighted-work summability

D87 left the exact concern:

\[
|W_k|\ge c_W
\]

but:

\[
\sum_k
\frac{r_k}{r_0}
c_W
<
\infty.
\]

D88 does not attempt to make this weighted sum diverge.

Instead it proves:

\[
\boxed{
\text{compact material ancestry cannot persist beyond }N_*\text{ periods}.
}
\]

The bound:

\[
N_*
\]

contains no factor:

\[
r_k/r_0.
\]

It is a normalized holonomy obstruction.

Thus the same-parent regeneration problem is not purely an energy-depletion problem.

---

# 12. Regeneration is source replacement, not closed recurrence

At every recurrent phase, D88.5 supplies a loop with:

\[
|\Gamma|\ge c_\Gamma.
\]

But the backward ancestry of that loop cannot remain compact indefinitely.

Therefore each regenerated high-circulation state must draw its circulation from:

- material tail ancestry;
- filamented / increasingly complex loop ancestry;
- a state-transition / packet-replacement event;
- or an active finite-scale Kelvin/SGS/scale defect.

This gives a precise meaning to “regeneration.”

It is not:

\[
\boxed{
\text{same compact material object reproducing itself}.
}
\]

It is:

\[
\boxed{
\text{continual replacement from outside any fixed compact ancestry class}.
}
\]

---

# 13. Finite loop permutations are impossible

Suppose a finite family of material loop states:

\[
C_1,\ldots,C_m
\]

is permuted after each DSS period.

Then after some finite number \(q\) of periods every loop returns to itself.

Kelvin holonomy gives:

\[
\Gamma(C_i)
=
\rho_\Gamma^q\Gamma(C_i).
\]

Since:

\[
0<\rho_\Gamma<1,
\]

we obtain:

## Theorem D88.9 — Finite Loop-Permutation NO-GO

\[
\boxed{
\Gamma(C_i)=0
}
\]

for every loop in the permutation cycle.

Therefore a finite circulation-atom library cannot realize exact material regeneration by permutation.

This complements the backward-depth theorem.

---

# 14. Relation to D32 and what is genuinely new here

D32 already proved:

\[
\boxed{
\text{recurrent material loop}
\Longrightarrow
\text{zero circulation}
}
\]

for strict DSS.

D88 adds two missing bridges:

## A. resolved badness forces a **uniform finite circulation atom family**

so the zero-circulation loophole is removed on the compact resolved-bad class;

## B. backward Kelvin amplification gives a **quantitative finite ancestry depth**

\[
N_*<\infty.
\]

Thus D88 converts D32's qualitative loop-holonomy obstruction into a regeneration theorem for the D87 bad-work-visible class.

---

# 15. Relation to the 2026 Constantin–Ignatova–Vicol theorem

The external paper derives the self-similar Kelvin law:

\[
e^{(1-2\gamma)\tau}
\Gamma_{\rm ss}(\tau)
=
\Gamma_{\rm ss}(0)
\]

for globally self-similar Euler.

D32 had already derived the same transformation directly from physical Kelvin conservation in the present project.

D88 uses only the circulation scaling law and extends the project logic to:

- DSS periodic phase;
- compact finite loop observability;
- same-parent regeneration depth.

No claim is made that the full globally self-similar theorems of that paper apply automatically to the time-periodic DSS profile.

---

# 16. What happens to the D87 forward/backscatter dichotomy

D87 gave:

\[
W_+\vee W_-.
\]

D88 now says:

> even if the signed work payments are physically summable, the regenerated resolved-bad state cannot be materially closed.

Therefore the combined late compiler is:

\[
\boxed{
\text{resolved recurrent badness}
}
\]

\[
\Downarrow
\]

\[
\boxed{
W_+\vee W_-
}
\]

and independently:

\[
\boxed{
\text{finite-depth ancestry escape}
}
\]

unless a previously named Kelvin/SGS/scale defect is active.

The two ledgers are complementary:

- work = energetic visibility;
- Kelvin = material ancestry visibility.

Neither is identified with the other.

---

# 17. Updated late frontier

The D87 question was:

\[
\boxed{
\text{can order-one normalized badness regenerate forever at geometrically summable work cost?}
}
\]

D88 answers:

\[
\boxed{
\textbf{
not inside a compact same-parent material ancestry class.
}
}
\]

Therefore any such infinite regeneration must be one of:

\[
\boxed{
R_{\rm tail}
\vee
R_{\rm fil}
\vee
R_{\rm state}
\vee
\widetilde{\mathcal S}_{\rm active}
\vee
\mathfrak D_{\rm gap}
}
\]

plus the already-visible forward/backscatter work channel.

The remaining issue is no longer a compact “critical regeneration conveyor.”

It is the packing/recurrence of explicit ancestry-escape modes.

---

# 18. What D88 does not prove

D88 does **not** prove:

- material-tail replenishment is impossible;
- filamentation is impossible;
- repeated loop-state replacement is impossible;
- repeated finite-depth ancestry escape has a globally finite budget;
- backscatter is impossible;
- global Navier–Stokes regularity.

It proves that geometric work summability cannot by itself produce an indefinitely compact same-parent regeneration mechanism.

---

# 19. New STOP

\[
\boxed{
\textbf{
STOP-D88:
The weighted signed-work summability problem can be bypassed on the compact same-parent ancestry branch by Kelvin holonomy. Strict Type-II similarity has a one-period circulation multiplier }\rho_\Gamma=e^{-(1-2\gamma)S_0}<1\textbf{. Meanwhile positive resolved badness on a compact residual-free native-Morrey class forces a uniform finite family of nonzero circulation atoms: if all loop circulations vanished, the resolved velocity would be globally curl-free and divergence-free, hence harmonic, and the Morrey law would force }U=0\textbf{ and then }\nabla P=0\textbf{. For any compact loop-state class with circulation ceiling }\Gamma_*\textbf{, backward Kelvin ancestry amplifies a }c_\Gamma\textbf{-atom by }\rho_\Gamma^{-n}\textbf{, so it must leave that compact class within the explicit finite depth }N_*=1+\lfloor\log(\Gamma_*/c_\Gamma)/\log(1/\rho_\Gamma)\rfloor\textbf{. Thus order-one normalized badness cannot regenerate forever by recycling a compact material ancestry even though its physical work cost is geometrically summable; regeneration must repeatedly enter tail, filamentation, state-transition, increment, or scale-gap defect channels.}
}
\]

---

# 20. Next autonomous step

## DCRP89 / X72-R72 — Finite-Depth Ancestry Escape Packing

**Working title**

> **Can Repeated Kelvin-Forced Ancestry Escape Be Packed into the Critical Tail / Filamentation Budgets without Creating a New Infinite Supplier?**

Primary tasks:

1. start from the uniform ancestry-depth bound:
   \[
   N_*<\infty;
   \]
2. follow the high-circulation predecessor that exits the compact loop class;
3. classify the first-exit mechanism quantitatively:
   - support radius;
   - loop length/curvature;
   - packet-state mismatch;
   - SGS/scale defect;
4. if support escapes, measure the minimum annular circulation/tube reservoir required at the exit radius;
5. compare with native:
   \[
   E(R)\lesssim R;
   \]
   without assuming an invalid codimension-two trace bound;
6. if loop geometry blows up, connect to the existing filamentation / direction-gradient compiler;
7. build a forest of circulation-ancestry exits and test bounded multiplicity;
8. seek:
   \[
   \text{repeated regeneration}
   \Longrightarrow
   R_{\rm tail}^{\rm paid}
   \vee
   R_{\rm fil}^{\rm paid}
   \vee
   R_{\rm state}^{\rm paid}
   \vee
   \text{one explicit infinite-supplier normal form}.
   \]

Desired endpoint:

\[
\boxed{
\text{finite-depth ancestry escape}
\Longrightarrow
\text{quantitative supplier debt}
\vee
\text{one explicit noncompact supplier}.
}
\]

---

# 21. One-line checkpoint

Resolved badness cannot be regenerated forever by a compact material ancestry: finite circulation observability plus the strict DSS Kelvin multiplier forces every order-one circulation atom to exit any compact loop-state class after a uniformly bounded number of backward periods, independently of the geometrically summable work weights.

---

**End checkpoint:** DCRP88 / X72-R71  
**Next:** DCRP89 / X72-R72 — Finite-Depth Ancestry Escape Packing.
