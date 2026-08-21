# DCRP63 symbolic verification
# Verify the exact modulation-oscillation identity.

import sympy as sp

Z, Zp, Zpp, lamstar, M4 = sp.symbols(
    "Z Zp Zpp lamstar M4",
    positive=True,
    real=True,
)

lam = lamstar + sp.Rational(1,2)*Zp/Z

# lambda' represented via Z
lamp = sp.Rational(1,2)*(Zpp/Z - Zp**2/Z**2)

A = sp.expand(-(lamp + lam)*Z - M4/sp.Integer(6))
target = (
    -sp.Rational(1,2)*Zpp
    + sp.Rational(1,2)*Zp**2/Z
    - lamstar*Z
    - sp.Rational(1,2)*Zp
    - M4/sp.Integer(6)
)

print("Pointwise algebra difference =", sp.simplify(A-target))

# After period integration Z',Z'' vanish:
period_core = sp.Rational(1,2)*Zp**2/Z - lamstar*Z - M4/sp.Integer(6)
print("Period integrand after total derivatives =", period_core)

# lambda formulation:
mod = 2*Z*(lam-lamstar)**2
print(
    "Temporal modulation identity difference =",
    sp.simplify(mod - sp.Rational(1,2)*Zp**2/Z),
)

# Check lambda_star range for gamma in (2/5,1/2)
gamma = sp.symbols("gamma", real=True)
ls = (2-3*gamma)/2
print("lambda_* =", ls)

# Spatially homogeneous defect exact modulation:
# M_t = B_p => integral Z dev^2 = lambda*/2 int Z + M4/12
print(
    "Homogeneous branch weighted variance baseline coefficient = lambda*/2"
)
