---
title: "Navier–Stokes C3-P: Operator Escape, Far-Pressure Harmonic Matrix, and Finite-Dimensionalization No-Go"
subtitle: "Operator-Level Escape from a Regular Strain Model, Near/Far Pressure Hessian Decomposition, and Why Finite-Dimensional Far Pressure Is Not Automatically Small"
version: "v0.1"
date: "2026-08-14"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style structural reduction / no-go note"
epistemic_status: "Uses external Miller operator criteria and standard pressure/Riesz representation; proves exact two-model and far-pressure structural lemmas. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C3-P
# Operator Escape, Far-Pressure Harmonic Matrix, and Finite-Dimensionalization No-Go

## 0. Context of this Round

C3-O has proven:

$$
\boxed{
\text{SSA-like strain-energy balance}
\not\Rightarrow
\text{SSA-like dynamics}.
}
$$

Using the adjoint cutoff:

$$
\partial_t\chi+u\cdot\nabla\chi+\nu\Delta\chi=0,
$$

the local strain balance can be rearranged as:

$$
E_\chi'+D_\chi=A_\chi+B_\chi,
$$

where:

$$
A_\chi=-2\int\chi\det S,
$$

and:

$$
B_\chi
=
\int\nabla\chi\cdot
\left(
\frac13F_B+F_p
\right).
$$

Thus, the scalar ratio:

$$
\rho=B/A
$$

can only classify the local strain-energy growth carrier,

but cannot determine whether the full operator is close to a certain model.

This round officially upgrades to the operator level.

Core results:

1. Miller 2026 has provided a theorem-backed operator blow-up necessity;
2. a hypothetical blow-up cannot permanently remain within the small perturbation tube of the globally-regular strain–vorticity model;
3. there is an exact operator gap between the strain self-amplification model and the strain–vorticity model;
4. smallness to the SSA model is not a direction for regularity; under Miller's specified initial-data / perturbative hypothesis, it is even compatible with blow-up;
5. the pressure Hessian admits an exact near/far source decomposition;
6. the far pressure is harmonic in the ancestry core;
7. the far pressure Hessian can be finite-dimensionalized into:
   $$
   \boxed{
   \text{constant symmetric trace-free matrix}
   +
   \text{spatially smaller remainder};
   }
   $$
8. but finite-dimensionalization does not equal smallness;
9. far-pressure decoupling requires additional control over a scale-invariant rescaled enstrophy number;
10. thus, a singular survivor must simultaneously pay:
   - the operator escape debt;
   - or the far-pressure harmonic-matrix debt;
   - or the rescaled enstrophy blow-up debt.

---

# 1. To facilitate citing Miller's theorems, we first set $\nu=1$

Miller's strain-model papers use:

$$
\nu=1.
$$

The operator-theorem subsections in this round initially adopt this normalization.

The general case:

$$
\nu>0
$$

can be recovered via standard parabolic nondimensionalization.

The pressure near/far subsections retain the general:

$$
\nu.
$$

---

# 2. Full strain equation

The full strain equation is:

$$
\partial_tS
-
\Delta S
+
P_{st}\left((u\cdot\nabla)S\right)
+
P_{st}\left(
S^2+\frac14\omega\otimes\omega
\right)
=
0.
$$

It can be regrouped relative to two different models.

---

# 3. Strain self-amplification model

Define:

$$
\boxed{
\mathcal N_{SSA}
=
\frac23P_{st}(S^2).
}
$$

The SSA model is:

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SSA}
=
0.
}
$$

The full N–S equation relative to the SSA model is:

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SSA}
+
\mathcal P_{SSA}
=
0,
}
$$

where:

$$
\boxed{
\mathcal P_{SSA}
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

---

# 4. Strain–vorticity interaction model

Miller 2026 defines:

$$
\boxed{
\mathcal N_{SV}
=
-\frac12P_{st}(\omega\otimes\omega).
}
$$

The SV interaction model is:

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SV}
=
0.
}
$$

Miller proved that this model, for:

$$
S^0\in L^2_{st}
$$

possesses a global smooth solution.

The full N–S equation relative to this model is:

$$
\boxed{
\partial_tS
-
\Delta S
+
\mathcal N_{SV}
+
\mathcal Q_{SV}
=
0,
}
$$

where:

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

---

# 5. C3-P.1: Exact Two-Model Gap

## Theorem 5.1

