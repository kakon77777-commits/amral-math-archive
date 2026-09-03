# CSM Paper 00
# Formal Foundations of Closure-Space Mathematics
## Closure-Space Mathematics: Formal Foundations for Relative-Global Mathematical Closure

**Version:** v0.1  
**Date:** 2026-08-27  
**Series:** Closure-Space Mathematics / CSM  
**Status:** Foundational Paper / Formal Foundations  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** `$...$` and `$$...$$`  
**Research Status:** Theoretical framework, definition system, formal propositions, and subsequent proof plans; not a completed proof of any unsolved mathematical problem.

---

# Abstract

This paper presents the first version of the formal foundations for **Closure-Space Mathematics** (CSM). The core problem of CSM is not "how to generate another proof route," but rather: after a long-term mathematical research program has accumulated a massive amount of propositions, assumptions, proof attempts, counterexamples, obstructions, bridges, representations, and local successes and failures, can these research states be organized into a verifiable, replayable, and updatable relative-global mathematical space? Furthermore, can we provide explicit, typed determinations of which regions within this space are closed, which remain open, and which are merely locally blocked?

CSM absorbs but is not identical to two existing internal theoretical lines. The first is Logic-Space Integration and Proof-Space Dynamics (LSI-PSD), which has established the semantic quotient, route graph, proof basin, obstruction confluence, theorem-strength preorder, and Proof-Space Observatory. The second is UGC/CUR / Unified Closure Theory (UCT), which established typed non-collapse, generative closure, reachability, transformation closure, bridge certificate, debt, and ledger. This paper elevates both into a new mathematical research object: **the closure space itself**.

The first core principle of this paper is:

$$
\boxed{
\text{Observed Proof Space}
\neq
\text{Admissible Proof Space}
\neq
\text{Mathematical Reality}.
}
$$

Therefore, this paper primarily defines **relative-global closure**, rather than masquerading a finite corpus, finite search regime, or finite graph structure as the entirety of all possible mathematical routes.

The second core principle is:

$$
\boxed{
\text{Route Closure}
\neq
\text{Theorem Proof}.
}
$$

If a researcher wishes to promote "all candidate routes are blocked" to a theorem, they must provide an additional route-completeness / decomposition-completeness certificate, proving that the enumerated and quotiented route family is complete with respect to the designated admissible mechanism class for the target proposition.

The third core principle is the **Globality Typing Principle**: any claim of "globality" must specify on which axis it is global. Using Navier--Stokes as the first large-scale experimental ground, this paper distinguishes between Clay/formal mathematical NS, physical realization NS, and the generalized NS-like equation family, asserting that:

$$
\boxed{
\text{Global-in-time}
\neq
\text{Global-across-equation-family}
\neq
\text{Global-across-physical-realizations}.
}
$$

Finally, this paper defines the typed closure-space object, nodes and hyperedges, closure actions, frontier, closure debt, reopening, relative-global closure grade, route-completeness certificate, and the first-version data model of the NS Relative-Global Closure Space. Subsequent CSM series will progressively project the positive results, NO-GOs, survivors, OPENs, and conditional bridges from the existing NS C1--C6, X72, DCRP, MORP, RFP, FCBP, and Proof Asset Map into the same closure space, truly transforming "researched routes" into computable mathematical assets.

---

# 0. Research Status and Non-Claims

This paper does not claim that:

1. The unique, natural proof space for all mathematical problems has been established;
2. All proof routes for any mathematical proposition can be finitely enumerated;
3. Graph / hypergraph representations are identical to mathematical ontology;
4. Semantic quotients can be automatically completed by embeddings or LLM similarity;
5. Multiple routes hitting the same obstruction proves a proposition false or unprovable;
6. The closure of a certain basin implies the closure of the entire proof space;
7. Relative-global closure automatically equals absolute mathematical closure;
8. Closure operators on all CSM layers automatically satisfy the extensivity, monotonicity, and idempotence of traditional closure algebra;
9. The global regularity proof of Clay Navier--Stokes equates to a global proof of all fluid phenomena in the physical world;
10. The generalized NS-like family already has a unique canonical definition;
11. CSM can replace theorem-level verification;
12. CSM has solved Navier--Stokes existence and smoothness.

This paper only claims that:

- Long-term research states can be organized into a typed multilayer mathematical graph;
- Different closure types must maintain type differentiation;
- "Observed," "route-blocked," "proven," "falsified," and "relative-globally closed" must be separated;
- Closure promotion must carry a certificate;
- Globality must be typed;
- Relative-global closure can become an operable, auditable, and progressively approximable research object.

---

# 1. From Proof Routes to Closure Spaces

Traditional mathematical papers typically compress the research process into:

$$
A_0
\Rightarrow
A_1
\Rightarrow
\cdots
\Rightarrow
Q.
$$

Failed attempts are usually only left as narrative descriptions, or disappear entirely.

However, long-term AI mathematical research generates a massive amount of:

- theorem candidates;
- lemmas;
- assumptions;
- proof routes;
- representations;
- counterexamples;
- obstructions;
- NO-GOs;
- survivors;
- conditional theorems;
- bridges;
- failed bridges;
- reopened routes;
- repaired theorems;
- descendant problems.

The first transformation of CSM is:

$$
\boxed{
\text{Research History}
\longrightarrow
\text{Mathematical State Space}.
}
$$

This state space preserves not only the answers, but also "which routes were opened, blocked, conditionalized, repaired, quotiented, or reopened, and why."

---

# 2. Three Spaces Must Not Collapse

For a target proposition $Q$, three levels are defined.

## 2.1 Mathematical Possibility Space

Let:

$$
\Omega^{\rm math}(Q)
$$

denote the entire mathematically possible proof / counterexample / reduction / representation / mechanism space related to $Q$.

This paper does not assume that it can be effectively enumerated, nor does it assume that it naturally possesses a unique graph representation.

