"""
Symbolic / numerical verification for NS_X72 Round 53.

Checks:
1. General lower/upper boundary-null polarizations.
2. General compact hidden-pair state cancellation.
3. Hidden-pair ratio asymptotics.
4. Source-output asymptotics.
5. Frozen recurrence characteristic factorization.
6. Canonical one-sided source cascade at the two sqrt(17) fibres
   numerically approaches the predicted factorial-growing multiplier.
"""
import sympy as sp
import math

I = sp.I
K, n, nu = sp.symbols("K n nu", positive=True, real=True)
e3 = sp.Matrix([0,0,1])

def a(s):
    return sp.Matrix([1,s*I,0])/2

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

Dm = K**2+(n-1)**2
Dp = K**2+(n+1)**2
Pn = K**4+2*K**2*n**2-4*K**2+n**4-2*n**2+1

Bn = sp.Matrix([
    n,
    I*((3-n)*K**2-n*(n-1)**2)/Dm,
    -K,
])

np2 = n+2
Dp2 = K**2+(np2+1)**2
Bm0 = sp.Matrix([
    np2,
    I*((np2+3)*K**2+np2*(np2+1)**2)/Dp2,
    -K,
])

kn = sp.Matrix([K,0,n])
km = sp.Matrix([K,0,np2])

assert sp.simplify(dot(kn,Bn)) == 0
assert sp.simplify(dot(km,Bm0)) == 0
assert sp.simplify(Nside(kn,Bn,-1)) == 0
assert sp.simplify(Nside(km,Bm0,1)) == 0

rho = sp.factor(
    -Nside(kn,Bn,1)/Nside(km,Bm0,-1)
)

# Compact hidden pair.
assert sp.simplify(
    Nside(kn,Bn,1)
    + rho*Nside(km,Bm0,-1)
) == 0

# Check ratio expansion through n^-3.
eps = sp.symbols("eps", positive=True)
rho_eps = sp.series(
    rho.subs(n,1/eps),
    eps, 0, 5
).removeO()
rho_asym = sp.expand(rho_eps.subs(eps,1/n))
target_rho = -1 + 2/n - 4/n**2 + 8/n**3
assert sp.limit(
    n**4*(rho_asym-target_rho),
    n, sp.oo
).is_finite

def source_rel(level,B):
    k = sp.Matrix([K,0,level])
    out = {}
    for s in (-1,1):
        C = EulerSide(k,B,s)
        p = k+s*e3
        for t in (-1,1):
            off = s+t
            out[off] = sp.simplify(
                out.get(off,0)+Nside(p,C,t)
            )
    k2 = dot(k,k)
    for s in (-1,1):
        off = s
        out[off] = sp.simplify(
            out.get(off,0)
            + nu*Nside(k,-k2*B,s)
        )
    return out

o1 = source_rel(n,Bn)
o2 = source_rel(n+2,rho*Bm0)

comb = {}
for off,val in o1.items():
    comb[off] = comb.get(off,0)+val
for off,val in o2.items():
    comb[off+2] = comb.get(off+2,0)+val
comb = {
    off:sp.factor(sp.together(sp.simplify(comb.get(off,0))))
    for off in (-2,-1,0,1,2,3,4)
}

assert comb[-1] == 0
assert comb[3] == 0

# Exact intermediate viscous coefficient.
J1_expected = -16*n*nu*(n+1)*Pn/(Dm*Dp)
assert sp.simplify(comb[1]-J1_expected) == 0

# Leading asymptotics checked by limits.
assert sp.simplify(
    sp.limit(n**2*comb[-2]/(-I*K**3),n,sp.oo)-1
) == 0
assert sp.simplify(
    sp.limit(comb[0]/(4*I*K),n,sp.oo)-1
) == 0
assert sp.simplify(
    sp.limit(comb[2]/(4*I*K),n,sp.oo)-1
) == 0
assert sp.simplify(
    sp.limit(n**2*comb[4]/(-I*K**3),n,sp.oo)-1
) == 0
assert sp.simplify(
    sp.limit(comb[1]/(-16*nu*n**2),n,sp.oo)-1
) == 0

# Frozen characteristic factorization.
A, lam = sp.symbols("A lam")
poly = lam**3-A*lam**2-A*lam+1
assert sp.simplify(poly-(lam+1)*(lam**2-(A+1)*lam+1)) == 0

# Numerical coefficient functions.
funcs = {
    off:sp.lambdify((K,n,nu),comb[off],"math")
    for off in (-2,0,1,2,4)
}

def coeffs(Kv,nv,nuv=0.0):
    return {
        off:complex(funcs[off](Kv,nv,nuv))
        for off in funcs
    }

def cascade_ratio(Kv,Nmax=1200):
    # normalized target g0=1; one-sided compact-block cascade.
    c2 = -1/coeffs(Kv,2,0.0)[-2]
    d2 = c2*coeffs(Kv,2,0.0)[0]
    c4 = -d2/coeffs(Kv,4,0.0)[-2]
    amps = {2:c2,4:c4}
    ratios = {4:c4/c2}

    for m in (4,6):
        d = 0j
        for j in (m,m-2,m-4):
            if j in amps:
                d += amps[j]*coeffs(Kv,j,0.0)[m-j]
        cnew = -d/coeffs(Kv,m+2,0.0)[-2]
        amps[m+2] = cnew
        ratios[m+2] = cnew/amps[m]

    for m in range(8,Nmax,2):
        Rm = ratios[m]
        Rm2 = ratios[m-2]
        A0 = coeffs(Kv,m,0.0)[0]
        B0 = coeffs(Kv,m-2,0.0)[2]
        C0 = coeffs(Kv,m-4,0.0)[4]
        L0 = coeffs(Kv,m+2,0.0)[-2]
        ratios[m+2] = -(
            A0
            + B0/Rm
            + C0/(Rm*Rm2)
        )/L0

    return amps, ratios

rminus = (math.sqrt(17)-3)/2
rplus = (math.sqrt(17)+3)/2

for rr in (rminus,rplus):
    Kv = 2*rr
    amps, ratios = cascade_ratio(Kv,1200)
    observed = abs(ratios[1002])/(1000**2)
    predicted = 4/(Kv**2)
    relerr = abs(observed-predicted)/predicted
    assert relerr < 0.02
    print("K =",Kv)
    print("predicted 4/K^2 =",predicted)
    print("n=1000 observed =",observed)
    print("relative error =",relerr)
    print("early amplitudes:",
          {m:abs(amps[m]) for m in sorted(amps) if m <= 8})
    print()

print("Round 53 symbolic/numerical checks passed.")
