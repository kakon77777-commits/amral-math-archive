# Finite-Word Contraction Boundaries and the Binomial Cylinder Law
## ——From Exact Affine Drift and Word-Order Correction to a Purely Combinatorial Explanation of $89.4943\%$

**English Title:** *Finite-Word Contraction Boundaries and the Binomial Cylinder Law in the Collatz Local Affine Atlas*

**作者：** Neo.K  
**機構：** EveMiss Technology Co., Ltd. (EveMissLab)  
**系列：** Collatz Operation Translation Series — Paper 05  
**版本：** v0.1  
**日期：** 2026-08-10

---

## Abstract

Papers 02–04 have established the finite-word affine closure, the parity-word/residue-cylinder correspondence, and the bidirectional exact residue-class translation for the modified Collatz map. For any admissible parity word $w$ of length $k$, let $u=u(w)$ be the total number of odd branches $U$. Then, on its unique source cylinder:

$$
\boxed{
T^k(n)
=
F_w(n)
=
\frac{3^u n+b_w}{2^k},
}
$$

where:

$$
b_w\ge0
$$

is the exact affine correction determined by the word order.

This paper answers the following question:

> Under what conditions does a fixed-word chart guarantee a descent below the starting point after $k$ steps?

Direct comparison:

$$
F_w(n)<n
$$

yields:

$$
\boxed{
b_w<(2^k-3^u)n.
}
$$

Thus, finite words possess a structural boundary determined entirely by the principal multiplier:

$$
\boxed{
3^u<2^k
}
$$

and

$$
\boxed{
3^u>2^k.
}
$$

If:

$$
3^u<2^k,
$$

then $w$ is called a **contracting word**, and there exists an exact finite threshold

$$
\boxed{
\theta_w
=
\left\lfloor
\frac{b_w}{2^k-3^u}
\right\rfloor+1
}
$$

such that all admissible:

$$
n\ge\theta_w
$$

satisfy:

$$
T^k(n)<n.
$$

If:

$$
3^u>2^k,
$$

then since $b_w\ge0$,

$$
\boxed{
T^k(n)>n
}
$$

holds for every positive admissible $n$ in that chart; in this case, it is not "asymptotically rising," but rather the entire positive cylinder is $k$-block expanding.

For any nonempty finite word, there is no:

$$
3^u=2^k,
$$

because the prime factorizations of $2$ and $3$ are mutually exclusive. Therefore, every nonempty parity word falls strictly on either the contracting or expanding side; the only possible block equality is caused by the affine correction canceling out the principal contraction, namely:

$$
T^k(n)=n
\iff
n=\frac{b_w}{2^k-3^u}
$$

and the right side must be an admissible positive integer.

Define:

$$
\alpha
=
\frac{\ln2}{\ln3}
\approx
0.6309297536.
$$

Then:

$$
3^u<2^k
\iff
\frac uk<\alpha.
$$

Since $\alpha$ is irrational, $\alpha k$ is not an integer for any positive integer $k$, so the exact count of length-$k$ contracting words is:

$$
\boxed{
A_k
=
\sum_{u=0}^{\lfloor\alpha k\rfloor}
\binom{k}{u}.
}
$$

By the word–residue bijection from Paper 03, this is also the number of contracting residue cylinders modulo $2^k$. Thus, its cylinder-class proportion is:

$$
\boxed{
P_k
=
\frac{1}{2^k}
\sum_{u=0}^{\lfloor\alpha k\rfloor}
\binom{k}{u}.
}
$$

For:

$$
k=16,
$$

we have:

$$
\lfloor16\alpha\rfloor=10,
$$

hence:

$$
A_{16}
=
\sum_{u=0}^{10}\binom{16}{u}
=
58651
$$

and:

$$
\boxed{
P_{16}
=
\frac{58651}{65536}
=
0.8949432373\ldots
}
$$

which is:

$$
\boxed{
89.4943237\%.
}
$$

This provides a purely mathematical explanation for the approximately $89.494\%$ cylinder pruning phenomenon observed in the previous finite-verification prototype for $k=16$. However, this paper further corrects: **the cylinder-class proportion is not exactly identical to the strict-descent certificate proportion within a specific finite interval.**

In the experimental domain:

