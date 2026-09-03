#!/usr/bin/env python3
"""
AMRAL RH v3.8 — parallelogram rational-tail reference checks.

REFERENCE ONLY.

Checks:
1. finite-q coefficient formula vs direct finite Euler-product K4 FFT;
2. entire beta=0 Fourier axis cancellation;
3. alpha=0 surviving pair-axis identity;
4. exact Omega_N Fourier transform formula;
5. finite-q d-Sobolev diagnostics.

No full fixed-power high-conductor bound is claimed.
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


def raw_S_q(offsets, q: int) -> float:
    ps = prime_factors_squarefree(q)
    k = len(offsets)
    if k <= 1:
        return 1.0

    out = 1.0
    for p in ps:
        nu = len({int(x) % p for x in offsets})
        out *= (
            (1.0-nu/p)
            / ((1.0-1.0/p)**k)
        )
    return out


def refined_S0_q(offsets, q: int) -> float:
    offsets = list(offsets)
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
            * raw_S_q(subset,q)
        )
    return total


def K4_q_value(h: int, d: int, q: int) -> float:
    s04 = refined_S0_q([0,h,d,h+d],q)
    mu = raw_S_q([0,h],q)-1.0
    return s04-mu*mu


def direct_K4_table(q: int):
    arr = np.empty((q,q),dtype=float)
    for h in range(q):
        for d in range(q):
            arr[h,d] = K4_q_value(h,d,q)
    return arr


def rho_array(q: int):
    rho = np.zeros(q,dtype=float)

    for k in range(1,q):
        r = q // math.gcd(k,q)
        ps = prime_factors_squarefree(r)
        mu = -1.0 if len(ps) % 2 else 1.0

        phi = r
        for p in ps:
            phi = phi // p * (p-1)

        rho[k] = mu / phi

    return rho


def coefficient_table_from_rho(q: int):
    """
    Returns normalized Fourier coefficients c(alpha,beta)
    in K(h,d)=sum c(a,b)e((ah+bd)/q).
    """
    rho = rho_array(q)
    coeff = np.zeros((q,q),dtype=complex)

    for b in range(q):
        Bp = rho * np.roll(rho,-b)
        Bm = rho * np.roll(rho,+b)

        # circular convolution
        conv = np.fft.ifft(
            np.fft.fft(Bm)
            * np.fft.fft(Bp)
        )

        coeff[:,b] = conv

    # pair square exactly removes entire b=0 axis
    coeff[:,0] = 0.0
    return coeff


def endpoint_weight(N: int, n: int):
    if 1 <= n <= N:
        return float(N)
    if N < n < 2*N:
        return float(2*N-n)
    return 0.0


def omega_weight(N: int, h: int, d: int):
    if h < 1 or d < 1 or h+d > 2*N-2:
        return 0.0

    total = 0.0
    for r in range(1,2*N-h-d):
        total += (
            endpoint_weight(N,r+h)
            * endpoint_weight(N,r+h+d)
        )
    return total


def omega_transform_direct(N: int, alpha: float, beta: float):
    total = 0j
    for h in range(1,2*N-1):
        for d in range(1,2*N-1-h):
            Om = omega_weight(N,h,d)
            total += (
                Om
                * np.exp(
                    2j*math.pi*(h*alpha+d*beta)
                )
            )
    return total


def E_sum(M: int, alpha: float):
    if M <= 0:
        return 0j
    j = np.arange(1,M+1,dtype=float)
    return np.sum(np.exp(2j*math.pi*j*alpha))


def omega_transform_formula(N: int, alpha: float, beta: float):
    total = 0j

    for n in range(2,2*N):
        wn = endpoint_weight(N,n)
        if wn == 0:
            continue

        En = E_sum(n-1,alpha)

        for m in range(n+1,2*N):
            wm = endpoint_weight(N,m)
            if wm == 0:
                continue

            total += (
                wn*wm
                * np.exp(
                    2j*math.pi*(m-n)*beta
                )
                * En
            )

    return total


def d_sobolev_norm(q: int):
    coeff = coefficient_table_from_rho(q)
    total = 0.0

    for b in range(1,q):
        den = abs(
            1.0
            -
            np.exp(2j*math.pi*b/q)
        )**2

        total += (
            np.sum(np.abs(coeff[:,b])**2)
            / den
        )

    return float(total)


def axis_alpha0_residual(q: int):
    rho = rho_array(q)
    coeff = coefficient_table_from_rho(q)

    max_res = 0.0
    for b in range(1,q):
        expected = np.sum(
            (rho*rho)
            * np.roll(rho*rho,-b)
        )
        max_res = max(
            max_res,
            abs(coeff[0,b]-expected)
        )
    return float(max_res)


if __name__ == "__main__":
    for q in [6,30,210]:
        arr = direct_K4_table(q)
        direct_coeff = np.fft.fft2(arr)/(q*q)
        formula_coeff = coefficient_table_from_rho(q)

        print(
            "q",q,
            "coeff residual",
            np.max(np.abs(direct_coeff-formula_coeff)),
            "beta0",
            np.max(np.abs(formula_coeff[:,0])),
            "row mean",
            np.max(np.abs(arr.mean(axis=1))),
            "alpha0 residual",
            axis_alpha0_residual(q),
            "sobolev",
            d_sobolev_norm(q),
        )

    for q in [2310]:
        print(
            "q",q,
            "sobolev",
            d_sobolev_norm(q),
        )

    N=12
    for a,b in [
        (1/5,1/7),
        (0.0,1/7),
        (1/5,2/11),
    ]:
        d = omega_transform_direct(N,a,b)
        f = omega_transform_formula(N,a,b)
        print("Omega",a,b,d,f,d-f)
