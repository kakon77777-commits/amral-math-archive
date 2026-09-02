---
title: "Navier–Stokes C6-Q: Ancient Defect Rigidity, Local Growth Lift, Strain-Projection Tail Reduction, and Spatial Carrier Rebinding"
subtitle: "The H¹ Strain-Growth Ledger Has a Fully Local Representative, So the Projected-Operator Tail Is Not an Intrinsic TS Carrier Obstruction; P_st Far Tails Are Locally Constant Modulo Vanishing Oscillation; Spatial Carrier Escape Rebinds to Satellite Ancient Profiles"
version: "v0.1"
date: "2026-08-16"
author: "Neo.K / EveMissLab"
language: "en"
status: "C6 ancient-defect rigidity / TS lift correction / P_st tail audit / satellite ancient profiles"
epistemic_status: "Exact strain-growth identities, an explicit derived P_st projection formula, Calderón–Zygmund tail-oscillation bounds, and translation/time-shift compactness reductions. The local operator lift is a chosen exact representative, not a unique canonical lift. Does NOT prove all ancient defect states trivial and does NOT prove Navier–Stokes global regularity."
---

# Navier–Stokes C6-Q
# Ancient Defect Rigidity, Local Growth Lift, Strain-Projection Tail Reduction, and Spatial Carrier Rebinding

## 0. Current Round Positioning

C6-P compressed the frontier of the record-amplitude ancient peak into:

$$
\boxed{
\text{FLAT}
\vee
GP_{\rm loc}^{anc}
\vee
HF_{k,\rm geom}^{anc}
\vee
TS_{\rm loc/proj}^{anc}
\vee
\text{Spatial Carrier Escape}
\vee
\text{Order-Geometry Escape}.
}
$$

Among these, it has already been proven that:

1. fixed-order derivative tower:
   $$
   \boxed{\text{NO-GO}};
   $$
2. peak flattening:
   $$
   \boxed{
   v_\infty\equiv b
   }
   $$
   by backward uniqueness;
3. pressure Hessian remote tail:
   $$
   \boxed{
   O(R^{-2});
   }
   $$
4. what truly remains for fixed-order high derivatives is:
   $$
   \boxed{
   \text{local capture}
   \vee
   \text{spatial carrier escape};
   }
   $$
5. the seemingly most difficult ancient label in C6-P is:
   $$
   TS,
   $$
   because:
   $$
   P_{st}
   $$
   is a zero-order nonlocal projection.

C6-Q now discovers a major correction:

> **For the temporal positive \(H^1\)-growth ledger actually used by TS,
> \(P_{st}\) is not an intrinsic spatial-carrier object.**

Miller's exact identity:

$$
\boxed{
\langle-\Delta S,\omega\otimes\omega\rangle=0
}
$$

combined with:

$$
-\Delta S\in L^2_{st}
$$

allows:

$$
P_{st}
$$

to be removed from the entire growth pairing.

Thus, the TS operator temporal load can be represented by a **fully local** signed density.

Main results of this round:

1. Correction to C6-E:
   $$
   \boxed{
   \text{the spatial lift of the operator temporal marginal is not a unique canonical object};
   }
   $$
2. Definition of:
   $$
   \boxed{
   \textbf{Projected Representative Lift};
   }
   $$
3. Definition of the new:
   $$
   \boxed{
   \textbf{Local Growth Representative Lift};
   }
   $$
4. exact identity:
   $$
   \boxed{
   E_1'
   =
   \int
   g_O^{loc};
   }
   $$
5. :
   $$
   g_O^{loc}
   $$
   is fully local in:
   $$
   u,\nabla u,\nabla^2u,\nabla^3u;
   $$
6. Therefore:
   $$
   \boxed{
   \textbf{Projected-Operator Tail is deleted as an intrinsic TS growth-carrier obstruction};
   }
   $$
7. C6-E/F spatial-overlap statements must be tagged with their operator-lift provenance;
8. Reconstruct using the local lift:
   $$
   \Pi_O^{loc},
   \Omega_{ST}^{loc},
   \Pi_{\cap}^{loc};
   $$
9. TS ancient inheritance can therefore be rewritten as a local spacetime convergence problem;
10. But the Miller operator-**norm** criterion still genuinely depends on:
    $$
    Q_{SV}=P_{st}F;
    $$
11. So:
    $$
    \boxed{
    \text{growth carrier}
    \neq
    \text{operator norm carrier};
    }
    $$
12. Derive from the Miller–Sawyer strain isometry the explicit formula:
    $$
    \boxed{
    P_{st}M
    =
    -2\nabla_{\rm sym}
    (-\Delta)^{-1}
    P_{df}\operatorname{div}M;
    }
    $$
13. Therefore:
    $$
    P_{st}
    $$
    is a homogeneous degree-zero Calderón–Zygmund matrix operator;
14. its kernel:
    $$
    K_{st}(x)
    =
    |x|^{-3}\Omega(x/|x|);
    $$
15. gradient:
    $$
    |\nabla K_{st}(x)|
    \lesssim
    |x|^{-4};
    $$
16. For a bounded source far tail:
    $$
    \boxed{
    \text{tail oscillation on a fixed core}
    \lesssim
    R_0/R;
    }
    $$
17. So:
    $$
    \boxed{
    \textbf{P_st far tail is locally constant modulo vanishing oscillation};
    }
    $$
18. ancient operator norm tail therefore reduces to:
    - finite-radius projected source;
    - constant STF matrix background;
    - vanishing oscillatory remainder;
19. the constant background for the localized:
    $$
    -\Delta S
    $$
    pairing acts only through cutoff boundary/annulus coupling;
20. Thus, the nonlocal tail is not an arbitrary infinite-dimensional core forcing;
21. Spatial Carrier Escape is also not terminal:
    translate/recenter a defect carrier escaping:
    $$
    |z_n|\to\infty;
    $$
22. record peak boundedness + smoothing gives compactness after translation;
23. any nonzero local absolute defect load yields a:
    $$
    \boxed{
    \textbf{Satellite Bounded Ancient Defect Profile};
    }
    $$
24. fixed-order HF spatial escape therefore rebinds to:
    $$
    HF^{anc}_{sat};
    $$
25. GP spatial escape rebinds to:
    $$
    GP^{anc}_{sat}
    $$
    after pressure provenance repartition;
26. TS local-growth carrier spatial escape rebinds to:
    $$
    TS^{anc}_{sat}
    $$
    without a \(P_{st}\)-tail obstacle;
27. physical center:
    $$
    X_n=x_n+a_nz_n
    $$
    has its own trichotomy;
28. ancient-time recurrent local defects:
    $$
    \tau_j\to-\infty
    $$
    can be time/space shifted;
29. bounded ancient smoothing then yields a conditional:
    $$
    \boxed{
    \textbf{bounded eternal defect profile};
    }
    $$
30. general 3D bounded eternal/ancient Liouville remains open;
31. but:
    - \(L^3\)-bounded backward sequence;
    - FLAT;
    - special symmetry;
    - other known ancient rigidity classes;
    remain external kill gates;
