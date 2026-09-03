# CSM Paper 03 — Frontier Geometry, Cut Sets, and Relative Exhaustion

## Closure-Space Mathematics: Frontier Geometry, Cut Sets, Obstruction Covers, and Relative Exhaustion

**English Title:** *Closure-Space Mathematics: Frontier Geometry, Cut Sets, Obstruction Covers, and Relative Exhaustion*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 03  
**Version:** v0.1  
**Date:** 2026-08-27  
**Language:** English  
**Status:** Formal Theory / Frontier and Exhaustion Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline `$...$`; display `$$...$$`

---

## Abstract

This paper establishes the frontier geometry and relative exhaustion theory of Closure-Space Mathematics (CSM). Paper 00 established the relative-global closure space; Paper 01 established globality typing and scope contracts; Paper 02 established the typed closure hypergraph, obstruction propagation, reopening, and route-completeness obligations. This paper now addresses one of the most easily misjudged and critical problems in long-range mathematical research:

> After many research routes of a large-scale proposition have been proven, refuted, blocked, conditionally closed, or quotiented, what exactly is the remaining "truly unclosed portion"? Under what conditions can sealing these remaining frontiers be legally promoted to an exhaustion conclusion at the proposition level?

This paper first defines **active frontier**, **quotient frontier**, **weighted frontier mass**, **frontier component**, **closure distance**, and **reopening boundary**. It then generalizes the standard graph cut to the typed directed hypergraph of CSM, distinguishing:

1. route cut;
2. assumption cut;
3. obstruction cut;
4. bridge cut;
5. scope cut;
6. representation cut;
7. mixed typed cut.

This paper introduces the **Certified Cut** and **Obstruction Cover**: the former requires that every admissible route must pass through a specified cut; the latter requires that a set of certified obstructions can cover all cut elements or all admissible route classes. Only when:

$$
\boxed{
\mathsf{RouteCompleteness}
+
\mathsf{CutCompleteness}
+
\mathsf{ObstructionCoverage}
+
\mathsf{ScopeFidelity}
+
\mathsf{ParentBridge}
}
$$

hold simultaneously, is it permissible to promote "all observed routes are sealed" to a parent-level relative exhaustion.

This paper specifically distinguishes:

$$
\boxed{
\text{Observed Exhaustion}
\neq
\text{Admissible Exhaustion}
\neq
\text{Relative Mathematical Exhaustion}
\neq
\text{Absolute Mathematical Exhaustion}.
}
$$

This stratification directly prevents a common fallacy: a shrinking frontier in the research corpus does not equate to a shrinking frontier in the mathematical space; digging deeply into a proof basin does not mean the entire proof space has been traversed.

This paper also introduces **Frontier Reopening Geometry**. If a new representation, new bridge, new theorem, scope revision, or assumption relaxation invalidates an old cut, the previous exhaustion certificate must enter a `STALE` or `REOPENED` state, and the frontier must be recomputed. Thus, "exhaustion" in CSM is not a one-time final declaration, but a versioned, scoped, replayable, and revocable relative-global closure event.

Finally, this paper proposes the first version of frontiers for the Navier--Stokes relative-global closure graph: expressed not by paper count, but by quotient route classes, independent obstruction mass, survivor components, bridge debt, and route-completeness debt. This gives "step-by-step sealing of the NS proposition" an operational geometric meaning for the first time: the direct goal of research is no longer to increase paper count, but to shrink the effective frontier after quotienting and certificate audits, while avoiding false contractions.

---

# 1. Research Positioning

This paper builds upon:

$$
\mathcal H_{\rm CSM}
=
(V,E,\tau_V,\tau_E,\sigma,\lambda,\pi,\chi,\nu).
$$

Paper 02 can already answer:

- which route is sealed by which obstruction;
- which status is merely blocked;
- which branch is truly closed;
- which closure can be reopened.

This paper further asks:

$$
\boxed{
\text{Which OPEN / CONDITIONAL / UNKNOWN / REOPENED
nodes truly constitute the effective frontier of the target?}
}
$$

---

# 2. Raw Frontier

For a target $Q$, define the raw frontier:

$$
\partial_{\rm raw}\mathfrak C(Q)
=
\left\{
v:
\sigma(v)\in
\{
\mathsf{OPEN},
\mathsf{CONDITIONAL},
\mathsf{UNKNOWN},
\mathsf{REOPENED}
\}
\land
v\leadsto Q
\right\}.
$$

This is merely a candidate set.

---

# 3. Flaws of the Raw Frontier

The raw frontier may severely overestimate the unclosed space because:

- multiple nodes might represent the same proposition;
- multiple routes might just be representation variants;
- multiple obstruction debts might actually share the same origin;
- different detailed branches of a parent route might be double-counted.

Therefore, the raw frontier cannot serve as an exhaustion basis.

---

# 4. Quotient Frontier

Use:

$$
\sim_{\rm prop},
\qquad
\sim_{\rm route},
\qquad
\sim_{\rm obs}
$$

to perform quotienting.

Define:

$$
\boxed{
\partial^\ast\mathfrak C(Q)
=
\partial_{\rm raw}\mathfrak C(Q)
/\sim_{\rm route}.
}
$$

If necessary, further apply to the claim layer:

$$
\partial_{\rm prop}^\ast.
$$

---

# 5. Frontier Identity Principle

Whether two nodes are considered "the same" in the frontier must be determined by the quotient policy, and cannot solely rely on:

- lexical similarity;
- embedding proximity;
- notation similarity;
- same-paper ancestry.

---

# 6. Frontier Weight

For a route class $[R]$, define:

$$
w([R])\ge0.
$$

It can be composed of the following factors:

$$
w([R])
=
f(
\mathsf{Independence},
\mathsf{Generality},
\mathsf{ScopeBreadth},
\mathsf{CertificateQuality},
\mathsf{BridgeDebt}
).
$$

---

# 7. Frontier Mass

$$
\boxed{
M_{\partial}(Q)
=
\sum_{[R]\in\partial^\ast\mathfrak C(Q)}
w([R]).
}
$$

This is a research-space observable.

It is not "the percentage remaining until the proof is complete."

---

# 8. Frontier Cardinality is Not Mass

It is possible that:

$$
|\partial^\ast_1|
<
|\partial^\ast_2|
$$

