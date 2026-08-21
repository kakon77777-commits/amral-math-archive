# DCRP51 symbolic algebra verification
# Verifies the adapted-Hessian Bochner factorization used in Theorem D51.1–D51.8.

import sympy as sp

t, beta, F, E = sp.symbols("t beta F E", real=True)

H = sp.Matrix([
    [t**2 * F, t * E, t * F],
    [t * E, (1 - t**2) * F, E],
    [t * F, E, F],
])

G = sp.diag(1, 1, -1)
M = sp.diag(1, 1, -beta)

Q = sp.factor(sp.trace(G * H * M * H))

expected = sp.factor(
    (E**2 + F**2 * (t**2 - 1))
    * (2 * t**2 - (beta + 1))
)

print("Bochner factorization:")
print(Q)
print("Matches expected:", sp.simplify(Q - expected) == 0)

# Rank-one factorization on the nonlinear branch:
s = sp.symbols("s", real=True)
ell = sp.Matrix([t, s, 1])
H_rank1 = F * (ell * ell.T)

# Under s^2 = 1 - t^2 and E = F s.
substituted = H.subs(E, F * s)
difference = substituted - H_rank1

print("\nH - F ell ell^T before imposing s^2=1-t^2:")
sp.pprint(difference)

# Wave-null direction:
wave_norm = sp.expand((ell.T * G * ell)[0])
print("\nWave norm ell^T G ell =", wave_norm)
print("Under s^2=1-t^2 =>", sp.simplify(wave_norm.subs(s**2, 1-t**2)))

# Eikonal-normal orthogonality in adapted frame:
rho, r = sp.symbols("rho r", nonzero=True, real=True)
g = sp.Matrix([rho, 0, r])
orth = sp.expand((ell.T * M * g)[0])
print("\nell^T M grad u =", orth)
print("Under t=beta*r/rho =>", sp.simplify(orth.subs(t, beta*r/rho)))
