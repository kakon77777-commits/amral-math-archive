# Semi-Autonomous Research on Moser Skew Field: Round 9

## —— Arbitrary-Precision Reconstruction, Monotonic Darboux Cusp Envelopes, and Certificate Bounds

**Date:** July 26, 2026  
**Status:** Arbitrary-precision numerical audit; incomplete interval certificate  
**Continuation:** Moser Skew Lab v0.8

---

# 1. Objectives of This Round

The improvement of the Round 8 smooth candidate over the five-link event control is approximately:

$$
10^{-5}.
$$

This round does not expand the curve family, but examines whether this difference stems from:

- Double-precision errors;
- Curve integration errors;
- Support point sampling errors;
- Special phase cusp shifts;
- Event control value truncation.

---

# 2. Explicit Curve Definition

The smooth candidate uses fixed decimal parameters:

$$
\varepsilon=0.037,
$$

$$
w=0.3361057714712081,
$$

$$
\beta=1.405382794839393,
$$

$$
\delta=0.05204734906280986,
$$

$$
c=0.5801781668857768.
$$

The tangential angle is:

$$
\theta(u)=\beta+\delta F_\varepsilon(u;c),
$$

$$
F_\varepsilon(u;c)
=
\frac{g(u)-g(1)}{g(0)-g(1)},
$$

$$
g(u)=
\frac12
\left[
1-\tanh\left(\frac{u-c}{\varepsilon}\right)
\right].
$$

Therefore, this round studies a curve defined by explicit decimal constants, rather than an object implicitly residing in some floating-point memory.

---

# 3. Dimensionality Reduction Formula for the $270^\circ$ Cusp

Let the left wing endpoint be:

$$
p_1=(x_1,y_1),
$$

$$
x_1=w\int_0^1\cos\theta(u)\,du,
$$

$$
y_1=w\int_0^1\sin\theta(u)\,du.
$$

Central segment length:

$$
l_0=1-2w.
$$

At:

$$
\phi=\frac{3\pi}{2}
$$

, the active support identity reduces the scale to:

$$
\boxed{
s_{270}
=
\frac{y_1}{A}
+
\frac{x_1+l_0}{B}
}.
$$

Thus, the critical candidate value requires only two one-dimensional integrals.

---

# 4. Arbitrary-Precision Dual-Algorithm Results

| Decimal Precision | Integration Method | $s_{270}$ | Seconds |
|---:|---|---|---:|
| 40 | quad | `0.9989143390846327172529644185367022461801905097…` | 0.144 |
| 40 | quadgl | `0.9989143390846327172529644185367022461801905097…` | 0.325 |
| 60 | quad | `0.9989143390846327172529644185367022461801921193…` | 0.321 |
| 60 | quadgl | `0.9989143390846327172529644185367022461801921193…` | 0.398 |
| 80 | quad | `0.9989143390846327172529644185367022461801921193…` | 0.347 |
| 80 | quadgl | `0.9989143390846327172529644185367022461801921193…` | 0.199 |
| 120 | quad | `0.9989143390846327172529644185367022461801921193…` | 1.130 |
| 120 | quadgl | `0.9989143390846327172529644185367022461801921193…` | 1.724 |

`tanh–sinh` and `Gauss–Legendre` agree across all preserved digits.

Adopting the $120$-digit result:

$$
\boxed{
s_{270}
=
0.99891433908463271725296441853670224618019211931483351998479812835127468012734148
}.
$$

---

# 5. Recomputation of the Five-Link Event Control

The four contact branches of the event control:

| Branch | High-Precision Scale |
|---:|---:|
| B1 | `0.99890375713250867495512982490055648021726822671219…` |
| B2 | `0.99890375713250875719719987386818978772130872751630…` |
| B3 | `0.99890375713250890026993583710653792959092798377771…` |
| B4 | `0.99890375713250873231720030171493453710521365469528…` |

