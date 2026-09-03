#!/usr/bin/env python3
"""
AMRAL RH v3.10 — restriction-threshold reference checks.

REFERENCE ONLY.

Checks:
1. finite-q denominator slices of raw and Sobolev coefficient mass;
2. r^{-3} / r^{-2} diagnostic scaling;
3. product-Farey large-sieve numerical check for the differentiated Omega weight.

No super-sqrt(N) restriction theorem is claimed.
"""

from __future__ import annotations

import math
import numpy as np
from collections import defaultdict


def prime_factors_squarefree(q: int):
    out=[]
    n=q
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            n//=p
            if n%p==0:
                raise ValueError("q must be squarefree")
        p+=1
    if n>1:
        out.append(n)
    return out


def rho_array(q: int):
    rho=np.zeros(q,dtype=float)
    for k in range(1,q):
        r=q//math.gcd(k,q)
        ps=prime_factors_squarefree(r)
        mu=-1.0 if len(ps)%2 else 1.0
        phi=r
        for p in ps:
            phi=phi//p*(p-1)
        rho[k]=mu/phi
    return rho


def coefficient_table(q: int):
    rho=rho_array(q)
    coeff=np.zeros((q,q),dtype=complex)
    for b in range(q):
        Bp=rho*np.roll(rho,-b)
        Bm=rho*np.roll(rho,+b)
        coeff[:,b]=np.fft.ifft(
            np.fft.fft(Bm)*np.fft.fft(Bp)
        )
    coeff[:,0]=0.0
    return coeff


def denominator_slices(q: int):
    coeff=coefficient_table(q)
    raw=defaultdict(float)
    sob=defaultdict(float)

    for b in range(1,q):
        r=q//math.gcd(b,q)
        mass=float(np.sum(np.abs(coeff[:,b])**2))
        raw[r]+=mass
        den=abs(1.0-np.exp(2j*math.pi*b/q))**2
        sob[r]+=mass/den

    return raw,sob


def endpoint_weight(N,n):
    if 1<=n<=N:
        return float(N)
    if N<n<2*N:
        return float(2*N-n)
    return 0.0


def omega_weight(N,h,d):
    if h<1 or d<1 or h+d>2*N-2:
        return 0.0
    total=0.0
    for r in range(1,2*N-h-d):
        total += (
            endpoint_weight(N,r+h)
            * endpoint_weight(N,r+h+d)
        )
    return total


def differentiated_omega_array(N):
    size=2*N+1
    F=np.zeros((size,size),dtype=float)

    for h in range(size):
        for d in range(size):
            cur=omega_weight(N,h,d)
            prev=omega_weight(N,h,d-1)
            F[h,d]=cur-prev

    return F


def farey_points(Q):
    vals={0.0}
    for r in range(1,Q+1):
        for a in range(r):
            if math.gcd(a,r)==1:
                vals.add(a/r)
    return sorted(vals)


def Fourier2(F,alpha,beta):
    h=np.arange(F.shape[0],dtype=float)
    d=np.arange(F.shape[1],dtype=float)
    eh=np.exp(-2j*math.pi*alpha*h)
    ed=np.exp(-2j*math.pi*beta*d)
    return complex(eh @ F @ ed)


def low_conductor_large_sieve_diagnostic(N,Q):
    F=differentiated_omega_array(N)
    pts=farey_points(Q)

    sampled=0.0
    for a in pts:
        for b in pts:
            sampled += abs(Fourier2(F,a,b))**2

    l2=float(np.sum(F*F))
    theorem_scale=(2*N+Q*Q)**2*l2

    return {
        "N":N,
        "Q":Q,
        "farey_count":len(pts),
        "sampled_fourier_mass":sampled,
        "F_l2_square":l2,
        "product_large_sieve_scale":theorem_scale,
        "ratio":sampled/theorem_scale if theorem_scale else 0.0,
    }


if __name__=="__main__":
    for q in [30,210,2310]:
        raw,sob=denominator_slices(q)
        for r in sorted(raw):
            print(
                "slice",q,r,
                raw[r],
                sob[r],
                raw[r]*r**3,
                sob[r]*r**2,
            )

    for N,Q in [(10,2),(12,3),(16,4)]:
        print("LS",low_conductor_large_sieve_diagnostic(N,Q))
