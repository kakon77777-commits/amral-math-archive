#!/usr/bin/env python3
"""
AMRAL RH v2.1 — variance-saving / fixed-strip strength converter.

REFERENCE ONLY.
"""

from __future__ import annotations

import math
import cmath


def theta_from_kappa(kappa: float) -> float:
    """J(x,1) <= x^(3-kappa) -> Theta <= 1-kappa/2."""
    return 1.0 - 0.5 * kappa


def beta_from_kappa(kappa: float) -> float:
    return 1.0 - kappa


def strip_from_kappa(kappa: float):
    theta = theta_from_kappa(kappa)
    return 1.0 - theta, theta


def twisted_main_factor(h: float, tau: float) -> complex:
    z = 0.5 - 1j * tau
    if abs(z) < 1e-14:
        return h*h
    return 2.0 * (cmath.cosh(z*h) - 1.0) / (z*z)


def twisted_main_integral_numeric(h: float, tau: float, n=200000) -> complex:
    """
    Numerically integrate int_{-h}^h T_h(v) exp(-(1/2-i tau)v) dv.
    """
    dv = 2*h/n
    total = 0j
    for k in range(n+1):
        v = -h + k*dv
        tent = max(h-abs(v), 0.0)
        f = tent * cmath.exp(-(0.5-1j*tau)*v)
        w = 0.5 if k in (0, n) else 1.0
        total += w*f
    return total*dv


def gallagher_transferred_exponent(kappa: float) -> float:
    """
    If J ~ X H^2 X^{-kappa}, H=X/U, then
    U^2 J / X^2 ~ X^{1-kappa}.
    """
    return 1.0-kappa


if __name__ == "__main__":
    h = math.log(2.0)
    for tau in [0.0, 1.0, 10.0, 100.0]:
        a = twisted_main_factor(h, tau)
        b = twisted_main_integral_numeric(h, tau, n=20000)
        print("tau", tau, "closed", a, "numeric", b, "residual", abs(a-b))

    for kappa in [0.0, 0.05, 0.1, 0.25, 0.5, 0.9, 1.0]:
        print(
            "kappa", kappa,
            "beta", beta_from_kappa(kappa),
            "Theta", theta_from_kappa(kappa),
            "strip", strip_from_kappa(kappa)
        )
