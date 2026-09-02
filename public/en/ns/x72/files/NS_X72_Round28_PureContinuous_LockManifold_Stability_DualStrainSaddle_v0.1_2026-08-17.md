# NS × X Integral × 24/72 Paradigm Practice
## Round 28 — Pure Continuous Lock-Manifold Stability / Dual-Strain Saddle Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Lock-Stability Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round27_PureContinuous_CoherenceDynamics_AngularPhaseLocking_v0.1_2026-08-17.md`
- Objective of this round: Round 27 proved that sustained signed nonlocal coupling requires angular phase locking or strong modulation. This round performs a genuine linearization on the lock manifold, first extracting the frozen-strain principal dynamics, and then incorporating the moving eigenframe, viscosity, vorticity, pressure, and quotient gauge forcing. We examine whether the amplification-sign lock is attracting, repelling, saddle, or forced-neutral.
- Non-claims: This document does not prove that the lock manifold of actual Navier–Stokes dangerous trajectories is necessarily unstable, nor does it prove that intermediate-eigenvector alignment cannot be stabilized. This document proves that the frozen-strain leading subsystem possesses an exact dual stability and a common-lock saddle structure; the actual stability depends entirely on whether the additional frame/gauge/nonlocal forcing can overwrite this leading saddle.

---

# 0. Round 27 handoff

Round 27 established the:

$$
\boxed{
\mathcal C(t)=A(t)\cos\theta(t)
}
$$

-type signed coupling, as well as the nonstationary angular cancellation:

$$
|\theta'|\ge\Omega>0
\Longrightarrow
\text{cumulative signed coupling is suppressed by }O(\Omega^{-1}),
$$

unless the amplitude or phase-speed modulation is strong.

Meanwhile, the strain eigenframe rotation is:

$$
\boxed{
D_te_i
=
\sum_{j\ne i}
\frac{
\nu e_j^\top\Delta S e_i
-\frac14(\omega\cdot e_j)(\omega\cdot e_i)
-e_j^\top H_pe_i
}{
\lambda_i-\lambda_j
}
e_j.
}
\tag{0.1}
$$

where:

$$
-S^2
$$

has no direct off-diagonal frame rotation.

Round 27 STOP:

$$
\boxed{
\text{STOP-C31}
=
\text{Angular Phase-Locking / Coherence-Persistence Gap}.
}
$$

---

# 1. Frozen-strain vorticity-direction subsystem

First, take a fixed symmetric trace-free strain:

$$
S=S^\top,
$$

with eigenpairs:

$$
Se_i=\lambda_ie_i,
\qquad
\lambda_1<\lambda_2<\lambda_3.
$$

Ignoring:

- eigenframe rotation;
- viscosity;
- pressure forcing through frame motion.

The leading dynamics of the vorticity direction:

$$
\xi=\frac{\omega}{|\omega|}
$$

is:

$$
\boxed{
\dot\xi
=
P_\xi^\perp S\xi
=
S\xi
-
(\xi^\top S\xi)\xi.
}
\tag{1.1}
$$

Let:

$$
\sigma
=
\xi^\top S\xi.
$$

---

# 2. Vorticity direction is a Rayleigh-quotient ascent

From (1.1):

$$
\boxed{
\dot\sigma
=
2
\left(
|S\xi|^2-\sigma^2
\right)
\ge0.
}
\tag{2.1}
$$

Equality holds exactly at:

$$
S\xi\parallel\xi,
$$

which is the strain eigenvector direction.

Therefore, the frozen-strain vorticity direction is the gradient-ascent flow of the Rayleigh quotient on the sphere:

$$
\xi^\top S\xi
$$

---

# 3. Linear stability near a strain eigenvector

Let:

$$
\xi
=
e_i
+
\sum_{j\ne i}
\varepsilon_j e_j
+
O(|\varepsilon|^2).
$$

From (1.1):

$$
\boxed{
\dot\varepsilon_j
=
(\lambda_j-\lambda_i)
\varepsilon_j
+
O(|\varepsilon|^2).
}
\tag{3.1}
$$

Thus:

## alignment with $e_3$

