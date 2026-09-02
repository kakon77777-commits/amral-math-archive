# 03 | Quadratic-Twist Invariance Bridge

## 0. Purpose

The Fouquet–Wan theorem applies to a single:

$$
E_d,\ p
$$

What Banwait–Huang requires is:

$$
\text{a base }E
\Longrightarrow
\text{infinitely many }d.
$$

Therefore, the FW hypotheses must be reduced from the twist level back to the base level.

---

# 1. Residual representation under quadratic twist

For odd $p$:

$$
\bar\rho_{E_d,p}
\cong
\bar\rho_{E,p}\otimes\chi_d.
$$

where:

$$
\chi_d:G_\mathbb Q\to\{\pm1\}\subset\mathbb F_p^\times.
$$

---

# 2. Candidate Lemma A — irreducibility invariance

Tensoring by a 1-dimensional character is a category auto-equivalence.

Thus:

$$
\boxed{
\bar\rho_{E,p}\text{ absolutely irreducible}
\iff
\bar\rho_{E_d,p}\text{ absolutely irreducible}.
}
$$

This condition can be completely reduced to the base curve.

---

# 3. Candidate Lemma B — local semisimplification degeneracy invariance

If FW-H2 excludes the form:

$$
\bar\rho|_{G_{\mathbb Q_p}}^{ss}
\cong
\bar\chi
\oplus
\bar\chi_{\rm cyc}\bar\chi
$$

then after twisting:

$$
(\bar\rho\otimes\chi_d)^{ss}
\cong
(\bar\chi\chi_d)
\oplus
\bar\chi_{\rm cyc}(\bar\chi\chi_d).
$$

Therefore, the property that "there exists some common character $\bar\chi$ causing it to fall into the forbidden form" should remain invariant.

If the FW simplified theorem also excludes other equal-character cases, their twist-invariance must similarly be proven case by case.

**Status: Candidate for standard representation theory derivation; formal documentation requires checking against each theorem version.**

---

# 4. Candidate Lemma C — split-at-$\ell$ local preservation

The Banwait twist condition requires that the base conductor primes split in:

$$
K_d=\mathbb Q(\sqrt d)
$$

If:

$$
\ell\mid N
$$

splits in $K_d$, then the quadratic character is trivial on:

$$
G_{\mathbb Q_\ell}
$$

Therefore:

$$
\boxed{
\bar\rho_{E_d,p}|_{G_{\mathbb Q_\ell}}
\cong
\bar\rho_{E,p}|_{G_{\mathbb Q_\ell}}.
}
$$

Thus, any FW-H3 local certificate using this $\ell$ as a witness can be preserved along the entire admissible twist family.

---

# 5. Bridge Results

If A, B, and C are all formalized, then for a fixed $p$:

$$
\boxed{
\mathrm{FW}(E,p)
\Longrightarrow
\mathrm{FW}(E_d,p)
}
$$

holds for all Banwait admissible twists satisfying the corresponding splitting conditions.

This is extremely important:

> We do not need to rerun the residual representation theorem for infinitely many $d$.

We only need to establish for the base curve:

```text
FW certificate at p
```

---

# 6. Unresolved Issues

Even if the quantifier for $d$ is eliminated, there remains:

$$
\forall p>2.
$$

Therefore, this bridge only resolves the:

$$
\forall d
$$

part, and does not resolve the universal prime quantifier.