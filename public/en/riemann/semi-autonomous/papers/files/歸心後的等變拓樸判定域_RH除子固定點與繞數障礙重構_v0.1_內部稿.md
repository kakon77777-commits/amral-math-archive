# The Equivariant Topological Decision Domain after Re-centering
## A Reconstruction of the Riemann Hypothesis via Divisor Fixed Points and Winding Obstructions

**英文題名：** *The Equivariant Topological Decision Domain after Re-centering: A Reconstruction of the Riemann Hypothesis via Divisor Fixed Points and Winding Obstructions*  
**作者：** Neo.K (Chuan-Wei Hsu)  
**機構：** EveMissLab / Yiyannuo Technology Co., Ltd.  
**版本：** v0.1 (Internal Research Draft)  
**日期：** 2026-07-24  
**性質：** Mathematical Methodology / Equivariant Topology / Complex Analysis / Formalization Foundations / Legitimate RH Proof Research  
**狀態：** Unpublished final draft; does not constitute a proof of the Riemann Hypothesis

---

## Important Declaration: This Article is Not a Proof of the Riemann Hypothesis

This article does not claim to prove the Riemann Hypothesis, nor does it claim that the equivariant topological decision framework established herein is sufficient to deduce the Riemann Hypothesis.

The problem investigated in this article is more foundational:

> **If the Riemann Hypothesis is to obtain a legitimate, verifiable, formalizable proof that does not smuggle in the conclusion, what conditions must its domain of definition, decision domain, intermediary mappings, invariants, obstructions, and lifting procedures satisfy?**

This article retains only the "re-centering" operation from earlier research, and abandons the direct use of kernelization, zero locking, energy, heat flow, phase, potential wells, or physical collision intuitions as RH proof mechanisms. These methods can serve as inspirations, representations, or auxiliary tools, but they can only legitimately participate in the derivation of the original proposition after their domains of definition, scopes of action, equivalences, and lifting theorems have been rigorously proven.

The primary achievement of this article is the establishment of a type-safe reconstruction:

1. Expressing the critical line as the fixed-point set of a marked involution;
2. Expressing nontrivial zeros as a locally finite divisor with a group action;
3. Rewriting the RH as a fixed-point condition of a divisor projection operator;
4. Rewriting off-axis zeros as nonzero winding obstructions of half-strip boundary mappings;
5. Using the TOPO fiber criterion to test whether any intermediary representation loses necessary information for the RH;
6. Explaining the analytic-arithmetic lifting theorem that must additionally be established for a complete proof.

These restatements merely investigate **how the RH might possibly be legitimately proved**, rather than constituting a completed proof.

---

# Abstract

The Riemann Hypothesis is typically stated as all nontrivial zeros of the Riemann zeta function being located on the critical line
\[
\operatorname{Re}s=\frac12.
\]
This proposition appears to be a zero-location problem, but the primary flaw in numerous candidate routes is often not local calculation errors, but rather a lack of legitimate type relationships among the domain of definition, decision domain, and intermediary methods. Symmetry is mistaken for axial fixation, integral kernels are mistaken for the original function itself, physical deformations are mistaken for mathematical equivalence, finite verifications are mistaken for infinite propositions, and topological intuition may lose the information of "which line is the critical line" after forgetting coordinates and markings.

This article proposes an equivariant topological decision framework after re-centering. First, define
\[
F(z)=\xi\left(\frac12+z\right),
\]
such that the original critical line is transformed into the imaginary axis. Then, on the critical strip
\[
X=\left\{z\in\mathbb C:\left|\operatorname{Re}z\right|<\frac12\right\}
\]
introduce the reflection involution
\[
j(z)=-\overline z,
\]
whose fixed-point set is exactly
\[
A=\operatorname{Fix}(j)=i\mathbb R.
\]
The functional equation and real structure generate an equivariant action of the group
\[
G\cong C_2\times C_2
\]
on the zero set. Let \(D_F\) be the zero divisor of \(F\), and let
\[
r(z)=i\,\operatorname{Im}z
\]
be a continuous retraction from \(X\) to \(A\). Its divisor pushforward operator
\[
\mathcal R(D)=r_*D
\]
is an idempotent operator, and
\[
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
\]

To prevent the fixed-point restatement from becoming a mere tautology, this article further establishes half-strip winding obstructions. For any \(\varepsilon>0\) and height \(T>0\), on the zero-free boundary of the right half-critical strip rectangle
\[
U_{\varepsilon,T}^{+}
=
\left\{
z:
\varepsilon<\operatorname{Re}z<\frac12,\ 
|\operatorname{Im}z|<T
\right\}
\]
define the phase mapping
\[
\phi_{\varepsilon,T}(z)=\frac{F(z)}{|F(z)|}.
\]
Its topological degree
\[
\omega_{\varepsilon,T}(F)
=
\deg\phi_{\varepsilon,T}
\]
equals the number of zeros inside the rectangle, counted with multiplicity, by the argument principle. Thus, the RH is equivalent to the vanishing of all such right half-strip obstructions.

This article also introduces the TOPO fiber completeness criterion: if a single fiber of a coarsening map simultaneously contains functions that satisfy the axial zero property and those that do not, then this intermediary layer cannot independently decide the RH. This criterion strictly demonstrates that parity, conjugate symmetry, function order, general kernel positivity, or bare topological type are insufficient to complete the decision.

