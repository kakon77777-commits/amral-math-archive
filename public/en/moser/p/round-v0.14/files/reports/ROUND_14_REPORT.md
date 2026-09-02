# Moser Skewness Field Semi-Autonomous Research: Round 14

## ——Bimodal Curvature Splitting, Chiral Symmetry Breaking, and Unimodal Local Stability

**Date:** July 26, 2026  
**Status:** Curvature distribution exploration; finite search; non-full function space proof  
**Continuation of:** Moser Skew Lab v0.13

Baseline:

$$
s_{13}=0.998914343297485.
$$

---

# 1. Research Problem

Round 13 only allowed a single tanh curvature layer. This round introduces:

1. Splitting of the same flank into two curvature peaks;
2. Antisymmetric shifts in the curvature centers or widths of the left and right flanks.

The goal is to determine whether the unimodal mirror-symmetric candidate is merely a false isolated point caused by restricted parameterization.

---

# 2. Bimodal Curvature Density

$$
\rho(u)
=
(1-a)\rho_1(u;c_1,\varepsilon_1)
+
a\rho_2(u;c_2,\varepsilon_2),
$$

where:

$$
\rho_i(u)
\propto
\operatorname{sech}^2
\left(
\frac{u-c_i}{\varepsilon_i}
\right).
$$

The unimodal model is contained within:

$$
c_1=c_2,
\qquad
\varepsilon_1=\varepsilon_2.
$$

---

# 3. Bimodal Search Results

The optimal eight-parameter mixture yields:

$$
|c_2-c_1|
\approx
3.325511791719e-06.
$$

The two widths are:

$$
\varepsilon_1=0.037064233544,
$$

$$
\varepsilon_2=0.036584022364.
$$

The weight of the second component is:

$$
a=0.505765188602.
$$

The optimal solution does not form two distinguishable peaks, but instead collapses back into a near-unimodal shape.

Under the same high-resolution evaluator:

$$
s_{\mathrm{double}}-s_{\mathrm{single}}
=
-6.549770725783e-10.
$$

---

# 4. Peak Separation Direction

| Peak distance $d$ | Scale | Relative to $d=0$ |
|---:|---:|---:|
| 0.0000 | 0.998914341156203 | 0.000e+00 |
| 0.0020 | 0.998914205767712 | -1.354e-07 |
| 0.0040 | 0.998913798823585 | -5.423e-07 |
| 0.0060 | 0.998913115592216 | -1.226e-06 |
| 0.0080 | 0.998912149175696 | -2.192e-06 |
| 0.0100 | 0.998910890891321 | -3.450e-06 |
| 0.0240 | 0.998892167429063 | -2.217e-05 |
| 0.0400 | 0.998842447005232 | -7.189e-05 |
| 0.0560 | 0.998771954422084 | -1.424e-04 |
| 0.0720 | 0.998685929509345 | -2.284e-04 |

Small separation fitting:

$$
\Delta s(d)
\approx
-0.033794468d^2+O(d^4).
$$

The quadratic coefficient is negative.

For example, at $d=0.01$, the scale decreases by approximately:

$$
3.45\times10^{-6}.
$$

---

# 5. Correct Chiral Coordinates

The two local centers of the mirror-symmetric baseline are:

$$
c_L=c,
\qquad
c_R=1-c.
$$

Center chiral mode:

$$
c_L=c+\eta_c,
$$

$$
c_R=1-c+\eta_c.
$$

Width chiral mode:

$$
\varepsilon_L=\varepsilon e^{\eta_\varepsilon},
$$

$$
\varepsilon_R=\varepsilon e^{-\eta_\varepsilon}.
$$

The congruence objective is:

$$
s_{\mathrm{cong}}
=
\min(s_+,s_-).
$$

---

# 6. Center Shift

| $\eta_c$ | Original chirality | Mirror chirality | Congruence scale |
|---:|---:|---:|---:|
| -0.0300 | 0.998386461741 | 0.998038458209 | 0.998038458209 |
| -0.0200 | 0.998562356573 | 0.998342625752 | 0.998342625752 |
| -0.0100 | 0.998738317094 | 0.998638703661 | 0.998638703661 |
| 0.0000 | 0.998914319065 | 0.998914319065 | 0.998914319065 |
| 0.0100 | 0.998638703661 | 0.998738317094 | 0.998638703661 |
| 0.0200 | 0.998342625752 | 0.998562356573 | 0.998342625752 |
| 0.0300 | 0.998038458209 | 0.998386461741 | 0.998038458209 |

