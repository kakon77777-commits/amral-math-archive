# Dynamic Four-Layer Closure Framework for P/NP: A Heuristic Reformulation via Global Complexity, State-Rate Transformation, Effective Sequence Generation, and Lossless Completion

**Dynamic Four-Layer Closure Framework for P/NP: A Heuristic Reformulation via Global Complexity, State-Rate Transformation, Effective Sequence Generation, and Lossless Completion**

**Author: Neo.K (Chuan-Wei Hsu)**  
**Collaborator/Editor: Aletheia**  
**Institution: EveMissLab (Yiyannuo Technology Co., Ltd.)**  
**Date: 2026-08-02**  
**Version: v1.0**  
**Document Nature: Conceptual Paper / Heuristic Research Program; Not a Proof of P vs. NP**

---

## Abstract

The standard P vs. NP problem asks whether every language accepted by a nondeterministic polynomial-time algorithm can also be accepted by a deterministic polynomial-time algorithm. This paper does not attempt to prove \(P=NP\) or \(P\neq NP\). Instead, it proposes a four-layer closure framework compatible with the existing "dynamic rate" research line, re-projecting the traditional P/NP problem onto four interrelated observational planes with distinct conceptual functions: **Global Computational Complexity State (GCC)**, **Universal State-Rate Transformation State (USRT)**, **Universal Effective Sequence Generation State (USEG)**, and, as the capstone acceptance condition, **Global Lossless Completion State (GLC)**.

The fundamental position of this paper is that, when restricted to "admissible computational models" that share polynomial simulation relationships, the traditional polynomial-time classification can be viewed as a cross-model complexity equivalence class. This same classification can be rewritten in terms of whether the state completion rate can be transformed from nondeterministic polynomial dynamics to deterministic polynomial dynamics. Furthermore, whether the massive number of candidate sequences in nondeterministic computation can be compressed into a single decision-sufficient, deterministically polynomial-generated effective sequence serves as the third observational plane. Therefore, this paper proposes a heuristic three-phase equivalence program:

\[
\mathrm{GCC}\;\Longleftrightarrow\;\mathrm{USRT}\;\Longleftrightarrow\;\mathrm{USEG},
\]

and argues that, upon proper formalization, these three should establish an equivalence relationship with the standard \(P=NP\) proposition.

The fourth layer, GLC, is not merely a fourth parallel equivalent quantity, but a "final ledger" style closure condition: the computational process may be paused, rewritten, switch representations, rolled back, or rerouted, provided that all execution histories included in the admissible set ultimately deliver results that are correct, complete, have zero semantic loss, and meet resource ledger specifications. In standard reliable deterministic computational models, this weak version of GLC is essentially subsumed under the total correctness requirement of polynomial-time decision algorithms; if we further require convergence under valid rerouting, restarts, or finitely recoverable faults, we obtain a robust GLC extension that is stronger than the traditional \(P=NP\).

The purpose of this paper is to propose a dynamic coordinate system for subsequent formal proofs, counterexample constructions, algorithm designs, and complexity invariant research, rather than to declare P vs. NP solved.

**Keywords:** P vs. NP, dynamic rate, global computational complexity, state completion rate, nondeterministic computation, effective sequence generation, lossless completion, computational model invariance, heuristic framework

---

## 1. Problem Background and Research Positioning

The standard form of P vs. NP can be stated as: whether every language accepted by some nondeterministic polynomial-time algorithm can also be accepted by some deterministic polynomial-time algorithm. Equivalently, NP can also be defined via a polynomial-time verifier and a polynomial-length certificate [1].

This paper accepts the above standard definitions and does not modify the traditional meanings of P, NP, NP-complete, or polynomial-time reduction. What this paper truly changes is the **observational coordinates**.

Traditional formulations primarily focus on:

\[
T_A(n)\in \operatorname{poly}(n)?
\]

This paper, instead, poses four questions:

