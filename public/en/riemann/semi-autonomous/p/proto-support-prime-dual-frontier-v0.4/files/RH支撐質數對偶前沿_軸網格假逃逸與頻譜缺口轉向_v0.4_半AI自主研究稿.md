# RH Support—Prime Dual Frontier

## Axis Grid False Escapes, Covering Certificate Families, and the Shift to Spectral Notches

Version: v0.4  
Date: 2026-07-24  
Research Mode: Semi-AI Autonomous Mathematical Research  
Technical Research Lead and Judgment: OpenAI Codex (AI Research Collaborator)  
Research Environment, Authorization, and Review: Neo.K / EveMissLab

## Abstract

This node continues the handover from v0.3, implementing "band partitioning, multiple test functions, and covering certificate families," and compares the support radius $R$, basis density, basis width, axis band measures, patch core measures, and prime-side costs on the same frontier.

The first-layer uniform scan contains

$$
14\times3\times3=126
$$

geometric configurations. If we only look at the 18 patch centers, the first sampled escape occurs at $R=10$; if we instead look at the $3\times3$ core measure of each original patch, the first uniform escape is delayed to $R=14$. However, neither of these constitutes a complete dual gate, as uniform axis measures may severely underestimate the real-axis peaks.

The second layer subdivides each of the 18 patches into $4\times4$, yielding 288 sub-rectangles, and then jointly optimizes the five axis band measures and the $3\times3$ core measures for the difficult candidates at $R=10.25,12,14,16$. Explicit finite-model witnesses with safe lower bounds greater than the budget of $1$ were found for all four radii. The strongest safe lower bounds for each radius are

$$
2.6201,\quad1.8999,\quad1.3982,\quad1.0943.
$$

Therefore, all four sampled radii have at least one sub-rectangle that cannot achieve $J(A)<1$ using the current function class. This is sufficient to veto the finite-model route of "simply increasing the support with the same dictionary to configure test functions for every patch in the entire cover."

The most important technical discovery of this round is not the numerical values themselves, but axis grid aliasing. At $R=16$, on patch `x4_Y3__r2_3`, a step size of $0.25$ yields

$$
\alpha=0.985277<1,
$$

seemingly passing the dual gate; after reducing the step size to $0.1,0.05,0.025$, the results rebound sequentially to

$$
1.124306,\quad1.139551,\quad1.192293,
$$

and the final safe scaling still yields

$$
\alpha_{\mathrm{safe}}=1.096146>1.
$$

Thus, the escape on the coarse grid is a reproducible artifact, not evidence of primal feasibility.

The exact support relation on the prime side is

$$
\operatorname{supp}\psi\subset[-R,R]
\quad\Longrightarrow\quad
m\log p<2R,
\quad p^m<e^{2R}.
$$

At $R=10.25$, the actual segmented sieve has enumerated up to

$$
p^m<e^{20.5},
$$

containing $41{,}141{,}456$ primes and $41{,}144{,}807$ prime-power terms, taking about $4.50$ seconds. By $R=16$, the cutoff rises to

$$
78{,}962{,}960{,}182{,}680,
$$

and the $x/\log x$ proxy for the number of primes is approximately $2.47\times10^{12}$. Therefore, even if a larger support might eventually weaken the dual obstruction, brute-force increasing $R$ is no longer a reasonable next step.

The autonomous decision of this node is: halt the support-only expansion, and shift the next node to `RH_Axis_Notch_Cover_Codesign_v0.5`, directly co-designing the dictionary, axis band spectral notches, and patch core negative constraints. This is neither a proof nor a disproof of RH; it is a reproducible veto of the current finite function class and computational route, as well as a pivot in the research direction.

## 1. Questions to Answer in This Round

v0.3 has proven that in the exported $R=3$ rational surrogate, all 18 patches are blocked by a dual lower bound of $2$. The natural next question is:

