---
title: "Navier–Stokes C5-E: Strain-Direction Defect Measures, Middle-Gap Degeneration, and Derivative-Intermittency Closure"
subtitle: "From Quadratic Cancellation to Middle-Gap Concentration, Strain/Vorticity Leakage, Cubic Active-Volume Intermittency, and the Remaining Grujić–Xu Interface"
version: "v0.1"
date: "2026-08-15"
author: "Neo.K / EveMissLab"
language: "en"
status: "Theorem-style spatial defect-measure reduction / intermittency interface"
epistemic_status: "Exact trace-free eigenvalue algebra + Q-weighted defect measures + Poincaré fluctuation routing + effective-volume intermittency lemmas + conditional interface to published derivative-sparseness regularity criteria. Does NOT prove Navier–Stokes regularity."
---

# Navier–Stokes C5-E
# Strain-Direction Defect Measures, Middle-Gap Degeneration, and Derivative-Intermittency Closure

## 0. Current Round Positioning

C5-D obtained the first finite-dimensional recurrent-limit incompatibility of C5:

$$
\boxed{
\text{Strong-Middle Pointwise Cone}
\cap
\text{Seven-Point Zero-Barycenter Cancellation}
=
\varnothing.
}
$$

Therefore, the recurrent quadratic-cancellation motif:

$$
Q
$$

if it is to continue existing, can only escape to:

$$
\boxed{
\text{Middle-Gap Degeneration}
\vee
\text{Strain-Direction Dispersion}.
}
$$

The task of C5-E is not merely to preserve these two names,

but to ask:

> What kind of measurable / derivative / intermittency debt do they actually represent?

Main results of this round:

1. The normalized middle-gap variable:
   $$
   \vartheta(S)
   =
   \frac{
   \lambda_2^+(S)\lambda_3(S)
   }{
   |S|^2
   }
   $$
   and:
   $$
   \lambda_2^+(S)/|S|
   $$
   are quantitatively equivalent;
2. If:
   $$
   \vartheta\ge\delta>0,
   $$
   then pointwise:
   $$
   \boxed{
   |Q|
   \gtrsim
   \delta
   (
   |S|^2+|\omega|^2
   );
   }
   $$
3. Therefore, the Q-weighted middle-gap concentration is a genuine physical quadratic activity concentration,
   not a matrix-normalization artefact;
4. Establish the:
   $$
   \boxed{
   \text{Q-weighted strain-direction/middle-gap defect measure};
   }
   $$
5. If the zero quadratic barycenter limit has no middle-gap mass,
   then the strain-direction marginal cannot converge to a single strong-middle direction;
6. Quantitative Q-cancellation forcing fixed cone leakage;
7. Cone leakage is then exactly split into:
   $$
   \boxed{
   \text{strain-carrying directional leakage}
   \vee
   \text{vorticity-dominant leakage};
   }
   $$
8. Strain-carrying leakage utilizes weighted Poincaré to yield:
   $$
   \boxed{
   \text{higher-derivative strain fluctuation stock};
   }
   $$
9. Vorticity-dominant leakage yields:
   $$
   \boxed{
   \text{local critical vorticity/enstrophy stock};
   }
   $$
10. If middle-gap degeneration bears a fixed fraction of middle amplification,
    it must force:
    $$
    \boxed{
    \|S\|_3^3
    \gtrsim
    \delta^{-1}
    \times
    \text{middle load};
    }
    $$
11. Large cubic strain relative to the $L^2$ stock generates a:
    $$
    \boxed{
    \text{small effective active volume};
    }
    $$
12. An explicit effective-amplitude superlevel set can simultaneously:
    - carry a fixed fraction of cubic activity;
    - possess a small volume;
13. Thus, the middle-gap route is converted into genuine spatial intermittency;
14. However, the published Grujić–Xu theorem still requires:
    - $D^ku$ or $D^k\omega$ component/sign superlevel sparseness;
    - escape/later analytic time;
    - derivative-chain hypotheses;
15. Strain amplitude / $\nabla S$ intermittency cannot currently be directly substituted for the theorem hypotheses;
16. Therefore, what C5-E obtains is a:
    $$
    \boxed{
    \textbf{Derivative-Intermittency Pre-Gate},
    }
    $$
    not a full regularity gate;
17. The free Q-cancellation motif of C5-D is thus eliminated:
    $$
    \boxed{
    Q
    \Rightarrow
    \text{Gap Concentration}
    \vee
    \text{Derivative Fluctuation}
    \vee
    \text{Vorticity Leakage}.
    }
    $$

---

# 1. Fresh primary-source audit

## 1.1 Miller — middle eigenvalue

Miller's middle-eigenvalue work establishes:

$$
\lambda_2^+
$$

as a scale-critical regularity channel.

Therefore, C5-E's treatment of the normalized:

$$
\lambda_2^+/|S|
$$

degeneration is not an arbitrary eigenvalue statistic;

it is a shape degeneration within the middle-strain regularity geometry.

## 1.2 Grujić–Xu 2024 journal version

The official version of record:

$$
\boxed{
\text{J. Math. Fluid Mech. 26, Article 53 (2024)}.
}
$$

Its framework is centered around:

$$
\boxed{
\text{higher derivative component/sign superlevel-set sparseness}
}
$$

as its core.

Theorem 3.5 is a fixed derivative direct geometric regularity criterion.

Theorem 3.7 provides energy-level a-priori volumetric sparseness.

Theorem 3.14 uses:

- higher-order derivative chains;
- spatial analyticity;
- component/sign superlevel sets;

to obtain an asymptotically critical regularity route.

### C5-E guard

This document does not treat the magnitude geometry of:

$$
S,
\quad
\nabla S
$$

directly as the:

$$
D^ku
$$

component/sign theorem hypothesis.

---

# 2. Positive-middle normalized shape

For:

$$
S\in\operatorname{Sym}_0(3),
\qquad
S\ne0,
$$

