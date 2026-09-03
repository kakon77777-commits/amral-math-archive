# Bidirectional Residue-Class Translation: $2^k$ Cylinders and $3^u$ Progressions
## ——From the Collatz Local Affine Atlas to Exact Inverse Fibers, Odd Skeletons, and Double Helix Reconstruction

**English Title:** *Bidirectional Residue-Class Translation: From $2^k$ Cylinders to $3^u$ Progressions in the Collatz Local Affine Atlas*

**Author:** Neo.K  
**Institution:** EveMiss Technology Co., Ltd. (EveMissLab)  
**Series:** Collatz Operation Translation Series — Paper 04  
**Version:** v0.1  
**Date:** 2026-08-10

---

## Abstract

Paper 03 has proven that, for the modified Collatz map

$$
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\[2mm]
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
$$

each admissible parity word $w$ of length $k$ corresponds to a unique source residue cylinder

$$
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0},
$$

and if $u=u(w)$, $m_w=T^k(r_w)$, then

$$
\boxed{
T^k(r_w+2^ka)
=
m_w+3^ua.
}
$$

This paper elevates this unidirectional formula into a complete **bidirectional exact residue-class translation**.

On the all-integer affine extension, define

$$
\mathcal C_w=r_w+2^k\mathbb Z,
$$

$$
\mathcal P_w=m_w+3^u\mathbb Z.
$$

This paper proves:

$$
\boxed{
F_w:\mathcal C_w\overset{\sim}{\longrightarrow}\mathcal P_w
}
$$

is a bijection, and its inverse is

$$
\boxed{
F_w^{-1}(y)
=
r_w
+
2^k\frac{y-m_w}{3^u},
\qquad
y\equiv m_w\pmod{3^u}.
}
$$

Therefore, fixed-word Collatz transport can be understood as:

$$
\boxed{
r_w+2^k\mathbb Z
\;\longleftrightarrow\;
m_w+3^u\mathbb Z,
}
$$

where both sides share the same exact quotient coordinate

$$
a.
$$

The source side uses $2^k$ as the lattice spacing, and the target side uses $3^u$ as the lattice spacing; in the chart coordinate, both forward and inverse are simply

$$
a\leftrightarrow a.
$$

This paper refers to this structure as **Bidirectional Residue Transport**.

In the positive-integer Collatz domain, if we take the canonical representative

$$
0\le r_w<2^k,
$$

then the lower bound for the valid quotient coordinate is

$$
a_{\min}(w)
=
\begin{cases}
1,&r_w=0,\\
0,&r_w>0.
\end{cases}
$$

So the true positive source/image are

$$
\Omega_w
=
\{
r_w+2^ka:a\ge a_{\min}(w)
\},
$$

$$
\Gamma_w
=
\{
m_w+3^ua:a\ge a_{\min}(w)
\}.
$$

The inverse in a fixed chart thus remains exact, single-valued, and lossless.

This paper then reorganizes the author's early "double helix" research into two complementary levels:

1. **modified-map finite-word inverse transport**: composed of $2^k$ source cylinders and $3^u$ target progressions;
2. **accelerated odd-map inverse fibers**: for
   $$
   S(n)=\frac{3n+1}{2^{v_2(3n+1)}}
   $$
   define
   $$
   R_\kappa(t)=\frac{2^\kappa t-1}{3}.
   $$

If $t$ is a positive odd integer, then $R_\kappa(t)$ is a valid odd predecessor of $t$ if and only if

$$
\boxed{
2^\kappa t\equiv1\pmod3.
}
$$

Therefore:

- If $t\equiv1\pmod3$, the valid $\kappa$ must be even;
- If $t\equiv2\pmod3$, the valid $\kappa$ must be odd;
- If $3\mid t$, no accelerated odd predecessor exists.

Specifically, for the terminal state $t=1$:

$$
\kappa=2j
$$

gives

$$
\boxed{
R_{2j}(1)
=
\frac{4^j-1}{3}.
}
$$

Therefore, the $M_j=\frac{4^j-1}{3}$ from the author's previous research no longer needs to be interpreted as an independent "mysterious highway series"; it is precisely the valuation-labelled inverse fiber of the terminal state $1$ in the accelerated odd map. The number $5$ is simply

