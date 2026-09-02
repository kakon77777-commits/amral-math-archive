---
title: "Navier–Stokes C5-D: Spatial–Matrix Motif Compatibility, Strong-Middle Cones, and Quadratic/Pressure Convex-Hull Obstructions"
subtitle: "A Finite-Dimensional Incompatibility between Positive-Middle Strain Coherence, Seven-Point Quadratic Cancellation, and Common Far-Pressure Compensation"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style spatial–matrix compatibility / first finite-dimensional recurrent-limit obstruction"
epistemic_status: "Exact finite-dimensional matrix algebra + conditional pointwise-cone interface + adjoint pressure ledger + convex-hull obstruction. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-D
# Spatial–Matrix Motif Compatibility, Strong-Middle Cones, and Quadratic/Pressure Convex-Hull Obstructions

## 0. Current Positioning

C5-A established:

$$
\boxed{
\text{compensation-motif compactness}.
}
$$

C5-B established:

$$
\boxed{
\text{Young phase oscillation / load concentration defects}.
}
$$

C5-C further proved:

$$
\boxed{
\text{operator temporal phase}
=
\text{strain-dissipation-demand curvature source},
}
$$

but simultaneously proved:

$$
\boxed{
\textbf{scalar temporal identities alone still allow a separated compensation cycle}.
}
$$

Therefore, C5-D officially departs from the pure temporal scalar route,

placing the following objects into the same finite-dimensional spatial–matrix problem:

1. positive-middle strain direction;
2. local quadratic tensor:
   $$
   Q
   =
   S^2
   +
   \frac14\omega\otimes\omega
   -
   \frac14|\omega|^2I;
   $$
3. C4-J Seven-Point quadratic cancellation witness;
4. local adjoint pressure mean;
5. common harmonic far-pressure matrix;
6. C3-S convex-hull pressure geometry.

This round yields C5's first true:

$$
\boxed{
\textbf{finite-dimensional recurrent-limit incompatibility}.
}
$$

Core result:

> If pointwise strain directions persistently fall within a sufficiently narrow cone where the normalized middle eigenvalue is strictly positive, then all local quadratic tensors $Q$ automatically fall into the same strict matrix half-space, **without requiring any vorticity alignment or vorticity/strain ratio assumptions.**

Thus:

$$
\boxed{
\text{Strong-Middle Pointwise Cone}
\Rightarrow
\text{Quadratic Coherence}
}
$$

While:

$$
\boxed{
\text{Seven-Point Zero-Barycenter Cancellation}
}
$$

is incompatible with it.

---

# 1. Fresh primary-source audit

External anchors for this round:

## 1.1 Miller — middle strain geometry

Miller's strain formulation and middle-eigenvalue regularity criterion proved that:

$$
\boxed{
\lambda_2^+
}
$$

is a scale-critical regularity channel,

and the strain constraint space:

$$
L^2_{st}
$$

and its orthogonal complement have substantial significance for N–S strain evolution.

## 1.2 Miller — strain/vorticity interaction

The latest strain-vorticity work proved:

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0,
}
$$

and placed the strain/vorticity quadratic interaction and advection depletion into the operator architecture.

This round does not directly use its regularity theorem to prove the matrix cone,

but uses its strain/vorticity decomposition to confirm that:

$$
S^2,
\qquad
\omega\otimes\omega
$$

are the true local quadratic constituents of the full N–S.

## 1.3 Bradshaw–Tsai — local pressure expansion

The whole-space N–S pressure possesses a rigorous local expansion,

where the near-field Calderón–Zygmund part and the far-field contribution can be legitimately tracked separately.

Therefore, C5-D's local pressure / common far-pressure matrix architecture has PDE provenance.

---

# 2. Local quadratic tensor

Definition:

$$
\boxed{
Q(S,\omega)
=
S^2
+
\frac14
\omega\otimes\omega
-
\frac14
|\omega|^2I.
}
$$

Where:

$$
S=S^T,
\qquad
\operatorname{tr}S=0.
$$

Note:

$$
Q\in\operatorname{Sym}(3),
$$

In general:

$$
\operatorname{tr}Q
\ne0.
$$

The pressure Hessian complements the trace / constraint complement in the full strain equation.

---

# 3. Normalized positive-middle strain direction

Take:

$$
\boxed{
K\in\operatorname{Sym}_0(3),
\qquad
|K|_F=1.
}
$$

ordered eigenvalues:

$$
\boxed{
k_1<k_2\le k_3,
}
$$

and assume:

$$
\boxed{
k_2>0.
}
$$

Due to being trace-free:

$$
k_1=-(k_2+k_3)<0.
$$

Let:

$$
\boxed{
e_1
}
$$

be the unit eigenvector of $k_1$.

---

# 4. Strong-middle shape parameter

Definition:

$$
\boxed{
\theta_K
=
k_2k_3.
}
$$

From:

$$
|K|_F^2
=
k_1^2+k_2^2+k_3^2
=
1
$$

and:

$$
k_1=-(k_2+k_3),
$$

we have:

$$
\boxed{
k_1^2-\frac12
=
k_2k_3
=
\theta_K.
}
$$

Since:

$$
k_2,k_3>0,
$$

therefore:

$$
\boxed{
\theta_K>0.
}
$$

### Interpretation

$\theta_K$ quantifies how far the normalized strain shape is from the degenerate boundary of:

$$
\lambda_2=0
$$

If:

$$
k_2\downarrow0,
$$

then:

$$
\theta_K\downarrow0.
$$

---

# 5. Compressive-axis test tensor

Definition:

$$
\boxed{
P_1
=
e_1\otimes e_1.
}
$$

and:

$$
\boxed{
H_K
=
P_1
-
\frac{
1+\theta_K
}{
2
}
I.
}
$$

Its trace:

$$
\boxed{
\operatorname{tr}H_K
=
-\frac{
1+3\theta_K
}{
2
}.
}
$$

---

# 6. Vorticity positivity identity

Calculate:

$$
\boxed{
H_K
-
(\operatorname{tr}H_K)I
=
P_1+\theta_KI.
}
$$

Thus:

$$
\boxed{
H_K:
\left[
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\right]
=
\frac14
\omega\cdot
(P_1+\theta_KI)
\omega.
}
$$

