#!/usr/bin/env python3
"""
AMRAL RH v1.9 reference checks.

Checks:
1. direct triangular local-prime discrepancy;
2. compact FIR filter applied to normalized PNT error;
3. closed-form FIR autocorrelation kernel.

REFERENCE ONLY — not a rigorous RH certificate engine.
"""

from __future__ import annotations

import math
import bisect
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
    out.sort(key=lambda z: z[0])
    return out


class PsiTable:
    def __init__(self, xmax: float):
        self.pps = prime_powers_below(xmax)
        self.qs = [q for q, _ in self.pps]
        cumulative = []
        s = 0.0
        for q, lp in self.pps:
            s += lp
            cumulative.append(s)
        self.cumulative = cumulative

    def chebyshev_psi(self, x: float) -> float:
        k = bisect.bisect_right(self.qs, x)
        if k == 0:
            return 0.0
        return self.cumulative[k-1]

    def normalized_error(self, t: float) -> float:
        x = math.exp(t)
        return math.exp(-t/2) * (self.chebyshev_psi(x) - x)


def tent(h: float, v):
    return np.maximum(h - np.abs(v), 0.0)


def K_filter(h: float, v):
    v = np.asarray(v, dtype=float)
    out = np.zeros_like(v)
    left = (v > -h) & (v < 0)
    right = (v > 0) & (v < h)
    out[left] = 1.0 + 0.5*(h + v[left])
    out[right] = -1.0 + 0.5*(h - v[right])
    return out


def direct_discrepancy(t: float, h: float, table: PsiTable) -> float:
    lo = math.exp(t-h)
    hi = math.exp(t+h)
    s = 0.0
    for q, lp in table.pps:
        if q <= lo:
            continue
        if q >= hi:
            break
        s += lp/math.sqrt(q) * (h - abs(t-math.log(q)))
    main = 8*math.exp(t/2)*(math.cosh(h/2)-1)
    return s-main


def fir_discrepancy(t: float, h: float, table: PsiTable, order: int = 24) -> float:
    """
    Piecewise Gauss-Legendre integration. Breakpoints include all
    normalized-error jumps v=t-log(q) inside [-h,h] and the filter kink 0.
    """
    pts = [-h, 0.0, h]
    for q, _ in table.pps:
        v = t-math.log(q)
        if -h < v < h:
            pts.append(v)
    pts = sorted(set(pts))

    nodes, weights = np.polynomial.legendre.leggauss(order)
    total = 0.0

    for a, b in zip(pts[:-1], pts[1:]):
        if b-a < 1e-14:
            continue
        mid = 0.5*(a+b)
        rad = 0.5*(b-a)
        vs = mid + rad*nodes
        kvals = K_filter(h, vs)
        evals = np.array([table.normalized_error(t-v) for v in vs])
        total += rad * float(np.dot(weights, kvals*evals))
    return total


def A_sign(h: float, d: float) -> float:
    r = abs(d)
    if r >= 2*h:
        return 0.0
    if r <= h:
        return 2*h - 3*r
    return r - 2*h


def C_tent(h: float, d: float) -> float:
    r = abs(d)
    if r >= 2*h:
        return 0.0
    if r <= h:
        return 2*h**3/3 - h*r*r + r**3/2
    return (2*h-r)**3/6


def H_closed(h: float, d: float) -> float:
    return A_sign(h, d) + 0.25*C_tent(h, d)


def H_numeric(h: float, d: float, order: int = 8) -> float:
    """
    Piecewise Gauss-Legendre integration. The integrand is piecewise
    quadratic; splitting at every K-filter kink removes jump-integration
    artifacts.
    """
    lo = max(-h, d-h)
    hi = min(h, d+h)
    if lo >= hi:
        return 0.0

    pts = [lo, hi]
    for p in (-h, 0.0, h, d-h, d, d+h):
        if lo < p < hi:
            pts.append(p)
    pts = sorted(set(pts))

    nodes, weights = np.polynomial.legendre.leggauss(order)
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        mid = 0.5*(a+b)
        rad = 0.5*(b-a)
        x = mid + rad*nodes
        y = K_filter(h, x) * K_filter(h, x-d)
        total += rad * float(np.dot(weights, y))
    return total


def demo():
    h = math.log(2)
    tmax = 6.0
    table = PsiTable(math.exp(tmax+h)+2)

    print("FIR identity:")
    for t in [1.2, 2.0, 3.3, 4.7, 5.8]:
        a = direct_discrepancy(t, h, table)
        b = fir_discrepancy(t, h, table)
        print(t, a, b, "residual", a-b)

    print("Kernel identity:")
    for d in [0, h/2, h, 1.5*h, 2*h]:
        a = H_closed(h, d)
        b = H_numeric(h, d, order=8)
        print(d, a, b, "residual", a-b)


if __name__ == "__main__":
    demo()
