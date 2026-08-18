# NS-DCRP-52 — Palinstrophy Criticality Audit, Enstrophy-Surplus Closure, and Gaussian Batchelor Return Rigidity

- date: 2026-08-17
- status: research proof checkpoint / second-order-action audit and equality-manifold reduction
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit whether the positive/divergent normalized second-order sheet action from DCRP-51 is itself a non-repeatable parent-level tax;
  2. derive the exact Type-II scaling of endpoint enstrophy, palinstrophy action, stretching work, and lower-order energy dissipation;
  3. prove a critical NO-GO: raw normalized palinstrophy positivity does not by itself yield a same-parent finite-budget contradiction;
  4. derive the normalized similarity enstrophy ledger and separate canonical affine strain payment from genuine surplus;
  5. prove that the subdiffusive branch forces a diverging second-order surplus relative to the sheet enstrophy reservoir;
  6. connect that surplus to the filtered far-field / commutator / localization architecture;
  7. identify the diffusive Batchelor branch as a legitimate strain--diffusion equality rather than a defect;
  8. rescale the coherent Fokker--Planck normal profile by the local viscous length;
  9. derive the exact root-to-root Gaussian AR(1) return operator;
  10. prove Wasserstein contraction and uniqueness of the recurrent Gaussian normal profile;
  11. show that any non-Gaussian coherent recurrent normal profile requires a profile/source residual;
  12. identify the next frontier as unforced same-parent reproduction of the Batchelor--Gaussian sheet and its affine strain supplier.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1;
  - T. Gallay, Y. Maekawa, *Three-dimensional stability of Burgers vortices*, arXiv:1002.2489;
  - Y. Maekawa, H. Miura, C. Prange, *On stability of blow-up solutions of the Burgers vortex type for the Navier--Stokes equations with a linear strain*, arXiv:1807.10341.
- internal dependencies:
  - DCRP-30 strict same-parent DSS scaling;
  - DCRP-35 affine strain supplier;
  - DCRP-48 coherent sheet Fokker--Planck recurrence;
  - DCRP-51 fragmentation-proof second-order sheet activation.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction

DCRP-51 proved, on the strong coherent sheet-carrier branch,

$$
\boxed{
\mathcal P_{2,n}
\gtrsim
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}
\mathcal O_{{\rm sh},n},
}
\tag{1.1}
$$

where

$$
\boxed{
\mathcal P_{2,n}
=
\int_0^{S_0}
\int
\varepsilon_n(s)
|\nabla\Omega_n|^2
}
\tag{1.2}
$$

is the normalized second-order viscous sheet action.

If

$$
h_{{\rm harm},n}^2/\varepsilon_n\to0,
$$

then

$$
\mathcal P_{2,n}\to\infty.
$$

If

$$
h_{{\rm harm},n}^2\lesssim\varepsilon_n,
$$

then

$$
\mathcal P_{2,n}\ge c>0.
$$

It was tempting to treat repeated positivity of

$$
\mathcal P_{2,n}
$$

as a non-summable same-parent tax.

DCRP-52 proves that this is too strong.

The physical palinstrophy action and the physical endpoint enstrophy have **exactly the same Type-II scaling**.

Therefore:

$$
\boxed{
\textbf{
raw second-order action positivity is not by itself a finite parent-budget contradiction.
}
}
\tag{1.3}
$$

This is a critical NO-GO.

The correct obstruction is a **second-order surplus beyond the canonical strain/enstrophy return budget**.

The subdiffusive branch produces such a surplus.

The diffusive Batchelor branch need not.

---

# 2. Type-II normalization

Use the DCRP-30 normalization

$$
\boxed{
v_n(y,\tau)
=
\frac{
r_n
}{
a_n
}
U
\left(
x_n+r_ny,
t_n+\frac{
r_n^2
}{
a_n
}\tau
\right).
}
\tag{2.1}
$$

Then

$$
\boxed{
\varepsilon_n
=
\frac{
\nu
}{
a_n
}.
}
\tag{2.2}
$$

The normalized vorticity is

$$
\boxed{
\Omega_n
=
\nabla_y\times v_n
=
\frac{
r_n^2
}{
a_n
}
\omega.
}
\tag{2.3}
$$

