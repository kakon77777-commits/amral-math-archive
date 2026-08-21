# DCRP100 rotational SGS transfer-kernel checks

import sympy as sp
import numpy as np

# Symbolic 3D skew matrix B and x.
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
b1, b2, b3 = sp.symbols('b1 b2 b3', real=True)
x = sp.Matrix([x1, x2, x3])

# Bx = b x x (cross product matrix)
B = sp.Matrix([
    [0, -b3, b2],
    [b3, 0, -b1],
    [-b2, b1, 0],
])
f = B*x

# Symmetric gradient.
vars_ = [x1, x2, x3]
Grad = sp.Matrix([[sp.diff(f[i], vars_[j]) for j in range(3)] for i in range(3)])
SymGrad = sp.simplify((Grad + Grad.T)/2)

print("B + B^T =")
print(sp.simplify(B+B.T))
print("Sym grad f =")
print(SymGrad)

# Curl f.
curlf = sp.Matrix([
    sp.diff(f[2],x2)-sp.diff(f[1],x3),
    sp.diff(f[0],x3)-sp.diff(f[2],x1),
    sp.diff(f[1],x1)-sp.diff(f[0],x2),
])
print("curl f =")
print(sp.simplify(curlf))

# Construct symmetric stress R_B = -(1/5)[f⊗x + x⊗f].
R = -sp.Rational(1,5)*(f*x.T + x*f.T)
divR = sp.Matrix([
    sum(sp.diff(R[i,j], vars_[j]) for j in range(3))
    for i in range(3)
])

print("R symmetric error =")
print(sp.simplify(R-R.T))
print("div R + f =")
print(sp.simplify(divR+f))

# Concrete circulation for b=e3, circle radius r in xy-plane:
# f=(-y,x,0). Param x=(r cos t, r sin t,0)
t, r = sp.symbols('t r', positive=True, real=True)
xc = sp.Matrix([r*sp.cos(t), r*sp.sin(t), 0])
Bc = sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
fc = Bc*xc
dxc = sp.diff(xc,t)
integrand = sp.simplify((fc.T*dxc)[0])
circ = sp.integrate(integrand, (t,0,2*sp.pi))

print("circle integrand =", integrand)
print("circle circulation =", sp.simplify(circ))

# Local PSD shift sanity on a bounded sample grid for b=e3.
def R_numeric(xv):
    Bn = np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]])
    fv = Bn @ xv
    return -(np.outer(fv,xv)+np.outer(xv,fv))/5.0

mins = []
for a in np.linspace(-1,1,9):
    for b in np.linspace(-1,1,9):
        for c in np.linspace(-1,1,5):
            Rv = R_numeric(np.array([a,b,c]))
            mins.append(np.min(np.linalg.eigvalsh(Rv)))
min_eig = min(mins)
shift = -min_eig + 0.1
print("sample minimum eigenvalue of R on cube =", min_eig)
print("constant isotropic shift =", shift)
print("shifted sampled minimum =", min_eig+shift)

# Five-channel Duhamel pigeonhole toy check.
cX = 1.0
terms = np.array([0.10, -0.15, 0.20, 0.05, 0.80])
print("Duhamel toy sum =", terms.sum())
print("max abs term =", np.max(np.abs(terms)))
print("cX/5 =", cX/5)

print(
    "\nConclusion: a rigid rotational SGS force can carry nonzero Kelvin "
    "circulation while its direct symmetric-gradient response vanishes. "
    "Therefore bounded-lag X/Kelvin recurrence must be analyzed through "
    "memory/indirect forcing or an additional stress-profile restriction."
)
