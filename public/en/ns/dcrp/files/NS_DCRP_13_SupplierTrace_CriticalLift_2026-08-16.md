# NS-DCRP-13 — Supplier Trace Critical Lift, Finite-Family Anti-Diffusion, and Adjoint-Trace Bridge

- date: 2026-08-16
- status: research proof checkpoint
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective: bypass the DCRP-12 work-multiplicity obstruction by extracting a scale-uniform finite-family trace witness directly from the dissipation-boundary supplier atom.
- no full Navier--Stokes regularity claim is made.
- principal internal dependencies:
  - FCBP-02 filtered adjoint localization;
  - FCBP-04 heat-filter / moving-window architecture;
  - FCBP-05 combined observation hierarchy with selected adjoint-trace channel;
  - FCBP-06 CAR0--CAR3 / Native CAR Compiler;
  - MORP-01 through MORP-05;
  - DCRP-08 through DCRP-12.
- external primary calibration:
  - Cheskidov--Dai, arXiv:1507.06611v6;
  - Cheskidov--Shvydkoy, arXiv:1102.1944v2.

---

# 1. Executive result

DCRP-12 showed that a fixed amount of global critical heat-work may be spread over arbitrarily many normalized cells, so

$$
\boxed{
\text{fixed global work}
\not\Rightarrow
\text{uniform local work coefficient}.
}
\tag{1.1}
$$

That multiplicity obstruction does **not** apply to the dissipation-boundary supplier endpoint itself.

DCRP-08 established that at a dissipation-boundary shell

$$
Q=Q(t),
\qquad
\Lambda=\lambda_Q,
$$

one has

$$
\boxed{
\|u_Q(t)\|_\infty
\ge
c_0\nu\Lambda.
}
\tag{1.2}
$$

Define the critically rescaled shell

$$
\boxed{
w(y)
=
\Lambda^{-1}
u_Q
\left(
x_\ast+\Lambda^{-1}y,
t
\right).
}
\tag{1.3}
$$

After choosing

$$
x_\ast
$$

at a point of almost maximal shell amplitude,

$$
\boxed{
\|w\|_\infty
\ge
c_0\nu.
}
\tag{1.4}
$$

The Fourier support of

$$
w
$$

lies in one fixed annulus independent of

$$
Q.
$$

Therefore Bernstein gives

$$
\boxed{
\|\nabla w\|_\infty
\le
C_B
\|w\|_\infty.
}
\tag{1.5}
$$

This implies a uniform finite-family trace theorem:

there exist universal constants

$$
r_\ast>0,
\qquad
c_\ast>0,
$$

a fixed nonnegative bump

$$
\eta\in C_c^\infty(B_{r_\ast}),
$$

and one of only six signed coordinate functionals

$$
\boxed{
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta(y)
w_i(y)
\,dy,
\qquad
i\in\{1,2,3\},
\quad
\sigma\in\{-1,+1\},
}
\tag{1.6}
$$

such that

$$
\boxed{
\mathcal L_{i,\sigma}(w)
\ge
c_\ast\nu.
}
\tag{1.7}
$$

Thus:

$$
\boxed{
\textbf{
every dissipation-boundary supplier carries a fixed,
scale-uniform, six-test local trace atom.
}
}
\tag{1.8}
$$

This is fundamentally different from DCRP-12's diffuse work measure.

No number of distant work cells can make all six supplier-centered trace coefficients vanish.

The witness is:

- generated from the actual Navier--Stokes state;
- located at the actual supplier scale;
- located at an actual supplier center;
- fixed-shape after normalization;
- finite-dimensional;
- quantitatively scale uniform.

The same terminal bump can be propagated backward by the heat adjoint:

$$
\boxed{
\phi_{i,\sigma}(\tau)
=
e^{-\tau\Delta}
(
\sigma\eta e_i
)
}
\tag{1.9}
$$

in backward-time notation, producing a canonical selected caloric-adjoint trace family.

Therefore the old abstract CAR1 problem has a concrete solution **for the supplier state coordinate**:

$$
\boxed{
\textbf{
supplier atom}
\Longrightarrow
\textbf{
uniform finite-family native trace separation}.
}
}
\tag{1.10}
$$

The remaining issue is no longer anti-diffusion.

