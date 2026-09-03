#!/usr/bin/env python3
"""
AMRAL RH v3.5 — arithmetic mean-square / centered shift residual checks.

REFERENCE ONLY.

Checks:
1. exact I(N) = J_N - sum A(j) + N/3;
2. exact diagonal + shift expansion of J_N;
3. singular-series-centered reconstruction;
4. Cauchy shift-L2 sufficient inequality;
5. positive-frequency Fourier coefficient identity.
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


def twin_constant(prime_limit: int = 200000):
    prod = 1.0
    for p in sieve_primes(prime_limit):
        if p > 2:
            prod *= 1.0 - 1.0 / ((p - 1.0)**2)
    return prod


def singular_series_pair(h: int, C2: float):
    if h == 0:
        raise ValueError("h=0 singular series not used here")
    if h % 2:
        return 0.0
    n = h
    result = 2.0 * C2
    p = 3
    while p * p <= n:
        if n % p == 0:
            result *= (p - 1.0) / (p - 2.0)
            while n % p == 0:
                n //= p
        p += 2
    if n > 2:
        result *= (n - 1.0) / (n - 2.0)
    return result


def endpoint_weight(N: int, n: int):
    if 1 <= n <= N:
        return float(N)
    if N < n < 2*N:
        return float(2*N - n)
    return 0.0


def W_mass_closed(N: int, h: int):
    if h < 0 or h > 2*N-2:
        return 0.0
    if h <= N:
        return N*(N-h) + N*(N-1)/2.0
    m = 2*N-h-1
    return m*(m+1)/2.0


def compute_all(N: int, C2: float):
    limit = 2*N - 1
    lam = von_mangoldt(limit)
    a = lam - 1.0
    a[0] = 0.0

    A = np.cumsum(a)
    js = np.arange(N, 2*N)
    J = float(np.sum(A[js]**2))
    linear = float(np.sum(A[js]))
    I_exact = J - linear + N/3.0

    w = np.array([endpoint_weight(N,n) for n in range(limit+1)])
    D = float(np.sum(w[1:] * a[1:]**2))

    H = 2*N-2
    C = np.zeros(H+1)
    W = np.zeros(H+1)
    S = np.zeros(H+1)
    R = np.zeros(H+1)

    for h in range(1,H+1):
        n = np.arange(h+1, 2*N)
        C[h] = float(np.sum(w[n] * a[n] * a[n-h]))
        W[h] = W_mass_closed(N,h)
        S[h] = singular_series_pair(h,C2)
        R[h] = C[h] - (S[h]-1.0)*W[h]

    M = float(np.sum((S[1:]-1.0)*W[1:]))
    Rsum = float(np.sum(R[1:]))
    reconstruct = D + 2*M + 2*Rsum

    V = float(np.sum(R[1:]**2))
    cauchy_rhs = math.sqrt(H)*math.sqrt(V)
    cauchy_lhs = abs(Rsum)

    return {
        "N": N,
        "J": J,
        "linear": linear,
        "I_exact": I_exact,
        "D": D,
        "M": M,
        "Rsum": Rsum,
        "reconstruct": reconstruct,
        "reconstruct_residual": reconstruct-J,
        "V": V,
        "cauchy_lhs": cauchy_lhs,
        "cauchy_rhs": cauchy_rhs,
        "cauchy_ratio": cauchy_lhs/cauchy_rhs if cauchy_rhs else 0.0,
        "C": C,
        "R": R,
        "W": W,
        "S": S,
        "a": a,
        "w": w,
    }


def fourier_coefficient_check(data, samples=None):
    """
    Check that positive Fourier coefficient h of
      G(alpha) conjugate(F(alpha))
    equals C_N(h).

    Uses exact DFT sampling with enough points to avoid aliasing.
    """
    N = data["N"]
    limit = 2*N-1
    if samples is None:
        samples = 8*N
    if samples <= 4*N:
        raise ValueError("Use samples > 4N to avoid aliasing.")

    a = data["a"]
    w = data["w"]
    coeff_F = np.zeros(samples, dtype=complex)
    coeff_G = np.zeros(samples, dtype=complex)

    # np.fft.ifft uses exp(+2 pi i kn/M) / M.
    coeff_F[:limit+1] = a[:limit+1]
    coeff_G[:limit+1] = w[:limit+1] * a[:limit+1]

    alpha_vals_F = samples * np.fft.ifft(coeff_F)
    alpha_vals_G = samples * np.fft.ifft(coeff_G)
    product = alpha_vals_G * np.conjugate(alpha_vals_F)

    # Fourier coefficient c_h for exp(+2pi i h alpha):
    coeff_product = np.fft.fft(product) / samples

    errs = []
    for h in range(1, min(20, 2*N-1)):
        errs.append(abs(coeff_product[h].real - data["C"][h]))
        errs.append(abs(coeff_product[h].imag))
    return max(errs) if errs else 0.0


if __name__ == "__main__":
    C2 = twin_constant(100000)
    print("C2 approx", C2)

    for N in [100, 250, 500, 1000]:
        d = compute_all(N,C2)
        ferr = fourier_coefficient_check(d)
        print(
            N,
            "I", d["I_exact"],
            "J", d["J"],
            "diag", d["D"],
            "main", d["M"],
            "Rsum", d["Rsum"],
            "recon", d["reconstruct_residual"],
            "V", d["V"],
            "CS ratio", d["cauchy_ratio"],
            "Fourier", ferr,
        )
