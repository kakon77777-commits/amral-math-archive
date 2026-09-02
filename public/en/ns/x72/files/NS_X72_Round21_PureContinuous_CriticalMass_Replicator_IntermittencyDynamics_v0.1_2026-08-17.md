# NS × X Integral × 24/72 Paradigm in Practice
## Round 21 — Pure Continuous Critical-Mass Replicator / Dynamic Intermittency Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Dynamic-Intermittency Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round20_PureContinuous_LowAmplitude_DegeneracyIntermittency_v0.1_2026-08-16.md`
- This round's objective: No longer merely study the location of the low-amplitude set. Directly study the deterministic dynamics of the critical quotient mass
  $$
  d\mu_Q=\frac{|v|^3}{Q^3}dx
  $$
  and the normalized strain rate
  $$
  K_S=\frac{|S|}{|v|}.
  $$
  Establish the critical-mass transport–diffusion–selection equation, rewrite the normalized-strain intermittency ratio from Round 20 as a $\chi^2$ separation of two probability measures, and identify the exact competition between diffusion anti-intermittency and NS relative-source production.
- Non-claims: This round does not prove that the intermittency ratio decreases unconditionally. On the contrary, this round proves that common diffusion possesses an exact anti-separation term, but the Navier–Stokes strain dynamics provide additional selection / relative-source terms, the signs of which have not yet been controlled.

---

# 0. Round 20 handoff

Let:

$$
Q
=
\mathfrak Q_3[u],
$$

optimal representative:

$$
v=u+\nabla q,
$$

$$
r=|v|,
$$

$$
n=\frac v{|v|}
$$

for:

$$
r>0.
$$

Round 20 defines the critical quotient probability measure:

$$
\boxed{
d\mu_Q
=
\frac{r^3}{Q^3}dx,
}
\tag{0.1}
$$

and the normalized strain rate:

$$
\boxed{
K_S
=
\frac{|S|}{r}.
}
\tag{0.2}
$$

and proves:

$$
\boxed{
W_S
=
Q^3
\mathbb E_{\mu_Q}[K_S^2],
}
\tag{0.3}
$$

and:

$$
\boxed{
\mathcal I_0
=
Q^3
\mathbb E_{\mu_Q}[K_S^4].
}
\tag{0.4}
$$

intermittency ratio:

$$
\boxed{
\mathfrak J_S
=
\frac{
\mathbb E_{\mu_Q}[K_S^4]
}{
\mathbb E_{\mu_Q}[K_S^2]^2
}
\ge1.
}
\tag{0.5}
$$

Round 20 STOP:

$$
\boxed{
\text{STOP-C24}
=
\text{Normalized-Deformation Intermittency / Zero-Set Degeneracy Gap}.
}
$$

This round asks:

$$
\boxed{
\text{Does NS dynamics itself suppress or create }\mathfrak J_S?
}
$$

---

# 1. Optimal representative evolution

Round 14–20 representative equation:

$$
\boxed{
\partial_t v
+
\mathcal L_u^{(1)}v
=
\nu\Delta v
+
\nabla\chi_g,
}
\tag{1.1}
$$

where:

$$
\mathcal L_u^{(1)}v
=
(u\cdot\nabla)v
+
(\nabla u)^\top v,
$$

and:

$$
\chi_g
$$

is the scalar gauge-maintenance potential required to maintain the current optimal nonlinear gauge:

$$
\operatorname{div}(rv)=0.
$$

Denote:

$$
\boxed{
\gamma_Q
=
-
n^\top S_un.
}
\tag{1.2}
$$

---

# 2. Exact amplitude equation

Pair (1.1) with:

$$
n=\frac v{|v|}.
$$

Using:

$$
n^\top(\nabla u)^\top n
=
n^\top S_un
=
-\gamma_Q,
$$

and:

$$
n\cdot\Delta v
=
\Delta r
-
r|\nabla n|^2,
$$

we obtain:

$$
\boxed{
(\partial_t+u\cdot\nabla)r
=
\nu\Delta r
-
\nu r|\nabla n|^2
+
\gamma_Q r
+
n\cdot\nabla\chi_g.
}
\tag{2.1}
$$

