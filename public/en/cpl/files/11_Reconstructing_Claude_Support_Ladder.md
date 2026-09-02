# 11 — Reconstructing Claude's $1.04/1.26/1.70$ Support Ladder
## Generalized One-Delta Extremal Operator and the First Numerical Answer for $99\%$

**Date:** 2026-08-11  
**Status:** Mathematical structure reconstruction + numerical operator solve  
**Important Distinction:**
- The rough thresholds explicitly stated in Claude's paper: $70\%\to1.04$, $80\%\to1.26$, $90\%\to1.70$.
- The more precise values provided in this document, along with $95\%$ and $99\%$, are our numerical reconstructions/extensions based on the same one-delta extremal structure, not new theorems explicitly listed in Claude's paper.

---

# 0. We Found the Generative Mechanism for $1.04/1.26/1.70$

Claude Remark 1.1 states:

$$
70\%\leadsto\sigma\approx1.04,
$$

$$
80\%\leadsto\sigma\approx1.26,
$$

$$
90\%\leadsto\sigma\approx1.70.
$$

Previously, we only knew these three numbers were "roughly" estimated.

Now we can reconstruct the extremal problem they originate from.

Claude §7.1 uses the Montgomery–Taylor / CCLM one-delta extremal at $\sigma=1$:

$$
\min_R
M(R),
$$

where:

$$
M(R)
=
\int_{\mathbb R}
R(x)
\left[
1-
\left(
\frac{\sin\pi x}{\pi x}
\right)^2
\right]dx,
$$

subject to:

$$
R\ge0,
\qquad
R(0)\ge1,
\qquad
\operatorname{supp}\widehat R\subset[-1,1].
$$

Corollary 14 of CCLM gives the exact extremum for $\sigma=1$:

$$
M_{\min}(1)
=
0.3274992\ldots,
$$

Thus, the simple-zero certificate is:

$$
q(1)
=
1-M_{\min}(1)
=
0.6725007\ldots.
$$

This is exactly the $67.25\%$ in Montgomery–Taylor / Claude Theorem D.

---

# 1. Changing the Support to a General $\sigma$

Consider:

$$
\operatorname{supp}\widehat R
\subset[-\sigma,\sigma].
$$

Since:

$$
R=|S|^2,
$$

we can choose $\widehat S=f$ supported on:

$$
I_\sigma
=
[-\sigma/2,\sigma/2].
$$

The constraint:

$$
S(0)=1
$$

becomes:

$$
\int_{I_\sigma}f(t)\,dt=1.
$$

Also, by the Fourier transform identity:

$$
\mathcal F
\left[
\left(
\frac{\sin\pi x}{\pi x}
\right)^2
\right](\xi)
=
(1-|\xi|)_+,
$$

Plancherel's theorem gives:

$$
M(R)
=
\langle f,A_\sigma f\rangle,
$$

where:

$$
A_\sigma
=
I-T_\sigma,
$$

$$
(T_\sigma f)(t)
=
\int_{I_\sigma}
(1-|t-u|)_+
f(u)\,du.
$$

Therefore, the generalized one-delta problem is a quadratic minimisation:

$$
m(\sigma)
=
\min_{\int f=1}
\langle f,A_\sigma f\rangle.
$$

A Lagrange multiplier / reproducing-kernel argument yields:

$$
\boxed{
m(\sigma)
=
\frac{1}{
\langle
\mathbf 1,
A_\sigma^{-1}\mathbf1
\rangle
}.
}
$$

Hence, the simple proportion for the same integrality certificate is:

$$
\boxed{
q(\sigma)
=
1-m(\sigma)
=
1-
\frac{1}{
\langle
\mathbf1,
A_\sigma^{-1}\mathbf1
\rangle
}.
}
$$

This is the support ladder we are looking for.

---

# 2. Why Does $\sigma\le1$ Have Claude's Cosine Closed Form?

If:

$$
\sigma\le1,
$$

then for $t,u\in I_\sigma$, we always have:

$$
|t-u|\le1.
$$

So the kernel is not truncated:

$$
(1-|t-u|)_+
=
1-|t-u|.
$$

The Euler equation can be reduced to a second-order ODE; in the rescaled variable, it is exactly Claude §7.1:

$$
v_\sigma^*(s)
=
\cos(\sqrt2\,\sigma s).
$$

Therefore, Claude's:

$$
c_\sigma^*
=
\frac{
\sqrt2\tan(\sigma/\sqrt2)
}{
1+(\sigma/\sqrt2)\tan(\sigma/\sqrt2)
}
$$

is completely consistent with the operator formula for $\sigma\le1$.

---

# 3. Why Can't We Blindly Extrapolate This Cosine Formula to $\sigma>1$?

This is exactly the pitfall we discovered when we first calculated $90\%$ earlier.

When:

$$
\sigma>1,
$$

there begin to exist points in the interval $I_\sigma$ such that:

$$
|t-u|>1.
$$

At this point, the true kernel is:

$$
\boxed{
(1-|t-u|)_+,
}
$$

not:

$$
1-|t-u|.
$$

Thus, the structure of the operator changes.