Finally, this article proposes a six-layer legitimate proof architecture: original analytic definition, re-centering isomorphism, equivariant topology extraction, discrete obstruction establishment, analytic-arithmetic lifting, and ZFC dependency audit. The true uncompleted core is not renaming "zero locking", but proving a non-circular lifting theorem:
\[
\text{Original analytic and arithmetic structure of \(\xi\)}
\Longrightarrow
\omega_{\varepsilon,T}(F)=0
\quad
\text{for all legitimate }(\varepsilon,T).
\]

**Keywords:** Riemann Hypothesis, Re-centering, Equivariant Topology, Divisor, Fixed Point, Winding Number, Argument Principle, Decision Domain, TOPO Fiber, ZFC, Formalized Proof

---

# 0. Foundational Stance: ZFC, Original Proposition, and Proof Dependencies

## 0.1 Research Stance

This article adopts the following internal methodological stance:

> **The original proposition of the Riemann Hypothesis should be viewed as a proposition within the standard ZFC mathematical framework; a proof claimed to "unconditionally complete the original RH" should ultimately be reducible, compilable, or formalizable into a derivation within ZFC, or reside in a conservative and eliminable extension system over the relevant statements.**

This is not a proven metamathematical theorem, nor is it a claim that the RH is necessarily provable in ZFC. Currently, one cannot presuppose:

\[
\mathrm{ZFC}\vdash\mathrm{RH},
\]

nor can one presuppose:

\[
\mathrm{ZFC}\nvdash\mathrm{RH}.
\]

This article merely requires that candidate proofs clearly list their axiomatic dependencies.

If a theory \(T\) is strictly stronger than ZFC, and can only yield

\[
T\vdash\mathrm{RH},
\]

but the extra axioms cannot be eliminated, nor can it be translated into

\[
\mathrm{ZFC}\vdash\mathrm{RH},
\]

then according to the naming conventions of this article, the result should be called:

> **The RH Theorem under Theory \(T\)**

rather than being directly called an unconditional proof of the original RH.

## 0.2 Mathematical Language Does Not Equal Extra Axioms

Using the following tools does not automatically violate the above requirements:

- Topology;
- Algebraic Geometry;
- Category Theory;
- Spectral Theory;
- Probability;
- Computer Verification;
- Lean, Coq, or other proof assistants;
- Temporary models or physical inspirations.

What truly requires auditing is:

1. Whether the objects remain within the legitimate domain of definition of the original proposition;
2. Whether intermediary transformations possess bidirectional equivalence or legitimate lifting;
3. Whether ineliminable extra axioms are added;
4. Whether the final theorem is still the original RH, rather than an analogous proposition;
5. Whether the formalized core can be traced back to explicit axioms and proven theorems.

Therefore, the minimal proof dependency markup adopted in this research is:

\[
\mathfrak D(\Pi)
=
\left(
\mathsf{Base},
\mathsf{Defs},
\mathsf{Imports},
\mathsf{Extra},
\mathsf{Eliminable}
\right),
\]

where \(\Pi\) is the candidate proof. Only when the extra dependencies are empty, or proven to be eliminable, does it pass the "original proposition completeness" audit of this article.

---

# 1. Problem Reset: Retaining Only Re-centering

## 1.1 The Completed Function

Define the Riemann completed function

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}
\Gamma\left(\frac s2\right)\zeta(s).
\]

It is an entire function, and satisfies

\[
\xi(s)=\xi(1-s)
\]

as well as

\[
\xi(\overline s)=\overline{\xi(s)}.
\]

Its zeros correspond exactly to the nontrivial zeros of the zeta function, preserving multiplicity.

## 1.2 Re-centered Coordinates

Let

\[
z=s-\frac12,
\qquad
F(z)=\xi\left(\frac12+z\right).
\]

This transformation is a translation isomorphism of the complex plane, which does not alter:

- Zero multiplicity;
- Analyticity;
- Local topology;
- Zero counting;
- The truth or falsity of the original proposition.

The functional equation becomes

\[
F(-z)=F(z),
\]

and the real structure becomes

\[
F(\overline z)=\overline{F(z)}.
\]

The RH becomes:

\[
\boxed{
F(z)=0
\Longrightarrow
\operatorname{Re}z=0.
}
\]

Therefore, this article retains re-centering, not treating it as a proof, but as a legitimate coordinate normalization.

## 1.3 Why Other Old Mechanisms Are Temporarily Discarded

The following operations cannot directly bear the weight of the RH without prior proof of equivalence:

- Replacing \(F\) with some integral kernel;
- Replacing zero locations with energy minimization;
- Replacing analytic deformation with physical time evolution;
- Replacing off-axis zeros with particle collisions;
- Directly elevating symmetry to fixation;
- Elevating numerical verification to a global theorem.

They may constitute legitimate research, but one must additionally establish:

\[
\text{Original domain proposition}
\iff
\text{Intermediary domain proposition}.
\]

If only a one-way mapping is proven, a lifting theorem sufficient to return to the original problem must also be proven.

---

# 2. Domain of Definition, Mother Domain, and Decision Domain

## 2.1 Four Different Levels

To avoid type confusion, this article distinguishes four domains.

### (1) Function Domain of Definition

\[
F:\mathbb C\longrightarrow\mathbb C.
\]

### (2) Mother Domain of Zero Candidates

After re-centering, nontrivial zeros are located in the critical strip

