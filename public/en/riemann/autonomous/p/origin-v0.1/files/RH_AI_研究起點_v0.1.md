# Riemann Hypothesis AI Research Starting Point v0.1
## A Non-Proof Research Draft Cleaned Up from Four Old Manuscripts

**Original Concept:** Neo.K  
**Research Restructuring and Methodological Arrangement:** Aletheia (GPT-5.6 Thinking)  
**Date:** July 23, 2026  
**Nature:** Open problem research draft, experimental specifications, and AI research interface  
**Explicit Status:** Non-proof, non-theorem declaration, non-assertion of the validity of the Riemann Hypothesis

---

## 0. Document Boundaries

This document does not claim any of the following:

- Does not claim to have proved the Riemann Hypothesis;
- Does not claim to have found new equivalent conditions for the Riemann Hypothesis;
- Does not claim that the "Observer Dimension Theory" has become a mathematical theory;
- Does not claim that analytic continuation is equivalent to arbitrary parameterized projection;
- Does not claim the existence of a universal, unique "optimal observation angle";
- Does not refer to numerical minima, visual patterns, or finite-height verifications as proofs;
- Does not mistake the movement of zeros after coordinate transformations for the emergence of new structures in the original function;
- Does not consider the loss of the Euler product or multiplicativity as a contradiction.

This document only does four things:

1. Preserves the original intention of the research;
2. Organizes known and verifiable mathematical anchors;
3. Downgrades unsubstantiated narratives into falsifiable research hypotheses;
4. Establishes a research state that can be jointly advanced by AI, numerical computation, and formalization tools.

---

# 1. Original Research Intention

The initial intuition was not to "replace proof with imagery," but rather:

> The same mathematical object may exhibit vastly different visible structures across different coordinates, representations, integral formulas, kernel transformations, and deformation families. Rather than solely focusing on the final proposition, it is better to turn "how to observe, how to represent, how to deform" itself into a controllable, comparable, and falsifiable object of research.

This original intention can be preserved, but it requires stepping back from ontological declarations to research methodology:

- Do not presuppose that a certain representation is more "true";
- Do not presuppose that information metrics are necessarily optimal at $\operatorname{Re}(s)=\tfrac12$;
- Do not presuppose that optimal parameters exist or are unique;
- Do not presuppose that observed patterns logically imply the RH;
- Even if a path fails, preserve its breaking points, counterexamples, and reusable tools.

Therefore, the spirit of this project is not:

$$
\text{Generate a seemingly complete proof narrative},
$$

but rather:

$$
\text{Generate candidate structures}
\rightarrow
\text{Decompose proof obligations}
\rightarrow
\text{Actively seek counterexamples}
\rightarrow
\text{Preserve verifiable residues}.
$$

---

# 2. Cleanup Results of the Four Sources

This draft only uses the following four original materials:

1. *Riemann Hypothesis Thought Experiment 3.0 — Public Corrected Version*;
2. *Riemann Hypothesis Thought Experiment 3.0 — Public Final Version*;
3. *Observer Dimension Theory of Analytic Continuation: A Paradigm Revolution in Mathematics*;
4. *Dynamic Projection Experiment: Verifying the Map Nature of Analytic Continuation through "Parameter Tuning"*.

After cleanup, the content is divided into four categories.

| Category | Handling Method |
|---|---|
| Known classical results | Retained, but marked with external sources; not classified as new results of this document |
| Reproducible numerical computations | Retained as experiments and software tests; not elevated to theoretical evidence |
| Valuable research intuitions | Rewritten as hypotheses, candidate definitions, or research questions |
| Overclaims, circular reasoning, category confusion | Deleted or added to the failure database |

---

# 3. Known Mathematical Anchors

The following items serve as hard anchors that research agents must not rewrite on their own.

## 3.1 Status of the Riemann Hypothesis

The Riemann Hypothesis currently remains an open problem. Its standard form is: all non-trivial zeros $\rho$ of the Riemann $\zeta$ function satisfy

$$
\operatorname{Re}(\rho)=\frac12.
$$

Numerical verification up to a finite height does not equate to a global proposition.

## 3.2 Domain of Dirichlet Series and the Euler Product

For

$$
\operatorname{Re}(s)>1
$$

we have

$$
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}
=\prod_p\left(1-p^{-s}\right)^{-1}.
$$

The region of direct convergence for this Euler product does not include the critical strip

