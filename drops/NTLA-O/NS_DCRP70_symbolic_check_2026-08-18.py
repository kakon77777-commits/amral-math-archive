# DCRP70 symbolic verification
# Builds the joint first-jet compatibility system for:
#   L = S + R = grad V
#   H = Hess P = -(1+lambda'/lambda)S - S^2 - R^2
# after scaling lambda != 0 out of the fixed-time spatial equations.

import sympy as sp

c, rho, beta = sp.symbols("c rho beta", real=True)

e1 = sp.Matrix([1,0,0])

def crossmat(w):
    w1,w2,w3 = w
    return sp.Matrix([
        [0,-w3,w2],
        [w3,0,-w1],
        [-w2,w1,0],
    ])

S = sp.diag(
    1,
    c-sp.Rational(1,2),
    -c-sp.Rational(1,2),
)

Omega = rho*e1
R = sp.Rational(1,2)*crossmat(Omega)

# Scaled Hessian H/lambda^2.
Hess = -beta*S - S*S - R*R

# 9 frame-connection variables: three skew generators for each spatial derivative.
a = sp.symbols("a0:9")
dc = sp.symbols("c0:3")
dr = sp.symbols("r0:3")
vars_all = list(a)+list(dc)+list(dr)

Jc = sp.diag(0,1,-1)

dL = []
dH = []

for j in range(3):
    omega_j = sp.Matrix(a[3*j:3*j+3])
    Gamma = crossmat(omega_j)

    dS = Gamma*S - S*Gamma + dc[j]*Jc

    dOmega = dr[j]*e1 + rho*(Gamma*e1)
    dR = sp.Rational(1,2)*crossmat(dOmega)

    dL.append(sp.expand(dS+dR))

    dH.append(
        sp.expand(
            -beta*dS
            -(dS*S+S*dS)
            -(dR*R+R*dR)
        )
    )

eqs = []

for mats in [dL,dH]:
    for i in range(3):
        for j,k in [(0,1),(0,2),(1,2)]:
            eqs.append(
                sp.expand(
                    mats[k][i,j]-mats[j][i,k]
                )
            )

M, _ = sp.linear_eq_to_matrix(eqs, vars_all)

print("Double-integrability matrix shape:", M.shape)

# Generic c != 0 symbolic nullspace.
ns = M.nullspace()

print("\nGeneric symbolic nullity =", len(ns))

for idx,vec in enumerate(ns):
    print(f"\nNull vector {idx}:")
    for var,val in zip(vars_all,vec):
        if val != 0:
            print(" ", var, "=", sp.factor(val))

# Generic numerical rank sanity.
samples = [
    {c: sp.Rational(7,10), rho: sp.Rational(21,10), beta: sp.Rational(2,5)},
    {c: sp.Rational(11,10), rho: sp.Rational(4,5), beta: -sp.Rational(1,5)},
    {c: 2, rho: sp.Rational(13,10), beta: sp.Rational(7,10)},
]

print("\nGeneric rank checks:")
for sample in samples:
    print(sample, "rank =", M.subs(sample).rank())

# c=0 stratum.
M0 = sp.simplify(M.subs(c,0))
ns0 = M0.nullspace()

print("\nc=0 symbolic nullity =", len(ns0))

for idx,vec in enumerate(ns0):
    print(f"\nc=0 null vector {idx}:")
    for var,val in zip(vars_all,vec):
        if val != 0:
            print(" ", var, "=", sp.factor(val))

print(
    "\nInterpretation: in all generic null vectors, "
    "the only frame rotations are about e1, so d(e1)=0. "
    "At c=0 the three nulls are exactly rotations about e1 "
    "for the three derivative directions; dc=dr=0."
)
