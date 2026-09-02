# NS-DCRP-53 — Gaussian Width-to-Strain Reconstruction, Harmonic Supplier Orthogonality, and Finite Matching-Layer Rigidity

- date: 2026-08-17
- status: research proof checkpoint / Batchelor--Gaussian equality reduction
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. determine whether the DCRP-52 Batchelor--Gaussian sheet can self-generate the affine pancake strain required to maintain its normal profile;
  2. prove a local Hodge/harmonic decomposition showing that the one-normal-profile vorticity generates only a shear strain, while the diagonal pancake strain belongs to a harmonic/nonlocal velocity component;
  3. reconstruct the required pancake strain waveform directly from the viscosity-scaled Gaussian variance waveform;
  4. derive an exact period-averaged reciprocal-variance/Fisher identity;
  5. derive an orthogonal decomposition of the Gaussian strain action into its universal minimum plus profile-breathing penalties;
  6. characterize the minimum-action Gaussian equality as constant normalized variance and constant affine strain;
  7. prove that the global Gaussian shear and the global affine-strain normal form are incompatible with the strict sublinear Type-II kinetic-energy tail;
  8. obtain a quantitative finite upper bound on the radius of any exact affine-Gaussian core region;
  9. conclude that every Batchelor--Gaussian equality state must be a local core coupled to a finite normalized matching layer;
  10. audit the normal vorticity-flux amplitude equation and state precisely when a nonzero matching-layer flux replenishment is mandatory;
  11. avoid the incorrect inference that Gaussian shape recurrence alone implies flux-amplitude recurrence;
  12. identify the next frontier as the coupled finite-annulus strain-supplier / vorticity-flux matching problem.
- no full Navier--Stokes regularity claim is made.
- principal external primary calibration:
  - K. Shariff, G. E. Elsinga, *Viscous vortex layers subject to more general strain and comparison to isotropic turbulence*, arXiv:2102.01266v2;
  - T. Gallay, Y. Maekawa, *Three-dimensional stability of Burgers vortices*, arXiv:1002.2489;
  - T. Gallay, C. E. Wayne, *Existence and stability of asymmetric Burgers vortices*, arXiv:math/0503353.
- internal dependencies:
  - DCRP-35/36 finite-annulus affine strain supplier and reproduction identity;
  - DCRP-41 canonical pancake strain;
  - DCRP-48 coherent normal Fokker--Planck equation;
  - DCRP-52 Gaussian Batchelor return rigidity.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive result

DCRP-52 reduced the strongest coherent diffusive rank-two branch to a Batchelor-scale Gaussian normal profile.

DCRP-53 shows that this Gaussian sheet is **not self-contained**.

On the exact fixed-plane one-normal-profile branch,

$$
\boxed{
\Omega(z,s)
=
\zeta(z,s)e_1.
}
\tag{1.1}
$$

A divergence-free shear primitive is

$$
\boxed{
V_{\rm sh}(z,s)
=
U(z,s)e_2,
\qquad
-U_z=\zeta.
}
\tag{1.2}
$$

Its strain is

$$
\boxed{
S_{\rm sh}
=
\frac{
U_z
}{2}
\left(
e_2\otimes e_3
+
e_3\otimes e_2
\right).
}
\tag{1.3}
$$

The canonical pancake strain is

$$
\boxed{
A_{\rm pan}
=
a(s)
T,
\qquad
T
=
\operatorname{diag}(1,1,-2).
}
\tag{1.4}
$$

Since

$$
\boxed{
T:S_{\rm sh}=0,
}
\tag{1.5}
$$

the Gaussian sheet's one-dimensional self-field has **zero projection onto the diagonal pancake-strain sector**.

More generally, if

$$
V
$$

has the same one-dimensional vorticity in a simply connected local core, then

$$
\boxed{
H
=
V-V_{\rm sh}
}
\tag{1.6}
$$

satisfies

$$
\boxed{
\nabla\times H=0,
\qquad
\nabla\cdot H=0.
}
\tag{1.7}
$$

Hence locally

$$
\boxed{
H=\nabla\phi,
\qquad
\Delta\phi=0.
}
\tag{1.8}
$$

Therefore the required pancake affine strain belongs to the **harmonic/nonlocal component**

$$
\boxed{
\nabla^2\phi.
}
\tag{1.9}
$$

This gives the first central theorem:

$$
\boxed{
\textbf{
the Batchelor--Gaussian sheet does not self-generate its diagonal pancake strain;
the strain must be supplied by harmonic boundary/nonlocal data.
}
}
\tag{1.10}
$$

This is the local mathematical version of the background-strain interpretation of classical viscous vortex layers.

The second central result shows that the Gaussian width determines that nonlocal strain uniquely.

Let

$$
\boxed{
\lambda
=
1-2\gamma
>0,
}
\tag{1.11}
$$

and let the Type-II viscosity during one return be

$$
\boxed{
\varepsilon(s)
=
\varepsilon_n e^{-\lambda s}.
}
\tag{1.12}
$$

Let

$$
h^2(s)
$$

be the Gaussian normal variance and define the viscosity-scaled variance

$$
\boxed{
\delta(s)
=
\frac{
h^2(s)
}{
\varepsilon(s)
}.
}
\tag{1.13}
$$

The DCRP-48 exact variance equation is

$$
\boxed{
(h^2)'
=
2
[
\gamma-2a(s)
]
h^2
+
2\varepsilon(s).
}
\tag{1.14}
$$

Because

