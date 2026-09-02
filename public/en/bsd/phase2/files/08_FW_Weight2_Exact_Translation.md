# 08 | Fouquet–Wan Theorem 1.7: Weight-2 Exact Translation

## H1

$$
\bar\rho_{E,p}\text{ absolutely irreducible}.
$$

## H2

There does not exist a character $\psi:G_{\mathbf Q_p}\to\mathbf F_p^\times$ such that

$$
\bar\rho_{E,p}|_{G_{\mathbf Q_p}}^{ss}
\simeq
\psi\oplus\psi\bar\chi_{\rm cyc}.
$$

Since

$$
\det E[p]=\bar\chi_{\rm cyc}
$$

it follows that the forbidden type must satisfy

$$
\psi^2=1.
$$

Therefore, H2 failure means:

> the local residual semisimplification is the direct sum of a quadratic character and its cyclotomic twist.

If

$$
V^{ss}=\alpha\oplus\beta,
$$

then the equivalent ratio test is:

$$
\boxed{
\mathrm{H2\ FAIL}
\iff
\alpha\beta^{-1}
\in\{\bar\chi_{\rm cyc},\bar\chi_{\rm cyc}^{-1}\}.
}
$$

This is the representation-level predicate that should be used by the production compiler.

## H3

For a weight $2$ elliptic curve, FW's auxiliary Steinberg prime can be specialized to:

- $\ell\parallel N$;
- nonsplit multiplicative reduction;
- $\bar\rho_{E,p}$ is ramified at $\ell$.

Moreover, the residual ramification of a multiplicative prime is determined by:

$$
p\nmid v_\ell(\Delta_{\min}).
$$

Therefore:

$$
\boxed{
\mathrm{FW\text{-}H3}(E,p)
\iff
\exists\ell\parallel N:
\begin{cases}
E \text{ nonsplit multiplicative at }\ell,\\
\ell\ne p,\\
p\nmid v_\ell(\Delta_{\min}).
\end{cases}
}
$$