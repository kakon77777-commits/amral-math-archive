# DCRP84 scaling and capacity sanity checks

import sympy as sp

r, h, Lambda, eps = sp.symbols(
    "r h Lambda eps",
    positive=True,
    real=True,
)

# Critical line increment amplitude A ~ 1/r.
A = 1/r

# Coherent tube energy at a fixed time:
# A^2 * line_length(r) * cross_area(h^2)
E_atom = sp.simplify(A**2 * r * h**2)
print("Atom kinetic energy lower scaling =", E_atom)

E_Lambda = sp.simplify(E_atom.subs(h, r/Lambda))
print("In terms of Lambda=r/h:", E_Lambda)
print("Expected r/Lambda^2.")

# 2D condenser capacity energy:
cap_cross = 2*sp.pi*A**2 / sp.log(r/h)
print("\n2D transverse capacity energy =", cap_cross)

# Multiply by line length r and time r^2.
cap_spacetime = sp.simplify(cap_cross * r * r**2)
print("Space-time gradient cost =", cap_spacetime)

cap_Lambda = sp.simplify(
    cap_spacetime.subs(h, r/Lambda)
)
print("In terms of Lambda:", cap_Lambda)
print("Scale-normalized /r =", sp.simplify(cap_Lambda/r))

visc = sp.simplify(eps*cap_Lambda)
print("Viscous payment with coefficient eps =", visc)

Theta, C = sp.symbols("Theta C", positive=True)
q = C*Theta**(-sp.Rational(1,4))
print("\nD83 generation ratio extraction q <=", q)
print("If Theta -> infinity, q -> 0.")

print(
    "\nCompiler consequence:\n"
    "bounded generation ratio q>=q_->0 "
    "=> bounded trace ratio "
    "=> positive volumetric increment detector."
)
