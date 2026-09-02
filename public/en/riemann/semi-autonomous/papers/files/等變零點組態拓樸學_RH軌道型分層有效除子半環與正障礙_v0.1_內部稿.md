# Equivariant Topology of Zero Configurations
## Orbit-Type Stratification, Effective Divisor Semirings, and Positive Obstructions for the Riemann Hypothesis

**English Title:** *Equivariant Topology of Zero Configurations: Orbit-Type Stratification, Effective Divisor Semirings, and Positive Obstructions for the Riemann Hypothesis*  
**Author:** Neo.K (Chuan-Wei Hsu)  
**Institution:** EveMissLab / Yiyannuo Technology Co., Ltd.  
**Version:** v0.1 (Internal Research Draft)  
**Date:** 2026-07-24  
**Nature:** Equivariant Topology / Complex Analysis / Zero Configurations / Effective Divisors / RH Decision Domain Research  
**Prerequisite Document:** *From Centering to Equivariant Topology: Thinking Methods and Method Groups for the Legitimate Decision of the RH*  
**Status:** Internal draft; does not constitute a proof of the Riemann Hypothesis

---

## Important Declaration

This document is not a proof of the Riemann Hypothesis.

This document establishes the first technical topological branch of the Riemann Hypothesis after centering: treating the zeros of the completed function as locally finite effective divisors under a finite group action, establishing orbit-type decomposition, configuration space topology, idempotent axial projection, effective orbit-type semirings, irreducible off-axis positive obstructions, and obstruction filtration expanded by height.

The main propositions proved in this document fall into the following categories:

1. Definitions and well-definedness;
2. Equivariant reformulations of zero symmetry;
3. Equivalence between RH and certain fixed-point or positive obstruction vanishing conditions;
4. Orbit-type classification within finite windows;
5. Interfaces between analytic function perturbations and local zero configuration stability.

The above results do not automatically imply that all off-axis obstructions are zero. A true proof of RH still requires deducing the vanishing of all off-axis positive obstructions defined in this document from the independent analytic and arithmetic structures of \(\xi\).

---

# Abstract

Let
\[
F(z)=\xi\left(\frac12+z\right),
\]
and let the closed critical strip and its interior be
\[
S=\left\{z\in\mathbb C:\left|\operatorname{Re}z\right|\le\frac12\right\},
\qquad
X=S^\circ.
\]
The nontrivial zeros of the completed function all lie in \(X\). The functional equation and the conjugate real structure generate the Klein four-group after centering
\[
G=\langle a,b\rangle\cong C_2\times C_2,
\qquad
a(z)=-z,\quad b(z)=\overline z,
\]
where the fixed-point set of the critical reflection
\[
j=ab,\qquad j(z)=-\overline z
\]
is precisely the imaginary axis
\[
A=\operatorname{Fix}(j)=i\mathbb R.
\]

This document represents the zeros of \(F\) as a locally finite \(G\)-invariant effective divisor on \(S\) with support in \(X\)
\[
D_F=\sum_\rho m_\rho[\rho].
\]
Effective divisors can also be viewed as integer-valued positive Radon measures. Endowing the space of locally finite divisors with the vague topology allows the study of the creation, movement, merging, and orbit-type degeneration of zero orbits within finite height windows.

This document first classifies the realizable stabilizer types of \(G\) on \(S\). General off-axis and non-real points have trivial stabilizers and four-point orbits; non-zero imaginary axis points have \(\langle j\rangle\) stabilizers and two-point orbits; non-zero real axis points have \(\langle b\rangle\) stabilizers and two-point orbits; the origin has the full group stabilizer. RH is thus equivalent to the entire support of \(D_F\) lying in the orbit-type strata containing \(j\).

Secondly, this document defines a suitable axial retraction on the closed strip \(S\)
\[
r(z)=i\,\operatorname{Im}z.
\]
Since \(S\) is compact in the horizontal direction, \(r:S\to A\) is a proper continuous map, thus the pushforward can be well-defined on locally finite divisors
\[
\mathcal R(D)=r_*D.
\]
This operator is continuous and idempotent, and satisfies
\[
\mathcal R(D)=D
\iff
\operatorname{supp}D\subseteq A.
\]
Therefore
\[
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
\]

To prevent off-axis obstructions from canceling out due to positive and negative coefficients after groupification, this document introduces the positive Burnside semiring of finite \(G\)-sets
\[
A^+(G),
\]
and the orbit-type value within a finite window
\[
\tau_W(D)\in A^+(G).
\]
By retaining all generators whose stabilizers do not contain \(j\), the off-axis positive projection is defined
\[
\pi_{\mathrm{off}}^+.
\]
Since the coefficients lie in \(\mathbb N_0\), this obstruction cannot be algebraically canceled. The RH condition in a finite window is equivalent to
\[
\pi_{\mathrm{off}}^+\tau_W(D_F)=0.
\]

Finally, this document establishes a monotonic off-axis obstruction profile using the height window
\[
S_T=\{z\in S:|\operatorname{Im}z|\le T\}
\]
defined as
\[
\beta_D(T)=D(S_T\setminus A).
\]
It is a non-negative integer-valued, right-continuous step profile; RH is equivalent to
\[
\beta_{D_F}(T)=0
\qquad
\forall T\ge0.
\]
This profile provides a common interface for finite verification, winding number certificates, local divisor sheaves, and subsequent arithmetic separation methods, but it does not allow the automatic lifting of finite-height zero obstructions to full-height conclusions.

**Keywords:** Riemann Hypothesis, equivariant topology, zero configurations, effective divisors, Burnside semiring, orbit-type, positive obstruction, vague topology, height filtration, fixed point

---

# 1. Research Purpose and Position

## 1.1 Problems Addressed in This Document

Previous research has reconstructed RH as an equivariant topological decision problem after centering:

\[
F(z)=\xi\left(\frac12+z\right),
\]

