# 04 | 500K Preflight

This runtime does not independently recompute the 500K official output.

Prior to scaling up, the following sequence is executed:

1. Lock Sage / LMFDB / Git SHA / descent backend;
2. current `<150` exact replay;
3. 13 old-only first-failure replays;
4. four discrepancy exact rejection replays;
5. Only then run conductor `<500000`.

The 500K run must output:

```text
passed.csv
failed.csv
unknown.csv
predicate_trace.jsonl
descent_certificates/
run_manifest.json
hashes.txt
```

`unknown.csv` must not be discarded, otherwise timeouts / backend failures will be misinterpreted as mathematical rejections.

The criterion for success is not "the final count is very close", but rather:

$$
\boxed{
\text{final set exact}
+
\text{stage counts reproducible}
+
\text{adversarial corpus stable}
+
\text{certificate semantics stable}.
}
$$