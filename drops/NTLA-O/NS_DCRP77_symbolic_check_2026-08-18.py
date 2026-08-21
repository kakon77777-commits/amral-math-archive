# DCRP77 symbolic checks

import sympy as sp

alpha, gamma = sp.symbols("alpha gamma", positive=True, real=True)
kappa = 3-2*alpha
relation = {gamma: 1/(alpha+1)}

lamstar = (2-3*gamma)/2

print("gamma - lambda_* - gamma*kappa/2:")
print(
    sp.simplify(
        (gamma-lamstar-gamma*kappa/2).subs(relation)
    )
)

# Packet mean identity coefficient check.
bar, var, tilt2, ebar, mbar = sp.symbols(
    "bar var tilt2 ebar mbar",
    real=True,
)

cgamma = 2-3*gamma

# L'/Z:
# D_s lambda = 2 tilt2 - ebar - lambda - m/6 pointwise
# plus z growth (-2+2lambda) and volume 3gamma.
L_over_Z = (
    2*tilt2
    - ebar
    - mbar/6
    + (3*gamma-3)*bar
    + 2*(var+bar**2)
)

Z_rate = 2*bar-cgamma

bar_prime = sp.expand(
    L_over_Z-bar*Z_rate
)

target = (
    2*tilt2
    +2*var
    -ebar
    -mbar/6
    -bar
)

print("\nPacket mean identity difference:")
print(sp.simplify(bar_prime-target))

print(
    "\nPure-selector covariance identity: "
    "Delta = E[(w-1)(lambda-mean)] "
    "<= ||w-1||_2 sqrt(Var(lambda))."
)

print(
    "First-crossing gap = gamma-lambda_* "
    "= gamma*kappa/2."
)
