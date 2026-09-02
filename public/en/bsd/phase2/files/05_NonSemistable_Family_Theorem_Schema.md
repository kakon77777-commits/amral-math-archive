# 05 | Non-Semistable Family Theorem Schema

## Candidate theorem (not yet proved)

This document is not a theorem claim, but rather lists the complete proof obligations.

Let:

$$
E/\mathbb Q
$$

be an optimal, analytic-rank-0 elliptic curve, not required to be semistable.

Let:

$$
\mathcal D(E)
$$

be a squarefree twist parameter family such that a certain branch of Banwait–Huang Theorem 2.14 holds.

Then for:

$$
d\in\mathcal D(E)
$$

the known candidate outputs are:

$$
L(E_d,1)\ne0,
$$

$$
\operatorname{BSD}(E_d,2).
$$

If we can further prove:

$$
\forall p>2,
\quad
\operatorname{BSD}(E_d,p),
$$

then:

$$
\operatorname{BSD}(E_d)
$$

holds.

---

# Bridge hypotheses

For every odd $p$:

1. FW-H1/H2/H3 hold for the base $E$;
2. H1/H2 are preserved under quadratic twists;
3. The splitting conditions of $d$ ensure that the H3 witness is locally preserved;
4. The period / Manin normalization in the Fouquet–Wan Corollary is compatible with the Banwait BSD convention;
5. $L(E_d,1)\ne0$ can be directly fed into the FW rank-zero corollary.

If all of the above are proved:

$$
\boxed{
\forall d\in\mathcal D(E),
\quad
\mathrm{BSD}(E_d).
}
$$

---

# The two most critical current gaps

## Gap A

$$
\forall p>2
$$

is not yet finite-ized.

## Gap B

The treatment of the Manin constant when passing from the modular-form period to the Néron period in the FW Corollary requires clean patching at small primes $p$.

Therefore, for the first version, it is best to:

- Use FW to handle "large / generic odd primes";
- Retain Banwait's existing small-prime theorems to handle $3,5,7$;
- Retain Theorem 2.14 for $p=2$.

This could form a hybrid theorem that is easier to publish and verify.