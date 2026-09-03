# Parity Words, Residue Cylinders, and Local Identity Trivialization
## —Exact Admissible Domains, Binary Splitting, and Local Trivialization of the Collatz Local Affine Atlas

**English Title:** *Parity Words, Residue Cylinders, and Local Identity Trivialization in the Collatz Local Affine Atlas*

**Author:** Neo.K  
**Institution:** EveMiss Technology Co., Ltd. (EveMissLab)  
**Series:** Collatz Operation Translation Series — Paper 03  
**Version:** v0.1.1  
**Date:** 2026-08-10  
**Revision Date:** 2026-08-14

---

## Abstract

Paper 02 has proven that for the modified Collatz map

$$
T(n)=
\begin{cases}
\dfrac n2,&n\equiv0\pmod2,\\[2mm]
\dfrac{3n+1}{2},&n\equiv1\pmod2,
\end{cases}
$$

any finite parity word

$$
w\in\{D,U\}^k
$$

corresponds to a formal affine operator

$$
F_w(x)
=
\frac{3^{u(w)}x+b_w}{2^k}.
$$

However, Paper 02 has not yet answered the most important question regarding the admissible domain:

> Which positive integers actually have $w$ as their first $k$-step Collatz itinerary?

This paper proves that for every parity word $w$ of length $k$, there exists a unique residue

$$
r_w\in\mathbb Z/2^k\mathbb Z
$$

such that its admissible domain is exactly

$$
\boxed{
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}.
}
$$

Therefore, parity words of length $k$ and modulo $2^k$ residue classes form a one-to-one correspondence:

$$
\boxed{
\{D,U\}^k
\longleftrightarrow
\mathbb Z/2^k\mathbb Z.
}
$$

This paper also provides its closed congruence:

$$
\boxed{
r_w
\equiv
-b_w\,3^{-u(w)}
\pmod{2^k},
}
$$

where $3^{-u(w)}$ denotes the multiplicative inverse of $3^{u(w)}$ modulo $2^k$.

More importantly, let

$$
m_w=T^k(r_w)
=
\frac{3^{u(w)}r_w+b_w}{2^k},
$$

then for any integer quotient coordinate $a$, as long as

$$
n=r_w+2^k a>0,
$$

we have the exact cylinder transport:

$$
\boxed{
T^k(r_w+2^ka)
=
m_w+3^{u(w)}a.
}
$$

Thus, the source cylinder

$$
r_w+2^k\mathbb Z
$$

is mapped exactly by $T^k$ to the target arithmetic progression

$$
m_w+3^{u(w)}\mathbb Z.
$$

Defining the source chart

$$
\phi_w(n)
=
\frac{n-r_w}{2^k},
$$

and the target chart

$$
\psi_w(y)
=
\frac{y-m_w}{3^{u(w)}},
$$

then on the admissible domain:

$$
\boxed{
\psi_w\circ T^k\circ\phi_w^{-1}
=
\operatorname{id}.
}
$$

That is to say: **the Collatz dynamics for a fixed finite parity word is not merely affinized, but can be exactly trivialized into the identity map in appropriate source/target coordinates.**

This paper refers to this set of data

$$
\mathcal A_w
=
(\Omega_w,\Gamma_w,\phi_w,\psi_w,F_w)
$$

as a **Collatz Local Affine Chart**. All charts of length $k$ collectively form the level-$k$ atlas:

$$
\boxed{
\mathfrak A_k
=
\{\mathcal A_w:w\in\{D,U\}^k\}.
}
$$

Its source domains form an exact, non-overlapping partition of the positive integers. Furthermore, when transitioning from length $k$ to $k+1$, each cylinder uniquely splits into two sub-cylinders according to a parity bit of the quotient coordinate; therefore, atlas refinement is equivalent to binary residue refinement.

This paper ultimately reaches a core conclusion:

$$
\boxed{
\text{finite Collatz dynamics is locally identity-trivializable}.
}
$$

However, this paper also emphasizes:

$$
\boxed{
\text{local identity trivialization}
\not\Rightarrow
\text{global Collatz convergence}.
}
$$

