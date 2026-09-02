# NS × X Integral × 24/72 Paradigm in Practice
## Round 16 — Pure Continuous Layer-Cake / Superlevel-Distortion Route

- Date:  2026-08-16
- Version:  v0.1
- Status:  Proof-Route Experiment / Continuous-Only Amplitude-Level Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round:  `NS_X72_Round15_PureContinuous_pHodge_GaugeHessianDistortion_v0.1_2026-08-16.md`
- This round's objective:  Without using dyadic decomposition, atomic decomposition, or discrete shells, directly decompose the quotient dissipation $D$ and gauge-Hessian distortion $H$ from Round 15 using a continuous amplitude threshold
  $$
  \lambda\in(0,\infty)
  $$
  Examine whether the global distortion ratio $\Xi_Q$, if it becomes dangerous, necessarily leaves a localizable witness on some continuous superlevel layer.
- Non-claims:  This document does not prove that all superlevel distortion ratios are controlled; conversely, this round compresses the global obstruction into continuous tail ratio, surface ratio, and level-boundary flux problems.

---

# 0. Round 15 handoff

Let

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative:

$$
v=u+\nabla q,
$$

and set

$$
r=|v|,
\qquad
n=\frac v{|v|}
$$

for $r>0$.

Round 15 definition:

$$
D
=
\int_{\mathbb R^3}
r
\left(
|\nabla v|^2
+
|\nabla r|^2
\right)dx,
$$

and:

$$
H
=
\int_{\mathbb R^3}
r
\left(
|\nabla^2q|^2
+
|\nabla^2q\,n|^2
\right)dx.
$$

yielding:

$$
\boxed{
\frac13
\frac d{dt}Q^3
+
\nu D
=
I_Q,
}
\tag{0.1}
$$

and:

$$
\boxed{
|I_Q|
\le
C
Q
H^{1/2}
D^{1/2}.
}
\tag{0.2}
$$

Define:

$$
\boxed{
\Xi_Q
=
\frac{
Q^2H
}{
\nu^2D
}.
}
\tag{0.3}
$$

If:

$$
\frac d{dt}Q^3>0,
$$

then:

$$
\boxed{
\Xi_Q
>
c_0
}
\tag{0.4}
$$

for some universal threshold $c_0>0$.

Round 15 STOP:

$$
\boxed{
\text{STOP-C19}
=
\text{Weighted Gauge-Hessian / Quotient-Dissipation Gap}.
}
$$

---

# 1. Continuous superlevel sets

For each:

$$
\lambda\ge0,
$$

define:

$$
\boxed{
E_\lambda
=
\{
x\in\mathbb R^3:
r(x)>\lambda
\}.
}
\tag{1.1}
$$

distribution function:

$$
\boxed{
V(\lambda)
=
|E_\lambda|.
}
\tag{1.2}
$$

Define unweighted local densities:

$$
\boxed{
A
=
|\nabla v|^2+|\nabla r|^2,
}
\tag{1.3}
$$

and:

$$
\boxed{
B
=
|\nabla^2q|^2
+
|\nabla^2q\,n|^2.
}
\tag{1.4}
$$

The second term is defined as zero where $r=0$.

tail profiles:

$$
\boxed{
d(\lambda)
=
\int_{E_\lambda}
A\,dx,
}
\tag{1.5}
$$

$$
\boxed{
h(\lambda)
=
\int_{E_\lambda}
B\,dx.
}
\tag{1.6}
$$

Both are nonincreasing.

---

# 2. Exact layer-cake identities

Since:

$$
r(x)
=
\int_0^\infty
\mathbf 1_{\{r(x)>\lambda\}}
\,d\lambda,
$$

Tonelli's theorem gives:

$$
\boxed{
D
=
\int_0^\infty
d(\lambda)\,d\lambda,
}
\tag{2.1}
$$

and:

$$
\boxed{
H
=
\int_0^\infty
h(\lambda)\,d\lambda.
}
\tag{2.2}
$$

Similarly:

$$
r^3
=
\int_0^\infty
3\lambda^2
\mathbf 1_{\{r>\lambda\}}
d\lambda,
$$

thus:

$$
\boxed{
Q^3
=
\|v\|_3^3
=
3
\int_0^\infty
\lambda^2
V(\lambda)
\,d\lambda.
}
\tag{2.3}
$$

