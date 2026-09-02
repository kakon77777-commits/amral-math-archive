# 07 | Stopping Rules and Claim Ladder

## C0 — Literature map

Only knowing which theorems might be relevant.

## C1 — Hypothesis compiler

Every FW hypothesis has an exact executable meaning.

## C2 — Fixed $(E,p)$ certificate

Can rigorously prove:

$$
\mathrm{FW}(E,p).
$$

## C3 — Twist-uniform fixed-$p$

Prove:

$$
\forall d\in\mathcal D(E),
\quad
\mathrm{FW}(E_d,p).
$$

## C4 — Finite exceptional-prime reduction

Prove:

$$
p\notin P_E
\Rightarrow
\mathrm{FW}(E,p),
$$

and $P_E$ is finite/computable.

## C5 — All odd primes

Close out one by one:

$$
p\in P_E
$$

to obtain:

$$
\forall p>2.
$$

## C6 — Full strong-BSD twist family

Combine with Banwait's $2$-part / nonvanishing to obtain:

$$
\forall d\in\mathcal D(E),
\quad
\operatorname{BSD}(E_d).
$$

---

# Forbidden Upgrades

- Testing $p<1000$ does not equate to C4/C5;
- 99.9% of primes does not equate to C5;
- A residual image "looking generic" does not equate to a theorem;
- Success on a non-semistable sample does not equate to all non-semistable curves;
- The existence of the Fouquet–Wan theorem does not equate to it being algorithmized.

---

# Three-Round Stopping Rule

If for three consecutive rounds:

- Only checked primes are added;
- Only curves are added;
- No progress is made on the exact meaning of H2/H3;
- The finite exceptional set is not theoremized;

then freeze database scaling and return to the local Galois lemma.

This prevents repeating the scenario where "more and more data is generated, but the universal quantifier is not reduced at all."