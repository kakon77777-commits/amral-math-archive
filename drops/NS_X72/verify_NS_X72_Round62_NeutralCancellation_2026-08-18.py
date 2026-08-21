"""
Verification for NS_X72 Round 62.

Checks:
1. exact neutral residual limit n^3 S_n -> 48 K^3;
2. neutral-root first correction c = 12 K^2;
3. exact first relative corrections of even/odd rescaled viscous couplings;
4. quarter-power exponent optimization in the Schur-renormalized budget;
5. local frozen neutral-root numerical audit;
6. full 6D physical principal-angle diagnostics at j_m = round(nu^(-1/4));
7. decreasing theta/nu^(1/4) on the small-viscosity test sequence.

The full fast-Schur/Riccati interval theorem remains open.
"""
import contextlib
import csv
import io
import math
from pathlib import Path

import numpy as np
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round62_QuarterPowerGrassmannMap_2026-08-18.csv")

# ------------------------------------------------------------------
# Load the audited symbolic coefficient construction from Round 58,
# stopping before its numerical/file-output section.
# ------------------------------------------------------------------

src58 = Path(
    "/mnt/data/verify_NS_X72_Round58_SmallViscosityEndpoint_2026-08-17.py"
)
code58 = src58.read_text(encoding="utf-8")
cut58 = code58.split(
    'with OUT.open("w"',
    1,
)[0]

ns58 = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(
        compile(
            cut58,
            str(src58),
            "exec",
        ),
        ns58,
    )

A = ns58["A"]
b = ns58["b"]
K = ns58["K"]
n = ns58["n"]
Afunc = ns58["Afunc"]
bfunc = ns58["bfunc"]
fibres = ns58["fibres"]

# ------------------------------------------------------------------
# Exact neutral cancellation.
# ------------------------------------------------------------------

S = sp.factor(
    -A[-2]+A[0]-A[2]+A[4]
)

assert sp.simplify(
    sp.limit(
        n**3*S,
        n,
        sp.oo,
    )
    - 48*K**3
) == 0

r, c = sp.symbols(
    "r c",
    real=True,
)

F = (
    -A[-2]
    + A[0]*r
    - A[2]*r**2
    + A[4]*r**3
)

Fp1 = sp.simplify(
    sp.diff(F, r).subs(r, 1)
)

assert sp.simplify(
    sp.limit(
        Fp1,
        n,
        sp.oo,
    )
    + 4*K
) == 0

scaled = sp.simplify(
    sp.limit(
        n**3
        * F.subs(
            r,
            1+c/n**3,
        ),
        n,
        sp.oo,
    )
)

assert sp.simplify(
    scaled
    - (
        48*K**3
        - 4*K*c
    )
) == 0

csol = sp.solve(
    sp.Eq(
        scaled,
        0,
    ),
    c,
)[0]

assert sp.simplify(
    csol-12*K**2
) == 0

# ------------------------------------------------------------------
# Exact viscous-coupling corrections.
# ------------------------------------------------------------------

j = sp.symbols(
    "j",
    positive=True,
    real=True,
)

ae = sp.simplify(
    -b.subs(n, 2*j)
    / A[2].subs(n, 2*j)
)

ao = sp.simplify(
    -b.subs(n, 2*j+1)
    / A[2].subs(n, 2*j+1)
)

alead = 16*j**2/K

assert sp.simplify(
    sp.limit(
        j*(ae/alead-1),
        j,
        sp.oo,
    )
    - 1
) == 0

assert sp.simplify(
    sp.limit(
        j*(ao/alead-1),
        j,
        sp.oo,
    )
    - 2
) == 0

# ------------------------------------------------------------------
# Quarter-power exponent optimization.
# ------------------------------------------------------------------

alpha = sp.symbols(
    "alpha",
    real=True,
)

sol1 = sp.solve(
    sp.Eq(
        1-3*alpha,
        alpha,
    ),
    alpha,
)[0]

sol2 = sp.solve(
    sp.Eq(
        5*alpha-1,
        alpha,
    ),
    alpha,
)[0]

assert sol1 == sp.Rational(1, 4)
assert sol2 == sp.Rational(1, 4)

assert (
    1-3*sol1
    == sol1
    == 5*sol1-1
    == sp.Rational(1, 4)
)

# ------------------------------------------------------------------
# Numeric transfer / Grassmann helpers.
# ------------------------------------------------------------------

def coeffs(Kv, jj):
    ne = 2*jj
    no = 2*jj+1

    Ae = {
        d: float(Afunc[d](Kv, ne))
        for d in (-2, 0, 2, 4)
    }

    Ao = {
        d: float(Afunc[d](Kv, no))
        for d in (-2, 0, 2, 4)
    }

    be = float(
        bfunc(Kv, ne)
    )

    bo = float(
        bfunc(Kv, no)
    )

    return Ae, be, Ao, bo

