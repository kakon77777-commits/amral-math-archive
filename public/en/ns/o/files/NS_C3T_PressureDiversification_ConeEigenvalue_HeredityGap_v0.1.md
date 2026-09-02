---
title: "Navier–Stokes C3-T: Pressure-Support Diversification, Cone-to-Eigenvalue Barrier, and Hereditary-Ancestry Gap"
subtitle: "Quantitative Pressure Diversification, the Barrier from Five-Dimensional Mean-Strain Cones to Pointwise Middle-Eigenvalue Geometry, and the Missing Hereditary Lemma for Pressure-Poor Causal Rays"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Finite-dimensional matrix geometry + inherited pressure/enstrophy estimates + causal-tree selection no-go. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-T
# Pressure-Support Diversification, Cone-to-Eigenvalue Barrier, and Hereditary-Ancestry Gap

## 0. Context of this Round

C3-S has compressed the multi-core strain geometry into two branches:

$$
\boxed{
\text{uniform strain cone}
\quad\vee\quad
\text{cone degeneration}.
}
$$

In the uniform branch, the normalized local mean strains

$$
v_{n,i}
=
\frac{M_{n,i}}{|M_{n,i}|}
\in
S^4
\subset
\operatorname{Sym}_0(3)
$$

ultimately satisfy

$$
K_\ast:v_{n,i}
\ge
\gamma_0>0.
$$

In the degenerate branch,

$$
\gamma_n
=
\operatorname{dist}
\left(
0,\operatorname{conv}V_n
\right)
\to0,
$$

and one can extract an at-most-six-core witness.

This round addresses two unclosed problems:

1. Can the fixed 5D cone motif directly connect to Miller's $\lambda_2^+$ geometry?
2. Given a pressure-poor six-core witness at every scale, can we extract a pressure-poor causal ancestry ray?

The answer to both is:

$$
\boxed{
\textbf{Not directly.}
}
$$

However, both no-gos can be converted into precise new proof obligations.

---

# 1. Five-Dimensional Matrix Cone and Eigenvalue Signature

Let

$$
\mathbb S_0
=
\operatorname{Sym}_0(3).
$$

Take any

$$
K\in\mathbb S_0,
\qquad
|K|=1.
$$

Let its eigenvalues be

$$
\kappa_1\le\kappa_2\le\kappa_3.
$$

Since it is trace-free and nonzero:

$$
\boxed{
\kappa_1<0<\kappa_3.
}
$$

---

# 2. Two-Stretching Test Matrix

Define in the eigenbasis of $K$:

$$
\boxed{
V^+
=
\frac1{\sqrt6}
\operatorname{diag}(-2,1,1).
}
$$

Then

$$
|V^+|=1,
$$

and

$$
\boxed{
\lambda_2(V^+)
=
\frac1{\sqrt6}>0.
}
$$

Meanwhile,

$$
K:V^+
=
-\frac{3\kappa_1}{\sqrt6}
>0.
$$

---

# 3. One-Stretching Test Matrix

Define

$$
\boxed{
V^-
=
\frac1{\sqrt6}
\operatorname{diag}(-1,-1,2).
}
$$

Then

$$
|V^-|=1,
$$

and

$$
\boxed{
\lambda_2(V^-)
=
-\frac1{\sqrt6}<0.
}
$$

Meanwhile,

$$
K:V^-
=
\frac{3\kappa_3}{\sqrt6}
>0.
$$

---

# 4. C3-T.1: Half-Space Signature Non-Rigidity

## Theorem 4.1

For any nonzero

$$
K\in\operatorname{Sym}_0(3),
$$

the open half-space

$$
\mathcal H_K^+
=
\{
M:
K:M>0
\}
$$

simultaneously contains:

$$
\lambda_2(M)>0
$$

and

$$
\lambda_2(M)<0
$$

trace-free symmetric matrices.

Therefore,

$$
\boxed{
\text{fixed 5D strain half-space}
\not\Rightarrow
\text{middle-eigenvalue sign}.
}
$$

---

