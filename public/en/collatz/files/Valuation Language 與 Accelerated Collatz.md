# Valuation Language and the Accelerated Collatz Map
## — From Run-Length Encoding of Parity Words and Exact $v_2$ Drift to Valuation-Order Correction

**English Title:** *Valuation Language and the Accelerated Collatz Map: Exact $v_2$ Drift, Run-Length Encoding, and Valuation-Order Corrections*

**Author:** Neo.K  
**Institution:** Yiyannuo Technology Co., Ltd. (EveMissLab)  
**Series:** Collatz Operation Translation Series — Paper 06  
**Version:** v0.1  
**Date:** 2026-08-10

---

## Abstract

The author's early research on Collatz systems theory described the heuristic of average descent in Collatz trajectories as "$2$'s exponential contraction eventually overpowering $3$'s amplification." The main issue with this is that the average $2$-adic division depth, negative logarithmic drift, and dissipation analogies can only provide statistical/heuristic justifications. They cannot rule out exceptional orbits and thus cannot be directly elevated to a global proof of the Collatz conjecture.

Using the finite-word affine atlas established in the previous five papers, this paper reformulates this old heuristic into a precise **valuation language**.

For a positive odd integer $n$, we define:

$$
\boxed{
\kappa(n)=v_2(3n+1)\ge1
}
$$

and the accelerated odd Collatz map:

$$
\boxed{
S(n)
=
\frac{3n+1}{2^{\kappa(n)}}.
}
$$

Then:

$$
S(n)
$$

is again a positive odd integer.

For an odd-to-odd orbit of length $m$:

$$
n_0
\to n_1
\to\cdots
\to n_m,
$$

we define the exact valuation word:

$$
\boxed{
\boldsymbol\kappa
=
(\kappa_1,\ldots,\kappa_m),
\qquad
\kappa_i=v_2(3n_{i-1}+1).
}
$$

and the cumulative valuation:

$$
K_j=\sum_{i=1}^j\kappa_i,
\qquad
K_0=0,
$$

$$
K=K_m.
$$

This paper proves:

$$
\boxed{
S^m(n_0)
=
\frac{
3^m n_0+B_{\boldsymbol\kappa}
}{
2^K
},
}
$$

where:

$$
\boxed{
B_{\boldsymbol\kappa}
=
\sum_{i=1}^{m}
3^{m-i}2^{K_{i-1}}.
}
$$

Thus, the accelerated odd dynamics once again exhibit:

$$
\boxed{
\text{multiplicative skeleton}
+
\text{order correction}.
}
$$

The main skeleton depends only on:

$$
(m,K),
$$

while the local arrangement of valuations enters via the prefix sums:

$$
K_{i-1}
$$

into:

$$
B_{\boldsymbol\kappa}.
$$

Therefore, the exact log drift is:

$$
\boxed{
\ln\frac{S^m(n_0)}{n_0}
=
m\ln3
-
K\ln2
+
\ln\left(
1+\frac{B_{\boldsymbol\kappa}}{3^m n_0}
\right).
}
$$

This provides a precise version of the old "$2$'s exponent defeats $3$" heuristic:

$$
\boxed{
2^K>3^m
\iff
\frac Km>\log_2 3
}
$$

is the necessary and sufficient condition for a fixed valuation word to fall on the contracting-skeleton side; if this holds, there exists an exact finite threshold:

$$
\boxed{
n_0>
\frac{
B_{\boldsymbol\kappa}
}{
2^K-3^m
}
}
$$

which guarantees:

$$
S^m(n_0)<n_0.
$$

If:

$$
2^K<3^m,
$$

then:

$$
S^m(n_0)>n_0
$$

holds for all positive admissible inputs on that fixed valuation itinerary.

This paper also proves that there is a natural run-length correspondence between the valuation language and the modified-map parity language. A single odd-to-odd cycle:

$$
\kappa_i
$$

corresponds to the modified parity block:

$$
\boxed{
UD^{\kappa_i-1}.
}
$$

Therefore, a valuation word corresponds to:

$$
\boxed{
UD^{\kappa_1-1}
UD^{\kappa_2-1}
\cdots
UD^{\kappa_m-1},
}
$$

whose total modified-map step length is exactly:

$$
K=\sum_i\kappa_i,
$$

and the number of $U$ steps is:

$$
m.
$$

Thus, the finite-word contraction boundary from Paper 05:

$$
\frac{u}{k}<\frac{\ln2}{\ln3}
$$

is precisely equivalent in the valuation language to:

$$
\boxed{
\frac Km>\frac{\ln3}{\ln2}
=
\log_2 3.
}
$$

