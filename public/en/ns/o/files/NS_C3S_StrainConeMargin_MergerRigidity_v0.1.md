---
title: "Navier–Stokes C3-S: Multi-Core Strain-Cone Margin, Six-Core Near-Balance, and Merger Rigidity"
subtitle: "Quantitative Five-Dimensional Strain-Cone Coherence, Six-Core Near-Balance Witnesses, and Enstrophy Debt under Cone Degeneration"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Finite-dimensional convex geometry + previously established pressure/enstrophy estimates + conditional multi-core ancestry interfaces. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-S
# Multi-Core Strain-Cone Margin, Six-Core Near-Balance, and Merger Rigidity

## 0. Current Positioning

C3-R has established three main debts for the multi-core branch:

1. frontier core multiplicity:
   $$
   \mathfrak E_R
   \gtrsim
   m_R\beta_\ast^2;
   $$

2. The pressure provenance of a dense cluster must merge;

3. common far-pressure matrix:
   $$
   H_\ast\in\operatorname{Sym}_0(3)
   \simeq
   \mathbb R^5
   $$
   To positive-support all local mean strains:
   $$
   M_i=\int\chi_iS\,dx,
   $$
   it is required that:
   $$
   0\notin
   \operatorname{conv}\{M_i\}.
   $$

Carathéodory's theorem further gives:

If the origin enters the convex hull,

at most six cores are sufficient to witness the common-pressure obstruction.

This round upgrades this yes/no condition into a **quantitative margin theory**.

Core results:

1. The optimal common strain-cone margin is exactly equal to:
   $$
   \boxed{
   \operatorname{dist}
   \left(
   0,
   \operatorname{conv}
   \left\{
   \frac{M_i}{|M_i|}
   \right\}
   \right);
   }
   $$
2. If this margin is maintained across scales:
   $$
   \gamma_n\ge\gamma_0>0,
   $$
   then one can extract a fixed:
   $$
   K_\ast\in S^4
   $$
   that ultimately separates all multi-core strain directions;
3. Uniform cone coherence is not destroyed by vector cancellation under cluster merger;
4. If:
   $$
   \gamma_n\to0,
   $$
   then at each scale, one can extract at most six cores and convex weights such that the weighted sum of the normalized mean strains is only:
   $$
   O(\gamma_n);
   $$
5. Thus, cone collapse naturally generates a finite six-core near-balance certificate;
6. For any common far-pressure direction, at least one core in this witness has a normalized pressure-support efficiency:
   $$
   \le\gamma_n;
   $$
7. If this weakly supported core still requires a fixed normalized far-pressure work:
   $$
   b_0>0,
   $$
   then:
   $$
   \boxed{
   \mathfrak E_R
   \gtrsim
   b_0^{2/3}
   \kappa^2
   \gamma^{-2/3};
   }
   $$
8. Therefore, strain-cone degeneration is not free:
   $$
   \boxed{
   \text{cone margin}\downarrow0
   \Rightarrow
   \text{pressure-support enstrophy debt}\uparrow\infty;
   }
   $$
9. However, uniform cone coherence itself still does not yield a contradiction;
10. Thus, the next frontier is:
    $$
    \boxed{
    \text{fixed 5D strain-cone motif}
    \quad\text{vs}\quad
    \text{pressure-support diversification}.
    }
    $$

---

# 1. Five-Dimensional Strain Matrix Space

Definition:

$$
\boxed{
\mathbb S_0
=
\operatorname{Sym}_0(3)
=
\left\{
M=M^\top,\ 
\operatorname{tr}M=0
\right\}.
}
$$

Equipped with the Frobenius inner product:

$$
\boxed{
M:N
=
\operatorname{tr}(MN).
}
$$

Then:

$$
\dim\mathbb S_0=5.
$$

Identifying:

$$
\mathbb S_0
$$

with:

$$
\mathbb R^5.
$$

Unit sphere:

$$
\boxed{
S(\mathbb S_0)
=
\{K\in\mathbb S_0:|K|=1\}
\simeq S^4.
}
$$

---

# 2. Multi-Core Local Mean Strains

At the same ancestry / pressure cluster scale:

$$
R,
$$

take cores:

$$
i=1,\ldots,m.
$$

Define:

$$
\boxed{
M_i
=
\int
\chi_iS\,dx
\in\mathbb S_0.
}
$$

Retain only:

$$
M_i\ne0
$$

which are pressure-visible cores.

Define the normalized strain direction:

$$
\boxed{
v_i
=
\frac{M_i}{|M_i|}
\in S^4.
}
$$

Let:

$$
\boxed{
V
=
\{v_1,\ldots,v_m\}.
}
$$

---

