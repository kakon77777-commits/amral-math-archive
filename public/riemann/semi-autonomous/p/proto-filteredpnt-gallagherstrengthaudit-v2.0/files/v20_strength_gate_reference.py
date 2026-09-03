#!/usr/bin/env python3
"""
AMRAL RH v2.0 strength-gate reference calculations.

Illustrates asymptotic energy classes only.
This is NOT a rigorous numerical PNT bound or RH certificate.
"""

from __future__ import annotations
import math


A0 = 1.0 / 48.0718


def d_constant(A0=A0):
    return ((5**6 * A0**3) / (2**2 * 3**4)) ** (1.0 / 5.0)


def Omega(T, A0=A0):
    if T <= 1:
        return 0.0
    return d_constant(A0) * T**0.6 / (math.log(T)**0.2)


def vk_energy_log_bound(T):
    """
    Logarithm of the asymptotic energy envelope:
       exp(T - 2 Omega(T)).
    Implicit constants and lower-order terms omitted.
    """
    return T - 2.0 * Omega(T)


def effective_beta(T):
    return vk_energy_log_bound(T) / T


def zero_strip_from_beta(beta):
    return beta / 2.0


def fixed_saving_beta(epsilon):
    return 1.0 - epsilon


if __name__ == "__main__":
    print("A0 =", A0)
    print("d  =", d_constant())
    print()
    for T in [100, 1_000, 10_000, 100_000, 1_000_000]:
        beta = effective_beta(T)
        print(
            "T=", T,
            "Omega=", Omega(T),
            "effective beta=", beta,
            "strip half-width=", zero_strip_from_beta(beta),
        )
    print()
    for eps in [0.01, 0.05, 0.1, 0.25, 0.5]:
        beta = fixed_saving_beta(eps)
        print(
            "fixed exponent saving eps=", eps,
            "beta=", beta,
            "implied zero half-width=", beta/2,
        )
