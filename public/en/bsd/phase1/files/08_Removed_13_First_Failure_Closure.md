# 08 | Removed 13 First-Failure Closure

v0.2 conservatively labeled the 13 removed curves as:

```text
VERSION_REGRESSION_REMOVED
reason = OPEN
```

v0.3 has utilized:

1. exact one-commit diff;
2. official old/current fixture mapping;
3. LMFDB / Cremona primary curve/isogeny data;
4. an exact finite-field count;

to complete the first-failure closure.

## Histogram

$$
9\times P\_ISOGENY\_3,
$$

$$
2\times P\_ISOGENY\_5,
$$

$$
1\times P\_ISOGENY\_7,
$$

$$
1\times A3\_ABS\_3.
$$

## Complete Table

| Curve | LMFDB | First failure |
|---|---|---|
| 14a1 | 14.a6 | P_ISOGENY_3 |
| 34a1 | 34.a4 | P_ISOGENY_3 |
| 66c1 | 66.c3 | P_ISOGENY_5 |
| 26a1 | 26.a2 | P_ISOGENY_3 |
| 26b1 | 26.b2 | P_ISOGENY_7 |
| 35a1 | 35.a3 | P_ISOGENY_3 |
| 38a1 | 38.a3 | P_ISOGENY_3 |
| 38b1 | 38.b2 | P_ISOGENY_5 |
| 106a1 | 106.c2 | P_ISOGENY_3 |
| 110c1 | 110.a1 | P_ISOGENY_3 |
| 110b1 | 110.c1 | P_ISOGENY_3 |
| 142e1 | 142.c1 | A3_ABS_3 |
| 142d1 | 142.e2 | P_ISOGENY_3 |

`26b1` also has a secondary failure:

$$
a_3=-3.
$$

However, the production pipeline executes the strict isogeny gate first, so the first failure is `P_ISOGENY_7`.

## Key Conclusion

The 25→12 reduction in the small sample is no longer a black-box version drift:

$$
\boxed{
\text{13 removed curves are fully explained by the new Algorithm1 predicates.}
}
$$