1. If unreasonable computational shortcuts are excluded, do different admissible computational models fall into the same polynomial complexity equivalence class?
2. Can a nondeterministic polynomial completion process be universally transformed into a deterministic polynomial completion rate?
3. Can a massive number of possible nondeterministic computational sequences be compressed into a single decision-sufficient deterministic effective sequence?
4. Regardless of how the intermediate valid processes vary, can they all ultimately deliver the same correct, complete, lossless, and resource-qualified result?

Therefore, this paper does not attempt to replace P/NP with new terminology, but rather hopes to establish:

\[
\text{Standard Complexity Classification}
\longleftrightarrow
\text{Dynamic State Description}
\longleftrightarrow
\text{Sequence Generation Description}
\longrightarrow
\text{Final Closure Acceptance}.
\]

---

## 2. Model Boundaries: Not "Any Computable Machine", but a Family of Admissible Computational Models

Merely requiring two machines to possess Turing-complete capabilities does not imply they have the same time complexity. The reason traditional complexity theory can treat P as having fairly robust cross-model significance is that common "admissible" computational models can typically simulate each other with polynomial overhead; this is precisely one of the viewpoints of the invariance thesis / Cobham–Edmonds thesis in computational complexity [2,3].

Thus, this paper defines a family of admissible models:

\[
\mathfrak M_{\mathrm{adm}}.
\]

where each model should in principle satisfy:

- Finitely describable;
- Uniform;
- Does not pre-embed problem answers;
- Does not use unaccounted infinite-precision constants;
- Does not contain oracle-style external answer sources;
- Does not contain unaccounted super-polynomial advice;
- Possesses efficient simulations with polynomial overhead relative to other models in the family.

If \(M_i,M_j\in\mathfrak M_{\mathrm{adm}}\), let

\[
M_i\equiv_{\mathrm{poly}}M_j
\]

denote that the two can simulate each other with polynomial overhead.

All uses of the term "global" in this paper are, in principle, restricted within \(\mathfrak M_{\mathrm{adm}}\), rather than quantifying over arbitrary physical devices, arbitrary oracle models, or arbitrary hypercomputational models.

---

## 3. Layer I: Global Computational Complexity State (GCC)

### 3.1 Definition

For a decision language \(L\), let

\[
T_M^L(n)
\]

denote the worst-case time of some deterministic algorithm that correctly decides \(L\) on model \(M\in\mathfrak M_{\mathrm{adm}}\).

This paper denotes the "Global Computational Complexity State" as:

\[
\mathrm{GCC}(L)
=
[T_M^L]_{\equiv_{\mathrm{poly}}},
\]

which ignores the polynomial overhead between admissible models and retains only their polynomial equivalence class.

Define:

\[
\mathrm{GCC}(L)\in\mathbf{Poly}
\]

if and only if there exists some \(M\in\mathfrak M_{\mathrm{adm}}\) and some deterministic algorithm \(A\), such that

\[
T_{M,A}^L(n)\le n^{O(1)}.
\]

### 3.2 Relationship with Standard P

Under the assumption of polynomial invariance among admissible models:

\[
\mathrm{GCC}(L)\in\mathbf{Poly}
\]

can be viewed as

\[
L\in P
\]

a cross-model restatement, rather than a new complexity class.

Therefore:

\[
\forall L\in NP,\quad
\mathrm{GCC}(L)\in\mathbf{Poly}
\]

should have the same target content as the standard

\[
P=NP
\]

The role of GCC is to rewrite "whether there is a polynomial-time algorithm" into "whether the problem falls into the same polynomial resource equivalence domain under all admissible computational bases."

---

## 4. Layer II: Universal State-Rate Transformation State (USRT)

### 4.1 State and Completion Time

Let the computational state of algorithm \(A\) on input \(x\) be:

\[
S_A(x,t).
\]

Let the set of correct completion states be:

\[
H_L(x)
=
\{s:
s\text{ has halted and outputs }\chi_L(x)\}.
\]

Define the hitting time:

\[
\tau_A(x)
=
\min\{t:
S_A(x,t)\in H_L(x)\}.
\]

Then define the worst-case completion time:

\[
T_A(n)
=
\max_{|x|\le n}\tau_A(x).
\]

This paper uses a simple completion rate parameterization:

\[
R_A(n)
=
\frac{1}{1+T_A(n)}.
\]

Thus:

\[
T_A(n)\le n^k
\]

is equivalent to:

\[
R_A(n)
\ge
\frac{1}{1+n^k}.
\]

### 4.2 The Correct Meaning of "Rate Consistency"

This paper does not require nondeterministic and deterministic computations to have the same step-by-step speed, nor does it require:

\[
T_D(n)=T_N(n).
\]

If \(P=NP\), a nondeterministic \(n^2\) process could very well be transformed into a deterministic \(n^{20}\) algorithm; both still belong to polynomial time.

Therefore, "rate consistency" should be defined as:

\[
\boxed{\text{Belonging to the same polynomial completion-rate cone}}
\]

rather than numerical equality.

### 4.3 USRT

Let \(N\) be a polynomially clocked nondeterministic machine. Define a universal state-rate transformation schema:

\[
\mathcal U_{\mathrm{rate}}:
N\mapsto D_N,
\]

such that \(D_N\) is a deterministic machine, satisfying:

**Semantic Preservation:**

\[
D_N(x)=1
\iff
N(x)\text{ has an accepting path}.
\]

**Deterministic Completion:**

\[
\forall x,\quad
D_N(x)\text{ eventually halts}.
\]

**Polynomial Rate Preservation:**

\[
\exists q_N\in\operatorname{poly}
\quad
\forall n,
\quad
T_{D_N}(n)\le q_N(n).
\]

The order of quantifiers is particularly important:

\[
\exists\mathcal U_{\mathrm{rate}}
\;\forall N\;
\exists q_N\in\operatorname{poly}
\;\forall x.
\]

It must not be mistakenly written as a universal runtime bound where all \(N\) share the same fixed exponent; the latter is much stronger than the standard \(P=NP\).

---

## 5. Layer III: Universal Effective Sequence Generation State (USEG)

### 5.1 Raw Sequence Cardinality is Not Complexity

For a nondeterministic machine \(N\) and input \(x\), denote all valid computational paths as:

\[
\Gamma_N(x)
=
\{\gamma_1,\gamma_2,\ldots\}.
\]

If there are at most \(b\) branches per step and the path length is at most \(p(n)\), there could be:

\[
|\Gamma_N(x)|
\le
b^{p(n)}
\]

raw paths.

However, the number of raw paths itself does not directly imply hardness.

A problem originally in P can be deliberately written as a machine that first nondeterministically guesses a massive number of useless bits, then ignores them and calls the original P algorithm. In this case, \(|\Gamma_N(x)|\) can be exponentially large, but the language remains in P.

Therefore, this paper explicitly rejects the following inference:

\[
|\Gamma_N(x)|\text{ is exponentially large}
\Rightarrow
L\notin P.
\]

### 5.2 Effective Sequence Cardinality

What truly might hold complexity significance is the "sequence difference that can no longer be merged for decision-making."

Let:

\[
\gamma_a\sim_D\gamma_b
\]

denote that two computational paths can be accurately represented by the same summary regarding the information required for the final decision.

Define:

\[
\kappa_{\mathrm{eff}}(N,x)
=
|\Gamma_N(x)/{\sim_D}|.
\]

The focus here is not the numerical value of \(\kappa_{\mathrm{eff}}\) itself, but rather:

1. Whether the equivalence relation can be efficiently constructed;
2. Whether the quotient can be represented by a polynomial-size representation;
3. Whether the quotient transition can be updated in polynomial time;
4. Whether the final answer can be accurately read from the quotient state.

Otherwise, one could circularly "solve the problem first, and then claim that all paths actually belong to a single decision class."

### 5.3 USEG

Define the Universal Effective Sequence Generation State:

\[
\mathrm{USEG}.
\]

For every polynomial-time nondeterministic machine \(N\), it requires the existence of a deterministic generator \(G_N\) that, for each input \(x\), generates:

\[
Z_0,Z_1,\ldots,Z_m,
\]

where each \(Z_t\) is a **decision-sufficient summary** of the entire batch of nondeterministic computation histories, and:

\[
m\le\operatorname{poly}(|x|),
\]

\[
|Z_t|\le\operatorname{poly}(|x|),
\]

\[
Z_{t+1}
=
F_N(Z_t,x)
\]

can be computed in polynomial time, and:

\[
\operatorname{Dec}(Z_m)=1
\iff
\exists\gamma\in\Gamma_N(x):
\operatorname{Accept}(\gamma).
\]

USEG is therefore not "generating all nondeterministic branches one by one," but rather:

\[
\boxed{
\text{Accurately compressing the entire sequence family into a single deterministic effective sequence}.
}
\]

---

## 6. Three-Phase Equivalence: The Core Heuristic Proposition of This Paper

Under the above definitions and model boundaries, this paper proposes the following **heuristic equivalence program pending formal verification**:

\[
\boxed{
\mathrm{GCC}
\Longleftrightarrow
\mathrm{USRT}
\Longleftrightarrow
\mathrm{USEG}
}
\]

and anticipates that:

\[
\boxed{
\mathrm{GCC}
\Longleftrightarrow
\mathrm{USRT}
\Longleftrightarrow
\mathrm{USEG}
\Longleftrightarrow
P=NP
}
\]

can be proven to be truly equivalent in an appropriate formal system, or at least decomposed into several directions to be proven separately.

At present, this paper does not claim to have completed this proof.

The intuitive reasoning is as follows.

### 6.1 GCC \(\Rightarrow\) USRT

If the deterministic global complexity of every NP language falls into \(\mathbf{Poly}\), then the language decided by any polynomial-time nondeterministic machine has some deterministic polynomial-time realization, and thus a corresponding polynomial completion-rate realization can be established.

### 6.2 USRT \(\Rightarrow\) USEG

If \(N\) has been transformed into a deterministic polynomial machine \(D_N\), then:

\[
S_{D_N}(x,0)
\to
S_{D_N}(x,1)
\to
\cdots
\to
S_{D_N}(x,T)
\]

is itself a polynomial-length, decision-sufficient effective deterministic sequence.

### 6.3 USEG \(\Rightarrow\) GCC

If every NP computation family can be accurately represented by a deterministic polynomially generated:

\[
Z_0\to Z_1\to\cdots\to Z_m
\]

then a deterministic machine only needs to generate this sequence and read \(\operatorname{Dec}(Z_m)\), thereby obtaining a polynomial-time deterministic decision procedure.

What requires supplementation by subsequent work here is not the intuition above, but the complete formalization of uniformity, encoding, construction cost, state size, precision, and simulation overhead in each definition.

---

## 7. Layer IV: Global Lossless Completion State (GLC)

The first three layers answer:

> Can it be done within polynomial resources?

The fourth layer answers:

> Is a completed result that unconditionally meets the acceptance specifications truly delivered in the end?

Therefore, GLC is a **closure condition**, not simply a fourth equivalent parameter.

### 7.1 Final Ledger

For algorithm \(A\) and input \(x\), define the final ledger:

\[
\mathcal L_A(x)
=
(
C_A,
F_A,
B_A,
R_A,
S_A,
\Lambda_A
),
\]

which can be respectively understood as:

- \(C_A\): Correctness;
- \(F_A\): Completion / Finality;
- \(B_A\): Resource Budget;
- \(R_A\): Completion Rate;
- \(S_A\): Effective Sequence Cost;
- \(\Lambda_A\): Semantic Loss.

Define the qualified set:

\[
\mathcal A_{\mathrm{final}}.
\]

Final acceptance only requires:

\[
\forall x,\quad
\mathcal L_A(x)
\in
\mathcal A_{\mathrm{final}}.
\]

Its minimum specifications are:

\[
C_A=1,
\]

\[
F_A=1,
\]

\[
B_A\in\mathbf{Poly},
\]

\[
R_A\in\text{Polynomial Completion Cone},
\]

\[
S_A\in\mathbf{Poly},
\]

and:

\[
\Lambda_A=0.
\]

Thus, this paper adopts an **outcome-accounting** perspective:

\[
\boxed{
\text{The process is free, but the final ledger is not.}
}
\]

In the middle of the algorithm, one may:

- Switch data structures;
- Switch representations;
- Use different local algorithms;
- Rollback;
- Restart;
- Prune;
- Recompute;
- Pause and resume;

But as long as these operations are permitted, they must all be accounted for in the final resource ledger, and the final output must not be erroneous nor lose decision semantics.

---

## 8. Weak and Strong Versions of GLC

Here, two different claims must be distinguished.

### 8.1 Standard GLC

In the standard deterministic Turing-machine / RAM-style complexity setting, a P algorithm claiming to decide language \(L\) inherently must:

\[
\forall x
\]

halt and output the correct answer within polynomial time.

This has a direct analogy to total correctness in program verification—"halts and the result is correct" [4].

Therefore:

\[
\boxed{
\mathrm{GLC}_{\mathrm{std}}
}
\]

primarily writes the correctness + termination already implicit in traditional P explicitly into the final ledger.

It should not be claimed as a new conclusion stronger than \(P=NP\).

### 8.2 Robust GLC

If we further allow a set of execution histories:

\[
\operatorname{Runs}_{\mathrm{adm}}(A,x),
\]

which includes:

- Rerouting;
- Representation switching;
- Rollback;
- Restart;
- Finitely recoverable faults;
- Valid scheduler variations;

and require:

\[
\forall\pi\in
\operatorname{Runs}_{\mathrm{adm}}(A,x),
\]

there ultimately exists:

\[
t<\infty
\]

such that:

\[
\pi_t\in H_L(x),
\]

and:

\[
\operatorname{out}(\pi_t)=\chi_L(x),
\]

then we obtain:

\[
\boxed{
\mathrm{GLC}_{\mathrm{robust}}.
}
\]

This is a stronger resilient / dynamical property, no longer automatically equivalent to traditional \(P=NP\).

At the same time, if "permanent power loss, permanent non-scheduling, unrecoverable physical destruction" are allowed while still requiring guaranteed completion, the proposition itself becomes impossible. Therefore, robust GLC must only quantify over **valid and ultimately continuable perturbation sets**.

---

## 9. P/NP Dynamic Four-Layer Closure Framework

This paper ultimately proposes:

\[
\boxed{
\textbf{P/NP Dynamic Four-Layer Closure Framework}
}
\]

Its structure is:

### Layer I: Global Complexity

\[
\boxed{\mathrm{GCC}}
\]

Answers:

> Do the ultimately required deterministic computational resources lie within a polynomial equivalence class under admissible models?

### Layer II: State-Rate Transformation

\[
\boxed{\mathrm{USRT}}
\]

Answers:

> Can nondeterministic polynomial completion dynamics be universally transformed into deterministic polynomial completion dynamics?

### Layer III: Effective Sequence Generation

\[
\boxed{\mathrm{USEG}}
\]

Answers:

> Can a nondeterministic sequence family be accurately compressed into a deterministic polynomial effective sequence?

### Layer IV: Global Lossless Completion

\[
\boxed{\mathrm{GLC}}
\]

Answers:

> In the final ledger, are all requirements met, with zero erroneous results, zero semantic loss, and computation truly completed?

Thus, the whole can be written as:

\[
\boxed{
\left[
\mathrm{GCC}
\equiv
\mathrm{USRT}
\equiv
\mathrm{USEG}
\right]
\overset{\mathrm{GLC}}{\Longrightarrow}
\text{Closed Exact Computation}.
}
\]

In standard reliable computational models, if the first three are ultimately proven to be equivalent to \(P=NP\), then \(\mathrm{GLC}_{\mathrm{std}}\) can be viewed as its explicit final-state requirement; robust GLC is reserved as a stronger subsequent dynamic extension.

---

## 10. The Boundary Between "Final Ledger" and Process Agnosticism

This paper's "only accepting the final ledger" does not equate to completely ignoring process costs.

If an algorithm:

\[
A
\]

performs:

\[
2^{2^n}
\]

steps of computation midway before finally delivering the correct answer, then its Resource field will inevitably fail to qualify.