# 5. Narrow-Cone Eigenvalue Inheritance

If

$$
K,V\in\mathbb S_0,
\qquad
|K|=|V|=1,
$$

and

$$
K:V\ge\gamma,
$$

then

$$
|V-K|_F^2
=
2-2K:V
\le
2(1-\gamma).
$$

Thus,

$$
\boxed{
|V-K|_F
\le
\sqrt{2(1-\gamma)}.
}
$$

Weyl's inequality gives

$$
|\lambda_2(V)-\lambda_2(K)|
\le
\|V-K\|_{\rm op}
\le
\|V-K\|_F.
$$

Therefore:

## Theorem 5.1

$$
\boxed{
\lambda_2(V)
\ge
\lambda_2(K)
-
\sqrt{2(1-\gamma)}.
}
$$

and

$$
\boxed{
\lambda_2(V)
\le
\lambda_2(K)
+
\sqrt{2(1-\gamma)}.
}
$$

If

$$
\boxed{
\lambda_2(K)
>
\sqrt{2(1-\gamma)},
}
$$

then

$$
\lambda_2(V)>0.
$$

If

$$
\boxed{
\lambda_2(K)
<
-\sqrt{2(1-\gamma)},
}
$$

then

$$
\lambda_2(V)<0.
$$

---

# 6. New Splitting of the Uniform-Cone Branch

Therefore, the uniform branch of C3-S further splits into:

## T-A1 — Narrow nondegenerate cone

$$
\boxed{
|\lambda_2(K_\ast)|
>
\sqrt{2(1-\gamma_0)}.
}
$$

The $\lambda_2$ sign of the mean-strain directions is locked.

## T-A2 — Wide / eigenvalue-degenerate cone

$$
\boxed{
|\lambda_2(K_\ast)|
\le
\sqrt{2(1-\gamma_0)}.
}
$$

Cone coherence is insufficient to determine the middle-eigenvalue sign.

---

# 7. But This is Still Only Mean Strain

Local mean strain:

$$
M_i
=
\int\chi_iS\,dx.
$$

If

$$
m_i
=
\int\chi_i\,dx>0,
$$

define

$$
\overline S_i
=
\frac{M_i}{m_i}.
$$

It has the same normalized matrix direction and eigenvalue sign as $M_i$.

However, Miller's criterion uses the pointwise/spatial norm:

$$
\lambda_2^+(S(x,t)),
$$

not

$$
\lambda_2(\overline S_i).
$$

---

# 8. C3-T.2: Mean-to-Pointwise Middle-Eigenvalue No-Go

Take

$$
A
=
\operatorname{diag}(2,-1,-1),
$$

$$
B
=
\operatorname{diag}(-1,2,-1).
$$

Both have

$$
\lambda_2(A)=\lambda_2(B)=-1<0.
$$

But

$$
\frac{A+B}{2}
=
\operatorname{diag}
\left(
\frac12,
\frac12,
-1
\right),
$$

so

$$
\boxed{
\lambda_2
\left(
\frac{A+B}{2}
\right)
=
\frac12>0.
}
$$

Therefore:

$$
\boxed{
\text{mean }\lambda_2>0
\not\Rightarrow
\text{pointwise }\lambda_2>0.
}
$$

---

# 9. Mean-to-Pointwise Upgrade Requires Fluctuation Control

Weyl's inequality gives:

$$
\lambda_2(S(x))
\ge
\lambda_2(\overline S_i)
-
\|S(x)-\overline S_i\|_{\rm op}.
$$

So if

$$
\lambda_2(\overline S_i)>0
$$

and

$$
\boxed{
\|S-\overline S_i\|_{L^\infty(C_i),op}
<
\lambda_2(\overline S_i),
}
$$

then pointwise:

$$
\boxed{
\lambda_2(S(x))>0
}
$$

on the core.

Currently, the ancestry route lacks such a uniform fluctuation theorem.

---

# 10. Cone Degeneration Review

Now take

$$
\gamma_n\to0.
$$

At each scale, there is an at-most-six-core witness

