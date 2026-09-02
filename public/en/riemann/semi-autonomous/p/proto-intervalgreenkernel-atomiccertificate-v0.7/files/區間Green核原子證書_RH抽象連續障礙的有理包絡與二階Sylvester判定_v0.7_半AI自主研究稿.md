# Interval Green Kernel Atomic Certificate: Rational Enclosure of the RH Abstract Continuous Obstruction and Second-Order Sylvester Criterion

Version: v0.7  
Date: 2026-07-25  
Research Type: Semi-AI Autonomous Mathematics Research Internal Draft  
Node: `RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`

## Abstract

This paper continues the Paley–Wiener axis-kernel extremal research of v0.6. The previous node transferred the finite Chebyshev–Galerkin phenomenon to a continuous clamped Green RKHS, finding a rationalized atomic dual witness composed of $58$ axis atoms and $2$ core atoms. In standard floating-point reconstruction, the threshold for the fixed witness is approximately

$$
1.13244120,
$$

and under the safety target

$$
\alpha_\star=\frac{21}{20}=1.05
$$

the minimum eigenvalue of the final $2\times2$ Schur matrix is approximately

$$
0.06988523.
$$

However, a floating-point positive margin is not a certificate. This paper re-establishes the following using $90$-digit directed-decimal interval arithmetic:

1. $\pi$, exponential, trigonometric, and hyperbolic function enclosures;
2. closed-form pairings of the clamped $D^4$ Green representer;
3. interval projection of two structural zeros;
4. Neumann regularity of a $60\times60$ positive system family;
5. verified solution enclosure for two right-hand sides;
6. Sylvester positivity of the final $2\times2$ matrix.

The resulting rigorous bounds are

$$
\left\|I-\mathcal R A\right\|_\infty
\leq
7.531404753645390\times10^{-15},
$$

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

Therefore, for the rational abstract continuous model explicitly defined in this paper,

$$
W_{21/20}\succ0.
$$

This is the first time the research chain has completed a dictionary-independent, time-grid-independent, directed-rounding continuous atomic certificate.

However, this paper simultaneously discovers a more critical zeta-facing obstruction: the five positive band coefficients from the parent node are zero-count upper profiles, rather than the lower profiles guaranteed by the current $|S(T)|$ bound. Rounding an upper bound down does not turn it into a lower bound. Therefore, the interval certificate in this paper only completes Layer A and does not constitute an RH proof, disproof, or actual zeta zero-region exclusion.

## I. Shift in the Research Problem

### 1. From Optimization to Legitimization

The core question of early nodes was:

> Can we find a set of test functions such that a certain off-axis core contribution is blocked by axis and tail positivity?

By v0.6, the answer in the floating continuous model was already affirmative. Continuing to expand the Galerkin dimension or searching for more atoms would only increase numerical data without elevating the epistemological status of the proposition.

Therefore, v0.7 halts the optimization of

$$
\alpha
$$

and fixes

$$
\alpha_\star=\frac{21}{20}.
$$

The sole primary objective of this round is:

> To prove that the fixed rational atomic witness is indeed positive definite in the full continuous Green model, rather than merely appearing positive definite in some discrete approximation.

### 2. Two-Layer Certificate

This paper continues to use the two-layer distinction:

#### Layer A: abstract continuous extremal

Treat the radius, tail scale, band coefficients, atoms, and weights entirely as explicit rational model data, and prove their operator positivity.

#### Layer B: zeta-facing theorem transfer

Separately prove:

- the source theorem and monotonic direction of the tail coefficient;
- the zero-count semantics and bounding directions of the band coefficients;
- the admissibility of the test-function class for the explicit formula;
- the complete transfer between the prime-side and the zero-side.

Success in Layer A does not logically automatically complete Layer B.

## II. Continuous Hilbert Model

### 1. Space

Fix

$$
R=16
$$

and the rational tail scale

$$
\kappa
=
\frac{31794183142988}{10^{18}}.
$$

Define

$$
\mathcal H=
\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t),\
\int_{-R}^{R}\psi(t)\,dt=0,\
\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt=0
\right\}.
$$

The inner product is

$$
\langle\psi,\phi\rangle_{\mathcal H}
=
\kappa
\int_{-R}^{R}
\psi''(t)\phi''(t)\,dt.
$$

The clamped boundary conditions are

$$
\psi(-R)=\psi'(-R)=\psi(R)=\psi'(R)=0.
$$

The Paley–Wiener compact-support framework provides the background for the entire Fourier transform; reproducing-kernel representers are placed in Aronszajn's standard RKHS context. This paper does not claim that this space is already equivalent to a specific de Branges space.

