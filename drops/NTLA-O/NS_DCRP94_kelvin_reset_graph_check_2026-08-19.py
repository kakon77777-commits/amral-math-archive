# DCRP94 finite-state Kelvin reset graph checks

import math

rho = 0.82
c_gamma = 0.3
M = 7

delta_star = (1-rho)*c_gamma/M
print("Uniform exact-cycle reset atom delta_* =", delta_star)

# Exact cycle recurrence:
# Gamma_{n+q}=rho^q Gamma_n + sum rho^(q-1-j) delta_j
# If Gamma_{n+q}=Gamma_n=Gamma, cumulative absolute reset >= (1-rho^q)|Gamma|.
for q in range(1, M+1):
    lower = (1-rho**q)*c_gamma
    one_event = lower/q
    print(
        f"q={q}: cumulative reset >= {lower:.10g}, "
        f"one event >= {one_event:.10g}"
    )

print(
    "Universal coarser one-event lower bound:",
    (1-rho)*c_gamma/M
)

# Robust state-cell version.
eps_cyc = 0.5*(1-rho)*c_gamma
robust_cumulative = (1-rho)*c_gamma - eps_cyc
robust_atom = robust_cumulative/M
print("\nRobust half-gap cumulative reset =", robust_cumulative)
print("Robust reset atom =", robust_atom)

# Constant-circulation reset conveyor.
Gamma_star = 0.6
delta_const = (1-rho)*Gamma_star
Gamma = Gamma_star
print("\nConstant-circulation reset conveyor:")
for n in range(8):
    print(n, Gamma)
    Gamma = rho*Gamma + delta_const
print("delta_const =", delta_const)

# Physical homogeneity.
alpha = 1.25
p_gamma = 1-alpha
qscale = 0.5
print("\nPhysical reset amplitude for uniform normalized delta:")
for n in [0, 5, 10, 20]:
    ell = qscale**n
    phys = ell**p_gamma * delta_star
    print(
        f"n={n}, ell={ell:.8g}, physical reset ~ {phys:.10g}"
    )

# Block-density lower bound.
for Mtest in [3, 7, 12]:
    print(
        f"M={Mtest}: replacement/reset union density >= {1/(Mtest+1):.8g}"
    )

# Helicity homogeneity audit.
for alpha in [1.05, 1.25, 1.45]:
    pH = 2-2*alpha
    print(
        f"alpha={alpha}: helicity homogeneity p_H={pH:.6g}"
    )

print(
    "\nConclusion: finite-state recurrence forces a scale-uniform normalized "
    "Kelvin reset or state replacement.  The reset has p=0 in generation "
    "variables and negative physical circulation homogeneity, but a constant "
    "reset conveyor shows that a finite total reset capacity is still needed."
)
