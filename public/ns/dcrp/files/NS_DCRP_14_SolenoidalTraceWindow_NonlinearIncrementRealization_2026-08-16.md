# NS-DCRP-14 — Solenoidal Trace-Window Compiler, Nonlinear Supplier Increment, and the Final Trace-Realization Ledger

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: audit DCRP-13 against the actual finite-window adjoint-trace definition, correct the inadmissible scalar test shortcut, and build a genuine finite-dimensional divergence-free trace window for the supplier-generated nonlinear increment.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-02 filtered adjoint localization;
  - FCBP-05 combined observability;
  - FCBP-06 trace / CAR audit;
  - MORP-01 through MORP-05;
  - DCRP-08 through DCRP-13.
- external primary calibration:
  - Runlong Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756v1;
  - Cheskidov--Dai, arXiv:1507.06611v6;
  - Cheskidov--Shvydkoy, arXiv:1102.1944v2.

---

# 1. Executive result

DCRP-13 produced six scalar local traces

$$
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta(y)w_i(y)\,dy
$$

for the normalized supplier shell.

Those functionals are valid state diagnostics.

However they cannot be identified directly with the FCBP selected adjoint-trace channel.

The external finite-window trace space is:

$$
\boxed{
H_W
=
\text{finite-dimensional selected-time divergence-free trace correction space},
}
$$

localized in the observation ball and projected to the finite window.

The primal trace observation is:

$$
\boxed{
\mathcal O_W^T d
=
\Pi_W^T
\dot U(s_\ast).
}
\tag{1.1}
$$

Therefore the DCRP-13 claim

$$
\text{six scalar traces}
\Longrightarrow
O_W^T\ge c\nu
$$

was too fast.

There are two distinct issues.

First, the test field

$$
\eta e_i
$$

is not divergence free.

Second, the FCBP trace channel acts on the selected-time velocity component

$$
\dot U(s_\ast)
$$

of a cleaned defect direction, not on the full nonlinear supplier state

$$
u_Q(t_\ast)
$$

by arbitrary scalar pairing.

These points are corrected here.

The replacement argument uses the nonlinear supplier increment.

Let:

$$
q=Q(t_1),
\qquad
\lambda=\lambda_q,
$$

be a dissipation-boundary supplier shell.

Define:

$$
g_q(t)
=
u_q(t)
-
e^{\nu(t-t_0)\Delta}
u_q(t_0).
$$

Then:

$$
g_q(t_0)=0,
$$

and:

$$
\boxed{
\partial_tg_q
-
\nu\Delta g_q
+
\nabla\pi_q
=
-\nabla\cdot T_q,
}
\tag{1.2}
$$

where:

$$
T_q
=
\Delta_q(u\otimes u),
$$

and:

$$
\pi_q
=
\Delta_qp.
$$

Thus:

$$
g_q
$$

is the actual same-history nonlinear increment relative to linear heat memory.

Choose:

$$
t_0=t_1-\tau_q
$$

with:

$$
\tau_q
\sim
\frac{
\log(C\lambda^{1/2}K_0^{1/2}/\nu)
}{
\nu\lambda^2
}.
$$

Then the linear memory is small in

$$
L^\infty,
$$

while the dissipation-boundary supplier satisfies:

$$
\|u_q(t_1)\|_\infty
\gtrsim
\nu\lambda.
$$

Hence:

$$
\boxed{
\|g_q(t_1)\|_\infty
\ge
c\nu\lambda.
}
\tag{1.3}
$$

After critical rescaling and recentering at a point of near-maximal nonlinear-increment amplitude,

$$
\boxed{
h(y)
=
\lambda^{-1}
g_q
\left(
x_\ast+\lambda^{-1}y,
t_1
\right),
}
\tag{1.4}
$$

one has:

$$
\boxed{
\nabla\cdot h=0,
}
\tag{1.5}
$$

$$
\boxed{
\operatorname{supp}\widehat h
\subset
\mathcal A
}
\tag{1.6}
$$

for one fixed annulus

$$
\mathcal A,
$$

and:

$$
\boxed{
\|h\|_\infty
\ge
c\nu.
}
\tag{1.7}
$$

The main theorem of this round is:

> There exists one universal finite-dimensional subspace
>
> $$
> H_\ast
> \subset
> C_c^\infty(B_R;\mathbb R^3),
> $$
>
> consisting entirely of divergence-free vector fields, such that every normalized supplier nonlinear increment
>
> $$
> h
> $$
>
> satisfies:
>
> $$
> \boxed{
> \|\Pi_{H_\ast}h\|_{L^2(B_R)}
> \ge
> c_\ast\nu.
> }
> \tag{1.8}
> $$

The dimension of:

$$
H_\ast
$$

is universal and independent of:

- the supplier scale;
- the singular sequence;
- the number of work cells;
- the solution.

This fixes the trace-family admissibility problem.

The remaining gap is now exactly:

$$
\boxed{
\textbf{
Supplier Nonlinear-Increment / Cleaned-Defect Trace Realization}.
}
\tag{1.9}
$$

Namely, prove that the finite-window cleaned defect direction generated from the same actual return has selected-time component:

$$
\dot U(s_\ast)
$$

equal to the normalized nonlinear supplier increment up to an explicitly charged projection / localization / synchronization residual.

Once that is shown,

$$
\boxed{
\|\mathcal O_W^Td\|
\ge
c_\ast\nu
-
\mathcal E_{\rm tr-real}.
}
\tag{1.10}
$$

Thus exact trace invisibility requires:

$$
\mathcal E_{\rm tr-real}
\ge
c_\ast\nu.
$$

At that point the only escape is a positive native realization residual.

---

# 2. CORRECTION — DCRP-13 trace identification

The external finite-window trace channel is defined as follows.

A finite window is:

$$
W
=
(n,\ell,\Lambda,\chi,s_\ast).
$$

The trace correction space:

$$
H_W
$$

is finite dimensional.

Its elements are:

- divergence-free;
- selected-time vector fields;
- localized in the observation ball;
- projected to the finite active window.

The primal trace observation is:

$$
\boxed{
\mathcal O_W^Td
=
\Pi_W^T
\dot U(s_\ast).
}
\tag{2.1}
$$

The dual map:

$$
A_W^\ast
$$

is obtained from the backward **linearized coarse-grained Navier--Stokes adjoint**, not from the pure heat equation.

Therefore the following DCRP-13 statements must be corrected.

### Correction 1

The scalar terminal tests:

$$
\eta e_i
$$

are not themselves admissible trace corrections because:

$$
\nabla\cdot(\eta e_i)
=
\partial_i\eta
$$

is generally nonzero.

### Correction 2

A pure backward caloric propagation:

$$
e^{-\tau\Delta}\psi
$$

is not identical to the external:

$$
A_W^\ast
$$

adjoint, which contains linearized coarse transport and pressure coupling.

### Correction 3

The phrase:

$$
\boxed{
\text{CAR1 proved for the supplier-trace subgeometry}
}
$$

is too strong if it refers directly to the external FCBP trace channel.

The correct statement after DCRP-13 is:

$$
\boxed{
\text{a finite-dimensional scalar state witness exists}.
}
$$

DCRP-14 replaces it by an admissible solenoidal finite trace window.

Status:

$$
\boxed{
\textbf{CORRECTED}.
}
$$

---

# 3. The supplier shell and nonlinear memory subtraction

Let:

$$
q=Q(t_1)
$$

be a dissipation-boundary supplier shell.

By the dissipation-wavenumber boundary estimate:

$$
\boxed{
\|u_q(t_1)\|_\infty
\ge
c_0\nu\lambda_q.
}
\tag{3.1}
$$

Let:

$$
K_0
=
\|u(0)\|_2^2.
$$

For:

$$
t_0<t_1,
$$

the fixed shell mild formula is:

$$
u_q(t_1)
=
e^{\nu(t_1-t_0)\Delta}
u_q(t_0)
-
\int_{t_0}^{t_1}
e^{\nu(t_1-s)\Delta}
\mathbb P
\nabla\cdot
\Delta_q(u\otimes u)(s)
\,ds.
$$

Define:

$$
\boxed{
g_q(t_1)
=
u_q(t_1)
-
e^{\nu(t_1-t_0)\Delta}
u_q(t_0).
}
\tag{3.2}
$$

Then:

$$
\boxed{
g_q(t_1)
=
-
\int_{t_0}^{t_1}
e^{\nu(t_1-s)\Delta}
\mathbb P
\nabla\cdot
\Delta_q(u\otimes u)(s)
\,ds.
}
\tag{3.3}
$$

