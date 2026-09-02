# P/NP Dynamic Four-Layer Closed Framework
## Research Handoff and Subsequent Implementation Recommendations v1.0

- **Project Nature**: Long-term theoretical research / formalization / algorithmic experiment handoff document
- **Current Positioning**: Heuristic Characterization Program; does not claim to have proven $P=NP$ or $P\neq NP$
- **Guiding Concept**: P/NP Dynamic Four-Layer Closed Framework
- **Core Four Layers**:
  - $\mathrm{GCC}$: Global Computational Complexity state
  - $\mathrm{USRT}$: Universal State-Rate Transformation state
  - $\mathrm{USEG}$: Universal Effective Sequence Generation state
  - $\mathrm{GLC}$: Global Lossless Completion state
- **Handoff Objective**: To enable subsequent AIs, researchers, or formalization tools to continuously advance definitions, mathematical derivations, formal proofs, algorithmic implementations, counterexample testing, and barrier mapping without having to second-guess the project's intent.
- **Associated Main Document**: `P_NP_Dynamic_Four_Layer_Closed_Framework_Heuristic_Research_Proposal_v1.0.md`

---

# 0. The Most Important Overarching Principle

This project is currently **not** a paper claiming to have "proven $P=NP$ or $P\neq NP$."

The correct current positioning is:

$$
\boxed{
\text{P/NP Characterization Program}
}
$$

The research objective is:

> To re-project the traditional $P/NP$ problem onto four dimensions: resources, dynamic rate, effective sequence generation, and final lossless completion, and to study the precise logical relationships between these descriptions and standard complexity classes.

Any subsequent AI must avoid taking:

- Heuristic re-descriptions;
- Definitional equivalences;
- Restricted model theorems;
- Experimental observations;
- Local formalization results;

and mistakenly writing them as a complete proof of:

$$
P=NP
$$

or:

$$
P\neq NP
$$

.

---

# 1. Core Structure of the Current Framework

## 1.1 Layer 1: GCC

### Name

$$
\boxed{
\mathrm{GCC}
=
\text{Global Computational Complexity}
}
$$

### Objective

To study the global complexity class of a problem within a family of computational models that are "reasonable, acceptable, and polynomially simulable by one another."

The absolute clock time of a single physical machine should not be used as the GCC.

It is recommended to define an admissible computation-model family:

$$
\mathfrak M_{\mathrm{adm}}
$$

Requiring at least:

1. Finite description;
2. Uniformity;
3. No oracles;
4. No uncomputable advice;
5. No free infinite-precision constants;
6. Polynomial simulation relationships among models.

Candidate form:

$$
\mathrm{GCC}(L)
=
[T_M^L]_{\equiv_{\mathrm{poly}}}.
$$

### Subsequent Tasks

- Strictly define $\mathfrak M_{\mathrm{adm}}$;
- Explicitly specify the equivalence relation;
- Distinguish between deterministic / nondeterministic models;
- Verify whether GCC is merely a machine-invariant re-description of standard $P$;
- Identify the truly non-trivial new content within GCC.

---

## 1.2 Layer 2: USRT

### Name

$$
\boxed{
\mathrm{USRT}
=
\text{Universal State-Rate Transformation}
}
$$

### Objective

To transform the "state completion rate" of NP-type polynomial nondeterministic computation into a deterministic polynomial completion-rate process.

Given an algorithm/machine $A$:

$$
S_A(x,0)
\rightarrow
S_A(x,1)
\rightarrow
\cdots
$$

Define the completion time:

$$
\tau_A(x)
=
\min\{t:S_A(x,t)\in H_L(x)\}.
$$

Worst case:

$$
T_A(n)
=
\max_{|x|\le n}\tau_A(x).
$$

Available completion rate:

$$
R_A(n)
=
\frac{1}{1+T_A(n)}.
$$

### Key Restrictions

"Rate approximation" cannot require:

$$
R_D(n)\approx R_N(n)
$$

to be numerically close.

What should truly be required is:

$$
T_D(n)\in\operatorname{poly}(n)
$$

or that both reside in the same:

$$
\boxed{
\text{polynomial completion-rate cone}.
}
$$

### Correct Quantifier Direction

Priority should be given to studying:

$$
\exists \mathcal U
\;
\forall (N,p)
\;
\exists q_{N,p}\in\operatorname{poly}
\;
\forall x.
$$

Do not inadvertently strengthen this to:

$$
\exists \mathcal U
\exists K
\forall N
\forall x
$$

all using the same fixed exponent $K$.

The latter is generally much stronger than standard $P=NP$.

---

## 1.3 Layer 3: USEG

### Name

$$
\boxed{
\mathrm{USEG}
=
\text{Universal Effective Sequence Generation}
}
$$

### Objective

To study whether the massive number of possible computation sequences in nondeterministic computation can be compressed by a deterministic polynomial process into a single "decision-sufficient" effective sequence.

For an NTM $N$ and input $x$:

$$
\Gamma_N(x)
=
\{\gamma_1,\gamma_2,\ldots\}.
$$

NP acceptance:

$$
x\in L
\iff
\exists\gamma\in\Gamma_N(x):
\operatorname{Accept}(\gamma).
$$

### Absolutely Prohibited Errors

Do not treat:

$$
|\Gamma_N(x)|
$$

itself as a complexity lower bound.

A $P$ problem can be deliberately designed to have exponentially many useless nondeterministic branches.

What should truly be studied is:

$$
\boxed{
\text{effective / decision-relevant sequence cardinality}
}
$$

and the sequence quotient:

$$
\Gamma_N(x)/{\sim_D}.
$$

Candidate effective cardinality:

$$
\kappa_{\mathrm{eff}}(N,x)
=
|\Gamma_N(x)/{\sim_D}|.
$$

But the cost of constructing $\sim_D$ must be accounted for:

$$
T_{\mathrm{construct}}(\sim_D).
$$

Otherwise, a circularity will arise:

> First solving SAT, and then claiming that all paths actually reduce to just two equivalence classes.

### Minimum Legitimate Version of USEG

There must exist a deterministic sequence generator $G_N$:

$$
Z_0,Z_1,\ldots,Z_m
$$

such that:

$$
m\le\operatorname{poly}(n),
$$

$$
|Z_t|\le\operatorname{poly}(n),
$$

$$
Z_{t+1}=F_N(Z_t,x)
$$

can be computed in polynomial time, and:

$$
\operatorname{Dec}(Z_m)=1
\iff
\exists\gamma\in\Gamma_N(x):
\operatorname{Accept}(\gamma).
$$

---

## 1.4 Layer 4: GLC

### Name

$$
\boxed{
\mathrm{GLC}
=
\text{Global Lossless Completion}
}
$$

### Positioning

GLC should not currently be directly juxtaposed with the first three layers as a "fourth equivalent proposition."

A more reasonable positioning:

$$
\boxed{
\text{The first three layers handle polynomial realization; GLC handles the final capping and acceptance.}
}
$$

Framework representation:

$$
\left[
\mathrm{GCC}
\equiv
\mathrm{USRT}
\equiv
\mathrm{USEG}
\right]
\overset{\mathrm{GLC}}{\Longrightarrow}
\text{Closed Exact Computation}.
$$

### GLC's Final Ledger Perspective

This project adopts:

$$
\boxed{
\text{Freedom in process, no freedom in the final ledger.}
}
$$

Midway through, the algorithm may:

- Reroute;
- Rollback;
- Checkpoint;
- Perform representation switching;
- Recompute;
- Perform branch pruning;
- Switch to other legitimate algorithms;
- Temporarily interrupt;
- Resume.

But ultimately, it must satisfy:

$$
\boxed{
\mathcal L_A(x)
\in
\mathcal A_{\mathrm{final}}.
}
$$

Minimum fields of the final ledger:

$$
\mathcal L_A(x)
=
(
\mathrm{Correct},
\mathrm{Complete},
\mathrm{Resource},
\mathrm{Rate},
\mathrm{Sequence},
\mathrm{Loss}
).
$$