but:

$$
M_{\partial,1}
>
M_{\partial,2}.
$$

Because fewer routes might be more general, more independent, and harder to seal.

---

# 9. Frontier Component

On the quotient route graph, if frontier nodes form a connected component:

$$
F_i
\subset
\partial^\ast\mathfrak C(Q),
$$

it is called a:

$$
\boxed{
\text{frontier component}.
}
$$

---

# 10. Component is Not Basin

A proof basin is a high-density subgraph in historical/search dynamics.

A frontier component is:

> the structural connected component among currently unclosed obligations.

The two can overlap but are not equivalent.

---

# 11. Frontier Boundary Type

Each frontier component can have a dominant type:

$$
\tau_F(F_i)
\in
\{
\mathsf{LEMMA},
\mathsf{ASSUMPTION},
\mathsf{BRIDGE},
\mathsf{SCOPE},
\mathsf{REPRESENTATION},
\mathsf{OBSTRUCTION},
\mathsf{COMPLETENESS},
\mathsf{COUNTEREXAMPLE},
\mathsf{UNKNOWN}
\}.
$$

---

# 12. Frontier Debt

Define:

$$
\boxed{
\mathsf{FDebt}(F_i)
}
$$

to represent the proof obligations that the component has not yet discharged.

For example:

- route completeness;
- branch decomposition;
- missing bridge;
- uniformity;
- representation robustness;
- scope promotion;
- hidden-assumption audit.

---

# 13. Frontier Contraction

If:

$$
M_{\partial,t+1}(Q)
<
M_{\partial,t}(Q),
$$

and the decrease comes from a certified closure event, it is called a:

$$
\boxed{
\text{certified frontier contraction}.
}
$$

---

# 14. Frontier Expansion

If new research discovers a previously unmodeled route class:

$$
M_{\partial,t+1}(Q)
>
M_{\partial,t}(Q),
$$

it is called a:

$$
\boxed{
\text{frontier expansion}.
}
$$

This is not necessarily a regression.

---

# 15. Fidelity-over-Size Principle

$$
\boxed{
\text{A more faithful but larger frontier}
>
\text{A falsely contracted frontier}.
}
$$

In terms of epistemic quality, a false contraction is worse than a truthful expansion.

---

# 16. False Frontier Contraction

If the frontier shrinks due to:

1. false quotient;
2. stealthy scope reduction;
3. unsupported obstruction transfer;
4. representation deletion;
5. hidden assumption;
6. stale theorem;
7. branch omission;

then it is marked as:

$$
\boxed{
\mathsf{FALSE\_CONTRACTION}.
}
$$

---

# 17. Frontier Reopening

If an old closure is revoked, the corresponding route class returns to:

$$
\partial^\ast\mathfrak C(Q).
$$

This is called a:

$$
\boxed{
\text{frontier reopening}.
}
$$

---

# 18. Reopening Boundary

Define:

$$
\boxed{
\partial_{\rm reopen}\mathfrak C(Q)
}
$$

as the route classes that re-enter the active frontier due to a revision.

---

# 19. Closure Distance

For a node $v$ to a target $Q$, define the typed closure distance:

$$
d_{\rm Cl}(v,Q).
$$

It is not a pure edge count.

It can be weighted by:

- unresolved assumptions;
- bridge count;
- certificate debt;
- scope promotions;
- obstruction depth.

---

# 20. Closure Radius

For the target frontier, define:

$$
\boxed{
R_{\rm Cl}(Q)
=
\sup_{v\in\partial^\ast\mathfrak C(Q)}
d_{\rm Cl}(v,Q).
}
$$

---

# 21. Radius is Not Difficulty

$$
\boxed{
R_{\rm Cl}(Q)
\not\Rightarrow
\text{proof difficulty}.
}
$$

A very short route may contain an extremely difficult lemma.

---

# 22. Closure Depth

Define the closure depth of a route:

$$
D_{\rm Cl}(R)
$$

representing how many layers of certified narrowing / branch elimination it has currently passed.

It can be used to compare the research maturity of the same route family.

---

# 23. Directed Hypergraph Route

A route is no longer just a vertex sequence.

It is:

$$
R
=
(e_1,e_2,\ldots,e_k)
$$

where each $e_i$ is a directed hyperedge, and the output of the preceding batch satisfies the input requirements of the succeeding batch.

---

# 24. Admissible Route

$$
R\in\mathcal R_{\rm adm}(Q)
$$

must satisfy:

1. edge type legal;
2. assumption consistent;
3. scope valid;
4. bridge certified;
5. target fidelity;
6. no forbidden promotion;
7. version current.

---

# 25. Observed Route

$$
\mathcal R_{\rm obs}(Q)
$$

are the route classes that have actually appeared in the corpus / research history.

Generally:

$$
\boxed{
\mathcal R_{\rm obs}(Q)
\subseteq
\mathcal R_{\rm adm}(Q)
}
$$

but equality cannot be assumed.

---

# 26. Enumerated Route

$$
\mathcal R_{\rm enum}^{\Gamma}(Q)
$$

are the route classes generated under a specified route grammar $\Gamma$.

---

# 27. Relative Route Completeness

If:

$$
\boxed{
\mathcal R_{\rm enum}^{\Gamma}(Q)
=
\mathcal R_{\rm adm}^{\Gamma}(Q)
}
$$

we say:

$$
\mathsf{RCCert}_{\Gamma}(Q)
$$

passes.

---

# 28. Absolute Route Completeness

To claim:

$$
\mathcal R_{\rm enum}(Q)
=
\mathcal R_{\rm adm}(Q)
$$

one must prove that the route grammar itself does not miss any admissible mechanism class.

This is usually very strong.

---

# 29. Cut Set

Let:

$$
C\subset V.
$$

If every:

$$
R\in\mathcal R_{\rm adm}^{\Gamma}(Q)
$$

passes through at least one element in $C$, then $C$ is called a:

$$
\boxed{
\Gamma\text{-route cut}.
}
$$

---

# 30. Typed Cut

The cut itself has a type:

$$
\tau_C(C)
\in
\{
\mathsf{ROUTE},
\mathsf{ASSUMPTION},
\mathsf{OBSTRUCTION},
\mathsf{BRIDGE},
\mathsf{SCOPE},
\mathsf{REPRESENTATION},
\mathsf{MIXED}
\}.
$$

