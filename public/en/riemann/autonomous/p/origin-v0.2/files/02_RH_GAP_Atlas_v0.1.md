# Riemann Hypothesis GAP Atlas v0.1
## A Non-Proof Research Gap Atlas Established via RIITG, RAB, and KCPE/AMRAL

**Original Research Direction:** Neo.K  
**Methodological Reconstruction and First-Round Registration:** Aletheia (GPT-5.6 Thinking)  
**Date:** 2026-07-23  
**Nature:** Research engineering document, gap registration ledger, AI research interface  
**Explicit Status:** Non-proof, non-exhaustive literature review, no guarantee of feasibility for any approach

---

## 0. Why Build the GAP Atlas First

The difficulty of the Riemann Hypothesis (RH) lies not merely in lacking a final trick. It simultaneously suffers from:

- A vast number of mutually equivalent reformulations that do not reduce the burden of proof;
- Local approaches spanning complex analysis, harmonic analysis, operator theory, spectral theory, probability, numerical analysis, and arithmetic geometry;
- Many papers completing only a single local node, relying on voluntary relays for subsequent steps;
- Different approaches employing different function spaces, normalizations, topologies, and quantifiers;
- Frequent conflation of the evidentiary levels of numerical evidence, statistical analogies, and formal proofs;
- The so-called "missing final step" sometimes actually being an entire chain of global controls equivalent to RH.

Individual mathematical papers usually honestly indicate the propositions they have yet to complete; what is truly missing is:

> A unified GAP system across papers and approaches capable of tracking dependencies, circularities, equivalence risks, counterexamples, numerical certificates, and formalization statuses.

Therefore, the goal of this Atlas is not to answer:

$$
\text{Is } RH \text{ true?}
$$

But rather to answer:

$$
\text{On exactly which edge does each research approach halt?}
$$

And:

$$
\text{Does it halt at a local lemma, a globalization problem, or merely a renaming of RH itself?}
$$

---

# 1. Methodological Origins

This Atlas adopts a three-tier methodology:

## 1.1 Result-Induced Intermediate Theorem Generation (RIITG)

Reverse-generating candidate intermediate structures from the target proposition:

$$
P\rightsquigarrow M.
$$

The symbol $\rightsquigarrow$ merely denotes research generation, not logical implication.

## 1.2 Reverse Axiom Backfilling (RAB)

Demoting candidate intermediate propositions to proof obligations, then forward-backfilling from known foundations:

$$
T\Longrightarrow M\Longrightarrow P.
$$

If $T$ depends on $P$, depends on a proposition equivalent to $P$, or directly introduces $M$ as an assumption, the backfilling fails.

## 1.3 KCPE / AMRAL

Establishing a local candidate space under constraints of knowledge, failure records, semantic windows, and computational budgets:

$$
\Omega_t
=
\Omega(P,K_t,F_{<t},W_{\mathrm{sem}},B_t).
$$

Continuous updating of the research state:

$$
S_t\longrightarrow S_{t+1}.
$$

The complete cycle:

$$
\text{Analyze}
\to\text{Generate}
\to\text{Enumerate}
\to\text{Retrieve}
\to\text{Backfill}
\to\text{Compute}
\to\text{Verify}
\to\text{Falsify}
\to\text{Update}.
$$

---

# 2. Formal Definition of a GAP

Given a research dependency graph:

$$
D=(V,E),
$$

where nodes $V$ are definitions, lemmas, theorems, computational certificates, or target propositions; and directed edges:

$$
A\longrightarrow B
$$

indicate that $A$ is claimed to be sufficient to support $B$.

A GAP is not "we temporarily do not understand," but rather the following data:

$$
G=
(
A,B,
\mathcal C,
\mathcal O,
\mathcal D,
\mathcal W,
\mathcal V,
\mathcal S
),
$$

where:

- $A$: The currently known or provisionally accepted starting point;
- $B$: The next node desired to be deduced;
- $\mathcal C$: The gap type;
- $\mathcal O$: The precise proof obligation;
- $\mathcal D$: Dependencies and ancestor nodes;
- $\mathcal W$: Failure witnesses or counterexample interfaces;
- $\mathcal V$: Verification method;
- $\mathcal S$: Current status.

A GAP annotation is only considered complete when "what is missing" is rewritten into a decidable proposition.

---

# 3. Table of GAP Types