Minimum acceptance criteria:

$$
\mathrm{Correct}=1,
$$

$$
\mathrm{Complete}=1,
$$

$$
\mathrm{Resource}\in\mathbf{Poly},
$$

$$
\mathrm{Loss}=0.
$$

### GLC Must Be Divided into Two Versions

#### $\mathrm{GLC}_{std}$

Standard reliable deterministic model.

Essentially close to:

$$
\text{total correctness}
+
\text{polynomial runtime}.
$$

It is very likely just an explicit formulation of standard $P$ semantics.

#### $\mathrm{GLC}_{robust}$

Allows:

- Rollback;
- Rerouting;
- Representation switching;
- Restart;
- Finitely recoverable faults;

while still requiring all admissible runs to complete correctly in the end.

This is a stronger robustness extension than standard $P=NP$.

It is forbidden to claim that:

$$
\mathrm{GLC}_{robust}
$$

and standard:

$$
P=NP
$$

are directly equivalent.

---

# 2. The Most Important Current Research Propositions

Currently, the entire research program can be written as:

$$
\boxed{
\text{Characterize the exact relationships among }
\mathrm{GCC},
\mathrm{USRT},
\mathrm{USEG},
\mathrm{GLC},
P,
NP.
}
$$

Do not attempt to prove the grand equivalence all at once.

It must be broken down into unidirectional arrows.

It is recommended to establish a formal proposition table:

| ID | Proposition | Status |
|---|---|---|
| C1 | $P=NP\Rightarrow \mathrm{GCC}$ | To be proven after strict definition |
| C2 | $\mathrm{GCC}\Rightarrow P=NP$ | To be proven |
| C3 | $P=NP\Rightarrow\mathrm{USRT}$ | High priority |
| C4 | $\mathrm{USRT}\Rightarrow P=NP$ | High priority |
| C5 | $\mathrm{USRT}\Rightarrow\mathrm{USEG}$ | High priority |
| C6 | $\mathrm{USEG}\Rightarrow\mathrm{USRT}$ | May require additional conditions |
| C7 | $\mathrm{USEG}\Rightarrow P=NP$ | High priority |
| C8 | $P=NP\Rightarrow\mathrm{USEG}$ | To be formalized |
| C9 | Relationship between $\mathrm{GLC}_{std}$ and standard total correctness | High priority |
| C10 | Whether $\mathrm{GLC}_{robust}$ is strictly stronger than standard $P=NP$ | Independent research track |

Every arrow must be labeled with:

- Definition-level;
- Standard theorem;
- New theorem;
- Conditional theorem;
- Conjecture;
- False / counterexample.

---

# 3. Recommended Eight Parallel Research Tracks for the Future

---

## Track A: Axiomatization and Definition

### Objective

To transform all terms from colloquial concepts into verifiable mathematical objects.

### Tasks

1. Define admissible computation models;
2. Define state space;
3. Define terminal state;
4. Define semantic preservation;
5. Define completion rate;
6. Define polynomial-rate cone;
7. Define effective sequence;
8. Define decision-sufficient quotient;
9. Define final ledger;
10. Define admissible execution history.

### Completion Criteria

No notation may rely on:

> "Everyone knows what I mean."

All quantifiers must be explicit.

---

## Track B: Equivalence Arrows and Mathematical Derivation

### Objective

To study item by item:

$$
\mathrm{GCC},
\mathrm{USRT},
\mathrm{USEG},
P,
NP
$$

and the implications among them.

### Methodology

Work on only one arrow at a time.

For example:

$$
\mathrm{USRT}\Rightarrow P=NP.
$$

You must write out:

1. Assumptions;
2. Domain;
3. Codomain;
4. Uniformity;
5. Polynomial bound;
6. Correctness;
7. Conclusion;
8. Whether SAT NP-completeness is used;
9. Whether Cook–Levin is used;
10. Whether there is hidden machine dependence.

---

## Track C: Non-Circularity and Admissible Transformations