---

# 31. Route Cut

If the cut elements are route states, it is denoted as:

$$
C_R.
$$

---

# 32. Assumption Cut

If all admissible routes depend on at least one:

$$
A\in C_A,
$$

then $C_A$ is an assumption cut.

If all $A$ are refuted, it can form a high-leverage closure.

---

# 33. Bridge Cut

If all routes must pass through at least one bridge:

$$
B\in C_B,
$$

then $C_B$ is a bridge cut.

This is important for cross-domain / cross-representation theorems.

---

# 34. Scope Cut

If all routes require a scope promotion:

$$
S\in C_S,
$$

then its completeness can be transformed into a scope-level obstruction problem.

---

# 35. Representation Cut

If all existing route families depend on a certain representation family:

$$
\rho\in C_{\rho},
$$

that only means the observed route space has a representation bottleneck.

It is not automatically an admissible proof-space cut.

---

# 36. Mixed Cut

Mature problems often require:

$$
C=
C_A
\cup
C_B
\cup
C_R
\cup
C_S.
$$

This forms a mixed typed cut.

---

# 37. Cut Certificate

Define:

$$
\boxed{
\mathsf{CutCert}_{\Gamma}(C,Q)
}
$$

Its goal is to prove:

$$
\forall R\in\mathcal R_{\rm adm}^{\Gamma}(Q),
\quad
R\cap C\neq\varnothing.
$$

---

# 38. Cut Completeness Debt

If one can only prove for observed routes:

$$
\forall R\in\mathcal R_{\rm obs}(Q),
\quad
R\cap C\neq\varnothing,
$$

then it forms:

$$
\boxed{
\mathsf{Debt}_{\rm cut}
=
\mathcal R_{\rm adm}^{\Gamma}
\setminus
\mathcal R_{\rm obs}.
}
$$

---

# 39. Minimal Cut

If $C$ is a cut, and any proper subset:

$$
C'\subsetneq C
$$

is no longer a cut, it is called a:

$$
\boxed{
\text{minimal cut}.
}
$$

---

# 40. Minimum Cut

If there is a cost function:

$$
\kappa:C\to\mathbb R_{\ge0},
$$

then the minimum total cost cut is:

$$
C^\star
=
\arg\min_C
\sum_{c\in C}\kappa(c).
$$

This is a research-routing heuristic.

It does not replace a theorem proof.

---

# 41. Hypergraph Transversal

If every admissible route can be viewed as a hyperedge family, then a cut can be understood as a route-family transversal.

CSM uses this concept but retains:

- typed edges;
- scope;
- certificate;
- version;
- reopening;

Therefore, it is not a simple static hypergraph hitting-set problem.

---

# 42. Obstruction Cover

Let the obstruction family be:

$$
\mathcal O
=
\{O_1,\ldots,O_m\}.
$$

If for every admissible route $R$, there exists at least one:

$$
O_i
$$

such that:

$$
\mathsf{OPCert}(O_i\to R)=\mathsf{PASS},
$$

then it is said that:

$$
\boxed{
\mathcal O
\text{ is an obstruction cover of }
\mathcal R_{\rm adm}^{\Gamma}(Q).
}
$$

---

# 43. Cover is Not Cut

A cut is a structural set that routes must pass through.

An obstruction cover is an obstruction family that can legally seal the routes.

The two are different.

---

# 44. Cut-to-Cover Strategy

A high-leverage proof strategy:

1. First prove a small cut;
2. Then build obstructions only for the cut elements;
3. Deduce back to all routes via cut completeness.

---

# 45. Cover Certificate

Define:

$$
\boxed{
\mathsf{CoverCert}_{\Gamma}(\mathcal O,Q).
}
$$

Requires:

- route completeness;
- propagation certificates;
- scope match;
- no uncovered class;
- version freshness.

---

# 46. Obstruction Cover Debt

If there exists an uncovered route class:

$$
[R]\notin
\bigcup_i
\mathsf{BlockedBy}(O_i),
$$

then:

$$
\mathsf{Debt}_{\rm cover}\neq\varnothing.
$$

---

# 47. Survivor Set

Define:

$$
\boxed{
\mathcal S(Q)
=
\left\{
[R]\in\mathcal R_{\rm adm}^{\Gamma}(Q):
[R]\text{ not certified closed}
\right\}.
}
$$

---

# 48. Survivor Frontier

If:

$$
\mathcal S(Q)
=
\partial^\ast\mathfrak C(Q)
$$

it indicates that all active frontiers have been compressed into survivor route classes.

---

# 49. Minimal Survivor Set

If all more general parent classes of the survivors have been sealed or decomposed, we obtain:

$$
\boxed{
\mathcal S_{\min}(Q).
}
$$

---

# 50. Survivor Compression Ratio

We can define:

$$
\boxed{
\operatorname{SCR}(Q)
=
\frac{
|\mathcal S_{\min}(Q)|
}{
|\mathcal R_{\rm enum}^{\Gamma}(Q)|
}.
}
$$

Used only as a research diagnostic.

---

# 51. Exhaustion Level 0 — Corpus Exhaustion

If:

$$
\partial_{\rm raw}
$$

has no new nodes in the current corpus, one can only say:

$$
\boxed{
\mathsf{EXH}_{0}
=
\text{corpus-local exhaustion}.
}
$$

---

# 52. Exhaustion Level 1 — Observed Route Exhaustion

If:

$$
\forall R\in\mathcal R_{\rm obs}(Q),
\quad
R\text{ closed/blocked},
$$

it is called:

$$
\boxed{
\mathsf{EXH}_{1}.
}
$$

---

# 53. Exhaustion Level 2 — Grammar-Relative Exhaustion

If:

$$
\mathsf{RCCert}_{\Gamma}(Q)=\mathsf{PASS}
$$

and:

$$
\forall R\in\mathcal R_{\rm adm}^{\Gamma}(Q),
\quad
R\text{ certified closed},
$$

it is called:

$$
\boxed{
\mathsf{EXH}_{2}^{\Gamma}.
}
$$

---

# 54. Exhaustion Level 3 — Domain-Relative Mathematical Exhaustion

If there is additionally a parent bridge:

$$
\neg\operatorname{RouteExists}_{\Gamma}(Q)
\Longrightarrow
\neg Q
$$