$$
0<\operatorname{Re}(s)<1.
$$

Therefore, any reasoning claiming "the Euler product holds, thus the zeros in the critical strip must lie on the critical line" lacks a logical bridge.

## 3.3 Analytic Continuation and the Functional Equation

The completed function can be written as

$$
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s),
$$

and satisfies

$$
\xi(s)=\xi(1-s).
$$

To avoid notational confusion, this document distinguishes between two centered representations.

Complex centered coordinates:

$$
X(z):=\xi\!\left(\frac12+z\right),
\qquad
X(z)=X(-z).
$$

Real spectral coordinates:

$$
\Xi(t):=\xi\!\left(\frac12+it\right),
$$

where for $t\in\mathbb R$, $\Xi(t)$ is a real-valued even function.

## 3.4 Zero Symmetry Does Not Equal Zero Fixation

The functional equation and conjugate symmetry cause non-trivial zeros to form corresponding symmetric orbits. If $\rho$ is a zero, the related points typically include

$$
\rho,
\quad
1-\rho,
\quad
\overline{\rho},
\quad
1-\overline{\rho}.
$$

The invariance of a set under an involution does not imply that every element is a fixed point of the involution:

$$
J(Z)=Z
\not\Rightarrow
\forall \rho\in Z,\ J(\rho)=\rho.
$$

This is one of the core reasons why the original "symmetry locking" narrative fails.

## 3.5 Argument Principle

If there are no zeros or poles on the closed curve $\Gamma$, then

$$
\frac{1}{2\pi i}
\oint_\Gamma
\frac{f'(z)}{f(z)}\,dz
=
N_\Gamma-P_\Gamma.
$$

Symmetric zeros within the same counterclockwise contour are generally counted with the same sign and do not automatically cancel out due to mirror symmetry.

## 3.6 de Bruijn–Newman Deformation

Taking the standard kernel $\Phi(u)$, define

$$
H_t(z)
=
\int_0^\infty
 e^{tu^2}\Phi(u)\cos(zu)\,du.
$$

This family satisfies

$$
\frac{\partial H_t}{\partial t}
=
-\frac{\partial^2H_t}{\partial z^2}.
$$

There exists a de Bruijn–Newman constant $\Lambda$ such that the zeros of $H_t$ are all real if and only if

$$
t\geq\Lambda.
$$

The known relationship is

$$
RH
\Longleftrightarrow
\Lambda\leq0.
$$

Rodgers–Tao have established

$$
\Lambda\geq0.
$$

Published rigorous numerical results also yield

$$
\Lambda\leq0.2.
$$

Thus, it can currently be written as

$$
0\leq\Lambda\leq0.2,
$$

and

$$
RH
\Longleftrightarrow
\Lambda=0.
$$

This is a restatement of known facts and bounds, not a new derivation of this research.

## 3.7 Rigorous Verification at Finite Heights

Existing work using interval arithmetic and rigorous error bounds has confirmed: up to the height

$$
0<\operatorname{Im}(\rho)\leq3\times10^{12}
$$

the non-trivial zeros in this range lie on the critical line. This result remains solely a finite-height proposition.

---

# 4. Retainable Computational Tools

The following items can be retained as reproducible tools, but must not be claimed as new theorems of this document.

## 4.1 Jacobi Theta Transformation

Let

$$
\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},
$$

then

$$
\theta(1/t)=\sqrt t\,\theta(t).
$$

It can be used to transform numerically slow-converging regions into faster-converging ones.

## 4.2 Mellin–Theta Representation

Let

$$
\psi(t)=\sum_{n\geq1}e^{-\pi n^2t},
$$

then a symmetric integral representation can be used to compute the completed $\zeta$ function. This type of representation is suitable for:

- Numerical regression testing of the functional equation;
- Computation of function values in the critical strip;
- Cross-validation between different implementations.

It does not provide a direct proof of the RH.

## 4.3 Argument Counting