## 2.2 Admissible Route Space

Under a declared formal domain $D$, proof regime $\Theta$, language, and admissibility rule $\mathcal A$:

$$
\Omega^{\rm adm}_{D,\Theta,\mathcal A}(Q)
\subseteq
\Omega^{\rm math}(Q).
$$

It represents the proof objects, transformations, reductions, and certificates considered legal under the current problem setting.

## 2.3 Observed Research Space

Under a search regime $R$, resource bound $N$, and history $H$:

$$
\Omega^{\rm obs}_{R,N,H}(Q).
$$

It is the portion that is actually researched, scraped, generated, verified, or recorded.

Usually, one can only assume:

$$
\Omega^{\rm obs}_{R,N,H}(Q)
\subseteq
\Omega^{\rm adm}_{D,\Theta,\mathcal A}(Q),
$$

and cannot inversely assume the two are equal.

Therefore, the foundational non-collapse of CSM is:

$$
\boxed{
\Omega^{\rm obs}
\neq
\Omega^{\rm adm}
\neq
\Omega^{\rm math}
}
$$

unless an independent certificate establishes equivalence.

---

# 3. Relative Globality, Not Absolute Globality

CSM's use of "relative-global" is deliberate.

Define:

$$
\mathfrak C^{\rm rel}_{D,\Theta,\mathcal A,R,N,H}(Q)
$$

as the closure-space state obtained through audited quotients and certified closure actions under a specified domain, proof regime, admissibility rule, search regime, resources, and history.

Here, "global" means:

> A globalized integration over **all structures currently admissible within the declared scope and covered by the closure procedure**.

It does not mean:

$$
\mathfrak C^{\rm rel}
=
\Omega^{\rm math}(Q).
$$

Therefore:

$$
\boxed{
\text{Relative Globality}
\neq
\text{Absolute Completeness}.
}
$$

---

# 4. Globality Typing Principle

"Global" is not a single boolean value.

For any claim $Q$, define the scope / globality vector:

$$
\mathsf{GScope}(Q)
=
\left\langle
G_t,
G_x,
G_{\rm eq},
G_{\rm sol},
G_{\rm data},
G_{\rm bdry},
G_{\rm force},
G_{\rm reg},
G_{\rm rep},
G_{\rm phys},
G_{\rm proof}
\right\rangle.
$$

Each axis represents at least:

- $G_t$: time scope;
- $G_x$: spatial domain;
- $G_{\rm eq}$: equation / model family;
- $G_{\rm sol}$: solution notion;
- $G_{\rm data}$: initial / boundary data class;
- $G_{\rm bdry}$: boundary family;
- $G_{\rm force}$: forcing family;
- $G_{\rm reg}$: regularity class;
- $G_{\rm rep}$: representation family;
- $G_{\rm phys}$: physical realization / interpretation domain;
- $G_{\rm proof}$: proof system / admissibility regime.

Therefore:

$$
\boxed{
\text{Global-in-time}
\not\Rightarrow
\text{Global-across-equations}.
}
$$

$$
\boxed{
\text{Global-across-equations}
\not\Rightarrow
\text{Global-across-physical-realizations}.
}
$$

Any "global" claim without a marked scope vector belongs, in CSM, at least to:

$$
\mathsf{ILL\_SCOPED}.
$$

---

# 5. Basic Objects of CSM

The first version of the closure space is defined as:

$$
\boxed{
\mathfrak C
=
\left\langle
D,
V,
E,
\tau_V,
\tau_E,
\sim,
\preceq,
\sigma,
\mathfrak O,
\partial\mathfrak C,
\mathsf{Cert},
\mathsf{Debt},
\mathsf{Ledger}
\right\rangle.
}
$$

Where:

- $D$: declared mathematical domain;
- $V$: typed nodes;
- $E$: typed edges / hyperedges;
- $\tau_V$: node type;
- $\tau_E$: edge type;
- $\sim$: audited equivalence / quotient family;
- $\preceq$: strength / refinement preorder;
- $\sigma$: epistemic / closure status;
- $\mathfrak O$: closure action family;
- $\partial\mathfrak C$: active frontier;
- $\mathsf{Cert}$: proof / bridge / closure certificates;
- $\mathsf{Debt}$: outstanding proof obligations;
- $\mathsf{Ledger}$: versioned research history.

---

# 6. Why Use a Typed Hypergraph

Edges in a standard graph typically have only one source and one target.

But mathematical derivations are often:

$$
A_1\land A_2\land A_3
\Rightarrow
Q.
$$

Therefore, a canonical edge should allow:

$$
e:
\{v_1,\ldots,v_k\}
\longrightarrow
v'.
$$

At the same time, different edges possess different semantics.

The first version of edge types:

$$
\tau_E(e)
\in
\{
\mathsf{IMPLIES},
\mathsf{DEPENDS},
\mathsf{CONTRADICTS},
\mathsf{GENERALIZES},
\mathsf{SPECIALIZES},
\mathsf{REFINES},
\mathsf{WEAKENS},
\mathsf{REPRESENTS},
\mathsf{BRIDGES},
\mathsf{BLOCKS},
\mathsf{REOPENS},
\mathsf{INHERITS},
\mathsf{REPAIRS},
\mathsf{WITNESSES},
\mathsf{FALSIFIES},
\mathsf{TRANSFERS}
\}.
$$

Different edges must not be treated as the same kind of implication simply because they are all drawn as arrows on a graph.

---

# 7. Node Type System

The first version of nodes includes at least:

$$
\tau_V(v)
\in
\{
\mathsf{Problem},
\mathsf{Claim},
\mathsf{Assumption},
\mathsf{Lemma},
\mathsf{Construction},
\mathsf{Counterexample},
\mathsf{Representation},
\mathsf{RouteState},
\mathsf{Obstruction},
\mathsf{Basin},
\mathsf{Bridge},
\mathsf{Domain},
\mathsf{Certificate},
\mathsf{Debt},
\mathsf{Boundary}
\}.
$$

