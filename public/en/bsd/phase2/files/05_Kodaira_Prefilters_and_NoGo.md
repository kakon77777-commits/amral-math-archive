# 05 | Kodaira Prefilters and No-Go Results

## Exact no-go: potentially multiplicative

A potentially multiplicative curve becomes a Tate curve after being twisted by a quadratic character \(\psi\).

Tate residual semisimplification:

\[
1\oplus\omega.
\]

Twisting back:

\[
\psi\oplus\psi\omega.
\]

Since:

\[
\psi^2=1,
\]

it is exactly the forbidden form of FW Theorem 1.7.

Therefore:

```text
ADDITIVE + POTENTIALLY_MULTIPLICATIVE
=> FW17_H2_FAIL
```

No local backend is required.

---

## \(p=3\)

\[
\mathbf F_3^\times
=
\{\pm1\}.
\]

Therefore, any local \(1\)-dimensional constituent is quadratic/trivial.

Thus:

```text
p=3 + LOCAL_REDUCIBLE
=> FW17_H2_FAIL

p=3 + LOCAL_IRREDUCIBLE
=> FW17_H2_PASS
```

---

## rational local \(p\)-torsion

If:

\[
E(\mathbf Q_p)[p]\neq0,
\]

a trivial line exists:

```text
=> FW17_H2_FAIL
```

Pannekoek can assist in cheaply detecting additive local p-torsion.

However:

```text
NO rational p-torsion
!= H2 PASS
```

Because the kernel character could still be a nontrivial quadratic.

---

## Formally rejecting Kodaira-only tables

The following deductions must not be used:

```text
potentially supersingular => PASS
potentially good ordinary => FAIL/PASS
Kodaira X => automatic H2
```

Unless there is an additional residual-character theorem.

Kodaira / potential-reduction is only used for prioritization;
the final decision must come down to:

```text
local residual irreducibility
or
local p-isogeny character/kernel certificate.
```