### 2. Evaluation Densities

For an axis point $x\in\mathbb R$,

$$
p_x(t)=\cos(xt).
$$

For a core point $z=x+iy$, the real and imaginary evaluation densities on the real-even domain are

$$
u_{x,y}(t)
=
\cos(xt)\cosh(yt),
$$

$$
v_{x,y}(t)
=
-\sin(xt)\sinh(yt).
$$

Therefore

$$
G_\psi(x+iy)
=
\int_{-R}^{R}\psi(t)u_{x,y}(t)\,dt
+i
\int_{-R}^{R}\psi(t)v_{x,y}(t)\,dt.
$$

### 3. Fixed Atomic Witness

The five-band axis measures are each probability measures. All weights are exactly serialized with the denominator

$$
10^{12}
$$

and the sum of the numerators in each band exactly equals the denominator. The core measure is treated similarly.

The fixed operator can be written as

$$
W_\alpha
=
I
+\sum_{j=0}^{4}
N_j
\sum_{k}
\mu_{jk}\,
p_{x_{jk}}\otimes p_{x_{jk}}
+2\alpha
\sum_{\ell}
\nu_\ell
\left(
u_\ell\otimes u_\ell
-v_\ell\otimes v_\ell
\right).
$$

This paper verifies it under

$$
\alpha=\frac{21}{20}.
$$

## III. From Green Kernel to Finite Exponential Calculus

### 1. Why Not Directly Bound the Grid Error

The direct Green solver in v0.6 uses time-grid trapezoid integration. Its convergence performance is excellent, but to convert it into a truly rigorous quadrature, one must simultaneously control:

- high-frequency trigonometric derivatives;
- cumulative ODE integration error;
- structural projection cancellation;
- uniform error of the $62\times62$ pairings.

This is not impossible, but the certificate would be massive and difficult to audit.

A better approach is to exploit the fact that all densities are finite exponential sums.

### 2. Exponential Decomposition

For example,

$$
\cos(xt)
=
\frac12e^{ixt}
+\frac12e^{-ixt}.
$$

And

$$
\cos(xt)\cosh(yt)
$$

is a rational linear combination of four

$$
e^{(\pm y\pm ix)t}.
$$

Similarly,

$$
-\sin(xt)\sinh(yt)
$$

is also a rational complex linear combination of four exponential terms.

Therefore, we only need to handle the general density

$$
e^{bt}.
$$

### 3. Clamped Representer

The representer $r_b$ satisfies

$$
\kappa r_b^{(4)}(t)=e^{bt}
$$

and four clamped conditions.

If $b\neq0$, take the particular solution

$$
\frac{e^{bt}}{\kappa b^4}.
$$

Then add the unique cubic polynomial $P_b$ to eliminate the values and slopes at both ends:

$$
r_b(t)
=
\frac{e^{bt}}{\kappa b^4}
+P_b(t).
$$

If $b=0$, the closed-form solution is

$$
r_0(t)
=
\frac{(t^2-R^2)^2}{24\kappa}.
$$

### 4. Moment Recurrence

Let

$$
I_n(a)
=
\int_{-R}^{R}
t^n e^{at}\,dt.
$$

When $a\neq0$,

$$
I_0(a)
=
\frac{e^{aR}-e^{-aR}}{a},
$$

and

$$
I_n(a)
=
\frac{R^n e^{aR}-(-R)^n e^{-aR}}{a}
-\frac{n}{a}I_{n-1}(a).
$$

When $a=0$, the moments are exact rationals. Thus, each Green pairing

$$
\Gamma(a,b)
=
\int_{-R}^{R}
e^{at}r_b(t)\,dt
$$

requires only finitely many rational operations and endpoint exponentials.

### 5. Two-Way Check of Self-Adjoint Symmetry

The Green operator is self-adjoint, so

$$
\Gamma(a,b)=\Gamma(b,a).
$$

The program computes two intervals separately, using $b$ as the source and $a$ as the source, and then takes their intersection. If the two do not overlap, the computation halts immediately. This is not ordinary symmetry post-processing, but a cross-check of two boundary correction formula paths.

## IV. Directed Enclosure of Transcendental Functions

### 1. No Reliance on External Interval Packages

The execution environment does not have Arb or FLINT pre-installed. This paper does not revert to ordinary arbitrary-precision floating point, but instead uses the directed contexts of Python's `Decimal`:

- lower endpoint towards $-\infty$;
- upper endpoint towards $+\infty$;
- precision fixed at $90$ digits.

### 2. Rational Enclosure of $\pi$

Uses

