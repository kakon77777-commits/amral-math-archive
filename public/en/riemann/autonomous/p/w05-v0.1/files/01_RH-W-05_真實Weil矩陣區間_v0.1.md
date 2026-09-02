# RH-W-05: The First Authentic Weil Matrix Rational Enclosure
## From Floating-Point Candidates to a Replayable $2\times2$ Mathematical Receipt

**Version:** v0.1  
**Date:** 2026-07-23  
**Research Project:** RH GAP Atlas / AI Mathematical Engineering Relay  
**Parent Node:** `RH-W-04-GALERKIN-CERTIFICATE`  
**Current Node:** `RH-W-05-REAL-MATRIX-ENCLOSURE`  
**Status:** `CLOSED_FOR_PRIME_FREE_2D_SPLINE_BASIS`  
**Nature:** Finite-dimensional rigorous computation of the authentic Riemann zeta Weil functional; neither an RH proof nor an RH counterexample

---

# 0. Conclusion of the Current Round

This round completes the first authentic Weil matrix that does not rely on synthetic zeros, does not use finite zero truncation, and does not treat ordinary floating-point errors as certificates:

$$
M_{ij}=Q_W(v_i,v_j)=W(v_i*\widetilde v_j),
\qquad 1\le i,j\le2.
$$

The computation employs the complete Riemann–Weil explicit formula and bounds each term with rational enclosures. We obtain:

$$
M_{11}=M_{22}
\in
[0.42142579326768431214,\,
 0.42433406315905086714],
$$

$$
M_{12}=M_{21}
\in
[-0.17344762492928894604,\,
 -0.17288215757817251839].
$$

Due to the translational symmetry of the matrix, the two exact modes are:

$$
(1,1),\qquad(1,-1).
$$

Their quadratic form enclosures are respectively:

$$
Q_W(1,1)
=M_{11}+M_{12}
\in
[0.24797816833839535493,\,
 0.25145190558087834875],
$$

$$
Q_W(1,-1)
=M_{11}-M_{12}
\in
[0.59430795084585680927,\,
 0.59778168808833981318].
$$

Therefore:

$$
\boxed{
Q_W(v)>0
\quad
\text{for all } v\ne0 \text{ in the 2D subspace fixed in this round}
}
$$

This is merely a **finite-dimensional local positivity certificate**:

$$
\boxed{
\text{Finite-dimensional positivity}\not\Longrightarrow RH
}
$$

Its milestone significance is: authentic Weil matrix elements can now be generated along a complete pipeline of "formula—enclosure—certificate—small verifier".

---

# 1. Fixing the Explicit Formula

In additive coordinates, for an appropriate test function $f$, this engineering project fixes the Weil functional as:

$$
\begin{aligned}
W(f)
={}&
\int_{-\infty}^{\infty}
f(x)\left(e^{x/2}+e^{-x/2}\right)\,dx
\\
&-
\sum_{n\ge1}
\frac{\Lambda(n)}{\sqrt n}
f(\log n)
-
\sum_{n\ge1}
\frac{\Lambda(n)}{\sqrt n}
f(-\log n)
\\
&-
(\log4\pi+\gamma)f(0)
\\
&-
\int_0^\infty
\frac{
e^{x/2}\bigl(f(x)+f(-x)\bigr)-2f(0)
}{e^x-e^{-x}}\,dx.
\end{aligned}
$$

This is the equivalent version in additive coordinates of the Bombieri/Clay explicit formula in multiplicative coordinates. For real functions $v_i,v_j$, we fix:

$$
\widetilde v_j(x)=v_j(-x),
$$

$$
f_{ij}=v_i*\widetilde v_j,
$$

$$
M_{ij}=W(f_{ij}).
$$

If RH holds, the diagonal form can be written as a sum of squared moduli over the zeros, and thus must be non-negative. Therefore, any strictly negative direction is sufficient to negate RH; conversely, positivity in finitely many directions does not provide a proof of RH.

---

# 2. Why Choose B-splines First

The first version does not pursue the strongest search capability, but rather the following engineering properties:

1. Compact support;
2. Piecewise polynomial;
3. Closed-form computation of convolutions;
4. Sufficient decay in the Fourier transform;
5. All integrals can be reduced to "rational polynomials multiplied by exponentials";
6. The ability to rewrite integration errors as analytic tail bounds, rather than trusting the self-reported errors of integrators.

Define the centered cardinal cubic B-spline:

$$
\beta_3(x)
=
\frac1{3!}
\sum_{k=0}^{4}
(-1)^k{4\choose k}(x+2-k)_+^3.
$$

It satisfies:

$$
\operatorname{supp}(\beta_3)=[-2,2].
$$

Let:

$$
h=\frac1{20},
$$

$$
t_1=-\frac1{20},
\qquad
t_2=\frac1{20},
$$

and define:

$$
v_i(x)
=
h^{-1/2}
\beta_3\!\left(\frac{x-t_i}{h}\right).
$$

Both functions are supported on:

$$
\left[-\frac3{20},\frac3{20}\right].
$$

Using the convolution identity of cardinal B-splines:

$$
\beta_m*\beta_n=\beta_{m+n+1},
$$

we obtain:

$$
\boxed{
f_{ij}(x)
=
\beta_7\!\left(
\frac{x-(t_i-t_j)}{h}
\right)
}.
$$

Thus, all matrix elements only require handling degree-$7$ piecewise polynomials.

---

# 3. Exact Exclusion of Prime Terms

The support of the diagonal correlation functions is:

$$
\operatorname{supp}(f_{11})
=
\operatorname{supp}(f_{22})
=
\left[-\frac15,\frac15\right].
$$

The cross-correlation function extends at most to:

$$
\left|x\right|\le\frac3{10}.
$$

The program proves via a rational atanh series that:

$$
\log2>\frac3{10}.
$$

Therefore, for all $n\ge2$:

$$
|\log n|
\ge\log2
>\frac3{10},
$$

Hence:

$$
f_{ij}(\log n)=f_{ij}(-\log n)=0.
$$

Since $\Lambda(1)=0$, we have:

$$
\boxed{
M_{ij}^{\rm prime}=0
}
$$

This is an analytic conclusion, not an empirical observation that "the program failed to list any primes."

This is a deliberate first-stage design: first get the complete explicit formula pipeline running, and then in the next version expand the support beyond $\log2$ to activate authentic prime sampling.

---

# 4. Summable Series for the Archimedean Integral

Let:

$$
F(x)=f(x)+f(-x),
\qquad
f_0=f(0).
$$

The Archimedean integral is:

$$
A(f)
=
-
\int_0^\infty
\frac{e^{x/2}F(x)-2f_0}
{e^x-e^{-x}}\,dx.
$$

Using:

$$
\frac1{e^x-e^{-x}}
=
\sum_{k=0}^\infty e^{-(2k+1)x},
\qquad x>0,
$$

we obtain:

$$
A(f)
=
-
\sum_{k=0}^\infty
\left[
\int_0^r
F(x)e^{-(2k+1/2)x}\,dx
-
\frac{2f_0}{2k+1}
\right],
$$

where $r$ is the support radius of $F$ on the positive half-axis.

Viewed individually, both parts have a $1/k$ principal term, but the difference inside the brackets cancels out this divergent term, and the sum starts at $1/k^2$.

Here, one cannot compute the two divergent series separately and then subtract them; the program must maintain the bracketed structure term by term. Violations are flagged as:

```text
INVALID_DIVERGENT_SPLIT
```

---

# 5. Tail Bound via Six-Fold Integration by Parts

Let:

$$
a_k=2k+\frac12,
\qquad
b_k=2k+1.
$$

For:

$$
I(a)=\int_0^rF(x)e^{-ax}\,dx,
$$

Since $F$ is an even function and the B-spline vanishes to a sufficient order at the endpoints of its support, six-fold integration by parts yields:

$$
I(a)
=
\frac{F(0)}a
+
\frac{F''(0)}{a^3}
+
\frac{F^{(4)}(0)}{a^5}
+
R_6(a),
$$

where:

$$
|R_6(a)|
\le
\frac{\|F^{(6)}\|_\infty}{a^7}.
$$

Because:

$$
F(0)=2f_0,
$$

each tail term satisfies:

$$
\begin{aligned}
\left|
I(a_k)-\frac{2f_0}{b_k}
\right|
\le{}&
\frac{|F(0)|}{8k^2}
+
\frac{|F''(0)|}{8k^3}
\\
&+
\frac{|F^{(4)}(0)|}{32k^5}
+
\frac{\|F^{(6)}\|_\infty}{128k^7}.
\end{aligned}
$$

Then, using a purely rational integral comparison:

$$
\sum_{k=K}^\infty\frac1{k^p}
\le
\frac1{K^p}
+
\frac1{(p-1)K^{p-1}},
$$

we obtain a completely rational total tail bound.

