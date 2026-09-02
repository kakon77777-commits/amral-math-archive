# RH-W-20: Batch 02 Handoff and Platform Import Specifications

## 1. Handoff Objects

Batch 02 should not merely read the final summary, but should load:

1. `research_nodes.json`: Twenty rounds of typed nodes.
2. `dependency_graph.json`: Research relay and recertification edges.
3. `claim_ledger.json`: Finite claims and scope.
4. `failure_and_revision_log.json`: Failures, revisions, and disposition.
5. `certificate_index.json`: Executability and trust status.
6. `trust_boundary.json`: Matters that the backend cannot guarantee.
7. `handoff_batch_02.json`: The next batch of candidate tracks.

## 2. Suggested Batch 02 Main Axes

The priority order does not need to equal the round order, but it is recommended to maintain at least two parallel main tracks:

- **Trustworthiness Track:** Signatures, secondary verifiers, reproducible builds, and formalized kernels.
- **Mathematics Track:** Multi-event chamber graphs, prime-power entry surfaces, anisotropic low-spectral manifolds, dictionary expansion, and completeness stress testing.

## 3. Minimum Platform Import Contract

The frontend or database must:

- Not rewrite `node_id`, `claim_id`, or `event_id`;
- Preserve typed status, and not display all successful executions as a uniform "Proven";
- Display `rh_claim=false`;
- Allow a single node to simultaneously possess finite results and incomplete tasks;
- Render `RECERTIFIES` separately from standard dependencies;
- Not hide historical gaps due to the success of subsequent nodes.

## 4. Platform Significance of Case 0001

This case is not intended to prove that AI has solved the RH, but rather to demonstrate:

> How an AI research process can, on a long-standing open problem, form relayable nodes, replayable finite certificates, visible failures and revisions, and trust boundaries that are not erased by a success narrative.