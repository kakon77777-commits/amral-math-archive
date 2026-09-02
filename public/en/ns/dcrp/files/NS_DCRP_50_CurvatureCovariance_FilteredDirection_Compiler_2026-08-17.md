# NS-DCRP-50 — Thickness-Scale Curvature, Covariance-Kernel Differentiation, and the Filtered Vorticity-Direction Compiler

- date: 2026-08-17
- status: research proof checkpoint / folding-to-physical-defect compiler
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. compile the DCRP-49 thickness-scale curvature escape into physical vorticity/rank/tube defects;
  2. separate loss of tubular injectivity from smooth curvature;
  3. introduce a sheet-scale filtered normalized vorticity covariance;
  4. prove that a coherent rank-two covariance kernel differentiates with the sheet normal;
  5. prove that thickness-scale curvature forces a scale-invariant filtered vorticity-gradient gap unless rank coherence fails;
  6. split that gradient gap into vorticity-magnitude and vorticity-direction channels;
  7. connect the direction channel to the existing filtered vortex-stretching/difference-quotient architecture;
  8. prove a normal-turn / curvature-gradient trichotomy as a purely geometric backup compiler;
  9. classify all remaining escapes as rank-one collapse, rank-three lifting, covariance-weight rearrangement, tube multiplicity, magnitude-gradient concentration, direction-gradient concentration, or source/leakage residual;
  10. identify the next frontier as converting the sheet-scale filtered gradient gap into a same-parent non-summable or second-order viscous defect.
- no full Navier--Stokes regularity claim is made.
- principal external primary source:
  - R. Yu, *Filtered Vortex Stretching and Subgrid Defects for the Three-Dimensional Navier--Stokes Equations*, arXiv:2606.27560v1.
- geometric calibration:
  - standard surface identity $\nabla_\Sigma n=\mathrm{II}$ / shape operator;
  - standard tubular-neighborhood reach criterion for the signed-distance chart.
- internal dependencies:
  - DCRP-38 rank-two covariance nondegeneracy;
  - DCRP-41 planar covariance anisotropy;
  - DCRP-49 material-sheet viscous thickness floor and curvature necessity.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-49 proved that a subdiffusive coherent material sheet:

$$
\boxed{
H_n/\varepsilon_n\to0
}
\tag{1.1}
$$

cannot persist with all nongeometric tube residuals:

$$
o(\varepsilon_n)
$$

unless the sheet enters a thickness-scale curvature regime.

Schematically:

$$
\boxed{
\kappa_{\ast,n}\ell_n
\gtrsim
c_{\rm curv}>0.
}
\tag{1.2}
$$

Here:

-:

  $$
  \kappa_{\ast,n}
  $$

  is the maximal principal-curvature magnitude;

-:

  $$
  \ell_n
  $$

  is the retained sheet half-thickness.

DCRP-50 proves that this geometric escape cannot remain invisible.

At a sheet-scale filter:

$$
\ell
$$

define a smoothed vorticity:

$$
\boxed{
\Omega_\ell
=
\varphi_\ell*\Omega.
}
\tag{1.3}
$$

Let:

$$
\eta_\ell
$$

be a second nonnegative smooth averaging kernel at the same comparable scale.

Define the local filtered enstrophy mass:

$$
\boxed{
m_\ell
=
\eta_\ell*
|\Omega_\ell|^2.
}
\tag{1.4}
$$

Whenever:

$$
m_\ell>0,
$$

define the normalized covariance:

$$
\boxed{
C_\ell
=
\frac{
\eta_\ell*
(
\Omega_\ell\otimes\Omega_\ell
)
}{
m_\ell
}.
}
\tag{1.5}
$$

Then:

$$
\boxed{
C_\ell=C_\ell^T\ge0,
\qquad
\operatorname{tr}C_\ell=1.
}
\tag{1.6}
$$

Suppose the rank-two sheet remains coherent at the filter scale:

$$
\boxed{
C_\ell n=0,
}
\tag{1.7}
$$

where:

$$
n
$$

is the material-sheet normal.

Suppose the covariance stays away from rank one:

$$
\boxed{
\lambda_{\min}^{+}(C_\ell)
\ge
b_0>0.
}
\tag{1.8}
$$

Then differentiating the kernel relation along a unit sheet tangent:

$$
X
$$

gives:

$$
\boxed{
(\nabla_XC_\ell)n
+
C_\ell\nabla_Xn
=
0.
}
\tag{1.9}
$$

Since:

$$
\boxed{
\nabla_Xn
=
\mathrm{II}(X)
}
\tag{1.10}
$$

up to the conventional sign of the shape operator, and:

$$
\nabla_Xn\in n^\perp,
$$

the planar spectral gap implies:

$$
\boxed{
\|\nabla_XC_\ell\|_{\rm op}
\ge
b_0
|\mathrm{II}(X)|.
}
\tag{1.11}
$$

Taking the strongest tangential direction:

$$
\boxed{
|\nabla_\Sigma C_\ell|
\ge
b_0
|\mathrm{II}|_{\rm op}.
}
\tag{1.12}
$$

This is the first central theorem:

$$
\boxed{
\textbf{
sheet curvature}
\Longrightarrow
\textbf{
covariance-gradient activity}
}
\tag{1.13}
$$

unless rank coherence fails.

The second central theorem converts covariance-gradient activity into physical vorticity-gradient activity.

Let:

$$
B_\ell
=
\eta_\ell*
(
\Omega_\ell\otimes\Omega_\ell
).
$$

For any spatial derivative:

$$
\partial_j,
$$

Cauchy--Schwarz gives:

$$
\boxed{
|\partial_jB_\ell|
\le
2
\left(
\eta_\ell*
|\Omega_\ell|^2
\right)^{1/2}
\left(
\eta_\ell*
|\partial_j\Omega_\ell|^2
\right)^{1/2}.
}
\tag{1.14}
$$

Likewise:

$$
\boxed{
|\partial_jm_\ell|
\le
2
m_\ell^{1/2}
\left(
\eta_\ell*
|\partial_j\Omega_\ell|^2
\right)^{1/2}.
}
\tag{1.15}
$$

Because:

$$
|B_\ell|_{\rm op}\le m_\ell,
$$

differentiating:

$$
C_\ell=B_\ell/m_\ell
$$

gives:

$$
\boxed{
|\partial_jC_\ell|
\le
4
\left[
\frac{
\eta_\ell*
|\partial_j\Omega_\ell|^2
}{
m_\ell
}
\right]^{1/2}.
}
\tag{1.16}
$$

Hence:

$$
\boxed{
\eta_\ell*
|\nabla\Omega_\ell|^2
\ge
\frac{
m_\ell
}{
16
}
|\nabla C_\ell|^2.
}
\tag{1.17}
$$

Combining with (1.12):

$$
\boxed{
\eta_\ell*
|\nabla\Omega_\ell|^2
\ge
\frac{
b_0^2
}{
16
}
m_\ell
|\mathrm{II}|_{\rm op}^2.
}
\tag{1.18}
$$

Multiplying by:

$$
\ell^2,
$$

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
\frac{
b_0^2
}{
16
}
\left(
\ell
|\mathrm{II}|_{\rm op}
\right)^2.
}
\tag{1.19}
$$

Therefore thickness-scale curvature:

$$
\boxed{
\ell|\mathrm{II}|_{\rm op}
\ge
c_{\rm curv}
}
\tag{1.20}
$$

forces the scale-invariant filtered gradient gap:

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
c_{\rm grad}
=
\frac{
b_0^2c_{\rm curv}^2
}{
16
}
>0.
}
\tag{1.21}
$$

This is the principal physical compiler of DCRP-50.

The third central result splits the gap into magnitude and direction.

Where:

$$
\Omega_\ell\neq0,
$$

write:

$$
\boxed{
\Omega_\ell
=
\rho_\ell
\xi_\ell,
\qquad
\rho_\ell
=
|\Omega_\ell|,
\qquad
|\xi_\ell|=1.
}
\tag{1.22}
$$

Then exactly:

$$
\boxed{
|\nabla\Omega_\ell|^2
=
|\nabla\rho_\ell|^2
+
\rho_\ell^2
|\nabla\xi_\ell|^2.
}
\tag{1.23}
$$

Hence the DCRP-50 gradient gap forces at least one of:

$$
\boxed{
\textbf{
vorticity-magnitude gradient}
}
$$

or:

$$
\boxed{
\textbf{
vorticity-direction gradient}.
}
$$

On a compact normalized sheet class with nontrivial filtered enstrophy mass, at least one channel has a fixed scale-normalized lower gap.

The direction channel is exactly the geometry used by the modern filtered-vortex-stretching framework: positive near-field stretching is bounded by a pairwise defect of filtered vorticity directions, and the magnitude-weighted angular defect is converted into a first-order difference quotient of filtered vorticity controlled by filtered diffusion.

Thus DCRP-50 connects thickness-scale sheet curvature to the same family of angular/diffusive defects already present in the DCRP program.

The fourth central result handles loss of exact covariance kernel coherence.

If:

$$
C_\ell n\neq0,
$$

then filtering across the thickness scale has produced a nonzero covariance component in the sheet-normal direction.

This is a **filtered rank-lifting / plane-spread defect**.

If:

$$
\lambda_{\min}^{+}(C_\ell)\to0,
$$

the rank-two plane covariance collapses toward rank one and returns to the DCRP-39 rank-one branch.

Therefore the complete rank-two sheet-scale alternative is:

$$
\boxed{
\textbf{
rank-one collapse}
\ \vee\
\textbf{
filtered rank lifting}
\ \vee\
\textbf{
scale-normalized filtered vorticity-gradient gap}.
}
\tag{1.24}
$$

The fifth result handles the signed-distance tube itself.

If the normal injectivity radius/reach of the sheet is no larger than the retained half-thickness:

$$
\boxed{
\operatorname{reach}(\Sigma)
\le
\ell,
}
\tag{1.25}
$$

then the nearest-point projection used in DCRP-49 is not single valued throughout the retained tube.

This is already:

$$
\boxed{
\textbf{
sheet multiplicity / tube-injectivity failure}.
}
\tag{1.26}
$$

Thus DCRP-50 only applies the covariance-gradient compiler on the smooth injective-tube branch.

The sixth result gives a purely geometric backup compiler.

Suppose at:

$$
p\in\Sigma
$$

$$
\boxed{
|\mathrm{II}(p)|_{\rm op}
\ge
c_0/\ell.
}
\tag{1.27}
$$

Fix an upper curvature envelope:

$$
\boxed{
\ell
\|\mathrm{II}\|_{L^\infty(B_\Sigma(p,\rho\ell))}
\le
K_0.
}
\tag{1.28}
$$

Then for sufficiently small:

$$
\rho=\rho(c_0,K_0)>0,
$$

one has the dichotomy:

$$
\boxed{
\ell^2
\|\nabla_\Sigma\mathrm{II}\|_{L^\infty}
\ge
c_1
}
\tag{1.29}
$$

