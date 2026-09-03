# Generalized $mx+r$ Systems and Residue-Class Operation Translation
## — From the Collatz Special Case to Commutative Scalar Affine Dynamics, Phase Boundaries, and Generalized Local Atlases

**English Title:** *Generalized $mx+r$ Systems and Residue-Class Operation Translation: Affine Word Closure, Local Atlases, and a Cylinder Phase Boundary*

**Author:** Neo.K  
**Institution:** EveMiss Technology Co., Ltd. (EveMissLab)  
**Series:** Collatz Operation Translation Series — Paper 07  
**Version:** v0.1.1  
**Date:** 2026-08-10  
**Revision Date:** 2026-08-14

---

## Abstract

The previous six papers utilized the modified Collatz map

$$
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[2mm]
(3n+1)/2,&n\text{ odd}
\end{cases}
$$

to establish finite-word affine closure, parity-word/residue-cylinder correspondence, local identityization, bidirectional $2^k\leftrightarrow3^u$ residue-class translation, finite-word contraction boundaries, and a valuation language.

This paper removes the Collatz-specific $3,1$ and examines the parity-preserving generalized system defined by positive odd integer parameters

$$
m\ge1,\qquad r\ge1,\qquad m,r\text{ odd}
$$

which is

$$
\boxed{
T_{m,r}(n)
=
\begin{cases}
\dfrac n2,&n\equiv0\pmod2,\\[2mm]
\dfrac{mn+r}{2},&n\equiv1\pmod2.
\end{cases}
}
$$

Let

$$
D(x)=\frac x2,
\qquad
U_{m,r}(x)=\frac{mx+r}{2}.
$$

This paper proves that for any finite parity word $w\in\{D,U\}^k$ of length $k$, if $u=u(w)$, the formal composition always possesses an exact affine closure:

$$
\boxed{
F_w^{(m,r)}(x)
=
\frac{m^u x+b_w^{(m,r)}}{2^k},
}
$$

where

$$
\boxed{
b_w^{(m,r)}
=
r\sum_{t=1}^{u}
2^{j_t-1}m^{u-t},
}
$$

and $j_t$ is the position of the $t$-th $U$.

Thus, the generalized system preserves:

$$
\boxed{
\text{branch counts determine the multiplicative skeleton;}
}
$$

$$
\boxed{
\text{branch order determines the affine correction.}
}
$$

More importantly, since $m$ is odd,

$$
\gcd(m^u,2^k)=1,
$$

therefore each finite parity word still corresponds to a unique residue cylinder modulo $2^k$:

$$
\boxed{
\Omega_w^{(m,r)}
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0},
}
$$

and

$$
\boxed{
r_w
\equiv
-b_w^{(m,r)}m^{-u}
\pmod{2^k}.
}
$$

If

$$
s_w
=
F_w^{(m,r)}(r_w),
$$

then:

$$
\boxed{
T_{m,r}^k(r_w+2^ka)
=
s_w+m^ua.
}
$$

Thus, the source $2^k$-cylinder is exactly mapped to the target $m^u$-progression:

$$
\boxed{
r_w+2^k\mathbb Z
\longleftrightarrow
s_w+m^u\mathbb Z,
}
$$

and is once again identityized in the source/target quotient coordinates:

$$
\boxed{
\psi_w
\circ
T_{m,r}^k
\circ
\phi_w^{-1}
=
\operatorname{id}.
}
$$

This proves that the core local-affine/identity structure of the previous six papers is not unique to $3x+1$, but belongs to a broader odd-$m$, odd-$r$ residue-class affine family.

For fixed $(k,u)$, when $r>0$, the order correction has exact bounds:

$$
\boxed{
r\,\frac{m^u-2^u}{m-2}
\le
b_w^{(m,r)}
\le
r\,2^{k-u}\frac{m^u-2^u}{m-2}
}
$$

($m\neq2$, and in this paper $m$ is odd). The minimum value is attained by

$$
U^uD^{k-u}
$$

and the maximum value is attained by

$$
D^{k-u}U^u
$$

The finite-word drift is completely determined by:

$$
\boxed{
m^u\lessgtr2^k
}
$$

which dictates its skeleton side. If

$$
m^u<2^k,
$$

there exists a finite threshold such that the entire chart eventually undergoes strict descent; if

$$
m^u>2^k,
$$

then the entire positive admissible cylinder undergoes strict expansion on this $k$-block.

For $m>1$, define:

$$
\boxed{
\alpha_m
=
\frac{\ln2}{\ln m}.
}
$$

