#!/usr/bin/env python3
"""
AMRAL RH v3.11 — modulation-gate reference checks.

REFERENCE ONLY.

Checks:
1. exact finite character orthogonality for parallelogram constraints;
2. exact modulation translation E_f,H^(lambda)(alpha)=E_f,H(alpha+lambda);
3. comparison of the direct odd adding-fractions bound with the
   finite-resolution scale Q^4/N+Q^2.

No UMP4 theorem is claimed.
"""

from __future__ import annotations

import math
import cmath
import random


def e(x: float) -> complex:
    return cmath.exp(2j*math.pi*x)


def character_delta(L: int, M: int) -> complex:
    return sum(e(j*L/M) for j in range(M))/M


def parallelogram_delta(d1,d2,d3,d4,M):
    L=d1+d4-d2-d3
    return character_delta(L,M)


def sample_weight(m: int, H: int) -> float:
    # compact discrete test weight
    x=m/H
    if 0.1 <= x <= 1.8:
        return (x-0.1)*(1.8-x)
    return 0.0


def E_base(H: int, alpha: float) -> complex:
    total=0j
    for m in range(-2*H,2*H+1):
        total += sample_weight(m,H)*e(m*alpha)
    return total


def E_modulated(H: int, alpha: float, lam: float) -> complex:
    total=0j
    for m in range(-2*H,2*H+1):
        total += (
            sample_weight(m,H)
            * e(lam*m)
            * e(alpha*m)
        )
    return total


def odd_bound_proxy(N: float, Q: float) -> float:
    """
    Polylog factors omitted.

    Derived from the Bloom-Kuperberg interval theorem via the natural
    three-fraction lift.
    """
    if Q <= N:
        return Q**3
    return Q**4/N


def finite_resolution_scale(N: float, Q: float) -> float:
    return Q**4/N + Q**2


if __name__=="__main__":
    H=20
    M=8*H+1

    tests=[
        (1,4,7,10),
        (2,5,8,11),
        (1,3,6,9),
        (2,6,7,12),
    ]

    for t in tests:
        val=parallelogram_delta(*t,M)
        L=t[0]+t[3]-t[1]-t[2]
        print("delta",t,L,val)

    for alpha,lam in [
        (0.13,0.07),
        (0.21,0.31),
        (0.49,0.125),
    ]:
        a=E_modulated(H,alpha,lam)
        b=E_base(H,alpha+lam)
        print("mod",alpha,lam,a,b,a-b)

    for N in [1e4,1e6]:
        for exponent in [0.5,0.6,0.75,1.0,1.2]:
            Q=N**exponent
            if Q < math.sqrt(N):
                continue
            odd=odd_bound_proxy(N,Q)
            res=finite_resolution_scale(N,Q)
            print("scale",N,exponent,Q,odd,res,odd/res)
