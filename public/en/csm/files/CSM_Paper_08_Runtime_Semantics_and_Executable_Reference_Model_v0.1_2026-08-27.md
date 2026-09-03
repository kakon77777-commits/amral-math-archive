# CSM Paper 08 — Closure-Space Runtime Semantics and Executable Reference Model
## Closure-Space Mathematics: Runtime Semantics, State Machines, Registries, and Executable Reference Model

**Version:** v0.1  
**Date:** 2026-08-27  
**Status:** Executable Runtime Specification  
**Language:** en-US  
**Canonical source:** UTF-8 Markdown

---

## Abstract

Papers 00–07 have established CSM's closure objects, scope typing, typed graphs, frontiers / cuts / exhaustions, reopening dynamics, projections, cross-domain transfers, and proof-carrying operator calculus. This paper converges them into the first version of directly implementable runtime semantics.

Core machine state:

$$
\boxed{
\mathsf{State}_\nu
=
\langle
G_\nu,\Sigma_\nu,C_\nu,D_\nu,F_\nu,K_\nu,O_\nu,X_\nu,P_\nu,L_\nu,\nu
\rangle
}
$$

These represent, in order, the native graph, status map, certificate registry, debt registry, frontier, cuts, obstruction covers, exhaustion, policies, ledger head, and version.

All theorem-level mutations must be executed as transactions:

$$
\boxed{
\mathsf{Txn}:
\mathsf{State}_\nu
\rightharpoonup
\mathsf{State}_{\nu+1}.
}
$$

Core security principle:

$$
\boxed{
\text{No certificate path}
\Rightarrow
\text{No native theorem mutation}.
}
$$

---

# 1. Three-Tier Runtime

The CSM Runtime is strictly divided into three tiers:

$$
L_0=\text{Canonical Event Ledger},
$$

$$
L_1=\text{Native Materialized Closure State},
$$

$$
L_2=\text{Purpose-Specific Views}.
$$

`L0` is the canonical source of committed history; `L1` must be reconstructible via replay; `L2` contains audit / research / visual / execution views, whose authority must never exceed the native state.

---

# 2. Canonical Event Ledger

Each committed event:

$$
e_i
=
\langle
\mathsf{id},
\mathsf{type},
\mathsf{payload},
\mathsf{refs},
\mathsf{certRefs},
\Delta\mathsf{Debt},
\nu,
\mathsf{provenance}
\rangle.
$$

The ledger is append-only:

$$
\boxed{
L_\nu\subseteq L_{\nu+1}.
}
$$

Errors are not overwritten; instead, `CORRECTION` / `SUPERSEDE` events are appended.

---

# 3. Runtime State and Native State Hash

Every native state must be canonically serialized:

$$
h_\nu
=
\mathsf{Hash}
(
\mathsf{CanonicalSerialize}(\mathsf{State}_\nu)
).
$$

Canonical serialization requires at least:

- deterministic field ordering;
- UTF-8 encoding;
- stable IDs;
- explicit nulls;
- schema versioning;
- deterministic scalar normalization.

The state hash is a consistency tool, not a mathematical truth score.

---

# 4. Runtime Registries

The runtime has at least six registries:

1. `ObjectRegistry`
2. `CertificateRegistry`
3. `DebtRegistry`
4. `PolicyRegistry`
5. `SnapshotRegistry`
6. `SchemaRegistry`

They must not collapse into a single record type, because object identity, proof authority, unresolved obligations, policies, and materialization versions possess distinct semantics.

---

# 5. Object Registry

Minimum fields for an object record:

```yaml
object:
  object_id:
  object_type:
  domain_id:
  scope_id:
  representation_id:
  version:
  aliases: []
  provenance_refs: []
```

Stable IDs must not depend on filenames, visual positions, parser order, or temporary DB row IDs.

---

# 6. Certificate Registry

```yaml
certificate:
  certificate_id:
  certificate_type:
  subject_ids: []
  scope_id:
  assumption_ids: []
  evidence_refs: []
  verifier_results: []
  version:
  status:
```

status:

`VALID | STALE | REVOKED | PENDING | FAILED`

Certificate invalidation does not delete history.

---

# 7. Debt Registry

```yaml
debt:
  debt_id:
  debt_type:
  subject_id:
  cause:
  scope_id:
  discharge_requirements: []
  dependency_ids: []
  version:
  status:
```

