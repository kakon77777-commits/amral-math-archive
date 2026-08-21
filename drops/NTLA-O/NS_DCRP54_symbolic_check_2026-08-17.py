# DCRP54 symbolic verification
# Verifies the Newtonian quadrupole far-field coefficient and
# the fixed-plane normal-axis sign.

import sympy as sp

r = sp.symbols("r", positive=True, real=True)
M11, M22, M33 = sp.symbols("M11 M22 M33", real=True)

# Along x = r e3:
# Hessian of 1/(4 pi |x|) has diagonal entries
# (-1, -1, 2)/(4 pi r^3).
pi = sp.pi
H_K_normal = sp.diag(
    -1/(4*pi*r**3),
    -1/(4*pi*r**3),
    2/(4*pi*r**3),
)

Mdiag = sp.diag(M11, M22, M33)
coeff = sp.simplify(sp.trace(Mdiag * H_K_normal))

print("Quadrupole potential along e3:")
print(coeff)

print("\nPlanar-vorticity specialization M33=0:")
print(sp.simplify(coeff.subs(M33, 0)))

Mtrace_planar = sp.symbols("Mtrace_planar", positive=True, real=True)
print(
    "\nWith M11+M22=Mtrace:",
    -Mtrace_planar/(4*pi*r**3),
)

# X72 longitudinal correction norm coefficient:
# Delta W_L = (3/2) T0 C, ||T0 C||^2 = (2/3)||C||^2.
factor = sp.Rational(9,4) * sp.Rational(2,3)
print("\nLongitudinal correction energy factor =", sp.simplify(factor))
