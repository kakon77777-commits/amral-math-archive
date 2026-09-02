# Riemann Hypothesis AI Research Starting Point v0.2
## Transitioning from Non-Proof Research Drafts to GAP-Driven Research

**Original Research Direction:** Neo.K  
**Research Restructuring:** Aletheia (GPT-5.6 Thinking)  
**Date:** 2026-07-23  
**Nature:** Non-Proof Research Engineering Document

---

## 1. Core Changes in v0.2

v0.1 completed the claim cleanup, preservation of correct content, and reconstruction of research interfaces for the four old drafts.

v0.2 no longer uses "candidate proof drafts" as the unit of research, but instead adopts:

$$
G_i=(A_i\rightarrow B_i)
$$

That is, a GAP edge with a precise starting point, ending point, proof obligation, dependencies, failure witnesses, and verification methods.

Currently, 47 first-round GAPs have been established, distributed across:

- Weil-type positivity;
- Nyman–Beurling closure;
- Li coefficients;
- Hilbert–Pólya spectral realization;
- de Bruijn–Newman heat flow;
- Explicit formulas and prime error terms;
- Speiser derivative criterion;
- Random matrix statistics;
- Adelic/Connes approaches;
- Observational frameworks and dynamic projections;
- Rigorous numerical computation;
- Formal proof engineering.

---

## 2. Research Workflow

Each AMRAL round selects only one GAP:

$$
G_i\in\mathcal G_t.
$$

Then executes:

$$
\text{Fix Definitions}
\to
\text{Literature Search}
\to
\text{Candidate Backfilling}
\to
\text{Counterexample Search}
\to
\text{Computation / Formal Verification}
\to
\text{State Update}.
$$

Directly requesting to "prove RH" is not allowed.

---

## 3. First Batch of Recommended Work Nodes

### A. `RH-W-01`: Fix the Weil Test Function Space

This is the definitional foundation for subsequent discussions on positivity and negative witnesses.

### B. `RH-W-02`: Structured Compression of Negative Witnesses

This is the formalized GAP version of the original `B_3`, and it is currently the most worthwhile node for testing whether AI can generate new intermediate lemmas.

### C. `RH-W-05`: Positivity Closure

First, confirm which topologies and quadratic form closure conditions are truly sufficient to preserve positivity, and correct the directional issue with lower semi-continuity in the old drafts.

### D. `RH-OD-03`: Indicator–RH Interface

Demand a genuine theorem interface for all claims regarding "optimal observation angles, regularity, and clarity"; if one cannot be found, permanently retain them in the exploration layer rather than entering them into the proof graph.

### E. `RH-HP-05`: Spectral Construction Circularity Check

Establish an automated audit template for Hilbert–Pólya candidate drafts, specifically to check whether the zero sequence is pre-encoded into the operator.

---

## 4. Success Criteria

v0.2 does not use whether RH is proved as the sole criterion for success. First-stage successes include:

1. Converting an `OPEN` GAP to `REFUTED`, thereby permanently closing off an erroneous approach;
2. Compressing a `G-SEM` natural language gap into a unique formal proposition;
3. Upgrading a `G-NUM` experiment to `CERTIFIED_NUMERICAL`;
4. Completely formalizing a local node;
5. Proving that a candidate bridge is actually an `EQUIVALENT_RISK`;
6. Completing a genuinely non-circular `FILLED` GAP.

---

## 5. Document Structure

- `01_RH_AI_Research_Starting_Point_v0.1.md`: The research draft after cleaning up the four old drafts;
- `02_RH_GAP_Atlas_v0.1.md`: Registry of GAP types and main approaches;
- `gap_registry.json`: 47 machine-readable GAPs;
- `gap_registry.csv`: Human-review and spreadsheet version;
- `gap_schema.json`: Record schema;
- `validate_registry.py`: Consistency checker.

---

## 6. Current Conclusion

Starting from v0.2, the AI will no longer generate an entire un-audited RH proof, but will instead continuously maintain:

$$
S_t=(K_t,G_t,F_t,C_t,D_t),
$$

where $G_t$ is the current GAP set, $F_t$ is the failure record, $C_t$ represents computations and certificates, and $D_t$ is the dependency graph.

The next step in the research is not to add more narrative, but to answer item by item:

$$
\text{Can this GAP be backfilled?}
$$