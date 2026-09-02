# Positive Off-Axis Obstructions in the Explicit Formula
## Regional Negative Directions on the Zero Side, Computable Prime-Side Cones, and a ZFC-Auditable Contradiction Architecture

**英文題名：** *Positive Off-Axis Obstructions in the Explicit Formula: Regional Negative Directions on the Zero Side, Computable Prime-Side Cones, and a ZFC-Auditable Contradiction Architecture*  
**作者：** Neo.K (Chuan-Wei Hsu)  
**機構：** EveMissLab / Yiyannuo Technology Co., Ltd.  
**版本：** v0.1 (Internal Research Draft)  
**日期：** 2026-07-24  
**性質：** Riemann Hypothesis Research / Riemann–Weil Explicit Formula / Paley–Wiener Localization / Arithmetic Positivity Cone / Formal Auditing  
**前置文件：**
1. *From Core-Reduction to Equivariant Topology: Thinking Methods and Method Groups for Legitimate RH Verification*  
2. *Equivariant Zero Configuration Topology: RH Orbit-Type Stratification, Effective Divisor Semirings, and Positive Obstructions*  
3. *Stratified Zero Obstructions and Local-Global Lifting: From Rational Rectangular Certificates to Full Critical Strip Verification*  
4. *Equivariant Arithmetic Separation: From Orbit Space Localization to Admissible Test Functions for the $\zeta$ Explicit Formula*  
**狀態：** Internal draft; does not constitute a proof of the Riemann Hypothesis

---

## Important Declaration

This document is not a proof of the Riemann Hypothesis.

This document fixes a multiplicative group version of the Riemann–Weil explicit formula normalization, and decomposes the abstract "local negative witnesses" from the previous paper into three independently verifiable sub-problems:

1. **Regional Phase Shaping:**  
   Given an off-axis rectangle separated from the critical line, is it possible to construct a legitimate test function such that every potential zero in the rectangle produces a uniformly negative orbit block?

2. **Global Leakage Control:**  
   Can the total contribution of this test function to critical line zeros, other off-axis zeros, and zeros at infinity be unconditionally controlled?

3. **Arithmetic-Side Non-Negativity:**  
   Does the same test function fall into a cone whose non-negativity can be proven by finite prime data, archimedean terms, and strict tail bounds?

This document proposes a concrete Paley–Wiener regional phase shaping lemma and its proof architecture for the first item. This lemma only resolves the sign within the target region; it does not resolve the sum of zeros outside the region, nor does it prove arithmetic-side non-negativity.

This document simultaneously establishes a "support-prime activation filtration": the convolution square of a compactly supported test function activates only finitely many primes and prime powers. This allows the arithmetic side at each fixed support scale to be represented as a finite local matrix plus an archimedean matrix, though its sign is still not automatically non-negative.

This document does not rename full Weil positivity as a new theorem. The sign required to prove positivity for all legitimate convolution squares is precisely the existing core difficulty equivalent to, or extremely close to, RH.

---

# Abstract

Let
\[
F(z)=\xi\left(\frac12+z\right)
\]
and adopt the spectral coordinates
\[
s=\frac12+iw,
\qquad
w=-i\left(s-\frac12\right).
\]
RH is equivalent to $w$ being real for all non-trivial zeros.

This document fixes the Haar measure on the multiplicative group
\[
\mathbb R_+^\times=(0,\infty)
\]
as
\[
d^\times x=\frac{dx}{x}
\]
and the Mellin transform as
\[
\widetilde f(s)=\int_0^\infty f(x)x^s\,d^\times x
=\int_0^\infty f(x)x^{s-1}\,dx.
\]
For
\[
g^\sharp(x)=x^{-1}g(x^{-1}),
\qquad
f_g=g*\overline g^{\,\sharp},
\]
we have
\[
\widetilde f_g(s)
=
\widetilde g(s)\,
\overline{\widetilde g(1-\overline s)}.
\]
The Riemann–Weil explicit formula adopts:
\[
\widetilde f(0)
-\sum_{\rho}\widetilde f(\rho)
+\widetilde f(1)
=
\sum_v\mathcal W_v(f).
\]
If
\[
\widetilde g(0)=\widetilde g(1)=0,
\]
then
\[
Q_\zeta(g)
:=
-\sum_v\mathcal W_v(f_g)
=
\sum_\rho
\widetilde g(\rho)
\overline{\widetilde g(1-\overline\rho)}.
\]
Let
\[
G(w)=\widetilde g\left(\frac12+iw\right).
\]
The block for a zero $\rho=\frac12+iw_\rho$ is
\[
G(w_\rho)\overline{G(\overline{w_\rho})}.
\]
When $w_\rho\in\mathbb R$, this quantity is
\[
|G(w_\rho)|^2\ge0.
\]
When $w_\rho\notin\mathbb R$, the paired real block is
\[
B_w(G)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]
whose sign is indefinite.

This document further proves a regional phase shaping architecture. Let
\[
K\Subset\{w:\operatorname{Re}w>0,\ \operatorname{Im}w<0\}
\]
be a compact rectangle separated from the real axis and $\pm i/2$, and assume the square image
\[
K^2=\{w^2:w\in K\}
\]
and its conjugate can be approximated by polynomials. Then for any sufficiently small $\varepsilon>0$, one can construct a real-even
\[
\psi\in C_c^\infty(\mathbb R)
\]
such that its Fourier transform $G$ satisfies:
\[
G\left(\pm\frac i2\right)=0,
\]
and uniformly approximates $i$ on $K$. By real-even symmetry, it automatically holds that
\[
G(-w)=G(w),
\qquad
G(\overline w)=\overline{G(w)}.
\]
Therefore, on the entire orbit saturation set
\[
K\cup(-K)\cup\overline K\cup(-\overline K)
\]
we have
\[
2\operatorname{Re}(G(w)^2)\le-c<0.
\]
This construction depends only on the region $K$ and not on the exact locations of the zeros within the rectangle, thus it can interface with the rational rectangular winding number certificates from the previous paper.

