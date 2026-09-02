# Trust Boundary

## E0: Exact statement within the finite model

If the notch only shrinks the parent space $V$ into $V'\subseteq V$ using homogeneous linear constraints, then

$$
\mathcal F(V')\subseteq\mathcal F(V),
$$

therefore, for the same minimization objective,

$$
\inf_{\mathcal F(V)}J
\le
\inf_{\mathcal F(V')}J.
$$

Thus, the subspace notch cannot improve the primal optimum already obtained on the complete parent space.

Similarly, in a specified finite conic model, if the reconstructed

$$
W=B_\mu+\alpha C_\nu\succeq0,
$$

then for every specified finite primal feasible $A$, we have $J(A)\ge\alpha$.

## E1: Automated structural checks

- All 12 parent witnesses are read by the peak-atlas program.
- The notch screen contains two radii and 10 sets of codes per radius.
- The geometry screen has exactly 27 sets.
- All four saved joint dual objects pass the normalized measure reconstruction.
- Python syntax, tests, JSON, math delimiters, metadata flags, and the release manifest are checked by `validate_package.py`.
- All `global_rh_certificate` flags remain false.

## E2: Floating-point research evidence

- KDE peak atlas.
- Fourier quadrature and constrained whitening.
- External spectral-slope lift and analytical second derivatives.
- Uniform/core measure optimization.
- Joint dual measure optimization.
- Dense-axis / 4,941-point core complementary rank-one audit.
- Floating eigenvalue reconstruction.

## Not yet established

1. No directed-rounding enclosure for Fourier quadrature.
2. No continuous-axis supremum certificate.
3. No proof that the current lift or polynomial-bump family inevitably fails in all dimensions.
4. No new dictionary joint exhaustion of the complete 288 refined patches.
5. No theorem-backed, interval-evaluated zero-count and tail objects.
6. No arithmetic histogram interpolation error enclosure.
7. No complete leakage budget for unknown off-axis zero regions.
8. No argument-principle zero-presence or validated winding object.
9. No transfer from finite obstruction to continuous Paley–Wiener inequality.
10. No local-to-global RH closure, RH proof, or RH disproof.

## Key interpretations

The E0 monotonicity rules out the strategy of "adding only homogeneous notch constraints within the same parent space," not all spectral gap designs. The external lift does indeed bypass the E0 exclusion, but this node only tests one specific family, and the results show insufficient improvement and the onset of saturation.

A safe dual lower bound greater than $1$ is sufficient to reject the corresponding finite primal branch; conversely, if a dual value lower than $1$ is found in the future, it only means that the searched witnesses do not block it. It cannot independently prove that it is primal feasible, much less imply the RH.