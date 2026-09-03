#!/usr/bin/env python3
"""
AMRAL RH v3.3 — positive spectral-kernel reference checks.

REFERENCE ONLY.

Checks:
1. exact |B_h(delta+i y)|^2 formula;
2. positivity of fixed spectral-window coefficients;
3. translated-window U^-4 asymptotic;
4. normalized p=1,2,3 resolvent kernel Fourier checks.
"""

from __future__ import annotations

import math
import cmath
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma


def B_h(h: float, z: complex) -> complex:
    if abs(z) < 1e-12:
        return h*h
    return 2.0*(cmath.cosh(h*z)-1.0)/(z*z)


def B_abs2_closed(h: float, delta: float, y: float) -> float:
    return (
        4.0
        * (math.cosh(h*delta)-math.cos(h*y))**2
        / (delta*delta+y*y)**2
    )


def B_abs2_direct(h: float, delta: float, y: float) -> float:
    return abs(B_h(h,complex(delta,y)))**2


def xi_compact_band(
    h: float,
    delta: float,
    gamma0: float,
    center: float,
    width: float = 1.0,
) -> float:
    lo=center-width
    hi=center+width
    return quad(
        lambda tau:
            B_abs2_closed(h,delta,gamma0-tau),
        lo,hi,
        epsabs=1e-12,epsrel=1e-12,limit=200
    )[0]


def cp(p: float) -> float:
    return gamma(p)/(math.sqrt(math.pi)*gamma(p-0.5))


def omega_p(tau: float, p: float) -> float:
    return cp(p)*(1.0+tau*tau)**(-p)


def kernel_p_numeric(d: float, p: float) -> float:
    # Even cosine transform with oscillatory quadrature.
    d = abs(float(d))
    if d == 0.0:
        return 2.0*quad(
            lambda tau: omega_p(tau,p),
            0.0,np.inf,
            epsabs=2e-13,epsrel=2e-13,limit=500
        )[0]

    val, _err = quad(
        lambda tau: omega_p(tau,p),
        0.0,np.inf,
        weight="cos", wvar=d,
        epsabs=2e-13,limit=700
    )
    return 2.0*val


def kernel_p_closed_integer(d: float, m: int) -> float:
    r=abs(d)
    if m==1:
        return math.exp(-r)
    if m==2:
        return (1+r)*math.exp(-r)
    if m==3:
        return (r*r+3*r+3)/3.0*math.exp(-r)
    raise ValueError("implemented for m=1,2,3")


if __name__=="__main__":
    h=math.log(2.0)

    for delta in [0.01,0.1,0.25,0.49]:
        for y in [0.0,1.0,14.134725,50.0]:
            a=B_abs2_direct(h,delta,y)
            b=B_abs2_closed(h,delta,y)
            print("B",delta,y,a,b,a-b)

    delta=0.1
    gamma0=14.134725
    for U in [20.0,50.0,100.0,200.0,500.0]:
        xi=xi_compact_band(h,delta,gamma0,U,0.5)
        print("moving",U,xi,U**4*xi)

    for m in [1,2,3]:
        for d in [0.0,0.2,0.7,1.5]:
            n=kernel_p_numeric(d,float(m))
            c=kernel_p_closed_integer(d,m)
            print("kernel",m,d,n,c,n-c)
