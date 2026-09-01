---
title: "NS-CSP Cycle II — Standard PDE Recompilation"
version: "v1.0"
date: "2026-08-15"
status: "Cycle-II standard-PDE theorem/status recompilation"
---

# NS-CSP Cycle II — Standard PDE Recompilation v1.0

## 1. Purpose

This document removes most CSP-specific terminology and records the main standard-PDE content established or imported during Cycle II.

## 2. Middle-strain to local frequency amplitude

For a dyadic strain block $S_j=\nabla_{\rm sym}\Delta_ju$ and a wavelength cell $Q$ with $\ell(Q)=A2^{-j}$,

$$
\boxed{
2^{-j/2}\|\Delta_ju\|_\infty
\gtrsim_A
\|S_j\|_{L^2(Q)}.
}
$$

## 3. Spatial-atom equivalence

For a dyadic vorticity block $\omega_j$, define

$$
a_\omega^A(j,t)
=
\sup_Q
\frac{\|\omega_j\|_{L^2(Q)}^2}{\|\omega_j\|_2^2}.
$$

Then

$$
\boxed{
2^{-j/2}\|u_j\|_\infty
\asymp_A
\sqrt{a_\omega^A(j,t)}\,\|\omega_j\|_2.
}
$$

## 4. Type-I singular-core UV extraction

Under Barker--Prange Type-I hypotheses, singular-core vorticity enstrophy concentration and Lorentz--Bernstein imply a local high-frequency vorticity lower bound at parabolic frequency or above.

## 5. Spectral atomization

For

$$
D_{\rm eig}(S)=\inf_\rho\|-\rho\Delta S-S\|_2,
$$

projection monotonicity holds and severe dyadic spectral atomization implies

$$
D_{\rm eig}(F)^2\gtrsim\|F\|_2^2.
$$

## 6. Moving-window domination

On Bradshaw--Grujic active escape intervals at $\epsilon=1/2$,

$$
\boxed{
\Phi_{1/2}(t)
\ge
\frac12\|u(t)\|_{\dot B^{-1/2}_{\infty,\infty}}.
}
$$

## 7. Continuous Besov escape levels

Every sufficiently large critical-Besov level defines an escape time with an intrinsic $L^{-4}$ recovery interval carrying a universal moving-window action packet.

## 8. Model-cone departure

With

$$
\mathcal R_{SV}
=
P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right),
$$

one has

$$
\frac12\frac d{dt}\|S\|_{\dot H^1}^2
+
\|-\Delta S\|_2^2
=
-\langle\mathcal R_{SV},-\Delta S\rangle.
$$

## 9. Preload survival/replenishment

A later middle-strain spike forces high-frequency $\dot H^1$ strain stock. Old stock is exponentially heat-suppressed according to its viscous age. Therefore a stale preloaded reservoir must be exponentially oversized at the earlier escape time or replenished by Duhamel forcing.

## 10. Replenishment source split

The strain forcing is

$$
\frac12P_{st}(\omega\otimes\omega)-\mathcal R_{SV}.
$$

High-frequency quadratic-vorticity replenishment requires at least one high-frequency vorticity parent state.

## 11. Core dilution budget

Under the stated Type-I local shell hypothesis,

$$
\int\frac{dt}{\beta_c(t)R_I(t)}<\infty.
$$

## 12. Dissipation-range constraints

Cheskidov--Shvydkoy give

$$
\int_0^T\|\omega_{\le Q(t)}\|_{B^0_{\infty,\infty}}dt<\infty
\Longrightarrow
\text{regularity}.
$$

Cheskidov--Dai provide a terminal high-shell smallness criterion. Hence hypothetical blow-up must combine nonintegrable low-mode driver activity with recurrent non-small terminal high-shell activity.

## 13. Functional-analytic limitation

Finite energy and bounded instantaneous $\dot B^{-1/2}_{\infty,\infty}$ amplitude do not control $\|S\|_{\dot H^1}$. Therefore exponential preload cannot be excluded by static energy/Besov interpolation alone.

## 14. Final Cycle-II residual core

The unresolved mechanisms are:

1. exponentially inflated old-stock preload;
2. dissipation-range replenishment surviving low/high activity constraints;
3. Type-I core dilution profiles consistent with the energy budget;
4. source/state multiplicity, cancellation and efficiency loss.

## 15. Status

$$
\boxed{\text{Coercive Synchronization: PARTIALLY CLOSED}}
$$

$$
\boxed{\text{Finite Obstruction: OPEN}}
$$

$$
\boxed{\text{3D Navier--Stokes regularity: OPEN}}
$$