Thus:

$$
g_q
$$

is generated only by actual nonlinear forcing over:

$$
[t_0,t_1].
$$

---

# 4. Heat-memory $L^\infty$ bound

On the fixed dyadic annulus:

$$
|\xi|
\sim
\lambda_q,
$$

the heat semigroup gives:

$$
\left\|
e^{\nu\tau\Delta}
u_q
\right\|_2
\le
e^{-c_h\nu\lambda_q^2\tau}
\|u_q\|_2.
$$

Bernstein gives:

$$
\left\|
e^{\nu\tau\Delta}
u_q
\right\|_\infty
\le
C_B
\lambda_q^{3/2}
e^{-c_h\nu\lambda_q^2\tau}
\|u_q\|_2.
$$

By the energy inequality:

$$
\|u_q(t_0)\|_2
\le
K_0^{1/2}.
$$

Hence:

$$
\boxed{
\left\|
e^{\nu\tau\Delta}
u_q(t_0)
\right\|_\infty
\le
C_B
\lambda_q^{3/2}
K_0^{1/2}
e^{-c_h\nu\lambda_q^2\tau}.
}
\tag{4.1}
$$

Choose:

$$
\boxed{
\tau_q
=
\frac1{
c_h\nu\lambda_q^2
}
\log
\left(
\frac{
4C_B
\lambda_q^{1/2}
K_0^{1/2}
}{
c_0\nu
}
\right).
}
\tag{4.2}
$$

For sufficiently large:

$$
q,
$$

the logarithm is positive.

Then:

$$
\boxed{
\left\|
e^{\nu\tau_q\Delta}
u_q(t_0)
\right\|_\infty
\le
\frac{
c_0
}{
4
}
\nu\lambda_q.
}
\tag{4.3}
$$

---

# 5. NEW THEOREM — nonlinear supplier increment is critical and nonvanishing

## Theorem 5.1

Let:

$$
t_0=t_1-\tau_q
$$

with:

$$
\tau_q
$$

given by (4.2).

Then:

$$
\boxed{
\|g_q(t_1)\|_\infty
\ge
\frac{
3c_0
}{
4
}
\nu\lambda_q.
}
\tag{5.1}
$$

### Proof

By definition:

$$
g_q(t_1)
=
u_q(t_1)
-
e^{\nu\tau_q\Delta}
u_q(t_0).
$$

Therefore:

$$
\|g_q(t_1)\|_\infty
\ge
\|u_q(t_1)\|_\infty
-
\left\|
e^{\nu\tau_q\Delta}
u_q(t_0)
\right\|_\infty.
$$

Use (3.1) and (4.3).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Forced Stokes realization of the nonlinear increment

Define for:

$$
t\in[t_0,t_1]:
$$

$$
\boxed{
g_q(t)
=
u_q(t)
-
e^{\nu(t-t_0)\Delta}
u_q(t_0).
}
\tag{6.1}
$$

Then:

$$
g_q(t_0)=0.
$$

Apply:

$$
\Delta_q
$$

to the Navier--Stokes equation:

$$
\partial_tu_q
-
\nu\Delta u_q
+
\nabla p_q
=
-\nabla\cdot
\Delta_q(u\otimes u),
$$

where:

$$
p_q
=
\Delta_qp.
$$

The heat-memory term solves the homogeneous heat equation.

Therefore:

$$
\boxed{
\partial_tg_q
-
\nu\Delta g_q
+
\nabla p_q
=
-\nabla\cdot T_q,
}
\tag{6.2}
$$

with:

$$
\boxed{
T_q
=
\Delta_q(u\otimes u).
}
\tag{6.3}
$$

Also:

$$
\nabla\cdot g_q=0.
$$

Thus:

$$
\boxed{
(g_q,p_q,T_q)
}
$$

is an actual same-history forced Stokes package generated by the Navier--Stokes nonlinearity.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 7. Critical normalization

Choose:

$$
x_q
$$

such that:

$$
|g_q(x_q,t_1)|
\ge
\frac34
\|g_q(t_1)\|_\infty.
$$

Define:

$$
\boxed{
h_q(y)
=
\lambda_q^{-1}
g_q
\left(
x_q+\lambda_q^{-1}y,
t_1
\right).
}
\tag{7.1}
$$

