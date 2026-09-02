# RH Axis-Band Objective Dual Obstruction

## Explicit Lower Bound, Rejection of the $R=3$ Function Class, and Support-Prime Cost Frontier

Version: v0.3  
Date: 2026-07-24  
Research Mode: Semi-AI Autonomous Mathematical Research  
Technical Research Lead and Judgment: OpenAI Codex (AI Research Collaborator)  
Research Environment, Authorization, and Review: Neo.K / EveMissLab

## Abstract

This node follows the decision from v0.2: to stop undirected rank expansion on the same primal Gram model, and instead search for the dual lower bound forced by the real axis band $[18,23]$. The result is simpler and more decisive than originally expected.

For the 18 covering patches of the target rectangle

$$
[20,20.5]\times[-0.2,-0.1]
$$

this node constructs a matrix at the rational center $z_P$ of each patch:

$$
W_P=10^{-3}T+M_1+2C(z_P),
$$

where $T$ is the tail matrix, $M_1$ is the real-axis matrix formed by a uniform measure over 26 points on $[18,23]$, and $C(z_P)$ is the off-axis core matrix. All 18 matrices $W_P$ are positive definite in the floating model; the minimum eigenvalues fall within

$$
[3.1042101910,3.1042422675]\times10^{-5}.
$$

After term-by-term conversion of the tail matrix and transform vectors into 12-decimal-place rational numbers, all 18 matrices also pass the exact rational $LDL^{\mathsf T}$ positive pivot check. Therefore, within the exported finite rational surrogate, any candidate satisfying

$$
A\succeq0,\qquad \langle C(z_P),A\rangle\le-1
$$

has a banded objective value

$$
J(A)\ge2.
$$

The original objective requires $J(A)<1$, thus the current $R=3$, 24-bump, 22-dimensional restricted coordinate patchwise function class is rejected in this finite model. This is neither a proof of RH, nor a disproof of RH, nor a rejection of all admissible test functions.

Support radius diagnostics show: at a fixed density of about 8 bumps per unit, the first sampling radius where a patch escapes the tail single-point obstruction is $R=5.1$; it is only from $R=8.5$ in the sampling sequence that all 18 patch centers stably escape on subsequent samples. Compared to $R=3$, its prime truncation proxy

$$
e^{2R}
$$

increases by a factor of approximately $e^{11}=59874.14$. The next node should therefore investigate the "support-prime dual frontier" rather than performing further high-rank searches under the same support.

## 1. Problem Origin

Node v0.2 already expanded the 72 existing rank-one rays into full PSD Gram variables. Cross-terms improved by an average of about $21.08\%$, but the sampled axis-plus-tail is still at least $64.60$ times the budget, and the rank $1,2,4,8$ searches for all four representative patches numerically collapsed back to rank one. More importantly, $[18,23]$ constitutes the maximum real-axis charge across all 18 patches.

This leaves two possibilities:

1. The primal searcher has not yet found a truly good direction;
2. The entire restricted function class for $R=3$ is inherently blocked by the geometric relationship between the real axis and the tail term.

This node uses a dual witness to distinguish between the two. The results support the second explanation.

## 2. Finite PSD Model

The model uses 24 real even polynomial bumps on $[-3,3]$ with a numerical integration step size of $0.01$. After imposing the two structural conditions

$$
G(0)=0,\qquad G(i/2)=0
$$

we obtain 22-dimensional $C_0$-whitened coordinates. It is noted that the ordinates of the zeta zeros do not participate in the construction or selection of this node at all.

Let $g(z)\in\mathbb C^{22}$ be the transform row, and define

$$
C(z)=2\operatorname{Re}\!\left(g(z)g(z)^{\mathsf T}\right).
$$

For $A\succeq0$,

$$
B_A(z)=\langle C(z),A\rangle
$$

is the off-axis core value. On the real axis, $g(x)$ is a real vector; let

$$
P(x)=g(x)g(x)^{\mathsf T},\qquad
H_A(x)=\langle P(x),A\rangle\ge0.
$$

The five real-axis bands remain

$$
[14,18],\ [18,23],\ [23,35],\ [35,70],\ [70,145].
$$

If $u_j$ majorizes $H_A$ on the grid of the $j$-th band, the finite primal objective is written as

$$
J(A)=\langle T,A\rangle+\sum_{j=0}^{4}\widehat N_j u_j,
$$

where $T\succeq0$ is the prototype tail matrix, and $\widehat N_j$ is the inherited floating zero-count majorant.

## 3. Dual Lower Bound

