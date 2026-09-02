# RH-W-07: Certificate Architecture and GAP Updates

**Version:** v0.1  
**Date:** 2026-07-23

---

# 1. Four-Layer Trust Architecture

This iteration divides the multi-prime computation into four layers:

## L0: Exploration Layer

Allowed to use:

- NumPy eigenvalues;
- Floating-point parameter scanning;
- AI-generated bases and witnesses;
- Fast inertia of midpoint matrices.

This layer can only output:

```text
NUMERICAL_CANDIDATE
```

## L1: Interval Generation Layer

`build_multiprime_chamber.py` is responsible for:

- Strictly enumerating non-zero von Mangoldt indices;
- Proving that $n\ge8$ cannot have an effect;
- Interval evaluation of $f_{ij}(\pm\log n)$;
- Computing endpoints, constants, Archimedean, and prime-power blocks;
- Outputting rational interval JSON.

## L2: Small Exact Verifier

`verify_multiprime_certificate.py` only uses:

```python
int
fractions.Fraction
```

It verifies:

1. The activation graph;
2. Fixed rational centers and row-radii;
3. The exact $LDL^T$ of $C-\delta I$;
4. $\delta-\epsilon>0$;
5. Four strict sign-flip witnesses.

## L3: Formalization Layer

Not yet complete. In the future, the following will be ported to Lean or Coq:

- B-spline supports;
- von Mangoldt sieving;
- Rational interval arithmetic;
- $LDL^T$ positive definiteness.

---

# 2. Why a Fixed Rational Grid is Important

The natural midpoints of high-precision intervals can have extremely large denominators. Performing an exact $LDL^T$ directly would cause verification costs to spiral out of control due to fraction bloat.

This iteration instead selects:

$$
C_{ij}\in10^{-20}\mathbb Z,
$$

and reincorporates the center quantization error into the interval radius $E=M-C$.

Therefore:

$$
\text{Analytical Precision}
$$

and:

$$
\text{Verifier Denominator Complexity}
$$

are formally separated.

This action does not sacrifice rigor; it only slightly expands the error budget.

---

# 3. Certificate Contents

Main certificate:

```text
multiprime_9x9_interval.json
```

Contains:

- Nine bases and support parameters;
- A complete explicit formula audit for each lag;
- The prime-power blocks for $2,3,4,5,7$;
- A $9\times9$ rational interval matrix;
- The positive definite margin of the rational center matrix;
- An exploration summary of cumulative ablation;
- Four exact witness sign flips;
- An explicit non-RH claim contract.

Verification results:

```text
schema=OK
activation_graph=OK
dimension=9
delta=1/2000
ldlt_pivots_positive=9
strict_sign_flips=4
status=CERTIFIED_POSITIVE_ON_THIS_9D_SUBSPACE
RH_CLAIM=False
```

---

# 4. GAP Status

| GAP | Status |
|---|---|
| von Mangoldt prime-power sieving | `CLOSED_FOR_N_LE_7` |
| Shifted support-window determination | `CLOSED_FOR_CURRENT_SPLINES` |
| Activation graph for nine lags | `CLOSED` |
| True multi-prime $9\times9$ interval matrix | `CLOSED` |
| Exact 9D positive definite certificate | `CLOSED` |
| Four cumulative sign-flip witnesses | `CLOSED_FOR_FIXED_WITNESSES` |
| Universal compiler for arbitrary rational bases | `PARTIAL_FIXED_FAMILY` |
| Unbounded prime-power tails | `OPEN_ENGINEERING` |
| Automated parameter/chamber search | `OPEN_ENGINEERING` |
| True negative witnesses | `NOT_FOUND` |
| Formalized backend | `OPEN` |

---

# 5. Statements Not Proven in This Iteration

Must not output:

$$
\text{"Adding each prime makes the Weil form more positive"}.
$$

This iteration only proves sign flips in four specified directions.

Must not output:

$$
\text{"The 9D matrix being positive definite supports RH and is thus close to a proof"}.
$$

Finite-dimensional positive definiteness is one of the expected phenomena and lacks global sufficiency.

Do not refer to the artificial ablation matrix as a new form of zeta. The true matrix of the fixed explicit formula in this iteration is only formed when all valid prime-power blocks are present simultaneously.

---

# 6. Acceptance Criteria for the Next Iteration

`RH-W-08` must at least feature:

1. Parameterized inputs: degree, $h$, shifts, maximum support;
2. A fast but untrusted chamber searcher;
3. Conversion of the candidate matrix's minimum eigenvector into a rational witness;
4. Rigorous reconstruction of the selected candidate;
5. If the certificate fails, distinguish between:
   - Truly close to zero;
   - Archimedean tail being too wide;
   - Center quantization being too coarse;
   - Basis condition number being too poor;
   - Incomplete prime-power enumeration;
6. Prohibition of inferring RH from a positive finite matrix.