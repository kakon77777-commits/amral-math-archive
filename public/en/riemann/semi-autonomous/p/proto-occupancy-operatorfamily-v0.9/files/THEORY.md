# Theory

## 0. Positioning

Theoretically, RH can only be resolved by a proof dependency chain based on and traceable to ZFC; if the core proposition relies on another set of axioms or an analogical system that has not been translated back to ZFC, the resulting conclusion can only be a proposition within that extended system. This document is not a proof of RH, but rather an investigation into "how the determination of RH-related operators can possess valid quantifiers and dependency semantics."

v0.8 has proven:

$$
\text{count lower}
\not\Longrightarrow
\text{arbitrary dual-measure operator lower mass}.
$$

Therefore, this node no longer suppresses position variables, but instead adopts occupancy cells and a universal operator family.

## 1. Data Type of Cell Occupancy

Let $\Gamma$ be the actual point set with multiplicities. Each source cell $I_r$ stores at least:

- the rational endpoints of the cell;
- the endpoint convention;
- the multiplicity lower bound $\ell_r$;
- the presence theorem identifier;
- the source hash and certification status.

The source cells must form a non-overlapping counting partition according to the endpoint convention; when proving the operator, each source cell can be expanded to its closed hull, because enlarging the set of unknown positions only makes the universal claim more conservative.

A valid statement is

$$
\#(\Gamma\cap I_r)\ge\ell_r.
$$

It is neither a probability measure nor a fixed rank-one operator.

## 2. Occupancy selection transfer theorem

Let $\mathcal H$ be a real Hilbert space, where for each position $x$ we have

$$
P_x=p_x\otimes p_x\succeq0.
$$

Fix a base operator $C$ that may contain negative directions. For each cell, select $\ell_r$ positions

$$
x_{rk}\in I_r,
\qquad
1\le k\le\ell_r,
$$

and define the selected operator

$$
W_{\mathrm{sel}}(\mathbf x)
=
C+
\sum_r\sum_{k=1}^{\ell_r}\lambda_rP_{x_{rk}},
\qquad
\lambda_r\ge0.
$$

### Theorem `OccupancySelectionOperatorTransfer`

If:

1. Each $I_r$ actually contains at least $\ell_r$ points;
2. For all admissible selections $\mathbf x$, we have

   $$
   W_{\mathrm{sel}}(\mathbf x)\succeq0;
   $$

3. All unselected actual points contribute to $P_x$ with the same non-negative coefficient $\lambda_r$;

then the operator containing all actual points is also PSD.

### Proof

Select $\ell_r$ points from the actual points in each cell to obtain an admissible $\mathbf x_\Gamma$. The full operator can be written as

$$
W_{\mathrm{all}}(\Gamma)
=
W_{\mathrm{sel}}(\mathbf x_\Gamma)
+
\sum_{\text{surplus actual points }z}
\lambda(z)P_z.
$$

The first term is PSD by the universal premise; the second term is a finite sum of PSD operators. Therefore,

$$
W_{\mathrm{all}}(\Gamma)\succeq0.
\qquad\square
$$

This theorem preserves the quantifier order of "first having source-backed occupancy, then proving for all unknown positions," without introducing arbitrary dual measures.

## 3. Low Negative-Rank Green–Schur Reduction

Let the positive and negative representers form the columns

$$
U=(u_1,\ldots,u_m),
\qquad
V=(v_1,\ldots,v_q),
$$

and let $D_\lambda, D_\beta$ be positive diagonal matrices. Consider

$$
W
=
I+UD_\lambda U^\ast-VD_\beta V^\ast.
$$

Denote

$$
B=I+UD_\lambda U^\ast\succ0.
$$

By the finite-rank Schur complement,

$$
W\succeq0
\quad\Longleftrightarrow\quad
S
:=
D_\beta^{-1}-V^\ast B^{-1}V
\succeq0.
$$

The Woodbury identity gives

$$
B^{-1}
=
I-U
\left(D_\lambda^{-1}+U^\ast U\right)^{-1}
U^\ast.
$$

Therefore,