\[
F(z)=0
\Longrightarrow
z\in i\mathbb R.
\]

But simply writing
\[
Z(F)\subseteq i\mathbb R
\]
is still insufficient to form an extensible method group.

This document further asks:

1. In which topological space should the infinite set of zeros be placed?
2. How can symmetric zero quadruplets be represented as orbit-types?
3. How is zero multiplicity preserved?
4. How do off-axis zeros become irreducible positive obstructions?
5. As height increases, how are obstructions filtered and tracked?
6. How do local perturbations of analytic functions map to topological changes in zero configurations?
7. Which results are merely equivalent reformulations of RH, and which might serve as interfaces for subsequent proofs?

## 1.2 Position of This Document in the Overall Method Group

The overall research chain is:

\[
\text{Centering}
\to
\boxed{\text{Equivariant Topology of Zero Configurations}}
\to
\text{Sheafified Local-Global}
\to
\text{Topological Separation}
\to
\text{Analytic Admissible Lifting}
\to
\text{Arithmetic Sign Control}.
\]

This document only completes the boxed portion.

## 1.3 Distinction from the "Zero Locking" Language

This document does not use "zeros being locked by some force" as a mathematical premise.

This document only defines:

- which configurations are on-axis configurations;
- which configurations contain off-axis orbits;
- whether an on-axis configuration is a fixed point of a certain operator;
- whether off-axis orbits generate non-zero positive obstructions.

These definitions themselves do not contain the reasons why zeros must lie on the axis.

---

# 2. Equivariant Ambient Space After Centering

## 2.1 Completed Function and Centering

Define

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}
\Gamma\left(\frac s2\right)\zeta(s),
\]

and

\[
F(z)=\xi\left(\frac12+z\right).
\]

From the functional equation and real structure:

\[
F(-z)=F(z),
\qquad
F(\overline z)=\overline{F(z)}.
\]

## 2.2 Closed and Open Strips

Define the closed critical strip:

\[
S
=
\left\{
z\in\mathbb C:
\left|\operatorname{Re}z\right|
\le\frac12
\right\},
\]

and its interior:

\[
X
=
\left\{
z\in\mathbb C:
\left|\operatorname{Re}z\right|
<\frac12
\right\}.
\]

Nontrivial zeros lie in \(X\).

This document intentionally establishes the divisor topology on \(S\) rather than solely on \(X\), because the axial projection

\[
r(z)=i\,\operatorname{Im}z
\]

is a proper map on the closed strip \(S\). This ensures that the pushforward of a locally finite divisor remains locally finite.

If arbitrary locally finite divisors were considered only on the open strip \(X\), there could be infinitely many points accumulating towards the vertical boundaries within a finite height, resulting in infinite mass within a finite interval of the imaginary axis after projection. Therefore, the previous divisor pushforward must be supplemented with a properness condition.

## 2.3 Group Action

Define

\[
a(z)=-z,
\]

\[
b(z)=\overline z,
\]

\[
j(z)=a(b(z))=-\overline z.
\]

Then

\[
a^2=b^2=j^2=\operatorname{id},
\qquad
ab=ba=j.
\]

Therefore

\[
G=\{e,a,b,j\}
\cong C_2\times C_2.
\]

\(G\) acts continuously on \(S\) and \(X\).

## 2.4 The Critical Line as a Marked Fixed Set

We have:

\[
j(z)=z
\iff
z=-\overline z
\iff
\operatorname{Re}z=0.
\]

Thus

\[
A
=
\operatorname{Fix}(j)
=
i\mathbb R.
\]

Here, \(A\) is not an arbitrarily chosen line in a bare topological space, but the fixed-point set of the marked involution \(j\).

---

# 3. Point Orbits and Stabilizer Types

## 3.1 Stabilizers

For \(z\in S\), define

\[
G_z
=
\{g\in G:g\cdot z=z\}.
\]

By the orbit-stabilizer theorem:

\[
|Gz|
=
\frac{|G|}{|G_z|}.
\]

## 3.2 General Off-Axis Points

If

\[
\operatorname{Re}z\ne0,
\qquad
\operatorname{Im}z\ne0,
\]

then

\[
G_z=\{e\}.
\]

The orbit is

\[
Gz
=
\{
z,-z,\overline z,-\overline z
\},
\]

which has four elements.

This is a general off-axis four-element orbit.

## 3.3 Non-Zero Imaginary Axis Points

If

\[
z=iy,
\qquad
y\ne0,
\]

then

\[
j(z)=z,
\]

and

\[
a(z)=b(z)=-z.
\]

Therefore

\[
G_z=\langle j\rangle,
\]

the orbit is

\[
Gz=\{z,-z\}.
\]

This is the primary orbit-type permitted by RH.

## 3.4 Non-Zero Real Axis Points

If

\[
z=x\in\mathbb R,
\qquad
x\ne0,
\]

then

\[
b(z)=z,
\]

and

\[
a(z)=j(z)=-z.
\]

Therefore

\[
G_z=\langle b\rangle,
\]

the orbit is

\[
Gz=\{z,-z\}.
\]

This orbit does not lie on the critical line, so it still constitutes an off-axis obstruction within the general decision framework.

## 3.5 The Origin

For

\[
z=0,
\]

we have

\[
G_0=G.
\]

The origin is a full-group fixed point.

## 3.6 Realizable Orbit-Types

The realizable stabilizer types on \(S\) are:

\[
[e],
\qquad
[\langle b\rangle],
\qquad
[\langle j\rangle],
\qquad
[G].
\]

Since \(G\) is an abelian group, the conjugacy classes are equal to the subgroups themselves.

\(\langle a\rangle\) alone does not appear as a stabilizer, because

\[
a(z)=z
\Longrightarrow
z=0,
\]

and the origin is simultaneously fixed by the full group.

## 3.7 Orbit-Type Strata

Define:

\[
S_{(H)}
=
\{z\in S:G_z=H\}.
\]

Then

\[
S
=
S_{(e)}
\sqcup
S_{(\langle b\rangle)}
\sqcup
S_{(\langle j\rangle)}
\sqcup
S_{(G)}.
\]

where:

\[
S_{(\langle j\rangle)}
=
i\mathbb R\setminus\{0\},
\]

\[
S_{(\langle b\rangle)}
=
\left(
\mathbb R\cap S
\right)\setminus\{0\},
\]

\[
S_{(G)}=\{0\}.
\]

And \(S_{(e)}\) is the general region after removing the real and imaginary axes.

## 3.8 Orbit-Type Formulation of RH

Let \(D_F\) be the zero divisor.

RH is equivalent to:

\[
\operatorname{supp}D_F
\subseteq
S_{(\langle j\rangle)}
\cup
S_{(G)}.
\]

If we additionally use \(F(0)\ne0\), it can be further written as:

\[
\operatorname{supp}D_F
\subseteq
S_{(\langle j\rangle)}.
\]

---

# 4. Space of Locally Finite Effective Divisors

## 4.1 Effective Divisors

A locally finite effective divisor on \(S\) is a formal sum:

\[
D
=
\sum_{\rho\in S}
m_\rho[\rho],
\qquad
m_\rho\in\mathbb N_0,
\]

satisfying:

> For any compact set \(K\subset S\), there are only finitely many \(\rho\in K\) with \(m_\rho>0\).

Denote its space as:

\[
\operatorname{Div}_{\mathrm{lf}}^+(S).
\]

## 4.2 Radon Measure Representation

View \(D\) as a positive integer-valued Radon measure:

\[
\mu_D
=
\sum_\rho m_\rho\delta_\rho.
\]

Hereafter, no distinction is made between \(D\) and \(\mu_D\).

Addition makes

\[
\operatorname{Div}_{\mathrm{lf}}^+(S)
\]

a commutative monoid.

## 4.3 Subspace Supported on the Open Strip

Define:

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)
=
\left\{
D\in\operatorname{Div}_{\mathrm{lf}}^+(S):
\operatorname{supp}D\subset X
\right\}.
\]

\(D_F\) belongs to this space.

## 4.4 \(G\)-Invariant Divisors

Define:

\[
g_*D(B)=D(g^{-1}B).
\]

If

\[
g_*D=D
\qquad
\forall g\in G,
\]

then \(D\) is said to be \(G\)-invariant.

Denoted as:

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G.
\]

### Proposition 4.1

The zero divisor \(D_F\) of \(F\) belongs to

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G.
\]

### Proof Sketch

From

\[
F(-z)=F(z)
\]

and

\[
F(\overline z)=\overline{F(z)},
\]

if \(\rho\) is a zero, then

\[
-\rho,
\quad
\overline\rho,
\quad
-\overline\rho
\]

are also zeros of the same multiplicity. Therefore, the divisor is invariant under \(G\).

---

# 5. Vague Topology of the Configuration Space

## 5.1 Definition

Let

\[
C_c(S)
\]

denote the compactly supported continuous functions on \(S\).

A sequence of locally finite divisors \(D_n\) is said to converge vaguely to \(D\) if, for all

\[
\varphi\in C_c(S),
\]

we have

\[
\int_S\varphi\,dD_n
\longrightarrow
\int_S\varphi\,dD.
\]

Denoted as:

\[
D_n\xrightarrow{v}D.
\]

## 5.2 Intuition

The vague topology only observes zero configurations within arbitrary finite windows.

It allows:

- Zeros to move within a finite region;
- Zeros to escape to infinity;
- New zeros to enter from infinity;
- Multiple zeros to merge in the limit and accumulate multiplicity.

However, in any fixed compact window, local finiteness is preserved.

## 5.3 \(G\)-Invariant Subspace

Since \(G\) is a finite group and its action is continuous,

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G
\]

forms a natural closed subclass of the \(G\)-invariant configuration space.

## 5.4 Typical Limits of Orbit Merging

Suppose

\[
z_n=x_n+iy,
\qquad
x_n\to0,
\qquad
x_n\ne0.
\]

A general orbit divisor is:

\[
D_n
=
[z_n]+[-z_n]+[\overline z_n]+[-\overline z_n].
\]

As \(x_n\to0\):

\[
z_n,
\ -\overline z_n
\to iy,
\]

and

\[
-z_n,
\ \overline z_n
\to -iy.
\]

Thus the vague limit is:

\[
D_n
\xrightarrow{v}
2[iy]+2[-iy].
\]

This indicates that a four-point trivial stabilizer orbit can degenerate in the limit into two \(j\)-fixed orbit points with double multiplicity.

## 5.5 Separation of RH and Simplicity of Zeros

The above limit shows:

- Orbit-types can change;
- Multiplicities can increase;
- Off-axis orbits can degenerate to the critical line.

RH only requires the positions to lie on \(A\); it does not require the zeros to be simple.

Therefore, this document does not treat "multiple zero discriminants" as RH obstructions.

The target configuration space must allow:

\[
m_\rho>1
\qquad
\text{and }\rho\in A.
\]

Otherwise, it would illegitimately conflate RH with the simple zero conjecture.

---

# 6. Axial Retraction and Idempotent Divisor Operators

## 6.1 Retraction Map

Define:

\[
r:S\to A,
\qquad
r(z)=i\,\operatorname{Im}z.
\]

It satisfies:

\[
r|_A=\operatorname{id}_A,
\]

\[
r\circ r=r.
\]

## 6.2 Properness

### Proposition 6.1

\(r:S\to A\) is a proper map.

### Proof

Let \(K\subset A\) be a compact set. Then there exists a bounded closed interval \(I\subset\mathbb R\) such that

\[
K\subseteq\{iy:y\in I\}.
\]

We have:

\[
r^{-1}(K)
\subseteq
\left[-\frac12,\frac12\right]\times I.
\]

