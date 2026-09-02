# 02 | Paper Pseudocode and Current Official Code Audit

## 0. Conclusion

The current GitHub implementation is not simply a direct copy of the paper's pseudocode.

It has incorporated several important corrections to the certificate strength, in particular:

$$
\boxed{
\operatorname{BSD}(E,2)\text{ anti-overclaiming gate}.
}
$$

---

# 1. What Exactly Can $2$-descent Prove?

What 2-descent directly controls is:

$$
\dim_{\mathbb F_2}\Sha(E)[2],
$$

rather than the general:

$$
\operatorname{ord}_2\#\Sha(E).
$$

Because even if:

$$
\dim_{\mathbb F_2}\Sha[2]=2,
$$

we could still have:

$$
\Sha[2^\infty]\cong(\mathbb Z/4\mathbb Z)^2,
$$

in which case:

$$
\operatorname{ord}_2\#\Sha=4.
$$

Therefore, the current official `check_BSD_at_2` adopts:

```text
sha_an_ord_2 != 0
→ reject / False
```

Only when:

$$
\operatorname{ord}_2\#\Sha_{\mathrm{an}}=0
$$

and the descent strictly yields:

$$
\Sha[2]=0
$$

do we accept:

$$
\operatorname{BSD}(E,2).
$$

This is consistent with the warning in Remark 2.19 of the paper:

> A positive analytic 2-adic valuation requires a higher $2$-power descent.

---

# 2. The Conditions for $E'$ Are Also Hardened

The CLZ20 branch requires:

$$
\Sha(E')[2]=0.
$$

Although the current program reads:

$$
\Sha_{\mathrm{an}}(E'),
$$

it only treats it as an input to the descent gate.

The condition actually accepted is:

$$
\operatorname{ord}_2\Sha_{\mathrm{an}}(E')=0
$$

and the 2-descent pins down:

$$
\dim\Sha(E')[2]=0.
$$

Thus, the analytic value is not directly substituted for the actual group order.

---

# 3. Descent Backend

The current program sequentially attempts:

1. PARI 2-descent;
2. mwrank;
3. Sage native 2-isogeny descent.

Because mwrank might get stuck, it is placed in a forked process and set with a wall-clock timeout.

This is not mathematical content, but it is extremely important for large-scale reproducibility.

---

# 4. Deterministic Criterion for $\mathcal S\ne\varnothing$

Proposition 2.16 of the paper gives an algebraic criterion.

The current program uses a deterministic filter by default, rather than just searching for witnesses up to:

$$
q\le10000
$$

.

The bounded prime search is still kept for cross-validation/testing, but it is no longer the primary certificate.

---

# 5. Soundness-Sensitive Flags

The current program explicitly marks the following options as testing only:

```text
skip_filter_S
skip_BSD_at_2_check
```

The output after enabling them can no longer be called fully theorem-qualified curves.

The local Agent must write these flags into the metadata and cannot just save the list of results.

---

# 6. Paper / Repository Format Drift

The paper text and the current output format of the repository have slightly evolved; for example, the twist output is currently in JSON.

This does not affect the theorem, but reproduction work must lock down:

```text
paper version
repository commit / file SHA
Sage version
LMFDB release
runtime flags
```

---

# 7. A Point That Still Requires a Phase 1 v0.2 Audit

The condition for Theorem 2.18 is:

$$
\text{analytic rank}=0.
$$

The initial dataframe in the Algorithm 1 code uses the LMFDB `rank` field, and then practically rules out central vanishing via the non-zero special value and the $L^{alg}$ condition.

During a full reproduction, one should still explicitly save:

```text
algebraic rank field
analytic rank field
special value nonvanishing
proof/evidence type
```

to avoid silently conflating the two types of rank into the same column.