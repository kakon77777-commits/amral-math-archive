# Results

## 1. Semantic bridge

| transfer | status |
|---|---|
| count upper $\to$ supremum leakage upper bound | valid |
| count lower $\to$ infimum scalar lower bound | valid |
| count lower $\to$ arbitrary probability average | false |
| upper-envelope lower bound $\to$ actual zero-sum lower bound | false |
| upper-envelope lower bound $\to$ method no-go | valid |

A two-point exact countermodel satisfies

$$
Z=0,\qquad
L\int H\,d\delta_{x_1}=1.
$$

Therefore, the third item is not due to a lack of precision, but rather the general proposition itself is false.

## 2. Five-band floating profiles

| band | lower candidate | upper candidate |
|---|---:|---:|
| $A_0=[14,18]$ | $0$ | $6.797423271049$ |
| $A_1=[18,23]$ | $0$ | $7.246636980607$ |
| $A_2=[23,35]$ | $0$ | $9.346770522331$ |
| $A_3=[35,70]$ | $5.069962795568$ | $18.367573606597$ |
| $A_4=[70,145]$ | $26.742367141539$ | $40.545362729237$ |

The values in the table are floating profiles. The endpoint convention and transcendental directed enclosure have not yet been certified.

## 3. Robust lower-profile search

| raw dimension | effective dimension | optimized $\alpha$ |
|---:|---:|---:|
| $24$ | $22$ | $2.6662663794$ |
| $40$ | $38$ | $1.0616159317$ |
| $64$ | $62$ | $0.4565992248$ |
| $80$ | $78$ | $0.3168124263$ |
| $96$ | $94$ | $0.2363398270$ |
| $120$ | $118$ | $0.1705859126$ |
| $144$ | $142$ | $0.1394428108$ |
| $160$ | $158$ | $0.1301510855$ |
| $176$ | $174$ | $0.1297049092$ |
| $192$ | $190$ | $0.1297047862$ |

The first raw dimension yielding a value below $1$ is $64$. Thus, the low-dimensional

$$
\alpha>1
$$

under the correct lower candidate profile is a clear Galerkin truncation artifact.

## 4. Direct Green transfer

| $\Delta t$ | grid count | threshold |
|---:|---:|---:|
| $0.02$ | $1601$ | $0.1296980713$ |
| $0.01$ | $3201$ | $0.1297028387$ |
| $0.005$ | $6401$ | $0.1297031276$ |

The final value differs from the effective dimension $190$ Galerkin value by less than

$$
1.7\times10^{-6}.
$$

## 5. Sampled primal escape

Under a $101\times101$ core grid and an axis step of $0.01$, after normalization we obtain

$$
\max_{\mathrm{core\ grid}}B=-1
$$

and

$$
\mathcal E_L^{\mathrm{sampled}}
=
0.1297069814.
$$

The sampled maxima of the non-zero bands are approximately

$$
\sup_{A_3}H
\approx
1.00123\times10^{-5},
$$

$$
\sup_{A_4}H
\approx
2.95980\times10^{-8}.
$$

Therefore, the next round should not attempt to fine-tune the original upper-profile witness into a lower-profile obstruction.

## 6. New classification in v0.7

The interval certificate of v0.7 is retained:

$$
W_{21/20}\succ0
$$

It remains a completed abstract continuous theorem.

However, its two external interpretations are now separated:

- upper-envelope method no-go: promising, but still lacks a count/tail source theorem;
- actual zero-side positive obstruction: unproven, and scalar counts are insufficient.

## 7. Prototype relevance

The current patch height is approximately $20.4$. Platt–Trudgian have rigorously verified that all non-trivial $\zeta$ zeros up to a height of $3\cdot10^{12}$ lie on the critical line. Therefore, in this study, this patch can only serve as a functional-analytic prototype, not an unresolved actual off-axis region of $\zeta$.

## 8. Decision

The next data structure can no longer be

$$
[L_j,U_j]
$$

but must be an occupancy/operator-family certificate with positional quantifiers, such as:

$$
\gamma_{jk}\in I_{jk},
\qquad
m_{jk}\ge1,
$$

and, holding jointly for all permissible positions,

$$
W_\alpha(\gamma_{11},\ldots,\gamma_{JK})
\succeq0.
$$

Without positional or local configuration information, the count lower bound can only fall back to the infimum, which typically degenerates to zero.