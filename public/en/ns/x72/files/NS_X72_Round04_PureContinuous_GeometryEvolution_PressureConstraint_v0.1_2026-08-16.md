# NS × X Integral × 24/72 Paradigm in Practice
## Round 04 — Pure Continuous Geometry Evolution / Pressure-Constraint Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Geometry-Evolution Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round03_PureContinuous_RelationalGeometry_v0.1_2026-08-16.md`
- This round's objective: Instead of treating $\lambda_2^+$, $\det S$, and $\sigma^+$ as external regularity criteria, directly derive their continuous evolution to determine whether Navier–Stokes dynamics intrinsically generates geometric feedback; and examine whether the pressure Hessian forms the first global continuous constraint carrier that cannot be eliminated by purely local geometry.
- Non-claims: This round does not claim to rule out all purely continuous proofs, nor does it claim that pressure nonlocality equates to blow-up. This document only determines the formation eligibility and stopping points of the specified local-geometric closure architecture.

---

# 0. Round 03 handoff

Round 03 established the relational state:

$$
X_{\rm geom}
=
\left\langle
u,p,S,\omega,
\lambda_1,\lambda_2,\lambda_3,
\xi,\sigma,
\det S,
\nabla S
\right\rangle,
$$

where:

$$
S
=
\nabla_{\rm sym}u,
$$

$$
\omega
=
\nabla\times u,
$$

$$
\xi
=
\frac{\omega}{|\omega|},
$$

$$
\sigma
=
\xi^\top S\xi.
$$

and proved that amplitude-only observation in the specified context:

$$
\Gamma_{\rm amp}
$$

is insufficient.

Specifically, the two trace-free strain tensors:

$$
S_{\rm grow}
=
\operatorname{diag}(-2a,a,a),
$$

$$
S_{\rm decay}
=
\operatorname{diag}(-a,-a,2a)
$$

have the same:

$$
|S|^2=6a^2,
$$

but:

$$
\det S_{\rm grow}
=
-2a^3,
$$

$$
\det S_{\rm decay}
=
2a^3.
$$

Thus, the same amplitude can correspond to opposite enstrophy-production signs.

Therefore:

$$
\boxed{
\mathsf X_{\Gamma_{\rm amp}}
}
$$

has been established within the restricted observation class.

The primary STOP of Round 03:

$$
\boxed{
\text{STOP-C06}
=
\text{Geometry-Evolution / Coercivity Gap}.
}
$$

This round directly targets:

$$
\boxed{
D_tS,
\quad
D_t\lambda_2,
\quad
D_t\det S,
\quad
D_t(\xi^\top S\xi).
}
$$

---

# 1. Velocity-gradient equation

Let:

$$
A
=
\nabla u
$$

adopt the convention:

$$
A_{ij}
=
\partial_j u_i.
$$

Navier–Stokes:

$$
\partial_tu
+
u\cdot\nabla u
+
\nabla p
=
\nu\Delta u.
$$

Taking the gradient.

Let the material derivative be:

$$
D_t
=
\partial_t+u\cdot\nabla.
$$

Then:

$$
\boxed{
D_tA
+
A^2
+
\nabla^2p
=
\nu\Delta A.
}
\tag{1.1}
$$

Decompose:

$$
A=S+\Omega,
$$

where:

$$
S^\top=S,
$$

$$
\Omega^\top=-\Omega.
$$

Taking the symmetric part:

$$
\operatorname{sym}(A^2)
=
S^2+\Omega^2.
$$

In three dimensions:

$$
\Omega
=
\frac12[\omega]_\times,
$$

thus:

$$
\boxed{
\Omega^2
=
\frac14
\left(
\omega\otimes\omega
-
|\omega|^2I
\right).
}
\tag{1.2}
$$

Therefore, the exact strain equation is:

$$
\boxed{
D_tS
-
\nu\Delta S
=
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
H_p,
}
\tag{1.3}
$$

