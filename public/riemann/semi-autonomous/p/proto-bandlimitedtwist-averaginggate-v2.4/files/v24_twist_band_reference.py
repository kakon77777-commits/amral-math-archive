#!/usr/bin/env python3
"""
AMRAL RH v2.4 — twisted local-band reference checks.

REFERENCE ONLY.

Checks:
1. direct twisted local discrepancy against pair-energy expansion
   on a finite prime-power sample;
2. closed twisted main factor against numerical integration;
3. generic large-sieve spacing-scale diagnostics.
"""

from __future__ import annotations
import math
import cmath
import numpy as np


def sieve_primes(limit: int):
    if limit < 2:
        return []
    mark = np.ones(limit + 1, dtype=bool)
    mark[:2] = False
    for p in range(2, int(limit**0.5)+1):
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


def tent(h: float, v):
    return np.maximum(h-np.abs(v), 0.0)


def main_factor(h: float, tau: float) -> complex:
    z = 0.5 - 1j*tau
    return 2.0*(cmath.cosh(z*h)-1.0)/(z*z)


def main_factor_numeric(h: float, tau: float, n=200000) -> complex:
    v = np.linspace(-h, h, n+1)
    vals = tent(h, v) * np.exp((0.5-1j*tau)*v)
    return complex(np.trapezoid(vals, v))


def twisted_observable(t: float, h: float, tau: float, pps):
    lo = math.exp(t-h)
    hi = math.exp(t+h)
    s = 0j
    x = math.exp(t)
    for q, lp in pps:
        if q <= lo:
            continue
        if q >= hi:
            break
        v = math.log(q)-t
        s += lp/math.sqrt(q) * (h-abs(v)) * cmath.exp(-1j*tau*v)
    s -= math.sqrt(x) * main_factor(h, tau)
    return s


def block_energy(T: float, h: float, tau: float, pps, samples=2001):
    grid = np.linspace(T, T+1, samples)
    vals = np.array(
        [twisted_observable(float(t), h, tau, pps) for t in grid],
        dtype=complex
    )
    return float(np.trapezoid(np.abs(vals)**2, grid))


def local_square_mass(T: float, h: float, pps):
    lo = math.exp(T-h)
    hi = math.exp(T+1+h)
    s = 0.0
    for q, lp in pps:
        if lo < q < hi:
            s += (lp*lp)/q
    return s


def generic_large_sieve_scale(T: float, h: float, pps):
    X = math.exp(T)
    coeff2 = local_square_mass(T, h, pps)
    return X * coeff2


if __name__ == "__main__":
    h = math.log(2.0)
    T = 5.0
    pps = prime_powers_below(math.exp(T+1+h)+2)

    for tau in [0.0, 1.0, 10.0, 30.0]:
        closed = main_factor(h, tau)
        numeric = main_factor_numeric(h, tau, n=50000)
        print("main", tau, closed, numeric, abs(closed-numeric))
        print("block energy", tau, block_energy(T,h,tau,pps,1001))

    print("local coeff square mass", local_square_mass(T,h,pps))
    print("generic large-sieve scale", generic_large_sieve_scale(T,h,pps))
