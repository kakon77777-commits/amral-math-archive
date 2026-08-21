# DCRP102 adjoint / half-space / pair-copula checks
import numpy as np

def frob(A, B):
    return float(np.sum(A * B))

def L(S, Phi):
    return Phi @ S + S @ Phi - (2.0 / 3.0) * frob(S, Phi) * np.eye(3)

G = np.diag([1.0, -1.0, 0.0])
Phi0 = np.diag([1.0, 1.0, -2.0])

print("tr G =", np.trace(G))
print("tr Phi0 =", np.trace(Phi0))
print("G:Phi0 =", frob(G, Phi0))

for sign in [1.0, -1.0]:
    S = sign * G
    LS = L(S, Phi0)
    print("\nsign =", sign)
    print("L_S(Phi0)=\n", LS)
    print("G:L_S(Phi0)=", frob(G, LS))

# Numerical self-adjointness of L_S on Sym_0(3)
rng = np.random.default_rng(12)

def sym0(M):
    A = 0.5 * (M + M.T)
    return A - np.trace(A) / 3.0 * np.eye(3)

errs = []
for _ in range(20):
    S = sym0(rng.normal(size=(3, 3)))
    E = sym0(rng.normal(size=(3, 3)))
    P = sym0(rng.normal(size=(3, 3)))
    lhs = frob(P, L(S, E))
    rhs = frob(E, L(S, P))
    errs.append(abs(lhs - rhs))

print("\nmax L_S self-adjointness error =", max(errs))

# Pair-increment bilinear decomposition
errs = []
for _ in range(20):
    Sx = sym0(rng.normal(size=(3, 3)))
    Sy = sym0(rng.normal(size=(3, 3)))
    Px = sym0(rng.normal(size=(3, 3)))
    Py = sym0(rng.normal(size=(3, 3)))
    lhs = L(Sx, Px) - L(Sy, Py)
    rhs = L(Sx, Px - Py) + L(Sx - Sy, Py)
    errs.append(np.max(np.abs(lhs - rhs)))

print("max pair bilinear decomposition error =", max(errs))

# Positive pair-occupancy lower bound example
cTR = 0.2
MG = 1.5
MPhi = 2.0
Mq = 1.2
M = MG * MPhi * Mq

occupancy = cTR / (2 * M - cTR)
eta_theta = cTR / (2 * M)

print("\nM product =", M)
print("positive occupancy lower bound =", occupancy)
print("angular cosine lower bound after sign split =", eta_theta)

print(
    "\nConclusion: the local adjoint strain operator is self-adjoint but "
    "does not preserve a detector half-space; fixed positive TR transfer "
    "forces oriented angular pair-copula occupancy rather than pointwise "
    "adjoint sign preservation."
)
