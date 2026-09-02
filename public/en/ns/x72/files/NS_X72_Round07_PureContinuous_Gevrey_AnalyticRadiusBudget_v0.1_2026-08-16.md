# NS × X-Integral × 24/72 Paradigm in Practice
## Round 07 — Pure Continuous Gevrey Resummation / Analytic-Radius Budget Route

- Date:  2026-08-16
- Version:  v0.1
- Status:  Proof-Route Experiment / Continuous-Only Gevrey Resummation Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round:  `NS_X72_Round06_PureContinuous_ContinuousHierarchy_SpectralCovariance_v0.1_2026-08-16.md`
- This round's objective:  To resum the real-order Sobolev hierarchy from Round 06 into a single Gevrey / analytic generating carrier, determining whether the "infinite derivative hierarchy" is truly an unclosable obstruction for Pure-C; and to establish an adaptive analytic-radius budget, compressing potential singular escape into a single continuous radius exhaustion problem.
- Non-claims:  This document does not achieve three-dimensional Navier–Stokes global regularity. It establishes continuous hierarchy resummation and analytic-radius budget reduction.

---

# 0. Round 06 handoff

Round 06 established for any real number:

$$
s\ge0
$$

the following:

$$
M_s
=
\|\Lambda^sS\|_2^2,
$$

$$
\alpha_s
=
\frac{
T_s
}{
\nu M_{s+1}
},
$$

$$
\kappa_s
=
\frac{
M_{s+1}
}{
M_s
},
$$

and obtained the exact hierarchy law:

$$
\boxed{
\kappa_s'
=
2\nu\kappa_s
\left[
(\alpha_{s+1}-\alpha_s)\kappa_s
+
(\alpha_{s+1}-1)
(\kappa_{s+1}-\kappa_s)
\right].
}
\tag{0.1}
$$

The Fourier probability measure:

$$
d\mu_s(\xi)
=
\frac{
|\xi|^{2s}
|\widehat S(\xi)|^2
}{
M_s
}
d\xi
$$

yields:

$$
\kappa_s
=
\mathbb E_{\mu_s}
|\xi|^2,
$$

and:

$$
V_s
=
\operatorname{Var}_{\mu_s}
(|\xi|^2).
$$

and obtained the continuous spectral-covariance law:

$$
\boxed{
\kappa_s'
=
2\kappa_s
(g_{s+1}-g_s)
-
2\nu V_s.
}
\tag{0.2}
$$

The STOP condition of Round 06:

$$
\boxed{
\text{STOP-C10}
=
\text{Continuous Hierarchy-Slope / Spectral-Covariance Gap}.
}
$$

However, it remained unanswered at the time:

> Can the infinite hierarchy itself be compressed at once by a continuous generating carrier?

This round directly answers this question.

---

# 1. Projected strain seed

In the smooth rapidly decaying whole-space class, using:

$$
\Lambda
=
(-\Delta)^{1/2}.
$$

the projected strain equation is:

$$
\boxed{
\partial_tS
+
\nu\Lambda^2S
=
F,
}
\tag{1.1}
$$

where:

$$
F
=
\frac12
P_{st}(\omega\otimes\omega)
-
\mathcal R.
$$

This round does not need to further expand:

$$
F
$$

into its full tensor structure.

It is solely utilized as an exact nonlinear transfer carrier.

---

# 2. Gevrey generating carrier

For:

$$
\tau\ge0,
\qquad
s\ge0,
$$

define:

$$
\boxed{
\mathcal G_{\tau,s}(t)
=
\left\|
e^{\tau\Lambda}
\Lambda^sS(t)
\right\|_2^2.
}
\tag{2.1}
$$

In Fourier form:

$$
\boxed{
\mathcal G_{\tau,s}
=
\int_{\mathbb R^3}
e^{2\tau|\xi|}
|\xi|^{2s}
|\widehat S(\xi)|^2
\,d\xi.
}
\tag{2.2}
$$

