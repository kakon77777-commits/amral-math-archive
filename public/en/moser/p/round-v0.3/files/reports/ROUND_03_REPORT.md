# Semi-Autonomous Study of Moser Skewness Fields: Round 3

## — Reverse Generation of Contact Ledgers, Mirror-Symmetric Multi-Link Chains, and Validity Testing of Degrees of Freedom

**Date:** July 26, 2026  
**Status:** Exploratory numerical study; non-formal proof; non-universal covering certificate  
**Container Core:** Exact three-normal formula for the Wetzel certified triangle  
**Search Family:** Mirror-symmetric 3-, 5-, and 7-segment polygonal chains

---

# 1. Methodology of This Round

Round 2 revealed that high-pressure three-link chains possess:

- Almost zero chiral skewness;
- Three segments of nearly equal length;
- Left-right near mirror symmetry;
- Synchronized activity across the three triangle boundaries.

Therefore, instead of randomly generating from arbitrary curve coordinates, this round restricts the search space by reverse-engineering from a target contact ledger:

$$
\mathcal T=
\{\mathrm{left},\mathrm{bottom},\mathrm{hypotenuse}\},
$$

and enforces mirror symmetry on the curve, such that:

$$
s_+(\gamma)=s_-(\gamma).
$$

Chiral false alarms are thus eliminated at the parameter level.

## 1.1 Five-Link Family

$$
(\alpha,\beta,0,-\beta,-\alpha),
$$

$$
(l_1,l_2,l_3,l_2,l_1).
$$

## 1.2 Seven-Link Family

$$
(\alpha,\beta,\gamma,0,-\gamma,-\beta,-\alpha),
$$

$$
(l_1,l_2,l_3,l_4,l_3,l_2,l_1).
$$

All segment lengths are positive, with the total length normalized to $1$.

---

# 2. Exact Accommodation Core

For a fixed rotation phase $\phi$:

$$
s(\phi)=
\max_i\left(
\frac{x_i(\phi)}A+\frac{y_i(\phi)}B
\right)
-
\frac{\min_i x_i(\phi)}A
-
\frac{\min_i y_i(\phi)}B.
$$

The outer-layer difficulty is:

$$
s_\ast(\gamma)=\min_\phi s(\phi).
$$

Search objective:

$$
\max_{\gamma\in\mathcal F_n}s_\ast(\gamma),
$$

where $\mathcal F_n$ is the specified family of mirror-symmetric $n$-segment polygonal chains.

Approximate support angles are no longer used to describe the triangle here. The three half-spaces constitute the complete finite description of the container.

---

# 3. Three-Link Baseline

The Round 2 candidate was re-evaluated using a maximum $65536$-phase grid and local refinement:

$$
s_3=0.998574374711.
$$

Optimal phase:

$$
\phi_3=2.094396758064.
$$

The number of local minima in the phase landscape is:

$$
N_3=7.
$$

Contact ledger:

> Left boundary vertex [2]; Bottom boundary vertex [1]; Hypotenuse vertices [0, 3]

---

# 4. Five-Link Results

Optimal five-link chain:

$$
\boxed{
s_5=0.998754371668.
}
$$

Gain relative to the three-link chain:

$$
\boxed{
s_5-s_3=1.799969565222e-04.
}
$$

Distance to the certified scale of $1$:

$$
1-s_5=1.245628332221e-03.
$$

Length structure:

$$
(l_1,l_2,l_3,l_2,l_1)
=
(0.1915275890,0.1440083663,0.3289280894,0.1440083663,0.1915275890).
$$

Directional structure:

$$
(\alpha,\beta,0,-\beta,-\alpha),
$$

$$
\alpha=83.20204747^\circ,
\qquad
\beta=80.87459061^\circ.
$$

The two outer directions are very close to the two inner directions. This indicates that the five-segment curve is not composed of five completely independent directions, but rather splits each side of the original three-link chain into two nearly parallel sub-segments.

Optimal phase:

$$
\phi_5=2.094395102393.
$$

Contact ledger:

> Left boundary vertex [3]; Bottom boundary vertex [2]; Hypotenuse vertices [0, 5]

Specifically, the hypotenuse is simultaneously contacted by the two endpoints of the curve, while the left and bottom boundaries are controlled by two internal vertices, respectively. The effective number of contacts is $4$.

---

# 5. Seven-Link Results

Optimal seven-link chain:

$$
s_7=0.998674157956.
$$

Relative to the three-link chain:

$$
s_7-s_3=9.978324505744e-05.
$$

Relative to the five-link chain:

$$
\boxed{
s_7-s_5=-8.021371146472e-05.
}
$$

The seven-segment family did not surpass the five-segment family in this round of search.

Length structure:

$$
(l_1,l_2,l_3,l_4,l_3,l_2,l_1)
=
(0.1235587192,0.1387194732,0.0726712116,0.3301011921,0.0726712116,0.1387194732,0.1235587192).
$$

Angular structure:

$$
(\alpha,\beta,\gamma,0,-\gamma,-\beta,-\alpha),
$$

$$
\alpha=83.13833037^\circ,
\quad
\beta=82.51914854^\circ,
\quad
\gamma=80.18827111^\circ.
$$

The three positive angles are distributed only within a narrow interval of approximately $80^\circ$ to $83^\circ$. In other words, the seven-segment solution also degenerates into a low-dimensional skeleton of "nearly vertical flanks plus a central horizontal segment," rather than utilizing seven significantly distinct directions.

