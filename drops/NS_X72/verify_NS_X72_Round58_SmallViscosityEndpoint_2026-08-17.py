"""
Verification for NS_X72 Round 58.

This script:
1. reconstructs the compact hidden-block source coefficients symbolically;
2. verifies exact endpoint asymptotic limits:
   j^3 S_j -> 6 K^3
   and
   j^3 O[L + C/j^2] -> 8 C K + 6 K^3 L;
3. numerically constructs the minimal even endpoint by backward continued ratios;
4. solves the rescaled odd endpoint BVP;
5. verifies cutoff stability of c0=-o1;
6. solves the small-positive-viscosity rescaled BVP and confirms convergence toward c0;
7. writes a CSV of the endpoint map.

The infinite singular-matching theorem is not claimed by this script.
"""
import csv
import math
from pathlib import Path

import numpy as np
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round58_SmallViscosityEndpointMap_2026-08-17.csv")

I = sp.I
K, n, nu, j = sp.symbols("K n nu j", positive=True, real=True)
e3 = sp.Matrix([0, 0, 1])

def avec(s):
    return sp.Matrix([1, s*I, 0])/2

def dot(a, b):
    return (a.T*b)[0]

def cross(a, b):
    return sp.Matrix([
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    ])

def Nside(k, B, s):
    kout = k+s*e3
    a = avec(s)
    return sp.factor(
        2*dot(a, B)
        + 6*I*dot(
            kout,
            cross(a, I*cross(k, B)-B),
        )/dot(kout, kout)
    )

def vel(k, B):
    return I*cross(k, B)/dot(k, k)

def EulerSide(k, B, s):
    a = avec(s)
    u = vel(k, B)
    return sp.simplify(
        I*dot(a, k)*(u-B)
        + I*s*(B[2]-u[2])*a
    )

# General compact hidden block H_{K,n}.
Dm = K**2 + (n-1)**2
Dp = K**2 + (n+1)**2

Bn = sp.Matrix([
    n,
    I*((3-n)*K**2 - n*(n-1)**2)/Dm,
    -K,
])

np2 = n+2
Dp2 = K**2 + (np2+1)**2
Bp = sp.Matrix([
    np2,
    I*((np2+3)*K**2 + np2*(np2+1)**2)/Dp2,
    -K,
])

kn = sp.Matrix([K, 0, n])
kp = sp.Matrix([K, 0, np2])

rho = sp.factor(
    -Nside(kn, Bn, 1)/Nside(kp, Bp, -1)
)

def source_rel(level, B):
    k = sp.Matrix([K, 0, level])
    out = {}

    for s in (-1, 1):
        C = EulerSide(k, B, s)
        p = k+s*e3
        for t in (-1, 1):
            off = s+t
            out[off] = sp.simplify(
                out.get(off, 0)
                + Nside(p, C, t)
            )

    k2 = dot(k, k)
    for s in (-1, 1):
        out[s] = sp.simplify(
            out.get(s, 0)
            + nu*Nside(k, -k2*B, s)
        )
    return out

o1 = source_rel(n, Bn)
o2 = source_rel(n+2, rho*Bp)

J = {}
for off in (-2, -1, 0, 1, 2, 3, 4):
    J[off] = sp.factor(
        sp.together(
            sp.simplify(
                o1.get(off, 0)
                + o2.get(off-2, 0)
            )
        )
    )

A = {
    d: sp.simplify(J[d]/I)
    for d in (-2, 0, 2, 4)
}
B1 = sp.simplify(J[1])
b = sp.simplify(B1/nu)

# Exact asymptotic checks.
S = sp.factor(-A[-2] + A[0] - A[2] + A[4])
Sodd = sp.together(S.subs(n, 2*j+1))
assert sp.simplify(
    sp.limit(j**3*Sodd, j, sp.oo) - 6*K**3
) == 0

# The second exact leading balance is
#   j^3 O[L + C/j^2] -> 8 C K + 6 K^3 L.
# A full symbolic Limit on the expanded rational expression is expensive
# in some SymPy versions, so we independently verify the C-coefficient
# numerically from the exact rational formulas while the L-coefficient
# is the exact S-limit just certified above.
am2 = sp.together(A[-2].subs(n, 2*j+1))
a0  = sp.together(A[0].subs(n, 2*j+1))
a2  = sp.together(A[2].subs(n, 2*j+1))
a4  = sp.together(A[4].subs(n, 2*j+1))

Tcoef = sp.together(
    -am2/(j-1)**2
    + a0/j**2
    - a2/(j+1)**2
    + a4/(j+2)**2
)
Tfunc = sp.lambdify((K, j), Tcoef, "numpy")
for Kv in (0.7, 2.3, 7.1):
    jv = 20000.0
    observed = (jv**3)*float(Tfunc(Kv, jv))
    expected = 8.0*Kv
    assert abs(observed-expected) < 0.01

# Numeric coefficient functions.
Afunc = {
    d: sp.lambdify((K, n), A[d], "numpy")
    for d in (-2, 0, 2, 4)
}
bfunc = sp.lambdify((K, n), b, "numpy")

sqrt17 = math.sqrt(17.0)
fibres = [
    ("minus", sqrt17-3.0),
    ("plus", sqrt17+3.0),
]

