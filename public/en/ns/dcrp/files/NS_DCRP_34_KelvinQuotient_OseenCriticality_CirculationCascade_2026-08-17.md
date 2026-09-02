# NS-DCRP-34 — Quotient-Corrected Kelvin Number, Coarse Circulation Cascade, and the Critical Kelvin–Oseen Equality Manifold

- date: 2026-08-17
- status: research proof checkpoint / correction-and-reduction round
- canonical source: UTF-8 Markdown
- canonical math delimiters: `$...$` and `$$...$$`
- objective:
  1. audit the DCRP-32/33 interpretation of DSS circulation contraction as a native return tax;
  2. identify the quotient-correct circulation variable under the same-parent Type-II normalization;
  3. show that strict DSS circulation contraction, transverse-area contraction, and effective-viscosity scaling are exactly critical;
  4. derive the coarse-grained Kelvin balance and separate SGS circulation cascade from molecular viscosity;
  5. prove fixed-filter viscous vanishing and classify any nonuniform small-scale Kelvin defect;
  6. define the corrected Kelvin/Oseen equality manifold;
  7. recalibrate the remaining obstruction against rigorous Oseen/vortex-filament and Burgers-vortex theory.
- no full Navier--Stokes regularity claim is made.
- principal external primary sources:
  - G. L. Eyink, *The Cascade of Circulations in Fluid Turbulence*, arXiv:physics/0606159;
  - J. Bedrossian, P. Germain, B. Harrop-Griffiths, *Vortex filament solutions of the Navier--Stokes equations*, arXiv:1809.04109;
  - T. Gallay, C. E. Wayne, *Existence and stability of asymmetric Burgers vortices*, arXiv:math/0503353;
  - P. Constantin, M. Ignatova, V. Vicol, *On putative self-similarity for incompressible 3D Euler*, arXiv:2602.17570v3.
- internal dependencies:
  - DCRP-30 same-parent DSS scaling;
  - DCRP-31 radial PFET matching layer;
  - DCRP-32 Kelvin holonomy;
  - DCRP-33 replenishment / filamentation / direct Navier--Stokes Kelvin correction.
- no novelty/priority claim is made without independent audit.

---

# 1. Executive correction

DCRP-32 introduced the strict-DSS similarity circulation contraction

$$
\boxed{
\Gamma_{ss}(s+S_0)
=
\rho_\Gamma
\Gamma_{ss}(s),
}
\tag{1.1}
$$

where

$$
\boxed{
\rho_\Gamma
=
e^{-(1-2\gamma)S_0}
\in(0,1)
}
\tag{1.2}
$$

for

$$
\boxed{
\frac25<\gamma<\frac12.
}
\tag{1.3}
$$

DCRP-32/33 then treated the raw difference

$$
\Gamma_{ss}(s+S_0)-\Gamma_{ss}(s)
$$

as a candidate material-holonomy return residual.

That interpretation is **too strong** after the full same-parent normalization is taken into account.

Let

$$
a_n
$$

be the Type-II amplitude normalization and

$$
\boxed{
\mu
=
\frac{a_{n+1}}{a_n}.
}
\tag{1.4}
$$

For an exact strict same-parent DSS return,

$$
\boxed{
\mu
=
e^{(1-2\gamma)S_0}
=
\rho_\Gamma^{-1}.
}
\tag{1.5}
$$

The effective viscosity of the normalized Type-II equation is

$$
\boxed{
\varepsilon_n
=
\frac{\nu}{a_n}.
}
\tag{1.6}
$$

Therefore

$$
\boxed{
\frac{\varepsilon_{n+1}}{\varepsilon_n}
=
\frac1\mu
=
\rho_\Gamma.
}
\tag{1.7}
$$

For a same physical material loop,

$$
\boxed{
\Gamma_n^{norm}
=
\frac{\Gamma^{phys}}{a_n}.
}
\tag{1.8}
$$

Hence

$$
\boxed{
\frac{\Gamma_n^{norm}}{\varepsilon_n}
=
\frac{\Gamma^{phys}}{\nu}.
}
\tag{1.9}
$$

Thus the **quotient-correct Kelvin number**

$$
\boxed{
\mathscr K_\Gamma
=
\frac{\Gamma^{norm}}{\varepsilon_{\rm eff}}
}
\tag{1.10}
$$

is invariant under the canonical Type-II amplitude re-root whenever the physical circulation is unchanged.

