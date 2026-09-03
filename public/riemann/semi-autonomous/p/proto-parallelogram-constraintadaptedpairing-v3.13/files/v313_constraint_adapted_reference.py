#!/usr/bin/env python3
"""
AMRAL RH v3.13 — constraint-adapted axis / 2D remainder checks.

REFERENCE ONLY.

Checks:
1. axis Sobolev norm;
2. mixed axis-free Sobolev norm;
3. mixed double antiderivative;
4. exact sharp-weight double summation by parts;
5. exact axis one-direction summation by parts.

No infinite-conductor finite-box theorem is claimed.
"""

from __future__ import annotations

import math
import numpy as np


def prime_factors_squarefree(q: int):
    out = []
    n = q
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            n //= p
            if n % p == 0:
                raise ValueError("q must be squarefree")
        p += 1
    if n > 1:
        out.append(n)
    return out


def rho_array(q: int):
    rho = np.zeros(q, dtype=float)
    for k in range(1, q):
        r = q // math.gcd(k, q)
        ps = prime_factors_squarefree(r)
        mu = -1.0 if len(ps) % 2 else 1.0
        phi = r
        for p in ps:
            phi = phi // p * (p - 1)
        rho[k] = mu / phi
    return rho


def covariance_coeff(q: int):
    rho = rho_array(q)
    coeff = np.zeros((q, q), dtype=complex)

    for b in range(q):
        Bp = rho * np.roll(rho, -b)
        Bm = rho * np.roll(rho, +b)
        coeff[:, b] = np.fft.ifft(
            np.fft.fft(Bm) * np.fft.fft(Bp)
        )

    # Original K4 centering removes beta=0.
    coeff[:, 0] = 0.0
    return coeff


def axis_coeff(q: int):
    coeff = covariance_coeff(q)
    out = np.zeros(q, dtype=complex)
    out[1:] = coeff[0, 1:]
    return out


def kperp_coeff(q: int):
    coeff = covariance_coeff(q)
    # Remove the entire alpha=0 axis too.
    coeff[0, :] = 0.0
    return coeff


def axis_sobolev(q: int):
    a = axis_coeff(q)
    total = 0.0
    for b in range(1, q):
        den = abs(
            1.0 - np.exp(2j*math.pi*b/q)
        )**2
        total += abs(a[b])**2 / den
    return float(total)


def mixed_sobolev(q: int):
    c = kperp_coeff(q)
    den = np.array([
        abs(
            1.0 - np.exp(2j*math.pi*k/q)
        )**2
        for k in range(q)
    ])
    total = 0.0
    for a in range(1, q):
        total += np.sum(
            np.abs(c[a, 1:])**2
            / (
                den[a] * den[1:]
            )
        )
    return float(total)


def mixed_antiderivative(q: int):
    c = kperp_coeff(q)
    gc = np.zeros_like(c)

    for a in range(1, q):
        da = np.exp(2j*math.pi*a/q) - 1.0
        for b in range(1, q):
            db = np.exp(2j*math.pi*b/q) - 1.0
            gc[a, b] = c[a, b] / (da * db)

    K = (q*q*np.fft.ifft2(c)).real
    G = (q*q*np.fft.ifft2(gc)).real
    return K, G, gc


def axis_antiderivative(q: int):
    a = axis_coeff(q)
    bc = np.zeros(q, dtype=complex)
    for b in range(1, q):
        bc[b] = a[b] / (
            np.exp(2j*math.pi*b/q) - 1.0
        )
    A = (q*np.fft.ifft(a)).real
    B = (q*np.fft.ifft(bc)).real
    return A, B


def endpoint_weight(N: int, n: int):
    if 1 <= n <= N:
        return float(N)
    if N < n < 2*N:
        return float(2*N - n)
    return 0.0


def omega_weight(N: int, h: int, d: int):
    if h < 1 or d < 1 or h+d > 2*N-2:
        return 0.0

    total = 0.0
    for r in range(1, 2*N-h-d):
        total += (
            endpoint_weight(N, r+h)
            * endpoint_weight(N, r+h+d)
        )
    return total


def omega_array(N: int):
    size = 2*N + 2
    W = np.zeros((size, size), dtype=float)
    for h in range(size):
        for d in range(size):
            W[h, d] = omega_weight(N, h, d)
    return W


def mixed_backward_difference(W):
    out = np.zeros_like(W)

    for h in range(W.shape[0]):
        for d in range(W.shape[1]):
            out[h, d] = W[h, d]

            if h > 0:
                out[h, d] -= W[h-1, d]
            if d > 0:
                out[h, d] -= W[h, d-1]
            if h > 0 and d > 0:
                out[h, d] += W[h-1, d-1]

    return out


def double_sbp_check(N: int, q: int):
    K, G, _gc = mixed_antiderivative(q)
    W = omega_array(N)
    D2 = mixed_backward_difference(W)

    direct = 0.0
    sbp = 0.0

    for h in range(W.shape[0]):
        for d in range(W.shape[1]):
            direct += W[h, d] * K[h % q, d % q]
            sbp += D2[h, d] * G[h % q, d % q]

    return {
        "N": N,
        "q": q,
        "direct": direct,
        "sbp": sbp,
        "residual": direct-sbp,
        "mixed_diff_l2": float(
            np.sqrt(np.sum(D2*D2))
        ),
        "G_box_l2": float(
            np.sqrt(sum(
                G[h % q, d % q]**2
                for h in range(W.shape[0])
                for d in range(W.shape[1])
            ))
        ),
    }


def axis_sbp_check(N: int, q: int):
    A, B = axis_antiderivative(q)
    W = omega_array(N)
    Xi = np.sum(W, axis=0)

    dXi = np.zeros_like(Xi)
    for d in range(len(Xi)):
        dXi[d] = Xi[d] - (
            Xi[d-1] if d > 0 else 0.0
        )

    direct = sum(
        Xi[d] * A[d % q]
        for d in range(len(Xi))
    )

    sbp = -sum(
        dXi[d] * B[d % q]
        for d in range(len(Xi))
    )

    return {
        "N": N,
        "q": q,
        "direct": direct,
        "sbp": sbp,
        "residual": direct-sbp,
        "dXi_l2": float(
            np.sqrt(np.sum(dXi*dXi))
        ),
        "B_interval_l2": float(
            np.sqrt(sum(
                B[d % q]**2
                for d in range(len(Xi))
            ))
        ),
    }


if __name__ == "__main__":
    for q in [6, 30, 210, 2310]:
        print(
            "sobolev",
            q,
            axis_sobolev(q),
            mixed_sobolev(q),
        )

    for N, q in [
        (10, 6),
        (20, 6),
        (20, 30),
    ]:
        print("double", double_sbp_check(N, q))
        print("axis", axis_sbp_check(N, q))
