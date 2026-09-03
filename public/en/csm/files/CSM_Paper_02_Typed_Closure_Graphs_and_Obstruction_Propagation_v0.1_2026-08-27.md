# CSM Paper 02 — Typed Closure Graphs and Obstruction Propagation

## Closure-Space Mathematics: Typed Closure Graphs, Obstruction Propagation, Reopening, and Frontier Contraction

**English Title:** *Closure-Space Mathematics: Typed Closure Graphs, Obstruction Propagation, Reopening, and Frontier Contraction*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 02  
**Version:** v0.1  
**Date:** 2026-08-27  
**Language:** en-US  
**Status:** Formal Theory / Graph-Operational Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline `$...$`; display `$$...$$`

---

## Abstract

This paper establishes the first graph-theoretic operational core of Closure-Space Mathematics (CSM). Paper 00 organized propositions, routes, obstructions, certificates, frontiers, debts, and ledgers in research into a relative-global closure space; Paper 01 further decomposed "globality" into quantifier scopes and domain typing, prohibiting uncertified promotion from narrower to broader scopes. This paper now addresses the next core problem:

> In a large-scale mathematical problem, how can "this route is blocked," "this branch is proven," "this conditional proposition holds," "this obstruction is only valid under certain assumptions," and "a subsequent new bridge reopens an old dead end" all be represented within the same auditable graph-theoretic system?

This paper argues that ordinary directed graphs are insufficient to carry a mature proof-space closure. What is truly needed is a **typed directed hypergraph** equipped with types, scopes, certificates, multiple premises, multiple outputs, conditionalization, and versioning. On this graph, we define respectively:

1. implication closure;
2. equivalence quotient closure;
3. conditional closure;
4. obstruction propagation closure;
5. bridge-mediated closure;
6. reopening operator;
7. frontier contraction operator;
8. debt propagation;
9. closure ledger;
10. relative route-exhaustion certificate.

The core non-collapse principle of this paper is:

$$
\boxed{
\mathsf{RouteBlocked}
\neq
\mathsf{ClaimRefuted}
\neq
\mathsf{BranchClosed}
\neq
\mathsf{DomainClosed}.
}
$$

An obstruction is allowed to propagate along legal dependency edges only when its assumption, scope, representation, bridge, and target fidelity all match. Any obstruction promotion across scopes, representations, equation families, or model classes must be accompanied by a propagation certificate; otherwise, it can only form a local blocked state and cannot be elevated to a theorem-level no-go.

On the other hand, CSM does not view closure as permanently monotonic. When old assumptions are removed, new representations emerge, new bridges are proven, obstructions are narrowed, counterexamples are retracted, or parent theorems are revised, previously blocked routes can legally become OPEN again. Therefore, this paper introduces the **Reopening Operator** and the **Versioned Closure Ledger**, making proof-space closure a replayable, revisable, and locally reversible dynamic graph evolution.

Finally, this paper proposes the minimal instantiation rules for the NS relative-global closure graph: `NO-GO`, `OPEN`, `SURVIVOR`, `CONDITIONAL`, and `CLOSED` in past C1--C6, X72, DCRP, MORP, RFP, FCBP, and other proof families are no longer just document labels, but are compiled into typed nodes, hyperedges, obstruction certificates, and frontier states. This ensures that "closing a proposition step by step" in the future is no longer just a research narrative, but can become an explicit graph-theoretic closure procedure.

---

# 1. Research Positioning

This paper does not redefine the entire ontology of CSM. Paper 00 has established:

$$
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
$$

Paper 01 has established scope contracts and globality typing.

This paper focuses on:

$$
\boxed{
\text{How to make }\mathfrak C
\text{ truly execute closure operations.}
}
$$

---

# 2. Why Ordinary Directed Graphs Are Insufficient

A typical mathematical derivation is not:

$$
A\to B.
$$

But rather often:

$$
A_1,\ldots,A_k
\Longrightarrow
B_1,\ldots,B_m.
$$

For example, an obstruction might require:

$$
A_{\rm regularity}
\land
A_{\rm symmetry}
\land
A_{\rm scale}
\land
A_{\rm boundary}
$$

to deduce:

$$
\neg R.
$$

Therefore, the primitive edge in CSM must allow:

$$
e:
\{v_1,\ldots,v_k\}
\longrightarrow
\{w_1,\ldots,w_m\}.
$$

This paper uses directed hyperedges as the fundamental relational unit.

---

# 3. Typed Closure Hypergraph

Define the CSM closure hypergraph:

$$
\boxed{
\mathcal H_{\rm CSM}
=
(V,E,\tau_V,\tau_E,\sigma,\lambda,\pi,\chi,\nu).
}
$$

Where:

- $V$: set of nodes;
- $E$: set of directed hyperedges;
- $\tau_V$: node types;
- $\tau_E$: edge types;
- $\sigma$: epistemic / closure status;
- $\lambda$: scope label;
- $\pi$: provenance;
- $\chi$: certificate metadata;
- $\nu$: version information.

---

# 4. Node Types

The minimal node type family is defined as:

$$
\tau_V(v)
\in
\{
\mathsf{Problem},
\mathsf{Claim},
\mathsf{Assumption},
\mathsf{Lemma},
\mathsf{RouteState},
\mathsf{Obstruction},
\mathsf{Bridge},
\mathsf{Certificate},
\mathsf{Counterexample},
\mathsf{Domain},
\mathsf{Scope},
\mathsf{Representation},
\mathsf{Frontier},
\mathsf{Debt},
\mathsf{Revision}
\}.
$$

Not all nodes can be directly connected to each other by edges.

---

# 5. Edge Types

The minimal edge type family:

$$
\tau_E(e)
\in
\{
\mathsf{IMPLIES},
\mathsf{DEPENDS},
\mathsf{ASSUMES},
\mathsf{REFINES},
\mathsf{EQUIV},
\mathsf{BLOCKS},
\mathsf{REFUTES},
\mathsf{BRIDGES},
\mathsf{REOPENS},
\mathsf{GENERALIZES},
\mathsf{SPECIALIZES},
\mathsf{LIFTS},
\mathsf{PROJECTS},
\mathsf{CERTIFIES},
\mathsf{WEAKENS},
\mathsf{STRENGTHENS},
\mathsf{REVISES},
\mathsf{INHERITS}
\}.
$$

Any edge type must have a source/target type signature.

---

# 6. Edge Signature

Let:

$$
\operatorname{sig}(e)
=
\left(
\tau_V(\operatorname{src}(e)),
\tau_E(e),
\tau_V(\operatorname{tgt}(e))
\right).
$$

If an edge does not conform to its signature, then:

$$
\boxed{
e\notin E_{\rm legal}.
}
$$

For example:

$$
\mathsf{Obstruction}
\xrightarrow{\mathsf{BLOCKS}}
\mathsf{RouteState}
$$

is legal.

But:

$$
\mathsf{Representation}
\xrightarrow{\mathsf{REFUTES}}
\mathsf{Claim}
$$

is illegal without a theorem-level counterexample bridge.

---

# 7. Closure Status

Node status:

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
\mathsf{STALE},
\mathsf{REOPENED}
\}.
$$

Where:

$$
\mathsf{CLOSED}^{+}
$$

indicates positive proof.

$$
\mathsf{CLOSED}^{-}
$$

indicates a theorem-level refutation or certified counterexample.

$$
\mathsf{BLOCKED}
$$

indicates that the route cannot proceed under the current scope/assumption/regime.

---

# 8. First Non-Collapse Principle

$$
\boxed{
\mathsf{BLOCKED}
\neq
\mathsf{CLOSED}^{-}.
}
$$

If a proof route is blocked by an estimate barrier, one can only obtain:

$$
\sigma(R)=\mathsf{BLOCKED}.
$$

One cannot obtain:

$$
\sigma(Q)=\mathsf{CLOSED}^{-}.
$$

---

# 9. Second Non-Collapse Principle

$$
\boxed{
\mathsf{BranchClosed}
\neq
\mathsf{ProblemClosed}.
}
$$

If a route family:

$$
B_i
$$

is entirely blocked, it does not mean that:

$$
Q
$$

has no other admissible route families.

---

# 10. Third Non-Collapse Principle

$$
\boxed{
\mathsf{LocalObstruction}
\neq
\mathsf{GlobalObstruction}.
}
$$

Any obstruction must carry a scope:

$$
\lambda(O).
$$

If:

$$
\lambda(O)=D_0,
$$

then unless there is a promotion certificate, one cannot automatically elevate:

$$
O
$$

to:

$$
D_1\supsetneq D_0.
$$

---

# 11. Assumption Envelope

Every theorem, route, or obstruction carries:

$$
\boxed{
\mathsf{Asm}(x)
=
\{A_1,\ldots,A_n\}.
}
$$

The first necessary condition for obstruction propagation:

$$
\boxed{
\mathsf{Asm}(O)
\subseteq
\mathsf{Asm}(R).
}
$$

If this does not hold, the obstruction cannot act directly.

---

# 12. Scope Envelope

Every object simultaneously carries a scope contract:

$$
\mathsf{Scope}(x).
$$

Obstruction propagation requires:

$$
\mathsf{Scope}(R)
\preceq
\mathsf{Scope}(O)
$$

or the existence of a legal scope bridge.

Here $\preceq$ indicates that the obstruction's scope covers at least the scope where the route resides.

---

# 13. Representation Envelope

Let:

$$
\mathsf{Rep}(x)
$$

denote the representation class used by the proof object.

If an obstruction is only valid for:

$$
\rho_1
$$

and the route switches to:

$$
\rho_2,
$$

then:

$$
\boxed{
O_{\rho_1}
\not\Rightarrow
O_{\rho_2}.
}
$$

Unless there is a:

$$
\mathsf{RepTransferCert}_{\rho_1\to\rho_2}.
$$

---

# 14. Target Fidelity

Every obstruction must also align with a target:

$$
\mathsf{Target}(O).
$$

If the true target of the route is:

$$
Q',
$$

but the obstruction proves:

$$
\neg Q,
$$

and:

$$
Q'\not\Rightarrow Q,
$$

then the obstruction cannot propagate.

---

# 15. Obstruction Record

Define an obstruction:

$$
\boxed{
O
=
\left\langle
\mathsf{Target},
\mathsf{Asm},
\mathsf{Scope},
\mathsf{Rep},
\mathsf{Mechanism},
\mathsf{Strength},
\mathsf{Cert},
\mathsf{Version}
\right\rangle.
}
$$

---

# 16. Obstruction Strength

$$
\mathsf{Strength}(O)
\in
\{
\mathsf{DIAGNOSTIC},
\mathsf{EMPIRICAL},
\mathsf{CONDITIONAL\_NO\_GO},
\mathsf{FORMAL\_NO\_GO},
\mathsf{COUNTEREXAMPLE},
\mathsf{INDEPENDENCE}
\}.
$$

Only the latter three classes have a theorem-level closure effect under the appropriate scope.

---

# 17. Diagnostic Obstructions Do Not Close Propositions

If:

$$
\mathsf{Strength}(O)=\mathsf{DIAGNOSTIC},
$$

then at most:

$$
R
\mapsto
\mathsf{BLOCKED}.
$$

It must not be that:

