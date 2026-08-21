# DCRP105 / X72-R88 — Shear-Polarized TR Geometry, Vanishing-Viscosity Residual Matching, and the No-Forced-Spectral-Migration Audit

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-20  
**Status:** proof-development checkpoint / vanishing-viscosity shear-polarization round  
**Immediate predecessor:** `NS_DCRP104_X72R87_RieszSelfConsistency_ShearPolarization_2026-08-20.md`

## Primary internal dependencies

- DCRP95–96 — sign-coherent Kelvin phase slip / nematic second-moment lock.
- DCRP102 — recurrent fixed-sign transport–Riesz angular pair cell.
- DCRP103 — local adjoint five-ray classification.
- DCRP104 — frozen Riesz self-consistency:
  - coaxial \(L^2\) NO-GO;
  - simple-shear off-resonance \(L^2\) survivors;
  - axisymmetric polarization kernels;
  - exact positive-viscosity frozen \(L^2\) eigen-lock NO-GO.

## Fresh primary-source calibration

- G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468 (2026).
  Current Type-II analysis continues to use Euler-scaled limits and Liouville-type exclusions.
- R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier-Stokes Equations*, arXiv:2606.27560 (2026).
  The differentiated filtered stress is controlled by scale-invariant velocity-increment defects; at criticality bounded defects produce cylindrical generalized Young profiles.
- E. Hess-Childs, M. Rosenzweig, S. Serfaty, *Another look at regularity in transport-commutator estimates*, arXiv:2601.02326 (2026).
  Generic Riesz transport commutator control retains a sharp regularity burden; soft BMO replacement of Lipschitz control fails in general.
- B. Álvarez-Samaniego, W. Álvarez-Samaniego, P. Fernández-Dalgo, *On the use of the Riesz transforms to determine the pressure term in the incompressible Navier-Stokes equations on the whole space*, arXiv:2004.02588.

No full Navier–Stokes regularity theorem is claimed.

---

# 0. Executive result

D104 left three frozen inviscid nonlocal mechanisms:

\[
\boxed{
\mathsf K_{\rm sh}^{\rm off-res}
\vee
\mathsf K_{\rm sh}^{\rm near-res}
\vee
\mathsf K_{\rm axi-pol}.
}
\]

It also proved that for every fixed:

\[
\varepsilon>0,
\]

the exact globally frozen whole-space \(L^2\) viscous eigen-lock is zero.

D105 audits whether this positive-viscosity NO-GO becomes a useful **uniform** obstruction as:

\[
\varepsilon\to0.
\]

It does not.

Let:

\[
\mathscr M_0(n)
\]

be the frozen inviscid adjoint symbol on one D104 shear/polarization kernel and let:

\[
\widehat\Phi_0(\xi)
\]

satisfy:

\[
\boxed{
\mathscr M_0(\widehat\xi)\widehat\Phi_0(\xi)=0.
}
\tag{0.1}
\]

The viscous symbol is:

\[
\boxed{
\mathscr M_\varepsilon(\xi)
=
\mathscr M_0(\widehat\xi)
+
\varepsilon|\xi|^2I.
}
\tag{0.2}
\]

Therefore the **same inviscid normalized profile** has residual:

\[
\boxed{
\widehat R_\varepsilon
=
\mathscr M_\varepsilon\widehat\Phi_0
=
\varepsilon|\xi|^2\widehat\Phi_0.
}
\tag{0.3}
\]

Hence, for every:

\[
\Phi_0\in H^2,
\]

\[
\boxed{
\|R_\varepsilon\|_2
=
\varepsilon
\|\Delta\Phi_0\|_2.
}
\tag{0.4}
\]

Thus a fixed normalized frequency profile survives as an \(O(\varepsilon)\) approximate eigen-lock.

There is **no forced frequency migration** at the natural \(O(\varepsilon)\) residual scale.

The true critical quantity is:

\[
\boxed{
\Theta_{\rm vis}
:=
\frac{
\eta_\varepsilon
}{
\varepsilon
},
}
\tag{0.5}
\]

where:

\[
\eta_\varepsilon
=
\|\mathscr M_\varepsilon\Phi_\varepsilon\|_2
\]

is the adjoint eigen-lock residual.

If a nontrivial kernel component remains in a fixed normalized radial band:

\[
\rho_-
\le
|\xi|
\le
\rho_+,
\qquad
\rho_->0,
\]

