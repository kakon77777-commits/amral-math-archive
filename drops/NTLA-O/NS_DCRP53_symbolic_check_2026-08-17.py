# DCRP53 symbolic verification
# Checks the nilpotent vorticity-gradient identity and X72 visibility constants.

import sympy as sp

kappa = sp.symbols("kappa", real=True)
l1, l2, l3 = sp.symbols("l1 l2 l3", real=True)

ell = sp.Matrix([l1, l2, l3])

R = sp.Matrix([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 0],
])

mvec = R * ell
A = kappa * (mvec * ell.T)

print("ell dot R ell =", sp.simplify((ell.T * mvec)[0]))
print("A^2 =")
sp.pprint(sp.simplify(A * A))
print("trace(A^2) =", sp.simplify(sp.trace(A * A)))
print("trace(A) =", sp.simplify(sp.trace(A)))

# X72 stress algebra constants: m = |Omega|^2.
m = sp.symbols("m", positive=True, real=True)

# total stress norm squared = 2/3 m^2
total = sp.Rational(2, 3) * m**2

# null-envelope: T0*W = m/3, V = 1/12 m,
# W_L = 1/2 T0(m), and ||T0 m||^2 = 2/3 ||m||^2.
visible = sp.Rational(1, 4) * sp.Rational(2, 3) * m**2
invisible = sp.simplify(total - visible)

print("\nPointwise coefficient bookkeeping:")
print("total coefficient =", sp.factor(total / m**2))
print("visible coefficient =", sp.factor(visible / m**2))
print("invisible coefficient =", sp.factor(invisible / m**2))
print("visible fraction =", sp.simplify(visible / total))
print("invisible fraction =", sp.simplify(invisible / total))

# Simultaneous null-direction impossibility for G and M.
G = sp.diag(1, 1, -1)
M = sp.diag(1, 1, -sp.Rational(3, 2))

print("\nG-null quadratic =", sp.expand((ell.T * G * ell)[0]))
print("M-null quadratic =", sp.expand((ell.T * M * ell)[0]))
print(
    "Difference M-null - G-null =",
    sp.expand((ell.T * (M-G) * ell)[0]),
)