Then:

$$
\boxed{
\|h_q\|_\infty
\ge
c_s\nu
}
\tag{7.2}
$$

for:

$$
c_s>0.
$$

Moreover:

$$
\boxed{
\nabla\cdot h_q=0,
}
\tag{7.3}
$$

and:

$$
\boxed{
\operatorname{supp}\widehat h_q
\subset
\mathcal A
}
\tag{7.4}
$$

for one universal compact annulus:

$$
\mathcal A
=
\{
\xi:
c_-\le|\xi|\le c_+
\}.
$$

---

# 8. Normalized supplier-increment class

Fix:

$$
a\in(0,1).
$$

Define:

$$
\boxed{
\mathscr K_{\mathcal A,a}
}
$$

to be the class of vector fields:

$$
f:\mathbb R^3\to\mathbb R^3
$$

satisfying:

$$
\boxed{
\nabla\cdot f=0,
}
\tag{8.1}
$$

$$
\boxed{
\operatorname{supp}\widehat f
\subset
\mathcal A,
}
\tag{8.2}
$$

$$
\boxed{
\|f\|_\infty
\le
1,
}
\tag{8.3}
$$

and:

$$
\boxed{
|f(0)|
\ge
a.
}
\tag{8.4}
$$

Every normalized supplier increment:

$$
h_q
$$

can be divided by its:

$$
L^\infty
$$

norm and placed in:

$$
\mathscr K_{\mathcal A,a}
$$

for a fixed universal:

$$
a>0.
$$

---

# 9. Local compactness of the normalized annulus class

Let:

$$
m\ge0.
$$

Because:

$$
f
$$

has Fourier support in:

$$
\mathcal A,
$$

choose one fixed smooth multiplier:

$$
\vartheta
$$

with:

$$
\vartheta\equiv1
$$

on:

$$
\mathcal A.
$$

Then:

$$
f
=
\check\vartheta*f.
$$

Hence for every multi-index:

$$
\alpha,
$$

$$
\partial^\alpha f
=
(\partial^\alpha\check\vartheta)*f.
$$

Therefore:

$$
\boxed{
\|\partial^\alpha f\|_\infty
\le
C_\alpha
\|f\|_\infty
\le
C_\alpha.
}
\tag{9.1}
$$

Thus:

$$
\mathscr K_{\mathcal A,a}
$$

is uniformly bounded in:

$$
C^m(B_R)
$$

for every fixed:

$$
m,R.
$$

Arzela--Ascoli gives:

$$
\boxed{
\mathscr K_{\mathcal A,a}
\text{ is precompact in }
C^\infty_{\rm loc}.
}
\tag{9.2}
$$

Its closure retains:

$$
|f(0)|\ge a.
$$

---

# 10. Local solenoidal test space

Fix any:

$$
R>0.
$$

Let:

$$
\boxed{
V_R
=
\overline{
\{
\psi\in C_c^\infty(B_R;\mathbb R^3):
\nabla\cdot\psi=0
\}
}^{L^2(B_R)}.
}
\tag{10.1}
$$

Let:

$$
P_R
$$

denote the:

$$
L^2(B_R)
$$

orthogonal projection onto:

$$
V_R.
$$

The central question is whether:

$$
P_Rf
$$

can vanish for:

$$
f\in\mathscr K_{\mathcal A,a}.
$$

---

# 11. NEW THEOREM — local solenoidal nondegeneracy

## Theorem 11.1

For every:

$$
R>0,
$$

$$
\boxed{
\delta_R
:=
\inf_{
f\in\mathscr K_{\mathcal A,a}
}
\|P_Rf\|_{L^2(B_R)}
>
0.
}
\tag{11.1}
$$

### Proof

Assume the contrary.

Then there exists:

$$
f_n\in\mathscr K_{\mathcal A,a}
$$

with:

$$
\|P_Rf_n\|_{L^2(B_R)}
\to0.
$$

By local compactness, after a subsequence:

$$
f_n
\to
f_\ast
$$

strongly in:

$$
C^\infty(B_R).
$$

Therefore:

$$
\boxed{
|f_\ast(0)|
\ge
a>0.
}
\tag{11.2}
$$

Also:

$$
P_Rf_\ast=0.
$$

Hence:

$$
f_\ast
$$

is orthogonal in:

$$
B_R
$$

to every compactly supported divergence-free test field.

For every:

$$
\Phi\in C_c^\infty(B_R;\mathbb R^3),
$$

the field:

$$
\nabla\times\Phi
$$

is divergence free and compactly supported.

Thus:

$$
0
=
\int_{B_R}
f_\ast\cdot
(\nabla\times\Phi)
\,dx
=
\int_{B_R}
(\nabla\times f_\ast)
\cdot\Phi
\,dx.
$$

Therefore:

$$
\boxed{
\nabla\times f_\ast=0
}
\tag{11.3}
$$

in:

$$
B_R.
$$

But:

$$
\nabla\cdot f_\ast=0.
$$

Hence:

$$
\boxed{
\Delta f_\ast=0
}
\tag{11.4}
$$

in:

$$
B_R.
$$

Because:

$$
f_\ast
$$

is band limited, it is real analytic.

Thus:

$$
\Delta f_\ast=0
$$

on one nonempty open ball implies:

$$
\boxed{
\Delta f_\ast=0
}
\tag{11.5}
$$

globally.

Taking Fourier transforms:

$$
|\xi|^2
\widehat f_\ast(\xi)
=
0.
$$

But:

$$
\operatorname{supp}\widehat f_\ast
\subset
\mathcal A,
$$

and:

$$
0\notin\mathcal A.
$$

Therefore:

$$
\widehat f_\ast=0,
$$

so:

$$
f_\ast=0.
$$

This contradicts (11.2).

Therefore:

$$
\delta_R>0.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. Finite-dimensional compression of the solenoidal trace space

Choose a countable dense family:

$$
\{
\psi_1,\psi_2,\ldots
\}
\subset
C_c^\infty(B_R;\mathbb R^3)
$$

with:

$$
\nabla\cdot\psi_j=0,
$$

dense in:

$$
V_R.
$$

Let:

$$
\boxed{
H_N
=
\operatorname{span}
\{
\psi_1,\ldots,\psi_N
\}.
}
\tag{12.1}
$$

Let:

$$
P_N
$$

be the:

$$
L^2(B_R)
$$

orthogonal projection onto:

$$
H_N.
$$

Then:

$$
P_N
\to
P_R
$$

strongly on:

$$
L^2(B_R).
$$

Because the closure of:

$$
\mathscr K_{\mathcal A,a}
$$

is compact in:

$$
L^2(B_R),
$$

the convergence is uniform on:

$$
\mathscr K_{\mathcal A,a}.
$$

Therefore for some finite:

$$
N_\ast,
$$

$$
\boxed{
\sup_{
f\in\mathscr K_{\mathcal A,a}
}
\|
(P_R-P_{N_\ast})f
\|_{L^2(B_R)}
<
\frac{
\delta_R
}{
2
}.
}
\tag{12.2}
$$

Hence:

$$
\boxed{
\inf_{
f\in\mathscr K_{\mathcal A,a}
}
\|
P_{N_\ast}f
\|_{L^2(B_R)}
\ge
\frac{
\delta_R
}{
2
}.
}
\tag{12.3}
$$

---

# 13. NEW THEOREM — universal finite-dimensional solenoidal supplier trace window

Define:

$$
\boxed{
H_\ast
=
H_{N_\ast}.
}
\tag{13.1}
$$

## Theorem 13.1

There exist universal:

$$
R<\infty,
$$

$$
N_\ast<\infty,
$$

and:

$$
c_\ast>0
$$

such that every normalized supplier nonlinear increment:

$$
h_q
$$

satisfies:

$$
\boxed{
\|
\Pi_{H_\ast}
h_q
\|_{L^2(B_R)}
\ge
c_\ast\nu.
}
\tag{13.2}
$$

The space:

$$
H_\ast
$$

consists of compactly supported divergence-free vector fields.

### Proof

Let:

$$
M_q
=
\|h_q\|_\infty.
$$

By Theorem 5.1 / Section 7:

$$
M_q
\ge
c_s\nu.
$$

Define:

$$
f_q
=
M_q^{-1}h_q.
$$

After recentering:

$$
f_q\in
\mathscr K_{\mathcal A,a}.
$$

Therefore:

$$
\|
\Pi_{H_\ast}
f_q
\|_2
\ge
\delta_R/2.
$$