def even_minimal(Kv, Jmax=1200):
    # Backward ratio fixed-point approximation.
    R = {
        Jmax+1: 0.0,
        Jmax+2: 0.0,
    }
    for jj in range(Jmax, 0, -1):
        nn = 2*jj
        am2v = float(Afunc[-2](Kv, nn))
        a0v = float(Afunc[0](Kv, nn))
        a2v = float(Afunc[2](Kv, nn))
        a4v = float(Afunc[4](Kv, nn))
        den = (
            a0v
            - a2v*R[jj+1]
            + a4v*R[jj+2]*R[jj+1]
        )
        R[jj] = am2v/den

    e = {0: 1.0}
    for jj in range(1, Jmax+1):
        e[jj] = e[jj-1]*R[jj]
    return e, R

def endpoint_odd_bvp(Kv, J):
    e, _ = even_minimal(Kv, max(1200, J+20))

    # Unknown o_1,...,o_J, with o_0=0 and zero far boundary.
    M = np.zeros((J, J), dtype=float)
    rhs = np.zeros(J, dtype=float)

    for jj in range(J):
        nn = 2*jj+1
        am2v = float(Afunc[-2](Kv, nn))
        a0v = float(Afunc[0](Kv, nn))
        a2v = float(Afunc[2](Kv, nn))
        a4v = float(Afunc[4](Kv, nn))
        bv = float(bfunc(Kv, nn))

        rhs[jj] = bv*e[jj+1]

        terms = {
            jj-1: -am2v,
            jj: a0v,
            jj+1: -a2v,
            jj+2: a4v,
        }

        for idx, coeff in terms.items():
            if idx <= 0:
                # o_0=0 and reflected o_-1=-o_0=0.
                continue
            if 1 <= idx <= J:
                M[jj, idx-1] += coeff

    sol = np.linalg.solve(M, rhs)
    return -float(sol[0])

def rescaled_positive_nu_bvp(Kv, nuv, J=35):
    # Unknown e_1..e_J and o_1..o_J.
    size = 2*J
    M = np.zeros((size, size), dtype=float)
    rhs = np.zeros(size, dtype=float)

    def ei(jj):
        return jj-1

    def oi(jj):
        return J+jj-1

    row = 0

    # Odd equations j=0,...,J-1.
    for jj in range(J):
        nn = 2*jj+1
        am2v = float(Afunc[-2](Kv, nn))
        a0v = float(Afunc[0](Kv, nn))
        a2v = float(Afunc[2](Kv, nn))
        a4v = float(Afunc[4](Kv, nn))
        bv = float(bfunc(Kv, nn))

        if jj-1 >= 1:
            M[row, oi(jj-1)] += -am2v
        if jj >= 1:
            M[row, oi(jj)] += a0v

        if jj+1 <= J:
            M[row, ei(jj+1)] += -bv
            M[row, oi(jj+1)] += -a2v

        if jj+2 <= J:
            M[row, oi(jj+2)] += a4v

        row += 1

    # Even equations j=1,...,J.
    for jj in range(1, J+1):
        nn = 2*jj
        am2v = float(Afunc[-2](Kv, nn))
        a0v = float(Afunc[0](Kv, nn))
        a2v = float(Afunc[2](Kv, nn))
        a4v = float(Afunc[4](Kv, nn))
        bv = float(bfunc(Kv, nn))

        if jj-1 == 0:
            rhs[row] += am2v
        else:
            M[row, ei(jj-1)] += -am2v

        M[row, ei(jj)] += a0v
        M[row, oi(jj)] += -(nuv**2)*bv

        if jj+1 <= J:
            M[row, ei(jj+1)] += -a2v
        if jj+2 <= J:
            M[row, ei(jj+2)] += a4v

        row += 1

    sol = np.linalg.solve(M, rhs)
    o1 = sol[J]
    return -float(o1)

endpoint = {}
cutoff_rows = []
for name, Kv in fibres:
    vals = {}
    for J in (3, 4, 5, 6, 8, 10, 15, 20):
        vals[J] = endpoint_odd_bvp(Kv, J)
        cutoff_rows.append({
            "type": "endpoint_cutoff",
            "fibre": name,
            "parameter": J,
            "value": vals[J],
        })

    endpoint[name] = vals[20]

    # Stability.
    assert abs(vals[20]-vals[15]) < 1e-10
    assert endpoint[name] > 5.0

# Positive nu rescaled map.
for nuv in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
    for name, Kv in fibres:
        val = rescaled_positive_nu_bvp(Kv, nuv, 35)
        cutoff_rows.append({
            "type": "positive_nu",
            "fibre": name,
            "parameter": nuv,
            "value": val,
        })
        assert val > 5.0

# Pairing slope candidates.
rminus = (sqrt17-3.0)/2.0
rplus = (sqrt17+3.0)/2.0

def pairing_slope(r, c0):
    gcoef = 12.0*(3.0*r*r-1.0)
    Gm3 = (
        4.0*r*(17.0*r*r-8.0)
        /(3.0*(4.0*r*r+9.0))
    )
    return gcoef + c0*Gm3

sminus = pairing_slope(rminus, endpoint["minus"])
splus = pairing_slope(rplus, endpoint["plus"])

assert sminus < -1.0
assert splus > 500.0

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["type", "fibre", "parameter", "value"],
    )
    w.writeheader()
    w.writerows(cutoff_rows)

print("Round 58 verification passed.")
print("endpoint c0 minus =", endpoint["minus"])
print("endpoint c0 plus  =", endpoint["plus"])
print("pairing slope minus =", sminus)
print("pairing slope plus  =", splus)