# 3. Common Far-Pressure Support

Common far harmonic pressure Hessian:

$$
H\in\mathbb S_0.
$$

Its leading pressure work on core $i$:

$$
\boxed{
B_i^H
=
-H:M_i.
}
$$

If:

$$
H\ne0,
$$

define the pressure support direction:

$$
\boxed{
K_H
=
-\frac{H}{|H|}.
}
$$

Then:

$$
\boxed{
B_i^H
=
|H||M_i|
(K_H:v_i).
}
$$

Therefore:

$$
B_i^H>0
\quad\forall i
$$

is equivalent to:

$$
\boxed{
K_H:v_i>0
\quad\forall i.
}
$$

---

# 4. Optimal Strain-Cone Margin

Define:

$$
\boxed{
\gamma(V)
=
\left[
\max_{|K|=1}
\min_{1\le i\le m}
K:v_i
\right]_+.
}
$$

where:

$$
[x]_+=\max\{x,0\}.
$$

Thus:

$$
0\le\gamma(V)\le1.
$$

---

# 5. C3-S.1: Cone Margin = Convex-Hull Distance

## Theorem 5.1

$$
\boxed{
\gamma(V)
=
\operatorname{dist}
\left(
0,
\operatorname{conv}V
\right).
}
$$

### Proof

Let:

$$
C=\operatorname{conv}V.
$$

---

## Case 1: $0\in C$

For any:

$$
|K|=1,
$$

since:

$$
0
=
\sum_i\alpha_iv_i
$$

for some:

$$
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=1,
$$

we have:

$$
0
=
\sum_i
\alpha_i(K:v_i).
$$

So it is impossible that:

$$
K:v_i>0
$$

for all $i$.

Therefore:

$$
\max_{|K|=1}\min_iK:v_i
\le0.
$$

Hence:

$$
\gamma(V)=0.
$$

And:

$$
\operatorname{dist}(0,C)=0.
$$

---

## Case 2: $0\notin C$

Let:

$$
y_\ast\in C
$$

be the point closest to the origin:

$$
|y_\ast|
=
d
=
\operatorname{dist}(0,C)>0.
$$

The convex projection theorem gives:

$$
(v-y_\ast):y_\ast
\ge0
\qquad
\forall v\in C.
$$

Take:

$$
K_\ast
=
\frac{y_\ast}{|y_\ast|}.
$$

Then:

$$
K_\ast:v
\ge
|y_\ast|
=
d
$$

for all:

$$
v\in C.
$$

In particular:

$$
\min_iK_\ast:v_i
\ge d.
$$

Thus:

$$
\gamma(V)\ge d.
$$

Conversely, if some unit $K$ satisfies:

$$
K:v_i\ge a>0
$$

for all $i$,

then:

$$
K:y\ge a
$$

for all:

$$
y\in C.
$$

Hence:

$$
|y|\ge a.
$$

Thus:

$$
d\ge a.
$$

Taking the supremum over $K$:

$$
d\ge\gamma(V).
$$

Hence:

$$
\gamma(V)=d.
$$

$\square$

---

# 6. Geometric Semantics

Therefore:

$$
\boxed{
\gamma(V)>0
}
$$

if and only if all normalized mean strains lie in some common open half-space.

And:

$$
\boxed{
\gamma(V)
}
$$

is exactly the Euclidean distance from the origin to their convex hull.

Thus, pressure coherence is upgraded from:

$$
\boxed{
\text{YES/NO}
}
$$

to:

$$
\boxed{
\text{quantitative five-dimensional margin}.
}
$$

---

# 7. Actual Pressure Efficiency

For an actual common far matrix:

$$
H\ne0,
$$

define:

$$
\boxed{
\eta_H(V)
=
\min_i
\frac{-H:M_i}{|H||M_i|}
=
\min_i
K_H:v_i.
}
$$

If:

$$
\eta_H>0,
$$

the actual far matrix positive-supports all cores.

By optimality:

$$
\boxed{
\eta_H(V)
\le
\gamma(V).
}
$$

Therefore:

$$
\boxed{
\text{actual common-pressure margin}
\le
\text{best possible strain-cone margin}.
}
$$

---

# 8. Cross-Scale Cone Family

Consider ancestry scales:

$$
n=1,2,\ldots.
$$

Each scale has a normalized core set:

$$
\boxed{
V_n
=
\{v_{n,1},\ldots,v_{n,m_n}\}
\subset S^4.
}
$$

Define:

$$
\boxed{
\gamma_n
=
\gamma(V_n).
}
$$

Now there are only two asymptotic branches:

## S-A — Uniform Cone Coherence

$$
\boxed{
\liminf_{n\to\infty}
\gamma_n
>
0.
}
$$

