# Collatz Local Affine Atlas: Exact Affine Linearization of Finite Parity Words
## — Finite-Word Affine Closure, Count/Order Decomposition, and Word Order Correction

**English Title:** *Collatz Local Affine Atlas: Exact Affine Linearization of Finite Parity Words*

**Author:** Neo.K  
**Institution:** EveMiss Technology Co., Ltd. (EveMissLab)  
**Series:** Collatz Operation Translation Series — Paper 02  
**Version:** v0.1.1  
**Date:** 2026-08-10  
**Revision Date:** 2026-08-14

---

## Abstract

This paper establishes the first core mathematical layer of the Collatz Operation Translation Series: **the exact affine closure of finite parity words**.

We adopt the modified Collatz map

$$
T(n)=
\begin{cases}
\dfrac n2,&n\equiv0\pmod2,\\[2mm]
\dfrac{3n+1}{2},&n\equiv1\pmod2,
\end{cases}
$$

and define two branch operators

$$
D(x)=\frac x2,
\qquad
U(x)=\frac{3x+1}{2}.
$$

For any finite word of length $k$

$$
w=\sigma_1\sigma_2\cdots\sigma_k,
\qquad
\sigma_j\in\{D,U\},
$$

let $u(w)$ be the total number of occurrences of $U$. This paper proves that there exists a unique non-negative integer $b_w$ such that the formal composition can always be written as

$$
\boxed{
F_w(x)
=
\frac{3^{u(w)}x+b_w}{2^k}.
}
$$

If $U$ appears at positions

$$
1\le j_1<j_2<\cdots<j_u\le k,
$$

then

$$
\boxed{
b_w
=
\sum_{t=1}^{u}
2^{j_t-1}3^{u-t}.
}
$$

Therefore, all affine information of a finite Collatz word can be exactly decomposed into

$$
\boxed{
(k,u(w))
+
b_w.
}
$$

Here, $(k,u)$ determines the principal slope

$$
\lambda_w=\frac{3^u}{2^k},
$$

while $b_w$ preserves the affine offset caused by the branch order. This provides the most important structural decomposition of this paper:

$$
\boxed{
\text{counts determine the multiplicative skeleton;}
}
$$

$$
\boxed{
\text{order determines the affine correction.}
}
$$

This paper further establishes the recurrence relations

$$
b_{wD}=b_w,
$$

$$
\boxed{
b_{wU}=3b_w+2^{|w|},
}
$$

as well as the string composition law. If $w$ is executed first followed by $v$, then

$$
\boxed{
b_{wv}
=
3^{u(v)}b_w
+
2^{|w|}b_v.
}
$$

Thus, the triplet

$$
\Omega(w)=(|w|,u(w),b_w)
$$

possesses an exact semidirect product structure under concatenation.

This same structure can also be represented using upper-triangular matrices:

$$
M_D=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
M_U=
\begin{pmatrix}
3&1\\
0&2
\end{pmatrix},
$$

and

$$
\boxed{
M_w=
\begin{pmatrix}
3^{u(w)}&b_w\\
0&2^{|w|}
\end{pmatrix}.
}
$$

Word composition is thereby transformed into matrix multiplication. This representation clearly reveals that the scalar principal multiplier $3^u$ and the denominator $2^k$ depend only on branch counts; the noncommutative word order information is concentrated entirely in the top-right correction term $b_w$.

This paper also strictly distinguishes between two levels:

1. **Formal Word Operator**: Any $w\in\{D,U\}^*$ defines an affine operator over $\mathbb Q$;
2. **Admissible Collatz Itinerary**: Only when the actual parity decisions of an input $n$ match $w$ do we have
   $$
   T^k(n)=F_w(n).
   $$

Therefore, finite-word affine closure does not mean that any word is a valid Collatz trajectory for any positive integer. This domain restriction will be further formalized in Paper 03 as the correspondence between a parity word and a unique residue cylinder modulo $2^k$.

This paper also proves that for a fixed $(k,u)$, the extrema of $b_w$ are determined by the word order:

$$
\boxed{
3^u-2^u
\le b_w
\le
2^{k-u}(3^u-2^u),
}
$$