Therefore, for any:

$$
\omega\in\mathbb R^3,
$$

we have:

$$
\boxed{
H_K:
\left[
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\right]
\ge
\frac{
\theta_K
}{
4
}
|\omega|^2.
}
$$

### Key Point

Does not require:

- vorticity alignment;
- vorticity magnitude upper bound;
- helicity sign.

---

# 7. Strain-square positivity at cone center

Since:

$$
P_1:K^2
=
k_1^2,
$$

$$
I:K^2
=
|K|_F^2
=
1,
$$

therefore:

$$
H_K:K^2
=
k_1^2
-
\frac{
1+\theta_K
}{
2
}.
$$

Using:

$$
k_1^2
=
\frac12+\theta_K,
$$

we obtain:

$$
\boxed{
H_K:K^2
=
\frac{
\theta_K
}{
2
}.
}
$$

---

# 8. Nearby strain directions

Take normalized:

$$
V\in\operatorname{Sym}_0(3),
\qquad
|V|_F=1.
$$

If:

$$
|V-K|_F
\le
\delta,
$$

then:

$$
V^2-K^2
=
(V-K)V
+
K(V-K).
$$

Thus:

$$
\boxed{
|V^2-K^2|_F
\le
2\delta.
}
$$

Therefore:

$$
\boxed{
H_K:V^2
\ge
\frac{
\theta_K
}{2}
-
2
|H_K|_F
\delta.
}
$$

---

# 9. Strong-middle cone radius

Definition:

$$
\boxed{
\delta_K
=
\frac{
\theta_K
}{
8|H_K|_F
}.
}
$$

If:

$$
\boxed{
|V-K|_F
\le
\delta_K,
}
$$

then:

$$
\boxed{
H_K:V^2
\ge
\frac{
\theta_K
}{
4
}.
}
$$

This document refers to:

$$
\boxed{
\mathcal C_K
=
\{
V\in\operatorname{Sym}_0(3):
|V|_F=1,\ 
|V-K|_F\le\delta_K
\}
}
$$

as:

$$
\boxed{
\textbf{Strong-Middle Pointwise Strain Cone}.
}
$$

---

# 10. C5-D.1: Positive-Middle Cone → Quadratic Half-Space Theorem

## Theorem 10.1

Suppose:

$$
S\ne0,
$$

and:

$$
\boxed{
\frac{
S
}{
|S|_F
}
\in
\mathcal C_K.
}
$$

Then for any:

$$
\omega\in\mathbb R^3,
$$

we have:

$$
\boxed{
H_K:
Q(S,\omega)
\ge
\frac{
\theta_K
}{
4
}
\left(
|S|_F^2
+
|\omega|^2
\right).
}
$$

If:

$$
S=0,
$$

the same inequality still holds.

### Proof

If:

$$
S=sV,
\qquad
s=|S|_F,
$$

then by §9:

$$
H_K:S^2
=
s^2
H_K:V^2
\ge
\frac{
\theta_K
}{4}
|S|^2.
$$

Adding the vorticity lower bound from §6 completes the proof. $\square$

---

# 11. Uniform half-space margin relative to $|Q|$

We have:

$$
|S^2|_F
\le
|S|_F^2.
$$

Additionally:

$$
\left|
\omega\otimes\omega
-
|\omega|^2I
\right|_F
=
\sqrt2
|\omega|^2.
$$

Therefore:

$$
\boxed{
|Q|_F
\le
|S|^2
+
\frac{\sqrt2}{4}
|\omega|^2
\le
|S|^2+|\omega|^2.
}
$$

Thus, C5-D.1 gives:

$$
\boxed{
H_K:Q
\ge
\frac{
\theta_K
}{4}
|Q|.
}
$$

---

# 12. Unit half-space functional

Definition:

$$
\boxed{
\widehat H_K
=
\frac{
H_K
}{
|H_K|_F
}.
}
$$

and margin:

$$
\boxed{
\gamma_K
=
\frac{
\theta_K
}{
4|H_K|_F
}
>0.
}
$$

Then:

$$
\boxed{
\widehat H_K:
\frac{
Q
}{
|Q|
}
\ge
\gamma_K
}
$$

whenever:

$$
Q\ne0
$$

and the strain direction lies in:

$$
\mathcal C_K.
$$

---

# 13. First finite-dimensional consequence

All normalized quadratic directions:

$$
U
=
Q/|Q|
$$

fall into the strict half-space:

$$
\boxed{
\mathcal H_K^+
=
\{
U\in S^5:
\widehat H_K:U
\ge
\gamma_K
\}.
}
$$

Therefore:

$$
\boxed{
0
\notin
\operatorname{conv}
(
\mathcal H_K^+
).
}
$$

Stronger:

$$
\boxed{
\operatorname{dist}
\left(
0,
\operatorname{conv}
\mathcal H_K^+
\right)
\ge
\gamma_K.
}
$$

---

# 14. Weighted local quadratic mean

Take:

$$
\chi\ge0.
$$

Definition:

$$
\boxed{
A_\chi^Q
=
\int
\chi|Q|dx,
}
$$

$$
\boxed{
B_\chi^Q
=
\int
\chi Qdx.
}
$$

If:

$$
A_\chi^Q>0,
$$

coherence:

$$
\boxed{
\kappa_\chi^Q
=
\frac{
|B_\chi^Q|
}{
A_\chi^Q
}.
}
$$

---

# 15. C5-D.2: Strong-Middle Cone Forces Quadratic Coherence

If all nonzero strain directions in the $\chi$-relevant region satisfy:

$$
S/|S|
\in
\mathcal C_K,
$$

then:

$$
\widehat H_K:B_\chi^Q
=
\int
\chi
\widehat H_K:Q
dx
\ge
\gamma_K
A_\chi^Q.
$$

Therefore:

$$
\boxed{
\kappa_\chi^Q
\ge
\gamma_K.
}
$$

### Conclusion

$$
\boxed{
\textbf{Strong-Middle Pointwise Cone}
\Rightarrow
\textbf{nondegenerate local quadratic mean coherence}.
}
$$

---

# 16. C5-D.3: Seven-Point Zero-Barycenter Incompatibility

If the cancellation motif of C4-J has:

$$
\kappa_j^Q\to0,
$$