status:

`OPEN | PARTIAL | DISCHARGED | SUPERSEDED`

Core invariant:

$$
\boxed{
\text{Debt cannot disappear without a discharge event.}
}
$$

---

# 8. Status Record

Status is not a freely overwritable field, but a versioned record:

```yaml
status_record:
  object_id:
  status:
  environment_id:
  certificate_ids: []
  debt_ids: []
  event_id:
  valid_from:
  valid_to:
```

Therefore:

$$
\mathsf{BLOCKED}
\to
\mathsf{REOPENED}
$$

will not delete the original blocked history.

---

# 9. Candidate Layer

All non-deterministic / heuristic ingestion, such as natural language parsing, LLM extraction, and embedding clustering, must first enter the:

$$
\boxed{
\mathsf{CandidateStore}.
}
$$

Candidate record:

```yaml
candidate:
  candidate_id:
  source_ref:
  extracted_type:
  text_span:
  proposed_object:
  confidence:
  parser_version:
```

Core firewall:

$$
\boxed{
\mathsf{Candidate}
\not\Rightarrow
\mathsf{NativeObject}.
}
$$

---

# 10. Candidate-to-Native Promotion

Candidates can only enter the native layer after passing through:

$$
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
$$

and obtaining the corresponding certificates.

Thus, LLM extraction can be non-deterministic; mutations in the Native Closure Layer cannot be directly determined by unverified natural language.

---

# 11. Closure Transaction

transaction:

```yaml
closure_transaction:
  txn_id:
  input_state_hash:
  policy_id:
  operator_plan: []
  precheck_results: {}
  operator_instances: []
  certificate_ids: []
  debt_delta:
  graph_delta:
  status_delta:
  output_state_hash:
  commit_status:
```

---

# 12. Transaction State Machine

$$
\boxed{
\mathsf{IDLE}
\to
\mathsf{PLANNED}
\to
\mathsf{PREFLIGHT}
\to
\mathsf{EXECUTING}
\to
\mathsf{COMMITTING}
\to
\mathsf{COMMITTED}
}
$$

Failure at any critical gate:

$$
\to
\mathsf{ABORTED}.
$$

---

# 13. Atomicity

Theorem-level mutations must be atomic:

$$
\boxed{
\mathsf{COMMIT}
\vee
\mathsf{ABORT}.
}
$$

Partial native mutations are strictly prohibited.

---

# 14. Preflight

Preflight must check:

- input state hash;
- object existence;
- version freshness;
- operator composition;
- scope compatibility;
- certificate validity;
- debt compatibility;
- authority boundary;
- expected output types.

---

# 15. Stale Transaction

If the native head has changed after the transaction was created:

$$
\boxed{
\mathsf{STALE\_TXN}.
}
$$

Blind commits are prohibited.

---

# 16. Deterministic Commit

Given fixed:

- input state hash;
- operator versions;
- policy version;
- certificate results;

the same transaction must yield the same output hash.

---

# 17. Replay

$$
\boxed{
\widehat{\mathsf{State}}_\nu
=
\mathsf{Replay}
(
L_{\le\nu},
P_\nu
).
}
$$

Replay verification:

$$
\boxed{
\mathsf{Hash}
(
\widehat{\mathsf{State}}_\nu
)
=
h_\nu.
}
$$

Upon mismatch:

$$
\mathsf{RUNTIME\_INCONSISTENT}.
$$

and fail closed.

---

# 18. Snapshot

Snapshots can accelerate recovery but are not the canonical source:

```yaml
snapshot:
  state_version:
  state_hash:
  ledger_head:
  policy_version:
  schema_version:
  artifact_refs: []
```

A replay-check is mandatory after restoration.

---

# 19. Query Model

Query:

$$
\mathsf{Query}:
(\mathsf{State},q)
\to
\mathsf{QueryResult}.
$$

The result cannot be merely boolean:

$$
\boxed{
\mathsf{QueryResult}
=
\langle
\mathsf{Answer},
\mathsf{Authority},
\mathsf{Scope},
\mathsf{CertRefs},
\mathsf{DebtRefs},
\mathsf{Version},
\mathsf{SourceLayer}
\rangle.
}
$$

---

# 20. Query Family v0.1

