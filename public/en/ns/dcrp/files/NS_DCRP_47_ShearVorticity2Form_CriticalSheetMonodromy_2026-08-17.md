# NS-DCRP-47 — Shear–Vorticity Two-Form Invariance, Normal Cotangent Contraction, and Critical Sheet Monodromy

- date: 2026-08-17
- status: research proof checkpoint / Euler equality-manifold identification round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit the DCRP-46 proposal that vanishing material volume should force physical carrier concentration;
  2. identify the natural physical carrier of the pure rank-two pancake branch as a codimension-one vorticity-flux form rather than a three-dimensional volume density;
  3. derive the continuous self-similar vorticity two-form equation;
  4. combine it with the pure anchored shear scalar equation to prove an exactly Lie-advected weighted shear--vorticity two-form;
  5. derive the one-period normal-cotangent contraction law from the scalar and vorticity cocycles;
  6. derive the remaining quotient-line multiplier from the similarity Jacobian;
  7. identify a complete critical sheet-monodromy exponent identity;
  8. prove a material-surface weighted-flux invariant;
  9. record the exactness/relative-surface limitation of this flux;
  10. correct the logical role of DCRP-46 volume intermittency;
  11. identify the next genuinely Navier--Stokes-specific frontier as viscous shadowing of the sheet-form invariant and conditional subdiffusive thickness mismatch.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.
- external geometric calibration:
  - A. Enciso, A. J. Fernández, D. Meyer, *Vortex-sheet desingularization for three-dimensional ideal fluids*, arXiv:2607.19233.
- internal dependencies:
  - DCRP-32/34 self-similar Kelvin scaling audit;
  - DCRP-40 fixed-plane rank-two potential--shear representation;
  - DCRP-42/43 pure anchored pancake scalar cocycle;
  - DCRP-46 material-intermittency theorem.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction

DCRP-46 proved that on the coherent bounded-planar-enstrophy super-DSS exhaust branch, the material-label fraction may satisfy

$$
\boxed{
\theta_m
\lesssim
(1+m)\mu_r^{-2m},
}
\tag{1.1}
$$

where

$$
\boxed{
\mu_r
=
e^{(1-2\gamma)S_0}
>
1.
}
\tag{1.2}
$$

It was tempting to infer:

> if the three-dimensional material fraction vanishes, then every remaining label must carry a growing amount of physical vorticity.

DCRP-47 shows that this inference is too strong.

The pure rank-two pancake branch possesses a natural **codimension-one weighted flux invariant**.

Its carrier is a two-form, not a three-dimensional volume density.

Therefore:

$$
\boxed{
\textbf{
vanishing three-dimensional material fraction}
\not\Rightarrow
\textbf{
physical vorticity concentration}
}
\tag{1.3}
$$

without a further surface-area/thickness/trace theorem.

Status:

$$
\boxed{
\textbf{CORRECTION}.
}
$$

The correct Euler equality object is constructed below.

---

# 2. Fixed-plane pure pancake branch

Work on a regular fixed-plane rank-two patch.

Choose coordinates

$$
y=(x_1,x_2,z)
$$

with plane normal

$$
n=e_3.
$$

The vorticity is

$$
\boxed{
\Omega
=
\left(
\partial_2q,
-\partial_1q,
0
\right).
}
\tag{2.1}
$$

Let

$$
\widetilde q
$$

be the DCRP-43 anchor-relative gauge completion and let

$$
\eta(s)>0
$$

be the periodic scalar factor from DCRP-42.

Define

$$
\boxed{
r
=
\eta(s)\widetilde q.
}
\tag{2.2}
$$

On the pure anchored branch

$$
\boxed{
D_sr
=
\lambda_\gamma r,
}
\tag{2.3}
$$

where

$$
\boxed{
D_s
=
\partial_s+W\cdot\nabla,
\qquad
W=\gamma y+V,
}
\tag{2.4}
$$

and