$$
\boxed{
\mathcal Q_{SV}
-
\mathcal P_{SSA}
=
\mathcal N_{SSA}
-
\mathcal N_{SV}.
}
$$

More explicitly:

$$
\boxed{
\mathcal Q_{SV}
-
\mathcal P_{SSA}
=
P_{st}
\left(
\frac23S^2
+
\frac12\omega\otimes\omega
\right).
}
$$

### Proof

Subtract term by term. $\square$

---

# 6. Two-model triangle barrier

Define the model-gap operator:

$$
\boxed{
\mathcal G
=
P_{st}
\left(
\frac23S^2
+
\frac12\omega\otimes\omega
\right).
}
$$

Then:

$$
\mathcal G
=
\mathcal Q_{SV}-\mathcal P_{SSA}.
$$

Therefore:

## Corollary 6.1

For any Banach norm:

$$
\boxed{
\|\mathcal Q_{SV}\|
+
\|\mathcal P_{SSA}\|
\ge
\|\mathcal G\|.
}
$$

Thus, unless the full strain dynamics has:

$$
\mathcal G
$$

being intrinsically small,

it is impossible to simultaneously approach:

- the SSA model;
- the SV interaction model.

---

# 7. External theorem: operator-level regularity debt

Miller 2026 Theorem 1.8, when:

$$
\alpha=0
$$

gives:

If:

$$
T_\ast<\infty
$$

is a finite blow-up time, then:

$$
\boxed{
\int_0^{T_\ast}
\frac{
\|\mathcal Q_{SV}(t)\|_2^2
}{
\|S(t)\|_{\dot H^1}^2
}
\,dt
=
\infty.
}
$$

This is a scale-invariant integrated operator debt.

---

# 8. Scaling audit

Under:

$$
u_\lambda(x,t)
=
\lambda u(\lambda x,\lambda^2t),
$$

we have:

$$
S_\lambda
=
\lambda^2S(\lambda x,\lambda^2t),
$$

and the equation-level quadratic operator:

$$
(\mathcal Q_{SV})_\lambda
=
\lambda^4
\mathcal Q_{SV}(\lambda x,\lambda^2t).
$$

Therefore:

$$
\|\mathcal Q_{SV,\lambda}\|_2
=
\lambda^{5/2}
\|\mathcal Q_{SV}\|_2,
$$

$$
\|S_\lambda\|_{\dot H^1}
=
\lambda^{3/2}
\|S\|_{\dot H^1}.
$$

Thus, the squared ratio scales as:

$$
\lambda^2,
$$

Paired with:

$$
dt\mapsto\lambda^{-2}dt,
$$

the total integral is invariant.

---

# 9. C3-P.2: Regular-Model Operator Escape

Miller 2026 Theorem 1.9 gives:

a hypothetical finite blow-up must satisfy:

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}
\ge
1.
}
$$

Therefore:

## Corollary 9.1

If there exist:

$$
\delta>0
$$

and:

$$
t_0<T_\ast
$$

such that:

$$
\boxed{
\|\mathcal Q_{SV}(t)\|_2
\le
(1-\delta)
\|-\Delta S(t)\|_2
}
$$

holds for all:

$$
t_0<t<T_\ast
$$

then:

$$
T_\ast
$$

cannot be a singular time.

---

# 10. The meaning of operator escape

Therefore, a full N–S hypothetical blow-up cannot asymptotically remain forever in:

$$
\boxed{
\text{the dissipation-small perturbation tube of the globally regular SV-model}.
}
$$

It must, infinitely near the blow-up, satisfy:

$$
\boxed{
\mathcal Q_{SV}
\text{ reaching the same order as }
-\Delta S.
}
$$

This is a true operator-level necessity,

not a scalar energy balance inference.

---

# 11. SSA-small is not a direction for regularity

On the other hand, the SSA model itself can blow up in finite time.

Miller's SSA model paper also proves:

For a specified initial-data sign condition,

if in the full N–S equation:

$$
\mathcal P_{SSA}
$$

remains perturbatively controlled relative to the evolution norm specified in the paper,

then the full N–S also has a conditional finite-time blow-up conclusion.

Therefore:

$$
\boxed{
\mathcal P_{SSA}\text{ being small}
}
$$

cannot be treated as a universal regularity criterion.

---

# 12. Operator phase map

Thus, there are two completely different operator distances:

## Distance to regular SV model

$$
\boxed{
d_{SV}(t)
=
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}.
}
$$

