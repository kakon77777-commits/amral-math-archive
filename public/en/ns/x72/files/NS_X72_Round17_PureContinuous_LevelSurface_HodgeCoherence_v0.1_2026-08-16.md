# NS × X Integral × 24/72 Paradigm Practice
## Round 17 — Pure Continuous Level-Surface Flux / Hodge-Coherence Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Level-Surface Geometry Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round16_PureContinuous_LayerCake_SuperlevelDistortion_v0.1_2026-08-16.md`
- Objective of this round: Dissect the level-surface boundary flux of Round 16
  $$
  \mathcal B_Q(\lambda)
  $$
  , decompose it into incidence angle, direction turning, surface geometry, and optimal gauge slope using the nonlinear critical gauge
  $$
  \operatorname{div}(r^2n)=0
  $$
  ; and verify whether the boundary flux is a truly independent obstruction, or if it can be reabsorbed into the nonlinear-Hodge bulk geometry.
- Non-assertion: This document does not prove that the critical weighted physical-gradient budget is necessarily finite. After partially resolving the boundary-flux obstruction from Round 16, this document pushes the remaining problem to a scale-critical weighted physical-gradient / Hodge-coherence frontier.

---

# 0. Round 16 handoff

Let:

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative:

$$
v
=
u+\nabla q,
$$

and:

$$
r=|v|,
\qquad
n=\frac v{|v|}
$$

in:

$$
r>0.
$$

nonlinear gauge:

$$
\boxed{
\operatorname{div}(r^2n)=0.
}
\tag{0.1}
$$

Round 16 defines:

$$
E_\lambda
=
\{r>\lambda\}
$$

and the regular level surface:

$$
\Sigma_\lambda
=
\{r=\lambda\}.
$$

global nonlinear-Hodge orthogonality localized to:

$$
E_\lambda
$$

yields:

$$
\boxed{
E_M^u(\lambda)
=
D_M(\lambda)
+
H_M(\lambda)
-
2\mathcal B_Q(\lambda).
}
\tag{0.2}
$$

where:

$$
\boxed{
\mathcal B_Q(\lambda)
=
\sum_{\ell=1}^3
\int_{\Sigma_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot\eta_\lambda
\,dS,
}
\tag{0.3}
$$

$$
q_\ell=\partial_\ell q,
$$

$$
M_v
=
r(I+n\otimes n),
$$

and:

$$
\eta_\lambda
$$

is the outward unit normal of:

$$
E_\lambda
$$

.

Round 16 STOP:

$$
\boxed{
\text{STOP-C20}
=
\text{Continuous Layer-Distortion / Boundary-Flux Gap}.
}
$$

---

# 1. Level-surface notation

On the regular level:

$$
\Sigma_\lambda,
$$

let:

$$
g
=
|\nabla r|.
$$

Since:

$$
E_\lambda=\{r>\lambda\},
$$

the outward normal points to smaller $r$:

$$
\boxed{
\eta
=
-\frac{\nabla r}{g}.
}
\tag{1.1}
$$

Define the directional incidence:

$$
\boxed{
a
=
n\cdot\eta.
}
\tag{1.2}
$$

and decompose:

$$
\boxed{
n
=
a\eta+n_T,
\qquad
n_T\cdot\eta=0.
}
\tag{1.3}
$$

---

# 2. Gauge incidence relation

From:

$$
\operatorname{div}(r^2n)=0,
$$

we have:

$$
2r\,n\cdot\nabla r
+
r^2\operatorname{div}n
=
0.
$$

At:

$$
r=\lambda,
$$

and:

$$
n\cdot\nabla r
=
-ga,
$$

therefore:

$$
\boxed{
\operatorname{div}n
=
\frac{
2ga
}{
\lambda
}.
}
\tag{2.1}
$$

This is an exact relation between the amplitude-level normal incidence and the direction-field divergence.

---

# 3. Zero net directional incidence

If:

$$
E_\lambda^{(j)}
$$

is a bounded regular connected superlevel component, then by the divergence theorem:

$$
0
=
\int_{E_\lambda^{(j)}}
\operatorname{div}(r^2n)dx
=
\int_{\partial E_\lambda^{(j)}}
r^2
n\cdot\eta\,dS.
$$

On the boundary:

$$
r=\lambda,
$$

thus:

$$
\boxed{
\int_{\partial E_\lambda^{(j)}}
n\cdot\eta\,dS
=
0.
}
\tag{3.1}
$$

Named:

$$
\boxed{
\textbf{Zero Net Incidence Law}.
}
$$

Therefore, the optimal direction field cannot cross the entire closed amplitude surface unidirectionally outward or unidirectionally inward.

The normal incidence must be globally balanced.

---

# 4. Mean-curvature / incidence balance

Let the signed mean-curvature convention be:

$$
\boxed{
\mathcal H_\Sigma
=
\operatorname{div}\eta.
}
\tag{4.1}
$$

Using on the surface:

$$
n=a\eta+n_T.
$$

the ambient divergence decomposition is:

$$
\operatorname{div}n
=
\partial_\eta a
+
\operatorname{div}_\Sigma n_T
+
\mathcal H_\Sigma a.
$$

Comparing with (2.1):

$$
\boxed{
\left(
\frac{2g}{\lambda}
-
\mathcal H_\Sigma
\right)a
=
\partial_\eta a
+
\operatorname{div}_\Sigma n_T.
}
\tag{4.2}
$$

Thus, the level-set curvature, amplitude slope, direction incidence, and tangential directional flux are not independent.

---

# 5. Exact surface decomposition of quotient dissipation density

Round 16 unweighted dissipation density:

$$
A
=
|\nabla v|^2
+
|\nabla r|^2.
$$

From:

$$
v=rn
$$

and:

$$
n\cdot\partial_jn=0,
$$

we have:

$$
\boxed{
|\nabla v|^2
=
|\nabla r|^2
+
r^2|\nabla n|^2.
}
\tag{5.1}
$$

therefore:

$$
\boxed{
A
=
2g^2
+
r^2|\nabla n|^2.
}
\tag{5.2}
$$

Round 16 surface dissipation density:

$$
a_\Sigma(\lambda)
=
-d'(\lambda)
$$

thus:

$$
\boxed{
a_\Sigma(\lambda)
=
\int_{\Sigma_\lambda}
\left[
2g
+
\frac{
\lambda^2|\nabla n|^2
}{
g
}
\right]dS.
}
\tag{5.3}
$$

This exact decomposition states that:

the surface dissipation pays for two costs:

1. amplitude steepness:
   $$
   g;
   $$
2. directional turning:
   $$
   |\nabla n|.
   $$

---

# 6. Incidence-angle dissipation tax

From:

$$
|\operatorname{div}n|^2
\le
3|\nabla n|^2,
$$

and (2.1):

$$
\frac{
\lambda^2|\nabla n|^2
}{
g
}
\ge
\frac{
4
}{
3
}
g a^2.
$$

thus:

$$
\boxed{
a_\Sigma(\lambda)
\ge
\int_{\Sigma_\lambda}
g
\left(
2+\frac43a^2
\right)dS.
}
\tag{6.1}
$$

Named:

$$
\boxed{
\textbf{Incidence-Angle Dissipation Tax}.
}
$$

Therefore, when the direction field crosses the amplitude surface with a stronger normal angle, the surface dissipation must increase.

---

# 7. Area–distribution dissipation inequality

Let:

$$
S(\lambda)
=
\operatorname{Area}(\Sigma_\lambda),
$$

and:

$$
-V'(\lambda)
=
\int_{\Sigma_\lambda}
\frac1g\,dS.
$$

By Cauchy–Schwarz:

$$
S(\lambda)^2
\le
\left(
\int_{\Sigma_\lambda}g\,dS
\right)
\left(
-V'(\lambda)
\right).
$$

From (5.3):

$$
a_\Sigma
\ge
2\int_\Sigma g.
$$

Thus:

$$
\boxed{
a_\Sigma(\lambda)
\left(
-V'(\lambda)
\right)
\ge
2S(\lambda)^2.
}
\tag{7.1}
$$

Then by the 3D isoperimetric inequality:

$$
S(\lambda)
\ge
C_{\rm iso}
V(\lambda)^{2/3},
$$

we obtain:

$$
\boxed{
a_\Sigma(\lambda)
\left(
-V'(\lambda)
\right)
\ge
c_{\rm iso}
V(\lambda)^{4/3}.
}
\tag{7.2}
$$

Therefore, if the superlevel volume does not decay rapidly along the amplitude axis, the surface dissipation must pay an area cost.

---

# 8. Exact boundary-flux factorization

From:

$$
\partial_\ell v
=
(\partial_\ell r)n
+
r\partial_\ell n,
$$

and:

$$
M_v
=
r(I+n\otimes n),
$$

we obtain:

$$
\boxed{
M_v\partial_\ell v
=
2r
(\partial_\ell r)n
+
r^2\partial_\ell n.
}
\tag{8.1}
$$

Substituting into the boundary flux.

At:

$$
r=\lambda,
$$

simplified via (2.1):

$$
\boxed{
\begin{aligned}
\mathcal B_Q(\lambda)
={}&
\lambda^2
\int_{\Sigma_\lambda}
\left[
((\nabla q\cdot\nabla)n)\cdot\eta
-
(\operatorname{div}n)
(\nabla q\cdot\eta)
\right]dS.
\end{aligned}
}
\tag{8.2}
$$

Equivalent tensor form:

$$
\boxed{
\mathcal B_Q(\lambda)
=
\lambda^2
\int_{\Sigma_\lambda}
\eta\cdot
\left[
\nabla n
-
(\operatorname{div}n)I
\right]
\nabla q
\,dS.
}
\tag{8.3}
$$

This is the first core boundary-flux identity of this round.

---

# 9. Meaning of the boundary-flux identity

(8.2) shows that:

$$
\mathcal B_Q
$$

is not an arbitrary boundary artifact.

It must simultaneously utilize:

- direction-field gradient:
  $$
  \nabla n;
  $$
- normal incidence/divergence;
- optimal gauge slope:
  $$
  \nabla q;
  $$
- level-surface normal:
  $$
  \eta.
  $$

A large surface area or large amplitude alone is insufficient to generate a large boundary flux.

---

# 10. Surface gauge-slope bound

Define:

$$
\boxed{
P_q(\lambda)
=
\int_{\Sigma_\lambda}
g
|\nabla q|^2dS.
}
\tag{10.1}
$$

From:

$$
|\operatorname{div}n|
\le
\sqrt3|\nabla n|
$$

and (8.2):

$$
|\mathcal B_Q|
\le
C
\lambda^2
\int_\Sigma
|\nabla n|
|\nabla q|\,dS.
$$

Using weights:

$$
g^{-1},
\qquad
g
$$

applying Cauchy:

$$
|\mathcal B_Q|
\le
C
\lambda^2
\left(
\int_\Sigma
\frac{
|\nabla n|^2
}{
g
}dS
\right)^{1/2}
P_q(\lambda)^{1/2}.
$$

From (5.3):

$$
\boxed{
|\mathcal B_Q(\lambda)|
\le
C
\lambda
a_\Sigma(\lambda)^{1/2}
P_q(\lambda)^{1/2}.
}
\tag{10.2}
$$

Therefore, a large pointwise boundary flux requires:

$$
\boxed{
\text{directional surface dissipation}
\times
\text{optimal gauge slope}
}
$$

to increase together.

---

# 11. Boundary flux is also a bulk Hodge cross term

From:

$$
\operatorname{div}
(M_v\partial_\ell v)=0
$$

and the divergence theorem:

$$
\boxed{
\mathcal B_Q(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\partial_\ell v\,dx.
}
\tag{11.1}
$$

Therefore, the boundary flux is simultaneously a bulk nonlinear-Hodge coherence.

Define:

$$
D_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\partial_\ell v
\cdot
M_v
\partial_\ell v\,dx,
$$

$$
H_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\nabla q_\ell\,dx.
$$

Then:

$$
\boxed{
|\mathcal B_Q(\lambda)|
\le
\sqrt{
D_M(\lambda)H_M(\lambda)
}.
}
\tag{11.2}
$$

Thus, the magnitude of the boundary flux is not an additional unbounded trace variable.

It is controlled by the bulk quotient/gauge energies.

---

# 12. Level Hodge-coherence coefficient

If:

$$
D_MH_M>0,
$$

Define:

$$
\boxed{
\rho_M(\lambda)
=
\frac{
\mathcal B_Q(\lambda)
}{
\sqrt{
D_M(\lambda)H_M(\lambda)
}
}.
}
\tag{12.1}
$$

Then:

$$
\boxed{
-1\le\rho_M\le1.
}
$$

The local Pythagorean:

$$
E_M^u
=
D_M+H_M-2\mathcal B_Q
$$

can be written as:

$$
\boxed{
\frac{
E_M^u
}{
D_M
}
=
1+R_M
-
2\rho_M\sqrt{R_M},
}
\tag{12.2}
$$

where:

$$
\boxed{
R_M
=
\frac{
H_M
}{
D_M
}.
}
\tag{12.3}
$$

Rewriting again:

$$
\boxed{
\frac{
E_M^u
}{
D_M
}
=
\left(
\sqrt{R_M}-1
\right)^2
+
2\sqrt{R_M}
\left(
1-\rho_M
\right).
}
\tag{12.4}
$$

Named:

$$
\boxed{
\textbf{Level Hodge-Coherence Identity}.
}
$$

---

# 13. Consequence of the Hodge-coherence identity

(12.4) indicates that for the localized physical weighted gradient to become small, it must simultaneously satisfy:

1. gauge distortion is close to quotient dissipation:
   $$
   R_M\approx1;
   $$
2. the nonlinear-Hodge cross term is almost perfectly positively aligned:
   $$
   \rho_M\approx1.
   $$

If:

$$
R_M\gg1,
$$

then no matter how the boundary flux is chosen,

$$
\boxed{
E_M^u
\ge
\left(
\sqrt{H_M}-\sqrt{D_M}
\right)^2.
}
\tag{13.1}
$$

Therefore, a very large local gauge distortion cannot be secretly and completely canceled out by the boundary flux.

It must transform into a large physical weighted-gradient tail.

---

# 14. Relation to Round 16 continuous tails

Round 16:

$$
d(\lambda)
=
\int_{E_\lambda}
A\,dx,
$$

$$
h(\lambda)
=
\int_{E_\lambda}
B\,dx.
$$

and:

$$
D_M(\lambda)
=
\int_{E_\lambda}
rA\,dx,
$$

so by layer-cake:

$$
\boxed{
D_M(\lambda)
=
\lambda d(\lambda)
+
\int_\lambda^\infty
d(\mu)d\mu.
}
\tag{14.1}
$$

Similarly:

$$
\boxed{
H_M(\lambda)
=
\lambda h(\lambda)
+
\int_\lambda^\infty
h(\mu)d\mu.
}
\tag{14.2}
$$

Therefore, $R_M(\lambda)$ is not a new discrete scale.

It is a smoothed amplitude-weighted transform of the Round 16 continuous tail profile.

---

# 15. Cumulative boundary-flux identity

Define:

$$
\boxed{
\overline{\mathcal B}_Q(\lambda)
=
\int_\lambda^\infty
\mathcal B_Q(\mu)d\mu.
}
\tag{15.1}
$$

By coarea:

$$
\overline{\mathcal B}_Q(\lambda)
=
-
\sum_\ell
\int_{E_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot\nabla r\,dx.
$$

Using again:

$$
\operatorname{div}
(M_v\partial_\ell v)=0
$$

testing against:

$$
q_\ell(r-\lambda)_+,
$$

we obtain:

$$
\boxed{
\overline{\mathcal B}_Q(\lambda)
=
\sum_\ell
\int_{E_\lambda}
(r-\lambda)
\nabla q_\ell
\cdot
M_v
\partial_\ell v\,dx.
}
\tag{15.2}
$$

Therefore, the cumulative surface flux is completely reintegrated back into the continuous bulk coherence.

---

# 16. Cumulative flux bound

Define:

$$
\overline D_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
(r-\lambda)
\partial_\ell v
\cdot
M_v
\partial_\ell v\,dx,
$$

$$
\overline H_M(\lambda)
=
\sum_\ell
\int_{E_\lambda}
(r-\lambda)
\nabla q_\ell
\cdot
M_v
\nabla q_\ell\,dx.
$$

Then:

$$
\boxed{
|\overline{\mathcal B}_Q(\lambda)|
\le
\sqrt{
\overline D_M(\lambda)
\overline H_M(\lambda)
}.
}
\tag{16.1}
$$

Therefore, if the pointwise surface trace is difficult to estimate,

continuous $\lambda$ integration can reabsorb it into the bulk nonlinear-Hodge metric.

This is a partial repair of the Round 16 boundary-flux obstruction.

---

# 17. Physical weighted-gradient tail

By definition:

$$
E_M^u(\lambda)
=
\sum_\ell
\int_{E_\lambda}
\partial_\ell u
\cdot
M_v
\partial_\ell u\,dx.
$$

Expanding:

$$
\boxed{
E_M^u(\lambda)
=
\int_{E_\lambda}
r
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
\tag{17.1}
$$

Thus:

$$
\boxed{
\int_{E_\lambda}
r|\nabla u|^2dx
\le
E_M^u(\lambda)
\le
2
\int_{E_\lambda}
r|\nabla u|^2dx.
}
\tag{17.2}
$$

Therefore, the localized boundary-flux problem is ultimately pushed toward a physical carrier:

$$
\boxed{
|v|
|\nabla u|^2.
}
$$

---

# 18. Global critical weighted-gradient budget

Let:

$$
\boxed{
E_M(t)
=
E_M^u(0,t)
=
\int_{\mathbb R^3}
r
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
\tag{18.1}
$$

Round 15 global Pythagorean:

$$
\boxed{
E_M
=
D+H.
}
\tag{18.2}
$$

Under NS scaling:

$$
u_\lambda=\lambda u(\lambda x,\lambda^2t),
$$

the optimal quotient representative scales similarly:

$$
v_\lambda=\lambda v(\lambda x,\lambda^2t).
$$

Thus:

$$
E_M
\mapsto
\lambda^2 E_M.
$$

Therefore:

$$
\boxed{
\int
E_M(t)\,dt
}
\tag{18.3}
$$

is a scale-invariant spacetime quantity.

This is a new Pure-C critical budget.

---

# 19. Critical Weighted-Gradient Budget Criterion

Round 15 growth estimate:

$$
|I_Q|
\le
C
Q
H^{1/2}
D^{1/2}.
$$

Since:

$$
E_M=D+H,
$$

by AM–GM:

$$
H^{1/2}D^{1/2}
\le
\frac12E_M.
$$

Therefore:

$$
\boxed{
|I_Q|
\le
C
Q
E_M.
}
\tag{19.1}
$$

And the exact quotient equation:

$$
\frac13
(Q^3)'
+
\nu D
=
I_Q.
$$

that is:

$$
Q^2Q'
+
\nu D
=
I_Q.
$$

If:

$$
Q>0,
$$

then:

$$
Q Q'
\le
C E_M.
$$

Thus:

$$
\boxed{
\frac d{dt}
Q^2
\le
C
E_M(t).
}
\tag{19.2}
$$

Integrating:

$$
\boxed{
Q(T)^2
\le
Q(0)^2
+
C
\int_0^T
E_M(t)dt.
}
\tag{19.3}
$$

Therefore:

$$
\boxed{
\int_0^{T_\ast}
E_M(t)dt
<
\infty
}
\tag{19.4}
$$

is sufficient to keep:

$$
Q(t)
$$

bounded.

From:

$$
Q\simeq\|u\|_3,
$$

and standard endpoint $L^\infty_tL^3_x$ continuation theory,

we obtain conditional regularity.

Named:

$$
\boxed{
\textbf{Critical Weighted-Gradient Budget Criterion}.
}
$$

This document does not claim academic novelty for this formulation; it is a direct consequence of the identities in this route.

---

# 20. Why this is not yet closure

The standard energy inequality provides:

$$
\int
\|\nabla u\|_2^2dt.
$$

But:

$$
E_M
$$

contains an additional critical amplitude weight:

$$
|v|.
$$

Therefore, currently there is no direct way from ordinary energy to obtain:

$$
\boxed{
\int E_Mdt<\infty.
}
$$

Thus:

$$
\boxed{
\text{boundary flux}
}
$$

is no longer the deepest obstruction.

It can be controlled by surface geometry, bulk Hodge coherence, and cumulative integration.

What is truly missing is:

$$
\boxed{
\text{critical weighted physical-gradient budget}.
}
$$

---

# 21. Relation to strain / vorticity geometry

Pointwise:

$$
|\nabla u|^2
=
|S_u|^2
+
\frac12|\omega|^2.
$$

Therefore:

$$
E_M
$$

contains at least the weighted:

$$
\boxed{
|v|
\left(
|S_u|^2
+
\frac12|\omega|^2
\right).
}
$$

The second term:

$$
|(\nabla u)^\top n|^2
$$

further incorporates optimal-direction alignment information.

Therefore, the new frontier of Round 17 reconnects to:

- Round 03 strain/vorticity geometry;
- Round 05 gradient-alignment;
- Round 08 frequency-transfer geometry;

but now they are weighted by a critical quotient amplitude:

$$
|v|
$$

---

# 22. STOP-C21 — Level Hodge-Coherence / Critical Weighted-Gradient Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C21}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ level\text{-}surface\ geometry},
\\
\text{zero\ net\ incidence}
=
\int_{\Sigma_\lambda}
n\cdot\eta
=
0,
\\
\text{surface\ dissipation}
=
2g+\lambda^2|\nabla n|^2/g,
\\
\text{boundary\ flux}
=
\lambda^2
\int
\eta\cdot
[\nabla n-(\operatorname{div}n)I]
\nabla q,
\\
\text{bulk\ coherence}
=
|\mathcal B_Q|
\le
\sqrt{D_MH_M},
\\
\text{localized\ identity}
=
E_M^u
=
D_M+H_M-2\mathcal B_Q,
\\
\text{cumulative\ surface\ flux}
=
\mathrm{resummed\ into\ bulk\ coherence},
\\
\text{new\ critical\ budget}
=
\int E_Mdt,
\\
\text{missing}
=
\mathrm{unconditional\ control\ of\ critical\ weighted\ physical\ gradient},
\\
\text{essential\ discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

Named:

$$
\boxed{
\textbf{STOP-C21:
Level Hodge-Coherence / Critical Weighted-Gradient Gap}.
}
$$

---

# 23. 24/72 Ledger — Round 17

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C197 | level normal / incidence | $\mathsf C$ | surface geometry | relational | $\mathsf F$ | FORM |
| C198 | gauge incidence relation | $\mathsf C$ | constraint | scalar relation | $\mathsf F$ | EXACT |
| C199 | zero net incidence | $\mathsf C$ | global surface | scalar | $\mathsf F$ | PROVED |
| C200 | mean-curvature/incidence balance | $\mathsf C$ | surface differential | $\mathsf X$ | $\mathsf F$ | EXACT |
| C201 | surface dissipation decomposition | $\mathsf C$ | coarea | scalar profile | $\mathsf F$ | EXACT |
| C202 | incidence-angle dissipation tax | $\mathsf C$ | geometry | targeted | $\mathsf F$ | PROVED |
| C203 | area–distribution dissipation | $\mathsf C$ | isoperimetric/coarea | targeted | $\mathsf F$ | PROVED |
| C204 | boundary-flux factorization | $\mathsf C$ | surface geometry | $\mathsf X$ | $\mathsf F$ | EXACT |
| C205 | surface gauge-slope bound | $\mathsf C$ | surface estimate | scalar profile | $\mathsf F$ | PROVED |
| C206 | boundary flux as bulk cross term | $\mathsf C$ | nonlinear Hodge | relational | $\mathsf F$ | EXACT |
| C207 | Hodge coherence coefficient | $\mathsf C$ | recognition | scalar profile | $\mathsf F$ | FORM |
| C208 | level Hodge-coherence identity | $\mathsf C$ | geometric decomposition | targeted | $\mathsf F$ | EXACT |
| C209 | cumulative flux resummation | $\mathsf C$ | continuous $\lambda$ integration | relational | $\mathsf F$ | EXACT |
| C210 | physical weighted-gradient carrier | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | FORM |
| C211 | scale-critical weighted-gradient budget | $\mathsf C$ | spacetime integration | scalar | $\mathsf F$ | CRITICAL |
| C212 | finite weighted-gradient budget $\Rightarrow$ bounded $Q$ | $\mathsf C$ | continuation | targeted | $\mathsf F$ | PROVED |
| C213 | unconditional weighted-gradient budget | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C21 |

---

# 24. Continuous-versus-discrete status

This round even takes:

$$
\mathcal B_Q(\lambda)
$$

first decomposes it into surface geometry, and then uses:

$$
\int_\lambda^\infty
\mathcal B_Q(\mu)d\mu
$$

to reintegrate it back into the bulk continuous coherence.

There are no:

- discrete surface components as necessary indices;
- dyadic thresholds;
- atomic layers;
- shell graphs;
- sequence extractions.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

---

# 25. Strongest results of Round 17

## R17-A — Zero Net Incidence

$$
\boxed{
\int_{\Sigma_\lambda}
n\cdot\eta\,dS=0.
}
$$

## R17-B — Incidence Dissipation Tax

$$
\boxed{
a_\Sigma
\ge
\int_\Sigma
g
\left(
2+\frac43(n\cdot\eta)^2
\right)dS.
}
$$

## R17-C — Exact surface flux

$$
\boxed{
\mathcal B_Q
=
\lambda^2
\int_\Sigma
\eta\cdot
[\nabla n-(\operatorname{div}n)I]
\nabla q\,dS.
}
$$

## R17-D — Level Hodge-Coherence Identity

$$
\boxed{
\frac{E_M^u}{D_M}
=
(\sqrt{R_M}-1)^2
+
2\sqrt{R_M}(1-\rho_M).
}
$$

## R17-E — Critical weighted-gradient budget

$$
\boxed{
Q(T)^2
\le
Q(0)^2
+
C
\int_0^T
E_M(t)dt.
}
$$

---

# 26. Next round — Weighted Physical-Gradient / Strain–Vorticity Return

The next round will no longer treat:

$$
\mathcal B_Q
$$

as the primary Boss.

It will directly attack:

$$
\boxed{
E_M
=
\int
|v|
\left[
|\nabla u|^2
+
|(\nabla u)^\top n|^2
\right]dx.
}
$$

Questions:

1. Accurately decompose $E_M$ into the relational channels of:
   $$
   S_u,
   \omega,
   n
   $$
   ;

2. Whether there is pressure-free / vorticity orthogonality that can cancel out part of the weighted gradient;

3. Whether the time integral of $E_M$ can be jointly constrained by the strain-$H^1$ balance of Round 05 and the geometric carriers of Round 03;

4. Whether there exists:
   $$
   \text{large weighted gradient}
   \Longrightarrow
   \text{alignment rigidity}
   \vee
   \text{viscous overpayment};
   $$

5. If amplitude layers are needed, continue using the continuous $\lambda$ profile without entering dyadic scales.

---

# 27. External primary-source anchors

1. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - velocity-direction geometry can enter 3D NS regularity criteria;
   - $n$ in this round is the optimal quotient representative direction, which is not equivalent to $u/|u|$, thus it only serves as an external methodological anchor for directional geometry.

2. Dongho Chae, Jihoon Lee, *On the Geometric Regularity Conditions for the 3D Navier-Stokes Equations*, arXiv:1606.08126.
   - primary-source background for directional/alignment geometric regularity criteria.

3. Isabelle Gallagher, Gabriel S. Koch, Fabrice Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier-Stokes regularity criterion*, arXiv:1012.0145.
   - bounded $L^\infty_tL^3_x$ prevents finite-time singularity;
   - used in this round to connect the bounded quotient carrier $Q\simeq\|u\|_3$ to the endpoint continuation.

The level-surface identities, incidence tax, Hodge-coherence identity, cumulative flux resummation, and weighted-gradient budget criterion in this round are all directly derived in this document.

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Level\text{-}Surface/Hodge\ Coherence},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Boundary flux}
&=
\mathrm{surface\ geometric\ and\ bulk\ coherent},
\\
\text{Zero incidence}
&=
\mathrm{exact},
\\
\text{Direction crossing}
&=
\mathrm{pays\ dissipation},
\\
\text{Cumulative flux}
&=
\mathrm{continuously\ resumable},
\\
\text{New physical carrier}
&=
E_M,
\\
\text{Spacetime budget}
&=
\int E_Mdt
\text{ scale-critical},
\\
\text{Finite budget}
&=
\mathrm{controls\ }Q,
\\
\text{STOP-C21}
&=
\mathrm{Level\ Hodge\text{-}Coherence/Critical\ Weighted\text{-}Gradient\ Gap},
\\
\text{Next}
&=
\mathrm{Weighted\ Physical\text{-}Gradient/Strain\text{-}Vorticity\ Return}.
\end{aligned}
}
$$