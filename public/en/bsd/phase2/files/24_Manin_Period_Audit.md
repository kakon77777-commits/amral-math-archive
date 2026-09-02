# 24 | Manin / Period Audit

The formula in FW Corollary 1.10 uses the modular-form period, and notes that the Néron period of the elliptic curve differs by the Manin constant.

Modern results state that:

> the Manin constant of an optimal parametrization can only be supported by additive reduction primes.

For $E_q$:

- the additive primes are $2$ and the twist prime $q$;
- FW is only applied at a **good supersingular $p$**.

Therefore:

$$
p\notin\{2,q\}
$$

and:

$$
\boxed{p\nmid c_{E_q}.}
$$

Thus, the modular/Néron periods have the same $p$-adic valuation.

## Optimality

The base `696.e1` mod-$\ell$ images are maximal for all $\ell$.

Quadratic twisting preserves residual irreducibility, so $E_q$ has no rational prime-degree isogeny.

Hence, its Q-isogeny class contains no other nonisomorphic curve, and $E_q$ itself is the optimal representative.

Therefore, this period argument does not depend on an arbitrary choice of isogenous model.