And \(r^{-1}(K)\) is a closed set. Therefore, it is a closed and bounded set in \(\mathbb R^2\), hence compact. This completes the proof.

## 6.3 Divisor Pushforward

Since \(r\) is proper, we can define:

\[
\mathcal R:
\operatorname{Div}_{\mathrm{lf}}^+(S)
\to
\operatorname{Div}_{\mathrm{lf}}^+(S),
\]

\[
\mathcal R(D)=r_*D.
\]

Its support lies in \(A\).

## 6.4 Continuity

### Proposition 6.2

\(\mathcal R\) is continuous with respect to the vague topology.

### Proof

If

\[
D_n\xrightarrow{v}D,
\]

for any \(\varphi\in C_c(A)\), since \(r\) is proper,

\[
\varphi\circ r\in C_c(S).
\]

Thus

\[
\int_A\varphi\,d(r_*D_n)
=
\int_S\varphi\circ r\,dD_n
\to
\int_S\varphi\circ r\,dD
=
\int_A\varphi\,d(r_*D).
\]

This completes the proof.

## 6.5 Idempotency

From

\[
r^2=r,
\]

we obtain:

\[
\mathcal R^2=\mathcal R.
\]

Thus \(\mathcal R\) is a continuous idempotent operator.

## 6.6 Fixed-Point Characterization

### Theorem 6.3

For any positive locally finite divisor \(D\),

\[
\mathcal R(D)=D
\iff
\operatorname{supp}D\subseteq A.
\]

### Proof

If \(\operatorname{supp}D\subseteq A\), then \(r\) is the identity on the support, hence \(\mathcal R(D)=D\).

Conversely, the support of \(\mathcal R(D)\) is contained in \(A\). If \(\mathcal R(D)=D\), then the support of \(D\) is also contained in \(A\). Positivity prevents any off-axis mass from being canceled by negative coefficients. This completes the proof.

### Corollary 6.4

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
\]

## 6.7 Positioning of the Operator

\(\mathcal R\) is a diagnostic projection:

- It defines the subspace of on-axis divisors;
- It establishes fixed-point equivalence;
- It does not provide the reason why \(D_F\) is a fixed point.

Therefore:

\[
\mathcal R(D_F)=D_F
\]

cannot be treated as a proven theorem, but only as an equivalent criterion to be achieved.

---

# 7. Finite Windows and Orbit-Type Values

## 7.1 \(G\)-Invariant Finite Windows

Let

\[
W\subset S
\]

be a compact and \(G\)-invariant Borel set.

Since \(D\) is locally finite,

\[
D(W)<\infty.
\]

Therefore, only finitely many zero orbits appear in \(W\).

## 7.2 Orbit Multiplicity

If \(D\) is \(G\)-invariant, then each point on the same orbit has the same multiplicity.

For an orbit \(\mathcal O=G\rho\), denote the common multiplicity as:

\[
m_{\mathcal O}.
\]

## 7.3 Positive Burnside Semiring

Let

\[
A^+(G)
\]

denote the positive Burnside semiring formed by the isomorphism classes of finite \(G\)-sets.

Its addition is given by disjoint union, and multiplication by Cartesian product.

The additive basis is given by transitive \(G\)-sets:

\[
[G/H]
\]

where \(H\le G\).

Thus each element can be written as:

\[
\sum_{[H]}n_H[G/H],
\qquad
n_H\in\mathbb N_0.
\]

## 7.4 Window Orbit-Type Value

Define:

\[
\tau_W(D)
=
\sum_{\mathcal O\subseteq\operatorname{supp}D\cap W}
m_{\mathcal O}[G/G_\rho]
\in A^+(G),
\]

where \(\rho\in\mathcal O\).

Since \(G\) is abelian, the choice of orbit representative does not affect the stabilizer type.

## 7.5 Expanded Form

Under the action in this document, it can be written as:

\[
\tau_W(D)
=
n_e(W)[G/e]
+
n_b(W)[G/\langle b\rangle]
+
n_j(W)[G/\langle j\rangle]
+
n_G(W)[G/G].
\]

All coefficients lie in \(\mathbb N_0\).

where:

- \(n_e\): multiplicity of general four-point off-axis orbits;
- \(n_b\): multiplicity of real-axis off-axis orbits;
- \(n_j\): multiplicity of imaginary-axis orbits;
- \(n_G\): multiplicity of the origin.

---

# 8. Off-Axis Positive Obstructions

## 8.1 On-Axis and Off-Axis Generators

An orbit lies on \(A=\operatorname{Fix}(j)\) if and only if its stabilizer contains \(j\).

Among the currently realizable types:

- \(\langle j\rangle\) contains \(j\);
- \(G\) contains \(j\);
- \(e\) does not contain \(j\);
- \(\langle b\rangle\) does not contain \(j\).

## 8.2 Positive Projection

Define the additive monoid homomorphism:

\[
\pi_{\mathrm{off}}^+:
A^+(G)
\to
\mathbb N_0^2,
\]

such that:

\[
\pi_{\mathrm{off}}^+([G/e])=(1,0),
\]

\[
\pi_{\mathrm{off}}^+([G/\langle b\rangle])=(0,1),
\]

\[
\pi_{\mathrm{off}}^+([G/\langle j\rangle])=(0,0),
\]

\[
\pi_{\mathrm{off}}^+([G/G])=(0,0).
\]

Therefore:

\[
\pi_{\mathrm{off}}^+\tau_W(D)
=
(n_e(W),n_b(W)).
\]

## 8.3 Non-Cancellation Property

### Theorem 8.1

\[
\pi_{\mathrm{off}}^+\tau_W(D)=0
\]

if and only if \(D\) has no off-axis orbits in \(W\).

### Proof

Since the coefficients are all non-negative integers,

\[
(n_e,n_b)=(0,0)
\]

