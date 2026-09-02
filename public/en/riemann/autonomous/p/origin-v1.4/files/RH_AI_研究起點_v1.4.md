# RH AI Research Starting Point v1.4: Kernel Sensitivity-Regularity Duality

- Date: 2026-07-23
- Original Research Concept: Neo.K
- Mathematical Engineering: Aletheia (GPT-5.6 Thinking)
- Status: Non-proof research engineering; no claim that RH is solved

---

## 1. Milestones of This Version

`v1.3` discovered that the cubic B-spline autocorrelation causes the prime-$3$ boundary to soft-start at the seventh order:

$$
p_3(\mu)
\propto
-\mu_+^7.
$$

`v1.4` generalizes this phenomenon to the complete family of centered cardinal B-spline kernels.

For degree-$m$ and degree-$n$ bases:

$$
\beta_m*\beta_n=\beta_{m+n+1}.
$$

Therefore, the activation order of the prime-power support boundary is:

$$
\boxed{r=m+n+1}.
$$

The special case for autocorrelation is:

$$
\boxed{r=2m+1}.
$$

---

## 2. The True Trade-off in Kernel Design

The same $r$ simultaneously controls:

- the local amplitude of the prime boundary $O(\varepsilon^r)$;
- boundary regularity $C^{r-1}$;
- Fourier decay $|\xi|^{-(r+1)}$;
- the conservative Laplace tail bound of this engineering project $O(K^{-r})$.

Therefore:

$$
\text{Smoother}
\Longrightarrow
\text{Easier to certify, but harder to observe new prime layers}.
$$

$$
\text{Sharper}
\Longrightarrow
\text{More sensitive, but tail bounds and condition control are more expensive}.
$$

No single degree is simultaneously optimal.

---

## 3. A Difference of Sixteen Orders of Magnitude

Continuing with the dimensionless penetration depth from `RH-W-10`:

$$
\varepsilon
\approx
4.7510957191\times10^{-4}.
$$

prime-$3$ local elements:

$$
|p_3|_{m=1}
\approx
1.13374\times10^{-11},
$$

$$
|p_3|_{m=3}
\approx
6.87717\times10^{-28}.
$$

Therefore:

$$
\boxed{
\frac{|p_3|_{m=1}}{|p_3|_{m=3}}
\approx1.64856\times10^{16}
}.
$$

The previous near-invisibility of prime-$3$ was not necessarily due to the arithmetic term itself being weak, but rather because the degree-$7$ correlation kernel smoothed out the boundary events.

---

## 4. Next-Generation Dictionary

This version no longer seeks the "optimal single kernel," but adopts a mixed-order architecture:

$$
\boxed{m=1\quad\text{Sensing channel}}
$$

and

$$
\boxed{m=3\quad\text{Certificate channel}}.
$$

Its block correlation orders are:

$$
1\times1\to3,
\qquad
1\times3\to5,
\qquad
3\times3\to7.
$$

The same Hermitian matrix thus simultaneously carries:

$$
\varepsilon^3,
\quad
\varepsilon^5,
\quad
\varepsilon^7
$$

three prime boundary sensing scales.

Next node:

$$
\boxed{
\texttt{RH-W-12-MIXED-ORDER-DICTIONARY}
}.
$$

The goal is to construct the first degree-$1/3$ real Weil block Toeplitz interval matrix and exact Gram certificate.

---

## 5. Scope and Limitations

This version does not contain:

- a proof of RH;
- a true negative witness;
- infinite-dimensional positivity conclusions;
- equating local kernel effects with off-axis zeros of the zeta function.

What this version accomplishes is the engineering of the kernel selection GAP: rewriting "smoother is better" into a computable, comparable, and relayable Pareto problem.