Blow-up necessity:

$$
\boxed{
\limsup d_{SV}\ge1.
}
$$

## Distance to blow-up-capable SSA model

Centered around:

$$
\mathcal P_{SSA}
$$

Its smallness is not a guarantee of regularity;

under specific hypotheses, it is even blow-up-compatible.

---

# 13. Balance ratio and operator ratio must be separated

C3-O's:

$$
\rho=B/A
$$

only looks at:

$$
\boxed{
\text{localized strain-energy balance}.
}
$$

While:

$$
d_{SV}
$$

looks at:

$$
\boxed{
\text{full operator size relative to strain dissipation}.
}
$$

Therefore:

$$
\boxed{
\rho\to0
}
$$

can perfectly well hold simultaneously with:

$$
\boxed{
d_{SV}\gtrsim1
}
$$

This is exactly the:

$$
\boxed{
\text{Balance-SSA / Operator-large}
}
$$

regime.

---

# 14. Pressure Poisson equation

Returning to the general case:

$$
\nu>0.
$$

Let:

$$
A=\nabla u.
$$

The divergence-free N–S gives:

$$
\boxed{
-\Delta p
=
\partial_i u_j
\partial_j u_i
=
\operatorname{tr}(A^2).
}
$$

Define:

$$
\boxed{
f
=
\operatorname{tr}(A^2).
}
$$

Then:

$$
p
=
(-\Delta)^{-1}f
$$

up to a time-dependent additive constant.

Therefore:

$$
\boxed{
\partial_a\partial_b p
=
R_aR_b f.
}
$$

The pressure Hessian is a zero-order Calderón–Zygmund transform of $f$.

---

# 15. Source size

Pointwise:

$$
|f|
=
|\operatorname{tr}(A^2)|
\le
|A|^2.
$$

Therefore:

$$
\boxed{
\|f(t)\|_1
\le
\|\nabla u(t)\|_2^2.
}
$$

---

# 16. Near/far source decomposition

Fix:

$$
x_0\in\mathbb R^3,
$$

core radius:

$$
R>0,
$$

and:

$$
\kappa\ge4.
$$

Take a smooth cutoff:

$$
\eta_{\kappa R}
$$

satisfying:

$$
\eta_{\kappa R}=1
$$

on:

$$
B_{\kappa R}(x_0),
$$

and supported in:

$$
B_{2\kappa R}(x_0).
$$

Define:

$$
f_{\rm near}
=
\eta_{\kappa R}f,
$$

$$
f_{\rm far}
=
(1-\eta_{\kappa R})f.
$$

and:

$$
p_{\rm near}
=
(-\Delta)^{-1}f_{\rm near},
$$

$$
p_{\rm far}
=
(-\Delta)^{-1}f_{\rm far}.
$$

---

# 17. Far pressure is harmonic in the core

Since:

$$
f_{\rm far}=0
$$

on:

$$
B_{\kappa R}(x_0),
$$

therefore:

$$
\boxed{
\Delta p_{\rm far}=0
}
$$

in:

$$
B_{\kappa R}(x_0).
$$

Thus:

$$
\boxed{
H_{\rm far}
=
\nabla^2p_{\rm far}
}
$$

is a harmonic symmetric tensor field in the ancestry core,

and:

$$
\boxed{
\operatorname{tr}H_{\rm far}=0.
}
$$

---

# 18. Riesz kernel bound

The Riesz-pair kernel, away from the singularity, satisfies:

$$
|\nabla^mK_{ab}(z)|
\le
C_m
|z|^{-3-m}.
$$

For:

$$
x\in B_R(x_0),
$$

and:

$$
y\in\operatorname{supp}f_{\rm far},
$$

we have:

$$
|x-y|
\ge
(\kappa-1)R.
$$

Therefore:

## Theorem 18.1

For any:

$$
m\ge0,
$$

$$
\boxed{
\|\nabla^mH_{\rm far}\|_{L^\infty(B_R)}
\le
C_m
(\kappa R)^{-3-m}
\|f\|_1.
}
$$

up to harmless constants depending on the cutoff geometry.

From:

$$
\|f\|_1\le\|\nabla u\|_2^2,
$$

we obtain:

$$
\boxed{
\|\nabla^mH_{\rm far}\|_{L^\infty(B_R)}
\le
C_m
\kappa^{-3-m}
R^{-3-m}
\|\nabla u\|_2^2.
}
$$