The normalized vorticity gradient is

$$
\boxed{
\nabla_y\Omega_n
=
\frac{
r_n^3
}{
a_n
}
\nabla_x\omega.
}
\tag{2.4}
$$

The Jacobians are

$$
\boxed{
dy
=
r_n^{-3}dx,
}
\tag{2.5}
$$

and

$$
\boxed{
d\tau
=
\frac{
a_n
}{
r_n^2
}
dt.
}
\tag{2.6}
$$

---

# 3. Physical endpoint enstrophy scaling

At one root time,

$$
\omega
=
\frac{
a_n
}{
r_n^2
}
\Omega_n.
$$

Therefore

$$
\boxed{
\int
|\omega|^2dx
=
\frac{
a_n^2
}{
r_n
}
\int
|\Omega_n|^2dy.
}
\tag{3.1}
$$

Define the endpoint enstrophy scale

$$
\boxed{
Q_n^{(2)}
=
\frac{
a_n^2
}{
r_n
}.
}
\tag{3.2}
$$

---

# 4. Physical palinstrophy action scaling

The normalized second-order action is

$$
\mathcal P_{2,n}
=
\varepsilon_n
\iint
|\nabla_y\Omega_n|^2
dyd\tau.
$$

Using Sections 2--3,

$$
\boxed{
\mathcal P_{2,n}
=
\frac{
r_n
}{
a_n^2
}
\nu
\iint
|\nabla_x\omega|^2
dxdt.
}
\tag{4.1}
$$

Equivalently,

$$
\boxed{
\nu
\iint
|\nabla_x\omega|^2
dxdt
=
\frac{
a_n^2
}{
r_n
}
\mathcal P_{2,n}.
}
\tag{4.2}
$$

Thus the physical palinstrophy action has the same prefactor

$$
Q_n^{(2)}
=
a_n^2/r_n
$$

as the physical endpoint enstrophy.

Status:

$$
\boxed{
\textbf{PROVED BY SCALING}.
}
$$

---

# 5. Physical stretching-work scaling

The physical strain scales as

$$
\boxed{
S_{\rm phys}
=
\frac{
a_n
}{
r_n^2
}
S_n.
}
\tag{5.1}
$$

Hence

$$
S_{\rm phys}\omega\cdot\omega
$$

scales as

$$
a_n^3/r_n^6.
$$

Using the spacetime Jacobian

$$
dxdt
=
\frac{
r_n^5
}{
a_n
}
dyd\tau,
$$

one gets

$$
\boxed{
\iint
S_{\rm phys}\omega\cdot\omega
dxdt
=
\frac{
a_n^2
}{
r_n
}
\iint
S_n\Omega_n\cdot\Omega_n
dyd\tau.
}
\tag{5.2}
$$

Thus:

$$
\boxed{
\textbf{
endpoint enstrophy, vortex stretching, and palinstrophy action all have the same Type-II scaling.
}
}
\tag{5.3}
$$

This is the core criticality.

---

# 6. Lower-order energy dissipation scaling

The normalized spacetime enstrophy satisfies

$$
\boxed{
\iint
|\Omega_n|^2
dyd\tau
=
\frac1{
a_nr_n
}
\iint
|\omega|^2
dxdt.
}
\tag{6.1}
$$

Therefore the physical kinetic-energy dissipation on the corresponding parent window is

$$
\boxed{
\nu
\iint
|\omega|^2
dxdt
=
\nu
a_nr_n
\iint
|\Omega_n|^2
dyd\tau.
}
\tag{6.2}
$$

This uses the divergence-free identity that the vorticity and velocity-gradient

$$
L^2
$$

norms agree in the whole-space/no-boundary idealization, with local cutoff errors retained separately in localized settings.

---

# 7. Same-parent scaling factors

Let

$$
\boxed{
\lambda
=
r_{n+1}/r_n
\in(0,1),
}
\tag{7.1}
$$

and

$$
\boxed{
\mu
=
a_{n+1}/a_n
=
\lambda^{1-\alpha},
}
\tag{7.2}
$$

where the strict DSS exponent satisfies

$$
\boxed{
1<\alpha<3/2.
}
\tag{7.3}
$$

Then

