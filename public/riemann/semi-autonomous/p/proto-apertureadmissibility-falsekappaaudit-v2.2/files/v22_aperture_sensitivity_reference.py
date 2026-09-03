#!/usr/bin/env python3
"""
AMRAL RH v2.2 — aperture sensitivity / false-kappa reference checks.

REFERENCE ONLY.
"""

from __future__ import annotations


def exact_symmetry_multiplier(rho: complex, r: float) -> complex:
    return ((1+r)**rho + (1-r)**rho - 2.0) / rho


def asymptotic_multiplier(rho: complex, r: float) -> complex:
    return (rho - 1.0) * r*r


def mode_power_exponent(delta: float, a: float, order: int = 2) -> float:
    return delta - order*(1.0-a)


def total_blind_for_zeta(a: float, order: int = 2) -> bool:
    return 0.5 - order*(1.0-a) < 0.0


def aperture_alpha_from_a(a: float) -> float:
    return 1.0-a


if __name__ == "__main__":
    rho = 0.6 + 14.134725j
    for r in [1e-1, 1e-2, 1e-3, 1e-4]:
        exact = exact_symmetry_multiplier(rho, r)
        approx = asymptotic_multiplier(rho, r)
        print(
            "r", r,
            "exact", exact,
            "approx", approx,
            "relative error", abs(exact-approx)/abs(exact)
        )

    for a in [0.25, 0.5, 0.6, 0.75, 0.9, 0.99]:
        print(
            "a", a,
            "alpha", aperture_alpha_from_a(a),
            "delta=.1 exponent", mode_power_exponent(0.1, a),
            "delta=.5 exponent", mode_power_exponent(0.5, a),
            "total blind", total_blind_for_zeta(a)
        )
