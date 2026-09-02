# NS × X Integral × 24/72 Paradigm in Action
## Round 45 — Pure Continuous Visibility Replicator / Quartic Alignment and Boundary-Injection Dynamics

- Date:  2026-08-17
- Version:  v0.1
- Status:  Proof-Route Experiment / Continuous-Only Dynamic-Visibility Branch
- canonical source: UTF-8 Markdown
- canonical math delimiters: inline `$...$`; display `$$...$$`
- Previous round:  `NS_X72_Round44_PureContinuous_VorticityStress_ActualTriadRealizability_v0.1_2026-08-17.md`
- This round's objective:  Round 44 proved that neither static divdiv geometry nor actual quadratic vorticity realizability can eliminate a transport derivative between visible/invisible stress. Therefore, this round halts the static realizability attack and directly investigates the exact dynamics of the visibility ratio
  $$
  \eta_\omega
  =
  \frac{\|W_L\|_2^2}{\|W_L\|_2^2+\|W_T\|_2^2}
  $$
  It is decomposed into stretching selection, Laplacian scale selection, gradient-stress selection, and conservative Riesz-transfer, while investigating whether pure-visible / pure-invisible boundaries are dynamically invariant.
- Non-claims:  This document does not prove that $\eta_\omega$ is monotonic, nor does it prove that mixed visibility must vanish. Conversely, this round proves that neither inviscid selection nor transfer has a universal sign; pure sectors are stationary at first order, but generally exhibit second-order cross-sector injection; meanwhile, an exact periodic Beltrami pure-invisible invariant branch exists.

---

# 0. Round 44 handoff

trace-free vorticity stress:

$$
\boxed{
W
=
\omega\otimes\omega
-
\frac13|\omega|^2I.
}
\tag{0.1}
$$

Round 42–44 decomposition:

$$
\boxed{
W=W_L+W_T,
}
\tag{0.2}
$$

with orthogonal Riesz projection:

$$
\boxed{
W_L=\mathbb P_LW,
\qquad
W_T=\mathbb P_TW,
\qquad
\mathbb P_T=I-\mathbb P_L.
}
\tag{0.3}
$$

and:

$$
\boxed{
\langle W_L,W_T\rangle_{L^2}=0.
}
\tag{0.4}
$$

Round 42 visibility Pythagorean:

$$
\boxed{
\frac23
\|\omega\|_4^4
=
24
\|\mathfrak V_\omega\|_2^2
+
\|W_T\|_2^2.
}
\tag{0.5}
$$

Round 44 proved that actual vorticity triads can still generate a one-derivative visible/invisible transfer.

Round 44 STOP:

$$
\boxed{
\text{STOP-C48}
=
\text{Actual-Vorticity Triad / Dynamic-Only Depletion Gap}.
}
$$

---

# 1. Visible, invisible and total stress energies

Definition:

$$
\boxed{
E_L
=
\|W_L\|_2^2,
}
\tag{1.1}
$$

$$
\boxed{
E_T
=
\|W_T\|_2^2,
}
\tag{1.2}
$$

$$
\boxed{
E
=
E_L+E_T
=
\|W\|_2^2
=
\frac23
\|\omega\|_4^4.
}
\tag{1.3}
$$

visibility ratio:

$$
\boxed{
\eta
=
\eta_\omega
=
\frac{E_L}{E}
\in[0,1].
}
\tag{1.4}
$$

Therefore:

$$
\boxed{
E_L=\eta E,
\qquad
E_T=(1-\eta)E.
}
\tag{1.5}
$$

Additionally, from:

$$
E_L
=
24\|\mathfrak V_\omega\|_2^2,
$$

we have:

$$
\boxed{
\eta
=
\frac{
36\|\mathfrak V_\omega\|_2^2
}{
\|\omega\|_4^4
}.
}
\tag{1.6}
$$

---

# 2. Stress-source decomposition

Round 42 exact stress PDE:

$$
\boxed{
(D_t-\nu\Delta)W
=
B_\omega^0
-
2\nu G_\omega^0.
}
\tag{2.1}
$$

where:

$$
\boxed{
B_\omega^0
=
S\omega\otimes\omega
+
\omega\otimes S\omega
-
\frac23
(\omega^\top S\omega)I,
}
\tag{2.2}
$$

and:

$$
\boxed{
G_\omega^0
=
\sum_k
\partial_k\omega
\otimes
\partial_k\omega
-
\frac13
|\nabla\omega|^2I.
}
\tag{2.3}
$$

Denote for simplicity:

$$
\boxed{
\mathcal R_\omega
=
B_\omega^0
-
2\nu G_\omega^0.
}
\tag{2.4}
$$

---

# 3. Projected stress equations

Round 42:

$$
\boxed{
(D_t-\nu\Delta)W_L
=
\mathbb P_L\mathcal R_\omega
+
\mathcal C_PW,
}
\tag{3.1}
$$