then:

\[
\boxed{
\eta_\varepsilon
\ge
\varepsilon
\rho_-^2
\|\Phi_\varepsilon\|_2.
}
\tag{0.6}
\]

Hence order-one fixed-band mass requires:

\[
\boxed{
\eta_\varepsilon
\gtrsim
\varepsilon.
}
\tag{0.7}
\]

Conversely, if:

\[
\boxed{
\eta_\varepsilon=o(\varepsilon),
}
\tag{0.8}
\]

then every normalized kernel component is forced toward:

\[
\boxed{
|\xi|\to0.
}
\]

More precisely, if:

\[
\|\Phi_\varepsilon\|_2=1,
\]

and the state lies exactly in the inviscid kernel bundle, then for every fixed:

\[
\rho>0,
\]

\[
\boxed{
\int_{|\xi|\ge\rho}
|\widehat\Phi_\varepsilon|^2d\xi
\le
\frac1{\rho^4}
\left(
\frac{\eta_\varepsilon}{\varepsilon}
\right)^2.
}
\tag{0.9}
\]

So:

\[
\eta_\varepsilon/\varepsilon\to0
\]

forces low-normalized-frequency migration.

In the same-parent compact compiler this is a large-spatial-scale / scale-state escape unless the profile vanishes.

Therefore:

# Main viscosity-rate trichotomy

\[
\boxed{
\begin{array}{rcl}
\eta_\varepsilon=o(\varepsilon)
&\Longrightarrow&
\text{low-frequency / large-scale escape or vanishing},
\\[1mm]
\eta_\varepsilon\asymp\varepsilon
&\Longrightarrow&
\text{fixed-scale inviscid shear/polarization may survive},
\\[1mm]
\eta_\varepsilon\gg\varepsilon
&\Longrightarrow&
\text{eigen-lock residual itself is active}.
\end{array}
}
\tag{0.10}
\]

This is the main D105 result.

The positive-viscosity exact NO-GO is a **singular perturbation**:

\[
\boxed{
\ker\mathscr M_\varepsilon=\{0\}
\quad(\varepsilon>0),
\qquad
\ker\mathscr M_0\neq\{0\}.
}
\tag{0.11}
\]

The smallest singular value on a fixed inviscid-kernel frequency band collapses linearly like:

\[
\boxed{
\sigma_{\min}
\sim
\varepsilon|\xi|^2.
}
\tag{0.12}
\]

D105 also checks the D102 TR angular cone and the D95 Kelvin nematic lock.

They do **not** eliminate the simple-shear survivor locally.

For the trace-free Riesz kernel:

\[
K_0(z)
=
c|z|^{-3}
(I-3n\otimes n),
\qquad
n=z/|z|,
\]

and shear tensor:

\[
H_{ij}
=
e_i\otimes e_j+e_j\otimes e_i,
\]

the exact pair projection is:

\[
\boxed{
\begin{aligned}
&
[(v\cdot\nabla)K_0(rn)]
:
H_{ij}
\\
&\qquad=
-6c\,r^{-4}
\left[
v_i n_j
+
v_j n_i
-
5(v\cdot n)n_in_j
\right].
\end{aligned}
}
\tag{0.13}
\]

For:

\[
H_{13},
\qquad
n=e_3,
\qquad
v=e_1,
\]

this equals:

\[
\boxed{
-6c\,r^{-4}\neq0.
}
\tag{0.14}
\]

At the same time choose Kelvin detector:

\[
A_\Gamma
=
\operatorname{diag}(1,-1,0)
\]

and increment covariance:

\[
Q=e_1\otimes e_1.
\]

Then:

\[
\boxed{
A_\Gamma:Q=1>0.
}
\tag{0.15}
\]

Choosing the sign of:

\[
\delta q
\]

appropriately gives a positive TR factor simultaneously.

Thus:

\[
\boxed{
\text{Kelvin nematic lock}
+
\text{simple-shear TR angular lock}
}
\]

is locally algebraically compatible.

The late compact survivor therefore becomes:

\[
\boxed{
\mathsf C_{\rm vm\mbox{-}shear/pol}
}
\]

= a **viscosity-matched shear/polarization conveyor** carrying:

- \(O(\varepsilon)\) adjoint eigen-lock residual;
- fixed normalized spectral support or axisymmetric polarization;
- fixed-sign TR angular pair cell;
- Kelvin nematic second-moment lock.

---

