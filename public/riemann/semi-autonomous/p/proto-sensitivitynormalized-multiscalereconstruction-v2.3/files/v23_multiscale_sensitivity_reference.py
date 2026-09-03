#!/usr/bin/env python3
"""
AMRAL RH v2.3 — multiscale sensitivity-normalization reference checks.

REFERENCE ONLY.
"""

from __future__ import annotations
import cmath
import math


def second_difference(f, t: float, h: float):
    return f(t+h) + f(t-h) - 2.0*f(t)


def D(f, t: float, h: float):
    return 0.5*second_difference(f, t, h)


def multiscale_reconstruction(f, t: float, h: float, m: int):
    return sum(
        (m-abs(k))*D(f, t+k*h, h)
        for k in range(-(m-1), m)
    )


def normalized_D(f, t: float, h: float):
    return D(f, t, h)/(h*h)


def normalized_multiscale(f, t: float, h: float, m: int):
    return sum(
        (m-abs(k))/(m*m) * normalized_D(f, t+k*h, h)
        for k in range(-(m-1), m)
    )


def modal_multiplier(lam: complex, h: float) -> complex:
    return cmath.cosh(lam*h)-1.0


def normalized_modal_multiplier(lam: complex, h: float) -> complex:
    return modal_multiplier(lam, h)/(h*h)


def tent_response(z: complex, h: float) -> complex:
    if abs(z) < 1e-14:
        return h*h
    return 2.0*(cmath.cosh(h*z)-1.0)/(z*z)


def normalized_tent_response(z: complex, h: float) -> complex:
    return tent_response(z, h)/(h*h)


def corrected_beta(beta_raw: float, alpha: float, order: int = 2) -> float:
    return beta_raw + 2.0*order*alpha


def corrected_kappa(kappa_raw: float, alpha: float, order: int = 2) -> float:
    return kappa_raw - 2.0*order*alpha


if __name__ == "__main__":
    funcs = [
        lambda x: math.exp(0.2*x),
        lambda x: math.sin(1.7*x)+0.3*math.cos(0.4*x),
        lambda x: x**4 - 2*x + 1,
    ]
    for m in [2,3,5,8]:
        h = 0.13
        H = m*h
        for f in funcs:
            lhs = D(f, 0.7, H)
            rhs = multiscale_reconstruction(f, 0.7, h, m)
            nlhs = normalized_D(f, 0.7, H)
            nrhs = normalized_multiscale(f, 0.7, h, m)
            print("m",m,"raw residual",lhs-rhs,"norm residual",nlhs-nrhs)

    lam = 0.13 + 14j
    H = 0.7
    for m in [2,4,8,16,32,64]:
        h = H/m
        ratio = modal_multiplier(lam,H)/modal_multiplier(lam,h)
        print("m",m,"raw ratio/m^2",ratio/(m*m),
              "normalized fine",normalized_modal_multiplier(lam,h))

    delta = 0.1
    for h in [0.7,0.2,0.05,0.01]:
        print("h",h,"resonance normalized tent",
              normalized_tent_response(delta,h))
