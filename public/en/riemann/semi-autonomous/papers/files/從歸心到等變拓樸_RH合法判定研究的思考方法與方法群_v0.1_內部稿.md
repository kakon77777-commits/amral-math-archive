# From Re-centering to Equivariant Topology
## Methodological Thinking and Methodological Architectures for the Legal Formulation of Riemann Hypothesis Research

**英文題名：** *From Re-centering to Equivariant Topology: A Methodological Architecture for Legally Formulating Research on the Riemann Hypothesis*  
**作者：** Neo.K (Chuan-Wei Hsu)  
**機構：** EveMissLab / Yiyannuo Technology Co., Ltd.  
**版本：** v0.1 (Internal Methodology Draft)  
**日期：** 2026-07-24  
**性質：** Mathematical Research Methodology / Topological Methodological Architecture / Complex Analysis / Formal Foundations / RH Research Program  
**狀態：** Internal Draft; Not a Proof of the Riemann Hypothesis

---

## Important Declaration

This document is not a proof of the Riemann Hypothesis, nor does it claim that the methodological architecture proposed herein is sufficient to prove the Riemann Hypothesis.

This document does not investigate "how to quickly provide a new proof of the RH," but rather:

> **If one is to study the RH, which modes of thinking are mathematically legal? Which mathematical methods can be integrated into a unified proof architecture? What exactly can and cannot be achieved by each method?**

The primary task of this document is to establish a methodological architecture and a research sequence so that subsequent research will not repeatedly make the following errors:

- Mistaking symmetry for fixedness;
- Mistaking kernel representations for the original proposition;
- Mistaking physical intuition for mathematical equivalence;
- Mistaking finite verification for infinite theorems;
- Mistaking topological analogies for topological proofs;
- Mistaking results under stronger axioms for the original RH;
- Splicing multiple necessary conditions into a sufficient condition;
- Treating a renamed RH as a new theorem.

This document solely retains "re-centering" as a legal and necessary coordinate normalization. On this foundation, it establishes a methodological architecture comprising equivariant topology, configuration spaces, effective divisors, positive obstructions, stratification, filtration, sheaf theory, topological separation, arithmetic test functions, and formal auditing.

---

# Abstract

Research on the Riemann Hypothesis has long suffered from a methodological problem: although numerous candidate approaches employ advanced analysis, topology, physics, dynamical systems, spectral theory, or computational methods, their difficulties may not solely stem from technical inadequacies. They may also arise from a lack of legal relationships among the domain of definition, the domain of determination, the intermediary domain, and the lifting procedures.

This document proposes a methodology of "reconstructing legality first, then researching the proof." The first step retains only re-centering:
\[
F(z)=\xi\left(\frac12+z\right),
\]
rewriting the RH such that all zeros of \(F\) lie on the imaginary axis. The second step does not directly seek a "zero-locking mechanism," but rather establishes an equivariant topological space with a marked involution:
\[
j(z)=-\overline z,
\qquad
\operatorname{Fix}(j)=i\mathbb R.
\]
The third step represents the zeros as locally finite effective divisors under the action of \(G\cong C_2\times C_2\), further establishing fixed-point conditions, positive obstructions, orbit-type stratification, and height filtration. The fourth step uses the TOPO fiber criterion to check whether any intermediary method loses the information required for RH determination. The fifth step employs sheaf theory and local-global gluing to manage the lifting between finite certificates and infinite propositions. The sixth step positions the core that could genuinely generate proof content as "whether topological separation can be lifted to arithmetically admissible separation," which means lifting the separation of off-axis mass on the orbit space into test functions that can enter the explicit formula for \(\zeta\), thereby establishing a contradiction from the prime side.

Therefore, this document proposes a methodological architecture with a clear division of labor:

\[
\text{Re-centering}
\to
\text{Equivariant Topology}
\to
\text{Configuration & Positive Obstructions}
\to
\text{Stratification & Filtration}
\to
\text{Sheafified Local-Global}
\to
\text{Topological Separation}
\to
\text{Analytic Lifting}
\to
\text{Arithmetic Sign Control}
\to
\text{ZFC Auditing}.
\]

Herein, topology is not responsible for directly proving the RH, but for identifying orbit types, establishing non-cancelable obstructions, localizing off-axis zeros, and managing global quantifiers; analysis is responsible for constructing legal test functions and controlling limits; arithmetic is responsible for establishing signs or bounds on the prime side of the explicit formula; and the formal system is responsible for verifying whether definitions, types, dependencies, and liftings genuinely hold.