$$
R_4(1)=5,
$$

and $5\cdot2^q$ is its even $2$-ray in the ordinary Collatz inverse structure.

This paper also reorganizes the odd skeleton. Any positive integer can be uniquely represented as

$$
n=2^{v_2(n)}\operatorname{oddcore}(n),
$$

so the ordinary Collatz inverse coverage can be decomposed into:

$$
\boxed{
\text{odd inverse skeleton}
+
\text{even }2\text{-rays}.
}
$$

On the accelerated odd map, all nodes are odd states; the inverse fibers $R_\kappa(t)$ directly describe the edge labels of the odd skeleton.

This paper particularly emphasizes that three different "inverses" must not be confused:

- fixed-word local inverse;
- inverse-tree predecessor relation;
- global inverse coverage.

The first two can be exact; the third remains equivalent to the global Collatz problem. In other words:

$$
\boxed{
\text{local invertibility}
\not\Rightarrow
\text{global inverse-tree coverage}.
}
$$

This paper thus redefines the early "double helix" from a visual/graph-theoretic approach into a rigorous arithmetic framework:

$$
\boxed{
\text{forward }2^k\text{-cylinder refinement}
\quad\leftrightarrow\quad
\text{backward }3^u\text{-progression / valuation fiber}.
}
$$

**Keywords:** Collatz conjecture, inverse iteration, residue class, $2$-adic cylinder, $3$-progression, accelerated Collatz, valuation fiber, odd skeleton, bidirectional transport, exact recovery

---

# 1. Problem: Can the forward transport of Paper 03 be truly reversed?

Paper 03 has obtained:

$$
\boxed{
T^k(r_w+2^ka)
=
m_w+3^ua.
}
$$

This equation already implies:

- the source quotient label is $a$;
- the target quotient label is also $a$.

So the most natural question is:

> If only the target $y$ and the fixed chart $w$ are known, can the source $n$ be exactly recovered?

The answer is affirmative.

---

# 2. All-Integer Affine Extension

To avoid interference from positive-integer boundaries on the algebraic structure, first consider on:

$$
\mathbb Z
$$

the fixed-word affine map:

$$
F_w(x)
=
\frac{3^ux+b_w}{2^k}.
$$

Define the source cylinder:

$$
\boxed{
\mathcal C_w
=
r_w+2^k\mathbb Z.
}
$$

From Paper 03:

$$
r_w
\equiv
-b_w3^{-u}
\pmod{2^k},
$$

so for:

$$
x\in\mathcal C_w,
$$

$F_w(x)$ must be an integer.

---

# 3. Target Progression

Let:

$$
m_w=F_w(r_w).
$$

For:

$$
x=r_w+2^ka,
$$

we have:

$$
F_w(x)
=
m_w+3^ua.
$$

Therefore, the image is exactly:

$$
\boxed{
\mathcal P_w
=
m_w+3^u\mathbb Z.
}
$$

So:

$$
\boxed{
F_w(\mathcal C_w)=\mathcal P_w.
}
$$

---

# 4. Bidirectional Residue Transport Theorem

## Theorem 4.1

For any finite parity word $w$:

$$
F_w:
\mathcal C_w
\to
\mathcal P_w
$$

is a bijection.

Its inverse is:

$$
\boxed{
F_w^{-1}(y)
=
r_w
+
2^k
\frac{y-m_w}{3^u}.
}
$$

### Proof

If:

$$
y\in\mathcal P_w,
$$

then there uniquely exists:

$$
a\in\mathbb Z
$$

such that:

$$
y=m_w+3^ua.
$$

Define:

$$
x=r_w+2^ka.
$$

Then:

$$
F_w(x)
=
m_w+3^ua
=
y.
$$

Uniqueness comes from $3^u\neq0$ and the uniqueness of the source coordinate $a$.

This completes the proof.

---

# 5. Inverse Legality Congruence

From:

$$
y=m_w+3^ua,
$$

we obtain:

$$
\boxed{
y\equiv m_w\pmod{3^u}.
}
$$

Conversely, if:

$$
y\equiv m_w\pmod{3^u},
$$

then:

$$
a=\frac{y-m_w}{3^u}\in\mathbb Z
$$

