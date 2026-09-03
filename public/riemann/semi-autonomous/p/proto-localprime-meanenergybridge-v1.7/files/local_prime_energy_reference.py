#!/usr/bin/env python3
"""
AMRAL RH v1.7 — finite local-prime energy reference implementation.

REFERENCE ONLY. NOT A RIGOROUS RH CERTIFICATE ENGINE.

Uses precomputed prime powers and vectorized trapezoidal integration.
"""

from __future__ import annotations
import math
import numpy as np


def sieve_primes(limit: int):
    if limit < 2:
        return []
    mark = np.ones(limit + 1, dtype=bool)
    mark[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if mark[p]:
            mark[p*p:limit+1:p] = False
    return np.flatnonzero(mark).tolist()


def prime_powers_below(xmax: float):
    limit = max(2, int(math.floor(xmax)))
    out = []
    for p in sieve_primes(limit):
        q = p
        lp = math.log(p)
        while q < xmax:
            out.append((q, lp))
            if q > limit // p:
                break
            q *= p
    out.sort()
    return out


def tent(h: float, x):
    return np.maximum(h - np.abs(x), 0.0)


def main_density(t, h: float):
    t = np.asarray(t, dtype=float)
    return 8.0 * np.exp(t/2.0) * (math.cosh(h/2.0)-1.0)


def discrepancy_grid(t_grid, h: float, pps):
    t_grid = np.asarray(t_grid, dtype=float)
    total = np.zeros_like(t_grid)
    for q, lp in pps:
        a = math.log(q)
        vals = tent(h, t_grid-a)
        if np.any(vals):
            total += lp/math.sqrt(q) * vals
    return total - main_density(t_grid, h)


def block_energy(m: int, h: float, global_pps, samples: int = 4001):
    grid = np.linspace(m, m+1, samples)
    lo = math.exp(m-h)
    hi = math.exp(m+1+h)
    active = [(q,lp) for q,lp in global_pps if lo < q < hi]
    vals = discrepancy_grid(grid, h, active)
    return float(np.trapezoid(vals*vals, grid)), len(active)


def tent_autocorrelation(h: float, d: float) -> float:
    r = abs(d)
    if r >= 2*h:
        return 0.0
    if r <= h:
        return 2*h**3/3 - h*r*r + r**3/2
    return (2*h-r)**3/6


def numerical_tent_autocorrelation(h: float, d: float, samples: int = 200001):
    lo = max(-h, d-h)
    hi = min(h, d+h)
    if lo >= hi:
        return 0.0
    x = np.linspace(lo, hi, samples)
    y = tent(h, x) * tent(h, x-d)
    return float(np.trapezoid(y, x))


def demo():
    h = math.log(2.0)
    max_m = 8
    cutoff = math.exp(max_m + 1 + h)
    pps = prime_powers_below(cutoff)

    print("h =", h)
    print("prime cutoff =", cutoff)
    for d in [0.0, h/2, h, 1.5*h, 2*h]:
        exact = tent_autocorrelation(h, d)
        numeric = numerical_tent_autocorrelation(h, d, samples=20001)
        print("kernel", d, exact, "residual", exact-numeric)

    for m in range(1, max_m+1):
        e, active = block_energy(m, h, pps, samples=2001)
        print("block", m, "energy", e, "active_pp", active)


if __name__ == "__main__":
    demo()