The strict similarity circulation contraction and the effective-viscosity contraction have the **same factor**.

Therefore:

$$
\boxed{
\textbf{
raw similarity circulation contraction is canonical scaling,
not by itself a native return tax.
}
}
\tag{1.11}
$$

This is the principal correction of DCRP-34.

The valid native quantities are instead:

1. a change in the quotient-correct quantity:

   $$
   \mathscr K_\Gamma;
   $$

2. an anomalous circulation cascade across unresolved scales;

3. a material/scale/loop transition defect;

4. a deviation from the critical strain--diffusion matching described below.

---

# 2. Four equal strict-DSS scaling factors

The strict same-parent DSS branch has a remarkable equality of four multipliers.

Let

$$
\boxed{
\rho
=
e^{-(1-2\gamma)S_0}.
}
\tag{2.1}
$$

Then:

### similarity circulation

$$
\boxed{
\Gamma_{ss}(s+S_0)
=
\rho
\Gamma_{ss}(s).
}
\tag{2.2}
$$

### effective viscosity

$$
\boxed{
\varepsilon_{n+1}
=
\rho
\varepsilon_n.
}
\tag{2.3}
$$

### amplitude normalization

$$
\boxed{
a_{n+1}
=
\rho^{-1}
a_n.
}
\tag{2.4}
$$

### periodic-vortex transverse area

For a periodic material vortex point, DCRP-33 gives

$$
\boxed{
\det
D\Phi^m|_{\perp}
=
\rho^m.
}
\tag{2.5}
$$

Thus, per DSS period,

$$
\boxed{
\rho_\Gamma
=
\rho_\nu
=
\rho_\perp
=
\rho.
}
\tag{2.6}
$$

This is an exact critical scaling coincidence.

---

# 3. Critical transverse viscous scale

The normalized Type-II viscous diffusion length over an order-one normalized time is

$$
\boxed{
\ell_{\nu,n}
\sim
\sqrt{\varepsilon_n}.
}
\tag{3.1}
$$

Its transverse **area** scale is

$$
\boxed{
A_{\nu,n}
\sim
\varepsilon_n.
}
\tag{3.2}
$$

Across one strict DSS return:

$$
\boxed{
\frac{
A_{\nu,n+1}
}{
A_{\nu,n}
}
=
\rho.
}
\tag{3.3}
$$

At a periodic material vortex point the transverse material-area product has exactly the same multiplier:

$$
\boxed{
\frac{
A_{\perp,n+1}
}{
A_{\perp,n}
}
=
\rho.
}
\tag{3.4}
$$

Therefore the ratio

$$
\boxed{
\mathscr A_\nu
=
\frac{
A_\perp
}{
\varepsilon_{\rm eff}
}
}
\tag{3.5}
$$

is return-invariant in the exact periodic-vortex equality geometry.

This is the first precise form of the **critical strain--diffusion balance**.

---

# 4. Kelvin Reynolds number

Define the circulation Reynolds number of a same physical loop:

$$
\boxed{
\mathrm{Re}_\Gamma
=
\frac{
|\Gamma^{phys}|
}{
\nu
}.
}
\tag{4.1}
$$

In normalized Type-II variables:

$$
\boxed{
\mathrm{Re}_\Gamma
=
\frac{
|\Gamma^{norm}|
}{
\varepsilon_{\rm eff}
}.
}
\tag{4.2}
$$

Thus the quotient-correct Kelvin number is simply the physical circulation Reynolds number.

If physical Kelvin circulation is approximately preserved during the Type-II return, then

$$
\boxed{
\mathrm{Re}_\Gamma
}
$$

is automatically return-neutral.

Hence neither:

$$
\Gamma^{norm}\to\rho\Gamma^{norm}
$$

nor:

$$
\varepsilon\to\rho\varepsilon
$$

is independently a defect.

---

# 5. Kelvin-holonomy correction

The DCRP-32 raw holonomy functional was

$$
\boxed{
\mathcal H_\Gamma^{raw}(C)
=
\left|
\Gamma(
\Phi(C)
)
-
\Gamma(C)
\right|.
}
\tag{5.1}
$$

In a strict DSS equality state:

$$
\mathcal H_\Gamma^{raw}
=
(1-\rho)
|\Gamma(C)|.
$$

This is positive even when the physical circulation of the same material loop is **exactly conserved**.

Therefore:

$$
\boxed{
\mathcal H_\Gamma^{raw}
}
$$

is not invariant under the full Type-II return normalization.

It must not be inserted into:

$$
\mathsf R_{\rm nat}
$$

as a positive cost without quotient correction.

Status:

$$
\boxed{
\textbf{CORRECTION TO DCRP-32/33}.
}
$$

---

# 6. Quotient-correct Kelvin residual

For two same-parent roots linked by the same material loop define:

$$
\boxed{
\mathcal R_\Gamma^{q}
=
\left|
\frac{
\Gamma_{n+1}^{norm}
}{
\varepsilon_{n+1}
}
-
\frac{
\Gamma_n^{norm}
}{
\varepsilon_n
}
\right|.
}
\tag{6.1}
$$

Using (1.9):

$$
\boxed{
\mathcal R_\Gamma^{q}
=
\frac1\nu
\left|
\Gamma_{phys}(t_{n+1})
-
\Gamma_{phys}(t_n)
\right|.
}
\tag{6.2}
$$

This is normalization invariant.

For smooth Navier--Stokes material loops the physical Kelvin balance gives

$$
\boxed{
\mathcal R_\Gamma^{q}
=
\left|
\int_{t_n}^{t_{n+1}}
\oint_{C(t)}
\Delta U(x,t)\cdot dx
dt
\right|.
}
\tag{6.3}
$$

The viscosity coefficient cancels because the circulation has been divided by:

$$
\nu.
$$

Thus a nonzero quotient-correct Kelvin residual is a genuine second-order viscous effect.

It is not automatically small in the Type-II limit.

---

# 7. Why direct one-dimensional Kelvin control is too sharp

The quantity

$$
\oint_C
\Delta U\cdot dx
$$

restricts a second derivative of the velocity to a one-dimensional moving curve.

Ordinary:

$$
L^2
$$

energy and:

$$
H^1
$$

dissipation do not directly control this trace.

Therefore DCRP-33's direct second-order residue is legitimate as a formal exact quantity but is **not** the preferred compactness bridge.

The safer bridge is coarse-grained circulation.

---

# 8. Coarse-grained Navier--Stokes equation

Let:

$$
U_{n,\ell}
=
G_\ell*v_n,
$$

and define the SGS stress:

$$
\boxed{
R_{n,\ell}
=
G_\ell*
(
v_n\otimes v_n
)
-
U_{n,\ell}
\otimes
U_{n,\ell}.
}
\tag{8.1}
$$

The filtered Type-II Navier--Stokes equation is

$$
\boxed{
\partial_\tau U_{n,\ell}
+
(
U_{n,\ell}\cdot\nabla
)
U_{n,\ell}
+
\nabla P_{n,\ell}
=
f_{n,\ell}
+
\varepsilon_n
\Delta U_{n,\ell},
}
\tag{8.2}
$$

where:

$$
\boxed{
f_{n,\ell}
=
-\nabla\cdot
R_{n,\ell}.
}
\tag{8.3}
$$

This is the standard coarse-grained equation.

---

# 9. Exact coarse Kelvin balance

Let:

$$
C_{n,\ell}(\tau)
$$

be a closed loop advected by:

$$
U_{n,\ell}.
$$

Define:

$$
\boxed{
\Gamma_{n,\ell}(\tau)
=
\oint_{
C_{n,\ell}(\tau)
}
U_{n,\ell}\cdot dy.
}
\tag{9.1}
$$

Then:

$$
\boxed{
\frac d{d\tau}
\Gamma_{n,\ell}
=
\oint_{
C_{n,\ell}(\tau)
}
\left[
f_{n,\ell}
+
\varepsilon_n
\Delta U_{n,\ell}
\right]
\cdot dy.
}
\tag{9.2}
$$

Status:

$$
\boxed{
\textbf{EXACT / STANDARD COARSE KELVIN BALANCE}.
}
$$

This is precisely the large-scale circulation balance emphasized by Eyink.

---

# 10. Circulation flux

Define the SGS circulation flux:

$$
\boxed{
K_{n,\ell}(C,\tau)
=
-
\oint_{
C_{n,\ell}(\tau)
}
f_{n,\ell}\cdot dy.
}
\tag{10.1}
$$

Then:

$$
\boxed{
\frac d{d\tau}
\Gamma_{n,\ell}
=
-
K_{n,\ell}
+
\varepsilon_n
\oint
\Delta U_{n,\ell}\cdot dy.
}
\tag{10.2}
$$

