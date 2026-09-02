# NS × X Integral × 24/72 Paradigm in Practice
## Round 25 — Pure Continuous Nonlocal Cross-Blob Coupling / Virtual-Connectivity Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Nonlocal Cross-Region Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round24_PureContinuous_CriticalMass_ConductanceDynamics_v0.1_2026-08-17.md`
- This round's objective: Round 24 showed that local viscous neck communication can become extremely slow as blob separation increases. This round reintroduces the nonlocal pressure and whole-space Biot–Savart / strain recovery from Round 04 to investigate whether two critical-mass blobs still form a "virtual connection" via algebraically decaying nonlocal kernels when there is almost no mass neck.
- Non-claims: This document does not prove that nonlocal coupling necessarily synchronizes two blobs, nor does it deduce a positive Cheeger gap from nonlocal interaction. On the contrary, this round proves that nonlocal coupling is generally signed / anisotropic, so dynamic coupling and positive mixing conductance must be distinguished.

# 0. Round 24 handoff

The critical mass:

$$
d\mu_Q
=
m_Qdx
$$

obeys:

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
\tag{0.1}
$$

Round 24 continuous Cheeger conductance:

$$
\boxed{
h_Q
=
\inf_A
\frac{
\operatorname{Per}_{\mu_Q}(A)
}{
\min\{
\mu_Q(A),
1-\mu_Q(A)
\}
}.
}
\tag{0.2}
$$

material cut odds:

$$
\boxed{
\frac d{dt}
\log
\frac a{1-a}
=
\nu
\frac{
J_A
}{
a(1-a)
}
+
3\Delta_A G_Q.
}
\tag{0.3}
$$

And the two-Gaussian heat witness shows:

$$
\boxed{
\text{strictly positive density}
\not\Rightarrow
\text{uniformly positive conductance}.
}
$$

Round 24 STOP:

$$
\boxed{
\text{STOP-C28}
=
\text{Conductance-Restoration / Neck-Selection Gap}.
}
$$

---

# 1. Two separated critical-mass regions

Let:

$$
A,B\subset\mathbb R^3
$$

be two measurable / smooth regions, satisfying:

$$
\boxed{
\operatorname{dist}(A,B)
=
R>0.
}
\tag{1.1}
$$

Allowing the existence of a low-mass neck in between:

$$
N
=
\mathbb R^3\setminus(A\cup B).
$$

Define:

$$
a
=
\mu_Q(A),
\qquad
b
=
\mu_Q(B).
$$

This round does not treat:

$$
A,B
$$

as discrete graph nodes.

They are merely two testing regions in the continuous field.

---

# 2. Pressure source and nonlocal pressure Hessian

The whole-space incompressible NS pressure satisfies:

$$
\boxed{
-\Delta p
=
f_p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.1}
$$

Therefore:

$$
\boxed{
H_p
=
\nabla^2(-\Delta)^{-1}f_p.
}
\tag{2.2}
$$

The Newtonian potential kernel:

$$
\Phi(z)
=
\frac1{4\pi|z|}
$$

gives:

$$
\boxed{
\partial_i\partial_j\Phi(z)
=
\frac{
3z_iz_j-|z|^2\delta_{ij}
}{
4\pi|z|^5
}.
}
\tag{2.3}
$$

Thus, away from the source:

$$
\boxed{
|K_H(z)|
\lesssim
|z|^{-3}.
}
\tag{2.4}
$$

This is an algebraic nonlocal coupling.

---

# 3. Exact source-region split for pressure

Since the operator:

$$
\nabla^2(-\Delta)^{-1}
$$

is linear with respect to the source:

$$
f_p
$$

we can define:

$$
f_p^A
=
\mathbf1_Af_p,
$$

$$
f_p^B
=
\mathbf1_Bf_p,
$$

$$
f_p^N
=
\mathbf1_Nf_p.
$$

Then:

$$
\boxed{
H_p
=
H_p^A
+
H_p^B
+
H_p^N,
}
\tag{3.1}
$$

where:

$$
H_p^B
=
\nabla^2(-\Delta)^{-1}f_p^B.
$$

For:

$$
x\in A,
$$

we have:

$$
\boxed{
|H_p^B(x)|
\le
\frac{
C
}{
R^3
}
\|f_p\|_{L^1(B)}.
}
\tag{3.2}
$$

For higher derivatives:

$$
\boxed{
|\nabla^mH_p^B(x)|
\le
\frac{
C_m
}{
R^{3+m}
}
\|f_p\|_{L^1(B)}.
}
\tag{3.3}
$$

---

# 4. Whole-space Biot–Savart cross coupling

For an appropriately decaying divergence-free velocity:

$$
\boxed{
u
=
\nabla\times(-\Delta)^{-1}\omega.
}
\tag{4.1}
$$

The magnitude of the 3D Biot–Savart kernel is:

$$
|K_{BS}(z)|
\sim
|z|^{-2}.
$$

Therefore, splitting the vorticity by region:

$$
\omega
=
\omega^A+\omega^B+\omega^N,
$$

and defining:

$$
u^B
=
\mathcal B[\omega^B].
$$

For:

$$
x\in A,
$$

we have:

$$
\boxed{
|u^B(x)|
\le
\frac{
C
}{
R^2
}
\|\omega\|_{L^1(B)}.
}
\tag{4.2}
$$

And the cross velocity gradient / strain:

$$
S^B
=
\operatorname{sym}\nabla u^B
$$

satisfies:

$$
\boxed{
|S^B(x)|
\le
\frac{
C
}{
R^3
}
\|\omega\|_{L^1(B)}.
}
\tag{4.3}
$$

Therefore:

$$
\boxed{
\text{velocity cross influence}
\sim
R^{-2},
\qquad
\text{strain / pressure-Hessian cross influence}
\sim
R^{-3}
}
$$

in the absence of higher multipole cancellations.

---

# 5. Cross strain enters critical-mass selection directly

The Round 21 critical-mass growth field is:

$$
\boxed{
G_Q
=
\gamma_Q-\nu K_D,
}
\tag{5.1}
$$

where:

$$
\boxed{
\gamma_Q
=
-
n^\top Sn.
}
\tag{5.2}
$$

For region:

$$
A,
$$

split:

$$
S
=
S^A+S^B+S^N.
$$

Define:

$$
\boxed{
\gamma_{A\leftarrow B}(x)
=
-
n(x)^\top
S^B(x)
n(x),
\qquad
x\in A.
}
\tag{5.3}
$$

Then:

$$
\boxed{
|\gamma_{A\leftarrow B}(x)|
\le
\frac{
C
}{
R^3
}
\|\omega\|_{L^1(B)}.
}
\tag{5.4}
$$

Define the conditional average:

$$
\boxed{
\Gamma_{A\leftarrow B}
=
\frac1a
\int_A
\gamma_{A\leftarrow B}
\,d\mu_Q.
}
\tag{5.5}
$$

Therefore:

$$
\boxed{
|\Gamma_{A\leftarrow B}|
\le
\frac{
C
}{
R^3
}
\|\omega\|_{L^1(B)}.
}
\tag{5.6}
$$

This is the nonlocal cross term that truly and directly enters the Round 24 cut-selection contrast.

---

# 6. Cross pressure enters intermittency selection, not the critical-mass equation directly

We must distinguish:

- critical-mass selection:
  $$
  G_Q
  $$
  directly contains the strain:
  $$
  -n^\top Sn;
  $$
- strain-measure relative source:
  $$
  \mathcal R_S
  $$
  is what directly contains:
  $$
  H_p.
  $$

Therefore, the virtual connection of pressure primarily enters the intermittency / source-selection channel of Rounds 22–23.

For the continuous tilt:

$$
p\ge0,
$$

the raw moment weight is:

$$
w_p
=
r^{3-p}|S|^{p-2}.
$$

The cross-pressure contribution is:

$$
\boxed{
\mathcal P_p(A\leftarrow B)
=
-2
\int_A
w_p
S:H_p^B\,dx.
}
\tag{6.1}
$$

From (3.2):

$$
\boxed{
|\mathcal P_p(A\leftarrow B)|
\le
\frac{
C
}{
R^3
}
\|f_p\|_{L^1(B)}
\int_A
r^{3-p}
|S|^{p-1}dx.
}
\tag{6.2}
$$