\[
X
=
\left\{
z\in\mathbb C:
-\frac12<\operatorname{Re}z<\frac12
\right\}.
\]

### (3) Target Subspace

\[
A=i\mathbb R.
\]

The RH requires

\[
Z(F)\subseteq A,
\]

rather than merely requiring

\[
Z(F)\subseteq X.
\]

### (4) Decision Domain

This article does not treat "zeros being locked" as the decision domain, but establishes a discrete obstruction space

\[
\mathcal J
=
\prod_{\alpha\in\mathcal A}\mathbb N_0,
\]

where each coordinate records the number of off-axis zeros within a legitimate half-strip region. The decision mapping is denoted as

\[
\Omega:\mathcal E\longrightarrow\mathcal J.
\]

Ultimately:

\[
\mathrm{RH}
\iff
\Omega(F)=\mathbf 0.
\]

## 2.2 A Class of Functions Rather Than a Single Function

Define a minimal class of functions

\[
\mathcal E
=
\left\{
f\in\operatorname{Hol}(\mathbb C):
f(-z)=f(z),\
f(\overline z)=\overline{f(z)},\
\operatorname{ord}(f)\le 1
\right\}.
\]

The specific \(F\) satisfies

\[
F\in\mathcal E.
\]

The purpose of introducing \(\mathcal E\) is not to generalize the RH, but to check exactly which unique structures of \(F\) a given method utilizes.

If an argument only uses data common to all \(f\in\mathcal E\), and there exist functions in \(\mathcal E\) with off-axis zeros, then that argument cannot deduce the RH based solely on this data.

---

# 3. Equivariant Topology with Involution

## 3.1 The Inadequacy of Bare Topology

If \(X\) is viewed merely as an unmarked topological space, the imaginary axis does not possess an immovable, special identity. Different embedded lines in the plane can be mapped to one another via homeomorphisms.

Therefore, merely saying "using topology" is insufficient to preserve the critical line.

What truly needs to be preserved is:

\[
(X,j),
\]

namely, a topological space equipped with a marked involution.

## 3.2 Critical Involution

Define

\[
j:X\longrightarrow X,
\qquad
j(z)=-\overline z.
\]

Then

\[
j^2=\operatorname{id}_X.
\]

Moreover,

\[
j(z)=z
\iff
z=-\overline z
\iff
\operatorname{Re}z=0.
\]

Thus,

\[
\boxed{
A=\operatorname{Fix}(j)=i\mathbb R.
}
\]

This makes the critical line no longer just an externally added line, but the fixed-point set of a marked involution.

## 3.3 Klein Four-Group Action

Further define

\[
a(z)=-z,
\qquad
b(z)=\overline z.
\]

Then

\[
a^2=b^2=\operatorname{id},
\qquad
ab=ba=j.
\]

Thus, they generate the group

\[
G=\langle a,b\rangle
\cong C_2\times C_2.
\]

Due to \(F(-z)=F(z)\) and the real structure, the zero divisor is invariant under the action of \(G\).

For a general off-axis, non-real point \(\rho\), its orbit is

\[
G\rho
=
\{
\rho,-\rho,\overline\rho,-\overline\rho
\},
\]

which typically has four elements.

If \(\rho\in i\mathbb R\), then

\[
j(\rho)=\rho,
\]

and the orbit shrinks to

\[
G\rho=\{\rho,-\rho\}.
\]

Therefore, the RH can be expressed as:

\[
\boxed{
\text{Every zero has a nontrivial stabilizer containing } j.
}
\]

But it must be emphasized:

> The functional equation only guarantees that the zero divisor is \(G\)-invariant; the RH requires its support to fall within \(\operatorname{Fix}(j)\). Group invariance does not equal pointwise fixation.

---

# 4. Zero Divisors and Fixed-Point Operators

## 4.1 Locally Finite Effective Divisors

Let

\[
\operatorname{Div}_{\mathrm{lf}}^+(X)
\]

denote the locally finite effective divisors on \(X\). Its elements take the form

\[
D
=
\sum_{\rho\in X}m_\rho[\rho],
\qquad
m_\rho\in\mathbb N_0,
\]

and any compact subset intersects only finitely many support points.

Let \(D_F\) be the zero divisor of \(F\) in \(X\):

\[
D_F
=
\operatorname{div}_0(F)
=
\sum_{F(\rho)=0}m_\rho[\rho].
\]

Due to the discreteness of zeros of entire functions, \(D_F\) is locally finite.

## 4.2 Axial Retraction

Define

\[
r:X\longrightarrow A,
\qquad
r(z)
=
\frac{z+j(z)}2
=
i\,\operatorname{Im}z.
\]

It satisfies

\[
r|_A=\operatorname{id}_A
\]

as well as

\[
r\circ r=r.
\]

Thus, \(r\) is a continuous retraction from \(X\) to \(A\).

## 4.3 Divisor Pushforward Operator

Viewing \(A\) as a subspace of \(X\), define

\[
\mathcal R:
\operatorname{Div}_{\mathrm{lf}}^+(X)
\longrightarrow
\operatorname{Div}_{\mathrm{lf}}^+(X),
\qquad
\mathcal R(D)=r_*D.
\]

If

\[
D=\sum_\rho m_\rho[\rho],
\]

then

\[
\mathcal R(D)
=
\sum_\rho m_\rho[r(\rho)],
\]

