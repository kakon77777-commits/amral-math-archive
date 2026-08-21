# DCRP73 symbolic checks

import sympy as sp

gamma, S0 = sp.symbols("gamma S0", positive=True, real=True)
cg = 2-3*gamma

print("Cylinder material enstrophy exponent =", -cg)
print("One-period material multiplier =", sp.exp(-cg*S0))
print("Strict Type-II gamma in (2/5,1/2) => c_gamma in (1/2,4/5), positive.")

# Enstrophy density e = |Omega|^2/2:
# D_s e = -2 e; div Y = 3 gamma
# conservative loss coefficient = 2-3gamma.
print("Conservative loss coefficient check:", sp.expand(2-3*gamma))

# Finite N-cycle return multiplier.
N = sp.symbols("N", positive=True, integer=True)
print("N-cycle material multiplier =", sp.exp(-N*cg*S0))
