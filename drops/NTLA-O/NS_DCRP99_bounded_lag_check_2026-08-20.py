# DCRP99 bounded-lag synchronization sanity checks

from collections import Counter
import math

# Two syndetic event clocks.
B_gamma = 8
B_X = 5
B = max(B_gamma, B_X)

# Build a toy sequence where slip and X never coincide, but both are syndetic.
N = 10000
slip = set(range(2, N, B_gamma))     # gaps exactly 8
xev = set(range(4, N, B_X))          # gaps exactly 5

print("intersection size =", len(slip & xev))
print("slip density ~", len(slip)/N)
print("X density ~", len(xev)/N)

# In each disjoint B-block choose one slip and one X if possible.
pairs = []
for start in range(0, N-B+1, B):
    block = range(start, start+B)
    sg = [n for n in block if n in slip]
    xx = [n for n in block if n in xev]
    if sg and xx:
        pairs.append((sg[0], xx[0], xx[0]-sg[0]))

lags = Counter(lag for _,_,lag in pairs)
print("number paired blocks =", len(pairs))
print("lag counts =", lags)

if lags:
    lag_star, count_star = lags.most_common(1)[0]
    print("fixed lag =", lag_star)
    print("joint word density ~", count_star/N)

# Crude abstract lower bound from finite lag/type alphabet.
M_gamma = 4
M_X = 6
M_word = M_gamma * M_X * (2*B-1)
density_lower = 1/(B*M_word)
print("\ncrude finite-word density lower =", density_lower)

# D62 aligned-neutral signed X gap.
gamma = 0.45
S0 = 2.0
Omega2_integral = 1.4
signed_pressure = (
    (2-3*gamma)/2 * S0
    + Omega2_integral/6
)
print("\naligned-neutral -integral xi^T E_p xi >=", signed_pressure)

# Finite directed graph illustration:
# if no X-free directed cycle exists, the maximum X-free path length
# in a finite graph is at most the number of X-free states.
# (Compact D99 theorem is the infinite-dimensional analogue.)
n_free_states = 11
print(
    "\nfinite-state analogue: no X-free cycle => X hit within at most",
    n_free_states,
    "X-free states"
)

# Positive density does NOT imply same-generation intersection.
A = set(range(0, N, 2))
C = set(range(1, N, 2))
print("\neven/odd density =", len(A)/N, len(C)/N)
print("even/odd intersection =", len(A & C))

print(
    "\nConclusion: zero-lag synchronization is not automatic, but syndetic "
    "Kelvin and X clocks force a bounded-lag finite word; finite type/lag "
    "pigeonholing then yields one recurring X72-Kelvin word."
)
