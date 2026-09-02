# RH Arithmetic Matrix / PSD Prototype v0.1

This package is the second executable engineering prototype in the series "Off-Axis Positivity Obstructions in Explicit Formulas".

It constructs the following on a real, even, compactly supported basis:

\[
M_{\mathrm{arith}}(R)
=
M_\infty(R)+M_{\mathrm{fin}}(R),
\]

where \(R\) is the support radius of the test function \(\psi\) in logarithmic coordinates.

## Implemented Normalizations

Let

\[
G(t)=\int_{\mathbb R}\psi(x)e^{itx}\,dx.
\]

The archimedean term is primarily computed using an explicit kernel in the compactly supported time domain; the spectral cross-check uses

\[
2\theta'(t)
=
\operatorname{Re}\psi_0\!\left(\frac14+\frac{it}{2}\right)-\log\pi,
\]

where \(\psi_0\) is the digamma function. The spectral formula is only used for cross-checking; the main matrix is computed from the time-domain correlation kernel over a finite interval.

If \(\operatorname{supp}\psi\subset[-R,R]\), the support of the convolution square lies in \([-2R,2R]\). The finite places only activate prime powers satisfying

\[
m\log p<2R
\]

and incorporate them into the \(Q_\zeta\) matrix (in the notation of this text) via

\[
-2(\log p)p^{-m/2}
\int\psi_j(x)\psi_k(x-m\log p)\,dx
\]

## Constraints

The default is to project onto the subspace of coefficients that simultaneously satisfy

\[
G(i/2)=0,
\qquad
G(0)=0
\]

The first condition eliminates the endpoints of the explicit formula; the second condition connects to the known small-support archimedean positivity framework.

## Execution

```bash
python -m pip install -r requirements.txt
python run_demo.py --config examples/support_scan.json
python run_sensitivity.py
pytest -q
```

## Outputs

- `arithmetic_scan_result.json`: Full scan and minimum eigenvectors;
- `support_scan.csv`: Support radii, activated prime powers, and minimum eigenvalues;
- `activated_prime_powers.csv`: Scale-by-scale activation list;
- `support_scan.png`: Minimum eigenvalues of the archimedean / finite places / total matrices;
- `selected_matrices.png`: Three matrices at specified scales;
- `selected_matrix_*.csv`: Raw matrix data;
- `quadrature_sensitivity.csv`: Time-domain grid convergence scans for three support scales.

## Important Limitations

This is neither an RH proof nor a rigorous PSD certificate.

It currently still uses:

- Floating-point discretization for time-domain correlations and kernel integrals;
- Correlation matrix interpolation at prime power positions;
- Floating-point null spaces and eigenvalues;
- Non-intervalized handling of removable singularities.

Finite-frequency digamma integrals are only used for cross-checking and do not determine `numerical_psd`.

Therefore, `numerical_psd=true` only indicates that no negative eigenvalues have been found under the current discretization.

## Main Reference Normalizations

- Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771.
- Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068.