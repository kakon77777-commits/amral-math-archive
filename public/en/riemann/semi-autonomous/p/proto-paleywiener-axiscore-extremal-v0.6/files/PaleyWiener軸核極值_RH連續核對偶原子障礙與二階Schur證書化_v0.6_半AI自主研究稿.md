# Paley–Wiener Axis-Core Extremals

## RH Continuous-Kernel Duality, Atomic Obstructions, and Rank-Two Schur Certification

Version: v0.6  
Date: 2026-07-25  
Research Mode: Semi-AI Autonomous Mathematical Research  
Technical Research Lead: OpenAI Codex  
On-Site Research Authorization and Review: Neo.K / EveMissLab

## Abstract

This node continues the axis-notch co-design from v0.5. The parent node proved that if the notch only shrinks the existing finite Gram space via homogeneous constraints, it is impossible to improve the primal feasibility of the original space; although external spectral lifts and 27 sets of local bump geometries yielded a $1\%$ to $4\%$ improvement, the joint safe dual bounds remained greater than $1$. Therefore, instead of searching for another batch of dictionaries, v0.6 elevates the problem to a continuous Hilbert-space extremal of compact-support entire functions.

This manuscript selects the real-even clamped space

$$
\mathcal H_R^0
\subset H_0^2(-R,R;\mathbb R),
$$

using

$$
\langle\psi,\phi\rangle_T
=\kappa_R\int_{-R}^{R}\psi''(t)\phi''(t)\,dt
$$

as the tail inner product, and imposing

$$
G_\psi(0)=G_\psi(i/2)=0.
$$

The finite multi-test Gram matrix is elevated to a positive trace-class operator on $\mathcal H_R^0$. Real-axis evaluation generates a positive rank-one operator, while off-axis evaluation yields

$$
C_z=2(u_z\otimes u_z-v_z\otimes v_z),
$$

thus the dual of the five-axis-band supremum and the core negativity naturally become probability measures. This paper proves that if

$$
I+\sum_jN_j\int P_x\,d\mu_j(x)
+\alpha\int C_z\,d\nu(z)\succeq0,
$$

then the continuous primal value is at least $\alpha$. This weak-duality obstruction does not require strong duality.

This node also derives a rank-two closed form for the one-axis-point, one-core-point extremal, and provides the clamped bi-Laplacian Green kernel and structural zero projection. The numerical part utilizes two independent paths:

1. nested clamped-even Chebyshev–Galerkin spaces;
2. a direct Green ODE solver for $\kappa_Rk''''=f$.

In the simplified point test, the raw-dimension-192 Galerkin value and the direct Green value differ by only about $1.05\times10^{-9}$. The five-band joint dual monotonically decreases from $7.7882$ at effective dimension $22$ to $1.132475$ at dimension $190$. More crucially: after the final 58 axis atoms and 2 core atoms are directly transferred into the continuous Green RKHS, the dictionary-independent floating threshold converges to

$$
1.1324411997.
$$

At

$$
\alpha_{\rm safe}=1.0662376054
$$

the minimum eigenvalue of the continuous-kernel finite-span matrix is approximately $0.2568266$.

Since the core measure has only two atoms, after absorbing the 60 positive directions, the infinite-dimensional PSD condition is equivalent to a $2\times2$ Schur matrix PSD. Finally, by rationalizing the supports, weights, and target alpha, we fix

$$
\alpha_\star=\frac{21}{20}=1.05.
$$

The floating Schur minimum of this rational candidate is

$$
0.0698852338.
$$

Therefore, v0.6 halts the dictionary and Galerkin expansion. The next node only needs to perform interval enclosure on the explicit Green-kernel pairings, the positive $60\times60$ solve, and the final $2\times2$ Schur matrix.

This node establishes a continuous-kernel floating obstruction, not an interval-certified analytic certificate, and certainly not a proof or disproof of the RH.

## 1. From Finite Dictionary Obstructions to Continuous Problems

### 1.1 The Real Problem Left by v0.5

The strongest conclusion of v0.5 is not the failure of a specific set of notches, but the monotonicity within finite spaces:

$$
V'\subseteq V
\Longrightarrow
\mathcal F(V')\subseteq\mathcal F(V).
$$

If the parent PSD Gram has already searched the complete $V$, then adding

$$
G(a)=0,\qquad G'(a)=0
$$

will only remove directions and will not create new feasible points. This forces a choice in the research trajectory:

- Continue adding external atoms, but with no way to determine when it is sufficient;
- Or directly define a continuous space containing all admissible directions.

v0.6 chooses the latter. This is not an escape from computation by abstracting the numerical problem, but an attempt to answer the most core identifiable question:

> Is the $\alpha>1$ in v0.5 an artificial obstruction of the local bump dictionary, or have the compact support and axis/core geometry themselves already formed a separation in the continuous space?

### 1.2 Why Use Clamped $H_0^2$

The Fourier transform of compact support naturally enters the Paley–Wiener-type entire function framework. On the other hand, the tail penalty of the parent research chain is controlled by the $\psi''$ quadratic form. Therefore, selecting

$$
H_0^2(-R,R)
$$

has three direct advantages:

1. Preserves value/slope boundary compatibility after zero extension;
2. $\|\psi''\|_{L^2}$ is a norm on the clamped domain;
3. The tail quadratic form can directly become a Hilbert identity.

This manuscript does not claim that the defined space is equivalent to some unweighted standard $PW_R^2$. More precisely, it is a Paley–Wiener-type Hilbert space obtained via the Fourier transform of a compact-support Sobolev domain.

## 2. Continuous Tail Space

Fix $R=16$. Let

$$
\mathcal H_R
=\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t)
\right\}.
$$

The clamped traces are

$$
\psi(\pm R)=\psi'(\pm R)=0.
$$

Define

$$
\langle\psi,\phi\rangle_T
=\kappa_R\int_{-R}^{R}
\psi''(t)\phi''(t)\,dt,
$$

where $\kappa_R$ follows the floating tail scale of the parent research chain:

$$
\kappa_R=2R\,\tau_R.
$$

By the clamped Poincaré inequality, $\|\psi''\|_2$ controls $\|\psi\|_2$ and $\|\psi'\|_2$. Thus, for a fixed $z=x+iy$,

$$
\left|
\int_{-R}^{R}\psi(t)e^{izt}\,dt
\right|
\le
C(R,z)\|\psi\|_{\mathcal H_R}.
$$

Therefore,

$$
G_\psi(z)
=\int_{-R}^{R}\psi(t)e^{izt}\,dt
$$

is a bounded linear functional, and the compact support generates an entire function of exponential type at most $R$.

The structural zeros define the closed subspace

$$
\mathcal H_R^0
=\left\{
\psi\in\mathcal H_R:
G_\psi(0)=G_\psi(i/2)=0
\right\}.
$$

Since $\psi$ is even,

$$
G_\psi(0)=\int_{-R}^{R}\psi(t)\,dt,
$$

$$
G_\psi(i/2)
=\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt.
$$

## 3. Evaluation Operators

### 3.1 Real Axis

By Riesz representation, for every real $x$ there exists a unique $p_x\in\mathcal H_R^0$ such that

$$
\langle\psi,p_x\rangle_T=G_\psi(x).
$$

Let

$$
P_x=p_x\otimes p_x.
$$

Then

$$
\langle\psi,P_x\psi\rangle_T
=G_\psi(x)^2\ge0.
$$

### 3.2 Off-Axis Core

For $z=x+iy$, even symmetry gives

$$
\operatorname{Re}G_\psi(z)
=\int_{-R}^{R}
\psi(t)\cos(xt)\cosh(yt)\,dt,
$$

$$
\operatorname{Im}G_\psi(z)
=-\int_{-R}^{R}
\psi(t)\sin(xt)\sinh(yt)\,dt.
$$

Let $u_z,v_z$ be two real Riesz representers. Then

$$
2\operatorname{Re}G_\psi(z)^2
=2\left[
\langle\psi,u_z\rangle_T^2
-\langle\psi,v_z\rangle_T^2
\right].
$$

Thus, the core operator is exactly

$$
C_z
=2\left(
u_z\otimes u_z-v_z\otimes v_z
\right).
$$

This rank-two identity is the core of the entire continuous reduction: the off-axis negative direction is not a large unknown operator, but comes solely from the imaginary evaluation representer.

## 4. Positive Trace-Class Primal

A finite PSD Gram matrix can be viewed as a finite-rank positive operator. After continuization, consider

$$
A\succeq0,\qquad
A\in\mathcal S_1(\mathcal H_R^0).
$$

Fix the five bands

$$
\mathcal A_0=[14,18],\quad
\mathcal A_1=[18,23],\quad
\mathcal A_2=[23,35],
$$

$$
\mathcal A_3=[35,70],\quad
\mathcal A_4=[70,145],
$$

and the v0.5 difficult patch

$$
\mathcal P
=[20.395,20.42]\times[-0.10625,-0.1].
$$

Introduce epigraph variables $s_j$ and define the primal:

$$
\begin{aligned}
\Lambda_R=\inf\quad&
\operatorname{Tr}(A)
+\sum_{j=0}^{4}N_js_j\\
\text{subject to}\quad&
\operatorname{Tr}(P_xA)\le s_j
\quad\forall x\in\mathcal A_j,\\
&
\operatorname{Tr}(C_zA)\le-1
\quad\forall z\in\mathcal P,\\
&A\succeq0.
\end{aligned}
$$

$\operatorname{Tr}(A)$ is precisely the tail objective, because the tail quadratic form has been inner-productized.

## 5. Measure Dual Weak Theorem

Let $\mu_j$ be probability measures on $\mathcal A_j$, and $\nu$ be a probability measure on $\mathcal P$. Suppose there exists $\alpha>0$ such that

$$
W_\alpha
=I+\sum_{j=0}^{4}N_j
\int_{\mathcal A_j}P_x\,d\mu_j(x)
+\alpha
\int_{\mathcal P}C_z\,d\nu(z)
\succeq0.
$$

For every primal-feasible $A$,

$$
0\le\operatorname{Tr}(W_\alpha A).
$$

Also, due to probability normalization and the primal inequalities,

$$
\begin{aligned}
\operatorname{Tr}(W_\alpha A)
&=\operatorname{Tr}(A)
+\sum_jN_j
\int\operatorname{Tr}(P_xA)\,d\mu_j(x)\\
&\quad+\alpha
\int\operatorname{Tr}(C_zA)\,d\nu(z)\\
&\le
\operatorname{Tr}(A)+\sum_jN_js_j-\alpha.
\end{aligned}
$$

Therefore,

$$
\Lambda_R\ge\alpha.
$$

This theorem only uses weak duality. Even if infinite-dimensional strong duality has not yet been established, a dual-feasible witness is still sufficient to rule out $\Lambda_R<\alpha$.

This also explains why the dual axis grid does not suffer from the same v0.4 primal coarse-grid false escape problem: an atomic $\mu_j$ at any valid real-axis position is a genuine continuous probability measure; it does not need to cover the entire band to provide a lower bound.

## 6. One-Axis-Point, One-Core-Point Closed-Form Model

### 6.1 Generalized Rank-Two Eigenvalue

Fix $x,z,N$. Let

$$
B=I+Np_x\otimes p_x.
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
\widehat v=B^{-1/2}v_z
$$

and

$$
a=\|\widehat u\|^2,\quad
b=\|\widehat v\|^2,\quad
c=\langle\widehat u,\widehat v\rangle.
$$

Since

$$
B^{-1/2}C_zB^{-1/2}
=2\left(
\widehat u\otimes\widehat u
-\widehat v\otimes\widehat v
\right),
$$

its non-zero eigenvalues are

$$
\lambda_\pm
=(a-b)\pm
\sqrt{(a+b)^2-4c^2}.
$$

If $\lambda_-<0$, the optimal PSD operator can take rank one along the most-negative eigendirection, thus

$$
\Lambda(x,z;N)
=-\frac1{\lambda_-}.
$$

That is,

$$
\Lambda(x,z;N)
=
\frac1{
\sqrt{(a+b)^2-4c^2}-(a-b)
}.
$$

### 6.2 Six Kernel Numbers

Sherman–Morrison gives

$$
B^{-1}
=I-\frac{N}{1+N\|p_x\|^2}
p_x\otimes p_x.
$$

Thus

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
-\frac{
N\langle p_x,u_z\rangle
\langle p_x,v_z\rangle
}{
1+N\|p_x\|^2
}.
$$

Therefore, the simplified problem is completely determined by

$$
\|p\|^2,\ \|u\|^2,\ \|v\|^2,\
\langle u,v\rangle,\
\langle p,u\rangle,\
\langle p,v\rangle
$$

### 6.3 Numerical Conclusions

Fix the patch center

$$
z_c=20.4075-0.103125i.
$$

After point-by-point scanning across the five bands, the optimal single-point lower bounds are

$$
0.111322,\quad
0.261253,\quad
0.111224,\quad
0.111034,\quad
0.111031.
$$

All are below $1$. $A_1$ is indeed the strongest, but it alone is insufficient to generate an obstruction. The blocking repeatedly observed in v0.5 must come from a multi-band union, not a single target-near peak.

## 7. Clamped Green Kernel

### 7.1 Explicit Kernel

Let

$$
L=2R,\quad
\xi=s+R,\quad
\eta=t+R,
$$

$$
a=\min(\xi,\eta),\quad
b=\max(\xi,\eta).
$$

For the clamped space without structural zeros imposed,

$$
K_{\rm cl}(s,t)
=\frac{
a^2(L-b)^2
\left[3bL-(L+2b)a\right]
}{
6L^3\kappa_R
}.
$$

It is a cubic polynomial before and after $s=t$, with the first three orders matching $K,K',K''$, while the third derivative jump yields

$$
\kappa_R\partial_s^4K_{\rm cl}(s,t)
=\delta_t(s).
$$

Both ends satisfy

$$
K_{\rm cl}=0,\qquad
\partial_sK_{\rm cl}=0.
$$

### 7.2 Structural Projection

Let

$$
c_0(t)=1,\qquad
c_1(t)=\cosh(t/2).
$$

Let $k_f$ denote the clamped representer of density $f$. The structural Gram matrix is

$$
M_{ij}
=\langle k_{c_i},k_{c_j}\rangle_T.
$$

For any two densities $f,g$, after projecting onto the $G(0)=G(i/2)=0$ subspace,

$$
\Gamma(f,g)
=\langle k_f,k_g\rangle_T
-b_f^\mathsf TM^{-1}b_g,
$$

where

$$
b_f
=\begin{pmatrix}
\langle k_{c_0},k_f\rangle_T\\
\langle k_{c_1},k_f\rangle_T
\end{pmatrix}.
$$

Thus, all continuous inner products are reduced to explicit Green integrals and a $2\times2$ projection.

### 7.3 Independent ODE Evaluation

The program does not directly build a massive Green matrix, but instead solves

$$
\kappa_Rk''''=f.
$$

