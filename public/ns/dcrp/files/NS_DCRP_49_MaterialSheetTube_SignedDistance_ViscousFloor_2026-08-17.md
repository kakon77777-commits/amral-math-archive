# NS-DCRP-49 — Material-Sheet Tube Signed-Distance Ledger, Curvature-Scale Breakdown, and the General Viscous Thickness Floor

- date: 2026-08-17
- status: research proof checkpoint / viscous material-tube generalization
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. generalize the DCRP-48 one-dimensional coherent-sheet variance identity to a genuinely curved material sheet tube;
  2. derive the exact material signed-distance identity;
  3. derive the exact second normal-moment ledger for a nonnegative coherent sheet carrier;
  4. isolate normal-strain, curvature, non-affine Taylor, leakage, and source residuals;
  5. prove that molecular diffusion contributes a positive leading term independent of sheet curvature;
  6. show that bounded curvature at scales large compared with the sheet thickness cannot cancel the viscous floor;
  7. derive the same-parent robust thickness recurrence with a tube residual;
  8. prove that subdiffusive same-parent shadowing forces an order-$\varepsilon_n$ tube residual;
  9. show that, when all nongeometric residuals vanish, cancellation of the viscous floor requires curvature radius comparable to sheet thickness;
  10. classify the surviving escape channels as thickness-scale folding, tangential leakage, rank/plane transition, non-affine strain, or higher-order source;
  11. identify the next frontier as converting thickness-scale curvature/folding or leakage into existing DCRP strain/PFET/second-order defects.
- no full Navier--Stokes regularity claim is made.
- principal external calibration:
  - T. Gallay, Y. Maekawa, *Three-dimensional stability of Burgers vortices*, arXiv:1002.2489;
  - Y. Maekawa, H. Miura, C. Prange, *On stability of blow-up solutions of the Burgers vortex type for the Navier--Stokes equations with a linear strain*, arXiv:1807.10341;
  - N. Ogawa, *Diffusion in a Curved Tube*, arXiv:1109.0590.
- internal dependencies:
  - DCRP-41 moving pancake-jet normal strain;
  - DCRP-47 critical Euler sheet monodromy;
  - DCRP-48 coherent one-normal-profile viscous Batchelor floor.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-48 proved, on a one-sign one-dimensional coherent pancake-sheet subbranch,

$$
\boxed{
h_{n+1}^2
=
\mu^{-4}h_n^2
+
\varepsilon_n
\mathfrak D_{\rm nor},
\qquad
\mathfrak D_{\rm nor}>0,
}
\tag{1.1}
$$

with

$$
\boxed{
\varepsilon_{n+1}
=
\mu^{-1}\varepsilon_n.
}
\tag{1.2}
$$

Hence

$$
\boxed{
h_n^2/\varepsilon_n
\to
\delta_\ast>0.
}
\tag{1.3}
$$

The main limitation was the one-dimensional normal-profile assumption.

DCRP-49 removes that assumption at the level of the **normal second moment**.

Let

$$
\Sigma_s
$$

be a smooth material sheet transported by the similarity material velocity

$$
\boxed{
W
=
\gamma y+V.
}
\tag{1.4}
$$

Let

$$
d(y,s)
$$

be its signed distance in a tubular neighborhood.

Let

$$
f(y,s)\ge0
$$

be a normalized coherent sheet-carrier density with

$$
\boxed{
\int f(y,s)dy=1,
}
\tag{1.5}
$$

satisfying, modulo explicitly retained leakage/source terms,

$$
\boxed{
\partial_sf
+
\nabla\cdot(Wf)
=
\varepsilon(s)\Delta f
+
\mathcal S.
}
\tag{1.6}
$$

Define the normal second moment

$$
\boxed{
H(s)
=
\int d(y,s)^2f(y,s)dy.
}
\tag{1.7}
$$

The first main theorem is the exact signed-distance identity:

$$
\boxed{
D_sd(y,s)
=
\left[
W(y,s)
-
W(\pi_s y,s)
\right]
\cdot
n(\pi_s y,s),
}
\tag{1.8}
$$

where:

-:

  $$
  D_s=\partial_s+W\cdot\nabla;
  $$

-:

  $$
  \pi_s y
  $$

  is the nearest point on:

  $$
  \Sigma_s;
  $$

-:

  $$
  n
  $$

  is the oriented unit normal.

Thus, if

$$
y
=
\pi_s y
+
d\,n,
$$

$$
\boxed{
D_sd
=
\sigma_n(\pi_s y,s)d
+
\mathcal R_d,
}
\tag{1.9}
$$

where

$$
\boxed{
\sigma_n
=
n\cdot\nabla W\,n
}
\tag{1.10}
$$

and

$$
\boxed{
|\mathcal R_d|
\le
\frac12
\|\nabla^2W\|_{L^\infty(U)}
d^2.
}
\tag{1.11}
$$

The second main theorem is the exact tube second-moment ledger:

$$
\boxed{
H'
=
2
\int
dD_sd
\,fdy
+
2\varepsilon
+
2\varepsilon
\int
d\Delta d\,fdy
+
\mathcal R_{\rm src}.
}
\tag{1.12}
$$