$$
Q
\mapsto
\mathsf{CLOSED}^{-}.
$$

---

# 18. Local Route Blocking by Formal No-Go

If:

$$
\mathsf{Strength}(O)=\mathsf{FORMAL\_NO\_GO}
$$

and the propagation contract is satisfied, then we can have:

$$
O
\xrightarrow{\mathsf{BLOCKS}}
R.
$$

If $R$ itself is a complete claim branch, then:

$$
\sigma(R)=\mathsf{CLOSED}^{-}.
$$

However, whether the parent problem is closed is still determined separately.

---

# 19. Obstruction Propagation Contract

Define:

$$
\boxed{
\mathsf{OPCert}(O\to R)
}
$$

which must at least include:

1. target match;
2. assumption coverage;
3. scope compatibility;
4. representation compatibility;
5. dependency validity;
6. theorem-strength compatibility;
7. version freshness;
8. exception audit;
9. bridge status;
10. provenance reference.

---

# 20. Propagation Rule

If:

$$
\mathsf{OPCert}(O\to R)=\mathsf{PASS},
$$

then:

$$
O\triangleright R.
$$

Meaning the obstruction can act on the route.

If:

$$
\mathsf{OPCert}(O\to R)\neq\mathsf{PASS},
$$

then:

$$
O\ntriangleright R.
$$

---

# 21. Obstruction Propagation Closure

For an obstruction set $\mathfrak O$, define:

$$
\boxed{
\operatorname{Cl}_{\rm obs}(S)
=
S
\cup
\left\{
R:
\exists O\in\mathfrak O,
\mathsf{OPCert}(O\to R)=\mathsf{PASS}
\right\}.
}
$$

This is not a traditional topological closure.

It is a typed proof-space closure operator family.

---

# 22. Implication Closure

Define:

$$
\boxed{
\operatorname{Cl}_{\Rightarrow}(S)
=
\left\{
q:
S\vdash_{\mathcal H}q
\right\}.
}
$$

Where the hypergraph derivation must only use legal certified implication edges.

---

# 23. Conditional Closure

If:

$$
A_1,\ldots,A_k
\Rightarrow
Q
$$

is proven, but $A_i$ are not all closed, then:

$$
\boxed{
\sigma(Q)=\mathsf{CONDITIONAL}.
}
$$

Corresponding to:

$$
\operatorname{Cl}_{\rm cond}(S).
$$

---

# 24. Quotient Closure

Given equivalence relations:

$$
\sim_{\rm prop},
\qquad
\sim_{\rm route},
\qquad
\sim_{\rm obs}.
$$

Define:

$$
\boxed{
\operatorname{Cl}_{\sim}(S)
=
\bigcup_{x\in S}[x]_{\sim}.
}
$$

However, quotient closure does not delete search provenance.

---

# 25. Quotients Must Not Erase Genealogy

If:

$$
R_1\sim_{\rm route}R_2,
$$

then the mathematical identity can be quotiented.

But:

$$
\pi(R_1)\neq\pi(R_2)
$$

can still be preserved.

Therefore:

$$
\boxed{
\text{Mathematical quotient}
\neq
\text{Historical deletion}.
}
$$

---

# 26. Bridge Closure

If:

$$
X
\xrightarrow{\mathsf{Bridge}}
Y
$$

and:

$$
\mathsf{BridgeCert}^{X\to Y}
=
\mathsf{PASS},
$$

then:

$$
Y
$$

can enter:

$$
\operatorname{Cl}_{\rm bridge}(X).
$$

---

# 27. Bridges Are Not Guaranteed to Be Lossless

Even if:

$$
\mathsf{BridgeCert}^{X\to Y}
=
\mathsf{PASS},
$$

it is still possible that:

$$
\mathsf{Loss}(X\to Y)>0.
$$

Therefore, closure metadata must record bridge loss.

---

# 28. Closure Family

CSM does not assume a single closure operator.

Let:

$$
\boxed{
\mathfrak{Cl}
=
\{
\operatorname{Cl}_{\Rightarrow},
\operatorname{Cl}_{\rm cond},
\operatorname{Cl}_{\rm obs},
\operatorname{Cl}_{\sim},
\operatorname{Cl}_{\rm bridge},
\operatorname{Cl}_{\rm reopen}
\}.
}
$$

---

# 29. Heterogeneous Closure Principle

Different closure operators have different semantics.

Therefore:

$$
\boxed{
\operatorname{Cl}_{\Rightarrow}
\neq
\operatorname{Cl}_{\rm obs}
\neq
\operatorname{Cl}_{\sim}.
}
$$

They cannot be equated simply because their symbols are all called closure.

---

# 30. Closure Composition

In some cases, one can perform:

$$
\operatorname{Cl}_{\rm obs}
\circ
\operatorname{Cl}_{\Rightarrow}.
$$

But it is not guaranteed that:

$$
\operatorname{Cl}_{\Rightarrow}
\circ
\operatorname{Cl}_{\rm obs}
=
\operatorname{Cl}_{\rm obs}
\circ
\operatorname{Cl}_{\Rightarrow}.
$$

---

# 31. Noncommutative Closure

Thus, in general:

$$
\boxed{
\operatorname{Cl}_i
\circ
\operatorname{Cl}_j
\neq
\operatorname{Cl}_j
\circ
\operatorname{Cl}_i.
}
$$

This is one of the formal sources of proof-space order dependence.

---

# 32. Closure Schedule

Define a closure schedule:

$$
\boxed{
\Sigma_{\rm Cl}
=
(C_1,C_2,\ldots,C_n).
}
$$

The same initial graph under different schedules may yield different intermediate states.

---

# 33. Stable Closure State

If a graph state $G^\star$ satisfies:

$$
C_i(G^\star)=G^\star
$$

for all currently active closure operators, it is said that:

$$
\boxed{
G^\star
\text{ is locally closure-stable}.
}
$$

This does not imply absolute mathematical completeness.

---

# 34. Frontier

Define the active frontier:

$$
\boxed{
\partial\mathfrak C(Q)
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
}
$$

Where $v\leadsto Q$ indicates the existence of a legal route or bridge reachability.

---

# 35. Quotient Frontier

Define:

$$
\boxed{
\partial^\ast\mathfrak C(Q)
=
\partial\mathfrak C(Q)/\sim_{\rm route}.
}
$$

This is closer to the true independent route mass than the raw frontier size.

---

# 36. Frontier Mass

One can define:

$$
\boxed{
M_{\partial}(Q)
=
\sum_{[r]\in\partial^\ast\mathfrak C(Q)}
w([r]).
}
$$

Where $w([r])$ can reflect route independence, generality, or certificate quality.

---

# 37. Frontier Contraction

If a legal closure step causes:

$$
M_{\partial,t+1}(Q)
<
M_{\partial,t}(Q),
$$

it is called:

$$
\boxed{
\text{frontier contraction}.
}
$$

However, frontier contraction does not equal theorem progress unless supported by closure certificates.

---

# 38. False Contraction

If the frontier shrinks merely due to:

- over-aggressive quotient;
- assumption bait-and-switch;
- scope shrinking;
- representation deletion;
- unsupported obstruction propagation;

then it is called:

$$
\boxed{
\text{false contraction}.
}
$$

---

# 39. Frontier Expansion

New representations, new theorems, new bridges, or assumption relaxations may cause:

$$
M_{\partial,t+1}(Q)
>
M_{\partial,t}(Q).
$$

This is not necessarily a regression.

It may indicate that the research space has become more faithful.

---

# 40. Reopening Principle

If a route $R$ once had:

$$
\sigma_t(R)=\mathsf{BLOCKED},
$$

but subsequently:

- the obstruction is narrowed;
- an assumption is removed;
- the representation changes;
- a bridge appears;
- the theorem is revised;

then it is allowed that:

$$
\boxed{
\sigma_{t+1}(R)=\mathsf{REOPENED}.
}
$$

---

# 41. Reopening Operator

Define:

$$
\boxed{
\operatorname{Cl}_{\rm reopen}^{-1}
}
$$

This is not a traditional inverse closure.

It signifies:

> Performing a versioned re-audit of past closure decisions, revoking blocked/closed inheritances that are no longer valid.

---

# 42. Reopening Certificate

$$
\boxed{
\mathsf{ReopenCert}(R)
}
$$

must at least include:

1. previous closure event;
2. invalidated premise;
3. changed scope/representation/bridge;
4. surviving dependencies;
5. new status;
6. provenance;
7. version reference.

---

# 43. Closure Need Not Be Globally Monotonic

Under a fixed theorem base and fixed assumptions, certain closure operators can be monotonic.

But in a research system:

$$
\boxed{
\mathfrak C_t
\subseteq
\mathfrak C_{t+1}
}
$$

is not a universal truth.

Because revisions can revoke old closures.

---

# 44. Monotone Evidence / Nonmonotone Status

More precisely:

$$
\boxed{
\text{Evidence Ledger may be monotone,
while Closure Status may be nonmonotone}.
}
$$

Old evidence is not deleted, but old conclusions can be revised.

---

# 45. Closure Ledger

Define:

$$
\boxed{
\mathsf{Ledger}_{\rm Cl}
=
\{
e_1,e_2,\ldots
\}
}
$$

Every closure event:

$$
e_t
=
\left\langle
\mathsf{Object},
\mathsf{OldStatus},
\mathsf{NewStatus},
\mathsf{Cause},
\mathsf{Cert},
\mathsf{Scope},
\mathsf{Version},
\mathsf{Time}
\right\rangle.
$$

---

# 46. Event-Sourced Closure

System state:

$$
\boxed{
\mathcal S_{t+1}
=
\operatorname{Apply}(\mathcal S_t,e_t).
}
$$

Any reopening is a new event, not an erasure of old history.

---

# 47. Closure Debt

If a closure decision lacks a partial proof obligation, define:

$$
\boxed{
\mathsf{Debt}_{\rm Cl}(x).
}
$$

For example:

- missing scope proof;
- missing bridge proof;
- missing route-completeness proof;
- missing representation robustness;
- missing target fidelity;
- missing independence audit.

---

# 48. Debt Propagation

If:

$$
A\Rightarrow B
$$

but $A$ carries an unfulfilled debt, then:

$$
B
$$

cannot automatically be marked as debt-free.

One can define:

$$
\boxed{
\mathsf{Debt}(B)
\supseteq
\mathsf{TransferDebt}(A\to B).
}
$$

---

# 49. Closure with Debt

Allow:

$$
\boxed{
\sigma(Q)=\mathsf{CONDITIONAL}
\quad
\text{with}
\quad
\mathsf{Debt}(Q)\neq\varnothing.
}
$$

This aligns better with long-term research than a rigid PASS/FAIL dichotomy.

---

# 50. Route Exhaustion

Let:

$$
\mathcal R_{\rm adm}(Q)
$$

be the admissible route classes.

If:

$$
\forall [R]\in\mathcal R_{\rm adm}(Q),
\quad
\sigma([R])\in
\{
\mathsf{CLOSED}^{-},
\mathsf{BLOCKED}
\},
$$

one still cannot immediately say:

$$
Q
$$

is refuted.

Because the route space itself may be incomplete.

---

# 51. Route-Completeness Certificate

Define:

$$
\boxed{
\mathsf{RCCert}(Q,\mathcal G_R).
}
$$

Its goal is to prove:

$$
\boxed{
\mathcal R_{\rm enum}(Q)
=
\mathcal R_{\rm adm}(Q)
}
$$

relative to a specified route grammar / mechanism class.

---

# 52. Relative Route Completeness

Usually, one can only prove:

$$
\boxed{
\mathcal R_{\rm enum}^{\Gamma}(Q)
=
\mathcal R_{\rm adm}^{\Gamma}(Q)
}
$$

where $\Gamma$ is an explicit route grammar.

This is still relative completeness.

---

# 53. Exhaustion Theorem Pattern

If:

1. $\mathsf{RCCert}(Q,\Gamma)=\mathsf{PASS}$;
2. every admissible route class is excluded by a certified obstruction;
3. obstruction propagations are all scope-valid;

then one can obtain:

$$
\boxed{
\Gamma
\vdash
\neg\operatorname{RouteExists}(Q).
}
$$

---

# 54. Route Exhaustion Does Not Equal Claim Refutation

If $Q$ itself is not a proposition about "the existence of a route," but an external mathematical proposition, a bridge is still needed:

$$
\neg\operatorname{RouteExists}(Q)
\Longrightarrow
\neg Q.
$$

This bridge must also have a certificate.

---

# 55. Positive Exhaustion

Conversely, if a claim can be decomposed into a finite or controllable branch family:

$$
Q
\Longleftrightarrow
Q_1\vee\cdots\vee Q_n,
$$

and some $Q_i$ is proven, then:

$$
Q
$$

is positively closed.

If all $Q_i$ are refuted, then:

$$
Q
$$

is negatively closed.

---

# 56. Branch Decomposition Certificate

Define:

$$
\boxed{
\mathsf{BDCert}
\left(
Q
\leftrightarrow
\bigvee_iQ_i
\right).
}
$$

Without a branch decomposition certificate, branch closure cannot be promoted to parent closure.

---

# 57. Hypergraph Cut

For a target $Q$, define a cut set:

$$
C\subset V
$$

such that every admissible route to $Q$ passes through $C$.

If:

$$
C
$$

is completely certified closed, it may form a high-leverage obstruction boundary.

---

# 58. Certified Cut

If:

$$
\mathsf{CutCert}(C,Q)=\mathsf{PASS},
$$

and:

$$
\forall c\in C,
\quad
\sigma(c)=\mathsf{CLOSED}^{-},
$$

then all routes to:

$$
Q
$$

are truncated.

However, a parent bridge is still needed to determine whether $\neg Q$ is deduced.

---

# 59. Obstruction Centrality

Define:

$$
Z(O)
$$

to represent the independent route mass truncated by the obstruction in the route graph.

This is not a theorem truth score.

---

# 60. High-Centrality Obstruction

If:

$$
Z(O)\gg0,
$$

it indicates that:

$$
O
$$

is worth prioritizing for research.

But:

$$
\boxed{
Z(O)\gg0
\not\Rightarrow
O
\text{ is globally necessary}.
}
$$

---

# 61. Obstruction Confluence

If different route quotient classes:

$$
[R_i]_{\rm route}
$$

all hit the same obstruction class:

$$
[O^\star]_{\rm obs},
$$

it forms an:

$$
\boxed{
\text{obstruction confluence}.
}
$$

---

# 62. False Confluence

If different routes actually share the same hidden premise or are merely notation variants, the confluence strength must be down-weighted.

Therefore:

$$
C_{\rm raw}(O)
\neq
C_{\rm ind}(O).
$$

---

# 63. Closure Robustness

One can define:

$$
\boxed{
\mathsf{RobustCl}(O)
=
f(
C_{\rm ind},
C_B,
C_M,
C_L,
\mathsf{Scope},
\mathsf{CertQuality}
).
}
$$

But it remains a research metric, not a proof substitute.

---

# 64. Survivor

If a route family remains OPEN after all current legal obstruction propagations, it is called a:

$$
\boxed{
\mathsf{Survivor}(R).
}
$$

A survivor does not mean the route will succeed.

It only means it has not yet been blocked.

---

# 65. Minimal Survivor

If:

$$
R
$$

is a survivor, and all weaker or more general sibling routes are blocked, then:

$$
\boxed{
\mathsf{MinimalSurvivor}(R).
}
$$

This is a high-leverage target for the next round of research.

---

# 66. Survivor Compression

A mature research workflow will iterate:

$$
\text{many routes}
\to
\text{few survivors}
\to
\text{refined decomposition}
\to
\text{new obstruction audit}.
$$

This is the first fundamental cycle of closure-space dynamics.

---

# 67. Interaction Between Reopening and Survivors

Old survivors can be closed by new obstructions.

Old blocked routes can also be reopened by new bridges.

Therefore, the graph frontier is a:

$$
\boxed{
\text{dynamic boundary},
}
$$

not a static list.

---

# 68. NS Compilation Rules: From Document Labels to Graph States

Past NS documents frequently used:

- `CLOSED`;
- `OPEN`;
- `NO-GO`;
- `SURVIVOR`;
- `CONDITIONAL`;
- `STOP-*`.

CSM does not directly treat these texts as theorem statuses.

Every entry must first be compiled into:

$$
\boxed{
\mathsf{StatusRecord}
=
\langle
\mathsf{Object},
\mathsf{Claim},
\mathsf{Scope},
\mathsf{Asm},
\mathsf{CertType},
\mathsf{Status}
\rangle.
}
$$

---

# 69. NS NO-GO Compilation

If a document states:

> scalar additive budget NO-GO

It cannot directly generate:

$$
\mathsf{CLOSED}^{-}(\text{Navier--Stokes blow-up}).
$$

It should generate:

$$
\boxed{
O_{\rm scalar-budget}
\xrightarrow{\mathsf{BLOCKS}}
R_{\rm scalar-budget}.
}
$$

---

# 70. NS SURVIVOR Compilation

If a route is still surviving, such as a shear/polarization survivor, then establish:

$$
\sigma(R_{\rm sh/pol})
=
\mathsf{OPEN}.
$$

It is not:

$$
\mathsf{PROVEN}.
$$

---

# 71. NS STOP Compilation

`STOP-D105` is not a claim refutation.

It should be compiled as:

$$
\boxed{
\mathsf{FrontierNode}
(
\text{first-order solvability / spectral drift}
).
}
$$

This is an active boundary node.

---

# 72. NS Relative-Global Closure Graph

The minimal model:

$$
\boxed{
\mathcal H_{\rm NS}^{\rm rel}
=
\mathcal H_{\rm C1-C6}
\cup
\mathcal H_{\rm X72}
\cup
\mathcal H_{\rm DCRP}
\cup
\mathcal H_{\rm RFP}
\cup
\mathcal H_{\rm MORP}
\cup
\mathcal H_{\rm FCBP}
\cup
\mathcal H_{\rm bridge}.
}
$$

---

# 73. Cross-Series Bridge

Different NS series can only share obstructions when their claims/assumptions/scopes are aligned.

Therefore, there must be a:

$$
\mathsf{SeriesBridgeCert}.
$$

---

# 74. Cross-Series False Merge

If two papers both mention:

> carrier escape

But one refers to a spatial carrier and the other to a spectral carrier, then:

$$
\boxed{
O_1\not\sim_{\rm obs}O_2
}
$$

Unless there is a formal mapping otherwise.

---

# 75. First Goal of the Closure Graph

The primary goal of the NS closure graph is not to prove Clay.

Rather, it is:

$$
\boxed{
\text{To convert known routes, obstructions, survivors, and debts
into a queryable, propagatable, and reopenable relative-global graph.}
}
$$

---

# 76. Second Goal of the Closure Graph

To compute:

$$
\partial^\ast\mathfrak C_{\rm NS}(Q_{\rm Clay})
$$

which is the active independent frontier after quotienting.

---

# 77. Third Goal of the Closure Graph

To find:

$$
\boxed{
\text{high-centrality certified cuts}.
}
$$

They may offer more research leverage than blindly adding papers.

---

# 78. Fourth Goal of the Closure Graph

To check which blocked routes can be legally reopened by:

- assumption relaxation;
- new representation;
- new external theorem;
- bridge proof;
- domain retyping.

---

# 79. Closure-Space Update

Define:

$$
\boxed{
\mathfrak C_{t+1}
=
\mathfrak U(
\mathfrak C_t,
\Delta\mathsf{Claim},
\Delta\mathsf{Cert},
\Delta\mathsf{Bridge},
\Delta\mathsf{Obstruction},
\Delta\mathsf{Revision}
).
}
$$

---

# 80. Closure Fixed Point

If under a fixed corpus, fixed theorem base, and fixed bridge set:

$$
\mathfrak U(\mathfrak C^\star)=\mathfrak C^\star,
$$

it is called a local closure fixed point.

---

# 81. Fixed Point Does Not Equal Mathematical Completeness

$$
\boxed{
\mathfrak C^\star
\text{ locally stable}
\not\Rightarrow
\mathfrak C^\star
=
\Omega^{\rm math}.
}
$$

---

# 82. Closure Expansion

A new theorem or representation can cause:

$$
\mathfrak C^\star
\to
\mathfrak C^{\star\prime}
$$

and the frontier reappears.

Therefore, CSM's closure is an re-expandable closure.

---

# 83. Closure-Space Conservation of History

This paper requires:

$$
\boxed{
\text{No closure event may erase its provenance history.}
}
$$

Even if a route is reopened, the old obstruction event is still preserved.

---

# 84. Dual Identity of Proof Objects and Search Events

The same artifact simultaneously possesses a:

$$
\boxed{
\text{Mathematical Identity}
}
$$

and a:

$$
\boxed{
\text{Search-Historical Identity}.
}
$$

A mathematical quotient does not mean historical deletion.

---

# 85. Closure-Space Auditability

Any status must be able to answer:

1. Who closed it?
2. Using which theorem?
3. What are the assumptions?
4. What is the scope?
5. Does it cross representations?
6. Is there a bridge?
7. Is there a debt?
8. Has it ever been reopened?
9. Which version is valid?
10. Which descendants inherit this status?

---

# 86. Claim-Level Closure Certificate

Define:

$$
\boxed{
\mathsf{ClaimClCert}(Q)
}
$$

which includes:

- theorem proof / counterexample reference;
- branch decomposition;
- route completeness;
- obstruction propagation;
- scope fidelity;
- version;
- debt status.

---

# 87. Relative-Global Closure Certificate

For domain $D$:

$$
\boxed{
\mathsf{RGClCert}_{D}(Q).
}
$$

It signifies:

> Under the specified domain, route grammar, theorem base, representation policy, and bridge policy, the closure status of $Q$ has been fully audited.

---

# 88. Relative-Global Does Not Equal Absolute

$$
\boxed{
\mathsf{RGClCert}_{D}(Q)
\not\Rightarrow
\mathsf{AbsoluteClosure}(Q).
}
$$

---

# 89. Local-to-Absolute Gate

To elevate:

$$
\mathsf{RGClCert}_{D}(Q)
\to
\mathsf{AbsoluteClosure}(Q),
$$

one must at least resolve:

