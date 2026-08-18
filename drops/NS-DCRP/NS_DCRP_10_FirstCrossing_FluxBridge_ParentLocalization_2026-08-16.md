# NS-DCRP-10 — First-Crossing Shell Flux, Signed Triadic Ancestry, and Parent-or-Defect Localization

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: refine DCRP-09 from nonlinear-source ancestry to genuine positive kinetic-energy transfer into the dissipation-boundary supplier shell, and localize the signed triadic ancestry into a parent-or-defect alternative.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: MORP-01 through MORP-05, DCRP-08, DCRP-09.
- external primary calibration: Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-09 proved that a sufficiently high dissipation-boundary supplier shell must receive a fixed amount of actual same-history nonlinear Duhamel forcing.

That result remains correct, but the source norm

$$
\left\|
\Delta_Q
\mathbb P
\nabla\cdot
(u\otimes u)
\right\|_2
$$

does not distinguish genuine shell-energy transfer from transport / phase deformation.

The present round replaces source-norm ancestry by a signed shell-energy statement.

For a fixed dyadic shell

$$
q,
$$

define

$$
e_q(t)
=
\|u_q(t)\|_2^2
$$

and the signed nonlinear shell transfer

$$
\boxed{
\mathcal T_q(t)
=
-
\left<
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u),
u_q
\right>.
}
\tag{1.1}
$$

The exact shell-energy identity is

$$
\boxed{
\frac12
\frac d{dt}
e_q(t)
+
\nu
\|\nabla u_q(t)\|_2^2
=
\mathcal T_q(t).
}
\tag{1.2}
$$

Define the critical shell energy

$$
\boxed{
\mathcal K_q(t)
=
\lambda_q
e_q(t)
=
\lambda_q
\|u_q(t)\|_2^2.
}
\tag{1.3}
$$

DCRP-08 gives, at every dissipation-boundary supplier time,

$$
\boxed{
\mathcal K_{Q(t)}(t)
\ge
\kappa_0\nu^2
}
\tag{1.4}
$$

for a universal

$$
\kappa_0>0.
$$

Suppose

$$
T
$$

is a hypothetical first singular time and choose supplier times

$$
t_n\uparrow T,
$$

with

$$
Q_n=Q(t_n)\to\infty.
$$

Because the solution is smooth on every compact subinterval

$$
[0,T-\varepsilon],
$$

the high-shell critical energy satisfies

$$
\sup_{t\le T-\varepsilon}
\mathcal K_{Q_n}(t)
\to0.
$$

Therefore each sufficiently large supplier shell must undergo a genuine first threshold crossing near

$$
T.
$$

Choose the fixed levels

$$
\alpha
=
\frac14
\kappa_0\nu^2,
$$

$$
\beta
=
\frac12
\kappa_0\nu^2.
$$

There exist times

$$
r_n<s_n<t_n,
$$

with

$$
r_n,s_n\uparrow T,
$$

such that

$$
\mathcal K_{Q_n}(r_n)=\alpha,
$$

$$
\mathcal K_{Q_n}(s_n)=\beta,
$$

and

$$
\alpha
<
\mathcal K_{Q_n}(t)
<
\beta
$$

for

$$
r_n<t<s_n.
$$

Integrating (1.2) gives the new lower bound

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)\,dt
\ge
\frac18
\kappa_0\nu^2.
}
\tag{1.5}
$$

Hence also

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\left(
\mathcal T_{Q_n}(t)
\right)_+
\,dt
\ge
\frac18
\kappa_0\nu^2.
}
\tag{1.6}
$$

This is an actual positive, scale-critical kinetic-energy transfer event occurring arbitrarily close to the hypothetical singular horizon.

Thus the UV supplier does not merely have nonlinear ancestry.

It has a **paid net flux ancestry**.

A signed Bony decomposition yields

$$
\mathcal T_Q
=
\mathcal T_Q^{LH}
+
\mathcal T_Q^{HL}
+
\mathcal T_Q^{HH}.
$$

Therefore at least one of the three integrated signed classes carries a fixed positive critical amount.

The low--high / high--low classes are controlled by a genuine low-frequency shear commutator.

The remote high--high class obeys a new suppression estimate:

$$
\boxed{
\lambda_Q
\int_I
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
\,dt
\le
C\nu
2^{-5M/2}
\mathfrak W_{Q,M}[I],
}
\tag{1.7}
$$

on a threshold-crossing interval, where