| Type | Name | Typical Issue |
|---|---|---|
| `G-DEF` | Definition Gap | Object, operator, function space, or normalization is unfixed |
| `G-DOM` | Domain/Quantifier Gap | Local results applied globally; finite height applied to all zeros |
| `G-INT` | Interface Gap | An index, operator, or statistic lacks a theorem connecting it to RH |
| `G-EQV` | Equivalence Risk | The intermediate proposition is essentially just an equivalent reformulation of RH |
| `G-DEP` | Dependency Gap | The proof chain uses unstated or overly strong external propositions |
| `G-CIR` | Circular Gap | RH or its equivalent propositions appear in the backfilling ancestors |
| `G-UNI` | Uniformity/Globalization Gap | Holds for each fixed parameter, but lacks uniform constants or global control |
| `G-ERR` | Error Gap | Main term is known, but the error cannot be suppressed to the required scale |
| `G-POS` | Positivity Gap | Requires proving non-negativity for an infinite function family or all indices |
| `G-CLS` | Closure/Limit Gap | Properties cannot be transferred from the generating family to the closure or limit |
| `G-SPC` | Spectral Realization Gap | Lacks a true self-adjoint operator, domain, or exact spectral correspondence |
| `G-COR` | Complete Correspondence Gap | Only partial correspondence; lacks a bijection without omissions or extraneous elements |
| `G-INV` | Representation/Invariance Gap | Coordinate effects mistaken for new structures; conclusions depend on arbitrary parameterizations |
| `G-NUM` | Numerical-Infinite Gap | Finite computations or statistical evidence cannot deduce infinite propositions |
| `G-CER` | Certificate Gap | Numerical results lack interval bounds, boundary certificates, or reproducible errors |
| `G-FRM` | Formalization Gap | Lacks libraries, complete Lean definitions, or `sorry`-free proofs |
| `G-LIT` | Literature/Novelty Gap | Proposition may be known, refuted, or miscited |
| `G-SEM` | Semantic Width Gap | Natural language intermediate propositions have too many non-equivalent formalization candidates |

---

# 4. Status, Severity, and Evidence Tags

## 4.1 Status

- `KNOWN`: Externally known theorem;
- `FILLED`: Gap has been non-circularly backfilled;
- `PROVISIONAL`: Candidate backfill exists but is not yet fully audited;
- `OPEN`: Precise gap is known, not yet backfilled;
- `BLOCKED`: Blocked by upstream gaps;
- `EQUIVALENT_RISK`: Highly likely to be merely a reformulation of RH;
- `CIRCULAR`: Circularity discovered;
- `REFUTED`: Proposition has counterexamples or logical errors;
- `NOT_FORMALIZED`: Natural language proof may hold, but lacks formal proof;
- `CERTIFIED_NUMERICAL`: Strict certificates exist within a finite range;
- `EXPERIMENTAL`: Only general numerical or statistical observations exist.

## 4.2 Severity

- `S0`: Document and notation organization;
- `S1`: Local technical gap;
- `S2`: Major bridge, potentially requiring new tools;
- `S3`: Terminal gap, equivalent to RH or bearing almost all of its difficulty.

## 4.3 Minimum Conditions for Completing a GAP

A GAP can only be marked `FILLED` when all the following conditions are met:

1. Domain, quantifiers, and topology are fixed;
2. $A\Rightarrow B$ is explicitly written out;
3. The proof does not use $B$, RH, or equivalent conditions;
4. All external theorems are traceable;
5. Limit exchanges, infinite sums, integrals, and operator domains all have valid conditions;
6. Numerical parts possess error certificates;
7. Falsification agents have found no counterexamples;
8. If formalizable, Lean/other core checkers have no `sorry` and no undeclared axioms.

---

# 5. Master Graph: RH is Not a Single Path

Let the target be:

$$
P_{RH}:
\forall\rho\in Z_{\mathrm{nt}},\quad
\operatorname{Re}(\rho)=\frac12.
$$

The first-round Atlas does not mix all equivalent conditions into a single list, but treats them as distinct "entry functions":

$$
\begin{aligned}
P_{RH}
&\Longleftrightarrow P_{\mathrm{Weil}}\\
&\Longleftrightarrow P_{\mathrm{NB}}\\
&\Longleftrightarrow P_{\mathrm{Li}}\\
&\Longleftrightarrow P_{\mathrm{DBN}}\\
&\Longleftrightarrow P_{\mathrm{Speiser}}\\
&\Longleftrightarrow P_{\mathrm{PrimeError}}\\
&\Longleftarrow P_{\mathrm{Hilbert\text{-}Polya}}.
\end{aligned}
$$

Critical Warning:

> Equivalences provide new operational languages, but do not automatically reduce the difficulty of the proof.

Therefore, the first GAP of every approach is:

$$
\text{Does it generate a local proof burden lower than that of RH?}
$$

---

# 6. Approach W: Weil-Type Positivity and Explicit Formulas

## 6.1 Known Entry

Under an appropriate test function space $\mathcal H$ and normalization, it can be abstractly written as:

$$
RH
\Longleftrightarrow
\forall f\in\mathcal H,\quad Q(f)\geq0.
$$

If RH is false, there exists a negative witness:

$$
\exists w\in\mathcal H,
\quad Q(w)<0.
$$

## 6.2 GAP Registration

### `RH-W-01`: Test Function Space Fixation

- Type: `G-DEF`, `G-DOM`
- Severity: `S1`
- Obligation: Fix $\mathcal H$, Fourier/Mellin normalizations, support, and decay conditions, and prove that the explicit formula used is valid in this space.
- Failure Witness: A candidate $f$ causes the prime side or zero side to diverge, or boundary terms fail to vanish.
- Status: `OPEN`

### `RH-W-02`: Structured Compression of Negative Witnesses

- Type: `G-CLS`, `G-UNI`
- Severity: `S2`
- Obligation: Construct a generating family $\mathcal G$ independent of the positivity definition, such that

$$
Q(w)<0
\Longrightarrow
\exists g\in\operatorname{span}(\mathcal G),
\quad Q(g)<0.
$$

- Risk: If $\mathcal G=\{g:Q(g)\geq0\}$ or the family is chosen using RH, it immediately becomes circular.
- Status: `OPEN`

### `RH-W-03`: Computable Arithmetic Decomposition

- Type: `G-INT`, `G-ERR`
- Severity: `S2`
- Obligation: For $g\in\mathcal G$, establish

$$
Q(g)=L_\infty(g)+\sum_pL_p(g)+R(g),
$$

and provide convergence and unconditional bounds for $R(g)$.
- Status: `OPEN`

### `RH-W-04`: Positivity of the Generating Family

- Type: `G-POS`, `G-EQV`
- Severity: `S3`
- Obligation: Prove via independent local estimates, operator positivity, or compensation mechanisms that

$$
\forall g\in\mathcal G,
\quad Q(g)\geq0.
$$

- Equivalence Risk: If $\mathcal G$ is sufficiently dense, this step may bear almost the entirety of RH.
- Status: `EQUIVALENT_RISK`

### `RH-W-05`: Transmission of Positivity to the Closure

- Type: `G-CLS`
- Severity: `S2`
- Obligation: Fix the formal topology or closed quadratic form structure of $Q$ so that positivity is validly transmitted when $g_n\to f$.
- Warning: Standard lower semi-continuity is

$$
Q(f)\leq\liminf Q(g_n),
$$

which cannot directly deduce $Q(f)\geq0$ from $Q(g_n)\geq0$; it requires continuity, closed quadratic forms, or other correct closure mechanisms.
- Status: `OPEN`

## 6.3 Approach Verdict

The true core of this approach is not "off-axis zeros generate negative witnesses"; this is already contained in the positivity equivalence. The real GAP is:

$$
\text{Arbitrary negative witness}
\to
\text{Controllable generating family}
\to
\text{Decomposable positivity}
\to
\text{Closure transmission}.
$$

---

# 7. Approach NB: Nyman–Beurling / Báez-Duarte Closure Criterion

## 7.1 Known Entry

RH can be equivalently formulated as a specific function belonging to the closed subspace generated by fractional part functions. Báez-Duarte further showed this can be restricted to a smaller generating family with natural number parameters.

Abstractly written as:

$$
RH
\Longleftrightarrow
\chi\in\overline{\operatorname{span}\{\rho_a\}}.
$$

## 7.2 GAP Registration

### `RH-NB-01`: Constructive Approximation Sequence

- Type: `G-CLS`, `G-ERR`
- Severity: `S2`
- Obligation: Explicitly construct $f_N$ such that

$$
\|\chi-f_N\|_{L^2}\longrightarrow0.
$$

- Status: `OPEN`

### `RH-NB-02`: Unconditional Error Decay Rate

- Type: `G-ERR`, `G-UNI`
- Severity: `S3`
- Obligation: Provide an unconditional bound sufficient to drive the distance to zero for all sufficiently large $N$.
- Equivalence Risk: The required approximation rate often reconnects to Möbius sums, zeros, or RH-equivalent estimates.
- Status: `EQUIVALENT_RISK`

### `RH-NB-03`: Coefficient Control

- Type: `G-UNI`
- Severity: `S2`
- Obligation: Control the magnitude, condition number, and cancellation of approximation coefficients to avoid formal approximations with exploding coefficients.
- Status: `OPEN`

### `RH-NB-04`: Finite-Dimensional Optimization to Infinite Closure

- Type: `G-NUM`, `G-CLS`
- Severity: `S2`
- Obligation: Prove that the numerical decay of the finite-dimensional minimum distance is not a finite-sample phenomenon, and can be validly transmitted to $N\to\infty$.
- Status: `OPEN`

