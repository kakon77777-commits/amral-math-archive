# 25 | Chebotarev Referee Audit

$$
f_2(x)=x^3+x^2+8x-16.
$$

Its discriminant is:

$$
-11136=-2^7\cdot3\cdot29.
$$

irreducible + nonsquare discriminant:

$$
\operatorname{Gal}(L/\mathbf Q)=S_3.
$$

Unique quadratic subfield:

$$
F_0=\mathbf Q(\sqrt{-174}).
$$

Let:

$$
K=\mathbf Q(\zeta_{24},\sqrt{29}).
$$

$$
[K:\mathbf Q]=16.
$$

Moreover:

$$
\sqrt{-174}=\sqrt{-6}\sqrt{29},
$$

Since $\mathbf Q(\sqrt{-6})\subset\mathbf Q(\zeta_{24})$, we have:

$$
F_0\subset K.
$$

Since $K$ is abelian and the unique nontrivial proper Galois subfield of $L$ is $F_0$:

$$
L\cap K=F_0.
$$

Therefore:

$$
[LK:\mathbf Q]=48.
$$

Support condition:

- identity on $K$;
- 3-cycle on $L$.

The 3-cycle fixes $F_0$, so it is compatible.

Class size:

$$
2.
$$

Chebotarev:

$$
\boxed{\delta(\mathcal P)=2/48=1/24.}
$$

---

# Numerical sanity

v0.4 additionally uses a completely independent, small polynomial-mod-$q$ verifier to scan:

$$
q<10^7.
$$

This only verifies the implementation and density trend, and does not replace the theorem.