or a corresponding closure bridge for a positive target, then:

$$
\boxed{
\mathsf{EXH}_{3}^{D,\Gamma}.
}
$$

---

# 55. Exhaustion Level 4 — Cross-Representation Exhaustion

If all admissible representation classes:

$$
\rho\in\mathcal P_{\rm adm}
$$

are covered, and representation robustness holds:

$$
\boxed{
\mathsf{EXH}_{4}^{D}.
}
$$

---

# 56. Exhaustion Level 5 — Absolute Exhaustion Candidate

Only after domain, representation, route grammar, bridge, and formal-system completeness obligations have all been addressed, can one discuss:

$$
\boxed{
\mathsf{EXH}_{5}
=
\text{absolute exhaustion candidate}.
}
$$

This paper does not assume it is generally provable.

---

# 57. Exhaustion Ladder

$$
\boxed{
\mathsf{EXH}_0
\prec
\mathsf{EXH}_1
\prec
\mathsf{EXH}_2
\prec
\mathsf{EXH}_3
\prec
\mathsf{EXH}_4
\prec
\mathsf{EXH}_5.
}
$$

Skipping levels is prohibited.

---

# 58. Relative Exhaustion Certificate

Define:

$$
\boxed{
\mathsf{RECert}_{D,\Gamma}(Q).
}
$$

It contains at least:

1. target statement;
2. domain;
3. route grammar;
4. route-completeness cert;
5. cut cert;
6. obstruction cover cert;
7. bridge cert;
8. representation policy;
9. scope policy;
10. debt ledger;
11. version;
12. reopening policy.

---

# 59. Exhaustion with Debt

If:

$$
\mathsf{Debt}\neq\varnothing,
$$

then the exhaustion status can only be marked as:

$$
\boxed{
\mathsf{PARTIAL\_EXHAUSTION}.
}
$$

---

# 60. Exhaustion Staleness

If the theorem base, scope, representation family, or bridge set changes, the old:

$$
\mathsf{RECert}
$$

must enter:

$$
\mathsf{STALE}.
$$

---

# 61. Revalidated Exhaustion

Only after re-running the closure audit can it transition:

$$
\mathsf{STALE}
\to
\mathsf{VALID}.
$$

---

# 62. Parent Closure Bridge

If route exhaustion is to deduce parent claim closure, it requires:

$$
\boxed{
\mathsf{ParentBridgeCert}.
}
$$

For example:

$$
\neg\operatorname{RouteExists}
\Rightarrow
\neg Q.
$$

This implication cannot be taken for granted.

---

# 63. Positive Parent Bridge

For an existence theorem:

$$
\exists R\in\mathcal R_{\rm adm}(Q)
\land
\mathsf{Proof}(R)
\Rightarrow
Q.
$$

target fidelity is also required.

---

# 64. Negative Parent Bridge

For an impossibility theorem:

$$
\forall R\in\mathcal R_{\rm adm}(Q),
\neg\mathsf{Valid}(R)
\Rightarrow
\neg Q
$$

route completeness and proof-form completeness are usually required.

---

# 65. Exhaustion is Not Falsehood

Even if:

$$
\mathsf{EXH}_2^\Gamma
$$

holds, it only means:

> there are no surviving routes in $\Gamma$.

One cannot directly write:

$$
\neg Q.
$$

---

# 66. Exhaustion is Not Unprovability

Similarly:

$$
\mathsf{EXH}_2^\Gamma
\not\Rightarrow
\text{$Q$ unprovable}.
$$

---

# 67. Exhaustion is Not Independence

Only by truly proving under a specified formal theory $\mathcal T$:

$$
\mathcal T\nvdash Q,
\qquad
\mathcal T\nvdash\neg Q
$$

can one claim relative independence.

---

# 68. Cut Centrality

Define cut centrality:

$$
Z(C)
$$

representing the independent route mass truncated by the cut.

---

# 69. Obstruction Centrality

Define:

$$
Z(O)
=
\sum_{[R]:
O\triangleright R}
w([R]).
$$

---

# 70. Centrality is Not Necessity

$$
\boxed{
Z(O)\text{ high}
\not\Rightarrow
O\text{ mathematically necessary}.
}
$$

---

# 71. Closure Bottleneck

If a small number of cut elements bear the majority of the route mass:

$$
Z(C)/M_{\mathcal R}\to1,
$$

it is called a:

$$
\boxed{
\text{closure bottleneck}.
}
$$

---

# 72. Bottleneck Research Priority

Prioritizing research on closure bottlenecks can usually maximize:

$$
\Delta M_{\partial}
$$

the expected reduction of.

This is a routing heuristic.

---

# 73. Bottleneck Reopening Risk

Once a high-centrality cut becomes invalid, it may also cause massive frontier reopening.

Therefore, one must record:

$$
\boxed{
\mathsf{ReopenRisk}(C).
}
$$

---

# 74. Redundant Cut

If multiple cut elements actually belong to the same obstruction class, the raw cut size will be overestimated.

Quotienting is required:

$$
C^\ast=C/\sim_{\rm obs}.
$$

---

# 75. Independent Cut Mass

$$
\boxed{
M_C
=
\sum_{[c]\in C^\ast}
w([c]).
}
$$

---

# 76. Route-Cut Duality Candidate

In certain finite typed graphs, the minimal route cover and obstruction cut might form a duality problem.

This paper only treats this as a research direction and does not claim that general max-flow/min-cut type theorems automatically hold.

---

# 77. Hypergraph Duality Debt

To establish a general duality theorem, one needs to handle:

- hyperedge multiplicity;
- edge typing;
- nonlocal assumptions;
- scope;
- bridge loss;
- reopening;
- versioning.

---

# 78. Frontier Topology

This paper does not yet claim the frontier to be a traditional topological space.

But a graph-induced neighborhood can be defined:

$$
N_k(v)
=
\{u:d_{\rm graph}(u,v)\le k\}.
$$

---

# 79. Closure Neighborhood

More suitable for CSM is:

$$
\boxed{
N_{\rm Cl}(v)
=
\{u:
u\text{ shares closure obligations with }v\}.
}
$$

---

# 80. Shared-Obstruction Neighborhood

If two routes are both constrained by the same obstruction family:

$$
O\triangleright R_1,
\quad
O\triangleright R_2,
$$

then they can be viewed as being in the same closure neighborhood.

---

# 81. Shared-Bridge Neighborhood

If multiple routes share the same bridge debt, they form a bridge-frontier cluster.

---

# 82. Frontier Curvature Heuristic

If a minor modification to a frontier node causes a large number of neighboring routes to reopen/close, high sensitivity can be defined.

This paper tentatively calls:

$$
\boxed{
\kappa_{\rm F}(v)
}
$$

the frontier curvature heuristic.

This is not differential geometric curvature.

---

# 83. High-Curvature Frontier

High $\kappa_{\rm F}$ nodes are typically:

- key lemma;
- scope gate;
- representation bridge;
- common assumption;
- central obstruction.

---

# 84. Frontier Flat Region

A large number of mutually similar, low-impact, low-independence open nodes can form a:

$$
\boxed{
\text{frontier flat region}.
}
$$

They should usually be quotiented first.

---

# 85. Frontier Singularity Heuristic

If all active route mass concentrates in a few unresolved nodes:

$$
M_{\partial}(F_{\rm core})
/
M_{\partial}(Q)
\to1,
$$

it can be called closure-frontier concentration.

This paper does not equate it to a PDE singularity.

---

# 86. Closure Cone

For an unresolved assumption $A$, all downstream routes depending on it are:

$$
\boxed{
\mathsf{Cone}(A)
=
\{R:A\leadsto R\leadsto Q\}.
}
$$

---

# 87. Cone Closure

If $A$ is refuted at the theorem level, and the inheritance cert is complete, the entire cone can enter a blocked / closed audit in batch.

---

# 88. Cone Reopening

If the refutation of $A$ is restricted, the entire cone enters a reopening audit.

---

# 89. Closure Shell

Stratified by closure distance:

$$
\boxed{
\mathcal S_k(Q)
=
\{v:d_{\rm Cl}(v,Q)=k\}.
}
$$

---

# 90. Shell Progression

Research history can track the frontier compressing from distant shells to near shells, or vice versa.

This is a geometric description and does not guarantee proof completion.

---

# 91. Closure Core

Define:

$$
\boxed{
\mathsf{Core}_{\rm Cl}(Q)
}
$$

as the high-overlap substructure of all admissible route classes.

---

# 92. Core is Not Necessary Lemma

Only when a CutCert is present can the core be promoted to a route-necessary region.

---

# 93. Relative Global Frontier

For domain $D$:

$$
\boxed{
\partial_D^\ast\mathfrak C(Q).
}
$$

Frontiers of different domains need not be the same.

---

# 94. Domain Projection of Frontier

If:

$$
D_0\preceq D_1,
$$

there can be a projection:

$$
\Pi_{D_1\to D_0}
:
\partial_{D_1}^\ast
\to
\partial_{D_0}^\ast.
$$

But it cannot be presumed injective or surjective.

---

# 95. Scope Expansion Creates Frontier

When the globality scope expands, new proof obligations can appear:

$$
\boxed{
\partial_{D_1}^\ast
\supsetneq
\operatorname{Lift}
(\partial_{D_0}^\ast).
}
$$

---

# 96. NS Formal Frontier

For the Clay/formal NS domain:

$$
\boxed{
\partial_{\mathfrak N_{\rm C}}^\ast
}
$$

it only contains obligations that have legal route relevance to the formal target.

---

# 97. NS Physical Frontier

$$
\partial_{\mathfrak N_{\rm P}}^\ast
$$

will also contain model-to-world bridge obligations.

Therefore:

$$
\partial_{\mathfrak N_{\rm C}}^\ast
\neq
\partial_{\mathfrak N_{\rm P}}^\ast.
$$

---

# 98. NS Generalized Frontier

For:

$$
\mathfrak N_{\rm G}^{\Sigma}
$$

the frontier changes according to the signature $\Sigma$.

Without $\Sigma$, there is no unique generalized frontier.

---

# 99. NS Cross-Series Frontier

The relative graph of NS should integrate:

$$
\mathcal H_{\rm C1-C6},
\mathcal H_{\rm X72},
\mathcal H_{\rm DCRP},
\mathcal H_{\rm RFP},
\mathcal H_{\rm MORP},
\mathcal H_{\rm FCBP}.
$$

But route/obstruction quotienting must be done first.

---

# 100. NS Frontier Node Types

Typical frontier nodes:

- unresolved bridge;
- minimal survivor;
- conditional lemma;
- route completeness debt;
- representation ambiguity;
- scope mismatch;
- external theorem interface;
- potential counterexample class.

---

# 101. NS Obstruction Cover

In the future, one can establish:

$$
\mathcal O_{\rm NS}^{\rm active}
$$

and test:

$$
\mathsf{CoverCert}_{\Gamma_{\rm NS}}
(
\mathcal O_{\rm NS}^{\rm active},
Q_{\rm Clay}
).
$$

In the early stages, it is highly expected to be FAIL / PARTIAL.

---

# 102. NS Cut Discovery

One can search within the existing corpus for:

$$
C_{\rm NS}^{\rm candidate}
$$

such as high-confluence assumptions, bridges, carrier states, or recurrent survivor classes.

But a candidate cut is not a certified cut.

---

# 103. New Use for NS-203

The historical NS-203 corpus is no longer used solely for novelty / saturation analysis.

It can now serve as:

$$
\boxed{
\text{candidate frontier / cut / obstruction mining substrate}.
}
$$

---

# 104. Corpus-to-Closure Pipeline

$$
\boxed{
\text{Artifacts}
\to
\text{Claims}
\to
\text{Route Classes}
\to
\text{Obstruction Classes}
\to
\text{Frontier}
\to
\text{Candidate Cuts}
\to
\text{Certified Cuts}.
}
$$

---

# 105. Mining is Not Proof

Any automatic graph mining:

$$
\not\Rightarrow
\mathsf{CutCert}.
$$

formal / theorem-level audit remains necessary.

---

# 106. Exhaustion Proof Pattern A — Finite Branching

If:

$$
Q
\leftrightarrow
Q_1\vee\cdots\vee Q_n
$$

has a BDCert, and each branch is refuted at the theorem level, then:

$$
Q
$$

is negatively closed.

---

# 107. Exhaustion Proof Pattern B — Certified Cut