Multiply by:

$$
M_q.
$$

Then:

$$
\|
\Pi_{H_\ast}
h_q
\|_2
\ge
\frac{
\delta_Rc_s
}{
2
}
\nu.
$$

Set:

$$
c_\ast
=
\delta_Rc_s/2.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. Why this trace window matches the FCBP type

The external finite-window definition allows:

$$
\Lambda
$$

to be a finite-dimensional space of:

- localized test functions;
- wave packets;
- Stokes eigenfunctions;
- localized Fourier packets;
- adjoint test modes.

The selected-time correction space:

$$
H_W
$$

must be finite dimensional, divergence free, and localized in the observation ball.

The space:

$$
H_\ast
$$

constructed above satisfies exactly these structural requirements.

Therefore:

$$
\boxed{
\textbf{
trace-family admissibility is solved.
}
}
\tag{14.1}
$$

No new detector architecture is needed.

What remains is the identity of the **observed object**.

---

# 15. The observed object mismatch

The external primal trace map is:

$$
\mathcal O_W^Td
=
\Pi_W^T
\dot U(s_\ast).
$$

Theorem 13.1 controls:

$$
\Pi_{H_\ast}
h_q,
$$

where:

$$
h_q
$$

is the normalized nonlinear supplier increment.

Thus to obtain:

$$
\mathcal O_W^T d
\ne0,
$$

one needs:

$$
\boxed{
\dot U(s_\ast)
=
h_q
+
e_{\rm tr}
}
\tag{15.1}
$$

inside the selected trace window, with controlled:

$$
e_{\rm tr}.
$$

Define the trace-realization error:

$$
\boxed{
\mathcal E_{\rm tr-real}
=
\|
\Pi_{H_\ast}
e_{\rm tr}
\|_{L^2(B_R)}.
}
\tag{15.2}
$$

Then:

$$
\boxed{
\|
\mathcal O_W^Td
\|
\ge
c_\ast\nu
-
\mathcal E_{\rm tr-real}.
}
\tag{15.3}
$$

Status:

$$
\boxed{
\textbf{PROVED by triangle inequality once (15.1) is established}.
}
$$

---

# 16. Exact trace-realization alternative

Equation (15.3) gives the following elementary but important alternative.

For every supplier nonlinear increment:

$$
\boxed{
\|\mathcal O_W^Td\|
\ge
\frac{
c_\ast
}{
2
}
\nu
}
\tag{16.1}
$$

or:

$$
\boxed{
\mathcal E_{\rm tr-real}
\ge
\frac{
c_\ast
}{
2
}
\nu.
}
\tag{16.2}
$$

Thus:

$$
\boxed{
\textbf{
supplier nonlinear increment}
\Longrightarrow
\textbf{
trace visibility}
\ \vee\
\textbf{
positive trace-realization residual}.
}
}
\tag{16.3}
$$

This is now exactly the kind of alternative MORP is designed to retain.

The missing theorem is to prove that:

$$
\mathcal E_{\rm tr-real}
$$

belongs to the existing:

$$
\mathsf R_{\rm nat}
$$

or another already-paid localization / projection / synchronization ledger.

---

# 17. Relation to the forced Stokes package

The nonlinear supplier increment satisfies:

$$
\partial_tg_q
-
\nu\Delta g_q
+
\nabla p_q
=
-\nabla\cdot T_q.
$$

This is a linear forced Stokes evolution with actual Navier--Stokes-generated source:

$$
T_q
=
\Delta_q(u\otimes u).
$$

Hence the selected-time trace:

$$
g_q(t_1)
$$

is not a fabricated direction.

It belongs to an actual PDE-generated linear forced package.

This makes the following realization program natural:

1. use the normalized:

   $$
   g_q
   $$

   as the velocity direction:

   $$
   \dot U;
   $$

2. use the normalized:

   $$
   T_q
   $$

   as the source / residual direction:

   $$
   \dot R;
   $$

3. use:

   $$
   p_q
   $$

   as the corresponding pressure direction;

4. localize / project / clean this forced Stokes package into the finite-window constrained space.

Every mismatch generated by:

- finite-window projection;
- localization;
- coarse baseline coupling;
- active/harmonic pressure cleaning;
- synchronization;

must then appear explicitly in the finite-window residual ledger.