where multiplicities of identical image points are summed.

From \(r^2=r\), we obtain

\[
\mathcal R^2=\mathcal R.
\]

Thus, \(\mathcal R\) is an idempotent operator.

## 4.4 Fixed-Point Equivalence

### Proposition 4.1

For any \(D\in\operatorname{Div}_{\mathrm{lf}}^+(X)\),

\[
\mathcal R(D)=D
\iff
\operatorname{supp}D\subseteq A.
\]

### Proof

If \(\operatorname{supp}D\subseteq A\), then \(r\) is the identity on every support point, hence \(\mathcal R(D)=D\).

Conversely, the support of \(\mathcal R(D)\) is contained in \(A\). If \(\mathcal R(D)=D\), then the support of \(D\) is also contained in \(A\). This completes the proof.

### Corollary 4.2

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
\]

This is the divisor fixed-point form of the RH.

## 4.5 The True Status of This Operator

The definition of \(\mathcal R\) does not use "the RH is true", because:

- \(X\) is determined by the known critical strip;
- \(j\) is determined by the known functional equation and real structure;
- \(A=\operatorname{Fix}(j)\) can be defined independently;
- \(r\) is an explicit formula.

However, \(\mathcal R\) is still merely a **diagnostic operator**, not a proof operator.

It tells us:

\[
\text{RH is equivalent to } D_F \text{ being a fixed point of some idempotent operator},
\]

but it does not explain why \(D_F\) must be a fixed point.

This corresponds to two things that must be distinguished in the M6 method:

1. Establishing a non-circular fixed-point characterization;
2. Establishing a substantive theorem capable of deducing fixation from the original structure.

This article currently only accomplishes the first task.

---

# 5. Off-axis Divisor Obstructions

## 5.1 Difference in the Free Divisor Group

Embed the effective divisors into the group of locally finite integer-coefficient divisors

\[
\operatorname{Div}_{\mathrm{lf}}(X).
\]

Define

\[
\Theta(D)
=
D-\mathcal R(D).
\]

Then

\[
\Theta(D)=0
\iff
\mathcal R(D)=D.
\]

Thus,

\[
\boxed{
\mathrm{RH}
\iff
\Theta(D_F)=0.
}
\]

\(\Theta(D_F)\) can be called the "off-axis divisor obstruction".

## 5.2 Why Winding Numbers Are Still Needed

\(\Theta\) still directly uses the complete zero divisor, making it computationally close to the original problem. It is suitable for representing logical structure, but does not yet provide a method to decide internal off-axis zeros from boundary data.

For this, the divisor obstruction needs to be projected onto integer-valued topological invariants.

---

# 6. The Right Half-Strip and Winding Obstructions

## 6.1 Why It Suffices to Study the Right Half-Strip

If there exists an off-axis zero \(\rho\), then by \(j\) symmetry,

\[
j(\rho)=-\overline\rho
\]

is also a zero, and their real parts are opposite.

Therefore, any off-axis zero orbit contains at least one zero satisfying

\[
\operatorname{Re}\rho>0.
\]

Thus, excluding zeros in the right half-strip is sufficient to exclude all off-axis zeros.

## 6.2 Truncated Regions

For

\[
0<\varepsilon<\frac12,
\qquad
T>0,
\]

define the right half-strip open rectangle

\[
U_{\varepsilon,T}^+
=
\left\{
z\in X:
\varepsilon<\operatorname{Re}z<\frac12,\
|\operatorname{Im}z|<T
\right\}.
\]

Let

\[
N_{\varepsilon,T}^+(F)
\]

denote the total number of zeros within it, counted with multiplicity.

Even if there are zeros on the boundary, the number of zeros in this open set still has a well-defined meaning.

## 6.3 Regular Parameters and Phase Mappings

Call \((\varepsilon,T)\) \(F\)-regular, if

\[
F(z)\ne0
\qquad
\text{for all } z\in\partial U_{\varepsilon,T}^+.
\]

For regular parameters, define

\[
\phi_{\varepsilon,T}:
\partial U_{\varepsilon,T}^+
\longrightarrow
S^1,
\qquad
\phi_{\varepsilon,T}(z)
=
\frac{F(z)}{|F(z)|}.
\]

Its topological degree is

\[
\omega_{\varepsilon,T}(F)
=
\deg\phi_{\varepsilon,T}.
\]

By the argument principle,