### Suggested Name

$$
\boxed{
\text{Admissible Transformation Theory}
}
$$

### Objective

To prevent all circularities of "solving for the answer first, then defining the compression."

Prohibited:

- SAT oracles;
- Hidden advice;
- Answer-dependent equivalence relations;
- Infinite precision;
- Free precomputation;
- Nonuniform exponential lookup tables;
- Placing exponential construction costs in preprocessing and leaving them unaccounted for;
- Directly treating the final answer as an abstract state.

### Deliverable

A document:

`Admissible_Transformation_Axioms.md`

This could become one of the most important foundational documents of the entire theory.

---

## Track D: Formal Proofs

### Recommended Tools

Priority:

- Lean 4;
- Coq;
- Isabelle/HOL.

### Do Not Formalize Grand Propositions Initially

First establish a theorem ladder.

Recommended sequence:

1. Polynomial bound algebra;
2. Machine simulation relation;
3. Total deterministic computation;
4. Completion-time definition;
5. Completion-rate equivalence lemma;
6. Polynomial-rate cone;
7. State transformation correctness;
8. Finite computation sequence;
9. Decision-sufficient sequence;
10. USRT $\Rightarrow$ deterministic polynomial solver;
11. USEG $\Rightarrow$ deterministic polynomial solver;
12. Only tackle the three-phase equivalence at the very end.

### Every Theorem

Must have:

- Statement;
- Dependencies;
- Proof status;
- Countermodel status;
- Formal file path;
- Version.

---

## Track E: Algorithmic Implementation and Observatory

### Objective

Not to experimentally prove $P/NP$.

But rather to test:

> Whether the four-layer framework can truly describe different algorithms.

### First Batch of Benchmarks

Recommended:

1. 2-SAT;
2. Horn-SAT;
3. XOR-SAT;
4. Bounded-treewidth SAT;
5. General 3-SAT;
6. Tseitin formulas;
7. Pigeonhole Principle;
8. Planted SAT;
9. Random $k$-SAT.

### Execution Records per Run

$$
\mathcal O
=
(
T,
M,
N_{\mathrm{states}},
N_{\mathrm{branches}},
\kappa_{\mathrm{raw}},
\kappa_{\mathrm{eff}},
N_{\mathrm{switch}},
N_{\mathrm{rollback}},
S_{\mathrm{peak}},
R_{\mathrm{completion}},
\mathrm{final\ ledger}
).
$$

### Recommended Deliverable

Establish:

$$
\boxed{
\text{Dynamic Complexity Observatory}
}
$$

Engineering-wise, a Python MVP can be done first.

---

## Track F: Counterexamples and Destructive Testing

### Objective

To specifically attack our own framework.

For every new definition, attempt to construct:

- Trivialization;
- Oracle smuggling;
- Preprocessing smuggling;
- Nonuniform smuggling;
- Path-cardinality counterexample;
- Precision blow-up;
- Representation blow-up;
- Model dependence;
- Sequence quotient construction blow-up;
- False GLC;
- Robust GLC impossibility under permanent fault.

### Rules

If a counterexample overthrows a definition:

Do not sugarcoat it.

Directly:

1. Save the counterexample;
2. Modify the definition;
3. Update the version;
4. Record the breaking change.

---

## Track G: Model Invariance

### Objective

To confirm which quantities belong to the problem itself, and which are merely machine representations.

Needs classification:

### Potentially Highly Invariant

$$
\text{Polynomial-time class membership}.
$$

### Potentially Not Invariant

$$
\text{local state-change velocity}.
$$

### Potentially Quotient-Invariant

$$
\text{completion-rate polynomial class}.
$$

### Research Question

If:

$$
M_1\equiv_{\mathrm{poly}}M_2,
$$

then:

$$
\mathrm{GCC}_{M_1}(L)
\stackrel{?}{=}
\mathrm{GCC}_{M_2}(L).
$$

And:

$$
R_{M_1}(n)
$$

and:

$$
R_{M_2}(n)
$$