$$
\boxed{
(D_t-\nu\Delta)W_T
=
\mathbb P_T\mathcal R_\omega
-
\mathcal C_PW,
}
\tag{3.2}
$$

where:

$$
\boxed{
\mathcal C_P
=
[D_u,\mathbb P_L],
\qquad
D_u=u\cdot\nabla.
}
\tag{3.3}
$$

$\mathcal C_P$ is self-adjoint and off-diagonal with respect to:

$$
L\oplus T.
$$

---

# 4. Exact sector energy equations

Define:

$$
\boxed{
\mathcal S_L
=
\langle
W_L,
B_\omega^0
\rangle,
\qquad
\mathcal S_T
=
\langle
W_T,
B_\omega^0
\rangle,
}
\tag{4.1}
$$

$$
\boxed{
\mathcal G_L
=
\langle
W_L,
G_\omega^0
\rangle,
\qquad
\mathcal G_T
=
\langle
W_T,
G_\omega^0
\rangle,
}
\tag{4.2}
$$

$$
\boxed{
\mathcal D_L
=
\|\nabla W_L\|_2^2,
\qquad
\mathcal D_T
=
\|\nabla W_T\|_2^2.
}
\tag{4.3}
$$

Round 42 transfer:

$$
\boxed{
\mathcal X
=
\mathcal X_\omega
=
\langle
W_L,
\mathcal C_PW_T
\rangle.
}
\tag{4.4}
$$

Then:

$$
\boxed{
\frac12E_L'
=
\mathcal S_L
-
\nu\mathcal D_L
-
2\nu\mathcal G_L
+
\mathcal X,
}
\tag{4.5}
$$

$$
\boxed{
\frac12E_T'
=
\mathcal S_T
-
\nu\mathcal D_T
-
2\nu\mathcal G_T
-
\mathcal X.
}
\tag{4.6}
$$

---

# 5. Sector fitnesses

For:

$$
E_L>0,
\qquad
E_T>0,
$$

define:

$$
\boxed{
s_L
=
\frac{\mathcal S_L}{E_L},
\qquad
s_T
=
\frac{\mathcal S_T}{E_T},
}
\tag{5.1}
$$

$$
\boxed{
d_L
=
\frac{\mathcal D_L}{E_L},
\qquad
d_T
=
\frac{\mathcal D_T}{E_T},
}
\tag{5.2}
$$

$$
\boxed{
g_L
=
\frac{\mathcal G_L}{E_L},
\qquad
g_T
=
\frac{\mathcal G_T}{E_T}.
}
\tag{5.3}
$$

Define net sector fitness:

$$
\boxed{
f_L
=
s_L
-
\nu d_L
-
2\nu g_L,
}
\tag{5.4}
$$

$$
\boxed{
f_T
=
s_T
-
\nu d_T
-
2\nu g_T.
}
\tag{5.5}
$$

Thus:

$$
\boxed{
E_L'
=
2f_LE_L
+
2\mathcal X,
}
\tag{5.6}
$$

$$
\boxed{
E_T'
=
2f_TE_T
-
2\mathcal X.
}
\tag{5.7}
$$

---

# 6. Exact Visibility Replicator Equation

From:

$$
\eta
=
E_L/E,
$$

and:

$$
E'=E_L'+E_T',
$$

we obtain:

$$
\boxed{
\eta'
=
2\eta(1-\eta)
(
f_L-f_T
)
+
\frac{
2\mathcal X
}{
E
}.
}
\tag{6.1}
$$

Named:

$$
\boxed{
\textbf{Visibility Replicator Equation}.
}
$$

Expanding the fitness:

$$
\boxed{
\begin{aligned}
\eta'
={}&
2\eta(1-\eta)
[
s_L-s_T
]
\\
&-
2\nu
\eta(1-\eta)
[
d_L-d_T
]
\\
&-
4\nu
\eta(1-\eta)
[
g_L-g_T
]
\\
&+
\frac{
2\mathcal X
}{
E
}.
\end{aligned}
}
\tag{6.2}
$$

---

# 7. Four visibility drivers

Equation (6.2) decomposes the dynamics into four categories:

## V1 — stretching selection

$$
\boxed{
2\eta(1-\eta)
(
s_L-s_T
).
}
$$

## V2 — Laplacian scale selection

$$
\boxed{
-2\nu
\eta(1-\eta)
(
d_L-d_T
).
}
$$

If the visible sector normalized gradient cost is higher:

$$
d_L>d_T,
$$

the pure Laplacian effect decreases:

$$
\eta.
$$

## V3 — gradient-stress selection

$$
\boxed{
-4\nu
\eta(1-\eta)
(
g_L-g_T
).
}
$$

This term has no universal sign.

## V4 — conservative representation transfer