Then the contracting condition is:

$$
\boxed{
\frac uk<\alpha_m.
}
$$

Since an odd $m>1$ cannot be a power of 2, $\alpha_m$ is irrational, so the length-$k$ contracting cylinder count is:

$$
\boxed{
A_k(m)
=
\sum_{u=0}^{\lfloor\alpha_m k\rfloor}
\binom ku.
}
$$

with the proportion:

$$
\boxed{
P_k(m)
=
\frac{A_k(m)}{2^k}.
}
$$

This leads to a generalized cylinder phase theorem:

- $m=1$: All nonempty finite words lie on the contracting-skeleton side;
- $m=3$: $\alpha_3>1/2$, hence
  $$
  \boxed{P_k(3)\to1;}
  $$
- odd $m\ge5$: $\alpha_m<1/2$, hence
  $$
  \boxed{P_k(m)\to0.}
  $$

The critical value in the sense of a continuous parameter is exactly:

$$
\boxed{
m_c=4.
}
$$

This criticality arises from:

$$
\frac{\ln2}{\ln m}
=
\frac12
\iff
m=4.
$$

It is worth noting that the almost-all theorem by Gonçalves–Greenfeld–Madrid for more general $p,q,r$ Collatz-like maps uses the condition:

$$
q<p^{p/(p-1)}.
$$

When $p=2$, this is exactly:

$$
\boxed{
q<4.
}
$$

Therefore, the parity-family phase boundary obtained in this paper via finite-word/residue-cylinder combinatorial counting yields the same critical constant as the existing, deeper almost-all analytic theory on the $p=2$ cross-section. This paper does not consider the two to be the same theorem: the former is a deterministic finite chart density, while the latter is a logarithmic-density theorem of actual orbits; their agreement should be understood as an important structural cross-validation.

This paper also proves that the additive parameter $r$ does not alter the asymptotic skeleton boundary:

$$
m^u\lessgtr2^k
$$

depends only on $m,k,u$. $r$ linearly scales the correction, thus primarily controlling the finite-size threshold, fixed-point positions, and local orbit geometry, without shifting the cylinder-density phase boundary.

Finally, this paper defines this class of structures as the **Residue-Class Operation Translation (RCOT) parity kernel**: as long as the branch maps are commutative scalar affine operators, and the odd multiplier is a unit with respect to the binary denominator, then finite-word closure, unique residue charts, local identityization, exact recovery, and count/order decomposition all hold.

The next paper will further expand the algebra of the coefficients layer by layer to commutative rings with zero divisors, unordered fields, matrices/noncommutative algebras, Möbius transformations, and higher-degree polynomial dynamics, in order to determine the true algebraic domain of RCOT and its first structural breaking point.

**Keywords:** generalized Collatz, $mx+r$, residue-class affine map, operation translation, local affine atlas, phase boundary, parity word, binomial cylinder law, exact recovery

---

# 1. Removing $3,1$ from the Collatz Special Case

Collatz modified branches:

$$
D(x)=\frac x2,
\qquad
U(x)=\frac{3x+1}{2}.
$$

The local algebraic conditions actually utilized here are:

1. $D,U$ are both affine;
2. The multiplier of the odd branch is odd;
3. The translation term is also odd, mapping odd inputs to integers;
4. The denominator is 2;
5. Scalar coefficients commute.

Therefore, consider:

$$
\boxed{
D(x)=\frac x2,
}
$$

$$
\boxed{
U_{m,r}(x)=\frac{mx+r}{2},
}
$$

where:

$$
m,r\in2\mathbb Z+1,
\qquad
m,r>0.
$$

---

# 2. Why Must $m,r$ Be Odd?

If:

$$
n\text{ odd},
$$

and:

$$
m,r\text{ odd},
$$

then:

$$
mn+r
=
\text{odd}+\text{odd}
=
\text{even}.
$$

So:

$$
U_{m,r}(n)
=
\frac{mn+r}{2}
\in\mathbb Z.
$$

Thus:

$$
\boxed{
\text{odd branch legality is automatic on odd inputs}.
}
$$

---

# 3. Formal Word

Let:

$$
w=\sigma_1\cdots\sigma_k,
\qquad
\sigma_i\in\{D,U\}.
$$

Let:

$$
u(w)=u
$$

be the number of $U$'s.

Formal composition:

$$
F_w^{(m,r)}
=
\sigma_k\circ\cdots\circ\sigma_1.
$$

As with Collatz:

$$
F_w^{(m,r)}
$$

can be formally computed over $\mathbb Q$;

the true dynamics still require branch admissibility.

---

# 4. Generalized Finite-Word Affine Closure

## Theorem 4.1

For any:

$$
w\in\{D,U\}^k,
$$

there exists a unique:

$$
b_w^{(m,r)}\in\mathbb Z_{\ge0}
$$

such that:

$$
\boxed{
F_w^{(m,r)}(x)
=
\frac{m^u x+b_w^{(m,r)}}{2^k}.
}
$$

---

# 5. Correction Recurrence

Empty word:

$$
b_\varepsilon=0.
$$

If appending $D$:

$$
\boxed{
b_{wD}=b_w.
}
$$

If appending $U$:

$$
U\left(
\frac{m^u x+b_w}{2^k}
\right)
=
\frac{
m^{u+1}x
+
m b_w
+
r2^k
}{
2^{k+1}
}.
$$

So:

$$
\boxed{
b_{wU}
=
m b_w+r2^k.
}
$$

---

# 6. Closed Form

If $U$ appears at:

$$
1\le j_1<\cdots<j_u\le k,
$$

then the $t$-th $U$ injects:

$$
r2^{j_t-1},
$$

and there remain:

$$
u-t
$$

$U$'s after it, each multiplying by $m$ again.

Thus:

$$
\boxed{
b_w^{(m,r)}
=
r\sum_{t=1}^{u}
2^{j_t-1}m^{u-t}.
}
$$

Collatz:

$$
(m,r)=(3,1)
$$

immediately recovers Paper 02.

---

# 7. Count/Order Decomposition survives

Fixing:

$$
k,u,
$$

the leading multiplier is always:

$$
\boxed{
\lambda_w
=
\frac{m^u}{2^k}.
}
$$

independent of the arrangement of $U,D$.

All order information enters:

$$
\boxed{
b_w^{(m,r)}.
}
$$

So:

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

This is not a $3x+1$ special case.

---

# 8. Matrix Representation

Define:

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
m&r\\
0&2
\end{pmatrix}.
}
$$

Then:

$$
\boxed{
M_w
=
\begin{pmatrix}
m^u&b_w^{(m,r)}\\
0&2^k
\end{pmatrix}.
}
$$

finite-word composition still translates to upper-triangular matrix multiplication.

---

# 9. Concatenation Law

If $w$ is executed first, followed by $v$, then:

$$
\boxed{
b_{wv}
=
m^{u(v)}b_w
+
2^{|w|}b_v.
}
$$

So:

$$
\Omega(w)
=
(k,u,b)
$$

has the generalized composition:

$$
\boxed{
(k_w,u_w,b_w)
\circ
(k_v,u_v,b_v)
}
$$

which still possesses a semidirect-type structure.

---

# 10. Residue Cylinder Remains Unique

The true key is not $m=3$.

But rather:

$$
\boxed{
m\text{ odd}.
}
$$

So:

$$
\gcd(m^u,2^k)=1.
$$

Thus:

$$
m^u
$$

in:

$$
\mathbb Z/2^k\mathbb Z
$$

is a unit.

---

# 11. Closed Residue Formula

If $w$ is admissible,

it must be that:

$$
m^u n+b_w
\equiv0
\pmod{2^k}.
$$

So the unique:

$$
\boxed{
r_w
\equiv
-b_wm^{-u}
\pmod{2^k}.
}
$$

---

# 12. Word–Residue Bijection survives

More strictly, using induction as in Paper 03:

Assume:

$$
n=r_w+2^ka.
$$

Then:

$$
T_{m,r}^k(n)
=
s_w+m^ua.
$$

Since:

$$
m^u
$$

is odd,

So:

$$
T_{m,r}^k(n)\pmod2
=
s_w+a\pmod2.
$$

Thus the next $D/U$ branch is once again determined solely by:

$$
a\bmod2
$$

Each parent cylinder uniquely splits into two modulo $2^{k+1}$ child cylinders.

So:

$$
\boxed{
\{D,U\}^k
\longleftrightarrow
\mathbb Z/2^k\mathbb Z
}
$$

still holds.

---

# 13. Generalized Local Atlas

Define:

$$
\Omega_w^{(m,r)}
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}.
$$

Let:

$$
s_w
=
F_w^{(m,r)}(r_w).
$$

Then:

$$
\boxed{
T_{m,r}^k(r_w+2^ka)
=
s_w+m^ua.
}
$$

So:

$$
\boxed{
r_w+2^k\mathbb Z
\longleftrightarrow
s_w+m^u\mathbb Z.
}
$$

---

# 14. Generalized Identityization

source chart:

$$
\phi_w(n)
=
\frac{n-r_w}{2^k}.
$$

target chart:

$$
\psi_w(y)
=
\frac{y-s_w}{m^u}.
$$

Then:

$$
\boxed{
\psi_w
\circ
T_{m,r}^k
\circ
\phi_w^{-1}
=
\operatorname{id}.
}
$$

So:

$$
\boxed{
\text{local identity trivialization survives for all positive odd }m,r.
}
$$

---

# 15. Exact Recovery survives

If:

$$
y\equiv s_w\pmod{m^u},
$$

then:

$$
a=
\frac{y-s_w}{m^u}.
$$

So:

$$
\boxed{
n
=
r_w
+
2^k
\frac{y-s_w}{m^u}.
}
$$

Thus fixed chart transport remains lossless.

---

# 16. Fixed $(k,u)$ Order Extremes

For:

$$
r>0,
$$

swapping a $U$ to the right past a $D$:

$$
UD(x)
=
\frac{mx+r}{4},
$$

and:

$$
DU(x)
=
\frac{mx+2r}{4}.
$$

So:

$$
DU(x)-UD(x)
=
\frac r4>0.
$$

Thus moving $U$ right increases correction.

---

# 17. Minimum Correction

All $U$'s leftmost:

$$
U^uD^{k-u}.
$$

Its correction:

$$
b_{\min}
=
r
\sum_{t=1}^{u}
2^{t-1}m^{u-t}.
$$

Finite geometric sum:

$$
\boxed{
b_{\min}
=
r\frac{m^u-2^u}{m-2}.
}
$$

---

# 18. Maximum Correction

All $U$'s rightmost:

$$
D^{k-u}U^u.
$$

So:

$$
\boxed{
b_{\max}
=
r\,2^{k-u}
\frac{m^u-2^u}{m-2}.
}
$$

Thus:

$$
\boxed{
r\frac{m^u-2^u}{m-2}
\le
b_w
\le
r2^{k-u}\frac{m^u-2^u}{m-2}.
}
$$

---

# 19. $m=1$ Requires Separate Understanding

When:

$$
m=1,
$$

the formula:

$$
\frac{m^u-2^u}{m-2}
$$

can still be directly substituted:

$$
\frac{1-2^u}{-1}
=
2^u-1.
$$

So:

$$
b_{\min}
=
r(2^u-1).
$$

There is no singularity.

It is just that the skeleton here:

$$
\lambda_w=\frac1{2^k}
$$

is independent of $u$.

---

# 20. Exact Descent Criterion

From:

$$
T_{m,r}^k(n)
=
\frac{m^un+b_w}{2^k},
$$

we have:

$$
T_{m,r}^k(n)<n
$$

iff:

$$
\boxed{
b_w<(2^k-m^u)n.
}
$$

---

# 21. Contracting Skeleton

If:

$$
\boxed{
m^u<2^k,
}
$$

then there exists a finite threshold:

$$
\boxed{
\theta_w
=
\left\lfloor
\frac{b_w}{2^k-m^u}
\right\rfloor+1
}
$$

such that:

$$
n\ge\theta_w
$$

when:

$$
\boxed{
T_{m,r}^k(n)<n.
}
$$

---

# 22. Uniform Expansion

If:

$$
m^u>2^k,
$$

Since:

$$
b_w\ge0,
$$

for any positive admissible:

$$
n,
$$

we have:

$$
\boxed{
T_{m,r}^k(n)>n.
}
$$

Thus the generalized family still possesses a strict finite-word two-sided classification.

---

# 23. $r$ Does Not Shift the Skeleton Boundary

Note that:

$$
m^u\lessgtr2^k
$$

completely lacks:

$$
r.
$$

So:

$$
\boxed{
r
\text{ controls correction and finite thresholds, not the asymptotic skeleton side}.
}
$$

This is a very important parameter division of labor in the generalized family.

---

# 24. Generalized Critical Fraction

For:

$$
m>1,
$$

define:

$$
\boxed{
\alpha_m
=
\frac{\ln2}{\ln m}.
}
$$

Then:

$$
m^u<2^k
$$

iff:

$$
\boxed{
\frac uk<\alpha_m.
}
$$

---

# 25. Irrationality of $\alpha_m$

If odd:

$$
m>1
$$

and:

$$
\alpha_m=\frac pq
\in\mathbb Q,
$$

then:

$$
m^p=2^q.
$$

The left side is odd,

the right side is even,

a contradiction.

Thus:

$$
\boxed{
\alpha_m\notin\mathbb Q
}
$$

for all odd $m>1$.

So there are no nonempty neutral-slope words.

---

# 26. Generalized Binomial Cylinder Law

Among length-$k$ words,

the number containing exactly $u$ $U$'s is:

$$
\binom ku.
$$

So the contracting cylinder count is:

$$
\boxed{
A_k(m)
=
\sum_{u=0}^{\lfloor\alpha_mk\rfloor}
\binom ku.
}
$$

Proportion:

$$
\boxed{
P_k(m)
=
\frac{A_k(m)}{2^k}.
}
$$

---

# 27. $m=1$: Completely Contracting Skeleton

If:

$$
m=1,
$$

then for any nonempty word:

$$
1=m^u<2^k.
$$

So:

$$
\boxed{
P_k(1)=1
}
$$

for all:

$$
k\ge1.
$$

Note that this only refers to the finite-word skeleton.

Different $r$ can still cause finite corrections, cycles, or other global structures.

---

# 28. $m=3$: Collatz Regime

$$
\alpha_3
=
\frac{\ln2}{\ln3}
\approx0.63093
>
\frac12.
$$

Thus, by the law of large numbers for the binomial distribution:

$$
\boxed{
P_k(3)\to1.
}
$$

This is the Collatz cylinder law from Paper 05.

---

# 29. $m=5$

$$
\alpha_5
=
\frac{\ln2}{\ln5}
\approx0.43068
<
\frac12.
$$

So:

$$
\boxed{
P_k(5)\to0.
}
$$

That is, among length-$k$ words, the proportion of contracting-skeleton cylinders instead tends to zero.

---

# 30. odd $m\ge5$

For:

$$
m\ge5,
$$

we have:

$$
\ln m>\ln4=2\ln2.
$$

So:

$$
\frac{\ln2}{\ln m}
<
\frac12.
$$

Hence:

$$
\boxed{
P_k(m)\to0
}
$$

for all odd:

$$
m\ge5.
$$

---

# 31. Continuous Phase Boundary

Consider:

$$
\alpha_m=\frac12.
$$

Solving:

$$
\frac{\ln2}{\ln m}
=
\frac12.
$$

So:

$$
\ln m=2\ln2=\ln4.
$$

yields:

$$
\boxed{
m_c=4.
}
$$

Thus:

$$
\boxed{
m<4
\Rightarrow
\text{typical word lies on contracting side},
}
$$

$$
\boxed{
m>4
\Rightarrow
\text{typical word lies on expanding side}.
}
$$

In the odd integer family:

- $m=3$ lies in the contraction regime;
- The next, $m=5$, has already crossed into the expansion regime.

---

# 32. Why is $3$ Special?

This does not need to be mystified.

binomial center:

$$
u/k\approx1/2.
$$

Typical skeleton multiplier:

$$
\left(
\frac{\sqrt m}{2}
\right)^k.
$$

So:

$$
\boxed{
\frac{\sqrt m}{2}<1
\iff
m<4.
}
$$

For:

$$
m=3,
$$

typical factor:

$$
\frac{\sqrt3}{2}<1.
$$

For:

$$
m=5,
$$

$$
\frac{\sqrt5}{2}>1.
$$

So $3$ is exactly the last nontrivial value among odd multipliers that falls on the typical contraction side.

---

# 33. $r$ Only Alters Finite Geometry

For fixed:

$$
m,k,u,w,
$$

the correction:

$$
b_w^{(m,r)}
$$

is linear with respect to $r$:

$$
\boxed{
b_w^{(m,r)}
=
r\,b_w^{(m,1)}.
}
$$

So the threshold:

$$
\theta_w
$$

roughly moves linearly with $r$.

But:

$$
\alpha_m
$$

remains completely unchanged.

Thus:

$$
\boxed{
m=\text{phase parameter},
\qquad
r=\text{finite correction parameter}.
}
$$

---

# 34. Generalized Log Drift

For:

$$
n>0,
$$

$$
T_{m,r}^k(n)
=
\frac{m^un+b_w}{2^k}.
$$

Taking the log:

$$
\boxed{
\ln\frac{T_{m,r}^k(n)}{n}
=
u\ln m
-
k\ln2
+
\ln\left(
1+\frac{b_w}{m^un}
\right).
}
$$

So:

$$
\boxed{
\text{additive core}=u\ln m-k\ln2,
}
$$

$$
\boxed{
\text{correction}
=
\ln\left(
1+\frac{b_w}{m^un}
\right).
}
$$

The corrected additivization of Series A still holds completely in the generalized Collatz family.

---

# 35. Accelerated $mx+r$ Map

For odd $n$, we can define:

$$
\boxed{
S_{m,r}(n)
=
\frac{mn+r}
{2^{v_2(mn+r)}}.
}
$$

Since $m,r,n$ are all odd,

the numerator is even.

Thus the generalized valuation language also naturally exists:

$$
\kappa_i
=
v_2(mn_{i-1}+r).
$$

---

# 36. Generalized Valuation Skeleton

After $q$ odd-to-odd cycles,

the leading multiplier becomes:

$$
\boxed{
\frac{m^q}{2^K}.
}
$$

So the valuation boundary is:

$$
\boxed{
K/q>\log_2 m.
}
$$

This is a direct generalization of Paper 06:

$$
K/q>\log_2 3
$$

---

# 37. One-Step Valuation Density Still Possesses Geometric Structure

Since an odd $m$ in:

$$
\mathbb Z/2^{j+1}\mathbb Z
$$

is a unit.

Requiring:

$$
v_2(mn+r)=j
$$

is equivalent to a unique odd residue congruence modulo:

$$
2^{j+1}.
$$

So in the odd residue classes, we still have:

$$
\boxed{
\delta(\kappa=j)=2^{-j}.
}
$$

Thus the one-step residue mean:

$$
\boxed{
\mathbb E_{\mathrm{res}}\kappa=2
}
$$

is independent of $m,r$, as long as both are odd.

---

# 38. Hence the Generalized Skeleton Mean

one-step accelerated skeleton:

$$
\ln m-\kappa\ln2.
$$

residue ensemble mean:

$$
\boxed{
\ln m-2\ln2
=
\ln\frac m4.
}
$$

So the average skeleton sign also flips at:

$$
\boxed{
m=4
}
$$

This is completely consistent with the binomial cylinder phase boundary.

---

# 39. Two Different Derivations Yield the Same Criticality

### Finite parity-word combinatorics:

$$
u/k\approx1/2
$$

leads to:

$$
\frac{\sqrt m}{2}\lessgtr1.
$$

### Accelerated valuation residue mean:

$$
\mathbb E\kappa=2
$$

leads to:

$$
\frac m4\lessgtr1.
$$

Both yield:

$$
\boxed{
m_c=4.
}
$$

This is an internal cross-validation.

---

# 40. Intersection with More General $p,q,r$ Literature

Gonçalves–Greenfeld–Madrid studied a class of more general Collatz-like maps:

- divide by $p$ when divisible by $p$;
- use $qN+r(j)$ for other residue classes;
- then study their Syracuse acceleration.

One of the important conditions for their almost-all theorem is:

$$
\boxed{
q<p^{p/(p-1)}.
}
$$

For the parity case:

$$
p=2,
$$

it becomes:

$$
\boxed{
q<4.
}
$$

If we set in this paper:

$$
q=m,
$$

we obtain exactly the same criticality:

$$
\boxed{
m<4.
}
$$

---

# 41. But the Two $m<4$ Are Not the Same Theorem

This paper proves:

$$
\boxed{
P_k(m)\to1
}
$$

is merely a finite-word / residue-cylinder combinatorial theorem.

The theorem by Gonçalves–Greenfeld–Madrid deals with the almost-bounded behavior of actual generalized Collatz orbits, and requires deeper analytic/probabilistic machinery.

So:

$$
\boxed{
\text{same critical constant}
\neq
\text{same mathematical result}.
}
$$

Their agreement should be viewed as a structural consistency check.

---

# 42. The Danger of Broader Collatz-like Maps

A general Collatz-like map can be written as:

$$
T(N)=a_NN+b_N
$$

where:

$$
a_N,b_N
$$

depend periodically on the residue class.

Existing literature also points out that Conway's FRACTRAN is related to such systems; a sufficiently general Collatz-like family can simulate universal computation, hence certain global orbit questions are even undecidable.

So:

$$
\boxed{
\text{不能期待 RCOT 的局部簡化自動產生所有 Collatz-like systems 的 global classification}.
}
$$

This again illustrates why this paper must be restricted to a specific affine parity kernel.

---

# 43. RCOT Parity Kernel

This paper refers to the following conditions as the **RCOT parity kernel**:

1. The state domain is the positive integers;
2. The branch domain is determined by parity;
3. The branch maps are scalar affine maps;
4. The common denominator is 2;
5. The odd multiplier $m$ is a unit modulo $2^k$;
6. The translation $r$ keeps the odd branch integer-valued;
7. Scalar coefficient multiplication is commutative.

In this domain, all of the following hold:

$$
\boxed{
\text{finite affine closure},
}
$$

$$
\boxed{
\text{count/order decomposition},
}
$$

$$
\boxed{
\text{unique residue cylinder},
}
$$

$$
\boxed{
\text{local identityization},
}
$$

$$
\boxed{
\text{exact inverse recovery},
}
$$

$$
\boxed{
\text{binomial cylinder law}.
}
$$

---

# 44. What is Collatz-specific?

Collatz-specific:

$$
m=3,\qquad r=1.
$$

Thus specifically:

$$
\alpha=\frac{\ln2}{\ln3},
$$

$$
2^k\leftrightarrow3^u,
$$

$$
R_\kappa(t)=\frac{2^\kappa t-1}{3},
$$

and:

$$
\frac{4^j-1}{3}
$$

and similar families.

---

# 45. What is NOT Collatz-specific?

All of the following actually belong to the generalized odd-$m,r$ RCOT:

- finite-word affine closure;
- upper-triangular matrix representation;
- word/residue bijection mod $2^k$;
- source cylinder ↔ target $m^u$-progression;
- quotient-label identityization;
- exact recovery;
- branch-order correction;
- $m^u\lessgtr2^k$ finite-word phase boundary;
- generalized binomial cylinder law;
- valuation run-length compression.

So the previous six papers actually revealed a much larger local arithmetic class than Collatz.

---

# 46. Generalized Order Correction Width

From:

$$
b_{\max}
=
2^{k-u}b_{\min},
$$

we have:

$$
\boxed{
W_{k,u}^{(m,r)}
=
r
\left(2^{k-u}-1\right)
\frac{m^u-2^u}{m-2}.
}
$$

So branch-order sensitivity:

- scales linearly with $r$;
- grows with $k-u$;
- is controlled by $m^u-2^u$.

This provides the exact finite width of the generalized affine correction.

---

# 47. Order-Uniform Threshold

contracting:

$$
m^u<2^k.
$$

Using the maximum correction:

$$
b_{\max}
=
r2^{k-u}\frac{m^u-2^u}{m-2},
$$

yields:

$$
\boxed{
\Theta_{k,u}^{(m,r)}
=
\left\lfloor
\frac{
r2^{k-u}(m^u-2^u)
}{
(m-2)(2^k-m^u)
}
\right\rfloor+1.
}
$$

Then all fixed $(k,u)$ words:

$$
n\ge\Theta_{k,u}^{(m,r)}
$$

undergo strict descent.

So the generalized family can likewise compress a complete word into a conservative $(k,u)$ certificate.

---

# 48. Why $m=3$ is Special but Not Mystical

In the odd multiplier family:

$$
1,3,5,7,\ldots,
$$

$m=1$ is a degenerate case of nearly pure contraction.

The truly first nontrivial odd multiplier with multiplicative growth:

$$
m=3
$$

still lies in:

$$
m<4.
$$

The next:

$$
m=5
$$

has already crossed the phase boundary.

So Collatz's $3$ lies in a very narrow parameter window:

$$
\boxed{
\text{nontrivial growth}
+
\text{typical finite-word contraction}.
}
$$

This is likely one of the important structural reasons why the $3x+1$ system is both simple and exhibits a long-term descending tendency.

---

# 49. But the Cylinder Density of $m=3$ is Still Not Convergence

Even if:

$$
P_k(3)\to1,
$$

it still cannot be deduced that all $3x+r$ systems are globally bounded.

Different $r$ can alter:

- periodic points;
- cycles;
- finite thresholds;
- chart transitions;
- orbit merging patterns.

Thus:

$$
\boxed{
\text{skeleton phase}
\neq
\text{complete global dynamics}.
}
$$

---

# 50. Summary of Main Theorems in This Paper

## Theorem A — Generalized Affine Closure

$$
\boxed{
F_w^{(m,r)}(x)
=
\frac{m^ux+b_w^{(m,r)}}{2^k}.
}
$$

## Theorem B — Correction Closed Form

$$
\boxed{
b_w^{(m,r)}
=
r\sum_{t=1}^{u}
2^{j_t-1}m^{u-t}.
}
$$