If:

1. CutCert holds;
2. Every cut node is refuted;
3. propagation is valid;
4. parent bridge is valid;

then parent negative closure can hold.

---

# 108. Exhaustion Proof Pattern C — Obstruction Cover

If:

$$
\mathcal O
$$

is a complete cover for the admissible route space, and route completeness is proven, then route exhaustion can be obtained.

---

# 109. Exhaustion Proof Pattern D — Representation Family

If every admissible representation family has route exhaustion, cross-representation completeness is still required.

---

# 110. Exhaustion Proof Pattern E — Scope Family

If the target carries a parameter family:

$$
\theta\in\Theta,
$$

the closure of each local $\theta$ does not automatically deduce uniform closure.

A uniformity certificate is required.

---

# 111. Uniform Exhaustion

$$
\boxed{
\forall\theta\in\Theta,
\quad
\mathsf{RECert}_{D,\Gamma}(Q_\theta)
}
$$

still does not necessarily deduce:

$$
\mathsf{RECert}
(
\forall\theta,Q_\theta
).
$$

A uniform proof object is required.

---

# 112. Compactness Bridge

In some cases, compactness can be used to promote local closure to uniform closure.

But compactness itself must be proven under the specified topology / parameterization.

---

# 113. Finite Cover Bridge

If the parameter space can be covered by finite certified regions:

$$
\Theta
=
\bigcup_{i=1}^n\Theta_i,
$$

and each region has a closure cert, it can form a finite-cover exhaustion.

---

# 114. Infinite Cover Debt

If only countably many cases are proven, but exhaustiveness cannot be proven, there is still a coverage debt.

---

# 115. Closure Measure Warning

This paper does not claim the existence of a natural probability measure:

$$
\mu(\Omega^{\rm math}).
$$

Therefore, one should not write:

> The NS proof space is 93% closed.

---

# 116. Operational Coverage

One can define relative to a specified finite graph:

$$
\operatorname{Cov}_{\Gamma}
=
1-
\frac{
M_{\partial}
}{
M_{\rm total}^{\Gamma}
}.
$$

But it must be labeled as:

$$
\boxed{
\Gamma\text{-relative operational metric}.
}
$$

---

# 117. Coverage is Not Truth Probability

$$
\boxed{
\operatorname{Cov}_{\Gamma}
\not\Rightarrow
P(Q\text{ true}).
}
$$

---

# 118. Closure Saturation

If new research events fail to generate new frontier classes or new cut escapes over a long period, it can be called:

$$
\mathsf{Sat}_{\rm Cl}(B;R,N).
$$

It is still regime-relative.

---

# 119. Saturation is Not Exhaustion

$$
\boxed{
\mathsf{Saturation}
\neq
\mathsf{Exhaustion}.
}
$$

---

# 120. Exhaustion is Not Closure

A certain route space may be exhausted, but the parent target remains unclosed.

Therefore:

$$
\boxed{
\mathsf{RouteExhaustion}
\neq
\mathsf{ClaimClosure}.
}
$$

---

# 121. Closure is Not Completeness

A claim being closed does not mean the surrounding theory is complete.

---

# 122. Relative Completeness

CSM most frequently uses:

$$
\boxed{
\text{relative completeness}
}
$$

rather than absolute completeness.

---

# 123. Closure Certificate Stack

A mature closure conclusion should carry:

$$
\boxed{
\mathsf{CertStack}
=
(
\mathsf{StatementCert},
\mathsf{ScopeCert},
\mathsf{RouteCert},
\mathsf{CutCert},
\mathsf{CoverCert},
\mathsf{BridgeCert},
\mathsf{DebtCert}
).
}
$$

---

# 124. Certificate Failure Modes

Failure at any layer should downgrade the status of the:

- claim;
- branch;
- exhaustion;
- cut;
- cover;

, rather than forcefully maintaining it as closed.

---

# 125. Certificate Composition

The composition of certificates itself requires compatibility.

One cannot assume:

$$
\mathsf{Cert}_1+\mathsf{Cert}_2
\Rightarrow
\mathsf{Cert}_{12}.
$$

---

# 126. Certificate Coherence

If different certs indicate different scope / assumptions / representation, a coherence audit must be performed.

---

# 127. Exhaustion Ledger

Each exhaustion event:

$$
e_{\rm exh}
=
\left\langle
Q,D,\Gamma,C,\mathcal O,
\mathsf{RECert},
\mathsf{Debt},
\nu,t
\right\rangle.
$$

---

# 128. Reopening Exhaustion Event

If a cut becomes invalid:

$$
e_{\rm reopen}
$$

references the old exhaustion event, rather than deleting it.

---

# 129. Relative Exhaustion as Versioned Object

$$
\boxed{
\mathsf{EXH}_{D,\Gamma}^{(\nu)}
}
$$

Different versions cannot be merged without certification.

---

# 130. Frontier Version

Similarly:

$$
\partial^{\ast,(\nu)}\mathfrak C(Q).
$$

---

# 131. Frontier Drift

Define between versions:

$$
\Delta\partial^\ast
=
\partial^{\ast,(\nu+1)}
\triangle
\partial^{\ast,(\nu)}.
$$

This allows analysis of newly added / disappeared / reopened route classes.

---

# 132. Closure Drift

The closure status distribution changes with versions:

$$
\Delta\sigma.
$$

---

# 133. Research Value of Negative Results

If a formal no-go can form a high-centrality obstruction cover, its value may be higher than many isolated positive lemmas.

---

# 134. Research Value of Reopening

Finding a counterexample or bridge that invalidates a high-centrality false cut can also be of extremely high value.

---

# 135. Proof-Space Geometry Is Not Truth Geometry

CSM must maintain:

$$
\boxed{
\text{proof-space geometry}
\neq
\text{truth-value geometry}.
}
$$

"Close" on the graph does not mean logically "close to truth."

---

# 136. Search Geometry Is Not Proof Geometry

Similarly:

$$
\boxed{
\text{search geometry}
\neq
\text{proof geometry}.
}
$$

An embedding cluster is not a theorem relation.

---

# 137. Representation Geometry Is Not Ontology

$$
\boxed{
\text{representation proximity}
\neq
\text{ontological identity}.
}
$$

---

# 138. Frontier Geometry Is Operational