This is the circulation analogue of the energy SGS flux.

The SGS force is generated entirely by actual velocity increments.

---

# 11. NEW THEOREM — Fixed-Filter Viscous Vanishing

## Theorem 11.1

Fix:

$$
\ell>0,
$$

a compact loop-tube region:

$$
K,
$$

and a finite normalized time interval:

$$
I.
$$

Assume:

$$
\boxed{
\sup_n
\|v_n\|_{
L^\infty(
I;
L^2(
K_{2\ell}
)
)
}
\le
M,
}
\tag{11.1}
$$

and:

$$
\boxed{
\sup_{n,\tau}
\operatorname{Length}
(
C_{n,\ell}(\tau)
)
\le
L_\ast.
}
\tag{11.2}
$$

Then:

$$
\boxed{
\left|
\varepsilon_n
\int_I
\oint_{
C_{n,\ell}(\tau)
}
\Delta U_{n,\ell}\cdot dy
d\tau
\right|
\le
C
\varepsilon_n
\ell^{-7/2}
M
L_\ast
|I|.
}
\tag{11.3}
$$

Consequently:

$$
\boxed{
\varepsilon_n
\int_I
\oint
\Delta U_{n,\ell}\cdot dy
d\tau
\to0
}
\tag{11.4}
$$

for every fixed:

$$
\ell>0.
$$

### Proof

For a compactly supported smooth filter:

$$
\|\Delta G_\ell\|_2
=
C
\ell^{-7/2}.
$$

By Young/Cauchy--Schwarz:

$$
\boxed{
\|\Delta U_{n,\ell}\|_{
L^\infty(K)
}
\le
C
\ell^{-7/2}
\|v_n\|_{
L^2(K_{2\ell})
}.
}
\tag{11.5}
$$

Integrate along the loop and then in time.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED}.
}
$$

The exponent:

$$
7/2
$$

is a crude fixed-filter estimate, not claimed optimal.

---

# 12. Interpretation

At every fixed positive coarse scale:

$$
\boxed{
\textbf{
Type-II molecular viscosity disappears from the circulation balance.
}
}
\tag{12.1}
$$

Thus the large-scale circulation dynamics are controlled by:

$$
\boxed{
\textbf{
SGS circulation flux}
}
$$

plus the deterministic similarity/return normalization.

This is exactly the inertial-range picture emphasized in coarse-grained Kelvin theory.

---

# 13. Fixed-filter compact shadowing

Assume a strict no-defect branch with:

$$
v_n\to v
$$

strongly in local:

$$
L^2.
$$

Then for every fixed:

$$
\ell>0,
$$

convolution gives:

$$
\boxed{
U_{n,\ell}
\to
U_\ell
}
\tag{13.1}
$$

in local:

$$
C^k
$$

for every finite:

$$
k,
$$

after shrinking the core away from the filter boundary.

Also:

$$
v_n\otimes v_n
\to
v\otimes v
$$

strongly in local:

$$
L^1,
$$

so:

$$
\boxed{
R_{n,\ell}
\to
R_\ell
}
\tag{13.2}
$$

smoothly after filtering.

Therefore the coarse flow maps and loop circulations converge on every finite interval.

The coarse Kelvin balance shadows to the Euler profile at fixed filter scale without requiring a direct trace bound on:

$$
\Delta v_n.
$$

Status:

$$
\boxed{
\textbf{PROVED under the stated strong local compactness}.
}
$$

---

# 14. Smooth Euler small-filter limit

If the limiting Euler/DSS profile is smooth on the loop tube, then:

$$
\boxed{
R_\ell
\to0
}
\tag{14.1}
$$

in:

$$
C^1
$$

as:

$$
\ell\downarrow0.
$$

Hence:

$$
\boxed{
K_\ell(C,\tau)
\to0.
}
\tag{14.2}
$$

The filtered flow maps converge to the true Euler material flow.

Thus the ordinary Euler Kelvin law is recovered by the ordered limit:

$$
\boxed{
n\to\infty
\quad\text{first},
\qquad
\ell\downarrow0
\quad\text{second}.
}
\tag{14.3}
$$

This bypasses the raw:

$$
\Delta v_n
$$

loop trace.

---

# 15. Circulation-cascade defect

The ordered limits need not commute on a weak/noncompact branch.