CSM does not treat paper files as basic mathematical nodes.

An artifact is a provenance container; the true units of computation are the typed mathematical objects within it.

---

# 8. Closure Status Type System

Define:

$$
\sigma(v)
\in
\{
\mathsf{OPEN},
\mathsf{CLOSED}^{+},
\mathsf{CLOSED}^{-},
\mathsf{BLOCKED},
\mathsf{CONDITIONAL},
\mathsf{UNKNOWN},
\mathsf{INDEPENDENT}_{\mathcal T}
\}.
$$

## 8.1 Positive Closure

$$
\mathsf{CLOSED}^{+}
$$

Indicates that the specified claim has a valid proof certificate within the scope.

## 8.2 Negative Closure

$$
\mathsf{CLOSED}^{-}
$$

Indicates that the claim has been ruled out by a counterexample, proof of contradiction, or theorem-level no-go.

## 8.3 Blocked

$$
\mathsf{BLOCKED}
$$

Is a route-level / mechanism-level state:

> Under the current assumptions, representation, bridges, and theorem set, this route cannot complete the specified promotion.

It is not equal to:

$$
\mathsf{CLOSED}^{-}.
$$

## 8.4 Conditional

$$
\mathsf{CONDITIONAL}
$$

Indicates that:

$$
A_1\land\cdots\land A_k
\Rightarrow
Q
$$

is proven, but at least one $A_i$ remains unclosed.

## 8.5 Relative Independence

$$
\mathsf{INDEPENDENT}_{\mathcal T}
$$

Can only be used when a formal theory $\mathcal T$ has been explicitly specified and an independence proof exists.

"AI keeps failing" is not an independence certificate.

---

# 9. More Than One Kind of Closure

CSM decomposes closure into multiple typed actions, rather than defaulting to a single $\operatorname{Cl}$.

First version:

$$
\mathfrak O
=
\{
\mathsf{Cl}_{\rm imp},
\mathsf{Cl}_{\rm dep},
\mathsf{Cl}_{\rm quot},
\mathsf{Cl}_{\rm obs},
\mathsf{Cl}_{\rm bridge},
\mathsf{Cl}_{\rm gen},
\mathsf{Cl}_{\rm cert}
\}.
$$

These actions can interact with each other, but are not presumed to be isomorphic.

---

# 10. Implication Closure

Given a node set $S$, if there exists a verified implication hyperedge:

$$
\{v_1,\ldots,v_k\}
\Rightarrow
v',
$$

and:

$$
\{v_1,\ldots,v_k\}
\subseteq
S,
$$

then:

$$
v'
\in
\mathsf{Cl}_{\rm imp}(S).
$$

However, implication closure only propagates proven implications.

It must not treat:

- semantic similarity;
- empirical correlation;
- heuristic plausibility;
- representation proximity;

as implication edges.

---

# 11. Dependency Closure

If claim $Q$ depends on:

$$
A_1,\ldots,A_k,
$$

then dependency closure preserves:

$$
\operatorname{Dep}(Q)
=
\{A_1,\ldots,A_k\}
$$

and its recursive ancestors.

If an upstream assumption is falsified, descendant claims should not be automatically deleted, but should instead enter:

$$
\mathsf{REQUIRES\_DESCENDANT\_AUDIT}.
$$

Because some descendants may possess independent reproofs or weaker surviving formulations.

---

# 12. Quotient Closure

LSI-PSD has pointed out that raw artifact count does not equal route count.

CSM defines multiple equivalence relations:

$$
\sim_{\rm prop},
\qquad
\sim_{\rm route},
\qquad
\sim_{\rm obs},
\qquad
\sim_{\rm evid},
\qquad
\sim_{\rm rep}.
$$

Therefore:

$$
\mathsf{Cl}_{\rm quot}
$$

is not "deleting duplicates," but rather establishing quotient classes while preserving the original provenance.

Core rule:

$$
\boxed{
\text{Mathematical Redundancy}
\not\Rightarrow
\text{Search-Dynamical Redundancy}.
}
$$

---

# 13. Obstruction Closure

Let $O$ be a proven obstruction on a certain route family.

The most dangerous error is:

$$
O(R_1)
\Rightarrow
O(R_2)
$$

simply because the two "look similar".

CSM requires an obstruction transfer certificate:

$$
\mathsf{ObsTransferCert}
(O,R_1\to R_2).
$$

The certificate must at least specify:

- whether the target statements are consistent;
- whether the assumptions are included;
- whether the obstruction mechanism is invariant;
- whether the representation change is sound;
- whether the domains are compatible;
- whether the bridge is sound;
- whether counterexamples are excluded.

Only then can $\mathsf{Cl}_{\rm obs}$ legally propagate the barrier to descendant routes.

---

# 14. Bridge Closure

Promotions across domains, representations, proof systems, or model classes must be mediated through bridges.

General form:

$$
X
\xrightarrow{\mathsf{BridgeCert}}
Y.
$$

CSM does not fix the bridge backend.

It can be realized by:

- equivalence theorem;
- reduction;
- interpretation;
- conservative extension;
- functor / morphism;
- lifting theorem;
- model correspondence;
- asymptotic limit theorem.

But without a bridge certificate:

$$
\boxed{
\text{Similarity}
\not\Rightarrow
\text{Transfer Permission}.
}
$$

---

# 15. Generative Closure of Research States

Inspired by UCT generative closure, CSM defines proof-state generative closure:

$$
\operatorname{GenCl}^{\rm proof}_{D,T}
(S\mid\Theta).
$$

It represents:

> The family of research/proof states that can be legally generated from the current state $S$, under specified operators, admissibility rules, resources, and proof regimes.