Because the truly unresolved problem has shifted to: how the next chart is selected after a trajectory leaves a finite chart, and whether the infinite chart itinerary inevitably enters a descending / certified region for every starting point.

**Keywords:** Collatz conjecture, parity word, residue cylinder, 2-adic coding, local affine atlas, identity conjugacy, operation translation, exact recovery, 3n+1

---

# 1. The Admissible Domain Gap Left by Paper 02

For any formal word

$$
w=\sigma_1\cdots\sigma_k,
\qquad
\sigma_j\in\{D,U\},
$$

Paper 02 defined:

$$
D(x)=\frac{x}{2},
$$

$$
U(x)=\frac{3x+1}{2},
$$

and proved:

$$
\boxed{
F_w(x)
=
\frac{3^{u(w)}x+b_w}{2^k}.
}
$$

But:

$$
F_w(n)
$$

is merely a formal composition.

For

$$
T^k(n)=F_w(n),
$$

the first $k$ parity decisions of $n$ must truly equal $w$.

Therefore, we must find:

$$
\boxed{
\Omega_w
=
\{n>0:w\text{ is the first }k\text{-step parity word of }n\}.
}
$$

---

# 2. Preview of the Main Theorem

This paper will prove:

$$
\boxed{
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}
}
$$

and $r_w$ is unique.

Therefore, the "admissible domain of a finite word" is not an arbitrary sparse set, but a complete residue cylinder.

---

# 3. Base Case: Length 1

There are two words:

$$
D,\qquad U.
$$

where:

$$
\Omega_D
=
2\mathbb Z_{>0}
=
(0+2\mathbb Z)\cap\mathbb Z_{>0},
$$

and:

$$
\Omega_U
=
(1+2\mathbb Z)\cap\mathbb Z_{>0}.
$$

Thus:

$$
r_D=0\pmod2,
$$

$$
r_U=1\pmod2.
$$

The word ↔ residue correspondence holds for length 1.

---

# 4. Inductive Cylinder Hypothesis

Assume that for a word $w$ of length $k$,

there already exists a unique residue class:

$$
r_w\pmod{2^k},
$$

and we take its canonical representative:

$$
0\le r_w<2^k.
$$

such that:

$$
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}.
$$

Let:

$$
u=u(w),
$$

and define:

$$
m_w
=
F_w(r_w)
=
\frac{3^ur_w+b_w}{2^k}.
$$

By the cylinder hypothesis, whether $r_w$ is $0$ or not, we have:

$$
r_w+2^k\in\Omega_w.
$$

Therefore, $F_w$ equals the true $T^k$ on this positive integer admissible input, hence:

$$
F_w(r_w+2^k)
=
m_w+3^u
\in\mathbb Z.
$$

Since $3^u\in\mathbb Z$, we obtain:

$$
m_w\in\mathbb Z.
$$

---

# 5. Cylinder Quotient Coordinate

Any:

$$
n\in\Omega_w
$$

can be uniquely written as:

$$
\boxed{
n=r_w+2^ka,
\qquad
a\in\mathbb Z,
}
$$

satisfying $n>0$.

The affine formula from Paper 02 gives:

$$
T^k(n)
=
\frac{3^u(r_w+2^ka)+b_w}{2^k}.
$$

Therefore:

$$
\boxed{
T^k(n)
=
m_w+3^ua.
}
$$

Since:

$$
3^u
$$

is odd,

we have:

$$
T^k(n)\pmod2
=
m_w+a\pmod2.
$$

This simple equation is the core of atlas refinement.

---

# 6. Append-$D$ Sub-Cylinder

The word:

$$
wD
$$

is admissible under the condition:

$$
T^k(n)\equiv0\pmod2.
$$

Thus:

$$
m_w+a\equiv0\pmod2.
$$

Equivalent to:

$$
\boxed{
a\equiv m_w\pmod2.
}
$$

Let:

$$
a=m_w+2q
$$

in the modulo 2 sense.

Substituting back into:

