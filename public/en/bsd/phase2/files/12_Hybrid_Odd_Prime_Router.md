# 12｜Hybrid Odd-Prime Router

The complete strong-BSD family does not require a single theorem to cover all $p$.

## P0 — $p=2$

Banwait–Huang Theorem 2.14.

## P1 — $p\mid d$

$p$ is a good prime of the base curve. Requires support primes:

- $p\ge5$;
- good ordinary;
- residual irreducibility;
- existence of a multiplicative residual-ramification witness.

Use the existing additive-twist ordinary theorem.

## P2 — good ordinary, $p\nmid d$

- residual reducible: proceed via the reducible/Eisenstein ordinary theorem;
- residual irreducible: proceed via the ordinary Iwasawa theorem / direct ramified witness / BCS support.

Do not use FW.

## P3 — fixed multiplicative $p\mid N$

Finite set. Check prime-by-prime for:

- residual irreducibility;
- another ramified multiplicative witness $q\ne p$;
- corresponding multiplicative theorem hypotheses.

## P4 — fixed additive $p\mid N$

Finite set. Use FW:

```text
H1 = exact residual absolute irreducibility
H2 = exact local character-ratio test
H3 = nonsplit multiplicative witness
period = Manin compatibility
```

## P5 — good supersingular

Use the derived FW bridge:

```text
H1 automatic
H2 automatic
H3 uniform from g_-(E)
```

## Results

The original

$$
\forall p>2
$$

is decomposed into:

- finite bad-prime table;
- support-prime restrictions;
- ordinary theorem;
- supersingular uniform certificate.

This is the viable global quantifier compression.