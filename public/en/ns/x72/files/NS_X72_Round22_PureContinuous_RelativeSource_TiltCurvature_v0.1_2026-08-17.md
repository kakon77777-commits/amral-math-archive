# NS × X Integral × 24/72 Paradigm in Practice
## Round 22 — Pure Continuous Relative-Source Decomposition / Continuous Tilt-Curvature Route

- Date: 2026-08-17
- Version: v0.1
- Status: Proof-Route Experiment / Continuous-Only Relative-Source Branch
- canonical source：UTF-8 Markdown
- canonical math delimiters：inline `$...$`; display `$$...$$`
- Previous round: `NS_X72_Round21_PureContinuous_CriticalMass_Replicator_IntermittencyDynamics_v0.1_2026-08-17.md`
- This round's objective: Completely separate the abstract relative source
  $$
  \mathcal R_S
  $$
  and intermittency production
  $$
  \mathcal P_{\rm sel}
  $$
  from Round 21. Identify how strain self-amplification, vorticity coupling, pressure Hessian, relative diffusion, quotient growth, and gauge maintenance individually enter the normalized-deformation intermittency; and re-integrate the discrete-looking $p=0,2,4$ moments into a continuous moment-order tilt
  $$
  p\in[0,\infty).
  $$
- Non-claims: This document does not claim to prove that the selection curvature is unconditionally suppressed by the relative Fisher dissipation. The main results of this document are the exact tilt-curvature law, relative-source decomposition, and weighted-pressure commutator reduction.

---

# 0. Round 21 handoff

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

and:

$$
K
=
K_S
=
\frac{|S|}{r}
$$

for:

$$
r>0,\quad |S|>0.
$$

critical mass:

$$
\boxed{
d\mu_0
=
d\mu_Q
=
\frac{r^3}{Q^3}dx.
}
\tag{0.1}
$$

strain-energy measure:

$$
\boxed{
d\mu_2
=
d\nu_S
=
\frac{r|S|^2}{W_S}dx.
}
\tag{0.2}
$$

Round 21 intermittency:

$$
\boxed{
\mathfrak J_S
=
\frac{
\mathbb E_{\mu_0}[K^4]
}{
\mathbb E_{\mu_0}[K^2]^2
}
=
1+\chi^2(\mu_2\|\mu_0).
}
\tag{0.3}
$$

and we obtained:

$$
\boxed{
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}.
}
\tag{0.4}
$$

Round 21 STOP:

$$
\boxed{
\text{STOP-C25}
=
\text{Relative-Source / Critical-Mass Separation Gap}.
}
$$

---

# 1. Strain amplitude equation

Navier–Stokes strain equation:

$$
\boxed{
D_tS
=
\nu\Delta S
-
S^2
-
\frac14\omega\otimes\omega
+
\frac14|\omega|^2I
-
H_p,
}
\tag{1.1}
$$

where:

$$
D_t
=
\partial_t+u\cdot\nabla,
$$

$$
H_p
=
\nabla^2p.
$$

Let:

$$
e
=
|S|^2.
$$

Since:

$$
\operatorname{tr}S=0,
$$

we have:

$$
S:I=0.
$$

Therefore:

$$
\boxed{
D_te
=
\nu\Delta e
-
2\nu|\nabla S|^2
+
F_S,
}
\tag{1.2}
$$

where:

$$
\boxed{
F_S
=
-6\det S
-
\frac12\omega^\top S\omega
-
2S:H_p.
}
\tag{1.3}
$$

Here we use the three-dimensional trace-free identity:

$$
\operatorname{tr}(S^3)=3\det S.
$$

---

# 2. Quotient amplitude equation

From Round 21, we have:

$$
\boxed{
D_tr
=
\nu\Delta r
-
\nu r|\nabla n|^2
+
\gamma_Qr
+
n\cdot\nabla\chi_g,
}
\tag{2.1}
$$

where:

$$
n=\frac vr,
$$

