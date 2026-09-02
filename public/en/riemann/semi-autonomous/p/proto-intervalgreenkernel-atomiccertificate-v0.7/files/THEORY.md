# Theory

## 1. Abstract Continuous Space

Fix $R=16$ and

$$
\kappa=
\frac{31794183142988}{10^{18}}>0.
$$

Let

$$
\mathcal H=
\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t),\
\int_{-R}^{R}\psi(t)\,dt=0,\
\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt=0
\right\},
$$

equipped with

$$
\langle\psi,\phi\rangle_{\mathcal H}
=
\kappa\int_{-R}^{R}\psi''(t)\phi''(t)\,dt.
$$

For rational $x,y$, define three real-even densities:

$$
p_x(t)=\cos(xt),
$$

$$
u_{x,y}(t)=\cos(xt)\cosh(yt),
$$

$$
v_{x,y}(t)=-\sin(xt)\sinh(yt).
$$

They correspond respectively to axis evaluation and

$$
G_\psi(x+iy)
=
\langle\psi,u_{x,y}\rangle_{L^2}
+i\langle\psi,v_{x,y}\rangle_{L^2}.
$$

## 2. Clamped Green Representer

If the density is $e^{bt}$ and $b\neq0$, its unprojected representer can be written as

$$
r_b(t)=\frac{e^{bt}}{\kappa b^4}+P_b(t),
$$

where $P_b\in\mathbb P_3$ uniquely satisfies

$$
r_b(-R)=r_b'(-R)=r_b(R)=r_b'(R)=0.
$$

If $b=0$, then

$$
r_0(t)=\frac{(t^2-R^2)^2}{24\kappa}.
$$

Therefore, the exponential pairing

$$
\Gamma(a,b)
=
\int_{-R}^{R}e^{at}r_b(t)\,dt
$$

only requires the exponential moments

$$
I_n(a)=\int_{-R}^{R}t^n e^{at}\,dt.
$$

When $a\neq0$,

$$
I_0(a)=\frac{e^{aR}-e^{-aR}}{a},
$$

and

$$
I_n(a)
=
\frac{R^n e^{aR}-(-R)^n e^{-aR}}{a}
-\frac{n}{a}I_{n-1}(a).
$$

When $a=0$,

$$
I_n(0)=
\begin{cases}
0,&n\text{ is odd},\\
\dfrac{2R^{n+1}}{n+1},&n\text{ is even}.
\end{cases}
$$

All axis, core, and structural densities are linear combinations of finitely many rational complex exponentials, so every unprojected pairing can be finitely computed by the above recurrence.

## 3. Structural Constraint Projection

Let

$$
c_0(t)=1,\qquad c_1(t)=\cosh(t/2),
$$

and the structural Gram

$$
M_{ab}=\Gamma(c_a,c_b).
$$

For any densities $f,g$, the reproducing pairing restricted to $\mathcal H$ is

$$
\Gamma_0(f,g)
=
\Gamma(f,g)
-\mathbf c(f)^\mathsf T
M^{-1}
\mathbf c(g),
$$

where

$$
\mathbf c(f)=
\begin{pmatrix}
\Gamma(c_0,f)\\
\Gamma(c_1,f)
\end{pmatrix}.
$$

This package directly proves via interval arithmetic that

$$
\inf\det M
>
6.087163164690596\times10^{20},
$$

so the projection formula is well-defined over the entire enclosure.

## 4. Finite-Rank Operator

Let the $60$ columns of $F$ be:

- $58$ axis representers;
- $2$ core-real representers.

Let the $2$ columns of $V$ be the core-imag representers. The positive and negative rational weights are placed in the diagonal matrices $D$ and $B$, respectively. Fix

$$
\alpha_\star=\frac{21}{20}
$$

which has already been absorbed into the core weights.

Define

$$
K_+=I+FDF^\ast,
$$

and

$$
W=K_+-VBV^\ast.
$$

Let

$$
G=F^\ast F,\qquad
C=F^\ast V,\qquad
H=V^\ast V.
$$

By the Woodbury identity,

$$
K_+^{-1}
=
I-FD(I+GD)^{-1}F^\ast.
$$

Therefore,

$$
Q
=
V^\ast K_+^{-1}V
=
H-C^\mathsf T D(I+GD)^{-1}C.
$$

By the positive definite Schur complement,

$$
W\succ0
\quad\Longleftrightarrow\quad
T:=B^{-1}-Q\succ0.
$$

So the final determination of the infinite-dimensional operator reduces to just $2\times2$.

## 5. Verified Neumann Solve

Let

$$
A=I+GD.
$$

The package stores a finite-decimal rational matrix $\mathcal R$ as a candidate for $A^{-1}$. For the entire interval matrix family, it verifies

$$
E=I-\mathcal R A,
$$

and

$$
\|E\|_\infty
\leq
7.531404753645390\times10^{-15}
<1.
$$

Therefore, every $A$ is invertible.

For the stored rational approximate solution $X_0$, let

$$
\rho
=
\mathcal R(C-AX_0).
$$

Then the true solution $X=A^{-1}C$ satisfies

$$
\|X-X_0\|_\infty
\leq
\frac{\|\rho\|_\infty}{1-\|E\|_\infty}.
$$

The componentwise radii upper bounds of the two right-hand sides are approximately

$$
6.47914\times10^{-16}
$$

and

$$
2.88127\times10^{-16}.
$$

## 6. Final Sylvester Criterion

The final interval matrix is

$$
T\subset
\begin{pmatrix}
[0.3524279496453903,\ 0.3524279496454152]
&
[-0.4286502909903863,\ -0.4286502909903751]
\\
[-0.4286502909903863,\ -0.4286502909903751]
&
[0.7018637127810353,\ 0.7018637127810464]
\end{pmatrix}.
$$

Directed arithmetic gives

$$
\inf T_{11}
>
0.3524279496453903,
$$

and

$$
\inf\det T
>
0.0636153172597786.
$$

By the $2\times2$ Sylvester criterion,

$$
T\succ0,
$$

and consequently

$$
W_{21/20}\succ0.
$$

## 7. Precise Scope of the Theorem

The above conclusion is an abstract continuous interval theorem. It uses a fixed rational $\kappa$ and five rational band coefficients as the model definition.

It does not prove:

- that these five coefficients are valid lower bounds for the positive contribution on the zeta zero-side;
- that $\kappa$ is guaranteed by the source theorem to be lower than the actual tail coefficient;
- that the clamped closure satisfies all admissibility conditions of the explicit formula;
- the existence of any off-axis zero;
- that the universal quantifier of the RH is closed.