> Can increasing the support, increasing the degrees of freedom of the test functions, subdividing the cover, and allowing the dual measure to be automatically selected pass through the budget of $1$ before the prime costs spiral out of control?

This question cannot be answered using only a single patch center or a fixed uniform axis measure. If the goal is to establish a covering certificate family for the entire region

$$
\mathcal R=[20,20.5]\times[-0.2,-0.1]
$$

one must simultaneously address at least:

1. Multi-point negativity within the patch, rather than a single center;
2. The worst-case peaks across the five real-axis bands, rather than a uniform average;
3. The prime and prime-power cutoffs as $R$ increases;
4. False escapes caused by coarse grids;
5. Initiating primal searches only after the dual is unblocked.

## 2. Finite Model

### 2.1 Test Function Coordinates

For each radius $R$, we take real, even, compactly supported polynomial bumps on $[-R,R]$. The number of basis functions is

$$
n=\operatorname{round}(dR),
$$

where the density $d\in\{6,8,10\}$. After imposing two structural conditions

$$
G(0)=0,\qquad G(i/2)=0
$$

we apply $C_0$ Gram matrix whitening to obtain approximately $n-2$ dimensional coordinates.

This node adopts the Fourier convention

$$
G(w)=\int_{\mathbb R}\psi(t)e^{iwt}\,dt.
$$

Let $g(z)$ be the transform row in the restricted coordinates, and define

$$
C(z)=2\operatorname{Re}\!\left(g(z)g(z)^{\mathsf T}\right).
$$

For any $A\succeq0$,

$$
B_A(z)=\langle C(z),A\rangle
$$

represents the off-axis core value. On the real axis, $g(x)$ is a real vector, hence

$$
P(x)=g(x)g(x)^{\mathsf T}\succeq0,\qquad
H_A(x)=\langle P(x),A\rangle\ge0.
$$

### 2.2 Band Partitioning Objective

The real axis is partitioned into

$$
A_0=[14,18],\quad
A_1=[18,23],\quad
A_2=[23,35],\quad
A_3=[35,70],\quad
A_4=[70,145].
$$

Let $u_j$ majorize $H_A$ on the discrete grid of the $j$-th band. The finite proxy objective is

$$
J(A)=\langle T,A\rangle+\sum_{j=0}^{4}\underline N_j u_j,
$$

where $T\succeq0$ is the tail prototype, and $\underline N_j$ are coefficients calculated from the published $S(T)$ profile and truncated downwards to 12 decimal places.

This $J$ is a leakage upper-bound proxy in the current program, not a zeta explicit formula theorem object that has completed interval transfer.

## 3. Multi-Measure Dual Witness

For each axis band, we select a discrete probability measure

$$
\mu_j=\sum_k\mu_{jk}\delta_{x_{jk}},
\qquad
\mu_{jk}\ge0,
\qquad
\sum_k\mu_{jk}=1.
$$

For the core points in the patch, we select

$$
\nu=\sum_q\nu_q\delta_{z_q},
\qquad
\nu_q\ge0,
\qquad
\sum_q\nu_q=1.
$$

Define

$$
B_\mu
=T+\sum_{j=0}^{4}
\underline N_j\sum_k\mu_{jk}P(x_{jk}),
$$

and

$$
C_\nu=\sum_q\nu_qC(z_q).
$$

If there exists $\alpha>0$ such that

$$
W=B_\mu+\alpha C_\nu\succeq0,
$$

then for any finite primal candidate satisfying

$$
A\succeq0,\qquad
\langle C(z_q),A\rangle\le-1
$$

we have

$$
\begin{aligned}
J(A)
&\ge\langle B_\mu,A\rangle\\
&\ge-\alpha\langle C_\nu,A\rangle\\
&\ge\alpha.
\end{aligned}
$$

Thus, $\alpha>1$ directly vetoes the budget $J(A)<1$ for that patch. This deduction relies solely on PSD cone self-duality, non-negative probability weights, and discrete primal constraints; it is algebraic logic within the specified finite model.

