# DCRP76 symbolic verification

import sympy as sp

gamma, alpha, S0 = sp.symbols(
    "gamma alpha S0",
    positive=True,
    real=True,
)

kappa = 3 - 2*alpha
cgamma = 2 - 3*gamma
relation = {gamma: 1/(alpha+1)}

print("2gamma - c_gamma - gamma*kappa:")
print(sp.simplify((2*gamma-cgamma-gamma*kappa).subs(relation)))

lamstar = cgamma/2
print("gamma - lambda_* - gamma*kappa/2:")
print(sp.simplify((gamma-lamstar-gamma*kappa/2).subs(relation)))

# Resonant amplification exponent
print("Material centered energy/enstrophy amplification:")
print(sp.exp(gamma*kappa*S0))

# Observer/material gap
T, A = sp.symbols("T A", positive=True, real=True)
sigma_E = cgamma - T/A
sigma_M = 2*gamma
gap = sp.simplify((sigma_M-sigma_E).subs(relation))
print("\nStretch-selection gap:")
print(gap)
print("minus gamma*kappa:")
print(sp.simplify((sigma_M-sigma_E-gamma*kappa).subs(relation)))

# Lambda gap
lambda_E = sigma_E/2
lambda_M = gamma
print("\nLambda-selection gap minus gamma*kappa/2:")
print(
    sp.simplify(
        (lambda_M-lambda_E-gamma*kappa/2).subs(relation)
    )
)

print(
    "\nIf Pi_circ=0 and Q is periodic: "
    "(log Q)'=2gamma-sigma, hence int sigma=2gamma S0."
)
print(
    "Also int Q'=0 gives int (sigma-2gamma)Q=0, "
    "so the ordinary and Q-weighted resonance moments both vanish."
)