Therefore:

\[
\boxed{
\text{Agnostic to process details}
\neq
\text{Ignoring process costs}.
}
\]

A more precise statement is:

> The acceptance layer does not require the algorithm to adhere to fixed internal mechanisms, but all accountable resource costs incurred by internal mechanisms must be compressed into the final ledger.

Thus, the final ledger is a **path-agnostic but cost-complete** interface.

This distinction is extremely important to the framework.

---

## 11. What This Paper Does Not Claim

To avoid confusion with formal P/NP proofs, this paper explicitly does not claim:

1. To have proven the complete formal theorem of \(\mathrm{GCC}\iff\mathrm{USRT}\iff\mathrm{USEG}\);
2. To have proven all directions between the above three and \(P=NP\);
3. To have found an effective polynomial sequence quotient for SAT;
4. That raw nondeterministic path cardinality itself can imply time lower bounds;
5. That arbitrary Turing-complete computational models possess the same complexity;
6. That robust GLC is equivalent to standard \(P=NP\);
7. That this framework bypasses existing barriers such as relativization, natural proofs, or algebrization;
8. That this paper provides a proof of \(P=NP\) or \(P\neq NP\).

The current academic positioning of this paper should be:

\[
\boxed{
\text{heuristic reformulation + formalization agenda}.
}
\]

---

## 12. Main Lines of Formalization Research

For this framework to advance from a conceptual paper to a testable mathematical theory, at least the following work needs to be completed.

### 12.1 Model Theorem for GCC

Explicitly define:

\[
\mathfrak M_{\mathrm{adm}}
\]

and admissible simulation relations, proving that GCC does not depend on a specific machine representation.

### 12.2 Equivalence Theorem for USRT

Prove or refute:

\[
P=NP
\iff
\mathrm{USRT}
\]

and fix:

- Machine encoding;
- Clock encoding;
- Uniform transformation;
- Transformation construction cost;
- The quantifier order of the per-machine polynomial exponent.

### 12.3 Non-Circular Definition of USEG

One of the most difficult tasks is defining a "decision-sufficient effective sequence" without secretly embedding a SAT solver into the quotient relation itself.

It is necessary to precisely control:

\[
T_{\mathrm{construct}},
\quad
L_{\mathrm{state}},
\quad
T_{\mathrm{update}},
\quad
T_{\mathrm{decode}}.
\]

### 12.4 Three-Phase Equivalence

Separately prove:

\[
\mathrm{GCC}\Rightarrow\mathrm{USRT},
\]

\[
\mathrm{USRT}\Rightarrow\mathrm{USEG},
\]

\[
\mathrm{USEG}\Rightarrow\mathrm{GCC},
\]

and confirm that no direction is merely a definitional circularity.

### 12.5 GLC Acceptance Semantics

Formalize the final ledger:

\[
\mathcal L_A(x)
\]

distinguishing between:

\[
\mathrm{GLC}_{\mathrm{std}}
\]

and:

\[
\mathrm{GLC}_{\mathrm{robust}},
\]

and avoid mistakenly writing engineering fault tolerance as a traditional complexity-theoretic necessary condition.

---

## 13. Discussion

The core value of this four-layer framework lies not in renaming "polynomial time" to "rate," but in decomposing the same core difficulty of P/NP into four research interfaces.

The first interface asks about resources:

\[
\text{How much is needed?}
\]

The second interface asks about dynamics:

\[
\text{How and at what rate is the completion state reached?}
\]

The third interface asks about representation and generation:

\[
\text{How can a massive number of possible histories be accurately compressed?}
\]

The fourth interface asks about closure:

\[
\text{Does the finally delivered result truly meet all specifications?}
\]

The part that truly might generate new mathematical content is particularly concentrated in USEG. This is because generating a polynomial state sequence from a known deterministic polynomial algorithm is not difficult; the difficulty lies in whether, without yet assuming \(P=NP\), one can independently construct an effective quotient / aggregation mechanism that accurately folds the existential quantifier of an NP computation family into a polynomial deterministic sequence.

