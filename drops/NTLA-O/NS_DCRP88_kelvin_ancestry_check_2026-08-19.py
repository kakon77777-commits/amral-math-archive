# DCRP88 Kelvin multiplier / ancestry-depth sanity checks

import math

def rho_gamma(gamma: float, S0: float) -> float:
    return math.exp(-(1.0 - 2.0*gamma)*S0)

def ancestry_depth(rho: float, gamma_star: float, c_gamma_atom: float) -> int:
    assert 0.0 < rho < 1.0
    assert gamma_star >= c_gamma_atom > 0.0
    return 1 + math.floor(
        math.log(gamma_star / c_gamma_atom) /
        math.log(1.0 / rho)
    )

# Sample strict Type-II parameters.
gamma = 0.45
S0 = 1.3
rho = rho_gamma(gamma, S0)

print("rho_Gamma =", rho)
print("0 < rho_Gamma < 1:", 0.0 < rho < 1.0)

Gamma_star = 7.0
c_atom = 0.25
Nstar = ancestry_depth(rho, Gamma_star, c_atom)

print("N_* =", Nstar)
print(
    "At N_*, backward lower circulation:",
    (rho**(-Nstar))*c_atom,
)
print("Compact ceiling Gamma_* =", Gamma_star)

# Alpha / Lambda identity.
alpha = 1.25
gamma2 = 1.0/(alpha+1.0)
Lambda = 2.0
S02 = (alpha+1.0)*math.log(Lambda)
rho_time = rho_gamma(gamma2, S02)
rho_scale = Lambda**(-(alpha-1.0))

print("\nalpha-Lambda identity:")
print("gamma =", gamma2)
print("rho from time law =", rho_time)
print("rho from Lambda law =", rho_scale)
print("match =", abs(rho_time-rho_scale) < 1e-12)

# Robust approximate Kelvin recursion:
# |Gamma_0 - rho^n Gamma_-n| <= eta (1-rho^n)/(1-rho)
eta = 0.25 * (1.0-rho) * c_atom  # safely below half threshold
for n in [1, 3, 5, 10]:
    lower = (c_atom - eta/(1.0-rho)) * rho**(-n)
    print(f"n={n}: robust backward lower bound >= {lower:.8g}")

print(
    "\nConclusion: normalized circulation ancestry depth is controlled "
    "by rho_Gamma and compact circulation ceiling, not by physical scale weight r_k/r_0."
)
