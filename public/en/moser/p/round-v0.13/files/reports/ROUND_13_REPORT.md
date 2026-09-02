# Semi-Autonomous Research on Moser Skew Field: Round 13

## ——Smooth Five-Parameter Event—KKT System, Isolation, and Peak Correction

**Date:** July 26, 2026  
**Status:** Numerical event—KKT reconstruction; Non-interval KKT certificate; Informal proof  
**Continuation:** Moser Skew Lab v0.12

---

# 1. Twelve-Variable System

The curve parameters are:

$$
p=(w,\beta,\delta,c,\varepsilon).
$$

The control branches are:

$$
m_1(p,\phi_1),\quad
m_2(p,\phi_2),\quad
m_3\left(p,\frac{2\pi}{3}\right),\quad
m_4\left(p,\frac{3\pi}{2}\right).
$$

The unknowns are:

$$
(w,\beta,\delta,c,\varepsilon,\phi_1,\phi_2,s,\mu_1,\mu_2,\mu_3,\mu_4),
$$

for a total of $12$.

The equations are:

$$
m_r-s=0,\qquad r=1,\ldots,4,
$$

$$
\partial_\phi m_1=\partial_\phi m_2=0,
$$

$$
\sum_r\mu_r\nabla_p m_r=0,
$$

$$
\sum_r\mu_r=1.
$$

---

# 2. Five-Parameter Candidate

$$
w=0.336104284558314,
$$

$$
\beta=1.405407705040992,
$$

$$
\delta=0.052008500382349,
$$

$$
c=0.580164729946572,
$$

$$
\varepsilon=0.036823344353076.
$$

Angles:

$$
\beta=80.523929994016^\circ,
\qquad
\delta=2.979867570713^\circ,
$$

$$
\alpha=83.503797564729^\circ.
$$

Central segment:

$$
l_0=0.327791430883373.
$$

---

# 3. Four-Branch Equal Height

| Branch | Phase | High-Precision Recalculated Value |
|---|---:|---:|
| B1 low | 0.154865921088826 | 0.998914343297489 |
| B2 low | 0.123902822042353 | 0.998914343297485 |
| 120° | 2.094395102393195 | 0.998914343297542 |
| 270° | 4.712388980384690 | 0.998914343297542 |

Common scale:

$$
\boxed{
s_{13}=0.998914343297485
}
$$

Branch difference:

$$
5.739853037312e-14.
$$

Relative to Round 8:

$$
\boxed{
s_{13}-s_8=4.212852400265e-09
}
$$

Distance to certified scale:

$$
1-s_{13}=1.085656702515e-03.
$$

This gain is approximately $4.21\times10^{-9}$. Its significance lies in the correction of the peak position, rather than a new geometric breakthrough.

---

# 4. Parameter Corrections

$$
\Delta w=-1.486912894477e-06,
$$

$$
\Delta\beta=2.491020159856e-05,
$$

$$
\Delta\delta=-3.884868046042e-05,
$$

$$
\Delta c=-1.343693920453e-05,
$$

$$
\Delta\varepsilon=-1.766556469240e-04.
$$

The most prominent correction is:

$$
0.037
\longrightarrow
0.036823344353076.
$$

---

# 5. Branch Pressures

| Branch | Pressure |
|---|---:|
| B1 low | 0.0282523300 |
| B2 low | 0.0283757600 |
| 120° | 0.7360431600 |
| 270° | 0.2073287400 |

The $120^\circ$ branch bears approximately $73.6\%$ of the pressure, and the $270^\circ$ branch bears about $20.7\%$.

---

# 6. Five-Parameter Gradients

| Branch | $\partial_w$ | $\partial_\beta$ | $\partial_\delta$ | $\partial_c$ | $\partial_\varepsilon$ |
|---|---:|---:|---:|---:|---:|
| B1 low | -2.865884868 | -0.248527131 | -0.010715915 | -0.006727360 | -0.007779309 |
| B2 low | -2.793250780 | -0.268319607 | -0.019829414 | -0.025109379 | -0.007772916 |
| 120° | 0.261986134 | 0.095277667 | 0.047078423 | 0.005108074 | 0.000473420 |
| 270° | -0.157260180 | -0.267658292 | -0.162960229 | -0.013781158 | 0.000443204 |

