# NS-DCRP-11 — Heat-Band PFET Compatibility, Forward/Backscatter Alternative, and the Final Localization Gap

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: bridge the positive first-crossing spectral shell flux from DCRP-10 to the already existing FCBP pressure--flux / paid-backscatter architecture without inventing a new physical detector.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-03 signed pressure--flux telescope;
  - FCBP-04 heat-semigroup coarse graining and co-moving heat pressure--flux ledger;
  - FCBP-05 combined pressure/flux/energy/trace observability;
  - FCBP-06 paid-side and combined-invisible audit;
  - MORP-01 through MORP-05;
  - DCRP-08 through DCRP-10.
- external primary calibration:
  - Runlong Yu, arXiv:2606.25322v1;
  - Cheskidov--Dai, arXiv:1507.06611v6.

---

# 1. Executive result

DCRP-10 proved that a hypothetical finite-time singularity forces arbitrarily high dyadic first-crossing events with

$$
\boxed{
\lambda_{Q_n}
\int_{r_n}^{s_n}
\mathcal T_{Q_n}(t)\,dt
\ge
c\nu^2.
}
\tag{1.1}
$$

This is a positive, scale-critical, signed kinetic-energy transfer into a Littlewood--Paley supplier shell.

The remaining question was whether this transfer must be visible to the already existing pressure--flux / paid-side ledgers.

A direct comparison between a Littlewood--Paley shell flux and the compact-mollifier PFET observable is unnecessarily difficult and filter-dependent.

The present round bypasses that mismatch.

Use instead the heat-semigroup coarse graining already constructed internally in FCBP-04:

$$
S_s
=
e^{s\Delta}.
$$

For fixed constants

$$
0<a<b,
$$

and a frequency

$$
\lambda>0,
$$

define the two comparable smoothing parameters

$$
s_a
=
a\lambda^{-2},
$$

$$
s_b
=
b\lambda^{-2}.
$$

Define the scale-critical heat-band energy

$$
\boxed{
\mathcal B_{\lambda}^{a,b}(t)
=
\frac{\lambda}{2}
\left(
\|e^{s_a\Delta}u(t)\|_2^2
-
\|e^{s_b\Delta}u(t)\|_2^2
\right).
}
\tag{1.2}
$$

Because

$$
b>a,
$$

the Fourier multiplier

$$
e^{-2a|\xi|^2/\lambda^2}
-
e^{-2b|\xi|^2/\lambda^2}
$$

is nonnegative.

If the Littlewood--Paley supplier shell at frequency

$$
\lambda_Q
$$

satisfies

$$
\lambda_Q
\|u_Q\|_2^2
\ge
\kappa_0\nu^2,
$$

then:

$$
\boxed{
\mathcal B_{\lambda_Q}^{a,b}
\ge
\kappa_{HB}\nu^2
}
\tag{1.3}
$$

for a universal

$$
\kappa_{HB}>0
$$

depending only on the fixed LP annulus and the fixed pair

$$
a<b.
$$

On every compact regular time interval before a first singular time,

$$
\mathcal B_{\lambda}^{a,b}(t)
\to0
$$

uniformly as

$$
\lambda\to\infty.
$$

Hence the heat-band energy itself has arbitrarily high first-crossing intervals approaching the singular horizon.

For a fixed heat filter

$$
S_s,
$$

let

$$
U^s
=
S_su,
$$

$$
R^s
=
S_s(u\otimes u)
-
U^s\otimes U^s,
$$

and

$$
\Pi^s
=
-
R^s:\nabla U^s.
$$

Define the whole-space resolved interscale work

$$
\boxed{
F_s(t)
=
\int_{\mathbb R^3}
\Pi^s(x,t)\,dx.
}
\tag{1.4}
$$

The exact whole-space heat-filter energy identity is

$$
\boxed{
\frac d{dt}
\frac12
\|U^s\|_2^2
+
\nu
\|\nabla U^s\|_2^2
+
F_s
=
0.
}
\tag{1.5}
$$

Subtracting the two heat-filter identities produces an exact heat-band balance.

If

$$
\mathcal B_{\lambda}^{a,b}
$$

rises by

$$
\delta\nu^2
$$

on an interval

$$
I,
$$

then:

$$
\boxed{
\lambda
\int_I
\left(
F_{s_b}
-
F_{s_a}
\right)
dt
\ge
\delta\nu^2.
}
\tag{1.6}
$$

Therefore:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
+
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\delta\nu^2.
}
\tag{1.7}
$$

Hence at least one of:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{1.8}
$$

or:

$$
\boxed{
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{1.9}
$$

must occur.

Interpretation:

- the coarser heat filter sees fixed positive **forward interscale work**;
- or the finer heat filter sees fixed positive **backscatter payment**.

These are precisely the two signs already present in the FCBP pressure--flux / paid-side architecture.

Thus:

$$
\boxed{
\textbf{
supplier first crossing}
\Longrightarrow
\textbf{
heat-PFET forward work}
\ \vee\
\textbf{
heat-Paid backscatter}.
}
}
\tag{1.10}
$$

No new physical mechanism is introduced.

The only remaining compatibility gap is spatial / window localization:

> the theorem above is a whole-space heat-filter work statement, whereas the MORP/finite-window PFET kernel is a local normalized package.

Thus the next target is now a single precise lemma:

$$
\boxed{
\textbf{Heat-Flux Localization / Package-Completion Lemma}.
}
$$

---

# 2. Internal PFET architecture audited

MORP-01 defines

$$
\mathsf O_{\rm PFET}(D)
$$

as combined pressure--flux--energy--trace visibility,

$$
\mathsf{Paid}(D)
$$

as normalized paid-side leakage/backscatter tax,

and:

$$
\mathsf R_{\rm nat}(D)
$$

as a retained native residual not already included in the previous channels.

The zero-cost minimal obstruction satisfies:

$$
\mathsf O_{\rm PFET}(D_\ast)=0,
$$

$$
\mathsf{Paid}(D_\ast)=0,
$$

and:

$$
\mathsf R_{\rm nat}(D_\ast)=0.
$$

FCBP-03 defines the signed coarse work distribution

$$
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell),
$$

with

$$
\Pi^\ell
=
-
R^\ell:\nabla U^\ell.
$$

Its signed telescope explicitly places negative work / backscatter on the paid side.

FCBP-04 separately develops heat-semigroup coarse graining:

$$
S_s=e^{s\Delta},
$$

and proves the corresponding exact coarse Navier--Stokes equation and heat pressure--flux ledger.

Therefore heat-filter interscale work is not an ad hoc DCRP observable.

It already belongs to the internal FCBP coarse-work architecture.

---

# 3. External PFET calibration

The external coarse-grained pressure--flux work theorem uses a nonnegative compactly supported smooth spatial mollifier.

For a spatial filter length

$$
\ell,
$$

it defines:

$$
U^\ell=S_\ell u,
$$

$$
P^\ell=S_\ell p,
$$

$$
R^\ell
=
S_\ell(u\otimes u)
-
U^\ell\otimes U^\ell,
$$

$$
\boxed{
\Pi^\ell
=
-
R^\ell:\nabla U^\ell,
}
\tag{3.1}
$$

and:

$$
\boxed{
G^\ell
=
\Pi^\ell
+
\nabla\cdot(P^\ell U^\ell).
}
\tag{3.2}
$$

Its localized normalized work is:

$$
\boxed{
\mathcal W_{I,r}[\phi]
=
r^{-1}
\int_I
\int
\left(
\phi\Pi^\ell
-
P^\ell U^\ell\cdot\nabla\phi
\right)
dxdt.
}
\tag{3.3}
$$

The external theorem proves an exact finite-chain energy/work telescope once a chosen local coarse-work signal is present.

It explicitly leaves the general coarse-observability implication open.

Thus the DCRP-11 result should not be described as a theorem that the external compact-mollifier active detector automatically sees the supplier event.

The current exact bridge is to the internal **heat-filter** pressure--flux / backscatter ledger.

---

# 4. Heat-band energy

Fix:

$$
0<a<b.
$$

Let:

$$
\lambda>0.
$$

Define:

$$
s_a
=
a\lambda^{-2},
$$

$$
s_b
=
b\lambda^{-2}.
$$

Set:

$$
U_a
=
e^{s_a\Delta}u,
$$

$$
U_b
=
e^{s_b\Delta}u.
$$

Define:

$$
\boxed{
\mathcal B_\lambda^{a,b}(t)
=
\frac{\lambda}{2}
\left(
\|U_a(t)\|_2^2
-
\|U_b(t)\|_2^2
\right).
}
\tag{4.1}
$$

By Plancherel:

$$
\mathcal B_\lambda^{a,b}
=
\frac{\lambda}{2}
\int_{\mathbb R^3}
m_{a,b}
\left(
\frac{
|\xi|
}{
\lambda
}
\right)
|\widehat u(\xi)|^2
d\xi,
$$

where:

$$
\boxed{
m_{a,b}(\rho)
=
e^{-2a\rho^2}
-
e^{-2b\rho^2}.
}
\tag{4.2}
$$

For:

$$
\rho>0,
$$

$$
m_{a,b}(\rho)>0.
$$