we can extract the Seven-Point limit:

$$
\boxed{
\sum_{i=1}^{7}
\alpha_i^\ast
U_i^\ast
=
0.
}
$$

But if simultaneously:

$$
U_i^\ast
\in
\mathcal H_K^+
$$

for all:

$$
i,
$$

then:

$$
\widehat H_K:
\sum_i
\alpha_i^\ast U_i^\ast
\ge
\gamma_K
\sum_i\alpha_i^\ast
=
\gamma_K>0.
$$

Contradiction.

Therefore:

$$
\boxed{
\textbf{Strong-Middle Cone}
\quad\text{and}\quad
\textbf{Seven-Point Zero-Barycenter Cancellation}
}
$$

cannot coexist in the same recurrent limit.

---

# 17. This is C5's first true finite-dimensional incompatibility

The compactification of C5-A/B/C itself only yielded:

- limit states;
- defect measures;
- transition constraints.

C5-D.3 yields for the first time:

$$
\boxed{
\textbf{algebraic mutual exclusion of two recurrent limit motifs}.
}
$$

This is not a matter of:

- norm divergence;
- integral budget;
- temporal packing.

It is purely a:

$$
\boxed{
\textbf{finite-dimensional convex geometry obstruction}.
}
$$

---

# 18. Approximate cone leakage

In reality, pointwise strain may not entirely lie within the cone.

Define the good set:

$$
\boxed{
G_K
=
\left\{
x:
S(x)=0
\text{ or }
S(x)/|S(x)|
\in
\mathcal C_K
\right\}.
}
$$

Define the quadratic-mass leakage fraction:

$$
\boxed{
\varepsilon_\chi^K
=
\frac{
\int_{\mathbb R^3\setminus G_K}
\chi|Q|dx
}{
A_\chi^Q
}
}
$$

when:

$$
A_\chi^Q>0.
$$

---

# 19. C5-D.4: Quantitative Cone-Leakage / Cancellation Theorem

In the good region:

$$
\widehat H_K:Q
\ge
\gamma_K|Q|.
$$

In the bad region, we only have:

$$
\widehat H_K:Q
\ge
-|Q|.
$$

Therefore:

$$
\widehat H_K:B_\chi^Q
\ge
\left[
\gamma_K
(
1-\varepsilon_\chi^K
)
-
\varepsilon_\chi^K
\right]
A_\chi^Q.
$$

That is:

$$
\boxed{
\kappa_\chi^Q
\ge
\left[
\gamma_K
-
(
1+\gamma_K
)
\varepsilon_\chi^K
\right]_+.
}
$$

---

# 20. Cancellation forces cone leakage

If:

$$
\kappa_\chi^Q
\le
\kappa_0
<
\gamma_K,
$$

then:

$$
\boxed{
\varepsilon_\chi^K
\ge
\frac{
\gamma_K-\kappa_0
}{
1+\gamma_K
}.
}
$$

In particular:

If:

$$
\kappa_j^Q\to0,
$$

and:

$$
K_j\to K
$$

with:

$$
\lambda_2(K)>0,
$$

then:

$$
\boxed{
\liminf_j
\varepsilon_{\chi_j}^{K_j}
\ge
\frac{
\gamma_K
}{
1+\gamma_K
}
>0
}
$$

as long as the cone margins remain nondegenerate.

### Interpretation

For quadratic cancellation to survive,

a fixed fraction of the local quadratic mass must be borne by:

$$
\boxed{
\textbf{strain directions outside the strong-middle cone}
}
$$

---

# 21. Recurrent-limit dichotomy

Therefore, if:

$$
\kappa_j^Q\to0,
$$

it is only possible that:

## D-Q1 — Middle-gap degeneration

$$
\boxed{
\theta_{K_j}
=
\lambda_2(K_j)\lambda_3(K_j)
\to0.
}
$$

Or:

## D-Q2 — Strain-direction dispersion

$$
\boxed{
\varepsilon_{\chi_j}^{K_j}
\not\to0.
}
$$

That is:

$$
\boxed{
\textbf{Q cancellation}
\Rightarrow
\textbf{normalized middle-gap degeneration}
\vee
\textbf{pointwise strain-direction leakage}.
}
$$

---

# 22. Meaning of middle-gap degeneration

Since:

$$
|K_j|_F=1,
$$

If:

$$
\theta_{K_j}\to0
$$

and:

$$
\lambda_3(K_j)>0,
$$

then:

$$
\boxed{
\lambda_2(K_j)\to0.
}
$$

Therefore, the normalized strain shape approaches:

the degenerate boundary of:

$$
\boxed{
\lambda_2=0
}
$$

schematically:

$$
(-1/\sqrt2,0,1/\sqrt2).
$$

This is the:

$$
\boxed{
\textbf{Middle-Gap Degeneration Motif}.
}
$$

It is not that the middle-strain positivity itself disappears,

but rather that:

$$
\lambda_2^+
$$

becomes too small relative to the full strain amplitude.

---

# 23. Mean strain is not pointwise strain

The:

$$
\boxed{
\text{strain cone}
}
$$

of C3-S primarily acts on the local mean matrices:

$$
M_i
$$

or:

$$
\bar S_R.
$$

The cone in C5-D.1–4, however, is a:

$$
\boxed{
\textbf{pointwise normalized strain-direction cone}.
}
$$

The two must not be confused.

Therefore:

$$
\boxed{
\text{mean-strain cone}
\not\Rightarrow
\text{C5-D pointwise cone}
}
$$

without fluctuation control.

---

# 24. Mean-to-pointwise interface

Let:

$$
\boxed{
\bar S_R
=
\frac1{
\int\chi
}
\int
\chi Sdx.
}
$$

Assume:

$$
\bar S_R\ne0.
$$

Definition:

$$
\boxed{
m_R
=
|\bar S_R|_F,
}
$$

$$
\boxed{
K_R
=
\frac{
\bar S_R
}{
m_R
}.
}
$$

---

# 25. Relative strain fluctuation

Definition:

$$
\boxed{
\eta_R^S
=
\frac{
\|S-\bar S_R\|_{L^\infty(\operatorname{supp}\chi)}
}{
|\bar S_R|
}.
}
$$

If:

$$
\eta_R^S<1,
$$

then:

$$
S=m_R(K_R+E),
$$

$$
|E|\le\eta_R^S.
$$

---

# 26. Direction perturbation bound

If:

$$
V
=
\frac{
K+E
}{
|K+E|
},
$$

$$
|K|=1,
$$

$$
|E|\le\eta<1,
$$

then:

$$
\boxed{
|V-K|
\le
\frac{
2\eta
}{
1-\eta
}.
}
$$

Therefore, if:

$$
\boxed{
\eta_R^S
\le
\eta_{K_R}^{crit}
:=
\frac{
\delta_{K_R}
}{
2+\delta_{K_R}
},
}
$$

then:

$$
\boxed{
S(x)/|S(x)|
\in
\mathcal C_{K_R}
}
$$

through the core.

---

# 27. C5-D.5: Mean-Coherence Excludes Quadratic Cancellation

If:

1. the normalized mean direction:
   $$
   K_R
   $$
   satisfies:
   $$
   \lambda_2(K_R)>0;
   $$

2. the relative fluctuation:
   $$
   \eta_R^S
   \le
   \eta_{K_R}^{crit};
   $$

then:

$$
\boxed{
\kappa_\chi^Q
\ge
\gamma_{K_R}
>0.
}
$$

Therefore:

$$
\boxed{
\textbf{Seven-Point quadratic cancellation is impossible on that core}.
}
$$

---

# 28. Cancellation forces strain fluctuation

Conversely,

If:

$$
\kappa_\chi^Q
<
\gamma_{K_R},
$$

then:

$$
\boxed{
\eta_R^S
>
\eta_{K_R}^{crit}
}
$$

or the normalized middle gap has already degenerated enough to make:

$$
\gamma_{K_R}
$$

small.

Therefore:

$$
\boxed{
\textbf{Quadratic cancellation}
\Rightarrow
\textbf{strain fluctuation / middle-gap debt}.
}
$$

---

# 29. Morrey derivative bridge

If:

$$
p>3,
$$

the Morrey/Poincaré estimate gives:

$$
\boxed{
\|S-\bar S_R\|_{L^\infty(B_R)}
\le
C_p
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}
}
$$

up to cutoff/ball constants.

Thus, if cancellation requires:

$$
\eta_R^S
\ge
\eta_0>0,
$$

then:

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p(B_R)}
\ge
c_p
\eta_0
|\bar S_R|.
}
$$

### Conclusion

If Seven-Point cancellation does not take the middle-gap degeneration route,

it must pay a:

$$
\boxed{
\textbf{higher-derivative strain-fluctuation debt}.
}
$$

This directly connects back to:

- C3-V fluctuation/intermittency;
- C3-W/X/Y derivative geometry.

---

# 30. Quadratic intensity under cone coherence

C5-D.1 also gives:

$$
H_K:Q
\ge
\frac{
\theta_K
}{4}
|S|^2.
$$

Therefore:

$$
|Q|
\ge
\frac{
\theta_K
}{
4|H_K|
}
|S|^2
=
\gamma_K|S|^2.
$$

Thus:

$$
\boxed{
A_\chi^Q
\ge
\gamma_K
\int
\chi|S|^2dx.
}
$$

---

# 31. Mean strain forces quadratic intensity

By Jensen's inequality:

$$
\int
\chi|S|^2dx
\ge
\left(
\int\chi
\right)
|\bar S_R|^2.
$$

If:

$$
c_\chi R^3
\le
\int\chi
\le
C_\chi R^3,
$$

then:

$$
\boxed{
A_\chi^Q
\ge
c_\chi
\gamma_K
R^3
|\bar S_R|^2.
}
$$

Define the mean-strain critical amplitude:

$$
\boxed{
\mu_R
=
\frac{
R^2
|\bar S_R|
}{
\nu
}.
}
$$

Then:

$$
\boxed{
a_\chi^Q
=
\frac{
R
}{
\nu^2
}
A_\chi^Q
\ge
c_\chi
\gamma_K
\mu_R^2.
}
$$

Therefore, if a strong-middle coherent mean core has:

$$
\mu_R\gtrsim1,
$$

the local quadratic intensity is automatically nondegenerate.

---

# 32. Local pressure re-entry

Adjoint mean strain:

$$
\boxed{
M_\chi'
=
-B_\chi^Q-P_\chi,
}
$$

where:

$$
\boxed{
P_\chi
=
\int
\chi\nabla^2pdx.
}
$$

Under cone coherence:

$$
\boxed{
\widehat H_K:B_\chi^Q
\ge
\gamma_K
A_\chi^Q.
}
$$

---

# 33. C5-D.6: Oriented Pressure Re-entry Theorem

Assume:

$$
\boxed{
|M_\chi'|
\le
\varepsilon
A_\chi^Q,
}
$$

where:

$$
0\le
\varepsilon
<
\gamma_K.
$$

From:

$$
P_\chi
=
-M_\chi'
-
B_\chi^Q,
$$

we have:

$$
-\widehat H_K:P_\chi
=
\widehat H_K:B_\chi^Q
+
\widehat H_K:M_\chi'.
$$

Therefore:

$$
\boxed{
-\widehat H_K:P_\chi
\ge
(
\gamma_K-\varepsilon
)
A_\chi^Q.
}
$$

Thus:

$$
\boxed{
|P_\chi|
\ge
(
\gamma_K-\varepsilon
)
A_\chi^Q.
}
$$

---

# 34. Critical pressure oscillation

C4-I / C3-X local Hessian estimate:

$$
\boxed{
|P_\chi|
\le
C
R^{-1}
\inf_{\ell\in\mathcal A_1}
\|
p-\ell
\|_{L^{3/2}(B_{CR})}.
}
$$

Therefore:

$$
\boxed{
\Pi_R^{(2)}
=
\nu^{-2}
\inf_{\ell\in\mathcal A_1}
\|
p-\ell
\|_{L^{3/2}(B_{CR})}
\ge
c
\frac{
R
}{
\nu^2
}
|P_\chi|.
}
$$

Combining with §33:

$$
\boxed{
\Pi_R^{(2)}
\ge
c
(
\gamma_K-\varepsilon
)
a_\chi^Q.
}
$$

If we further use §31:

$$
\boxed{
\Pi_R^{(2)}
\ge
c
(
\gamma_K-\varepsilon
)
\gamma_K
\mu_R^2.
}
$$

---

# 35. C5-D.7: Strong-Middle Coherent Core Forces Pressure or Mean Rotation

If:

1. the normalized mean direction:
   $$
   K_R
   $$
   has a uniform:
   $$
   \lambda_2(K_R)>0;
   $$

2. the pointwise fluctuation is small enough to enter:
   $$
   \mathcal C_{K_R};
   $$

3. the mean-strain amplitude:
   $$
   \mu_R\ge\mu_0>0;
   $$

then at least:

## D-MROT

$$
\boxed{
\frac{
R
}{
\nu^2
}
|M_\chi'|
\ge
c
\gamma_{K_R}
\mu_0^2,
}
$$

Or:

## D-PRESS

$$
\boxed{
\Pi_R^{(2)}
\ge
c
\gamma_{K_R}^2
\mu_0^2.
}
$$

### Key Point

The quadratic-cancellation branch has been excluded by the strong-middle pointwise cone,

so the trichotomy of C4-I:

$$
\text{Cancellation}
\vee
\text{Mean Rotation}
\vee
\text{Pressure}
$$

is reduced here to:

$$
\boxed{
\text{Mean Rotation}
\vee
\text{Pressure Concentration}.
}
$$

---

# 36. Far harmonic pressure

The Bradshaw–Tsai local pressure expansion allows for local / far pressure provenance.

For pressure sources sufficiently far from the core,

the far pressure inside the core is harmonic,

and its Hessian can be expanded in a small core as:

$$
\boxed{
\nabla^2p_{far}(x)
=
F
+
\text{higher spatial remainder},
}
$$

where the leading constant matrix:

$$
\boxed{
F\in\operatorname{Sym}_0(3)
}
$$

Due to harmonicity:

$$
\operatorname{tr}F=0.
$$

This is the far-pressure matrix architecture of C3-Q/S.

---

# 37. Trace-free part of the cone functional

$H_K$ itself is not trace-free.

But for:

$$
F\in\operatorname{Sym}_0(3),
$$

only:

$$
H_K^0
=
H_K
-
\frac13
(\operatorname{tr}H_K)I
$$

has an effect.

Direct calculation:

$$
\boxed{
H_K^0
=
P_1
-
\frac13I.
}
$$

Surprisingly:

$$
\boxed{
H_K^0
}
$$

is independent of:

$$
\theta_K
$$

It only depends on:

$$
\boxed{
\textbf{the most-compressive eigenvector }e_1.
}
$$

---

# 38. Compressive-axis projector

Definition:

$$
\boxed{
G(e)
=
e\otimes e
-
\frac13I
\in
\operatorname{Sym}_0(3).
}
$$

Therefore, for a harmonic far-pressure matrix:

$$
F,
$$

$$
\boxed{
H_K:F
=
G(e_1):F.
}
$$

---

# 39. Multi-core common-pressure setting

Consider cores:

$$
i=1,\ldots,m.
$$

Each core has:

- a strong-middle cone center:
  $$
  K_i;
  $$
- a compressive axis:
  $$
  e_i;
  $$
- local quadratic forcing;
- depleted mean rotation;
- the same dominant far harmonic pressure matrix:
  $$
  F_\ast\in\operatorname{Sym}_0(3).
  $$

After absorbing local/far remainders,

suppose each core requires:

$$
\boxed{
G(e_i):F_\ast
\le
-c_i,
\qquad
c_i>0.
}
$$

---

# 40. C5-D.8: Compressive-Axis Convex-Hull Pressure Obstruction

## Theorem 40.1

If:

$$
\boxed{
0
\in
\operatorname{conv}
\{
G(e_1),\ldots,G(e_m)
\},
}
$$

then there do not exist:

$$
F_\ast\in\operatorname{Sym}_0(3)
$$

and:

$$
c_i>0
$$

that simultaneously satisfy:

$$
G(e_i):F_\ast
\le
-c_i
$$

for all:

$$
i.
$$

### Proof

There exist:

$$
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=1,
$$

such that:

$$
\sum_i
\alpha_i
G(e_i)
=
0.
$$

Multiplying by:

$$
F_\ast
$$

:

$$
0
=
\sum_i
\alpha_i
G(e_i):F_\ast
\le
-
\sum_i
\alpha_ic_i
<0.
$$

Contradiction. $\square$

---

# 41. Six-core witness

Since:

$$
\operatorname{Sym}_0(3)
\simeq
\mathbb R^5,
$$

Carathéodory's theorem gives:

If:

$$
0
\in
\operatorname{conv}
\{
G(e_i)
\}_{i\in I},
$$

then there already exist:

$$
\boxed{
\le6
}
$$

compressive axes as witnesses.

Therefore:

$$
\boxed{
\textbf{Six-Core Compressive-Axis Pressure Obstruction}.
}
$$

This lies in the same dimension-five convex geometry as the Six-Core Pressure Obstruction of C3-S,

but the witness objects are different:

- C3-S: mean strain matrices;
- C5-D: compressive-axis STF projectors.

---

# 42. Orthogonal-triplet obstruction

If:

$$
e_1,e_2,e_3
$$

is an orthonormal basis,

then:

$$
\sum_{i=1}^{3}
e_i\otimes e_i
=
I.
$$

Thus:

$$
\boxed{
G(e_1)+G(e_2)+G(e_3)
=
0.
}
$$

Therefore, only:

$$
\boxed{
3
}
$$

mutually orthogonal compressive axes are needed,

to already have:

$$
\boxed{
0
\in
\operatorname{conv}
\{
G(e_1),G(e_2),G(e_3)
\}.
}
$$

### C5-D.9: Orthogonal-Triplet Pressure Obstruction

If three strong-middle coherent cores:

1. have mutually orthogonal compressive axes;
2. have depleted mean rotation;
3. require simultaneous compensation from the same dominant harmonic far-pressure matrix;

then it is impossible.

---

# 43. Meaning for pressure compensation

If a common far pressure is to support many strong-middle coherent cores,

it cannot allow the compressive axes in the:

$$
\operatorname{Sym}_0(3)
$$

projector space to excessively "surround the origin".

Therefore, persistent common-pressure compensation requires:

$$
\boxed{
0
\notin
\operatorname{conv}
\{
G(e_i)
\}.
}
$$

Equivalently, there exists some:

$$
F
$$

such that:

$$
\boxed{
G(e_i):F
}
$$

have a common sign.

This is a form of:

$$
\boxed{
\textbf{Compressive-Axis Cone Coherence}.
}
$$

---

# 44. C5-D pressure escape classification

If strong-middle pointwise coherence recurrently exists,

for pressure to still avoid contradiction,

it must at least take:

## D-P1 — Mean-rotation escape

$$
\boxed{
M_\chi'
\text{ remains large}.
}
$$

## D-P2 — Pressure locality/source fragmentation

different cores can no longer be dominated by the same far harmonic matrix.

## D-P3 — Compressive-axis directional locking

$$
\boxed{
0
\notin
\operatorname{conv}
\{G(e_i)\}.
}
$$

## D-P4 — Strong-middle cone failure

strain direction disperses / middle gap degenerates.

## D-P5 — Pressure concentration

pressure local oscillation itself enters the critical branch.

---

# 45. A C5 limit formulation

For each recurrent core,

define the normalized strain-direction measure:

$$
\boxed{
\nu_j^S
}
$$

on:

$$
S^4
\subset
\operatorname{Sym}_0(3)
$$

using a selected local quadratic or strain-energy weight.

Define the quadratic-direction measure:

$$
\boxed{
\nu_j^Q
}
$$

on:

$$
S^5
\subset
\operatorname{Sym}(3)
$$

with:

$$
\chi|Q|
$$

weight.

---

# 46. Strong-middle support condition

If:

$$
\nu_j^S
$$

concentrates in:

$$
\mathcal C_K,
$$

then C5-D.1 gives the support constraint:

$$
\boxed{
\operatorname{supp}
\nu_j^Q
\subset
\mathcal H_K^+.
}
$$

hence any weak limit:

$$
\nu_\ast^Q
$$

also satisfies:

$$
\boxed{
\operatorname{supp}
\nu_\ast^Q
\subset
\mathcal H_K^+.
}
$$

---

# 47. C5-D.10: Limit Barycenter Incompatibility

If:

$$
\nu_\ast^S
$$

is supported inside one nondegenerate strong-middle cone:

$$
\mathcal C_K,
$$

then:

$$
\boxed{
\left|
\int
U
d\nu_\ast^Q(U)
\right|
\ge
\gamma_K.
}
$$

Therefore:

$$
\boxed{
\int
U
d\nu_\ast^Q(U)
=
0
}
$$

is impossible.

### Conclusion

$$
\boxed{
\textbf{Q-cancellation limit}
}
$$

and:

$$
\boxed{
\textbf{single strong-middle strain-cone limit}
}
$$

are mutually exclusive.

---

# 48. Recurrent limit escape

If:

$$
\int U\,d\nu_j^Q
\to0,
$$

then any recurrent strain-direction limit must:

$$
\boxed{
\text{not be confined to a single positive-middle strong cone}
}
$$

unless:

$$
\boxed{
\theta_K\to0.
}
$$

Therefore:

$$
\boxed{
\textbf{Quadratic zero-barycenter}
\Rightarrow
\textbf{middle-gap degeneration}
\vee
\textbf{strain-direction mixing}.
}
$$

---

# 49. Relation to temporal motifs

C5-C has proved:

scalar temporal dynamics allow:

$$
O^+\to M
$$

separated compensation cycle.

C5-D now states:

Even if the temporal ordering is valid,

if the Q-cancellation phase therein is to compensate for pressure,

its spatial/matrix state cannot simultaneously maintain a:

$$
\boxed{
\text{single strong-middle cone}.
}
$$

Therefore, the recurrent temporal cycle must carry new spatial metadata:

$$
\boxed{
\text{directional dispersion}
\vee
\text{middle-gap degeneration}.
}
$$

This is the first true closure of temporal→spatial compatibility.

---

# 50. Middle record toll and strong-middle cone are still different

C4-H only has a:

$$
\boxed{
\int
\lambda_2^+
|S|^2
}
$$

record-window toll.

It does not guarantee:

$$
\boxed{
\lambda_2(S)/|S|
\ge c_0
}
$$

pointwise.

Therefore, the C5-D theorem cannot be directly initiated from the C4-H middle toll.

The truly newly added gate is:

$$
\boxed{
\textbf{normalized strong-middle shape}.
}
$$

---

# 51. Strong-middle shape variable

For:

$$
S\ne0,
$$

Definition:

$$
\boxed{
\vartheta(S)
=
\frac{
\lambda_2^+(S)
\lambda_3(S)
}{
|S|_F^2
}.
}
$$

If the normalized direction:

$$
K=S/|S|,
$$

then:

$$
\boxed{
\vartheta(S)
=
\theta_K.
}
$$

Therefore:

$$
\boxed{
\vartheta>0
}
$$

is precisely the pointwise margin source of the C5-D half-space mechanism.

---

# 52. C5-D survivor trichotomy for Q motif

If Seven-Point Q-cancellation is recurrently active,

then at least:

## D-QGAP

$$
\boxed{
\vartheta
\to0
}
$$

on substantial quadratic mass;

Or:

## D-QMIX

$$
\boxed{
\text{strain-direction cone leakage}
}
$$

carries substantial quadratic mass;

Or:

## D-QDER

if the mean direction remains coherent,

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p}
/
|\bar S_R|
\gtrsim1.
}
$$

which means derivative fluctuation.

---

# 53. What C5-D has really eliminated

C4-J residual:

$$
\boxed{
Q
=
\text{Seven-Point Quadratic Cancellation}
}
$$

originally appeared to be a completely independent finite-dimensional compensator.

C5-D now proves:

$$
\boxed{
Q
}
$$

cannot coexist with:

$$
\boxed{
\text{strong-middle pointwise coherence}
}
$$

Therefore, Q is not a free compact motif.

It must synchronize with:

$$
\boxed{
\text{Middle-Gap Degeneration}
\vee
\text{Strain-Direction Dispersion / Derivative Fluctuation}.
}
$$

---

# 54. Pressure geometry new bridge

At the same time,

if strong-middle pointwise coherence holds,

the Q cancellation branch disappears.