Therefore, the quotient amplitude co-evolves through:

- viscosity;
- direction turning;
- compressive strain;
- dynamic gauge maintenance.

---

# 3. Exact critical-mass density equation

Let:

$$
\boxed{
\rho_Q
=
r^3.
}
\tag{3.1}
$$

Define the local normalized-Hodge dissipation rate:

$$
\boxed{
K_D
=
\frac{
|\nabla v|^2+|\nabla r|^2
}{
r^2
}
}
\tag{3.2}
$$

for:

$$
r>0.
$$

By the convex chain rule:

$$
r\,v\cdot\Delta v
=
\frac13\Delta(r^3)
-
r
\left(
|\nabla v|^2+|\nabla r|^2
\right).
$$

Moreover, the nonlinear gauge:

$$
\operatorname{div}(rv)=0
$$

gives:

$$
rv\cdot\nabla\chi_g
=
\operatorname{div}(\chi_g rv).
$$

Therefore:

$$
\boxed{
\begin{aligned}
\partial_t\rho_Q
+
\operatorname{div}(u\rho_Q)
={}&
\nu\Delta\rho_Q
\\
&+
3
\left(
\gamma_Q-\nu K_D
\right)
\rho_Q
\\
&+
3\operatorname{div}(\chi_g rv).
\end{aligned}
}
\tag{3.3}
$$

---

# 4. Effective deterministic critical-mass drift

For:

$$
r>0
$$

define:

$$
\boxed{
b_Q
=
u
-
3
\frac{
\chi_g
}{
r
}
n.
}
\tag{4.1}
$$

Since:

$$
\rho_Q
\left(
-3\frac{\chi_g}{r}n
\right)
=
-3\chi_g r^2n
=
-3\chi_g rv,
$$

(3.3) can be written as:

$$
\boxed{
\partial_t\rho_Q
+
\operatorname{div}(b_Q\rho_Q)
=
\nu\Delta\rho_Q
+
3G_Q\rho_Q,
}
\tag{4.2}
$$

where:

$$
\boxed{
G_Q
=
\gamma_Q-\nu K_D.
}
\tag{4.3}
$$

Note that:

$$
b_Q
$$

can appear singular in its normalized representation as:

$$
r\to0,
$$

but the original physical gauge flux:

$$
-3\chi_g rv
=
-3\chi_g r^2n
$$

actually degenerates with $r^2$ when $\chi_g$ is bounded.

Thus:

$$
\boxed{
\text{singular normalized drift}
\neq
\text{automatically singular physical flux}.
}
\tag{4.4}
$$

---

# 5. Exact logarithmic critical-quotient growth rate

Since:

$$
Q^3
=
\int\rho_Qdx,
$$

integrating (4.2) yields:

$$
\boxed{
\frac d{dt}Q^3
=
3Q^3
\mathbb E_{\mu_Q}[G_Q].
}
\tag{5.1}
$$

Thus:

$$
\boxed{
\frac d{dt}
\log Q
=
\mathbb E_{\mu_Q}[G_Q].
}
\tag{5.2}
$$

Named:

$$
\boxed{
\textbf{Critical-Mass Mean-Growth Identity}.
}
$$

That is:

> The logarithmic growth of the critical quotient norm is exactly the average of the local growth field $G_Q$ under the critical mass distribution.

---

# 6. Normalized critical-mass replicator–diffusion equation

Let:

$$
m_Q
=
\frac{
\rho_Q
}{
Q^3
}
$$

be the Lebesgue density of $\mu_Q$.

From (4.2) and (5.1):

$$
\boxed{
\partial_t m_Q
+
\operatorname{div}(b_Qm_Q)
=
\nu\Delta m_Q
+
3
\left(
G_Q-\overline G_Q
\right)m_Q,
}
\tag{6.1}
$$

where:

$$
\boxed{
\overline G_Q
=
\mathbb E_{\mu_Q}[G_Q].
}
\tag{6.2}
$$

This is a deterministic:

$$
\boxed{
\text{transport}
+
\text{diffusion}
+
\text{replicator/selection}
}
$$

equation.

