# DCRP61 symbolic checks

import sympy as sp

lam, gamma = sp.symbols("lam gamma", real=True)
m = sp.symbols("m", positive=True, real=True)

# Material enstrophy-density + similarity-volume exponent:
exp_material = sp.expand(2*(lam-1) + 3*gamma)
lam_neutral = sp.solve(sp.Eq(exp_material, 0), lam)[0]

print("Material covariance exponent =", exp_material)
print("Neutral aligned lambda =", lam_neutral)
print("Expected (2-3gamma)/2 =", sp.simplify((2-3*gamma)/2))
print("Difference =", sp.simplify(lam_neutral-(2-3*gamma)/2))

# Stress source decomposition:
# S Omega = lambda Omega + tau, tau.Omega=0
# B^0 = (SΩ⊗Ω + Ω⊗SΩ - 2/3 sigma I)
#       = 2 lambda W + tau⊗Ω + Ω⊗tau.
# Check coefficients abstractly by Q = W + m/3 I.
coef_iso = sp.simplify(
    2*lam*(m/sp.Integer(3))
    - sp.Rational(2,3)*lam*m
)
print("\nIsotropic coefficient after rewriting 2 lambda Q - 2/3 lambda m I:")
print(coef_iso, "(should be 0)")

# Fixed isotropic covariance trace law:
rho = sp.symbols("rho", positive=True, real=True)
cgamma = 2 - 3*gamma
rho_rate = sp.expand((2*lam-cgamma)*rho)
print("\nIsotropic covariance rho' =", rho_rate)
print(
    "Periodic neutral mean lambda =",
    sp.simplify(cgamma/2),
)
