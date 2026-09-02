# P/NP Debate Game Research Area | Round 09

## Searching for SAT's Blossom: Exact Quotient Candidates, Representation Counterattacks, and Quotient Debt

**Round 09: Searching for SAT's Blossom — Exact Quotients, Representation Counterattacks, and Quotient Debt**

- **Lead Researcher:** Neo.K (Hsu Chuan-Wei)
- **Collaborator/Editor:** Aletheia
- **Institution:** EveMissLab (Yiyannuo Technology Co., Ltd.)
- **Date:** August 1, 2026
- **Version:** v1.0
- **Research Status:** Round 09 Dual-Hypothesis Rehearsal
- **Prerequisite Document:** `08_Round_08_Algorithmic_Algebraic_Bridge_Stress_Test_and_Exact_Quotient_Structures.md`
- **Game Attitude:** In this round, the Equality Team earnestly builds weapons first, and then the Inequality Team dismantles them one by one.
- **Document Standard:** All "theorems" hold only within explicitly stated models; anything unproven is uniformly labeled as a conjecture, candidate, or research object.

---

## Abstract

Round 08 extracted a common phenomenon from matching, flow, determinant, shortest path, and treewidth-DP: efficient algorithms often do not process all microscopic candidates one by one, but rather establish some kind of **exact quotient structure**, merging states that have the same effect on the future answer, and retaining only the necessary summaries. From this, the provisional Polynomial Exact Quotient Scheme (PEQS) was proposed.

Round 09 directly pushes this idea to SAT, conducting the "Searching for SAT's Blossom" experiment. We sequentially examine six realistic and mature exact/semi-exact quotient routes: variable elimination, OBDD/DNNF knowledge compilation, XOR/affine extraction, symmetry quotients, backdoor condensation, and CDCL learned-clause compression. The results show that each route can significantly compress the search on specific structures, but each also has identifiable explosion parameters, such as elimination fill-in, representation width, nonlinear residual cores, symmetry-breaking costs, backdoor size, proof system strength, and learned-clause growth.

The most important counterexample in this round comes from OBDDs: there exist functions that are inherently computable in polynomial time, such as the output bits of integer division, whose OBDDs still require exponential size under any variable ordering. This proves that "a certain exact quotient representation inevitably explodes" not only fails to prove $P\neq NP$, but it cannot even deduce that "the function is not in $P$." There is no such direct one-to-one correspondence between representation size and algorithmic time.

Therefore, this round no longer seeks a single "magic representation," but proposes a new research object: **Quotient Debt**. If any exact quotient reduces online search, it may transfer the cost to compilation time, summary size, boundary width, exceptional variables, algebraic residuals, proof length, or answer lifting. Quotient debt is not a proven conservation law, but a resource ledger used to uniformly compare different SAT compression methods.

Finally, this round poses the next question: does there exist a family of SAT instances that **simultaneously lacks low-cost escape channels** across multiple known quotient structures? If it exists, we can study the "Multi-Anti-Structure Core" (MASC); if it does not exist, the Equality Team might use a multi-representation portfolio to peel away all difficulties layer by layer.

---

# I. Last Round's Results: What Exactly is Exact Quotienting?

Round 08 observed:

$$
\text{matching}
\rightarrow
\text{blossom contraction},
$$

$$
\text{max-flow}
\rightarrow
\text{residual-network summary},
$$

$$
\text{determinant}
\rightarrow
\text{elimination},
$$

$$
\text{shortest path}
\rightarrow
\text{semiring aggregation},
$$

$$
\text{bounded-treewidth DP}
\rightarrow
\text{separator state quotient}.
$$

Their common form is:

$$
\Omega
\xrightarrow{\sim}
\Omega/\!\sim
\xrightarrow{\text{exact evaluation}}
\{0,1\}\text{ or optimal value}.
$$

Where $\Omega$ is the massive microscopic candidate space, and the equivalence relation $\sim$ only merges those states that "have the same effect on the remaining computation."

If SAT also possesses a local-global contraction similar to blossoms, the following might occur:

$$
2^n\text{ assignments}
\longrightarrow
\operatorname{poly}(n)\text{ equivalent summaries}
\longrightarrow
\text{exact SAT/UNSAT decision}.
$$

The task of this round is not to assume this structure exists, but to examine existing SAT technologies one by one: are they already local versions of the SAT Blossom?