$$
\varepsilon'/\varepsilon=-\lambda,
$$

one obtains

$$
\boxed{
\delta'
=
[
1-4a(s)
]
\delta
+
2.
}
\tag{1.15}
$$

Thus

$$
\boxed{
a(s)
=
\frac14
+
\frac1{
2\delta(s)
}
-
\frac14
\frac{
\delta'(s)
}{
\delta(s)
}.
}
\tag{1.16}
$$

This is the exact **Gaussian width-to-strain reconstruction formula**.

The third central theorem follows from one-period recurrence.

On the same-parent Gaussian fixed-profile branch,

$$
\boxed{
\delta(S_0)=\delta(0).
}
\tag{1.17}
$$

DCRP-41 gives

$$
\boxed{
\bar a
=
\frac1{S_0}
\int_0^{S_0}
a(s)ds
=
\frac{
2-3\gamma
}{2}.
}
\tag{1.18}
$$

Integrating (1.16) over one period yields

$$
\boxed{
\frac1{S_0}
\int_0^{S_0}
\frac{
ds
}{
\delta(s)
}
=
\frac32
(1-2\gamma)
=
\frac32\lambda.
}
\tag{1.19}
$$

For a Gaussian probability profile

$$
f(z,s)
$$

with variance

$$
h^2(s),
$$

the Fisher information is

$$
\boxed{
I(f(s))
=
\frac1{
h^2(s)
}.
}
\tag{1.20}
$$

Therefore

$$
\boxed{
\varepsilon(s)I(f(s))
=
\frac1{
\delta(s)
}.
}
\tag{1.21}
$$

Hence every recurrent zero-residual Gaussian sheet obeys the exact Fisher signature

$$
\boxed{
\int_0^{S_0}
\varepsilon(s)
I(f(s))
ds
=
\frac32
(1-2\gamma)
S_0.
}
\tag{1.22}
$$

This value is independent of the detailed strain waveform.

The fourth central theorem decomposes the strain action.

Since

$$
\boxed{
\bar a
=
\frac14
+
\frac34\lambda,
}
\tag{1.23}
$$

(1.16) gives

$$
\boxed{
a-\bar a
=
\frac12
\left[
\delta^{-1}
-
\frac32\lambda
\right]
-
\frac14
(\log\delta)'.
}
\tag{1.24}
$$

The two terms are orthogonal over one period because

$$
\boxed{
\int_0^{S_0}
\left[
\delta^{-1}
-
\frac32\lambda
\right]
(\log\delta)'
ds
=
0.
}
\tag{1.25}
$$

Therefore

$$
\boxed{
\int_0^{S_0}
(a-\bar a)^2ds
=
\frac14
\int_0^{S_0}
\left[
\delta^{-1}
-
\frac32\lambda
\right]^2ds
+
\frac1{16}
\int_0^{S_0}
[
(\log\delta)'
]^2ds.
}
\tag{1.26}
$$

Hence

$$
\boxed{
\int_0^{S_0}
a^2ds
=
S_0\bar a^2
+
\frac14
\int
\left[
\delta^{-1}
-
\frac32\lambda
\right]^2
+
\frac1{16}
\int
[
(\log\delta)'
]^2.
}
\tag{1.27}
$$

Since

$$
|T|_F^2=6,
$$

the pancake strain action is

$$
\boxed{
\int_0^{S_0}
|A_{\rm pan}|_F^2ds
=
6S_0\bar a^2
+
\frac32
\int
\left[
\delta^{-1}
-
\frac32\lambda
\right]^2
+
\frac38
\int
[
(\log\delta)'
]^2.
}
\tag{1.28}
$$

The universal minimum is

$$
\boxed{
6S_0\bar a^2
=
\frac32
(2-3\gamma)^2S_0.
}
\tag{1.29}
$$

Every nontrivial Gaussian width breathing adds a strictly positive harmonic-strain action.

The fifth central result characterizes equality.

The minimum in (1.28) is achieved if and only if

$$
\boxed{
\delta(s)
\equiv
\delta_0
}
\tag{1.30}
$$

and

$$
\boxed{
a(s)
\equiv
\bar a.
}
\tag{1.31}
$$

Using (1.19),

$$
\boxed{
\delta_0
=
\frac{
2
}{
3(1-2\gamma)
}.
}
\tag{1.32}
$$

Therefore the **minimum-reproduction Gaussian sheet** has:

$$
\boxed{
a_0
=
\frac{
2-3\gamma
}{2},
}
\tag{1.33}
$$

and constant viscosity-scaled normal variance

$$
\boxed{
\delta_0
=
\frac{
2
}{
3(1-2\gamma)
}.
}
\tag{1.34}
$$

This is the narrowest constant-strain Batchelor--Gaussian equality state.

The sixth central result is a global no-go.

A one-dimensional nonzero Gaussian vorticity sheet has

$$
\boxed{
\int_{\mathbb R}
\zeta(z)dz
=
M\neq0.
}
\tag{1.35}
$$

Its shear primitive satisfies

$$
\boxed{
U(+\infty)-U(-\infty)
=
-M.
}
\tag{1.36}
$$

After any additive velocity gauge, at least one asymptotic shear plateau has magnitude at least

$$
|M|/2.
$$

Therefore for all large

$$
R,
$$

$$
\boxed{
\int_{B_R}
|V_{\rm sh}|^2dy
\ge
c
M^2
R^3.
}
\tag{1.37}
$$

The strict Type-II tail allows only

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2
dyds
\le
C_E
R^\kappa,
\qquad
0<\kappa<1.
}
\tag{1.38}
$$