with ordered eigenvalues:

$$
\lambda_1\le\lambda_2\le\lambda_3.
$$

Define:

$$
\boxed{
\xi_2(S)
=
\frac{
\lambda_2^+(S)
}{
|S|_F
}.
}
$$

and the C5-D shape variable:

$$
\boxed{
\vartheta(S)
=
\frac{
\lambda_2^+(S)\lambda_3(S)
}{
|S|_F^2
}.
}
$$

If:

$$
\lambda_2\le0,
$$

set:

$$
\vartheta=0.
$$

---

# 3. C5-E.1: Middle-Gap Equivalence

If:

$$
\lambda_2>0,
$$

the normalized eigenvalues satisfy:

$$
\boxed{
\frac1{\sqrt6}
\le
\frac{\lambda_3}{|S|}
\le
\frac1{\sqrt2}.
}
$$

Thus:

$$
\boxed{
\frac1{\sqrt6}
\xi_2
\le
\vartheta
\le
\frac1{\sqrt2}
\xi_2.
}
$$

Equivalently:

$$
\boxed{
\sqrt2\,\vartheta
\le
\xi_2
\le
\sqrt6\,\vartheta.
}
$$

### Conclusion

$$
\boxed{
\vartheta\to0
\quad\Longleftrightarrow\quad
\lambda_2^+/|S|\to0
}
$$

within the positive-middle sector.

Therefore:

$$
\boxed{
\textbf{Middle-Gap Degeneration}
}
$$

is the genuine degeneration of the normalized middle eigenvalue.

---

# 4. Pointwise quadratic coercivity away from the middle gap

C5-D constructs, for each normalized positive-middle direction:

$$
K=S/|S|
$$

a matrix:

$$
H_K
$$

and proves:

$$
H_K:Q
\ge
\frac{
\vartheta(S)
}{
4
}
(
|S|^2+|\omega|^2
).
$$

Moreover:

$$
|H_K|_F
$$

is uniformly bounded on the normalized trace-free sphere.

Thus, there exists a universal:

$$
c_Q>0
$$

such that:

## C5-E.2

If:

$$
\boxed{
\vartheta(S)\ge\delta>0,
}
$$

then:

$$
\boxed{
|Q(S,\omega)|
\ge
c_Q
\delta
(
|S|^2+|\omega|^2
).
}
$$

On the other hand:

$$
\boxed{
|Q|
\le
|S|^2
+
\frac{\sqrt2}{4}
|\omega|^2
\le
|S|^2+|\omega|^2.
}
$$

Therefore, in the region:

$$
\vartheta\ge\delta
$$

we have:

$$
\boxed{
|Q|
\asymp_\delta
|S|^2+|\omega|^2.
}
$$

---

# 5. Meaning

If the Q-weighted mass concentrates at:

$$
\vartheta\to0,
$$

that is pushing the genuine:

$$
|S|^2+|\omega|^2
$$

quadratic activity towards the middle-degenerate boundary.

It is not a false defect caused by the normalization of:

$$
Q/|Q|
$$

.

---

# 6. Q-weighted spatial probability measure

Take the selected adjoint/local core cutoff:

$$
\chi_j\ge0.
$$

Define:

$$
\boxed{
A_j^Q
=
\int
\chi_j|Q_j|dx.
}
$$

In the active Q motif:

$$
A_j^Q>0.
$$

Define:

$$
\boxed{
d\nu_j^Q(x)
=
\frac{
\chi_j(x)|Q_j(x)|
}{
A_j^Q
}
dx.
}
$$

Thus:

$$
\boxed{
\nu_j^Q
}
$$

is a probability measure.

---

# 7. Joint strain-direction / gap state

If:

$$
S_j(x)\ne0,
$$

define:

$$
\boxed{
V_j(x)
=
\frac{
S_j(x)
}{
|S_j(x)|
}
\in
S^4
\subset
\operatorname{Sym}_0(3).
}
$$

If:

$$
S_j=0,
$$

add the cemetery state:

$$
\partial_S.
$$

Define:

$$
\boxed{
\theta_j(x)
=
\vartheta(S_j(x))
\in
\left[
0,\frac16
\right].
}
$$

push-forward:

$$
\boxed{
\Xi_j^{S\theta}
=
(V_j,\theta_j)_\#
\nu_j^Q.
}
$$

state space:

$$
\boxed{
\mathcal K_{S\theta}
=
(S^4\cup\{\partial_S\})
\times
[0,1/6]
}
$$

is compact.

---

# 8. Middle-gap distribution function

Define:

$$
\boxed{
\mathfrak g_j(\delta)
=
\nu_j^Q
\{
\theta_j\le\delta
\}
}
$$

for:

$$
0<\delta<1/6.
$$

Extract a subsequence:

$$
\Xi_j^{S\theta}
\rightharpoonup
\Xi_\ast^{S\theta}.
$$

define the limit gap mass:

$$
\boxed{
\mathfrak g_\ast(\delta)
=
\Xi_\ast^{S\theta}
\{
\theta\le\delta
\}.
}
$$

---

# 9. Middle-gap defect mass

Define:

$$
\boxed{
\mathfrak G_\ast
=
\Xi_\ast^{S\theta}
\{
\theta=0
\}.
}
$$

equivalently:

$$
\boxed{
\mathfrak G_\ast
=
\lim_{\delta\downarrow0}
\mathfrak g_\ast(\delta).
}
$$

If:

$$
\mathfrak G_\ast>0,
$$

we say the:

$$
\boxed{
\textbf{Middle-Gap Defect Measure}
}
$$

is active.

---

# 10. Quadratic-direction barycenter

Additionally define:

$$
\boxed{
U_j(x)
=
\frac{
Q_j(x)
}{
|Q_j(x)|
}
\in
S^5
}
$$

on:

$$
Q_j\ne0.
$$

Then:

$$
\boxed{
\int
U_j
d\nu_j^Q
=
\frac{
B_j^Q
}{
A_j^Q
}.
}
$$

The Seven-Point cancellation extreme branch is:

$$
\boxed{
\left|
\int
U_jd\nu_j^Q
\right|
=
\kappa_j^Q
\to0.
}
$$

---

# 11. C5-E.3: Zero-Barycenter Limit Cannot Have a Single Strong-Middle Direction

Assume:

$$
\boxed{
\kappa_j^Q\to0.
}
$$

If:

$$
\Xi_\ast^{S\theta}
=
\delta_{(K,\theta_K)}
$$

with:

$$
\boxed{
\theta_K>0,
}
$$

then this is impossible.

### Proof

Take:

$$
0<\delta<\theta_K.
$$

By weak concentration,

for large $j$, almost all Q mass falls in:

- $\theta\ge\delta$;
- $V$ sufficiently close to $K$.

The C5-D strong-middle cone theorem thus gives:

$$
\kappa_j^Q
\ge
\gamma_K/2
$$

for large $j$,

which contradicts:

$$
\kappa_j^Q\to0
$$

. $\square$

### Conclusion

If the zero quadratic barycenter survives,

the strain-direction/gap limit must:

$$
\boxed{
\text{hit }\theta=0
}
$$

or:

$$
\boxed{
\text{remain directionally nontrivial}.
}
$$

---

# 12. Uniform strong-middle subset

Fix:

$$
\delta>0.
$$

Define:

$$
\boxed{
\mathcal S_\delta
=
\{
V\in S^4:
\vartheta(V)\ge\delta
\}.
}
$$

$\mathcal S_\delta$ is compact.

The C5-D cone radius and half-space margin can be chosen as uniform constants here:

$$
\boxed{
r_\delta>0,
\qquad
\gamma_\delta>0.
}
$$

schematically:

$$
r_\delta\gtrsim\delta,
$$

$$
\gamma_\delta\gtrsim\delta.
$$

---

# 13. C5-E.4: Quantitative Direction Anti-Concentration

Assume:

$$
\kappa_j^Q\le\kappa_0
<
\gamma_\delta.
$$

For any:

$$
K\in\mathcal S_\delta,
$$

define:

$$
B_{r_\delta}(K)
\subset S^4.
$$

If the middle-gap mass:

$$
\mathfrak g_j(\delta/2)
$$

has been separately excluded,

the C5-D cone-leakage theorem gives:

$$
\boxed{
\nu_j^Q
\left(
\{
\theta\ge\delta/2
\}
\setminus
B_{r_\delta}(K)
\right)
\ge
c_\delta
-
\mathfrak g_j(\delta/2)
}
$$

for a constant:

$$
c_\delta>0.
$$

### Interpretation

If the middle-gap mass is very small,

Q cancellation forces:

$$
\boxed{
\text{strain-direction probability cannot concentrate in any single strong-middle cone}.
}
$$

---

# 14. Directional variance lower bound

Under the same conditions,

if:

$$
\mathfrak g_j(\delta/2)
\le
c_\delta/2,
$$

then for any:

$$
K\in\mathcal S_\delta,
$$

$$
\boxed{
\int
|V_j-K|^2
d\nu_j^Q
\ge
\frac{
c_\delta
}{2}
r_\delta^2.
}
$$

Therefore:

$$
\boxed{
\textbf{Q cancellation + no middle-gap defect}
\Rightarrow
\textbf{nondegenerate directional dispersion}.
}
$$

---

# 15. From direction leakage to physical PDE stock

To convert direction dispersion into derivative stock,

we cannot directly equate the Q-weight with the strain-energy weight.

Therefore, C5-E performs another exact split.

Fix:

$$
0<\eta<1.
$$

Define:

$$
\boxed{
E_S(\eta)
=
\{
|S|^2
\ge
\eta|Q|
\},
}
$$

and:

$$
\boxed{
E_\omega(\eta)
=
\{
|S|^2
<
\eta|Q|
\}.
}
$$

---

# 16. Vorticity dominance on $E_\omega$

Since:

$$
|Q|
\le
|S|^2
+
c_\omega
|\omega|^2,
$$

where:

$$
\boxed{
c_\omega
=
\frac{\sqrt2}{4},
}
$$

on:

$$
E_\omega(\eta)
$$

we have:

$$
(1-\eta)|Q|
\le
c_\omega
|\omega|^2.
$$

Thus:

$$
\boxed{
|\omega|^2
\ge
\frac{
1-\eta
}{
c_\omega
}
|Q|.
}
$$

---

# 17. Direction-to-ray distance

Fix a unit:

$$
K\in S^4.
$$

If:

$$
|V-K|
\ge r,
$$

then there exists:

$$
c_r>0
$$

such that:

$$
\boxed{
\operatorname{dist}
(
V,
\{aK:a\ge0\}
)
\ge
c_r.
}
$$

For example, for:

$$
0<r\le1,
$$

we can choose:

$$
\boxed{
c_r\ge r/2.
}
$$

Thus, if the local mean is:

$$
\bar S=mK,
\qquad
m\ge0,
$$

then:

$$
\boxed{
|S-\bar S|
\ge
c_r|S|
}
$$

on:

$$
|S/|S|-K|\ge r.
$$

---

# 18. Standard weighted core Poincaré

Take the standard radius-$R$ core cutoff:

$$
\chi_R,
$$

set:

$$
\boxed{
\bar S_{\chi}
=
\frac{
\int\chi_RS
}{
\int\chi_R
}.
}
$$

Assume the standard weighted Poincaré constant:

$$
C_P
$$

such that:

$$
\boxed{
\int
\chi_R
|S-\bar S_\chi|^2
\le
C_P
R^2
\int_{B_{CR}}
|\nabla S|^2.
}
$$

---

# 19. Leakage mass

Assume a cone center:

$$
K
=
\bar S_\chi/|\bar S_\chi|
$$

has a nondegenerate strong-middle margin,

and Q cancellation forces:

$$
\boxed{
\int_{E_{\rm leak}}
\chi|Q|
\ge
\varepsilon_0
A_\chi^Q,
}
$$

where:

$$
E_{\rm leak}
=
\{
|S/|S|-K|
\ge r_0
\}.
$$

---

# 20. C5-E.5: Leakage → Derivative or Vorticity Dichotomy

Split:

$$
E_{\rm leak}
$$

into:

$$
E_{\rm leak}\cap E_S(\eta)
$$

and:

$$
E_{\rm leak}\cap E_\omega(\eta).
$$

At least one branch bears:

$$
\varepsilon_0A_\chi^Q/2.
$$

---

## Branch E-DER

If:

$$
\int_{E_{\rm leak}\cap E_S(\eta)}
\chi|Q|
\ge
\frac{
\varepsilon_0
}{2}
A_\chi^Q,
$$

then:

$$
\int
\chi
|S-\bar S_\chi|^2
\ge
c_{r_0}^2
\eta
\frac{
\varepsilon_0
}{2}
A_\chi^Q.
$$

weighted Poincaré gives:

$$
\boxed{
R^2
\int_{B_{CR}}
|\nabla S|^2
\ge
c
\eta
\varepsilon_0
A_\chi^Q.
}
$$

Define:

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
|\nabla S|^2,
}
$$

$$
\boxed{
a_R^Q
=
\frac{
R
}{
\nu^2
}
A_\chi^Q.
}
$$

Then:

$$
\boxed{
\mathfrak H_R
\ge
c
\eta
\varepsilon_0
a_R^Q.
}
$$

---

## Branch E-VORT

If:

$$
\int_{E_{\rm leak}\cap E_\omega(\eta)}
\chi|Q|
\ge
\frac{
\varepsilon_0
}{2}
A_\chi^Q,
$$

then by §16:

$$
\boxed{
\int
\chi|\omega|^2
\ge
c_\eta
\varepsilon_0
A_\chi^Q.
}
$$

Define the local critical vorticity stock:

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\int
\chi|\omega|^2.
}
$$

Then:

$$
\boxed{
\mathfrak W_R
\ge
c_\eta
\varepsilon_0
a_R^Q.
}
$$

---

# 21. C5-E.6: Q-Cancellation Spatial Debt Trichotomy

Under a nondegenerate local Q-intensity:

$$
a_R^Q\ge a_0>0
$$

,

a recurrent small quadratic mean:

$$
\kappa_Q\ll1
$$

must take at least one of the following routes:

$$
\boxed{
\text{Middle-Gap Defect}
}
$$

or:

$$
\boxed{
\mathfrak H_R
\gtrsim1
}
$$

or:

$$
\boxed{
\mathfrak W_R
\gtrsim1.
}
$$

That is:

$$
\boxed{
\textbf{Q Cancellation}
\Rightarrow
\textbf{Gap Concentration}
\vee
\textbf{Strain-Derivative Fluctuation}
\vee
\textbf{Vorticity-Dominant Leakage}.
}
$$

### This is the first major compression of this round.

---

# 22. Middle-gap degeneration is not a free escape

Now we handle:

$$
\vartheta\le\delta.
$$

The middle source density is:

$$
\boxed{
\lambda_2^+|S|^2
=
\xi_2(S)|S|^3.
}
$$

By C5-E.1:

$$
\xi_2
\le
\sqrt6\vartheta.
$$

Therefore, on:

$$
\vartheta\le\delta,
$$

$$
\boxed{
\lambda_2^+|S|^2
\le
\sqrt6
\delta
|S|^3.
}
$$

---

# 23. C5-E.7: Middle-Gap Load Forces Cubic Strain

If the measurable set:

$$
G_\delta
=
\{
\vartheta\le\delta
\}
$$

bears the middle load:

$$
\boxed{
M_{\delta}
=
\int_{G_\delta}
\lambda_2^+
|S|^2dx,
}
$$

then:

$$
\boxed{
\int_{G_\delta}
|S|^3dx
\ge
\frac{
M_\delta
}{
\sqrt6\,\delta
}.
}
$$

### Conclusion

If:

$$
M_\delta
$$

does not degenerate,

while:

$$
\delta\downarrow0,
$$

then:

$$
\boxed{
\|S\|_3^3
\to\infty
}
$$

at least at a rate of:

$$
\delta^{-1}
$$

.

---

# 24. Global derivative lower bound from cubic strain

Whole-space Sobolev / interpolation gives:

$$
\boxed{
\|S\|_3
\le
C
\|S\|_2^{1/2}
\|\nabla S\|_2^{1/2}.
}
$$

Thus:

$$
\boxed{
\|S\|_3^3
\le
C
\|S\|_2^{3/2}
\|\nabla S\|_2^{3/2}.
}
$$

Combined with C5-E.7:

$$
\boxed{
\|\nabla S\|_2
\ge
c
\frac{
M_\delta^{2/3}
}{
\delta^{2/3}
\|S\|_2
}.
}
$$

### Significance

If middle-gap degeneration is to maintain middle amplification,

it will also directly elevate the:

$$
\boxed{
D^2u\text{-level }L^2\text{ stock}
}
$$

unless enstrophy itself compensates.

---

# 25. Effective cubic amplitude

For any:

$$
f\in L^2\cap L^3,
\qquad
f\not\equiv0,
$$

define:

$$
\boxed{
A_{\rm eff}(f)
=
\frac{
\|f\|_3^3
}{
\|f\|_2^2
}.
}
$$

Since:

$$
\|f\|_3^3
\le
\|f\|_\infty
\|f\|_2^2,
$$

we have:

$$
\boxed{
A_{\rm eff}(f)
\le
\|f\|_\infty.
}
$$

---

# 26. Effective active volume

