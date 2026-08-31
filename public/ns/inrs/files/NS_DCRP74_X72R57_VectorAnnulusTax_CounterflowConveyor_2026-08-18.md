# DCRP74 / X72-R57 — Vector Annulus Tax, Material Pressure Counterflow, and the Scale-Matched Conveyor Normal Form

**Date:** 2026-08-18  
**Status:** Proof-development checkpoint  
**Predecessor:** DCRP73 / X72-R56

## 0. Executive result

DCRP73 restored the native frontier to

\[
\boxed{\mathsf X_{\rm active}\vee\mathsf T.}
\]

The T branch carries two unavoidable finite normalized obligations:

1. DCRP31 inward physical pressure–kinetic-energy flux (PFET);
2. DCRP35/D59/D73 inward enstrophy/material turnover.

DCRP49 already proves these are independent observables, so the correct combined object is not one scalar current but a vector current.

Choose one finite normalized package

\[
\boxed{\mathcal A_* = \{R_-<|y|<R_+\}}
\]

containing both witnesses, and define

\[
\mathfrak J_E=\int_{R_-}^{R_+}w_E(R)[-\mathcal F(R)]_+\,dR,
\]

\[
\mathfrak J_\omega=\int_{R_-}^{R_+}w_\omega(R)\mathcal J_{\omega,\rm in}(R)\,dR.
\]

On the compact normalized T class,

\[
\boxed{\mathfrak J_E\ge c_E>0,\qquad \mathfrak J_\omega\ge c_\omega>0.}
\]

Hence

\[
\boxed{\mathbf J_*=(\mathfrak J_E,\mathfrak J_\omega)}
\]

has a strict vector gap, but the two coordinates are not algebraically identical.

The main new exact identity comes from following one similarity-material packet in the zero-stretch T submodel. If

\[
K_D=\int_{D(s)}\frac{|V|^2}{2},\qquad
Z_D=\int_{D(s)}\frac{|\Omega|^2}{2},
\]

and

\[
\Pi_P=\int_{\partial D(s)}PV\cdot n,
\]

then