$$
\boxed{
\lambda_\gamma
=
1-2\gamma
>
0.
}
\tag{2.5}
$$

---

# 3. Vorticity two-form

Let

$$
\boxed{
d\mathrm{Vol}
=
dy_1\wedge dy_2\wedge dz.
}
\tag{3.1}
$$

Define the vorticity two-form

$$
\boxed{
\varpi
=
\iota_\Omega d\mathrm{Vol}.
}
\tag{3.2}
$$

For

$$
\Omega
=
(q_{x_2},-q_{x_1},0),
$$

one computes

$$
\boxed{
\varpi
=
dq\wedge dz.
}
\tag{3.3}
$$

The anchor subtraction changes

$$
q
$$

by a function of

$$
z,s
$$

only.

Therefore

$$
\boxed{
d_y\widetilde q\wedge dz
=
dq\wedge dz.
}
\tag{3.4}
$$

Since

$$
r=\eta\widetilde q
$$

and

$$
\eta
$$

has no spatial dependence,

$$
\boxed{
\varpi
=
\eta(s)^{-1}
dr\wedge dz.
}
\tag{3.5}
$$

This identity is gauge completed.

---

# 4. Similarity vorticity equation

The DSS Euler vorticity equation is

$$
\boxed{
\partial_s\Omega
+
W\cdot\nabla\Omega
+
\Omega
=
(\Omega\cdot\nabla)V.
}
\tag{4.1}
$$

Since

$$
W=\gamma y+V,
$$

$$
\boxed{
(\Omega\cdot\nabla)W
=
\gamma\Omega
+
(\Omega\cdot\nabla)V.
}
\tag{4.2}
$$

Thus

$$
\boxed{
\partial_s\Omega
+
W\cdot\nabla\Omega
-
(\Omega\cdot\nabla)W
=
-(1+\gamma)\Omega.
}
\tag{4.3}
$$

Also

$$
\boxed{
\nabla\cdot W=3\gamma.
}
\tag{4.4}
$$

---

# 5. NEW THEOREM — Similarity Vorticity Two-Form Equation

## Theorem 5.1

The vorticity two-form obeys

$$
\boxed{
(\partial_s+\mathcal L_W)\varpi
=
-\lambda_\gamma\varpi,
}
\tag{5.1}
$$

where

$$
\lambda_\gamma=1-2\gamma.
$$

### Proof

For a vector field

$$
\Omega
$$

and volume form

$$
d\mathrm{Vol},
$$

the Lie derivative of

$$
\varpi=\iota_\Omega d\mathrm{Vol}
$$

corresponds to the vector expression

$$
W\cdot\nabla\Omega
-
(\Omega\cdot\nabla)W
+
(\nabla\cdot W)\Omega.
$$

Using (4.3) and

$$
\nabla\cdot W=3\gamma,
$$

the coefficient is

$$
-(1+\gamma)+3\gamma
=
2\gamma-1
=
-\lambda_\gamma.
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

This is the differential-form version of the self-similar Cauchy/Kelvin scaling.

---

# 6. Pullback form

Let

$$
Y_s
$$

be the similarity material flow.

Theorem 5.1 is equivalent to

$$
\boxed{
Y_s^\ast\varpi(s)
=
e^{-\lambda_\gamma s}
\varpi(0).
}
\tag{6.1}
$$

For one DSS period:

$$
\boxed{
\Phi^\ast\varpi
=
\mu_r^{-1}\varpi,
}
\tag{6.2}
$$

where

$$
\Phi=Y_{S_0}.
$$

This agrees with the self-similar Kelvin circulation factor.

---

# 7. Scalar pullback

The pure scalar equation

$$
D_sr=\lambda_\gamma r
$$

gives

$$
\boxed{
Y_s^\ast r(s)
=
e^{\lambda_\gamma s}r(0).
}
\tag{7.1}
$$

Differentiating spatially:

$$
\boxed{
Y_s^\ast dr(s)
=
e^{\lambda_\gamma s}dr(0).
}
\tag{7.2}
$$