$$
\boxed{
\gamma_Q
=
-
n^\top S n,
}
\tag{2.2}
$$

and:

$$
\chi_g
$$

is the gauge-maintenance potential for maintaining the nonlinear optimal gauge:

$$
\operatorname{div}(rv)=0.
$$

---

# 3. Weighted strain density

Define:

$$
\boxed{
\zeta_S
=
r|S|^2
=
re.
}
\tag{3.1}
$$

Then:

$$
W_S
=
\int
\zeta_Sdx.
$$

Round 21 common critical-mass drift:

$$
\boxed{
b_Q
=
u
-
3\frac{\chi_g}{r}n.
}
\tag{3.2}
$$

and:

$$
\boxed{
G_Q
=
\gamma_Q-\nu K_D,
}
\tag{3.3}
$$

where:

$$
\boxed{
K_D
=
\frac{
|\nabla v|^2+|\nabla r|^2
}{
r^2
}
=
2|\nabla\log r|^2
+
|\nabla n|^2.
}
\tag{3.4}
$$

---

# 4. Exact relative-source definition

For:

$$
\zeta_S>0
$$

define:

$$
\boxed{
\mathcal R_S
=
\frac{
\partial_t\zeta_S
+
\operatorname{div}(b_Q\zeta_S)
-
\nu\Delta\zeta_S
}{
\zeta_S
}
-
3G_Q.
}
\tag{4.1}
$$

Therefore:

$$
\boxed{
\partial_t\zeta_S
+
\operatorname{div}(b_Q\zeta_S)
=
\nu\Delta\zeta_S
+
\left(
3G_Q+\mathcal R_S
\right)\zeta_S.
}
\tag{4.2}
$$

---

# 5. Exact decomposition of $\mathcal R_S$

Substituting directly from Sections 1–3, we obtain:

$$
\boxed{
\mathcal R_S
=
\mathcal R_{\rm self}
+
\mathcal R_{\rm vort}
+
\mathcal R_{\rm press}
+
\mathcal R_{\rm quot}
+
\mathcal R_{\rm diff}
+
\mathcal R_{\rm gauge},
}
\tag{5.1}
$$

where:

$$
\boxed{
\mathcal R_{\rm self}
=
-6
\frac{
\det S
}{
|S|^2
},
}
\tag{5.2}
$$

$$
\boxed{
\mathcal R_{\rm vort}
=
-\frac12
\frac{
\omega^\top S\omega
}{
|S|^2
},
}
\tag{5.3}
$$

$$
\boxed{
\mathcal R_{\rm press}
=
-2
\frac{
S:H_p
}{
|S|^2
},
}
\tag{5.4}
$$

$$
\boxed{
\mathcal R_{\rm quot}
=
-2\gamma_Q,
}
\tag{5.5}
$$

and:

$$
\boxed{
\begin{aligned}
\mathcal R_{\rm diff}
={}&
3\nu K_D
-
\nu|\nabla n|^2
-
2\nu
\frac{
|\nabla S|^2
}{
|S|^2
}
\\
&-
2\nu
\nabla\log r
\cdot
\nabla\log|S|^2,
\end{aligned}
}
\tag{5.6}
$$

and:

$$
\boxed{
\mathcal R_{\rm gauge}
=
-\frac2r
n\cdot\nabla\chi_g
-
\frac{3\chi_g}{r}
\left[
n\cdot\nabla\log|S|^2
+
\operatorname{div}n
\right].
}
\tag{5.7}
$$

All division formulas are used only where:

$$
r>0,\quad |S|>0
$$

; zero sets should revert to the density equation (4.2).

---

# 6. Gauge source simplifies through the nonlinear critical gauge

The Round 20 nonlinear gauge:

$$
\operatorname{div}(r^2n)=0
$$

gives:

$$
\boxed{
\operatorname{div}n
=
-2
n\cdot\nabla\log r.
}
\tag{6.1}
$$

Also:

$$
K
=
\frac{|S|}{r}.
$$

Thus:

$$
n\cdot\nabla\log|S|^2
+
\operatorname{div}n
=
2n\cdot\nabla\log K.
$$

Therefore:

$$
\boxed{
\mathcal R_{\rm gauge}
=
-\frac2r
n\cdot\nabla\chi_g
-
\frac{
6\chi_g
}{
r
}
n\cdot\nabla\log K.
}
\tag{6.2}
$$

Thus, the impact of the dynamic gauge on relative intermittency is mediated only via:

- the gauge-potential slope;
- the normalized strain-rate slope;

entering the dynamics.

---

# 7. Relative diffusion in normalized variables

For:

$$
|S|>0
$$

let the normalized strain orientation be:

$$
\widehat S
=
\frac S{|S|}.
$$

Then:

$$
\boxed{
\frac{
|\nabla S|^2
}{
|S|^2
}
=
|\nabla\log|S||^2
+
|\nabla\widehat S|^2.
}
\tag{7.1}
$$

Using:

$$
\nabla\log|S|
=
\nabla\log r
+
\nabla\log K,
$$

we can rewrite (5.6) as:

$$
\boxed{
\mathcal R_{\rm diff}
=
2\nu
\left[
|\nabla n|^2
-
|\nabla\widehat S|^2
-
|\nabla\log K|^2
-
4
\nabla\log r
\cdot
\nabla\log K
\right].
}
\tag{7.2}
$$

Therefore, the relative diffusion itself is not a purely negative term.

The common viscous anti-intermittency and the local strain-orientation / quotient-amplitude geometry couple with each other.

---

# 8. Continuous moment-order tilt

For any real:

$$
p\ge0
$$

such that the moment is finite, define:

$$
\boxed{
Z_p
=
\mathbb E_{\mu_0}[K^p].
}
\tag{8.1}
$$

and:

$$
\boxed{
d\mu_p
=
\frac{
K^p
}{
Z_p
}
d\mu_0.
}
\tag{8.2}
$$

Special values:

$$
\boxed{
\mu_0=\mu_Q,
}
$$

$$
\boxed{
\mu_2=\nu_S,
}
$$

and:

$$
\boxed{
d\mu_4
=
\frac{
K^4
}{
\mathbb E_{\mu_0}[K^4]
}
d\mu_0.
}
\tag{8.3}
$$

Thus, the Round 21 moment orders:

$$
0,\ 2,\ 4
$$

are not intrinsically discrete.

They belong to the continuous tilt family:

$$
\boxed{
p\in[0,\infty)
}
$$

as three slices.

---

# 9. Relative Fisher term becomes a $\mu_4$ expectation

Round 21:

$$
f_S
=
\frac{
d\mu_2
}{
d\mu_0
}
=
\frac{
K^2
}{
Z_2
}.
$$

Thus:

$$
\boxed{
\nabla f_S
=
2f_S
\nabla\log K.
}
\tag{9.1}
$$

The relative Fisher term is:

$$
\mathcal F_{\rm rel}
=
\int
|\nabla f_S|^2d\mu_0.
$$

Therefore:

$$
\boxed{
\mathcal F_{\rm rel}
=
4
\mathfrak J_S
\mathbb E_{\mu_4}
\left[
|\nabla\log K|^2
\right].
}
\tag{9.2}
$$

Thus, the common viscosity anti-intermittency term:

$$
-2\nu\mathcal F_{\rm rel}
$$

transforms exactly into:

$$
\boxed{
-8\nu
\mathfrak J_S
\mathbb E_{\mu_4}
\left[
|\nabla\log K|^2
\right].
}
\tag{9.3}
$$

---

# 10. Exact selection term in the $0$–$2$–$4$ tilt hierarchy

Round 21:

$$
\mathcal P_{\rm sel}
=
\int
f_S^2
\left[
3G_Q
+
2\mathcal R_S
-
2\overline C_S
+
3\overline G_Q
\right]
d\mu_0.
$$

where:

$$
\overline G_Q
=
\mathbb E_{\mu_0}[G_Q],
$$

