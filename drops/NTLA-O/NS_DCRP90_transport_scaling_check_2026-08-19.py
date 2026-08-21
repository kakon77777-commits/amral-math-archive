# DCRP90 transport-action / R^2-vs-R scaling sanity checks

import math

gamma = 0.45
Tstar = 3.0
R0 = 4.0

def action_lower(R, T=Tstar):
    # exact lower bound from variation of constants:
    # int |U| >= R - exp(-gamma*T)*R0
    return R - math.exp(-gamma*T)*R0

print("Material action lower bounds:")
for R in [10, 100, 1000]:
    print(R, action_lower(R))

# Worldsheet constants
c0 = 0.2
Wmeasure = 5.0
ell = 0.25
Ctrace = 8.0
CM = 3.0

def resolved_trace_lower(R):
    # If filtered part carries at least c0 R / 2 in L1:
    return (0.5*c0*R)**2 / Wmeasure

def tube_energy_lower(R):
    # I_trace <= Ctrace ell^-2 E_tube
    # hence E_tube >= ell^2 I_trace / Ctrace
    return ell**2 * resolved_trace_lower(R) / Ctrace

def morrey_time_upper(R):
    return Tstar * CM * (R + ell)

print("\nResolved branch R^2 lower vs Morrey R upper:")
for R in [10, 100, 1000, 10000]:
    lo = tube_energy_lower(R)
    hi = morrey_time_upper(R)
    print(
        f"R={R:5d} lower={lo:.8g} upper={hi:.8g} "
        f"ratio={lo/hi:.8g}"
    )

# Increment branch quartic trace lower:
def increment_quartic_lower(R):
    # L1 >= c0 R/2, Holder: int M^4 >= L1^4 / |W|^3
    return (0.5*c0*R)**4 / (Wmeasure**3)

print("\nIncrement worldsheet quartic trace growth:")
for R in [10, 100, 1000]:
    print(R, increment_quartic_lower(R))

# Solve schematic quadratic-vs-linear ceiling:
# c_tr ell^2 R^2 <= C_M T R
c_tr = (0.5*c0)**2 / (Wmeasure*Ctrace)
R_ceiling = (CM*Tstar)/(c_tr*ell**2)
print("\nSchematic tame radius ceiling =", R_ceiling)

print(
    "\nConclusion: bounded-time material return gives an R^2 resolved "
    "transport cost (or R^4 increment trace), while native Morrey gives only O(R)."
)