$$
1\le n<2^{20},
$$

the exact number of strict-descent certificates for $k=16$ is:

$$
938413,
$$

with a proportion of:

$$
\boxed{
\frac{938413}{1048575}
=
89.4941229\%\ldots
}
$$

The slight difference from $P_{16}$ arises from finite boundaries and block equality: $n=0$ for residue $0$ does not belong to the positive domain, and $n=1,2$ return to themselves after 16 modified-Collatz steps, thus failing to satisfy the strict $<$. Therefore, the high consistency between the previous rounded benchmark and $89.4943\%$ is not a numerical coincidence, but "class density" and "finite strict certificate rate" must be precisely distinguished.

Since:

$$
\alpha>\frac12
$$

(equivalent to $3<4$), if we let:

$$
X_k\sim\operatorname{Binomial}(k,1/2),
$$

then:

$$
P_k
=
\Pr(X_k\le\alpha k)
$$

holds in the sense of integer thresholds, and thus by the Law of Large Numbers:

$$
\boxed{
P_k\to1.
}
$$

Furthermore, by the Chernoff large-deviation bound:

$$
1-P_k
\le
\exp\left(
-kD\!\left(\alpha\middle\|\frac12\right)
\right),
$$

where:

$$
D\!\left(\alpha\middle\|\frac12\right)
=
\alpha\ln(2\alpha)
+
(1-\alpha)\ln(2(1-\alpha))
\approx
0.0346882.
$$

Thus, the combinatorial proportion of expanding finite-word cylinders tends to 0 at an exponential rate.

However, the most important quantifier warning of this paper also becomes clearer from this:

$$
\boxed{
P_k\to1
\not\Rightarrow
\text{Collatz conjecture}.
}
$$

A density-one finite-word contraction cannot rule out an ordinary positive-integer orbit continuously traversing rare expanding/correction-dominated prefixes. This forms a clear logical boundary with existing parity-vector, stopping-time, paradoxical-sequence, and Tao's almost-all results.

This paper thus completes the upgrade from the old heuristic that "on average, division by 2 defeats 3" to the following exact finite-word statement:

$$
\boxed{
\text{finite-word drift sign is determined exactly by }3^u\lessgtr2^k,
}
$$

while the word order only affects the finite correction threshold on the contracting side, without changing the asymptotic side.

**Keywords:** Collatz conjecture, contraction boundary, parity word, binomial law, residue cylinder, stopping time, affine correction, large deviations, finite verification, operation translation

---

# 1. From Local Affine Atlas to Descent

Paper 03 establishes for a fixed parity word:

$$
w\in\{D,U\}^k
$$

a unique admissible residue cylinder:

$$
\Omega_w
=
(r_w+2^k\mathbb Z)\cap\mathbb Z_{>0}.
$$

Paper 02 gives:

$$
\boxed{
T^k(n)
=
\frac{3^un+b_w}{2^k}
}
$$

for all:

$$
n\in\Omega_w.
$$

Therefore, stopping-time type problems no longer require step-by-step analysis within a fixed chart.

One only needs to compare an affine operator with the identity.

---

# 2. Exact Descent Equation

Consider:

$$
T^k(n)-n.
$$

We have:

$$
T^k(n)-n
=
\frac{3^un+b_w}{2^k}-n
$$

$$
=
\boxed{
\frac{
(3^u-2^k)n+b_w
}{
2^k
}.
}
$$

Thus:

$$
T^k(n)<n
$$

if and only if:

$$
\boxed{
b_w<(2^k-3^u)n.
}
$$

This is the master equation for all contraction results in this paper.

---

# 3. Drift Gap

Define:

$$
\boxed{
\Delta_{k,u}
=
2^k-3^u.
}
$$

Then:

$$
T^k(n)-n
=
\frac{
b_w-\Delta_{k,u}n
}{2^k}.
$$

Therefore, fixed-word behavior can be classified by:

$$
\operatorname{sgn}\Delta_{k,u}
$$

---

# 4. Contracting Word

If:

$$
\boxed{
\Delta_{k,u}>0
}
$$

namely:

$$
\boxed{
3^u<2^k,
}
$$

then:

$$
T^k(n)<n
$$

is equivalent to:

$$
n>\frac{b_w}{\Delta_{k,u}}.
$$

So we define:

$$
\boxed{
\theta_w
=
\left\lfloor
\frac{b_w}{2^k-3^u}
\right\rfloor+1.
}
$$

yielding:

## Theorem 4.1 — Exact Contracting Threshold

If:

$$
3^u<2^k,
$$

then for all:

$$
n\in\Omega_w
$$

and:

$$
n\ge\theta_w,
$$

we have:

$$
\boxed{
T^k(n)<n.
}
$$

---

# 5. Correction Only Determines "When Descent Begins"

For a contracting word:

Principal slope:

$$
\lambda_w=\frac{3^u}{2^k}<1.
$$

But if:

$$
b_w>0,
$$

a very small $n$ may still:

- rise;
- or return exactly to itself.

Therefore:

$$
\boxed{
3^u<2^k
}
$$

determines the ultimate direction of the entire cylinder,

while:

$$
\boxed{
b_w
}
$$

determines the finite-size threshold.

This is precisely:

$$
\boxed{
\text{multiplicative skeleton}
+
\text{order correction}
}
$$

the specific division of labor in the descent problem.

---

# 6. Expanding Words Are Stronger Than Expected

If:

$$
3^u>2^k,
$$

then for any:

$$
n>0,
$$

we have:

$$
(3^u-2^k)n>0
$$

and:

$$
b_w\ge0.
$$

Thus:

$$
\boxed{
T^k(n)-n>0.
}
$$

Therefore:

## Theorem 6.1 — Uniform Block Expansion

If:

$$
\boxed{
3^u>2^k,
}
$$

then for all positive admissible:

$$
n\in\Omega_w,
$$

we have:

$$
\boxed{
T^k(n)>n.
}
$$

So an expanding word does not only rise as $n\to\infty$.

The entire positive cylinder rises over that block length.

---

# 7. Nonempty Words Have No Neutral Slope

If:

$$
3^u=2^k,
$$

by unique prime factorization, it must be that:

$$
u=k=0.
$$

So for:

$$
k\ge1,
$$

it is impossible to have:

$$
3^u=2^k.
$$

Therefore:

$$
\boxed{
\text{every nonempty finite word is strictly on one side of the slope boundary}.
}
$$

Namely:

$$
\boxed{
3^u<2^k
\quad\text{or}\quad
3^u>2^k.
}
$$

---

# 8. Block Equality Can Still Occur

Although the slope cannot equal 1,

a contracting word may still have, at a specific $n$:

$$
T^k(n)=n.
$$

From the master equation:

$$
(2^k-3^u)n=b_w.
$$

Thus:

$$
\boxed{
n_w^\ast
=
\frac{b_w}{2^k-3^u}.
}
$$

If the right side:

1. is a positive integer;
2. and belongs to $\Omega_w$;

then it is a periodic/fixed point of that fixed-word block.

So:

$$
\boxed{
\text{slope contraction}
\neq
\text{strict descent at every finite point}.
}
$$

---

# 9. Block Equality of the Trivial Collatz Cycle

modified Collatz:

$$
1\to2\to1.
$$

Thus, any even block length:

$$
2q
$$

has:

$$
T^{2q}(1)=1,
$$

$$
T^{2q}(2)=2.
$$

Especially for:

$$
k=16,
$$

$n=1,2$ are both:

$$
\boxed{
T^{16}(n)=n.
}
$$

So even if their 16-step words lie on the contracting-slope side,

they are still not strict-descent certificates.

---

# 10. Any Positive Cycle Must Live on Contracting-Slope Side

If some positive periodic orbit has a length-$k$ parity word $w$,

then:

$$
T^k(n)=n.
$$

Thus:

$$
(2^k-3^u)n=b_w.
$$

Since:

$$
n>0,
\qquad
b_w\ge0,
$$

non-trivial cases must have:

$$
\boxed{
2^k>3^u.
}
$$

That is:

$$
\boxed{
\frac uk<
\frac{\ln2}{\ln3}.
}
$$

This is a necessary condition that all positive periodic blocks must satisfy.

It does not rule out non-trivial Collatz cycles;

it merely restricts possible cycle words to the contracting-slope side.

---

# 11. Critical Odd-Step Fraction