$$
\boxed{
\frac{
Q_{n+1}^{(2)}
}{
Q_n^{(2)}
}
=
\frac{
\mu^2
}{
\lambda
}
=
\lambda^{1-2\alpha}
>
1.
}
\tag{7.4}
$$

Thus physical endpoint enstrophy and physical palinstrophy action can both grow geometrically along the same-parent roots.

By contrast,

$$
\boxed{
\frac{
a_{n+1}r_{n+1}
}{
a_nr_n
}
=
\lambda\mu
=
\lambda^{2-\alpha}
<1.
}
\tag{7.5}
$$

Because

$$
2-\alpha>1/2,
$$

a constant normalized spacetime enstrophy cost is compatible with a geometrically summable physical kinetic-energy dissipation.

---

# 8. NEW NO-GO — Raw Palinstrophy Return Summation

## Theorem 8.1

A lower bound

$$
\boxed{
\mathcal P_{2,n}\ge c_0>0
}
\tag{8.1}
$$

on infinitely many same-parent returns does not by itself contradict either:

1. the physical enstrophy balance;

2. the global kinetic-energy dissipation budget.

### Reason

The physical palinstrophy action is

$$
Q_n^{(2)}\mathcal P_{2,n},
$$

and the physical endpoint enstrophy is also scaled by

$$
Q_n^{(2)}.
$$

Thus enstrophy growth can replenish palinstrophy at the same critical scaling.

Meanwhile the corresponding lower-order physical energy dissipation is weighted by

$$
a_nr_n,
$$

which decays geometrically.

Therefore there is no independent finite parent budget for raw palinstrophy supplied by the energy inequality.

Status:

$$
\boxed{
\textbf{PROVED SCALING NO-GO}.
}
$$

---

# 9. Physical enstrophy balance audit

For a smooth physical Navier--Stokes solution on a window where boundary terms vanish or are retained explicitly,

$$
\boxed{
\frac12
E_\omega(t_1)
+
\nu
\int_{t_0}^{t_1}
\|\nabla\omega\|_2^2dt
=
\frac12
E_\omega(t_0)
+
\int_{t_0}^{t_1}
\int
S\omega\cdot\omega
dxdt.
}
\tag{9.1}
$$

The three nontrivial terms on the right/left all scale as

$$
a_n^2/r_n.
$$

Hence the second-order action is naturally a **transfer/balance term**, not an independently monotone quantity.

---

# 10. Similarity enstrophy ledger

In strict similarity variables,

$$
\boxed{
\partial_s\Omega
+
W\cdot\nabla\Omega
+
\Omega
=
S\Omega
+
\varepsilon(s)\Delta\Omega.
}
\tag{10.1}
$$

Let

$$
w
=
|\Omega|^2/2.
$$

Then

$$
\boxed{
\partial_sw
+
\nabla\cdot(Ww)
+
c_\gamma w
=
\Omega\cdot S\Omega
+
\varepsilon\Delta w
-
\varepsilon|\nabla\Omega|^2,
}
\tag{10.2}
$$

where

$$
\boxed{
c_\gamma
=
2-3\gamma
>
0.
}
\tag{10.3}
$$

This is the exact similarity enstrophy identity.

---

# 11. Period-integrated local form

Let

$$
\chi
$$

be a fixed or solution-adapted core weight.

Define

$$
\boxed{
\mathcal E_n(s)
=
\int
\chi w_n,
}
\tag{11.1}
$$

$$
\boxed{
\mathcal P_{2,n}
=
\int_0^{S_0}
\int
\chi
\varepsilon_n(s)
|\nabla\Omega_n|^2,
}
\tag{11.2}
$$

and

$$
\boxed{
\mathcal W_{S,n}
=
\int_0^{S_0}
\int
\chi
\Omega_n\cdot S_n\Omega_n.
}
\tag{11.3}
$$

Then

$$
\boxed{
\mathcal E_n(S_0)
-
\mathcal E_n(0)
+
c_\gamma
\mathcal O_n
+
\mathcal P_{2,n}
=
\mathcal W_{S,n}
+
\mathcal R_{{\rm loc},n},
}
\tag{11.4}
$$

where

$$
\boxed{
\mathcal O_n
=
\int_0^{S_0}
\int
\chi w_n,
}
\tag{11.5}
$$

and

