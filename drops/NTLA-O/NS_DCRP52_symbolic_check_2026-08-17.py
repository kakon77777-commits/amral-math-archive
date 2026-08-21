# DCRP52 symbolic verification
# Checks the explicit gradient-hyperboloid null-curve formulas and
# the X72 vorticity-stress algebraic invariant.

import sympy as sp

C = sp.symbols("C", positive=True, real=True)
eta = sp.symbols("eta", real=True)
theta_p = sp.symbols("theta_p", real=True)

beta = sp.Rational(3, 2)

rho = sp.sqrt(C) * sp.cosh(eta)
r = sp.sqrt(C / beta) * sp.sinh(eta)

# g' wave norm after separating the angular derivative theta'
wave_norm_over_C = sp.factor(
    (
        sp.diff(rho, eta) ** 2
        + rho ** 2 * theta_p ** 2
        - sp.diff(r, eta) ** 2
    ) / C
)

target_theta_sq = sp.simplify(
    sp.Rational(2, 3) - sp.tanh(eta) ** 2
)

print("g' wave norm / C:")
print(wave_norm_over_C)

print("\nNull condition theta'^2:")
print(target_theta_sq)

print("\nSubstitution check:")
print(
    sp.simplify(
        wave_norm_over_C.subs(theta_p ** 2, target_theta_sq)
    )
)

# X72 vorticity-stress invariant.
m = sp.symbols("m", positive=True, real=True)
W = sp.diag(
    sp.Rational(2, 3) * m,
    -sp.Rational(1, 3) * m,
    -sp.Rational(1, 3) * m,
)

Wnorm2 = sp.simplify(sp.trace(W * W))
Wdet = sp.simplify(W.det())

print("\n|W|^2 =", Wnorm2)
print("det W =", Wdet)
print(
    "54(det W)^2 - |W|^6 =",
    sp.simplify(54 * Wdet ** 2 - Wnorm2 ** 3),
)

# Null-Hessian direction longitudinal stress coordinate.
t = sp.symbols("t", real=True)
# normalized ell_z = 1, |ell_h|^2=1
# Omega dot ell = sqrt(m)*sqrt(1-t^2)
ell_W_ell = sp.simplify(
    m * (1 - t ** 2)
    - sp.Rational(1, 3) * m * 2
)
print("\nell^T W ell =", sp.factor(ell_W_ell))
