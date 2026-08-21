# DCRP95 phase-slip / total-variation sanity checks
import math

rho = 0.82
c_gamma = 0.30
M = 7

c_cycle = (1-rho)*c_gamma
c_slip = 0.5*c_cycle/M
Bstar = M+1

print("cycle reset floor =", c_cycle)
print("conservative SGS slip atom =", c_slip)
print("block length =", Bstar)

for q in range(1, M+1):
    net = (1-rho**q)*c_gamma
    print(q, "weighted oriented cycle reset >=", net, "one-event avg >=", net/q)

for N in [100, 1000, 10000]:
    blocks = N // Bstar
    tv = blocks*c_slip
    print("N =", N, "TV lower =", tv, "TV/N =", tv/N)

Gamma_star = 0.6
delta = (1-rho)*Gamma_star
Gamma = Gamma_star
TV = 0.0
for _ in range(20):
    TV += abs(delta)
    Gamma = rho*Gamma + delta
print("constant conveyor Gamma =", Gamma)
print("constant conveyor reset TV =", TV)

print("Eyink model exponent 2h-1:")
for h in [0.3, 0.4, 0.5, 0.6, 0.75]:
    print(h, 2*h-1)

ells = [2.0**(-n) for n in [2,5,10,20]]
for h in [0.4,0.5,0.6]:
    print("h =", h, "model flux factors =", [ell**(2*h-1) for ell in ells])

print("Conclusion: sign-coherent reset TV grows linearly; bounded Gamma does not bound reset TV.")
