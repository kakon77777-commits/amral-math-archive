# DCRP69 symbolic verification

import sympy as sp

lam, d, m = sp.symbols("lam d m", real=True)
e, f, g = sp.symbols("e f g", real=True)
c = sp.symbols("c", real=True)

U = sp.diag(
    sp.Rational(2,3),
    -sp.Rational(1,3),
    -sp.Rational(1,3),
)
H = sp.diag(0,1,-1)
K = sp.Matrix([
    [0,0,0],
    [0,0,1],
    [0,1,0],
])

S = sp.Rational(3,2)*lam*U + d*H
a = sp.Rational(3,4)*lam**2-d**2
C = a*U-lam*d*H
W = m*U
E = e*U+f*H+g*K

def project_coeff(M, B):
    return sp.simplify(
        sp.trace(M.T*B)
        /
        sp.trace(B.T*B)
    )

# L_S(E)
LS = (
    -(E*S+S*E)
    + sp.Rational(2,3)*sp.trace(S*E)*sp.eye(3)
)

G0 = m*S/sp.Integer(6) - lam*W/sp.Integer(2)
F = sp.simplify(LS+G0)

AU = project_coeff(F,U)
BH = project_coeff(F,H)
GK = project_coeff(F,K)

print("Angular driver U coefficient =", AU)
print("Angular driver H coefficient =", BH)
print("Angular driver K coefficient =", GK)

parallel_condition = sp.factor(a*BH+lam*d*AU)
print("\nU-H phase-lock condition factor:")
sp.pprint(parallel_condition)

# Substitute D62 axial pressure coefficient.
lamp = sp.symbols("lamp", real=True)
e_aligned = -sp.Rational(3,2)*(lamp+lam+m/sp.Integer(6))

f_lock = sp.solve(
    sp.Eq(
        4*d*e_aligned+d*m-6*f*lam,
        0
    ),
    f
)[0]

print("\nPhase-lock transverse pressure coefficient:")
sp.pprint(sp.factor(f_lock))

# Counter-shape torque norm.
C2 = sp.simplify(sp.trace(C.T*C))
G02 = sp.simplify(sp.trace(G0.T*G0))
CG = sp.simplify(sp.trace(C.T*G0))
perp2 = sp.factor(G02-CG**2/C2)

print("\n|P_C^perp G0|^2 =")
sp.pprint(perp2)

# Pressure-defect floor for d=c lambda.
at = sp.symbols("at", real=True)
Sc = sp.simplify(S.subs(d,c*lam))
Ec = -at*Sc-W/sp.Integer(4)

E2 = sp.factor(sp.trace(Ec.T*Ec))
x = sp.symbols("x", real=True)
E2x = sp.factor(E2.subs(at, x/lam))

print("\nPhase-lock |E_p|^2 as quadratic in x=at*lambda:")
sp.pprint(E2x)

xmin = sp.simplify(
    -sp.diff(E2x,x).subs(x,0)
    /
    (2*sp.diff(E2x,x,2)/2)
)

# safer direct solve
xmin = sp.solve(sp.Eq(sp.diff(E2x,x),0),x)[0]
Emin = sp.factor(E2x.subs(x,xmin))

print("minimizer x =")
sp.pprint(xmin)
print("minimum =")
sp.pprint(Emin)

expected = c**2*m**2/(6*(4*c**2+3))
print("minimum check =", sp.simplify(Emin-expected))