This is the concrete form of the next theorem.

---

# 18. Why the pure heat adjoint is no longer needed

DCRP-13 used a pure backward heat test.

The actual FCBP dual trace:

$$
A_W^\ast
$$

solves a backward **linearized coarse Navier--Stokes** equation.

DCRP-14 avoids this mismatch.

The trace lower bound is now stated on the primal selected-time space:

$$
H_\ast.
$$

One only needs:

$$
\Pi_W^T
\dot U(s_\ast),
$$

which is exactly the external primal trace definition.

The backward adjoint may then be used internally by the finite-window anti-phantom theorem in its own correct form.

Thus no direct identification:

$$
e^{-\tau\Delta}
=
A_W^\ast
$$

is required.

---

# 19. Relation to MORP-02 selected-time traces

MORP-02 already treats selected-time native carriers as a separate extraction route.

It proves strong trace compactness under:

- fixed relative frequency support;
- a global trace:

  $$
  L^2
  $$

  bound;
- spatial tightness.

The DCRP-14 theorem is complementary.

It does not require a global trace bound or spatial tightness.

Instead it produces a fixed finite-dimensional **local solenoidal projection** with uniform lower bound.

Thus:

$$
\boxed{
\text{supplier trace does not need full global trace compactness
merely to remain locally observable}.
}
$$

This removes one source of unnecessary compactness debt.

---

# 20. Why finite dimensionality is genuinely uniform

The dimension:

$$
N_\ast
$$

depends only on:

- the fixed annulus:

  $$
  \mathcal A;
  $$

- the fixed local radius:

  $$
  R;
  $$

- the fixed normalized point-amplitude fraction:

  $$
  a.
  $$

It does not depend on:

$$
q.
$$

Therefore:

$$
\boxed{
N_\ast
=
O(1)
}
\tag{20.1}
$$

along the entire hypothetical singular cascade.

This avoids the moving-window dimension blowup that plagued earlier abstract finite-window CAR attempts.

---

# 21. Why the unique-continuation step is essential

The compactness theorem alone would only give a limiting band-limited field.

The key fact is:

$$
\boxed{
\text{no nonzero annulus-band-limited divergence-free field
can be locally orthogonal to every compactly supported divergence-free test}.
}
$$

If it were orthogonal to all such tests:

$$
\nabla\times f=0
$$

locally.

Together with:

$$
\nabla\cdot f=0,
$$

this gives:

$$
\Delta f=0
$$

locally.

Band-limited analyticity propagates that identity globally.

But a globally harmonic field with Fourier support away from zero must vanish.

This is precisely what gives a positive uniform solenoidal distance.

---

# 22. A possible shortcut through finite-window projection

The external finite-window framework allows:

$$
\Lambda
$$

to be a chosen finite-dimensional localized Fourier / wave-packet window.

Therefore one may choose:

$$
\Lambda_\ast
$$

so that its selected-time velocity subspace contains:

$$
H_\ast.
$$

Then:

$$
\Pi_W^T
$$

may be chosen to dominate:

$$
\Pi_{H_\ast}.
$$

Under an exact supplier-increment realization:

$$
\dot U(s_\ast)=h_q,
$$

one would immediately obtain:

$$
\boxed{
\|
\mathcal O_W^Td
\|
\ge
c_\ast\nu.
}
\tag{22.1}
$$

Thus:

$$
\boxed{
\textbf{
the trace-window geometry itself is no longer the missing step.
}
}
$$

Only realization/cleaning remains.

---

# 23. Concrete next theorem — Supplier Increment Realization

The next exact target is:

$$
\boxed{
\textbf{
Supplier Increment / Finite-Window Defect Realization Lemma}.
}
$$

Desired statement:

Let:

$$
g_q
$$

be the DCRP-14 nonlinear supplier increment on:

$$
[t_0,t_1].
$$

Normalize at:

$$
\lambda_q
$$

and re-center at:

$$
x_q.
$$

Then there exists an admissible finite-window cleaned defect direction:

$$
d_q
=
[
\dot U_q,
\dot P_q;
\dot P_q^{act},
\dot P_q^{har},
\dot R_q,
\dot\Pi_q
]
\in
Y_{W_q}
$$

such that at the selected terminal time:

$$
\boxed{
\dot U_q(s_\ast)
=
h_q
+
e_q,
}
\tag{23.1}
$$