\[
\boxed{K_D'=\gamma\kappa K_D-\Pi_P,}
\]

\[
\boxed{Z_D'=-(2-3\gamma)Z_D,}
\]

and therefore for

\[
Q_D:=K_D/Z_D
\]

one has

\[
\boxed{Q_D'=2\gamma Q_D-\Pi_P/Z_D.}
\]

If a proposed closed material cycle returns with

\[
Q_D(S_0)=Q_D(0)>0,
\]

then necessarily

\[
\boxed{
\int_0^{S_0}\frac{\Pi_P}{Z_D}\,ds
=2\gamma\int_0^{S_0}Q_D\,ds>0.
}
\]

Thus a closed zero-stretch material packet cannot be pressure-work silent: it must export pressure work in a positive enstrophy-weighted average.

At the same time D31 requires the fixed Eulerian core to receive inward PFET. Hence the surviving T equality geometry is a genuine counterflow:

\[
\boxed{\text{Eulerian energy inward}\quad/\quad\text{material pressure work outward}.}
\]

This does not contradict D49 because the two fluxes live on different observers (fixed sphere versus moving material boundary).

Finally, the two current magnitudes have the exact physical homogeneity

\[
\boxed{\mathfrak J_E^{\rm phys}\sim \ell^{3-2\alpha},}
\]

\[
\boxed{\mathfrak J_\omega^{\rm phys}\sim \ell^{1-2\alpha},}
\]

so after the natural energy conversion

\[
\boxed{\ell^2\mathfrak J_\omega^{\rm phys}\sim\mathfrak J_E^{\rm phys}\sim\ell^{3-2\alpha}.}
\]

Therefore the two-current raw energy-equivalent payments are geometrically summable in the strict Type-II range. A scale-only budget contradiction is impossible.

The surviving T normal form is therefore a **scale-matched pressure-mediated counterflow conveyor**.

---

## 1. Similarity local-energy equation

Use

\[
\gamma=\frac1{\alpha+1},\qquad \kappa=3-2\alpha,
\]

and

\[
Y=\gamma y+V,\qquad k=|V|^2/2.
\]

The similarity Euler equation is

\[
D_sV+(1-\gamma)V+\nabla P=0,
\qquad D_s=\partial_s+Y\cdot\nabla.
\]

Dotting with V gives

\[
D_sk+2(1-\gamma)k+V\cdot\nabla P=0.
\]

Since

\[
\nabla\cdot Y=3\gamma,
\]

and

\[
2-5\gamma=-\gamma\kappa,
\]

we get

### Theorem D74.1

\[
\boxed{
\partial_sk+\nabla\cdot[\gamma y\,k+(k+P)V]-\gamma\kappa k=0.
}
\]

Integrating over one period and B_R recovers D31 exactly:

\[
\boxed{
\mathcal F(R)=\gamma[\kappa\mathcal E(R)-R\mathcal E'(R)]
=-\gamma R^{\kappa+1}\frac d{dR}[R^{-\kappa}\mathcal E(R)].
}
\]

---

## 2. Similarity enstrophy equation

Let

\[
z=|\Omega|^2/2.
\]

From

\[
D_s\Omega+\Omega=S\Omega,
\]

we have

\[
D_sz+2z=\Omega\cdot S\Omega.
\]

Hence

### Theorem D74.2

\[
\boxed{
\partial_sz+\nabla\cdot(Yz)+(2-3\gamma)z=\Omega\cdot S\Omega.
}
\]

This is the exact local ledger behind D35/D59/D73.

---

## 3. Vector-valued annulus tax

D31 and D59 give two finite normalized positive coordinates. Their witness radii need not coincide, but one finite package can contain both.

Define

\[
\boxed{\mathbf J_*=(\mathfrak J_E,\mathfrak J_\omega).}
\]

Then

\[
\boxed{\|\mathbf J_*\|_2\ge\sqrt{c_E^2+c_\omega^2}>0.}
\]

This is a **vector tax**. There is no legitimate cancellation of one coordinate against the other.

What is not proved is pointwise/radius-wise overlap.

---

## 4. Physical scaling audit

At physical similarity length ell,

\[
|u|\sim\ell^{-\alpha},\qquad
|\omega|\sim\ell^{-\alpha-1},\qquad
dx\sim\ell^3,
\]

and one fixed similarity-time interval has physical duration

\[
dt\sim\ell^{\alpha+1}.
\]

### PFET

\[
(u^2+p)u\,dS\,dt
\sim\ell^{3-2\alpha}.
\]

Therefore

\[
\boxed{\mathfrak J_E^{\rm phys}\sim\ell^\kappa.}
\]

### Enstrophy turnover

\[
|\omega|^2u\,dS\,dt
\sim\ell^{1-2\alpha}.
\]

Therefore

\[
\boxed{\mathfrak J_\omega^{\rm phys}\sim\ell^{1-2\alpha}.}
\]

Multiplying by ell^2,

\[
\boxed{\ell^2\mathfrak J_\omega^{\rm phys}\sim\ell^\kappa.}
\]

Thus both energy-equivalent current coordinates have the same similarity homogeneity.

---

## 5. Flux length

Define

\[
\boxed{
L_{E\omega}^2
:=\frac{\mathfrak J_E^{\rm phys}}{\mathfrak J_\omega^{\rm phys}}.
}
\]

Then

\[
\boxed{L_{E\omega}^2=\ell^2\sigma_{E\omega}^2,}
\]

where

\[
\sigma_{E\omega}^2=\mathfrak J_E/\mathfrak J_\omega
\]

is dimensionless in normalized variables.

For exact DSS recurrence, a scale-matched equality conveyor simply repeats sigma and therefore

\[
\boxed{L_{E\omega}\propto\ell.}
\]

This is a natural cascade law, not a contradiction.

---

## 6. Scale-only depletion NO-GO

Let

\[
\ell_{n+1}=q_\ell\ell_n,
\qquad 0<q_\ell<1.
\]

Since

\[
\kappa=3-2\alpha>0,
\]

we have

\[
\boxed{\sum_n\ell_n^\kappa<\infty.}
\]

Hence even if every recurrence pays both normalized positive currents, the raw energy-equivalent tax is summable.

### Theorem D74.3

\[
\boxed{
\text{positive PFET + positive enstrophy turnover at all scales}
\not\Rightarrow
\text{raw energy exhaustion}.
}
\]

A state/pressure realizability obstruction is required.

---

## 7. Viscous ancestry scaling

The Navier–Stokes viscous kinetic-energy dissipation over one generalized similarity cycle scales as

\[
\nu\int|\omega|^2dxdt\sim\nu\ell^{2-\alpha}.
\]

Relative to the joint energy scale ell^kappa,

\[
\frac{\nu\ell^{2-\alpha}}{\ell^{3-2\alpha}}
=\nu\ell^{\alpha-1}.
\]

For alpha>1,

\[
\boxed{\nu\ell^{\alpha-1}\to0.}
\]

So the simplest viscous energy-budget coupling becomes asymptotically too weak to close T.

This does not exclude subtler Navier–Stokes ancestry constraints.

---

## 8. Material kinetic-energy ledger

Let D(s) be transported by Y. Define

\[
K_D(s)=\int_{D(s)}k\,dy.
\]

The moving boundary absorbs the Yk current. Define the outward pressure work

\[
\boxed{
\Pi_P(s)=\int_{\partial D(s)}PV\cdot n\,dS.
}
\]

Then Reynolds transport gives

### Theorem D74.4

\[
\boxed{K_D'=\gamma\kappa K_D-\Pi_P.}
\]

Pi_P is gauge invariant under P -> P+C(s), because div V=0.

---

## 9. Zero-stretch material enstrophy ledger

On the D73 zero-stretch T submodel,

\[
(\Omega\cdot\nabla)V=0,
\]

so

\[
D_s\Omega=-\Omega.
\]

For

\[
Z_D=\int_{D(s)}z\,dy,
\]

### Theorem D74.5

\[
\boxed{Z_D'=-(2-3\gamma)Z_D.}
\]

---

## 10. Exact material counterflow equation

Set

\[
Q_D=K_D/Z_D.
\]

Then

\[
Q_D'
=\gamma\kappa Q_D-\Pi_P/Z_D+(2-3\gamma)Q_D.
\]

But

\[
\gamma\kappa+(2-3\gamma)=2\gamma.
\]

Thus:

### Theorem D74.6 — Material Energy/Enstrophy Counterflow Law

\[
\boxed{Q_D'=2\gamma Q_D-\Pi_P/Z_D.}
\]

This is the main new exact coupling of the round.

---

## 11. Closed material ratio return forces pressure export

Suppose

\[
Q_D(S_0)=Q_D(0)>0.
\]

Integrating the previous equation gives

### Theorem D74.7

\[
\boxed{
\int_0^{S_0}\frac{\Pi_P}{Z_D}\,ds
=2\gamma\int_0^{S_0}Q_D\,ds>0.
}
\]

Equivalently,

\[
\boxed{
\int_0^{S_0}e^{-2\gamma s}\frac{\Pi_P}{Z_D}\,ds
=(1-e^{-2\gamma S_0})Q_D(0)>0.
}
\]

Therefore a closed zero-stretch material packet cannot be pressure-work silent.

---

## 12. Eulerian-in / Lagrangian-pressure-out

D31 requires finite-radius inward total PFET:

\[
\mathcal F<0
\]

on a nontrivial set.

D74.7 requires positive weighted outward pressure work on any closed material packet ratio cycle.

These are different surfaces/observers, so they do not contradict D49.

Instead they imply the counterflow architecture

\[
\boxed{
\text{Eulerian core energy inward}
\quad\text{while}\quad
\text{material pressure work is outward}.
}
\]

A passive conveyor is therefore impossible.

---

## 13. Surviving T normal form

The strongest T equality geometry is now the

# Scale-Matched Counterflow Conveyor (CFC)

It must simultaneously carry:

- positive normalized inward PFET;
- positive normalized inward enstrophy turnover;
- flux length L_Eomega proportional to the physical similarity scale;
- material replacement, or else the exact positive pressure-export law for any closed Q_D cycle.

This is a pressure-mediated conveyor, not mere radial replacement.

---

## 14. What remains open

D74 does not prove:

- PFET and enstrophy turnover occur on the same radius;
- material pressure export equals -PFET;
- material pressure export directly forces X72 E_p;
- CFC is impossible.

D49's independence warning remains active.

---

## 15. New pressure bridge target

T has now generated a gauge-invariant pressure observable

\[
\Pi_P=\int_{\partial D}PV\cdot n.
\]

X is controlled by pressure curvature / response

\[
E_p=H_P^0+C_S^0.
\]

The next high-leverage question is whether, after removing packet translation and affine pressure jets, the positive recurrent material pressure-export functional forces nonzero pressure curvature on the same finite package.

A useful decomposition is

\[
V=\bar V_D+V_D^0,
\qquad \int_DV_D^0=0,
\]

and

\[
P=P_{\rm aff}+P_{\rm curv}.
\]

The target is a centered pressure-work / Hessian identity rather than an invalid universal PFET=E_p relation.

---

## STOP-D74

\[
\boxed{
\textbf{
PFET and inward enstrophy turnover form a vector-valued finite-annulus tax, but their natural energy-equivalent raw scalings match and remain summable. The new exact material law Q_D'=2 gamma Q_D-Pi_P/Z_D shows that every closed zero-stretch normalized packet cycle must export pressure work while the Eulerian recurrent core simultaneously imports PFET. Thus the surviving T equality state is a scale-matched pressure-mediated counterflow conveyor.}
}
\]

---

## Next: DCRP75 / X72-R58

**Material Pressure Export versus X72 Pressure Curvature**

Target:

\[
\boxed{
\mathsf T_{\rm CFC}
\Longrightarrow
\mathsf X
\vee
\text{one explicit affine-pressure / bulk-translation conveyor normal form}.
}
\]

**End checkpoint:** DCRP74 / X72-R57.
