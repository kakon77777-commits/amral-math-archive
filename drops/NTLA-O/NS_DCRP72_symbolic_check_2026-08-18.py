# DCRP72 symbolic sanity checks
import sympy as sp

gamma,z,w,ths,thz,t = sp.symbols("gamma z w ths thz t", real=True)
Theta = ths + (gamma*z+w)*thz
print("Theta =", Theta)

R = sp.symbols("R", positive=True)
print("Integral t^2 on [-R,R] =", sp.integrate(t**2,(t,-R,R)))
print("Linear-in-t velocity => R^3 energy over fixed cross-section.")

print("Plane-uniform vorticity: pairing ~ R^2, curl-test norm ~ R => E(R) >= c R^2.")
