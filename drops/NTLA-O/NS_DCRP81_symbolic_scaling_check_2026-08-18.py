# DCRP81 scaling / decomposition sanity checks

import sympy as sp

eps, p = sp.symbols("eps p", positive=True, real=True)

ell = eps**p
exponent = sp.simplify(1-sp.Rational(7,2)*p)

print("Filtered viscous Kelvin factor:")
print("eps * ell^(-7/2) = eps^", exponent)
print("Vanishing condition exponent > 0 => p < 2/7.")

print("\nAt p=1/4:")
print("exponent =", sp.simplify(exponent.subs(p, sp.Rational(1,4))))
print("Expected 1/8 > 0.")

# Exact algebraic decomposition
K, M, Kfv, Ksgs = sp.symbols("K M Kfv Ksgs")
print("\nExact decomposition:")
print(sp.Eq(K, M + Kfv + Ksgs))

# Filter-kernel derivative scaling in d=3:
# phi_l ~ l^-3, Delta adds l^-2, L2 contributes l^(3/2)
d = 3
delta_L2_exp = -(d+2) + sp.Rational(d,2)
print("\n||Delta phi_l||_2 scaling exponent:", delta_L2_exp)
print("Expected -7/2.")

print(
    "\nSGS circulation forcing is the surface pairing of "
    "C_l^omega = -curl div R_l."
)