# 1. Exact shear projection of the Riesz derivative

Use:

\[
K_{ab}(z)
=
c
\left[
r^{-3}\delta_{ab}
-
3r^{-5}z_az_b
\right],
\qquad
r=|z|.
\]

Let:

\[
z=rn.
\]

Differentiate in the direction:

\[
v.
\]

A direct calculation gives:

\[
\boxed{
(v\cdot\nabla)K_0(rn)
=
-3cr^{-4}
\left[
(v\cdot n)I
+
v\otimes n
+
n\otimes v
-
5(v\cdot n)n\otimes n
\right].
}
\tag{1.1}
\]

For:

\[
H_{ij}
=
e_i\otimes e_j+e_j\otimes e_i,
\]

one has:

\[
I:H_{ij}=0,
\]

\[
(v\otimes n+n\otimes v):H_{ij}
=
2(v_in_j+v_jn_i),
\]

\[
(n\otimes n):H_{ij}
=
2n_in_j.
\]

Hence:

## Theorem D105.1 — Simple-shear TR angular scalar

\[
\boxed{
[(v\cdot\nabla)K_0(rn)]
:
H_{ij}
=
-6cr^{-4}
[
v_in_j+v_jn_i-5(v\cdot n)n_in_j
].
}
\tag{1.2}
\]

This scalar is generically sign-indefinite.

So the recurrent D102 TR angular cell is a real orientation/correlation constraint, not a pointwise positivity identity.

---

# 2. Local Kelvin/TR compatibility

Take:

\[
i=1,
\qquad
j=3,
\]

\[
n=e_3,
\qquad
v=e_1.
\]

Then:

\[
v\cdot n=0,
\]

and D105.1 gives:

\[
\boxed{
[(e_1\cdot\nabla)K_0(re_3)]
:
H_{13}
=
-6cr^{-4}.
}
\tag{2.1}
\]

Now let the Kelvin covariance be:

\[
Q=e_1\otimes e_1.
\]

Take:

\[
A_\Gamma
=
\operatorname{diag}(1,-1,0).
\]

Then:

\[
\boxed{
A_\Gamma:Q=1.
}
\tag{2.2}
\]

If:

\[
c>0,
\]

choose:

\[
\delta q<0.
\]

Then:

\[
\boxed{
[(e_1\cdot\nabla)K_0(re_3)]
:
H_{13}
\,
\delta q
>
0.
}
\tag{2.3}
\]

Thus:

## Theorem D105.2 — Local Kelvin/TR compatibility witness

The same velocity-increment direction can satisfy:

- positive Kelvin nematic covariance projection;
- positive simple-shear TR angular projection.

So no generic local second-moment/angular-sign contradiction exists.

### Scope

The Fourier direction controlling D104 Riesz self-consistency and the pair-separation direction \(n=z/|z|\) in D105.1 are different variables.

D105 does not identify them.

---

# 3. Viscous residual on an inviscid kernel

Let:

\[
P(n)
\]

be a smooth inviscid shear/polarization kernel bundle on one compact angular patch away from D104 spectral degeneracies.

Let:

\[
\widehat\Phi
=
P(n)\widehat\Phi.
\]

Then:

\[
\mathscr M_0(n)\widehat\Phi=0.
\]

The prelimit frozen operator is:

\[
\mathscr M_\varepsilon(\xi)
=
\mathscr M_0(n)
+
\varepsilon|\xi|^2I.
\]

Therefore:

## Theorem D105.3 — Exact viscosity residual on the inviscid kernel

\[
\boxed{
\mathscr M_\varepsilon(\xi)\widehat\Phi
=
\varepsilon|\xi|^2\widehat\Phi.
}
\tag{3.1}
\]

Consequently:

\[
\boxed{
\|\mathscr M_\varepsilon\Phi\|_2
=
\varepsilon
\||\xi|^2\widehat\Phi\|_2
=
\varepsilon
\|\Delta\Phi\|_2.
}
\tag{3.2}
\]

This equality is exact for a fixed frozen inviscid-kernel field.

---

# 4. Fixed radial band lower bound

Suppose:

\[
\operatorname{supp}\widehat\Phi
\subset
\{
\rho_-\le|\xi|\le\rho_+
\},
\]

where:

\[
0<\rho_-\le\rho_+<\infty.
\]

Then:

\[
\rho_-^2
\|\Phi\|_2
\le
\||\xi|^2\widehat\Phi\|_2
\le
\rho_+^2
\|\Phi\|_2.
\]

Therefore:

## Theorem D105.4 — Fixed-band viscosity matching

\[
\boxed{
\varepsilon\rho_-^2\|\Phi\|_2
\le
\|\mathscr M_\varepsilon\Phi\|_2
\le
\varepsilon\rho_+^2\|\Phi\|_2.
}
\tag{4.1}
\]

For normalized nontrivial mass:

\[
\|\Phi\|_2\ge m_0>0,
\]

one necessarily has:

\[
\boxed{
\eta_\varepsilon
\ge
m_0\rho_-^2\varepsilon.
}
\tag{4.2}
\]

Thus fixed normalized scale requires an \(O(\varepsilon)\) residual.

---

# 5. Subviscous residual forces low-frequency migration

Assume:

\[
\|\Phi_\varepsilon\|_2=1,
\]

and:

\[
\mathscr M_0(\widehat\xi)\widehat\Phi_\varepsilon=0.
\]

Set:

\[
\eta_\varepsilon
=
\|\mathscr M_\varepsilon\Phi_\varepsilon\|_2.
\]

Then:

\[
\frac{\eta_\varepsilon^2}{\varepsilon^2}
=
\int
|\xi|^4
|\widehat\Phi_\varepsilon|^2d\xi.
\]

For every:

\[
\rho>0,
\]

\[
\begin{aligned}
\int_{|\xi|\ge\rho}
|\widehat\Phi_\varepsilon|^2d\xi
&\le
\rho^{-4}
\int
|\xi|^4
|\widehat\Phi_\varepsilon|^2d\xi
\\
&=
\rho^{-4}
\left(
\frac{\eta_\varepsilon}{\varepsilon}
\right)^2.
\end{aligned}
\]

Thus:

## Theorem D105.5 — Subviscous residual migration

If:

\[
\boxed{
\eta_\varepsilon/\varepsilon\to0,
}
\]

then:

\[
\boxed{
\forall\rho>0:
\quad
\int_{|\xi|\ge\rho}
|\widehat\Phi_\varepsilon|^2
\to0.
}
\tag{5.1}
\]

The normalized Fourier mass collapses toward zero frequency.

For a same-parent compact spatial package, persistent order-one low-frequency concentration is a large-normalized-scale / tail/state issue, not a fixed-core recurrent mode.

---

# 6. The \(O(\varepsilon)\) rate is achievable

Let:

\[
\Phi_0
\]

be any nonzero smooth frozen inviscid shear/polarization survivor from D104 with:

\[
\Phi_0\in H^2.
\]

Use the same normalized profile for every \(\varepsilon\):

\[
\Phi_\varepsilon:=\Phi_0.
\]

Then:

\[
\boxed{
R_\varepsilon
=
\mathscr M_\varepsilon\Phi_0
=
-\varepsilon\Delta\Phi_0
}
\]

up to Fourier sign convention, and therefore:

\[
\boxed{
\|R_\varepsilon\|_2
=
\varepsilon
\|\Delta\Phi_0\|_2.
}
\tag{6.1}
\]

So:

## Theorem D105.6 — No forced spectral migration at natural viscosity order

A fixed normalized shear/polarization spectrum can approach the inviscid eigen-lock with residual exactly \(O(\varepsilon)\).

Therefore:

\[
\boxed{
\varepsilon\to0
\not\Rightarrow
\text{frequency migration}.
}
\tag{6.2}
\]

The frozen positive-viscosity exact NO-GO is nonuniform in the inviscid limit.

---

# 7. Singular-value interpretation

On a fixed radial band and a smooth inviscid-kernel angular patch, the viscous symbol restricted to the inviscid kernel is simply:

\[
\varepsilon|\xi|^2I.
\]

Thus:

\[
\boxed{
\sigma_{\min}^{\rm ker}
(
\mathscr M_\varepsilon
)
=
\varepsilon|\xi|^2.
}
\tag{7.1}
\]

On:

\[
\rho_-\le|\xi|\le\rho_+,
\]

\[
\boxed{
\varepsilon\rho_-^2
\le
\sigma_{\min}^{\rm ker}
\le
\varepsilon\rho_+^2.
}
\tag{7.2}
\]

The inverse condition number therefore diverges like:

\[
\boxed{
\varepsilon^{-1}.
}
\tag{7.3}
\]

