# NS × X Integral × 24/72 Paradigm Practice
## Round 08 — Pure Continuous Transfer–Dispersion Feedback Route

- Date: 2026-08-16
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Spectral-Feedback Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`；display `$$...$$`
- Previous round: `NS_X72_Round07_PureContinuous_Gevrey_AnalyticRadiusBudget_v0.1_2026-08-16.md`
- This round's objective: Test the hypothesis proposed in Round 07 that "spectral variance automatically forms an analytic-radius negative feedback." Establish the exact moment evolution of the analytic-weighted spectral measure, distinguishing between mean-frequency damping, variance dynamics, and nonlinear transfer-frequency covariance.
- Non-claims: This document does not prove an unconditional upper bound for the Navier–Stokes nonlinear transfer covariance. The strongest result of this text is compressing this gap into an exact continuous covariance inequality.

---

# 0. Round 07 handoff

Round 07 defined the Gevrey carrier:

$$
\mathcal G_{\tau,s}
=
\left\|
e^{\tau\Lambda}
\Lambda^sS
\right\|_2^2
$$

and the analytic spectral probability measure:

$$
d\mu_{\tau,s}(\xi)
=
\frac{
e^{2\tau|\xi|}
|\xi|^{2s}
|\widehat S(\xi)|^2
}{
\mathcal G_{\tau,s}
}
d\xi.
$$

Let:

$$
r=|\xi|.
$$

Define:

$$
m
=
\mathbb E_\mu[r],
$$

$$
\kappa
=
\mathbb E_\mu[r^2],
$$

$$
V
=
\operatorname{Var}_\mu(r)
=
\kappa-m^2.
$$

the weighted nonlinear growth rate:

$$
g
=
\frac{
T_{\tau,s}
}{
\mathcal G_{\tau,s}
},
$$

and:

$$
\alpha
=
\frac{
g
}{
\nu\kappa
}.
$$

Round 07 exact norm law:

$$
\boxed{
\frac12
\frac d{dt}
\log\mathcal G_{\tau,s}
=
\nu(\alpha-1)\kappa
+
\tau'm.
}
\tag{0.1}
$$

and proposed the analytic-radius tax:

$$
\rho
=
\nu
(\alpha-1)_+
\frac{\kappa}{m}.
$$

Choosing:

$$
\tau'=-\rho
$$

ensures that:

$$
\mathcal G_{\tau(t),s}
$$

does not increase.

Round 07 STOP:

$$
\boxed{
\text{STOP-C11}
=
\text{Analytic-Radius Budget Exhaustion Gap}.
}
$$

This round asks:

> Does spectral variance automatically suppress high-frequency drift, thereby preventing the radius budget from being exhausted?

---

# 1. Exact weighted spectral replicator identity

projected strain equation:

$$
\partial_tS
+
\nu\Lambda^2S
=
F.
$$

In Fourier space, let:

$$
e(\xi,t)
=
|\widehat S(\xi,t)|^2,
$$

$$
h(\xi,t)
=
\operatorname{Re}
\left(
\widehat F(\xi,t):
\overline{\widehat S(\xi,t)}
\right).
$$

At:

$$
e>0
$$

define the local nonlinear transfer rate:

$$
\boxed{
\vartheta(\xi,t)
=
\frac{h(\xi,t)}{e(\xi,t)}.
}
\tag{1.1}
$$

At:

$$
e=0
$$

let:

$$
\vartheta=0.
$$

Since:

$$
\partial_te
=
-2\nu r^2e
+
2h,
$$

and the analytic weight:

$$
w_{\tau,s}
=
e^{2\tau r}r^{2s}
$$

satisfies:

$$
\partial_tw_{\tau,s}
=
2\tau' r w_{\tau,s},
$$

therefore:

$$
\partial_t(w_{\tau,s}e)
=
2
\left(
\vartheta
-
\nu r^2
+
\tau'r
\right)
w_{\tau,s}e.
$$

Define:

$$
\boxed{
\Psi
=
\vartheta
-
\nu r^2
+
\tau'r.
}
\tag{1.2}
$$

Then for any sufficiently integrable test observable depending only on $r$:

$$
\phi(r),
$$

we have the exact probability-measure evolution:

$$
\boxed{
\frac d{dt}
\mathbb E_\mu[\phi]
=
2
\operatorname{Cov}_\mu
\left(
\phi,
\Psi
\right).
}
\tag{1.3}
$$

This is the master equation for all moment equations in this round.

---

# 2. Exact mean-frequency equation

Taking:

$$
\phi(r)=r.
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
2\tau'V.
}
\tag{2.1}
$$

This equation exactly decomposes the mean-frequency drift into three channels:

1. nonlinear transfer-frequency covariance:

$$
\operatorname{Cov}(r,\vartheta);
$$

2. viscous frequency damping:

$$
-\nu\operatorname{Cov}(r,r^2);
$$

3. analytic-radius reweighting:

$$
\tau'V.
$$

If:

$$
\tau'\le0,
$$

the third term is always non-positive.

---

# 3. Universal viscous covariance lower bound

## Lemma 3.1

For any probability measure on:

$$
r\ge0,
$$

we have:

$$
\boxed{
\operatorname{Cov}(r,r^2)
=
\mathbb E
\left[
(r-m)^2(r+m)
\right].
}
\tag{3.1}
$$

### Proof

Expanding the right side:

$$
(r-m)^2(r+m)
=
r^3
-
mr^2
-
m^2r
+
m^3.
$$

Taking the expectation:

$$
\mathbb E[r^3]
-
m\mathbb E[r^2]
-
m^3
+
m^3
$$

which is:

$$
\operatorname{Cov}(r,r^2).
$$

The proof is complete.

Since:

$$
r+m\ge m,
$$

we obtain:

$$
\boxed{
\operatorname{Cov}(r,r^2)
\ge
mV.
}
\tag{3.2}
$$

Therefore, the damping of the mean frequency by pure diffusion is at least:

$$
\boxed{
2\nu mV.
}
\tag{3.3}
$$

---

# 4. Strict positivity in the nontrivial $L^2$ spectral class

In the current smooth finite-energy whole-space class,

$$
\widehat S
$$

is an ordinary $L^2$ function.

If:

$$
V=0,
$$

then:

$$
r=m
$$

holds for $\mu$-almost every frequency.

Thus, the spectral mass must be entirely supported on the sphere:

$$
|\xi|=m.
$$

However, this sphere has Lebesgue measure zero in:

$$
\mathbb R^3
$$

Since:

$$
\mu
$$

is absolutely continuous with respect to the Lebesgue measure,

a non-zero $L^2$ state cannot have its entire mass supported on a single sphere.

Therefore, for a nontrivial state:

$$
\boxed{
V>0.
}
\tag{4.1}
$$

Similarly:

$$
m>0.
$$

Thus:

$$
\boxed{
\operatorname{Cov}(r,r^2)>0
}
\tag{4.2}
$$

holds for a nontrivial analytic-weighted strain state.

This indicates that pure viscosity strictly pushes the mean frequency downward.

---

# 5. Mean-Frequency Feedback Theorem

If:

$$
\tau'\le0,
$$

from (2.1) and (3.2):

$$
m'
\le
2
\operatorname{Cov}(r,\vartheta)
-
2\nu mV.
$$

Therefore:

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
\le
\nu mV
\quad
\Longrightarrow
\quad
m'\le0.
}
\tag{5.1}
$$

Conversely:

$$
\boxed{
m'>0
\quad
\Longrightarrow
\quad
\operatorname{Cov}(r,\vartheta)
>
\nu
\operatorname{Cov}(r,r^2)
\ge
\nu mV
}
\tag{5.2}
$$

if:

$$
\tau'\le0.
$$

Named:

$$
\boxed{
\textbf{Mean-Frequency Feedback Theorem}.
}
$$

Intuition:

> To push the analytic-weighted spectral mean to higher frequencies, the nonlinearity cannot merely "become stronger on average"; it must preferentially assign a larger normalized growth rate to higher frequencies, and this covariance must overcome the universal monotone covariance of viscosity.

---

# 6. Transfer–Dispersion Ratio

Define:

$$
\boxed{
\zeta_{\tau,s}
=
\frac{
\operatorname{Cov}(r,\vartheta)
}{
\nu
\operatorname{Cov}(r,r^2)
}.
}
\tag{6.1}
$$

For a nontrivial state, the denominator is strictly positive.

Then the mean-frequency law can be written as:

$$
\boxed{
m'
=
2\nu
\operatorname{Cov}(r,r^2)
(\zeta_{\tau,s}-1)
+
2\tau'V.
}
\tag{6.2}
$$

So:

$$
\boxed{
\zeta_{\tau,s}\le1
\quad\text{and}\quad
\tau'\le0
\Longrightarrow
m'\le0.
}
\tag{6.3}
$$

Therefore:

$$
\boxed{
\zeta=1
}
$$

is the exact continuous threshold for the mean-frequency cascade.

---

# 7. $\alpha$ and $\zeta$ measure different information

Recall:

$$
\alpha
=
\frac{
\mathbb E[\vartheta]
}{
\nu\mathbb E[r^2]
}.
$$

So:

$$
\alpha
$$

only looks at the average nonlinear growth.

Whereas:

$$
\zeta
$$

looks at:

$$
\operatorname{Cov}(r,\vartheta),
$$

that is, whether the nonlinear growth preferentially favors higher frequencies.

Therefore:

$$
\boxed{
\alpha
\neq
\zeta
}
$$

are fundamentally different in their information content.

---

# 8. Observation-level no-go: $\alpha$ alone cannot determine spectral drift

Fix any nondegenerate spectral probability measure:

$$
\mu
$$

with:

$$
V>0.
$$

Fix the desired mean transfer:

$$
c.
$$

Consider two abstract transfer profiles:

$$
\vartheta_+(r)
=
c
+
a(r-m),
$$

$$
\vartheta_-(r)
=
c
-
a(r-m),
$$

where:

$$
a>0.
$$

Both have the same mean:

$$
\boxed{
\mathbb E[\vartheta_+]
=
\mathbb E[\vartheta_-]
=
c.
}
\tag{8.1}
$$

Thus, for the same:

$$
\kappa
$$

they have the same:

$$
\boxed{
\alpha_+
=
\alpha_-.
}
\tag{8.2}
$$

But:

$$
\operatorname{Cov}(r,\vartheta_+)
=
aV,
$$

$$
\operatorname{Cov}(r,\vartheta_-)
=
-aV.
$$

So the mean-frequency nonlinear contributions have opposite directions.

Therefore, in the observation class that "only knows $\alpha$ and does not preserve the transfer-frequency relation":

$$
\boxed{
\alpha
\text{ is insufficient to determine spectral drift}.
}
\tag{8.3}
$$

Important limitation:

This is an **observation architecture no-go**.

This document does not claim that:

$$
\vartheta_\pm
$$

can necessarily be realized by actual Navier–Stokes convolution dynamics.

The true NS proof obligation is precisely to use its convolution / incompressibility structure to constrain the realizable:

$$
\vartheta.
$$

---

# 9. A restricted $\mathsf X$ result appears again

Let the observation context:

$$
\Gamma_{\alpha}
$$

require simultaneously preserving:

$$
\mathbb E[\vartheta]
$$

and:

$$
\operatorname{sign}
\operatorname{Cov}(r,\vartheta).
$$

If the scalar observation class is allowed to only have:

$$
q=q(\alpha),
$$

then Section 8 shows:

The same:

$$
\alpha
$$

can correspond to opposite covariance signs.

Thus:

$$
\boxed{
\mathsf X_{\Gamma_\alpha}
}
\tag{9.1}
$$

holds in this restricted observation class.

The repair is to take:

$$
\boxed{
(\alpha,\zeta)
}
$$

at least as a two-dimensional targeted state.

---

# 10. Radial conditional transfer profile

Since:

$$
r=|\xi|
$$

depends only on the radial frequency,

define the conditional radial mean of the transfer:

$$
\boxed{
\bar\vartheta(r)
=
\mathbb E[
\vartheta
\mid
|\xi|=r
].
}
\tag{10.1}
$$

Formally:

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
=
\operatorname{Cov}
(r,\bar\vartheta(r)).
}
\tag{10.2}
$$

So the effect of angular complexity on the mean-frequency drift can first be compressed into a radial conditional transfer profile.

This does not mean that angular geometry is unimportant.

It only means that for the observable:

$$
m'
$$

angular information enters solely through:

$$
\bar\vartheta(r)
$$

---

# 11. Radial-slope sufficient condition

Assume:

$$
\bar\vartheta(r)
$$

is Lipschitz on the relevant spectral support:

$$
|
\bar\vartheta(r_1)
-
\bar\vartheta(r_2)
|
\le
L
|r_1-r_2|.
$$

For independent copies:

$$
R,R'\sim\mu,
$$

we have the covariance identity:

$$
\operatorname{Cov}
(R,\bar\vartheta(R))
=
\frac12
\mathbb E
\left[
(R-R')
(
\bar\vartheta(R)
-
\bar\vartheta(R')
)
\right].
$$

Thus:

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
\le
LV.
}
\tag{11.1}
$$

If:

$$
\boxed{
L\le\nu m,
}
\tag{11.2}
$$

then:

$$
\operatorname{Cov}(r,\vartheta)
\le
\nu mV
\le
\nu
\operatorname{Cov}(r,r^2).
$$

Therefore:

$$
\boxed{
L\le\nu m,
\quad
\tau'\le0
\Longrightarrow
m'\le0.
}
\tag{11.3}
$$

So a sufficient continuous anti-cascade condition is:

$$
\boxed{
\operatorname{Lip}_r
\bar\vartheta
\le
\nu m.
}
\tag{11.4}
$$

This round does not prove that the actual NS transfer profile unconditionally satisfies this bound.

---

# 12. Variance evolution

From the master equation (1.3):

$$
V
=
\mathbb E[(r-m)^2].
$$

we directly obtain:

$$
\boxed{
V'
=
2
\operatorname{Cov}
\left(
(r-m)^2,
\vartheta
\right)
-
2\nu
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
+
2\tau'
\operatorname{Cov}
\left(
(r-m)^2,
r
\right).
}
\tag{12.1}
$$

These three covariances generally do not have a fixed sign.

Therefore:

$$
\boxed{
V
}
$$

itself is not a monotone Lyapunov quantity guaranteed by the formal structure.

---

# 13. Counterexample: pure diffusion need not monotonically decrease variance

Consider an abstract radial probability measure supported on:

$$
r\in\{0,1\}
$$

with:

$$
\mathbb P(r=1)=p,
$$

$$
\mathbb P(r=0)=1-p.
$$

Then:

$$
m=p,
$$

$$
V=p(1-p).
$$

And we can directly calculate:

$$
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
=
p(1-p)(1-2p).
$$

If:

$$
p>\frac12,
$$

then:

$$
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
<0.
$$

Under pure diffusion:

$$
\vartheta=0,
\qquad
\tau'=0
$$

we have:

$$
V'
=
-2\nu
\operatorname{Cov}
\left(
(r-m)^2,
r^2
\right)
>0.
$$

So:

$$
\boxed{
\textbf{
spectral variance itself can initially increase even under pure diffusion.
}
}
\tag{13.1}
$$

This two-point measure is not a smooth $L^2$ Fourier density.

But it can be approximated by two very narrow smooth radial annuli, making this initial sign persistence hold.

Therefore, this round corrects the intuitive conjecture from Round 07:

> viscosity does not form feedback by "making the variance inevitably decrease."

What is truly guaranteed is:

$$
\boxed{
\text{viscosity makes the spectral mean drift downward},
}
$$

since:

$$
\operatorname{Cov}(r,r^2)>0.
$$

---

# 14. Two distinct continuous danger coordinates

Define the analytic weighted log-amplitude:

$$
\boxed{
L_G
=
\frac12
\log
\mathcal G_{\tau,s}.
}
$$

From Round 07:

$$
\boxed{
L_G'
=
D_{\rm amp}
+
\tau'm,
}
\tag{14.1}
$$

where:

$$
\boxed{
D_{\rm amp}
=
\mathbb E[\vartheta]
-
\nu
\mathbb E[r^2]
=
\nu
(\alpha-1)\kappa.
}
\tag{14.2}
$$

On the other hand:

$$
\boxed{
\frac12m'
=
D_{\rm shift}
+
\tau'V,
}
\tag{14.3}
$$

where:

$$
\boxed{
D_{\rm shift}
=
\operatorname{Cov}(r,\vartheta)
-
\nu
\operatorname{Cov}(r,r^2).
}
\tag{14.4}
$$

So the analytic danger actually has at least two distinct coordinates:

$$
\boxed{
D_{\rm amp}
}
$$

and:

$$
\boxed{
D_{\rm shift}.
}
$$

The first asks:

> Does the analytic weighted mass increase?

The second asks:

> Does the analytic weighted mean frequency shift to higher frequencies?

They cannot be losslessly replaced by a single:

$$
\alpha
$$

---

# 15. Radius control acts on both channels

The effect of the radius change:

$$
\tau'
$$

on the two observables is:

$$
\boxed{
\begin{pmatrix}
L_G'
\\[0.3em]
\frac12m'
\end{pmatrix}
=
\begin{pmatrix}
D_{\rm amp}
\\[0.3em]
D_{\rm shift}
\end{pmatrix}
+
\tau'
\begin{pmatrix}
m
\\[0.3em]
V
\end{pmatrix}.
}
\tag{15.1}
$$

If:

$$
\tau'<0,
$$

then shrinking the analytic radius simultaneously:

1. decreases the analytic weighted norm growth;
2. decreases the weighted mean-frequency drift.

This provides a two-dimensional continuous feedback picture.

---

# 16. Joint compensation tax

Since a nontrivial state has:

$$
m>0,
\qquad
V>0,
$$

define:

$$
\boxed{
\rho_{\rm joint}
=
\max
\left\{
\frac{
(D_{\rm amp})_+
}{
m
},
\;
\frac{
(D_{\rm shift})_+
}{
V
}
\right\}.
}
\tag{16.1}
$$

Choose:

$$
\boxed{
\tau'
=
-\rho_{\rm joint}.
}
\tag{16.2}
$$

Then from (15.1):

$$
\boxed{
L_G'\le0,
}
\tag{16.3}
$$

and:

$$
\boxed{
m'\le0.
}
\tag{16.4}
$$

Named:

$$
\boxed{
\textbf{Joint Analytic-Amplitude / Mean-Frequency Compensation Law}.
}
$$

Note:

This joint tax is more conservative than the minimal amplitude tax from Round 07 that only controls:

$$
L_G
$$

Its purpose is to simultaneously fix both observables, rather than claiming it is the optimal continuation control.

---

# 17. Joint radius budget

Along:

$$
\tau'=-\rho_{\rm joint},
$$

we have:

$$
\boxed{
\tau(t)
=
\tau_0
-
\int_{t_0}^t
\rho_{\rm joint}(\sigma)
d\sigma.
}
\tag{17.1}
$$

and:

$$
\boxed{
\mathcal G_{\tau(t),s}(t)
\le
\mathcal G_{\tau_0,s}(t_0),
}
\tag{17.2}
$$

$$
\boxed{
m(t)\le m(t_0).
}
\tag{17.3}
$$

If:

$$
\inf_{t<T_\ast}\tau(t)>0,
$$

then the Round 07 resummation theorem still gives uniform control for all finite Sobolev levels.

Therefore, on this joint-control path, a potential finite-time singularity necessarily requires:

$$
\boxed{
\int_{t_0}^{T_\ast}
\rho_{\rm joint}(t)dt
\ge
\tau_0.
}
\tag{17.4}
$$

This is not a contradiction.

But it splits the danger budget into:

$$
\boxed{
\text{amplitude excess}
\vee
\text{frequency-shift excess}.
}
$$

---

# 18. What variance feedback actually proves

The original hope for this round was:

$$
\boxed{
V\text{ large}
\Longrightarrow
\text{automatic nonlinear suppression}.
}
$$

This proposition has not been proved.

What is actually obtained is:

$$
\boxed{
V>0
}
$$

provides a viscous restoring scale:

$$
\nu mV.
$$

But the nonlinear term also has:

$$
\operatorname{Cov}(r,\vartheta).
$$

Therefore, the true comparison for negative feedback is:

$$
\boxed{
\operatorname{Cov}(r,\vartheta)
\stackrel{?}{\le}
\nu
\operatorname{Cov}(r,r^2).
}
\tag{18.1}
$$

which is:

$$
\boxed{
\zeta_{\tau,s}
\stackrel{?}{\le}
1.
}
\tag{18.2}
$$

So variance is not the answer.

Variance is the denominator / restoring resource.

The real Boss is how the nonlinear transfer depends on frequency.

---

# 19. STOP-C12 — Nonlinear Transfer–Dispersion Covariance Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C12}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{analytic\ spectral\ feedback},
\\
\text{exact\ mean\ law}
=
m'
=
2\operatorname{Cov}(r,\vartheta)
-
2\nu\operatorname{Cov}(r,r^2)
+
2\tau'V,
\\
\text{viscous\ lower\ bound}
=
\operatorname{Cov}(r,r^2)
\ge
mV,
\\
\text{exact\ threshold}
=
\zeta_{\tau,s}=1,
\\
\text{missing}
=
\mathrm{unconditional\ NS\ bound\ on\ }
\operatorname{Cov}(r,\vartheta),
\\
\text{variance\ monotonicity}
=
\mathrm{false\ in\ general},
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
\textbf{STOP-C12:
Nonlinear Transfer–Dispersion Covariance Gap}.
}
$$

---

# 20. The Pure-C frontier is now extremely specific

Round 01:

$$
\mathrm{energy\ scale\ mismatch}.
$$

Round 02:

$$
\mathrm{critical\ amplitude\ gap}.
$$

Round 03:

$$
\mathrm{geometry\ feedback\ gap}.
$$

Round 04:

$$
\mathrm{nonlocal\ pressure\ gap}.
$$

Round 05:

$$
\mathrm{compressive\ gradient\ alignment}.
$$

Round 06:

$$
\mathrm{continuous\ hierarchy\ slope}.
$$

Round 07:

$$
\mathrm{analytic\ radius\ budget}.
$$

Round 08:

$$
\boxed{
\mathrm{transfer\text{-}frequency\ covariance}.
}
$$

So currently, Pure-C is no longer a vague:

> Can we prove NS using continuous methods?

but rather:

$$
\boxed{
\textbf{
Can actual Navier–Stokes convolution geometry enforce
a transfer-frequency covariance bound strong enough
to keep }\zeta_{\tau,s}\le1
\textbf{ or make its positive excess integrable?}
}
\tag{20.1}
$$

---

# 21. No essential discrete intrusion

This round uses:

$$
r\in[0,\infty),
$$

$$
\xi\in\mathbb R^3,
$$

the continuous probability measure:

$$
\mu_{\tau,s},
$$

and continuous covariance.

There are no:

- dyadic shells;
- discrete triad graphs;
- countable scale sequences;
- Galerkin modes;
- profile extractions.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{21.1}
$$

The Pure-C route is currently:

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
\mathsf C_{\rm hierarchy}
\\
&\to
\mathsf C_{\rm Gevrey}
\\
&\to
\mathsf C_{\rm transfer\ covariance}.
\end{aligned}
}
$$

---

# 22. 24/72 Ledger — Round 08

| Step | X object / operation | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C74 | spectral replicator identity | $\mathsf C$ | $\mathsf P$ spectral | $\mathsf X$ | $\mathsf F$ | EXACT |
| C75 | mean frequency $m$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C76 | viscous covariance lower bound | $\mathsf C$ | — | targeted | $\mathsf F$ | PROVED |
| C77 | transfer–dispersion ratio $\zeta$ | $\mathsf C$ | relational | targeted scalar | $\mathsf F$ | FORM |
| C78 | $\zeta\le1\Rightarrow m'\le0$ | $\mathsf C$ | feedback | scalar | $\mathsf F$ | PROVED |
| C79 | $\alpha$ determines cascade sign | $\mathsf C$ | — | scalar | $\mathsf F$ | REFUTED as observation architecture |
| C80 | radial transfer slope condition | $\mathsf C$ | radial conditional | targeted | $\mathsf F$ | CONDITIONAL |
| C81 | variance monotone under viscosity | $\mathsf C$ | — | scalar | $\mathsf F$ | REFUTED in general spectral-measure class |
| C82 | two-danger state $(D_{\rm amp},D_{\rm shift})$ | $\mathsf C$ | relational | $\mathsf X$→2D targeted | $\mathsf F$ | FORM |
| C83 | joint compensation law | $\mathsf C$ | adaptive | targeted | $\mathsf F$ | PROVED |
| C84 | unconditional NS covariance bound | $\mathsf C$ | convolution | targeted | $\mathsf F$ | OPEN / STOP-C12 |

---

# 23. Next round — continuous Fourier triad geometry

The next round will no longer study the abstract:

$$
\vartheta.
$$

It will directly substitute back into the actual Navier–Stokes Fourier nonlinearity.

The Fourier velocity equation:

$$
\partial_t\widehat u(\xi)
+
\nu|\xi|^2\widehat u(\xi)
=
-
i
\mathbb P_\xi
\int_{\mathbb R^3}
(\xi\cdot\widehat u(\eta))
\widehat u(\xi-\eta)
\,d\eta
$$

can be rearranged using an equivalent divergence-form convention.

Next round's objective:

$$
\boxed{
\textbf{Continuous Triad Geometry}.
}
$$

Do not use discrete triad graphs.

Directly on:

$$
(\xi,\eta,\xi-\eta)
\in
\mathbb R^3\times\mathbb R^3\times\mathbb R^3
$$

ask:

1. Does the incompressibility projection:

$$
\mathbb P_\xi
$$

provide cancellation for the high-frequency transfer covariance?

2. Does the triad geometry:

$$
\xi=\eta+(\xi-\eta)
$$

force transfer to high $|\xi|$ to pay an angular / amplitude cost?

3. Does convolution symmetry allow:

$$
\operatorname{Cov}(r,\vartheta)
$$

to be rewritten as a signed triad integral?

4. Does there exist a continuous antisymmetry such that forward transfer is necessarily accompanied by some lower-frequency loss?

5. Can we push:

$$
\zeta>1
$$

into another rigid triad geometry?

6. If all useful estimates must ultimately partition the frequency space into shells to record the true:

$$
T_{\mathsf C\to\mathsf D}.
$$

---

# 24. External primary-source anchors

1. Dong Li, Ping Zhang, *On the refined analyticity radius of 3-D generalized Navier-Stokes equations*, arXiv:2406.10865.
   - Gevrey exponential Fourier weights;
   - critical/subcritical analyticity-radius lower bounds;
   - high-frequency-tail-sensitive analyticity analysis.

2. Ira Herbst, Erik Skibsted, *Analyticity estimates for the Navier-Stokes equations*, arXiv:0907.4351.
   - classical spatial analyticity-radius estimates for Navier–Stokes.

3. Cong Wang, *Space-time analyticity and refined analyticity radius of the Navier-Stokes equations in the critical Besov spaces*, arXiv:2503.03658.
   - modern critical-space Gevrey/analyticity-radius framework.

These sources anchor the use of analytic/Gevrey Fourier weights. The covariance identities and transfer–dispersion ratio in this checkpoint are direct derivations within the present route and are not attributed to those papers.

---

# 25. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&:
\mathrm{Pure\ Continuous\ Transfer\text{-}Dispersion\ Feedback},
\\
\text{Essential }\mathsf C\to\mathsf D
&:
\mathrm{Not\ reached},
\\
\text{Variance}
&:
\mathrm{not\ monotone\ in\ general},
\\
\text{Guaranteed\ viscous\ feedback}
&:
\operatorname{Cov}(r,r^2)\ge mV,
\\
\text{Exact\ cascade\ ratio}
&:
\zeta_{\tau,s},
\\
\text{Mean-frequency threshold}
&:
\zeta=1,
\\
\text{Single }\alpha\text{ observation}
&:
\mathrm{insufficient\ for\ spectral\ drift},
\\
\text{Joint danger coordinates}
&:
(D_{\rm amp},D_{\rm shift}),
\\
\text{STOP-C12}
&:
\mathrm{Nonlinear\ Transfer\text{-}Dispersion\ Covariance\ Gap},
\\
\text{Next}
&:
\mathrm{Continuous\ Fourier\ Triad\ Geometry}.
\end{aligned}
}
$$