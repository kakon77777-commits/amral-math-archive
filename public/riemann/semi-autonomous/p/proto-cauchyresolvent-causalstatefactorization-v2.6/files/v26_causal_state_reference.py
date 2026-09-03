#!/usr/bin/env python3
"""
AMRAL RH v2.6 — causal state / four-state transfer reference checks.

REFERENCE ONLY.

Implements:
- exact elementary background segment transfer;
- prime atom jump;
- actual local source sweep;
- independent direct pair-energy quadrature.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad


def sieve_primes(limit: int):
    if limit < 2:
        return []
    mark = np.ones(limit + 1, dtype=bool)
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


def particular_params(m: float, c: float):
    p = 2.0*m/3.0
    r0 = 2.0*c/3.0 - 4.0*m/9.0
    return p, r0


def P(u: float, m: float, c: float) -> float:
    p, r0 = particular_params(m, c)
    return math.exp(u/2.0) * (p*u + r0)


def F2(u: float, m: float, c: float) -> float:
    p, r0 = particular_params(m, c)
    return math.exp(u) * (
        p*p*(u*u - 2*u + 2)
        + 2*p*r0*(u-1)
        + r0*r0
    )


def F1(u: float, m: float, c: float) -> float:
    p, r0 = particular_params(m, c)
    return math.exp(-u/2.0) * (-2*p*u - 4*p - 2*r0)


def segment_coeffs(x0: float, x1: float, m: float, c: float):
    delta = x1-x0
    rho = math.exp(-delta)
    P0 = P(x0,m,c)
    P1 = P(x1,m,c)
    cseg = P1-rho*P0

    J2 = F2(x1,m,c)-F2(x0,m,c)
    J1 = F1(x1,m,c)-F1(x0,m,c)

    A2 = 1-rho*rho
    A1 = 4*math.exp(x0)*J1 - 2*A2*P0
    A0 = 2*J2 - 4*math.exp(x0)*J1*P0 + A2*P0*P0

    return rho,cseg,A0,A1,A2


def apply_segment(state, x0, x1, m, c):
    one,s,s2,E = state
    rho,cseg,A0,A1,A2 = segment_coeffs(x0,x1,m,c)
    snew = rho*s+cseg
    Enew = E+A0+A1*s+A2*s2
    return np.array([1.0,snew,snew*snew,Enew])


def segment_matrix(x0,x1,m,c):
    rho,cseg,A0,A1,A2 = segment_coeffs(x0,x1,m,c)
    return np.array([
        [1,0,0,0],
        [cseg,rho,0,0],
        [cseg*cseg,2*rho*cseg,rho*rho,0],
        [A0,A1,A2,1],
    ],dtype=float)


def atom_matrix(a):
    return np.array([
        [1,0,0,0],
        [a,1,0,0],
        [a*a,2*a,1,0],
        [0,0,0,1],
    ],dtype=float)


def apply_atom(state,a):
    return atom_matrix(a) @ state


def tent(h,x):
    return max(h-abs(x),0.0)


def background_f(u,t,h):
    return -tent(h,t-u)*math.exp(u/2.0)


def actual_local_causal_energy(t,h,pps):
    a=t-h
    b=t+h
    atoms=[]
    for q,lp in pps:
        x=math.log(q)
        if a < x < b:
            w=lp/math.sqrt(q)*tent(h,t-x)
            atoms.append((x,w))

    state=np.array([1.0,0.0,0.0,0.0])
    pos=a

    # add center as a branch-change breakpoint
    events=[(x,"atom",w) for x,w in atoms]
    events.append((t,"center",0.0))
    events.sort(key=lambda z:(z[0],0 if z[1]=="atom" else 1))

    for x,kind,w in events:
        if x>pos:
            if pos < t:
                m=-1.0
                c=a
            else:
                m=1.0
                c=-b
            state=apply_segment(state,pos,x,m,c)
            pos=x
        if kind=="atom":
            state=apply_atom(state,w)

    if pos<b:
        m=1.0 if pos>=t else -1.0
        c=-b if pos>=t else a
        state=apply_segment(state,pos,b,m,c)

    # homogeneous right tail contributes s(b)^2
    return state[3]+state[2], state, atoms


def direct_pair_energy(t,h,atoms):
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
        def integrand(u):
            return math.exp(-abs(x-u))*background_f(u,t,h)
        pts=sorted(set([a,t,x,b]))
        val=0.0
        for lo,hi in zip(pts[:-1],pts[1:]):
            if hi>lo:
                val += quad(integrand,lo,hi,epsabs=1e-11,epsrel=1e-11,limit=150)[0]
        ab += 2*w*val

    # background-background via lower triangle
    def inner(u):
        fu=background_f(u,t,h)
        if fu==0.0:
            return 0.0
        # split inner integral at t if necessary
        pts=sorted(set([a,min(max(t,a),u),u]))
        inner_val=0.0
        for lo,hi in zip(pts[:-1],pts[1:]):
            if hi>lo:
                inner_val += quad(
                    lambda v: math.exp(-(u-v))*background_f(v,t,h),
                    lo,hi,epsabs=1e-11,epsrel=1e-11,limit=120
                )[0]
        return 2*fu*inner_val

    bb=0.0
    for lo,hi in [(a,t),(t,b)]:
        if hi>lo:
            bb += quad(inner,lo,hi,epsabs=1e-10,epsrel=1e-10,limit=180)[0]

    return aa+ab+bb, {"atom_atom":aa,"atom_bg":ab,"bg_bg":bb}


if __name__=="__main__":
    h=math.log(2.0)
    tmax=4.2
    pps=prime_powers_below(math.exp(tmax+h)+2)

    for t in [2.0,2.8,3.6,4.2]:
        causal,state,atoms=actual_local_causal_energy(t,h,pps)
        direct,parts=direct_pair_energy(t,h,atoms)
        print(t,len(atoms),causal,direct,causal-direct,parts)

    # Matrix-vs-direct state update sanity
    state=np.array([1.0,0.4,0.16,0.2])
    M=segment_matrix(0.2,0.8,-1.0,0.1)
    s1=M@state
    s2=apply_segment(state,0.2,0.8,-1.0,0.1)
    print("segment matrix residual",np.max(np.abs(s1-s2)))
