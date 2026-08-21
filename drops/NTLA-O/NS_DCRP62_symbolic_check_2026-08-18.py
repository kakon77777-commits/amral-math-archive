# DCRP62 symbolic verification
# Checks:
# 1. pressure/cofactor cancellation on an aligned eigenvector
# 2. neutral Floquet sign

import sympy as sp

Dsl, lam, Smag2, m, gamma, S0 = sp.symbols(
    "Dsl lam Smag2 m gamma S0",
    real=True,
)
# Pressure-Hessian eigenvalue under persistent alignment:
mu_H = -(Dsl + lam + lam**2)

# Delta P = -|S|^2 + m/2
DeltaP = -Smag2 + m/2

# H^0 eigenvalue:
mu_H0 = sp.simplify(mu_H - DeltaP/3)

# C_S^0 eigenvalue:
mu_C0 = lam**2 - Smag2/3

mu_E = sp.simplify(mu_H0 + mu_C0)

print("H eigenvalue =", mu_H)
print("H^0 eigenvalue =", mu_H0)
print("C_S^0 eigenvalue =", mu_C0)
print("E_p eigenvalue =", mu_E)
print(
    "Expected = -(D_s lambda + lambda + m/6):",
    sp.simplify(mu_E + Dsl + lam + m/6),
)

c_gamma = 2 - 3*gamma
lam_bar = c_gamma/2

print("\nNeutral Floquet mean lambda =", lam_bar)
print(
    "Strict Type-II range gamma in (2/5,1/2) => lambda_bar in (1/4,2/5)."
)

# Integrated E_p directional action when lambda returns:
M_int = sp.symbols("M_int", positive=True, real=True)
period_integral = sp.simplify(-lam_bar*S0 - M_int/6)
print("\nOne-period directional E_p integral =", period_integral)
