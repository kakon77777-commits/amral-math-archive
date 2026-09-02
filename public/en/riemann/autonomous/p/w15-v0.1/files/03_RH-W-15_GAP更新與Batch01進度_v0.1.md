# RH-W-15: GAP Update and Batch 01 Progress

## Closed Nodes

### `RH-W-15-ARCH-SUPPORT-EXTERIOR-TAIL`

Identified and corrected the tail integral left outside the spline support by the Archimedean normalization constant:

$$
\operatorname{artanh}(e^{-R}).
$$

### `RH-W-15-W14-RE-AUDIT`

Re-audited RH-W-14 using the corrected first derivative bounds; the original 2D small tube conclusion is retained.

### `RH-W-15-SECOND-DERIVATIVE-BOUNDS`

Established rational global bounds for the second derivatives of the degree-$3/5/7$ Weil centers:

$$
2494,
\qquad3110,
\qquad3697.
$$

### `RH-W-15-BILINEAR-TUBE`

Established four-corner interval matrices, bilinear convex combinations, and second-order remainder certificates, expanding the parameter radius to $10^{-7}$.

### `RH-W-15-CONTINUOUS-BRACKET`

Proved for the entire new rectangle:

$$
10^{-8}<\lambda_{\min}<5\times10^{-8}.
$$

## Open Nodes

### `RH-W-15-ANISOTROPIC-MAX-TUBE`

Currently adopting

$$
\rho_d=\rho_\sigma=10^{-7}.
$$

The maximum provable radii in the $d$ and $\sigma$ directions have not yet been determined, nor has the actual block sparsity of the Hessian been utilized for anisotropic expansion.

### `RH-W-15-H-DIRECTION`

The scale $h$ is still fixed. After incorporating $h$, the spline knots, sample normalizations, endpoint integrals, and Gram matrices will all vary simultaneously, requiring a 3D Taylor certificate.

### `RH-W-15-HESSIAN-SIGN-STRUCTURE`

Currently, the second-order remainder still uses element-wise absolute value upper bounds. The sign, Toeplitz, and block structures of the Hessian matrix have not yet been preserved.

## Batch 01 Progress

The first batch is fixed as:

$$
\texttt{RH-W-01}\sim\texttt{RH-W-20}.
$$

The current round is:

$$
\boxed{15/20}.
$$

Remaining plan:

1. `RH-W-16`: Incorporate $h$ and establish a 3D parameter box;
2. `RH-W-17`: Chamber-aware automatic subdivision;
3. `RH-W-18`: Unification of the certificate backend;
4. `RH-W-19`: Adversarial and reproducibility audit;
5. `RH-W-20`: Batch 01 integration, website data, and handover package.

This round does not change the overall status of RH:

$$
\boxed{\text{RH remains open.}}
$$