Thus:

$$
\boxed{
\mathcal B_\lambda^{a,b}\ge0.
}
\tag{4.3}
$$

---

# 5. Scale invariance

Under the Navier--Stokes scaling:

$$
u_c(x,t)
=
c
u(cx,c^2t),
$$

the frequency parameter transforms as:

$$
\lambda\mapsto c\lambda.
$$

The filtered

$$
L^2
$$

energy scales as:

$$
\|U\|_2^2
\mapsto
c^{-1}
\|U\|_2^2.
$$

Hence:

$$
(c\lambda)
\left(
c^{-1}
\|U\|_2^2
\right)
=
\lambda
\|U\|_2^2.
$$

Therefore:

$$
\boxed{
\mathcal B_\lambda^{a,b}
}
$$

is parabolic-scale invariant when the heat parameters are kept at fixed relative values:

$$
s_a=a\lambda^{-2},
\qquad
s_b=b\lambda^{-2}.
$$

---

# 6. NEW THEOREM — supplier shell forces nonzero heat-band energy

Let the Littlewood--Paley shell multiplier defining

$$
u_Q
$$

be supported in the fixed annulus:

$$
c_-\lambda_Q
\le
|\xi|
\le
c_+\lambda_Q,
$$

with:

$$
0<c_-<c_+<\infty.
$$

Let:

$$
|\varphi_Q(\xi)|\le1.
$$

Define:

$$
\boxed{
d_{a,b}
=
\min_{
c_-\le\rho\le c_+
}
m_{a,b}(\rho).
}
\tag{6.1}
$$

Because:

$$
m_{a,b}>0
$$

on:

$$
(0,\infty),
$$

$$
\boxed{
d_{a,b}>0.
}
\tag{6.2}
$$

## Theorem 6.1

If:

$$
\lambda_Q
\|u_Q(t)\|_2^2
\ge
\kappa_0\nu^2,
$$

then:

$$
\boxed{
\mathcal B_{\lambda_Q}^{a,b}(t)
\ge
\frac{
d_{a,b}\kappa_0
}{
2
}
\nu^2.
}
\tag{6.3}
$$

### Proof

On the support of:

$$
\varphi_Q,
$$

$$
m_{a,b}
\left(
\frac{|\xi|}{\lambda_Q}
\right)
\ge
d_{a,b}.
$$

Hence:

$$
\begin{aligned}
\mathcal B_{\lambda_Q}^{a,b}
&=
\frac{\lambda_Q}{2}
\int
m_{a,b}
\left(
\frac{|\xi|}{\lambda_Q}
\right)
|\widehat u|^2d\xi\\
&\ge
\frac{
d_{a,b}\lambda_Q
}{
2
}
\int_{\operatorname{supp}\varphi_Q}
|\widehat u|^2d\xi.
\end{aligned}
$$

Since:

$$
|\varphi_Q|\le1,
$$

$$
\int_{\operatorname{supp}\varphi_Q}
|\widehat u|^2
\ge
\int
|\varphi_Q\widehat u|^2
=
\|u_Q\|_2^2.
$$

Therefore:

$$
\mathcal B_{\lambda_Q}^{a,b}
\ge
\frac{
d_{a,b}
}{
2
}
\lambda_Q
\|u_Q\|_2^2.
$$

Apply the supplier lower bound.

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

# 7. High heat-band energy is absent on every regular compact time interval

The multiplier difference satisfies:

$$
0
\le
e^{-2ax}
-
e^{-2bx}
\le
2(b-a)x
$$

for:

$$
x\ge0.
$$

Therefore:

$$
m_{a,b}
\left(
\frac{|\xi|}{\lambda}
\right)
\le
2(b-a)
\frac{
|\xi|^2
}{
\lambda^2
}.
$$

Hence:

$$
\boxed{
\mathcal B_{\lambda}^{a,b}(t)
\le
(b-a)
\lambda^{-1}
\|\nabla u(t)\|_2^2.
}
\tag{7.1}
$$

If:

$$
T
$$

is a hypothetical first singular time, then for every:

$$
\varepsilon>0,
$$

the strong solution satisfies:

$$
\sup_{
0\le t\le T-\varepsilon
}
\|\nabla u(t)\|_2
<
\infty.
$$

Thus:

$$
\boxed{
\sup_{
0\le t\le T-\varepsilon
}
\mathcal B_{\lambda}^{a,b}(t)
\to0
\qquad
(\lambda\to\infty).
}
\tag{7.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 8. NEW THEOREM — heat-band first crossing

Let:

$$
t_n\uparrow T
$$

be the supplier times from DCRP-08 / DCRP-10, with:

$$
\lambda_n
=
\lambda_{Q_n}
\to\infty.
$$

By Theorem 6.1:

$$
\mathcal B_{\lambda_n}^{a,b}(t_n)
\ge
\kappa_{HB}\nu^2,
$$

where:

$$
\boxed{
\kappa_{HB}
=
\frac{
d_{a,b}\kappa_0
}{
2
}.
}
\tag{8.1}
$$

Choose:

$$
\alpha_{HB}
=
\frac14
\kappa_{HB}\nu^2,
$$

$$
\beta_{HB}
=
\frac12
\kappa_{HB}\nu^2.
$$

Then for all sufficiently large:

$$
n,
$$

there exist:

$$
\rho_n<\sigma_n<t_n
$$

such that:

$$
\boxed{
\rho_n,\sigma_n\to T,
}
\tag{8.2}
$$

$$
\boxed{
\mathcal B_{\lambda_n}^{a,b}(\rho_n)
=
\alpha_{HB},
}
\tag{8.3}
$$

$$
\boxed{
\mathcal B_{\lambda_n}^{a,b}(\sigma_n)
=
\beta_{HB},
}
\tag{8.4}
$$

and:

$$
\alpha_{HB}
<
\mathcal B_{\lambda_n}^{a,b}(t)
<
\beta_{HB}
$$

for:

$$
\rho_n<t<\sigma_n.
$$

### Proof

The proof is identical in structure to DCRP-10's shell first-crossing theorem.

Theorem 7.1 prevents level:

$$
\alpha_{HB}
$$

from being reached on any fixed compact subinterval before:

$$
T
$$

once:

$$
\lambda_n
$$

is sufficiently large.

The supplier lower bound places the endpoint above:

$$
2\beta_{HB}.
$$

Continuity gives the two crossing times.

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

# 9. Whole-space heat-filter energy identity

For fixed:

$$
s>0,
$$

define:

$$
U^s
=
e^{s\Delta}u,
$$

$$
P^s
=
e^{s\Delta}p,
$$

and:

$$
R^s
=
e^{s\Delta}(u\otimes u)
-
U^s\otimes U^s.
$$

The heat-filtered velocity satisfies:

$$
\partial_tU^s
-
\nu\Delta U^s
+
\nabla\cdot(U^s\otimes U^s)
+
\nabla P^s
=
-\nabla\cdot R^s.
$$

Define:

$$
\boxed{
\Pi^s
=
-
R^s:\nabla U^s.
}
\tag{9.1}
$$

For a smooth finite-energy whole-space solution, pair with:

$$
U^s
$$

and integrate over:

$$
\mathbb R^3.
$$

The resolved advection term vanishes by incompressibility.

The pressure term integrates to zero.

The Reynolds-stress term gives:

$$
\int
U^s\cdot
(-\nabla\cdot R^s)
dx
=
\int
R^s:\nabla U^s
dx
=
-
\int
\Pi^s dx.
$$

Therefore:

$$
\boxed{
\frac d{dt}
\frac12
\|U^s\|_2^2
+
\nu
\|\nabla U^s\|_2^2
+
F_s(t)
=
0,
}
\tag{9.2}
$$

where:

$$
\boxed{
F_s(t)
=
\int_{\mathbb R^3}
\Pi^s(x,t)\,dx.
}
\tag{9.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 10. Heat-band balance

For a fixed frequency:

$$
\lambda,
$$

set:

$$
s_a=a\lambda^{-2},
$$

$$
s_b=b\lambda^{-2}.
$$

Define:

$$
E_a(t)
=
\frac12
\|U^{s_a}(t)\|_2^2,
$$

$$
E_b(t)
=
\frac12
\|U^{s_b}(t)\|_2^2.
$$

Define:

$$
D_a(t)
=
\|\nabla U^{s_a}(t)\|_2^2,
$$

$$
D_b(t)
=
\|\nabla U^{s_b}(t)\|_2^2.
$$

Equation (9.2) gives:

$$
E_a'
+
\nu D_a
+
F_{s_a}
=
0,
$$

$$
E_b'
+
\nu D_b
+
F_{s_b}
=
0.
$$

Subtract:

$$
(E_a-E_b)'
+
\nu
(D_a-D_b)
+
F_{s_a}
-
F_{s_b}
=
0.
$$

Multiply by:

$$
\lambda:
$$

$$
\boxed{
\frac d{dt}
\mathcal B_\lambda^{a,b}
+
\nu\lambda
(D_a-D_b)
+
\lambda
(
F_{s_a}-F_{s_b}
)
=
0.
}
\tag{10.1}
$$

Because:

$$
s_a<s_b,
$$

the finer-filter dissipation is larger:

$$
\boxed{
D_a-D_b
\ge0.
}
\tag{10.2}
$$

This follows directly from the Fourier multipliers:

$$
|\xi|^2
e^{-2a|\xi|^2/\lambda^2}
\ge
|\xi|^2
e^{-2b|\xi|^2/\lambda^2}.
$$

---

# 11. NEW THEOREM — Heat-Band PFET / Paid Alternative

## Theorem 11.1

Suppose on an interval:

$$
I=[\rho,\sigma]
$$

the heat-band energy satisfies:

$$
\mathcal B_\lambda^{a,b}(\sigma)
-
\mathcal B_\lambda^{a,b}(\rho)
=
\delta\nu^2,
$$

with:

$$
\delta>0.
$$

Then:

$$
\boxed{
\lambda
\int_I
\left(
F_{s_b}
-
F_{s_a}
\right)
dt
\ge
\delta\nu^2.
}
\tag{11.1}
$$

Consequently:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
+
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\delta\nu^2.
}
\tag{11.2}
$$

Hence at least one of:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{11.3}
$$

or:

$$
\boxed{
\lambda
\int_I
(F_{s_a})_-
dt
\ge
\frac{\delta}{2}\nu^2
}
\tag{11.4}
$$

holds.

### Proof

Integrate (10.1):

$$
\delta\nu^2
+
\nu\lambda
\int_I
(D_a-D_b)
dt
+
\lambda
\int_I
(F_{s_a}-F_{s_b})
dt
=
0.
$$

Therefore:

$$
\lambda
\int_I
(F_{s_b}-F_{s_a})
dt
=
\delta\nu^2
+
\nu\lambda
\int_I
(D_a-D_b)
dt.
$$

By (10.2), the final term is nonnegative.

Thus (11.1) follows.

Next:

$$
F_{s_b}-F_{s_a}
\le
(F_{s_b})_+
+
(F_{s_a})_-.
$$

Integrate and multiply by:

$$
\lambda.
$$

This proves (11.2).

If both terms in (11.2) were less than:

$$
\frac{\delta}{2}\nu^2,
$$

their sum would be less than:

$$
\delta\nu^2,
$$

a contradiction.

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

# 12. Corollary — arbitrarily high heat-PFET / paid events

Apply Theorem 11.1 to the first-crossing intervals:

$$
I_n
=
[\rho_n,\sigma_n].
$$

Here:

$$
\delta
=
\frac{
\kappa_{HB}
}{
4
}.
$$

Therefore for every sufficiently large:

$$
n,
$$

either:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{b,n})_+
dt
\ge
c_{HB}\nu^2
}
\tag{12.1}
$$

