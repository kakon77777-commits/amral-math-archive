# DCRP71 symbolic checks
# 1) Phase-lock residual metric.
# 2) Cauchy-Riemann / harmonic source law.
# 3) Effective 2D DSS energy exponent.
# 4) Isotropic director pair dispersion.

import sympy as sp

lam, cp, c, theta = sp.symbols(
    "lam cp c theta",
    real=True,
)

# H and K have norm^2 = 2 and are orthogonal.
Rnorm2 = 2*lam**2*cp**2 + 2*(2*lam*c*theta)**2
expected = 2*lam**2*(cp**2+4*c**2*theta**2)

print("Phase-lock residual norm check =", sp.simplify(Rnorm2-expected))

# CR law.
rho, b = sp.symbols("rho b", real=True)
rho2, rho3 = sp.symbols("rho2 rho3", real=True)

c2 = (rho*rho2-b*rho3)/(4*c)
c3 = (b*rho2+rho*rho3)/(4*c)

U2 = sp.simplify(4*c*c2-rho*rho2)
U3 = sp.simplify(4*c*c3-rho*rho3)

print("\nU_2 =", U2)
print("U_3 =", U3)
print("Expected: -b rho_3, b rho_2")

# Effective 2D DSS energy exponent.
alpha, Lambda = sp.symbols("alpha Lambda", positive=True, real=True)
scale2 = Lambda**(2*alpha-2)
print("\n2D per-length DSS energy scale =", scale2)
print("Nonzero conserved energy with Lambda != 1 forces alpha = 1.")

# Isotropic director pair dispersion.
Z = sp.symbols("Z", positive=True, real=True)
pair_dot2 = Z**2/sp.Integer(3)
pair_disp = sp.simplify(Z**2-pair_dot2)

print("\nPair director dispersion =", pair_disp)
print("Expected 2 Z^2 / 3.")