or there exists:

$$
q\in
B_\Sigma(p,\rho\ell)
$$

with:

$$
\boxed{
|n(q)-n(p)|
\ge
c_2>0.
}
\tag{1.30}
$$

Thus thickness-scale curvature produces:

$$
\boxed{
\textbf{
curvature-gradient concentration}
\ \vee\
\textbf{
order-one Gauss-map turn}.
}
\tag{1.31}
$$

If the upper curvature envelope itself fails:

$$
\ell\|\mathrm{II}\|_\infty\to\infty,
$$

that is an even stronger curvature-amplitude concentration channel.

The seventh result converts a Gauss-map turn into a covariance increment under rank-two nondegeneracy.

Let:

$$
C_p,C_q
$$

be trace-one positive semidefinite rank-two covariance matrices with:

$$
\ker C_p=\operatorname{span}\{n_p\},
\qquad
\ker C_q=\operatorname{span}\{n_q\},
$$

and:

$$
\lambda_{\min}^{+}(C_p)\ge b_0.
$$

Then:

$$
\boxed{
\|C_p-C_q\|_{\rm op}
\ge
b_0
\left[
1-
(n_p\cdot n_q)^2
\right].
}
\tag{1.32}
$$

Indeed:

$$
n_q^TC_qn_q=0,
$$

while:

$$
n_q^TC_pn_q
\ge
b_0
|P_{n_p^\perp}n_q|^2.
$$

Thus an order-one plane-normal turn yields an order-one covariance increment.

On a compact filtered sheet class, such a covariance increment must be produced by at least one of:

- filtered vorticity-direction redistribution;
- filtered vorticity-magnitude weight redistribution;
- rank loss/lifting;
- localization/commutator transition.

This is the **direction-or-weight compiler**.

Combining DCRP-49 and DCRP-50 gives the principal theorem:

$$
\boxed{
\begin{aligned}
&\textbf{
subdiffusive coherent Navier--Stokes sheet shadowing}
\\
&\Longrightarrow
\textbf{
order-}\varepsilon
\textbf{ source/leakage/rank residual}
\\
&\qquad\vee\
\textbf{
tube multiplicity/injectivity failure}
\\
&\qquad\vee\
\textbf{
rank-one collapse}
\\
&\qquad\vee\
\textbf{
filtered rank lifting / plane spread}
\\
&\qquad\vee\
\textbf{
scale-normalized vorticity-magnitude gradient}
\\
&\qquad\vee\
\textbf{
scale-normalized vorticity-direction gradient}
\\
&\qquad\vee\
\textbf{
curvature-gradient concentration}.
\end{aligned}
}
\tag{1.33}
$$

Thus **thickness-scale folding is now compiled into physical or transition defects**.

It is no longer an unclassified geometric escape.

The remaining problem is not to prove that some defect exists.

It is to prove that the resulting sheet-scale gradient/direction defect either:

1. enters an already non-summable same-parent budget;
2. activates a second-order viscous residue;
3. forces rank lifting;
4. or cannot recur in the strict DSS equality state.

That is the next frontier:

$$
\boxed{
\textbf{
Sheet-Scale Gradient Recurrence /
Second-Order Diffusive Closure.
}
}
\tag{1.34}
$$

---

# 2. Filtered covariance construction

Let:

$$
\varphi,\eta
\in
C_c^\infty(\mathbb R^3),
$$

with:

$$
\varphi,\eta\ge0,
\qquad
\int\varphi
=
\int\eta
=
1.
$$

At sheet scale:

$$
\ell>0,
$$

set:

$$
\boxed{
\Omega_\ell
=
\varphi_\ell*\Omega.
}
\tag{2.1}
$$

Define:

$$
\boxed{
B_\ell
=
\eta_\ell*
(
\Omega_\ell\otimes\Omega_\ell
),
}
\tag{2.2}
$$

and:

$$
\boxed{
m_\ell
=
\operatorname{tr}B_\ell
=
\eta_\ell*
|\Omega_\ell|^2.
}
\tag{2.3}
$$

Whenever:

$$
m_\ell>0,
$$

define:

$$
\boxed{
C_\ell
=
B_\ell/m_\ell.
}
\tag{2.4}
$$

Then:

$$
C_\ell
$$

is a normalized positive covariance tensor.

---

# 3. Rank-two coherence conditions

The exact coherent filtered rank-two branch assumes:

$$
\boxed{
C_\ell n=0.
}
\tag{3.1}
$$

This says the sheet normal is still the missing covariance direction after smoothing at the physical sheet scale.

Let the two positive eigenvalues of:

$$
C_\ell
$$

be:

$$
\lambda_1\ge\lambda_2>0.
$$

The nondegeneracy condition is:

$$
\boxed{
\lambda_2
\ge
b_0>0.
}
\tag{3.2}
$$

If DCRP-41's planar anisotropy parameter obeys:

$$
\vartheta_2
\ge
\vartheta_0>0,
$$

then one may take:

$$
\boxed{
b_0
=
\frac{
1-\sqrt{1-\vartheta_0}
}{
2
}.
}
\tag{3.3}
$$

Thus the spectral gap is equivalent to staying away from the rank-one boundary.

---

# 4. NEW THEOREM — Covariance-Kernel Differentiation

## Theorem 4.1

Let:

$$
X
$$

be a unit tangent vector to the material sheet.

On the coherent filtered rank-two branch:

$$
\boxed{
\|\nabla_XC_\ell\|_{\rm op}
\ge
b_0
|\nabla_Xn|.
}
\tag{4.1}
$$

Therefore:

$$
\boxed{
|\nabla_\Sigma C_\ell|
\ge
b_0
|\mathrm{II}|_{\rm op}.
}
\tag{4.2}
$$

### Proof

Differentiate:

$$
C_\ell n=0
$$

along:

$$
X.
$$

Then:

$$
(\nabla_XC_\ell)n
+
C_\ell\nabla_Xn
=
0.
$$

Because:

$$
n\cdot\nabla_Xn=0,
$$

the vector:

$$
\nabla_Xn
$$

belongs to the positive covariance plane.

Therefore:

$$
|C_\ell\nabla_Xn|
\ge
b_0
|\nabla_Xn|.
$$

The first term has norm at most:

$$
\|\nabla_XC_\ell\|_{\rm op}.
$$

Use:

$$
\nabla_\Sigma n
=
\mathrm{II}
$$

up to the usual sign convention.

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

# 5. Derivative of the covariance numerator

For a spatial derivative:

$$
\partial_j,
$$

$$
\partial_jB_\ell
=
\eta_\ell*
\left[
(\partial_j\Omega_\ell)\otimes\Omega_\ell
+
\Omega_\ell\otimes
(\partial_j\Omega_\ell)
\right].
$$

Therefore:

$$
\boxed{
|\partial_jB_\ell|
\le
2
m_\ell^{1/2}
D_{j,\ell}^{1/2},
}
\tag{5.1}
$$

where:

$$
\boxed{
D_{j,\ell}
=
\eta_\ell*
|\partial_j\Omega_\ell|^2.
}
\tag{5.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 6. Derivative of filtered enstrophy mass

Likewise:

$$
\boxed{
\partial_jm_\ell
=
2
\eta_\ell*
(
\Omega_\ell\cdot
\partial_j\Omega_\ell
),
}
\tag{6.1}
$$

so:

$$
\boxed{
|\partial_jm_\ell|
\le
2
m_\ell^{1/2}
D_{j,\ell}^{1/2}.
}
\tag{6.2}
$$

---

# 7. NEW THEOREM — Covariance Gradient Controlled by Vorticity Gradient

## Theorem 7.1

Whenever:

$$
m_\ell>0,
$$

$$
\boxed{
|\partial_jC_\ell|
\le
4
\left(
D_{j,\ell}/m_\ell
\right)^{1/2}.
}
\tag{7.1}
$$

Consequently:

$$
\boxed{
\eta_\ell*
|\nabla\Omega_\ell|^2
\ge
\frac{
m_\ell
}{
16
}
|\nabla C_\ell|^2.
}
\tag{7.2}
$$

### Proof

Differentiate:

$$
C_\ell
=
B_\ell/m_\ell.
$$

Then:

$$
\partial_jC_\ell
=
\frac{
\partial_jB_\ell
}{
m_\ell
}
-
\frac{
B_\ell
\partial_jm_\ell
}{
m_\ell^2
}.
$$

Since:

$$
|B_\ell|_{\rm op}
\le
m_\ell,
$$

insert the bounds from Sections 5--6.

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

# 8. NEW THEOREM — Curvature-to-Vorticity-Gradient Compiler

## Theorem 8.1

On the coherent nondegenerate rank-two branch:

$$
\boxed{
\eta_\ell*
|\nabla\Omega_\ell|^2
\ge
\frac{
b_0^2
}{
16
}
m_\ell
|\mathrm{II}|_{\rm op}^2.
}
\tag{8.1}
$$

Equivalently:

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
\frac{
b_0^2
}{
16
}
\left(
\ell
|\mathrm{II}|_{\rm op}
\right)^2.
}
\tag{8.2}
$$

Thus:

$$
\boxed{
\ell|\mathrm{II}|_{\rm op}
\ge
c_{\rm curv}
}
$$

implies:

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
\frac{
b_0^2c_{\rm curv}^2
}{
16
}
>0.
}
\tag{8.3}
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

# 9. Physical scaling interpretation

The quantity:

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
}
\tag{9.1}
$$

is dimensionless.

It measures whether the filtered vorticity changes by order one across the sheet thickness.

Thus DCRP-49's:

$$
\kappa_\ast\ell
\gtrsim1
$$

cannot remain a purely geometric statement.

On a coherent nondegenerate rank-two sheet it forces a thickness-scale physical vorticity variation.

---

# 10. Magnitude-direction decomposition

Where:

$$
\Omega_\ell\neq0,
$$

write:

$$
\Omega_\ell
=
\rho_\ell\xi_\ell.
$$

Then:

$$
\partial_j\Omega_\ell
=
(\partial_j\rho_\ell)\xi_\ell
+
\rho_\ell
\partial_j\xi_\ell.
$$

Since:

$$
\xi_\ell\cdot
\partial_j\xi_\ell=0,
$$

