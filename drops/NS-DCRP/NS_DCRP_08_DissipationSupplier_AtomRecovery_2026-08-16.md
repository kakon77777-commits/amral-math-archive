# NS-DCRP-08 — Dissipation-Wavenumber Supplier Atom Recovery and the UV Supply Bridge

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: continue DCRP-07 by bridging a derivative-dominant ultraviolet tail back to a lower-order, scale-critical, state-visible supplier shell.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies: MORP-02 through MORP-05, DCRP-05 through DCRP-07.
- principal external primary source: Alexey Cheskidov and Mimi Dai, arXiv:1507.06611v6.
- secondary calibration: Cheskidov--Shvydkoy, arXiv:1102.1944.

---

# 1. Executive result

DCRP-07 proved that a derivative-dominant ultraviolet tail may satisfy

$$
K_{\rm UV}\to0,
\qquad
E_{\rm UV}\to0,
\qquad
H_{\rm UV}\to0,
$$

while

$$
\frac{Z_{\rm UV}^2}{Z^2}\to1.
$$

Thus lower-order raw mass alone cannot see the final tail.

The present round shows that this does **not** mean the ultraviolet derivative tail can be dynamically supplied without a lower-order critical atom.

Let

$$
u_q=\Delta_q u,
\qquad
\lambda_q=2^q,
$$

and define the Navier--Stokes dissipation wavenumber in the $r=\infty$ form

$$
\boxed{
\Lambda(t)
=
\lambda_{Q(t)}
=
\min
\left\{
\lambda_q:
\lambda_p^{-1}
\|u_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{1.1}
$$

For every smooth nontrivial state with

$$
1<\Lambda(t)<\infty,
$$

minimality gives the exact boundary lower bound

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t).
}
\tag{1.2}
$$

Bernstein therefore yields

$$
\boxed{
\Lambda(t)
\|u_{Q(t)}(t)\|_2^2
\ge
c_1\nu^2.
}
\tag{1.3}
$$

The quantity

$$
\lambda_q\|u_q\|_2^2
$$

is scale critical in three dimensions.

After rescaling the $Q$-shell to unit frequency,

$$
v_Q(y)
=
\Lambda^{-1}
u_Q
\left(
x_0+\Lambda^{-1}y
\right),
$$

one obtains

$$
\boxed{
\|v_Q\|_\infty
\ge
c_0\nu,
}
\tag{1.4}
$$

and

$$
\boxed{
\|v_Q\|_2^2
=
\Lambda
\|u_Q\|_2^2
\ge
c_1\nu^2.
}
\tag{1.5}
$$

After translating to a point of almost maximal amplitude, band limitation gives a fixed-radius local lower bound

$$
\boxed{
\int_{B_{r_0}}
|v_Q(y)|^2\,dy
\ge
c_2\nu^2.
}
\tag{1.6}
$$

Thus the dissipation-boundary supplier shell is a genuine nonvanishing state-visible object after its natural critical rescaling.

The second part of the result uses Cheskidov--Dai's Littlewood--Paley flux estimate. For the Navier--Stokes equation and any

$$
s>\frac12,
$$

in particular

$$
s=2,
$$

the nonlinear $H^s$ flux satisfies schematically

$$
\boxed{
|I_s|
\le
c_3\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
C f(t)
\sum_q
\lambda_q^{2s}
\|u_q\|_2^2,
}
\tag{1.7}
$$

where

$$
\boxed{
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty.
}
\tag{1.8}
$$

The first term is absorbed by viscosity when the defining constant of the dissipation wavenumber is chosen sufficiently small.

Hence the high derivative norm is not self-funded above the dissipation boundary:

$$
\boxed{
\frac d{dt}
\|u\|_{H^2}^2
\le
C f(t)
\|u\|_{H^2}^2.
}
\tag{1.9}
$$

For an actual concentrating return with

$$
H_{\rm out}
=
\Gamma^3H_{\rm in},
\qquad
\Gamma>1,
$$

one therefore obtains the scale-invariant supplier-activity debt

$$
\boxed{
\int_a^b
f(t)\,dt
\ge
c_4\log\Gamma.
}
\tag{1.10}
$$

The main structural conclusion is:

