# 05 | Global Scope and Stopping Rules

## Even if this path is completely successful, what can it prove?

When Banwait–Huang Algorithm 1 succeeds, it proves:

> The base curve has an explicit, effectively enumerable infinite quadratic-twist subfamily, whose members are guaranteed to satisfy strong BSD by existing theorems.

It does not prove:

1. All twists of the base curve satisfy BSD;
2. Base curves that fail Algorithm 1 do not have strong-BSD twists;
3. All elliptic curves have such a family;
4. Full BSD holds for all $E/\mathbb Q$.

Therefore, this approach belongs to:

$$
\boxed{
\text{Uniform infinite-family theorem}
}
$$

Rather than:

$$
\boxed{
\forall E/\mathbb Q.
}
$$

---

# Global Value of Phase 1

Even without solving full BSD, it can still produce:

- theorem applicability atlas;
- curve family certificates;
- descent soundness audit;
- data / theorem separation;
- twist generator;
- external result reproduction.

This is highly cumulative work.

---

# Stopping Rules

If for three consecutive rounds we only achieve:

- Increasing the twist bound;
- Listing a few more $d$;
- Recomputing the same batch of curves;
- Only adjusting the runtime;
- No new theorem predicate or certificate;

Then freeze.

Only the following changes can extend the main thread:

1. New theorem family;
2. New descent certificate;
3. New eligibility criterion;
4. Discrepancy / bug with mathematical consequence;
5. Independent global reproduction of the authors' results;
6. Genuinely expanding the family coverage to new types of curves.