$$
\boxed{
\frac{
2\mathcal X
}{
E
}.
}
$$

It does not change the total stress energy,

only the visible/invisible split.

---

# 8. Total stress fitness

weighted sector mean:

$$
\boxed{
\overline f
=
\eta f_L
+
(1-\eta)f_T
=
\frac{
E'
}{
2E
}.
}
\tag{8.1}
$$

Let:

$$
Z_4
=
\|\omega\|_4^4.
$$

Round 42 quartic identity:

$$
\boxed{
\begin{aligned}
\frac13
Z_4'
&+
4\nu
\int
|\omega|^2
|\nabla|\omega||^2dx
\\
&+
\frac{4\nu}{3}
\int
|\omega|^4
|\nabla\xi|^2dx
\\
&=
\frac43
\int
|\omega|^4
\lambda_\omega
dx,
\end{aligned}
}
\tag{8.2}
$$

where:

$$
\xi
=
\frac{\omega}{|\omega|},
$$

$$
\lambda_\omega
=
\xi^\top S\xi.
$$

Define the quartic vorticity probability:

$$
\boxed{
d\mu_{\omega,4}
=
\frac{
|\omega|^4
}{
Z_4
}
dx.
}
\tag{8.3}
$$

Then:

$$
\boxed{
\begin{aligned}
\overline f
={}&
2
\langle
\lambda_\omega
\rangle_{\mu_{\omega,4}}
\\
&-
6\nu
\frac{
\int
|\omega|^2
|\nabla|\omega||^2
}{
Z_4
}
\\
&-
2\nu
\frac{
\int
|\omega|^4
|\nabla\xi|^2
}{
Z_4
}.
\end{aligned}
}
\tag{8.4}
$$

Thus, total stress growth is still completely controlled by quartic alignment minus amplitude/direction diffusion.

---

# 9. Stretching selection is a relative alignment effect

The sector stretching rates:

$$
s_L,
\qquad
s_T
$$

are not local conditional expectations,

because:

$$
W_L,W_T
$$

are nonlocal Riesz projections.

However, their weighted mean exactly satisfies:

$$
\boxed{
\eta s_L
+
(1-\eta)s_T
=
2
\langle
\lambda_\omega
\rangle_{\mu_{\omega,4}}.
}
\tag{9.1}
$$

Therefore:

$$
\boxed{
s_L-s_T
}
$$

measures:

$$
\boxed{
\text{the relative response of visible versus invisible stress to the quartic stretching source}.
}
$$

It is a global projection-selection quantity.

---

# 10. Laplacian selection is genuinely sign-directed

Since:

$$
d_L,d_T\ge0,
$$

the pure Laplacian contribution is:

$$
\boxed{
\eta'_{\rm Lap}
=
-2\nu
\eta(1-\eta)
(
d_L-d_T
).
}
\tag{10.1}
$$

Therefore:

- If the visible sector has a higher normalized spatial frequency:
  $$
  d_L>d_T,
  $$
  viscosity favors the invisible sector;
- If the invisible sector is rougher:
  $$
  d_T>d_L,
  $$
  viscosity favors the visible sector.

Thus, viscosity is not intrinsically visible-depleting.

It favors:

$$
\boxed{
\text{the smoother stress sector}.
}
$$

---

# 11. Gradient-stress viscosity is not sectorwise positive

The total combination:

$$
\boxed{
\mathcal D_L+\mathcal D_T
+
2(
\mathcal G_L+\mathcal G_T
)
}
$$

can be reduced to positive quartic amplitude/direction dissipation.

But the individual:

$$
\boxed{
\mathcal D_j
+
2\mathcal G_j
}
$$

need not be non-negative.

Therefore, we cannot assign a universal sign to:

$$
g_L-g_T
$$

That is:

$$
\boxed{
\text{total vorticity-stress diffusion is coercive,
but sectorwise projected diffusion need not be.}
}
$$

---

# 12. Transfer has no universal sign

The Round 44 Actual-Vorticity Transfer Triad gives:

$$
\boxed{
\mathcal X_{\rm triad}
\ne0.
}
$$

In this construction, changing one of the input vorticity amplitudes:

$$
b
$$

to:

$$
-b
$$

will flip the sign of the corresponding invisible input stress coefficient:

$$
B
$$

while the transport velocity and the chosen matching visible output channel can be preserved.

Therefore, this triad contribution:

$$
\boxed{
\mathcal X_{\rm triad}
}
$$

can change sign.

Thus:

$$
\boxed{
\textbf{
transport projection transfer can move quartic stress in either direction}.
}
\tag{12.1}
$$

It is not a visible-to-invisible entropy law.

---

# 13. Inviscid sign-reversal no-go for monotonic visibility

Consider the instantaneous transformation:

$$
\boxed{
u\mapsto-u.
}
\tag{13.1}
$$

Then:

$$
\omega\mapsto-\omega,
$$

so:

$$
W,W_L,W_T,E_L,E_T,\eta
$$

all remain unchanged.

But:

$$
S\mapsto-S.
$$

Therefore, the stretching source:

$$
\boxed{
B_\omega^0
\mapsto
-B_\omega^0,
}
\tag{13.2}
$$

while:

$$
G_\omega^0
$$

remains unchanged.

At the same time:

$$
\boxed{
[D_u,\mathbb P_L]
\mapsto
-[D_u,\mathbb P_L].
}
\tag{13.3}
$$

Thus:

$$
\boxed{
s_L-s_T
\mapsto
-(s_L-s_T),
}
\tag{13.4}
$$

$$
\boxed{
\mathcal X
\mapsto
-\mathcal X.
}
\tag{13.5}
$$

In the inviscid:

$$
\nu=0
$$

instantaneous geometry:

$$
\boxed{
\eta'
\mapsto
-\eta'.
}
\tag{13.6}
$$

Therefore, there is no purely algebraic universal inviscid law:

$$
\boxed{
\eta'\ge0
}
$$

or:

$$
\boxed{
\eta'\le0.
}
$$

Named:

$$
\boxed{
\textbf{Inviscid Visibility Monotonicity No-Go}.
}
$$

---

# 14. Strong-branch transfer envelope

Round 42 strong regularity estimate:

$$
\boxed{
|\mathcal X|
\lesssim
\|\nabla u\|_\infty
\|W_L\|_2
\|W_T\|_2.
}
\tag{14.1}
$$

Thus:

$$
\boxed{
\left|
\frac{
2\mathcal X
}{
E
}
\right|
\lesssim
\|\nabla u\|_\infty
\sqrt{
\eta(1-\eta)
}.
}
\tag{14.2}
$$

Therefore, the first-order effect of transport transfer vanishes at:

$$
\eta=0
$$

and:

$$
\eta=1
$$

The maximum geometric transfer capacity occurs in the mixed visibility interior.

---

# 15. Visibility log-odds equation

If:

$$
0<\eta<1,
$$

define:

$$
\boxed{
\Lambda_\eta
=
\log
\frac{
\eta
}{
1-\eta
}.
}
\tag{15.1}
$$

Then:

$$
\boxed{
\Lambda_\eta'
=
2(
f_L-f_T
)
+
\frac{
2\mathcal X
}{
E\eta(1-\eta)
}.
}
\tag{15.2}
$$

If:

$$
\mathcal X=0,
$$

it exactly reduces to the classic relative-fitness log-odds:

$$
\boxed{
\Lambda_\eta'
=
2(
f_L-f_T
).
}
\tag{15.3}
$$

The commutator transfer acts as a sector-conversion term rather than multiplicative selection.

---

# 16. Pure sectors are first-order stationary

If:

$$
\eta(t_0)=0,
$$

then:

$$
W_L(t_0)=0.
$$

Therefore:

$$
\mathcal X(t_0)=0,
$$

$$
\mathcal S_L(t_0)=0,
$$

$$
\mathcal D_L(t_0)=0,
$$

$$
\mathcal G_L(t_0)=0.
$$

Thus:

$$
\boxed{
E_L'(t_0)=0,
}
\tag{16.1}
$$

and:

$$
\boxed{
\eta'(t_0)=0.
}
\tag{16.2}
$$

Similarly, when:

$$
\eta(t_0)=1
$$

we have:

$$
\boxed{
\eta'(t_0)=0.
}
\tag{16.3}
$$

Thus, pure sectors are tangent-stationary boundaries.

---

# 17. Pure invisible boundary has a second-order injection law

At:

$$
\eta(t_0)=0,
$$

we have:

$$
W=W_T.
$$

From the projected PDE,

since:

$$
W_L(t_0)\equiv0
$$

as a spatial field,

the homogeneous $W_L$ terms in:

$$
D_tW_L,
\Delta W_L
$$

vanish at that instant.

Define the visible injection forcing:

$$
\boxed{
F_L
=
\mathbb P_L\mathcal R_\omega
+
[D_u,\mathbb P_L]W_T.
}
\tag{17.1}
$$

Then:

$$
\boxed{
\partial_tW_L(t_0)
=
F_L(t_0).
}
\tag{17.2}
$$

Thus:

$$
\boxed{
E_L''(t_0)
=
2
\|F_L(t_0)\|_2^2.
}
\tag{17.3}
$$

If:

$$
E(t_0)>0,
$$

then:

$$
\boxed{
\eta''(t_0)
=
\frac{
2
\|F_L(t_0)\|_2^2
}{
E(t_0)
}
\ge0.
}
\tag{17.4}
$$

Named:

$$
\boxed{
\textbf{Pure-Invisible Second-Order Injection Law}.
}
$$