$$
\overline C_S
=
\mathbb E_{\mu_2}
[
3G_Q+\mathcal R_S
].
$$

Since:

$$
\frac{
f_S^2
}{
\mathfrak J_S
}
d\mu_0
=
d\mu_4,
$$

we obtain:

$$
\boxed{
\begin{aligned}
\frac{
\mathcal P_{\rm sel}
}{
\mathfrak J_S
}
={}&
3
\left[
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\right]
\\
&+
2
\left[
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
\right],
\end{aligned}
}
\tag{10.1}
$$

where:

$$
\langle A\rangle_p
=
\mathbb E_{\mu_p}[A].
$$

We name this:

$$
\boxed{
\textbf{Tilt-Selection Decomposition}.
}
$$

---

# 11. Exact logarithmic intermittency law

From:

$$
\mathfrak J_S'
=
-2\nu\mathcal F_{\rm rel}
+
\mathcal P_{\rm sel}
$$

divided by:

$$
\mathfrak J_S>0
$$

and using Sections 9–10:

$$
\boxed{
\begin{aligned}
\frac d{dt}
\log\mathfrak J_S
={}&
-8\nu
\langle
|\nabla\log K|^2
\rangle_4
\\
&+
3
\left[
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\right]
\\
&+
2
\left[
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
\right].
\end{aligned}
}
\tag{11.1}
$$

This is the strongest exact identity of this round.

---

# 12. Continuous tilt derivatives

Let:

$$
L
=
\log K.
$$

For any observable that does not explicitly depend on $p$:

$$
A(x,t),
$$

exponential-tilt calculus gives:

$$
\boxed{
\frac d{dp}
\langle A\rangle_p
=
\operatorname{Cov}_{\mu_p}(A,L).
}
\tag{12.1}
$$

Differentiating again:

$$
\boxed{
\frac{d^2}{dp^2}
\langle A\rangle_p
=
\operatorname{Cov}_{\mu_p}
\left(
A,
(L-\langle L\rangle_p)^2
\right).
}
\tag{12.2}
$$

Thus, the tilt-order curvature itself is a covariance.

---

# 13. Continuous Tilt-Curvature Intermittency Law

By the fundamental theorem of calculus:

$$
\boxed{
\begin{aligned}
&
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\\
&=
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds.
\end{aligned}
}
\tag{13.1}
$$

and:

$$
\boxed{
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
=
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp.
}
\tag{13.2}
$$

Substituting into (11.1):

$$
\boxed{
\begin{aligned}
(\log\mathfrak J_S)'
={}&
-8\nu
\langle
|\nabla L|^2
\rangle_4
\\
&+
3
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds
\\
&+
2
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp.
\end{aligned}
}
\tag{13.3}
$$

We name this:

$$
\boxed{
\textbf{Continuous Tilt-Curvature Intermittency Law}.
}
$$

Thus, intermittency growth requires two types of continuous moment-order bias:

1. A positive tilt curvature of the critical-mass growth field with respect to the log-rate dispersion;
2. A positive covariance of the strain-specific relative source with respect to the log normalized-rate.

---

# 14. Intermittency growth necessity

If:

$$
(\log\mathfrak J_S)'>0,
$$

then we must have:

$$
\boxed{
\begin{aligned}
&
3
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds
\\
&+
2
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp
\\
&>
8\nu
\langle
|\nabla L|^2
\rangle_4.
\end{aligned}
}
\tag{14.1}
$$

Therefore, for the normalized strain intermittency to grow,

the bias of the NS selection/source along the continuous moment-order axis must overcome the spatial relative-Fisher smoothing.

---

# 15. Pressure source under a general tilt

Define the raw $p$-moment:

$$
\boxed{
\mathcal M_p
=
\int
r^{3-p}
|S|^pdx
=
Q^3Z_p.
}
\tag{15.1}
$$

From:

$$
\mathcal R_{\rm press}
=
-2
\frac{
S:H_p
}{
|S|^2
},
$$