where the minimum is achieved by

$$
U^uD^{k-u}
$$

and the maximum is achieved by

$$
D^{k-u}U^u
$$

This makes the "order correction" not just a concept, but a quantity with a clearly computable finite range.

This paper does not claim that the finite affine closure itself solves the Collatz conjecture. On the contrary, the conclusion of this paper is precisely that:

$$
\boxed{
\text{finite local arithmetic is exactly compressible;}
}
$$

and the truly unclosed problem will shift to:

$$
\boxed{
\text{which affine chart is admissible at each stage?}
}
$$

which is referred to subsequently as the global itinerary problem.

**Keywords:** Collatz conjecture, parity word, affine operator, operation translation, correction term, upper-triangular matrix, finite-word closure, local atlas, 3n+1

---

# 1. Problem Setting

The traditional Collatz map is

$$
\operatorname{Col}(n)
=
\begin{cases}
n/2,&n\text{ even},\\
3n+1,&n\text{ odd}.
\end{cases}
$$

This paper adopts the equivalent modified form:

$$
\boxed{
T(n)
=
\begin{cases}
n/2,&n\equiv0\pmod2,\\[2mm]
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
}
$$

This form is adopted because an odd number mapped by $3n+1$ is necessarily even; thus, the inevitable subsequent division by 2 can be merged into the odd branch.

Define:

$$
D(x)=\frac{x}{2},
$$

$$
U(x)=\frac{3x+1}{2}.
$$

---

# 2. Formal Words and Admissible Itineraries Must Be Separated

Let:

$$
\Sigma=\{D,U\}.
$$

Finite word:

$$
w=\sigma_1\cdots\sigma_k
\in\Sigma^k.
$$

This paper adopts the convention that words are executed from left to right:

$$
\sigma_1
\to
\sigma_2
\to\cdots\to
\sigma_k.
$$

Thus, the formal operator is:

$$
F_w
=
\sigma_k\circ\cdots\circ\sigma_2\circ\sigma_1.
$$

This operator can be formally evaluated for all:

$$
x\in\mathbb Q
$$

However, for a genuine Collatz trajectory,

it must satisfy:

$$
\sigma_j
=
\begin{cases}
D,&T^{j-1}(n)\text{ even},\\
U,&T^{j-1}(n)\text{ odd}.
\end{cases}
$$

for $w$ to be called **admissible** for $n$.

---

# 3. Admissible Domain

Define:

$$
\boxed{
\Omega_w
=
\{
n\in\mathbb Z_{>0}:
\text{the first }|w|
\text{ parity branches of }n
\text{ equal }w
\}.
}
$$

If:

$$
n\in\Omega_w,
$$

then:

$$
\boxed{
T^{|w|}(n)=F_w(n).
}
$$

If:

$$
n\notin\Omega_w,
$$

then $F_w(n)$ remains a valid rational expression,

but it does not represent the actual Collatz itinerary of $n$.

This is precisely what Operation Translation refers to as:

$$
\boxed{
\text{formal transform legality}
\neq
\text{dynamical-domain legality}.
}
$$

---

# 4. Finite-Word Affine Closure Theorem

## Theorem 4.1

For any:

$$
w\in\{D,U\}^k,
$$

let:

$$
u(w)
=
\#\{j:\sigma_j=U\}.
$$

Then there exists a unique:

$$
b_w\in\mathbb Z_{\ge0}
$$

such that:

$$
\boxed{
F_w(x)
=
\frac{3^{u(w)}x+b_w}{2^k}
}
$$

holds for all $x\in\mathbb Q$.

---

# 5. Proof by Induction

For the empty word:

$$
\varepsilon,
$$

we have:

$$
F_\varepsilon(x)=x.
$$

Thus:

$$
k=0,\qquad u=0,\qquad b_\varepsilon=0.
$$

Assume for a word $w$ of length $k$:

$$
F_w(x)
=
\frac{3^ux+b_w}{2^k}.
$$

---

## 5.1 Appending a $D$

$$
F_{wD}(x)
=
D(F_w(x))
$$