where:

$$
\boxed{
H_p
=
\nabla^2p.
}
\tag{1.4}
$$

The first important result of this round:

> The evolution of strain geometry at the pointwise level is not solely determined by the local algebra of $S$ and $\omega$; the pressure Hessian and viscosity-induced spatial geometry enter simultaneously.

---

# 2. Pressure Poisson constraint

Taking the divergence of the momentum equation.

From:

$$
\nabla\cdot u=0
$$

we obtain:

$$
\boxed{
-\Delta p
=
\partial_i u_j\,
\partial_j u_i.
}
\tag{2.1}
$$

Also:

$$
\operatorname{tr}(A^2)
=
\operatorname{tr}(S^2)
+
\operatorname{tr}(\Omega^2).
$$

and:

$$
\operatorname{tr}(S^2)
=
|S|^2,
$$

$$
\operatorname{tr}(\Omega^2)
=
-\frac12|\omega|^2.
$$

So:

$$
\boxed{
-\Delta p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.2}
$$

Define the pressure source:

$$
\boxed{
f_p
=
|S|^2
-
\frac12|\omega|^2.
}
\tag{2.3}
$$

Then:

$$
-\Delta p=f_p.
$$

In $\mathbb R^3$, under appropriate decay conditions:

$$
p
=
(-\Delta)^{-1}f_p
$$

up to a function of time.

Therefore:

$$
\boxed{
(H_p)_{ij}
=
\partial_i\partial_j(-\Delta)^{-1}f_p.
}
\tag{2.4}
$$

If we use the Riesz transform:

$$
\mathcal R_i
=
\partial_i(-\Delta)^{-1/2},
$$

then:

$$
\boxed{
(H_p)_{ij}
=
\mathcal R_i\mathcal R_j f_p.
}
\tag{2.5}
$$

This is an order-zero singular integral operator.

---

# 3. Isotropic / anisotropic pressure-Hessian split

From:

$$
\Delta p=-f_p
$$

we can write:

$$
\boxed{
H_p
=
-\frac13 f_p I
+
H_p^{\rm dev},
}
\tag{3.1}
$$

where:

$$
\operatorname{tr}
H_p^{\rm dev}
=
0.
$$

So the pressure Hessian consists of two parts:

1. isotropic trace part:

$$
-\frac13f_pI,
$$

whose scalar source is directly determined by the local:

$$
S,\omega
$$

2. deviatoric part:

$$
H_p^{\rm dev},
$$

which is determined by the Poisson/Riesz global reconstruction.

Therefore:

$$
\boxed{
\text{pressure trace is locally sourced, but pressure anisotropy is nonlocal}.
}
\tag{3.2}
$$

This distinction will directly control the eigenvalue evolution.

---

# 4. PROVED — pressure Hessian is not a finite local differential operator of its source

Consider the operator:

$$
T_{ij}
=
\partial_i\partial_j(-\Delta)^{-1}.
$$

In Fourier space:

$$
\widehat{T_{ij}f}(\xi)
=
-
\frac{\xi_i\xi_j}{|\xi|^2}
\widehat f(\xi).
$$

If $T_{ij}$ could be represented by some finite-order constant-coefficient local differential operator:

$$
P(D)
$$

on all smooth compactly supported sources, then its Fourier symbol must be a polynomial:

$$
P(i\xi).
$$

However:

$$
-\frac{\xi_i\xi_j}{|\xi|^2}
$$

is not a polynomial.

Therefore:

$$
\boxed{
\partial_i\partial_j(-\Delta)^{-1}
}
$$

is not a finite-order local differential operator.

That is:

$$
\boxed{
H_p(x)
}
$$

cannot be reconstructed from:

$$
f_p(x),
\nabla f_p(x),
\ldots,
\nabla^k f_p(x)
$$

via any universal finite-order local differential rule on all admissible source functions.

Status:

$$
\boxed{
\textbf{PROVED operator-level nonlocality}.
}
\tag{4.1}
$$

