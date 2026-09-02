# NS × X Integration × 24/72 Paradigm in Practice
## Round 69 — Pure Continuous Rank-One Scattering Tangent / Affine Endpoint Repair

- Date:  2026-08-18
- Version:  v0.1
- Status:  Proof-Route Experiment / Continuous-Only Rank-One Jost-Scattering Branch
- Previous round:  Round 68 — Central Sign-Cone Reduction
- canonical math delimiters: inline `$...$`; display `$$...$$`

## 0. Round 68 handoff

Round 68 reduced the final viscosity closure to a deliberately coarse central cone:

$$
e_1=u_2,
\qquad
o_2=u_5/\nu.
$$

For the large fibre:

$$
e_1<0,\quad o_2>0
\Longrightarrow
u_3<0.
$$

For the small fibre, the extremely loose cone

$$
e_1\le-0.1,
\qquad
0\le o_2\le100
$$

already forces:

$$
u_3<0.
$$

Thus one merely needs a uniform coarse parameter-control theorem over

$$
0<\nu\le10^{-6}.
$$

Round 69 asks whether the whole tangent really has nine independent degrees of freedom.

It does not.

---

# 1. Repair note — the actual endpoint plane is affine-coupled

Rounds 61–62 used a convenient diagnostic proxy at $\nu=0$:

$$
E_{\rm even}^{\min}
\oplus
E_{\rm odd}^{\rm bd}.
$$

That proxy omitted one piece:

the even minimal mode forces a bounded **odd particular response** through the $\nu=0$ odd equation.

Therefore the true selected endpoint plane is not block-diagonal in the raw parity state.

This does **not** invalidate:

- Round 59 endpoint Jost theorem;
- Round 56 positive-tail theorem;
- Round 61/62 algebraic factorization and exponent balances;
- Round 64–68 validated viscosity/Fredholm results.

But the old Round 61/62 **principal-angle numerical constants** should be regarded as proxy diagnostics and are superseded by the corrected affine-Jost diagnostics of Round 69.

Name:

$$
\boxed{
\textbf{Affine Endpoint Repair}.
}
$$

---

# 2. True endpoint plane at $j=1$

Use the parity state:

$$
S_1
=
(
e_2,e_1,e_0,o_2,o_1,o_0)^T.
$$

Round 59 provides the even minimal sequence:

$$
e_0=1,
$$

and the bounded odd affine graph:

$$
o_2
=
P_0o_1
+
Q_0o_0
+
G_0.
$$

The selected even-driven particular column is:

$$
v_{\rm p}
=
(
e_2,e_1,1,o_2,o_1,0)^T.
$$

The two homogeneous bounded odd columns may be chosen as:

$$
v_{\rm h,0}
=
(
0,0,0,Q_0,0,1)^T,
$$

$$
v_{\rm h,1}
=
(
0,0,0,P_0,1,0)^T.
$$

Therefore the actual endpoint plane is:

$$
\boxed{
E_0^{\rm Jost}
=
\operatorname{span}
\{
v_{\rm p},
v_{\rm h,0},
v_{\rm h,1}
\}.
}
\tag{2.1}
$$

---

# 3. Central affine endpoint shear

The large chart distortion in raw parity coordinates comes mainly from the even-driven odd particular response.

At $j=1$ define:

$$
\boxed{
\widetilde o_2
=
o_2-o_{2,\rm p}e_0,
}
\tag{3.1}
$$

and:

$$
\boxed{
\widetilde o_1
=
o_1-o_{1,\rm p}e_0.
}
\tag{3.2}
$$

This is a fixed linear shear determined entirely by the rigorous endpoint Jost data.

In the sheared chart use:

### base

$$
\boxed{
(e_0,\widetilde o_2,o_0),
}
\tag{3.3}
$$

### output

$$
\boxed{
(e_2,e_1,\widetilde o_1).
}
\tag{3.4}
$$

The endpoint chart condition numbers are:

$$
\boxed{
\kappa_-
\approx1.44713,
}
\tag{3.5}
$$