$$
\boxed{
\textbf{
a derivative-dominant UV tail may lose raw lower-order mass,
but it cannot simultaneously lose its scale-critical supplier atom
and its low-mode supplier activity.
}
}
$$

The remaining bridge is now causal/compactness-based:

> show that the recovered dissipation-boundary supplier atom belongs to the same actual singular return chain and therefore either re-profiles under MORP or leaves a nonzero native transition/escape residual.

---

# 2. Dissipation wavenumber

For a smooth Navier--Stokes state define

$$
\Lambda(t)
=
\lambda_{Q(t)}
$$

by

$$
\boxed{
\Lambda(t)
=
\min
\left\{
\lambda_q:
\lambda_p^{-1}
\|u_p(t)\|_\infty
<
c_0\nu
\quad
\forall p>q
\right\}.
}
\tag{2.1}
$$

This is the

$$
r=\infty
$$

specialization of the Cheskidov--Dai dissipation wavenumber.

For a smooth state the dyadic amplitudes decay faster than every power at high frequency, so

$$
\Lambda(t)<\infty.
$$

The region

$$
p>Q(t)
$$

is the dissipation range in the sense that the high-frequency nonlinear contributions are small enough to be absorbed into the viscous term.

---

# 3. Boundary shell lower bound

Cheskidov--Dai record directly that if

$$
1<\Lambda(t)<\infty,
$$

then

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu
\Lambda(t)
}
\tag{3.1}
$$

for the Navier--Stokes

$$
r=\infty
$$

case.

This follows from minimality of

$$
Q(t).
$$

Indeed, if the boundary shell and every shell above it all satisfied the strict high-frequency smallness condition at the previous dyadic cutoff, then

$$
Q(t)
$$

would not be minimal.

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE ESTABLISHED}.
}
$$

---

# 4. NEW THEOREM — critical kinetic supplier atom

## Theorem 4.1

At every smooth time with

$$
1<\Lambda(t)<\infty,
$$

the dissipation-boundary shell satisfies

$$
\boxed{
\Lambda(t)
\|u_{Q(t)}(t)\|_2^2
\ge
c_1\nu^2.
}
\tag{4.1}
$$

### Proof

Bernstein gives

$$
\|u_Q\|_\infty
\le
C_B
\Lambda^{3/2}
\|u_Q\|_2.
$$

By (3.1),

$$
c_0\nu\Lambda
\le
C_B
\Lambda^{3/2}
\|u_Q\|_2.
$$

Hence

$$
\|u_Q\|_2
\ge
\frac{c_0}{C_B}
\nu
\Lambda^{-1/2}.
$$

Squaring and multiplying by

$$
\Lambda
$$

gives

$$
\Lambda
\|u_Q\|_2^2
\ge
\frac{c_0^2}{C_B^2}
\nu^2.
$$

Set

$$
c_1
=
\frac{c_0^2}{C_B^2}.
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

# 5. Scale invariance of the supplier atom

Under Navier--Stokes scaling

$$
u_a(x,t)
=
a
u(ax,a^2t),
$$

a dyadic shell at frequency

$$
\lambda_q
$$

moves to frequency

$$
a\lambda_q.
$$

The shell

$$
L^2
$$

norm obeys

$$
\|(u_a)_{q+\log_2a}\|_2^2
=
a^{-1}
\|u_q\|_2^2
$$

up to the standard bounded dyadic-index ambiguity.

Therefore

$$
(a\lambda_q)
\left[
a^{-1}
\|u_q\|_2^2
\right]
=
\lambda_q
\|u_q\|_2^2.
$$

Thus

$$
\boxed{
\lambda_q\|u_q\|_2^2
}
\tag{5.1}
$$

is parabolic-scale invariant.

The lower bound (4.1) is therefore an intrinsic critical amplitude statement, not a raw-energy statement.

---

# 6. NEW THEOREM — unit-frequency supplier recovery

Let

$$
\Lambda
=
\lambda_Q.
$$

Define the critically rescaled boundary shell

$$
\boxed{
v_Q(y)
=
\Lambda^{-1}
u_Q
\left(
x_0+\Lambda^{-1}y
\right).
}
\tag{6.1}
$$

The Fourier support of

$$
v_Q
$$

lies in a fixed annulus

$$
c\le|\eta|\le C
$$

independent of

$$
Q.
$$