$$
\lambda_j-\lambda_3<0
\qquad
(j=1,2),
$$

so:

$$
\boxed{
e_3
\text{ is locally attracting for frozen-strain vorticity direction}.
}
\tag{3.2}
$$

## alignment with $e_1$

$$
\lambda_j-\lambda_1>0
\qquad
(j=2,3),
$$

so:

$$
\boxed{
e_1
\text{ is repelling}.
}
\tag{3.3}
$$

## alignment with $e_2$

One transverse exponent is negative, and the other is positive:

$$
\boxed{
e_2
\text{ is a saddle}.
}
\tag{3.4}
$$

---

# 4. Why observed intermediate alignment is genuinely dynamical

Section 3 only describes:

$$
\boxed{
\text{frozen eigenframe + leading strain action}.
}
$$

In the actual NS:

- the eigenframe rotates;
- the pressure Hessian enters the eigenframe dynamics;
- viscosity enters the vorticity direction;
- the strain itself evolves;
- material stretching history matters.

Therefore:

$$
\boxed{
\text{instantaneous }e_2\text{ alignment}
}
$$

is not equivalent to a frozen-$S$ attracting fixed point.

If the actual dynamics favors:

$$
e_2,
$$

it must utilize structures outside the frozen-strain subsystem.

---

# 5. Frozen-strain optimal-quotient-direction subsystem

The Round 27 quotient direction equation is:

$$
D_tn
=
\nu P_n^\perp[\cdots]
-
P_n^\perp Sn
+
\frac12\omega\times n
+
r^{-1}P_n^\perp\nabla\chi_g.
$$

Retaining only the frozen strain principal term:

$$
\boxed{
\dot n
=
-
P_n^\perp Sn
=
-
Sn
+
(n^\top Sn)n.
}
\tag{5.1}
$$

Let:

$$
\tau
=
n^\top Sn.
$$

---

# 6. Quotient direction is a Rayleigh-quotient descent

From (5.1):

$$
\boxed{
\dot\tau
=
-2
\left(
|Sn|^2-\tau^2
\right)
\le0.
}
\tag{6.1}
$$

Therefore, the strain-only dynamics of the quotient direction is the gradient-descent flow of the same Rayleigh quotient.

Thus:

$$
\boxed{
\xi
\text{ climbs strain Rayleigh quotient},
\qquad
n
\text{ descends it}.
}
\tag{6.2}
$$

Named:

$$
\boxed{
\textbf{Dual Strain Gradient-Flow Structure}.
}
$$

---

# 7. Quotient-direction eigenvector stability

Let:

$$
n
=
e_i
+
\sum_{j\ne i}
\eta_j e_j
+
O(|\eta|^2).
$$

From (5.1):

$$
\boxed{
\dot\eta_j
=
(\lambda_i-\lambda_j)
\eta_j
+
O(|\eta|^2).
}
\tag{7.1}
$$

Thus:

$$
\boxed{
e_1
\text{ attracts }n,
}
\tag{7.2}
$$

$$
\boxed{
e_3
\text{ repels }n,
}
\tag{7.3}
$$

and:

$$
\boxed{
e_2
\text{ is again a saddle}.
}
\tag{7.4}
$$

This is completely dual to the vorticity-direction stability.

---

# 8. Exact strain-only alignment equation between $\xi$ and $n$

Define:

$$
\boxed{
q
=
\xi\cdot n.
}
\tag{8.1}
$$

Using:

$$
\dot\xi
=
S\xi-\sigma\xi,
$$

and:

$$
\dot n
=
-Sn+\tau n,
$$

Since $S$ is symmetric:

$$
n\cdot S\xi
=
\xi\cdot Sn.
$$

so the cross terms cancel:

$$
\boxed{
\dot q
=
(\tau-\sigma)q.
}
\tag{8.2}
$$

Therefore:

- $q=0$ is invariant;
- $q=\pm1$ is fixed if both are simultaneously located at the same eigenvector;
- alignment growth is determined by the difference in the strain Rayleigh quotients seen from the two directions.

---

# 9. Common eigenvector lock has paired opposite exponents

Consider the common lock:

$$
\xi=n=e_i.
$$

For a transverse direction:

$$
e_j,
\qquad
j\ne i,
$$

the vorticity perturbation is:

$$
\boxed{
\dot\varepsilon_j
=
(\lambda_j-\lambda_i)\varepsilon_j.
}
$$

the quotient-direction perturbation is:

$$
\boxed{
\dot\eta_j
=
-(\lambda_j-\lambda_i)\eta_j.
}
$$

Thus, each transverse strain gap:

$$
\Delta_{ji}
=
\lambda_j-\lambda_i
$$

generates a pair:

$$
\boxed{
+\Delta_{ji},
\qquad
-\Delta_{ji}.
}
\tag{9.1}
$$

If the spectrum is simple:

$$
\Delta_{ji}\ne0.
$$

Therefore, the common lock transverse subsystem must have one growing mode and one decaying mode.

---

# 10. Dual-Strain Common-Lock Saddle Theorem

From Section 9:

$$
\boxed{
\textbf{
in the frozen-strain principal subsystem,
a common lock }\xi=n=e_i
\textbf{ is never asymptotically attracting for simple strain spectrum.}
}
\tag{10.1}
$$

More precisely:

$$
\boxed{
\text{transverse Lyapunov exponents occur in }\pm|\lambda_j-\lambda_i|\text{ pairs}.
}
\tag{10.2}
$$

Therefore, the common vorticity–quotient-direction lock requires additional dynamics to possibly stabilize.

---

# 11. Middle-eigenvector common lock is doubly saddle-like

For:

$$
i=2,
$$

vorticity:

$$
\lambda_1-\lambda_2<0,
\qquad
\lambda_3-\lambda_2>0.
$$

the quotient direction has exactly the opposite signs:

$$
\lambda_2-\lambda_1>0,
\qquad
\lambda_2-\lambda_3<0.
$$

So near:

$$
e_2
$$

- $\xi$ has one stable and one unstable direction;
- $n$ also has one stable and one unstable direction;
- the unstable transverse directions are complementary.

Therefore:

$$
\boxed{
\textbf{
simultaneous }\xi\approx n\approx e_2
\textbf{ requires genuine multi-frame balancing}.
}
}
\tag{11.1}
$$

---

# 12. Moving-eigenframe coefficient equations

Returning to the actual NS.

Define:

$$
a_i
=
\xi\cdot e_i,
$$

$$
b_i
=
n\cdot e_i.
$$

Let the eigenframe angular-velocity coefficients be:

$$
\boxed{
\Omega_{ji}
=
e_j\cdot D_te_i,
}
\tag{12.1}
$$

Then:

$$
\Omega_{ji}
=
-\Omega_{ij}.
$$

From Round 27:

$$
\boxed{
\Omega_{ji}
=
\frac{
\nu e_j^\top\Delta S e_i
-\frac14(\omega\cdot e_j)(\omega\cdot e_i)
-e_j^\top H_pe_i
}{
\lambda_i-\lambda_j
}
}
\tag{12.2}
$$

for:

$$
j\ne i.
$$

---

# 13. Exact vorticity coefficients in the moving eigenframe

Let:

$$
\mathcal V_\omega
=
\nu
P_\xi^\perp
\frac{\Delta\omega}{|\omega|}.
$$

Then:

$$
\boxed{
D_ta_i
=
(\lambda_i-\sigma)a_i
+
e_i\cdot\mathcal V_\omega
+
\sum_j
a_j\Omega_{ji}.
}
\tag{13.1}
$$

Thus, the frozen-strain stability exponent:

$$
\lambda_i-\sigma
$$

is now continuously driven by:

- viscous angular forcing;
- eigenframe rotation;

---

# 14. Exact quotient coefficients in the moving eigenframe

Define the non-strain quotient angular forcing:

$$
\boxed{
\begin{aligned}
\mathcal F_n
={}&
\nu
P_n^\perp
[
\Delta n+2\nabla\log r\cdot\nabla n]
\\
&+
\frac12\omega\times n
+
\frac1r
P_n^\perp\nabla\chi_g.
\end{aligned}
}
\tag{14.1}
$$

