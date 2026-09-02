# Local Interval Green Position Covering: Scale Elevation and Technical Convergence of the RH 58-Cell Operator Family Certificate

版本：v1.0  
日期：2026-07-25  
性質：Semi-AI autonomous research draft; technical convergence of this phase, not a proof of RH

## Abstract

This draft completes a local technical node of the preceding RH validity determination research: elevating the fixed rational positions or the extremely small uniform perturbation radius into a reproducible 58-dimensional independent position box certificate.

It continues to use the even clamped $H_0^2(-16,16)$ Green model from v0.7, two structural constraints, five frequency bands, $58$ on-axis rational atoms, and two core complex atoms; the sub-parameter is set to $\alpha=1$. Each axis position can vary independently:

$$
x_j\in[c_j-h,c_j+h],
\qquad 1\le j\le58.
$$

There are three new core tools:

1. Affine complex exponential representations that preserve shared position variables;
2. Analytic power series and explicit remainder terms for moments where the sum of exponents crosses zero;
3. Preservation of the low negative-rank structure with $60$ positive directions and $2$ negative directions, completing the universal interval determination via a Neumann–Schur–Sylvester chain.

The strongest tested and passed uniform radius is

$$
h_*=\frac{89}{50\,000\,000}
=1.78\times10^{-6}.
$$

The certificate yields

$$
\|I-RA\|_\infty
\le0.02755725053402449<1,
$$

$$
T_{11}\ge0.33057431704010146>0,
$$

$$
\det T
\ge6.693751188377321\times10^{-5}>0.
$$

Therefore, the abstract operator family within the entire $58$-dimensional maximal Cartesian product box is strictly positive. Any closed rational sub-box contained coordinate-wise within this box automatically inherits the certificate, forming a downward-closed covering certificate family.

Compared to the strict uniform radius of $2\times10^{-15}$ in v0.9, the exact radius elevation factor of this result is

$$
890\,000\,000.
$$

However, this result still does not connect the synthetic position family to actual zeta zero occupancy, nor does it complete the explicit formula admissibility and global elevation; therefore, it is not a proof of RH.

## 1. Research Problem

Preceding nodes have separated two tasks of completely different natures.

The first is positivity within the abstract continuous model: given test densities, a Green kernel, band coefficients, and core positive/negative directions, can one strictly prove the positivity of the operator after a finite-rank perturbation?

The second is validity on the zeta side: can these bands, positions, weights, and test functions be legitimately obtained from actual zero data and explicit formulas?

v0.7 has already completed the first type of certificate for a set of fixed rational atoms. v0.9 then used a generic operator norm budget to prove that positions can vary simultaneously within a radius of

$$
h_{0.9}=2\times10^{-15}
$$

but this scale is extremely conservative. The reason is not that the central witness is close to failing, but rather that the estimation first compresses the geometric information of each Green representer into a global worst-case constant, and then sums over the $58$ positions.

The problem of this node is thus clarified as:

> Can we directly perform directed interval arithmetic on the Green pairings, structural projections, and low negative-rank Schur complements within the position box, avoiding the premature loss of geometric structure?

## 2. Fixed Model

The radius is fixed at

$$
R=16,
$$

and the tail scale is fixed at

$$
\eta
=
\frac{31794183142988}{10^{18}}.
$$

Consider even test functions satisfying two structural conditions:

$$
\int_{-R}^{R}\psi(t)\,dt=0,
$$

$$
\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt=0.
$$

The five frequency bands contain

$$
[22,5,14,9,8]
$$

on-axis atoms respectively, totaling $58$. The axis density is

$$
\phi_x(t)=\cos(xt).
$$

There are also two fixed core atoms. They decompose into a core real density and a core imaginary density; the former forms the positive directions, and the latter forms the negative directions. After reducing the sub-parameter to $\alpha=1$, the projected Gram system has a total of $60$ positive directions and $2$ negative directions.

The "positions" here are merely parameters of the abstract witness. They have not yet been proven to equal the imaginary parts of any actual zeta zeros.

## 3. Interval Green Pairings

### 3.1 Complex Exponentialization

Each axis density is written as

$$
\cos(xt)
=
\frac12e^{ixt}
+\frac12e^{-ixt}.
$$

Therefore, all Green pairings can be transformed into complex exponential pairings

$$
K(z,w)
=
\int_{-R}^{R}
e^{zt}L^{-1}(e^{w\cdot})(t)\,dt,
$$

where $L=\eta D^4$, imposing clamped boundary conditions at both ends.

### 3.2 Closed Moment Representation

$L^{-1}(e^{wt})$ can be written as an exponential particular solution plus a cubic polynomial correction. The four polynomial coefficients are determined by

$$
u(-R)=u'(-R)=u(R)=u'(R)=0.
$$