The "geometry" in this paper primarily refers to:

- graph structure;
- quotient structure;
- reachability;
- cuts;
- covers;
- weighted neighborhoods;
- closure distance.

It does not automatically claim a smooth manifold structure.

---

# 139. Core Proposition I of Paper 03

## Relative Exhaustion Theorem Schema

If:

$$
\mathsf{RCCert}_{\Gamma}(Q)=\mathsf{PASS},
$$

$$
\mathsf{CutCert}_{\Gamma}(C,Q)=\mathsf{PASS},
$$

$$
\forall c\in C,
\quad
\sigma(c)=\mathsf{CLOSED}^{-},
$$

and all closure inheritances have certs, then:

$$
\boxed{
\Gamma
\vdash
\neg\operatorname{AdmissibleRoute}(Q).
}
$$

---

# 140. Core Proposition II of Paper 03

## Parent Closure Theorem Schema

If there is additionally:

$$
\mathsf{ParentBridgeCert}
:
\neg\operatorname{AdmissibleRoute}(Q)
\Rightarrow
\neg Q,
$$

then:

$$
\boxed{
D,\Gamma
\vdash
\neg Q.
}
$$

This is a relative-domain theorem conclusion.

---

# 141. Core Proposition III of Paper 03

## Reopening Theorem Schema

If:

$$
\mathsf{CutCert}^{(\nu)}
$$

depends on premise $A$, and the new version proves:

$$
\neg\mathsf{Valid}^{(\nu+1)}(A),
$$

then the old exhaustion cert must be marked as:

$$
\boxed{
\mathsf{STALE}
}
$$

and the frontier must be reconstructed.

---

# 142. Core Proposition IV of Paper 03

## False Exhaustion No-Go

If any of the following is missing:

- route completeness;
- cut completeness;
- obstruction cover;
- scope fidelity;
- parent bridge;

then deducing parent theorem closure from observed route closure is prohibited.

---

# 143. Core Proposition V of Paper 03

## Relative-Global Frontier Principle

Any "global frontier" must be written as:

$$
\boxed{
\partial^\ast_{D,\Gamma,\rho,\nu}
\mathfrak C(Q)
}
$$

indicating at least:

- domain;
- route grammar;
- representation policy;
- version.

---

# 144. NS Instantiation Prerequisites

Before truly establishing the NS closure graph, the following are required at minimum:

1. canonical artifact inventory;
2. claim extraction;
3. assumption extraction;
4. route quotient;
5. obstruction quotient;
6. scope normalization;
7. cross-series bridge audit;
8. status reclassification;
9. survivor extraction;
10. frontier reconstruction.

---

# 145. NS Version 1 Does Not Pursue Global Completeness

v0.1 only establishes:

$$
\boxed{
\partial^{\ast}_{\rm obs}
\mathfrak C_{\rm NS}
}
$$

namely the observed relative frontier.

---

# 146. NS Version 2

After the route grammar is established:

$$
\partial^{\ast}_{\Gamma_{\rm NS}}
\mathfrak C_{\rm NS}.
$$

---

# 147. NS Version 3

Only after route-completeness is supported by partial theorems can one discuss:

$$
\mathsf{EXH}_2^{\Gamma_{\rm NS}}.
$$

---

# 148. Initial High-Risk Errors for NS

Most necessary to avoid:

$$
\boxed{
\text{203 artifacts}
\Rightarrow
\text{203 independent routes}.
}
$$

---

# 149. Second High-Risk Error

$$
\boxed{
\text{many NO-GOs}
\Rightarrow
\text{NS false or regular}.
}
$$

---

# 150. Third High-Risk Error

$$
\boxed{
\text{one recurrent survivor}
\Rightarrow
\text{blow-up mechanism}.
}
$$

---

# 151. Fourth High-Risk Error

$$
\boxed{
\text{frontier small}
\Rightarrow
\text{near proof}.
}
$$

---

# 152. True Research Goal for NS

In the early stages, the pursuit is not:

$$
\mathsf{Proof}(Q_{\rm NS}).
$$

but rather to establish:

$$
\boxed{
\text{a faithful, typed, quotient-aware, reopenable relative closure geometry}.
}
$$

---

# 153. Relationship Between CSM Paper 03 and LSI-PSD

LSI-PSD has established:

- proof basins;
- semantic quotient;
- obstruction confluence;
- search regime limitation;
- observatory governance.

This paper absorbs its methodology but promotes frontier/cut/exhaustion to CSM closure operations.

---

# 154. Relationship Between CSM Paper 03 and UCT

The relative-global gate, bridge/debt/ledger of UCT are concretized here as:

- CutCert;
- CoverCert;
- RECert;
- ParentBridgeCert;
- reopening ledger.

---

# 155. Relationship Between CSM Paper 03 and General Graph Theory

This paper uses:

- directed graph;
- hypergraph;
- cut;
- transversal;
- cover;
- connected component;

as formal tools.

This paper does not claim to have invented these general concepts.

The newly added research focus of CSM lies in:

> binding them together with typed proof objects, scope contracts, obstruction certificates, reopening, debt, versioned ledgers, and relative-global theorem gates into the same operational framework.

---

# 156. Machine Schema — Frontier Record

```yaml
frontier_record:
  target_id:
  domain_id:
  route_grammar_id:
  representation_policy:
  version:
  raw_nodes: []
  quotient_route_classes: []
  components: []
  frontier_mass:
  closure_radius:
  debt_ids: []
  reopened_classes: []
  certificate_status:
```

---

# 157. Machine Schema — Cut Record

```yaml
cut_record:
  cut_id:
  target_id:
  cut_type:
  element_ids: []
  route_grammar_id:
  coverage_scope:
  cut_certificate_id:
  uncovered_route_classes: []
  quotient_policy:
  version:
  status:
```

---

# 158. Machine Schema — Obstruction Cover

```yaml
obstruction_cover:
  cover_id:
  target_id:
  obstruction_ids: []
  route_grammar_id:
  covered_route_classes: []
  uncovered_route_classes: []
  propagation_certificate_ids: []
  scope_fidelity:
  representation_fidelity:
  version:
  status:
```

---

# 159. Machine Schema — Relative Exhaustion

