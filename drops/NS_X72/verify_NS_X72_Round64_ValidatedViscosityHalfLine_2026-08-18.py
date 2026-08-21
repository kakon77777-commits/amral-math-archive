"""
Validated verification for NS_X72 Round 64.

The certificate has two parts.

PART A: 1e-4 <= nu <= 0.7
- exact coefficient formulas are inherited from Round 58;
- finite cores use N=250 on [1e-4,1e-3] and N=80 on [1e-3,0.7];
- each viscosity chunk uses an arbitrary floating approximate inverse R;
- ||I-RM_c||_inf and core-solution residuals are recomputed using
  high-precision OUTWARD INTERVAL coefficient evaluation;
- Neumann bounds validate the true core inverse across the whole chunk;
- core-to-tail feedback is enclosed;
- the infinite tail uses the exact Round 56 monotone contraction q_n.

PART B: nu >= 0.7
- exact algebraic bounds q_* < 0.53 and r_* < 0.151 are checked;
- Round 56 monotonicity supplies q_n <= q_* beyond n=6;
- the full sequence map is a contraction and the u3 forcing sign survives.

This proves u3<0, hence a3=-u3>0, for both source fibres and every nu>=1e-4.
"""
from pathlib import Path
import contextlib, csv, hashlib, io, math
import numpy as np
import mpmath as mp
import sympy as sp

OUT = Path("/mnt/data/NS_X72_Round64_ViscosityCertificate_2026-08-18.csv")

# Integrity dependencies.
def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

assert sha256(
    "/mnt/data/verify_NS_X72_Round56_RigorousAdjointTail_2026-08-17.py"
) == "0dd1549c7b1f39f6915b172124d038890a10d84bd7802516b82083239010414d"

assert sha256(
    "/mnt/data/verify_NS_X72_Round59_EndpointJostGraph_2026-08-17.py"
) == "18a1d167b1d157ae9e1d127ad03f54c6efd3c820974546dd57bdd6f4099b05e2"

# Load the exact Round 58 coefficient construction, stopping before its output phase.
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
        compile(cut, str(src), "exec"),
        ns,
    )

A = ns["A"]
b = ns["b"]
Ksym = ns["K"]
nsym = ns["n"]
Afunc = ns["Afunc"]
bfunc = ns["bfunc"]

sqrt17 = sp.sqrt(17)
Kminus_exact = sqrt17-3
Kplus_exact = sqrt17+3

fibres = [
    ("minus", float(math.sqrt(17)-3)),
    ("plus", float(math.sqrt(17)+3)),
]

# Outward interval coefficient evaluators.
mp.iv.dps = 55

Aiv = {
    d: sp.lambdify(
        (Ksym, nsym),
        A[d],
        "mpmath",
    )
    for d in (-2, 0, 2, 4)
}

biv = sp.lambdify(
    (Ksym, nsym),
    b,
    "mpmath",
)

def K_iv(name):
    if name == "minus":
        return mp.iv.sqrt(17)-3
    return mp.iv.sqrt(17)+3

def upper_abs(iv):
    # b is already an outward endpoint. A tiny float-conversion inflation is added.
    return float(abs(iv).b)*(1+2e-15)+1e-300

# ------------------------------------------------------------------
# Finite core construction.
# ------------------------------------------------------------------