Then:

$$
D_tn
=
-P_n^\perp Sn
+
\mathcal F_n.
$$

Therefore:

$$
\boxed{
D_tb_i
=
-(\lambda_i-\tau)b_i
+
e_i\cdot\mathcal F_n
+
\sum_j
b_j\Omega_{ji}.
}
\tag{14.2}
$$

The actual quotient-direction lock can be re-stabilized or re-destabilized by:

- viscosity;
- vorticity rotation;
- gauge feedback;
- eigenframe rotation;

---

# 15. Linearized forced common-lock system

Near:

$$
\xi\approx n\approx e_i
$$

, for:

$$
j\ne i,
$$

let the transverse variables be:

$$
z_j
=
\begin{pmatrix}
a_j\\
b_j
\end{pmatrix}.
$$

The leading linear part is:

$$
\boxed{
D_tz_j
=
\begin{pmatrix}
\lambda_j-\lambda_i & 0\\
0 & \lambda_i-\lambda_j
\end{pmatrix}
z_j
+
F_j
+
\mathcal C_jz
+
O(|z|^2).
}
\tag{15.1}
$$

where:

$$
F_j
$$

collects the following at the lock-point:

- viscous vorticity-direction forcing;
- quotient gauge/vorticity/viscous forcing;
- eigenframe forcing;

and:

$$
\mathcal C_j
$$

collects their first-order variations and mode coupling.

The principal matrix trace is:

$$
0,
$$

and the determinant is:

$$
\boxed{
-(\lambda_j-\lambda_i)^2<0.
}
\tag{15.2}
$$

Therefore, for the additional forcing / coupling to make the common lock stable, it must genuinely overwrite the principal saddle.

---

# 16. Spectral collision is a separate degeneracy channel

When:

$$
|\lambda_i-\lambda_j|
\to0,
$$

the frozen-strain saddle exponent:

$$
|\lambda_i-\lambda_j|
$$

becomes small.

However, the Round 27 eigenframe rotation coefficients:

$$
\Omega_{ji}
$$

simultaneously contain:

$$
\frac1{\lambda_i-\lambda_j}.
$$

Thus, near spectral collision:

$$
\boxed{
\text{principal alignment attraction/repulsion weakens,
while frame sensitivity can strengthen}.
}
\tag{16.1}
$$

Therefore, the simple-spectrum linearization cannot be uniformly extended to eigenvalue collisions.

This is a continuous spectral-degeneracy branch, not a discrete intrusion.

---

# 17. Pressure-coherence lock needs a tangent error, not only $c$

The Round 27 pressure tensor coherence is:

$$
c_P
=
\widehat S:\widehat{\mathbb Q}_P.
$$

At perfect lock:

$$
c_P=1.
$$

But if:

$$
\widehat S=\widehat{\mathbb Q}_P,
$$

since both tangent velocities are orthogonal to themselves,

we immediately have:

$$
\boxed{
\dot c_P=0
}
\tag{17.1}
$$

regardless of whether the lock is stable.

Therefore, the scalar:

$$
c_P
$$

contains no first-order stability information at the perfect lock.

What is genuinely needed is the tangent-space error:

$$
\boxed{
\delta_P
=
\widehat{\mathbb Q}_P-\widehat S.
}
\tag{17.2}
$$

and:

$$
\boxed{
1-c_P
=
\frac12|\delta_P|^2.
}
\tag{17.3}
$$

---

# 18. Generic tangent lock-error equation

Let:

$$
U=\widehat S,
\qquad
V=\widehat{\mathbb Q}_P,
$$

and:

$$
\delta=V-U.
$$

Then exactly:

$$
\boxed{
\frac12
\frac d{dt}
|\delta|^2
=
\delta:
(\dot V-\dot U).
}
\tag{18.1}
$$

On the lock manifold:

$$
U=V,
$$

If:

$$
\boxed{
\dot V-\dot U\ne0,
}
\tag{18.2}
$$

then the tangent vector error is immediately forced away from the lock.

If:

$$
\dot V-\dot U=0
$$

on the manifold,

only then do we need to study the linearized relative angular operator:

$$
\boxed{
\dot\delta
=
\mathcal J_{\rm rel}\delta
+
O(|\delta|^2).
}
\tag{18.3}
$$

The necessary condition for the lock to be locally attracting is:

$$
\boxed{
\lambda_{\max}
\left(
\operatorname{sym}\mathcal J_{\rm rel}
\right)
<0.
}
\tag{18.4}
$$

---

# 19. No universal sign for the relative angular Jacobian

From Round 27, it is known that:

$$
D_t\widehat S
$$

contains:

- the pressure Hessian;
- the vorticity dyad;
- viscosity;
- the self-amplification shape term.

The remote quadrupole dynamics also contains:

- source motion;
- line-of-sight motion;
- remote source reorientation;
- amplitude normalization.

These terms have no universal sign relation.

Therefore, there is no purely algebraic universal statement:

$$
\boxed{
\operatorname{sym}\mathcal J_{\rm rel}
\le
-\kappa I
}
\tag{19.1}
$$

that deduces:

$$
\lambda_2>0,
\quad
Q,
\quad
|S|,
\quad
|\omega|
$$

---

# 20. Neutral-lock structural witness

Consider a local structural model:

- $S$ is constant;
- the eigenframe is fixed;
- the line of sight:
  $$
  e
  $$
  is fixed;
- the remote quadrupole is fixed.

Then:

$$
\widehat S,
\qquad
\widehat{\mathbb Q}_P
$$

are all constant.

Therefore:

$$
\boxed{
\dot c_P=0
}
$$

for all initial coherences.

Thus, there can be:

$$
\boxed{
\text{neutral persistent amplification-sign coherence}
}
$$

without restoring or dephasing.

This witness is not a whole-space finite-energy NS solution.

What it rules out is the purely geometric inference that:

$$
\boxed{
\text{all nontrivial locks are automatically unstable}
}
$$

---

# 21. Conditional lock-stability lemma

Consider the tangent lock error:

$$
z(t)
$$

satisfying:

$$
\boxed{
z'
=
A(t)z+f(t).
}
\tag{21.1}
$$

If:

$$
\boxed{
\lambda_{\max}
\left(
\frac{
A+A^\top
}{2}
\right)
\le
-\kappa(t)
}
\tag{21.2}
$$

and:

$$
\kappa(t)\ge0,
$$

Then:

$$
\boxed{
\frac d{dt}|z|
\le
-\kappa(t)|z|
+
|f(t)|.
}
\tag{21.3}
$$

Therefore:

$$
\boxed{
|z(t)|
\le
e^{-\int_{t_0}^t\kappa}
|z(t_0)|
+
\int_{t_0}^t
e^{-\int_s^t\kappa}
|f(s)|ds.
}
\tag{21.4}
$$

Thus, a stable phase lock requires two things:

1. a negative transverse angular Jacobian;
2. small off-manifold forcing.

---

# 22. Lock-attraction margin

Define:

$$
\boxed{
\kappa_{\rm lock}(t)
=
-
\lambda_{\max}
\left(
\operatorname{sym}\mathcal J_{\rm rel}(t)
\right).
}
\tag{22.1}
$$

Interpretation:

$$
\kappa_{\rm lock}>0
$$

represents instantaneous attraction;

$$
\kappa_{\rm lock}<0
$$

represents instantaneous transverse instability;

$$
\kappa_{\rm lock}=0
$$

represents a neutral/center direction.

Next, define the forcing ratio:

$$
\boxed{
\mathfrak F_{\rm lock}
=
\frac{
|f|
}{
\kappa_{\rm lock}|z|
}
}
\tag{22.2}
$$

for:

$$
\kappa_{\rm lock}>0,\quad z\ne0.
$$

If:

$$
\mathfrak F_{\rm lock}\ll1,
$$

lock attraction dominates.

---

# 23. Frozen-strain common lock has negative attraction margin

The common lock principal matrix from Section 10 is:

$$
A_j
=
\begin{pmatrix}
\Delta_{ji} & 0\\
0 & -\Delta_{ji}
\end{pmatrix}.
$$