It is compiler compatibility:

> Does the specific `selected adjoint trace` channel used by the FCBP/MORP finite-window audit admit this fixed terminal family, or a uniformly equivalent filtered version?

If yes, then the supplier mechanism cannot lie in the exact combined-invisible kernel

$$
O_W^T=0.
$$

If no, the mismatch is now finite and explicit: it is a trace-family admissibility problem, not a diffuse-carrier problem.

---

# 2. Supplier endpoint from the dissipation wavenumber

For the Navier--Stokes dissipation wavenumber in the

$$
r=\infty
$$

form,

$$
\Lambda(t)
=
\lambda_{Q(t)},
$$

Cheskidov--Dai / Cheskidov--Shvydkoy give the boundary estimate

$$
\boxed{
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t)
}
\tag{2.1}
$$

whenever

$$
1<\Lambda(t)<\infty.
$$

DCRP-08 already converted this by Bernstein into

$$
\boxed{
\Lambda
\|u_Q\|_2^2
\ge
c_1\nu^2.
}
\tag{2.2}
$$

The present round uses the stronger pointwise form (2.1).

---

# 3. Critical rescaling

Let

$$
x_\ast
$$

satisfy

$$
|u_Q(x_\ast,t)|
\ge
\frac34
\|u_Q(t)\|_\infty.
$$

Define

$$
\boxed{
w(y)
=
\Lambda^{-1}
u_Q
\left(
x_\ast+\Lambda^{-1}y,
t
\right).
}
\tag{3.1}
$$

Then

$$
\boxed{
|w(0)|
\ge
\frac34c_0\nu.
}
\tag{3.2}
$$

The Fourier support of

$$
w
$$

lies in a fixed annulus

$$
\boxed{
\mathcal A
=
\{
\xi:
c_-\le|\xi|\le c_+
\},
}
\tag{3.3}
$$

where

$$
0<c_-<c_+<\infty
$$

depend only on the chosen Littlewood--Paley partition.

Consequently all Bernstein constants below are universal.

---

# 4. Finite coordinate selection

For every vector

$$
a\in\mathbb R^3,
$$

there exists

$$
i\in\{1,2,3\}
$$

such that

$$
|a_i|
\ge
\frac{
|a|
}{
\sqrt3
}.
$$

Apply this to

$$
a=w(0).
$$

There exist

$$
i_\ast\in\{1,2,3\}
$$

and

$$
\sigma_\ast\in\{-1,+1\}
$$

such that

$$
\boxed{
\sigma_\ast
w_{i_\ast}(0)
\ge
\frac{
3c_0
}{
4\sqrt3
}
\nu.
}
\tag{4.1}
$$

The pair

$$
(i_\ast,\sigma_\ast)
$$

belongs to a fixed family of exactly six possibilities.

---

# 5. Bernstein persistence

Because

$$
w
$$

is supported in the fixed annulus

$$
\mathcal A,
$$

Bernstein gives

$$
\boxed{
\|\nabla w\|_\infty
\le
C_B
\|w\|_\infty.
}
\tag{5.1}
$$

Also

$$
\|w\|_\infty
\le
\frac43
|w(0)|
$$

if

$$
x_\ast
$$

is chosen sufficiently close to the essential supremum point; alternatively one may carry a harmless factor two in all constants.

Thus there is a universal constant

$$
C_1
$$

such that

$$
\boxed{
\|\nabla w\|_\infty
\le
C_1
|w(0)|.
}
\tag{5.2}
$$

Choose

$$
\boxed{
r_\ast
=
\frac1{
8\sqrt3C_1
}.
}
\tag{5.3}
$$

For

$$
|y|\le r_\ast,
$$

$$
|w_{i_\ast}(y)-w_{i_\ast}(0)|
\le
\|\nabla w\|_\infty
|y|
\le
\frac{
|w(0)|
}{
8\sqrt3
}.
$$

Using (4.1),

$$
\boxed{
\sigma_\ast
w_{i_\ast}(y)
\ge
c_2\nu
}
\tag{5.4}
$$

throughout

$$
B_{r_\ast}(0)
$$

for a universal

$$
c_2>0.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. NEW THEOREM — Finite-Family Supplier Trace Lift

Choose a fixed function