**Keywords:** Riemann Hypothesis, Re-centering, Equivariant Topology, Configuration Space, Effective Divisor, Positive Obstruction, Stratified Topology, Sheaf Theory, Explicit Formula, Test Function, ZFC, Formal Proof

---

# 1. The Core Shift of This Round of Research

## 1.1 Stepping Back from "How to Prove" to "How to Legally Prove"

Past research tended to directly ask:

> What kind of mechanism can lock the zeros onto the critical line?

However, this question itself is premature.

Before distinguishing among the domain of definition, the domain of determination, the intermediary domain, and the lifting conditions, "locking" might merely be a physical metaphor, or simply a renaming of the RH.

This round of research asks instead:

> **If any candidate method is to participate in the proof of the original RH, what legality checks must it pass?**

This shift has three effects:

1. Separating proofs from analogies;
2. Separating restatements from substantive progress;
3. Separating methodological language from axiomatic dependencies.

## 1.2 Retaining Only Re-centering

Re-centering is:

\[
z=s-\frac12,
\qquad
F(z)=\xi\left(\frac12+z\right).
\]

Its legality stems from the fact that it is merely a translational isomorphism of the complex plane.

Re-centering adds no assumptions and loses neither zeros nor multiplicities; thus, it can be fully retained.

After re-centering:

\[
F(-z)=F(z),
\]

and the RH becomes:

\[
F(z)=0
\Longrightarrow
\operatorname{Re}z=0.
\]

This step proves nothing new, but it transforms the critical line into a central fixed set, enabling precise expression in subsequent equivariant topology.

## 1.3 Temporarily Suspended Old Methods

This document does not claim that the following methods are permanently invalid, but temporarily revokes their "direct proof qualifications":

- Kernelization;
- Heat flow;
- Zero collision;
- Phase locking;
- Energy minimization;
- Physical potential wells;
- Topological quantization;
- Total positivity intuition;
- Purely finite-height verification.

If these methods are to be reintroduced, they must provide complete type declarations, equivalence theorems, or lifting theorems.

---

# 2. General Principles of Method Usage

## 2.1 Each Method Only Performs the Work It Can Legally Accomplish

This document adopts the principle of "methodological division of labor" rather than "a single omnipotent method."

Any given method must answer:

1. What is its input type?
2. What is its output type?
3. What information does it preserve?
4. What information does it forget?
5. Does it provide an equivalence, a necessary condition, a sufficient condition, or merely a heuristic?
6. Can it be lifted back to the original RH proposition?
7. What axioms and external theorems does it use?

## 2.2 Restatement Does Not Equal Proof

If one establishes:

\[
\mathrm{RH}\iff P,
\]

then only a new form of determination has been completed.

A true proof still requires:

\[
\text{Independent Known Structures}
\Longrightarrow P.
\]

If \(P\) is merely "all off-axis obstructions vanish" or "the zero divisor is a fixed point," it remains an equivalent restatement of the RH.

## 2.3 Necessary Conditions Cannot Accumulate into Sufficient Conditions

If it is known that:

\[
\mathrm{RH}\Longrightarrow A,
\]

\[
\mathrm{RH}\Longrightarrow B,
\]

\[
\mathrm{RH}\Longrightarrow C,
\]

one cannot thereby deduce:

\[
A\land B\land C\Longrightarrow\mathrm{RH}.
\]

unless there is another theorem proving its sufficiency.

## 2.4 Intermediary Methods Must Pass the Fiber Constancy Check

If:

\[
Q:\mathcal D\to\mathcal T
\]

is a coarsening map, and the RH determination function is:

\[
P:\mathcal D\to\{0,1\},
\]

then for \(P\) to be determinable in \(\mathcal T\), it requires at least:

\[
Q(x)=Q(y)
\Longrightarrow
P(x)=P(y).
\]

If true and false instances coexist within the same fiber, the intermediary representation has lost the information required for the RH.

## 2.5 Must Ultimately Fall Back to ZFC-Auditable Derivations

This document adopts the following stance:

> A complete proof of the original RH should ultimately be formalizable in ZFC, or be able to fall back to ZFC from an extension system that is conservative over the relevant statements and eliminable.