Substituting (1.9),

$$
\boxed{
H'
=
2\sigma_{\rm ref}(s)H
+
2\varepsilon
+
\mathcal E_{\rm tube},
}
\tag{1.13}
$$

where

$$
\boxed{
\mathcal E_{\rm tube}
=
\mathcal E_{\rm strain}
+
\mathcal E_{\rm Taylor}
+
\mathcal E_{\rm curv}
+
\mathcal E_{\rm src/leak}.
}
\tag{1.14}
$$

The pieces are

$$
\boxed{
\mathcal E_{\rm strain}
=
2
\int
[
\sigma_n(\pi_s y,s)
-
\sigma_{\rm ref}(s)
]
d^2fdy,
}
\tag{1.15}
$$

$$
\boxed{
\mathcal E_{\rm Taylor}
=
2
\int
d\mathcal R_d
fdy,
}
\tag{1.16}
$$

$$
\boxed{
\mathcal E_{\rm curv}
=
2\varepsilon
\int
d\Delta d
fdy,
}
\tag{1.17}
$$

and

$$
\boxed{
\mathcal E_{\rm src/leak}
}
\tag{1.18}
$$

collects:

- nonconservative source;
- tube-boundary leakage;
- carrier renormalization;
- chart/rank changes.

The crucial point is:

$$
\boxed{
\textbf{
the leading molecular-diffusion contribution is always }+2\varepsilon.
}
\tag{1.19}
$$

Curvature modifies it only through

$$
2\varepsilon\int d\Delta d\,f.
$$

The third main theorem quantifies the curvature correction.

If the principal curvatures of the material sheet obey

$$
\boxed{
|\kappa_i|
\le
\kappa_\ast
}
\tag{1.20}
$$

and the carrier is confined to

$$
\boxed{
|d|
\le
\ell,
\qquad
\kappa_\ast\ell<1,
}
\tag{1.21}
$$

then

$$
\boxed{
|\Delta d|
\le
\frac{
2\kappa_\ast
}{
1-\kappa_\ast\ell
}
}
\tag{1.22}
$$

throughout the tube.

Hence

$$
\boxed{
|\mathcal E_{\rm curv}|
\le
\frac{
4\varepsilon
\kappa_\ast\ell
}{
1-\kappa_\ast\ell
}.
}
\tag{1.23}
$$

Therefore, if

$$
\boxed{
\kappa_\ast\ell\to0,
}
\tag{1.24}
$$

then

$$
\boxed{
\mathcal E_{\rm curv}
=
o(\varepsilon).
}
\tag{1.25}
$$

A sheet whose radius of curvature remains much larger than its thickness cannot cancel the positive viscous thickness production.

The fourth result bounds the non-affine Taylor term:

$$
\boxed{
|\mathcal E_{\rm Taylor}|
\le
\|\nabla^2W\|_\infty
\ell H.
}
\tag{1.26}
$$

Also, if

$$
\boxed{
|\sigma_n-\sigma_{\rm ref}|
\le
\delta_\sigma,
}
\tag{1.27}
$$

then

$$
\boxed{
|\mathcal E_{\rm strain}|
\le
2\delta_\sigma H.
}
\tag{1.28}
$$

Thus on a subdiffusive branch

$$
\boxed{
H/\varepsilon\to0,
}
\tag{1.29}
$$

bounded normal-strain mismatch and bounded

$$
\ell\|\nabla^2W\|_\infty
$$

produce only

$$
o(\varepsilon)
$$

errors.

Therefore, if the source/leakage residual is also

$$
o(\varepsilon),
$$

the only way to cancel the viscous floor is for

$$
\boxed{
\kappa_\ast\ell
}
$$

to fail to vanish.

In particular:

$$
\boxed{
\textbf{
subdiffusive material-sheet shadowing}
\Longrightarrow
\textbf{
thickness-scale curvature/folding}
\ \vee\
\textbf{
order-}\varepsilon
\textbf{ source/leakage/rank residual}.
}
}
\tag{1.30}
$$

This is the principal generalization of DCRP-48.

The fifth result restores the same-parent recurrence.

On the canonical moving-pancake normal strain branch, take

$$
\boxed{
\sigma_{\rm ref}(s)
=
\gamma-2a(s),
}
\tag{1.31}
$$

with

$$
\boxed{
\int_0^{S_0}
\sigma_{\rm ref}(s)ds
=
-2(1-2\gamma)S_0.
}
\tag{1.32}
$$

Let

$$
\boxed{
\lambda
=
1-2\gamma,
\qquad
\mu=e^{\lambda S_0}>1.
}
\tag{1.33}
$$

The Type-II viscosity during one DSS period is

$$
\boxed{
\varepsilon_n(s)
=
\varepsilon_n
e^{-\lambda s}.
}
\tag{1.34}
$$

Solving the tube ledger gives

$$
\boxed{
H_{n+1}
=
\mu^{-4}H_n
+
\varepsilon_n
\mathfrak D_{\rm nor}
+
\mathfrak R_{{\rm tube},n},
}
\tag{1.35}
$$

where

