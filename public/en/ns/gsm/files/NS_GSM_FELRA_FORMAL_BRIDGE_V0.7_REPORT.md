# NS_GSM v0.7 — FELRA Formal Proof Bridge & Kernel Authority Protocol — Release Closure Report

**Runtime:** CSM Reference Runtime 0.7.0  
**Domain:** NS_GSM  
**Release mode in this environment:** `BRIDGE_READY`  
**Date:** 2026-08-28

## 1. Executive result

v0.7 implements the artifact/subprocess bridge between NS_GSM and FELRA formal backends without coupling NS_GSM closure semantics to FELRA Python internals.

The canonical flow is:

```text
NS_GSM PROOF asset
-> NSGSM-FIR/0.1
-> deterministic Lean obligation + TranslationCertificate
-> FELRA bridge bundle
-> FELRA formal_check / Lean kernel (external environment)
-> fail-closed FELRA result import
-> bounded FORMAL_PROOF[lean] promotion gate
```

This sandbox has no `lake`, `lean`, or `felra` executable. Therefore the release contains **no kernel proof claims**. It freezes the bridge-ready state only.

## 2. Frozen release state

- bridge targets: 5 (D103.1–D103.5)
- valid FIR→Lean translations: 5
- formal obligations: 5
- FELRA formal runs imported in release evidence: 0
- `FORMAL_PROOF[lean]` receipts: 0
- deferred formal-proof targets: 5
- formal NS root: `OPEN`
- C1: `OPEN`
- C2: `OPEN`
- scope: `observed-relative`
- canonical ledger events: 5,291
- canonical state/replay SHA-256: `22f7da42fcfa7bcbde1a3d552b01d307a7ab9ca320a290828bb7a46f462e50b1`
- replay: exact
- bridge conformance: 12/12 PASS

## 3. New canonical records

v0.7 adds replayable records:

- `TranslationCertificateRecord`
- `FormalObligationRecord`
- `FELRAFormalRunRecord`
- `KernelFormalProofReceipt`

Machine-local fields such as absolute path, working directory, duration and raw command are excluded from canonical mathematical state.

## 4. FIR → Lean translation

Translator profile: `lean-v0.1`  
Bridge protocol: `NSGSM-FELRA/0.1`

The first supported family is exactly D103.1–D103.5. Unsupported FIR constructs fail closed as `DEFER`.

Generated Lean artifacts are **obligation scaffolds**, not proofs. Their unresolved body uses an explicit marker rather than `sorry`. Every obligation also emits `#print axioms <theorem>` so FELRA can perform non-vacuous axiom auditing when executed in a real Lean environment.

A translation certificate binds:

- FIR identity/hash;
- native subject identity;
- theorem signature identity;
- obligation content hash;
- Lean project/support contract hash;
- assumptions and limitations.

`Lean verified` alone is not enough: FIR/translation identity must also match.

## 5. Deterministic FELRA export

Each target exports a content-addressed bridge bundle containing:

- `ns_gsm_bridge_manifest.json`
- `fir.json`
- `translation.json`
- `lean/obligation.lean`
- `lean/project/PROJECT_CONTRACT.json`
- `felra/project.yaml`

The manifest is location-independent and contains no machine-local absolute paths.

The FELRA project uses only the registered backend name `lean`, declares `expect: verified`, carries `derives_from`, assumptions/limitations and an axiom allowlist.

## 6. Fail-closed FELRA import

The importer does **not** trust FELRA's pipeline `success` flag as proof authority. Kernel eligibility requires all of:

1. translation status `VALID`;
2. exact FIR and obligation identity;
3. backend `lean`;
4. FELRA `formal_status=verified`;
5. declared expectation `verified` and met;
6. checker version and executable SHA-256;
7. non-empty theorem axiom audit;
8. intended theorem visible in the axiom audit output;
9. observed axioms within the obligation allowlist;
10. no `sorry`, unavailable, undecided, refuted, or hash-mismatch condition.

A stored FELRA `external_formal` certificate may prove certificate integrity but cannot by itself stand in for a fresh kernel run.

## 7. Kernel formal proof gate

A successful imported Lean run may add a bounded `FORMAL_PROOF` tier only to the exact child proof asset. The transaction requires the existing child to already have base `PROOF` authority and `FORMALIZED_CORE_ONLY` lineage.

The gate does **not**:

- change the child's base closure status;
- rewrite the child's base `PROOF` authority;
- propagate authority to a parent route or problem;
- close the formal NS root;
- close C1 or C2.

Thus:

```text
FORMAL_PROOF[lean] on D103.x != Navier-Stokes regularity theorem
```

## 8. v0.6 → v0.7 schema migration

v0.7 adds four empty canonical registries, so serializing the old v0.6 snapshot with the new schema necessarily changes the state hash.

The migration invariant is therefore:

```text
migrate(v0.6 snapshot) == replay(v0.6 ledger under v0.7 schema)
```

Both produce the same migrated hash. The old published v0.6 hash is preserved as historical evidence and is not incorrectly compared against the new serializer.

## 9. Historical regression maintenance

Two historical-test issues were corrected without changing runtime semantics:

1. `test_v06_release_version.py` no longer pins the *current* package forever to 0.6.0. It now checks current runtime/project version synchronization while asserting frozen v0.6 evidence remains exactly `v0.6 / 0.6.0`.
2. the historical v0.6 evidence-writer regression now validates frozen v0.6 evidence integrity/conformance instead of re-running the complete v0.5→v0.6 corpus/verifier pipeline in every later release.

A separate environmental observation remains: the old v0.6 standalone SymPy replicator can take about 17–18 seconds on a cold Python 3.13 start, close to its historical 20-second internal timeout; warm starts are around one second. This was observed but not changed in v0.7 because it is outside the FELRA bridge scope.

## 10. Regression status

Full v0.7 regression coverage: **185/185 PASS**.

The suite is executed in mutually exclusive file shards because the execution harness imposes a per-command time budget. No shard with a timeout is counted as passing; only normal exit-0 runs are included in the total.

## 11. Environment boundary

Sandbox executable probe:

```text
lake: unavailable
lean: unavailable
felra: unavailable
```

Therefore canonical v0.7 release mode is:

```text
BRIDGE_READY
FORMAL_PROOF count = 0
```

Fixtures used by unit/integration tests demonstrate the promotion semantics only and are not included as release kernel evidence.

## 12. FELRA integration contract

Audited FELRA package: 1.8.1/main.

NS_GSM treats FELRA as an external formal-execution/evidence authority, not as part of native closure semantics. FELRA may evolve independently as long as the bridge artifact/result contract remains valid.

The future Coq backend belongs to FELRA Phase B and is deliberately not implemented in NS_GSM v0.7.

## 13. Nonclaims

v0.7 does not claim:

- Lean kernel verification occurred in this sandbox;
- any `FORMAL_PROOF[lean]` exists in the release evidence;
- Coq support exists;
- D103 local algebra proves parent NS regularity;
- formalization completeness;
- route completeness;
- representation completeness;
- formal NS root closure.

## 14. Next execution step

On a machine with FELRA 1.8.1 and a real Lean/Lake project environment:

1. export one or more D103 bridge bundles;
2. replace/discharge the explicit proof-body obligation using the local Lean development;
3. run FELRA `formal_check` with the generated project contract;
4. retain the FELRA formal result and external-formal certificate;
5. import them into NS_GSM;
6. require exact translation / obligation / checker / axiom-policy match;
7. only then create bounded `FORMAL_PROOF[lean]` receipts.

Phase B then adds a real-tested Coq backend to FELRA rather than creating a second NS_GSM prover runner.
