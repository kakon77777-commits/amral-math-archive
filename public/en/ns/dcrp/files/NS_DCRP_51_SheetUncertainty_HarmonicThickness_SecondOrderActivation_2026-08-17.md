# NS-DCRP-51 — Curved-Sheet Uncertainty, Harmonic-Mean Thickness, and Fragmentation-Proof Second-Order Diffusive Activation

- date: 2026-08-17
- status: research proof checkpoint / sheet-gradient-to-absolute-action round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. close the DCRP-50 loophole that the sheet-scale relative gradient rate may be large while the sheet enstrophy carrier mass vanishes;
  2. derive a curved-sheet uncertainty inequality directly from the signed-distance geometry;
  3. combine the gentle-sheet uncertainty branch with the DCRP-50 strong-folding compiler;
  4. obtain a universal coherent-sheet gradient lower bound unless rank/multiplicity/localization residuals occur;
  5. sum the bound over arbitrarily many coherent sheet pieces using an enstrophy-weighted harmonic-mean thickness;
  6. prove that sheet fragmentation cannot reduce the reciprocal-thickness diffusion bill;
  7. compile the multi-sheet filtered gradient sum back into actual unfiltered Navier--Stokes second-order diffusion under bounded atlas overlap;
  8. derive positive or divergent second-order viscous action when the effective sheet thickness is diffusive or subdiffusive;
  9. classify all escapes as superdiffusive thickening, unbounded sheet overlap/multiplicity, derivative compactness failure, rank transition, carrier leakage, or source/localization residual;
  10. identify the next frontier as recurrence/depletion of the now-positive second-order diffusive action.
- no full Navier--Stokes regularity claim is made.
- principal external primary calibration:
  - R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- internal dependencies:
  - DCRP-35 periodic core enstrophy demand;
  - DCRP-38 rank-two covariance nondegeneracy;
  - DCRP-49 material-sheet viscous thickness floor;
  - DCRP-50 curvature-to-filtered-vorticity-gradient compiler.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-50 obtained, on a coherent nondegenerate rank-two folded sheet,

$$
\boxed{
\ell^2
\frac{
\eta_\ell*
|\nabla\Omega_\ell|^2
}{
\eta_\ell*
|\Omega_\ell|^2
}
\ge
c_{\rm grad}>0
}
\tag{1.1}
$$

whenever the sheet enters the thickness-scale curvature regime

$$
\boxed{
\ell|\mathrm{II}|
\gtrsim1,
}
\tag{1.2}
$$

unless one already has:

- rank-one collapse;
- filtered rank lifting;
- tube multiplicity;
- covariance-weight rearrangement;
- curvature-gradient concentration.

The remaining concern was:

> could the sheet enstrophy mass itself tend to zero fast enough that the absolute second-order diffusion:
>
> $$
> \varepsilon
> \int
> |\nabla\Omega|^2
> $$
>
> remains negligible?

DCRP-51 proves that this loophole cannot be hidden merely by fragmenting the core into many thin sheets.

The first main theorem is a curved-sheet uncertainty principle.

Let

$$
\Sigma
$$

be a smooth oriented sheet with signed distance

$$
d.
$$

Let

$$
G
$$

be a smooth vector field localized in an injective tube around

$$
\Sigma.
$$

Define

$$
\boxed{
M_G
=
\int
|G|^2dy
}
\tag{1.3}
$$

and

$$
\boxed{
H_G
=
\int
d^2|G|^2dy.
}
\tag{1.4}
$$

When

$$
M_G>0,
$$

define the RMS normal thickness

$$
\boxed{
h_G^2
=
H_G/M_G.
}
\tag{1.5}
$$

Assume on the support of

$$
G
$$

$$
\boxed{
|d\Delta d|
\le
\alpha
<
1.
}
\tag{1.6}
$$

Then

$$
\boxed{
\int
|\nabla G|^2dy
\ge
\frac{
(1-\alpha)^2
}{
4h_G^2
}
M_G.
}
\tag{1.7}
$$

Thus a gently curved coherent sheet cannot be simultaneously:

- thin;
- nontrivial in enstrophy;
- low-gradient.

The proof is an uncertainty-principle integration by parts based on

$$
\boxed{
\nabla\cdot
(d\nabla d)
=
1+d\Delta d.
}
\tag{1.8}
$$

The second central result combines this with DCRP-50.

For every coherent rank-two sheet piece one has the alternative:

### gentle-sheet branch

The signed-distance geometry satisfies

$$
|d\Delta d|\le\alpha<1,
$$

and (1.7) gives

$$
\boxed{
\int
|\nabla\Omega_\ell|^2
\gtrsim
\frac{
\mathcal O_{\ell}
}{
h^2
}.
}
\tag{1.9}
$$

### strong-folding branch

The curvature reaches the thickness scale.

If the tube remains injective and the filtered rank-two covariance stays nondegenerate, DCRP-50 gives the same schematic lower bound at the sheet scale:

$$
\boxed{
\int
|\nabla\Omega_\ell|^2
\gtrsim
\frac{
\mathcal O_{\ell}
}{
h^2
}
}
\tag{1.10}
$$

provided the retained hard tube width and RMS carrier thickness are uniformly comparable.

