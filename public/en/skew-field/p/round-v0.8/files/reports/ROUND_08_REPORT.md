# Centrally Generated Kakeya-Moser Bridging Family: Round 8

## ——Fourth Non-Convex Alternating Cycle, Fourier-18 Dual Pool, and Spectral Parent-Spatial Phenotype Decoupling

**Version:** v0.8  
**Date:** July 28, 2026  
**Status:** Finite Fourier/B-spline curvature families, finite congruence search, and non-convex container coordinate descent candidates

---

# 1. Fourth Alternating Cycle

Completed in this round:

\[
C_7
\longrightarrow
\gamma_8
\longrightarrow
C_8.
\]

The formal attack is the Fourier-16 local-penetration candidate saved from Round 7.

---

# 2. Formal Attack

Optimal exposed area:

\[
\boxed{
e_8
=
0.007080929041.
}
\]

Proportion of the full tubular area of the monomer:

\[
8.3279%.
\]

Curvature box:

\[
\max\kappa
\in
[
21.426569439939,
21.502612021114
],
\]

Thus:

\[
\frac1{\max\kappa}
\ge
0.046505977926
>
0.04.
\]

---

# 3. Container Response

Round 7:

\[
A_7
=
0.204320360988.
\]

Naive inclusion:

\[
A_{\mathrm{naive}}
=
0.211400720567.
\]

After reconfiguring the eleven families:

\[
\boxed{
A_8
=
0.208938653536.
}
\]

The container has no remaining holes.

Recovered:

\[
0.002462067031.
\]

Absorption rate:

\[
\eta_8
=
34.7704%.
\]

Net increment:

\[
\Delta A_8
=
0.004618292548,
\]

Relative increase:

\[
2.2603%.
\]

![Area Sequence](../../../../skew-field/p/round-v0.8/files/figures/01_area_sequence.png)

![Attack vs Net Increment](../../../../skew-field/p/round-v0.8/files/figures/02_attack_vs_net_increment.png)

![Absorption and Novelty](../../../../skew-field/p/round-v0.8/files/figures/03_absorption_novelty.png)

---

# 4. Increment Sequence

\[
\begin{aligned}
\Delta A_5&=0.002818179861,\\
\Delta A_6&=0.004464130667,\\
\Delta A_7&=0.005593838791,\\
\Delta A_8&=0.004618292548.
\end{aligned}
\]

The Round 8 increment is lower than that of Round 7, but still higher than Rounds 5 and 6.

Therefore, this is merely the first pullback and does not constitute a convergence trend.

---

# 5. Active Families

Using a leave-one-out exposure threshold of \(10^{-3}\):

1. `round3_double_harmonic`: 0.007320161834
2. `round4_fourier10`: 0.008606249632
3. `round6_holdout`: 0.002061809501
4. `round7_fourier14`: 0.005407020379
5. `round8_fourier16`: 0.002823706215

The Round 8 Fourier-16 attack still leaves:

\[
0.002823706215
\]

of leave-one-out exposure; thus, it does not become immediately redundant upon inclusion.

The Archimedean family only retains exposure at the level of numerical noise.

![Final Container](../../../../skew-field/p/round-v0.8/files/figures/06_final_container.png)

![Active Ledger](../../../../skew-field/p/round-v0.8/files/figures/08_leave_one_out.png)

---

# 6. Dual Pool and Non-Fourier Holdout Set

Optimal value for the Fourier-18 dispersed parent:

\[
0.004050690308.
\]

Optimal value for the Fourier-18 local parent:

\[
0.003625184186.
\]

Optimal refined value for the B-spline holdout pool:

\[
0.000021419854.
\]

Thus, both Fourier parents can still generate positive-exposure candidates, whereas this batch of smooth B-spline perturbations is nearly completely absorbed.

![Dual Pool Audit](../../../../skew-field/p/round-v0.8/files/figures/07_dual_pool_audit.png)

