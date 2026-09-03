#!/usr/bin/env python3
"""
AMRAL RH v3.4 — elliptic PNT mean-square comparison reference checks.

REFERENCE ONLY.

Checks:
1. full-center elliptic symbol S_h for h=log 2;
2. high-frequency symbol limit 4h^3/3;
3. actual-prime local Cauchy energy vs local normalized PNT L2 upper bound.
"""

from __future__ import annotations

import math
import bisect
import numpy as np
from scipy.integrate import quad


def tent(h, z):
    return max(h-abs(z), 0.0)


def C_h(h, d):
    r=abs(d)
    if r>=2*h:
        return 0.0
    if r<=h:
        return 2*h**3/3 - h*r*r + r**3/2
    return (2*h-r)**3/6


def Hhat(h, xi):
    return 2.0*quad(
        lambda d:
            math.exp(-d)*C_h(h,d)*math.cos(xi*d),
        0.0,2*h,
        epsabs=1e-12,epsrel=1e-12,limit=220
    )[0]


def symbol_S(h, xi):
    return (xi*xi+0.25)*Hhat(h,xi)


def sieve_primes(limit):
    if limit<2:
        return []
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


class PrimeTable:
    def __init__(self,xmax):
        self.pps=prime_powers_below(xmax)
        self.logs=[math.log(q) for q,_ in self.pps]
        self.lambdas=[lp for _q,lp in self.pps]
        self.cumpsi=[]
        s=0.0
        for lp in self.lambdas:
            s+=lp
            self.cumpsi.append(s)

    def psi_log(self,t):
        k=bisect.bisect_right(self.logs,t)
        return self.cumpsi[k-1] if k else 0.0

    def e(self,t):
        x=math.exp(t)
        return math.exp(-t/2)*(self.psi_log(t)-x)


# Exact fixed-t causal Cauchy energy, reused from v2.6.
def particular_params(m,c):
    p=2*m/3
    r0=2*c/3-4*m/9
    return p,r0


def Ppart(u,m,c):
    p,r0=particular_params(m,c)
    return math.exp(u/2)*(p*u+r0)


def F2(u,m,c):
    p,r0=particular_params(m,c)
    return math.exp(u)*(
        p*p*(u*u-2*u+2)
        +2*p*r0*(u-1)
        +r0*r0
    )


def F1(u,m,c):
    p,r0=particular_params(m,c)
    return math.exp(-u/2)*(-2*p*u-4*p-2*r0)


def segment(state,x0,x1,m,c):
    one,s,s2,E=state
    rho=math.exp(-(x1-x0))
    P0=Ppart(x0,m,c)
    P1=Ppart(x1,m,c)
    cseg=P1-rho*P0
    J2=F2(x1,m,c)-F2(x0,m,c)
    J1=F1(x1,m,c)-F1(x0,m,c)
    A2=1-rho*rho
    A1=4*math.exp(x0)*J1-2*A2*P0
    A0=2*J2-4*math.exp(x0)*J1*P0+A2*P0*P0
    snew=rho*s+cseg
    Enew=E+A0+A1*s+A2*s2
    return np.array([1.0,snew,snew*snew,Enew])


def atom(state,a):
    one,s,s2,E=state
    snew=s+a
    return np.array([1.0,snew,snew*snew,E])


def local_cauchy_energy(t,h,table):
    left=t-h
    right=t+h
    atoms=[]
    for (q,lp),x in zip(table.pps,table.logs):
        if left<x<right:
            atoms.append(
                (x,lp/math.sqrt(q)*tent(h,t-x))
            )

    events=[(x,"atom",a) for x,a in atoms]
    events.append((t,"center",0.0))
    events.sort(key=lambda z:(z[0],0 if z[1]=="atom" else 1))

    st=np.array([1.0,0.0,0.0,0.0])
    pos=left
    for x,typ,a in events:
        if x>pos:
            if pos<t:
                st=segment(st,pos,x,-1.0,left)
            else:
                st=segment(st,pos,x,+1.0,-right)
            pos=x
        if typ=="atom":
            st=atom(st,a)

    if pos<right:
        if pos<t:
            st=segment(st,pos,right,-1.0,left)
        else:
            st=segment(st,pos,right,+1.0,-right)

    return st[3]+st[2]


def local_e2(t,h,table):
    lo=t-h
    hi=t+h
    pts=[lo,hi]
    for x in table.logs:
        if lo<x<hi:
            pts.append(x)
    pts=sorted(set(pts))
    total=0.0
    for a,b in zip(pts[:-1],pts[1:]):
        total+=quad(
            lambda u: table.e(u)**2,
            a,b,
            epsabs=1e-11,epsrel=1e-11,limit=100
        )[0]
    return total


if __name__=="__main__":
    h=math.log(2.0)

    xs=np.concatenate([
        np.linspace(0,20,401),
        np.linspace(20,100,161)
    ])
    vals=np.array([symbol_S(h,float(x)) for x in xs])
    print("symbol grid min",vals.min(),xs[vals.argmin()])
    print("symbol grid max",vals.max(),xs[vals.argmax()])
    print("high limit",4*h**3/3)
    print("S(100)",symbol_S(h,100.0))

    table=PrimeTable(math.exp(6.0+h)+2)
    for t in [2.0,3.0,4.0,5.0,6.0]:
        C=local_cauchy_energy(t,h,table)
        L=local_e2(t,h,table)
        bound=2*(h+1)**2*L
        print("local",t,C,L,bound,C/bound)