On the arithmetic side, if
\[
\operatorname{supp}\psi\subseteq[-L/2,L/2],
\]
then the multiplicative support of $f_g$ is contained in
\[
[e^{-L},e^L].
\]
The finite place terms only involve finitely many prime powers satisfying
\[
m\log p\le L.
\]
This document therefore defines the support-prime activation set
\[
\mathcal P_L
=
\{p^m:m\log p\le L\}
\]
and the support filtration matrix
\[
M_L
=
M_\infty
+
\sum_{p^m\in\mathcal P_L}M_{p^m}.
\]
This yields a finite arithmetic certificate problem at a fixed scale.

Finally, the entire text compresses the RH pathway into a quantitative comparison:
\[
L_{\mathrm{sep}}(K,c,\varepsilon)
\stackrel{?}{\le}
L_{\mathrm{arith}+}(c,\varepsilon),
\]
where the left side is the minimum support cost required to shape the off-axis region into a uniformly negative block, and the right side is the maximum support scale at which the arithmetic side can still independently prove non-negativity. If the two never overlap, this pathway cannot prove RH; only if an auditable overlap exists for every hypothetical off-axis rectangle can a contradiction be formed.

**Keywords:** Riemann Hypothesis, Riemann–Weil Explicit Formula, Mellin Transform, Convolution Square, Paley–Wiener, Polynomial Approximation, Regional Negative Direction, Prime Activation Filtration, Positive Semi-Definite Certificate, ZFC

---

# 1. Research Position of this Document

## 1.1 Completed First Half

Previous research established:
\[
\text{Off-axis zeros}
\Longrightarrow
\text{Positive divisor obstructions}
\Longrightarrow
\text{Regular rectangular winding number certificates}.
\]

If RH fails, there exists a rational rectangle $R$ in the right half of the critical strip such that
\[
\omega_R(F)>0.
\]

## 1.2 Missing Second Half

It is necessary to lift:
\[
\omega_R(F)>0
\]
into a certain explicit formula test function $g_R$, such that:
\[
Q_\zeta(g_R)<0.
\]

And then independently prove from the prime side:
\[
Q_\zeta(g_R)\ge0.
\]

## 1.3 Decomposition in this Document

This document does not assume the complete lifting holds all at once, but decomposes it into:
\[
\boxed{
\text{Regional negative shaping}
+
\text{Global leakage bound}
+
\text{Arithmetic non-negative cone}.
}
\]

All three are indispensable.

---

# 2. Fixed Multiplicative Group Normalization

## 2.1 Multiplicative Group

Let:
\[
\mathbb G_m^+=\mathbb R_+^\times.
\]

Haar measure:
\[
d^\times x=\frac{dx}{x}.
\]

## 2.2 Mellin Transform

For
\[
f\in C_c^\infty(\mathbb R_+^\times)
\]
define:
\[
\widetilde f(s)
=
\int_0^\infty f(x)x^s\,d^\times x.
\]

## 2.3 Multiplicative Convolution

Define:
\[
(f*h)(x)
=
\int_0^\infty f(y)h(x/y)\,d^\times y.
\]

Then:
\[
\widetilde{f*h}(s)
=
\widetilde f(s)\widetilde h(s).
\]

## 2.4 Sharp Involution

Define:
\[
g^\sharp(x)=x^{-1}g(x^{-1}).
\]

And let:
\[
\overline g(x)=\overline{g(x)}.
\]

Then:
\[
\widetilde{\overline g^{\,\sharp}}(s)
=
\overline{\widetilde g(1-\overline s)}.
\]

## 2.5 Convolution Square

Define:
\[
f_g
=
g*\overline g^{\,\sharp}.
\]

Therefore:
\[
\boxed{
\widetilde f_g(s)
=
\widetilde g(s)
\overline{\widetilde g(1-\overline s)}.
}
\]

This is the quadratic form kernel fixed for use in this document.

---

# 3. Riemann–Weil Explicit Formula

## 3.1 Global Formula

For a legitimate test function $f$, adopt:
\[
\boxed{
\widetilde f(0)
-
\sum_{\rho\in Z_\zeta}
\widetilde f(\rho)
+
\widetilde f(1)
=
\sum_v\mathcal W_v(f).
}
\]

Where:

- $Z_\zeta$ is the multiset of non-trivial zeros;
- $v$ ranges over the archimedean and all finite places;
- $\mathcal W_v$ is the corresponding local distribution;
- The sum over zeros is understood according to the symmetry or regularization specified by the theorem.

## 3.2 Endpoint Vanishing

Require:
\[
\widetilde g(0)=0,
\qquad
\widetilde g(1)=0.
\]

Then:
\[
\widetilde f_g(0)
=
\widetilde g(0)\overline{\widetilde g(1)}
=
0,
\]
and:
\[
\widetilde f_g(1)
=
\widetilde g(1)\overline{\widetilde g(0)}
=
0.
\]

Thus:
\[
-\sum_\rho\widetilde f_g(\rho)
=
\sum_v\mathcal W_v(f_g).
\]

## 3.3 Weil Quadratic Form

Define:
\[
Q_\zeta(g)
=
-\sum_v\mathcal W_v(f_g).
\]

Then:
\[
\boxed{
Q_\zeta(g)
=
\sum_\rho
\widetilde g(\rho)
\overline{\widetilde g(1-\overline\rho)}.
}
\]

## 3.4 Sign Convention

This document adopts:
\[
\mathrm{RH}
\Longrightarrow
Q_\zeta(g)\ge0.
\]

Equivalently:
\[
\sum_v\mathcal W_v(f_g)\le0.
\]

All subsequent mentions of "arithmetic non-negativity" refer to the sign of $Q_\zeta$, not the sign of individual $\mathcal W_v$.

---

# 4. Logarithmic-Unitary Coordinates

## 4.1 Logarithmic Variables

Let:
\[
x=e^t.
\]

Define:
\[
\psi(t)
=
e^{t/2}g(e^t).
\]

Then:
\[
g(e^t)=e^{-t/2}\psi(t).
\]

## 4.2 Fourier–Mellin Correspondence

For:
\[
s=\frac12+iw,
\]
we have:
\[
\widetilde g\left(\frac12+iw\right)
=
\int_{\mathbb R}\psi(t)e^{iwt}\,dt.
\]

