# NS × X-Integral × 24/72 Paradigm In Practice
## Round 02 — Pure Critical Continuous Carrier Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Critical Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round01_PureContinuous_EnergyRoute_v0.1_2026-08-16.md`
- Objective of this round: Without introducing essential discrete tools, switch to a scale-critical carrier to test whether it is possible to bypass `STOP-C01` and `STOP-C02` from Round 01, forming an unconditional global regularity closure.
- Non-assertion: This round only evaluates the pure continuous critical-carrier architectures tested herein; it does not claim to rule out all possible pure continuous proofs.

---

# 0. Round 01 handoff

Round 01 yielded:

$$
\boxed{
u\in
L_t^\infty L_x^2
\cap
L_t^2\dot H_x^1
}
$$

and the energy interpolation family:

$$
\boxed{
\frac2q+\frac3p=\frac32.
}
$$

while the Serrin critical line is:

$$
\boxed{
\frac2q+\frac3p=1.
}
$$

Therefore:

$$
\boxed{
\text{STOP-C01}
=
\text{Energy-to-Critical Scaling Gap}.
}
$$

The vorticity/enstrophy route yielded:

$$
Y(t)
=
\|\omega(t)\|_2^2,
$$

$$
Y'
\lesssim
\nu^{-3}Y^3,
$$

which fails to provide an arbitrary-data global a priori bound, hence:

$$
\boxed{
\text{STOP-C02}
=
\text{Vortex-Stretching Coercivity Gap}.
}
$$

Most importantly:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

Thus, this round maintains:

$$
\boxed{
B=\mathsf C.
}
$$

---

# 1. NS scaling and critical carrier

Navier–Stokes scaling:

$$
u_\lambda(x,t)
=
\lambda
u(\lambda x,\lambda^2 t),
$$

$$
p_\lambda(x,t)
=
\lambda^2
p(\lambda x,\lambda^2t).
$$

This scaling keeps the viscosity $\nu$ invariant.

For the Lebesgue norm:

$$
\|u_\lambda(t)\|_{L^p}
=
\lambda^{1-\frac3p}
\|u(\lambda^2t)\|_{L^p}.
$$

Therefore:

$$
\boxed{
p=3
}
$$

is the velocity Lebesgue critical exponent:

$$
\boxed{
\|u_\lambda(t)\|_3
=
\|u(\lambda^2t)\|_3.
}
\tag{1.1}
$$

For the homogeneous Sobolev norm:

$$
\|u_\lambda(t)\|_{\dot H^s}
=
\lambda^{s-\frac12}
\|u(\lambda^2t)\|_{\dot H^s}.
$$

Thus:

$$
\boxed{
s=\frac12
}
$$

is the critical Sobolev index:

$$
\boxed{
\|u_\lambda(t)\|_{\dot H^{1/2}}
=
\|u(\lambda^2t)\|_{\dot H^{1/2}}.
}
\tag{1.2}
$$

For the mixed norm:

$$
\|u_\lambda\|_{L_t^qL_x^p}
=
\lambda^{1-\frac3p-\frac2q}
\|u\|_{L_t^qL_x^p}.
$$

Therefore:

$$
\boxed{
\frac2q+\frac3p=1
}
\tag{1.3}
$$

which is the scale-critical Serrin line.

The strategy for this round is:

$$
\boxed{
\text{No longer force criticality from a subcritical energy carrier;
directly establish the X-integral chain in the critical layer.}
}
$$

---

# 2. X-integral graph: critical formation and global control must be separated

Definition:

$$
X_{\rm crit}
=
\int_{\rm scaling}
X_{\rm NS}.
$$

Candidate continuous critical observations include:

$$
\mathcal A_{H}(u)
=
\|u\|_{\dot H^{1/2}},
$$

$$
\mathcal A_{3}(u)
=
\|u\|_{L^3},
$$

and the critical Kato heat-flow norm.