we obtain:

$$
\boxed{
\langle
\mathcal R_{\rm press}
\rangle_p
=
-\frac2{\mathcal M_p}
\int
w_p
S:H_p\,dx,
}
\tag{15.2}
$$

where:

$$
\boxed{
w_p
=
r^{3-p}
|S|^{p-2}.
}
\tag{15.3}
$$

Specifically:

$$
\boxed{
w_2=r,
}
$$

$$
\boxed{
w_4=\frac{|S|^2}{r}.
}
$$

---

# 16. Weighted pressure cancellation identity

For any smooth scalar weight:

$$
w,
$$

using:

$$
S:H_p
=
\partial_j u_i
\partial_{ij}p
$$

and:

$$
\nabla\cdot u=0,
$$

integration by parts gives:

$$
\boxed{
\int
w
S:H_p\,dx
=
\int
u\cdot
\left[
(\Delta p)I-H_p
\right]
\nabla w\,dx.
}
\tag{16.1}
$$

When:

$$
w\equiv1,
$$

the right-hand side is zero, recovering the global pressure cancellation:

$$
\boxed{
\int
S:H_pdx=0.
}
$$

Thus, the pressure in the weighted relative-source is not a raw bulk term.

It completely transforms into:

$$
\boxed{
\text{pressure anisotropy}
\times
\text{tilt-weight gradient}.
}
$$

We name this:

$$
\boxed{
\textbf{Weighted Pressure-Commutator Identity}.
}
$$

---

# 17. Pressure contribution to intermittency is a weight-geometry contrast

From Sections 15–16:

$$
\boxed{
\begin{aligned}
\langle
\mathcal R_{\rm press}
\rangle_4
={}&
-\frac2{\mathcal M_4}
\int
u\cdot
\left[
(\Delta p)I-H_p
\right]
\nabla
\left(
\frac{|S|^2}{r}
\right)
dx,
\\
\langle
\mathcal R_{\rm press}
\rangle_2
={}&
-\frac2{\mathcal M_2}
\int
u\cdot
\left[
(\Delta p)I-H_p
\right]
\nabla r
\,dx.
\end{aligned}
}
\tag{17.1}
$$

Therefore:

$$
\boxed{
\langle
\mathcal R_{\rm press}
\rangle_4
-
\langle
\mathcal R_{\rm press}
\rangle_2
}
$$

only sees:

> the differential effect of pressure anisotropy on the high-normalized-strain tilt weight versus the ordinary strain-energy weight.

This is the return of the Round 04 pressure nonlocality in the language of dynamic intermittency.

---

# 18. Self-amplification source under the tilt hierarchy

From:

$$
\mathcal R_{\rm self}
=
-6
\frac{\det S}{|S|^2},
$$

we have:

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_p
=
-\frac6{\mathcal M_p}
\int
r^{3-p}
|S|^{p-2}
\det S\,dx.
}
\tag{18.1}
$$

In particular:

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_2
=
-\frac6{W_S}
\int
r\det S\,dx,
}
\tag{18.2}
$$

and:

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_4
=
-\frac6{\mathcal I_0}
\int
\frac{|S|^2}{r}
\det S\,dx.
}
\tag{18.3}
$$

Thus:

$$
\boxed{
\langle
\mathcal R_{\rm self}
\rangle_4
-
\langle
\mathcal R_{\rm self}
\rangle_2
}
$$

exactly measures:

> whether strain self-amplification is preferentially concentrated in high normalized-strain-rate regions.

---

# 19. Vorticity-coupling source under the tilt hierarchy

Similarly:

$$
\boxed{
\langle
\mathcal R_{\rm vort}
\rangle_p
=
-\frac1{2\mathcal M_p}
\int
r^{3-p}
|S|^{p-2}
\omega^\top S\omega
\,dx.
}
\tag{19.1}
$$

Thus:

$$
\boxed{
\langle
\mathcal R_{\rm vort}
\rangle_4
-
\langle
\mathcal R_{\rm vort}
\rangle_2
}
$$

measures:

> whether the vortex-stretching interaction preferentially falls in the high-$K$ tail.

The obstruction confluence of Rounds 18–19 thus directly reappears in the $\mathfrak J_S$ dynamics.

---

# 20. Quotient-growth source under the tilt hierarchy

From:

$$
\mathcal R_{\rm quot}
=
-2\gamma_Q,
$$

its contribution is:

$$
\boxed{
\langle
\mathcal R_{\rm quot}
\rangle_4
-
\langle
\mathcal R_{\rm quot}
\rangle_2
=
-2
\left[
\langle\gamma_Q\rangle_4
-
\langle\gamma_Q\rangle_2
\right].
}
\tag{20.1}
$$

Therefore, if high-normalized-strain regions are more biased toward the compressive quotient-growth geometry of:

$$
\gamma_Q>0
$$

it will directly become an intermittency selection source.

---

# 21. Diffusion and gauge terms remain genuinely relational

From (7.2):

$$
\mathcal R_{\rm diff}
$$

contains:

$$
|\nabla n|^2,
$$

$$
|\nabla\widehat S|^2,
$$

$$
|\nabla\log K|^2,
$$

and:

$$
\nabla\log r\cdot\nabla\log K.
$$

While:

$$
\mathcal R_{\rm gauge}
$$

by (6.2) depends only on:

$$
n\cdot\nabla\chi_g,
$$

and:

$$
n\cdot\nabla\log K.
$$

Thus, the remaining relative source is not a scalar amplitude problem.

It is:

$$
\boxed{
\text{orientation}
+
\text{rate gradient}
+
\text{quotient amplitude}
+
\text{gauge feedback}
}
$$

as a relational field.

---

# 22. Three exact pressure/self/vorticity conclusions

This round yields the following for the three main nonlinear sources:

## P1 — pressure

$$
\boxed{
\text{unweighted pressure cancels;
relative pressure survives only as a weight-gradient commutator}.
}
$$

## P2 — strain self-amplification

$$
\boxed{
\text{intermittency sees whether determinant production is biased toward high }K.
}
$$

## P3 — vortex stretching

$$
\boxed{
\text{intermittency sees whether }\omega^\top S\omega
\text{ is biased toward high }K.
}
$$

Therefore:

$$
\boxed{
\textbf{
intermittency is not caused merely by large nonlinear production;
it requires nonlinear production to be preferentially organized
in the high normalized-deformation tail.
}
}
\tag{22.1}
$$

---

# 23. Conditional self-closing branch

From (13.3), if:

$$
\boxed{
\begin{aligned}
&
3
\int_0^2
\int_s^{s+2}
\operatorname{Cov}_{\mu_\tau}
\left(
G_Q,
(L-\langle L\rangle_\tau)^2
\right)
d\tau ds
\\
&+
2
\int_2^4
\operatorname{Cov}_{\mu_p}
(
\mathcal R_S,L
)
dp
\\
&\le
8\nu
\langle
|\nabla L|^2
\rangle_4,
\end{aligned}
}
\tag{23.1}
$$

then:

$$
\boxed{
\mathfrak J_S'(t)\le0.
}
\tag{23.2}
$$

Thus, the Pure-C dynamic intermittency closure has been compressed into a single continuous tilt-covariance inequality.

---

# 24. Why this is not yet QED

Currently, (23.1) cannot be unconditionally derived from ordinary NS energy / enstrophy / critical quotient control.

In particular:

- determinant self-amplification may be biased toward high-$K$ regions;
- vortex stretching may be biased toward high-$K$ regions;
- pressure anisotropy may be strongly correlated with the tilt-weight gradient;
- gauge feedback may maintain the high-$K$ tail.

Therefore:

$$
\boxed{
\text{viscous relative Fisher smoothing exists,
but source organization can still defeat it}.
}
$$

---

# 25. STOP-C26 — Continuous Tilt-Selection / Relative-Source Gap

