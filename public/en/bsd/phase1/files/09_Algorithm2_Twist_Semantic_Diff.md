# 09｜Algorithm 2 Twist Semantic Diff

## Code semantics changed

### Tightening

$$
\gcd(M,N)=1
\to
\gcd(M,3N)=1.
$$

When $3\nmid N$, any old candidate with $3\mid M$ will be rejected by the new gate.

### Relaxation

The old version additionally required a twist-side discriminant-valuation ramification-style condition.

The current version has removed this predicate.

Therefore, there exist candidates that:

- Were rejected by this gate in the old version;
- Are no longer rejected for this reason in the new version.

## But the small fixture did not test this

For the 12 surviving base curves, the old/current `twists_of_ec_labels_150.json`:

$$
\boxed{
\text{exact match}.
}
$$

Therefore, this fixture can only verify that "the current results remain unchanged", but cannot verify that the two new semantic branches are actually exercised.

## Solution

Add two synthetic semantic cases.

### Case A

Take:

$$
N=46,\qquad M=3.
$$

Then:

$$
\gcd(3,46)=1,
$$

But:

$$
\gcd(3,138)=3.
$$

This can directly distinguish between the old and new coprimality gates.

### Case B

Abstract setting:

$$
p=3,\quad q\in\{2,5\},
$$

and:

$$
v_2(\Delta)=3,\quad v_5(\Delta)=6.
$$

For $p=3$, the old `disc_valuation_condition` could not find a witness with a valuation that is not a multiple of 3, and therefore rejected it; the current program no longer has this gate.

This is merely a predicate-level regression fixture and does not claim to correspond to an actual theorem-eligible twist.