$$
\boxed{
\mathfrak W_{Q,M}[I]
=
\lambda_Q^{-1}
\int_I
\sum_{p\ge Q+M}
\lambda_p^4
\|u_p(t)\|_2^2
\,dt.
}
\tag{1.8}
$$

The quantity

$$
\mathfrak W_{Q,M}
$$

is scale critical.

Consequently, if a fixed positive portion of the supplier flux is carried by parent scales

$$
p-Q\to\infty,
$$

then

$$
\mathfrak W_{Q,M}
$$

must grow at least exponentially in the relative parent separation.

Thus:

$$
\boxed{
\textbf{
positive supplier flux}
\Longrightarrow
\textbf{
low-mode shear tax}
\ \vee\
\textbf{
bounded-relative parent}
\ \vee\
\textbf{
large derivative occupancy defect}.
}
}
\tag{1.9}
$$

This is the first parent-or-defect reduction using a **signed actual kinetic-energy transfer**, rather than an unsigned source norm.

---

# 2. Refinement of DCRP-09

DCRP-09 defined the critical Duhamel source input

$$
\mathfrak J_Q
=
\lambda_Q^{1/2}
\int
\left\|
\Delta_Q
\mathbb P
\nabla\cdot
(u\otimes u)
\right\|_2
dt.
$$

A lower bound on

$$
\mathfrak J_Q
$$

proves actual same-history nonlinear dependence.

However, a low-frequency velocity can advect a high-frequency packet and make the source norm large without producing comparable net kinetic-energy gain of that shell.

Therefore:

$$
\boxed{
\text{Duhamel source ancestry}
\not\equiv
\text{paid shell-energy ancestry}.
}
\tag{2.1}
$$

DCRP-09 remains a correct causal result.

DCRP-10 strengthens the paid-side statement by working with

$$
\mathcal T_Q.
$$

Status:

$$
\boxed{
\textbf{REFINEMENT, not retraction}.
}
$$

---

# 3. Exact shell-energy equation

Apply the Littlewood--Paley projector

$$
\Delta_q
$$

to

$$
\partial_tu
-
\nu\Delta u
+
\mathbb P\nabla\cdot(u\otimes u)
=
0.
$$

Because

$$
\Delta_q,
\qquad
\mathbb P,
\qquad
\Delta
$$

are Fourier multipliers,

$$
\partial_tu_q
-
\nu\Delta u_q
+
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u)
=
0.
$$

Pair with

$$
u_q.
$$

Then

$$
\boxed{
\frac12
\frac d{dt}
\|u_q\|_2^2
+
\nu
\|\nabla u_q\|_2^2
=
-
\left<
\Delta_q
\mathbb P
\nabla\cdot
(u\otimes u),
u_q
\right>.
}
\tag{3.1}
$$

Define the right side to be

$$
\mathcal T_q.
$$

Positive

$$
\mathcal T_q
$$

means net nonlinear energy transfer **into** shell

$$
q.
$$

This sign convention is fixed for the remainder of the checkpoint.

---

# 4. Scale-critical shell flux

Define

$$
\boxed{
\Phi_q[I]
=
\lambda_q
\int_I
\mathcal T_q(t)\,dt.
}
\tag{4.1}
$$

and the positive paid amount

$$
\boxed{
\Phi_q^+[I]
=
\lambda_q
\int_I
(\mathcal T_q(t))_+
\,dt.
}
\tag{4.2}
$$

Under a dyadic Navier--Stokes scaling

$$
u_a(x,t)
=
a
u(ax,a^2t),
\qquad
a=2^m,
$$

the corresponding shell index shifts by

$$
m.
$$

Shell energy scales as

$$
\|u_q\|_2^2
\mapsto
a^{-1}
\|u_q\|_2^2.
$$

Hence its time derivative and

$$
\mathcal T_q
$$

scale as

$$
a.
$$

Since

$$
\lambda_q\mapsto a\lambda_q
$$

and

$$
dt\mapsto a^{-2}dt,
$$

$$
\boxed{
\Phi_q
}
$$

is exactly invariant under dyadic parabolic rescaling.

For arbitrary scaling factors it is scale critical up to the bounded overlap constants of the fixed Littlewood--Paley partition.

---

# 5. Uniform high-shell smallness before the singular horizon

Let

$$
T
$$

be a hypothetical first singular time of a strong solution.

Fix

$$
\varepsilon>0.
$$

Since the solution is smooth on

$$
[0,T-\varepsilon],
$$

for any

$$
s>\frac12,
$$