Thus, local pressure avoidance is left only with:

$$
\boxed{
\text{Mean Rotation}
\vee
\text{Pressure}.
}
$$

If multiple cores further share the same far harmonic pressure,

the pressure branch is again subjected to the compressive-axis coherence requirement of:

$$
\boxed{
0
\notin
\operatorname{conv}
\{
e_i\otimes e_i-I/3
\}
}
$$

Therefore:

$$
\boxed{
\textbf{pressure compensation itself produces a recurrent
axis-cone geometry}.
}
$$

---

# 55. C5-D first incompatibility cycle

Currently, we can write:

$$
\boxed{
\begin{aligned}
&\text{Strong-Middle Pointwise Cone}\\
&\qquad\Downarrow\\
&\text{Quadratic Half-Space}\\
&\qquad\Downarrow\\
&\text{No Seven-Point Cancellation}\\
&\qquad\Downarrow\\
&\text{Mean Rotation}\vee\text{Pressure Re-entry}\\
&\qquad\Downarrow\\
&\text{if common far pressure: Compressive-Axis Convex-Hull Constraint}.
\end{aligned}
}
$$

And in the reverse direction:

$$
\boxed{
\text{Q Cancellation}
\Rightarrow
\text{Middle-Gap Degeneration}
\vee
\text{Direction Dispersion}.
}
$$

This is C5's first true:

$$
\boxed{
\textbf{spatial–matrix compatibility cycle}.
}
$$

---

# 56. Major no-go audit

### NG-D1

$$
\text{middle-strain record toll}
\Rightarrow
\text{strong-middle pointwise cone}.
$$

FALSE / not proved.

### NG-D2

$$
\text{mean-strain cone}
\Rightarrow
\text{pointwise strain cone}.
$$

FALSE without fluctuation control.

### NG-D3

$$
\text{positive-middle cone requires vorticity alignment}.
$$

FALSE.

C5-D test tensor handles arbitrary $\omega$.

### NG-D4

$$
\text{Q cancellation can coexist with uniform strong-middle pointwise cone}.
$$

FALSE.

### NG-D5

$$
\text{pressure re-entry}
\Rightarrow
\text{one common far-pressure matrix}.
$$

FALSE.

local/source-specific pressure may dominate.

### NG-D6

$$
\text{compressive-axis convex hull contains origin}
\Rightarrow
\text{pressure singularity contradiction}.
$$

FALSE.

It only obstructs one common far-pressure compensation matrix.

---

# 57. X-Integration guards update

## G-SCONEPT

The mean cone and the pointwise normalized strain cone must be separated.

## G-SMARGIN

The strong-middle cone preserves:

$$
\theta_K
=
\lambda_2(K)\lambda_3(K).
$$

## G-QHALF

Quadratic directions must preserve the half-space functional:

$$
H_K.
$$

## G-QLEAK

Approximate cancellation must record the cone-leakage fraction:

$$
\varepsilon_\chi^K.
$$

## G-MIDGAP

$\theta_K\to0$ is a valid boundary escape,

and must not be misjudged as a cone theorem contradiction.

## G-PAXIS

The pairing between far pressure and:

$$
G(e_1)
=
e_1\otimes e_1-I/3
$$

must be preserved.

## G-FARCOMMON

The multi-core pressure obstruction can only be used after common far-matrix dominance is proved.

---

# 58. True ETN update

C5-D spatial–matrix state:

$$
\boxed{
\Theta_\ast^{SM}
=
\left\langle
\nu_\ast^S,
\nu_\ast^Q,
\theta_\ast,
\gamma_\ast,
\varepsilon_\ast^{cone},
\mathcal U_\ast^{(7)},
\mu_\ast^R,
\Pi_\ast^{(2)},
\mathcal G_\ast^{axis}
\right\rangle.
}
$$

Where:

- $\nu_\ast^S$ = normalized strain-direction measure;
- $\nu_\ast^Q$ = quadratic-direction measure;
- $\theta_\ast$ = strong-middle shape margin;
- $\varepsilon^{cone}$ = Q-weighted cone leakage;
- $\mathcal U^{(7)}$ = Seven-Point witness;
- $\mu^R$ = mean-rotation metadata;
- $\mathcal G^{axis}$ = compressive-axis STF projector configuration.

---

# 59. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal Young / concentration defects}.
$$

C5-C:

$$
\text{temporal transition / curvature constraints}.
$$

C5-D:

$$
\boxed{
\textbf{first finite-dimensional recurrent-limit incompatibility}.
}
$$

Specifically:

$$
\boxed{
\text{Strong-Middle Cone}
\cap
\text{Seven-Point Zero-Barycenter}
=
\varnothing.
}
$$

While common far-pressure compensation is further subjected to:

$$
\boxed{
\text{compressive-axis convex-hull obstruction}.
}
$$

---

# 60. New frontier: C5-E

C5-D ultimately leaves three spatial escapes:

$$
\boxed{
\text{Middle-Gap Degeneration}
}
$$

$$
\boxed{
\text{Strain-Direction Dispersion / Derivative Fluctuation}
}
$$

$$
\boxed{
\text{Pressure Locality / Axis Locking / Mean Rotation}.
}
$$

Therefore, the official next topic is:

$$
\boxed{
\textbf{C5-E — Strain-Direction Defect Measures,
Middle-Gap Degeneration, and Derivative-Intermittency Closure}.
}
$$

---

# 61. C5-E proof obligations

## E1 — Strain-direction probability measure

Using:

$$
\chi|Q|
$$

or strain energy as the weight,

establish the exact compactification and strong-middle support spectrum of:

$$
\nu_j^S
$$

## E2 — Middle-gap mass

Definition:

$$
\boxed{
\mathfrak g_j(\delta)
=
\nu_j^S
\{
\vartheta(S)\le\delta
\}.
}
$$

Investigate whether Q cancellation forces a fixed mass into the:

$$
\delta\downarrow0
$$

boundary.

## E3 — Directional dispersion defect

If the middle gap does not degenerate,

quantify the minimal number / angular diameter of strain cones required to allow a Q zero barycenter.

## E4 — Mean-to-pointwise fluctuation

Unify:

$$
\eta_R^S
$$

using:

- Morrey;
- $D^2u$ active volume;
- C3-V fluctuation intermittency;

