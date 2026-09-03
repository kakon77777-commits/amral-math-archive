#!/usr/bin/env python3
"""
AMRAL RH v3.9 — uniform conductor Sobolev reference checks.

REFERENCE ONLY.

Checks:
1. finite-q H_d(q) from the rational coefficient convolution;
2. analytic finite-q Young/Jordan majorant;
3. periodic antiderivative Delta_d G = K;
4. Parseval H_d = mean |G|^2;
5. weighted summation-by-parts identity.

No full infinite-conductor fixed-power theorem is claimed.
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


def phi_squarefree(n: int):
    out=n
    for p in prime_factors_squarefree(n):
        out=out//p*(p-1)
    return out


def jordan2_squarefree(n: int):
    out=float(n*n)
    for p in prime_factors_squarefree(n):
        out *= 1.0-1.0/(p*p)
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


def K4_table(q: int):
    coeff=coefficient_table(q)
    arr=(q*q*np.fft.ifft2(coeff)).real
    return arr,coeff


def sobolev_from_coeff(coeff):
    q=coeff.shape[0]
    total=0.0
    for b in range(1,q):
        den=abs(1.0-np.exp(2j*math.pi*b/q))**2
        total += float(np.sum(np.abs(coeff[:,b])**2))/den
    return total


def periodic_antiderivative_from_coeff(coeff):
    q=coeff.shape[0]
    gc=np.zeros_like(coeff)
    for b in range(1,q):
        gc[:,b]=coeff[:,b]/(
            np.exp(2j*math.pi*b/q)-1.0
        )
    G=(q*q*np.fft.ifft2(gc)).real
    return G,gc


def A0(p: int):
    return 1.0+(p-1.0)**(-5.0/3.0)


def A1(p: int):
    return (
        (p-1.0)**(-4.0/3.0)
        * (
            2.0
            +(p-2.0)*(p-1.0)**(-4.0/3.0)
        )
    )


def finite_young_majorant(q: int):
    ps=prime_factors_squarefree(q)
    total=0.0
    for r in divisors_squarefree(q):
        if r==1:
            continue
        qcorr=1.0
        for p in ps:
            qcorr *= A1(p) if r%p==0 else A0(p)
        coeff_l2_upper=qcorr**3
        total += (
            coeff_l2_upper
            * jordan2_squarefree(r)
            / 12.0
        )
    return total


def endpoint_weight(N,n):
    if 1<=n<=N:
        return N
    if N<n<2*N:
        return 2*N-n
    return 0


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


def weighted_sbp_check(N,q):
    arr,coeff=K4_table(q)
    G,_gc=periodic_antiderivative_from_coeff(coeff)

    deltaG=np.roll(G,-1,axis=1)-G
    delta_res=float(np.max(np.abs(deltaG-arr)))

    direct=0.0
    sbp=0.0
    dOmega2=0.0
    Gbox2=0.0

    for h in range(0,2*N):
        for d in range(0,2*N):
            Om=omega_weight(N,h,d)
            Oprev=omega_weight(N,h,d-1)
            dOm=Om-Oprev

            direct += Om*arr[h%q,d%q]
            sbp -= dOm*G[h%q,d%q]

            dOmega2 += dOm*dOm
            Gbox2 += G[h%q,d%q]**2

    return {
        "N":N,
        "q":q,
        "direct_sum":direct,
        "sbp_sum":sbp,
        "sbp_residual":direct-sbp,
        "deltaG_residual":delta_res,
        "dOmega_l2":math.sqrt(dOmega2),
        "G_box_l2":math.sqrt(Gbox2),
        "cauchy_bound":math.sqrt(dOmega2*Gbox2),
    }


if __name__=="__main__":
    for q in [6,30,210,2310]:
        arr,coeff=K4_table(q)
        H=sobolev_from_coeff(coeff)
        G,gc=periodic_antiderivative_from_coeff(coeff)
        meanG=float(np.mean(G*G))
        upper=finite_young_majorant(q)
        print(
            "q",q,
            "H",H,
            "meanG2",meanG,
            "majorant",upper,
            "beta0",np.max(np.abs(coeff[:,0])),
        )

    for N,q in [(20,6),(40,6),(40,30),(80,30)]:
        print("sbp",weighted_sbp_check(N,q))
