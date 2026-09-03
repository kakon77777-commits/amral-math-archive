#!/usr/bin/env python3
"""
AMRAL RH v1.5 — canonical box-Toeplitz reference utilities.

REFERENCE ONLY. NOT A RIGOROUS RH CERTIFICATE ENGINE.

Core identities implemented:
    M_box[i,j] = 1/2 * (Psi(d+h) + Psi(d-h) - 2 Psi(d)),
    d = (i-j) h.

Prime-side finite-position identity:
    M_fin[i,j] = -1/2 sum_{n=p^k} Lambda(n)/sqrt(n)
                 * (T_h(d-log n) + T_h(d+log n)),
    T_h(x) = max(h-|x|,0).

For production:
- use MPFR/Arb outward intervals,
- prove prime enumeration completeness,
- certify transcendental functions and logs,
- use generalized Schur complements,
- attach hashes and independent recomputation.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable, List, Tuple

try:
    import numpy as np
except ImportError:
    np = None


def tent(h: float, x: float) -> float:
    if h <= 0:
        raise ValueError("h must be positive")
    return max(h - abs(x), 0.0)


def sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    mark = bytearray(b"\x01") * (limit + 1)
    mark[0:2] = b"\x00\x00"
    r = int(limit ** 0.5)
    for p in range(2, r + 1):
        if mark[p]:
            start = p * p
            mark[start:limit + 1:p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i in range(2, limit + 1) if mark[i]]


def prime_powers_below(xmax: float) -> List[Tuple[int, int, float]]:
    """
    Return tuples (n, p, Lambda(n)) for prime powers n=p^k < xmax.
    """
    if xmax <= 2:
        return []
    limit = int(math.floor(xmax - 1e-15))
    primes = sieve_primes(limit)
    out = []
    for p in primes:
        n = p
        lam = math.log(p)
        while n < xmax:
            out.append((n, p, lam))
            if n > limit // p:
                break
            n *= p
    out.sort(key=lambda t: t[0])
    return out


def box_matrix_from_psi(
    h: float,
    m: int,
    psi: Callable[[float], float],
):
    if np is None:
        raise RuntimeError("numpy is required")
    if h <= 0 or m < 1:
        raise ValueError("require h>0 and m>=1")

    M = np.zeros((m, m), dtype=float)
    for i in range(m):
        for j in range(m):
            d = (i - j) * h
            M[i, j] = 0.5 * (
                psi(d + h)
                + psi(d - h)
                - 2.0 * psi(d)
            )
    return M


def prime_finite_matrix(h: float, m: int):
    """
    Reference float implementation of the exact finite-position tent formula.

    Completeness cutoff:
        only prime powers n < exp(m*h) can contribute.
    """
    if np is None:
        raise RuntimeError("numpy is required")
    if h <= 0 or m < 1:
        raise ValueError("require h>0 and m>=1")

    cutoff = math.exp(m * h)
    pps = prime_powers_below(cutoff)

    M = np.zeros((m, m), dtype=float)
    for i in range(m):
        for j in range(m):
            d = (i - j) * h
            s = 0.0
            for n, p, lam in pps:
                a = math.log(n)
                weight = lam / math.sqrt(n)
                s += weight * (tent(h, d - a) + tent(h, d + a))
            M[i, j] = -0.5 * s
    return M, pps


def is_toeplitz(M, atol: float = 1e-12) -> bool:
    if np is None:
        raise RuntimeError("numpy is required")
    m, n = M.shape
    if m != n:
        return False
    for i in range(1, m):
        for j in range(1, m):
            if abs(M[i, j] - M[i - 1, j - 1]) > atol:
                return False
    return True


def schur_reserve(K, k, d: float) -> float:
    """
    Ordinary Schur reserve d - k^T K^{-1} k.
    Reference only; production should use rigorous linear algebra / pseudoinverse
    range conditions.
    """
    if np is None:
        raise RuntimeError("numpy is required")
    return float(d - k.T @ np.linalg.solve(K, k))


def toeplitz_innovation_reserve(M) -> float:
    """
    For a positive-definite Toeplitz prefix M of size >=2, return
    det(M_m)/det(M_{m-1}) through a Schur solve rather than determinants.
    """
    if np is None:
        raise RuntimeError("numpy is required")
    if M.shape[0] < 2 or M.shape[0] != M.shape[1]:
        raise ValueError("need square matrix of size >=2")

    K = M[:-1, :-1]
    k = M[:-1, -1]
    d = float(M[-1, -1])
    return schur_reserve(K, k, d)


def demo() -> None:
    if np is None:
        print("numpy unavailable; demo skipped")
        return

    h = 0.25
    m = 5
    Mfin, pps = prime_finite_matrix(h, m)

    print("h =", h, "m =", m)
    print("prime cutoff exp(mh) =", math.exp(m * h))
    print("prime powers used =", [(n, p) for n, p, _ in pps])
    print("M_fin:")
    np.set_printoptions(precision=10, suppress=True)
    print(Mfin)
    print("Toeplitz:", is_toeplitz(Mfin))


if __name__ == "__main__":
    demo()