This paper further proves a one-step valuation-density law: for any $j\ge1$, in the sense of the natural density of positive odd integers,

$$
\boxed{
\Pr_{\mathrm{res}}\bigl(v_2(3n+1)=j\bigr)
=
2^{-j}.
}
$$

More precisely, among the $2^j$ odd residue classes modulo $2^{j+1}$, exactly one residue class satisfies:

$$
v_2(3n+1)=j.
$$

Therefore:

$$
\boxed{
\sum_{j\ge1}j\,2^{-j}=2.
}
$$

That is, the statement "the average valuation is 2" can be elevated to an exact residue-density statement.

However, this paper specifically emphasizes:

$$
\boxed{
\text{one-step residue density}
\neq
\text{independent valuation process along an orbit}.
}
$$

Thus:

$$
\ln3-2\ln2=\ln(3/4)<0
$$

can only describe the skeleton mean drift of the residue ensemble; it alone cannot imply the convergence of every orbit. Tao's almost-all result for the Syracuse iteration uses approximate-transport, renewal processes, and $3$-adic random-walk machinery that are far stronger than an "independent geometric distribution," which precisely demonstrates that this quantifier gap is real.

This paper also proves the exact impact of valuation order on the correction. If two adjacent terms in a valuation word:

$$
a,b
$$

are swapped while the rest remain unchanged, and the cumulative valuation before this position is $P$, then the correction difference is:

$$
\boxed{
B_{(\ldots,a,b,\ldots)}
-
B_{(\ldots,b,a,\ldots)}
=
3^{m-i-1}2^P(2^a-2^b).
}
$$

Therefore, when:

$$
a>b
$$

placing the larger valuation in an earlier position increases the affine correction. For a fixed valuation multiset:

$$
\boxed{
\text{ascending valuation order minimizes }B_{\boldsymbol\kappa},
}
$$

$$
\boxed{
\text{descending valuation order maximizes }B_{\boldsymbol\kappa}.
}
$$

This is the precise version of "counts determine drift; order determines finite correction" in the accelerated setting.

Finally, this paper reunifies the inverse fibers. For an odd target $t$ and valuation $\kappa$:

$$
\boxed{
R_\kappa(t)
=
\frac{2^\kappa t-1}{3},
}
$$

as long as:

$$
2^\kappa t\equiv1\pmod3
$$

it is a valid odd predecessor. For a reverse-admissible valuation word and a terminal odd state $t=n_m$, one can exactly recover:

$$
\boxed{
n_0
=
\frac{
2^K t-B_{\boldsymbol\kappa}
}{
3^m
}.
}
$$

Thus, the valuation language simultaneously supports forward compression and exact inverse recovery.

This paper does not claim that the valuation language solves the Collatz conjecture. It accomplishes a more precise task:

$$
\boxed{
\text{old heuristic of average negative drift}
\longrightarrow
\text{exact finite valuation-word drift}
+
\text{separate statistical layer}.
}
$$

**Keywords:** Collatz conjecture, accelerated Collatz, Syracuse map, $2$-adic valuation, valuation word, parity vector, log drift, inverse fiber, operation translation, exact recovery

---

# 1. Why Do We Need a Valuation Language?

In the modified Collatz map:

$$
T(n)
=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
$$

after an odd state undergoes $U$,

it may require:

$$
0,1,2,\ldots
$$

additional $D$ steps to return to the next odd state.

For example:

$$
n\text{ odd},
$$

if:

$$
v_2(3n+1)=4,
$$

then the modified parity segment is:

$$
\boxed{
UDDD.
}
$$

Therefore, the complete parity word contains a large number of repeated $D$ runs for odd-to-odd dynamics.

The purpose of the valuation language is to losslessly compress these runs.

---

# 2. Accelerated Odd Map

Let:

$$
\mathcal O
=
\{1,3,5,\ldots\}.
$$

For:

$$
n\in\mathcal O,
$$

define:

$$
\boxed{
\kappa(n)
=
v_2(3n+1).
}
$$

Since for an odd $n$:

$$
3n+1
$$

must be even,

we have:

$$
\kappa(n)\ge1.
$$

We further define:

$$
\boxed{
S(n)
=
\frac{3n+1}{2^{\kappa(n)}}.
}
$$

Since all factors of 2 have been divided out,

we have:

$$
S(n)\in\mathcal O.
$$

Therefore:

$$
\boxed{
S:\mathcal O\to\mathcal O.
}
$$

---

# 3. Valuation Word

Given an actual odd orbit:

$$
n_0
\xrightarrow{S}
n_1
\xrightarrow{S}
\cdots
\xrightarrow{S}
n_m,
$$

we define:

$$
\boxed{
\kappa_i
=
v_2(3n_{i-1}+1).
}
$$

