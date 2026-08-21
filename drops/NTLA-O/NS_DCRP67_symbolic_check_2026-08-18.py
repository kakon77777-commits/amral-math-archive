# DCRP67 symbolic verification

import sympy as sp

lam, d, m = sp.symbols("lam d m", real=True)
mpos = sp.symbols("mpos", positive=True, real=True)

S = sp.diag(
    lam,
    -lam/sp.Integer(2)+d,
    -lam/sp.Integer(2)-d,
)

Snorm2 = sp.simplify(sum(S[i, i]**2 for i in range(3)))
C = sp.simplify(S*S - sp.eye(3)*Snorm2/3)

U = sp.diag(
    sp.Rational(2,3),
    -sp.Rational(1,3),
    -sp.Rational(1,3),
)
H = sp.diag(0, 1, -1)

a = sp.Rational(3,4)*lam**2-d**2
C_form = sp.simplify(a*U-lam*d*H)

print("Aligned strain |S|^2 =", sp.factor(Snorm2))
print("C normal-form difference:")
sp.pprint(sp.simplify(C-C_form))

Cnorm2 = sp.simplify(sum(C[i,i]**2 for i in range(3)))
print("|C|^2 - |S|^4/6 =", sp.factor(Cnorm2-Snorm2**2/6))

W = mpos*U
CW = sp.simplify(sum(C[i,i]*W[i,i] for i in range(3)))

chi = sp.factor(
    3*(sp.Rational(1,2)*lam**2-sp.Rational(2,3)*d**2)
    /Snorm2
)

print("C:W =", sp.factor(CW))
print("Normalized C-W angle =", chi)

detS = sp.factor(S.det())
shape_defect = sp.factor(
    1-54*detS**2/Snorm2**3
)
print("1 - determinant-shape ratio =")
sp.pprint(shape_defect)

rate_sq = sp.factor(6*Snorm2*shape_defect)
rate_sq_target = sp.factor(
    12*d**2*(4*d**2-9*lam**2)**2
    /(4*d**2+3*lam**2)**2
)

print("Angular-rate-square identity difference =",
      sp.simplify(rate_sq-rate_sq_target))

# Self-lock type checks.
for label, dval in [
    ("Type A", 0),
    ("Type B+", sp.Rational(3,2)*lam),
    ("Type B-", -sp.Rational(3,2)*lam),
]:
    Ccase = sp.simplify(C_form.subs(d, dval))
    Scase = sp.simplify(S.subs(d, dval))
    print(f"\n{label} S:")
    sp.pprint(Scase)
    print(f"{label} C:")
    sp.pprint(Ccase)
    print(f"{label} chi =", sp.simplify(chi.subs(d, dval)))

# Pairwise W increment formula check in abstract dot c = xi.xi'.
mx, my, cxy = sp.symbols("mx my cxy", positive=True, real=True)
lhs = (
    sp.Rational(2,3)*(mx**2+my**2)
    - 2*mx*my*(cxy**2-sp.Rational(1,3))
)
rhs = (
    sp.Rational(2,3)*(mx-my)**2
    + 2*mx*my*(1-cxy**2)
)
print("\nW pair split difference =", sp.expand(lhs-rhs))
