# DCRP92 / X72-R75 — Finite-Scale Defect Confluence, Joint Detector Compression, and Positive-Density Recurrence

**Series:** Independent Navier–Stokes Research Series / X72 Bridge  
**Date:** 2026-08-19  
**Status:** Proof-development checkpoint / finite-scale confluence round  
**Immediate predecessor:** `NS_DCRP91_X72R74_FilamentationScale_DirectionDiffusionCompiler_2026-08-19.md`

## Executive result

DCRP91 reduced same-parent material regeneration to
\[
\widetilde{\mathcal S}_{\rm active}
\vee
R_{\rm FV}
\vee
\mathfrak D_{\rm gap}
\vee
R_{\rm state}
\vee
R_{\rm crit}.
\]

This round compresses the first three finite-scale branches into one finite detector vector.

### 1. Fixed-relative filtered-vorticity activity returns to the increment compiler

On a sequentially compact carrier-locked bounded-reservoir class, suppose
\[
R_{\rm FV}\ge c_{\rm FV}>0.
\]
If
\[
\widetilde{\mathcal S}^{(3)}=0,
\]
then all velocity increments on the filter-support directions vanish. On a connected strong-profile region the velocity is spatially constant, hence vorticity and every filtered-vorticity rank/gradient/direction witness vanish. Contradiction.

Therefore compactness yields
\[
\boxed{
R_{\rm FV}\ge c_{\rm FV}
\Longrightarrow
\widetilde{\mathcal S}^{(3)}\ge s_{\rm FV}>0.
}
\]

This is a compactness-separation theorem, not a claimed universal pointwise inequality.

### 2. D26 already gives a finite recurrence detector for persistent strong increments

For a compact strong-profile class with
\[
\widetilde{\mathcal S}^{(3)}\ge s_*>0,
\]
D26 gives finitely many normalized SGS recurrence windows with
\[
\boxed{
\max_{1\le m\le N_S}
\left[
W^{\rm SGS}_{m,+}
+
|L^{\rm SGS}_m|
+
|\Delta K^{\rm SGS}_m|
\right]
\ge c_S>0.
}
\]

Thus both the raw increment branch and the fixed-relative filtered-vorticity branch share one recurrence compiler.

### 3. Gap debt is a route selector, not a local terminal

At a CKN-bad scale,
\[
\Psi\ge\varepsilon_{\rm CKN}.
\]
The coarse-resolution theorem gives
\[
\Psi\le4\Psi^\ell+4\Omega^\ell.
\]
Hence
\[
\boxed{
\Psi^\ell\ge\varepsilon_{\rm CKN}/8
\quad\vee\quad
\Omega^\ell\ge\varepsilon_{\rm CKN}/8.
}
\]

The second branch is an explicit subfilter velocity-pressure residual.

On the first branch, D87 supplies a finite combined pressure-flux work test family:
\[
\boxed{
\max_{1\le j\le N_G}
|\langle G^\ell,\psi_j\rangle|
\ge c_G>0
}
\]
after the already-declared residual/leakage/return/compactness escapes are removed.

Therefore the scale-gap debt guarantees repeated visits to the same finite detector architecture.

### 4. Joint detector vector

Define
\[
\mathbf J
=
(
\mathbf J_{\rm SGS},
\mathbf J_G,
J_{\rm sub},
J_{\rm loc},
J_{\rm ret}
).
\]

Its entries are:

\[
J_{{\rm SGS},m}
=
W^{\rm SGS}_{m,+}
+
|L^{\rm SGS}_m|
+
|\Delta K^{\rm SGS}_m|,
\]

\[
J_{G,j}
=
|\langle G^\ell,\psi_j\rangle|,
\]

\[
J_{\rm sub}=\Omega^\ell,
\qquad
J_{\rm loc}=\mathcal R_{\rm loc/press},
\qquad
J_{\rm ret}=\mathcal R_{\rm return}.
\]

Let
\[
\mathfrak J_{\rm joint}
=
\|\mathbf J\|_{\ell^\infty}.
\]

Then on a compact same-parent material-regeneration class with state/critical-reservoir escape excluded,

\[
\boxed{
\mathfrak J_{\rm joint}\ge c_J>0.
}
\]

No single universal signed scalar is claimed; the correct object is finite-dimensional vector observability.

### 5. Why no new pressure-compatible equality kernel survives