and:

$$
\boxed{
\|
\Pi_{H_\ast}e_q
\|_2
\le
\mathcal E_q^{\rm proj}
+
\mathcal E_q^{\rm loc}
+
\mathcal E_q^{\rm press}
+
\mathcal E_q^{\rm sync}.
}
\tag{23.2}
$$

Every error on the right must be one of the already declared finite-window residual-ledger channels.

Then:

$$
\boxed{
\|
\mathcal O_{W_q}^T
d_q
\|
+
\mathcal E_q^{\rm ledger}
\ge
c_\ast\nu.
}
\tag{23.3}
$$

If the residual ledger tends to zero, the trace channel has a uniform positive lower bound.

If the trace channel tends to zero, the residual ledger has a uniform positive lower bound.

Either alternative is incompatible with exact combined invisibility plus zero native residual.

---

# 24. What this would and would not prove

If the Supplier Increment Realization Lemma is proved, it would establish:

$$
\boxed{
\text{supplier mechanism}
\not\subset
\{
O_W^T=0,
\mathsf R_{\rm nat}=0
\}.
}
$$

It would **not yet** prove global Navier--Stokes regularity.

One still has to verify that:

1. every hypothetical singular branch entering the MORP minimal-return normal form must carry the supplier-increment package through the same return object;

2. the positive trace / residual event produces enough depletion or exclusion in the minimal-obstruction geometry;

3. the remaining defect-only branch cannot detach from the supplier mechanism.

Thus the present result closes one concrete CAR / trace realization interface, not the Clay problem.

---

# 25. Source ledger

## External finite-window trace definition

Runlong Yu, *Invisible Defect Cascades for Navier--Stokes Regularity*, arXiv:2606.12756v1.

Relevant definitions:

- finite observation window:

  $$
  W=(n,\ell,\Lambda,\chi,s_\ast);
  $$

- trace correction space:

  $$
  H_W;
  $$

- $H_W$ consists of divergence-free selected-time fields localized in the observation ball and projected to the finite window;

- primal trace observation:

  $$
  \mathcal O_W^Td
  =
  \Pi_W^T\dot U(s_\ast);
  $$

- the window:

  $$
  \Lambda
  $$

  may be a finite-dimensional space of localized test functions, wave packets, Stokes eigenfunctions, localized Fourier packets, or adjoint test modes;

- the dual map:

  $$
  A_W^\ast
  $$

  is generated by the backward adjoint **linearized coarse-grained Navier--Stokes equation**.

These facts are the reason DCRP-13 required correction and DCRP-14 uses a primal solenoidal trace window.

## Cheskidov--Dai / Cheskidov--Shvydkoy

Used for:

$$
\|u_Q\|_\infty
\gtrsim
\nu\lambda_Q.
$$

This is the starting amplitude that survives nonlinear memory subtraction.

---

# 26. End state

DCRP-13's scalar six-test shortcut has been corrected.

The correct statement is stronger in the relevant sense.

The actual nonlinear supplier increment satisfies:

$$
\boxed{
\|g_q(t_1)\|_\infty
\gtrsim
\nu\lambda_q.
}
$$

After critical re-scaling:

$$
\boxed{
h_q
=
\lambda_q^{-1}
g_q
}
$$

is:

- divergence free;
- supported in one fixed Fourier annulus;
- generated by actual same-history NS forcing;
- nonvanishing at fixed normalized amplitude.

There exists one universal finite-dimensional solenoidal trace window:

$$
\boxed{
H_\ast
\subset
C_c^\infty(B_R;\mathbb R^3),
\qquad
\dim H_\ast=N_\ast<\infty,
}
$$

such that:

$$
\boxed{
\|\Pi_{H_\ast}h_q\|_2
\ge
c_\ast\nu.
}
$$

Therefore the trace-family / detector-space geometry is no longer open.

The single remaining bridge is:

$$
\boxed{
\textbf{
actual nonlinear supplier increment}
\Longrightarrow
\textbf{
cleaned finite-window defect selected-time component}
}
$$

up to already-paid projection / localization / pressure / synchronization residuals.

The next exact target is:

$$
\boxed{
\textbf{
Supplier Increment / Finite-Window Defect Realization Lemma}.
}
$$

That is now the next attack.