## E5 — Derivative-gate interface

If the Q motif recurrently requires:

$$
R^{1-3/p}
\|\nabla S\|_{L^p}
/|\bar S|
\gtrsim1,
$$

test whether it can force:

- derivative active-volume shrinkage;
- Grujić–Xu gate;
- or higher-order multiplicity.

## E6 — Axis-locking dynamics

If common pressure permanently requires:

$$
0\notin\operatorname{conv}\{G(e_i)\},
$$

investigate whether compressive axes are forced to fall into a fixed spherical cap.

## E7 — Axis locking × middle eigenframe

If compressive axes are locked,

does it restrict:

- middle eigenvectors;
- vorticity geometry;
- mean rotation.

## E8 — Second finite-dimensional incompatibility

Search for whether:

$$
\boxed{
\text{axis locking}
+
\text{Q-cancellation-required dispersion}
}
$$

are mutually exclusive.

---

# 62. Official Status

$$
\boxed{
\begin{aligned}
\theta_K=k_2k_3=k_1^2-\frac12
&:\ \mathrm{PROVED},\\
\text{compressive-axis test tensor}
&:\ \mathrm{DEFINED},\\
\text{vorticity contribution uniformly positive}
&:\ \mathrm{PROVED},\\
\text{strong-middle cone}\Rightarrow Q\text{ strict half-space}
&:\ \mathrm{PROVED},\\
\text{strong-middle cone}\Rightarrow\kappa_Q\ge\gamma_K
&:\ \mathrm{PROVED},\\
\text{Seven-Point zero barycenter under cone}
&:\ \mathrm{IMPOSSIBLE},\\
\text{cone-leakage lower bound under cancellation}
&:\ \mathrm{PROVED},\\
Q\text{-cancellation}\Rightarrow
\text{middle-gap degeneration or direction leakage}
&:\ \mathrm{PROVED},\\
\text{mean-to-pointwise interface}
&:\ \mathrm{CONDITIONAL\ ON\ FLUCTUATION},\\
\text{cancellation}\Rightarrow\text{Morrey derivative debt}
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{oriented pressure re-entry}
&:\ \mathrm{PROVED\ UNDER\ CONE+MEAN\ STABILITY},\\
\text{compressive-axis convex-hull pressure obstruction}
&:\ \mathrm{PROVED},\\
\text{six-core witness}
&:\ \mathrm{PROVED},\\
\text{orthogonal-triplet obstruction}
&:\ \mathrm{PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 63. Conclusion

C5-C proved:

$$
\boxed{
\text{temporal scalar compensation cycle itself can still exist}.
}
$$

C5-D now for the first time forces recurrent compensation to confront true spatial–matrix geometry.

For a normalized positive-middle strain direction:

$$
K,
\qquad
\lambda_2(K)>0,
$$

define:

$$
\boxed{
\theta_K
=
\lambda_2(K)\lambda_3(K)
=
\lambda_1(K)^2-\frac12
>0.
}
$$

Then define:

$$
\boxed{
H_K
=
e_1\otimes e_1
-
\frac{
1+\theta_K
}{2}
I.
}
$$

Then within a sufficiently narrow strain cone,

for **arbitrary vorticity**:

$$
\boxed{
H_K:Q
\ge
\frac{
\theta_K
}{4}
(
|S|^2+|\omega|^2
)
\ge
\frac{
\theta_K
}{4}
|Q|.
}
$$

Therefore, the quadratic directions all fall into the same strict half-space:

$$
\boxed{
\widehat H_K:Q/|Q|
\ge
\gamma_K>0.
}
$$

Thus:

$$
\boxed{
0
\notin
\operatorname{conv}\{Q/|Q|\}.
}
$$

Seven-Point zero-barycenter cancellation is directly impossible.

More quantitatively:

$$
\boxed{
\kappa_Q
\ge
[
\gamma_K
-
(1+\gamma_K)
\varepsilon_{\rm cone}
]_+.
}
$$

Therefore:

$$
\boxed{
Q\text{ cancellation}
\Rightarrow
\text{Middle-Gap Degeneration}
\vee
\text{Strain-Direction Leakage}.
}
$$

If the mean direction remains coherent,

leakage further forces:

$$
\boxed{
R^{1-3/p}
\|\nabla S\|_{L^p}
/
|\bar S_R|
\gtrsim1,
}
$$

sending the Q motif directly back to the derivative/intermittency route.

On the other hand,

a strong-middle coherent core makes the quadratic mean no longer capable of cancellation.

Therefore, if mean rotation is also depleted,

pressure must re-enter in an oriented manner:

$$
\boxed{
-\widehat H_K:P_\chi
\gtrsim
A_\chi^Q.
}
$$

If multiple cores further share the same harmonic far-pressure matrix:

$$
F_\ast\in\operatorname{Sym}_0(3),
$$

the true test direction simplifies to:

$$
\boxed{
G(e_1)
=
e_1\otimes e_1-\frac13I.
}
$$

If:

$$
0
\in
\operatorname{conv}
\{G(e_{1,i})\},
$$

a common $F_\ast$ cannot simultaneously compensate all cores.

Since:

$$
\dim\operatorname{Sym}_0(3)=5,
$$

at most six cores are needed to witness this.

Even simpler:

three mutually orthogonal compressive axes directly yield:

$$
\boxed{
G(e_1)+G(e_2)+G(e_3)=0,
}
$$

thus already forming the **Orthogonal-Triplet Pressure Obstruction**.

This is the first time in C5 so far that we have truly obtained:

$$
\boxed{
\textbf{finite-dimensional recurrent-limit incompatibility}.
}
$$

Officially the next paper:

$$
\boxed{
\textbf{C5-E — Strain-Direction Defect Measures,
Middle-Gap Degeneration, and Derivative-Intermittency Closure}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026), 247–270.
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. P. Constantin, *Pressure, Intermittency, Singularity*, arXiv:2301.04489.
5. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024); arXiv:1911.00974.

# Internal dependencies

- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C4I_MiddleOperatorOverlap_PressureReentry_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3U_PressureHeredity_MeanPointwiseRigidity_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-E — Strain-Direction Defect Measures,
Middle-Gap Degeneration, and Derivative-Intermittency Closure}
}
$$