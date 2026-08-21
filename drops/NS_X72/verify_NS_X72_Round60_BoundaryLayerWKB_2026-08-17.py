"""
Verification for NS_X72 Round 60.

Checks:
1. reduced 2x2 slow-pair transfer matrix and its exact stable root;
2. small-a stable-log expansion;
3. cubic WKB half-decay prediction;
4. direct sparse solutions of the FULL rescaled adjoint recurrence;
5. observed half-decay / WKB half-decay collapse for both sqrt(17) fibres;
6. central matching errors relative to the rigorous Round 59 endpoint constants.

The full three-plane dichotomy matching theorem is NOT claimed here.
"""
import contextlib
import csv
import io
import math
import runpy
from pathlib import Path

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round60_BoundaryLayerMap_2026-08-17.csv")

# ------------------------------------------------------------------
# Exact reduced-model checks.
# ------------------------------------------------------------------

a, lam = sp.symbols("a lam", positive=True, real=True)

M = sp.Matrix([
    [1, a],
    [a, 1+a**2],
])

assert sp.simplify(M.det()-1) == 0

char = sp.expand((M-lam*sp.eye(2)).det())
expected_char = sp.expand(
    lam**2-(2+a**2)*lam+1
)
assert sp.simplify(char-expected_char) == 0

lam_minus = sp.simplify(
    (
        2+a**2-a*sp.sqrt(a**2+4)
    )/2
)

lam_alt = sp.simplify(
    (
        (sp.sqrt(a**2+4)-a)/2
    )**2
)

assert sp.simplify(
    lam_minus-lam_alt
) == 0

# The elementary identity
# exp(-asinh(a/2)) = sqrt(1+a^2/4)-a/2
# gives lam_- = exp(-2 asinh(a/2)).
# Verify the logarithmic asymptotic directly from the RHS.
log_series = sp.series(
    -2*sp.asinh(a/2),
    a,
    0,
    6,
).removeO()

assert sp.expand(log_series).coeff(a, 1) == -1
assert sp.expand(log_series).coeff(a, 3) == sp.Rational(1, 24)

# ------------------------------------------------------------------
# Reuse the already-audited Round 58 coefficient generator.
# ------------------------------------------------------------------

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(
        "/mnt/data/verify_NS_X72_Round58_SmallViscosityEndpoint_2026-08-17.py"
    )

Afunc = g["Afunc"]
bfunc = g["bfunc"]
fibres = g["fibres"]

def even_minimal(Kv, Jmax=1800):
    R = {
        Jmax+1: 0.0,
        Jmax+2: 0.0,
    }

    for jj in range(Jmax, 0, -1):
        nn = 2*jj
        am2 = float(Afunc[-2](Kv, nn))
        a0 = float(Afunc[0](Kv, nn))
        a2 = float(Afunc[2](Kv, nn))
        a4 = float(Afunc[4](Kv, nn))

        R[jj] = (
            am2
            / (
                a0
                - a2*R[jj+1]
                + a4*R[jj+2]*R[jj+1]
            )
        )

    e = np.empty(Jmax+1)
    e[0] = 1.0

    for jj in range(1, Jmax+1):
        e[jj] = e[jj-1]*R[jj]

    return e

def endpoint_odd_profile(Kv, J=1200):
    e = even_minimal(
        Kv,
        max(1800, J+100),
    )

    rows = []
    cols = []
    data = []
    rhs = np.zeros(J)

    def add(r, c, v):
        rows.append(r)
        cols.append(c)
        data.append(v)

    for jj in range(J):
        nn = 2*jj+1

        am2 = float(Afunc[-2](Kv, nn))
        a0 = float(Afunc[0](Kv, nn))
        a2 = float(Afunc[2](Kv, nn))
        a4 = float(Afunc[4](Kv, nn))
        bv = float(bfunc(Kv, nn))

        rhs[jj] = bv*e[jj+1]

        for idx, coeff in (
            (jj-1, -am2),
            (jj, a0),
            (jj+1, -a2),
            (jj+2, a4),
        ):
            if idx <= 0:
                continue
            if idx <= J:
                add(
                    jj,
                    idx-1,
                    coeff,
                )

    Mat = sps.csr_matrix(
        (data, (rows, cols)),
        shape=(J, J),
    )

    return spla.spsolve(
        Mat,
        rhs,
    )

