"""
Symbolic verification for NS_X72 Round 49.
Checks the Golden source coefficients after imposing lambda^2 - 3 lambda + 1 = 0.
"""
import sympy as sp

lam = sp.symbols("lam", positive=True, real=True)

c1 = -(lam - 1) * (lam**2 - 3*lam + 4) / (lam**2 + 4)
c2 = -(lam - 1) * (4*lam**2 - 3*lam + 1) / (lam * (4*lam**2 + 1))
cnu = -2 * (lam**2 - 3*lam + 1)

roots = sp.solve(sp.Eq(lam**2 - 3*lam + 1, 0), lam)

for root in roots:
    sigma = sp.simplify(c1.subs(lam, root))
    assert sp.simplify(c2.subs(lam, root) - sigma) == 0
    assert sp.simplify(cnu.subs(lam, root)) == 0
    assert sp.simplify(sigma**2 - sp.Rational(1, 5)) == 0
    assert sp.simplify(
        sigma + (root - 1) / (root + 1)
    ) == 0
    print("lambda =", root)
    print("sigma  =", sigma)
    print("sigma^2=", sp.simplify(sigma**2))
    print()

print("All Round 49 Golden source-lock symbolic checks passed.")
