"""
Verification for NS_X72 Round 55.

Checks:
1. raw physical reflection intertwining for state/source finite sections;
2. physical localized adjoint extraction without compact-block coordinates;
3. canonical central normalization psi_+(0)=1, psi_+(1)=0 and
   psi_-(0)=0, psi_-(1)=1;
4. reflection and anti-linear C symmetry residuals;
5. exact target sign relations on the two sqrt(17) fibres;
6. one-coefficient pairing identity for psi_+;
7. cutoff convergence and positivity of Im psi_+(3) at nu=1.

The infinite-dimensional positivity theorem remains open.
"""
import math
import numpy as np
import sympy as sp

# ------------------------------------------------------------
# Raw physical sideband functions
# ------------------------------------------------------------

def dot(a, b):
    return np.dot(a, b)

def cross(a, b):
    return np.cross(a, b)

e3 = np.array([0.0+0.0j, 0.0, 1.0])

def avec(s):
    return np.array(
        [1.0, 1.0j*s, 0.0],
        dtype=complex,
    )/2.0

def Nside(K, level, B, s):
    k = np.array(
        [K, 0.0, float(level)],
        dtype=complex,
    )
    kout = k+s*e3
    a = avec(s)
    return (
        2*dot(a, B)
        + 6j*dot(
            kout,
            cross(
                a,
                1j*cross(k, B)-B,
            ),
        )/dot(kout, kout)
    )

def vel(K, level, B):
    k = np.array(
        [K, 0.0, float(level)],
        dtype=complex,
    )
    return 1j*cross(k, B)/dot(k, k)

def EulerSide(K, level, B, s):
    k = np.array(
        [K, 0.0, float(level)],
        dtype=complex,
    )
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
            out[off] = (
                out.get(off, 0.0)
                + Nside(K, p, C, t)
            )

    k2 = K*K + level*level
    for s in (-1, 1):
        out[s] = (
            out.get(s, 0.0)
            + nu*Nside(
                K,
                level,
                -k2*B,
                s,
            )
        )
    return out

def divfree_basis(K, level):
    den = math.sqrt(
        K*K+level*level
    )
    vxz = np.array(
        [
            level/den,
            0.0,
            -K/den,
        ],
        dtype=complex,
    )
    ey = np.array(
        [0.0, 1.0, 0.0],
        dtype=complex,
    )
    return vxz, ey

def physical_matrices(K, N, nu):
    levels = list(range(-N, N+1))
    basis = []
    for n in levels:
        v1, v2 = divfree_basis(K, n)
        basis.append((n, 0, v1))
        basis.append((n, 1, v2))

    nouts = list(
        range(-N-1, N+2)
    )
    Nmat = np.zeros(
        (len(nouts), len(basis)),
        dtype=complex,
    )
    for j, (n, bidx, B) in enumerate(basis):
        for s in (-1, 1):
            mm = n+s
            if mm in nouts:
                Nmat[
                    nouts.index(mm), j
                ] += Nside(
                    K, n, B, s
                )

    souts = list(
        range(-N-2, N+3)
    )
    Smat = np.zeros(
        (len(souts), len(basis)),
        dtype=complex,
    )
    for j, (n, bidx, B) in enumerate(basis):
        out = source_single(
            K, n, B, nu
        )
        for off, val in out.items():
            mm = n+off
            if mm in souts:
                Smat[
                    souts.index(mm), j
                ] += val

    return (
        basis,
        nouts,
        Nmat,
        souts,
        Smat,
    )

# ------------------------------------------------------------
# Reflection matrices
# ------------------------------------------------------------

def reflection_domain_matrix(basis):
    # P=diag(1,-1,-1) maps each chosen transverse basis
    # at n to minus the same basis label at -n.
    dim = len(basis)
    D = np.zeros((dim, dim), complex)

    index = {
        (n, bidx): j
        for j, (n, bidx, B) in enumerate(basis)
    }
    for j, (n, bidx, B) in enumerate(basis):
        jp = index[(-n, bidx)]
        D[jp, j] = -1.0
    return D