\[
\omega_{\varepsilon,T}(F)
=
\frac{1}{2\pi i}
\oint_{\partial U_{\varepsilon,T}^+}
\frac{F'(z)}{F(z)}\,dz
=
N_{\varepsilon,T}^+(F).
\]

Since \(F\) is an entire function, there are no pole terms.

Therefore,

\[
\omega_{\varepsilon,T}(F)\in\mathbb N_0.
\]

## 6.4 Family of Obstructions

Let

\[
\mathcal A_F
=
\left\{
(\varepsilon,T):
0<\varepsilon<\frac12,\
T>0,\
(\varepsilon,T)\text{ is } F\text{-regular}
\right\}.
\]

Define

\[
\Omega(F)
=
\left(
\omega_{\varepsilon,T}(F)
\right)_{(\varepsilon,T)\in\mathcal A_F}.
\]

Its codomain is

\[
\mathcal J_F
=
\prod_{(\varepsilon,T)\in\mathcal A_F}
\mathbb N_0.
\]

### Theorem 6.1: Equivalence of Winding Obstructions

\[
\boxed{
\mathrm{RH}
\iff
\omega_{\varepsilon,T}(F)=0
\quad
\text{for all } (\varepsilon,T)\in\mathcal A_F.
}
\]

### Proof

If the RH holds, all zeros are located at \(\operatorname{Re}z=0\), while \(U_{\varepsilon,T}^+\) is located at \(\operatorname{Re}z>\varepsilon>0\), so there are no zeros inside it, meaning all winding numbers are zero.

Conversely, if the RH does not hold, there exists a zero \(\rho\) satisfying \(\operatorname{Re}\rho\ne0\). By symmetry, one can choose a zero with a positive real part. Take

\[
0<\varepsilon<\operatorname{Re}\rho
\]

and

\[
T>|\operatorname{Im}\rho|.
\]

Then apply arbitrarily small perturbations to \(\varepsilon,T\) to avoid the discrete set of zeros, making the boundary zero-free. Then

\[
N_{\varepsilon,T}^+(F)\ge1,
\]

thus

\[
\omega_{\varepsilon,T}(F)\ge1.
\]

Contradiction. This completes the proof.

## 6.5 Countable Decision Family

For formalization and computation, one can restrict

\[
\varepsilon\in\mathbb Q\cap\left(0,\frac12\right),
\qquad
T\in\mathbb Q_{>0}.
\]

If an off-axis zero exists, one can always select rational \(\varepsilon,T\) to enclose it, and then select a regular rational boundary. Therefore, a countable family of obstructions is already sufficient for the decision.

---

# 7. What Topology Actually Accomplishes Here

Topology did not prove

\[
\omega_{\varepsilon,T}(F)=0.
\]

What topology accomplishes is the following transformation:

\[
\text{Existence of off-axis zeros}
\longmapsto
\text{Some integer-valued degree is nonzero}.
\]

Its value lies in three points.

## 7.1 Discretization

The continuous position of off-axis zeros is transformed into

\[
\omega_{\varepsilon,T}\in\mathbb N_0.
\]

## 7.2 Homotopy Stability

As long as the boundary mapping does not cross a zero during deformation, the degree remains unchanged.

## 7.3 Local-Global Bridging

The phase winding on the boundary precisely counts the internal zeros.

But topology cannot independently explain:

- Why the degree of every right half-strip rectangle is zero;
- Why the arithmetic structure of the zeta function forces a zero degree;
- Why a certain intermediary deformation will not cross a zero;
- Why finite-height results can be lifted to all heights.

Therefore:

> **Topology is responsible for making the obstructions discrete, stable, and traceable; analysis and arithmetic must still be responsible for proving that the obstructions vanish.**

---

# 8. TOPO Fiber Completeness Check

## 8.1 Coarsening Map

Let

\[
Q:\mathcal E\longrightarrow\mathcal T
\]

be an intermediary coarsening map that only retains certain data, such as:

- Parity;
- Conjugate real structure;
- Function order;
- General growth class;
- A certain kernel representation;
- A certain unmarked topological type.

Let the proposition be

\[
P(f)
=
\begin{cases}
1,&Z(f)\subseteq i\mathbb R,\\
0,&\text{otherwise}.
\end{cases}
\]

If one hopes that \(P\) can descend to a decision on \(\mathcal T\), there must at least exist

\[
\overline P:\mathcal T\to\{0,1\}
\]

such that

\[
P=\overline P\circ Q.
\]

## 8.2 Fiber Constant Criterion

The necessary condition is:

\[
Q(f)=Q(g)
\Longrightarrow
P(f)=P(g).
\]

That is, \(P\) must remain constant on every fiber of \(Q\).

If there exist

\[
f,g\in\mathcal E
\]

such that

\[
Q(f)=Q(g)
\]

but

\[
P(f)\ne P(g),
\]

then \(Q\) has lost the information necessary to decide the RH.

## 8.3 Explicit Counterexample to the Sufficiency of Symmetry, Order, and Bare Topology

Let

\[
f_0(z)=\cosh z.
\]

It is an even entire function with real coefficients, of order one, and all its zeros are located on the imaginary axis:

\[
z=i\pi\left(k+\frac12\right).
\]

Take a complex number \(a\) not located on the real or imaginary axis, and define

\[
q_a(z)
=
(z-a)(z+a)(z-\overline a)(z+\overline a).
\]

Then \(q_a\) is an even polynomial with real coefficients. Now let

\[
f_1(z)=f_0(z)q_a(z).
\]

Then \(f_1\) still:

- Is an even entire function;
- Satisfies the conjugate real structure;
- Is of order one;
- Has the same general symmetry type as \(f_0\).

However, \(f_1\) additionally has an off-axis quadruple of zeros

\[
\{a,-a,\overline a,-\overline a\}.
\]

Therefore, for a coarsening map that only retains parity, real structure, and function order, functions with \(P=1\) and \(P=0\) can simultaneously exist in the same fiber.

The conclusion is:

\[
\boxed{
\text{Functional equation-type symmetry data is insufficient to decide the RH.}
}
\]

Similarly, if a kernelization, phase representation, or physicalization causes the above two types of functions to fall into the same fiber, that representation is also insufficient for the decision.

---

# 9. Spatial State and Type Safety

## 9.1 Minimal Spatial State of the RH

According to the spatial state method, the minimal state of this research can be written as

\[
\Sigma_{\mathrm{RH}}
=
\left(
B,
X,
F,
\Theta,
\mathcal A,
\mathcal P
\right),
\]

where:

- \(B=\mathbb C\): Background complex plane;
- \(X\): Re-centered critical strip;
- \(F\): Completed function;
- \(\Theta=(G,j,A)\): Group action, marked involution, and fixed-point set;
- \(\mathcal A\): Legitimate operators, such as divisor formation, pushforward, boundary restriction, degree;
- \(\mathcal P\): Observations and coarsening, such as zero divisors, truncated counting, winding number families.

Whenever any method introduces a new object \(Y\), it must provide a type declaration:

\[
Y\in\mathsf{Type}(Y),
\]

and legitimate mappings:

\[
\alpha:X\to Y,
\qquad
\beta:Y\to\mathcal J.
\]

If it is ultimately to return to the RH, it must also prove:

\[
\beta(\alpha(F))=0
\Longrightarrow
\Omega(F)=0.
\]

Without this lifting arrow, the intermediary model can only be an inspiration or analogy.

## 9.2 Legitimate Composition Conditions

For a cross-domain chain

\[
\mathcal D_{\mathrm{RH}}
\xrightarrow{Q}
\mathcal T
\xrightarrow{B}
\mathcal K
\xrightarrow{L}
\mathcal J,
\]

one must check one by one:

1. Whether the domain of definition of \(Q\) includes \(F\);
2. What information \(Q\) forgets;
3. Whether \(B\) is a well-defined mapping;
4. Whether \(L\) can return to the decision domain of the RH;
5. Whether the composition \(L\circ B\circ Q\) is compatible with \(\Omega\);
6. Whether the compatibility is equality, one-way implication, or merely empirical correlation.

Only when there exists a commutative relationship

\[
L\circ B\circ Q
=
\Omega
\]

or at least a sufficiently strong implication

\[
L(B(Q(F)))=0
\Longrightarrow
\Omega(F)=0
\]

does the intermediary method possess the logical qualification to complete the RH.

---

# 10. Porting and Limitations of the M6 Method

The M6 research provides three portable principles.

## 10.1 Determine the Mother Domain First

M6 first establishes \(M6^*\), and then acknowledges that primes are merely a proper subset within it.

Correspondingly in the RH:

\[
Z(F)\subset X
\]

is the known mother domain restriction, while

\[
Z(F)\subset A
\]

is the subdomain restriction to be proven.

One cannot mistake "located in the critical strip" for "located on the critical line".

## 10.2 Operators Cannot Be Defined Circularly

\(\mathcal R\) does not take "which points are RH zeros" as input, but only uses the independently defined \(j\), \(A\), and \(r\).

Therefore, the fixed-point characterization is definitionally non-circular.

## 10.3 Single-Limb Localization and Multi-Limb Corroboration

The formalization experience of M6 requires distinguishing:

- Which operator truly accomplishes unique localization;
- Which statistical or ergodic properties only provide corroboration.

In the RH:

- \(\mathcal R(D_F)=D_F\) and \(\Omega(F)=0\) are equivalent localization conditions;
- Zero statistics, finite verifications, average distributions, and numerical calculations can only serve as corroboration, unless there is a separate global lifting theorem.

This article must not splice together multiple necessary properties that "all seem to support the RH" into sufficiency.

---

# 11. Six-Layer Architecture of a Legitimate Proof

This article proposes the following minimal proof architecture.

## Layer 1: Original Analytic Layer

Define in complex analysis and number theory formalizable within ZFC:

\[
\zeta,\quad \xi,\quad F.
\]

Prove:

- Entirety;
- Functional equation;
- Conjugate compatibility;
- Critical strip location;
- Discreteness of zeros.

## Layer 2: Re-centering Isomorphism Layer

Prove that the translation

\[
s\mapsto z=s-\frac12
\]

completely preserves the original proposition.

## Layer 3: Equivariant Topology Layer

Establish:

\[
(X,G,j,A),
\]

and prove

\[
A=\operatorname{Fix}(j).
\]

## Layer 4: Decision Obstruction Layer

Establish:

\[
D_F,\quad \mathcal R,\quad \Theta,\quad \Omega.
\]

Prove the equivalence chain:

\[
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F
\iff
\Theta(D_F)=0
\iff
\Omega(F)=0.
\]

## Layer 5: Substantive Lifting Layer

This is the core that is currently completely uncompleted.

One needs to find a non-circular set of data conditions \(\mathfrak S(F)\), and prove:

\[
\mathfrak S(F)
\Longrightarrow
\Omega(F)=0.
\]

\(\mathfrak S(F)\) must come from the independent analytic or arithmetic structure of \(\xi\), and cannot smuggle "no off-axis zeros" into the assumptions in a renamed form.

## Layer 6: Foundational and Formalization Audit Layer

Finally, one must list:

- ZFC axioms used;
- Cited theorems;
- Extra assumptions;
- Computational certificates;
- Classical logic dependencies;
- Axiom of Choice dependencies;
- Whether uneliminated stronger axioms exist;
- The core trusted base of the proof assistants.

---

# 12. The Missing Core Theorem

This article names the true gap awaiting research as:

## The Equivariant Obstruction Vanishing Lifting Problem

Find a set of non-circular, formalizable structural conditions \(\mathfrak S_\xi\) of \(\xi\), such that

\[
\boxed{
\mathfrak S_\xi
\Longrightarrow
\omega_{\varepsilon,T}(F)=0
\quad
\text{for all regular } (\varepsilon,T).
}
\]

This proposition cannot be replaced by the following synonymous sentences:

- Zeros are locked on the critical line;
- Off-axis zeros cannot exist;
- All right half-strip winding numbers are zero;
- The divisor is a fixed point of the retraction operator;
- Topological obstructions vanish.

These are all equivalent expressions or direct renamings of the RH.

The truly new content must be:

\[
\text{Known or independently provable analytic/arithmetic structure}
\Longrightarrow
\text{Obstruction vanishes}.
\]

---

# 13. Illegitimate or Insufficient Shortcuts

## 13.1 Symmetry as Fixation

Erroneous form:

\[
D_F \text{ is } G\text{-invariant}
\Longrightarrow
\operatorname{supp}D_F\subseteq\operatorname{Fix}(j).
\]

A group-invariant divisor can perfectly well be composed of four-point orbits.

## 13.2 Identifying the Critical Line via Bare Topology

Without the marked involution \(j\), topology cannot distinguish the imaginary axis from other embedded lines.

## 13.3 Fixed-Point Restatement as Proof

\[
\mathcal R(D_F)=D_F
\]

Although formally clean, it is still merely an equivalent proposition to the RH.

## 13.4 Kernel Representations Automatically Preserving Zero Decisions

Unless the kernel mapping is proven to be fiber-constant with respect to the relevant proposition, kernelization may lose necessary information.

## 13.5 Physical Dynamics Replacing Analytic Theorems

If the language of energy, heat flow, collisions, phase transitions, or steady states cannot be compiled into legitimate mathematical mappings and theorems, it can only be viewed as an analogy.

## 13.6 Finite-Height Verification Replacing Global Proof

Proving

\[
\omega_{\varepsilon,T}(F)=0
\]

for all \(T\le T_0\) cannot deduce it for all \(T\).

There must be a separate tail theorem or infinite lifting.

## 13.7 Unstated Stronger Axioms

If a candidate proof uses an extra axiom \(A\), it must be marked as

\[
\mathrm{ZFC}+A\vdash\mathrm{RH},
\]

until \(A\) is eliminated or proven to be a conservative extension.

---

# 14. Formalization Research Plan

## 14.1 Phase 1: Equivalence Framework

Establish in Lean 4 / Mathlib:

1. Interface between the completed function and the re-centered function;
2. Critical strip \(X\);
3. Involutions \(a,b,j\);
4. \(G=C_2\times C_2\) action;
5. \(A=\operatorname{Fix}(j)\);
6. Zero divisors;
7. Retraction \(r\);
8. Idempotent divisor operator \(\mathcal R\);
9. Equivalence of the RH and the fixed-point condition.

## 14.2 Phase 2: Winding Obstructions

Formalize:

1. Right half-strip rectangles;
2. Regular boundaries;
3. Circle-valued mapping of \(F/|F|\);
4. Topological degree;
5. Argument principle;
6. Equality of degree and number of zeros;
7. Equivalence of the RH and the vanishing of all obstructions.

## 14.3 Phase 3: TOPO Fiber Tester

For each candidate intermediary method \(Q\), require the output:

\[
\operatorname{FiberTest}(Q,P).
\]

Test items:

- Whether counterexamples of different decisions in the same fiber are found;
- What invariants are lost;
- Whether a lifting mapping exists;
- Whether the lifting is single-valued;
- Whether the lifting preserves multiplicity;
- Whether the lifting preserves universal quantifiers;
- Whether extra axioms are added.

## 14.4 Phase 4: Lifting Theorem Search

Only after the first three phases are completed should one research possible \(\mathfrak S_\xi\).

The research goal is not to invent yet another RH equivalent, but to find:

\[
\mathfrak S_\xi
\not\equiv
\mathrm{RH}
\]

and

\[
\mathfrak S_\xi
\Longrightarrow
\Omega(F)=0.
\]

---

# 15. Falsifiability and Failure Conditions

The equivalence portion of this framework can be directly checked. If any of the following points fail, the corresponding part of this article must be corrected:

1. The fixed-point set of \(j(z)=-\overline z\) is not the imaginary axis;
2. \(D_F\) is not locally finite in \(X\);
3. \(\mathcal R\) is not a well-defined locally finite divisor operator;
4. \(\mathcal R^2\ne\mathcal R\);
5. \(\mathcal R(D)=D\) is not equivalent to the support being located in \(A\);
6. The winding number of a regular right half-strip does not equal the number of internal zeros;
7. A countable rational parameter family is insufficient to capture arbitrary off-axis zeros;
8. The ZFC dependency declaration confuses methodological language with axiomatic dependencies.

More importantly, even if all the above hold, it does not deduce the RH. If the lifting theorem of Layer 5 cannot be established, this article should permanently remain as:

> **Legitimate RH Proof Architecture and Decision Domain Reconstruction**

rather than an RH proof.

---

# 16. Conclusion

This article retains only re-centering.

After re-centering, the mathematical identity of the RH can be cleanly rewritten as:

\[
F(z)=\xi\left(\frac12+z\right),
\]

\[
X=\left\{\left|\operatorname{Re}z\right|<\frac12\right\},
\]

\[
j(z)=-\overline z,
\]

\[
A=\operatorname{Fix}(j)=i\mathbb R,
\]

\[
D_F=\operatorname{div}_0(F).
\]

The divisor fixed-point form is:

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
\]

