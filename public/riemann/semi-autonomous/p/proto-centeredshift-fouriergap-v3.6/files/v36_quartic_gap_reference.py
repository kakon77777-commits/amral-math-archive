#!/usr/bin/env python3
"""
AMRAL RH v3.6 — centered quartic-gap reference checks.

REFERENCE ONLY.

Checks:
1. V_N = quartic diagonal + semi-diagonal + genuine four-distinct remainder;
2. scale diagnostics;
3. finite-Euler-product samples of refined singular-series covariance K4.

Finite singular-series products are illustrative only.
"""

from __future__ import annotations
import math
import itertools
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


def von_mangoldt(limit: int):
    lam = np.zeros(limit + 1, dtype=float)
    for p in sieve_primes(limit):
        q = p
        lp = math.log(p)
        while q <= limit:
            lam[q] = lp
            if q > limit // p:
                break
            q *= p
    return lam


def twin_constant(prime_limit: int = 120000):
    prod = 1.0
    for p in sieve_primes(prime_limit):
        if p > 2:
            prod *= 1.0 - 1.0 / ((p - 1.0)**2)
    return prod


def singular_series_pair(h: int, C2: float):
    if h % 2:
        return 0.0
    n = h
    out = 2.0*C2
    p = 3
    while p*p <= n:
        if n % p == 0:
            out *= (p-1.0)/(p-2.0)
            while n % p == 0:
                n //= p
        p += 2
    if n > 2:
        out *= (n-1.0)/(n-2.0)
    return out


def endpoint_weight(N: int, n: int):
    if 1 <= n <= N:
        return float(N)
    if N < n < 2*N:
        return float(2*N-n)
    return 0.0


def compute_quartic(N: int, C2: float):
    limit = 2*N-1
    lam = von_mangoldt(limit)
    a = lam - 1.0
    a[0] = 0.0
    w = np.array([endpoint_weight(N,n) for n in range(limit+1)])

    H = 2*N-2
    R = np.zeros(H+1)

    diag4 = 0.0
    semi3 = 0.0

    # Store b arrays shift by shift only transiently.
    for h in range(1,H+1):
        mu = singular_series_pair(h,C2)-1.0
        n = np.arange(h+1,2*N)
        b = a[n]*a[n-h]-mu
        wn = w[n]

        R[h] = float(np.sum(wn*b))
        diag4 += float(np.sum((wn*wn)*(b*b)))

        # shared-index configuration m = n-h
        if h <= N-1:
            n2 = np.arange(2*h+1,2*N)
            m = n2-h
            b1 = a[n2]*a[n2-h]-mu
            b2 = a[m]*a[m-h]-mu
            semi3 += 2.0*float(np.sum(w[n2]*w[m]*b1*b2))

    V = float(np.sum(R[1:]**2))
    genuine4 = V-diag4-semi3

    return {
        "N": N,
        "V": V,
        "diag4": diag4,
        "semi3": semi3,
        "genuine4": genuine4,
        "reconstruction_residual": V-(diag4+semi3+genuine4),
        "V_over_N5": V/(N**5),
        "Q_over_N5": genuine4/(N**5),
        "V_over_N4log2": V/(N**4*math.log(N)**2),
        "Q_over_N4log2": genuine4/(N**4*math.log(N)**2),
        "D_over_N4log2": diag4/(N**4*math.log(N)**2),
    }


# ---- refined singular series finite-product illustrations ----

def singular_series_set(offsets, primes):
    offsets = tuple(sorted(set(int(x) for x in offsets)))
    k = len(offsets)
    if k <= 1:
        return 1.0

    prod = 1.0
    for p in primes:
        nu = len({x % p for x in offsets})
        factor = (1.0-nu/p)/((1.0-1.0/p)**k)
        prod *= factor
        if factor == 0.0:
            return 0.0
    return prod


def refined_singular_series(offsets, primes):
    offsets = tuple(offsets)
    k = len(offsets)
    total = 0.0
    for mask in range(1 << k):
        subset = [
            offsets[i]
            for i in range(k)
            if (mask >> i) & 1
        ]
        total += (
            (-1.0)**(k-len(subset))
            * singular_series_set(subset,primes)
        )
    return total


def K4_sample(h: int, d: int, primes):
    if h <= 0 or d <= 0 or h == d:
        raise ValueError("Need h,d positive and d != h.")

    pair0 = refined_singular_series([0,h],primes)
    four0 = refined_singular_series([0,h,d,d+h],primes)
    raw4 = singular_series_set([0,h,d,d+h],primes)
    return {
        "h": h,
        "d": d,
        "S0_pair": pair0,
        "S0_four": four0,
        "K4": four0-pair0*pair0,
        "S_four_raw": raw4,
    }


if __name__ == "__main__":
    C2 = twin_constant()
    for N in [100,250,500,1000]:
        d = compute_quartic(N,C2)
        print("quartic",d)

    ps = sieve_primes(5000)
    for h,d in [(2,4),(2,6),(4,6),(6,10),(3,5),(4,10),(6,12),(10,14)]:
        print("K4",K4_sample(h,d,ps))