Using stronger languages, computers, topology, category theory, or physical heuristics is not inherently problematic.

The issue lies in whether there exist ineliminable additional axioms or extra ontological assumptions.

---

# 3. Overview of the Methodological Architecture

This document proposes the following methodological architecture:

\[
\boxed{
\mathfrak M_{\mathrm{RH}}
=
\{
M_0,M_1,\ldots,M_9
\}
}
\]

Where:

- \(M_0\): Re-centering and Domain Normalization;
- \(M_1\): Equivariant Topology;
- \(M_2\): Zero Configuration Space;
- \(M_3\): Effective Divisors and Positive Obstruction Semirings;
- \(M_4\): Orbit-Type Stratified Topology;
- \(M_5\): Height Filtration and Persistent Obstructions;
- \(M_6\): Sheafified Local-Global Methods;
- \(M_7\): Orbit Space Topological Separation;
- \(M_8\): Analytic Admissible Lifting;
- \(M_9\): Arithmetic Sign Control and Formal Auditing.

These methods are not nine competing proof routes, but rather nine division-of-labor layers within the same research architecture.

---

# 4. Method \(M_0\): Re-centering and Domain Normalization

## 4.1 Function

Transforms:

\[
\operatorname{Re}s=\frac12
\]

into:

\[
\operatorname{Re}z=0.
\]

Establishes:

\[
F(z)=\xi\left(\frac12+z\right).
\]

## 4.2 What It Can Do

- Preserve zeros and multiplicities;
- Transform the functional equation into evenness;
- Transform the critical line into a central fixed set;
- Facilitate group actions and involution representations.

## 4.3 What It Cannot Do

- Cannot deduce that all zeros are on the imaginary axis from evenness;
- Cannot deduce pointwise fixedness from symmetry;
- Cannot autonomously generate a zero-exclusion mechanism.

## 4.4 Criterion for Success

Must prove that the propositions before and after re-centering are completely equivalent.

---

# 5. Method \(M_1\): Equivariant Topology

## 5.1 Basic Objects

Define:

\[
a(z)=-z,
\qquad
b(z)=\overline z,
\qquad
j(z)=-\overline z.
\]

Group:

\[
G=\langle a,b\rangle
\cong C_2\times C_2.
\]

Critical line:

\[
A=\operatorname{Fix}(j)=i\mathbb R.
\]

## 5.2 Function

Equivariant topology is responsible for:

- Preserving which subspace is the critical line;
- Describing zero orbits;
- Distinguishing between group invariance and pointwise fixedness;
- Defining orbit stabilizer types.

## 5.3 What It Cannot Do

Equivariant topology itself cannot deduce:

\[
Z(F)\subseteq A.
\]

Because a \(G\)-invariant zero set can perfectly well consist of off-axis quadruplets.

## 5.4 Rules of Usage

One must not use only a bare topological space \(X\).

One must use objects with marked involutions:

\[
(X,G,j,A).
\]

---

# 6. Method \(M_2\): Zero Configuration Space

## 6.1 Basic Objects

Let:

\[
\mathscr D_G(X)
\]

denote the space of locally finite, \(G\)-invariant effective zero divisors on \(X\).

Each zero divisor is:

\[
D=\sum_\rho m_\rho[\rho].
\]

## 6.2 Function

The configuration space is responsible for:

- Transforming infinite zero sets into stratifiable geometric objects;
- Preserving multiplicities;
- Preserving orbit structures;
- Allowing height truncation;
- Establishing fixed points and obstruction operators.

## 6.3 Three Main Strata

They can be classified by support type into:

\[
\mathscr D_{\mathrm{axis}},
\qquad
\mathscr D_{\mathrm{mixed}},
\qquad
\mathscr D_{\mathrm{off}}.
\]

Where:

- \(\mathscr D_{\mathrm{axis}}\): All zeros are located on the critical line;
- \(\mathscr D_{\mathrm{mixed}}\): Both on-axis and off-axis zeros exist simultaneously;
- \(\mathscr D_{\mathrm{off}}\): Has off-axis support.

The RH is precisely:

\[
D_F\in\mathscr D_{\mathrm{axis}}.
\]

## 6.4 What It Cannot Do

Configuration classification only marks which stratum \(D_F\) should fall into; it does not explain why it falls into that stratum.

---