Define a completed circulation-cascade coordinate schematically by

$$
\boxed{
\mathfrak D_{\rm circ}
=
\limsup_{
\ell\downarrow0
}
\limsup_{
n\to\infty
}
\left|
\int_I
K_{n,\ell}
d\tau
\right|.
}
\tag{15.1}
$$

A complete implementation should include:

- the declared loop family;
- moving-center/loop gauges;
- scale-localization;
- endpoint loop mismatch.

If:

$$
\boxed{
\mathfrak D_{\rm circ}>0,
}
\tag{15.2}
$$

the Type-II branch retains a genuine circulation-cascade / vortex-line transport defect.

If:

$$
\boxed{
\mathfrak D_{\rm circ}=0,
}
\tag{15.3}
$$

and loop compactness holds, the Euler Kelvin theorem is shadowed through the coarse-grained bridge.

---

# 16. Increment representation of the SGS force

The coarse SGS force admits an exact velocity-increment representation of the schematic form

$$
\boxed{
f_{\ell}
=
O
\left(
\frac{
\delta v(\ell)^2
}{
\ell
}
\right).
}
\tag{16.1}
$$

More precisely, it is a filter-gradient average of quadratic velocity increments.

Therefore for a velocity field with local Holder regularity:

$$
|\delta v(r)|
\lesssim
r^h,
$$

$$
\boxed{
|f_\ell|
\lesssim
\ell^{2h-1}.
}
\tag{16.2}
$$

For finite-length loops:

$$
\boxed{
h>1/2
\Longrightarrow
K_\ell\to0.
}
\tag{16.3}
$$

This is the circulation analogue of Onsager's regularity threshold.

Status:

$$
\boxed{
\textbf{EXTERNAL EYINK CALIBRATION}.
}
$$

---

# 17. Meaning for the DCRP defect package

A nonzero small-scale circulation defect requires at least one of:

$$
\boxed{
\text{velocity roughness at or below the Kelvin threshold}
}
$$

or:

$$
\boxed{
\text{unbounded/fractal loop geometry}
}
$$

or:

$$
\boxed{
\text{nonuniform scale concentration}.
}
$$

All are genuine compactness/transition coordinates.

Thus the direct second-order viscous line trace is not the only way to represent failure of Kelvin shadowing.

---

# 18. Reclassification of the DCRP-33 viscous Kelvin residue

DCRP-33 defined

$$
\mathfrak K_n^{visc}
=
\varepsilon_n
\int
\oint
\Delta v_n\cdot dy.
$$

The exact quantity remains valid for the smooth prelimit.

However DCRP-34 changes its logical role.

At every fixed coarse scale:

$$
\boxed{
\mathfrak K_{n,\ell}^{visc}\to0.
}
\tag{18.1}
$$

Therefore any nonzero direct Kelvin viscosity which survives the Type-II limit must be concentrated at:

$$
\boxed{
\ell_n\downarrow0.
}
\tag{18.2}
$$

It is therefore a **microviscous circulation concentration**, not a large-scale return residual.

It should be retained together with:

- circulation cascade;
- tube/loop concentration;
- second-order viscous concentration;

rather than being assumed to be the unique bridge obstruction.

Status:

$$
\boxed{
\textbf{CORRECTION / RECLASSIFICATION}.
}
$$

---

# 19. A crude Kelvin dissipation-scale bound

Under the assumptions of Theorem 11.1, if a coarse viscous circulation correction obeys

$$
\boxed{
\left|
\varepsilon_n
\int_I
\oint
\Delta U_{n,\ell_n}\cdot dy
d\tau
\right|
\ge
c_0>0,
}
\tag{19.1}
$$

then:

$$
\boxed{
\ell_n
\le
C
\varepsilon_n^{2/7}.
}
\tag{19.2}
$$

up to fixed powers of:

$$
M,
L_\ast,
|I|,
c_0.
$$

### Proof

Use (11.3):

$$
c_0
\le
C
\varepsilon_n
\ell_n^{-7/2}.
$$

Rearrange.

$$
\square
$$

Status:

$$
\boxed{
\textbf{PROVED AS A CRUDE NONOPTIMAL CONCENTRATION SCALE}.
}
$$

Thus a genuinely nonzero molecular Kelvin residue is forced into a vanishing transverse scale.

---

# 20. Critical Kelvin--Oseen equality manifold

The strict compact strong branch may now be organized correctly.