Define:

$$
\boxed{
\alpha
=
\frac{\ln2}{\ln3}.
}
$$

Value:

$$
\boxed{
\alpha
\approx0.6309297535714574.
}
$$

Then:

$$
3^u<2^k
$$

is equivalent to:

$$
u\ln3<k\ln2,
$$

namely:

$$
\boxed{
\frac uk<\alpha.
}
$$

---

# 12. $\alpha$ is Irrational

Assume:

$$
\alpha=\frac pq
$$

is a rational number.

Then:

$$
\frac{\ln2}{\ln3}
=
\frac pq
$$

implies:

$$
q\ln2=p\ln3
$$

thus:

$$
2^q=3^p.
$$

This is impossible by unique prime factorization.

Therefore:

$$
\boxed{
\alpha\notin\mathbb Q.
}
$$

Hence, for any:

$$
k\ge1,
$$

$$
\alpha k
$$

is not an integer.

---

# 13. Exact Contracting Count

There are a total of:

$$
2^k
$$

length-$k$ parity words.

The number of words containing exactly:

$$
u
$$

$U$'s is:

$$
\boxed{
\binom ku.
}
$$

The contracting condition is:

$$
u<\alpha k.
$$

Since $\alpha k$ is not an integer, this is equivalent to:

$$
u\le\lfloor\alpha k\rfloor.
$$

Therefore:

## Theorem 13.1 — Binomial Cylinder Count

$$
\boxed{
A_k
=
\sum_{u=0}^{\lfloor\alpha k\rfloor}
\binom ku.
}
$$

---

# 14. Why is this also the Residue Cylinder Count?

Paper 03 has proven:

$$
\boxed{
\{D,U\}^k
\longleftrightarrow
\mathbb Z/2^k\mathbb Z.
}
$$

So every parity word corresponds exactly to one modulo $2^k$ cylinder.

Therefore:

$$
A_k
$$

is not only the number of contracting words,

but also the exact number of:

$$
\boxed{
\text{contracting residue cylinders modulo }2^k
}
$$

---

# 15. Cylinder-Class Proportion

Define:

$$
\boxed{
P_k
=
\frac{A_k}{2^k}.
}
$$

Thus:

$$
\boxed{
P_k
=
\frac1{2^k}
\sum_{u=0}^{\lfloor\alpha k\rfloor}
\binom ku.
}
$$

This is called the **Binomial Cylinder Law**.

---

# 16. $k=8$

$$
8\alpha
\approx5.047.
$$

So:

$$
u\le5.
$$

$$
A_8
=
\sum_{u=0}^5\binom8u
=
219.
$$

Therefore:

$$
\boxed{
P_8
=
\frac{219}{256}
=
85.546875\%.
}
$$

---

# 17. $k=12$

$$
12\alpha
\approx7.571.
$$

So:

$$
u\le7.
$$

$$
A_{12}=3302.
$$

Thus:

$$
\boxed{
P_{12}
=
\frac{3302}{4096}
=
80.615234375\%.
}
$$

This is lower than for $k=8$.

Therefore:

$$
\boxed{
P_k
\text{ is not necessarily monotonic for finite } k.
}
$$

The reason is the discrete jumps of the floor threshold.

---

# 18. $k=16$: The Origin of $89.4943\%$

$$
16\alpha
\approx10.094876.
$$

So:

$$
u\le10.
$$

Therefore:

$$
A_{16}
=
\sum_{u=0}^{10}\binom{16}{u}.
$$

Direct calculation yields:

$$
\boxed{
A_{16}=58651.
}
$$

Hence:

$$
\boxed{
P_{16}
=
\frac{58651}{65536}
=
0.8949432373046875.
}
$$

which is:

$$
\boxed{
89.49432373046875\%.
}
$$

---

# 19. This Explains the Previous Benchmark, but is Not Exactly the Same Proportion

The previous finite-verification prototype in:

$$
1\le n<2^{20}
$$

using:

$$
k=16
$$

obtained:

$$
938413
$$

strict $16$-step descent certificates.

Its proportion is:

$$
\boxed{
\frac{938413}{1048575}
\approx
89.4941229\%.
}
$$

It is extremely close to:

$$
P_{16}
\approx89.4943237\%
$$