Therefore, exact invisibility is not a generic first-order attractor.

---

# 18. Pure visible boundary has the dual injection law

If:

$$
\eta(t_0)=1,
$$

then:

$$
W_T(t_0)=0.
$$

Define:

$$
\boxed{
F_T
=
\mathbb P_T\mathcal R_\omega
-
[D_u,\mathbb P_L]W_L.
}
\tag{18.1}
$$

Then:

$$
\boxed{
\partial_tW_T(t_0)
=
F_T(t_0),
}
\tag{18.2}
$$

$$
\boxed{
E_T''(t_0)
=
2
\|F_T(t_0)\|_2^2.
}
\tag{18.3}
$$

Since:

$$
1-\eta
=
E_T/E,
$$

we obtain:

$$
\boxed{
\eta''(t_0)
=
-
\frac{
2
\|F_T(t_0)\|_2^2
}{
E(t_0)
}
\le0.
}
\tag{18.4}
$$

Thus, the pure visible boundary is likewise typically pulled back into the interior by second-order invisible injection.

---

# 19. Pure-sector invariance criterion

Sections 17–18 show:

for a pure sector to be truly invariant over a time interval,

it must at least continuously satisfy:

## invisible invariant condition

$$
\boxed{
\mathbb P_L\mathcal R_\omega
+
[D_u,\mathbb P_L]W_T
=
0.
}
\tag{19.1}
$$

## visible invariant condition

$$
\boxed{
\mathbb P_T\mathcal R_\omega
-
[D_u,\mathbb P_L]W_L
=
0.
}
\tag{19.2}
$$

Thus, pure visibility does not rely solely on:

$$
W_L=0
$$

or:

$$
W_T=0.
$$

It also requires:

$$
\boxed{
\text{source projection}
+
\text{transport projection leakage}
}
$$

exact cancellation.

---

# 20. Exact periodic Beltrami pure-invisible branch

On:

$$
\mathbb T^3,
$$

let:

$$
\boxed{
u(x,t)
=
A
e^{-\nu t}
\begin{pmatrix}
\cos x_3\\
-\sin x_3\\
0
\end{pmatrix}.
}
\tag{20.1}
$$

Then:

$$
\boxed{
\nabla\cdot u=0,
}
\tag{20.2}
$$

$$
\boxed{
\nabla\times u=u,
}
\tag{20.3}
$$

$$
\boxed{
\Delta u=-u.
}
\tag{20.4}
$$

And:

$$
(u\cdot\nabla)u=0
$$

since the field only depends on:

$$
x_3
$$

and:

$$
u_3=0.
$$

Thus:

$$
\boxed{
\partial_tu
+
(u\cdot\nabla)u
=
\nu\Delta u
}
\tag{20.5}
$$

with constant pressure.

This is an exact smooth periodic NS solution.

---

# 21. Beltrami stress is Riesz-invisible

For this solution:

$$
\omega=u.
$$

Let:

$$
v(x_3)
=
(
\cos x_3,
-\sin x_3,
0
).
$$

Then:

$$
\boxed{
W
=
A^2
e^{-2\nu t}
\left[
v\otimes v
-
\frac13I
\right].
}
\tag{21.1}
$$

Its nonzero Fourier stress harmonics are located only at:

$$
\pm2e_3.
$$

For these harmonics:

$$
\boxed{
(W_{\pm2e_3})_{33}=0.
}
\tag{21.2}
$$

Thus:

$$
\boxed{
\mathbb P_L(\pm e_3)
W_{\pm2e_3}
=
0.
}
\tag{21.3}
$$

The zero-frequency mean stress for the homogeneous Riesz projection takes:

$$
\mathbb P_L(0)=0.
$$

Therefore:

$$
\boxed{
W_L(t)\equiv0,
}
\tag{21.4}
$$

$$
\boxed{
\eta(t)\equiv0.
}
\tag{21.5}
$$

and necessarily:

$$
\boxed{
F_L(t)\equiv0.
}
\tag{21.6}
$$

Named:

$$
\boxed{
\textbf{Beltrami Pure-Invisible Invariant Branch}.
}
$$

---

# 22. Boundary injection is generic but not universal

Section 17 says:

$$
F_L\ne0
\Rightarrow
\eta''>0
$$

at exact invisibility.

Section 21 gives:

$$
F_L=0
$$

for a nontrivial exact NS branch.

Thus:

$$
\boxed{
\textbf{
pure invisibility is dynamically possible but requires a special source-transfer compatibility.
}
}
\tag{22.1}
$$

There is no universal:

$$
\eta''>0.
$$

---

# 23. Piola-defect escape dichotomy

From:

$$
\eta
=
\frac{
36
\|\mathfrak V_\omega\|_2^2
}{
\|\omega\|_4^4
},
$$

if a hypothetical branch:

$$
\boxed{
\|\omega(t)\|_4^4
\to\infty
}
\tag{23.1}
$$