Define:

$$
\boxed{
V_{\rm eff}(f)
=
\frac{
\|f\|_2^6
}{
\|f\|_3^6
}.
}
$$

Its dimension is volume.

If:

$$
f
$$

is roughly constant on a set of volume:

$$
V,
$$

then:

$$
V_{\rm eff}\sim V.
$$

---

# 27. C5-E.8: Effective Active-Set Lemma

Fix:

$$
0<c<1.
$$

Define:

$$
\boxed{
E_c(f)
=
\{
x:
|f(x)|
\ge
cA_{\rm eff}(f)
\}.
}
$$

Then:

## Volume bound

$$
\boxed{
|E_c(f)|
\le
c^{-2}
V_{\rm eff}(f).
}
$$

### Proof

Chebyshev:

$$
|E_c|
\le
\frac{
\|f\|_2^2
}{
c^2A_{\rm eff}^2
}
=
c^{-2}
\frac{
\|f\|_2^6
}{
\|f\|_3^6
}.
$$

## Cubic activity bound

$$
\boxed{
\int_{E_c(f)}
|f|^3dx
\ge
(1-c)
\|f\|_3^3.
}
$$

### Proof

In the complement:

$$
|f|<cA_{\rm eff}.
$$

Thus:

$$
\int_{E_c^c}
|f|^3
\le
cA_{\rm eff}
\|f\|_2^2
=
c\|f\|_3^3.
$$

$\square$

---

# 28. Meaning

Large:

$$
\|S\|_3^3/\|S\|_2^2
$$

is not just high amplitude.

It guarantees the existence of a:

$$
\boxed{
\text{small effective-volume set}
}
$$

that carries at least a:

$$
1-c
$$

proportion of the cubic strain activity.

This is:

$$
\boxed{
\textbf{Strain-Amplitude Intermittency}.
}
$$

---

# 29. Normalized effective volume on an ancestry scale

Take:

$$
R>0.
$$

Define:

$$
\boxed{
\phi_{S,3}(R)
=
\frac{
V_{\rm eff}(S)
}{
R^3
}.
}
$$

If the local middle-gap load is normalized as:

$$
\boxed{
b_R^{mid}
=
\frac{
R^3
}{
\nu^3
}
M_\delta,
}
$$

and the global/local strain enstrophy stock is:

$$
\boxed{
e_R^S
=
\frac{
R
}{
\nu^2
}
\|S\|_2^2,
}
$$

then C5-E.7 gives:

$$
\|S\|_3^3
\ge
\frac{
\nu^3
}{
R^3
}
\frac{
b_R^{mid}
}{
\sqrt6\delta
}.
$$

Thus:

$$
\boxed{
\phi_{S,3}(R)
\le
6
\delta^2
\frac{
(e_R^S)^3
}{
(b_R^{mid})^2
}.
}
$$

---

# 30. C5-E.9: Middle-Gap → Effective-Volume Collapse

If along a subsequence:

$$
\boxed{
b_R^{mid}\ge b_0>0,
}
$$

and:

$$
\boxed{
e_R^S\le E_0<\infty,
}
$$

while:

$$
\delta\to0,
$$

then:

$$
\boxed{
\phi_{S,3}(R)
\lesssim
\delta^2
\to0.
}
$$

### Conclusion

If middle-gap degeneration continues to bear a nondegenerate middle load,

in the bounded strain-stock regime, it must convert into a:

$$
\boxed{
\textbf{vanishing effective active volume}.
}
$$

If:

$$
e_R^S
$$

is not bounded,

then it has already entered:

$$
\boxed{
\textbf{strain-enstrophy escape}.
}
$$

---

# 31. Volume-to-line sparseness pre-gate

C3-W pure geometric lemma:

If a set:

$$
A
$$

has a volume fraction in:

$$
B_r(x_0)
$$

of:

$$
<\delta_{sp}^3,
$$

then there exists a line direction through:

$$
x_0
$$

such that the one-dimensional occupancy is:

$$
\le\delta_{sp}.
$$

For the global effective set:

$$
E_c(S),
$$

since:

$$
|E_c(S)|
\le
c^{-2}
V_{\rm eff}(S),
$$

take:

$$
\boxed{
r_{sp}
\asymp
\delta_{sp}^{-1}
c^{-2/3}
V_{\rm eff}(S)^{1/3}.
}
$$

Then:

$$
E_c(S)
$$

exhibits, at any base point, a line direction with:

$$
\boxed{
1D\ \delta_{sp}\text{-sparseness}.
}
$$

---

# 32. Middle-gap sparseness scale

Using C5-E.9:

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
e_R^S
}{
(b_R^{mid})^{2/3}
}
}
$$

up to fixed constants.

Thus:

$$
\boxed{
\delta\downarrow0
}
$$

will push the strain cubic active set to an even finer sparse scale,

unless:

$$
e_R^S
$$

expands synchronously.

---

# 33. Relation to fixed-fraction $L^\infty$ strain superlevel sets

Since:

$$
A_{\rm eff}(S)
\le
\|S\|_\infty,
$$

if:

$$
0<c\le\lambda<1,
$$

then:

$$
\boxed{
\{
|S|
>
\lambda
\|S\|_\infty
\}
\subset
E_c(S).
}
$$

Therefore, E-c sparseness also applies to the fixed-fraction:

$$
|S|
$$

magnitude high set.

### But:

the published Grujić–Xu theorem tracks the component/sign superlevel sets of:

$$
D^ku
$$

or:

$$
D^k\omega
$$

.

Thus, there is still a field-interface gap.

---

# 34. C5-E derivative-intermittency pre-gate

Currently, C5-E can generate:

## From direction leakage

$$
\boxed{
\mathfrak H_R
=
\frac{
R^3
}{
\nu^2
}
\|\nabla S\|_2^2
\gtrsim1
}
$$

or:

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\|\omega\|_2^2
\gtrsim1.
}
$$