This is the exact singular-perturbation mechanism behind:

\[
\ker\mathscr M_\varepsilon=\{0\}
\quad
(\varepsilon>0),
\]

but:

\[
\ker\mathscr M_0\neq\{0\}.
\]

---

# 8. Near-resonance simple-shear debt

D104 simple shear has:

\[
\widehat r
=
\frac{
h(n)
}{
d(n)
}
\widehat q,
\]

where:

\[
h(n)=-2n_in_j,
\]

and:

\[
d(n)=1-a(n).
\]

Let:

\[
E_\delta
=
\{
|d(n)|\le\delta,
\quad
|h(n)|\ge h_0
\}.
\]

Then:

\[
|\widehat r|
\ge
\frac{h_0}{\delta}
|\widehat q|
\]

on \(E_\delta\).

Therefore:

## Theorem D105.7 — Near-resonance compactness debt

\[
\boxed{
\|\widehat q\|_{L^2(E_\delta)}
\le
\frac{\delta}{h_0}
\|\widehat r\|_{L^2(E_\delta)}.
}
\tag{8.1}
\]

If:

\[
\|r\|_2\le R_*,
\]

then:

\[
\boxed{
\|\widehat q\|_{L^2(E_\delta)}
\le
\frac{\delta R_*}{h_0}.
}
\tag{8.2}
\]

So bounded \(r\) forbids order-one source mass from accumulating on a nondegenerate part of the resonance cone.

Near resonance, one must have at least one of:

\[
\boxed{
\text{source suppression}
\vee
\text{numerator/angular degeneration}
\vee
\text{Riesz amplitude blow-up}.
}
\tag{8.3}
\]

The last is:

\[
R_{\rm crit}
\vee
R_{\rm state}.
\]

---

# 9. Concrete \(S=\operatorname{diag}(1,0,-1)\), \(H_{13}\) near-resonance geometry

D104 gives:

\[
d(n)=3n_2^2,
\]

\[
h(n)=-2n_1n_3.
\]

The resonance set is:

\[
\boxed{
n_2=0.
}
\tag{9.1}
\]

The numerator vanishes when:

\[
\boxed{
n_1n_3=0.
}
\tag{9.2}
\]

On the resonance great circle, simultaneous numerator degeneration occurs only at:

\[
\boxed{
n=\pm e_1,
\qquad
n=\pm e_3.
}
\tag{9.3}
\]

Therefore a bounded-\(r\) near-resonance sequence with nonvanishing \(q\)-mass can avoid blow-up only by angular concentration toward those isolated endpoint directions or by suppressing \(q\).

This compresses the canonical near-resonance branch to a finite angular endpoint set.

### Scope

This \(n\) is the Fourier direction.

It is not the D102 physical pair-separation direction.

---

# 10. Axisymmetric polarization has the same viscosity rate threshold

D104 axisymmetric polarization has:

\[
r=0,
\]

and:

\[
\mathscr M_0(n)\widehat\Phi=0
\]

on an open set of Fourier directions.

Therefore D105.3 applies unchanged:

\[
\boxed{
\mathscr M_\varepsilon\widehat\Phi
=
\varepsilon|\xi|^2\widehat\Phi.
}
\tag{10.1}
\]

Thus:

- exact positive-viscosity \(L^2\) eigen-lock is zero;
- \(O(\varepsilon)\) approximate fixed-band polarization survives;
- \(o(\varepsilon)\) residual forces low-frequency migration.

So the critical residual rate is not special to simple shear.

It is common to every open-set inviscid polarization kernel.

---

# 11. Why strict DSS recurrence does not by itself kill the \(O(\varepsilon)\) conveyor

In the normalized Euler-limit architecture:

\[
\varepsilon_n\to0.
\]

If the same normalized inviscid shear/polarization profile recurs at each generation, then:

\[
\eta_n
=
O(\varepsilon_n).
\]

Therefore the normalized residual itself becomes smaller with generation.

There is no contradiction from this fact alone.

In particular, D105 does not infer:

\[
\sum_n\eta_n=\infty.
\]

Depending on the same-parent scaling, \(\varepsilon_n\) may itself be summable.

Thus the correct obstruction is not raw residual summation.

It is the **rate-matching and first-order solvability** of the recurrent state.

---

# 12. Vanishing-viscosity rate compiler

Define:

\[
\boxed{
\Theta_n
=
\frac{
\eta_n
}{
\varepsilon_n
}.
}
\tag{12.1}
\]