$$
S
=
D_\beta^{-1}
-K_{YY}
+K_{YX}
\left(D_\lambda^{-1}+K_{XX}\right)^{-1}
K_{XY}.
$$

If $q=2$, it suffices to prove

$$
S_{11}>0,
\qquad
\det S>0.
$$

The dimension of the unknown positions can be very high, but the final sign test is still only performed on the negative rank $q$.

## 4. Fully Rational Dirichlet Green Prototype

Take

$$
\mathcal H=H_0^1(0,1),
\qquad
\langle f,g\rangle_{\mathcal H}
=
\int_0^1f'(t)g'(t)\,dt.
$$

The Green kernel of the evaluation representer is

$$
K(s,t)=\min(s,t)-st.
$$

The synthetic model in this round fixes

$$
I_1=
\left[\frac15,\frac25\right],
\qquad
I_2=
\left[\frac35,\frac45\right],
$$

two negative positions

$$
y_1=\frac13,
\qquad
y_2=\frac23,
$$

and

$$
\beta_1=\beta_2=\frac{83}{25}.
$$

The universal family to be proven is

$$
W(x_1,x_2)
=
I+P_{x_1}+P_{x_2}
-\frac{83}{25}
\left(P_{1/3}+P_{2/3}\right)
\succeq0
$$

holds for all

$$
(x_1,x_2)\in I_1\times I_2.
$$

### 4.1 Why a Total Count of $2$ is Still Insufficient

If we only retain a total count of $2$ within the broad union, it allows both points to be located at $1/5$. In this case, the exact Schur matrix is

$$
S=
\begin{pmatrix}
\frac{2611}{24651}&-\frac{29}{297}\\
-\frac{29}{297}&\frac{2113}{24651}
\end{pmatrix},
$$

and

$$
\det S
=
-\frac{254}{558009}<0.
$$

Take

$$
v=
\left(
-\frac{29}{297},
-\frac{2611}{24651}
\right),
$$

then

$$
v^\mathsf TSv
=
-\frac{663194}{13755479859}<0.
$$

This is an exact count-only failure, not a floating-point example.

### 4.2 Why a Covering Certificate is Necessary

When directly performing a natural interval extension on the root box

$$
I_1\times I_2
$$

the lower endpoint of the Schur determinant enclosure is negative. This only indicates that the interval dependency overestimation is too wide; it does not imply the existence of a failure position.

The algorithm proceeds sequentially:

1. Reconstruct the interval $K_{XX}, K_{XY}, K_{YY}$ for each box;
2. Enclose the positive $2\times2$ system with an exact rational interval inverse;
3. Construct the interval Schur matrix;
4. If the Sylvester lower bounds are insufficient, bisect along the midpoint of the widest coordinate;
5. Repeat until all leaves pass or the stopping depth is reached.

In this example, we obtain:

$$
\text{certified leaves}=8,
\qquad
\text{maximum depth}=7,
$$

The determinant lower bound of the smallest leaf box is

$$
\frac{
996149099768633906407318481
}{
92259342242007809509970517515625
}
>
1.0797\times10^{-5}.
$$

Therefore, the universal family holds under the synthetic occupancy premise.

## 5. Micro-Radius Lifting of the v0.7 Clamped Green Parent Certificate

v0.7 has proven the abstract operator for fixed atom positions:

$$
W_{21/20}(\mathbf c)\succeq0.
$$

Both the positive and negative parts of the core depend linearly on $\alpha$, and the positive axis part is denoted as $A(\mathbf c)\succeq0$. Therefore,

$$
W_1(\mathbf c)
=
\frac{20}{21}W_{21/20}(\mathbf c)
+
\frac1{21}\left(I+A(\mathbf c)\right)
\succeq
\frac1{21}I.
$$

This step derives an exact coercivity margin from the parent positivity that does not depend on the unknown eigenvalues of the parent.

### 5.1 Green–Poincaré Perturbation Bound

In the clamped $H_0^2$ space on $[-R,R]$, the energy is

$$
\tau\int_{-R}^{R}|u''(t)|^2\,dt.
$$

