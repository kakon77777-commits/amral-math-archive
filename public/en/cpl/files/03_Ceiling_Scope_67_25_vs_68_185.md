# 03 — $67.25\%$ and $68.185\%$: The Scopes of Two Ceilings

## 1. Why They Must Be Distinguished

Currently, the most common misinterpretation is:

$$
67.25\%<68.185\%.
$$

One cannot therefore claim that "if Claude's window is optimized a bit more, it can reach $68.185\%$."

---

## 2. The Exact Scope of $67.25\%$

Claude §7.1 optimizes the window functional, obtaining the Montgomery--Taylor kernel. The main paper then cites CCLM17 Corollary 14 to explain that in the one-delta extremal problem using only Montgomery's $F(\alpha)$ on $[-1,1]$, this kernel is extremal.

The paper's own phrasing summarizes this scope as:

$$
\boxed{
\text{block structure + two traces + primes up to }T
}
$$

Therefore:

$$
0.672500\ldots
$$

is the extremum of this **window-optimization / two-trace sub-framework**.

---

## 3. The Exact Known Extent of $68.185\%$

Remark 1.1 states that using only:

- mean density;
- pair-correlation data with Fourier support $(-1,1)$;
- multiplicity integrality;
- and requiring the certificate to hold for every configuration;

an explicit extremal law shows that the simple-zero certificate cannot exceed:

$$
0.68185.
$$

This is a broader statement than the §7.1 window class.

However, in the main text of the paper read so far, the complete extremal-law derivation for $0.68185$ is not explicitly expanded into a directly recalculable closed-form formula like $c_1^*$.

Therefore, this research package marks it as:

$$
\boxed{\text{OPEN-RECONSTRUCTION-01}}
$$

The research task is not to doubt the number, but to:

> Find the complete definition, variables, constraints, optimizer, and numerical reproduction path of this extremal law.

---

## 4. Another Cap Provided in §7.5

Proposition 7.4 gives a finite-dimensional dimension cap: if the support length of the test functions corresponds to $\lambda$, then

$$
\operatorname{rank}P\le d\approx\lambda N.
$$

Thus, no finite compression of the same type can certify more than approximately $\lambda N$ on-line points.

Meanwhile, certificates relying solely on the first/second trace are not even positive when $\lambda\le1/2$; and for $1/2<\lambda<1$, the unconditionally available higher moments are restricted by the Rudnick--Sarnak range

$$
k\lambda<2
$$

and are unable to provide new even-moment gains.

This indicates that "just computing more moments" is not free even in the unconditional bandwidth-one region.

---

## 5. Practical Implications for $P_{70}$

It can currently be confirmed that:

$$
P_{70}
$$

is already outside of:

$$
70\%>68.185\%
$$

this limit.

Therefore, if the certificate class assumptions of Remark 1.1 fully apply, $P_{70}$ must break at least one of these restrictions:

$$
\boxed{
\text{more support}
\ \lor\ 
\text{more correlation information}
\ \lor\ 
\text{richer non-configuration-wise/global structure}
}
$$

The conditional fourth-moment route is exactly the second category; the support $>1$ route is the first category.

---

## 6. Next Steps

1. Trace the bibliography / supplementary / Lean audit to see if they contain the formal statement of the extremal law from Remark 1.1;
2. Search whether the authors / Anthropic have separately published a numerical notebook;
3. If not, build a configuration LP / moment problem ourselves from the bandwidth-one pair-correlation + integrality constraints, and attempt to numerically reproduce $0.68185$;
4. If reproducible, formally study its dual certificate and escape directions.