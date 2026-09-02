# Occupancy Operator Families and Covering Green Certificates

## RH Location Quantifier Semantic Bridge, Exact Synthetic Models, and Micro-Radius Transfer

### v0.9 Semi-AI Autonomous Research Draft

Date: 2026-07-25  
Node: `RH-Occupancy-OperatorFamily-20260725-v0.9`

---

## Abstract

The previous node v0.8 completed the type correction for zero-count coefficients: a band count upper bound can legitimately generate a supremum leakage upper envelope; a band count lower bound can only generate an infimum scalar lower bound, and cannot be multiplied by an arbitrary probability measure to be interpreted as the operator mass of actual zeros. This correction removes the original objective of "making per-band counting coefficients more precise" from the main storyline. What is truly missing is the zero location information and an operator theorem that holds simultaneously for all permissible locations.

This document rewrites the next stage as

$$
\text{cell occupancy}
\longrightarrow
\text{uncertain locations}
\longrightarrow
\text{universal operator family}
\longrightarrow
\text{cover certificate}.
$$

This round achieves results on three levels.

First, it establishes `OccupancySelectionOperatorTransfer`: if each sourced cell contains at least the specified multiplicity of actual points, and the selected-point operator is jointly PSD for all locations within the cells, then the operator containing all actual points is also PSD. This deduction solely relies on "unselected points providing additional PSD terms" and completely eliminates the need for arbitrary dual measures.

Second, it establishes a fully rational prototype in the Dirichlet Green RKHS of

$$
H_0^1(0,1)
$$

Knowing merely that the total count is $2$, one can place both points at $1/5$, yielding the exact Schur determinant

$$
-\frac{254}{558009}<0.
$$

Conversely, if it is known that two separated left and right cells contain at least one point each, an adaptive interval cover can prove positivity for all unknown locations. The natural interval extension of the root box itself is inconclusive; after bisection, it yields $8$ certified leaves with a maximum depth of $7$ and a minimum determinant lower bound of approximately $1.0797\times10^{-5}$.

Third, it utilizes the fixed-location abstract interval theorem completed in v0.7. Reducing $\alpha=21/20$ to $\alpha=1$ generates an exact $1/21$ identity margin; then, using the Poincaré inequality twice and a rank-one perturbation bound, it expands each of the original $58$ fixed axis atoms into independent closed location cells. At a uniform half-width of

$$
2\times10^{-15}
$$

the coercivity lower bound of the entire family is proven to be approximately $0.00644077361$.

A floating-point adversarial corner study observes the threshold crossing $1$ between half-widths $0.016$ and $0.017$. This is not a universal theorem, but it indicates a gap of approximately

$$
8\times10^{12}
$$

between the exact Poincaré budget and the local numerical scale. Therefore, the next node should develop local interval Green derivatives and adaptive Schur cell covers, rather than returning to scalar count refinement.

This document contains no theorem-backed $\zeta$ occupancy cells, does not complete the explicit formula global transfer, and constitutes neither a proof nor a disproof of RH. All global RH flags remain false.

---

## 1. Research Positioning: Shifting from Counting Semantics to Location Quantifiers

### 1. ZFC and Propositional Boundaries

Theoretically, RH can only be resolved by a proof chain based on ZFC, with traceable dependencies and immutable definitions. If a core operator identity, trace formula, topological obstruction, or positivity theorem holds only in an extended system that has not been translated back to ZFC, it at best supports an analogous proposition within that extended system.

The purpose of this research is not to claim RH first and then retroactively fill in the gaps; rather, it is to compile every suspicious deduction into:

- Explicit input types;
- Explicit quantifiers;
- Machine-readable dependencies;
- Fallible verifiers;
- GAPs that cannot be obscured by name substitutions.

### 2. Irreversible Corrections Left by v0.8

Fix a band $A_j$, an actual zero multiset $\Gamma_j$, and a non-negative function $H$. If

$$
|\Gamma_j|\le U_j,
$$

then

$$
\sum_{\gamma\in\Gamma_j}H(\gamma)
\le
U_j\sup_{x\in A_j}H(x).
$$

If

$$
|\Gamma_j|\ge L_j,
$$

then

$$
\sum_{\gamma\in\Gamma_j}H(\gamma)
\ge
L_j\inf_{x\in A_j}H(x).
$$

The second equation cannot be rewritten as a lower bound

$$
L_j\int H\,d\mu_j
$$