$$
\mathcal R_{{\rm loc},n}
$$

contains transport/diffusion cutoff terms.

On an exact recurrent profile with a periodic/adapted weight, the endpoint difference vanishes.

---

# 12. Canonical pancake affine stretching

On the rank-two moving-pancake branch,

$$
\boxed{
S_n
=
A_{{\rm pan},n}
+
S_{{\rm rem},n}.
}
\tag{12.1}
$$

For vorticity tangent to the pancake plane,

$$
\boxed{
\Omega\cdot A_{\rm pan}\Omega
=
a(s)|\Omega|^2.
}
\tag{12.2}
$$

Thus the canonical affine stretching budget is

$$
\boxed{
\mathcal W_{{\rm pan},n}
=
2
\int_0^{S_0}
a(s)
\mathcal E_{\Omega,n}(s)ds.
}
\tag{12.3}
$$

If

$$
a
$$

is uniformly bounded on a compact normalized class,

$$
\boxed{
|\mathcal W_{{\rm pan},n}|
\le
C_a
\mathcal O_n.
}
\tag{12.4}
$$

The similarity damping term is likewise

$$
O(\mathcal O_n).
$$

---

# 13. Second-order rate

Define the sheet second-order rate

$$
\boxed{
\mathfrak R_{2,n}
=
\frac{
\mathcal P_{2,n}
}{
\mathcal O_{{\rm sh},n}
}
}
\tag{13.1}
$$

whenever

$$
\mathcal O_{{\rm sh},n}>0.
$$

DCRP-51 gives

$$
\boxed{
\mathfrak R_{2,n}
\ge
c
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}.
}
\tag{13.2}
$$

Thus:

### subdiffusive sheet

$$
\boxed{
h_{{\rm harm},n}^2/\varepsilon_n\to0
}
\tag{13.3}
$$

implies

$$
\boxed{
\mathfrak R_{2,n}\to\infty.
}
\tag{13.4}
$$

### diffusive sheet

$$
\boxed{
h_{{\rm harm},n}^2
\asymp
\varepsilon_n
}
\tag{13.5}
$$

gives

$$
\boxed{
\mathfrak R_{2,n}
=
O(1)
}
\tag{13.6}
$$

on an equality-scale coherent profile.

---

# 14. Genuine second-order surplus

Define schematically the canonical second-order surplus

$$
\boxed{
\mathfrak X_{2,n}
=
\left[
\mathcal P_{2,n}
-
C_{\rm can}
\mathcal O_{{\rm sh},n}
-
|\mathcal R_{{\rm end/loc},n}|
\right]_+,
}
\tag{14.1}
$$

where

$$
C_{\rm can}
$$

absorbs:

- bounded affine pancake stretching;
- similarity damping;
- bounded lower-order enstrophy reservoir;
- declared compact endpoint mismatch.

This quantity is not intended as a universal formula independent of the declared filtered/localized compiler.

It records the correct logical object:

$$
\boxed{
\textbf{
diffusion beyond what canonical recurrent enstrophy/strain can pay}.
}
}
\tag{14.2}
$$

---

# 15. NEW THEOREM — Subdiffusive Surplus Activation

## Theorem 15.1

Assume:

1. persistent sheet enstrophy:

   $$
   \mathcal O_{{\rm sh},n}\ge o_0>0;
   $$

2. bounded canonical affine strain and endpoint/localization ratio:

   $$
   \frac{
   |\mathcal R_{{\rm end/loc},n}|
   }{
   \mathcal O_{{\rm sh},n}
   }
   \le C_R;
   $$

3. subdiffusive harmonic thickness:

   $$
   h_{{\rm harm},n}^2/\varepsilon_n\to0.
   $$

Then:

$$
\boxed{
\mathfrak X_{2,n}\to\infty.
}
\tag{15.1}
$$

### Proof

DCRP-51 gives

$$
\mathcal P_{2,n}
\ge
c
\varepsilon_n
\mathcal O_{{\rm sh},n}
/h_{{\rm harm},n}^2.
$$

Divide by

$$
\mathcal O_{{\rm sh},n}.
$$

The first factor tends to infinity, while all canonical payment ratios remain bounded.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED CONDITIONAL ON THE DECLARED COMPACT CANONICAL BUDGET}.
}
$$

