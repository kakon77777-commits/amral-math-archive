# 04 | Finite Exceptional Prime Problem

## Mother problem

For a fixed non-CM elliptic curve $E/\mathbb Q$:

$$
\boxed{
\forall p>2,\quad \mathrm{FW}(E,p)
}
$$

How can this be transformed into a finite certificate?

---

# 1. The finite nature of H1

Absolute reducibility:

$$
\bar\rho_{E,p}\text{ reducible}
$$

For $E/\mathbb Q$, this is equivalent to the existence of a residual stable line of rational $p$-isogeny type.

This only occurs for finitely many primes.

For the actual pipeline, it should use:

- LMFDB isogeny/Galois-image metadata;
- Sage isogeny classes;
- known rational isogeny theorems;

to generate the finite set:

$$
P_{\rm red}(E).
$$

---

# 2. The finite-exception heuristic for H3

If a multiplicative prime:

$$
\ell\parallel N
$$

can serve as a witness, the residual ramification is often related to:

$$
p\nmid v_\ell(\Delta_E).
$$

Therefore, a fixed $\ell$ will only be obstructed by the finite number of primes satisfying:

$$
p\mid v_\ell(\Delta_E).
$$

If there are multiple $\ell$ candidates, they can form a finite obstruction set of the form:

$$
P_{\rm ram}(E)
=
\bigcap_{\ell\in W(E)}
\{p:p\mid v_\ell(\Delta_E)\}.
$$

**Note: Fouquet–Wan H3 is finer than ramification alone; this formula can only serve as a compiler heuristic and cannot be directly used as a theorem.**

---

# 3. H2 is currently the least clear part

Whether the failure of local degeneracy at $p$ can be reduced to:

- congruences on $a_p$;
- local reduction types;
- a finite exceptional set;

requires formal derivation.

Therefore, the first true algebraic task of Phase 2 is:

$$
\boxed{
\text{derive FW-H2 for weight-2 elliptic curves in explicit local terms}.
}
$$

---

# 4. Criteria for success

Finding a theorem:

$$
p\notin
P_{\rm red}(E)
\cup
P_{\rm loc}(E)
\cup
P_{\rm ram}(E)
\Longrightarrow
\mathrm{FW}(E,p),
$$

where the three sets on the right-hand side are all:

- finite;
- effectively computable;
- certificate-producing.

In this case, the full odd-prime part becomes a finite verification.

---

# 5. Criteria for failure

If the exact conditions for FW-H2 / H3 require incompressible local Galois computations for infinitely many $p$, and there is no generic-large-$p$ theorem:

$$
\boxed{
\text{route remains a per-prime theorem, not full-BSD family closure}.
}
$$

In this case, we must downgrade, and we cannot substitute the universal quantifier with "tested up to $B$".