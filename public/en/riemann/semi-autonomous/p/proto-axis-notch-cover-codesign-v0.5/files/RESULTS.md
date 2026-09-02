# Results

## Peak atlas

The five-band primary peaks of the 12 parent witnesses are:

| band | interval | primary peak |
|---|---:|---:|
| $A_0$ | $[14,18]$ | $17.83$ |
| $A_1$ | $[18,23]$ | $20.38$ |
| $A_2$ | $[23,35]$ | $23.24$ |
| $A_3$ | $[35,70]$ | $42.18$ |
| $A_4$ | $[70,145]$ | $83.05$ |

The $A_1$ primary peak overlaps with the target real part interval, indicating that the axis burden and the off-axis core are not independent design problems.

## Homogeneous notch screen

At $R=16$, the optimized-core / uniform-axis threshold of the baseline is 0.251927; after adding only the patch-center value notch, it becomes 0.252055, showing no improvement. When both value and derivative notches are required simultaneously, the anchor derivative Frobenius norm drops to approximately $1.07\times10^{-12}$, and the threshold rises to $33.845656$.

At $R=10.25$, `anchor_flat` further rises to $691.837880$. These values are not a proof of the monotonicity theorem, but rather an experimental verification of its expected consequences.

## External lift

uniform/core screen:

| radius | baseline | 6-direction lift |
|---:|---:|---:|
| $10.25$ | $0.999424$ | $0.979093$ |
| $16$ | $0.251927$ | $0.245526$ |

When expanded to 21 frequencies at $R=16$, 15 directions remain effective after constraint and whitening, and the threshold improves by $3.10\%$. However, the joint dual only decreases from

$$
\alpha=1.189562
$$

to

$$
\alpha=1.176230,\qquad
\alpha_{\rm safe}=1.088115>1.
$$

The raw improvement is $1.12\%$, which does not cross the gate.

## Polynomial-bump geometry

The best among the 27 sets of screens is `d12_w2_p5`:

$$
\text{dimension}=190,\qquad
\text{screen threshold}=0.236986.
$$

Its minimum tail eigenvalue is only about $1.15\times10^{-3}$, indicating that the improvement is accompanied by near-zero directions. The joint dual results are:

| geometry | raw $\alpha$ | safe $\alpha$ | safe $\lambda_{\min}$ | raw improvement |
|---|---:|---:|---:|---:|
| baseline | $1.189562$ | $1.094781$ | $0.114990$ | — |
| `d10_w2_p4` | $1.146055$ | $1.073027$ | $0.005438$ | $3.66\%$ |
| `d12_w2_p5` | $1.143522$ | $1.071761$ | $0.001151$ | $3.87\%$ |

All four saved joint objects are reconstructed using serialized measures and maintain $\alpha_{\rm safe}>1$ and PSD; the maximum absolute difference of the reconstructed minimum eigenvalues is approximately $5.15\times10^{-16}$.

## Dense complementary audit

The four rank-one complementary objectives are:

$$
1.275147,\quad1.254665,\quad1.265481,\quad1.263246,
$$

all of which are greater than $1$. The best lift shifts the far-band peaks from approximately $42.3,82.9$ to $41.275,81.875$; the best geometry shifts them to $36.325,73.575$. The $A_1$ charge remains dominant. This is consistent with the stopping rule of the parent node: peak migration cannot be treated as the disappearance of the global burden.

## Decisions

- Stop the purely homogeneous value/derivative notch.
- Stop the current spectral-slope atom family.
- Stop further polynomial-bump density/width/power scaling.
- Do not initiate the primal Gram search, as all safe dual bounds remain greater than $1$.
- Shift the next node to `RH-PaleyWiener-AxisCoreExtremal-20260724-v0.6`.

These conclusions apply only to the explicitly listed finite dictionaries, patches, axis grids, and floating matrices; they do not rule out other external dictionaries, nor do they constitute an obstruction in the continuous function space.