32. C6-Q ancient frontier becomes:
    $$
    \boxed{
    GP^{anc}
    \vee
    HF^{anc}_{fixed}
    \vee
    TS^{anc}_{local}
    \vee
    \text{ORDER-GEOMETRY}
    \vee
    \text{ETERNAL-DEFECT}
    \vee
    \text{OPERATOR-CONSTANT-MODE}.
    }
    $$

---

# 1. Fresh primary-source audit

## 1.1 Miller strain-vorticity identity

Miller proves:

$$
\boxed{
\left\langle
-\Delta S,
\omega\otimes\omega
\right\rangle
=
0.
}
$$

The same paper writes the strain equation using:

$$
P_{st},
$$

and derives critical regularity criteria involving:

$$
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
$$

Thus the paper already distinguishes:

- exact \(H^1\)-growth pairing;
- the full projected operator norm.

C6-Q exploits this distinction.

## 1.2 Miller–Sawyer strain projection

Miller–Sawyer define:

$$
L^2_{st}
=
\nabla_{\rm sym}
(-\Delta)^{-1/2}
L^2_{df},
$$

and prove the isometry:

$$
\boxed{
\|
\nabla_{\rm sym}
(-\Delta)^{-1/2}u
\|_2^2
=
\frac12
\|u\|_2^2.
}
$$

They also prove a Helmholtz-type decomposition for symmetric matrices and a projection-size identity:

$$
\boxed{
\|P_{st}M\|_2^2
=
2
\|
\nabla\times
\operatorname{div}
(-\Delta)^{-1}M
\|_2^2.
}
$$

This provides the functional-analytic basis for the projection formula derived below.

## 1.3 Bounded ancient profiles

Koch–Nadirashvili–Seregin–Šverák study bounded ancient N–S solutions and show the general 3D Liouville problem remains open.

Thus satellite/eternal profile extraction is a legitimate reduction, not an automatic contradiction.

## 1.4 Backward uniqueness

Lei–Yang–Yuan prove backward uniqueness for bounded mild whole-space 3D N–S solutions with nontrivial final data.

C6-P already used this to eliminate the FLAT ancient branch.

## 1.5 Type-II alternative interface

Seregin's 2026 Type-II work studies specific local Type-II scenarios by Euler scaling.

C6-Q retains this as a scenario-dependent external route and does not merge it with the record-peak ancient N–S route.

---

# 2. Exact strain evolution

For viscosity:

$$
\nu>0,
$$

the strain equation is:

$$
\boxed{
\partial_tS
-
\nu\Delta S
+
P_{st}
\left(
(u\cdot\nabla)S
\right)
+
P_{st}
\left(
S^2
+
\frac14
\omega\otimes\omega
\right)
=
0.
}
$$

Because:

$$
S\in L^2_{st},
$$

also:

$$
\boxed{
-\Delta S\in L^2_{st}.
}
$$

---

# 3. $H^1$ strain energy

Define:

$$
\boxed{
E_1(t)
=
\frac12
\|S(t)\|_{\dot H^1}^2
=
\frac12
\|\nabla S(t)\|_2^2.
}
$$

Pair the strain equation with:

$$
-\Delta S.
$$

Then:

$$
\boxed{
E_1'
+
\nu
\|\Delta S\|_2^2
+
\left\langle
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac14\omega\otimes\omega
\right),
-\Delta S
\right\rangle
=
0.
}
$$

---

# 4. Projection removal in the pairing

Because:

$$
P_{st}
$$

is the orthogonal projection onto:

$$
L^2_{st},
$$

and:

$$
-\Delta S\in L^2_{st},
$$

for any admissible symmetric matrix field:

$$
F,
$$

$$
\boxed{
\langle P_{st}F,-\Delta S\rangle
=
\langle F,-\Delta S\rangle.
}
$$

---

# 5. Vorticity orthogonality

Miller proves:

$$
\boxed{
\langle
-\Delta S,
\omega\otimes\omega
\rangle
=
0.
}
$$

Therefore:

$$
\boxed{
\left\langle
P_{st}
\left(
\frac14
\omega\otimes\omega
\right),
-\Delta S
\right\rangle
=
0.
}
$$

---

# 6. C6-Q.1: Projection-Free $H^1$ Growth Identity

Combining §§3–5:

$$
\boxed{
E_1'
=
-
\nu
\|\Delta S\|_2^2
-
\left\langle
(u\cdot\nabla)S
+
S^2,
-\Delta S
\right\rangle.
}
$$

Equivalently:

$$
\boxed{
E_1'(t)
=
\int_{\mathbb R^3}
g_O^{loc}(t,x)\,dx,
}
$$

where:

$$
\boxed{
g_O^{loc}
=
-
\left[
(u\cdot\nabla)S
+
S^2
\right]
:
(-\Delta S)
-
\nu
|\Delta S|^2.
}
$$

---

# 7. Locality

The density:

$$
g_O^{loc}
$$

depends pointwise on:

- velocity;
- first derivatives through:
  $$
  S;
  $$
- second/third derivatives through:
  $$
  (u\cdot\nabla)S,\Delta S.
  $$

There is no:

$$
P_{st}
$$

or pressure singular integral in the formula.

Thus:

$$
\boxed{
\textbf{$H^1$ growth has a fully local exact spatial representative}.
}
$$

---

# 8. Correction to C6-E terminology

C6-E previously introduced:

$$
g_O^{proj}
=
-
Q_{SV}:(-\Delta S)
-
\nu|\Delta S|^2,
$$

and called the induced positive operator spacetime lift “canonical”.

That word is too strong.

Both:

$$
g_O^{proj}
$$

and:

$$
g_O^{loc}
$$

integrate to the same temporal net growth:

$$
E_1'.
$$

Their positive parts need not have the same spatial distribution.

Therefore:

# 9. C6-Q.2: Operator-Lift Nonuniqueness Guard

$$
\boxed{
\textbf{a temporal operator-growth marginal does not determine a unique positive spatial lift}.
}
$$

Every spatial-overlap theorem must store the chosen **lift provenance**.

---

# 10. Lift labels

C6-Q defines:

## Q-LIFT-P

$$
\boxed{
\textbf{Projected Representative Lift}
}
$$

using:

$$
g_O^{proj}.
$$

## Q-LIFT-L

$$
\boxed{
\textbf{Local Growth Representative Lift}
}
$$

using:

$$
g_O^{loc}.
$$

The two are different carrier models of the same temporal marginal.

---

# 11. Local positive operator capacity

Define:

$$
\boxed{
c_O^{loc}(t)
=
\int
[g_O^{loc}(t,x)]_+dx.
}
$$

Since:

$$
E_1'
=
\int
g_O^{loc},
$$