This is a fully continuous spectral carrier.

It does not use:

- dyadic shells;
- integer Fourier mode partitions;
- finite Galerkin indices;
- derivative-order recursions.

Its primary coordinates are:

$$
\boxed{
(\tau,s,\xi)
\in
[0,\infty)
\times
[0,\infty)
\times
\mathbb R^3.
}
$$

---

# 3. Continuous Hierarchy Resummation Theorem

## Theorem 3.1

Assume:

$$
\mathcal G_{\tau,s}<\infty
$$

for some:

$$
\tau>0.
$$

Arbitrarily choose:

$$
0\le\tau'<\tau
$$

and any real number:

$$
a\ge0.
$$

Let:

$$
\delta
=
\tau-\tau'>0.
$$

Then:

$$
\boxed{
\mathcal G_{\tau',s+a}
\le
\left(
\frac{a}{e\delta}
\right)^{2a}
\mathcal G_{\tau,s}
}
\tag{3.1}
$$

where for:

$$
a=0
$$

the multiplicative factor on the right-hand side is defined as:

$$
1.
$$

### Proof

By definition:

$$
\mathcal G_{\tau',s+a}
=
\int
e^{2\tau'|\xi|}
|\xi|^{2s+2a}
|\widehat S|^2d\xi.
$$

Rewrite:

$$
e^{2\tau'|\xi|}
|\xi|^{2s+2a}
=
\left(
|\xi|^{2a}
e^{-2\delta|\xi|}
\right)
e^{2\tau|\xi|}
|\xi|^{2s}.
$$

For:

$$
r\ge0,
$$

the function:

$$
r^{2a}e^{-2\delta r}
$$

attains its maximum at:

$$
r=\frac{a}{\delta}
$$

, and:

$$
\sup_{r\ge0}
r^{2a}e^{-2\delta r}
=
\left(
\frac{a}{e\delta}
\right)^{2a}.
$$

Thus, (3.1) is obtained.

$$
\square
$$

---

# 4. Meaning of the resummation theorem

Theorem 3.1 indicates:

If a certain:

$$
\boxed{
\mathcal G_{\tau,s}
}
$$

is bounded under a positive analytic radius:

$$
\tau>0
$$

then for every real derivative increment:

$$
a\ge0
$$

and every smaller radius:

$$
\tau'<\tau
$$

we have:

$$
\boxed{
\|e^{\tau'\Lambda}\Lambda^{s+a}S\|_2
<\infty.
}
$$

Therefore, the infinite hierarchy of Round 06:

$$
\left\{
M_s
\right\}_{s\ge0}
$$

does not require order-by-order closure.

As long as a Gevrey carrier with:

$$
\boxed{
\tau>0
}
$$

remains controlled,

all higher derivative levels are simultaneously absorbed.

Thus:

$$
\boxed{
\textbf{
Infinite derivative hierarchy is not, by itself,
an essential obstruction to Pure-C.
}
}
\tag{4.1}
$$

The hierarchy representation problem of Round 06 has been resummed.

---

# 5. Gevrey norm is a continuous spectral exponential moment

Define:

$$
r
=
|\xi|.
$$

Let:

$$
e(\xi,t)
=
|\widehat S(\xi,t)|^2.
$$

Then:

$$
\mathcal G_{\tau,s}
=
\int
e^{2\tau r}
r^{2s}
e(\xi,t)
d\xi.
$$

Therefore, it is the exponential moment of the continuous spectral measure with respect to:

$$
e^{2\tau r}
$$

The X-integral in this round can be written as:

$$
\boxed{
X_{\rm Gevrey}
=
\int_{\rm exp\ spectral\ weight}
X_{\rm hierarchy}.
}
\tag{5.1}
$$

Its function is not to add another derivative.

Rather, it preserves the entire high-frequency tail at once.

---

# 6. Exact time-dependent Gevrey balance

Allow the analytic radius:

$$
\tau=\tau(t)
$$

to vary with time.

Define:

$$
G
=
\mathcal G_{\tau,s},
$$

$$
K
=
\left\|
e^{\tau\Lambda}
\Lambda^{s+\frac12}S
\right\|_2^2,
$$

$$
H
=
\left\|
e^{\tau\Lambda}
\Lambda^{s+1}S
\right\|_2^2.
$$

Differentiating:

$$
\mathcal G_{\tau(t),s}
$$

Since:

$$
\partial_t
e^{\tau(t)\Lambda}
=
\tau'(t)
\Lambda
e^{\tau(t)\Lambda},
$$

from (1.1) we obtain:

$$
\boxed{
\frac12
G'
+
\nu H
=
\tau'K
+
T_{\tau,s},
}
\tag{6.1}
$$

where:

$$
\boxed{
T_{\tau,s}
=
\left\langle
e^{\tau\Lambda}
\Lambda^sF,
e^{\tau\Lambda}
\Lambda^sS
\right\rangle.
}
\tag{6.2}
$$

This is the exact balance of the analytic generating carrier.

---

# 7. Analytic spectral probability measure

If:

$$
G>0,
$$

define:

$$
\boxed{
d\mu_{\tau,s}(\xi)
=
\frac{
e^{2\tau|\xi|}
|\xi|^{2s}
|\widehat S(\xi)|^2
}{
G
}
d\xi.
}
\tag{7.1}
$$

Then:

$$
\mu_{\tau,s}
$$

is a probability measure.

Define:

$$
\boxed{
m_{\tau,s}
=
\mathbb E_{\mu_{\tau,s}}[r]
=
\frac{K}{G},
}
\tag{7.2}
$$

and:

$$
\boxed{
\kappa_{\tau,s}
=
\mathbb E_{\mu_{\tau,s}}[r^2]
=
\frac{H}{G}.
}
\tag{7.3}
$$

and define:

$$
\boxed{
V_{\tau,s}
=
\operatorname{Var}_{\mu_{\tau,s}}(r)
=
\kappa_{\tau,s}
-
m_{\tau,s}^2
\ge0.
}
\tag{7.4}
$$

---

# 8. Exact nonlinear growth rate

Define the weighted nonlinear growth rate:

$$
\boxed{
g_{\tau,s}
=
\frac{
T_{\tau,s}
}{
G
}.
}
\tag{8.1}
$$

If:

$$
\kappa_{\tau,s}>0,
$$

define the analytic nonlinear/dissipation ratio:

$$
\boxed{
\alpha_{\tau,s}
=
\frac{
g_{\tau,s}
}{
\nu\kappa_{\tau,s}
}
=
\frac{
T_{\tau,s}
}{
\nu H
}.
}
\tag{8.2}
$$

From (6.1):

$$
\boxed{
\frac12
\frac d{dt}
\log G
=
\nu
(\alpha_{\tau,s}-1)
\kappa_{\tau,s}
+
\tau'
m_{\tau,s}.
}
\tag{8.3}
$$

This is the core exact identity of this round.

---

# 9. Fixed-radius interpretation

If:

$$
\tau'=0,
$$

then:

$$
\boxed{
\frac12
\frac d{dt}
\log G
=
\nu
(\alpha_{\tau,s}-1)
\kappa_{\tau,s}.
}
\tag{9.1}
$$

Therefore:

$$
\alpha_{\tau,s}<1
$$

indicates that analytic weighted dissipation dominates;

$$
\alpha_{\tau,s}>1
$$

indicates that analytic weighted nonlinear transfer dominates.

This is the same as in Round 05 / Round 06,

but now:

$$
\boxed{
\alpha_{\tau,s}
}
$$

simultaneously sees the entire high-frequency tail.

---

# 10. Adaptive radius tax

If:

$$
m_{\tau,s}>0,
$$

define:

$$
\boxed{
\rho_{\tau,s}
=
\nu
(\alpha_{\tau,s}-1)_+
\frac{
\kappa_{\tau,s}
}{
m_{\tau,s}
}.
}
\tag{10.1}
$$

This quantity has the dimension of:

$$
\text{length}/\text{time}
$$

Now choose the adaptive analytic radius:

$$
\boxed{
\tau'
=
-\rho_{\tau,s}.
}
\tag{10.2}
$$

If:

$$
\alpha_{\tau,s}\le1,
$$

then:

$$
\rho_{\tau,s}=0
$$

and:

$$
G'\le0.
$$

If:

$$
\alpha_{\tau,s}>1,
$$

then from (8.3):

$$
\frac12
\frac d{dt}
\log G
=
\nu
(\alpha_{\tau,s}-1)\kappa_{\tau,s}
-
\rho_{\tau,s}
m_{\tau,s}
=
0.
$$

Thus, we uniformly obtain:

$$
\boxed{
G'(t)\le0.
}
\tag{10.3}
$$

Named:

$$
\boxed{
\textbf{Adaptive Analytic-Radius Compensation Law}.
}
$$

---

# 11. Radius tax decomposes into mean frequency + spectral spread

From:

$$
\kappa_{\tau,s}
=
m_{\tau,s}^2
+
V_{\tau,s},
$$

we have:

$$
\frac{
\kappa_{\tau,s}
}{
m_{\tau,s}
}
=
m_{\tau,s}
+
\frac{
V_{\tau,s}
}{
m_{\tau,s}
}.
$$

Therefore:

$$
\boxed{
\rho_{\tau,s}
=
\nu
(\alpha_{\tau,s}-1)_+
\left[
m_{\tau,s}
+
\frac{
V_{\tau,s}
}{
m_{\tau,s}
}
\right].
}
\tag{11.1}
$$

This decomposes the analytic-radius consumption into:

1. supercritical nonlinear excess:

$$
(\alpha_{\tau,s}-1)_+;
$$

2. mean active frequency:

$$
m_{\tau,s};
$$

3. spectral-spread surcharge:

$$
\frac{
V_{\tau,s}
}{
m_{\tau,s}
}.
$$

Thus, the higher the mean frequency, the broader the spectral distribution, and the more supercritical the nonlinearity,

the faster the analytic radius is consumed.

---

# 12. Round 06 spectral variance reappears as a radius cost

In Round 06, the exact scale-damping of viscosity was represented by the spectral variance.

In this round, the variance is no longer just:

a damping term for:

$$
\kappa_s'
$$

It appears directly in:

$$
\boxed{
\rho_{\tau,s}
}
$$

That is:

$$
\boxed{
\text{spectral spread}
}
$$

simultaneously plays two roles:

- diffusion utilizes the spread to suppress scale drift;
- if the nonlinear transfer is already supercritical, the radius sacrifice required to maintain the analytic norm also increases due to the spread.

This establishes a direct connection between Round 06 and Round 07.

---

# 13. Analytic-radius budget identity

From:

$$
\tau'
=
-\rho_{\tau,s},
$$

we obtain:

$$
\boxed{
\tau(t)
=
\tau_0
-
\int_{t_0}^t
\rho_{\tau(\sigma),s}(\sigma)
\,d\sigma.
}
\tag{13.1}
$$

And along this adaptive path:

$$
\boxed{
\mathcal G_{\tau(t),s}(t)
\le
\mathcal G_{\tau_0,s}(t_0).
}
\tag{13.2}
$$

Therefore, a positive initial analytic radius:

$$
\tau_0
$$

can be viewed as a finite continuous budget.

Nonlinear supercritical transfer consumes this budget through:

$$
\rho
$$

---

# 14. Continuation theorem along the adaptive radius

## Theorem 14.1

Assume a smooth solution exists on:

$$
[t_0,T)
$$

and:

$$
\mathcal G_{\tau_0,s}(t_0)<\infty
$$

for some:

$$
\tau_0>0.
$$

Let:

$$
\tau(t)
$$

satisfy the adaptive law (10.2).

If there exists:

$$
\tau_{\min}>0
$$

such that:

$$
\boxed{
\tau(t)\ge\tau_{\min}
\qquad
\forall t<T,
}
\tag{14.1}
$$

then all finite Sobolev levels are uniformly controlled on:

$$
[t_0,T)
$$

### Proof

From (13.2):

$$
\mathcal G_{\tau(t),s}(t)
\le
G_0.
$$

Since:

$$
\tau(t)\ge\tau_{\min},
$$

choose:

$$
\tau'
=
\frac12\tau_{\min}.
$$

Then:

$$
\tau(t)-\tau'
\ge
\frac12\tau_{\min}.
$$

By Theorem 3.1, for any:

$$
a\ge0,
$$

we have:

$$
\boxed{
\mathcal G_{\tau',s+a}(t)
\le
\left(
\frac{
2a
}{
e\tau_{\min}
}
\right)^{2a}
G_0.
}
\tag{14.2}
$$

Therefore, any fixed high Sobolev norm is uniformly bounded.

In the standard strong-solution continuation framework, taking a sufficiently high order allows the solution to be extended.

$$
\square
$$

---

# 15. Radius-Budget Necessity for a finite maximal time

Assume:

$$
T_\ast<\infty
$$

is the strong solution maximal time.

At any:

$$
t_0<T_\ast
$$

if there exists:

$$
\tau_0>0
$$

such that:

$$
\mathcal G_{\tau_0,s}(t_0)<\infty,
$$

then the adaptive path cannot maintain:

$$
\tau(t)\ge\tau_{\min}>0.
$$

throughout the entire:

$$
[t_0,T_\ast)
$$

Otherwise, by Theorem 14.1, it could be extended beyond:

$$
T_\ast.
$$

Therefore, a potential singular branch must exhaust the adaptive radius budget or lose continuation:

$$
\boxed{
\inf_{t<T_\ast}
\tau(t)
=
0.
}
\tag{15.1}
$$

Provided the adaptive ODE remains definable:

$$
\boxed{
\int_{t_0}^{T_\ast}
\rho_{\tau(t),s}(t)
\,dt
\ge
\tau_0.
}
\tag{15.2}
$$

This is the:

$$
\boxed{
\textbf{Analytic-Radius Budget Necessity}.
}
$$

---

# 16. Important limitation

(15.2) is not a contradiction.

Reason:

$$
\tau_0
$$

is a finite positive budget.

And:

$$
\rho
$$

may have a sufficiently large integral in finite time to consume it entirely.

Therefore, this round has not proved that:

$$
\boxed{
\int\rho<\tau_0.
}
$$

holds unconditionally.

Thus:

$$
\boxed{
\text{analytic resummation closes the hierarchy representation,
but not the radius budget}.
}
\tag{16.1}
$$

---

# 17. Why Gevrey resummation is stronger than finite derivative closure

Round 06 asked for:

$$
\alpha_s
\quad
\text{for all }s.
$$

Round 07 changes this to:

$$
\boxed{
\mathcal G_{\tau,s}.
}
$$

By Theorem 3.1,

a single positive:

$$
\tau
$$

controls all real higher levels:

$$
s+a.
$$

Therefore:

$$
\boxed{
\text{one analytic carrier}
}
$$

replaces:

$$
\boxed{
\text{infinitely many derivative carriers}.
}
$$

This is precisely the true function of the X-integral in this round:

$$
\boxed{
\int_{\rm Gevrey}
\left\{
M_s
\right\}_{s\ge0}
\rightsquigarrow
\mathcal G_{\tau,s}.
}
\tag{17.1}
$$

---

# 18. Analytic radius is conjugate to frequency

From:

$$
G
=
\int
e^{2\tau r}
r^{2s}e\,d\xi,
$$

differentiating with respect to:

$$
\tau
$$

$$
\boxed{
\partial_\tau\log G
=
2m_{\tau,s}.
}
\tag{18.1}
$$

Differentiating again:

$$
\boxed{
\partial_\tau m_{\tau,s}
=
2
V_{\tau,s}.
}
\tag{18.2}
$$

Therefore:

$$
\tau
$$

is not an arbitrary auxiliary parameter.

It is the exponential-tilt coordinate of the spectral frequency.

And the variance:

$$
V_{\tau,s}
$$

is precisely the response of:

$$
m
$$

to the analytic radius.

Thus:

$$
\boxed{
\text{analytic radius}
\leftrightarrow
\text{continuous frequency statistics}
}
$$

is an exact dual relation.

---

# 19. Exact spectral replicator identity

Define the local Fourier transfer rate:

$$
\vartheta(\xi,t)
=
\frac{
\operatorname{Re}
\left(
\widehat F(\xi,t):
\overline{\widehat S(\xi,t)}
\right)
}{
|\widehat S(\xi,t)|^2
}
$$

where:

$$
\widehat S\neq0
$$

Where:

$$
\widehat S=0
$$

set:

$$
\vartheta=0.
$$

For any suitable test function:

$$
\phi(r),
$$

the analytic weighted probability measure satisfies:

$$
\boxed{
\frac d{dt}
\mathbb E_{\mu_{\tau,s}}
[\phi(r)]
=
2
\operatorname{Cov}_{\mu_{\tau,s}}
\left(
\phi(r),
\vartheta
-
\nu r^2
+
\tau'r
\right).
}
\tag{19.1}
$$

Specifically taking:

$$
\phi(r)=r,
$$

we obtain:

$$
\boxed{
m'
=
2
\operatorname{Cov}(r,\vartheta)
-
2\nu
\operatorname{Cov}(r,r^2)
+
2\tau'
V.
}
\tag{19.2}
$$

Along the adaptive path:

$$
\tau'\le0,
$$

the last term:

$$
2\tau'V
\le0.
$$

Therefore, shrinking the analytic radius has the additional effect of reweighting the weighted spectral state toward lower frequencies.

This is gauge compensation, not physical energy dissipation.

---

# 20. Pure-C frontier compression

The Boss of Round 06:

$$
\boxed{
\text{Continuous Infinite Hierarchy}.
}
$$

Round 07 shows:

$$
\boxed{
\text{positive analytic radius}
\Longrightarrow
\text{all derivative levels jointly controlled}.
}
$$

Therefore, the hierarchy itself is no longer the primary frontier.

The new frontier:

$$
\boxed{
\textbf{Analytic-Radius Budget}.
}
$$

Form:

$$
\boxed{
\tau_0
\stackrel{\rho}{\longrightarrow}
\tau(t).
}
$$

A potential singularity can only escape along the adaptive closure path of:

$$
\boxed{
\tau(t)\downarrow0
}
$$

---

# 21. STOP-C11 — Analytic-Radius Budget Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C11}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{Gevrey\ resummation},
\\
\text{carrier}
=
\mathcal G_{\tau,s},
\\
\text{hierarchy}
=
\mathrm{resummed},
\\
\text{exact\ radius\ tax}
=
\rho_{\tau,s}
=
\nu
(\alpha_{\tau,s}-1)_+
\kappa_{\tau,s}/m_{\tau,s},
\\
\text{radius\ law}
=
\tau'
=
-\rho_{\tau,s},
\\
\text{norm\ law}
=
\mathcal G_{\tau(t),s}(t)
\le
\mathcal G_{\tau_0,s}(t_0),
\\
\text{missing}
=
\mathrm{unconditional\ proof\ that\ radius\ budget\ cannot\ be\ exhausted},
\\
\text{discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

Named:

$$
\boxed{
\textbf{STOP-C11:
Analytic-Radius Budget Exhaustion Gap}.
}
$$

---

# 22. 24/72 interpretation

This round remains:

$$
\boxed{
B=\mathsf C.
}
$$

Because:

$$
\xi\in\mathbb R^3
$$

and:

$$
\tau\in[0,\infty)
$$

are both continuous coordinates.

The update mode is hybrid:

$$
\boxed{
\mathsf S_{\rm time}
+
\mathsf P_{\rm spectral/global}.
}
$$

The observation mode:

$$
\boxed{
\mathsf X
\to
\mathsf C_{\rm targeted}
}
$$

reappears.

Originally, the infinite hierarchy was a multi-observable:

$$
\mathsf X.
$$

After the Gevrey X-integral:

$$
\mathcal G_{\tau,s}
$$

becomes a sufficient targeted carrier for the analytic continuation objective.

The transition law remains:

$$
\boxed{
L=\mathsf F.
}
$$

There is no need for:

$$
\mathsf K
$$

or:

$$
\mathsf Q.
$$

---

# 23. 24/72 Ledger — Round 07

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C64 | Gevrey carrier $\mathcal G_{\tau,s}$ | $\mathsf C$ | continuous spectral | $\mathsf X$→targeted | $\mathsf F$ | FORM |
| C65 | real-order hierarchy resummation | $\mathsf C$ | global | targeted | $\mathsf F$ | PROVED |
| C66 | time-varying radius balance | $\mathsf C$ | $\mathsf S/\mathsf P$ | targeted | $\mathsf F$ | EXACT |
| C67 | analytic probability $\mu_{\tau,s}$ | $\mathsf C$ | spectral | $\mathsf X$ | $\mathsf F$ | FORM |
| C68 | $\alpha_{\tau,s}$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C69 | adaptive radius tax $\rho_{\tau,s}$ | $\mathsf C$ | feedback | scalar | $\mathsf F$ | EXACT DEFINITION |
| C70 | $G'\le0$ under $\tau'=-\rho$ | $\mathsf C$ | adaptive | scalar | $\mathsf F$ | PROVED |
| C71 | positive radius $\to$ all Sobolev levels | $\mathsf C$ | resummed | targeted | $\mathsf F$ | PROVED |
| C72 | finite-time singularity $\to$ radius-budget exhaustion | $\mathsf C$ | adaptive | targeted | $\mathsf F$ | NECESSARY under continuation assumptions |
| C73 | unconditional non-exhaustion of radius | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C11 |

---

# 24. No essential discrete intrusion

Even when facing:

$$
\text{all derivative orders}
$$

Round 07 still does not require:

- dyadic decomposition;
- profile sequences;
- scale indices;
- Galerkin truncation;
- discrete shell cascades.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{24.1}
$$

Currently, the Pure-C route has become:

$$
\boxed{
\begin{aligned}
\mathsf C_{\rm energy}
&\to
\mathsf C_{\rm critical}
\\
&\to
\mathsf C_{\rm relational}
\\
&\to
\mathsf C_{\rm nonlocal}
\\
&\to
\mathsf C_{\rm projected}
\\
&\to
\mathsf C_{\rm gradient\ geometry}
\\
&\to
\mathsf C_{\rm infinite\ hierarchy}
\\
&\to
\mathsf C_{\rm Gevrey\ resummed}
\\
&\to
\mathsf C_{\rm radius\ budget}.
\end{aligned}
}
\tag{24.2}
$$

---

# 25. What the next proof must actually do

Now, further studying:

$$
\alpha_s
$$

order-by-order dynamics is no longer the optimal route.

The true closure-bearing problem becomes:

$$
\boxed{
\text{Can the adaptive radius tax }
\rho_{\tau,s}
\text{ be shown unable to exhaust every positive initial analytic radius?}
}
$$

That is, seeking an unconditional mechanism for:

$$
\boxed{
\int_{t_0}^{T_\ast}
\rho_{\tau(t),s}(t)
dt
<
\tau_0.
}
\tag{25.1}
$$

If proven, then:

$$
\tau(t)
$$

remains positive,

and by Theorem 14.1:

$$
\boxed{
\text{all high Sobolev norms remain bounded}
}
$$

thereby ruling out:

$$
T_\ast<\infty.
$$

---

# 26. Candidate next route — exploit radius tax structure

From:

$$
\rho
=
\nu
(\alpha-1)_+
\left(
m+\frac Vm
\right),
$$

the next round should not merely estimate:

$$
\alpha.
$$

It should simultaneously study:

$$
\boxed{
(\alpha-1)_+,
\quad
m,
\quad
V.
}
$$

Possible cancellation targets:

1. whether high nonlinear excess:

$$
(\alpha-1)_+
$$

forces the viscosity variance:

$$
V
$$

to increase synchronously;

2. if:

$$
V
$$

increases, whether it conversely rapidly reduces:

$$
\alpha
$$

or the nonlinear-frequency covariance;

3. whether there exists a continuous uncertainty relation:

$$
\boxed{
\text{supercritical transfer}
\Longrightarrow
\text{spectral broadening}
\Longrightarrow
\text{stronger viscous damping}
}
$$

forming a negative feedback;

4. if the spectrum tends to be narrow:

$$
V\to0,
$$

whether it is forced to approach a monochromatic / self-similar rigid state, which is then ruled out by known rigidity/Liouville cuts.

This will divide the next round into two continuous cases:

$$
\boxed{
V\text{ large}
\quad\vee\quad
V\text{ small}.
}
$$

But still without using discrete shells.

---

# 27. External primary-source anchors

1. Animikh Biswas, Joshua Hudson, Jing Tian, *Persistence time of solutions of the three-dimensional Navier-Stokes equations in Sobolev-Gevrey classes*, arXiv:1912.11192.
   - time-varying analytic Gevrey classes;
   - persistence times comparable to Sobolev existence times;
   - explicit discussion that Gevrey methods avoid recursive higher-derivative estimation and quantify analyticity radius.

2. Ciprian Foias and Roger Temam, *Gevrey class regularity for the solutions of the Navier-Stokes equations*, Journal of Functional Analysis 87 (1989), 359–369.
   - classical Gevrey regularity framework for Navier–Stokes.

3. Cong Wang, *Space-time analyticity and refined analyticity radius of the Navier-Stokes equations in the critical Besov spaces*, arXiv:2503.03658.
   - current analytic-radius / critical-space continuation of the Gevrey program.

4. Luan T. Hoang, Vincent R. Martinez, *Asymptotic expansion in Gevrey spaces for solutions of Navier-Stokes equations*, arXiv:1511.03523.
   - later Gevrey-space Navier–Stokes framework.

---

# 28. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Gevrey\ Resummation},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Infinite derivative hierarchy}
&:
\mathrm{resummed},
\\
\text{Generating carrier}
&:
\mathcal G_{\tau,s},
\\
\text{Adaptive radius tax}
&:
\rho_{\tau,s},
\\
\text{Exact compensation}
&:
\tau'=-\rho,
\\
\text{Gevrey norm}
&:
\mathrm{nonincreasing\ along\ adaptive\ path},
\\
\text{Positive radius}
&:
\mathrm{controls\ all\ higher\ Sobolev\ levels},
\\
\text{Potential singular escape}
&:
\mathrm{analytic\ radius\ budget\ exhaustion},
\\
\text{STOP-C11}
&:
\mathrm{Analytic\text{-}Radius\ Budget\ Exhaustion\ Gap},
\\
\text{Next}
&:
\mathrm{Radius\text{-}Tax\ Feedback\ via\ spectral\ variance}.
\end{aligned}
}
$$