This round strictly distinguishes four different X-integral steps:

$$
\boxed{
\begin{aligned}
&\mathsf I_{\rm form}:
X_{\rm NS}
\rightsquigarrow
X_{\rm crit},
\\
&\mathsf I_{\rm local}:
X_{\rm crit}
\rightsquigarrow
\text{local strong solution},
\\
&\mathsf I_{\rm criterion}:
\text{bounded critical carrier}
\rightsquigarrow
\text{regularity},
\\
&\mathsf I_{\rm global}:
X_{\rm NS}
\rightsquigarrow
\text{global bounded critical carrier}.
\end{aligned}
}
\tag{2.1}
$$

The validity of the first three cannot be conflated with the validity of the fourth.

What the Navier–Stokes Millennium closure truly lacks is:

$$
\boxed{
\mathsf I_{\rm global}.
}
\tag{2.2}
$$

---

# 3. Pure-Critical Route A — $\dot H^{1/2}$

Let:

$$
\Lambda
=
(-\Delta)^{1/2}.
$$

Define:

$$
Y(t)
=
\|u(t)\|_{\dot H^{1/2}}^2
=
\|\Lambda^{1/2}u(t)\|_2^2,
$$

and:

$$
Z(t)
=
\|u(t)\|_{\dot H^{3/2}}^2
=
\|\Lambda^{3/2}u(t)\|_2^2.
$$

For the Leray-projected NS:

$$
\partial_tu
-
\nu\Delta u
+
\mathbb P(u\cdot\nabla u)
=
0
$$

taking the $L^2$ pairing with $\Lambda u$:

$$
\boxed{
\frac12Y'(t)
+
\nu Z(t)
=
-
\langle
\mathbb P(u\cdot\nabla u),
\Lambda u
\rangle.
}
\tag{3.1}
$$

---

# 4. Continuous product estimate without dyadic decomposition

This round prohibits the use of Littlewood–Paley dyadic shells as a core tool.

Using the 3D Sobolev embedding:

$$
\dot H^{1/2}
\hookrightarrow
L^3,
$$

and:

$$
\dot H^{3/2}
\ni u
\Longrightarrow
\nabla u\in\dot H^{1/2}
\hookrightarrow
L^3.
$$

Therefore:

$$
\|u\cdot\nabla u\|_{L^{3/2}}
\le
\|u\|_3
\|\nabla u\|_3
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}.
$$

By the dual Sobolev embedding:

$$
L^{3/2}
\hookrightarrow
\dot H^{-1/2},
$$

we obtain:

$$
\boxed{
\|
\mathbb P(u\cdot\nabla u)
\|_{\dot H^{-1/2}}
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}.
}
\tag{4.1}
$$

On the other hand:

$$
\|\Lambda u\|_{\dot H^{1/2}}
=
\|u\|_{\dot H^{3/2}}.
$$

Thus, by the $\dot H^{-1/2}$–$\dot H^{1/2}$ dual pairing:

$$
\boxed{
\left|
\langle
\mathbb P(u\cdot\nabla u),
\Lambda u
\rangle
\right|
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}^2.
}
\tag{4.2}
$$

Substituting into (3.1):

$$
\boxed{
\frac12Y'
+
\left(
\nu
-
C\sqrt{Y}
\right)
Z
\le
0.
}
\tag{4.3}
$$

This is the first critical equality-interface of this round.

---

# 5. Small-data closure

If:

$$
\|u_0\|_{\dot H^{1/2}}
\le
\delta_\nu
$$

and we choose:

$$
C\delta_\nu
\le
\frac{\nu}{2},
$$

then within the bootstrap region:

$$
\nu
-
C\|u(t)\|_{\dot H^{1/2}}
\ge
\frac{\nu}{2}.
$$

Therefore:

$$
\boxed{
\frac12Y'
+
\frac{\nu}{2}Z
\le
0.
}
\tag{5.1}
$$

