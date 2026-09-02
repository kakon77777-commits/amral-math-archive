# 00 | BSD Global Envelopment Consensus Ruling

## 0. In One Sentence

BSD is indeed more "human-readable" than RH:

$$
\boxed{
\text{LHS: Behavior of }L(E,s)\text{ at }s=1
\quad\Longleftrightarrow\quad
\text{RHS: Rational points, local data, and }\Sha
}
$$

The terminology barrier is high, but each term is a high-value, strongly-typed, computable, or certifiable mathematical object.

This makes BSD particularly suitable for multi-agent division of labor.

---

# 1. Current Global Ruling

$$
\boxed{
\text{GO: Enter Phase 1.}
}
$$

However, we will not directly treat the "full BSD" as a single task.

First, restrict to:

$$
E/\mathbb Q.
$$

Then, decompose the conjecture into three layers:

## BSD-W: Weak BSD / Rank Equality

$$
\boxed{
\operatorname{rank}E(\mathbb Q)
=
\operatorname{ord}_{s=1}L(E,s).
}
$$

## BSD-F: Finiteness of $\Sha$

$$
\boxed{
\#\Sha(E/\mathbb Q)<\infty.
}
$$

## BSD-S: Strong BSD Leading Coefficient Formula

If:

$$
r=\operatorname{rank}E(\mathbb Q),
$$

then:

$$
\boxed{
\frac{L^{(r)}(E,1)}{r!}
=
\frac{
\#\Sha(E/\mathbb Q)\,
\Omega_E\,
\operatorname{Reg}(E/\mathbb Q)\,
\prod_p c_p
}{
\#E(\mathbb Q)_{\mathrm{tors}}^2
}.
}
$$

Different normalizations may adjust notations such as the period; research data must preserve the adopted convention.

---

# 2. Why is it worth doing now?

BSD possesses four characteristics that are highly advantageous for Agents.

## 2.1 Typed objects

```text
curve
conductor
local reduction
L-function
analytic rank
Mordell–Weil generators
Selmer group
Tamagawa numbers
regulator
torsion
Tate–Shafarevich group
```

Each item can have an independent Agent, tool, and verifier.

## 2.2 Strong Closure Already Exists for Low Ranks

The weak BSD for analytic ranks $0$ and $1$ already has a core closure established by Gross–Zagier, Kolyvagin, and the Modularity Theorem.

This means Agents do not need to invent the entire theory from scratch; they can first learn to identify "which theorem is applicable."

## 2.3 A Complete Benchmark Can Be Established

The LMFDB data for $E/\mathbb Q$ with conductors less than $500{,}000$ is complete, thus a finite, replayable full-scale experimental domain can be established.

## 2.4 Failures Still Yield Cumulative Results

Even if the full BSD cannot be proven, we can still obtain:

- theorem applicability atlas;
- certificates for certain $p$-parts;
- twist-family classifications;
- high-rank wall maps;
- $\Sha$ prime-support lists;
- counterexamples for algorithms and data quality;
- exact numerical certificate pipelines.

---

# 3. Mark the Real Walls First

## 3.1 The High-Rank Wall

For general:

$$
r_{\mathrm{an}}\ge2,
$$

there currently does not exist a universally closed Gross–Zagier–Kolyvagin bridge like there is for ranks $0/1$.

## 3.2 The $\Sha$ Wall

Numerical BSD can infer:

$$
\#\Sha_{\mathrm{an}},
$$

but:

$$
\boxed{
\text{analytic predicted order}
\neq
\text{proved finite group order}.
}
$$

## 3.3 The All-Prime Unification Wall

Proving a specific $p$-part:

$$
\operatorname{ord}_p(\#\Sha)
$$

does not equate to proving the complete formula for all primes.

## 3.4 The All-Curve Quantifier Wall

Even if all conductors $\le500{,}000$ are processed, it is still just a finite benchmark:

$$
\boxed{
\text{finite database closure}
\neq
\forall E/\mathbb Q.
}
$$

---

# 4. First Main Track

$$
\boxed{
\text{Strong-BSD Twist-Family Reproduction}
+
\text{BSD Certificate Atlas}
}
$$

Use the 2024 zeta-element / Iwasawa work and the 2026 Banwait–Huang algorithmization work as the external foundation.

The first phase does not seek new theorems, but first requires:

1. Whether their hypotheses can be reproduced;
2. Whether they can be rerun over the complete domain of conductors $\le500{,}000$;
3. Whether each determination can output a machine-checkable applicability certificate;
4. Which curves are excluded and for what reasons;
5. Which conditions repeatedly become common bottlenecks.

---

# 5. Second Main Track

$$
\boxed{
\text{High-Rank Wall Atlas}
}
$$

First, use:

$$
389.a1
$$

curves of rank $2$ like this as samples.

LMFDB numerically provides the complete BSD identity, but we must annotate item by item:

- Which quantities are exact;
- Which quantities are rigorous analytic computations;
- Which quantities are merely inferred from BSD;
- Which $\Sha$ information has been proven;
- Which theorems are no longer applicable.

This will have more research value than merely generating another beautiful numerical equality.

---

# 6. Stopping Rules

If any track for three consecutive rounds only achieves:

- Increasing numerical precision;
- Restating BSD;
- Renaming the same gap;
- Replaying the same formulas on new curves;
- Substituting actual $\Sha$ with analytic $\Sha$;

without:

- New theorem applicability;
- New exact certificates;
- New exclusion domains;
- New families;
- New barrier escapes;

then it shall be frozen.

---

# 7. Conclusion of This Round

BSD is not guaranteed to be easier to solve than RH.

But it is easier to answer:

$$
\boxed{
\text{Which typed component has actually been proven now?}
}
$$

Therefore, it deserves to be the next official Agent mathematics project.