Therefore, the pressure relative-source also acts algebraically across the low-mass neck.

---

# 7. Local neck communication versus nonlocal interaction

The Round 24 heat-type thin-neck model gives:

$$
\boxed{
\mathcal D_{\rm neck}(R,t)
\lesssim
C_D(t)
\exp
\left[
-\frac{
R^2
}{
C\nu t
}
\right]
}
\tag{7.1}
$$

as the cross-neck communication scale.

Meanwhile, the nonlocal strain / pressure coupling at the first nonvanishing far-field multipole order:

$$
m\ge0
$$

is generally:

$$
\boxed{
\mathcal C_{\rm nl}(R)
\sim
R^{-(3+m)}.
}
\tag{7.2}
$$

Thus, if for a certain interaction channel there exists:

$$
\boxed{
|\mathcal C_{\rm nl}(R)|
\ge
c_\ast
R^{-(3+m)}
}
\tag{7.3}
$$

for large:

$$
R,
$$

then for a fixed:

$$
t>0
$$

we have:

$$
\boxed{
\frac{
|\mathcal C_{\rm nl}(R)|
}{
\mathcal D_{\rm neck}(R,t)
}
\to
\infty
\qquad
R\to\infty.
}
\tag{7.4}
$$

Named:

$$
\boxed{
\textbf{Algebraic-over-Gaussian Virtual-Coupling Regime}.
}
$$

---

# 8. Important limitation — algebraic upper bound is not a lower bound

The:

$$
R^{-3}
$$

in Sections 3–4 is a robust upper-envelope decay.

However, signed multipole moments can undergo cancellation.

Therefore, one cannot deduce a nonzero:

$$
R^{-3}
$$

lower bound solely from:

$$
\|f_p\|_{L^1(B)}
$$

or:

$$
\|\omega\|_{L^1(B)}
$$

The true far-field order depends on:

$$
\boxed{
\text{first nonvanishing signed multipole}.
}
$$

Thus:

$$
\boxed{
\text{nonlocal dominance}
}
$$

is a conditional geometric regime,

not a universal theorem for every blob pair.

---

# 9. Virtual Coupling Dominance Ratio

Let the Round 24 cut-diffusion odds rate be:

$$
\boxed{
\mathcal D_A
=
\nu
\left|
\frac{
J_A
}{
a(1-a)
}
\right|.
}
\tag{9.1}
$$

For two dominant regions:

$$
A,B,
$$

define the cross-strain contrast rate:

$$
\boxed{
\mathcal C_{AB}^{S}
=
\left|
\Gamma_{A\leftarrow B}
-
\Gamma_{B\leftarrow A}
\right|.
}
\tag{9.2}
$$

When:

$$
\mathcal D_A>0,
$$

define:

$$
\boxed{
\mathfrak V_{AB}
=
\frac{
3\mathcal C_{AB}^{S}
}{
\mathcal D_A
}.
}
\tag{9.3}
$$

If:

$$
\boxed{
\mathfrak V_{AB}\gg1,
}
\tag{9.4}
$$

then the relative growth of the two regions can be influenced more strongly by the nonlocal strain coupling than by direct neck diffusion.

Note:

$$
\mathfrak V_{AB}
$$

does not imply mixing.

It merely indicates:

$$
\boxed{
\text{dynamical coupling}
>
\text{mass-exchange coupling}.
}
$$

---

# 10. Cross coupling is signed

Assume:

$$
S^B(x)
$$

is nonzero in region:

$$
A
$$

Since:

$$
\operatorname{tr}S^B=0,
$$

a nonzero symmetric strain tensor must have spectral directions of different signs.

And:

$$
\gamma_{A\leftarrow B}
=
-
n^\top S^Bn.
$$

Therefore, depending on the local optimal quotient direction:

$$
n,
$$

it is possible that:

$$
\boxed{
\gamma_{A\leftarrow B}>0
}
$$

or:

$$
\boxed{
\gamma_{A\leftarrow B}<0.
}
$$

Thus, the cross strain can:

- amplify the local critical mass;
- suppress the local critical mass.

There is no universal synchronizing sign.

---

# 11. Pressure Hessian kernel is anisotropic and sign-indefinite