Thus, the critical norm does not increase, and the bootstrap closes itself.

This recovers the core energy geometry of the Fujita–Kato type small-critical-data global mechanism:

$$
\boxed{
\text{critical carrier}
+
\text{small amplitude}
\Longrightarrow
\text{viscous absorption}.
}
\tag{5.2}
$$

---

# 6. Large-data barrier

If:

$$
C\|u(t)\|_{\dot H^{1/2}}
>
\nu,
$$

then the coercive coefficient in (4.3):

$$
\nu
-
C\|u(t)\|_{\dot H^{1/2}}
$$

loses its positive sign.

Therefore, the standard critical energy estimate itself can only provide:

$$
\boxed{
\text{smallness-conditioned coercivity}.
}
$$

It cannot provide:

$$
\boxed{
\text{arbitrary-amplitude coercivity}.
}
$$

Therefore:

$$
\boxed{
\Gamma_{\mathsf C,\dot H^{1/2}}
\not\vdash
\int_{\rm global\ coercivity}
X_{\dot H^{1/2}}
\;\operatorname{form}
}
\tag{6.1}
$$

under the current single-carrier estimate framework.

Definition:

$$
\boxed{
\textbf{STOP-C03:
Critical-Amplitude Absorption Gap}.
}
\tag{6.2}
$$

Note:

$$
\boxed{
\text{STOP-C03}
\neq
\text{no large-data critical-space proof can exist}.
}
$$

It only rules out the current single $\dot H^{1/2}$ absorption architecture as an unconditional closure.

---

# 7. Critical Scaling Fixed-Point Lemma

Here emerges a structural fact more fundamental than "the estimate is not strong enough."

From (1.2):

$$
\mathcal A_H(u)
=
\|u\|_{\dot H^{1/2}}
$$

satisfies:

$$
\boxed{
\mathcal A_H(u_\lambda)
=
\mathcal A_H(u).
}
\tag{7.1}
$$

Similarly:

$$
\boxed{
\mathcal A_3(u_\lambda)
=
\mathcal A_3(u).
}
\tag{7.2}
$$

Therefore, if critical absorption requires:

$$
\mathcal A(u)
<
\delta,
$$

while the original state satisfies:

$$
\mathcal A(u)
\ge
\delta,
$$

then any NS symmetry scaling:

$$
u
\mapsto
u_\lambda
$$

cannot change this fact.

Therefore:

$$
\boxed{
\textbf{
critical scaling cannot turn large critical data into small critical data.
}
}
\tag{7.3}
$$

This can be written as an X-integral fixed point:

$$
\boxed{
\mathsf I_{\rm scale}
\left(
\mathcal A_{\rm crit}
\right)
=
\mathcal A_{\rm crit}.
}
\tag{7.4}
$$

Therefore:

$$
\boxed{
\text{Scale}
}
$$

is no longer an amplitude-repair operator in the critical layer.

It only changes:

- spatial location of detail;
- temporal scale;
- physical amplitude and wavelength jointly;

but it does not change the magnitude of the critical carrier.

This is an important structural no-go for this round.

---

# 8. Pure-Critical Route B — $L^\infty_tL^3_x$

$L^3$ is a scaling-critical space.

The known endpoint regularity theorem states:

For an appropriate Navier–Stokes strong / suitable weak solution, if it is maintained within a finite time window:

$$
\boxed{
u\in L^\infty(0,T;L^3(\mathbb R^3)),
}
\tag{8.1}
$$

then no finite-time singularity will occur at $T$.

Therefore, if we can unconditionally prove:

$$
\boxed{
\sup_{0<t<T_\ast}
\|u(t)\|_3
<
\infty
}
\tag{8.2}
$$

holds for every finite $T_\ast$, then the regularity closure is established.

Thus:

$$
\boxed{
\mathsf I_{\rm criterion}^{L^3}
}
$$