---

# 16. Filtered enstrophy-surplus compiler

The filtered-vorticity balance of Yu has the exact structural form

$$
\boxed{
E_{\rm out}^{\omega}
+
P
\le
E_{\rm in}^{\omega}
+
V^{+,\rm near}
+
V^{+,\rm far}
+
F^{\rm com}
+
L.
}
\tag{16.1}
$$

The finite-scale coercive estimate absorbs a fixed fraction of the positive singular near-field stretching into diffusion, up to a lower-order filtered-enstrophy reservoir.

The differentiated commutator forcing is likewise bounded by another chosen fraction of diffusion plus a derivative-compatible increment defect.

The resulting positive surplus is therefore controlled by:

$$
\boxed{
\textbf{
far-field strain}
\ \vee\
\textbf{
derivative-compatible commutator increment}
\ \vee\
\textbf{
localization}.
}
\tag{16.2}
$$

This is exactly the correct analytic destination of the DCRP-52 subdiffusive surplus.

Status:

$$
\boxed{
\textbf{EXTERNAL PRIMARY COMPILER}.
}
$$

---

# 17. Consequence for the subdiffusive sheet branch

On the strict compact branch, a diverging

$$
\mathfrak X_{2,n}
$$

cannot remain a silent second-order action.

At least one of the filtered structured residual channels must become nontrivial.

Thus:

$$
\boxed{
\textbf{
subdiffusive sheet}
\Longrightarrow
\textbf{
far-field strain}
\ \vee\
\textbf{
commutator increment defect}
\ \vee\
\textbf{
localization/rank transition}
}
\tag{17.1}
$$

after the DCRP-49--51 geometric alternatives have been inserted.

This closes the **zero-residual subdiffusive sheet**.

---

# 18. Why the diffusive sheet survives

If

$$
h^2\asymp\varepsilon,
$$

then

$$
\mathcal P_2/\mathcal O
=
O(1).
$$

A bounded affine strain can pay an

$$
O(\mathcal O)
$$

diffusion term in the enstrophy balance.

Therefore:

$$
\boxed{
\textbf{
positive second-order action at Batchelor scale is not itself an obstruction.
}
}
\tag{18.1}
$$

This is the second major correction of DCRP-52.

The correct zero-defect diffusive branch is a strain--diffusion equality state.

---

# 19. External viscous-vortex calibration

Classical Burgers vortices are exact stationary Navier--Stokes structures in which a linear strain balances molecular diffusion and maintains a coherent vorticity core.

Rigorous work proves three-dimensional stability of Burgers vortices, and time-dependent linear-strain Burgers-vortex-type profiles have also been studied.

Therefore:

$$
\boxed{
\textbf{
persistent positive vorticity diffusion balanced by strain is a legitimate viscous mechanism.
}
}
\tag{19.1}
$$

DCRP-52 does not identify the strict rank-two sheet with a Burgers vortex.

The literature is used as a NO-GO against taxing the mere existence of a strain--diffusion equilibrium.

---

# 20. Return to the DCRP-48 Fokker--Planck profile

On the coherent one-sign fixed-plane sheet subbranch,

$$
\boxed{
\partial_sf_n
+
\partial_z
[
\sigma(s)zf_n
]
=
\varepsilon_n
e^{-\lambda s}
\partial_{zz}f_n,
}
\tag{20.1}
$$

where

$$
\boxed{
\lambda
=
1-2\gamma,
\qquad
\mu
=
e^{\lambda S_0}.
}
\tag{20.2}
$$

The normal drift over one period satisfies

$$
\boxed{
A_\sigma
=
\exp
\left[
\int_0^{S_0}
\sigma(s)ds
\right]
=
\mu^{-2}.
}
\tag{20.3}
$$

The noise variance generated over one period is

$$
\boxed{
\varepsilon_n
\mathfrak D_{\rm nor},
}
\tag{20.4}
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
\sigma(s)ds
}
d\tau
>0.
}
\tag{20.5}
$$

---

# 21. Stochastic representation

Let

$$
Z_n
$$

be a random variable distributed according to the centered normal profile at the

$$
n
$$

th root.

The linear Fokker--Planck equation gives the exact one-period law