Define:
\[
G(w)
=
\widehat\psi(w)
=
\widetilde g\left(\frac12+iw\right).
\]

## 4.3 Endpoint Conditions

When $s=0$:
\[
w=\frac i2.
\]

When $s=1$:
\[
w=-\frac i2.
\]

So endpoint vanishing is equivalent to:
\[
\boxed{
G\left(\frac i2\right)
=
G\left(-\frac i2\right)
=
0.
}
\]

## 4.4 Real-Even Test Functions

If:
\[
\psi(t)\in\mathbb R,
\qquad
\psi(-t)=\psi(t),
\]
then:
\[
G(-w)=G(w),
\]
and:
\[
G(\overline w)=\overline{G(w)}.
\]

This perfectly matches the $\pm$ and conjugate symmetry of the zeros.

---

# 5. Orbit Blocks on the Zero Side

## 5.1 Spectral Coordinates

For a zero:
\[
\rho=\frac12+iw_\rho,
\]
we have:
\[
1-\overline\rho
=
\frac12+i\overline{w_\rho}.
\]

Therefore:
\[
\widetilde f_g(\rho)
=
G(w_\rho)
\overline{G(\overline{w_\rho})}.
\]

## 5.2 Critical Line Zeros

If:
\[
w_\rho\in\mathbb R,
\]
then:
\[
\widetilde f_g(\rho)
=
|G(w_\rho)|^2
\ge0.
\]

## 5.3 Off-Axis Zeros

If:
\[
w\notin\mathbb R,
\]
pairing $w$ with $\overline w$ yields:
\[
B_w(G)
=
G(w)\overline{G(\overline w)}
+
G(\overline w)\overline{G(w)}.
\]

Thus:
\[
\boxed{
B_w(G)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right).
}
\]

## 5.4 After Real-Even Symmetrization

If $G$ has the real structure:
\[
G(\overline w)=\overline{G(w)},
\]
then:
\[
\overline{G(\overline w)}=G(w).
\]

So:
\[
\boxed{
B_w(G)
=
2\operatorname{Re}(G(w)^2).
}
\]

If:
\[
G(w)\approx i,
\]
then:
\[
B_w(G)\approx-2.
\]

This is the algebraic core of regional negative shaping.

---

# 6. From Point Interpolation to Regional Shaping

## 6.1 Insufficiency of Point Interpolation

Specifying for a single hypothetical zero $w_0$:
\[
G(w_0)=i
\]
is easily accomplished through finite entire function interpolation.

But if $w_0$ is unknown, and we only know:
\[
w_0\in K,
\]
point interpolation cannot form a test function driven by a rectangular certificate.

## 6.2 Regional Target

We need a $G_K$ that depends only on $K$, such that:
\[
2\operatorname{Re}(G_K(w)^2)\le-c_K<0
\qquad
\forall w\in K.
\]

This is called **regional uniform negative shaping**.

## 6.3 Orbit Saturation

Let:
\[
K\Subset
\{w:
\operatorname{Re}w>0,\ 
\operatorname{Im}w<0
\}.
\]

Its orbit saturation is:
\[
K^G
=
K\cup(-K)\cup\overline K\cup(-\overline K).
\]

A real-even $G$ only needs to be shaped on $K$; the other three blocks are automatically determined by symmetry.

---

# 7. Paley–Wiener Regional Phase Shaping Lemma

## 7.1 Geometric Assumptions

Let $K$ be a compact rectangle satisfying:

\[
\operatorname{dist}(K,\mathbb R)>0,
\]

\[
\operatorname{dist}
\left(
K,\left\{\frac i2,-\frac i2\right\}
\right)>0,
\]

\[
\inf_{w\in K}|\operatorname{Re}w|>0.
\]

The last condition excludes the degeneracy of $w^2$ falling on the real axis.

Let:
\[
E=K^2\cup\overline{K^2},
\qquad
K^2=\{w^2:w\in K\}.
\]

Assume $\mathbb C\setminus E$ is connected; for sufficiently small, disjoint rectangles, this can usually be achieved by subdivision.

## 7.2 Lemma

### Lemma 7.1 (Regional Phase Shaping)

For any:
\[
0<\varepsilon<\frac14,
\]
there exists a real-even function:
\[
\psi\in C_c^\infty(\mathbb R)
\]
such that its Fourier transform $G$ satisfies:

1. 
   \[
   G(-w)=G(w);
   \]
2. 
   \[
   G(\overline w)=\overline{G(w)};
   \]
3. 
   \[
   G\left(\pm\frac i2\right)=0;
   \]
4. For all $w\in K$:
   \[
   |G(w)-i|<\varepsilon.
   \]

Therefore:
\[
2\operatorname{Re}(G(w)^2)
\le
-2\left(1-2\varepsilon-\varepsilon^2\right)
<0
\]
holds for all $w\in K$.

## 7.3 Proof Architecture

### Step 1: Paley–Wiener Basis Approximating a Constant

Take a real-even:
\[
h\in C_c^\infty(\mathbb R),
\qquad
\int h(t)\,dt=1.
\]

Let:
\[
h_\delta(t)=\delta^{-1}h(t/\delta).
\]

Its Fourier transform:
\[
H_\delta(w)=H(\delta w)
\]
uniformly approaches:
\[
1
\]
on any fixed compact set.

Choose $\delta$ sufficiently small such that $H_\delta$ has no zeros on $K^G$ and is close to $1$.

### Step 2: Incorporating Endpoint Zeros

Let:
\[
Z_0(w)=w^2+\frac14.
\]

Then:
\[
Z_0\left(\pm\frac i2\right)=0.
\]

By the geometric assumptions, $Z_0$ has no zeros on $K^G$.

### Step 3: Defining the Target Function on the Square Image

On $K^2$, define:
\[
q(u)
=
\frac{i}
{
(u+\frac14)
H_\delta(\sqrt u)
},
\]
where the expression should be understood as a holomorphic function descending to $u=w^2$ from the even function
\[
H_\delta(w).
\]

On $\overline{K^2}$, define by the conjugation rule:
\[
q(\overline u)=\overline{q(u)}.
\]

### Step 4: Polynomial Approximation