$$
\eta
\in
C_c^\infty(B_{r_\ast}(0)),
$$

with

$$
\eta\ge0
$$

and

$$
\boxed{
\int
\eta(y)\,dy
=
1.
}
\tag{6.1}
$$

For

$$
i\in\{1,2,3\},
\qquad
\sigma\in\{-1,+1\},
$$

define

$$
\boxed{
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta(y)
w_i(y)
\,dy.
}
\tag{6.2}
$$

## Theorem 6.1

For every dissipation-boundary supplier shell, after the admissible critical rescaling and spatial re-centering above,

$$
\boxed{
\max_{
1\le i\le3,
\ \sigma=\pm1
}
\mathcal L_{i,\sigma}(w)
\ge
c_2\nu.
}
\tag{6.3}
$$

### Proof

Use the selected pair

$$
(i_\ast,\sigma_\ast)
$$

from Section 5.

Since

$$
\eta\ge0,
$$

has unit mass, and

$$
\sigma_\ast w_{i_\ast}\ge c_2\nu
$$

throughout its support,

$$
\mathcal L_{i_\ast,\sigma_\ast}(w)
\ge
c_2\nu.
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

# 7. Why this is a genuine anti-diffusion theorem

The work multiplicity obstruction of DCRP-12 concerns a measure whose fixed total mass may be split into

$$
N\to\infty
$$

separate cells.

Theorem 6.1 does not estimate a sum of work cells.

It uses one dynamically selected supplier endpoint.

Once the supplier center is chosen, one of six fixed local coordinate tests has a uniform lower bound.

Therefore:

$$
\boxed{
\text{supplier endpoint}
\Longrightarrow
\text{one local coefficient }\ge c\nu
}
\tag{7.1}
$$

independently of:

- number of other active cells;
- total work multiplicity;
- spatial distribution of the remaining solution;
- pressure--flux cancellation elsewhere.

Thus:

$$
\boxed{
\textbf{
supplier-state trace visibility cannot be defeated by work fragmentation.
}
}
\tag{7.2}
$$

This bypasses rather than solves the global heat-work multiplicity problem.

---

# 8. Physical-variable form

Recall

$$
w(y)
=
\Lambda^{-1}
u_Q
\left(
x_\ast+\Lambda^{-1}y,t
\right).
$$

Then

$$
\begin{aligned}
\mathcal L_{i,\sigma}(w)
&=
\sigma
\int
\eta(y)
\Lambda^{-1}
u_{Q,i}
\left(
x_\ast+\Lambda^{-1}y,t
\right)
dy\\
&=
\sigma
\Lambda^2
\int
\eta
\left(
\Lambda(x-x_\ast)
\right)
u_{Q,i}(x,t)
dx.
\end{aligned}
$$

Hence Theorem 6.1 is equivalently

$$
\boxed{
\max_{i,\sigma}
\sigma
\Lambda^2
\int
\eta
\left(
\Lambda(x-x_\ast)
\right)
u_{Q,i}(x,t)
dx
\ge
c_2\nu.
}
\tag{8.1}
$$

The normalization

$$
\Lambda^2
$$

is exactly the one dictated by the Navier--Stokes scaling of this local linear trace.

---

# 9. Filtered-state interpretation

Let

$$
P_{\mathcal A}
$$

denote the fixed unit-annulus Littlewood--Paley projector in normalized variables.

The supplier shell is

$$
w
=
P_{\mathcal A}v,
$$

where

$$
v
$$

is the full normalized velocity state.

Therefore:

$$
\boxed{
\mathcal L_{i,\sigma}(w)
=
\sigma
\int
\eta
\left(
P_{\mathcal A}v
\right)_i.
}
\tag{9.1}
$$

This is a **filtered selected-time trace** of the actual normalized Navier--Stokes state.

It is generated from the state by a fixed Fourier filter and a fixed local test.

No dangerous/singular label is copied into the coordinate.

Thus it passes the FCBP-06 Copied-Gate safety requirement.

---

# 10. Native CAR1 interpretation

FCBP-06 isolates CAR1 as the missing statement:

$$
\boxed{
\operatorname{dist}_{\rm native}
\ge
a_0
\mu_{\rm dang}
-
\mathcal R^{extract},
}
$$