$$
\boxed{
\kappa_+
\approx1.57880.
}
\tag{3.6}
$$

Thus the corrected full affine-Jost plane is extremely well conditioned in this chart.

---

# 4. Exact parity-rescaled local parameter structure

The parity-rescaled positive-viscosity state is:

$$
S_j
=
(
e_{j+1},e_j,e_{j-1},o_{j+1},o_j,o_{j-1})^T.
$$

Its exact transfer has only one viscosity-dependent entry:

$$
\boxed{
(T_j)_{1,5}
=
\nu^2
\frac{
b_{2j}
}{
A_4^{(2j)}
}.
}
\tag{4.1}
$$

All other entries are independent of $\nu$.

Therefore:

$$
\boxed{
T_j(\nu)
=
T_j(0)
+
\nu^2E_j.
}
\tag{4.2}
$$

In particular:

$$
\boxed{
\partial_\nu T_j(0)=0.
}
\tag{4.3}
$$

This is the fundamental reason the local fast dynamics cannot generate an independent first-order $\nu$ tangent.

---

# 5. Finite-cutoff Rank-One Tangent Theorem

Fix a finite Floquet cutoff $J$.

At $\nu=0$, the two fast minimal branches are isolated from the neutral pair.

Since the local transfer depends analytically on

$$
\mu=\nu^2,
$$

finite-dimensional analytic perturbation gives fast columns:

$$
F_{1,2}(\nu)
=
F_{1,2}(0)
+
O(\nu^2).
$$

The slow minimal branch arises from the neutral two-dimensional degeneracy and may have:

$$
L(\nu)
=
L(0)
+
\nu L_1
+
O(\nu^2).
$$

Thus one may choose a stable-plane basis:

$$
\mathcal V(\nu)
=
[
F_1(\nu),
F_2(\nu),
L(\nu)
]
$$

with:

$$
\boxed{
\mathcal V(\nu)
=
\mathcal V_0
+
\nu w e_3^T
+
O(\nu^2).
}
\tag{5.1}
$$

Every finite backward transfer from $J$ to the center also depends only on $\nu^2$.

Hence (5.1) persists at the central plane.

Now split the basis into graph base/output blocks:

$$
B(\nu)
=
B_0
+
\nu b e_3^T
+
O(\nu^2),
$$

$$
O(\nu)
=
O_0
+
\nu o e_3^T
+
O(\nu^2).
$$

The graph is:

$$
R(\nu)
=
O(\nu)B(\nu)^{-1}.
$$

Differentiating at $\nu=0$ gives:

$$
\boxed{
R'(0)
=
(
o-R_0b
)
e_3^T
B_0^{-1}.
}
\tag{5.2}
$$

The right side is an outer product.

Therefore:

$$
\boxed{
\operatorname{rank}
R'(0)
\le1.
}
\tag{5.3}
$$

Name:

$$
\boxed{
\textbf{Finite-Cutoff Rank-One Scattering Tangent Theorem}.
}
$$

This statement is exact for every fixed finite cutoff.

---

# 6. Meaning of the theorem

The first-order endpoint motion of the admissible three-plane has only one degree of freedom:

$$
\boxed{
\text{slow neutral/Jost scattering}.
}
$$

The two fast directions cannot rotate independently at order $\nu$ because their local dynamics sees only:

$$
\mu=\nu^2.
$$

Thus the nine-entry Grassmann tangent is structurally over-parameterized.

At first order:

$$
\boxed{
\text{one scalar scattering amplitude}
}
$$

controls the whole plane rotation.

---

# 7. Corrected affine-Jost diagnostics

Using the true affine endpoint plane and the endpoint shear, let:

$$
R_\nu
$$

be the positive-viscosity central graph and:

$$
R_0
$$

the corrected endpoint graph.

The attached verifier computes the singular values of:

$$
R_\nu-R_0.
$$

### Small fibre

The hierarchy is:

$$
\boxed{
\begin{aligned}
\sigma_1
&\sim
125.1\,\nu,
\\
\sigma_2
&\sim
76.7\,\nu^2,
\\
\sigma_3
&\sim
0.033\,\nu^2.
\end{aligned}
}
\tag{7.1}
$$

over the well-resolved microscopic range.

### Large fibre

Likewise:

$$
\boxed{
\begin{aligned}
\sigma_1
&\sim
15.7\,\nu,
\\
\sigma_2
&\sim
86.4\,\nu^2,
\\
\sigma_3
&\sim
1.64\,\nu^2.
\end{aligned}
}
\tag{7.2}
$$

Thus:

$$
\boxed{
R_\nu
=
R_0
+
\nu\,u v^T
+
O(\nu^2)
}
\tag{7.3}
$$

is exactly the hierarchy seen by the corrected full endpoint plane.

These singular-value constants are coordinate-dependent diagnostics; the rank hierarchy is the important invariant content.

---

# 8. Intrinsic principal-angle picture

Using the corrected affine endpoint plane directly, the Grassmannian principal-angle diagnostic shows that only one angle is visible at order $\nu$.

At $\nu=10^{-7}$, the leading intrinsic slopes are approximately:

$$
\boxed{
\theta_{1,-}/\nu
\approx6.05,
}
\tag{8.1}
$$

and:

$$
\boxed{
\theta_{1,+}/\nu
\approx1.48.
}
\tag{8.2}
$$

The other two angles are already below ordinary double resolution at this scale.

So the rank-one hierarchy is not an artifact of the endpoint shear.

---

# 9. Deep-tail tangent sensitivity theorem

Round 56 controls the original adjoint tail after solving each row for $u_{n+1}$.

Write the tail fixed-point equation as:

$$
\boxed{
y
=
K_t y
+
S_t x,
}
\tag{9.1}
$$

where:

$$
t=\log\nu.
$$

Because every solved-row coefficient contains the denominator:

$$
\nu b_n,
$$

both operators scale exactly as:

$$
K_t=e^{-t}K_\ast,
$$

$$
S_t=e^{-t}S_\ast.
$$

Suppose:

$$
\boxed{
\|K_t\|\le q<1,
}
\tag{9.2}
$$

and the total boundary row norm is also bounded by $q$.

Then the tail graph:

$$
y=G_tx
$$

obeys:

$$
\boxed{
\|G_t\|
\le
\frac{
q
}{
1-q
}.
}
\tag{9.3}
$$

Differentiate:

$$
(I-K_t)G_t=S_t.
$$

Since:

$$
\partial_tK_t=-K_t,
$$

and:

$$
\partial_tS_t=-S_t,
$$

we obtain:

$$
\boxed{
(I-K_t)\partial_tG_t
=
-G_t.
}
\tag{9.4}
$$

Therefore:

$$
\boxed{
\|\partial_tG_t\|
\le
\frac{
q
}{
(1-q)^2
}.
}
\tag{9.5}
$$

A second differentiation gives:

$$
\boxed{
\|\partial_t^2G_t\|
\le
\frac{
q(1+q)
}{
(1-q)^3
}.
}
\tag{9.6}
$$

Name:

$$
\boxed{
\textbf{Deep-Tail Jet Theorem}.
}
$$

---

# 10. Uniform terminal jet balls

Because Round 56 proves $q_n$ decreases sufficiently far out, for every positive $\nu$ we may choose a cutoff $J(\nu)$ satisfying:

$$
q_{J(\nu)}
\le
\frac14.
$$

Then:

$$
\boxed{
\|G_J\|
\le
\frac13,
}
\tag{10.1}
$$

$$
\boxed{
\|\partial_tG_J\|
\le
\frac49,
}
\tag{10.2}
$$

and:

$$
\boxed{
\|\partial_t^2G_J\|
<
0.741.
}
\tag{10.3}
$$

These bounds are independent of how small viscosity becomes.

Thus infinity itself is no longer the source of any tangent blow-up.

---

# 11. What remains after Round 69

