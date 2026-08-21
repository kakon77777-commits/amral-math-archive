"""
Validated verification for NS_X72 Round 59.

The script certifies:

1. exact algebraic coefficient sign/bound inequalities for all real j >= 10
   at K = sqrt(17) +/- 3, using rationalized root isolation;
2. invariant/contraction boxes for the even minimal-ratio pullback;
3. outward interval propagation of the finite even ratios;
4. a coarse uniform tail-forcing bound |f_j| < 1e-3;
5. invariant/contraction boxes for the affine odd Jost graph;
6. outward interval propagation of the entire Jost graph box to the center;
7. strict positive interval enclosures for c0 on both source fibres.

The only non-exact numerical layer is outward interval arithmetic for the
finite pullback; all infinite-tail existence/uniqueness is certified by the
algebraic invariant-box contraction estimates.
"""
import math

import mpmath as mp
import sympy as sp

mp.iv.dps = 70

I = sp.I
sqrt17 = sp.sqrt(17)
K, n, j, nu = sp.symbols(
    "K n j nu",
    positive=True,
    real=True,
)
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

# General compact hidden block and source coefficients.
Dm = K**2 + (n-1)**2

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

A = {
    d: sp.simplify(J[d]/I)
    for d in (-2, 0, 2, 4)
}

B1 = sp.simplify(J[1])
b = sp.simplify(B1/nu)

# ------------------------------------------------------------------
# Exact Q(sqrt17) root-isolation helper.
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

def certify_nonzero_ge(expr, var, threshold):
    expr = sp.together(expr)
    num, den = sp.fraction(expr)

    for piece in (num, den):
        poly = rationalized_poly(
            piece,
            var,
        )

        if poly.degree() <= 0:
            continue

        ints = sp.polys.polytools.intervals(
            poly,
            eps=sp.Rational(
                1,
                10**7,
            ),
        )

        for interval, mult in ints:
            if interval[1] >= threshold:
                raise AssertionError(
                    (
                        "possible root",
                        interval,
                        mult,
                    )
                )

def certify_positive_ge(expr, var, threshold):
    certify_nonzero_ge(
        expr,
        var,
        threshold,
    )

    assert sp.sign(
        sp.simplify(
            expr.subs(
                var,
                threshold,
            )
        )
    ) == 1

# ------------------------------------------------------------------
# Global coefficient bounds for j >= 10.
# ------------------------------------------------------------------

Kminus = sqrt17-3
Kplus = sqrt17+3

def certify_coeff_bounds(Kval, parity):
    if parity == "even":
        nn = 2*j
    else:
        nn = 2*j+1

    subs = {
        K: Kval,
        n: nn,
    }

    if Kval == Kminus:
        checks = [
            (A[-2].subs(subs) + sp.Rational(1,100), 1),
            (-A[-2].subs(subs), 1),
            (A[4].subs(subs) + sp.Rational(1,100), 1),
            (-A[4].subs(subs), 1),
            (A[0].subs(subs)-4, 1),
            (5-A[0].subs(subs), 1),
            (A[2].subs(subs)-4, 1),
            (5-A[2].subs(subs), 1),
        ]
    else:
        checks = [
            (A[-2].subs(subs) + sp.Rational(7,5), 1),
            (-A[-2].subs(subs), 1),
            (A[4].subs(subs) + sp.Rational(2,5), 1),
            (-A[4].subs(subs), 1),
            (A[0].subs(subs)-25, 1),
            (29-A[0].subs(subs), 1),
            (A[2].subs(subs)-24, 1),
            (29-A[2].subs(subs), 1),
        ]

    for expr, sign in checks:
        certify_positive_ge(
            expr,
            j,
            10,
        )

for Kv in (Kminus, Kplus):
    certify_coeff_bounds(
        Kv,
        "even",
    )
    certify_coeff_bounds(
        Kv,
        "odd",
    )

# b_n is negative and |b_n| < 100 n^2 on odd tail.
for Kv in (Kminus, Kplus):
    nn = 2*j+1
    bexpr = sp.together(
        b.subs({
            K: Kv,
            n: nn,
        })
    )

    certify_positive_ge(
        -bexpr,
        j,
        10,
    )

    certify_positive_ge(
        100*nn**2 + bexpr,
        j,
        10,
    )

# ------------------------------------------------------------------
# Hand-certified invariant/contraction estimates.
# ------------------------------------------------------------------

# Even ratio box X=[-0.1,0]^2.
# Small fibre:
# D >= 4 - 0.01*0.01 > 3.999
# |R| <= 0.01/3.999 < 0.003
# Jacobian row sum < 0.004.
assert 0.01/(4-0.0001) < 0.1
assert (
    0.01*(5+0.001)/(4-0.0001)**2
    + 0.01*0.1/(4-0.0001)**2
) < 0.004

# Large fibre:
# D >= 25 - 0.4*0.01 = 24.996
# |R| <= 1.4/24.996 < 0.057
# Jacobian row sum < 0.067.
assert 1.4/(25-0.004) < 0.1
assert (
    1.4*(29+0.04)/(25-0.004)**2
    + 1.4*0.4*0.1/(25-0.004)**2
) < 0.067

# ------------------------------------------------------------------
# Outward interval finite ratio propagation.
# ------------------------------------------------------------------

Aiv = {
    d: sp.lambdify(
        (K, n),
        A[d],
        "mpmath",
    )
    for d in A
}
biv = sp.lambdify(
    (K, n),
    b,
    "mpmath",
)

