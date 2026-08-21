"""
Numerical / structural verification for NS_X72 Round 57.

This script checks:
1. physical finite-section canonical adjoint coefficient a3(nu)
   without compact hidden-block coordinates;
2. positivity on a logarithmic viscosity grid;
3. cutoff stability at selected points;
4. endpoint diagnostics a3/nu and nu*a3;
5. the structural tail scaling q_n(K,nu)=q_n(K,1)/nu
   at the formula level is documented in the paper and follows
   because only J1 is proportional to nu.

The global all-nu positivity is NOT claimed as a rigorous theorem here.
"""
import math
import csv
from pathlib import Path

import numpy as np

OUT = Path("/mnt/data/NS_X72_Round57_ViscosityMap_2026-08-17.csv")

def dot(a, b):
    return np.dot(a, b)

def cross(a, b):
    return np.cross(a, b)

e3 = np.array([0.0+0.0j, 0.0, 1.0])

def avec(s):
    return np.array([1.0, 1.0j*s, 0.0], dtype=complex)/2.0

def Nside(K, level, B, s):
    k = np.array([K, 0.0, float(level)], dtype=complex)
    kout = k+s*e3
    a = avec(s)
    return (
        2*dot(a, B)
        + 6j*dot(
            kout,
            cross(a, 1j*cross(k, B)-B),
        )/dot(kout, kout)
    )

def vel(K, level, B):
    k = np.array([K, 0.0, float(level)], dtype=complex)
    return 1j*cross(k, B)/dot(k, k)

def EulerSide(K, level, B, s):
    k = np.array([K, 0.0, float(level)], dtype=complex)
    a = avec(s)
    u = vel(K, level, B)
    return (
        1j*dot(a, k)*(u-B)
        + 1j*s*(B[2]-u[2])*a
    )

def source_single(K, level, B, nu):
    out = {}
    for s in (-1, 1):
        C = EulerSide(K, level, B, s)
        p = level+s
        for t in (-1, 1):
            off = s+t
            out[off] = out.get(off, 0.0) + Nside(K, p, C, t)

    k2 = K*K + level*level
    for s in (-1, 1):
        out[s] = (
            out.get(s, 0.0)
            + nu*Nside(K, level, -k2*B, s)
        )
    return out

def divfree_basis(K, level):
    den = math.sqrt(K*K + level*level)
    return (
        np.array([level/den, 0.0, -K/den], dtype=complex),
        np.array([0.0, 1.0, 0.0], dtype=complex),
    )

def physical_matrices(K, N, nu):
    levels = list(range(-N, N+1))
    basis = []
    for n in levels:
        v1, v2 = divfree_basis(K, n)
        basis.append((n, v1))
        basis.append((n, v2))

    nouts = list(range(-N-1, N+2))
    Nmat = np.zeros((len(nouts), len(basis)), dtype=complex)
    for j, (n, B) in enumerate(basis):
        for s in (-1, 1):
            mm = n+s
            if mm in nouts:
                Nmat[nouts.index(mm), j] += Nside(K, n, B, s)

    souts = list(range(-N-2, N+3))
    Smat = np.zeros((len(souts), len(basis)), dtype=complex)
    for j, (n, B) in enumerate(basis):
        out = source_single(K, n, B, nu)
        for off, val in out.items():
            mm = n+off
            if mm in souts:
                Smat[souts.index(mm), j] += val

    return nouts, Nmat, souts, Smat

def canonical_a3(K, N, nu, tol=1e-12):
    nouts, Nmat, souts, Smat = physical_matrices(K, N, nu)

    U0, S0, Vh0 = np.linalg.svd(Nmat, full_matrices=True)
    rankN = int(np.sum(S0 > tol*S0[0]))
    Q = Vh0.conj().T[:, rankN:]
    A = Smat @ Q

    U, S, Vh = np.linalg.svd(A, full_matrices=True)
    rankA = int(np.sum(S > tol*S[0]))
    left = U[:, rankA:]

    mask = np.array([
        1.0 if abs(m) > N-6 else 0.0
        for m in souts
    ])
    B = left.conj().T @ (mask[:, None]*left)
    vals, vecs = np.linalg.eigh(B)
    loc = left @ vecs[:, :2]

    M = np.array([
        [loc[souts.index(0), j] for j in range(2)],
        [loc[souts.index(1), j] for j in range(2)],
    ], dtype=complex)

    can = loc @ np.linalg.inv(M)
    psi_plus = can[:, 0]

    return float(psi_plus[souts.index(3)].imag)

sqrt17 = math.sqrt(17)
rminus = (sqrt17-3)/2
rplus = (sqrt17+3)/2
fibres = [
    ("minus", 2*rminus),
    ("plus", 2*rplus),
]

# Logarithmic grid.
nus = np.logspace(-5, 3, 33)

rows = []
for nu in nus:
    # Small nu requires a deeper section because the contractive tail starts farther out.
    if nu < 3e-5:
        N = 100
    elif nu < 3e-4:
        N = 80
    elif nu < 3e-3:
        N = 70
    else:
        N = 55

    vals = {}
    for name, K in fibres:
        vals[name] = canonical_a3(K, N, float(nu))
        assert vals[name] > 0.0

    rows.append({
        "nu": float(nu),
        "N": N,
        "a3_minus": vals["minus"],
        "a3_plus": vals["plus"],
    })

# Add selected endpoint diagnostics.
extra_nus = [1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0, 1000.0, 10000.0]
extra = {}
for nu in extra_nus:
    if nu <= 1e-5:
        N = 110
    elif nu < 1e-3:
        N = 85
    else:
        N = 60
    vals = {}
    for name, K in fibres:
        vals[name] = canonical_a3(K, N, nu)
        assert vals[name] > 0.0
    extra[nu] = vals

# Cutoff stability at representative points.
for nu in (1e-3, 1e-2, 0.1, 1.0, 10.0):
    for name, K in fibres:
        a = canonical_a3(K, 45, nu)
        b = canonical_a3(K, 60, nu)
        # Absolute tolerance chosen far below the sign margin.
        assert abs(a-b) < 5e-7

# Endpoint positive diagnostics.
small_minus = extra[1e-6]["minus"]/1e-6
small_plus = extra[1e-6]["plus"]/1e-6
large_minus = extra[10000.0]["minus"]*10000.0
large_plus = extra[10000.0]["plus"]*10000.0

assert small_minus > 5.0
assert small_plus > 5.0
assert large_minus > 0.04
assert large_plus > 0.08

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["nu", "N", "a3_minus", "a3_plus"])
    w.writeheader()
    w.writerows(rows)

print("Round 57 continuation diagnostics passed.")
print("small-nu a3/nu:", small_minus, small_plus)
print("large-nu nu*a3:", large_minus, large_plus)

for name in ("minus", "plus"):
    arr = np.array([r[f"a3_{name}"] for r in rows])
    j = int(np.argmax(arr))
    print(
        name,
        "grid maximum",
        arr[j],
        "at nu",
        rows[j]["nu"],
    )