$$
\boxed{
[E_1']_+
\le
c_O^{loc}.
}
$$

---

# 12. Local conditional operator probability

On:

$$
[E_1'(t)]_+>0,
$$

define:

$$
\boxed{
p_O^{loc}(x|t)
=
\frac{
[g_O^{loc}(t,x)]_+
}{
c_O^{loc}(t)
}.
}
$$

This is a spatial probability density.

---

# 13. Local operator spacetime lift

For a record window:

$$
J,
$$

let:

$$
P_J
=
\int_J
[E_1']_+dt>0.
$$

Define:

$$
d\mu_J^O(t)
=
\frac{
[E_1'(t)]_+
}{
P_J
}dt.
$$

Then:

$$
\boxed{
d\Pi_{J}^{O,loc}(t,x)
=
d\mu_J^O(t)
p_O^{loc}(x|t)dx.
}
$$

Its temporal marginal is exactly:

$$
\boxed{
(\pi_t)_\#
\Pi_J^{O,loc}
=
\mu_J^O.
}
$$

---

# 14. Local TS overlap

Middle lift:

$$
\Pi_J^M
$$

is unchanged.

Define:

$$
\boxed{
\Omega_{ST}^{loc}
=
1-
d_{TV}
(
\Pi_J^M,
\Pi_J^{O,loc}
).
}
$$

If:

$$
\Omega_{ST}^{loc}>0,
$$

define:

$$
\boxed{
\Pi_J^{\cap,loc}
=
\frac{
\Pi_J^M
\wedge
\Pi_J^{O,loc}
}{
\Omega_{ST}^{loc}
}.
}
$$

This is a fully local TS shared-source representative.

---

# 15. C6-Q.3: Projected-Tail Deletion for the TS Growth Carrier

All C6-E/F arguments which require only:

- temporal middle load;
- temporal positive:
  $$
  E_1'
  $$
  load;
- a chosen positive spatial operator-growth representative;

may be rebuilt using:

$$
\boxed{
\Pi_J^{O,loc}.
}
$$

Therefore:

$$
\boxed{
\textbf{the nonlocal }P_{st}\textbf{ tail is not an intrinsic obstruction to TS growth-carrier localization}.
}
$$

### Important

This deletes the **carrier-tail** problem,

not every use of:

$$
P_{st}.
$$

---

# 16. What remains genuinely projected

Miller's critical operator criterion uses:

$$
\boxed{
Q_{SV}
=
P_{st}
\left(
(u\cdot\nabla)S
+
S^2
+
\frac34
\omega\otimes\omega
\right).
}
$$

The quantities:

$$
\|Q_{SV}\|_{\dot H^\alpha}
$$

and:

$$
\|Q_{SV}\|_2
$$

are genuine projected norms.

They are not determined by:

$$
g_O^{loc}.
$$

Thus:

$$
\boxed{
\textbf{Growth Carrier}
\neq
\textbf{Operator-Norm Carrier}.
}
$$

This distinction is mandatory from C6-Q onward.

---

# 17. Strain-space operator

Let:

$$
\boxed{
T
:
L^2_{df}
\to
L^2_{\rm sym}
}
$$

be:

$$
\boxed{
Tu
=
\nabla_{\rm sym}
(-\Delta)^{-1/2}u.
}
$$

Miller–Sawyer prove:

$$
\boxed{
T^\ast T
=
\frac12
I
}
$$

on:

$$
L^2_{df}.
$$

---

# 18. Adjoint

For symmetric:

$$
M,
$$

and divergence-free:

$$
u,
$$

$$
\begin{aligned}
\langle Tu,M\rangle
&=
\left\langle
\nabla_{\rm sym}
(-\Delta)^{-1/2}u,
M
\right\rangle
\\
&=
-
\left\langle
u,
(-\Delta)^{-1/2}
\operatorname{div}M
\right\rangle
\\
&=
-
\left\langle
u,
P_{df}
(-\Delta)^{-1/2}
\operatorname{div}M
\right\rangle.
\end{aligned}
$$

Thus:

$$
\boxed{
T^\ast M
=
-
P_{df}
(-\Delta)^{-1/2}
\operatorname{div}M.
}
$$

---

# 19. C6-Q.4: Explicit Strain-Projection Formula

Orthogonal projection onto:

$$
\operatorname{Ran}T
=
L^2_{st}
$$

is:

$$
P_{st}
=
T(T^\ast T)^{-1}T^\ast.
$$

Since:

$$
T^\ast T
=
\frac12I,
$$

$$
\boxed{
P_{st}
=
2TT^\ast.
}
$$

Hence:

$$
\boxed{
P_{st}M
=
-2
\nabla_{\rm sym}
(-\Delta)^{-1}
P_{df}
\operatorname{div}M.
}
$$

### Status

Derived directly from the external Miller–Sawyer isometry and standard adjoint computation.

---

# 20. Fourier degree

Each term in:

$$
P_{st}
$$

has net Fourier degree:

$$
0.
$$

Therefore:

$$
\boxed{
P_{st}
}
$$

is a matrix-valued homogeneous degree-zero Calderón–Zygmund operator.

Its symbol is smooth away from:

$$
\xi=0.
$$

---

# 21. Physical-space kernel

Away from:

$$
x=0,
$$

the kernel has the form:

$$
\boxed{
K_{st}(x)
=
|x|^{-3}
\Omega
\left(
\frac{x}{|x|}
\right),
}
$$

with the usual spherical cancellation appropriate to a zero-order CZ operator.

Moreover:

$$
\boxed{
|\nabla K_{st}(x)|
\le
C|x|^{-4}.
}
$$

---

# 22. Truncated far tail

Let:

$$
F
$$

be a bounded symmetric matrix field.

Fix:

$$
0<R_0<R/2,
$$

and:

$$
L>R.
$$

Define:

$$
\boxed{
T_{R,L}F(x)
=
\int_{
R<|y|<L
}
K_{st}(x-y)
F(y)dy.
}
$$

---

# 23. Kernel difference

For:

$$
|x|\le R_0,
\quad
|y|>R>2R_0,
$$

the mean-value theorem gives:

$$
\boxed{
|K_{st}(x-y)-K_{st}(-y)|
\le
C
R_0
|y|^{-4}.
}
$$

---

# 24. C6-Q.5: Far-Tail Oscillation Lemma

Therefore:

$$
\begin{aligned}
|
T_{R,L}F(x)
-
T_{R,L}F(0)
|
&\le
C
R_0
\|F\|_\infty
\int_R^L
r^{-4}r^2dr
\\
&\le
C
\frac{R_0}{R}
\|F\|_\infty.
\end{aligned}
$$

Hence:

$$
\boxed{
\sup_{
|x|\le R_0
}
|
T_{R,L}F(x)
-
T_{R,L}F(0)
|
\le
C
\frac{R_0}{R}
\|F\|_\infty.
}
$$

The bound is uniform in:

$$
L.
$$

---

# 25. Tail differences converge

For:

$$
L_2>L_1>R,
$$

apply the same estimate to:

$$
L_1<|y|<L_2.
$$

Then:

$$
\boxed{
\sup_{
|x|\le R_0
}
\left|
[
T_{R,L_2}F(x)-T_{R,L_2}F(0)
]
-
[
T_{R,L_1}F(x)-T_{R,L_1}F(0)
]
\right|
\le
C
\frac{R_0}{L_1}
\|F\|_\infty.
}
$$

Therefore the far-tail **oscillation** converges as:

$$
L\to\infty.
$$

---

# 26. Renormalized tail oscillation

Define:

$$
\boxed{
E_R^F(x)
=
\lim_{L\to\infty}
\left[
T_{R,L}F(x)
-
T_{R,L}F(0)
\right].
}
$$

Then:

$$
\boxed{
E_R^F(0)=0,
}
$$

and:

$$
\boxed{
\|E_R^F\|_{L^\infty(B_{R_0})}
\le
C
\frac{R_0}{R}
\|F\|_\infty.
}
$$

---

# 27. C6-Q.6: Local-Constant Tail Reduction

On a fixed bounded core,

the far:

$$
P_{st}
$$

tail has the form:

$$
\boxed{
\text{constant matrix mode}
+
E_R^F(x),
}
$$

where:

$$
\boxed{
\|E_R^F\|_\infty
\to0
\qquad
(R\to\infty).
}
$$

Thus:

$$
\boxed{
\textbf{P_st far-field nonlocality is locally finite-dimensional modulo vanishing oscillation}.
}
$$

---

# 28. BMO/gauge interpretation

A zero-order CZ operator maps bounded sources naturally into:

$$
BMO
$$

rather than canonically into:

$$
L^\infty.
$$

The local constant matrix is the expected additive/gauge-type ambiguity of the far representative.

C6-Q does not discard it.

It records:

$$
\boxed{
C_R(\tau)
\in
\operatorname{Sym}_0(3)
}
$$

as an operator-background coordinate.

---

# 29. Record ancient source boundedness

At record peak:

$$
|v_n|\le1
$$

on every fixed backward interval.

Bounded mild smoothing gives global fixed-order derivative bounds there.

Hence the local source:

$$
F_n
=
(v_n\cdot\nabla)S_n
+
S_n^2
+
\frac34
\omega_n\otimes\omega_n
$$

obeys:

$$
\boxed{
\|F_n\|_\infty
\le
C
}
$$

uniformly on a shorter fixed ancient-time slab.

Therefore the oscillatory tail estimate C6-Q.6 is uniform in:

$$
n.
$$

---

# 30. Operator norm tail decomposition

On:

$$
B_{R_0},
$$

schematically:

$$
\boxed{
Q_{SV,n}
=
P_{st}
(F_n1_{B_R})
+
C_{n,R}(\tau)
+
E_{n,R}(\tau,x),
}
$$

where:

$$
\boxed{
\|E_{n,R}\|_{L^\infty(B_{R_0})}
\le
C
R_0/R.
}
$$

### Guard

The constant matrices:

$$
C_{n,R}
$$

need not vanish and need not have a uniform:

$$
R\to\infty
$$

limit without extra normalization/capacity control.

---

# 31. Constant background mode

The remaining far-field uncertainty for the **operator field itself** is therefore:

$$
\boxed{
\textbf{Constant STF Background Mode}.
}
$$

This is finite-dimensional.

It replaces the previous generic infinite-dimensional projected-tail defect on bounded peak cores.

---

# 32. Constant mode in a localized growth pairing

Let:

$$
\chi\in C_c^\infty
$$

be a cutoff.

For constant matrix:

$$
C,
$$

$$
\begin{aligned}
\int
\chi
C:(-\Delta S)dx
&=
C:
\int
\chi(-\Delta S)dx
\\
&=
C:
\int
(-\Delta\chi)Sdx.
\end{aligned}
$$

Therefore:

# 33. C6-Q.7: Constant-Tail Boundary Coupling Identity

$$
\boxed{
\int
\chi
C:(-\Delta S)
=
C:
\int
(-\Delta\chi)S.
}
$$

If:

$$
\chi\equiv1
$$

on the selected core,

the constant operator background enters the localized growth balance only through the cutoff transition annulus:

$$
\operatorname{supp}\Delta\chi.
$$

---

# 34. Boundary-annulus coordinate

Define:

$$
\boxed{
\mathfrak B_{\chi}^{ann}
=
\left|
\int
(-\Delta\chi)Sdx
\right|.
}
$$

Then:

$$
\boxed{
\left|
\int
\chi
C:(-\Delta S)
\right|
\le
|C|
\mathfrak B_{\chi}^{ann}.
}
$$

Thus even in a projected localized growth representation,

the far constant mode is reduced to:

$$
\boxed{
\textbf{finite-dimensional constant amplitude}
\times
\textbf{boundary-annulus strain debt}.
}
$$

---

# 35. Preferred TS ancient lift

Because C6-Q.1 already provides:

$$
g_O^{loc},
$$

C6 does **not** need to carry:

$$
C_R
$$

inside the preferred TS growth-carrier state.

From C6-Q onward:

$$
\boxed{
TS^{anc}_{growth}
}
$$

uses the local growth lift by default,

while:

$$
\boxed{
OP^{anc}_{norm}
}
$$

stores the projected operator field and constant-tail mode.

---

# 36. Ancient TS local density convergence

Suppose:

$$
v_n
\to
v_\infty
$$

in:

$$
C^3_{\rm loc}
$$

on a fixed peak cylinder.

Then:

$$
\boxed{
g_{O,n}^{loc}
\to
g_{O,\infty}^{loc}
}
$$

uniformly locally.

Likewise:

$$
a_{M,n}
=
\lambda_2^+(S_n)|S_n|^2
\to
a_{M,\infty}.
$$

Therefore positive local source capacities and common-part measures pass under suitable nondegeneracy/margin assumptions.

---

# 37. C6-Q.8: Conditional Ancient TS Local-Growth Inheritance

Assume on a fixed peak cylinder:

1. local middle load:
   $$
   \ge m_0>0;
   $$
2. local positive growth capacity:
   $$
   \int[g_O^{loc}]_+
   \ge o_0>0;
   $$
3. local shared overlap:
   $$
   \Omega_{ST}^{loc}
   \ge
   \omega_0>0;
   $$
4. the peak time window has a nondegenerate ancient representation;
5. local:
   $$
   C^3
   $$
   convergence holds.

Then:

$$
\boxed{
TS_{growth}^{anc}
}
$$

passes to:

$$
v_\infty
$$

without any:

$$
P_{st}
$$

far-tail hypothesis.

### This is a major correction to C6-P.

---

# 38. What does not pass automatically

The Miller operator-norm state:

$$
\|Q_{SV}\|_{\dot H^\alpha}
$$

is not determined by the local growth lift.

Therefore an ancient state may be:

$$
\boxed{
TS_{growth}^{anc}
}
$$

without a compact:

$$
OP_{norm}^{anc}
$$

state.

These remain separate typed objects.

---

# 39. Spatial carrier escape in C6-P

C6-P left fixed-order defect carriers which satisfy:

$$
|z_n|\to\infty
$$

in the peak frame.

Because spatial translation is an exact N–S symmetry,

this escape can be rebound.

---

# 40. Carrier recentering

Let:

$$
z_n\in\mathbb R^3
$$

be carrier centers.

Define:

$$
\boxed{
w_n(y,\tau)
=
v_n(y+z_n,\tau).
}
$$

Then:

$$
w_n
$$

solves the same N–S equations.

Record bound:

$$
\boxed{
\|w_n(\tau)\|_\infty
\le1
\qquad
\tau\le0.
}
$$

All fixed-order derivative bounds remain uniform.

---

# 41. Local defect load

Let:

$$
\mathcal D
$$

be a translation-covariant local defect functional.

Examples:

- local:
  $$
  \int|Q|;
  $$
- local middle load;
- local:
  $$
  [g_O^{loc}]_+;
  $$
- fixed-order derivative/sign carrier;
- local absolute:
  $$
  L^3
  $$
  floor.

Assume:

$$
\boxed{
\mathcal D[
v_n;
B_R(z_n)\times I
]
\ge
d_0>0.
}
$$

---

# 42. C6-Q.9: Satellite Ancient Defect Extraction

After translation:

$$
\boxed{
\mathcal D[
w_n;
B_R(0)\times I
]
\ge
d_0.
}
$$

Bounded smoothing gives:

$$
w_n
$$

precompact in:

$$
C^\infty_{\rm loc}
$$

on fixed ancient cylinders.

After subsequence:

$$
\boxed{
w_n
\to
w_\infty,
}
$$

where:

$$
\boxed{
w_\infty
}
$$

is a bounded ancient N–S solution carrying the same nonzero local defect load.

This is:

$$
\boxed{
\textbf{Satellite Ancient Defect Profile}.
}
$$

---

# 43. Spatial escape is a translation rebinding

Therefore, for local translation-covariant fixed-order defect states:

$$
\boxed{
\textbf{Spatial Carrier Escape is not terminal}.
}
$$

It can be quotiented/rebound to another bounded ancient profile centered at the carrier.

### Guard

The new profile need not contain the original **amplitude record point**.

Its:

$$
L^\infty
$$

supremum can be strictly less than:

$$
1.
$$

---

# 44. HF satellite

If a fixed-order HF carrier escapes peak infinity but:

- local derivative/sign load stays nonzero;
- strict geometry margin survives;

then translation rebinding yields:

$$
\boxed{
HF_{k,sat}^{anc}.
}
$$

No fixed-order scale restart is needed.

---

# 45. GP satellite

If a GP carrier escapes peak infinity with:

- local Q load;
- strong-middle geometry;
- pressure response;

then recentering yields a:

$$
\boxed{
GP_{sat}^{anc}
}
$$

candidate.

Pressure provenance must be repartitioned relative to the new satellite core.

The peak-pressure Hessian tail closure remains valid because:

$$
w_n
$$

is still globally bounded by:

$$
1.
$$

---

# 46. TS satellite

Using:

$$
g_O^{loc},
$$

a TS growth carrier escaping peak infinity can be translated directly.

If local middle/growth overlap stays nondegenerate:

$$
\boxed{
TS_{sat}^{anc}
}
$$

is extracted without a projected-operator tail obstruction.

This is one of the strongest payoffs of C6-Q.1.

---

# 47. Physical satellite center

In original coordinates:

$$
\boxed{
X_n
=
x_n
+
a_nz_n.
}
$$

Define physical displacement:

$$
\boxed{
d_n^{phys}
=
a_n|z_n|.
}
$$

After subsequence:

---

# 48. C6-Q.10: Satellite Physical-Center Trichotomy

## Q-X0

$$
\boxed{
d_n^{phys}\to0.
}
$$

The satellite carrier collapses onto the same physical blow-up center as the record peak,

but is far away in peak units.

## Q-X1

$$
\boxed{
d_n^{phys}\to d_\ast\in(0,\infty).
}
$$

The satellite carrier approaches a distinct finite physical location relative to the record peak center.

## Q-X∞

$$
\boxed{
d_n^{phys}\to\infty.
}
$$

The satellite carrier escapes to physical infinity.

### Guard

C6-Q does not automatically identify Q-X1 as a second singular point for every defect functional.

That requires a local singularity/regularity criterion for the carried defect.

---

# 49. Translation quotient state

For local ancient defect classification,

C6 can quotient spatial translations:

$$
\boxed{
[v]
=
\{
v(\cdot+z,\cdot):
z\in\mathbb R^3
\}.
}
$$

Then peak-centered and satellite ancient profiles belong to the same **translation-modulo state space** only if their full local states match after translation.

The original amplitude record center remains extra provenance metadata.

---

# 50. Carrier multiplicity

There may be many pairwise widely separated:

$$
z_{j,n}.
$$

If each carries a fixed local absolute defect load,

one can extract multiple satellite ancient profiles.

The number need not remain finite because the global peak-frame:

$$
L^3/L^2
$$

capacities may diverge.

Thus:

$$
\boxed{
\textbf{satellite multiplicity remains a real fiber mechanism}.
}
$$

---

# 51. Ancient-time recurrence

Suppose one bounded ancient profile:

$$
v
$$

carries the same local defect type at times:

$$
\boxed{
\tau_j\to-\infty.
}
$$

Let:

$$
z_j
$$

be corresponding spatial carrier centers.

Define time/space shifted fields:

$$
\boxed{
w_j(x,t)
=
v(x+z_j,t+\tau_j).
}
$$

---

# 52. Time domain after ancient shift

Original:

$$
v
$$

is defined on:

$$
(-\infty,0].
$$

Thus:

$$
w_j
$$

is defined on:

$$
\boxed{
t\le-\tau_j.
}
$$

Since:

$$
-\tau_j\to+\infty,
$$

for every finite:

$$
T>0,
$$

eventually:

$$
w_j
$$

is defined on:

$$
[-T,T].
$$

---

# 53. Uniform boundedness

If:

$$
v
$$

is bounded ancient:

$$
\|v\|_\infty\le M,
$$

then:

$$
\boxed{
\|w_j\|_\infty
\le M
}
$$

uniformly on every compact spacetime set.

Bounded mild smoothing gives uniform derivative estimates.

---

# 54. C6-Q.11: Ancient Recurrence → Eternal Profile Extraction

If a local translation-covariant defect load satisfies:

$$
\boxed{
\mathcal D[
v;
B_R(z_j)\times[\tau_j-T_0,\tau_j+T_0]
]
\ge
d_0>0
}
$$

with:

$$
\tau_j\to-\infty,
$$

then after space-time shifting and subsequence:

$$
\boxed{
w_j
\to
w_\infty
}
$$

in:

$$
C^\infty_{\rm loc}
(
\mathbb R^3\times\mathbb R
).
$$

The limit:

$$
\boxed{
w_\infty
}
$$

is a bounded **eternal** Navier–Stokes solution carrying the nonzero local defect.

---

# 55. Eternal does not imply trivial

A bounded eternal solution is in particular bounded ancient.

The general 3D bounded ancient Liouville problem is open.

Therefore:

$$
\boxed{
\textbf{Eternal Defect Extraction}
\neq
\textbf{contradiction}.
}
$$

It is a stronger compactness reduction.

---

# 56. Eternal external kill gates

If:

$$
w_\infty
$$

also lies in one of the known rigidity classes:

- bounded:
  $$
  L^3
  $$
  along backward times;
- Type-I decay;
- special symmetry;
- FLAT;
- another valid ancient/eternal Liouville class;

then the corresponding external theorem can close the branch.

Otherwise the eternal defect remains open.

---

# 57. Local growth TS recurrence

Because:

$$
TS_{growth}^{anc}
$$

can be represented by local densities,

ancient recurrence of TS growth carriers fits C6-Q.11 directly.

Thus repeated TS source events at:

$$
\tau_j\to-\infty
$$

yield a bounded eternal profile carrying recurrent/local source structure after translation.

---

# 58. GP recurrence

Peak-local pressure Hessian has finite-radius closure.

Therefore a recurrent ancient GP state can also be translated/time-shifted,

and, under uniform local margins/provenance tightness,

an eternal:

$$
GP^{et}
$$

state can be extracted.

Again, no general Liouville theorem closes it automatically.

---

# 59. HF recurrence

For fixed:

$$
k,
$$

record/ancient smoothing gives uniform derivative bounds.

If a fixed-order HF geometry recurs at:

$$
\tau_j\to-\infty,
$$

translation/time shifting yields an eternal bounded profile carrying the local fixed-order HF geometry.

The unresolved part is theorem setup/order-asymptotic behavior,

not amplitude blow-up.

---

# 60. Order-geometry escape remains separate

The translation/eternal reduction applies to each fixed order.

A sequence:

$$
k_j\to\infty
$$

can still carry normalized sign/harmonic geometry not captured at any fixed order.

Because raw factorial growth is regularized by analyticity,

a genuine order escape must be encoded by:

- normalized roots;
- sign profiles;
- theorem clocks;
- harmonic bad sets.

This is still open.

---

# 61. Lift provenance in cross-domain routing

C6-E/F used operator spacetime overlaps in TS→GP/HF bridges.

After C6-Q, these statements must specify whether they use:

- Projected Representative Lift;
- Local Growth Representative Lift.

The resulting spatial shared carriers can differ.

Therefore:

$$
\boxed{
\textbf{TS cross-domain edge metadata now includes Lift Provenance}.
}
$$

---

# 62. What remains invariant across lifts?

Both operator lifts have the same temporal marginal:

$$
\boxed{
\mu_J^O.
}
$$

Thus temporal phase statements from C5-B/C remain unchanged.

What changes:

- spatial overlap;
- core localization;
- carrier identity;
- label transfer.

This is a precise correction rather than a collapse of the earlier temporal theory.

---

# 63. Preferred local-growth convention

For future **singular-carrier** work, C6-Q adopts:

$$
\boxed{
\textbf{Local Growth Representative Lift}
}
$$

as the preferred TS operator carrier because:

- it is exact;
- local;
- scale covariant;
- stable under:
  $$
  C^3_{\rm loc}
  $$
  convergence;
- free of projected-tail provenance.

The projected lift remains useful for operator-norm regularity questions.

---

# 64. Operator-norm state

Define:

$$
\boxed{
OP_{\rm norm}
=
\left\langle
Q_{SV},
\|Q_{SV}\|_{\dot H^\alpha},
\text{local finite-radius part},
C_R,
E_R
\right\rangle.
}
$$

Its ancient compactness is a different research problem from:

$$
TS_{growth}.
$$

---

# 65. Constant-mode compactification

For operator-norm local state,

compactify:

$$
C_R
$$

by:

$$
\boxed{
\widehat C_R
=
\frac{
C_R
}{
1+|C_R|
}.
}
$$

Then either:

- constant mode bounded/subconvergent;
- or:
  $$
  |C_R|\to\infty.
  $$

The latter is a genuine projected-operator capacity-at-infinity mode, not an arbitrary spatial oscillation.

---

# 66. Constant mode and trace

Because:

$$
P_{st}
$$

projects onto trace-free strain matrices,

the local constant background may be taken:

$$
\boxed{
C_R\in
\operatorname{Sym}_0(3)
}
$$

under the corresponding normalized representative.

Thus it has only five scalar degrees of freedom.

---

# 67. Projected-tail geometry

A constant STF matrix can have:

- one-negative;
- two-negative;
- degenerate signature.

So, if needed, the same finite-dimensional signature analysis used for pressure can be applied to the projected-operator background.

C6-Q does not claim such a signature has the same physical meaning as pressure Hessian.

---

# 68. TS local carrier vs OP norm carrier

A hypothetical blow-up may have:

$$
\boxed{
TS_{growth}
}
$$

with a compact local source carrier,

while:

$$
OP_{\rm norm}
$$

escapes through a large constant background or global norm.

Conversely, large:

$$
OP_{\rm norm}
$$

does not guarantee positive local:

$$
E_1'
$$

growth carrier.

This type separation mirrors C6-C:

$$
\boxed{
\text{capacity}
\neq
\text{realized response}.
}
$$

---

# 69. Ancient defect taxonomy after lift correction

The peak ancient classes are now:

## Q-A — FLAT

already killed as TS/GP/HF carrier.

## Q-GP

$$
\boxed{
GP_{\rm loc}^{anc}
}
$$

with peak pressure closure.

## Q-HF

$$
\boxed{
HF_{k,\rm geom}^{anc}
}
$$

fixed-order local geometry.

## Q-TS

$$
\boxed{
TS_{growth}^{anc}
}
$$

using local growth lift.

## Q-OP

$$
\boxed{
OP_{\rm norm}^{anc}
}
$$

projected operator-norm state, possibly with constant background.

## Q-SAT

$$
\boxed{
\text{Satellite Ancient Defect}.
}
$$

## Q-ORD

$$
\boxed{
\text{Order-Geometry Escape}.
}
$$

## Q-ET

$$
\boxed{
\text{Eternal Defect Profile}.
}
$$

---

# 70. C6-Q.12: Ancient Defect Reduction

After:

1. record-peak fixed-order derivative rigidity;
2. pressure-Hessian peak-tail closure;
3. local growth lift replacement for TS;
4. translation rebinding of spatial carriers;

the ancient peak/satellite defect problem reduces to:

$$
\boxed{
GP_{\rm loc}^{anc}
\vee
HF_{k,\rm geom}^{anc}
\vee
TS_{growth}^{anc}
\vee
OP_{\rm norm}^{anc}
\vee
\text{ORDER-GEOMETRY}
\vee
\text{ETERNAL-DEFECT}
\vee
\text{FLAT}.
}
$$

FLAT carries no nontrivial C6 defect.

Spatial carrier escape is removed as a terminal category for local translation-covariant defects.

---

# 71. What C6-Q eliminates

## Q-DEL1

$$
\text{TS growth carrier intrinsically requires a nonlocal }P_{st}\text{ tail}.
$$

FALSE.

## Q-DEL2

$$
\text{operator temporal marginal has a unique canonical positive spatial lift}.
$$

FALSE.

## Q-DEL3

$$
\text{P_st far tail can oscillate arbitrarily on a fixed bounded peak core under bounded source control}.
$$

FALSE; modulo a constant, oscillation is:

$$
O(R^{-1}).
$$

## Q-DEL4

$$
\text{spatial carrier escape is terminal for fixed-order local defects}.
$$

FALSE; translation rebinding extracts a satellite ancient profile.

## Q-DEL5

$$
\text{ancient defect recurrence only gives another ancient profile}.
$$

FALSE; time shifting:

$$
\tau_j\to-\infty
$$

produces an eternal-profile limit.

## Q-DEL6

$$
\text{local TS carrier and Miller projected operator norm are the same state}.
$$

FALSE.

---

# 72. What remains open

## Q-O1 — Operator constant mode

Can:

$$
C_R
$$

diverge/recur in a way compatible with Miller's operator criterion and bounded ancient dynamics?

## Q-O2 — Eternal GP rigidity

Can a nontrivial bounded eternal:

$$
GP
$$

state exist?

## Q-O3 — Eternal HF geometry

Can fixed-order sign geometry recur eternally without entering a known regularity/Liouville class?

## Q-O4 — Eternal TS growth state

Can local middle/growth shared-source events recur for all time in a bounded eternal solution?

## Q-O5 — Order-geometry escape

Can analytic bounded ancient profiles sustain a genuine:

$$
k\to\infty
$$

harmonic/sign defect?

## Q-O6 — Lift dependence

Can projected and local TS carrier lifts have radically different singular-carrier classifications along one solution?

## Q-O7 — Carrier multiplicity

Can infinitely many satellite ancient profiles be dynamically relevant to one singular event?

---

# 73. Strategic interpretation

C6-P ended with one difficult-looking nonlocal obstruction:

$$
P_{st}.
$$

C6-Q shows that obstruction was partly representational.

For the exact temporal:

$$
H^1
$$

strain-growth ledger:

$$
\boxed{
E_1'
=
-\nu\|\Delta S\|_2^2
-
\langle
(u\cdot\nabla)S+S^2,
-\Delta S
\rangle.
}
$$

So a local exact operator-growth carrier exists.

That means:

$$
\boxed{
\textbf{TS shared-source localization does not fundamentally depend on a global strain projection}.
}
$$

The genuinely nonlocal projected operator remains only where its **norm** or full matrix field is itself the object.

Even there,

the far tail on a bounded peak core is not arbitrary:

$$
\boxed{
\textbf{constant matrix}
+
O(R^{-1})\textbf{ oscillation}.
}
$$

At the same time,

spatial carrier escape is not a terminal loophole.

Translation symmetry lets us recenter escaping local defect carriers and extract:

$$
\boxed{
\textbf{satellite bounded ancient profiles}.
}
$$

If a local ancient defect repeats at:

$$
\tau\to-\infty,
$$

space-time shifting produces a:

$$
\boxed{
\textbf{bounded eternal defect profile}.
}
$$

So the C6 frontier has moved again:

we no longer primarily need to chase peak infinity or projected tails.

The core questions are now:

> **Can nontrivial bounded eternal TS/GP/HF defect states exist?**

and:

> **Can the only remaining genuinely high-order branch—order-geometry escape under a uniform analytic baseline—survive?**

Those are much more rigid targets.

---

# 74. Proposed C6-R

$$
\boxed{
\textbf{C6-R — Eternal Defect Profiles,
Analytic Order-Geometry Rigidity,
and Operator-Constant-Mode Closure}.
}
$$

---

# 75. C6-R proof obligations

## R1 — eternal TS local-growth state

Classify bounded eternal solutions carrying persistent:

- middle load;
- local:
  $$
  E_1'
  $$
  growth carrier;
- shared-source overlap.

## R2 — eternal GP state

Use local pressure closure and finite-dimensional geometry to test eternal recurrence.

## R3 — eternal HF fixed-order geometry

Analyze sign-thick/sparse states with uniformly bounded derivative amplitudes.

## R4 — order-geometry escape

Use uniform analyticity radius and factorial-normalized roots to constrain:

$$
k_n\to\infty.
$$

## R5 — operator constant background

Study:

$$
C_R(t)
$$

as a finite-dimensional forcing/projection mode.

## R6 — global-vs-local growth

Relate local growth representative to Miller's projected operator norm criterion.

## R7 — eternal Liouville interfaces

Audit:

- backward-sequence:
  $$
  L^3;
  $$
- Type-I;
- symmetry;
- periodicity;
- finite-energy;
- decay.

## R8 — satellite multiplicity

Determine when many satellite profiles force profile splitting or critical-capacity inflation.

## R9 — lift-equivalence criteria

Find conditions under which local/projected operator carrier lifts become asymptotically equivalent.

## R10 — ancient/eternal graph rebuild

Replace spatial-escape branches by translated ancient/eternal nodes.

---

# 76. Major no-go audit

### NG-Q1

$$
P_{st}
\text{ is unavoidable in the exact }H^1\text{ temporal growth density}.
$$

FALSE.

### NG-Q2

$$
\text{positive operator spatial lift is unique}.
$$

FALSE.

### NG-Q3

$$
P_{st}\text{ bounded-source tail has no local structure}.
$$

FALSE.

### NG-Q4

$$
\text{spatial carrier escape destroys local defect compactness}.
$$

FALSE after translation rebinding.

### NG-Q5

$$
\text{ancient recurrence cannot yield an eternal profile}.
$$

FALSE under the bounded/local recurrence hypotheses.

### NG-Q6

$$
\text{bounded eternal profile is automatically constant in 3D}.
$$

OPEN / NOT PROVED.

### NG-Q7

$$
TS_{growth}
=
OP_{norm}.
$$

FALSE.

---

# 77. X-Integration guards update

## G-LIFTPROV

Every operator spatial carrier stores lift provenance.

## G-TSLOCAL

Preferred TS growth carrier uses:

$$
g_O^{loc}.
$$

## G-OPNORM

Projected operator norm remains a separate state.

## G-PSTCONST

Projected far tail stores constant STF background + oscillation remainder.

## G-SATTRANS

Spatial carrier escape triggers translation rebinding before being called a new defect.

## G-PHYSCENTER

Satellite profiles preserve physical center rate:

$$
a_nz_n.
$$

## G-ETERNAL

Ancient-time recurrence triggers eternal-profile extraction.

## G-ORDAN

Order escape is compared against analytic/factorial baseline.

---

# 78. True ETN update

Ancient/local operator state:

$$
\boxed{
\Theta^{C6Q}
=
\left\langle
\text{lift provenance},
g_O^{loc},
\Pi_O^{loc},
\Omega_{ST}^{loc},
Q_{SV},
C_R,
E_R,
\text{satellite center},
\text{physical center rate},
\text{ancient/eternal class},
\text{order geometry}
\right\rangle.
}
$$

State classes:

$$
\boxed{
\mathfrak Q^{C6Q}
=
\{
TS_{\rm growth},
OP_{\rm norm},
GP_{\rm anc},
HF_{\rm anc},
SAT,
ETERNAL,
ORDER,
FLAT
\}.
}
$$

---

# 79. Formal status

$$
\boxed{
\begin{aligned}
\text{projection-free }H^1\text{ growth identity}
&:\ \mathrm{PROVED},\\
\text{local growth density}
&:\ \mathrm{DEFINED/EXACT},\\
\text{operator-lift uniqueness}
&:\ \mathrm{REJECTED},\\
\text{local TS growth lift}
&:\ \mathrm{DEFINED},\\
\text{projected-tail as intrinsic TS growth obstruction}
&:\ \mathrm{NO\mbox{-}GO/REJECTED},\\
P_{st}\text{ explicit projection formula}
&:\ \mathrm{PROVED\ FROM\ MILLER\mbox{-}SAWYER},\\
P_{st}\text{ degree-zero CZ structure}
&:\ \mathrm{PROVED},\\
\text{far-tail oscillation }O(R^{-1})
&:\ \mathrm{PROVED},\\
\text{local-constant tail reduction}
&:\ \mathrm{PROVED},\\
\text{constant-tail boundary coupling}
&:\ \mathrm{PROVED},\\
\text{ancient TS local-growth inheritance}
&:\ \mathrm{CONDITIONAL\ PROVED},\\
\text{operator-norm tail fully eliminated}
&:\ \mathrm{NOT\ PROVED},\\
\text{satellite ancient defect extraction}
&:\ \mathrm{PROVED\ UNDER\ LOCAL\ LOAD},\\
\text{spatial carrier escape as terminal local defect}
&:\ \mathrm{REJECTED},\\
\text{ancient recurrence}\Rightarrow\text{eternal profile}
&:\ \mathrm{PROVED\ UNDER\ LOCAL\ RECURRENCE},\\
\text{general bounded eternal Liouville}
&:\ \mathrm{OPEN},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 80. Conclusion

The final difficulty of C6-P appeared to be:

$$
\boxed{
P_{st}\text{ tail}
+
\text{spatial carrier escape}
+
\text{order geometry}.
}
$$

C6-Q now significantly compresses the first two.

First,

for the genuine:

$$
H^1
$$

strain growth:

$$
E_1
=
\frac12
\|S\|_{\dot H^1}^2,
$$

the exact identity is:

$$
\boxed{
E_1'
=
-\nu\|\Delta S\|_2^2
-
\left\langle
(u\cdot\nabla)S+S^2,
-\Delta S
\right\rangle.
}
$$

So:

$$
\boxed{
g_O^{loc}
=
-
[(u\cdot\nabla)S+S^2]:(-\Delta S)
-
\nu|\Delta S|^2
}
$$

is a fully local exact spatial representative.

Therefore:

$$
\boxed{
\textbf{the TS growth carrier does not need to cross the }P_{st}\textbf{ tail.}
}
$$

The projected operator lift of C6-E is not the unique canonical lift,

and must be changed to:

$$
\boxed{
\textbf{Lift Provenance}.
}
$$

Second,

the operator-norm channel that genuinely requires:

$$
P_{st}
$$

is also not completely uncontrolled.

Using:

$$
\boxed{
P_{st}M
=
-2
\nabla_{\rm sym}
(-\Delta)^{-1}
P_{df}
\operatorname{div}M,
}
$$

one sees it is a zero-order CZ operator.

For a bounded ancient peak source:

$$
F,
$$

its far tail on:

$$
B_{R_0}
$$

satisfies:

$$
\boxed{
\text{tail}(x)
=
C_R
+
E_R(x),
}
$$

with:

$$
\boxed{
\|E_R\|_\infty
\lesssim
R_0/R.
}
$$

So:

$$
\boxed{
\textbf{the far projection tail retains at most a finite-dimensional constant background + vanishing oscillation}.
}
$$

And the constant background in the localized:

$$
-\Delta S
$$

growth pairing acts only through the cutoff annulus.

Third,

a fixed-order spatial carrier escaping to:

$$
|z_n|\to\infty
$$

is no longer a terminal escape.

Translation symmetry:

$$
w_n(x,t)
=
v_n(x+z_n,t)
$$

preserves:

- boundedness;
- fixed-order smoothing;
- local defect load.

So one can extract a:

$$
\boxed{
\textbf{Satellite Ancient Defect Profile}.
}
$$

Finally,

if a bounded ancient defect recurs at:

$$
\tau_j\to-\infty,
$$

time + space shifting pushes the future horizon to:

$$
+\infty,
$$

allowing the extraction of a:

$$
\boxed{
\textbf{bounded eternal defect profile}.
}
$$

This is still not a contradiction,

because the general 3D bounded ancient/eternal Liouville problem remains open.

But the C6 problem is now highly focused:

$$
\boxed{
\textbf{Can nontrivial bounded eternal TS/GP/HF defect states exist?}
}
$$

and:

$$
\boxed{
\textbf{Under a uniform analytic baseline,
can order-asymptotic sign/harmonic geometry escape?}
}
$$

Formally the next paper:

$$
\boxed{
\textbf{C6-R — Eternal Defect Profiles,
Analytic Order-Geometry Rigidity,
and Operator-Constant-Mode Closure}.
}
$$

---

# References

1. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure Appl. Analysis 8 (2026), 247–270.
2. E. Miller, E. Sawyer, *A Helmholtz-type decomposition for the space of symmetric matrices*, arXiv:2111.12891; Trans. Amer. Math. Soc. Ser. B 10 (2023), 1449–1493.
3. G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, arXiv:0709.3599.
4. Z. Lei, Z. Yang, C. Yuan, *Backward Uniqueness for 3D Navier-Stokes Equations with Non-trivial Final Data and Applications*, arXiv:2311.02429.
5. G. Seregin, *On potential Type II blowups for the Navier–Stokes equations*, arXiv:2606.29468 (2026).
6. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.

# Internal dependencies

- `NS_C6P_AncientDefect_DerivativeRigidity_PressureClosure_v0.1.md`
- `NS_C6O_PeakScale_DefectInheritance_TypeII_TwoScale_v0.1.md`
- `NS_C6N_NearLossless_AncientProfile_DefectRigidity_v0.1.md`
- `NS_C6M_CarrierCompleteness_SpectralPressure_NestedRigidity_v0.1.md`
- `NS_C6L_SingularCarrier_Spectator_Rebinding_v0.1.md`
- `NS_C6K_CriticalFiber_ProfileSplitting_v0.1.md`
- `NS_C6J_LogScale_RenormalizedFlow_CriticalFiberEscape_v0.1.md`
- `NS_C6I_CriticalDebt_CapacityInfinity_BarrierCycles_v0.1.md`
- `NS_C6H_BoundaryFaces_DebtCoercivity_CycleElimination_v0.1.md`
- `NS_C6G_TypedCrossDomainGraph_SCC_BoundarySurvivors_v0.1.md`
- `NS_C6F_SharedSource_CoreExtraction_CrossDomainRouting_v0.1.md`
- `NS_C6E_TemporalSpatial_SharedSource_TTrap_v0.1.md`
- `NS_C6D_GeometryPressure_Provenance_SignatureReturn_v0.1.md`
- `NS_C6C_DuhamelCoherence_ReentryCriticalSaturation_v0.1.md`
- `NS_C6B_ForcingReentry_HF_CycleTest_v0.1.md`
- `NS_C6A_CertifiedDefectGraph_TypedCycles_MinimalSurvivors_v0.1.md`

Next:

$$
\boxed{
\textbf{C6-R — Eternal Defect Profiles,
Analytic Order-Geometry Rigidity,
and Operator-Constant-Mode Closure}
}
$$