def interval_even_data(Kiv):
    R = {
        11: mp.iv.mpf([-0.1, 0]),
        12: mp.iv.mpf([-0.1, 0]),
    }

    for jj in range(10, 0, -1):
        nn = 2*jj

        am2 = Aiv[-2](Kiv, nn)
        a0 = Aiv[0](Kiv, nn)
        a2 = Aiv[2](Kiv, nn)
        a4 = Aiv[4](Kiv, nn)

        R[jj] = (
            am2
            / (
                a0
                - a2*R[jj+1]
                + a4*R[jj+2]*R[jj+1]
            )
        )

    e = {
        0: mp.iv.mpf([1, 1])
    }

    for jj in range(1, 12):
        e[jj] = e[jj-1]*R[jj]

    return R, e

# Interval endpoint helper.
def upper_abs(iv):
    av = abs(iv)
    return float(av.b)

Kiv_minus = mp.iv.sqrt(17)-3
Kiv_plus = mp.iv.sqrt(17)+3

Rminus, eminus = interval_even_data(
    Kiv_minus
)
Rplus, eplus = interval_even_data(
    Kiv_plus
)

assert upper_abs(eminus[11]) < 1e-19
assert upper_abs(eplus[11]) < 1e-8

# Uniform forcing bound from j=10 onward:
# |b| < 100(2j+1)^2, |R|<=0.1.
# The polynomial*0.1^m envelope is decreasing for j>=10.
assert (
    ((23/21)**2)*0.1
) < 1.0

assert (
    100*(21**2)*1e-19
) < 1e-3

assert (
    100*(21**2)*1e-8
) < 1e-3

# ------------------------------------------------------------------
# Odd affine graph invariant boxes and contractions.
# ------------------------------------------------------------------

# Small fibre box:
# P in [.7,1.3], Q in [0,.01], G in [-1,1].
Dmin_m = 4.0
Dmax_m = 5.0 + 0.01*1.3

Plo_m = (
    4.0 - 0.01*0.01
)/Dmax_m
Phi_m = 5.0/4.0
Qhi_m = 0.01/4.0
Ghi_m = (
    0.01+0.001
)/4.0

assert Plo_m > 0.7
assert Phi_m < 1.3
assert Qhi_m < 0.01
assert Ghi_m < 1.0

LipP_m = (
    0.01*(5.0+0.01*0.01)/(4.0**2)
    + 0.01/4.0
)
LipQ_m = (
    0.01*0.01/(4.0**2)
)
LipG_m = (
    0.01*(0.01+0.001)/(4.0**2)
    + 0.01/4.0
)

assert max(
    LipP_m,
    LipQ_m,
    LipG_m,
) < 0.01

# Large fibre box:
# P in [.8,1.25], Q in [0,.06], G in [-1,1].
Dmin_p = 24.0
Dmax_p = 29.0 + 0.4*1.25

Plo_p = (
    25.0 - 0.4*0.06
)/Dmax_p
Phi_p = 29.0/24.0
Qhi_p = 1.4/24.0
Ghi_p = (
    0.4+0.001
)/24.0

assert Plo_p > 0.8
assert Phi_p < 1.25
assert Qhi_p < 0.06
assert Ghi_p < 1.0

LipP_p = (
    0.4*(29.0+0.4*0.06)/(24.0**2)
    + 0.4/24.0
)
LipQ_p = (
    1.4*0.4/(24.0**2)
)
LipG_p = (
    0.4*(0.4+0.001)/(24.0**2)
    + 0.4/24.0
)

assert max(
    LipP_p,
    LipQ_p,
    LipG_p,
) < 0.04

# ------------------------------------------------------------------
# Outward interval graph pullback to the center.
# ------------------------------------------------------------------

def interval_graph_to_center(
    Kiv,
    fibre,
):
    R, e = interval_even_data(
        Kiv
    )

    if fibre == "minus":
        P = mp.iv.mpf([0.7, 1.3])
        Q = mp.iv.mpf([0.0, 0.01])
        G = mp.iv.mpf([-1.0, 1.0])
    else:
        P = mp.iv.mpf([0.8, 1.25])
        Q = mp.iv.mpf([0.0, 0.06])
        G = mp.iv.mpf([-1.0, 1.0])

    for jj in range(10, 0, -1):
        nn = 2*jj+1

        am2 = Aiv[-2](Kiv, nn)
        a0 = Aiv[0](Kiv, nn)
        a2 = Aiv[2](Kiv, nn)
        a4 = Aiv[4](Kiv, nn)

        f = (
            biv(Kiv, nn)
            * e[jj+1]
        )

        den = a2-a4*P

        Pnew = (
            a0+a4*Q
        )/den

        Qnew = (
            -am2
        )/den

        Gnew = (
            a4*G-f
        )/den

        P, Q, G = (
            Pnew,
            Qnew,
            Gnew,
        )

    # Central c0.
    nn = 1

    a2 = Aiv[2](Kiv, nn)
    a4 = Aiv[4](Kiv, nn)

    f0 = (
        biv(Kiv, nn)
        * e[1]
    )

    c0 = (
        f0-a4*G
    )/(
        a2-a4*P
    )

    return c0, (P, Q, G)

cminus, graph_minus = (
    interval_graph_to_center(
        Kiv_minus,
        "minus",
    )
)

cplus, graph_plus = (
    interval_graph_to_center(
        Kiv_plus,
        "plus",
    )
)

# Rigorous positivity margins.
assert float(cminus.a) > 5.79
assert float(cplus.a) > 5.33

print(
    "Round 59 validated verification passed."
)
print(
    "c0 minus interval =",
    cminus,
)
print(
    "c0 plus interval  =",
    cplus,
)
print(
    "center graph minus =",
    graph_minus,
)
print(
    "center graph plus  =",
    graph_plus,
)
