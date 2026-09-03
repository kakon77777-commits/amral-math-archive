#!/usr/bin/env python3
"""
AMRAL RH v3.7 — finite-modulus parallelogram centering checks.

REFERENCE ONLY.

Checks:
1. exact rational local means for one prime p;
2. finite squarefree q mean of K_{4,q};
3. Fourier zero coefficient;
4. truncated weighted-model diagnostics.

This code does NOT evaluate or bound the infinite high-conductor tail.
"""

from __future__ import annotations

import math
import itertools
from fractions import Fraction
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


def local_factor(p: int, residues, k: int) -> Fraction:
    nu = len(set(int(x) % p for x in residues))
    return (
        Fraction(p-nu, p)
        / (Fraction(p-1, p) ** k)
    )


def local_pair_means_exact(p: int):
    vals = []
    for h in range(p):
        vals.append(local_factor(p, [0,h], 2))
    mean1 = sum(vals, Fraction(0,1)) / p
    mean2 = sum((x*x for x in vals), Fraction(0,1)) / p
    return mean1, mean2


def local_triple_mean_exact(p: int):
    s = Fraction(0,1)
    for h in range(p):
        for d in range(p):
            s += local_factor(p, [0,h,d], 3)
    return s / (p*p)


def local_four_mean_exact(p: int):
    s = Fraction(0,1)
    for h in range(p):
        for d in range(p):
            s += local_factor(p, [0,h,d,h+d], 4)
    return s / (p*p)


def raw_S_q(offsets, q: int) -> float:
    ps = prime_factors_squarefree(q)
    k = len(offsets)
    if k <= 1:
        return 1.0
    out = 1.0
    for p in ps:
        nu = len({int(x) % p for x in offsets})
        out *= (1.0 - nu/p) / ((1.0 - 1.0/p)**k)
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


def K4_q(h: int, d: int, q: int) -> float:
    s04 = refined_S0_q([0,h,d,h+d],q)
    mu = raw_S_q([0,h],q)-1.0
    return s04-mu*mu


def finite_q_mean(q: int):
    arr = np.empty((q,q),dtype=float)
    for h in range(q):
        for d in range(q):
            arr[h,d] = K4_q(h,d,q)
    return {
        "mean": float(arr.mean()),
        "max_abs": float(np.max(np.abs(arr))),
        "fft00": complex(np.fft.fft2(arr)[0,0]/(q*q)),
        "arr": arr,
    }


def endpoint_weight(N: int, n: int) -> int:
    if 1 <= n <= N:
        return N
    if N < n < 2*N:
        return 2*N-n
    return 0


def omega_weight(N: int, h: int, d: int) -> int:
    if h < 1 or d < 1 or h+d > 2*N-2:
        return 0
    total = 0
    for r in range(1,2*N-h-d):
        total += (
            endpoint_weight(N,r+h)
            * endpoint_weight(N,r+h+d)
        )
    return total


def weighted_truncated_sum(N: int, q: int):
    table = finite_q_mean(q)["arr"]
    total = 0.0
    diag = 0.0
    max_omega = 0
    max_dh = 0
    max_dd = 0

    # Precompute weights to inspect regularity.
    Om = np.zeros((2*N,2*N),dtype=np.int64)
    for h in range(1,2*N-1):
        for d in range(1,2*N-1-h):
            Om[h,d] = omega_weight(N,h,d)
            max_omega = max(max_omega,int(Om[h,d]))

    for h in range(1,2*N-1):
        for d in range(1,2*N-1-h):
            val = Om[h,d] * table[h % q,d % q]
            if h == d:
                diag += val
                continue
            total += val

    for h in range(1,2*N-2):
        for d in range(1,2*N-2-h):
            max_dh = max(max_dh,abs(int(Om[h+1,d])-int(Om[h,d])))
            max_dd = max(max_dd,abs(int(Om[h,d+1])-int(Om[h,d])))

    phi = q
    for p in prime_factors_squarefree(q):
        phi = phi // p * (p-1)
    R = q/phi
    scale = (N**4)*min(q,N)*(R**3)

    return {
        "N":N,
        "q":q,
        "sum_excluding_diagonal":total,
        "removed_diagonal":diag,
        "max_omega":max_omega,
        "max_delta_h":max_dh,
        "max_delta_d":max_dd,
        "theorem_scale_N4qR3":scale,
        "ratio_to_scale":abs(total)/scale if scale else 0.0,
    }


if __name__ == "__main__":
    for p in [2,3,5,7,11]:
        m1,m2 = local_pair_means_exact(p)
        m3 = local_triple_mean_exact(p)
        m4 = local_four_mean_exact(p)
        expected = Fraction(1,1) + Fraction(1,(p-1)**3)
        print("local",p,m1,m2,m3,m4,expected)

    for q in [2,6,30,210]:
        x = finite_q_mean(q)
        print("qmean",q,x["mean"],x["fft00"],x["max_abs"])

    for N,q in [(40,6),(80,30),(120,30),(120,210)]:
        print("weighted",weighted_truncated_sum(N,q))