For a point-like scalar source:

$$
f_p^B
\approx
M\delta_y,
$$

and:

$$
e
=
\frac{x-y}{|x-y|},
$$

we have the far-field model:

$$
\boxed{
H_p^B(x)
\approx
\frac{
M
}{
4\pi R^3
}
\left(
3e\otimes e-I
\right).
}
\tag{11.1}
$$

The tensor:

$$
3e\otimes e-I
$$

has eigenvalues:

$$
2,-1,-1.
$$

Therefore, the same source amplitude will produce opposite-sign contractions for different strain orientations.

For example:

$$
e=e_1,
$$

$$
S_1
=
\operatorname{diag}(-2a,a,a)
$$

gives:

$$
S_1:
(3e_1\otimes e_1-I)
<0.
$$

While:

$$
S_2
=
\operatorname{diag}(a,-2a,a)
$$

gives the opposite sign.

Thus:

$$
\boxed{
\textbf{
nonlocal pressure coupling is not a positive synchronization kernel.
}
}
\tag{11.2}
$$

---

# 12. Virtual connection does not imply a Cheeger gap

The Cheeger conductance:

$$
h_Q
$$

measures:

$$
\boxed{
\text{critical mass crossing weighted cuts}.
}
$$

The nonlocal strain / pressure kernels measure:

$$
\boxed{
\text{field influence across geometric separation}.
}
$$

The latter does not require:

$$
m_Q
$$

to actually cross the neck.

Therefore, it is entirely possible to simultaneously have:

$$
\boxed{
h_Q\ll1
}
$$

and:

$$
\boxed{
\mathcal C_{\rm nl}\neq0.
}
$$

Thus:

$$
\boxed{
\textbf{Virtual Dynamical Connectivity}
\neq
\textbf{Positive Mass Conductance}.
}
\tag{12.1}
$$

This is the most important conceptual distinction of this round.

---

# 13. Duplex connectivity state

Round 24 only tracked:

$$
h_Q.
$$

This round shows that NS connectivity requires at least two layers:

$$
\boxed{
X_{\rm duplex}
=
\left\langle
h_Q,
\mathscr I_Q(s),
\mathcal C_{AB}^{S},
\mathcal P_p(A\leftarrow B),
\mathfrak V_{AB}
\right\rangle.
}
\tag{13.1}
$$

where:

## Layer M — mass connectivity

$$
\boxed{
h_Q,\quad
\mathscr I_Q(s).
}
$$

is the positive / metric mixing carrier.

## Layer N — nonlocal field connectivity

$$
\boxed{
\mathcal C_{AB}^{S},
\quad
\mathcal P_p.
}
$$

is the signed dynamical coupling carrier.

These two layers cannot replace each other.

---

# 14. Exact cross-selection split across a cut

Let:

$$
A^c
$$

be the source complement.

By Biot–Savart linearity:

$$
S
=
S^A+S^{A^c}.
$$

On:

$$
A
$$

$$
\gamma_Q
=
-
n^\top S^An
-
n^\top S^{A^c}n.
$$

Define:

$$
\boxed{
\langle\gamma^{\rm cross}\rangle_A
=
-\frac1a
\int_A
n^\top S^{A^c}n
\,d\mu_Q.
}
\tag{14.1}
$$

and:

$$
\boxed{
\langle\gamma^{\rm cross}\rangle_{A^c}
=
-\frac1{1-a}
\int_{A^c}
n^\top S^An
\,d\mu_Q.
}
\tag{14.2}
$$

Therefore, the Round 24 selection contrast:

$$
\Delta_A G_Q
$$

contains the exact nonlocal piece:

$$
\boxed{
\Delta_A G_Q^{\rm cross}
=
\langle\gamma^{\rm cross}\rangle_A
-
\langle\gamma^{\rm cross}\rangle_{A^c}.
}
\tag{14.3}
$$

Thus, the cut odds equation can be written as:

$$
\boxed{
\ell_A'
=
\mathcal D_A^{\rm signed}
+
3\Delta_A G_Q^{\rm local}
+
3\Delta_A G_Q^{\rm cross}
+
3\Delta_A G_Q^{\rm gauge/diff}.
}
\tag{14.4}
$$