but is not the exact same number.

---

# 20. Difference One: $n=0$ is Excluded

Since:

$$
2^{20}=16\cdot2^{16},
$$

each modulo $2^{16}$ residue appears exactly 16 times in:

$$
0\le n<2^{20}
$$

If we multiply all contracting classes by 16:

$$
58651\cdot16
=
938416.
$$

But the positive domain excludes:

$$
n=0.
$$

And residue $0$ itself is a contracting class.

So it first becomes:

$$
938415.
$$

---

# 21. Difference Two: $1,2$ are Equality, Not Descent

As mentioned earlier:

$$
T^{16}(1)=1,
$$

$$
T^{16}(2)=2.
$$

So we must also subtract 2 starting values that are not strict descents:

$$
938415-2
=
\boxed{
938413.
}
$$

This exactly equals the exact certificate count of the benchmark.

Therefore:

$$
\boxed{
\text{benchmark count}
=
\text{binomial class law}
+
\text{finite-domain boundary correction}.
}
$$

This is a complete theory-experiment alignment.

---

# 22. $k=20$

$$
20\alpha
\approx12.6186.
$$

So:

$$
u\le12.
$$

Yielding:

$$
A_{20}=910596.
$$

Therefore:

$$
\boxed{
P_{20}
=
\frac{910596}{1048576}
\approx86.8412\%.
}
$$

This again illustrates that the finite-$k$ proportion exhibits staircase oscillation.

---

# 23. Large-Scale Trend

Although:

$$
P_k
$$

is not monotonic for finite values,

its limit is very clear.

Let:

$$
X_k\sim\operatorname{Binomial}(k,1/2).
$$

Then:

$$
\Pr(X_k=u)
=
\frac1{2^k}\binom ku.
$$

Therefore:

$$
\boxed{
P_k
=
\Pr(X_k<\alpha k).
}
$$

After integerization, this is equivalent to the previous formula.

---

# 24. Why is $\alpha>1/2$?

$$
\alpha>\frac12
$$

is equivalent to:

$$
2\ln2>\ln3
$$

equivalent to:

$$
\ln4>\ln3
$$

namely:

$$
\boxed{
4>3.
}
$$

Therefore, the mean fraction of the binomial distribution:

$$
1/2
$$

lies to the left of the contraction threshold:

$$
\alpha
$$

---

# 25. Law of Large Numbers

From:

$$
\frac{X_k}{k}\to\frac12
$$

in probability,

and:

$$
\frac12<\alpha,
$$

we obtain:

$$
\boxed{
\Pr\left(
\frac{X_k}{k}<\alpha
\right)\to1.
}
$$

Therefore:

## Theorem 25.1

$$
\boxed{
P_k\to1.
}
$$

Namely:

> Among length-$k$ parity cylinders, the proportion of contracting-slope cylinders approaches 100%.

---

# 26. Large-Deviation Rate

More precisely, for:

$$
\alpha>\frac12,
$$

the Chernoff bound gives:

$$
\Pr(X_k\ge\alpha k)
\le
\exp\left(
-kD\!\left(
\alpha\middle\|\frac12
\right)
\right).
$$

where the binary relative entropy is:

$$
\boxed{
D\!\left(
\alpha\middle\|\frac12
\right)
=
\alpha\ln(2\alpha)
+
(1-\alpha)\ln(2(1-\alpha)).
}
$$

For:

$$
\alpha=\frac{\ln2}{\ln3},
$$

the value is approximately:

$$
\boxed{
D\approx0.0346882.
}
$$

Thus, the expanding-word fraction has an exponential upper bound.

---

# 27. This is Not a Stochastic Collatz Assumption

This point is crucial.

This paper does not assume:

> The actual Collatz orbit behaves like an independent fair coin at each step.

We are merely performing uniform combinatorial counting over the **finite set of all length-$k$ words**.

Since Paper 03 has proven:

$$
\text{word}
\leftrightarrow
\text{residue class mod }2^k,
$$

So:

$$
\frac{1}{2^k}\binom ku
$$

is also the exact finite density of the residue-class.

Therefore:

$$
\boxed{
P_k
}
$$

is a deterministic combinatorial fact,

not a stochastic orbit model.