The winding obstruction form is:

\[
\boxed{
\mathrm{RH}
\iff
\omega_{\varepsilon,T}(F)=0
\quad
\text{for all legitimate right half-strips.}
}
\]

Neither of these forms proves the RH.

What they accomplish is:

1. Separating the original domain of definition from the decision domain;
2. Transforming the critical line into the fixed-point set of a marked involution;
3. Strictly distinguishing zero symmetry from pointwise fixation;
4. Transforming off-axis zeros into integer-valued topological obstructions;
5. Establishing a fiber information loss check for any intermediary method;
6. Providing clear interfaces for formalization and ZFC dependency audits.

Therefore, this article's core judgment on the RH is:

> **The difficulty of the RH should no longer be vaguely described as "how to lock the zeros", but should be precisely described as: how to prove the vanishing of the entire family of equivariant winding obstructions from the independent analytic and arithmetic structure of \(\xi\), under conditions that are non-circular, do not cross incorrect types, do not lose universal quantifiers, and do not introduce unstated extra axioms.**

If a true proof exists, it must cross this lifting arrow:

\[
\boxed{
\text{Original analytic/arithmetic structure}
\Longrightarrow
\Omega(F)=\mathbf0.
}
\]

Until this arrow is legitimately established, all fixed points, topology, kernels, phases, dynamics, or computational results can only be decision frameworks, local certificates, research intermediaries, or analogies, rather than a completed proof of the original Riemann Hypothesis.

