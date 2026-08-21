# DCRP79 symbolic verification

import sympy as sp

lam, rho, a, b, m = sp.symbols(
    "lam rho a b m",
    positive=True,
    real=True,
)

# D78 E_p=0 ODE
lamp = 2*rho**2 - lam - m/sp.Integer(6)
logrhop = a - 1 - lam
ap = -2*rho**2 + 2*b**2 - a + m/sp.Integer(12)
logbp = -(1 + lam + 2*a)

Fp = sp.simplify(
    ap + logrhop + lamp/sp.Integer(2)
)

Gp = sp.simplify(
    logbp + 2*logrhop
)

print("F' =", Fp)
print("Expected -rho^2 + 2b^2 - 1 - 3lambda/2.")

print("\nG' =", Gp)
print("Expected -3(1+lambda).")

gamma, S0, N = sp.symbols(
    "gamma S0 N",
    positive=True,
    real=True,
)

print("\nUnder resonance int lambda = gamma*T:")
print(
    "G(T)-G(0) =",
    -3*(1+gamma)*N*S0,
)

cF = 1 + sp.Rational(3,2)*gamma
print(
    "F secular linear coefficient c_F =",
    cF,
)

# D78 coherent return contradiction is recovered if Delta F=0,
# but D79 uses the stronger long-time drift.
print(
    "\nIf integral b^2 is finite, "
    "F(NS0) <= const - c_F*N*S0 -> -infinity."
)
