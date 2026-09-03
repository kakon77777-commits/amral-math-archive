#!/usr/bin/env python3
"""
AMRAL RH v2.8 — critical-centering / Lyapunov-gate reference checks.

REFERENCE ONLY.

Checks:
1. finite prime-power relative moments versus exact PNT continuum backbone;
2. centered residual size on moderate finite ranges;
3. finite-moment nullspace with strictly positive Cauchy energy;
4. synthetic zero-mode exponent alignment.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad


CHANNELS = [
    (-1.0,0), (-1.0,1),
    (0.5,0), (0.5,1), (0.5,2),
    (1.0,0), (1.0,1),
]


def sieve_primes(limit: int):
    if limit < 2:
        return []
    mark = np.ones(limit+1, dtype=bool)
    mark[:2] = False
    for p in range(2, int(limit**0.5)+1):
        if mark[p]:
            mark[p*p:limit+1:p] = False
    return np.flatnonzero(mark).tolist()


def prime_powers_below(xmax: float):
    limit = max(2, int(math.floor(xmax)))
    out = []
    for p in sieve_primes(limit):
        q = p
        lp = math.log(p)
        while q < xmax:
            out.append((q, lp))
            if q > limit // p:
                break
            q *= p
    out.sort()
    return out


def side_domain(side: str, h: float):
    return (-h,0.0) if side == "L" else (0.0,h)


def backbone_const(side: str, lam: float, j: int, h: float):
    lo,hi = side_domain(side,h)
    return quad(
        lambda d: math.exp((lam+0.5)*d)*(d**j),
        lo,hi,
        epsabs=1e-13,
        epsrel=1e-13,
        limit=100,
    )[0]


def relative_prime_moment(t, side, lam, j, h, pps):
    lo,hi = side_domain(side,h)
    total = 0.0
    for q,lp in pps:
        x = math.log(q)
        d = x-t
        if lo < d < hi:
            c = lp/math.sqrt(q)
            total += c*math.exp(lam*d)*(d**j)
    return total


def centered_moment(t, side, lam, j, h, pps):
    prime = relative_prime_moment(t,side,lam,j,h,pps)
    backbone = math.exp(t/2)*backbone_const(side,lam,j,h)
    return prime, backbone, prime-backbone


def all_centered(t,h,pps):
    rows = []
    for side in ("L","R"):
        for lam,j in CHANNELS:
            prime,bb,res = centered_moment(t,side,lam,j,h,pps)
            rows.append((side,lam,j,prime,bb,res))
    return rows


def right_moment_matrix(points):
    points = np.asarray(points,dtype=float)
    rows = []
    for lam,j in CHANNELS:
        rows.append(np.exp(lam*points)*(points**j))
    return np.vstack(rows)


def moment_nullspace_example(h):
    # Eight distinct right-side points against seven right moments.
    pts = np.linspace(0.05*h,0.95*h,8)
    A = right_moment_matrix(pts)
    _u,_s,vt = np.linalg.svd(A)
    w = vt[-1]
    w = w/np.linalg.norm(w)

    K = np.exp(-np.abs(pts[:,None]-pts[None,:]))
    energy = float(w@K@w)
    residual = float(np.max(np.abs(A@w)))
    return pts,w,residual,energy


def zero_mode_coefficient(side,lam,j,h,rho):
    lo,hi = side_domain(side,h)

    def real_part(d):
        z = np.exp((lam+rho-0.5)*d)*(d**j)
        return float(np.real(z))

    def imag_part(d):
        z = np.exp((lam+rho-0.5)*d)*(d**j)
        return float(np.imag(z))

    re = quad(real_part,lo,hi,epsabs=1e-12,epsrel=1e-12)[0]
    im = quad(imag_part,lo,hi,epsabs=1e-12,epsrel=1e-12)[0]
    return complex(re,im)


def zero_mode_value(t,side,lam,j,h,rho):
    coeff = zero_mode_coefficient(side,lam,j,h,rho)
    return -np.exp((rho-0.5)*t)*coeff


if __name__ == "__main__":
    h = math.log(2.0)
    tmax = 10.0
    pps = prime_powers_below(math.exp(tmax+h)+2)

    for t in [2,4,6,8,10]:
        vals = all_centered(t,h,pps)
        print(
            "t",t,
            "max prime",max(abs(v[3]) for v in vals),
            "max backbone",max(abs(v[4]) for v in vals),
            "max residual",max(abs(v[5]) for v in vals),
        )

    pts,w,res,energy = moment_nullspace_example(h)
    print("moment-null residual",res)
    print("moment-null Cauchy energy",energy)

    rho = 0.63 + 14.134725j
    for side in ("L","R"):
        for lam,j in CHANNELS:
            v1 = zero_mode_value(2.0,side,lam,j,h,rho)
            v2 = zero_mode_value(7.0,side,lam,j,h,rho)
            if abs(v1) > 1e-14:
                slope = math.log(abs(v2/v1))/5.0
                print(side,lam,j,"mode slope",slope)
