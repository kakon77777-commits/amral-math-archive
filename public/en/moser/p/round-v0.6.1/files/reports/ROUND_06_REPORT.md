# Semi-Autonomous Study of the Moser Skew Field: Round 6

## ——Chiral Escape, Eight-Dimensional Contact Topology Search, and Local Stability Draft

**Date:** July 26, 2026  
**Status:** Exploratory numerical study; non-formal proof; non-interval certificate  
**Continuation:** Moser Skew Lab v0.5  
**Objective:** Depart from the fixed mirror-symmetric 5-link platform to test asymmetric directions and new contact identities

---

# 1. General 5-Link Neighborhood

The isolated candidate from Round 5 is described by four symmetric parameters:

$$
(l_1,l_2,\beta,\delta).
$$

This round introduces four antisymmetric parameters:

$$
(d_{l_1},d_{l_2},d_\alpha,d_\beta).
$$

The lengths become:

$$
(l_1+d_{l_1},
 l_2+d_{l_2},
 l_3,
 l_2-d_{l_2},
 l_1-d_{l_1}),
$$

The directions become:

$$
(\alpha+d_\alpha,
 \beta+d_\beta,
 0,
 -\beta+d_\beta,
 -\alpha+d_\alpha).
$$

The research objective remains the congruence difficulty:

$$
s_{\mathrm{cong}}(\gamma)
=
\min\{s_+(\gamma),s_-(\gamma)\}.
$$

Therefore, any single-chirality improvement must be jointly supported by the mirror branch; otherwise, it is not considered a breakthrough.

---

# 2. Four Basic Chiral Modes

| Mode | Optimal Perturbation | Relative Central Gain | Max Chiral Difference in Scan |
|---|---:|---:|---:|
| outer_length_antisym | 0.000000000e+00 | 0.000000000e+00 | 1.686411486e-03 |
| inner_length_antisym | 0.000000000e+00 | 0.000000000e+00 | 2.448355423e-03 |
| outer_angle_antisym | 0.000000000e+00 | 0.000000000e+00 | 1.328757456e-02 |
| inner_angle_antisym | 0.000000000e+00 | 0.000000000e+00 | 5.369528921e-03 |

The common characteristics of the four single-mode scans are:

- The original curve branch and the mirror branch vary in opposite directions;
- The congruence objective takes the minimum of the two;
- A cusp or near-cusp forms around zero perturbation;
- Breaking left-right symmetry alone does not provide a stable positive gain.

Thus:

$$
\boxed{
\text{Mirror symmetry is not an arbitrary aesthetic constraint,
but the natural equilibrium point of the congruence minimum for the chiral branches.}
}
$$

---

# 3. Eight-Dimensional Topological Escape Search

A simultaneous search was conducted over the four symmetric and four antisymmetric parameters, with the final candidate re-verified using $131072$ phase points and local refinement.

Congruence scale of the best candidate:

$$
s_{\mathrm{escape}}
=
0.998557207698881.
$$

Relative to the Round 5 event scale:

$$
s_{\mathrm{escape}}-s_{\mathrm{event}}
=
-3.465494336274e-04.
$$

Distance to the certified scale:

$$
1-s_{\mathrm{escape}}
=
1.442792301119e-03.
$$

Chiral difference:

$$
\chi_{\mathrm{escape}}
=
3.303777160502e-05.
$$

The antisymmetric parameters are:

$$
d_{l_1}=1.111783809093e-02,
\quad
d_{l_2}=-1.114055830434e-02,
$$

$$
d_\alpha=-0.357266992^\circ,
\quad
d_\beta=0.368096323^\circ.
$$

If these values reconverge to zero, it indicates that the eight-dimensional search did not find a true chiral escape, but rather returned to the mirror-symmetric platform.

---

# 4. Random Contact Topology Census

1600 general 5-links were sampled near the event solution. A coarse dual-chirality phase evaluation was performed first, followed by a high-resolution re-verification of the top twenty.

Top ten:

| Rank | Congruence Scale | Chiral Difference | Winning Branch Contact Signature |
|---:|---:|---:|---|
| 1 | 0.996355596021 | 1.065e-03 | {"bottom": [5], "hypotenuse": [2], "left": [0, 5]} |
| 2 | 0.996179294211 | 1.109e-03 | {"bottom": [2], "hypotenuse": [0, 5], "left": [3]} |
| 3 | 0.996198796374 | 1.955e-03 | {"bottom": [3], "hypotenuse": [0, 5], "left": [2]} |
| 4 | 0.996055603749 | 1.456e-03 | {"bottom": [5], "hypotenuse": [2], "left": [4, 5]} |
| 5 | 0.995738890698 | 1.409e-03 | {"bottom": [2], "hypotenuse": [0, 5], "left": [3]} |
| 6 | 0.995550378570 | 1.031e-04 | {"bottom": [2], "hypotenuse": [0, 5], "left": [3]} |
| 7 | 0.995536814088 | 2.074e-03 | {"bottom": [3], "hypotenuse": [0, 5], "left": [2]} |
| 8 | 0.995460296273 | 2.951e-03 | {"bottom": [3], "hypotenuse": [0, 5], "left": [2]} |
| 9 | 0.995490044035 | 8.661e-04 | {"bottom": [2], "hypotenuse": [0, 5], "left": [3]} |
| 10 | 0.995631912709 | 6.065e-04 | {"bottom": [2], "hypotenuse": [0, 5], "left": [3]} |

