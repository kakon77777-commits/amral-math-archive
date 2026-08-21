# DCRP89 first-exit / tail-supplier scaling checks

import math

# Tail energy atom:
# Gamma_filt <= L_* ||U_l||_inf
# ||U_l||_inf <= ||phi_l||_2 ||U||_L2
# ||phi_l||_2 = C_phi l^(-3/2)
# If Gamma_filt >= cGamma/2:
# E_tube >= cGamma^2 l^3 / (4 C_phi^2 L_*^2)

cGamma = 0.4
ell = 0.2
Cphi = 1.7
Lstar = 3.0

cE = cGamma**2 * ell**3 / (4*Cphi**2*Lstar**2)
print("Tail energy atom c_E =", cE)
print("positive:", cE > 0)

# Packing trade:
# J cE <= M_J C_M R_J
CM = 2.5

for J, M in [(10,1), (100,1), (100,5), (1000,20)]:
    Rmin = cE * J / (M*CM)
    print(f"J={J}, overlap={M}: R_J >= {Rmin:.8g}")

# Backward length escape strain action:
L0 = 1.0
Lexit = 4.0
strain_action_floor = math.log(Lexit/L0)
print("\nLength-exit strain action floor =", strain_action_floor)

# Robust Kelvin shadowing threshold from D88.
rho = 0.83
eta_threshold = 0.5*(1-rho)*cGamma
print("Robust Kelvin error threshold =", eta_threshold)

# Demonstrate Morrey compatibility with a linear-speed supplier:
# one fixed energy atom per unit radial interval gives E(R) ~ cE * R.
for R in [10, 100, 1000]:
    atoms = int(R)
    packed_energy = atoms*cE
    morrey_model = 2*cE*R
    print(
        f"R={R}: supplier energy={packed_energy:.8g}, "
        f"linear Morrey model={morrey_model:.8g}, compatible={packed_energy <= morrey_model}"
    )

print(
    "\nConclusion: first-exit tail atoms are quantitatively paid, "
    "but Morrey packing allows a linear-speed infinite tail supplier. "
    "The next target is annular/far-field confluence."
)
