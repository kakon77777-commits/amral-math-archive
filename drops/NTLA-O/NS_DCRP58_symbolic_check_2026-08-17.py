# DCRP58 symbolic checks
# Cylindrical vorticity decomposition and beta=0 harmonic collapse.

import sympy as sp

fr, beta = sp.symbols("fr beta", real=True)

# In the moving horizontal basis (xi, eta):
# grad_h q = (fr, beta)
# J grad_h q = (-beta, fr) in the (xi,eta) components
Omega_xi = -beta
Omega_eta = fr

print("Omega dot xi =", Omega_xi)
print("Omega dot eta =", Omega_eta)

# If beta=0 and w=0 on an active open cylinder:
# incompressibility => Delta_h phi=0,
# q=-phi_z => Delta_h q=0,
# q=f(r)+c => f_rr=0.
frr = sp.symbols("frr", real=True)
Delta_h_q = frr

print("\nPure cylinder horizontal Laplacian:")
print("Delta_h q =", Delta_h_q)

# Energy exponent:
alpha = sp.symbols("alpha", real=True)
kappa = 3 - 2*alpha

print("\nDSS local-energy exponent kappa =", kappa)
print("For 1<alpha<3/2, 0<kappa<1.")
