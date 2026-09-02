# 15 | Fresh Semantic Replay: Algorithm2 OLD → CURRENT

## 1. Source chronology

Three semantic nodes:

$$
G=\text{generator commit }7286794,
$$

$$
O=\text{OLD commit }1a0489,
$$

$$
C=\text{CURRENT commit }31fae2.
$$

The Algorithm2 theorem predicate added in `G -> O`:

$$
D(E,d)=\texttt{disc\_valuation\_condition}.
$$

`O -> C`:

1. Removed $D(E,d)$;
2. Tightened
   $$
   \gcd(d,N)=1
   $$
   to
   $$
   \gcd(d,3N)=1.
   $$

The remaining relevant admissibility predicates are unchanged.

---

## 2. Why is Sage not needed to reconstruct the OLD stable output?

The generator archived twist JSON is already the output of the generator Algorithm2 on the actual curves.

Therefore, the OLD source only needs to apply the following to the same generator-domain curves:

$$
D(E,d).
$$

v0.5 simultaneously provides for each curve:

- conductor primes;
- minimal discriminant;
- $v_q(\Delta_E)$.

Thus, $D(E,d)$ can be directly exact replayed without recalculating:

- $a_p$;
- 2-division field;
- Kronecker conditions;
- squarefreeness;

Because the generator output has already passed through these unchanged gates.

---

## 3. Fully materialized generator domain

Generator archived JSON:

$$
39{,}394\text{ curves},
$$

$$
293{,}482\text{ twist pairs}.
$$

Applying the OLD addition pair by pair:

$$
D(E,d)
$$

Yields:

$$
\boxed{
0\text{ failures}.
}
$$

Therefore, on all materialized generator outputs:

$$
\boxed{
T_O(E)=T_G(E).
}
$$

Note: This is a data-domain statement; it does not claim that $D$ is always redundant as an abstract theorem condition.

---

## 4. Two-gate partition of the stable 36,687 curves

Define on the generator twist pairs:

$$
D=1
$$

indicating it passes the OLD disc gate;

$$
G_3=1
$$

indicating it passes the CURRENT:

$$
\gcd(d,3N)=1.
$$

Exact four-cell partition:

| Cell | Count | Meaning |
|---|---:|---|
| $D=1,G_3=1$ | 247,391 | Common to OLD/CURRENT |
| $D=1,G_3=0$ | 21,306 | OLD-only; removed by the new gcd gate |
| $D=0,G_3=1$ | 0 | CURRENT-only; could have been added by deleting the disc gate |
| $D=0,G_3=0$ | 0 | Hidden region of two-gate interaction |

Therefore:

$$
|T_O|=268{,}697,
$$

$$
|T_C|=247{,}391.
$$

And:

$$
T_C
=
\{(E,d)\in T_O:\gcd(d,3N_E)=1\}.
$$

Curve-by-curve mismatch comparison:

$$
\boxed{0}.
$$

---

## 5. Semantic attribution

Therefore, the OLD→CURRENT delta in the stable domain can be **fully attributed to**:

$$
\boxed{
21{,}306\text{ removals}
=
\text{new factor-3 coprimality gate}.
}
$$

And:

$$
\boxed{
0\text{ additions}
=
\text{disc gate deletion produced no observable gain}.
}
$$

There is no mixed interaction.

---

## 6. Branch structure

### CLZ20

generator stable pairs:

$$
5{,}849.
$$

All:

$$
D=1,G_3=1.
$$

So:

$$
\Delta_{\rm CLZ}=0.
$$

This is compatible with the CLZ twist prime condition requirement:

$$
p\equiv1\pmod4
$$

$p=3$ could never be a twist prime to begin with.

### Zha16

generator stable pairs:

$$
262{,}848.
$$

Of which:

$$
241{,}542
$$

are retained,

$$
21{,}306
$$

are removed due to factor $3$.

Thus, the entire observable Algorithm2 semantic delta falls within the Zha16 branch.

---

## 7. Curve-level census

$$
31{,}250
$$

stable curves are completely unchanged.

$$
5{,}437
$$

have only removals.

$$
0
$$

have only additions.

$$
0
$$

are mixed.

Therefore:

$$
\boxed{
\text{The CURRENT semantic update in the stable domain is a pure monotonic reduction.}
}
$$

Previously, it was inferred from the source diff that there might be both shrink + expand directions; now the exact replay proves:

> The expand mechanism was not triggered in this actual data domain.

---

## 8. Epistemic boundary

There are also:

$$
1{,}355
$$

OLD base curves that were added to the OLD base file only after the generator twist JSON was generated.

They lack generator twist entries, so this replay cannot reconstruct their OLD-source output without re-executing the Algorithm2 common gates.

However, these 1,355 curves have all been excluded by the CURRENT Algorithm1 strict isogeny gate.

Therefore, for the **current theorem-qualified universe**:

$$
\boxed{
\text{The stable semantic replay is closed.}
}
$$

Supplementing those 1,355 curves only holds historical reconstruction value and is not a necessary dependency for current BSD research.

---

## 9. Stopping rule

This reproduction line has completed a three-layer closure from:

$$
\text{artifact diff}
\to
\text{exact census}
\to
\text{source semantic replay}
$$

If there are no new theorem discrepancies, continuing to do:

- Finer Git archaeology;
- Reconstruction of the 1,355 historical curves;
- More formatting replays;

should be labeled as:

`ENGINEERING / HISTORICAL ONLY`

rather than mathematical progress on BSD.

Therefore, it is recommended to cap the Phase 1 reproduction at v0.6.