as:

$$
t\uparrow T,
$$

then we have the exact dichotomy:

## visible Piola-defect branch

If there exists:

$$
\eta_\ast>0
$$

and a sequence:

$$
t_n\uparrow T
$$

such that:

$$
\eta(t_n)\ge\eta_\ast,
$$

then:

$$
\boxed{
\|\mathfrak V_\omega(t_n)\|_2^2
\ge
\frac{
\eta_\ast
}{
36
}
\|\omega(t_n)\|_4^4
\to\infty.
}
\tag{23.2}
$$

## asymptotically invisible escape branch

If:

$$
\boxed{
\sup_{t<T}
\|\mathfrak V_\omega(t)\|_2
<
\infty
}
\tag{23.3}
$$

while:

$$
\|\omega\|_4^4\to\infty,
$$

then necessarily:

$$
\boxed{
\eta(t)\to0.
}
\tag{23.4}
$$

Named:

$$
\boxed{
\textbf{Piola-Defect Escape Dichotomy}.
}
$$

---

# 24. Invisible escape requires dynamic boundary compatibility

Round 44 proved that actual realizability does not prohibit:

$$
\eta\approx0.
$$

Round 45 now shows that if a hypothetical dangerous branch is to achieve:

$$
\eta\to0,
$$

it must additionally suppress the visible-sector injection mechanism:

$$
\boxed{
F_L
=
\mathbb P_L
(
B_\omega^0-2\nu G_\omega^0
)
+
[D_u,\mathbb P_L]W_T.
}
\tag{24.1}
$$

at least in a cumulative / asymptotic sense.

Therefore, the remaining invisible escape route is not the static condition:

$$
W_L\approx0
$$

alone.

It is a dynamical compatibility among:

- projected stretching;
- projected vorticity-gradient source;
- transport projection leakage.

This is the direct target of the next round.

---

# 25. Transfer cancellation ledger

From the visible energy equation:

$$
\frac12E_L'
=
\mathcal S_L
-
\nu\mathcal D_L
-
2\nu\mathcal G_L
+
\mathcal X,
$$

on the interval:

$$
I=[t_0,t_1],
$$

we have the exact signed-transfer reconstruction:

$$
\boxed{
\begin{aligned}
\int_I
\mathcal Xdt
={}&
\frac12
[
E_L(t_1)-E_L(t_0)
]
\\
&-
\int_I
\mathcal S_Ldt
+
\nu
\int_I
\mathcal D_Ldt
+
2\nu
\int_I
\mathcal G_Ldt.
\end{aligned}
}
\tag{25.1}
$$

Thus, the cumulative **signed** representation transfer has no independent degrees of freedom.

But:

$$
\boxed{
\int_I|\mathcal X|dt
}
$$

may still be large.

Therefore, the transfer itself can also exhibit rapid cancellation / phase oscillation,

connecting back once again to the cancellation family of Rounds 27 and 34.

---

# 26. Visibility selection has no static direction

This round yields three no-gos:

1. stretching selection:
   $$
   s_L-s_T
   $$
   is sign-indefinite;

2. transfer:
   $$
   \mathcal X
   $$
   is sign-indefinite;

3. sectorwise gradient-stress diffusion:
   $$
   g_L-g_T
   $$
   is sign-indefinite.

Only the pure Laplacian scale-selection part has a definite interpretation:

$$
\boxed{
\text{viscosity favors the sector with lower normalized gradient cost}.
}
$$

Thus:

$$
\boxed{
\textbf{
there is no universal visible or invisible attractor at the level of the exact first-order ratio equation.
}
}
\tag{26.1}
$$

---

# 27. STOP-C49 — Visibility Replicator / Boundary-Injection Compatibility Gap

$$
\boxed{
\begin{aligned}
\text{layer}
&=
\mathrm{dynamic\ Riesz\ visibility},
\\
\eta
&=
E_L/(E_L+E_T),
\\
\text{replicator}
&=
2\eta(1-\eta)(f_L-f_T)
+
2\mathcal X/E,
\\
\text{stretching selection}
&=
\mathrm{sign\text{-}indefinite},
\\
\text{Laplacian selection}
&=
\mathrm{favors\ smoother\ sector},
\\
\text{gradient-stress selection}
&=
\mathrm{sign\text{-}indefinite},
\\
\text{transfer}
&=
\mathrm{conservative\ and\ sign\text{-}indefinite},
\\
\eta=0,1
&=
\mathrm{first\text{-}order\ stationary},
\\
\text{generic pure-sector injection}
&=
\mathrm{second\ order},
\\
\text{pure invisible invariant branch}
&=
\mathrm{exists\ (Beltrami)},
\\
\text{quartic blowup with bounded Piola defect}
&\Rightarrow
\eta\to0,
\\
\text{missing}
&=
\mathrm{control\ of\ visible\ boundary\ injection}
\\
&\quad
\mathbb P_L\mathcal R_\omega
+
[D_u,\mathbb P_L]W_T,
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
\textbf{STOP-C49:
Visibility Replicator / Boundary-Injection Compatibility Gap}.
}
$$