---

# Appendix A: Minimal Glossary of Symbols

| Symbol | Meaning |
|---|---|
| \(\xi(s)\) | Riemann completed function |
| \(F(z)\) | Re-centered completed function \(\xi(1/2+z)\) |
| \(X\) | Re-centered critical strip |
| \(a(z)\) | Central inversion \(-z\) |
| \(b(z)\) | Complex conjugate \(\overline z\) |
| \(j(z)\) | Critical reflection \(-\overline z\) |
| \(G\) | \(C_2\times C_2\) symmetry group |
| \(A\) | \(\operatorname{Fix}(j)=i\mathbb R\) |
| \(D_F\) | Zero divisor of \(F\) |
| \(r\) | Axial retraction \(i\operatorname{Im}z\) |
| \(\mathcal R\) | Divisor pushforward idempotent operator |
| \(\Theta\) | Off-axis divisor obstruction \(D-\mathcal R(D)\) |
| \(U_{\varepsilon,T}^+\) | Right half-strip truncated rectangle |
| \(\omega_{\varepsilon,T}\) | Topological degree of the boundary phase mapping |
| \(\Omega(F)\) | Family of all right half-strip winding obstructions |
| \(Q\) | TOPO coarsening / controlled forgetting map |
| \(\mathfrak S_\xi\) | Independent lifting condition yet to be discovered |