---

# 19. C3-P.3: Far-Pressure Finite-Dimensionalization Lemma

Let:

$$
\boxed{
H_0(t)
=
H_{\rm far}(x_0,t).
}
$$

Then:

$$
H_0
$$

is a symmetric trace-free matrix.

Furthermore:

$$
\boxed{
|H_0|
\le
C
\kappa^{-3}
R^{-3}
\|\nabla u\|_2^2.
}
$$

By the mean value theorem and the $m=1$ estimate:

$$
\boxed{
\sup_{x\in B_R}
|H_{\rm far}(x)-H_0|
\le
C
\kappa^{-4}
R^{-3}
\|\nabla u\|_2^2.
}
$$

Therefore:

$$
\boxed{
H_{\rm far}(x)
=
H_0
+
E_{\rm far}(x),
}
$$

where:

$$
\boxed{
\|E_{\rm far}\|_{L^\infty(B_R)}
\le
C
\kappa^{-4}
R^{-3}
\|\nabla u\|_2^2.
}
$$

---

# 20. 5-dimensional far-pressure channel

The dimension of the space of symmetric:

$$
3\times3
$$

trace-free matrices is:

$$
\boxed{
5.
}
$$

Therefore, the leading effect of the far pressure in a small ancestry core is not an arbitrary field,

but rather:

$$
\boxed{
\textbf{a five-dimensional harmonic pressure-Hessian channel}
}
$$

plus an extra factor of:

$$
\kappa^{-1}
$$

for the spatially varying remainder.

---

# 21. Finite-dimensionalization ≠ smallness

Define the scale-invariant rescaled enstrophy number:

$$
\boxed{
\mathfrak E_R(t)
=
\frac{
R
\|\nabla u(t)\|_2^2
}{
\nu^2
}.
}
$$

Under N–S scaling:

$$
R\mapsto\lambda^{-1}R,
$$

$$
\|\nabla u\|_2^2\mapsto\lambda\|\nabla u\|_2^2,
$$

Therefore:

$$
\mathfrak E_R
$$

is invariant.

---

# 22. Normalized far-pressure Hessian

The pressure Hessian scales as:

$$
\nu^2R^{-4}.
$$

Define:

$$
\boxed{
\widehat H_{\rm far}
=
\frac{
R^4
}{
\nu^2
}
H_{\rm far}.
}
$$

Then:

$$
\boxed{
|\widehat H_0|
\le
C
\kappa^{-3}
\mathfrak E_R.
}
$$

and:

$$
\boxed{
\sup_{B_R}
|\widehat H_{\rm far}-\widehat H_0|
\le
C
\kappa^{-4}
\mathfrak E_R.
}
$$

---

# 23. C3-P.4: Conditional Far-Pressure Decoupling

## Theorem 23.1

If a sequence of ancestry scales:

$$
R_n\to0
$$

satisfies a uniform rescaled-enstrophy bound:

$$
\boxed{
\sup_n
\mathfrak E_{R_n}(t_n)
<\infty,
}
$$

then taking:

$$
\kappa\to\infty
$$

yields:

$$
\boxed{
\widehat H_{{\rm far},n}
\to0
}
$$

uniformly on the unit rescaled core,

decaying at least as:

$$
O(\kappa^{-3})
$$

$\square$

---

# 24. Far-pressure decoupling No-Go

The energy inequality only gives:

$$
\nu
\int_0^{T_\ast}
\|\nabla u(t)\|_2^2dt
<
\infty.
$$

It does not give:

$$
\boxed{
\sup_n
R_n
\|\nabla u(t_n)\|_2^2
<\infty.
}
$$

Therefore:

$$
\boxed{
\text{far pressure cannot be unconditionally discarded in a singular ancestry zoom}.
}
$$

If:

$$
\mathfrak E_{R_n}\to\infty,
$$

it can compensate for the:

$$
\kappa^{-3}
$$

spatial distance decay.

---

# 25. Far pressure dichotomy

Thus, the far pressure in the ancestry core has:

## P-FAR-A — Decoupled branch

$$
\boxed{
\mathfrak E_R=O(1)
}
$$

then the far pressure can be decoupled by a large:

$$
\kappa
$$

## P-FAR-B — Critical enstrophy branch

$$
\boxed{
\mathfrak E_R\to\infty
}
$$

then the far pressure may maintain an order-one or even larger normalized influence.