for density $f$. Taking the left endpoint as $a=-R$, the particular solution is

$$
k_p(t)
=\frac1{6\kappa_R}
\int_a^t(t-s)^3f(s)\,ds.
$$

Then add

$$
c_2(t-a)^2+c_3(t-a)^3
$$

to satisfy the right-endpoint value/slope zero. The integral is reconstructed from four cumulative moments

$$
\int_a^t s^mf(s)\,ds,\qquad m=0,1,2,3
$$

This path is distinct from the basis, whitening, and generalized eigensolver of Chebyshev–Galerkin, thus allowing for a genuine cross-check.

## 8. Nested Galerkin Convergence

### 8.1 Basis Family

Let $u=t/R$, adopt

$$
\phi_n(t)
=\left(1-u^2\right)^2T_{2n}(u).
$$

The window ensures the value and slope are zero at both ends, and the even Chebyshev polynomials make the spaces nested. After projecting two structural rows from each raw space, the effective dimension is reduced by 2.

### 8.2 Joint Sequence

Computation results:

| effective dimension | raw joint $\alpha$ |
|---:|---:|
| $22$ | $7.788239$ |
| $38$ | $3.679471$ |
| $62$ | $1.588306$ |
| $78$ | $1.300399$ |
| $94$ | $1.184647$ |
| $118$ | $1.159914$ |
| $142$ | $1.139122$ |
| $158$ | $1.133508$ |
| $174$ | $1.132795$ |
| $190$ | $1.132475$ |