or:

$$
\boxed{
\lambda_n
\int_{I_n}
(F_{a,n})_-
dt
\ge
c_{HB}\nu^2,
}
\tag{12.2}
$$

where:

$$
F_{a,n}
=
F_{
a\lambda_n^{-2}
},
$$

$$
F_{b,n}
=
F_{
b\lambda_n^{-2}
},
$$

and:

$$
c_{HB}>0
$$

is universal for the fixed filter parameters and LP decomposition.

Thus a hypothetical finite-time singularity produces arbitrarily high, near-horizon, scale-critical events of one of the two forms:

$$
\boxed{
\text{forward heat-filter interscale work}
}
$$

or:

$$
\boxed{
\text{heat-filter backscatter}.
}
$$

---

# 13. PFET / paid interpretation

For the coarser filter:

$$
s_b,
$$

positive:

$$
F_{s_b}
$$

means resolved kinetic energy is transferred forward into the unresolved scales.

This is the same physical sign as the forward coarse flux:

$$
\Pi^\ell>0
$$

in the FCBP / external pressure--flux ledger.

For the finer filter:

$$
s_a,
$$

negative:

$$
F_{s_a}
$$

is backscatter from unresolved to resolved scales.

FCBP-03 / FCBP-05 / FCBP-06 already place persistent negative combined work / backscatter on the explicitly paid side.

Therefore Theorem 11.1 is structurally aligned with the existing split:

$$
\boxed{
\text{visible forward work}
\ \vee\
\text{paid backscatter}.
}
\tag{13.1}
$$

This is not merely an analogy.

The heat-semigroup coarse equation in FCBP-04 uses exactly the same Reynolds-covariance flux definition:

$$
\Pi
=
-R:\nabla U.
$$

---

# 14. Why pressure does not obstruct the whole-space bridge

The FCBP / external local combined work is:

$$
G
=
\Pi
+
\nabla\cdot(PU).
$$

On the whole space, for the smooth finite-energy class used in the present argument, the pressure transport is a divergence and contributes zero to the global energy balance.