## Theorem 6.1

There exists a translation

$$
x_0
$$

such that

$$
\boxed{
\|v_Q\|_\infty
\ge
c_0\nu,
}
\tag{6.2}
$$

$$
\boxed{
\|v_Q\|_2^2
\ge
c_1\nu^2,
}
\tag{6.3}
$$

and for universal

$$
r_0,c_2>0,
$$

$$
\boxed{
\int_{B_{r_0}(0)}
|v_Q(y)|^2\,dy
\ge
c_2\nu^2.
}
\tag{6.4}
$$

### Proof

From (3.1),

$$
\|v_Q\|_\infty
=
\Lambda^{-1}
\|u_Q\|_\infty
\ge
c_0\nu.
$$

Also:

$$
\|v_Q\|_2^2
=
\Lambda
\|u_Q\|_2^2
\ge
c_1\nu^2.
$$

Let

$$
M
=
\|v_Q\|_\infty.
$$

Choose

$$
y_0
$$

with

$$
|v_Q(y_0)|
\ge
\frac34M.
$$

Translate so that

$$
y_0=0.
$$

Because

$$
v_Q
$$

is supported in a fixed Fourier annulus, Bernstein gives

$$
\|\nabla v_Q\|_\infty
\le
C_0M.
$$

Choose

$$
r_0
=
\frac1{4C_0}.
$$

Then for

$$
|y|\le r_0,
$$

$$
|v_Q(y)-v_Q(0)|
\le
C_0Mr_0
\le
\frac14M.
$$

Therefore

$$
|v_Q(y)|
\ge
\frac12M
\ge
\frac{c_0}{2}\nu
$$

throughout

$$
B_{r_0}.
$$

Hence

$$
\int_{B_{r_0}}
|v_Q|^2
\ge
|B_{r_0}|
\frac{c_0^2}{4}
\nu^2.
$$

Set

$$
c_2
=
|B_{r_0}|
\frac{c_0^2}{4}.
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

# 7. Interpretation — the supplier is not a vanishing profile

DCRP-07 showed that the derivative-dominant tail itself can have

$$
K_{\rm UV},
E_{\rm UV},
H_{\rm UV}
\to0
$$

while carrying almost all of

$$
Z^2.
$$

Theorem 6.1 shows that the dynamically defined dissipation-boundary supplier behaves differently.

After scaling to its own natural frequency:

$$
\boxed{
\text{supplier shell}
\Longrightarrow
\text{fixed local }L^2\text{ amplitude}.
}
$$

Thus:

$$
\boxed{
\textbf{
derivative invisibility does not imply supplier invisibility.
}
}
\tag{7.1}
$$

The high derivative tail may be lower-order invisible **at its own UV location**, but the nonlinear/viscous interface that permits such a tail contains a scale-critical lower-order atom.

---

# 8. Compactness dichotomy at the supplier scale

Consider a sequence of times

$$
t_n\uparrow T
$$

with

$$
\Lambda_n
=
\Lambda(t_n)
\to\infty.
$$

Let

$$
v_n
$$

be the full state rescaled to the supplier scale

$$
\Lambda_n^{-1},
$$

translated according to Theorem 6.1.

Its unit shell component satisfies

$$
\boxed{
\int_{B_{r_0}}
|P_{\sim1}v_n|^2
\ge
c_2\nu^2.
}
\tag{8.1}
$$

There are now only two possibilities.

## Compact supplier branch

If the rescaled full states have a uniform local compactness bound strong enough to pass the fixed Littlewood--Paley shell, then after subsequence extraction

$$
v_n\to v_\ast
$$

locally in a topology for which

$$
P_{\sim1}v_n\to P_{\sim1}v_\ast
$$

strongly in

$$
L^2(B_{r_0}),
$$

and therefore

$$
\boxed{
P_{\sim1}v_\ast\ne0.
}
\tag{8.2}
$$

This gives a genuine nonzero state-visible reprofile.

## Noncompact supplier branch

If no such local compactness is available, then the supplier scale itself produces an explicit state compactness / amplitude / tail defect.

Therefore the supplier cannot disappear silently.

Status:

$$
\boxed{
\textbf{CONDITIONAL REPROFILE DICHOTOMY}.
}
$$

The missing condition is precisely the local compactness transfer for the full state at the supplier scale.