This converts pressure nonlocality into another critical moment debt.

---

# 26. Pressure current decomposition

C3-N defines:

$$
F_p
=
(\nabla^2p-\Delta p\,I)u.
$$

In the core, the far pressure is harmonic:

$$
\Delta p_{\rm far}=0.
$$

Therefore:

$$
\boxed{
F_{p,{\rm far}}
=
H_{\rm far}u.
}
$$

Using:

$$
H_{\rm far}=H_0+E_{\rm far},
$$

we obtain:

$$
\boxed{
F_{p,{\rm far}}
=
H_0u
+
E_{\rm far}u.
}
$$

---

# 27. Leading harmonic-matrix pressure current

For the localization:

$$
\chi,
$$

the far-pressure boundary current is:

$$
B_p^{far}
=
\int
\nabla\chi\cdot
H_{\rm far}u.
$$

The leading constant-matrix part is:

$$
B_p^{H_0}
=
\int
\nabla\chi\cdot
H_0u.
$$

Since:

$$
H_0
$$

is spatially constant,

integration by parts gives:

$$
\boxed{
B_p^{H_0}
=
-
\int
\chi
H_0:S\,dx.
}
$$

Therefore, the leading-order core effect of the far pressure can be viewed as:

$$
\boxed{
\text{a constant trace-free external strain matrix coupled to local }S.
}
$$

---

# 28. This matrix cannot be gauged away

The pressure only allows adding:

$$
c(t)
$$

without changing:

$$
\nabla p.
$$

A constant Hessian:

$$
H_0\ne0
$$

corresponds to a quadratic harmonic pressure component,

whose gradient is an affine force.

Therefore:

$$
\boxed{
H_0
}
$$

is not a pressure additive gauge.

It is a genuine dynamical far-field channel.

---

# 29. Spatially varying far-pressure remainder

The remainder current is:

$$
B_p^{rem}
=
\int
\nabla\chi\cdot
E_{\rm far}u.
$$

If:

$$
|\nabla\chi|
\lesssim
R^{-1}
$$

in the shell:

$$
\mathcal A_R,
$$

then:

$$
\boxed{
|B_p^{rem}|
\le
C
\kappa^{-4}
R^{-4}
\|\nabla u\|_2^2
\int_{\mathcal A_R}
|u|dx.
}
$$

Compared to the leading pressure-Hessian bound,

the spatial variation gains an extra:

$$
\boxed{
\kappa^{-1}.
}
$$

---

# 30. The true meaning of the pressure finite-dimensionalization theorem

The far pressure is not:

$$
\boxed{
\text{automatically negligible}.
}
$$

Rather, it is:

$$
\boxed{
\text{large-scale infinite-dimensional source}
\to
\text{5D harmonic matrix}
+
\text{small spatial variation}
}
$$

as its leading asymptotic representation in the local core.

Therefore, it is a:

$$
\boxed{
\textbf{complexity compression theorem},
}
$$

not a smallness theorem.

---

# 31. Relationship with the Bradshaw–Tsai local pressure expansion

The local pressure expansion literature inherently splits the pressure into:

- a local source contribution;
- a nonlocal/harmonic contribution;

to handle the whole-space Navier–Stokes pressure.

The far-pressure matrix lemma in this round is, under smooth ancestry-core conditions,

applying a first-order Taylor / multipole compression to:

$$
\nabla^2p
$$

Thus, it is compatible with the local pressure expansion framework,

but the 5D matrix statement in this text is a specific derivative-level consequence utilized by this route of the project.

---

# 32. Betchov current and pressure current must not be conflated

Adjoint balance:

$$
B_\chi
=
B_\chi^B+B_\chi^p.
$$

where:

$$
B_\chi^B
=
\frac13
\int\nabla\chi\cdot F_B,
$$

$$
B_\chi^p
=
\int\nabla\chi\cdot F_p.
$$

Difference:

### Betchov current

$$
F_B
$$

is a local algebraic current:

$$
u(\nabla u)^2.
$$

### Pressure current

$$
F_p
$$

contains:

$$
\nabla^2p,
$$

while:

$$
\nabla^2p
$$

is a Calderón–Zygmund nonlocal transform.

Therefore:

$$
\boxed{
\text{boundary current}
}
$$

this common name cannot erase the fact that:

$$
\boxed{
\text{local algebraic provenance}
\neq
\text{nonlocal pressure provenance}.
}
$$

---