Highest tested point:

$$
\boxed{\eta_c=0}.
$$

Quadratic coefficient near zero:

$$
-3.674929940.
$$

---

# 7. Width Shift

| $\eta_\varepsilon$ | Original chirality | Mirror chirality | Congruence scale |
|---:|---:|---:|---:|
| -0.450 | 0.998917547301 | 0.998696999268 | 0.998696999268 |
| -0.300 | 0.998916078391 | 0.998783827179 | 0.998783827179 |
| -0.150 | 0.998915019154 | 0.998858563359 | 0.998858563359 |
| 0.000 | 0.998914319065 | 0.998914319065 | 0.998914319065 |
| 0.150 | 0.998858563359 | 0.998915019154 | 0.998858563359 |
| 0.300 | 0.998783827179 | 0.998916078391 | 0.998783827179 |
| 0.450 | 0.998696999269 | 0.998917547301 | 0.998696999269 |

Highest tested point:

$$
\boxed{\eta_\varepsilon=0}.
$$

Quadratic coefficient near zero:

$$
-0.003092904.
$$

---

# 8. Two-Dimensional Chiral Census

Within:

$$
\eta_c\in[-0.03,0.03],
$$

$$
\eta_\varepsilon\in[-0.45,0.45]
$$

sample $80$ two-dimensional shifts.

High-resolution zero shift:

$$
s_{\mathrm{zero}}
=
0.998914341156140.
$$

Best non-zero candidate:

$$
s_{\mathrm{nonzero}}
=
0.998886247847192.
$$

Under the same evaluator:

$$
s_{\mathrm{nonzero}}-s_{\mathrm{zero}}
=
-2.809330894860e-05.
$$

Therefore, chiral symmetry breaking provides no congruence improvement.

---

# 9. Coordinate Error Audit

The first version mistakenly set the right flank local center to $c$ again, instead of $1-c$.

This generated a non-mirror-symmetric baseline and caused:

- False improvements on coarse grids;
- Narrow weak phase branches;
- Contradictions between coarse and high resolutions.

This batch of numerical values has been completely excluded and did not enter this round's conclusions.

After correction, the zero-shift curve and its mirror scale are consistent to approximately $10^{-15}$.

---

# 10. Complete Phase Audit

Both the unimodal and near-degenerate bimodal candidates retain the original low-branch structure.

No new phase valleys lower than the original four control branches were generated due to peak splitting.

---

# 11. Research Verdict

Finite data supports:

$$
\boxed{
\text{The unimodal curvature layer is locally stable against peak splitting directions.}
}
$$

and:

$$
\boxed{
\text{Mirror symmetry is locally stable against the tested center and width chiral modes.}
}
$$

After adding degrees of freedom to the curvature distribution, the optimal solution still returns to the vicinity of the unimodal, zero-chiral shift.

---

# 12. What Cannot Be Inferred

This round cannot prove:

1. The unimodal shape is optimal for all curvature density functions;
2. All bimodal models are inferior;
3. All asymmetric curves are inferior;
4. Biarcs or general splines cannot surpass it;
5. The Hessian in the curvature function space is entirely negative definite.

---

# 13. Direction for Round 15

The next round will shift to local analysis in the curvature function space:

$$
\rho_a(u)
=
\frac{
\rho_0(u)\exp(\sum_k a_k\psi_k(u))
}{
\int_0^1\rho_0(v)\exp(\sum_k a_k\psi_k(v))\,dv
}.
$$

Priority modes:

- Translation;
- Broadening;
- Bimodal splitting;
- Skewness;
- Higher-order oscillations.

Estimate the constrained Hessian on the four-branch level manifold:

$$
H_{\mathrm{eff}}
=
P_T^\top\nabla^2s\,P_T.
$$

---

# 14. Conclusion

Optimal bimodal peak distance:

$$
|c_2-c_1|
\approx
3.325511791719e-06,
$$

i.e., re-collapsing into a unimodal shape.

Optimal center chirality:

$$
\eta_c^\ast=0.
$$

Optimal width chirality:

$$
\eta_\varepsilon^\ast=0.
$$

Therefore:

$$
\boxed{
\text{Within the tested families of curvature splitting and chiral symmetry breaking,
the unimodal mirror-symmetric candidate from Round 13 has no discernible ascending direction.}
}
$$