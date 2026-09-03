#!/usr/bin/env python3
"""
AMRAL RH v3.0 — work / lifecycle reference checks.

REFERENCE ONLY.

Checks:
1. finite signed-atom work-energy identity;
2. integrated kinetic action vs A_h pair kernel;
3. total impulse work vs -action;
4. per-source lifecycle self/external work;
5. selected actual prime-power lifecycle work with exact smooth background.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad


def tent(h, x):
    return max(h-abs(x), 0.0)


def tent_slope(h, x):
    if -h < x < 0:
        return 1.0
    if 0 < x < h:
        return -1.0
    return 0.0


def A_h(h, d):
    r = abs(d)
    if r >= 2*h:
        return 0.0
    if r <= h:
        return 2*h - 3*r
    return r - 2*h


def L_h(h, d):
    return (
        tent(h, d-h)
        - 2*tent(h, d)
        + tent(h, d+h)
    )


def kernel_matrix(x):
    x = np.asarray(x, dtype=float)
    return np.exp(-np.abs(x[:,None]-x[None,:]))


def weights_at(t,h,x,a):
    return np.array(
        [aa*tent(h,t-xx) for xx,aa in zip(x,a)],
        dtype=float
    )


def slopes_at(t,h,x,a):
    return np.array(
        [aa*tent_slope(h,t-xx) for xx,aa in zip(x,a)],
        dtype=float
    )


def energy(t,h,x,a,K=None):
    if K is None:
        K = kernel_matrix(x)
    w = weights_at(t,h,x,a)
    return float(w @ K @ w)


def energy_prime(t,h,x,a,K=None):
    if K is None:
        K = kernel_matrix(x)
    w = weights_at(t,h,x,a)
    d = slopes_at(t,h,x,a)
    return 2.0*float(d @ K @ w)


def kinetic(t,h,x,a,K=None):
    if K is None:
        K = kernel_matrix(x)
    d = slopes_at(t,h,x,a)
    return float(d @ K @ d)


def all_events(h,x,a):
    ev = []
    for j,(xx,aa) in enumerate(zip(x,a)):
        ev.append((xx-h,j,+aa,"ENTER"))
        ev.append((xx,j,-2*aa,"CENTER"))
        ev.append((xx+h,j,+aa,"EXIT"))
    ev.sort()
    return ev


def chronological_action_and_work(h,x,a):
    x = np.asarray(x,dtype=float)
    a = np.asarray(a,dtype=float)
    K = kernel_matrix(x)
    ev = all_events(h,x,a)

    # Event-free kinetic is constant.
    action = 0.0
    impulse_work = 0.0

    left = min(e[0] for e in ev) - 1.0
    right = max(e[0] for e in ev) + 1.0

    cur = left
    idx = 0

    while idx < len(ev):
        te = ev[idx][0]

        if te > cur:
            mid = 0.5*(cur+te)
            action += (te-cur)*kinetic(mid,h,x,a,K)
            cur = te

        # Multiple simultaneous events: apply sequentially.
        while idx < len(ev) and abs(ev[idx][0]-te) < 1e-13:
            _t,j,delta_d,_typ = ev[idx]
            w = weights_at(te,h,x,a)
            field = K @ w
            impulse_work += delta_d * field[j]
            idx += 1

    if right > cur:
        mid = 0.5*(cur+right)
        action += (right-cur)*kinetic(mid,h,x,a,K)

    return action, impulse_work


def pair_action(h,x,a):
    x = np.asarray(x,dtype=float)
    a = np.asarray(a,dtype=float)
    total = 0.0
    for i in range(len(x)):
        for j in range(len(x)):
            total += (
                a[i]*a[j]
                * math.exp(-abs(x[i]-x[j]))
                * A_h(h,x[i]-x[j])
            )
    return total


def pair_work(h,x,a):
    x = np.asarray(x,dtype=float)
    a = np.asarray(a,dtype=float)
    total = 0.0
    for i in range(len(x)):
        for j in range(len(x)):
            total += (
                a[i]*a[j]
                * math.exp(-abs(x[i]-x[j]))
                * L_h(h,x[i]-x[j])
            )
    return total


def source_lifecycle_work(h,x,a,j):
    K = kernel_matrix(x)
    xx = x[j]
    aa = a[j]

    val = 0.0
    for te,coeff in [
        (xx-h,+1.0),
        (xx,-2.0),
        (xx+h,+1.0),
    ]:
        w = weights_at(te,h,x,a)
        field = K @ w
        val += aa*coeff*field[j]
    return val


# ---- actual prime/background sample ----

def sieve_primes(limit):
    mark = np.ones(limit+1,dtype=bool)
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


def full_field_at(t,x0,h,pps):
    # prime field
    s = 0.0
    lo=t-h
    hi=t+h
    for q,lp in pps:
        x=math.log(q)
        if x <= lo:
            continue
        if x >= hi:
            break
        c=lp/math.sqrt(q)
        s += (
            c
            * tent(h,t-x)
            * math.exp(-abs(x0-x))
        )

    # smooth archimedean background
    pts=sorted(set([lo,t,x0,hi]))
    bg=0.0
    for a,b in zip(pts[:-1],pts[1:]):
        if b>a:
            bg += quad(
                lambda u:
                    math.exp(u/2)
                    * tent(h,t-u)
                    * math.exp(-abs(x0-u)),
                a,b,
                epsabs=1e-11,
                epsrel=1e-11,
                limit=100,
            )[0]

    return s-bg


def actual_prime_lifecycle(h,q,lp,pps):
    x=math.log(q)
    c=lp/math.sqrt(q)

    F_enter=full_field_at(x-h,x,h,pps)
    F_center=full_field_at(x,x,h,pps)
    F_exit=full_field_at(x+h,x,h,pps)

    total=c*(F_enter-2*F_center+F_exit)
    self_work=-2*h*c*c
    external=total-self_work

    return total,self_work,external,F_enter,F_center,F_exit


if __name__ == "__main__":
    h=math.log(2.0)

    x=np.array([0.2,0.75,1.1,1.55])
    a=np.array([0.8,-0.55,1.05,0.4])

    action,work=chronological_action_and_work(h,x,a)
    print("chron action",action)
    print("chron work",work)
    print("pair action",pair_action(h,x,a))
    print("pair work",pair_work(h,x,a))
    print("balance",action+work)

    for j in range(len(x)):
        W=source_lifecycle_work(h,x,a,j)
        selfW=-2*h*a[j]*a[j]
        print("source",j,"work",W,"self",selfW,"external",W-selfW)

    pps=prime_powers_below(math.exp(5.0)+2)
    for q,lp in pps:
        if q in (5,7,11,13,17,19):
            print("prime",q,actual_prime_lifecycle(h,q,lp,pps))
