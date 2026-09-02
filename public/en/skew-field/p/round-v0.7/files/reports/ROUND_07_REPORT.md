# Centrally Generated Kakeya-Moser Bridging Family: Round 7

## —Third Non-Convex Alternating Cycle, Spatial Exposure Entropy, and Fourier-16 Residual Attack

**Version:** v0.7  
**Date:** July 28, 2026  
**Status:** Finite Fourier curvature family, finite congruence search, and non-convex container coordinate descent candidate

---

# 1. Third Alternating Cycle

Completed in this round:

\[
C_6
\longrightarrow
\gamma_7
\longrightarrow
C_7.
\]

The formal attack is the Fourier-14 residual candidate saved from Round 6.

---

# 2. Attack Validity

Curvature box:

\[
\max\kappa
\in
[
21.737588058490,
21.798886996249
].
\]

Thus:

\[
\frac1{\max\kappa}
\ge
0.045873901735
>
0.04.
\]

The centerline is simple, the tubular buffer is valid, and the tubular area replay error is:

\[
-1.068639737117e-07.
\]

---

# 3. Formal Attack Volume

After optimal congruence placement:

\[
\boxed{
e_7
=
0.006847625978.
}
\]

Accounting for approximately the following percentage of the complete single tubular area:

\[
8.0535%.
\]

The exposed set is divided into four connected components, with the largest component accounting for only:

\[
36.9234%.
\]

This is the first signal of the multi-lobe dispersed attack in this round.

---

# 4. Container Response

Round 6 area:

\[
A_6
=
0.198726522197.
\]

Directly adding the attack curve:

\[
A_{\mathrm{naive}}
=
0.205574148175.
\]

After rearranging the ten families:

\[
\boxed{
A_7
=
0.204320360988.
}
\]

Original union area:

\[
0.204267918556.
\]

Hole area:

\[
0.000052442432.
\]

Net increment after hole filling:

\[
\boxed{
\Delta A_7
=
0.005593838791.
}
\]

Relative increase:

\[
2.8148%.
\]

Absorption rate:

\[
\eta_7
=
18.3098%.
\]

![Area Sequence](../figures/01_area_sequence.png)

![Attack vs Net Increment](../figures/02_attack_vs_net_increment.png)

![Absorption and Novelty](../figures/03_absorption_novelty.png)

---

# 5. Spatial Novelty

For the Round 7 attack:

- Positive deficit arc length ratio:
  \[
  55.3149%;
  \]
- Effective deficit box count:
  \[
  17.906819;
  \]
- Largest component proportion:
  \[
  36.9234%.
  \]

Compared to Round 6, its exposure is more widely distributed along the centerline and the container boundary.

However, its effective spectral modes decreased from the Round 6 value of approximately:

\[
6.130555
\]

down to:

\[
4.849191.
\]

Therefore:

\[
\boxed{
\text{More Fourier modes or higher-frequency energy does not equate to more dispersed non-convex exposure.}
}
\]

![Clearance Deficit Profiles](../figures/05_clearance_deficit_profiles.png)

![Spatial Dispersion](../figures/06_spatial_dispersion.png)

![Effective Spectral Modes](../figures/09_effective_spectral_modes.png)

---

# 6. Ten-Family Activity Ledger

Using a leave-one-out exposure area of \(10^{-3}\) as the numerical threshold, the active families are:

1. `constant`: 0.002277589439
2. `round3_double_harmonic`: 0.007756962510
3. `round4_fourier10`: 0.008983552993
4. `round6_holdout`: 0.004926380500
5. `round7_fourier14`: 0.003274473472

The Archimedean spiral has been completely absorbed by the other nine families.

The Round 7 attack still retains:

\[
0.003274473472
\]

of leave-one-out exposure; thus, it does not become immediately redundant upon inclusion.

![Final Container](../figures/07_final_container.png)

---

# 7. Fourier-16 Residual Attack

An independent Fourier-16 search yields:

\[
\boxed{
e_7^{\mathrm{res}}
=
0.007080929041.
}
\]

Accounting for the following percentage of the single tubular area:

\[
8.3279%.
\]

Its curvature box is:

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

The largest exposed component of this candidate accounts for:

\[
84.0244%,
\]

The effective deficit box count is only:

\[
5.996579.
\]

It is dominated by a deep and concentrated deficit, which differs from the dispersed multi-lobe attack of Round 7.

![Residual Challenger](../figures/08_residual_challenger.png)

---

# 8. Convergence Diagnostics

Area increments:

\[
\Delta A_5
<
\Delta A_6
<
\Delta A_7.
\]

Meanwhile, the Fourier-16 residual attack is slightly higher than the formal attack of this round.

Therefore:

\[
\boxed{
\text{There is currently no evidence of area increment convergence, curvature dimension closure, or adversarial equilibrium.}
}
\]

---

# 9. Theoretical Feedback

This round demonstrates that the difficulty of non-convex universal containers lies in at least three distinct axes:

1. **Total exposure volume**
   \[
   e_n;
   \]

2. **Spatial distribution of exposure**
   — dispersed lobes or localized deep deficits;

3. **Container absorption rate**
   \[
   \eta_n.
   \]

Attacks of the same magnitude can elicit completely different container responses due to differing spatial distributions.

Therefore, subsequent adversarial searches must not solely maximize the exposed area, but should also incorporate exposure distribution patterns into multi-objective or holdout set designs.

---

# 10. Honesty Bounds

This round does not prove:

1. Fourier-14 is the global strongest attack for Round 7;
2. The ten-family non-convex container is the global minimum;
3. The Fourier-16 residual candidate is optimal over the complete function space;
4. The optimal congruence placement possesses a formal certificate;
5. The floating-point curvature box is a formal interval certificate;
6. This round establishes new bounds for the Kakeya or Moser problems.

---

# 11. The Next Natural Node

Round 8 can directly utilize the saved Fourier-16 localized-penetration candidate.

Simultaneously, the methodology should be upgraded to a bi-objective attack:

\[
\max_\gamma
\left[
\mathcal A_C(\gamma)
+
\lambda\,\mathcal D_C(\gamma)
\right],
\]

where \(\mathcal D_C\) can distinguish between:

- Dispersed-coverage types;
- Localized-penetration types.

Furthermore, two holdout pools should be established to prevent the container from overfitting to a single exposure pattern.

---

# 12. Conclusion

The final simply connected area for Round 7 is:

\[
\boxed{
A_7
=
0.204320360988.
}
\]

However, the more important conclusion is:

\[
\boxed{
\text{Spectral novelty, spatial exposure novelty, and container area novelty are three distinct quantities.}
}
\]

This advances the bridging family research from a singular max-min area problem to a geometric adversarial system featuring multiple attack modes.