if and only if the coefficients of both types of off-axis orbits are zero. There are no negative coefficients to cancel them out. This completes the proof.

## 8.4 Why Not Enter the Burnside Ring Directly

The Burnside ring \(A(G)\) is the Grothendieck groupification of \(A^+(G)\), allowing formal differences:

\[
[X]-[Y].
\]

Groupification is suitable for studying stable algebraic relations, but it may produce:

\[
\text{Non-zero positive obstruction}
+
\text{Negative formal term}
=
0.
\]

Such algebraic cancellation does not mean the actual off-axis zeros have vanished.

Therefore, this document adopts the approach:

> **First complete the existence decision in the positive semiring, then groupify as needed.**

## 8.5 Window RH Condition

For \(D_F\):

\[
\pi_{\mathrm{off}}^+\tau_W(D_F)=0
\]

is equivalent to having no off-axis zeros in \(W\).

This is a finite window decision, not the global RH.

---

# 9. Direct Off-Axis Mass Obstruction

## 9.1 Off-Axis Restriction

Define:

\[
D^{\mathrm{off}}
=
D|_{S\setminus A}.
\]

It remains a positive locally finite divisor.

## 9.2 Global Positive Obstruction

Define:

\[
\mathfrak O(D)=D^{\mathrm{off}}.
\]

Then:

\[
\mathfrak O(D)=0
\iff
\operatorname{supp}D\subseteq A.
\]

Therefore:

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak O(D_F)=0.
}
\]

## 9.3 Distinction from Divisor Difference Obstructions

Previously, one could define the formal difference:

\[
\Theta(D)=D-\mathcal R(D).
\]

But \(\Theta(D)\) lies in the group of divisors with integer coefficients, possessing both positive and negative terms.

This document considers the more fundamental obstruction to be:

\[
\mathfrak O(D)=D|_{S\setminus A},
\]

because it preserves positivity, and:

\[
\mathfrak O(D)=0
\]

directly indicates that the off-axis support is empty.

\(\Theta\) can serve as a comparative difference, but it should not replace the positive obstruction.

---

# 10. Height Filtration

## 10.1 Compact Height Windows

For \(T\ge0\), define:

\[
S_T
=
\left\{
z\in S:
|\operatorname{Im}z|\le T
\right\}.
\]

Since \(S\) is bounded horizontally, \(S_T\) is a compact set.

## 10.2 Truncated Divisors

Define:

\[
D_{\le T}=D|_{S_T}.
\]

Its total mass is finite.

## 10.3 Off-Axis Mass Profile

Define:

\[
\beta_D(T)
=
D(S_T\setminus A).
\]

Then:

\[
\beta_D(T)\in\mathbb N_0.
\]

## 10.4 Monotonicity

If

\[
T_1\le T_2,
\]

then

\[
S_{T_1}\subseteq S_{T_2},
\]

thus:

\[
\beta_D(T_1)
\le
\beta_D(T_2).
\]

## 10.5 Step Structure

Since \(D\) has only finite support in each \(S_T\), \(\beta_D\) will only jump when the height

\[
T=|\operatorname{Im}\rho|
\]

crosses an off-axis zero.

Therefore, it is a non-negative integer-valued monotonic step profile.

In intervals containing no boundary zeros, it is locally constant.

## 10.6 Filtered Formulation of RH

### Theorem 10.1

\[
\boxed{
\mathrm{RH}
\iff
\beta_{D_F}(T)=0
\quad
\forall T\ge0.
}
\]

### Proof

If RH holds, the off-axis restriction is zero, hence the mass at all heights is zero.

Conversely, if there exists an off-axis zero \(\rho\), taking

\[
T\ge|\operatorname{Im}\rho|,
\]

yields

\[
\beta_{D_F}(T)\ge m_\rho>0.
\]

This completes the proof.

## 10.7 The True Status of Finite Verification

If numerical or formal methods prove:

\[
\beta_{D_F}(T_0)=0,
\]

it only means:

\[
|\operatorname{Im}\rho|\le T_0
\]

there are no off-axis zeros within.

It does not imply:

\[
\beta_{D_F}(T)=0
\qquad
\forall T>T_0.
\]

To complete the global RH, an independent tail theorem is still required.

---

# 11. Orbit-Type Height Profile

## 11.1 Burnside Value Filtration

Define:

\[
\tau_T(D)
=
\tau_{S_T}(D)
\in A^+(G).
\]

Expanded:

\[
\tau_T(D)
=
n_e(T)[G/e]
+
n_b(T)[G/\langle b\rangle]
+
n_j(T)[G/\langle j\rangle]
+
n_G(T)[G/G].
\]

## 11.2 Off-Axis Orbit Profile

Define:

\[
\gamma_D(T)
=
\pi_{\mathrm{off}}^+\tau_T(D)
=
(n_e(T),n_b(T)).
\]

This profile is finer than \(\beta_D(T)\) because it distinguishes between:

- General four-point off-axis orbits;
- Real-axis two-point off-axis orbits.

## 11.3 Point Mass and Orbit Mass

If calculation by point multiplicity is needed, one can define:

\[
\beta_D(T)
=
4n_e(T)+2n_b(T),
\]

provided that \(n_e,n_b\) are already weighted by the common point multiplicity of each orbit.

Orbit counting and point counting each have their uses:

- Orbit counting describes the symmetric structure;
- Point counting interfaces with the argument principle and the total number of zeros.

---

# 12. Configuration Decomposition and Orbit-Type Closure

## 12.1 On-Axis Subspace

Define:

\[
\mathscr D_{\mathrm{axis}}
=
\left\{
D\in\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G:
\operatorname{supp}D\subseteq A
\right\}.
\]

By the fixed-point theorem:

\[
\mathscr D_{\mathrm{axis}}
=
\operatorname{Fix}(\mathcal R).
\]

## 12.2 Mixed Subspace

Define:

\[
\mathscr D_{\mathrm{mixed}}
=
\left\{
D:
D|_A\ne0,
\ D|_{S\setminus A}\ne0
\right\}.
\]

## 12.3 Pure Off-Axis Subspace

Define:

\[
\mathscr D_{\mathrm{off}}
=
\left\{
D:
D|_A=0,
\ D\ne0
\right\}.
\]

## 12.4 Decomposition

Excluding the zero divisor, we can write:

\[
\mathscr D^G
=
\mathscr D_{\mathrm{axis}}
\sqcup
\mathscr D_{\mathrm{mixed}}
\sqcup
\mathscr D_{\mathrm{off}}.
\]

## 12.5 Closure of the On-Axis Subspace

### Proposition 12.1

Under the vague topology,

\[
\mathscr D_{\mathrm{axis}}
\]

is a closed set.

### Proof Sketch

Since \(A\) is a closed set, if \(D_n\) are all supported on \(A\) and \(D_n\xrightarrow v D\), then for any non-negative test function \(\varphi\) supported on \(S\setminus A\), we have:

\[
\int\varphi\,dD_n=0.
\]

The limit gives:

\[
\int\varphi\,dD=0.
\]

Thus \(D\) has no mass on \(S\setminus A\).

## 12.6 The On-Axis Subspace is Not an Open Set

General off-axis four-element orbits can degenerate towards the imaginary axis, so off-axis configurations may exist near any on-axis multiple configuration.

This indicates:

- The RH configuration space is a closed condition;
- But it does not necessarily possess open stability against arbitrary function perturbations;
- Stability under small perturbations alone cannot prove RH.

---

# 13. From Analytic Function Space to Zero Configuration Space

## 13.1 Class of Symmetric Entire Functions

Define:

\[
\mathcal E_G
=
\left\{
f\in\operatorname{Hol}(\mathbb C):
f(-z)=f(z),
f(\overline z)=\overline{f(z)}
\right\}.
\]

Endowed with the compact-open topology, i.e., uniform convergence on every compact set.

## 13.2 Zero Divisor Map

For non-zero \(f\in\mathcal E_G\), define:

\[
\mathfrak Z(f)
=
D_f|_X.
\]

Abstractly:

\[
\mathfrak Z:
\mathcal E_G\setminus\{0\}
\to
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G.
\]

## 13.3 Local Stability

Let \(U\Subset X\) be a relatively compact region, and

\[
f(z)\ne0
\qquad
z\in\partial U.
\]

If \(f_n\to f\) uniformly on \(\overline U\), then by Rouché's theorem, for sufficiently large \(n\):

\[
D_{f_n}(U)=D_f(U)
\]

counting multiplicities.

This means that within a zero-free boundary, the total number of zeros is locally stable.

## 13.4 Finer Configuration Convergence

Under appropriate conditions, Hurwitz's theorem and local factorization can transform:

\[
f_n\to f
\]

into the vague convergence of zero divisors in relatively compact windows.

Therefore, a locally stable interface exists between the analytic function space and the zero configuration space.

## 13.5 Limitations

The zero divisor map is not unconditionally globally continuous in all cases:

- Zeros can cross window boundaries;
- Zeros can escape to infinity;
- The limit function may be identically zero;
- Multiple zeros can cause local orbit-type changes.

Therefore, any subsequent study of dynamics or parameter families must be accompanied by regular windows and boundary control.

---

# 14. Interface with Winding Number Obstructions

## 14.1 Regular Regions

Let \(U\Subset X\setminus A\) be a bounded region, and:

\[
F(z)\ne0
\qquad
z\in\partial U.
\]

Define:

\[
\omega_U(F)
=
\frac{1}{2\pi i}
\oint_{\partial U}
\frac{F'(z)}{F(z)}\,dz.
\]

## 14.2 Zero Counting

By the argument principle:

\[
\omega_U(F)
=
D_F(U).
\]

Therefore, the winding number is the total mass of the positive divisor on the region \(U\).

## 14.3 Relationship with Configuration Obstructions

If \(U\subset S\setminus A\), then:

\[
\omega_U(F)>0
\]

indicates:

\[
\mathfrak O(D_F)(U)>0.
\]

Thus:

\[
\text{Winding number certificate}
\]

is the boundary representation of the off-axis positive obstruction.

## 14.4 Division of Labor

- Divisor configurations preserve positions, multiplicities, and orbit-types;
- Burnside values preserve symmetric orbit types;
- Winding numbers preserve the total positive mass within a region;
- Height filtration preserves the emergence of obstructions across scales.

They are not competing representations, but different projections of the same obstruction.

---

# 15. Precise Porting of the M6 Fixed-Point Method

## 15.1 Ambient Domain

M6 first establishes:

\[
M6^*
\]

as the candidate ambient domain.

This document establishes:

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G
\]

as the zero configuration ambient domain.

## 15.2 Target Subset

In M6, primes are merely a proper subset of the ambient domain.

In this document, on-axis configurations:

\[
\mathscr D_{\mathrm{axis}}
\]

are merely a proper subset of the entire configuration ambient domain.

## 15.3 Non-Circular Operator

The definition of \(\mathcal R\) only uses:

- The closed critical strip \(S\);
- The involution \(j\);
- The fixed set \(A\);
- The axial retraction \(r\).

It does not use the assumption "that \(D\) already satisfies RH".

## 15.4 Distinction Between Positioning and Proof

\[
\operatorname{Fix}(\mathcal R)
=
\mathscr D_{\mathrm{axis}}
\]

accomplishes unique positioning.

But to prove:

\[
D_F\in\operatorname{Fix}(\mathcal R),
\]

still requires additional mathematical content.

Therefore, this document continues to adopt:

> **One-limb positioning, without masquerading as a proof.**

---

# 16. Version of the TOPO Fiber Check in Configuration Space

## 16.1 Coarsening Map

Let:

\[
Q:
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G
\to
\mathcal T
\]

