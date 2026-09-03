#!/usr/bin/env python3
"""
AMRAL RH v3.17 — structured pair-variance reference checks.

REFERENCE ONLY.
"""

from __future__ import annotations
import numpy as np


def pair_coefficients(values):
    n=len(values)
    out={}
    for h in range(-(n-1),n):
        if h>=0:
            out[h]=sum(values[k+h]*values[k] for k in range(n-h))
        else:
            hh=-h
            out[h]=sum(values[k]*values[k+hh] for k in range(n-hh))
    return out


def finite_pair_parseval(values, model):
    n=len(values)
    m=8*n+1
    alpha=np.arange(m)/m

    S=np.zeros(m,dtype=complex)
    for k,v in enumerate(values, start=1):
        S += v*np.exp(2j*np.pi*k*alpha)

    V=np.zeros(m,dtype=complex)
    coeff=pair_coefficients(values)
    Dcoeff={}
    for h in range(-(n-1),n):
        mod=model.get(h,0.0)
        Dcoeff[h]=coeff[h]-mod
        V += mod*np.exp(2j*np.pi*h*alpha)

    D=np.abs(S)**2-V
    lhs=float(np.mean(np.abs(D)**2))
    rhs=float(sum(abs(v)**2 for v in Dcoeff.values()))
    return lhs,rhs,lhs-rhs


def structured_identity(A,B,V):
    S=A+B
    lhs=np.abs(S)**2-V
    rhs=(np.abs(A)**2-V)+2*np.real(A*np.conjugate(B))+np.abs(B)**2
    return float(np.max(np.abs(lhs-rhs)))


def pvaa_bound(A,B,V):
    M=float(np.mean(np.abs(np.abs(A)**2-V)**2))
    X=float(np.mean(np.abs(A)**2*np.abs(B)**2))
    U=float(np.mean(np.abs(B)**4))
    actual=float(np.mean(np.abs(np.abs(A+B)**2-V)**2))
    envelope=3*M+12*X+3*U
    return actual,envelope,actual/envelope if envelope else 0.0


def selberg_l2_fraction(theta):
    return 1.0-theta


def ppeu_translation(eta):
    return {
        "pair_variance_exponent":3.0-eta,
        "Theta_upper_direct":1.0-eta/2.0,
        "EPV_exponent":4.0-eta,
        "V_exponent":5.0-eta,
    }


if __name__=="__main__":
    rng=np.random.default_rng(1234)
    values=rng.normal(size=12)
    model={h:0.2/(1+abs(h)) for h in range(-11,12)}
    print("parseval",finite_pair_parseval(values,model))

    m=257
    A=rng.normal(size=m)+1j*rng.normal(size=m)
    B=0.2*(rng.normal(size=m)+1j*rng.normal(size=m))
    V=np.abs(rng.normal(size=m))
    print("structured residual",structured_identity(A,B,V))
    print("PVAA",pvaa_bound(A,B,V))