and gives the unique source:

$$
x=r_w+2^ka.
$$

Therefore, the fixed-word inverse legality is exactly:

$$
\boxed{
y\equiv m_w\pmod{3^u}.
}
$$

---

# 6. Dual Residue-Class Structure of Source and Target

source:

$$
\boxed{
x\equiv r_w\pmod{2^k}.
}
$$

target:

$$
\boxed{
y\equiv m_w\pmod{3^u}.
}
$$

So a single chart simultaneously possesses:

$$
\boxed{
(2^k,r_w)
}
$$

and:

$$
\boxed{
(3^u,m_w)
}
$$

two sets of residual metadata.

Which can be denoted as:

$$
\boxed{
\mathcal R(w)
=
(2^k,r_w;3^u,m_w).
}
$$

---

# 7. Quotient Coordinate Conservation

source coordinate:

$$
a
=
\frac{x-r_w}{2^k}.
$$

target coordinate:

$$
a
=
\frac{y-m_w}{3^u}.
$$

Therefore:

$$
\boxed{
\frac{x-r_w}{2^k}
=
\frac{y-m_w}{3^u}.
}
$$

This is the core conservation equation of fixed-word transport.

It is not that "the value $x$ is invariant".

What is truly invariant is:

$$
\boxed{
\text{chart quotient label }a.
}
$$

---

# 8. Cross-Multiplied Exact Relation

The previous equation is equivalent to:

$$
\boxed{
3^u(x-r_w)
=
2^k(y-m_w).
}
$$

This equation requires no division at all.

Therefore, in an exact-integer backend, it can directly serve as a:

$$
\boxed{
\text{transport certificate}.
}
$$

It also provides a bidirectional consistency check that does not rely on floating-point numbers.

---

# 9. Positive-Integer Domain

The true Collatz domain of Paper 03 is:

$$
\Omega_w
=
\mathcal C_w\cap\mathbb Z_{>0}.
$$

Take the canonical:

$$
0\le r_w<2^k.
$$

If:

$$
r_w>0,
$$

then:

$$
a\ge0
$$

guarantees:

$$
r_w+2^ka>0.
$$

If:

$$
r_w=0,
$$

then it must be that:

$$
a\ge1.
$$

Therefore, define:

$$
\boxed{
a_{\min}(w)
=
\begin{cases}
1,&r_w=0,\\
0,&r_w>0.
\end{cases}
}
$$

---

# 10. Positive Source / Image Theorem

So:

$$
\boxed{
\Omega_w
=
\{
r_w+2^ka:
a\ge a_{\min}(w)
\}.
}
$$

Its positive-integer image is:

$$
\boxed{
\Gamma_w
=
\{
m_w+3^ua:
a\ge a_{\min}(w)
\}.
}
$$

And:

$$
\boxed{
T^k:
\Omega_w
\overset{\sim}{\longrightarrow}
\Gamma_w
}
$$

remains a bijection.

Therefore, on a fixed chart:

$$
\boxed{
\text{positive-domain exact recovery}
}
$$

holds.

---

# 11. Example: $w=U$

From Paper 03:

$$
r_U=1,
$$

$$
m_U=2,
$$

$$
k=1,
\qquad
u=1.
$$

Therefore:

$$
\boxed{
1+2a
\longleftrightarrow
2+3a.
}
$$

inverse:

$$
\boxed{
n
=
1+2\frac{y-2}{3}.
}
$$

Valid target:

$$
\boxed{
y\equiv2\pmod3.
}
$$

---

# 12. Single-step inverse branches of the modified Collatz map

From:

$$
T(n)=y.
$$

There are two possibilities.

## even predecessor

If $n$ is even:

$$
n/2=y
$$

so:

$$
\boxed{
n=2y.
}
$$

This predecessor exists for all:

$$
y>0
$$

---

## odd predecessor

If $n$ is odd:

$$
\frac{3n+1}{2}=y.
$$

So:

$$
\boxed{
n=\frac{2y-1}{3}.
}
$$

To be an integer:

$$
2y-1\equiv0\pmod3.
$$

That is:

$$
\boxed{
y\equiv2\pmod3.
}
$$

In this case:

$$
y=3q+2
$$

gives:

$$
n=2q+1,
$$

which is automatically odd.

Therefore, the modified-map inverse relation is:

$$
\boxed{
T^{-1}(y)
=
\{2y\}
\cup
\left\{
\frac{2y-1}{3}
:
y\equiv2\pmod3
\right\}.
}
$$

---

# 13. Relationship with the original Collatz inverse branch

original map odd step:

$$
n\mapsto3n+1.
$$

The odd predecessor for target $y$ is:

$$
n=\frac{y-1}{3}.
$$

Its validity condition is:

$$
\boxed{
y\equiv4\pmod6.
}
$$

The modified map merges the inevitable division by 2 after the odd step,

so the target is changed to:

$$
y_{\mathrm{mod}}
=
\frac{y_{\mathrm{orig}}}{2}.
$$

Therefore:

$$
y_{\mathrm{orig}}\equiv4\pmod6
$$

is exactly equivalent to:

$$
y_{\mathrm{mod}}\equiv2\pmod3.
$$

So the two inverse conditions are simply the same arithmetic restriction sampled at different times.

---

# 14. Repositioning of early "branch points"

Previous research called the original target:

$$
y\equiv4\pmod6
$$

a branch point capable of generating an odd predecessor.

In the modified map, it is more naturally written as:

$$
\boxed{
y\equiv2\pmod3.
}
$$

Therefore, branch sparsity can be viewed as:

$$
\boxed{
\text{target-domain inverse legality}.
}
$$

This is more precise than "decimal filtering" and completely independent of base-10.

---

# 15. Difference between fixed-word inverse and inverse tree

fixed-word inverse:

$$
F_w^{-1}:
\mathcal P_w
\to
\mathcal C_w
$$

is single-valued.

But the global Collatz inverse:

$$
T^{-1}(y)
$$

is generally:

- one predecessor;
- or two predecessors.

So:

$$
\boxed{
\text{fixed itinerary removes inverse branching}.
}
$$

This is an important local simplification.

---

# 16. Why is the inverse single-valued after fixing the word?

Because global inverse branching comes from:

> Not knowing the branch history of the predecessor.

Once $w$ is fixed,

the branch history is known,

so all branching decisions are eliminated.

Therefore:

$$
\boxed{
\text{inverse ambiguity}
=
\text{itinerary uncertainty}.
}
$$

In a fixed-word chart, itinerary uncertainty is zero,

thus the inverse is exact and single-valued.

---

# 17. Odd Core

Any:

$$
n\in\mathbb Z_{>0}
$$

is uniquely represented as:

$$
\boxed{
n=2^{v_2(n)}m,
\qquad
m\text{ odd}.
}
$$

Define:

$$
\boxed{
\operatorname{oddcore}(n)
=
\frac{n}{2^{v_2(n)}}.
}
$$

Therefore, all positive integers are partitioned into disjoint $2$-rays:

$$
\boxed{
\mathbb Z_{>0}
=
\bigsqcup_{m\text{ odd}}
\{2^qm:q\ge0\}.
}
$$

---

# 18. Odd Skeleton of the Inverse Tree

If a certain odd state:

$$
m
$$

is already in the inverse convergence tree,

then:

$$
m,2m,4m,8m,\ldots
$$

are all automatically in the tree.

Therefore, global inverse coverage is equivalent to odd coverage:

$$
\boxed{
\text{all positive integers covered}
\iff
\text{all positive odd integers covered}.
}
$$

So the inverse tree can be divided into:

$$
\boxed{
\text{odd skeleton}
+
\text{even }2\text{-rays}.
}
$$

This observation from previous research is preserved in this paper.

---

# 19. Accelerated Odd Map

For positive odd $n$, define:

$$
\boxed{
S(n)
=
\frac{3n+1}{2^{\kappa(n)}},
}
$$

where:

$$
\boxed{
\kappa(n)
=
v_2(3n+1).
}
$$

Because:

$$
3n+1
$$

is even,

so:

$$
\kappa(n)\ge1.
$$

And:

$$
S(n)
$$

is again odd.

Therefore:

$$
S:
\mathbb Z_{>0}^{\mathrm{odd}}
\to
\mathbb Z_{>0}^{\mathrm{odd}}.
$$

---