$$
N_\Gamma-P_\Gamma
=
\frac{1}{2\pi i}
\oint_\Gamma\frac{f'}{f}
$$

can be converted into a regional zero-counting procedure. Actual rigorous verification still requires:

- Certificates of no zeros/poles on the boundary;
- Integral error bounds;
- Interval arithmetic;
- Coordination with Turing's method when necessary.

## 4.4 Log-Gaussian Weights

The weights in the old drafts

$$
g_\lambda(n)
=
\exp\!\left[-\frac{\lambda}{4}(\log n)^2\right]
$$

satisfy

$$
\frac{g_\lambda(pq)}{g_\lambda(p)g_\lambda(q)}
=
\exp\!\left[-\frac{\lambda}{2}\log p\log q\right].
$$

Thus, for $\lambda\neq0$, it generally lacks multiplicativity. This is a correct algebraic fact, but there is currently no logical bridge to the RH. Its reasonable use is to study smoothing kernels, numerical weighting, and the loss of multiplicative structure, rather than to manufacture contradictions.

---

# 5. Content That Must Be Deleted or Downgraded

## 5.1 "Analytic Continuation is a Projection Family"

For a fixed analytic germ, analytic continuation is governed by uniqueness under compatible and connected conditions. A new function obtained by arbitrarily changing parameters cannot automatically be called another analytic continuation of the same function.

The original concept is rewritten as:

> Study different representations, coordinates, integral formulas, truncation schemes, and valid deformation families of the same mathematical object, and compare their observable structures.

## 5.2 "Unique Optimal Observation Angle"

There is no universal reason to guarantee that an optimal parameter necessarily exists, is unique, or equals $\tfrac12$. Any optimization must first specify:

- Parameter space;
- Allowed transformations;
- Objective function;
- Topology and compactness;
- Whether it is invariant under reparameterization.

At most, it can only be written as a task-relative problem:

$$
\theta^*(J,\Theta)
\in
\operatorname*{argmin}_{\theta\in\Theta}
J(\mathcal O_\theta).
$$

Existence and uniqueness themselves are propositions to be studied.

## 5.3 "Scanning $\beta$ to Find $\beta=\tfrac12$"

If zeros known to lie on the critical line are first used as seeds, and then different lines are compared, the experiment will feed input bias back into the output. In particular, `zetazero(n)` returns the representation of zeros on the critical line; it cannot be used again to prove that the critical line is privileged.

## 5.4 "The More Equidistant the Zeros, the Truer"

The original spacing of Riemann zeros is not equidistant. When studying local spacing, one must first unfold it according to the average zero density, for example using

$$
\overline N(T)
\approx
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+
\frac78,
$$

and defining the unfolded coordinates

$$
x_n=\overline N(\gamma_n),
\qquad
s_n=x_{n+1}-x_n.
$$

Even if a certain deformation decreases the coefficient of variation of the spacing, one can only say that this metric has decreased; it does not imply the RH.

## 5.5 "Coordinate Distortion Generates New Zero Information"

If

$$
F_\alpha(s)=\zeta(T_\alpha(s))
$$

and $T_\alpha$ is invertible, then

$$
F_\alpha(s)=0
\Longleftrightarrow
T_\alpha(s)\in Z(\zeta).
$$

This is merely the preimage of the zero set. If the image becomes skewed, scaled, or rotated, it may be entirely a coordinate effect.

## 5.6 "Losing the Euler Product is a Contradiction"

The fact that a function no longer has multiplicative coefficients or an Euler product after deformation does not violate the Fundamental Theorem of Arithmetic. This original proof path is closed, unless an additional theorem is found in the future that can establish a non-circular implication between the non-multiplicativity of a specific deformation and the negation of the RH.

## 5.7 "The Normal Operation of Technology Supports the RH"

The related mathematics appearing in RSA, QED, hash functions, and string theory do not provide valid Bayesian evidence for $\Lambda=0$. All such narratives are removed from the main body of research.

---

# 6. Observation Framework Research Hypotheses

The original "Observer Dimension Theory" is downgraded and reconstructed into the following operational framework.

## 6.1 Basic Data

Let $O$ be the research object and $\Theta$ be the parameter space. For each $\theta\in\Theta$, define

$$
\mathcal O_\theta
=
M_\theta\bigl(T_\theta(O)\bigr),
$$

where:

- $T_\theta$ represents a valid transformation of the object, coordinates, or representation;
- $M_\theta$ represents an observable, numerical procedure, or feature extractor;
- $\mathcal O_\theta$ is the actual obtained observation result.

The "observer" here is merely an indexed framework and does not refer to a psychological subject.

## 6.2 Five Types of Operations Must Be Separated

### A. Coordinate Transformation

The same object represented in different coordinates. The main issues are covariance and invariants.

### B. Representation Transformation

For example, series, integrals, Fourier representations, Mellin representations, or operator representations. They may change computability but do not change the underlying object.

### C. Function Deformation

For example, the de Bruijn–Newman family $H_t$. Different parameters usually mean different functions, but one can study how zeros evolve with the parameters.

### D. Analytic Continuation

Expanding from local analytic data to a larger domain, constrained by the identity theorem and monodromy conditions. It is not an arbitrary parameter scan.

### E. Numerical Approximation

Truncation, discretization, finite precision, and root finders produce approximate observations, which must be accompanied by an error model.

## 6.3 Invariants and Defect Quantities

For coordinate or representation transformations, one can look for

$$
I(\mathcal O_\theta)=I(O).
$$

For true deformations, one should not presuppose invariance, but rather track

$$
\Delta_I(\theta)
=
I(T_\theta O)-I(O).
$$

The research questions are: which quantities are preserved, which quantities change, and whether the changes exhibit monotonicity or critical behavior.

---

# 7. Experimental Families Applicable to the Riemann Hypothesis

## 7.1 Control Group: Pure Coordinate Transformations

Invertible transformations such as translation, rotation, scaling, and shearing should first serve as negative controls. Their purpose is to confirm that the research system can distinguish:

$$
\text{Image changes}
\neq
\text{New mathematical information}.
$$

## 7.2 Main Experimental Family A: de Bruijn–Newman Heat Flow

This is a deformation family with a known logical interface to the RH. One can study:

- Zero trajectories;
- Near-collisions and Lehmer pairs;
- Condition numbers of zeros;
- Local dynamics in the $t$-direction;
- Computational certificates required for existing upper and lower bounds.

However, numerical tracking can only improve bounds or discover local structures; it cannot automatically achieve $\Lambda\leq0$.

## 7.3 Main Experimental Family B: Explicit Formulas and Test Functions

Let $\mathcal H$ be the space of allowed test functions, and consider the functional coupling the zero side and the prime side

$$
Q(f).
$$

If adopting the Weil-type positivity route, the core research interface is not "looks the most regular," but rather:

$$
RH
\Longleftrightarrow
\forall f\in\mathcal H,
\quad
Q(f)\geq0.
$$

Subsequent research can study the generating family $\mathcal G$, the compression of negative witnesses, and positivity closure.

## 7.4 Main Experimental Family C: Comparison of Computational Representations

When comparing Riemann–Siegel, theta–Mellin, contour integrals, and other representations, reasonable goals are:

- Error;
- Condition number;
- Computational cost;
- Stability under height growth;
- Sensitivity to zero localization.

An optimal representation merely means it is more effective for a specific computational task; it does not mean that the representation proves the RH.

---

# 8. Acceptable Experimental Metrics

## 8.1 Function Residuals

$$
r_\theta(z)=|F_\theta(z)|.
$$

Precision, truncation error, and root-finding stopping criteria must be reported simultaneously.

## 8.2 Condition Number of Zeros

For a simple zero $z_0$, the local sensitivity is related to

$$
\kappa(z_0)
\sim
\frac1{|F'(z_0)|}
$$

. Near multiple zeros or zero collisions, the condition number may deteriorate sharply.

## 8.3 Symmetry Defects

When the corresponding function is indeed supposed to possess relevant symmetries, one can define

$$
D_{\mathrm{sym}}(z)
=
|X(z)-X(-z)|
+
|X(z)-\overline{X(\overline z)}|.
$$

This quantity is primarily used to check whether the numerical implementation breaks known symmetries; it is not used to prove that all zeros are fixed points.

## 8.4 Unfolded Spacing Statistics

Unfold the zeros using the average counting function, then compute local statistics. Any statistical results are marked as `EXPERIMENTAL` and are not to be conflated with global zero localization.

## 8.5 Integer-Type Certificates

The argument principle, Turing's method, and interval arithmetic can form stronger computational certificates. Only results with explicit error bounds and boundary conditions are marked as `CERTIFIED_NUMERICAL`.

---

# 9. Falsifiable Bridges and Research Graph

This project does not directly generate

$$
\varnothing\Longrightarrow RH,
$$

but rather builds a research graph.

## 9.1 Target Node

$$
P_0:
\quad
\text{Determine whether the observation framework/deformation method can produce non-circular, non-trivial RH constraints.}
$$

## 9.2 Candidate Bridges

### $M_1$: Completeness of Operation Classification

Each experiment must be unambiguously classified as a coordinate transformation, representation transformation, function deformation, analytic continuation, or numerical approximation.

Failure witness: The same operation is inconsistently classified by different modules, or lacks a verifiable definition.

### $M_2$: Non-Trivial Deformability

The candidate deformation family cannot merely be a renaming of invertible coordinate transformations. It must be determined whether there exists $C_\theta$ such that

$$
F_\theta=C_\theta^{-1}F_0C_\theta.
$$

If completely conjugate, the observed changes might just be a representation effect.

### $M_3$: Metric-Proposition Interface

If an objective function $J(\theta)$ is used, an explicit theorem interface must be established:

$$
\text{Some property of } J(\theta)
\Longrightarrow
\text{Some known RH equivalent or necessary condition}.
$$

Without this interface, optimization only has data analysis significance.

### $M_4$: Compression of Negative Witnesses

If a positivity criterion is adopted, it must be studied whether arbitrary negative witnesses can be compressed into a controllable generating family:

$$
Q(w)<0
\Longrightarrow
\exists g\in\mathcal G,
\quad
Q(g)<0.
$$

### $M_5$: Positivity of the Generating Family

$$
\forall g\in\mathcal G,
\quad
Q(g)\geq0.
$$

This is a high-risk node; it must be checked whether it is implicitly equivalent to the RH.

### $M_6$: Positivity Closure

If $g_n\to f$, it requires sufficient conditions to deduce

$$
Q(g_n)\geq0
\Longrightarrow
Q(f)\geq0
$$

proper continuity or closed quadratic form conditions. The direction of standard lower semi-continuity inequalities must not be written backwards.

---

# 10. AI Research Agent Specifications

The research state is denoted as

$$
S_t=
(P_t,K_t,M_t,T_t,\Omega_t,F_t,C_t,D_t),
$$

where:

- $P_t$: Target proposition;
- $K_t$: Known hard anchors;
- $M_t$: Candidate bridges;
- $T_t$: Secondary propositions required for the bridges;
- $\Omega_t$: Candidate definitions, deformations, and test families;
- $F_t$: Records of failures, counterexamples, and circularities;
- $C_t$: Computational results and error certificates;
- $D_t$: Dependency graph.

Each cycle is

$$
\text{Analyze}
\rightarrow
\text{Generate}
\rightarrow
\text{Retrieve}
\rightarrow
\text{Backfill}
\rightarrow
\text{Compute}
\rightarrow
\text{Verify}
\rightarrow
\text{Falsify}
\rightarrow
\text{Update}.
$$

## 10.1 AI Division of Labor

- **Construction Agent:** Generates definitions, bridges, and local derivations;
- **Skeptic Agent:** Searches for counterexamples, circularities, quantifier errors, and scope confusions;
- **Literature Agent:** Determines whether propositions are known, miscited, or already have counterexamples;
- **Computation Agent:** Performs high-precision and interval computations;
- **Formalization Agent:** Feeds closable fragments into Lean;
- **Dependency Audit Agent:** Confirms that the RH itself does not appear in the ancestor nodes of candidate bridges.

## 10.2 State Tags

- `KNOWN`: Externally known results;
- `REPRODUCED`: Reproducible computations or derivations;
- `CERTIFIED_NUMERICAL`: Finite computations with rigorous error certificates;
- `EXPERIMENTAL`: General numerical observations;
- `CONJECTURAL`: Candidate propositions;
- `FORMALIZED`: Complete verification in a formal system;
- `BLOCKED`: Missing bridges;
- `REFUTED`: Existing counterexamples or logical errors;
- `CIRCULAR`: Dependent on the target proposition or its equivalent forms.

Except for externally known theorems or complete formalized results, the "proved" tag is not used.

---

# 11. Phase One Execution Sequence

## Cycle 0: Source Cleanup

Status: Completed.

Output:

- Claims removed;
- Known results separated from original intuitions;
- Failed proof chains preserved as a counterexample database;
- Dynamic projections reclassified.

## Cycle 1: Regression Testing of Classical Tools

Reproduce:

- Theta transformation;
- Mellin representation;
- Functional equation;
- Argument counting;
- Non-multiplicativity of log-Gaussian weights.

This cycle only tests the research environment and does not seek new conclusions for the RH.

## Cycle 2: Control Group

Implement invertible coordinate transformations to confirm that the system will not mistake:

- Skewing;
- Rotation;
- Scaling;
- Shearing;

for new discoveries of zero structures.

## Cycle 3: de Bruijn–Newman Local Dynamics

Establish modules for zero tracking, condition numbers, near-collisions, and error control. The research output is primarily local dynamics data and algorithmic stability.

## Cycle 4: Positivity Bridges

Select explicit Weil-type or related positivity forms, attempt to define a computable generating family $\mathcal G$, and prioritize attacking $M_4$, $M_5$, and $M_6$.

## Cycle 5: Formalization Interface

Feed local lemmas that do not depend on the RH into Lean, and prohibit the use of:

- `sorry`;
- Unlisted additional axioms;
- Claiming completion after taking the main bridge as an assumption.

---

# 12. Currently Most Important Research Questions

1. Can an observation metric insensitive to reparameterization be established?
2. Which deformations truly change the function, and which merely change the coordinates?
3. In the de Bruijn–Newman heat flow, which local zero dynamics can be automatically classified and formalized by AI?
4. Does there exist a natural generating family $\mathcal G$ such that negative witnesses can be compressed into it?
5. Is positivity on the generating family easier than the full RH, or is it merely a repackaging of the RH?
6. Can the local prime terms and infinite place terms in explicit formulas form a computable compensation mechanism?
7. Which numerical results can be upgraded to interval arithmetic certificates?
8. Which local propositions are already suitable for Lean, and which still lack analytic function libraries?
9. Can the observation framework method generate truly new invariants, rather than renaming existing representations?
10. If all candidate bridges fail, can the reasons for failure be compressed into an explicit impossibility result?

---

# 13. Current Conclusions

After cleaning up the four old drafts, no proof of the Riemann Hypothesis remains, nor does any theorem stating that "analytic continuation has a unique optimal observation angle."

What remains are three usable assets:

1. **A precise map of failures.** This includes typical errors such as the misuse of symmetry, confusion over the domain of the Euler product, conflation of deformation and continuation, and the elevation of numerical results to proofs.
2. **A set of reproducible tools.** This includes theta transformations, Mellin representations, argument counting, heat flow deformations, and high-precision computation interfaces.
3. **A research intuition that can be re-established.** No longer claiming an "observer ontology," but rather studying how different representations and deformations alter visible structures, and which visible quantities genuinely connect to the RH.

Therefore, the new research starting point is not:

$$
\text{We are already close to proving the RH},
$$

but rather:

$$
\text{We have established a research environment that does not allow false proofs to survive}.
$$

This environment can now be handed over to AI for long-term iteration. Its criterion for success is not generating longer narratives, but reducing the following cycle by cycle:

- Undefined concepts;
- Circular dependencies;
- Numerical metrics without causal links;
- Unbackfillable bridges;
- Hypotheses that have not been actively attacked.

If there is ultimately no proof, verifiable local theorems, algorithms, counterexamples, formalized modules, and failure boundaries should still remain.

---

# References

1. B. Rodgers and T. Tao, *The De Bruijn–Newman Constant Is Non-Negative*, Forum of Mathematics, Pi 8 (2020), e6; arXiv:1801.05914.
2. D. H. J. Polymath, *Effective Approximation of Heat Flow Evolution of the Riemann $\xi$ Function, and a New Upper Bound for the De Bruijn–Newman Constant*, Research in the Mathematical Sciences 6 (2019); arXiv:1904.12438.
3. D. Platt and T. Trudgian, *The Riemann Hypothesis Is True up to $3\cdot10^{12}$*, Bulletin of the London Mathematical Society 53 (2021), 792–797; arXiv:2004.09765.
4. NIST Digital Library of Mathematical Functions, Chapter 25: Riemann Zeta Function.
5. Clay Mathematics Institute, *The Riemann Hypothesis*, Millennium Prize Problems.
6. Neo.K, *Riemann Hypothesis Thought Experiment 3.0 — Public Corrected Version*.
7. Neo.K, *Riemann Hypothesis Thought Experiment 3.0 — Public Final Version*.
8. Neo.K, *Observer Dimension Theory of Analytic Continuation: A Paradigm Revolution in Mathematics*.
9. Neo.K, *Dynamic Projection Experiment: Verifying the Map Nature of Analytic Continuation through "Parameter Tuning"*.