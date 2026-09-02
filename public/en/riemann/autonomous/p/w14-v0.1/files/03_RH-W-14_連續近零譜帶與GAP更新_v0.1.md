# RH-W-14: Continuous Near-Zero Spectral Band and GAP Update

**Version:** v0.1  
**Date:** 2026-07-23

---

## 1. Closed Sub-nodes

### RH-W-14-GENUINE-PARAMETERS

Distinguished:

- $\alpha$: Congruence change-of-basis gauge, does not change the generalized spectrum;
- $d,\sigma$: Genuinely change the test subspace.

Status: **CLOSED**.

### RH-W-14-WEIL-LIPSCHITZ

Established upper bounds for the Weil central derivative for degrees $3,5,7$ via B-spline global derivative bounds:

$$
L_3\le175,
\qquad
L_5\le215,
\qquad
L_7\le253.
$$

Status: **CLOSED**.

### RH-W-14-GRAM-LIPSCHITZ

Proved:

$$
|\Delta G_{ij}|
\le\frac1h|\Delta c_{ij}|.
$$

Status: **CLOSED**.

### RH-W-14-CHAMBER-STABILITY

Strictly proved that within the entire parameter tube:

- The global prime-power set remains $\{2,3,4\}$;
- The identities of all spline pieces remain unchanged;
- The minimum sample-to-knot distance is greater than $0.02125$.

Status: **CLOSED**.

### RH-W-14-CONTINUOUS-LOWER

Proved:

$$
\lambda_{\min}>10^{-8}
$$

Holds throughout the entire two-dimensional rectangle.

Status: **CLOSED**.

### RH-W-14-CONTINUOUS-UPPER

Proved via a fixed integer witness:

$$
\lambda_{\min}<5\times10^{-8}
$$

Holds throughout the entire two-dimensional rectangle.

Status: **CLOSED**.

---

## 2. Unclosed Sub-nodes

### RH-W-14-H-DIRECTION

Fixed $h$ in this round. A three-dimensional parameter box simultaneously incorporating scale variation has not yet been established.

Status: **OPEN**.

### RH-W-14-LARGE-TUBE

The current tube width is only on the order of $10^{-12}$. This is the scale guaranteed by the global Lipschitz certificate, and does not imply that the true low spectral band must be this narrow.

Status: **OPEN**.

### RH-W-14-TOPOLOGY

The connectivity, number of branches, closedness, or whether the near-zero set forms a surface in a larger parameter domain has not yet been proved.

Status: **OPEN**.

### RH-W-14-DIMENSION-CONTINUATION

The parameter tube certificate has not yet been combined with the dictionary dimension continuation of $N\to N+1$.

Status: **OPEN**.

### TRUE-WEIL-NEGATIVE-WITNESS

Still not found.

Status: **NOT FOUND**.

---

## 3. Significance to the Overall GAP Map

RH-W was originally a working branch of the Weil positivity large GAP. By this round, it has formed the following internal chain:

$$
\text{Fixed test kernel}
\to
\text{Finite matrix}
\to
\text{Prime-power chamber}
\to
\text{Automated search}
\to
\text{Mixed regularity}
\to
\text{Near-zero single point}
\to
\boxed{\text{Strict continuous parameter tube}}.
$$

This still does not close the Weil positivity large GAP, but it has elevated the single-point numerical phenomenon into verifiable local geometric data.

---

## 4. Next Fixed Node

$$
\boxed{
\texttt{RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION}
}
$$

Objectives:

1. Establish first-order matrix derivatives with respect to $d,\sigma$;
2. Establish an interval Hessian for the second-order remainder;
3. Preserve the signs and block structure of the first-order terms;
4. Expand the two-dimensional tube;
5. If computational cost permits, incorporate $h$ to form the first three-dimensional parameter box;
6. Distinguish between "certificate conservativeness" and "true spectral band termination".