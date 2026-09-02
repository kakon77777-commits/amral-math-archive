# 14 | Phase 1 Next Lowest-Cost Gate

## Do Not Directly Rerun the Full Algorithm 1

Do the following first:

### Gate A — Delta-only base verifier

Input: old accepted list + `a3/isogeny_degrees`.

Goal:

$$
40{,}749
\to
36{,}687.
$$

### Gate B — Twist JSON parser diff

Directly materialize:

```text
old twists_of_ec_labels_500k.json
current twists_of_ec_labels_500k.json
```

Compute:

1. removed base keys;
2. stable base keys;
3. stable curves with twist changes;
4. twists removed only by gcd(3N);
5. twists added after deleting old disc gate;
6. both-effect curves.

### Gate C — Only then full Sage replay

If both A and B match the repository's current outputs, only then rerun all expensive descents.

---

# Why?

The full Algorithm 1 current paper runtime of about ten or so minutes is not actually expensive in itself.

What is truly expensive is **the rework caused by research semantic errors**.

A delta-first approach allows us to first confirm:

$$
\boxed{
\text{We understand the same theorem version.}
}
$$

Then proceed to full proof-engineering.