---
title: "NS-ANP 05 Causal Correction"
version: "v0.2"
date: "2026-08-15"
status: "Corrective note"
---

# NS-ANP 05 Causal Correction v0.2

## Correction

In `NS_ANP_05_ArbitraryDepth_C3Paths_v0.1.md`, the original inheritance route treated:

$$
e_k^\chi(a)>0
$$

as sufficient for a causal inheritance parent.

This is too strong.

Positive earlier weighted shell energy proves earlier **state existence**, but not a positive propagated contribution to the later child observable.

The earlier state may be dissipated/cancelled while the later state is rebuilt by forcing.

## Correct inheritance criterion

Let:

$$
\mathsf U_u(t,a)
$$

solve the homogeneous shell transport--diffusion equation and let:

$$
\Phi_c
$$

be a terminal norming functional for the child.

Then define:

$$
\Phi(a)
=
\mathsf U_u(t_c,a)^\ast\Phi_c.
$$

The correct propagated inheritance contribution is:

$$
\boxed{
\mathcal I_c(a)
=
\langle
\omega_k(a),
\Phi(a)
\rangle.
}
$$

A positive causal inheritance edge requires:

$$
\boxed{
\mathcal I_c(a)>0.
}
$$

The exact dual ledger is:

$$
\boxed{
A_c
=
\mathcal I_c(a)
+
\int_a^{t_c}
\langle
F_k(s),
\Phi(s)
\rangle ds.
}
$$

If:

$$
\mathcal I_c(a)\le0,
$$

the source integral is strictly positive and supplies a positive source atom.

## Status after correction

The finite-depth continuation logic survives after replacing the original inheritance branch by:

$$
C3_{\rm PROP}
\vee
C3_W.
$$

The correction is incorporated into `NS_ANP_06_SingularHorizon_ExtractionAudit_v0.1.md`.

No Full Chain Necessity or regularity claim is made.