It includes:

- theorem descendants;
- refined assumptions;
- alternative representations;
- counterexample targets;
- bridge candidates;
- obstruction descendants;
- reopened routes.

But:

$$
\boxed{
\operatorname{GenCl}^{\rm proof}
\neq
\Omega^{\rm math}(Q).
}
$$

Generative capacity is not a complete proof of mathematical possibility.

---

# 16. Closure-on-Closure Dynamics

The research space will change due to new proofs, new counterexamples, new bridges, and new representations.

Define:

$$
\mathfrak C_{t+1}
=
\mathfrak U_t
\left(
\mathfrak C_t,
 e_t
\right),
$$

where $e_t$ can be:

- theorem certification;
- counterexample;
- obstruction proof;
- assumption revision;
- quotient merge / split;
- bridge creation / invalidation;
- domain refinement;
- route reopen;
- target rewrite.

Therefore, CSM's closure is a **dynamic, versioned closure**, not a permanently unalterable blacked-out node.

---

# 17. Reopening Principle

A route at time $t$ might be:

$$
\sigma_t(R)=\mathsf{BLOCKED}.
$$

But if later:

- assumptions change;
- representations change;
- new theorems appear;
- the applicability conditions of the obstruction are weakened;
- new bridges are established;

then there can exist:

$$
\sigma_{t+1}(R)=\mathsf{OPEN}.
$$

Therefore:

$$
\boxed{
\text{Research-Route Blockage is not generally monotone.}
}
$$

This must be separated from theorem truth status.

---

# 18. Different Monotonicities of Theorem Closure and Search Closure

If $Q$ already has a valid proof in a fixed formal system, and subsequent work is merely a conservative extension, then its proof certificate can remain valid.

But search closure may be reopened.

Thus, CSM distinguishes between:

$$
\mathsf{LogicalClosure}
$$

and:

$$
\mathsf{SearchClosure}.
$$

The former handles theorem validity; the latter handles whether the current route family still holds research value and reachability.

The two must not collapse.

---

# 19. Frontier

Define the active frontier:

$$
\partial\mathfrak C(Q)
$$

as the nodes/route classes currently related to the target $Q$ and satisfying at least one of the following:

- not yet positively closed;
- not yet negatively closed;
- has legal incoming / outgoing proof transitions;
- conditional premises remain unresolved;
- obstructions are not yet transferable;
- bridge debts remain unpaid;
- representation completeness is not established.

But raw frontier size is meaningless.

Therefore, define the quotient frontier:

$$
\boxed{
\partial^{\ast}\mathfrak C(Q)
=
\partial\mathfrak C(Q)
/\sim_{\rm route,obs}.
}
$$

What truly needs to be reduced are the audited frontier classes, not the document count.

---

# 20. Closure Debt

Any closure claim can carry a debt vector:

$$
\mathsf{Debt}(Q)
=
\left
\langle
\delta_{\rm assumption},
\delta_{\rm bridge},
\delta_{\rm quotient},
\delta_{\rm witness},
\delta_{\rm obstruction},
\delta_{\rm representation},
\delta_{\rm completeness},
\delta_{\rm domain},
\delta_{\rm verification}
\right\rangle.
$$

Among which the most important is:

$$
\delta_{\rm completeness}.
$$

As long as route completeness has not been established, relative-global route closure cannot be promoted to absolute theorem closure.

---

# 21. Route-Completeness Certificate

Define:

$$
\boxed{
\mathsf{RCCert}
(Q;D,\Theta,\mathcal A)
}
$$

as the route-completeness certificate.

Minimum obligations:

1. Explicitly define the admissible route grammar;
2. Prove that all specified mechanism classes can be represented by the grammar;
3. Prove that the quotient will not merge non-equivalent routes;
4. Prove the completeness of the representation family or provide scope limitations;
5. Bridge family is complete or explicitly limited;
6. Obstruction transfer soundness;
7. Target fidelity;
8. Formal verification / independent proof witness;
9. Explicitly record debt for uncovered route classes.

Without $\mathsf{RCCert}$, the following is prohibited:

$$
\text{all observed routes blocked}
\Rightarrow
\text{all mathematical routes blocked}.
$$

---

# 22. Relative-Global Closure Grade

First version definitions:

### RGC-0 — Ill-Typed

Scope, target, or node/edge typing is incomplete.

### RGC-1 — Local Closure

A single lemma, route segment, or local mechanism is closed.

### RGC-2 — Basin Closure

The active frontier within a quotient-aware proof basin is closed, but outside the basin remains unknown.

### RGC-3 — Observed Relative-Global Closure

In the audited quotient space of the declared corpus / regime, all observed frontiers are closed.

### RGC-4 — Admissible Relative-Global Closure Candidate

A route/decomposition completeness certificate exists, such that the specified admissible mechanism space is covered and closed.

Even RGC-4 is only relative to:

$$
(D,\Theta,\mathcal A).
$$

Therefore:

$$
\boxed{
\mathsf{RGC4}
\not\Rightarrow
\text{absolute mathematical completeness}.
}
$$

---

# 23. Closure Proof Principle

CSM does not negate the traditional proof format of a single successful proof path.

If there is:

$$
P:
A_0\Rightarrow\cdots\Rightarrow Q
$$

and the proof verifier accepts it, then $Q$ can be positively closed.

What CSM adds is another type of research structure:

> If the failure / counterexample / singularity formation mechanism of a target can be proven to have a complete decomposition, and every branch of the decomposition is blocked by a theorem-level obstruction, then a new proof route can be formed by closure-space exhaustion.

But the key remains:

$$
\boxed{
\text{Exhaustion Proof}
=
\text{Complete Decomposition}
+
\text{Certified Branch Closures}.
}
$$

Merely "all the branches we thought of are dead" is not enough.

---

# 24. No-Premature-Closure Principle