## 7.3 Approach Verdict

The "closure criterion" transforms zero localization into an approximation problem, but the terminal gap remains:

$$
\text{Establishing a global, unconditional, and controllable approximation rate}.
$$

---

# 8. Approach LI: Positivity of Li Coefficients

## 8.1 Known Entry

Li's criterion rewrites RH as the global positivity of a sequence of coefficients:

$$
RH
\Longleftrightarrow
\forall n\geq1,
\quad \lambda_n\geq0.
$$

## 8.2 GAP Registration

### `RH-LI-01`: Uniform Positivity Across All Indices

- Type: `G-POS`, `G-UNI`
- Severity: `S3`
- Obligation: Not merely verifying the first $N$ terms, but providing an unconditional lower bound for all $n$.
- Status: `EQUIVALENT_RISK`

### `RH-LI-02`: Main Term–Oscillatory Term Decomposition

- Type: `G-ERR`
- Severity: `S2`
- Obligation: Find

$$
\lambda_n=A_n+E_n,
$$

where $A_n$ is explicitly positive, and unconditionally prove that $|E_n|<A_n$ holds for all required $n$.
- Status: `OPEN`

### `RH-LI-03`: Numerical Positivity Cannot Be Extrapolated

- Type: `G-NUM`
- Severity: `S2`
- Obligation: Any verification for finite $n$ can only be marked `CERTIFIED_NUMERICAL` and cannot be extrapolated globally.
- Status: `OPEN`

### `RH-LI-04`: Formula Contamination Check

- Type: `G-CIR`, `G-DEP`
- Severity: `S2`
- Obligation: Check whether coefficient asymptotics, zero sum rearrangements, or conditionally convergent operations implicitly use RH.
- Status: `OPEN`

---

# 9. Approach HP: Hilbert–Pólya Spectral Realization

## 9.1 Candidate Entry

If there exists a self-adjoint operator $H$ whose spectrum exactly yields the imaginary parts of the non-trivial zeros:

$$
\operatorname{Spec}(H)=\{\gamma:\zeta(\tfrac12+i\gamma)=0\},
$$

then the real spectrum guaranteed by self-adjointness leads to RH.

This is not a known equivalence theorem, but a strong sufficiency framework.

## 9.2 GAP Registration

### `RH-HP-01`: Hilbert Space and Operator Definition

- Type: `G-DEF`, `G-SPC`
- Severity: `S2`
- Obligation: Explicitly provide $\mathcal H$, a dense domain $D(H)$, the action formula, and boundary conditions.
- Status: `OPEN`

### `RH-HP-02`: Self-Adjointness Rather Than Formal Symmetry

- Type: `G-SPC`
- Severity: `S3`
- Obligation: Prove closedness and equality of adjoint domains, or compute deficiency indices and specify a unique self-adjoint extension.
- Failure Mode: Only proving

$$
\langle Hf,g\rangle=\langle f,Hg\rangle
$$

holds on test functions, without addressing the domains.
- Status: `OPEN`

### `RH-HP-03`: Exact Spectral Correspondence

- Type: `G-COR`, `G-INT`
- Severity: `S3`
- Obligation: Simultaneously prove:

1. Every non-trivial zero corresponds to a spectral value;
2. Every spectral value corresponds to a non-trivial zero;
3. Multiplicities match;
4. There is no extraneous spectrum;
5. The correspondence does not rely on first assuming the zeros lie on the critical line.

- Status: `OPEN`

### `RH-HP-04`: Trace Formula and Prime Side

- Type: `G-INT`, `G-ERR`
- Severity: `S2`
- Obligation: Derive a trace formula compatible with the Riemann–Weil explicit formula, and control regularizations and divergent terms.
- Status: `OPEN`

### `RH-HP-05`: Non-Circular Construction

- Type: `G-CIR`
- Severity: `S3`
- Obligation: The operator must not use "a sequence of zeros already on the critical line" as defining data to then deduce RH from the real spectrum.
- Status: `OPEN`

## 9.3 Approach Verdict

The most common false completion in this approach is:

$$
\text{Formal Hamiltonian}
+\text{Numerical spectral similarity}
\not\Rightarrow
\text{Hilbert–Pólya completion}.
$$

The terminal GAP is the simultaneous establishment of self-adjointness and a complete spectral bijection.

---

# 10. Approach DBN: de Bruijn–Newman Heat Flow

## 10.1 Known Entry

There exists a constant $\Lambda$ such that all zeros of $H_t$ are real if and only if $t\geq\Lambda$. It is known that:

$$
RH\Longleftrightarrow\Lambda\leq0,
$$

and Rodgers–Tao proved:

$$
\Lambda\geq0.
$$