Taking only the second band $A_1=[18,23]$. Let

$$
\mathcal G_1=\{18,18.2,\ldots,23\},\qquad |\mathcal G_1|=26,
$$

and truncate the original floating count $7.113998598824585$ downwards to

$$
\underline N_1=7.113998598824.
$$

Define

$$
M_1=
\frac{\underline N_1}{26}
\sum_{x\in\mathcal G_1}P(x).
$$

For any primal-feasible $A$, since $u_1$ majorizes all grid values, $H_A(x)\ge0$, $\underline N_1\le\widehat N_1$, and $0<\rho\le1$, we have

$$
\begin{aligned}
J(A)
&\ge \rho\langle T,A\rangle+\langle M_1,A\rangle\\
&=\langle \rho T+M_1,A\rangle.
\end{aligned}
$$

Now fix the rational center $z_P$ of a patch $P$. If there exists $\alpha>0$ such that

$$
W_P=\rho T+M_1+\alpha C(z_P)\succeq0,
$$

then the self-duality of the PSD cone gives

$$
0\le\langle W_P,A\rangle
=\langle\rho T+M_1,A\rangle
+\alpha\langle C(z_P),A\rangle.
$$

Therefore, as long as the patchwise candidate must satisfy at the center

$$
\langle C(z_P),A\rangle\le-1,
$$

we have

$$
J(A)\ge-\alpha\langle C(z_P),A\rangle\ge\alpha.
$$

Checking only the center here is not a loophole: a candidate required to be less than or equal to $-1$ over the entire patch must necessarily satisfy the center constraint. For a "rejection", a necessary condition is sufficient.

## 4. Explicit Witness Family

This node adopts the same set of axis measure and tail fraction:

$$
\rho=10^{-3},\qquad \alpha=2,
$$

and only lets $C(z_P)$ vary with the 18 patch centers. Thus the certificate family is

$$
\left\{
10^{-3}T+M_1+2C(z_P)
:\ P\in\mathcal P_{18}
\right\}.
$$

This is a dualized version of a "banded, multi-test-function, covering certificate family":

- Banded: Requires only a non-negative uniform measure on $[18,23]$, plus a minimal tail term;
- Multi-test-function: $A\succeq0$ already simultaneously covers any finite PSD Gram combination in the restricted space, no longer confined to existing rays;
- Covering certificate family: Each of the 18 patches has a center witness.

The original plan considered an SDP cutting-plane search. However, the runtime lacks a convex SDP solver, and directly testing the simplest uniform band measure immediately yielded strictly positive definite witnesses, so there is no need to use more complex numerical optimization to produce the same conclusion.

## 5. Verification Results

### 5.1 Floating matrix check

The minimum eigenvalues of the 18 primary witnesses range from

$$
3.1042101910186086\times10^{-5}
\le\lambda_{\min}(W_P)\le
3.1042422674836540\times10^{-5}.
$$

Lowering $\rho$ to $10^{-6}$, all 18 matrices still pass, with the minimum eigenvalues ranging from

$$
[1.6148647147,3.1044753831]\times10^{-8}.
$$

The $\rho=0$ axis-only matrix exhibits

$$
\lambda_{\min}\in
[-1.1127262618\times10^{-6},-2.4418929376\times10^{-17}],
$$

therefore, this node does not claim a pure $A_1$ witness; the tail term provides necessary regularization in near-zero directions. How much of the minimal negative values comes from true geometry versus ill-conditioned numerics is left for interval or high-precision analysis.

### 5.2 Exact rational surrogate

The exported `outputs/rational_model.json` saves:

- 12-decimal-place rational tail matrix;
- Downward-truncated $\underline N_1$;
- 26 real-axis transform vectors;
- Real and imaginary parts of the 18 core transforms;
- $\rho=1/1000$ and $\alpha=2$.

Reforming from vectors

$$
P=gg^{\mathsf T},\qquad
C=2(rr^{\mathsf T}-ii^{\mathsf T}),
$$

then executing exact $LDL^{\mathsf T}$ without pivoting using Python's `Fraction`. The 22 pivots of the rational tail matrix and the 18 witnesses are all strictly positive; the floating display value of the minimum pivot across the entire family is

$$
3.240761260825524\times10^{-5}.
$$

They also all pass under 6-, 8-, 10-, and 12-decimal-place rationalization. This establishes the exact algebraic positivity of the exported finite surrogate; it does not automatically upgrade the numerical integration, zero-count bound, or tail theorem into a formal proof.

### 5.3 Parent primal cross-check

