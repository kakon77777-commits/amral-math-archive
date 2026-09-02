# 10 | FW-H2 Compiler and Ordinary Obstruction

## Good supersingular

The residual local representation of a good supersingular prime is controlled by niveau-2 fundamental characters, and the local residual type is irreducible.

Therefore:

$$
\boxed{
\mathrm{FW\text{-}H1=PASS,\qquad
FW\text{-}H2=PASS.
}
$$

For FW, only H3 remains.

## Good ordinary

The standard ordinary semisimplification is:

$$
\bar\rho^{ss}
\simeq
\bar\alpha
\oplus
\bar\chi_{\rm cyc}\bar\alpha^{-1},
$$

where $\bar\alpha$ is unramified, and the Frobenius value corresponds to $a_p\bmod p$.

H2 fails iff

$$
\bar\alpha^2=1,
$$

Thus:

$$
\boxed{
a_p(E)^2\equiv1\pmod p.
}
$$

This is a cheap exact criterion.

## Why should ordinary primes not use FW?

To use FW to cover all ordinary primes, one must exclude all primes satisfying:

$$
a_p^2\equiv1\pmod p
$$

In general, there is no clean finite-exception theorem available.

Therefore:

$$
\boxed{
\text{Ordinary primes continue to use the ordinary theorem; FW is reserved for additive + supersingular.}
}
$$

## Potentially multiplicative

The local semisimplification inherently takes the form of a quadratic Tate twist:

$$
\psi\oplus\psi\bar\chi_{\rm cyc},
$$

Thus, it falls into the forbidden type of FW-H2.

This branch also does not use FW.