The program calculates the critical value using the generalized minimum eigenvalue

$$
\alpha_*=-\frac{1}{
\lambda_{\min}(C_\nu,B_\mu)
}.
$$

If $\alpha_*>1$, the exported value uses

$$
\alpha_{\mathrm{safe}}
=1+\frac{\alpha_*-1}{2},
$$

and then directly checks the minimum eigenvalue of $W_{\mathrm{safe}}$. This is a floating safety margin, not an interval proof.

## 4. Scan Design

The first-layer uniform frontier uses:

- 14 radii:
  $4.5,5,5.5,6,7,8,9,10,10.25,10.5,11,12,14,16$;
- 3 basis densities: $6,8,10$;
- 3 width factors: $0.9,1.2,1.5$;
- 4 band sets: tail-only, single band $A_1$, three bands $A_0$ to $A_2$,
  five bands $A_0$ to $A_4$;
- 18 original patch centers;
- Uniform $3\times3$ core measures for each original patch.

The second-layer joint dual fixes the stronger dictionary from the uniform frontier:

$$
d=10,\qquad\text{width factor}=1.5.
$$

Each original patch is subdivided into $4\times4$, totaling

$$
18\cdot16=288.
$$

The joint search uses uniform ranking to select the most difficult

$$
2+2+3+5=12
$$

sub-rectangles, and performs cutting-plane optimization on the five-band axis measures and $3\times3$ core measures. This is not a complete joint exhaustion of the 288 sub-rectangles; however, if any single patch already has $\alpha_{\mathrm{safe}}>1$, the current covering strategy cannot be completed at that radius.

## 5. Uniform Frontier

For each radius, the optimal maximum threshold for the original patch uniform $3\times3$ is:

| $R$ | density | width factor | dimension | max patch threshold |
|---:|---:|---:|---:|---:|
| $9$ | $10$ | $1.5$ | $88$ | $1.570260$ |
| $10$ | $10$ | $1.5$ | $98$ | $1.478511$ |
| $10.25$ | $10$ | $1.5$ | $100$ | $1.464445$ |
| $12$ | $10$ | $1.5$ | $118$ | $1.152840$ |
| $14$ | $10$ | $1.5$ | $138$ | $0.540797$ |
| $16$ | $10$ | $1.5$ | $158$ | $0.414010$ |

This table shows that increasing the support indeed lowers the uniform witness threshold. However, "below $1$" only means that the specified uniform measure found no obstruction; it does not imply primal feasibility.

Two easily confused transitions are:

$$
R=10
$$

the first occurrence where all 18 centers of a certain geometry fall below $1$; and

$$
R=14
$$

the first occurrence where all 18 original patch uniform $3\times3$ thresholds of a certain geometry fall below $1$. Joint measure optimization subsequently overturned the interpretation of treating these transitions as feasibility thresholds.

## 6. Joint Dual Results

| $R$ | dimension | searched patches | strongest raw $\alpha$ | strongest $\alpha_{\rm safe}$ | safe $\lambda_{\min}$ |
|---:|---:|---:|---:|---:|---:|
| $10.25$ | $100$ | $2$ | $4.240160$ | $2.620080$ | $0.0713394$ |
| $12$ | $118$ | $2$ | $2.799900$ | $1.899950$ | $0.0834713$ |
| $14$ | $138$ | $3$ | $1.796359$ | $1.398180$ | $0.0992519$ |
| $16$ | $158$ | $5$ | $1.188563$ | $1.094281$ | $0.1149902$ |

All 12 serialized sparse-measure witnesses were reconstructed by `verify_saved_witnesses.py`. After renormalizing each set of serialized non-negative weights to sum to $1$:

- All 12 witnesses remain PSD;
- All 12 valid dual lower bounds are strictly greater than $1$;
- The maximum difference between the reconstructed and stored minimum eigenvalues is approximately $1.3\times10^{-15}$.