Note:

What is proved here is the nonlocality of the pressure reconstruction operator.

It does not claim:

> The pressure Hessian of every NS solution cannot be effectively controlled using additional global invariants.

---

# 5. 72 / X interpretation of the incompressibility constraint

NS time evolution is deterministic:

$$
L=\mathsf F.
$$

But the pressure at each time slice is not a scalar updated solely by the pointwise local state.

It is reconstructed by the global elliptic constraint:

$$
-\Delta p=f_p
$$

Therefore, if the 24-update axis is to describe "how to organize the update of the current state," a more precise NS profile is not purely:

$$
\mathsf S.
$$

but rather a hybrid:

$$
\boxed{
\mathsf S_{\rm time}
+
\mathsf P_{\rm constraint}.
}
\tag{5.1}
$$

where:

- $\mathsf S_{\rm time}$: time evolution depends on the state at the previous moment;
- $\mathsf P_{\rm constraint}$: on the same time slice, the pressure constraint global coupling acts simultaneously on the entire spatial state.

Thus, for the first time in this round, an update-axis refinement supported by actual PDE structure appears:

$$
\boxed{
\langle
\mathsf C;
\mathsf S;
\mathsf X;
\mathsf F
\rangle
}
$$

is elevated to:

$$
\boxed{
\langle
\mathsf C;
\{\mathsf S,\mathsf P\};
\mathsf X;
\mathsf F
\rangle.
}
\tag{5.2}
$$

This is not a substrate transition.

So:

$$
\boxed{
B=\mathsf C
}
$$

remains unchanged.

---

# 6. Exact eigenvalue evolution

Assume the strain spectrum at a point is simple:

$$
\lambda_1<\lambda_2<\lambda_3.
$$

Let:

$$
e_i
$$

be the normalized eigenvector:

$$
Se_i
=
\lambda_ie_i.
$$

For the material derivative:

$$
\boxed{
D_t\lambda_i
=
e_i^\top(D_tS)e_i.
}
\tag{6.1}
$$

For the spatial derivative, the standard symmetric-matrix eigenvalue perturbation formula gives:

$$
\partial_k^2\lambda_i
=
e_i^\top(\partial_k^2S)e_i
+
2
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
$$

Summing over $k$:

$$
\Delta\lambda_i
=
e_i^\top(\Delta S)e_i
+
2
\sum_{k=1}^3
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
$$

Thus:

$$
e_i^\top(\Delta S)e_i
=
\Delta\lambda_i
-
2
\sum_{k=1}^3
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
$$

Substituting into the strain equation (1.3):

$$
\boxed{
\begin{aligned}
(D_t-\nu\Delta)\lambda_i
={}&
-\lambda_i^2
-\frac14(\omega\cdot e_i)^2
+\frac14|\omega|^2
\\
&-
e_i^\top H_pe_i
\\
&-
2\nu
\sum_{k=1}^3
\sum_{j\ne i}
\frac{
|e_j^\top(\partial_kS)e_i|^2
}{
\lambda_i-\lambda_j
}.
\end{aligned}
}
\tag{6.2}
$$

This equation is only used directly in the simple spectrum region.

Eigenvalue collision requires spectral projection / generalized eigenvalue treatment; (6.2) cannot be unconditionally passed through the collision set.

---

# 7. Middle eigenvalue equation has two independent sign-indefinite channels

For:

$$
i=2,
$$

define:

$$
\mathcal G_2
=
-
2\nu
\sum_{k=1}^3
\left[
\frac{
|e_1^\top(\partial_kS)e_2|^2
}{
\lambda_2-\lambda_1
}
+
\frac{
|e_3^\top(\partial_kS)e_2|^2
}{
\lambda_2-\lambda_3
}
\right].
$$

Since:

$$
\lambda_2-\lambda_1>0,
$$

but:

$$
\lambda_2-\lambda_3<0,
$$