---

# Appendix B: Minimal Equivalence Chain

\[
\mathrm{RH}
\]

\[
\iff
Z(F)\subseteq i\mathbb R
\]

\[
\iff
\operatorname{supp}D_F\subseteq\operatorname{Fix}(j)
\]

\[
\iff
\mathcal R(D_F)=D_F
\]

\[
\iff
\Theta(D_F)=0
\]

\[
\iff
N_{\varepsilon,T}^+(F)=0
\quad
\text{for all } \varepsilon,T
\]

\[
\iff
\omega_{\varepsilon,T}(F)=0
\quad
\text{for all regular } \varepsilon,T.
\]

This entire chain belongs to restatement and decision domain reconstruction, and does not contain a substantive proof of the RH.

---

# Appendix C: Internal Theoretical Sources and Roles

## C.1 Triple Fixed-Point Characterization on M6*

Ported content:

- Establish the candidate mother domain first;
- Separation of the target subset and the mother domain;
- Operator definitions must not presuppose the property to be decided;
- Fixed-point localization and statistical corroboration must be divided;
- Formalization changes the precise shape of the claims.

Unported content:

- Specific divisibility topology of M6;
- Prime minimum factor operator;
- Statistical and ergodic operators themselves.

## C.2 TOPO Theory

Ported content:

- Topology as controlled forgetting;
- Coarsening-intermediary-lifting chain;
- Fiber constant decision criterion;
- Failure of invariant survival;
- Lifting gap;
- Non-closing residuals of commutative diagrams.

## C.3 Spatial State Theory

Ported content:

- Base space, types, operators, and observations must be jointly marked;
- Common representation does not equal common operation;
- Coarse-graining is generally irreversible;
- Illegitimate cross-type composition must be blocked;
- Intermediary methods must leave traceable interfaces.

---

# Appendix D: Version Boundaries

Completed in v0.1:

- Non-proof declaration;
- ZFC methodological stance;
- Equivariant mother space after re-centering;
- Divisor fixed-point restatement;
- Winding obstruction restatement;
- TOPO fiber insufficiency criterion;
- Six-layer legitimate proof architecture;
- Formalization research plan.

Not yet completed in v0.1:

- Lean 4 implementation;
- Complete formalization details of divisor pushforward;
- Argument principle interface;
- Systematic review of external mathematical literature;
- Non-circular analytic-arithmetic lifting theorem;
- Any form of RH proof.