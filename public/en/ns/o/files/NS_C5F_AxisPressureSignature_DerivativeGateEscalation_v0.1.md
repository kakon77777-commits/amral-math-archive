---
title: "Navier–Stokes C5-F: Compressive-Axis Robustness, Pressure-Signature Locking, and Derivative-Gate Escalation"
subtitle: "Middle-Gap Limits Preserve the Compressive Axis; Nondegenerate Q-Cancellation Forces Axis Dispersion; Strong Common Far Pressure Can Conflict with It"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style strain/vorticity defect coupling / axis-pressure incompatibility / derivative-gate audit"
epistemic_status: "Exact trace-free spectral algebra + finite-dimensional axis-cap half-space theorem + pressure-signature geometry + vorticity projection/complement dichotomy + conditional scaling interface to published derivative-sparseness criteria. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-F
# Compressive-Axis Robustness, Pressure-Signature Locking, and Derivative-Gate Escalation

## 0. Current Round Positioning

C5-E has completely translated the recurrent Seven-Point quadratic cancellation into PDE field defects:

$$
\boxed{
Q\text{-Cancellation}
\Rightarrow
\text{Middle-Gap/Cubic Intermittency}
\vee
\text{Strain-Derivative Fluctuation}
\vee
\text{Vorticity-Dominant Leakage}.
}
$$

Meanwhile, C5-D features the common far-pressure convex geometry:

$$
\boxed{
G(e_1)
=
e_1\otimes e_1-\frac13I,
}
$$

and:

$$
\boxed{
0\in\operatorname{conv}\{G(e_i)\}
\Rightarrow
\text{one common far-pressure matrix cannot compensate all cores}.
}
$$

Questions for C5-F:

1. Does middle-gap degeneration:
   $$
   \lambda_2/|S|\to0
   $$
   cause the compressive-axis pressure geometry to disappear?
2. Does the strain-direction dispersion required for Q-cancellation truly necessitate the dispersion of the most-compressive eigenvector?
3. Can common far-pressure compensation force axis locking, and form a second finite-dimensional incompatibility with Q-cancellation?
4. Does vorticity leakage ultimately return to the Miller operator or the constraint complement?
5. Can the strain-derivative / cubic-intermittency pre-gates truly approach the scale of the published Grujić–Xu theorem?
6. If fixed derivative levels consistently fail, are we truly forced into:
   $$
   k_j\to\infty?
   $$

Main results of this round:

1. The most-compressive eigenvalue of the positive-middle normalized strain possesses a uniform spectral gap:
   $$
   \boxed{
   \lambda_2-\lambda_1\ge1/\sqrt2;
   }
   $$
2. Therefore, the compressive-axis projector is stable metadata throughout the entire positive-middle sector, including the middle-gap boundary;
3. Middle-gap degeneration only pushes the eigenvalue shape toward:
   $$
   (-1/\sqrt2,0,1/\sqrt2),
   $$
   and does not erase $e_1$;
4. If:
   $$
   \vartheta\ge\delta>0
   $$
   and the compressive axes all lie within a sufficiently narrow common cap, all local quadratic directions still fall into a common strict half-space;
5. Thus:
   $$
   \boxed{
   Q\text{-cancellation}
   +
   \text{nondegenerate middle gap}
   \Rightarrow
   \textbf{compressive-axis dispersion};
   }
   $$
6. Merely rotating $e_2/e_3$ while keeping $e_1$ fixed cannot support a Q zero barycenter;
7. If the common far-pressure matrix has the signature:
   $$
   (-,+,+)
   $$
   and the negative compensation margin is sufficiently strong, it will lock the compressive axes into a projective cap;
8. If this cap is narrower than the axis-dispersion scale required by Q-cancellation, the two are incompatible;
9. Therefore, if nondegenerate-gap Q-cancellation is to coexist with common far pressure, it must escape toward:
   - weak pressure margin;
   - two-negative-eigenvalue far matrix;
   - pressure-source fragmentation;
   - mean rotation;
10. Middle-gap degeneration still preserves the common pressure-axis constraint;
11. Vorticity-dominant leakage forces:
    $$
    \boxed{
    P_{st}(\omega\otimes\omega)
    \text{ congestion}
    \vee
    P_{st}^{\perp}(\omega\otimes\omega)
    \text{ constraint-complement congestion};
    }
    $$
12. Strain-derivative stock directly generates a scale-critical $D^2u$ pointwise amplitude somewhere;
13. The sparse-scale exponent of middle-gap cubic intermittency in NS-rescaled variables:
    $$
    2/3
    $$
    is more favorable than the fixed-$k=1$ direct velocity regularity scale exponent:
    $$
    3/5
    $$
14. However, the raw $Du$ component/sign theorem interface may still be obstructed by vorticity geometry;
15. Derivative-order escalation is not an automatic theorem: any best-order sequence only has:
    $$
    \boxed{
    \text{fixed-order recurrent defect}
    \vee
    k_j\to\infty;
    }
    $$
16. $k_j\to\infty$ makes the Grujić–Xu scaling burden asymptotically vanish, but does not automatically satisfy the component/sign, analytic-time, and chain hypotheses;
17. Therefore, C5-F compresses the residual into:
    $$
    \boxed{
    \text{Axis/Pressure Signature Defect}
    \vee
    \text{Vorticity Projection Defect}
    \vee
    \text{Fixed-Order Gate Defect}
    \vee
    \text{Derivative-Order Escape}.
    }
    $$

---

# 1. Fresh primary-source audit

This round re-audits three theorem-level anchors.

## 1.1 Miller 2026

Miller defines:

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
\right),
}
$$

and proves that if there is a finite-time blow-up:

$$
\boxed{
\limsup_{t\uparrow T_\ast}
\frac{
\|\mathcal Q_{SV}(t)\|_2
}{
\|-\Delta S(t)\|_2
}
\ge1.
}
$$

His new identity:

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0
}
$$

continues to provide an orthogonality anchor for the vorticity-quadratic operator channel and the growth direction.

## 1.2 Grujić–Xu 2024

Formal publication:

$$
\boxed{
\text{J. Math. Fluid Mech. 26, 53 (2024)}.
}
$$

Theorem 3.5:

For a fixed derivative order $k$,

if at an appropriate later time after the escape time,

the selected:

$$
D^ku
$$

or:

$$
D^k\omega
$$

component/sign superlevel set at the scale:

$$
\boxed{
\rho
\lesssim
\|D^ku\|_\infty^{-3/(2k+3)}
}
$$

for velocity in $d=3$,

or the corresponding vorticity scale,

exhibits 1D sparseness,

then regularity extends past the potential blow-up time.

Theorem 3.14:

In the derivative-chain / analyticity framework,

the regularity scale improves to:

$$
\boxed{
\rho
\lesssim
\|D^ku\|_\infty^{-1/(k+1)}
}
$$

for the velocity route,

and the scaling gap asymptotically vanishes as:

$$
k\to\infty.
$$

### Guard

C5-F only performs a theorem-interface audit,

and does not directly claim the strain/vorticity pre-gates as published theorem hypotheses.

## 1.3 Bradshaw–Tsai

The whole-space pressure local expansion provides a rigorous foundation for:

- local pressure;
- far contribution;
- harmonic far-field provenance.

Therefore, the common far-pressure matrix in C5-D/F is only used when:

$$
\boxed{
\text{common far-field dominance has been separately proven}
}
$$

---

# 2. Positive-middle normalized eigenvalue algebra

Take:

$$
K\in\operatorname{Sym}_0(3),
\qquad
|K|_F=1.
$$

with ordered eigenvalues:

$$
k_1\le k_2\le k_3.
$$

Assume:

$$
\boxed{
k_2\ge0.
}
$$

Define:

$$
\boxed{
\vartheta(K)
=
k_2k_3.
}
$$

From C5-D:

$$
\boxed{
k_1^2
=
\frac12+\vartheta.
}
$$

---

# 3. C5-F.1: Uniform Compressive Spectral Gap

Since:

$$
\vartheta\ge0,
$$

$$
|k_1|
\ge
\frac1{\sqrt2}.
$$

and:

$$
k_1<0,
\qquad
k_2\ge0.
$$

therefore:

$$
\boxed{
k_2-k_1
\ge
\frac1{\sqrt2}.
}
$$

### Conclusion

The most-compressive eigenvalue:

$$
k_1
$$

is uniformly simple throughout the entire positive-middle closed sector:

$$
k_2\ge0
$$

---

# 4. Compressive-axis projector

Let:

$$
\boxed{
P_1(K)
=
e_1(K)\otimes e_1(K)
}
$$

be the $k_1$ spectral projector.

Due to the uniform gap:

$$
\ge1/\sqrt2,
$$

standard finite-dimensional spectral perturbation estimates yield:

$$
\boxed{
\|P_1(K)-P_1(L)\|_F
\le
C
\|K-L\|_F
}
$$

for sufficiently close:

$$
K,L,
$$

in the positive-middle normalized sector, where $C$ can be chosen universally.

### Significance

$$
\boxed{
\textbf{compressive axis is robust even when the middle gap degenerates}.
}
$$

---

# 5. Middle-gap boundary shape

If:

$$
K_j
$$

is normalized positive-middle,

and:

$$
\vartheta(K_j)\to0,
$$

then:

$$
k_{1,j}^2
=
\frac12+\vartheta_j
\to
\frac12.
$$

Since:

$$
k_{1,j}<0,
$$

$$
\boxed{
k_{1,j}\to
-\frac1{\sqrt2}.
}
$$

From:

$$
k_1+k_2+k_3=0
$$

and:

$$
k_2k_3\to0,
$$

the positive sector gives:

$$
\boxed{
k_{2,j}\to0,
}
$$

$$
\boxed{
k_{3,j}\to
\frac1{\sqrt2}.
}
$$

---

# 6. C5-F.2: Middle-Gap Limit Preserves the Compressive Axis

Along a subsequence:

$$
P_1(K_j)\to P_\ast
$$

in the compact rank-one projector space.

The limit strain shape is:

$$
\boxed{
K_\ast
=
R_\ast
\operatorname{diag}
\left(
-\frac1{\sqrt2},
0,
\frac1{\sqrt2}
\right)
R_\ast^T,
}
$$

with:

$$
\boxed{
P_\ast
=
R_\ast
e_1\otimes e_1
R_\ast^T.
}
$$

### Conclusion

$$
\boxed{
\text{Middle-Gap Degeneration}
\not\Rightarrow
\text{Pressure-Axis Decoherence}.
}
$$

Gap degeneration only kills the:

$$
\theta_K
$$

half-space margin,

it does not kill:

$$
\boxed{
G(e_1)
=
e_1\otimes e_1-\frac13I.
}
$$

---

# 7. Exact common-axis quadratic half-space

Now assume:

$$
\boxed{
\vartheta(S/|S|)
\ge
\delta>0.
}
$$

and the most-compressive axis is exactly:

$$
\boxed{
e_1=e
}
$$

fixed.

Define:

$$
\boxed{
H_{e,\delta}
=
e\otimes e
-
\frac{
1+\delta
}{
2
}
I.
}
$$

---

# 8. Strain contribution with fixed axis

Since:

$$
e^TS^2e
=
\lambda_1^2
=
|S|^2
\left(
\frac12+\vartheta
\right),
$$

therefore:

$$
H_{e,\delta}:S^2
=
|S|^2
\left[
\frac12+\vartheta
-
\frac{
1+\delta
}{2}
\right].
$$

Thus:

$$
\boxed{
H_{e,\delta}:S^2
\ge
\frac{
\delta
}{2}
|S|^2.
}
$$

---

# 9. Vorticity contribution with fixed axis

Compute:

$$
\operatorname{tr}H_{e,\delta}
=
-\frac{
1+3\delta
}{2}.
$$

therefore:

$$
\boxed{
H_{e,\delta}
-
(\operatorname{tr}H_{e,\delta})I
=
e\otimes e
+
\delta I.
}
$$

Thus:

$$
\boxed{
H_{e,\delta}:
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\ge
\frac{
\delta
}{4}
|\omega|^2.
}
$$

---

# 10. C5-F.3: Fixed Compressive Axis Excludes Q Cancellation

Combining §§8–9:

$$
\boxed{
H_{e,\delta}:Q
\ge
\frac{
\delta
}{4}
(
|S|^2+|\omega|^2
)
\ge
\frac{
\delta
}{4}
|Q|.
}
$$

Therefore, all:

$$
Q/|Q|
$$

fall into the same strict half-space.

Thus:

$$
\boxed{
\vartheta\ge\delta
+
e_1\equiv e
\Rightarrow
0\notin\operatorname{conv}\{Q/|Q|\}.
}
$$