---

# 28. But There is Still a Wall Between Residue Density and Orbit Theorem

Although:

$$
P_k\to1,
$$

there may still exist a tiny minority of:

$$
1-P_k
$$

expanding cylinders.

Whether the subsequent prefixes of a specific positive integer orbit:

- repeatedly fall into rare expanding cylinders;
- or stop below the finite correction threshold in contracting cylinders;

cannot be determined solely by $P_k$.

Therefore:

$$
\boxed{
\text{density of charts}
\neq
\text{itinerary theorem}.
}
$$

---

# 29. Logical Relationship with Almost-All Results

Tao's result proves:

For any:

$$
f(N)\to\infty,
$$

almost all $N$ (in logarithmic density) satisfy:

$$
\operatorname{Col}_{\min}(N)\le f(N).
$$

That is a deep almost-all theorem regarding actual Collatz orbits.

This paper's:

$$
P_k\to1
$$

is merely finite parity-cylinder combinatorics.

So the two cannot be conflated as the same result.

The value of this paper lies in:

$$
\boxed{
\text{making the local affine slope distribution exact}.
}
$$

It does not replace Tao's global probabilistic/analytic machinery.

---

# 30. Relationship with Paradoxical Finite Prefixes

Recent parity-vector/stopping-time research examines:

- odd-step proportion;
- growth of finite prefixes;
- deviation between slope prediction and actual finite correction;
- so-called paradoxical sequence behavior.

This paper provides a precise decomposition:

$$
\boxed{
\text{slope effect}
=
\frac{3^u}{2^k},
}
$$

$$
\boxed{
\text{finite correction}
=
\frac{b_w}{2^k}.
}
$$

Therefore, any situation where "the principal slope predicts descent, but the finite starting point has not yet descended" can be pinpointed as:

$$
\boxed{
b_w
\text{ has not yet been overpowered by }
(2^k-3^u)n.
}
$$

---

# 31. How Does Word Order Affect the Threshold?

Paper 02 has proven for fixed $(k,u)$:

$$
3^u-2^u
\le
b_w
\le
2^{k-u}(3^u-2^u).
$$

For contracting:

$$
2^k>3^u,
$$

the threshold is:

$$
\theta_w
=
\left\lfloor
\frac{b_w}{2^k-3^u}
\right\rfloor+1.
$$

Therefore:

$$
b_w
$$

the larger it is,

the higher the finite threshold.

---

# 32. Order-Uniform Descent Threshold

Using the worst-case:

$$
b_{\max}
=
2^{k-u}(3^u-2^u),
$$

define:

$$
\boxed{
\Theta_{k,u}
=
\left\lfloor
\frac{
2^{k-u}(3^u-2^u)
}{
2^k-3^u
}
\right\rfloor
+1.
}
$$

As long as:

$$
3^u<2^k,
$$

then for **all** length-$k$ words containing exactly $u$ $U$'s:

$$
w,
$$

and all admissible:

$$
n\ge\Theta_{k,u},
$$

we have:

$$
\boxed{
T^k(n)<n.
}
$$

---

# 33. This Compresses the Full Word into a $(k,u)$ Certificate

Usually, the exact threshold:

$$
\theta_w
$$

requires:

$$
b_w,
$$

so it requires complete word-order data.

But if one is willing to use the conservative upper bound:

$$
\Theta_{k,u},
$$

then only:

$$
\boxed{
(k,u)
}
$$

is needed to provide a universal finite threshold for the entire word family.

Thus, operation translation once again yields information compression:

$$
\boxed{
w
\to
(k,u)
}
$$

But the cost is that the certificate becomes conservative.

---

# 34. Minimum Threshold Word

Paper 02:

$$
b_{\min}=3^u-2^u
$$

is achieved by:

$$
U^uD^{k-u}
$$

Therefore, for a fixed $(k,u)$, the permutation that descends most easily is:

$$
\boxed{
U^uD^{k-u}.
}
$$

The permutation that begins guaranteed descent the latest is:

$$
\boxed{
D^{k-u}U^u.
}
$$

So the branch order does not change the contraction side;

it only changes the position of the finite threshold.

---

# 35. Example: $UUDD$

$$
k=4,
\qquad
u=2.
$$