Minimum support:

- `status(object)`
- `why_blocked(route)`
- `why_closed(claim)`
- `frontier(target)`
- `applicable_obstructions(route)`
- `uncovered_routes(target)`
- `debt(object)`
- `history(object)`
- `transferability(a,b)`
- `diff(v1,v2)`
- `replay(version)`

---

# 21. Query Authority

If the query source is a projected view:

$$
\mathsf{Authority}(result)
\le
\mathsf{Authority}(view).
$$

A DISPLAY view must not answer proof-authority queries.

---

# 22. Why-Blocked

`why_blocked` must return at least:

- applicable obstruction;
- OPCert;
- scope;
- assumptions;
- cert refs;
- active debt;
- version.

Thus, the runtime does not merely reply "blocked," but answers "who blocked it, under what conditions, and with what certificate."

---

# 23. Frontier Engine

Input:

- native graph;
- status map;
- quotient policy;
- target;
- route grammar.

Output:

$$
\partial^\ast_{D,\Gamma,\rho,\nu}\mathfrak C(Q).
$$

If route completeness is unproven, a `RouteCompletenessDebt` must be attached.

---

# 24. Cut / Cover Engines

Graph algorithms can only generate:

$$
\mathsf{CutCandidate},
\qquad
\mathsf{CoverCandidate}.
$$

They cannot directly generate theorem-level:

$$
\mathsf{CutCert},
\qquad
\mathsf{CoverCert}.
$$

This is the concrete implementation of the Candidate-to-Native firewall in graph mining.

---

# 25. Exhaustion Engine

Only when:

- RCCert;
- CutCert;
- CoverCert;
- scope fidelity;
- parent bridge;

meet the conditions of Paper 03 can an RECert be generated.

The output must still be labeled:

$$
\mathsf{EXH}_{k}^{D,\Gamma,\nu}.
$$

It must not masquerade as absolute exhaustion.

---

# 26. Projection Engine

Projection output:

```yaml
projection_artifact:
  artifact_id:
  native_state_id:
  native_state_hash:
  projection_policy:
  preserved_invariants: []
  projection_debt_ids: []
  authority:
  version:
  status:
```

After a native reopening / revision occurs, dependent views transition:

$$
\mathsf{VALID}
\to
\mathsf{STALE}.
$$

---

# 27. Verifier Interface

```yaml
verifier:
  verifier_id:
  accepted_certificate_types: []
  version:
  deterministic:
  trust_policy:
```

Verifier result:

```yaml
verification_result:
  certificate_id:
  verifier_id:
  result:
  evidence_refs: []
  verifier_version:
```

If verifier results conflict:

$$
\mathsf{CERT\_CONFLICT}
$$

theorem-level mutations must DEFER / REFUSE.

---

# 28. Runtime Exec Result

$$
\boxed{
\mathsf{ExecResult}
\in
\{
\mathsf{PASS},
\mathsf{REFUSE},
\mathsf{DEFER},
\mathsf{UNKNOWN},
\mathsf{ERROR}
\}.
}
$$

`PASS_runtime` does not equal theorem proven; it merely indicates that the operation conforms to runtime semantics.

---

# 29. Fail-Closed Semantics

Critical precondition FAIL:

$$
\boxed{
\mathsf{REFUSE}.
}
$$

Insufficient information:

$$
\mathsf{DEFER}
$$

and append a debt.

Unclassified:

$$
\mathsf{UNKNOWN}.
$$

Runtime/schema bug:

$$
\mathsf{ERROR}.
$$

ERROR must not be mistaken for a mathematical status.

---

# 30. Crash Recovery

Transaction recovery must classify at least:

- `NOT_STARTED`
- `PREPARED`
- `COMMITTED`
- `COMMIT_STATE_UNKNOWN`

When uncertain, reconstruct based on the ledger head; blind recommits are prohibited.

---

# 31. Idempotency

Every mutation transaction should have a stable idempotency key.

The same committed txn must not repeatedly generate theorem mutations.

---

# 32. Runtime Safety Invariants

$$
\boxed{
\begin{aligned}
&\text{No theorem mutation without cert path};\\
&\text{No debt disappearance without discharge};\\
&\text{No reopening history erasure};\\
&\text{No projected-view native mutation};\\
&\text{Replay must reconstruct native state};\\
&\text{No candidate-to-theorem direct jump};\\
&\text{No cross-domain authority without transfer cert};\\
&\text{No silent version mismatch composition}.
\end{aligned}
}
$$