Since Round 5 only saved double-precision roots, the four branches will not be perfectly equal after arbitrary-precision recomputation.

The minimum value of the explicit decimal event curve is:

$$
\boxed{
s_0
=
0.99890375713250867495512982490055648021726822671219210378943867995125633337938996
}.
$$

Difference:

$$
\boxed{
s_{270}-s_0
=
0.0000105819521240422978345936361457659629238926026414161953594484
}.
$$

---

# 6. Monotonic Darboux Cusp Envelope

Within the candidate range:

$$
0<\theta(u)<\frac{\pi}{2},
\qquad
\theta'(u)<0.
$$

Thus:

$$
\sin\theta(u)
$$

is monotonically decreasing, while:

$$
\cos\theta(u)
$$

is monotonically increasing.

Therefore, the left and right Riemann sums provide mathematical lower and upper bounds for the integrals.

| Partitions | Lower Bound | Upper Bound | Envelope Width | Lower Bound Minus Event Control |
|---:|---:|---:|---:|---:|
| 2048 | `0.998908810334668384712867473311…` | `0.998919867834597053657245003141…` | 1.10575e-5 | 5.0532022e-6 |
| 4096 | `0.998911574709650550499897197013…` | `0.998917103459614884972085961928…` | 5.52875e-6 | 7.8175771e-6 |
| 8192 | `0.998912956897141633755674280421…` | `0.998915721272123800991768662878…` | 2.764375e-6 | 9.1997646e-6 |
| 16384 | `0.998913647990887175474130102630…` | `0.998915030178378259092177293859…` | 1.3821875e-6 | 9.8908584e-6 |

Using only $4096$ partitions:

$$
s_{270}^{\mathrm{lower}}-s_0
>
7.8\times10^{-6}.
$$

This positivity does not rely on two quadratures coincidentally outputting the same decimal, but stems from the monotonic order of the integrand.

However, the conclusion must be qualified here:

> The Darboux envelope only proves that the exact $270^\circ$ cusp value is higher than the event control; it does not directly prove that it is the global minimum over the complete phase circle.

---

# 7. Independent High-Precision Audit of the Four Control Branches

Pure `mpmath` support evaluator:

- Re-integrates curve coordinates;
- Inversely solves for the intra-wing support points from the tangency and normal perpendicularity conditions;
- Does not read the Round 8 curve CSV;
- Does not use NumPy dense point clouds.

| Branch | Phase | High-Precision Scale | Above $270^\circ$ |
|---|---:|---:|---:|
| low-1 | 0.1546991336743802 | `0.99891438487362665738117862916810012877023458…` | 4.5788994e-8 |
| low-2 | 0.1240808007425145 | `0.99891438598653319985024388065682119515720639…` | 4.69019e-8 |
| 120° | $2\pi/3$ | `0.99891434072296678644611538508900424690954547…` | 1.6383341e-9 |
| 270° | $3\pi/2$ | `0.99891433908463271725296441853670224618019211…` | 0 |

The closest competitor is $120^\circ$:

$$
s_{120}-s_{270}
\approx
1.6383\times10^{-9}.
$$

This extremely narrow gap explains why a complete phase interval certificate is much more difficult than cusp integral verification.

---

# 8. Non-Smooth Cusps

Estimate the one-sided phase derivatives using $h=10^{-9}$.

## $120^\circ$

$$
D_-s
\approx
-0.26765828712846099158541019163433513227162387662221,
$$

$$
D_+s
\approx
0.61241640533971782839191670429430484687720698747482.
$$

## $270^\circ$

$$
D_-s
\approx
-0.32948028282201254839549821055633001477896472662321,
$$

$$
D_+s
\approx
0.43268675794937853584820971062851505492461178023733.
$$

Both events satisfy:

$$
D_-s<0<D_+s.
$$

Therefore, they are local cusp minima caused by the switching of active support identities.

---

# 9. Peak Width Diagnostics