with the requirement that the native geometry must be generated from Navier--Stokes rather than from a copied dangerous mark.

Theorem 6.1 provides a concrete supplier-side separation:

$$
\boxed{
\mathsf T_{\rm sup}(v)
:=
\max_{i,\sigma}
\mathcal L_{i,\sigma}
(
P_{\mathcal A}v
)
\ge
c_2\nu.
}
\tag{10.1}
$$

The quantity

$$
\mathsf T_{\rm sup}
$$

is:

- state-generated;
- scale normalized;
- spatially re-rooted by an allowed symmetry;
- finite-dimensional;
- quantitatively uniform.

Thus, for any native package norm that contains the six filtered trace coefficients as genuine components,

$$
\boxed{
\operatorname{dist}_{\rm native}
\ge
c_3\nu
}
\tag{10.2}
$$

away from the subspace where all six supplier traces vanish.

Status:

$$
\boxed{
\textbf{CAR1 PROVED FOR THIS CONCRETE SUPPLIER-TRACE SUBGEOMETRY}.
}
$$

This is not yet a theorem about the entire external admissible quotient

$$
\Gamma_W.
$$

That compiler identification remains explicit.

---

# 11. Finite-dimensional anti-phantom advantage

The old work-carrier branch had an effective number of cells

$$
\mathfrak M_{\rm work}
$$

that could diverge.

The supplier trace vector is only:

$$
\boxed{
\mathbf T_{\rm sup}
=
\left(
\mathcal L_{1,+},
\mathcal L_{1,-},
\mathcal L_{2,+},
\mathcal L_{2,-},
\mathcal L_{3,+},
\mathcal L_{3,-}
\right).
}
\tag{11.1}
$$

Its dimension is fixed:

$$
\boxed{
\dim
\mathbf T_{\rm sup}
=
6.
}
\tag{11.2}
$$

Theorem 6.1 gives

$$
\boxed{
\|\mathbf T_{\rm sup}\|_{\ell^\infty}
\ge
c_2\nu.
}
\tag{11.3}
$$

Thus no moving-window multiplicity constant occurs at the extraction stage.

This is precisely the geometry that FCBP-06's Native CAR Detector Compiler is designed to exploit once the trace vector is identified with an admissible detector/quotient component.

---

# 12. Backward caloric adjoint family

For each terminal test

$$
\psi_{i,\sigma}
=
\sigma
\eta e_i,
$$

define the backward heat-adjoint family on normalized time

$$
\tau\le0
$$

by

$$
\boxed{
\Psi_{i,\sigma}(y,\tau)
=
e^{-\tau\Delta}
\psi_{i,\sigma}(y),
\qquad
\tau\le0.
}
\tag{12.1}
$$

Then

$$
\boxed{
\partial_\tau
\Psi_{i,\sigma}
+
\Delta
\Psi_{i,\sigma}
=
0,
}
\tag{12.2}
$$

and

$$
\boxed{
\Psi_{i,\sigma}(y,0)
=
\psi_{i,\sigma}(y).
}
\tag{12.3}
$$

The terminal filtered trace is

$$
\boxed{
\left<
P_{\mathcal A}v(0),
\Psi_{i,\sigma}(0)
\right>
=
\mathcal L_{i,\sigma}
(
P_{\mathcal A}v(0)
).
}
\tag{12.4}
$$

Therefore one of this fixed six-element terminal adjoint family satisfies

$$
\boxed{
\left<
P_{\mathcal A}v(0),
\Psi_{i,\sigma}(0)
\right>
\ge
c_2\nu.
}
\tag{12.5}
$$

This gives a canonical route from the supplier trace atom to a selected caloric-adjoint trace.

---

# 13. Relation to FCBP filtered adjoint localization

FCBP-02 already uses a backward filtered adjoint weight to cancel the principal localization residual.

FCBP-04 / FCBP-05 explicitly retain a selected adjoint-trace channel in the combined observability hierarchy.

Therefore the structure required by DCRP-13 is not foreign to the existing compiler.

However the current corpus does not state, in one theorem, that the exact selected-adjoint family

$$
\Psi_{i,\sigma}
$$

from Section 12 is an admissible basis for

$$
O_W^T.
$$

The final identification must therefore be stated conditionally.

---

