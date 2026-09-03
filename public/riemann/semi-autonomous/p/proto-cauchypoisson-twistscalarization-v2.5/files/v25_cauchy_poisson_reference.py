#!/usr/bin/env python3
"""
AMRAL RH v2.5 — Cauchy / Poisson scalarization reference checks.

REFERENCE ONLY.

Checks:
1. Cauchy characteristic-function identity numerically using oscillatory quadrature.
2. Finite exponential-sum Cauchy mean against exact pair kernel.
3. Resolvent Green energy against exact pair kernel for point masses.
"""

from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad


def cauchy_ft_numeric(d: float) -> float:
    """
    Numerically verify
        int exp(-i tau d)/(pi(1+tau^2)) d tau = exp(-|d|).
    Uses cosine-weight quadrature on [0,inf).
    """
    d = abs(float(d))
    if d == 0.0:
        val, _ = quad(
            lambda t: 1.0/(math.pi*(1.0+t*t)),
            0.0, np.inf, epsabs=1e-13, epsrel=1e-13, limit=500
        )
        return 2.0*val

    val, _ = quad(
        lambda t: 1.0/(math.pi*(1.0+t*t)),
        0.0, np.inf,
        weight="cos", wvar=d,
        epsabs=1e-13, limit=500
    )
    return 2.0*val


def cauchy_ft_closed(d: float) -> float:
    return math.exp(-abs(d))


def finite_pair_closed(v, a):
    v = np.asarray(v, dtype=float)
    a = np.asarray(a, dtype=complex)
    total = 0j
    for i in range(len(v)):
        for j in range(len(v)):
            total += (
                a[i] * np.conjugate(a[j])
                * math.exp(-abs(v[i]-v[j]))
            )
    return float(total.real)


def finite_cauchy_mean_numeric(v, a):
    """
    Independent numerical reconstruction of the Cauchy mean by numerically
    evaluating the Cauchy characteristic function for every frequency gap.
    """
    v = np.asarray(v, dtype=float)
    a = np.asarray(a, dtype=complex)
    total = 0j
    for i in range(len(v)):
        for j in range(len(v)):
            total += (
                a[i] * np.conjugate(a[j])
                * cauchy_ft_numeric(v[i]-v[j])
            )
    return float(total.real)


def green_y_scalar(x, v, a):
    return 0.5 * np.sum(a * np.exp(-np.abs(x-v)))


def green_yprime_scalar(x, v, a):
    diff = x-v
    return -0.5 * np.sum(
        a * np.sign(diff) * np.exp(-np.abs(diff))
    )


def resolvent_energy_numeric(v, a):
    """
    Verify:
        pair energy = 2 int_R (y^2 + y'^2) dx
    with y = (1/2 e^{-|.|}) * sum a_j delta_{v_j}.

    The integration is split at every point source and extends to +/- infinity.
    """
    v = np.asarray(v, dtype=float)
    a = np.asarray(a, dtype=float)
    order = np.argsort(v)
    v = v[order]
    a = a[order]

    def integrand(x):
        y = green_y_scalar(x, v, a)
        yp = green_yprime_scalar(x, v, a)
        return 2.0*(y*y + yp*yp)

    bounds = [-np.inf] + v.tolist() + [np.inf]
    total = 0.0
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        val, _ = quad(
            integrand, lo, hi,
            epsabs=1e-12, epsrel=1e-12, limit=200
        )
        total += val
    return total


if __name__ == "__main__":
    for d in [0.0, 0.2, 0.7, 1.5, 3.0]:
        print("FT", d, cauchy_ft_closed(d), cauchy_ft_numeric(d))

    v = np.array([-0.6, -0.1, 0.35, 0.8])
    a = np.array([0.7, -1.1, 0.9, 0.4])
    print("pair closed", finite_pair_closed(v,a))
    print("Cauchy numeric", finite_cauchy_mean_numeric(v,a))
    print("resolvent numeric", resolvent_energy_numeric(v,a))
