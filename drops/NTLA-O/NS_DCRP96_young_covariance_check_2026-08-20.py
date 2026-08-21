# DCRP96 Young-profile / covariance algebra checks
import numpy as np

e1 = np.array([1.0, 0.0, 0.0])
e2 = np.array([0.0, 1.0, 0.0])
e3 = np.array([0.0, 0.0, 1.0])

A = np.diag([1.0, -1.0, 0.0])
print("trace(A) =", np.trace(A))

# Centered sign-symmetric Young measure 1/2 (delta_e1 + delta_-e1)
m = 0.5*e1 + 0.5*(-e1)
Q = 0.5*np.outer(e1,e1) + 0.5*np.outer(-e1,-e1) - np.outer(m,m)
print("barycenter =", m)
print("Q symmetric example =\n", Q)
print("A:Q =", np.sum(A*Q))

# Isotropic sign-symmetric measure on ±e1, ±e2, ±e3
Qiso = (
    np.outer(e1,e1)
    + np.outer(e2,e2)
    + np.outer(e3,e3)
) / 3.0
print("\nQ isotropic =\n", Qiso)
print("A:Qiso =", np.sum(A*Qiso))

# Deviatoric projection identity
Q0 = Q - np.trace(Q)/3.0*np.eye(3)
print("\nA:Q0 =", np.sum(A*Q0))
print("A:Q == A:Q0:", np.allclose(np.sum(A*Q), np.sum(A*Q0)))

# Dual lock example: same centered symmetric Q supports positive circulation
# detector and positive SGS work.
S = np.diag([-1.0, 1.0, 0.0])  # trace free incompressible strain
L_gamma = np.sum(A*Q0)
L_energy = -np.sum(S*Q0)
print("\nDual lock rank-one example:")
print("L_gamma =", L_gamma)
print("L_energy =", L_energy)

# Rank-two PSD example with plane normal e3
Q2 = np.diag([0.7, 0.3, 0.0])
Q20 = Q2 - np.trace(Q2)/3.0*np.eye(3)
print("\nRank-two Q2 eigenvalues =", np.linalg.eigvalsh(Q2))
print("A:Q2^0 =", np.sum(A*Q20))
print("-S:Q2^0 =", -np.sum(S*Q20))

# Pressure-compatible / isotropic sanity: isotropic covariance has zero
# pairing against any trace-free detector.
rng = np.random.default_rng(3)
for k in range(5):
    M = rng.normal(size=(3,3))
    T = 0.5*(M+M.T)
    T -= np.trace(T)/3*np.eye(3)
    val = np.sum(T*Qiso)
    print("random trace-free detector : Qiso =", val)

print(
    "\nConclusion: sign symmetry/barycenter zero does not kill quadratic SGS "
    "circulation flux. The correct order parameter is the oriented deviatoric "
    "second moment; isotropic and pressure-compatible covariances are silent."
)
