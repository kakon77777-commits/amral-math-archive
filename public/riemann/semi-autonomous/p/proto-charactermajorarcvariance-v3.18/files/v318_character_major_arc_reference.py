#!/usr/bin/env python3
"""
AMRAL RH v3.18 — character-major-arc reference checks.

REFERENCE ONLY.

Checks:
1. character/Gauss-sum orthogonality for a prime modulus;
2. exact core-arc kernel scaling W_{x,u/x}(s)=x^s W_s(u);
3. pole-zero and pure-zero power scaling;
4. minor-arc fourth-moment exponent table.

No zero theorem or RH claim is made.
"""

from __future__ import annotations
import math
import cmath
import numpy as np


def e(x):
    return np.exp(2j*np.pi*x)


def primitive_root_prime(p):
    factors=[]
    n=p-1
    d=2
    while d*d<=n:
        if n%d==0:
            factors.append(d)
            while n%d==0:
                n//=d
        d+=1
    if n>1:
        factors.append(n)
    for g in range(2,p):
        if all(pow(g,(p-1)//r,p)!=1 for r in factors):
            return g
    raise ValueError("no primitive root")


def character_table_prime(p):
    """
    Characters indexed by k=0,...,p-2.
    chi_k(g^m)=exp(2pi i k m/(p-1)).
    """
    g=primitive_root_prime(p)
    logmap={}
    x=1
    for m in range(p-1):
        logmap[x]=m
        x=(x*g)%p

    table=np.zeros((p-1,p),dtype=complex)
    for k in range(p-1):
        for a in range(1,p):
            table[k,a]=np.exp(
                2j*np.pi*k*logmap[a]/(p-1)
            )
    return table


def gauss_sums_prime(p,chars):
    tau=np.zeros(p-1,dtype=complex)
    for k in range(p-1):
        tau[k]=sum(
            chars[k,a]*e(a/p)
            for a in range(1,p)
        )
    return tau


def character_energy_check(p,seed=1234):
    chars=character_table_prime(p)
    tau=gauss_sums_prime(p,chars)
    rng=np.random.default_rng(seed)
    z=rng.normal(size=p-1)+1j*rng.normal(size=p-1)

    lhs=0.0
    for a in range(1,p):
        val=sum(
            np.conjugate(tau[k])
            * chars[k,a]
            * z[k]
            for k in range(p-1)
        )/(p-1)
        lhs += abs(val)**2

    rhs=sum(
        abs(tau[k])**2*abs(z[k])**2
        for k in range(p-1)
    )/(p-1)

    return float(lhs),float(rhs),float(lhs-rhs)


def bump(v):
    v=np.asarray(v)
    out=np.zeros_like(v,dtype=float)
    mask=(v>0.5)&(v<2.0)
    x=(v[mask]-0.5)/1.5
    out[mask]=np.exp(-1.0/(x*(1.0-x)))
    return out


def W_scaled(s,u,grid_n=20000):
    v=np.linspace(0.50001,1.99999,grid_n)
    vals=bump(v)*np.exp(2j*np.pi*u*v)*np.exp((s-1)*np.log(v))
    return np.trapz(vals,v)


def W_direct(x,s,u,grid_n=20000):
    v=np.linspace(0.50001,1.99999,grid_n)
    t=x*v
    eps=u/x
    vals=(
        bump(v)
        * np.exp(2j*np.pi*eps*t)
        * np.exp((s-1)*np.log(t))
    )
    # dt = x dv
    return x*np.trapz(vals,v)


def kernel_scaling_check(x,s,u):
    direct=W_direct(x,s,u)
    scaled=(x**s)*W_scaled(s,u)
    return direct,scaled,abs(direct-scaled)


def kernel_energy_constants(rho,U=3.0,nu=1201):
    us=np.linspace(-U,U,nu)
    W1=np.array([W_scaled(1.0+0j,u,4000) for u in us])
    Wr=np.array([W_scaled(rho,u,4000) for u in us])
    C=np.trapz(np.abs(W1)**2*np.abs(Wr)**2,us)
    D=np.trapz(np.abs(Wr)**4,us)
    return float(C),float(D)


def direct_core_energies(x,rho,U=3.0,nu=401):
    us=np.linspace(-U,U,nu)
    eps=us/x
    W1=np.array([W_direct(x,1.0+0j,u,3000) for u in us])
    Wr=np.array([W_direct(x,rho,u,3000) for u in us])
    # integrate in epsilon, using d eps = du/x
    cross=np.trapz(np.abs(W1)**2*np.abs(Wr)**2,us)/x
    pure=np.trapz(np.abs(Wr)**4,us)/x
    return float(cross),float(pure)


def minor_exponents(theta):
    exponent=max(3.0-theta,31.0/12.0)
    saving=3.0-exponent
    return exponent,saving


if __name__=="__main__":
    for p in [5,7,11]:
        print("char",p,character_energy_check(p))

    s=0.83+7.2j
    for x in [20.0,50.0,100.0]:
        print("kernel",x,kernel_scaling_check(x,s,0.7)[2])

    rho=0.82+1.3j
    C,D=kernel_energy_constants(rho)
    for x in [20.0,40.0,80.0]:
        cross,pure=direct_core_energies(x,rho)
        print(
            "energy",x,
            cross/x**(1+2*rho.real),
            C,
            pure/x**(4*rho.real-1),
            D,
        )

    for theta in [0.1,0.2,0.3,5/12,0.45,0.5]:
        print("minor",theta,minor_exponents(theta))