For one period:

$$
\boxed{
\Phi^\ast dr
=
\mu_r\,dr.
}
\tag{7.3}
$$

---

# 8. NEW THEOREM — Weighted Shear–Vorticity Two-Form Invariance

Define

$$
\boxed{
\mathfrak W
=
r\varpi.
}
\tag{8.1}
$$

## Theorem 8.1

On the pure fixed-plane pancake branch,

$$
\boxed{
(\partial_s+\mathcal L_W)\mathfrak W
=
0.
}
\tag{8.2}
$$

Equivalently,

$$
\boxed{
Y_s^\ast\mathfrak W(s)
=
\mathfrak W(0).
}
\tag{8.3}
$$

In particular,

$$
\boxed{
\Phi^\ast\mathfrak W
=
\mathfrak W.
}
\tag{8.4}
$$

### Proof

Use the product rule:

$$
(\partial_s+\mathcal L_W)
(r\varpi)
=
(D_sr)\varpi
+
r
(\partial_s+\mathcal L_W)\varpi.
$$

The two terms are

$$
\lambda_\gamma r\varpi
$$

and

$$
-\lambda_\gamma r\varpi.
$$

They cancel exactly.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the principal invariant of DCRP-47.

---

# 9. Interpretation

The pure pancake scalar amplifies as

$$
e^{\lambda_\gamma s}.
$$

The vorticity two-form decays as

$$
e^{-\lambda_\gamma s}.
$$

Their product is exactly material.

Thus the strongest Euler equality branch satisfies

$$
\boxed{
\textbf{
shear amplification}
\times
\textbf{
vorticity-flux contraction}
=
\textbf{
constant weighted material flux}.
}
}
\tag{9.1}
$$

This is a critical cancellation.

It is the codimension-one analogue of earlier critical scaling equalities in the DCRP program.

---

# 10. Material-surface flux invariant

Let

$$
S_0
$$

be an oriented smooth material surface contained in the pure patch.

Let

$$
S_s=Y_s(S_0).
$$

Define

$$
\boxed{
\mathcal Q_{\mathfrak W}(S_s)
=
\int_{S_s}
\mathfrak W(s).
}
\tag{10.1}
$$

Then

$$
\boxed{
\mathcal Q_{\mathfrak W}(S_s)
=
\mathcal Q_{\mathfrak W}(S_0)
}
\tag{10.2}
$$

for all times for which the patch remains in the pure branch.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the natural weighted physical carrier sought after DCRP-46.

It is a surface flux, not a volume mass.

---

# 11. Exactness limitation

Using

$$
\varpi
=
\eta^{-1}dr\wedge dz,
$$

$$
\boxed{
\mathfrak W
=
\frac{
r
}{
\eta
}
dr\wedge dz
=
d_y
\left[
\frac{
r^2
}{
2\eta
}
dz
\right].
}
\tag{11.1}
$$

Thus

$$
\mathfrak W
$$

is locally exact on the fixed-plane patch.

Consequently:

$$
\boxed{
\int_S
\mathfrak W
=
0
}
\tag{11.2}
$$

for every closed surface

$$
S
$$

contained in a simply connected pure patch.

Therefore the invariant is naturally a **relative/open-surface carrier**.

Its nonzero value is tied to the boundary shear contrast of a material ribbon or sheet patch.

This limitation is essential.

No global topological invariant is claimed.

---

# 12. One-period normal-cotangent identity

At one DSS period:

$$
\eta(S_0)=\eta(0).
$$

Using

$$
\varpi
=
\eta^{-1}dr\wedge dz,
$$

the two pullback equations give

$$
\eta^{-1}
\mu_r
dr
\wedge
\Phi^\ast dz
=
\mu_r^{-1}
\eta^{-1}
dr\wedge dz.
$$

Therefore

$$
\boxed{
dr
\wedge
\Phi^\ast dz
=
\mu_r^{-2}
dr\wedge dz.
}
\tag{12.1}
$$

---

