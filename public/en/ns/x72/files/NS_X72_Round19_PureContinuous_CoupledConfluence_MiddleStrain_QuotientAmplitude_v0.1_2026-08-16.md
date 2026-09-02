# NS × X Integral × 24/72 Paradigm In Action
## Round 19 — Pure Continuous Coupled Confluence / Middle-Strain–Quotient-Amplitude Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Two-Route Coupled Pure-C Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round18_PureContinuous_WeightedStrainVorticity_ObstructionConfluence_v0.1_2026-08-16.md`
- Objective of this round: Do not open new representations. Directly couple the two already confluent Pure-C routes:
  1. critical quotient amplitude
     $$
     r=|v|;
     $$
  2. middle-strain / determinant / vortex-stretching geometry
     $$
     \lambda_2^+,\quad(-\det S)_+.
     $$
  Establish the exact algebraic comparability, direction-independent floor, continuous confluence layers, and low-amplitude escape carrier between the two.
- Non-assertion: This round does not rule out the low-amplitude degeneracy channel; instead, this round formalizes the fact that "middle-strain can be spatially separated from the quotient amplitude" into a new continuous sublevel obstruction.

---

# 0. 24/72 branch audit

Currently, the entire NS experiment remains within the 24/72 framework.

However, we deliberately focus exclusively on the substrate axis:

$$
\boxed{
B=\mathsf C.
}
$$

Therefore, up to Round 19, it is not the case that "after running through the 24/72 framework, we found only continuity."

More precisely:

$$
\boxed{
\text{we are exhausting the Pure-C substrate slice before switching substrate}.
}
$$

Within this slice, the other axes have undergone multiple changes:

- update organization:
  $$
  \mathsf S,\quad
  \mathsf P,\quad
  \mathsf R,
  \quad
  \text{hybrid continuous routes};
  $$
- observation:
  $$
  \mathsf C
  \to
  \mathsf X
  \to
  \mathsf C_{\rm targeted}
  $$
  multiple back-and-forth transitions;
- transition law remains:
  $$
  \boxed{
  L=\mathsf F.
  }
  $$

Thus, the current results merely indicate:

$$
\boxed{
\textbf{
NS Pure-C proof search has not yet forced an essential discrete substrate.
}
}
$$

This does not imply that the general world, general mathematics, or the complete 72-grid only requires a continuous substrate.

---

# 1. Round 18 confluence core

Round 18 established the bridge between:

$$
Q(t)
=
\mathfrak Q_3[u(t)]
$$

and the weighted physical-gradient carrier:

$$
E_M
$$

and proved that a potential critical quotient blow-up:

$$
Q(t)\to\infty
$$

would force:

$$
\int_0^{T_\ast}
\|\nabla\omega\|_2^2dt
=
\infty,
$$

which in turn forces the cumulative vortex stretching:

$$
\int_0^{T_\ast}
\int
\omega^\top S\omega\,dxdt
=
+\infty.
$$

Finally returning to:

$$
\boxed{
\int_0^{T_\ast}
\int
\lambda_2^+
|S|^2dxdt
=
\infty.
}
$$

Therefore, this round directly couples:

$$
r=|v|
$$

with:

$$
\lambda_2^+.
$$

---

# 2. Exact eigenvalue parametrization on the dangerous branch

Let the strain eigenvalues be:

$$
\lambda_1
\le
\lambda_2
\le
\lambda_3,
$$

and:

$$
\lambda_1+\lambda_2+\lambda_3=0.
$$

On the dangerous branch:

$$
\lambda_2>0.
$$

Let:

$$
b=\lambda_2>0,
$$

and:

$$
k
=
\frac{\lambda_3}{\lambda_2}
\ge1.
$$

Then:

$$
\boxed{
\lambda_3=kb,
}
$$

and:

$$
\boxed{
\lambda_1=-(1+k)b.
}
\tag{2.1}
$$

Therefore:

$$
\boxed{
|S|^2
=
2b^2
(1+k+k^2).
}
\tag{2.2}
$$

And:

$$
\boxed{
-\det S
=
b^3k(1+k).
}
\tag{2.3}
$$

---

# 3. Two-sided determinant–middle-eigenvalue equivalence

From (2.2)–(2.3):

$$
\frac{
-\det S
}{
b|S|^2
}
=
\frac{
k(1+k)
}{
2(1+k+k^2)
}.
$$