$$
\boxed{
Z_{n+1}
=
\mu^{-2}
Z_n
+
\sqrt{
\varepsilon_n
\mathfrak D_{\rm nor}
}
\,G_n,
}
\tag{21.1}
$$

where

$$
\boxed{
G_n\sim N(0,1)
}
\tag{21.2}
$$

is independent Gaussian noise in the Markov representation.

This is equivalent to the DCRP-48 variance recurrence.

Status:

$$
\boxed{
\textbf{PROVED FROM THE LINEAR FOKKER--PLANCK EQUATION}.
}
$$

---

# 22. Viscosity-scaled normal coordinate

Define

$$
\boxed{
X_n
=
\frac{
Z_n
}{
\sqrt{\varepsilon_n}
}.
}
\tag{22.1}
$$

Since

$$
\boxed{
\varepsilon_{n+1}
=
\mu^{-1}\varepsilon_n,
}
\tag{22.2}
$$

divide (21.1) by

$$
\sqrt{\varepsilon_{n+1}}.
$$

Then

$$
\boxed{
X_{n+1}
=
qX_n
+
\sigma_G G_n,
}
\tag{22.3}
$$

where

$$
\boxed{
q
=
\mu^{-3/2}
\in(0,1),
}
\tag{22.4}
$$

and

$$
\boxed{
\sigma_G^2
=
\mu
\mathfrak D_{\rm nor}.
}
\tag{22.5}
$$

This return map is independent of

$$
n.
$$

This is the **viscosity-scaled normal-profile return operator**.

---

# 23. Markov return operator

For a probability measure

$$
\nu
$$

on

$$
\mathbb R
$$

with finite second moment, define

$$
\boxed{
\mathcal T\nu
=
\operatorname{Law}
(
qX+\sigma_GG
),
}
\tag{23.1}
$$

where

$$
X\sim\nu,
\qquad
G\sim N(0,1),
$$

independently.

The coherent same-parent normal profiles satisfy

$$
\boxed{
\nu_{n+1}
=
\mathcal T\nu_n.
}
\tag{23.2}
$$

---

# 24. NEW THEOREM — Wasserstein Contraction

## Theorem 24.1

For any

$$
\nu_1,\nu_2
\in
\mathcal P_2(\mathbb R),
$$

$$
\boxed{
W_2(
\mathcal T\nu_1,
\mathcal T\nu_2
)
\le
q
W_2(
\nu_1,\nu_2
).
}
\tag{24.1}
$$

### Proof

Take an optimal coupling

$$
(X_1,X_2)
$$

for

$$
\nu_1,\nu_2.
$$

Use the same Gaussian

$$
G
$$

for both images.

Then

$$
[
qX_1+\sigma_GG
]
-
[
qX_2+\sigma_GG
]
=
q(X_1-X_2).
$$

Take the quadratic expectation and infimum.

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

# 25. Unique Gaussian fixed point

The fixed-point variance satisfies

$$
\boxed{
\delta_\ast
=
q^2\delta_\ast
+
\sigma_G^2.
}
\tag{25.1}
$$

Thus

$$
\boxed{
\delta_\ast
=
\frac{
\sigma_G^2
}{
1-q^2
}
=
\frac{
\mu
\mathfrak D_{\rm nor}
}{
1-\mu^{-3}
}.
}
\tag{25.2}
$$

This is exactly the DCRP-48 Batchelor thickness constant.

Define

$$
\boxed{
\nu_\ast
=
N(0,\delta_\ast).
}
\tag{25.3}
$$

Gaussian stability under affine Gaussian convolution gives

$$
\boxed{
\mathcal T\nu_\ast
=
\nu_\ast.
}
\tag{25.4}
$$

---

# 26. NEW THEOREM — Gaussian Batchelor Return Rigidity

## Theorem 26.1

The Markov return operator

$$
\mathcal T
$$

has a unique fixed point in

$$
\mathcal P_2(\mathbb R),
$$

namely

$$
\boxed{
\nu_\ast
=
N(0,\delta_\ast).
}
\tag{26.1}
$$

Moreover, for every initial

$$
\nu_0\in\mathcal P_2(\mathbb R),
$$