Therefore, the critical amplitude, dissipation, and gauge distortion can all be described by the same continuous level parameter:

$$
\lambda
$$

---

# 3. Tail distortion ratio

When:

$$
d(\lambda)>0,
$$

define:

$$
\boxed{
\theta(\lambda)
=
\frac{
h(\lambda)
}{
d(\lambda)
}.
}
\tag{3.1}
$$

Next, define the dimensionless superlevel distortion ratio:

$$
\boxed{
\xi_Q(\lambda)
=
\frac{
Q^2
}{
\nu^2
}
\theta(\lambda)
=
\frac{
Q^2h(\lambda)
}{
\nu^2d(\lambda)
}.
}
\tag{3.2}
$$

If:

$$
d(\lambda)=0<h(\lambda),
$$

define:

$$
\xi_Q(\lambda)=+\infty.
$$

---

# 4. Global distortion is a continuous weighted average of tail distortion

From (2.1)–(2.2):

$$
\frac HD
=
\frac{
\int_0^\infty
\theta(\lambda)d(\lambda)d\lambda
}{
\int_0^\infty
d(\lambda)d\lambda
}.
$$

thus:

$$
\boxed{
\Xi_Q
=
\frac{
\int_0^\infty
\xi_Q(\lambda)
d(\lambda)d\lambda
}{
\int_0^\infty
d(\lambda)d\lambda
}.
}
\tag{4.1}
$$

Therefore:

$$
\boxed{
\Xi_Q
\le
\operatorname*{ess\,sup}_{\lambda>0}
\xi_Q(\lambda).
}
\tag{4.2}
$$

This is an exact mean-value structure.

---

# 5. Continuous Superlevel Distortion Witness

From Round 15:

$$
\frac d{dt}Q^3>0
\Longrightarrow
\Xi_Q>c_0.
$$

From (4.2):

$$
\boxed{
\frac d{dt}Q^3>0
\Longrightarrow
\exists\lambda_\ast>0
:
\xi_Q(\lambda_\ast)>c_0
}
\tag{5.1}
$$

in the essential-supremum sense.

Nomenclature:

$$
\boxed{
\textbf{Continuous Superlevel Distortion Witness}.
}
$$

Meaning:

> When the global critical quotient genuinely grows, the gauge-Hessian distortion cannot exist merely as an unlocalizable weighted average; there must be at least one real amplitude threshold whose entire high-amplitude tail has crossed a distortion/dissipation threshold of the same order of magnitude.

This is not a dyadic pigeonhole.

The threshold:

$$
\lambda_\ast
$$

belongs to the continuous amplitude continuum.

---

# 6. Coarea representation

Assume that on a fixed smooth time slice:

$$
r
$$

is sufficiently regular.

For a.e. regular value:

$$
\lambda,
$$

the coarea formula gives:

$$
\boxed{
-d'(\lambda)
=
\int_{\{r=\lambda\}}
\frac{
A
}{
|\nabla r|
}
\,dS.
}
\tag{6.1}
$$

and:

$$
\boxed{
-h'(\lambda)
=
\int_{\{r=\lambda\}}
\frac{
B
}{
|\nabla r|
}
\,dS.
}
\tag{6.2}
$$

Meanwhile:

$$
\boxed{
-V'(\lambda)
=
\int_{\{r=\lambda\}}
\frac1{|\nabla r|}
\,dS.
}
\tag{6.3}
$$

At critical points, the standard a.e. coarea interpretation can be used.

---

# 7. Surface distortion ratio

Define:

$$
a_\Sigma(\lambda)
=
-d'(\lambda),
$$

$$
b_\Sigma(\lambda)
=
-h'(\lambda).
$$

When:

$$
a_\Sigma(\lambda)>0,
$$

define the instantaneous level-surface distortion ratio:

$$
\boxed{
\sigma(\lambda)
=
\frac{
b_\Sigma(\lambda)
}{
a_\Sigma(\lambda)
}.
}
\tag{7.1}
$$

tail ratio:

$$
\theta=\frac hd.
$$

Differentiating directly:

$$
\boxed{
\theta'(\lambda)
=
\frac{
a_\Sigma(\lambda)
}{
d(\lambda)
}
\left[
\theta(\lambda)
-
\sigma(\lambda)
\right].
}
\tag{7.2}
$$

Nomenclature:

$$
\boxed{
\textbf{Continuous Tail–Surface Ratio Equation}.
}
$$

---

# 8. Interpretation of the ratio equation

If:

$$
\sigma(\lambda)
<
\theta(\lambda),
$$

then:

$$
\theta'(\lambda)>0.
$$

That is, after removing the current level surface, the remaining higher-amplitude tail becomes more distorted.

If:

$$
\sigma(\lambda)
>
\theta(\lambda),
$$

then:

$$
\theta'(\lambda)<0.
$$

Therefore, high-amplitude distortion growth is not discrete shell hopping.

It can be described as a flow on the continuous amplitude-coordinate between:

$$
\boxed{
\text{tail ratio}
\leftrightarrow
\text{boundary-surface ratio}
}
$$

---

# 9. Continuous superlevel Sobolev bridge

Let:

$$
0\le\lambda<\mu.
$$

Take:

$$
f_\lambda
=
(r-\lambda)_+.
$$

Sobolev:

$$
\|f_\lambda\|_6^2
\le
C
\int_{E_\lambda}
|\nabla r|^2dx
\le
C d(\lambda).
$$

But on:

$$
E_\mu,
$$

we have:

$$
f_\lambda
\ge
\mu-\lambda.
$$

Thus:

$$
\boxed{
(\mu-\lambda)^2
V(\mu)^{1/3}
\le
C
d(\lambda).
}
\tag{9.1}
$$

Nomenclature:

$$
\boxed{
\textbf{Continuous Interlevel Sobolev Constraint}.
}
$$

This implies:

> To maintain a large volume for a high-amplitude superlevel set, gradient dissipation must be paid at a lower threshold.

---

# 10. Deviatoric curvature tail

Round 15 proved:

$$
I_Q
=
\int
r^3
n^\top H_q^0n\,dx,
$$

where:

$$
H_q^0
=
\nabla^2q
-
\frac13(\Delta q)I.
$$

Define:

$$
\boxed{
c(\lambda)
=
\int_{E_\lambda}
n^\top H_q^0n\,dx.
}
\tag{10.1}
$$

layer-cake:

$$
\boxed{
I_Q
=
3
\int_0^\infty
\lambda^2
c(\lambda)
\,d\lambda.
}
\tag{10.2}
$$

Thus, the critical quotient growth itself can also be exactly rewritten using continuous amplitude layers.

---

# 11. Tail curvature bound

There exists a universal:

$$
C_0>0
$$

such that:

$$
|H_q^0|
\le
C_0|\nabla^2q|.
$$

Thus:

$$
|c(\lambda)|
\le
C_0
\left(
\int_{E_\lambda}
|\nabla^2q|^2dx
\right)^{1/2}
V(\lambda)^{1/2}.
$$

From:

$$
h(\lambda)
\ge
\int_{E_\lambda}
|\nabla^2q|^2dx,
$$

we obtain:

$$
\boxed{
|c(\lambda)|
\le
C_0
h(\lambda)^{1/2}
V(\lambda)^{1/2}.
}
\tag{11.1}
$$

Thus:

$$
\boxed{
|I_Q|
\le
3C_0
\int_0^\infty
\lambda^2
h(\lambda)^{1/2}
V(\lambda)^{1/2}
\,d\lambda.
}
\tag{11.2}
$$

---

# 12. Continuous Dangerous-Layer Witness

Define:

$$
\boxed{
\Gamma_Q(\lambda)
=
\frac{
3C_0
\lambda^2
h(\lambda)^{1/2}
V(\lambda)^{1/2}
}{
\nu d(\lambda)
}
}
\tag{12.1}
$$

for:

$$
d(\lambda)>0.
$$

If all:

$$
\lambda
$$

satisfy:

$$
\Gamma_Q(\lambda)\le1,
$$

then from (11.2):

$$
|I_Q|
\le
\nu
\int_0^\infty
d(\lambda)d\lambda
=
\nu D.
$$

Thus:

$$
\frac d{dt}Q^3
\le0.
$$

Conversely:

$$
\boxed{
\frac d{dt}Q^3>0
\Longrightarrow
\exists\lambda_\ast:
\Gamma_Q(\lambda_\ast)>1.
}
\tag{12.2}
$$

Nomenclature:

$$
\boxed{
\textbf{Continuous Dangerous-Layer Witness}.
}
$$

Compared to Section 5, this more directly places the growth and:

- tail gauge Hessian;
- tail volume;
- tail dissipation;

at the same threshold.

---

# 13. Cross-level necessary condition

Choosing in (9.1):

$$
\mu=\lambda,
\qquad
\lambda_0=\frac\lambda2.
$$

we obtain:

$$
\frac{\lambda^2}{4}
V(\lambda)^{1/3}
\le
C
d(\lambda/2).
$$

Thus:

$$
\boxed{
V(\lambda)^{1/2}
\le
C
\frac{
d(\lambda/2)^{3/2}
}{
\lambda^3
}.
}
\tag{13.1}
$$

Substituting into:

$$
\Gamma_Q(\lambda)>1
$$

yielding the necessary condition:

$$
\boxed{
h(\lambda)^{1/2}
d(\lambda/2)^{3/2}
>
c
\nu
\lambda
d(\lambda)
}
\tag{13.2}
$$

for some universal:

$$
c>0.
$$

Thus, a dangerous high-amplitude layer requires a continuous two-threshold imbalance:

$$
\boxed{
\lambda/2
\longrightarrow
\lambda.
}
$$

Note:

$$
\frac12
$$

is merely a convenient choice here, not a dyadic hierarchy.

For any:

$$
0<\alpha<1
$$

one can choose:

$$
\lambda_0=\alpha\lambda.
$$

---

# 14. Localizing nonlinear-Hodge orthogonality

Round 15 differentiated gauge:

$$
\operatorname{div}
\left(
M_v\partial_\ell v
\right)
=
0,
$$

where:

$$
M_v
=
r(I+n\otimes n).
$$

Testing over the whole space:

$$
q_\ell=\partial_\ell q
$$

yields the global orthogonality:

$$
\int
\nabla q_\ell
\cdot
M_v
\partial_\ell v
dx
=
0.
$$

Now restricting to:

$$
E_\lambda.
$$

For a regular level, integration by parts gives:

$$
\boxed{
\int_{E_\lambda}
\nabla q_\ell
\cdot
M_v
\partial_\ell v
dx
=
\int_{\partial E_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot
\nu_\lambda
\,dS.
}
\tag{14.1}
$$

where:

$$
\nu_\lambda
$$

is the outward normal of $E_\lambda$.

Define:

$$
\boxed{
\mathcal B_Q(\lambda)
=
\sum_{\ell=1}^3
\int_{\partial E_\lambda}
q_\ell
\left(
M_v\partial_\ell v
\right)
\cdot
\nu_\lambda
\,dS.
}
\tag{14.2}
$$

---

# 15. Local Pythagorean identity acquires a boundary flux

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
\nabla q_\ell\,dx,
$$

and:

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

Since:

$$
\partial_\ell u
=
\partial_\ell v-\nabla q_\ell,
$$

from (14.1):

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
\tag{15.1}
$$

This is the localized nonlinear-Hodge Pythagorean identity.

When over the whole space:

$$
\mathcal B_Q=0
$$

it recovers Round 15:

$$
E_M^u=D+H.
$$

---

# 16. Localization is not free

Section 15 shows that:

$$
\boxed{
\text{global nonlinear-Hodge orthogonality}
}
$$

does not restrict losslessly to each:

$$
E_\lambda.
$$

Localization generates:

$$
\boxed{
\text{level-surface boundary flux }\mathcal B_Q(\lambda).
}
$$

Therefore, even if the Continuous Superlevel Distortion Witness tells us:

> a certain layer must be dangerous,

when transferring the global Pythagorean coercivity to that layer, one must control:

$$
\boxed{
\mathcal B_Q(\lambda).
}
$$

This is the genuine new obstruction of this round.

---

# 17. Boundary flux is continuous, not discrete

The level boundary:

$$
\partial E_\lambda
=
\{r=\lambda\}
$$

continuously sweeps through the amplitude geometry with:

$$
\lambda
$$

Thus:

$$
\mathcal B_Q:
(0,\infty)
\to\mathbb R
$$

is a continuous-level flux profile.

Currently, there is no reason to replace:

$$
\lambda
$$

with:

$$
2^j.
$$

Therefore, the level localization itself remains entirely Pure-C.

---

# 18. Layer profile as an X-state

This round establishes:

$$
\boxed{
X_{\rm layer}(\lambda)
=
\left\langle
V(\lambda),
d(\lambda),
h(\lambda),
\theta(\lambda),
\sigma(\lambda),
c(\lambda),
\Gamma_Q(\lambda),
\mathcal B_Q(\lambda)
\right\rangle.
}
\tag{18.1}
$$

The entire weighted nonlinear-Hodge obstruction is lifted to a continuous field:

$$
\boxed{
\lambda
\longmapsto
X_{\rm layer}(\lambda).
}
\tag{18.2}
$$

Thus, the single global ratio of Round 15:

$$
\Xi_Q
$$

is now resolved into a continuous amplitude-profile.

---

# 19. Observation update

Knowing only:

$$
\Xi_Q
$$

can tell us that:

$$
\exists\lambda_\ast
$$

is dangerous,

but cannot tell us:

- at which threshold the danger lies;
- how the tail ratio moves with the threshold;
- the distortion density of the level surface itself;
- the localized orthogonality boundary flux.

Thus:

$$
\boxed{
\mathsf C_{\Xi_Q}
\to
\mathsf X_{\rm layer}
}
$$

is the observation refinement of this round.

But:

$$
X_{\rm layer}
$$

remains a continuous object.

---

# 20. STOP-C20 — Continuous Layer Distortion / Boundary-Flux Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C20}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ amplitude\ superlevels},
\\
\text{global\ distortion}
=
\mathrm{weighted\ average\ of\ tail\ ratios},
\\
\text{positive\ growth}
\Rightarrow
\mathrm{dangerous\ continuous\ layer},
\\
\text{tail\ evolution}
=
\theta'
=
(a_\Sigma/d)(\theta-\sigma),
\\
\text{interlevel\ constraint}
=
(\mu-\lambda)^2V(\mu)^{1/3}
\lesssim
d(\lambda),
\\
\text{localized\ Hodge\ identity}
=
E_M^u
=
D_M+H_M-2\mathcal B_Q,
\\
\text{missing}
=
\mathrm{unconditional\ control\ of\ dangerous\ tail\ ratio\ and\ boundary\ flux},
\\
\text{essential\ discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

Nomenclature:

$$
\boxed{
\textbf{STOP-C20:
Continuous Layer-Distortion / Boundary-Flux Gap}.
}
$$

---

# 21. 24/72 Ledger — Round 16

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C181 | superlevel sets $E_\lambda$ | $\mathsf C$ | level organization | relational | $\mathsf F$ | FORM |
| C182 | layer-cake $D,H$ | $\mathsf C$ | continuous integral | targeted | $\mathsf F$ | EXACT |
| C183 | distribution formula for $Q^3$ | $\mathsf C$ | continuous integral | scalar | $\mathsf F$ | EXACT |
| C184 | tail ratio $\theta$ | $\mathsf C$ | recognition | scalar profile | $\mathsf F$ | FORM |
| C185 | $\Xi_Q$ as weighted average | $\mathsf C$ | continuous profile | scalar | $\mathsf F$ | EXACT |
| C186 | continuous distortion witness | $\mathsf C$ | mean-value | targeted | $\mathsf F$ | PROVED |
| C187 | coarea surface densities | $\mathsf C$ | surface organization | $\mathsf X$ | $\mathsf F$ | EXACT a.e. |
| C188 | tail–surface ratio ODE | $\mathsf C$ | continuous $\lambda$ flow | scalar profile | $\mathsf F$ | EXACT |
| C189 | interlevel Sobolev constraint | $\mathsf C$ | continuous thresholds | targeted | $\mathsf F$ | PROVED |
| C190 | curvature layer-cake | $\mathsf C$ | continuous integral | relational | $\mathsf F$ | EXACT |
| C191 | dangerous-layer witness $\Gamma_Q$ | $\mathsf C$ | necessity | scalar profile | $\mathsf F$ | PROVED |
| C192 | cross-level danger condition | $\mathsf C$ | continuous two-threshold | targeted | $\mathsf F$ | PROVED |
| C193 | localized Hodge orthogonality | $\mathsf C$ | level surface | relational | $\mathsf F$ | EXACT |
| C194 | boundary flux $\mathcal B_Q$ | $\mathsf C$ | surface flux | $\mathsf X$ | $\mathsf F$ | FORM |
| C195 | localized Pythagorean | $\mathsf C$ | surface/global | relational | $\mathsf F$ | EXACT |
| C196 | unconditional boundary-flux control | $\mathsf C$ | level geometry | targeted | $\mathsf F$ | OPEN / STOP-C20 |

---

# 22. Continuous-versus-discrete status

This round explicitly adopts:

$$
\boxed{
\lambda\in(0,\infty)
}
$$

instead of:

$$
\lambda_j=2^j.
$$

All pigeonhole / localization statements are accomplished via continuous integrals and essential supremums.

Thus:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{22.1}
$$

We can even state more precisely now:

> If a dyadic shell appears in the future, it must be proven to provide essential information that a continuous $\lambda$ profile cannot provide; otherwise, it can only be considered a convenience discretization.

---

# 23. Strongest results of Round 16

## R16-A — global-to-layer witness

$$
\boxed{
Q^3{}'>0
\Longrightarrow
\exists\lambda_\ast:
\xi_Q(\lambda_\ast)>c_0.
}
$$

## R16-B — dangerous growth layer

$$
\boxed{
Q^3{}'>0
\Longrightarrow
\exists\lambda_\ast:
\Gamma_Q(\lambda_\ast)>1.
}
$$

## R16-C — continuous tail-surface dynamics

$$
\boxed{
\theta'
=
\frac{a_\Sigma}{d}
(\theta-\sigma).
}
$$

## R16-D — localization cost

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
$$

Thus, global orthogonality is not localizable for free.

---

# 24. Next round — Level-Surface Flux Geometry

The next round will no longer study the global:

$$
\Xi_Q.
$$

It will directly study:

$$
\boxed{
\mathcal B_Q(\lambda)
}
$$

and:

$$
\boxed{
\sigma(\lambda).
}
$$

Core questions:

1. Does the level-set normal:
   $$
   \nu_\lambda
   =
   -\frac{\nabla r}{|\nabla r|}
   $$
   connect the boundary flux to the amplitude-gradient geometry?

2. What exact restriction does the nonlinear gauge:
   $$
   \operatorname{div}(r^2n)=0
   $$
   impose on the normal/tangential decomposition on the level surface?

3. Can $\mathcal B_Q$ be decomposed into continuous surface invariants such as mean curvature, normal gauge Hessian, and tangential derivatives?

4. Does a dangerous $\Gamma_Q>1$ force the surface area / curvature / flux to be simultaneously anomalous?

5. If the topology of the level surfaces changes, first use a continuous Morse/stratified description; only consider $\mathsf D$ when countable component enumeration is genuinely needed.

---

# 25. External primary-source anchors

1. Tobias Barker, Wendong Wang, *Estimates of the singular set for the Navier-Stokes equations with supercritical assumptions on the pressure*, arXiv:2111.15444.
   - Primary-source background of using velocity-gradient weighted quantities
     $$
     |\nabla v|^2|v|^{q-2}
     $$
     in NS regularity analysis; the $|v|$-weighted structure of $D$ in this round is only compared methodologically with it.

2. Yanqing Wang, Wei Wei, Huan Yu, *$\varepsilon$-regularity criteria in Lorentz spaces to the 3D Navier-Stokes equations*, arXiv:1909.09957.
   - Background in distribution-function/Lorentz critical regularity; the continuous superlevel profile formulas in this round are directly derived in this document.

The layer-cake identities, tail-ratio equation, dangerous-layer witness, cross-level inequality, and localized Hodge boundary-flux identity in this text are all directly derived in this document.

---

# 26. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Layer\text{-}Cake/Superlevel},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Global distortion}
&=
\mathrm{continuous\ weighted\ average},
\\
\text{Positive growth}
&=
\mathrm{forces\ dangerous\ continuous\ layer},
\\
\text{Amplitude coordinate}
&=
\lambda\in(0,\infty),
\\
\text{Tail dynamics}
&=
\theta'=(a_\Sigma/d)(\theta-\sigma),
\\
\text{Interlevel constraint}
&=
(\mu-\lambda)^2V(\mu)^{1/3}\lesssim d(\lambda),
\\
\text{Localization cost}
&=
\mathcal B_Q(\lambda),
\\
\text{STOP-C20}
&=
\mathrm{Continuous\ Layer\text{-}Distortion/Boundary\text{-}Flux\ Gap},
\\
\text{Next}
&=
\mathrm{Level\text{-}Surface\ Flux\ Geometry}.
\end{aligned}
}
$$