so the first part is non-positive, and the second part is non-negative.

Thus:

$$
\boxed{
\mathcal G_2
\text{ has no fixed sign}.
}
\tag{7.1}
$$

On the other hand, the pressure channel:

$$
\boxed{
\mathcal P_2
=
-
e_2^\top H_pe_2
}
\tag{7.2}
$$

also lacks a universal pointwise sign.

So:

$$
\boxed{
(D_t-\nu\Delta)\lambda_2
}
$$

is not controlled by a scalar sign-definite reaction-diffusion law of:

$$
\lambda_2
$$

This directly implies:

$$
\boxed{
\lambda_2\le0
}
$$

Although it is the safe conditional branch from Round 03,

it does not yield a simple scalar maximum principle from (6.2) to prove that this region is invariant for arbitrary NS data.

Status:

$$
\boxed{
\textbf{PROVED failure of the naive scalar maximum-principle architecture}.
}
\tag{7.3}
$$

This does not equate to proving that the safe region will necessarily be exited; it only means that this invariance cannot be established by a pointwise scalar sign argument that solely looks at $\lambda_2$.

---

# 8. Pressure trace does not solve the eigenvalue problem

Using (3.1):

$$
e_2^\top H_pe_2
=
-\frac13f_p
+
e_2^\top H_p^{\rm dev}e_2.
$$

So:

$$
\mathcal P_2
=
\frac13f_p
-
e_2^\top H_p^{\rm dev}e_2.
$$

The first term:

$$
\frac13
\left(
|S|^2-\frac12|\omega|^2
\right)
$$

is a local scalar.

But:

$$
e_2^\top H_p^{\rm dev}e_2
$$

remains a global anisotropic constraint channel.

Therefore, even if the pressure trace is completely substituted back into the local strain/vorticity amplitude:

$$
\boxed{
\text{anisotropic pressure feedback remains}.
}
\tag{8.1}
$$

---

# 9. Calderón–Zygmund control gives no criticality gain

Riesz transforms on:

$$
1<q<\infty
$$

satisfy:

$$
\|H_p\|_{L^q}
\le
C_q
\|f_p\|_{L^q}.
$$

From:

$$
f_p
=
|S|^2-\frac12|\omega|^2
$$

we obtain:

$$
\boxed{
\|H_p\|_{L^q}
\le
C_q
\left(
\|S\|_{L^{2q}}^2
+
\|\omega\|_{L^{2q}}^2
\right).
}
\tag{9.1}
$$

The Riesz operator is of order zero.

So:

$$
\boxed{
\text{pressure reconstruction does not create derivative gain}.
}
\tag{9.2}
$$

Nor does it provide a pointwise sign.

In other words, formally X-integrating:

$$
H_p
$$

into the state is legal:

$$
\boxed{
X_{\rm geom+p}
=
\int_{\rm pressure\ Poisson}
X_{\rm geom}.
}
\tag{9.3}
$$

However:

$$
\boxed{
\text{legal formation}
\neq
\text{coercive improvement}.
}
$$

---

# 10. Global pressure cancellation

A very important contrast now emerges.

For a smooth decaying incompressible field:

$$
\boxed{
\int_{\mathbb R^3}
S:H_p\,dx
=
0.
}
\tag{10.1}
$$

Proof:

Since the Hessian is symmetric:

$$
S:H_p
=
\partial_j u_i\,
\partial_{ij}p
$$

are equivalent under the integral.

Integrating by parts:

$$
\int
\partial_j u_i\,
\partial_{ij}p\,dx
=
-
\int
u_i
\partial_i\Delta p\,dx.
$$

Integrating again:

$$
-
\int
u_i
\partial_i\Delta p\,dx
=
\int
(\nabla\cdot u)
\Delta p\,dx
=
0.
$$

So the pressure Hessian vanishes in the global $L^2$ strain pairing.

This explains why the global strain-enstrophy identity can be written as:

$$
\boxed{
\frac d{dt}
\|S\|_2^2
=
-2\nu
\|\nabla S\|_2^2
-
4
\int
\det S\,dx
}
\tag{10.2}
$$

without an explicit pressure term.

---

# 11. But local spectral projection keeps the pressure channel

For $\lambda_2$:

$$
e_2^\top H_pe_2
$$

is generally not equal to zero.

So:

$$
\boxed{
\int S:H_p=0
}
$$

does not imply:

$$
\boxed{
e_2^\top H_pe_2=0.
}
$$

Therefore, global constraint cancellation and local spectral observation do not commute.

In X-integral language:

$$
\boxed{
\mathsf I_{\rm global\ pairing}
\circ
\mathsf I_{\rm pressure}
\neq
\mathsf O_{\rm local\ spectrum}
\circ
\mathsf I_{\rm pressure}.
}
\tag{11.1}
$$

More intuitively:

- If global pairing is done first, pressure is annihilated by the incompressibility constraint;
- If local eigenvalue evolution is observed first, the anisotropic pressure Hessian is retained.

This is the true **X-order noncommutativity** of this round.

---

# 12. Constraint–Observation Tradeoff

The geometric route of Round 03 requires:

$$
\lambda_2,
\quad
\sigma,
\quad
\det S
$$

and other local relational information.

Round 04 shows:

If the local spectrum is retained:

$$
\boxed{
\text{pressure anisotropy survives}.
}
$$

If global energy/enstrophy pairing is performed:

$$
\boxed{
\text{pressure disappears},
}
$$

but local spectral feedback is compressed into global integrated quantities.

Thus emerges the:

$$
\boxed{
\textbf{Constraint–Observation Tradeoff}.
}
\tag{12.1}
$$

Its form is:

$$
\boxed{
\begin{array}{c}
\text{local geometric resolution}
\\
\Downarrow
\\
\text{nonlocal pressure coupling retained}
\end{array}
}
$$

Whereas:

$$
\boxed{
\begin{array}{c}
\text{global incompressible pairing}
\\
\Downarrow
\\
\text{pressure cancellation}
\\
\Downarrow
\\
\text{loss of pointwise spectral feedback}
\end{array}
}
$$

This is not a logical contradiction.

It indicates that the two observation routes preserve different invariants.

---

# 13. Evolution of determinant does not close the hierarchy

For a trace-free $3\times3$ matrix:

$$
\operatorname{adj}S
=
S^2
-
\frac12|S|^2I.
$$

Therefore:

$$
D_t(\det S)
=
\operatorname{adj}S:D_tS.
$$

On the other hand:

$$
\Delta(\det S)
=
\operatorname{adj}S:\Delta S
+
\sum_{k=1}^3
D^2(\det)_S
[
\partial_kS,
\partial_kS
].
$$

So from (1.3):

$$
\boxed{
\begin{aligned}
(D_t-\nu\Delta)\det S
={}&
-
\operatorname{adj}S:
\left(
S^2
+
\frac14\omega\otimes\omega
-
\frac14|\omega|^2I
+
H_p
\right)
\\
&-
\nu
\sum_{k=1}^3
D^2(\det)_S
[
\partial_kS,
\partial_kS
].
\end{aligned}
}
\tag{13.1}
$$

Therefore, the determinant evolution introduces:

- pressure Hessian contraction;
- strain-gradient quadratic terms;
- vorticity-strain coupling.

There is no scalar sign closure.

So switching from:

$$
\lambda_2
$$

to:

$$
\det S
$$

will not eliminate the pressure/nonlocality problem.

---

# 14. Evolution of vorticity direction

The vorticity equation:

$$
D_t\omega
=
S\omega
+
\nu\Delta\omega.
$$

In the region where:

$$
|\omega|>0
$$

let:

$$
\xi
=
\frac{\omega}{|\omega|}.
$$

Then:

$$
\boxed{
D_t\xi
=
(I-\xi\otimes\xi)S\xi
+
\frac{\nu}{|\omega|}
(I-\xi\otimes\xi)\Delta\omega.
}
\tag{14.1}
$$

So the vorticity direction evolution already depends on:

$$
S\xi
$$

and:

$$
\Delta\omega.
$$

For:

$$
\sigma
=
\xi^\top S\xi
$$

we have:

$$
\boxed{
D_t\sigma
=
\xi^\top(D_tS)\xi
+
2(D_t\xi)^\top S\xi.
}
\tag{14.2}
$$

Substituting (1.3) and (14.1), there inevitably appears:

$$
\boxed{
-\xi^\top H_p\xi
}
\tag{14.3}
$$

as well as diffusion / higher-gradient terms.

So:

$$
\boxed{
\sigma
}
$$

is likewise not a local finite-dimensional closed scalar state.

---

# 15. Finite local geometry closure fails in the tested class

This round tests the finite relational local state:

$$
\mathcal G_k(x,t)
=
J^k
\left(
S,\omega
\right)(x,t),
$$

i.e., some finite spatial jet of strain / vorticity.

For the local spectrum:

$$
\lambda_2,
$$

determinant:

$$
\det S,
$$

alignment:

$$
\sigma,
$$

their exact evolution will all couple back to the global field via:

$$
H_p
=
\nabla^2(-\Delta)^{-1}f_p
$$

And Section 4 has proved that this operator is not a finite-order local differential operator of $f_p$.

Therefore, if the closure class is restricted to:

$$
\boxed{
\text{finite local differential functions of }
J^k(S,\omega),
}
$$

then it cannot exactly contain the pressure Hessian feedback.

So:

$$
\boxed{
\textbf{
Finite Local Geometry Closure fails for exact NS strain-spectrum evolution.
}
}
\tag{15.1}
$$

This is a restricted architecture no-go.

It does not rule out:

- global integral carriers;
- pseudodifferential carriers;
- nonlocal functionals;
- semigroup formulations;
- Lagrangian global geometry;
- infinite-but-continuous state descriptions.

---

# 16. First continuous constraint barrier

Therefore, the Pure-C route has not yet encountered:

$$
\mathsf C\to\mathsf D.
$$

Instead, it first encounters:

$$
\boxed{
\mathsf C_{\rm local}
\to
\mathsf C_{\rm global/nonlocal}.
}
\tag{16.1}
$$

Namely:

$$
\boxed{
\text{continuous local geometry}
\Longrightarrow
\text{continuous global elliptic constraint}.
}
$$

This is a finer transition than 'continuous vs. discrete':

$$
\boxed{
\textbf{
Local-C}
\to
\textbf{Nonlocal-C}.
}
\tag{16.2}
$$

This transition is forced by the incompressibility pressure constraint.

---

# 17. STOP-C07 — Local Geometry / Nonlocal Pressure Closure Gap

The primary X diagnostic of this round:

$$
\boxed{
\bot_X^{\mathrm{C07}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{geometry\ evolution},\\
\text{local\ state}=
(\lambda_2,\det S,\sigma,J^kS,J^k\omega),\\
\text{required\ carrier}=H_p^{\rm dev},\\
\text{operator}=
\nabla^2(-\Delta)^{-1},\\
\text{local\ finite\ closure}=\mathrm{impossible\ in\ tested\ class},\\
\text{global\ continuous\ closure}=\mathrm{legal},\\
\text{coercivity\ gain}=\mathrm{not\ obtained},\\
\text{discrete\ intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
\tag{17.1}
$$

Named:

$$
\boxed{
\textbf{STOP-C07:
Local-Geometry / Nonlocal-Pressure Closure Gap}.
}
$$

---

# 18. STOP-C08 — Global cancellation does not imply local feedback control

Another diagnostic:

$$
\boxed{
\bot_X^{\mathrm{C08}}
=
\left\langle
\begin{array}{l}
\text{layer}=\mathrm{constraint/observation\ ordering},\\
\text{global\ fact}=
\int S:H_p=0,\\
\text{local\ need}=
e_2^\top H_pe_2,\\
\text{failure}=
\mathrm{global\ cancellation}
\not\Rightarrow
\mathrm{local\ spectral\ sign},\\
\text{repair}=
\mathrm{nonlocal\ relational\ functional\ or\ new\ cancellation},\\
\text{discrete\ intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
\tag{18.1}
$$

Named:

$$
\boxed{
\textbf{STOP-C08:
Global-Cancellation / Local-Feedback Gap}.
}
$$

---

# 19. 24/72 Ledger — Round 04

| Step | X integral / object | $B$ | $U$ | $O$ | $L$ | Status |
|---|---|---|---|---|---|---|
| C29 | $\int_{\nabla u}$ | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | FORM |
| C30 | $\int_{D_tS}$ | $\mathsf C$ | $\mathsf S$ | relational | $\mathsf F$ | FORM |
| C31 | pressure Poisson | $\mathsf C$ | $\mathsf P$ constraint | $\mathsf X$ | $\mathsf F$ | FORM |
| C32 | $H_p=\nabla^2(-\Delta)^{-1}f_p$ | $\mathsf C$ | global/nonlocal | $\mathsf X$ | $\mathsf F$ | FORM |
| C33 | finite local reconstruction of $H_p$ | $\mathsf C$ | local | local scalar/vector | $\mathsf F$ | REFUTED in finite differential class |
| C34 | exact $\lambda_2$ evolution | $\mathsf C$ | hybrid $\mathsf S/\mathsf P$ | $\mathsf X$ | $\mathsf F$ | FORM on simple spectrum |
| C35 | scalar maximum principle for $\lambda_2$ | $\mathsf C$ | local | scalar | $\mathsf F$ | NOT AVAILABLE |
| C36 | determinant evolution | $\mathsf C$ | hybrid | $\mathsf X$ | $\mathsf F$ | FORM but not closed |
| C37 | alignment evolution | $\mathsf C$ | hybrid | $\mathsf X$ | $\mathsf F$ | FORM but not closed |
| C38 | global $S:H_p$ cancellation | $\mathsf C$ | global pairing | compressed | $\mathsf F$ | FORM |
| C39 | global cancellation $\to$ local pressure sign | $\mathsf C$ | — | local spectrum | $\mathsf F$ | ILLEGAL |
| C40 | unconditional geometry feedback | $\mathsf C$ | hybrid | $\mathsf X$ | $\mathsf F$ | OPEN |

---

# 20. What happened to the original continuous-vs-discrete question?

After four rounds:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

Instead the route has produced:

$$
\boxed{
\mathsf C_{\rm local}
\to
\mathsf C_{\rm critical}
\to
\mathsf C_{\rm relational}
\to
\mathsf C_{\rm global/nonlocal}.
}
\tag{20.1}
$$

So the continuous route is not exhausted.

It has internally changed its required information architecture.

The actual first hard transition so far is:

$$
\boxed{
\text{local continuum}
\to
\text{globally constrained continuum}.
}
\tag{20.2}
$$

This is directly caused by incompressibility.

---

# 21. Constraint and infinity

The user hypothesis motivating this program emphasized:

$$
\boxed{
\text{constraint}
+
\text{infinity}
+
\text{continuous/discrete}.
}
$$

Round 04 supplies the first precise connection.

The incompressibility constraint:

$$
\nabla\cdot u=0
$$

forces pressure to solve:

$$
-\Delta p=f_p.
$$

The inverse Laplacian:

$$
(-\Delta)^{-1}
$$

couples each point to an unbounded continuum of spatial points.

Thus the constraint does not merely remove one degree of freedom.

It introduces:

$$
\boxed{
\text{a global continuous dependency graph of infinite spatial extent}.
}
\tag{21.1}
$$

This is not a discrete infinity.

It is a continuum nonlocal constraint.

Therefore:

$$
\boxed{
\text{constraint}
\Longrightarrow
\text{nonlocal continuous infinity}
}
\tag{21.2}
$$

already appears before any essential discrete decomposition.

---

# 22. Why this still does not prove blow-up or regularity

Nonlocality alone does not imply failure.

In fact pressure can act as a regularizing redistribution mechanism.

The obstruction is narrower:

$$
\boxed{
\text{we do not yet have a sign/coercivity theorem
for the anisotropic pressure feedback
strong enough to force safe geometry globally}.
}
$$

So the current frontier is not:

> pressure is bad.

It is:

$$
\boxed{
\text{pressure constraint is exact and legal,
but its anisotropic feedback has not yet been converted into a global coercive invariant}.
}
\tag{22.1}
$$

---

# 23. Next round — Pure Continuous Nonlocal Cancellation / Projection Route

Round 04 shows that following local eigenvalues directly keeps the hard pressure channel.

The next continuous route should therefore reverse the order:

instead of trying to control:

$$
e_2^\top H_pe_2
$$

pointwise,

search for global/nonlocal functionals in which pressure or other dangerous terms cancel exactly.

Candidates:

$$
\langle S,H_p\rangle=0,
$$

Miller-type strain/vorticity orthogonality,

Leray projection identities,

nonlocal commutator structures,

Biot–Savart/Riesz cancellations,

global strain–vorticity interaction functionals.

The next X question:

$$
\boxed{
\text{Can a nonlocal continuous X integral preserve enough geometry
while retaining the exact global cancellations?}
}
$$

This is designed to attack the tradeoff:

$$
\boxed{
\text{local geometry}
\leftrightarrow
\text{global cancellation}.
}
$$

If yes, Pure-C continues.

If every such closure eventually requires countable scale extraction / profile decomposition / dyadic localization, that point will finally be recorded as:

$$
\boxed{
T_{\mathsf C\to\mathsf D}.
}
$$

---

# 24. External primary-source anchors

1. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - strain evolution;
   - exact enstrophy/strain identity;
   - middle-eigenvalue regularity criteria.

2. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain-vorticity interaction;
   - exact structural identities;
   - global regularity for a related interaction model;
   - advection/depletion analysis.

3. Borys Álvarez-Samaniego, Wilson P. Álvarez-Samaniego, Pedro G. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.
   - pressure reconstruction by Riesz transforms on the whole space.

4. Laurent Chevillard, Emmanuel Lévêque, Francesco Taddia, Charles Meneveau, Huidan Yu, Carlos Rosales, *Local and nonlocal pressure Hessian effects in real and synthetic fluid turbulence*, arXiv:1106.1046.
   - pressure-Hessian local/nonlocal roles in velocity-gradient dynamics.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Geometry\ Evolution},
\\
\text{Essential } \mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{New transition}
&:
\mathsf C_{\rm local}
\to
\mathsf C_{\rm global/nonlocal},
\\
\text{Update profile}
&:
\mathsf S_{\rm time}
+
\mathsf P_{\rm constraint},
\\
\text{Pressure reconstruction}
&:
\mathrm{exact\ continuous\ nonlocal},
\\
\text{Finite local pressure closure}
&:
\mathrm{refuted\ in\ differential\ class},
\\
\text{Naive }\lambda_2\text{ max principle}
&:
\mathrm{fails\ structurally},
\\
\text{STOP-C07}
&:
\mathrm{Local\ Geometry/Nonlocal\ Pressure\ Gap},
\\
\text{STOP-C08}
&:
\mathrm{Global\ Cancellation/Local\ Feedback\ Gap},
\\
\text{Next}
&:
\mathrm{Pure\ Continuous\ Nonlocal\ Cancellation/Projection}.
\end{aligned}
}
$$