for an arbitrary probability measure $\mu_j$. This is not an issue of error magnitude, but an issue of quantifiers and data types.

Therefore, if the operator $P_x$ rotates with location, knowing that "there is at least one point in the band" generally cannot produce a non-zero fixed common floor

$$
Q\preceq P_x
\qquad
\forall x\in A_j.
$$

This round shifts to preserving $x$ and directly proving the family.

---

## 2. Minimum Valid Data for Occupancy Certificates

### 1. Source Cells and Operator Hulls

Each occupancy record must contain at least:

| field | Meaning |
| --- | --- |
| `cell_id` | Stable identifier |
| rational endpoints | Exactly reproducible intervals |
| endpoint convention | Open/closed endpoints for counting partitions |
| `multiplicity_lower` | Minimum number of actual points in the cell |
| `presence_theorem_id` | Source proving existence |
| source hash | Source version lock |
| certification status | synthetic, floating, or rigorous |

The endpoint convention of source cells is responsible for preventing boundary points from being double-counted. The uncertainty interval of the operator family can use the closed hull of the source cell, because expanding the set of permissible locations only makes the universal theorem stronger and more conservative.

### 2. Indispensable Quantifiers

A valid occupancy premise is

$$
\#(\Gamma\cap I_r)\ge\ell_r.
$$

Next, one must select

$$
x_{rk}\in I_r,
\qquad
1\le k\le\ell_r,
$$

and preserve

$$
\forall(x_{rk})
$$

until the operator inequality is completed. If the locations are averaged out midway using some convenient atomic measure, it reverts back to the deduction already rejected in v0.8.

---

## 3. Occupancy Selection Operator Transfer

Let $\mathcal H$ be a real Hilbert space, and let

$$
P_x=p_x\otimes p_x\succeq0.
$$

Fix a base operator $C$, which may contain finite-rank negative directions. For each cell, select $\ell_r$ locations and define

$$
W_{\mathrm{sel}}(\mathbf x)
=
C+
\sum_r\sum_{k=1}^{\ell_r}\lambda_rP_{x_{rk}},
\qquad
\lambda_r\ge0.
$$

### Theorem

If the occupancy premise holds for each cell, and

$$
W_{\mathrm{sel}}(\mathbf x)\succeq0
$$

holds jointly for all permissible selections, then the operator containing all actual points is also PSD.

### Proof

Select $\ell_r$ points from the actual points in each cell to form $\mathbf x_\Gamma$. The full operator equals

$$
W_{\mathrm{all}}(\Gamma)
=
W_{\mathrm{sel}}(\mathbf x_\Gamma)
+
\sum_{z\in\Gamma_{\mathrm{surplus}}}
\lambda(z)P_z.
$$

The first term is PSD by the universal theorem; the second term is a non-negative weighted rank-one PSD sum. Thus,

$$
W_{\mathrm{all}}(\Gamma)\succeq0.
$$

Q.E.D.

### What This Theorem Truly Fixes

It does not claim that the scalar count becomes an operator lower mass. It merely states:

1. The occupancy theorem allows selecting points from the actual configuration;
2. The universal family theorem already covers all possible selections;
3. The surplus points of the actual configuration only add PSD terms.

Therefore, the content of the operator transfer is entirely borne by "selection" and "surplus PSD".

---

## 4. Green–Schur Families with Small Negative Rank

Let the positive representers be $U$, the negative representers be $V$, and consider

$$
W
=
I+UD_\lambda U^\ast-VD_\beta V^\ast.
$$

The positive operator

$$
B=I+UD_\lambda U^\ast
$$

is always strictly positive. By the Schur complement,

$$
W\succeq0
\quad\Longleftrightarrow\quad
D_\beta^{-1}-V^\ast B^{-1}V\succeq0.
$$

Applying the Woodbury identity:

$$
B^{-1}
=
I-U
\left(D_\lambda^{-1}+U^\ast U\right)^{-1}
U^\ast.
$$

Let the Green Gram blocks be $K_{XX},K_{XY},K_{YY}$, yielding

$$
S
=
D_\beta^{-1}
-K_{YY}
+K_{YX}
\left(D_\lambda^{-1}+K_{XX}\right)^{-1}
K_{XY}.
$$

Unknown occupancy locations only enter these Gram blocks. When the negative rank $q=2$, the final universal test only requires

$$
S_{11}>0,
\qquad
\det S>0.
$$

Thus, "having many location variables" does not necessarily equate to "having a large final sign matrix". The true engineering problem is how to strictly enclose each Green pairing and positive solve.