In this round, we take:

$$
K=200.
$$

The tail bound for the diagonal elements is:

$$
\boxed{
B_{\rm tail}^{(11)}
=
\frac{19463441}{13440000000}
\approx0.00144817269345
},
$$

The tail bound for the cross elements is:

$$
\boxed{
B_{\rm tail}^{(12)}
=
\frac{7591921}{26880000000}
\approx0.000282437537202
}.
$$

These tail bounds are relatively loose, but they are already sufficient to rigorously determine the positivity of this 2D space. In the future, they can be tightened by increasing the order of integration by parts or computing more series terms.

---

# 6. Sources of Rational Enclosures

## 6.1 Integrals of Piecewise Polynomials

All finite integrals are reduced to:

$$
\int_l^uP(x)e^{\lambda x}\,dx,
$$

where $P$ is a polynomial with rational coefficients, and $l, u, \lambda$ are all finite decimal rational numbers.

The program exactly computes a polynomial $R$ such that:

$$
R'(x)+\lambda R(x)=P(x),
$$

Therefore:

$$
\int_l^uP(x)e^{\lambda x}\,dx
=
e^{\lambda u}R(u)-e^{\lambda l}R(l).
$$

Only the exponential function requires a transcendental enclosure.

## 6.2 Exponential Function

All exponential inputs have terminating decimal expansions. The program uses the "correctly rounded" contract of CPython's `Decimal.exp()`, expands the result to the adjacent representable Decimals above and below, and then exactly converts them into rational numbers.

Thus, the software trust base is:

```text
CPython 3.13.5
libmpdec 2.5.1
Decimal.exp correctly-rounded contract
```

This round is not a fully formalized machine proof; it is a:

```text
RIGOROUS_NUMERICAL_CERTIFICATE
UNDER_DOCUMENTED_SOFTWARE_CONTRACT
```

The next layer can replace the exponential function with a fully self-contained rational Taylor verifier to further reduce the trust base.

## 6.3 $\pi$, $\log$, and Euler's Constant

- $\pi$: Machin's formula and the arctan alternating series;
- $\log$: atanh positive-term series and analytic tail bounds;
- $\gamma$: Using

  $$
  \frac1{2n+1}
  <H_n-\log n-\gamma
  <\frac1{2n}
  $$

  and taking $n=100$.

These parts are entirely computed using `Fraction` rational arithmetic.

---

# 7. Itemized Enclosure Ledger

## 7.1 Diagonal Elements

$$
M_{11}=M_{22}.
$$

| Component | Decimal Display of Rational Enclosure |
|---|---:|
| Exponential Endpoint Integrals | $[0.10002083539509445953,\ 0.10002083539509445953]$ |
| $-(\log4\pi+\gamma)f(0)$ | $[-1.4899896018750768967,\ -1.4899776773706152611]$ |
| Archimedean Integral | $[1.8113945597476668325,\ 1.8142909051345714744]$ |
| Prime Terms | $[0,0]$ |
| **Total Sum** | $[0.42142579326768431214,\ 0.42433406315905086714]$ |

## 7.2 Cross Elements

| Component | Decimal Display of Rational Enclosure |
|---|---:|
| Exponential Endpoint Integrals | $[0.10014588748860156486,\ 0.10014588748860156486]$ |
| $-(\log4\pi+\gamma)f(0)$ | $[-0.074006106053397857636,\ -0.074005513776686182581]$ |
| Archimedean Integral | $[-0.19958740636449265327,\ -0.19902253129008790067]$ |
| Prime Terms | $[0,0]$ |
| **Total Sum** | $[-0.17344762492928894604,\ -0.17288215757817251839]$ |

Decimals are for readability only. The certificate file stores the complete rational numerators and denominators.

---

# 8. The Gram Matrix is Exactly Rational

From:

$$
G_{ij}
=\langle v_i,v_j\rangle_{L^2}
=f_{ij}(0),
$$

we obtain:

$$
G
=
\begin{pmatrix}
\frac{151}{315} & \frac1{42}\\[4pt]
\frac1{42} & \frac{151}{315}
\end{pmatrix}.
$$

Its determinant is:

$$
\det G
=
\frac{12997}{56700}
>0.
$$

Thus, the two basis functions are linearly independent, and the 2D subspace is not a degenerate representation.

---

# 9. Independent Floating-Point Crosscheck

Another completely different `mpmath` implementation, performing 80-digit precision computations directly on the original integrals, yields:

$$
M_{11}^{\rm float}
=
0.42311359228192251613851204858\ldots,
$$

$$
M_{12}^{\rm float}
=
-0.17344518442309131614786074708\ldots.
$$

Both fall within the rational enclosures.

This floating-point program is solely for crosschecking:

```text
INDEPENDENT_FLOATING_CROSSCHECK_ONLY
```

It does not participate in the logic establishing the certificate.

---

# 10. What Was Truly Closed in This Round

What was closed in this round is:

$$
\boxed{
\text{Authentic zeta Weil elements}
\longrightarrow
\text{Rational enclosure matrix}
\longrightarrow
\text{exact verifier}
}
$$

Within the following restricted scope:

- 2D;
- Translated cubic B-spline basis;
- Maximum correlation support less than $\log2$;
- Prime terms are therefore zero;
- Archimedean tail enclosed via six-fold integration by parts;
- Exponential function relies on the CPython Decimal correctly-rounded contract.

What remains unclosed is:

1. Active prime terms once the support crosses $\log2$;
2. Enclosure explosion control for high-dimensional matrices;
3. Automatic rationalization and sparsification of floating-point eigenvectors;
4. Finding any authentic negative direction;
5. Fully formalizing the transcendental function backend.

---

# 11. GAP Status

| GAP | Status | Description |
|---|---|---|
| `RH-W-05-FORMULA-LOCK` | `CLOSED` | Clay/Suzuki explicit formula notation aligned |
| `RH-W-05-SPLINE-ADMISSIBILITY` | `CLOSED_FOR_W_CLASS` | Correlation functions are $C^6$ compactly supported piecewise polynomials, meeting explicit formula requirements |
| `RH-W-05-PRIME-EMPTY` | `CLOSED` | Prime terms exactly excluded by support $<\log2$ |
| `RH-W-05-ARCH-SERIES` | `CLOSED_FOR_CURRENT_BASIS` | Singular integral rewritten as a summable series |
| `RH-W-05-ARCH-TAIL` | `CLOSED_FOR_ORDER_6` | Six-fold integration by parts + rational $p$-series tail bound |
| `RH-W-05-TRANSCENDENTAL` | `CLOSED_UNDER_DECIMAL_CONTRACT` | Exponential values enclosed by correctly rounded Decimals |
| `RH-W-05-MATRIX-2D` | `CLOSED_POSITIVE` | 2D Weil matrix is strictly positive definite |
| `RH-W-05-PRIME-ACTIVE` | `OPEN_ENGINEERING` | Non-zero von Mangoldt sampling not yet computed |
| `RH-W-05-HIGH-DIM` | `OPEN_ENGINEERING` | Not yet expanded to high-dimensional dictionaries |
| `RH-W-05-NEGATIVE-WITNESS` | `NOT_FOUND` | No authentic negative witness |
| `RH-W-05-FORMAL-BACKEND` | `OPEN` | Decimal trust not yet replaced by Lean/Coq or a purely rational exp core |

---

# 12. Next Node

The next round will not rush to increase dimensionality, but will first cross the first prime threshold:

$$
\boxed{
\texttt{RH-W-06-PRIME-ACTIVE-MATRIX}
}
$$

Choose the correlation support to satisfy:

$$
\log2<r<\log3,
$$

so that in the explicit formula, only the von Mangoldt term for:

$$
n=2
$$

is activated.

This will establish the first item-by-item verifiable:

$$
\text{Continuous Archimedean terms}
+
\text{Discrete prime sampling terms}
$$

mixed matrix certificate.

This has more engineering value than directly enlarging the support to include many primes, because the first discrete jump can be individually observed, verified, and versioned.

---

# 13. Boundary Declaration

This document does not:

- Prove RH;
- Find an RH counterexample;
- Infer global positivity from 2D positivity;
- Infer positivity for all supports from low-support positivity;
- Treat floating-point agreement as a certificate;
- Claim a software correctly-rounded contract as a formal proof.

What this round accomplishes is a mathematical engineering milestone:

> **The first authentic Weil matrix has been materialized from an abstract formula into a replayable, auditable rational enclosure object capable of rejecting false claims.**

---

# 14. Primary Sources

1. Enrico Bombieri, *The Riemann Hypothesis*, Clay Mathematics Institute, Section 5: explicit formula and Weil negativity criterion.
2. Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096, additive-coordinate Weil functional and localized quadratic form.
3. Python Documentation, `decimal` module: `Decimal.exp()` is correctly rounded using `ROUND_HALF_EVEN`.