### Conclusion

Merely allowing:

$$
e_2,e_3
$$

to rotate within $e^\perp$,

cannot generate a Seven-Point zero barycenter.

---

# 11. Axis-cap version

Now we do not require:

$$
e_1=e
$$

to be exact.

Assume:

$$
\boxed{
\angle(e_1,e)
\le
\alpha.
}
$$

Fix:

$$
\sigma
=
\delta/2.
$$

Define:

$$
\boxed{
H_{e,\sigma}
=
e\otimes e
-
\frac{
1+\sigma
}{2}
I.
}
$$

---

# 12. Strain lower bound in an axis cap

Let:

$$
\alpha
=
\angle(e_1,e).
$$

Since:

$$
S^2
$$

is positive semidefinite,

$$
e^TS^2e
\ge
\lambda_1^2
\cos^2\alpha.
$$

and:

$$
\lambda_1^2
\ge
|S|^2
\left(
\frac12+\delta
\right).
$$

therefore:

$$
H_{e,\sigma}:S^2
\ge
|S|^2
\left[
\left(
\frac12+\delta
\right)
\cos^2\alpha
-
\frac12
-
\frac{\delta}{4}
\right].
$$

That is:

$$
\boxed{
H_{e,\sigma}:S^2
\ge
|S|^2
\left[
\frac{3\delta}{4}
-
\left(
\frac12+\delta
\right)
\sin^2\alpha
\right].
}
$$

---

# 13. Axis-cap radius

If:

$$
\boxed{
\sin^2\alpha
\le
\frac{
\delta
}{
2+4\delta
},
}
$$

then:

$$
\left(
\frac12+\delta
\right)
\sin^2\alpha
\le
\frac{\delta}{4}.
$$

Thus:

$$
\boxed{
H_{e,\sigma}:S^2
\ge
\frac{
\delta
}{2}
|S|^2.
}
$$

Define:

$$
\boxed{
\alpha_\delta
=
\arcsin
\sqrt{
\frac{
\delta
}{
2+4\delta
}
}.
}
$$

---

# 14. Vorticity in the axis-cap test

For:

$$
\sigma=\delta/2,
$$

$$
H_{e,\sigma}
-
(\operatorname{tr}H_{e,\sigma})I
=
e\otimes e
+
\frac{\delta}{2}I.
$$

therefore:

$$
\boxed{
H_{e,\sigma}:
\frac14
(
\omega\otimes\omega
-
|\omega|^2I
)
\ge
\frac{
\delta
}{8}
|\omega|^2.
}
$$

---

# 15. C5-F.4: Axis-Cap Quadratic Half-Space Theorem

If:

$$
\boxed{
\vartheta\ge\delta>0
}
$$

and:

$$
\boxed{
\angle(e_1,e)
\le
\alpha_\delta,
}
$$

then:

$$
\boxed{
H_{e,\delta/2}:Q
\ge
\frac{
\delta
}{8}
(
|S|^2+|\omega|^2
)
\ge
\frac{
\delta
}{8}
|Q|.
}
$$

Thus:

$$
\boxed{
\textbf{all Q directions in one narrow compressive-axis cap
lie in a common strict half-space}.
}
$$

---

# 16. Projective compressive-axis space

Since:

$$
e
$$

and:

$$
-e
$$

generate the same projector,

the true axis state is:

$$
\boxed{
[e]\in\mathbb{RP}^2.
}
$$

Equivalently, use the:

$$
\boxed{
P=e\otimes e
}
$$

rank-one projector.

Its space is compact.

---

# 17. Q-weighted axis measure

In the active Q core,

define:

$$
\boxed{
\nu_j^{axis}
=
P_1(S_j)_\#
\nu_j^Q
}
$$

on:

$$
\mathbb{RP}^2.
$$

If:

$$
S=0
$$

on nonzero Q points,

use a cemetery state;

but the C5-E away-from-gap physical coercivity can control this branch.

---

# 18. C5-F.5: Nondegenerate Q Cancellation Forces Axis Anti-Concentration

Fix:

$$
\delta>0.
$$

Assume:

1. gap mass:
   $$
   \nu_j^Q\{\vartheta<\delta\}
   \to0;
   $$

2. quadratic coherence:
   $$
   \kappa_j^Q\to0.
   $$

Then for any projective axis:

$$
[e],
$$

it is impossible that:

$$
\nu_j^{axis}
\left(
B_{\alpha_\delta}([e])
\right)
\to1.
$$

More quantitatively,

there exists:

$$
c_\delta>0
$$

such that for large $j$:

$$
\boxed{
\sup_{[e]}
\nu_j^{axis}
\left(
B_{\alpha_\delta}([e])
\right)
\le
1-c_\delta
}
$$

after absorbing the small gap mass.

### Conclusion

$$
\boxed{
Q\text{-cancellation}
+
\text{nondegenerate gap}
\Rightarrow
\textbf{compressive-axis dispersion}.
}
$$

This is stronger than the full strain-direction dispersion in C5-E.

---

# 19. Common far-pressure axis condition

From C5-D:

the harmonic far-pressure leading matrix is:

$$
\boxed{
F\in\operatorname{Sym}_0(3).
}
$$

For a strong-middle coherent core,

if mean rotation is depleted,

the required oriented compensation is:

$$
\boxed{
G(e_1):F
=
e_1^TFe_1
\le
-c
}
$$

for:

$$
c>0.
$$

Therefore, the compressive axis must fall into:

$$
\boxed{
\Omega_F^-(c)
=
\{
[e]\in\mathbb{RP}^2:
e^TFe\le-c
\}.
}
$$

---

# 20. Far-pressure signature dichotomy

A nonzero trace-free symmetric:

$$
F
$$

has only two nondegenerate inertia types:

## Signature I

$$
\boxed{
(-,+,+).
}
$$

one negative eigenvalue.

## Signature II

$$
\boxed{
(-,-,+).
}
$$

two negative eigenvalues.

A zero eigenvalue is a boundary degeneration.

These two pressure-axis geometries are fundamentally different.

---

# 21. Signature $(-,+,+)$ gives projective cap locking

Let:

$$
f_1<0<f_2\le f_3
$$

be the eigenvalues,

$$
v_1
$$

be the unique negative eigenvector.

For a unit:

$$
e,
$$

let:

$$
\alpha
=
\angle(e,v_1)
$$

projectively.

Since:

$$
e^TFe
\ge
f_1\cos^2\alpha
+
f_2\sin^2\alpha,
$$

if:

$$
e^TFe
\le
-c,
$$

where:

$$
0<c<|f_1|,
$$

then:

$$
\boxed{
\sin^2\alpha
\le
\frac{
|f_1|-c
}{
|f_1|+f_2
}.
}
$$

---

# 22. Pressure cap radius

Define:

$$
\boxed{
\alpha_F(c)
=
\arcsin
\sqrt{
\frac{
|f_1|-c
}{
|f_1|+f_2
}
}.
}
$$

Then:

$$
\boxed{
\Omega_F^-(c)
\subset
B_{\alpha_F(c)}
([v_1]).
}
$$

Therefore, a strong negative pressure margin:

$$
c\uparrow|f_1|
$$

forces the compressive axes to lock into an arbitrarily narrow projective cap.

---

# 23. C5-F.6: Strong One-Negative Far Pressure vs Q-Cancellation Incompatibility

Assume:

1. Q-cancellation:
   $$
   \kappa_Q\to0;
   $$

2. nondegenerate middle gap:
   $$
   \vartheta\ge\delta>0
   $$
   on asymptotically full Q mass;

3. same common far matrix:
   $$
   F
   $$
   with signature:
   $$
   (-,+,+);
   $$

4. every active core requires:
   $$
   e_1^TFe_1\le-c<0;
   $$

5. pressure cap satisfies:
   $$
   \boxed{
   \alpha_F(c)
   <
   \alpha_\delta.
   }
   $$

Then this is impossible.

### Proof

The pressure condition locks all compressive axes into:

$$
B_{\alpha_F(c)}([v_1])
\subset
B_{\alpha_\delta}([v_1]).
$$

C5-F.4 places all Q directions into the same strict half-space.

Therefore, the Q barycenter cannot tend to zero. $\square$

---

# 24. Explicit margin criterion

The condition:

$$
\alpha_F(c)
<
\alpha_\delta
$$

is equivalent to:

$$
\boxed{
\frac{
|f_1|-c
}{
|f_1|+f_2
}
<
\frac{
\delta
}{
2+4\delta
}.
}
$$

That is:

$$
\boxed{
c
>
|f_1|
-
(
|f_1|+f_2
)
\frac{
\delta
}{
2+4\delta
}.
}
$$

Thus, there is an explicit:

$$
\boxed{
\textbf{pressure-margin vs middle-gap incompatibility threshold}.
}
$$

---

# 25. Signature $(-,-,+)$ does not force a cap

If:

$$
f_1\le f_2<0<f_3,
$$

the negative quadratic region contains a projective belt near the whole negative eigenspace.

Even if:

$$
e^TFe\le-c,
$$

the axes can still spread significantly within the two-dimensional negative subspace.

Therefore:

$$
\boxed{
\text{common pressure sign}
}
$$

does not by itself imply:

$$
\boxed{
\text{single-axis cap locking}.
}
$$

---

# 26. Pressure-signature escape

Thus, if nondegenerate-gap Q-cancellation is to coexist with common far pressure,

it must at least take:

## F-P1 — Weak pressure alignment

$$
c
$$

is insufficient to form a narrow cap.

## F-P2 — Two-negative-eigenvalue pressure

$$
\boxed{
\operatorname{sig}F=(-,-,+).
}
$$

## F-P3 — Far-pressure spectral degeneration

one eigenvalue:

$$
\to0,
$$

the signature approaches the boundary.

## F-P4 — Pressure-source fragmentation

different cores do not share a common dominant:

$$
F.
$$

## F-P5 — Mean rotation

pressure does not need to bear coherent quadratic forcing.

## F-P6 — Middle-gap degeneration

$$
\delta\to0
$$

causes the Q half-space margin to disappear.

---

# 27. Middle-gap does not remove F-axis condition

Even if:

$$
\delta\to0,
$$

C5-F.2 proves:

$$
P_1=e_1\otimes e_1
$$

remains stable.

And the far pressure pairing remains:

$$
\boxed{
G(e_1):F
=
e_1^TFe_1.
}
$$

Therefore:

$$
\boxed{
\text{middle-gap route}
}
$$

can only escape the:

$$
Q\text{-half-space margin},
$$

it cannot automatically escape the:

$$
\boxed{
\text{pressure-axis constraint}.
}
$$

This keeps the middle-gap / pressure motifs coupled.

---

# 28. Axis measure compactness through the gap

Since:

$$
\mathbb{RP}^2
$$

is compact,

any recurrent gap-degenerate sequence can still extract:

$$
\boxed{
\nu_j^{axis}
\rightharpoonup
\nu_\ast^{axis}.
}
$$

Therefore, the C5 limit can simultaneously record:

- gap defect:
  $$
  \vartheta=0;
  $$
- compressive-axis distribution:
  $$
  \nu_\ast^{axis}.
  $$

These two coordinates cannot be merged into a single "strain degeneracy".

---

# 29. Vorticity-dominant leakage

C5-E gives for the local core:

$$
B_R
$$

the critical vorticity stock:

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\int_{B_R}
|\omega|^2dx
\ge
w_0>0.
}
$$

Therefore:

$$
\boxed{
\int_{B_R}
|\omega|^2dx
\ge
w_0
\frac{
\nu^2
}{
R
}.
}
$$

---

# 30. C5-F.7: Vorticity Stock Forces Quadratic $L^2$ Congestion

By Hölder's inequality:

$$
\left(
\int_{B_R}
|\omega|^2
\right)^2
\le
|B_R|
\int_{B_R}
|\omega|^4.
$$

Therefore:

$$
\boxed{
\|\omega\|_{L^4(\mathbb R^3)}^2
\ge
c
w_0
\nu^2
R^{-5/2}.
}
$$

That is:

$$
\boxed{
\|\omega\otimes\omega\|_2
\ge
c
w_0
\nu^2
R^{-5/2}.
}
$$

---

# 31. Strain-space / complement split

Since:

$$
P_{st}
$$

is an $L^2$ orthogonal projection,

$$
\boxed{
\|\omega\otimes\omega\|_2^2
=
\|P_{st}(\omega\otimes\omega)\|_2^2
+
\|P_{st}^{\perp}(\omega\otimes\omega)\|_2^2.
}
$$

Therefore, at least:

## F-VOP

$$
\boxed{
\frac{
R^{5/2}
}{
\nu^2
}
\|
P_{st}(\omega\otimes\omega)
\|_2
\ge
c w_0,
}
$$