If that comparability fails, record a normal-profile/thickness-tail intermittency residual.

If rank/tube coherence fails, record the corresponding DCRP-50 residual.

Thus on the **fully coherent carrier branch**, every thin sheet piece pays a reciprocal-thickness gradient bill.

The third central result is fragmentation-proof.

Suppose a fixed recurrent core is decomposed into coherent sheet pieces

$$
U_j
$$

with sheet-scale filtered enstrophy masses

$$
\boxed{
\mathcal O_j
=
\int_{U_j}
m_{\ell_j}
}
\tag{1.11}
$$

and effective RMS thicknesses

$$
h_j.
$$

Define

$$
\boxed{
\mathcal O_{\rm sh}
=
\sum_j
\mathcal O_j.
}
\tag{1.12}
$$

Define the enstrophy-weighted harmonic-mean squared thickness

$$
\boxed{
h_{\rm harm}^2
=
\frac{
\sum_j\mathcal O_j
}{
\sum_j
\mathcal O_j/h_j^2
}.
}
\tag{1.13}
$$

Then the sheetwise uncertainty/folding inequalities give

$$
\boxed{
\sum_j
\int_{U_j}
|\nabla\Omega_{\ell_j}|^2
\ge
c_{\rm sh}
\frac{
\mathcal O_{\rm sh}
}{
h_{\rm harm}^2
}.
}
\tag{1.14}
$$

No bound on the number of sheets is required.

If one sheet is split into many pieces, the quantities

$$
\mathcal O_j/h_j^2
$$

remain additive.

Therefore:

$$
\boxed{
\textbf{
sheet fragmentation cannot reduce the reciprocal-thickness gradient bill.
}
}
\tag{1.15}
$$

This is the key resolution of the carrier-mass concern from DCRP-50.

The fourth main result compiles the multi-sheet filtered action into the actual unfiltered second-order Navier--Stokes action.

For each sheet piece, Jensen gives

$$
\boxed{
|\nabla\Omega_{\ell_j}|^2
\le
\varphi_{\ell_j}*
|\nabla\Omega|^2.
}
\tag{1.16}
$$

After the additional averaging kernel

$$
\eta_{\ell_j},
$$

one obtains

$$
\boxed{
\int_{U_j}
\eta_{\ell_j}*
|\nabla\Omega_{\ell_j}|^2
\le
C
\int_{\widetilde U_j}
|\nabla\Omega|^2,
}
\tag{1.17}
$$

where

$$
\widetilde U_j
$$

is a fixed-multiple enlargement of

$$
U_j.
$$

If the enlarged sheet atlas has bounded overlap

$$
\boxed{
\sum_j
\mathbf 1_{\widetilde U_j}
\le
N_{\rm ov},
}
\tag{1.18}
$$

then

$$
\boxed{
\sum_j
\int_{U_j}
\eta_{\ell_j}*
|\nabla\Omega_{\ell_j}|^2
\le
C
N_{\rm ov}
\int_{\widetilde K}
|\nabla\Omega|^2.
}
\tag{1.19}
$$

Hence:

$$
\boxed{
\int_{\widetilde K}
|\nabla\Omega|^2
\ge
\frac{
c_{\rm sh}
}{
C N_{\rm ov}
}
\frac{
\mathcal O_{\rm sh}
}{
h_{\rm harm}^2
}.
}
\tag{1.20}
$$

If bounded overlap fails, the branch has explicit sheet multiplicity/stacking.

Thus the absolute physical second-order gradient cannot be removed by sheet fragmentation unless the sheet atlas itself develops unbounded overlap.

The fifth central result inserts the actual Type-II viscosity.

During one DSS period,

$$
\boxed{
\varepsilon_n(s)
=
\varepsilon_n
e^{-(1-2\gamma)s}.
}
\tag{1.21}
$$

Therefore

$$
\boxed{
\varepsilon_n(s)
\ge
\mu^{-1}\varepsilon_n,
\qquad
0\le s\le S_0.
}
\tag{1.22}
$$

Define the normalized second-order viscous action

$$
\boxed{
\mathcal P_{2,n}
=
\int_0^{S_0}
\int_{\widetilde K}
\varepsilon_n(s)
|\nabla\Omega_n|^2
dyds.
}
\tag{1.23}
$$

Define the spacetime sheet enstrophy

$$
\boxed{
\mathcal O_{{\rm sh},n}
=
\sum_j
\int_0^{S_0}
\mathcal O_{n,j}(s)ds.
}
\tag{1.24}
$$

Define the spacetime harmonic thickness by

$$
\boxed{
\frac1{
h_{{\rm harm},n}^2
}
=
\frac{
\displaystyle
\sum_j
\int_0^{S_0}
\mathcal O_{n,j}(s)
h_{n,j}(s)^{-2}
ds
}{
\displaystyle
\mathcal O_{{\rm sh},n}
}.
}
\tag{1.25}
$$

Then:

$$
\boxed{
\mathcal P_{2,n}
\ge
c_\ast
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}
\mathcal O_{{\rm sh},n},
}
\tag{1.26}
$$

where

$$
c_\ast>0
$$

depends only on:

- the gentle-sheet curvature margin;
- the DCRP-50 rank-two spectral gap;
- thickness comparability constants;
- the atlas overlap bound;
- the fixed DSS period.

This is the main absolute-action compiler.

The sixth result supplies the core carrier mass.

Let the exact strict DSS limiting profile have a nontrivial vorticity core:

$$
\boxed{
\mathcal O_\ast
=
\int_0^{S_0}
\int_K
|\Omega_\ast|^2
dyds
>
0.
}
\tag{1.27}
$$

On a strong derivative-shadowing same-parent branch:

$$
\boxed{
\Omega_n
\to
\Omega_\ast
\quad
\text{strongly in }
L^2(K\times[0,S_0]),
}
\tag{1.28}
$$

one has:

$$
\boxed{
\mathcal O_{{\rm core},n}
\ge
\frac12
\mathcal O_\ast
}
\tag{1.29}
$$

for all large

$$
n.
$$

If the coherent sheet atlas captures a fixed fraction:

$$
\boxed{
\mathcal O_{{\rm sh},n}
\ge
\theta_{\rm sh}
\mathcal O_{{\rm core},n},
\qquad
\theta_{\rm sh}>0,
}
\tag{1.30}
$$

then:

$$
\boxed{
\mathcal O_{{\rm sh},n}
\ge
o_0
=
\frac{
\theta_{\rm sh}\mathcal O_\ast
}{2}
>0.
}
\tag{1.31}
$$

If derivative shadowing fails, retain a derivative compactness defect.

If the sheet atlas fails to capture a fixed fraction, retain carrier leakage / non-sheet enstrophy.

Thus the carrier-mass lower bound is obtained at the **whole sheet atlas level**, not on any individual sheet.

The seventh result is the decisive second-order activation dichotomy.

Define

$$
\boxed{
\delta_{{\rm harm},n}
=
\frac{
h_{{\rm harm},n}^2
}{
\varepsilon_n
}.
}
\tag{1.32}
$$

Then on the strong coherent carrier branch:

$$
\boxed{
\mathcal P_{2,n}
\ge
c_\ast
\frac{
o_0
}{
\delta_{{\rm harm},n}
}.
}
\tag{1.33}
$$

Therefore:

### subdiffusive effective sheet thickness

If

$$
\boxed{
\delta_{{\rm harm},n}
\to0,
}
\tag{1.34}
$$

then

$$
\boxed{
\mathcal P_{2,n}
\to\infty.
}
\tag{1.35}
$$

### diffusive effective sheet thickness

If

$$
\boxed{
\delta_{{\rm harm},n}
\le
C_{\rm diff}
}
\tag{1.36}
$$

uniformly, then

$$
\boxed{
\mathcal P_{2,n}
\ge
c_2>0.
}
\tag{1.37}
$$

### vanishing second-order action

If

$$
\boxed{
\mathcal P_{2,n}\to0,
}
\tag{1.38}
$$

then necessarily

$$
\boxed{
\delta_{{\rm harm},n}\to\infty
}
\tag{1.39}
$$

or one of the coherence/atlas/carrier assumptions has failed.

Thus a zero second-order-action branch can survive only by becoming **superdiffusively thick** or by entering an already declared transition defect.

This is the strongest conclusion of DCRP-51.

The eighth central result is that fragmentation is not a loophole.

Suppose:

$$
N_n\to\infty
$$

and the core enstrophy is split among more and more sheets.

Equation (1.26) still depends only on:

$$
\sum_j
\mathcal O_{n,j}/h_{n,j}^2.
$$

If all sheets remain diffusive/subdiffusive in the enstrophy-weighted harmonic sense, the total second-order action remains positive or divergent.

Thus:

$$
\boxed{
\textbf{
infinite sheet count does not by itself evade second-order diffusion.
}
}
\tag{1.40}
$$

Only **unbounded geometric overlap/multiplicity** can break the unfiltered-action compiler.

That failure is already a tube multiplicity/stacking defect.

The ninth result identifies the analytic home of

$$
\mathcal P_{2,n}.
$$

The modern filtered-vorticity balance uses a localized filtered diffusion term based on

$$
|\nabla\Omega_\ell|^2.
$$

The pairwise filtered-vorticity direction defect is converted into a first-order difference quotient and absorbed by this filtered diffusion up to lower-order enstrophy.

Thus the DCRP-51 action is not a newly invented unrelated quantity.

It lies in the same **diffusion-coercive second-order channel** already present in the filtered-vorticity obstruction architecture.

The unresolved issue is now no longer:

> does a physical second-order defect appear?

On the coherent diffusive/subdiffusive sheet branch, yes.

The remaining issue is:

> does the positive/divergent normalized second-order action admit a finite global parent budget or an irreversible same-parent return/depletion argument?

That is the new frontier:

$$
\boxed{
\textbf{
Second-Order Sheet Action /
Same-Parent Return-Depletion Closure.
}
}
\tag{1.41}
$$

---

# 2. Curved-sheet uncertainty identity

Let

$$
d
$$

be the signed distance to a smooth sheet in an injective tube.

Then

$$
\boxed{
|\nabla d|=1.
}
\tag{2.1}
$$

Therefore:

$$
\boxed{
\nabla\cdot
(d\nabla d)
=
1+d\Delta d.
}
\tag{2.2}
$$

Let

$$
G\in H^1
$$

be compactly supported in the tube, or let a cutoff be used with its boundary term retained separately.

Multiply (2.2) by

$$
|G|^2
$$

and integrate.

---

# 3. Integration by parts

Assuming zero boundary contribution:

$$
\boxed{
\int
(1+d\Delta d)
|G|^2
=
-
2
\int
d
G\cdot
(\nabla d\cdot\nabla)G.
}
\tag{3.1}
$$

If:

$$
|d\Delta d|
\le
\alpha<1,
$$

then:

$$
\boxed{
(1-\alpha)
\int
|G|^2
\le
2
\left(
\int
d^2|G|^2
\right)^{1/2}
\left(
\int
|(\nabla d\cdot\nabla)G|^2
\right)^{1/2}.
}
\tag{3.2}
$$

Since:

$$
|(\nabla d\cdot\nabla)G|
\le
|\nabla G|,
$$

the uncertainty estimate follows.

---

# 4. NEW THEOREM — Curved-Sheet Uncertainty Principle

## Theorem 4.1

Let:

$$
M_G
=
\int|G|^2>0,
$$

and:

$$
h_G^2
=
\frac{
\int d^2|G|^2
}{
M_G
}.
$$

If:

$$
|d\Delta d|
\le
\alpha<1
$$

on the support, then:

$$
\boxed{
\int
|\nabla G|^2
\ge
\frac{
(1-\alpha)^2
}{
4h_G^2
}
M_G.
}
\tag{4.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

For a flat sheet:

$$
\alpha=0,
$$

this is the standard one-dimensional normal uncertainty estimate embedded in three dimensions.

---

# 5. Curvature interpretation

If the principal curvatures satisfy:

$$
|\kappa_i|\le\kappa_\ast
$$

and the tube half-width is:

$$
\ell,
$$

DCRP-49 gives:

$$
\boxed{
|d\Delta d|
\le
\frac{
2\kappa_\ast\ell
}{
1-\kappa_\ast\ell
}.
}
\tag{5.1}
$$

Thus the uncertainty branch applies uniformly whenever:

$$
\boxed{
\kappa_\ast\ell
\le
c_{\rm gentle}
}
\tag{5.2}
$$

for a sufficiently small fixed:

$$
c_{\rm gentle}.
$$

If this fails, one enters the DCRP-50 strong-folding compiler.

---

# 6. Tightness/comparability of hard and RMS thickness

Let:

$$
h
$$

be the RMS carrier thickness and:

$$
\ell
$$

a retained hard tube half-width.

The strong-folding compiler is naturally stated at:

$$
\ell.
$$

To express its gradient gap using:

$$
h,
$$

declare the coherent tightness condition:

$$
\boxed{
\ell^2
\le
C_{\rm tight}
h^2.
}
\tag{6.1}
$$

If this fails:

$$
\ell/h\to\infty,
$$

the carrier occupies only a vanishing portion of the retained tube.

This is recorded as:

$$
\boxed{
\textbf{
normal-profile tail / thickness intermittency}.
}
\tag{6.2}
$$

Thus the full branch tree remains explicit.

---

# 7. Strong-folding gradient bound in RMS thickness

DCRP-50 gives:

$$
\ell^2
\frac{
\eta_\ell*
|\nabla\Omega_\ell|^2
}{
\eta_\ell*
|\Omega_\ell|^2
}
\ge
c_{\rm fold}.
$$

Under:

$$
\ell^2\le C_{\rm tight}h^2,
$$

$$
\boxed{
\eta_\ell*
|\nabla\Omega_\ell|^2
\ge
\frac{
c_{\rm fold}
}{
C_{\rm tight}
}
\frac{
\eta_\ell*
|\Omega_\ell|^2
}{
h^2
}.
}
\tag{7.1}
$$

Thus the gentle and strong-folding branches have the same reciprocal-RMS-thickness form.

---

# 8. Unified coherent-sheet gradient inequality

Define:

$$
c_{\rm sh}
=
\min
\left\{
\frac{
(1-\alpha)^2
}{4},
\frac{
c_{\rm fold}
}{
C_{\rm tight}
}
\right\}.
$$

Then every fully coherent sheet piece satisfies:

$$
\boxed{
\mathcal D_j
\ge
c_{\rm sh}
\frac{
\mathcal O_j
}{
h_j^2
},
}
\tag{8.1}
$$

where:

$$
\boxed{
\mathcal D_j
=
\int_{U_j}
\eta_{\ell_j}*
|\nabla\Omega_{\ell_j}|^2,
}
\tag{8.2}
$$

and:

$$
\boxed{
\mathcal O_j
=
\int_{U_j}
\eta_{\ell_j}*
|\Omega_{\ell_j}|^2.
}
\tag{8.3}
$$

If this inequality is unavailable, at least one of the following has already occurred:

- rank-one collapse;
- filtered rank lifting;
- tube multiplicity;
- curvature-gradient concentration;
- profile-tail intermittency;
- localization/source residual.

Status:

$$
\boxed{
\textbf{PROVED FROM DCRP-49/50 + THEOREM 4.1}.
}
$$

---

# 9. Harmonic-mean thickness

For any collection of sheet pieces with:

$$
\mathcal O_j>0,
$$

define:

$$
\boxed{
h_{\rm harm}^2
=
\frac{
\sum_j\mathcal O_j
}{
\sum_j\mathcal O_j/h_j^2
}.
}
\tag{9.1}
$$

Then:

$$
\boxed{
\sum_j
\frac{
\mathcal O_j
}{
h_j^2
}
=
\frac{
\mathcal O_{\rm sh}
}{
h_{\rm harm}^2
}.
}
\tag{9.2}
$$

The harmonic mean automatically emphasizes the thinnest enstrophy-bearing sheets.

---

# 10. NEW THEOREM — Fragmentation-Proof Filtered Gradient Bound

## Theorem 10.1

On the fully coherent sheet atlas:

$$
\boxed{
\sum_j
\mathcal D_j
\ge
c_{\rm sh}
\frac{
\mathcal O_{\rm sh}
}{
h_{\rm harm}^2
}.
}
\tag{10.1}
$$

### Proof

Sum (8.1) and use (9.2).

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

No sheet-count bound appears.

---

# 11. Fragmentation NO-GO

Suppose a fixed total sheet enstrophy:

$$
\mathcal O_{\rm sh}
$$

is split into:

$$
N
$$

pieces.

Even if:

$$
\mathcal O_j
\sim
\mathcal O_{\rm sh}/N,
$$

the total reciprocal-thickness bill is:

$$
\sum_j
\mathcal O_j/h_j^2.
$$

If the thickness scale is unchanged, the sum is unchanged.

If fragmentation creates thinner pieces, the bill increases.

Therefore:

$$
\boxed{
\textbf{
carrier-mass fragmentation cannot by itself make the total sheet-gradient action vanish.
}
}
\tag{11.1}
$$

The only geometric fragmentation loophole is unbounded physical overlap/multiplicity in the filter-enlarged atlas.

---

# 12. Local filter-to-unfiltered inequality

Let:

$$
\Omega_\ell
=
\varphi_\ell*\Omega.
$$

Because:

$$
\nabla\Omega_\ell
=
\varphi_\ell*
\nabla\Omega,
$$

Jensen gives:

$$
\boxed{
|\nabla\Omega_\ell|^2
\le
\varphi_\ell*
|\nabla\Omega|^2.
}
\tag{12.1}
$$

After convolution with:

$$
\eta_\ell,
$$

$$
\boxed{
\eta_\ell*
|\nabla\Omega_\ell|^2
\le
(\eta_\ell*\varphi_\ell)*
|\nabla\Omega|^2.
}
\tag{12.2}
$$

---

# 13. Enlarged tube estimate

If:

$$
U_j
$$

is one sheet piece and:

$$
\widetilde U_j
$$

is enlarged by the support radius of:

$$
\eta_{\ell_j}*\varphi_{\ell_j},
$$

then:

$$
\boxed{
\mathcal D_j
\le
C
\int_{\widetilde U_j}
|\nabla\Omega|^2.
}
\tag{13.1}
$$

The constant depends only on the declared filters.

---

# 14. Bounded-overlap atlas

Assume:

$$
\boxed{
\sum_j
\mathbf 1_{\widetilde U_j}
\le
N_{\rm ov}
}
\tag{14.1}
$$

on an enlarged recurrent core:

$$
\widetilde K.
$$

Then:

$$
\boxed{
\sum_j
\mathcal D_j
\le
C
N_{\rm ov}
\int_{\widetilde K}
|\nabla\Omega|^2.
}
\tag{14.2}
$$

If:

$$
N_{\rm ov}\to\infty,
$$

record:

$$
\boxed{
\textbf{
sheet stacking / multiplicity}.
}
\tag{14.3}
$$

---

# 15. NEW THEOREM — Absolute Unfiltered Gradient Compiler

## Theorem 15.1

On a bounded-overlap coherent sheet atlas:

$$
\boxed{
\int_{\widetilde K}
|\nabla\Omega|^2
\ge
c_{\rm abs}
\frac{
\mathcal O_{\rm sh}
}{
h_{\rm harm}^2
},
}
\tag{15.1}
$$

where:

$$
\boxed{
c_{\rm abs}
=
\frac{
c_{\rm sh}
}{
C N_{\rm ov}
}.
}
\tag{15.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is the desired carrier-mass-to-absolute-gradient bridge.

---

# 16. Period-integrated formulation

Let the sheet atlas vary in similarity time.

Define:

$$
\boxed{
\mathcal O_{{\rm sh},n}
=
\sum_j
\int_0^{S_0}
\mathcal O_{n,j}(s)ds.
}
\tag{16.1}
$$

Define:

$$
\boxed{
\frac1{
h_{{\rm harm},n}^2
}
=
\frac{
\displaystyle
\sum_j
\int_0^{S_0}
\mathcal O_{n,j}(s)
h_{n,j}(s)^{-2}ds
}{
\displaystyle
\mathcal O_{{\rm sh},n}
}.
}
\tag{16.2}
$$

Then the time-integrated version of Theorem 15.1 is:

$$
\boxed{
\int_0^{S_0}
\int_{\widetilde K}
|\nabla\Omega_n|^2
dyds
\ge
c_{\rm abs}
\frac{
\mathcal O_{{\rm sh},n}
}{
h_{{\rm harm},n}^2
}.
}
\tag{16.3}
$$

---

# 17. Core enstrophy persistence

Let:

$$
\Omega_\ast
$$

be the nonzero strict DSS limiting profile.

Choose a fixed recurrent core:

$$
K
$$

such that:

$$
\boxed{
\mathcal O_\ast
=
\int_0^{S_0}
\int_K
|\Omega_\ast|^2
dyds
>
0.
}
\tag{17.1}
$$

If:

$$
\boxed{
\Omega_n
\to
\Omega_\ast
\quad
\text{strongly in }
L^2(K\times[0,S_0]),
}
\tag{17.2}
$$

then:

$$
\boxed{
\mathcal O_{{\rm core},n}
\ge
\frac12
\mathcal O_\ast
}
\tag{17.3}
$$

for all large:

$$
n.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

If this derivative-level shadowing fails, retain a derivative compactness / second-order profile defect.

---

# 18. Sheet-carrier coverage

Assume the coherent sheet atlas captures a fixed fraction:

$$
\boxed{
\mathcal O_{{\rm sh},n}
\ge
\theta_{\rm sh}
\mathcal O_{{\rm core},n},
\qquad
\theta_{\rm sh}>0.
}
\tag{18.1}
$$

Then:

$$
\boxed{
\mathcal O_{{\rm sh},n}
\ge
o_0
=
\frac{
\theta_{\rm sh}
\mathcal O_\ast
}{2}
>0.
}
\tag{18.2}
$$

If the coverage fails, a positive fraction of the core enstrophy is not represented by the coherent rank-two sheet atlas.

This is:

$$
\boxed{
\textbf{
carrier leakage / non-sheet residual}.
}
\tag{18.3}
$$

---

# 19. Type-II viscosity over one period

Let:

$$
\lambda=1-2\gamma,
\qquad
\mu=e^{\lambda S_0}.
$$

The Type-II viscosity is:

$$
\boxed{
\varepsilon_n(s)
=
\varepsilon_n
e^{-\lambda s}.
}
\tag{19.1}
$$

Therefore:

$$
\boxed{
\mu^{-1}\varepsilon_n
\le
\varepsilon_n(s)
\le
\varepsilon_n.
}
\tag{19.2}
$$

---

# 20. Second-order viscous sheet action

Define:

$$
\boxed{
\mathcal P_{2,n}
=
\int_0^{S_0}
\int_{\widetilde K}
\varepsilon_n(s)
|\nabla\Omega_n|^2
dyds.
}
\tag{20.1}
$$

Using (16.3) and (19.2):

$$
\boxed{
\mathcal P_{2,n}
\ge
c_2
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}
\mathcal O_{{\rm sh},n}.
}
\tag{20.2}
$$

Here:

$$
c_2
=
\mu^{-1}c_{\rm abs}.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 21. NEW THEOREM — Positive / Divergent Second-Order Activation

## Theorem 21.1

On the strong coherent carrier branch:

$$
\boxed{
\mathcal P_{2,n}
\ge
c_2o_0
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}.
}
\tag{21.1}
$$