All pairings ultimately only require a finite number of moments:

$$
M_p(z)
=
\int_{-R}^{R}t^p e^{zt}\,dt,
\qquad
0\le p\le4.
$$

If the rectangular interval of $z$ does not contain zero, one can use the recurrence

$$
M_p(z)
=
\frac{R^p e^{zR}-(-R)^p e^{-zR}}{z}
-\frac{p}{z}M_{p-1}(z).
$$

### 3.3 Zero-Crossing Moments

The position box introduces a new rigorous problem: $i x$ and $-i x$ within the same density may cause $z+w$ to cross zero, making the interval $1/(z+w)$ non-existent.

This node instead uses

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
\begin{cases}
0,&m\text{ is odd},\\
\dfrac{2R^{m+1}}{m+1},&m\text{ is even}.
\end{cases}
$$

If $|z|\le Z$, then

$$
|E_{N,p}(z)|
\le
\frac{2R^{p+1}}{p+1}
e^{ZR}
\frac{(ZR)^{N+1}}{(N+1)!}.
$$

The implementation takes $N=28$. This allows the analyticity near zero to appear directly in the certificate, no longer being represented as a spurious reciprocal singularity.

## 4. Shared Position Variables

Using only ordinary rectangular intervals still creates severe dependency loss. If the same position $x_j$ appears in two places, ordinary interval arithmetic might treat the two occurrences as independent, relaxing the exact equality

$$
i x_j-i x_j=0
$$

into a non-zero interval.

v1.0 therefore lets each exponent first preserve the affine form

$$
z=z_0+\sum_j a_j\delta_j,
\qquad
|\delta_j|\le h.
$$

Variables $\delta_j$ with the same name are merged first during addition and subtraction; they are converted into directed rectangular intervals only when entering non-linear steps such as exponentials, reciprocals, or high powers. This modification preserves the most important linear cancellations within the same atom, while still allowing different positions to be independent.

## 5. Structural Projection and Low Negative-Rank Determination

Let the Green–Gram matrix of the two structural densities be $S$, the structural cross matrix be $B$, and the unprojected Gram matrix of all evaluated densities be $G$. After projection

$$
G^\perp
=
G-B^\mathsf{T}S^{-1}B.
$$

Partition $G^\perp$ according to the $60$ positive directions and $2$ negative directions. If the diagonal matrices of positive and negative weights are $D_+$ and $D_-$, let

$$
A=I+G_{++}D_+.
$$

The floating-point midpoint matrix is only used to generate a candidate inverse $R$. Once written in finite decimal form, the candidate matrix is treated as an exact rational number in the verifier. If

$$
\|I-RA\|_\infty<1,
$$

then $A^{-1}$ and

$$
X=A^{-1}G_{+-}
$$

can be strictly bounded by the Neumann series.

The final negative direction determination matrix is

$$
T
=
D_-^{-1}
-G_{--}
+G_{-+}D_+X.
$$

Since the negative rank is only $2$, it suffices to prove

$$
T_{11}>0,
\qquad
\det T>0.
$$

This is precisely the value of preserving the low negative-rank structure: there is no need to perform a crude minimum eigenvalue estimation on the entire $62$-dimensional interval matrix.

## 6. Main Theorem

### Theorem

Under the above fixed abstract model and sub-parameter $\alpha=1$, let

$$
h_*=\frac{89}{50\,000\,000}.
$$

If the $58$ axis positions in the five bands respectively satisfy

$$
x_j\in[c_j-h_*,c_j+h_*],
$$

and can be chosen independently of each other, then the resulting projected Green operator is strictly positive.

### Certificate Values

Directed interval recomputation yields

$$
\|I-RA\|_\infty
\le
0.0275572505340244852914879709,
$$

thus the positive block is invertible. Finally

$$
T_{11}
\ge
0.3305743170401014605302036438,
$$

and

$$
\det T
\ge
0.0000669375118837732116365347031.
$$

Both lower bounds are strictly positive, hence the theorem holds.

### Covering Family

The theorem proves the maximal box

$$
\mathcal B_{h_*}
=
\prod_{j=1}^{58}[c_j-h_*,c_j+h_*]
$$

in one go. For any closed rational interval $J_j$, if

$$
J_j\subseteq[c_j-h_*,c_j+h_*],
$$

then

$$
\prod_{j=1}^{58}J_j
\subseteq
\mathcal B_{h_*}.
$$

Therefore, all such sub-boxes constitute a downward-closed certificate family. Formally there is only one maximal leaf, but semantically it covers infinitely many sub-boxes and all position configurations within the box.

## 7. Scale Ladder and Failure Semantics

The radius ladder results are as follows.