## S-B — Cone Degeneration

$$
\boxed{
\gamma_n\to0
}
$$

along some subsequence.

---

# 9. C3-S.2: Cross-Scale Separator Compactness

## Theorem 9.1

If:

$$
\gamma_n\ge\gamma_0>0
$$

for all sufficiently large $n$,

then there exists a subsequence:

$$
n_k
$$

and a fixed unit matrix:

$$
\boxed{
K_\ast\in S^4
}
$$

such that:

$$
\boxed{
K_\ast:v_{n_k,i}
\ge
\frac{\gamma_0}{2}
}
$$

for all sufficiently large $k$ and all:

$$
i=1,\ldots,m_{n_k}.
$$

### Proof

For each $n$, take the maximizer:

$$
K_n\in S^4
$$

satisfying:

$$
K_n:v_{n,i}
\ge
\gamma_n
\ge
\gamma_0
$$

for all $i$.

Since:

$$
S^4
$$

is compact,

we can extract a subsequence:

$$
K_{n_k}\to K_\ast.
$$

When:

$$
|K_{n_k}-K_\ast|
\le\gamma_0/2,
$$

since:

$$
|v_{n_k,i}|=1,
$$

we have:

$$
K_\ast:v_{n_k,i}
\ge
K_{n_k}:v_{n_k,i}
-
|K_\ast-K_{n_k}|
\ge
\gamma_0/2.
$$

$\square$

---

# 10. Cross-Scale Fixed Strain Cone

Therefore, the uniform-margin branch forces:

$$
\boxed{
\text{all late-stage multi-core mean strains to fall into a fixed 5D spherical cap}.
}
$$

The cone half-angle is at most:

$$
\boxed{
\arccos(\gamma_0/2).
}
$$

This document refers to this as the:

$$
\boxed{
\textbf{Cross-Scale Strain-Cone Fixed Motif}.
}
$$

This is a relation-level compactness result,

not full velocity/strain field compactness.

---

# 11. Actual Far-Pressure Direction Compactness

If the actual matrices:

$$
H_n\ne0
$$

satisfy a uniform support efficiency:

$$
\boxed{
\eta_{H_n}(V_n)
\ge
\eta_0>0,
}
$$

define:

$$
K_n^H
=
-\frac{H_n}{|H_n|}.
$$

The compactness of:

$$
S^4
$$

gives a subsequence:

$$
K_n^H\to K_\ast^H.
$$

Similarly:

$$
\boxed{
K_\ast^H:v_{n,i}
\ge
\eta_0/2
}
$$

for all late-stage cores.

Thus, if the common far pressure maintains a uniform fractional efficiency across scales,

the pressure-matrix orientation itself can form a:

$$
\boxed{
\textbf{renormalized 5D matrix motif}.
}
$$

---

# 12. Merger

Fix a common separator:

$$
K,
\qquad
|K|=1,
$$

such that:

$$
\boxed{
K:M_i
\ge
\gamma|M_i|
}
$$

for all $i$,

where:

$$
\gamma>0.
$$

Define the merged mean strain:

$$
\boxed{
M_{\rm merge}
=
\sum_{i=1}^{m}
M_i.
}
$$

---

# 13. C3-S.3: Cone Inheritance under Merger

## Theorem 13.1

$$
\boxed{
|M_{\rm merge}|
\ge
\gamma
\sum_i|M_i|.
}
$$

And:

$$
\boxed{
K:
\frac{M_{\rm merge}}{|M_{\rm merge}|}
\ge
\gamma.
}
$$

### Proof

$$
K:M_{\rm merge}
=
\sum_iK:M_i
\ge
\gamma
\sum_i|M_i|.
$$

And:

$$
K:M_{\rm merge}
\le
|M_{\rm merge}|.
$$

Hence:

$$
|M_{\rm merge}|
\ge
\gamma
\sum_i|M_i|.
$$

Also:

$$
|M_{\rm merge}|
\le
\sum_i|M_i|,
$$

Therefore:

$$
K:
\frac{M_{\rm merge}}{|M_{\rm merge}|}
=
\frac{
K:M_{\rm merge}
}{
|M_{\rm merge}|
}
\ge
\gamma.
$$

$\square$

---

# 14. Merger Rigidity

Therefore, in the uniform cone coherence branch,

dense cluster merge will not wipe out the mean strain through vector cancellation.

Instead:

$$
\boxed{
\text{coherent fine-scale mean strains}
\Rightarrow
\text{coherent coarse merged mean strain}.
}
$$

Thus, the pressure-provenance merge rule is compatible with strain-cone coherence:

$$
\boxed{
\text{merge preserves cone margin}.
}
$$