## From middle-gap degeneration

$$
\boxed{
\phi_{S,3}\ll1
}
$$

or:

$$
\boxed{
e_R^S\text{ large}.
}
$$

These are genuine:

$$
\boxed{
\textbf{derivative / intermittency pre-gates}.
}
$$

---

# 35. Published Grujić–Xu gate

The antecedent of Theorem 3.5:

At an appropriate later time after the escape time of:

$$
D^ku
$$

or:

$$
D^k\omega
$$

,

for any spatial point:

$$
x_0,
$$

there exists a scale:

$$
\rho
$$

such that the selected:

$$
\boxed{
\text{component/sign superlevel set}
}
$$

is 1D sparse on that scale.

Theorem 3.14 further requires a derivative-chain / analytic-time structure,

and forms an asymptotically critical route on the scale:

$$
\|D^ku\|_\infty^{-1/(k+1)}
$$

.

---

# 36. C5-E.10: Derivative-Gate Interface

For the strain intermittency obtained in C5-E to legitimately enter the published theorem,

it still requires:

## E-G1 — Field conversion

Conversion from the geometry of:

$$
S
$$

or:

$$
\nabla S
$$

to the component/sign superlevel geometry of some:

$$
D^ku
$$

or:

$$
D^k\omega
$$

.

## E-G2 — Threshold conversion

The C5-E effective amplitude:

$$
A_{\rm eff}
$$

must align with the theorem's threshold:

$$
\lambda
\|D^ku\|_\infty
$$

.

## E-G3 — Uniform-local / global set

The C5-E sparse set must genuinely control the full-space component/sign superlevel set used by the theorem,

and not merely control a subset within the ancestry core.

## E-G4 — Time gate

The geometry must appear at the theorem's admissible later analytic time:

$$
s=s(t).
$$

## E-G5 — Chain gate

If using Theorem 3.14,

ascending/descending derivative-chain hypotheses are required.

### Status

$$
\boxed{
\mathrm{OPEN\ INTERFACE}.
}
$$

---

# 37. Why we do not silently identify strain with $D u$

Although:

$$
S
=
\frac12
(
\nabla u+\nabla u^T
),
$$

pointwise large:

$$
|S|
$$

will force certain linear derivative combinations to be large.

However, the norm / component / sign reference of the published theorem is:

$$
D^\zeta u
$$

itself.

And:

$$
\nabla u
$$

also contains the antisymmetric vorticity part.

Therefore:

$$
\boxed{
\text{strain high-set sparse}
}
$$

does not automatically yield:

$$
\boxed{
\text{all relevant raw derivative component/sign high-sets sparse}.
}
$$

This distinction must be preserved.

---

# 38. Vorticity leakage branch and theorem interface

E-VORT of C5-E.5 gives:

$$
\boxed{
\mathfrak W_R
\gtrsim1.
}
$$

But the vorticity $L^2$ stock is likewise not:

$$
\boxed{
\text{vorticity superlevel sparseness}.
}
$$

If it can subsequently be proven that:

- vorticity active volume shrinkage;
- fixed-fraction vorticity high-set geometry;

then it can directly interface with the vorticity version of Grujić–Xu's Theorem 3.5 / 3.14.

Currently, it remains:

$$
\boxed{
\mathrm{OPEN}.
}
$$

---

# 39. C5-E limit taxonomy

For the recurrent Q-cancellation limit,

there are now only:

## E-L1 — Middle-gap defect

$$
\boxed{
\mathfrak G_\ast>0.
}
$$

## E-L2 — Direction-dispersion defect

The strong-middle mass does not degenerate,

but the strain direction measure cannot concentrate in a single cone.

## E-L3 — Strain-derivative fluctuation

$$
\boxed{
\mathfrak H_R
\gtrsim1.
}
$$

## E-L4 — Vorticity-dominant leakage

$$
\boxed{
\mathfrak W_R
\gtrsim1.
}
$$

Among these:

If E-L1 bears middle amplification,

it further converts into:

$$
\boxed{
\text{cubic strain intermittency}.
}
$$

---

# 40. Q motif is no longer free

C4-J:

$$
Q
=
\text{Seven-Point Quadratic Cancellation}
$$

was once a compact compensator.

C5-D:

$$
Q
\Rightarrow
\text{Gap}
\vee
\text{Direction Leakage}.
$$

C5-E:

$$
\boxed{
Q
\Rightarrow
\text{Middle-Gap/Cubic Intermittency}
\vee
\text{Strain-Derivative Fluctuation}
\vee
\text{Vorticity Leakage}.
}
$$

Therefore:

$$
\boxed{
\textbf{Q motif has been fully converted into PDE field defects}.
}
$$

---

# 41. Middle-gap concentration measure

For the gap limit:

$$
\mathfrak G_\ast>0,
$$

we can further examine the:

$$
\boxed{
\theta^{-1}
}
$$

weighted middle activity.

Define the truncated gap severity:

$$
\boxed{
\mathfrak J_j(\delta)
=
\int_{\{
0<\theta_j\le\delta
\}}
\frac{
1
}{
\theta_j
}
\,d\mu_j^{mid,Q}
}
$$

where:

$$
\mu_j^{mid,Q}
$$

is an appropriately normalized middle/Q joint measure.

If:

$$
\mathfrak G_\ast>0
$$

and the middle load does not degenerate at the gap layer,

then:

$$
\boxed{
\mathfrak J_j(\delta)
}
$$

must lose uniform integrability as:

$$
\delta\downarrow0
$$

.

### This round will not further expand on this severity measure,

leaving it as available metadata for C5-F.

---

# 42. X-Integration guards update

## G-GAPVAR

Preserve:

$$
\vartheta
=
\lambda_2^+\lambda_3/|S|^2
$$

rather than just recording $\lambda_2^+$.

## G-QPHYS

When:

$$
\vartheta\ge\delta
$$

