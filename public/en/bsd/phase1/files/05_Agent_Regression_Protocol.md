# 05 | Agent Regression Protocol

Before modifying the theorem router, each Agent must run three layers of tests:

- Layer A: current 12 positive fixtures;
- Layer B: old-only 13 historical regressions;
- Layer C: official discrepancy four.

Output format:

```json
{
  "curve": "...",
  "decision": "PASS | FAIL | UNKNOWN",
  "first_failure": "...",
  "all_failures": [],
  "evidence": [],
  "code_version": "...",
  "semantic_version": "..."
}
```

Cognitive firewall:

- `analytic Sha = 1` does not equal `Sha is trivial`;
- `rank = 0` does not automatically equal rigorous analytic rank $0$;
- The 2-descent dimension being numerically equal to the analytic valuation does not automatically mean BSD$(E,2)$ is proven;
- A timeout must be `UNKNOWN`.

If the new version only improves runtime/cache/batching/output formatting, label it `ENGINEERING ONLY`; it is not counted as mathematical progress on BSD.