---

## 5. Fully Rational Dirichlet Green Prototype

### 1. Reasons for Choosing This Model

Take

$$
\mathcal H=H_0^1(0,1)
$$

and the inner product

$$
\langle f,g\rangle
=
\int_0^1f'(t)g'(t)\,dt.
$$

Its evaluation Green kernel is

$$
K(s,t)=\min(s,t)-st.
$$

This is a genuine infinite-dimensional RKHS Green kernel, yet it can still be computed using pure `Fraction`s on rational cells. It is suitable for isolating quantifiers, covers, and Schur engineering first, without mixing transcendental interval arithmetic into the first prototype.

### 2. Model Parameters

The two occupancy cells are

$$
I_1=
\left[\frac15,\frac25\right],
\qquad
I_2=
\left[\frac35,\frac45\right].
$$

The negative targets are

$$
y_1=\frac13,
\qquad
y_2=\frac23,
$$

and

$$
\beta_1=\beta_2=\frac{83}{25}.
$$

The target family is:

$$
W(x_1,x_2)
=
I+P_{x_1}+P_{x_2}
-\frac{83}{25}
\left(P_{1/3}+P_{2/3}\right).
$$

### 3. Exact Counterexample for Total Count $2$

If it is only known that there are two points within the broad union, then the configuration

$$
x_1=x_2=\frac15
$$

is still permitted. In this case, the positive system is

$$
A=
\begin{pmatrix}
\frac{29}{25}&\frac4{25}\\
\frac4{25}&\frac{29}{25}
\end{pmatrix}.
$$

The Schur matrix is

$$
S=
\begin{pmatrix}
\frac{2611}{24651}&-\frac{29}{297}\\
-\frac{29}{297}&\frac{2113}{24651}
\end{pmatrix},
$$

whose determinant is

$$
\det S=-\frac{254}{558009}<0.
$$

and it has an explicit negative direction

$$
v=
\left(
-\frac{29}{297},
-\frac{2611}{24651}
\right),
$$

satisfying

$$
v^\mathsf TSv
=
-\frac{663194}{13755479859}<0.
$$

Therefore, a total count of $2$ is insufficient; one point in each of the left and right cells is the type truly required by this operator statement.

---

## 6. Covering Certificate Families

### 1. Why the Root Box Cannot Pass Directly

Performing an interval extension directly on

$$
I_1\times I_2
$$

causes repeated variables to be treated as independent endpoint selections, leading to dependency overestimation. The lower endpoint of the determinant enclosure for the root box is negative, so the single-box verifier must reject it.

The status of this rejection is:

`split_inconclusive`

rather than:

`operator_counterexample`.

### 2. Adaptive Rules

For each box, sequentially:

1. Enclose $K_{XX},K_{XY},K_{YY}$;
2. Enclose

   $$
   A^{-1}
   =
   \left(D_\lambda^{-1}+K_{XX}\right)^{-1};
   $$

3. Enclose $S$;
4. Check the lower endpoints of $S_{11}$ and $\det S$;
5. If insufficient, bisect along the exact midpoint of the widest coordinate;
6. If widths are equal, select the smallest coordinate index.

All nodes store their path, box, split, Schur intervals, and status. Leaf box paths must be prefix-free, and children must completely cover their parent.

### 3. Results

| Metric | Result |
| --- | ---: |
| root directly certified | false |
| tree nodes | $15$ |
| certified leaves | $8$ |
| unresolved leaves | $0$ |
| maximum depth | $7$ |

The first leading minor lower bounds of all leaves are positive. The minimum determinant lower bound is

$$
\frac{
996149099768633906407318481
}{
92259342242007809509970517515625
}
\approx
1.07972708\times10^{-5}.
$$

Therefore,

$$
W(x_1,x_2)\succ0
$$

holds for all

$$
(x_1,x_2)\in I_1\times I_2
$$

.

This example also illustrates the specific utility of "covering topology" in this method: it does not treat some intuitive space name as a proof, but rather partitions the parameter box into a finite closed cover, allowing each local chart to carry a reproducible inequality certificate, and finally recovers the global quantifier via cover completeness.

---

## 7. From Fixed Atoms to a $58$-Cell Clamped Family

### 1. Parent Theorem and Convex Margin

v0.7 has interval-certified the fixed-location abstract operator

$$
W_{21/20}(\mathbf c)\succeq0.
$$

