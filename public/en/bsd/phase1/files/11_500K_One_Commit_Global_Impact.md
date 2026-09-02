# 11 | 500K One-Commit Global Impact

## 1. Current benchmark

The paper reports that among the

$$
3{,}064{,}705
$$

curves with conductor $<500{,}000$:

$$
1{,}170{,}876
$$

have analytic rank $0$;

After further restricting to semistable, optimal curves with at least two prime factors in the conductor:

$$
178{,}364.
$$

Current Algorithm 1 accepts:

$$
36{,}687.
$$

Therefore:

$$
\frac{36{,}687}{178{,}364}
\approx20.5686\%.
$$

---

## 2. One-commit effect

Git compare:

```text
ec_labels_500k.txt  +2 / -4064
```

The Algorithm 1 predicate change in the same commit is a monotonic tightening.

The output writer is unchanged and identical to the `<150` document; the two modified metadata lines are timestamp/runtime information.

Thus:

$$
4064-2=4062
$$

curve rows were removed.

Reconstructing the old accepted count:

$$
40{,}749.
$$

---

## 3. Impact scale

Proportion removed from the old accepted set:

$$
\frac{4062}{40749}
\approx9.9683\%.
$$

Retained in the new version:

$$
\frac{36687}{40749}
\approx90.0317\%.
$$

In the pre-candidate pool:

$$
22.8460\%
\to
20.5686\%.
$$

A decrease of approximately:

$$
2.2774
$$

percentage points.

For all $3{,}064{,}705$ curves:

$$
1.3296\%
\to
1.1971\%.
$$

This single semantic correction alone accounts for approximately:

$$
0.1325
$$

percentage points across the entire data domain.

---

## 4. Global cause union

Because Algorithm 1 has only two theorem-level changes in this commit:

1. strict $3/5/7$ rational-isogeny exclusion;
2. independent $a_3\ne\pm3$;

every one of the $4062$ removed curves must fall into:

$$
\boxed{
\text{new strict isogeny failure}
\;\cup\;
\{|a_3|=3\}.
}
$$

This is the **set-level closure** of all causes.

However, the exact histogram for each gate remains unknown, and the $9/2/1/1$ ratio from `<150` cannot be extrapolated to 500K.

---

## 5. Research interpretation

This is not a new BSD theorem.

What it demonstrates is:

> A seemingly minor correction to the theorem predicate can alter approximately $10\%$ of the old accepted base-curve universe.

Therefore, for Agent systems:

$$
\boxed{
\text{semantic versioning is not an engineering add-on, but a part of mathematical soundness.}
}
$$