The term "replicator" merely describes the mathematical form in which normalized mass is relatively amplified in regions with above-average growth.

It does not introduce any stochastic physical state.

---

# 7. 24/72 classification audit — probability does not imply stochastic transition

Equation (6.1) uses the probability density:

$$
m_Q.
$$

However:

$$
m_Q
$$

is a normalized structural observable of a single deterministic Navier–Stokes state:

$$
u(t).
$$

Given:

$$
u(t),
$$

$$
m_Q(t)
$$

is uniquely determined.

Therefore, in this round:

$$
\boxed{
L=\mathsf F
}
$$

still holds.

We cannot, just because it is written as:

$$
\text{Fokker–Planck-like}
$$

or in probability-measure language,

surreptitiously replace the 72 transition-law axis with:

$$
\mathsf K.
$$

Thus:

$$
\boxed{
\textbf{
probability representation
does not imply stochastic transition law.
}
}
\tag{7.1}
$$

This is a consistency check for the 24/72 framework itself in this round.

---

# 8. Exact observable covariance law

For a smooth time-dependent scalar observable:

$$
\phi(x,t),
$$

by integration by parts on (6.1):

$$
\boxed{
\begin{aligned}
\frac d{dt}
\mathbb E_{\mu_Q}[\phi]
={}&
\mathbb E_{\mu_Q}
\left[
\partial_t\phi
+
b_Q\cdot\nabla\phi
+
\nu\Delta\phi
\right]
\\
&+
3
\operatorname{Cov}_{\mu_Q}
(\phi,G_Q).
\end{aligned}
}
\tag{8.1}
$$

Therefore, the structural selection of the critical mass is precisely controlled by:

$$
\boxed{
\operatorname{Cov}_{\mu_Q}
(\phi,G_Q).
}
$$

If the observable is larger in high-growth regions, the selection will increase its normalized expectation.

---

# 9. Critical-mass entropy balance

Define the Shannon-type entropy in the smooth positive-density regime:

$$
\boxed{
\mathscr H_Q
=
-
\int
m_Q\log m_Q\,dx.
}
\tag{9.1}
$$

From (6.1):

$$
\boxed{
\begin{aligned}
\mathscr H_Q'
={}&
\mathbb E_{\mu_Q}
[
\operatorname{div}b_Q
]
\\
&+
\nu
\int
|\nabla\log m_Q|^2
d\mu_Q
\\
&-
3
\operatorname{Cov}_{\mu_Q}
(
\log m_Q,
G_Q
).
\end{aligned}
}
\tag{9.2}
$$

The three terms are:

1. deterministic drift compression / expansion;
2. positive Fisher-information diffusion;
3. growth-selection concentration / deconcentration.

So viscosity indeed provides anti-concentration entropy production,

but:

$$
\boxed{
\text{entropy is not automatically monotone}
}
$$

because the gauge drift and selection covariance do not have a universal sign.

---

# 10. Strain-energy probability measure

Assume:

$$
W_S
=
\int
r|S|^2dx
>0.
$$

Define the weighted strain-energy measure:

$$
\boxed{
d\nu_S
=
\frac{
r|S|^2
}{
W_S
}
dx.
}
\tag{10.1}
$$

From:

$$
d\mu_Q
=
\frac{
r^3
}{
Q^3
}
dx,
$$

we have:

$$
\boxed{
\frac{
d\nu_S
}{
d\mu_Q
}
=
\frac{
K_S^2
}{
\mathbb E_{\mu_Q}[K_S^2]
}.
}
\tag{10.2}
$$

Let:

$$
\boxed{
f_S
=
\frac{
d\nu_S
}{
d\mu_Q
}.
}
\tag{10.3}
$$

Then:

$$
\mathbb E_{\mu_Q}[f_S]=1.
$$

---

# 11. Intermittency is exactly a $\chi^2$ measure separation

In Round 20:

$$
\mathfrak J_S
=
\frac{
\mathbb E[K_S^4]
}{
\mathbb E[K_S^2]^2
}.
$$

From (10.2):

$$
\boxed{
\mathfrak J_S
=
\int
f_S^2
d\mu_Q.
}
\tag{11.1}
$$