---

# II. Equality Team's Weapon 1: Variable Elimination

Consider a CNF formula $F$ and a variable $x$. By performing resolution on clauses containing $x$ and clauses containing $\neg x$ to generate resolvents, and then deleting all original clauses containing $x$, we can obtain an elimination result that is equivalent to the original formula in terms of satisfiability.

Written abstractly:

$$
F
\xrightarrow{\operatorname{elim}(x)}
F',
$$

And:

$$
F\text{ is satisfiable}
\iff
F'\text{ is satisfiable}.
$$

This is a very direct exact quotient: the two possibilities for variable $x$ no longer exist explicitly, but are projected into new clause relationships.

Bounded variable elimination in SAT preprocessing is indeed an important practical technique; the work of Eén and Biere demonstrates that variable/clause elimination combined with methods like subsumption can significantly shrink many industrial SAT instances and improve solving time.

## 2.1 The Equality Team's Ideal Scenario

If there exists a variable ordering:

$$
\pi=(x_{\pi(1)},\ldots,x_{\pi(n)}),
$$

Such that the formula size after each elimination remains:

$$
|F_i|\leq\operatorname{poly}(n),
$$

Then:

$$
F_0\to F_1\to\cdots\to F_n\in\{\top,\bot\}
$$

This could form a direct polynomial solving route.

## 2.2 Inequality Team's Counterattack: Fill-in and Induced Width

Elimination does not erase dependencies out of thin air; it may transform originally scattered local dependencies into larger new constraints. Graph-theoretically, this is closely related to the fill-in and treewidth/induced width generated by the elimination ordering.

Therefore, the true cost is not "how many steps it takes to eliminate a variable," but rather:

$$
\operatorname{Debt}_{\mathrm{elim}}
=
\max_i |F_i|
$$

Or more structurally characterized by the elimination width.

If the width $w$ is small, dynamic programming/elimination can indeed solve the problem in time roughly exponential in $w$ and polynomial in the input size; if $w$ grows with $n$, this route may explode.

**Round Verdict:** Variable elimination is a true local version of the SAT Blossom, but its escape conditions are controlled by the elimination width, and it is not yet a general polynomial compressor.

---

# III. Equality Team's Weapon 2: OBDD/DNNF Knowledge Compilation

The second strategy is closer to the original inspiration of the video: first compile the formula into a mathematical/graphical object that can be evaluated directly.

Let:

$$
\operatorname{Compile}(F)=R_F.
$$

If $R_F$ is a structure like OBDD, DNNF, or d-DNNF, many queries can be completed quickly after compilation.

Ideal scenario:

$$
T_{\mathrm{compile}}(F)\in\operatorname{poly}(n),
$$

$$
|R_F|\in\operatorname{poly}(n),
$$

$$
T_{\mathrm{query}}(R_F)\in\operatorname{poly}(n).
$$

Then SAT is truly "functionalized."

## 3.1 Inequality Team's Counterattack: Representation Size Will Explode

OBDDs and structured DNNFs are known to have strong size lower bounds. This indicates that exact knowledge compilation for certain Boolean functions cannot maintain a small size within these representation families.

But here emerges the most important counterattack of this round.

### Counterattack: Functions in P Can Also Have Exponential OBDDs

Existing results show that for certain output bit functions of integer division, their OBDDs require exponential size under any variable ordering.

However, integer division itself can obviously be computed in polynomial time.

Therefore:

$$
\boxed{
\text{OBDD size}=2^{\Omega(n)}
\not\Rightarrow
f\notin P
}
$$

Even:

$$
\boxed{
\text{all orderings explode}
\not\Rightarrow
\text{no other polynomial algorithm exists}
}
$$

This is a very important warning for the Inequality Team: a bridge must be separately established between representation lower bounds and time lower bounds; they cannot be directly conflated.

**Round Verdict:** Knowledge Compilation is one of the SAT Blossom candidates closest to "construct first, evaluate directly later," but the size lower bound of any specific compilation language cannot be directly elevated to $P\neq NP$.

---

# IV. Equality Team's Weapon 3: XOR/Affine Extraction

Many CNF instances may hide parity relationships:

$$
x_1\oplus x_2\oplus\cdots\oplus x_k=b.
$$

If they can be extracted into an $\mathbb F_2$ linear system:

$$
Ax=b,
$$