Performing low-degree polynomial fitting on the narrow scan from Round 8:

| Degree | Estimated $\varepsilon_*$ | Estimated Scale | Second Derivative |
|---:|---:|---:|---:|
| 2 | 0.0367514042 | 0.998914327819115 | -2.255644e-02 |
| 3 | 0.0367690341 | 0.998914346242333 | -2.822115e-02 |
| 4 | 0.0370322777 | 0.998914337907332 | -2.615875e-02 |

Different low-degree fits place the peak at:

$$
0.0367\lesssim\varepsilon_*\lesssim0.0371.
$$

This supports $\varepsilon=0.037$ as a reasonable peak sampling point, but does not constitute a proof of continuous optimality.

---

# 10. Certificate Status

| Item | Status |
|---|---|
| Arbitrary-precision independent curve integration | Passed |
| tanh–sinh / Gauss–Legendre cross-check | Passed |
| $270^\circ$ Darboux positive lower bound | Passed |
| High-precision recomputation of four control branches | Passed |
| Left and right directional derivatives at cusps | Passed |
| Complete phase interval exclusion | **Incomplete** |
| Parameter box Krawczyk / interval Newton | **Incomplete** |
| Formal proof | Not started |

Thus, this round can elevate the conclusion of Round 8 to:

$$
\boxed{
\text{The critical cusp value and positive difference of the smooth candidate,
have passed arbitrary-precision, dual-quadrature algorithms, and monotonic sum envelopes.}
}
$$

But it cannot yet be elevated to:

$$
\boxed{
\text{A rigorous interval certificate for the complete curve congruence problem.}
}
$$

---

# 11. Missing Global Steps

What truly needs to be proven is:

$$
s(\phi)\ge s_{270}
\qquad
\forall\phi\in[0,2\pi).
$$

If only a global Lipschitz constant and a uniform grid are used, the $10^{-9}$ level gap between $120^\circ$ and $270^\circ$ would force the grid to be extremely fine.

The next round must utilize the contact structure:

1. Partition the phase circle into intervals of fixed active identities;
2. Write out smooth support formulas in each interval;
3. Use one-sided derivatives for the cusps;
4. Use derivative signs or interval Newton methods for the smooth intervals;
5. Separately bound the competition between $120^\circ$ and $270^\circ$.

---

# 12. Direction for Round 10

The next round will establish a "phase contact interval map":

$$
\phi
\longmapsto
(
I_{\min x},
I_{\min y},
I_{\max d}
).
$$

and partition:

$$
[0,2\pi)
$$

into a finite number of active identity intervals.

For each interval, we will then establish:

$$
s_I(\phi)
$$

and derivative envelopes, systematically excluding the possibility of values lower than $s_{270}$ region by region.

In parallel, establish a smooth five-parameter event—KKT:

$$
(w,\beta,\delta,c,\varepsilon)
$$

incorporating two low-phase stationary points, two special cusps, and branch pressures.

---

# 13. Conclusion

Arbitrary-precision candidate cusp:

$$
\boxed{
s_{270}
=
0.9989143390846327172529644185367022461801921193148335199847981283512747
}.
$$

Event control:

$$
\boxed{
s_0
=
0.9989037571325086749551298249005564802172682267121921037894386799512563
}.
$$

Difference:

$$
\boxed{
s_{270}-s_0
=
0.0000105819521240422978345936361457659629238926026
}.
$$

The monotonic Darboux lower bound with $4096$ partitions still retains a positive difference of approximately:

$$
7.8\times10^{-6}
$$

Therefore, the smooth candidate has been elevated from a double-precision candidate to:

$$
\boxed{
\text{A candidate confirmed by arbitrary precision, consistent across dual algorithms,
and possessing a monotonic Darboux cusp lower bound.}
}
$$

The next core task is not to add more decimal places, but to complete the piecewise interval exclusion for the entire phase circle.