On a normalized nontrivial shear/polarization kernel sequence:

## Regime I — subviscous

\[
\boxed{
\Theta_n\to0.
}
\]

Then:

\[
\boxed{
\text{low-frequency migration}
\vee
R_{\rm scale}
\vee
R_{\rm tail}
\vee
R_{\rm state}.
}
\tag{12.2}
\]

## Regime II — viscosity matched

\[
\boxed{
0<c_-\le\Theta_n\le c_+<\infty.
}
\]

Then fixed normalized spectral support may persist.

This is the genuine survivor:

\[
\boxed{
\mathsf C_{\rm vm}.
}
\]

## Regime III — superviscous residual

\[
\boxed{
\Theta_n\to\infty.
}
\]

Then the eigen-lock residual is not asymptotically negligible relative to viscosity and must be retained as an active state/critical defect.

Thus:

## Theorem D105.8 — Residual/viscosity trichotomy

\[
\boxed{
\mathsf K_{\rm sh/axi}^{\rm prelimit}
\Longrightarrow
R_{\rm lowfreq}
\vee
\mathsf C_{\rm vm}
\vee
R_{\rm adj-res}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\tag{12.3}
\]

---

# 13. Final viscosity-matched shear/polarization normal form

Define:

\[
\boxed{
\mathsf C_{\rm vm\mbox{-}shear/pol}
}
\]

by:

1. \(\varepsilon_n\to0\);
2. normalized adjoint state remains nontrivial;
3. state remains close to a D104 shear or axisymmetric inviscid kernel;
4. one fixed normalized spectral cell remains active;
5. adjoint eigen-lock residual satisfies:
   \[
   c_-\varepsilon_n
   \le
   \eta_n
   \le
   c_+\varepsilon_n;
   \]
6. D102 fixed-sign TR angular pair cell persists;
7. D95 Kelvin nematic second-moment lock persists;
8. no tail/scale/state/critical escape occurs.

This is now the sharp vanishing-viscosity compact survivor.

---

# 14. What has actually been eliminated

D105 eliminates the following overstrong routes.

## False route A

> Exact frozen positive-viscosity \(L^2\) kernel is zero, therefore the inviscid ray cannot arise as a vanishing-viscosity limit.

False.

The kernel is singular in \(\varepsilon\), and \(O(\varepsilon)\) residuals approximate inviscid kernel states at fixed normalized frequency.

## False route B

> Vanishing viscosity forces high-frequency or low-frequency migration.

False at the natural \(O(\varepsilon)\) residual scale.

A fixed normalized spectral patch survives.

## True route

If the eigen-lock residual is **smaller than viscosity**:

\[
o(\varepsilon),
\]

then normalized Fourier mass must migrate to zero frequency or vanish.

## True near-resonance route

Bounded Riesz scalar forbids order-one source mass on nondegenerate resonance sectors.

---

# 15. Status ledger

## PROVED this round

### D105-P1 — exact simple-shear directional Riesz projection formula.

### D105-P2 — local Kelvin nematic / simple-shear TR angular compatibility witness.

### D105-P3 — exact viscous residual on an inviscid kernel:
\[
R_\varepsilon=\varepsilon|\xi|^2\Phi.
\]

### D105-P4 — fixed normalized radial band requires residual \(\gtrsim\varepsilon\).

### D105-P5 — \(o(\varepsilon)\) residual forces low-frequency Fourier migration.

### D105-P6 — \(O(\varepsilon)\) residual is explicitly achievable with a fixed normalized inviscid profile.

### D105-P7 — inviscid kernel is a singular perturbation of the positive-viscosity operator with singular value \(\sim\varepsilon|\xi|^2\).

### D105-P8 — near-resonance source/Riesz amplitude inequality.

### D105-P9 — canonical shear near-resonance set reduces to a great circle with only four numerator-degenerate endpoints.

### D105-P10 — axisymmetric polarization has the same \(O(\varepsilon)\) critical residual rate.

### D105-P11 — strict DSS recurrence plus \(\varepsilon_n\to0\) does not itself contradict viscosity-matched recurrence.

### D105-P12 — the remaining prelimit ray branch is compressed to the viscosity-matched shear/polarization conveyor.

---

# 16. What is NOT proved

D105 does not prove:

- \(\mathsf C_{\rm vm\mbox{-}shear/pol}\) is impossible;
- the actual adjoint residual of a Navier–Stokes prelimit must be \(o(\varepsilon)\);
- \(\varepsilon_n\) is nonsummable across generations;
- low normalized frequency always implies literal spatial-tail escape without an additional localization/Poincaré hypothesis;
- the Fourier angle in Riesz self-consistency equals the physical pair angle in the TR detector;
- Kelvin nematic lock determines the shear spectral polarization;
- near-resonance endpoint concentration is impossible;
- global Navier–Stokes regularity.

The remaining problem is now a **first-order vanishing-viscosity solvability / spectral-drift problem**.

---

# 17. STOP-D105

\[
\boxed{
\begin{minipage}{0.94\linewidth}
The exact positive-viscosity frozen \(L^2\) eigen-lock NO-GO from D104 is not uniform as viscosity vanishes. On any D104 inviscid shear or axisymmetric polarization kernel, the viscous symbol is simply \(\varepsilon|\xi|^2\) on the kernel, so the same fixed normalized profile has residual \(R_\varepsilon=\varepsilon|\xi|^2\Phi\) and \(\|R_\varepsilon\|_2=\varepsilon\|\Delta\Phi\|_2\). Hence no spectral migration is required at the natural \(O(\varepsilon)\) residual rate. The critical quantity is \(\Theta_\varepsilon=\eta_\varepsilon/\varepsilon\): fixed normalized-band mass forces \(\eta_\varepsilon\gtrsim\varepsilon\), while \(\eta_\varepsilon=o(\varepsilon)\) quantitatively forces all Fourier mass toward \(|\xi|=0\), which becomes a large-scale/state escape in the compact same-parent compiler. Near a simple-shear Riesz resonance, bounded \(r\) forces source suppression or numerator/angular degeneration; for the canonical \(S=\operatorname{diag}(1,0,-1)\), \(H_{13}\) branch, the resonance circle \(n_2=0\) has numerator degeneration only at \(\pm e_1,\pm e_3\). The D102 TR cone and D95 Kelvin nematic lock do not kill the off-resonance shear locally: the same increment direction \(e_1\) gives a positive Kelvin covariance projection and a nonzero \(H_{13}\) Riesz-derivative pairing at pair direction \(e_3\). Thus the sharp remaining prelimit state is a viscosity-matched shear/polarization conveyor with eigen-lock residual of order exactly \(\varepsilon\), fixed-sign TR angular occupancy, and Kelvin second-moment lock. The next question is not whether viscosity kills the inviscid kernel, but whether a recurrent strict-DSS state can satisfy the first-order solvability conditions needed to absorb that \(O(\varepsilon)\) perturbation without radial spectral narrowing or coefficient/eigenframe drift.
\end{minipage}
}
\]

---

# 18. Next autonomous step

## DCRP106 / X72-R89 — First-Order Fredholm / Radial Spectral Narrowing

**Working title**

> **Can the Viscosity-Matched Shear/Polarization Conveyor Absorb the \(O(\varepsilon|\xi|^2)\) Perturbation by a Single Recurring Eigenvalue/State Correction, or Must Its Spectrum Narrow onto a Radial Shell?**

Primary tasks:

1. linearize:
   \[
   \beta_\varepsilon
   =
   \beta_0
   +
   \varepsilon\beta_1
   +o(\varepsilon);
   \]
2. allow:
   \[
   S_\varepsilon
   =
   S_0+\varepsilon S_1+o(\varepsilon);
   \]
3. project the \(O(\varepsilon)\) equation onto the inviscid kernel/cokernel;
4. derive the Fredholm solvability condition;
5. on a fixed shear polarization, compare:
   \[
   \beta_1
   \quad\text{with}\quad
   |\xi|^2;
   \]
6. test whether a single \(\beta_1\) can cancel viscosity on a broadband radial spectrum;
7. seek:
   \[
   \text{broadband survivor}
   \Longrightarrow
   \text{radial spectral narrowing}
   \vee
   \text{coefficient/eigenframe drift}
   \vee
   R_{\rm state};
   \]
8. audit whether shell narrowing is compatible with spatial localization / strict DSS recurrence.

Desired endpoint:

\[
\boxed{
\mathsf C_{\rm vm}
\Longrightarrow
\text{one radial-shell / coefficient-drift normal form}
\vee
R_{\rm scale}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

**End checkpoint:** DCRP105 / X72-R88.