This is where the virtual connection directly enters the critical-mass separation dynamics.

---

# 15. Nonlocal coupling can synchronize or anti-synchronize

If:

$$
\Delta_A G_Q^{\rm cross}
$$

has the same sign as:

$$
-\ell_A
$$

it tends to reduce the mass imbalance on both sides:

$$
\boxed{
\text{synchronizing virtual coupling}.
}
$$

If it has the same sign as:

$$
\ell_A
$$

it tends to increase the mass imbalance:

$$
\boxed{
\text{anti-synchronizing virtual coupling}.
}
$$

From Sections 10–11:

$$
\boxed{
\text{both signs are allowed by local tensor geometry}.
}
$$

Therefore, nonlocality itself is not a regularity mechanism.

It requires an additional:

$$
\boxed{
\text{sign coherence / depletion geometry}.
}
$$

---

# 16. Pressure cross interaction returns Round 04 in a sharper form

Round 04 obstruction:

$$
\boxed{
\text{local geometry / nonlocal pressure closure gap}.
}
$$

Round 25 now recognizes:

pressure nonlocality is not purely an obstruction in the low-conductance regime.

It can also be a:

$$
\boxed{
\text{cross-blob communication channel}.
}
$$

However, because the kernel is sign-indefinite,

it can simultaneously:

- synchronize;
- de-synchronize;
- rotate local strain geometry;
- bias high-$K$ relative source.

Therefore, the Boss of Round 04 is reclassified as:

$$
\boxed{
\textbf{nonlocal signed coupling rather than merely nonlocal nuisance}.
}
$$

---

# 17. Pressure self-adjoint reciprocity does not give positivity

The operator:

$$
\nabla^2(-\Delta)^{-1}
$$

is the Fourier multiplier matrix:

$$
-\frac{
\xi\otimes\xi
}{
|\xi|^2
}
$$

up to a sign convention.

It possesses a self-adjoint / reciprocal structure.

However:

$$
3e\otimes e-I
$$

has mixed signs.

Thus:

$$
\boxed{
\text{reciprocity}
\neq
\text{positive coupling}.
}
\tag{17.1}
$$

Therefore, one cannot directly deduce the restoration of:

$$
h_Q
$$

from the symmetric character of the pressure operator.

---

# 18. Algebraic virtual connection versus exponential neck

Combining Round 24 with this round:

$$
\boxed{
\begin{array}{c|c}
\text{channel}
&
\text{large-separation scale}
\\
\hline
\text{local viscous neck}
&
\exp[-R^2/(C\nu t)]
\\
\text{cross velocity}
&
R^{-2}
\\
\text{cross strain}
&
R^{-3}
\\
\text{cross pressure Hessian}
&
R^{-3}
\end{array}
}
\tag{18.1}
$$

This table is not a universal lower bound table.

It represents:

- the model scale of heat communication;
- the far-field envelope / nonvanishing-multipole scale of the whole-space kernel.

In the nonzero cross multipole branch,

a large separation can form:

$$
\boxed{
\text{weak mass conductance}
+
\text{comparatively stronger nonlocal field interaction}.
}
\tag{18.2}
$$

---

# 19. Translation-invariant norms miss both separation and cross sign

Round 24 has already pointed out:

translation-invariant norms do not record the blob separation:

$$
R.
$$

Round 25 adds:

they typically also do not record:

$$
\boxed{
\text{relative orientation / signed kernel phase}.
}
$$

Therefore, identical:

- $L^p$ amplitudes;
- energy;
- enstrophy;
- critical quotient norms;

can correspond to different signs and magnitudes of:

$$
\mathcal C_{AB}^{S}
$$

Thus, conductance/nonlocal coupling requires a truly relational observation:

$$
\boxed{
\mathsf O_{\mathsf X}.
}
$$

---

# 20. Nonlocal interaction-to-mixing transduction gap

For virtual coupling to truly repair the Round 24 issue of:

$$
h_Q\ll1,
$$

what is needed is not just:

$$
\mathcal C_{\rm nl}\neq0.
$$

We must also prove:

$$
\boxed{
\text{signed nonlocal field interaction}
\Longrightarrow
\text{positive neck mass restoration}.
}
$$

