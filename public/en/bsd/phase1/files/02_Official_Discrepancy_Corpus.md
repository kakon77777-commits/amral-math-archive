# 02 | Official discrepancy corpus

The official repository maintains a dedicated diagnostic report that explains, predicate by predicate, why the current Algorithm 1 rejects the following four curves:

$$
62a1,\quad66b1,\quad105a1,\quad141c1.
$$

All four curves jointly pass the semistability, isogeny exclusion, ramification, optimality, and rank-zero gates, as well as the $2$-descent gate for $E'$ and the current $\operatorname{BSD}(E,2)$ gate.

Common failures:

1. $\operatorname{ord}_2 L^{alg}=-2$, whereas CLZ20 requires $-1$;
2. The $2$-torsion structure of $E'(\mathbb Q)_{\mathrm{tors}}$ is $(2,2)$, which does not satisfy the required cyclic condition;
3. $f'(x_0)$ is a rational square;
4. The $\mathcal S$ nonempty gate fails.

This dataset should be regarded as a:

$$
\boxed{
\text{theorem-router adversarial regression corpus}.
}
$$

If a future version suddenly accepts these four curves, the first label applied should be `REGRESSION?`, not `NEW BSD BREAKTHROUGH!`.