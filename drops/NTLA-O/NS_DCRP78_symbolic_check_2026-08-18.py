# DCRP78 symbolic checks

import sympy as sp

gamma, S0 = sp.symbols("gamma S0", positive=True, real=True)
Rrho, M = sp.symbols("Rrho M", positive=True, real=True)

# Resonant return consequences:
Aint = (1+gamma)*S0
b_log_coeff = S0 + gamma*S0 + 2*Aint

print("Integral coefficient in b'/b:")
print(sp.expand(b_log_coeff))
print("Expected 3(1+gamma)S0.")

# lambda return:
# 0 = 2Rrho - gamma*S0 - M/6
M_over_12 = Rrho - gamma*S0/2

# a return with b=0:
a_return = sp.simplify(
    -2*Rrho - Aint + M_over_12
)

print("\nFinal a-return expression:")
print(sp.factor(a_return))
print("Expected -Rrho -(1+3gamma/2)S0 < 0.")

# Tilt Hessian silent multiplier
mult_exponent = -(1+2*gamma)*S0
print("\nPressure-Hessian-silent resonant tilt multiplier exponent:")
print(mult_exponent)

# General moving-frame matrix bookkeeping
lam, rho, a, b, m = sp.symbols(
    "lam rho a b m",
    real=True
)

S = sp.Matrix([
    [lam, rho, 0],
    [rho, a, b],
    [0, b, -lam-a],
])

print("\nTrace S =", sp.simplify(sp.trace(S)))
print("S*e1 =", S[:,0])

print(
    "\nE_p=0 ODE ledger used:\n"
    "lambda' = 2 rho^2 - lambda - m/6\n"
    "rho'/rho = a - 1 - lambda\n"
    "a' = -2 rho^2 + 2 b^2 - a + m/12\n"
    "b' = -(1+lambda+2a)b\n"
    "m' = 2(lambda-1)m"
)
