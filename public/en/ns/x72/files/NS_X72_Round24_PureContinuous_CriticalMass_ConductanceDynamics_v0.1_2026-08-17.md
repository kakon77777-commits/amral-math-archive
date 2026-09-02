# NS × X Integral × 24/72 Paradigm Practice
## Round 24 — Pure Continuous Critical-Mass Conductance Dynamics / Neck-Restoration Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Conductance Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round23_PureContinuous_ConfluenceFeedback_SpectralGapLeakage_v0.1_2026-08-17.md`
- Objective of this round: Directly study the continuous Cheeger conductance, isoperimetric profile, and material-cut dynamics of the critical quotient mass
  $$
  d\mu_Q=m_Qdx
  $$
  Examine whether viscosity automatically restores a disconnected / thin-neck critical mass to a sufficiently large spectral gap, and quantify the competition of selection against neck restoration.
- Non-assertion: This document does not prove uniform-in-time positive conductance. Instead, this round proves that strict positivity / topological reconnection is insufficient to deduce a quantitative spectral gap, and compresses the remaining obstruction into continuous neck-restoration and source-contrast problems.

---

# 0. Round 23 handoff

Round 23 obtained the dynamic intermittency comparison:

$$
\boxed{
(\log\mathfrak J)'
\le
-8\nu I_4
+
\sqrt{\mathfrak J-1}\,
\mathcal A_{\rm sel},
}
\tag{0.1}
$$

where:

$$
I_4
=
\left\langle
|\nabla\log K|^2
\right\rangle_4.
$$

If the critical mass:

$$
\mu_Q
$$

has the Poincaré constant:

$$
C_P,
$$

then:

$$
\boxed{
\mathfrak J-1
\le
4C_P
\mathfrak J
I_4.
}
\tag{0.2}
$$

Therefore, it requires:

$$
\boxed{
C_P(\mu_Q)
<\infty
}
$$

in order to convert spatial Fisher smoothing into an intermittency restoring force.

However, the nonlinear gauge itself does not guarantee:

$$
C_P<\infty.
$$

Round 23 STOP:

$$
\boxed{
\text{STOP-C27}
=
\text{Critical-Mass Spectral-Gap / Source-Variance Leakage Gap}.
}
$$

---

# 1. Critical-mass equation

Round 21:

$$
\boxed{
\partial_t m
+
\operatorname{div}(bm)
=
\nu\Delta m
+
3(G-\bar G)m,
}
\tag{1.1}
$$

In this round, we abbreviate:

$$
m=m_Q,
\qquad
b=b_Q,
\qquad
G=G_Q,
$$

and:

$$
\bar G
=
\int
Gm\,dx.
$$

normalize:

$$
\boxed{
m\ge0,
\qquad
\int m\,dx=1.
}
\tag{1.2}
$$

This is a deterministic uniformly diffusive equation, but the drift:

$$
b_Q
=
u
-
3\frac{\chi_g}{r}n
$$

in the normalized form as:

$$
r\to0
$$

may degenerate / appear singular.

Therefore, all classical positivity statements must be accompanied by coefficient-regularity conditions and cannot be applied unconditionally.

---

# 2. Weighted perimeter

For a finite-perimeter set:

$$
A\subset\mathbb R^3,
$$

define the critical-mass weighted perimeter:

$$
\boxed{
\operatorname{Per}_{\mu}(A)
=
\int_{\partial^\ast A}
m\,d\mathcal H^2.
}
\tag{2.1}
$$

In the smooth case, this is:

$$
\operatorname{Per}_{\mu}(A)
=
\int_{\partial A}
m\,dS.
$$

Let:

$$
a
=
\mu(A)
=
\int_A
m\,dx.
$$

---

# 3. Continuous Cheeger conductance

Define:

$$
\boxed{
h_Q(t)
=
\inf_{
0<\mu(A)<1
}
\frac{
\operatorname{Per}_{\mu}(A)
}{
\min\{
\mu(A),1-\mu(A)
\}
}.
}
\tag{3.1}
$$