forget partial data.

For example, \(Q\) might only retain:

- Total number of zeros;
- Number of orbits;
- Height distribution;
- Some topological isomorphism class;
- Some average density.

## 16.2 On-Axis Decision

Define:

\[
P(D)
=
\begin{cases}
1,&D\in\mathscr D_{\mathrm{axis}},\\
0,&\text{otherwise}.
\end{cases}
\]

If there exist:

\[
D_1,D_2
\]

such that:

\[
Q(D_1)=Q(D_2),
\]

but:

\[
P(D_1)\ne P(D_2),
\]

then \(Q\) is insufficient to decide RH.

## 16.3 Informational Advantage of Positive Obstructions

\[
\mathfrak O(D)=D|_{S\setminus A}
\]

is complete for the on-axis decision, because:

\[
P(D)=1
\iff
\mathfrak O(D)=0.
\]

But it retains almost the entire off-axis divisor, so it is not a highly compressed decision quantity.

The research question becomes:

> Does there exist an invariant that is more compressed than the full off-axis divisor, yet remains constant on the fibers of \(P\)?

Burnside orbit-types, height profiles, and winding number families are three candidate compressions.

---

# 17. Overly Strong Conclusions Not Used in This Document

## 17.1 No Claim That Orbit-Type Stratification Proves RH

Orbit-types only classify possibilities.

## 17.2 No Claim That Closure Implies Inevitability

That \(\mathscr D_{\mathrm{axis}}\) is a closed set does not mean \(D_F\) must fall into it.

## 17.3 No Claim That Retraction Equals Actual Zero Movement

\(r\) is a diagnostic map, not a physical or analytic evolution of the zeros of \(\xi\).

## 17.4 No Claim That Four-Point Orbit Degeneration Inevitably Occurs

That the configuration space allows such limits does not mean the zeros of \(F\) actually move this way along some parameter family.

## 17.5 Multiple Zeros Are Not Treated as RH Failure

RH and the simplicity of zeros are distinct propositions.

## 17.6 Finite-Height Zero Obstructions Are Not Lifted Globally

Lacking tail control, one can only obtain finite window results.

---

# 18. Available Interfaces for Subsequent Research

## 18.1 Sheafification Interface

For an open set \(U\subset S\), define:

\[
\mathscr Z_{\mathrm{off}}(U)
=
\operatorname{Div}_{\mathrm{lf}}^+(U\setminus A).
\]

Subsequent research can study its restriction maps and zero-section gluing.

## 18.2 Orbit Space Interface

Define:

\[
Y=S/G.
\]

\(G\)-invariant divisors can descend to positive discrete measures on \(Y\) marked with orbit-types.

Subsequently, off-axis orbits can be localized in:

\[
Y_{\mathrm{off}}
\]

## 18.3 Test Function Interface

For:

\[
\varphi\in C_c(S\setminus A),
\qquad
\varphi\ge0,
\]

define:

\[
\langle\mathfrak O(D),\varphi\rangle
=
\int\varphi\,dD.
\]

If \(\mathfrak O(D)\ne0\), then there exists a non-negative compactly supported continuous function \(\varphi\) such that:

\[
\int\varphi\,dD>0.
\]

This is the most basic form of subsequent "topological separation".

The real difficulty lies in lifting \(\varphi\) to an analytic test function permitted by explicit formulas.

## 18.4 Arithmetic Interface

Ultimately, a map is needed:

\[
\mathfrak A:
\mathcal H_{\mathrm{adm}}
\to
\mathbb R,
\]

possessing simultaneously:

- A zero-side representation;
- A prime-side representation;
- The capability to detect off-axis positive obstructions;
- A sign controllable from the arithmetic side.

This document does not establish this map; it only provides the configuration input for it.

---

# 19. Formalization Specifications

## 19.1 Basic Types

It is recommended to establish in Lean:

```text
ClosedCriticalStrip
OpenCriticalStrip
KleinFourAction
CriticalInvolution
LocallyFiniteEffectiveDivisor
InvariantDivisor
OrbitType
PositiveOrbitSemiring
OffAxisObstruction
HeightRestriction
```

## 19.2 Core Theorems

Need to formalize:

1. \(j^2=\mathrm{id}\);
2. \(\operatorname{Fix}(j)=A\);
3. \(G\)-invariance of \(D_F\);
4. Properness of \(r\);
5. Well-definedness of \(\mathcal R\);
6. \(\mathcal R^2=\mathcal R\);
7. Equivalence between fixed points and on-axis support;
8. Orbit-type classification;
9. Equivalence between zero positive obstruction and the non-existence of off-axis orbits;
10. Monotonicity of height obstructions;
11. Equivalence between full-height zero obstruction and RH.

## 19.3 Content That Should Not Be Formalized as Axioms

The following content must not be mixed into the main library directly as unproven axioms:

\[
\mathfrak O(D_F)=0,
\]

\[
\mathcal R(D_F)=D_F,
\]

\[
\beta_{D_F}(T)=0
\quad
\forall T.
\]

They are precisely equivalent forms of RH.

If temporarily assumed for testing purposes, they must be isolated in clearly marked assumption files.

---

# 20. Research Evaluation

## 20.1 What This Document Truly Adds

Compared to the prerequisite decision domain paper, this document adds:

1. Correcting the properness issue of the axial pushforward using the closed critical strip;
2. Constructing the zero divisor space as a vague topological configuration space;
3. Completely classifying the realizable stabilizer types under the Klein four-group;
4. Formulating RH as a specific orbit-type support condition;
5. Introducing the positive Burnside semiring to avoid obstruction cancellation;
6. Establishing the off-axis positive projection;
7. Establishing the monotonically increasing height obstruction profile;
8. Separating RH from the simplicity of zeros;
9. Establishing a locally stable interface from the analytic function space to the zero configuration space.

## 20.2 What Has Not Been Added