# 14. Conditional theorem — direct collision with the trace-zero kernel

## Theorem 14.1

Assume the FCBP/MORP selected adjoint-trace channel

$$
O_W^T
$$

contains, after the standard scale/translation normalization, the six terminal caloric trace functionals generated by:

$$
\psi_{i,\sigma}
=
\sigma\eta e_i.
$$

Then every dissipation-boundary supplier state satisfies

$$
\boxed{
O_W^T
\ge
c_T\nu
}
\tag{14.1}
$$

for a universal:

$$
c_T>0.
$$

Consequently no such supplier state belongs to the exact trace-invisible kernel

$$
\boxed{
O_W^T=0.
}
\tag{14.2}
$$

### Proof

Theorem 6.1 gives one terminal coefficient at least

$$
c_2\nu.
$$

By the assumed channel inclusion, the trace observation norm dominates that coefficient up to a fixed normalization constant.

$$
\square
$$

Status:

$$
\boxed{
\textbf{CONDITIONAL ONLY ON TRACE-FAMILY COMPILER ADMISSIBILITY}.
}
$$

No scale-uniform observability constant is otherwise needed for this direct finite-family branch.

---

# 15. Corollary — supplier sequence cannot be combined-invisible if the trace family is admissible

DCRP-08 proved that a hypothetical finite-time singularity requires a sequence

$$
t_n\uparrow T
$$

with:

$$
\Lambda_n\to\infty
$$

and supplier shells

$$
Q_n=Q(t_n).
$$

Under Theorem 14.1's compiler assumption, every normalized supplier state satisfies:

$$
\boxed{
O_{W,n}^T
\ge
c_T\nu.
}
\tag{15.1}
$$

Hence:

$$
\boxed{
\textbf{
the supplier sequence cannot enter any combined-invisible branch that requires }
O_W^T\to0.
}
\tag{15.2}
$$

This directly attacks the FCBP-06 combined-invisible cascade survivor.

Status:

$$
\boxed{
\textbf{CONDITIONAL ON THE SAME TRACE-COMPILER IDENTIFICATION}.
}
$$

---

# 16. Why this is stronger than local positive energy alone

A positive local

$$
L^2
$$

mass statement gives:

$$
\int_{B_R}
|w|^2
\ge
c\nu^2.
$$

To convert that to a finite set of **linear** detector coefficients one would normally need a finite-dimensional approximation argument.

The dissipation-boundary

$$
L^\infty
$$

lower bound is stronger.

Because the field is band-limited, pointwise largeness persists on a fixed ball with a fixed coordinate sign.

Therefore a fixed **six-element linear test family** already detects it.

No compactness, singular-value decomposition, or increasing detector dimension is needed.

---

# 17. The detector shape is not solution dependent

The following are fixed once and for all:

- the reference bump:

  $$
  \eta;
  $$

- the six component/sign choices:

  $$
  (i,\sigma);
  $$

- the unit-annulus filter:

  $$
  P_{\mathcal A}.
  $$

The solution determines only:

- the admissible spatial re-centering:

  $$
  x_\ast;
  $$

- the admissible parabolic scale:

  $$
  \Lambda^{-1};
  $$

- which one of the six tests is positive.

Thus the detector **family** is fixed and finite.

This avoids the tautology:

> choose the test to be the solution itself.

No such solution-dependent shape is used.

---

# 18. Rotational normalization

If the MORP state normalization also allows spatial rotations, the six-test family can be reduced conceptually to one coordinate test after rotation.

However no rotation is required.

Keeping all six signed coordinate tests has two advantages:

1. it avoids a separate rotational selection theorem;
2. it makes finite-dimensionality explicit.

Thus:

$$
\boxed{
6
}
$$

is a safe universal detector count.

---

# 19. Quantitative stability under approximate supplier threshold

Suppose only:

$$
\|u_Q\|_\infty
\ge
(c_0-\varepsilon)\nu\Lambda
$$

with:

$$
0\le\varepsilon<c_0/2.
$$

Then the same proof gives:

$$
\boxed{
\max_{i,\sigma}
\mathcal L_{i,\sigma}(w)
\ge
c(\,c_0-\varepsilon\,)\nu
\ge
c'\nu.
}
\tag{19.1}
$$