Contact ledger:

> Left boundary vertex [4]; Bottom boundary vertex [3]; Hypotenuse vertices [0, 7]

---

# 6. Validity Assessment of Degrees of Freedom

The results of this round are:

$$
s_3=0.998574374711,
$$

$$
s_5=0.998754371668,
$$

$$
s_7=0.998674157956.
$$

Therefore:

$$
\Delta_{5,3}=1.799969565222e-04,
$$

$$
\Delta_{7,5}=-8.021371146472e-05.
$$

The first conclusion is:

$$
\boxed{
\text{The three-link chain is not the endpoint in this search framework;
the five-link chain can generate a small but stable higher pressure.}
}
$$

The second conclusion is:

$$
\boxed{
\text{Increasing to seven segments did not yield further improvement;
the newly added parameters largely degenerated into nearly parallel sub-segments.}
}
$$

Therefore, the current effective degrees of freedom are not the "number of segments," but rather:

1. Whether new independent active vertices can be added;
2. Whether the lowest phase branch can be elevated;
3. Whether endpoints and internal contacts can be redistributed without creating new, easier-to-place phases;
4. Whether multiple local minima can be raised simultaneously.

---

# 7. Four-Contact Skeleton

Both the optimal five-segment and seven-segment candidates exhibit the same contact topology:

$$
\boxed{
2\text{ endpoints contacting the hypotenuse}
+
1\text{ internal vertex contacting the left boundary}
+
1\text{ internal vertex contacting the bottom boundary}.
}
$$

The triangle has only three boundary normals, but the curve allows the same hypotenuse constraint to be simultaneously saturated by two endpoints. This is the most important structural discovery of Round 3.

It indicates that the contact ledger should not only record the normal types:

$$
\{\mathrm{left},\mathrm{bottom},\mathrm{hypotenuse}\},
$$

but must also record how many curve support points exist on each normal, as well as their order in the curve parameters:

$$
\mathcal T^\sharp
=
\{(f_j,I_j,\lambda_j)\},
$$

where $I_j$ is the set of contact vertex indices.

---

# 8. Equalization of Phase Minima Branches

The goal of a difficult curve is not to create a very high phase peak, but to raise:

$$
m_1(\gamma)
=
\min_\phi s(\phi).
$$

If the primary local minima are ordered as:

$$
m_1\le m_2\le\cdots,
$$

raising only $m_2$ or a certain peak cannot increase the true difficulty. This makes the next step:

$$
\boxed{
\text{Identify the lowest placement branch}
\longrightarrow
\text{Recognize its contact ledger}
\longrightarrow
\text{Modify only the curve degrees of freedom that can elevate this branch}.
}
$$

If a modification causes another branch to drop, it becomes the new weakest link. This is a minimax equalization process among the branches.

---

# 9. Contact Pressure Entropy

After normalizing the equilibrium weights of the three normals of the triangle, we define:

$$
H_\lambda
=
-\frac1{\log3}
\sum_{j=1}^3p_j\log p_j.
$$

The geometric pressure entropy of this container is:

$$
H_\lambda=0.963370649827.
$$

This is the baseline determined by the normal geometry of the container. The curve cannot change the three normals themselves, but it can change:

- Which vertices provide support in each direction;
- Whether the same normal is jointly contacted by multiple points;
- The order of the contact vertices along the curve;
- When each phase branch loses a certain contact;
- The sensitivity of the support extrema to small deformations.

---

# 10. Research Nodes for Round 4

The next round will not immediately increase to $9$ or $11$ segments, but will instead establish:

## Phase Branch Ledger and Sensitivity Updater

For each primary local minimum $\phi_r$, save:

$$
\mathcal B_r
=
(
\phi_r,
s(\phi_r),
I_{\mathrm{left}},
I_{\mathrm{bottom}},
I_{\mathrm{hyp}},
\nabla_\eta s_r
).
$$

where $\eta$ is the curve parameter.

The next round will proceed sequentially to:

1. Identify the lowest few phase branches;
2. Calculate the finite difference sensitivity for each branch;
3. Find a common direction that can simultaneously elevate the lowest branches;
4. Incorporate a branch variance penalty;
5. Directly optimize for branch equalization, rather than simply increasing the number of segments;
6. Check whether the five-segment solution can further approach $1$ under this mechanism.

---

# 11. Limitations

1. The outer-layer curve search remains a floating-point global heuristic;
2. The global optimality of the five-segment or seven-segment families is not proven;
3. Phase refinement is not an interval certificate;
4. No new Moser upper or lower bounds are proposed;
5. No formal proofs have been conducted;
6. The curves are still restricted to polygonal chains;
7. The seven-segment performing worse than the five-segment may be due to the family itself, the parameterization, or insufficient search; a general negation cannot yet be made.

---

# 12. Conclusion

The first version of the reverse generation of contact ledgers yielded a small but genuine positive advancement:

$$
\boxed{
s_5>s_3,
}
$$

but simultaneously revealed a more important limitation:

$$
\boxed{
s_7<s_5.
}
$$

Therefore, the direction of problem-solving cannot be simplified to "increasing curve complexity." The most informative structure at present is:

$$
\boxed{
\text{Low-chiral mirror symmetry}
+
\text{Nearly vertical split flanks}
+
\text{Central horizontal skeleton}
+
\text{Hypotenuse dual-endpoint contact}
+
\text{Left and right internal contacts}
+
\text{Equalization of the lowest phase branches}.
}
$$