The decrease in this sequence is important. The low-dimensional $\alpha=7.79$ is clearly not a continuous conclusion; as the space expands, primal freedom increases, and the dual obstruction must decrease. By dimensions $174$ and $190$, the amount of decrease starts to shrink, but one still cannot rely solely on plateau extrapolation.

### 8.3 Point-Kernel Convergence

At $x=20.4$, $z=z_c$:

$$
\Lambda_{40}=0.8789952,
$$

$$
\Lambda_{96}=0.2017878,
$$

$$
\Lambda_{160}=0.1135563,
$$

$$
\Lambda_{192}=0.11244168195.
$$

The direct Green solver at $\Delta t=0.0025$ gives

$$
0.11244168090.
$$

The absolute difference between the two is about

$$
1.05\times10^{-9}.
$$

This shows that raw dimension 192 has already resolved the target-near high-frequency direction; v0.6 subsequently does not need to rely on blind dimension-increase guessing.

## 9. Atomic Transfer to the Continuous Kernel

### 9.1 Frozen Measures

The optimized measures at dimension 190 have:

$$
22,\ 5,\ 14,\ 9,\ 8
$$

five-band axis atoms, totaling 58. The core measure is supported only at

$$
(20.395,-0.1),\qquad
(20.42,-0.1),
$$