or:

## F-VCOMP

$$
\boxed{
\frac{
R^{5/2}
}{
\nu^2
}
\|
P_{st}^{\perp}(\omega\otimes\omega)
\|_2
\ge
c w_0.
}
$$

---

# 32. Meaning of F-VOP

$$
P_{st}(\omega\otimes\omega)
$$

is precisely the growth-orthogonal vorticity-quadratic source in the Miller operator architecture.

Therefore:

$$
\boxed{
\text{Vorticity Leakage}
\Rightarrow
\text{Miller Orthogonal Operator Congestion}
}
$$

in the F-VOP branch.

---

# 33. Meaning of F-VCOMP

$$
P_{st}^{\perp}(\omega\otimes\omega)
$$

is the constraint-space complement.

### Hard guard

It is not the:

$$
\boxed{
\text{actual pressure Hessian}
}
$$

itself.

The actual pressure is the full raw N–S nonlinearity projection complement,

and not solely the:

$$
\omega\otimes\omega
$$

complement.

Therefore, F-VCOMP can only be recorded as:

$$
\boxed{
\textbf{Constraint-Complement Congestion}.
}
$$

In the future, it must be coupled with:

- $S^2$;
- advection;
- pressure current.

---

# 34. Strain-derivative leakage

C5-E E-DER:

$$
\boxed{
\mathfrak H_R
=
\frac{
R^3
}{
\nu^2
}
\int_{B_{CR}}
|\nabla S|^2dx
\ge
h_0>0.
}
$$

Therefore:

$$
\boxed{
\int_{B_{CR}}
|\nabla S|^2
\ge
h_0
\frac{
\nu^2
}{
R^3
}.
}
$$

---

# 35. C5-F.8: Derivative Stock Forces Critical $D^2u$ Amplitude

By volume average,

there exists:

$$
x_R\in B_{CR}
$$

such that:

$$
|\nabla S(x_R)|
\ge
c
h_0^{1/2}
\frac{
\nu
}{
R^3
}.
$$

Since pointwise:

$$
|\nabla S|
\le
C
|D^2u|,
$$

we have:

$$
\boxed{
\|D^2u\|_{L^\infty(B_{CR})}
\ge
c
h_0^{1/2}
\frac{
\nu
}{
R^3
}.
}
$$

Therefore:

$$
\boxed{
\frac{
R^3
}{
\nu
}
\|D^2u\|_\infty
\gtrsim1.
}
$$

This is a scale-critical second-derivative amplitude.

---

# 36. Stock still does not give derivative geometry

C5-F.8 only gives:

$$
\boxed{
D^2u\text{ amplitude}
}
$$

it does not give:

$$
\boxed{
D^2u\text{ component/sign superlevel sparseness}.
}
$$

Therefore, we still cannot directly apply:

$$
\boxed{
\text{Grujić--Xu Theorem 3.5}.
}
$$

This hard guard remains.

---

# 37. Middle-gap cubic amplitude in NS-scaled coordinates

From C5-E:

$$
\|S\|_3^3
\ge
\frac{
M_\delta
}{
\sqrt6\,\delta
}.
$$

If on the ancestry scale $R$:

$$
b_R^{mid}
=
\frac{
R^3
}{
\nu^3
}
M_\delta
\ge
b_0,
$$

and:

$$
e_R^S
=
\frac{
R
}{
\nu^2
}
\|S\|_2^2
\le
E_0,
$$

then the effective amplitude:

$$
A_{\rm eff}
=
\frac{
\|S\|_3^3
}{
\|S\|_2^2
}
$$

satisfies:

$$
\boxed{
\widehat A_S
:=
\frac{
R^2
}{
\nu
}
A_{\rm eff}
\ge
c
\frac{
b_0
}{
E_0
}
\delta^{-1}.
}
$$

Thus:

$$
\boxed{
\frac{
R^2
}{
\nu
}
\|S\|_\infty
\gtrsim
\delta^{-1}.
}
$$

---

# 38. Middle-gap sparse scale

From C5-E:

$$
\boxed{
\frac{
r_{sp}
}{
R
}
\lesssim
\delta^{2/3}
\frac{
E_0
}{
b_0^{2/3}
}
}
$$

under fixed stock/load bounds.

Therefore, the middle-gap route generates:

$$
\boxed{
\text{amplitude}\sim\delta^{-1},
\qquad
\text{sparse scale}\sim\delta^{2/3}.
}
$$

---

# 39. Fixed-$k=1$ direct regularity scale comparison

Grujić–Xu Theorem 3.5,

velocity route:

$$
d=3,
\qquad
k=1,
$$

geometric scale exponent:

$$
\boxed{
\frac{
d
}{
2k+d
}
=
\frac35.
}
$$

In NS-rescaled coordinates,

if the raw gradient amplitude is comparable to the strain amplitude:

$$
\boxed{
\frac{
R^2
}{
\nu
}
\|\nabla u\|_\infty
\lesssim
C
\widehat A_S
\sim
\delta^{-1},
}
$$

then the theorem target normalized scale behaves as:

$$
\boxed{
\frac{
\rho_{\rm dir}
}{
R
}
\sim
\delta^{3/5}.
}
$$

Whereas the C5-E strain sparse scale is:

$$
\boxed{
\frac{
r_{sp}
}{
R
}
\lesssim
\delta^{2/3}.
}
$$

Since:

$$
\boxed{
\frac23>\frac35,
}
$$

for:

$$
0<\delta\ll1,
$$

$$
\boxed{
\delta^{2/3}
<
\delta^{3/5}.
}
$$

Therefore:

$$
\boxed{
\textbf{middle-gap intermittency has a formally favorable spatial exponent
relative to the fixed-}k=1\textbf{ direct scale}.
}
$$

---

# 40. The raw-gradient/vorticity interface

However:

$$
\nabla u
=
S
+
A(\omega),
$$

therefore:

$$
\|\nabla u\|_\infty
$$

can be much larger than:

$$
\|S\|_\infty
$$

due to vorticity.

If the raw derivative component:

$$
(\nabla u)_\ell^\pm
>
\lambda
\|\nabla u\|_\infty
$$

while:

$$
|\omega|
\le
\eta
\|\nabla u\|_\infty
$$

at that point,

then:

$$
|S|
\ge
c
(\lambda-C\eta)
\|\nabla u\|_\infty.
$$