and the valuation word:

$$
\boxed{
\boldsymbol\kappa
=
(\kappa_1,\ldots,\kappa_m)
\in\mathbb Z_{\ge1}^m.
}
$$

---

# 4. Formal Valuation Word and Admissible Valuation Word

Any:

$$
(\kappa_1,\ldots,\kappa_m)
\in\mathbb Z_{\ge1}^m
$$

can serve as a formal symbol.

However, only when there exists:

$$
n_0\in\mathcal O
$$

such that:

$$
v_2(3n_{i-1}+1)=\kappa_i
$$

holds step-by-step,

is it called an admissible valuation word for $n_0$.

Thus, we once again require:

$$
\boxed{
\text{formal language}
\neq
\text{dynamical legality}.
}
$$

---

# 5. Run-Length Expansion

For a valuation symbol:

$$
\kappa\ge1,
$$

we define its modified parity expansion:

$$
\boxed{
E(\kappa)
=
UD^{\kappa-1}.
}
$$

For example:

$$
E(1)=U,
$$

$$
E(2)=UD,
$$

$$
E(4)=UDDD.
$$

For the entire valuation word:

$$
\boxed{
E(\boldsymbol\kappa)
=
UD^{\kappa_1-1}
UD^{\kappa_2-1}
\cdots
UD^{\kappa_m-1}.
}
$$

---

# 6. Run-Length Correspondence

For an actual odd-to-odd trajectory,

each:

$$
\kappa_i
$$

is exactly equal to:

> the number of modified Collatz steps experienced from the $(i-1)$-th odd state to the $i$-th odd state.

Because:

- The first step is $U$, which divides by 2 once;
- Then there are $\kappa_i-1$ steps of $D$;
- And then it reaches the next odd state.

Therefore:

$$
\boxed{
|E(\boldsymbol\kappa)|
=
\sum_{i=1}^m\kappa_i.
}
$$

---

# 7. Cumulative Valuation

Define:

$$
\boxed{
K_j
=
\sum_{i=1}^j\kappa_i,
}
$$

$$
K_0=0.
$$

Total valuation:

$$
\boxed{
K=K_m.
}
$$

In the expanded parity word:

$$
\boxed{
k_{\mathrm{parity}}=K,
}
$$

$$
\boxed{
u_{\mathrm{parity}}=m.
}
$$

This establishes a direct bridge between Paper 05 and the accelerated setting.

---

# 8. One-Cycle Formula

From:

$$
n_i
=
\frac{3n_{i-1}+1}{2^{\kappa_i}},
$$

we rewrite it as:

$$
\boxed{
2^{\kappa_i}n_i
=
3n_{i-1}+1.
}
$$

This is the fundamental local equation of the valuation language.

---

# 9. Two-Cycle Example

Two steps:

$$
n_1
=
\frac{3n_0+1}{2^{\kappa_1}},
$$

$$
n_2
=
\frac{3n_1+1}{2^{\kappa_2}}.
$$

Substituting:

$$
n_2
=
\frac{
3\frac{3n_0+1}{2^{\kappa_1}}+1
}{
2^{\kappa_2}
}
$$

$$
=
\frac{
9n_0+3+2^{\kappa_1}
}{
2^{\kappa_1+\kappa_2}
}.
$$

Therefore:

$$
\boxed{
B_{(\kappa_1,\kappa_2)}
=
3+2^{\kappa_1}.
}
$$

It can already be seen that the correction depends on the valuation order.

---

# 10. Accelerated Affine Closure Theorem

## Theorem 10.1

For any actual admissible valuation word:

$$
\boldsymbol\kappa
=
(\kappa_1,\ldots,\kappa_m),
$$

we have:

$$
\boxed{
S^m(n_0)
=
\frac{
3^mn_0+B_{\boldsymbol\kappa}
}{
2^K
},
}
$$

where:

$$
\boxed{
B_{\boldsymbol\kappa}
=
\sum_{i=1}^{m}
3^{m-i}2^{K_{i-1}}.
}
$$

---

# 11. Proof by Induction

Define:

$$
B_0=0.
$$

Assume:

$$
n_{j-1}
=
\frac{
3^{j-1}n_0+B_{j-1}
}{
2^{K_{j-1}}
}.
$$

Then:

$$
n_j
=
\frac{3n_{j-1}+1}{2^{\kappa_j}}
$$

$$
=
\frac{
3^j n_0
+
3B_{j-1}
+
2^{K_{j-1}}
}{
2^{K_j}
}.
$$

Thus, the recurrence is:

$$
\boxed{
B_j
=
3B_{j-1}
+
2^{K_{j-1}}.
}
$$