---

# 9. Cheskidov--Dai high-frequency flux estimate

For the Navier--Stokes equation, Cheskidov--Dai derive for any

$$
s>\frac12
$$

an

$$
H^s
$$

energy estimate based on the dissipation wavenumber.

Define

$$
\boxed{
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty.
}
\tag{9.1}
$$

Their Bony/commutator estimate for the nonlinear velocity flux gives, schematically,

$$
\boxed{
|I_s|
\le
C_1c_0\nu
\sum_{q>Q-3}
\lambda_q^{2s+2}
\|u_q\|_2^2
+
C_2f(t)
\sum_q
\lambda_q^{2s}
\|u_q\|_2^2.
}
\tag{9.2}
$$

For the Navier--Stokes case they allow every

$$
s>\frac12.
$$

Choose

$$
s=2.
$$

Then:

$$
\boxed{
|I_2|
\le
C_1c_0\nu
\sum_{q>Q-3}
\lambda_q^{6}
\|u_q\|_2^2
+
C_2f(t)
\sum_q
\lambda_q^{4}
\|u_q\|_2^2.
}
\tag{9.3}
$$

If

$$
c_0
$$

is chosen sufficiently small, the first term is absorbed by the viscous

$$
H^3
$$

dissipation.

Thus:

$$
\boxed{
\frac d{dt}
\sum_q
\lambda_q^4
\|u_q\|_2^2
\le
C f(t)
\sum_q
\lambda_q^4
\|u_q\|_2^2.
}
\tag{9.4}
$$

This is the frequency-localized counterpart of the global

$$
H^2
$$

interaction estimate in DCRP-07.

Status:

$$
\boxed{
\textbf{PRIMARY-SOURCE ESTABLISHED modulo equivalent Littlewood--Paley norm constants}.
}
$$

---

# 10. Supplier interpretation of the flux estimate

Equation (9.3) has a structural meaning.

Above

$$
Q(t),
$$

the high-frequency self-interaction contribution is small enough to be absorbed by viscosity.

The remaining non-absorbable growth is controlled by

$$
f(t),
$$

which contains only modes

$$
q\le Q(t).
$$

Thus:

$$
\boxed{
\textbf{
the high derivative range is not self-sustaining above the dissipation wavenumber;
its non-absorbable growth is mediated by the supplier side }q\le Q(t).
}
}
\tag{10.1}
$$

This provides the desired qualitative low--high bridge.

It does not yet identify one unique triadic causal path from

$$
u_Q
$$

to the derivative tail.

That stronger causal assignment remains open.

---

# 11. NEW THEOREM — supplier activity debt for a scale return

Define the dyadic

$$
H^2
$$

energy

$$
\boxed{
\mathcal H_2(t)
=
\sum_q
\lambda_q^4
\|u_q(t)\|_2^2.
}
\tag{11.1}
$$

It is equivalent to

$$
\|u(t)\|_{\dot H^2}^2,
$$

and hence to the strain quantity

$$
H(t)
=
\|S(t)\|_{\dot H^1}^2
$$

up to universal constants.

Suppose an actual forward concentrating return satisfies an exact physical scale gain

$$
\boxed{
\mathcal H_2(b)
=
\Gamma^3
\mathcal H_2(a),
\qquad
\Gamma>1.
}
\tag{11.2}
$$

Then:

$$
\boxed{
\int_a^b
f(t)\,dt
\ge
c_4
\log\Gamma.
}
\tag{11.3}
$$

### Proof

Equation (9.4) gives

$$
\frac d{dt}
\log\mathcal H_2(t)
\le
Cf(t)
$$

whenever

$$
\mathcal H_2>0.
$$

Integrating:

$$
\log
\frac{
\mathcal H_2(b)
}{
\mathcal H_2(a)
}
\le
C
\int_a^b
f(t)\,dt.
$$

Using (11.2):

$$
3\log\Gamma
\le
C
\int_a^b
f(t)\,dt.
$$

Hence:

$$
\boxed{
\int_a^b
f(t)\,dt
\ge
\frac3C
\log\Gamma.
}
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED assuming the exact return gain and the Cheskidov--Dai }s=2\textbf{ estimate}.
}
$$

---

# 12. Scale invariance of supplier activity

