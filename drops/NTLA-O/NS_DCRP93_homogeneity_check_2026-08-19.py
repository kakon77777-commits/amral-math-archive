# DCRP93 homogeneity-sign and geometric-summability checks

import math

def geometric_cost_sum(ell0, q, p, Jmax, N=100000):
    return sum((ell0*(q**n))**p * Jmax for n in range(N))

alpha_samples = [1.05, 1.20, 1.40, 1.49]
print("Type-II homogeneity exponents:")
for alpha in alpha_samples:
    kappa = 3.0 - 2.0*alpha
    p_gamma = 1.0 - alpha
    p_helicity = 2.0 - 2.0*alpha
    print(
        f"alpha={alpha:.2f}: "
        f"kappa={kappa:.4f}>0, "
        f"p_Gamma={p_gamma:.4f}<0, "
        f"p_H={p_helicity:.4f}<0"
    )

ell0 = 1.0
q = 0.5
Jmax = 2.0

print("\nPositive-homogeneity geometric sums:")
for p in [0.02, 0.2, 0.8, 1.0]:
    approx = geometric_cost_sum(ell0, q, p, Jmax, N=5000)
    exact = Jmax * ell0**p / (1.0-q**p)
    print(
        f"p={p}: numerical={approx:.10g}, exact={exact:.10g}"
    )

print("\nSubset activation cannot exceed full geometric sum:")
active = [n for n in range(5000) if (n % 3) == 0]
p = 0.4
subset = sum((ell0*q**n)**p * Jmax for n in active)
full = Jmax/(1-q**p)
print("subset =", subset)
print("full   =", full)
print("subset <= full:", subset <= full + 1e-12)

print("\nNegative homogeneity amplitudes grow on smaller scales:")
alpha = 1.25
p_gamma = 1-alpha
for n in [0, 5, 10, 20]:
    ell = q**n
    amp = ell**p_gamma
    print(f"n={n}, ell={ell:.8g}, ell^(1-alpha)={amp:.8g}")

print("\nZero homogeneity with positive-density activation:")
N = 10000
active_count = sum(1 for n in range(N) if n % 4 == 0)
print("density ~", active_count/N)
print("unweighted sum with unit gap =", active_count)

gamma = 1/(1.25+1)
kappa = 3-2*1.25
print("\nSimilarity-dilation sign check:")
print("gamma =", gamma, "kappa =", kappa, "gamma*kappa =", gamma*kappa)
print("Periodic K ledger requires integral Pi = gamma*kappa * integral K > 0.")

print(
    "\nConclusion: positive generation density never defeats p>0 geometric summability; "
    "a non-summable regeneration witness needs p<=0 plus a finite/conserved capacity."
)
