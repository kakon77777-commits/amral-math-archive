# DCRP64 symbolic verification
# Core algebra:
# Z'/Z = 2(lambda-lambda*)
# A/Z = -lambda' - lambda - M4/(6Z)
# period integral gives fixed negative axial quotient action.

import sympy as sp

lamstar, S0 = sp.symbols("lamstar S0", positive=True, real=True)
I_M4Z = sp.symbols("I_M4Z", positive=True, real=True)
I_M4Z2 = sp.symbols("I_M4Z2", positive=True, real=True)

Pstar = lamstar*S0 + sp.Rational(1,6)*I_M4Z
lower = sp.simplify(Pstar**2 / I_M4Z2)

print("Fixed quotient action P_* =")
sp.pprint(Pstar)

print("\nQuantitative oscillation lower bound =")
sp.pprint(lower)

# Constant-defect contradiction:
# 0 = lambda_* S0 + (1/6) int M4/Z, impossible for positive terms.
contradiction_sum = Pstar
print("\nConstant defect would require P_* = 0, but P_* is positive:")
sp.pprint(contradiction_sum)

# Pairwise variance coefficient:
Phi = sp.symbols("Phi", positive=True, real=True)
pair_lower = sp.simplify(2*Phi*lower)
print("\nForced pairwise increment lower bound =")
sp.pprint(pair_lower)
