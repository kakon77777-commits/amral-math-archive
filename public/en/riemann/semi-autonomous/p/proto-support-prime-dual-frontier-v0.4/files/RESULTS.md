# Results

## Conclusion

Currently, the support-only dictionary still fails to pass the dual gate even when sampled up to $R=16$.
All four candidate radii have at least one hard sub-rectangle blocked by the safe lower bound.

| $R$ | dimension | Strongest $\alpha_{\rm safe}$ | PSD margin |
|---:|---:|---:|---:|
| $10.25$ | $100$ | $2.620080$ | $0.0713394$ |
| $12$ | $118$ | $1.899950$ | $0.0834713$ |
| $14$ | $138$ | $1.398180$ | $0.0992519$ |
| $16$ | $158$ | $1.094281$ | $0.1149902$ |

`outputs/witness_verification.json` reconstructs 12 serialized witnesses, all of which remain
PSD and have an effective lower bound greater than $1$.

## Coarse-grid false escapes

Fixing $R=16$ and patch `x4_Y3__r2_3`:

| axis step | raw $\alpha$ | safe $\alpha$ |
|---:|---:|---:|
| $0.25$ | $0.985277$ | $0.980351$ |
| $0.1$ | $1.124306$ | $1.062153$ |
| $0.05$ | $1.139551$ | $1.069775$ |
| $0.025$ | $1.192293$ | $1.096146$ |

Therefore, a coarse-grid pass cannot serve as evidence of primal feasibility.

## Uniform frontier

- 126 sets: 14 radii × 3 densities × 3 width factors.
- First sampled center-only uniform escape: $R=10$.
- First sampled original-patch uniform $3\times3$ escape: $R=14$.
- Joint measure optimization re-blocks the optimistic transitions mentioned above.

## Prime cost

At $R=10.25$, actual enumeration yields:

$$
\pi(799{,}902{,}177)=41{,}141{,}456
$$

and $41{,}144{,}807$ prime-power terms. Up to $R=16$, the strict
cutoff is

$$
78{,}962{,}960{,}182{,}680,
$$

with the $x/\log x$ prime proxy being approximately $2.47\times10^{12}$.

## Decision

Increasing $R$ will no longer be the primary direction. The next node will jointly design axis notches, the dictionary,
and the cover, and will require any result with $\alpha<1$ to undergo a dense-axis audit.