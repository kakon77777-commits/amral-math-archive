# DCRP83 symbolic scaling checks

import sympy as sp

Theta, beta = sp.symbols("Theta beta", positive=True)
r, ell, delta, sigma, pmax = sp.symbols(
    "r ell delta sigma pmax",
    positive=True,
)

# H(delta)=Theta^beta and A(delta)<=A(ell)
# implies ell^2/delta^2 >= Theta^beta
delta_ratio = Theta**(-beta/2)
print("General extraction bound delta/ell <=", delta_ratio)

print(
    "At beta=1/2:",
    sp.simplify(delta_ratio.subs(beta, sp.Rational(1,2))),
)
print("Expected Theta^(-1/4).")

# Number of parabolic line cells
N = (r/delta)**3
print("\nParabolic line cell count ~", N)

# Local atom transfer ratio:
# small S / outer S ~ (ell/r)^3 (r/delta)^2 pmax
ratio = sp.simplify(
    (ell/r)**3 * (r/delta)**2 * pmax
)
print("Local descendant ratio =", ratio)

fixed = sp.simplify(ratio.subs(ell, sigma*r))
print("At ell=sigma*r:", fixed)

threshold = (delta/r)**2
print("pmax threshold for O(1) descendant ~", threshold)
print(
    "Ratio at threshold:",
    sp.simplify(fixed.subs(pmax, threshold)),
)

uniform_p = (delta/r)**3
print(
    "Ratio under uniform parabolic spreading:",
    sp.simplify(fixed.subs(pmax, uniform_p)),
)
print("Expected sigma^3 * delta/r.")

# Rerooted filter ratio
Lambda = sp.simplify(ell/delta)
print("\nRerooted relative filter ratio Lambda =", Lambda)

# With delta/ell <= Theta^-1/4
print("Lambda lower bound ~ Theta^(1/4).")