Let the axis positive part be $A(\mathbf c)$, and the core indefinite part be linear with respect to $\alpha$. Then

$$
W_1(\mathbf c)
=
\frac{20}{21}W_{21/20}(\mathbf c)
+
\frac1{21}\left(I+A(\mathbf c)\right)
\succeq
\frac1{21}I.
$$

The crucial point of this transformation is: there is no need to guess the minimum eigenvalue of the full operator from the parent interval Schur matrix; the identity margin is exactly given by the convex combination.

### 2. Global Green Norm Upper Bound

In the clamped space on $[-R,R]$, take the energy

$$
\tau\int_{-R}^{R}|u''(t)|^2\,dt.
$$

Applying the Poincaré inequality twice gives

$$
\|u\|_2
\le
\frac{(2R)^2}{\pi^2}\|u''\|_2.
$$

Thus, the $L^2$ norm of the Green inverse can be bounded by

$$
\|G\|_{2\to2}
\le
\frac{(2R)^4}{\pi^4\tau}
<
\frac{(2R)^4}{81\tau}
=C_G
$$

The axis density and its location derivative are

$$
f_x(t)=\cos(xt),
\qquad
\partial_xf_x(t)=-t\sin(xt).
$$

Hence,

$$
\|f_x\|_2\le\sqrt{2R},
\qquad
\|\partial_xf_x\|_2
\le
\sqrt{\frac{2R^3}{3}}.
$$

If $p_x$ is a projected representer, the structural projection does not increase the norm. Using

$$
\|p_x\otimes p_x-p_c\otimes p_c\|
\le
\|p_x-p_c\|
\left(\|p_x\|+\|p_c\|\right)
$$

and

$$
\sqrt3>\frac53,
$$

we obtain

$$
\|P_x-P_c\|
<
\frac{12}{5}R^2C_G|x-c|.
$$

### 3. Multi-Cell Budget

Let the $58$ axis operator weights be $\lambda_i$. Their exact sum is

$$
\Lambda
=
\sum_i\lambda_i
=
\frac{10287970888727}{125000000000}.
$$

For independent locations

$$
x_i\in[c_i-h,c_i+h]
$$

we have

$$
\left\|
\sum_i\lambda_i(P_{x_i}-P_{c_i})
\right\|
\le
\frac{12}{5}R^2C_G\Lambda h.
$$

Taking

$$
h=\frac{1}{500000000000000},
$$

yields the perturbation upper bound

$$
\varepsilon
=
\frac{
12328822128706060288
}{
299401138693037109375
}
\approx0.04117827401.
$$

Since

$$
\varepsilon<\frac1{21},
$$

it holds jointly for all $58$ independent locations:

$$
W_1(\mathbf x)
\succeq
\frac{
13498624663403281109
}{
2095807970851259765625
}I
\succ0.
$$

### 4. Exact Classification of This Certificate

It is:

- an exact rational perturbation theorem;
- conditional on the v0.7 parent interval theorem;
- universal over $58$ independent location cells;
- coordinate-dependent on v0.7 dual atom centers and weights.

It is not:

- a $\zeta$ zero occupancy theorem;
- an operator realization of a count lower profile;
- an unresolved-height exclusion;
- an RH certificate.

---

## 8. Floating-Point Local Scale Diagnostics

### 1. Adversarial Corner Search

To estimate the conservativeness of the global Poincaré bound, this document uses a direct clamped Green reconstruction to perform an E2 diagnostic:

1. Perform central difference at each center location;
2. Take the gradient-sign corner that lowers the fixed-measure threshold;
3. Attempt to flip the corner sign coordinate by coordinate;
4. Up to four rounds, until there is no further improvement.

### 2. Results

| half-width | threshold at $\Delta t=0.02$ |
| ---: | ---: |
| $0.012$ | $1.0458517424$ |
| $0.014$ | $1.0240427949$ |
| $0.015$ | $1.0124640056$ |
| $0.016$ | $1.0004604738$ |
| $0.017$ | $0.9880516263$ |
| $0.018$ | $0.9748129050$ |
| $0.020$ | $0.9471623347$ |

For the same corner at $h=0.016$, the time-step refinement is

$$
\begin{array}{c|c}
\Delta t&\text{threshold}\\
\hline
0.02&1.0004604738\\
0.01&1.0004696571\\
0.005&1.0004702150
\end{array}
$$

For $h=0.017$, it is

