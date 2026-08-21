# DCRP56 symbolic checks

import sympy as sp

q11, q22, q12 = sp.symbols("q11 q22 q12", real=True)

# fixed-plane stream scalar q:
# Omega=(q_y,-q_x,0)
# divdiv(Omega tensor Omega)=2(q_xy^2-q_xx q_yy)
expr = 2 * (q12**2 - q11*q22)
print("divdiv fixed-plane dyadic =", expr)
print("= -2 det Hess_h q =", -2*(q11*q22-q12**2))

Z = sp.symbols("Z", positive=True, real=True)
l1, l2, c = sp.symbols("l1 l2 c", nonnegative=True, real=True)

Min = sp.diag(l1, l2, 0)
Mout = c*sp.eye(3)-Min
Mtot = sp.simplify(Min+Mout)

print("\nFull compensation total covariance:")
sp.pprint(Mtot)

print("\nOuter trace:", sp.simplify(sp.trace(Mout)))
print("If c >= (l1+l2)/2, outer trace >= Z/2 at trace Z.")

# Physical same-parent enstrophy-time scaling.
lam, alpha = sp.symbols("lam alpha", positive=True, real=True)
mu = lam**(1-alpha)

snapshot = sp.simplify(mu**2/lam)
time_scale = sp.simplify(lam**2/mu)
action = sp.simplify(snapshot*time_scale)

print("\nSnapshot enstrophy ratio =", snapshot)
print("Root time ratio =", time_scale)
print("Enstrophy-time action ratio =", action)
