# Center-Generated Kakeya-Moser Bridge Family: Round 5

## — Non-Convex Area Exposure Tension and the First Curve-Container Alternating Adversarial Cycle

**Version:** v0.5  
**Date:** July 27, 2026  
**Status:** Finite Fourier family, finite placement search, and non-convex container coordinate descent candidate

---

# 1. Research Pivot

The curve searches in the first 4 rounds primarily targeted the convex support gap.

Round 4 showed that the area of the seven-family simply connected non-convex container is only:

\[
0.191444211669,
\]

far lower than that of the convex container for the same families.

Therefore, Round 5 no longer asks:

> Which curve is the hardest to place into a given convex hull?

Instead, it asks:

> Which thickened curve leaves the maximum exposed area even when utilizing existing non-convex grooves, channels, and local complementary structures?

---

# 2. Area Exposure Tension

Definition:

\[
\mathcal A_C(\gamma)
=
\inf_{g\in E(2)}
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
\]

If:

\[
\mathcal A_C(\gamma)=0,
\]

then the complete tubular neighborhood of the curve can be placed into \(C\) under some congruent configuration.

This is the actual non-convex container tension utilized in Round 5.

---

# 3. Fourier-12 Attack Curve

The curvature still adopts the normalized logarithmic Fourier form:

\[
\kappa(s)
=
\frac{
\pi e^{g_{12}(s)}
}{
\int_0^1e^{g_{12}(u)}du
}.
\]

Semi-verified curvature box:

\[
\max\kappa
\in
[
19.278187626136,
19.342578149755
].
\]

Thus:

\[
\frac1{\max\kappa}
\ge
0.051699416296
>
0.04.
\]

The sampled minimum radial derivative ledger is positive, the centerline is simple, and the buffer is valid.

The optimal exposed area of the attack curve in the Round 4 container:

\[
\boxed{
\mathcal A_{C_4}(\gamma_5)
=
0.006664458451
}.
\]

Relative to the single tubular area:

\[
7.8381%.
\]

![Curve Comparison](../figures/01_curve_comparison.png)

![Curvature Profiles](../figures/02_curvature_profiles.png)

![Attack Configuration](../figures/03_attack_against_round4.png)

---

# 4. Multi-Branch Placement Audit

Multiple global search seeds converged to the same configuration on the optimal mirrored branch.

The low-resolution exposure value of the optimal mirrored branch is approximately:

\[
0.00665814.
\]

The highest-resolution local recomputation is:

\[
0.006664458451.
\]

The next orientation-preserving control branch is approximately:

\[
0.00685613.
\]

Other local branches are significantly higher.

This supports the current configuration as a strong numerical candidate, though it is not yet a global placement certificate.

---

# 5. Direct Addition and Defensive Response

Round 4 container:

\[
A_4
=
0.191444211669.
\]

Keeping the existing configurations fixed and directly adding the attack curve:

\[
A_{\mathrm{naive}}
=
0.198108843289.
\]

After family-by-family reconfiguration:

\[
\boxed{
A_5
=
0.194262391530.
}
\]

Container recovery:

\[
0.003846451759,
\]

representing the following percentage of the attack exposure:

\[
57.7159%.
\]

Final net increase:

\[
0.002818179861,
\]

Relative to Round 4:

\[
1.4721%.
\]

![Area Response](../figures/04_attack_response_area.png)

![Pressure Decomposition](../figures/07_recovery_decomposition.png)

---

# 6. Final Container

High-resolution replay yields:

\[
A_{\mathrm{raw}}
=
0.194082126470.
\]

The union contains a small hole with an area of:

\[
0.000180265060.
\]

Simply connected area after hole-filling:

\[
A_{\mathrm{sc}}
=
0.194262391530.
\]

The container is valid and connected.

![Final Container](../figures/05_final_container.png)

---

# 7. Active Skeleton

Using a leave-one-out exposed area of \(10^{-3}\) as the activity threshold, the current main active families are:

1. `constant`: 0.009712611659
2. `round3_double_harmonic`: 0.007655203324
3. `round4_fourier10`: 0.007965433132
4. `round5_fourier12`: 0.004067990482

See the machine-readable ledger and charts for the detailed exposure of each family.

![Activity Ledger](../figures/06_leave_one_out.png)

This indicates that the newly added curve in Round 5 does not merely replace the old skeleton, but becomes the fourth major source of non-convex activity.

---

# 8. Holdout Sample and Non-Convergence

After the container update was completed, a random 12-mode curve that did not participate in training was used as a holdout sample.

The best holdout candidate still has:

\[
\boxed{
\mathcal A_{C_5}(\gamma_{\mathrm{holdout}})
=
0.004934177792
>0.
}
\]

Its maximum curvature is approximately:

\[
15.540501909157.
\]

Therefore:

\[
\boxed{
\text{The Round 5 alternating system has not yet converged.}
}
\]

This curve has been saved as the attack seed for Round 6.

![Holdout Candidate](../figures/08_holdout_challenger.png)

---

# 9. Theoretical Signals of This Round

This round directly quantifies for the first time:

\[
\text{Curve attack pressure}
\longrightarrow
\text{Container rearrangement absorption}
\longrightarrow
\text{Container net increase}.
\]

Yielding:

\[
\boxed{
\text{Approximately }57.7\%\text{ of the initial exposure pressure can be absorbed by reconfiguration.}
}
\]

The remaining approximately:

\[
42.3\%
\]

translates into actual container area growth.

Therefore, merely calculating the "exposure of a new curve against a fixed container" overestimates the area increase of a long-term universal container; the accounting must be done after allowing the container to respond.

---

# 10. Honest Bounds

This round does not prove:

1. The Fourier-12 attack curve is optimal in the function space;
2. The optimal congruent placement has obtained a global certificate;
3. The eight-family non-convex container has reached a global minimum;
4. The holdout sample represents the entire curvature function space;
5. The floating-point curvature box is an Arb/MPFI certificate;
6. This round establishes a new bound for the Kakeya or Moser problem.

---

# 11. The Next Natural Node

Round 6 can directly start the second alternating cycle using the saved holdout candidate.

However, the methodology should be upgraded to:

1. Use signed-distance adjoint gradients to update curvature coefficients;
2. Use continuous erosion clearance instead of pure grid proxies;
3. Synchronously update curve coefficients and rigid body configurations;
4. Use local boundary displacement or level-set reduction on the container side;
5. Record for each round:
   \[
   \text{Attack exposure, recovery amount, net increase}.
   \]
6. Observe whether the net increase sequence converges to zero.

---

# 12. Conclusion

Round 5 completed the first full cycle:

\[
C_4
\longrightarrow
\gamma_5
\longrightarrow
C_5.
\]

Attack curve exposure against the fixed container:

\[
0.006664458451.
\]

Net area increase after container response:

\[
0.002818179861.
\]

Final simply connected area:

\[
\boxed{
A_5
=
0.194262391530.
}
\]

The most important research pivot is:

\[
\boxed{
\text{True universal container research must be an alternating adversarial process between curvature functions and non-convex containers,}
\text{ rather than merely sorting curves against a fixed convex container.}
}
\]