$$
\boxed{
W_2(
\nu_n,
\nu_\ast
)
\le
q^n
W_2(
\nu_0,\nu_\ast
).
}
\tag{26.2}
$$

### Proof

Theorem 24.1 makes

$$
\mathcal T
$$

a strict contraction on the complete metric space

$$
\mathcal P_2(\mathbb R).
$$

The explicit Gaussian is a fixed point.

Banach contraction gives uniqueness and exponential convergence.

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

# 27. No nontrivial periodic normal-profile cycles

Suppose

$$
\boxed{
\mathcal T^m\nu
=
\nu
}
\tag{27.1}
$$

for some

$$
m\ge1.
$$

Then

$$
\mathcal T^m
$$

is a contraction with factor

$$
q^m<1.
$$

Its unique fixed point is

$$
\nu_\ast.
$$

Therefore

$$
\boxed{
\nu=\nu_\ast.
}
\tag{27.2}
$$

Thus the coherent diffusive sheet has no non-Gaussian periodic normal-profile orbit.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 28. Normal-profile residual

For a general same-parent coherent sheet define the profile-return mismatch

$$
\boxed{
\mathcal R_{{\rm prof},n}
=
W_2(
\nu_{n+1},
\mathcal T\nu_n
).
}
\tag{28.1}
$$

Exact coherent Fokker--Planck evolution has

$$
\boxed{
\mathcal R_{{\rm prof},n}=0.
}
\tag{28.2}
$$

If the profile remains recurrent but does not converge to the Gaussian fixed point, then

$$
\boxed{
\limsup_n
\mathcal R_{{\rm prof},n}>0
}
\tag{28.3}
$$

or another coherence assumption fails.

Thus non-Gaussian recurrence is an explicit normal-profile/source residual.

---

# 29. Equality-manifold reduction

The coherent zero-residual diffusive branch is therefore not:

$$
\text{an arbitrary sheet with }
h\sim\sqrt{\varepsilon}.
$$

It is:

$$
\boxed{
\textbf{
a viscosity-scaled Gaussian normal vorticity profile}
}
\tag{29.1}
$$

with variance

$$
\delta_\ast
$$

and the DCRP-41 pancake affine strain.

This is the **Batchelor--Gaussian sheet equality manifold**.

---

# 30. Relation to Burgers Gaussian structure

The classical axisymmetric Burgers vortex has an explicit Gaussian vorticity profile in the transverse variable, generated by the balance of linear strain and viscosity.

The DCRP-52 Gaussian appears from a different rank-two sheet geometry and a one-dimensional normal Fokker--Planck return.

Therefore the two should not be identified.

The common structural lesson is:

$$
\boxed{
\textbf{
linear strain + diffusion naturally rigidifies coherent viscous profiles toward Gaussian form.
}
}
\tag{30.1}
$$

This is consistent with rigorous viscous-vortex theory.

---

# 31. Corrected status of the second-order action

The status after DCRP-52 is:

### subdiffusive branch

$$
\boxed{
\mathcal P_2/\mathcal O\to\infty
}
$$

and therefore a genuine surplus/residual is forced.

### diffusive coherent branch

$$
\boxed{
\mathcal P_2/\mathcal O=O(1)
}
$$

and the normal profile contracts to the Gaussian Batchelor fixed point.

### superdiffusive branch

$$
\boxed{
\varepsilon/h^2\to0
}
$$

and the sheet leaves the thin-sheet Euler-shadowing regime or activates the DCRP-48/49 thickness residual.

Thus the raw second-order action has been replaced by a more precise branch classification.

---

# 32. Why raw same-parent depletion is the wrong target

The strict DSS branch is scale recurrent.

Endpoint enstrophy and palinstrophy both scale with

$$
a_n^2/r_n.
$$

Therefore the correct return-rigidity question is not:

> can the parent pay positive palinstrophy again?

It can, at the level of scale bookkeeping.

The correct question is:

> can the unforced same parent reproduce the exact Gaussian strain--diffusion equality, including the required affine strain field, annular source, PFET matching layer, and profile return, with all surplus channels zero?

This is substantially narrower.

---

# 33. Combined final equality state

The strongest coherent strict Type-II rank-two survivor now has:

1.:

   $$
   h_n^2
   \sim
   \delta_\ast
   \varepsilon_n;
   $$

