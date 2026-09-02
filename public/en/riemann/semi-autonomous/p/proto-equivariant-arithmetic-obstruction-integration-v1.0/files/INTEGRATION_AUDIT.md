# Consolidated Audit of RH Equivariant Arithmetic Obstruction

**Version:** v1.0  
**Date:** 2026-07-24  
**Audit Scope:** Six theoretical manuscripts, six engineering/certificate ZIPs  
**Summary:** Sources are complete and reproducible; the highest evidence level is the verified numerical certificate `E3` for a single intersection function; RH remains open.

## 1. Checks Completed in This Audit

- SHA-256 source fingerprints completed for all twelve attachments;
- All six ZIPs passed archive integrity tests;
- A total of $159$ files inventoried after unpacking;
- No network calls, subprocess executions, dynamic `eval`/`exec`, or deletion operations found in the Python source code;
- All $15$ tests passed across the five packages with test suites;
- `RH_Validated_Intersection_Certificate_v0.2` certificate successfully recomputed;
- Original SHA-256 manifests for v0.2 and the axis suppression package fully match;
- Axis suppression candidates and zero-side leakage reports both recomputed consistently.

## 2. Claim Grading

| Claim | Evidence | Level | Audit Conclusion |
|---|---|---:|---|
| Equivalence of centering, group action, and positive obstruction to RH | Manuscript proof / Standard complex analysis | `E1` | Usable as a decision framework |
| Equivalence of zero winding number for all regular rational rectangles to RH | Manuscript proof / Argument principle | `E1` | Usable as a countable decision family |
| Existence of a locally uniformly negative Paley–Wiener function for a fixed rectangle | Manuscript construction | `E1` | Pending external review and formalization |
| Floating-point separation—existence of positive intersection | Executable prototype | `E2` | Numerically reproducible |
| Continuous regional negative values and arithmetic positive interval for a single explicit function | Verified numerical certificate | `E3` | Highest level in this batch |
| General positive semi-definiteness of the arithmetic matrix | None | — | Unproven |
| Complete zero-side is negative | Leakage budget reverse-vetoes existing functions | — | Not achieved |
| RH | None | — | Unproven |

## 3. Exact Status of the v0.2 Certificate

Reproduced:

$$
\sup_{w\in[8,8.5]+i[-0.2,-0.1]}
2\operatorname{Re}(G(w)^2)
\le
-2.2416560599\times10^{-6},
$$

and:

$$
Q_{\mathrm{arith}}
\in
[0.033762674558557,\ 0.061347696341296].
$$

This proves that a single explicit function falls within the intersection of two strict inequalities.

It does not prove:

$$
M_{\mathrm{arith}}\succeq0,
$$

Nor does it prove that the target rectangle contains a ζ zero. The rectangle is a synthetic test region; the attachments do not provide its winding number certificate.

## 4. Definitive Failure Signals

The target negative margin of the existing function is:

$$
2.2416560599\times10^{-6}.
$$

The numerical mass of the first known critical line zero is:

$$
0.005352157501758449,
$$

Approximately $2387.591$ times larger.

The cumulative mass of the first $50$ known on-axis zeros is approximately $10583.150$ times larger. The existing tail prototype upper bound is even larger. Therefore, "single target negative value + arithmetic positive scalar" does not automatically form an explicit formula contradiction.

## 5. Structural Cost of Axis Suppression

As the finite elimination number increases from $q=0$ to $q=15$, the arithmetic positive directions in the supply basis drop from $12$ to $0$. At $q=12$, it is still possible to simultaneously maintain the target negative value and the arithmetic positive value, but the maximum value of the full control window is positive.

The currently observed research tension is:

$$
\text{Suppressing more on-axis mass}
\Longrightarrow
\text{Fewer available arithmetic positive directions}.
$$

This is a trade-off that must be directly quantified in the next version, rather than temporarily masked by increasing the basis dimension.

## 6. Semantic Boundaries That Must Be Maintained

Permitted to use:

- "Verified numerical intersection certificate";
- "Arithmetic scalar positive interval for a single function";
- "Synthetic target rectangle";
- "Global leakage not yet closed";
- "Finite axis elimination and arithmetic positive dimensional collapse".

Prohibited from escalating to:

- "PSD proven";
- "Off-axis zeros have been excluded";
- "Complete Weil positivity proven";
- "RH is nearing completion";
- "Finite grid or finite zero prefix represents the global domain".

## 7. Final Audit Verdict

This batch of research is not a proof of RH, but it has successfully reduced a vague problem into a measurable core:

$$
\boxed{
\text{Is it possible to make the global dominating margin strictly positive under arithmetic positivity constraints?}
}
$$

If the next round still only improves the local target negative value without improving the strict global dominating margin, it should be recorded as an engineering improvement and should not be marked as a major GAP advancement.