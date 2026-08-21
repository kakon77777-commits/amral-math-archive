# DCRP55 symbolic checks
# 1) full angular transparency iff dyadic moment is isotropic
# 2) planar inner + isotropic compensation lower bound
# 3) normal-axis cancellation formula

import sympy as sp

l1, l2, c = sp.symbols("l1 l2 c", nonnegative=True, real=True)
N, T, Zin = sp.symbols("N T Zin", nonnegative=True, real=True)

# Inner basis: planar eigenvalues l1,l2, normal 0.
Min = sp.diag(l1, l2, 0)
Mout = c * sp.eye(3) - Min

print("Outer eigenvalues for full isotropization:")
print([sp.simplify(Mout[i, i]) for i in range(3)])

print("\nPSD requires c >= max(l1,l2).")
print("Inner trace =", sp.trace(Min))
print("If l1>=l2, l1 >= trace/2.")

# Normal-axis angular coefficient A_M(n)=3 nMn-tr M.
Ain_normal = -sp.trace(Min)
Aout_normal = sp.simplify(3*N - (N + T))

print("\nInner normal coefficient =", Ain_normal)
print("Outer normal coefficient =", Aout_normal)

eqN = sp.solve(sp.Eq(Aout_normal, Zin), N)[0]
print("N required for normal cancellation =", eqN)

# minimal isotropic planar inner
Z = sp.symbols("Z", positive=True, real=True)
Min_iso = sp.diag(Z/2, Z/2, 0)
Mout_min = Z/2 * sp.eye(3) - Min_iso

print("\nMinimal isotropic planar outer compensator:")
sp.pprint(Mout_min)

# Same-parent physical enstrophy-time scaling.
lam, alpha = sp.symbols("lam alpha", positive=True, real=True)
mu = lam**(1-alpha)

enstrophy_ratio = sp.simplify(mu**2 / lam)
action_ratio = sp.simplify((mu**2 / lam) * (lam**2 / mu))

print("\nPhysical enstrophy ratio =", enstrophy_ratio)
print("Enstrophy-time action ratio =", action_ratio)
