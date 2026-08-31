"""
Validated verification for NS_X72 Round 66.

Round 66 replaces the growing dense finite-core representation with a fixed-size
3x3 Jost/Riccati graph.

Certified result:
    a3_-(1e-7) > 0
    a3_+(1e-7) > 0

The certificate includes the infinite tail:
1. Round 56 monotone tail contraction gives a rigorous terminal graph norm ball.
2. The exact 3x3 Riccati graph is pulled back to n=1 using outward interval arithmetic.
3. The canonical central coefficient is read directly from G_1[1,1].

No large dense inverse and no finite-tail closure are used.
"""
from pathlib import Path
import csv
import hashlib
import math
import numpy as np
import mpmath as mp
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round66_RiccatiAnchorMap_2026-08-18.csv")

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

# Pinned dependencies.
assert sha256(
    "/mnt/data/verify_NS_X72_Round56_RigorousAdjointTail_2026-08-17.py"
) == "0dd1549c7b1f39f6915b172124d038890a10d84bd7802516b82083239010414d"

assert sha256(
    "/mnt/data/verify_NS_X72_Round59_EndpointJostGraph_2026-08-17.py"
) == "18a1d167b1d157ae9e1d127ad03f54c6efd3c820974546dd57bdd6f4099b05e2"

assert sha256(
    "/mnt/data/verify_NS_X72_Round65_BandedViscosityCertificate_2026-08-18.py"
) == "47a1b9fa556d3a8a00bac47664a78367bd50753c965fa058af5e960e23a989cf"

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

# ------------------------------------------------------------------
# Exact symbolic Riccati identity.
# ------------------------------------------------------------------

a,b,c,d = sp.symbols("a b c d")
gg = sp.Matrix(3,3,lambda i,j: sp.symbols(f"g{i}{j}"))

AA = sp.Matrix([
    [0,a,b],
    [1,0,0],
    [0,1,0],
])
BB = sp.Matrix([
    [c,0,d],
    [0,0,0],
    [0,0,0],
])
CC = sp.Matrix([
    [0,0,1],
    [0,0,0],
    [0,0,0],
])
DD = sp.Matrix([
    [0,0,0],
    [1,0,0],
    [0,1,0],
])

den = a*gg[2,0] + b - gg[0,0]

explicit = sp.Matrix([
    [
        -(a*gg[1,0]*gg[2,1]-a*gg[1,1]*gg[2,0]-b*gg[1,1]+c*gg[1,0]+gg[0,0]*gg[1,1]-gg[0,1]*gg[1,0])/den,
        -(a*gg[1,0]*gg[2,2]-a*gg[1,2]*gg[2,0]-b*gg[1,2]+gg[0,0]*gg[1,2]-gg[0,2]*gg[1,0])/den,
        -d*gg[1,0]/den,
    ],
    [
        (b*gg[2,1]-c*gg[2,0]-gg[0,0]*gg[2,1]+gg[0,1]*gg[2,0])/den,
        (b*gg[2,2]-gg[0,0]*gg[2,2]+gg[0,2]*gg[2,0])/den,
        -d*gg[2,0]/den,
    ],
    [
        -(a*gg[2,1]+c-gg[0,1])/den,
        -(a*gg[2,2]-gg[0,2])/den,
        -d/den,
    ],
])

matrix_form = (gg*CC-AA).inv()*(BB-gg*DD)

for i in range(3):
    for j in range(3):
        assert sp.simplify(matrix_form[i,j]-explicit[i,j]) == 0

# ------------------------------------------------------------------
# Outward interval graph certificate.
# ------------------------------------------------------------------

mp.iv.dps = 18

def K_iv(name):
    return (
        mp.iv.sqrt(17)-3
        if name == "minus"
        else mp.iv.sqrt(17)+3
    )

def terminal_q(name, nu, J):
    K = K_iv(name)
    nv = mp.iv.mpf([nu,nu])
    return (
        -A_m2(K,J)+A0(K,J)+A2(K,J)-A4(K,J)
    )/(-nv*bcoef(K,J))

def riccati_step(G, K, nu, n):
    am = A_m2(K,n)
    a0 = A0(K,n)
    a2 = A2(K,n)
    a4 = A4(K,n)
    bb = bcoef(K,n)

    aa = a2/a4
    bbv = nu*bb/a4
    cc = -a0/a4
    dd = am/a4

    g00,g01,g02 = G[0]
    g10,g11,g12 = G[1]
    g20,g21,g22 = G[2]

    Delta = aa*g20 + bbv - g00

    return [
        [
            -(aa*g10*g21-aa*g11*g20-bbv*g11+cc*g10+g00*g11-g01*g10)/Delta,
            -(aa*g10*g22-aa*g12*g20-bbv*g12+g00*g12-g02*g10)/Delta,
            -dd*g10/Delta,
        ],
        [
            (bbv*g21-cc*g20-g00*g21+g01*g20)/Delta,
            (bbv*g22-g00*g22+g02*g20)/Delta,
            -dd*g20/Delta,
        ],
        [
            -(aa*g21+cc-g01)/Delta,
            -(aa*g22-g02)/Delta,
            -dd/Delta,
        ],
    ]