Therefore the trace lift is stable under fixed relative threshold errors.

This is useful if the dissipation-wavenumber definition is implemented with harmless dyadic / mollifier constants.

---

# 20. Quantitative stability under finite shell overlap

A smooth Littlewood--Paley decomposition may represent the dissipation-boundary frequency by a bounded cluster

$$
|p-Q|\le C_0
$$

rather than a single sharp shell.

If:

$$
\max_{|p-Q|\le C_0}
\lambda_p^{-1}
\|u_p\|_\infty
\ge
c\nu,
$$

then one of the finitely many cluster shells satisfies the same lower bound with a modified universal constant.

The trace construction can therefore use a finite family enlarged by the bounded relative shell offsets.

The detector dimension remains universal:

$$
\boxed{
6(2C_0+1).
}
\tag{20.1}
$$

No scale-dependent growth occurs.

---

# 21. Duhamel-adjoint identity for the matched supplier shell

Let:

$$
t_1
$$

be a supplier time and:

$$
q=Q(t_1).
$$

Let:

$$
t_0<t_1.
$$

Define the backward heat evolution of the **terminal supplier shell**:

$$
\boxed{
\varphi_q(s)
=
e^{\nu(t_1-s)\Delta}
u_q(t_1).
}
\tag{21.1}
$$

Then:

$$
\partial_s\varphi_q
+
\nu\Delta\varphi_q
=
0.
$$

Let:

$$
F_q
=
\Delta_q
\mathbb P
\nabla\cdot(u\otimes u).
$$

The projected velocity satisfies:

$$
\partial_su_q
-
\nu\Delta u_q
+
F_q
=
0.
$$

Therefore:

$$
\frac d{ds}
\left<
u_q(s),
\varphi_q(s)
\right>
=
-
\left<
F_q(s),
\varphi_q(s)
\right>.
$$

Integrating:

$$
\boxed{
\|u_q(t_1)\|_2^2
-
\left<
u_q(t_0),
e^{\nu(t_1-t_0)\Delta}
u_q(t_1)
\right>
=
-
\int_{t_0}^{t_1}
\left<
F_q(s),
\varphi_q(s)
\right>
ds.
}
\tag{21.2}
$$

This is an exact signed adjoint ancestry identity.

---

# 22. NEW THEOREM — matched-adjoint nonlinear payment

Let:

$$
A_q(t)
=
\lambda_q^{1/2}
\|u_q(t)\|_2.
$$

Assume at:

$$
t_1
$$

the supplier satisfies:

$$
A_q(t_1)
\ge
a_0\nu.
$$

Let:

$$
K_0
=
\|u(0)\|_2^2.
$$

Choose:

$$
\tau_q
=
\frac1{
c_h\nu\lambda_q^2
}
\log
\left(
\frac{
2\lambda_q^{1/2}K_0^{1/2}
}{
a_0\nu
}
\right)
$$

as in DCRP-09, and set:

$$
t_0=t_1-\tau_q.
$$

Then:

$$
\boxed{
-\lambda_q
\int_{t_0}^{t_1}
\left<
F_q(s),
\varphi_q(s)
\right>
ds
\ge
\frac12
a_0^2\nu^2.
}
\tag{22.1}
$$

### Proof

By shell heat decay:

$$
\left\|
e^{\nu\tau_q\Delta}
u_q(t_1)
\right\|_2
\le
e^{-c_h\nu\lambda_q^2\tau_q}
\|u_q(t_1)\|_2.
$$

Hence:

$$
\left|
\left<
u_q(t_0),
e^{\nu\tau_q\Delta}
u_q(t_1)
\right>
\right|
\le
K_0^{1/2}
e^{-c_h\nu\lambda_q^2\tau_q}
\|u_q(t_1)\|_2.
$$

By definition of:

$$
\tau_q,
$$

the right side is at most:

$$
\frac12
\|u_q(t_1)\|_2^2.
$$

Equation (21.2) gives:

$$
-\int_{t_0}^{t_1}
\left<
F_q,
\varphi_q
\right>
ds
\ge
\frac12
\|u_q(t_1)\|_2^2.
$$

Multiply by:

$$
\lambda_q.
$$

Since:

$$
\lambda_q
\|u_q(t_1)\|_2^2
=
A_q(t_1)^2
\ge
a_0^2\nu^2,
$$

