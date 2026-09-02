# Results

## 1. Layer A interval certificate

Fixed data:

| Item | Value |
|---|---:|
| radius | $16$ |
| target | $\alpha=21/20$ |
| axis atoms | $58$ |
| core atoms | $2$ |
| positive rank | $60$ |
| negative rank | $2$ |
| decimal precision | $90$ |

Core enclosure:

| Check | rigorous bound |
|---|---:|
| structural determinant lower | $6.087163164690596\times10^{20}$ |
| maximum projected Gram width | $3.71216\times10^{-84}$ |
| Neumann defect upper | $7.531404753645390\times10^{-15}$ |
| solution radius, column $1$ | $6.479135069600651\times10^{-16}$ |
| solution radius, column $2$ | $2.881263499141683\times10^{-16}$ |
| first Sylvester minor lower | $0.3524279496453903$ |
| determinant lower | $0.0636153172597786$ |

Conclusion:

$$
W_{21/20}\succ0
$$

in the abstract continuous model explicitly defined by the package.

## 2. Floating cross-check

Converting the interval midpoint back to the scaled Schur convention of v0.6 yields

$$
\lambda_{\min}^{\mathrm{mid}}
\approx
0.06988523568969546.
$$

The finest time-grid diagnostic in v0.6 is

$$
\lambda_{\min}^{\mathrm{grid}}
\approx
0.06988523379762435.
$$

The difference is approximately

$$
1.8921\times10^{-9}.
$$

This comparison is for cross-diagnostic purposes only; the proof itself does not use this difference.

## 3. Coefficient orientation

Let

$$
B(T)
=
0.112\log T
+0.278\log\log T
+2.510.
$$

| band | stored coefficient | lower count from $|S|$ only | profile |
|---|---:|---:|---|
| $A_0=[14,18]$ | $6.797423271048$ | $0$ | upper |
| $A_1=[18,23]$ | $7.246636980606$ | $0$ | upper |
| $A_2=[23,35]$ | $9.346770522330$ | $0$ | upper |
| $A_3=[35,70]$ | $18.367573606596$ | $5.069962795569$ | upper |
| $A_4=[70,145]$ | $40.545362729236$ | $26.742367141539$ | upper |

All five stored coefficients conform to the downward-rounded upper profile; none are directly guaranteed to be positive lower coefficients by the current absolute-$S$ argument.

## 4. Orientation stress test

Retaining the atoms, probability weights, core measure, kernel, and $\alpha=21/20$, we only replace the five band coefficients with the lower profile mentioned above.

The resulting floating Schur eigenvalues are approximately

$$
-5.53605304212116
$$

and

$$
0.942631731149592.
$$

Therefore, the original fixed witness does not survive this substitution. This is not an interval theorem stating that "no possible witness exists"; it merely proves that in the next iteration, one cannot mechanically replace the upper coefficients with the lower coefficients and declare completion.

## 5. Research assessment

v0.7 successfully closed four v0.6 gaps:

- interval Green pairings;
- structural projection enclosure;
- verified positive solve;
- final Schur positivity.

However, the coefficient orientation audit exposed the true next bottleneck in advance:

$$
\text{continuous numerical legitimacy}
\neq
\text{zeta coefficient legitimacy}.
$$

Therefore, the next iteration will not first expand to the full covering family, but will instead first establish a robust count coefficient bridge.