Let $L=2R$. Applying the Dirichlet Poincaré inequality twice consecutively yields

$$
\|G\|_{L^2\to L^2}
\le
\frac{L^4}{\pi^4\tau}
<
\frac{L^4}{3^4\tau}
=:
C_G.
$$

The structural condition projection is a Hilbert orthogonal projection and does not increase the representer norm.

The axis density is

$$
f_x(t)=\cos(xt),
\qquad
\partial_xf_x(t)=-t\sin(xt).
$$

Thus,

$$
\|f_x\|_2\le\sqrt{2R},
\qquad
\|\partial_xf_x\|_2
\le
\sqrt{\frac{2R^3}{3}}.
$$

If $p_x$ is the projected Green representer, then

$$
\|p_x-p_c\|
\le
|x-c|
\sup_\xi\|\partial_\xi p_\xi\|.
$$

Furthermore,

$$
\|P_x-P_c\|
\le
\|p_x-p_c\|
\left(\|p_x\|+\|p_c\|\right).
$$

Using

$$
\sqrt3>\frac53
$$

we obtain the exact rational upper bound

$$
\|P_x-P_c\|
<
\frac{12}{5}R^2C_G|x-c|.
$$

If the operator weight of the $i$-th axis atom is $\lambda_i$, we have

$$
\left\|
\sum_i\lambda_i
\left(P_{x_i}-P_{c_i}\right)
\right\|
\le
\frac{12}{5}R^2C_G
\sum_i\lambda_i|x_i-c_i|.
$$

As long as the right-hand side is less than $1/21$, all independent positions jointly preserve positivity.

### 5.2 Exact Radius in This Round

The exact sum of the $58$ axis weights from v0.7 is

$$
\Lambda
=
\frac{10287970888727}{125000000000}.
$$

Taking a uniform cell half-width

$$
h=
\frac{1}{500000000000000},
$$

the perturbation norm upper bound for this round is

$$
\varepsilon
=
\frac{
12328822128706060288
}{
299401138693037109375
}
\approx0.0411782740
<
\frac1{21}.
$$

Therefore,

$$
W_1(\mathbf x)
\succeq
\left(\frac1{21}-\varepsilon\right)I
$$

and the exact coercivity lower bound is

$$
\frac{
13498624663403281109
}{
2095807970851259765625
}
\approx0.00644077361.
$$

This is an abstract clamped-Green family certificate that holds jointly for $58$ independent position quantifiers, but its centers and weights still come from the dual atoms of v0.7; it is not the actual $\zeta$ zero occupancy.

## 6. Floating-Point Adversarial Corners and Proof-Budget Gap

Using a direct Green reconstruction with $\Delta t=0.02$, we perform the following on the $58$ cell corners:

1. Central finite difference gradient;
2. Gradient sign corner;
3. Up to four rounds of deterministic coordinate flips.

The resulting threshold at

$$
h=0.016
$$

is approximately

$$
1.00046047,
$$

while at

$$
h=0.017
$$

it is approximately

$$
0.98805163.
$$

Fixing the corners and recalculating with

$$
\Delta t\in\{0.02,0.01,0.005\}
$$

yields a difference of less than $2\times10^{-5}$.

This is merely an adversarial diagnostic; it does not exhaust the $2^{58}$ corners, let alone cover the cell interiors. It cannot replace an interval proof. However,

$$
\frac{0.016}{2\times10^{-15}}
=
8\times10^{12}
$$

shows that the current primary loss comes from the global Poincaré bound, rather than implying that the proven operator family inevitably fails in macroscopic cells.

## 7. Closed and Unclosed Items in This Round

Closed:

- Valid operator transfer for occupancy selection;
- Exact counterexample for scalar count-only;
- Exact rational Green cover engine;
- Synthetic two-cell universal family;
- Conditional $58$-cell clamped micro-radius family.

Unclosed:

- Theorem-backed cell presence certificates for $\zeta$ zeros;
- Local interval clamped-Green derivatives;
- Universal Schur family for macroscopic cells;
- Explicit-formula admissibility and prime-side nonnegative cone;
- Full critical strip and global RH transfer.