$$
\pi
=
16\arctan\left(\frac15\right)
-4\arctan\left(\frac1{239}\right).
$$

Applies the alternating remainder theorem to

$$
\arctan x
=
\sum_{n=0}^{\infty}
\frac{(-1)^n x^{2n+1}}{2n+1}.
$$

The two series take $96$ and $40$ terms respectively, generating a $\pi$ interval of width

$$
10^{-89}.
$$

### 3. Trigonometric Functions

For a rational angle $\theta$, choose an integer $k$ and let

$$
r=\theta-k\frac{\pi}{2}.
$$

The program verifies that the absolute value of the entire $r$ interval is less than $0.8$. In this region, a $44$-term Taylor polynomial and Lagrange remainder enclose $\sin r$ and $\cos r$, and then restore the quadrant based on $k$ modulo $4$.

### 4. Real Exponentials

For $e^x$, first divide the argument by $2^m$ until

$$
\left|\frac{x}{2^m}\right|
\leq
\frac1{16}.
$$

Use a $48$-term Taylor polynomial on the reduced interval, providing a remainder bound via

$$
e^{|\xi|}<2;
$$

finally, perform repeated interval squaring.

### 5. Enclosure Width

The maximum interval width of the complete projected Gram matrix is

$$
3.71216\times10^{-84}.
$$

This width is far smaller than the subsequent Neumann and Sylvester margins.

## V. Structural-Zero Projection

Let

$$
c_0(t)=1,
\qquad
c_1(t)=\cosh(t/2).
$$

The unconstrained Green Gram matrix is

$$
M=
\begin{pmatrix}
\Gamma(c_0,c_0)&\Gamma(c_0,c_1)\\
\Gamma(c_1,c_0)&\Gamma(c_1,c_1)
\end{pmatrix}.
$$

For any densities $f,g$, the pairing in the constrained subspace is

$$
\Gamma_0(f,g)
=
\Gamma(f,g)
-\mathbf c(f)^\mathsf T
M^{-1}
\mathbf c(g).
$$

This round proves

$$
\inf\det M
>
6.087163164690596\times10^{20}.
$$

Thus, the entire structural inverse interval is valid. This step closes the structural projection gap from v0.6.

## VI. From Infinite-Dimensional Operator to $2\times2$

### 1. Positive and Negative Factors

Assemble the $58$ axis representers and $2$ core-real representers into $F$. Assemble the $2$ core-imag representers into $V$.

Place the positive and negative weights into $D$ and $B$, respectively. Then

$$
K_+=I+FDF^\ast,
$$

$$
W=K_+-VBV^\ast.
$$

Since $D\succ0$,

$$
K_+\succ0.
$$

### 2. Square-Root-Free Formula

Let

$$
G=F^\ast F,\qquad
C=F^\ast V,\qquad
H=V^\ast V.
$$

Let

$$
A=I+GD.
$$

The Woodbury identity gives

$$
K_+^{-1}
=
I-FD A^{-1}F^\ast.
$$

Thus

$$
Q
=
V^\ast K_+^{-1}V
=
H-C^\mathsf T D A^{-1}C.
$$

Originally,

$$
I-B^{1/2}QB^{1/2}
$$

could be used as the Schur matrix, but this would introduce additional square-root intervals. This paper instead uses the congruent matrix

$$
T=B^{-1}-Q.
$$

From

$$
B^{1/2}TB^{1/2}
=
I-B^{1/2}QB^{1/2},
$$

we know

$$
W\succ0
\quad\Longleftrightarrow\quad
T\succ0.
$$

## VII. Verified Neumann Solve

### 1. Candidate is Not a Proof

First, use standard NumPy to generate an approximate candidate for $A^{-1}$, then serialize each entry into a finite decimal rational, denoted as $\mathcal R$.

The proof phase completely distrusts the original floating-point inverse, and instead recomputes

$$
E=I-\mathcal R\mathbf A,
$$

where $\mathbf A$ is the complete interval matrix family.

### 2. Regularity

The directed row-sum norm gives

$$
\|E\|_\infty
\leq
7.5314047536453899529795284724
\times10^{-15}.
$$

Because this value is strictly less than $1$, the Neumann series proves that every

$$
A\in\mathbf A
$$

is invertible.

### 3. Solution Enclosure

For the stored approximate solution $X_0$,

$$
\rho
=
\mathcal R(C-AX_0).
$$

The true solution satisfies

$$
X-X_0
=
(I-E)^{-1}\rho.
$$

Thus

$$
\|X-X_0\|_\infty
\leq
\frac{\|\rho\|_\infty}{1-\|E\|_\infty}.
$$

The componentwise radius upper bounds for the two columns are