---

# 28. 24/72 Ledger — Round 45

| Step | object | $B$ | $U$ | $O$ | $L$ | status |
|---|---|---|---|---|---|---|
| C696 | visible/invisible stress energies | $\mathsf C$ | Hilbert projection | scalar | $\mathsf F$ | FORM |
| C697 | sector source decomposition | $\mathsf C$ | stress PDE | relational | $\mathsf F$ | EXACT |
| C698 | sector fitnesses | $\mathsf C$ | normalized dynamics | scalar | $\mathsf F$ | FORM |
| C699 | Visibility Replicator Equation | $\mathsf C$ | ratio dynamics | targeted | $\mathsf F$ | EXACT |
| C700 | four-driver decomposition | $\mathsf C$ | selection/transfer | $\mathsf X$ | $\mathsf F$ | EXACT |
| C701 | total quartic fitness | $\mathsf C$ | vorticity probability | scalar | $\mathsf F$ | EXACT |
| C702 | relative stretching selection | $\mathsf C$ | projection geometry | targeted | $\mathsf F$ | IDENTIFIED |
| C703 | Laplacian scale selection | $\mathsf C$ | normalized gradients | targeted | $\mathsf F$ | EXACT |
| C704 | sector diffusion noncoercivity | $\mathsf C$ | projected stress | targeted | $\mathsf F$ | IDENTIFIED |
| C705 | transfer sign no-go | $\mathsf C$ | actual triad | targeted | $\mathsf F$ | CONSTRUCTED |
| C706 | inviscid monotonicity no-go | $\mathsf C$ | sign reversal | targeted | $\mathsf F$ | PROVED |
| C707 | strong transfer envelope | $\mathsf C$ | commutator bound | scalar | $\mathsf F$ | CONDITIONAL |
| C708 | visibility log-odds | $\mathsf C$ | ratio transform | scalar | $\mathsf F$ | EXACT |
| C709 | pure-sector first-order stationarity | $\mathsf C$ | projection energy | targeted | $\mathsf F$ | EXACT |
| C710 | invisible second-order injection | $\mathsf C$ | projected PDE | targeted | $\mathsf F$ | EXACT |
| C711 | visible second-order injection | $\mathsf C$ | projected PDE | targeted | $\mathsf F$ | EXACT |
| C712 | pure-sector invariance condition | $\mathsf C$ | source compatibility | relational | $\mathsf F$ | EXACT |
| C713 | Beltrami pure-invisible branch | $\mathsf C$ | exact periodic NS | targeted | $\mathsf F$ | CONSTRUCTED |
| C714 | Piola-defect escape dichotomy | $\mathsf C$ | stress ratio | targeted | $\mathsf F$ | EXACT |
| C715 | signed transfer ledger | $\mathsf C$ | spacetime budget | scalar | $\mathsf F$ | EXACT |
| C716 | universal visibility attractor | $\mathsf C$ | dynamic selection | targeted | $\mathsf F$ | REFUTED at first order |
| C717 | boundary-injection closure | $\mathsf C$ | coupled NS | targeted | $\mathsf F$ | OPEN / STOP-C49 |

---

# 29. Continuous-versus-discrete status

Although this round uses:

$$
W_L,
\qquad
W_T
$$

two orthogonal sectors,

they are continuous Hilbert-space subspaces,

not discrete substrate states.

The core dynamics use:

- continuous stress energies;
- continuous ratio:
  $$
  \eta\in[0,1];
  $$
- continuous PDE sources;
- continuous Riesz projection;
- continuous quartic probability measure.

The Beltrami periodic wave is merely an exact witness,

whose same geometry can be viewed as a continuous helical wave representation.

Therefore:

$$
\boxed{
T_{\mathsf C\to\mathsf D}
=
\text{NOT YET REACHED}.
}
$$

---

# 30. Strongest results of Round 45

## R45-A — exact Visibility Replicator Equation

$$
\boxed{
\eta'
=
2\eta(1-\eta)(f_L-f_T)
+
\frac{2\mathcal X}{E}.
}
$$

## R45-B — four-way selection decomposition

$$
\boxed{
\begin{aligned}
\eta'
={}&
2\eta(1-\eta)(s_L-s_T)
\\
&-
2\nu\eta(1-\eta)(d_L-d_T)
\\
&-
4\nu\eta(1-\eta)(g_L-g_T)
+
2\mathcal X/E.
\end{aligned}
}
$$

## R45-C — pure-invisible second-order injection

if:

$$
\eta(t_0)=0,
$$

then:

$$
\boxed{
\eta'(t_0)=0,
\qquad
\eta''(t_0)
=
\frac{
2\|
\mathbb P_L\mathcal R_\omega
+
[D_u,\mathbb P_L]W_T
\|_2^2
}{
E
}.
}
$$

## R45-D — exact pure-invisible NS branch

$$
\boxed{
u
=
Ae^{-\nu t}
(
\cos x_3,
-\sin x_3,
0
)
}
$$

satisfies:

$$
\boxed{
\eta_\omega(t)\equiv0.
}
$$

## R45-E — Piola-defect escape dichotomy

$$
\boxed{
\|\omega\|_4^4\to\infty,
\quad
\sup\|\mathfrak V_\omega\|_2<\infty
\Rightarrow
\eta_\omega\to0.
}
$$

## R45-F — no universal first-order visibility direction

Inviscid sign reversal flips both stretching selection and transfer while preserving $\eta$.

So static/inviscid geometry cannot choose a universal visible or invisible attractor.

---

# 31. Next round — Invisible-Escape Boundary Injection Depletion

Round 45 forces the hypothetical bounded-Piola-defect escape branch to:

$$
\boxed{
\eta_\omega\to0.
}
$$

But exact boundary dynamics show that for pure invisibility to persist,

it must suppress:

$$
\boxed{
F_L
=
\mathbb P_L
(
B_\omega^0-2\nu G_\omega^0
)
+
[D_u,\mathbb P_L]W_T.
}
$$

The next round will directly investigate:

1. whether the stretching, gradient, and transport terms of $F_L$ can mutually cancel;
2. why the Beltrami branch is exact:
   $$
   F_L=0;
   $$
3. the $F_L$ linearization of near-Beltrami / near-helical branches;
4. whether there exists a lower bound:
   $$
   \|F_L\|_2
   \gtrsim
   \text{distance from helical/invariant manifold};
   $$
5. how high-frequency actual triads inject visible stress;
6. if $\eta\to0$, whether it requires cumulative:
   $$
   \int
   \|F_L\|_2^2/E
   $$
   depletion;
7. if the injection cannot be kept small long-term, the bounded-Piola-defect escape branch is ruled out;
8. maintaining continuous helical / projection / stress dynamics throughout.

---

# 32. External primary-source anchors

1. Evan Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691.
   - Primary-source background for strain–vorticity interaction, advection depletion, and exact divergence-free identities.

2. Dhawal Buaria, Alain Pumir, *Non-local amplification of intense vorticity in turbulent flows*, arXiv:2106.14370.
   - DNS shows that intense vorticity amplification is highly correlated with nonlocal strain alignment, supporting this round's connection of total quartic stress fitness back to vorticity–strain alignment.

3. Jian-Zhou Zhu, *On the exact solutions of (magneto)hydrodynamic systems and the superposition principles of nonlinear helical waves*, arXiv:1407.8404.
   - Helical-wave background where circularly polarized homochiral Beltrami modes can eliminate generic nonlinear interactions; the Beltrami pure-invisible branch in this round is directly verified by this document itself.

4. Gennaro Ciampa, Renato Lucà, *Localization of Beltrami fields: global smooth solutions and vortex reconnection for the Navier-Stokes equations*, arXiv:2311.01369.
   - Modern primary-source background for Beltrami geometry in 3D Navier–Stokes global smooth constructions.

The Visibility Replicator Equation, sector-selection decomposition, pure-sector second-order injection laws, Beltrami visibility computation, and Piola-Defect Escape Dichotomy in this round are all directly derived in this document.

---

# 33. Commit state

$$
\boxed{
\begin{aligned}
\text{Route}
&=
\mathrm{Pure\ Continuous\ Visibility\ Replicator/Quartic\ Alignment\ Dynamics},
\\
\text{Essential }\mathsf C\to\mathsf D
&=
\mathrm{Not\ reached},
\\
\text{Visibility dynamics}
&=
\mathrm{selection}
+
\mathrm{conservative\ transfer},
\\
\text{Universal visibility direction}
&=
\mathrm{false},
\\
\text{Pure-sector first derivative}
&=
0,
\\
\text{Generic boundary injection}
&=
\mathrm{second\ order},
\\
\text{Pure invisible invariant branch}
&=
\mathrm{Beltrami\ exists},
\\
\text{Bounded Piola defect under quartic growth}
&\Rightarrow
\eta_\omega\to0,
\\
\text{Remaining obstruction}
&=
\mathrm{visible\ boundary\ injection\ compatibility},
\\
\text{STOP-C49}
&=
\mathrm{Visibility\ Replicator/Boundary\text{-}Injection\ Compatibility\ Gap},
\\
\text{Next}
&=
\mathrm{Invisible\text{-}Escape\ Boundary\ Injection\ Depletion}.
\end{aligned}
}
$$