# 20. Accelerated Inverse Fiber

Given an odd target:

$$
t,
$$

if:

$$
S(n)=t,
$$

then there exists:

$$
\kappa\ge1
$$

such that:

$$
3n+1
=
2^\kappa t.
$$

So:

$$
\boxed{
n
=
R_\kappa(t)
=
\frac{2^\kappa t-1}{3}.
}
$$

This is the valuation-labelled inverse candidate.

---

# 21. Inverse Fiber Legality Theorem

## Theorem 21.1

For positive odd $t$ and $\kappa\ge1$,

$$
R_\kappa(t)
=
\frac{2^\kappa t-1}{3}
$$

is a valid positive odd predecessor if and only if:

$$
\boxed{
2^\kappa t\equiv1\pmod3.
}
$$

### Proof

If the congruence holds,

the numerator is divisible by 3.

Since:

$$
2^\kappa t
$$

is even,

the numerator:

$$
2^\kappa t-1
$$

is odd.

Dividing by the odd number 3 still yields an odd number.

Positivity is obvious.

The converse holds immediately.

This completes the proof.

---

# 22. Complete Classification Modulo 3

Since $t$ is odd,

consider:

$$
t\bmod3.
$$

### Case A

If:

$$
t\equiv1\pmod3,
$$

it requires:

$$
2^\kappa\equiv1\pmod3.
$$

And:

$$
2^\kappa
\equiv
(-1)^\kappa
\pmod3.
$$

So:

$$
\boxed{
\kappa\text{ must be even}.
}
$$

### Case B

If:

$$
t\equiv2\pmod3,
$$

it requires:

$$
2^\kappa(-1)\equiv1\pmod3,
$$

so:

$$
\boxed{
\kappa\text{ must be odd}.
}
$$

### Case C

If:

$$
t\equiv0\pmod3,
$$

then:

$$
2^\kappa t\equiv0\pmod3
$$

cannot equal 1.

So:

$$
\boxed{
3\mid t
\Rightarrow
S^{-1}(t)=\varnothing.
}
$$

---

# 23. Accelerated Map Image Avoids Multiples of 3

From the previous section:

$$
\boxed{
S(n)\not\equiv0\pmod3
}
$$

for all odd $n$.

This can also be seen directly:

$$
3n+1\equiv1\pmod3,
$$

and dividing by:

$$
2^\kappa
$$

only multiplies by a unit mod 3.

So the target states of the accelerated odd skeleton always fall in:

$$
\boxed{
1,2\pmod3.
}
$$

---

# 24. Terminal Fiber at $t=1$

Take:

$$
t=1.
$$

Since:

$$
1\equiv1\pmod3,
$$

valid $\kappa$ must be even:

$$
\kappa=2j,
\qquad
j\ge1.
$$

Therefore:

$$
R_{2j}(1)
=
\frac{2^{2j}-1}{3}.
$$

That is:

$$
\boxed{
R_{2j}(1)
=
\frac{4^j-1}{3}.
}
$$

This is exactly the:

$$
\boxed{
M_j.
}
$$

from previous research.

---

# 25. Reinterpretation of the old "highway" family

Previous research:

$$
M_j
=
\frac{4^j-1}{3}
=
1,5,21,85,341,\ldots.
$$

In the past, they were viewed as a special family for rapidly entering the powers-of-two spine.

Now, their essence can be precisely written as:

$$
\boxed{
S(M_j)=1.
}
$$

And:

$$
\boxed{
v_2(3M_j+1)=2j.
}
$$

So:

$$
M_j
$$

is the complete valid even-valuation inverse fiber of the terminal odd state 1.

This is more structured and more general than a "highway".

---

# 26. Repositioning of the number 5

$$
5
=
\frac{4^2-1}{3}
=
R_4(1).
$$

So:

$$
\boxed{
5
\text{ is simply an inverse-fiber member of }t=1,\kappa=4.
}
$$

Its ordinary Collatz trajectory is:

$$
5\to16\to8\to4\to2\to1.
$$

And:

$$
5\cdot2^q
$$

is just the even $2$-ray above the odd node 5.

Therefore, there is no need to additionally assume that "5 is a super attractor".

---

# 27. Inverse Highway Family for Arbitrary Targets