Its symmetric part is itself.

So:

$$
\lambda_{\max}
=
|\Delta_{ji}|.
$$

Therefore:

$$
\boxed{
\kappa_{\rm lock}^{\rm frozen}
=
-|\lambda_j-\lambda_i|
<0.
}
\tag{23.1}
$$

for a simple spectrum.

That is, the frozen-strain common lock is not marginal:

$$
\boxed{
\textbf{it is a genuine saddle instability.}
}
$$

---

# 24. Stabilization burden

If the actual NS is to turn the common lock of:

$$
\xi\approx n\approx e_i
$$

into an attracting one,

the additional angular dynamics must provide a transverse correction that at least exceeds the unstable gap rate of:

$$
\boxed{
|\lambda_j-\lambda_i|
}
$$

Thus, the stabilizing burden can be written as:

$$
\boxed{
\mathcal D_{\rm extra}
\gtrsim
|\lambda_j-\lambda_i|.
}
\tag{24.1}
$$

where:

$$
\mathcal D_{\rm extra}
$$

must come from:

- pressure-driven eigenframe rotation;
- viscous direction diffusion;
- vorticity/gauge rotation;
- correlated multi-frame coupling.

This is a genuine rate competition.

---

# 25. Vorticity strongest-direction lock versus quotient weakest-direction lock

The frozen-strain leading dynamics each have a stable branch:

$$
\boxed{
\xi\to e_3,
}
\tag{25.1}
$$

$$
\boxed{
n\to e_1.
}
\tag{25.2}
$$

So the generic strain-only tendency is:

$$
\boxed{
\text{vorticity and quotient direction separate toward opposite strain extremes}.
}
\tag{25.3}
$$

This implies that the Round 26 transverse depletion factor:

$$
|\xi\times n|
$$

does not approach zero in this simplified asymptotic picture,

but tends toward:

$$
\boxed{
|\xi\times n|\to1
}
$$

if:

$$
e_1\perp e_3.
$$

Therefore, the strain-only dynamics itself will not use:

$$
\xi\parallel n
$$

to shut down the cross-strain amplitude.

---

# 26. But amplitude persistence still does not fix signed phase

Even if:

$$
|\xi\times n|
$$

remains order-one,

the Round 27 pair coupling still has the signed phase:

$$
\psi_{BS}
=
2(n\cdot e)(m\cdot e)
$$

Therefore:

$$
\boxed{
\text{transverse amplitude persistence}
\neq
\text{signed coherence persistence}.
}
$$

It still requires a multi-frame lock of:

$$
e,
\quad
n,
\quad
\xi
$$

---

# 27. Stability classification after Round 28

Currently, angular locks can be classified as:

## Type A — strain-only individual attractors

$$
\xi\to e_3,
\qquad
n\to e_1.
$$

## Type B — common-direction lock

frozen-strain:

$$
\boxed{
\text{saddle}.
}
$$

## Type C — pressure/tensor coherence lock

Requires the relative angular Jacobian:

$$
\mathcal J_{\rm rel}.
$$

Has no universal sign.

## Type D — forced lock

Even if the principal dynamics are unstable,

external pressure/gauge/viscous feedback can continuously press the system near the lock manifold.

Therefore, persistent danger can arise from:

$$
\boxed{
\text{stable lock}
\vee
\text{forced lock}
\vee
\text{neutral persistence}.
}
$$

---

# 28. STOP-C32 — Dual-Strain Saddle / Lock-Stability Forcing Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{lock\text{-}manifold\ stability},
\\
\text{vorticity frozen-strain flow}
&=
\mathrm{Rayleigh\ ascent},
\\
\text{quotient-direction frozen-strain flow}
&=
\mathrm{Rayleigh\ descent},
\\
\text{vorticity stable direction}
&=
e_3,
\\
\text{quotient stable direction}
&=
e_1,
\\
\text{common eigenvector lock}
&=
\mathrm{saddle\ for\ simple\ spectrum},
\\
\text{middle-eigenvector common lock}
&=
\mathrm{multi\text{-}frame\ saddle},
\\
\text{actual stabilization}
&=
\mathrm{pressure}
+
\mathrm{viscosity}
+
\mathrm{vorticity}
+
\mathrm{gauge}
+
\mathrm{frame\ dynamics},
\\
\text{missing}
&=
\mathrm{unconditional\ sign/control\ of\ relative\ angular\ Jacobian
and\ lock\ forcing},
\\
T_{\mathsf C\to\mathsf D}
&=
\mathrm{NOT\ REACHED}.
\end{aligned}
}
$$

