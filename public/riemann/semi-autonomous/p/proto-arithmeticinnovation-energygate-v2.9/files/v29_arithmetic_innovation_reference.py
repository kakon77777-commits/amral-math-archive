#!/usr/bin/env python3
"""
AMRAL RH v2.9 — arithmetic innovation reference checks.

REFERENCE ONLY.

Checks:
1. critical-centered moments vs exact Stieltjes integration-by-parts
   representation through the scalar innovation primitive b(t);
2. local Cauchy energy vs innovation H^{-1} upper bound.
"""

from __future__ import annotations

import math
import bisect
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


class InnovationTable:
    def __init__(self, xmax: float):
        self.pps = prime_powers_below(xmax)
        self.xlogs = [math.log(q) for q,_lp in self.pps]
        self.weights = [lp/math.sqrt(q) for q,lp in self.pps]
        self.cum = []
        s = 0.0
        for w in self.weights:
            s += w
            self.cum.append(s)

    def weighted_prime_cumulative(self, t: float) -> float:
        k = bisect.bisect_right(self.xlogs, t)
        if k == 0:
            return 0.0
        return self.cum[k-1]

    def b(self, t: float) -> float:
        return self.weighted_prime_cumulative(t) - 2.0*math.exp(t/2)

    def local_atoms(self, t: float, h: float):
        lo = t-h
        hi = t+h
        out = []
        for x,w in zip(self.xlogs,self.weights):
            if x <= lo:
                continue
            if x >= hi:
                break
            out.append((x,w))
        return out


def side_domain(side: str, h: float):
    return (-h,0.0) if side == "L" else (0.0,h)


def phi(d: float, lam: float, j: int) -> float:
    return math.exp(lam*d)*(d**j)


def phi_prime(d: float, lam: float, j: int) -> float:
    val = lam*(d**j)
    if j:
        val += j*(d**(j-1))
    return math.exp(lam*d)*val


def direct_centered_moment(t, side, lam, j, h, table: InnovationTable):
    lo,hi = side_domain(side,h)

    # prime relative moment
    prime = 0.0
    for x,w in zip(table.xlogs,table.weights):
        d = x-t
        if lo < d < hi:
            prime += w*phi(d,lam,j)

    # continuum backbone = int phi(d) exp((t+d)/2) dd
    backbone = math.exp(t/2) * quad(
        lambda d: math.exp((lam+0.5)*d)*(d**j),
        lo,hi,
        epsabs=1e-13,epsrel=1e-13,limit=100
    )[0]

    return prime-backbone


def ibp_centered_moment(t, side, lam, j, h, table: InnovationTable):
    lo,hi = side_domain(side,h)

    # split at every prime jump of b(t+d)
    pts = [lo,hi]
    for x in table.xlogs:
        d = x-t
        if lo < d < hi:
            pts.append(d)
    pts = sorted(set(pts))

    integ = 0.0
    for a,b in zip(pts[:-1],pts[1:]):
        if b <= a:
            continue
        integ += quad(
            lambda d: table.b(t+d)*phi_prime(d,lam,j),
            a,b,
            epsabs=1e-12,epsrel=1e-12,limit=80
        )[0]

    return (
        phi(hi,lam,j)*table.b(t+hi)
        - phi(lo,lam,j)*table.b(t+lo)
        - integ
    )


def tent(h: float, z: float) -> float:
    return max(h-abs(z),0.0)


def background_f(u,t,h):
    return -tent(h,t-u)*math.exp(u/2)


def direct_local_cauchy_energy(t,h,table: InnovationTable):
    atoms = []
    for x,w in table.local_atoms(t,h):
        atoms.append((x,w*tent(h,t-x)))

    a=t-h
    b=t+h

    # atom-atom
    aa=0.0
    for xi,wi in atoms:
        for xj,wj in atoms:
            aa += wi*wj*math.exp(-abs(xi-xj))

    # atom-background
    ab=0.0
    for x,w in atoms:
        pts=sorted(set([a,t,x,b]))
        val=0.0
        for lo,hi in zip(pts[:-1],pts[1:]):
            if hi>lo:
                val += quad(
                    lambda u: math.exp(-abs(x-u))*background_f(u,t,h),
                    lo,hi,
                    epsabs=1e-11,epsrel=1e-11,limit=100
                )[0]
        ab += 2*w*val

    # background-background on lower triangle
    def inner(u):
        fu=background_f(u,t,h)
        pts=sorted(set([a,min(max(t,a),u),u]))
        val=0.0
        for lo,hi in zip(pts[:-1],pts[1:]):
            if hi>lo:
                val += quad(
                    lambda v: math.exp(-(u-v))*background_f(v,t,h),
                    lo,hi,
                    epsabs=1e-11,epsrel=1e-11,limit=100
                )[0]
        return 2*fu*val

    bb=0.0
    for lo,hi in [(a,t),(t,b)]:
        bb += quad(
            inner,lo,hi,
            epsabs=1e-10,epsrel=1e-10,limit=130
        )[0]

    return aa+ab+bb


def b_square_integral(t,h,table: InnovationTable):
    lo=t-h
    hi=t+h
    pts=[lo,hi]
    for x in table.xlogs:
        if lo < x < hi:
            pts.append(x)
    pts=sorted(set(pts))

    total=0.0
    for a,b in zip(pts[:-1],pts[1:]):
        total += quad(
            lambda u: table.b(u)**2,
            a,b,
            epsabs=1e-11,epsrel=1e-11,limit=100
        )[0]
    return total


def innovation_energy_upper_bound(t,h,table: InnovationTable):
    return 4.0*(h*h+1.0)*b_square_integral(t,h,table)


if __name__ == "__main__":
    h=math.log(2.0)
    tmax=5.0
    table=InnovationTable(math.exp(tmax+h)+2)

    for t in [1.37,2.13,3.27,4.41]:
        max_res=0.0
        for side in ("L","R"):
            for lam,j in CHANNELS:
                d=direct_centered_moment(t,side,lam,j,h,table)
                b=ibp_centered_moment(t,side,lam,j,h,table)
                max_res=max(max_res,abs(d-b))
        E=direct_local_cauchy_energy(t,h,table)
        U=innovation_energy_upper_bound(t,h,table)
        print(t,"moment residual",max_res,"energy",E,"bound",U,"ratio",E/U)