By the polynomial approximation condition of $E$, we can choose a polynomial $p(u)$ that uniformly approximates $q(u)$ on $E$.

Then, by taking:
\[
p_{\mathbb R}(u)
=
\frac12
\left(
p(u)+\overline{p(\overline u)}
\right)
\]
we obtain a polynomial with real coefficients while maintaining the approximation accuracy.

### Step 5: Constructing the Fourier Transform

Define:
\[
G(w)
=
\left(w^2+\frac14\right)
p_{\mathbb R}(w^2)
H_\delta(w).
\]

Then $G$:

- is an entire function;
- is real-even;
- is zero at $\pm i/2$;
- uniformly approximates $i$ on $K$.

### Step 6: Returning to the Compactly Supported Preimage

The polynomial multiplication:
\[
p_{\mathbb R}(w^2)H_\delta(w)
\]
corresponds to applying a finite-order constant-coefficient differential operator to $h_\delta$ on the inverse Fourier transform side.

Therefore, its inverse transform still belongs to:
\[
C_c^\infty(\mathbb R),
\]
and the support is not enlarged by differentiation.

The proof architecture is complete.

## 7.4 Essence of the Lemma

The lemma proves:

> For a finite off-axis region separated from the real axis, the Paley–Wiener class itself possesses sufficient degrees of freedom to form a uniformly negative zero orbit block throughout the entire region.

This is stronger than single-point interpolation and does not depend on the exact locations of the zeros within the rectangle.

## 7.5 What the Lemma Does Not Resolve

It does not control:

- $G$ outside $K^G$;
- The sum of all critical line zeros;
- Other off-axis zeros;
- Archimedean terms;
- The sign on the prime side;
- The optimal size of the required support scale.

---

# 8. From Rational Rectangular Certificates to Regional Negative Directions

## 8.1 Coordinate Transformation

The right half-strip rectangle from the previous paper:
\[
R\Subset
\left\{
z:
0<\operatorname{Re}z<\frac12
\right\}
\]
is transformed via:
\[
w=-iz
\]
into a spectral rectangle $K_R$ located in:
\[
\operatorname{Im}w<0.
\]

## 8.2 Horizontal Coordinates of Non-Trivial Zeros

If $z=\beta+i\gamma$, then:
\[
w=\gamma-i\beta.
\]

Non-trivial zeros have non-zero heights $\gamma$, so the rectangle can be subdivided such that:
\[
\operatorname{Re}w
\]
is separated from $0$.

## 8.3 Regional Negative Certificate

If:
\[
\omega_R(F)>0,
\]
then there exists at least one off-axis zero in $K_R$.

By the lemma, we can construct $G_R$ such that every zero orbit located in $K_R$ contributes:
\[
B_w(G_R)\le-c_R<0.
\]

Therefore, the total contribution of the target region satisfies:
\[
Q_{K_R}^{\mathrm{zero}}(G_R)
\le
-c_R\,\omega_R(F)
\]
up to orbit multiplicity and root multiplicity normalization.

## 8.4 The Truly Novel Implication (Arrow)

This document thus completes an implication with clear conditions:
\[
\boxed{
\omega_R(F)>0
\Longrightarrow
\text{Existence of a legitimate Paley-Wiener regional negative direction}.
}
\]

But we have not yet obtained:
\[
Q_\zeta(g_R)<0,
\]
because the contributions outside the region are not yet controlled.

---

# 9. Support and Finite Prime Activation

## 9.1 Support Scale

If:
\[
\operatorname{supp}\psi
\subseteq
[-L/2,L/2],
\]
then the corresponding multiplicative function $g$ is supported in:
\[
[e^{-L/2},e^{L/2}].
\]

## 9.2 Convolution Square Support

Because the supports of multiplicative convolutions multiply:
\[
\operatorname{supp}f_g
\subseteq
[e^{-L},e^L].
\]

## 9.3 Finite Place Distributions

Under the normalization of this document, the finite place terms can be written as:
\[
\mathcal W_p(f)
=
(\log p)
\sum_{m\ge1}
\left(
f(p^m)+p^{-m}f(p^{-m})
\right),
\]
whose exact interpretation and endpoint conventions are fixed by the adopted explicit formula theorem.

If:
\[
p^m>e^L,
\]
then:
\[
f(p^m)=0.
\]

Similarly, only the corresponding reciprocal terms falling within the support can be non-zero.

Therefore, we only need to consider:
\[
m\log p\le L.
\]

## 9.4 Prime Activation Set

Define:
\[
\mathcal P_L
=
\left\{
(p,m):
p\text{ is prime},\
m\ge1,\
m\log p\le L
\right\}.
\]

It is a finite set.

## 9.5 Arithmetic Filtration

As $L$ increases, new prime powers are activated only at discrete thresholds:
\[
L=m\log p.
\]

Thus we obtain:
\[
\mathcal P_{L_1}
\subseteq
\mathcal P_{L_2}
\qquad
(L_1\le L_2).
\]

This is called the **support-prime activation filtration**.

---

# 10. Tension Between Small and Large Supports

## 10.1 Advantages of Small Support

A small $L$ means:

- Fewer primes are activated;
- The arithmetic side is easier to compute exactly;
- The archimedean distribution may exhibit stronger local positivity;
- The certificate matrix is smaller.

When the support does not reach the minimum prime threshold, it is even possible that only archimedean places participate.

## 10.2 Disadvantages of Small Support

A small $L$ limits the spectral resolution of $G$.

To shape the phase in regions that are:

- Very high in altitude;
- Very close to the real axis;
- Very close to other zeros;

a larger $L$ is usually required.

## 10.3 Advantages of Large Support

A large $L$ allows for:

- Finer spectral localization;
- Smaller regional leakage;
- More complex interpolation and phase control.

## 10.4 Disadvantages of Large Support

A large $L$ activates more:
\[
p^m.
\]

The signs on the prime side become more complex, and the cost of exact certificates rises.

## 10.5 Core Quantitative Competition

Define the separation cost:
\[
L_{\mathrm{sep}}(K;c,\varepsilon)
\]
as the minimum support scale required to produce the target negative value $c$ with leakage outside the region not exceeding $\varepsilon$.