Named:

$$
\boxed{
\textbf{STOP-C32:
Dual-Strain Saddle / Lock-Stability Forcing Gap}.
}
$$

---

# 29. 24/72 Ledger — Round 28

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C380 | frozen vorticity direction flow | $\mathsf C$ | angular ODE | relational | $\mathsf F$ | EXACT |
| C381 | vorticity Rayleigh ascent | $\mathsf C$ | gradient flow | scalar | $\mathsf F$ | PROVED |
| C382 | vorticity eigenvector stability | $\mathsf C$ | linearization | targeted | $\mathsf F$ | PROVED |
| C383 | frozen quotient direction flow | $\mathsf C$ | angular ODE | relational | $\mathsf F$ | EXACT |
| C384 | quotient Rayleigh descent | $\mathsf C$ | gradient flow | scalar | $\mathsf F$ | PROVED |
| C385 | quotient eigenvector stability | $\mathsf C$ | linearization | targeted | $\mathsf F$ | PROVED |
| C386 | $\xi\cdot n$ exact strain-only law | $\mathsf C$ | relational | scalar | $\mathsf F$ | EXACT |
| C387 | common-lock paired exponents | $\mathsf C$ | linearization | relational | $\mathsf F$ | PROVED |
| C388 | common-lock saddle theorem | $\mathsf C$ | stability | targeted | $\mathsf F$ | PROVED |
| C389 | moving eigenframe coefficients | $\mathsf C$ | frame transport | relational | $\mathsf F$ | EXACT |
| C390 | vorticity moving-frame equation | $\mathsf C$ | coupled angular PDE | relational | $\mathsf F$ | EXACT |
| C391 | quotient moving-frame equation | $\mathsf C$ | gauge/angular PDE | relational | $\mathsf F$ | EXACT |
| C392 | forced common-lock linearization | $\mathsf C$ | stability | $\mathsf X$ | $\mathsf F$ | FORM |
| C393 | spectral-collision branch | $\mathsf C$ | degeneracy | relational | $\mathsf F$ | IDENTIFIED |
| C394 | tensor tangent lock error | $\mathsf C$ | manifold stability | $\mathsf X$ | $\mathsf F$ | EXACT |
| C395 | relative angular Jacobian criterion | $\mathsf C$ | linearization | targeted | $\mathsf F$ | CONDITIONAL |
| C396 | neutral-lock witness | $\mathsf C$ | structural model | targeted | $\mathsf F$ | CONSTRUCTED |
| C397 | conditional lock-stability lemma | $\mathsf C$ | Gronwall | scalar | $\mathsf F$ | PROVED |
| C398 | frozen common-lock attraction | $\mathsf C$ | stability | scalar | $\mathsf F$ | REFUTED |
| C399 | unconditional actual lock stability sign | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C32 |

---

# 30. Continuous-versus-discrete status

This round uses:

- continuous sphere dynamics;
- continuous eigenframe transport;
- tangent-space linearization;
- continuous Lyapunov / attraction rates;
- continuous spectral gaps:
  $$
  \lambda_i-\lambda_j.
  $$

The finite eigenvalue label:

$$
i=1,2,3
$$

is merely the finite spectral notation for a $3\times3$ symmetric tensor.

The entire result can be rewritten using spectral projectors.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 31. Strongest results of Round 28

## R28-A — Dual Strain Gradient Flow

$$
\boxed{
\xi'=
P_\xi^\perp S\xi
}
$$

is a Rayleigh ascent;

$$
\boxed{
n'=
-P_n^\perp Sn
}
$$

is a Rayleigh descent.

## R28-B — Opposite individual attractors