def certify_point(name, nu, J):
    K = K_iv(name)
    nv = mp.iv.mpf([nu,nu])

    q = terminal_q(name,nu,J)
    q_hi = float(q.b)
    assert 0 < q_hi < 1

    # Round 56 tail contraction:
    # ||G_J||_inf <= q_J/(1-q_J).
    # Entrywise box enlargement by 2% is safe.
    terminal_radius = 1.02*q_hi/(1-q_hi)

    z = mp.iv.mpf([
        -terminal_radius,
        terminal_radius,
    ])
    G = [
        [z,z,z],
        [z,z,z],
        [z,z,z],
    ]

    for n in range(J,0,-1):
        G = riccati_step(
            G,
            K,
            nv,
            n,
        )

    u3 = G[1][1]

    lo = float(u3.a)
    hi = float(u3.b)

    assert math.isfinite(lo)
    assert math.isfinite(hi)
    assert hi < 0

    return {
        "kind": "validated_point",
        "fibre": name,
        "nu": nu,
        "J": J,
        "q_J_upper": q_hi,
        "terminal_radius": terminal_radius,
        "u3_lower": lo,
        "u3_upper": hi,
        "a3_lower": -hi,
        "a3_upper": -lo,
        "a3_over_nu_mid":
            (-(lo+hi)/2)/nu,
    }

validated = [
    certify_point(
        "minus",
        1e-7,
        8000,
    ),
    certify_point(
        "plus",
        1e-7,
        12000,
    ),
]

assert validated[0]["a3_lower"] > 5.7905265e-7
assert validated[1]["a3_lower"] > 5.3317441e-7

# ------------------------------------------------------------------
# O(1)-memory double diagnostics far deeper into the singular strip.
# ------------------------------------------------------------------

def coeff_double(name,n,nu):
    K = (
        math.sqrt(17)-3
        if name == "minus"
        else math.sqrt(17)+3
    )
    am = A_m2(K,n)
    a0 = A0(K,n)
    a2 = A2(K,n)
    a4 = A4(K,n)
    bb = bcoef(K,n)

    return (
        a2/a4,
        nu*bb/a4,
        -a0/a4,
        am/a4,
    )

def step_double(G,name,n,nu):
    aa,bbv,cc,dd = coeff_double(
        name,n,nu
    )

    g00,g01,g02 = G[0]
    g10,g11,g12 = G[1]
    g20,g21,g22 = G[2]

    Delta = aa*g20 + bbv - g00

    return np.array([
        [
            -(aa*g10*g21-aa*g11*g20-bbv*g11+cc*g10+g00*g11-g01*g10)/Delta,
            -(aa*g10*g22-aa*g12*g20-bbv*g12+g00*g12-g02*g10)/Delta,
            -dd*g10/Delta,
        ],
        [
            (bbv*g21-cc*g20-g00*g21+g01*g20)/Delta,
            (bbv*g22-g00*g22+g02*g20)/Delta,
            -dd*g20/Delta,
        ],
        [
            -(aa*g21+cc-g01)/Delta,
            -(aa*g22-g02)/Delta,
            -dd/Delta,
        ],
    ],dtype=float)

def diagnostic(name,nu,mult=10):
    J = max(
        100,
        int(mult*nu**(-1/3)),
    )

    G = np.zeros((3,3))

    for n in range(J,0,-1):
        G = step_double(
            G,
            name,
            n,
            nu,
        )

    a3 = -float(G[1,1])

    return {
        "kind": "double_diagnostic",
        "fibre": name,
        "nu": nu,
        "J": J,
        "q_J_upper": "",
        "terminal_radius": "",
        "u3_lower": "",
        "u3_upper": "",
        "a3_lower": "",
        "a3_upper": "",
        "a3_over_nu_mid": a3/nu,
    }

diagnostics = []

for nu in (
    1e-8,
    1e-10,
):
    for name in (
        "minus",
        "plus",
    ):
        diagnostics.append(
            diagnostic(
                name,
                nu,
            )
        )

# Endpoint consistency diagnostics.
assert abs(
    diagnostics[0]["a3_over_nu_mid"]
    - 5.790525578422648
) < 2e-6

assert abs(
    diagnostics[1]["a3_over_nu_mid"]
    - 5.331752545874489
) < 2e-6

rows = validated+diagnostics

with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    fields = [
        "kind",
        "fibre",
        "nu",
        "J",
        "q_J_upper",
        "terminal_radius",
        "u3_lower",
        "u3_upper",
        "a3_lower",
        "a3_upper",
        "a3_over_nu_mid",
    ]
    writer = csv.DictWriter(
        f,
        fieldnames=fields,
    )
    writer.writeheader()
    writer.writerows(rows)

print(
    "Round 66 fixed-size Riccati verification passed."
)

for row in rows:
    print(row)
