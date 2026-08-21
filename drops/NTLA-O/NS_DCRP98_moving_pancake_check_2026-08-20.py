# DCRP98 moving-pancake / reverse-phase sanity checks

import numpy as np
import math

gamma = 0.45
cgam = 2 - 3*gamma
m = cgam/2
S0 = 2*np.pi

print("c_gamma =", cgam)
print("mean pancake amplitude m =", m)

# Moving pancake contraction with plane-locked Q.
n = np.array([0.0,0.0,1.0])
P = np.eye(3)-np.outer(n,n)
Q = np.diag([0.7,0.3,0.0])
tau = np.trace(Q)

def A_pan(a, n, nprime):
    P = np.eye(3)-np.outer(n,n)
    return a*(P-2*np.outer(n,n)) - (
        np.outer(nprime,n)+np.outer(n,nprime)
    )

for a in [0.4,0.1,-0.2]:
    nprime = np.array([0.2,-0.1,0.0])
    A = A_pan(a,n,nprime)
    Pi = -np.sum(A*Q)
    print("a =", a, "Pi =", Pi, "expected =", -a*tau)

# A periodic reverse-pancake example with positive mean.
# a(s)=m + A cos s, A>m gives negative phases.
amp = 0.6
grid = np.linspace(0,S0,20001)
a = m + amp*np.cos(grid)

mean_num = np.trapz(a,grid)/S0
neg_action = np.trapz(np.maximum(-a,0),grid)
variance_action = np.trapz((a-m)**2,grid)
reproduction = 6*np.trapz(a*a,grid)

print("\nreverse-pancake example:")
print("mean a =", mean_num)
print("min a =", np.min(a))
print("negative action =", neg_action)
print("variance action =", variance_action)
print("reproduction action =", reproduction)
print("Jensen minimum =", 6*m*m*S0)

# TV lower bound for periodic scalar.
tv = np.sum(np.abs(np.diff(a)))
print("discrete TV(a) =", tv)
print("2(max-min) =", 2*(np.max(a)-np.min(a)))

# Window forward work on negative phase with tau=1.
mask = a < 0
W = np.trapz((-a[mask])*tau, grid[mask]) if np.any(mask) else 0
print("modeled forward work on negative phase =", W)

# Decomposition: forward work can be reverse scalar + shape + non-affine.
a0 = 0.15
Sshape = np.diag([-0.5,0.5,0.0])
E = np.diag([-0.4,0.2,0.2])
A0 = A_pan(a0,n,np.zeros(3))
Stotal = A0 + Sshape + E
Pi_total = -np.sum(Stotal*Q)
parts = (
    -a0*tau,
    -np.sum(Sshape*Q),
    -np.sum(E*Q),
)
print("\nwork decomposition:")
print("parts =", parts)
print("sum parts =", sum(parts))
print("direct total =", Pi_total)

# Show fixed A* gap can be nonzero purely from scalar modulation
# while remaining in moving pancake family.
Astar = A_pan(m,n,np.zeros(3))
for aa in [m, -0.2, 0.8]:
    Acur = A_pan(aa,n,np.zeros(3))
    gap = np.max(np.abs(np.linalg.eigvalsh(Acur-Astar)))
    print("a =", aa, "frozen-gap =", gap, "zero-shape family = True")

print(
    "\nConclusion: forward work does not exclude the full moving-pancake "
    "manifold; it can use a temporary a<0 phase.  The correct compiler is "
    "carrier unlock/state escape or reconvergence to the established X/N/T "
    "rank-two closure."
)