Then polynomial-time reasoning can be performed using Gaussian/Gauss-Jordan elimination.

Modern SAT research already includes DPLL(XOR)-type methods that combine clause learning with complete parity reasoning; cryptographic SAT also shows that preserving ANF/XOR structures is sometimes more effective than flattening everything back into ordinary CNF.

## 4.1 Equality Team's Claim

General SAT might just be a mixture of multiple implicit algebraic structures:

$$
F
=
F_{\mathrm{affine}}
\wedge
F_{\mathrm{Horn}}
\wedge
F_{\mathrm{2SAT}}
\wedge
F_{\mathrm{residual}}.
$$

If tractable structures are extracted every time, the remaining core might gradually shrink.

## 4.2 Inequality Team's Counterattack

Affine extraction can only solve the parts that genuinely possess an affine closure. Mixing CNF + XOR does not automatically enter $P$ because of this; the true difficulty may be concentrated in:

$$
F_{\mathrm{residual}}.
$$

Therefore:

$$
\operatorname{Debt}_{\mathrm{affine}}
=
|F_{\mathrm{nonlinear\ residual}}|.
$$

**Round Verdict:** A representation revolution can pierce through false difficulties caused by incorrect coordinate systems, but the remaining nonlinear core may still preserve the true difficulty.

---

# V. Equality Team's Weapon 4: Symmetry Quotient

If two sets of assignments are equivalent under the problem's symmetry group $G$:

$$
a\sim b
\iff
\exists g\in G,
\quad
b=g(a),
$$

Then searching all orbit members is a waste.

The search space can be reduced to:

$$
\{0,1\}^n/G.
$$

Classic work on symmetry-breaking predicates shows that adding appropriate symmetry-breaking conditions in many search problems can significantly reduce redundancy; however, in general cases, complete symmetry breaking itself may be difficult to generate, and only partial predicates can be used.

Therefore:

$$
\operatorname{Debt}_{\mathrm{sym}}
=
T_{\mathrm{detect}}
+
T_{\mathrm{break}}
+
|\{0,1\}^n/G|.
$$

If the formula has almost no useful symmetry:

$$
|G|\approx1,
$$

This quotient yields almost no benefit.

**Round Verdict:** Symmetry quotient is a real and elegant candidate for compression, but it only eliminates "repetition" and cannot guarantee the elimination of "fundamentally different candidates."

---

# VI. Equality Team's Weapon 5: Backdoor Condensation

Let $B$ be a set of variables such that for every assignment $\beta$ to $B$, the remaining formula falls into some tractable class $\mathcal C$:

$$
F\! estriction_\beta\in\mathcal C.
$$

Then:

$$
\operatorname{SAT}(F)
=
\bigvee_{\beta\in\{0,1\}^{B}}
\operatorname{SAT}(F\!\restriction_\beta).
$$

If:

$$
|B|=O(\log n),
$$

Then even if all backdoor assignments are enumerated:

$$
2^{|B|}=\operatorname{poly}(n).
$$

This is almost like a "small control surface" for SAT: as long as a small number of key variables are determined first, the rest entirely falls into an easy world.

Backdoor research indeed formalizes the concept in SAT/CSP that "a small number of key variables control the overall difficulty," and studies the parameterized complexity of backdoor detection under different base classes.

## 6.1 Inequality Team's Counterattack

The problem has two layers:

1. Does a small backdoor exist?
2. Even if it exists, can it be found at a low cost?

The total cost is at least:

$$
\operatorname{Debt}_{\mathrm{backdoor}}
=
T_{\mathrm{detect}}(B)
+2^{|B|}\operatorname{poly}(n).
$$

If the minimum backdoor is:

$$
|B|=\Theta(n),
$$

Then this route remains exponential.

**Round Verdict:** Backdoor is the clearest model of "difficulty concentrated into a few degrees of freedom," but it inherently transforms the problem into: does general SAT always have a polylog-size, polytime-detectable backdoor? Currently, there is no such result.

---

# VII. Equality Team's Weapon 6: CDCL Learned-Clause Compression

Modern CDCL solvers do not just search; they learn new clauses from conflicts:

$$
\text{conflict history}
\longrightarrow
\text{learned clause}
\longrightarrow
\text{massive future branches are simultaneously excluded}.
$$

This perfectly aligns with "exact quotienting": a learned clause can represent a massive number of microscopic paths that have been proven invalid.