$$
v_{n,i_1},\ldots,v_{n,i_r},
\qquad
r\le6,
$$

with weights

$$
\alpha_j\ge0,
\qquad
\sum_j\alpha_j=1,
$$

such that

$$
\left|
\sum_{j=1}^{r}
\alpha_jv_{n,i_j}
\right|
=
\gamma_n.
$$

---

# 11. Common Pressure Efficiency Bound

For any unit common far-pressure direction

$$
K_H,
$$

at least one core in the witness

$$
i_\ast
$$

satisfies

$$
\boxed{
K_H:v_{n,i_\ast}
\le
\gamma_n.
}
$$

Therefore, if the actual common far matrix is to still have uniform efficiency across all cores

$$
\eta_0>0,
$$

it must be that

$$
\boxed{
\gamma_n\ge\eta_0.
}
$$

Thus,

$$
\boxed{
\gamma_n\to0
}
$$

automatically precludes uniform common-pressure efficiency.

---

# 12. Enstrophy Compensation Route

C3-S has already established:

If the witnesses entirely require a fixed normalized common far-pressure work

$$
b_0>0,
$$

then

$$
\boxed{
\mathfrak E_{R_n}
\gtrsim
b_0^{2/3}
\kappa_n^2
\gamma_n^{-2/3}.
}
$$

Therefore, the pressure-side survivors of cone degeneration are only:

## T-B1 — Enstrophy compensation

$$
\mathfrak E_{R_n}
$$

grows at least at the above rate.

## T-B2 — Pressure-support diversification

At least one witness core is no longer provided fixed support by the common far matrix.

---

# 13. Alternative-Support Lower Bound

Let the normalized required correction/growth demand of a witness core be:

$$
G_i^{req}>0.
$$

Decomposition:

$$
G_i^{req}
=
P_i^{common}
+
A_i^{alt},
$$

where

- $P_i^{common}$ = common far pressure;
- $A_i^{alt}$ = bulk SSA / near pressure / Betchov / projected operator / other channels.

For a weak-pressure core:

$$
P_i^{common}
\le
C
\gamma
\kappa^{-3}
\mathfrak E_R^{3/2}.
$$

Thus:

## Theorem 13.1

If

$$
G_i^{req}\ge g_0>0,
$$

then

$$
\boxed{
A_i^{alt}
\ge
g_0
-
C
\gamma
\kappa^{-3}
\mathfrak E_R^{3/2}.
}
$$

If the common-pressure bound on the right side does not exceed $g_0/2$, then

$$
\boxed{
A_i^{alt}
\ge
\frac12g_0.
}
$$

This is the:

$$
\boxed{
\textbf{Pressure-Support Diversification Lower Bound}.
}
$$

---

# 14. Pressure-Poor Per-Level Witness

Fix a threshold:

$$
\eta_0>0.
$$

A core is called pressure-poor if the common far-pressure efficiency:

$$
\eta_H\le\eta_0.
$$

When

$$
\gamma_n\to0,
$$

under any fixed $\eta_0$,

all sufficiently large scales have at least one pressure-poor witness core.

---

# 15. But Per-Level Witness ≠ Causal Ray

Consider an infinite rooted binary tree.

At depth $n\ge1$, only mark:

$$
\boxed{
0^{n-1}1.
}
$$

Then:

- every depth has a marked node;
- the tree is locally finite;
- but there is no infinite all-marked ray.

Therefore:

## No-Go 15.1

$$
\boxed{
\text{pressure-poor core at every scale}
\not\Rightarrow
\text{existence of a pressure-poor causal ancestry ray}.
}
$$

---

# 16. C3-T.3: Hereditary Pressure-Poor Ray Criterion

Let $\mathcal T$ be a locally finite causal ancestry tree.

Let $\mathcal P$ be the set of pressure-poor nodes.

If there exists $v_0\in\mathcal P$, and every $v\in\mathcal P$ has at least one pressure-poor child,

then there exists an infinite pressure-poor causal ray:

$$
\boxed{
v_0\to v_1\to v_2\to\cdots,
\qquad
v_n\in\mathcal P.
}
$$

More generally, if there exists a fixed $L$ such that every pressure-poor node has a pressure-poor descendant within $1,\ldots,L$ generations,

then there exists a bounded-generation-gap infinite pressure-poor ancestry subsequence.

---

# 17. The Truly Missing Lemma

Therefore, if the degenerate branch is to truly decouple the far-pressure channel,

it requires:

$$
\boxed{
\textbf{Pressure-Poor Heredity Lemma}.
}
$$

Candidate form:

$$
\boxed{
\eta_H(parent)\ll1
+
\text{local source dominance}
\Rightarrow
\exists child:
\eta_H(child)\lesssim
\eta_H(parent)+\varepsilon.
}
$$

or a bounded-generation version.

Currently:

$$
\boxed{\text{OPEN}.}
$$

---

# 18. Why is Pressure-Poor Not Necessarily Hereditary?

The child will change:

- spatial center;
- pressure near/far split;
- far matrix orientation;
- local mean strain;
- merger status;
- local pressure source.

So

$$
\eta_{H,parent}\ll1
$$

does not automatically imply

$$
\eta_{H,child}\ll1.
$$

This is a dynamical geometry gap.

---

# 19. Uniform Cone Motif and Miller Operator Escape

The uniform cone only controls:

$$
M_i
=
\int\chi_iS.
$$

These are five scalar first moments.

But the Miller operator:

$$
\mathcal Q_{SV}
$$

depends on:

- spatial derivatives;
- quadratic fluctuations;
- vorticity;
- advection;
- nonlocal projection.

Therefore, the mean-strain cone cannot generally control operator escape.

---

# 20. C3-T.4: Mean-Motif / Operator-Fluctuation Separation No-Go

The mean map

$$
S
\mapsto
M_\chi(S)
=
\int\chi S\,dx
$$

has only five scalar outputs.

Its kernel

$$
\left\{
W:
\int\chi W\,dx=0
\right\}
$$

is infinite-dimensional.

Thus, one can add oscillatory zero-mean fluctuations while keeping $M_\chi$ unchanged.

These fluctuations can change:

- $\Delta S$;
- $S^2$;
- $\omega$;
- $\mathcal Q_{SV}$;

but do not change the mean-strain cone data.

Therefore:

$$
\boxed{
\text{fixed mean-strain motif}
\not\Rightarrow
\text{small Miller operator defect}.
}
$$

This is an information-level no-go, not an N–S counterexample construction.

---

# 21. Fixed Cone and Operator Escape Can Coexist

So:

$$
\boxed{
\gamma_n\ge\gamma_0
}
$$

and:

$$
\boxed{
d_{SV}(t_n)\gtrsim1
}
$$

are currently completely compatible.

Operator escape can be hidden in:

$$
\boxed{
\text{zero-mean/high-frequency fluctuations around a coherent mean motif}.
}
$$

---

# 22. Fixed Pressure Motif

If the actual common far-pressure directions

$$
K_n^H
$$

also have uniform efficiency,

the compactness of $S^4$ gives a subsequence:

$$
K_n^H\to K_H^\ast.
$$

So the uniform branch can form two fixed matrix motifs:

$$
K_\ast^{cone},
\qquad
K_\ast^{pressure}.
$$

The two need not be identical.

Define the angle:

$$
\vartheta_\ast
=
\arccos
\left(
K_\ast^{pressure}
:
K_\ast^{cone}
\right).
$$

Currently, there is no theorem fixing this angle.

---

# 23. New Subbranches of the Uniform Cone Branch

By the narrow-cone theorem:

## T-C1 — Positive-middle narrow mean motif

$$
\lambda_2(K_\ast)
>
\sqrt{2(1-\gamma_0)}.
$$

All normalized mean strains:

$$
\lambda_2(v_i)>0.
$$

## T-C2 — Negative-middle narrow mean motif

$$
\lambda_2(K_\ast)
<
-\sqrt{2(1-\gamma_0)}.
$$