$$
\sup_{0\le t\le T-\varepsilon}
\|u(t)\|_{H^s}
<
\infty.
$$

For every shell

$$
q,
$$

$$
\|u_q(t)\|_2
\le
C
\lambda_q^{-s}
\|u(t)\|_{H^s}.
$$

Therefore

$$
\mathcal K_q(t)
=
\lambda_q
\|u_q(t)\|_2^2
\le
C_\varepsilon
\lambda_q^{1-2s}.
$$

Since

$$
s>\frac12,
$$

$$
\boxed{
\sup_{0\le t\le T-\varepsilon}
\mathcal K_q(t)
\to0
\qquad
(q\to\infty).
}
\tag{5.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. NEW THEOREM — first-crossing supplier flux

## Theorem 6.1

Assume

$$
T<\infty
$$

is a hypothetical first singular time.

Let

$$
t_n\uparrow T
$$

be dissipation-boundary supplier times with

$$
Q_n=Q(t_n)\to\infty
$$

and

$$
\mathcal K_{Q_n}(t_n)
\ge
\kappa_0\nu^2.
$$

Set

$$
\alpha
=
\frac14
\kappa_0\nu^2,
$$

$$
\beta
=
\frac12
\kappa_0\nu^2.
$$

Then after discarding finitely many terms there exist

$$
r_n<s_n<t_n
$$

such that:

$$
\boxed{
r_n,s_n\to T,
}
\tag{6.1}
$$

$$
\boxed{
\mathcal K_{Q_n}(r_n)=\alpha,
\qquad
\mathcal K_{Q_n}(s_n)=\beta,
}
\tag{6.2}
$$

and

$$
\boxed{
\alpha
<
\mathcal K_{Q_n}(t)
<
\beta
\qquad
(r_n<t<s_n).
}
\tag{6.3}
$$

Moreover:

$$
\boxed{
\Phi_{Q_n}[r_n,s_n]
\ge
\frac18
\kappa_0\nu^2.
}
\tag{6.4}
$$

and hence:

$$
\boxed{
\Phi_{Q_n}^+[r_n,s_n]
\ge
\frac18
\kappa_0\nu^2.
}
\tag{6.5}
$$

### Proof

By (5.1), for every fixed

$$
\varepsilon>0,
$$

and all sufficiently large

$$
n,
$$

$$
\sup_{t\le T-\varepsilon}
\mathcal K_{Q_n}(t)
<
\alpha.
$$

But

$$
\mathcal K_{Q_n}(t_n)
\ge
2\beta.
$$

By continuity in time, the shell must cross the levels

$$
\alpha
$$

and

$$
\beta.
$$

Let

$$
s_n
$$

be the first time before

$$
t_n
$$

at which

$$
\mathcal K_{Q_n}=\beta.
$$

Let

$$
r_n
$$

be the last time before

$$
s_n
$$

at which

$$
\mathcal K_{Q_n}=\alpha.
$$

Then (6.2)--(6.3) hold.

Since for every fixed

$$
\varepsilon>0
$$

the level

$$
\alpha
$$

cannot be reached on

$$
[0,T-\varepsilon]
$$

for sufficiently large

$$
n,
$$

one has

$$
r_n\to T.
$$

Therefore also

$$
s_n\to T.
$$

Integrate the exact shell-energy identity (3.1):

$$
\frac12
\left[
e_{Q_n}(s_n)-e_{Q_n}(r_n)
\right]
+
\nu
\int_{r_n}^{s_n}
\|\nabla u_{Q_n}\|_2^2
dt
=
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)
dt.
$$

Multiply by

$$
\lambda_{Q_n}.
$$

The first term is:

$$
\frac12
\left[
\mathcal K_{Q_n}(s_n)
-
\mathcal K_{Q_n}(r_n)
\right]
=
\frac12
(\beta-\alpha).
$$

The viscous term is nonnegative.

Thus:

$$
\Phi_{Q_n}[r_n,s_n]
\ge
\frac12
(\beta-\alpha)
=
\frac18
\kappa_0\nu^2.
$$

Finally:

$$
\int
\mathcal T
\le
\int
\mathcal T_+,
$$

which gives (6.5).

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

# 7. Meaning of the first-crossing theorem

The lower bound

$$
\Phi_{Q_n}
\ge
c\nu^2
$$

has four useful properties.

1. It is generated by the actual Navier--Stokes state.

2. It is signed: the shell has received **net positive energy**.

3. It is scale critical.

4. The interval on which the payment occurs satisfies

$$
r_n,s_n\to T.
$$