$$
\boxed{
|\nabla\Omega_\ell|^2
=
|\nabla\rho_\ell|^2
+
\rho_\ell^2
|\nabla\xi_\ell|^2.
}
\tag{10.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 11. NEW THEOREM — Magnitude-or-Direction Gradient Alternative

## Theorem 11.1

Under the hypotheses of Theorem 8.1, at least one of the following holds with at least half the normalized gradient gap:

$$
\boxed{
\ell^2
\frac{
\eta_\ell*
|\nabla\rho_\ell|^2
}{
m_\ell
}
\ge
\frac{
b_0^2
}{
32
}
(
\ell|\mathrm{II}|
)^2
}
\tag{11.1}
$$

or:

$$
\boxed{
\ell^2
\frac{
\eta_\ell*
\left[
\rho_\ell^2
|\nabla\xi_\ell|^2
\right]
}{
m_\ell
}
\ge
\frac{
b_0^2
}{
32
}
(
\ell|\mathrm{II}|
)^2.
}
\tag{11.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus thickness-scale folding forces either:

- vorticity-amplitude variation;
- vorticity-direction variation.

---

# 12. Filtered direction-defect calibration

The external filtered-vorticity theorem proves that positive near-field vortex stretching is controlled by a pairwise defect of the filtered vorticity direction.

It further converts the angular defect into a first-order difference quotient of filtered vorticity, which is absorbed by filtered diffusion up to a lower-order enstrophy reservoir.

DCRP-50's direction-gradient branch therefore lives in exactly the same geometric/diffusive sector.

The present theorem does not claim that the sheet-scale direction-gradient gap automatically produces a **uniform core-scale** near-field stretching gap, because the filter ratio may itself be shrinking.

That final scale-ratio bridge remains to be proved.

Status:

$$
\boxed{
\textbf{EXTERNAL CALIBRATION / PARTIAL COMPILER}.
}
$$

---

# 13. Filter-ratio caution

In the filtered-vorticity framework, fixed relative filter scale:

$$
\ell=\sigma r
$$

has uniform constants in the physical scale.

The DCRP sheet thickness:

$$
\ell_n
$$

may be much smaller than the recurrent core radius.

Therefore:

$$
\boxed{
\textbf{
sheet-scale gradient activity}
}
$$

must not be silently identified with a fixed-ratio core-scale defect.

The remaining bridge is a nested-scale/relative-filter compiler.

This is an explicit limitation of DCRP-50.

---

# 14. Loss of covariance kernel

Suppose:

$$
\boxed{
C_\ell n\neq0.
}
\tag{14.1}
$$

Then the sheet-scale filtered vorticity covariance has nonzero normal support.

This means at least one of:

- neighboring tangent planes differ enough across the filter;
- normal vorticity has appeared;
- multiple layers with different planes enter the filter;
- the declared rank-two chart is no longer coherent.

Define schematically:

$$
\boxed{
\mathcal R_{\rm rank,\ell}
=
|C_\ell n|.
}
\tag{14.2}
$$

A positive value is a native filtered rank-lifting / plane-spread residual.

---

# 15. Rank-one collapse

If:

$$
\boxed{
\lambda_{\min}^{+}(C_\ell)\to0,
}
\tag{15.1}
$$

the filtered covariance approaches rank one.

This returns to the DCRP-39 axial/Burgers-jet branch.

Thus the covariance-gradient theorem needs no artificial uniform nondegeneracy assumption in the full branch tree:

failure of the assumption is already an existing low-rank alternative.

---

# 16. Plane projector increment

For unit normals:

$$
n_p,n_q,
$$

define:

$$
P_p=I-n_p\otimes n_p,
\qquad
P_q=I-n_q\otimes n_q.
$$

Then:

$$
\boxed{
\|P_p-P_q\|_F^2
=
2
\left[
1-(n_p\cdot n_q)^2
\right].
}
\tag{16.1}
$$

Thus an order-one Gauss-map turn is exactly an order-one plane-projector increment.

---

# 17. NEW LEMMA — Plane Turn Forces Covariance Increment

Let:

$$
C_p,C_q
$$

be trace-one positive semidefinite rank-two matrices with:

$$
C_pn_p=0,
\qquad
C_qn_q=0,
$$

and:

$$
\lambda_{\min}^{+}(C_p)\ge b_0.
$$

Then:

$$
\boxed{
\|C_p-C_q\|_{\rm op}
\ge
b_0
\left[
1-(n_p\cdot n_q)^2
\right].
}
\tag{17.1}
$$

### Proof

Since:

$$
C_qn_q=0,
$$

$$
n_q^T(C_p-C_q)n_q
=
n_q^TC_pn_q.
$$

The projection of:

$$
n_q
$$

onto:

$$
n_p^\perp
$$

has squared length:

$$
1-(n_p\cdot n_q)^2.
$$

The positive planar spectrum of:

$$
C_p
$$

is bounded below by:

$$
b_0.
$$

Hence:

$$
n_q^TC_pn_q
\ge
b_0
[
1-(n_p\cdot n_q)^2
].
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

# 18. Direction-or-weight interpretation of covariance increments

Write the normalized covariance abstractly as:

$$
\boxed{
C_x
=
\int
\xi\otimes\xi
\,d\mu_x(\xi),
}
\tag{18.1}
$$

where:

$$
\mu_x
$$

is the magnitude-squared weighted local distribution of filtered vorticity directions.

Then a large:

$$
\|C_p-C_q\|
$$

must come from:

1. a change in the direction distribution;

2. a change in the magnitude weights/localization distribution;

3. rank creation/loss.

Thus an order-one plane turn on a nondegenerate compact sheet class yields:

$$
\boxed{
\textbf{
direction redistribution}
\ \vee\
\textbf{
covariance-weight rearrangement}
\ \vee\
\textbf{
rank transition}.
}
\tag{18.2}
$$

A fully quantitative optimal-coupling inequality may be added later if required.

---

# 19. Geometric backup: curvature spike or normal turn

Suppose at:

$$
p\in\Sigma
$$

$$
|\mathrm{II}(p)|_{\rm op}
\ge
c_0/\ell.
$$

If:

$$
\ell
\|\mathrm{II}\|_{L^\infty}
$$

is unbounded, record:

$$
\boxed{
\text{curvature-amplitude concentration}.
}
\tag{19.1}
$$

Otherwise assume:

$$
\ell
\|\mathrm{II}\|_{L^\infty}
\le
K_0.
$$

Choose a principal direction at:

$$
p
$$

and the corresponding geodesic.

Taylor expansion of the Gauss map gives, for:

$$
t=O(\ell),
$$

$$
\boxed{
n(\gamma(t))
=
n(p)
-
t\,S_p\dot\gamma(0)
+
O
\left[
t^2
\left(
\|\nabla_\Sigma S\|_\infty
+
\|S\|_\infty^2
\right)
\right].
}
\tag{19.2}
$$

Thus, for sufficiently small fixed:

$$
\rho>0,
$$

at:

$$
t=\rho\ell,
$$

either:

$$
\boxed{
\ell^2
\|\nabla_\Sigma\mathrm{II}\|_\infty
\ge
c_1(c_0,K_0)
}
\tag{19.3}
$$

or:

$$
\boxed{
|n(\gamma(\rho\ell))-n(p)|
\ge
c_2(c_0,K_0)
>0.
}
\tag{19.4}
$$

Status:

$$
\boxed{
\textbf{PROVED AS A LOCAL SMOOTH-SURFACE TAYLOR DICHOTOMY}.
}
$$

---

# 20. Meaning of curvature-gradient concentration

The quantity:

$$
\boxed{
\ell^2
|\nabla_\Sigma\mathrm{II}|
}
\tag{20.1}
$$

is dimensionless.

A fixed lower bound means the sheet geometry itself develops second-order variation at its own thickness scale.

Because:

$$
\mathrm{II}
=
\nabla_\Sigma n,
$$

this is a second derivative of the plane-normal field.

DCRP-50 retains it as a **tube-geometry second-order transition coordinate**.

A direct universal inequality from:

$$
\nabla_\Sigma\mathrm{II}
$$

to:

$$
\nabla^2\Omega
$$

is not asserted without additional sheet-coherence hypotheses.

---

# 21. Tube injectivity / multiplicity branch

The signed-distance chart used in DCRP-49 requires a tubular neighborhood with unique nearest-point projection.

If:

$$
\boxed{
\operatorname{reach}(\Sigma)
\le
\ell,
}
\tag{21.1}
$$

the retained thickness reaches the medial/focal geometry.

Then:

- different normal rays may intersect;
- nearest-point projection may cease to be unique;
- multiple sheet layers may enter one tube.

This is recorded as:

$$
\boxed{
\mathcal R_{\rm mult}>0.
}
\tag{21.2}
$$

No curvature-to-gradient theorem is required on this branch.

---

# 22. DCRP-49 curvature amount

DCRP-49 proved only:

$$
\limsup
\kappa_\ast\ell>0
$$

under the stated small-residual assumptions.

A more quantitative lower constant can be extracted from the period recurrence.

If all noncurvature tube residuals satisfy:

$$
o(\varepsilon_n),
$$

then the normalized curvature contribution must cancel the positive coefficient:

$$
\mathfrak D_{\rm nor}.
$$

Because:

$$
|\mathcal E_{\rm curv}|
\le
4\varepsilon
\frac{
\kappa_\ast\ell
}{
1-\kappa_\ast\ell
},
$$

there exists:

$$
\boxed{
c_{\rm curv}
=
c
(
\mathfrak D_{\rm nor},
\gamma,S_0
)
>0
}
\tag{22.1}
$$

such that, along a subsequence:

$$
\boxed{
\kappa_\ast\ell
\ge
c_{\rm curv}.
}
\tag{22.2}
$$

The exact optimal constant is not needed for the compiler.

---

# 23. NEW THEOREM — Thickness-Scale Folding Compiler

## Theorem 23.1

Consider a same-parent strict Type-II sheet sequence satisfying:

1.:

   $$
   H_n/\varepsilon_n\to0;
   $$

2. normal-strain/Taylor/source leakage errors smaller than:

   $$
   o(\varepsilon_n);
   $$

3. a smooth material tube exists at thickness:

   $$
   \ell_n.
   $$

Then along a subsequence at least one of the following occurs:

### tube multiplicity

$$
\boxed{
\operatorname{reach}(\Sigma_n)
\le
\ell_n;
}
\tag{23.1}
$$

### rank-one collapse

$$
\boxed{
\lambda_{\min}^{+}(C_{\ell_n})
\to0;
}
\tag{23.2}
$$

### filtered rank lifting / plane spread

$$
\boxed{
|C_{\ell_n}n_n|
\ge
c_{\rm rank}>0
}
\tag{23.3}
$$

on a normalized witness patch;

### vorticity-gradient gap

$$
\boxed{
\ell_n^2
\frac{
\eta_{\ell_n}*
|\nabla\Omega_{\ell_n}|^2
}{
\eta_{\ell_n}*
|\Omega_{\ell_n}|^2
}
\ge
c_{\rm grad}>0;
}
\tag{23.4}
$$

### curvature-gradient concentration

$$
\boxed{
\ell_n^2
|\nabla_{\Sigma_n}\mathrm{II}_n|
\ge
c_{\rm II}>0.
}
\tag{23.5}
$$

The fourth branch further splits into:

$$
\boxed{
\text{magnitude-gradient}
\ \vee\
\text{direction-gradient}.
}
\tag{23.6}
$$

Status:

$$
\boxed{
\textbf{PROVED / CONDITIONAL ON THE DECLARED COHERENT FILTERED-COVARIANCE COMPILER}.
}
$$

---

# 24. Relation to filtered near-field coercivity

The filtered-vorticity theorem establishes:

$$
\boxed{
\mathcal V_{r,\ell}^{+,\mathrm{near}}
\lesssim
\mathcal A_{r,\ell}^{\mathrm{pair}},
}
\tag{24.1}
$$

where:

$$
\mathcal A_{r,\ell}^{\mathrm{pair}}
$$

is a magnitude-weighted pairwise filtered-vorticity direction defect.

It also proves:

$$
\boxed{
\mathcal A_{r,\ell}^{\mathrm{pair}}
\le
\eta
\mathcal P_{r,\ell}^{\rho}
+
C_\eta
M_{r,\rho}(u)
\left(
\frac r\ell
\right)^5
\mathcal O_{r,\ell}.
}
\tag{24.2}
$$

At fixed relative:

$$
\ell=\sigma r,
$$

the constants are scale uniform.

Thus the DCRP-50 direction-gradient branch is aligned with an existing diffusion-coercive direction-defect channel.

The unresolved issue is the potentially small ratio:

$$
\ell_n/r_{\rm core}.
$$

---

# 25. Difference-quotient architecture

The same external source defines a local first-order difference-quotient operator and proves an:

$$
L^2
$$

bound by:

$$
\nabla\Omega_\ell.
$$

This confirms that the natural analytic object corresponding to direction incoherence is a first-order vorticity increment at the filtered scale.

DCRP-50 does not reverse that upper bound blindly.

Instead it retains:

$$
\ell^2
|\nabla\Omega_\ell|^2
$$

as the sheet-scale physical gradient witness and treats conversion to a fixed-ratio commutator defect as the next scale-bridge problem.

---

# 26. Why the compiler is stronger than normal-turn language

DCRP-49 ended at:

$$
\kappa_\ast\ell\gtrsim1.
$$

One could describe this merely as:

> the sheet folds strongly.

DCRP-50 shows that, provided the rank-two covariance remains coherent,

$$
\boxed{
\text{strong folding}
\Longrightarrow
\text{strong spatial change of the vorticity covariance}
\Longrightarrow
\text{strong vorticity gradient}.
}
$$

Thus the folding is visible to the PDE.

It is not merely an external geometric decoration.

---

# 27. Why rank-two nondegeneracy matters

If the vorticity covariance were rank one, the common vorticity direction could lie along the intersection of many differently tilted tangent planes.

Then a changing plane normal need not force a changing vorticity direction.

This is exactly why DCRP-50 requires:

$$
\lambda_{\min}^{+}(C_\ell)\ge b_0.
$$

Failure returns to the already isolated rank-one branch.

Thus the spectral-gap hypothesis is logically sharp for a plane-to-vorticity compiler.

---

# 28. Weight-rearrangement escape

A covariance tensor may change because the magnitude-squared weights of different directions change even when the direction field itself changes little.

This is not ignored.

It is the:

$$
\boxed{
\textbf{
covariance-weight rearrangement}
}
$$

branch.

In a filtered equation this belongs naturally with:

- localization;
- commutator;
- source/leakage;

rather than pure direction geometry.

A future quantitative transport metric on the local direction measure:

$$
\mu_x
$$

could separate angle and weight changes more sharply.

---

# 29. Compact-class finite gradient witness

Suppose a compact normalized sheet class has:

-:

  $$
  m_\ell\ge m_0>0;
  $$

-:

  $$
  \lambda_{\min}^{+}(C_\ell)\ge b_0;
  $$

-:

  $$
  \ell|\mathrm{II}|\ge c_{\rm curv};
  $$

on a patch of normalized measure:

$$
\ge v_0>0.
$$

Then:

$$
\boxed{
\ell^2
\int_{\rm patch}
|\nabla\Omega_\ell|^2
\ge
c
m_0
b_0^2
c_{\rm curv}^2
v_0.
}
\tag{29.1}
$$

Thus the folding branch has a finite sheet-scale physical-gradient compiler gap.

This is not yet a same-parent non-summability theorem.

---

# 30. Potential second-order viscous meaning

The Navier--Stokes vorticity diffusion term contains:

$$
\varepsilon_n\Delta\Omega_n.
$$

A thickness-scale gradient gap suggests a diffusive cost of order:

$$
\boxed{
\varepsilon_n
\int
|\nabla\Omega|^2.
}
\tag{30.1}
$$

If:

$$
\ell_n^2
\ll
\varepsilon_n,
$$

the scale:

$$
\ell_n
$$

is subdiffusive and the normalized factor:

$$
\varepsilon_n/\ell_n^2
$$

is large.

Therefore a fixed sheet-scale gradient ratio may become a strong second-order viscous signal.

However the relevant volume/enstrophy normalization must be audited before claiming a non-summable payment.

Status:

$$
\boxed{
\textbf{PROMISING / NOT YET CLOSED}.
}
$$

---

# 31. Possible subdiffusive amplification

Suppose:

$$
\ell_n^2/\varepsilon_n\to0
$$

and the folding compiler gives:

$$
\ell_n^2
\frac{
\int|\nabla\Omega_{\ell_n}|^2
}{
\int|\Omega_{\ell_n}|^2
}
\ge
c.
$$

Then formally:

$$
\boxed{
\varepsilon_n
\frac{
\int|\nabla\Omega_{\ell_n}|^2
}{
\int|\Omega_{\ell_n}|^2
}
\ge
c
\frac{
\varepsilon_n
}{
\ell_n^2
}
\to\infty.
}
\tag{31.1}
$$

Thus **relative vorticity diffusion rate** diverges on the subdiffusive folding branch.

This is a genuine quantitative signal.

It does not alone prove that the absolute dissipation has a nonzero lower bound because the enstrophy mass may vanish.

The next theorem should combine this rate with the persistent rank-two core carrier normalization.

---

# 32. Exact next bridge

The needed statement is a lower bound of the form:

$$
\boxed{
\int_{\rm sheet}
|\Omega_{\ell_n}|^2
\ge
m_\ast
\times
\text{appropriate same-parent scale}
}
\tag{32.1}
$$

on the surviving strict branch.

Then (31.1) would produce a normalized second-order viscous cost.

Candidate sources for such a lower bound include:

- DCRP-38 core covariance nontriviality;
- DCRP-35 periodic enstrophy demand;
- DCRP-42 scalar turnover;
- DCRP-47 weighted sheet-form flux.

This is now the shortest analytic closure route.

---

# 33. Corrected final sheet branch

After DCRP-49/50, the strongest subdiffusive rank-two Navier--Stokes sheet cannot be:

- smooth;
- gently curved;
- rank-two coherent;
- low-gradient;
- low-residual.

It must enter:

$$
\boxed{
\begin{aligned}
&
\text{tube multiplicity}
\\
&\vee
\text{rank-one collapse}
\\
&\vee
\text{rank-three/filter rank lifting}
\\
&\vee
\text{magnitude-gradient concentration}
\\
&\vee
\text{direction-gradient concentration}
\\
&\vee
\text{curvature-gradient concentration}
\\
&\vee
\text{order-}\varepsilon
\text{ leakage/source residual}.
\end{aligned}
}
\tag{33.1}
$$

Thus **thickness-scale folding has been compiled**.

---

# 34. What DCRP-50 closes

The following unresolved phrase from DCRP-49 is removed:

> perhaps the sheet simply folds at its own thickness scale.

That is no longer an unclassified escape.

If the tube remains injective and rank-two coherent, folding produces a scale-normalized filtered vorticity-gradient gap.

If the tube or rank-two covariance does not remain coherent, the failure is already a native transition defect.

Thus every thickness-scale fold is visible somewhere in the DCRP state package.

---

# 35. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Sheet-Scale Gradient Recurrence /
Second-Order Diffusive Closure.
}
}
$$