dimension:

$$
[h_Q]
=
L^{-1}.
$$

Under NS scaling:

$$
\boxed{
h_Q
\mapsto
\Lambda h_Q.
}
\tag{3.2}
$$

Therefore:

$$
\boxed{
\nu h_Q^2
}
$$

is a scale-critical mixing rate.

---

# 4. Continuous isoperimetric profile

A more complete carrier than a single:

$$
h_Q
$$

is:

$$
\boxed{
\mathscr I_Q(s,t)
=
\inf_{
\mu(A)=s
}
\operatorname{Per}_{\mu}(A),
\qquad
s\in(0,1).
}
\tag{4.1}
$$

Then:

$$
\boxed{
h_Q(t)
=
\inf_{0<s<1}
\frac{
\mathscr I_Q(s,t)
}{
\min\{s,1-s\}
}.
}
\tag{4.2}
$$

Thus, connectivity itself can be represented as a continuous mass-fraction profile:

$$
\boxed{
s\in(0,1)
\longmapsto
\mathscr I_Q(s,t).
}
$$

No cluster graph is needed.

---

# 5. Cheeger-to-Poincaré bridge

In the standard weighted Cheeger/Poincaré framework:

$$
\boxed{
\lambda_1(\mu)
\ge
\frac{
h_Q^2
}{4},
}
\tag{5.1}
$$

so:

$$
\boxed{
C_P
=
\lambda_1^{-1}
\le
\frac4{h_Q^2}.
}
\tag{5.2}
$$

Therefore, Round 23:

$$
\mathfrak J-1
\le
4C_P
\mathfrak J I_4
$$

can be sharpened to:

$$
\boxed{
\mathfrak J-1
\le
\frac{
16
}{
h_Q^2
}
\mathfrak J I_4.
}
\tag{5.3}
$$

That is:

$$
\boxed{
I_4
\ge
\frac{
h_Q^2
}{
16
}
\frac{
\mathfrak J-1
}{
\mathfrak J
}.
}
\tag{5.4}
$$

---

# 6. Conductance-based intermittency feedback

Substituting into Round 23:

$$
(\log\mathfrak J)'
\le
-8\nu I_4
+
\sqrt{\mathfrak J-1}
\mathcal A_{\rm sel},
$$

we obtain:

$$
\boxed{
(\log\mathfrak J)'
\le
-
\frac{
\nu h_Q^2
}{
2
}
\frac{
\mathfrak J-1
}{
\mathfrak J
}
+
\sqrt{\mathfrak J-1}
\mathcal A_{\rm sel}.
}
\tag{6.1}
$$

Let:

$$
y
=
\sqrt{
\mathfrak J-1
}.
$$

Then:

$$
\boxed{
y'
\le
-
\frac{
\nu h_Q^2
}{
4
}
y
+
\frac12
(1+y^2)
\mathcal A_{\rm sel}.
}
\tag{6.2}
$$

Therefore:

$$
\boxed{
\text{conductance mixing rate}
=
\frac{
\nu h_Q^2
}{4}.
}
\tag{6.3}
$$

---

# 7. Dimensionless conductance-feedback ratio

Define:

$$
\boxed{
\mathfrak R_{\rm cond}
=
\frac{
4\mathcal A_{\rm sel}
}{
\nu h_Q^2
}.
}
\tag{7.1}
$$

Under NS scaling:

- $\mathcal A_{\rm sel}\mapsto\Lambda^2\mathcal A_{\rm sel}$;
- $h_Q^2\mapsto\Lambda^2h_Q^2$;

Therefore:

$$
\boxed{
\mathfrak R_{\rm cond}
}
$$

is scale-invariant.

If:

$$
\boxed{
\mathfrak R_{\rm cond}<1,
}
\tag{7.2}
$$

then there exists a Round 23-type intermittency trapping window.

Thus, the feedback closure can be condensed to:

$$
\boxed{
\text{source-selection rate}
<
\text{critical-mass conductance mixing rate}.
}
$$

---

# 8. Material critical-mass cut

Let:

$$
A_t
$$

be advected by the drift:

$$
b
$$

via:

$$
\frac{dX}{dt}
=
b(X,t).
$$

Let:

$$
\boxed{
a(t)
=
\mu_t(A_t).
}
\tag{8.1}
$$

By Reynolds transport theorem and (1.1):

$$
\boxed{
a'
=
\nu
\int_{\partial A_t}
\partial_\eta m\,dS
+
3
\int_{A_t}
(G-\bar G)m\,dx.
}
\tag{8.2}
$$

where:

$$
\eta
$$

is the outward normal.

---

# 9. Exact selection contrast across a cut

Define:

$$
\boxed{
\langle G\rangle_A
=
\frac1a
\int_A
Gm\,dx,
}
\tag{9.1}
$$

and:

$$
\boxed{
\langle G\rangle_{A^c}
=
\frac1{1-a}
\int_{A^c}
Gm\,dx.
}
\tag{9.2}
$$

Since:

$$
\bar G
=
a\langle G\rangle_A
+
(1-a)
\langle G\rangle_{A^c},
$$

we have:

$$
\boxed{
\int_A
(G-\bar G)m\,dx
=
a(1-a)
\left[
\langle G\rangle_A
-
\langle G\rangle_{A^c}
\right].
}
\tag{9.3}
$$

Therefore:

$$
\boxed{
a'
=
\nu J_A
+
3a(1-a)
\Delta_A G,
}
\tag{9.4}
$$

where:

$$
\boxed{
J_A
=
\int_{\partial A}
\partial_\eta m\,dS,
}
\tag{9.5}
$$

and:

$$
\boxed{
\Delta_A G
=
\langle G\rangle_A
-
\langle G\rangle_{A^c}.
}
\tag{9.6}
$$

---

# 10. Material-cut odds equation

Let:

$$
\boxed{
\ell_A
=
\log
\frac{
a
}{
1-a
}.
}
\tag{10.1}
$$

Then:

$$
\boxed{
\ell_A'
=
\nu
\frac{
J_A
}{
a(1-a)
}
+
3\Delta_A G.
}
\tag{10.2}
$$

Named:

$$
\boxed{
\textbf{Critical-Mass Cut Odds Equation}.
}
$$

Therefore, the relative mass of two critical-mass regions is changed by only two things:

1. diffusive neck flux;
2. selection-rate contrast.

---

# 11. Diffusive neck score

If:

$$
m>0
$$

on:

$$
\Sigma=\partial A,
$$

then:

$$
J_A
=
\int_\Sigma
m\,
\partial_\eta\log m
\,dS.
$$

Define the weighted perimeter:

$$
P_A
=
\int_\Sigma
m\,dS,
$$

and the normal score:

$$
\boxed{
\kappa_1(A)
=
\frac1{P_A}
\int_\Sigma
m
\partial_\eta\log m
\,dS.
}
\tag{11.1}
$$

Therefore:

$$
\boxed{
J_A
=
P_A
\kappa_1(A).
}
\tag{11.2}
$$

Thus, the cut-to-cut communication strength of diffusion has two factors:

$$
\boxed{
\text{neck mass }P_A
\times
\text{normal density score }\kappa_1.
}
$$

Low conductance only suppresses the first factor.

---

# 12. Material weighted-perimeter dynamics

Let:

$$
\Sigma_t=\partial A_t
$$

be smooth, closed, and advected by:

$$
b
$$

By the surface transport theorem:

$$
\frac d{dt}
\int_{\Sigma_t}
m\,dS
=
\int_{\Sigma_t}
\left[
D_t^b m
+
m\operatorname{div}_\Sigma b
\right]dS,
$$

where:

$$
D_t^b
=
\partial_t+b\cdot\nabla.
$$