# 7. Method \(M_3\): Effective Divisors and Positive Obstructions

## 7.1 Why Groupification Cannot Be Done Too Early

Ordinary homology or free abelian groups allow positive and negative cancellations.

However, zero divisors are effective divisors:

\[
m_\rho\ge0.
\]

Off-axis zeros cannot "disappear" due to sign cancellation.

## 7.2 Positive Obstruction Semiring

For a finitely truncated region, define:

\[
\mu_T(D)
=
\left(
n_{\mathrm{axis}}(T),
n_{\mathrm{off}}(T)
\right)
\in\mathbb N_0^2.
\]

Or, more finely recording the orbit types:

\[
\mu_T(D)
=
\sum_{[H]}
n_{[H]}(T)e_{[H]}.
\]

Where \([H]\) denotes the stabilizer conjugacy class.

## 7.3 Function

The positive obstruction method is responsible for:

- Preventing algebraic cancellation;
- Preserving multiplicities;
- Converting off-axis existence into non-negative integers;
- Establishing monotonic height obstructions.

## 7.4 Core Condition

The RH is equivalent to:

\[
n_{\mathrm{off}}(T)=0
\qquad
\forall T.
\]

## 7.5 What It Cannot Do

Positive obstructions can only guarantee that "if there are off-axis zeros, the obstruction is non-zero"; they cannot autonomously prove that the obstruction is zero.

---

# 8. Method \(M_4\): Orbit-Type Stratified Topology

## 8.1 Basis for Stratification

For each point \(z\in X\), consider the stabilizer:

\[
G_z=\{g\in G:g\cdot z=z\}.
\]

Stratify \(X\) according to stabilizer types:

\[
X=\bigsqcup_{[H]}X_{([H])}.
\]

## 8.2 Key Strata

- Trivial stabilizer stratum: General off-axis points;
- \(\langle j\rangle\) stabilizer stratum: Imaginary axis points;
- \(\langle b\rangle\) stabilizer stratum: Real axis points;
- Full group stabilizer stratum: The origin.

## 8.3 Stratified Form of the RH

\[
\operatorname{supp}D_F
\subseteq
X_{(\langle j\rangle)}
\cup X_{(G)}.
\]

Since the origin is not a non-trivial zero, it practically falls primarily into \(X_{(\langle j\rangle)}\).

## 8.4 Function

Stratified topology is responsible for:

- Precisely distinguishing different orbit types;
- Describing how off-axis zeros form quadruplet orbits;
- Providing interfaces for sheaf theory, local certificates, and orbit spaces.

---

# 9. Method \(M_5\): Height Filtration and Persistent Obstructions

## 9.1 Height Filtration

Define:

\[
X_T=
\{z\in X:|\operatorname{Im}z|\le T\}.
\]

Restrict the divisor:

\[
D_F^{(T)}=D_F|_{X_T}.
\]

Off-axis obstruction:

\[
\Omega_T(F)=n_{\mathrm{off}}(D_F^{(T)}).
\]

## 9.2 Monotonicity

If:

\[
T_1<T_2,
\]

then:

\[
\Omega_{T_1}(F)\le\Omega_{T_2}(F).
\]

## 9.3 Function

Height filtration is responsible for:

- Managing infinite zero sets;
- Decomposing global propositions into finite truncations;
- Recording when off-axis obstructions appear;
- Connecting numerical verification with formal certificates.

## 9.4 What It Cannot Do

Zero obstruction at a finite height cannot deduce zero obstruction at all heights.

There must be an additional tail theorem:

\[
\Omega_T(F)=0
\quad
(T\le T_0)
\]

coupled with:

\[
\text{Analytic exclusion for }T>T_0
\]

to complete the global result.

---

# 10. Method \(M_6\): Sheafified Local-Global Methods

## 10.1 Zero Divisor Sheaf

For an open set \(U\subseteq X\), define:

\[
\mathscr Z(U)
=
\operatorname{Div}_{\mathrm{lf}}^+(U).
\]

For an inclusion relation \(V\subseteq U\), there exists a restriction map:

\[
\mathscr Z(U)\to\mathscr Z(V).
\]

## 10.2 Off-Axis Obstruction Sheaf

Define:

\[
\mathscr Z_{\mathrm{off}}(U)
=
\operatorname{Div}_{\mathrm{lf}}^+(U\setminus A).
\]

