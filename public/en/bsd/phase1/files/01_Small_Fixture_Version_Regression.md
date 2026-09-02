# 01 | Small Sample Version Regression: 25 → 12

## Old fixture

Date: $2026$-$05$-$22$.

Total: $25$, of which $10$ are CLZ20 and $15$ are Zha16.

## Current fixture

Date: $2026$-$06$-$03$.

Total: $12$, of which $7$ are CLZ20 and $5$ are Zha16.

## Exact diff

Retained $12$, removed $13$, added $0$.

Removed list:

```text
106a1, 110b1, 110c1, 142d1, 142e1, 14a1, 26a1, 26b1, 34a1, 35a1, 38a1, 38b1, 66c1
```

## Do not overinterpret

This diff only indicates that a certain curve changed from `PASS` in the old version to non-`PASS` in the current version.

Until replayed filter-by-filter, uniformly mark as:

```text
VERSION_REGRESSION_REMOVED
reason = OPEN
```

Do not infer mathematical reasons from commit messages, branch distributions, or intuition.