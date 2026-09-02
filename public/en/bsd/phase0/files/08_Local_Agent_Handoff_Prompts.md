# 08 | Local Multi-Agent Handoff Prompts

## Agent A — Statement Auditor

**Task:**  
Construct a theorem dependency DAG for BSD-W, BSD-F, and BSD-S using only standard external mathematics.

**Forbidden:**

- Equating rank equality with full BSD;
- Equating analytic $\Sha$ with actual $\Sha$;
- Using Wikipedia as a core theorem source.

**Output:**

```text
theorem
statement
assumptions
claim_scope
what_it_does_not_prove
primary_source
```

---

## Agent B — Banwait–Huang Reproducer

**Task:**  
Reproduce the algorithm from arXiv:2601.16044. Run the samples provided by the authors first, then run for conductor $\le500000$.

**Output:**

- source code;
- environment lock;
- predicate list;
- result CSV/JSONL;
- discrepancies;
- exact count;
- hash.

**Stopping Condition:**  
If any paper criterion has fields that cannot be exactly determined from LMFDB / Sage / Magma, mark them as `unknown`; guessing is not allowed.

---

## Agent C — Certificate Schema Engineer

**Task:**  
Implement `bsd_curve_certificate.schema.json`, and build an importer and validator.

**Key:**

```text
numeric evidence
rigorous computation
external theorem
conditional theorem
actual proof
```

Must be kept separate.

---

## Agent D — Rank-2 Wall Analyst

**Task:**  
Centering on 389.a1, audit item by item:

$$
r_{\mathrm{alg}},
r_{\mathrm{an}},
\Omega,
\operatorname{Reg},
c_p,
E_{\mathrm{tors}},
\Sha,
L^{(2)}(1)/2!.
$$

For each item, answer:

```text
value
how computed
rigorous?
theorem?
assumption?
missing certificate?
```

---

## Agent E — Adversarial Referee

**Task:**  
Search all outputs for:

- circular BSD assumption;
- numerical-to-proof leap;
- finite-to-global leap;
- p-part-to-full leap;
- rank0/1-to-high-rank leap;
- isogeny double counting;
- database incompleteness;
- normalization mismatch.

The output must be:

```text
PASS
FAIL
OPEN
```

Do not merely provide general suggestions.

---

## Agent F — Internal Theory Quarantine

**Task:**  
Audit the relationship between Neo.K's old lattice / PRC drafts and BSD.

Only the following outputs are allowed:

1. Parts that can be translated into standard lemmas;
2. Circular or undefined parts;
3. New proof obligations required.

Directly bringing internal axioms into the external main proof is prohibited.