$$
n
=
r_w+2^k a.
$$

Thus, modulo $2^{k+1}$:

$$
\boxed{
r_{wD}
\equiv
r_w+2^k(m_w\bmod2)
\pmod{2^{k+1}}.
}
$$

Therefore, $wD$ corresponds to a unique modulo $2^{k+1}$ residue.

---

# 7. Append-$U$ Sub-Cylinder

Similarly,

$$
wU
$$

admissibility requires:

$$
T^k(n)\equiv1\pmod2.
$$

Thus:

$$
m_w+a\equiv1\pmod2.
$$

That is:

$$
\boxed{
a\equiv1-m_w\pmod2.
}
$$

Therefore:

$$
\boxed{
r_{wU}
\equiv
r_w
+
2^k(1-m_w\bmod2)
\pmod{2^{k+1}}.
}
$$

More intuitively:

$$
\{r_{wD},r_{wU}\}
=
\{r_w,r_w+2^k\}
\pmod{2^{k+1}}.
$$

These two are exactly the two binary refinements of the parent cylinder.

---

# 8. Word–Residue Bijection Theorem

## Theorem 8.1

For each:

$$
w\in\{D,U\}^k,
$$

there exists a unique:

$$
r_w\in\mathbb Z/2^k\mathbb Z
$$

such that:

$$
\boxed{
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}.
}
$$

Furthermore:

$$
w\neq v
\Longrightarrow
r_w\not\equiv r_v\pmod{2^k}.
$$

Therefore:

$$
\boxed{
\{D,U\}^k
\cong
\mathbb Z/2^k\mathbb Z
}
$$

as finite sets.

### Proof

The base case is already established.

If every cylinder of length $k$ is unique,

then the previous section proves that each cylinder splits exactly into two mutually exclusive and exhaustive modulo $2^{k+1}$ sub-cylinders, $wD$ and $wU$.

Therefore, by induction, it holds for all $k$.

This completes the proof.

---

# 9. Partition Theorem

Since modulo $2^k$ residue classes exactly partition $\mathbb Z$,

we have:

$$
\boxed{
\mathbb Z_{>0}
=
\bigsqcup_{w\in\{D,U\}^k}
\Omega_w.
}
$$

where:

$$
\bigsqcup
$$

denotes the disjoint union.

Therefore, every positive integer at any fixed depth $k$ belongs to exactly one parity chart.

This conclusion is extremely important:

$$
\boxed{
\text{the level-}k\text{ atlas is globally source-complete}.
}
$$

However, it is only complete in terms of source coverage for the "first $k$-step classification", not complete for Collatz convergence.

---

# 10. Closed Congruence Formula

From Paper 02:

$$
F_w(n)
=
\frac{3^un+b_w}{2^k}.
$$

If:

$$
n\in\Omega_w,
$$

then $F_w(n)$ must be an integer.

Thus:

$$
3^un+b_w
\equiv0
\pmod{2^k}.
$$

Since:

$$
\gcd(3^u,2^k)=1,
$$

$3^u$ is a unit in:

$$
\mathbb Z/2^k\mathbb Z.
$$

Therefore:

$$
\boxed{
n
\equiv
-b_w3^{-u}
\pmod{2^k}.
}
$$

By word–residue uniqueness,

this unique solution must be:

$$
\boxed{
r_w
\equiv
-b_w3^{-u}
\pmod{2^k}.
}
$$

---

# 11. Why Shouldn't We Rely Solely on This Congruence to Prove Admissibility?

Seeing only:

$$
3^un+b_w\equiv0\pmod{2^k}
$$

merely guarantees explicitly that the final denominator of the formal operator vanishes.

Without separately proving the uniqueness of the finite parity coding,

jumping directly from "the final result is an integer" to "every intermediate parity branch is correct" would leave a logical gap in the argument.

Therefore, this paper first uses layer-by-layer cylinder refinement to prove:

$$
\boxed{
\text{word}\leftrightarrow\text{residue}
}
$$

and then treats the closed congruence as the closed formula for that residue.

This is an important correction in the proof order.

