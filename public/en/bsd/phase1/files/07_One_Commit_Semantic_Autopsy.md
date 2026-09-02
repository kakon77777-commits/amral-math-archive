# 07 | One-Commit Semantic Autopsy

## Commit distance

Old fixture commit:

`1a0489c3c3099dd0c248624e6621df73ae8f0d43`

Current commit:

`31fae20c8df3f1f0383f41112b914d4995d5809d`

The difference between the two is exactly one commit.

## Algorithm 1

The old version did not uniformly exclude $3,5,7$-isogenies; instead, it constructed a dynamic set:

$$
A_{\mathrm{old}}
=
\{3: 3\mid N\text{ or }|a_3|=3\}
\cup
\{5:5\mid N\}
\cup
\{7:7\mid N\}.
$$

It only excluded:

$$
p\in A_{\mathrm{old}}
$$

rational $p$-isogenies.

The new version changed this to:

$$
A_{\mathrm{new}}=\{3,5,7\},
$$

and additionally added:

$$
a_3(E)\neq\pm3.
$$

This is a substantive tightening of the theorem predicate, not a performance refactoring.

## Algorithm 2

In the same commit:

$$
\gcd(M,N)=1
\quad\longrightarrow\quad
\gcd(M,3N)=1,
$$

but simultaneously removed the old twist-side `disc_valuation_condition`.

Therefore, Algorithm 2 simultaneously contains:

- a shrink mechanism;
- an expand mechanism.

It cannot be summarized in a single direction as "the new version is stricter".