the result follows.

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

# 23. Significance of the matched-adjoint payment

DCRP-09 proved an unsigned source-norm lower bound:

$$
\lambda_q^{1/2}
\int
\|F_q\|_2
dt
\gtrsim
\nu.
$$

Theorem 22.1 gives a stronger **signed dual pairing**:

$$
\boxed{
-\lambda_q
\int
\left<
F_q,
e^{\nu(t_1-s)\Delta}
u_q(t_1)
\right>
ds
\gtrsim
\nu^2.
}
\tag{23.1}
$$

This pairing is:

- exact;
- actual-history;
- scale critical;
- sign definite after the heat-memory term is removed;
- naturally adjoint.

Thus the supplier branch generates both:

$$
\boxed{
\text{terminal finite-family trace atom}
}
$$

and:

$$
\boxed{
\text{signed matched-adjoint nonlinear payment}.
}
$$

This is much less compatible with an adjoint-trace-invisible minimal obstruction than a diffuse unsigned work measure.

---

# 24. Why the matched adjoint is not yet an admissible detector by itself

The terminal state:

$$
u_q(t_1)
$$

appears inside:

$$
\varphi_q.
$$

Therefore the matched adjoint shape is solution dependent.

Using it directly as a detector would risk the same kind of tautological adaptivity that FCBP-06 warns against.

For this reason:

- Theorem 22.1 is retained as a native signed identity;
- Theorem 6.1 is the actual finite-family detector extraction.

The six-test trace lift removes the solution dependence from the detector family.

A future compiler theorem may use Theorem 22.1 to prove that one of the six fixed adjoint channels inherits nonzero nonlinear payment, but that step is not claimed here.

---

# 25. Updated Critical Lift status

The original FCBP Critical Lift problem asked for a non-tautological, scale-uniform route from dangerous causal data to an auditable local observable.

The DCRP chain has now produced:

1. hypothetical singularity:

   $$
   \Longrightarrow
   $$

2. arbitrarily high dissipation-boundary suppliers:

   $$
   \Longrightarrow
   $$

3. critical endpoint shell atom:

   $$
   \Longrightarrow
   $$

4. fixed local pointwise normalized amplitude:

   $$
   \Longrightarrow
   $$

5. finite six-test trace lower bound:

   $$
   \boxed{
   \max_{i,\sigma}
   \mathcal L_{i,\sigma}
   \ge
   c\nu.
   }
   $$

This is a genuine native, scale-uniform extraction statement.

Therefore the supplier branch has solved the **geometry** of CAR1.

What remains is a finite compiler question:

$$
\boxed{
\textbf{
is the supplier trace family contained in, or uniformly controlled by,
the already-declared }O_W^T\textbf{ adjoint-trace channel?}
}
\tag{25.1}
$$

---

# 26. If the compiler answer is yes

If:

$$
O_W^T
\gtrsim
\max_{i,\sigma}
\mathcal L_{i,\sigma},
$$

then:

$$
\boxed{
O_W^T
\ge
c\nu
}
\tag{26.1}
$$

on every supplier state.

Since a hypothetical first singularity forces suppliers at arbitrarily high scales:

$$
\boxed{
\liminf_{n\to\infty}
O_{W,n}^T
\ge
c\nu.
}
\tag{26.2}
$$

Thus the supplier branch cannot enter a moving-window combined-invisible cascade with:

$$
O_{W,n}^{comb}\to0.
$$

At that point the remaining global closure work would return to:

- paid-side recurrence;
- transition realization;
- whether every hypothetical singular branch must pass through the supplier-normalized MORP minimal object.

The diffuse-work multiplicity obstruction would no longer be relevant to supplier observability.

---

# 27. If the compiler answer is no

If the declared:

$$
O_W^T
$$

does **not** admit the six fixed caloric terminal traces, then the gap is now explicit.

One must explain which of the following fails:

1. filtered velocity traces are not part of the trace state;
2. the allowed terminal adjoint family excludes fixed compact bumps;
3. the trace is defined only for a different tensor/source variable;
4. the filter class cannot include the fixed unit-annulus shell;
5. normalization loses the trace under actual return/re-root.

Any such failure is a finite interface mismatch.