Define the arithmetic positivity radius:
\[
L_{\mathrm{arith}+}(\mathcal C)
\]
as the maximum scale at which one can still independently prove:
\[
Q_\zeta(g)\ge0
\]
within a specified structural cone $\mathcal C$.

We require:
\[
\boxed{
L_{\mathrm{sep}}(K;c,\varepsilon)
\le
L_{\mathrm{arith}+}(\mathcal C).
}
\]

---

# 11. Archimedean Local Positivity as an Edge Case

## 11.1 Usage of Known Background

Existing research on Weil positivity shows that under specific small supports, endpoint vanishing, and additional linear conditions, the archimedean distribution can provide a non-negative lower bound via positive operators or compressed traces.

This document only views this as local evidence that:
\[
L_{\mathrm{arith}+}>0
\]
might hold.

## 11.2 Cannot Directly Imply RH

Small support positivity only covers a small cone in the test function space.

If this cone is insufficient to perform phase shaping for arbitrary off-axis regions close to the real axis, it cannot exclude all off-axis zeros.

## 11.3 Requires Comparison, Not Renaming

One cannot claim "the archimedean part of RH is proven" just because:
\[
Q_\infty(g)\ge0
\]
holds in a small support subspace.

What truly needs to be compared is:
\[
\text{Support range of the positivity cone}
\]
with:
\[
\text{Minimum support to separate arbitrary off-axis regions}.
\]

---

# 12. Arithmetic Computable Cones

## 12.1 Purpose of Definition

We cannot use:
\[
\mathcal G_{\mathrm{arith}+}
=
\{g:Q_\zeta(g)\ge0\}
\]
as a definition, because this merely writes the conclusion into the set.

We need a cone generated by verifiable sufficient conditions.

## 12.2 Certificate Generator

Let:
\[
\mathsf{Cert}_L(g)
\]
contain:

1. The exact representation of $g$ or $\psi$;
2. Proof of support;
3. Proof of endpoint vanishing;
4. Lower bounds for the archimedean terms;
5. Exact intervals for each activated prime power term;
6. Legitimacy of the zero sums and local sums;
7. Upper bounds on the total error.

## 12.3 Computable Cone

Define:
\[
\mathcal C_L^{\mathrm{cert}}
=
\left\{
g:
\mathsf{Cert}_L(g)
\text{ proves }
Q_\zeta(g)\ge0
\right\}.
\]

The premise that this definition is not circular is that the certificate only uses:

- The explicit formula;
- Finite prime data;
- Archimedean analysis;
- Interval arithmetic;
- Unconditional estimates;

and does not use RH or equivalent criteria.

## 12.4 Conicity

If the certificate method is closed under:

- Non-negative scaling;
- Direct sums;
- Positive semi-definite matrix combinations;

then $\mathcal C_L^{\mathrm{cert}}$ can form a convex cone.

---

# 13. Finite-Dimensional Matrixification

## 13.1 Basis

Select a real-even smooth basis supported in:
\[
[-L/2,L/2]
\]
denoted as:
\[
\psi_1,\ldots,\psi_N.
\]

Let:
\[
\psi_c=\sum_{j=1}^Nc_j\psi_j,
\qquad
c\in\mathbb R^N.
\]

## 13.2 Fourier Evaluation Vector

Define:
\[
v(w)
=
\begin{pmatrix}
G_1(w)\\
\vdots\\
G_N(w)
\end{pmatrix}.
\]

Then:
\[
G_c(w)=c^\top v(w).
\]

## 13.3 Target Orbit Matrix

For an off-axis point $w$, define the real symmetric matrix:
\[
M_{\mathrm{orb}}(w)
=
2\operatorname{Re}
\left(
v(w)v(w)^\top
\right)
\]
under real-even normalization, such that:
\[
B_w(G_c)
=
c^\top M_{\mathrm{orb}}(w)c.
\]

## 13.4 Archimedean Matrix

Define:
\[
(M_\infty)_{jk}
=
-\mathcal W_\infty
\left(
g_j*\overline{g_k}^{\,\sharp}
\right)
\]
after Hermitian/real-symmetric conversion.

## 13.5 Finite Place Matrix

For each activated prime power, define the corresponding bilinear sampling matrix. Combine them as:
\[
M_{\mathrm{fin}}(L)
=
\sum_{(p,m)\in\mathcal P_L}
M_{p,m}.
\]

## 13.6 Arithmetic Matrix

\[
M_{\mathrm{arith}}(L)
=
M_\infty
+
M_{\mathrm{fin}}(L).
\]

Then:
\[
Q_\zeta(g_c)
=
c^\top M_{\mathrm{arith}}(L)c.
\]

This equality is understood according to the full explicit formula and endpoint conditions.

## 13.7 Positive Semi-Definite (PSD) Certificate

If it can be strictly proven that:
\[
M_{\mathrm{arith}}(L)\succeq0,
\]
then all test functions in the space spanned by the basis belong to the computable non-negative cone.

The proof method can be:

- Exact $LDL^\top$ decomposition;
- Rational interval Cholesky;
- Principal minors;
- sum-of-squares;
- Lean-verified positive semi-definite matrix certificates.

---

# 14. Regional Matrix Inequalities

## 14.1 Uniform Negative Direction

For a rectangle $K$, we hope to find $c$ such that:
\[
c^\top
M_{\mathrm{orb}}(w)c
\le-c_0
\qquad
\forall w\in K.
\]

This is a semi-infinite quadratic constraint problem.

## 14.2 Insufficiency of Discrete Grids

Checking for negative values only at finite grid points cannot guarantee it holds for the entire rectangle.

We need:

- Derivative Lipschitz bounds;
- Bernstein-type inequalities;
- Interval complex analysis;
- Complex interval envelopes over the rectangle.

## 14.3 Exact Regional Certificate

A regional negative certificate should include:
\[
\sup_{w\in K}
c^\top M_{\mathrm{orb}}(w)c
\le-c_0.
\]

## 14.4 Combination with Winding Number Certificates

If:
\[
\omega_R(F)\ge1
\]
and $K=-iR$, then there is at least one zero in the region, hence the target negative contribution is at least:
\[
-c_0.
\]

This does not require knowing the exact locations of the zeros.

