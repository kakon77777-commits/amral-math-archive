# DCRP103 five-ray / Riesz-loaded adjoint eigen-lock checks
import sympy as sp
import numpy as np

# ------------------------------------------------------------------
# Symbolic simple-strain diagonal block.
# ------------------------------------------------------------------
s1, s2 = sp.symbols("s1 s2", real=True)
s3 = -s1 - s2
p1, p2 = sp.symbols("p1 p2", real=True)
p3 = -p1 - p2

a = s1*p1 + s2*p2 + s3*p3

L1 = 2*s1*p1 - sp.Rational(2,3)*a
L2 = 2*s2*p2 - sp.Rational(2,3)*a

M = sp.Matrix([
    [sp.diff(L1,p1), sp.diff(L1,p2)],
    [sp.diff(L2,p1), sp.diff(L2,p2)],
])

lam = sp.symbols("lam", real=True)
char = sp.factor(M.charpoly(lam).as_expr())
print("diagonal-block matrix =")
print(M)
print("diagonal-block charpoly =", char)

Ssq = sp.expand(s1**2 + s2**2 + s3**2)
d2 = sp.simplify(sp.Rational(2,3)*Ssq)
print("d_S^2 =", sp.factor(d2))

# ------------------------------------------------------------------
# Check L_S(S)=2C and L_S(C)=|S|^2 S/3 numerically.
# ------------------------------------------------------------------
def frob(A,B):
    return float(np.sum(A*B))

def L(S,Phi):
    return Phi@S + S@Phi - (2.0/3.0)*frob(S,Phi)*np.eye(3)

def C0(S):
    return S@S - np.trace(S@S)/3.0*np.eye(3)

rng = np.random.default_rng(19)
for _ in range(5):
    vals = rng.normal(size=3)
    vals -= vals.mean()
    S = np.diag(vals)
    C = C0(S)
    e1 = np.max(np.abs(L(S,S)-2*C))
    e2 = np.max(np.abs(L(S,C)-(frob(S,S)/3.0)*S))
    print("operator identity errors =", e1, e2)

# ------------------------------------------------------------------
# Five local eigenvalues.
# ------------------------------------------------------------------
S = np.diag([1.3, -0.2, -1.1])
normS = np.sqrt(frob(S,S))
d = np.sqrt(2.0/3.0)*normS
evals_pred = [-1.3, 0.2, 1.1, d, -d]
print("\nfive-ray predicted spectrum =", evals_pred)

# Build 5x5 matrix numerically in an orthonormal Sym_0 basis.
E12 = np.array([[0,1,0],[1,0,0],[0,0,0]],float)/np.sqrt(2)
E13 = np.array([[0,0,1],[0,0,0],[1,0,0]],float)/np.sqrt(2)
E23 = np.array([[0,0,0],[0,0,1],[0,1,0]],float)/np.sqrt(2)
D1 = np.diag([1,-1,0])/np.sqrt(2)
D2 = np.diag([1,1,-2])/np.sqrt(6)
basis = [E23,E13,E12,D1,D2]
A = np.array([[frob(Bi,L(S,Bj)) for Bj in basis] for Bi in basis])
evals_num = np.linalg.eigvalsh(A)
print("5x5 numerical spectrum =", evals_num)

# ------------------------------------------------------------------
# Verify Riesz-loaded diagonal formula.
# ------------------------------------------------------------------
beta = 0.7
r = 0.4
C = C0(S)
d2_num = (2.0/3.0)*frob(S,S)
PhiD = 2*r/(beta**2-d2_num)*(beta*S+2*C)
res = L(S,PhiD) + 2*r*S - beta*PhiD
print("\nRiesz-loaded diagonal residual =", np.max(np.abs(res)))

# ------------------------------------------------------------------
# Verify single-shear normal form.
# active E13 -> beta=s1+s3=-s2 = 0.2 for this S.
# ------------------------------------------------------------------
beta_sh = -S[1,1]
q = 0.9
den = S[1,1]**2 - d2_num
Phi_sh = q*E13 + 2*r/den*(-S[1,1]*S + 2*C)
res_sh = L(S,Phi_sh) + 2*r*S - beta_sh*Phi_sh
print("single-shear residual =", np.max(np.abs(res_sh)))

# ------------------------------------------------------------------
# Axisymmetric spectrum.
# ------------------------------------------------------------------
aa = 0.6
Saxi = np.diag([aa,aa,-2*aa])
Aaxi = np.array([[frob(Bi,L(Saxi,Bj)) for Bj in basis] for Bi in basis])
print("\naxisymmetric numerical spectrum =", np.linalg.eigvalsh(Aaxi))
print("expected =", sorted([-2*aa,2*aa,2*aa,-aa,-aa]))

# ------------------------------------------------------------------
# Exact local TR compatibility witness.
# S=diag(1,0,-1), Phi=E13 (unnormalized below).
# K0(z)=r^-3 I - 3 r^-5 z⊗z.
# directional derivative at z=e3, v=e1 is -3(E13+E31).
# ------------------------------------------------------------------
S0 = np.diag([1.0,0.0,-1.0])
Phi0 = np.array([[0,0,1],[0,0,0],[1,0,0]],float)
print("\nlocal shear eigen-lock residual =", np.max(np.abs(L(S0,Phi0))))

G = -3.0*Phi0
print("Riesz directional tensor G:Phi =", frob(G,Phi0))

print(
    "\nConclusion: for simple strain the local adjoint eigen-lock is exactly "
    "three single-shear families plus a coaxial Riesz-loaded family; "
    "axisymmetric eigenvalue degeneracy is the only local enlargement. "
    "A genuine Riesz-kernel shear detector can pair nontrivially with an "
    "exact shear eigen-lock, so the next obstruction is global nonlocal "
    "self-consistency rather than pointwise tensor algebra."
)