$$
\boxed{
\mathfrak D_{\rm nor}
=
2
\int_0^{S_0}
e^{-\lambda\tau}
e^{
2\int_\tau^{S_0}
\sigma_{\rm ref}(s)ds
}
d\tau
>0
}
\tag{1.36}
$$

is exactly the DCRP-48 positive normal-diffusion coefficient, and

$$
\boxed{
\mathfrak R_{{\rm tube},n}
=
\int_0^{S_0}
e^{
2\int_\tau^{S_0}
\sigma_{\rm ref}
}
\mathcal E_{{\rm tube},n}(\tau)d\tau.
}
\tag{1.37}
$$

Thus the same positive viscous recurrence survives at the material-tube level.

Since

$$
\boxed{
\varepsilon_{n+1}
=
\mu^{-1}\varepsilon_n,
}
\tag{1.38}
$$

define

$$
\boxed{
\delta_n
=
H_n/\varepsilon_n.
}
\tag{1.39}
$$

Then

$$
\boxed{
\delta_{n+1}
=
\mu^{-3}\delta_n
+
\mu\mathfrak D_{\rm nor}
+
\mu
\frac{
\mathfrak R_{{\rm tube},n}
}{
\varepsilon_n
}.
}
\tag{1.40}
$$

Therefore:

### robust coherent tube

If

$$
\boxed{
\mathfrak R_{{\rm tube},n}/\varepsilon_n\to0,
}
\tag{1.41}
$$

then

$$
\boxed{
\delta_n
\to
\delta_\ast
=
\frac{
\mu\mathfrak D_{\rm nor}
}{
1-\mu^{-3}
}
>0.
}
\tag{1.42}
$$

### subdiffusive tube

If

$$
\boxed{
\delta_n\to0,
}
\tag{1.43}
$$

then necessarily

$$
\boxed{
\frac{
\mathfrak R_{{\rm tube},n}
}{
\varepsilon_n
}
\to
-\mathfrak D_{\rm nor}.
}
\tag{1.44}
$$

Hence

$$
\boxed{
\liminf_n
\frac{
|\mathfrak R_{{\rm tube},n}|
}{
\varepsilon_n
}
\ge
\mathfrak D_{\rm nor}>0.
}
\tag{1.45}
$$

This is the general **viscous material-sheet shadowing barrier**.

The sixth central conclusion is geometric.

Assume the subdiffusive branch:

$$
H_n/\varepsilon_n\to0.
$$

Assume further:

$$
\boxed{
\sup_n
\delta_{\sigma,n}
<
\infty,
}
\tag{1.46}
$$

$$
\boxed{
\sup_n
\ell_n
\|\nabla^2W_n\|_\infty
<
\infty,
}
\tag{1.47}
$$

and:

$$
\boxed{
\mathfrak R_{{\rm src/leak},n}
=
o(\varepsilon_n).
}
\tag{1.48}
$$

Then the strain and Taylor contributions are

$$
o(\varepsilon_n).
$$

Therefore (1.44) can be realized only if the curvature correction remains order

$$
\varepsilon_n.
$$

By (1.23), this requires:

$$
\boxed{
\limsup_n
\kappa_{\ast,n}\ell_n
>
0.
}
\tag{1.49}
$$

Thus:

$$
\boxed{
\textbf{
a subdiffusive sheet with otherwise small residuals must bend/fold at its own thickness scale.
}
}
\tag{1.50}
$$

This is stronger than the statement that the sheet may simply be curved.

The radius of curvature must become comparable to the actual tube half-thickness.

Such geometry is a natural candidate for:

- sheet folding;
- multiplicity;
- tangential leakage;
- rank lifting;
- curvature-driven strain/PFET activity.

DCRP-49 does not yet prove which of those occurs.

The next frontier is therefore

$$
\boxed{
\textbf{
Thickness-Scale Sheet Curvature /
Folding--Leakage Compiler.
}
}
\tag{1.51}
$$

The target is to show that

$$
\kappa_\ast\ell\gtrsim1
$$

cannot persist through same-parent DSS returns without activating one of the already declared DCRP transition or second-order channels.

---

# 2. Material surface and signed distance

Let

$$
\Sigma_s
$$

be a smooth embedded oriented surface.

Assume it is material:

$$
\boxed{
\Sigma_s
=
Y_s(\Sigma_0),
}
\tag{2.1}
$$

where

$$
Y_s
$$

is the similarity flow of

$$
W.
$$

Let

$$
d(y,s)
$$

be the signed distance to

$$
\Sigma_s
$$

in a tubular neighborhood where the nearest-point projection

$$
\pi_s(y)
$$

is unique.

Then

$$
\boxed{
\nabla d(y,s)
=
n(\pi_s y,s).
}
\tag{2.2}
$$

The normal is extended constantly along normal rays.

---

# 3. Exact time derivative of signed distance

For a moving hypersurface with normal velocity

$$
W\cdot n,
$$

the derivative of the signed distance at a fixed observation point is

$$
\boxed{
\partial_sd(y,s)
=
-
W(\pi_s y,s)
\cdot
n(\pi_s y,s).
}
\tag{3.1}
$$

Therefore