The final coarse cone of Round 68 needs only:

$$
|e_1'|<10^5,
$$

$$
|o_2'|<10^6.
$$

Round 69 shows that the first-order Grassmann motion has only one slow degree of freedom.

Therefore a much smaller sufficient theorem is now available:

> Bound one scalar Jost-scattering amplitude and its propagation from the uniformly bounded deep-tail jet ball to the central affine-Jost chart.

The fast directions contribute only:

$$
O(\nu)
$$

to the derivative after their $O(\nu^2)$ plane displacement is differentiated.

Hence they are harmless relative to the enormous Round 68 cone margins.

---

# 12. Scalar scattering amplitude formulation

Let the first-order graph tangent be written:

$$
\boxed{
R'(0)
=
\alpha_{\rm sc}
\,
u_{\rm sc}
v_{\rm sc}^T.
}
\tag{12.1}
$$

Here:

- $u_{\rm sc}$ is the propagated slow response direction;
- $v_{\rm sc}$ is the endpoint slow-coordinate covector;
- $\alpha_{\rm sc}$ is a single scalar scattering amplitude.

The remaining bridge can therefore be reformulated as:

$$
\boxed{
|\alpha_{\rm sc}|
<
C_{\rm absurdly\ large}
}
\tag{12.2}
$$

with a constant large enough to imply the Round 68 central derivative cone.

The numerical chart slopes are only order:

$$
10^2
$$

or smaller.

The allowed derivative cones are order:

$$
10^5
\text{--}
10^6.
$$

So there remain several orders of magnitude of proof slack even after the full endpoint repair.

---

# 13. STOP-C73 — Scalar Scattering-Amplitude / Uniform Jost-Passage Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{endpoint\text{-}aligned\ parity\ Grassmann\ tangent},
\\
\text{Round 61/62 endpoint proxy}
&=
\mathrm{repaired},
\\
\text{true endpoint plane}
&=
\mathrm{even\ minimal}
+
\mathrm{forced\ odd\ particular}
+
\mathrm{odd\ bounded\ homogeneous},
\\
\text{endpoint chart condition}
&\approx
1.447,\ 1.579,
\\
T_j(\nu)
&=
T_j(0)+\nu^2E_j,
\\
\text{finite-cutoff first tangent rank}
&\le1,
\\
\sigma_1(R_\nu-R_0)
&=
O(\nu),
\\
\sigma_{2,3}(R_\nu-R_0)
&=
O(\nu^2),
\\
\text{deep-tail log-tangent}
&\le
q/(1-q)^2,
\\
\text{deep-tail second jet}
&\le
q(1+q)/(1-q)^3,
\\
\text{uniform terminal jet at }q\le1/4
&=
O(1),
\\
\text{remaining first-order freedom}
&=
1\text{ scalar scattering amplitude},
\\
\text{remaining theorem}
&=
\mathrm{uniform\ infinite\text{-}Jost\ passage/bound\ for\ that\ scalar},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Name:

$$
\boxed{
\textbf{STOP-C73:
Scalar Scattering-Amplitude / Uniform Jost-Passage Gap}.
}
$$

---