| $h$ | Result | Prover State |
|---:|---|---|
| $0$ | Passed | Center point |
| $10^{-8}$ | Passed | Neumann and Sylvester passed |
| $10^{-6}$ | Passed | Neumann and Sylvester passed |
| $1.78\times10^{-6}$ | Passed | Strongest tested passed value |
| $1.8\times10^{-6}$ | Uncertain | Sylvester determinant lower bound failed |
| $10^{-4}$ | Uncertain | Neumann defect upper bound greater than $1$ |
| $10^{-3}$ | Uncertain | Neumann defect upper bound greater than $1$ |

At $h=1.8\times10^{-6}$, the Neumann defect is still only about $0.02787$, but the final determinant interval lower bound drops to about $-0.0012315$. This indicates that the interval dependency loss of the Schur term appears first.

At $h=10^{-4}$ and $h=10^{-3}$, the defect upper bounds are approximately

$$
1.54837
\quad\text{and}\quad
15.5092,
$$

respectively, thus the Neumann verification for the candidate inverse can no longer be initiated.

These failures are merely "currently uncertain for the prover". They are neither negative eigenvalue certificates nor position counterexamples.

## 8. Exact Corner Counter-Diagnosis

To completely separate "interval failure" and "point counterexample" at the data level, this node takes a set of deterministic signs given by the v0.9 floating-point corner search, and changes each position to an exact rational point

$$
x_j=c_j+s_j10^{-3},
\qquad
s_j\in\{-1,+1\}.
$$

Using a zero-width full Green–Schur interval recomputation on this single point yields

$$
\det T
\ge
0.1098330850588932>0.
$$

Therefore, there is at least one strictly positive point located on the boundary of the failed large box at $h=10^{-3}$. This result does not prove that the entire large box is positive, but it strictly proves that "large box verification failure" cannot be treated as "failure at that corner".

## 9. Comparison with v0.9

The strict uniform radius of v0.9 is

$$
h_{0.9}
=
\frac{1}{500\,000\,000\,000\,000}.
$$

The radius elevation of this node is

$$
\frac{h_*}{h_{0.9}}
=
890\,000\,000.
$$

This massive elevation is not due to modifying the central witness, but due to changes in the proof representation:

- v0.9 first controls each rank-one term using a global Green norm;
- v1.0 directly bounds the Green pairings;
- v1.0 preserves the structural projection;
- v1.0 preserves the Schur geometry with only two negative directions;
- v1.0 performs affine cancellation for shared positions.

However, the floating-point diagnosis of the parent v0.9 only observed a potential turning point at around $0.016$ to $0.017$, while the strict radius is only $1.78\times10^{-6}$. The two still differ by about four orders of magnitude. This is not a contradiction: floating-point corner search is not a universal proof, and rectangular Gram intervals ignore many shared dependencies across matrix terms.

## 10. Trust Boundaries and Research Determination

The correct conclusion of v1.0 is:

> In the fixed abstract Green model, the specified $58$ synthetic positions can vary within independent boxes of radius $1.78\times10^{-6}$, while the entire operator family still possesses a strictly positive certificate.

The following statements are not yet established:

- These $58$ positions are the actual zeta zeros;
- The actual zeros have the occupancy or weights required by the witness in the corresponding five bands;
- The selected test functions have satisfied the full zeta explicit formula admissibility;
- The prime-side coefficients have been strictly transferred to this Green model;
- The local finite-dimensional certificate has been elevated to a full critical strip determination;
- RH has been proven.

Therefore, the classification is fixed as:

- `actual_zeta_occupancy_family = false`
- `explicit_formula_transfer_certified = false`
- `global_rh_certificate = false`

## 11. Technical Convergence of This Phase

The original direction of this round was "banding, multiple test functions, covering certificate families". By v1.0, these three have formed a consistent node at the abstract model layer:

- Banding: The five bands and the $[22,5,14,9,8]$ atomic structure are completely preserved;
- Multiple test functions: $58$ axis densities, two core real densities, and two core imaginary densities jointly enter the projected Gram matrix;
- Covering certificate family: A maximal $58$-dimensional box and all downward-closed sub-boxes are covered by the same universal certificate.

This is a suitable point to halt technical expansion for this phase. Moving forward, the most valuable mathematical work is not to continue fine-tuning the last few digits of the radius, but to address two real bridges:

1. The legitimate mapping between actual zeta zero occupancy and the synthetic $58$-position witness;
2. The strict transfer among explicit formula test functions, coefficient cones, and abstract Green positivity.

According to this research workflow, the next round will compile a comprehensive report from v0.1 to v1.0, including valid and failed routes, the claim register, the gap ledger, and subsequent AI handovers. This draft only completes the v1.0 technical node and does not prematurely pretend to have completed that overall synthesis.