def core_matrix_parts(Kv, N):
    m = N-1
    M0 = np.zeros((m, m), dtype=float)
    M1 = np.zeros((m, m), dtype=float)
    rhs = np.zeros(m, dtype=float)
    C = np.zeros((m, 3), dtype=float)

    def add(row, idx, c0, c1=0.0):
        if idx < 0:
            kk = -idx
            sign = (-1)**kk
            idx = kk
            c0 *= sign
            c1 *= sign

        if idx == 0:
            rhs[row] -= c0
        elif idx == 1:
            pass
        elif 2 <= idx <= N:
            M0[row, idx-2] += c0
            M1[row, idx-2] += c1
        elif N+1 <= idx <= N+3:
            C[row, idx-(N+1)] += c0
            assert c1 == 0.0
        else:
            raise RuntimeError((row, idx))

    for row, nn in enumerate(range(1, N)):
        am = float(Afunc[-2](Kv, nn))
        a0 = float(Afunc[0](Kv, nn))
        a2 = float(Afunc[2](Kv, nn))
        a4 = float(Afunc[4](Kv, nn))
        bb = float(bfunc(Kv, nn))

        add(row, nn-2, -am)
        add(row, nn, a0)
        add(row, nn+1, 0.0, -bb)
        add(row, nn+2, -a2)
        add(row, nn+4, a4)

    return M0, M1, rhs, C

def core_sparse_iv(name, nu_c, N):
    kv = K_iv(name)
    nuiv = mp.iv.mpf([nu_c, nu_c])
    m = N-1

    M_entries = []
    M1_entries = []
    C_entries = []
    rhs = [mp.iv.mpf([0, 0]) for _ in range(m)]

    def add(row, idx, value, deriv=None):
        if deriv is None:
            deriv = mp.iv.mpf([0, 0])

        if idx < 0:
            kk = -idx
            sign = (-1)**kk
            idx = kk
            value *= sign
            deriv *= sign

        if idx == 0:
            rhs[row] -= value
        elif idx == 1:
            pass
        elif 2 <= idx <= N:
            M_entries.append(
                (row, idx-2, value)
            )
            if upper_abs(deriv) > 0:
                M1_entries.append(
                    (row, idx-2, deriv)
                )
        elif N+1 <= idx <= N+3:
            C_entries.append(
                (row, idx-(N+1), value)
            )
            assert upper_abs(deriv) < 1e-250
        else:
            raise RuntimeError((row, idx))

    for row, nn in enumerate(range(1, N)):
        am = Aiv[-2](kv, nn)
        a0 = Aiv[0](kv, nn)
        a2 = Aiv[2](kv, nn)
        a4 = Aiv[4](kv, nn)
        bb = biv(kv, nn)

        add(row, nn-2, -am)
        add(row, nn, a0)
        add(row, nn+1, -nuiv*bb, -bb)
        add(row, nn+2, -a2)
        add(row, nn+4, a4)

    return M_entries, M1_entries, rhs, C_entries

def residual_inverse_upper(R, entries, m):
    cols = [[] for _ in range(m)]
    for rr, cc, vv in entries:
        cols[cc].append((rr, vv))

    max_row_sum = 0.0

    for i in range(m):
        row_sum = 0.0

        for cc in range(m):
            val = mp.iv.mpf([0, 0])

            for rr, vv in cols[cc]:
                rij = mp.iv.mpf(
                    [float(R[i, rr]), float(R[i, rr])]
                )
                val += rij*vv

            if i == cc:
                val = 1-val
            else:
                val = -val

            row_sum += upper_abs(val)

        max_row_sum = max(
            max_row_sum,
            row_sum,
        )

    return max_row_sum

def sparse_product_row_triangle(R, entries):
    rows = np.zeros(
        R.shape[0],
        dtype=float,
    )

    for rr, cc, vv in entries:
        av = upper_abs(vv)
        rows += np.abs(R[:, rr])*av

    return rows

def solution_residual_upper(entries, rhs_iv, x):
    rows = [
        mp.iv.mpf(rhs_iv[i])
        for i in range(len(rhs_iv))
    ]

    for rr, cc, vv in entries:
        rows[rr] -= (
            vv
            * mp.iv.mpf(
                [float(x[cc]), float(x[cc])]
            )
        )

    return max(
        upper_abs(v)
        for v in rows
    )