---

# 15. Pressure Work is Additive under Common Matrix

If the same:

$$
H
$$

acts on all cores,

then:

$$
B_i^H=-H:M_i.
$$

Therefore:

$$
\boxed{
B_{\rm merge}^H
=
-H:M_{\rm merge}
=
\sum_i
B_i^H.
}
$$

Under a common support cone:

$$
B_i^H>0
$$

Thus, the merger will not vanish due to pressure-work sign cancellation.

---

# 16. Normalized Core Mean Magnitude

Define:

$$
\boxed{
\mu_i
=
\frac{
|M_i|
}{
\nu R
}.
}
$$

For an $R$-scale core, this is the scale-invariant mean-strain size.

If all pressure-relevant cores satisfy:

$$
\boxed{
\mu_i\ge\mu_0>0,
}
$$

uniform cone coherence can also provide a local strain-stock lower bound.

---

# 17. C3-S.4: Merger Strain-Stock Lower Bound

Assume:

1. Core cutoffs have uniformly bounded overlap;
2. Union volume:
   $$
   |U|
   \le
   C
   mR^3;
   $$
3. Common cone margin:
   $$
   K:M_i
   \ge
   \gamma|M_i|;
   $$
4. Each:
   $$
   \mu_i\ge\mu_0.
   $$

Then:

$$
\boxed{
\frac{
R
}{
\nu^2
}
\int_U
|S|^2dx
\ge
c
\gamma^2
\mu_0^2
m.
}
$$

### Proof

By the merger theorem:

$$
|M_{\rm merge}|
\ge
\gamma
\sum_i|M_i|
\ge
\gamma
m
\mu_0
\nu R.
$$

On the other hand, bounded-overlap Cauchy gives:

$$
|M_{\rm merge}|^2
\le
C
|U|
\int_U|S|^2.
$$

Therefore:

$$
\int_U|S|^2
\ge
c
\frac{
\gamma^2
m^2
\mu_0^2
\nu^2R^2
}{
mR^3
}
=
c
\gamma^2
\mu_0^2
\nu^2
\frac mR.
$$

Multiply by:

$$
R/\nu^2.
$$

$\square$

---

# 18. Dense Cluster Scale

If:

$$
L\sim m^{1/3}R,
$$

then the cluster-scale normalized strain stock:

$$
\boxed{
\mathfrak S_L
=
\frac{
L
}{
\nu^2
}
\int_U|S|^2
}
$$

satisfies:

$$
\boxed{
\mathfrak S_L
\gtrsim
\gamma^2
\mu_0^2
m^{4/3}.
}
$$

Therefore, uniform strain-cone coherence + significant mean strain will amplify the dense-merger strain stock,

rather than canceling it out during the merge.

---

# 19. Cone Degeneration Branch

Now assume:

$$
\boxed{
\gamma(V)\ll1.
}
$$

By Theorem 5.1:

$$
\gamma(V)
=
\operatorname{dist}
(0,\operatorname{conv}V).
$$

Let the closest convex point:

$$
y_\ast\in\operatorname{conv}V
$$

satisfy:

$$
|y_\ast|
=
\gamma(V).
$$

---

# 20. C3-S.5: Six-Core Near-Balance Witness

## Theorem 20.1

There exist:

$$
r\le6
$$

normalized core strains:

$$
v_{i_1},\ldots,v_{i_r}
$$

and weights:

$$
\alpha_j\ge0,
\qquad
\sum_{j=1}^{r}\alpha_j=1,
$$

such that:

$$
\boxed{
\left|
\sum_{j=1}^{r}
\alpha_j
v_{i_j}
\right|
=
\gamma(V).
}
$$

### Proof

The closest point:

$$
y_\ast
$$

belongs to:

$$
\operatorname{conv}V
\subset\mathbb R^5.
$$

Carathéodory's theorem gives that:

$$
y_\ast
$$

can be represented by a convex combination of at most:

$$
5+1=6
$$

points.

And:

$$
|y_\ast|=\gamma(V).
$$

$\square$

---

# 21. Exact Obstruction as a Special Case

If:

$$
\gamma(V)=0,
$$

we obtain:

$$
\boxed{
\sum_{j=1}^{r}
\alpha_jv_{i_j}
=
0
}
$$

for:

$$
r\le6.
$$

This recovers the six-core pressure obstruction of C3-R.

---

# 22. C3-S.6: Robust Six-Core Margin Obstruction

## Theorem 22.1

Take the witness from Theorem 20.1.

For any unit pressure direction:

$$
K\in S^4,
$$

there exists at least one:

$$
j\in\{1,\ldots,r\}
$$

such that:

$$
\boxed{
K:v_{i_j}
\le
\gamma(V).
}
$$

### Proof

If all:

$$
K:v_{i_j}
>
\gamma(V),
$$

then:

$$
K:
\sum_j\alpha_jv_{i_j}
>
\gamma(V).
$$

But:

$$
\left|
K:
\sum_j\alpha_jv_{i_j}
\right|
\le
\left|
\sum_j\alpha_jv_{i_j}
\right|
=
\gamma(V),
$$

Contradiction. $\square$

---

# 23. Significance

Therefore, when:

$$
\gamma(V)\to0,
$$

it is not only the optimal common support that deteriorates.

Stronger:

$$
\boxed{
\text{Any common far-pressure matrix direction}
}
$$

must encounter, within an at-most-six-core witness, at least one:

$$
\boxed{
\text{normalized support efficiency}\le\gamma.
}
$$

This is a completely finite certificate.

---

# 24. Normalized Far-Pressure Work

Following C3-Q.

Define:

$$
\boxed{
\widehat H
=
\frac{
R^4
}{
\nu^2
}
H,
}
$$

$$
\boxed{
\widehat M_i
=
\frac{
M_i
}{
\nu R
},
}
$$

and the normalized pressure work:

$$
\boxed{
\widehat B_i^H
=
-\widehat H:\widehat M_i.
}
$$

If:

$$
\widehat H\ne0,
\quad
\widehat M_i\ne0,
$$

then:

$$
\boxed{
\widehat B_i^H
=
|\widehat H|
|\widehat M_i|
\eta_i,
}
$$

where:

$$
\eta_i
=
-\frac{
\widehat H:\widehat M_i
}{
|\widehat H|
|\widehat M_i|
}.
$$

---

# 25. Pressure Magnitude Bound

For a pressure source outside:

$$
\kappa R
$$

,

C3-Q gives:

$$
\boxed{
|\widehat H|
\le
C
\kappa^{-3}
\mathfrak E_R,
}
$$

where:

$$
\boxed{
\mathfrak E_R
=
\frac{
R\|\nabla u\|_2^2
}{
\nu^2
}.
}
$$

---

# 26. Mean Strain Magnitude Bound

For an $R$-scale core:

$$
|M_i|
\le
C
R^{3/2}
\|S\|_{L^2(B_{CR})}.
$$

Therefore:

$$
|\widehat M_i|
=
\frac{
|M_i|
}{
\nu R
}
\le
C
\left(
\frac{
R
}{
\nu^2
}
\|S\|_2^2
\right)^{1/2}.
$$

Thus:

$$
\boxed{
|\widehat M_i|
\le
C
\mathfrak E_R^{1/2}.
}
$$

---

# 27. C3-S.7: Cone-Degeneration Pressure Debt

## Theorem 27.1

Assume:

1. Multi-core cone margin:
   $$
   \gamma=\gamma(V)>0;
   $$
2. Common far matrix:
   $$
   H
   $$
   originates from outside:
   $$
   \kappa R
   $$
   ;
3. Each core in the six-core witness requires:
   $$
   \boxed{
   \widehat B_i^H
   \ge
   b_0>0.
   }
   $$

Then:

$$
\boxed{
\mathfrak E_R
\ge
c
b_0^{2/3}
\kappa^2
\gamma^{-2/3}.
}
$$

### Proof

By the robust six-core theorem,

for the actual pressure direction:

$$
K_H=-H/|H|,
$$

at least one core in the witness:

$$
i_\ast
$$

satisfies:

$$
\eta_{i_\ast}
\le
\gamma.
$$

And:

$$
b_0
\le
\widehat B_{i_\ast}^H
=
|\widehat H|
|\widehat M_{i_\ast}|
\eta_{i_\ast}.
$$

Therefore:

$$
b_0
\le
\gamma
|\widehat H|
|\widehat M_{i_\ast}|.
$$

Using:

$$
|\widehat H|
\le
C
\kappa^{-3}
\mathfrak E_R,
$$

and:

$$
|\widehat M_{i_\ast}|
\le
C
\mathfrak E_R^{1/2},
$$

we obtain:

$$
b_0
\le
C
\gamma
\kappa^{-3}
\mathfrak E_R^{3/2}.
$$

Rearranging:

$$
\mathfrak E_R^{3/2}
\ge
c
b_0
\kappa^3
\gamma^{-1}.
$$

Taking the:

$$
2/3
$$

power:

$$
\boxed{
\mathfrak E_R
\ge
c
b_0^{2/3}
\kappa^2
\gamma^{-2/3}.
}
$$

$\square$

---

# 28. This is Stronger than the Far-Pressure Debt of C3-Q