$$
\boxed{
\xi\to e_3,
\qquad
n\to e_1
}
$$

in a frozen simple strain.

## R28-C — Common-lock saddle theorem

$$
\boxed{
\xi=n=e_i
}
$$

has transverse exponents forming:

$$
\boxed{
\pm|\lambda_j-\lambda_i|
}
$$

pairs, so the common lock cannot be asymptotically attracted by the strain-only principal dynamics.

## R28-D — Moving-frame forcing requirement

An actual stable common lock must rely on pressure / viscosity / vorticity / gauge / frame dynamics to genuinely overcome the unstable strain-gap rate.

## R28-E — Scalar coherence is insufficient at perfect lock

When:

$$
c=1
$$

$$
c'=0
$$

holds automatically.

Lock stability must be determined by the tangent-space error and the relative angular Jacobian.

---

# 32. Next round — Lock-Stability Energy / Frame-Forcing Budget

The next round will no longer just write:

$$
\mathcal J_{\rm rel}.
$$

It will directly attack:

$$
\boxed{
\text{Does the extra frame/gauge forcing have enough budget to maintain an unstable lock for a long time?}
}
$$

Questions:

1. A stable/forced common lock needs to overcome:
   $$
   |\lambda_j-\lambda_i|;
   $$
2. Whether the pressure-Hessian off-diagonal forcing has an integrable budget;
3. Whether the viscosity frame forcing:
   $$
   \nu\Delta S
   $$
   will form damping rather than persistent forcing;
4. Whether the gauge-direction forcing:
   $$
   r^{-1}P_n^\perp\nabla\chi_g
   $$
   can maintain the lock for a long time in the low-amplitude region;
5. Define the cumulative lock-work:
   $$
   \mathcal W_{\rm lock};
   $$
6. If a persistent amplification lock requires an infinite / critical forcing budget, it may form a new continuation criterion;
7. Only if the budget itself can be provided by the existing energy is there a chance to genuinely close the phase-locking route;
8. Still do not discretize frame states.

---

# 33. External primary-source anchors

1. Alex Encinas-Bartos, George Haller, *Vorticity Alignment with Lyapunov Vectors and Rate-of-Strain Eigenvectors*, arXiv:2310.17267.
   - Primary-source background for material stretching, vorticity alignment, and viscous-flow intermediate strain-eigenvector estimates.

2. Alain Pumir, Eberhard Bodenschatz, Haitao Xu, *Tetrahedron deformation and alignment of perceived vorticity and strain in a turbulent flow*, arXiv:1204.5857.
   - DNS/experimental primary-source background for instantaneous intermediate alignment and the evolution of vorticity toward the strongest eigendirection under a fixed strain eigenframe.

3. B. Galanti, J. D. Gibbon, M. Heritage, *Vorticity alignment results for the three-dimensional Euler and Navier-Stokes equations*, arXiv:chao-dyn/9709003.
   - Primary-source background for vorticity–strain alignment variables, pressure-Hessian-driven alignment dynamics, and attracting alignment states under additional assumptions.

The dual Rayleigh-flow identities, common-lock saddle theorem, moving-eigenframe coefficient equations, tangent lock-error criterion, and conditional stability lemma in this round are all directly derived in this document.

---

# 34. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Lock\text{-}Manifold\ Stability},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Vorticity principal flow}
&=
\mathrm{strain\ Rayleigh\ ascent},
\\
\text{Quotient principal flow}
&=
\mathrm{strain\ Rayleigh\ descent},
\\
\text{Common lock}
&=
\mathrm{frozen\text{-}strain\ saddle},
\\
\text{Stable actual lock}
&=
\mathrm{requires\ extra\ angular\ stabilization},
\\
\text{Middle alignment}
&=
\mathrm{requires\ moving\text{-}frame/nonlocal/viscous\ organization},
\\
\text{STOP-C32}
&=
\mathrm{Dual\text{-}Strain\ Saddle/Lock\text{-}Stability\ Forcing\ Gap},
\\
\text{Next}
&=
\mathrm{Lock\text{-}Stability\ Energy/Frame\text{-}Forcing\ Budget}.
\end{aligned}
}
$$