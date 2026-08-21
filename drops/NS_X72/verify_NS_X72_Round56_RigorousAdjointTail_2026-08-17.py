"""
Exact verification for NS_X72 Round 56.

This script independently certifies the normalized nu=1 tail proof.

Main tasks:
1. derive the compact hidden-block source coefficients J_d^(n);
2. transform the adjoint equation to the real C-even recurrence;
3. use exact Q(sqrt(17)) algebra and rationalized polynomial root isolation
   to certify the coefficient signs and q_n' < 0 for all real n >= 6;
4. solve the n=1,...,5 central equations exactly over Q(sqrt(17));
5. certify coarse rational bounds on x0, L, and T(0);
6. combine them into Banach fixed-point tail bounds and rigorous u_3 < 0.

No floating finite-section convergence is used in the proof certificate.
"""
import sympy as sp

I = sp.I
sqrt17 = sp.sqrt(17)

K, n, nu = sp.symbols(
    "K n nu",
    positive=True,
    real=True,
)
e3 = sp.Matrix([0, 0, 1])

def avec(s):
    return sp.Matrix(
        [1, s*I, 0]
    )/2

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
            cross(
                a,
                I*cross(k, B)-B,
            ),
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

# ------------------------------------------------------------------
# General compact hidden block H_{K,n}.
# ------------------------------------------------------------------

Dm = K**2 + (n-1)**2
Dp = K**2 + (n+1)**2
Pn = (
    K**4
    + 2*K**2*n**2
    - 4*K**2
    + n**4
    - 2*n**2
    + 1
)

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
    -Nside(kn, Bn, 1)
    / Nside(kp, Bp, -1)
)

assert sp.simplify(
    Nside(kn, Bn, -1)
) == 0

assert sp.simplify(
    Nside(kp, Bp, 1)
) == 0

