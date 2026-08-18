# DCRP59 symbolic / constant checks

import sympy as sp

cg, RHO, Z = sp.symbols("cg RHO Z", positive=True, real=True)
rna, rtr = sp.symbols("rna rtr", real=True)

total_trace = 3 * cg * RHO
half_total = sp.Rational(3, 2) * cg * RHO

print("Total signed residual trace budget =", total_trace)
print("At least one channel >=", half_total)

# rho >= Z/2
print(
    "Channel lower bound using rho>=Z/2 =",
    sp.simplify(half_total.subs(RHO, Z/2))
)

# Non-affine trace has factor 2:
na_work = sp.simplify(
    (half_total / 2).subs(RHO, Z/2)
)
print("Non-affine work lower bound =", na_work)

# Turnover trace = 2 * weighted inward signed flux,
# so divide channel lower bound by 2.
turnover = sp.simplify(
    (half_total / 2).subs(RHO, Z/2)
)
print("Smoothed inward-turnover lower bound =", turnover)

# Norm backup constants
Gnorm = sp.sqrt(3)/2 * cg * Z
channel_norm = sp.simplify(Gnorm/2)
na_abs = sp.simplify(channel_norm/2)

print("\nNorm total gap =", Gnorm)
print("At least one residual norm >=", channel_norm)
print("Weighted |E||Omega|^2 lower bound on na branch >=", na_abs)
