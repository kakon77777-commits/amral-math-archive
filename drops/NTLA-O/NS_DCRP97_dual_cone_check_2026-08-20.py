# DCRP97 dual-lock PSD cone / pancake-gap checks
import numpy as np
import math

def frob(A):
    return np.sqrt(np.sum(A*A))

def opnorm(A):
    return np.max(np.abs(np.linalg.eigvalsh(A)))

# Canonical pancake
gamma = 0.45
cgam = 2 - 3*gamma
n = np.array([0.0,0.0,1.0])
I = np.eye(3)
P = I - np.outer(n,n)
Astar = 0.5*cgam*I - 1.5*cgam*np.outer(n,n)

print("c_gamma =", cgam)
print("Astar =\n", Astar)
print("trace Astar =", np.trace(Astar))

# Plane-supported PSD covariances: forward SGS work is strictly negative.
for Q in [
    np.diag([0.8,0.2,0.0]),
    np.diag([0.5,0.5,0.0]),
    np.array([[0.6,0.2,0.0],[0.2,0.4,0.0],[0.0,0.0,0.0]])
]:
    eig = np.linalg.eigvalsh(Q)
    tau = np.trace(Q)
    Pi = -np.sum(Astar*Q)
    print("\nQ eig =", eig, "trace =", tau, "canonical Pi =", Pi)
    print("expected =", -0.5*cgam*tau)

# Scope-repair identity for arbitrary PSD Q.
rng = np.random.default_rng(7)
for k in range(5):
    X = rng.normal(size=(3,3))
    Q = X @ X.T
    M = rng.normal(size=(3,3))
    Delta = 0.5*(M+M.T)
    S = Astar + Delta
    tau = np.trace(Q)
    r_n = n @ Q @ n
    lhs = -np.sum(S*Q)
    rhs = -0.5*cgam*tau + 1.5*cgam*r_n - np.sum(Delta*Q)
    print("identity error =", abs(lhs-rhs))

# Locked rank-two parameterization.
tau = 1.0
b0 = 0.2
for theta in np.linspace(0, np.pi, 5):
    v = np.array([np.cos(theta), np.sin(theta), 0.0])
    Qv = b0*P + (tau-2*b0)*np.outer(v,v)
    print("extreme eig =", np.linalg.eigvalsh(Qv), "trace =", np.trace(Qv))

# Explicit dual-lock example away from pancake equality.
Q = np.diag([0.8,0.2,0.0])
G = np.diag([1.0,-1.0,0.0])
S = np.diag([-1.0,1.2,-0.2])
Lgamma = np.sum(G*Q)
Lenergy = -np.sum(S*Q)
print("\nAway-from-equality example:")
print("Kelvin detector =", Lgamma)
print("forward SGS work =", Lenergy)

# Quantitative equality-gap check.
Delta = S - Astar
theta_Q = (n @ Q @ n)/np.trace(Q)
lower_lhs = 1.5*cgam*theta_Q + opnorm(Delta)
e_star = 0.3
required_rhs = 0.5*cgam + e_star/np.trace(Q)
print("\nGap diagnostic for sample:")
print("theta_Q =", theta_Q)
print("||Delta S||op =", opnorm(Delta))
print("gap LHS =", lower_lhs)
print("required RHS for c_E*=0.3 =", required_rhs)

# Exact two-half-plane disk feasibility check by grid and Farkas support criterion.
# Use plane trace-free matrices identified by orthonormal basis E1,E2.
E1 = np.diag([1,-1,0])/np.sqrt(2)
E2 = np.array([[0,1,0],[1,0,0],[0,0,0]])/np.sqrt(2)

def coords(T):
    return np.array([np.sum(T*E1), np.sum(T*E2)])

def plane_tf(T):
    # plane block trace-free part
    Tpp = P @ T @ P
    trp = np.trace(Tpp)
    return Tpp - 0.5*trp*P

Rdisk = np.sqrt(2)*(tau/2-b0)
Gtf = plane_tf(G)
H = -S
Htf = plane_tf(H)
u = coords(Gtf)
vvec = coords(Htf)

aG = 0.1 + tau/2*(n @ G @ n)
aE = 0.1 + tau/2*(n @ H @ n)

# grid feasibility
feasible = False
best = None
for rr in np.linspace(0,Rdisk,201):
    for ang in np.linspace(0,2*np.pi,721):
        d = rr*np.array([np.cos(ang),np.sin(ang)])
        if u@d >= aG-1e-9 and vvec@d >= aE-1e-9:
            feasible = True
            best = d
            break
    if feasible:
        break

# Farkas criterion
min_margin = float("inf")
worst_lam = None
for lam in np.linspace(0,1,2001):
    lhs = Rdisk*np.linalg.norm(lam*u+(1-lam)*vvec)
    rhs = lam*aG+(1-lam)*aE
    margin = lhs-rhs
    if margin < min_margin:
        min_margin = margin
        worst_lam = lam

print("\nDisk feasibility:")
print("grid feasible =", feasible)
print("Farkas min margin =", min_margin, "at lambda =", worst_lam)
print("criterion predicts feasible =", min_margin >= -1e-6)

print(
    "\nConclusion: the canonical pancake empties the forward dual-lock cone "
    "for every plane-supported PSD increment covariance.  General dual lock "
    "is possible only after a quantitative carrier-unlock or non-affine strain gap."
)
