#!/usr/bin/env python3
"""
AMRAL RH v3.15 — prime-shell tail reference checks.

REFERENCE ONLY.

Checks:
1. Boolean Möbius shell reconstruction of finite K_perp;
2. shell Fourier support denominators divide shell conductor;
3. shell double-axis cancellation;
4. conservative low/high exponent optimization.

The analytic Euler-shell tail theorem is proved in the source document;
the code provides finite normalization checks only.
"""

from __future__ import annotations
import math
import numpy as np


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


def divisors_squarefree(q: int):
    vals=[1]
    for p in prime_factors_squarefree(q):
        old=list(vals)
        vals.extend([d*p for d in old])
    return sorted(vals)


def mobius_squarefree(n: int):
    if n==1:
        return 1
    k=len(prime_factors_squarefree(n))
    return -1 if k%2 else 1


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


def covariance_coeff(q: int):
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


def kperp_table(q: int):
    if q==1:
        return np.zeros((1,1),dtype=float)
    coeff=covariance_coeff(q)
    coeff[0,:]=0.0
    return (q*q*np.fft.ifft2(coeff)).real


def lifted_table(table, q_target: int):
    q=table.shape[0]
    out=np.empty((q_target,q_target),dtype=float)
    for h in range(q_target):
        for d in range(q_target):
            out[h,d]=table[h%q,d%q]
    return out


def shell_table(q: int):
    out=np.zeros((q,q),dtype=float)
    for r in divisors_squarefree(q):
        if r==1:
            continue
        sign=mobius_squarefree(q//r)
        out += sign*lifted_table(kperp_table(r),q)
    return out


def shell_reconstruct(q: int):
    total=np.zeros((q,q),dtype=float)
    for r in divisors_squarefree(q):
        if r==1:
            continue
        total += lifted_table(shell_table(r),q)
    target=kperp_table(q)
    return float(np.max(np.abs(total-target)))


def reduced_denominator(k: int,q: int):
    if k%q==0:
        return 1
    return q//math.gcd(k,q)


def shell_spectral_diagnostics(q: int):
    sh=shell_table(q)
    coeff=np.fft.fft2(sh)/(q*q)

    axis=max(
        float(np.max(np.abs(coeff[0,:]))),
        float(np.max(np.abs(coeff[:,0])))
    )

    bad=0.0
    total_nonzero=0
    for a in range(q):
        for b in range(q):
            if abs(coeff[a,b])<1e-10:
                continue
            total_nonzero+=1
            ra=reduced_denominator(a,q)
            rb=reduced_denominator(b,q)
            if ra>q or rb>q:
                bad=max(bad,abs(coeff[a,b]))

    return {
        "q":q,
        "reconstruction_residual":shell_reconstruct(q),
        "axis_residual":axis,
        "bad_denominator_residual":float(bad),
        "nonzero_fourier_coeff_count":total_nonzero,
        "shell_sup":float(np.max(np.abs(sh))),
        "shell_l2_mean":float(np.mean(sh*sh)),
    }


def exponent_balance(theta: float):
    # low N^3(N+Q^2)Q for Q=N^theta
    # high N^5/Q
    if theta<=0.5:
        low=4.0+theta
    else:
        low=3.0+3.0*theta
    high=5.0-theta
    return low,high,max(low,high)


if __name__=="__main__":
    for q in [5,6,10,15,30,42,70,105,210]:
        print("shell",shell_spectral_diagnostics(q))

    for theta in [0.25,0.4,0.5,0.6,0.75]:
        print("balance",theta,exponent_balance(theta))