$$
\boxed{
D_sd
=
\partial_sd
+
W(y,s)\cdot\nabla d
}
$$

gives

$$
\boxed{
D_sd
=
[
W(y,s)
-
W(\pi_s y,s)
]
\cdot n.
}
\tag{3.2}
$$

Status:

$$
\boxed{
\textbf{PROVED IN THE SMOOTH TUBULAR REGIME}.
}
$$

---

# 4. Normal Taylor expansion

Write

$$
y
=
\pi_s y
+
d\,n.
$$

Then

$$
W(y)-W(\pi y)
=
\int_0^d
\nabla W(
\pi y+\tau n
)n
d\tau.
$$

Therefore

$$
\boxed{
D_sd
=
d
n\cdot\nabla W(\pi y)n
+
\mathcal R_d.
}
\tag{4.1}
$$

Define

$$
\boxed{
\sigma_n(\pi y,s)
=
n\cdot\nabla W(\pi y,s)n.
}
\tag{4.2}
$$

By the fundamental theorem of calculus,

$$
\boxed{
|\mathcal R_d|
\le
\frac12
\|\nabla^2W\|_\infty
d^2.
}
\tag{4.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 5. Coherent tube carrier

Let

$$
f\ge0
$$

be a mass-normalized carrier:

$$
\boxed{
\int fdy=1.
}
\tag{5.1}
$$

The ideal conservative equation is

$$
\boxed{
\partial_sf
+
\nabla\cdot(Wf)
=
\varepsilon(s)\Delta f.
}
\tag{5.2}
$$

For a localized tube, actual vorticity-flux carriers may have:

- side leakage;
- sign cancellation;
- tangential transport;
- rank/plane exchange;
- source terms.

We write these as

$$
\boxed{
\partial_sf
+
\nabla\cdot(Wf)
=
\varepsilon\Delta f
+
\mathcal S.
}
\tag{5.3}
$$

If mass is not exactly preserved, the normalization correction is included in

$$
\mathcal S.
$$

The theorem below is exact for the declared normalized carrier equation.

---

# 6. Tube thickness

Define the normal second moment

$$
\boxed{
H(s)
=
\int
d^2fdy.
}
\tag{6.1}
$$

The RMS thickness is

$$
\boxed{
h_{\rm rms}
=
H^{1/2}.
}
\tag{6.2}
$$

For pointwise geometric estimates we also declare a hard tube half-thickness

$$
\boxed{
\ell(s)
}
\tag{6.3}
$$

such that the carrier support, or the retained dominant carrier region, lies in

$$
|d|\le\ell.
$$

Tail mass outside this tube is counted as leakage.

---

# 7. NEW THEOREM — Exact Material-Tube Second-Moment Ledger

## Theorem 7.1

The second moment satisfies

$$
\boxed{
H'
=
2
\int
dD_sd
fdy
+
\varepsilon
\int
\Delta(d^2)
fdy
+
\int
d^2\mathcal Sdy.
}
\tag{7.1}
$$

Since

$$
|\nabla d|=1,
$$

$$
\boxed{
\Delta(d^2)
=
2
+
2d\Delta d.
}
\tag{7.2}
$$

Hence

$$
\boxed{
H'
=
2
\int
dD_sd
fdy
+
2\varepsilon
+
2\varepsilon
\int
d\Delta d
fdy
+
\mathcal R_{\rm src}.
}
\tag{7.3}
$$

### Proof

Multiply the carrier equation by

$$
d^2
$$

and integrate.

The transport term is integrated by parts and combined with

$$
\partial_sd^2
$$

to produce

$$
D_sd^2=2dD_sd.
$$

The Laplacian is integrated by parts twice.

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

# 8. Reference normal strain

Let

$$
\sigma_{\rm ref}(s)
$$

be the canonical moving-pancake normal strain.

Write

$$
\boxed{
D_sd
=
\sigma_{\rm ref}d
+
[
\sigma_n-\sigma_{\rm ref}
]d
+
\mathcal R_d.
}
\tag{8.1}
$$

Then Theorem 7.1 becomes

$$
\boxed{
H'
=
2\sigma_{\rm ref}H
+
2\varepsilon
+
\mathcal E_{\rm tube}.
}
\tag{8.2}
$$

This is an exact decomposition.

---

# 9. Residual channels

Define:

$$
\boxed{
\mathcal E_{\rm strain}
=
2
\int
[
\sigma_n-\sigma_{\rm ref}
]
d^2fdy,
}
\tag{9.1}
$$

$$
\boxed{
\mathcal E_{\rm Taylor}
=
2
\int
d\mathcal R_d
fdy,
}
\tag{9.2}
$$

$$
\boxed{
\mathcal E_{\rm curv}
=
2\varepsilon
\int
d\Delta d
fdy,
}
\tag{9.3}
$$

and

$$
\boxed{
\mathcal E_{\rm src/leak}
=
\int
d^2\mathcal Sdy
}
\tag{9.4}
$$

plus any explicitly separated tube-boundary flux term.

Then

$$
\boxed{
\mathcal E_{\rm tube}
=
\mathcal E_{\rm strain}
+
\mathcal E_{\rm Taylor}
+
\mathcal E_{\rm curv}
+
\mathcal E_{\rm src/leak}.
}
\tag{9.5}
$$

---

# 10. Strain-mismatch bound

If:

$$
\boxed{
|\sigma_n-\sigma_{\rm ref}|
\le
\delta_\sigma,
}
\tag{10.1}
$$

then

$$
\boxed{
|\mathcal E_{\rm strain}|
\le
2\delta_\sigma H.
}
\tag{10.2}
$$

Thus on a subdiffusive branch

$$
H=o(\varepsilon),
$$

a uniformly bounded normal-strain mismatch produces only

$$
o(\varepsilon).
$$

---

# 11. Taylor-remainder bound

By (4.3),

$$
\begin{aligned}
|\mathcal E_{\rm Taylor}|
&\le
\|\nabla^2W\|_\infty
\int
|d|^3fdy
\\
&\le
\|\nabla^2W\|_\infty
\ell
H.
\end{aligned}
$$

Hence

$$
\boxed{
|\mathcal E_{\rm Taylor}|
\le
\|\nabla^2W\|_\infty
\ell H.
}
\tag{11.1}
$$

If:

$$
\ell\|\nabla^2W\|_\infty
$$

is uniformly bounded and

$$
H=o(\varepsilon),
$$

then

$$
\boxed{
\mathcal E_{\rm Taylor}=o(\varepsilon).
}
\tag{11.2}
$$

---

# 12. Signed-distance curvature identity

Let the principal curvatures of

$$
\Sigma_s
$$

at the footpoint be

$$
\kappa_1,\kappa_2.
$$

Inside the tubular neighborhood,

$$
\boxed{
\Delta d
=
\frac{
\kappa_1
}{
1+d\kappa_1
}
+
\frac{
\kappa_2
}{
1+d\kappa_2
}
}
\tag{12.1}
$$

up to the orientation convention for the signs of the principal curvatures.

Only the absolute bound is used below.

If:

$$
|\kappa_i|
\le
\kappa_\ast
$$

and:

$$
\kappa_\ast\ell<1,
$$

then

$$
\boxed{
|\Delta d|
\le
\frac{
2\kappa_\ast
}{
1-\kappa_\ast\ell
}.
}
\tag{12.2}
$$

---

# 13. NEW THEOREM — Curvature Correction Bound

## Theorem 13.1

Under Section 12:

$$
\boxed{
|\mathcal E_{\rm curv}|
\le
\frac{
4\varepsilon
\kappa_\ast\ell
}{
1-\kappa_\ast\ell
}.
}
\tag{13.1}
$$

### Proof

Use:

$$
|d|\le\ell
$$

and:

$$
\int f=1.
$$

Then:

$$
\left|
\int
d\Delta d
f
\right|
\le
\frac{
2\kappa_\ast\ell
}{
1-\kappa_\ast\ell
}.
$$

Multiply by:

$$
2\varepsilon.
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

# 14. Positive diffusion survives weak curvature

If:

$$
\boxed{
\kappa_\ast\ell
\le
c_0<1/5,
}
\tag{14.1}
$$

then:

$$
\boxed{
2\varepsilon
+
\mathcal E_{\rm curv}
\ge
c_{\rm diff}
\varepsilon
}
\tag{14.2}
$$

for some fixed:

$$
c_{\rm diff}>0.
$$

For example one may take:

$$
c_{\rm diff}
=
2
-
\frac{
4c_0
}{
1-c_0
}.
$$

Thus positive molecular thickness production remains uniformly coercive whenever the sheet curvature radius is larger than a fixed multiple of the tube thickness.

---

# 15. Canonical strict-DSS normal strain

On the shape-static moving-pancake branch:

$$
\boxed{
\sigma_{\rm ref}(s)
=
\gamma-2a(s).
}
\tag{15.1}
$$

DCRP-41 gives:

$$
\boxed{
\int_0^{S_0}
a(s)ds
=
\frac{
2-3\gamma
}{
2
}
S_0.
}
\tag{15.2}
$$

Therefore:

$$
\boxed{
\int_0^{S_0}
\sigma_{\rm ref}(s)ds
=
-2(1-2\gamma)S_0.
}
\tag{15.3}
$$

Let:

$$
\boxed{
\lambda=1-2\gamma,
\qquad
\mu=e^{\lambda S_0}.
}
\tag{15.4}
$$

Then:

$$
\boxed{
e^{
2\int_0^{S_0}
\sigma_{\rm ref}
}
=
\mu^{-4}.
}
\tag{15.5}
$$

---

# 16. Periodic Type-II viscosity

During one same-parent DSS period:

$$
\boxed{
\varepsilon_n(s)
=
\varepsilon_n
e^{-\lambda s}.
}
\tag{16.1}
$$

At the next root:

$$
\boxed{
\varepsilon_{n+1}
=
\mu^{-1}
\varepsilon_n.
}
\tag{16.2}
$$

This is inherited from DCRP-34/48.

---

# 17. Variation-of-constants formula

Let:

$$
G(s,\tau)
=
\exp
\left[
2
\int_\tau^s
\sigma_{\rm ref}(\xi)d\xi
\right].
$$

Then (8.2) gives:

$$
\boxed{
H(S_0)
=
G(S_0,0)H(0)
+
2
\int_0^{S_0}
G(S_0,\tau)
\varepsilon_n
e^{-\lambda\tau}
d\tau
+
\int_0^{S_0}
G(S_0,\tau)
\mathcal E_{\rm tube}(\tau)d\tau.
}
\tag{17.1}
$$

Define:

$$
\boxed{
\mathfrak D_{\rm nor}
=
2
\int_0^{S_0}
G(S_0,\tau)
e^{-\lambda\tau}
d\tau
>0.
}
\tag{17.2}
$$

and:

$$
\boxed{
\mathfrak R_{{\rm tube},n}
=
\int_0^{S_0}
G(S_0,\tau)
\mathcal E_{{\rm tube},n}(\tau)d\tau.
}
\tag{17.3}
$$

Then:

$$
\boxed{
H(S_0)
=
\mu^{-4}H(0)
+
\varepsilon_n
\mathfrak D_{\rm nor}
+
\mathfrak R_{{\rm tube},n}.
}
\tag{17.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 18. Same-parent tube recurrence

For a coherent tube lineage define:

$$
\boxed{
H_n
=
H_n(0),
\qquad
H_{n+1}
=
H_n(S_0).
}
\tag{18.1}
$$

Then:

$$
\boxed{
H_{n+1}
=
\mu^{-4}H_n
+
\varepsilon_n
\mathfrak D_{\rm nor}
+
\mathfrak R_{{\rm tube},n}.
}
\tag{18.2}
$$

This is the general material-sheet version of the DCRP-48 recurrence.

---

# 19. Dimensionless tube thickness

Set:

$$
\boxed{
\delta_n
=
\frac{
H_n
}{
\varepsilon_n
}.
}
\tag{19.1}
$$

Using:

$$
\varepsilon_{n+1}
=
\mu^{-1}\varepsilon_n,
$$

$$
\boxed{
\delta_{n+1}
=
\mu^{-3}\delta_n
+
\mu
\mathfrak D_{\rm nor}
+
\mu
\frac{
\mathfrak R_{{\rm tube},n}
}{
\varepsilon_n
}.
}
\tag{19.2}
$$

---

# 20. NEW THEOREM — Robust Material-Sheet Viscous Floor

## Theorem 20.1

If:

$$
\boxed{
\mathfrak R_{{\rm tube},n}
=
o(\varepsilon_n),
}
\tag{20.1}
$$

then:

$$
\boxed{
\delta_n
\to
\delta_\ast
=
\frac{
\mu
\mathfrak D_{\rm nor}
}{
1-\mu^{-3}
}
>0.
}
\tag{20.2}
$$

Hence:

$$
\boxed{
H_n
\sim
\delta_\ast
\varepsilon_n.
}
\tag{20.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus the DCRP-48 Batchelor/Burgers floor is stable at the material-tube level.

---

# 21. NEW THEOREM — General Subdiffusive Shadowing Residual

## Theorem 21.1

If:

$$
\boxed{
H_n/\varepsilon_n\to0,
}
\tag{21.1}
$$

then:

$$
\boxed{
\frac{
\mathfrak R_{{\rm tube},n}
}{
\varepsilon_n
}
\to
-
\mathfrak D_{\rm nor}.
}
\tag{21.2}
$$

In particular:

$$
\boxed{
\liminf_n
\frac{
|\mathfrak R_{{\rm tube},n}|
}{
\varepsilon_n
}
\ge
\mathfrak D_{\rm nor}>0.
}
\tag{21.3}
$$

### Proof

Divide (18.2) by:

$$
\varepsilon_n.
$$

Both:

$$
H_n/\varepsilon_n
$$

and:

$$
H_{n+1}/\varepsilon_n
=
\mu^{-1}
H_{n+1}/\varepsilon_{n+1}
$$

tend to zero.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the general viscous sheet-form shadowing barrier.

---

# 22. Thin-tube small-residual regime

Assume:

$$
H_n/\varepsilon_n\to0.
$$

Assume also:

$$
\boxed{
\sup_n
\delta_{\sigma,n}
<
\infty,
}
\tag{22.1}
$$

and:

$$
\boxed{
\sup_n
\ell_n
\|\nabla^2W_n\|_\infty
<
\infty.
}
\tag{22.2}
$$

Then:

$$
\boxed{
\mathcal E_{{\rm strain},n}
=
o(\varepsilon_n),
}
\tag{22.3}
$$

and:

$$
\boxed{
\mathcal E_{{\rm Taylor},n}
=
o(\varepsilon_n).
}
\tag{22.4}
$$

If:

$$
\boxed{
\mathfrak R_{{\rm src/leak},n}
=
o(\varepsilon_n),
}
\tag{22.5}
$$

the only remaining order-$\varepsilon_n$ channel is curvature.

---

# 23. NEW THEOREM — Thickness-Scale Curvature Necessity

## Theorem 23.1

Under Section 22, subdiffusive shadowing:

$$
H_n/\varepsilon_n\to0
$$

implies:

$$
\boxed{
\limsup_{n\to\infty}
\kappa_{\ast,n}
\ell_n
>
0.
}
\tag{23.1}
$$

### Proof

If:

$$
\kappa_{\ast,n}\ell_n\to0,
$$

then Theorem 13.1 gives:

$$
\mathcal E_{{\rm curv},n}
=
o(\varepsilon_n).
$$

All tube residual channels would then be:

$$
o(\varepsilon_n),
$$

contradicting Theorem 21.1.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED UNDER THE DECLARED THIN-TUBE COHERENCE ASSUMPTIONS}.
}
$$

---

# 24. Geometric interpretation

Theorem 23.1 says the sheet cannot remain both:

- subdiffusive;
- gently curved.

If:

$$
\ell_n
$$

is the actual retained carrier half-thickness, then:

$$
\boxed{
\kappa_{\ast,n}
\ell_n
\gtrsim1
}
\tag{24.1}
$$

means that the local curvature radius:

$$
R_{\rm curv}\sim\kappa_\ast^{-1}
$$

is of the same order as:

$$
\ell_n.
$$

Thus the sheet must fold or bend on its own thickness scale.

This is an extreme geometric regime.

It is a natural source of:

- self-near-interaction;
- layer collision;
- multiplicity;
- tangential leakage;
- rank lifting.

No one of those is inferred automatically in DCRP-49.

---

# 25. Why curvature can cancel the diffusion ledger

The Laplacian of squared distance is:

$$
\Delta(d^2)
=
2+2d\Delta d.
$$

The positive:

$$
2
$$

is the flat-sheet diffusion term.

A large negative:

$$
d\Delta d
$$

can reduce that contribution only when the parallel surfaces are strongly curved relative to their separation.

The tubular-coordinate singularity:

$$
1+d\kappa_i=0
$$

occurs precisely when the normal projection ceases to be regular.

Thus:

$$
\boxed{
\kappa_\ast\ell=O(1)
}
$$

marks the breakdown of the gentle-sheet tubular geometry.

This is why curvature escape is naturally a transition/folding channel.

---

# 26. Relation to curved-tube diffusion

Diffusion in a curved thin tube is known to acquire geometric correction terms depending on curvature and torsion.

DCRP-49 does not import a reduced curved-tube PDE.

It uses only the exact ambient identity:

$$
\Delta(d^2)=2+2d\Delta d
$$

and the signed-distance curvature formula.

The external curved-tube literature is used only as geometric calibration.

---

# 27. Moving-plane compatibility

The material sheet normal may rotate with time.

The signed-distance identity (3.2) remains valid because:

$$
\Sigma_s
$$

is transported by the full material flow.

The leading term is always:

$$
n\cdot\nabla W\,n.
$$

Therefore moving-plane kinematics do not by themselves destroy the tube ledger.

They enter through:

- normal-strain mismatch;
- curvature;
- chart/rank residuals.

This is one advantage of the signed-distance formulation over a fixed Cartesian normal coordinate.

---

# 28. Sign-coherence limitation

The carrier density:

$$
f\ge0
$$

is essential.

For a sign-changing vorticity component, a probability-type flux normalization may not exist.

Then:

- cancellations;
- multiple layers;
- sheet splitting;

must be retained.

Thus DCRP-49 generalizes DCRP-48 geometrically, but still belongs to the **coherent nonnegative carrier** sector.

A fully signed vorticity-measure theorem remains open.

---

# 29. Tangential leakage limitation

A curved sheet may transport vorticity along the sheet and exchange it between nearby sheets.

Such transport changes the retained normal carrier distribution even when molecular diffusion is small.

In the tube ledger it enters:

$$
\mathcal E_{\rm src/leak}.
$$

Therefore a subdiffusive sheet may survive by paying a finite tangential-leakage residual.

This is a legitimate complementary branch.

---

# 30. Rank-lifting limitation

If the vorticity develops a normal component, the selected rank-two coherent carrier no longer describes the full vorticity.

That is:

$$
\boxed{
\text{rank-three lifting}.
}
$$

It is already an existing DCRP transition channel.

DCRP-49 does not need to force such lifting; it merely ensures that leaving the coherent sheet sector is visible.

---

# 31. Candidate curvature-to-strain bridge

If:

$$
\kappa_\ast\ell\gtrsim1,
$$

a sheet of thickness:

$$
\ell
$$

has order-one change of normal direction across a thickness-scale horizontal displacement.

One expects this to activate:

- vorticity-direction increments;
- near-field strain geometry;
- filtered commutator defects.

A future theorem should quantify:

$$
\boxed{
\kappa_\ast\ell
\gtrsim1
\Longrightarrow
\widetilde{\mathcal S}^{(3)}
+
\mathcal M_{SV}
+
\mathsf R_{\rm rank}
\ge
c
}
\tag{31.1}
$$

under a compact normalized class.

This bridge is not proved in DCRP-49.

---

# 32. Candidate curvature-to-PFET bridge

A strongly folded sheet may create nearby regions with:

- opposing normals;
- rapid pressure variation;
- layer-layer interaction.

Since DCRP-31 already forces a finite-radius inward PFET matching layer, another possible route is to prove that thickness-scale folding must intersect or reinforce that PFET carrier.

Again:

$$
\boxed{
\textbf{OPEN}.
}
$$

No pressure contradiction is asserted in this round.

---

# 33. Robust branch tree after DCRP-49

The strongest rank-two Navier--Stokes sheet shadow now satisfies at least one of:

$$
\boxed{
\text{diffusive thickness floor}
}
$$

or:

$$
\boxed{
\text{thickness-scale curvature/folding}
}
$$

or:

$$
\boxed{
\text{tangential leakage/source residual}
}
$$

or:

$$
\boxed{
\text{non-affine normal strain}
}
$$

or:

$$
\boxed{
\text{rank/plane transition}
}
$$

or:

$$
\boxed{
\text{sign/multilayer breakdown}.
}
$$

Thus the pure smooth gently curved subdiffusive sheet branch is closed.

---

# 34. What DCRP-49 closes

DCRP-48's one-dimensional coherence assumption is no longer needed for the second-moment mechanism itself.

The following material-tube branch is closed:

$$
\boxed{
\textbf{
coherent nonnegative carrier}
+
\textbf{
canonical normal strain}
+
\textbf{
gentle curvature}
+
\textbf{
small leakage/source}
+
\textbf{
subdiffusive same-parent thickness}.
}
}
$$