From (1.1):

$$
D_t^b m
=
\nu\Delta m
+
3(G-\bar G)m
-
m\operatorname{div}b.
$$

and:

$$
\operatorname{div}b
-
\operatorname{div}_\Sigma b
=
\eta^\top(\nabla b)\eta.
$$

Hence:

$$
\boxed{
P_A'
=
\int_{\Sigma}
\left[
\nu\Delta m
+
3(G-\bar G)m
-
m\,
\eta^\top(\nabla b)\eta
\right]dS.
}
\tag{12.1}
$$

---

# 13. Surface diffusion curvature

Let the signed mean curvature be:

$$
\boxed{
H_\Sigma
=
\operatorname{div}\eta.
}
\tag{13.1}
$$

On the surface:

$$
\Delta m
=
\partial_{\eta\eta}m
+
H_\Sigma
\partial_\eta m
+
\Delta_\Sigma m.
$$

On a closed surface:

$$
\int_\Sigma
\Delta_\Sigma m\,dS=0.
$$

Define:

$$
\boxed{
\kappa_2(A)
=
\frac1{P_A}
\int_\Sigma
m
\left[
\partial_{\eta\eta}\log m
+
(\partial_\eta\log m)^2
+
H_\Sigma\partial_\eta\log m
\right]dS.
}
\tag{13.2}
$$

and:

$$
\boxed{
B_n(A)
=
\frac1{P_A}
\int_\Sigma
m
\eta^\top(\nabla b)\eta
\,dS.
}
\tag{13.3}
$$

and the surface selection mean:

$$
\boxed{
G_\Sigma(A)
=
\frac1{P_A}
\int_\Sigma
Gm\,dS.
}
\tag{13.4}
$$

Then:

$$
\boxed{
\frac{P_A'}{P_A}
=
\nu\kappa_2
+
3(G_\Sigma-\bar G)
-
B_n.
}
\tag{13.5}
$$

---

# 14. Exact material-cut conductance law

Assume:

$$
a=\mu(A)\le\frac12.
$$

Define:

$$
\boxed{
\Phi_A
=
\frac{
P_A
}{
a
}.
}
\tag{14.1}
$$

Subtracting (13.5) from:

$$
\frac{a'}a
=
\nu
\Phi_A
\kappa_1
+
3(1-a)
\left[
\langle G\rangle_A
-
\langle G\rangle_{A^c}
\right],
$$

the selection terms simplify exactly to:

$$
G_\Sigma-\langle G\rangle_A.
$$

Therefore:

$$
\boxed{
\frac d{dt}
\log\Phi_A
=
\nu
\left[
\kappa_2
-
\Phi_A\kappa_1
\right]
+
3
\left[
G_\Sigma
-
\langle G\rangle_A
\right]
-
B_n.
}
\tag{14.2}
$$

Named:

$$
\boxed{
\textbf{Material-Cut Conductance Evolution Law}.
}
$$

This is the strongest exact identity of this round.

---

# 15. Three continuous mechanisms for neck collapse

Equation (14.2) indicates that the material cut conductance can decrease via three mechanisms.

## N1 — diffusion-curvature imbalance

$$
\boxed{
\kappa_2
<
\Phi_A\kappa_1.
}
$$

## N2 — selection interior bias

$$
\boxed{
G_\Sigma
<
\langle G\rangle_A.
}
$$

That is, the interior critical mass grows faster than the boundary neck.

## N3 — normal drift deformation

$$
\boxed{
B_n>0.
}
$$

Causing the weighted boundary to be diluted relative to the interior mass.

Therefore:

$$
\boxed{
\textbf{
positive diffusion does not by itself imply monotone conductance.
}
}
$$

---

# 16. Continuous cut profile rather than a single minimizer

The Cheeger constant:

$$
h_Q
$$

is the infimum over all sets.

The minimizing cut may change over time,

therefore, one should not write without evidence:

$$
h_Q'
=
\text{derivative of a single optimizer}.
$$

The correct carrier is the continuous family:

$$
\boxed{
A
\longmapsto
\left(
\mu(A),
P_A,
\kappa_1,
\kappa_2,
G_A,
G_\Sigma,
B_n
\right).
}
\tag{16.1}
$$

or the mass-fraction isoperimetric profile:

$$
\boxed{
\mathscr I_Q(s,t).
}
$$

Optimizer switching is a variational envelope problem,

which is not equivalent to essential discreteness.

---

# 17. Conditional topological reconnection branch

If in some interval:

- the drift coefficients are sufficiently regular;
- the lower-order source is controlled;
- uniform diffusion coefficient:
  $$
  \nu>0;
  $$

then standard uniformly parabolic theory can provide heat-kernel positivity / Gaussian lower-bound type results.

In this regular-coefficient branch,

a non-zero:

$$
m(t_0)
$$

can become a strictly positive density at:

$$
t>t_0
$$

Therefore:

$$
\boxed{
\text{exactly disconnected support}
}
$$

can be eliminated by viscosity.

However, this route cannot unconditionally invoke this branch near:

$$
r=0
$$

when:

$$
b_Q
$$

is uncontrolled.

---

# 18. Strict positivity is not a quantitative conductance bound

Even if:

$$
m(x)>0
\quad
\forall x,
$$

it is still possible that:

$$
\boxed{
h_Q\ll1.
}
$$

Therefore:

$$
\boxed{
\text{topological reconnection}
\neq
\text{quantitative mixing restoration}.
}
\tag{18.1}
$$

Below we provide an explicit continuous probability witness.

---

# 19. Two-Gaussian thin-neck witness

Let:

$$
\phi_s(x)
=
\frac1{
(2\pi s^2)^{3/2}
}
\exp
\left(
-\frac{|x|^2}{2s^2}
\right).
$$

Define:

$$
\boxed{
m_{R,s}(x)
=
\frac12
\phi_s(x-Re_1)
+
\frac12
\phi_s(x+Re_1).
}
\tag{19.1}
$$

For all:

$$
x,
$$

$$
m_{R,s}(x)>0.
$$

Take the cut:

$$
A
=
\{x_1<0\}.
$$

By symmetry:

$$
\mu(A)=\frac12.
$$

The weighted perimeter:

$$
P_A
=
\int_{x_1=0}
m_{R,s}\,dS
$$

is exactly:

$$
\boxed{
P_A
=
\frac1{
\sqrt{2\pi}\,s
}
\exp
\left(
-\frac{
R^2
}{
2s^2
}
\right).
}
\tag{19.2}
$$

Therefore:

$$
\boxed{
h(m_{R,s})
\le
\frac{
2
}{
\sqrt{2\pi}\,s
}
\exp
\left(
-\frac{
R^2
}{
2s^2
}
\right).
}
\tag{19.3}
$$

Thus:

$$
\boxed{
R/s\to\infty
\Longrightarrow
h\to0
}
$$

even if the density is everywhere positive.

---

# 20. Heat smoothing does not give a uniform rapid gap

If we only consider heat evolution:

$$
\partial_tm=\nu\Delta m
$$

starting from:

$$
m_{R,s_0}
$$

then:

$$
s_t^2
=
s_0^2+2\nu t.
$$

Therefore:

$$
\boxed{
h(t)
\le
\frac{
2
}{
\sqrt{2\pi}\,s_t
}
\exp
\left(
-\frac{
R^2
}{
2s_t^2
}
\right).
}
\tag{20.1}
$$

For fixed:

$$
t>0,
$$

letting:

$$
R\to\infty,
$$

we still have:

$$
h(t)\to0.
$$

Therefore:

$$
\boxed{
\textbf{
uniform diffusion can make support positive instantly
without producing a separation-independent conductance lower bound.
}
}
\tag{20.2}
$$

The quantitative reconnection timescale can still become very large depending on:

$$
R^2/\nu
$$

This witness is a heat/probability model, and does not claim to be a Navier–Stokes critical-mass solution itself.

---

# 21. Norm-level data cannot see arbitrary blob separation

Translation-invariant norms:

$$
L^p,
\quad
\dot H^s,
\quad
\text{energy},
\quad
\text{critical amplitudes}
$$

do not inherently record the physical separation between two identical localized structures.

The disjoint gauge-blob witness of Round 23 can also arbitrarily translate the two blobs.

Therefore, we cannot rely solely on:

$$
\boxed{
\text{translation-invariant norm bounds}
}
$$

to expect to deduce a geometry-independent:

$$
\boxed{
h_Q\ge h_\ast>0.
}
$$

We still need genuine:

$$
\boxed{
\text{mixing / localization / interaction geometry}.
}
$$

---

# 22. Selection can compete directly with neck repair

The cut odds equation:

$$
\ell_A'
=
\nu
\frac{
J_A
}{
a(1-a)
}
+
3\Delta_A G
$$

shows:

If:

$$
\boxed{
3|\Delta_A G|
>
\nu
\left|
\frac{
J_A
}{
a(1-a)
}
\right|,
}
\tag{22.1}
$$

then the selection contrast can overpower the diffusive cut exchange at an instantaneous rate.

Therefore, whether viscosity can reconnect the critical mass

cannot be determined solely by:

$$
\nu>0.
$$

We must also compare:

$$
\boxed{
\text{cross-neck diffusion}
\quad\text{vs}\quad
\text{cross-cut growth selection}.
}
$$

---

# 23. Conductance restoration criterion for a material cut

From (14.2), if:

$$
\boxed{
\nu
\left[
\kappa_2
-
\Phi_A\kappa_1
\right]
+
3
\left[
G_\Sigma
-
\langle G\rangle_A
\right]
-
B_n
\ge0,
}
\tag{23.1}
$$

then:

$$
\boxed{
\Phi_A'(t)\ge0.
}
\tag{23.2}
$$

If a uniform lower margin:

$$
\delta_{\rm neck}>0,
$$

can be established for all near-minimizing cuts, then there is hope to deduce the quantitative restoration of:

$$
h_Q
$$

This round has not yet obtained such a uniform estimate.

---

# 24. Conductance X-state

This round can write the critical-mass mixing as:

$$
\boxed{
X_{\rm cond}
=
\left\langle
\mathscr I_Q(s),
h_Q,
\Phi_A,
\kappa_1,
\kappa_2,
\Delta_A G,
G_\Sigma-G_A,
B_n,
\mathcal A_{\rm sel}
\right\rangle.
}
\tag{24.1}
$$

where:

- $s\in(0,1)$;
- $A$ traverses measurable / finite-perimeter cuts;
- all variables are continuous.

This is the geometric expansion of the Round 23 scalar:

$$
C_P
$$

---

# 25. STOP-C28 — Conductance-Restoration / Neck-Selection Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C28}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{critical\text{-}mass\ conductance\ dynamics},
\\
\text{Cheeger\ carrier}
=
h_Q,
\\
\text{isoperimetric\ carrier}
=
\mathscr I_Q(s),
\\
\text{mixing\ rate}
=
\nu h_Q^2/4,
\\
\text{intermittency\ feedback}
=
\mathfrak R_{\rm cond}
=
4\mathcal A_{\rm sel}/(\nu h_Q^2),
\\
\text{material\ cut\ mass}
=
a'
=
\nu J_A
+
3a(1-a)\Delta_A G,
\\
\text{material\ conductance}
=
(\log\Phi_A)'
=
\nu(\kappa_2-\Phi_A\kappa_1)
+
3(G_\Sigma-G_A)
-
B_n,
\\
\text{topological\ reconnection}
\neq
\text{quantitative\ conductance},
\\
\text{strict\ positivity}
\not\Rightarrow
h_Q\ge h_\ast,
\\
\text{missing}
=
\mathrm{uniform\ control\ of\ neck\ diffusion,\ selection\ contrast,
and\ normal\ drift\ deformation},
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
\textbf{STOP-C28:
Critical-Mass Conductance-Restoration / Neck-Selection Gap}.
}
$$

---

# 26. 24/72 Ledger — Round 24

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C307 | weighted perimeter | $\mathsf C$ | variational geometry | relational | $\mathsf F$ | FORM |
| C308 | Cheeger conductance $h_Q$ | $\mathsf C$ | global infimum | scalar | $\mathsf F$ | FORM |
| C309 | isoperimetric profile $\mathscr I_Q(s)$ | $\mathsf C$ | continuous mass fraction | profile | $\mathsf F$ | FORM |
| C310 | Cheeger–Poincaré bridge | $\mathsf C$ | global measure geometry | scalar | $\mathsf F$ | STANDARD |
| C311 | conductance feedback ODE | $\mathsf C$ | feedback | scalar | $\mathsf F$ | PROVED conditionally |
| C312 | scale-invariant $\mathfrak R_{\rm cond}$ | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C313 | material cut mass law | $\mathsf C$ | transport/diffusion | relational | $\mathsf F$ | EXACT |
| C314 | selection contrast identity | $\mathsf C$ | measure | scalar | $\mathsf F$ | EXACT |
| C315 | cut odds equation | $\mathsf C$ | transport/selection | scalar | $\mathsf F$ | EXACT |
| C316 | material weighted-perimeter law | $\mathsf C$ | surface transport | relational | $\mathsf F$ | EXACT |
| C317 | surface diffusion curvature | $\mathsf C$ | surface geometry | $\mathsf X$ | $\mathsf F$ | EXACT |
| C318 | material-cut conductance law | $\mathsf C$ | coupled | targeted | $\mathsf F$ | EXACT |
| C319 | regular-coefficient positivity branch | $\mathsf C$ | parabolic smoothing | scalar | $\mathsf F$ | CONDITIONAL |
| C320 | positivity $\Rightarrow$ uniform conductance | $\mathsf C$ | measure geometry | scalar | $\mathsf F$ | REFUTED |
| C321 | two-Gaussian thin-neck witness | $\mathsf C$ | smooth density | relational | $\mathsf F$ | CONSTRUCTED |
| C322 | diffusion-only uniform rapid restoration | $\mathsf C$ | heat flow | targeted | $\mathsf F$ | REFUTED by separation family |
| C323 | uniform NS neck-restoration estimate | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C28 |

---

# 27. Continuous-versus-discrete status

Conductance is most commonly depicted as a graph in numerical / Markov-chain language.

However, this round entirely uses:

- continuous probability density;
- finite-perimeter measurable sets;
- continuous mass fraction:
  $$
  s\in(0,1);
  $$
- continuous weighted surface measure;
- continuous surface transport.

There are no:

- graph vertices;
- cluster labels;
- component enumeration;
- discrete transition matrix.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{27.1}
$$

If in the future, for numerical computation, we discretize:

$$
\mathscr I_Q(s)
$$

into graph conductance,

that is primarily just a numerical representation.

Unless it is proven that the continuous cut profile cannot carry the information required for closure,

it does not count as an essential:

$$
\mathsf C\to\mathsf D.
$$

---

# 28. Strongest results of Round 24

## R24-A — Conductance feedback rate

$$
\boxed{
y'
\le
-\frac{
\nu h_Q^2
}{4}
y
+
\frac12(1+y^2)\mathcal A_{\rm sel}.
}
$$

## R24-B — Exact cut odds dynamics

$$
\boxed{
\ell_A'
=
\nu\frac{J_A}{a(1-a)}
+
3\Delta_A G.
}
$$

## R24-C — Exact material-cut conductance dynamics

$$
\boxed{
(\log\Phi_A)'
=
\nu(\kappa_2-\Phi_A\kappa_1)
+
3(G_\Sigma-G_A)
-
B_n.
}
$$

## R24-D — Positivity is not mixing

$$
\boxed{
m>0
\not\Rightarrow
h_Q\ge h_\ast.
}
$$

## R24-E — Heat alone has a separation timescale

two-Gaussian model:

$$
\boxed{
h(t)
\lesssim
s_t^{-1}
\exp
\left(
-\frac{R^2}{2s_t^2}
\right),
\qquad
s_t^2=s_0^2+2\nu t.
}
$$

Therefore, a large separation can make conductance restoration very slow.

---

# 29. Next round — Nonlocal Cross-Blob Coupling

Round 24 shows:

$$
\boxed{
\text{local diffusion}
}
$$

cannot alone provide a separation-independent gap.

But Navier–Stokes is not just local diffusion.

It also has:

- Biot–Savart velocity coupling;
- pressure Hessian;
- incompressibility;
- global quotient gauge.

So the next round directly tests:

$$
\boxed{
\textbf{
Can nonlocal NS coupling provide a virtual connection
when critical mass has a thin or almost-empty neck?
}
}
$$

Core questions:

1. Even if two high-mass blobs have:
   $$
   h_Q\ll1,
   $$
   the pressure / velocity field still acts across space;

2. Split the source contrast:
   $$
   \Delta_A G
   $$
   into local and nonlocal cross-blob contributions;

3. Check whether nonlocal pressure tends to synchronize the growth rates of the two blobs or instead can increase the selection contrast;

4. Define a continuous cross-interaction kernel without establishing a blob graph;

5. If the kernel interaction decays with an algebraic tail at large separation, while the conductance decays with a Gaussian/exponential neck, then a new regime may emerge:
   $$
   \boxed{
   \text{nonlocal coupling dominates local neck communication}
   }
   $$

6. This will reconnect back to the pressure nonlocality of Round 04, but re-attacked using conductance language.

---

# 30. External primary-source anchors

1. Sergey G. Bobkov, Michel Ledoux, *Weighted Poincaré-type inequalities for Cauchy and other convex measures*, arXiv:0906.1651.
   - Background on weighted Poincaré / Cheeger-type measure geometry;
   - The conductance-to-Poincaré route used in this round belongs to the classical weighted isoperimetric/spectral framework.

2. D. Kinzebulatov, Yu. A. Semenov, *Heat kernel bounds for parabolic equations with singular (form-bounded) vector fields*, arXiv:2103.11482.
   - Background on Gaussian heat-kernel lower/upper bounds for uniformly elliptic parabolic equations under appropriate drift/divergence assumptions;
   - This round only uses it to support the external background that "the regular-coefficient branch can have positivity / Gaussian propagation", without unconditionally applying its assumptions to $b_Q$.

The material-cut mass law, odds law, weighted-perimeter dynamics, material-cut conductance law, and two-Gaussian thin-neck witness in this round are all directly derived in this document.

---

# 31. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Critical\text{-}Mass\ Conductance\ Dynamics},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Connectivity carrier}
&=
\mathscr I_Q(s),\ h_Q,
\\
\text{Mixing rate}
&=
\nu h_Q^2/4,
\\
\text{Mass cut dynamics}
&=
\mathrm{diffusive\ neck\ flux}
+
\mathrm{selection\ contrast},
\\
\text{Conductance dynamics}
&=
\mathrm{diffusion\ curvature}
+
\mathrm{surface/interior\ selection}
+
\mathrm{normal\ drift},
\\
\text{Positivity}
&\neq
\mathrm{uniform\ spectral\ gap},
\\
\text{Diffusion-only restoration}
&=
\mathrm{separation\ dependent},
\\
\text{STOP-C28}
&=
\mathrm{Conductance\text{-}Restoration/Neck\text{-}Selection\ Gap},
\\
\text{Next}
&=
\mathrm{Nonlocal\ Cross\text{-}Blob\ Coupling}.
\end{aligned}
}
$$