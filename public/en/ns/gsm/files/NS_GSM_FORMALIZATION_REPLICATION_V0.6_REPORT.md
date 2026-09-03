# NS_GSM v0.6 — Formalization / Cross-Implementation Replication Closure Report

**Runtime:** CSM Reference Runtime 0.6.0  
**Date:** 2026-08-28  
**Scope:** observed-relative  
**Root formal Navier–Stokes status:** OPEN

## 1. Purpose

v0.6 strengthens the auditability of the twelve bounded v0.5 `PROOF`-authority assets without changing their parent closure status. It adds orthogonal authority tiers rather than replacing the base authority lattice.

The implemented tiers are:

- `FORMALIZED_CORE_ONLY`
- `CROSS_IMPLEMENTATION_REPLICATED`
- `EXTERNAL_THEOREM_ANCHORED`
- `FORMAL_PROOF` (reserved schema; zero assets in this release)

These tiers do **not** imply one another and do not propagate to parent claims.

## 2. Formalization IR

All twelve v0.5 `PROOF` assets compile deterministically to `NSGSM-FIR/0.1` bundles containing subject identity, source statement, scope, assumptions, normalized claim, goals, dependencies, derivation class, bundle SHA-256, and explicit limitations.

The FIR is a machine-readable formalization intermediate representation. It is not a proof-assistant kernel object.

## 3. Independent second implementation

All twelve FIR cases are executed by a standalone replicator under `python -I`. The replicator does not import `csm_runtime` or the original v0.5 verifier modules.

Final result:

- formalizations: **12**
- replication attempts: **12**
- replication `MATCH`: **12**
- `FORMALIZED_CORE_ONLY` assets: **12**
- `CROSS_IMPLEMENTATION_REPLICATED` assets: **12**

D105.4 and RFP05.32.1 retain schema-level limitations; replication does not silently turn them into proof-assistant proofs.

## 4. External theorem anchor

ETN–X Proposition 8.1 receives one `EXTERNAL_THEOREM_ANCHORED` record for the critical-$L^3$ dependency associated with Escauriaza–Seregin–Šverák (2003), DOI `10.1070/RM2003v058n02ABEH000609`.

This is a bibliographic/dependency anchor. It does not re-prove the external theorem and does not upgrade the base authority of `claim:uv-escape-necessity`, which remains `AUDIT`.

## 5. Formal-proof boundary

The current environment does not provide Lean or Coq executables. Therefore:

- `FORMAL_PROOF` tier count: **0**
- no SymPy calculation is relabeled as a proof-assistant kernel proof
- attaching `FORMAL_PROOF` requires a valid `KERNEL_FORMAL_PROOF` certificate with `kernel_checked=true`, a named tool, and a content hash for the proof object

## 6. Canonical runtime result

Release freeze:

- ledger events: **5,280**
- formalizations: **12**
- replications: **12**
- replication matches: **12**
- external theorem anchors: **1**
- formal proofs: **0**
- conformance: **15 / 15 PASS**
- replay: **exact**
- root formal NS: **OPEN**
- C1 Chain Necessity: **OPEN**
- C2 Finite Obstruction: **OPEN**

Canonical native/replay state SHA-256:

`f5d4a8a739d15b5605d59ba354dd1d5771924c50d355a3787db0f7b75e06dfac`

## 7. Regression

Fresh release-tree regression covered all **168 tests** using mutually exclusive shards because the execution harness imposes a per-command time budget:

- 59 PASS
- 50 PASS
- 28 PASS
- 15 PASS
- 11 PASS
- 2 PASS
- 1 PASS
- 1 PASS
- 1 PASS

Total: **168 / 168 PASS**.

## 8. Distribution-path regression

A release-freeze CLI run using `--root .` exposed a relative-path defect: the replication process changed to a temporary working directory before invoking the relative replicator script, producing `DEFER` instead of `MATCH`.

The fix resolves the script path before entering the temporary directory. A dedicated regression test now verifies that a relative replicator path remains executable. The source-tree release freeze consequently returns 12/12 `MATCH`.

## 9. Epistemic firewalls preserved

v0.6 preserves:

- formalization != formal proof
- replication != theorem generalization
- external theorem anchor != re-proof
- bounded replicated asset != parent closure
- source theorem label != independent authority
- local/bounded proof asset != Navier–Stokes global regularity

The formal Navier–Stokes root remains `OPEN`.