---

# 7. Round 9 Seed

Strongest Fourier-18 candidate exposure:

\[
\boxed{
e_8^{\mathrm{res}}
=
0.004050717099.
}
\]

Proportion of the monomer's tubular area:

\[
4.7641%.
\]

Curvature box:

\[
\max\kappa
\in
[
20.321848458779,
20.387027508692
],
\]

Therefore:

\[
\frac1{\max\kappa}
\ge
0.049050799562
>
0.04.
\]

Its spatial phenotype:

- Five exposed components;
- Maximum component:
  \[
  60.2183%;
  \]
- Effective deficit boxes:
  \[
  10.170047;
  \]
- Positive deficit arc length ratio:
  \[
  36.4527%.
  \]

It is a hybrid attack and has been saved as the initial seed for Round 9.

![Clearance Deficits](../../../../skew-field/p/round-v0.8/files/figures/05_clearance_deficits.png)

![Residual Challenger](../../../../skew-field/p/round-v0.8/files/figures/09_residual_challenger.png)

---

# 8. New Theoretical Judgments

This round simultaneously refutes three overly simplistic judgments:

\[
\text{Local parents inevitably produce local phenotypes};
\]

\[
\text{Dispersed parents inevitably produce dispersed phenotypes};
\]

\[
\text{Local-penetration types are inevitably harder to absorb than dispersed types}.
\]

A more reasonable relationship is:

\[
\boxed{
\text{Spatial exposure phenotype}
=
\mathcal P
(
\text{Curvature spectrum},
\text{Spectral phase},
\text{Congruence configuration},
\text{Container geometry}
).
}
\]

The absorption rate is:

\[
\boxed{
\eta
=
\mathcal R
(
\text{Attack phenotype},
\text{Current container state}
).
}
\]

Neither of these is a standalone scalar property of the curve.

---

# 9. Convergence Diagnostics

Although the area increment decreased in Round 8, the Round 9 seed still leaves:

\[
0.004050717099
>0.
\]

Furthermore, neither the dispersed nor the local Fourier parents are closed.

Therefore:

\[
\boxed{
\text{There is currently no evidence of function space closure, attack closure, or non-convex container equilibrium.}
}
\]

---

# 10. Honest Bounds

This round does not prove:

1. Fourier-16 is the globally strongest attack for Round 8;
2. The eleven-family non-convex container is the global minimum;
3. The Fourier-18 seed is optimal over the complete curvature space;
4. The B-spline pool represents all non-Fourier curvature families;
5. The congruence placements possess formal certificates;
6. The floating-point curvature boxes are formal interval certificates;
7. This round establishes a new area bound for the Kakeya or Moser problems.

---

# 11. Next Natural Node

Round 9 can directly utilize the saved Fourier-18 hybrid candidate.

Methodologically, we should:

1. Retain the three phenotype pools: dispersed, local, and hybrid;
2. Establish Wasserstein or distributional distances for the area distribution of exposed components;
3. Perform multi-pool min-max optimization using the worst-case values of different phenotypes:
   \[
   \max_{\gamma\in\mathcal P_j}
   \mathcal A_C(\gamma);
   \]
4. Avoid overfitting to a single phenotype during the container response;
5. Introduce non-Fourier local B-spline knot movements, rather than solely perturbing fixed control point values;
6. Track whether the residual exposures of all three pools decrease simultaneously.

---

# 12. Conclusion

Round 8 final area:

\[
\boxed{
A_8
=
0.208938653536.
}
\]

Its core advancement is not a single number, but rather:

\[
\boxed{
\text{Spectral parents, spatial exposure phenotypes, and container absorption rates must be accounted for separately.}
}
\]

Non-convex universal containers can no longer be described merely by "which curve is harder," but require the study of:

\[
\boxed{
\text{The dynamic equilibrium between multiple attack phenotype pools and the container response.}
}
\]