All normalized mean strains:

$$
\lambda_2(v_i)<0.
$$

## T-C3 — Wide / degenerate motif

The rest.

All three still require pointwise fluctuation control to connect to the Miller criterion.

---

# 24. Mean Fluctuation Ratio

Define:

$$
\boxed{
\mathfrak F_i
=
\frac{
\|S-\overline S_i\|_{L^\infty(C_i),op}
}{
|\overline S_i|
}
}
$$

when $\overline S_i\ne0$.

If the normalized mean has:

$$
\lambda_2
\left(
\frac{\overline S_i}{|\overline S_i|}
\right)
\ge\delta>0
$$

and:

$$
\mathfrak F_i<\delta,
$$

then Weyl's inequality gives:

$$
\boxed{
\lambda_2(S(x))>0
}
$$

on the core.

Currently, there is no uniform theorem giving:

$$
\mathfrak F_i<\delta.
$$

---

# 25. C3-T Survivor Map

## Branch T-U — Uniform cone

$$
\gamma_n\ge\gamma_0.
$$

Remaining debt:

$$
\boxed{
\text{mean-to-pointwise fluctuation}
+
\text{operator fluctuation}.
}
$$

## Branch T-D — Cone degeneration

$$
\gamma_n\to0.
$$

Remaining debt:

$$
\boxed{
\text{enstrophy compensation}
\quad\vee\quad
\text{pressure-support diversification}.
}
$$

To extract a pressure-poor ray,

one also needs:

$$
\boxed{
\text{pressure-poor heredity}.
}
$$

---

# 26. Major No-Gos

### NG-T1

$$
\text{fixed strain half-space}
\Rightarrow
\lambda_2\text{ fixed sign}.
$$

FALSE.

### NG-T2

$$
\text{mean }\lambda_2>0
\Rightarrow
\text{pointwise }\lambda_2>0.
$$

FALSE.

### NG-T3

$$
\text{pressure-poor node every scale}
\Rightarrow
\text{pressure-poor causal ray}.
$$

FALSE.

### NG-T4

$$
\text{fixed mean motif}
\Rightarrow
\text{small Miller operator escape}.
$$

FALSE / information insufficient.

### NG-T5

$$
\gamma\to0
\Rightarrow
\text{far pressure irrelevant}.
$$

FALSE.

Enstrophy can compensate or support can diversify.

---

# 27. X-Integration Guards

## G-MEAN/PT

$$
\boxed{
\text{mean strain}
\neq
\text{pointwise strain}.
}
$$

## G-EIGGAP

If a narrow cone is to deduce the eigenvalue sign,

one must check:

$$
|\lambda_2(K_\ast)|
>
\sqrt{2(1-\gamma)}.
$$

## G-FLUCT

To connect to the pointwise criterion,

preserve:

$$
\mathfrak F_i.
$$

## G-PPOOR

The six-core witness outputs a pressure-poor node,

but it must not be automatically marked as a pressure-poor ancestor for the next generation.

## G-HERED

A pressure-poor causal ray requires hereditary / bounded-gap inheritance.

## G-MEANOP

The mean motif must not be used to control operator fluctuation.

---

# 28. True ETN Update

Uniform branch:

$$
\Theta_n^{motif}
=
\left\langle
K_\ast,
\gamma_0,
\lambda_2(K_\ast),
\{\mathfrak F_i\},
d_{SV},
K_H^\ast,
\operatorname{Prov}
\right\rangle.
$$

Degenerate branch:

$$
\Theta_n^{div}
=
\left\langle
\gamma_n,
\text{six-core witness},
\eta_{\min,n},
\mathfrak E_{R_n},
\text{alternative support},
\operatorname{HereditaryFlag}
\right\rangle.
$$

---

# 29. New Frontier: C3-U

The formal next problem:

$$
\boxed{
\textbf{C3-U — Hereditary Pressure-Poor Ancestry and Mean-to-Pointwise Strain Rigidity}.
}
$$

---

# 30. C3-U Proof Obligations

