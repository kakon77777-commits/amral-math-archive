# 06 | Local Agent Handoff

## Agent A — Sage Environment Builder

Setup:

```text
Sage version
LMFDB release
database connection
Python dependencies
PARI / mwrank status
```

First, run for conductor $<150$.

---

## Agent B — Algorithm 1 Reproducer

Output the row count after each filter:

```text
initial
semistable/optimal/composite conductor
a3
p-isogeny
ramification
rank/L-value
CLZ branch
Zhai branch
BSD(E,2)
```

Save the pass/fail reason for each curve.

---

## Agent C — 2-Descent Referee

For check_BSD_at_2:

- Confirm the analytic Sha valuation;
- Save the bounds for each backend;
- Verify sha_an_ord_2 != 0 -> False;
- Check if timeouts cause false negatives;
- Do not allow treating $\dim\Sha[2]$ as $\operatorname{ord}_2\#\Sha$.

---

## Agent D — Algorithm 2 Cross-Checker

Run simultaneously:

1. Official Sage code;
2. Pure-Python mirror of this package.

Categorize each discrepancy:

```text
number-field index issue
Kronecker convention
negative twist convention
finite-field point count
source-branch mismatch
official code drift
```

---

## Agent E — Paper/Code Version Auditor

Pin:

- arXiv version;
- GitHub file SHA;
- LMFDB release;
- runtime flags.

Output the semantic diff between the paper pseudocode and the current code.

---

## Agent F — Global Enclosure Referee

In each round, only answer:

```text
Did this round expand the theorem coverage?
Did it increase the certificate strength?
Or did it only increase the enumeration volume?
```

If it is only the enumeration volume, stop after three consecutive rounds.