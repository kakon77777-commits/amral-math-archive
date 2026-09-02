# 09｜FW-H3 Exact Elliptic-Curve Compiler

Definition

$$
W_-(E)=
\{\ell:\ell\parallel N_E,\ E\text{ nonsplit multiplicative at }\ell\}.
$$

For odd $p$:

$$
\mathrm{FW\text{-}H3}(E,p)
\iff
\exists\ell\in W_-(E),\ 
\ell\ne p,\ 
p\nmid v_\ell(\Delta_{\min}).
$$

## Uniform certificate

Let

$$
g_-(E)=
\gcd_{\ell\in W_-(E)}
v_\ell(\Delta_{\min}).
$$

If:

$$
W_-(E)\ne\varnothing
$$

and

$$
g_-(E)=2^a,
$$

then no odd prime simultaneously divides all witness valuations.

Therefore, in the good supersingular / fixed additive branch:

$$
\boxed{
\forall p>2,\quad
\mathrm{FW\text{-}H3}(E,p)=PASS
}
$$

Only a finite base certificate is needed.

## Twist-family preservation

If a Banwait-style twist family requires every $\ell\mid N$ to split in $\mathbf Q(\sqrt d)$, then the quadratic twist character is trivial on $G_{\mathbf Q_\ell}$, and thus the same H3 witness is preserved along the family.