---

# 15. Unconditional Control of the Infinity Tail

## 15.1 Paley–Wiener Decay

If:
\[
\psi\in C_c^\infty([-L/2,L/2]),
\]
then for any $N\ge0$, in the fixed horizontal strip:
\[
|\operatorname{Im}w|\le\frac12
\]
there exists a constant $C_{N,\psi,L}$ such that:
\[
|G(w)|
\le
C_{N,\psi,L}
e^{(L/2)|\operatorname{Im}w|}
(1+|\operatorname{Re}w|)^{-N}.
\]

## 15.2 Orbit Block Bounds

Therefore:
\[
|B_w(G)|
\le
2C_{N,\psi,L}^2
e^{L|\operatorname{Im}w|}
(1+|\operatorname{Re}w|)^{-2N}.
\]

In the critical strip:
\[
|\operatorname{Im}w|<\frac12,
\]
so the exponential factor has a uniform upper bound:
\[
e^{L/2}.
\]

## 15.3 Zero Counting

Using the unconditional zero counting:
\[
N(T)=O(T\log T),
\]
the number of zeros in height shells can be controlled to polynomial-logarithmic growth.

## 15.4 Tail Summability

When $N$ is sufficiently large:
\[
\sum_{|\operatorname{Re}w_\rho|>T}
|B_{w_\rho}(G)|
\]
converges, and can provide an upper bound that decays as $T\to\infty$.

## 15.5 Resolved and Unresolved Issues

This demonstrates:

> For a fixed test function, the tail of zeros at infinity can in principle be controlled using unconditional zero counting and Paley–Wiener decay.

What remains unresolved is the positive leakage from other unknown off-axis zeros within the finite control window.

---

# 16. Lowest Off-Axis Orbit Reduction

## 16.1 Assumption for Contradiction

Assume there exist off-axis zeros.

By the discreteness of zeros and the finite number of zeros up to a given height, we can select the minimum positive height level among off-axis zeros:
\[
T_\ast
=
\min
\left\{
|\operatorname{Re}w_\rho|:
w_\rho\notin\mathbb R
\right\}.
\]

Here $\operatorname{Re}w$ corresponds to the traditional zero height.

## 16.2 Below the Lowest Level

In:
\[
|\operatorname{Re}w|<T_\ast
\]
all zeros are located on the real axis.

For real-even convolution squares, their contributions are non-negative.

## 16.3 Orbits at the Same Height

There may be multiple off-axis orbits at the lowest height.

All off-axis orbits at the same height should be included in a finite family of target regions, rather than assuming uniqueness.

## 16.4 Above the Height

Higher zeros form the tail and the finite intermediate window:

- The sufficiently high part can be controlled by decay;
- The finite unknown off-axis orbits between the target and the tail truncation still require leakage bounds.

## 16.5 Value

The lowest off-axis reduction avoids "unknown off-axis positive leakage below the target," but it cannot completely eliminate unknown contributions above the target.

---

# 17. Tension Between Target Dependence and Arithmetic Independence

## 17.1 Weak Witnesses

Weak witnesses can depend on:

- The exact locations of off-axis zeros;
- The locations of other zeros;
- The complete set of zeros.

Such witnesses are easily constructed by interpolation, but their arithmetic side usually cannot be independently proven positive in advance.

## 17.2 Regional Witnesses

Regional witnesses only depend on:

- A rational rectangle;
- The support scale;
- Error parameters.

They can interface with winding number certificates and do not require zero coordinates.

The phase shaping lemma in this document belongs to this category.

## 17.3 Arithmetic-Native Witnesses

Stronger witnesses are directly generated by:

- Bases with rational coefficients;
- Finite prime data;
- Archimedean operators;
- Positive semi-definite programming.

They do not depend on any unknown zeros.

## 17.4 The Truly Required Version

The most ideal form of a non-circular proof is:

\[
\text{Rectangle }R
\longmapsto
g_R
\]
determined jointly by regional geometry and arithmetic data, simultaneously satisfying:

\[
\text{Regional negative shaping}
\]
and:
\[
\text{Arithmetic non-negative certificate}.
\]

---

# 18. Contradiction Certificate Architecture

## 18.1 Input

Assume there is a regular rectangle $R$ and:
\[
\omega_R(F)>0.
\]

## 18.2 Regional Negative Certificate

Construct $g_R$, proving:
\[
Q_R^{\mathrm{target}}(g_R)
\le-c_R<0.
\]

## 18.3 Leakage Certificate

Prove:
\[
Q_{\mathrm{rest}}^{\mathrm{zero}}(g_R)
\le E_R.
\]

This is an upper bound, as we must exclude other zeros from producing positive values sufficient to offset the negative contribution.

## 18.4 Dominance Condition

Require:
\[
E_R<c_R.
\]

Therefore:
\[
Q_\zeta(g_R)<0.
\]

## 18.5 Arithmetic Certificate

On the other hand, from:
\[
g_R\in\mathcal C_L^{\mathrm{cert}}
\]
we obtain:
\[
Q_\zeta(g_R)\ge0.
\]

## 18.6 Contradiction

\[
Q_\zeta(g_R)<0
\quad\land\quad
Q_\zeta(g_R)\ge0.
\]

Thus:
\[
\omega_R(F)=0.
\]

If this is completed for all regular rational rectangles, then RH holds.

---

# 19. Conditional Main Theorem

### Theorem 19.1 (Regional Certificate-Type Conditional Theorem)

Assume that for every regular rational rectangle $R$ in the right half of the critical strip, there exists an algorithm or ZFC-definable procedure that generates $g_R$, and it can be proven that:

1. If $\omega_R(F)>0$, then the contribution of zeros in the target region is at most $-c_R<0$;
2. The contribution of all non-target zeros is at most $E_R<c_R$;
3. $g_R$ satisfies all legitimacy conditions of the explicit formula;
4. From finite prime data and archimedean certificates, it can be proven that:
   \[
   Q_\zeta(g_R)\ge0.
   \]

Then RH holds.

### Proof

If RH fails, by the countable rectangle verification theorem, there exists $R$ such that:
\[
\omega_R(F)>0.
\]