# 33. Operator theorem and boundary theorem are different observation interfaces

The Miller operator criterion:

$$
d_{SV}(t)
=
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}
$$

is the:

$$
\boxed{
\text{bulk operator norm interface}.
}
$$

C3-O's:

$$
\rho=B/A
$$

is the:

$$
\boxed{
\text{adjoint-localized balance interface}.
}
$$

The pressure matrix:

$$
H_0
$$

is the:

$$
\boxed{
\text{far-field harmonic forcing interface}.
}
$$

The three cannot be stealthily substituted for one another.

---

# 34. C3-P.5: Three-Interface Survivor Constraint

A hypothetical singular ancestry must simultaneously respect:

## Interface P1 — Operator escape

$$
\boxed{
\limsup
d_{SV}\ge1.
}
$$

## Interface P2 — Local growth

For positive SSA-supported adjoint windows:

$$
\boxed{
\rho>-1.
}
$$

## Interface P3 — Far pressure

If the far-pressure effect remains non-negligible in the rescaled core,

then at least:

$$
\boxed{
\mathfrak E_R
}
$$

cannot be too small,

or its 5D harmonic matrix:

$$
\boxed{
H_0
}
$$

must persistently possess a critical-size coupling.

Currently, these are **parallel necessary constraints**,

not a proven mutual contradiction.

---

# 35. Blow-up operator debt is better than the original candidate $\mathfrak P$

The candidate proposed in C3-O:

$$
\mathfrak P
=
\frac{
\int
\|\mathcal P_{SSA}\|_{\dot H^{-1}}^2
}{
\nu^2\int
\|S\|_{\dot H^1}^2
}
$$

remains a reasonable diagnostic,

but lacks direct theorem support.

C3-P should prioritize incorporating the Miller theorem-backed:

$$
\boxed{
\mathfrak Q_{SV}
=
\int
\frac{
\|\mathcal Q_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}dt.
}
$$

A hypothetical blow-up requires:

$$
\boxed{
\mathfrak Q_{SV}
=
\infty.
}
$$

---

# 36. Two-operator X-certificate

Define:

$$
\boxed{
\operatorname{XOp}_n
=
\left\langle
\mathcal P_{SSA,n},
\mathcal Q_{SV,n},
\mathcal G_n,
d_{SSA,n},
d_{SV,n},
\operatorname{Prov}_n
\right\rangle.
}
$$

where:

$$
\mathcal G_n
=
\mathcal Q_{SV,n}
-
\mathcal P_{SSA,n}.
$$

Guards:

## G-MODEL

Explicitly indicates which model is being compared.

## G-REGMODEL

The SV model has a global regularity theorem.

## G-BLOWMODEL

The SSA model has a finite-time blowup theorem.

## G-GAP

The two model distances cannot be conflated into a single "perturbation size".

## G-ORTH

Zero pairing does not equal a zero operator.

---

# 37. Pressure X-certificate

Define:

$$
\boxed{
\operatorname{XPressure}_n
=
\left\langle
p_{\rm near},
H_{0,n},
E_{{\rm far},n},
\kappa,
\mathfrak E_{R_n},
\operatorname{ProvFar}
\right\rangle.
}
$$

Guards:

## G-PNEAR

The near pressure is generated by the core/source neighborhood.

## G-PFAR

The far pressure is harmonic in the core.

## G-H0

Preserves the constant trace-free matrix:

$$
H_0.
$$

## G-PREM

Preserves the remainder:

$$
E_{\rm far}.
$$

## G-PENST

Cannot declare the far pressure small simply because of:

$$
\kappa^{-3}
$$

must check:

$$
\mathfrak E_R.
$$

---

# 38. The true threshold for pressure decoupling

Normalized:

$$
|\widehat H_0|
\lesssim
\kappa^{-3}
\mathfrak E_R.
$$

Therefore, for the far pressure to decouple,

what is truly needed is:

$$
\boxed{
\kappa^{-3}
\mathfrak E_R
\to0.
}
$$

not simply:

$$
\kappa\to\infty.
$$

If in the ancestry:

$$
\mathfrak E_R
$$

grows as:

$$
\kappa^3
$$

or faster,

the far pressure can remain non-negligible.

---

# 39. New No-Go: spatial separation alone cannot kill pressure

$$
\boxed{
\operatorname{dist}(\text{defect},\text{core})/R
\to\infty
}
$$

does not automatically imply:

$$
\boxed{
\text{pressure influence}\to0.
}
$$

because the pressure source amplitude / rescaled enstrophy can grow synchronously.

Therefore, C3-F's off-diagonal decay is very strong for the band-limited Leray nonlinearity,

but the far source of the pressure Hessian requires additional control via a critical source norm.

---

# 40. New frontier: C3-Q

C3-P has answered two questions.

### Can operator-smallness represent the full singular dynamics?

For the globally regular SV model:

$$
\boxed{
\text{NO: blow-up must operator-escape}.
}
$$

### Can the far pressure be directly spatially decoupled?

$$
\boxed{
\text{NO: it can only be finite-dimensionalized;
smallness still requires rescaled-enstrophy control}.
}
$$

Thus, the next topic is:

$$
\boxed{
\textbf{C3-Q — Harmonic Pressure-Matrix / Operator-Escape Coupling Rigidity}.
}
$$

---

# 41. C3-Q proof obligations

## Q1 — Normalize harmonic matrix

At the ancestry scale:

$$
R_n,
$$

Define:

$$
\boxed{
\mathsf H_n
=
\frac{
R_n^4
}{
\nu^2
}
H_{0,n}.
}
$$

Extract a subsequence and analyze:

- $\mathsf H_n\to0$;
- $\mathsf H_n\to\mathsf H_\ast\ne0$;
- $|\mathsf H_n|\to\infty$.

## Q2 — Harmonic-matrix eigengeometry

$\mathsf H_n$ is a symmetric trace-free 5D object.

Study the coupling of its eigenframe with the local strain:

$$
S_n
$$

and the vorticity direction:

$$
\xi_n
$$

## Q3 — Pressure-current ratio

Compare:

$$
B_I^p/A_I
$$

with:

$$
\mathsf H_n:S_n.
$$

Determine whether the cancellation corridor can be primarily supported by the far harmonic matrix.

## Q4 — Operator escape localization

The Miller criterion is global:

$$
\|\mathcal Q_{SV}\|_2.
$$

Investigate whether a localized operator debt can be extracted within the ancestry core.

Avoid the scenario where:

$$
\text{global operator large}
$$

actually only comes from a far defect.

## Q5 — Integrated operator debt partition

Partition:

$$
\int
\frac{
\|\mathcal Q_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}
dt
=
\infty
$$

into:

- the ancestry core;
- spatial defects;
- frequency defects.

Connecting to the C3-I defect trichotomy.

## Q6 — Two-model gap rigidity

Investigate whether:

$$
\mathcal G
=
P_{st}
\left(
\frac23S^2+\frac12\omega\otimes\omega
\right)
$$

can be small in the ancestry core.

If not small, the full dynamics cannot simultaneously approach both models.

## Q7 — Pressure/enstrophy dichotomy

If:

$$
\mathsf H_n
$$

does not decouple,

use:

$$
|\mathsf H_n|
\lesssim
\kappa^{-3}\mathfrak E_{R_n}
$$

to convert the far-pressure survivor into a rescaled-enstrophy blow-up condition.

## Q8 — Far-pressure Taylor hierarchy

If the constant matrix channel can be ruled out by some rigidity,

the next-order far-pressure term is:

$$
\nabla H_{\rm far}(x_0)
$$

and pays an extra:

$$
\kappa^{-1}.
$$

Establish a multipole hierarchy.

---

# 42. Formal status