## U1 — Pressure-poor heredity

Prove or disprove:

$$
\eta_H(parent)\ll1
+
\text{local source dominance}
\Rightarrow
\exists child:
\eta_H(child)\lesssim
\eta_H(parent)+\varepsilon.
$$

## U2 — Bounded-generation heredity

If one-step is too strong,

test:

$$
\exists L<\infty:
\text{poor parent}
\Rightarrow
\text{poor descendant within }L\text{ generations}.
$$

## U3 — Far-pressure matrix transport

Investigate:

$$
H_n\to H_{n+1}
$$

and its scale-invariant variation.

## U4 — Mean-strain transport

Investigate:

$$
M_{parent}\to M_{child}
$$

and its local equation bound.

## U5 — Mean fluctuation control

Find a bound for:

$$
\mathfrak F_i
$$

or prove a no-go.

## U6 — Narrow-cone pointwise branch

Connect cone eigen-gap + fluctuation smallness to the Miller middle-eigenvalue criterion.

## U7 — Operator fluctuation branch

If the fluctuation cannot be small,

convert it into Miller operator escape / critical moment / extra core multiplicity.

## U8 — Pressure-poor ray closure

If U1/U2 succeed,

extract from the cone-degeneration branch:

$$
\boxed{
\text{one causal ancestry ray
with asymptotically weak common far-pressure support}.
}
$$

---

# 31. Formal Status

$$
\boxed{
\begin{aligned}
\text{half-space contains both middle-eigenvalue signatures}
&:\ \mathrm{PROVED},\\
\text{narrow-cone eigenvalue inheritance}
&:\ \mathrm{PROVED},\\
\text{fixed cone}\Rightarrow\lambda_2\text{ sign}
&:\ \mathrm{FALSE\ in\ general},\\
\text{mean }\lambda_2\Rightarrow\text{pointwise }\lambda_2
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{mean-to-pointwise upgrade under fluctuation gap}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\gamma\to0\Rightarrow\text{no uniform common-pressure efficiency}
&:\ \mathrm{PROVED},\\
\text{pressure-support diversification lower bound}
&:\ \mathrm{PROVED},\\
\text{per-level pressure-poor witness}
&:\ \mathrm{PROVED},\\
\text{per-level witness}\Rightarrow\text{pressure-poor ray}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{hereditary pressure-poor ray criterion}
&:\ \mathrm{PROVED\ COMBINATORIAL},\\
\text{pressure-poor heredity for N--S dynamics}
&:\ \mathrm{OPEN},\\
\text{mean motif controls Miller operator escape}
&:\ \mathrm{FALSE/INFORMATION\ NO\mbox{-}GO},\\
\text{mean-to-pointwise / hereditary rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 32. Conclusion

C3-S leaves:

$$
\text{uniform cone}
\quad\vee\quad
\text{cone degeneration}.
$$

C3-T now proves that both branches each have a deeper type gap.

In the uniform cone:

$$
\boxed{
\text{5D half-space coherence}
\not\Rightarrow
\lambda_2^+\text{ geometry}.
}
$$

Only a narrow cone + eigenvalue gap locks the mean sign,

and the mean sign still does not equal the pointwise sign.

In the degenerate branch:

$$
\boxed{
\text{a common-pressure weak core at every scale}
}
$$

does not equal:

$$
\boxed{
\text{the existence of a pressure-poor causal ray}.
}
$$

What is truly missing is heredity.

So the next step is no longer more convex geometry,

but rather:

$$
\boxed{
\textbf{C3-U — Hereditary Pressure-Poor Ancestry and Mean-to-Pointwise Strain Rigidity}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, arXiv:2003.06717.

# Internal dependencies

- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3R_MultiCore_PressureHorizon_StrainConvexity_v0.1.md`
- `NS_C3Q_PressureProjection_OperatorLocalization_v0.1.md`
- `NS_C3P_OperatorEscape_FarPressureMatrix_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-U — Hereditary Pressure-Poor Ancestry and Mean-to-Pointwise Strain Rigidity}
}
$$