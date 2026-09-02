# 05 | Audit of Neo.K's Old "Grid Rank Convergence" Route

## 0. Contents of the Old Draft

An internal old draft previously proposed:

1. Grid discretization of elliptic curves;
2. Computing the grid $L$-function;
3. Defining the grid rank;
4. Defining the grid order of vanishing;
5. Claiming some form of grid BSD relation;
6. Taking the limit:
   $$
   a\to0;
   $$
7. Using "continuity to guarantee the equality holds."

This route currently cannot be included in the main proof.

---

# 1. The First Circularity: Grid BSD Relation

If it is assumed at each scale that:

$$
\operatorname{rank}_a(E)
\le
\operatorname{ord}_{s=1}L_a(E,s),
$$

and even ultimately requiring equality in the limit, then one must explain where this inequality comes from.

If its proof already uses a classical BSD-type connection, then the argument is circular.

---

# 2. Rank is Not an Ordinary Continuous Quantity

$$
\operatorname{rank}E(\mathbb Q)
$$

is an integer-valued, global arithmetic invariant.

The "approximate number of points", "matrix rank", or "discrete homological rank" on a numerical grid will not, due to:

$$
a\to0
$$

automatically converge to the Mordell–Weil rank.

One must establish:

$$
\boxed{
\text{grid certificate}
\Longleftrightarrow
\text{rational-point independence / Selmer bound}.
}
$$

---

# 3. The Order of Vanishing is Also Not Preserved by Ordinary Function Convergence

Even if:

$$
L_a(E,s)\to L(E,s)
$$

converges in some region, it does not automatically imply:

$$
\operatorname{ord}_{s=1}L_a(E,s)
\to
\operatorname{ord}_{s=1}L(E,s).
$$

The order of vanishing is not continuous with respect to small perturbations.

It requires at least:

- Analytic control in the neighborhood of $s=1$;
- Uniform convergence of derivatives;
- Exact vanishing of lower derivatives;
- The first non-zero derivative and its error margin;
- No spurious grid zeros.

---

# 4. "Both Sides Converging" Does Not Imply "Equality of Limits"

From:

$$
A_a\to A
$$

and:

$$
B_a\to B
$$

one cannot deduce:

$$
A=B.
$$

Unless there is a valid relation for each $a$:

$$
A_a=B_a
$$

and all limits are compatible with their definitions.

But if $A_a=B_a$ is precisely the grid BSD, the difficulty has merely been shifted to the grid level.

---

# 5. Four Independent Theorems are Required to Salvage This

## GR-1: Faithful discretisation

The grid objects must preserve:

- rational points;
- group law;
- torsion;
- height;
- local reduction.

## GR-2: Rank certificate equivalence

The grid rank must be equivalent to:

$$
\operatorname{rank}E(\mathbb Q),
$$

rather than a visual/numerical rank.

## GR-3: Analytic-order stability

The zero order of the grid $L$-function must be preserved by a rigorous analytic certificate.

## GR-4: Non-circular bridge

The equality between GR-2 and GR-3 cannot presuppose BSD.

Currently, none of these four items have been accomplished.

---

# 6. Verdict

$$
\boxed{
\text{Archive as exploratory analogy;}
\quad
\text{do not use as Phase 1 proof route.}
}
$$

The only things that can be retained are the engineering concepts:

- Multi-scale checking;
- Representation consistency;
- Exact certificate;
- Limit audit.

The theorem claim that "continuity guarantees BSD equality" cannot be retained.