---

# 33. NS Ingestion Profile v0.1

The first large-scale instance:

$$
\boxed{
\mathsf{NSProfile}_{v0.1}.
}
$$

Expected sources:

- ETN--X Integration;
- C1;
- C2;
- C3--C6;
- X72;
- DCRP;
- RFP;
- MORP;
- FCBP;
- Proof Asset Map;
- validation scripts.

---

# 34. NS Artifact Record

```yaml
ns_artifact:
  artifact_id:
  source_ref:
  series:
  round:
  title:
  date:
  source_hash:
  parser_version:
```

---

# 35. NS Claim Candidate

```yaml
ns_claim_candidate:
  candidate_id:
  artifact_id:
  text_span:
  normalized_statement:
  claim_type:
  explicit_status_label:
  assumptions: []
  scope:
  dependencies: []
  evidence_refs: []
```

---

# 36. NS Status Labels Are Hints

Original:

`CLOSED | OPEN | NO-GO | SURVIVOR | STOP | CONDITIONAL`

Can only be parsed into:

- `StatusCandidate`
- `OpenClaimCandidate`
- `ObstructionCandidate`
- `RouteStateCandidate`
- `FrontierCandidate`
- `ConditionalCandidate`

Cannot directly mutate native status.

---

# 37. NS Operator Planning

For example, `NO-GO`:

$$
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Block?}
$$

Not:

$$
\mathsf{Refute}.
$$

`CLOSED` might ultimately be evaluated as:

- `Prove`
- `Condition`
- `Block`
- `UNVERIFIED`

Determined by actual evidence.

---

# 38. NS Seed Dataset

The first version seed is recommended to start with:

1. ETN--X Integration;
2. C1;
3. C2;
4. C6-Q;
5. DCRP103;
6. DCRP104;
7. DCRP105.

The reason is that this set simultaneously features:

- CLOSED;
- OPEN;
- NO-GO;
- survivor;
- STOP;
- cross-series / cross-stage semantics;
- validation scripts.

This is sufficient to test the compiler without having to ingest the entire corpus at the outset.

---

# 39. NS Native Graph v0.1

The first version only claims:

$$
\boxed{
\mathfrak C_{\rm NS,obs}^{\rm nat,v0.1}
}
$$

i.e., the observed-relative graph.

It does not claim:

$$
\Omega_{\rm NS}^{\rm math}.
$$

---

# 40. NS Frontier v0.1

Output:

$$
\boxed{
\partial_{\rm NS,obs}^{\ast,v0.1}.
}
$$

Any unproven parts of route completeness enter the debt registry.

---

# 41. Runtime Conformance Suite

CSM Runtime v0.1 must have a conformance suite.

Minimum 12 vectors:

1. diagnostic obstruction;
2. counterexample;
3. proof + unmet assumption;
4. debt discharge;
5. projected-view mutation refusal;
6. lossy transfer;
7. reopening wave;
8. false quotient split;
9. deterministic replay;
10. stale transaction;
11. NS `NO-GO` candidate;
12. NS `CLOSED` without cert.

---

# 42. Conformance Vector — Deterministic Replay

Replaying twice with the same ledger + same policy:

$$
h_1=h_2.
$$

---

# 43. Conformance Vector — Block Is Not Refute

route OPEN + valid obstruction:

$$
\mathsf{OPEN}
\to
\mathsf{BLOCKED}.
$$

Parent claim remains unchanged.

---

# 44. Conformance Vector — Conditional

proof cert is valid but assumption is undischarged:

$$
\sigma(Q)=\mathsf{CONDITIONAL}.
$$

---

# 45. Conformance Vector — Debt Discharge

After debt discharge:

$$
\mathsf{CONDITIONAL}
\to
\mathsf{CLOSED}^{+}
$$

if all other certs are valid.

---

# 46. Conformance Vector — Reopening

A shared premise is invalidated:

- downstream certs -> STALE;
- routes -> REOPENED / audit;
- frontier rebuild.

---

# 47. Conformance Vector — NS NO-GO

Document labeled `NO-GO`:

Expected:

`ObstructionCandidate`

Instead of:

`CLOSED_NEGATIVE`.

---

# 48. Conformance Vector — NS CLOSED

Document labeled `CLOSED` but lacks a proof cert:

Expected:

`StatusCandidate / UNVERIFIED`.

---

# 49. Reference Runtime Module Layout

```text
csm_runtime/
  model/
  schema/
  registry/
  ledger/
  operators/
  transaction/
  replay/
  frontier/
  query/
  projection/
  transfer/
  compiler/
    ns/
  conformance/
```

---

# 50. MVP Boundary

CSM Reference Runtime v0.1 **does not require**:

- LLMs;
- theorem provers;
- GUIs;
- web services;
- distributed databases.

It only requires:

$$
\boxed{
\text{deterministic semantics}
+
\text{registries}
+
\text{ledger}
+
\text{PCOs}
+
\text{transaction}
+
\text{replay}
+
\text{query}
+
\text{conformance}.
}
$$

---

# 51. Runtime Nonclaims

This paper does not claim that:

1. the runtime can automatically prove all theorems;
2. graph completeness can be automatically determined;
3. LLM extraction equals formal verification;
4. state hash equals truth;
5. deterministic replay resolves semantic ambiguity;
6. completion of NS ingestion equals a Clay proof;
7. candidate cuts equal theorem cuts;
8. observed frontiers equal absolute frontiers.

---

# 52. Core Propositions

## 52.1 Ledger Reconstruction Principle

Given fixed ledger, policy, schema, and operator versions:

$$
\boxed{
\mathsf{Replay}
\text{ must reconstruct the native state deterministically}.
}
$$

## 52.2 Transactional Closure Principle

theorem-level mutations:

$$
\boxed{
\text{atomic commit or abort}.
}
$$

## 52.3 Registry Separation Principle

Objects, Certs, Debts, Policies, and Snapshots must not undergo semantic collapse.

## 52.4 Query Authority Principle

Any query result must carry authority / scope / cert / debt / version / source layer metadata.

## 52.5 Candidate Isolation Principle

Heuristic extraction can only enter the Candidate Layer.

## 52.6 NS Safe-Ingestion Principle

NS natural language status labels serve only as hints; closure status must be reconstructed by the runtime calculus.

---

# 53. Next Phase

Paper 09 should return to the first large-scale instance:

$$
\boxed{
\textbf{NS Relative-Global Closure Graph:
Canonical Domain Model and Ingestion Specification}
}
$$

Paper 09 will no longer introduce general CSM foundations, but will begin defining:

- NS target objects;
- formal / generalized / physical domain graphs;
- series ontology;
- route family taxonomy;
- obstruction taxonomy;
- survivor taxonomy;
- artifact inventory schema;
- seed ingestion order;
- cross-series bridges;
- canonical graph construction plan.

---

# 54. Conclusion

Paper 08 transitions CSM from closure calculus into machine semantics.

The entire system now possesses:

$$
\boxed{
\text{State}
+
\text{Events}
+
\text{Operators}
+
\text{Transactions}
+
\text{Registries}
+
\text{Replay}
+
\text{Queries}
+
\text{Conformance}.
}
$$

The most important runtime boundary is:

$$
\boxed{
\text{Candidate uncertainty outside;
deterministic closure authority inside}.
}
$$

And:

$$
\boxed{
\text{No certificate path}
\Rightarrow
\text{No native theorem mutation}.
}
$$

Therefore, when the NS corpus enters the system in the future, it will no longer be a matter of "stuffing hundreds of articles into a graph," but rather compiling each artifact into candidate events, and then progressively passing them through validation, operator transactions, replays, and frontier rebuilds to form a truly auditable observed-relative closure state.

---

## Appendix A — Paper 08 Core Invariants

1. ledger is append-only;
2. native state is replayable;
3. theorem mutations are atomic;
4. candidate layer has no theorem authority;
5. debts do not disappear without discharge;
6. cert revoke/stale does not delete history;
7. projected views must not natively mutate;
8. replay mismatches fail closed;
9. operators/schemas/policies are all versioned;
10. NS status labels serve only as candidate hints;
11. queries must carry authority metadata;
12. observed NS graphs do not masquerade as absolute proof spaces.

---

**END OF CSM PAPER 08 v0.1**