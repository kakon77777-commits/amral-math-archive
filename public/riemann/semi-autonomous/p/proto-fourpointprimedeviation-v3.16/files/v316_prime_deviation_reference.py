#!/usr/bin/env python3
"""
AMRAL RH v3.16 — actual-prime deviation reference checks.

REFERENCE ONLY.

Checks:
1. local FPD algebra identity for arbitrary deterministic main terms;
2. endpoint identity Q_j(h)=r_j(h)-E(j)-E(j-h)+E(h);
3. V_N <= N * integrated endpoint pair variance;
4. exponent translation table.

No fixed-power prime theorem is claimed.
"""

from __future__ import annotations
import math
import numpy as np


def primes_upto(n: int):
    if n < 2:
        return []
    mark=np.ones(n+1,dtype=bool)
    mark[:2]=False
    for p in range(2,int(n**0.5)+1):
        if mark[p]:
            mark[p*p:n+1:p]=False
    return np.flatnonzero(mark).tolist()


def von_mangoldt(limit: int):
    lam=np.zeros(limit+1,dtype=float)
    for p in primes_upto(limit):
        q=p
        lp=math.log(p)
        while q<=limit:
            lam[q]=lp
            if q>limit//p:
                break
            q*=p
    return lam


def local_fpd_identity(a_r,a_rh,a_rd,a_rdh,mu_h,s0):
    P1=a_r*a_rh-mu_h
    P2=a_rd*a_rdh-mu_h
    K4=s0-mu_h*mu_h

    lhs=P1*P2-K4
    T=a_r*a_rh*a_rd*a_rdh-s0
    rhs=T-mu_h*(P1+P2)
    return lhs,rhs,lhs-rhs


def endpoint_identity(j,h,lam,S_h):
    psi=np.cumsum(lam)
    a=lam-1.0
    a[0]=0.0

    Q=sum(
        a[n]*a[n-h]
        for n in range(h+1,j+1)
    )-(S_h-1.0)*(j-h)

    psi2=sum(
        lam[n]*lam[n-h]
        for n in range(h+1,j+1)
    )
    r=psi2-S_h*(j-h)

    def E(x):
        if x<=0:
            return 0.0
        return psi[x]-x

    rhs=r-E(j)-E(j-h)+E(h)
    return Q,rhs,Q-rhs


def endpoint_Q_matrix(N,lam,Sfun):
    psi=np.cumsum(lam)
    a=lam-1.0
    a[0]=0.0

    Q={}
    for j in range(N,2*N):
        for h in range(1,j):
            S=Sfun(h)
            val=sum(
                a[n]*a[n-h]
                for n in range(h+1,j+1)
            )-(S-1.0)*(j-h)
            Q[(j,h)]=val
    return Q


def V_and_EPV(N,Q):
    V=0.0
    for h in range(1,2*N-1):
        R=sum(
            Q.get((j,h),0.0)
            for j in range(N,2*N)
        )
        V+=R*R

    EPV=sum(v*v for v in Q.values())
    return V,EPV,V/(N*EPV) if EPV else 0.0


def twin_constant(prime_limit=50000):
    prod=1.0
    for p in primes_upto(prime_limit):
        if p>2:
            prod*=1.0-1.0/((p-1.0)**2)
    return prod


def pair_singular_series(h,C2):
    if h%2:
        return 0.0
    n=h
    out=2.0*C2
    p=3
    while p*p<=n:
        if n%p==0:
            out*=(p-1.0)/(p-2.0)
            while n%p==0:
                n//=p
        p+=2
    if n>2:
        out*=(n-1.0)/(n-2.0)
    return out


def exponent_translation(eta):
    return {
        "eta_EPV":eta,
        "V_exponent":5.0-eta,
        "I_exponent":3.0-eta/2.0,
        "Theta_upper":1.0-eta/4.0,
    }


if __name__=="__main__":
    # Pure algebra identity.
    vals=(0.7,-1.2,0.4,2.1,0.3,-0.8)
    print("local",local_fpd_identity(*vals))

    N=30
    lam=von_mangoldt(2*N+10)
    C2=twin_constant()
    Sfun=lambda h: pair_singular_series(h,C2)

    for j,h in [(30,2),(35,4),(45,6),(55,10)]:
        print("endpoint",j,h,endpoint_identity(j,h,lam,Sfun(h)))

    Q=endpoint_Q_matrix(N,lam,Sfun)
    print("gate",V_and_EPV(N,Q))

    for eta in [0.1,0.25,0.5,0.75]:
        print("exp",exponent_translation(eta))
