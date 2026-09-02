# Round 8 Finite-Width Surpassing Re-verification

Event 5-link:

$$
s_0=0.998903757132509.
$$

For nine widths in $\varepsilon\in[0.008,0.050]$, re-verified by equalizing the heights of the four-branch epigraph, using up to a $12001$ curve integration grid and a $32768$ phase grid.

Optimal width:

$$
\varepsilon_*=0.04.
$$

Optimal smoothing scale:

$$
\boxed{s_*=0.998914215192917}.
$$

Relative to the event 5-link:

$$
s_*-s_0=1.045806040811e-05.
$$

Gap between the four tracking branches:

$$
3.782521451612e-08.
$$

This is a new numerical candidate for the finite family: a smooth turning layer with finite peak curvature, which may be slightly higher than the previous isolated 5-link polyline. It is still not a Moser lower bound, for reasons including:

1. The outer parameter search has no global guarantee;
2. The curve integration and support stationary points are still floating-point computations;
3. The improvement is only about $10^{-6}$;
4. Interval certificates or independent implementation cross-validations have not yet been established.

Therefore, it is currently marked as: **Candidate breakthrough, pending independent verification**.