def q_upper(name, nn, nu_lo):
    kv = K_iv(name)

    am = Aiv[-2](kv, nn)
    a0 = Aiv[0](kv, nn)
    a2 = Aiv[2](kv, nn)
    a4 = Aiv[4](kv, nn)
    bb = biv(kv, nn)

    q = (
        -am+a0+a2-a4
    )/(
        -mp.iv.mpf([nu_lo, nu_lo])*bb
    )

    return upper_abs(q)

# ------------------------------------------------------------------
# Chunk certificate.
# ------------------------------------------------------------------

def certify_chunk(
    name,
    Kv,
    nu_lo,
    nu_hi,
    N,
):
    nu_c = (nu_lo+nu_hi)/2
    h = (nu_hi-nu_lo)/2

    M0, M1, rhs, C = core_matrix_parts(
        Kv,
        N,
    )

    Mc = M0+nu_c*M1

    # Any approximate inverse is allowed; all true bounds come from residuals.
    R = np.linalg.inv(Mc)
    x_tilde = R@rhs

    M_entries, M1_entries, rhs_iv, C_entries = (
        core_sparse_iv(
            name,
            nu_c,
            N,
        )
    )

    eta = residual_inverse_upper(
        R,
        M_entries,
        N-1,
    )

    assert eta < 1e-10

    Rnorm = float(
        np.max(
            np.sum(
                np.abs(R),
                axis=1,
            )
        )
    )*(1+2e-15)

    residual_x = solution_residual_upper(
        M_entries,
        rhs_iv,
        x_tilde,
    )

    err_x = (
        Rnorm
        /(1-eta)
        * residual_x
    )

    x_inf = (
        float(
            np.max(
                np.abs(x_tilde)
            )
        )
        + err_x
    )

    RB_rows = sparse_product_row_triangle(
        R,
        M1_entries,
    )

    RB_inf = float(
        np.max(RB_rows)
    )

    B_inf = (
        RB_inf
        /(1-eta)
    )

    B_error = (
        eta
        /(1-eta)
        * RB_inf
    )

    B_rows = RB_rows+B_error

    rho = h*B_inf
    assert rho < 0.65

    RC_rows = sparse_product_row_triangle(
        R,
        C_entries,
    )

    RC_inf = float(
        np.max(RC_rows)
    )

    L_inf = (
        RC_inf
        /(1-eta)
    )

    L_error = (
        eta
        /(1-eta)
        * RC_inf
    )

    L_rows_center = RC_rows+L_error

    def x_abs_bound(row):
        return (
            abs(float(x_tilde[row]))
            + err_x
            + h*float(B_rows[row])
            /(1-rho)
            * x_inf
        )

    def L_row_bound(row):
        return (
            float(L_rows_center[row])
            + h*float(B_rows[row])
            /(1-rho)
            * L_inf
        )

    u3_core_upper = (
        float(x_tilde[1])
        + err_x
        + h*float(B_rows[1])
        /(1-rho)
        * x_inf
    )

    X_bd = max(
        x_abs_bound(-3),
        x_abs_bound(-2),
        x_abs_bound(-1),
    )

    L_bd = max(
        L_row_bound(-3),
        L_row_bound(-2),
        L_row_bound(-1),
    )

    L3 = L_row_bound(1)

    q_raw = q_upper(
        name,
        N,
        nu_lo,
    )

    # Round 56 exact monotonicity gives q_n <= q_N beyond the cutoff.
    q_hat = q_raw*(1+L_bd)

    assert q_hat < 0.80

    tail_bound = (
        q_raw*X_bd
        /(1-q_hat)
    )

    u3_upper = (
        u3_core_upper
        + L3*tail_bound
    )

    assert u3_upper < 0

    return {
        "fibre": name,
        "nu_lo": nu_lo,
        "nu_hi": nu_hi,
        "N": N,
        "eta": eta,
        "rho": rho,
        "q_raw": q_raw,
        "q_hat": q_hat,
        "X_bd": X_bd,
        "L_bd": L_bd,
        "L3": L3,
        "tail_bound": tail_bound,
        "u3_core_upper": u3_core_upper,
        "u3_upper": u3_upper,
        "a3_lower": -u3_upper,
    }