---

# 12. Exact Cylinder Transport Theorem

## Theorem 12.1

Let:

$$
w\in\{D,U\}^k,
$$

$$
u=u(w),
$$

$$
r=r_w,
$$

and:

$$
m_w=T^k(r_w).
$$

Then for any:

$$
a\in\mathbb Z
$$

as long as:

$$
n=r+2^ka>0,
$$

we have:

$$
\boxed{
T^k(n)
=
m_w+3^ua.
}
$$

### Proof

Since:

$$
n\equiv r_w\pmod{2^k},
$$

by Theorem 8.1:

$$
n\in\Omega_w.
$$

Thus:

$$
T^k(n)=F_w(n).
$$

Substituting into the affine form from Paper 02:

$$
T^k(n)
=
\frac{3^u(r+2^ka)+b_w}{2^k}
$$

$$
=
\frac{3^ur+b_w}{2^k}
+
3^ua
$$

$$
=
m_w+3^ua.
$$

This completes the proof.

---

# 13. Source Cylinder and Target Progression

Define:

$$
\boxed{
\mathcal C_w
=
r_w+2^k\mathbb Z
}
$$

and:

$$
\boxed{
\mathcal P_w
=
m_w+3^u\mathbb Z.
}
$$

Then formally:

$$
\boxed{
F_w(\mathcal C_w)
=
\mathcal P_w.
}
$$

In the positive integer Collatz domain,

taking:

$$
\Omega_w=\mathcal C_w\cap\mathbb Z_{>0},
$$

its image:

$$
\Gamma_w=T^k(\Omega_w)
$$

is the portion of:

$$
\mathcal P_w
$$

corresponding to the same quotient coordinates and generated by positive sources.

If studied solely on the full integer affine extension,

then there is a complete two-way bijection between the cylinder and the progression.

---

# 14. Source Chart

Define:

$$
\boxed{
\phi_w:
\mathcal C_w\to\mathbb Z,
}
$$

$$
\boxed{
\phi_w(n)
=
\frac{n-r_w}{2^k}.
}
$$

Inverse mapping:

$$
\boxed{
\phi_w^{-1}(a)
=
r_w+2^ka.
}
$$

Thus, the source cylinder in the chart coordinate is simply the ordinary integer line:

$$
a\in\mathbb Z.
$$

---

# 15. Target Chart

Define:

$$
\boxed{
\psi_w:
\mathcal P_w\to\mathbb Z,
}
$$

$$
\boxed{
\psi_w(y)
=
\frac{y-m_w}{3^u}.
}
$$

Inverse:

$$
\boxed{
\psi_w^{-1}(a)
=
m_w+3^ua.
}
$$

---

# 16. Local Identity Trivialization Theorem

## Theorem 16.1

On:

$$
\mathcal C_w
$$

the formal operator:

$$
F_w
$$

satisfies:

$$
\boxed{
\psi_w
\circ
F_w
\circ
\phi_w^{-1}
=
\operatorname{id}_{\mathbb Z}.
}
$$

On the positive integer admissible domain:

$$
\Omega_w
$$

the corresponding restriction satisfies:

$$
\boxed{
\psi_w
\circ
T^k
\circ
\phi_w^{-1}
=
\operatorname{id}
}
$$

holding on its admissible quotient-coordinate subset.

### Proof

Take any $a$:

$$
\phi_w^{-1}(a)
=
r_w+2^ka.
$$

By cylinder transport:

$$
F_w(\phi_w^{-1}(a))
=
m_w+3^ua.
$$

Thus:

$$
\psi_w(m_w+3^ua)
=
a.
$$

This completes the proof.

---

# 17. This is Stronger Than "Linearization"

Paper 02 obtained:

$$
T^k(n)
=
\frac{3^un+b_w}{2^k}.
$$

This is merely affine compression.

Paper 03 further utilizes the source/target lattices:

$$
2^k\mathbb Z
$$

and:

$$
3^u\mathbb Z,
$$

to transform it into:

$$
\boxed{
a\mapsto a.
}
$$