# 13. NEW THEOREM — Normal Cotangent Contraction

## Theorem 13.1

At every regular point where

$$
dr\neq0,
$$

there exists a scalar

$$
\beta
$$

such that

$$
\boxed{
\Phi^\ast dz
=
\mu_r^{-2}dz
+
\beta\,dr.
}
\tag{13.1}
$$

Equivalently, in the quotient cotangent line

$$
\boxed{
T^\ast/
\operatorname{span}
\{dr\},
}
\tag{13.2}
$$

$$
\boxed{
[dz]
\mapsto
\mu_r^{-2}[dz].
}
\tag{13.3}
$$

### Proof

Equation (12.1) gives

$$
dr
\wedge
\left[
\Phi^\ast dz
-
\mu_r^{-2}dz
\right]
=
0.
$$

For a nonzero one-form

$$
dr,
$$

the bracketed one-form must be pointwise proportional to

$$
dr.
$$

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED LOCALLY ON REGULAR PURE PATCHES}.
}
$$

---

# 14. Equal-shear transverse separation

Let

$$
v
$$

be a tangent vector satisfying

$$
\boxed{
dr(v)=0.
}
\tag{14.1}
$$

Then Theorem 13.1 gives

$$
\boxed{
dz(D\Phi\,v)
=
\mu_r^{-2}
dz(v).
}
\tag{14.2}
$$

Thus the plane-normal component of an equal-shear material separation contracts by the exact factor

$$
\boxed{
\mu_r^{-2}.
}
\tag{14.3}
$$

This is the precise geometric meaning of the normal-cotangent law.

It is not asserted to equal a Euclidean sheet thickness unless the chosen material tube is coherently aligned with the pure chart.

---

# 15. Continuous-time normal law

For intermediate time

$$
s,
$$

the periodic integrating factor

$$
\eta(s)
$$

appears.

The corresponding wedge identity is

$$
\boxed{
dr(0)
\wedge
Y_s^\ast dz
=
e^{-2\lambda_\gamma s}
\frac{
\eta(s)
}{
\eta(0)
}
dr(0)\wedge dz.
}
\tag{15.1}
$$

Thus the exact pure exponential normal factor is recovered at every integer DSS period.

---

# 16. Invariant two-dimensional cotangent subspace

The span

$$
\boxed{
\mathcal E^\ast
=
\operatorname{span}
\{dr,dz\}
}
\tag{16.1}
$$

is invariant under the one-period pullback.

In the basis

$$
(dr,dz),
$$

the pullback is triangular with diagonal entries

$$
\boxed{
\mu_r,
\qquad
\mu_r^{-2}.
}
\tag{16.2}
$$

Therefore:

$$
\boxed{
\det
\left(
\Phi^\ast|_{\mathcal E^\ast}
\right)
=
\mu_r^{-1}.
}
\tag{16.3}
$$

This is exactly the vorticity two-form multiplier.

---

# 17. Quotient vorticity-line multiplier

The full cotangent pullback has determinant

$$
\boxed{
\det
\Phi^\ast
=
J_\Phi
=
e^{3\gamma S_0}.
}
\tag{17.1}
$$

Since

$$
\mathcal E^\ast
$$

is invariant and has determinant

$$
\mu_r^{-1},
$$

the induced one-dimensional map on

$$
\boxed{
T^\ast/\mathcal E^\ast
}
\tag{17.2}
$$

has multiplier

$$
\boxed{
\lambda_{\parallel}^{quot}
=
J_\Phi\mu_r.
}
\tag{17.3}
$$

Using

$$
J_\Phi=e^{3\gamma S_0}
$$

and

$$
\mu_r=e^{(1-2\gamma)S_0},
$$

$$
\boxed{
\lambda_{\parallel}^{quot}
=
e^{(1+\gamma)S_0}.
}
\tag{17.4}
$$

Status:

$$
\boxed{
\textbf{PROVED AS A QUOTIENT-COTANGENT MULTIPLIER}.
}
$$

