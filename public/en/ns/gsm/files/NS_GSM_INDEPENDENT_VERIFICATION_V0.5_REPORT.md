# NS_GSM v0.5 — Independent Verification + Authority Upgrade Report

**Runtime:** CSM Reference Runtime 0.5.0  
**Date:** 2026-08-28  
**Scope:** observed-relative  
**Root formal NS status:** `OPEN`

## Result

v0.5 adds a verification layer independent of the source-assertion path used in v0.4. It does not accept a source heading such as `Theorem` or `NO-GO` as proof authority. Each target is rerun through a separate deterministic verifier and receives a hashed proof/check artifact.

Frozen result:

- 14 independent verification records;
- 12 `AUDIT -> PROOF` authority upgrades;
- 2 non-upgrades;
- 11 v0.4 proof assets upgraded to `PROOF`;
- 1 v0.4 obstruction upgraded to `PROOF` authority while its closure status remains `OPEN`;
- formal NS root remains `OPEN`;
- C1 remains `OPEN`;
- C2 remains `OPEN`;
- replay is exact.

Canonical v0.5 native-state SHA-256:

`fcfb478ff75c908c56019fdaee4e7199ec1b5d19e817d5287bbf179bcc7ca44a`

Ledger event count: **5,178**.

## Verification classes

| Kind | Count | Meaning |
|---|---:|---|
| `SYMBOLIC_EXACT` | 7 | exact SymPy / exact-algebra checks |
| `ANALYTIC_SCHEMA` | 4 | deterministic bounded mathematical proof schemas |
| `EXACT_WITNESS` | 1 | explicit exact compatibility witness |
| `GRAPH_THEOREM_REDUCTION` | 1 | exact reduction to finitely-branching infinity principle |
| `CORPUS_AUDIT` | 1 | corpus-relative statement; never proof-upgrade eligible |

## Upgraded D103 assets

All five curated D103 algebraic assets upgraded to `PROOF` authority:

1. D103.1 — Eigen-lock commutator equation;
2. D103.2 — Shear resonance condition;
3. D103.3 — Single-shear theorem;
4. D103.4 — Five-Ray Spectrum;
5. D103.5 — Riesz-loaded coaxial response.

These are bounded local tensor-algebra assets. Their upgrade does not imply a Navier–Stokes regularity theorem.

## Upgraded D105 assets

All four curated bounded D105 assets upgraded:

1. D105.1 — simple-shear TR angular scalar;
2. D105.2 — local Kelvin/TR compatibility witness;
3. D105.3 — exact viscosity residual on the inviscid kernel;
4. D105.4 — fixed-band viscosity matching.

D105's viscosity-matched shear/polarization survivor and first-order solvability/spectral-drift frontier remain open.

## Upgraded RFP assets

- RFP-05 Theorem 32.1 — Infinite Path Extraction: upgraded through a graph-theorem reduction.
- RFP-12 Theorem 12.1 — Exact Spectral-Variance Identity: upgraded through an analytic quadratic-minimization schema.
- RFP-12 Theorem 19.1 — Frequency-Norm Synchronization No-Go: the obstruction object gains `PROOF` authority, but no parent route is automatically blocked/refuted by this event.

## Deliberate non-upgrades

### RFP-10 Theorem 42.1

Verification result is `VALID`, but verifier kind is `CORPUS_AUDIT`. The theorem is explicitly relative to the current Candidate Cover v0 / audited corpus state. It remains `AUDIT` authority.

### ETN-X Proposition 8.1

The reduction from an unbounded critical L3 norm to an unbounded fixed-cutoff high-frequency tail is independently rechecked. However, the proof depends on the external critical-L3 blow-up criterion, which v0.5 does not re-prove or formally import as an independently verified theorem certificate. Therefore the native ETN-X asset remains `AUDIT` authority.

C1 Chain Necessity and C2 Finite Obstruction remain open proof obligations.

## Trust boundary

In v0.5, `PROOF` means:

> the bounded native asset passed a separate deterministic verifier under the current CSM verifier policy, with an independent certificate and hashed proof/check artifact.

It does **not** mean:

- Lean / Coq / Isabelle kernel-checking;
- external peer review;
- independent human mathematician replication;
- parent theorem closure;
- route completeness;
- Navier–Stokes global regularity.

That stronger escalation remains a future authority tier / verification stage.

## Regression and conformance

Fresh release regression was sharded because the execution harness limits single commands. The three mutually exclusive shards cover all 47 test files:

- shard A: 90 passed;
- shard B1: 24 passed;
- shard B2: 23 passed;
- shard C: 15 passed;
- total: **152 / 152 passed**.

v0.5 conformance: **11 / 11 checks passed**.

## Runtime invariants retained

- source-internal proof != independent proof;
- `AUDIT -> PROOF` requires a new independent certificate;
- failed/partial/deferred/corpus-only checks cannot upgrade authority;
- obstruction proof authority does not equal parent refutation;
- parent closure does not propagate automatically;
- root NS / C1 / C2 remain `OPEN`;
- deterministic replay remains exact.

## Release artifact verification

- deterministic wheel (`SOURCE_DATE_EPOCH=1787875200`): `csm_reference_runtime-0.5.0-py3-none-any.whl`;
- wheel SHA-256: `8c6b1f3a1d9c0ef17340e2af97115790259e9f3a95cd80153e936f4f7f1c7022`;
- installed-target smoke imports `csm_runtime` from the isolated `/tmp/csm_v05_target` installation;
- PyYAML and SymPy are declared runtime dependencies and were supplied by the offline host environment during smoke;
- installed-wheel verification reproduces the exact canonical v0.5 state hash.