C3-Q only has:

$$
\boxed{
\mathfrak E_R
\gtrsim
b_0^{2/3}
\kappa^2.
}
$$

After incorporating multi-core cone degeneration, C3-S becomes:

$$
\boxed{
\mathfrak E_R
\gtrsim
b_0^{2/3}
\kappa^2
\gamma^{-2/3}.
}
$$

Therefore:

$$
\boxed{
\gamma\downarrow0
}
$$

will additionally force:

$$
\boxed{
\mathfrak E_R\uparrow\infty.
}
$$

This document refers to this as the:

$$
\boxed{
\textbf{Cone-Degeneration Pressure Debt}.
}
$$

---

# 29. Pressure-Support Diversification

Theorem 27.1 has a contrapositive-style research reading.

If:

$$
\mathfrak E_R
$$

is insufficient to pay the:

$$
\gamma^{-2/3}
$$

debt,

then at least one core in the six-core witness cannot be provided with fixed normalized pressure support by the same far matrix.

Thus, the growth / dynamics of that core must rely more on:

- near pressure;
- bulk SSA;
- local Betchov current;
- projected operator escape;
- other pressure matrix sources.

This document refers to this as:

$$
\boxed{
\textbf{Pressure-Support Diversification}.
}
$$

---

# 30. Cross-Scale Coherence / Degeneration Dichotomy

Therefore, every subsequence of the multi-core strain geometry ultimately falls into:

## Branch S-A — Uniform Cone Motif

$$
\boxed{
\gamma_n\ge\gamma_0>0.
}
$$

Then:

- a fixed separator:
  $$
  K_\ast
  $$
  emerges;
- merger preserves the cone;
- the common pressure direction can compactify across scales;
- mean-strain cancellation is suppressed.

## Branch S-B — Cone Degeneration

$$
\boxed{
\gamma_n\to0.
}
$$

Then:

- an at-most-six-core near-balance witness;
- common pressure efficiency for at least one core:
  $$
  \le\gamma_n;
  $$
- fixed pressure work forces:
  $$
  \mathfrak E_{R_n}
  \gtrsim
  \kappa_n^2
  \gamma_n^{-2/3};
  $$
- otherwise, pressure support must diversify.

---

# 31. Uniform Cone Branch is Still Not a Contradiction

Take an abstract sequence:

$$
v_{n,i}=K_\ast
$$

for all:

$$
n,i.
$$

Then:

$$
\boxed{
\gamma_n=1.
}
$$

The merger is completely coherent.

At the same time, as long as the ordinary energy cost per core is:

$$
\sim R_n,
$$

one can still keep:

$$
m_nR_n
$$

bounded.

Therefore:

$$
\boxed{
\text{perfect 5D strain-cone coherence}
}
$$

does not contradict finite kinetic energy scaling.

This is an important no-go.

---

# 32. Cone Coherence Does Not Equal Common Eigenframe

The condition:

$$
K_\ast:M_i
\ge
\gamma|M_i|
$$

only restricts the Frobenius angle in:

$$
\mathbb S_0\simeq\mathbb R^5
$$

.

It does not imply:

- $M_i$ commute;
- identical eigenvectors;
- identical eigenvalue ordering;
- $\lambda_2(M_i)>0$;
- consistent vorticity alignment.

Therefore:

$$
\boxed{
\text{5D matrix-cone coherence}
\neq
\text{eigenframe coherence}.
}
$$

This is the next level of type distinction.

---

# 33. Cone Coherence Does Not Equal Middle-Strain Positivity

The open half-space:

$$
\{M:K_\ast:M>0\}
$$

typically simultaneously contains:

- two-positive-eigenvalue matrices;
- one-positive-eigenvalue matrices;
- near-degenerate matrices.

Therefore:

$$
\boxed{
K_\ast:M>0
}
$$

cannot replace:

$$
\boxed{
\lambda_2^+(M)>0.
}
$$

Thus, the middle-eigenvalue channel of C3-L/M must still be preserved independently.

---

# 34. Type-I Interface

The Barker–Prange quantitative Type-I theory, under the:

$$
L_t^\infty L_x^{3,\infty}
$$

bound, can control the terminal singular-point number.

But in this round:

$$
V_n
$$

are transient pressure/frontier core strain directions.

Therefore, the Type-I terminal count cannot directly rule out:

- the uniform cone branch;
- six-core transient witnesses;
- repeated mergers.

It can only be used after the branch-to-terminal mapping is established.

---

# 35. X-Integration Guards Update

## G-CMARGIN

Preserve:

$$
\boxed{
\gamma(V)
=
\operatorname{dist}(0,\operatorname{conv}V).
}
$$

## G-SEPARATOR

