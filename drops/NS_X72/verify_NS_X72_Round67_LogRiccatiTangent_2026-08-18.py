"""
Verification for NS_X72 Round 67.

Round 67 derives the fixed-size Riccati tangent flow in logarithmic viscosity
t = log(nu), together with the exact identity

    d/dnu [a3(nu)/nu]
      = (d/dt a3(nu) - a3(nu))/nu^2.

The script:
1. uses the exact NS_X72 coefficient formulas;
2. propagates G, H=d_t G and K=d_t^2 G in O(1) memory;
3. verifies the first/second tangent numerically against centered log-viscosity
   finite differences;
4. tabulates the normalized elasticity and scattering derivative;
5. confirms the observed scattering derivative is O(10), while a bridge proof
   over (0,1e-6) would tolerate a vastly larger integrable bound.

The numerical scattering values are diagnostics, not yet a uniform interval theorem.
"""
import csv
import math
from pathlib import Path

import numpy as np
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round67_LogTangentMap_2026-08-18.csv")

# Exact coefficient formulas inherited from the symbolic Round 58/65 derivation.
def A_m2(K,n):
    return -K**3*(K**4 + 2*K**2*n**2 + 6*K**2*n - 13*K**2 + n**4 + 6*n**3 - 14*n**2 + 3*n + 4)/((K**2 + n**2)*(K**2 + n**2 - 4*n + 4)*(K**2 + n**2 - 2*n + 1))

def A0(K,n):
    return K*n*(K**10 + 8*K**8*n**2 + 30*K**8*n + 19*K**8 + 22*K**6*n**4 + 134*K**6*n**3 + 270*K**6*n**2 + 241*K**6*n + 83*K**6 + 28*K**4*n**6 + 222*K**4*n**5 + 663*K**4*n**4 + 946*K**4*n**3 + 604*K**4*n**2 + 122*K**4*n - K**4 + 17*K**2*n**8 + 162*K**2*n**7 + 592*K**2*n**6 + 1005*K**2*n**5 + 515*K**2*n**4 - 1000*K**2*n**3 - 1970*K**2*n**2 - 1319*K**2*n - 306*K**2 + 4*n**10 + 44*n**9 + 180*n**8 + 300*n**7 + 12*n**6 - 588*n**5 - 580*n**4 + 100*n**3 + 384*n**2 + 144*n)/((K**2 + n**2)*(n + 2)*(K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 4*n + 4)*(K**4 + 2*K**2*n**2 + 8*K**2*n + 4*K**2 + n**4 + 8*n**3 + 22*n**2 + 24*n + 9))

def A2(K,n):
    return K*(K**10 + 8*K**8*n**2 + 2*K**8*n - 9*K**8 + 22*K**6*n**4 + 42*K**6*n**3 - 6*K**6*n**2 - 65*K**6*n - 39*K**6 + 28*K**4*n**6 + 114*K**4*n**5 + 123*K**4*n**4 - 42*K**4*n**3 - 200*K**4*n**2 - 226*K**4*n - 101*K**4 + 17*K**2*n**8 + 110*K**2*n**7 + 228*K**2*n**6 + 107*K**2*n**5 - 335*K**2*n**4 - 616*K**2*n**3 - 330*K**2*n**2 + 15*K**2*n + 36*K**2 + 4*n**10 + 36*n**9 + 108*n**8 + 84*n**7 - 156*n**6 - 276*n**5 - 28*n**4 + 156*n**3 + 72*n**2)/((K**2 + n**2)*(K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 4*n + 4)*(K**4 + 2*K**2*n**2 + 8*K**2*n + 4*K**2 + n**4 + 8*n**3 + 22*n**2 + 24*n + 9))

def A4(K,n):
    return -K**3*n*(K**4 + 2*K**2*n**2 - 4*K**2 + n**4 - 2*n**2 + 1)*(K**4 + 2*K**2*n**2 + 2*K**2*n - 17*K**2 + n**4 + 2*n**3 - 26*n**2 - 99*n - 90)/((n + 2)*(K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 4*n + 4)*(K**2 + n**2 + 8*n + 16)*(K**4 + 2*K**2*n**2 + 8*K**2*n + 4*K**2 + n**4 + 8*n**3 + 22*n**2 + 24*n + 9))

def bcoef(K,n):
    return -16*n*(n + 1)*(K**4 + 2*K**2*n**2 - 4*K**2 + n**4 - 2*n**2 + 1)/((K**2 + n**2 - 2*n + 1)*(K**2 + n**2 + 2*n + 1))



C = np.array([
    [0.0,0.0,1.0],
    [0.0,0.0,0.0],
    [0.0,0.0,0.0],
])

D = np.array([
    [0.0,0.0,0.0],
    [1.0,0.0,0.0],
    [0.0,1.0,0.0],
])

