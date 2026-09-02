# Equivariant Arithmetic Separation
## From Orbit-Space Localization to Admissible Test Functions in the Explicit Formula for the Riemann Zeta Function

**英文題名：** *Equivariant Arithmetic Separation: From Orbit-Space Localization to Admissible Test Functions in the Explicit Formula for the Riemann Zeta Function*  
**作者：** Neo.K (Chuan-Wei Hsu)  
**機構：** EveMissLab / A Word Promise Technology Co., Ltd.  
**版本：** v0.1 (Internal Research Draft)  
**日期：** 2026-07-24  
**性質：** Riemann Hypothesis Research / Explicit Formula / Weil-type Quadratic Form / Equivariant Topology / Test Functions / Localization  
**前置文件：**
1. *From Centering to Equivariant Topology: Methodologies and Method Groups for the Legitimate Decidability of RH*  
2. *Topology of Equivariant Zero Configurations: RH Orbit-Type Stratification, Effective Divisor Semirings, and Positive Obstructions*  
3. *Stratified Zero Obstructions and Local-Global Lifting: From Rational Rectangular Certificates to Full Critical Strip Decidability*  
**狀態：** Internal draft; does not constitute a proof of the Riemann Hypothesis

---

## Important Declaration

This document is not a proof of the Riemann Hypothesis.

This document enters for the first time an interface that may contain substantive proof content, but it only establishes the problem, function classes, quadratic forms, localization specifications, and conditional derivations. This document does not prove that the required local negative witnesses necessarily exist, nor does it prove that the prime side of the explicit formula possesses sufficient unconditional non-negativity for all test functions in this document.

This document uses the Weil-type explicit formula and positivity criterion as known background. The important warning is:

> If one directly proves that the entire Weil-type quadratic form is non-negative for all admissible test functions, it is usually already equivalent to or sufficient to deduce RH.

Therefore, this document cannot treat "proving positivity" as an obviously weaker new intermediate step. What this document truly investigates is a more refined question:

> **If off-axis zeros exist, can we start from their local orbit positions to construct a local negative witness that can enter the explicit formula, suppress the contribution of that orbit, control the leakage from other zeros, and preserve the computability of the prime side?**

Only if such negative witnesses can be constructed for any off-axis orbit, and the arithmetic side can independently exclude negative values, could a non-circular proof of RH be formed.

---

# Abstract

Let
\[
F(z)=\xi\left(\frac12+z\right),
\qquad
z=\beta+i\gamma,
\]
where RH is equivalent to all zeros satisfying \(\beta=0\). Previous research has represented off-axis zeros as positive divisor obstructions in the right half of the critical strip, establishing countable local certificates via rational rectangular winding numbers.

This document further introduces the spectral coordinates naturally used by the explicit formula:
\[
w=-iz=\gamma-i\beta.
\]
The critical axis \(\beta=0\) is mapped to the real axis \(w\in\mathbb R\), while off-axis zeros are mapped to non-real points in the horizontal strip
\[
\mathcal S_{1/2}
=
\left\{
w\in\mathbb C:
|\operatorname{Im}w|<\frac12
\right\}.
\]
The Klein four-group orbit in these coordinates becomes
\[
\{w,-w,\overline w,-\overline w\}.
\]

Topologically, any compact off-axis orbit set separated from the real axis can be localized by continuous functions. However, the \(\zeta\) explicit formula cannot use arbitrary two-dimensional continuous functions; it only accepts entire functions obtained via Fourier/Mellin transforms of one-dimensional additive or multiplicative test functions. This forms the core lifting gap of this document:
\[
\boxed{
\text{Topologically separable}
\;\dashrightarrow\;
\text{Arithmetically admissibly separable}.
}
\]

Taking a test function \(g\) in the convolution algebra as the basic input, this document defines
\[
g^\ast(x)=\overline{g(-x)},
\qquad
f_g=g*g^\ast.
\]
If \(G=\widehat g\), then
\[
\widehat{f_g}(w)
=
G(w)\overline{G(\overline w)}.
\]
On the real axis,
\[
\widehat{f_g}(t)=|G(t)|^2\ge0,
\]
while on non-real points, this quantity is no longer a modulus squared. The block contribution after merging with conjugate orbits is
\[
B_w(g)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]
which can take a negative sign. This difference precisely describes: zeros on the critical line naturally yield positive squares, whereas off-axis orbits introduce sign indefiniteness into the Weil-type quadratic form.

This document defines "Equivariant Local Arithmetic Separability": for every compact off-axis orbit set \(K\), control window \(C\), and admissible leakage \(\varepsilon\), there exists an admissible test function \(g\) such that the target orbit block has a quantitative negative value, while the real axis, non-target zeros, Gamma terms, prime terms, and tail contributions are all verifiably controlled. This is not simply requiring the existence of some negative quadratic form, but requiring the witness to possess:

1. Orbit symmetry;
2. Spatial or frequency support specifications;
3. Target localization;
4. Leakage upper bounds;
5. Explicit formula admissibility;
6. Prime side computability;
7. ZFC formalizable certificates.

This document proves a conditional architectural theorem: if the aforementioned local negative witnesses can be generated for any off-axis zero, and the arithmetic side of the explicit formula possesses an independent non-negative lower bound for the same class of test functions, then RH holds. This theorem itself is a logical architecture; the truly unfinished parts are the witness construction and the arithmetic lower bound.

This document also proposes a stratified research plan for finite window interpolation, entire function approximation, Paley–Wiener support costs, non-target orbit leakage, and tail control, explicitly clarifying: arbitrary two-dimensional Urysohn separation functions cannot be directly treated as explicit formula test functions; there is an uncertainty cost between perfect localization and finite Fourier support; and any overly strong global positivity proposition may have already smuggled RH into its assumptions.