Therefore:

$$
RH\Longleftrightarrow\Lambda=0.
$$

## 10.2 GAP Registration

### `RH-DBN-01`: Terminal Upper Bound

- Type: `G-EQV`
- Severity: `S3`
- Obligation: Prove

$$
\Lambda\leq0.
$$

- Status: `EQUIVALENT_RISK`

### `RH-DBN-02`: Local Zero Dynamics to Global Threshold

- Type: `G-UNI`, `G-DOM`
- Severity: `S3`
- Obligation: Elevate finite-height zero tracking, near-collisions, or Lehmer pair information into control over all heights and the entire heat flow.
- Status: `OPEN`

### `RH-DBN-03`: Directionality of Near-Collision Information

- Type: `G-INT`
- Severity: `S2`
- Obligation: Explicitly distinguish which structures can only improve the lower bound of $\Lambda$, and which might provide an upper bound. Mechanisms proving $\Lambda\geq c$ cannot be reversely claimed to prove $\Lambda\leq0$.
- Status: `OPEN`

### `RH-DBN-04`: Finite Computational Certificates

- Type: `G-NUM`, `G-CER`
- Severity: `S2`
- Obligation: Interval arithmetic can prove finite-region zero properties or improve upper bounds, but must indicate the analytic tail bounds required for their global extension.
- Status: `OPEN`

---

# 11. Approach EF: Explicit Formulas and Prime Error Terms

## 11.1 Known Entry

RH is equivalent or tightly equivalent to square-root scale control of several prime-counting errors, for example, the typical form for the Chebyshev function:

$$
\psi(x)=x+O\!\left(x^{1/2}\log^2x\right).
$$

The specific logarithmic power depends on the equivalent version and normalization used.

## 11.2 GAP Registration

### `RH-EF-01`: Square-Root Cancellation

- Type: `G-ERR`, `G-EQV`
- Severity: `S3`
- Obligation: Unconditionally suppress the error to the scale required by RH.
- Status: `EQUIVALENT_RISK`

### `RH-EF-02`: Explicit Formula Truncation

- Type: `G-ERR`, `G-UNI`
- Severity: `S2`
- Obligation: Simultaneously control zero truncation, horizontal level selection, smoothing, and prime-side tail terms, with constants uniform over the required range.
- Status: `OPEN`

### `RH-EF-03`: Average Results to Pointwise Results

- Type: `G-UNI`, `G-DOM`
- Severity: `S2`
- Obligation: Average, almost-everywhere, or density results cannot be directly upgraded to bounds for every $x$.
- Status: `OPEN`

### `RH-EF-04`: Local Prime Data to Global Zero Exclusion

- Type: `G-INT`
- Severity: `S3`
- Obligation: Finite prime tables or finite-interval errors do not exclude off-axis zeros at extremely high altitudes.
- Status: `OPEN`

---

# 12. Approach SP: Speiser Derivative Zero Criterion

## 12.1 Known Entry

Speiser's theorem equivalently links RH to the absence of non-real zeros of $\zeta'(s)$ to the left of the critical line.

## 12.2 GAP Registration

### `RH-SP-01`: Global Critical Point Exclusion

- Type: `G-EQV`, `G-UNI`
- Severity: `S3`
- Obligation: Prove that all non-real zeros of $\zeta'$ in the specified half-plane do not exist.
- Status: `EQUIVALENT_RISK`

### `RH-SP-02`: Local Mapping Geometry to Global Exclusion

- Type: `G-INT`, `G-DOM`
- Severity: `S2`
- Obligation: Establish theorems capable of globally excluding derivative zeros from local conformal mappings, level sets, or numerical phase portraits.
- Status: `OPEN`

### `RH-SP-03`: Multiplicities of Zeros and Critical Points

- Type: `G-DOM`, `G-COR`
- Severity: `S2`
- Obligation: Handle the multiplicity correspondence between multiple zeros, near-multiple zeros, and derivative zeros.
- Status: `OPEN`

---

# 13. Approach RMT: Random Matrices and Zero Statistics

## 13.1 Known Entry

The local statistics of Riemann zeros and the spectral statistics of random matrices exhibit profound consistency; this provides strong heuristics and numerous testable predictions.

## 13.2 GAP Registration

### `RH-RMT-01`: Statistical Laws Do Not Localize Single-Point Real Parts

- Type: `G-INT`
- Severity: `S3`
- Obligation: Establish deterministic theorems moving from zero correlation functions, spacing distributions, or spectral statistics to "no off-axis zeros."
- Status: `OPEN`

### `RH-RMT-02`: Zero-Density Exceptions

