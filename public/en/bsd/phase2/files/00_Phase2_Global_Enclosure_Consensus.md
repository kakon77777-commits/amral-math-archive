# 00 | Phase 2 Global Coverage Consensus

## 1. First, Eliminate a False Mainline

Banwait–Huang Remark 2.19 explicitly states:

$$
\operatorname{ord}_2(\#\Sha_{\rm an}(E))=0
$$

holds for all LMFDB curves that actually reach the final `check_BSD_at_2` step in Algorithm 1.

Therefore:

$$
\boxed{
\text{positive }v_2(\Sha_{\rm an})
\text{ does not appear in the current 500K eligible frontier.}
}
$$

Although higher $2$-descent is generally important, it is currently not the bottleneck for increasing Banwait–Huang coverage.

**Verdict: HOLD / TOOLBOX ONLY.**

---

# 2. The Largest Structural Restriction is Semistability

Banwait–Huang Remark 2.10 directly states:

> semistable condition is a strong restriction.

Its impact is primarily in the odd-$p$ part:

1. The additive twist case requires the ramified-prime hypothesis;
2. The irreducible ordinary case requires the ramified-prime bridge;
3. The supersingular case in the existing BSTW corollary carries a squarefree-conductor restriction.

On the other hand:

- The underlying result for the multiplicative case itself does not require a conductor restriction;
- The reducible ordinary case already has non-semistable results;
- Burungale–Castella–Skinner can also handle some non-semistable ordinary irreducible cases;
- Fouquet–Wan directly handles arbitrary reduction types at $p$, but the residual hypotheses have not yet been algorithmized.

Therefore:

$$
\boxed{
\text{The truly worthwhile target is the odd-}p\text{ theorem router.}
}
$$

---

# 3. Why Not Full Rational 2-Torsion?

Banwait–Huang Remark 2.15 explicitly states that the existing $2$-part results they use do not have a corresponding version for full rational $2$-torsion.

While there is indeed new research post-2023 on full-$2$-torsion twists / Selmer / $\Sha[2^\infty]$, it does not currently provide the kind of general strong-BSD infinite-family replacement theorem required by Banwait–Huang.

Therefore:

$$
\boxed{
\text{full }E(\mathbb Q)[2]\cong(\mathbb Z/2)^2
}
$$

is a valuable secondary line of attack, but the theorem gap is larger than that of the non-semistable odd-$p$ route.

---

# 4. Why Not Analytic Rank 1?

Results by Yan–Zhu and others can already handle more good-ordinary $p$-part BSD cases for rank $\le1$.

However, Banwait–Huang Remark 2.11 itself points out that the rank-1 algorithmic extension still encounters residual-image conditions of type `(Im)` which are difficult to determine algorithmically.

Furthermore, the rank 1 family also requires redesigning the $2$-part twist theorem and the generator/regulator layer.

Therefore:

$$
\boxed{
\text{rank 1 = YELLOW}
}
$$

It is not the first Phase 2 project.

---

# 5. The Main Problem of Phase 2

We formulate the research objective as follows:

> Given a non-semistable, analytic-rank-0 optimal elliptic curve $E/\mathbb Q$, can we compile the odd-$p$ hypotheses of Fouquet–Wan into finite, reproducible, base-curve-level predicates, so that Banwait–Huang's $2$-part twist family and the odd-$p$ full-BSD closure can be pieced back together?

Formally:

$$
\boxed{
\mathrm{BH2}(E,d)
+
\forall p>2\,\mathrm{FW}(E_d,p)
\Longrightarrow
\mathrm{BSD}(E_d).
}
$$

Where:

$$
\mathrm{BH2}(E,d)
$$

denotes the $2$-part / nonvanishing conditions of Theorem 2.14.

---

# 6. The Largest Unclosed Quantifier

The real challenge becomes:

$$
\boxed{
\forall p>2.
}
$$

We cannot simply substitute this with full BSD just because:

- most $p$ are good;
- all $p\le B$ are good;
- the residual representation is generically surjective.

Phase 2 must find:

$$
\boxed{
\text{finite exceptional-prime reduction}
}
$$

or admit that this route can only yield a "$p$-part theorem for a fixed finite set of primes".

---

# 7. Current Verdict

$$
\boxed{
\text{GO: Fouquet–Wan Hypothesis Compiler}
}
$$

$$
\boxed{
\text{STOP: Direct higher }2\text{-descent mainline}
}
$$

$$
\boxed{
\text{HOLD: full rational 2-torsion / rank 1}
}
$$