Weighted stationary residual:

```text
[7.92303109024174e-09, -2.4601682404565255e-08, -1.2172673240943544e-08, -2.8343874670266987e-08, 7.059235300514802e-10]
```

Norm:

$$
4.025002772641e-08.
$$

This residual is limited by finite differences and curve integral interpolation, and cannot be considered an interval KKT proof.

---

# 7. Mechanism of Four Branches Controlling Five Parameters

The four-branch equal height condition provides three independent difference equations; the equal-height set locally retains two tangential degrees of freedom.

The projection of the common scale gradient onto this two-dimensional tangent space is approximately:

$$
2.7\times10^{-9}.
$$

Therefore, there is currently no identifiable first-order ascent direction.

---

# 8. Jacobian Isolation

Full Jacobian:

$$
12\times12.
$$

Numerical rank:

$$
\boxed{
\operatorname{rank}J=12.
}
$$

Minimum singular value:

$$
1.139753650e+01.
$$

Condition number:

$$
\kappa(J)\approx3.766322538e+07.
$$

The system is full rank but highly ill-conditioned. Therefore, it supports numerical isolation but does not support a robust conclusion of interval invertibility.

---

# 9. Local Basin

Re-solving with $20$ sets of random five-parameter perturbations nearby:

$$
\boxed{
20/20
}
$$

All returned to the same scale basin.

Scale range:

$$
[0.998914343297213,\ 0.998914343297252].
$$

Maximum parameter distance:

$$
3.900000000000e-07.
$$

---

# 10. Curvature Ledger

Total turning angle:

$$
\int|\kappa|\,ds\approx0.052008500382.
$$

Peak curvature:

$$
\|\kappa\|_\infty\approx2.101101621113.
$$

$5\%$ to $95\%$ turning width:

$$
W_{5\%-95\%}\approx0.036441801352.
$$

The candidate remains a finite-width, finite-peak curvature layer.

---

# 11. Full Phase Audit

The full phase landscape still has $8$ local minima.

Outside the four control branches, the lowest of the other local minima is approximately:

$$
1.02935,
$$

which is far above the common scale. No new low branches introduced by the five-parameter correction were found.

---

# 12. Verdict

Round 13 supports:

$$
\boxed{
\text{The smooth candidate from Round 8 can be corrected into a
five-parameter event—KKT numerically isolated candidate.}
}
$$

Its scale is approximately:

$$
\boxed{
0.99891434329749.
}
$$

---

# 13. Limitations

1. Parameter gradients use finite differences;
2. The full rank of the Jacobian is a floating-point diagnostic;
3. The system condition number is high;
4. The $12\times12$ Krawczyk/interval Newton method has not yet been completed;
5. Arb replay has not yet been completed;
6. No new Moser area upper and lower bounds have been proposed;
7. No formal proof has been conducted.

---

# 14. Directions for Round 14

Stop fine-tuning the unimodal tanh curvature layer, and instead test curvature distributions:

1. Bimodal curvature layers;
2. Asymmetric curvature on the left and right wings;
3. Biarc/piecewise constant curvature;
4. Congruent bichiral targets;
5. New contact branches and new pressure ledgers.

Any candidate must exceed:

$$
s_{\mathrm{base}}=0.99891434329749
$$

and pass the full phase and bichirality review.

---

# 15. Conclusion

$$
\boxed{
s_{13}=0.998914343297485
}
$$

$$
\boxed{
\varepsilon=0.036823344353076
}
$$

$$
\boxed{
\operatorname{rank}J=12.
}
$$

The most accurate description at present is:

$$
\boxed{
\text{A finite-width tanh curvature layer,
forming a numerically isolated,
yet highly ill-conditioned minimax candidate within the five-parameter family.}
}
$$