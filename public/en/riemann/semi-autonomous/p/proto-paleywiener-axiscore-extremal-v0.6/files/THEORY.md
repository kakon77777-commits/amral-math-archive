# Theory

## 1. Continuous tail Hilbert space

Fix $R>0$ and $\kappa_R>0$. Let

$$
\mathcal H_R
=\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t)
\right\},
$$

where $H_0^2$ takes the clamped trace:

$$
\psi(\pm R)=\psi'(\pm R)=0.
$$

Define

$$
\langle\psi,\phi\rangle_T
=\kappa_R\int_{-R}^{R}\psi''(t)\phi''(t)\,dt.
$$

By the clamped Poincaré inequality, this is a Hilbert norm. Let

$$
G_\psi(z)
=\int_{-R}^{R}\psi(t)e^{izt}\,dt.
$$

$G_\psi$ is an entire function of exponential type at most $R$. The evaluation at each fixed $z$ is continuous on $\mathcal H_R$.

The structural subspace is

$$
\mathcal H_R^0
=\left\{
\psi\in\mathcal H_R:
G_\psi(0)=G_\psi(i/2)=0
\right\}.
$$

Since $\psi$ is even,

$$
G_\psi(i/2)
=\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt.
$$

## 2. Evaluation representers

For real $x$, let $p_x\in\mathcal H_R^0$ be such that

$$
\langle\psi,p_x\rangle_T=G_\psi(x).
$$

For $z=x+iy$, let $u_z,v_z\in\mathcal H_R^0$ represent $\operatorname{Re}G_\psi(z)$ and $\operatorname{Im}G_\psi(z)$, respectively. Their densities are

$$
f_z^{\rm re}(t)=\cos(xt)\cosh(yt),
$$

$$
f_z^{\rm im}(t)=-\sin(xt)\sinh(yt).
$$

Define the rank-one/rank-two operators

$$
P_x=p_x\otimes p_x,
$$

$$
C_z
=2\left(u_z\otimes u_z-v_z\otimes v_z\right).
$$

Then

$$
\langle\psi,P_x\psi\rangle_T=G_\psi(x)^2,
$$

$$
\langle\psi,C_z\psi\rangle_T
=2\operatorname{Re}G_\psi(z)^2.
$$

## 3. Trace-class primal

Let $\mathcal A_j$ be five real-axis bands, $\mathcal P$ be the target core patch, and $N_j>0$ be the specified count coefficients. Consider

$$
\begin{aligned}
\Lambda_R=\inf\quad&
\operatorname{Tr}(A)+\sum_{j=0}^{4}N_js_j\\
\text{subject to}\quad&
A\succeq0,\qquad A\in\mathcal S_1(\mathcal H_R^0),\\
&\operatorname{Tr}(P_xA)\le s_j
\quad(x\in\mathcal A_j),\\
&\operatorname{Tr}(C_zA)\le-1
\quad(z\in\mathcal P).
\end{aligned}
$$

Finite multi-test Gram matrices are finite-rank instances of this problem.

## 4. Measure dual and weak duality

Let each $\mu_j$ be a probability measure on $\mathcal A_j$, and $\nu$ be a probability measure on $\mathcal P$. If

$$
W
=I+\sum_{j=0}^{4}N_j\int_{\mathcal A_j}P_x\,d\mu_j(x)
+\alpha\int_{\mathcal P}C_z\,d\nu(z)
\succeq0,
$$

then for every primal-feasible $A$,

$$
\operatorname{Tr}(WA)\ge0.
$$

On the other hand,

$$
\begin{aligned}
\operatorname{Tr}(WA)
&=\operatorname{Tr}(A)
+\sum_jN_j\int\operatorname{Tr}(P_xA)\,d\mu_j(x)\\
&\quad+\alpha\int\operatorname{Tr}(C_zA)\,d\nu(z)\\
&\le\operatorname{Tr}(A)+\sum_jN_js_j-\alpha.
\end{aligned}
$$

Therefore,

$$
\Lambda_R\ge\alpha.
$$

This is continuous weak duality. It only requires a dual-feasible measure witness and does not require strong duality.