Assume:

- no circulation-cascade defect:

  $$
  \mathfrak D_{\rm circ}=0;
  $$

- no loop/scale/transition defect;

- no quotient-correct physical circulation change:

  $$
  \mathcal R_\Gamma^q=0;
  $$

- same-parent strict DSS scaling.

Then:

$$
\boxed{
\frac{
\Gamma^{norm}
}{
\varepsilon
}
=
\text{constant},
}
\tag{20.1}
$$

and at a periodic material vortex point:

$$
\boxed{
\frac{
A_\perp
}{
\varepsilon
}
=
\text{constant}.
}
\tag{20.2}
$$

This is the:

$$
\boxed{
\textbf{
Critical Kelvin--Oseen Equality Manifold}.
}
\tag{20.3}
$$

The circulation strength, transverse core area, and viscosity all renormalize at exactly the same rate.

No return tax has yet been produced inside this equality manifold.

---

# 21. Why this equality manifold is plausible

The mathematical Navier--Stokes literature contains genuine viscous vortex structures whose core width is set by diffusion and whose circulation remains a distinguished parameter.

Examples include:

- the self-similar Oseen vortex and three-dimensional Oseen vortex column;
- large self-similar three-dimensional vortex-filament solutions near Oseen columns;
- Burgers vortices in which axial strain concentrates vorticity while transverse viscosity diffuses it.

Therefore:

$$
\boxed{
\textbf{
strain concentration}
+
\textbf{
viscous diffusion}
+
\textbf{
persistent circulation}
}
$$

is a legitimate Navier--Stokes balance mechanism.

DCRP-34 does **not** identify the Type-II survivor with a Burgers or Oseen vortex.

It uses those rigorous examples as a NO-GO against declaring the local critical balance impossible by geometry alone.

---

# 22. Vortex-filament calibration

Bedrossian--Germain--Harrop-Griffiths construct three-dimensional Navier--Stokes solutions with vortex-filament initial data of arbitrary circulation.

Their theory includes:

- perturbations of the Oseen vortex column in scaling-critical spaces;
- locally approximately self-similar curved filaments.

Thus a concentration of vorticity into a thin viscous filament is mathematically meaningful and can survive within Navier--Stokes dynamics.

The remaining DCRP problem must use the **same-parent blowup/return constraints**, not merely the existence of a thin vortex core.

---

# 23. Burgers-vortex calibration

Burgers vortices are stationary three-dimensional Navier--Stokes vortices in a background straining flow.

The key balance is:

$$
\boxed{
\text{vortex stretching}
\sim
\text{viscous transverse diffusion}.
}
\tag{23.1}
$$

Rigorous existence/stability theory persists even under asymmetric strain.

Therefore the DCRP equality:

$$
A_\perp/\varepsilon
=
\text{constant}
$$

has a familiar viscous-vortex analogue.

The decisive difference is that the DCRP parent is:

- unforced;
- globally finite-energy before the singular time;
- same-parent recurrent;
- coupled to the mandatory DCRP-31 inward PFET tail.

Those extra constraints must do the exclusion work.

---

# 24. DCRP-31 survives the Kelvin correction

The correction to raw Kelvin holonomy does **not** affect DCRP-31.

Every nonzero smooth strict DSS state still satisfies a finite-radius inward PFET matching-layer gap:

$$
\boxed{
\mathsf O_{\rm PFET}^{rad}>0.
}
\tag{24.1}
$$

Thus the strongest corrected strict state is:

$$
\boxed{
\textbf{
PFET-active}
+
\textbf{
Kelvin--Oseen critically balanced}
+
\textbf{
tail-fed DSS}.
}
\tag{24.2}
$$

This is more accurate than:

$$
\text{PFET-active}
+
\text{positive raw holonomy tax}.
$$

---

# 25. Corrected role of material filamentation

DCRP-33 proved that backward ancestors of a nonzero similarity-circulation loop must:

- escape to the material tail; or
- filament exponentially in a compact core.

That geometric theorem remains correct.

What changes is its interpretation.

The filamentation is required by the canonical DSS material scaling and Kelvin conservation.

It is **not by itself** a positive native tax.

A native tax requires an additional failure such as:

- excess filamentation beyond the canonical DSS factor;
- loss of loop compactness;
- circulation cascade across unresolved scales;
- genuine physical circulation change;
- failure of the strain--diffusion equality.

---

