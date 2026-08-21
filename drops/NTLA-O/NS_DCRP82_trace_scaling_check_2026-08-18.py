# DCRP82 scaling / trace-ratio checks

import sympy as sp

r, ell, delta, L, T = sp.symbols(
    "r ell delta L T",
    positive=True,
    real=True,
)

# K bound:
# |K| <= ell^-1 * (L*T)^(1/2) * (int_C M^4)^(1/2)
# with L*T ~ r^3 and S_C = r int_C M^4.
# Thus K^2 <= (r/ell)^2 S_C.

print("If L*T ~ r^3 and S_C = r * I_C:")
print("K^2 factor = (r/ell)^2 * S_C.")

# Trace ratio countermodel
Theta = sp.simplify(ell**2/delta**2)
Vnorm = sp.simplify(delta**2/ell**2)

print("\nCodimension-two concentration model:")
print("Theta_tr ~", Theta)
print("tube-normalized volumetric mass ~", Vnorm)
print("product =", sp.simplify(Theta*Vnorm))
print("Expected O(1) line mass.")

sigma = sp.symbols("sigma", positive=True)
fixed_ratio = sp.simplify((r/ell)**2).subs(ell, sigma*r)
print("\nAt ell=sigma*r:")
print("(r/ell)^2 =", fixed_ratio)

print(
    "\nCorrected terminal logic:\n"
    "nonzero K_sgs + vanishing S_vol => Theta_tr -> infinity."
)