It is no longer:

$$
\boxed{
\text{unknown diffuse NS obstruction}.
}
$$

---

# 28. Relation to DCRP-12

DCRP-12 remains useful for the physical work ledger.

Its result is:

$$
\boxed{
\text{local PFET}
\vee
\text{paid backscatter}
\vee
\text{work escape}.
}
$$

DCRP-13 does not invalidate that theorem.

It proves a different statement:

$$
\boxed{
\text{work may diffuse, but the supplier state itself has a fixed trace atom}.
}
$$

Thus the two routes are complementary.

### Work route

tracks **how the supplier is paid**.

### Trace route

tracks **whether the supplier can be observationally invisible**.

The trace route is immune to work-cell multiplicity.

---

# 29. New exact frontier

The previous frontier was:

$$
\text{Quantitative Work Anti-Diffusion / Critical Lift}.
$$

The supplier trace theorem bypasses the anti-diffusion half.

The next exact target is now:

$$
\boxed{
\textbf{
Supplier Trace / FCBP Adjoint-Channel Identification Lemma}.
}
$$

Desired statement:

> After the standard supplier scale/translation normalization, the six fixed terminal filtered trace functionals
>
> $$
> \mathcal L_{i,\sigma}
> $$
>
> belong to the admissible selected-adjoint trace family defining
>
> $$
> O_W^T,
> $$
>
> or are uniformly dominated by that trace norm.
>
> Therefore:
>
> $$
> O_W^T
> \ge
> c\nu
> $$
>
> on every dissipation-boundary supplier.

This is now a finite compiler theorem.

No new PDE mechanism is required.

---

# 30. Source ledger

## Cheskidov--Dai

Alexey Cheskidov and Mimi Dai, *Regularity criteria for the 3D Navier-Stokes and MHD equations*, arXiv:1507.06611v6.

Used for the dissipation-wavenumber architecture and the Navier--Stokes high-frequency boundary condition.

## Cheskidov--Shvydkoy

Alexey Cheskidov and Roman Shvydkoy, *A unified approach to regularity problems for the 3D Navier-Stokes and Euler equations: the use of Kolmogorov's dissipation range*, arXiv:1102.1944v2.

Contains the explicit boundary estimate:

$$
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t)
$$

on the active dissipation-wavenumber set.

## Internal FCBP-02

Already uses a backward filtered adjoint cutoff and proves cancellation of the principal localization residual.

## Internal FCBP-05

Declares the combined observation hierarchy:

$$
O_W^{comb}
=
(
O_W^P,
O_W^F,
O_W^E,
O_W^T
),
$$

including the selected adjoint-trace channel.

## Internal FCBP-06

Factorizes Critical Lift into:

$$
\mathrm{CAR0}
\to
\mathrm{CAR1}
\to
\mathrm{CAR2}
\to
\mathrm{CAR3}.
$$

The supplier trace theorem provides a concrete scale-uniform native separation for a specific NS-generated state coordinate and respects the Copied-Gate prohibition.

---

# 31. End state

The key new theorem is:

$$
\boxed{
\textbf{
Dissipation-boundary supplier}
\Longrightarrow
\textbf{
finite-family local trace atom}.
}
$$

Quantitatively:

$$
\boxed{
\max_{
1\le i\le3,\,
\sigma=\pm1
}
\sigma
\int
\eta(y)
\left[
P_{\mathcal A}v(y)
\right]_i
dy
\ge
c\nu.
}
$$

The family has fixed dimension:

$$
\boxed{
6.
}
$$

No work multiplicity can dilute this coefficient.

In addition, the supplier has a signed matched-adjoint nonlinear payment:

$$
\boxed{
-\lambda_Q
\int
\left<
F_Q(s),
e^{\nu(t_Q-s)\Delta}
u_Q(t_Q)
\right>
ds
\ge
c\nu^2.
}
$$

Thus the supplier mechanism is simultaneously:

- state-visible;
- trace-visible to a finite fixed family;
- dynamically and nonlinearly generated.

The next single frontier is:

$$
\boxed{
\textbf{
Supplier Trace / FCBP Adjoint-Channel Identification Lemma}.
}
$$

If this finite compiler bridge holds, the dissipation-boundary supplier branch cannot be combined-invisible.