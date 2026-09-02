# 06 | Phase 2 First Agent Experiment

## Experiment name

`FW-Hypothesis-Compiler / Weight-2 Elliptic Curves`

---

# Step 1 — No Full Database Scan

First select:

```text
20 semistable known-pass curves
20 non-semistable analytic-rank-0 curves
20 deliberately bad/control curves
```

Only for compiler correctness, not for statistics.

---

# Step 2 — Build a local prime table for each curve

First take:

$$
p\in\{3,5,7,11,13,17,19,23,29,31,37\}
$$

Along with:

- rational isogeny primes;
- bad reduction primes;
- prime divisors of all $v_\ell(\Delta_E)$.

This is only a test set, not a full quantifier closure.

Output:

```text
curve
p
reduction_type
a_p
residual_irreducible
local_ss_type
FW_H2
candidate_ell
FW_H3
evidence
```

---

# Step 3 — H2 symbolic derivation

Dedicated Agent:

> Specialise the Fouquet–Wan local semisimplification prohibition to weight-2 elliptic curves, dividing into good ordinary / supersingular / multiplicative / additive reduction, and derive computable local criteria.

The initial output should not be code, but rather:

```text
lemma
proof
allowed assumptions
counterexamples
Sage predicate
```

---

# Step 4 — H3 symbolic derivation

Dedicated Agent:

> Specialise the Fouquet–Wan auxiliary $\ell$ condition to elliptic curves and compare with Banwait's residual-ramification criterion $p\nmid v_\ell(\Delta_E)$.

Goal:

```text
exact equivalence
or
strict implication
or
not equivalent
```

Do not assume equivalence by default.

---

# Step 5 — twist invariance proof

Formalise three bridge lemmas:

```text
absolute irreducibility invariant
FW-H2 bad type invariant
split-local FW-H3 witness invariant
```

Dual output in Lean and theorem-style prose is preferred.

---

# Step 6 — finite exceptional prime theorem search

Agent to search/prove:

```text
for fixed E, which p can fail H1?
which p can fail H2?
which p can fail H3?
```

Output:

$$
P_E^{\rm candidate}
$$

However, if there is no theorem guaranteeing completeness, it must not be marked as complete.

---

# Step 7 — only then database census

Only scan after the compiler passes:

$$
895{,}988
$$

or so curves in the non-semistable analytic-rank-0 search pool.

The first database output should be:

```text
FW_COMPILER_PASS
FW_COMPILER_FAIL
FW_COMPILER_UNKNOWN
```

UNKNOWN must not be silently ignored.

---

# Success Gate

Phase 2 v0.1 success does not require finding a new curve.

It only requires:

1. H2 exact specialisation is completed;
2. H3 exact specialisation is completed;
3. twist-invariance lemmas are completed;
4. finite-prime reduction holds for at least one nontrivial curve class.

This already constitutes a new mathematical result in standard mathematical language.