Among the top twenty, there appeared:

$$
5
$$

distinct winning contact signatures.

The critical criterion is not the number of signature types, but whether a new signature can simultaneously:

1. Exceed the event scale;
2. Maintain a low chiral difference;
3. Pass the complete phase re-verification for both mirror branches.

---

# 5. Local Contact Stability Draft

Existing diagnostics for the Round 5 event root:

$$
\sigma_{\min}(J)
=
3.607219048175e-02,
$$

$$
\kappa(J)
=
162.781733366.
$$

Minimum absolute one-sided slope of the four cusps:

$$
\min |D_\pm s|
=
2.377371632889e-02.
$$

At the event root, the minimum geometric gap of the inactive vertices for each branch has been saved in:

`data/round06_summary.json`

Random sampling was then performed within the symmetric parameter box:

| Parameter Box Radius | Maintained 4-Signatures | Ratio | Min Observed Inactive Gap |
|---:|---:|---:|---:|
| 1.0e-07 | 500/500 | 1.000 | 6.736e-03 |
| 2.0e-07 | 500/500 | 1.000 | 6.736e-03 |
| 5.0e-07 | 500/500 | 1.000 | 6.736e-03 |
| 1.0e-06 | 500/500 | 1.000 | 6.736e-03 |
| 2.0e-06 | 500/500 | 1.000 | 6.736e-03 |
| 5.0e-06 | 500/500 | 1.000 | 6.735e-03 |
| 1.0e-05 | 500/500 | 1.000 | 6.734e-03 |
| 2.0e-05 | 500/500 | 1.000 | 6.732e-03 |
| 5.0e-05 | 500/500 | 1.000 | 6.727e-03 |
| 1.0e-04 | 500/500 | 1.000 | 6.718e-03 |
| 2.0e-04 | 500/500 | 1.000 | 6.701e-03 |
| 5.0e-04 | 500/500 | 1.000 | 6.642e-03 |

This is a draft of a local numerical certificate, not an interval proof. It only demonstrates that within the sampled small neighborhood:

- The four contact identities do not immediately collapse;
- The inactive vertices still maintain a positive gap;
- The directional derivatives of the cusps and the non-singularity of the Jacobian provide additional stability signals.

---

# 6. Round Verdict

This round simultaneously examines two possibilities.

## 6.1 If the Eight-Dimensional Candidate Does Not Surpass

Then the current data supports:

$$
\boxed{
\text{The isolated candidate from Round 5 is not only stationary in the symmetric subspace,
but also possesses local stability against small antisymmetric breakings.}
}
$$

This would shift the focus of the next round toward different segment counts, curvature arcs, or entirely different contact sequences, rather than continuing to fine-tune within the 5-link neighborhood.

## 6.2 If a Stable Surpass is Found

Then the following must be re-established:

- New contact events;
- A new dual-chirality branch ledger;
- A new KKT system;
- A new local stability audit.

Any curve that surpasses only in a single chirality will not be counted.

---

# 7. Directions for Round 7

Based on the results of this round, the priorities for the next round are as follows:

1. If the 5-link eight-dimensional neighborhood is closed: shift to the "mixed polyline-curvature arc family";
2. If a new signature appears but does not surpass: use this signature for reverse contact generation;
3. If the local signature stability box is sufficiently clear: begin the Krawczyk / Interval Newton draft;
4. If an asymmetric candidate surpasses: reconstruct its event equations first, without rushing to expand the curve family.

---

# 8. Limitations

1. The eight-dimensional search remains a floating-point heuristic;
2. The dual-chirality phase re-verification is not an interval-complete proof;
3. The local stability box uses random sampling;
4. There is no proof that the event root is locally optimal for all general 5-links;
5. No new Moser upper or lower bounds are proposed;
6. No formal proof has been conducted.

---

# 9. Conclusion

The question for Round 6 is not to chase another prettier decimal, but to determine:

$$
\boxed{
\text{Whether the current 5-link platform can be escaped via chiral breaking or new contact signatures.}
}
$$

The eight-dimensional congruence search, the four chiral modes, and the local contact stability box collectively provide the first numerical ledger for this determination.