Therefore:

### subdiffusive harmonic thickness

If:

$$
\boxed{
h_{{\rm harm},n}^2/\varepsilon_n
\to0,
}
\tag{21.2}
$$

then:

$$
\boxed{
\mathcal P_{2,n}\to\infty.
}
\tag{21.3}
$$

### diffusive-or-thinner harmonic thickness

If:

$$
\boxed{
h_{{\rm harm},n}^2
\le
C_{\rm diff}
\varepsilon_n,
}
\tag{21.4}
$$

then:

$$
\boxed{
\mathcal P_{2,n}
\ge
\frac{
c_2o_0
}{
C_{\rm diff}
}
>0.
}
\tag{21.5}
$$

### vanishing second-order action

If:

$$
\boxed{
\mathcal P_{2,n}\to0,
}
\tag{21.6}
$$

then:

$$
\boxed{
h_{{\rm harm},n}^2/\varepsilon_n
\to\infty
}
\tag{21.7}
$$

or one of the coherent-carrier assumptions fails.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED CONDITIONAL ON THE DECLARED STRONG SHEET ATLAS}.
}
$$

---

# 22. Meaning of the superdiffusive escape

The condition:

$$
h_{{\rm harm},n}^2/\varepsilon_n\to\infty
$$

means that the enstrophy-weighted sheet thickness is much larger than the viscous scale:

$$
\sqrt{\varepsilon_n}.
$$

This is not the pure Euler subdiffusive pancake shadow.

Thus a zero second-order-action branch must abandon the DCRP-47 thin-sheet equality geometry.

It becomes a thickness-transition branch.

---

# 23. Fragmentation cannot save subdiffusive sheets

Suppose:

$$
N_n\to\infty
$$

sheet pieces divide the core enstrophy into smaller and smaller masses.

The quantity:

$$
h_{{\rm harm},n}^{-2}
=
\frac{
\sum_j\int\mathcal O_{j}/h_j^2
}{
\sum_j\int\mathcal O_j
}
$$

