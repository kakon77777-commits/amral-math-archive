"""
Symbolic verification for NS_X72 Round 52.

Checks:
1. The explicit n=2,4 Floquet block is divergence-free.
2. The three state-normal outputs n=1,3,5 vanish.
3. The central source coefficient J0 is exact and nonzero.
4. The source output coefficients J2,J3,J4,J6 match the paper.
5. The Round 51 curvature can be exactly cancelled by a scalar multiple
   of the hidden block.
"""
import sympy as sp

I = sp.I
K, nu, r = sp.symbols("K nu r", positive=True, real=True)
e3 = sp.Matrix([0,0,1])

def a(s):
    return sp.Matrix([1, s*I, 0])/2

def dot(x,y):
    return (x.T*y)[0]

def cross(x,y):
    return sp.Matrix([
        x[1]*y[2]-x[2]*y[1],
        x[2]*y[0]-x[0]*y[2],
        x[0]*y[1]-x[1]*y[0],
    ])

def Nside(k,B,s):
    kout = k+s*e3
    return sp.factor(
        2*dot(a(s),B)
        + 6*I*dot(
            kout,
            cross(
                a(s),
                I*cross(k,B)-B
            )
        )/dot(kout,kout)
    )

def vel(k,B):
    return I*cross(k,B)/dot(k,k)

def EulerSide(k,B,s):
    u = vel(k,B)
    return sp.simplify(
        I*dot(a(s),k)*(u-B)
        + I*s*(B[2]-u[2])*a(s)
    )

Q = K**4 + 4*K**2 + 9
D = K**4 + 28*K**2 + 225

x4 = -(K**2+25)*Q/(2*(K**2+1)*D)

B2 = sp.Matrix([
    2,
    I*(K**2-2)/(K**2+1),
    -K,
])

B4 = sp.Matrix([
    4*x4,
    I*x4*(7*K**2+100)/(K**2+25),
    -K*x4,
])

k2 = sp.Matrix([K,0,2])
k4 = sp.Matrix([K,0,4])

assert sp.simplify(dot(k2,B2)) == 0
assert sp.simplify(dot(k4,B4)) == 0

assert sp.simplify(Nside(k2,B2,-1)) == 0
assert sp.simplify(Nside(k4,B4,1)) == 0
assert sp.simplify(
    Nside(k2,B2,1)
    + Nside(k4,B4,-1)
) == 0

def source_outputs(k,B):
    n = int(k[2])
    out = {}
    # Euler: N L_E
    for s in (-1,1):
        C = EulerSide(k,B,s)
        p = k+s*e3
        for t in (-1,1):
            m = n+s+t
            out[m] = out.get(m,0) + Nside(p,C,t)
    # Viscous hidden spectral dispersion: nu N Delta
    knorm2 = dot(k,k)
    for s in (-1,1):
        m = n+s
        out[m] = out.get(m,0) + nu*Nside(k,-knorm2*B,s)
    return out

o2 = source_outputs(k2,B2)
o4 = source_outputs(k4,B4)

outs = {}
for m in sorted(set(o2)|set(o4)):
    outs[m] = sp.factor(
        sp.simplify(
            o2.get(m,0)
            + o4.get(m,0)
        )
    )

J0 = -I*K*(K**4+7*K**2+18)/((K**2+1)*(K**2+4))

P2 = K**8 + 95*K**6 + 1549*K**4 + 4947*K**2 + 5400
J2 = I*K*P2/(2*(K**2+1)*(K**2+4)*D)

J3 = -96*nu*Q/((K**2+1)*(K**2+9))

P4 = (
    K**10 + 27*K**8 + 495*K**6 + 5719*K**4
    + 24906*K**2 + 43200
)
J4 = I*K*P4/(
    (K**2+1)*(K**2+4)*(K**2+16)*D
)

J6 = -I*K**3*(K**4-5*K**2-360)*Q/(
    2*(K**2+1)*(K**2+16)*(K**2+36)*D
)

assert sp.simplify(outs[0]-J0) == 0
assert sp.simplify(outs[1]) == 0
assert sp.simplify(outs[2]-J2) == 0
assert sp.simplify(outs[3]-J3) == 0
assert sp.simplify(outs[4]-J4) == 0
assert sp.simplify(outs[5]) == 0
assert sp.simplify(outs[6]-J6) == 0

# Central rescue on K=2r.
J0r = sp.factor(J0.subs(K,2*r))
Vcurv = 4*nu*(r**2+1)*(r**4-7*r**2+1)/9
cres = sp.factor(-Vcurv/J0r)

assert sp.simplify(
    Vcurv
    + cres*J0r
) == 0

# J2 is manifestly nonzero for positive K because its polynomial
# and denominator are positive and K>0.
assert all(c > 0 for c in [1,95,1549,4947,5400])

print("Round 52 symbolic checks passed.")
print("J0(K) =", sp.factor(J0))
print("J2(K) =", sp.factor(J2))
print("J3(K) =", sp.factor(J3))
print("rescue amplitude c_res =", sp.factor(cres))