No node may be promoted to $\mathsf{CLOSED}^{-}$ for the following reasons:

- unable to search for new routes;
- multiple models all fail;
- novelty is very low;
- basin recurrence is very high;
- paper count is very high;
- obstruction confluence is very high;
- a certain representation fails long-term.

The correct state is at most:

$$
\mathsf{BLOCKED},
\quad
\mathsf{SATURATED}_{\rm rel},
\quad
\mathsf{UNKNOWN}.
$$

This is the epistemic firewall of CSM.

---

# 25. No-Premature-Quotient Principle

Two routes can only be quotiented under sufficient conditions.

If:

$$
R_1
\sim_{\rm semantic}
R_2
$$

but the representation has different success rates for the prover / theorem backend, then:

$$
[R_1]_{\rm math}
=
[R_2]_{\rm math}
$$

can still simultaneously have:

$$
[R_1]_{\rm search}
\neq
[R_2]_{\rm search}.
$$

Therefore, CSM maintains multi-layered quotients.

---

# 26. Theorem-Strength and Route-Refinement Order

If:

$$
Q_1\Rightarrow Q_2,
$$

but:

$$
Q_2\not\Rightarrow Q_1,
$$

define:

$$
Q_1\succeq Q_2.
$$

Similarly, if route $R_2$ contains all legal steps of $R_1$ and additionally handles more general conditions, one can write:

$$
R_1\preceq R_2.
$$

Therefore, the closure space simultaneously contains quotient classes and a partial/refinement order.

It is not a simple cluster graph.

---

# 27. Obstruction Confluence in CSM

If multiple genuinely distinct routes:

$$
[R_i]_{\rm route}
\neq
[R_j]_{\rm route}
$$

are all reduced to the same audited obstruction class:

$$
[O(R_i)]_{\rm obs}
=
[O^{\star}]_{\rm obs},
$$

then an obstruction confluence is formed.

But:

$$
\boxed{
\text{High Confluence}
\not\Rightarrow
\text{Absolute Barrier}.
}
$$

It merely raises the priority of that obstruction becoming the next research target.

---

# 28. Closure-Space Ledger

Every state change must be written to:

$$
\mathsf{Ledger}_t.
$$

Minimum event fields:

$$
\mathsf{Event}
=
\left\langle
\mathsf{id},
\mathsf{time},
\mathsf{source},
\mathsf{target},
\mathsf{operation},
\mathsf{assumptions},
\mathsf{before},
\mathsf{after},
\mathsf{certificate},
\mathsf{debt},
\mathsf{version}
\right\rangle.
$$

Thus:

- theorem repair;
- obstruction invalidation;
- route reopen;
- quotient split;
- target rewrite;

are all traceable.

---

# 29. Differences Between CSM and Proof-Space Observatory

The role of the Proof-Space Observatory is:

$$
\boxed{
\text{Observe, measure, replay, and route research space}.
}
$$

The role of CSM is:

$$
\boxed{
\text{Define closure-space objects and the mathematics of their legal evolution}.
}
$$

Therefore:

$$
\text{PSO}
\subseteq
\text{possible CSM instrumentation backends},
$$

But:

$$
\text{CSM}
\neq
\text{PSO software specification}.
$$

---

# 30. Relationship Between CSM and UCT

UCT establishes:

$$
\operatorname{GenCl},
\qquad
\mathsf{Reach},
\qquad
\operatorname{TransCl},
\qquad
\mathsf{BridgeCert},
\qquad
\mathsf{Debt},
\qquad
\mathsf{Ledger}.
$$

CSM projects these concepts onto the mathematical research domain, but does not claim they are completely isomorphic.

Primary correspondences:

$$
\operatorname{GenCl}
\rightsquigarrow
\operatorname{GenCl}^{\rm proof},
$$

$$
\mathsf{Reach}
\rightsquigarrow
\text{proof-state / theorem-state reachability},
$$

$$
\operatorname{TransCl}
\rightsquigarrow
\text{legal proof-state transformations},
$$

$$
\mathsf{BridgeCert}
\rightsquigarrow
\text{cross-domain / cross-representation transfer certificates}.
$$

CSM maintains:

$$
\boxed{
\text{Analogy}
\neq
\text{Identity}.
}
$$

---

# 31. Three-Domain Separation of Navier--Stokes

The first large-scale experimental ground for CSM is Navier--Stokes.

Define three distinct target domains.

## 31.1 Formal Clay / Mathematical NS

Denoted as:

$$
\mathfrak N_{\rm C}.
$$

It represents Navier--Stokes existence / smoothness type targets under a fixed mathematical formulation.

The key is that:

$$
\text{equation},
\quad
\text{dimension},
\quad
\text{domain},
\quad
\text{data class},
\quad
\text{solution notion},
\quad
\text{regularity target}
$$

are all typed.

## 31.2 Physical NS Realization Domain

Denoted as:

$$
\mathfrak N_{\rm P}.
$$

It handles the correspondence between mathematical models and actual physical fluids, approximations, scales, measurable quantities, constitutive assumptions, and effective theoretical ranges.

Therefore:

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm P}).
}
$$

This is not a negation of mathematical NS, but a refusal to automatically promote formal theorems to the entirety of physical reality.

## 31.3 Generalized NS-Like Equation Family

Denoted as:

$$
\mathfrak N_{\rm G}^{\Sigma}.
$$

where $\Sigma$ is the family signature.

The first version only requires that $\Sigma$ can declare:

- transport / advection operator;
- incompressibility or generalized constraint;
- diffusion / dissipation operator;
- pressure / projection / nonlocal coupling;
- nonlinear interaction order;
- forcing;
- domain / boundary;
- scale-transfer structure;
- solution / regularity class.

Formally, one can write:

$$
\mathcal E
\in
\mathfrak N_{\rm G}^{\Sigma}
$$