Therefore:

$$
\boxed{
\text{affine linearization}
\to
\text{local identity trivialization}.
}
$$

This is an extreme simplification case of Operation Translation.

---

# 18. Exact Recovery

If we know:

$$
w,\quad r_w,\quad m_w,\quad k,\quad u,
$$

and the target:

$$
y\in\mathcal P_w,
$$

then:

$$
a
=
\frac{y-m_w}{3^u}
$$

is exactly an integer.

Therefore, the source can be exactly recovered:

$$
\boxed{
n
=
r_w
+
2^k
\frac{y-m_w}{3^u}.
}
$$

Thus, in the fixed-chart domain:

$$
\boxed{
\text{forward transport is lossless}.
}
$$

---

# 19. Faithfulness

If:

$$
n_1,n_2\in\mathcal C_w
$$

and:

$$
F_w(n_1)=F_w(n_2),
$$

then:

$$
\frac{3^u(n_1-n_2)}{2^k}=0.
$$

In $\mathbb Z/\mathbb Q$:

$$
n_1=n_2.
$$

Therefore, the fixed-word affine transform is injective.

Thus, local identity trivialization has no information loss.

---

# 20. Example 1: $w=D$

$$
r_D=0\pmod2.
$$

Take the representative:

$$
r_D=0.
$$

$$
m_D=T(0)=0
$$

in the integer affine extension.

cylinder:

$$
2\mathbb Z.
$$

target:

$$
\mathbb Z.
$$

source chart:

$$
a=n/2.
$$

target chart:

$$
a=y.
$$

Therefore:

$$
D(2a)=a.
$$

This is the simplest identity chart.

For the positive integer domain,

we only take:

$$
a\ge1.
$$

---

# 21. Example 2: $w=U$

$$
r_U=1\pmod2.
$$

Take:

$$
r_U=1.
$$

$$
m_U=T(1)=2.
$$

Thus:

$$
\boxed{
T(1+2a)
=
2+3a.
}
$$

source:

$$
1+2\mathbb Z,
$$

target:

$$
2+3\mathbb Z.
$$

charts:

$$
\phi_U(n)=\frac{n-1}{2},
$$

$$
\psi_U(y)=\frac{y-2}{3}.
$$

Then:

$$
\boxed{
\psi_UT\phi_U^{-1}(a)=a.
}
$$

---

# 22. Example 3: $w=UD$

From Paper 02:

$$
F_{UD}(n)
=
\frac{3n+1}{4}.
$$

Thus:

$$
u=1,
\qquad
b=1.
$$

residue:

$$
3n+1\equiv0\pmod4.
$$

Since:

$$
3^{-1}\equiv3\pmod4,
$$

$$
r_{UD}
\equiv
-3
\equiv1
\pmod4.
$$

Thus:

$$
\Omega_{UD}
=
(1+4\mathbb Z)\cap\mathbb Z_{>0}.
$$

Take:

$$
r=1.
$$

$$
m=T^2(1)=1.
$$

Therefore:

$$
\boxed{
T^2(1+4a)
=
1+3a.
}
$$

---

# 23. Example 4: $w=DU$

From Paper 02:

$$
F_{DU}(n)
=
\frac{3n+2}{4}.
$$

Thus:

$$
u=1,
\qquad
b=2.
$$

Solving:

$$
3n+2\equiv0\pmod4.
$$

yields:

$$
r_{DU}=2.
$$

$$
m=T^2(2)=2.
$$

Thus:

$$
\boxed{
T^2(2+4a)
=
2+3a.
}
$$

Note that for $UD$ and $DU$:

- $k$ is the same;
- $u$ is the same;
- the target step sizes are both $3$;

but:

$$
r_w,\quad m_w
$$

are different.

This is exactly the domain-level manifestation of the order correction from Paper 02.

---

# 24. Example 5: $w=UUDD$

From Paper 02:

$$
F_w(n)
=
\frac{9n+5}{16}.
$$

Thus:

$$
k=4,\qquad u=2,\qquad b=5.
$$

Solving:

$$
9n+5\equiv0\pmod{16}.
$$

Since:

$$
9^{-1}\equiv9\pmod{16},
$$

$$
r_w
\equiv
-45
\equiv3
\pmod{16}.
$$

Take:

$$
r_w=3.
$$

Directly:

$$
3\to5\to8\to4\to2.
$$

Thus:

$$
m_w=2.
$$

Therefore, the entire cylinder:

$$
\boxed{
3+16a
\longmapsto
2+9a.
}
$$

charts:

$$
\phi_w(n)
=
\frac{n-3}{16},
$$

$$
\psi_w(y)
=
\frac{y-2}{9}.
$$

Thus:

$$
\boxed{
a\mapsto a.
}
$$

---

# 25. Level-$k$ Collatz Atlas

Define each word chart:

$$
\boxed{
\mathcal A_w
=
(
\Omega_w,
\Gamma_w,
\phi_w,
\psi_w,
T^k|_{\Omega_w}
).
}
$$

All words of length $k$:

$$
\boxed{
\mathfrak A_k
=
\{
\mathcal A_w:
w\in\{D,U\}^k
\}.
}
$$

are called the **level-$k$ Collatz Local Affine Atlas**.

---

# 26. Source-Complete Atlas

By the Partition Theorem:

$$
\boxed{
\mathbb Z_{>0}
=
\bigsqcup_{w\in\{D,U\}^k}
\Omega_w.
}
$$

Therefore, for any positive integer $n$,

at level $k$ there is exactly one chart:

$$
\mathcal A_w
$$

responsible for describing its first $k$-step dynamics.

Thus:

$$
\boxed{
\mathfrak A_k
\text{ is source-complete}.
}
$$

---

# 27. But Target Charts Can Overlap

The target images:

$$
\Gamma_w,\Gamma_v
$$

of different $w\neq v$ are not necessarily mutually exclusive.

This is because different starting points can merge into the same state or the same progression intersection after $k$ steps.

Therefore:

$$
\boxed{
\text{source partition}
\neq
\text{target partition}.
}
$$

This point will become important in finite certificates / path-merging.

---

# 28. Atlas Refinement

Each:

$$
\Omega_w
$$

splits in the next level into:

$$
\boxed{
\Omega_w
=
\Omega_{wD}
\bigsqcup
\Omega_{wU}.
}
$$

And modulo:

$$
2^{k+1},
$$

these two child residues are exactly:

$$
r_w
$$

and:

$$
r_w+2^k.
$$

Which one corresponds to $D$ and which one corresponds to $U$

is determined by the parity of:

$$
m_w.
$$

---

# 29. Quotient Bit Interpretation

Write:

$$
n=r_w+2^ka.
$$

Then the next parity is:

$$
T^k(n)\pmod2
=
m_w+a\pmod2.
$$

Thus, in a fixed chart,

the next Collatz branch no longer requires re-evaluating the huge integer $n$.

One only needs to look at the quotient coordinate:

$$
\boxed{
a\bmod2
}
$$

plus a fixed chart bit:

$$
m_w\bmod2.
$$

This is a very important computational / symbolic simplification.

---

# 30. Atlas Refinement is Binary Decision

Therefore, from level $k$ to $k+1$:

$$
\boxed{
\text{one new itinerary symbol}
\leftrightarrow
\text{one new quotient bit}.
}
$$

The Collatz parity tree and binary residue refinement are therefore not merely analogous,

but are exactly the same finite combinatorial refinement structure.

---

# 31. Relationship with $2$-adic Parity Coding

Existing Collatz research has known that:

a one-to-one correspondence can be established between $2$-adic integers and their infinite parity sequences, and a conjugacy structure exists between the modified Collatz map and the $2$-adic shift.

This paper does not re-claim this result as a new discovery.

The finite contribution of this paper is to explicitly organize the finite prefix as:

$$
\boxed{
\text{word}
\leftrightarrow
\text{mod }2^k\text{ cylinder}
\leftrightarrow
\text{exact affine transport}
\leftrightarrow
\text{local identity chart}.
}
$$

