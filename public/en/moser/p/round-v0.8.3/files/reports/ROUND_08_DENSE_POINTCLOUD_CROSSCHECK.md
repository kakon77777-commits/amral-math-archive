# Round 8 Dense Point Cloud Cross-Validation

To avoid using the same support logic for both the stationary point angle inverse interpolation and the curve integration, this cross-validation adopts an alternative method:

- 120,001 integration points are used per wing;
- 240,017 points are directly generated for the entire curve;
- For each phase, the maximum/minimum of $x$, $y$, and the hypotenuse functional are directly calculated across all points;
- Tangent-normal stationary point inverse solving is not used.

Candidate:

$$
\varepsilon=0.04.
$$

Stationary point support method scale:

$$
s_{\mathrm{stat}}=0.998914215192917.
$$

Minimum value of the four branches of the dense point cloud:

$$
s_{\mathrm{cloud}}=0.998914222896210.
$$

Difference between the two methods:

$$
s_{\mathrm{cloud}}-s_{\mathrm{stat}}=7.703293336547e-09.
$$

Relative to the event five-bar linkage:

$$
s_{\mathrm{cloud}}-s_0=1.046576370145e-05.
$$

This cross-validation supports that the finite-width positive lift is not an artifact caused by the single implementation of stationary point inverse interpolation. However, since both methods still share the same numerical curve integration, it cannot yet replace a completely independent implementation or an interval certificate.