For any positive odd:

$$
t\not\equiv0\pmod3,
$$

there are infinitely many parity-compatible $\kappa$:

If:

$$
t\equiv1\pmod3,
$$

then:

$$
\kappa=2,4,6,\ldots.
$$

If:

$$
t\equiv2\pmod3,
$$

then:

$$
\kappa=1,3,5,\ldots.
$$

Therefore:

$$
\boxed{
\mathcal R(t)
=
\left\{
\frac{2^\kappa t-1}{3}:
2^\kappa t\equiv1\pmod3
\right\}
}
$$

forms the accelerated inverse fiber of target $t$.

So the early "highways" do not only exist at 1.

Every valid odd target has its own valuation-labelled inverse family.

---

# 28. Odd Skeleton as a Valuation-Labeled Graph

Therefore, the accelerated inverse graph can be represented as:

Nodes:

$$
t\in\mathbb Z_{>0}^{\mathrm{odd}},
\qquad
3\nmid t
$$

and their admissible predecessors.

Edge label:

$$
\boxed{
\kappa=v_2(3n+1).
}
$$

Edge relation:

$$
\boxed{
n
\xrightarrow{\;\kappa\;}
t
\iff
n=\frac{2^\kappa t-1}{3}.
}
$$

So the odd skeleton is a valuation-labelled directed graph.

---

# 29. Relationship with the early double helix

The old "double helix" mainly viewed:

- the forward orbit;
- the backward convergence tree;

as two paths moving toward each other.

After this paper, it can be rewritten more precisely.

## Forward local strand

$$
\boxed{
r_w+2^k a
\to
m_w+3^u a.
}
$$

## Backward local strand

$$
\boxed{
m_w+3^u a
\to
r_w+2^k a.
}
$$

## Accelerated odd inverse strand

$$
\boxed{
t
\leftarrow
\frac{2^\kappa t-1}{3}.
}
$$

Therefore, the "double helix" is no longer just a visual diagram,

but:

$$
\boxed{
\text{two compatible exact coordinate directions}.
}
$$

---

# 30. Why is it called $2^k\leftrightarrow3^u$?

In a fixed finite word:

source spacing:

$$
2^k.
$$

target spacing:

$$
3^u.
$$

So:

$$
\boxed{
2^k
}
$$

controls the admissible source residue resolution,

while:

$$
\boxed{
3^u
}
$$

controls the target progression resolution.

The quotient label for these two scales:

$$
a
$$

is exactly the same.

---

# 31. This does not mean "$2$-adic = $3$-adic"

Over-interpretation must be avoided.

This paper only proves the fixed-word arithmetic progression transport:

$$
r_w+2^k\mathbb Z
\leftrightarrow
m_w+3^u\mathbb Z.
$$

It does not automatically establish:

$$
\mathbb Z_2\cong\mathbb Z_3.
$$

In fact:

$$
\mathbb Z_2
$$

and:

$$
\mathbb Z_3
$$

have different local-field / topological structures.

So:

$$
\boxed{
\text{$2^k$/$3^u$ bidirectional residue transport}
}
$$

is not:

$$
\boxed{
\text{global $2$-adic/$3$-adic isomorphism}.
}
$$

---

# 32. Local Inverse ≠ Global Coverage

For a fixed $w$:

$$
F_w^{-1}
$$

exists and is exact.

But the Collatz conjecture requires:

$$
\forall n>0,
$$

its forward orbit eventually enters the terminal cycle.

The inverse formulation equivalently requires:

$$
\boxed{
\text{inverse tree rooted at 1 covers all positive integers}.
}
$$

The local inverse theorem only answers:

> If the itinerary / target congruence is known, how can we exactly solve for the inverse?

It does not answer:

> Does every integer appear in the terminal inverse tree?

So:

$$
\boxed{
\text{local exact inversion}
\not\Rightarrow
\text{global inverse coverage}.
}
$$

---

# 33. Merge and Inversion are also different

If different charts:

$$
w\neq v
$$

satisfy:

$$
\Gamma_w\cap\Gamma_v\neq\varnothing,
$$

there may exist different sources that merge to the same target after a fixed number of steps.

This does not violate fixed-chart injectivity,