Therefore, it is closer to the finite local atlas formulation of Operation Translation.

---

# 32. Finite Atlas and Infinite 2-adic Coding

If:

$$
w_1\prec w_2\prec w_3\prec\cdots
$$

is a consistent infinite parity-prefix chain,

corresponding to residues:

$$
r_1\bmod2,
$$

$$
r_2\bmod2^2,
$$

$$
r_3\bmod2^3,
$$

and satisfying:

$$
r_{k+1}
\equiv
r_k
\pmod{2^k}.
$$

This forms an inverse system,

whose limit naturally corresponds to a $2$-adic integer in:

$$
\mathbb Z_2.
$$

Therefore, finite atlas refinement is compatible with classical $2$-adic parity coding.

---

# 33. But the Positive Integer Problem Remains Different

An arbitrary infinite parity sequence corresponds to some:

$$
2\text{-adic integer},
$$

which does not mean that this $2$-adic integer is an ordinary positive integer.

Therefore:

$$
\boxed{
\text{$2$-adic itinerary existence}
\not\Rightarrow
\text{positive-integer orbit existence}.
}
$$

This is also why $2$-adic conjugacy itself does not directly solve the Collatz conjecture.

---

# 34. Local Identity Does Not Eliminate Global Dynamics

This point must be specially emphasized.

For a fixed $w$:

$$
\psi_wT^k\phi_w^{-1}
=
\operatorname{id}.
$$

This might lead one to mistakenly believe:

> Collatz has been transformed into the identity, so the problem is solved.

Incorrect.

Because each chart is only responsible for:

$$
k
$$

steps.

After stepping out of the target:

$$
\Gamma_w
$$

if one wants to continue to the next block,

the next admissible chart must be re-determined.

Therefore, the true global system is:

$$
\boxed{
\mathcal A_{w_0}
\to
\mathcal A_{w_1}
\to
\mathcal A_{w_2}
\to\cdots.
}
$$

---

# 35. Global Itinerary Problem

This allows the global difficulty of Collatz to be reformulated as:

> For every positive integer starting point, does its infinite chart itinerary inevitably enter a known descending / terminal certificate domain in finite time?

Thus:

$$
\boxed{
\text{local operator complexity}
}
$$

has been largely eliminated,

what remains is:

$$
\boxed{
\text{global chart-selection complexity}.
}
$$

This is the core division of labor in this series.

---

# 36. The Scales of Source Coordinates and Target Coordinates are Different

source spacing:

$$
2^k.
$$

target spacing:

$$
3^u.
$$

Therefore, identity trivialization does not mean saying on the original number line that:

$$
T^k(n)=n.
$$

Rather, it means:

$$
\boxed{
\text{the quotient label }a\text{ is preserved}.
}
$$

The original value changes:

$$
r_w+2^ka
\to
m_w+3^ua,
$$

but the chart coordinate:

$$
a
$$

remains unchanged.

This is the correct semantics of "local identity".

---

# 37. Exact Recovery and Series A

Series A emphasizes:

$$
\text{approximate coordinate}
\to
\text{exact decision}
$$

and:

$$
\text{faithful transform}.
$$

The situation in this paper is even stronger:

the coordinate:

$$
a
$$

itself is an exact integer.

Thus:

$$
\boxed{
\text{encoding}
\to
\text{identity transport}
\to
\text{exact decoding}
}
$$

involves absolutely no numerical approximation.

This is a purely discrete exact model.

---

# 38. Core Classification of Paper 03

For a fixed finite word:

### Domain legality

$$
n\in\Omega_w
\iff
n\equiv r_w\pmod{2^k}.
$$

### Exact operator

$$
T^k(n)
=
\frac{3^un+b_w}{2^k}.
$$

### Cylinder transport

$$
r_w+2^ka
\to
m_w+3^ua.
$$

### Local coordinate law

$$
a\to a.
$$

### Recovery

$$
n
=
r_w
+
2^k\frac{y-m_w}{3^u}.
$$

All five layers are exact.

---

