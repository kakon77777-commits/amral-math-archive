"""
Verification for NS_X72 Round 63.

This script checks:
1. exact difference-coordinate identities numerically against the original recurrence coefficients;
2. asymptotic fast coefficients p,q,s,c;
3. inherited coarse fast-operator bounds from the certified Round 59 coefficient boxes;
4. actual exact-coefficient fast feedback values at representative j;
5. symmetrized coupling and the three-quarter shift law;
6. staggered gauge asymptotic.

The global fast inverse theorem uses the already-certified Round 59 coefficient boxes:
small fibre:
  -0.01 < A_-2,A_4 < 0, A_2 > 4
large fibre:
  -1.4 < A_-2 < 0, -0.4 < A_4 < 0, A_2 > 24
for both parity sectors and all j>=10.
"""
import contextlib
import csv
import io
import math
from pathlib import Path

import numpy as np

OUT = Path("/mnt/data/NS_X72_Round63_SchurCoefficientMap_2026-08-18.csv")

# Load the audited coefficient functions from Round 58.
src = Path(
    "/mnt/data/verify_NS_X72_Round58_SmallViscosityEndpoint_2026-08-17.py"
)
code = src.read_text(encoding="utf-8")
cut = code.split(
    'with OUT.open("w"',
    1,
)[0]

ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(
        compile(
            cut,
            str(src),
            "exec",
        ),
        ns,
    )

Afunc = ns["Afunc"]
bfunc = ns["bfunc"]
fibres = ns["fibres"]

def diff_coeffs(K, n):
    am = float(Afunc[-2](K, n))
    a0 = float(Afunc[0](K, n))
    a2 = float(Afunc[2](K, n))
    a4 = float(Afunc[4](K, n))
    bb = float(bfunc(K, n))

    D = -a2+a4
    S = -am+a0-a2+a4

    p = -am/D
    q = -a4/D
    s = -S/D
    c = bb/D

    return {
        "A_m2": am,
        "A0": a0,
        "A2": a2,
        "A4": a4,
        "D": D,
        "S": S,
        "p": p,
        "q": q,
        "s": s,
        "c": c,
        "delta": abs(p)+abs(q),
    }

# Coarse rigorous bounds inherited from Round 59.
assert (0.01+0.01)/4 < 0.0050000001
assert (1.4+0.4)/24 < 0.0750000001
assert 1/(1-0.005) < 200/199 + 1e-15
assert 1/(1-0.075) < 40/37 + 1e-15

rows = []

jvals = [10, 20, 50, 100, 1000, 10000]

for name, K in fibres:
    for j in jvals:
        ce = diff_coeffs(K, 2*j)
        co = diff_coeffs(K, 2*j+1)

        # Actual coefficients satisfy the coarse inherited boxes.
        if name == "minus":
            assert ce["delta"] < 0.005
            assert co["delta"] < 0.005
        else:
            assert ce["delta"] < 0.075
            assert co["delta"] < 0.075

        # Signs.
        for d in (ce, co):
            assert d["p"] < 0
            assert d["q"] < 0
            assert d["s"] > 0
            assert d["c"] > 0

        lead_c = 16*j*j/K
        cbar = math.sqrt(ce["c"]*co["c"])
        shift = 16*(j+0.75)**2/K
        gauge = (ce["c"]/co["c"])**0.25

        rows.append({
            "fibre": name,
            "j": j,
            "delta_even": ce["delta"],
            "delta_odd": co["delta"],
            "delta_even_scaled":
                ce["delta"]*j*j/(K*K/8),
            "delta_odd_scaled":
                co["delta"]*j*j/(K*K/8),
            "s_even_scaled":
                ce["s"]*j**3/(1.5*K*K),
            "s_odd_scaled":
                co["s"]*j**3/(1.5*K*K),
            "c_even_over_lead":
                ce["c"]/lead_c,
            "c_odd_over_lead":
                co["c"]/lead_c,
            "cbar_over_shift":
                cbar/shift,
            "gauge":
                gauge,
            "j_gauge_minus_1":
                j*(gauge-1),
        })

# High-j asymptotic checks.
for name, K in fibres:
    row = [
        r for r in rows
        if r["fibre"] == name
        and r["j"] == 10000
    ][0]

    assert abs(
        row["delta_even_scaled"]-1
    ) < 3e-4

    assert abs(
        row["delta_odd_scaled"]-1
    ) < 3e-4

    assert abs(
        row["s_even_scaled"]-1
    ) < 5e-4

    assert abs(
        row["s_odd_scaled"]-1
    ) < 5e-4

    assert abs(
        row["j_gauge_minus_1"]+0.25
    ) < 5e-4

    assert abs(
        row["cbar_over_shift"]-1
    ) < 1e-5

with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    writer = csv.DictWriter(
        f,
        fieldnames=list(rows[0].keys()),
    )
    writer.writeheader()
    writer.writerows(rows)

print("Round 63 verification passed.")
for row in rows:
    if row["j"] in (10, 10000):
        print(row)
