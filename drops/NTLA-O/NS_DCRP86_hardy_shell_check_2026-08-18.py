# DCRP86 discrete Hardy / shell-debt verification

from math import isclose

lam = 0.5
r0 = 1.0
K = 8

r = [r0 * (lam**k) for k in range(K + 2)]

# Critical model F(r)=c r^2
c = 0.37
F = [c * rk**2 for rk in r]
A = [F[k] - F[k+1] for k in range(K+1)]
C3 = [F[k] / r[k]**2 for k in range(K+1)]

lhs_core = sum(C3)
rhs_identity = 0.0
for j in range(K+1):
    H_j = sum(1.0 / r[k]**2 for k in range(j+1))
    rhs_identity += A[j] * H_j
rhs_identity += F[K+1] * sum(1.0 / r[k]**2 for k in range(K+1))

print("Finite Hardy identity:")
print("core sum =", lhs_core)
print("shell+tail identity =", rhs_identity)
print("match =", isclose(lhs_core, rhs_identity, rel_tol=1e-12, abs_tol=1e-12))

annular_normalized = sum(A[j] / r[j]**2 for j in range(K+1))
lower_from_hardy = (1-lam**2) * lhs_core - F[K+1] / r[K]**2

print("\nNormalized disjoint-shell sum =", annular_normalized)
print("Hardy lower bound =", lower_from_hardy)
print("bound valid =", annular_normalized + 1e-12 >= lower_from_hardy)

print("\nCritical model checks:")
print("C3 per scale:", C3[:4], "...")
print("shell normalized per scale:",
      [A[j]/r[j]**2 for j in range(4)], "...")
print("physical shell total =", sum(A))
print("expected telescoping =", F[0]-F[K+1])

# Geometric Hardy weights
print("\nGeometric Hardy ratios H_j * r_j^2:")
for j in range(5):
    H_j = sum(1.0 / r[k]**2 for k in range(j+1))
    ratio = H_j * r[j]**2
    print(j, ratio)
print("Upper limiting constant =", 1/(1-lam**2))

# Generic symbolic-style finite-chain implication
eps3 = 0.02
M = 5.0
for Ktest in [10, 100, 1000]:
    debt_lb = (1-lam**2)*eps3*(Ktest+1) - lam**2*M
    print(f"K={Ktest}: disjoint shell debt lower bound >= {debt_lb:.6g}")

print(
    "\nInterpretation: Hardy annularization removes overlap, "
    "but F(r)=c r^2 shows normalized shell debt can remain O(1) "
    "at every scale while physical L3 mass is finite."
)