2. viscosity-scaled Gaussian normal profile:

   $$
   \nu_n\to
   N(0,\delta_\ast);
   $$

3. moving/fixed pancake affine strain;

4. finite-annulus affine strain reproduction;

5. DCRP-31 inward PFET;

6. zero second-order surplus;

7. zero rank/lifting/multiplicity/profile residuals.

This is an extremely rigid equality manifold.

---

# 34. Candidate next strain-reproduction question

A Gaussian sheet at Batchelor thickness requires persistent compressive normal strain and planar extension.

But the DCRP parent is unforced.

The strain must be generated by the same recurrent flow.

DCRP-35/36 already reduce the core strain source to a finite annular affine jet with a positive reproduction action.

The next theorem should therefore couple:

$$
\boxed{
\textbf{
Gaussian normal-profile fixed point}
}
$$

to

$$
\boxed{
\textbf{
annular affine-jet reproduction}
}
$$

and

$$
\boxed{
\textbf{
inward PFET}.
}
$$

The final equality branch may then be compared against known forced/externally strained Burgers structures.

---

# 35. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Batchelor--Gaussian Sheet Equality /
Unforced Affine-Strain Reproduction Closure.
}
}
$$

A useful theorem would prove that an unforced same-parent strict Type-II sequence cannot realize indefinitely:

$$
\boxed{
\nu_\ast
=
N(0,\delta_\ast)
}
$$

together with the exact recurrent pancake affine strain unless at least one of:

1. annular strain-source transition;

2. PFET/pressure work;

3. commutator increment defect;

4. localization/tangential leakage;

5. rank or sheet multiplicity transition;

6. non-Gaussian profile residual;

7. a parent-level affine-strain reproduction cost

remains positive.

This is now the narrowest coherent viscous equality problem.

---

# 36. Source-status audit

The filtered-vorticity primary source proves an exact localized filtered enstrophy balance and a finite-scale coercive estimate in which positive near-field vortex stretching is absorbed into filtered diffusion up to a lower-order enstrophy reservoir. The differentiated commutator forcing is also split into a chosen diffusion fraction plus a derivative-compatible increment defect. The remaining positive surplus is assigned to far-field strain, commutator increment, and localization channels.

This validates the DCRP-52 distinction between:

$$
\boxed{
\text{positive diffusion}
}
$$

and

$$
\boxed{
\text{positive post-canonical surplus}.
}
$$

The Burgers-vortex primary literature provides rigorous examples and stability theory for coherent Navier--Stokes vortex structures maintained by linear strain and viscosity. It therefore calibrates the NO-GO against declaring Batchelor-scale positive diffusion itself impossible.

---

# 37. End state

The Type-II scaling audit gives:

$$
\boxed{
E_\omega^{phys}
\sim
\frac{
a_n^2
}{
r_n
}
E_\Omega^{norm},
}
$$

and

$$
\boxed{
\nu
\iint
|\nabla\omega|^2
\sim
\frac{
a_n^2
}{
r_n
}
\mathcal P_{2,n}.
}
$$

Thus raw palinstrophy and endpoint enstrophy are critical peers.

No raw return-depletion theorem follows.

The actual normalized enstrophy balance shows that subdiffusive:

$$
\boxed{
\mathcal P_{2,n}/\mathcal O_{{\rm sh},n}\to\infty
}
$$

forces a genuine surplus, hence structured residual activity.

The diffusive coherent branch instead reduces to the root-to-root Markov map

$$
\boxed{
X_{n+1}
=
\mu^{-3/2}X_n
+
\sqrt{
\mu
\mathfrak D_{\rm nor}
}
G_n.
}
$$

This map is a strict

$$
W_2
$$

contraction.

Its unique recurrent profile is

$$
\boxed{
N(0,\delta_\ast),
\qquad
\delta_\ast
=
\frac{
\mu
\mathfrak D_{\rm nor}
}{
1-\mu^{-3}
}.
}
$$

Therefore the strongest coherent zero-residual viscous sheet is a **Batchelor-scale Gaussian sheet**.

The next frontier is:

$$
\boxed{
\textbf{
Batchelor--Gaussian Sheet Equality /
Unforced Affine-Strain Reproduction Closure.
}
}
$$