$$
\boxed{
\begin{aligned}
\text{SSA/SV two-model operator decomposition}
&:\ \mathrm{PROVED},\\
\text{exact two-model gap}
&:\ \mathrm{PROVED},\\
\text{Miller integrated SV-operator debt}
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\limsup\|\mathcal Q_{SV}\|_2/\|-\Delta S\|_2\ge1
&:\ \mathrm{EXTERNAL\ THEOREM},\\
\text{eventual SV-small perturbation under blow-up}
&:\ \mathrm{EXCLUDED},\\
\text{SSA perturbation smallness as regularity}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
-\Delta p=\operatorname{tr}(A^2)
&:\ \mathrm{STANDARD},\\
\nabla^2p=R_iR_j\operatorname{tr}(A^2)
&:\ \mathrm{STANDARD},\\
\text{far pressure harmonic in core}
&:\ \mathrm{PROVED},\\
\text{far-pressure derivative decay}
&:\ \mathrm{PROVED},\\
\text{5D harmonic-matrix finite-dimensionalization}
&:\ \mathrm{PROVED},\\
\text{spatially varying far remainder gains }\kappa^{-1}
&:\ \mathrm{PROVED},\\
\text{finite-dimensionalization}\Rightarrow\text{smallness}
&:\ \mathrm{FALSE/NO\mbox{-}GO},\\
\text{far pressure decoupling under bounded }\mathfrak E_R
&:\ \mathrm{PROVED\ CONDITIONAL},\\
\text{unconditional far-pressure decoupling}
&:\ \mathrm{OPEN/NO\mbox{-}GO\ from\ energy},\\
\text{harmonic pressure-matrix/operator coupling rigidity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 43. Conclusion

C3-O tells us:

$$
\boxed{
\text{the balance ratio is insufficient;
we must look at the operator}.
}
$$

C3-P now obtains a ready-made theorem-backed operator necessity:

$$
\boxed{
\mathrm{Blowup}
\Rightarrow
\int_0^{T_\ast}
\frac{
\|\mathcal Q_{SV}\|_2^2
}{
\|S\|_{\dot H^1}^2
}dt
=
\infty,
}
$$

and:

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\frac{
\|\mathcal Q_{SV}\|_2
}{
\|-\Delta S\|_2
}
\ge1.
}
$$

Therefore, singular dynamics must escape the perturbative tube of the globally-regular SV model.

On the other hand,

the SSA model itself can blow up,

so:

$$
\boxed{
\text{small distance to SSA model}
}
$$

cannot serve as a direction for regularity.

The pressure route is also clearly compressed:

$$
\boxed{
\nabla^2p_{\rm far}
=
H_0
+
E_{\rm far},
}
$$

where:

$$
H_0
$$

is a:

$$
\boxed{
5\text{-dimensional constant symmetric trace-free matrix},
}
$$

while:

$$
E_{\rm far}
$$

gains an extra:

$$
\kappa^{-1}
$$

of spatial-variation suppression.

But:

$$
\boxed{
\text{finite-dimensionalization}
\neq
\text{smallness}.
}
$$

The normalized far-pressure strength obeys:

$$
\boxed{
|\widehat H_0|
\lesssim
\kappa^{-3}
\mathfrak E_R.
}
$$

Therefore, the true decoupling condition is:

$$
\boxed{
\kappa^{-3}\mathfrak E_R\to0.
}
$$

If the rescaled enstrophy blows up fast enough,

the far-field pressure can still maintain a critical-size effect.

Thus, the next round officially enters:

$$
\boxed{
\textbf{C3-Q — Harmonic Pressure-Matrix / Operator-Escape Coupling Rigidity}.
}
$$

What truly needs to be tested is:

> If a singular ancestry must simultaneously make the regular-model operator defect reach the dissipation scale,
> and allow the far pressure to persistently support the local strain geometry via a 5D harmonic matrix,
> can these two channels be simultaneously maintained down to infinite scales by the same set of exact N–S constraints?

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691; Pure and Applied Analysis 8 (2026).
2. E. Miller, *Finite-time blowup for a Navier–Stokes model equation for the self-amplification of strain*, arXiv:1910.05415; Analysis & PDE 16 (2023).
3. B. Álvarez-Samaniego, W. P. Álvarez-Samaniego, P. G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier–Stokes equations on the whole space*, arXiv:2004.02588; Acta Applicandae Mathematicae 176 (2021).
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
5. M. Carbone, M. Wilczek, *Only two Betchov homogeneity constraints exist for isotropic turbulence*, arXiv:2112.12820; Journal of Fluid Mechanics 948 (2022), R2.

# Internal dependencies

- `NS_C3N_LocalizedBetchov_StrainBoundaryBalance_v0.1.md`
- `NS_C3O_AdjointCore_BalanceDynamicsSeparation_v0.1.md`
- `NS_C3M_VorticityStrain_Betchov_GeometryDebt_v0.1.md`
- `NS_C3L_CriticalMomentEscape_StrainGeometryDebt_v0.1.md`
- `NS_C3K_AbsoluteOccupancy_OneMomentGap_v0.1.md`
- `NS_C3I_FrontierUVCap_DefectTrichotomy_v0.1.md`
- `NS_C3G_FirstCrossing_CausalAncestry_DepletionNoGo_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C3-Q — Harmonic Pressure-Matrix / Operator-Escape Coupling Rigidity}
}
$$