# 39. Limitations of This Paper

First, this paper only deals with finite words / finite depth.

Second, this paper does not prove that any arbitrary infinite positive-integer itinerary converges.

Third, this paper does not claim the known $2$-adic parity conjugacy as a new discovery.

Fourth, the completeness of the source residue partition does not equal the completeness of target convergence coverage.

Fifth, local identity trivialization relies on word-specific source/target charts and is not a single global coordinate transform.

---

# 40. Summary of Main Theorems

## Theorem A — Unique Residue Cylinder

$$
\boxed{
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}.
}
$$

## Theorem B — Word–Residue Bijection

$$
\boxed{
\{D,U\}^k
\longleftrightarrow
\mathbb Z/2^k\mathbb Z.
}
$$

## Theorem C — Closed Residue Formula

$$
\boxed{
r_w
\equiv
-b_w3^{-u}
\pmod{2^k}.
}
$$

## Theorem D — Exact Cylinder Transport

$$
\boxed{
T^k(r_w+2^ka)
=
m_w+3^ua.
}
$$

## Theorem E — Local Identity Trivialization

$$
\boxed{
\psi_wT^k\phi_w^{-1}
=
\operatorname{id}.
}
$$

## Theorem F — Exact Recovery

$$
\boxed{
n
=
r_w+
2^k\frac{y-m_w}{3^u}.
}
$$

---

# 41. Conclusion

Paper 02 has already proven:

$$
\text{finite parity word}
\to
\text{exact affine operator}.
$$

This paper further proves:

$$
\text{finite parity word}
\to
\text{unique residue cylinder}.
$$

Therefore, combining the two yields:

$$
\boxed{
\text{word}
\longleftrightarrow
\text{source cylinder}
\longrightarrow
\text{target progression}.
}
$$

And in quotient coordinates:

$$
\boxed{
a\longmapsto a.
}
$$

Thus, the first $k$-step dynamics of Collatz,

can be completely trivialized in every admissible chart.

This is exactly the core meaning of:

$$
\boxed{
\text{Collatz Local Affine Atlas}
}
$$

What truly has not yet been trivialized is:

$$
\boxed{
\text{which chart comes next?}
}
$$

Therefore:

$$
\boxed{
\textbf{Collatz dynamics is locally identity-trivializable,
but globally itinerary-nontrivial.}
}
$$

After this paper, this is no longer merely a methodological slogan,

but has its first complete finite-domain theorem version.

Paper 04 will follow the exact cylinder transport of this paper:

$$
r_w+2^k a
\longmapsto
m_w+3^u a
$$

to study its inverse form,

and reconstruct the author's early concept of the "double helix" into:

$$
\boxed{
2^k\text{-source cylinder}
\leftrightarrow
3^u\text{-target progression}.
}
$$

---

# References

1. Olivier Rozier, *Parity sequences of the 3x+1 map on the 2-adic integers and Euclidean embedding*, arXiv:1805.00133.
2. Jonathan Yazinski, *Pseudoperiodicity and the 3x+1 Conjugacy Function*, arXiv:1102.5547.
3. Olivier Rozier, Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948.
4. Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886.
5. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), arXiv:1909.03562.
6. David Applegate, Jeffrey C. Lagarias, *The 3x+1 Semigroup*, Journal of Number Theory 117 (2006), arXiv:math/0411140.
7. Collatz Operation Translation Series — Paper 02, *Collatz Local Affine Atlas: Exact Affinization of Finite Parity Words*.

---

## Next Paper

**Paper 04 — *Bidirectional Residue Class Translation: $2^k$ Cylinders and $3^u$ Progressions***

Core tasks:

1. Formulate
   $$
   r_w+2^ka\mapsto m_w+3^ua
   $$
   as a complete bidirectional arithmetic transport;
2. Establish exact inverse legality;
3. Reorganize the inverse tree / odd skeleton;
4. Integrate old "highway" families such as $(4^j-1)/3$ back into the inverse-fiber framework;
5. Explicitly distinguish between local bijection, global merge, and inverse-tree coverage.