with weights approximately

$$
0.5917914068,\qquad
0.4082085932.
$$

### 9.2 Higher-Space Reconstruction

Without re-optimizing the measures, simply placing the same witness into higher Galerkin spaces:

| raw dimension | fixed-measure threshold |
|---:|---:|
| $192$ | $1.13247521$ |
| $208$ | $1.13247311$ |
| $224$ | $1.13246577$ |
| $256$ | $1.13245246$ |
| $288$ | $1.13244239$ |

The decrease continues but is already very small.

### 9.3 Direct Green Reconstruction

After completely removing the Galerkin dictionary:

| time step | direct Green threshold |
|---:|---:|
| $0.02$ | $1.1324314430$ |
| $0.01$ | $1.1324406087$ |
| $0.005$ | $1.1324411657$ |
| $0.0025$ | $1.1324411997$ |

Therefore, the floating threshold of the fixed atomic measure in the continuous Green kernel stabilizes at

$$
1.1324412.
$$

At

$$
\alpha_{\rm safe}=1.0662376054
$$

$$
\lambda_{\min}(W_{\rm safe})
=0.2568265725.
$$

This is no longer the PSD of some finite dictionary, but the floating PSD of a continuous-kernel finite-rank operator defined by explicit Green pairings.

## 10. Infinite PSD to a $2\times2$ Schur Test

### 10.1 Positive and Negative Directions

For the finite atomic witness, multiply the 58 axis vectors and the two core-real vectors by their coefficient/weight square roots and place them into $U$. Place the two core-imag vectors into $V$. Then

$$
W_\alpha
=I+UU^\ast-VV^\ast.
$$

Let

$$
B_\alpha=I+UU^\ast\succ0.
$$

Then

$$
W_\alpha\succeq0
$$

is equivalent to

$$
I-V^\ast B_\alpha^{-1}V\succeq0.
$$

By the Woodbury identity,

$$
B_\alpha^{-1}
=I-U(I+U^\ast U)^{-1}U^\ast.
$$

Therefore, the final certificate matrix is

$$
S_\alpha
=I-\left[
V^\ast V
-V^\ast U
(I+U^\ast U)^{-1}
U^\ast V
\right].
$$

Note that adjacent factors are multiplied in sequence; the second term inside the brackets is fully

$$
V^\ast U(I+U^\ast U)^{-1}U^\ast V.
$$

Since $V$ has only two columns,

$$
S_\alpha\in\mathbb R^{2\times2}.
$$

### 10.2 Floating Schur Margin

At $\alpha_{\rm safe}$:

$$
S_{\rm safe}
\approx
\begin{pmatrix}
0.42967760&-0.44911051\\
-0.44911051&0.59598368
\end{pmatrix},
$$

and

$$
\lambda_{\min}(S_{\rm safe})
\approx0.05608708.
$$

This reduction is much simpler than directly interval-checking an abstract infinite operator: v0.7 only requires the enclosure of the kernel Gram, the positive $60\times60$ solve, and the final $2\times2$ matrix.

## 11. Rational Witness

### 11.1 Why Lower Alpha

This node does not treat the floating optimum $1.13244$ as the certification target. Selecting

$$
\alpha_\star=\frac{21}{20}=1.05
$$

preserves a lower-bound margin of

$$
0.05
$$

while simultaneously increasing the PSD buffer.