does not contain:

$$
N_n
$$

explicitly.

If all the new sheets remain thin, their reciprocal-thickness contributions add.

Hence:

$$
\boxed{
\textbf{
arbitrarily fine sheet fragmentation is not a mass-vanishing loophole.
}
}
\tag{23.1}
$$

The only fragmentation escape is geometric stacking that destroys the bounded-overlap atlas or coherent sheet representation.

---

# 24. Effective multiplicity

Define the atlas overlap number:

$$
\boxed{
N_{\rm ov}
=
\left\|
\sum_j
\mathbf 1_{\widetilde U_j}
\right\|_{L^\infty}.
}
\tag{24.1}
$$

Then the absolute gradient compiler constant is:

$$
\propto
N_{\rm ov}^{-1}.
$$

Thus:

$$
\boxed{
N_{\rm ov}\to\infty
}
$$

is the exact way sheet fragmentation can defeat the single physical-gradient integral.

This is not invisible fragmentation.

It is:

$$
\boxed{
\textbf{
sheet stacking / multiplicity concentration}.
}
\tag{24.2}
$$

---

# 25. Derivative-shadowing alternative

The core enstrophy lower bound used:

$$
\Omega_n\to\Omega_\ast
$$

strongly in:

$$
L^2.
$$

If only velocity-level compactness is available and derivative shadowing fails, one has already produced a higher-order compactness defect.

Therefore the branch tree is:

$$
\boxed{
\text{derivative compactness failure}
}
$$

or:

$$
\boxed{
\text{persistent core enstrophy}.
}
$$

No derivative convergence is silently assumed.

---

# 26. Filtered-vorticity calibration

Runlong Yu's finite-scale theorem places positive near-field filtered vortex stretching into a pairwise filtered-vorticity direction defect and then converts that defect to a first-order filtered-vorticity difference quotient controlled by filtered diffusion, up to a lower-order enstrophy reservoir.

The localized filtered enstrophy balance leaves only far-field strain, commutator forcing, and localization residuals after that diffusion closure.

Thus the DCRP-51 quantity:

$$
\varepsilon
\int
|\nabla\Omega_\ell|^2
$$

is exactly in the diffusion-coercive analytic sector already identified by the external finite-scale theory.

DCRP-51 adds the sheet-geometry and harmonic-thickness mechanism that forces this channel to become positive on the surviving thin-sheet branch.

---

# 27. Why positivity is not yet a contradiction

The Navier--Stokes energy inequality controls:

$$
\nu
\int
|\nabla u|^2,
$$

not directly the second-order quantity:

$$
\nu
\int
|\nabla\omega|^2.
$$

Therefore:

$$
\boxed{
\mathcal P_{2,n}\ge c>0
}
$$

or even:

$$
\boxed{
\mathcal P_{2,n}\to\infty
}
$$

in normalized Type-II charts is not by itself a global regularity contradiction.

It is a genuine higher-order viscous obstruction coordinate.

The next theorem must supply a return/depletion, delayed-action, or parent-level finite-budget argument.

---

# 28. Relation to DCRP-28 / DCRP-33

Earlier rounds isolated:

- anomalous Type-II viscous energy residue;
- second-order Kelvin circulation residue;
- delayed second-order action as a candidate parent-level carrier.

DCRP-51 now derives an actual source of second-order vorticity diffusion from the sheet geometry.

Thus the previous abstract higher-order viscous channels acquire a concrete geometric realization:

$$
\boxed{
\textbf{
thin/folded rank-two sheet}
\Longrightarrow
\textbf{
second-order filtered vorticity diffusion}.
}
}
\tag{28.1}
$$

The precise conversion between:

$$
\mathcal P_{2,n}
$$

and the earlier delayed second-order/Oseen action remains open.

---

# 29. A stronger normalized rate statement

Let:

$$
\mathcal O_{{\rm sh},n}\ge o_0.
$$

Then:

$$
\boxed{
\frac{
\mathcal P_{2,n}
}{
\mathcal O_{{\rm sh},n}
}
\ge
c_2
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}.
}
\tag{29.1}
$$

Thus the **second-order viscous rate per unit sheet enstrophy** diverges on every subdiffusive harmonic-thickness branch.

This statement is independent of sheet fragmentation.

---

# 30. Sheet uncertainty versus Batchelor floor

DCRP-48/49 showed:

$$
h^2\sim\varepsilon
$$

for coherent viscous sheets unless a residual is activated.

DCRP-51 shows that at exactly that diffusive thickness:

$$
\varepsilon/h^2
\sim1,
$$

so persistent core enstrophy automatically produces a positive second-order action gap.

Thus the viscous floor does not make the second-order channel disappear.

It places the surviving coherent sheet precisely at an order-one second-order diffusion rate.

---

# 31. Stronger subdiffusive branch

If the sheet attempts to shadow the pure Euler normal contraction:

$$
h^2/\varepsilon\to0,
$$

then:

$$
\varepsilon/h^2\to\infty.
$$

Once the sheet enstrophy is retained at the atlas level, the second-order action diverges.

This is the analytic counterpart of the DCRP-49 statement that viscosity cannot follow the Euler subdiffusive sheet without a residual.

