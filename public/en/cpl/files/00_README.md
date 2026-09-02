# Critical-Line Proportion Ladder (CPL) — Claude 67.25% Research Pack

**Creation Date:** 2026-08-11  
**Research Status:** Batch 01 / Literature + Proof Reconstruction  
**Main Problem:** Starting from Claude's unconditional $67.25\%$ result on 2026-08-10, investigate the reachability conditions for $70\%/80\%/90\%/99\%$.

## 0. Semantic Clarification

The percentages in this project are **not the completion rate of the Riemann Hypothesis**.

Definition:

$$
P_q:\quad
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}\ge q,
$$

where $N_0^s(T,2T)$ is the number of zeros in $T<\gamma\le2T$ that are **simple and lie on $\Re(s)=1/2$**, and $N(T,2T)$ is counted with multiplicity.

Even if we achieve:

$$
P_1,
$$

it only implies density-one simple critical zeros, which is still not equivalent to the pointwise universal proposition of RH.

---

## 1. Contents of this Pack

### Main Paper

- `00_Claude_More_Than_Two_Thirds_Riemann_Zeta_2026-08-10.pdf`
  - Claude, *More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie on the Critical Line* (2026-08-10).

### Direct Prerequisites / Comparative Literature

- `01_BGSTB24_Unconditional_Montgomery_Theorem.pdf`
- `02_BGSTB25_Pair_Correlation_Proportions.pdf`
- `03_GLSS25_PCC_Simple_Critical_Zeros.pdf`
- `04_GS25_Zeta_Zeros_on_Critical_Line.pdf`
- `05_GS26_Zeta_Zeros_Narrow_Vertical_Box.pdf`
- `06_CGdL20_Pair_Correlation_SDP.pdf`
- `07_CCLM17_Hilbert_Spaces_Pair_Correlation.pdf`

### Research Notes

- `notes/01_Proof_Graph_Claude_67_25.md`
- `notes/02_CPL_Targets_70_80_90_99.md`
- `notes/03_Ceiling_Scope_67_25_vs_68_185.md`
- `notes/00_constant_check.txt`

### Scripts

- `scripts/reproduce_constants.py`

It only recalculates the constants in the paper that can be directly obtained from closed-form formulas, and does not claim to reproduce the entire proof.

---

## 2. Key Structures Confirmed in the First Round

Claude's core proof can be compressed into:

$$
\boxed{
\text{Weil explicit formula}
\to
\text{finite Gabor compression}
\to
\text{zero-side inertia}
\to
\text{prime-side traces}
\to
\text{rank--trace certificate}
}
$$

Baseline flat-window certificate:

$$
H(\lambda)=2-\frac1\lambda-\frac\lambda3,
$$

At $\lambda=1$:

$$
H(1)=\frac23.
$$

After optimizing the window:

$$
c_1^*=0.753296\ldots,
$$

$$
2-\frac1{c_1^*}=0.672500\ldots.
$$

---

## 3. Two Types of "Ceilings" Must Not Be Confused

### A. $67.25\%$

This is the extremum achieved by the Montgomery–Taylor extremal kernel within the framework of "block structure + two traces + primes up to $T$" and only modifying the window, as presented in §7.1 of the paper; the paper states that no window does better.

### B. $68.185\%$

Remark 1.1 of the paper claims that the upper bound for a broader bandwidth-one, configuration-by-configuration certificate class is approximately:

$$
0.68185.
$$

Therefore, $68.185\%$ cannot be treated as "guaranteed to be reachable just by further optimizing the window". Currently, the main text of the paper provides this extremal-law conclusion, but this Batch has not yet found a complete derivation sufficient to independently reconstruct this $0.68185$ constant; this item is marked as **OPEN-RECONSTRUCTION-01**.

---

## 4. Known Target Ladder

The rough Fourier-support requirements given by the main paper for the "same route":

$$
P_{70}:\ \sigma\approx1.04,
$$

$$
P_{80}:\ \sigma\approx1.26,
$$

$$
P_{90}:\ \sigma\approx1.70.
$$

For $P_{99}$, the paper **does not** provide a finite support threshold, so this project forbids linear extrapolation from the first three points.

Another conditional higher-moment route: if $HL^*(4,\lambda)$ holds for all $\lambda<1$, the paper obtains:

$$
P\ge\frac{13}{18}=0.722222\ldots.
$$

If corresponding moments of arbitrarily high order can be obtained, this mechanism can achieve density $1$, but it is still not equivalent to RH.

---

## 5. Next Batch of Priority Research

1. **P0**: Independently reprove the Lemma 3.2 rank--trace inequality.
2. **P1**: Reconstruct the $(1,1)$ signature and pull-back inertia of the off-line pair.
3. **P2**: Reconstruct the prime-side first/second trace normalisation.
4. **P3**: Independently derive $H(\lambda)$ and $2/3$.
5. **P4**: Independently solve the §7.1 extremal problem to re-obtain $c_1^*$ and $67.25\%$.
6. **P5**: Investigate/reconstruct the $0.68185$ extremal law from Remark 1.1.
7. **P6**: Establish a numerical/analytical research plane for $q(\sigma,k)$, separating support expansion and moment expansion.

---

## 6. Lean Companion

Anthropic official companion repo:

`https://github.com/anthropics/zeta-23-lean`

It can be cloned directly locally later to cross-reference Theorems A–E of the paper with `AUDIT.md`. This pack currently focuses on the paper PDF and research reconstruction, and has not mirrored the complete repo.