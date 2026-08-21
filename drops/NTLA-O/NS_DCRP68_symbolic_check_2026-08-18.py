# DCRP68 symbolic verification
# 1) Type-A first-jet compatibility determinant and resonant nullity.
# 2) Type-B first-jet connection and curvature obstruction.

import sympy as sp

lam, r = sp.symbols("lam r", real=True)

def crossmat(w):
    w1, w2, w3 = w
    return sp.Matrix([
        [0, -w3, w2],
        [w3, 0, -w1],
        [-w2, w1, 0],
    ])

# ------------------------------------------------------------
# Type A
# ------------------------------------------------------------
e3 = sp.Matrix([0, 0, 1])

p = sp.symbols("p0:3")
q = sp.symbols("q0:3")
g = sp.symbols("g0:3")

dLs = []
for a in range(3):
    dxi = sp.Matrix([p[a], q[a], 0])
    dOm = sp.Matrix([r*p[a], r*q[a], g[a]])
    dS = sp.Rational(3,2)*lam*(dxi*e3.T + e3*dxi.T)
    dR = sp.Rational(1,2)*crossmat(dOm)
    dLs.append(sp.simplify(dS+dR))

eqs = []
for i in range(3):
    for j, k in [(0,1),(0,2),(1,2)]:
        eqs.append(sp.expand(dLs[k][i,j]-dLs[j][i,k]))

varsA = list(p)+list(q)+list(g)
MA, _ = sp.linear_eq_to_matrix(eqs, varsA)

detA = sp.factor(MA.det())
print("Type-A determinant:")
sp.pprint(detA)

for rval in [3*lam, -3*lam]:
    Mr = sp.simplify(MA.subs(r, rval))
    print("\nType-A resonance", rval, "nullity =", len(Mr.nullspace()))

# ------------------------------------------------------------
# Type B
# ------------------------------------------------------------
# adapted frame xi=e1, eta=e2, zeta=e3
e1 = sp.Matrix([1,0,0])

aa = sp.symbols("a0:3") # d_j xi along eta
bb = sp.symbols("b0:3") # d_j xi along zeta; d_j zeta along -xi
dd = sp.symbols("d0:3") # d_j zeta along eta
gg = sp.symbols("G0:3") # d_j r

dLsB = []
for j in range(3):
    dxi = sp.Matrix([0, aa[j], bb[j]])
    dzeta = sp.Matrix([-bb[j], dd[j], 0])
    dS = -3*lam*(dzeta*e3.T + e3*dzeta.T)
    dOm = sp.Matrix([gg[j], r*aa[j], r*bb[j]])
    dR = sp.Rational(1,2)*crossmat(dOm)
    dLsB.append(sp.simplify(dS+dR))

eqsB = []
for i in range(3):
    for j, k in [(0,1),(0,2),(1,2)]:
        eqsB.append(sp.expand(dLsB[k][i,j]-dLsB[j][i,k]))

varsB = list(aa)+list(bb)+list(dd)+list(gg)
MB, _ = sp.linear_eq_to_matrix(eqsB, varsB)

print("\nType-B compatibility rank =", MB.rank())
print("Type-B generic nullity =", len(varsB)-MB.rank())

# ------------------------------------------------------------
# Curvature check from invariant Type-B frame connection
# ------------------------------------------------------------
alpha, kval, kval1 = sp.symbols("alpha k k1", real=True)

# R(xi,eta)xi:
# D_xi(D_eta xi) = D_xi(alpha*k eta)
# with xi(alpha)=0, D_xi eta=-k zeta
term1_eta = alpha*kval1
term1_zeta = -alpha*kval**2

# [xi,eta] = -alpha*k eta - k zeta
# D_[xi,eta] xi = alpha*k^2 zeta
comm_zeta = alpha*kval**2

R_eta = sp.simplify(term1_eta)
R_zeta = sp.simplify(term1_zeta - comm_zeta)

print("\nType-B curvature components:")
print("eta component =", R_eta)
print("zeta component =", R_zeta)
print("Flatness with alpha != 0 forces k=0.")
