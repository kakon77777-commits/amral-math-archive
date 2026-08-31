---
title: "Navier–Stokes Residual Kernel and Amplitude Program: Cycle-XI Roadmap"
version: "v0.1"
date: "2026-08-16"
status: "Active research roadmap"
---

# NS-RKAP Cycle-XI Roadmap v0.1

## Starting point

Cycle X reduced the surviving residual to:

$$
\boxed{
\textbf{TSRP}.
}
$$

The main generic geometric branch is the hyperbolic two-sided mismatch:

$$
H=u\otimes w+w\otimes u,
\qquad
w\perp u,
$$

and under flux invisibility:

$$
w\perp S_u u.
$$

## RKAP-01 — Hyperbolic Fiber / Amplitude Lift

### Native covariance-transport transversality

The external linearized energy balance contains:

$$
-(\dot R U)\cdot\nabla\phi.
$$

At:

$$
U=u,
$$

the hyperbolic mismatch satisfies:

$$
\boxed{
Hu=|u|^2w.
}
$$

Therefore:

$$
\boxed{
|Hu|
=
\frac{|u|}{\sqrt2}
\|H\|_F.
}
$$

On:

$$
|u|\ge m>0,
$$

this is quantitatively coercive.

### Transport-separating finite window

For selected energy tests:

$$
T_{\phi_j}(H)
=
\iint(Hu)\cdot\nabla\phi_j,
$$

a finite-dimensional hyperbolic class with trivial common transport kernel has a positive finite-window gap.

Thus a native linear energy route can kill HYP if:

- test geometry separates:
  $$
  Hu;
  $$
- cancellation by other energy terms is controlled.

### Two-sided PSD lift

Define:

$$
T_{\rm lift}(H)
=
\inf_{A,B\ge0,\ A-B=H}
[
\operatorname{tr}A+\operatorname{tr}B
].
$$

Then:

$$
\boxed{
T_{\rm lift}(H)
=
\|H\|_*.
}
$$

For hyperbolic:

$$
H,
$$

$$
\boxed{
T_{\rm lift}(H)
=
2|u||w|
=
\sqrt2\|H\|_F.
}
$$

### Positive covariance lift cost

Any realization:

$$
H=R^+-R^-,
\qquad
R^\pm\ge0
$$

satisfies:

$$
\boxed{
\operatorname{tr}R^+
+
\operatorname{tr}R^-
\ge
\|H\|_*.
}
$$

At least one side carries covariance energy comparable to the residual amplitude.

### Linear-amplitude candidate

For:

$$
H_n=\rho_n\widehat H_n,
$$

normalized hyperbolic:

$$
\widehat H_n,
$$

the lift tax is:

$$
\boxed{
T_{\rm lift}(H_n)
\asymp
\rho_n.
}
$$

If a recursive budget can charge the positive two-package lift linearly:

$$
B_n-B_{n+1}
\gtrsim
\lambda_n\rho_n-e_n,
$$

recurrence is excluded when:

$$
\boxed{
\sum_n\lambda_n\rho_n=\infty.
}
$$

For:

$$
\rho_n\sim n^{-2/3},
$$

and:

$$
\lambda_n\sim n^{-s},
$$

the threshold is:

$$
\boxed{
s\le1/3.
}
$$

### No-go

The lift tax is not automatically telescoping.

Existing linear PFET energy observations act on the signed residual and do not automatically charge the sum of positive lift energies.

Thus:

$$
\boxed{
\text{lift geometry}
\neq
\text{global lift packing}.
}
$$

## Current obligations

$$
\boxed{
TR\mbox{-}GAP
}
$$

moving-window covariance-transport test separation;

$$
\boxed{
LIFT\mbox{-}REAL
}
$$

positive NS-realizable two-package lift;

$$
\boxed{
LIFT\mbox{-}PACK
}
$$

global/telescoping lift-energy tax;

$$
\boxed{
AMP
}
$$

physical amplitude Critical Lift.

## RKAP-02

Transport-Test Gap Stability / Positive-Lift Realizability / Two-Package Energy Depletion / Hyperbolic Degenerate Sets / Linear-Amplitude Packing.

## Hard rules

- Linear sign-changing covariance trace and nonlinear positive lift cost are different objects.
- Lift tax uses pre-existing positive package coordinates; do not create a copied residual gate.
- A pointwise positive lift cost is not a global finite budget.
- Covariance-transport transversality is native because $\dot R U$ already appears in the linearized local-energy balance.
- A finite energy-test family must actually separate the moving hyperbolic class; this is not automatic.
- No Navier-Stokes regularity claim is made.