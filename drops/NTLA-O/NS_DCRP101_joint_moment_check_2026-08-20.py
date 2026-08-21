# DCRP101 second/third-moment and triple-increment checks

import itertools
import numpy as np

# -------------------------------------------------------------------
# 1. General discrete triple-increment identity.
# For a symmetric pair kernel G with zero row sums:
# <phi, G q> = -1/2 sum_ij G_ij (phi_i-phi_j)(q_i-q_j)
# -------------------------------------------------------------------

G = np.array([
    [ 2.0, -1.0, -1.0],
    [-1.0,  3.0, -2.0],
    [-1.0, -2.0,  3.0],
])
assert np.allclose(G, G.T)
assert np.allclose(G.sum(axis=1), 0.0)

phi = np.array([0.3, -1.1, 0.7])
q = np.array([1.2, -0.4, 0.9])

lhs = phi @ (G @ q)

rhs = 0.0
for i in range(3):
    for j in range(3):
        rhs += -0.5 * G[i,j] * (phi[i]-phi[j]) * (q[i]-q[j])

print("general pair identity:")
print("lhs =", lhs)
print("rhs =", rhs)
print("error =", abs(lhs-rhs))

# -------------------------------------------------------------------
# 2. Parity-copula example.
# Same one-factor and pairwise marginals, same Kelvin second moment,
# but triple moment +1, 0, -1.
# -------------------------------------------------------------------

def law_case(mode):
    rows = []
    if mode in ("positive", "negative"):
        for s,t in itertools.product([-1,1], repeat=2):
            c = s*t if mode == "positive" else -s*t
            rows.append((s,t,c,1/4))
    elif mode == "zero":
        for s,t,r in itertools.product([-1,1], repeat=3):
            rows.append((s,t,r,1/8))
    return rows

def moments(rows):
    E_u2 = sum(w*s*s for s,t,c,w in rows)
    E_abc = sum(w*s*t*c for s,t,c,w in rows)
    E_a = sum(w*s for s,t,c,w in rows)
    E_b = sum(w*t for s,t,c,w in rows)
    E_c = sum(w*c for s,t,c,w in rows)
    E_ab = sum(w*s*t for s,t,c,w in rows)
    E_ac = sum(w*s*c for s,t,c,w in rows)
    E_bc = sum(w*t*c for s,t,c,w in rows)
    return {
        "E_u2":E_u2,
        "E_abc":E_abc,
        "E_a":E_a,
        "E_b":E_b,
        "E_c":E_c,
        "E_ab":E_ab,
        "E_ac":E_ac,
        "E_bc":E_bc,
    }

print("\nparity-copula cases:")
for mode in ["positive","zero","negative"]:
    print(mode, moments(law_case(mode)))

# -------------------------------------------------------------------
# 3. Kelvin covariance example remains fixed.
# u = ±e1 -> Q=e1⊗e1.
# -------------------------------------------------------------------

e1 = np.array([1.0,0.0,0.0])
Q = np.outer(e1,e1)
A_gamma = np.diag([1.0,-1.0,0.0])
print("\nKelvin covariance Q =\n", Q)
print("A_gamma:Q =", np.sum(A_gamma*Q))

# -------------------------------------------------------------------
# 4. D66 coefficient check:
# Q_TR = sqrt(6) Q_CC - sqrt(3/8) Q_Cw
#      = sqrt(3/8) (4 Q_CC - Q_Cw)
# -------------------------------------------------------------------

coef_ratio = np.sqrt(6.0) / np.sqrt(3.0/8.0)
print("\nD66 coefficient ratio =", coef_ratio)

Q_CC = 0.7
Q_Cw = 1.9
Q_TR = np.sqrt(6.0)*Q_CC - np.sqrt(3.0/8.0)*Q_Cw
Q_TR_alt = np.sqrt(3.0/8.0)*(4*Q_CC-Q_Cw)
print("Q_TR =", Q_TR)
print("Q_TR_alt =", Q_TR_alt)
print("identity error =", abs(Q_TR-Q_TR_alt))

c_TR = abs(Q_TR)
distance_4to1 = abs(Q_Cw-4*Q_CC)
predicted = np.sqrt(8.0/3.0)*c_TR
print("|Q_Cw - 4 Q_CC| =", distance_4to1)
print("sqrt(8/3)|Q_TR| =", predicted)

# -------------------------------------------------------------------
# 5. Same pairwise statistics, different third-order copula.
# Verify every pair distribution is uniform in all cases.
# -------------------------------------------------------------------

def pair_distribution(rows, inds):
    d = {}
    for row in rows:
        vals = row[:3]
        w = row[3]
        key = tuple(vals[i] for i in inds)
        d[key] = d.get(key,0.0)+w
    return d

base = law_case("positive")
for mode in ["zero","negative"]:
    rows = law_case(mode)
    for inds in [(0,1),(0,2),(1,2)]:
        same = pair_distribution(base, inds) == pair_distribution(rows, inds)
        print(f"pair marginal {inds}, positive vs {mode}: same =", same)

print(
    "\nConclusion: Kelvin second moments and even all one-/two-factor "
    "marginals do not determine the transport-Riesz mixed third moment. "
    "The surviving information is a genuine joint copula/path-phase lock."
)
