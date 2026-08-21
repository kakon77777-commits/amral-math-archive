# DCRP66 symbolic checks

import sympy as sp

# Verify the trace-free 3x3 cofactor norm identity through tracefree eigenvalues.
a, b = sp.symbols("a b", real=True)
c = -a-b
p2 = sp.expand(a**2+b**2+c**2)
p4 = sp.expand(a**4+b**4+c**4)

print("p4 - p2^2/2 =", sp.factor(p4 - p2**2/sp.Integer(2)))

# C eigenvalues = s_i^2 - p2/3
C2 = sp.expand(
    (a**2-p2/3)**2
    +(b**2-p2/3)**2
    +(c**2-p2/3)**2
)
print("|C|^2 - |S|^4/6 =", sp.factor(C2 - p2**2/sp.Integer(6)))

# Two-stress source coefficient ratio.
ratio = sp.simplify(
    sp.sqrt(6) / sp.sqrt(sp.Rational(3,8))
)
print("source-flat amplitude ratio =", ratio)

# Stress norm relation.
m = sp.symbols("m", positive=True, real=True)
Wnorm = sp.sqrt(sp.Rational(2,3))*m
recovered_m = sp.simplify(sp.sqrt(sp.Rational(3,2))*Wnorm)
print("Recovered |Omega|^2 from |W_Omega| =", recovered_m)

# Correlation coefficient balance:
# sqrt(6) Qcc - sqrt(3/8) Qcw = 0 -> Qcw=4 Qcc
Qcc, Qcw = sp.symbols("Qcc Qcw", real=True)
sol = sp.solve(
    sp.Eq(sp.sqrt(6)*Qcc-sp.sqrt(sp.Rational(3,8))*Qcw, 0),
    Qcw
)
print("silent correlation balance:", sol)
