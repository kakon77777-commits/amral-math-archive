# Moser Skewness Field Semi-Autonomous Research: Round 12

## —Independent `mpmath.iv` Replay, Interval Newton, and Arb Absence Bounds

**Date:** July 27, 2026  
**Status:** Partial independent interval replay; not an Arb certificate; informal proof

---

# 1. Environment Results

This environment lacks `python-flint`, Arb, or Sage; the package repository also has no installable `python-flint`.

Therefore, this round does not claim to have completed an Arb replay, but instead adopts:

$$
\boxed{\texttt{mpmath.iv}\text{ directed interval arithmetic}}
$$

as an independent fallback verification.

# 2. Special Competing Branches

$$
s_{270}\in[0.9989143389428913213797012975,0.9989143392263741131243407093].
$$

$$
\boxed{s_{120}-s_{270}\in[1.584622955726897820027e-9,1.692045182662177229601e-9]}.
$$

The lower bound remains strictly positive.

Smooth candidate relative to fixed event control:

$$
\boxed{s_{270}-s_{\mathrm{event},B1}\in[0.00001058181038264642457147,0.00001058209386543816921088]}.
$$

This also maintains a strictly positive lower bound.

# 3. Analytic Contact Boundaries

$19$ analytic phase boundaries were recomputed using interval balls:

$$
\boxed{19/19}
$$

All of them contain the floating-point values saved in Round 11.

# 4. Twelve Stationary Point Root Boxes

| Root | Signature | Type | $N(X)\subset\operatorname{int}X$ | Endpoint Sign Change | Scale Lower Bound Distance |
|---:|---|---|---:|---:|---:|
| 1 | `L|p0|p2` | smooth_minimum | True | True | 4.6581599e-8 |
| 2 | `L|p0|p2` | smooth_maximum | True | True | 8.1974837e-6 |
| 3 | `L|p0|p2` | smooth_minimum | True | True | 4.5455127e-8 |
| 4 | `p1|p0|p3` | smooth_maximum | True | True | 0.24896511 |
| 5 | `p2|L|p3` | smooth_minimum | True | True | 0.030437642 |
| 6 | `p2|p1|p3` | smooth_maximum | True | True | 0.035237883 |
| 7 | `p2|p1|p0` | smooth_maximum | True | True | 0.17278687 |
| 8 | `p3|p2|p0` | smooth_maximum | True | True | 0.18060899 |
| 9 | `p3|p2|L` | smooth_minimum | True | True | 0.12867719 |
| 10 | `p3|p2|p1` | smooth_maximum | True | True | 0.17020992 |
| 11 | `p0|p3|p1` | smooth_maximum | True | True | 0.089684617 |
| 12 | `p0|p3|p2` | smooth_maximum | True | True | 0.22111049 |

Results:

$$
\boxed{12/12}
$$

root boxes satisfy the interval Newton inclusion condition; the endpoint derivative signs also all conform to the minimum/maximum classification.

# 5. Boundary Box Replay

| Boundary | Formula | Direct IV Sign | Round 11 Global Safety | Status |
|---:|---|---:|---:|---|
| 1 | `\pi/2-\alpha` | False | True | dependency_inflation |
| 2 | `\pi/2-\beta` | False | True | dependency_inflation |
| 3 | `\beta-\pi/3` | False | True | dependency_inflation |
| 4 | `\alpha-\pi/3` | False | True | dependency_inflation |
| 5 | `\pi/2` | True | True | direct_pass |
| 6 | `\pi-\alpha` | False | True | dependency_inflation |
| 7 | `\pi-\beta` | False | True | dependency_inflation |
| 8 | `2\pi/3` | True | True | direct_pass |
| 9 | `\pi/2+\beta` | False | True | dependency_inflation |
| 10 | `\pi/2+\alpha` | False | True | dependency_inflation |
| 11 | `\pi` | True | True | direct_pass |
| 12 | `5\pi/3-\alpha` | False | True | dependency_inflation |
| 13 | `5\pi/3-\beta` | False | True | dependency_inflation |
| 14 | `\pi+\beta` | False | True | dependency_inflation |
| 15 | `\pi+\alpha` | False | True | dependency_inflation |
| 16 | `3\pi/2` | True | True | direct_pass |
| 17 | `5\pi/3` | True | True | direct_pass |

Boundaries whose left and right signs were directly determined by `mpmath.iv`:

$$
\boxed{5/17}.
$$

The remaining boundaries are concentrated where the `L/R` smooth support points are generated or vanish. The inverse formulas approach $\operatorname{atanh}(\pm1)$, and ordinary natural interval extension suffers from severe overestimation, so this library cannot reproduce the narrow boxes of Round 11.

This is **dependency inflation**, not the discovery of a counterexample. The analytic error bounds and scale exclusions from Round 11 are retained, but were not independently replayed by the fallback library in this round.

# 6. Incomplete Parts

The original plan was to replay the $579$ derivative leaf boxes from Round 11 one by one. Implementation showed that re-solving the inverse for the smooth support points for every box would exceed the execution limits of this environment.

Therefore, this round does not mark "unfinished" as "passed". The formal status is:

- Special differences: Passed;
- Smooth-event comparison: Passed;
- Analytic boundary balls: Passed;
- Twelve root boxes interval Newton: Passed;
- Boundary direct IV: Partially passed;
- $579$ leaf boxes independent replay: Incomplete;
- Arb replay: Incomplete.

# 7. Research Verdict

The most important low-value competition and all smooth stationary points were reproduced by another set of interval arithmetic.

Thus, it can currently be elevated to:

$$
\boxed{\text{Core candidates and stationary point structures are supported by independent IV replay.}}
$$

But it cannot be elevated to:

$$
\boxed{\text{Complete Arb full-phase machine certificate.}}
$$

# 8. Round 13 Direction

The complete phase framework is already sufficiently stable; the next round will shift to the smooth five-parameter event-KKT system:

$$
p=(w,\beta,\delta,c,\varepsilon).
$$

By equating the heights of the two low-phase smooth minima and the $120^\circ$ and $270^\circ$ cusps simultaneously, and then adding branch pressure stationarity, we will determine whether the current smooth candidate is a numerical isolated point within this family.

The actual Arb replay will be handed over by this round's script to an external environment equipped with `python-flint`.