$$
3^u=9,
\qquad
2^k=16.
$$

So it is contracting.

Paper 02:

$$
b=5.
$$

Therefore:

$$
\theta_w
=
\left\lfloor
\frac5{7}
\right\rfloor+1
=
1.
$$

So all positive admissible:

$$
n
$$

satisfy:

$$
T^4(n)<n.
$$

For example, the source cylinder:

$$
n=3+16a
$$

has:

$$
T^4(n)=2+9a<n.
$$

---

# 36. Example: $UUU$

$$
k=3,
\qquad
u=3.
$$

$$
3^3=27>8=2^3.
$$

So it is uniform expanding.

Paper 02:

$$
b=19.
$$

Therefore:

$$
T^3(n)
=
\frac{27n+19}{8}
>
n
$$

holds for all its positive admissible:

$$
n\equiv7\pmod8
$$

For example:

$$
7\to11\to17\to26.
$$

So:

$$
26>7.
$$

---

# 37. Local Expansion Does Not Imply Global Escape

In the above example:

$$
7\to11\to17\to26
$$

rises for three steps.

But continuing:

$$
26\to13\to20\to10\to5\to\cdots
$$

it still falls back.

So:

$$
\boxed{
\text{expanding finite word}
\not\Rightarrow
\text{divergent infinite orbit}.
}
$$

This again illustrates:

$$
\boxed{
\text{local chart classification}
\neq
\text{global itinerary classification}.
}
$$

---

# 38. Finite Cylinder Law and the Old Negative Drift Intuition

Old research states in average terms:

> Roughly every odd step is accompanied by enough divisions by 2, so $2$ eventually overpowers $3$.

This paper rewrites this into a completely finite and exact proposition:

When

$$
\boxed{
u/k<\ln2/\ln3
}
$$

the multiplicative skeleton of a fixed word is necessarily contracting.

This does not require:

- 50/50 parity assumption;
- independence;
- random-walk models;
- expectation.

Therefore, the local core of the old heuristic has been fully exactified.

---

# 39. But the Gap in the Global Heuristic Remains

From:

$$
P_k\to1
$$

one cannot deduce:

$$
\forall n,\exists k:
T^k(n)<n.
$$

Because the latter correlates:

$$
k
$$

and:

$$
n
$$

along the actual itinerary.

What truly needs to be ruled out is:

> Does there exist some positive integer whose every candidate descent prefix is blocked by a rare itinerary structure or finite correction?

This remains a global problem.

---

# 40. Core Boundary Map of Paper 05

For a nonempty word:

### Contracting-slope side

$$
\boxed{
u/k<\alpha.
}
$$

There exists a finite strict-descent threshold.

### Expanding side

$$
\boxed{
u/k>\alpha.
}
$$

The entire positive cylinder strictly expands on that block.

### Neutral slope

$$
\boxed{
\varnothing.
}
$$

Since:

$$
\alpha
$$

is irrational.

### Block equality

Can only occur at a single finite value on the contracting side:

$$
\boxed{
n=b_w/(2^k-3^u)
}
$$

if it is an admissible integer.

---

# 41. Direct Connection with Finite Verification

For a contracting cylinder,

once:

$$
n\ge\theta_w,
$$

one can directly output the certificate:

$$
\boxed{
T^k(n)<n.
}
$$

If using strong induction finite verification:

All starting values less than $n$ have already been certified,

then:

$$
T^k(n)<n
$$

immediately completes the path-merge certificate for $n$.

So the mathematics of Paper 05 is precisely the theoretical foundation for the previous benchmark pruning.

---

# 42. What Does This Paper Not Prove?

This paper does not prove:

$$
\forall n,\exists k:T^k(n)<n.
$$

It does not prove that:

$$
P_k\to1
$$

can rule out all exceptional integer itineraries.

It does not prove that all contracting words immediately descend for their minimum positive representative.

It does not rule out non-trivial cycles.

This paper only establishes the exact classification and combinatorial density of finite-word contraction / expansion.

---

# 43. Summary of Main Theorems

## Theorem A — Exact Descent Criterion

$$
\boxed{
T^k(n)<n
\iff
b_w<(2^k-3^u)n.
}
$$

## Theorem B — Contracting Threshold

