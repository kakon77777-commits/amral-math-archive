# 13 — Test-Specific Weighted Pair-Correlation Hypothesis
## $P_{70}$ Does Not Require the Full Hardy–Littlewood: Only a High-Leverage Weighted Moment is Needed

**Date:** 2026-08-11  
**Status:** source-grounded derivation + new conditional schema  
**Important Distinctions:**
- Claude Proposition 5.6's $O_1$ formula and $\sigma>1$ requiring prime-pair information are directly supported by the source.
- The relationship between Goldston's strong Hardy–Littlewood hypothesis and SPC is directly supported by classical sources.
- The definitions of `WSPC / WPPH` and the concept of "only needing one weighted moment" in this text are **weaker sufficient hypothesis schemas** extracted from these formulas by this research, not the original names or theorems from the sources.

---

# 0. Why is the "Full Hardy–Littlewood" Obviously Too Strong?

Claude §7.5 states that when:

$$
\sigma>1
$$

the off-diagonal term in Proposition 5.6:

$$
O_1
$$

is no longer controlled by the diagonal and requires Hardy–Littlewood-strength prime-pair information, which is equivalently requiring Montgomery pair correlation information at:

$$
\alpha>1
$$

In Goldston's classical notes, the strong prime-pair hypothesis used by Montgomery is:

$$
\sum_{n\le N}
\Lambda(n)\Lambda(n+h)
=
\mathfrak S(h)N
+
O_\varepsilon(N^{1/2+\varepsilon})
$$

uniformly for:

$$
0<h\le N.
$$

This is extremely strong: it requires a square-root level error for **every single shift**.

But to prove:

$$
P_{70},
$$

we do not need to know all test functions, nor do we need to know all shifts.

---

# 1. Goldston's Formula Already Implies "One Test = One Weighted Moment"

The general form of the pair-correlation formula is:

$$
\sum_{\gamma,\gamma'}
R\!\left(
(\gamma-\gamma')
\frac{\log T}{2\pi}
\right)
w(\gamma-\gamma')
$$

Corresponding to the Fourier side:

$$
\int
\widehat R(\alpha)
F(\alpha,T)
\,d\alpha.
$$

Therefore, if we only intend to use **one specific extremal test**:

$$
R_\sigma^\star,
$$

then to run this certificate, the only new zero-pair input truly needed is the correct asymptotic for:

$$
\boxed{
\int_{1<|\alpha|\le\sigma}
\widehat R_\sigma^\star(\alpha)
F(\alpha,T)
\,d\alpha
}
$$

There is no need to first prove:

$$
F(\alpha,T)=1+o(1)
$$

pointwise/uniformly for every:

$$
1<\alpha\le\sigma
$$

---

# 2. Defining WSPC — Weighted Strong Pair Correlation

Let:

$$
R_\sigma^\star
$$

be the generalized one-delta optimizer reconstructed in v8, normalized such that:

$$
R_\sigma^\star(0)=1,
$$

and:

$$
\operatorname{supp}\widehat R_\sigma^\star
\subset[-\sigma,\sigma].
$$

Define:

## WSPC$(\sigma)$

$$
\boxed{
\mathcal J_\sigma(T)
:=
\int_{1<|\alpha|\le\sigma}
\widehat R_\sigma^\star(\alpha)
\left[
F(\alpha,T)-1
\right]d\alpha
=
o(1).
}
$$

This is the **one-test weighted SPC**.

The full SPC:

$$
F(\alpha,T)=1+o(1)
$$

uniformly on the interval, will obviously imply WSPC.

However, WSPC only constrains a single linear functional.

Thus, in terms of information structure:

$$
\boxed{
\mathrm{WSPC}(\sigma)
\ll
\mathrm{SPC}[1,\sigma].
}
$$

Here, $\ll$ means "the required information dimension is much lower," not the Vinogradov notation.

---

# 3. Why is this Single Weighted Moment Enough?

For the optimizer, the pair-correlation second-moment constant can be decomposed into:

$$
C_\sigma
=
\widehat R_\sigma^\star(0)
+
\int_{|\alpha|\le1}
|\alpha|
\widehat R_\sigma^\star(\alpha)\,d\alpha
+
\int_{1<|\alpha|\le\sigma}
\widehat R_\sigma^\star(\alpha)\,d\alpha.
$$

The model value satisfies:

$$
C_\sigma
=
2-q(\sigma).
$$

If the true $F$ in the unknown strip is not $1$, the correction term is:

$$
\mathcal J_\sigma(T).
$$

So the second-moment constant becomes:

$$
C_\sigma+\mathcal J_\sigma(T)+o(1).
$$

Claude's same integrality / rank-trace mechanism will change the proportion to:

$$
q(\sigma)-\mathcal J_\sigma(T)+o(1)
$$

(for a positive error; if $\mathcal J$ is negative, it is actually advantageous).

Therefore:

$$
\boxed{
\mathcal J_\sigma(T)=o(1)
}
$$

is the natural test-specific condition for running the same optimal certificate.

**This section is a conditional reconstruction of this research; to formally elevate it to a Claude paper-style theorem, the generalized-support prime-side trace and its localization errors still need to be written out completely.**

---

# 4. The Surprising Aspect of $P_{70}$: The Test Mass in the Unknown Strip is Actually Extremely Small

Our numerical reconstruction gives:

$$
\sigma_{70}
\approx
1.042628.
$$

For the corresponding optimizer:

$$
\int_{1<|\alpha|\le\sigma}
\widehat R_\sigma^\star(\alpha)\,d\alpha
\approx
0.00114.
$$

Which is, of the entire normalized Fourier mass:

$$
\boxed{
\approx0.114\%.
}
$$

Therefore, $P_{70}$ is highly unique from an information-theoretic perspective:

- the support indeed must cross $1$;
- but the total Fourier mass of the unknown strip actually used by the optimal test is only about one-thousandth.

This reinforces an important observation:

$$
\boxed{
\text{The difficulty comes from "crossing the boundary," not from "needing a large new band."}
}
$$

---

# 5. As the Proportion Increases, the Unknown-Band Dependence Grows Rapidly

The same numerical diagnostics:

| target | $\sigma$ | optimizer Fourier mass in $|\alpha|>1$ |
|---:|---:|---:|
| $70\%$ | $1.04263$ | $\approx0.114\%$ |
| $80\%$ | $1.25785$ | $\approx2.89\%$ |
| $90\%$ | $1.70146$ | $\approx12.36\%$ |
| $95\%$ | $2.26079$ | $\approx24.32\%$ |
| $99\%$ | $4.18722$ | $\approx51.07\%$ |

So:

$$
P_{70}
$$

and:

$$
P_{99}
$$

are not "doing the same thing a few more times."

By $99\%$, about half of the Fourier mass of the optimal certificate already relies on the unknown pair-correlation region of:

$$
|\alpha|>1
$$

---

# 6. Practical Version: No Need to be Stuck Exactly at $\sigma_{70}$

If we take exactly:

$$
\sigma=1.042628,
$$

the model certificate is almost exactly:

$$
q=0.70.
$$

Thus, there is no error slack.

It is more practical to take slightly more support.

For example:

## $\sigma=1.05$

Numerically:

$$
q(1.05)
\approx
0.70443.
$$

So as long as the weighted unknown-strip error satisfies:

$$
\boxed{
|\mathcal J_{1.05}(T)|
\le
0.0044+o(1),
}
$$

it is still sufficient to deduce:

$$
P_{70}.
$$

And at this point, the unknown-strip Fourier mass is also only about:

$$
0.154\%.
$$

## $\sigma=1.06$

$$
q(1.06)
\approx
0.71031.
$$

This allows:

$$
|\mathcal J_{1.06}(T)|
\lesssim
0.0103,
$$

while the unknown-strip mass is about:

$$
0.217\%.
$$

So a very natural tradeoff emerges:

$$
\boxed{
\text{Expanding the support slightly}
\leftrightarrow
\text{lowering the arithmetic accuracy requirement}.
}
$$

This can be viewed as CPL's first **support–accuracy frontier**.

---

# 7. The Exact Prime-Side Correspondence: WPPH

Claude Proposition 5.6 gives the exact:

$$
O_1
=
\frac{1}{2\pi^2}
\Re
\sum_{n\ne m}
\frac{a_na_m}{i(\log n-\log m)}
\left[
\left(\frac nm\right)^{2iT}
(\alpha_m^++\alpha_n^-)
-
\left(\frac nm\right)^{iT}
(\alpha_n^++\alpha_m^-)
\right],
$$

where:

$$
a_n
=
\frac{\Lambda(n)}{\sqrt n},
$$

$$
\alpha_n^+
=
\int_0^T
\Phi(x)^2n^{ix}\,dx,
$$

$$
\alpha_n^-
=
\int_{-T}^0
\Phi(x)^2n^{ix}\,dx.
$$

Therefore, we can group:

$$
n=m+h
$$

and write it as:

$$
\boxed{
O_1
=
\sum_{h\ne0}
\sum_m
\Lambda(m)\Lambda(m+h)
K_{T,X,\Phi}(m,h),
}
$$

where $K$ is a smooth / oscillatory weight determined by the exact formula above, which includes:

- $1/\sqrt{m(m+h)}$;
- $1/\log(1+h/m)$;
- endpoint oscillations;
- $\alpha_n^\pm$ window transforms.

---

# 8. Defining WPPH — Weighted Prime-Pair Hypothesis

Let:

$$
O_1^{HL}
$$

denote the model main term obtained by replacing:

$$
\Lambda(m)\Lambda(m+h)
$$

in the **same weight** mentioned above with the Hardy–Littlewood model:

$$
\mathfrak S(h)
$$

(along with the appropriate local density / summation normalization).

Define:

## WPPH$(\sigma,\Phi)$

$$
\boxed{
O_1(T,X,\Phi)
-
O_1^{HL}(T,X,\Phi)
=
o(TL^3),
\qquad
X=T^\sigma.
}
$$

This only requires that **the specific weighted double sum actually used by Claude** is correct.

Pointwise Hardy–Littlewood with a strong uniform error is a sufficient condition;

but WPPH allows:

- errors for different $h$ to cancel each other out;
- cancellations across different $m$ segments;
- not requiring an asymptotic for every shift;
- not requiring it to hold for arbitrary test weights.

So WPPH is the hypothesis we can currently extract from Claude's $O_1$ that is much closer to the actual proof obligation.

---

# 9. The Near-Diagonal Support of $P_{70}$

In the previous round, we deduced:

$$
X=T^\sigma,
$$

and near-diagonal:

$$
h
\sim
\frac XT.
$$

For:

$$
\sigma=1.05,
$$

we get:

$$
h
\sim
T^{0.05}.
$$

On the prime scale:

$$
h
\sim
X^{1-1/1.05}
=
X^{0.047619\ldots}.
$$

Therefore, the practical $P_{70}$ weighted prime-pair input primarily focuses on a very short relative shift scale.

But it must be noted:

> the exact $O_1$ weight still has oscillatory tails; "primarily focuses" does not mean we can directly truncate all larger $h$ without proving a tail bound.

---

# 10. Logical Relationship with Goldston's Strong HL

The strong hypothesis recorded by Goldston requires:

$$
\forall h\le N:
\quad
\sum_{n\le N}
\Lambda(n)\Lambda(n+h)
=
\mathfrak S(h)N
+
O(N^{1/2+\varepsilon}).
$$

WPPH, on the other hand, only requires:

$$
\sum_{h,m}
E(m,h)
K_{T,X,\Phi}(m,h)
=
o(TL^3),
$$

where:

$$
E(m,h)
=
\Lambda(m)\Lambda(m+h)-\text{HL model}.
$$

So the hierarchy can be drawn as:

$$
\boxed{
\text{Strong pointwise HL}
\Rightarrow
\text{full SPC (in its valid range)}
\Rightarrow
\text{WSPC for every chosen test}
}
$$

And in Claude's prime-side formulation:

$$
\boxed{
\text{Strong HL}
\Rightarrow
\text{WPPH}
\Rightarrow
\text{test-specific trace evaluation}.
}
$$

The converses do not hold automatically.

---

# 11. The New $P_{70}$ Conditional Target

We now do not need to write the research problem as:

> Prove Hardy–Littlewood.

It can be changed to:

## WPPH-$70$

Choose:

$$
\sigma=1.05
$$

and its optimized one-delta window.

Prove that for the exact weight generated by Claude Proposition 5.6:

$$
K_{T,T^{1.05},\Phi^\star_{1.05}}
$$

we have:

$$
\boxed{
\left|
O_1-O_1^{model}
\right|
\le
(0.004+\!o(1))
\times
(\text{normalized second-moment scale}).
}
$$

Once fully integrated with the generalized trace normalization, this should already be sufficient to maintain:

$$
q\ge0.70.
$$

This is a much weaker requirement than the "full HL," and also much closer to the information actually used in the proof than requiring the full:

$$
F(\alpha)=1
$$

on $[1,1.05]$.

---

# 12. Next Steps

There are two things most worth doing now:

## A. Kernel extraction

Further simplify:

$$
K_{T,X,\Phi}(m,h)
$$

from Proposition 5.6 to find its leading near-diagonal kernel.

Goal:

$$
K_{T,X,\Phi}(m,h)
\approx
W_\Phi(m/X,hT/X)
$$

or a similar rescaled form.

This will turn WPPH into an expression that can truly be compared with the average Hardy–Littlewood literature.

## B. Existing theorem matching

Search for currently proven average prime-pair / Selberg-integral / short-interval variance bounds to see if there are already results that can control:

$$
\sum_{h,m}E(m,h)K(m,h)
$$

enough to yield $q>67.25\%$, even if it cannot yet reach $70\%$.

If we can unconditionally push past:

$$
68.185\%
$$

it would be more important than a conditional $70\%$.