This document does not provide:

- The analytic reason why the off-axis positive obstruction is zero;
- The prime-side sign theorem;
- New zero-free regions;
- Full-height estimates;
- A proof of RH.

## 20.3 Research Value

The value of this document lies in transforming "where the zeros are" into an ambient structure possessing the following characteristics:

- Has topology;
- Has group action;
- Has multiplicity;
- Has positivity;
- Has orbit-types;
- Has finite windows;
- Has height filtration;
- Has analytic perturbation interfaces;
- Has formalization specifications.

Subsequent research no longer needs to rely on the vague "zero locking" as a common language.

---

# 21. Conclusion

This document has established the equivariant topology of zero configurations for the Riemann Hypothesis after centering.

The basic data are:

\[
S
=
\left\{
\left|\operatorname{Re}z\right|\le\frac12
\right\},
\]

\[
G
=
\langle z\mapsto-z,
\ z\mapsto\overline z\rangle
\cong C_2\times C_2,
\]

\[
j(z)=-\overline z,
\]

\[
A=\operatorname{Fix}(j)=i\mathbb R,
\]

\[
D_F=\operatorname{div}_0(F).
\]

The fixed-point formulation of RH is:

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
\]

The positive obstruction formulation of RH is:

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak O(D_F)=0.
}
\]

The height filtration formulation of RH is:

\[
\boxed{
\mathrm{RH}
\iff
\beta_{D_F}(T)=0
\quad
\forall T\ge0.
}
\]

The orbit-type formulation of RH is:

\[
\boxed{
\mathrm{RH}
\iff
\pi_{\mathrm{off}}^+\tau_{S_T}(D_F)=0
\quad
\forall T\ge0.
}
\]

These formulations collectively accomplish:

- The equivariant configuration of the zero set;
- The stratification of on-axis and off-axis orbits;
- The preservation of multiplicity;
- The non-cancellability of positive obstructions;
- The height filtration of infinite propositions.

However, they remain merely a legitimate decision framework.

The true core yet to be completed remains:

\[
\boxed{
\text{Independent analytic / arithmetic structure of \(\xi\)}
\Longrightarrow
\mathfrak O(D_F)=0.
}
\]

The next stage should study:

# *Sheafified Zero Obstructions and Local-Global Lifting*

Its task is to organize the finite window positive obstructions, boundary winding numbers, and local divisor data of this document into sheaf and cosheaf structures, and precisely analyze:

\[
\text{Local zero obstruction}
\;\dashrightarrow\;
\text{Global zero obstruction}
\]

the missing gluing conditions, infinity control, and tail theorems.

---

# Appendix A: Main Notation

| Symbol | Meaning |
|---|---|
| \(S\) | Closed critical strip after centering |
| \(X\) | Interior of the closed critical strip |
| \(G\) | Klein four-group |
| \(a\) | Central inversion \(z\mapsto-z\) |
| \(b\) | Conjugation \(z\mapsto\overline z\) |
| \(j\) | Critical reflection \(z\mapsto-\overline z\) |
| \(A\) | Fixed-point set of \(j\), i.e., the imaginary axis |
| \(D_F\) | Nontrivial zero divisor of \(F\) |
| \(\mathcal R\) | Divisor pushforward of the axial retraction |
| \(A^+(G)\) | Positive Burnside semiring |
| \(\tau_W(D)\) | Orbit-type value within a window |
| \(\pi_{\mathrm{off}}^+\) | Off-axis orbit positive projection |
| \(\mathfrak O(D)\) | Off-axis positive divisor |
| \(S_T\) | Compact window of height \(T\) |
| \(\beta_D(T)\) | Off-axis point multiplicity profile |
| \(\gamma_D(T)\) | Off-axis orbit-type profile |
| \(\mathfrak Z\) | Map from analytic functions to zero divisors |

---

# Appendix B: Logical Strength Table

| Proposition | Nature |
|---|---|
| \(D_F\) is \(G\)-invariant | Direct consequence of known symmetries |
| \(\operatorname{Fix}(j)=i\mathbb R\) | Direct calculation |
| \(\mathcal R^2=\mathcal R\) | Consequence of definition |
| \(\mathcal R(D)=D\iff\operatorname{supp}D\subseteq A\) | General divisor theorem |
| \(\mathfrak O(D)=0\iff\operatorname{supp}D\subseteq A\) | General positive obstruction theorem |
| \(\beta_D(T)\) is monotonic | Direct consequence of set inclusion |
| RH \(\iff\mathfrak O(D_F)=0\) | Equivalent reformulation |
| RH \(\iff\beta_{D_F}\equiv0\) | Equivalent reformulation |
| \(\mathfrak O(D_F)=0\) | Not yet proven; equivalent to RH |
| All off-axis orbits do not exist | Not yet proven; equivalent to RH |

---

# Appendix C: Subsequent Interfaces

This document outputs to the next paper:

\[
\left(
S,
A,
G,
\mathscr D^G,
\mathfrak O,
\tau_T,
\beta_T,
\omega_U
\right).
\]

The next paper needs to add:

- Category of open sets;
- Divisor sheaf;
- Off-axis obstruction sheaf;
- Boundary winding number data;
- Local certificate gluing;
- Infinity control;
- Tail lifting conditions.

---

# Appendix D: Version Boundaries

v0.1 has completed:

- Closed critical strip and proper axial projection;
- Vague topology;
- Orbit-type classification;
- Effective divisor configurations;
- Positive Burnside semiring;
- Off-axis positive obstructions;
- Height profiles;
- Equivalence chain between RH and obstruction vanishing;
- Formalization specifications.

v0.1 has not yet completed:

- Lean 4 implementation;
- Complete metrization of the configuration space;
- Whitney conditions for orbit-type decomposition;
- Sheaf and cosheaf formalization;
- Explicit formula test functions;
- Arithmetic sign theorems;
- Any proof of RH.