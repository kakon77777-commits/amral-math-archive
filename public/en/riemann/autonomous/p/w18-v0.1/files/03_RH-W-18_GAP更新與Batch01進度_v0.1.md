# RH-W-18: GAP Update and Batch 01 Progress

## Work Nodes Closed in This Round

- Unified historical certificate status vocabulary.
- Established a single manifest and dependency graph.
- Established the SHA-256 artifact identity layer.
- Established the native verifier adapter layer.
- Established claim normalization and the RH claim firewall.
- Established a red-team for hashes, semantic parameters, and claim escalation.
- Publicly documented W-06 legacy incomplete and W-14 supersession.

## Not Yet Closed

- The missing original 2×2 prime-active artifact from W-06 has not yet been recovered.
- The backend has not yet achieved proof object verification at the Lean/Coq layer.
- Historical transcendentals still rely on the documented software contract of each round, rather than a common formalized core.
- Schema migration is currently handled by the adapter; not all old JSONs have been converted in-place to canonical payloads yet.

## Batch 01

$$
\boxed{\texttt{RH-W-18}/\texttt{RH-W-20}}
$$

Currently $18/20$ completed, with two rounds remaining.

Next node:

$$
\boxed{\texttt{RH-W-19-REPRODUCIBILITY-AND-ADVERSARIAL-AUDIT}}
$$

W-19 will not only test the backend itself, but will also establish a publicly available zoo of erroneous certificates: missing prime powers, incorrect knot pieces, $M/G$ parameter mismatches, non-outward intervals, floating-point false negatives, tail bound truncations, and witness version mismatches, requiring the backend to provide classifiable reasons for rejection.