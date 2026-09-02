# NS-DCRP-22 — Supplier-to-Filtered-Enstrophy Activation, Temporal-Spike Elimination, and a Poincaré Correction to the Local Reservoir Branch

- date: 2026-08-17
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. connect the DCRP-16 local supplier atom to the filtered-vorticity mechanism of DCRP-20/21;
  2. eliminate the proposed "ultrashort temporal spike" escape;
  3. correct the DCRP-20 treatment of the compactly localized filtered-enstrophy reservoir;
  4. reduce supplier activation to explicit diffusion / commutator / localization / far-field spatial-escape channels.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - Runlong Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- supporting primary source:
  - Cheskidov--Dai, *Regularity Criteria for the 3D Navier-Stokes and MHD Equations*, arXiv:1507.06611v6.
- internal dependencies:
  - DCRP-16 Local Supplier Capture;
  - DCRP-20 filtered mechanism reduction;
  - DCRP-21 far-field annular spatial-escape theorem.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-21 left the interface:

$$
\boxed{
\textbf{
Local Supplier}
\Longrightarrow
\textbf{
Filtered-Enstrophy Activation}
\ \vee\
\textbf{
temporal/paid defect}.
}
}
\tag{1.1}
$$

This round closes that interface at the level of a quantitative alternative.

The argument has three modules.

## Module A — supplier velocity forces local supplier vorticity

DCRP-16 produces, near every first singular point,

$$
t_n\uparrow T,
\qquad
x_n\to x_\ast,
\qquad
r_n=\lambda_n^{-1}\downarrow0,
$$

with a localized dissipation-boundary shell satisfying

$$
\boxed{
r_n
\|
(v_n)_{q_n}(t_n)
\|_\infty
\ge
c_{\rm sup}\nu.
}
\tag{1.2}
$$

After normalizing at its own global shell maximum, the field belongs to a fixed annulus-bandlimited divergence-free class.

A compactness/analyticity argument gives a uniform local curl lower bound.

Consequently, after transferring from the good-collar localization back to the original field,

$$
\boxed{
r_n
\int_{
B_{Rr_n}(x_n)
}
|
\omega_{q_n}(x,t_n)
|^2dx
\ge
c_\omega\nu^2.
}
\tag{1.3}
$$

Thus the local supplier is also a critical local vorticity-shell atom.

## Module B — two fixed mollifier scales force a full filtered-vorticity endpoint atom or a localization defect

Choose one fixed radial nonnegative compactly supported mollifier

$$
\varphi,
\qquad
\int\varphi=1.
$$

There exist fixed constants

$$
0<a<b\ll1
$$

such that the Fourier multiplier difference

$$
\boxed{
m_{a,b}(\zeta)
=
\widehat\varphi(a\zeta)
-
\widehat\varphi(b\zeta)
}
\tag{1.4}
$$

is bounded away from zero on the fixed supplier annulus:

$$
\boxed{
|m_{a,b}(\zeta)|
\ge
d_\varphi>0
\qquad
(\zeta\in\mathcal A).
}
\tag{1.5}
$$

Let

$$
\Omega_{a,n}
=
\nabla\times
S_{ar_n}u,
$$

$$
\Omega_{b,n}
=
\nabla\times
S_{br_n}u,
$$

and

$$
G_n
=
\Omega_{a,n}
-
\Omega_{b,n}.
$$

The supplier shell lower bound implies

$$
\boxed{
r_n
\|
\eta_n
\Delta_{q_n}G_n(t_n)
\|_2^2
\ge
c_G\nu^2
}
\tag{1.6}
$$

for a fixed normalized cutoff

$$
\eta_n.
$$

Using

$$
\eta_n\Delta_qG
=
\Delta_q(\eta_nG)
-
[
\Delta_q,\eta_n
]G,
$$

one obtains the exact alternative:

$$
\boxed{
r_n
\|
\eta_nG_n(t_n)
\|_2^2
\ge
c_1\nu^2
}
\tag{1.7}
$$

or:

$$
\boxed{
\mathcal C_n^{spec}
:=
r_n
\|
[
\Delta_{q_n},\eta_n
]
G_n(t_n)
\|_2^2
\ge
c_2\nu^2.
}
\tag{1.8}
$$

If (1.7) holds, then by the triangle inequality at least one of the two **full filtered vorticities** satisfies:

$$
\boxed{
r_n
\|
\eta_n
\Omega_{\sigma_n,n}(t_n)
\|_2^2
\ge
e_0\nu^2,
\qquad
\sigma_n\in\{a,b\}.
}
\tag{1.9}
$$

Hence:

$$
\boxed{
\textbf{
supplier endpoint}
\Longrightarrow
\textbf{
full filtered-vorticity endpoint atom}
\ \vee\
\textbf{
spectral-localization defect}.
}
}
\tag{1.10}
$$

The detector family contains only two filter ratios.

No scale-dependent detector dimension is introduced.

## Module C — a temporal spike cannot avoid the filtered-enstrophy ledger

Assume the endpoint filtered atom (1.9).

Fix a normalized backward time length

$$
\tau_0>0.
$$

Let

