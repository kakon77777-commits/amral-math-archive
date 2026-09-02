# 00 | Phase 1 v0.2 Convergence Verdict

## Conclusion of this Round

$$
\boxed{
\text{The Phase 1 small sample has been upgraded from "result reproduction" to "versioned certificate regression".}
}
$$

v0.1 has independently reproduced the two representative branches of Algorithm 2.

v0.2 adds:

1. Complete diff between the May 22 old fixture and the June 3 current fixture;
2. Independent adversarial corpus from the official discrepancy report;
3. Controlled failure dictionary for false-positive / unknown / timeout / testing-only;
4. Soundness preflight for the 500K rerun;
5. Data stratification of "version regression does not equal mathematical rejection reason";
6. Executable regression test.

The old fixture has $25$ items, and the current fixture has $12$ items; the current set is a subset of the old set with no additions, exactly removing $13$ items.

This demonstrates that theorem-producing code cannot merely save the final success list, but must preserve the version history of its mathematical semantics.

## Two Adversarial Corpora

### Corpus A — Version Regression

It only answers:

> Which curves were previously passed by the old official pipeline, but are no longer passed by the current version?

It only proves membership change, and cannot automatically infer the mathematical rejection reason for each curve.

### Corpus B — Explicit Discrepancy

The official `discrepancy_report.txt` lists the current rejection reasons predicate by predicate for four curves.

This is the true theorem-level adversarial corpus.

## New Gate

Before proceeding to the 500K run, it must simultaneously pass:

$$
\boxed{
\text{Current positive fixture}
+
\text{Historical regression}
+
\text{Explicit discrepancy corpus}.
}
$$