---

# 32. Carrier leakage branch

If:

$$
\mathcal O_{{\rm sh},n}
/
\mathcal O_{{\rm core},n}
\to0,
$$

the rank-two sheet atlas ceases to carry the singular core vorticity.

Then the obstruction has moved into:

- non-sheet vorticity;
- rank-three geometry;
- diffuse carrier;
- localization;
- source/leakage.

This is already a branch transition.

Thus sheet carrier mass cannot disappear silently.

---

# 33. Correct master branch after DCRP-51

The strong strict Type-II rank-two sheet branch now satisfies at least one of:

$$
\boxed{
\text{derivative compactness failure}
}
$$

or:

$$
\boxed{
\text{carrier leakage / loss of sheet coverage}
}
$$

or:

$$
\boxed{
\text{unbounded sheet stacking/multiplicity}
}
$$

or:

$$
\boxed{
\text{rank-one collapse / rank-three lifting}
}
$$

or:

$$
\boxed{
\text{profile-tail / thickness intermittency}
}
$$

or:

$$
\boxed{
\text{superdiffusive thickness transition}
}
$$

or:

$$
\boxed{
\text{positive/divergent second-order viscous action}.
}
$$

Thus the original "enstrophy mass may vanish" loophole has been compiled.

---

# 34. What DCRP-51 closes

DCRP-50 ended with the concern:

> the relative second-order diffusion rate can diverge while the absolute sheet carrier mass tends to zero.

DCRP-51 shows that:

1. persistent core enstrophy is available on the derivative-shadowing branch;

2. that enstrophy may be split among arbitrarily many sheets;

3. reciprocal thickness is additive under that split;

4. bounded-overlap filtering compiles the multi-sheet sum into one actual physical:

   $$
   \int|\nabla\Omega|^2;
   $$

5. therefore fragmentation cannot make the second-order action vanish while the enstrophy-weighted effective thickness remains diffusive/subdiffusive.

This is the precise carrier-mass closure.

---

# 35. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Second-Order Sheet Action /
Same-Parent Return-Depletion Closure.
}
}
$$

A useful theorem would connect:

$$
\boxed{
\mathcal P_{2,n}
=
\int
\varepsilon_n
|\nabla\Omega_n|^2
}
$$

to one of the already retained parent-level higher-order channels:

1. delayed second-order action;

2. Oseen second-order saturation;

3. second-order Kelvin residue;

4. filtered derivative-compatible increment defect;

5. a finite parent-level budget or monotone depletion law.

The strongest desired statement is:

$$
\boxed{
\mathcal P_{2,n}\ge c>0
\text{ on infinitely many same-parent returns}
\Longrightarrow
\text{non-summable native parent cost}.
}
$$

That theorem is not yet proved.

---

# 36. Source-status audit

The external filtered-vorticity source proves a finite-scale coercive mechanism in which filtered vorticity-direction defects are converted into first-order filtered-vorticity difference quotients and absorbed by the localized filtered diffusion term. After this insertion, remaining positive surplus is assigned to far-field strain, commutator forcing, and localization residuals.

This validates the analytic role of:

$$
|\nabla\Omega_\ell|^2
$$

as the correct diffusion-coercive object at finite scale.

DCRP-51's project-specific contribution is the geometric and multi-sheet argument that forces a positive amount of that second-order channel from thin rank-two sheet recurrence.

---

# 37. End state

For a gently curved sheet carrier:

$$
\boxed{
\int|\nabla G|^2
\ge
\frac{
(1-\alpha)^2
}{
4h^2
}
\int|G|^2.
}
$$

For a thickness-scale folded coherent rank-two sheet, DCRP-50 supplies the same reciprocal-thickness structure or an existing rank/multiplicity defect.

For a sheet atlas:

$$
\boxed{
h_{\rm harm}^2
=
\frac{
\sum_j\mathcal O_j
}{
\sum_j\mathcal O_j/h_j^2
}.
}
$$

Therefore:

$$
\boxed{
\int|\nabla\Omega|^2
\gtrsim
\frac{
\mathcal O_{\rm sh}
}{
h_{\rm harm}^2
}
}
$$

under bounded atlas overlap.

With Type-II viscosity:

$$
\boxed{
\mathcal P_{2,n}
\gtrsim
\frac{
\varepsilon_n
}{
h_{{\rm harm},n}^2
}
\mathcal O_{{\rm sh},n}.
}
$$

Persistent strict-DSS core enstrophy gives:

$$
\boxed{
\mathcal O_{{\rm sh},n}\ge o_0>0
}
$$

on the strong sheet-carrier branch.

Hence:

$$
\boxed{
h_{{\rm harm},n}^2/\varepsilon_n\to0
\Longrightarrow
\mathcal P_{2,n}\to\infty,
}
$$

while:

$$
\boxed{
h_{{\rm harm},n}^2
\lesssim
\varepsilon_n
\Longrightarrow
\mathcal P_{2,n}\ge c>0.
}
$$

Fragmentation does not remove this bill.

The remaining frontier is:

$$
\boxed{
\textbf{
Second-Order Sheet Action /
Same-Parent Return-Depletion Closure.
}
}
$$