the Q-weight can be compared with the strain/vorticity quadratic activity.

## G-QWEIGHT

The amount of direction leakage must be specified as Q-weighted, strain-weighted, or volume-weighted.

## G-SVLEAK

Before converting Q leakage to derivative, first split into:

$$
\text{strain-carrying}
\vee
\text{vorticity-dominant}.
$$

## G-CUBIC

Preserve cubic strain concentration when the middle-gap bears the middle load.

## G-EFFVOL

Effective-volume sparseness is a strain-amplitude pre-gate,

and must not be directly labeled as a Grujić–Xu theorem hypothesis.

## G-GXFIELD

The published derivative theorem requires $D^ku$ / $D^k\omega$ component/sign geometry.

---

# 43. True ETN Update

C5-E defect state:

$$
\boxed{
\Theta_\ast^{SDef}
=
\left\langle
\Xi_\ast^{S\theta},
\mathfrak G_\ast,
\mathfrak D_\ast^{dir},
\mathfrak H_\ast,
\mathfrak W_\ast,
\phi_{S,3}^\ast,
r_{sp}^\ast,
\mathsf G_{\rm der}
\right\rangle.
}
$$

Where:

- $\Xi^{S\theta}$ = Q-weighted strain-direction/gap measure;
- $\mathfrak G$ = middle-gap mass;
- $\mathfrak D^{dir}$ = direction-dispersion defect;
- $\mathfrak H$ = strain derivative stock;
- $\mathfrak W$ = vorticity stock;
- $\phi_{S,3}$ = cubic effective-volume ratio;
- $\mathsf G_{\rm der}$ = derivative theorem-interface status.

---

# 44. C5 strategic status

C5-A:

$$
\text{motif compactness}.
$$

C5-B:

$$
\text{temporal oscillation/concentration}.
$$

C5-C:

$$
\text{transition curvature constraints}.
$$

C5-D:

$$
\text{Strong-Middle vs Q-cancellation incompatibility}.
$$

C5-E:

$$
\boxed{
\textbf{Q-cancellation residual}
\to
\textbf{middle-gap / derivative / vorticity / intermittency defects}.
}
$$

Thus, the C5 spatial–matrix route no longer leaves a free Seven-Point motif.

---

# 45. What remains unresolved

## 1. Middle-gap route

middle-gap → cubic strain intermittency is proven,

but it has not yet interfaced with the raw:

$$
D^ku
$$

component/sign theorem gate.

## 2. Direction-leak route

Has been converted to:

$$
\mathfrak H_R
\vee
\mathfrak W_R,
$$

but stock ≠ geometric regularity.

## 3. Common far-pressure axis locking

The compressive-axis constraint of C5-D has not yet been coupled with the gap/dispersion defects.

## 4. Derivative order escalation

It is also not yet determined whether:

$$
k_j\to\infty
$$

can systematically absorb the C5-E defects.

---

# 46. New frontier: C5-F

The official next topic:

$$
\boxed{
\textbf{C5-F — Strain/Vorticity Defect Coupling,
Axis Locking, and Derivative-Gate Escalation}.
}
$$

---

# 47. C5-F proof obligations

## F1 — Middle-gap × compressive-axis limit

When:

$$
\vartheta\to0,
$$

investigate whether:

$$
e_1\otimes e_1-I/3
$$

still retains nontrivial pressure-axis information.

## F2 — Gap degeneration × axis locking

If common far pressure requires compressive axes to lock,

can middle-gap degeneration simultaneously maintain the Q zero-barycenter geometry?

## F3 — Direction dispersion × axis locking

Q cancellation requires strain directions to spread,

while pressure compensation requires compressive axes to fall into a common cone;

do these two form a second finite-dimensional incompatibility?

## F4 — Vorticity leakage × Miller orthogonality

When E-VORT is recurrent,

connect to the:

$$
P_{st}(\omega\otimes\omega)
$$

operator orthogonal congestion.

## F5 — Strain derivative stock × derivative amplitudes

From:

$$
\mathfrak H_R
$$

establish the:

$$
D^2u
$$

amplitude / multiplicity dichotomy.

## F6 — Cubic strain intermittency × derivative component sets

Test whether there exists a safe finite-component transfer:

$$
S\text{-magnitude sparse}
\to
D u\text{ component/sign sparse}
$$

or if a vorticity defect must be paid.

## F7 — Derivative order escalation

If k=1/2 interfaces repeatedly fail,

investigate whether the defect forces:

$$
k_j\to\infty.
$$

## F8 — Grujić–Xu gate audit

Strictly using the 2024 Theorem 3.5 / 3.14 hypotheses,

determine which C5 defect branch has truly connected to a theorem-ready closure.

---

# 48. Official Status

$$
\boxed{
\begin{aligned}
\vartheta\leftrightarrow\lambda_2^+/|S|
&:\ \mathrm{PROVED},\\
\vartheta\ge\delta\Rightarrow |Q|\gtrsim_\delta |S|^2+|\omega|^2
&:\ \mathrm{PROVED},\\
\text{Q-weighted gap measure compactification}
&:\ \mathrm{DEFINED/COMPACT},\\
\text{zero Q barycenter excludes single strong-middle limit}
&:\ \mathrm{PROVED},\\
\text{quantitative direction anti-concentration}
&:\ \mathrm{PROVED},\\
\text{direction leakage}\Rightarrow
\text{strain derivative or vorticity stock}
&:\ \mathrm{PROVED},\\
\text{middle-gap load}\Rightarrow\text{cubic strain}
&:\ \mathrm{PROVED},\\
\text{cubic strain}\Rightarrow\text{small effective active volume}
&:\ \mathrm{PROVED},\\
\text{effective active-set lemma}
&:\ \mathrm{PROVED},\\
\text{middle-gap}\Rightarrow\text{strain intermittency}
&:\ \mathrm{PROVED\ UNDER\ BOUNDED\ STRAIN\ STOCK},\\
\text{strain intermittency}\Rightarrow
\text{published Grujić--Xu gate}
&:\ \mathrm{NOT\ YET},\\
Q\text{ motif free compensation}
&:\ \mathrm{NO},\\
\text{global regularity}
&:\ \mathrm{OPEN}.
\end{aligned}
}
$$