Thus, the selected raw derivative high set can be contained within:

$$
\boxed{
\text{strain high set}
\cup
\text{vorticity-high defect set}.
}
$$

---

# 41. C5-F.9: Field-Conversion Dichotomy

Schematically,

for suitable thresholds:

$$
\boxed{
V_\lambda(Du)
\subset
E_{\lambda_S}(S)
\cup
E_{\eta}(\omega).
}
$$

Therefore, to legitimately convert strain sparseness into:

$$
D^1u
$$

component/sign sparseness,

one only needs to additionally control the vorticity high set.

### Conclusion

The field-conversion gap of C5-E can be rewritten as:

$$
\boxed{
\text{raw-velocity derivative gate}
\vee
\textbf{vorticity-geometry defect}.
}
$$

This exactly connects with the E-VORT branch.

---

# 42. Direct-gate pre-closure

Thus, if the middle-gap branch simultaneously satisfies:

1. bounded normalized strain stock;
2. nondegenerate middle load;
3. sufficiently small gap:
   $$
   \delta\ll1;
   $$
4. the vorticity high set does not destroy union sparsity at the same scale;
5. full-space / component-sign conversion holds;
6. the geometry appears at a Theorem 3.5 admissible later time;

then the C5-E sparse scale is no worse in exponent than the:

$$
k=1
$$

direct target.

### Status

$$
\boxed{
\mathrm{SCALING\mbox{-}FAVORABLE\ CONDITIONAL\ INTERFACE}.
}
$$

It is not a theorem application.

---

# 43. Chain-assisted scale

Grujić–Xu Theorem 3.14 velocity scale:

$$
\boxed{
\rho_{\rm chain}^{(k)}
\sim
\|D^ku\|_\infty^{-1/(k+1)}.
}
$$

For a formal:

$$
k=1
$$

amplitude:

$$
\sim\delta^{-1},
$$

normalized target:

$$
\sim
\delta^{1/2}.
$$

From C5-E:

$$
r_{sp}/R
\sim
\delta^{2/3}
<
\delta^{1/2}.
$$

Therefore, the spatial exponent is also favorable.

### Hard guard

Theorem 3.14 is not a standalone $k=1$ sparseness theorem.

It involves:

- sufficiently high derivative hierarchy;
- ascending/descending chains;
- later analytic time;
- all stated constants/hypotheses.

Therefore, this can only be called:

$$
\boxed{
\textbf{formal chain-scale compatibility}.
}
$$

---

# 44. Derivative-order selection

For each recurrent event:

$$
j,
$$

let:

$$
\boxed{
k_j^{best}
}
$$

be the most favorable derivative order we select based on:

- available amplitude;
- available sparseness;
- field conversion;
- theorem time gate;
- chain status.

We do not assume:

$$
k_j^{best}
$$

is necessarily unique.

Fix a deterministic tie-break.

---

# 45. C5-F.10: Fixed-Order Recurrence or Derivative-Order Escape

Any:

$$
k_j^{best}\in\mathbb N
$$

sequence has a subsequence satisfying:

## F-KFIX

$$
\boxed{
k_j^{best}
=
k_\ast
}
$$

eventually,

or:

## F-KINF

$$
\boxed{
k_j^{best}
\to\infty.
}
$$

### Proof

Elementary subsequence dichotomy of $\mathbb N$. $\square$

### Significance

$$
\boxed{
\text{repeated low-order failure}
}
$$

does not automatically imply:

$$
\boxed{
k\to\infty.
}
$$

unless all fixed-order recurrent defect motifs are independently excluded.

---

# 46. Fixed-order defect stabilization

If:

$$
k_j^{best}=k_\ast
$$

along a subsequence,

the C5-A derivative defect vector:

$$
d_j^{der}
\in
\{0,1\}^{4}
$$

can be made eventually constant by extracting a further subsequence.

Thus, we obtain a:

$$
\boxed{
\textbf{Fixed-Order Recurrent Gate Defect}.
}
$$

For example, permanent:

- MULT;
- SHELLFULL;
- TIMECHAIN;
- COMPSIGN.

This is a compact motif that can be directly attacked in the next stage of C5.

---

# 47. Derivative-order escape

If:

$$
k_j^{best}\to\infty,
$$

the Grujić–Xu direct exponent:

$$
\boxed{
\alpha_k^{dir}
=
\frac{
3
}{
2k+3
}
\to0,
}
$$

and the chain exponent:

$$
\boxed{
\alpha_k^{chain}
=
\frac1{k+1}
\to0.
}
$$

Its framework precisely proves:

$$
\boxed{
\text{regularity/a-priori scaling gap asymptotically vanishes}
}
$$

as:

$$
k\to\infty.
$$

---

# 48. But derivative-order escape is not regularity

Even if:

$$
k_j\to\infty,
$$

it may still fail at each generation due to:

- component/sign conversion;
- later analytic time;
- derivative chain;
- spatial carrier mismatch;
- effective multiplicity.

Therefore:

$$
\boxed{
k_j\to\infty
}
$$

is merely an:

$$
\boxed{
\textbf{Asymptotically-Critical Boundary Motif}.
}
$$

It is not a contradiction.

---

# 49. C5-F residual network

C5-E residual:

$$
\text{Gap}
\vee
\text{Derivative}
\vee
\text{Vorticity}.
$$

After C5-F:

## Gap branch

$$
\boxed{
\text{Gap Intermittency}
+
\text{persistent compressive-axis metadata}.
}
$$

If the common far pressure one-negative strongly locks axes,

it is incompatible with nondegenerate-gap Q cancellation.

## Vorticity branch

$$
\boxed{
\text{Miller Orthogonal Operator}
\vee
\text{Constraint-Complement Congestion}.
}
$$

## Derivative branch

$$
\boxed{
\text{critical }D^2u\text{ amplitude}
+
\text{fixed-order defect}
\vee
\text{order escape}.
}
$$

---

# 50. Second finite-dimensional incompatibility

The first from C5-D:

$$
\boxed{
\text{Strong-Middle Full Strain Cone}
\cap
\text{Q Zero-Barycenter}
=
\varnothing.
}
$$

The second from C5-F:

$$
\boxed{
\text{Nondegenerate Middle Gap}
+
\text{Strong One-Negative Common Far-Pressure Axis Lock}
+
\text{Q Zero-Barycenter}
=
\varnothing.
}
$$

Here, we no longer require the full strain direction to be locked in a single cone;

we only require:

$$
\boxed{
\textbf{compressive axis itself is locked}.
}
$$

This is a stronger motif incompatibility.

---

# 51. Why this matters

One might originally imagine for Q cancellation:

> Fixing the most-compressive axis,
> and merely letting the other two eigenvectors / eigenvalues rotate randomly,
> should be enough to cancel out the quadratic directions, right?

C5-F proves:

$$
\boxed{
\textbf{No — as long as the middle gap has a fixed positive margin.}
}
$$

Q cancellation truly requires:

$$
\boxed{
\textbf{compressive-axis dispersion}
}
$$

or:

$$
\boxed{
\textbf{middle-gap collapse}.
}
$$

And pressure compensation happens to also look at:

$$
\boxed{
\textbf{the same compressive axis}.
}
$$

Therefore, the two residual motifs of Q / Pressure now share a truly finite-dimensional order parameter:

$$
\boxed{
[e_1]\in\mathbb{RP}^2.
}
$$

---

# 52. New C5 shared state

Define:

$$
\boxed{
\Theta_\ast^{Axis}
=
\left\langle
\nu_\ast^{axis},
\mathfrak G_\ast,
F_\ast,
\operatorname{sig}F_\ast,
c_\ast^P,
\mathfrak C_\ast^{axis}
\right\rangle.
}
$$

where:

- $\nu_\ast^{axis}$ = compressive-axis probability;
- $\mathfrak G_\ast$ = middle-gap defect mass;
- $F_\ast$ = normalized common far-pressure matrix metadata;
- signature = pressure inertia type;
- $c_\ast^P$ = pressure alignment margin;
- $\mathfrak C_\ast^{axis}$ = cap / convex-hull concentration statistic.

---

# 53. Axis concentration statistic

Define:

$$
\boxed{
\mathfrak C_{\rm axis}(\alpha)
=
\sup_{[e]\in\mathbb{RP}^2}
\nu_\ast^{axis}
(
B_\alpha([e])
).
}
$$

If:

$$
\mathfrak C_{\rm axis}(\alpha_\delta)=1,
$$

and the gap:

$$
\ge\delta,
$$

a Q zero barycenter is impossible.

If Q cancellation is active:

$$
\boxed{
\mathfrak C_{\rm axis}(\alpha_\delta)
\le
1-c_\delta.
}
$$

unless middle-gap mass intervenes.

---

# 54. Pressure axis-locking statistic

A signature:

$$
(-,+,+)
$$

common far matrix with margin:

$$
c
$$

forces:

$$
\boxed{
\mathfrak C_{\rm axis}
(
\alpha_F(c)
)
=
1.
}
$$

Therefore, if:

$$
\alpha_F(c)<\alpha_\delta,
$$

it directly conflicts with the Q cancellation limit.

---

# 55. X-Integration guards update

## G-AXROB

Middle-gap degeneration must not delete compressive-axis metadata.

## G-AXCAP

Q cancellation under a nondegenerate gap must preserve axis anti-concentration.

## G-PSIG

The common far-pressure matrix must preserve its eigenvalue signature.

## G-PCAP

Only signature $(-,+,+)$ + strong negative margin can escalate into a single projective cap.

## G-PBELT

Signature $(-,-,+)$ only gives a negative-plane/belt geometry,

and must not be falsely claimed as axis locking.

## G-VPROJ

Vorticity L2 stock first converts to raw $\omega\otimes\omega$ L2,

then splits into $P_{st}$ / complement.

## G-PCOMPNEQ

$P_{st}^{\perp}(\omega\otimes\omega)$ must not be called the actual pressure.

## G-KESC

Repeated derivative gate failure must not directly imply $k\to\infty$.

## G-GXSCALE

Scaling-favorable does not equal theorem-ready.

---

# 56. True ETN update

C5-F state:

$$
\boxed{
\Theta_\ast^{F}
=
\left\langle
\nu_\ast^{axis},
\mathfrak G_\ast,
F_\ast,
\operatorname{sig}F_\ast,
c_\ast^P,
\mathfrak V_\ast^{op,\omega},
\mathfrak V_\ast^{\perp,\omega},
k_\ast^{best},
d_\ast^{der}
\right\rangle.
}
$$

---

# 57. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal Young oscillation/concentration}.
$$

C5-C:

$$
\text{temporal cross-curvature constraints}.
$$

C5-D:

$$
\text{Strong-Middle vs Q-cancellation incompatibility}.
$$

C5-E:

$$
Q
\to
\text{Gap/Derivative/Vorticity field defects}.
$$

C5-F:

$$
\boxed{
\textbf{Gap preserves pressure axis;
Q cancellation forces axis dispersion;
strong one-negative far pressure can force the opposite.}
}
$$

Meanwhile, the derivative route is organized into:

$$
\boxed{
\text{fixed-order recurrent defect}
\vee
\text{asymptotically-critical order escape}.
}
$$

---

# 58. What remains unresolved

## 1. Pressure signature $(-,-,+)$

The negative-plane geometry may still accommodate axis dispersion and Q cancellation.

## 2. Middle-gap + one-negative pressure

Gap collapse causes the Q half-space margin to disappear,

so a strong axis lock can coexist with gap intermittency.

## 3. Vorticity complement

Constraint-complement congestion has not yet been coupled with actual pressure / advection.

## 4. Derivative theorem gate

Scaling becomes favorable,

but the field/component/sign/time/chain interfaces remain.

---

# 59. New frontier: C5-G

Formally the next topic:

$$
\boxed{
\textbf{C5-G — Pressure-Signature Defects,
Vorticity Constraint Complements,
and Fixed-Order Derivative-Gate Closure}.
}
$$

---

# 60. C5-G proof obligations

## G1 — Two-negative pressure geometry

For:

$$
\operatorname{sig}F=(-,-,+),
$$

investigate whether the negative-plane axis distribution and Q cancellation can still coexist without restriction.

## G2 — Pressure signature transitions

If the recurrent common pressure switches between:

$$
(-,+,+)
\leftrightarrow
(-,-,+)
$$

it must cross:

$$
\det F=0.
$$

Investigate the signature-transition defect / eigenvalue-zero congestion.

## G3 — Gap × pressure signature

Whether the middle-gap defect and the pressure signature boundary synchronously form a compact recurrent motif.

## G4 — Vorticity constraint complement

Place:

$$
P_{st}^{\perp}(\omega\otimes\omega)
$$

and:

- $S^2$ complement;
- advection complement;
- actual pressure Hessian;

into the same orthogonal ledger.

## G5 — Fixed $k=1$ gate

When the vorticity-high-set is not dominant,

strictly measure the union-sparseness constants of:

$$
\text{strain sparse}
\to
D u\text{ component/sign sparse}
$$

## G6 — Fixed $k=2$ gate

From:

$$
\mathfrak H_R
$$

and additional active-volume data,

measure the Theorem 3.5 $k=2$ scale.

## G7 — Fixed-order defect elimination

Process one by one:

- SHELLFULL;
- COMPSIGN;
- TIMECHAIN;
- MULT.

If a certain fixed order is completely closed,

the hypothetical survivor is excluded.

## G8 — Escalation audit

Only when all fixed-order defects can no longer be recurrently borne,

is it legitimate to send the research route to:

$$
k_j\to\infty.
$$

---

# 61. Formal status

$$
\boxed{
\begin{aligned}
\text{uniform compressive spectral gap}
&:\ \mathrm{PROVED},\\
\text{middle-gap preserves compressive axis}
&:\ \mathrm{PROVED},\\
\text{fixed-axis + gap}\Rightarrow Q\text{ half-space}
&:\ \mathrm{PROVED},\\
\text{axis-cap + gap}\Rightarrow Q\text{ half-space}
&:\ \mathrm{PROVED},\\
Q\text{-cancellation + gap}\Rightarrow\text{axis dispersion}
&:\ \mathrm{PROVED},\\
(-,+,+)\text{ far pressure}\Rightarrow\text{axis cap}
&:\ \mathrm{PROVED},\\
\text{strong cap pressure + gap + Q cancellation}
&:\ \mathrm{INCOMPATIBLE},\\
(-,-,+)\text{ far pressure}\Rightarrow\text{single cap}
&:\ \mathrm{FALSE},\\
\text{vorticity stock}\Rightarrow\omega\otimes\omega\ L^2\text{ congestion}
&:\ \mathrm{PROVED},\\
\text{vorticity congestion}\Rightarrow
P_{st}\text{ or complement}
&:\ \mathrm{PROVED},\\
\text{strain derivative stock}\Rightarrow D^2u\text{ critical amplitude}
&:\ \mathrm{PROVED},\\
\text{middle-gap sparse exponent vs fixed }k=1\text{ scale}
&:\ \mathrm{FAVORABLE\ CONDITIONAL},\\
\text{raw }Du\text{ gate}\vee\text{vorticity geometry defect}
&:\ \mathrm{PROVED\ STRUCTURAL},\\
\text{fixed order or }k\to\infty\text{ subsequence}
&:\ \mathrm{PROVED},\\
k\to\infty\Rightarrow\text{regularity}
&:\ \mathrm{FALSE/NOT\ PROVED},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 62. Conclusion

C5-E translates Q cancellation into:

$$
\text{Gap}
\vee
\text{Derivative}
\vee
\text{Vorticity}.
$$

C5-F now couples these three branches further with pressure / derivative theorem geometry.

First,

the middle gap does not destroy the most-compressive axis.

For normalized positive-middle strain:

$$
\boxed{
\lambda_2-\lambda_1
\ge
1/\sqrt2.
}
$$

Therefore:

$$
e_1\otimes e_1
$$

remains stable even when:

$$
\lambda_2/|S|\to0
$$

Second,

if the gap:

$$
\vartheta\ge\delta
$$

does not degenerate,

as long as the compressive axes stay in the cap:

$$
\boxed{
\sin^2\angle(e_1,e)
\le
\frac{
\delta
}{
2+4\delta
},
}
$$

there exists a common matrix functional such that:

$$
\boxed{
H:Q
\gtrsim
\delta|Q|.
}
$$

Therefore:

$$
\boxed{
Q\text{-cancellation}
+
\text{nondegenerate gap}
\Rightarrow
\textbf{compressive-axis dispersion}.
}
$$

Third,

if the common harmonic far pressure has the signature:

$$
(-,+,+)
$$

and the negative compensation margin is sufficiently strong,

it instead forces the compressive axes to fall into a single projective cap.

If the cap is narrower than the Q-cancellation threshold above,

we obtain the second finite-dimensional incompatibility:

$$
\boxed{
\text{Strong One-Negative Pressure Axis Lock}
+
\text{Nondegenerate Gap}
+
\text{Q Zero Barycenter}
=
\varnothing.
}
$$

Therefore, the pressure survivor must take:

$$
\boxed{
\text{weak margin}
\vee
(-,-,+)\text{ signature}
\vee
\text{signature degeneration}
\vee
\text{source fragmentation}
\vee
\text{mean rotation}
\vee
\text{middle-gap collapse}.
}
$$

Fourth,

vorticity leakage is now also sent back to the operator architecture:

$$
\boxed{
\text{Vorticity Leakage}
\Rightarrow
P_{st}(\omega\otimes\omega)
\vee
P_{st}^{\perp}(\omega\otimes\omega).
}
$$

Fifth,

strain-derivative leakage gives:

$$
\boxed{
R^3\|D^2u\|_\infty/\nu
\gtrsim1.
}
$$

And middle-gap cubic intermittency already exhibits a favorable relation in the normalized spatial exponent relative to the fixed-$k=1$ direct sparseness scale.

However, the published Grujić–Xu theorem still requires true:

$$
D^ku
\text{ / }
D^k\omega
$$

component/sign, later time, and chain conditions, so one still cannot skip levels.

Finally,

the only truly correct logic for derivative escalation is:

$$
\boxed{
\textbf{Fixed-Order Recurrent Defect}
\vee
\textbf{Derivative Order }k_j\to\infty.
}
$$

Only after systematically killing off all fixed-order defects,

is one qualified to truly send the survivor route to:

$$
k\to\infty
$$

the asymptotically-critical boundary of.

Formally the next paper:

$$
\boxed{
\textbf{C5-G — Pressure-Signature Defects,
Vorticity Constraint Complements,
and Fixed-Order Derivative-Gate Closure}.
}
$$

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026).
2. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
3. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
4. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.

# Internal dependencies

- `NS_C5E_StrainDirection_MiddleGap_DerivativeIntermittency_v0.1.md`
- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3S_StrainConeMargin_MergerRigidity_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-G — Pressure-Signature Defects,
Vorticity Constraint Complements,
and Fixed-Order Derivative-Gate Closure}
}
$$