## 5. One-axis/one-core closed form

Fix $x,z$ and $N>0$, and let

$$
B=I+N\,p_x\otimes p_x.
$$

Consider

$$
\inf_{A\succeq0}
\left\{
\operatorname{Tr}(BA):
\operatorname{Tr}(C_zA)\le-1
\right\}.
$$

Let

$$
\widehat u=B^{-1/2}u_z,\qquad
\widehat v=B^{-1/2}v_z,
$$

and

$$
a=\|\widehat u\|^2,\qquad
b=\|\widehat v\|^2,\qquad
c=\langle\widehat u,\widehat v\rangle.
$$

The only possible non-zero eigenvalues of $B^{-1/2}C_zB^{-1/2}$ are

$$
\lambda_\pm
=(a-b)\pm\sqrt{(a+b)^2-4c^2}.
$$

If $\lambda_-<0$, the optimal value is

$$
\Lambda(x,z;N)
=-\frac1{\lambda_-}
=\frac1{
\sqrt{(a+b)^2-4c^2}-(a-b)
}.
$$

By Sherman–Morrison,

$$
a
=\|u_z\|^2
-\frac{N\langle p_x,u_z\rangle^2}
{1+N\|p_x\|^2},
$$

$$
b
=\|v_z\|^2
-\frac{N\langle p_x,v_z\rangle^2}
{1+N\|p_x\|^2},
$$

$$
c
=\langle u_z,v_z\rangle
-\frac{N\langle p_x,u_z\rangle
\langle p_x,v_z\rangle}
{1+N\|p_x\|^2}.
$$

Thus, the entire simplified extremal depends only on six kernel inner products.

## 6. Explicit clamped Green kernel

First, without projecting onto the structural zeros, let

$$
L=2R,\qquad
\xi=s+R,\qquad
\eta=t+R,
$$

$$
a=\min(\xi,\eta),\qquad
b=\max(\xi,\eta).
$$

The clamped bi-Laplacian kernel is

$$
K_{\rm cl}(s,t)
=\frac{
a^2(L-b)^2\left[3bL-(L+2b)a\right]
}{
6L^3\kappa_R
}.
$$

It satisfies

$$
\kappa_R\partial_s^4K_{\rm cl}(s,t)=\delta_t(s)
$$

and the clamped boundary conditions at both ends.

For a density $f$, let

$$
k_f(t)=\int_{-R}^{R}K_{\rm cl}(t,s)f(s)\,ds.
$$

The structural densities are

$$
c_0(t)=1,\qquad c_1(t)=\cosh(t/2).
$$

Let

$$
M_{ij}
=\iint c_i(s)K_{\rm cl}(s,t)c_j(t)\,ds\,dt,
$$

$$
b_f
=\begin{pmatrix}
\langle k_{c_0},k_f\rangle_T\\
\langle k_{c_1},k_f\rangle_T
\end{pmatrix}.
$$

Then the kernel pairing after projecting onto $\mathcal H_R^0$ is

$$
\Gamma(f,g)
=\iint f(s)K_{\rm cl}(s,t)g(t)\,ds\,dt
-b_f^\mathsf TM^{-1}b_g.
$$

## 7. Finite atomic Schur reduction

For finite atomic measures, absorb all axis vectors and positive core-real vectors into

$$
B_\alpha=I+UU^\ast,
$$

and write the core-imaginary negative vectors as the columns of $V$. Then

$$
W_\alpha=B_\alpha-VV^\ast.
$$

Since $B_\alpha\succ0$,

$$
W_\alpha\succeq0
$$

is equivalent to

$$
S_\alpha
=I-V^\ast B_\alpha^{-1}V
\succeq0.
$$

The Woodbury identity gives

$$
S_\alpha
=I-\left[
V^\ast V
-V^\ast U
\left(I+U^\ast U\right)^{-1}
U^\ast V
\right].
$$

The witness for this node has only two core atoms, so $V$ has only two columns, and $S_\alpha$ is $2\times2$. All entries consist solely of explicit $\Gamma(f,g)$, rational weights, and rational coefficients.

This is the complete finitization interface for the v0.7 interval certificate.