A useful theorem would combine:

$$
\boxed{
\ell_n^2
\frac{
\int
|\nabla\Omega_{\ell_n}|^2
}{
\int
|\Omega_{\ell_n}|^2
}
\ge
c
}
$$

with a same-parent lower bound on the persistent sheet enstrophy mass to force:

$$
\boxed{
\text{positive / divergent normalized second-order viscous action}.
}
$$

The desired closure alternatives are:

1. filtered direction defect enters the known diffusion-coercive channel;

2. vorticity-magnitude gradient enters a second-order supplier defect;

3. the enstrophy carrier mass vanishes, contradicting periodic rank-two covariance demand;

4. rank lifting or multiplicity occurs;

5. a residual term of order:

   $$
   \varepsilon_n
   $$

   cancels the viscous floor.

This is now the sharpest genuinely viscous sheet-scale frontier.

---

# 36. Source-status audit

Runlong Yu's 2026 filtered-vorticity work proves that positive near-field stretching is controlled by a magnitude-weighted pairwise defect of filtered vorticity directions.

It then converts that angular defect into a first-order difference quotient of filtered vorticity and absorbs the resulting term by filtered diffusion up to a lower-order enstrophy reservoir.

The same work explicitly separates remaining positive surplus into far-field strain, commutator forcing, and localization residuals.

