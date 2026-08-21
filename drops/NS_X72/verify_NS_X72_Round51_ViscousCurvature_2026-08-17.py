"""
Symbolic verification for NS_X72 Round 51.
Checks:
1. source/deep polynomial incompatibility;
2. source-circle hidden polarization;
3. explicit second-order state correction;
4. full two-sideband correction family;
5. correction-independent central second-order source coefficient.
"""
import sympy as sp

I = sp.I
r, t, nu = sp.symbols("r t nu", positive=True, real=True)
e3 = sp.Matrix([0,0,1])
a = {
    1: sp.Matrix([1,I,0])/2,
    -1: sp.Matrix([1,-I,0])/2,
}

def dot(x,y):
    return (x.T*y)[0]

def cross(x,y):
    return sp.Matrix([
        x[1]*y[2]-x[2]*y[1],
        x[2]*y[0]-x[0]*y[2],
        x[0]*y[1]-x[1]*y[0],
    ])

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

Psrc = r**4 - 13*r**2 + 4
Pdeep = r**4 - 7*r**2 + 1

# Polynomial incompatibility in x=r^2.
x = sp.symbols("x")
assert sp.gcd(
    sp.Poly(x**2-13*x+4,x),
    sp.Poly(x**2-7*x+1,x)
).degree() == 0

q = sp.Matrix([r,0,0])
B = sp.Matrix([0,-r,-I*(r**2+1)/3])
assert sp.simplify(dot(q,B)) == 0
assert sp.simplify(normal_side(q,B,1)) == 0
assert sp.simplify(normal_side(q,B,-1)) == 0

theta2 = sp.simplify(-2*dot(B,B))
assert sp.simplify(theta2 - 2*Pdeep/9) == 0

# Reduce modulo source polynomial.
def rem_src(expr):
    num, den = sp.fraction(sp.together(expr))
    num_poly = sp.Poly(num, r)
    # Psrc is even. Polynomial remainder in r is okay.
    rem = sp.rem(num_poly, sp.Poly(Psrc,r)).as_expr()
    return sp.factor(rem/den)

# Explicit one-sided correction.
C0 = sp.Matrix([
    (r**2+1)/3,
    -I*(4*r**2+1)/3,
    2*r*(r**2+1)/3,
])
pm = sp.Matrix([2*r,0,-1])

assert sp.simplify(dot(pm,C0)) == 0
assert rem_src(normal_side(pm,C0,-1)) == 0
assert rem_src(normal_side(pm,C0,1) + theta2) == 0

# Full two-sideband affine family.
gamma = (4*r**2+1)/(2*r*(r**2+1))
vm = sp.Matrix([1/(2*r), -I*gamma, 1])
vp = sp.Matrix([-1/(2*r), -I*gamma, 1])
Cm = C0 + t*vm
Cp = t*vp
pp = sp.Matrix([2*r,0,1])

assert sp.simplify(dot(pm,Cm)) == 0
assert sp.simplify(dot(pp,Cp)) == 0
assert rem_src(normal_side(pm,Cm,-1)) == 0
assert rem_src(normal_side(pp,Cp,1)) == 0
assert rem_src(
    normal_side(pm,Cm,1)
    + normal_side(pp,Cp,-1)
    + theta2
) == 0

# Heat-rate mismatch / central source coefficient.
central = sp.simplify(2*nu*(r**2+1)*theta2)
expected = 4*nu*(r**2+1)*Pdeep/9
assert sp.simplify(central-expected) == 0

central_on_source = rem_src(
    central
    - 4*nu*(r**2+1)*(2*r**2-1)/3
)
assert central_on_source == 0

roots = [
    (sp.sqrt(17)-3)/2,
    (sp.sqrt(17)+3)/2,
]
for rr in roots:
    assert sp.simplify(Psrc.subs(r,rr)) == 0
    assert sp.simplify(Pdeep.subs(r,rr)) != 0

print("Round 51 symbolic checks passed.")
print("theta2 =", sp.factor(theta2))
print("central source =", sp.factor(central))
print("source radii =", roots)
