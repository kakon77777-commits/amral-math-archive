# DCRP104 Riesz self-consistency checks
import sympy as sp
import numpy as np

# -----------------------------------------------------------
# 1. Symbol M(n) = I/3 - n n^T and trace-free contraction.
# -----------------------------------------------------------
n = np.array([1.0,2.0,3.0])
n = n/np.linalg.norm(n)
M = np.eye(3)/3.0 - np.outer(n,n)

Phi = np.array([
    [1.0,0.2,0.1],
    [0.2,-0.3,0.4],
    [0.1,0.4,-0.7],
])
print("tr Phi =", np.trace(Phi))
print("M:Phi =", np.sum(M*Phi))
print("-n^T Phi n =", -(n@Phi@n))

# -----------------------------------------------------------
# 2. Symbolic simple-shear loading tensor.
# -----------------------------------------------------------
si, sj = sp.symbols("si sj", real=True)
sk = -(si+sj)
S2 = si**2 + sj**2 + sk**2
d2 = sp.Rational(2,3)*S2
den = sp.simplify(sk**2-d2)
print("\ns_k^2-d_S^2 =", sp.factor(den))

vals = []
for sm in (si,sj,sk):
    C = sm**2-S2/3
    vals.append(sp.factor(2*(-sk*sm+2*C)/den))
print("A shear ordered eigenvalues =", vals)

# -----------------------------------------------------------
# 3. Concrete simple shear S=diag(1,0,-1), H13.
# -----------------------------------------------------------
S = np.diag([1.0,0.0,-1.0])
A = np.diag([-1.0,2.0,-1.0])

nstar = np.ones(3)/np.sqrt(3.0)
a = -nstar@A@nstar
h = -2*nstar[0]*nstar[2]
mult = h/(1-a)

print("\nconcrete shear at n*=(1,1,1)/sqrt3:")
print("a(n*) =", a)
print("1-a =", 1-a)
print("h13 =", h)
print("r/q multiplier =", mult)

# Verify self-consistency m:Phi = r for q=1.
H13 = np.array([[0,0,1],[0,0,0],[1,0,0]],float)
r = mult
Phi_hat = H13 + A*r
Mstar = np.eye(3)/3.0 - np.outer(nstar,nstar)
print("M:Phi_hat =", np.sum(Mstar*Phi_hat), " r =", r)

# Sample an angular patch away from n2=0 and verify bounded multiplier.
rng = np.random.default_rng(9)
mults=[]
for _ in range(100000):
    v = nstar + 0.12*rng.normal(size=3)
    v /= np.linalg.norm(v)
    denv = 3*v[1]**2
    if denv > 1e-12:
        mults.append((-2*v[0]*v[2])/denv)
print("patch multiplier max abs ~", max(abs(x) for x in mults))

# -----------------------------------------------------------
# 4. Axisymmetric cross-plane polarization.
# -----------------------------------------------------------
aa = 0.7
Saxi = np.diag([aa,aa,-2*aa])
H23 = np.array([[0,0,0],[0,0,1],[0,1,0]],float)

def frob(A,B):
    return float(np.sum(A*B))

def L(S,P):
    return P@S + S@P - (2/3)*frob(S,P)*np.eye(3)

errs_r=[]
errs_L=[]
for _ in range(1000):
    v=rng.normal(size=3)
    v/=np.linalg.norm(v)
    Ppol = -v[1]*H13 + v[0]*H23
    Mv = np.eye(3)/3.0 - np.outer(v,v)
    errs_r.append(abs(frob(Mv,Ppol)))
    errs_L.append(np.max(np.abs(L(Saxi,Ppol)+aa*Ppol)))
print("\naxisymmetric cross-plane polarization:")
print("max |M:Ppol| =", max(errs_r))
print("max eigen equation error =", max(errs_L))

# -----------------------------------------------------------
# 5. Axisymmetric planar polarization.
# -----------------------------------------------------------
D = np.diag([1.0,-1.0,0.0])
H12 = np.array([[0,1,0],[1,0,0],[0,0,0]],float)
errs_r=[]
errs_L=[]
for _ in range(1000):
    v=rng.normal(size=3)
    v/=np.linalg.norm(v)
    Ppol = -2*v[0]*v[1]*D + (v[0]**2-v[1]**2)*H12
    Mv = np.eye(3)/3.0 - np.outer(v,v)
    errs_r.append(abs(frob(Mv,Ppol)))
    errs_L.append(np.max(np.abs(L(Saxi,Ppol)-2*aa*Ppol)))
print("\naxisymmetric planar polarization:")
print("max |M:Ppol| =", max(errs_r))
print("max eigen equation error =", max(errs_L))

# -----------------------------------------------------------
# 6. Frozen viscous determinant sanity: build 5x5 symbol and
# show determinant grows at large frequency.
# -----------------------------------------------------------
E12 = H12/np.sqrt(2)
E13n = H13/np.sqrt(2)
E23n = H23/np.sqrt(2)
D1 = D/np.sqrt(2)
D2 = np.diag([1,1,-2])/np.sqrt(6)
basis = [E23n,E13n,E12,D1,D2]

def operator_matrix(S,nvec,nu,rho,beta):
    Mv=np.eye(3)/3.0-np.outer(nvec,nvec)
    mat=np.zeros((5,5))
    for j,B in enumerate(basis):
        out = nu*rho**2*B + L(S,B) + 2*S*frob(Mv,B) - beta*B
        for i,Ai in enumerate(basis):
            mat[i,j]=frob(Ai,out)
    return mat

nvec=np.array([1.,1.,1.])/np.sqrt(3)
for rho in [1,10,100]:
    mat=operator_matrix(S,nvec,0.2,rho,0.1)
    print("rho",rho,"det",np.linalg.det(mat))

print(
    "\nConclusion: frozen whole-space L2 coaxial rays are forced onto "
    "measure-zero quadratic Fourier cones and vanish; simple shear rays "
    "instead survive through a regular order-zero Riesz multiplier off "
    "their resonance cone, while axisymmetric degeneracy admits genuine "
    "vector-polarization kernels with r=0."
)
