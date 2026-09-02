# 09 — Exact $P_{70}$ Boundary-Escape Certificate
## $N=4$ continuous toy model strictly crosses $70\%$ for the first time

**Date:** 2026-08-11  
**Status:** exact-rational finite certificate  
**Important limitation:** This is our defined $N=4$ toy marked-configuration theorem, not a new theorem on the Riemann zeta zeros.

---

# 0. Main Results

Consider the total multiplicity:

$$
N=4,
$$

marks:

$$
m_i\in\{1,2\},
$$

and positions that can be continuously located on the unit circle.

Let:

$$
S(j)
=
\frac14
\left|
\sum_i m_i e^{ij\theta_i}
\right|^2.
$$

For any probability law over configurations, assume:

$$
\mathbb E[S(1)]=\frac14,
$$

$$
\mathbb E[S(2)]=\frac12,
$$

$$
\mathbb E[S(3)]=\frac34,
$$

and:

$$
\mathbb E[S(4)]\le B.
$$

We can now rigorously prove using an exact-rational dual + exact-rational Bernstein subdivision that:

$$
\boxed{
B
\le
\frac{11254781}{3068556}
}
$$

That is, when:

$$
\boxed{
B\le3.667777612662112\ldots
}
$$

we must have:

$$
\boxed{
\mathbb E[p]\ge0.70.
}
$$

Therefore, the toy minimal-escape threshold:

$$
B_{70}^*
=
\sup\{B:p_{\min}(B)\ge0.70\}
$$

satisfies at least:

$$
\boxed{
B_{70}^*
\ge
3.667777612662112\ldots
}
$$

The previous round of numerical column generation showed the crossing is around:

$$
3.6694
$$

; thus, the exact certificate is already very close, though the numerical side is not yet a rigorous upper bound.

---

# 1. Exact dual

Take:

$$
c_0
=
1.12269224,
$$

$$
y_1=-0.38437941,
$$

$$
y_2=-0.25114540,
$$

$$
y_3=-0.11796917,
$$

and the boundary price:

$$
\mu=-0.03068556.
$$

Configuration-wise, we need to prove:

$$
c_0
+
y_1S(1)
+
y_2S(2)
+
y_3S(3)
+
\mu S(4)
\le
p.
$$

Note that this inequality is independent of $B$; $B$ only enters the dual objective.

The open-band objective constant is:

$$
A
=
c_0
+
\frac14y_1
+
\frac12y_2
+
\frac34y_3
=
0.81254781.
$$

Thus:

$$
L(B)
=
A+\mu B.
$$

Setting:

$$
L(B)=0.70
$$

yields the exact:

$$
\boxed{
B_{cert}
=
\frac{11254781}{3068556}
=
3.667777612662112\ldots.
}
$$

Since:

$$
\mu<0,
$$

all:

$$
B\le B_{cert}
$$

satisfy:

$$
L(B)\ge0.70.
$$

---

# 2. Pattern $(2,2)$

Fix the positions at:

$$
0,\theta,
$$

and let:

$$
q=\cos\theta.
$$

The reduced cost becomes the exact quartic:

$$
R_{22}(q)
=
\frac{
12274224q^4
+
23593834q^3
+
12840316q^2
+
1523595q
+
118679
}{
25000000
}.
$$

Transforming:

$$
q=2Q-1,
\qquad
Q\in[0,1]
$$

into the Bernstein basis, we perform exact midpoint subdivision.

Results:

- internal nodes: $7$;
- terminal intervals: $8$;
- max depth: $7$;
- minimum terminal Bernstein coefficient:

$$
\boxed{
\frac{46501207}{1638400000000}
>
0.
}
$$

Hence:

$$
R_{22}(q)>0
$$

for all:

$$
q\in[-1,1].
$$

---

# 3. Pattern $(2,1,1)$

Fix the double point at $0$, and let the phases of the other two simple points be $\alpha,\beta$.

Let:

$$
u=\frac{\alpha+\beta}{2},
\qquad
v=\frac{\alpha-\beta}{2},
$$

$$
x=\cos u,
\qquad
z=\cos v.
$$

Then:

$$
S_j
=
1+T_j(z)^2+2T_j(z)T_j(x),
$$

where $T_j$ is the Chebyshev polynomial.

After adding $j=4$:

$$
R_{211}(x,z)
$$

becomes of degree:

$$
(4,8)
$$

as an exact rational bivariate polynomial.

Mapping to:

$$
[0,1]^2
$$

and performing exact Bernstein subdivision yields:

- internal nodes: $61$;
- terminal boxes: $62$;
- maximum depth: $12$;
- minimum terminal coefficient:

$$
\boxed{
\frac{
10973215641
}{
734003200000000
}
>
0.
}
$$

Thus, the entire continuous $(2,1,1)$ configuration space passes.

---

# 4. Pattern $(1,1,1,1)$: The most crucial new step

This branch originally has three continuous phase degrees of freedom.

Direct trigonometric subdivision is very cumbersome, so we switch to a unit-circle root structure.

Let the four roots be:

$$
z_1,z_2,z_3,z_4,
\qquad
|z_i|=1.
$$

Because the form factors:

$$
|p_j|^2
$$

are invariant under global rotation, we can rotate the roots simultaneously such that:

$$
e_4=z_1z_2z_3z_4=1.
$$

Let:

$$
A=e_1=x+iy,
$$

$$
B=e_2.
$$

The unit-circle self-inversive relation gives:

$$
e_3=\overline A,
$$

and:

$$
B\in\mathbb R.
$$

Newton's identities give the power sums:

$$
p_1=A,
$$

$$
p_2=A^2-2B,
$$

$$
p_3=A^3-3AB+3\overline A,
$$

$$
p_4
=
A^4
-
4A^2B
+
4|A|^2
+
2B^2
-
4.
$$

And:

$$
S(j)=\frac{|p_j|^2}{4}.
$$

---

# 5. Reduction to three real variables

Define:

$$
u=|A|^2,
$$

$$
v=\Re(A^2).
$$

From:

$$
|A|\le4
$$

we get:

$$
0\le u\le16.
$$

And:

$$
|v|\le u,
$$

so we can set:

$$
v=ut,
\qquad
-1\le t\le1.
$$

Meanwhile:

$$
B=e_2
$$

is the sum of six unit complex products, so we roughly but sufficiently have:

$$
|B|\le6.
$$

Therefore, all true fully-simple root configurations fall within:

$$
\boxed{
(u,t,B)
\in
[0,16]\times[-1,1]\times[-6,6].
}
$$

Note that this is a **superset**; we prove positivity on a larger domain, so it automatically holds for true root configurations.

---

# 6. Exact 3D Bernstein certificate

The fully-simple reduced cost is:

$$
R_{1111}
=
1-c_0
+
\sum_{j=1}^4
a_jS(j),
$$

where:

$$
a_j=-y_j
$$

and:

$$
a_4=-\mu.
$$

Substituting Newton's identities and switching to $(u,t,B)$ yields the exact rational polynomial:

$$
R_{1111}(u,t,B).
$$

Mapping:

$$
u=16U,
$$

$$
t=2T-1,
$$

$$
B=12C-6,
$$

to:

$$
(U,T,C)\in[0,1]^3.
$$

Its multidegree is:

$$
(4,2,4).
$$

Using exact rational Bernstein midpoint subdivision:

- internal boxes: $179$;
- terminal boxes: $180$;
- max depth: $13$;
- all terminal Bernstein coefficients are non-negative;
- minimum terminal coefficient:

$$
\boxed{
\frac1{20000}
=
5\times10^{-5}.
}
$$

Therefore:

$$
\boxed{
R_{1111}\ge5\times10^{-5}>0
}
$$

holds even on that box which is larger than the true root data.

This completes the final multiplicity pattern.

---

# 7. Thus obtaining the toy $P_{70}$ theorem

The three patterns:

$$
(2,2),
$$

$$
(2,1,1),
$$

$$
(1,1,1,1)
$$

are all configuration-wise valid.

So for any probability mixture, if:

$$
\mathbb E[S(1)]=\frac14,
$$

$$
\mathbb E[S(2)]=\frac12,
$$

$$
\mathbb E[S(3)]=\frac34,
$$

$$
\mathbb E[S(4)]\le
\frac{11254781}{3068556},
$$

then by weak duality we obtain:

$$
\boxed{
\mathbb E[p]\ge70\%.
}
$$

---

# 8. Research significance of this result

We have now truly accomplished for the first time:

$$
\text{open-band ceiling}
\rightarrow
\text{add one boundary observable}
\rightarrow
\text{strictly cross }70\%.
$$

Therefore, in the toy model:

$$
\boxed{
\text{Minimal Escape Information}
}
$$

is no longer just numerical intuition.

Moreover, the boundary constraint does not require:

$$
S(4)\le1.
$$

As long as:

$$
S(4)\lesssim3.66778
$$

it is sufficient to guarantee $70\%$.

This demonstrates once again:

> To break through the ceiling, one does not necessarily need full control over the boundary; a small amount of new information sufficient to rule out the most extreme adversarial spikes is enough.

---

# 9. Relationship with Claude's true $70\%$ problem

Claude's actual paper estimates that following the same route requires expanding the Fourier support from:

$$
1
$$

to approximately:

$$
1.04
$$

to reach $70\%$.

Our toy theorem cannot deduce:

$$
1.04.
$$

But it rigorously proves the corresponding mechanistic proposition:

$$
\boxed{
\text{Once an observable capable of constraining boundary-spikes is added, the bandwidth-one ceiling can be crossed.}
}
$$

Therefore, what is truly worth studying in the next stage is:

1. Replacing the discrete $S(4)$ constraint with a small continuous support extension;
2. Finding the toy analogue:

$$
\delta^*_{70};
$$

3. Then studying how it establishes a quantitative correspondence with Claude's:

$$
\sigma_{70}\approx1.04
$$

---

# 10. Next steps

There are two natural next goals.

## A. Exact threshold refinement

Currently, the exact:

$$
B_{70}^*
\ge3.66777761266\ldots
$$

and the numerical crossing is about:

$$
3.6694.
$$

We can try to re-optimize the rational dual to push the certificate threshold closer to the numerical crossing.

## B. Support-strip replacement

Instead of just adding a single:

$$
S(4)
$$

we add a small interval:

$$
\alpha\in[1,1+\delta].
$$

and study:

$$
\delta_{70}^*
=
\inf\{\delta:p_{\min}\ge0.70\}.
$$

This will begin to truly connect back to Claude's $1.04$.