# 14. 24/72 Ledger — Round 69

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C1085 | actual affine endpoint plane | $\mathsf C$ | Jost/Floquet geometry | relational | $\mathsf F$ | REPAIRED |
| C1086 | Round61/62 diagnostic proxy audit | $\mathsf C$ | checkpoint integrity | targeted | $\mathsf F$ | SUPERSEDED numerically |
| C1087 | endpoint particular-response shear | $\mathsf C$ | Grassmann chart | relational | $\mathsf F$ | EXACT |
| C1088 | endpoint chart conditioning | $\mathsf C$ | numerical geometry | scalar | $\mathsf F$ | VERIFIED |
| C1089 | parity transfer $\mu=\nu^2$ law | $\mathsf C$ | local transfer | matrix | $\mathsf F$ | EXACT |
| C1090 | fast first derivative vanishing | $\mathsf C$ | isolated fast branches | relational | $\mathsf F$ | FINITE-CUTOFF THEOREM |
| C1091 | rank-one graph derivative formula | $\mathsf C$ | Grassmann calculus | matrix | $\mathsf F$ | EXACT |
| C1092 | corrected singular-value hierarchy | $\mathsf C$ | affine-Jost graph | profile | $\mathsf F$ | VERIFIED |
| C1093 | intrinsic one-angle diagnostic | $\mathsf C$ | principal angles | scalar | $\mathsf F$ | VERIFIED |
| C1094 | deep-tail first jet | $\mathsf C$ | contraction sensitivity | scalar | $\mathsf F$ | PROVED |
| C1095 | deep-tail second jet | $\mathsf C$ | contraction sensitivity | scalar | $\mathsf F$ | PROVED |
| C1096 | uniform terminal jet ball | $\mathsf C$ | moving cutoff | targeted | $\mathsf F$ | PROVED conditional on $q_J\le1/4$ |
| C1097 | scalar scattering-amplitude reduction | $\mathsf C$ | final bridge dimension | scalar | $\mathsf F$ | STRUCTURALLY REDUCED |
| C1098 | uniform infinite-Jost scalar bound | $\mathsf C$ | final viscosity closure | targeted | $\mathsf F$ | OPEN / STOP-C73 |

---

# 15. Continuous-versus-discrete status

The affine endpoint repair and rank-one tangent live in the Grassmannian of admissible subspaces of the continuous periodic Floquet operator.

The finite sideband index is still only a representation coordinate.

The remaining theorem is a continuous viscosity bound on one scattering amplitude.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 16. Next round — Scalar Jost Scattering Flow / Final Coarse Cone

Round 69 has reduced the first-order bridge to one scalar degree of freedom.

Concrete targets:

1. extract the endpoint slow covector $v_{\rm sc}$ from the corrected affine Jost plane;
2. extract the slow response direction $u_{\rm sc}$ from the central shear chart;
3. project the Riccati tangent equation onto that rank-one channel;
4. derive a scalar nonautonomous recurrence for $\alpha_{\rm sc}$;
5. use the Deep-Tail Jet Theorem for a uniform terminal interval;
6. propagate only the scalar interval inward;
7. bound its contribution to
   $$
   e_1',
   \qquad
   o_2';
   $$
8. exploit the extremely loose Round 68 requirements:
   $$
   |e_1'|<10^5,
   $$
   $$
   |o_2'|<10^6;
   $$
9. conclude the central sign cones are invariant for:
   $$
   0<\nu\le10^{-6};
   $$
10. if successful, combine with Round 65 and remove viscosity from the two $\sqrt{17}$ hidden-rescue circles entirely.

This becomes:

$$
\boxed{
\textbf{Scalar Jost Scattering Flow / Final Coarse Cone}.
}
$$

---

# 17. External primary-source anchors

Fresh primary-source check:

1. Pierre Del Moral, Emma Horton, *A note on Riccati matrix difference equations*, arXiv:2107.12918.
   - provides time-varying Riccati semigroup/Floquet-type representations and uniform Riccati-map bounds;
   - relevant framework for the fixed-size tangent and scalar projection.

2. F. Battelli, M. Franca, K. J. Palmer, *Exponential Dichotomy for Noninvertible Linear Difference Equations*, arXiv:2111.04553.
   - proves roughness/persistence results for finite-dimensional difference-equation dichotomies;
   - relevant framework for stable-subspace persistence under the parameter perturbation.

3. Yuri Latushkin, Shibi Vasudevan, *Fredholm determinants, continued fractions, Jost and Evans functions for a Jacobi matrix associated with the 2D-Euler equations*, arXiv:2401.14037.
   - gives a directly adjacent hydrodynamic precedent for Jost/Evans/Fredholm/continued-fraction equivalence.

These are framework anchors only. The affine endpoint repair, rank-one tangent formula, tail-jet bounds and NS-specific diagnostics above are direct results of this series.