No claim is made that every Euclidean vorticity-line length stretches by this exact factor.

---

# 18. Match with the Cauchy prefactor

The self-similar Cauchy vector formula has the prefactor

$$
\boxed{
e^{-(1+\gamma)S_0}.
}
\tag{18.1}
$$

The quotient-line multiplier is

$$
\boxed{
e^{(1+\gamma)S_0}.
}
\tag{18.2}
$$

Thus the exponents exactly cancel.

This explains why the pure pancake branch can reproduce a periodic vorticity field without an exponent mismatch.

Again, this is a quotient-coordinate identity, not a pointwise Euclidean-magnitude theorem.

---

# 19. Critical sheet-monodromy identity

The pure sheet branch has four canonical factors.

### shear scalar

$$
\boxed{
\mu_r
=
e^{(1-2\gamma)S_0}.
}
\tag{19.1}
$$

### normal cotangent quotient

$$
\boxed{
\mu_\perp
=
\mu_r^{-2}.
}
\tag{19.2}
$$

### vorticity-line quotient

$$
\boxed{
\mu_\parallel
=
J_\Phi\mu_r
=
e^{(1+\gamma)S_0}.
}
\tag{19.3}
$$

### total similarity volume

$$
\boxed{
J_\Phi
=
e^{3\gamma S_0}.
}
\tag{19.4}
$$

They satisfy

$$
\boxed{
\mu_r
\mu_\perp
\mu_\parallel
=
J_\Phi.
}
\tag{19.5}
$$

Also:

$$
\boxed{
\mu_r
\cdot
\mu_{\varpi}
=
1,
\qquad
\mu_{\varpi}
=
\mu_r^{-1}.
}
\tag{19.6}
$$

This is the **critical sheet monodromy**.

---

# 20. Relation to DCRP-46 intermittency exponent

DCRP-46 found the material-fraction upper bound

$$
\theta_m
\lesssim
(1+m)\mu_r^{-2m}
$$

on the bounded-enstrophy super-DSS exhaust.

DCRP-47 finds the exact canonical normal quotient factor

$$
\mu_r^{-2}
$$

per DSS period.

The equality of exponents is striking.

However:

$$
\boxed{
\textbf{
DCRP-47 does not identify the DCRP-46 material fraction with the sheet-normal cotangent factor.
}
}
\tag{20.1}
$$

Such an identification requires a coherent material-tube/thickness theorem.

The matching exponents should be viewed as evidence of critical compatibility, not as a proved geometric equivalence.

---

# 21. No volume-to-vorticity concentration theorem

Because the natural invariant is the two-form

$$
\mathfrak W=r\varpi,
$$

a codimension-one material sheet can retain a fixed weighted flux while its three-dimensional tubular neighborhood has vanishing volume.

Therefore:

$$
\boxed{
\textbf{
the DCRP-46 vanishing material fraction alone does not force}
\ 
|\Omega|
\textbf{ to diverge}.
}
\tag{21.1}
$$

The missing information is one of:

- sheet area;
- sheet thickness;
- surface multiplicity;
- transverse gradient;
- trace-to-volume conversion.

This is a methodological NO-GO to the naive weighted-volume route.

---

# 22. Surface-flux versus surface-enstrophy inequality

Let

$$
S
$$

be an oriented material surface in a compact pure patch.

Suppose

$$
\boxed{
|\mathcal Q_{\mathfrak W}(S)|
=
Q_0>0.
}
\tag{22.1}
$$

Then

$$
\begin{aligned}
Q_0
&=
\left|
\int_S
r
\varpi
\right|
\\
&\le
\|r\|_{L^\infty(S)}
\int_S
|\Omega\cdot n_S|
dA
\\
&\le
\|r\|_{L^\infty(S)}
|S|^{1/2}
\left(
\int_S
|\Omega|^2dA
\right)^{1/2}.
\end{aligned}
$$

Therefore

