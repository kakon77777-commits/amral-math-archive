# DCRP65 symbolic sanity checks

import sympy as sp

lamstar, S0, I_lam2 = sp.symbols(
    "lamstar S0 I_lam2",
    positive=True,
    real=True,
)

period_riccati = lamstar*S0 + I_lam2
print("Periodic aligned q=0 condition would require:")
print("0 =", period_riccati, "> 0")

kappa = sp.symbols("kappa", real=True)
print("\nConstant-source q0 cutoff exponent:", kappa-5)
print("It tends to zero for kappa < 5.")

print(
    "\nAffine-kernel rigidity logic: "
    "v ⟂ n implies (n^T A n)|v|^2=0; "
    "hence sym(A)=0, then the remaining skew condition forces A=0."
)
