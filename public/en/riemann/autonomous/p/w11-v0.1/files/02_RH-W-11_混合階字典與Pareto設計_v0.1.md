# RH-W-11: Mixed-Order Dictionary and Pareto Design v0.1

- Node: `RH-W-11-MIXED-KERNEL-PARETO`
- Date: 2026-07-23
- Status: Design specification completed; real mixed-order Weil matrix reserved for `RH-W-12`

---

## 1. Why a Single Kernel is Insufficient

If we only consider prime boundary sensitivity, the lowest-order kernel is best; if we only consider tail bounds and frequency-domain decay, the highest-order kernel is best. The two objectives are contradictory:

$$
\text{boundary sensitivity}
\quad\leftrightarrow\quad
\text{certification regularity}.
$$

Therefore, kernel selection should not be compressed into a single ranking.

This project adopts the Pareto principle: we only eliminate kernels that are simultaneously worse in sensitivity, regularity, tail bound cost, and numerical conditioning. For the current B-spline families of $m=0,1,2,3,4,5$, no single kernel dominates the rest across all metrics.

---

## 2. Proposed Dual-Channel Kernel

The first version of the mixed-order dictionary selection is:

$$
\boxed{m=1\quad\text{and}\quad m=3}.
$$

### Sensing Channel: $m=1$

The autocorrelation of the linear B-spline is degree-$3$:

$$
\beta_1*\beta_1=\beta_3.
$$

The prime boundary appears as

$$
\varepsilon^3
$$

which, for the penetration depth of `RH-W-10`, can produce prime-$3$ local elements of approximately $10^{-11}$.

This is about sixteen orders of magnitude larger than the $10^{-28}$ of the cubic autocorrelation, while still maintaining a continuous basis and a $C^2$ correlation kernel.

### Certificate Channel: $m=3$

The autocorrelation of the cubic B-spline is degree-$7$:

$$
\beta_3*\beta_3=\beta_7.
$$

Its prime boundary sensitivity is low, but:

- The correlation kernel is $C^6$;
- The Fourier decay is $|\xi|^{-8}$;
- The Archimedean Laplace tail can be expanded using higher-order derivatives;
- Existing programs from `RH-W-05` to `RH-W-10` can be reused.

---

## 3. Cross-Channels Automatically Form Intermediate Orders

The most valuable aspect of a mixed dictionary is not simply concatenating two sets of bases, but that cross-correlation automatically generates a third layer:

$$
\beta_1*\beta_3=\beta_5.
$$

Thus, the correlation degrees in the $m=1/3$ mixed dictionary are:

| Pairing | Correlation Degree | Prime Activation Order | Boundary Regularity |
|---|---:|---:|---:|
| $1\times1$ | 3 | 3 | $C^2$ |
| $1\times3$ | 5 | 5 | $C^4$ |
| $3\times3$ | 7 | 7 | $C^6$ |

Therefore, the same matrix naturally contains:

$$
\boxed{
\varepsilon^3,
\quad
\varepsilon^5,
\quad
\varepsilon^7
}
$$

three arithmetic sensing scales.

This is better than "first using a low order to find candidates, then completely switching to a high-order basis for verification", because different scales are coupled within the same Hermitian matrix, allowing the lowest mode to autonomously select the required sensitivity layer.

---

## 4. Mixed-Order Block Toeplitz Structure

For the same translation grid

$$
t_j=jd,
$$

define two families of bases:

$$
v^{(1)}_j=v_{1,h,t_j},
\qquad
v^{(3)}_j=v_{3,h,t_j}.
$$

If each family has $N$ translations, the complete Weil matrix is a $2N\times2N$ block Toeplitz:

$$
M=
\begin{pmatrix}
M^{11} & M^{13}\\
M^{31} & M^{33}
\end{pmatrix},
$$

where:

$$
M^{11}_{ij}\leftrightarrow\beta_3,
$$

$$
M^{13}_{ij}\leftrightarrow\beta_5,
$$

$$
M^{33}_{ij}\leftrightarrow\beta_7.
$$

The Gram matrix has the same block structure:

$$
G=
\begin{pmatrix}
G^{11} & G^{13}\\
G^{31} & G^{33}
\end{pmatrix}.
$$

Each block depends only on the lag $i-j$, so there is no need to recompute $O(N^2)$ mutually uncorrelated elements; one only needs to compile a finite lag table for each block.

---

## 5. Certificate Contract for `RH-W-12`

The real matrix in the next iteration must simultaneously satisfy:

### 5.1 Complete Explicit Formula

Each $M^{ab}_{ij}$ must be decomposed into:

$$
\text{endpoint/pole}
+
\text{constant}
+
\text{Archimedean}
+
\sum_{p^k}\text{prime-power sample}.
$$

It cannot merely compute the local prime block.

### 5.2 Complete Prime-Power Enumeration

For each cross-correlation support, it must be proven:

- Which $\pm\log p^k$ are located within the support;
- Which spline piece they are located in;
- That their intervals do not cross knots or support boundaries.

### 5.3 Exact Gram

Due to the convolution closure of B-splines, the Gram elements can be given exactly by the values of the corresponding $\beta_{m+n+1}$ at the lag points.

### 5.4 Spectral Criterion

The exploration layer may use floating-point generalized eigenvalues; the formal layer must use:

$$
C-\delta G-E\succ0
$$

via a purely rational $LDL^T$, or prove for a rational witness that:

$$
c^TMc<0.
$$

### 5.5 Conclusions That Cannot Be Output

Even if the $2N\times2N$ mixed matrix is positive definite, it can only output:

$$
\texttt{CERTIFIED\_POSITIVE\_ON\_THIS\_MIXED\_SUBSPACE}.
$$

It cannot output RH.

---

## 6. New GAPs

### `RH-W-12-CROSS-ARCH`

Requires generalizing the current Archimedean integrator dedicated to degree-$7$ to degrees-$3,5,7$.

### `RH-W-12-CROSS-PRIME`

Requires the prime-power compiler to automatically use different support radii and knot tables according to the block.

### `RH-W-12-GRAM-CONDITION`

Near-linear dependence may appear after mixing different degrees; $G\succ0$ and the condition number must be strictly controlled.

### `RH-W-12-MODE-ATTRIBUTION`

If the lowest mode drops, its energy ratio in the $m=1$ and $m=3$ channels needs to be decomposed to avoid misinterpreting cross-coupling as a single prime event.

### `RH-W-12-COMPLETENESS`

A mixed dictionary with fixed $h,d,N$ is still finite-dimensional. To form an enumerable complete family, one must simultaneously design:

$$
h\downarrow0,
\qquad
N\uparrow\infty,
\qquad
\text{support range expansion}.
$$

---

## 7. Design Conclusion

The next-generation dictionary will no longer have just a single smoothness, but rather a "kernel ladder":

$$
\boxed{
\text{Low orders see events,}
\quad
\text{high orders suppress tail terms,}
\quad
\text{cross orders connect the two.}
}
$$

This is not complicating the numerical method, but acknowledging that sensing and certification in Weil geometry are inherently two distinct tasks.