Substituting the 18 saved Gram matrices from v0.2 back into the witnesses:

- All 18 $\langle W_P,A_P\rangle$ are non-negative;
- All dual sub-objectives are at least $2$;
- The pairing range is $[9.51235,28.15543]$;
- The maximum absolute identity residual is $1.07\times10^{-14}$.

This demonstrates that the massive budget overrun in v0.2 was not due to the non-convex searcher accidentally missing a low-cost rank; it is consistent with the cone geometric obstruction identified by this node.

## 6. Stability and Support Radius Diagnostics

The primary witnesses maintain an 18/18 pass rate under all the following perturbations:

- transform quadrature step: $0.02,0.015,0.01,0.0075$;
- axis grid step: $0.2,0.1,0.05,0.025,0.0125$;
- decimal rationalization: 6, 8, 10, 12 places.

This supports the E2 judgment that the "$R=3$ rejection is not a single-mesh coincidence."

Next, maintaining about 8 bumps per unit, we scan $R\in[2,10]$ and compute the single-point optimal dual threshold relying solely on the tail matrix. Results:

| Diagnostic Event | Sampling Radius | $e^{2R}$ Proxy | Relative to $R=3$ |
|---|---:|---:|---:|
| All patches still killed by the tail single-point obstruction | $R=5.0$ | $22026.47$ | $54.60$ |
| First patch escapes | $R=5.1$ | $26903.19$ | $66.69$ |
| All 18 centers stably escape in subsequent sampling | $R=8.5$ | $24154952.75$ | $59874.14$ |

$R=8.4$ briefly passed entirely, and $R=8.45$ rebounded, indicating that basis discretization at a fixed bump density still causes non-monotonicity. Therefore, $R=8.5$ is not a critical constant, but merely the stable turning point of the current sampling sequence. Even if the center tail bound is less than $1$, it does not mean a patchwise primal feasible solution has been found; it only indicates that this specific single-point dual obstruction has receded.

## 7. Research Judgments

This node yields three clear decisions.

First, the $R=3$ function class used in v0.2 should be retired. Higher ranks cannot bypass a witness acting directly on the entire PSD cone.

Second, expanding the support may indeed loosen the obstruction, but the cost is not free. If the prime-side workload of the explicit formula grows with $e^{2R}$, moving from $R=3$ to the diagnostic $R=8.5$ amplifies the truncation proxy by about sixty thousand times.

Third, the next question should not merely ask "which $R$ is feasible," but should simultaneously ask:

$$
\text{dual lower bound}
\quad\text{vs.}\quad
\text{prime-side cost}
\quad\text{vs.}\quad
\text{theorem-certification cost}.
$$

Therefore, the next node is designated as

`RH_Support_Prime_Dual_Frontier_v0.4`.

It should first establish a parametric dual frontier with multiple basis densities and multiple dictionaries over $R\in[4.5,9]$; only radii that pass the dual gate will trigger expensive primal and prime-side computations. Simultaneously, the $A_1$ count and tail prototype should be replaced with sourced, interval-enclosable theorem objects. This saves more information cost than blindly expanding the rank or rushing directly to large prime truncations.

## 8. Trust Boundary

The strongest statement established by this node is:

> In the exported decimal rational finite surrogate, each of the 18 patch centers has an exact rational PSD dual witness, forcing the finite objective to be at least $2$; for the original floating discretization, grid and precision perturbations provide consistent E2 support.

This node does not establish:

- interval transfer between the exact Fourier integral and the exported rational transform;
- theorem-backed zero-count majorant;
- theorem-backed tail inequality;
- complete sign budget for the unknown off-axis zero region;
- zero existence or winding certificate within the patch;
- ZFC logical closure from local to the full critical strip;
- proof of RH, disproof of RH, or proof of equivalent criteria.

For detailed declarations, see `TRUST_BOUNDARY.md`, `metadata/claim_register.json`, and `metadata/gap_ledger.json`.

## 9. Replayable Objects

The primary machine-readable outputs are:

- `outputs/experiment_summary.json`
- `outputs/witness_summary.csv`
- `outputs/witnesses/*.witness.json`
- `outputs/rational_model.json`
- `outputs/rational_verification.json`
- `outputs/sensitivity.json`

The core scripts are:

- `run_dual_experiment.py`
- `verify_rational_witnesses.py`
- `run_sensitivity.py`
- `validate_package.py`

The technical research choices, mathematical interpretations, and next-node decisions of this node are attributed to AI research judgment; Neo.K / EveMissLab provides the research environment, authorization, and review context.