$$
=
\frac{3^ux+b_w}{2^{k+1}}.
$$

Thus:

$$
\boxed{
u(wD)=u(w),
}
$$

$$
\boxed{
b_{wD}=b_w.
}
$$

---

## 5.2 Appending a $U$

$$
F_{wU}(x)
=
U(F_w(x))
$$

$$
=
\frac{
3\frac{3^ux+b_w}{2^k}+1
}{2}
$$

$$
=
\frac{
3^{u+1}x+3b_w+2^k
}{
2^{k+1}
}.
$$

Therefore:

$$
\boxed{
u(wU)=u(w)+1,
}
$$

$$
\boxed{
b_{wU}=3b_w+2^k.
}
$$

This completes the induction.

---

# 6. Correction Recurrence

Thus, $b_w$ can be viewed as a state variable on a word:

Initial state:

$$
b_\varepsilon=0.
$$

Reading a symbol:

$$
D:
\quad
b\mapsto b,
$$

$$
\boxed{
U:
\quad
b\mapsto3b+2^j,
}
$$

where $j$ is the length of the word before appending the symbol.

This is not a numerical error.

It is an exact structural correction.

---

# 7. Closed Form of the Order Correction

Suppose:

$$
U
$$

appears at positions:

$$
1\le j_1<j_2<\cdots<j_u\le k.
$$

The $t$-th $U$ generates upon appending:

$$
2^{j_t-1}.
$$

Subsequently, each time another $U$ is encountered,

the existing correction is multiplied by 3.

There are a total of:

$$
u-t
$$

$U$'s after the $t$-th $U$.

Therefore:

$$
\boxed{
b_w
=
\sum_{t=1}^{u}
2^{j_t-1}3^{u-t}.
}
$$

---

# 8. Example 1: $UD$

First:

$$
U(x)=\frac{3x+1}{2}.
$$

Then $D$:

$$
F_{UD}(x)
=
\frac{3x+1}{4}.
$$

Thus:

$$
k=2,
\qquad
u=1,
\qquad
b_{UD}=1.
$$

Closed form:

$$
j_1=1
$$

gives:

$$
b=2^0=1.
$$

---

# 9. Example 2: $DU$

First:

$$
D(x)=\frac x2.
$$

Then $U$:

$$
F_{DU}(x)
=
\frac{3x+2}{4}.
$$

Thus:

$$
b_{DU}=2.
$$

The two words:

$$
UD
$$

and:

$$
DU
$$

have the same:

$$
k=2,\qquad u=1,
$$

and thus the same principal slope:

$$
\frac34.
$$

But:

$$
\boxed{
b_{UD}\neq b_{DU}.
}
$$

Therefore:

$$
\boxed{
\text{branch counts do not determine the full operator}.
}
$$

---

# 10. Count/Order Decomposition

This paper defines:

## Multiplicative Skeleton

$$
\boxed{
S(w)
=
(k,u(w)).
}
$$

It determines:

$$
\boxed{
\lambda_w
=
\frac{3^{u(w)}}{2^k}.
}
$$

## Order Correction

$$
\boxed{
C(w)=b_w.
}
$$

Therefore:

$$
\boxed{
F_w(x)
=
\lambda_wx+\frac{b_w}{2^k}.
}
$$

This can be read as:

$$
\boxed{
\text{finite dynamics}
=
\text{order-insensitive multiplicative skeleton}
+
\text{order-sensitive affine correction}.
}
$$

---

# 11. Why Is This Not an Ordinary "Linearization"?

Because:

$$
F_w(x)
$$

is already affine itself.

What this paper actually does is:

$$
\boxed{
\text{many branch-dependent steps}
\longrightarrow
\text{one exact affine operator}.
}
$$

Original process:

$$
x
\to\sigma_1(x)
\to\sigma_2\sigma_1(x)
\to\cdots
\to F_w(x).
$$

After translation:

$$
\boxed{
x
\longmapsto
\frac{3^ux+b_w}{2^k}.
}
$$

This is the operator compression of finite temporal composition.

---

# 12. Triplet Representation

Define:

$$
\boxed{
\Omega(w)
=
(k_w,u_w,b_w).
}
$$