$$
J_n
=
(
t_n-\tau_0r_n^2,
t_n
).
$$

Define:

$$
\boxed{
\mathcal O_n
=
r_n^{-1}
\int_{J_n}
\int
\eta_n^2
|
\Omega_{\sigma_n,n}
|^2dxdt.
}
\tag{1.11}
$$

There are two cases.

### Reservoir branch

If:

$$
\mathcal O_n
\ge
o_0>0,
$$

then a local Poincaré inequality gives:

$$
\boxed{
\mathcal O_n
\le
C_\eta
\left(
\nu^{-1}\mathcal P_n
+
\mathcal L_n^\omega
\right).
}
\tag{1.12}
$$

Therefore a fixed reservoir immediately forces fixed filtered diffusion or cutoff-shell cost.

### Temporal-spike branch

If:

$$
\mathcal O_n
<
o_0
$$

with:

$$
o_0
$$

chosen sufficiently small relative to the endpoint atom and:

$$
\tau_0,
$$

then there exists:

$$
s_n\in J_n
$$

with small initial filtered enstrophy:

$$
\boxed{
\mathcal E_n^\omega(s_n)
\le
\frac14
e_0\nu^2.
}
\tag{1.13}
$$

while:

$$
\boxed{
\mathcal E_n^\omega(t_n)
\ge
e_0\nu^2.
}
\tag{1.14}
$$

The exact localized filtered-enstrophy identity therefore forces a fixed positive mechanism payment.

After inserting the external near-field stretching coercivity and derivative-compatible commutator estimate, one obtains:

$$
\boxed{
c_{\rm act}\nu^2
\le
C(M)
\mathcal O_n
+
\mathcal V_n^{+,\mathrm{far}}
+
C
\widetilde{\mathcal S}_n^{(3)}
+
\mathcal L_n
+
\mathcal L_n^{\mathrm{com}}.
}
\tag{1.15}
$$

Thus an ultrashort supplier spike does not evade the spacetime ledger.

It forces a fixed positive:

- far-field strain event;
- derivative-compatible commutator defect;
- or localization residual.

Combining Modules A--C:

$$
\boxed{
\begin{aligned}
\textbf{local supplier}
\Longrightarrow\quad
&
\mathcal C^{spec}\ge c\\
&\vee\
\mathcal P+\mathcal L^\omega\ge c\\
&\vee\
\mathcal V^{far}\ge c\\
&\vee\
\widetilde{\mathcal S}^{(3)}\ge c\\
&\vee\
\mathcal L+\mathcal L^{com}\ge c.
\end{aligned}
}
\tag{1.16}
$$

All constants are scale uniform after fixing:

- the normalized supplier annulus;
- the two relative filter ratios;
- the local-energy bound;
- the normalized cutoff family.

The remaining far-field branch is handled by DCRP-21:

if the local reservoir tends to zero and far-field work remains positive, the annular source must escape to normalized spatial infinity with diverging amplitude.

Therefore a transition-complete zero-cost package satisfying:

- zero filtered diffusion;
- zero spectral/localization defect;
- zero derivative-compatible increment defect;
- zero spatial-source escape;

cannot contain the local supplier sequence.

This eliminates the "supplier exists only as an ultrashort invisible spike" loophole.

---

# 2. CORRECTION — the DCRP-20 local IR reservoir branch is unnecessary

DCRP-20 defined:

$$
f_{r,\ell}
=
\eta_r\Omega_\ell
$$

with:

$$
\eta_r
$$

compactly supported in a fixed normalized ball.

It then introduced a relative-frequency measure and concluded:

$$
\boxed{
O^\eta>0,
\quad
P^\eta\to0,
\quad
L^\omega\to0
\Longrightarrow
\text{relative IR concentration}.
}
\tag{2.1}
$$

The second-moment inequality itself is correct.

However, because:

$$
f_{r,\ell}
$$

has compact support of radius:

$$
O(r),
$$

one has an ordinary Poincaré inequality.

This yields a strictly stronger conclusion.

---

# 3. NEW THEOREM — Compact Local Reservoir Poincaré Bound

## Theorem 3.1

Let:

$$
f
=
\eta_r\Omega_\ell
$$

with:

$$
\eta_r
$$

supported in:

$$
B_{Cr}(x_0).
$$

Then:

$$
\boxed{
\mathcal O_{r,\ell}^{\eta}
\le
C_{\eta}
\left(
\nu^{-1}
\mathcal P_{r,\ell}^{\eta}
+
\mathcal L_{r,\ell}^{\omega}
\right).
}
\tag{3.1}
$$

### Proof

For every fixed time, because:

$$
f
\in
H_0^1
(
B_{Cr}
),
$$

Poincaré gives:

$$
\|f\|_2^2
\le
C_\eta
r^2
\|
\nabla f
\|_2^2.
$$

But:

$$
\nabla f
=
\eta_r
\nabla\Omega_\ell
+
(
\nabla\eta_r
)
\otimes
\Omega_\ell.
$$

Hence:

$$
\|
\nabla f
\|_2^2
\le
2
\int
\eta_r^2
|
\nabla\Omega_\ell
|^2
+
C_\eta
r^{-2}
\int_{
\supp\nabla\eta_r
}
|
\Omega_\ell
|^2.
$$

Integrate in time and multiply by:

$$
r^{-1}.
$$

The first term becomes:

$$
C_\eta
\nu^{-1}
\mathcal P_{r,\ell}^{\eta},
$$

and the second becomes:

$$
C_\eta
\mathcal L_{r,\ell}^{\omega}.
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

# 4. Consequence for DCRP-20

For the compactly localized reservoir:

$$
\boxed{
\mathcal P_n^\eta\to0,
\qquad
\mathcal L_n^\omega\to0
\Longrightarrow
\mathcal O_n^\eta\to0
}
\tag{4.1}
$$

**without any no-IR assumption**.

Therefore DCRP-20's infrared alternative should be read only as a Fourier concentration description that would necessarily be accompanied by a nonvanishing cutoff-gradient/diffusion cost in the fixed compact local geometry.

The two-sided infrared completion of DCRP-18 remains necessary for:

- global carriers;
- scale-re-rooted old suppliers;
- noncompact transition packages.

It is not needed to eliminate the compact localized filtered-enstrophy reservoir.

Status:

$$
\boxed{
\textbf{CORRECTION / STRENGTHENING}.
}
$$

---

# 5. Strengthening of DCRP-20/21

The DCRP-20 zero-cost reservoir conclusion improves from:

$$
\boxed{
P\to0
+
L^\omega\to0
+
\text{no IR}
\Longrightarrow
O\to0
}
$$

to:

$$
\boxed{
P\to0
+
L^\omega\to0
\Longrightarrow
O\to0.
}
\tag{5.1}
$$

Accordingly, the DCRP-21 far-field-only survivor reduction no longer requires a separate no-IR hypothesis for the compact core reservoir.

The only remaining scale/spatial noncompactness in that argument is the **far-field source** itself.

---

# 6. Local supplier sequence from DCRP-16

Fix a first singular point:

$$
(x_\ast,T).
$$

DCRP-16 constructs good-collar localized divergence-free fields:

$$
v_n
$$

and localized boundary shells:

$$
q_n
$$

with:

$$
r_n
=
\lambda_{q_n}^{-1},
$$

such that:

$$
t_n\uparrow T,
$$

the shell maximum point:

$$
x_n\to x_\ast,
$$

and:

$$
\boxed{
r_n
\|
(v_n)_{q_n}(t_n)
\|_\infty
\ge
a_0\nu.
}
\tag{6.1}
$$

Moreover:

$$
r_n/\rho_n
\to0
$$

arbitrarily fast after increasing the supplier threshold inside each good collar.

The original shell:

$$
u_{q_n}
$$

agrees with:

$$
(v_n)_{q_n}
$$

near:

$$
x_n
$$

up to rapidly decaying high-frequency localization errors.

---

# 7. Normalized supplier class

Set:

$$
A_n
=
r_n
\|
(v_n)_{q_n}(t_n)
\|_\infty.
$$

Then:

$$
\boxed{
A_n\ge a_0\nu.
}
\tag{7.1}
$$

Choose:

$$
x_n
$$

with:

$$
\boxed{
r_n
|
(v_n)_{q_n}(x_n,t_n)
|
\ge
\frac34
A_n.
}
\tag{7.2}
$$

Define:

$$
\boxed{
W_n(y)
=
A_n^{-1}
r_n
(v_n)_{q_n}
(
x_n+r_ny,t_n
).
}
\tag{7.3}
$$

Then:

$$
\boxed{
\|W_n\|_\infty=1,
}
\tag{7.4}
$$

$$
\boxed{
|W_n(0)|
\ge
\frac34,
}
\tag{7.5}
$$

$$
\boxed{
\nabla\cdot W_n=0,
}
\tag{7.6}
$$

and:

$$
\boxed{
\supp
\widehat W_n
\subset
\mathcal A
}
\tag{7.7}
$$

for one fixed compact annulus:

$$
0<c_-\le|\xi|\le c_+.
$$

Bernstein gives uniform:

$$
C^m
$$

bounds for every:

$$
m.
$$

---

# 8. NEW THEOREM — Supplier Curl Atom

## Theorem 8.1

There exist universal:

$$
R_\omega<\infty,
$$

and:

$$
c_\omega>0
$$

such that every normalized supplier:

$$
W_n
$$

satisfies:

$$
\boxed{
\int_{
B_{R_\omega}
}
|
\nabla\times W_n
|^2dy
\ge
c_\omega.
}
\tag{8.1}
$$

### Proof

Assume the contrary.

Then there exists a sequence:

$$
W_n
$$

in the normalized supplier class with:

$$
\|
\nabla\times W_n
\|_{
L^2(B_{R_\omega})
}
\to0.
$$

By Bernstein and Arzela--Ascoli, after a subsequence:

$$
W_n
\to
W_\ast
$$

in:

$$
C^\infty_{\rm loc}.
$$

Then:

$$
|W_\ast(0)|
\ge
3/4,
$$

while:

$$
\nabla\times W_\ast=0
$$