is valid.

What is truly missing is:

$$
\boxed{
\mathsf I_{\rm global}^{L^3}.
}
$$

---

# 9. Energy closure to $L^3$ only yields $L_t^4$

Round 01 energy bounds:

$$
u\in
L_t^\infty L_x^2
\cap
L_t^2L_x^6.
$$

For each time:

$$
\|u(t)\|_3
\le
\|u(t)\|_2^{1/2}
\|u(t)\|_6^{1/2}.
$$

Taking the fourth power:

$$
\|u(t)\|_3^4
\le
\|u(t)\|_2^2
\|u(t)\|_6^2.
$$

Integrating over time:

$$
\int_0^T
\|u(t)\|_3^4dt
\le
\left(
\sup_{0<t<T}
\|u(t)\|_2^2
\right)
\int_0^T
\|u(t)\|_6^2dt.
$$

Therefore:

$$
\boxed{
u\in L_t^4L_x^3.
}
\tag{9.1}
$$

However:

$$
L^4(0,T)
\not\hookrightarrow
L^\infty(0,T).
$$

For example:

$$
f(t)
=
(T-t)^{-\alpha}
$$

for:

$$
0<\alpha<\frac14
$$

satisfies:

$$
f\in L^4(0,T)
$$

but:

$$
\sup_{0<t<T}f(t)
=
\infty.
$$

Therefore, solely from the energy bounds:

$$
\boxed{
L_t^4L_x^3
\not\Rightarrow
L_t^\infty L_x^3.
}
\tag{9.2}
$$

This is a functional-space non-implication; it does not assert that the NS solution will necessarily produce such a spike.

Thus:

$$
\boxed{
\Gamma_{\rm energy}
\not\vdash
\int_{L_t^\infty L_x^3}
X_{\rm energy}
\;\operatorname{form}.
}
\tag{9.3}
$$

Definition:

$$
\boxed{
\textbf{STOP-C04:
Endpoint-in-Time Critical Control Gap}.
}
\tag{9.4}
$$

---

# 10. Relationship between $\dot H^{1/2}$ and $L^3$

Sobolev embedding:

$$
\boxed{
\dot H^{1/2}
\hookrightarrow
L^3.
}
\tag{10.1}
$$

So if we can establish a uniform:

$$
\sup_{t<T}
\|u(t)\|_{\dot H^{1/2}}
<
\infty,
$$

then we at least obtain:

$$
\sup_{t<T}
\|u(t)\|_3
<
\infty.
$$

However, Route A has shown that the standard $\dot H^{1/2}$ energy architecture only possesses smallness-conditioned absorption.

Therefore, Route A and Route B converge under the current framework to:

$$
\boxed{
\text{unconditional global critical-amplitude control is missing}.
}
\tag{10.2}
$$

---

# 11. Pure-Critical Route C — Kato / Duhamel continuous route

Writing the mild formulation:

$$
\boxed{
u(t)
=
e^{\nu t\Delta}u_0
-
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot
(u\otimes u)(s)
\,ds.
}
\tag{11.1}
$$

The entire equation is completely composed of:

- continuous time integral;
- continuous heat semigroup;
- continuous convolution;
- deterministic transition;

Therefore:

$$
\boxed{
B=\mathsf C,
\qquad
L=\mathsf F.
}
$$

Essential discrete concepts have still not been introduced.

---

# 12. Taking the $L^3\to L^6$ Kato norm as an example

Define:

$$
\boxed{
\|u\|_{\mathcal K_6(T)}
=
\sup_{0<t<T}
t^{1/4}
\|u(t)\|_6.
}
\tag{12.1}
$$

This norm remains invariant under NS scaling.

Heat estimate:

$$
\|e^{\nu t\Delta}f\|_6
\le
C
(\nu t)^{-1/4}
\|f\|_3.
$$

Therefore:

$$
\boxed{
\|e^{\nu t\Delta}u_0\|_{\mathcal K_6(T)}
\le
C\nu^{-1/4}
\|u_0\|_3.
}
\tag{12.2}
$$

For the bilinear term:

$$
B(u,v)(t)
=
-
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot
(u\otimes v)(s)
\,ds.
$$

heat-kernel derivative estimate:

$$
\|
e^{\nu(t-s)\Delta}
\mathbb P\nabla\cdot F
\|_6
\le
C
(\nu(t-s))^{-3/4}
\|F\|_3.
$$

and:

$$
\|u\otimes v\|_3
\le
\|u\|_6
\|v\|_6.
$$

If:

$$
M_u
=
\|u\|_{\mathcal K_6(T)},
$$

$$
M_v
=
\|v\|_{\mathcal K_6(T)},
$$

then:

$$
\|u(s)\|_6
\le
M_us^{-1/4},
$$

$$
\|v(s)\|_6
\le
M_vs^{-1/4}.
$$

Therefore:

$$
\|B(u,v)(t)\|_6
\le
C\nu^{-3/4}
M_uM_v
\int_0^t
(t-s)^{-3/4}
s^{-1/2}
\,ds.
$$

Beta scaling:

$$
\int_0^t
(t-s)^{-3/4}
s^{-1/2}
ds
=
C_\beta
t^{-1/4}.
$$

Thus:

$$
\boxed{
\|B(u,v)\|_{\mathcal K_6(T)}
\le
C_\ast
\nu^{-3/4}
\|u\|_{\mathcal K_6(T)}
\|v\|_{\mathcal K_6(T)}.
}
\tag{12.3}
$$

This is a fully continuous scale-critical quadratic fixed-point estimate.

---

# 13. Local large-data formation and global small-data closure

For:

$$
u_0\in L^3,
$$

the short-time Kato norm of the heat flow can be made, via approximation + heat smoothing, to satisfy:

$$
\boxed{
\|e^{\nu t\Delta}u_0\|_{\mathcal K_6(T)}
\to0
\qquad
(T\downarrow0).
}
\tag{13.1}
$$

Therefore, arbitrary $L^3$ data can form a local mild solution.

That is:

$$
\boxed{
\mathsf I_{\rm local}^{L^3}
\;\operatorname{form}.
}
\tag{13.2}
$$

But to perform a single contraction directly at:

$$
T=\infty
$$

(12.2)–(12.3) require the linear critical size to be sufficiently small.

Thus, small $L^3$ data:

$$
\|u_0\|_3
\ll
\nu
$$

can establish the global contraction closure.

For arbitrary large data, this set of scale-critical bilinear estimates does not provide a single global contraction.

Therefore:

$$
\boxed{
\textbf{STOP-C05:
Global Critical Fixed-Point Gap}.
}
\tag{13.3}
$$

---

# 14. Why shortening time works locally, but not directly globally

Two things must be distinguished here.

The critical spatial norm:

$$
\|u_0\|_3
$$

is invariant under NS scaling.

But the local Kato profile:

$$
\sup_{0<t<T}
t^{1/4}
\|e^{\nu t\Delta}u_0\|_6
$$

for a fixed $u_0\in L^3$ can approach zero as:

$$
T\downarrow0
$$

This is why arbitrary large critical data still possess local well-posedness.

However, if the maximal existence time:

$$
T_\ast<\infty,
$$

to continuously restart all the way to $T_\ast$, one needs to control the critical profile of each restart state:

$$
u(t_0)
$$

If critical concentration continues to intensify, the local lifespan can continuously shorten.

Currently, there is no deduction solely from the energy identity that:

$$
\inf_{t_0<T_\ast}
T_{\rm local}(u(t_0))
>
0.
$$

Therefore, local formation does not equal global closure.

---

# 15. Common structure of the three critical routes

Current tests:

## Route A

$$
\dot H^{1/2}
$$