because injectivity is internal to:

$$
F_w|_{\mathcal C_w}
$$

Across charts:

$$
F_w(x)=F_v(z)
$$

is entirely possible.

Therefore:

$$
\boxed{
\text{local bijection}
\neq
\text{global one-to-one dynamics}.
}
$$

---

# 34. Fixed-Word Fiber Intersection

If:

$$
y\in\Gamma_w\cap\Gamma_v,
$$

then there exist:

$$
a,b
$$

such that:

$$
y=m_w+3^{u_w}a
$$

and:

$$
y=m_v+3^{u_v}b.
$$

This transforms into a linear Diophantine congruence:

$$
m_w-m_v
=
3^{u_v}b-3^{u_w}a.
$$

Therefore, the target merge problem itself can also be reduced to an arithmetic progression intersection.

This will reappear in the finite certificate frontier of Paper 09.

---

# 35. Relationship with the 3x+1 Semigroup

Existing research on the 3x+1 semigroup has already used rational multiplicative generators to encode backward iteration.

This paper does not claim that "backward algebraic encoding" is a new discovery.

The specific work of this paper is to write the finite parity chart of Paper 03 as:

$$
\boxed{
\text{source residue class}
\overset{F_w}{\longleftrightarrow}
\text{target progression}
}
$$

and provide exact forward/inverse recovery using the same quotient coordinate.

This is the atlas formulation of the Operation Translation Series.

---

# 36. Relationship with the $2$-adic inverse parity transform

Existing $2$-adic Collatz research has studied:

$$
\text{$2$-adic integer}
\leftrightarrow
\text{infinite parity sequence}.
$$

This paper only deals with finite words:

$$
w\in\{D,U\}^k
$$

and their:

$$
r_w\bmod2^k.
$$

Therefore, the finite residue atlas is compatible with $2$-adic parity coding,

but this paper further appends:

$$
\boxed{
m_w\bmod3^u
}
$$

as target-side metadata,

for exact inverse recovery.

---

# 37. Bidirectional Chart Object

This paper denotes the complete bidirectional data of a fixed word as:

$$
\boxed{
\mathcal B_w
=
(
w,
k,
u,
b_w,
r_w,
m_w,
\mathcal C_w,
\mathcal P_w,
\phi_w,
\psi_w
).
}
$$

where:

$$
\phi_w(n)=\frac{n-r_w}{2^k},
$$

$$
\psi_w(y)=\frac{y-m_w}{3^u}.
$$

and:

$$
\boxed{
\psi_wF_w\phi_w^{-1}
=
\operatorname{id}.
}
$$

---

# 38. Bidirectional Certificate

Given:

$$
(x,y,w),
$$

it can be verified using three exact conditions:

### Source legality

$$
\boxed{
x\equiv r_w\pmod{2^k}.
}
$$

### Target legality

$$
\boxed{
y\equiv m_w\pmod{3^u}.
}
$$

### Transport consistency

$$
\boxed{
3^u(x-r_w)
=
2^k(y-m_w).
}
$$

If all three hold and satisfy the positive-domain quotient bound,

then the fixed-word transport can be machine-exactly verified.

---

# 39. Significance for finite verification

Traditional finite verification often stores:

$$
n\to T(n)\to T^2(n)\to\cdots.
$$

This paper shows that for a known word:

$$
w
$$

one only needs to store:

$$
\boxed{
(r_w,m_w,k,u,b_w).
}
$$

All starting states of the entire cylinder can be batch-described by the quotient label $a$.

Therefore:

$$
\boxed{
\text{trajectory storage}
\to
\text{chart certificate storage}.
}
$$

This will be formalized in Paper 09.

---

# 40. Summary of Main Theorems in this Paper

## Theorem A — Bidirectional Residue Transport

$$
\boxed{
r_w+2^k\mathbb Z
\overset{\sim}{\longleftrightarrow}
m_w+3^u\mathbb Z.
}
$$

## Theorem B — Exact Inverse

$$
\boxed{
x
=
r_w+
2^k\frac{y-m_w}{3^u}.
}
$$

## Theorem C — Target Legality

$$
\boxed{
y\equiv m_w\pmod{3^u}.
}
$$

## Theorem D — Quotient Conservation