Therefore:

$$
\boxed{
\textbf{
a hypothetical singularity requires arbitrarily high-frequency,
near-horizon, positive critical kinetic-energy transfer events.
}
}
\tag{7.1}
$$

This is stronger for paid-side purposes than the unsigned Duhamel forcing bound of DCRP-09.

---

# 8. Signed Bony decomposition

Write the Bony decomposition of the shell nonlinear term as:

$$
\mathcal T_Q
=
\mathcal T_Q^{LH}
+
\mathcal T_Q^{HL}
+
\mathcal T_Q^{HH}.
$$

The precise finite index ranges depend on the chosen smooth Littlewood--Paley partition, but the structural classes are:

### Low--high

A low-frequency velocity transports / deforms a near-

$$
Q
$$

mode.

### High--low

A near-

$$
Q
$$

mode acts on a lower-frequency velocity.

### High--high

Two comparable high parents interact and output at shell

$$
Q.
$$

Define:

$$
\boxed{
\Phi_Q^{XY}[I]
=
\lambda_Q
\int_I
\mathcal T_Q^{XY}(t)\,dt,
}
\tag{8.1}
$$

for

$$
XY\in\{LH,HL,HH\}.
$$

Then:

$$
\boxed{
\Phi_Q
=
\Phi_Q^{LH}
+
\Phi_Q^{HL}
+
\Phi_Q^{HH}.
}
\tag{8.2}
$$

If:

$$
\Phi_Q\ge c_\ast\nu^2,
$$

then:

$$
\boxed{
\max
\left\{
\Phi_Q^{LH},
\Phi_Q^{HL},
\Phi_Q^{HH}
\right\}
\ge
\frac{
c_\ast
}{
3
}
\nu^2.
}
\tag{8.3}
$$

This is a signed statement.

No absolute-value overcount is used.

---

# 9. Low--high transport cancellation

The low--high energy contribution is not merely bounded by the size of the low velocity.

The divergence-free leading transport cancels.

For a representative term:

$$
\left<
\Delta_Q
(
u_{\le Q-2}\cdot\nabla u_Q
),
u_Q
\right>,
$$

insert:

$$
\Delta_Q
(
u_{\le Q-2}\cdot\nabla u_Q
)
=
u_{\le Q-2}\cdot\nabla\Delta_Qu_Q
+
[
\Delta_Q,
u_{\le Q-2}\cdot\nabla
]u_Q.
$$

The leading term satisfies:

$$
\left<
u_{\le Q-2}\cdot\nabla u_Q,
u_Q
\right>
=
0
$$

because:

$$
\nabla\cdot u_{\le Q-2}=0.
$$

Therefore the actual shell-energy transfer is governed by the commutator / shear:

$$
\boxed{
\left|
\mathcal T_Q^{LH}
\right|
\le
C
\|\nabla u_{\le Q+C}\|_\infty
\sum_{|p-Q|\le C}
\|u_p\|_2^2.
}
\tag{9.1}
$$

The same structural bound holds for the corresponding high--low class after the standard paraproduct rearrangement:

$$
\boxed{
\left|
\mathcal T_Q^{HL}
\right|
\le
C
\|\nabla u_{\le Q+C}\|_\infty
\sum_{|p-Q|\le C}
\|u_p\|_2^2.
}
\tag{9.2}
$$

These are standard Littlewood--Paley commutator consequences of incompressibility.

The important point is:

$$
\boxed{
\text{constant / Galilean low velocity does not pay the shell flux}.
}
$$

Only low-frequency deformation / shear does.

---

# 10. Low--high parent-or-shear dichotomy

Define the near-shell critical cluster:

$$
\boxed{
\mathcal C_Q(t)
=
\lambda_Q
\sum_{|p-Q|\le C}
\|u_p(t)\|_2^2.
}
\tag{10.1}
$$

Equations (9.1)--(9.2) imply:

$$
\boxed{
\lambda_Q
\left|
\mathcal T_Q^{LH}
+
\mathcal T_Q^{HL}
\right|
\le
C
\|\nabla u_{\le Q+C}\|_\infty
\mathcal C_Q(t).
}
\tag{10.2}
$$

Suppose on a first-crossing interval

$$
I=[r,s]
$$

the low--high / high--low class pays:

$$
\boxed{
\Phi_Q^{LH}
+
\Phi_Q^{HL}
\ge
\eta\nu^2.
}
\tag{10.3}
$$

Fix any

$$
M_0>0.
$$

