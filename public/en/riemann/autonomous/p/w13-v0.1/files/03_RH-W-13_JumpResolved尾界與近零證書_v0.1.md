# RH-W-13: Jump-Resolved Tail Bounds and Near-Zero Certificates

## 1. Limitations of the Old Tail Bounds

For degree-$r$ correlation kernels, the old method, after integration by parts, bounded the entire top-derivative remainder term using

$$
|R(a)|\le \frac{\|F^{(r)}\|_\infty}{a^{r+1}}
$$

For the degree $3$ channel, when $d\approx h$, certain spline knots are very close to zero; the coarse absolute value majorant cannot resolve the generalized spectral bottom at the $10^{-8}$ level.

## 2. Exact Jump Representation

Let

$$
F(x)=f(x)+f(-x),\qquad x\ge0,
$$

and let $F$ be a compactly supported, degree-$r$ piecewise polynomial. Since $F^{(r)}$ is piecewise constant, the complete integration by parts can be written as

$$
\int_0^\infty e^{-ax}F(x)\,dx
=
\sum_{j=0}^{r-1}\frac{F^{(j)}(0)}{a^{j+1}}
+
\frac{F^{(r)}(0^+)+\sum_\ell \Delta F^{(r)}(x_\ell)e^{-ax_\ell}}{a^{r+1}}.
$$

This is not an asymptotic expansion, but an exact finite representation for this piecewise-polynomial kernel.

## 3. Exponential Jump Tail Bounds

Let

$$
a_k=2k+\frac12.
$$

For every $x>0$, we have

$$
0\le
\sum_{k=K}^\infty\frac{e^{-a_kx}}{a_k^p}
\le
\frac{e^{-a_Kx}}{a_K^p(1-e^{-2x})}.
$$

Therefore, once the spline knot distance is positive, the tail terms of the top-derivative jumps acquire an additional exponential decay, rather than relying solely on $K^{-r}$.

## 4. Cutoffs for This Round

Using:

$$
K_3=4000,
$$

$$
K_5=1500,
$$

$$
K_7=700.
$$

The maximum interval widths for each block-lag are approximately:

- degree $3$: $1.94\times10^{-12}$;
- degree $5$: $9.68\times10^{-13}$;
- degree $7$: $6.45\times10^{-13}$.

The maximum row radius of the full ten-dimensional matrix is

$$
\epsilon\approx2.91\times10^{-12}.
$$

## 5. Certificates

Lower bound:

$$
C-10^{-8}G-\epsilon I\succ0.
$$

Upper bound: there exists an integer vector $c$ such that

$$
c^TMc<5\times10^{-8}c^TGc.
$$

Thus,

$$
\boxed{10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}}.
$$

## 6. Trust Boundary

The certificate path uses:

- Python `int`;
- `fractions.Fraction`;
- rational interval arithmetic;
- rational atanh/arctan/log series;
- integer square-root enclosure;
- documented outward-rounded `Decimal.exp`;
- exact rational $LDL^T$.

80-digit mpmath integration is used only for cross-checking and is not part of the proof path.

The label is:

$$
\boxed{\texttt{RIGOROUS\_NUMERICAL\_CERTIFICATE UNDER DOCUMENTED SOFTWARE CONTRACT}}.
$$

It has not yet been transcribed to Lean, Coq, or other formal provers.