- domain completeness;
- route grammar completeness;
- representation completeness;
- theorem-base adequacy;
- hidden assumption absence;
- bridge completeness;
- undecidability/independence status.

---

# 90. Closure No-Go 1

$$
\boxed{
\text{Many blocked routes}
\not\Rightarrow
\text{claim false}.
}
$$

---

# 91. Closure No-Go 2

$$
\boxed{
\text{Many surviving routes}
\not\Rightarrow
\text{claim true}.
}
$$

---

# 92. Closure No-Go 3

$$
\boxed{
\text{Frontier shrinking}
\not\Rightarrow
\text{proof nearing completion}.
}
$$

---

# 93. Closure No-Go 4

$$
\boxed{
\text{One central obstruction}
\not\Rightarrow
\text{global obstruction}.
}
$$

---

# 94. Closure No-Go 5

$$
\boxed{
\text{One representation fails}
\not\Rightarrow
\text{all equivalent representations fail}.
}
$$

---

# 95. Closure No-Go 6

$$
\boxed{
\text{One domain is closed}
\not\Rightarrow
\text{all generalized domains are closed}.
}
$$

---

# 96. Closure No-Go 7

$$
\boxed{
\text{Research graph stable}
\not\Rightarrow
\text{mathematical reality exhausted}.
}
$$

---

# 97. Minimal Machine Record

```yaml
closure_record:
  object_id:
  object_type:
  target_id:
  scope_id:
  assumptions: []
  representation_id:
  old_status:
  new_status:
  cause_type:
  cause_ids: []
  certificate_id:
  debt_ids: []
  version:
  provenance:
  reopen_of:
```

---

# 98. Obstruction Machine Record

```yaml
obstruction:
  obstruction_id:
  target_pattern:
  assumptions: []
  scope:
  representation:
  mechanism:
  strength:
  certificate:
  exceptions: []
  bridge_requirements: []
  version:
  active: true
```

---

# 99. Propagation Machine Record

```yaml
obstruction_propagation:
  obstruction_id:
  target_route_id:
  target_match: PASS
  assumption_coverage: PASS
  scope_compatibility: PASS
  representation_compatibility: PASS
  dependency_validity: PASS
  theorem_strength: PASS
  version_freshness: PASS
  exception_audit: PASS
  bridge_status: PASS
  result: BLOCKED
```

---

# 100. Reopening Machine Record

```yaml
reopening:
  route_id:
  previous_closure_event:
  invalidated_premise:
  changed_scope:
  changed_representation:
  new_bridge:
  new_certificate:
  result: REOPENED
```

---

# 101. Validation Scenario A — Local estimate barrier

Route:

$$
R_1
$$

fails under the:

$$
L^p
$$

estimate.

If there is no theorem proving that all admissible norms fail, then:

$$
\sigma(R_1)=\mathsf{BLOCKED}.
$$

The parent claim remains OPEN.

---

# 102. Validation Scenario B — Counterexample

If there is a legal counterexample:

$$
c\models\neg Q,
$$

then:

$$
\sigma(Q)=\mathsf{CLOSED}^{-}.
$$

This is not a route-level block, but a claim-level refutation.

---

# 103. Validation Scenario C — Conditional theorem

If:

$$
A\Rightarrow Q
$$

is proven, but:

$$
\sigma(A)=\mathsf{OPEN},
$$

then:

$$
\sigma(Q)=\mathsf{CONDITIONAL}.
$$

---

# 104. Validation Scenario D — Representation reopening

If:

$$
R_{\rho_1}
$$

is blocked by obstruction $O_{\rho_1}$, but:

$$
R_{\rho_2}
$$

is unaffected by this obstruction, then:

$$
R_{\rho_2}
$$

remains OPEN.

If both are representation variants of the same route, one can record:

$$
\mathsf{REOPENED}.
$$

---

# 105. Validation Scenario E — Scope promotion forbidden

If an obstruction holds for:

$$
D_0
$$

but the target route is located in:

$$
D_1\supsetneq D_0,
$$

and there is no promotion certificate, then:

$$
O\ntriangleright R_{D_1}.
$$

---

# 106. Validation Scenario F — Branch exhaustion

If:

$$
Q
\leftrightarrow
Q_1\vee Q_2\vee Q_3
$$

has a $\mathsf{BDCert}$, and all three branches are theorem-level refuted, then:

$$
\sigma(Q)=\mathsf{CLOSED}^{-}.
$$

---

# 107. Validation Scenario G — Route grammar incomplete

If all listed routes are blocked, but there is no $\mathsf{RCCert}$, then:

$$
\sigma(Q)\neq\mathsf{CLOSED}^{-}
$$

One can only say:

$$
\text{observed route space exhausted}.
$$

---

# 108. Validation Scenario H — Obstruction superseded

If theorem $T_1$ is revised by a stronger theorem $T_2$, causing the old obstruction scope to shrink, then all closure events depending on the old scope enter a re-audit.

---

# 109. Validation Scenario I — False quotient

If two routes are merged merely due to lexical similarity, but their assumptions differ, they should be split back into different route classes.

This avoids false frontier contraction.

---

# 110. Validation Scenario J — NS scalar budget no-go

If the scalar/additive budget route is formally NO-GO, then:

$$
R_{\rm scalar}
\mapsto
\mathsf{BLOCKED}
$$

While:

$$
Q_{\rm NS}
$$

remains OPEN.

---

# 111. Validation Scenario K — NS survivor

If the DCRP shear/polarization branch has not yet been excluded by a theorem-level no-go, then:

$$
\sigma(R_{\rm sh/pol})=\mathsf{OPEN}.
$$

Even if other sibling branches are closed.

---

# 112. Validation Scenario L — Cross-series merge