def geometric_chunks(start, end, ratio):
    out = []
    lo = start

    while lo < end*(1-1e-15):
        hi = min(
            lo*ratio,
            end,
        )
        out.append((lo, hi))
        lo = hi

    return out

low_chunks = geometric_chunks(
    1e-4,
    1e-3,
    1.5,
)

mid_chunks = geometric_chunks(
    1e-3,
    0.7,
    1.5,
)

rows = []

for name, Kv in fibres:
    for lo, hi in low_chunks:
        rows.append(
            certify_chunk(
                name,
                Kv,
                lo,
                hi,
                250,
            )
        )

    for lo, hi in mid_chunks:
        rows.append(
            certify_chunk(
                name,
                Kv,
                lo,
                hi,
                80,
            )
        )

# Certified worst cases.
for name in ("minus", "plus"):
    low = [
        r for r in rows
        if r["fibre"] == name
        and r["nu_hi"] <= 1e-3+1e-18
    ]
    mid = [
        r for r in rows
        if r["fibre"] == name
        and r["nu_lo"] >= 1e-3-1e-18
    ]

    worst_low = min(
        r["a3_lower"]
        for r in low
    )

    worst_mid = min(
        r["a3_lower"]
        for r in mid
    )

    if name == "minus":
        assert worst_low > 2.16e-4
        assert worst_mid > 2.40e-3
    else:
        assert worst_low > 3.04e-4
        assert worst_mid > 3.03e-3

# ------------------------------------------------------------------
# Global contraction theorem for nu >= 0.7.
# ------------------------------------------------------------------

q_expr = (
    -A[-2]+A[0]+A[2]-A[4]
)/(-b)

feedback2_expr = (
    A[0]+A[2]-A[4]
)/(-b)

c_inf_expr = sp.simplify(
    A[-2].subs(nsym, 2)
    / b.subs(nsym, 2)
)

for name, Kval in (
    ("minus", Kminus_exact),
    ("plus", Kplus_exact),
):
    # Exact finite checks n=1,...,6.
    for nn in range(1, 7):
        qv = sp.simplify(
            q_expr.subs({
                Ksym: Kval,
                nsym: nn,
            })
        )

        assert sp.sign(
            sp.Rational(53, 100)-qv
        ) == 1

    rv = sp.simplify(
        feedback2_expr.subs({
            Ksym: Kval,
            nsym: 2,
        })
    )

    assert sp.sign(
        sp.Rational(151, 1000)-rv
    ) == 1

    cv = sp.simplify(
        c_inf_expr.subs(
            Ksym,
            Kval,
        )
    )

    assert sp.sign(cv) == 1

# At nu >= 0.7:
# q <= .53/.7 < 1 and the u3 sign bracket is >= 19/170.
assert sp.Rational(53, 100)/sp.Rational(7, 10) < 1

bracket = (
    1
    - sp.Rational(151, 1000)
    / (
        sp.Rational(7, 10)
        - sp.Rational(53, 100)
    )
)

assert bracket == sp.Rational(19, 170)
assert bracket > 0

# Save certificate rows.
with OUT.open(
    "w",
    newline="",
    encoding="utf-8",
) as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "fibre",
            "nu_lo",
            "nu_hi",
            "N",
            "eta",
            "rho",
            "q_raw",
            "q_hat",
            "X_bd",
            "L_bd",
            "L3",
            "tail_bound",
            "u3_core_upper",
            "u3_upper",
            "a3_lower",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)

print("Round 64 validated verification passed.")

for name in ("minus", "plus"):
    sub = [
        r for r in rows
        if r["fibre"] == name
    ]
    worst = min(
        sub,
        key=lambda r: r["a3_lower"],
    )
    print(
        name,
        "worst validated chunk =",
        worst,
    )

print(
    "Global nu>=0.7 bracket =",
    bracket,
)