### 11.2 Exact Finite Data

Each set of probability weights is converted into integers with a denominator of

$$
10^{12}
$$

using the largest-remainder rule to ensure each set of numerators sums exactly. The axis/core locations are converted to decimal rationals. The two core points are

$$
\left(\frac{4079}{200},-\frac1{10}\right),
$$

$$
\left(\frac{1021}{50},-\frac1{10}\right).
$$

The core weights are

$$
\frac{591791406771}{10^{12}},
\qquad
\frac{408208593229}{10^{12}}.
$$

### 11.3 Rationalized Floating Audit

At $\alpha_\star=1.05$:

$$
\lambda_{\min}(W_{\alpha_\star})
\approx0.3122432495,
$$

$$
\lambda_{\min}(S_{\alpha_\star})
\approx0.0698852338.
$$

When the time step goes from $0.005\to0.0025$, the variation in the Schur minimum is about

$$
2.68\times10^{-8}.
$$

This variation is merely an experimental convergence indicator, not a directed error bound.

## 12. Research Verdict

### 12.1 Resolved Issues

v0.6 has answered the main suspicion of the parent node:

> The obstruction is not an artifact of the local bump dictionary.

The evidence does not rely solely on "switching to a larger basis still fails", but rather:

1. Nested spaces show the obstruction decreasing with dimension;
2. The point extremal and the direct Green solver match to $10^{-9}$;
3. Frozen atomic measures remain stable in higher dimensions;
4. The same measures still yield $\alpha>1$ in the explicit continuous Green kernel;
5. The infinite PSD is exactly reduced to a finite kernel Gram and a $2\times2$ Schur test.

### 12.2 Unresolved Issues

The floating result still cannot be written as a theorem instance, because:

- Green integrals lack directed rounding;
- The structural projection is not interval-enclosed;
- The positive solve is not verified;
- The tail/count coefficients have not completed a theorem-backed interval transfer;
- The complete interface from the $H_0^2$ model to zeta explicit-formula admissibility is unproven.

### 12.3 Stop Decision

Therefore:

- Halt the notch dictionary search;
- Halt the external lift scaling;
- Halt further Galerkin dimensions;
- Do not rerun the primal construction;
- Save the rational 58+2 atomic witness;
- The next node will fix the verification at $\alpha=21/20$.

## 13. v0.7 Certification Path

Next node:

`RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`

The work is divided into two layers.

### 13.1 Layer A: Abstract Continuous Extremal

Using exact rational finite data and an explicit continuous kernel, interval-enclose

$$
S_{21/20}.
$$

The goal is to prove

$$
\lambda_{\min}(S_{21/20})>0.
$$

Once completed, continuous weak duality immediately gives

$$
\Lambda_{16}\ge\frac{21}{20}.
$$

### 13.2 Layer B: Zeta-Facing Coefficients

Must be verified separately:

1. $\kappa_R$ is indeed a valid, conservative tail coefficient;
2. $N_j$ are count lower coefficients with complete assumptions;
3. The relationship between explicit-formula admissible tests and the $\mathcal H_R^0$ domain;
4. All leakage regions outside the target patch;
5. All quantifiers from the local object to the global RH statement.

Layer A is an important analytic obstruction, but it cannot replace Layer B.

## 14. Trust Boundary

The formal conclusion of this node is:

> In the specified clamped $H_0^2$ continuous axis/core model, the trace-class primal has a probability-measure weak dual; the one-axis-point, one-core-point model can be exactly reduced to rank two. The nested Galerkin and independent Green solver consistently show that the continuous-kernel floating threshold of a 58-axis, 2-core atomic measure is $1.1324412$. After rationalizing the data and fixing $\alpha=21/20$, the continuous PSD can be exactly reduced to a $2\times2$ Schur certificate, with a floating minimum of $0.0698852$. Therefore, the next step should be interval certification, rather than continuing to expand the dictionary.

It cannot be inferred from this node that:

- The interval-certified continuous obstruction is complete;
- All RH test-function architectures are infeasible;
- A zeta zero exists in the target patch;
- The global budget for unknown off-axis zeros is closed;
- The RH is true or false.

What this round accomplishes is the transition "from finite dictionary exploration to an interval-enclosable continuous-kernel certificate", not the endgame of the RH.