```yaml
relative_exhaustion:
  exhaustion_id:
  target_id:
  domain_id:
  route_grammar_id:
  exhaustion_level:
  route_completeness_certificate:
  cut_certificate:
  obstruction_cover_certificate:
  parent_bridge_certificate:
  representation_policy:
  scope_policy:
  debt_ids: []
  reopening_policy:
  version:
  status:
```

---

# 160. Validation Scenario A — Small raw frontier, bad quotient

If 100 raw frontier nodes are falsely merged into 1 class, then even if:

$$
|\partial^\ast|=1
$$

it is unacceptable.

A gold audit must catch the false quotient.

---

# 161. Validation Scenario B — True minimal cut

If all admissible routes pass through $A$, and CutCert holds, then:

$$
C=\{A\}
$$

is a true minimal cut.

---

# 162. Validation Scenario C — Observed-only cut

If $A$ only truncates all observed routes, then:

$$
\mathsf{CutCert}_{\rm obs}
$$

cannot be promoted to a grammar-relative CutCert.

---

# 163. Validation Scenario D — Complete obstruction cover

If route completeness holds and every route has a valid OPCert, then the obstruction cover PASSes.

---

# 164. Validation Scenario E — One uncovered survivor

If even one route class is not covered, then exhaustion FAILs.

That class becomes a minimal survivor candidate.

---

# 165. Validation Scenario F — Reopened cut

If the obstruction of a cut element is restricted by a new counterexample, the cut must be re-audited.

---

# 166. Validation Scenario G — Parent bridge missing

Route exhaustion is proven, but without:

$$
\neg\operatorname{RouteExists}\Rightarrow\neg Q,
$$

then the parent claim still cannot be CLOSED negative.

---

# 167. Validation Scenario H — Scope expansion

If expanding from one parameter region to the entire parameter space, the old cut does not automatically maintain completeness.

---

# 168. Validation Scenario I — Cross-representation escape

Exhaustion of representation $\rho_1$ does not exclude $\rho_2$.

If $\rho_2$ is admissible, the frontier reopens.

---

# 169. Validation Scenario J — NS observed frontier

After compiling NS `OPEN / SURVIVOR / STOP`, one can initially only obtain:

$$
\partial_{\rm obs}^\ast\mathfrak C_{\rm NS}.
$$

One must not claim an absolute frontier.

---

# 170. Validation Scenario K — NS scalar NO-GO

A scalar-budget NO-GO can become a high-centrality obstruction, but if other geometric/nonlocal routes do not pass through it, it is not a global cut.

---

# 171. Validation Scenario L — NS survivor concentration

If a large number of sibling branches are sealed, leaving only a few shear/polarization / ancient-profile classes, this is survivor compression, not theorem completion.

---

# 172. Non-Claim 1

This paper does not claim that all proof spaces naturally possess a unique graph representation.

---

# 173. Non-Claim 2

This paper does not claim that all mathematical routes can be effectively enumerated.

---

# 174. Non-Claim 3

This paper does not claim that a finite corpus can prove absolute route completeness.

---

# 175. Non-Claim 4

This paper does not claim that frontier mass is an objective natural measure.

---

# 176. Non-Claim 5

This paper does not claim that a minimal cut automatically equals the most important mathematical lemma.

---

# 177. Non-Claim 6

This paper does not claim that graph centrality equals theorem necessity.

---

# 178. Non-Claim 7

This paper does not claim that obstruction confluence equals unprovability.

---

# 179. Non-Claim 8

This paper does not claim that relative exhaustion equals absolute mathematical exhaustion.

---

# 180. Paper 04 Route

The next paper should address:

$$
\boxed{
\textbf{Closure Dynamics, Reopening, and Fixed-Point Evolution}
}
$$

Including:

- time-indexed closure states;
- schedule dependence;
- closure fixed points;
- reopening waves;
- debt discharge;
- closure hysteresis;
- frontier attractors;
- relative equilibrium;
- research routing dynamics.

---

# 181. Conclusion

This paper advances CSM from "being able to seal routes" to "being able to describe the remaining unclosed space."

Its core chain is:

$$
\boxed{
\text{Route Space}
\to
\text{Quotient Frontier}
\to
\text{Certified Cut}
\to
\text{Obstruction Cover}
\to
\text{Relative Exhaustion}
\to
\text{Parent Closure Gate}.
}
$$

The most important non-collapse is:

$$
\boxed{
\text{Observed Exhaustion}
\neq
\text{Admissible Exhaustion}
\neq
\text{Relative Mathematical Exhaustion}
\neq
\text{Absolute Mathematical Exhaustion}.
}
$$

Therefore, "step-by-step sealing of the proposition" truly possesses theorem-level significance only when route completeness, cut completeness, obstruction coverage, scope fidelity, and parent bridge all have certificates.

The goal of CSM is not to turn mathematical research into pretty graphs, but to ensure that:

$$
\boxed{
\text{every closure, every omission, every reopening, and every exhaustion declaration}
}
$$

can be precisely located within the relative mathematical space where it truly has the authority to operate.

---

## Appendix A — Core Invariants of Paper 03

1. raw frontier does not equal quotient frontier;
2. frontier contraction does not equal proof progress;
3. false contraction must be detectable;
4. cut must have a route coverage proof;
5. observed cut does not equal admissible cut;
6. cut does not equal obstruction cover;
7. obstruction cover must have an OPCert;
8. survivor does not equal successful route;
9. route exhaustion does not equal parent claim closure;
10. exhaustion ladder cannot be skipped;
11. representation exhaustion must not cross representations without certification;
12. scope-local exhaustion must not be promoted without certification;
13. exhaustion certificate can become stale;
14. reopening must reconstruct the frontier;
15. relative-global frontier must indicate domain / grammar / representation / version.

---

## Appendix B — Series Dependencies

### Paper 00
- Relative-Global Closure Space
- status / debt / ledger
- route-completeness obligation

### Paper 01
- Globality Typing
- Scope Contract
- Domain Stratification
- Globality Promotion

### Paper 02
- Typed Closure Hypergraph
- Obstruction Propagation
- Reopening
- Branch Decomposition
- Route Exhaustion Machinery

### Paper 03
- Frontier Geometry
- Cut Sets
- Obstruction Covers
- Exhaustion Ladder
- Relative Exhaustion Certificate
- Parent Closure Gate

---

**END OF CSM PAPER 03 v0.1**