#!/usr/bin/env python3
"""
AMRAL RH v3.1 — lifecycle renewal / boundary-inventory reference checks.

REFERENCE ONLY.

Checks:
1. finite signed atomic source:
   J(t) = completed_reward(t) + unfinished_inventory(t);
2. block identity;
3. completion-field relative-moment formula;
4. actual prime EXIT completion rewards including smooth background.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad


def tent(h, x):
    return max(h-abs(x), 0.0)


def C_h(h, d):
    r = abs(d)
    if r >= 2*h:
        return 0.0
    if r <= h:
        return 2*h**3/3 - h*r*r + r**3/2
    return (2*h-r)**3/6


def H_h(h, d):
    return math.exp(-abs(d))*C_h(h,d)


def pair_start(h,u,v):
    return max(u,v)-h


def pair_end(h,u,v):
    return min(u,v)+h


def pair_profile(t,h,u,v):
    return math.exp(-abs(u-v))*tent(h,t-u)*tent(h,t-v)


def pair_accrued(t,h,u,v):
    s = pair_start(h,u,v)
    e = pair_end(h,u,v)
    if abs(u-v) >= 2*h:
        return 0.0
    if t <= s or t >= e:
        return 0.0
    return quad(
        lambda z: pair_profile(z,h,u,v),
        s,t,
        epsabs=1e-12,epsrel=1e-12,limit=100
    )[0]


def atomic_point_energy(t,h,x,a):
    total=0.0
    for i in range(len(x)):
        for j in range(len(x)):
            total += a[i]*a[j]*pair_profile(t,h,x[i],x[j])
    return total


def atomic_J(t,h,x,a):
    lo=min(x)-h-0.5
    if t <= lo:
        return 0.0
    events=[lo,t]
    for xx in x:
        for e in (xx-h,xx,xx+h):
            if lo < e < t:
                events.append(e)
    events=sorted(set(events))
    total=0.0
    for p,q in zip(events[:-1],events[1:]):
        total += quad(
            lambda z: atomic_point_energy(z,h,x,a),
            p,q,
            epsabs=1e-11,epsrel=1e-11,limit=100
        )[0]
    return total


def atomic_completed_reward(t,h,x,a):
    total=0.0
    for i in range(len(x)):
        for j in range(len(x)):
            if abs(x[i]-x[j]) >= 2*h:
                continue
            if pair_end(h,x[i],x[j]) <= t:
                total += a[i]*a[j]*H_h(h,x[i]-x[j])
    return total


def atomic_unfinished_inventory(t,h,x,a):
    total=0.0
    for i in range(len(x)):
        for j in range(len(x)):
            if abs(x[i]-x[j]) >= 2*h:
                continue
            total += a[i]*a[j]*pair_accrued(t,h,x[i],x[j])
    return total


def completion_poly_coeffs(h, side):
    if side == "L":
        return [h**3/6, -h*h/2, h/2, 1/2]
    return [h**3/6, -h*h/2, h/2, -1/6]


def direct_future_field(h,t,x,a):
    """
    Earlier source is at x0=t-h.
    Future field integrates r in (0,2h), equivalently current d in (-h,h).
    Finite signed atomic source only.
    """
    x0=t-h
    total=0.0
    for xx,aa in zip(x,a):
        r=xx-x0
        if 0 < r < 2*h:
            total += aa*H_h(h,r)
    return total


def moment_future_field(h,t,x,a):
    total=0.0
    for side,lo,hi in [("L",-h,0.0),("R",0.0,h)]:
        coeff=completion_poly_coeffs(h,side)
        moments=[]
        for j in range(4):
            m=0.0
            for xx,aa in zip(x,a):
                d=xx-t
                if lo < d < hi:
                    m += aa*math.exp(-d)*(d**j)
            moments.append(m)
        total += math.exp(-h)*sum(coeff[j]*moments[j] for j in range(4))
    return total


# ---- actual prime + continuum completion sample ----

def sieve_primes(limit):
    mark=np.ones(limit+1,dtype=bool)
    mark[:2]=False
    for p in range(2,int(limit**0.5)+1):
        if mark[p]:
            mark[p*p:limit+1:p]=False
    return np.flatnonzero(mark).tolist()


def prime_powers_below(xmax):
    limit=max(2,int(math.floor(xmax)))
    out=[]
    for p in sieve_primes(limit):
        q=p
        lp=math.log(p)
        while q<xmax:
            out.append((q,lp))
            if q>limit//p:
                break
            q*=p
    out.sort()
    return out


def actual_future_innovation_field(h,x0,pps):
    total=0.0

    # later prime powers
    for q,lp in pps:
        x=math.log(q)
        r=x-x0
        if r <= 0:
            continue
        if r >= 2*h:
            break
        total += lp/math.sqrt(q)*H_h(h,r)

    # smooth background
    total -= quad(
        lambda r:
            math.exp((x0+r)/2)*H_h(h,r),
        0.0,2*h,
        epsabs=1e-12,epsrel=1e-12,limit=120
    )[0]

    return total


def actual_prime_completion_jump(h,q,lp,pps):
    x=math.log(q)
    c=lp/math.sqrt(q)
    gamma=actual_future_innovation_field(h,x,pps)
    jump=c*c*C_h(h,0.0)+2*c*gamma
    return jump,gamma,c*c*C_h(h,0.0),2*c*gamma


if __name__ == "__main__":
    h=math.log(2.0)
    x=np.array([0.1,0.55,1.05,1.42])
    a=np.array([0.8,-0.45,1.1,0.35])

    for t in [0.0,0.6,1.0,1.5,2.0]:
        J=atomic_J(t,h,x,a)
        R=atomic_completed_reward(t,h,x,a)
        U=atomic_unfinished_inventory(t,h,x,a)
        print("renewal",t,J,R,U,J-R-U)

    for t in [0.7,1.0,1.4]:
        d=direct_future_field(h,t,x,a)
        m=moment_future_field(h,t,x,a)
        print("future field",t,d,m,d-m)

    pps=prime_powers_below(math.exp(5.0)+2)
    mp={q:lp for q,lp in pps}
    for q in [5,7,11,13,17,19]:
        if q in mp:
            print("prime completion",q,actual_prime_completion_jump(h,q,mp[q],pps))