**Keywords:** Riemann Hypothesis, Explicit Formula, Weil Positivity, Equivariant Separation, Test Functions, Paley–Wiener, Orbit Space, Convolution Square, Local Negative Witness, Arithmetic Lifting

---

# 1. From Local Zero Certificates to Arithmetic Witnesses

## 1.1 Prerequisite Results

The previous document established:

\[
\mathrm{RH}
\iff
\omega_R(F)=0
\]

holds for all regular rational rectangles \(R\) in the right half of the critical strip.

If RH fails, there exists a rectangle \(R\Subset X^+\) such that:

\[
\omega_R(F)>0.
\]

This is a local positive certificate for the existence of off-axis zeros.

## 1.2 The New Problem

The winding number certificate tells us:

\[
R\text{ contains off-axis zeros}.
\]

But it does not tell us how to derive a contradiction from prime data.

Therefore, we need to establish:

\[
\boxed{
\text{Local off-axis certificate}
\longrightarrow
\text{Sign witness in the explicit formula}.
}
\]

## 1.3 Why We Cannot Directly Use Rectangle Indicator Functions

The rectangle indicator function is a two-dimensional function:

\[
\mathbf 1_R(\beta,\gamma).
\]

However, the traditional explicit formula for \(\zeta\) typically uses one-dimensional test functions \(g(x)\), or their Fourier/Mellin transforms \(G(w)\).

Thus:

\[
\mathbf 1_R
\]

cannot be directly substituted into the explicit formula.

This is not a minor technical issue, but a mismatch in domains:

\[
C_c(X^+)
\not\subset
\mathcal H_{\mathrm{explicit}}.
\]

---

# 2. Spectral Coordinates and Equivariant Orbits

## 2.1 Coordinate Transformation

For centered zeros:

\[
z=\beta+i\gamma,
\]

define:

\[
w=-iz=\gamma-i\beta.
\]

The inverse transformation is:

\[
z=iw.
\]

## 2.2 The Critical Line

If:

\[
\beta=0,
\]

then:

\[
w=\gamma\in\mathbb R.
\]

So RH is equivalent to all spectral points \(w_\rho\) being real numbers.

## 2.3 The Critical Strip

Since:

\[
|\beta|<\frac12,
\]

we have:

\[
|\operatorname{Im}w|<\frac12.
\]

Define the spectral strip:

\[
\mathcal S
=
\left\{
w\in\mathbb C:
|\operatorname{Im}w|<\frac12
\right\}.
\]

## 2.4 Transformation of Group Actions

In \(z\)-coordinates:

\[
a(z)=-z,
\qquad
b(z)=\overline z,
\qquad
j(z)=-\overline z.
\]

In \(w=-iz\) coordinates:

\[
a_w(w)=-w,
\]

\[
b_w(w)=-\overline w,
\]

\[
j_w(w)=\overline w.
\]

Thus, the critical reflection becomes standard complex conjugation, and its fixed set is:

\[
\operatorname{Fix}(j_w)=\mathbb R.
\]

A general off-axis orbit is:

\[
\mathcal O(w)
=
\{w,-w,\overline w,-\overline w\}.
\]

## 2.5 Orbit Space

Let:

\[
Y=\mathcal S/G.
\]

Real axis orbits form:

\[
Y_{\mathrm{axis}},
\]

and non-real orbits form:

\[
Y_{\mathrm{off}}.
\]

RH is equivalent to the descended measure of spectral divisors being completely supported on \(Y_{\mathrm{axis}}\).

---

# 3. Topological Separation

## 3.1 Compact Off-Axis Orbit Sets

Let:

\[
K\subset Y_{\mathrm{off}}
\]

be a compact set.

Its preimage:

\[
\widetilde K\subset\mathcal S
\]

is a \(G\)-invariant compact set separated from the real axis.

Therefore, there exists:

\[
d(K,\mathbb R)>0.
\]

## 3.2 Continuous Separation

In a normal topological space, one can find a continuous \(G\)-invariant function:

\[
u_K:\mathcal S\to[0,1]
\]

such that:

\[
u_K|_{\widetilde K}=1,
\]

and in some neighborhood of the real axis:

\[
u_K=0.
\]

## 3.3 Significance of Topological Separation

If the off-axis zero measure \(\nu_F\) has positive mass on \(K\), then:

\[
\int u_K\,d\nu_F>0.
\]

So topologically, off-axis mass can be localized.

## 3.4 Inadequacies of Topological Separation

\(u_K\) typically:

- Is not a holomorphic function;
- Is not a one-dimensional Fourier transform;
- Lacks the required decay;
- Lacks the analytic continuation permitted by the explicit formula;
- Cannot be naturally converted into prime sums.

Therefore, topological separation only establishes target specifications, not arithmetic witnesses.

---

# 4. Admissible Test Function Classes

## 4.1 Basic Test Algebra

Let:

\[
\mathcal G
\]

be a complex-valued test function algebra to be precisely selected, such as:

- \(C_c^\infty(\mathbb R)\);
- A certain Schwartz subspace;
- Smooth compactly supported functions with specified exponential weights;
- Other nuclear spaces permitted by explicit formula theorems.

Different normalizations will alter the details, but this document requires \(\mathcal G\) to at least satisfy:

1. Closed under convolution;
2. Closed under involution;
3. Fourier or Mellin transforms can be analytically continued to a region containing \(\mathcal S\);
4. Zero sums, prime sums, and Gamma terms are well-defined;
5. The explicit formula can be applied;
6. Finite linear combinations and approximations can be performed.

## 4.2 Involution

Define:

\[
g^\ast(x)
=
\overline{g(-x)}.
\]

Convolution square:

\[
f_g
=
g*g^\ast.
\]

