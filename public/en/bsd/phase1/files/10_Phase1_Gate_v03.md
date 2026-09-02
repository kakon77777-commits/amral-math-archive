# 10 | Phase 1 Gate v0.3

The `<150` regression for Phase 1 is now divided into four tiers:

## A. Positive base fixture

Current $12$ fixtures:

```text
must PASS
```

## B. Historical removed fixture

Old-only $13$ fixtures:

```text
must FAIL at the now-closed predicate map
```

Simply returning `not in final output` is no longer permitted.

## C. Explicit discrepancy corpus

The four official discrepancy curves:

```text
must remain rejected for theorem-level reasons
```

## D. Algorithm2 semantic unit fixtures

Even if the 12 positive twist outputs remain completely unchanged, the following must still be tested directly:

- `TWIST_GCD_3N`
- `TWIST_DISC_VAL_GATE_REMOVED`

## 500K Gate

Only when A+B+C+D all pass is it permitted to label the 500K results as:

```text
REPRODUCTION-QUALIFIED
```

Otherwise, they can at most be labeled as:

```text
OUTPUT-MATCHED
```

These two labels must not be mixed.