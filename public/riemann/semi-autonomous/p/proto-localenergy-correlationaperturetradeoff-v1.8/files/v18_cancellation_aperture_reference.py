#!/usr/bin/env python3
"""
AMRAL RH v1.8 reference checks.

REFERENCE ONLY.
- dyadic local energy / prime self-energy decomposition
- zero-side mean-energy partial sum
- shrinking-aperture synthetic mode response
"""

from __future__ import annotations

import math
import numpy as np
import mpmath as mp

mp.mp.dps = 35


def sieve_primes(limit: int):
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


def tent(h, x):
    return np.maximum(h - np.abs(x), 0.0)


def block_decomposition(m, h, pps, samples=20001):
    grid = np.linspace(m, m+1, samples)
    lo = math.exp(m-h)
    hi = math.exp(m+1+h)
    active = [(q,lp) for q,lp in pps if lo < q < hi]

    prime_field = np.zeros_like(grid)
    self_density = np.zeros_like(grid)

    for q, lp in active:
        a = math.log(q)
        w = lp / math.sqrt(q)
        tt = tent(h, grid-a)
        prime_field += w * tt
        self_density += (w*tt)**2

    background = 8*np.exp(grid/2) * (math.cosh(h/2)-1)
    discrepancy = prime_field - background

    total = float(np.trapezoid(discrepancy**2, grid))
    self_energy = float(np.trapezoid(self_density, grid))
    return total, self_energy, total-self_energy, len(active)


def zero_energy_partial(h, nzeros=100):
    s = mp.mpf("0")
    for n in range(1, nzeros+1):
        rho = mp.zetazero(n)
        gamma = mp.im(rho)
        c = (1-mp.cos(gamma*h))/(gamma**2)
        s += c*c
    return 8*s


def synthetic_mode_response(delta, tau, alpha, t):
    """
    Mode exp((delta+i*tau)t) filtered by variable centered second difference
    h(t)=exp(-alpha*t).
    Returns magnitude of exact multiplier times exp(delta*t).
    """
    h = math.exp(-alpha*t)
    lam = complex(delta, tau)
    mult = np.cosh(lam*h)-1
    return abs(mult) * math.exp(delta*t), h


if __name__ == "__main__":
    h = math.log(2)
    maxm = 8
    pps = prime_powers_below(math.exp(maxm+1+h))

    print("dyadic h =", h)
    print("self asymptotic coefficient h^3/3 =", h**3/3)

    for m in range(1, maxm+1):
        print(m, block_decomposition(m, h, pps))

    print("zero-side first100 mean-energy =", zero_energy_partial(mp.log(2), 100))

    for alpha in [0.0, 0.05, 0.25, 1.0]:
        val, aperture = synthetic_mode_response(
            delta=0.1, tau=14.0, alpha=alpha, t=40.0
        )
        print("alpha", alpha, "aperture", aperture, "response", val)