Therefore:

$$
\boxed{
\int_{\mathbb R^3}
G\,dx
=
\int_{\mathbb R^3}
\Pi\,dx
=
F_s.
}
\tag{14.1}
$$

Thus the whole-space heat-band bridge is already a pressure--flux work bridge.

The difficulty begins only when one restricts to a finite local window, where pressure transport is physical and must remain in the ledger.

---

# 15. Compatibility with FCBP-04 heat filtering

FCBP-04 proves internally that for:

$$
S_s=e^{s\Delta},
$$

the covariance:

$$
R
=
S_s(u\otimes u)
-
U\otimes U
$$

is nonnegative because the heat kernel is nonnegative.

It also proves the coarse Navier--Stokes equation for a time-dependent:

$$
s(t),
$$

and constructs a co-moving heat pressure--flux ledger.

DCRP-11 uses only **fixed** heat filters on each first-crossing interval.

Thus no filter-drift term is present.

Across the sequence:

$$
n\to\infty,
$$

the physical filter scale changes as:

$$
s_{a,n},
s_{b,n}
\sim
\lambda_n^{-2},
$$

but the relative heat parameters:

$$
a,
\qquad
b
$$

remain fixed.

Therefore the constants in Theorem 11.1 do not degenerate with:

$$
n.
$$

This bypasses the old moving-filter switching issue at the one-event level.

---

# 16. Why DCRP-11 does not yet close the MORP zero kernel

The theorem above is global in space.

MORP and the external finite-window PFET framework are built from normalized local windows and local test families.

The external PFET work is:

$$
\mathcal W_{I,r}[\phi]
=
r^{-1}
\int_I
\int
\left(
\phi\Pi
-
PU\cdot\nabla\phi
\right)
dxdt.
$$

The whole-space identity corresponds formally to:

$$
\phi\equiv1,
$$

for which the pressure term disappears.

But:

$$
\phi\equiv1
$$

is not a compact local normalized window.

Therefore one cannot yet write:

$$
\boxed{
F_s\ne0
\Longrightarrow
\mathsf O_{\rm PFET}(D_\ast)>0
}
$$

for a specific local MORP minimal obstruction.

A localization theorem is still required.

This is the only major compatibility gap introduced by the present bridge.

---

# 17. Measure-theoretic localization alternative

Consider the forward-work case.

Define the nonnegative work measure on:

$$
I_n\times\mathbb R^3
$$

by:

$$
\boxed{
d\mu_n^+
=
\frac{
\lambda_n
(\Pi^{s_{b,n}})_+
\,dxdt
}{
M_n^+
},
}
\tag{17.1}
$$

where:

$$
M_n^+
=
\lambda_n
\int_{I_n}
\int
(\Pi^{s_{b,n}})_+
dxdt.
$$

When the forward branch occurs:

$$
M_n^+
\ge
c_{HB}\nu^2.
$$

Thus:

$$
\mu_n^+
$$

is a probability measure.

Rescale parabolically at:

$$
\lambda_n:
$$

$$
y
=
\lambda_n(x-x_n),
$$

$$
\tau
=
\lambda_n^2(t-t_n).
$$

The normalized positive-work measures again have unit mass.

After one-point compactification in the spatial variable and compactification of bounded normalized-time windows, every sequence has a weak-star subsequence.

There are only two generic outcomes relevant to local visibility.

### Localized work

A fixed normalized parabolic cell captures a positive fraction:

$$
\boxed{
\limsup_n
\mu_n^+
(
Q_R(y_n,\tau_n)
)
>0
}
\tag{17.2}
$$

for some fixed:

$$
R<\infty.
$$

Then recentering at that cell produces nonzero local forward-flux visibility.

### Diffuse / escaping work

Every fixed normalized parabolic cell captures vanishing mass.

Then the positive heat-flux work itself is a diffuse / escaping native work carrier.

The same alternative applies to the negative/backscatter measure.

Status:

$$
\boxed{
\textbf{ELEMENTARY COMPACTNESS REDUCTION}.
}
$$

This does not yet prove that the diffuse alternative contradicts:

$$
\mathsf R_{\rm nat}=0.
$$

That package-completion statement is the next target.

---

# 18. Local work versus local combined work

Even if:

$$
\Pi
$$

has a positive localized pairing, the local combined work:

$$
G
=
\Pi+\nabla\cdot(PU)
$$

may suffer pressure--flux cancellation.

This is already an explicit FCBP warning.

However the combined PFET architecture does not consist only of the signed scalar:

$$
G.
$$

FCBP-05 / FCBP-06 retain separate pressure, flux, energy, and trace channels in the combined observation package.