on a nonempty ball.

Also:

$$
\nabla\cdot W_\ast=0.
$$

Therefore:

$$
\Delta W_\ast=0
$$

on that ball.

Because:

$$
W_\ast
$$

is band limited, it is real analytic.

Hence:

$$
\Delta W_\ast=0
$$

globally.

Taking Fourier transforms:

$$
|\xi|^2
\widehat W_\ast(\xi)
=
0.
$$

But the Fourier support lies in an annulus disjoint from:

$$
\xi=0.
$$

Therefore:

$$
W_\ast=0,
$$

contradicting:

$$
|W_\ast(0)|\ge3/4.
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

# 9. Physical supplier-vorticity lower bound

Undoing the normalization:

$$
\nabla_y\times
\left[
r_n
(v_n)_{q_n}
(
x_n+r_ny,t_n
)
\right]
=
r_n^2
\nabla_x\times
(v_n)_{q_n}.
$$

Therefore Theorem 8.1 gives:

$$
\boxed{
r_n
\int_{
B_{R_\omega r_n}(x_n)
}
|
\nabla\times
(v_n)_{q_n}(x,t_n)
|^2dx
\ge
c_\omega
A_n^2.
}
\tag{9.1}
$$

Using:

$$
A_n\ge a_0\nu,
$$

$$
\boxed{
r_n
\int_{
B_{R_\omega r_n}(x_n)
}
|
\nabla\times
(v_n)_{q_n}
|^2dx
\ge
c_1\nu^2.
}
\tag{9.2}
$$

The derivative Littlewood--Paley kernel tail gives the same estimate for the original shell:

$$
\omega_{q_n}
=
\nabla\times u_{q_n},
$$

after discarding finitely many terms:

$$
\boxed{
r_n
\int_{
B_{2R_\omega r_n}(x_n)
}
|
\omega_{q_n}(x,t_n)
|^2dx
\ge
c_2\nu^2.
}
\tag{9.3}
$$

Status:

$$
\boxed{
\textbf{PROVED using DCRP-16 good-collar separation plus the derivative kernel tail}.
}
$$

---

# 10. Two fixed compact mollifier scales

Choose one fixed radial:

$$
\varphi
\in
C_c^\infty(B_1),
$$

with:

$$
\varphi\ge0,
$$

and:

$$
\int\varphi=1.
$$

Because:

$$
\varphi
$$

is radial and nontrivial, its Fourier transform has the Taylor expansion:

$$
\boxed{
\widehat\varphi(\zeta)
=
1
-
c_\varphi
|\zeta|^2
+
O(
|\zeta|^4
)
}
\tag{10.1}
$$

near:

$$
\zeta=0,
$$

with:

$$
c_\varphi>0.
$$

Therefore one may choose fixed:

$$
0<a<b
$$

sufficiently small that:

$$
\boxed{
m_{a,b}(\zeta)
=
\widehat\varphi(a\zeta)
-
\widehat\varphi(b\zeta)
}
\tag{10.2}
$$

satisfies:

$$
\boxed{
|m_{a,b}(\zeta)|
\ge
d_\varphi
>
0
}
\tag{10.3}
$$

for every:

$$
\zeta\in\mathcal A.
$$

These two relative filter ratios are fixed for the entire sequence.

---

# 11. Full filtered-vorticity pair

At physical scale:

$$
r_n,
$$

define:

$$
\boxed{
\Omega_{a,n}
=
\nabla\times
S_{ar_n}u,
}
\tag{11.1}
$$

$$
\boxed{
\Omega_{b,n}
=
\nabla\times
S_{br_n}u,
}
\tag{11.2}
$$

and:

$$
\boxed{
G_n
=
\Omega_{a,n}
-
\Omega_{b,n}.
}
\tag{11.3}
$$

Because filtering and Littlewood--Paley projection commute:

$$
\boxed{
\Delta_{q_n}G_n
=
\left(
S_{ar_n}
-
S_{br_n}
\right)
\omega_{q_n}.
}
\tag{11.4}
$$

On the supplier annulus the multiplier is uniformly invertible.

---

# 12. NEW THEOREM — Filter-Difference Supplier Atom

There exist:

$$
R_G<\infty,
$$

and:

$$
c_G>0
$$

such that, after discarding finitely many:

$$
n,
$$

$$
\boxed{
r_n
\int_{
B_{R_Gr_n}(x_n)
}
|
\Delta_{q_n}G_n(x,t_n)
|^2dx
\ge
c_G\nu^2.
}
\tag{12.1}
$$

### Proof sketch

In normalized variables, the operator:

$$
S_a-S_b
$$

acts on the fixed supplier annulus by the multiplier:

$$
m_{a,b}.
$$

Equation (10.3) makes this multiplier invertible on the annulus.

Apply the same compactness/analyticity argument as Theorem 8.1 to the normalized class after applying:

$$
m_{a,b}(D)
\nabla\times.
$$

A vanishing local output would force the band-limited normalized supplier to vanish identically, contradicting its normalized point amplitude.

Undo the normalization and use (9.3).

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

# 13. Spectral-localization commutator