If we first execute:

$$
w
$$

then execute:

$$
v,
$$

then:

$$
F_{wv}
=
F_v\circ F_w.
$$

Let:

$$
F_w(x)
=
\frac{3^{u_w}x+b_w}{2^{k_w}},
$$

$$
F_v(x)
=
\frac{3^{u_v}x+b_v}{2^{k_v}}.
$$

Substituting:

$$
F_v(F_w(x))
=
\frac{
3^{u_v}
\left(
\frac{3^{u_w}x+b_w}{2^{k_w}}
\right)
+b_v
}{
2^{k_v}
}.
$$

Simplifying:

$$
=
\frac{
3^{u_v+u_w}x
+
3^{u_v}b_w
+
2^{k_w}b_v
}{
2^{k_v+k_w}
}.
$$

Therefore:

$$
\boxed{
\Omega(wv)
=
\left(
k_w+k_v,\,
u_w+u_v,\,
3^{u_v}b_w+2^{k_w}b_v
\right).
}
$$

---

# 13. Semidirect Product Structure

The first two components:

$$
k_w+k_v,
$$

$$
u_w+u_v
$$

undergo only ordinary addition.

The third component:

$$
3^{u_v}b_w+2^{k_w}b_v
$$

is acted upon by the first two components.

Thus, this structure can be viewed as a kind of:

$$
\boxed{
\text{additive count monoid acting on an affine correction coordinate}.
}
$$

This is the operation-translation algebra of finite parity words.

---

# 14. Concatenation Order Defect

Swapping the execution order of $w$ and $v$.

We have:

$$
b_{wv}
=
3^{u_v}b_w+2^{k_w}b_v,
$$

while:

$$
b_{vw}
=
3^{u_w}b_v+2^{k_v}b_w.
$$

Thus:

$$
\boxed{
b_{wv}-b_{vw}
=
b_w(3^{u_v}-2^{k_v})
-
b_v(3^{u_w}-2^{k_w}).
}
$$

This is the exact word-order defect.

Note that:

$$
k_w+k_v
$$

and:

$$
u_w+u_v
$$

remain completely unchanged.

Therefore, in the scalar Collatz finite-word algebra:

$$
\boxed{
\text{noncommutativity is confined to the affine correction coordinate}.
}
$$

This phenomenon will be contrasted with matrix/noncommutative algebras in Paper 08; in a truly noncommutative multiplier, order dependence enters the leading linear part and no longer resides solely in the correction.

---

# 15. Upper-Triangular Matrix Representation

Mapping:

$$
F(x)=\frac{Ax+B}{D}
$$

to:

$$
M(F)
=
\begin{pmatrix}
A&B\\
0&D
\end{pmatrix}.
$$

Its action is:

$$
x
\mapsto
\frac{Ax+B}{D}.
$$

For the Collatz branches:

$$
\boxed{
M_D
=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
}
$$

$$
\boxed{
M_U
=
\begin{pmatrix}
3&1\\
0&2
\end{pmatrix}.
}
$$

---

# 16. Word Matrix

If:

$$
w=\sigma_1\cdots\sigma_k,
$$

then:

$$
M_w
=
M_{\sigma_k}\cdots M_{\sigma_1}.
$$

By affine closure:

$$
\boxed{
M_w
=
\begin{pmatrix}
3^{u(w)}&b_w\\
0&2^k
\end{pmatrix}.
}
$$

Therefore:

$$
\boxed{
\text{word concatenation}
\longrightarrow
\text{matrix multiplication}.
}
$$

---

# 17. Significance of the Matrix Representation

This representation separates three types of information:

Top-left:

$$
3^u
$$

represents the odd-branch multiplicative accumulation.

Bottom-right:

$$
2^k
$$

represents the total binary division depth.

Top-right:

$$
b_w
$$

represents the accumulated correction left by all $+1$ injections after subsequent branch scaling.

Therefore:

$$
\boxed{
M_w
=
\begin{pmatrix}
\text{odd multiplier}&\text{order correction}\\
0&\text{division scale}
\end{pmatrix}.
}
$$

---

