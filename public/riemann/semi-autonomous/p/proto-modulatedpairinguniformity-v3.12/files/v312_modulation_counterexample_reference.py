#!/usr/bin/env python3
"""
AMRAL RH v3.12 — modulation counterexample / constraint-centering checks.

REFERENCE ONLY.

Checks:
1. q=2 pointwise resonant remainder scales as H^4;
2. normalized character-averaged remainder equals additive energy and scales as H^3;
3. finite-q constrained centering means;
4. double-centered K_perp has both Fourier axes zero;
5. K_perp is symmetric.

No RH or fixed-power prime theorem is claimed.
"""

from __future__ import annotations

import math
import numpy as np


def bump_values(H: int):
    n = np.arange(1, H, dtype=float)
    x = n / H
    c = np.exp(-1.0 / (x * (1.0 - x)))
    return c


def q2_resonant_remainder(H: int):
    c = bump_values(H)
    E0 = float(np.sum(c))
    return -2.0 * E0**4, E0


def q2_averaged_remainder(H: int):
    c = bump_values(H)
    conv = np.convolve(c, c)
    additive_energy = float(np.sum(conv * conv))
    return -2.0 * additive_energy, additive_energy


def direct_character_average(H: int):
    """
    Directly check average |E(1/2+j/M)|^4 = additive energy.
    M > additive support diameter.
    """
    c = bump_values(H)
    n = np.arange(1, H, dtype=float)
    M = 4 * H + 1

    total = 0.0
    for j in range(M):
        x = 0.5 + j / M
        E = np.sum(c * np.exp(2j * math.pi * n * x))
        total += abs(E)**4

    direct = total / M
    conv = np.convolve(c, c)
    energy = float(np.sum(conv * conv))
    return direct, energy, abs(direct - energy)


def prime_factors_squarefree(q: int):
    out = []
    n = q
    p = 2
    while p * p <= n:
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


def coefficient_table(q: int):
    rho = rho_array(q)
    coeff = np.zeros((q, q), dtype=complex)

    for b in range(q):
        Bp = rho * np.roll(rho, -b)
        Bm = rho * np.roll(rho, +b)
        coeff[:, b] = np.fft.ifft(
            np.fft.fft(Bm) * np.fft.fft(Bp)
        )

    # Pair-square centering removes beta=0 exactly.
    coeff[:, 0] = 0.0
    return coeff


def physical_K4(q: int):
    coeff = coefficient_table(q)
    return (q * q * np.fft.ifft2(coeff)).real, coeff


def pair_mu(q: int):
    rho = rho_array(q)
    a = rho * rho
    return (q * np.fft.ifft(a)).real


def A_minus_one(q: int):
    A = 1.0
    for p in prime_factors_squarefree(q):
        A *= 1.0 + 1.0 / ((p - 1.0)**3)
    return A - 1.0


def constrained_centering_stats(q: int):
    K, coeff = physical_K4(q)
    mu = pair_mu(q)
    A1 = A_minus_one(q)

    mu_d2 = np.tile(mu**2, (q, 1))

    P3 = np.empty((q, q), dtype=float)
    for h in range(q):
        for d in range(q):
            P3[h, d] = (
                mu[(h + d) % q]
                * mu[(h - d) % q]
            )

    # K = S0 - mu_h^2.
    # Full Wick-connected C4 = K - mu_d^2 - P3.
    C4 = K - mu_d2 - P3

    # Constraint-adapted double centering.
    Kperp = K - (mu_d2 - A1)
    Kperp_hat = np.fft.fft2(Kperp) / (q * q)

    predicted_p3 = 1.0 if q % 2 == 0 else 0.0
    predicted_C4 = -A1 - predicted_p3

    return {
        "q": q,
        "A_minus_one": A1,
        "mean_K4": float(np.mean(K)),
        "mean_P3": float(np.mean(P3)),
        "predicted_mean_P3": predicted_p3,
        "mean_C4": float(np.mean(C4)),
        "predicted_mean_C4": predicted_C4,
        "Kperp_alpha0_axis": float(
            np.max(np.abs(Kperp_hat[0, :]))
        ),
        "Kperp_beta0_axis": float(
            np.max(np.abs(Kperp_hat[:, 0]))
        ),
        "Kperp_symmetry": float(
            np.max(np.abs(Kperp - Kperp.T))
        ),
    }


if __name__ == "__main__":
    for H in [16, 32, 64, 128, 256]:
        point, E0 = q2_resonant_remainder(H)
        avg, energy = q2_averaged_remainder(H)
        print(
            "scale",
            H,
            "E0/H", E0 / H,
            "point/H4", point / H**4,
            "avg/H3", avg / H**3,
        )

    direct, energy, err = direct_character_average(16)
    print("character-average", direct, energy, err)

    for q in [2, 3, 6, 15, 30, 210]:
        print("centering", constrained_centering_stats(q))