For:

$$
k\ge1,
$$

we have:

$$
\boxed{
\frac13
\le
\frac{
k(1+k)
}{
2(1+k+k^2)
}
<
\frac12.
}
\tag{3.1}
$$

Thus:

$$
\boxed{
\frac13
\lambda_2
|S|^2
\le
-\det S
\le
\frac12
\lambda_2
|S|^2
}
\tag{3.2}
$$

in the region:

$$
\lambda_2>0.
$$

If:

$$
\lambda_2\le0,
$$

then:

$$
\det S\ge0
$$

and:

$$
(-\det S)_+=0.
$$

Therefore, globally pointwise:

$$
\boxed{
\frac13
\lambda_2^+
|S|^2
\le
(-\det S)_+
\le
\frac12
\lambda_2^+
|S|^2.
}
\tag{3.3}
$$

Named:

$$
\boxed{
\textbf{Dangerous Determinant Equivalence}.
}
$$

Round 03 only required the right-hand upper bound.

Round 19 provides the left-hand side, showing that the dangerous determinant and the positive middle-eigenvalue density are actually constant-factor equivalent.

---

# 4. Spectral eccentricity does not destroy the equivalence

The parameter:

$$
k=\frac{\lambda_3}{\lambda_2}
$$

can be arbitrarily large.

However:

$$
\frac{
k(1+k)
}{
2(1+k+k^2)
}
$$

always falls within:

$$
\left[
\frac13,\frac12
\right).
$$

Therefore:

$$
\boxed{
\text{even extreme strain spectral eccentricity cannot separate }
(-\det S)_+
\text{ from }
\lambda_2^+|S|^2
\text{ by more than universal constants}.
}
$$

This indicates that the Round 03 obstruction core is more rigid than when initially using a one-way inequality.

---

# 5. Direction-Independent Middle-Eigenvalue Floor

When:

$$
\lambda_2=b>0,
$$

the three eigenvalue absolute values are:

$$
|\lambda_1|
=
(1+k)b
\ge2b,
$$

$$
|\lambda_2|
=
b,
$$

$$
|\lambda_3|
=
kb
\ge b.
$$

Therefore, the smallest singular value of $S$ is exactly:

$$
b.
$$

Thus, for any unit vector:

$$
n\in\mathbb S^2,
$$

we have:

$$
\boxed{
|Sn|
\ge
\lambda_2.
}
\tag{5.1}
$$

Adding the positive part, this can be written as:

$$
\boxed{
\lambda_2^+
\le
|Sn|
}
\tag{5.2}
$$

which holds for all unit $n$.

Named:

$$
\boxed{
\textbf{Direction-Independent Middle-Strain Floor}.
}
$$

---

# 6. Consequence for the optimal quotient direction

The:

$$
n
=
\frac v{|v|}
$$

from Rounds 14–18 is not an arbitrary external direction.

It is the direction of the optimal critical quotient representative.

However, (5.2) holds for all:

$$
n.
$$

Therefore:

$$
\boxed{
\textbf{
positive middle strain cannot be hidden by choosing a favorable optimal quotient direction.
}
}
\tag{6.1}
$$

This rules out a potential escape:

> Perhaps the nonlinear gauge can avoid $\lambda_2^+$ simply by choosing $n$ in the weak direction of the strain.

When:

$$
\lambda_2>0
$$

there is no singular direction weaker than:

$$
\lambda_2.
$$

---

# 7. Weighted middle-strain floor

Multiplying by:

$$
r=|v|\ge0,
$$

from (5.2) we get:

$$
\boxed{
r(\lambda_2^+)^2
\le
r|Sn|^2
\le
r|S|^2.
}
\tag{7.1}
$$

Integrating:

$$
\boxed{
\int
r(\lambda_2^+)^2dx
\le
W_S
\le
E_M.
}
\tag{7.2}
$$

where:

$$
W_S
=
\int
r|S|^2dx.
$$

Therefore, the Round 17 physical weighted-gradient carrier must inevitably observe the weighted square of the positive middle eigenvalue.

---

# 8. Directional trichotomy

Round 18 defined:

$$
d_n
=
Sn
-
\frac12
\omega\times n.
$$

Then:

$$
Sn
=
d_n
+
\frac12
\omega\times n.
$$

From:

$$
(\lambda_2^+)^2
\le
|Sn|^2
$$

and:

$$
|a+b|^2
\le
2|a|^2+2|b|^2,
$$

we obtain:

$$
\boxed{
(\lambda_2^+)^2
\le
2|d_n|^2
+
\frac12
|\omega\times n|^2.
}
\tag{8.1}
$$

Therefore, if the positive middle strain is large, it must appear in at least one of:

1. strain–rotation mismatch:
   $$
   |d_n|;
   $$
2. transverse vorticity:
   $$
   |\omega\times n|;
   $$

Both are already included in:

$$
E_M.
$$

---

# 9. Define the confluence ratio

For:

$$
r>0
$$

define:

$$
\boxed{
\chi_C
=
\frac{
\lambda_2^+
}{
r
}.
}
\tag{9.1}
$$

If:

$$
r=0
\quad\text{and}\quad
\lambda_2^+>0,
$$

define:

$$
\chi_C=+\infty.
$$

If both are zero, let:

$$
\chi_C=0.
$$

Under NS scaling:

$$
r_\Lambda
=
\Lambda r,
$$

$$
(\lambda_2^+)_\Lambda
=
\Lambda^2\lambda_2^+,
$$

Therefore:

$$
\boxed{
(\chi_C)_\Lambda
=
\Lambda\chi_C.
}
\tag{9.2}
$$

Thus:

$$
\chi_C
$$

is an inverse-length / critical-rate type variable.

---

# 10. Determinant production as a weighted expectation of $\chi_C$

In the:

$$
\lambda_2>0
$$

region:

$$
(-\det S)_+
=
c(k)
\lambda_2^+
|S|^2
$$

where:

$$
\boxed{
\frac13
\le
c(k)
<
\frac12.
}
$$

But:

$$
\lambda_2^+
|S|^2
=
\chi_C
\left(
r|S|^2
\right).
$$

Therefore:

$$
\boxed{
\frac13
\chi_C
r|S|^2
\le
(-\det S)_+
\le
\frac12
\chi_C
r|S|^2.
}
\tag{10.1}
$$

Define the positive-strain weighted measure:

$$
\boxed{
d\mu_C
=
\mathbf 1_{\{\lambda_2>0\}}
r|S|^2dx.
}
\tag{10.2}
$$

Then:

$$
\boxed{
\frac13
\int
\chi_C\,d\mu_C
\le
\int
(-\det S)_+dx
\le
\frac12
\int
\chi_C\,d\mu_C.
}
\tag{10.3}
$$

This is the exact coupling formula of the two proof routes.

---

# 11. Interpretation

The dangerous strain production of Round 03:

$$
(-\det S)_+
$$

can now be interpreted as:

$$
\boxed{
\text{critical weighted strain budget}
\times
\text{middle-strain / quotient-amplitude rate}.
}
$$

That is:

$$
\boxed{
\text{production}
\sim
\chi_C
\,d\mu_C.
}
$$

Therefore, the obstruction core is no longer just:

$$
\lambda_2^+
$$

or:

$$
r.
$$

but rather the relational ratio of the two:

$$
\boxed{
\chi_C=\lambda_2^+/r.
}
$$

---

# 12. Continuous confluence layers

For:

$$
\eta\ge0,
$$

define:

$$
\boxed{
\mathcal C_\eta
=
\{
x:
\chi_C(x)>\eta
\}.
}
\tag{12.1}
$$

By the layer-cake representation:

$$
\boxed{
\int
\chi_C\,d\mu_C
=
\int_0^\infty
\mu_C(\mathcal C_\eta)
\,d\eta.
}
\tag{12.2}
$$

Therefore, the positive determinant production can be represented by the continuous ratio-level field:

$$
\eta\in(0,\infty).
$$

This is another continuous layer coordinate.

There are no dyadic ratio bins.

---

# 13. Confluence-layer witness

Let:

$$
P_+(t)
=
\int
(-\det S)_+dx.
$$

From (10.3):

$$
\int
\chi_C\,d\mu_C
\ge
2P_+.
$$

If:

$$
\mu_C(\mathbb R^3)>0,
$$

define the weighted mean confluence rate:

$$
\boxed{
\bar\chi_C
=
\frac{
\int
\chi_C\,d\mu_C
}{
\mu_C(\mathbb R^3)
}.
}
\tag{13.1}
$$

