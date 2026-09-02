# 07 — Exact-Rational Bernstein Certificate for the $N=4$ Continuous Toy PairCeiling
## Elevating from a Numerical Candidate to a Machine-Verifiable Rigorous Lower Bound

**Date:** 2026-08-11  
**Status:** exact-rational finite certificate; not yet formalized in Lean  
**Scope:** The $N=4$ continuous-position toy marked-configuration class defined in this study, not the Riemann zeta theorem.

---

# 0. Conclusion

We can now rigorously prove that for the following toy configuration class:

- total multiplicity:

$$
N=4;
$$

- marks:

$$
m_i\in\{1,2\};
$$

- positions arbitrarily located on the unit circle;
- configuration-wise open-band constraints observing only:

$$
j=1,2,3;
$$

- CUE target:

$$
S(1)=\frac14,\qquad
S(2)=\frac12,\qquad
S(3)=\frac34,
$$

its primal adversarial-law optimum satisfies at least:

$$
\boxed{
p_{\min}
\ge
0.6982110925.
}
$$

That is:

$$
\boxed{
p_{\min}
\ge
69.82110925\%.
}
$$

This is not a lower bound provided by a numerical optimizer, but rather derived from an exact-rational dual certificate combined with exact-rational Bernstein subdivision.

The candidate floor from the previous round of numerical column generation was approximately:

$$
69.82311\%.
$$

Therefore, the current toy optimum is bounded within an extremely narrow region:

$$
69.82110925\%
\le
p_{\min}
\approx
69.82311\%.
$$

The right side remains a numerical candidate and is not a rigorous upper bound; the truly rigorous bound is on the left side.

---

# 1. Dual certificate

Let:

$$
c_0
=
\frac{99998}{100000}
=
0.99998,
$$

$$
y_1
=
-\frac{42763734}{10^8},
$$

$$
y_2
=
-\frac{25119857}{10^8},
$$

$$
y_3
=
-\frac{9234705}{10^8}.
$$

For any configuration $\mathcal C$, we wish to prove:

$$
c_0
+
y_1S_{\mathcal C}(1)
+
y_2S_{\mathcal C}(2)
+
y_3S_{\mathcal C}(3)
\le
p(\mathcal C).
$$

If this holds, the LP dual objective yields:

$$
L
=
c_0
+
\frac14y_1
+
\frac12y_2
+
\frac34y_3.
$$

exactly:

$$
\boxed{
L
=
\frac{279284437}{400000000}
=
0.6982110925.
}
$$

Thus, weak duality directly gives:

$$
p_{\min}\ge L.
$$

---

# 2. Why do we only need to check three multiplicity patterns?

For:

$$
N=4,
\qquad
m_i\in\{1,2\},
$$

the only possible partitions are:

$$
(1,1,1,1),
$$

$$
(2,1,1),
$$

$$
(2,2).
$$

The positions remain continuous.

---

# 3. Pattern $(1,1,1,1)$

In this case:

$$
p=1.
$$

And since:

$$
S(j)\ge0,
$$

and:

$$
y_j<0.
$$

Therefore:

$$
c_0+\sum_{j=1}^3y_jS(j)
\le
c_0
=
0.99998
<
1=p.
$$

This branch does not require numerical computation.

---

# 4. Pattern $(2,2)$

Using translation symmetry, the two double points can be placed at:

$$
0,\theta.
$$

Let:

$$
q=\cos\theta\in[-1,1].
$$

Then:

$$
S_j
=
2+2\cos(j\theta).
$$

The reduced-cost polynomial can be exactly formulated as:

$$
R_{22}(q)
=
\frac{
36938820q^3
+
50239714q^2
+
15059619q
+
1999439
}{
50000000
}.
$$

We transform:

$$
q=2Q-1,
\qquad
Q\in[0,1]
$$

into the degree-$3$ Bernstein basis.

The global Bernstein coefficients are not all non-negative, so we perform midpoint subdivision.

Exact-rational subdivision results:

- internal nodes: $3$;
- terminal boxes: $4$;
- maximum depth: $3$;
- all terminal Bernstein coefficients are non-negative;
- minimum terminal coefficient:

$$
\boxed{
\frac{120357}{25000000}
=
0.00481428.
}
$$

Thus:

$$
R_{22}(q)>0
$$