$$
\begin{array}{c|c}
\Delta t&\text{threshold}\\
\hline
0.02&0.9880516263\\
0.01&0.9880608157\\
0.005&0.9880613743
\end{array}
$$

### 3. No Over-Interpretation

This search:

- does not exhaust all $2^{58}$ corners;
- does not cover interiors;
- lacks interval enclosure;
- a threshold below $1$ is merely a floating candidate.

Therefore, it cannot prove the failure of a certain cell family. It only provides the local scale and a target for the next verifier design.

### 4. Proof-Budget Gap

The exact uniform half-width is

$$
2\times10^{-15},
$$

while the last half-width measured in floating-point with a threshold above $1$ is

$$
0.016.
$$

The ratio between the two is

$$
8\times10^{12}.
$$

This indicates that the most worthwhile improvements for the next step are:

- local frequency-sensitive Green resolvent bounds;
- interval derivatives in $x$;
- Taylor models;
- adaptive location covers;
- low-rank Schur interval solves.

Merely continuing to refine the global Poincaré constant typically cannot bridge a gap of thirteen orders of magnitude.

---

## 9. GAP Map

### Closed

#### `G09-SEM-01`

The operator transfer for occupancy selection is closed.  
Evidence: Symbolic deduction and exact semantic output.

#### `G09-SEM-02`

Total count cannot replace per-band occupancy.  
Evidence: Determinant $-254/558009$ and explicit negative direction.

#### `G09-COVER-01`

The exact rational Green cover engine is closed.  
Evidence: $8$ leaves, no unresolved nodes, complete reproducible verification.

#### `G09-CLAMP-01`

The conditional elevation of fixed parent atoms to micro-radius location families is closed.  
Evidence: $58$ cells and an exact positive coercivity lower bound.

### Still Open

#### `G09-GREEN-LOCAL`

Missing local directed enclosure of clamped Green pairings for location cells.  
Priority: Highest.

#### `G09-ZETA-OCC`

Missing cell presence theorems, endpoint nonzero certificates, multiplicities, and source hashes for actual $\zeta$ zeros.  
Priority: Highest.

#### `G09-EF-TRANSFER`

Missing ZFC dependency chains for test-function admissibility, zero-side operator expressions, and prime-side nonnegative cones.  
Priority: Highest.

#### `G09-UPPER-NOGO`

The v0.7 upper-envelope method no-go still requires directed source certification for upper counts and tail coefficients.  
Route: Track A, separated from actual occupancy.

#### `G09-GLOBAL`

Missing unresolved-height covers, local-to-global exhaustion, and full critical band transfer.  
Priority: Deferred but necessary.

---

## 10. Next Node

The next node is fixed as:

`RH-LocalIntervalGreen-CellCover-20260725-v0.10`

### Work Package A: Local Green Enclosure

Establish directed bounds for

$$
\langle p_x,p_y\rangle
$$

over $x,y$ cells, prioritizing the inclusion of first- and second-order location derivatives.

### Work Package B: Adaptive Schur Cover

Sequentially test the half-width ladder

$$
10^{-8},\ 10^{-6},\ 10^{-4},\ 10^{-3}.
$$

Each failure must distinguish between:

- point counterexamples;
- interval dependencies;
- inverse enclosures;
- Sylvester lower bounds;
- resource stops.

### Work Package C: Occupancy Source Schema

Only implement the data types and verifiers for presence certificates; do not claim actual zeta-facing exclusions before the kernel family has handled macroscopic cells.

---

## Conclusion

The most important advancement in this round is not a specific threshold number, but transforming the negative results of v0.8 into a positive, executable alternative architecture:

$$
\boxed{
\text{Sourced cell occupancy}
+
\text{Preserving all location quantifiers}
+
\text{Low negative-rank Schur family}
+
\text{Finite covering certificates}
}
$$

The fully rational Green prototype proves that this architecture works, and that scalar count-only approaches indeed fail. The v0.7 parent theorem further makes the first $58$-cell clamped family a rigorous result, even though the current radius is only $2\times10^{-15}$.

The floating-point local diagnostics have not been over-interpreted as a theorem; their purpose is to locate the thirteen-order-of-magnitude proof-budget gap. The next step should replace the global norm bound with local interval Green geometry, allowing covering certificates to truly enter usable scales.

Final status:

- exact synthetic occupancy family: true;
- conditional abstract clamped family: true;
- actual zeta occupancy family: false;
- explicit-formula global transfer: false;
- global RH certificate: false.