if $\mathcal E$ satisfies the signature predicate:

$$
\Sigma(\mathcal E)=1.
$$

This is still a **relative generalized family**, not "all fluid equations" or "all physical PDEs".

---

# 32. NS Globality Non-Collapse

Therefore:

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm G}^{\Sigma}).
}
$$

Similarly:

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm G}^{\Sigma})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm P}).
}
$$

Unless there is an additional bridge.

Thus, the NS domain graph should be written as a typed graph, rather than simple set inclusions:

$$
\mathfrak N_{\rm C}
\xrightarrow{\mathsf{GeneralizationBridge}}
\mathfrak N_{\rm G}^{\Sigma},
$$

and:

$$
\mathfrak N_{\rm C}
\xleftrightarrow[\mathsf{Idealization}]
{\mathsf{Interpretation}}
\mathfrak N_{\rm P}.
$$

Each edge requires an independent certificate.

---

# 33. Why Clay NS Appears Global but Remains Restricted

The "global" in Clay-type global regularity primarily targets time continuation and solution regularity for a fixed formulation.

Its scope is large, but it still fixes:

- equation family;
- dimension;
- incompressibility;
- viscosity regime;
- domain / boundary alternatives;
- solution notion;
- data assumptions.

Therefore:

$$
\boxed{
\text{Large Scope}
\neq
\text{Unbounded Scope}.
}
$$

More importantly:

$$
\boxed{
\text{Global in one scope axis}
\neq
\text{Global in every scope axis}.
}
$$

This is CSM's first formal correction to the term "global".

---

# 34. NS Relative-Global Closure Space

Define:

$$
\boxed{
\mathfrak C_{\rm NS}^{\rm rel}
}
$$

as the relative-global closure space for Navier--Stokes research.

The first version's data sources may include:

- ETN--X Integration;
- C1 / C2;
- C3--C6;
- X72;
- DCRP;
- RFP;
- MORP;
- FCBP;
- Proof Asset Map;
- theorem-check scripts;
- external theorem anchors;
- later corrections and supersessions.

However, these artifacts must first be decomposed into typed objects before entering the graph.

---

# 35. The New Meaning of "Blocked Routes" in NS

Suppose a study yields:

$$
\text{scalar additive budget}
\not\Rightarrow
\text{blow-up exclusion}.
$$

CSM does not mark the entire Navier--Stokes target as a failure.

It only establishes:

$$
O_{\rm scalar-budget}.
$$

on the corresponding route class. And sets:

$$
\sigma(R_{\rm scalar})
=
\mathsf{BLOCKED}
$$

or, when theorem-level counterexamples are sufficient:

$$
\sigma(Q_{\rm scalar-sufficiency})
=
\mathsf{CLOSED}^{-}.
$$

Other routes are unaffected, unless an obstruction-transfer certificate holds.

---

# 36. Survivor is Not a Failure, but Frontier Compression

A large number of results in NS C3--C6, X72, and DCRP ultimately are not theorem completions, but rather:

$$
R_1\vee R_2\vee\cdots\vee R_k
\longrightarrow
S_1\vee\cdots\vee S_m,
\qquad
m<k.
$$

CSM defines this kind of result as:

$$
\boxed{
\text{Frontier Compression}.
}
$$

If the compression has a theorem-level proof, it is itself a positive mathematical asset.

Even if the final target is still OPEN, the frontier volume / complexity has been reduced.

---

# 37. Closure Volume Does Not Equal Node Count

Let the raw frontier have:

$$
N
$$

nodes.

If after quotienting there are only:

$$
N_{\rm eff}
$$

independent route / obstruction classes, then the true closure-space size should be based on:

$$
N_{\rm eff},
$$

rather than $N$.

Future research may investigate:

$$
\operatorname{Vol}_{\rm CSM}
\left(
\partial^{\ast}\mathfrak C
\right),
$$

but this paper does not presume the existence of a unique natural measure.

---

# 38. Closure Density and Saturation

A local basin $B$ can have a high closure density:

$$
\rho_{\rm cl}(B)
=
\frac{
\text{audited closed classes}
}{
\text{audited reachable classes}
}.
$$

But:

$$
\boxed{
\rho_{\rm cl}(B)\to1
\not\Rightarrow
\Omega^{\rm math}(Q)=B.
}
$$

Therefore, saturation can still only be a relative observational state, unless a completeness certificate intervenes.

---

# 39. Closure Boundary as Research Target

In CSM, the next step in research is no longer simply selecting the "TODOs of the latest paper".

One can perform priority ranking on:

$$
\partial^{\ast}\mathfrak C(Q)
$$

Candidate priority function:

$$
\mathsf{Priority}(v)
=
F
\left(
\mathsf{Centrality},
\mathsf{Confluence},
\mathsf{DependencyMass},
\mathsf{BridgePotential},
\mathsf{DebtReduction},
\mathsf{ReopenGain}
\right).
$$

This allows AI to choose:

> Which boundary node, once closed, will block the most descendant space or open the most new legal routes.

---

# 40. Closure as a Search Strategy

CSM's research strategy can be upgraded from:

$$
\text{find one promising path}
$$

to:

$$
\boxed{
\text{maximize certified closure gain per unit research cost}.
}
$$

However, cost / gain remain parameters of the research regime, not mathematical truths themselves.

---

# 41. Minimum Closure Certificate

Any closure event must carry at least:

```yaml
closure_id:
target_id:
closure_type:
domain:
scope_vector:
assumptions:
source_nodes:
source_edges:
proof_or_counterexample:
bridge_dependencies:
quotient_policy:
status_before:
status_after:
remaining_debt:
provenance:
version:
```

If the closure type is `BLOCKED`, it must additionally tag:

```yaml
block_scope:
reopen_conditions:
transferability:
```

To avoid disguising a temporary blockage as a permanent no-go.