If:

$$
3^u<2^k,
$$

then:

$$
\boxed{
n\ge\theta_w
\Rightarrow
T^k(n)<n.
}
$$

## Theorem C — Uniform Expansion

If:

$$
3^u>2^k,
$$

then:

$$
\boxed{
T^k(n)>n
}
$$

for all positive admissible $n$.

## Theorem D — Binomial Cylinder Law

$$
\boxed{
A_k
=
\sum_{u=0}^{\lfloor\alpha k\rfloor}
\binom ku,
\qquad
\alpha=\frac{\ln2}{\ln3}.
}
$$

## Theorem E — Cylinder Density

$$
\boxed{
P_k=\frac{A_k}{2^k}\to1.
}
$$

## Theorem F — Order-Uniform Threshold

$$
\boxed{
\Theta_{k,u}
=
\left\lfloor
\frac{
2^{k-u}(3^u-2^u)
}{
2^k-3^u
}
\right\rfloor+1.
}
$$

---

# 44. Conclusion

Paper 02 compressed the finite parity word into an exact affine operator.

Paper 03 identified its valid domain as a unique residue cylinder.

Paper 04 established the bidirectional exact transport between source and target.

This paper completes the fourth step:

$$
\boxed{
\text{each finite chart has an exact drift sign and, when contracting, an exact finite threshold}.
}
$$

Its most core division of labor is:

$$
\boxed{
(k,u)
\text{ decides which side of the contraction boundary the word lies on},
}
$$

while:

$$
\boxed{
b_w
\text{ decides the finite correction threshold}.
}
$$

Therefore:

$$
\boxed{
\text{counts determine asymptotic direction;}
}
$$

$$
\boxed{
\text{order determines finite delay}.
}
$$

Furthermore, by the finite word–residue bijection:

$$
\boxed{
P_k
=
2^{-k}
\sum_{u\le\lfloor\alpha k\rfloor}
\binom ku
}
$$

it precisely describes the contracting cylinder fraction.

For $k=16$:

$$
\boxed{
58651/65536
=
89.4943237\%.
}
$$

And the previous finite benchmark's:

$$
938413/1048575
\approx89.4941229\%
$$

is the result of this class law after positive-domain and strict-descent boundary corrections.

This gives the previous computational observations a complete, purely mathematical explanation for the first time.

However:

$$
\boxed{
P_k\to1
}
$$

still only indicates that the combinatorial proportion of expanding regions in the finite chart space tends to zero.

Collatz conjecture requires:

$$
\boxed{
\text{every actual positive-integer itinerary eventually acquires a descent certificate}.
}
$$

This is a stronger universal itinerary proposition.

The next paper will rewrite the "average division by 2 depth" from old research into precise valuation language, using the accelerated odd map and:

$$
\kappa_i=v_2(3n_i+1)
$$

to compress the parity word into a valuation word, and reorganize $M_j=(4^j-1)/3$, inverse fibers, and exact log drift.

---

# References

1. Olivier Rozier, Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948.
2. Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886.
3. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), arXiv:1909.03562.
4. Collatz Operation Translation Series — Paper 02, *Collatz Local Affine Atlas: Exact Affinization of Finite Parity Words*.
5. Collatz Operation Translation Series — Paper 03, *Parity Word, Residue Cylinder, and Local Identitization*.
6. Collatz Operation Translation Series — Paper 04, *Bidirectional Residue-Class Translation: $2^k$ Cylinders and $3^u$ Progressions*.

---

## Next Paper

**Paper 06 — *Valuation Language and Accelerated Collatz: From Parity Words to $v_2$ Words***

Core tasks:

1. Define the accelerated odd map;
2. Losslessly compress parity runs into a valuation word
   $$
   (\kappa_1,\ldots,\kappa_m);
   $$
3. Derive
   $$
   S^m(n)=\frac{3^mn+B_\kappa}{2^{K}},
   \qquad
   K=\sum_i\kappa_i;
   $$
4. Establish the exact log drift
   $$
   m\ln3-K\ln2+C_\kappa(n);
   $$
5. Correct the old "exponent of 2 defeats 3" heuristic into a finite exact statement;
6. Re-unify terminal inverse fibers and $M_j=(4^j-1)/3$.