# DCRP75 symbolic verification

import sympy as sp

gamma, kappa, cg = sp.symbols("gamma kappa cg", real=True)
M, K, Ktr, Kc, Z = sp.symbols("M K Ktr Kc Z", positive=True)
Pi, Piaff, Pic = sp.symbols("Pi Piaff Pic", real=True)
sigma = sp.symbols("sigma", real=True)

# Identities
# M' = 3 gamma M
# K' = gamma kappa K - Pi
# Ktr' = gamma kappa Ktr - Piaff
# Kc = K-Ktr
print("Centered energy derivative:")
print("Kc' = gamma*kappa*Kc - Pic")

# Z' = -cg Z + W = (-cg + sigma) Z
# Qc = Kc/Z
# coefficient gamma*kappa + cg = 2gamma in project scaling
print("General centered ratio:")
print("Qc' = (gamma*kappa + cg - sigma) Qc - Pic/Z")
print("Using gamma*kappa + cg = 2gamma:")
print("Qc' = (2gamma - sigma) Qc - Pic/Z")

# zero-stretch periodic gap Cauchy calculation
I_Q = sp.symbols("I_Q", positive=True)
A = 2*gamma*I_Q
lower_grad_var = sp.simplify(A**2/(2*I_Q))
print("\nZero-stretch periodic pressure-gradient variance lower bound:")
print(lower_grad_var)
print("Expected 2 gamma^2 I_Q.")

# D62 zero-stretch defect floor
m = sp.symbols("m", positive=True)
Ep_sq_floor = m**2/sp.Integer(36)
W_sq = sp.Rational(2,3)*m**2
print("\nEp floor / W floor ratio:")
print(sp.simplify(Ep_sq_floor/W_sq))
print("Expected 1/24.")

# pointwise silent stretching rate and enstrophy growth
# if sigma=2gamma, Z'/Z = -cg + 2gamma;
# with cg=2-3gamma -> 5gamma-2 = gamma*kappa
expr = sp.simplify(- (2-3*gamma) + 2*gamma)
print("\nZ growth at sigma=2gamma:", expr)
print("Expected 5gamma-2 = gamma*kappa.")