---

# 42. Minimum Route Record

```yaml
route_id:
problem_id:
domain:
start_state:
target_state:
assumptions:
representation:
method_family:
steps:
bridge_ids:
obstruction_ids:
survivor_ids:
status:
refinement_parent:
quotient_class:
certificates:
debt:
provenance:
```

---

# 43. Minimum Domain Record

```yaml
domain_id:
name:
equation_or_target_family:
space_dimension:
spatial_domain:
time_scope:
data_class:
solution_class:
regularity_target:
boundary_conditions:
forcing_class:
representation_scope:
physical_interpretation_scope:
admissibility_rules:
proof_regime:
parent_domains:
bridge_ids:
```

---

# 44. Core Axioms / Norms of CSM v0.1

## CSM-A1 — Typed Node Principle

Different mathematical roles must not be treated as isomorphic nodes simply because they both appear in the research text.

## CSM-A2 — Typed Edge Principle

Implication, dependency, representation, bridge, block, and contradiction must not collapse.

## CSM-A3 — Relative Globality Principle

Any global closure is relative to the declared scope, unless there is an absolute-completeness proof.

## CSM-A4 — No Premature Promotion

Observational evidence must not be promoted to theorem closure without a certificate.

## CSM-A5 — No Premature Quotient

Semantic similarity must not be promoted to mathematical equivalence without a certificate.

## CSM-A6 — Provenance Preservation

Any quotient / closure / repair must be traceable back to the original evidence.

## CSM-A7 — Blockage Non-Finality

Route blockage is not proposition falsehood, and can be legally reopened.

## CSM-A8 — Bridge Explicitness

Transfers across domains / representations / models must have a bridge certificate.

## CSM-A9 — Completeness Debt Preservation

When route / decomposition completeness is not established, relative closure must not masquerade as absolute closure.

## CSM-A10 — Globality Typing

Any global claim must be accompanied by a scope vector or an equivalent domain declaration.

## CSM-A11 — Closure Non-Collapse

Different closure actions are not presumed to be mutually derivable or isomorphic.

## CSM-A12 — Ledgered Dynamics

Closure-space state changes must be versioned and auditable.

---

# 45. First Batch of Provable Propositions

The following are structural propositions of CSM v0.1, not deep new mathematical theorems.

## Proposition 45.1 — Observed Closure Non-Completeness

If:

$$
\Omega^{\rm obs}
\subsetneq
\Omega^{\rm adm},
$$

then:

$$
\mathsf{Closed}(\Omega^{\rm obs})
\not\Rightarrow
\mathsf{Closed}(\Omega^{\rm adm}).
$$

This is an epistemic firewall directly derived from set inclusion.

## Proposition 45.2 — Quotient Preservation Requirement

If a quotient map:

$$
q:\Omega\to\Omega/\sim
$$

does not preserve target-relevant assumptions or theorem strength, then the quotient closure cannot serve as a sound certificate for the target closure.

## Proposition 45.3 — Bridge-Soundness Requirement

If a closure claim from $X$ to $Y$ uses bridge $B$, but $B$ is not proven sound, then the closure status of $Y$ retains at least the bridge debt.

## Proposition 45.4 — Blockage Reopening Possibility

If a blockage proof depends on assumption set $A$, and a new route $R'$ does not satisfy $A$, then the old blockage cannot transfer to $R'$ without a certificate.

## Proposition 45.5 — Relative-Global Closure Bound

The claim strength of any:

$$
\mathfrak C^{\rm rel}_{D,\Theta,\mathcal A,R,N,H}(Q)
$$

must not exceed the combined strength of its domain, bridge, completeness, and verification certificates.

---

# 46. The First Closure-Space Research Program for NS

The first version of the NS experiment does not directly pursue "drawing all 203 papers into a graph".

It should proceed sequentially:

1. Fix the $\mathfrak N_{\rm C}$ formal target;
2. Build the domain records for $\mathfrak N_{\rm P}$ and $\mathfrak N_{\rm G}^{\Sigma}$;
3. Extract Claims / Assumptions / Lemmas / Routes / Obstructions / Survivors from the existing corpus;
4. Establish $\sim_{\rm prop}$, $\sim_{\rm route}$, $\sim_{\rm obs}$;
5. Build the implication DAG;
6. Build the route hypergraph;
7. Build obstruction transfer edges;
8. Establish lineage for C1--C6, X72, DCRP, etc.;
9. Tag CLOSED+, CLOSED-, BLOCKED, CONDITIONAL, OPEN;
10. Calculate the quotient frontier;
11. Find closure-central nodes;
12. Systematically research high closure-gain targets;
13. Recalculate the entire relative-global graph after each closure.

This is:

$$
\boxed{
\text{Solve by iterative certified closure of a relative-global proof space.}
}
$$

---

# 47. Complementary Relationship with Traditional "Proof Finding"

CSM does not claim that all future mathematics must use closure-space exhaustion.

Some problems may still be solved directly by a single elegant lemma.

The value of CSM primarily emerges when:

- the proof space is extremely large;
- the research history is very long;
- failures / obstructions are numerous;
- multiple representations coexist;
- multiple agents / tools operate in parallel;
- routes are frequently revisited;
- no-gos and survivors are reusable;
- the target itself possesses multiple domain / scope interpretations.

NS is exactly this kind of experimental ground.

---

# 48. The True Long-Term Questions of CSM

Ultimately, CSM does not merely ask:

> Which routes have already been taken?

Rather, it asks:

1. Does a stable quotient geometry exist for the closure-space?
2. Do obstructions possess a composable transfer algebra?
3. Does the frontier have a provable compression rate?
4. In which mathematical domains can completeness certificates be realized?
5. Can certain theorems be rewritten as finite / transfinite closure problems?
6. Do closure actions form lattice / category / fixed-point structures in specific subclasses?
7. Do closure-space dynamics possess invariants, attractors, or recurrent basins?
8. Can the route grammar of certain proof domains be proven complete?
9. Is there a "closure of the closure itself" and a meta-closure hierarchy?
10. Can CSM further evolve from a research methodology into a reusable formal mathematical tool?

