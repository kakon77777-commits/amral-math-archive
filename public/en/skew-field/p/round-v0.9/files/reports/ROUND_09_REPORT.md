# Centrally Generated Kakeya-Moser Bridging Family: Round 9

## ——Fifth Non-Convex Alternating Cycle, Transient Forcing Curves, and Fourier/B-spline Multi-Family Residuals

**Version:** v0.9  
**Date:** July 28, 2026  
**Status:** Finite Fourier/B-spline curvature families, finite congruence search, and non-convex container coordinate descent candidates

---

# 1. Fifth Alternating Cycle

Completed in this round:

\[
C_8
\longrightarrow
\gamma_9
\longrightarrow
C_9.
\]

The formal attack is the Fourier-18 mixed-type candidate saved from Round 8.

---

# 2. Formal Attack

Optimal exposed area:

\[
\boxed{
e_9
=
0.004050717099.
}
\]

Accounts for approximately this percentage of the single tube area:

\[
4.7641\%.
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

Thus:

\[
\frac1{\max\kappa}
\ge
0.049050799562
>
0.04.
\]

---

# 3. Container Response

Round 8:

\[
A_8
=
0.208938653597.
\]

Naive addition:

\[
A_{\mathrm{naive}}
=
0.212989343905.
\]

After rearranging the twelve families:

\[
\boxed{
A_9
=
0.211402629026.
}
\]

The final union is connected, valid, and hole-free.

Recovered area:

\[
0.001586714880.
\]

Absorption rate:

\[
\eta_9
=
39.1712\%.
\]

Net increment:

\[
\boxed{
\Delta A_9
=
0.002463975428.
}
\]

Increase relative to Round 8:

\[
1.1793\%.
\]

![Area Sequence](../../../../skew-field/p/round-v0.9/files/figures/01_area_sequence.png)

![Attack vs Net Increment](../../../../skew-field/p/round-v0.9/files/figures/02_attack_vs_net_increment.png)

![Absorption and Novelty](../../../../skew-field/p/round-v0.9/files/figures/03_absorption_novelty.png)

---

# 4. Increment Sequence

\[
\begin{aligned}
\Delta A_5&=0.002818179861,\\
\Delta A_6&=0.004464130667,\\
\Delta A_7&=0.005593838791,\\
\Delta A_8&=0.004618292548,\\
\Delta A_9&=0.002463975428.
\end{aligned}
\]

Round 9 has the lowest net increment among Rounds 5 to 9.

However, the Fourier-20 and B-spline reserved candidates for the next round still have positive exposure, so this is merely a single-round low point.

---

# 5. Transient Forcing Curve

The exposure of the Round 9 attack in the fixed old container is:

\[
0.004050717099.
\]

But after the update, the leave-one-out exposure drops to:

\[
0.000664164818
<
10^{-3}.
\]

Therefore, it is nearly redundant under the final-state activity threshold, yet it genuinely caused a net container growth of:

\[
0.002463975428.
\]

This establishes:

\[
\boxed{
\text{Historical forcing}
\not\Rightarrow
\text{Final-state activity}.
}
\]

![Transient Forcing](../../../../skew-field/p/round-v0.9/files/figures/10_transient_forcing.png)

---

# 6. Final-State Active Families

Using a leave-one-out exposure of \(10^{-3}\) as the threshold:

1. `round3_double_harmonic`: 0.006981984814
2. `round4_fourier10`: 0.009658593581
3. `round5_fourier12`: 0.001911602351
4. `round7_fourier14`: 0.004708312773
5. `round8_fourier16`: 0.001952499210

The Round 9 formal attack did not make this list.

Thus, the final static skeleton and the attack history must be preserved separately.

![Final Container](../../../../skew-field/p/round-v0.9/files/figures/06_final_container.png)

![Activity Ledger](../../../../skew-field/p/round-v0.9/files/figures/08_leave_one_out.png)

---

# 7. Fourier-20 Three Pools

Dispersed parent optimal exposure:

\[
0.003755030295.
\]

Local parent:

\[
0.000000000000.
\]

Mixed parent:

\[
\boxed{
0.004423629900.
}
\]

All refined candidates from the local parent in this batch were absorbed, but the dispersed and mixed parents remain positive.

---

# 8. Non-Fourier B-spline Reserve Pool

The moving-knot natural cubic B-spline candidate leaves:

\[
\boxed{
e_{\mathrm{spline}}
=
0.002135639003.
}
\]

Its curvature box:

\[
\max\kappa
\in
[
15.157618959651,
15.190835559256
],
\]

Thus:

\[
\frac1{\max\kappa}
\ge
0.065829163649
>
0.04.
\]

This indicates that residual exposure does not exist solely within the Fourier homologous curvature family.

![Pool Audit](../../../../skew-field/p/round-v0.9/files/figures/07_pool_audit.png)

---

# 9. Round 10 Seed

The strongest Fourier-20 mixed parent candidate:

\[
\boxed{
e_9^{\mathrm{res}}
=
0.004423629900.
}
\]

Curvature box:

\[
\max\kappa
\in
[
20.787610395035,
20.938252289988
],
\]

Conservative radius of curvature:

\[
0.047759478019.
\]

Its exposure is split into five connected components, with the largest component accounting for:

\[
63.2415\%,
\]

Effective gap box count:

\[
10.332930.
\]

It has been saved as the initial attack for Round 10.

![Residual Challengers](../../../../skew-field/p/round-v0.9/files/figures/09_residual_challengers.png)

---

# 10. Theoretical Feedback

Three separation quantities are introduced in this round:

1. Attack volume on the fixed old container:
   \[
   e_n;
   \]

2. Net cost after container response:
   \[
   \Delta A_n;
   \]

3. Final-state leave-one-out activity:
   \[
   \ell_n.
   \]

For Round 9:

\[
e_9
>
\Delta A_9
>
\ell_9.
\]

Therefore, the attack strength of a curve, its historical causal cost, and its final-state structural necessity are distinct concepts.

---

# 11. Convergence Diagnostics

Although the net increment in Round 9 dropped to the current lowest, we have:

- Fourier-20 dispersed pool is positive;
- Fourier-20 mixed pool is positive;
- Moving-knot B-spline pool is positive.

Therefore:

\[
\boxed{
\text{There is currently no evidence of synchronous closure across multi-phenotype, multi-representation families.}
}
\]

---

# 12. Honesty Bounds

This round does not prove:

1. That Fourier-18 is the globally strongest attack for Round 9;
2. That the twelve-family non-convex container is the global minimum;
3. That the Fourier-20 seed is optimal over the complete curvature space;
4. That the B-spline reserve pool represents all non-Fourier curvature families;
5. That the optimal congruence placement possesses a formal certificate;
6. That the floating-point curvature box is a formal interval certificate;
7. That this round establishes a new area bound for the Kakeya or Moser problems.

---

# 13. Next Natural Node

Round 10 can directly use the saved Fourier-20 mixed candidate.

Simultaneously, the following should be retained:

- Fourier dispersed pool;
- Fourier local pool;
- Fourier mixed pool;
- Moving-knot B-spline pool.

The container stopping condition should require the residuals of all pools to decrease simultaneously, rather than merely observing a single strongest candidate.

---

# 14. Conclusion

The final simply connected area for Round 9 is:

\[
\boxed{
A_9
=
0.211402629026.
}
\]

The most important new conclusion of this round is:

\[
\boxed{
\text{A curve can historically force the container to expand,}
\text{yet become sub-active or even near-redundant after the update.}
}
\]

Therefore, the research ledger for non-convex universal containers must simultaneously preserve both the attack history and the final-state structure.