# 18. A Physical Understanding of the Correction is Not Necessary

Intuitively, one could say:

Each $U$ injects a:

$$
+1
$$

term.

However, $+1$'s injected at different times,

will be amplified by subsequent:

$$
3
$$

multipliers a different number of times.

This is exactly why:

$$
2^{j_t-1}3^{u-t}.
$$

appears.

Nevertheless, this paper treats it solely as an exact algebraic result,

without assigning it any additional physical ontology.

---

# 19. Correction Range for Fixed $(k,u)$

For fixed:

$$
k,\qquad u,
$$

different words only change:

$$
j_1,\ldots,j_u.
$$

From:

$$
b_w
=
\sum_t2^{j_t-1}3^{u-t},
$$

we can study the extrema of the order correction.

---

# 20. Adjacent Swap Lemma

Consider adjacent symbols in a word:

$$
UD
$$

and:

$$
DU.
$$

Under the same prefix state $x$:

$$
UD(x)
=
\frac{3x+1}{4},
$$

$$
DU(x)
=
\frac{3x+2}{4}.
$$

Thus:

$$
\boxed{
DU(x)-UD(x)=\frac14.
}
$$

If followed by any identical suffix,

their difference is still multiplied by a positive coefficient.

Therefore, moving a $U$ to the right past a $D$

strictly increases the final correction $b_w$.

---

# 21. Order Extremal Theorem

Thus, for a fixed:

$$
(k,u),
$$

the minimum correction is achieved by placing all $U$'s on the far left:

$$
\boxed{
w_{\min}
=
U^uD^{k-u}.
}
$$

the maximum correction is achieved by placing all $U$'s on the far right:

$$
\boxed{
w_{\max}
=
D^{k-u}U^u.
}
$$

---

# 22. Minimum Correction

For:

$$
U^uD^{k-u},
$$

the positions of $U$ are:

$$
j_t=t.
$$

Thus:

$$
b_{\min}
=
\sum_{t=1}^u
2^{t-1}3^{u-t}.
$$

Using the finite geometric sum:

$$
\boxed{
b_{\min}
=
3^u-2^u.
}
$$

---

# 23. Maximum Correction

For:

$$
D^{k-u}U^u,
$$

the positions are:

$$
j_t=k-u+t.
$$

Thus:

$$
b_{\max}
=
\sum_{t=1}^u
2^{k-u+t-1}3^{u-t}.
$$

Factoring out:

$$
2^{k-u},
$$

we obtain:

$$
\boxed{
b_{\max}
=
2^{k-u}(3^u-2^u).
}
$$

Therefore:

$$
\boxed{
3^u-2^u
\le
b_w
\le
2^{k-u}(3^u-2^u).
}
$$

---

# 24. Boundary Cases

If:

$$
u=0,
$$

then:

$$
w=D^k,
$$

$$
b_w=0.
$$

The above formula also gives:

$$
3^0-2^0=0.
$$

If:

$$
u=k,
$$

then there is only:

$$
w=U^k,
$$

and the upper and lower bounds are identical:

$$
b_w=3^k-2^k.
$$

For example:

$$
U^3:
$$

$$
b=27-8=19.
$$

Therefore:

$$
F_{UUU}(x)
=
\frac{27x+19}{8}.
$$

---

# 25. Order Correction Width

The width of the correction range for a fixed $(k,u)$ is:

$$
W_{k,u}
=
b_{\max}-b_{\min}.
$$

Thus:

$$
\boxed{
W_{k,u}
=
(2^{k-u}-1)(3^u-2^u).
}
$$

This provides an exact measure of the order sensitivity of finite words.

When:

$$
k=u
$$

we have:

$$
W_{k,u}=0
$$

because there is only one permutation.

When both $D$ and $U$ are present,

typically:

$$
W_{k,u}>0.
$$

---

# 26. Logarithmic Form

If:

$$
x>0,
$$

and:

$$
F_w(x)>0,
$$

then:

$$
\log F_w(x)
=
\log x
+
u\log3
-
k\log2
+
\log\left(
1+\frac{b_w}{3^ux}
\right).
$$

Thus:

$$
\boxed{
\Delta_w L
=
u\log3-k\log2
+
C_w(x),
}
$$

where:

$$
\boxed{
C_w(x)
=
\log\left(
1+\frac{b_w}{3^ux}
\right).
}
$$

---

# 27. Additive Core and Correction

Therefore, the corrected linearization of Series A:

$$
T\mu=\nu T+C
$$

finds a very standard instantiation in finite Collatz words.

Additive core:

$$
\boxed{
u\log3-k\log2.
}
$$

Order-sensitive correction:

$$
\boxed{
C_w(x).
}
$$

And:

$$
C_w(x)\to0
$$

as:

$$
x\to\infty.
$$

Thus, for a fixed word:

$$
\boxed{
\text{asymptotic drift is count-controlled}.
}
$$

This conclusion will be used in Paper 05 to establish the contraction boundary.

---

# 28. But Log is Not a Necessary Form for Proof Certificates

Because the affine identity is already exact:

$$
F_w(n)
=
\frac{3^un+b_w}{2^k}.
$$

descent can be determined directly:

$$
3^un+b_w<2^kn.
$$

Therefore, subsequent finite verification should prioritize exact integer inequalities.

Log-space is suitable for:

- interpretation;
- ordering;
- asymptotic classification;
- heuristic search.

But exact certificates do not need to rely on floating-point logarithms.

---

# 29. Relationship with Existing Parity-Vector Research

The one-to-one correspondence between Collatz parity sequences / parity vectors and $2$-adic integers is an important part of existing research.

Therefore, this paper does not claim that:

- parity vectors are a new discovery;
- the algebraic expression of finite itineraries is completely unknown;
- $2$-adic coding is proposed for the first time in this paper.

The role of this paper is to reorganize finite-word dynamics in the language of Operation Translation as:

$$
\boxed{
\text{formal word}
\to
\text{affine operator}
\to
\text{multiplicative skeleton}
+
\text{order correction}.
}
$$

and to explicitly prepare for the subsequent local atlas.

---

# 30. Why Can't Paper 02 Directly Discuss Residue Bijection Yet?

We already know that for:

$$
F_w(n)
$$

to represent the genuine:

$$
T^k(n),
$$

it must be that:

$$
n\in\Omega_w.
$$

But this paper has not yet proven what:

$$
\Omega_w
$$

exactly looks like.

Paper 03 will prove:

$$
\boxed{
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}
}
$$

where $r_w$ is the canonical representative modulo $2^k$ such that $0\le r_w<2^k$,

and:

$$
\boxed{
r_w
\equiv
-b_w3^{-u}
\pmod{2^k}.
}
$$

Only then will the formal affine operator be upgraded to a Local Affine Atlas.

---

# 31. What Does This Paper Not Prove?

This paper does not prove:

$$
\forall n,\quad T^j(n)=1
$$

for some $j$.

It does not prove that all infinite parity sequences eventually contain a descending prefix.

It does not prove that all finite words are admissible for all $n$.

It does not use:

$$
u/k
$$

to deduce universal convergence from its average.

This paper only proves:

$$
\boxed{
\text{fixed finite word}
\Rightarrow
\text{exact finite affine operator}.
}
$$

---

# 32. Summary of Core Theorems

## Theorem A — Finite-Word Affine Closure

$$
\boxed{
F_w(x)
=
\frac{3^{u(w)}x+b_w}{2^{|w|}}.
}
$$

## Theorem B — Correction Recurrence

$$
\boxed{
b_{wD}=b_w,
\qquad
b_{wU}=3b_w+2^{|w|}.
}
$$

## Theorem C — Closed Form

$$
\boxed{
b_w
=
\sum_{t=1}^{u}
2^{j_t-1}3^{u-t}.
}
$$

## Theorem D — Concatenation

$$
\boxed{
b_{wv}
=
3^{u(v)}b_w+2^{|w|}b_v.
}
$$

## Theorem E — Matrix Representation

$$
\boxed{
M_w
=
\begin{pmatrix}
3^{u(w)}&b_w\\
0&2^{|w|}
\end{pmatrix}.
}
$$

## Theorem F — Order Extremes

