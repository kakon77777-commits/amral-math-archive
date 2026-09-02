# 06 | Phase 1 Agent Experiment Specifications
## BSD Certificate Atlas + Strong-BSD Twist-Family Reproduction

## 0. Objective

Not:

> Calculating a BSD ratio for millions of curves.

But rather:

> Generating theorem-applicability, certificate levels, and unclosed items for every isogeny class in a complete bounded domain.

---

# 1. Benchmark domain

First batch:

$$
\boxed{
N_E<500{,}000
}
$$

An isogeny-class representative for the above.

Reason: LMFDB is complete for this conductor range.

Curves outside this dataset can be used as an extension set, but must be labeled:

```text
database_completeness = partial
```

---

# 2. Workflow

## Step A — Ingest

Fetch:

```text
LMFDB label
Cremona label
a-invariants
conductor
discriminant
rank
analytic rank
root number
torsion
regulator
Tamagawa factors
CM
semistable
Galois image metadata
Sha_an
```

## Step B — Evidence typing

Add to each field:

```text
exact
rigorous_computation
numerical
BSD_inferred
unknown
```

## Step C — Theorem router

Check item by item:

- Gross–Zagier–Kolyvagin;
- BSTW zeta-element hypotheses;
- Banwait–Huang algorithmic criteria;
- ordinary / supersingular main conjecture;
- Eisenstein-prime p-converse;
- CM-specific results;
- twist-family conditions.

Output for each determination:

```json
{
  "theorem": "...",
  "applicable": true,
  "verified_hypotheses": [],
  "failed_hypotheses": [],
  "unknown_hypotheses": [],
  "source": "...",
  "claim_scope": "weak BSD / p-part / strong BSD family"
}
```

## Step D — Certificate level

Label C0–C10 according to `03_BSD_Certificate_Ladder.md`.

## Step E — Wall classification

Reasons for non-closure must be selected from the controlled vocabulary:

```text
analytic_rank_not_rigorous
algebraic_rank_upper_bound_open
generator_saturation_open
sha_finiteness_open
sha_p_part_open
all_prime_unification_open
local_hypothesis_failed
residual_representation_unknown
high_rank_bridge_missing
normalization_or_data_issue
```

---

# 3. Three Test Groups

## Group R0

rank $0$ curves.

Purpose:

- Test known theorems for weak BSD;
- Test strong BSD $p$-parts;
- Test the separation of analytic $\Sha$ and actual proofs.

## Group R1

rank $1$ curves.

Purpose:

- Heegner point / Kolyvagin applicability;
- Regulator and generator saturation;
- p-converse.

## Group R2+

rank $\ge2$ curves.

Purpose:

- Do not seek full closure;
- Find locations where theorem coverage drops abruptly;
- Build a high-rank dependency DAG.

---

# 4. First rank-2 wall sample

$$
389.a1:
\quad
y^2+y=x^3+x^2-2x.
$$

LMFDB gives:

$$
r_{\mathrm{alg}}=r_{\mathrm{an}}=2,
$$

and the numerical value:

$$
\frac{L^{(2)}(E,1)}{2!}
\approx
0.7593165002884.
$$

The right-hand side uses:

$$
\Omega\approx4.9804251217,
$$

$$
\operatorname{Reg}\approx0.15246017794,
$$

$$
\prod c_p=1,
\qquad
\#E_{\mathrm{tors}}=1,
$$

to obtain the same numerical value.

The Agent's task is not to recalculate it, but to answer:

1. What is the certificate source for the rank $2$ equality?
2. Are the generators saturated?
3. Is the analytic rank rigorous?
4. Is $\Sha_{\mathrm{an}}=1$ an actual proof?
5. Which $p$-parts are known?
6. What exactly is the complete strong BSD status level?

---

# 5. First family reproduction

Using Banwait–Huang 2026 as the specification:

> Find which curves with conductor $\le500{,}000$ satisfy known theorems, and thus have infinitely many quadratic twists satisfying strong BSD.

Requirements:

1. Reconstruct the paper's algorithm;
2. Translate each criterion into a predicate;
3. Compare with the authors' results using a small sample;
4. Rerun over the entire domain;
5. Save versions, code, raw data, and hashes;
6. Perform an adversarial audit on any discrepancies.

---

# 6. Success Criteria

Phase 1 does not require new BSD theorems.

Success is achieved by completing the following five items:

1. Complete schema;
2. Certificates for at least three classes of curves;
3. Reproducibility of the Banwait–Huang algorithm;
4. Ability to distinguish between evidence / theorem for each result;
5. Identifying the top three common bottlenecks for high ranks.

---

# 7. Failure / Freeze Criteria

If the Agent:

- Only copies from LMFDB;
- Only calculates numerical ratios;
- Cannot trace theorem hypotheses;
- Treats analytic $\Sha$ as actual $\Sha$;
- Cannot distinguish between weak / strong / p-part;

then this round is not considered valid research.