$$
6.479135069600651\times10^{-16}
$$

and

$$
2.881263499141683\times10^{-16}.
$$

## VIII. Final Sylvester Certificate

Calculations yield

$$
T_{11}
\in
[
0.3524279496453903261,\
0.3524279496454151611
],
$$

$$
T_{12}=T_{21}
\in
[
-0.4286502909903862159,\
-0.4286502909903751717
],
$$

$$
T_{22}
\in
[
0.7018637127810353025,\
0.7018637127810463962
].
$$

And

$$
\det T
\in
[
0.0636153172597786300,\
0.0636153172598094386
].
$$

Therefore

$$
\inf T_{11}>0
$$

and

$$
\inf\det T>0.
$$

By the $2\times2$ Sylvester criterion,

$$
T\succ0.
$$

Ultimately, we obtain the main theorem of this paper:

> For the stored rational atoms, weights, tail scale, and band coefficients, in the real-even clamped structural-zero continuous Hilbert model, $W_{21/20}$ is strictly positive definite.

Combined with the abstract weak duality of the parent node, we can deduce within the same abstract model that

$$
\Lambda_{16}
\geq
\frac{21}{20}
>
1.
$$

## IX. Verification Architecture

### 1. Full Recomputation

`verify_certificate.py` reads the witness and certificate back from disk, re-establishing:

- $\pi$ interval;
- exponential and trigonometric enclosures;
- all Green pairings;
- structural projection;
- projected Gram hash;
- Neumann proof;
- final Sylvester proof.

All checks evaluate to true.

### 2. Exact Serialization Audit

`audit_certificate.py` converts the finite decimal endpoints into exact `Fraction`s, verifying again:

$$
0\leq q<1,
$$

$$
\inf T_{11}>0,
$$

$$
\inf\det T>0,
$$

all probability sums, and all trust-boundary flags.

### 3. Failure Injection

Test by replacing the inverse candidate with a zero matrix. In this case,

$$
\left\|I-\mathcal R A\right\|_\infty=1,
$$

and the verifier correctly rejects the candidate.

### 4. Cross-Check with v0.6

Converting the new interval midpoint back to the scaled Schur convention of v0.6 yields

$$
\lambda_{\min}
\approx
0.06988523568969546.
$$

The finest time-grid value from v0.6 was

$$
0.06988523379762435.
$$

The difference between the two is approximately

$$
1.8921\times10^{-9}.
$$

This result supports the consistency of the two independent paths, but does not participate in the rigorous proof.

## X. Coefficient Orientation Audit

### 1. Unexpected Discovery

After completing Layer A, the next natural step was originally to intervalize the source theorems of the five band coefficients. However, when auditing the parent node's code, it was discovered that the function name was explicitly called `count_majorant`, and the formula was indeed an upper-count profile.

For a band $[a,b]$, under the standard endpoint convention,

$$
N(b)-N(a)
=
\frac{\theta(b)-\theta(a)}{\pi}
+S(b)-S(a).
$$

Trudgian's inherited bound is

$$
|S(T)|
\leq
B(T)
:=
0.112\log T
+0.278\log\log T
+2.510
$$

for $T\geq e$.

So the lower and upper profiles obtained directly from this data are respectively

$$
L_{a,b}
=
\max\left(
0,\
\frac{\theta(b)-\theta(a)}{\pi}
-B(a)-B(b)
\right),
$$

and

$$
U_{a,b}
=
\max\left(
0,\
\frac{\theta(b)-\theta(a)}{\pi}
+B(a)+B(b)
\right).
$$

### 2. Five-Band Comparison

The existing coefficients are:

| band | stored | direct lower from $|S|$ | classification |
|---|---:|---:|---|
| $[14,18]$ | $6.797423271048$ | $0$ | upper profile |
| $[18,23]$ | $7.246636980606$ | $0$ | upper profile |
| $[23,35]$ | $9.346770522330$ | $0$ | upper profile |
| $[35,70]$ | $18.367573606596$ | $5.069962795569$ | upper profile |
| $[70,145]$ | $40.545362729236$ | $26.742367141539$ | upper profile |

All five stored values tightly hug the downward-rounded values of $U_{a,b}$, and none are guaranteed by the current $L_{a,b}$.

### 3. Why This is Not a Small Error

If a positive semi-definite axis operator enters the witness as

$$
+N_jP_j
$$

then the operator is monotonically increasing with respect to $N_j$. To guarantee that the true operator is not less than the certified operator, one typically requires

$$
N_j^{\mathrm{cert}}
\leq
N_j^{\mathrm{true}}.
$$