yields:

$$
\frac12Y'
+
\left(
\nu-C\sqrt{Y}
\right)Z
\le0.
$$

Obstacle:

$$
\boxed{
\text{large critical amplitude destroys direct absorption}.
}
$$

## Route B

$$
L_t^\infty L_x^3
$$

is a sufficient regularity interface, but energy only provides:

$$
L_t^4L_x^3.
$$

Obstacle:

$$
\boxed{
\text{critical endpoint-in-time bound lacks an a priori bridge}.
}
$$

## Route C

critical Duhamel / Kato contraction.

Obstacle:

$$
\boxed{
\text{quadratic fixed point is globally contractive only in a small critical regime}.
}
$$

Convergence of the three:

$$
\boxed{
\textbf{
Critical-Carrier Formation
\neq
Critical-Carrier Global Control.
}
}
\tag{15.1}
$$

---

# 16. Critical Amplitude Barrier Principle

This round extracts a methodological no-go.

Suppose a pure-continuous critical energy architecture possesses:

$$
\boxed{
\frac d{dt}
\mathcal A(u)^2
+
\left(
\nu
-
C\mathcal A(u)
\right)
\mathcal D(u)^2
\le0,
}
\tag{16.1}
$$

where:

$$
\mathcal A(u_\lambda)
=
\mathcal A(u).
$$

Then:

1. If:

$$
C\mathcal A(u_0)<\nu,
$$

small-data coercivity can be established via absorption;

2. If:

$$
C\mathcal A(u_0)\ge\nu,
$$

the inequality itself does not provide a positive dissipation coefficient;

3. Due to critical scaling invariance:

$$
\mathcal A(u_\lambda)
=
\mathcal A(u),
$$

the large-amplitude branch cannot be mapped back to the small regime via NS rescaling.

Therefore:

$$
\boxed{
\textbf{
a single scale-invariant amplitude carrier with only
smallness-based viscous absorption cannot by itself close arbitrary-data global regularity.
}
}
\tag{16.2}
$$

This is a no-go for this architecture, not a no-go for all continuous proofs.

---

# 17. New signal in the 24 paradigm: It may not be the $B$-axis that transitions first, but the $O$-axis

From Round 01 to Round 02, it has not yet been necessary to set:

$$
B=\mathsf D.
$$

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

But currently, all three critical routes compress the complex state into a single critical amplitude:

$$
\|u\|_{\dot H^{1/2}},
$$

$$
\|u\|_3,
$$

or:

$$
\|u\|_{\mathcal K_6}.
$$

These carriers can:

- detect criticality;
- form a local theory;
- achieve closure under smallness;
- perform regularity recognition under bounded endpoint conditions;

but they cannot independently generate arbitrary-data global coercivity.

Thus, a candidate observation mode transition emerges:

$$
\boxed{
\mathsf O_{\mathsf C}
\longrightarrow
\mathsf O_{\mathsf X}.
}
\tag{17.1}
$$

Here, $\mathsf X$ does not mean "unmeasurable."

It indicates that the next round should examine:

> Does there not exist a single scalar critical carrier that simultaneously preserves the closure information required for nonlinear geometry, alignment, sign, transport, pressure coupling, and dissipation?

It has not yet been proven that:

$$
\boxed{
O=\mathsf X
}
$$

is a necessary observation mode for NS.

Therefore, (17.1) is only marked as:

$$
\boxed{
\text{CANDIDATE TRANSITION}.
}
$$

It is a proposition to be tested in the next round.

---

# 18. The 4th axis of 72: This round remains entirely in $\mathsf F$

This round did not introduce:

$$
\mathsf K
$$

classical probability kernels,

nor did it introduce:

$$
\mathsf Q
$$

quantum channels.

All routes are deterministic:

$$
\boxed{
L=\mathsf F.
}
$$

Therefore, the current obstacle is not:

$$
\mathsf F
\to
\mathsf K
$$

or:

$$
\mathsf F
\to
\mathsf Q.
$$

The more precise 72 diagnosis at present is:

$$
\boxed{
\langle
\mathsf C;
\mathsf S;
\mathsf C;
\mathsf F
\rangle
}
$$

can already form a critical local theory and conditional regularity theory, but unconditional global coercivity is not closed.

---

# 19. Round 02 24/72 Ledger

| Step | Carrier / X-integral | $B$ | $U$ | $O$ | $L$ | Status |
|---|---|---|---|---|---|---|
| C08 | $\int_{\rm scaling}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C09 | $\int_{\dot H^{1/2}}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C10 | $\int_{\rm critical\ energy}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C11 | $\int_{\rm arbitrary\ amplitude\ coercivity}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |
| C12 | $\int_{L^3}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C13 | bounded $L^\infty_tL^3_x\to$ regularity | $\mathsf C$ | $\mathsf R$ meta-step | $\mathsf C$ | $\mathsf F$ | FORM / known criterion |
| C14 | energy $\to L^\infty_tL^3_x$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |
| C15 | $\int_{\rm Duhamel/Kato}$ | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C16 | local arbitrary $L^3$ fixed point | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | FORM |
| C17 | global arbitrary $L^3$ contraction | $\mathsf C$ | $\mathsf S$ | $\mathsf C$ | $\mathsf F$ | NOT CERTIFIED |
| C18 | $\mathsf C\to\mathsf X$ observation transition | $\mathsf C$ | — | $\mathsf X$ candidate | $\mathsf F$ | OPEN |

Wherein for C13:

$$
\mathsf R
$$

only indicates "the proof meta-layer uses a known regularity criterion for recognition."

It does not imply that the NS physical evolution itself changes from:

$$
\mathsf S
$$

to:

$$
\mathsf R.
$$

---

# 20. X-Failure Diagnosis Objects

## STOP-C03

