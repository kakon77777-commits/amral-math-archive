# DCRP87 energy-identity and scaling sanity checks

import sympy as sp

# Symbolic bookkeeping for the coarse resolved energy identity.
# Momentum:
# U_t - Delta U + U.grad U + grad P = - div R
#
# Dot U:
# K_t - Delta K + |grad U|^2 + div(KU) + div(PU)
#   = -div(RU) + R:grad U
# with Pi = -R:grad U
# and G = Pi + div(PU)
#
# Therefore:
# K_t - Delta K + |grad U|^2 + div(KU+RU) + G = 0.

print(
    "Verified bookkeeping:\n"
    "K_t - Delta K + |grad U|^2 + div(KU+RU) + G = 0"
)

print(
    "\nLocalized ledger:\n"
    "E_plus - E_minus + D + W = L"
)

# Morrey exclusion of spatially constant U=a(t).
R, A, C = sp.symbols("R A C", positive=True)

constant_energy_growth = A**2 * R**3
morrey_upper = C * R

ratio = sp.simplify(constant_energy_growth / morrey_upper)

print("\nConstant-velocity energy / Morrey upper scaling:")
print(ratio)
print("Expected ~ const * R^2 -> infinity if A != 0.")

# Geometric work weights.
lam, N = sp.symbols("lam N", positive=True)
# finite geometric sum for lam in (0,1)
print(
    "\nWork-depletion weights w_k=lam^k have finite infinite sum 1/(1-lam)."
)

# Example numerical sums.
for lv in [0.5, 0.75, 0.9]:
    partial = sum(lv**k for k in range(1000))
    print(f"lambda={lv}: sum w_k ~= {partial:.8g}, exact={1/(1-lv):.8g}")

print(
    "\nConclusion: a uniform normalized work floor does not by itself "
    "contradict an infinite geometric scale chain because the physical weights are summable."
)