It cannot persist with positive Navier--Stokes viscosity.

This is a genuinely viscous geometric exclusion.

---

# 35. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Thickness-Scale Sheet Curvature /
Folding--Leakage Compiler.
}
}
$$

A useful theorem would prove that:

$$
\kappa_\ast\ell
\gtrsim1
$$

on a same-parent strict Type-II sequence forces at least one existing native DCRP channel:

1. vorticity-direction increment / filtered defect;

2. rank lifting;

3. tangential leakage with positive sheet-flux residual;

4. pressure/PFET interaction;

5. second-order vorticity-gradient concentration;

6. loss of tubular injectivity / sheet multiplicity.

A second target is to remove the nonnegative-carrier assumption by working directly with vector-valued vorticity two-form measures.

This is now the sharpest remaining sheet-geometry frontier.

---

# 36. Source-status audit

The Burgers-vortex literature provides rigorous examples in which linear strain and molecular diffusion balance to produce coherent Navier--Stokes vorticity structures, and rigorous stability theory exists both for classical Burgers vortices and for time-dependent linear-strain variants.

These results calibrate the DCRP-49 conclusion that a viscous thickness scale of order:

$$
\sqrt{\varepsilon}
$$

is a legitimate strain--diffusion equilibrium rather than a proof artifact.