Hence a nonzero global one-dimensional Gaussian shear layer is impossible.

Likewise a nonzero global affine pancake field has

$$
\boxed{
\int_{B_R}
|A_{\rm pan}y|^2dy
=
\frac{
4\pi
}{
15
}
|A_{\rm pan}|_F^2
R^5
=
\frac{
8\pi
}{5}
a(s)^2
R^5.
}
\tag{1.39}
$$

Thus the affine component is even more incompatible with the sublinear tail.

Therefore

$$
\boxed{
\textbf{
a global Batchelor--Gaussian affine sheet is impossible in the strict Type-II tail class.
}
}
\tag{1.40}
$$

The Batchelor--Gaussian normal form must be local.

The seventh central result makes the matching radius quantitative.

Suppose the exact affine-Gaussian normal form holds on the centered ball

$$
B_R
$$

for the entire period and the translational gauge is removed.

The cross term between

$$
A_{\rm pan}y
$$

and the one-dimensional shear integrates to zero on the centered ball.

Therefore

$$
\boxed{
C_E
R^\kappa
\ge
\frac{
8\pi
}{5}
R^5
\int_0^{S_0}
a(s)^2ds.
}
\tag{1.41}
$$

Hence

$$
\boxed{
R^{5-\kappa}
\le
\frac{
5C_E
}{
8\pi
\displaystyle
\int_0^{S_0}
a(s)^2ds
}.
}
\tag{1.42}
$$

Using the universal strain-action minimum,

$$
\boxed{
R^{5-\kappa}
\le
\frac{
5C_E
}{
12\pi
(2-3\gamma)^2
S_0
}.
}
\tag{1.43}
$$

up to the declared normalization convention for the tail constant.

Thus the exact affine-Gaussian core has a **finite normalized matching radius**.

The matching layer cannot be pushed to infinity.

The eighth central conclusion is therefore

$$
\boxed{
\textbf{
Batchelor--Gaussian core}
+
\textbf{
finite matching annulus}
}
\tag{1.44}
$$

with the matching region responsible for at least one of:

- harmonic affine-strain supply;
- tangential localization of the one-dimensional shear;
- vorticity-flux exchange;
- PFET/pressure work;
- rank/plane transition;
- commutator/localization residual.

This is the unforced local replacement for the externally imposed background strain of classical viscous-layer models.

The ninth result is a flux-amplitude audit.

For the ideal closed one-dimensional coherent component,

$$
\boxed{
\partial_s\zeta
+
\sigma(s)z\partial_z\zeta
=
[a(s)-1]\zeta
+
\varepsilon(s)\zeta_{zz},
}
\tag{1.45}
$$

define

$$
\boxed{
M(s)
=
\int_{\mathbb R}
\zeta(z,s)dz.
}
\tag{1.46}
$$

Then

$$
\boxed{
M'
=
[
\gamma-a(s)-1
]
M.
}
\tag{1.47}
$$

Therefore the source-free one-period multiplier is

$$
\boxed{
\rho_M
=
\exp
\left[
\frac{
5\gamma-4
}{2}
S_0
\right].
}
\tag{1.48}
$$

For

$$
2/5<\gamma<1/2,
$$

$$
\boxed{
0<\rho_M<1.
}
\tag{1.49}
$$

This proves:

$$
\boxed{
\textbf{
a source-free closed one-dimensional flux amplitude is not period-preserving.
}
}
\tag{1.50}
$$

However DCRP-53 makes an important logical correction:

$$
\boxed{
\textbf{
Gaussian shape recurrence under same-parent re-rooting does not automatically imply }M(S_0)=M(0).
}
}
\tag{1.51}
$$

Therefore (1.50) is **not** an unconditional contradiction to the DCRP-52 root-to-root Gaussian shape branch.

If one additionally imposes recurrent flux amplitude, then a matching-layer source is mandatory.

With a normal-integrated source

$$
J(s),
$$

$$
\boxed{
M'
=
[
\gamma-a(s)-1
]
M
+
J.
}
\tag{1.52}
$$

Let

$$
\boxed{
b(s)
=
\gamma-a(s)-1.
}
\tag{1.53}
$$

If

$$
M(S_0)=M(0)=M_0>0,
$$

variation of constants gives the exact source identity

$$
\boxed{
\int_0^{S_0}
\exp
\left[
\int_\tau^{S_0}
b(s)ds
\right]
J(\tau)d\tau
=
(1-\rho_M)M_0
>0.
}
\tag{1.54}
$$

Thus flux-amplitude recurrence has a quantitative replenishment gap.

This is **CONDITIONAL** on amplitude recurrence.

The tenth central conclusion is that the strongest coherent zero-excess branch is no longer an arbitrary Gaussian sheet.

It is:

$$
\boxed{
\textbf{
a local constant-width Batchelor--Gaussian sheet}
}
$$

held by

$$
\boxed{
\textbf{
a nonlocally supplied constant pancake strain}
}
$$

and necessarily joined to

$$
\boxed{
\textbf{
a finite normalized matching annulus}.
}
$$

If the sheet width breathes, the annular harmonic supplier pays a positive modulation action.

If the flux amplitude itself is recurrent, the matching system also pays a positive flux-replenishment amount.

The next frontier is therefore

$$
\boxed{
\textbf{
Finite Matching Annulus /
Coupled Strain--Vorticity-Flux Reproduction.
}
}
\tag{1.55}
$$

The key question is now:

> can one finite unforced annular region simultaneously regenerate the required harmonic pancake strain, localize the Gaussian shear, close the vorticity-flux ledger, and supply the already-required inward PFET with all transition/commutator/rank costs asymptotically zero?

That is the narrowest remaining coherent viscous equality problem.

---

# 2. Local shear primitive

Assume in a simply connected fixed-plane core

$$
\Omega
=
\zeta(z,s)e_1.
$$

Choose

$$
\boxed{
V_{\rm sh}
=
U(z,s)e_2,
\qquad
U_z=-\zeta.
}
\tag{2.1}
$$

Then

$$
\nabla\cdot V_{\rm sh}=0
$$

and

$$
\nabla\times V_{\rm sh}
=
\zeta e_1.
$$

Its velocity gradient has only

$$
\partial_zV_2
=
U_z.
$$

Thus

$$
\boxed{
S_{\rm sh}
=
\frac{
U_z
}{2}
(
e_2\otimes e_3
+
e_3\otimes e_2
).
}
\tag{2.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 3. Pancake-strain projection

Let

$$
\boxed{
T
=
e_1\otimes e_1
+
e_2\otimes e_2
-
2e_3\otimes e_3.
}
\tag{3.1}
$$

Then

$$
\boxed{
T:S_{\rm sh}=0.
}
\tag{3.2}
$$

Thus the one-dimensional sheet self-strain has no component in the canonical pancake diagonal sector.

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 4. NEW THEOREM — Harmonic Supplier Decomposition

## Theorem 4.1

Let

$$
V
$$

be any divergence-free velocity in a simply connected local core with

$$
\nabla\times V
=
\zeta(z,s)e_1.
$$

Then

$$
\boxed{
V
=
V_{\rm sh}
+
\nabla\phi,
}
\tag{4.1}
$$

where

$$
\boxed{
\Delta\phi=0.
}
\tag{4.2}
$$

Therefore the diagonal pancake strain

$$
aT
$$

lies entirely in the harmonic part

$$
\nabla^2\phi.
$$

### Proof

Set

$$
H=V-V_{\rm sh}.
$$

Then

$$
\nabla\times H=0
$$

and

$$
\nabla\cdot H=0.
$$

In a simply connected core

$$
H=\nabla\phi.
$$

Then

$$
\Delta\phi=0.
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

# 5. Nonlocal interpretation

In a whole-space finite-energy setting, a globally harmonic gradient field satisfying the relevant decay belongs to the trivial harmonic class.

Thus a nonzero local harmonic affine strain must be generated through data outside the local sheet core.

Equivalently, it is the Taylor jet of a nonlocal velocity contribution.

This reproduces the DCRP-35/36 finite-annulus affine-strain supplier picture from the Gaussian-sheet side.

No claim is made that the nonlocal source is literally an external force.

In the unforced parent it is generated by the rest of the same fluid.

---

# 6. External calibration

Classical Burgers-vortex and viscous-vortex-layer models are formulated in the presence of a prescribed or background straining flow.

Modern vortex-layer literature explicitly interprets the uniform strain as the local potential velocity induced by other vortex structures, often at larger scales.

This is used only as structural calibration.

DCRP-53 proves the local harmonic-supplier decomposition directly.

---

# 7. Gaussian normal profile

Let

$$
f(z,s)
=
\frac1{
\sqrt{
2\pi h^2(s)
}
}
\exp
\left[
-\frac{
(z-\bar z)^2
}{
2h^2(s)
}
\right].
$$

After centering:

$$
\bar z=0.
$$

The DCRP-48 Fokker--Planck equation preserves Gaussianity.

The variance satisfies

$$
\boxed{
(h^2)'
=
2
[
\gamma-2a(s)
]
h^2
+
2\varepsilon(s).
}
\tag{7.1}
$$

---

# 8. Viscosity-scaled variance

Set

$$
\boxed{
\delta(s)
=
h^2(s)/\varepsilon(s),
}
\tag{8.1}
$$

with

$$
\boxed{
\varepsilon'
=
-\lambda\varepsilon,
\qquad
\lambda=1-2\gamma.
}
\tag{8.2}
$$

Then

$$
\begin{aligned}
\delta'
&=
\frac{
(h^2)'
}{
\varepsilon
}
-
\frac{
h^2\varepsilon'
}{
\varepsilon^2
}
\\
&=
2
[
\gamma-2a
]
\delta
+
2
+
\lambda\delta
\\
&=
[
1-4a
]
\delta
+
2.
\end{aligned}
$$

Thus

$$
\boxed{
\delta'
=
[
1-4a
]
\delta
+
2.
}
\tag{8.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 9. NEW THEOREM — Width-to-Strain Reconstruction

## Theorem 9.1

For every positive Gaussian variance trajectory

$$
\delta(s)>0,
$$

the required canonical pancake strain is

$$
\boxed{
a(s)
=
\frac14
+
\frac1{
2\delta(s)
}
-
\frac14
(\log\delta(s))'.
}
\tag{9.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus Gaussian width breathing and affine strain are not independent coordinates.

---

# 10. Periodic reciprocal-variance identity

Assume the root-scaled Gaussian variance is periodic:

$$
\boxed{
\delta(S_0)=\delta(0).
}
\tag{10.1}
$$

Integrate Theorem 9.1.

The logarithmic derivative integrates to zero.

Therefore

$$
\boxed{
\bar a
=
\frac14
+
\frac12
\left\langle
\delta^{-1}
\right\rangle.
}
\tag{10.2}
$$

Since

$$
\bar a
=
(2-3\gamma)/2,
$$

$$
\boxed{
\left\langle
\delta^{-1}
\right\rangle
=
\frac32
(1-2\gamma).
}
\tag{10.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 11. Fisher identity

For a Gaussian probability density of variance

$$
h^2,
$$

$$
\boxed{
I(f)
=
\int
\frac{
|f_z|^2
}{
f
}
dz
=
1/h^2.
}
\tag{11.1}
$$

Thus

$$
\boxed{
\varepsilon I(f)
=
1/\delta.
}
\tag{11.2}
$$

The period identity becomes

$$
\boxed{
\int_0^{S_0}
\varepsilon(s)I(f(s))ds
=
\frac32
(1-2\gamma)S_0.
}
\tag{11.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This is an exact equality signature of the Gaussian branch.

---

# 12. Harmonic mean of the normalized variance

Equation (10.3) says the harmonic mean of

$$
\delta
$$

is fixed:

$$
\boxed{
\delta_{\rm harm}
=
\left\langle
\delta^{-1}
\right\rangle^{-1}
=
\frac{
2
}{
3(1-2\gamma)
}.
}
\tag{12.1}
$$

By Jensen,

$$
\boxed{
\langle\delta\rangle
\ge
\delta_{\rm harm},
}
\tag{12.2}
$$

with equality if and only if

$$
\delta
$$

is constant.

Thus any Gaussian breathing increases the average viscosity-scaled width above the constant-profile minimum.

---

# 13. Orthogonal breathing decomposition

Set

$$
\boxed{
c_\delta
=
\frac32\lambda.
}
\tag{13.1}
$$

Then

$$
\boxed{
a-\bar a
=
\frac12
(
\delta^{-1}-c_\delta
)
-
\frac14
(\log\delta)'.
}
\tag{13.2}
$$

The cross term is

$$
\begin{aligned}
\int
(
\delta^{-1}-c_\delta
)
(\log\delta)'
ds
&=
\int
\frac{
\delta'
}{
\delta^2
}
ds
-
c_\delta
\int
\frac{
\delta'
}{
\delta
}
ds
\\
&=
-
[
\delta^{-1}
]_0^{S_0}
-
c_\delta
[
\log\delta
]_0^{S_0}
\\
&=
0.
\end{aligned}
$$

Therefore

$$
\boxed{
\int
(a-\bar a)^2
=
\frac14
\int
(
\delta^{-1}-c_\delta
)^2
+
\frac1{16}
\int
[
(\log\delta)'
]^2.
}
\tag{13.3}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 14. NEW THEOREM — Gaussian Strain-Action Rigidity

## Theorem 14.1

The pancake strain action satisfies

$$
\boxed{
\int_0^{S_0}
|A_{\rm pan}|_F^2ds
=
\frac32
(2-3\gamma)^2S_0
+
\frac32
\int
\left[
\delta^{-1}
-
\frac32(1-2\gamma)
\right]^2ds
+
\frac38
\int
[
(\log\delta)'
]^2ds.
}
\tag{14.1}
$$

Therefore

$$
\boxed{
\int
|A_{\rm pan}|^2
\ge
\frac32
(2-3\gamma)^2S_0.
}
\tag{14.2}
$$

Equality holds if and only if

$$
\boxed{
\delta(s)
\equiv
\frac{
2
}{
3(1-2\gamma)
}
}
\tag{14.3}
$$

and

$$
\boxed{
a(s)
\equiv
\frac{
2-3\gamma
}{2}.
}
\tag{14.4}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This identifies the minimum-action Gaussian equality.

---

# 15. Reproduction-action consequence

DCRP-36 gives, for a periodic affine jet,

$$
\boxed{
\int_0^{S_0}
|A'+A|^2ds
=
\int
|A'|^2
+
\int
|A|^2.
}
\tag{15.1}
$$

For

$$
A=aT,
$$

$$
\boxed{
\int
|A'+A|^2
=
6
\int
[
(a')^2+a^2
].
}
\tag{15.2}
$$

Hence the universal lower bound is again

$$
\boxed{
\mathcal A_{\rm rep}
\ge
\frac32
(2-3\gamma)^2S_0.
}
\tag{15.3}
$$

Equality requires constant

$$
a
$$

and therefore constant

$$
\delta.
$$

Any Gaussian breathing creates a strictly larger annular affine-jet reproduction action.

---

# 16. Global Gaussian shear energy

Assume

$$
\zeta
$$

is one sign, integrable, and nonzero.

Let

$$
M
=
\int_{\mathbb R}
\zeta dz.
$$

Then

$$
U_z=-\zeta
$$

gives

$$
U(+\infty)-U(-\infty)=-M.
$$

For any additive constant in

$$
U,
$$

$$
\boxed{
\max
\left(
|U(+\infty)|,
|U(-\infty)|
\right)
\ge
|M|/2.
}
\tag{16.1}
$$

Therefore on one normal half-space

$$
|U|
\ge
|M|/4
$$

for sufficiently large

$$
|z|.
$$

A fixed positive fraction of a large ball lies in this region.

Hence

$$
\boxed{
\int_{B_R}
|V_{\rm sh}|^2dy
\ge
cM^2R^3
}
\tag{16.2}
$$

for all sufficiently large

$$
R.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

This alone excludes a global nonzero one-dimensional Gaussian shear from the strict

$$
R^\kappa,
\qquad
\kappa<1
$$

tail class.

---

# 17. Global affine energy

For any trace-free matrix

$$
A,
$$

isotropy of the ball gives

$$
\boxed{
\int_{B_R}
|Ay|^2dy
=
\frac{
4\pi
}{
15
}
|A|_F^2
R^5.
}
\tag{17.1}
$$

For

$$
A=aT,
$$

$$
|A|_F^2=6a^2,
$$

so

$$
\boxed{
\int_{B_R}
|A_{\rm pan}y|^2dy
=
\frac{
8\pi
}{5}
a^2R^5.
}
\tag{17.2}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

Thus a global affine background strain is even farther from the strict sublinear tail class.

---

# 18. NEW THEOREM — Global Gaussian-Affine Tail NO-GO

## Theorem 18.1

A nonzero exact global field of the form

$$
\boxed{
V(y,s)
=
U(z,s)e_2
+
a(s)Ty
}
\tag{18.1}
$$

with nonzero one-sign normal vorticity flux and

$$
\bar a>0
$$

cannot satisfy

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2dyds
\le
C_ER^\kappa
}
\tag{18.2}
$$

for any

$$
\kappa<1.
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The exact Batchelor--Gaussian affine profile is necessarily local.

---

# 19. Cross-term audit

On a centered ball,

$$
A_{\rm pan}y
=
a(y_1,y_2,-2z).
$$

The shear is

$$
U(z)e_2.
$$

Their inner product is

$$
a
y_2
U(z).
$$

For every fixed

$$
z,
$$

the horizontal disk is symmetric in

$$
y_2.
$$

Therefore

$$
\boxed{
\int_{B_R}
(A_{\rm pan}y)
\cdot
V_{\rm sh}
dy
=
0.
}
\tag{19.1}
$$

Thus the affine energy lower bound cannot be hidden by cancellation with the pure shear on the exact centered normal form.

---

# 20. NEW THEOREM — Finite Matching Radius

## Theorem 20.1

Suppose the exact centered Gaussian-affine normal form holds throughout

$$
B_R
$$

for all

$$
s\in[0,S_0],
$$

and the strict tail envelope is

$$
\boxed{
\int_0^{S_0}
\int_{B_R}
|V|^2
\le
C_ER^\kappa.
}
\tag{20.1}
$$

Then

$$
\boxed{
R^{5-\kappa}
\le
\frac{
5C_E
}{
8\pi
\displaystyle
\int_0^{S_0}
a(s)^2ds
}.
}
\tag{20.2}
$$

In particular,

$$
\boxed{
R^{5-\kappa}
\le
\frac{
5C_E
}{
12\pi
(2-3\gamma)^2S_0
}.
}
\tag{20.3}
$$

Status:

$$
\boxed{
\textbf{PROVED UNDER THE EXACT CORE-NORMAL-FORM HYPOTHESIS}.
}
$$

The matching layer is forced at finite normalized radius.

---

# 21. Meaning of the matching layer

Outside the exact Gaussian-affine core, at least one of the following must occur:

1. the harmonic affine field changes;

2. the one-dimensional shear is tangentially localized;

3. the vorticity direction/plane changes;

4. the normal Gaussian profile ceases to be exact;

5. vorticity flux is exchanged with neighboring structures;

6. pressure/PFET supplies the core;

7. the filtered/localized equation acquires a commutator or boundary residual.

Thus the matching layer is not optional geometry.

It is required by the global tail class.

---

# 22. Matching layer and DCRP-35/36

DCRP-35 showed that a nonzero strict rank-two core must have:

- inward enstrophy turnover;
- or a finite-annulus strain supplier.

DCRP-36 encoded the supplier as a harmonic affine jet with a positive reproduction action.

DCRP-53 independently arrives at the same conclusion from the Gaussian viscous core:

$$
\boxed{
\text{the core cannot generate }A_{\rm pan};
\quad
A_{\rm pan}\text{ is harmonic/nonlocal}.
}
$$

Thus the Gaussian equality branch and the earlier annular-strain branch are the same structural object viewed from opposite sides.

---

# 23. Flux-amplitude equation

Return to the ideal closed one-normal-profile vorticity equation:

$$
\partial_s\zeta
+
\sigma z\zeta_z
=
(a-1)\zeta
+
\varepsilon\zeta_{zz}.
$$

Assuming sufficient normal decay, define

$$
M(s)
=
\int
\zeta dz.
$$

Then

$$
\int
z\zeta_z dz
=
-M,
$$

and diffusion integrates to zero.

Hence

$$
\boxed{
M'
=
(a-1+\sigma)M
=
(\gamma-a-1)M.
}
\tag{23.1}
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

---

# 24. One-period source-free flux multiplier

Using

$$
\bar a
=
(2-3\gamma)/2,
$$

$$
\begin{aligned}
\int_0^{S_0}
(
\gamma-a-1
)ds
&=
\left[
\gamma-1
-
\frac{
2-3\gamma
}{2}
\right]
S_0
\\
&=
\frac{
5\gamma-4
}{2}
S_0.
\end{aligned}
$$

Thus

$$
\boxed{
M(S_0)
=
\rho_M M(0),
}
\tag{24.1}
$$

with

$$
\boxed{
\rho_M
=
\exp
\left[
\frac{
5\gamma-4
}{2}
S_0
\right].
}
\tag{24.2}
$$

Since

$$
2/5<\gamma<1/2,
$$

$$
\boxed{
0<\rho_M<1.
}
\tag{24.3}
$$

This is an exact amplitude decay law for the ideal closed one-dimensional sheet.

---

# 25. Critical logical correction

The DCRP-52 Gaussian return theorem concerns the **viscosity-scaled normal probability profile**

$$
f_n/M_n
$$

and its shape distribution.

It does not, by itself, assert

$$
\boxed{
M_{n+1}=M_n.
}
\tag{25.1}
$$

Same-parent re-rooting may include a canonical amplitude multiplier.

Therefore:

$$
\boxed{
\rho_M<1
}
$$

does **not** unconditionally contradict the root-to-root Gaussian-shape branch.

Status:

$$
\boxed{
\textbf{CORRECTION / NO OVERCLAIM}.
}
$$

A source conclusion requires a declared amplitude recurrence or another invariant fixing the relevant flux mass.

---

# 26. Conditional flux-replenishment theorem

Consider

$$
\boxed{
M'
=
b(s)M
+
J(s),
\qquad
b(s)=\gamma-a(s)-1.
}
\tag{26.1}
$$

Then

$$
\boxed{
M(S_0)
=
\rho_M M(0)
+
\int_0^{S_0}
\exp
\left[
\int_\tau^{S_0}
b(s)ds
\right]
J(\tau)d\tau.
}
\tag{26.2}
$$

If

$$
\boxed{
M(S_0)=M(0)=M_0>0,
}
\tag{26.3}
$$

then

$$
\boxed{
\int_0^{S_0}
\exp
\left[
\int_\tau^{S_0}
b(s)ds
\right]
J(\tau)d\tau
=
(1-\rho_M)M_0
>0.
}
\tag{26.4}
$$

Status:

$$
\boxed{
\textbf{PROVED CONDITIONAL ON FLUX-AMPLITUDE RECURRENCE}.
}
$$

This is a quantitative matching-layer replenishment gap.

---

# 27. Where the source can live

Inside the exact one-dimensional Gaussian core, the ideal normal equation has no tangential source.

Therefore any nonzero

$$
J
$$

must arise from leaving that exact core model through:

- tangential transport;
- annular matching;
- localization boundary;
- rank/plane exchange;
- multiple-sheet interaction.

Because the exact Gaussian-affine region has a finite matching radius, such source activity cannot be hidden solely at normalized infinity.

This statement is conditional on the amplitude-recurrence branch.

---

# 28. Minimum Gaussian equality

If the strain reproduction excess vanishes, then:

$$
a(s)\equiv\bar a,
$$

and:

$$
\delta(s)\equiv\delta_0.
$$

The normal Fokker--Planck equation in viscosity-scaled variables is then an autonomous Ornstein--Uhlenbeck equation.

Its unique recurrent probability profile is the Gaussian already identified in DCRP-52.

Thus the minimum equality state is:

$$
\boxed{
\textbf{
constant-strain Ornstein--Uhlenbeck Gaussian sheet core}.
}
\tag{28.1}
$$

---

# 29. Constant-strain parameters

Let

$$
\lambda
=
1-2\gamma.
$$

Then

$$
\boxed{
a_0
=
\bar a
=
\frac{
1+3\lambda
}{4}
=
\frac{
2-3\gamma
}{2}.
}
\tag{29.1}
$$

The viscosity-scaled variance is

$$
\boxed{
\delta_0
=
\frac{
2
}{
3\lambda
}.
}
\tag{29.2}
$$

The normal similarity-material drift is

$$
\boxed{
\sigma_0
=
\gamma-2a_0
=
-2\lambda.
}
\tag{29.3}
$$

Thus the normal drift is strictly compressive.

---

# 30. Explicit one-period diffusion coefficient in the minimum branch

For constant

$$
\sigma_0=-2\lambda,
$$

the DCRP-48 coefficient is

$$
\begin{aligned}
\mathfrak D_{\rm nor}
&=
2
\int_0^{S_0}
e^{-\lambda\tau}
e^{-4\lambda(S_0-\tau)}
d\tau
\\
&=
\frac{
2
}{
3\lambda
}
\left(
e^{-\lambda S_0}
-
e^{-4\lambda S_0}
\right).
\end{aligned}
$$

With

$$
\mu=e^{\lambda S_0},
$$

$$
\boxed{
\mathfrak D_{\rm nor}
=
\frac{
2
}{
3\lambda
}
(
\mu^{-1}
-
\mu^{-4}
).
}
\tag{30.1}
$$

Then

$$
\boxed{
\frac{
\mu\mathfrak D_{\rm nor}
}{
1-\mu^{-3}
}
=
\frac{
2
}{
3\lambda
}
=
\delta_0.
}
\tag{30.2}
$$

Thus the constant-strain and Gaussian-return calculations agree exactly.

---

# 31. Strongest coherent equality state after DCRP-53

The surviving minimum-action coherent branch is:

$$
\boxed{
\textbf{
local constant-strain Batchelor--Gaussian sheet}
}
$$

with:

$$
\boxed{
a_0
=
\frac{
2-3\gamma
}{2},
\qquad
\delta_0
=
\frac{
2
}{
3(1-2\gamma)
}.
}
$$

It is not global.

It must be coupled to:

$$
\boxed{
\textbf{
a finite normalized matching annulus}
}
$$

which supplies the harmonic strain and localizes the shear.

If flux-amplitude recurrence is also imposed, the same open system must supply a definite vorticity-flux amount.

---

# 32. Why this is narrower than a Burgers/Townsend analogy

Classical strained viscous vortices/layers assume or model a background linear strain.

DCRP-53 does not import that strain.

It proves that on the strict unforced same-parent branch:

1. the local Gaussian core cannot create the needed diagonal strain itself;

2. the background strain must be generated by the rest of the same solution;

3. the strict tail forces that strain and the shear to match back to the ambient flow at finite normalized radius.

Thus the background strain has been converted from an imposed datum into an internal finite-annulus reproduction problem.

---

# 33. Mandatory finite-annulus open-system picture

The final equality architecture is therefore:

$$
\boxed{
\text{finite Gaussian core}
}
\longleftrightarrow
\boxed{
\text{finite matching annulus}
}
\longleftrightarrow
\boxed{
\text{outer recurrent flow}.
}
$$

The annulus must mediate at least:

- harmonic strain input to the core;
- departure from globally infinite-energy affine/shear behavior;
- the DCRP-31 PFET matching current;
- any required flux-amplitude replenishment.

This is a much more constrained object than an isolated Gaussian sheet.

---

# 34. What DCRP-53 closes

The following candidate equality is removed:

$$
\boxed{
\textbf{
self-contained global Gaussian sheet maintained by its own strain}.
}
}
$$

It fails twice:

1. the self-induced one-dimensional sheet strain has zero pancake-diagonal projection;

2. the global Gaussian shear/affine velocity violates the strict sublinear kinetic-energy tail.

The following equality is also minimized:

$$
\boxed{
\textbf{
arbitrarily breathing Gaussian width + arbitrary strain waveform}.
}
}
$$

The width uniquely determines the strain, and breathing adds a strictly positive harmonic-strain action.

The minimum branch has constant normalized width and constant strain.

---

# 35. What remains open

The finite matching annulus may in principle self-consistently generate:

- the harmonic affine strain;
- tangential localization;
- vorticity-flux exchange;
- PFET;
- pressure;
- return geometry.

DCRP-53 does not prove this is impossible.

The final task is to couple those duties quantitatively.

In particular, it remains open whether one finite annulus can satisfy all of them with zero normalized surplus and zero transition defect.

---

# 36. Correct next frontier

The next target is:

$$
\boxed{
\textbf{
Finite Matching Annulus /
Coupled Strain--Vorticity-Flux Reproduction.
}
}
$$

A useful theorem would derive a single annular ledger containing simultaneously:

1. the harmonic affine-strain coefficient:

   $$
   a(s);
   $$

2. the Gaussian-core strain demand reconstructed from:

   $$
   \delta(s);
   $$

3. the DCRP-31 inward PFET;

4. tangential localization of the one-dimensional shear;

5. conditional or invariant vorticity-flux replenishment;

6. annular kinetic-energy / vorticity / commutator cost.

The desired closure is:

$$
\boxed{
\textbf{
finite Gaussian core recurrence}
\Longrightarrow
\textbf{
positive annular turnover/supplier defect}
}
$$

in a quotient-safe parent coordinate.

That is now the sharpest coherent viscous equality problem.

---

# 37. Source-status audit

The primary viscous-vortex-layer literature treats Gaussian/Townsend-type layers under spatially uniform strain and explicitly interprets such strain as a local potential flow induced by other, often larger-scale, vortex structures.

That literature also shows that in some uniform-strain regimes nonzero steady vorticity layers require boundary vorticity supply.

These results calibrate, but do not prove, the DCRP-53 matching-layer conclusions.

The harmonic-supplier theorem, width-to-strain reconstruction, strain-action decomposition, global tail no-go, and finite matching-radius theorem are derived directly in this document.

---

# 38. End state

The one-dimensional Gaussian sheet self-field is

$$
\boxed{
V_{\rm sh}=U(z)e_2,
}
$$

with strain orthogonal to

$$
\boxed{
T=\operatorname{diag}(1,1,-2).
}
$$

Thus the required pancake strain is harmonic/nonlocal.

The Gaussian viscosity-scaled variance obeys

$$
\boxed{
\delta'
=
(1-4a)\delta+2,
}
$$

so

$$
\boxed{
a
=
\frac14
+
\frac1{2\delta}
-
\frac14(\log\delta)'.
}
$$

Periodicity gives

$$
\boxed{
\left\langle
\delta^{-1}
\right\rangle
=
\frac32(1-2\gamma).
}
$$

The Gaussian Fisher action is therefore exactly

$$
\boxed{
\int_0^{S_0}
\varepsilon I(f)
=
\frac32(1-2\gamma)S_0.
}
$$

The strain action decomposes as

$$
\boxed{
\int|A_{\rm pan}|^2
=
\frac32(2-3\gamma)^2S_0
+
\frac32
\int
\left[
\delta^{-1}
-
\frac32(1-2\gamma)
\right]^2
+
\frac38
\int
[
(\log\delta)'
]^2.
}
$$

Hence the minimum equality has

$$
\boxed{
a(s)
\equiv
\frac{
2-3\gamma
}{2},
\qquad
\delta(s)
\equiv
\frac{
2
}{
3(1-2\gamma)
}.
}
$$

Neither its affine field nor its one-dimensional Gaussian shear can extend globally under the strict

$$
R^\kappa,
\qquad
\kappa<1
$$

tail.

Therefore the strongest coherent zero-excess viscous survivor is:

$$
\boxed{
\textbf{
a local constant-strain Batchelor--Gaussian sheet coupled to a finite normalized matching annulus.
}
}
$$

The next frontier is:

$$
\boxed{
\textbf{
Finite Matching Annulus /
Coupled Strain--Vorticity-Flux Reproduction.
}
}
$$