That is:

$$
\boxed{
\text{interaction}
\to
\text{selection synchronization}
\to
\text{mass redistribution}
\to
\text{conductance increase}.
}
\tag{20.1}
$$

Currently, the first arrow itself lacks a universal sign.

Therefore, virtual connection is not a ready-made spectral-gap proof.

---

# 21. STOP-C29 — Virtual-Connectivity / Sign-Coherence Transduction Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C29}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{nonlocal\ cross\text{-}blob\ coupling},
\\
\text{mass\ connectivity}
=
h_Q,\ \mathscr I_Q,
\\
\text{cross\ velocity}
\sim
R^{-2},
\\
\text{cross\ strain}
\sim
R^{-3},
\\
\text{cross\ pressure\ Hessian}
\sim
R^{-3},
\\
\text{neck\ diffusion}
\sim
\exp[-R^2/(C\nu t)]
\text{ in heat-type separation model},
\\
\text{virtual\ dominance}
=
\mathrm{possible\ under\ nonzero\ multipole},
\\
\text{coupling\ sign}
=
\mathrm{indefinite},
\\
\text{virtual\ connectivity}
\neq
\text{positive\ conductance},
\\
\text{missing}
=
\mathrm{sign\ coherence\ and\ interaction\text{-}to\text{-}mixing\ transduction},
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
\textbf{STOP-C29:
Virtual-Connectivity / Sign-Coherence Transduction Gap}.
}
$$

---

# 22. 24/72 Ledger — Round 25

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C324 | separated continuous regions $A,B$ | $\mathsf C$ | relational partition | $\mathsf X$ | $\mathsf F$ | FORM |
| C325 | pressure Hessian kernel | $\mathsf C$ | nonlocal integral | relational | $\mathsf F$ | EXACT |
| C326 | pressure source-region split | $\mathsf C$ | linear source split | $\mathsf X$ | $\mathsf F$ | EXACT |
| C327 | $R^{-3}$ cross-pressure bound | $\mathsf C$ | kernel estimate | scalar | $\mathsf F$ | PROVED |
| C328 | Biot–Savart cross velocity | $\mathsf C$ | nonlocal integral | relational | $\mathsf F$ | EXACT |
| C329 | $R^{-2}/R^{-3}$ cross bounds | $\mathsf C$ | kernel estimate | scalar | $\mathsf F$ | PROVED |
| C330 | cross strain in $G_Q$ | $\mathsf C$ | selection coupling | targeted | $\mathsf F$ | EXACT |
| C331 | cross pressure in $\mathcal R_S$ | $\mathsf C$ | tilt/source coupling | targeted | $\mathsf F$ | EXACT |
| C332 | algebraic-over-Gaussian regime | $\mathsf C$ | asymptotic comparison | scalar | $\mathsf F$ | CONDITIONAL PROVED |
| C333 | virtual dominance ratio | $\mathsf C$ | recognition | scalar | $\mathsf F$ | FORM |
| C334 | strain cross sign | $\mathsf C$ | tensor geometry | relational | $\mathsf F$ | INDEFINITE |
| C335 | pressure cross sign | $\mathsf C$ | Hessian kernel geometry | relational | $\mathsf F$ | INDEFINITE |
| C336 | virtual connectivity $\Rightarrow$ gap | $\mathsf C$ | mixing geometry | targeted | $\mathsf F$ | REFUTED as automatic implication |
| C337 | duplex connectivity state | $\mathsf C$ | coupled observation | $\mathsf X$ | $\mathsf F$ | FORM |
| C338 | exact cut cross-selection split | $\mathsf C$ | Biot–Savart/selection | targeted | $\mathsf F$ | EXACT |
| C339 | interaction-to-mixing transduction | $\mathsf C$ | global feedback | targeted | $\mathsf F$ | OPEN / STOP-C29 |

---

# 23. Continuous-versus-discrete status

This round is naturally easy to depict as:

$$
\text{blob A}
\leftrightarrow
\text{blob B}.
$$

But this does not mean we already need a graph substrate.

All operations remain:

- continuous source partitions;
- continuous singular-integral kernels;
- continuous region averages;
- continuous weighted cuts;
- continuous separation parameter:
  $$
  R.
  $$

