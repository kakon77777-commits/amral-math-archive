"""
Verification for NS_X72 Round 61.

Checks:
1. exact leading cubic factorization;
2. fast reciprocal-root asymptotics;
3. optimal matching exponent alpha=2/7;
4. full 6D parity-rescaled transfer construction;
5. positive-viscosity minimal three-plane via backward QR;
6. zero-viscosity endpoint selected plane:
   one even minimal line + two odd bounded lines;
7. principal-angle diagnostics at j_m = round(nu^(-2/7));
8. log-log slopes of the largest principal angle.

The principal-angle convergence is numerical. The cubic factorization and
matching-exponent optimization are analytic.
"""
import contextlib
import csv
import io
import math
import runpy
from pathlib import Path

import numpy as np
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round61_GrassmannMatchingMap_2026-08-18.csv")

# ------------------------------------------------------------------
# Analytic checks.
# ------------------------------------------------------------------

r, eps, alpha = sp.symbols(
    "r eps alpha",
    positive=True,
    real=True,
)

poly = eps+r-r**2-eps*r**3
fact = -(r-1)*(eps*r**2+(1+eps)*r+eps)

assert sp.expand(poly-fact) == 0

disc = 1+2*eps-3*eps**2
rsmall = (
    -(1+eps)+sp.sqrt(disc)
)/(2*eps)

rlarge = (
    -(1+eps)-sp.sqrt(disc)
)/(2*eps)

assert sp.simplify(rsmall*rlarge-1) == 0

small_series = sp.series(
    rsmall,
    eps,
    0,
    3,
).removeO()

assert sp.expand(small_series).coeff(eps, 1) == -1

# Optimize min(1-3a,4a-1,a) on (1/4,1/3):
# first two limiting exponents balance.
astar = sp.solve(
    sp.Eq(
        1-3*alpha,
        4*alpha-1,
    ),
    alpha,
)[0]

assert astar == sp.Rational(2, 7)
assert sp.simplify(
    1-3*astar-sp.Rational(1, 7)
) == 0
assert sp.simplify(
    4*astar-1-sp.Rational(1, 7)
) == 0

# ------------------------------------------------------------------
# Load audited coefficient functions from Round 58.
# ------------------------------------------------------------------

text_path = Path(
    "/mnt/data/verify_NS_X72_Round58_SmallViscosityEndpoint_2026-08-17.py"
)

code = text_path.read_text(
    encoding="utf-8",
)

cut = code.split(
    'with OUT.open("w"',
    1,
)[0]

ns = {}
with contextlib.redirect_stdout(
    io.StringIO()
):
    exec(
        compile(
            cut,
            str(text_path),
            "exec",
        ),
        ns,
    )

Afunc = ns["Afunc"]
bfunc = ns["bfunc"]
fibres = ns["fibres"]

# ------------------------------------------------------------------
# Full 6D parity-rescaled transfer.
# ------------------------------------------------------------------

def coeffs(Kv, jj):
    ne = 2*jj
    no = 2*jj+1

    Ae = {
        d: float(
            Afunc[d](Kv, ne)
        )
        for d in (-2, 0, 2, 4)
    }

    Ao = {
        d: float(
            Afunc[d](Kv, no)
        )
        for d in (-2, 0, 2, 4)
    }

    be = float(
        bfunc(Kv, ne)
    )

    bo = float(
        bfunc(Kv, no)
    )

    return Ae, be, Ao, bo

def T6(Kv, jj, nuv):
    Ae, be, Ao, bo = coeffs(
        Kv,
        jj,
    )

    T = np.zeros(
        (6, 6),
        dtype=float,
    )

    # State:
    # (e_{j+1},e_j,e_{j-1},o_{j+1},o_j,o_{j-1})
    # -> j+1 state.

    T[0, 0] = Ae[2]/Ae[4]
    T[0, 1] = -Ae[0]/Ae[4]
    T[0, 2] = Ae[-2]/Ae[4]
    T[0, 4] = (
        nuv**2*be
    )/Ae[4]

    T[1, 0] = 1
    T[2, 1] = 1

    T[3, 0] = bo/Ao[4]
    T[3, 3] = Ao[2]/Ao[4]
    T[3, 4] = -Ao[0]/Ao[4]
    T[3, 5] = Ao[-2]/Ao[4]

    T[4, 3] = 1
    T[5, 4] = 1

    return T

def T3_even(Kv, jj):
    Ae, be, Ao, bo = coeffs(
        Kv,
        jj,
    )

    return np.array([
        [
            Ae[2]/Ae[4],
            -Ae[0]/Ae[4],
            Ae[-2]/Ae[4],
        ],
        [1, 0, 0],
        [0, 1, 0],
    ], dtype=float)

def T3_odd(Kv, jj):
    Ae, be, Ao, bo = coeffs(
        Kv,
        jj,
    )

    return np.array([
        [
            Ao[2]/Ao[4],
            -Ao[0]/Ao[4],
            Ao[-2]/Ao[4],
        ],
        [1, 0, 0],
        [0, 1, 0],
    ], dtype=float)