These are E2 floating finite-model results. v0.4 did not convert the matrices to rational numbers, nor did it interval-enclose the Fourier quadrature.

## 7. Axis Grid False Escapes

Performing grid refinement with a fixed configuration at $R=16$ on patch `x4_Y3__r2_3`:

| axis step size | raw $\alpha$ | $\alpha_{\rm safe}$ | safe $\lambda_{\min}$ |
|---:|---:|---:|---:|
| $0.25$ | $0.985277$ | $0.980351$ | $0.0346388$ |
| $0.1$ | $1.124306$ | $1.062153$ | $0.1149901$ |
| $0.05$ | $1.139551$ | $1.069775$ | $0.1149901$ |
| $0.025$ | $1.192293$ | $1.096146$ | $0.1149901$ |

Each discrete measure is itself a valid lower-bound witness; reducing the step size expands the searchable measure support, so an increasing lower bound is not contradictory. The coarse grid simply sampled the real-axis waveform at the wrong positions, missing the narrow peaks.

This introduces a new methodological rule:

> Any "dual escape" with $\alpha<1$ must undergo an audit with a denser axis grid or a continuous supremum upper bound; conversely, a reconstructed and PSD witness with $\alpha>1$ does not need to prove dual optimality to sufficiently veto that finite primal branch.

Therefore, the two sides of the dual are asymmetric:

- Finding $\alpha>1$ is positive evidence for a veto;
- Failing to find $\alpha>1$ is merely a search failure, not a proof of feasibility.

## 8. Primal Gate

This node adopts the following gate:

$$
\text{Only when all searched difficult patches are unblocked by safe dual witnesses,}
\quad\text{are high-cost primal searches initiated.}
$$

None of the four radii passed this gate. Therefore, no ray-cone primal Gram candidates were generated. `primal_diagnostics.json` only saves the dense audit of the complementary rank-one direction; their scaled objectives are approximately

$$
4.4040,\quad2.9649,\quad1.8478,\quad1.2832,
$$

all greater than $1$. These directions are merely diagnostics, not complete primal infeasibility proofs; the true vetoes come from the exported PSD dual witnesses.

## 9. Support and Prime Costs

From

$$
\operatorname{supp}\psi\subset[-R,R]
$$

we know the autocorrelation support is contained in $[-2R,2R]$. The prime-power term located at $m\log p$ in the explicit formula can only appear when

$$
m\log p<2R
$$

which is equivalent to

$$
p^m<e^{2R}.
$$

This cutoff relation is an exact support statement in the finite construction. The actual costs are as follows:

| $R$ | strict cutoff | number of primes | prime-power terms | status |
|---:|---:|---:|---:|---|
| $3$ | $403$ | $79$ | $98$ | actual enumeration |
| $7$ | $1{,}202{,}604$ | $93{,}117$ | $93{,}371$ | actual enumeration |
| $8.5$ | $24{,}154{,}952$ | $1{,}516{,}233$ | $1{,}517{,}020$ | actual enumeration |
| $9$ | $65{,}659{,}969$ | $3{,}877{,}186$ | $3{,}878{,}366$ | actual enumeration |
| $10.25$ | $799{,}902{,}177$ | $41{,}141{,}456$ | $41{,}144{,}807$ | actual enumeration |
| $12$ | $26{,}489{,}122{,}129$ | approx $1.10\times10^9$ | not enumerated | $x/\log x$ proxy |
| $14$ | $1{,}446{,}257{,}064{,}291$ | approx $5.17\times10^{10}$ | not enumerated | $x/\log x$ proxy |
| $16$ | $78{,}962{,}960{,}182{,}680$ | approx $2.47\times10^{12}$ | not enumerated | $x/\log x$ proxy |

The program linearly deposits the prime-power coefficients into log bins of width $0.01$. This reduces the number of subsequent matrix updates from once per prime-power to once per bin, but:

1. It does not eliminate prime enumeration;
2. It has not yet provided the interval error for bin interpolation;
3. $R=12,14,16$ only perform cost projections and have not built the full arithmetic matrix.

Thus, the histogram is an engineering compression, not a certificate compression.

## 10. Source Correction

The previous node adopted the arXiv abstract's

$$
|S(T)|
\le0.111\log T+0.275\log\log T+2.450.
$$

This node switches to the conservative constants from Trudgian's *Journal of Number Theory* version abstract:

$$
|S(T)|
\le0.112\log T+0.278\log\log T+2.510,
\qquad T\ge e.
$$

Consequently, the five-band floating count profiles all slightly increase. This node uses the published profile, but has still not implemented directed rounding or a theorem-hypothesis checker.

## 11. Decision

The data supports three conclusions:

1. Increasing $R$ indeed weakens the fixed uniform dual witness;
2. After jointly optimizing the axis measures, the sampled support-only route for $R\le16$ remains blocked;
3. The prime-side costs expand at $e^{2R}$, making the return on blindly continuing to increase $R$ too poor.

Therefore, the next round will no longer treat $R=18,20,\ldots$ as the primary search axis. A better direction is to have the dictionary itself actively suppress the five-band peaks:

$$
\min_{\mathcal D,A}
\left[
\langle T_{\mathcal D},A\rangle
+\sum_j\underline N_j
\sup_{x\in A_j}H_{\mathcal D,A}(x)
\right]
$$

while maintaining patch core negativity:

$$
\sup_{z\in P}B_{\mathcal D,A}(z)\le-1.
$$

This is a co-design problem of the dictionary, spectral notches, and the cover, rather than a single Gram rank or single radius problem.

## 12. Next Node

The next node is named:

`RH_Axis_Notch_Cover_Codesign_v0.5`

Minimum delivery standards:

1. Introduce controllable axis band notch constraints or null directions into the dictionary;
2. Use adaptive maximization to find the true peak of each band, instead of using a fixed coarse grid for pass determination;
3. First reuse the existing frontier at $R\in\{10.25,12,14,16\}$, without expanding to larger supports;
4. Bring the safe dual bound of at least one currently blocked patch down below $1$;
5. Perform primal Gram, dense core, and guard-ring audits only after the dual is unblocked;
6. The arithmetic histogram must be accompanied by a verifiable interpolation error, otherwise it cannot be upgraded to a certificate.

The stopping rule must also be explicit: if notch co-design can only shift the axis peaks to adjacent bands, or causes the core negativity to collapse simultaneously, then halt this dictionary family and pivot to an analytic kernel family, rather than continuing to increase dimensions.

## 13. Trust Boundaries

What this node establishes:

- Dual implications within the finite model;
- 126 sets of uniform frontiers;
- Structural covering of 288 sub-rectangles;
- 12 reconstructible floating dual witnesses;
- A counterexample of an axis grid false escape;
- A real prime enumeration benchmark at $R=10.25$;
- Cost projections for $R=12,14,16$.

What this node does NOT establish:

- Interval enclosures for Fourier quadrature;
- Upper bound certificates for continuous axis supremums;
- Complete joint exhaustion of the 288 patches;
- A theorem-certified tail matrix;
- Interpolation errors for the arithmetic histogram;
- A complete leakage budget for unknown off-axis regions;
- Any argument-principle certificate for the existence of zeros;
- A global contradiction from local patches to RH;
- A proof of RH, a disproof of RH, or a proof of an equivalent criterion.

Therefore, the correct way to read this document is:

> The current support-only finite-model strategy still faces clear dual obstructions when sampled up to $R=16$, and the prime costs for larger supports rapidly spiral out of control; the next step should be to change the spectral geometry of the dictionary.

It must not be rewritten as:

> All large-support test functions have failed, or RH has been decided.