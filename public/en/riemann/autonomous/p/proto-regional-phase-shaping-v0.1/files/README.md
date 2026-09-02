# RH Regional Phase Shaping v0.1

This package is the first executable engineering prototype in the "Off-axis Positive Obstructions in Explicit Formulas" series.

It accepts an off-axis spectral rectangle

\[
K=[x_0,x_1]\times i[y_0,y_1],\qquad y_1<0,
\]

along with a support scale, basis dimension, and regularization parameter, to construct a real, even, compactly supported smooth function \(\psi\) such that its Fourier transform

\[
G(w)=\int_{\mathbb R}\psi(t)e^{iwt}\,dt
\]

satisfies:

1. \(G(-w)=G(w)\);
2. \(G(\bar w)=\overline{G(w)}\);
3. \(G(i/2)=G(-i/2)=0\);
4. Approximates \(i\) as closely as possible on the target rectangle;
5. Ensures the off-axis orbital block
   \[
   B(w)=2\operatorname{Re}(G(w)^2)
   \]
   remains negative on the rectangular grid.

## Important Limitations

This is a numerical prototype, not an RH proof, nor an interval arithmetic certificate.

The currently output `continuous_upper_estimate` uses an analytic Lipschitz upper bound combined with floating-point integration estimates, which can only serve as an indicator of candidate certificate strength. To become a rigorous certificate, it still requires:

- Complex interval arithmetic such as MPFI/Arb;
- Outer envelopes for bump integration and Fourier evaluation;
- Rigorous upper bounds over the entire rectangle rather than a finite grid;
- Connection with the arithmetic matrix of the explicit formula.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Execution Example

```bash
python run_demo.py --config examples/synthetic_rectangle.json
```

Outputs are located in `outputs/`:

- phase_shaping_result.json: Report on coefficients, errors, and signs;
- region_block.csv: \(B(w)\) on the rectangular grid;
- phase_shaping.png: Plot of the block and Fourier values;
- psi_samples.csv: Compactly supported preimage samples.

## Method

Uses a real, even basis of pairwise translated bump functions:

\[
\phi_k(t)=b\!\left(\frac{t-a_k}{\delta}\right)
+b\!\left(\frac{t+a_k}{\delta}\right),
\]

where

\[
b(u)=
\begin{cases}
\exp\!\left(-\frac1{1-u^2}\right),& |u|<1,\\
0,& |u|\ge1.
\end{cases}
\]

Let

\[
\psi=\sum_k c_k\phi_k.
\]

The endpoint condition \(G(i/2)=0\) is a real linear constraint on the coefficients. The program first computes the null space of this constraint, and then performs ridge least squares within the null space:

\[
\min_c\sum_{w_j\in K}|G_c(w_j)-i|^2+\lambda\|c\|_2^2.
\]

## Next Steps

The next engineering package will construct the following on a fixed basis:

\[
M_{\mathrm{arith}}(L)=M_\infty+\sum_{m\log p\le L}M_{p,m},
\]

and test whether the same coefficient vector simultaneously satisfies:

\[
B_K(c)<0,
\qquad
c^TM_{\mathrm{arith}}(L)c\ge0.
\]