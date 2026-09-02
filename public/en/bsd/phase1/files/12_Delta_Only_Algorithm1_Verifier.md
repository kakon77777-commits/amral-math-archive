# 12 | Delta-Only Algorithm1 Verifier

## Purpose

Do not rerun initially:

- L-value merge;
- 2-descent;
- $E'$ descent;
- $\mathcal S$;
- All old filters.

Because every curve in the old output has already passed old Algorithm1.

For the old accepted set:

$$
\mathcal C_{\rm old},
$$

the current set only needs to compute:

$$
\mathcal C_{\rm new}
=
\left\{
E\in\mathcal C_{\rm old}:
\{3,5,7\}\cap I(E)=\varnothing,\;
|a_3(E)|\ne3
\right\},
$$

where:

$$
I(E)
$$

is the set of rational prime-degree isogeny degrees.

This is an **incremental proof replay**.

---

## Why is it exact?

There is only one commit from old → current.

The theorem predicate difference of Algorithm1 has no other loosen/tighten gates.

Therefore, for the known old PASS rows:

$$
\boxed{
\text{new membership}
=
\text{strict-isogeny gate}
\land
a_3\text{ gate}.
}
$$

There is no need to redo unchanged proof obligations.

---

## Input Minimization

Each curve only requires:

```json
{
  "cremona_label": "...",
  "a3": 0,
  "isogeny_degrees": [1,2,3,6]
}
```

If the local LMFDB is connected, these two fields are very cheap:

- `a3`: the $p=3$ term of the `aplist` class;
- `isogeny_degrees`: curve table metadata.

---

## Success Gate

Input old version:

$$
40{,}749
$$

curves.

Expected:

$$
\text{PASS}=36{,}687,
$$

$$
\text{FAIL}=4{,}062.
$$

And output the full failure histogram:

```text
P_ISOGENY_3
P_ISOGENY_5
P_ISOGENY_7
A3_ABS_3
multi-failure
```

This will be the first 500K semantic-cause census.

---

## Implications of Failure

If the delta-only verifier cannot obtain the current official set, then at least one of the following holds:

1. We missed a semantic diff;
2. The LMFDB release is different;
3. The old/current outputs are not from the same data snapshot;
4. The metadata mapping is incorrect;
5. The implementation has undocumented side effects.

At this point, we should stop and not proceed directly to a full replay.