Thus:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{23.1}
$$

If blobs are turned into graph vertices in the future,

it will initially just be a coarse-grained representation.

Unless it can be proven that the closure of the signed kernel interaction must record discrete component identities,

it cannot yet be considered an essential:

$$
\mathsf C\to\mathsf D.
$$

---

# 24. Strongest results of Round 25

## R25-A — nonlocal cross-field bounds

$$
\boxed{
|u^{B\to A}|
\lesssim
R^{-2}
\|\omega\|_{L^1(B)},
}
$$

$$
\boxed{
|S^{B\to A}|
\lesssim
R^{-3}
\|\omega\|_{L^1(B)},
}
$$

$$
\boxed{
|H_p^{B\to A}|
\lesssim
R^{-3}
\|f_p\|_{L^1(B)}.
}
$$

## R25-B — nonlocal interaction can outlive the neck

conditional nonzero-multipole branch:

$$
\boxed{
\frac{
\text{algebraic nonlocal coupling}
}{
\text{Gaussian neck communication}
}
\to\infty
}
$$

for fixed positive time and large separation.

## R25-C — cross coupling has no universal sign

$$
\boxed{
\text{strain kernel coupling}
\quad\text{and}\quad
\text{pressure-Hessian coupling}
}
$$

can both amplify or suppress depending on the geometry.

## R25-D — connectivity duplex

$$
\boxed{
\text{mass conductance}
\neq
\text{nonlocal dynamical connectivity}.
}
$$

---

# 25. Next round — signed-kernel coherence

What truly remains now is:

$$
\boxed{
\text{sign coherence}.
}
$$

The next round will no longer ask:

> Does nonlocal coupling exist?

But will ask:

$$
\boxed{
\textbf{
Can incompressibility, strain geometry, or critical-mass tilt
force the signed cross-kernel interaction to be predominantly synchronizing
on dangerous branches?
}
}
$$

Specifically:

1. Define the continuous signed coherence for the cross strain:
   $$
   \mathfrak c_S(A,B);
   $$

2. Define for the pressure Hessian:
   $$
   \mathfrak c_P^{(p)}(A,B);
   $$

3. Incorporate the alignment geometry of the kernel orientation with:
   $$
   n,\quad
   \widehat S,\quad
   \omega
   $$

4. Test whether the dangerous middle-strain branch:
   $$
   \lambda_2>0
   $$
   is biased towards a certain nonlocal sign;

5. If the sign remains completely free, then the virtual connection can only be a signed transport network and cannot close the conductance;

6. If the sign exhibits a bias under high-$K$/high-$\lambda_2$ tilt, it can be connected back to the Round 22 tilt-selection law.

---

# 26. External primary-source anchors

1. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - The primary-source background where the whole-space pressure is determined by the Riesz transforms of $u_i u_j$.

2. Maurizio Carbone, Michele Iovieno, Andrew D. Bragg, *Gauge symmetry and dimensionality reduction of the anisotropic pressure Hessian*, arXiv:1911.08652.
   - The primary-source background of the anisotropic pressure Hessian as a nonlocal functional in velocity-gradient dynamics.

The pressure-kernel far-field bound, cross-region source split, virtual-dominance comparison, signed pressure witness, and duplex-connectivity distinction in this round are all directly derived in this document.

---

# 27. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Nonlocal\ Cross\text{-}Blob\ Coupling},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Mass connectivity}
&=
h_Q,
\\
\text{Nonlocal connectivity}
&=
\mathcal C_{AB}^{S}
+
\mathcal P_p(A\leftarrow B),
\\
\text{Far-field coupling}
&=
\mathrm{algebraic},
\\
\text{Neck diffusion}
&=
\mathrm{Gaussian/exponential\ in\ separation\ model},
\\
\text{Virtual dominance}
&=
\mathrm{possible},
\\
\text{Universal synchronizing sign}
&=
\mathrm{false},
\\
\text{STOP-C29}
&=
\mathrm{Virtual\text{-}Connectivity/Sign\text{-}Coherence\ Transduction\ Gap},
\\
\text{Next}
&=
\mathrm{Signed\text{-}Kernel\ Coherence}.
\end{aligned}
}
$$