Then one of the following holds.

### Near-scale parent amplification

There exists

$$
t\in I
$$

such that:

$$
\boxed{
\mathcal C_Q(t)
>
M_0\nu^2.
}
\tag{10.4}
$$

This is a nonvanishing, indeed large, near-scale critical state cluster.

### Low-mode shear tax

Otherwise:

$$
\mathcal C_Q(t)
\le
M_0\nu^2
$$

throughout

$$
I.
$$

Then (10.2)--(10.3) yield:

$$
\boxed{
\int_I
\|\nabla u_{\le Q+C}(t)\|_\infty
dt
\ge
\frac{
\eta
}{
CM_0
}.
}
\tag{10.5}
$$

The integral is scale invariant.

Therefore:

$$
\boxed{
\textbf{
positive LH/HL supplier flux}
\Longrightarrow
\textbf{
near-scale critical parent}
\ \vee\
\textbf{
positive low-mode shear debt}.
}
}
\tag{10.6}
$$

Status:

$$
\boxed{
\textbf{PROVED modulo the standard commutator bound (9.1)--(9.2)}.
}
$$

---

# 11. Remote high--high forcing estimate

Consider the high--high contribution from parent shells:

$$
p\ge Q+M.
$$

Write:

$$
F_Q^{HH,\ge Q+M}
=
\sum_{p\ge Q+M}
\Delta_Q
\mathbb P
\nabla\cdot
(
u_p\otimes\widetilde u_p
).
$$

By Bernstein:

$$
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\le
C
\lambda_Q
\sum_{p\ge Q+M}
\|u_p\|_\infty
\|\widetilde u_p\|_2.
$$

Again by Bernstein:

$$
\|u_p\|_\infty
\le
C
\lambda_p^{3/2}
\|u_p\|_2.
$$

After absorbing the finite neighbor width in

$$
\widetilde u_p,
$$

$$
\boxed{
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\le
C
\lambda_Q
\sum_{p\ge Q+M}
\lambda_p^{3/2}
\|u_p\|_2^2.
}
\tag{11.1}
$$

Since:

$$
\lambda_p^{3/2}
=
\lambda_p^{-5/2}
\lambda_p^4,
$$

and:

$$
\lambda_p^{-5/2}
\le
2^{-5M/2}
\lambda_Q^{-5/2},
$$

one gets:

$$
\boxed{
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\le
C
2^{-5M/2}
\lambda_Q^{-3/2}
\mathcal H^{(2)}_{\ge Q+M},
}
\tag{11.2}
$$

where:

$$
\boxed{
\mathcal H^{(2)}_{\ge Q+M}(t)
=
\sum_{p\ge Q+M}
\lambda_p^4
\|u_p(t)\|_2^2.
}
\tag{11.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 12. NEW THEOREM — remote-parent $H^2$ occupancy barrier

On a first-crossing interval:

$$
I=[r,s],
$$

one has:

$$
\mathcal K_Q(t)
<
\beta
=
\frac12
\kappa_0\nu^2.
$$

Hence:

$$
\boxed{
\|u_Q(t)\|_2
\le
C_\kappa
\nu
\lambda_Q^{-1/2}.
}
\tag{12.1}
$$

The remote high--high shell transfer satisfies:

$$
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
\le
\left\|
F_Q^{HH,\ge Q+M}
\right\|_2
\|u_Q\|_2.
$$

Using (11.2) and (12.1):

$$
\boxed{
\lambda_Q
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
\le
C
\nu
2^{-5M/2}
\lambda_Q^{-1}
\mathcal H^{(2)}_{\ge Q+M}(t).
}
\tag{12.2}
$$

Define the scale-critical remote

$$
H^2
$$

occupancy:

$$
\boxed{
\mathfrak W_{Q,M}[I]
=
\lambda_Q^{-1}
\int_I
\mathcal H^{(2)}_{\ge Q+M}(t)
\,dt.
}
\tag{12.3}
$$

Then:

$$
\boxed{
\lambda_Q
\int_I
\left|
\mathcal T_Q^{HH,\ge Q+M}
\right|
dt
\le
C
\nu
2^{-5M/2}
\mathfrak W_{Q,M}[I].
}
\tag{12.4}
$$

Therefore if:

$$
\boxed{
\lambda_Q
\int_I
\mathcal T_Q^{HH,\ge Q+M}
dt
\ge
\eta\nu^2
}
\tag{12.5}
$$

for some

$$
\eta>0,
$$

then necessarily:

$$
\boxed{
\mathfrak W_{Q,M}[I]
\ge
c
\eta
\nu
2^{5M/2}.
}
\tag{12.6}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 13. Scale criticality of the remote occupancy

The homogeneous velocity

$$
\dot H^2
$$

square scales as:

$$
\|u\|_{\dot H^2}^2
\mapsto
a^3
\|u\|_{\dot H^2}^2.
$$

Also:

$$
dt\mapsto a^{-2}dt,
$$

and:

$$
\lambda_Q^{-1}
\mapsto
a^{-1}
\lambda_Q^{-1}.
$$

Therefore:

$$
\boxed{
\lambda_Q^{-1}
\int
\|u\|_{\dot H^2}^2
dt
}
\tag{13.1}
$$

is parabolic-scale invariant.

Hence:

$$
\boxed{
\mathfrak W_{Q,M}
}
$$

is a genuine scale-critical derivative occupancy coordinate.

Remote parent escape cannot be dismissed as a raw supercritical artifact.

---

# 14. Corollary — bounded occupancy localizes high--high parents

Suppose a family of first-crossing intervals satisfies:

$$
\boxed{
\sup_n
\mathfrak W_{Q_n,0}[I_n]
\le
W_\ast
<
\infty.
}
\tag{14.1}
$$

Suppose also that:

$$
\Phi_{Q_n}^{HH}[I_n]
\ge
\eta\nu^2.
$$

Choose

$$
M_\ast
$$

large enough that:

$$
C
\nu
2^{-5M_\ast/2}
W_\ast
<
\frac12
\eta\nu^2.
$$

Then the remote parents:

$$
p\ge Q_n+M_\ast
$$

cannot contribute more than half the required positive

$$
HH
$$

flux.

Therefore:

$$
\boxed{
\lambda_{Q_n}
\int_{I_n}
\mathcal T_{Q_n}^{HH,\,
Q_n-2\le p<Q_n+M_\ast}
dt
\ge
\frac12
\eta\nu^2.
}
\tag{14.2}
$$

Since there are only finitely many relative parent indices in this range, at least one bounded-relative parent class carries a fixed positive signed transfer share.

Thus:

$$
\boxed{
\textbf{
bounded scale-normalized }H^2\textbf{ occupancy}
\Longrightarrow
\textbf{
bounded-relative HH ancestry}.
}
}
\tag{14.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 15. Remote parent escape forces a derivative defect

Suppose instead that for every fixed

$$
M,
$$

the positive

$$
HH
$$

flux increasingly originates from:

$$
p-Q\ge M.
$$

Then for a sequence

$$
M_n\to\infty,
$$

one has:

$$
\lambda_{Q_n}
\int_{I_n}
\mathcal T_{Q_n}^{HH,\ge Q_n+M_n}
dt
\ge
\eta\nu^2.
$$

Theorem 12.1 gives:

$$
\boxed{
\mathfrak W_{Q_n,M_n}[I_n]
\ge
c
\eta\nu
2^{5M_n/2}
\to\infty.
}
\tag{15.1}
$$

Thus:

$$
\boxed{
\textbf{
unbounded relative HH ancestry}
\Longrightarrow
\textbf{
divergent scale-critical }H^2\textbf{ occupancy}.
}
}
\tag{15.2}
$$

This is a concrete derivative noncompactness defect.

It is substantially stronger than the purely probabilistic statement that parent mass escapes to relative infinity.

---

# 16. Normalized crossing duration

Define the normalized duration of a first-crossing interval:

$$
\boxed{
L_Q[I]
=
\nu
\lambda_Q^2
|I|.
}
\tag{16.1}
$$

This is scale invariant.

There are two possibilities.

### Bounded-duration branch

$$
\sup_n
L_{Q_n}[I_n]
<
\infty.
$$

Then any bounded-relative parent interaction that pays a fixed amount over the interval must achieve nontrivial critical amplitude at some actual time.

### Long-germ branch

$$
L_{Q_n}[I_n]
\to\infty.
$$

But by construction:

$$
\alpha
<
\mathcal K_{Q_n}(t)
<
\beta
$$

throughout the entire crossing interval.

After re-scaling to shell

$$
Q_n,
$$

the supplier shell therefore remains nonvanishing for a normalized time interval whose length tends to infinity.

Thus:

$$
\boxed{
\textbf{
long normalized crossing duration}
\Longrightarrow
\textbf{
an arbitrarily long nonvanishing supplier germ}.
}
}
\tag{16.2}
$$

