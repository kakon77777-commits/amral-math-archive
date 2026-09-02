# Semi-Autonomous Study of Moser Skew Fields: Round 2

## — Phase Jumps, Dual Contact Pressure Ledgers, and Topology-Guided Curve Search

**Date:** July 26, 2026  
**Status:** Exploratory computation; informal proof; non-universal cover certificate  
**Continuation of:** Moser Skew Lab v0.1  
**Scale:** 256 support directions, 360 full rotation phases per curve

---

# 1. Dual Contact Pressure Ledger

For a fixed curve rotation $\phi$, the primal problem is:

$$
\min_{t_x,t_y,s\ge0}s
$$

subject to:

$$
h_\gamma(\theta_j-\phi)+t\cdot u_{\theta_j}-s h_C(\theta_j)\le0.
$$

Non-zero dual multipliers $\lambda_j$ only fall on the support directions that genuinely control the optimal scale. The positive scale solution approximately satisfies:

$$
\sum_j\lambda_j u_{\theta_j}=0,
$$

$$
\sum_j\lambda_j h_C(\theta_j)=1,
$$

$$
s_\ast=\sum_j\lambda_j h_\gamma(\theta_j-\phi).
$$

This indicates that the active normal pressures are self-balancing, decomposing the minimum scale into an auditable contact pressure ledger.

Maximum numerical errors:

- Primal feasibility residual: 2.987e-15;
- Normal balance residual: 3.140e-16;
- Dual normalization residual: 2.220e-16;
- Duality gap: 4.441e-16.

---

# 2. Full Phase Scan

| Curve | Minimum Scale | Phase Barrier | Local Minima | Jump Points | Container Contact Signatures |
|---|---:|---:|---:|---:|---:|
| U_equal | 0.951236875 | 0.177263986 | 8 | 27 | 1 |
| arc_270 | 0.922316000 | 0.127589662 | 31 | 26 | 1 |
| semicircle | 0.913857419 | 0.620026793 | 3 | 26 | 2 |
| segment | 0.910859678 | 1.182791197 | 2 | 26 | 4 |
| round1_adversarial | 0.913756411 | 0.764323330 | 4 | 26 | 2 |

The phase barrier is defined as:

$$
B_\phi=\max_\phi s(\phi)-\min_\phi s(\phi).
$$

It describes the additional scale due to directional misalignment and is not equivalent to the Moser difficulty of the curve; universal cover is only concerned with $\min_\phi s(\phi)$.

---

# 3. Structure of Phase Jumps

The optimal translation forms a piecewise smooth path in phase space. When the dual active directions change:

- Translation derivatives jump;
- Contact weights are redistributed;
- Curve support points controlling the container scale change;
- Phase space enters a new placement mechanism regime.

The primal variables are only $(t_x,t_y,s)$, so non-degenerate optimal solutions are typically controlled by a small number of active directions. This explains why the large number of "near-zero residual directions" in Round 1 does not equate to a large number of independent contacts.

---

# 4. Topology-Guided Three-Link Search

Equal-length U-shaped baseline:

$$
(\alpha,0,-\alpha),\qquad(l,1-2l,l),
$$

$$
\alpha=90^\circ,\qquad l=\frac13.
$$

This round scans $65^\circ\le\alpha\le115^\circ$ and $0.18\le l\le0.42$, then generates 120 asymmetric local candidates.

High-resolution baseline:

$$
s_U=0.9512368779.
$$

Best topology-guided candidate:

$$
s_{\mathrm{topo}}=0.9933108210.
$$

Difference:

$$
\Delta s=4.2073943098e-02.
$$

Optimal parameters:

$$
(l_1,l_2,l_3)=(0.28724539,0.38561210,0.32714251),
$$

$$
(\alpha_1,\alpha_3)=(92.468232^\circ,80.979113^\circ).
$$

This is merely a numerical extremum within the finite three-link family, not an extremum for all unit arcs.

---

# 5. Contact Pressure Ledger of the Best Candidate

| Contact | Support Direction (degrees) | Dual Weight | Container Feature |
|---:|---:|---:|---|
| 1 | 29.53125 | 2.09372094 | vertex:1 |
| 2 | 180.00000 | 1.82171936 | edge:0-2 |
| 3 | 270.00000 | 1.03199127 | edge:0-1 |

Conservation residuals:

$$
\left\|\sum_j\lambda_j u_{\theta_j}\right\|=3.140e-16,
$$

$$
\left|\sum_j\lambda_j h_C(\theta_j)-1\right|=2.220e-16,
$$

$$
\left|s_\ast-\sum_j\lambda_j h_\gamma(\theta_j-\phi)\right|=1.110e-16.
$$

---

# 6. Assessment of this Round

The three-link family can still provide high-pressure candidates, but it has not yet approached the Wetzel certified scale of $1$. The true next step should not simply be to continue adding random polylines, but rather to shift from "curve coordinate search" to "contact ledger search".

The next round will establish a reverse generator for contact ledgers. Input:

$$
\{(\theta_j,\lambda_j)\}_{j=1}^m,
$$

with the requirement:

$$
\sum_j\lambda_j u_{\theta_j}\approx0.
$$

Then, reversely construct a curve of total length one such that the specified directions simultaneously form high-pressure active contacts.

Scoring will incorporate:

1. Critical scale;
2. Dual weight entropy;
3. Contact signature novelty;
4. Topological competition near the optimal phase;
5. Higher-order skewness spectrum;
6. Four- to eight-link polylines and curvature arc segments.

---

# 7. Unclaimed Matters in this Round

1. No new Moser upper or lower bounds are proposed;
2. The three-link candidate is not proven to be an extremum of any continuous curve family;
3. Interval certificates were not executed;
4. The 599 SOCP models from Wetzel's paper were not rerun;
5. Lean/Coq formalization was not performed;
6. Phase discretization results are not treated as continuous complete proofs.

---

# 8. Reference Baselines

1. W. Wichiramala and C. Panraksa, *Wetzel's 30-60-90 Triangle Covers Unit Arcs*, arXiv:2606.14625, 2026.
2. T. Khandhawit, D. Pagonakis, and S. Sriswasdi, *Lower Bound for Convex Hull Area and Universal Cover Problems*, arXiv:1101.5638.