## 4.3 Fourier Transform

Adopting a fixed convention:

\[
G(w)
=
\widehat g(w)
=
\int_{\mathbb R}
g(x)e^{iwx}\,dx.
\]

Then:

\[
\widehat{g^\ast}(w)
=
\overline{G(\overline w)}.
\]

Thus:

\[
\widehat{f_g}(w)
=
G(w)\overline{G(\overline w)}.
\]

## 4.4 Positivity on the Critical Line

If:

\[
w=t\in\mathbb R,
\]

then:

\[
\widehat{f_g}(t)
=
|G(t)|^2
\ge0.
\]

This is the fundamental algebraic reason why the Weil-type quadratic form exhibits positivity under RH.

## 4.5 Sign Indefiniteness Off-Axis

If:

\[
w\notin\mathbb R,
\]

then:

\[
G(w)\overline{G(\overline w)}
\]

need not be real, nor non-negative.

Pairing conjugate orbits yields a real block:

\[
B_w(g)
=
G(w)\overline{G(\overline w)}
+
G(\overline w)\overline{G(w)}
\]

\[
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right).
\]

This quantity can be positive, zero, or negative.

---

# 5. Equivariant Symmetrization

## 5.1 Why Symmetry is Needed

Zeros appear in orbits as:

\[
\{w,-w,\overline w,-\overline w\}.
\]

If the test function does not respect this symmetry, it may:

- Generate unnecessary complex values;
- Double-count the same orbit;
- Conflate sign issues with coordinate choices.

## 5.2 Taking the Even Part

For \(g\in\mathcal G\), define:

\[
g_{\mathrm{ev}}(x)
=
\frac12(g(x)+g(-x)).
\]

If \(\mathcal G\) is closed, then:

\[
g_{\mathrm{ev}}\in\mathcal G.
\]

Its Fourier transform satisfies:

\[
G_{\mathrm{ev}}(-w)=G_{\mathrm{ev}}(w).
\]

## 5.3 Real Structure

We can further take:

\[
g_{\mathbb R}(x)
=
\frac12
\left(
g_{\mathrm{ev}}(x)
+
\overline{g_{\mathrm{ev}}(x)}
\right).
\]

Making \(g_{\mathbb R}\) a real even function, and we have:

\[
G(-w)=G(w),
\]

\[
G(\overline w)=\overline{G(w)}.
\]

## 5.4 Note

If \(G(\overline w)=\overline{G(w)}\), then:

\[
G(w)\overline{G(\overline w)}
=
G(w)^2.
\]

The conjugate block becomes:

\[
B_w(g)=2\operatorname{Re}(G(w)^2).
\]

This can still be negative.

For example, if:

\[
G(w)\approx i\alpha,
\]

then:

\[
\operatorname{Re}(G(w)^2)\approx-\alpha^2.
\]

Therefore, the goal of a local negative witness can be understood as:

> At the target off-axis point, make the phase of \(G(w)\) close to purely imaginary, while controlling other spectral points and arithmetic side costs.

---

# 6. Weil-Type Quadratic Form

## 6.1 Abstract Explicit Formula

For an appropriate test function \(f\), the \(\zeta\) explicit formula can be abstractly written as:

\[
\mathcal Z_\zeta(f)
=
\mathcal A_\infty(f)
+
\mathcal P_\zeta(f)
+
\mathcal N(f),
\]

where:

- \(\mathcal Z_\zeta\): Non-trivial zero side;
- \(\mathcal A_\infty\): Gamma factors and infinite places;
- \(\mathcal P_\zeta\): Prime and prime power side;
- \(\mathcal N\): Normalization, pole, or endpoint terms.

Exact constants, signs, and Fourier conventions need to be fixed in the formalized version.

## 6.2 Quadratic Form

For:

\[
f_g=g*g^\ast,
\]

define the Weil-type quadratic form:

\[
Q_\zeta(g)
=
\mathcal W_\zeta(f_g),
\]

where \(\mathcal W_\zeta\) is the explicit formula functional adopting a fixed normalization.

The zero side has the form:

\[
Q_\zeta^{\mathrm{zero}}(g)
=
\sum_{\rho}
G(w_\rho)
\overline{G(\overline{w_\rho})},
\]

summed in a symmetric or regularized manner.

## 6.3 The Zero Side Under RH

If RH holds, all:

\[
w_\rho\in\mathbb R.
\]

Therefore:

\[
Q_\zeta^{\mathrm{zero}}(g)
=
\sum_\rho
|G(w_\rho)|^2
\ge0.
\]

## 6.4 Off-Axis Block

If a non-real orbit \(\mathcal O(w)\) exists, its merged contribution has the form:

\[
m_w B_w(g),
\]

where:

\[
B_w(g)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]

and corresponding multiples are added according to \(\pm w\) symmetry and normalization.

This block can be negative.

## 6.5 The Status of Known Positivity Criteria

Under appropriate test function spaces and normalizations, the non-negativity of the Weil-type quadratic form for all test functions is one of the known equivalent or necessary and sufficient forms of RH.

Therefore, this document does not treat:

\[
Q_\zeta(g)\ge0
\qquad
\forall g
\]

as a new goal with reduced difficulty.

Instead, this document investigates:

\[
\text{Local off-axis data}
\Longrightarrow
\text{Localizable }g\text{ and negative block}.
\]

---

# 7. Local Orbit Negative Witness

## 7.1 Target Orbit

Let:

\[
w_0=\gamma_0-i\beta_0,
\qquad
\beta_0\ne0.
\]

Its orbit is:

\[
\mathcal O_0
=
\{w_0,-w_0,\overline{w_0},-\overline{w_0}\}.
\]

## 7.2 Ideal Local Conditions

We wish to construct \(g\in\mathcal G\) such that:

\[
B_{w_0}(g)\le-c
\]

for some \(c>0\).

Simultaneously, for other zero orbits \(w\) in the control region:

\[
|B_w(g)|\le\varepsilon.
\]

And control:

\[
|\mathcal A_\infty(f_g)|,
\qquad
|\mathcal P_\zeta(f_g)|,
\qquad
|\mathcal N(f_g)|.
\]

## 7.3 Cannot Demand Absolute Zero Leakage

If \(G\) is an entire function, requiring it to be completely zero on a non-target set with accumulation points usually forces:

\[
G\equiv0.
\]

Therefore, the legitimate goal is not:

\[
G=0
\quad
\text{at all non-target positions},
\]

but a quantitative approximation:

\[
\sum_{\text{non-target}}
|B_w(g)|
\le
\varepsilon.
\]

## 7.4 Witness Definition

We call \(g\) a

\[
(c,\varepsilon,C)
\text{-local negative witness}
\]

for the target orbit \(\mathcal O_0\), if:

1. \(g\in\mathcal G\);
2. \(g\) satisfies the specified symmetries;
3. The target block
   \[
   B_{w_0}(g)\le-c;
   \]
4. The total leakage from non-target zeros in the control window \(C\) is at most \(\varepsilon\);
5. The tail outside the window has an explicit upper bound;
6. Each term of the explicit formula converges absolutely or symmetrically;
7. The prime side can be computed from finite data plus tail bounds;
8. The total error is less than a specified proportion of \(c\).

## 7.5 Certificate Form

\[
\mathsf{Witness}
=
\left(
g,
G,
\mathcal O_0,
c,
\varepsilon,
C,
E_{\mathrm{tail}},
E_{\mathrm{prime}},
E_{\infty}
\right).
\]

If one can verify:

\[
c
>
\varepsilon
+
E_{\mathrm{tail}}
+
E_{\mathrm{prime}}
+
E_{\infty},
\]

then the sign of the total quadratic form is dominated by the target negative block.

---

# 8. Finite Window Interpolation

## 8.1 Finite Spectral Set

Let:

\[
\Sigma
=
\{w_1,\ldots,w_N\}
\subset\mathcal S
\]

be a finite set closed under \(\pm\) and conjugation.

## 8.2 Pure Entire Function Interpolation

For finite target values conforming to symmetry:

\[
v_k,
\]

one can use polynomial or entire function interpolation to construct \(G\) such that:

\[
G(w_k)=v_k.
\]

Then, by averaging, ensure:

\[
G(-w)=G(w),
\]

\[
G(\overline w)=\overline{G(w)}.
\]

## 8.3 Local Phase Configuration

One can specify for the target off-axis point:

\[
G(w_0)=i,
\]

\[
G(\overline{w_0})=-i,
\]

so that:

\[
B_{w_0}(g)
=
2\operatorname{Re}(i^2)
=
-2.
\]

And specify small values for the finite non-target set.

## 8.4 This Result is Still Insufficient

An arbitrary interpolating entire function is not necessarily the Fourier transform of some:

\[
g\in\mathcal G.
\]

It might:

- Grow too fast;
- Not decay on the real axis;
- Cause the prime sum to diverge;
- Not be of finite exponential type;
- Not conform to explicit formula assumptions.

Therefore:

\[
\text{Finite entire function interpolation}
\not\Rightarrow
\text{Arithmetically admissible witness}.
\]

---

# 9. Paley–Wiener Lifting Problem

## 9.1 Finite Support and Exponential Type

If:

\[
g\in C_c^\infty([-L,L]),
\]

then its Fourier transform \(G\) is an entire function of exponential type controlled by \(L\).

Conversely, appropriate exponential type and real-axis decay conditions correspond to compactly supported test functions.

## 9.2 Localization Cost

To make \(G\) highly localized in spectral space, it usually requires expanding the support of \(g\).

This is a manifestation of Fourier uncertainty:

\[
\text{Increased spectral localization}
\Longrightarrow
\text{Expanded support in arithmetic variables}.
\]

In the explicit formula, this means more prime and prime power data are required.

## 9.3 Arithmetic Cost

If the support of \(g\) is restricted to:

\[
[-L,L],
\]

the prime side typically only involves:

\[
\log n\le L
\]

or a corresponding finite range.

Thus, \(L\) simultaneously controls:

- Spectral resolution;
- Required prime range;
- Computational certificate size;
- Tail error.

## 9.4 Core Optimization Problem

Given:

\[
w_0,\quad c,\quad\varepsilon,
\]

find the minimum support radius:

\[
L_{\min}(w_0;c,\varepsilon)
\]

such that there exists:

\[
g\in C_c^\infty([-L,L])
\]

satisfying the local negative witness conditions.

This is the quantitative "arithmetic separation cost" proposed by this document.

---

# 10. Equivariant Local Arithmetic Separability

## 10.1 Definition

The explicit formula test system of \(\zeta\) is said to possess **Equivariant Local Arithmetic Separability** if, for every:

- Compact off-axis orbit set \(K\subset Y_{\mathrm{off}}\);
- Compact control window \(C\supset K\);
- Admissible error \(\varepsilon>0\);

as long as the zero divisor has positive mass on \(K\), there exists:

\[
g\in\mathcal G
\]

such that:

1. The total contribution of the target orbit is at most \(-c_K<0\);
2. The total leakage from zeros in \(C\setminus K\) is less than \(\varepsilon\);
3. The tail of zeros outside \(C\) is less than \(\varepsilon\);
4. Archimedean and normalization errors can be explicitly computed;
5. The prime side depends only on finite-range data and provable tail bounds;
6. The total error is less than \(c_K\).

## 10.2 Strong Version

The strong version requires that:

\[
c_K
\]

can be given an explicit lower bound by:

- The distance from \(K\) to the real axis;
- The minimum multiplicity in \(K\);
- The size of the control window;
- The support of the test function.

## 10.3 Weak Version

The weak version only requires the existence of some negative witness, without requiring effective estimates.

The weak version is close to the contrapositive of known global positivity criteria; the strong version requires localizable, constructible, and computable certificates.

## 10.4 Claims of This Document

This document does not claim to have proven either the strong or weak version.

This document asserts that they are among the most precise lifting problems between the topological framework and the explicit formula.

---

# 11. Arithmetic Non-negativity Interface

## 11.1 Arithmetic Side Functional

The explicit formula writes the quadratic form as:

\[
Q_\zeta(g)
=
Q_{\mathrm{prime}}(g)
+
Q_{\infty}(g)
+
Q_{\mathrm{norm}}(g).
\]

Specific signs vary depending on normalization.

## 11.2 Required Proposition

To derive a contradiction from a local negative witness, one needs to independently prove:

\[
Q_\zeta(g)\ge0
\]

holds at least for all \(g\) generated by the separation construction.

## 11.3 Why We Cannot Directly Assume Non-negativity for the Whole Class

If we assume:

\[
Q_\zeta(g)\ge0
\qquad
\forall g\in\mathcal G,
\]

in the standard Weil-type setting, this may already be equivalent to RH.

Therefore, legitimate research should seek:

- A smaller subclass naturally generated by arithmetic structures;
- A structural cone that can be directly proven non-negative;
- Or a local estimate distinct from full Weil positivity.

## 11.4 Intersection of the Separation Class and Positivity Class

Let:

\[
\mathcal G_{\mathrm{sep}}
\]

be the class of test functions capable of generating local negative witnesses.

Let:

\[
\mathcal G_{\mathrm{arith}+}
\]

be the class of test functions for which the prime side can independently prove:

\[
Q_\zeta(g)\ge0.
\]

What is truly needed is:

\[
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\ne\varnothing
\]

holding for every hypothetical off-axis orbit.

This intersection problem is more precise than vaguely "proving Weil positivity".

---

# 12. Conditional Exclusion Theorem

## 12.1 Theorem Architecture

### Theorem 12.1 (Conditional)

Assume:

1. The zero divisor of \(F\) possesses the known \(G\)-symmetry;
2. Any compact off-axis orbit set satisfies strong equivariant local arithmetic separability;
3. Every test function \(g\) generated by this separation procedure satisfies the unconditional arithmetic lower bound:
   \[
   Q_\zeta(g)\ge0;
   \]
4. The explicit formula, all summations, limits, and error bounds are legitimate.

Then RH holds.

## 12.2 Proof

Assume for contradiction that RH does not hold.

Then there exist off-axis zero orbits. Take a compact set \(K\) containing only finitely many off-axis orbits and separated from the real axis.

By Condition 2, there exists a local negative witness \(g\) whose target negative contribution strictly exceeds all non-target and error contributions, thus:

\[
Q_\zeta(g)<0.
\]

But by Condition 3:

\[
Q_\zeta(g)\ge0.
\]

Contradiction.

Therefore, no off-axis zeros exist, and RH holds. Q.E.D.

## 12.3 Status of the Theorem

This theorem is merely a logical decomposition.

Condition 2 and Condition 3 are both major unsolved contents.

The conditional theorem itself cannot be claimed as progress on RH unless at least one of its non-trivial conditions is independently proven.

---

# 13. Stratified Workflow from Local Certificates to Negative Witnesses

## 13.1 Step One: Rectangular Certificate

Find:

\[
R\Subset X^+
\]

such that:

\[
\omega_R(F)>0.
\]

In a proof by contradiction, this is obtained by assuming the existence of off-axis zeros.

## 13.2 Step Two: Orbit Saturation

Saturate \(R\) under \(G\) to obtain the target compact set in spectral coordinates:

\[
K_R
=
G\cdot(-iR).
\]

## 13.3 Step Three: Topological Separation

Construct:

\[
u_R
\]

which is large on \(K_R\) and zero in a neighborhood of the real axis.

## 13.4 Step Four: Analytic Approximation

Find an entire function or Paley–Wiener function \(G_R\) such that the orbit block it generates approximates the required sign shape.

Note that this is not approximating \(u_R\) itself, but approximating a sign kernel expressible by:

\[
2\operatorname{Re}
\left(
G_R(w)\overline{G_R(\overline w)}
\right).
\]

## 13.5 Step Five: Inverse Fourier Lifting

Prove that:

\[
G_R=\widehat{g_R}
\]

for some:

\[
g_R\in\mathcal G.
\]

## 13.6 Step Six: Error Decomposition

Decompose the total quadratic form into:

\[
Q_\zeta(g_R)
=
Q_K
+
Q_{C\setminus K}
+
Q_{\mathrm{tail}}
+
Q_{\mathrm{prime}}
+
Q_\infty
+
Q_{\mathrm{norm}}.
\]

## 13.7 Step Seven: Sign Domination

Prove that:

\[
Q_K
<
-
\left(
|Q_{C\setminus K}|
+
|Q_{\mathrm{tail}}|
+
|Q_{\mathrm{prime}}|
+
|Q_\infty|
+
|Q_{\mathrm{norm}}|
\right).
\]

Then:

\[
Q_\zeta(g_R)<0.
\]

---

# 14. Major Analytical Obstacles

## 14.1 Holomorphic Rigidity

An arbitrary continuous two-dimensional separation function cannot be arbitrarily precisely and globally replicated by a holomorphic function.

## 14.2 Maximum Modulus and Unique Continuation

Requiring an entire function to completely vanish on an overly large set may force it to be identically zero.