The uniform margin branch preserves:

$$
K_n\to K_\ast.
$$

## G-MERGE-CONE

Cluster merge must not delete the no-cancellation lower bound brought by:

$$
K:M_i\ge\gamma|M_i|
$$

.

## G-6NEAR

Cone degeneration must output an at-most-six-core certificate:

$$
\left|
\sum\alpha_iv_i
\right|
=
\gamma
$$

.

## G-PEFF

The common pressure actual efficiency:

$$
\eta_H
$$

must not be replaced by the optimal:

$$
\gamma
$$

.

Only the following can be used:

$$
\eta_H\le\gamma.
$$

## G-CDEBT

Fixed pressure support + small $\gamma$ must pay:

$$
\mathfrak E_R
\gtrsim
\kappa^2\gamma^{-2/3}.
$$

## G-EIGTYPE

Matrix-cone coherence cannot be upgraded to eigenframe/middle-eigenvalue coherence.

---

# 36. True ETN Update

The multi-core strain geometry can now be written as:

$$
\boxed{
\Theta_n^{cone}
=
\left\langle
V_n,
\gamma_n,
K_n,
K_\ast,
\text{six-core witness},
\mathfrak E_{R_n},
\kappa_n,
\operatorname{Prov}
\right\rangle.
}
$$

Its primary transition is:

$$
\boxed{
\text{uniform-margin fixed motif}
\quad\vee\quad
\text{degenerate six-core pressure debt}.
}
$$

This preserves more multi-scale information than the binary:

$$
0\in\operatorname{conv}V
\ ?
$$

.

---

# 37. Main No-Gos of This Round

### NG-S1

$$
\gamma_n\ge\gamma_0
\Rightarrow
\text{regularity}.
$$

FALSE.

### NG-S2

$$
\gamma_n\to0
\Rightarrow
\text{common far pressure is completely impossible}.
$$

FALSE.

It can compensate for the small directional efficiency by:

$$
\mathfrak E_R
\to\infty
$$

.

### NG-S3

$$
K_\ast\text{ fixed}
\Rightarrow
\text{common strain eigenframe}.
$$

FALSE.

### NG-S4

$$
\text{six-core near-balance}
\Rightarrow
\text{all six cores cannot grow}.
$$

FALSE.

It only restricts the common far-pressure support channel.

### NG-S5

$$
\dim\mathbb S_0=5
\Rightarrow
\text{at most five coherent cores}.
$$

FALSE.

---

# 38. New Frontier: C3-T

C3-S has compressed the multi-core pressure geometry into:

$$
\boxed{
\text{fixed strain-cone motif}
}
$$

or:

$$
\boxed{
\text{six-core degeneration + pressure/enstrophy debt}.
}
$$

The formal next problem is:

$$
\boxed{
\textbf{C3-T — Pressure-Support Diversification and Strain-Cone Fixed-Motif Rigidity}.
}
$$

---

# 39. C3-T Proof Obligations

## T1 — Fixed Cone vs Middle Eigenvalue

In the uniform:

$$
K_\ast
$$

cone,

investigate whether the:

$$
\lambda_2^+
$$

critical divergence can persist long-term without forcing eigenframe concentration.

## T2 — Fixed Cone vs Operator Escape

Add the local mean strains of Miller operator-active cores to:

$$
V_n.
$$

Determine whether:

$$
d_{SV}\gtrsim1
$$

forces the strain directions to leave the fixed cone or increases the cone width.

## T3 — Degenerate Six-Core Selection

When:

$$
\gamma_n\to0,
$$

use the six-core witness to select the core with the lowest common far-pressure efficiency.

Track whether it can form a:

$$
\boxed{
\text{pressure-poor causal ancestry}.
}
$$

across scales.

## T4 — Pressure-Poor Core Alternative

If this core still positive-grows,

it must be supported more by:

- bulk SSA;
- near pressure;
- local Betchov current;
- projected operator;

.

Establish a finite alternative list.

## T5 — Cone-Debt Iteration

If a fixed far-pressure work is maintained at each scale:

$$
b_0,
$$

iterate:

$$
\mathfrak E_{R_n}
\gtrsim
\kappa_n^2
\gamma_n^{-2/3}.
$$

Investigate whether it forms a new packing contradiction with:

- C3-K active worldvolume;
- C3-L critical moment;
- viscous-window timing;

.

## T6 — Merger Tree Cone Inheritance

In the uniform cone branch,

prove that the coarse strain direction of each dense merge still falls within the:

$$
K_\ast
$$

cone.

Establish a cross-scale merger tree.

## T7 — Eigenframe Entropy

Cone coherence is only in $\mathbb R^5$.