$$
\boxed{
3^u-2^u
\le b_w
\le
2^{k-u}(3^u-2^u).
}
$$

---

# 33. New Research Paradigm

At this point, a segment of Collatz dynamics of length $k$ no longer needs to be viewed as:

$$
k
$$

if/else operations.

It can be compressed into:

$$
\boxed{
(k,u,b_w).
}
$$

or:

$$
\boxed{
\begin{pmatrix}
3^u&b_w\\
0&2^k
\end{pmatrix}.
}
$$

Therefore:

$$
\boxed{
\text{temporal branch sequence}
\longrightarrow
\text{finite algebraic operator}.
}
$$

This is the algebraic kernel of the Collatz Local Affine Atlas.

---

# 34. Connection with Series A

Series A Paper 01:

$$
T(\mu(x,y))
=
\nu(Tx,Ty)+C_T(x,y).
$$

Series A Paper 03:

$$
\text{Linear Core}+\text{Correction}.
$$

Series A Paper 05:

$$
\text{Local Chart / Atlas}.
$$

This paper transplants these three into the Collatz context:

$$
\boxed{
\text{finite itinerary}
\to
\text{affine core}
+
\text{word-order correction}.
}
$$

The next paper will then precisely identify:

$$
\Omega_w
$$

as a residue cylinder.

---

# 35. Conclusion

The single-step rule of the Collatz conjecture is extremely simple,

but the branch composition of any finite word does not need to be preserved step-by-step.

It possesses an exact affine closure:

$$
\boxed{
F_w(x)
=
\frac{3^ux+b_w}{2^k}.
}
$$

where:

$$
\boxed{
(k,u)
}
$$

preserves the branch-count skeleton,

while:

$$
\boxed{
b_w
}
$$

preserves the branch order.

Therefore:

$$
\boxed{
\text{counts determine slope;}
}
$$

$$
\boxed{
\text{order determines offset.}
}
$$

This is the most core structural conclusion of this paper.

It also illustrates a larger point:

The finite local arithmetic of Collatz can actually be completely compressed into a low-dimensional algebraic state.

The true difficulty no longer needs to be described as:

> Every step of $3n+1$ and division by 2 is too chaotic.

A more precise description is:

> For a fixed finite itinerary, the arithmetic is fully compressible; the unresolved problem lies in exactly which itineraries each starting point extends along infinitely, and how these local operators are globally stitched together.

Paper 03 will push this conclusion one step further:

$$
\boxed{
\text{parity word}
\longleftrightarrow
\text{unique residue cylinder modulo }2^k,
}
$$

and prove that under appropriate source / destination charts:

$$
\boxed{
\psi_w\circ T^k\circ\phi_w^{-1}
=
\operatorname{id}.
}
$$

which is the local reduction to the identity map of Collatz.

---

# References

1. Olivier Rozier, *Parity sequences of the 3x+1 map on the 2-adic integers and Euclidean embedding*, arXiv:1805.00133.
2. Olivier Rozier, Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948.
3. Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886.
4. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), arXiv:1909.03562.
5. David Applegate, Jeffrey C. Lagarias, *The 3x+1 Semigroup*, Journal of Number Theory 117 (2006), arXiv:math/0411140.
6. Tristan Stérin, Damien Woods, *The Collatz process embeds a base conversion algorithm*, arXiv:2007.06979.
7. Collatz Operation Translation Series — Paper 01, *Reclassification and Correction of Existing Research on the Collatz Conjecture*.

---

## Next Paper

**Paper 03 — *Parity Word, Residue Cylinder, and Local Identity-ization***

Core tasks:

1. Prove that each finite parity word corresponds to a unique residue $r_w\bmod2^k$;
2. Prove
   $$
   r_w\equiv-b_w3^{-u}\pmod{2^k};
   $$
3. Establish the exact cylinder map:
   $$
   T^k(r_w+2^ka)=m_w+3^ua;
   $$
4. Define source / destination charts;
5. Prove:
   $$
   \psi_wT^k\phi_w^{-1}=\operatorname{id};
   $$
6. Formally establish the Collatz Local Affine Atlas.