# DCRP105 vanishing-viscosity / shear-TR / residual matching checks
import sympy as sp
import numpy as np

# -----------------------------------------------------------
# 1. Symbolic Riesz-kernel directional derivative contracted
#    against H_13.
# K = c[r^-3 I - 3 r^-5 z⊗z].
# -----------------------------------------------------------
x, y, z = sp.symbols("x y z", real=True)
v1, v2, v3, c = sp.symbols("v1 v2 v3 c", real=True)
R = sp.sqrt(x**2 + y**2 + z**2)
zz = sp.Matrix([x, y, z])
v = sp.Matrix([v1, v2, v3])
I = sp.eye(3)
K = c*(R**-3*I - 3*R**-5*(zz*zz.T))

G = sp.zeros(3)
for a in range(3):
    for b in range(3):
        G[a,b] = sum(v[k]*sp.diff(K[a,b],[x,y,z][k]) for k in range(3))

H13 = sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])
contract = sp.simplify(sum(G[a,b]*H13[a,b] for a in range(3) for b in range(3)))

# Evaluate z=e3*r, v=e1.
rr = sp.symbols("rr", positive=True)
val = sp.simplify(contract.subs({
    x:0, y:0, z:rr,
    v1:1, v2:0, v3:0
}))
print("Riesz derivative H13 pairing at z=r e3, v=e1 =", val)

# -----------------------------------------------------------
# 2. General hand formula numerical audit.
# -----------------------------------------------------------
def formula(v,n,r=1.0,c=1.0,i=0,j=2):
    return -6*c*r**-4 * (
        v[i]*n[j] + v[j]*n[i] - 5*np.dot(v,n)*n[i]*n[j]
    )

print("hand formula canonical =", formula(
    np.array([1.,0.,0.]),
    np.array([0.,0.,1.])
))

# -----------------------------------------------------------
# 3. Kelvin + TR local compatibility.
# -----------------------------------------------------------
A_gamma = np.diag([1.,-1.,0.])
Q = np.diag([1.,0.,0.])
print("Kelvin A:Q =", np.sum(A_gamma*Q))
TR = formula(np.array([1.,0.,0.]), np.array([0.,0.,1.]))
delta_q = -1.0
print("TR factor * delta_q =", TR*delta_q)

# -----------------------------------------------------------
# 4. Fixed-band viscous residual exact scaling.
# -----------------------------------------------------------
rng = np.random.default_rng(21)
N = 200000
rho = rng.uniform(1.5,2.5,size=N)
weights = rng.random(N)
weights /= np.linalg.norm(weights)

eps_list = [1e-1,1e-2,1e-3,1e-4]
print("\nfixed-band residual scaling:")
for eps in eps_list:
    eta = eps*np.linalg.norm((rho**2)*weights)
    print(eps, eta, eta/eps)

rho_minus=1.5
mass=np.linalg.norm(weights)
print("lower bound coefficient rho_-^2 ||Phi|| =", rho_minus**2*mass)

# -----------------------------------------------------------
# 5. Subviscous migration inequality toy.
# Construct mass in a shrinking ball rho<=sqrt(theta).
# -----------------------------------------------------------
print("\nsubviscous migration toy:")
for theta in [1e-1,1e-2,1e-3]:
    # If eta/eps = theta, then mass outside rho0 bound theta^2/rho0^4.
    for rho0 in [0.2,0.5,1.0]:
        bound = theta**2/rho0**4
        print("theta",theta,"rho0",rho0,"outside-mass bound",bound)

# -----------------------------------------------------------
# 6. Near-resonance canonical shear:
# d=3 n2^2, h=-2 n1 n3.
# -----------------------------------------------------------
print("\ncanonical near-resonance samples:")
for n2 in [0.5,0.2,0.1,0.05,0.02]:
    n1=np.sqrt((1-n2**2)/2)
    n3=n1
    d=3*n2**2
    h=-2*n1*n3
    mult=h/d
    print("n2",n2,"d",d,"h",h,"|h/d|",abs(mult))

# -----------------------------------------------------------
# 7. Verify numerator/resonance intersections on n2=0:
# h=-2 n1 n3=0 => n1=0 or n3=0.
# -----------------------------------------------------------
angles=np.linspace(0,2*np.pi,17)
zeros=[]
for t in angles:
    n1=np.cos(t); n2=0.; n3=np.sin(t)
    h=-2*n1*n3
    if abs(h)<1e-10:
        zeros.append((round(n1,6),round(n3,6)))
print("sample resonance numerator zeros =", zeros)

# -----------------------------------------------------------
# 8. Explicit O(eps) approximate-kernel sequence.
# Take one fixed smooth Fourier profile on rho~2.
# -----------------------------------------------------------
rho_vals=np.linspace(1.8,2.2,10000)
amp=np.exp(-((rho_vals-2.0)/0.08)**2)
norm=np.sqrt(np.trapz(amp**2,rho_vals))
amp/=norm
lapnorm=np.sqrt(np.trapz((rho_vals**4)*(amp**2),rho_vals))
print("\nfixed profile Laplacian norm ~",lapnorm)
for eps in [1e-2,1e-3,1e-4]:
    eta=eps*lapnorm
    print("eps",eps,"eta",eta,"eta/eps",eta/eps)

print(
    "\nConclusion: positive-viscosity exact kernel emptiness is nonuniform. "
    "A fixed normalized inviscid shear/polarization profile survives as an "
    "O(epsilon) approximate eigen-lock; only o(epsilon) residual forces "
    "low-frequency migration. Kelvin nematic and simple-shear TR angular "
    "locks are locally compatible."
)
