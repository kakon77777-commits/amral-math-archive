#!/usr/bin/env python3
"""
AMRAL RH v3.14 — pair-square axis Ramanujan reference checks.

REFERENCE ONLY.

Checks:
1. c_p(n)^2=(p-2)c_p(n)+(p-1);
2. finite-prime exact axis coefficient expansion;
3. coefficient decay diagnostics;
4. collapsed Xi_N size / first-difference scaling;
5. low/high exponent optimization.

No RH claim is made.
"""

from __future__ import annotations
import math
import itertools
import numpy as np


def primes_upto(n: int):
    if n < 2:
        return []
    mark = np.ones(n+1,dtype=bool)
    mark[:2] = False
    for p in range(2,int(n**0.5)+1):
        if mark[p]:
            mark[p*p:n+1:p] = False
    return np.flatnonzero(mark).tolist()


def mobius_squarefree(q: int):
    n=q
    count=0
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            count+=1
            if n%p==0:
                return 0
        p+=1
    if n>1:
        count+=1
    return -1 if count%2 else 1


def phi(n: int):
    out=n
    x=n
    p=2
    while p*p<=x:
        if x%p==0:
            out=out//p*(p-1)
            while x%p==0:
                x//=p
        p+=1
    if x>1:
        out=out//x*(x-1)
    return out


def ramanujan_sum(q: int, n: int):
    # c_q(n)=sum_{d|(q,n)} d mu(q/d)
    g=math.gcd(q,n)
    total=0
    for d in range(1,g+1):
        if g%d==0:
            total += d*mobius_squarefree(q//d)
    return total


def g_p(p: int):
    return (
        (2*p-3)
        /
        (
            (p-1)
            *
            (p*p-3*p+3)
        )
    )


def finite_prime_data(P):
    A=1.0
    primorial=1
    for p in P:
        A *= 1.0 + 1.0/(p-1.0)**3
        primorial *= p

    divisors=[1]
    for p in P:
        old=list(divisors)
        divisors += [d*p for d in old]
    divisors=sorted(divisors)

    coeff={}
    for q in divisors:
        if q==1:
            coeff[q]=0.0
            continue
        g=1.0
        for p in P:
            if q%p==0:
                g*=g_p(p)
        coeff[q] = A*g - 2.0/(phi(q)**2)

    return A,primorial,divisors,coeff


def finite_axis_direct(P,n):
    S=1.0
    A=1.0
    for p in P:
        S *= 1.0 + ramanujan_sum(p,n)/(p-1.0)**2
        A *= 1.0 + 1.0/(p-1.0)**3
    axis=(S-1.0)**2-(A-1.0)
    return axis,S,A


def finite_axis_coeff(P,n):
    A,primorial,divisors,coeff=finite_prime_data(P)
    total=0.0
    for q in divisors:
        if q>1:
            total += coeff[q]*ramanujan_sum(q,n)
    return total


def endpoint_weight(N,n):
    if 1<=n<=N:
        return float(N)
    if N<n<2*N:
        return float(2*N-n)
    return 0.0


def Xi_array(N: int):
    # Xi_N(d)=sum_n (n-1) w(n) w(n+d)
    arr=np.zeros(2*N+1,dtype=float)
    for d in range(1,2*N-1):
        total=0.0
        for n in range(2,2*N-d):
            total += (
                (n-1)
                * endpoint_weight(N,n)
                * endpoint_weight(N,n+d)
            )
        arr[d]=total
    return arr


def xi_scaling(N: int):
    Xi=Xi_array(N)
    dXi=np.diff(
        np.concatenate(([0.0],Xi))
    )
    return {
        "N":N,
        "Xi_sup":float(np.max(np.abs(Xi))),
        "Xi_l2":float(np.linalg.norm(Xi)),
        "dXi_sup":float(np.max(np.abs(dXi))),
        "dXi_l2":float(np.linalg.norm(dXi)),
        "Xi_l2_over_N45":float(np.linalg.norm(Xi)/N**4.5),
        "dXi_l2_over_N35":float(np.linalg.norm(dXi)/N**3.5),
    }


def exponent_balance(theta):
    low=3.5+max(0.5,theta)
    high=5.0-theta
    return low,high,max(low,high)


if __name__=="__main__":
    for p in [2,3,5,7,11]:
        for n in [1,p,2*p+1]:
            cp=ramanujan_sum(p,n)
            print(
                "cp2",
                p,n,
                cp*cp,
                (p-2)*cp+(p-1),
            )

    P=[2,3,5,7,11]
    for n in [1,2,3,4,5,6,10,12,30,60]:
        a=finite_axis_direct(P,n)[0]
        b=finite_axis_coeff(P,n)
        print("axis",n,a,b,a-b)

    for N in [20,40,80,160]:
        print("Xi",xi_scaling(N))

    for theta in [
        0.5,0.6,0.7,0.75,0.8,0.9,1.0
    ]:
        print("balance",theta,exponent_balance(theta))