Choose a fixed normalized cutoff:

$$
\eta
\in
C_c^\infty(B_{2R_G}),
$$

with:

$$
\eta\equiv1
$$

on:

$$
B_{R_G}.
$$

Define:

$$
\eta_n(x)
=
\eta
\left(
\frac{
x-x_n
}{
r_n
}
\right).
$$

Then:

$$
\boxed{
\eta_n
\Delta_{q_n}G_n
=
\Delta_{q_n}
(
\eta_nG_n
)
-
[
\Delta_{q_n},
\eta_n
]
G_n.
}
\tag{13.1}
$$

Since:

$$
\Delta_{q_n}
$$

is bounded on:

$$
L^2,
$$

$$
\boxed{
\|
\eta_n
\Delta_{q_n}G_n
\|_2
\le
C
\|
\eta_nG_n
\|_2
+
\|
[
\Delta_{q_n},
\eta_n
]
G_n
\|_2.
}
\tag{13.2}
$$

---

# 14. NEW THEOREM — Endpoint Filtered Atom / Spectral-Localization Defect Alternative

## Theorem 14.1

There exists:

$$
c_E>0
$$

such that every sufficiently late local supplier event satisfies at least one of:

### full filtered endpoint atom

for one:

$$
\sigma_n\in\{a,b\},
$$

$$
\boxed{
r_n
\int
\eta_n^2
|
\Omega_{\sigma_n,n}(x,t_n)
|^2dx
\ge
c_E\nu^2,
}
\tag{14.1}
$$

or:

### spectral-localization defect

$$
\boxed{
\mathcal C_n^{spec}
=
r_n
\|
[
\Delta_{q_n},\eta_n
]
G_n(t_n)
\|_2^2
\ge
c_E\nu^2.
}
\tag{14.2}
$$

### Proof

Theorem 12.1 and:

$$
\eta_n\equiv1
$$

on the supplier ball give:

$$
r_n^{1/2}
\|
\eta_n
\Delta_{q_n}G_n
\|_2
\ge
c\nu.
$$

Use (13.2).

If the commutator term is at least half the right scale, (14.2) holds.

Otherwise:

$$
r_n^{1/2}
\|
\eta_nG_n
\|_2
\ge
c\nu.
$$

But:

$$
G_n
=
\Omega_{a,n}
-
\Omega_{b,n}.
$$

Hence:

$$
\|
\eta_nG_n
\|_2
\le
\|
\eta_n\Omega_{a,n}
\|_2
+
\|
\eta_n\Omega_{b,n}
\|_2.
$$

At least one term is bounded below by a fixed fraction.

Square and multiply by:

$$
r_n.
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

# 15. Interpretation of the spectral-localization defect

The commutator:

$$
[
\Delta_q,\eta_r
]
G
$$

measures the incompatibility between:

- isolating the supplier frequency;
- and isolating the supplier spatial core.

It is generated by the actual filtered vorticity and the fixed localization operation.

It does not copy a singularity label.

Thus:

$$
\boxed{
\mathcal C^{spec}
}
$$

is an admissible native localization residual.

A zero-localization branch must satisfy:

$$
\boxed{
\mathcal C_n^{spec}\to0.
}
\tag{15.1}
$$

On such a branch every sufficiently late supplier produces a genuine endpoint atom for one of the two fixed full filtered-vorticity fields.

---

# 16. Endpoint filtered enstrophy

Assume the endpoint-atom branch.

Let:

$$
\ell_n
=
\sigma_nr_n,
\qquad
\sigma_n\in\{a,b\}.
$$

Define:

$$
\boxed{
\mathcal E_n^\omega(t)
=
\frac{
r_n
}{
2
}
\int
\eta_n^2
|
\Omega_{\ell_n}(x,t)
|^2dx.
}
\tag{16.1}
$$

Then:

$$
\boxed{
\mathcal E_n^\omega(t_n)
\ge
e_0\nu^2
}
\tag{16.2}
$$

for a fixed:

$$
e_0>0.
$$

---

# 17. Fixed normalized backward window

Fix:

$$
\tau_0\in(0,1].
$$

Let:

$$
\boxed{
J_n
=
(
t_n-\tau_0r_n^2,
t_n
).
}
\tag{17.1}
$$

For sufficiently late:

$$
n,
$$

the interval lies before the first singular time and the solution is smooth there.

Define the spacetime filtered-enstrophy reservoir:

$$
\boxed{
\mathcal O_n
=
r_n^{-1}
\int_{J_n}
\int
\eta_n^2
|
\Omega_{\ell_n}
|^2dxdt.
}
\tag{17.2}
$$

Since:

$$
\mathcal E_n^\omega(t)
=
\frac{r_n}{2}
\int
\eta_n^2
|
\Omega_{\ell_n}
|^2,
$$

one has:

$$
\boxed{
\mathcal O_n
=
2
\int_{-\tau_0}^{0}
\mathcal E_n^\omega(\tau)
\,d\tau
}
\tag{17.3}
$$

in normalized time.

---

# 18. Reservoir branch is already taxed by diffusion/localization

Apply Theorem 3.1 with the cutoff:

$$
\eta_n.
$$

Then:

$$
\boxed{
\mathcal O_n
\le
C_\eta
\left(
\nu^{-1}\mathcal P_n
+
\mathcal L_n^\omega
\right),
}
\tag{18.1}
$$

where:

$$
\mathcal P_n
=
\nu r_n
\int_{J_n}
\int
\eta_n^2
|
\nabla\Omega_{\ell_n}
|^2,
$$

and:

$$
\mathcal L_n^\omega
$$

is the normalized cutoff-shell filtered-enstrophy cost.

Therefore if:

$$
\boxed{
\mathcal O_n
\ge
o_0>0,
}
\tag{18.2}
$$

then:

$$
\boxed{
\nu^{-1}\mathcal P_n
+
\mathcal L_n^\omega
\ge
c(o_0)>0.
}
\tag{18.3}
$$

Thus a supplier with nontrivial normalized residence time already pays a fixed diffusion/localization cost.

---

# 19. Temporal-spike branch

Suppose instead:

$$
\boxed{
\mathcal O_n
<
o_0.
}
\tag{19.1}
$$

Choose:

$$
o_0
\le
\frac{
e_0\nu^2\tau_0
}{
4
}.
$$

Then the normalized-time average of:

$$
\mathcal E_n^\omega
$$

over:

$$
[-\tau_0,0]
$$

is:

$$
\frac{
\mathcal O_n
}{
2\tau_0
}
<
\frac{
e_0\nu^2
}{
8
}.
$$

Therefore there exists:

$$
s_n\in J_n
$$

such that:

$$
\boxed{
\mathcal E_n^\omega(s_n)
\le
\frac{
e_0\nu^2
}{
8
}.
}
\tag{19.2}
$$

Together with (16.2):

$$
\boxed{
\mathcal E_n^\omega(t_n)
-
\mathcal E_n^\omega(s_n)
\ge
\frac{
7e_0
}{
8
}
\nu^2.
}
\tag{19.3}
$$

Thus an ultrashort endpoint spike has a fixed filtered-enstrophy rise inside the same normalized window.

---

# 20. Exact filtered-enstrophy balance on the spike interval

The external filtered-vorticity identity gives, on:

$$
[s_n,t_n],
$$

$$
\boxed{
\mathcal E_n^\omega(t_n)
-
\mathcal E_n^\omega(s_n)
+
\mathcal P_n^{[s_n,t_n]}
=
\mathcal V_n^{near}
+
\mathcal V_n^{far}
+
\mathcal R_n^{com}
+
\mathcal L_n.
}
\tag{20.1}
$$

Taking positive/absolute contributions:

$$
\boxed{
\frac{
7e_0
}{
8
}
\nu^2
+
\mathcal P_n^{[s_n,t_n]}
\le
\mathcal V_n^{+,\mathrm{near}}
+
\mathcal V_n^{+,\mathrm{far}}
+
|
\mathcal R_n^{com}
|
+
|
\mathcal L_n|.
}
\tag{20.2}
$$

This is the exact anti-spike ledger.

---

# 21. Insert near-field coercivity

For a fixed relative filter ratio:

$$
\sigma_n\in\{a,b\},
$$

the external theorem gives:

$$
\boxed{
\mathcal V_n^{+,\mathrm{near}}
\le
(1-\varepsilon)
\mathcal P_n^\rho
+
C_{\varepsilon,\sigma,M}
\mathcal O_n.
}
\tag{21.1}
$$

The local-energy constant is uniform on a fixed normalized obstruction slice.

Because:

$$
a,b
$$

are fixed, the filter-ratio constant is uniform.

---

# 22. Insert derivative-compatible commutator forcing

The external commutator theorem gives:

$$
\boxed{
|
\mathcal R_n^{com}
|
\le
\eta
\mathcal P_n
+
C_{\eta,\varphi}
\widetilde{\mathcal S}_n^{(3)}
+
\mathcal L_n^{com}.
}
\tag{22.1}
$$

Choose:

$$
\eta
<
\varepsilon/2.
$$

After matching the slightly enlarged diffusion regions by a fixed cutoff convention, the positive diffusion fraction left on the left-hand side is uniform.

Thus:

$$
\boxed{
c_0\nu^2
\le
C(M)
\mathcal O_n
+
\mathcal V_n^{+,\mathrm{far}}
+
C
\widetilde{\mathcal S}_n^{(3)}
+
\mathcal L_n
+
\mathcal L_n^{com},
}
\tag{22.2}
$$

for some fixed:

$$
c_0>0,
$$

provided:

$$
o_0
$$

has been chosen sufficiently small.

Status:

$$
\boxed{
\textbf{PROVED using the exact balance and arXiv:2606.27560 near-field/commutator theorems}.
}
$$

---

# 23. No invisible temporal spike

Equation (22.2) gives:

$$
\boxed{
\textbf{
ultrashort supplier spike}
\Longrightarrow
\textbf{
far-field work}
\ \vee\
\textbf{
critical commutator increment defect}
\ \vee\
\textbf{
localization residual}.
}
}
\tag{23.1}
$$

