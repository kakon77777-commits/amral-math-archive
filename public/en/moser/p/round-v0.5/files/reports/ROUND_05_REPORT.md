# Semi-Autonomous Research on the Moser Skew Field: Round 5

## — Contact Event Equations, Nonsmooth KKT Systems, and Isolated 5-Link Candidates

**Date:** July 26, 2026  
**Status:** Numerical structure reconstruction; Informal proof; Non-interval certificate  
**Continuation of:** Moser Skew Lab v0.4  
**Curve Family:** Mirror-symmetric 5-link

---

# 1. Transitioning from Black-Box Branch Tracking to Event Equations

The directions and lengths of the mirror-symmetric 5-link are:

$$
(\alpha,\beta,0,-\beta,-\alpha),
$$

$$
(l_1,l_2,l_3,l_2,l_1),
$$

where:

$$
\alpha=\beta+\delta,
\qquad
l_3=1-2(l_1+l_2).
$$

Let the vertices of the unrotated curve be:

$$
q_0,\ldots,q_5.
$$

Define:

$$
q_2=l_1v_\alpha+l_2v_\beta,
$$

$$
q_3=q_2+l_3(1,0),
$$

and the horizontal span of the endpoints:

$$
D
=
2l_1\cos\alpha
+
2l_2\cos\beta
+
l_3.
$$

From the active vertex identities observed in Round 4, the phases of the four controlling branches can be written out directly, no longer relying on black-box local minimizer tracking.

---

# 2. Four Exact Contact Events

## 2.1 First Branch

Vertices $q_0,q_1$ simultaneously contact the left boundary, hence:

$$
\phi_1=\frac\pi2-\alpha.
$$

## 2.2 Second Branch

Vertices $q_1,q_2$ simultaneously contact the left boundary, hence:

$$
\phi_2=\frac\pi2-\beta.
$$

## 2.3 Third Branch

Both endpoints simultaneously contact the hypotenuse. From the Wetzel triangle:

$$
\frac BA=\sqrt3,
$$

we obtain the exact phase:

$$
\phi_3=\frac{2\pi}{3}.
$$

## 2.4 Fourth Branch

Both endpoints simultaneously contact the left boundary, yielding:

$$
\phi_4=\frac{3\pi}{2}.
$$

The numerical phases are:

$$
(\phi_1,\phi_2,\phi_3,\phi_4)
=
(
0.114929000958,
0.162519595932,
2.094395102393,
4.712388980385
).
$$

The angles are:

$$
(
6.584946699^\circ,
9.311686935^\circ,
120^\circ,
270^\circ
).
$$

---

# 3. Event Scale Functions

Define the hypotenuse support functional after rotation:

$$
H_\phi(x,y)
=
\frac{x\cos\phi-y\sin\phi}{A}
+
\frac{x\sin\phi+y\cos\phi}{B}.
$$

The four branch scales can be written as:

$$
m_1=H_{\phi_1}(q_3),
$$

$$
m_2
=
H_{\phi_2}(q_3)
-
\frac{x_{\phi_2}(q_1)}A,
$$

$$
m_3
=
-\frac{x_{\phi_3}(q_3)}A
-
\frac{y_{\phi_3}(q_2)}B,
$$

$$
m_4
=
\frac{y_2}{A}
+
\frac{D-x_2}{B}.
$$

These four functions depend only on:

$$
p=(l_1,l_2,\beta,\delta).
$$

---

# 4. Nine-Equation Event-KKT System

Merely requiring:

$$
m_1=m_2=m_3=m_4
$$

provides three independent equations, thus generally forming a one-dimensional candidate family, which cannot uniquely determine the curve.

Adding the second-level branch pressures of the minimax:

$$
\mu_r\ge0,
\qquad
\sum_{r=1}^4\mu_r=1,
$$

and the stationarity condition:

$$
\sum_{r=1}^4
\mu_r\nabla_p m_r
=
0,
$$

we obtain:

$$
\boxed{
m_r(p)-s=0
\quad(r=1,\ldots,4)
}
$$

$$
\boxed{
\sum_r\mu_r-1=0
}
$$

$$
\boxed{
\sum_r\mu_r\nabla_p m_r=0
}.
$$

The unknowns are:

$$
(l_1,l_2,\beta,\delta,s,\mu_1,\ldots,\mu_4),
$$

totaling $9$; there are also $9$ equations.

---

# 5. Event System Solution

The numerical solution is:

$$
\boxed{
l_1=0.194313116153072,
\quad
l_2=0.141593079119592,
\quad
l_3=0.328187609454671
},
$$

$$
\boxed{
\beta=80.688313064938^\circ,
\quad
\delta=2.726740236531^\circ,
\quad
\alpha=83.415053301469^\circ
}.
$$

Common scale:

$$
\boxed{
s_{\mathrm{event}}
=
0.998903757132509
}.
$$

The difference among the four analytical event scales is:

$$
\max_r m_r-\min_r m_r
=
2.220446049250e-16.
$$

Compared to the complete nonsmooth audit value from Round 4, the improvement is:

$$
s_{\mathrm{event}}-s_5^{(4)}
=
6.656150519646e-09.
$$

Distance to the certified scale:

$$
1-s_{\mathrm{event}}
=
1.096242867491e-03.
$$

This improvement is only about $10^{-9}$; its significance is not a substantial increase in the Moser lower bound, but rather projecting the black-box level points from Round 4 onto the stationary solution of the exact event equations.

---

# 6. Branch Pressure Ledger

| Branch | Pressure |
|---|---:|
| B1 | 0.027979394124 |
| B2 | 0.028750082793 |
| B3 | 0.736540138466 |
| B4 | 0.206730384616 |

where the third branch still bears the primary pressure, followed by the fourth branch.

Event equation residual norm:

$$
\|F\|
=
2.777480200316e-16.
$$

---

# 7. Branch Gradients

| Branch | $\partial_{l_1}$ | $\partial_{l_2}$ | $\partial_\beta$ | $\partial_\delta$ |
|---|---:|---:|---:|---:|
| B1 | -2.808858450 | -2.723385298 | -0.274339827 | -0.023773699 |
| B2 | -2.885212398 | -2.884021564 | -0.243891703 | -0.009722549 |
| B3 | 0.267943760 | 0.254102052 | 0.095066488 | 0.046873361 |
| B4 | -0.173226017 | -0.135644459 | -0.267655455 | -0.162430955 |

After pressure weighting:

$$
\sum_r\mu_r\nabla m_r
=
0
$$

holds within numerical precision.

---

# 8. Contact Identity Verification

| Branch | Phase | Angle | Left Boundary | Bottom Boundary | Hypotenuse |
|---|---:|---:|---|---|---|
| B1 | 0.114929001 | 6.584947 | [0, 1] | [0] | [3] |
| B2 | 0.162519596 | 9.311687 | [1, 2] | [0] | [3] |
| B3 | 2.094395102 | 120.000000 | [3] | [2] | [0, 5] |
| B4 | 4.712388980 | 270.000000 | [0, 5] | [5] | [2] |

The active identities of the four events are consistent with the observations from Round 4, indicating that the event equations are not incorrectly connected to another topological branch.

---

# 9. Nonsmooth Local Minimum Check

| Branch | Left Directional Derivative | Right Directional Derivative |
|---|---:|---:|
| B1 | -0.330210281 | 0.023773716 |
| B2 | -0.023773716 | 0.234169151 |
| B3 | -0.267655431 | 0.612833351 |
| B4 | -0.330210281 | 0.432315428 |

All branches satisfy:

$$
D_-s(\phi_r)<0<D_+s(\phi_r).
$$

Therefore, all four events are cusp local minima formed by active vertex switching, rather than ordinary smooth stationary points.

This also explains why the black-box one-dimensional minimizer in Round 4 produced a cusp deviation of about $10^{-8}$.