Define a local strain eigenframe dispersion measure,

to test whether it can remain completely rotationally chaotic within the fixed cone.

## T8 — Common Pressure Motif

If the actual:

$$
H_n/|H_n|
\to H_\ast,
$$

compare:

$$
H_\ast
$$

with:

- $K_\ast$;
- middle eigenvectors;
- vorticity direction;
- operator model gap.

---

# 40. Formal Status

$$
\boxed{
\begin{aligned}
\gamma(V)=\operatorname{dist}(0,\operatorname{conv}V)
&:\ \mathrm{PROVED},\\
\text{uniform margin}\Rightarrow\text{fixed cross-scale separator}
&:\ \mathrm{PROVED},\\
\text{actual pressure uniform efficiency}\Rightarrow\text{pressure-direction motif}
&:\ \mathrm{PROVED},\\
\text{cone inheritance under merger}
&:\ \mathrm{PROVED},\\
\text{merger mean-strain no-cancellation}
&:\ \mathrm{PROVED},\\
\text{conditional merger strain-stock lower bound}
&:\ \mathrm{PROVED},\\
\text{six-core near-balance witness}
&:\ \mathrm{PROVED},\\
\text{robust six-core margin obstruction}
&:\ \mathrm{PROVED},\\
\text{cone-degeneration pressure debt}
&:\ \mathrm{PROVED},\\
\text{uniform cone coherence}\Rightarrow\text{regularity}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{cone coherence}\Rightarrow\text{common eigenframe}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{cone degeneration forces pressure support diversification unless enstrophy grows}
&:\ \mathrm{PROVED/STRUCTURAL},\\
\text{fixed motif vs operator/middle-strain rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 41. Conclusion

The common-pressure criterion of C3-R was originally:

$$
0
\notin
\operatorname{conv}\{M_i\}.
$$

C3-S now upgrades it into an exact quantitative quantity:

$$
\boxed{
\gamma(V)
=
\operatorname{dist}
\left(
0,
\operatorname{conv}
\left\{
\frac{M_i}{|M_i|}
\right\}
\right).
}
$$

Thus, the multi-core branch has only two truly distinct asymptotic geometries.

---

## Uniform-Margin Branch

$$
\gamma_n\ge\gamma_0>0.
$$

Then one can extract:

$$
\boxed{
K_\ast\in S^4
}
$$

such that all late-stage core mean strains remain in the same fixed 5D cone.

Moreover, merger will not cancel out this coherence:

$$
\boxed{
|M_{\rm merge}|
\ge
\gamma_0
\sum_i|M_i|.
}
$$

Therefore:

$$
\boxed{
\text{Strain-cone coherence can be inherited across scales}.
}
$$

---

## Degenerate Branch

$$
\gamma_n\to0.
$$

Then each scale has an at-most-six-core witness:

$$
\boxed{
\left|
\sum_{j\le6}
\alpha_jv_j
\right|
=
\gamma_n.
}
$$

For any common far-pressure direction,

the normalized support efficiency of at least one core is:

$$
\le\gamma_n.
$$

If it still requires a fixed pressure work:

$$
b_0>0,
$$

then:

$$
\boxed{
\mathfrak E_{R_n}
\gtrsim
b_0^{2/3}
\kappa_n^2
\gamma_n^{-2/3}.
}
$$

Therefore:

$$
\boxed{
\text{cone collapse}
\Rightarrow
\text{pressure-support cost diverges}
}
$$

unless far pressure is no longer the primary support channel for that core.

This generates true:

$$
\boxed{
\textbf{pressure-support diversification}.
}
$$

However, uniform cone coherence itself can still survive in scaling,

so there is no global contradiction in this round yet.

The next round:

$$
\boxed{
\textbf{C3-T — Pressure-Support Diversification and Strain-Cone Fixed-Motif Rigidity}
}
$$

will truly test:

> whether a fixed 5D strain-cone direction can coexist long-term with middle-strain divergence, helical ancestry, and Miller operator escape;  
> or, if the cone collapses, whether one can repeatedly select a pressure-poor causal ancestry along the six-core witness to truly strip the far-pressure channel away from the survivor.

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
2. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
3. T. Barker, C. Prange, *Quantitative regularity for the Navier–Stokes equations via spatial concentration*, arXiv:2003.06717.
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.

# Internal Dependencies

- `NS_C3R_MultiCore_PressureHorizon_StrainConvexity_v0.1.md`
- `NS_C3Q_PressureProjection_OperatorLocalization_v0.1.md`
- `NS_C3P_OperatorEscape_FarPressureMatrix_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-T — Pressure-Support Diversification and Strain-Cone Fixed-Motif Rigidity}
}
$$