#!/usr/bin/env python3
"""
vRH 1.65 independent normalization audit.

Compares three representations of the fixed-aperture observable:

A. Direct Suzuki Psi formula, then centered second difference.
B. Local prime-tent formula + archimedean second difference.
C. Adjacent-block cumulative-prime identity.

REFERENCE / SANITY CHECK ONLY.
Not a rigorous RH proof engine.
"""

from __future__ import annotations

import math
import csv
import mpmath as mp

mp.mp.dps = 70


def sieve_primes(n: int):
    if n < 2:
        return []
    mark = bytearray(b"\x01") * (n + 1)
    mark[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if mark[p]:
            mark[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if mark[i]]


def prime_powers_below(xmax: float):
    limit = max(2, int(math.floor(xmax)))
    out = []
    for p in sieve_primes(limit):
        q = p
        lp = mp.log(p)
        while q < xmax:
            out.append((q, lp))
            if q > limit // p:
                break
            q *= p
    out.sort(key=lambda z: z[0])
    return out


def ramp_prime_sum(t):
    t = mp.mpf(t)
    xmax = float(mp.e**t) + 1.0
    total = mp.mpf("0")
    for n, lp in prime_powers_below(xmax):
        if mp.mpf(n) <= mp.e**t:
            total += lp / mp.sqrt(n) * (t - mp.log(n))
    return total


def psi_suzuki(t):
    t = abs(mp.mpf(t))
    if t == 0:
        return mp.mpf("0")

    C = mp.pi**2 + 8 * mp.catalan
    return (
        4 * (mp.e**(t/2) + mp.e**(-t/2) - 2)
        - ramp_prime_sum(t)
        + t/2 * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
        + mp.mpf("0.25") * (
            C
            - mp.e**(-t/2)
            * mp.lerchphi(mp.e**(-2*t), 2, mp.mpf("0.25"))
        )
    )


def arch_suzuki(t):
    t = abs(mp.mpf(t))
    C = mp.pi**2 + 8 * mp.catalan
    return (
        4 * (mp.e**(t/2) + mp.e**(-t/2) - 2)
        + t/2 * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
        + mp.mpf("0.25") * (
            C
            - mp.e**(-t/2)
            * mp.lerchphi(mp.e**(-2*t), 2, mp.mpf("0.25"))
        )
    )


def d_direct(t, h):
    return mp.mpf("0.5") * (
        psi_suzuki(t+h) + psi_suzuki(t-h) - 2*psi_suzuki(t)
    )


def local_tent_sum(t, h):
    t = mp.mpf(t)
    h = mp.mpf(h)
    lo = mp.e**(t-h)
    hi = mp.e**(t+h)
    total = mp.mpf("0")
    for n, lp in prime_powers_below(float(hi) + 1.0):
        nmp = mp.mpf(n)
        if lo < nmp < hi:
            total += (
                lp / mp.sqrt(nmp)
                * (h - abs(t - mp.log(nmp)))
            )
    return total


def d_local(t, h):
    arch = mp.mpf("0.5") * (
        arch_suzuki(t+h) + arch_suzuki(t-h) - 2*arch_suzuki(t)
    )
    return arch - mp.mpf("0.5") * local_tent_sum(t, h)


def cumulative_integral(a, b):
    """
    Integral_a^b S(y)/y dy with
    S(y)=sum_{n<=y} Lambda(n)/sqrt(n).

    Exact step-function integration:
      sum_{n<b} w_n * log(b/max(a,n)).
    """
    a = mp.mpf(a)
    b = mp.mpf(b)
    total = mp.mpf("0")
    for n, lp in prime_powers_below(float(b) + 1.0):
        nmp = mp.mpf(n)
        if nmp >= b:
            continue
        lower = max(a, nmp)
        if lower < b:
            total += lp / mp.sqrt(nmp) * mp.log(b/lower)
    return total


def local_sum_from_blocks(t, h):
    x = mp.e**mp.mpf(t)
    eh = mp.e**mp.mpf(h)
    return (
        cumulative_integral(x, x*eh)
        - cumulative_integral(x/eh, x)
    )


def run_tests():
    cases = []
    hs = [mp.log(2), mp.mpf("0.4"), mp.mpf("1.1")]
    for h in hs:
        ts = [h + mp.mpf("0.2"), mp.mpf("3.7"), mp.mpf("6.2")]
        for t in ts:
            if t <= h:
                continue
            da = d_direct(t, h)
            db = d_local(t, h)
            lt = local_tent_sum(t, h)
            lb = local_sum_from_blocks(t, h)
            cases.append({
                "h": mp.nstr(h, 30),
                "t": mp.nstr(t, 30),
                "D_direct": mp.nstr(da, 50),
                "D_local": mp.nstr(db, 50),
                "D_residual": mp.nstr(da-db, 20),
                "L_tent": mp.nstr(lt, 50),
                "L_block": mp.nstr(lb, 50),
                "L_residual": mp.nstr(lt-lb, 20),
            })
    return cases


if __name__ == "__main__":
    cases = run_tests()
    for row in cases:
        print(row)
