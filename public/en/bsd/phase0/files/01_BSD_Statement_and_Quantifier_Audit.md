# 01 | BSD Proposition, Quantifiers, and Exception Faithfulness Audit

## 1. Basic Objects

Take an elliptic curve defined over $\mathbb Q$:

$$
E:\quad y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6.
$$

The Mordell–Weil theorem gives:

$$
E(\mathbb Q)
\cong
E(\mathbb Q)_{\mathrm{tors}}
\oplus
\mathbb Z^{r_{\mathrm{alg}}}.
$$

Where:

$$
r_{\mathrm{alg}}
=
\operatorname{rank}E(\mathbb Q).
$$

The order of vanishing of the corresponding $L$-function at $s=1$:

$$
r_{\mathrm{an}}
=
\operatorname{ord}_{s=1}L(E,s)
$$

is called the analytic rank.

---

# 2. Three Levels of Claims Must Not Be Conflated

## 2.1 Weak Form

$$
r_{\mathrm{alg}}=r_{\mathrm{an}}.
$$

## 2.2 Finiteness

$$
\Sha(E/\mathbb Q)
$$

is finite.

## 2.3 Leading Coefficient Formula

$$
\frac{L^{(r)}(E,1)}{r!}
=
\frac{
\#\Sha\,
\Omega_E\,
\operatorname{Reg}_E\,
\prod_pc_p
}{
\#E(\mathbb Q)_{\mathrm{tors}}^2
}.
$$

It may happen that:

- The rank equality is proven;
- The finiteness of $\Sha$ is only known for some primes;
- The numerical leading coefficient matches;
- The full strong form remains unproven.

Therefore, the database cannot simply have a single:

```json
{"bsd": true}
```

---

# 3. Global Quantifiers

The full BSD conjecture over $\mathbb Q$ is:

$$
\boxed{
\forall E/\mathbb Q,\quad
\mathrm{BSD\text{-}W}(E)
\land
\mathrm{BSD\text{-}F}(E)
\land
\mathrm{BSD\text{-}S}(E).
}
$$

Its unit of exception is a specific curve.

Any statements like "holds for a positive proportion of curves," "low average rank," or "holds for almost all twists" cannot swallow up a genuine exception.

---

# 4. Three Types of Counterexamples

## 4.1 Rank mismatch

$$
r_{\mathrm{alg}}\ne r_{\mathrm{an}}.
$$

## 4.2 Infinite $\Sha$

Even if rank equality holds, it is still possible that:

$$
\#\Sha=\infty.
$$

## 4.3 Leading coefficient mismatch

Even if rank equality and finiteness hold, the leading coefficient formula may still not match.

Therefore:

$$
\boxed{
\text{Weak BSD holds}
\not\Rightarrow
\text{Strong BSD holds}.
}
$$

---

# 5. $p$-part and the Full Formula

Proving the $p$-part of strong BSD for a certain prime $p$ usually means that the $p$-adic valuations of both sides of the leading coefficient formula match, along with the corresponding Selmer / Iwasawa control.

However:

$$
\boxed{
\text{Uniform control for } \forall p
}
$$

and:

$$
\boxed{
\text{Theorem for a fixed } p
}
$$

are different quantifiers.

The agent must store:

```text
prime p
reduction type
ordinary / supersingular
Eisenstein / non-Eisenstein
local hypotheses
main-conjecture status
p-converse status
```

---

# 6. Isogeny-class Level

The rank and $L$-function of weak BSD remain invariant within an isogeny class.

The individual terms in the strong BSD formula may change among isogenous curves, but the overall prediction is compatible.

Therefore, in Phase 1:

- theorem routing is primarily based on the isogeny class;
- local invariants / exact formulas are primarily based on the curve;
- multiple curves in the same isogeny class should not be treated as independent global samples.

---

# 7. The Proper Status of Numerical Evidence

What LMFDB displays:

$$
\Sha_{\mathrm{an}}
=
\frac{
L^{(r)}(E,1)
\#E(\mathbb Q)_{\mathrm{tors}}^2
}{
r!\,
\Omega_E
\operatorname{Reg}_E
\prod_pc_p
}
$$

is an analytic prediction deduced backwards from the BSD formula.

It can be used for:

- detecting data anomalies;
- finding non-trivial $\Sha$ candidates;
- testing algorithms;
- family statistics.

But without an independent descent / cohomological proof, it cannot be labeled as:

$$
\#\Sha(E/\mathbb Q)\text{ is proven}.
$$

---

# 8. Global Audit Conclusion

BSD is more suitable for the Faithful Globalizer than the RH proportion route, because every curve is an explicit atom.

However, one must still avoid:

$$
\boxed{
\text{Matches in a large database}
\to
\text{Holds for all curves}.
}
$$

The global object in Phase 1 should measure the "certification frontier," rather than masquerading as the truth-value frontier.