$$
\boxed{
\frac{x-r_w}{2^k}
=
\frac{y-m_w}{3^u}.
}
$$

## Theorem E — Accelerated Inverse Fiber

$$
\boxed{
R_\kappa(t)
=
\frac{2^\kappa t-1}{3}
}
$$

Valid iff:

$$
\boxed{
2^\kappa t\equiv1\pmod3.
}
$$

## Theorem F — Terminal Fiber

$$
\boxed{
R_{2j}(1)
=
\frac{4^j-1}{3}.
}
$$

---

# 41. Limitations of this Paper

First, the fixed-word inverse relies on a known chart $w$.

Second, target progressions can overlap across charts.

Third, this paper does not prove that the inverse tree rooted at 1 covers all positive integers.

Fourth, the $2^k\leftrightarrow3^u$ in this paper is a finite arithmetic progression transport, not a global isomorphism between $\mathbb Z_2$ and $\mathbb Z_3$.

Fifth, accelerated inverse fibers describe odd skeleton edge candidates, but global coverage remains an unsolved problem.

---

# 42. Conclusion

Paper 03 proved:

$$
\text{parity word}
\longleftrightarrow
\text{unique }2^k\text{ source cylinder}.
$$

This paper further proves:

$$
\boxed{
\text{source }2^k\text{ cylinder}
\longleftrightarrow
\text{target }3^u\text{ progression}.
}
$$

Both sides are connected by the same exact quotient coordinate:

$$
a
$$

Therefore, fixed-word Collatz dynamics can not only be forward-compressed,

but also allow for exact inverse recovery.

This gives the author's early "double helix" research a more rigorous new form:

$$
\boxed{
\text{forward residue refinement}
+
\text{backward valuation / progression fibers}.
}
$$

On the other hand,

the:

$$
\frac{4^j-1}{3}
$$

from previous research is also repositioned as:

$$
\boxed{
\text{the accelerated inverse fiber of terminal state }1.
}
$$

So:

- powers of two;
- odd skeleton;
- $M_j$;
- 5;
- $5\cdot2^q$;

no longer need to be treated as mutually isolated "special structures", but can be unified into:

$$
\boxed{
\text{odd inverse skeleton}
+
\text{valuation-labelled fibers}
+
\text{even }2\text{-rays}.
}
$$

At this point, the early double helix framework has completed its reconstruction from a graphical method to exact residue transport.

The next paper will turn to another question:

> Among all finite parity charts, which charts inevitably descend at a sufficiently large scale?

and establish the contraction bound for:

$$
\boxed{
3^u<2^k
}
$$

the word-order threshold, and the binomial Cylinder Law.

---

# References

1. David Applegate, Jeffrey C. Lagarias, *The 3x+1 Semigroup*, Journal of Number Theory 117 (2006), arXiv:math/0411140.
2. Olivier Rozier, *Parity sequences of the 3x+1 map on the 2-adic integers and Euclidean embedding*, arXiv:1805.00133.
3. Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886.
4. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), arXiv:1909.03562.
5. Collatz Operation Translation Series — Paper 01, *Reclassification and Correction of Existing Research on the Collatz Conjecture*.
6. Collatz Operation Translation Series — Paper 02, *Collatz Local Affine Atlas: Exact Affinization of Finite Parity Words*.
7. Collatz Operation Translation Series — Paper 03, *Parity Words, Residue Cylinders, and Local Identitization*.

---

## Next Paper

**Paper 05 — *Finite-Word Contraction Bounds and the Binomial Cylinder Law***

Core tasks:

1. Prove
   $$
   T_w(n)<n
   \iff
   b_w<(2^k-3^u)n;
   $$
2. Establish the asymptotic contraction criterion for $3^u<2^k$;
3. Define
   $$
   \alpha=\frac{\ln2}{\ln3};
   $$
4. Prove the fixed $k$ contracting word count:
   $$
   A_k=
   \sum_{u=0}^{\lfloor \alpha k\rfloor}\binom ku;
   $$
5. Provide a pure mathematical explanation for the $89.4943\%$ at $k=16$;
6. Prove that the contracting-cylinder density $P_k\to1$;
7. Rigorously point out the gap between density-one and universal Collatz convergence.