If we blindly extend the cosine formula from $\sigma\le1$, the error is still small around $70\%$ and $80\%$, but it becomes severely incorrect at $90\%$.

The true support-extremal problem requires solving a Fredholm equation with a truncated triangular kernel.

This explains:

> why the $90\%$ in the paper is approximately $1.70$, rather than the larger number obtained by directly solving the closed form from §7.1.

---

# 4. Numerical Reconstruction

We use the midpoint Nyström method / sparse linear solve to compute:

$$
A_\sigma^{-1}\mathbf1
$$

and then root-find:

$$
q(\sigma)=q_{\rm target}.
$$

Higher-resolution results:

| target | $\sigma$ |
|---:|---:|
| $70\%$ | $\approx1.04263$ |
| $80\%$ | $\approx1.25785$ |
| $90\%$ | $\approx1.70146$ |
| $95\%$ | $\approx2.26079$ |
| $99\%$ | $\approx4.1872$ |

The first three match Claude's rough estimates:

$$
1.04,\quad1.26,\quad1.70
$$

almost perfectly one by one.

Therefore, we can say with great confidence:

$$
\boxed{
\text{The support numbers in Remark 1.1 are exactly the generalized one-delta extremal ladder.}
}
$$

This is a "numerical reconstruction mechanism," not an explicit formula obtained from the author's supplementary materials.

---

# 5. $99\%$: The First Answerable Number

Claude's paper does not list:

$$
\sigma_{99}.
$$

We now perform a numerical extension along the same generalized one-delta operator.

midpoint discretisation:

$$
n=1000:
\quad
\sigma_{99}\approx4.18714349,
$$

$$
n=1500:
\quad
\sigma_{99}\approx4.18719630,
$$

$$
n=2000:
\quad
\sigma_{99}\approx4.18721495.
$$

Assuming the dominant discretization error is $O(h^2)$, a simple Richardson heuristic gives:

$$
\sigma_{99}
\approx
4.18724.
$$

So the most appropriate way to write this in research currently is:

$$
\boxed{
\sigma_{99}
\approx4.19
\quad
\text{(numerical, same one-delta route)}.
}
$$

Do not write it as an exact theorem constant.

---

# 6. How Does This Result Answer Our Original "Proportionalism"?

Now the CPL ladder can be rewritten as:

$$
67.25\%
\leftrightarrow
\sigma=1,
$$

$$
70\%
\leftrightarrow
\sigma\approx1.043,
$$

$$
80\%
\leftrightarrow
\sigma\approx1.258,
$$

$$
90\%
\leftrightarrow
\sigma\approx1.701,
$$

$$
95\%
\leftrightarrow
\sigma\approx2.261,
$$

$$
99\%
\leftrightarrow
\sigma\approx4.19.
$$

This is a genuine mapping:

$$
\boxed{
\text{Proportion}
\longleftrightarrow
\text{Information Bandwidth}
}
$$

Therefore, the proportion is no longer the "degree of completion of RH," but rather:

> Within this one-delta / pair-correlation certificate class, if the arithmetic side can legitimately provide support up to $\sigma$, how far can the simple-critical proportion certificate be pushed at most?

---

# 7. Important: This is Not an Unconditional Result

Currently, the boundary for truly unconditionally available arithmetic input remains:

$$
\sigma\le1.
$$

Claude §7.5 explicitly states that when exceeding $1$, the prime-side off-diagonal sums require Hardy–Littlewood-strength prime-pair information, equivalently entering the $\alpha>1$ region of Montgomery's PCC.

So:

$$
\sigma_{70}\approx1.043
$$

does not mean "only $4.3\%$ short in computational power."

It represents:

$$
\boxed{
\text{One must cross the structural boundary of current arithmetic information.}
}
$$

---

# 8. Relationship with Our Boundary-Spike Toy Model

The previous toy model found:

$$
\text{open band}
\quad
\Rightarrow
\quad
\text{adversarial boundary spike}.
$$

Now the generalized one-delta operator provides a truly continuous support version:

$$
\sigma=1
\rightarrow
\sigma>1.
$$

The structures of both are consistent:

$$
\boxed{
\text{Increasing the observable frequency band}
\Rightarrow
\text{shrinking the adversarial configuration class}
\Rightarrow
q(\sigma)\uparrow.
}
$$

The single $S(4)$ in the toy model is a discrete probe;

the Fredholm operator is the continuum model that connects back to the true pair-correlation support.

---

# 9. The Next Problem

What is truly worth tackling now is no longer "how much support is actually needed for $99\%$."

We already have the first answer to that numerical problem:

$$
\sigma_{99}\approx4.19.
$$

More importantly:

## Support Realizability Problem

Claude's arithmetic side can currently only strictly achieve:

$$
\sigma\le1.
$$

So for each target:

$$
q\in\{0.70,0.80,0.90,0.99\},
$$

it should be split into two completely different proof obligations:

$$
\boxed{
\text{Extremal requirement }\sigma_q
}
$$

and:

$$
\boxed{
\text{Arithmetic realizability of }\sigma_q
}
$$

The first can now be numerically reconstructed.

The second is the true number-theoretic wall.