Then:

$$
\boxed{
2
\frac{
P_+
}{
\mu_C(\mathbb R^3)
}
\le
\bar\chi_C
\le
3
\frac{
P_+
}{
\mu_C(\mathbb R^3)
}.
}
\tag{13.2}
$$

Thus, if the production becomes large relative to the weighted strain budget, it necessarily means that the weighted mean of:

$$
\chi_C
$$

becomes large.

---

# 14. Median confluence witness

By the layer-cake / reverse Markov inequality principle:

If:

$$
\bar\chi_C>0,
$$

then we cannot have for a.e. $\mu_C$:

$$
\chi_C<
\frac12\bar\chi_C.
$$

More precisely, there must exist a positive $\mu_C$-measure set:

$$
\boxed{
\left\{
\chi_C
\ge
\frac12\bar\chi_C
\right\}
}
\tag{14.1}
$$

that carries a non-zero weighted strain mass.

Therefore, a large production-to-budget ratio must appear in actual continuous ratio layers, and cannot be generated merely by measure-zero spikes forming the weighted mean.

---

# 15. Low-amplitude escape carrier

The confluence ratio:

$$
\chi_C
=
\frac{
\lambda_2^+
}{
r
}
$$

exposes a new potential escape:

$$
r\downarrow0
$$

while:

$$
\lambda_2^+
$$

remains large.

To quantify this, define:

$$
\boxed{
\mathcal I_0
=
\int_{\{r>0\}}
\frac{
|S|^4
}{
r
}
dx,
}
\tag{15.1}
$$

with the convention that if on the set:

$$
r=0
$$

$$
|S|>0
$$

has positive measure / nonintegrable trace, then:

$$
\mathcal I_0=+\infty.
$$

This is the inverse-amplitude strain carrier.

---

# 16. Overlap–degeneracy inequality

Let:

$$
M_2
=
\int
\lambda_2^+
|S|^2dx.
$$

By Cauchy–Schwarz:

$$
M_2
=
\int
\left(
\sqrt r\,\lambda_2^+
\right)
\left(
\frac{
|S|^2
}{
\sqrt r
}
\right)dx.
$$

Therefore:

$$
M_2^2
\le
\left(
\int
r(\lambda_2^+)^2dx
\right)
\mathcal I_0.
$$

From (7.2):

$$
\boxed{
M_2^2
\le
E_M
\mathcal I_0.
}
\tag{16.1}
$$

Then by the Dangerous Determinant Equivalence:

$$
P_+
\le
\frac12M_2,
$$

Therefore:

$$
\boxed{
P_+^2
\le
\frac14
E_M
\mathcal I_0.
}
\tag{16.2}
$$

Named:

$$
\boxed{
\textbf{Overlap–Degeneracy Inequality}.
}
$$

---

# 17. Meaning of the overlap–degeneracy inequality

Strong dangerous determinant production requires the product of two types of resources:

$$
\boxed{
\text{high-amplitude weighted physical-gradient budget}
}
$$

and:

$$
\boxed{
\text{inverse-amplitude strain concentration}.
}
$$

If:

$$
E_M
$$

does not correspondingly amplify,

then:

$$
\mathcal I_0
$$

must amplify.

Therefore, if the middle-strain activity wants to avoid the quotient amplitude weight:

$$
r,
$$

it can only escape into the degeneracy region where:

$$
\boxed{
r\approx0
}
$$

---

# 18. Continuous sublevel representation of the inverse-amplitude escape

For:

$$
r>0,
$$

we have:

$$
\boxed{
\frac1r
=
\int_r^\infty
\frac{
d\eta
}{
\eta^2
}.
}
\tag{18.1}
$$

Thus, by Tonelli's theorem:

$$
\boxed{
\mathcal I_0
=
\int_0^\infty
\frac1{\eta^2}
\left[
\int_{\{0<r<\eta\}}
|S|^4dx
\right]
d\eta.
}
\tag{18.2}
$$

Therefore, the low-amplitude escape can also be completely described by the continuous sublevel parameter:

$$
\eta\in(0,\infty).
$$

There is no need to first slice it into:

$$
2^{-j}.
$$

---

# 19. High-overlap versus low-amplitude escape

This round thus forms two coupled continuous channels.

## Channel O — overlap

The dangerous middle strain overlaps with the nondegenerate quotient amplitude:

$$
\boxed{
r(\lambda_2^+)^2
}
$$

is directly paid for by:

$$
E_M.
$$

## Channel Z — zero-amplitude degeneracy

The dangerous strain avoids the weight:

$$
r
$$

and enters the region:

$$
r\approx0
$$

recorded by:

$$
\boxed{
\mathcal I_0
=
\int
|S|^4/r
}
$$

Thus:

$$
\boxed{
\textbf{
Middle-strain danger cannot simply disappear from the quotient route:
it must appear as weighted overlap or low-amplitude degeneracy.
}
}
\tag{19.1}
$$

---

# 20. Why this still does not close NS

Rounds 17–18 already established that a potential singularity can cause:

$$
\int E_Mdt
=
\infty.
$$

Therefore, (16.2) itself does not generate a contradiction.

At the same time:

$$
\mathcal I_0
$$

currently lacks an ordinary energy-level global bound.

So the new coupling formula narrows the escape routes,

but does not rule out:

$$
\boxed{
E_M\to\text{large}
}
$$

or:

$$
\boxed{
\mathcal I_0\to\text{large}.
}
$$

---

# 21. New representation-stable core

Currently, there are at least three continuous descriptions:

1. strain determinant:
   $$
   (-\det S)_+;
   $$
2. middle eigenvalue:
   $$
   \lambda_2^+|S|^2;
   $$
3. quotient-amplitude confluence:
   $$
   \chi_C\,r|S|^2;
   $$

which are all constant-factor equivalent on the dangerous branch.

Therefore:

$$
\boxed{
\textbf{
the obstruction core is no longer tied to a single representation.
}
}
\tag{21.1}
$$

This is a further strengthening of the Round 18 obstruction confluence.

---

# 22. STOP-C23 — Confluence-Ratio / Low-Amplitude Degeneracy Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C23}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{coupled\ quotient/strain\ confluence},
\\
\text{determinant}
\asymp
\lambda_2^+|S|^2,
\\
\text{directional\ escape}
=
\mathrm{impossible\ when\ }\lambda_2>0,
\\
\text{weighted\ floor}
=
\int r(\lambda_2^+)^2
\le
E_M,
\\
\text{confluence\ ratio}
=
\chi_C=\lambda_2^+/r,
\\
\text{production}
\asymp
\int\chi_C\,d\mu_C,
\\
\text{low-amplitude\ escape}
=
\mathcal I_0=\int|S|^4/r,
\\
\text{overlap–degeneracy}
=
P_+^2
\lesssim
E_M\mathcal I_0,
\\
\text{missing}
=
\mathrm{unconditional\ control\ of\ weighted\ overlap\ or\ inverse-amplitude\ sublevel\ escape},
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
\textbf{STOP-C23:
Confluence-Ratio / Low-Amplitude Degeneracy Gap}.
}
$$

---

# 23. 24/72 Ledger — Round 19

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C228 | 24/72 slice audit | $\mathsf C$ fixed | mixed | mixed | $\mathsf F$ fixed | CLARIFIED |
| C229 | dangerous eigenvalue parametrization | $\mathsf C$ | algebraic | relational | $\mathsf F$ | EXACT |
| C230 | two-sided determinant equivalence | $\mathsf C$ | algebraic | targeted | $\mathsf F$ | PROVED |
| C231 | spectral eccentricity robustness | $\mathsf C$ | algebraic | targeted | $\mathsf F$ | PROVED |
| C232 | direction-independent middle-strain floor | $\mathsf C$ | geometry | relational | $\mathsf F$ | PROVED |
| C233 | weighted $\lambda_2^+$ square floor | $\mathsf C$ | quotient coupling | targeted | $\mathsf F$ | PROVED |
| C234 | directional trichotomy | $\mathsf C$ | strain/vorticity geometry | $\mathsf X$ | $\mathsf F$ | PROVED |
| C235 | confluence ratio $\chi_C$ | $\mathsf C$ | relational | scalar field | $\mathsf F$ | FORM |
| C236 | determinant as $\chi_C$-weighted measure | $\mathsf C$ | measure/geometry | targeted | $\mathsf F$ | EXACT |
| C237 | continuous confluence layers | $\mathsf C$ | layer-cake | profile | $\mathsf F$ | EXACT |
| C238 | inverse-amplitude carrier $\mathcal I_0$ | $\mathsf C$ | sublevel geometry | scalar | $\mathsf F$ | FORM |
| C239 | overlap–degeneracy inequality | $\mathsf C$ | Cauchy coupling | relational | $\mathsf F$ | PROVED |
| C240 | continuous sublevel resummation | $\mathsf C$ | layer-cake | profile | $\mathsf F$ | EXACT |
| C241 | unconditional confluence closure | $\mathsf C$ | coupled | targeted | $\mathsf F$ | OPEN / STOP-C23 |

