# 10 — Refined Exact $B_{70}$ Certificate
## Exact certification remains possible after compressing the safety margin to $8.0\times10^{-8}$

**Date:** 2026-08-11  
**Scope:** $N=4$ continuous-position toy marked-configuration model  
**Status:** exact-rational finite certificate; not a Riemann zeta theorem

---

# 0. New Results

In the previous version, to facilitate exact positivity, the $c_0$ of the numerical dual was adjusted downward by:

$$
5\times10^{-5}.
$$

That yielded:

$$
B_{70}^{cert}
=
3.667777612662112\ldots.
$$

In this round, we continue to shrink the rationalization safety margin.

Ultimately, we use:

$$
\boxed{
\delta
=
\frac{25024291}{312500000000000}
=
8.00777312e-08
}
$$

Which is:

$$
\delta
=
8.00777312\times10^{-8}.
$$

We take:

$$
c_0
=
1.12274224-\delta
=
\frac{350856924975709}{312500000000000}.
$$

The remaining dual coefficients are kept as:

$$
y_1=-0.38437941,
$$

$$
y_2=-0.25114540,
$$

$$
y_3=-0.11796917,
$$

$$
\mu=-0.03068556.
$$

The configuration-wise reduced costs for the three multiplicity patterns can still be proven non-negative using exact-rational Bernstein subdivision.

Therefore:

$$
\boxed{
B_{70}^{cert}
=
\frac{35186790600709}{9589237500000}
=
3.669404433950979\ldots
}
$$

For all:

$$
B\le B_{70}^{cert}
$$

it strictly follows that:

$$
\boxed{
p_{min}(B)\ge0.70.
}
$$

---

# 1. Distance to the Numerical Crossing

The crossing from the previous round of continuous column-generation is approximately:

$$
B_{70}^{num}
\approx3.66941.
$$

Now, the exact value is:

$$
B_{70}^{cert}
=
3.669404433950979.
$$

The difference is approximately:

$$
3.66941-B_{70}^{cert}
\approx
5.56604902e-06.
$$

Which is approximately:

$$
5.6\times10^{-6}
$$

on the scale of $B$.

Thus, the numerical discovery and the exact certificate are already extremely close in the toy model.

---

# 2. Why Can't the Safety Margin Be Exactly Zero?

After decimal rationalization, the original numerical dual is not exactly the precise dual optimum.

For example, the nominal exact-rational quartic of the $(2,2)$ pattern has a very small negative valley, with a value of approximately:

$$
-8.0077731\times10^{-8}.
$$

The minimum negative value of the $(2,1,1)$ nominal polynomial is approximately:

$$
-6.72\times10^{-8}.
$$

Therefore, it is not that the Bernstein method "fails to prove it," but rather:

$$
\boxed{
\text{Directly treating numerical decimals as the exact dual indeed results in minor violations.}
}
$$

This is precisely a small-scale example in the QCI sense:

> A certificate that appears numerically valid must retain a sufficient margin when transitioning into exact arithmetic.

In this round, choosing:

$$
\delta=8.00777312\times10^{-8}
$$

is exactly enough to slightly overcome the worst rationalization defect.

---

# 3. Exact Certification Complexity

Under this minimal margin:

### $(2,2)$

The exact univariate Bernstein subdivision can still terminate.

### $(2,1,1)$

Exact bivariate Bernstein subdivision:

- internal boxes: approx. $131$;
- terminal boxes: approx. $132$.

### $(1,1,1,1)$

Continuing to use the three-variable superset proof after Newton/self-inversive dimensionality reduction:

- internal boxes: $179$;
- terminal boxes: $180$;
- max depth: $13$;
- the minimum terminal Bernstein coefficient is approximately the safety margin:

$$
8.00777312\times10^{-8}>0.
$$

So the fully-simple branch is not the main bottleneck for the threshold; what truly limits the safety margin is the minimal violation of the rationalized dual on the collision patterns.

---

# 4. How Can We Describe the Toy Threshold Now?

Strictly speaking, we can state:

$$
\boxed{
B_{70}^*
\ge
3.669404433950979\ldots
}
$$

where:

$$
B_{70}^*
=
\sup\{
B:p_{min}(B)\ge0.70
}.
$$

Numerical evidence suggests:

$$
B_{70}^*
\approx3.66941.
$$

However, the latter is not yet an upper-bound theorem.

---

# 5. What This Round Truly Taught Us

Originally, we wanted to ask:

> "How does Claude's $67.2\%$ become $70\%$?"

Now, the toy model has evolved into:

$$
\text{numerical dual}
\rightarrow
\text{rationalized dual}
\rightarrow
\text{find exact defect}
\rightarrow
\text{add minimal safety margin}
\rightarrow
\text{exact Bernstein proof}
\rightarrow
\text{certified escape threshold}.
$$

This is a complete, small-scale demonstration of "how an AI mathematical candidate result enters the exact proof domain."

The next step should not be to continue chasing the seventh or eighth decimal place of $B$, but rather to replace the single boundary row:

$$
S(4)
$$

with a true **continuous support strip**:

$$
\alpha\in[1,1+\delta].
$$

Only then will we begin to align with Claude's actual:

$$
\sigma_{70}\approx1.04
$$

and enter the same type of quantitative problem.