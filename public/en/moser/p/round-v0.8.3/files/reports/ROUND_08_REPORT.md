# Moser Skew Field Semi-Autonomous Research: Round 8

## ——Finite-Width Curvature Layers, Smooth Candidate Surpassing, and Dual-Path Support Cross-Validation

**Date:** July 26, 2026  
**Status:** Exploratory numerical research; non-formal proof; non-interval certificate  
**Continuation:** Moser Skew Lab v0.7

# 1. Original Problem

Smoothing the internal vertices of the 5-link flanks using an endpoint-normalized hyperbolic tangent layer:

$$
\theta_\varepsilon(u)=\beta+(\alpha-\beta)F_\varepsilon(u;c).
$$

As $\varepsilon\to0$, it converges to two constant-direction flanks. Initially, it was expected to only check:

$$
s_\varepsilon\to s_{\mathrm{event}}.
$$

However, numerical continuation revealed a stronger non-monotonic phenomenon: finite-width curvature layers can slightly exceed the polygonal event root.

# 2. Event Control

Round 5 5-link event value:

$$
s_0=0.998903757132509.
$$

It is a numerically isolated polygonal candidate within a fixed contact topology, not a proof of local optimality in the full curve space.

# 3. Four-Branch Isocontour Continuation

Re-optimizing for finite widths:

$$
(w,\beta,\delta,c),
$$

and maximizing the lowest value among the four control branches.

| $\varepsilon$ | High-Res Scale | Relative to Event Root | Tracking Branch Gap |
|---:|---:|---:|---:|
| 0.008 | 0.998906840475532 | +3.083e-06 | 4.093e-11 |
| 0.01 | 0.998907550948445 | +3.794e-06 | 3.122e-10 |
| 0.012 | 0.998908292529886 | +4.535e-06 | 9.310e-10 |
| 0.015 | 0.998909552492856 | +5.795e-06 | 2.608e-09 |
| 0.02 | 0.998911009485979 | +7.252e-06 | 8.250e-09 |
| 0.025 | 0.998912766749906 | +9.010e-06 | 1.439e-08 |
| 0.03 | 0.998913788104096 | +1.003e-05 | 2.261e-08 |
| 0.04 | 0.998914215192917 | +1.046e-05 | 3.783e-08 |
| 0.05 | 0.998912678555912 | +8.921e-06 | 3.506e-08 |

The scale first increases with width and then falls back, indicating that the event polygon is not the highest test point in this smooth family.

# 4. Narrow Peak Scan

| $\varepsilon$ | High-Res Scale | Relative to Event Root |
|---:|---:|---:|
| 0.034 | 0.998914233445604 | +1.048e-05 |
| 0.037 | 0.998914339084632 | +1.058e-05 |
| 0.039 | 0.998914282362084 | +1.053e-05 |
| 0.041 | 0.998914124398065 | +1.037e-05 |
| 0.043 | 0.998913860300118 | +1.010e-05 |
| 0.046 | 0.998913375588294 | +9.618e-06 |

Current best test width:

$$
\boxed{\varepsilon_*=0.037}.
$$

Candidate parameters:

$$
w=0.336105771471208,\qquad l_0=0.327788457057584,
$$

$$
\beta=80.522502744597^\circ,
\qquad
\alpha-\beta=2.982093436143^\circ,
$$

$$
\alpha=83.504596180740^\circ,
\qquad
c=0.580178166885777.
$$

The stationary point support method yields:

$$
\boxed{s_*=0.998914339084632}.
$$

Relative to the event polygon:

$$
\boxed{s_*-s_0=1.058195212322e-05}.
$$

The distance to the certified scale $1$ remains:

$$
1-s_*=1.085660915368e-03.
$$

# 5. Four Control Branches

| Branch | Phase | Tracking Scale |
|---:|---:|---:|
| B1 | 0.154703285399 | 0.998914378360892 |
| B2 | 0.124068014820 | 0.998914379509003 |
| B3 | 2.094395081474 | 0.998914346322076 |
| B4 | 4.712388997111 | 0.998914346322089 |

