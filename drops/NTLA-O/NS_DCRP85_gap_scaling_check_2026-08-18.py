# DCRP85 dyadic gap and scale-debt sanity checks

import math

def dyadic_gap(r_parent: float, r_child: float) -> int:
    assert 0 < r_child < r_parent
    return math.floor(math.log(r_parent / r_child, 2))

samples = [
    (1.0, 2**-4),
    (1.0, 2**-10),
    (0.125, 0.125 * 2**-20),
]

for rp, rc in samples:
    m = dyadic_gap(rp, rc)
    ratio = rp / rc
    print(
        f"parent={rp:g}, child={rc:g}, "
        f"gap m={m}, ratio={ratio:g}, "
        f"2^m <= ratio < 2^(m+1): "
        f"{2**m <= ratio < 2**(m+1)}"
    )

print("\nTwo-observer relative frequencies:")
for m in [4, 10, 20]:
    uv = 2**m
    ir = 2**(-m)
    print(f"m={m}: parent UV={uv:g}, child IR={ir:g}, product={uv*ir:g}")

# Schematic finite-chain debt.
# If each CKN-bad scale has standard package >= c_std(M),
# a gap with m+1 bad scales has total >= c_std(M)*(m+1).
c_std = 0.03
for m in [4, 10, 20, 100]:
    debt = c_std * (m + 1)
    print(
        f"m={m}: schematic standard-channel debt >= {debt:.6g}, "
        f"average >= {debt/(m+1):.6g}"
    )

print(
    "\nLogical branch:\n"
    "R_scale -> [uniform full critical bound -> linear CKN gap debt] "
    "OR [full critical bound failure -> critical-reservoir/state escape]."
)