## Theorem C — Unique Residue Cylinder

$$
\boxed{
r_w
\equiv
-b_wm^{-u}
\pmod{2^k}.
}
$$

## Theorem D — Local Identityization

$$
\boxed{
T_{m,r}^k(r_w+2^ka)
=
s_w+m^ua,
}
$$

hence:

$$
\boxed{
\psi_wT_{m,r}^k\phi_w^{-1}
=
\operatorname{id}.
}
$$

## Theorem E — Generalized Contraction Boundary

For odd $m>1$:

$$
\boxed{
m^u<2^k
\iff
u/k<\ln2/\ln m.
}
$$

For $m=1$, any nonempty word satisfies $m^u=1<2^k$, which must be handled independently and cannot be substituted into the $\ln m$ denominator.

## Theorem F — Generalized Binomial Cylinder Law

For odd $m>1$:

$$
\boxed{
P_k(m)
=
2^{-k}
\sum_{u=0}^{\lfloor k\ln2/\ln m\rfloor}
\binom ku.
}
$$

and:

$$
\boxed{P_k(1)=1.}
$$

## Theorem G — Cylinder Phase Classification

$$
\boxed{
P_k(3)\to1,
}
$$

and for odd:

$$
\boxed{
m\ge5
\Rightarrow
P_k(m)\to0.
}
$$

## Theorem H — Critical Parameter

$$
\boxed{
m_c=4.
}
$$

---

# 51. Conclusion

The previous six papers started from Collatz to establish:

$$
\text{finite word}
\to
\text{affine operator}
\to
\text{residue cylinder}
\to
\text{identity chart}
\to
\text{contraction law}
\to
\text{valuation language}.
$$

This paper shows that the core part of this chain does not depend on:

$$
3,\qquad1.
$$

As long as:

$$
m,r
$$

are positive odd integers,

the entire local RCOT structure still holds:

$$
\boxed{
T_{m,r}^k(r_w+2^ka)
=
s_w+m^ua.
}
$$

Thus:

$$
\boxed{
\text{Collatz is one member of a larger residue-class affine translation family}.
}
$$

And the phase boundary truly controlled by $m$:

$$
\boxed{
m_c=4
}
$$

appears simultaneously across three different levels:

1. binomial parity-cylinder majority;
2. accelerated one-step valuation mean;
3. the known analytic condition of the more general $p,q,r$ almost-all theory when $p=2$.

This consistency does not equate to a global proof, but it clearly indicates:

$$
\boxed{
m=3
}
$$

lies in a special subcritical regime within the generalized family.

The next paper will no longer merely change numbers.

We will truly change the **algebra**:

$$
\mathbb Z
\to
\text{commutative rings}
\to
\text{zero divisors}
\to
\text{unordered fields}
\to
\text{matrices / noncommutative algebras}
\to
\text{Möbius maps}
\to
\text{nonlinear polynomials}.
$$

The goal is to answer:

> At which layer do the theorems of RCOT first break? Is it residue uniqueness, exact recovery, count/order decomposition, or the finite-dimensional closure itself that breaks?

---

# References

1. Felipe Gonçalves, Rachel Greenfeld, Jose Madrid, *Generalized Collatz Maps with Almost Bounded Orbits*, arXiv:2111.06170.
2. Alec Edgington, *The autoconjugacy of a generalized Collatz map*, arXiv:1206.0553.
3. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562; Forum of Mathematics, Pi 10 (2022).
4. John H. Conway, work on generalized Collatz-like iterations and FRACTRAN, as discussed in the generalized Collatz literature.
5. Matthews & Watts, generalized Syracuse / residue-class-wise affine mappings, as discussed in Gonçalves–Greenfeld–Madrid.
6. Collatz Operation Translation Series — Papers 02–06.

---

## Next Paper

**Paper 08 — *Algebraic Domains and Structural Breaking Theorems***

Core tasks:

1. Extend from $\mathbb Z/\mathbb Q$ to general commutative integral domains;
2. Examine how residue uniqueness fractures when the multiplier is not a unit;
3. Examine how zero divisors destroy exact inverse recovery;
4. Examine how the semantics of "descent" change in $\mathbb C$ and $p$-adic domains;
5. Enter matrices / noncommutative algebras, proving that order dependence enters the leading operator;
6. Extend to Möbius transformations, identifying that finite-dimensional closure survives but progression transport vanishes;
7. Extend to degree $>1$ polynomial maps, identifying the breaking of fixed-dimensional affine closure.