- Type: `G-UNI`, `G-DOM`
- Severity: `S3`
- Obligation: Even if almost all zeros obey a certain statistical law, one must exclude zero-density yet infinitely many off-axis exceptions.
- Status: `OPEN`

### `RH-RMT-03`: Exact Model–Arithmetic Correspondence

- Type: `G-COR`, `G-SPC`
- Severity: `S2`
- Obligation: Clarify whether random matrices are limiting statistical models, effective approximations, or the spectrum of a true operator; the three must not be conflated.
- Status: `OPEN`

---

# 14. Approach AD: Adelic / Connes / Semi-Local Trace Formulas

## 14.1 Candidate Entry

Such approaches interpret explicit formulas as trace formulas or absorption spectra, translating Weil positivity into semi-local or non-commutative geometric structures.

## 14.2 GAP Registration

### `RH-AD-01`: Rigorous Definition of Spaces and Traces

- Type: `G-DEF`, `G-SPC`
- Severity: `S2`
- Obligation: Fix the quotient space, action, Hilbert space, regularized trace, and test function classes.
- Status: `OPEN`

### `RH-AD-02`: Semi-Local Positivity to Global Positivity

- Type: `G-POS`, `G-UNI`, `G-CLS`
- Severity: `S3`
- Obligation: Uniformly extend semi-local structures on finite prime sets $S$ to all places, preserving Weil-type positivity.
- Status: `OPEN`

### `RH-AD-03`: Completeness of Missing/Absorption Spectra

- Type: `G-COR`, `G-SPC`
- Severity: `S3`
- Obligation: Prove that all and only the non-trivial zeros appear in the spectral mechanism with correct multiplicities.
- Status: `OPEN`

---

# 15. Approach OD: Observational Frameworks, Parameterized Representations, and Dynamical Projections

This approach stems from the original research intentions retained after cleaning up four old manuscripts. It is not an RH equivalence criterion, but a candidate discovery tool.

## 15.1 GAP Registration

### `RH-OD-01`: Operation Classification

- Type: `G-DEF`, `G-INV`
- Severity: `S1`
- Obligation: Every operation must be classified as a coordinate transformation, representation transformation, function deformation, analytic continuation, or numerical approximation.
- Status: `OPEN`

### `RH-OD-02`: Non-Triviality

- Type: `G-INV`
- Severity: `S2`
- Obligation: Exclude the possibility that the candidate family is merely

$$
F_\theta=F_0\circ T_\theta
$$

a zero pre-image shift caused by $F_\theta=F_0\circ T_\theta$.
- Status: `OPEN`

### `RH-OD-03`: Index–RH Interface

- Type: `G-INT`, `G-EQV`
- Severity: `S3`
- Obligation: For any index $J(\theta)$ of "clarity, regularity, entropy, condition number, or optimal angle," establish an independent theorem:

$$
\mathcal P(J)
\Longrightarrow
\text{Known necessary, sufficient, or equivalent conditions for RH}.
$$

- Status: `OPEN`

### `RH-OD-04`: Reparameterization Invariance

- Type: `G-INV`
- Severity: `S2`
- Obligation: If the optimal point can be shifted by arbitrary parameter relabeling, then the "optimal angle" has no intrinsic meaning. A geometry, measure, or natural parameterization must be specified.
- Status: `OPEN`

### `RH-OD-05`: Data Leakage and Seed Bias

- Type: `G-NUM`, `G-CER`
- Severity: `S1`
- Obligation: Must not use known critical line zeros as seeds and then claim the concentration of outputs on the critical line as a discovery.
- Status: `OPEN`

## 15.2 Approach Verdict

This approach can currently only serve as:

- A candidate invariant generator;
- A numerical condition number comparator;
- A deformation family explorer;
- A tester for counterexamples and coordinate illusions.

Before `RH-OD-03` is backfilled, no optimization results can serve as evidence for RH.

---

# 16. Approach NUM: Finite Height Verification and Rigorous Computation

## 16.1 Known Entry

Interval arithmetic, Turing's method, and zero counting can rigorously verify that all zeros within a finite height lie on the critical line.

## 16.2 GAP Registration

### `RH-NUM-01`: Finite Height to Infinite Height

- Type: `G-NUM`, `G-DOM`
- Severity: `S3`
- Obligation: There is no step that automatically yields global RH merely by "verifying to a higher bound"; a separate analytic tail theorem is required.
- Status: `OPEN`

### `RH-NUM-02`: Boundary Zero-Free Certificates

- Type: `G-CER`
- Severity: `S1`
- Obligation: Argument integrals must prove the absence of zeros on the boundary, providing bounds for integration and rounding errors.
- Status: `OPEN`

### `RH-NUM-03`: High Precision Does Not Equal Rigor