---

# 49. Conclusion

C5-D compresses the Seven-Point Q-cancellation from a free finite-dimensional motif into:

$$
\boxed{
\text{Middle-Gap Degeneration}
\vee
\text{Direction Leakage}.
}
$$

C5-E now translates both of these branches back into PDE field quantities.

First,

the middle-gap variable:

$$
\vartheta(S)
=
\frac{
\lambda_2^+\lambda_3
}{
|S|^2
}
$$

and the normalized:

$$
\lambda_2^+/|S|
$$

are quantitatively equivalent.

If:

$$
\vartheta\ge\delta,
$$

then:

$$
\boxed{
|Q|
\gtrsim
\delta
(
|S|^2+|\omega|^2
).
}
$$

Thus, the Q-weighted gap concentration is a genuine physical quadratic-activity concentration.

Second,

if Q cancellation forces fixed cone leakage in the nondegenerate gap regime,

there are only two ways to pay for the leakage:

$$
\boxed{
\text{strain-carrying leakage}
}
$$

or:

$$
\boxed{
\text{vorticity-dominant leakage}.
}
$$

The former, via Poincaré, gives:

$$
\boxed{
\mathfrak H_R
=
\frac{
R^3
}{
\nu^2
}
\|\nabla S\|_2^2
\gtrsim
a_R^Q.
}
$$

The latter gives:

$$
\boxed{
\mathfrak W_R
=
\frac{
R
}{
\nu^2
}
\|\omega\|_2^2
\gtrsim
a_R^Q.
}
$$

Therefore:

$$
\boxed{
Q\text{-cancellation}
\Rightarrow
\text{Gap}
\vee
\text{Derivative}
\vee
\text{Vorticity}.
}
$$

Third,

the gap branch is also not free.

Since:

$$
\lambda_2^+|S|^2
=
\xi_2|S|^3,
$$

on:

$$
\vartheta\le\delta
$$

we have:

$$
\xi_2\lesssim\delta.
$$

Therefore, fixed middle amplification necessarily requires:

$$
\boxed{
\|S\|_3^3
\gtrsim
\delta^{-1}.
}
$$

Relative to a fixed $L^2$ strain stock,

this forces the effective volume:

$$
\boxed{
V_{\rm eff}
=
\frac{
\|S\|_2^6
}{
\|S\|_3^6
}
}
$$

to collapse.

And the explicit set:

$$
E_c
=
\{
|S|\ge
c\|S\|_3^3/\|S\|_2^2
\}
$$

carries a:

$$
\boxed{
\ge1-c
}
$$

proportion of cubic strain activity,

while:

$$
\boxed{
|E_c|
\le
c^{-2}V_{\rm eff}.
}
$$

Therefore, middle-gap degeneration truly becomes:

$$
\boxed{
\textbf{spatial intermittency}.
}
$$

But the final guard is extremely important:

Grujić–Xu 2024 Theorem 3.5 / 3.14 requires:

$$
\boxed{
D^ku
\text{ or }
D^k\omega
}
$$

component/sign superlevel-set sparseness,

as well as theorem-specific later-time and derivative-chain gates.

Our current:

$$
S,\quad\nabla S
$$

geometry cannot yet be directly substituted.

Thus, what C5-E reaches is a:

$$
\boxed{
\textbf{Derivative-Intermittency Pre-Gate},
}
$$

not a regularity proof.

The official next paper:

$$
\boxed{
\textbf{C5-F — Strain/Vorticity Defect Coupling,
Axis Locking, and Derivative-Gate Escalation}.
}
$$

---

# References

1. E. Miller, *A regularity criterion for the Navier–Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569; Arch. Rational Mech. Anal. 235 (2020).
2. E. Miller, *On the interaction of strain and vorticity for solutions of the Navier–Stokes equation*, arXiv:2407.02691v2; Pure and Applied Analysis 8 (2026).
3. Z. Grujić, L. Xu, *Asymptotic Criticality of the Navier–Stokes Regularity Problem*, Journal of Mathematical Fluid Mechanics 26, Article 53 (2024), DOI: 10.1007/s00021-024-00888-x; arXiv:1911.00974.
4. Z. Bradshaw, T.-P. Tsai, *On the local pressure expansion for the Navier–Stokes equations*, arXiv:2001.11526.
5. P. Constantin, *Pressure, Intermittency, Singularity*, arXiv:2301.04489.

# Internal dependencies

- `NS_C5D_SpatialMatrix_StrongMiddleQuadraticPressureObstruction_v0.1.md`
- `NS_C5C_TemporalCorrelation_CrossCurvatureOrdering_v0.1.md`
- `NS_C5B_TemporalYoung_PulsePhaseCompatibility_v0.1.md`
- `NS_C5A_RecordWindow_MotifCompactness_v0.1.md`
- `NS_C4J_CompensationRigidity_FinalSynchronizationAudit_v0.1.md`
- `NS_C3V_TurnoverPacking_StrainFluctuationEscape_v0.1.md`
- `NS_C3W_PressureRotation_StrainSparseness_v0.1.md`
- `NS_C3X_JointPressureStrain_AnalyticityGap_v0.1.md`
- `NS_C3Y_DerivativeChain_IntermittencyTradeoff_v0.1.md`
- `True ETN / Infinite-Dimensional Tension Field`
- `X_Integral_Unified_Program_v0.2.md`

Next:

$$
\boxed{
\textbf{C5-F — Strain/Vorticity Defect Coupling,
Axis Locking, and Derivative-Gate Escalation}
}
$$