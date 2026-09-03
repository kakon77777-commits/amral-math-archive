#!/usr/bin/env python3
"""
AMRAL RH v1.6 — fixed-aperture local-prime reference implementation.

REFERENCE ONLY. NOT A RIGOROUS RH CERTIFICATE ENGINE.

Implements:
- Suzuki smooth term A(t) in the simplified exponential-series form,
- local prime-power tent sum L_h(t),
- fixed-aperture observable D_h(t),
- local discrepancy E_h(t),
- conservative service-curvature threshold,
- prime event triplets,
- real Levinson/Durbin reflection recursion for a supplied Toeplitz sequence.

Production requirements:
- MPFR/Arb outward rounding,
- exact prime-power enumeration completeness,
- independent implementation,
- formal theorem validation.
"""

from __future__ import annotations

import math
from typing import List, Tuple

try:
    import mpmath as mp
except ImportError as exc:
    raise SystemExit("mpmath is required") from exc


mp.mp.dps = 60


def sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    mark = bytearray(b"\x01") * (limit + 1)
    mark[0:2] = b"\x00\x00"
    r = int(limit ** 0.5)
    for p in range(2, r + 1):
        if mark[p]:
            start = p * p
            mark[start:limit + 1:p] = (
                b"\x00" * (((limit - start) // p) + 1)
            )
    return [i for i in range(2, limit + 1) if mark[i]]


def prime_powers_below(xmax: float) -> List[Tuple[int, int, float]]:
    """
    (q, p, Lambda(q)) for q=p^k < xmax.
    """
    if xmax <= 2:
        return []
    limit = int(math.floor(xmax))
    out: List[Tuple[int, int, float]] = []
    for p in sieve_primes(limit):
        q = p
        lam = math.log(p)
        while q < xmax:
            out.append((q, p, lam))
            if q > limit // p:
                break
            q *= p
    out.sort(key=lambda item: item[0])
    return out


def arch_constants():
    C = mp.pi**2 + 8 * mp.catalan
    c = mp.mpf("0.5") * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
    return c, C


def arch_smooth(t, terms: int = 2000):
    """
    Simplified Suzuki smooth term for t>0:
      A(t)=4 e^(t/2)-8+c t+C/4
           -sum_{m>=1} e^{-(2m+1/2)t}/(2m+1/2)^2.
    At t=0 return the continuous value 0.
    """
    t = mp.mpf(t)
    if t == 0:
        return mp.mpf("0")
    if t < 0:
        raise ValueError("arch_smooth expects t>=0")

    c, C = arch_constants()
    s = mp.mpf("0")
    for m in range(1, terms + 1):
        a = 2 * m + mp.mpf("0.5")
        term = mp.e ** (-a * t) / (a * a)
        s += term
        if abs(term) < mp.mpf("1e-70"):
            break
    return 4 * mp.e ** (t / 2) - 8 + c * t + C / 4 - s


def tent(h, x):
    h = mp.mpf(h)
    x = mp.mpf(x)
    return max(h - abs(x), mp.mpf("0"))


def local_prime_sum(t, h):
    """
    L_h(t) = sum Lambda(n)/sqrt(n) * T_h(t-log n).
    Only prime powers exp(t-h)<n<exp(t+h) can contribute.
    Float sieve boundaries make this a reference implementation only.
    """
    t = mp.mpf(t)
    h = mp.mpf(h)
    if t < h:
        raise ValueError("reference formula assumes t>=h")

    lo = mp.e ** (t - h)
    hi = mp.e ** (t + h)

    total = mp.mpf("0")
    for q, p, lam in prime_powers_below(float(hi)):
        qmp = mp.mpf(q)
        if qmp <= lo:
            continue
        u = mp.log(qmp)
        w = mp.mpf(lam) / mp.sqrt(qmp)
        total += w * tent(h, t - u)
    return total


def R_h(t, h):
    t = mp.mpf(t)
    h = mp.mpf(h)
    if t < h:
        raise ValueError("require t>=h")
    return mp.mpf("0.5") * (
        arch_smooth(t + h)
        + arch_smooth(t - h)
        - 2 * arch_smooth(t)
    )


def D_h(t, h):
    return R_h(t, h) - mp.mpf("0.5") * local_prime_sum(t, h)


def main_density(t, h):
    t = mp.mpf(t)
    h = mp.mpf(h)
    return 8 * mp.e ** (t / 2) * (mp.cosh(h / 2) - 1)


def local_discrepancy(t, h):
    return local_prime_sum(t, h) - main_density(t, h)


def trivial_correction(t, h, terms: int = 2000):
    """
    Remainder Rcal_h(t) >= 0 such that
       D_h(t) = -1/2 E_h(t) - Rcal_h(t).
    """
    t = mp.mpf(t)
    h = mp.mpf(h)
    s = mp.mpf("0")
    for m in range(1, terms + 1):
        a = 2 * m + mp.mpf("0.5")
        term = (
            mp.e ** (-a * t)
            * (mp.cosh(a * h) - 1)
            / (a * a)
        )
        s += term
        if abs(term) < mp.mpf("1e-70"):
            break
    return s


def service_curvature(t, h, terms: int = 2000):
    """
    R_h''(t) exact exponential-series evaluation.
    """
    t = mp.mpf(t)
    h = mp.mpf(h)
    s = mp.e ** (t / 2) * (mp.cosh(h / 2) - 1)
    for m in range(1, terms + 1):
        a = 2 * m + mp.mpf("0.5")
        term = mp.e ** (-a * t) * (mp.cosh(a * h) - 1)
        s -= term
        if abs(term) < mp.mpf("1e-70"):
            break
    return s


def service_threshold(h):
    h = mp.mpf(h)
    c_h = mp.cosh(h / 2) - 1
    return max(
        h + mp.log(2) / 2,
        ((mp.mpf("2.5") * h) - mp.log(c_h)) / 3,
    )


def event_triplet(q: int, p: int):
    """
    Returns (log q, weight) only; caller adds +/- h event offsets.
    """
    a = math.log(q)
    w = math.log(p) / math.sqrt(q)
    return a, w


def levinson_real(r: List[float]):
    """
    Real Levinson/Durbin recursion for a positive-definite Toeplitz
    autocorrelation sequence r[0..n].

    Convention:
      kappa_i = (r[i] - sum_{j=1}^{i-1} a_j r[i-j]) / E_{i-1}
      E_i = E_{i-1} (1-kappa_i^2)

    Returns reflection coefficients and innovation errors.
    Reference float arithmetic only.
    """
    if not r or r[0] <= 0:
        raise ValueError("r[0] must be positive")

    order = len(r) - 1
    a = [0.0] * (order + 1)
    E = float(r[0])
    kappas = []
    errors = [E]

    for i in range(1, order + 1):
        acc = sum(a[j] * r[i - j] for j in range(1, i))
        kappa = (r[i] - acc) / E
        old = a.copy()
        for j in range(1, i):
            a[j] = old[j] - kappa * old[i - j]
        a[i] = kappa
        E = E * (1.0 - kappa * kappa)
        kappas.append(kappa)
        errors.append(E)

    return kappas, errors


def demo():
    h = mp.log(2)
    t = mp.mpf("5.0")

    D = D_h(t, h)
    E = local_discrepancy(t, h)
    R = trivial_correction(t, h)
    identity_residual = D - (-mp.mpf("0.5") * E - R)

    print("h=log 2")
    print("main coefficient =", 8 * (mp.cosh(h / 2) - 1))
    print("6sqrt(2)-8      =", 6 * mp.sqrt(2) - 8)
    print("D_h(5)          =", D)
    print("local discrepancy=", E)
    print("trivial correction=", R)
    print("identity residual =", identity_residual)
    print("service threshold =", service_threshold(h))
    print("curvature at threshold+0.1 =",
          service_curvature(service_threshold(h) + mp.mpf("0.1"), h))


if __name__ == "__main__":
    demo()