The RH is equivalent to the global section:

\[
D_F^{\mathrm{off}}
\]

being the zero section.

## 10.3 Boundary Winding Numbers and Cosheaf-like Data

For a zero-free boundary of a bounded region \(U\), the winding number:

\[
\omega_U(F)
=
\frac{1}{2\pi i}
\int_{\partial U}
\frac{F'(z)}{F(z)}\,dz
\]

records the number of interior zeros.

When different regions are glued together, the boundary contributions are additive.

## 10.4 Function

Sheafified methods are responsible for:

- Local zero data;
- Compatibility on overlapping regions;
- Gluing of local certificates;
- Rational rectangular coverings;
- The logical relationship between finite certificates and global zero sections.

## 10.5 The True Gap

Whether local zero everywhere can deduce global zero depends on:

- Whether the covering is complete;
- Whether infinity is controlled;
- Whether there is limit escape;
- Whether there is a tail theorem.

---

# 11. Method \(M_7\): Orbit Space Topological Separation

## 11.1 Orbit Space

Define:

\[
Y=X/G.
\]

The zero divisor descends to a positive discrete measure on the orbit space:

\[
\nu_F
=
\sum_{[\rho]\in Y}
m_{[\rho]}\delta_{[\rho]}.
\]

Decomposition:

\[
Y=Y_{\mathrm{axis}}\sqcup Y_{\mathrm{off}}.
\]

The RH is equivalent to:

\[
\nu_F(Y_{\mathrm{off}})=0.
\]

## 11.2 Topological Separation

If:

\[
K\subset Y_{\mathrm{off}}
\]

is a compact set, and disjoint from \(Y_{\mathrm{axis}}\), topologically one can usually construct a continuous function \(u\) such that:

\[
u|_K=1,
\qquad
u|_{Y_{\mathrm{axis}}}=0.
\]

## 11.3 Function

Topological separation is responsible for:

- Localizing arbitrary off-axis orbits;
- Transforming "the existence of off-axis zeros" into "the existence of separable positive mass";
- Proposing target specifications for the construction of analytic test functions.

## 11.4 Limitations

Ordinary continuous functions may not necessarily be able to enter the explicit formula for \(\zeta\).

Therefore, topological separation only accomplishes:

\[
\text{Existence of a continuous separating function}.
\]

It has not yet accomplished:

\[
\text{Existence of an arithmetically admissible separating function}.
\]

---

# 12. Method \(M_8\): Analytic Admissible Lifting

## 12.1 The Core GAP

The truly difficult arrow is:

\[
\boxed{
\text{Topologically Separable}
\;\dashrightarrow\;
\text{Explicit Formula Admissibly Separable}
}
\]

## 12.2 Admissible Test Function Class

It is necessary to establish a test function class:

\[
\mathcal H_{\mathrm{adm}},
\]

whose elements must satisfy:

- Sufficient regularity;
- Sufficient decay;
- Existence of Fourier transform;
- Controllability of Gamma terms;
- Convergence of prime sums;
- Legality of summation on the zero side;
- Exchangeability of limits and integrals;
- Preservation of required signs.

## 12.3 Target Lifting Theorem

For any compact set:

\[
K\subset Y_{\mathrm{off}},
\]

one hopes there exists:

\[
h_K\in\mathcal H_{\mathrm{adm}},
\]

such that its zero-side weight can detect the positive mass on \(K\), and control the contributions from the axis and other orbits.

Conceptually:

\[
\nu_F(K)>0
\Longrightarrow
\mathcal Z_F(h_K)<0
\]

or form other signs that can contradict the prime side.

## 12.4 Function

Analytic lifting is responsible for:

- Smoothing topological localizations;
- Establishing Paley–Wiener type control;
- Guaranteeing the legality of the explicit formula;
- Quantifying separation errors;
- Preventing on-axis and tail contributions from drowning out the off-axis signal.

## 12.5 Only This Layer Can Potentially Generate New Proof Content

Without this layer, all the aforementioned topological methods are merely a determination framework.

---

# 13. Method \(M_9\): Arithmetic Sign Control and Explicit Formula

## 13.1 The Explicit Formula Bridge

Written abstractly:

\[
\mathcal Z_F(h)
=
\mathcal P_\zeta(h)
+
\mathcal G(h)
+
\mathcal E(h),
\]

Where:

- \(\mathcal Z_F(h)\): Zero side;
- \(\mathcal P_\zeta(h)\): Prime and prime power side;
- \(\mathcal G(h)\): Gamma and infinity terms;
- \(\mathcal E(h)\): Normalization or boundary terms.

## 13.2 The True Proof Mode

If off-axis mass exists, the topological and analytic layers hope to construct:

\[
h\in\mathcal H_{\mathrm{adm}}
\]

such that:

\[
\mathcal Z_F(h)<0.
\]

On the other hand, if the arithmetic side can independently prove:

\[
\mathcal P_\zeta(h)
+
\mathcal G(h)
+
\mathcal E(h)
\ge0,
\]

then a contradiction arises.

Therefore:

\[
\nu_F(Y_{\mathrm{off}})=0.
\]

## 13.3 Division of Labor

\[
\boxed{
\begin{aligned}
\text{Topology}&:\text{ Separates off-axis orbits;}\\
\text{Analysis}&:\text{ Constructs admissible test functions;}\\
\text{Arithmetic}&:\text{ Controls the signs of the explicit formula;}\\
\text{Formalization}&:\text{ Audits all derivations.}
\end{aligned}
}
\]

## 13.4 The Greatest Risk

Sign control in the explicit formula might be equivalent to the RH itself.

Therefore, one must check whether:

\[
\text{The positivity conditions used}
\]

have already secretly incorporated the information that "all zeros are on the critical line."

---

# 14. Formalization and ZFC Auditing

## 14.1 Formalization is Not an Appendix

The role of formalization is not to stamp the paper at the very end, but to correct the shape of the claims in advance.

Each module should have:

- Definitions;
- Input types;
- Output types;
- Preconditions;
- Conclusion strength;
- External theorems;
- Unproven assumptions;
- Eliminability.

## 14.2 Suggested Modules

### Module A: Re-centering and Group Actions

- \(\xi\) and \(F\);
- \(a,b,j\);
- Klein four-group;
- Fixed point sets.

### Module B: Divisors and Configurations

- Locally finite divisors;
- Group invariance;
- Orbit decomposition;
- Effectiveness.

### Module C: Positive Obstructions

- Off-axis orbit counting;
- Height monotonicity;
- Non-cancelability.

### Module D: Sheaves and Winding Numbers

- Open set restriction;
- Boundary regularity;
- Argument principle;
- Gluing.

### Module E: TOPO Fiber Testing

- Intermediary mappings;
- Same-fiber counterexamples;
- Information loss reporting;
- Lifting interfaces.

### Module F: Test Functions and Explicit Formulas

- Admissible classes;
- Convergence;
- Limit exchange;
- Prime side and zero side.

## 14.3 Axiom Dependency Table

Each major theorem is marked with:

\[
\mathsf{Deps}(T)
=
(
\mathsf{ZFC},
\mathsf{Classical},
\mathsf{Choice},
\mathsf{Imported},
\mathsf{Extra}
).
\]

If:

\[
\mathsf{Extra}\ne\varnothing,
\]

then it must not be marked as an unconditional proof of the original RH, unless elimination is completed.

---

# 15. Sequence of Using the Methodological Architecture

## Phase One: Establishing the Master Framework

1. Re-centering;
2. Equivariant topology;
3. Zero configuration space;
4. Orbit-type stratification;
5. Positive obstruction semiring.

This phase only establishes the domain of determination.

## Phase Two: Establishing Local-Global Management

1. Height filtration;
2. Rational rectangles;
3. Local divisor sheaf;
4. Boundary winding numbers;
5. Gluing and tail gaps.

This phase establishes the certificate structure.

## Phase Three: Establishing Separation-Lifting

1. Orbit space;
2. Off-axis compact sets;
3. Topological separation;
4. Smoothing and approximation;
5. Admissible test functions;
6. Error and tail control.

This phase begins to touch upon substantive proof content.

## Phase Four: Arithmetic Contradiction and Auditing

1. Explicit formula;
2. Prime side signs;
3. Gamma terms;
4. Off-axis mass detection;
5. Global obstruction vanishing;
6. ZFC / Lean auditing.

Only if this phase is successful can one possibly approach a proof of the RH.

---

# 16. Methods Not Recommended for Priority Use

## 16.1 General Homology Groups

Premature groupification may allow positive obstructions to cancel out.

## 16.2 Fundamental Groups or Higher Homotopy Groups

Currently, there is no clear evidence indicating that they can perceive the effective multiplicities of off-axis zeros.

## 16.3 Persistent Homology as a Proof

It can serve as data analysis, but cannot automatically bear the weight of analytic theorems.

## 16.4 Quantum Topology or Physical Topology

Without precise objects, morphisms, functors, and lifting theorems, they can only be regarded as analogies.

## 16.5 Re-establishing the Heat Flow Route

Heat flow may have independent value, but it would reintroduce issues of physicalization and deformation legality, and should not be mixed into the main thread of this round.

## 16.6 Undefined RH Cohomology

Before possessing clear geometric objects and cohomology theories, one should not presuppose the existence of structures directly analogous to the Weil conjectures.

---

# 17. Falsifiability Conditions of This Methodological Architecture

This program is not an irrefutable philosophical framework.

The following situations would force a revision of the methodological architecture:

1. Equivariant orbit types provide no additional structure beyond ordinary zero counting;
2. The positive obstruction semiring cannot be connected to the explicit formula;
3. Sheafified local certificates cannot control infinity;
4. Topological separation cannot be approximated by any admissible test function;
5. Admissible test functions cannot maintain the off-axis detection signs;
6. Prime side sign control is completely equivalent to the RH itself;
7. The orbit space lacks the required separation properties;
8. All possible liftings inevitably introduce ineliminable additional axioms.

If these situations occur, this methodological architecture can still be retained as a determination and auditing tool, but can no longer be viewed as a possible main thread for a proof.

---

# 18. The Most Important Intellectual Outcomes of This Round

## 18.1 Topology is Not Meant to Replace Analysis

The functions of topology are:

\[
\text{Identification, Stratification, Localization, Discretization, Gluing}.
\]

The functions of analysis are:

\[
\text{Approximation, Convergence, Decay, Limits, Sign Control}.
\]

The function of arithmetic is:

\[
\text{Bringing the prime sources of }\zeta\text{ back to zero determination}.
\]

## 18.2 The True Core is Not "Topology Proving the RH"

The true core is:

\[
\boxed{
\text{Can topological separation be lifted to arithmetic admissible separation?}
}
\]

If this arrow cannot be established, topology remains merely a beautiful language of classification.

## 18.3 The Methodological Difficulties of the RH Lie Between Domains

The most important GAPs in this round are:

\[
\text{Zero Geometry}
\dashrightarrow
\text{Topological Obstructions},
\]

\[
\text{Topological Obstructions}
\dashrightarrow
\text{Analytic Test Functions},
\]

\[
\text{Analytic Test Functions}
\dashrightarrow
\text{Arithmetic Signs},
\]

\[
\text{Finite Certificates}
\dashrightarrow
\text{Global Propositions}.
\]

Therefore, research should not merely endlessly strengthen tools within a single domain, but should establish these lifting arrows one by one.

---

# 19. Subsequent Paper Cluster

## Paper One

### *Equivariant Zero Configuration Topology*
**Subtitle:** RH Orbit-Type Stratification, Effective Divisor Semirings, and Positive Obstructions

Research:

- \(G\)-invariant divisor spaces;
- Orbit types;
- Effective obstructions;
- Burnside positive semirings;
- Height filtration.

## Paper Two

### *Sheafified Zero Obstructions and Local-Global Lifting*
**Subtitle:** From Rational Rectangular Certificates to Full Critical Strip Determination

Research:

- Divisor sheaves;
- Winding number cosheaves;
- Local certificates;
- Gluing;
- Tail control.

## Paper Three

### *Equivariant Arithmetic Separation*
**Subtitle:** From Orbit Space Localization to Admissible Test Functions for the \(\zeta\) Explicit Formula

Research:

- Orbit space separation;
- Admissible test functions;
- Paley–Wiener type lifting;
- Off-axis mass detection.

## Paper Four

### *Off-Axis Positive Obstructions in the Explicit Formula*
**Subtitle:** Zero-Side Detection, Prime-Side Signs, and ZFC-Auditable Contradiction Architectures

Research:

- Explicit formula;
- Positivity;
- Prime side estimation;
- Gamma terms;
- Formal dependencies.

---

# 20. Conclusion

This round of research has not yielded a proof of the RH, nor does it claim that topology can directly prove the RH.

What this round has truly accomplished is a methodological reconstruction:

\[
\boxed{
\begin{aligned}
&\text{Retain only re-centering;}\\
&\text{Use equivariant topology to preserve the identity of the critical line;}\\
&\text{Use configuration spaces to carry zero divisors;}\\
&\text{Use positive obstructions to prevent algebraic cancellation;}\\
&\text{Use orbit-type stratification to distinguish on-axis from off-axis;}\\
&\text{Use height filtration to manage infinite quantifiers;}\\
&\text{Use sheaf theory to handle local-global relations;}\\
&\text{Use topological separation to locate off-axis mass;}\\
&\text{Use analysis to lift to admissible test functions;}\\
&\text{Use arithmetic and the explicit formula to establish contradictions;}\\
&\text{Use formalization and ZFC auditing to guarantee the integrity of the original proposition.}
\end{aligned}
}
\]

Therefore, this methodological architecture is not a stacking of names like "Topological XX-ology," but a research architecture with a strict division of labor.

The most important sentence among these is:

> **Topology is responsible for telling us where the off-axis obstructions are, what type they belong to, and how they are localized and preserved; if a true proof of the RH exists, it must still be proven by analytic and arithmetic structures that these obstructions cannot possibly exist.**

And the core question most worthy of subsequent investment is:

\[
\boxed{
\text{Can the topological separation of arbitrary off-axis orbits be lifted to arithmetic admissible separation in the }\zeta\text{ explicit formula?}
}
\]

This is the first legal entry point in this round for moving from "topological restatement" to "potentially generating substantive proof content."

---

# Appendix A: Methodological Architecture Function Table

| Method | Primary Input | Primary Output | What It Can Do | What It Cannot Do |
|---|---|---|---|---|
| Re-centering | \(\xi(s)\) | \(F(z)\) | Normalize the center | Prove zeros are on the axis |
| Equivariant Topology | \(X,G,j\) | Orbits and fixed sets | Preserve critical line identity | Exclude quadruplet orbits |
| Configuration Space | Zero divisors | Stratified divisor spaces | Preserve multiplicities and orbits | Explain why it falls into the on-axis stratum |
| Positive Obstructions | Effective divisors | \(\mathbb N_0\)-valued obstructions | Prevent cancellation | Prove obstructions are zero |
| Stratified Topology | Group actions | Stabilizer types | Distinguish on-axis/off-axis | Provide arithmetic reasons |
| Height Filtration | Infinite zero sets | Truncated obstruction families | Manage global quantifiers | Deduce infinite from finite |
| Sheaf Theory | Local zero data | Gluing structures | Local-global management | Automatically control infinity |
| Topological Separation | Orbit space | Continuous separating functions | Locate off-axis mass | Guarantee explicit formula usability |
| Analytic Lifting | Continuous separating functions | Admissible test functions | Convergence and decay control | Provide prime side signs |
| Arithmetic Control | Explicit formula | Signs or contradictions | Connect back to prime structures | Replace foundational auditing |
| Formal Auditing | All derivations | Core verification | Check types and dependencies | Create missing theorems |

---

# Appendix B: Minimal Research Workflow

\[
\xi
\overset{\text{Re-centering}}{\longrightarrow}
F
\]

\[
F
\overset{\text{Divisor}}{\longrightarrow}
D_F
\]

\[
D_F
\overset{\text{Equivariant Stratification}}{\longrightarrow}
D_F^{\mathrm{axis}}
\oplus
D_F^{\mathrm{off}}
\]

\[
D_F^{\mathrm{off}}
\overset{\text{Positive Obstruction}}{\longrightarrow}
\Omega(F)
\]

\[
\Omega(F)\ne0
\overset{\text{Topological Separation}}{\longrightarrow}
u_K
\]

\[
u_K
\overset{\text{Analytic Lifting}}{\longrightarrow}
h_K\in\mathcal H_{\mathrm{adm}}
\]

\[
h_K
\overset{\text{Explicit Formula}}{\longrightarrow}
\text{Zero-side / Prime-side Contradiction}
\]

\[
\Longrightarrow
\Omega(F)=0
\]

\[
\Longrightarrow
\mathrm{RH}.
\]

What has currently been established is the legal framework of the first half; the lifting and arithmetic contradiction in the second half remain unfinished research problems.