Each summand

$$
\lambda_q
\|u_q\|_\infty
$$

has physical dimension

$$
{\rm time}^{-1}.
$$

Under Navier--Stokes scaling

$$
u_a(x,t)
=
a
u(ax,a^2t),
$$

it transforms as

$$
\lambda_q
\|u_q\|_\infty
\mapsto
a^2
\lambda_q
\|u_q\|_\infty
$$

after the corresponding dyadic index shift.

Since

$$
dt\mapsto a^{-2}dt,
$$

the integral

$$
\boxed{
\int
f(t)\,dt
}
\tag{12.1}
$$

is scale invariant up to bounded dyadic partition constants.

Thus (11.3) is a genuine critical return cost.

---

# 13. NEW THEOREM — hypothetical blowup forces unbounded supplier frequency

Let

$$
u
$$

be a maximal smooth / strong solution on

$$
[0,T_{\max}),
$$

and suppose

$$
T_{\max}<\infty.
$$

Then:

$$
\boxed{
\limsup_{t\uparrow T_{\max}}
\Lambda(t)
=
+\infty.
}
\tag{13.1}
$$

### Proof

Assume instead that

$$
\Lambda(t)
\le\Lambda_0
$$

for all sufficiently late

$$
t.
$$

Then

$$
Q(t)\le Q_0
$$

for a fixed integer

$$
Q_0.
$$

Using Bernstein and the global kinetic-energy bound

$$
\|u(t)\|_2
\le
\|u(0)\|_2,
$$

for every fixed

$$
q\le Q_0,
$$

$$
\lambda_q
\|u_q(t)\|_\infty
\le
C
\lambda_q^{5/2}
\|u(0)\|_2.
$$

Therefore

$$
f(t)
=
\sum_{q\le Q(t)}
\lambda_q
\|u_q(t)\|_\infty
\le
C(Q_0,\|u(0)\|_2)
$$

uniformly near

$$
T_{\max}.
$$

Apply the Cheskidov--Dai estimate with

$$
s=2:
$$

$$
\frac d{dt}
\|u(t)\|_{H^2}^2
\le
C f(t)
\|u(t)\|_{H^2}^2.
$$

Gronwall gives a uniform

$$
H^2
$$

bound up to

$$
T_{\max}.
$$

Such a bound continues the strong Navier--Stokes solution beyond

$$
T_{\max},
$$

contradiction.

Hence

$$
\Lambda(t)
$$

must be unbounded.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED in the standard strong-solution continuation class}.
}
$$

---

# 14. Corollary — arbitrarily high critical supplier atoms

From Theorem 13.1, any hypothetical finite-time singularity admits times

$$
t_n\uparrow T_{\max}
$$

with

$$
\Lambda_n
=
\Lambda(t_n)
\to\infty.
$$

At each such time, Theorem 4.1 gives

$$
\boxed{
\Lambda_n
\|u_{Q_n}(t_n)\|_2^2
\ge
c_1\nu^2.
}
\tag{14.1}
$$

and Theorem 6.1 gives a critically rescaled translated shell with

$$
\boxed{
\int_{B_{r_0}}
|v_{Q_n}|^2
\ge
c_2\nu^2.
}
\tag{14.2}
$$

Therefore:

$$
\boxed{
\textbf{
finite-time blowup would require an unbounded sequence of
nonvanishing scale-critical supplier atoms.
}
}
\tag{14.3}
$$

This is a lower-order state-visible object at arbitrarily small physical scales.

---

# 15. Relation to the DCRP-07 derivative visibility no-go

DCRP-07 proved that an ultraviolet tail can have raw shell kinetic energy as small as

$$
K_{\rm UV}
\sim
N^{-5}
$$

while dominating

$$
Z^2.
$$

The present theorem does not contradict that construction.

Instead it says:

if such a derivative-dominant tail is part of an actual Navier--Stokes singular mechanism, then somewhere at the dynamically selected dissipation boundary there must also be a supplier shell with

$$
\boxed{
K_Q
\gtrsim
\nu^2
\Lambda^{-1}.
}
\tag{15.1}
$$

The raw energy

$$
K_Q
$$

still tends to zero as

$$
\Lambda\to\infty.
$$

That is exactly critical scaling.

After renormalization:

$$
\boxed{
\Lambda K_Q
\gtrsim\nu^2.
}
\tag{15.2}
$$

Thus the old raw-summability obstruction remains true, but the reprofile obstruction is stronger:

$$
\boxed{
\text{critical supplier atom does not vanish under its own scale normalization}.
}
$$

---

# 16. Atomic supplier versus diffuse derivative tail

The final state-visible picture is now asymmetric.

The extreme derivative tail may be diffuse in

$$
\mu_Z
$$

or may carry only vanishing base mass.

But the dissipation boundary itself carries an atomic critical lower-order state:

$$
\boxed{
\lambda_Q\|u_Q\|_2^2
\gtrsim\nu^2.
}
$$

Hence a surviving singular mechanism has the form

$$
\boxed{
\text{critical supplier atom}
\longrightarrow
\text{possibly diffuse derivative UV tail}.
}
\tag{16.1}
$$

The remaining mathematical question is no longer whether a lower-order atom exists.

It does.

The question is whether that supplier atom can fail to enter the same compact / causal return object used by MORP.

---

# 17. Connection to MORP atomic reprofile

MORP-05 proves schematically:

$$
\text{fixed-share atom}
\Longrightarrow
\text{recenter}
+
\text{rescale}
+
\text{extract nonzero profile}.
$$

Theorem 6.1 supplies exactly the first two analytic ingredients for the dissipation-boundary shell:

- natural scale;
- natural spatial center;
- fixed local shell amplitude after critical rescaling.

Therefore a direct MORP-compatible closure would follow from:

$$
\boxed{
\textbf{Supplier Compactness Bridge}.
}
$$

Desired statement:

> Along an actual singular return chain, the full Navier--Stokes states normalized at the dissipation-boundary supplier scales satisfy the local compactness package required to pass the fixed unit shell.
>
> Then the uniform lower bound
>
> $$
> \int_{B_{r_0}}
> |P_{\sim1}v_n|^2
> \ge
> c\nu^2
> $$
>
> yields a nonzero actual state profile.

If the compactness package fails, that failure must be retained as a state/pressure/defect/escape coordinate.

This is a much narrower bridge than the previous generic UV Flux Bridge.

---

# 18. Supplier activity and the existing low-mode regularity criterion

The Cheskidov--Dai regularity criterion further shows that regularity is controlled by the time integral of low-mode vorticity activity below the dissipation wavenumber.

In the Navier--Stokes case, finite-time blowup requires the corresponding critical low-mode activity condition to fail.

Thus a hypothetical singularity has two simultaneous supplier signatures:

$$
\boxed{
\begin{aligned}
&\text{instantaneous critical atom at }Q(t),\\
&\text{nontrivial scale-invariant low-mode activity in time}.
\end{aligned}
}
\tag{18.1}
$$

This independently supports the conclusion that the UV derivative tail cannot be dynamically isolated from its lower-frequency supplier sector.

No claim is made that this regularity criterion alone proves global regularity.

---

# 19. What has been closed in this round

## Closed A — complete lower-order invisibility

It is false that an actual derivative-dominant singular mechanism may be invisible at **all** lower-order scales.

The dissipation boundary contains

$$
\boxed{
\Lambda\|u_Q\|_2^2
\ge
c\nu^2.
}
$$

## Closed B — vanishing supplier under critical re-scaling

After scaling the supplier shell to unit frequency and translating,

$$
\boxed{
\int_{B_{r_0}}
|v_Q|^2
\ge
c\nu^2.
}
$$

So the supplier shell cannot vanish as a normalized shell object.

## Closed C — purely self-funded UV derivative growth

Cheskidov--Dai's paraproduct estimate absorbs the high-frequency nonlinear contribution above the dissipation boundary and leaves growth controlled by the low-mode activity

$$
f(t).
$$

Therefore the non-absorbable derivative growth is supplier-mediated.

---

# 20. What remains open

The remaining gap is no longer a generic analytic flux inequality.

It is a **same-history compactness / causality bridge**.

One must prove that the recovered supplier shell belongs to the same actual singular mechanism that generated the derivative tail.

More specifically, at least one of the following must be established.

## Route A — actual supplier reprofile

The supplier-normalized full states have enough local compactness to extract a nonzero actual Navier--Stokes profile.

