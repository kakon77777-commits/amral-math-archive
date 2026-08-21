# DCRP92 finite detector sanity checks
from math import floor

def ceil_div(a, b):
    return (a + b - 1) // b

for N, M in [(10,3), (100,7), (1000,11)]:
    lower = ceil_div(N, M)
    print(N, M, lower, lower/N, 1/M)

for M, Nstar in [(5,4), (8,7), (12,10)]:
    for N in [1000,10000]:
        events = floor(N/Nstar)
        lower = ceil_div(events, M)
        print("block", M, Nstar, N, lower/N, 1/(M*Nstar))

eps = 0.04
print("coarse threshold", eps/8)

samples = [(0.8,0.20),(0.7,0.13),(0.6,0.09),(0.5,0.05)]
c_fv = 0.5
eligible = [s for r,s in samples if r >= c_fv]
print("sample compact separation min S =", min(eligible))