By 1 and 2:
\[
Q_\zeta(g_R)
\le
-c_R+E_R
<0.
\]

By 4:
\[
Q_\zeta(g_R)\ge0.
\]

Contradiction. Therefore, the winding number of all rectangles is zero, and RH holds. Q.E.D.

## 19.2 Status of the Theorem

This theorem is a certificate architecture, not a proof of RH.

This document only provides a construction architecture for the "regional uniform negative shaping" of condition 1; conditions 2 and 4 are not yet completed.

---

# 20. Where It Might Again Be Equivalent to RH

## 20.1 Global Arithmetic Matrix Non-Negativity

If it is proven for a growing family dense in the test function space that:
\[
M_{\mathrm{arith}}(L)\succeq0
\quad
\forall L,
\]
and this can pass to the limit, this is very likely already full Weil positivity.

## 20.2 Zero Leakage for Arbitrary Regions

Claiming that for every off-axis region there exists a legitimate test function that completely eliminates all other zeros might imply an overly strong interpolation capability over the entire set of zeros.

## 20.3 Using Tail Bounds Under RH

Certain fine zero spacing, density, or spectral estimates might already assume RH.

## 20.4 Renaming the Conclusion as an "Arithmetic Cone"

If the arithmetic cone is defined as:
\[
\{g:Q_\zeta(g)\ge0\},
\]
then the intersection problem is merely a tautology.

---

# 21. ZFC and Formal Auditing

## 21.1 Definition Modules

```text
MultiplicativeGroupPositive
HaarMeasureMul
MellinTransform
MulConvolution
SharpInvolution
WeilConvolutionSquare
```

## 21.2 Explicit Formula Interfaces

```text
RiemannWeilTestClass
FinitePlaceDistribution
ArchimedeanDistribution
ExplicitFormula
EndpointVanishing
WeilQuadraticForm
```

The explicit formula should be imported as a proven external theorem, not as a new axiom.

## 21.3 Regional Shaping Modules

```text
SpectralRectangle
OrbitSaturation
SquareImageCompact
PolynomialApproximationHypothesis
PaleyWienerPhaseShaper
UniformNegativeOrbitBlock
```

## 21.4 Support Filtration Modules

```text
LogSupportRadius
ConvolutionSupport
ActivatedPrimePowers
FinitePrimeContribution
```

## 21.5 Matrix Certificates

```text
TestBasis
ArithmeticMatrix
OrbitMatrix
IntervalPSD
RegionalNegativeBound
```

## 21.6 Trust Boundaries

The following must be listed:

- Complex analysis function libraries;
- Mellin/Fourier transform normalizations;
- Sources for the explicit formula;
- Polynomial approximation theorems;
- Zero counting theorems;
- Prime list generation;
- Interval arithmetic;
- Positive semi-definite certificate checkers.

## 21.7 Prohibited Hidden Assumptions

The following must not be used as unmarked axioms:

```text
all_arithmetic_matrices_psd
all_regional_leakage_small
all_off_axis_rectangles_separable_within_positive_radius
RH
WeilPositivity
```

---

# 22. Computational Prototypes

## 22.1 Phase 1: Pure Regional Shaping

Input:

- Off-axis rectangle $K$;
- Support $L$;
- Basis dimension $N$.

Solve:
\[
\min_c
\sup_{w\in K}
2\operatorname{Re}(G_c(w)^2)
\]
and require:
\[
G_c(\pm i/2)=0.
\]

## 22.2 Phase 2: Incorporating On-Axis Leakage

Incorporate:
\[
\int_{\mathbb R}
|G_c(t)|^2\,d\mu_{\mathrm{majorant}}(t)
\]
or discrete upper bounds derived from zero counting.

## 22.3 Phase 3: Incorporating Prime Matrices

Construct:
\[
M_{\mathrm{arith}}(L).
\]

Find a solution that simultaneously satisfies:

\[
c^\top M_{\mathrm{arith}}(L)c\ge0
\]
and:
\[
\sup_{w\in K}
c^\top M_{\mathrm{orb}}(w)c<0.
\]

## 22.4 Phase 4: Exactification

Convert floating-point candidates to:

- Rational coefficients;
- Interval certificates;
- Exact support;
- Strict regional upper bounds;
- PSD certificates.

## 22.5 Experimental Determination

If it is repeatedly found that:

\[
L_{\mathrm{sep}}(K)
>
L_{\mathrm{arith}+},
\]
then this pathway may possess a structural incompatibility.

---

# 23. What This Document Truly Accomplishes

This document accomplishes:

1. Fixing the multiplicative group Riemann–Weil normalization;
2. Fixing the sign direction of $Q_\zeta$;
3. Converting endpoint vanishing to $G(\pm i/2)=0$;
4. Expanding the critical line modulus square and off-axis indefinite blocks;
5. Lifting single-point negative interpolation to a regional uniform negative shaping problem;
6. Proposing the Paley–Wiener regional phase shaping lemma and construction;
7. Connecting rational rectangular winding number certificates to regional negative directions;
8. Establishing the support-prime activation filtration;
9. Establishing the arithmetic finite matrix and PSD certificate framework;
10. Providing an unconditional control direction for the tail of zeros at infinity;
11. Establishing the lowest off-axis orbit reduction;
12. Establishing a complete ZFC certificate architecture.

---

# 24. What This Document Leaves Unfinished

This document does not accomplish:

1. A unified leakage upper bound for other unknown off-axis zeros within the finite control window;
2. Providing optimal support constants for the regional shaping lemma;
3. Establishing non-trivial large-support arithmetic non-negative cones;
4. Proving that the regional shaping function falls into this non-negative cone;
5. Formalizing the complete archimedean principal value distribution;
6. Establishing any contradiction certificate sufficient to exclude actual rectangles;
7. Proving RH.

---

# 25. Next Round of Research Directions

The four methodological papers originally planned for this series are now complete.

The next round should not continue adding synonymous RH equivalents, but should pivot into two engineering branches.

## Branch A: Regional Phase Shaping Prototype

Establish:

- Real-even bump function basis;
- Endpoint zero operators;
- Rectangular complex interval evaluation;
- Minimum support search;
- Regional uniform negative certificates.