Similarly, GCC and USRT might ultimately be proven to be merely different coordinates for standard P/NP, whereas the formalization of USEG might force researchers to explicitly answer:

> "What exactly does it mean to not unfold candidates one by one, yet still accurately preserve all information relevant to the final decision?"

This shares structural similarities with existing techniques such as dynamic programming, state compression, knowledge compilation, algebraic elimination, and quotient construction, but this paper currently does not claim the existence of a universal form that covers general SAT.

---

## 14. Conclusion

This paper proposes the "P/NP Dynamic Four-Layer Closure Framework," reformulating the core problem of traditional P vs. NP into four interconnected layers:

\[
\boxed{
\mathrm{GCC}
:
\text{Global Computational Complexity}
}
\]

\[
\boxed{
\mathrm{USRT}
:
\text{Universal State-Rate Transformation}
}
\]

\[
\boxed{
\mathrm{USEG}
:
\text{Universal Effective Sequence Generation}
}
\]

and:

\[
\boxed{
\mathrm{GLC}
:
\text{Global Lossless Completion}.
}
\]

The first three layers are proposed as three observational coordinates potentially equivalent to \(P=NP\):

\[
\boxed{
\mathrm{GCC}
\stackrel{?}{\Longleftrightarrow}
\mathrm{USRT}
\stackrel{?}{\Longleftrightarrow}
\mathrm{USEG}
\stackrel{?}{\Longleftrightarrow}
P=NP.
}
\]

The question marks indicate that this paper has not yet provided a complete formal proof.

The fourth layer, GLC, is not intended to change the standard definition of P/NP, but rather to explicitly write "must ultimately complete correctly" as a closure condition. Its most concise engineering-style formulation is:

\[
\boxed{
\text{The process is free, but the final ledger is not.}
}
\]

Computation may reroute, change representations, recompute, or use any valid intermediary mechanism; but ultimately it must be that:

\[
\boxed{
\text{Correct}
=
1,
\qquad
\text{Complete}
=
1,
}
\]

\[
\boxed{
\text{Resource}
\in
\mathbf{Poly},
}
\]

\[
\boxed{
\text{Semantic Loss}
=
0.
}
\]

Therefore, what this paper truly proposes is not a P/NP conclusion, but a new formalization research route:

\[
\boxed{
\text{Resources}
\rightarrow
\text{Rate}
\rightarrow
\text{Sequence}
\rightarrow
\text{Lossless Completion}.
}
\]

If, in the future, the complete equivalence of the first three with traditional \(P=NP\) can be proven—under the premises of no circular definitions, no hidden super-polynomial costs, and maintaining standard uniform complexity accounting—and a non-trivial construction or impossibility theorem is established for one of these layers, only then will this framework advance from a heuristic concept to a genuine complexity-theoretic tool.

At present, this paper only claims: **This is a research framework that can be formalized, refuted, or proven and decomposed layer by layer.**

---

## References

[1] Cook, S. A. *The P versus NP Problem*. In: **The Millennium Prize Problems**. Clay Mathematics Institute / American Mathematical Society.

[2] Cobham, A. “The Intrinsic Computational Difficulty of Functions.” Proceedings of the 1964 International Congress for Logic, Methodology, and Philosophy of Science, 1965.

[3] Computational Complexity Theory, *Stanford Encyclopedia of Philosophy*. Regarding the Cobham–Edmonds Thesis, Invariance Thesis, and polynomial simulation of admissible computational models.

[4] Cornell University CS3110 / CS4110 course materials. Regarding the standard distinction between partial correctness, termination, and total correctness.

[5] Blum, M. “A Machine-Independent Theory of the Complexity of Recursive Functions.” *Journal of the ACM*, 1967.

---

## Author's Note

This paper is a conceptual reorganization draft within the P/NP dynamic rate research line. Its purpose is not to write unproven equivalences as theorems, but to unify intuitions previously scattered across "computational resources, state transitions, sequence generation, and result acceptance" into a single formal framework. All subsequent proof work should be based on standard P/NP definitions, and any new definitions must be strictly cross-referenced one by one with existing complexity classes, computational models, and resource bounds.