Therefore a local nonzero flux event may be routed in one of two ways:

1. it is visible in the separate flux channel;

2. cancellation in the combined work requires a compensating pressure-work channel, which is itself retained.

The exact quantitative local lower bound still depends on the finite-window detector / quotient geometry.

No automatic universal constant is asserted here.

---

# 19. NEW CONDITIONAL THEOREM — local PFET/paid collision

## Theorem 19.1

Assume the first-crossing heat-band event of Theorem 12.1 is completed into a local MORP return package with the following property.

For every normalized heat-filter forward/backscatter work measure with total critical mass at least:

$$
c_{HB}\nu^2,
$$

either:

### local visibility

a fixed normalized finite window carries a detector amount:

$$
\mathsf O_{\rm PFET}
\ge
c_\ast>0;
$$

or:

### paid visibility

the negative-work / leakage realization satisfies:

$$
\mathsf{Paid}
\ge
c_\ast>0;
$$

or:

### noncompact work defect

the diffuse / escaping work measure is retained in:

$$
\mathsf R_{\rm nat}
$$

with:

$$
\mathsf R_{\rm nat}
\ge
c_\ast>0.
$$

Then no zero-cost MORP minimal obstruction can contain the supplier first-crossing mechanism.

### Proof

Theorem 12.1 gives a fixed positive heat-filter forward or backscatter event.

By the assumed package-completion property, at least one of:

$$
\mathsf O_{\rm PFET},
$$

$$
\mathsf{Paid},
$$

$$
\mathsf R_{\rm nat}
$$

is strictly positive.

But a zero-cost minimal obstruction satisfies:

$$
\mathsf O_{\rm PFET}
=
\mathsf{Paid}
=
\mathsf R_{\rm nat}
=
0.
$$

Contradiction.

$$
\square
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL only on the stated localization/package-completion lemma}.
}
$$

---

# 20. What has been closed in this round

## Closed A — filter-physics mismatch at the global level

A supplier shell does not need to be compared directly with a compact-mollifier flux.

The same supplier forces a nonzero **heat-band** energy.

Heat filters are already part of the FCBP internal coarse-graining architecture.

## Closed B — unsigned ancestry versus paid work

The heat-band first crossing gives a signed alternative:

$$
\boxed{
\text{forward heat flux}
\vee
\text{heat backscatter}.
}
$$

Thus the supplier mechanism genuinely enters the visible-work / paid-backscatter split.

## Closed C — pressure ambiguity globally

Whole-space pressure transport integrates out.

The global heat-band bridge is an exact pressure--flux work statement.

---

# 21. What remains open

Only one closure-facing issue remains in this branch:

$$
\boxed{
\textbf{
whole-space critical heat-work event}
\Longrightarrow
\textbf{
local completed MORP PFET/paid/native coordinate}.
}
}
\tag{21.1}
$$

The failure modes are now very specific:

1. spatial diffusion of positive work;
2. temporal diffusion / long normalized crossing;
3. pressure--flux cancellation inside a selected local scalar work test;
4. mismatch between the local heat-filter package and the exact finite-window detector family;
5. failure to retain the diffuse work measure as a native residual.

No new Navier--Stokes mechanism remains hidden behind the term "spectral flux".

---

# 22. Next exact target — Heat-Flux Localization / Package-Completion Lemma

The next proof target is:

$$
\boxed{
\textbf{
Heat-Flux Localization / Package-Completion Lemma}.
}
$$

A useful sufficient version is:

Let:

$$
I_n
$$

be heat-band first-crossing intervals and let:

$$
\lambda_n\to\infty.
$$

Suppose:

$$
\lambda_n
\int_{I_n}
(F_{b,n})_+
dt
\ge
c\nu^2
$$

or:

$$
\lambda_n
\int_{I_n}
(F_{a,n})_-
dt
\ge
c\nu^2.
$$

Then after parabolic recentering and subsequence extraction, prove at least one of:

1. **local PFET atom**

   a fixed normalized finite window has nonzero separate pressure/flux/energy/trace detector norm;

2. **paid local backscatter/leakage**

   a fixed normalized finite window has nonzero paid-side tax;

3. **completed diffuse work defect**

   the normalized work measures have no local atom, but their noncompact / diffuse limit is retained as a nonzero native residual.

A proof of this lemma would combine with Theorem 19.1 to eliminate the entire supplier first-crossing mechanism from the MORP zero-cost kernel.

---

# 23. Stronger route suggested by the supplier endpoint atom

DCRP-08 already supplies a spatially localized critical shell atom at the supplier endpoint after recentering:

$$
\boxed{
\lambda_Q
\int_{
B_{r_0/\lambda_Q}(x_Q)
}
|u_Q(x,t_Q)|^2dx
\ge
c\nu^2.
}
\tag{23.1}
$$

This suggests a stronger version of the localization lemma:

> anchor the local heat-band / pressure--flux package to the supplier center:
>
> $$
> x_Q.
> $$
>
> If the positive heat-work is not visible in a bounded normalized neighborhood of that center, then the supplier energy must have entered through localization transport / leakage or the work must remain spatially nonlocal.
>
> Either alternative is a candidate paid/native residual.

The missing step is a local elliptic / commutator comparison between:

$$
u_Q
$$

and the heat-band resolved difference in a bounded normalized neighborhood.

This is a finite-scale harmonic-analysis problem, not a new global NS mechanism problem.

---

# 24. Source ledger

## Internal FCBP sources

### FCBP-03

`NS_FCBP_03_SignedWork_SlowScale_Telescoping_v0.1.md`

Relevant structures:

$$
G^\ell
=
\Pi^\ell+\nabla\cdot(P^\ell U^\ell),
$$

the signed forward/backscatter work split, and the paid-side backscatter ledger.

### FCBP-04

`NS_FCBP_04_MovingFilter_HorizonAlignment_v0.1.md`

Relevant established internal modules:

$$
S_s=e^{s\Delta},
$$

$$
R=S_s(u\otimes u)-U\otimes U,
$$

$$
R\ge0,
$$

the heat-filter coarse Navier--Stokes equation, and the co-moving heat pressure--flux ledger.

### FCBP-05 / FCBP-06

Relevant architecture:

- separate pressure / flux / energy / trace visibility;
- pressure--flux cancellation warning;
- backscatter / leakage on the paid side;
- combined-invisible residual branch;
- native residual completion.

### MORP-01

Relevant zero-cost kernel:

$$
\mathsf O_{\rm PFET}
=
0,
$$

$$
\mathsf{Paid}
=
0,
$$

$$
\mathsf R_{\rm nat}
=
0.
$$

---

## External primary source

Runlong Yu, *Coarse-Grained Resolution and Pressure--Flux Work Depletion for Navier--Stokes CKN Badness*, arXiv:2606.25322v1.

Primary facts independently checked:

- compact spatial coarse graining;
- Reynolds covariance:

  $$
  R^\ell
  =
  S_\ell(u\otimes u)
  -
  U^\ell\otimes U^\ell;
  $$

- resolved interscale work:

  $$
  \Pi^\ell
  =
  -
  R^\ell:\nabla U^\ell;
  $$

- combined pressure--flux work:

  $$
  G^\ell
  =
  \Pi^\ell
  +
  \nabla\cdot(P^\ell U^\ell);
  $$

- local normalized work:

  $$
  \mathcal W_{I,r}[\phi]
  =
  r^{-1}
  \int
  \left(
  \phi\Pi^\ell
  -
  P^\ell U^\ell\cdot\nabla\phi
  \right);
  $$

- exact finite-chain telescope;
- explicit statement that coarse observability is a separate open compactness/separation problem and is not automatic from the resolved-energy identity.

The present heat-filter bridge is an internal DCRP/FCBP derivation and is not attributed to Yu's compact-mollifier theorem.

---

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611v6.

Used through DCRP-08 for the dissipation-boundary supplier shell:

$$
\lambda_Q
\|u_Q\|_2^2
\gtrsim
\nu^2.
$$

---

# 25. End state

The Spectral-Flux / PFET compatibility problem has been substantially reduced.

The key new theorem is:

$$
\boxed{
\begin{aligned}
\text{supplier critical shell}
&\Longrightarrow
\text{critical heat-band first crossing}\\
&\Longrightarrow
\text{coarse heat-filter forward work}\\
&\qquad\vee
\text{fine heat-filter backscatter}.
\end{aligned}
}
$$

Quantitatively:

$$
\boxed{
\lambda
\int_I
(F_{s_b})_+
dt
+
\lambda
\int_I
(F_{s_a})_-
dt
\ge
c\nu^2.
}
$$

Thus the supplier mechanism already lands in the physical **PFET forward-work / paid-backscatter split** at the whole-space heat-filter level.

The sole closure-facing gap in this route is now:

$$
\boxed{
\textbf{
global heat-work}
\Longrightarrow
\textbf{
local completed PFET / paid / native package}.
}
$$

The next exact target is:

$$
\boxed{
\textbf{
Heat-Flux Localization / Package-Completion Lemma}.
}
$$

If that lemma is proved, the supplier first-crossing mechanism is incompatible with the MORP zero-cost kernel.
