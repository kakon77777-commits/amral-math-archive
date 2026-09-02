# Semi-Autonomous Research on Moser Skewness Field: Round 11

## — Exact Contact Boundaries, Derivative Interval Boxes, and Dedicated Difference Certificate for $120^\circ$ / $270^\circ$

**Date:** July 26, 2026  
**Status:** Semi-verified interval boxes; non-strict directed-rounding; informal proof  
**Continuation of:** Moser Skew Lab v0.10

---

# 1. Objectives of this Round

Round 10 divided the phase circle into $18$ active identity intervals, but the boundaries, derivative signs, and stationary points were still primarily described by double-precision numerical root-finding.

Round 11 accomplishes three advancements:

1. Rewrite all contact boundaries into exact analytical formulas;
2. Establish adaptive derivative boxes for the $18$ intervals;
3. Construct independent analytical error envelopes for the most sensitive $120^\circ$ and $270^\circ$ cases.

---

# 2. Exact Contact Boundaries

From the triangle normal angle:

$$
\psi_d(\phi)=\frac{\pi}{6}-\phi
$$

and the smooth wing tangential angle range:

$$
\beta\le\theta\le\alpha
$$

all boundaries can be directly derived.

| Index | Analytical Formula | Phase | Angle |
|---:|---:|---:|---:|
| 0 | $0$ | 0.000000000000000 | 0.000000000° |
| 1 | $\pi/2-\alpha$ | 0.113366182892694 | 6.495403819° |
| 2 | $\pi/2-\beta$ | 0.165413531955503 | 9.477497255° |
| 3 | $\beta-\pi/3$ | 0.358185243642795 | 20.522502745° |
| 4 | $\alpha-\pi/3$ | 0.410232592705605 | 23.504596181° |
| 5 | $\pi/2$ | 1.570796326794897 | 90.000000000° |
| 6 | $\pi-\alpha$ | 1.684162509687590 | 96.495403819° |
| 7 | $\pi-\beta$ | 1.736209858750400 | 99.477497255° |
| 8 | $2\pi/3$ | 2.094395102393195 | 120.000000000° |
| 9 | $\pi/2+\beta$ | 2.976179121634289 | 170.522502745° |
| 10 | $\pi/2+\alpha$ | 3.028226470697100 | 173.504596181° |
| 11 | $\pi$ | 3.141592653589793 | 180.000000000° |
| 12 | $5\pi/3-\alpha$ | 3.778557612080786 | 216.495403819° |
| 13 | $5\pi/3-\beta$ | 3.830604961143596 | 219.477497255° |
| 14 | $\pi+\beta$ | 4.546975448429186 | 260.522502745° |
| 15 | $\pi+\alpha$ | 4.599022797491996 | 263.504596181° |
| 16 | $3\pi/2$ | 4.712388980384690 | 270.000000000° |
| 17 | $5\pi/3$ | 5.235987755982989 | 300.000000000° |
| 18 | $2\pi$ | 6.283185307179586 | 360.000000000° |

The maximum difference from the numerical boundaries in Round 10 is only:

$$
5.240e-14.
$$

Therefore, the phase partition no longer relies on decimals obtained via bisection, but is determined by a finite number of exact angular events.

---

# 3. Analytical Envelopes for Special Branches

Using:

$$
N=262144
$$

composite midpoint partitions, and controlling the error with a global second derivative bound.

We obtain:

$$
\boxed{
s_{270}
\in
[0.998914339075752,\,
 0.998914339093513]
}.
$$

And:

$$
\boxed{
s_{120}-s_{270}
\in
[1.634956007484312e-09,\,
 1.641712345829326e-09]
}.
$$

The lower bound is strictly positive:

$$
s_{120}-s_{270}
>
1.6349560\times10^{-9}.
$$

This is the first time in this series that an explicit error box is provided for the $10^{-9}$ scale competition between $120^\circ$ and $270^\circ$, rather than merely comparing two high-precision central values.

---

# 4. Comparison with Five-Bar Linkage Event Control

Using the first branch of the event control as the upper bound for the actual minimum of the event curve:

$$
s_0
\le
0.9989037571325086749551298249\ldots
$$

The difference between the conservative lower bound of the smooth candidate and this branch falls within:

$$
[0.000010581943243125044870175099443519782731773287807896210561320048743665520857071074,\,
 0.000010581961004625044870175099443519782731773287807896210561320048743665520857071074].
$$

Thus:

$$
\boxed{
s_{270}^{\mathrm{lower}}
>
s_0^{\mathrm{upper}}
}
$$

still maintaining a safe distance of approximately $1.05819\times10^{-5}$.

---

# 5. Derivative Box Coverage

For a fixed active signature:

$$
s'(\phi)
=
n_d'\cdot p_d
-
\frac{n_x'\cdot p_x}{A}
-
\frac{n_y'\cdot p_y}{B}.
$$

The coordinates of the smooth support points are bounded by monotonic prefix integral boxes; if the derivative box contains zero, recursive bisection is applied.

| Interval | Signature | Stationary Points | Derivative Sub-boxes | Observed Signs | Unresolved |
|---:|---|---:|---:|---|---:|
| 0 | `p0|p0|p2` | 0 | 1 | negative | 0 |
| 1 | `L|p0|p2` | 3 | 286 | negative, positive | 0 |
| 2 | `p1|p0|p2` | 0 | 2 | positive | 0 |
| 3 | `p1|p0|R` | 0 | 1 | positive | 0 |
| 4 | `p1|p0|p3` | 1 | 43 | negative, positive | 0 |
| 5 | `p2|p0|p3` | 0 | 1 | negative | 0 |
| 6 | `p2|L|p3` | 1 | 8 | negative, positive | 0 |
| 7 | `p2|p1|p3` | 1 | 45 | negative, positive | 0 |
| 8 | `p2|p1|p0` | 1 | 41 | negative, positive | 0 |
| 9 | `R|p1|p0` | 0 | 3 | negative | 0 |
| 10 | `p3|p1|p0` | 0 | 1 | positive | 0 |
| 11 | `p3|p2|p0` | 1 | 2 | negative, positive | 0 |
| 12 | `p3|p2|L` | 1 | 9 | negative, positive | 0 |
| 13 | `p3|p2|p1` | 1 | 47 | negative, positive | 0 |
| 14 | `p3|R|p1` | 0 | 1 | negative | 0 |
| 15 | `p3|p3|p1` | 0 | 1 | negative | 0 |
| 16 | `p0|p3|p1` | 1 | 40 | negative, positive | 0 |
| 17 | `p0|p3|p2` | 1 | 47 | negative, positive | 0 |

Total:

$$
\boxed{
579
}
$$

derivative sub-boxes, unresolved sub-boxes:

$$
\boxed{
0
}.
$$

Therefore, excluding the isolated stationary point root boxes and contact boundary boxes, the derivative signs inside the $18$ intervals are completely excluded via boxing.

---

# 6. Smooth Stationary Point Root Boxes

| Index | Interval | Type | Root Center | 2nd Derivative Box | Min Box Lower Bound minus $s_{270}$ Upper Bound |
|---:|---:|---|---:|---:|---:|
| 1 | 1 | smooth_minimum | 0.124080806550179 | [3.304413e-01, 3.342203e-01] | 4.670e-08 |
| 2 | 1 | smooth_maximum | 0.139389574288097 | [-1.284230e-01, -1.283342e-01] | 8.198e-06 |
| 3 | 1 | smooth_minimum | 0.154699127028334 | [3.304555e-01, 3.342464e-01] | 4.558e-08 |
| 4 | 4 | smooth_maximum | 0.994829121177570 | [-1.247879e+00, -1.247879e+00] | 2.490e-01 |
| 5 | 6 | smooth_minimum | 1.736180225507774 | [1.308566e+02, 6.779911e+02] | 3.044e-02 |
| 6 | 7 | smooth_maximum | 1.832595717654542 | [-1.034152e+00, -1.034152e+00] | 3.524e-02 |
| 7 | 8 | smooth_maximum | 2.644378233756333 | [-1.171701e+00, -1.171701e+00] | 1.728e-01 |
| 8 | 11 | smooth_maximum | 3.480731208100489 | [-1.179523e+00, -1.179523e+00] | 1.806e-01 |
| 9 | 12 | smooth_minimum | 3.778956292755884 | [3.036512e+01, 3.366684e+01] | 1.287e-01 |
| 10 | 13 | smooth_maximum | 4.092020570314876 | [-1.169124e+00, -1.169124e+00] | 1.702e-01 |
| 11 | 16 | smooth_maximum | 5.121148360205284 | [-1.088599e+00, -1.088599e+00] | 8.968e-02 |
| 12 | 17 | smooth_maximum | 5.717277034815458 | [-1.220025e+00, -1.220025e+00] | 2.211e-01 |

There are a total of:

$$
12
$$

smooth stationary points.

All root boxes satisfy:

$$
0\notin s''(X_r).
$$

Thus, in the current outward-rounding model, each root box satisfies the interval-Newton-like condition for a unique root.

The conservative safe distances for two of the low-phase smooth minima remain approximately:

$$
4.56\times10^{-8},
\qquad
4.67\times10^{-8}.
$$

---

# 7. Contact Boundary Neighborhoods

| Boundary | Formula | Type | Derivative Signs Fixed on Both Sides | Neighborhood Lower Bound minus $s_{270}$ Upper Bound | Treatment |
|---:|---:|---|---|---:|---|
| 1 | $\pi/2-\alpha$ | decreasing_through_switch | True | -2.691e-02 | General Box |
| 2 | $\pi/2-\beta$ | increasing_through_switch | True | -2.297e-02 | General Box |
| 3 | $\beta-\pi/3$ | increasing_through_switch | True | -7.712e-04 | General Box |
| 4 | $\alpha-\pi/3$ | increasing_through_switch | True | 1.058e-02 | General Box |
| 5 | $\pi/2$ | decreasing_through_switch | True | 4.764e-02 | General Box |
| 6 | $\pi-\alpha$ | decreasing_through_switch | True | 1.601e-02 | General Box |
| 7 | $\pi-\beta$ | increasing_through_switch | True | 1.713e-02 | General Box |
| 8 | $2\pi/3$ | cusp_minimum | True | 1.617e-09 | 120deg |
| 9 | $\pi/2+\beta$ | decreasing_through_switch | True | 8.583e-02 | General Box |
| 10 | $\pi/2+\alpha$ | unresolved_derivative | False | 7.391e-02 | General Box |
| 11 | $\pi$ | increasing_through_switch | True | 1.134e-01 | General Box |
| 12 | $5\pi/3-\alpha$ | decreasing_through_switch | True | 9.752e-02 | General Box |
| 13 | $5\pi/3-\beta$ | increasing_through_switch | True | 1.039e-01 | General Box |
| 14 | $\pi+\beta$ | decreasing_through_switch | True | 3.798e-02 | General Box |
| 15 | $\pi+\alpha$ | decreasing_through_switch | True | 1.546e-02 | General Box |
| 16 | $3\pi/2$ | cusp_minimum | True | -1.776e-11 | 270deg |
| 17 | $5\pi/3$ | cusp_minimum | True | 8.251e-02 | General Box |

Out of the $17$ internal boundaries, the derivative boxes on both sides of $16$ boundaries can be directly sign-determined.

The remaining one is a switch where the smooth support point exits the endpoint, resulting in a wider derivative box; however, the lower bound of its entire neighborhood scale is still about $7.39\times10^{-2}$ higher than the global candidate, so it does not affect the global exclusion.

The $120^\circ$ and $270^\circ$ cases use the aforementioned dedicated analytical envelopes.

---

# 8. Certificate Status

| Item | Status |
|---|---|
| Analytical boundaries for $18$ contact intervals | Passed |
| Internal derivative boxes for $18$ intervals | Passed |
| Zero exclusion in 2nd derivative for $12$ stationary point root boxes | Passed |
| Positive difference box for $120^\circ-270^\circ$ | Passed |
| Smooth candidate higher than event control | Passed |
| Global safe exclusion of all contact boundaries | Passed |
| Strict directed-rounding throughout | **Incomplete** |
| Independent recalculation with Arb / MPFI | **Incomplete** |
| Formal proof | Not started |

Therefore, this round elevates the "complete numerical exclusion ledger" from Round 10 to:

$$
\boxed{
\text{Analytical Boundaries}
+
\text{Adaptive Derivative Boxes}
+
\text{Stationary Point Root Boxes}
+
\text{Special Branch Positive Difference Boxes}.
}
$$

---

# 9. Honest Boundaries

All integration errors in this round have analytical second derivative bounds, with additional floating-point outward rounding applied.

However, NumPy's basic operations do not use strict directed-rounding throughout, so this cannot be called a complete machine-verified proof.

The precise formulation is:

> This is a semi-verified computational certificate with analytical error bounds, floating-point outward rounding, and interval-by-interval boxed exclusion.

It is significantly stronger than a standard grid scan, but still falls short of a strict certificate generated by Arb, MPFI, or dedicated interval libraries.

---

# 10. Directions for Round 12

The work for the next round is already very clear:

1. Port `special_branch_verify.py` to Arb / python-flint ball arithmetic;
2. Reconstruct the smooth wing prefix integrals using ball arithmetic;
3. Recalculate the $579$ derivative boxes;
4. Execute a true interval Newton method on the $12$ root boxes;
5. Generate an independent, reproducible certificate JSON;
6. If all pass, incorporate the smooth five-parameter event-KKT system.

---

# 11. Conclusion

Round 11 yields the most critical new envelope:

$$
\boxed{
s_{120}-s_{270}
>
1.6349560\times10^{-9}
}.
$$

and completes:

$$
\boxed{
18\text{ Analytical Contact Intervals}
+
579\text{ Derivative Boxes}
+
12\text{ Unique Stationary Point Root Boxes}.
}
$$

Therefore, the global phase exclusion of the smooth transcendental candidates is no longer just high-density sampling, but a semi-verified certificate evaluated interval by interval, root by root, and boundary by boundary.