It can be temporarily written as:

$$
H_t
\xrightarrow{\operatorname{learn}}
C_t,
$$

Where $H_t$ is the massive conflict history, and $C_t$ is a shorter, reusable summary.

CDCL has a profound relationship with resolution proof complexity; modern research is still exploring how to compress learned clauses. Work at the 2026 SAT Conference even directly studies learned-clause factoring, showing that "how to re-compress learned information" itself remains an active technical problem.

## 7.1 Inequality Team's Counterattack: Proof-System Debt

If a certain class of UNSAT formulas requires exponential proofs in resolution, then any solving process restricted to the corresponding proof capability may encounter massive learned-clause/conflict history costs.

But this is still not a general lower bound, because:

$$
\text{resolution hard}
\not\Rightarrow
\text{all proof systems hard}.
$$

Moreover, existing work demonstrates that after switching to MaxSAT/stronger reasoning frameworks, certain formulas that are hard for resolution/CDCL can be quickly processed by different forms of reasoning.

Therefore:

$$
\operatorname{Debt}_{\mathrm{proof}}
=
\text{minimum proof resources in the chosen proof system}.
$$

**Round Verdict:** Clause learning is a practical paradigm of "using history to create future quotients," but any resolution-based lower bound has a proof-system escape.

---

# VIII. SAT Blossom Candidate Matrix

| Quotient Method | What is Quotiented Out | Exactness | Success Parameter | Main Explosion Point | General SAT Blossom? |
|---|---|---:|---|---|---|
| Variable Elimination | Branches of eliminated variables | Yes | Small elimination width | fill-in / resolvents | No |
| OBDD / DNNF | Equivalent subfunctions | Yes | Small representation width/size | compiled size | No |
| XOR / Affine | Parity relationships | Yes | Strong affine structure | nonlinear residual | No |
| Symmetry Quotient | Symmetry orbits | Yes | Large symmetry group | detection / orbit count | No |
| Backdoor | Exceptional degrees of freedom | Yes | Small backdoor | detection + $2^k$ | No |
| CDCL Learning | Conflict history | Yes | Short proof / reusable clauses | proof length / clause database | No |

Currently, no single candidate can cover general SAT alone.

But they are not mutually repetitive either. They compress different types of redundancies:

$$
\text{variable redundancy},
\text{function redundancy},
\text{algebraic redundancy},
\text{symmetry redundancy},
\text{exceptional degrees of freedom},
\text{history redundancy}.
$$

This gives the Equality Team a new idea:

> Perhaps the SAT Blossom is not a single contraction, but an adaptive quotient portfolio.

---

# IX. Equality Team Upgrade: Hybrid Quotient Portfolio

Let the quotient operators be:

$$
\mathcal Q
=
\{Q_{\mathrm{elim}},Q_{\mathrm{KC}},Q_{\mathrm{xor}},Q_{\mathrm{sym}},Q_{\mathrm{bd}},Q_{\mathrm{learn}},\ldots\}.
$$

Establish an orchestrator:

$$
\operatorname{ORCH}(F_t)
\rightarrow
Q_i,
$$

At each step, choose the most suitable quotienting based on the current formula:

$$
F_{t+1}=Q_i(F_t).
$$

The ideal scenario is that there exists some potential function:

$$
\Phi(F_t)
$$

Such that each quotienting guarantees:

$$
\Phi(F_{t+1})<\Phi(F_t),
$$

And after a polynomial number of steps:

$$
F_T\in\mathcal C_{\mathrm{easy}}.
$$

If the construction and intermediate representations at each step maintain polynomial bounds, this would be a genuine $P=NP$ candidate mechanism.

This is closer to practical algorithmic engineering than "there must exist a magic function": use different weapons for different structures.

---

# X. Inequality Team's New Claim: Quotient Debt

Facing a hybrid portfolio, the Inequality Team can no longer just prove that one of the methods will explode.

Therefore, a new resource ledger is proposed:

$$
\boxed{
\mathbf D_Q(F)
=
(D_{\mathrm{build}},
D_{\mathrm{size}},
D_{\mathrm{width}},
D_{\mathrm{residual}},
D_{\mathrm{detect}},
D_{\mathrm{proof}},
D_{\mathrm{lift}})
}
$$

Where:

- $D_{\mathrm{build}}$: Cost of building the quotient structure;
- $D_{\mathrm{size}}$: Size of the summary/compiled representation;
- $D_{\mathrm{width}}$: Boundary, elimination, or decomposition width;
- $D_{\mathrm{residual}}$: The hard core that has not been quotiented out;
- $D_{\mathrm{detect}}$: Cost of detecting symmetry/backdoors/structures;
- $D_{\mathrm{proof}}$: Proof resources accumulated to prove UNSAT;
- $D_{\mathrm{lift}}$: Cost of recovering the original problem's answer/witness from the quotiented result.

This is called:

$$
\boxed{\text{Quotient Debt}}
$$

But it must be immediately stated:

> Quotient debt is currently not a conservation law, nor is it proven that it must be superpolynomial. It is merely a unified ledger for comparing cost transfers across methods.

What the Inequality Team truly needs to prove is some kind of non-circular lower bound, for example:

$$
\forall\text{ admissible quotient pipelines }\Pi,
\quad
\max_t \|\mathbf D_Q(F_t)\|
\geq
n^{\omega(1)}
$$

Holds for some explicit family of SAT instances.

Currently, there is absolutely no such general theorem.

---

# XI. The Most Important Counterexample of This Round: Representation Explosion Does Not Equal Computational Explosion

This point is worth recording independently, as it will prevent many false proofs in the future.

Suppose a Boolean function $f_n$ satisfies the following for a representation family $\mathcal R$:

$$
\forall R\in\mathcal R(f_n),
\quad
|R|\geq2^{\Omega(n)}.
$$

It cannot be deduced that:

$$
f_n\notin P.
$$

The OBDD lower bound for integer division is a concrete counterexample: a function can have a polynomial-time algorithm, yet lack a small OBDD.

Therefore, if any future "cross-representation invariant" is to truly touch upon $P/NP$, it must establish the additional bridge:

$$
\boxed{
\text{representation/structure lower bound}
\Longrightarrow
\text{general uniform time lower bound}
}
$$

This bridge itself might be more difficult to find than some elegant lower bound.

---

# XII. Reinterpretation of the Video Inspiration in Round 09

The original video demonstrated:

$$
\text{multiple conditional branches}
\rightarrow
\text{a mathematical function}
\rightarrow
\text{direct evaluation}.
$$

The results of Round 09 do not negate this possibility, but rather make it precise:

$$
\text{SAT's condition space}
\rightarrow
\text{some quotient representation}
\rightarrow
\text{fast decision}
$$

It is entirely possible for this to happen on **specific structures**, and modern SAT technologies perform local versions of this every day.

What is truly unknown is:

$$
\boxed{
\text{whether there exists a uniform, polynomial, exact quotient portfolio,}
}
$$

$$
\boxed{
\text{that can keep the quotient debt within polynomial bounds for all SAT instances?}
}
$$

This is actually very close to the strongest constructive version of the $P=NP$ side in this series so far.

The opposing side, on the other hand, must prove:

$$
\boxed{
\text{there exists a family of SAT instances such that all admissible quotient portfolios}
}
$$

$$
\boxed{
\text{explode superpolynomially in at least one quotient debt dimension.}
}
$$

---

# XIII. Next Round: Multi-Anti-Structure Core

Round 10 will no longer ask one by one "does this method have a hard example," but will instead change to:

> Can we find or construct a family of formulas that simultaneously invalidates multiple known low-cost escape channels?

For example, hoping that the same formula family simultaneously possesses:

$$
\text{high elimination/treewidth},
$$

$$
\text{no small backdoor},
$$

$$
\text{little useful symmetry},
$$

$$
\text{large OBDD / compilation size},
$$

$$
\text{weak affine extractability},
$$

$$
\text{long proofs in selected proof systems}.
$$

Provisionally called:

$$
\boxed{\text{MASC = Multi-Anti-Structure Core}}
$$

Or "Multi-Anti-Structure Core."

## Equality Team's Task for the Next Round

Prove that even if the above conditions hold simultaneously, there may still be unlisted new representation escapes; it is best to use a function/problem that is already in $P$ as a counterexample to demonstrate that "multiple representation hardnesses still do not equal time hardness."

## Inequality Team's Task for the Next Round

Find explicit SAT/CSP families that simultaneously have large lower bounds across multiple known quotient measures, and investigate whether these large lower bounds stem from a common cause rather than accidental superposition.

---

# XIV. Erroneous Routes Eliminated in This Round

1. "Variable elimination explodes, therefore $P\neq NP$." — This only restricts elimination-type methods.
2. "OBDDs for all variable orderings are exponentially large, therefore it is not in $P$." — Defeated by the direct counterexample of integer division.
3. "XOR is easy to solve, so general SAT might also be linearized." — This only holds for affine structures.
4. "Quotienting out all symmetries will make it polynomial." — General formulas may not have enough symmetry, and complete breaking also has a cost.
5. "All SAT instances have small backdoors, we just haven't found them yet." — There are no universal results to support this.
6. "CDCL is already very strong, so learned clauses will converge to a polynomial." — Limited by proof-system complexity, and there is no general guarantee.
7. "Mixing the six methods will definitely cover all formulas." — The complete low-cost nature of the portfolio is exactly the problem to be proven.
8. "Quotient debt must be conserved." — Currently just a research conjecture; there is no conservation theorem yet.

---

# XV. Round Verdict

## Equality Team's Score

The Equality Team successfully proved:

- SAT already has a large number of real, exact local quotient techniques;
- Different techniques handle different structures;
- Exponential lower bounds for specific representations cannot rule out other polynomial algorithms;
- A hybrid quotient portfolio remains a logically open $P=NP$ route.

## Inequality Team's Score

The Inequality Team successfully proved:

- Every known quotient has explicit structural parameters and explosion points;
- Compressing the search often just shifts the cost to compilation, width, residual, detection, or proof;
- To prove $P=NP$, one cannot just show one or two classes of formulas being quotiented, but must handle all worst-case SAT instances.

Game score for this round:

$$
P=NP:8
\qquad
P\neq NP:8.
$$

The score is merely a research game interface and does not constitute any mathematical evidence.

---

# XVI. External Theoretical References

1. Niklas Eén and Armin Biere, **Effective Preprocessing in SAT Through Variable and Clause Elimination**, SAT 2005.
   - Used for SAT variable/clause elimination and practical preprocessing.
2. Jan Krajíček, **An exponential lower bound for a constraint propagation proof system based on ordered binary decision diagrams**.
   - Used for exponential lower bounds of OBDD-based proof systems.
3. Takashi Horiyama and Shuzo Yajima, **Exponential Lower Bounds on the Size of Variants of OBDD Representing Integer Division**, 1998.
   - Key counterexample: P-time functions can still require exponential size under all OBDD orderings.
4. Thammanit Pipatsrisawat and Adnan Darwiche, **A Lower Bound on the Size of Decomposable Negation Normal Form**, AAAI 2010.
   - Used for representation lower bounds of structured DNNF/OBDD types.
5. Tero Laitinen, Tommi Junttila, Ilkka Niemelä, **Extending Clause Learning SAT Solvers with Complete Parity Reasoning**, 2012.
   - Used for DPLL(XOR) and incremental Gauss-Jordan parity reasoning.
6. James Crawford, Matthew Ginsberg, Eugene Luks, Amitabha Roy, **Symmetry-Breaking Predicates for Search Problems**, KR 1996.
   - Used for SAT/search symmetry quotients and symmetry-breaking predicates.
7. Serge Gaspers et al., **Backdoors into Heterogeneous Classes of SAT and CSP**, AAAI 2014; and Gaspers & Szeider, **Backdoors to satisfaction continued**, 2026 survey.
   - Used for backdoor condensation and parameterized complexity.
8. Florian Pollitt et al., **Factoring Learned Clauses**, SAT 2026.
   - Used for the latest examples of modern CDCL learned-clause compression.
9. Alexey Ignatiev, Antonio Morgado, João Marques-Silva, **On Tackling the Limits of Resolution in SAT Solving**, 2017.
   - Used for the representation/proof-system escape that "resolution/CDCL hard does not equal hard for all reasoning frameworks."

---

## One-Sentence Conclusion for Round 09

$$
\boxed{
\text{We have found many "local Blossoms" for SAT, but we have not yet found the SAT Blossom.}
}
$$

More precisely:

$$
\boxed{
\text{The true point of contention is no longer whether it can be compressed, but whether for all instances,}
}
$$

$$
\boxed{
\text{the correct exact quotient can be consistently found at a uniform polynomial cost.}
}
$$