The upper majorant goes in the opposite direction.

Rounding

$$
U_j
$$

down to twelve decimal places only yields a number slightly below $U_j$; it does not imply that it is below the true count.

### 4. Stress Test

To quantify the problem, we preserve the entire witness geometry and only replace the five coefficients with $L_j$. The resulting floating Schur eigenvalues are approximately

$$
-5.53605304212116
$$

and

$$
0.942631731149592.
$$

So the fixed witness does not survive under this lower profile.

This stress test does not prove that other atoms or other measures will inevitably fail; it only proves that the abstract certificate of v0.7 cannot be directly attached to the current zeta count argument.

## XI. Research Judgment and Next Node

### 1. What v0.7 Actually Accomplished

This paper closes:

- finite dictionary ambiguity;
- time-grid ambiguity;
- floating Green pairing ambiguity;
- unverified structural inverse;
- unverified $60\times60$ solve;
- floating $2\times2$ eigenvalue sign.

This is a substantial advancement. The obstruction within the abstract model is now a theorem object, rather than a numerical suggestion.

### 2. What v0.7 Did Not Accomplish

This paper did not complete:

- zeta zero-count coefficient legitimacy;
- tail coefficient theorem transfer;
- explicit-formula admissibility;
- prime-side directed cone;
- zero presence;
- cover family;
- global RH closure.

### 3. The Correct Direction for v0.8

The next node is changed to

`RH-RobustBandCounts-ZetaBridge-20260725-v0.8`.

First, reconstruct the original inequality to confirm whether the count majorant should be located in the positive term, the negative budget, or the normalization. If the positive term requires lower counts, then establish a robust coefficient polytope

$$
N_j\in[L_j,U_j]
$$

and re-optimize at the worst-case vector

$$
L=(L_0,\ldots,L_4).
$$

Since the lower endpoints obtained from the existing $|S|$ bound for the first $3$ bands are $0$, v0.8 may need to incorporate:

- interval argument-principle counts;
- Turing method certificates;
- validated zero presence;
- or an entirely new robust witness that does not rely on the first $3$ bands.

### 4. When to Return to Covering Certificate Families

The original long-term direction remains correct:

$$
\text{Band partitioning}
\;+\;
\text{Multiple test functions}
\;+\;
\text{Covering certificate families}.
$$

But the sequence must be:

$$
\text{single-patch abstract certificate}
\to
\text{coefficient semantics}
\to
\text{robust zeta-facing certificate}
\to
\text{cover family}.
$$

Otherwise, it will merely replicate an unverified coefficient orientation on a massive scale across more patches.

## XII. Conclusion

This round yields a twofold conclusion.

First, the continuous atomic obstruction of the fixed rational model has been truly intervalized:

$$
W_{21/20}\succ0.
$$

Second, this success did not mask the next error, but rather made the coefficient direction problem clearer. The numerically most difficult Green/Schur part is now rigorously justified; the blocking point now shifts to theorem semantics:

$$
\text{Whether a coefficient is an upper or lower bound,}
$$

is more important than retaining a few dozen more decimal places.

Therefore, this paper is neither an RH proof nor a research failure. It turns "whether a continuous kernel certificate exists" into an affirmative answer, while precisely reducing "whether this certificate can enter zeta" to a testable coefficient direction and zero-counting problem for the next round.

## References

1. R. E. A. C. Paley and N. Wiener,
   *Fourier Transforms in the Complex Domain*,
   AMS Colloquium Publications $19$,
   <https://bookstore.ams.org/coll-19>.
2. N. Aronszajn,
   “Theory of Reproducing Kernels,”
   *Transactions of the American Mathematical Society* $68$,
   DOI `10.1090/S0002-9947-1950-0051437-7`,
   <https://doi.org/10.1090/S0002-9947-1950-0051437-7>.
3. T. S. Trudgian,
   “An improved upper bound for the argument of the Riemann zeta-function
   on the critical line II,”
   *Journal of Number Theory* $134$, $2014$,
   DOI `10.1016/j.jnt.2013.07.017`,
   <https://openresearch-repository.anu.edu.au/items/2484efc1-7e1b-4a99-821a-ffb0bcbe5697>.
4. Python documentation, `decimal` fixed-point and floating-point arithmetic,
   <https://docs.python.org/3.11/library/decimal.html>.

## Appendix: Certificate Status

- `abstract_continuous_interval_certificate = true`
- `abstract_operator_strictly_positive = true`
- `zeta_facing_tail_theorem_certified = false`
- `zeta_facing_count_coefficients_certified = false`
- `explicit_formula_admissibility_certified = false`
- `global_rh_certificate = false`