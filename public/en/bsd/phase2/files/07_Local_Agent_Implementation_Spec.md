# 07｜Local Agent Implementation Spec

## Goal

Implement:

```text
certify_fw_h2(E, p, profile="FW17_EXACT")
```

The output must be replayable; it cannot just return a boolean.

---

## Required outputs

```json
{
  "curve": "...",
  "p": 5,
  "profile": "FW17_EXACT",
  "global_abs_irreducible": "PASS",
  "potential_reduction": "...",
  "potentially_multiplicative": false,
  "local_reducibility_Fp": "REDUCIBLE",
  "phi": {
    "defined_over_Qp": true,
    "kernel_polynomial": "...",
    "kernel_linear_factor_Qp": false
  },
  "dual_phi": {
    "kernel_polynomial": "...",
    "kernel_linear_factor_Qp": false
  },
  "fw17_h2": "PASS",
  "evidence": []
}
```

---

## Backend rules

### Rule 1

Prioritize using existing certified local isogeny / local factorization machinery in Sage/Magma.

Do not use floating-point approximations to determine:

```text
Q_p root
```

### Rule 2

If the backend can only determine:

```text
local p-isogeny exists
```

but cannot produce kernel character evidence, it cannot be treated as an H2 verdict.

### Rule 3

The kernel polynomial linear factor must be an exact \(p\)-adic factorization /
Hensel certificate.

### Rule 4

If the representation local irreducibility certificate itself is only a heuristic:

```text
UNKNOWN
```

it cannot be promoted to PASS.

---

## Regression fixtures

Include at least:

### Fixture A — \(p=3\) reducible
expected:
```text
FAIL
```

### Fixture B — potentially multiplicative additive
expected:
```text
FAIL
```

### Fixture C — reducible, phi kernel rational-x
expected:
```text
FAIL
```

### Fixture D — reducible, dual kernel rational-x
expected:
```text
FAIL
```

### Fixture E — reducible, both kernel polynomials no Qp-linear root
expected:
```text
PASS
```

### Fixture F — local irreducible
expected:
```text
PASS
```

---

## Do not infer

```text
Kodaira type alone -> PASS
no Qp rational p-torsion -> PASS
potentially supersingular -> PASS
global irreducible -> local irreducible
```

These four are all prohibited shortcuts.