Expanding this yields:

$$
\boxed{
B_j
=
\sum_{i=1}^{j}
3^{j-i}2^{K_{i-1}}.
}
$$

Proof complete.

---

# 12. Valuation Skeleton and Correction

Define:

$$
\boxed{
\Sigma(\boldsymbol\kappa)
=
(m,K).
}
$$

It determines the leading multiplier:

$$
\boxed{
\lambda_{\boldsymbol\kappa}
=
\frac{3^m}{2^K}.
}
$$

While:

$$
\boxed{
C(\boldsymbol\kappa)
=
B_{\boldsymbol\kappa}
}
$$

preserves the prefix-order information of the valuation word.

Therefore:

$$
\boxed{
S^m(n)
=
\lambda_{\boldsymbol\kappa}n
+
\frac{B_{\boldsymbol\kappa}}{2^K}.
}
$$

---

# 13. Counts Determine Drift; Valuation Order Determines Correction

Two valuation words can have the same:

$$
m
$$

and:

$$
K,
$$

yet have different:

$$
B_{\boldsymbol\kappa}.
$$

For example:

$$
(1,3)
$$

and:

$$
(3,1)
$$

both have:

$$
m=2,
\qquad
K=4.
$$

But:

$$
B_{(1,3)}
=
3+2
=
5,
$$

$$
B_{(3,1)}
=
3+8
=
11.
$$

Therefore:

$$
\boxed{
\text{same drift skeleton}
\not\Rightarrow
\text{same finite operator}.
}
$$

---

# 14. Exact Correspondence with Paper 02

The expanded parity word:

$$
E(\boldsymbol\kappa)
$$

has:

$$
k=K,
$$

$$
u=m.
$$

Therefore, in Paper 02:

$$
F_w(n)
=
\frac{3^un+b_w}{2^k}
$$

becomes in valuation form:

$$
\boxed{
S^m(n)
=
\frac{
3^mn+B_{\boldsymbol\kappa}
}{
2^K
}.
}
$$

Thus:

$$
\boxed{
B_{\boldsymbol\kappa}
=
b_{E(\boldsymbol\kappa)}
}
$$

holds for actual odd-to-odd segments.

The valuation language is not a different set of dynamics,

but rather the run-length compressed coordinates of the parity language.

---

# 15. Exact Log Drift

For:

$$
n_0>0,
$$

we have:

$$
S^m(n_0)
=
\frac{
3^mn_0+B_{\boldsymbol\kappa}
}{
2^K
}.
$$

Taking the logarithm:

$$
\ln S^m(n_0)
=
m\ln3
-
K\ln2
+
\ln n_0
+
\ln\left(
1+
\frac{
B_{\boldsymbol\kappa}
}{
3^m n_0
}
\right).
$$

Therefore:

$$
\boxed{
\Delta_{\boldsymbol\kappa}L
=
m\ln3
-
K\ln2
+
C_{\boldsymbol\kappa}(n_0),
}
$$

where:

$$
\boxed{
C_{\boldsymbol\kappa}(n)
=
\ln\left(
1+\frac{
B_{\boldsymbol\kappa}
}{
3^mn
}
\right).
}
$$

---

# 16. Properties of the Correction

For:

$$
m\ge1,
$$

$$
B_{\boldsymbol\kappa}>0.
$$

Therefore:

$$
C_{\boldsymbol\kappa}(n)>0.
$$

And:

$$
\boxed{
C_{\boldsymbol\kappa}(n)\to0
\quad(n\to\infty)
}
$$

holds for a fixed valuation word.

Thus:

$$
\boxed{
m\ln3-K\ln2
}
$$

is the exact asymptotic skeleton drift.

---

# 17. Valuation Contraction Boundary

Requiring:

$$
3^m<2^K.
$$

Taking:

$$
\log_2:
$$

$$
m\log_2 3<K.
$$

That is:

$$
\boxed{
\frac Km>\log_2 3.
}
$$

where:

$$
\boxed{
\log_2 3
\approx1.5849625007.
}
$$

---

# 18. Equivalence with the Boundary in Paper 05

Paper 05:

$$
\frac uk
<
\frac{\ln2}{\ln3}.
$$

The valuation expansion gives:

$$
u=m,
$$

$$
k=K.
$$

Therefore:

$$
\frac mK
<
\frac{\ln2}{\ln3}.
$$

Taking the reciprocal:

$$
\boxed{
\frac Km
>
\frac{\ln3}{\ln2}
=
\log_2 3.
}
$$

Thus, the contraction boundaries in both papers are completely identical.

---

# 19. Exact Descent Criterion

From:

$$
S^m(n)
=
\frac{3^mn+B}{2^K},
$$

