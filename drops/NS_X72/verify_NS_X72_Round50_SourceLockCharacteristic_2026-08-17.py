"""
Symbolic verification for NS_X72 Round 50.
Checks:
1. Round 48 state-normal determinant.
2. Horizontal source-filter coefficient.
3. Source-lock circle roots.
4. No overlap with the quadratic deep-hidden polynomial.
5. Nonhorizontal source-lock elimination via Groebner basis.
"""
import sympy as sp

I = sp.I
r, h, x = sp.symbols("r h x", positive=True, real=True)
Bx, By, Bz = sp.symbols("Bx By Bz")

def dot(a,b):
    return (a.T*b)[0]

def cross(a,b):
    return sp.Matrix([
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    ])

e3 = sp.Matrix([0,0,1])
a = {
    1: sp.Matrix([1,I,0])/2,
    -1: sp.Matrix([1,-I,0])/2,
}

def normal_side(q,B,s):
    k = q + s*e3
    return sp.simplify(
        2*dot(a[s],B)
        + 6*I*dot(
            k,
            cross(
                a[s],
                I*cross(q,B)-B
            )
        )/dot(k,k)
    )

# 1. State determinant
q = sp.Matrix([r,0,h])
B = sp.Matrix([Bx,By,Bz])
rows = [sp.Matrix([[r,0,h]])]
for s in (1,-1):
    expr = normal_side(q,B,s)
    rows.append(sp.Matrix([[sp.diff(expr,v) for v in (Bx,By,Bz)]]))
M = sp.Matrix.vstack(*rows)
detM = sp.factor(sp.together(M.det()))
expected_state_num = h*(h**4 + 2*h**2*r**2 - 2*h**2 + r**4 - 4*r**2 + 1)
assert sp.factor(sp.fraction(detM)[0] / expected_state_num).free_symbols == set()

# helper linearized Euler sideband
def euler_side(q,B,s):
    uq = I*cross(q,B)/dot(q,q)
    return sp.simplify(
        I*dot(a[s],q)*(uq-B)
        + I*s*(B[2]-uq[2])*a[s]
    )

# 2. Horizontal hidden polarization and source coefficient
qH = sp.Matrix([r,0,0])
BH = sp.Matrix([0,-r,-I*(r**2+1)/3])
assert sp.simplify(normal_side(qH,BH,1)) == 0
assert sp.simplify(normal_side(qH,BH,-1)) == 0

L = {s:euler_side(qH,BH,s) for s in (1,-1)}
outs = {2:0,0:0,-2:0}
for s in (1,-1):
    p = qH+s*e3
    for t in (1,-1):
        outs[s+t] += normal_side(p,L[s],t)
outs = {k:sp.factor(sp.together(v)) for k,v in outs.items()}

D = (r**4-13*r**2+4)/(3*(r**2+4))
assert sp.simplify(outs[2] + D) == 0
assert sp.simplify(outs[-2] - D) == 0
assert sp.simplify(outs[0]) == 0

# 3. Source roots
source_roots = sp.solve(sp.Eq(r**4-13*r**2+4,0), r)
positive_source_roots = [z for z in source_roots if z.is_positive]
expected_roots = [(sp.sqrt(17)-3)/2, (sp.sqrt(17)+3)/2]
for z in expected_roots:
    assert sp.simplify(z**4-13*z**2+4) == 0

# 4. No source/deep common positive root
Psrc = x**2-13*x+4
Pdeep = x**2-7*x+1
assert sp.gcd(sp.Poly(Psrc,x), sp.Poly(Pdeep,x)).degree() == 0

# 5. Nonhorizontal elimination
P = h**4 + 2*h**2*x - 2*h**2 + x**2 - 4*x + 1
Pp = 2*h**3 + 4*h**2 + 2*h*x + h + 3*x - 1
P0 = h**3 + h**2 + h*x - h + 2*x - 1
Pm = -7*h**4 + 2*h**3 - 16*h**2*x + 16*h**2 + h*x - 2*h + 33*x - 9

G = sp.groebner([P,Pp,P0,Pm], x,h, order="lex")
assert list(G) == [x, h+1]

print("Round 50 symbolic checks passed.")
print("State characteristic numerator:", sp.factor(expected_state_num))
print("Horizontal source coefficient D(r):", sp.factor(D))
print("Source-lock radii:", expected_roots)
print("Nonhorizontal Groebner basis:", list(G))