def reflection_output_matrix(levels):
    dim = len(levels)
    R = np.zeros((dim, dim), complex)
    index = {
        m: i for i, m in enumerate(levels)
    }
    for i, m in enumerate(levels):
        R[index[-m], i] = 1.0
    return R

# ------------------------------------------------------------
# Localized physical adjoint modes
# ------------------------------------------------------------

def source_hidden_map(K, N, nu, tol=1e-12):
    (
        basis,
        nouts,
        Nmat,
        souts,
        Smat,
    ) = physical_matrices(
        K, N, nu
    )

    U0, S0, Vh0 = np.linalg.svd(
        Nmat,
        full_matrices=True,
    )
    rankN = int(
        np.sum(
            S0 > tol*S0[0]
        )
    )
    Q = Vh0.conj().T[:, rankN:]
    A = Smat @ Q

    U, S, Vh = np.linalg.svd(
        A,
        full_matrices=True,
    )
    rankA = int(
        np.sum(
            S > tol*S[0]
        )
    )

    return {
        "basis": basis,
        "nouts": nouts,
        "Nmat": Nmat,
        "souts": souts,
        "Smat": Smat,
        "Q": Q,
        "A": A,
        "U": U,
        "rankA": rankA,
    }

def localized_cokernel(K, N, nu):
    d = source_hidden_map(
        K, N, nu
    )
    souts = d["souts"]
    U = d["U"]
    rankA = d["rankA"]
    left = U[:, rankA:]

    # Isolate the two modes with minimal boundary mass.
    mask = np.array(
        [
            1.0
            if abs(m) > N-6
            else 0.0
            for m in souts
        ]
    )
    B = (
        left.conj().T
        @ (mask[:, None]*left)
    )
    vals, vecs = np.linalg.eigh(B)
    loc = left @ vecs[:, :2]

    return souts, loc, vals[:2]

def canonical_modes(K, N, nu):
    souts, loc, vals = localized_cokernel(
        K, N, nu
    )

    M = np.array(
        [
            [
                loc[
                    souts.index(0), j
                ]
                for j in range(2)
            ],
            [
                loc[
                    souts.index(1), j
                ]
                for j in range(2)
            ],
        ],
        dtype=complex,
    )

    C = np.linalg.inv(M)
    can = loc @ C

    return souts, can, vals

# ------------------------------------------------------------
# Target
# ------------------------------------------------------------

def target_values(r, nu):
    return {
        -3:
            4j*r*(17*r*r-8)
            /(3*(4*r*r+9)),
        -1:
            2j*r*(37*r*r-11)
            /(3*(4*r*r+1)),
        0:
            12*nu*(3*r*r-1),
        1:
            -2j*r*(13*r*r-5)
            /(3*(4*r*r+1)),
    }

def target_vector(r, nu, souts):
    g = np.zeros(
        len(souts),
        dtype=complex,
    )
    for m, val in target_values(
        r, nu
    ).items():
        g[
            souts.index(m)
        ] = val
    return g

# ------------------------------------------------------------
# Exact target sign checks
# ------------------------------------------------------------

sqrt17 = sp.sqrt(17)
xminus = (
    13-3*sqrt17
)/2
xplus = (
    13+3*sqrt17
)/2

assert float(3*xminus-1) < 0
assert float(17*xminus-8) < 0
assert float(3*xplus-1) > 0
assert float(17*xplus-8) > 0

# ------------------------------------------------------------
# Numerical checks at nu=1
# ------------------------------------------------------------

rminus = (
    math.sqrt(17)-3
)/2
rplus = (
    math.sqrt(17)+3
)/2

fibres = [
    (2*rminus, rminus),
    (2*rplus, rplus),
]

# Raw reflection intertwining.
for K, r in fibres:
    (
        basis,
        nouts,
        Nmat,
        souts,
        Smat,
    ) = physical_matrices(
        K, 10, 1.0
    )
    DR = reflection_domain_matrix(
        basis
    )
    RN = reflection_output_matrix(
        nouts
    )
    RS = reflection_output_matrix(
        souts
    )

    assert (
        np.linalg.norm(
            Nmat@DR - RN@Nmat
        )
        < 1e-11
    )
    assert (
        np.linalg.norm(
            Smat@DR - RS@Smat
        )
        < 1e-10
    )

