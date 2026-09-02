# 03｜BSD Certificate Ladder

## Principles

Each curve must not merely store a single boolean value:

```text
BSD true / false
```

Instead, it must store "which level has been resolved by which certificate".

---

# C0 — Identity

- minimal Weierstrass model;
- $\mathbb Q$-isomorphism / isogeny label;
- conductor;
- discriminant;
- CM status;
- source provenance.

---

# C1 — Local arithmetic

- bad primes;
- reduction type;
- Tamagawa numbers;
- torsion;
- root number;
- Galois representation metadata.

---

# C2 — Numerical analytic rank

High-precision computations indicate:

$$
r_{\mathrm{an}}=r.
$$

However, there may not be a rigorous zero-order certificate.

Status:

```text
evidence
```

---

# C3 — Rigorous analytic rank

Proved via an auditable $L$-function algorithm, interval arithmetic, Turing-type count, or theorem:

$$
\operatorname{ord}_{s=1}L(E,s)=r.
$$

---

# C4 — Algebraic lower bound

Find $r$ independent rational points:

$$
r_{\mathrm{alg}}\ge r.
$$

Must store:

- generators;
- canonical heights;
- height-pairing matrix;
- independence certificate.

---

# C5 — Algebraic upper bound

Via descent / Selmer:

$$
r_{\mathrm{alg}}\le r.
$$

Must store:

- $n$-Selmer group;
- local conditions;
- saturation;
- descent implementation.

At this point:

$$
r_{\mathrm{alg}}=r.
$$

---

# C6 — Weak BSD certificate

Simultaneously having:

$$
r_{\mathrm{alg}}=r_{\mathrm{an}}.
$$

This can come from:

- rank $0/1$ theorem;
- curve-level analytic + algebraic certificates;
- family theorem.

---

# C7 — Single-prime strong BSD

For a specified $p$, prove the $p$-part of the leading term formula.

Store:

```text
p
reduction
Selmer structure
main-conjecture theorem
local factors
valuation equality
assumptions
```

---

# C8 — $\Sha$ finite and exact

Independently prove that:

$$
\Sha(E/\mathbb Q)
$$

is finite, and determine:

$$
\#\Sha.
$$

The value deduced from the BSD conjecture cannot be used as a proof.

---

# C9 — Full strong BSD

All components are resolved:

$$
\frac{L^{(r)}(E,1)}{r!}
=
\frac{
\#\Sha\Omega\operatorname{Reg}\prod c_p
}{
\#E_{\mathrm{tors}}^2
}.
$$

Must explicitly state:

- exact / certified numerical equality;
- convention;
- Manin constant / period normalization;
- all prime parts;
- no unproved assumptions.

---

# C10 — Family theorem

For an infinite family:

$$
\{E_t\}_{t\in T}
$$

establish a uniform theorem.

Must store:

- parameter domain;
- exceptional set;
- local hypotheses;
- whether all or positive proportion;
- whether weak or strong BSD.

---

# Certificate Status Dictionary

```text
unknown
numerical
conditional
theorem_applicable
proved_component
proved_curve
proved_family
refuted_data
```

---

# Strictly Prohibited

1. Writing `analytic_sha` as `proved_sha`;
2. Treating an integer returned by `rank()` as having a complete proof;
3. Labeling as full strong BSD just because a certain $p$-part holds;
4. Applying rank $0/1$ theorems to rank $2$;
5. Treating LMFDB data completeness as BSD completeness.