for all:

$$
q\in[-1,1].
$$

---

# 5. Pattern $(2,1,1)$

Using translation symmetry, we place the double point at $0$, and the two simple phases are:

$$
\alpha,\beta.
$$

Define:

$$
u=\frac{\alpha+\beta}{2},
\qquad
v=\frac{\alpha-\beta}{2}.
$$

Then:

$$
2+e^{ij\alpha}+e^{ij\beta}
=
2+2e^{iju}\cos(jv).
$$

Thus:

$$
S_j
=
1+\cos^2(jv)+2\cos(jv)\cos(ju).
$$

Next, let:

$$
x=\cos u,\qquad
z=\cos v.
$$

From Chebyshev polynomials:

$$
\cos(ju)=T_j(x),
\qquad
\cos(jv)=T_j(z),
$$

we obtain the bivariate polynomial:

$$
R_{211}(x,z)
=
-\frac12+2\times10^{-5}
+
\sum_{j=1}^3
a_j
\left[
1+T_j(z)^2+2T_j(z)T_j(x)
\right],
$$

where:

$$
a_1=\frac{42763734}{10^8},
$$

$$
a_2=\frac{25119857}{10^8},
$$

$$
a_3=\frac{9234705}{10^8}.
$$

and:

$$
(x,z)\in[-1,1]^2.
$$

After mapping:

$$
x=2X-1,
\qquad
z=2Z-1
$$

to:

$$
[0,1]^2
$$

we use exact-rational bivariate Bernstein coefficient subdivision.

Results:

- internal boxes: $77$;
- certified terminal boxes: $78$;
- maximum subdivision depth: $16$;
- all terminal Bernstein coefficients are non-negative;
- the minimum Bernstein coefficient among all terminal boxes is:

$$
\boxed{
\frac{
195858711475181
}{
34359738368000000000
}
}
$$

approximately:

$$
5.70023873225\times10^{-6}>0.
$$

Therefore:

$$
R_{211}(x,z)>0
$$

over the entire:

$$
[-1,1]^2.
$$

---

# 6. What has this proven?

All three patterns have passed, therefore:

$$
\boxed{
c_0+\sum_{j=1}^3y_jS_{\mathcal C}(j)
\le
p(\mathcal C)
}
$$

holds for our complete $N=4$ continuous toy configuration class.

Thus, for any probability law:

$$
\mathcal L=\{w_c,\mathcal C_c\},
$$

if:

$$
\mathbb E_{\mathcal L}[S(j)]
=
\frac j4,
\qquad
j=1,2,3,
$$

we have:

$$
\boxed{
\mathbb E_{\mathcal L}[p]
\ge
69.82110925\%.
}
$$

This is our first **certified small-$N$ PairCeiling analogue** to date.

---

# 7. Relationship with the Anthropic ceiling

The Anthropic $N=256$ exact-rational law is approximately:

$$
68.1828687\%.
$$

Our $N=4$ certified floor is:

$$
69.82110925\%.
$$

The difference between the two is approximately:

$$
1.63824
$$

percentage points.

This does not imply that $N\to\infty$ will necessarily converge to the Anthropic constant; however, it is consistent with the phenomenon of the previous numerical sequence:

$$
N=4,5,6,7
$$

shifting downwards toward the official law.

---

# 8. Why is Bernstein well-suited here?

The Bernstein basis has a very important property:

If all Bernstein coefficients of a polynomial on a box are non-negative, then:

$$
P(x)\ge0
$$

over the entire box.

If the global coefficients cannot yet be proven positive, we perform de Casteljau subdivision on the domain; each subdivision preserves exact rational coefficients.

Therefore:

```text
numerical dual
→ rationalize with margin
→ derive exact polynomial
→ Bernstein subdivision
→ exact positivity certificate
```

is a very natural:

$$
\boxed{
\text{numerical discovery}
\rightarrow
\text{rigorous finite certificate}
}
$$

pipeline.

---

# 9. The Next Formal Objective

We should now push:

$$
N=4
$$

from the open-band certificate further to the "minimum escape information".

That is, adding a boundary / beyond-band constraint:

$$
S(4)\le B
$$

and finding the weakest $B$ such that:

$$
p_{\min}\ge0.70.
$$

This would be the toy version of:

$$
I_{70}^*.
$$