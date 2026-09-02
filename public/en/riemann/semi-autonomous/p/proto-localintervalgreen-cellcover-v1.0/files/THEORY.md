# Theory

## 1. Abstract Space and Position Family

Following the even clamped space of the parent node, the radius is $R=16$, and the tail scale is

$$
\eta=\frac{31794183142988}{10^{18}}.
$$

Under the structural conditions

$$
\int_{-R}^{R}\psi(t)\,dt=0,
\qquad
\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt=0
$$

the test density on the axis is

$$
\phi_x(t)=\cos(xt).
$$

The five frequency bands yield a total of $58$ rational centers $c_j$. v1.0 studies the independent position variables

$$
x_j=c_j+\delta_j,
\qquad
|\delta_j|\le h.
$$

The two complex atoms in the core remain fixed; the positive and negative core weights use the sub-parameter $\alpha=1$.

## 2. Green Pairing

For the complex exponential $e^{zt}$, let $L^{-1}$ be the inverse of the clamping operator $\eta D^4$. The fundamental bilinear pairing is written as

$$
K(z,w)
=
\int_{-R}^{R}
e^{zt}\,L^{-1}(e^{w\cdot})(t)\,dt.
$$

The particular solution of the right-hand side equation and the cubic correction satisfying the four endpoint conditions can be expressed in closed form using a finite number of exponential moments

$$
M_p(z)
=
\int_{-R}^{R}t^p e^{zt}\,dt,
\qquad 0\le p\le4.
$$

For exponential boxes that do not cross zero, we use integration by parts recursively:

$$
M_p(z)
=
\frac{R^p e^{zR}-(-R)^p e^{-zR}}{z}
-\frac{p}{z}M_{p-1}(z).
$$

## 3. Analytic Enclosure of Zero-Crossing Moments

Positive and negative exponentials at the same position will produce $i x_j-i x_j=0$. If interval arithmetic is applied directly to $1/z$, the certificate will fail near zero. Therefore, for exponential boxes that simultaneously cross real and imaginary zeros, v1.0 uses

$$
M_p(z)
=
\sum_{k=0}^{N}
\frac{z^k}{k!}\mu_{p+k}
+E_{N,p}(z),
$$

where

$$
\mu_m
=
\int_{-R}^{R}t^m\,dt
=
\begin{cases}
0,&m\text{ is odd},\\
\dfrac{2R^{m+1}}{m+1},&m\text{ is even}.
\end{cases}
$$

If $|z|\le Z$, we adopt the directly computable remainder bound

$$
|E_{N,p}(z)|
\le
\frac{2R^{p+1}}{p+1}
e^{ZR}
\frac{(ZR)^{N+1}}{(N+1)!}.
$$

This package takes $N=28$. All trigonometric, exponential, division, and matrix operations are performed under $90$-decimal-digit directed rounding.

## 4. Affine Labels and Dependencies

Each exponential stores a center and named perturbations:

$$
z=z_0+\sum_j a_j\delta_j.
$$

Thus, the linear cancellation of the same named variable is completed before conversion to a rectangular interval. For example,

$$
i(c_j+\delta_j)-i(c_j+\delta_j)=0
$$

is an exact equality and will not be erroneously relaxed to $[-2h,2h]$. The $\delta_j$ at different positions remain independent.

## 5. Structural Projection

Let $S$ be the Green–Gram matrix of the two structural densities, $B$ be the cross matrix between the structural densities and all $62$ evaluation densities, and $G$ be the unprojected Gram matrix. After projection,

$$
G^\perp=G-B^\mathsf{T}S^{-1}B.
$$

$S$ is a fixed $2\times2$ interval matrix; the lower bound of its determinant is strictly positive. The projected Gram matrix contains $60$ positive directions and $2$ negative directions.

## 6. Low Negative Rank Schur Criterion

Partition $G^\perp$ into positive and negative blocks, and denote the positive and negative weight diagonal matrices as $D_+$ and $D_-$, respectively. Let

$$
A=I+G_{++}D_+,
\qquad
X=A^{-1}G_{+-}.
$$

Finally, it suffices to verify that

$$
T
=
D_-^{-1}
-G_{--}
+G_{-+}D_+X
$$

is positive definite. The candidate inverse $R$ is generated from the floating-point midpoint matrix, but the proof only uses its decimal string as an exact rational candidate. If

$$
\|I-RA\|_\infty<1,
$$

then the Neumann series provides a strict interval enclosure for $A^{-1}$ and $X$. Since $T$ is only $2\times2$, the Sylvester criterion reduces to

$$
T_{11}>0,
\qquad
\det T>0.
$$

## 7. Monotonic Inheritance of the Covering Family

The main certificate encloses the maximal Cartesian product box at once:

$$
\mathcal B_h
=
\prod_{j=1}^{58}[c_j-h,c_j+h].
$$

If every closed subinterval $J_j$ satisfies

$$
J_j\subseteq[c_j-h,c_j+h],
$$

then

$$
\prod_{j=1}^{58}J_j\subseteq\mathcal B_h.
$$

The universal quantifier of the main certificate thus automatically covers all such rational sub-boxes, forming a downward-closed family of certificates; there is no need for an exponentially large enumeration of leaf nodes.