## Branch B: Arithmetic Matrix Prototype

Fix a finite-dimensional basis and implement:

- Archimedean matrices;
- Activated prime power matrices;
- Interval PSD;
- Support threshold scanning;
- Intersection testing with regional negative matrices.

Only after completing both prototypes can it be determined whether:
\[
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\]
possesses actual research space.

---

# 26. Conclusion

This document further decomposes the abstract intersection problem from the previous paper:
\[
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\stackrel{?}{\ne}\varnothing
\]
into operable structures.

The first main result is regional phase shaping:

\[
\boxed{
\text{Off-axis rectangle}
\Longrightarrow
\text{Paley-Wiener regional uniform negative direction}.
}
\]

This construction uses:

- Logarithmic-Mellin transform;
- Real-even Fourier symmetry;
- $w^2$ orbit quotient;
- Polynomial approximation;
- Endpoint factor $w^2+\frac14$;
- Differential closure of compactly supported bump functions.

The second main structure is the support-prime activation filtration:

\[
\boxed{
\operatorname{supp}\psi
\subseteq[-L/2,L/2]
\Longrightarrow
\text{Activates only finite prime powers with }m\log p\le L.
}
\]

This makes the arithmetic side at each fixed scale a finite data problem.

However, a core tension still exists between the two structures:

\[
\text{Fine spectral separation}
\Longrightarrow
L\text{ increases}
\Longrightarrow
\text{More prime terms and harder arithmetic signs}.
\]

Therefore, the true determinant of this pathway is not yet another RH equivalent, but rather:

\[
\boxed{
L_{\mathrm{sep}}(K;c,\varepsilon)
\stackrel{?}{\le}
L_{\mathrm{arith}+}(\mathcal C).
}
\]

If this overlap can be established for arbitrary off-axis rectangles, coupled with finite window leakage and infinity tail control, one can form:

\[
Q_\zeta(g_R)<0
\quad\land\quad
Q_\zeta(g_R)\ge0.
\]

If the overlap cannot be established, the topological-explicit formula pathway will halt at a precise but insufficient verification architecture.

Thus, this document does not prove RH, but it completes the most important technical compression of this round:

> **The off-axis region itself can be shaped into a uniformly negative direction by legitimate Paley–Wiener test functions; what remains truly unresolved is whether this negative direction can, while controlling all other zeros, fall into an arithmetic non-negative cone that does not take RH as a premise.**

---

# Appendix A: Main Notation

| Symbol | Meaning |
|---|---|
| $d^\times x$ | Multiplicative Haar measure $dx/x$ |
| $\widetilde f$ | Mellin transform |
| $g^\sharp$ | $x^{-1}g(x^{-1})$ |
| $f_g$ | $g*\overline g^{\,\sharp}$ |
| $\mathcal W_v$ | Riemann–Weil local distribution |
| $Q_\zeta$ | Weil quadratic form under the notation of this document |
| $\psi$ | Logarithmic-unitary test function |
| $G$ | $\widehat\psi(w)=\widetilde g(1/2+iw)$ |
| $B_w(G)$ | Off-axis orbit block |
| $K$ | Off-axis spectral rectangle |
| $L$ | Logarithmic support scale |
| $\mathcal P_L$ | Activated prime power set |
| $M_{\mathrm{arith}}(L)$ | Fixed-support arithmetic matrix |
| $L_{\mathrm{sep}}$ | Regional separation cost |
| $L_{\mathrm{arith}+}$ | Arithmetically provable non-negative radius |

---

# Appendix B: Logical Status Table

| Proposition | Status |
|---|---|
| Riemann–Weil explicit formula | Known external theorem |
| Relationship between Weil positivity and RH | Known background |
| Critical line block is modulus square | Algebraic identity |
| Off-axis block sign is indefinite | Algebraic identity |
| Finite support activates only finite prime powers | Direct consequence of support |
| Paley–Wiener regional phase shaping | Construction architecture of this document; requires full theorem auditing before publication |
| Infinity tail can be controlled by rapid decay | Standard analytical architecture |
| All unknown off-axis leakage in finite window can be controlled | Unproven |
| Large support arithmetic matrix is non-negative | Unproven |
| All rectangles can generate contradiction certificates | Unproven; sufficient to imply RH |
| RH | Unproven |

---

# Appendix C: Circularity Checklist

Any candidate certificate must answer:

1. Does it use the assumption that "all other zeros are on the critical line"?
2. Does it use zero density bounds under RH?
3. Is the arithmetic cone defined directly by $Q_\zeta\ge0$?
4. Does it only check regional negative values on a finite grid?
5. Does it prove $G(\pm i/2)=0$?
6. Are the Mellin and local distribution normalizations fixed?
7. Are all activated prime powers controlled?
8. Is the archimedean principal value term controlled?
9. Are non-target off-axis zeros within the finite window controlled?
10. Is floating-point PSD mistakenly treated as exact PSD?
11. Are the Axiom of Choice, approximation theorems, and external numerical libraries used explicitly listed?
12. Can all additional assumptions be eliminated back to ZFC?

---

# Appendix D: Reference Background

1. A. Weil, *Sur les formules explicites de la théorie des nombres premiers*, 1952.  
2. A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica 5 (1999), 29–106.  
3. A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean place*, Selecta Mathematica 27 (2021); arXiv:2006.13771.  
4. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Annales de l’Institut Fourier 57 (2007); arXiv:math/0404394.  
5. Classical Paley-Wiener theorem, Mergelyan's polynomial approximation theorem, and Guinand-Weil explicit formula literature.  

---

# Appendix E: Version Boundaries

v0.1 has completed:

- Fixing multiplicative group normalization;
- Expanding finite place activation rules;
- Regional phase shaping construction;
- Interface from rectangular certificates to negative directions;
- Arithmetic matrix and PSD architecture;
- Tail control framework;
- Support cost comparison;
- ZFC auditing specifications.

v0.1 has not yet completed:

- Full publication-grade proof of the regional shaping lemma;
- Lean formalization of the archimedean distribution;
- Unknown off-axis leakage theorem for finite windows;
- Actual matrix prototypes;
- Arithmetic non-negative cones;
- Any proof of RH.