$$
\boxed{
|S|
\int_S
|\Omega|^2dA
\ge
\frac{
Q_0^2
}{
\|r\|_{L^\infty(S)}^2
}.
}
\tag{22.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This gives a surface-level alternative:

$$
\boxed{
\text{large sheet area}
\ \vee\
\text{large surface vorticity trace}
\ \vee\
\text{large shear amplitude}.
}
\tag{22.3}
$$

It is not yet a volume enstrophy estimate.

---

# 23. Compact material-surface witness

If along a material-surface sequence:

$$
S_m,
$$

one has:

$$
\boxed{
|S_m|
\le
A_\ast,
\qquad
\|r\|_{L^\infty(S_m)}
\le
M_\ast,
}
\tag{23.1}
$$

then the invariant flux gives

$$
\boxed{
\int_{S_m}
|\Omega|^2dA
\ge
\frac{
Q_0^2
}{
A_\ast M_\ast^2
}.
}
\tag{23.2}
$$

Thus a compact recurrent material surface with bounded shear amplitude carries a fixed surface-vorticity trace gap.

The pure exhaust evades this theorem by leaving the compact/bounded-amplitude regime.

---

# 24. Why surface area may absorb the carrier

A material sheet may increase its area while its tubular volume becomes small.

This is compatible with:

- thinning;
- folding;
- tangential expansion;
- vorticity-flux redistribution.

Therefore surface area growth is a genuine equality branch.

It cannot be declared impossible from incompressibility alone.

---

# 25. External sheet calibration

Recent exact Euler theory constructs smooth vorticities supported in tubular neighborhoods of analytic three-dimensional vortex sheets whose thickness tends to zero while the time of existence stays uniformly positive.

This confirms that:

$$
\boxed{
\textbf{
vanishing volume thickness with nontrivial sheet geometry is compatible with exact Euler dynamics.
}
}
\tag{25.1}
$$

Thus DCRP-47's codimension-one interpretation is consistent with known Euler flexibility.

It does not realize the strict DSS Type-II branch automatically.

---

# 26. What the Euler equality manifold now looks like

After DCRP-47 the pure rank-two branch has:

1. scalar amplification:

   $$
   r\mapsto\mu_r r;
   $$

2. vorticity-flux contraction:

   $$
   \varpi\mapsto\mu_r^{-1}\varpi;
   $$

3. weighted two-form conservation:

   $$
   r\varpi
   \mapsto
   r\varpi;
   $$

4. normal quotient contraction:

   $$
   [dz]\mapsto\mu_r^{-2}[dz];
   $$

5. quotient line multiplier:

   $$
   \lambda_\parallel^{quot}
   =
   e^{(1+\gamma)S_0};
   $$

6. total volume expansion:

   $$
   J_\Phi=e^{3\gamma S_0}.
   $$

All exponents are mutually compatible.

This is a genuine critical Euler sheet equality manifold.

---

# 27. Why the next step must return to viscosity

The Euler-side exponent bookkeeping no longer produces a mismatch.

The pure sheet branch has an exact Lie-advected weighted two-form.

Therefore the next closure must use information not present in the inviscid equality manifold.

The natural missing ingredient is:

$$
\boxed{
\textbf{
Navier--Stokes viscosity.
}
}
\tag{27.1}
$$

At the Type-II prelimit, the effective viscosity is small but nonzero.

It can diffuse:

- sheet-normal gradients;
- vorticity two-forms;
- scalar/vorticity interfaces.

Thus the correct next bridge is a viscous shadowing theorem for

$$
\mathfrak W.
$$

---

# 28. Formal prelimit sheet-form defect

Schematically, let

$$
\varpi_n
$$

be the prelimit normalized vorticity two-form and suppose a compatible prelimit shear scalar

$$
r_n
$$

has been declared on a coherent rank-two sheet chart.

The normalized Navier--Stokes vorticity equation has a viscous contribution of the form

$$
\boxed{
\varepsilon_n
\Delta\varpi_n,
}
\tag{28.1}
$$

where

$$
\varepsilon_n\to0.
$$

If

$$
r_n
$$

approximately obeys the pure scalar equation, then the weighted sheet form has a defect schematically of the form

$$
\boxed{
(\partial_s+\mathcal L_{W_n})
(r_n\varpi_n)
=
\mathcal R_{{\rm sh},n}\varpi_n
+
\varepsilon_n
r_n
\Delta\varpi_n
+
\mathcal R_{{\rm chart},n}.
}
\tag{28.2}
$$

This formula is a **programmatic target**, not a completed theorem in DCRP-47.

A rigorous derivation requires a prelimit rank-two chart and gauge compiler.

---

# 29. Candidate viscous sheet-form residual

The natural next observable is therefore

$$
\boxed{
\mathfrak D_{\rm sheet}^{visc}
=
\left|
\int
\varepsilon_n
r_n
\Delta\varpi_n
\right|
}
\tag{29.1}
$$

over a declared material sheet tube/window, together with:

- scalar residual;
- chart/rank residual;
- boundary transport.

This is higher order and more physical than taxing volume intermittency by itself.

---

# 30. Conditional thickness comparison

There is a suggestive exponent mismatch if the cotangent normal law can be promoted to a genuine geometric sheet thickness.

The Euler pure branch has the one-period normal quotient factor

$$
\boxed{
\mu_r^{-2}.
}
\tag{30.1}
$$

The DCRP Type-II effective viscosity scales between same-parent roots as

$$
\boxed{
\varepsilon_{n+1}
=
\mu_r^{-1}
\varepsilon_n.
}
\tag{30.2}
$$

Hence a diffusive length scale:

$$
\sqrt{\varepsilon_n}
$$

scales as

$$
\boxed{
\mu_r^{-1/2}.
}
\tag{30.3}
$$

If a coherent physical sheet thickness

$$
h_n
$$

satisfies

$$
h_{n+1}/h_n
\approx
\mu_r^{-2},
$$

then

$$
\boxed{
\frac{
h_{n+1}
}{
\sqrt{\varepsilon_{n+1}}
}
\approx
\mu_r^{-3/2}
\frac{
h_n
}{
\sqrt{\varepsilon_n}
}.
}
\tag{30.4}
$$

Thus the sheet would become increasingly subdiffusive.

However:

$$
\boxed{
\textbf{
this comparison is CONDITIONAL.
}
}
\tag{30.5}
$$

The quotient cotangent factor has not yet been proved to equal an actual Euclidean viscous-core thickness under same-parent re-rooting.

No contradiction is claimed.

This is a high-priority next theorem.

---

# 31. Critical equality versus viscous shadowing

The DCRP history repeatedly found that a raw Euler-side scaling mismatch disappears after the correct quotient is used.

DCRP-47 continues that pattern.

The pure Euler pancake sheet is internally scaling-consistent.

The remaining question is not:

> can Euler support the sheet monodromy?

At the level derived here, yes, algebraically.

The question is:

> can a sequence of smooth Navier--Stokes solutions with small but nonzero Type-II effective viscosity shadow this exact codimension-one monodromy without creating a second-order sheet defect?

This is genuinely Navier--Stokes-specific.

---

# 32. Corrected role of material intermittency

DCRP-46's theorem remains valid:

$$
\theta_m
\lesssim
(1+m)\mu_r^{-2m}
$$

for the declared super-DSS exhaust cohort.

DCRP-47 changes its interpretation.

It is not automatically a concentration tax.

Instead it is compatible with a codimension-one sheet carrier whose natural normal exponent is also

$$
\mu_r^{-2}.
$$

Thus material intermittency is best treated as a **sheet-thickness/geometry signal**.

A physical tax arises only after adding:

- a thickness lower bound;
- a surface-area bound;
- a trace-to-volume inequality;
- or viscous diffusion.

---

# 33. New equality normal form

The strongest rank-two survivor is now:

$$
\boxed{
\textbf{
pure anchored pancake scalar cocycle}
}
$$

plus

$$
\boxed{
\textbf{
Lie-advected weighted shear--vorticity two-form}
}
$$

plus

$$
\boxed{
\textbf{
critical normal/tangential sheet monodromy}.
}
$$

It may live on an asymptotically thin, large-area material sheet.

This is the most precise Euler equality state reached in the DCRP chain.

---

# 34. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Viscous Sheet-Form Shadowing /
Subdiffusive Thickness Closure.
}
}
$$

