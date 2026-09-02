# Semi-Autonomous Study of the Moser Skewness Field: Round 4

## — Phase Branch Ledgers, Sensitivity Matrices, and Four-Branch Leveling

**Date:** July 26, 2026  
**Status:** Exploratory numerical study; non-formal proof; non-universal covering certificate  
**Curve Family:** Mirror-symmetric 5-link chain  
**Container Core:** Exact tri-normal formula for the Wetzel certificate triangle

---

# 1. Problem for this Round

The critical scale of the 5-link chain in Round 3 was:

$$
s_5^{(3)}=0.998754371668.
$$

Denote the four lowest phase branches as:

$$
m_1(\eta),\ldots,m_4(\eta),
$$

where:

$$
\eta=(l_1,l_2,\beta,\delta).
$$

This round directly solves:

$$
\max_{\eta,z}z
$$

subject to:

$$
m_r(\eta)\ge z,
\qquad r=1,\ldots,4.
$$

---

# 2. Branch Leveling Results

| Branch | Phase Region | Round 3 | Round 4 | Optimal Phase |
|---:|---|---:|---:|---:|
| 1 | B1 low phase | 0.999388066722 | 0.998903763498 | 0.114909854 |
| 2 | B2 low phase | 0.999238612437 | 0.998903763495 | 0.162556218 |
| 3 | B3 120° | 0.998754376311 | 0.998903763495 | 2.094395111 |
| 4 | B4 270° | 0.999301890611 | 0.998903763495 | 4.712389010 |

Gap between the four branches after leveling:

$$
\max_r m_r-\min_r m_r
=
2.734812376559e-12.
$$

Critical scale from a full-phase rescan:

$$
\boxed{
s_5^{(4)}=0.998903750476
}.
$$

Improvement relative to Round 3:

$$
\Delta s=1.493788082036e-04.
$$

Distance to the certified scale $1$:

$$
1-s_5^{(4)}=1.096249523642e-03.
$$

---

# 3. Parameter Reallocation

Round 3:

$$
(l_1,l_2,l_3)
=
(0.1915275890,0.1440083663,0.3289280894),
$$

$$
(\beta,\alpha)
=
(80.87459061^\circ,83.20204747^\circ).
$$

Round 4:

$$
\boxed{
(l_1,l_2,l_3)
=
(0.1943225812,0.1415865167,0.3281818042)
},
$$

$$
\boxed{
(\beta,\alpha)
=
(80.68621471^\circ,83.41615042^\circ)
}.
$$

The outer segments slightly increased, while the inner segments slightly decreased; the inner angles decreased, and the outer angles increased. This is equivalent to strengthening the endpoint-hypotenuse contact while reconfiguring the control of the internal vertices over the left and bottom edges.

---

# 4. Branch Contact Ledger

| Branch | Name | Left Edge Contact | Bottom Edge Contact | Hypotenuse Contact |
|---:|---|---|---|---|
| 1 | B1 low phase | [0, 1] | [0] | [3] |
| 2 | B2 low phase | [1, 2] | [0] | [3] |
| 3 | B3 120° | [3] | [2] | [0, 5] |
| 4 | B4 270° | [0, 5] | [5] | [2] |

The four branches utilize different vertex identities and boundary arrangements. Therefore, what is being leveled are the local optima of different contact topologies, rather than rotated copies of the same placement.

---

# 5. Branch Sensitivity Matrix

$$
G_{rj}
=
\frac{\partial m_r}{\partial\eta_j}.
$$

| Branch | $\partial_{l_1}$ | $\partial_{l_2}$ | $\partial_\beta$ | $\partial_\delta$ |
|---|---:|---:|---:|---:|
| B1 low phase | -2.80882321 | -2.72325088 | -0.27436981 | -0.02382433 |
| B2 low phase | -2.88525400 | -2.88408375 | -0.24383978 | -0.00974016 |
| B3 120° | 0.26806247 | 0.25422165 | 0.09494274 | 0.04679436 |
| B4 270° | -0.17308714 | -0.13546270 | -0.26760573 | -0.16241876 |

Different branches react in conflicting directions to the same parameter. There is no local direction that allows all four branches to rise simultaneously, thus forming a max-min leveled point.

---

# 6. Second-Layer Branch Pressure Ledger

Find:

$$
\mu_r\ge0,
\qquad
\sum_r\mu_r=1,
$$

such that:

$$
\sum_r\mu_r\nabla_\eta m_r\approx0.
$$

| Branch | Name | Branch Pressure |
|---:|---|---:|
| 1 | B1 low phase | 0.0280095829 |
| 2 | B2 low phase | 0.0287990896 |
| 3 | B3 120° | 0.7367588828 |
| 4 | B4 270° | 0.2064324448 |

Stationary residual:

$$
\left\|
\sum_r\mu_r\nabla_\eta m_r
\right\|
=
1.840159765877e-07.
$$

This forms a two-layer pressure ledger:

1. Geometric contact pressure: container boundary normals and curve support points;
2. Phase branch pressure: checks and balances on curve parameters by different optimally placed branches.

---

# 7. Study Verdict

This round confirms:

$$
\boxed{
\text{Without increasing the number of segments, merely leveling the weakest phase branches
can still continue to improve the critical scale of the finite family of 5-link chains.}
}
$$

However, the improvement has narrowed to approximately $10^{-4}$. The candidate remains below $1$, failing to form a new Moser lower bound or a Wetzel counterexample.

More importantly:

$$
\boxed{
\text{The difficulty of the curve does not lie in a single contact ledger,
but in a multi-ledger equilibrium of a set of competing placement branches.}
}
$$

---

# 8. Directions for Round 5

The next round will formulate the four-branch leveling and fixed contact identities into a low-dimensional system of equations:

$$
F(\eta,\phi_1,\ldots,\phi_4,s)=0.
$$

To investigate:

1. Whether the four-branch intersection is an isolated point;
2. Whether the active vertex identities are stable in the neighborhood;
3. Whether contact event equations can replace black-box optimization;
4. Whether the leveled point of the 5-link chain is already approaching the limit within this contact topology;
5. Whether new contact identities exist that can break through the current $0.9989$ plateau.

---

# 9. Limitations

1. Branch local minima use floating-point 1D optimization;
2. Sensitivities use finite differences;
3. SLSQP has no guarantee of global optimality;
4. Interval certificates have not yet been established;
5. Active identities have not yet been proven stable in a complete neighborhood;
6. No new Moser upper or lower bounds have been proposed;
7. No formal proof has been conducted.

---

# 10. Conclusion

Round 4 result:

$$
\boxed{
s_5=0.998903750476
}.
$$

The leveling error of the four lowest branches is:

$$
2.734812376559e-12.
$$

Currently, the 5-link chain is no longer constrained by a single obviously weak branch, but is jointly counterbalanced by four different placement mechanisms. The next stage should rewrite this non-smooth intersection as contact event equations to directly study its structure.