def T3_from_A(Ac):
    return np.array([
        [
            Ac[2]/Ac[4],
            -Ac[0]/Ac[4],
            Ac[-2]/Ac[4],
        ],
        [1, 0, 0],
        [0, 1, 0],
    ], dtype=float)

def T3_even(Kv, jj):
    Ae, be, Ao, bo = coeffs(
        Kv,
        jj,
    )
    return T3_from_A(Ae)

def T3_odd(Kv, jj):
    Ae, be, Ao, bo = coeffs(
        Kv,
        jj,
    )
    return T3_from_A(Ao)

def T6(Kv, jj, nuv):
    Ae, be, Ao, bo = coeffs(
        Kv,
        jj,
    )

    T = np.zeros(
        (6, 6),
        dtype=float,
    )

    T[:3, :3] = T3_from_A(
        Ae
    )
    T[3:, 3:] = T3_from_A(
        Ao
    )

    # State uses e,o variables as in Round 61.
    T[0, 4] = (
        nuv**2*be
    )/Ae[4]

    T[3, 0] = (
        bo
    )/Ao[4]

    return T

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
            picked.append(
                v.real
            )
        else:
            picked.append(
                v.real
            )
            if len(picked) < count:
                picked.append(
                    v.imag
                )

        if len(picked) >= count:
            break

    Q = np.column_stack(
        picked[:count]
    )

    Q, _ = np.linalg.qr(
        Q
    )

    return Q

def fixed_minimal_plane(
    Kv,
    nuv,
    jm,
    J,
):
    vals, vecs = np.linalg.eig(
        T6(
            Kv,
            J,
            nuv,
        )
    )

    Q = real_basis_from_eig(
        vals,
        vecs,
        3,
    )

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
    ).reshape(
        3,
        1,
    )

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

# ------------------------------------------------------------------
# Local neutral-root audit.
# ------------------------------------------------------------------

neutral_audit = []

for name, Kv in fibres:
    target = (
        1.5*Kv*Kv
    )

    for parity in (
        "even",
        "odd",
    ):
        vals = []

        for jj in (
            200,
            500,
            1000,
            5000,
        ):
            T = (
                T3_even(Kv, jj)
                if parity == "even"
                else T3_odd(Kv, jj)
            )

            eigs = np.linalg.eigvals(
                T
            )

            idx = np.argmin(
                np.abs(
                    eigs-1
                )
            )

            rr = float(
                np.real(
                    eigs[idx]
                )
            )

            D = (
                jj**3
                * (rr-1)
                / target
            )

            vals.append(D)

            neutral_audit.append({
                "kind":
                    "neutral_root",
                "fibre": name,
                "parity": parity,
                "nu": "",
                "j_match": jj,
                "theta_max": "",
                "theta_over_nu_1_4": "",
                "diagnostic": D,
            })

        assert abs(
            vals[-1]-1
        ) < 0.02

# ------------------------------------------------------------------
# Full 6D quarter-power principal angles.
# ------------------------------------------------------------------

rows = []

nu_values = (
    1e-4,
    1e-5,
    1e-6,
    1e-7,
    1e-8,
)

for name, Kv in fibres:
    for nuv in nu_values:
        jm = max(
            3,
            int(
                round(
                    nuv**(-0.25)
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

        theta = float(
            np.max(
                principal_angles(
                    Qnu,
                    Q0,
                )
            )
        )

        rows.append({
            "kind":
                "principal_angle",
            "fibre": name,
            "parity": "",
            "nu": nuv,
            "j_match": jm,
            "theta_max": theta,
            "theta_over_nu_1_4":
                theta/(nuv**0.25),
            "diagnostic": "",
        })

# The normalized quarter-power ratios decrease on the tested tail.
slopes = {}

for name in (
    "minus",
    "plus",
):
    sub = [
        row
        for row in rows
        if row["fibre"] == name
    ]

    ratios = [
        row[
            "theta_over_nu_1_4"
        ]
        for row in sub
    ]

    assert ratios[-1] < ratios[0]

    tail = sub[-4:]

    x = np.log(
        [
            row["nu"]
            for row in tail
        ]
    )

    y = np.log(
        [
            row["theta_max"]
            for row in tail
        ]
    )

    slopes[name] = float(
        np.polyfit(
            x,
            y,
            1,
        )[0]
    )

    assert slopes[name] > 0.4

all_rows = (
    neutral_audit
    + rows
)

with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "kind",
            "fibre",
            "parity",
            "nu",
            "j_match",
            "theta_max",
            "theta_over_nu_1_4",
            "diagnostic",
        ],
    )

    writer.writeheader()
    writer.writerows(
        all_rows
    )

print(
    "Round 62 verification passed."
)

print(
    "quarter-power slopes =",
    slopes,
)

for row in rows:
    print(row)