def real_basis_from_eig(
    vals,
    vecs,
    count,
):
    order = np.argsort(
        np.abs(vals)
    )

    picked = []

    for idx in order:
        v = vecs[:, idx]

        if np.max(
            np.abs(v.imag)
        ) < 1e-8:
            cand = v.real
            picked.append(cand)
        else:
            picked.append(v.real)
            if len(picked) < count:
                picked.append(v.imag)

        if len(picked) >= count:
            break

    Q = np.column_stack(
        picked[:count]
    )

    Q, _ = np.linalg.qr(Q)

    return Q

def fixed_minimal_plane(
    Kv,
    nuv,
    jm,
    J,
):
    T = T6(
        Kv,
        J,
        nuv,
    )

    vals, vecs = np.linalg.eig(
        T
    )

    Q = real_basis_from_eig(
        vals,
        vecs,
        3,
    )

    # Q is local at level J.
    for jj in range(
        J-1,
        jm-1,
        -1,
    ):
        Q = np.linalg.solve(
            T6(
                Kv,
                jj,
                nuv,
            ),
            Q,
        )

        Q, _ = np.linalg.qr(
            Q
        )

    return Q

def endpoint_plane(
    Kv,
    jm,
    J,
):
    # Even: one fast minimal line.
    Te = T3_even(
        Kv,
        J,
    )

    ve, Ve = np.linalg.eig(
        Te
    )

    ie = np.argmin(
        np.abs(ve)
    )

    qe = np.real(
        Ve[:, ie]
    ).reshape(3, 1)

    qe /= np.linalg.norm(
        qe
    )

    for jj in range(
        J-1,
        jm-1,
        -1,
    ):
        qe = np.linalg.solve(
            T3_even(
                Kv,
                jj,
            ),
            qe,
        )

        qe /= np.linalg.norm(
            qe
        )

    # Odd: fast minimal + neutral bounded directions.
    To = T3_odd(
        Kv,
        J,
    )

    vo, Vo = np.linalg.eig(
        To
    )

    ids = np.argsort(
        np.abs(vo)
    )[:2]

    qo = np.real(
        Vo[:, ids]
    )

    qo, _ = np.linalg.qr(
        qo
    )

    for jj in range(
        J-1,
        jm-1,
        -1,
    ):
        qo = np.linalg.solve(
            T3_odd(
                Kv,
                jj,
            ),
            qo,
        )

        qo, _ = np.linalg.qr(
            qo
        )

    Q = np.zeros(
        (6, 3),
        dtype=float,
    )

    Q[:3, 0] = qe[:, 0]
    Q[3:, 1:] = qo

    Q, _ = np.linalg.qr(
        Q
    )

    return Q

def principal_angles(
    Q1,
    Q2,
):
    sv = np.linalg.svd(
        Q1.T@Q2,
        compute_uv=False,
    )

    sv = np.clip(
        sv,
        -1,
        1,
    )

    return np.arccos(
        sv
    )

rows = []

nu_values = (
    1e-3,
    1e-4,
    1e-5,
    1e-6,
    1e-7,
)

for name, Kv in fibres:
    for nuv in nu_values:
        jm = max(
            3,
            int(
                round(
                    nuv**(-2/7)
                )
            ),
        )

        J = max(
            700,
            int(
                12*nuv**(-1/3)
            ),
        )

        Qnu = fixed_minimal_plane(
            Kv,
            nuv,
            jm,
            J,
        )

        Q0 = endpoint_plane(
            Kv,
            jm,
            max(
                J,
                1500,
            ),
        )

        angles = principal_angles(
            Qnu,
            Q0,
        )

        theta = float(
            np.max(angles)
        )

        rows.append({
            "fibre": name,
            "nu": nuv,
            "j_match": jm,
            "J_tail": J,
            "theta_max": theta,
            "theta_over_nu_1_7":
                theta/(nuv**(1/7)),
        })

# Asymptotic diagnostic: ratios against nu^(1/7) decrease.
for name in ("minus", "plus"):
    sub = [
        row for row in rows
        if row["fibre"] == name
    ]

    tail = sub[-3:]

    ratios = [
        row["theta_over_nu_1_7"]
        for row in tail
    ]

    assert (
        ratios[-1]
        <
        ratios[0]
    )

# Log-log fitted slopes.
slopes = {}

for name in ("minus", "plus"):
    sub = [
        row for row in rows
        if row["fibre"] == name
    ][-3:]

    x = np.log(
        [row["nu"] for row in sub]
    )

    y = np.log(
        [row["theta_max"] for row in sub]
    )

    slopes[name] = float(
        np.polyfit(
            x,
            y,
            1,
        )[0]
    )

    assert slopes[name] > 0.3

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
    writer.writerows(
        rows
    )

print(
    "Round 61 verification passed."
)

print(
    "slopes =",
    slopes,
)

for row in rows:
    print(row)
