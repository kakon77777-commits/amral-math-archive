# 02 | Fouquet–Wan Hypothesis Compiler

## 0. Goal

Fouquet and Wan proved the Iwasawa Main Conjecture for modular motives with arbitrary reduction, and gave a $p$-part BSD corollary in the weight $2$ / elliptic-curve case.

Banwait and Huang have pointed out that this can be applied to non-semistable extensions, but:

> it is not immediately apparent how to algorithmically verify these conditions.

Therefore, this document formulates it as a formal compiler problem.

---

# 1. Compiler Level 0: Using a stronger but easier-to-implement sufficient theorem interface

First target the sufficient hypothesis package in the Introduction of Fouquet–Wan, rather than compiling the most general deformation-theoretic version in the first pass.

For each odd prime $p$, record:

## FW-H1 — Absolute irreducibility

$$
\bar\rho_{E,p}
$$

is absolutely irreducible.

For $E/\mathbb Q$:

- a reducible $\bar\rho_{E,p}$ is closely related to rational $p$-isogenies;
- a production implementation should use Sage/LMFDB Galois-image/isogeny metadata, rather than guessing using a small number of Frobenius traces.

Status:

```text
EXACT / THEOREM
```

---

## FW-H2 — Local residual non-degeneracy at $p$

We need to exclude the local semisimplification degeneracy specified in the Fouquet–Wan theorem.

Data interface:

```text
p
reduction_type_at_p
a_p
local_residual_representation
semisimplification_type
fw_local_degenerate
```

In the first pass, one **must not** use:

```text
a_p != something
```

to manually guess equivalent conditions.

One must:

1. Derive it from the theorem / local representation formalism;
2. Then compile it into a finite-field/local-Galois predicate.

This is the first true mathematical subproblem for the compiler.

---

## FW-H3 — Auxiliary multiplicative prime $\ell$

There needs to exist:

$$
\ell\ne p,\qquad \ell\parallel N
$$

such that the residual local representation satisfies the ramified-extension / fixed-space conditions specified in the theorem.

It is recommended to first establish:

```text
ell
ord_ell(N)
ord_ell(Delta_min)
split_multiplicative?
nonsplit_multiplicative?
rho_bar_ramified?
dim_inertia_invariants
dim_local_invariants
```

Banwait's semistable approach uses:

$$
p\nmid\operatorname{ord}_\ell(\Delta_E)
$$

as the residual ramification criterion.

However, Fouquet–Wan's exact local condition is more refined, so this cannot be directly used as the complete H3.

---

# 2. Compiler Level 1: base curve → prime certificate

For each $(E,p)$, output:

```json
{
  "curve": "...",
  "p": 5,
  "H1_absolute_irreducible": "PASS|FAIL|UNKNOWN",
  "H2_local_nondegenerate": "PASS|FAIL|UNKNOWN",
  "H3_auxiliary_prime": "PASS|FAIL|UNKNOWN",
  "witness_ell": null,
  "claim": "FW_APPLICABLE|FW_NOT_APPLICABLE|UNKNOWN"
}
```

---

# 3. Compiler Level 2: prime quantifier compression

For a fixed $E$, the goal is not to scan $p<1000$ and then declare it done.

We need to establish:

```text
generic_large_prime theorem
+
finite exceptional prime list
```

Form:

$$
\exists P_E\text{ finite}:
\quad
p\notin P_E
\Longrightarrow
\mathrm{FW}(E,p).
$$

Then for:

$$
p\in P_E
$$

perform an exact check item by item.

If this cannot be achieved, we can only output:

```text
FW verified for tested primes
```

and cannot upgrade to full BSD.

---

# 4. The most valuable first compiler theorem

The ideal outcome is not a count of a million curves, but a lemma in standard language:

> For a specific elliptic-curve class, FW-H1/H2/H3 automatically hold for all odd primes except a computable finite set.

Then:

$$
\boxed{
\text{infinite prime quantifier}
\to
\text{finite certificate}.
}
$$

This is the true Phase 2 mathematical advancement.