assert sp.simplify(
    Nside(kn, Bn, 1)
    + rho*Nside(kp, Bp, -1)
) == 0

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
        off = s
        out[off] = sp.simplify(
            out.get(off, 0)
            + nu*Nside(
                k,
                -k2*B,
                s,
            )
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

assert J[-1] == 0
assert J[3] == 0

# We use only d=-2,0,1,2,4.
A = {
    d: sp.simplify(J[d]/I)
    for d in (-2, 0, 2, 4)
}
B1 = sp.simplify(J[1])

# ------------------------------------------------------------------
# Q(sqrt(17)) exact root-isolation helpers.
# ------------------------------------------------------------------

def split_sqrt17(expr):
    expr = sp.expand(expr)
    parts = sp.collect(
        expr,
        sqrt17,
        evaluate=False,
    )
    return (
        sp.expand(parts.get(1, 0)),
        sp.expand(
            parts.get(sqrt17, 0)
        ),
    )

def rationalized_poly(expr, var):
    aa, bb = split_sqrt17(expr)
    return sp.Poly(
        sp.expand(
            aa*aa - 17*bb*bb
        ),
        var,
        domain=sp.QQ,
    )

def certify_no_root_ge(expr, var, threshold):
    expr = sp.together(expr)
    num, den = sp.fraction(expr)

    for piece in (num, den):
        poly = rationalized_poly(
            piece,
            var,
        )
        if poly.degree() <= 0:
            continue

        intervals = (
            sp.polys.polytools.intervals(
                poly,
                eps=sp.Rational(
                    1,
                    10**8,
                ),
            )
        )
        for interval, mult in intervals:
            lo, hi = interval
            if hi >= threshold:
                raise AssertionError(
                    (
                        "possible root >= threshold",
                        interval,
                        mult,
                    )
                )

def sign_at(expr, var, point):
    return sp.sign(
        sp.simplify(
            expr.subs(var, point)
        )
    )

# ------------------------------------------------------------------
# Exact tail sign / monotonicity certificate.
# ------------------------------------------------------------------

Kminus = sqrt17-3
Kplus = sqrt17+3

fibres = [
    (
        "minus",
        Kminus,
        sp.Rational(3, 250),
    ),
    (
        "plus",
        Kplus,
        sp.Rational(59, 1000),
    ),
]

q_general = sp.factor(
    (
        -A[-2]
        + A[0]
        + A[2]
        - A[4]
    )
    / (-B1)
).subs(nu, 1)

for name, Kval, qbar in fibres:
    signs = {
        -2: -1,
        0: +1,
        1: -1,
        2: +1,
        4: -1,
    }

    for d in (-2, 0, 2, 4):
        expr = sp.together(
            A[d].subs({
                K: Kval,
                nu: 1,
            })
        )
        certify_no_root_ge(
            expr,
            n,
            6,
        )
        assert sign_at(
            expr,
            n,
            6,
        ) == signs[d]

    exprB = sp.together(
        B1.subs({
            K: Kval,
            nu: 1,
        })
    )
    certify_no_root_ge(
        exprB,
        n,
        6,
    )
    assert sign_at(
        exprB,
        n,
        6,
    ) == signs[1]

    qexpr = sp.together(
        q_general.subs(
            K,
            Kval,
        )
    )

    dq = sp.together(
        sp.diff(
            q_general,
            n,
        ).subs(
            K,
            Kval,
        )
    )

    certify_no_root_ge(
        dq,
        n,
        6,
    )
    assert sign_at(
        dq,
        n,
        6,
    ) == -1

    q6 = sp.simplify(
        qexpr.subs(
            n,
            6,
        )
    )
    assert sp.sign(
        qbar-q6
    ) == 1

# ------------------------------------------------------------------
# Exact central affine solve.
# ------------------------------------------------------------------

def real_coeffs(Kval, nval):
    vals = {
        d: sp.simplify(
            J[d].subs({
                K: Kval,
                n: nval,
                nu: 1,
            })
        )
        for d in (-2, 0, 1, 2, 4)
    }

    Avec = {
        d: sp.simplify(
            vals[d]/I
        )
        for d in (-2, 0, 2, 4)
    }

    return Avec, sp.simplify(
        vals[1]
    )

def central_affine(Kval):
    M = sp.zeros(5, 5)
    C = sp.zeros(5, 3)
    rhs = sp.zeros(5, 1)

    for row, n0 in enumerate(
        range(1, 6)
    ):
        Avec, B = real_coeffs(
            Kval,
            n0,
        )

        terms = {
            n0-2: -Avec[-2],
            n0: Avec[0],
            n0+1: -B,
            n0+2: -Avec[2],
            n0+4: Avec[4],
        }

        for m0, coeff in terms.items():
            m = m0
            c = coeff

            if m < 0:
                mm = -m
                c = c*((-1)**mm)
                m = mm

            if m == 0:
                rhs[row, 0] -= c
            elif m == 1:
                pass
            elif 2 <= m <= 6:
                M[row, m-2] += c
            elif 7 <= m <= 9:
                C[row, m-7] += c
            else:
                raise RuntimeError(
                    (n0, m)
                )

    x0 = sp.simplify(
        M.inv()*rhs
    )
    L = sp.simplify(
        -M.inv()*C
    )

    return x0, L

def row_l1(L, row):
    return sp.simplify(
        sum(
            sp.Abs(
                L[row, j]
            )
            for j in range(3)
        )
    )

def exact_T0(Kval, x0):
    def uc(m):
        if m == 0:
            return sp.Integer(1)
        if m == 1:
            return sp.Integer(0)
        if 2 <= m <= 6:
            return x0[m-2]
        if m >= 7:
            return sp.Integer(0)
        if m < 0:
            mm = -m
            return (
                (-1)**mm
                * uc(mm)
            )
        raise RuntimeError(m)

    vals = []
    for k in (7, 8, 9):
        n0 = k-1
        Avec, B = real_coeffs(
            Kval,
            n0,
        )

        val = sp.simplify(
            (
                -Avec[-2]*uc(n0-2)
                + Avec[0]*uc(n0)
                - Avec[2]*uc(n0+2)
                + Avec[4]*uc(n0+4)
            )
            / B
        )
        vals.append(val)

    return vals

certificates = []

for name, Kval, qbar in fibres:
    x0, L = central_affine(
        Kval
    )

    if name == "minus":
        x3_upper = -sp.Rational(
            41,
            1000,
        )
        row3_bound = sp.Rational(
            1,
            400000,
        )
        near_bound = sp.Rational(
            1,
            125,
        )
        T0_bound = sp.Rational(
            1,
            2000000,
        )
        positivity_target = sp.Rational(
            40999,
            1000000,
        )
    else:
        x3_upper = -sp.Rational(
            21,
            250,
        )
        row3_bound = sp.Rational(
            1,
            2000,
        )
        near_bound = sp.Rational(
            13,
            500,
        )
        T0_bound = sp.Rational(
            1,
            10000,
        )
        positivity_target = sp.Rational(
            839,
            10000,
        )

    # x0 u3 bound.
    assert sp.sign(
        x3_upper-x0[1]
    ) == 1

    # u3 sensitivity.
    r3 = row_l1(
        L,
        1,
    )
    assert sp.sign(
        row3_bound-r3
    ) == 1

    # central rows used by the first tail equations.
    for row in (2, 3, 4):
        rr = row_l1(
            L,
            row,
        )
        assert sp.sign(
            near_bound-rr
        ) == 1
        assert sp.sign(
            1-rr
        ) == 1

    T0_vals = exact_T0(
        Kval,
        x0,
    )

    for vv in T0_vals:
        assert sp.sign(
            T0_bound-sp.Abs(vv)
        ) == 1

    # Banach fixed-point tail bound:
    # ||y*|| <= b/(1-q).
    tail_bound = sp.simplify(
        T0_bound/(1-qbar)
    )

    # u3 <= x3_upper + row3_bound*tail_bound.
    u3_upper = sp.simplify(
        x3_upper
        + row3_bound*tail_bound
    )

    # Need -u3 > positivity_target.
    assert sp.sign(
        -positivity_target-u3_upper
    ) == 1

    certificates.append({
        "name": name,
        "K": sp.N(Kval, 18),
        "q6": sp.N(
            q_general.subs({
                K: Kval,
                n: 6,
            }),
            18,
        ),
        "qbar": qbar,
        "x0_u3": sp.N(
            x0[1],
            18,
        ),
        "row_u3_l1": sp.N(
            r3,
            18,
        ),
        "T0_max": max(
            [
                float(
                    sp.N(
                        sp.Abs(v),
                        18,
                    )
                )
                for v in T0_vals
            ]
        ),
        "tail_bound": sp.N(
            tail_bound,
            18,
        ),
        "u3_upper": sp.N(
            u3_upper,
            18,
        ),
        "a3_lower": positivity_target,
    })

# ------------------------------------------------------------------
# Exact target sign geometry.
# ------------------------------------------------------------------

xminus = (
    13-3*sqrt17
)/2
xplus = (
    13+3*sqrt17
)/2

assert sp.sign(
    3*xminus-1
) == -1
assert sp.sign(
    17*xminus-8
) == -1

assert sp.sign(
    3*xplus-1
) == 1
assert sp.sign(
    17*xplus-8
) == 1

print(
    "Round 56 exact verification passed."
)

for item in certificates:
    print()
    for key, val in item.items():
        print(
            key,
            "=",
            val,
        )
