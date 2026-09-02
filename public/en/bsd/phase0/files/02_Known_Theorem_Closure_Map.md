# 02 | Known Theorem Closure Graph

## 0. Purpose

This document is not a comprehensive literature review, but rather answers:

> Which component of BSD does each existing theory actually close?

---

# 1. Fundamental Analytic Layer: Closed

For $E/\mathbb Q$, the modularity theorem provides the corresponding weight-$2$ modular form, thereby giving the analytic continuation and functional equation for $L(E,s)$.

Therefore, this project does not treat "the existence of the $L$-function" as a frontline issue.

---

# 2. Analytic Rank $0$ and $1$: Core Closure of Weak BSD

The work of Gross–Zagier and Kolyvagin, combined with the modularity theorem, establishes:

If:

$$
r_{\mathrm{an}}=0
\quad\text{or}\quad
r_{\mathrm{an}}=1,
$$

then:

$$
r_{\mathrm{alg}}=r_{\mathrm{an}},
$$

and provides corresponding finiteness control for $\Sha$.

This is the most important low-rank closure for BSD.

However, it cannot be extrapolated to:

$$
r_{\mathrm{an}}\ge2.
$$

---

# 3. The $p$-part of Strong BSD: Rapid Advancement Zone

Recent developments in Iwasawa theory, Euler systems, Kato classes, Heegner points, and $p$-adic $L$-functions have proven under numerous conditions:

- the $p$-part of BSD for rank $0/1$;
- the main conjecture for ordinary / supersingular primes;
- the p-converse;
- infinite twist families of non-CM curves satisfying strong BSD.

This layer is highly suitable for a theorem-applicability engine.

However, each result typically comes with explicit conditions:

```text
semistable?
p divides conductor?
ordinary/supersingular?
split in an imaginary quadratic field?
residual representation?
Eisenstein prime?
local Tamagawa divisibility?
```

---

# 4. Higher Rank: Structural Progress, but No General Closure

For rank $2$ and above, there already exist:

- generalized Kato classes;
- higher Gross–Zagier formulas;
- Selmer structure results;
- derived classes;
- higher-rank Iwasawa theory.

However, at present, these cannot be consolidated into:

$$
\forall E/\mathbb Q,\quad
r_{\mathrm{an}}\ge2
\Rightarrow
r_{\mathrm{alg}}=r_{\mathrm{an}}.
$$

Thus, higher rank remains the primary wall for BSD-W.

---

# 5. Strong $\Sha$ and the Leading Term Formula

Full BSD-S requires more than just the rank.

It also requires:

1. actual $\Sha$ finite;
2. actual order;
3. regulator exact enough and based on a saturated Mordell–Weil basis;
4. local Tamagawa factors;
5. torsion;
6. period convention;
7. exact leading term.

Finite cases can be exactly verified; general families of curves require deeper descent / Iwasawa theory / Euler systems.

---

# 6. Academic Status of Computational Verification

Work such as that by Keller–Stoll shows that full strong BSD can be unconditionally and exactly verified on explicit finite sets, even for absolutely simple modular abelian varieties of dimension $2$.

This provides an important engineering lesson:

$$
\boxed{
\text{A complete BSD certificate is engineerable,
but each component must be closed independently.}
}
$$

---

# 7. Arithmetic Statistics

Selmer group averages, rank distributions, twist families, and Goldfeld-type results can:

- predict that the majority of curves fall into rank $0/1$;
- identify high-value families;
- test the distribution of $\Sha$;
- determine Agent budgets.

However:

$$
\boxed{
\text{Positive density / average results}
\neq
\forall E.
}
$$

They are research routing, not global closure.

---

# 8. Closure Table

| Layer | Status | Primary Methods | Global Gap |
|---|---|---|---|
| Modularity and analytic continuation | Closed | modularity theorem | None |
| Weak BSD for analytic rank $0/1$ | Core closed | Gross–Zagier, Kolyvagin | Higher rank |
| Certain $p$-parts for rank $0/1$ | Numerous new closures | Iwasawa, zeta elements | Conditions and unification across all primes |
| Infinite strong-BSD twist families | Already exist | zeta elements + algorithmic criteria | Does not cover all curves |
| Weak BSD for rank $\ge2$ | Open | higher classes | Non-vanishing and rank bridge |
| General finiteness of $\Sha$ | Open | Selmer / Euler systems | Higher rank and all primes |
| Exact leading coefficient | Open | strong BSD machinery | All components |
| All $E/\mathbb Q$ | Open | No single route | Global uniformity |