These are all topics for subsequent Paper 01+.

---

# 49. Proposed Series Structure

CSM first round proposal:

- **Paper 00**: Formal Foundations;
- **Paper 01**: Globality Typing and Domain Stratification;
- **Paper 02**: Typed Route Hypergraphs and Quotient Geometry;
- **Paper 03**: Obstruction Closure, Transfer and Reopening;
- **Paper 04**: Frontier Mathematics and Relative-Global Closure Grades;
- **Paper 05**: Route-Completeness Certificates and Closure Proofs;
- **Paper 06**: Closure-Space Dynamics, Fixed Points and Meta-Closure;
- **NS Application 00**: NS Relative-Global Closure Graph v0.1;
- **NS Application 01**: C1--C6 / X72 / DCRP Closure Reconstruction;
- **Runtime 00**: CSM Graph Builder / Closure Verifier MVP.

Paper numbering can be changed later; this is a proposed research route, not canonical commitment beyond Paper 00.

---

# 50. Conclusion

The core of CSM is not about "drawing graphs" of mathematical research.

What it aims to do is transform:

$$
\text{Claim},
\quad
\text{Route},
\quad
\text{Obstruction},
\quad
\text{Bridge},
\quad
\text{Survivor},
\quad
\text{Frontier},
\quad
\text{Closure}
$$

into typed objects that can be mathematically manipulated.

The final research state is not:

$$
\text{we tried many things}.
$$

but rather:

$$
\boxed{
\mathfrak C_t
=
\text{the current audited relative-global closure state of the problem}.
}
$$

The next step in research is no longer just "think of another route," but rather:

$$
\boxed{
\text{select the frontier operation with the highest certified closure value}.
}
$$

However, the entire framework always retains a final firewall:

$$
\boxed{
\text{Relative-Global Closure}
\neq
\text{Absolute Mathematical Completeness}.
}
$$

Only when route / decomposition completeness itself becomes a provable theorem can closure-space exhaustion be promoted to a true exhaustive proof mechanism.

For Navier--Stokes, this means that all previously blocked routes, NO-GOs, survivors, and OPENs are no longer research waste, but the structural materials for the first large-scale closure space.

---

# Appendix A: Core Symbols

| Symbol | Meaning |
|---|---|
| $Q$ | target problem / theorem |
| $D$ | declared mathematical domain |
| $\Theta$ | proof / reasoning regime |
| $\mathcal A$ | admissibility rules |
| $R$ | search regime |
| $N$ | resource / sampling bound |
| $H$ | research history |
| $\Omega^{\rm math}$ | mathematical possibility space |
| $\Omega^{\rm adm}$ | admissible route space |
| $\Omega^{\rm obs}$ | observed research space |
| $\mathfrak C^{\rm rel}$ | relative-global closure space |
| $V$ | typed node set |
| $E$ | typed edge / hyperedge set |
| $\tau_V$ | node typing function |
| $\tau_E$ | edge typing function |
| $\sim$ | quotient relations |
| $\preceq$ | theorem / route refinement order |
| $\sigma$ | closure / epistemic status |
| $\mathfrak O$ | closure action family |
| $\partial\mathfrak C$ | active frontier |
| $\partial^{\ast}\mathfrak C$ | quotient frontier |
| $\mathsf{Debt}$ | outstanding proof obligations |
| $\mathsf{Ledger}$ | versioned closure history |
| $\mathsf{RCCert}$ | route-completeness certificate |
| $\mathsf{GScope}$ | typed globality / scope vector |
| $\mathfrak N_{\rm C}$ | formal Clay / mathematical NS domain |
| $\mathfrak N_{\rm P}$ | physical NS realization domain |
| $\mathfrak N_{\rm G}^{\Sigma}$ | generalized NS-like family under signature $\Sigma$ |

---

# Appendix B: Internal Theoretical Lineage

The formal design of this paper primarily inherits the following existing internal research assets:

1. **LSI-PSD / Logic-Space Integration and Proof-Space Dynamics**: semantic quotient, route graph, proof basin, obstruction confluence, theorem-strength preorder, Proof-Space Observatory, epistemic firewall.
2. **UGC/CUR / Unified Closure Theory**: typed non-collapse, generative closure, reachability, transformation closure, bridge certificate, debt, ledger, relative-global promotion discipline.
3. **NS ETN--X Integration**: rewriting Navier--Stokes research into a multiscale legality / UV-chain / obstruction program, while maintaining the stratification of the formal NS target and research language.
4. **NS C1--C6 / X72 / DCRP**: providing a massive number of closed, blocked, conditionalized, survivor, and reopened proof-state instances as the first large-scale closure-space corpus for CSM.
5. **Productive Mis-Specification / Descendant Survival line**: even if a parent formulation, model, or assumption is revised, all descendant mathematical assets cannot be automatically deleted; a lineage-aware audit is required.

These sources constitute the theoretical lineage of CSM; this does not imply that they are completely equivalent to each other, nor does it imply that CSM has completed academic benchmarking against external graph theory, proof theory, category theory, or closure algebra.

---

# Appendix C: Next Steps

After the completion of Paper 00, the next most important theoretical task is not to immediately build the complete NS graph, but to first write:

$$
\boxed{
\textbf{CSM Paper 01 — Globality Typing and Domain Stratification}.
}
$$

Because if we do not first clarify "which kind of global, which domain, and which bridges can legally cross domains," the subsequent NS Closure Graph will once again conflate Clay mathematical NS, physical realization, and the generalized NS-like family.

**END OF CSM PAPER 00 v0.1**