$$
\boxed{
\bot_X^{\mathrm{C03}}
=
\left\langle
\begin{array}{l}
\text{layer}=\dot H^{1/2}\text{ critical coercivity},\\
\text{reason}=\text{critical amplitude enters dissipation coefficient},\\
\text{available}=
\nu-C\|u\|_{\dot H^{1/2}},\\
\text{closure}=\text{smallness only},\\
\text{scale repair}=\text{impossible by NS symmetry},\\
\text{discrete intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

## STOP-C04

$$
\boxed{
\bot_X^{\mathrm{C04}}
=
\left\langle
\begin{array}{l}
\text{layer}=L^\infty_tL^3_x,\\
\text{reason}=\text{endpoint-in-time control missing},\\
\text{available}=L^4_tL^3_x,\\
\text{needed}=L^\infty_tL^3_x,\\
\text{discrete intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

## STOP-C05

$$
\boxed{
\bot_X^{\mathrm{C05}}
=
\left\langle
\begin{array}{l}
\text{layer}=\text{critical Kato fixed point},\\
\text{reason}=\text{quadratic global contraction requires small critical profile},\\
\text{local formation}=\mathrm{true},\\
\text{global arbitrary amplitude}=\mathrm{not\ certified},\\
\text{discrete intrusion}=\mathrm{false}
\end{array}
\right\rangle.
}
$$

---

# 21. The true new conclusion of this round

Round 01 showed:

$$
\boxed{
\text{energy carrier is too subcritical}.
}
$$

Round 02 shows:

$$
\boxed{
\text{moving directly to a critical scalar carrier fixes the scaling mismatch,
but exposes an amplitude/geometry closure gap}.
}
$$

Therefore, the obstruction advances from:

$$
\boxed{
\text{ScaleMismatch}
}
$$

to:

$$
\boxed{
\text{CriticalAmplitude/StructureMismatch}.
}
$$

This is a strict frontier reduction.

---

# 22. Current status of the Pure-C route

The current pure continuous route:

$$
\boxed{
\begin{aligned}
\mathsf C
&\xrightarrow{\rm energy}
\mathsf C
\\
&\xrightarrow{\rm critical\ carrier}
\mathsf C
\\
&\xrightarrow{\rm local\ theory}
\mathsf C
\\
&\xrightarrow{\rm global\ control}
\operatorname{STOP}.
\end{aligned}
}
$$

instead of:

$$
\mathsf C
\to
\mathsf D.
$$

Thus, the second round still has not found an essential discrete intrusion.

However, for the first time, a new candidate appears:

$$
\boxed{
\text{Substrate space remains }\mathsf C,
\quad
\text{observation mode may require }\mathsf X.
}
$$

In other words:

$$
\boxed{
\text{The next transition may occur first on the observation axis,
rather than the substrate axis.}
}
$$

---

# 23. Next round: Pure Continuous Relational / Geometric Route

The next round still prohibits essential discretization.

Objective:

$$
\boxed{
\text{Do not use a single critical amplitude;
instead, preserve the nonlinear geometry itself.}
}
$$

Candidate continuous relational carriers:

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
\lambda_2(S),
$$

$$
\omega^\top S\omega,
$$

$$
\text{vorticity direction field},
$$

$$
\text{strain-vorticity alignment},
$$

$$
\text{helicity / local flux / pressure-strain coupling}.
$$

The next round will test:

1. Whether a fully continuous multi-carrier X-state can be established:

$$
X_{\rm geom}
=
\int_{\rm relation}
(u,S,\omega,p,\text{alignment},\text{flux});
$$

2. Whether it truly requires:

$$
O=\mathsf X
$$

instead of a single scalar observation;

3. Whether geometric depletion can allow the nonlinear term to acquire a sign or subcritical gain;

4. If it fails, is the failure:

$$
\text{geometry not coercive},
$$

or:

$$
\text{geometry requires discrete scale extraction}.
$$

Only the latter would declare a true:

$$
T_{\mathsf C\to\mathsf D}.
$$

---

# 24. External source anchors

1. H. Fujita and T. Kato, *On the Navier-Stokes initial value problem. I*, Archive for Rational Mechanics and Analysis 16 (1964), 269–315. DOI: `10.1007/BF00276188`.

2. L. Escauriaza, G. A. Seregin, V. Šverák, *$L_{3,\infty}$-solutions of the Navier-Stokes equations and backward uniqueness*, Russian Mathematical Surveys 58(2) (2003), 211–250. DOI: `10.1070/RM2003v058n02ABEH000609`.

3. I. Gallagher, G. S. Koch, F. Planchon, *A profile decomposition approach to the $L^\infty_t(L^3_x)$ Navier-Stokes regularity criterion*, Math. Ann. 355 (2013), 1527–1559. arXiv: `1012.0145`.

4. J.-Y. Chemin and P. Zhang, *On the critical one component regularity for 3-D Navier-Stokes system*, arXiv: `1310.6442`.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route} &: \mathrm{Pure\ Continuous\ Critical},\\
\text{First\ essential\ D\ intrusion} &: \mathrm{Not\ reached},\\
\text{STOP-C03} &: \mathrm{Critical\ amplitude\ absorption\ gap},\\
\text{STOP-C04} &: \mathrm{Endpoint\ }L^\infty_tL^3_x\mathrm{\ control\ gap},\\
\text{STOP-C05} &: \mathrm{Global\ critical\ fixed\ point\ gap},\\
\text{Scaling repair} &: \mathrm{No,\ critical\ carrier\ is\ invariant},\\
\text{Candidate transition} &: \mathsf O_{\mathsf C}\to\mathsf O_{\mathsf X},\\
\text{Next} &: \mathrm{Pure\ Continuous\ Relational/Geometric\ Route}.
\end{aligned}
}
$$