## Route B — supplier-to-UV causal edge

The low-mode activity

$$
f(t)
$$

that pays for derivative growth can be localized to an actual transition edge already represented in the MORP return/transition ledger.

## Route C — noncompactness is itself retained

Failure of Route A produces a nonzero native compactness / escape / pressure / derivative defect rather than disappearing.

The key point is:

$$
\boxed{
\text{the supplier cannot be both nonzero and absent from every completed package coordinate}.
}
$$

This last sentence is still a target, not yet a proved theorem.

---

# 21. Next exact target

The next proof target is:

$$
\boxed{
\textbf{Supplier Compactness--Causality Lemma}.
}
$$

A useful sufficient version is:

Let

$$
t_n\uparrow T_{\max}
$$

be singular-approach times with

$$
\Lambda_n\to\infty.
$$

Normalize and recenter the full state at the dissipation-boundary shell:

$$
v_n(y,s)
=
\Lambda_n^{-1}
u
\left(
x_n+\Lambda_n^{-1}y,
t_n+\Lambda_n^{-2}s
\right).
$$

The unit shell satisfies

$$
\int_{B_{r_0}}
|P_{\sim1}v_n(y,0)|^2\,dy
\ge
c\nu^2.
$$

Prove one of:

1. the full state sequence has a locally compact subsequence and the limit has

   $$
   P_{\sim1}v_\ast\ne0;
   $$

2. a specific MORP native defect coordinate is strictly positive;

3. the supplier scale cannot be causally connected to the derivative-growth return, in which case the Cheskidov--Dai low-mode flux estimate must be sharpened to identify the actual supplying shell/edge.

If (1) is proved on the minimal-return branch, MORP atomic reprofile applies.

If (2) is proved, zero-cost minimality fails.

Only (3) can continue to escape.

Thus the next frontier has been reduced to a causal localization problem.

---

# 22. Source ledger

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611v6.

Primary facts used:

- dissipation wavenumber

  $$
  \Lambda_r(t)
  =
  \min
  \left\{
  \lambda_q:
  \lambda_p^{-1+3/r}
  \|u_p\|_r
  <
  c_r\nu
  \quad
  \forall p>q
  \right\};
  $$

- for the Navier--Stokes case,

  $$
  r=\infty
  $$

  is allowed;

- boundary lower bound

  $$
  \|u_Q\|_\infty
  \ge
  c\nu\Lambda;
  $$

- low-mode activity

  $$
  f(t)
  =
  \sum_{q\le Q(t)}
  \lambda_q
  \|u_q(t)\|_\infty;
  $$

- for Navier--Stokes and any

  $$
  s>\frac12,
  $$

  the Littlewood--Paley nonlinear flux estimate absorbs the high-frequency contribution above the dissipation wavenumber and leaves an

  $$
  f(t)\|u\|_{H^s}^2
  $$

  growth term.

## Cheskidov--Shvydkoy

Alexey Cheskidov and Roman Shvydkoy, *A unified approach to regularity problems for the 3D Navier-Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944.

Used as conceptual calibration for the interpretation of the dissipation wavenumber as the boundary between Euler-dominated and viscosity-dominated frequency ranges.

No novelty / priority claim is made for the dissipation-wavenumber framework.

The supplier-atom and MORP bridge deductions are internal derivations and require independent audit.

---

# 23. End state

The UV Flux Bridge problem has been reduced.

The derivative-dominant tail itself can remain lower-order raw-mass invisible.

But the actual Navier--Stokes dissipation boundary necessarily satisfies

$$
\boxed{
\|u_Q\|_\infty
\gtrsim
\nu\Lambda,
}
$$

and

$$
\boxed{
\Lambda\|u_Q\|_2^2
\gtrsim
\nu^2.
}
$$

After critical rescaling and recentering,

$$
\boxed{
\int_{B_{r_0}}
|P_{\sim1}v|^2
\gtrsim
\nu^2.
}
$$

Furthermore, high derivative growth above the dissipation boundary is controlled by the low-mode supplier activity

$$
f(t).
$$

Therefore:

$$
\boxed{
\textbf{
the final UV escape has acquired a nonvanishing lower-order supplier atom.
}
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Supplier Compactness--Causality Lemma}.
}
$$

That is the next exact attack.