- Type: `G-CER`
- Severity: `S1`
- Obligation: General floating-point `mpmath` results can only be marked `REPRODUCED` or `EXPERIMENTAL`; only interval/ball arithmetic and certificates can be marked `CERTIFIED_NUMERICAL`.
- Status: `OPEN`

---

# 17. Approach FORM: Formal Proof Engineering

Formalization is not a new RH approach, but it serves as a GAP auditing layer.

### `RH-FORM-01`: Definition Library Gap

- Type: `G-FRM`
- Severity: `S1–S2`
- Obligation: Confirm the formalization usability level of zeta, explicit formulas, test function spaces, quadratic forms, and closed operators.
- Status: `OPEN`

### `RH-FORM-02`: Semantic Preservation from Natural Language to Lean

- Type: `G-SEM`, `G-FRM`
- Severity: `S2`
- Obligation: Each candidate bridge must have a unique or finitely-candidiate formalized version to avoid altering the proposition during translation.
- Status: `OPEN`

### `RH-FORM-03`: Unproven Lemma Encapsulation

- Type: `G-CIR`, `G-FRM`
- Severity: `S2`
- Obligation: Forbids writing major GAPs as `theorem` parameters, `axiom`s, or `sorry`s, and then claiming downstream theorems are complete.
- Status: `OPEN`

### `RH-FORM-04`: Dependency Ancestor Audit

- Type: `G-DEP`, `G-CIR`
- Severity: `S2`
- Obligation: Automatically check

$$
RH\notin\operatorname{Anc}(M_i)
$$

and contamination from all equivalent propositions.
- Status: `OPEN`

---

# 18. First-Round Cross-Approach Core GAPs

After compressing the above approaches, what truly recurs are not hundreds of unrelated problems, but seven meta-gaps.

## `META-GAP-1`: Equivalent Reformulations Without Burden Reduction

$$
P\Longleftrightarrow M
$$

does not mean $M$ is easier than $P$. One must weigh:

$$
C(M)<C(P)?
$$

where $C$ may include the maximum local proof burden, function space complexity, global quantifiers, and formalizability.

## `META-GAP-2`: Local Results Cannot Be Globalized

Common form:

$$
\forall T<\infty,\ P(T)
$$

does not automatically deduce:

$$
P(\infty).
$$

## `META-GAP-3`: Averages/Statistics Cannot Exclude Sparse Exceptions

$$
\text{Holds with density one}
\not\Rightarrow
\text{Holds for all}.
$$

## `META-GAP-4`: Positivity Requires Controlling Infinite Families

Weil, Li, trace formulas, and operator approaches ultimately often converge to:

$$
\forall x\in\mathcal X,
\quad Q(x)\geq0.
$$

The problem is not merely computation, but finding generating families, decompositions, and closures that preserve positivity.

## `META-GAP-5`: Spectral Analogies Lack Exact Operators

Between "resembles a spectrum" and "is the complete spectrum of a self-adjoint operator" lies:

- Domain;
- Self-adjointness;
- Spectral type;
- Multiplicity;
- Complete correspondence;
- Trace formula.

## `META-GAP-6`: Numerical Evidence Lacks Analytic Tail Bridges

Finite computations are highly valuable, but their valid conclusions are finite-region certificates, bound improvements, or counterexample searches, not infinite propositions.

## `META-GAP-7`: Intermediate Propositions May Smuggle the Target

The closer a beautiful bridge is to the finish line, the more it needs to be checked:

$$
M\approx RH?
$$

And:

$$
RH\in\operatorname{Anc}(M)?
$$

---

# 19. GAP-Driven Execution Specifications for AMRAL

## 19.1 Select Only One Edge Per Round

Do not issue the command: "Prove RH."

Instead, issue:

> For `RH-W-02`, under a fixed Weil function space, list three candidate generating families not defined by $Q\geq0$, and search for closure failure witnesses for each generating family.

## 19.2 Output Per Round

Each round must produce:

1. Updated GAP records;
2. Added or deleted dependency edges;
3. Candidate backfill lemmas;
4. Counterexamples/failure witnesses;
5. Literature sources;
6. Computational or formal certificates;
7. Circularity and equivalence risks;
8. Minimum task for the next round.

## 19.3 Priority Function

Can use:

$$
\operatorname{Priority}(G)
=
\frac{
I(G)\cdot F(G)\cdot V(G)
}{
C(G)\cdot R(G)
},
$$

where:

- $I(G)$: Impact on the target;
- $F(G)$: Feasibility of being backfilled;
- $V(G)$: Verifiability;
- $C(G)$: Computational/proof cost;
- $R(G)$: Circularity, contamination, and equivalence risks.

This is not an objective mathematical quantity, but a research scheduling tool.

---