# 26. Corrected material residual

A suitable material residual should compare the observed return against the **canonical DSS material map**, not against the identity map.

Symbolically:

$$
\boxed{
\mathsf R_{\rm mat}^{q}
=
d
\left(
\mathsf T_{\rm actual},
\mathsf T_{\rm DSS}^{canonical}
\right).
}
\tag{26.1}
$$

Likewise the circulation residual should compare:

$$
\boxed{
\Gamma_{n+1}^{norm}
}
$$

against:

$$
\boxed{
\rho
\Gamma_n^{norm},
}
$$

or equivalently compare:

$$
\Gamma/\varepsilon.
$$

Therefore:

$$
\boxed{
\mathsf R_{\rm hol}^{raw}
}
$$

from DCRP-32 should be replaced in the canonical ledger by a quotient-corrected residual.

---

# 27. Corrected strict Type-II branch tree

The strict compact same-parent Type-II branch now has the alternatives:

$$
\boxed{
\begin{aligned}
&
\text{transition-parameter escape}
\\
&\vee
\text{Euler--Reynolds / trace defect}
\\
&\vee
\text{circulation-cascade defect}
\\
&\vee
\text{microviscous Kelvin concentration}
\\
&\vee
\text{quotient-correct material/Kelvin residual}
\\
&\vee
\text{Critical Kelvin--Oseen Equality}.
\end{aligned}
}
\tag{27.1}
$$

Inside the final equality branch, DCRP-31 still forces:

$$
\boxed{
\text{nonzero inward PFET}.
}
\tag{27.2}
$$

Thus the final strict state is not silent.

It is a critically balanced viscous-vortex recurrence fed by a pressure--kinetic matching layer.

---

# 28. Equality-manifold scaling identity

The exact strict return factors are:

$$
\boxed{
\mu
=
e^{(1-2\gamma)S_0},
}
\tag{28.1}
$$

$$
\boxed{
\rho
=
\mu^{-1},
}
\tag{28.2}
$$

and:

$$
\boxed{
\varepsilon_{n+1}
=
\rho
\varepsilon_n.
}
\tag{28.3}
$$

At a periodic vortex point:

$$
\boxed{
A_{\perp,n+1}
=
\rho
A_{\perp,n}.
}
\tag{28.4}
$$

Hence:

$$
\boxed{
\frac{
A_{\perp,n+1}
}{
\varepsilon_{n+1}
}
=
\frac{
A_{\perp,n}
}{
\varepsilon_n
}.
}
\tag{28.5}
$$

Likewise for one same material loop with negligible physical viscous circulation change:

$$
\boxed{
\frac{
\Gamma_{n+1}^{norm}
}{
\varepsilon_{n+1}
}
=
\frac{
\Gamma_n^{norm}
}{
\varepsilon_n
}.
}
\tag{28.6}
$$

This is the precise critical equality to attack next.

---

# 29. Why the equality cannot be excluded by energy summation

The raw kinetic core energy still obeys:

$$
\beta_{n+1}
=
q\beta_n,
\qquad
0<q<1.
$$

Thus:

$$
\sum_n\beta_n<\infty.
$$

The equality manifold may therefore consume a geometrically decreasing raw energy amount while preserving its dimensionless vortex structure after every re-root.

This is exactly the kind of critical recurrence that ordinary energy summation cannot exclude.

---

# 30. New closure-facing question

The remaining question is no longer:

> why does circulation contract?

That is answered by normalization.

It is:

> can an **unforced finite-energy same-parent Navier--Stokes solution** realize indefinitely a local Kelvin--Oseen critical vortex core whose stretching is supplied by the mandatory tail/PFET structure while all quotient-correct defects vanish?

The candidate equality state simultaneously needs:

1.:

   $$
   \Gamma/\varepsilon
   =
   \text{constant};
   $$

2.:

   $$
   A_\perp/\varepsilon
   =
   \text{constant};
   $$

3. inward radial PFET;

4. same-parent DSS return;

5. no raw energy atom;

6. no circulation cascade anomaly;

7. no transition escape.

This is now a sharply defined Navier--Stokes equality manifold.

---

# 31. Candidate strain-source split

A Burgers-type critical core requires persistent extensional strain.

For the DCRP branch the strain cannot be prescribed externally.

It must be generated by the same Navier--Stokes parent.

Therefore the equality branch naturally splits into:

$$
\boxed{
\text{local strain source}
\ \vee\
\text{tail-generated strain source}.
}
\tag{31.1}
$$

The local source returns to the existing strain/model-cone machinery.

The tail-generated source must cross the same finite matching region where DCRP-31 found inward PFET.

This suggests a coupled:

$$
\boxed{
\text{PFET}
+
\text{strain-source}
}
$$

return ledger rather than Kelvin contraction alone.

A quantitative closure is not yet proved in this round.

---

# 32. New exact frontier

The next target is:

$$
\boxed{
\textbf{
Critical Kelvin--Oseen Equality /
Same-Parent Tail-Strain Closure Lemma}.
}
$$

A sufficient theorem would prove that a strict same-parent Type-II equality state satisfying

$$
\boxed{
\Gamma/\varepsilon
=
\mathrm{const},
\qquad
A_\perp/\varepsilon
=
\mathrm{const}
}
$$

must have at least one of:

1. a nonzero quotient-correct circulation cascade;
2. a nonzero second-order viscous/tube concentration defect;
3. a nonzero tail-strain transition carrier;
4. a nonzero model-cone/strain tax;
5. a vortex-filament normal form incompatible with unforced finite-energy same-parent recurrence.

The last alternative is the new Liouville/classification route.

---

# 33. Source-status audit

## Eyink — circulation cascade

The coarse-grained velocity satisfies an exact effective equation with SGS stress and force.

For loops advected by the coarse velocity, the large-scale circulation obeys an exact balance whose non-viscous correction is the line integral of the SGS force.

Eyink defines the circulation flux from this force and shows:

$$
|f_\ell|
=
O
\left(
|\delta u(\ell)|^2/\ell
\right).
$$

For finite-length loops and velocity Holder exponent:

$$
h>1/2,
$$

the circulation flux vanishes as:

$$
\ell\downarrow0.
$$

The paper also explicitly notes that molecular viscosity is negligible at fixed coarse scale in the small-viscosity limit.

## Bedrossian--Germain--Harrop-Griffiths

Three-dimensional Navier--Stokes admits vortex-filament solutions of arbitrary circulation, including perturbative regimes around the Oseen vortex column and locally approximately self-similar curved filaments.

This prevents a local thin-filament exclusion by assertion.

## Gallay--Wayne

Burgers vortices provide rigorous three-dimensional strain--diffusion vortex equilibria in a background straining field.

Asymmetric variants also exist and are stable in appropriate classes.

This is the correct calibration for the critical transverse-area/viscosity equality.

---

# 34. End state

The main correction is:

$$
\boxed{
\Gamma_{ss}(s+S_0)
=
\rho\Gamma_{ss}(s)
}
$$

is **not itself** a native defect because:

$$
\boxed{
\varepsilon_{n+1}
=
\rho\varepsilon_n.
}
$$

The quotient-correct circulation is:

$$
\boxed{
\frac{
\Gamma^{norm}
}{
\varepsilon
}
=
\frac{
\Gamma^{phys}
}{
\nu
}.
}
$$

The strict DSS branch also satisfies the critical transverse equality:

$$
\boxed{
\frac{
A_\perp
}{
\varepsilon
}
=
\text{return invariant}
}
$$

at a periodic material vortex point.

Thus the true zero-defect state is a:

$$
\boxed{
\textbf{
Critical Kelvin--Oseen strain--diffusion equality manifold}.
}
$$

The exact coarse Kelvin balance is:

$$
\boxed{
\frac d{d\tau}
\Gamma_{n,\ell}
=
-
K_{n,\ell}
+
\varepsilon_n
\oint
\Delta U_{n,\ell}\cdot dy.
}
$$

At every fixed:

$$
\ell>0,
$$

the molecular term vanishes as:

$$
n\to\infty.
$$

Any nonuniform Kelvin failure must therefore enter:

$$
\boxed{
\text{circulation cascade}
\ \vee\
\text{microviscous concentration}
\ \vee\
\text{loop/transition defect}.
}
$$

DCRP-31's inward PFET gap remains valid.

The corrected strongest strict state is:

$$
\boxed{
\textbf{
tail-fed DSS}
+
\textbf{
inward PFET}
+
\textbf{
Kelvin--Oseen critical balance}.
}
$$

The next single frontier is:

$$
\boxed{
\textbf{
Critical Kelvin--Oseen Equality /
Same-Parent Tail-Strain Closure.
}
}
$$