Define:

$$
\boxed{
\bot_X^{\mathrm{C26}}
=
\left\langle
\begin{array}{l}
\text{layer}
=
\mathrm{continuous\ moment\text{-}order\ intermittency},
\\
\text{tilt\ family}
=
\mu_p,\quad p\in[0,\infty),
\\
\text{spatial\ anti\text{-}intermittency}
=
8\nu\langle|\nabla\log K|^2\rangle_4,
\\
\text{growth\text{-}selection\ curvature}
=
\partial_p^2\langle G_Q\rangle_p,
\\
\text{relative\ source\ bias}
=
\partial_p\langle\mathcal R_S\rangle_p,
\\
\text{pressure}
=
\mathrm{weight\text{-}gradient\ commutator},
\\
\text{self\text{-}amplification}
=
\mathrm{high\text{-}K\ determinant\ bias},
\\
\text{vorticity\ coupling}
=
\mathrm{high\text{-}K\ stretching\ bias},
\\
\text{missing}
=
\mathrm{unconditional\ domination\ of\ continuous\ tilt\ bias
by\ relative\ Fisher\ smoothing},
\\
\text{essential\ discrete\ intrusion}
=
\mathrm{false}.
\end{array}
\right\rangle.
}
$$

We name this:

$$
\boxed{
\textbf{STOP-C26:
Continuous Tilt-Selection / Relative-Source Gap}.
}
$$

---

# 26. 24/72 Ledger — Round 22

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C276 | strain-amplitude PDE | $\mathsf C$ | differential | relational | $\mathsf F$ | EXACT |
| C277 | exact relative source $\mathcal R_S$ | $\mathsf C$ | coupled | $\mathsf X$ | $\mathsf F$ | EXACT |
| C278 | six-source decomposition | $\mathsf C$ | relational | $\mathsf X$ | $\mathsf F$ | EXACT |
| C279 | gauge-source simplification | $\mathsf C$ | nonlinear gauge | targeted | $\mathsf F$ | EXACT |
| C280 | normalized diffusion decomposition | $\mathsf C$ | differential | relational | $\mathsf F$ | EXACT |
| C281 | continuous tilt $\mu_p$ | $\mathsf C$ | continuous $p$ | profile | $\mathsf F$ | FORM |
| C282 | relative Fisher as $\mu_4$ expectation | $\mathsf C$ | measure | scalar | $\mathsf F$ | EXACT |
| C283 | tilt-selection decomposition | $\mathsf C$ | measure hierarchy | scalar | $\mathsf F$ | EXACT |
| C284 | log-intermittency law | $\mathsf C$ | coupled | scalar | $\mathsf F$ | EXACT |
| C285 | tilt derivative covariance | $\mathsf C$ | continuous $p$ | relational | $\mathsf F$ | EXACT |
| C286 | continuous tilt-curvature law | $\mathsf C$ | continuous moment order | profile | $\mathsf F$ | EXACT |
| C287 | weighted pressure commutator | $\mathsf C$ | nonlocal/weight | relational | $\mathsf F$ | EXACT |
| C288 | determinant high-$K$ bias | $\mathsf C$ | strain geometry | targeted | $\mathsf F$ | EXACT reformulation |
| C289 | stretching high-$K$ bias | $\mathsf C$ | strain-vorticity | targeted | $\mathsf F$ | EXACT reformulation |
| C290 | unconditional tilt-bias domination | $\mathsf C$ | — | targeted | $\mathsf F$ | OPEN / STOP-C26 |

---

# 27. Continuous-versus-discrete status

The quantities in this round that most easily appear discrete:

$$
p=0,2,4
$$

are once again re-integrated into the continuous moment-order axis:

$$
\boxed{
p\in[0,\infty)
}
$$

And the:

$$
\mathfrak J_S
$$

growth is ultimately written as:

- a physical-space Fisher gradient;
- a moment-order covariance curvature.

Therefore, there is still no need to introduce:

- an integer moment hierarchy;
- discrete tail bins;
- atomic probability states;
- a stochastic transition kernel.

Thus:

$$
\boxed{
B=\mathsf C,
\qquad
L=\mathsf F,
}
$$

and:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
\tag{27.1}
$$

---

# 28. Strongest results of Round 22

## R22-A — exact relative-source decomposition

$$
\boxed{
\mathcal R_S
=
\mathcal R_{\rm self}
+
\mathcal R_{\rm vort}
+
\mathcal R_{\rm press}
+
\mathcal R_{\rm quot}
+
\mathcal R_{\rm diff}
+
\mathcal R_{\rm gauge}.
}
$$

## R22-B — exact log-intermittency law

$$
\boxed{
\begin{aligned}
(\log\mathfrak J_S)'
={}&
-8\nu
\langle|\nabla\log K|^2\rangle_4
\\
&+
3
\left[
\langle G_Q\rangle_4
-
2\langle G_Q\rangle_2
+
\langle G_Q\rangle_0
\right]
\\
&+
2
\left[
\langle\mathcal R_S\rangle_4
-
\langle\mathcal R_S\rangle_2
\right].
\end{aligned}
}
$$

## R22-C — continuous moment-order formulation

$$
\boxed{
\text{finite differences in }p
=
\text{continuous covariance integrals in }p.
}
$$

## R22-D — weighted pressure transmutation

$$
\boxed{
\int
wS:H_p
=
\int
u\cdot[(\Delta p)I-H_p]\nabla w.
}
$$

Thus, the pressure relative source survives only through tilt-weight gradients.

---

# 29. Next round — confluence-feedback closure test

The next round will no longer continue to expand the source taxonomy.

It will directly substitute Round 19's:

$$
\lambda_2^+,
\quad
(-\det S)_+,
\quad
\chi_C
$$

into Round 22's tilt-covariance law.

Core questions:

1. whether the dangerous determinant equivalence allows:
   $$
   \mathcal R_{\rm self}
   $$
   to have its positive high-$K$ bias directly controlled by the confluence ratio;

2. whether the middle-strain floor restricts:
   $$
   \partial_p\langle\mathcal R_{\rm self}\rangle_p;
   $$

3. whether the vorticity coupling can partially cancel or align in sign with the determinant source in the tilt difference;

4. whether the weighted pressure commutator can be absorbed by:
   $$
   |\nabla\log K|
   $$
   's relative Fisher term;

5. if these terms can form:
   $$
   \text{source bias}
   \le
   c\nu
   \langle|\nabla\log K|^2\rangle_4
   $$
   , which would form the first genuine self-closing feedback candidate.

---

# 30. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - strain–vorticity interaction;
   - projected strain structure;
   - global enstrophy identities and nonlinear depletion background.

2. Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.
   - scale-critical regularity background of the positive middle-eigenvalue channel.

The relative-source decomposition, continuous tilt calculus, log-intermittency law, and weighted pressure-commutator identity in this round are all directly derived in this document.

---

# 31. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Relative\text{-}Source/Tilt\ Curvature},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Normalized rate}
&=
K=|S|/|v|,
\\
\text{Tilt family}
&=
\mu_p,\ p\in[0,\infty),
\\
\text{Spatial smoothing}
&=
8\nu\langle|\nabla\log K|^2\rangle_4,
\\
\text{Moment-order danger}
&=
\mathrm{selection\ curvature}
+
\mathrm{relative\ source\ covariance},
\\
\text{Pressure source}
&=
\mathrm{weight\text{-}gradient\ commutator},
\\
\text{Self/vorticity source}
&=
\mathrm{high\text{-}K\ preferential\ bias},
\\
\text{STOP-C26}
&=
\mathrm{Continuous\ Tilt\text{-}Selection/Relative\text{-}Source\ Gap},
\\
\text{Next}
&=
\mathrm{Confluence\text{-}Feedback\ Closure\ Test}.
\end{aligned}
}
$$