D24 isolated the pressure-compatible covariance kernel
\[
\nabla\times\nabla\cdot R_\ell=0.
\]
D25 derived the nonnegative SGS viscous variance
\[
d_\ell
=
S_\ell|\nabla u|^2-|\nabla U_\ell|^2.
\]
If
\[
d_\ell=0,
\]
the strong profile is locally affine. Native Morrey growth
\[
\int_{B_R}|u|^2\lesssim R
\]
eliminates every nonzero global affine profile.

D26 further proves that a persistent nonzero strong increment profile cannot have all forward SGS work, localization transport, and endpoint-return mismatch vanish on every normalized recurrence window.

D87 analogously excludes a compact recurrent resolved-bad package with zero combined pressure-flux work, zero leakage, and exact endpoint return.

So the old pressure-compatible / work-orthogonal kernels do not create new joint-detector coordinates.

### 6. Finite-coordinate recurrence theorem

Let the joint vector have \(M_J\) scalar nonnegative coordinates.

At each regeneration event choose one coordinate \(i(n)\) with
\[
J_{i(n)}\ge c_J.
\]
Among the first \(N\) events some coordinate occurs at least
\[
N/M_J
\]
times.

Thus there exists one fixed coordinate \(i_*\) with
\[
\boxed{
\limsup_{N\to\infty}
\frac1N
\#\{n\le N:J_{i_*}^{(n)}\ge c_J\}
\ge
\frac1{M_J}.
}
\]

D88 gives a uniform ancestry depth \(N_*\). If one detector hit is guaranteed only somewhere inside every ancestry block of length \(N_*\), then
\[
\boxed{
\limsup_{N\to\infty}
\frac1N
\#\{n\le N:J_{i_*}^{(n)}\ge c_J\}
\ge
\frac1{M_JN_*}.
}
\]

So the survivor cannot evade forever by changing defect type.

### 7. Sign splitting

For each combined-work test
\[
w_j=\langle G^\ell,\psi_j\rangle
\]
replace the absolute coordinate by
\[
w_j^+,
\qquad
w_j^-.
\]
If
\[
|w_j|\ge c_G,
\]
one of these sign coordinates is at least \(c_G\).

Hence if a combined-work coordinate is the recurrent detector, one fixed sign—forward work or backscatter—recurs at positive generation density.

### 8. X72 is not needed for this confluence step

The pressure-compatible increment zero-work kernel is already removed by SGS variance + recurrence + Morrey rigidity.

The resolved zero-combined-work recurrent kernel is already removed by the resolved-energy identity + endpoint return + leakage silence + Morrey rigidity.

Therefore no new pressure-perfect equality state needs to be handed to X72 merely to merge the finite-scale branches.

X72 remains available only if a later pressure/cofactor residual survives.

## Main theorem — Joint late material compiler

\[
\boxed{
\text{same-parent material regeneration}
\Longrightarrow
\mathfrak J_{\rm joint}\ge c_J
\vee
R_{\rm state}
\vee
R_{\rm crit}.
}
\]

The old local labels
- velocity increment,
- filtered-vorticity geometry,
- scale-gap debt

now feed one finite recurrence package.

## What remains open

This does **not** prove a global depletion contradiction.

A detector coordinate can recur at positive generation density while its physical scale weights remain geometrically summable.

The remaining problem is now finite-dimensional:

> can one fixed sign/residual coordinate recur at positive generation density while paying only geometrically summable physical cost?

## STOP-D92

The late material tree has collapsed from many geometric and PDE defect types to one finite detector vector. Fixed-relative filtered-vorticity activity is compactly separated from zero velocity increments and therefore re-enters the D26 finite SGS recurrence compiler. Scale-gap badness enters resolved coarse badness or an explicit subfilter residual; the resolved branch enters D87's finite pressure-flux work family. Since the detector vector is finite and Kelvin ancestry depth is uniformly bounded, at least one fixed detector coordinate—and one fixed sign when it is a work coordinate—must recur at positive generation density at least \(1/(M_JN_*)\). The survivor can no longer hide by changing defect type indefinitely.

## Next autonomous step

### DCRP93 / X72-R76 — Positive-Density Detector Channel / Regeneration Debt

Attack one recurrent coordinate at a time:
- SGS forward work;
- combined forward work;
- combined backscatter;
- subfilter residual;
- localization/pressure residual;
- endpoint-return mismatch.

Goal:
\[
\boxed{
\text{positive-density finite detector recurrence}
\Longrightarrow
\text{non-summable regeneration debt}
\vee
\text{one explicit critical conveyor}.
}
\]