A useful theorem would prove at least one of the following.

### Route A — sheet-form shadowing

If the Navier--Stokes prelimit shadows the Euler weighted-form invariant, then the prelimit material sheet tubes inherit a quantitative normal contraction.

Show that this contraction cannot outrun viscous diffusion indefinitely without activating:

$$
\boxed{
\text{second-order vorticity action}
\ \vee\
\text{viscous sheet flux}
\ \vee\
\text{rank/normal-shear residual}.
}
$$

### Route B — failed sheet-form shadowing

If the weighted form does not shadow, retain a nonzero:

$$
\boxed{
\mathfrak D_{\rm sheet}^{visc}
}
$$

or chart/transition residual.

### Route C — area/thickness escape

If viscosity is avoided by increasing sheet area while shrinking volume thickness, prove that the required surface growth produces:

- PFET;
- strain;
- curvature/folding;
- or scale-transition activity.

This is now the sharpest genuinely viscous frontier.

---

# 35. Source-status audit

The primary self-similar Euler source derives:

$$
\boxed{
\Omega(Y(a,\tau))
=
e^{-(1+\gamma)\tau}
\nabla_aY(a,\tau)
\Omega(a)
}
$$

and

$$
\boxed{
\det\nabla_aY
=
e^{3\gamma\tau}.
}
$$