# 20. Phase 1 Execution Sequence

## Cycle G0: System Establishment

- Fix the GAP schema;
- Establish JSON/CSV registration;
- Establish unique IDs;
- Forbid propositions without status tags from entering the master graph.

## Cycle G1: Sentence-by-Sentence Mapping of Four Old Manuscripts

Map every surviving claim to:

- Known anchor points;
- `REFUTED`;
- `EXPERIMENTAL`;
- A specific `RH-OD-*` GAP;
- A specific `RH-W-*` GAP.

## Cycle G2: Weil Positivity Approach

Prioritize:

$$
RH\text{-W-01},
RH\text{-W-02},
RH\text{-W-05}.
$$

Reason: These three are suitable for functional analysis, counterexample searches, and formalization, and can first determine whether $B_3$/$B_6$ truly reduce the burden.

## Cycle G3: Nyman–Beurling Control Group

Use the closure and approximation problem as another computable, formalizable generating family experiment to contrast with the closure difficulties of the Weil approach.

## Cycle G4: Hilbert–Pólya Anti-Pseudoproof Template

Establish automated auditing:

- Does it only prove formal symmetry?
- Does it input zeros first?
- Does it lack a spectral bijection?
- Is there extraneous spectrum?
- Is the domain unaddressed?

## Cycle G5: DBN and Numerical Certificates

Categorize all results into:

- Lower bound mechanisms;
- Upper bound mechanisms;
- Finite zero tracking;
- Global tail bounds.

Forbid directional confusion.

---

# 21. Conclusion of This Version

This version has not resolved any RH terminal GAPs, but has completed a necessary research prerequisite:

1. Rewriting "the Riemann Hypothesis has many GAPs" into registrable gap types;
2. Deconstructing ten major entries into precise halting edges;
3. Distinguishing local technical gaps from terminal gaps that are substantially equivalent to RH;
4. Establishing interfaces for RIITG generation, RAB backfilling, KCPE local search, and AMRAL continuous updating;
5. Explicitly stratifying numerical, statistical, and spectral analogies from true theorems;
6. Establishing accumulable failure and dependency records for subsequent AI relays.

The most important judgment is:

> The Riemann Hypothesis does not lack a longer proof manuscript, but rather a dependency graph showing exactly where each approach re-aggregates local difficulties back into RH itself.

From now on, the unit of research is no longer "a candidate proof," but:

$$
\text{An auditable GAP edge}.
$$

---

# References and Methodological Sources

## EveMissLab Methodology

1. Neo.K / Aletheia, "From Transient Axioms to Backfillable Bridges: Result-Induced Intermediate Proposition Reconstruction in the Case of the Riemann Hypothesis," 2026.  
   https://logic.evemisslab.com/p/lm-001356/
2. Neo.K / Aletheia, "Result-Induced Intermediate Theorem Generation and Reverse Axiom Backfilling," 2026.  
   https://logic.evemisslab.com/p/lm-001368/
3. Neo.K / Aletheia, "Autonomous Mathematical Research Agent Cycle: Result-Induced Intermediate Theorem Generation, Reverse Axiom Backfilling, and Knowledge-Conditioned Quasi-Exhaustion," 2026.  
   https://logic.evemisslab.com/p/lm-001369/

## RH and Major Approaches

4. Clay Mathematics Institute, *Riemann Hypothesis*.  
   https://www.claymath.org/millennium/riemann-hypothesis/
5. B. Rodgers and T. Tao, *The De Bruijn–Newman Constant Is Non-Negative*, 2018/2020.  
   https://arxiv.org/abs/1801.05914
6. D. H. J. Polymath, *Effective Approximation of Heat Flow Evolution of the Riemann $\xi$ Function, and a New Upper Bound for the de Bruijn–Newman Constant*, 2019.  
   https://arxiv.org/abs/1904.12438
7. J.-F. Burnol, *The Explicit Formula in Simple Terms*, 1998.  
   https://arxiv.org/abs/math/9810169
8. J.-F. Burnol, *A Note on Nyman's Equivalent Formulation of the Riemann Hypothesis*, 1999.  
   https://arxiv.org/abs/math/9910055
9. L. Báez-Duarte, *A Strengthening of the Nyman–Beurling Criterion for the Riemann Hypothesis*, 2002.  
   https://arxiv.org/abs/math/0202141
10. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, 2004.  
    https://arxiv.org/abs/math/0404394
11. A. Connes, *An Essay on the Riemann Hypothesis*, 2015.  
    https://arxiv.org/abs/1509.05576
12. D. Platt and T. Trudgian, *The Riemann Hypothesis Is True up to $3\cdot10^{12}$*, 2020/2021.  
    https://arxiv.org/abs/2004.09765