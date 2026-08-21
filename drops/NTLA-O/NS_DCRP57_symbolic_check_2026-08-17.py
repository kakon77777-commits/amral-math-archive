# DCRP57 symbolic checks
# 1) isotropic covariance residual norm split
# 2) twisting-cylinder vertical-vorticity derivative

import sympy as sp

rho, rhop, cg = sp.symbols("rho rhop cg", real=True)
a1, a2, a3, a12, a13, a23 = sp.symbols(
    "a1 a2 a3 a12 a13 a23", real=True
)

A = sp.Matrix([
    [a1, a12, a13],
    [a12, a2, a23],
    [a13, a23, a3],
])

# impose trace-free with a3=-(a1+a2)
A = A.subs(a3, -(a1+a2))

R = (rhop + cg*rho)*sp.eye(3) - 2*rho*A

Rnorm2 = sp.expand(sum(R[i,j]**2 for i in range(3) for j in range(3)))
Anorm2 = sp.expand(sum(A[i,j]**2 for i in range(3) for j in range(3)))

expected = sp.expand(
    3*(rhop+cg*rho)**2
    + 4*rho**2*Anorm2
)

print("Residual norm identity difference:")
print(sp.simplify(Rnorm2-expected))

# Twisting-cylinder derivative.
fr, frr, frz, beta, betaz, thz, t = sp.symbols(
    "fr frr frz beta betaz thz t", real=True
)

# Coefficients in eta and xi basis:
eta_coeff = frz - beta*thz + thz*t*frr
xi_coeff = -(thz*fr + betaz)

print("\nVertical vorticity derivative coefficients:")
print("eta:", eta_coeff)
print("xi:", xi_coeff)
print("linear t coefficient:", sp.diff(eta_coeff, t))