It also derives the self-similar Kelvin law

$$
\boxed{
e^{(1-2\gamma)\tau}
\Gamma_{\rm ss}(\tau)
=
\Gamma_{\rm ss}(0).
}
$$

These identities calibrate the DCRP-47 vorticity two-form multiplier and quotient-line exponent.

Recent exact Euler vortex-sheet desingularization results show that smooth vorticity can remain concentrated in arbitrarily thin tubular neighborhoods of analytic three-dimensional vortex sheets for a nonvanishing time interval.

This calibrates the NO-GO against excluding the codimension-one equality state by thinness alone.

---

# 36. End state

The pure pancake scalar obeys

$$
\boxed{
D_sr
=
(1-2\gamma)r.
}
$$

The vorticity two-form obeys

$$
\boxed{
(\partial_s+\mathcal L_W)\varpi
=
-(1-2\gamma)\varpi.
}
$$

Therefore

$$
\boxed{
(\partial_s+\mathcal L_W)
(r\varpi)
=
0.
}
$$

The natural weighted physical carrier is a material two-form.

At one DSS period:

$$
\boxed{
\Phi^\ast dr
=
\mu_rdr,
}
$$

$$
\boxed{
\Phi^\ast\varpi
=
\mu_r^{-1}\varpi,
}
$$

and on regular patches:

$$
\boxed{
\Phi^\ast dz
=
\mu_r^{-2}dz
+
\beta dr.
}
$$

The remaining cotangent quotient multiplier is

$$
\boxed{
J_\Phi\mu_r
=
e^{(1+\gamma)S_0},
}
$$

matching the inverse Cauchy prefactor.

Thus the Euler sheet branch has a complete critical monodromy:

$$
\boxed{
\mu_r
\cdot
\mu_r^{-2}
\cdot
(J_\Phi\mu_r)
=
J_\Phi.
}
$$

DCRP-46 volume intermittency is therefore not by itself a physical concentration contradiction.

The strongest survivor is a codimension-one critical sheet carrier.

The next frontier is:

$$
\boxed{
\textbf{
Viscous Sheet-Form Shadowing /
Subdiffusive Thickness Closure.
}
}
$$