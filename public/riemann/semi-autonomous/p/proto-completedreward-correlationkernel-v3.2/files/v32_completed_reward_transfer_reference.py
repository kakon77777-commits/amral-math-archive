#!/usr/bin/env python3
"""
AMRAL RH v3.2 — completed-reward transfer reference checks.

REFERENCE ONLY.

Checks:
1. strict positivity of Phi_{h,delta}(gamma) over finite grids;
2. direct cosine-transform formula vs positive convolution formula;
3. completed-reward nonoscillatory mode coefficient.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad


def tent_hat(h: float, xi: float) -> float:
    if abs(xi) < 1e-10:
        return h*h
    return 2.0*(1.0-math.cos(h*xi))/(xi*xi)


def C_h(h: float, d: float) -> float:
    r=abs(d)
    if r >= 2*h:
        return 0.0
    if r <= h:
        return 2*h**3/3 - h*r*r + r**3/2
    return (2*h-r)**3/6


def phi_direct(h: float, delta: float, gamma: float) -> float:
    a=1.0-delta
    return 2.0*quad(
        lambda r:
            math.exp(-a*r)*C_h(h,r)*math.cos(gamma*r),
        0.0,2*h,
        epsabs=1e-12,epsrel=1e-12,limit=220
    )[0]


def phi_convolution(h: float, delta: float, gamma: float) -> float:
    """
    Fourier product-convolution:
      FT[e^{-a|r|} C_h(r)](gamma)
      = (1/2pi) int 2a/(a^2+xi^2) |T_hat(gamma-xi)|^2 dxi.
    """
    a=1.0-delta

    def integrand(xi):
        lor=2.0*a/(a*a+xi*xi)
        th=tent_hat(h,gamma-xi)
        return lor*th*th/(2.0*math.pi)

    # scipy handles infinite tails well because integrand ~ xi^-6
    return quad(
        integrand,
        -np.inf,np.inf,
        epsabs=2e-11,epsrel=2e-11,limit=400
    )[0]


def nonosc_completion_rate(
    h: float,
    delta: float,
    gamma: float,
    amp_abs: float,
    t: float,
) -> float:
    return (
        2.0*amp_abs*amp_abs
        * math.exp(2.0*delta*(t-h))
        * phi_direct(h,delta,gamma)
    )


def unit_block_nonosc_reward(
    h: float,
    delta: float,
    gamma: float,
    amp_abs: float,
    T: float,
) -> float:
    phi=phi_direct(h,delta,gamma)
    if abs(delta)<1e-15:
        return 2.0*amp_abs*amp_abs*phi
    return (
        amp_abs*amp_abs
        * math.exp(-2.0*delta*h)
        * phi
        * (math.exp(2.0*delta)-1.0)/delta
        * math.exp(2.0*delta*T)
    )


if __name__ == "__main__":
    h=math.log(2.0)
    for delta in [0.01,0.1,0.25,0.49]:
        vals=[]
        for gamma in [0,1,5,14.134725,25,50,100]:
            d=phi_direct(h,delta,gamma)
            c=phi_convolution(h,delta,gamma)
            vals.append(d)
            print(delta,gamma,d,c,d-c)
        print("minimum",delta,min(vals))