Only if X72 and DCRP obstructions are confirmed identical via semantic/assumption/scope audit is it allowed that:

$$
O_{\rm X72}
\sim_{\rm obs}
O_{\rm DCRP}.
$$

---

# 113. Relationship Between CSM and LSI-PSD

LSI-PSD primarily answers:

> How do we observe, deduplicate, partition basins, and measure recurrence and obstruction confluence?

CSM further asks:

> Once these objects are established, how does the closure status become a computable, propagatable, revocable, and auditable graph-theoretic object?

Therefore:

$$
\boxed{
\text{LSI-PSD}
\subset
\text{CSM methodological substrate}.
}
$$

The $\subset$ here denotes inclusion in architectural utility, not asserting complete equivalence in history or theoretical ontology.

---

# 114. Relationship Between CSM and UCT

UCT provides:

- typed non-collapse;
- bridge certificate;
- debt;
- ledger;
- relative-global gate.

CSM instantiates these into the mathematical proof-space.

Therefore:

$$
\boxed{
\text{UCT}
\to
\text{CSM proof-space instantiation}.
}
$$

But CSM is not equivalent to the entirety of UCT.

---

# 115. First Major Research Proposition of CSM

$$
\boxed{
\textbf{Closure Propagation Conjecture}
}
$$

In a typed finite or finitely generated closure hypergraph, if all edge signatures, scope contracts, obstruction certificates, and revision events are decidable, then the relative-global closure status can be algorithmically reconstructed and replayed.

This is the core to be implemented at the runtime layer in the future.

---

# 116. Second Major Research Proposition

$$
\boxed{
\textbf{Frontier Fidelity Conjecture}
}
$$

If the quotient policy, route grammar, scope typing, and obstruction propagation all pass audit, then:

$$
\partial^\ast\mathfrak C(Q)
$$

is closer to the "truly unclosed independent proof obligations" than raw paper counts or raw route counts.

This paper does not assert that it equals the absolute proof frontier.

---

# 117. Third Major Research Proposition

$$
\boxed{
\textbf{Certified Exhaustion Principle}
}
$$

Only when:

$$
\mathsf{BranchDecomposition}
+
\mathsf{RouteCompleteness}
+
\mathsf{CertifiedObstructionClosure}
+
\mathsf{ScopeFidelity}
$$

hold simultaneously can route exhaustion be safely elevated to a parent-level closure conclusion.

---

# 118. Fourth Major Research Proposition

$$
\boxed{
\textbf{Reopenability Principle}
}
$$

In a long-term research system with a non-fixed theorem base, non-fixed representations, and non-fixed scopes, a blocked-route status should default to being re-auditable, rather than a permanent final state.

---

# 119. Direct Significance for NS

The most valuable part of the massive existing work on NS is not merely "it wasn't proven this time."

The true value is:

$$
\boxed{
\text{We have accumulated a massive amount of compilable obstructions, survivors, branch splits, scope corrections, and reopening evidence.}
}
$$

CSM allows these results to be assembled into a relative-global closure space for the first time.

---

# 120. Next Stage

Paper 03 should address:

$$
\boxed{
\textbf{Frontier Geometry, Cut Sets, and Relative Exhaustion}
}
$$

Namely:

- frontier topology / graph geometry;
- minimal cut;
- obstruction cover;
- route-completeness;
- exhaustion certificate;
- closure radius;
- reopened frontier;
- global-vs-relative proof boundary.

---

# 121. Conclusion

This paper transforms "route blocking" from a research narrative into a typed graph-theoretic operation.

Its core conclusions can be condensed as:

$$
\boxed{
\mathsf{RouteBlocked}
\neq
\mathsf{ClaimRefuted}.
}
$$

$$
\boxed{
\mathsf{BranchClosed}
\neq
\mathsf{ProblemClosed}.
}
$$

$$
\boxed{
\mathsf{LocalObstruction}
\neq
\mathsf{GlobalObstruction}.
}
$$

$$
\boxed{
\mathsf{RelativeClosure}
\neq
\mathsf{AbsoluteClosure}.
}
$$

And:

$$
\boxed{
\text{closure status must be typed, scoped, certified, versioned, and reopenable}.
}
$$

Only when these conditions are met can the long-term research history of a large-scale unsolved problem be transformed into a truly computable closure space, rather than just a pile of documents.

---

## Appendix A — CSM Paper 02 Minimal Invariants

1. blocked does not equal refuted;
2. branch closure does not equal problem closure;
3. obstructions must have an assumption envelope;
4. obstructions must have a scope envelope;
5. representation-specific obstructions must not cross representations without a certificate;
6. cross-domain propagation must have a bridge;
7. quotients do not delete provenance;
8. closure status can be nonmonotone;
9. the evidence ledger is not deleted;
10. reopening must have a certificate;
11. frontier contraction must prevent false contraction;
12. route exhaustion must have a route-completeness certificate;
13. local closure must not be stealthily elevated to absolute closure;
14. machine records must preserve versions;
15. all closure events must be replayable.

---

## Appendix B — CSM Series Dependencies

### Paper 00

Provides:

- Relative-Global Closure Space;
- typed research objects;
- closure status;
- frontier;
- debt;
- ledger;
- route-completeness obligation.

### Paper 01

Provides:

- Globality Typing Principle;
- scope contract;
- domain stratification;
- globality promotion certificate;
- NS formal / physical / generalized domain separation.

### Paper 02

Adds:

- typed closure hypergraph;
- obstruction propagation contract;
- closure family;
- noncommutative closure schedule;
- reopening operator;
- frontier contraction;
- branch decomposition certificate;
- route exhaustion machinery;
- NS graph compilation rules.

---

**END OF CSM PAPER 02 v0.1**