Thus, the Pearson $\chi^2$ divergence:

$$
\chi^2
(\nu_S\|\mu_Q)
=
\int
(f_S-1)^2d\mu_Q
$$

satisfies:

$$
\boxed{
\mathfrak J_S-1
=
\chi^2
(\nu_S\|\mu_Q).
}
\tag{11.2}
$$

Named:

$$
\boxed{
\textbf{Intermittency–Measure-Separation Identity}.
}
$$

Therefore, the normalized-deformation intermittency from Round 20 has a very direct meaning:

> How much the strain-weighted energy measure and the critical quotient-mass measure are separated from each other.

---

# 12. Anti-concentration inequality

For any measurable set:

$$
A,
$$

by Cauchy–Schwarz:

$$
\nu_S(A)
=
\int_A
f_Sd\mu_Q
$$

$$
\le
\mu_Q(A)^{1/2}
\left(
\int_A
f_S^2d\mu_Q
\right)^{1/2}.
$$

Therefore:

$$
\boxed{
\nu_S(A)^2
\le
\mathfrak J_S
\mu_Q(A).
}
\tag{12.1}
$$

Thus, if a set carries a fixed fraction:

$$
\nu_S(A)\ge\beta>0,
$$

then:

$$
\boxed{
\mathfrak J_S
\ge
\frac{
\beta^2
}{
\mu_Q(A)
}.
}
\tag{12.2}
$$

Named:

$$
\boxed{
\textbf{Critical-Mass Anti-Concentration Inequality}.
}
$$

---

# 13. Low-amplitude escape becomes measure singularization

Let:

$$
A_\eta
=
\{
0<r<\eta
\}.
$$

If there exists:

$$
\eta_j\downarrow0
$$

such that:

$$
\mu_Q(A_{\eta_j})
\to0
$$

but:

$$
\nu_S(A_{\eta_j})
\ge
\beta>0,
$$

then by (12.2):

$$
\boxed{
\mathfrak J_S
\to\infty.
}
\tag{13.1}
$$

Therefore, near-zero strain escape is equivalent to:

$$
\boxed{
\text{strain-energy measure becomes singularly concentrated
relative to critical quotient mass}.
}
$$

If the exact-zero set:

$$
\{r=0,\ |S|>0\}
$$

itself has a relevant singular contribution,

then the Round 20 convention directly gives:

$$
\mathcal I_0=+\infty,
$$

which belongs to the stronger Z0 branch.

---

# 14. Effective critical-mass participation fraction

Define:

$$
\boxed{
\mathfrak m_{\rm eff}
=
\frac1{\mathfrak J_S}.
}
\tag{14.1}
$$

Since:

$$
\mathfrak J_S\ge1,
$$

we have:

$$
0<\mathfrak m_{\rm eff}\le1.
$$

It can be viewed as an inverse-participation fraction of the strain energy relative to the critical mass.

A large:

$$
\mathfrak J_S
$$

implies:

$$
\mathfrak m_{\rm eff}
\ll1.
$$

That is, the dangerous normalized strain occupies only a very small amount of the quotient-critical mass.

---

# 15. Continuous moment-order field

For real:

$$
p\ge0
$$

define:

$$
\boxed{
\mathcal M_p
=
\int
r^{3-p}
|S|^pdx
=
Q^3
\mathbb E_{\mu_Q}
[K_S^p].
}
\tag{15.1}
$$

Special values:

$$
\boxed{
\mathcal M_0=Q^3,
}
$$

$$
\boxed{
\mathcal M_2=W_S,
}
$$

$$
\boxed{
\mathcal M_4=\mathcal I_0.
}
$$

Therefore, the so-called second/fourth moments in Round 20 do not need to be treated as two discrete moment orders.

They are actually two slices of a continuous:

$$
\boxed{
p\in[0,\infty)
}
$$

moment-order field.

---

# 16. Continuous moment convexity

Let:

$$
F(p)
=
\log
\mathbb E_{\mu_Q}
[K_S^p]
$$

where the moments are finite and logarithmic differentiation is valid.

Define the $p$-tilted measure:

$$
\boxed{
d\mu_p
=
\frac{
K_S^p
}{
\mathbb E_{\mu_Q}[K_S^p]
}
d\mu_Q.
}
\tag{16.1}
$$

Then:

$$
\boxed{
F'(p)
=
\mathbb E_{\mu_p}
[
\log K_S
],
}
\tag{16.2}
$$

and:

$$
\boxed{
F''(p)
=
\operatorname{Var}_{\mu_p}
(
\log K_S
)
\ge0.
}
\tag{16.3}
$$

Therefore, the moment-order geometry itself is convex.

---

# 17. Intermittency as continuous moment-space curvature

Since:

$$
F(0)=0,
$$

we have:

$$
\log\mathfrak J_S
=
F(4)-2F(2)+F(0).
$$

Thus:

$$
\boxed{
\log\mathfrak J_S
=
\int_0^2
\int_s^{s+2}
F''(\tau)
\,d\tau\,ds.
}
\tag{17.1}
$$

Substituting (16.3):

$$
\boxed{
\log\mathfrak J_S
=
\int_0^2
\int_s^{s+2}
\operatorname{Var}_{\mu_\tau}
(
\log K_S
)
\,d\tau\,ds.
}
\tag{17.2}
$$

Named:

$$
\boxed{
\textbf{Continuous Moment-Curvature Identity}.
}
$$

Thus, intermittency is not a discrete phenomenon like "fourth order minus second order".

It is:

$$
\boxed{
\text{statistical curvature of the normalized deformation rate along the continuous moment order }p.
}
$$

---

# 18. Exact common-Markov anti-separation lemma

Consider two probability densities:

$$
m_1,
\qquad
m_2
$$

If they both obey only the same deterministic drift–diffusion:

$$
\partial_t m_j
+
\operatorname{div}(b m_j)
=
\nu\Delta m_j,
$$

let:

$$
f=\frac{m_2}{m_1}.
$$

then direct calculation yields:

$$
\boxed{
\frac d{dt}
\int
f^2m_1dx
=
-2\nu
\int
m_1
|\nabla f|^2dx
\le0.
}
\tag{18.1}
$$

Therefore:

$$
\boxed{
\textbf{
common deterministic transport does not create }\chi^2\textbf{ separation,
and common viscosity strictly dissipates it.
}
}
$$

This is a direct PDE calculation and does not require a stochastic ontology.

---

# 19. Actual strain measure does not follow the same generator

The weighted strain density:

$$
\zeta_S
=
r|S|^2
$$

is not only transported/diffused by:

$$
b_Q,
\qquad
\nu.
$$

The strain equation:

$$
(\partial_t+u\cdot\nabla)S
=
\nu\Delta S
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
\nabla^2p
$$

additionally generates:

- strain self-interaction;
- vorticity–strain coupling;
- local pressure-Hessian contraction;
- cross-diffusion between $r$ and $|S|^2$;
- gauge-maintenance terms.

Thus, define the exact relative-source rate:

$$
\boxed{
\mathcal R_S
=
\frac1{\zeta_S}
\left[
\partial_t\zeta_S
+
\operatorname{div}(b_Q\zeta_S)
-
\nu\Delta\zeta_S
\right]
-
3G_Q
}
\tag{19.1}
$$

for:

$$
\zeta_S>0.
$$

This is not an approximation.

It is the exact definition of "all the additional sources of the weighted strain density relative to the critical-mass common generator".

---

# 20. Normalized strain-measure equation

Let:

$$
m_S
=
\frac{
\zeta_S
}{
W_S
}
$$

be the density of $\nu_S$.

From (19.1), its normalized equation can be written as:

$$
\boxed{
\begin{aligned}
\partial_t m_S
+
\operatorname{div}(b_Qm_S)
={}&
\nu\Delta m_S
\\
&+
\left[
3G_Q+\mathcal R_S
-
\overline C_S
\right]
m_S,
\end{aligned}
}
\tag{20.1}
$$

where:

$$
\boxed{
\overline C_S
=
\mathbb E_{\nu_S}
[
3G_Q+\mathcal R_S
].
}
\tag{20.2}
$$

Therefore, $\mu_Q$ and $\nu_S$:

- share deterministic drift;
- share viscosity;
- differ in normalized selection/source structure.

---

# 21. Exact dynamic intermittency equation

Let:

$$
f_S
=
\frac{
m_S
}{
m_Q
}.
$$

Direct calculation from (6.1) and (20.1) yields:

$$
\boxed{
\begin{aligned}
\mathfrak J_S'
={}&
-2\nu
\int
m_Q
|\nabla f_S|^2dx
\\
&+
\int
f_S^2
\Big[
3G_Q
+
2\mathcal R_S
-
2\overline C_S
+
3\overline G_Q
\Big]
d\mu_Q.
\end{aligned}
}
\tag{21.1}
$$

where:

$$
\overline G_Q
=
\mathbb E_{\mu_Q}[G_Q].
$$

Define:

$$
\boxed{
\mathcal F_{\rm rel}
=
\int
m_Q|\nabla f_S|^2dx
}
\tag{21.2}
$$

and:

$$
\boxed{
\mathcal P_{\rm sel}
=
\int
f_S^2
\Big[
3G_Q
+
2\mathcal R_S
-
2\overline C_S
+
3\overline G_Q
\Big]
d\mu_Q.
}
\tag{21.3}
$$

Then:

$$
\boxed{
\mathfrak J_S'
=
-2\nu
\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}.
}
\tag{21.4}
$$

Named:

$$
\boxed{
\textbf{Dynamic Intermittency Balance}.
}
$$

---

# 22. Interpretation of the dynamic intermittency balance

The first term:

$$
\boxed{
-2\nu\mathcal F_{\rm rel}\le0
}
$$

is the exact relative Fisher-information dissipation.

It will remix:

$$
\nu_S
$$

and:

$$
\mu_Q.
$$

The second term:

$$
\boxed{
\mathcal P_{\rm sel}
}
$$

collects:

- critical-mass growth selection;
- strain-specific nonlinear source;
- pressure-Hessian source;
- gauge/source mismatch.

Therefore:

$$
\boxed{
\textbf{
intermittency can grow only if relative NS selection/source production
beats common viscous mixing.
}
}
\tag{22.1}
$$

This is the most important dynamic reduction of this round.

---

# 23. Conditional anti-intermittency branch

If on the interval:

$$
I
$$

we have:

$$
\boxed{
\mathcal P_{\rm sel}
\le
2\nu
\mathcal F_{\rm rel},
}
\tag{23.1}
$$

then:

$$
\boxed{
\mathfrak J_S'
\le0.
}
\tag{23.2}
$$

Stronger yet, if:

$$
\mathcal P_{\rm sel}
\le
(2-\delta)\nu
\mathcal F_{\rm rel}
$$

for:

$$
\delta>0,
$$

then:

$$
\boxed{
\mathfrak J_S'
\le
-\delta\nu
\mathcal F_{\rm rel}.
}
\tag{23.3}
$$

Therefore, the dynamic intermittency closure has been compressed into:

$$
\boxed{
\text{selection/source production}
\quad\text{versus}\quad
\text{relative Fisher mixing}.
}
$$

---

# 24. Why diffusion alone is not enough

Equation (21.4) simultaneously answers the question from Round 20.

Common viscosity indeed possesses an exact self-regularizing mechanism:

$$
-2\nu\mathcal F_{\rm rel}.
$$

But the full NS also has:

$$
\mathcal P_{\rm sel},
$$

which has no universal sign.

Therefore:

$$
\boxed{
\text{viscous anti-concentration exists,
but it is not by itself a global regularity proof}.
}
$$

What is truly missing is:

$$
\boxed{
\mathcal P_{\rm sel}
\stackrel{?}{\le}
2\nu\mathcal F_{\rm rel}
}
$$

or its time-integrated weaker version.

---

# 25. A new representation-stable interpretation of intermittency

In Round 20:

$$
\mathfrak J_S
$$

appears to be just a moment ratio.

Round 21 provides three equivalent perspectives:

$$
\boxed{
\begin{aligned}
\mathfrak J_S
&=
\frac{
\mathbb E[K_S^4]
}{
\mathbb E[K_S^2]^2}
\\
&=
1+\chi^2(\nu_S\|\mu_Q)
\\
&=
\exp
\left[
\int_0^2
\int_s^{s+2}
\operatorname{Var}_{\mu_\tau}
(\log K_S)
d\tau ds
\right].
\end{aligned}
}
\tag{25.1}
$$

Therefore, normalized-deformation intermittency is simultaneously:

- a moment gap;
- a measure separation;
- a continuous moment-space curvature.

This already possesses quite strong representation stability.

---

# 26. STOP-C25 — Relative-Source / Critical-Mass Separation Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C25}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{dynamic\ critical\ mass/intermittency},
\\
\text{critical\ mass\ PDE}
=
\mathrm{deterministic\ transport+diffusion+selection},
\\
\text{quotient\ growth}
=
\overline G_Q,
\\
\text{intermittency}
=
1+\chi^2(\nu_S\|\mu_Q),
\\
\text{common\ viscosity}
=
-2\nu\mathcal F_{\rm rel},
\\
\text{relative\ NS\ production}
=
\mathcal P_{\rm sel},
\\
\text{exact\ balance}
=
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel},
\\
\text{missing}
=
\mathrm{unconditional\ domination\ of\ relative\ production\ by\ viscous\ mixing},
\\
\text{probability\ representation}
\neq
\text{stochastic\ law},
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
\textbf{STOP-C25:
Relative-Source / Critical-Mass Separation Gap}.
}
$$

---

# 27. 24/72 Ledger — Round 21

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C259 | amplitude equation | $\mathsf C$ | transport/elliptic | relational | $\mathsf F$ | EXACT |
| C260 | critical-mass density $\rho_Q$ | $\mathsf C$ | continuous measure | targeted | $\mathsf F$ | FORM |
| C261 | deterministic critical-mass PDE | $\mathsf C$ | $\mathsf S+\mathsf P$ | $\mathsf X$ | $\mathsf F$ | EXACT |
| C262 | mean growth identity | $\mathsf C$ | recognition | scalar | $\mathsf F$ | EXACT |
| C263 | normalized replicator–diffusion | $\mathsf C$ | continuous selection | measure | $\mathsf F$ | EXACT |
| C264 | probability $\Rightarrow\mathsf K$ | — | — | — | — | REFUTED as classification inference |
| C265 | observable covariance law | $\mathsf C$ | selection | relational | $\mathsf F$ | EXACT |
| C266 | critical-mass entropy balance | $\mathsf C$ | diffusion/selection | scalar | $\mathsf F$ | EXACT under smoothness |
| C267 | strain-energy measure $\nu_S$ | $\mathsf C$ | measure | $\mathsf X$ | $\mathsf F$ | FORM |
| C268 | intermittency–$\chi^2$ identity | $\mathsf C$ | recognition | scalar | $\mathsf F$ | EXACT |
| C269 | anti-concentration inequality | $\mathsf C$ | measure geometry | targeted | $\mathsf F$ | PROVED |
| C270 | continuous moment field $\mathcal M_p$ | $\mathsf C$ | continuous $p$ | profile | $\mathsf F$ | FORM |
| C271 | moment-curvature identity | $\mathsf C$ | exponential tilt | profile | $\mathsf F$ | EXACT |
| C272 | common-Markov anti-separation | $\mathsf C$ | drift/diffusion | scalar | $\mathsf F$ | PROVED |
| C273 | strain relative-source $\mathcal R_S$ | $\mathsf C$ | nonlinear NS | $\mathsf X$ | $\mathsf F$ | EXACT DEFINITION |
| C274 | dynamic intermittency balance | $\mathsf C$ | measure coupling | scalar | $\mathsf F$ | EXACT |
| C275 | unconditional $\mathcal P_{\rm sel}\le2\nu\mathcal F_{\rm rel}$ | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C25 |

---

# 28. Continuous-versus-discrete status

This round appears most susceptible to being misjudged as "discrete/stochastic":

- probability measure;
- replicator;
- Fokker–Planck-like diffusion;
- moment hierarchy.

However:

1. the measure comes from a single deterministic state;
2. the transition is still determined by the NS deterministic PDE;
3. the moment order has been elevated to:
   $$
   p\in[0,\infty);
   $$
4. concentration is described by continuous measure divergence.

Therefore:

$$
\boxed{
B=\mathsf C,
\qquad
L=\mathsf F,
}
$$

is still maintained.

Thus:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{28.1}
$$

---

# 29. Strongest results of Round 21

## R21-A — deterministic critical-mass replicator equation

$$
\boxed{
\partial_t m_Q
+
\operatorname{div}(b_Qm_Q)
=
\nu\Delta m_Q
+
3(G_Q-\bar G_Q)m_Q.
}
$$

## R21-B — exact critical growth rate

$$
\boxed{
(\log Q)'
=
\mathbb E_{\mu_Q}[G_Q].
}
$$

## R21-C — intermittency is measure separation

$$
\boxed{
\mathfrak J_S-1
=
\chi^2(\nu_S\|\mu_Q).
}
$$

## R21-D — concentration witness

$$
\boxed{
\nu_S(A)^2
\le
\mathfrak J_S\mu_Q(A).
}
$$

## R21-E — continuous moment curvature

$$
\boxed{
\log\mathfrak J_S
=
\int_0^2\int_s^{s+2}
\operatorname{Var}_{\mu_\tau}(\log K_S)
\,d\tau ds.
}
$$

## R21-F — dynamic intermittency balance

$$
\boxed{
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}.
}
$$

Therefore, viscosity indeed provides an exact anti-intermittency mechanism,

but the NS relative source may still defeat it.

---

# 30. Next round — relative-source decomposition

The next round will no longer study:

$$
\mathfrak J_S
$$

as an abstract ratio.

It will directly expand:

$$
\boxed{
\mathcal R_S
}
$$

and:

$$
\boxed{
\mathcal P_{\rm sel}.
}
$$

Core questions:

1. Decompose the relative source into:
   $$
   \text{strain self-amplification}
   +
   \text{vorticity coupling}
   +
   \text{pressure Hessian}
   +
   \text{cross diffusion}
   +
   \text{gauge maintenance};
   $$

2. Check which terms have exact cancellation in the $\chi^2$ balance;

3. Whether the pressure Hessian can once again be eliminated by global/quotient projection;

4. Whether the dangerous middle-strain channel exactly appears in the positive relative selection term;

5. If the remaining $\mathcal P_{\rm sel}$ can be upper-bounded by the Round 05 / Round 19 confluence carriers, it may form the first true self-closing feedback loop;

6. Still maintain continuous measures, without making particle / atom approximations.

---

# 31. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - The primary-source background for strain–vorticity interaction, projected strain structure, and nonlinear depletion.

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - The scale-critical regularity background for the positive middle-strain channel.

3. Alexis Vasseur, *Regularity criterion for 3D Navier-Stokes equations in terms of the direction of the velocity*, arXiv:0705.2446.
   - The primary-source background for the amplitude/direction geometric regularity route; the optimal quotient direction in this round is different from the original velocity direction.

The critical-mass PDE, $\chi^2$ identity, continuous moment-curvature identity, and dynamic intermittency balance in this round are all directly derived in this text.

---

# 32. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Critical\text{-}Mass\ Dynamic\ Intermittency},
\\
\text{24/72 substrate}
&=
\mathsf C,
\\
\text{24/72 transition law}
&=
\mathsf F,
\\
\text{Probability representation}
&\neq
\mathrm{stochastic\ ontology},
\\
\text{Critical mass}
&=
\mu_Q,
\\
\text{Strain measure}
&=
\nu_S,
\\
\text{Intermittency}
&=
1+\chi^2(\nu_S\|\mu_Q),
\\
\text{Viscous mechanism}
&=
-2\nu\mathcal F_{\rm rel},
\\
\text{Dangerous mechanism}
&=
\mathcal P_{\rm sel},
\\
\text{STOP-C25}
&=
\mathrm{Relative\text{-}Source/Critical\text{-}Mass\ Separation\ Gap},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Next}
&=
\mathrm{Relative\text{-}Source\ Decomposition}.
\end{aligned}
}
$$