DCRP-50's magnitude/direction gradient alternatives therefore fit the same finite-scale defect architecture.

The present round adds a project-specific geometric compiler from thickness-scale material-sheet curvature to the filtered covariance/vorticity-gradient sector.

---

# 37. End state

DCRP-49 forces, on the subdiffusive low-residual branch:

$$
\boxed{
\ell|\mathrm{II}|
\gtrsim1.
}
$$

For the sheet-scale filtered covariance:

$$
\boxed{
C_\ell
=
\frac{
\eta_\ell*
(
\Omega_\ell\otimes\Omega_\ell
)
}{
\eta_\ell*
|\Omega_\ell|^2
},
}
$$

rank-two coherence gives:

$$
\boxed{
C_\ell n=0.
}
$$

Differentiating:

$$
\boxed{
|\nabla_\Sigma C_\ell|
\ge
b_0|\mathrm{II}|.
}
$$

But:

$$
\boxed{
|\nabla C_\ell|
\le
4
\left[
\frac{
\eta_\ell*
|\nabla\Omega_\ell|^2
}{
\eta_\ell*
|\Omega_\ell|^2
}
\right]^{1/2}.
}
$$

Therefore:

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
\frac{
b_0^2
}{
16
}
(
\ell|\mathrm{II}|
)^2.
}
$$

Thus thickness-scale curvature forces:

$$
\boxed{
\text{vorticity-magnitude gradient}
\ \vee\
\text{vorticity-direction gradient}
}
$$

unless rank coherence or tube injectivity has already failed.

The unresolved geometric escape from DCRP-49 has therefore been converted into physical filtered-vorticity or native transition defects.

The next frontier is:

$$
\boxed{
\textbf{
Sheet-Scale Gradient Recurrence /
Second-Order Diffusive Closure.
}
}
$$