we have:

$$
S^m(n)<n
$$

iff:

$$
\boxed{
B_{\boldsymbol\kappa}
<
(2^K-3^m)n.
}
$$

So if:

$$
2^K>3^m,
$$

define:

$$
\boxed{
\theta_{\boldsymbol\kappa}
=
\left\lfloor
\frac{
B_{\boldsymbol\kappa}
}{
2^K-3^m
}
\right\rfloor+1.
}
$$

Then:

$$
n\ge\theta_{\boldsymbol\kappa}
$$

and the valuation word is admissible,

this guarantees:

$$
\boxed{
S^m(n)<n.
}
$$

---

# 20. Uniform Expansion

If:

$$
2^K<3^m,
$$

then:

$$
(3^m-2^K)n>0,
$$

and:

$$
B_{\boldsymbol\kappa}>0.
$$

Therefore:

$$
\boxed{
S^m(n)>n
}
$$

for all positive $n$ on that admissible valuation segment.

Thus, the valuation language similarly possesses a strict two-sided finite-word classification.

---

# 21. One-Step Valuation Residue Theorem

Now we study how:

$$
\kappa(n)=v_2(3n+1)
$$

is distributed among odd residue classes.

Requiring:

$$
v_2(3n+1)=j
$$

is equivalent to:

$$
3n+1
\equiv
2^j
\pmod{2^{j+1}}.
$$

Therefore:

$$
\boxed{
3n
\equiv
2^j-1
\pmod{2^{j+1}}.
}
$$

Since:

$$
3
$$

in:

$$
\mathbb Z/2^{j+1}\mathbb Z
$$

is a unit,

there is exactly one unique solution:

$$
\boxed{
n
\equiv
3^{-1}(2^j-1)
\pmod{2^{j+1}}.
}
$$

This residue is automatically odd.

---

# 22. Exact Residue Density

Modulo:

$$
2^{j+1}
$$

there are a total of:

$$
2^j
$$

odd residue classes.

Exactly one of them satisfies:

$$
v_2(3n+1)=j.
$$

Therefore, the natural residue density among odd integers is:

$$
\boxed{
\delta_j
=
2^{-j}.
}
$$

Thus:

$$
\boxed{
\sum_{j=1}^{\infty}\delta_j=1.
}
$$

This is an exact arithmetic density law.

---

# 23. Mean Valuation = 2

From:

$$
\delta_j=2^{-j},
$$

we obtain:

$$
\boxed{
\sum_{j=1}^\infty
j2^{-j}
=
2.
}
$$

Therefore:

$$
\boxed{
\mathbb E_{\mathrm{res}}[\kappa]=2.
}
$$

The expectation here refers to:

> the natural density distribution over odd residue classes.

It does not claim that $\kappa_i$ on an actual orbit are independent random variables.

---

# 24. Correction of the Old "Average Division by 2 Depth is About 2"

Thus, the old research statement:

> $v_2(3n+1)$ averages about 2

can be rewritten into a precise version:

$$
\boxed{
\text{one-step odd-residue valuation distribution is geometric with mass }2^{-j}.
}
$$

Therefore, the mean is exactly:

$$
2.
$$

This is stronger and clearer than the heuristic statement.

---

# 25. Ensemble Skeleton Drift

If we only average the skeleton over the one-step residue ensemble:

$$
\ln3-\kappa\ln2,
$$

then:

$$
\mathbb E_{\mathrm{res}}
[
\ln3-\kappa\ln2
]
$$

$$
=
\ln3
-
2\ln2.
$$

Therefore:

$$
\boxed{
\mathbb E_{\mathrm{res}}[\Delta L_{\mathrm{skeleton}}]
=
\ln\frac34
<0.
}
$$

This precisely explains the origin of the Collatz negative drift heuristic.

---

# 26. But the Correction is Still Positive

The one-step exact drift is:

$$
\ln S(n)-\ln n
=
\ln3
-
\kappa(n)\ln2
+
\ln\left(
1+\frac1{3n}
\right).
$$

The last term:

$$
\boxed{
\ln\left(
1+\frac1{3n}
\right)>0.
}
$$

But:

$$
\to0
$$

as:

$$
n\to\infty.
$$

Therefore, "$3/4$" is the large-$n$ skeleton mean,

not the exact multiplier for every finite $n$.

---

# 27. The Biggest Quantifier Warning: Residue Density ≠ Orbit Independence

Even if:

$$
\Pr_{\mathrm{res}}(\kappa=j)=2^{-j},
$$

one cannot directly assume that on the same orbit:

$$
\kappa_1,\kappa_2,\ldots
$$

are independent geometric samples.

Because:

$$
n_{i+1}
=
S(n_i)
$$

is determined by the previous state.

Thus, the valuation sequence has arithmetic dependence.

Therefore:

$$
\boxed{
\text{exact one-step marginal}
\not\Rightarrow
\text{i.i.d. orbit process}.
}
$$

---

# 28. Why is Tao's Result Much Deeper Than "Average = 2"?

Tao's almost-all theorem for the closely related Syracuse iteration does not simply treat valuations as independent geometric random variables.

His proof involves:

- first-passage random variables;
- approximate transport;
- skew random walks;
- $3$-adic cyclic groups;
- Fourier decay;
- renewal processes.

Therefore:

$$
\boxed{
\text{negative one-step ensemble drift}
}
$$

is merely an intuitive entry point,

not a substitute for the almost-all theorem.

---

# 29. Valuation-Order Correction

For:

$$
\boldsymbol\kappa
=
(\kappa_1,\ldots,\kappa_m),
$$

$$
B_{\boldsymbol\kappa}
=
\sum_{i=1}^m
3^{m-i}2^{K_{i-1}}.
$$

Fixing:

$$
m,K,
$$

is still insufficient to determine:

$$
B_{\boldsymbol\kappa}.
$$

Because:

$$
K_{i-1}
$$

depends on the valuation order.

---

# 30. Adjacent Valuation Swap Theorem

Assume at positions:

$$
i,i+1
$$

we have:

$$
a,b,
$$

with the preceding cumulative valuation:

$$
P=K_{i-1}.
$$

Compare:

$$
\boldsymbol\kappa
=
(\ldots,a,b,\ldots)
$$

and:

$$
\boldsymbol\kappa'
=
(\ldots,b,a,\ldots).
$$

Both have exactly the same:

$$
m
$$

and:

$$
K
$$

Since the total valuation of the swapped pair:

$$
a+b
$$

remains unchanged,

all prefix sums after the pair remain the same.

The only difference is the second injection term within the pair.

Therefore:

$$
\boxed{
B_{\boldsymbol\kappa}
-
B_{\boldsymbol\kappa'}
=
3^{m-i-1}
2^P
(2^a-2^b).
}
$$

---

# 31. Ordering Corollary

If:

$$
a>b,
$$

then:

$$
2^a-2^b>0.
$$

Therefore:

$$
\boxed{
B_{(\ldots,a,b,\ldots)}
>
B_{(\ldots,b,a,\ldots)}.
}
$$

Thus, for a fixed valuation multiset:

$$
\boxed{
\kappa_1\le\kappa_2\le\cdots\le\kappa_m
}
$$

minimizes the correction,

while:

$$
\boxed{
\kappa_1\ge\kappa_2\ge\cdots\ge\kappa_m
}
$$

maximizes the correction.

---

# 32. Significance of This Result

A larger valuation means that:

$$
3n+1
$$

has more powers of 2 to divide out.

Intuitively, it seems that "an earlier large valuation is more favorable for descent."

But for a fixed total:

$$
K,
$$

the main drift:

$$
3^m/2^K
$$

is already fixed.

The earlier a larger valuation appears,

the more it places subsequent $+1$ injections under a larger prefix power:

$$
2^{K_{i-1}},
$$

thereby increasing the affine correction:

$$
B_{\boldsymbol\kappa}.
$$

This does not mean that an early large valuation is overall harmful,

but rather:

> in a comparison with fixed $(m,K)$, the order only leaves a finite correction effect, and early concentration makes the correction larger.

---

# 33. Skeleton vs. Correction Separated Again

Therefore:

$$
\boxed{
(m,K)
}
$$

determines the:

$$
\text{asymptotic side},
$$

while the arrangement of:

$$
\boxed{
(\kappa_1,\ldots,\kappa_m)
}
$$

determines the:

$$
\text{finite threshold}.
$$

This exactly parallels Paper 02:

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

---

# 34. Exact Reverse Step

Given an odd target:

$$
t,
$$

and valuation:

$$
\kappa\ge1,
$$

If:

$$
S(n)=t
$$

and:

$$
v_2(3n+1)=\kappa,
$$

then:

$$
3n+1
=
2^\kappa t.
$$

Therefore:

$$
\boxed{
n
=
R_\kappa(t)
=
\frac{2^\kappa t-1}{3}.
}
$$

---

# 35. Reverse Legality

$R_\kappa(t)$ is an integer iff:

$$
\boxed{
2^\kappa t\equiv1\pmod3.
}
$$

If this holds and:

$$
t>0
$$

is odd,

then the numerator is odd,

hence the predecessor is also odd.

Thus, it gives the exact odd inverse fiber.

---

# 36. Multi-Step Reverse Recovery

If the valuation word:

$$
(\kappa_1,\ldots,\kappa_m)
$$

and the terminal odd state:

$$
t=n_m
$$

are reverse-admissible,

then step-by-step:

$$
n_{m-1}=R_{\kappa_m}(n_m),
$$

$$
n_{m-2}=R_{\kappa_{m-1}}(n_{m-1}),
$$

down to:

$$
n_0.
$$

Since $\kappa$ is fixed at each step,

the inverse is single-valued.

---

# 37. Closed Reverse Formula

From the forward equation:

$$
2^K n_m
=
3^m n_0
+
B_{\boldsymbol\kappa},
$$

we have:

$$
\boxed{
n_0
=
\frac{
2^K n_m
-
B_{\boldsymbol\kappa}
}{
3^m}.
}
$$

Therefore, for a reverse-admissible word:

$$
\boxed{
\text{valuation encoding is losslessly invertible}.
}
$$

---

# 38. Why Must We Still Retain Recursive Legality?

Merely checking that the final closed fraction:

$$
\frac{
2^K t-B
}{
3^m}
$$

is an integer

should not automatically be equated, without proof, to:

> every intermediate reverse state satisfies the corresponding valuation legality.

Therefore, a rigorous inverse procedure should retain:

$$
\boxed{
R_{\kappa_m},
R_{\kappa_{m-1}},
\ldots,
R_{\kappa_1}
}
$$

step-by-step legality checks.

The closed formula is a recovery identity,

not a license to skip intermediate admissibility.

---

# 39. Reinterpretation of the Terminal Fiber

Take:

$$
t=1
$$

and a single valuation:

$$
\kappa=2j.
$$

From:

$$
2^{2j}\equiv1\pmod3,
$$

we obtain:

$$
\boxed{
R_{2j}(1)
=
\frac{4^j-1}{3}.
}
$$

Thus, the old:

$$
M_j
$$

series is exactly the even-valuation inverse fiber of the terminal state 1.

This was already established in Paper 04;

this paper places it into the complete valuation language.

---

# 40. Valuation-Labeled Odd Skeleton

The accelerated odd inverse graph can be denoted as:

$$
n
\xrightarrow{\kappa}
t
$$

iff:

$$
\boxed{
3n+1=2^\kappa t.
}
$$

So each edge inherently carries the label:

$$
\boxed{
\kappa=v_2(3n+1)
}
$$

An odd skeleton path:

$$
n_0\to n_1\to\cdots\to n_m
$$

thus naturally corresponds to:

$$
\boxed{
(\kappa_1,\ldots,\kappa_m).
}
$$

This is the graph-theoretic version of the valuation language.

---

# 41. How Should the Old "Dissipation" Language Be Retained?

We can retain the intuition that:

$$
3
$$

is the amplification of one odd update,

while:

$$
2^\kappa
$$

is its valuation-controlled contraction.

But rigorous mathematics no longer says:

> "Dissipation inevitably defeats input."

Instead, it says:

$$
\boxed{
\text{for a fixed finite valuation word, the exact skeleton multiplier is }
\frac{3^m}{2^K}.
}
$$

Whether it descends or not is precisely determined by:

$$
2^K\gtrless3^m
$$

---

# 42. What Does This Paper Not Prove?

This paper does not prove that:

$$
\frac{K_m}{m}>\log_2 3
$$

eventually holds for every sufficiently long ordinary positive-integer orbit.

It does not prove that:

$$
\kappa_i
$$

are independent along the orbit.

It does not deduce universal convergence from:

$$
\mathbb E_{\mathrm{res}}\kappa=2
$$

It does not rule out exceptional valuation words.

This paper only strictly stratifies:

- finite valuation trajectories;
- one-step residue density;
- exact drift;
- exact correction;
- inverse recovery.

---

# 43. Summary of Main Theorems in This Paper

## Theorem A — Valuation Run-Length Encoding

$$
\boxed{
E(\boldsymbol\kappa)
=
UD^{\kappa_1-1}
\cdots
UD^{\kappa_m-1},
}
$$

and:

$$
|E|=K,\qquad u(E)=m.
$$

## Theorem B — Accelerated Affine Closure

$$
\boxed{
S^m(n)
=
\frac{
3^mn+B_{\boldsymbol\kappa}
}{
2^K}.
}
$$

## Theorem C — Correction Closed Form

$$
\boxed{
B_{\boldsymbol\kappa}
=
\sum_{i=1}^{m}
3^{m-i}2^{K_{i-1}}.
}
$$

## Theorem D — Exact Log Drift

$$
\boxed{
\Delta L
=
m\ln3-K\ln2
+
\ln\left(
1+\frac{B_{\boldsymbol\kappa}}{3^mn}
\right).
}
$$

## Theorem E — Valuation Contraction Boundary

$$
\boxed{
2^K>3^m
\iff
K/m>\log_2 3.
}
$$

## Theorem F — One-Step Valuation Density

$$
\boxed{
\delta(\kappa=j)=2^{-j},
\qquad
\mathbb E_{\mathrm{res}}\kappa=2.
}
$$

## Theorem G — Adjacent Valuation Swap

$$
\boxed{
\Delta B
=
3^{m-i-1}2^{K_{i-1}}
(2^a-2^b).
}
$$

## Theorem H — Exact Reverse Recovery

$$
\boxed{
n_0
=
\frac{
2^K n_m-B_{\boldsymbol\kappa}
}{
3^m}
}
$$

on reverse-admissible valuation words.

---

# 44. Conclusion

The core intuition of the author's early Collatz systems theory was:

> A single $3n+1$ amplification will be offset by the subsequent exponential contraction of multiple divisions by 2.

This paper breaks this statement down into three mathematical layers of different strengths.

The first layer is the completely exact finite-word theorem:

$$
\boxed{
S^m(n)
=
\frac{
3^mn+B_{\boldsymbol\kappa}
}{
2^K}.
}
$$

Therefore:

$$
\boxed{
K/m>\log_2 3
}
$$

precisely determines the contracting skeleton side of a fixed valuation word.

The second layer is the exact one-step residue-density theorem:

$$
\boxed{
\Pr_{\mathrm{res}}(\kappa=j)=2^{-j},
}
$$

Thus:

$$
\boxed{
\mathbb E_{\mathrm{res}}\kappa=2
}
$$

and the skeleton ensemble mean:

$$
\boxed{
\ln3-2\ln2=\ln(3/4)<0.
}
$$

The third layer is the unfinished global orbit problem:

> Can the actual valuation itinerary be universally controlled in a sufficiently strong manner?

This layer cannot be directly deduced from the first two layers.

Therefore, what this paper truly accomplishes is:

$$
\boxed{
\text{old heuristic of average negative drift}
\longrightarrow
\text{exact finite valuation-word drift}
+
\text{separate statistical layer}.
}
$$

At the same time, the valuation order correction shows that:

$$
\boxed{
(m,K)
\text{ determines the main drift,}
}
$$

$$
\boxed{
\text{the arrangement of } (\kappa_1,\ldots,\kappa_m)
\text{ determines the finite correction}.
}
$$

Thus, the accelerated odd dynamics perfectly integrate with the Local Affine Atlas from the previous five papers.

The next paper will replace the Collatz numbers $3,1,2$ with general odd parameters to study:

$$
C_{p,r}(n)
=
\begin{cases}
n/2,\\
(pn+r)/2,
\end{cases}
$$

and find the generalized phase boundary formed by:

$$
\boxed{
\frac{u}{k}
<
\frac{\ln2}{\ln p}
}
$$

as well as the structural bifurcation of cylinder density between $p=3$ and $p\ge5$.

---

# References

1. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562; Forum of Mathematics, Pi 10 (2022).
2. Olivier Rozier, Claude Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948.
3. Tong Niu, *Parity vectors and paradoxical sequences in the accelerated Collatz map*, arXiv:2605.13886.
4. Olivier Rozier, *Parity sequences of the 3x+1 map on the 2-adic integers and Euclidean embedding*, arXiv:1805.00133.
5. Collatz Operation Translation Series — Paper 02, *Collatz Local Affine Atlas: Exact Affinization of Finite Parity Words*.
6. Collatz Operation Translation Series — Paper 03, *Parity Words, Residue Cylinders, and Local Identitization*.
7. Collatz Operation Translation Series — Paper 04, *Bidirectional Residue Class Translation: $2^k$ Cylinders and $3^u$ Progressions*.
8. Collatz Operation Translation Series — Paper 05, *Finite-Word Contraction Boundaries and the Binomial Cylinder Law*.

---

## Next Paper

**Paper 07 — *Generalized $mx+r$ Systems and Residue-Class Operation Translation***

Core Tasks:

1. Generalize $3n+1$ to a general odd $mn+r$;
2. Prove the finite-word affine closure;
3. Derive the generalized correction;
4. Establish the unit condition for word–residue legality;
5. Derive:
   $$
   \frac uk<\frac{\ln2}{\ln m};
   $$
6. Compare $m=1,3,5,7,\ldots$;
7. Establish the typical cylinder phase boundary for $m<4$ / $m>4$;
8. Clearly define which conclusions are Collatz-specific and which belong to the more general Residue-Class Operation Translation.