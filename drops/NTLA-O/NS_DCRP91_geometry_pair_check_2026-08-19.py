# DCRP91 tube-packing and pair-decomposition checks

import math
import random

def length_ceiling(R: float, tau: float) -> float:
    r = tau / 2.0
    return (4.0 / 3.0) * (R + r)**3 / (r**2)

print("Tube-packing length ceilings:")
for R, tau in [(5.0, 1.0), (5.0, 0.5), (10.0, 0.25)]:
    Lmax = length_ceiling(R, tau)
    print(f"R={R}, tau={tau}: L <= {Lmax:.8g}")

print(
    "\nScaling: for fixed R, the geometric length ceiling grows like tau^{-2}; "
    "therefore L->infinity in bounded support forces reach tau->0."
)

# Verify exact pairwise vorticity decomposition:
# |rho_x xi_x - rho_y xi_y|^2
# = (rho_x-rho_y)^2 + 2 rho_x rho_y (1-xi_x.xi_y)

def unit(v):
    n = math.sqrt(sum(x*x for x in v))
    return tuple(x/n for x in v)

for _ in range(5):
    xi = unit(tuple(random.uniform(-1, 1) for _ in range(3)))
    xj = unit(tuple(random.uniform(-1, 1) for _ in range(3)))
    ri = random.uniform(0.1, 3.0)
    rj = random.uniform(0.1, 3.0)

    oi = tuple(ri*x for x in xi)
    oj = tuple(rj*x for x in xj)

    lhs = sum((a-b)**2 for a, b in zip(oi, oj))
    dot = sum(a*b for a, b in zip(xi, xj))
    rhs = (ri-rj)**2 + 2*ri*rj*(1-dot)

    print("pair identity error =", abs(lhs-rhs))

# Demonstrate a shrinking filament scale is a relative-scale escape.
r_core = 1.0
ells = [2.0**(-k) for k in range(1, 8)]
print("\nRelative filament scales:")
for ell in ells:
    gap = math.log(r_core/ell, 2)
    print(f"ell={ell:.8g}, ell/r_core={ell/r_core:.8g}, dyadic gap={gap:.3f}")

print(
    "\nCompiler logic:\n"
    "bounded support + filamentation -> reach/field scale collapse or state multiplicity;\n"
    "carrier-locked curvature scale -> D50 rank/gradient witness;\n"
    "shrinking relative witness -> R_scale -> D85 gap debt."
)
