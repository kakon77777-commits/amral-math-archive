# 16 | Phase 1 Completion and Phase 2 Interfaces

## Phase 1 Completed

Completed:

1. Theorem 2.18 predicate map;
2. Algorithm2 independent reproduction;
3. paper/current-code soundness audit;
4. `<150` version regression;
5. 13 removed curves first-failure closure;
6. 500K exact artifact census;
7. Algorithm1 4062 removal cause closure;
8. stable-domain OLD→CURRENT Algorithm2 semantic replay.

Therefore, Phase 1 can be concluded:

$$
\boxed{
\text{Banwait–Huang Reproduction = COMPLETE}
}
$$

## No Longer Worth Primary Focus

The historical twist reconstruction of the 1,355 OLD-only curves is doable, but they are no longer in the CURRENT Algorithm1 accepted universe.

Unless the objective shifts to:
- repository history paper;
- proof-engineering case study;
- full historical reproducibility archive;

Otherwise, the marginal benefit to BSD itself is low.

## Phase 2 Recommendations

### Route A — High-Rank Wall Atlas

Starting from rank $2+$ curves, establish component by component:
- rigorous analytic rank;
- Mordell–Weil rank upper/lower;
- Selmer;
- $\Sha$ finiteness / p-parts;
- leading coefficient.

### Route B — Strong-BSD Coverage Expansion

Question:
> Can we use known theorems from 2024–2026 to further expand the eligible family of Banwait–Huang Algorithm1, rather than just reproducing the original algorithm?

Only then might we start generating new external mathematical results.

### Route C — 2-primary unresolved frontier

Currently, the current code conservatively rejects positive analytic $v_2(\Sha)$.

We can establish:
- families of curves tractable by higher 2-power descent;
- which rejections are merely due to insufficient computation/certificates;
- whether off-the-shelf theorems / Magma/Sage exact descent can expand the certified set.

This is the most natural new mathematical interface left by Phase 1.