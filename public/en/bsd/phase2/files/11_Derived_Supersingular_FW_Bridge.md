# 11 | Derived Supersingular FW Bridge

**Status:** A derived proposition pieced together from existing external theorems; not a named theorem from the original paper.

Let $E/\mathbf Q$ be an elliptic curve and $p>2$ be a good supersingular prime.

Suppose there exists:

$$
\ell\parallel N_E
$$

such that:

1. $E$ has nonsplit multiplicative reduction at $\ell$;
2.
   $$
   p\nmid v_\ell(\Delta_{\min}).
   $$

Then:

- good supersingular local irreducibility yields FW-H1;
- the same irreducibility excludes the FW-H2 forbidden types;
- nonsplit Steinberg + residual ramification yields FW-H3.

Therefore, $E[p]$ satisfies the Fouquet–Wan residual hypotheses.

If, furthermore, we have:

$$
L(E,1)\ne0,
$$

then we can apply its rank-zero $p$-part BSD corollary, although the period normalization / Manin constant must be resolved separately.

## Uniform form

If:

$$
g_-(E)=2^a,
$$

then all odd good supersingular primes simultaneously yield H3.

Therefore:

$$
\boxed{
\text{all good supersingular odd primes}
}
$$

can be resolved by a finite base certificate.

## Safe period condition

The first version of the candidate theorem suggests directly requiring:

$$
\boxed{c_E=1}
$$

to avoid ambiguity when patching the modular period / Néron period.