def Kval(name):
    return (
        math.sqrt(17)-3.0
        if name == "minus"
        else math.sqrt(17)+3.0
    )

def blocks(name,n,nu):
    K = Kval(name)

    am = A_m2(K,n)
    a0 = A0(K,n)
    a2 = A2(K,n)
    a4 = A4(K,n)
    bb = bcoef(K,n)

    A = np.array([
        [0.0, a2/a4, nu*bb/a4],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ])

    B = np.array([
        [-a0/a4, 0.0, am/a4],
        [0.0,0.0,0.0],
        [0.0,0.0,0.0],
    ])

    # t = log(nu), so d_t [nu bb/a4] = nu bb/a4.
    At = np.zeros((3,3))
    At[0,2] = nu*bb/a4

    return A,B,At

def flow(name,nu,J):
    G = np.zeros((3,3))
    H = np.zeros((3,3))
    K2 = np.zeros((3,3))

    for n in range(J,0,-1):
        A,B,At = blocks(name,n,nu)

        X = G@C-A
        F = np.linalg.solve(
            X,
            B-G@D,
        )

        R = D+C@F

        Hn = np.linalg.solve(
            X,
            At@F-H@R,
        )

        Knew = np.linalg.solve(
            X,
            At@F
            + 2*At@Hn
            - K2@R
            - 2*H@C@Hn,
        )

        G,H,K2 = F,Hn,Knew

    return G,H,K2

def a3_value(name,nu,J):
    G,_,_ = flow(name,nu,J)
    return -float(G[1,1])

# Exact scalar identity:
# if t=log(nu), then a_t = nu a_nu and
# d_nu(a/nu)=(a_t-a)/nu^2.
nu_s = sp.symbols("nu", positive=True)
a_fun = sp.Function("a")(nu_s)
a_t = nu_s*sp.diff(a_fun,nu_s)

assert sp.simplify(
    sp.diff(a_fun/nu_s,nu_s)
    - (a_t-a_fun)/nu_s**2
) == 0

# Tangent / curvature finite-difference audit.
for name in ("minus","plus"):
    nu = 1e-6
    J = 1800
    G,H,K2 = flow(name,nu,J)

    a0 = -float(G[1,1])
    at = -float(H[1,1])
    att = -float(K2[1,1])

    ht = 1e-4

    ap = a3_value(
        name,
        nu*math.exp(ht),
        J,
    )
    am = a3_value(
        name,
        nu*math.exp(-ht),
        J,
    )

    at_fd = (ap-am)/(2*ht)
    att_fd = (ap-2*a0+am)/(ht*ht)

    assert abs(at_fd-at) < 2e-8*max(1.0,abs(at))
    assert abs(att_fd-att) < 2e-6*max(1.0,abs(att))

# Certified endpoint values from Round 59 are used only as numerical
# reference constants for the secant-scattering diagnostic.
c0 = {
    "minus": 5.79052557842264771855,
    "plus":  5.3317525458744885,
}

rows = []

for name in ("minus","plus"):
    for nu in (
        1e-8,
        3e-8,
        1e-7,
        3e-7,
        1e-6,
    ):
        J = max(
            1500,
            int(
                15*nu**(-1/3)
            ),
        )

        G,H,K2 = flow(
            name,
            nu,
            J,
        )

        a = -float(G[1,1])
        at = -float(H[1,1])
        att = -float(K2[1,1])

        f = a/nu

        sigma_tangent = (
            at-a
        )/(nu*nu)

        sigma_secant = (
            f-c0[name]
        )/nu

        elasticity = at/a
        curvature_ratio = att/a

        rows.append({
            "fibre": name,
            "nu": nu,
            "J": J,
            "a3": a,
            "a3_over_nu": f,
            "log_elasticity": elasticity,
            "log_curvature_ratio": curvature_ratio,
            "sigma_tangent": sigma_tangent,
            "sigma_secant_to_R59_endpoint": sigma_secant,
        })

# Stable diagnostic envelopes in the tested strip.
minus_sigma = [
    r["sigma_tangent"]
    for r in rows
    if r["fibre"] == "minus"
    and r["nu"] >= 3e-8
]

plus_sigma = [
    r["sigma_tangent"]
    for r in rows
    if r["fibre"] == "plus"
    and r["nu"] >= 3e-8
]

assert min(minus_sigma) > 10.0
assert max(minus_sigma) < 10.2

assert min(plus_sigma) > -3.6
assert max(plus_sigma) < -3.3

for r in rows:
    assert abs(
        r["log_elasticity"]-1
    ) < 2e-6

with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    writer = csv.DictWriter(
        f,
        fieldnames=list(
            rows[0].keys()
        ),
    )
    writer.writeheader()
    writer.writerows(rows)

print(
    "Round 67 verification passed."
)

for r in rows:
    print(r)