This does not automatically give a full ancient Navier--Stokes profile because full-state local compactness is still required.

But temporal disappearance is no longer possible.

---

# 17. Bounded-duration bounded-relative parent atom

Assume:

$$
L_Q[I]
\le
L_\ast,
$$

and a fixed bounded-relative high--high parent index

$$
p
$$

with:

$$
|p-Q|\le M_\ast
$$

satisfies:

$$
\boxed{
\lambda_Q
\int_I
\mathcal T_{Q,p}^{HH}(t)
dt
\ge
\eta\nu^2.
}
\tag{17.1}
$$

A standard Bernstein estimate gives:

$$
\left|
\mathcal T_{Q,p}^{HH}
\right|
\le
C
\lambda_Q
\lambda_p^{3/2}
B_p(t)^2
\|u_Q(t)\|_2,
$$

where:

$$
B_p(t)^2
=
\sum_{|r-p|\le1}
\|u_r(t)\|_2^2.
$$

On the crossing interval:

$$
\|u_Q\|_2
\le
C\nu\lambda_Q^{-1/2}.
$$

Since:

$$
|p-Q|\le M_\ast,
$$

$$
\lambda_p
\asymp_{M_\ast}
\lambda_Q.
$$

Therefore:

$$
\lambda_Q
\left|
\mathcal T_{Q,p}^{HH}
\right|
\le
C(M_\ast)
\nu
\lambda_Q^3
B_p(t)^2.
$$

Integrating and using (17.1):

$$
\int_I
B_p(t)^2dt
\ge
c(M_\ast)
\eta
\nu
\lambda_Q^{-3}.
$$

But:

$$
|I|
\le
\frac{
L_\ast
}{
\nu\lambda_Q^2
}.
$$

Hence for some:

$$
t_\ast\in I,
$$

$$
B_p(t_\ast)^2
\ge
c(M_\ast)
\frac{
\eta\nu^2
}{
L_\ast
}
\lambda_Q^{-1}.
$$

Since the cluster contains finitely many shells, some:

$$
r
$$

with:

$$
|r-p|\le1
$$

satisfies:

$$
\boxed{
\lambda_r
\|u_r(t_\ast)\|_2^2
\ge
c(M_\ast,L_\ast)
\eta\nu^2.
}
\tag{17.2}
$$

Thus:

$$
\boxed{
\textbf{
bounded duration}
+
\textbf{
bounded-relative positive HH flux}
\Longrightarrow
\textbf{
a genuine critical parent shell atom}.
}
}
\tag{17.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. Combined parent-or-defect theorem

The previous sections can be assembled into the following structural result.

## Theorem 18.1

Let:

$$
I_n=[r_n,s_n]
$$

be the first-crossing intervals of Theorem 6.1.

Then after subsequence extraction, at least one of the following occurs.

### A. Positive low-mode shear debt

$$
\boxed{
\int_{I_n}
\|\nabla u_{\le Q_n+C}\|_\infty
dt
\ge
c>0.
}
\tag{18.1}
$$

### B. Near-scale critical cluster

There are times:

$$
t_n^\ast\in I_n
$$

with:

$$
\boxed{
\lambda_{Q_n}
\sum_{|p-Q_n|\le C}
\|u_p(t_n^\ast)\|_2^2
\ge
c\nu^2.
}
\tag{18.2}
$$

### C. Critical bounded-relative HH parent atom

There exist:

$$
p_n-Q_n=O(1)
$$

and:

$$
t_n^\ast\in I_n
$$

such that:

$$
\boxed{
\lambda_{p_n}
\|u_{p_n}(t_n^\ast)\|_2^2
\ge
c\nu^2.
}
\tag{18.3}
$$

### D. Divergent derivative occupancy defect

For some:

$$
M_n\to\infty,
$$

$$
\boxed{
\mathfrak W_{Q_n,M_n}[I_n]
\to\infty.
}
\tag{18.4}
$$

### E. Long normalized supplier germ

$$
\boxed{
\nu
\lambda_{Q_n}^2
|I_n|
\to\infty,
}
\tag{18.5}
$$

while:

$$
\boxed{
\alpha
<
\lambda_{Q_n}
\|u_{Q_n}(t)\|_2^2
<
\beta
}
\tag{18.6}
$$

throughout:

$$
I_n.
$$

### Proof status

The theorem is obtained by:

1. the first-crossing positive flux theorem;
2. the signed

$$
LH/HL/HH
$$

decomposition;
3. the low--high commutator dichotomy;
4. the remote

$$
HH
$$

occupancy barrier;
5. the bounded-duration bounded-relative parent estimate.

Status:

$$
\boxed{
\textbf{PROVED as a structural alternative under the standard LP/Bony estimates stated above}.
}
$$

---

# 19. What this means for MORP

MORP zero-cost minimality requires simultaneous saturation of:

$$
\mathsf O_{\rm PFET}=0,
$$

$$
\mathsf{Paid}=0,
$$

and:

$$
\mathsf R_{\rm nat}=0,
$$

together with the remaining mechanism kernels.

Theorem 6.1 now supplies an unavoidable actual near-horizon kinetic-energy transfer:

$$
\boxed{
\Phi_{Q_n}
\ge
c\nu^2.
}
\tag{19.1}
$$

This quantity is not a dangerous certificate.

It is a direct signed energy balance of the actual Navier--Stokes shell.

Therefore the remaining compatibility question is extremely concrete:

$$
\boxed{
\textbf{
does the existing PFET / paid / native-residual compiler retain
a positive scale-critical shell-energy transfer event?
}
}
\tag{19.2}
$$

One must not answer this by definition.

It has to be proved from the actual PFET observable / finite-window compiler.

If yes, the zero-cost minimal recurrent obstruction is immediately incompatible with Theorem 6.1.

If no, the exact visibility gap is now identified:

$$
\boxed{
\text{spectral shell transfer}
\longrightarrow
\text{PFET / paid visibility}.
}
$$

---

# 20. Why this is stronger than "there is a parent"

The parent-extraction approach alone risks an infinite regress:

$$
\text{supplier}
\leftarrow
\text{parent}
\leftarrow
\text{parent of parent}
\leftarrow
\cdots
$$

The first-crossing theorem changes the target.

Regardless of which individual parent pays, the shell itself must receive:

$$
\boxed{
\text{fixed positive net critical energy transfer}.
}
$$

So the closure problem can potentially terminate at the **flux event itself**, without identifying a unique parent profile.

Parent localization remains useful only if the existing paid ledger fails to see the flux directly.

This is a major proof-routing simplification.

---

# 21. External source calibration

Cheskidov--Dai's Littlewood--Paley argument explicitly uses:

- Bony paraproduct;
- commutator estimates;
- dissipation-wavenumber splitting;
- absorption of high-frequency nonlinear terms by viscosity;
- low-mode activity:

$$
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty.
$$

Their Lemma 3.2 states for the pure velocity flux:

$$
|I|
\lesssim
c_r\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
f(t)
\sum_q
\lambda_q^{2s}
\|u_q\|_2^2
$$

for every:

$$
s>0
$$

and:

$$
r\ge2.
$$

This external result supports the low--high shear / high-frequency absorption geometry used in the present checkpoint.

DCRP-10's first-crossing flux theorem itself follows directly from the exact shell energy identity and does not depend on Cheskidov--Dai's theorem.

No novelty / priority claim is made for standard Littlewood--Paley commutator estimates.

---

# 22. End state

DCRP-09 established:

$$
\boxed{
\text{critical supplier atom}
\Longrightarrow
\text{actual same-history nonlinear source ancestry}.
}
$$

DCRP-10 strengthens this to:

$$
\boxed{
\textbf{
hypothetical singularity}
\Longrightarrow
\textbf{
arbitrarily high near-horizon positive scale-critical shell-energy transfer events}.
}
$$

Quantitatively:

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)
dt
\ge
c\nu^2.
}
$$

The signed triadic analysis further yields:

$$
\boxed{
\text{positive low-mode shear debt}
\vee
\text{critical parent atom}
\vee
\text{divergent derivative occupancy}
\vee
\text{long supplier germ}.
}
$$

The next proof target is no longer generic parent extraction.

It is:

$$
\boxed{
\textbf{
Spectral-Flux / PFET Compatibility Lemma}.
}
$$

Desired statement:

> Every first-crossing shell event satisfying
>
> $$
> \lambda_Q
> \int_I
> \mathcal T_Q\,dt
> \ge
> c\nu^2
> $$
>
> must produce either:
>
> $$
> \mathsf O_{\rm PFET}>0,
> $$
>
> $$
> \mathsf{Paid}>0,
> $$
>
> or:
>
> $$
> \mathsf R_{\rm nat}>0.
> $$

If this compatibility lemma is established for the existing MORP compiler, the zero-cost minimal obstruction cannot contain the supplier mechanism.

That is now the single closure-facing frontier.
