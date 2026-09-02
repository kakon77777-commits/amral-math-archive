# Moser Skew Field Semi-Autonomous Research: Round 10

## —— Complete Phase Contact Interval Map, Envelope Derivatives, and Global Numerical Exclusion Ledger

**Date:** July 26, 2026  
**Status:** Complete phase numerical decomposition; non-strict interval certificate; informal proof  
**Continuation:** Moser Skew Lab v0.9  
**Research Objective:** Decompose the entire phase circle into intervals of fixed active support identities, enumerate all local minima, and verify whether $270^\circ$ remains the global minimum.

---

# 1. Active Support Identities

For each rotation phase $\phi$, record:

$$
\Sigma(\phi)
=
\left(
I_{\min x},
I_{\min y},
I_{\max d}
\right),
$$

where:

$$
d(x,y)=\frac{x}{A}+\frac{y}{B}.
$$

The active labels are:

- `p0`, `p1`, `p2`, `p3`: Curve endpoints and central junction points;
- `L`: Support stationary point inside the left smooth wing;
- `R`: Support stationary point inside the right smooth wing.

Within an interval of fixed signature, the triangle scale is:

$$
s(\phi)
=
n_d(\phi)\cdot p_d(\phi)
-
\frac{n_x(\phi)\cdot p_x(\phi)}{A}
-
\frac{n_y(\phi)\cdot p_y(\phi)}{B}.
$$

---

# 2. Envelope Derivatives

Within an open interval of fixed active identity, the support points are already extrema with respect to the normal functional, so by the envelope theorem:

$$
\boxed{
s'(\phi)
=
n_d'(\phi)\cdot p_d(\phi)
-
\frac{n_x'(\phi)\cdot p_x(\phi)}{A}
-
\frac{n_y'(\phi)\cdot p_y(\phi)}{B}
}.
$$

There is no need to explicitly differentiate the support point positions themselves.

Therefore, each active interval can be classified as:

1. Strictly increasing;
2. Strictly decreasing;
3. Containing one or more smooth stationary points;
4. Non-smooth contact switches at interval boundaries.

---

# 3. Phase Circle Decomposition

The complete phase circle is numerically divided into:

$$
\boxed{
18
}
$$

active identity intervals, containing:

$$
18
$$

distinct signatures.

| Interval | Start | End | Active Signature | Derivative Classification | Interval Minimum | Relative to $270^\circ$ |
|---:|---:|---:|---|---|---:|---:|
| 0 | 0.000000000 | 0.113366183 | `p0|p0|p2` | strictly_decreasing_sampled | 0.998992939447 | 7.860e-05 |
| 1 | 0.113366183 | 0.165413532 | `L|p0|p2` | contains_stationary | 0.998914384874 | 4.579e-08 |
| 2 | 0.165413532 | 0.358185244 | `p1|p0|p2` | strictly_increasing_sampled | 0.998992937554 | 7.860e-05 |
| 3 | 0.358185244 | 0.410232593 | `p1|p0|R` | strictly_increasing_sampled | 1.024754525639 | 2.584e-02 |
| 4 | 0.410232593 | 1.570796327 | `p1|p0|p3` | contains_stationary | 1.040650116923 | 4.174e-02 |
| 5 | 1.570796327 | 1.684162510 | `p2|p0|p3` | strictly_decreasing_sampled | 1.030501754256 | 3.159e-02 |
| 6 | 1.684162510 | 1.736209859 | `p2|L|p3` | contains_stationary | 1.029351988860 | 3.044e-02 |
| 7 | 1.736209859 | 2.094395102 | `p2|p1|p3` | contains_stationary | 0.998914340723 | 1.638e-09 |
| 8 | 2.094395102 | 2.976179122 | `p2|p1|p0` | contains_stationary | 0.998914340723 | 1.638e-09 |
| 9 | 2.976179122 | 3.028226471 | `R|p1|p0` | strictly_decreasing_sampled | 1.099810225768 | 1.009e-01 |
| 10 | 3.028226471 | 3.141592654 | `p3|p1|p0` | strictly_increasing_sampled | 1.099810225768 | 1.009e-01 |
| 11 | 3.141592654 | 3.778557612 | `p3|p2|p0` | contains_stationary | 1.112339567866 | 1.134e-01 |
| 12 | 3.778557612 | 3.830604961 | `p3|p2|L` | contains_stationary | 1.127591529695 | 1.287e-01 |
| 13 | 3.830604961 | 4.546975448 | `p3|p2|p1` | contains_stationary | 1.050201944900 | 5.129e-02 |
| 14 | 4.546975448 | 4.599022797 | `p3|R|p1` | strictly_decreasing_sampled | 1.029774207798 | 3.086e-02 |
| 15 | 4.599022797 | 4.712388980 | `p3|p3|p1` | strictly_decreasing_sampled | 0.998914339085 | -8.371e-14 |
| 16 | 4.712388980 | 5.235987756 | `p0|p3|p1` | contains_stationary | 0.998914339085 | -8.371e-14 |
| 17 | 5.235987756 | 6.283185307 | `p0|p3|p2` | contains_stationary | 1.029825335513 | 3.091e-02 |

This table is the core "global exclusion ledger" of this round: the minimum of each interval can only occur at:

- The left boundary;
- The right boundary;
- The enumerated smooth stationary points.

---

# 4. Multi-Resolution Stability

| Phase Points | Contact Switches | Distinct Signatures | Sampled Local Minima | Sampled Global Minimum | Minimum Phase |
|---:|---:|---:|---:|---:|---:|
| 32768 | 18 | 18 | 8 | 0.998914339084549 | 4.712388980385 |
| 65536 | 18 | 18 | 8 | 0.998914339084549 | 4.712388980385 |
| 131072 | 18 | 18 | 8 | 0.998914339084549 | 4.712388980385 |
| 262144 | 18 | 18 | 8 | 0.998914339084549 | 4.712388980385 |

From:

$$
32768
$$

to:

$$
262144
$$

phase points, all yield:

- $18$ cyclic contact switches;
- $18$ distinct active signatures;
- $8$ sampled local minima;
- The global minimum occurs at:

$$
\phi=\frac{3\pi}{2}.
$$

Therefore, the contact interval map does not generate new microscopic intervals or new local minima as the phase resolution increases.

---

# 5. Smooth Stationary Point Enumeration

Within the complete interval map, a total of:

$$
12
$$

smooth stationary points were found, including local minima, local maxima, and other stationary switches.

| Index | Phase | Scale | Type | Active Signature |
|---:|---:|---:|---|---|
| 0 | 0.124080806550 | 0.998914385986 | smooth_minimum | `L|p0|p2` |
| 1 | 0.139389574289 | 0.998922536883 | smooth_maximum | `L|p0|p2` |
| 2 | 0.154699127028 | 0.998914384874 | smooth_minimum | `L|p0|p2` |
| 3 | 0.994829121178 | 1.247879448750 | smooth_maximum | `p1|p0|p3` |
| 4 | 1.736180225508 | 1.029351988860 | smooth_minimum | `p2|L|p3` |
| 5 | 1.832595717655 | 1.034152222372 | smooth_maximum | `p2|p1|p3` |
| 6 | 2.644378233756 | 1.171701205190 | smooth_maximum | `p2|p1|p0` |
| 7 | 3.480731208101 | 1.179523333677 | smooth_maximum | `p3|p2|p0` |
| 8 | 3.778956292756 | 1.127591529695 | smooth_minimum | `p3|p2|L` |
| 9 | 4.092020570315 | 1.169124263471 | smooth_maximum | `p3|p2|p1` |
| 10 | 5.121148360205 | 1.088598956350 | smooth_maximum | `p0|p3|p1` |
| 11 | 5.717277034815 | 1.220024828834 | smooth_maximum | `p0|p3|p2` |

For each interval, the number of derivative roots remains consistent across three intra-interval sampling densities:

$$
257,\quad1025,\quad4097
$$

Therefore, no additional derivative sign changes hidden between coarse grid points have been discovered so far.

---

# 6. Contact Switch Boundaries

| Index | Phase | Left Signature | Right Signature | Type | Left Derivative | Right Derivative |
|---:|---:|---|---|---|---:|---:|
| 0 | 0.113366182893 | `p0|p0|p2` | `L|p0|p2` | contact_switch_nonextremum | -0.329242 | -0.149183 |
| 1 | 0.165413531955 | `L|p0|p2` | `p1|p0|p2` | contact_switch_nonextremum | 0.149175 | 0.231057 |
| 2 | 0.358185243643 | `p1|p0|p2` | `p1|p0|R` | contact_switch_nonextremum | 0.035390 | 0.129940 |
| 3 | 0.410232592706 | `p1|p0|R` | `p1|p0|p3` | contact_switch_nonextremum | 0.480744 | 0.688658 |
| 4 | 1.570796326795 | `p1|p0|p3` | `p2|p0|p3` | contact_switch_nonextremum | -0.679653 | -0.082514 |
| 5 | 1.684162509688 | `p2|p0|p3` | `p2|L|p3` | contact_switch_nonextremum | -0.200374 | -0.096417 |
| 6 | 1.736209858750 | `p2|L|p3` | `p2|p1|p3` | contact_switch_nonextremum | 0.052249 | 0.099523 |
| 7 | 2.094395102393 | `p2|p1|p3` | `p2|p1|p0` | cusp_minimum | -0.267658 | 0.612416 |
| 8 | 2.976179121634 | `p2|p1|p0` | `R|p1|p0` | contact_switch_nonextremum | -0.381677 | -0.299795 |
| 9 | 3.028226470697 | `R|p1|p0` | `p3|p1|p0` | cusp_minimum | -0.006893 | 0.173166 |
| 10 | 3.141592653590 | `p3|p1|p0` | `p3|p2|p0` | contact_switch_nonextremum | 0.047640 | 0.392398 |
| 11 | 3.778557612081 | `p3|p2|p0` | `p3|p2|L` | contact_switch_nonextremum | -0.346123 | -0.138209 |
| 12 | 3.830604961144 | `p3|p2|L` | `p3|p2|p1` | contact_switch_nonextremum | 0.207609 | 0.302158 |
| 13 | 4.546975448429 | `p3|p2|p1` | `p3|R|p1` | contact_switch_nonextremum | -0.513739 | -0.466464 |
| 14 | 4.599022797492 | `p3|R|p1` | `p3|p3|p1` | contact_switch_nonextremum | -0.318322 | -0.214365 |
| 15 | 4.712388980385 | `p3|p3|p1` | `p0|p3|p1` | cusp_minimum | -0.329480 | 0.432687 |
| 16 | 5.235987755983 | `p0|p3|p1` | `p0|p3|p2` | cusp_minimum | -0.124739 | 0.564777 |

Among these, four contact switches form cusp local minima, while the rest are local maxima or active identity switches that do not change the monotonic direction.

---

# 7. Complete Local Minima Ranking

| Rank | Source | Phase | Scale | Relative to $270^\circ$ | Signature |
|---:|---|---:|---:|---:|---|
| 1 | contact_switch_cusp | 4.712388980385 | 0.998914339084549 | -8.371e-14 | `p3|p3|p1 -> p0|p3|p1` |
| 2 | 120deg | 2.094395102393 | 0.998914340722870 | 1.638e-09 | `p2|p1|p3 -> p2|p1|p0` |
| 3 | smooth_stationary | 0.154699127028 | 0.998914384873594 | 4.579e-08 | `L|p0|p2` |
| 4 | smooth_stationary | 0.124080806550 | 0.998914385986498 | 4.690e-08 | `L|p0|p2` |
| 5 | smooth_stationary | 1.736180225508 | 1.029351988860359 | 3.044e-02 | `p2|L|p3` |
| 6 | contact_switch_cusp | 5.235987755983 | 1.081428573076156 | 8.251e-02 | `p0|p3|p1 -> p0|p3|p2` |
| 7 | contact_switch_cusp | 3.028226470697 | 1.099810225768483 | 1.009e-01 | `R|p1|p0 -> p3|p1|p0` |
| 8 | smooth_stationary | 3.778956292756 | 1.127591529695195 | 1.287e-01 | `p3|p2|L` |

The lowest remains:

$$
\boxed{
\phi=\frac{3\pi}{2}
}
$$

Double-precision contact map value:

$$
0.998914339084549.
$$

Round 9 arbitrary-precision value:

$$
\boxed{
0.99891433908463271725296441853670224618019211931483351998479812835127468110999017\ldots
}.
$$

The difference between the double-precision phase map and the arbitrary-precision value is approximately:

$$
-8.37\times10^{-14}.
$$

---

# 8. Closest Competing Branches

Excluding the duplicate accounting of the same $270^\circ$ cusp by adjacent left and right intervals, the second lowest is:

$$
\phi=\frac{2\pi}{3}.
$$

Arbitrary-precision gap:

$$
s_{120}-s_{270}
\approx
1.6383340692\times10^{-9}.
$$

The two low-phase smooth minima are higher by approximately:

$$
4.5789\times10^{-8},
$$

$$
4.6902\times10^{-8}.
$$

Thus, across the entire phase circle, the only major competition that truly requires strict interval processing is:

$$
\boxed{
120^\circ
\quad\text{vs.}\quad
270^\circ.
}
$$

The remaining intervals have a larger numerical safety margin.

---

# 9. What Global Numerical Exclusion Achieved

This round accomplished:

1. Active identity segmentation of the entire $[0,2\pi)$;
2. Enumeration of all contact switches;
3. Enumeration of all smooth stationary points;
4. A minimum value ledger for each interval;
5. Consistency across four phase resolutions;
6. Consistency of root counts across three derivative sampling densities;
7. Alignment with the arbitrary-precision four-branch results from Round 9.

Therefore, it can currently be stated that:

$$
\boxed{
\text{In the complete phase numerical decomposition,
no other phase branches lower than }270^\circ\text{ were found.}
}
$$

However, this statement cannot be substituted for a strict theorem, because the derivative signs are still confirmed via high-density floating-point sampling and numerical root-finding, rather than interval arithmetic envelopes.

---

# 10. Certificate Status

| Level | Status |
|---|---|
| Complete phase contact segmentation | Numerically complete |
| Multi-resolution contact map consistency | Passed |
| Derivative root count stability per interval | Passed |
| Enumeration of minima for all intervals | Numerically complete |
| Arbitrary-precision recalculation of the four lowest branches | Passed in Round 9 |
| $270^\circ$ Darboux positive lower bound | Passed in Round 9 |
| Strict derivative envelopes for each interval | **Incomplete** |
| Contact boundary interval localization | **Incomplete** |
| Complete global interval certificate | **Incomplete** |
| Formal proof | Not started |

---

# 11. Relationship with Event Control

Smooth candidate arbitrary-precision value:

$$
s_{270}
=
0.9989143390846327172529644185367022461801921193148335199847981283512746\ldots.
$$

Explicit five-bar linkage event control:

$$
s_0
=
0.9989037571325086749551298249005564802172682267121921037894386799512563\ldots.
$$

Difference:

$$
\boxed{
s_{270}-s_0
=
0.00001058195212404229783459363614576596292389260264141619\ldots
}.
$$

Round 9 has already bounded this positive difference using the Darboux lower bound; Round 10 confirms that there are no other lower branches in the complete phase numerical map to offset this elevation.

---

# 12. Round 11 Directions

The next round will not need to scan the entire phase circle again, but should instead convert these $18$ intervals one by one into interval arithmetic objects.

## 12.1 Contact Boundary Boxes

For each switch phase $\phi_k$, establish:

$$
[\underline\phi_k,\overline\phi_k],
$$

and prove that the active identity remains fixed outside the box.

## 12.2 Derivative Intervals

For intervals without stationary points, prove:

$$
0\notin s'(I_k).
$$

## 12.3 Smooth Stationary Point Interval Newton

For intervals containing smooth stationary points, use interval Newton to bound the unique root:

$$
s'(\phi_k^\ast)=0.
$$

Then bound:

$$
s(\phi_k^\ast)-s_{270}.
$$

## 12.4 Special Cusps

For $120^\circ$ and $270^\circ$, use:

- Exact special phases;
- Left and right active formulas;
- One-sided derivative intervals;
- Arbitrary-precision support values;
- Dedicated high-precision envelopes for the $10^{-9}$ scale gap.

---

# 13. Limitations

1. Contact boundaries are currently localized via double-precision bisection;
2. Derivative roots are currently localized via the floating-point Brent's method;
3. The absence of hidden derivative roots relies on multi-grid stability rather than strict bounds;
4. Intra-wing coordinates use high-density Simpson integration and PCHIP interpolation;
5. Arbitrary precision only rechecks the closest control branches;
6. A complete interval certificate has not been established;
7. Formal proof has not been conducted.

---

# 14. Conclusion

Round 10 extends the local cusp verification of Round 9 to the entire phase circle:

$$
\boxed{
[0,2\pi)
=
\bigcup_{k=1}^{18}I_k.
}
$$

In each $I_k$, the active identity is fixed, and all smooth stationary points and contact cusps have been numerically enumerated.

The complete numerical ranking remains:

$$
\boxed{
s_{270}
<
s_{120}
<
s_{\mathrm{low1}}
<
s_{\mathrm{low2}}
<
\text{remaining local minima}.
}
$$

Therefore, the smooth surpassing from Round 8 now has three layers of support:

1. Arbitrary-precision cusp values;
2. Monotonic Darboux positive lower bound;
3. Complete phase contact interval numerical exclusion.

The remaining critical task is to convert the third layer from a "complete numerical ledger" into "strict interval-by-interval envelopes."