Tracking branch gap:

$$
3.318692665122e-08.
$$

The true minimum of the full phase audit is located at the $270^\circ$ cusp. Tracking the local minimizer near the non-smooth cusp produces a deviation of about $10^{-8}$, so the final value is based on the full phase and exact special phase audits.

# 6. Multi-Resolution Audit

| Curve Integration Grid | Phase Grid | Critical Scale | Phase | Local Minima Count |
|---:|---:|---:|---:|---:|
| 3001 | 8192 | 0.998914339084638 | 4.712388980385 | 8 |
| 6001 | 16384 | 0.998914339084646 | 4.712388980385 | 8 |
| 12001 | 32768 | 0.998914339084632 | 4.712388980385 | 8 |

The three resolution levels are consistent within the displayed precision.

# 7. Dense Point Cloud Independent Support Path

To rule out false improvements caused by a single implementation of the "tangent-normal stationary point inverse solution," a curve point cloud of approximately $240,000$ points was additionally generated. For a fixed phase, the following are computed directly over all points:

$$
\min x,\qquad \min y,\qquad \max\left(\frac{x}{A}+\frac{y}{B}\right).
$$

This path does not use stationary point inverse solutions.

The dense point cloud at the exact $270^\circ$ cusp yields:

$$
s_{\mathrm{cloud}}=0.998914339084602.
$$

Difference from the stationary point support method:

$$
s_{\mathrm{cloud}}-s_*=-2.997602166488e-14.
$$

Relative to the event root:

$$
s_{\mathrm{cloud}}-s_0=1.058195209325e-05.
$$

The two support paths are consistent at the $10^{-14}$ level.

# 8. Curvature Ledger

Curvature data for the best candidate:

$$
\|\kappa\|_\infty=2.092618923824,
$$

$$
W_{5\%-95\%}=0.036579511462,
$$

$$
\int |\kappa|\,ds\approx0.052047349063.
$$

This indicates that the highest candidate is not a zero-width vertex, but a smooth layer with a finite support width and finite peak curvature.

# 9. Research Verdict

This round supports a new finite-family proposition:

$$
\boxed{\text{In the current tanh curvature layer family, there exist candidates with finite }\varepsilon>0\text{ whose pressure is slightly higher than the event 5-link.}}
$$

This corrects the simple narrative from Round 7 that "curvature concentration merely recovers the polygonal limit." A more accurate picture is:

$$
\boxed{\text{Flattening the curvature too widely reduces pressure; concentrating it too narrowly reverts to the polygon; intermediate widths can produce a slight surpassing.}}
$$

# 10. Claims Not Yet Made

1. This is not a new area lower bound for the Moser problem;
2. This is not a counterexample to Wetzel's triangle covering result, since $s_*<1$;
3. Global optimality of this smooth family has not yet been proven;
4. The two support paths still share the numerical integration of the curve coordinates;
5. Arbitrary-precision independent implementations, interval arithmetic, or Krawczyk certificates have not yet been used;
6. The improvement is only about $10^{-5}$ and must be treated as a candidate breakthrough.

# 11. Round 9 Directions

Priorities for the next round:

1. Re-implement curve integration and support with arbitrary precision;
2. Write the four smooth contact events as explicit equations;
3. Incorporate $\varepsilon$ simultaneously into the event-KKT system;
4. Establish an interval Newton/Krawczyk draft for the candidate box;
5. Test bimodal, offset, and biarc curvature distributions;
6. Check whether the finite-width improvement can be expanded to $10^{-4}$, or if it is merely a minor local effect within this family.

# 12. Conclusion

Current best candidate for Round 8:

$$
\boxed{s_*=0.998914339084632},
$$

$$
\boxed{s_*-s_0=1.058195212322e-05}.
$$

The true achievement is the discovery that:

$$
\boxed{\text{The 5-link polygonal plateau can be slightly surpassed by a smooth curvature layer of finite width.}}
$$

This result has been cross-validated by multi-resolution and dense point cloud support, but still awaits confirmation via arbitrary precision and interval certificates.