---

# 24. Continuous-versus-discrete status

This round introduces two new layer variables:

$$
\eta
=
\chi_C\text{ threshold},
$$

and:

$$
\eta
=
r\text{ sublevel threshold}.
$$

Both are in the:

$$
(0,\infty)
$$

continuous range.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

Currently, there is still no proof step that requires changing the continuous layer to a countable shell to hold.

---

# 25. Strongest results of Round 19

## R19-A — Dangerous Determinant Equivalence

$$
\boxed{
\frac13\lambda_2^+|S|^2
\le
(-\det S)_+
\le
\frac12\lambda_2^+|S|^2.
}
$$

## R19-B — No Directional Escape

$$
\boxed{
\lambda_2^+
\le
|Sn|
\quad
\forall n\in\mathbb S^2.
}
$$

## R19-C — Exact confluence carrier

$$
\boxed{
(-\det S)_+
\asymp
\frac{\lambda_2^+}{|v|}
\left(
|v||S|^2
\right).
}
$$

## R19-D — Overlap–Degeneracy Inequality

$$
\boxed{
P_+^2
\lesssim
E_M
\mathcal I_0.
}
$$

Therefore, dangerous middle-strain activity can only:

$$
\boxed{
\text{overlap with quotient amplitude}
\quad\vee\quad
\text{escape into low-amplitude degeneracy}.
}
$$

---

# 26. Next round — low-amplitude degeneracy geometry

After the two-route coupled attack, what truly remains undissected is the:

$$
\boxed{
r\approx0
}
$$

channel.

The next round will directly study:

$$
\mathcal Z_\eta
=
\{0<|v|<\eta\}.
$$

Core issues:

1. $v$ is the unique $L^3$ quotient minimizer;
2. gauge:
   $$
   \operatorname{div}(|v|v)=0;
   $$
3. If $|v|$ is very small but $|S_u|$ is very large, since:
   $$
   \nabla u
   =
   \nabla v-\nabla^2q,
   $$
   the large strain must be carried by:
   $$
   \nabla v
   $$
   or:
   $$
   \nabla^2q;
   $$
4. Check whether this forces the gauge-Hessian distortion from Round 15:
   $$
   H
   $$
   or the Round 17 surface dissipation to increase;
5. If the $v=0$ set forms degenerate strata, first use continuous zero-set / tubular-neighborhood geometry;
6. Only if the zero-set structure truly requires countable atom/component enumeration to close, will we consider:
   $$
   \mathsf C\to\mathsf D.
   $$

---

# 27. External primary-source anchors

1. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - The primary-source background of the middle eigenvalue of strain as a scale-critical blow-up/regularity channel.

2. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - The primary-source background of strain–vorticity interaction and
     $$
     \langle S,\omega\otimes\omega\rangle
     =
     -4\int\det S.
     $$

The two-sided determinant equivalence, direction-independent floor, confluence ratio, and overlap–degeneracy inequality in this round are all directly derived in this document.

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Coupled\ Confluence},
\\
\text{24/72 status}
&=
\mathrm{Pure\text{-}C\ substrate\ slice,\ not\ full\ grid},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Dangerous determinant}
&\asymp
\lambda_2^+|S|^2,
\\
\text{Directional escape}
&=
\mathrm{ruled\ out},
\\
\text{Confluence ratio}
&=
\chi_C=\lambda_2^+/|v|,
\\
\text{Overlap carrier}
&=
E_M,
\\
\text{Degenerate escape carrier}
&=
\mathcal I_0,
\\
\text{STOP-C23}
&=
\mathrm{Confluence\text{-}Ratio/Low\text{-}Amplitude\ Degeneracy\ Gap},
\\
\text{Next}
&=
\mathrm{Low\text{-}Amplitude\ Degeneracy\ Geometry}.
\end{aligned}
}
$$