## 14.3 Uncertainty Principle

High resolution in spectral space requires large support in arithmetic variables.

## 14.4 Unknownness of Zeros

The positions of non-target zeros are unknown; one cannot assume mastery of all zeros when constructing a witness.

## 14.5 On-Axis Zero Leakage

The number of on-axis zeros is infinite. Even if each single point's contribution is small, the total sum may still be non-negligible.

## 14.6 Gamma Terms

Archimedean terms may have contributions of the same order as the target negative value.

## 14.7 Prime Side Signs

Prime sums are generally not automatically non-negative term-by-term; they must be re-analyzed based on the test function structure.

## 14.8 Tail Regularization

The zero side often requires symmetric summation or regularization; local decomposition must be compatible with the summation order.

---

# 15. Cones Rather Than Linear Spaces

## 15.1 Why Use Positive Cones

To prove non-negativity, test functions should not be viewed merely as a linear space, but one should consider the convolution square cone:

\[
\mathcal C
=
\left\{
g*g^\ast:
g\in\mathcal G
\right\}.
\]

## 15.2 Critical Line Positive Cone

Under RH, the zero side for this cone is:

\[
\sum_\rho|G(w_\rho)|^2.
\]

## 15.3 Off-Axis Disruption

Off-axis orbits turn the zero side on the same cone into an indefinite quadratic form.

Therefore, RH can be understood as:

> The zero evaluation functional of \(\zeta\) maintains positivity on the convolution square cone.

This is the equivariant configuration interpretation of the known Weil-type perspective.

## 15.4 The New Decomposition of This Document

This document splits the global positive cone problem into:

\[
\text{Construction of local negative directions}
+
\text{Independent identification of the arithmetic positive cone}.
\]

---

# 16. Finite-Dimensional Matrix Prototype

## 16.1 Basis Test Functions

Select:

\[
g_1,\ldots,g_N\in\mathcal G.
\]

Let:

\[
g=\sum_{k=1}^Nc_kg_k.
\]

Then:

\[
Q_\zeta(g)
=
c^\ast M c
\]

for some Hermitian matrix \(M\).

## 16.2 Zero Orbit Matrices

The target off-axis orbit gives a matrix:

\[
M_K.
\]

Other contributions give:

\[
M_{\mathrm{rest}},
\quad
M_{\mathrm{prime}},
\quad
M_\infty.
\]

Total matrix:

\[
M
=
M_K
+
M_{\mathrm{rest}}
+
M_{\mathrm{prime}}
+
M_\infty.
\]

## 16.3 Finite-Dimensional Negative Witness

If there exists a vector \(c\) such that:

\[
c^\ast M_Kc<0
\]

and the negative value exceeds the operator norm upper bounds of the other matrices, a finite-dimensional negative certificate is obtained.

## 16.4 Value

This prototype can:

- Numerically search for test functions;
- Estimate required support;
- Discover uncontrollable leakages;
- Generate formalizable candidate certificates;
- Without directly claiming to prove RH.

## 16.5 Risks

Failing to find a negative direction in a finite-dimensional space does not mean it does not exist in infinite dimensions.

Finding a numerical negative direction also requires completing a precise error proof.

---

# 17. Formalized Separation Cost

## 17.1 Cost Vector

Define the witness cost:

\[
\mathfrak C(g)
=
\left(
L,
N_p,
P,
E_{\mathrm{tail}},
E_{\mathrm{axis}},
E_\infty,
E_{\mathrm{arith}}
\right),
\]

where:

- \(L\): Real variable support radius;
- \(N_p\): Upper limit of required prime data;
- \(P\): Numerical precision;
- \(E_{\mathrm{tail}}\): Zero tail error;
- \(E_{\mathrm{axis}}\): On-axis leakage;
- \(E_\infty\): Gamma term error;
- \(E_{\mathrm{arith}}\): Prime side tail bound.

## 17.2 Distance to Axis

It is expected that as:

\[
|\beta_0|\downarrow0,
\]

the cost required to distinguish the off-axis point from the real axis increases.

That is:

\[
L_{\min}
\to\infty
\]

or error control deteriorates.

## 17.3 Height Cost

When:

\[
|\gamma_0|\to\infty,
\]

one needs to handle more neighboring zeros and a larger range of arithmetic data.

## 17.4 Separation Complexity

Define the conceptual complexity:

\[
\operatorname{SepCost}(w_0;c,\varepsilon)
=
\inf_g
\mathfrak C(g),
\]

where the infimum is interpreted according to some partial order or weighted cost function.

This quantity can become the primary observable for subsequent computational experiments.

---

# 18. Circularity Audit

## 18.1 Prohibited Assumptions

When constructing \(g\), one cannot assume:

- All other zeros are on the critical line;
- The target orbit is the only off-axis orbit;
- The unknown zero tail has bounds under RH;
- The Weil quadratic form is already non-negative for all test functions;
- Some positivity condition equivalent to RH already holds.

## 18.2 Permitted Data

One may use:

- Functional equation;
- Zero symmetry;
- Known zero counting asymptotics;
- Unconditional zero-free regions;
- Proven explicit formulas;
- Verified finite-height data;
- Unconditional Gamma and prime sum estimates;
- Analytic bounds of the test function itself.

## 18.3 Dependency Tagging

Every local negative witness must be tagged:

\[
\mathsf{Deps}(g)
=
\left(
\mathsf{Analytic},
\mathsf{Arithmetic},
\mathsf{Numerical},
\mathsf{Axiomatic}
\right).
\]

If any estimate uses RH or equivalent propositions, the witness can only serve as a conditional experiment.

---

# 19. Relationship with Known Positivity Criteria

## 19.1 No New Equivalence Claims

This document acknowledges that:

- Weil-type positivity;
- Non-negativity of Li-type coefficients;
- Certain Hilbert space or trace formula formulations;

already provide equivalent or closely related criteria for RH.

This document does not rename them as new proofs.

## 19.2 The Difference of This Document

This document is concerned with whether:

\[
\text{Failure of global positivity}
\]

can be decomposed into:

\[
\text{Some local off-axis orbit}
\longrightarrow
\text{A localized negative direction}.
\]

## 19.3 New Research Goal

Known equivalent criteria usually state:

\[
\mathrm{RH\ false}
\Longrightarrow
\exists g,\ Q_\zeta(g)<0.
\]

This document pursues a stronger constructive question:

\[
\mathrm{RH\ false}
+
\text{Specified off-axis orbit }K
\Longrightarrow
\exists g_K
\]

and \(g_K\)'s:

- Support;
- Phase;
- Error;
- Arithmetic cost;
- Target orbit attribution;

are all controllable.

This is a lifting from "existence of a negative direction" to "locating a negative certificate".

---

# 20. Computational Experiment Specifications

## 20.1 Purpose

Computational experiments do not attempt to prove RH, but are used to judge whether local arithmetic separation is practically feasible.

## 20.2 Artificial Off-Axis Configuration

First, establish a finite model with:

- Known on-axis spectral points;
- An artificial off-axis four-element orbit;
- Controllable multiplicity.

## 20.3 Test Basis

One may use:

- Compactly supported B-splines;
- Smooth bump functions;
- Hermite/Gaussian prototypes;
- Prolate spheroidal-type bases;
- Finite Fourier combinations.

If a basis does not belong to the final explicit formula class, it can only serve for exploration.

## 20.4 Optimization Objective

Minimize:

\[
B_{w_0}(g)
+
\lambda_1 E_{\mathrm{axis}}
+
\lambda_2 E_{\mathrm{rest}}
+
\lambda_3 E_{\mathrm{support}}.
\]

## 20.5 Output

Each experiment outputs:

- Target negative block;
- On-axis leakage;
- Other off-axis leakage;
- Support cost;
- Numerical condition number;
- Error sensitivity;
- Whether it can be converted into a precise certificate.

---

# 21. Formalization Plan

## 21.1 Spectral Coordinate Module

```text
CenteredZero
SpectralCoordinate
SpectralStrip
SpectralKleinAction
AxisOrbit
OffAxisOrbit
```

## 21.2 Test Function Algebra

```text
AdmissibleTestFunction
Convolution
StarInvolution
ConvolutionSquare
FourierTransformInStrip
```

Core theorem:

\[
\widehat{g*g^\ast}(w)
=
G(w)\overline{G(\overline w)}.
\]

## 21.3 Orbit Block

```text
OrbitBlock
AxisBlockNonnegative
OffAxisBlockReal
OffAxisBlockSignIndefinite
```

## 21.4 Explicit Formula Interface

One should not immediately reconstruct the entire \(\zeta\) explicit formula; an abstract interface can be defined first:

```text
ExplicitFormulaFunctional
ZeroSide
PrimeSide
ArchimedeanSide
NormalizationSide
ExplicitFormulaIdentity
```

## 21.5 Witness Module

```text
LocalizedNegativeWitness
TargetOrbitContribution
LeakageBound
TailBound
PrimeComputability
WitnessDominatesErrors
```

## 21.6 Conditional Theorem

```text
localized_separation_and_arithmetic_nonnegativity_implies_RH
```

This theorem must clearly retain all unproven assumptions and must not hide them as axioms.

---

# 22. Failure Conditions

If any of the following situations occur in this research route, it must be downgraded or rerouted:

1. Admissible test functions cannot localize a single off-axis orbit;
2. Any localization causes uncontrollable total on-axis leakage;
3. Paley–Wiener support cost is infinite;
4. The prime side has no usable signs or bounds for separation functions;
5. Gamma terms inevitably cancel out the target negative value;
6. The target orbit cannot be separated from other unknown off-axis orbits;
7. The required arithmetic non-negativity itself is equivalent to full RH;
8. Finite-dimensional negative directions cannot be lifted to legitimate infinite-dimensional functions;
9. Tail estimates cannot be completed unconditionally;
10. Formalization shows a core mapping type is invalid.

Even if this route fails, the configurations, positive obstructions, stratifications, and certificate frameworks established in the previous two documents remain valid.

---

# 23. What This Document Has Accomplished

This document has accomplished:

1. Transformed centered zeros into explicit formula spectral coordinates;
2. Represented off-axis four-element orbits as non-real spectral orbits;
3. Distinguished arbitrary topological test functions from arithmetically admissible test functions;
4. Established the sign difference of convolution squares on the real axis versus non-real points;
5. Defined off-axis orbit blocks;
6. Defined local negative witnesses;
7. Defined Equivariant Local Arithmetic Separability;
8. Established the conditional RH exclusion theorem;
9. Proposed Paley–Wiener separation costs;
10. Established finite-dimensional matrix prototypes;
11. Established circularity and formalization audit specifications.

---

# 24. What This Document Has Not Accomplished

This document has not proven:

\[
\forall K\subset Y_{\mathrm{off}},
\quad
\exists g_K\in\mathcal G
\]

satisfying the local negative witness conditions.

This document also has not proven:

\[
Q_\zeta(g)\ge0
\]

holds unconditionally for all \(g\) generated by the separation procedure.

Therefore, this document has not yet excluded any actual off-axis zeros, nor has it proven RH.

---

# 25. Next Stage

The next document is scheduled to be:

# *Positive Off-Axis Obstructions in the Explicit Formula*
## Local Negative Directions on the Zero Side, Computable Cones on the Prime Side, and ZFC-Auditable Contradiction Architectures

Its tasks include:

1. Fixing a precise Guinand–Weil type explicit formula normalization;
2. Fixing the test function space;
3. Expanding the zero orbit blocks;
4. Expanding the Gamma terms;
5. Expanding the prime and prime power terms;
6. Defining the cone of test functions provably non-negative from the prime side;
7. Investigating the intersection of this cone with the local separation class;
8. Establishing finite-dimensional and function space prototypes;
9. Determining whether this intersection problem is merely another equivalence of RH.

---

# 26. Conclusion

The previous two documents accomplished:

\[
\text{Off-axis zeros}
\longrightarrow
\text{Positive divisor obstructions}
\longrightarrow
\text{Local winding number certificates}.
\]

This document establishes the next arrow to be crossed:

\[
\boxed{
\text{Local off-axis certificates}
\;\dashrightarrow\;
\text{Local negative witnesses in the explicit formula}.
}
\]

Spectral coordinates:

\[
w=-iz
\]

transform the critical line into the real axis. Convolution square test functions satisfy:

\[
\widehat{g*g^\ast}(t)
=
|G(t)|^2
\ge0
\qquad
(t\in\mathbb R),
\]

while off-axis orbits generate:

\[
B_w(g)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]

whose sign is indefinite.

This reveals the local equivariant origin of Weil-type positivity:

> **On-axis zeros form moduli squared; off-axis zeros disrupt the modulus squared structure.**

But knowing that the sign can become negative is not equivalent to being able to construct a legitimate, local, computable negative witness sufficient to overpower all other terms.

Therefore, the core research proposition of this document is:

\[
\boxed{
\begin{aligned}
&\text{Given any off-axis zero orbit,}\\
&\text{does there exist an explicit formula-admissible convolution square test function,}\\
&\text{that produces a quantitative negative value for this orbit,}\\
&\text{while keeping on-axis zeros, other orbits, Gamma terms, prime terms, and tail errors controllable?}
\end{aligned}
}
\]

If the answer is no, topological localization cannot be lifted to arithmetic separation, and this route stops at the decidability framework.

If the answer is yes, a second independent result is still required:

\[
\boxed{
\text{The arithmetic side of the same test function class cannot produce negative values.}
}
\]

Only when both are accomplished simultaneously will a true contradiction be obtained:

\[
Q_\zeta(g)<0
\quad\text{ and }\quad
Q_\zeta(g)\ge0.
\]

Therefore, this round has not proven RH, but has compressed "how topology truly participates in an RH proof" into a concrete, falsifiable, computable, and formalizable intersection problem:

\[
\boxed{
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\stackrel{?}{\ne}
\varnothing
}
\]

whether it holds for every hypothetical off-axis orbit.

This is the first time this series has formally moved from equivalent restatements into a technical gap that may generate substantive proof content.

---

# Appendix A: Main Symbols

| Symbol | Meaning |
|---|---|
| \(z=\beta+i\gamma\) | Centered zero coordinates |
| \(w=-iz\) | Explicit formula spectral coordinates |
| \(\mathcal S\) | Horizontal spectral strip |
| \(Y=\mathcal S/G\) | Orbit space |
| \(K\) | Compact off-axis orbit set |
| \(\mathcal G\) | Admissible test function algebra |
| \(g^\ast\) | Involution \(\overline{g(-x)}\) |
| \(f_g\) | Convolution square \(g*g^\ast\) |
| \(G\) | \(\widehat g\) |
| \(B_w(g)\) | Off-axis orbit block |
| \(Q_\zeta(g)\) | Weil-type quadratic form |
| \(\mathcal G_{\mathrm{sep}}\) | Class of locally separable test functions |
| \(\mathcal G_{\mathrm{arith}+}\) | Class of functions provably non-negative on the arithmetic side |
| \(\operatorname{SepCost}\) | Local arithmetic separation cost |

---

# Appendix B: Logical Status Table

| Proposition | Status |
|---|---|
| The critical line is the real axis in \(w\)-coordinates | Direct transformation |
| Convolution square is modulus squared on the real axis | Fourier algebraic identity |
| Off-axis blocks can be sign-indefinite | Algebraic fact |
| Topologically, compact off-axis sets can be separated from the real axis | General topological fact |
| Arbitrary topological separation can be lifted to admissible test functions | Unproven |
| Local negative witnesses exist for arbitrary off-axis orbits | Unproven |
| The arithmetic side is non-negative for the separation class | Unproven |
| Relationship between full Weil-type positivity and RH | Known background; cannot be smuggled |
| Condition 2 + Condition 3 implies RH | Conditional logical theorem |

---

# Appendix C: Reference Background

1. A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, 1998/1999.  
2. A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean place*, 2020.  
3. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, 2004.  
4. M. Suzuki, *Li coefficients as norms of functions in a model space*, 2023.  
5. Relevant literature on the classical Guinand–Weil explicit formula, Weil positivity criteria, and Paley–Wiener theory, to be uniformly supplemented with versions, page numbers, and normalizations in the formal public release.

---

# Appendix D: Version Boundaries

v0.1 has completed:

- Spectral coordinates and equivariant orbits;
- Distinction between topological separation / arithmetic separation;
- Abstract specifications for admissible test functions;
- Convolution square orbit blocks;
- Definition of local negative witnesses;
- Equivariant local arithmetic separability;
- Conditional exclusion theorem;
- Paley–Wiener separation costs;
- Finite-dimensional matrix prototypes;
- Circularity audit;
- Formalization plan.

v0.1 has not yet completed:

- Fixing a unique explicit formula normalization;
- Strong local separation theorem;
- Unconditional prime side non-negative cone;
- Unified bounds for on-axis and tail leakages;
- Lean 4 implementation;
- Numerical prototypes;
- Any proof of RH.