Thus temporal concentration is not an extra unpriced category.

The exact filtered-enstrophy balance prices it immediately.

This closes the DCRP-21 "probe head for an instant" loophole.

---

# 24. Far-field spike branch

Suppose a zero-commutator / zero-localization branch has:

$$
\widetilde{\mathcal S}_n^{(3)}
\to0,
$$

$$
\mathcal L_n
+
\mathcal L_n^{com}
\to0.
$$

Suppose also the reservoir branch is absent:

$$
\mathcal O_n\to0.
$$

Then (22.2) implies:

$$
\boxed{
\liminf
\mathcal V_n^{+,\mathrm{far}}
>
0.
}
\tag{24.1}
$$

DCRP-21 applies.

Therefore the source annulus must satisfy:

$$
\boxed{
m_n\to\infty
}
\tag{24.2}
$$

and:

$$
\boxed{
\mathfrak A_{j_n,n}
\to\infty.
}
\tag{24.3}
$$

Thus the last spike branch is a spatial-source escape defect.

---

# 25. NEW THEOREM — Local Supplier Activation/Tax Alternative

## Theorem 25.1

Assume:

- the DCRP-16 local supplier sequence;
- a uniform normalized local-energy bound:

  $$
  M_n\le M_\ast;
  $$

- the fixed two-filter family:

  $$
  \{a,b\};
  $$

- the fixed normalized spatial cutoff family.

Then every sufficiently late supplier event satisfies at least one of the following scale-uniform alternatives.

### A. spectral localization defect

$$
\boxed{
\mathcal C_n^{spec}
\ge
c_A\nu^2.
}
\tag{25.1}
$$

### B. filtered diffusion/localization payment

$$
\boxed{
\nu^{-1}
\mathcal P_n
+
\mathcal L_n^\omega
\ge
c_B\nu^2.
}
\tag{25.2}
$$

### C. derivative-compatible commutator defect

$$
\boxed{
\widetilde{\mathcal S}_n^{(3)}
\ge
c_C\nu^2.
}
\tag{25.3}
$$

### D. filtered localization residual

$$
\boxed{
\mathcal L_n
+
\mathcal L_n^{com}
\ge
c_D\nu^2.
}
\tag{25.4}
$$

### E. far-field spatial-source branch

$$
\boxed{
\mathcal V_n^{+,\mathrm{far}}
\ge
c_E\nu^2.
}
\tag{25.5}
$$

If branch E persists while the local reservoir tends to zero, DCRP-21 forces normalized spatial-source escape with diverging annular vorticity amplitude.

### Proof

Apply Theorem 14.1.

If branch A occurs, stop.

Otherwise a full filtered-vorticity endpoint atom exists.

If:

$$
\mathcal O_n\ge o_0,
$$

Theorem 3.1 gives branch B.

If:

$$
\mathcal O_n<o_0,
$$

Sections 19--22 give a fixed lower bound on the sum of branches C--E and the localization terms.

At least one is uniformly positive.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED at the finite supplier-event level}.
}
$$

---

# 26. Zero-cost supplier consequence

Suppose a transition-complete normalized supplier sequence satisfies:

$$
\mathcal C_n^{spec}\to0,
$$

$$
\mathcal P_n\to0,
$$

$$
\mathcal L_n^\omega\to0,
$$

$$
\widetilde{\mathcal S}_n^{(3)}\to0,
$$

$$
\mathcal L_n
+
\mathcal L_n^{com}
\to0,
$$

and has no far-field spatial-source escape defect.

Then Theorem 25.1 is impossible.

Hence:

$$
\boxed{
\textbf{
a local supplier sequence cannot be an exact zero-cost
filtered-vorticity mechanism sequence.
}
}
\tag{26.1}
$$

This is independent of any temporal residence-time assumption.

---

# 27. Relation to Cheskidov--Dai temporal activity

Cheskidov--Dai prove that high-frequency vorticity-shell activity integrated in time is itself a regularity-relevant quantity:

$$
\limsup_{q\to\infty}
\int
1_{\{q\le Q(t)\}}
\|
\Delta_q\omega(t)
\|_\infty
dt
$$

must exceed a fixed small threshold along a blowup branch.

DCRP-22 does not need this theorem to prove the anti-spike alternative.

The present proof instead uses:

- the local supplier endpoint;
- the exact localized filtered-enstrophy identity.

The Cheskidov--Dai criterion is retained as independent calibration that high-frequency **temporal** activity is not an artificial concern.

---

# 28. What is now closed

The following gap from DCRP-21 is closed:

$$
\boxed{
\text{local supplier}
\Longrightarrow
\text{filtered mechanism activation}
\ \vee\
\text{explicit paid/native defect}.
}
\tag{28.1}
$$

The supplier cannot escape by:

- being only a velocity atom;
- canceling silently in one filtered field;
- existing for vanishing normalized time;
- hiding in the lower-order compact local enstrophy reservoir.

Every route produces a fixed scale-critical entry.

---

# 29. What remains open

The supplier theorem gives infinitely many supplier events near a singular point.

The finite-scale critical ledger, however, requires **positive-density untaxed critical supply** along a persistent non-CKN chain.