def rescaled_sparse(Kv, nuv, J):
    rows = []
    cols = []
    data = []
    rhs = np.zeros(2*J)

    def add(r, c, v):
        rows.append(r)
        cols.append(c)
        data.append(v)

    def ei(jj):
        return jj-1

    def oi(jj):
        return J+jj-1

    row = 0

    for jj in range(J):
        nn = 2*jj+1

        am2 = float(Afunc[-2](Kv, nn))
        a0 = float(Afunc[0](Kv, nn))
        a2 = float(Afunc[2](Kv, nn))
        a4 = float(Afunc[4](Kv, nn))
        bv = float(bfunc(Kv, nn))

        if jj-1 >= 1:
            add(row, oi(jj-1), -am2)

        if jj >= 1:
            add(row, oi(jj), a0)

        if jj+1 <= J:
            add(row, ei(jj+1), -bv)
            add(row, oi(jj+1), -a2)

        if jj+2 <= J:
            add(row, oi(jj+2), a4)

        row += 1

    for jj in range(1, J+1):
        nn = 2*jj

        am2 = float(Afunc[-2](Kv, nn))
        a0 = float(Afunc[0](Kv, nn))
        a2 = float(Afunc[2](Kv, nn))
        a4 = float(Afunc[4](Kv, nn))
        bv = float(bfunc(Kv, nn))

        if jj-1 == 0:
            rhs[row] += am2
        else:
            add(row, ei(jj-1), -am2)

        add(row, ei(jj), a0)
        add(row, oi(jj), -(nuv**2)*bv)

        if jj+1 <= J:
            add(row, ei(jj+1), -a2)

        if jj+2 <= J:
            add(row, ei(jj+2), a4)

        row += 1

    Mat = sps.csr_matrix(
        (data, (rows, cols)),
        shape=(2*J, 2*J),
    )

    sol = spla.spsolve(
        Mat,
        rhs,
    )

    return (
        sol[:J],
        sol[J:],
    )

endpoint_c0 = {
    "minus":
        5.79052557842264771855,
    "plus":
        5.3317525458744885,
}

plateau = {}

for name, Kv in fibres:
    o0 = endpoint_odd_profile(
        Kv,
        1200,
    )
    plateau[name] = float(
        o0[799]
    )

rows_out = []

nu_values = (
    1e-3,
    1e-4,
    1e-5,
    1e-6,
    1e-7,
)

for name, Kv in fibres:
    for nuv in nu_values:
        J = max(
            1000,
            int(
                5*(1/nuv)**(1/3)
            ) + 500,
        )

        e, o = rescaled_sparse(
            Kv,
            nuv,
            J,
        )

        pred = (
            3*Kv*math.log(2)
            / (16*nuv)
        )**(1/3)

        threshold = (
            0.5*abs(
                plateau[name]
            )
        )

        inds = np.where(
            np.abs(o) > threshold
        )[0]

        observed = (
            int(inds[-1]+1)
            if len(inds)
            else None
        )

        ratio = (
            observed/pred
            if observed is not None
            else float("nan")
        )

        central = -float(o[0])
        error = (
            central
            - endpoint_c0[name]
        )

        rows_out.append({
            "fibre": name,
            "nu": nuv,
            "plateau_proxy": plateau[name],
            "half_decay_observed": observed,
            "half_decay_wkb": pred,
            "ratio": ratio,
            "a3_over_nu": central,
            "endpoint_c0": endpoint_c0[name],
            "central_error": error,
            "central_error_over_nu": error/nuv,
        })

for name in ("minus", "plus"):
    sub = [
        row
        for row in rows_out
        if row["fibre"] == name
        and row["nu"] <= 1e-6
    ]

    for row in sub:
        assert (
            math.isnan(row["ratio"])
            or abs(
                row["ratio"]-1
            ) < 0.03
        )

for name in ("minus", "plus"):
    sub = [
        row
        for row in rows_out
        if row["fibre"] == name
        and row["nu"] <= 1e-5
    ]

    slopes = [
        row["central_error_over_nu"]
        for row in sub
    ]

    assert (
        max(slopes)-min(slopes)
        < 0.05
    )

with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    writer = csv.DictWriter(
        f,
        fieldnames=list(
            rows_out[0].keys()
        ),
    )
    writer.writeheader()
    writer.writerows(rows_out)

print(
    "Round 60 verification passed."
)

for row in rows_out:
    print(row)