should be compared using what equivalence relation?

---

## Track H: Complexity Barrier Mapping

Any result claiming to approach general P/NP separation/equality must be checked against:

1. Relativization;
2. Natural proofs;
3. Algebrization;
4. Oracle dependence;
5. Restricted-model lower bounds;
6. Proof-system-specific lower bounds;
7. Nonuniformity;
8. Hidden advice;
9. Hidden precision;
10. Hidden compilation.

It is recommended to permanently add to the end of every formal research manuscript:

## Barrier Status

instead of:

## Future Work

---

# 4. Recommendation to Add an Independent Main Track: Complexity Ledger Calculus

This track does not need to wait for $P/NP$ results.

---

## 4.1 Core Objects

Define the computation ledger:

$$
\mathcal L
=
(
C_{\mathrm{correct}},
C_{\mathrm{time}},
C_{\mathrm{space}},
C_{\mathrm{construct}},
C_{\mathrm{repr}},
C_{\mathrm{sequence}},
C_{\mathrm{precision}},
C_{\mathrm{recover}},
C_{\mathrm{loss}}
).
$$

---

## 4.2 Representation Transitions

If:

$$
R_i\rightarrow R_j,
$$

then it corresponds to:

$$
\mathcal T_{ij}:
\mathcal L_i\mapsto\mathcal L_j.
$$

---

## 4.3 Research Questions

Does there exist a composition law:

$$
\mathcal T_{ik}
=
\mathcal T_{jk}\circ\mathcal T_{ij}?
$$

Which costs are:

- Additive;
- Multiplicative;
- Amortizable;
- Commutative;
- Hidden;
- Prone to blow-up;
- Quotientable;
- Incapable of being losslessly compressed.

---

## 4.4 Independent Value

Even if P/NP is ultimately not resolved, this track could form:

- An algorithm-analysis formalism;
- An agent computation ledger;
- A compiler cost calculus;
- Adaptive algorithm analysis;
- Representation-transition theory.

Therefore, it is recommended to establish this as an independent project.

---

# 5. Recommended Research Phases

---

## Phase I: Definition & Consistency

### Goal

Not to prove P/NP.

But to achieve:

$$
\boxed{
\text{Framework self-consistency}
}
$$

### Must Deliver

1. Symbol table;
2. Definitions;
3. Quantifier table;
4. Admissibility axioms;
5. Counterexample suite;
6. GCC model invariance;
7. GLC std/robust split;
8. Three-phase implication map.

### Gate

Phase II can only be entered once Phase I is completed.

---

## Phase II: Characterization Theorems

### Goal

Prove:

$$
A\Rightarrow B
$$

or find:

$$
A\not\Rightarrow B
$$

counterexamples.

### Not Required

It is not required to prove:

$$
P=NP
$$

or:

$$
P\neq NP.
$$

### Success Criteria

Even if we only obtain:

$$
\mathrm{USRT}
\Rightarrow
\mathrm{USEG}
$$

requiring conditions $X, Y, Z$,

it is still a genuine theoretical achievement.

---

## Phase III: Formalization & Experimental Validation

Can be partially parallel with Phase II.

### Formal

Lean/Coq/Isabelle.

### Experimental

Dynamic Complexity Observatory.

---

## Phase IV: P/NP Attack

Only when a theorem has truly crossed from:

$$
\text{characterization}
\rightarrow
\text{complexity consequence}
$$

should this phase be entered.

Only then is it permitted to propose:

$$
P=NP
$$

or:

$$
P\neq NP
$$

candidate proofs.

---

# 6. AI Handoff Standard Operating Procedure

Every succeeding AI should work in the following order.

---

## Step 1: Read

Priority reading:

1. This handoff document;
2. `P_NP_Dynamic_Four_Layer_Closed_Framework_Heuristic_Research_Proposal_v1.0.md`;
3. The latest Definitions;
4. The latest theorem index;
5. The latest counterexample index.

---

## Step 2: Confirm Task Type

First, tag the current task:

- Definition;
- Proof;
- Formalization;
- Counterexample;
- Algorithm;
- Benchmark;
- Literature;
- Barrier check;
- Engineering.

Do not mix different tasks into a single document.

---

## Step 3: Establish Dependencies

Every new result must state:

### Depends on

- Definitions;
- Lemmas;
- Theorems;
- External theorems;
- Assumptions.

---

## Step 4: Tag Result Level

Only use:

- `Definition`
- `Observation`
- `Lemma`
- `Proposition`
- `Theorem`
- `Conditional Theorem`
- `Conjecture`
- `Counterexample`
- `Experimental Result`
- `Open Problem`

Do not write a Conjecture as a Theorem.

---

## Step 5: Conduct Counterexample Testing

For any new proposition, ask at least:

1. Does a trivial P language break it?
2. Does an intentionally branching P machine break it?
3. Does an oracle degenerate the definition?
4. Is nonuniform advice smuggled in?
5. Is exponential preprocessing smuggled in?
6. Does arbitrary machine encoding affect it?
7. Does robust GLC become impossible due to permanent faults?

---

## Step 6: Update Research Graph

Recommended to maintain:

`THEOREM_GRAPH.md`

Format:

```text
GCC
 ├──?→ USRT
 ├──?→ P=NP
USRT
 ├──?→ USEG
 └──?→ P=NP
USEG
 └──?→ P=NP
GLC_std
 └── relation → Total Correctness
GLC_robust
 └── stronger extension
```

Arrow status:

- `✓`
- `✗`
- `?`
- `conditional`

---

## Step 7: Update Failure Records

Establish:

`FAILED_ROUTES.md`

For each failed route, retain:

- Original proposition;
- Why it failed;
- Counterexample;
- Whether it is fixable;
- Errors forbidden from being repeated.

---

# 7. Recommended Project Directory

```text
P_NP_Dynamic_Closure/
│
├── 00_overview/
│   ├── framework_v1.md
│   ├── research_handoff.md
│   └── terminology.md
│
├── 01_definitions/
│   ├── GCC.md
│   ├── USRT.md
│   ├── USEG.md
│   ├── GLC_std.md
│   └── GLC_robust.md
│
├── 02_axioms/
│   └── admissible_transformations.md
│
├── 03_theorems/
│   ├── implication_map.md
│   ├── lemmas/
│   └── conditional_results/
│
├── 04_counterexamples/
│   ├── path_cardinality.md
│   ├── hidden_preprocessing.md
│   ├── oracle_smuggling.md
│   └── robust_glc_faults.md
│
├── 05_formal/
│   ├── lean/
│   ├── coq/
│   └── isabelle/
│
├── 06_algorithms/
│   ├── 2sat/
│   ├── hornsat/
│   ├── xorsat/
│   └── 3sat/
│
├── 07_observatory/
│   ├── metrics.md
│   ├── benchmark_schema.md
│   └── experiments/
│
├── 08_ledger_calculus/
│   ├── ledger_definition.md
│   ├── transformations.md
│   └── composition_rules.md
│
├── 09_barriers/
│   ├── relativization.md
│   ├── natural_proofs.md
│   └── algebrization.md
│
├── 10_failed_routes/
│   └── FAILED_ROUTES.md
│
└── THEOREM_GRAPH.md
```

---

# 8. Next Batch of Recommended Tasks

Sorted by priority.

---

## Priority 0

### Task 0.1

Establish:

`P_NP_Dynamic_Closure_Definitions_v0.1.md`

Only do strict definitions.

Do not do grand proofs.

### Task 0.2

Establish:

`Admissible_Transformation_Axioms_v0.1.md`

Specifically define what constitutes an admissible transformation.

---

## Priority 1

### Task 1.1

Formalize:

$$
\mathrm{USRT}
\Rightarrow
P=NP
$$

candidate proposition.

### Task 1.2

Formalize:

$$
\mathrm{USEG}
\Rightarrow
P=NP
$$

candidate proposition.

### Task 1.3

Check:

$$
P=NP
\Rightarrow
\mathrm{USRT}
$$

exactly what kind of uniform transformation schema is required.

---

## Priority 2

### Task 2.1

Establish:

`Sequence_Cardinality_Counterexamples.md`

Prove that raw path cardinality is insufficient.

### Task 2.2

Define:

$$
\kappa_{\mathrm{eff}}.
$$

And attempt to find:

- Trivial examples;
- Useful examples;
- Circular examples;
- Impossible examples.

---

## Priority 3

### Task 3.1

Establish the Dynamic Complexity Observatory MVP.

First do:

- 2-SAT;
- XOR-SAT;
- 3-SAT.

### Task 3.2

Implement the final ledger.

---

## Priority 4

### Task 4.1

Start the Lean theorem ladder.

The first batch should only handle:

- Polynomial functions;
- Completion time;
- Completion rate;
- Elementary implications.

---

# 9. Research Red Lines

Any subsequent AI must strictly observe these.

### Red Line 1

Do not deduce:

$$
\text{Exponential number of candidates}
$$

directly into:

$$
P\neq NP.
$$

---

### Red Line 2

Do not, because some:

- OBDD;
- Resolution;
- Monotone circuit;
- LP;
- DNNF;

has an exponential lower bound, directly deduce a general lower bound.

---

### Red Line 3

Do not equate:

$$
\text{Finding an algorithm is hard}
$$

with:

$$
\text{The algorithm does not exist}.
$$

---

### Red Line 4

Do not pass off:

$$
\mathrm{GLC}_{robust}
$$

as synonymous with:

$$
P=NP
$$

.

---

### Red Line 5

Do not use answer-dependent abstraction/quotient without recording its construction cost.

---

### Red Line 6

Do not treat a single experimental success as an asymptotic theorem.

---

### Red Line 7

Do not call an AI-generated proof sketch a formal proof.

---

# 10. Recommended Template for Each Research Output

```markdown
# Title

## Status
Definition / Lemma / Conjecture / Experiment / Counterexample

## Scope
In which model does this result hold?

## Definitions Used

## Statement

## Assumptions

## Derivation / Proof

## Resource Accounting

## Uniformity Check

## Non-Circularity Check

## Counterexample Search

## Barrier Status

## Formalization Status

## Experimental Status

## Dependencies

## Open Questions

## Next Handoff Task
```

---

# 11. Long-Term Success Criteria

This project should not take:

$$
P=NP
$$

or:

$$
P\neq NP
$$

as the sole criterion for success.

The tiered success criteria are as follows.

### Level 1

The four-layer definitions are complete and self-consistent.

### Level 2

Obtain non-trivial implications / separations.

### Level 3

Form a formalizable theorem family.

### Level 4

Form an implementable Complexity Ledger / Observatory.

### Level 5

Form a new machine-independent dynamic complexity characterization.

### Level 6

If a theorem is truly sufficient to deduce:

$$
P=NP
$$

or:

$$
P\neq NP,
$$

only then enter formal P/NP proof verification.

---

# 12. Final Handoff Summary

The correct route for the next phase of this project is not:

> "Continuing to debate whether $P=NP$ or $P\neq NP$."

But rather:

$$
\boxed{
\text{Definition}
\rightarrow
\text{Characterization}
\rightarrow
\text{Formalization}
\rightarrow
\text{Experiment}
\rightarrow
\text{Counterexample}
\rightarrow
\text{Barrier Review}
}
$$

Then, depending on the results, deciding whether to enter:

$$
\boxed{
\text{P/NP Attack}.
}
$$

Core research skeleton:

$$
\boxed{
\mathrm{GCC}
\quad
\mathrm{USRT}
\quad
\mathrm{USEG}
\quad
\mathrm{GLC}
}
$$

Core research attitude:

$$
\boxed{
\text{The process can be free; definitions, quantifiers, ledgers, and proofs cannot be free.}
}
$$

Core final principle:

$$
\boxed{
\text{First establish a theory worthy of standing on its own, then ask if it can solve P/NP.}
}
$$