An infinite supplier subsequence may still be sparse in dyadic scale.

Therefore:

$$
\boxed{
\text{every supplier is taxed}
}
$$

does not yet imply:

$$
\boxed{
\text{every profitable bad transition is taxed}.
}
$$

This is the same distinction identified in DCRP-19, now sharpened.

---

# 30. New exact frontier — bounded-lag supplier capture

The next target is:

$$
\boxed{
\textbf{
Untaxed Critical Supply
}
\Longrightarrow
\textbf{
Bounded-Lag Local Supplier Activation}.
}
\tag{30.1}
$$

A useful quantitative form is:

> Fix:
>
> $$
> \eta>0.
> $$
>
> Suppose one non-CKN transition satisfies:
>
> $$
> \left(
> \mathrm{Sup}^{full}_k
> -
> \mathrm{Tax}^{full}_k
> \right)_+
> \ge
> \eta,
> $$
>
> while:
>
> - leakage is small;
> - coarse/subfilter native defects are below their paid thresholds.
>
> Then within at most:
>
> $$
> L=L(\eta,M)
> $$
>
> dyadic descendant steps, there exists a local supplier event satisfying:
>
> $$
> \lambda^{-1}
> |
> \Delta_\lambda u
> |
> \ge
> c(\eta,M)\nu,
> $$
>
> or one of the already-paid filtered-vorticity defects is positive.

If this is proved, the positive-density untaxed supply required by the finite-scale survival theorem produces positive-density supplier activations.

DCRP-22 then taxes every such activation.

This would directly attack the persistent profitable branch rather than a sparse auxiliary sequence.

---

# 31. Updated proof-state diagram

The current route is:

$$
\boxed{
\begin{aligned}
\text{first singular point}
&\Longrightarrow
\text{local supplier sequence}\\
&\Longrightarrow
\text{filtered endpoint atom}
\vee
\text{spectral localization defect}\\
&\Longrightarrow
\text{reservoir payment}
\vee
\text{filtered surplus}\\
&\Longrightarrow
\text{diffusion}
\vee
\widetilde{\mathcal S}^{(3)}
\vee
\text{localization}
\vee
\text{far spatial escape}.
\end{aligned}
}
\tag{31.1}
$$

Thus individual local suppliers have no zero-cost temporal-spike route.

The missing global bridge is density:

$$
\boxed{
\textbf{
profitable bad-scale supply}
\Longrightarrow
\textbf{
supplier within bounded scale lag}.
}
}
\tag{31.2}
$$

---

# 32. Source ledger

## Filtered Vortex Stretching and Subgrid Defects

Primary results used:

- exact spatially filtered vorticity equation;
- localized filtered-enstrophy identity:

  $$
  \mathcal E_\chi(s_1)
  -
  \mathcal E_\chi(s_0)
  +
  \mathcal P_\chi
  =
  \mathcal V_\chi^{near}
  +
  \mathcal V_\chi^{rem}
  +
  \mathcal R_\chi
  +
  \mathcal L_\chi;
  $$

- near-field stretching-to-diffusion coercivity:

  $$
  \mathcal V^{+,\mathrm{near}}
  \le
  (1-\varepsilon)\mathcal P^\rho
  +
  C_{\varepsilon}M(r/\ell)^5\mathcal O;
  $$

- derivative-compatible commutator insertion:

  $$
  F^{com}
  \le
  \eta P
  +
  C_\eta
  \widetilde{\mathcal S}^{(3)}
  +
  L^{com};
  $$

- adjoint cancellation of the principal localization residual;
- far-field annular reassignment used in DCRP-21.

## Cheskidov--Dai

Primary regularity criterion used only as independent temporal calibration:

a blowup branch cannot have asymptotically small integrated high-frequency vorticity-shell activity on the active dissipation range.

---

# 33. End state

The major correction is:

$$
\boxed{
\mathcal O^\eta
\le
C
\left(
\nu^{-1}\mathcal P^\eta
+
\mathcal L^\omega
\right).
}
$$

Thus the compact local filtered-enstrophy reservoir has no free IR escape.

The supplier-to-filtered bridge is:

$$
\boxed{
\text{supplier}
\Longrightarrow
\text{full filtered endpoint atom}
\ \vee\
\mathcal C^{spec}>0.
}
$$

The temporal anti-spike theorem is:

$$
\boxed{
\text{endpoint atom}
\Longrightarrow
\text{diffusion/localization reservoir payment}
\ \vee\
\text{positive filtered mechanism surplus}.
}
$$

After near-field and commutator insertion:

$$
\boxed{
\text{supplier}
\Longrightarrow
\text{diffusion}
\vee
\text{commutator defect}
\vee
\text{localization}
\vee
\text{far spatial escape}.
}
$$

Therefore ultrashort supplier spikes are not an untaxed mechanism.

The next single frontier is:

$$
\boxed{
\textbf{
Untaxed Critical Supply / Bounded-Lag Supplier Activation Lemma}.
}
$$

This is now the density bridge between the unconditional finite-scale survival ledger and the supplier mechanism that DCRP has learned how to tax.