General diffusion theory in curved tubes likewise shows that curvature modifies effective diffusion through geometric correction terms.

DCRP-49 does not import those reduced equations; its signed-distance moment ledger is derived directly in ambient space.

---

# 37. End state

For a material sheet:

$$
\Sigma_s,
$$

the signed distance satisfies

$$
\boxed{
D_sd
=
[
W(y)-W(\pi y)
]\cdot n.
}
$$

Therefore:

$$
\boxed{
D_sd
=
\sigma_n d
+
O(
\|\nabla^2W\|_\infty d^2
).
}
$$

For a coherent normalized nonnegative sheet carrier:

$$
f,
$$

the normal second moment

$$
H=\int d^2f
$$

satisfies:

$$
\boxed{
H'
=
2\sigma_{\rm ref}H
+
2\varepsilon
+
\mathcal E_{\rm strain}
+
\mathcal E_{\rm Taylor}
+
\mathcal E_{\rm curv}
+
\mathcal E_{\rm src/leak}.
}
$$

The curvature term obeys:

$$
\boxed{
|\mathcal E_{\rm curv}|
\le
\frac{
4\varepsilon\kappa_\ast\ell
}{
1-\kappa_\ast\ell
}.
}
$$

Thus gentle curvature:

$$
\kappa_\ast\ell\to0
$$

cannot cancel the positive viscous diffusion term.

The one-period same-parent recurrence is:

$$
\boxed{
H_{n+1}
=
\mu^{-4}H_n
+
\varepsilon_n\mathfrak D_{\rm nor}
+
\mathfrak R_{{\rm tube},n}.
}
$$

Hence:

$$
\boxed{
H_n/\varepsilon_n\to0
}
$$

requires:

$$
\boxed{
\mathfrak R_{{\rm tube},n}
=
-\mathfrak D_{\rm nor}\varepsilon_n
+
o(\varepsilon_n).
}
$$

If all nongeometric residuals are smaller than:

$$
\varepsilon_n,
$$

then:

$$
\boxed{
\limsup
\kappa_{\ast,n}\ell_n
>
0.
}
$$

Therefore:

$$
\boxed{
\textbf{
subdiffusive viscous sheet shadowing}
\Longrightarrow
\textbf{
thickness-scale folding/curvature}
\ \vee\
\textbf{
order-}\varepsilon
\textbf{ leakage/source/rank residual}.
}
}
$$

The next frontier is:

$$
\boxed{
\textbf{
Thickness-Scale Sheet Curvature /
Folding--Leakage Compiler.
}
}
$$