---

# 10. Isolation Diagnostics

Full Event-KKT Jacobian size:

$$
9\times9.
$$

Numerical rank:

$$
\operatorname{rank}J
=
9.
$$

Minimum singular value:

$$
\sigma_{\min}
=
3.607219048175e-02.
$$

Condition number:

$$
\kappa(J)
=
162.781733366.
$$

Thus, at the numerical linearization level, the Event-KKT solution is not an unresolved manifold, but an isolated intersection point.

Furthermore, randomly perturbing $40$ initial values nearby:

- Successfully returned to the same root: 40;
- Maximum solution distance: 8.312345999721e-15.

This does not constitute an analytical uniqueness proof, but strongly supports:

$$
\boxed{
\text{The current candidate is a numerically isolated stationary point within this fixed contact topology.}
}
$$

---

# 11. Complete Phase Audit

Scanned the complete period using $262144$ phase points.

Grid minimum value:

$$
0.998903757132509.
$$

Difference between the event value and the grid minimum value:

$$
0.000000000000e+00.
$$

The grid minimum point is located exactly at:

$$
\phi=\frac{3\pi}{2},
$$

Therefore, the fourth event can be directly hit on the current candidate; the other three cusps require event formulas to avoid phase grid offsets.

---

# 12. Research Verdict

This round completed transitions across three levels:

$$
\boxed{
\text{Black-box phase search}
\longrightarrow
\text{Explicit contact events}
\longrightarrow
\text{Simultaneous Event-KKT system}
}.
$$

The conclusion is not that "the Moser problem is close to being solved," but rather:

1. The 5-link plateau discovered in Rounds 3 and 4 can be described by four exact contact events;
2. The four-event equal-height condition itself forms a one-dimensional family;
3. Adding the branch pressure stationarity condition yields a numerically isolated solution;
4. The black-box search within this contact topology has largely converged;
5. Continuing to fine-tune the same 5-link topology is expected to yield only minimal numerical variations.

---

# 13. Directions for Round 6

The next round will no longer repeatedly fine-tune this isolated point, but will split into two paths.

## 13.1 Out-of-Bounds Search for Contact Topologies

Actively search for identities different from the current four events:

- The hypotenuse is not simultaneously contacted by both endpoints;
- The left and bottom boundaries are simultaneously contacted by multiple vertices;
- The 5-link exhibits a different vertex cyclic order;
- Non-mirror-symmetric curves where both chiral branches are simultaneously difficult;
- Curvature arcs replacing nearly parallel sub-segments.

## 13.2 Local Topology Limit Certificates

Without entering Lean, first establish:

- Active identity neighborhoods;
- Event equation interval boxes;
- Jacobian nonsingular numerical bounds;
- One-sided derivative bounds for branches;
- A computational certificate draft for the local non-existence of higher solutions.

The first path seeks a breakthrough; the second path confirms that the current plateau is not a solver hallucination.

---

# 14. Limitations

1. Equations are solved using double-precision floating-point;
2. The Jacobian rank and singular values are numerical diagnostics;
3. Perturbation returning to the root does not equate to analytical uniqueness;
4. Interval Newton or Krawczyk certificates have not yet been established;
5. It is not proven that this 5-link topology is optimal for all 5-links;
6. No new Moser upper or lower bounds have been proposed;
7. No formalized proofs have been conducted.

---

# 15. Conclusion

Round 5 obtained:

$$
\boxed{
s_{\mathrm{event}}
=
0.998903757132509
}.
$$

But the true achievement is not the improvement after the decimal point, but completely writing out the generative causes of the candidate:

$$
\boxed{
\text{Four cusp contact events at equal height}
+
\text{Four-branch pressure stationarity}
=
\text{Numerically isolated 5-link candidate}.
}
$$

This indicates that the current 5-link contact skeleton has been elevated from an exploratory graphic to a solvable, differentiable, and perturbation-verifiable low-dimensional event system.