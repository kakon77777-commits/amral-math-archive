# 13 | 500K Twist Output Non-Monotonicity

## Observation

On the same commit:

```text
twists_of_ec_labels_500k.json
+1899 / -53404
```

However, the Algorithm 1 base-curve set only shrinks.

If the twist JSON changed solely due to base curves being deleted:

$$
\text{diff additions}
$$

should at most come from a very small number of punctuation / context changes, and there would not be $1899$ added lines.

Therefore, the full output indicates:

$$
\boxed{
\text{Algorithm2 semantic change is active somewhere in the large domain.}
}
$$

---

## Two Predicate Changes in Opposite Directions

### Shrink

$$
\gcd(M,N)=1
\to
\gcd(M,3N)=1.
$$

This removes the $3\mid M$ candidates allowed in the old version (when $3\nmid N$).

### Expand

Deleting the old:

```text
disc_valuation_condition
```

might allow some $M$ previously blocked by the ramification-style gate to be added.

Therefore:

$$
\boxed{
\text{twist output need not be monotone}.
}
$$

---

## Why Can't We Simply Say "1899 Twists Added"?

Git diff counts **lines**, while the JSON simultaneously contains:

- key lines;
- bracket/comma structural lines;
- twist integer lines;
- entirely deleted base blocks.

Therefore:

$$
1899
$$

are added diff lines, not a proven unique new twist count.

A complete entry-level census requires materializing the old/current JSON and then parsing the set difference.

---

## Small fixture coverage failure

For the 12 currently surviving curves `<150`:

$$
T_{\rm old}(E)=T_{\rm new}(E)
$$

holds for each curve.

Thus, the branch coverage of the small positive fixture for this semantic diff in Algorithm 2 is:

$$
\boxed{
0\text{ observed output deltas}.
}
$$

This is why v0.3 added synthetic semantic tests, and v0.4 requires a full-file entry census.