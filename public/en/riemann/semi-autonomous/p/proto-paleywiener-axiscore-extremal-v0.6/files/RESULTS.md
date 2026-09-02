# Results

## 1. Simplified exact extremal

The one-axis-point, one-core-point model has a closed rank-two formula. For the central core point

$$
z=20.4075-0.103125i
$$

a point scan is performed for each band. The results at the finest time step are:

| band | best one-point lower bound | $x$ |
|---|---:|---:|
| $A_0$ | $0.111322$ | $17.85$ |
| $A_1$ | $0.261253$ | $20.30$ |
| $A_2$ | $0.111224$ | $23.15$ |
| $A_3$ | $0.111034$ | $35.15$ |
| $A_4$ | $0.111031$ | $70.65$ |

All single-band values are less than $1$. Therefore, the obstruction in v0.5 is not caused by any single band independently, but rather by the measure interaction across all five bands.

## 2. Galerkin convergence

| raw dimension | effective dimension | raw $\alpha$ |
|---:|---:|---:|
| $24$ | $22$ | $7.788239$ |
| $40$ | $38$ | $3.679471$ |
| $64$ | $62$ | $1.588306$ |
| $80$ | $78$ | $1.300399$ |
| $96$ | $94$ | $1.184647$ |
| $120$ | $118$ | $1.159914$ |
| $144$ | $142$ | $1.139122$ |
| $160$ | $158$ | $1.133508$ |
| $176$ | $174$ | $1.132795$ |
| $192$ | $190$ | $1.132475$ |

The sequence decreases monotonically and begins to plateau. The last row yields

$$
\alpha_{\rm safe}=1.0662376,
$$

$$
\lambda_{\min}(W_{\rm safe})=0.2569999.
$$

However, Galerkin PSD itself still does not imply continuous PSD.

## 3. Independent point-kernel agreement

For the $A_1$ simplified extremal at $x=20.4$ and the central core point:

$$
\Lambda_{\rm Galerkin,192}
=0.1124416819495,
$$

$$
\Lambda_{\rm Green,\Delta t=0.0025}
=0.1124416808961.
$$

The absolute difference is

$$
1.05\times10^{-9}.
$$

The difference between Gauss–Legendre orders 1,024 and 2,560 is also within approximately
$2.4\times10^{-10}$.

## 4. Direct continuous-kernel atomic transfer

The raw dimension 192 measures contain:

$$
58\ \text{axis atoms}+2\ \text{core atoms}.
$$

The same measures evaluated in the direct clamped Green solver yield:

| $\Delta t$ | raw threshold |
|---:|---:|
| $0.02$ | $1.1324314430$ |
| $0.01$ | $1.1324406087$ |
| $0.005$ | $1.1324411657$ |
| $0.0025$ | $1.1324411997$ |

At the v0.6 safe alpha,

$$
\alpha_{\rm safe}=1.0662376054,
$$

the full finite-span minimum eigenvalue is

$$
0.2568265725,
$$

while the equivalent $2\times2$ Schur certificate minimum is

$$
0.0560870811.
$$

This is a dictionary-independent continuous-kernel floating obstruction.

## 5. Rational candidate at $\alpha=21/20$

After rationalizing the supports and weights, at

$$
\alpha=\frac{21}{20}=1.05
$$

we obtain

$$
\lambda_{\min}(W)=0.3122432495,
$$

$$
\lambda_{\min}(S)=0.0698852338.
$$

The Schur minimum drift between the last two time steps is approximately

$$
2.68\times10^{-8}.
$$

This drift is merely a convergence diagnostic, not an interval bound.

## 6. Research decision

v0.6 has achieved the decision objective of continuization:

- The obstruction no longer depends on the v0.5 local bump dictionary;
- There is no need to further increase the Galerkin dimension;
- The next valuable task is to interval-enclose a 60-positive-rank,
  2-negative-rank witness;
- The certificate target is fixed at $\alpha=1.05$, and we will no longer pursue a higher floating alpha.

The next node is
`RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`.