# Canonical symmetry and pairing convergence.
expected_a3 = [
    0.041191045742266,
    0.084276516264333,
]
expected_pair = [
    -0.655636066314278,
    446.038740993707,
]

for fi, (K, r) in enumerate(fibres):
    vals_a3 = []
    vals_pair = []

    for N in (
        8, 10, 12, 20, 40, 60
    ):
        souts, can, locvals = (
            canonical_modes(
                K, N, 1.0
            )
        )

        psi_plus = can[:, 0]
        psi_minus = can[:, 1]

        # Central normalization.
        assert abs(
            psi_plus[
                souts.index(0)
            ] - 1
        ) < 1e-10
        assert abs(
            psi_plus[
                souts.index(1)
            ]
        ) < 1e-10

        assert abs(
            psi_minus[
                souts.index(0)
            ]
        ) < 1e-10
        assert abs(
            psi_minus[
                souts.index(1)
            ] - 1
        ) < 1e-10

        # Reflection / anti-linear C sector checks are imposed only
        # after the boundary-localization eigenspace has cleanly split.
        # Very shallow cutoffs are retained only as convergence diagnostics.
        if N >= 20:
            Rplus = np.array(
                [
                    psi_plus[
                        souts.index(-m)
                    ]
                    for m in souts
                ]
            )
            Rminus = np.array(
                [
                    psi_minus[
                        souts.index(-m)
                    ]
                    for m in souts
                ]
            )
            assert (
                np.linalg.norm(
                    Rplus-psi_plus
                )
                < 1e-10
            )
            assert (
                np.linalg.norm(
                    Rminus-psi_minus
                )
                < 1e-10
            )

            Cplus = np.array(
                [
                    ((-1)**m)
                    * np.conj(
                        psi_plus[i]
                    )
                    for i, m
                    in enumerate(souts)
                ]
            )
            Cminus = np.array(
                [
                    ((-1)**m)
                    * np.conj(
                        psi_minus[i]
                    )
                    for i, m
                    in enumerate(souts)
                ]
            )

            assert (
                np.linalg.norm(
                    Cplus-psi_plus
                )
                < 1e-10
            )
            assert (
                np.linalg.norm(
                    Cminus+psi_minus
                )
                < 1e-10
            )

        g = target_vector(
            r, 1.0, souts
        )

        pair = np.vdot(
            psi_plus, g
        )

        a3 = float(
            psi_plus[
                souts.index(3)
            ].imag
        )

        Gm3 = float(
            target_values(
                r, 1.0
            )[-3].imag
        )
        g0 = float(
            target_values(
                r, 1.0
            )[0].real
        )

        pair_reduced = (
            g0 + Gm3*a3
        )

        assert abs(
            pair.imag
        ) < 1e-10
        assert abs(
            pair.real-pair_reduced
        ) < 1e-10

        vals_a3.append(a3)
        vals_pair.append(
            pair.real
        )

    assert min(vals_a3) > 0
    assert abs(
        vals_a3[-1]
        - expected_a3[fi]
    ) < 5e-13
    assert abs(
        vals_pair[-1]
        - expected_pair[fi]
    ) < 5e-10

    # Stabilization from N=12 onward.
    assert (
        max(vals_a3[2:])
        - min(vals_a3[2:])
        < 5e-13
    )

print(
    "Round 55 verification passed."
)

for fi, (K, r) in enumerate(fibres):
    print()
    print("K =", K)
    for N in (
        8, 10, 12, 20, 40, 60
    ):
        souts, can, vals = (
            canonical_modes(
                K, N, 1.0
            )
        )
        psi_plus = can[:, 0]
        g = target_vector(
            r, 1.0, souts
        )
        print(
            "N =",
            N,
            "Im psi_+(3) =",
            psi_plus[
                souts.index(3)
            ].imag,
            "pairing =",
            np.vdot(
                psi_plus, g
            ).real,
        )
