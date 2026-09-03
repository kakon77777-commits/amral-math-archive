# CSM Paper 07 — Closure Calculus, Composition Rules, and Proof-Carrying Operators

## Closure-Space Mathematics: Closure Calculus, Composition Rules, and Proof-Carrying Operators

**English Title:** *Closure-Space Mathematics: Closure Calculus, Composition Rules, and Proof-Carrying Operators*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 07  
**Version:** v0.1  
**Date:** 2026-08-27  
**Language:** en  
**Status:** Formal Theory / Executable Calculus Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline `$...$`; display `$$...$$`

---

## Abstract

This paper establishes the first version of the executable calculus core for Closure-Space Mathematics (CSM). Papers 00–06 have respectively established: relative-global closure spaces, globality typing, typed closure hypergraphs, frontier / cut / exhaustion, closure dynamics, projection invariants, and cross-domain transfer laws. This paper further converges these objects into a **proof-carrying closure calculus**, ensuring that closure operations are no longer merely descriptive rules, but verifiable operators with explicit input types, preconditions, scopes, output types, state transitions, certificates, debts, and versions.

The basic operator is written as:

$$
\boxed{
\mathcal O:
(X_1,\ldots,X_n;\Gamma)
\rightharpoonup
(Y_1,\ldots,Y_m;\Gamma')
}
$$

Where:

- $X_i$: input closure objects;
- $\Gamma$: scope, assumptions, representation, policy, and version environment;
- $Y_j$: output closure objects;
- The partial arrow $\rightharpoonup$ indicates that the operator may refuse execution due to insufficient type / scope / certificate / debt.

This paper proposes:

$$
\boxed{
\mathsf{PCO}
=
\langle
\mathsf{Signature},
\mathsf{Pre},
\mathsf{Transform},
\mathsf{Post},
\mathsf{Cert},
\mathsf{Debt},
\mathsf{Version}
\rangle
}
$$

referred to as the **Proof-Carrying Closure Operator**.

Upon execution, the operator must not only output the result, but must also output:

$$
\boxed{
\text{result}
+
\text{certificate}
+
\text{debt delta}
+
\text{ledger event}.
}
$$

This paper establishes the first version of the operator family:

1. $\mathsf{Infer}$: implication closure;
2. $\mathsf{Block}$: obstruction propagation;
3. $\mathsf{Refute}$: claim-level negative closure;
4. $\mathsf{Prove}$: claim-level positive closure;
5. $\mathsf{Condition}$: conditional closure;
6. $\mathsf{Bridge}$: cross-domain / cross-representation lift;
7. $\mathsf{Project}$: native-to-view projection;
8. $\mathsf{Transfer}$: cross-domain authority transfer;
9. $\mathsf{Quotient}$: semantic / route / obstruction quotient;
10. $\mathsf{Split}$: revokes excessive quotienting;
11. $\mathsf{Reopen}$: reopens a closure;
12. $\mathsf{Discharge}$: discharges debt;
13. $\mathsf{Cut}$: cut certification;
14. $\mathsf{Cover}$: obstruction cover;
15. $\mathsf{Exhaust}$: relative exhaustion;
16. $\mathsf{Promote}$: globality / authority promotion;
17. $\mathsf{Replay}$: ledger reconstruction;
18. $\mathsf{Compile}$: runtime / graph / view compilation.

This paper particularly emphasizes that the composition of closure operators is not free. Even if:

$$
\mathcal O_1
\quad\text{and}\quad
\mathcal O_2
$$

are individually legal, it does not mean that:

$$
\mathcal O_2\circ\mathcal O_1
$$

is legal. Composition requires:

$$
\boxed{
\mathsf{CompCert}(\mathcal O_1,\mathcal O_2).
}
$$

This paper therefore defines:

- type composability;
- scope composability;
- certificate composability;
- debt composability;
- authority monotonicity;
- version coherence;
- bridge coherence;
- projection closure-commutation;
- transfer conservation;
- reopening invalidation.

This paper proposes the first version of the **Closure Normal Form**:

$$
\boxed{
\mathsf{CNF}
=
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Infer}
\to
\mathsf{Propagate}
\to
\mathsf{Resolve}
\to
\mathsf{Rebuild}
\to
\mathsf{Project}.
}
$$

Where `Project` is executed by default after the native closure state is completed; if incremental projection is adopted, it must be accompanied by the incremental materialization certificate defined in Paper 05.

Finally, this paper defines the minimal interface for the NS closure graph compiler. The `CLOSED`, `OPEN`, `NO-GO`, `SURVIVOR`, `STOP`, and `CONDITIONAL` labels from past NS documents will no longer directly become graph statuses. Instead, they must first be parsed into claim / assumption / scope / certificate candidates, and then the closure calculus will determine their true status. Thus, starting from this paper, CSM acquires the formal foundation to directly enter a reference runtime.

---

# 1. Research Positioning

CSM Papers 00–06 have provided:

$$
\text{Objects}
+
\text{Graphs}
+
\text{Dynamics}
+
\text{Projection}
+
\text{Transfer}.
$$

This paper adds:

$$
\boxed{
\text{Executable Closure Calculus}.
}
$$

---

# 2. Closure Judgment

Define the closure judgment:

$$
\boxed{
\Gamma
\vdash
x
:
\tau
\;[\sigma]
\;\{\chi\}
\;\langle d\rangle
}
$$

Where:

- $\Gamma$: closure environment;
- $x$: object;
- $\tau$: object type;
- $\sigma$: closure status;
- $\chi$: certificate set;
- $d$: debt set.

---

# 3. Closure Environment

$$
\boxed{
\Gamma
=
(
D,
A,
\rho,
\Gamma_R,
\mathcal T,
\mathcal B,
\mathcal P,
\nu
).
}
$$

Where:

- $D$: domain / scope;
- $A$: active assumptions;
- $\rho$: representation;
- $\Gamma_R$: route grammar;
- $\mathcal T$: theorem base;
- $\mathcal B$: bridge set;
- $\mathcal P$: policy;
- $\nu$: version.

---

# 4. Judgment Noncollapse

The same object can have different statuses under different $\Gamma$:

$$
\Gamma_1\vdash x[\mathsf{OPEN}],
$$

$$
\Gamma_2\vdash x[\mathsf{BLOCKED}].
$$

Therefore:

$$
\boxed{
\sigma(x)
\text{ is environment-indexed}.
}
$$

---

# 5. Proof-Carrying Closure Operator

Define:

$$
\boxed{
\mathsf{PCO}
=
\langle
\mathsf{Signature},
\mathsf{Pre},
\mathsf{Transform},
\mathsf{Post},
\mathsf{Cert},
\mathsf{Debt},
\mathsf{Version}
\rangle.
}
$$

---

# 6. Operator Signature

$$
\boxed{
\mathsf{Sig}(\mathcal O)
:
(\tau_1,\ldots,\tau_n)
\to
(\tau'_1,\ldots,\tau'_m).
}
$$

---

# 7. Operator Preconditions

$$
\mathsf{Pre}(\mathcal O,\Gamma,X)
$$

May at least include:

- type;
- scope;
- assumptions;
- target fidelity;
- bridge validity;
- certificate presence;
- representation compatibility;
- version freshness.

---

# 8. Operator Transform

$$
\mathsf{Transform}_{\mathcal O}
(X,\Gamma)
=
Y.
$$

---

# 9. Operator Postconditions

$$
\mathsf{Post}_{\mathcal O}(Y,\Gamma')
$$

Defines the output's:

- status;
- authority;
- debt;
- provenance;
- ledger event.

---

# 10. Operator Certificate

Every theorem-level operator execution generates:

$$
\boxed{
\chi_{\mathcal O}.
}
$$

---

# 11. Operator Debt Delta

Define:

$$
\boxed{
\Delta d_{\mathcal O}
=
d_{\rm out}
\setminus
d_{\rm in}.
}
$$

---

# 12. Operator Ledger Event

$$
e_{\mathcal O}
=
\langle
\mathcal O,
X,
Y,
\Gamma,
\Gamma',
\chi,
\Delta d,
\nu
\rangle.
$$

---

# 13. Fail-Closed Rule

If any theorem-critical gate in the precondition FAILs:

$$
\boxed{
\mathcal O(X)
=
\mathsf{REFUSE}.
}
$$

It must not stealthily upgrade the status on a best-effort basis.

---

# 14. Defer Rule

If information is insufficient but not proven illegal:

$$
\boxed{
\mathcal O(X)
=
\mathsf{DEFER}
}
$$

and adds debt.

---

# 15. Refuse is Distinct from Defer

$$
\boxed{
\mathsf{REFUSE}
\neq
\mathsf{DEFER}.
}
$$

---

# 16. Operator Family

First version:

$$
\boxed{
\mathfrak O_{\rm calc}
=
\{
\mathsf{Infer},
\mathsf{Block},
\mathsf{Refute},
\mathsf{Prove},
\mathsf{Condition},
\mathsf{Bridge},
\mathsf{Project},
\mathsf{Transfer},
\mathsf{Quotient},
\mathsf{Split},
\mathsf{Reopen},
\mathsf{Discharge},
\mathsf{Cut},
\mathsf{Cover},
\mathsf{Exhaust},
\mathsf{Promote},
\mathsf{Replay},
\mathsf{Compile}
\}.
}
$$

---

# 17. Infer Operator

$$
\mathsf{Infer}:
(\mathsf{Claim}^n,\mathsf{Lemma})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 18. Infer Preconditions

Requires:

- implication certificate;
- assumptions satisfied;
- scope compatible;
- version current.

---

# 19. Infer Output

If the proof is complete:

$$
\sigma=\mathsf{CLOSED}^{+}.
$$

If the assumptions are not closed:

$$
\sigma=\mathsf{CONDITIONAL}.
$$

---

# 20. Block Operator

$$
\mathsf{Block}:
(\mathsf{Obstruction},\mathsf{RouteState})
\rightharpoonup
\mathsf{RouteState}.
$$

---

# 21. Block Preconditions

Requires:

$$
\mathsf{OPCert}
=
\mathsf{PASS}.
$$

---

# 22. Block Output

Typically:

$$
\mathsf{OPEN}
\to
\mathsf{BLOCKED}.
$$

---

# 23. Block Cannot Refute Claim

$$
\boxed{
\mathsf{Block}
\neq
\mathsf{Refute}.
}
$$

---

# 24. Refute Operator

$$
\mathsf{Refute}:
(\mathsf{Claim},\mathsf{Counterexample/NoGoCert})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 25. Refute Output

$$
\boxed{
\sigma=\mathsf{CLOSED}^{-}.
}
$$

---

# 26. Prove Operator

$$
\mathsf{Prove}:
(\mathsf{Claim},\mathsf{ProofCert})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 27. Prove Output

$$
\boxed{
\sigma=\mathsf{CLOSED}^{+}.
}
$$

---

# 28. Condition Operator

$$
\mathsf{Condition}:
(\mathsf{Claim},\mathsf{AssumptionSet})
\rightharpoonup
\mathsf{Claim}.
$$

---

# 29. Condition Output

$$
\boxed{
\sigma=\mathsf{CONDITIONAL}.
}
$$

---

# 30. Bridge Operator

$$
\mathsf{Bridge}:
(x_A,\mathsf{BridgeCert}_{A\to B})
\rightharpoonup
x_B.
$$

---

# 31. Bridge Preconditions

- source object valid;
- bridge active;
- scope map valid;
- target type defined;
- loss/debt declared.

---

# 32. Bridge Output Authority

Authority is determined by the bridge cert, not automatically copied from the source status.

---

# 33. Project Operator

$$
\mathsf{Project}:
\mathfrak C^{\rm nat}
\rightharpoonup
\mathcal V.
$$

---

# 34. Project Preconditions

Requires:

$$
\mathsf{ProjCert}.
$$

---

# 35. Project Cannot Upgrade Authority

$$
\boxed{
\mathsf{Authority}(\mathcal V)
\le
\mathsf{Authority}(\mathfrak C^{\rm nat}).
}
$$

---

# 36. Transfer Operator

$$
\mathsf{Transfer}:
x_A
\rightharpoonup
x_B.
$$

---

# 37. Transfer Preconditions

Requires:

$$
\mathsf{TContract},
\quad
\mathsf{BridgeCert}.
$$

---

# 38. Transfer Output

Can be:

- conservative;
- lossy;
- undefined.

---

# 39. Quotient Operator

$$
\mathsf{Quotient}:
(x_1,\ldots,x_n)
\rightharpoonup
[x]_\sim.
$$

---

# 40. Quotient Preconditions

Requires equivalence evidence.

---

# 41. Quotient No-Go

Embedding / lexical similarity is insufficient to execute a theorem-level quotient.

---

# 42. Split Operator

$$
\mathsf{Split}:
[x]_\sim
\rightharpoonup
(x_1,\ldots,x_n).
$$

---

# 43. Split Trigger

- false equivalence;
- assumption divergence;
- scope divergence;
- representation semantic divergence.

---

# 44. Split Output

Typically triggers:

$$
\text{frontier rebuild}.
$$

---

# 45. Reopen Operator

$$
\mathsf{Reopen}:
(\mathsf{Blocked/ClosedObject},\mathsf{ReopenCert})
\rightharpoonup
\mathsf{ReopenedObject}.
$$

---

# 46. Reopen Preconditions

Requires an invalidated premise / bridge / theorem / scope.

---

# 47. Reopen Output

$$
\boxed{
\sigma=\mathsf{REOPENED}.
}
$$

---

# 48. Discharge Operator

$$
\mathsf{Discharge}:
(d,\chi_d)
\rightharpoonup
\varnothing.
$$

---

# 49. Discharge Preconditions

A debt-specific certificate.

---

# 50. Discharge Cascade

Discharging a parent debt may upgrade a downstream CONDITIONAL to CLOSED.

---

# 51. Cut Operator

$$
\mathsf{Cut}:
(\mathcal R,C)
\rightharpoonup
\mathsf{CutCert}.
$$

---

# 52. Cut Preconditions

The route grammar + route completeness scope must be explicit.

---

# 53. Cover Operator

$$
\mathsf{Cover}:
(\mathcal R,\mathcal O)
\rightharpoonup
\mathsf{CoverCert}.
$$

---

# 54. Exhaust Operator

$$
\mathsf{Exhaust}:
(
\mathsf{RCCert},
\mathsf{CutCert},
\mathsf{CoverCert}
)
\rightharpoonup
\mathsf{RECert}.
$$

---

# 55. Exhaust Preconditions

There must be no uncovered admissible routes.

---

# 56. Exhaust Output

Only generates a relative exhaustion level.

---

# 57. Promote Operator

$$
\mathsf{Promote}:
(
x_{D_0},
\mathsf{PromotionCert}_{D_0\to D_1}
)
\rightharpoonup
x_{D_1}.
$$

---

# 58. Promote Preconditions

- quantifier lift;
- scope;
- uniformity;
- representation;
- bridge;
- debt.

---

# 59. Promote No-Go

$$
\boxed{
\text{local theorem}
\not\Rightarrow
\text{global theorem}.
}
$$

---

# 60. Replay Operator

$$
\mathsf{Replay}:
(\mathsf{Ledger},\mathsf{Policy})
\to
\mathfrak C.
$$

---

# 61. Replay Determinism

Should be deterministic under a fixed ledger + policy.

---

# 62. Compile Operator

$$
\mathsf{Compile}:
\mathfrak C
\rightharpoonup
\mathsf{RuntimeArtifact}.
$$

---

# 63. Compile Preconditions

Requires a projection / serialization contract.

---

# 64. Compile Authority

The runtime artifact authority must not exceed the source state.

---

# 65. Composition

Let:

$$
\mathcal O_1:
A\rightharpoonup B,
$$

$$
\mathcal O_2:
B\rightharpoonup C.
$$

Formally written as:

$$
\mathcal O_2\circ\mathcal O_1.
$$

---

# 66. Type Composability

Requires:

$$
\operatorname{cod}(\mathcal O_1)
\subseteq
\operatorname{dom}(\mathcal O_2).
$$

---

# 67. Scope Composability

$$
\Gamma_1'
$$

must satisfy the scope preconditions of $\mathcal O_2$.

---

# 68. Certificate Composability

If $\chi_1$ is a prerequisite for $\mathcal O_2$, it must be verifiable.

---

# 69. Debt Composability

If $\mathcal O_1$ generates unresolved debt, $\mathcal O_2$ must not pretend to be debt-free.

---

# 70. Version Composability

Both operators must execute on compatible versions.

---

# 71. Authority Composability

Downstream operators must not upgrade upstream authority without a certificate.

---

# 72. Composition Certificate

$$
\boxed{
\mathsf{CompCert}(
\mathcal O_1,\mathcal O_2
).
}
$$

---

# 73. Composition Failure

If any of:

- type;
- scope;
- cert;
- debt;
- version;
- authority;

is incompatible:

$$
\boxed{
\mathcal O_2\circ\mathcal O_1
=
\mathsf{REFUSE}.
}
$$

---

# 74. Associativity Warning

Even if three operators are pairwise composable, it does not automatically guarantee:

$$
(\mathcal O_3\circ\mathcal O_2)\circ\mathcal O_1
=
\mathcal O_3\circ(\mathcal O_2\circ\mathcal O_1).
$$

---

# 75. Associativity Debt

If the composition introduces different intermediate debt / scope, it requires:

$$
\mathsf{AssocCert}.
$$

---

# 76. Commutation

If:

$$
\mathcal O_1\mathcal O_2
=
\mathcal O_2\mathcal O_1,
$$

they are said to commute.

---

# 77. Noncommuting Operator Pair

Typically:

$$
\mathsf{Quotient}
$$

and:

$$
\mathsf{Block}
$$

may not commute.

---

# 78. Reopen–Project Noncommutation

If the view does not support invalidation:

$$
\mathsf{Project}\circ\mathsf{Reopen}
\neq
\mathsf{Reopen}^{\Pi}\circ\mathsf{Project}.
$$

---

# 79. Transfer–Refute Noncommutation

Source refutation may not necessarily transfer to the target.

---

# 80. Operator Authority Order

Define:

$$
\mathcal O_1
\preceq_{\rm auth}
\mathcal O_2
$$

if $\mathcal O_2$ can produce a higher authority output.

---

# 81. Authority Inflation No-Go

Operator composition must not arbitrarily inflate:

$$
\boxed{
A_{\rm out}
>
\max A_{\rm input}
}
$$

unless the composition includes a new theorem / promotion cert.

---

# 82. Proof-Carrying Composition

A legal composition must output a composite cert:

$$
\boxed{
\chi_{2\circ1}.
}
$$

---

# 83. Composite Debt

$$
\boxed{
d_{2\circ1}
=
\mathsf{Map}(d_1)
\cup
d_2
\cup
d_{\rm comp}.
}
$$

---

# 84. Operator Normalization

The same closure effect may be generated by multiple operator sequences.

Normalization is required.

---

# 85. Closure Normal Form

First version:

$$
\boxed{
\mathsf{CNF}
=
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Infer}
\to
\mathsf{Propagate}
\to
\mathsf{Resolve}
\to
\mathsf{Rebuild}
\to
\mathsf{Project}.
}
$$

---

# 86. Normalize Phase

Executes:

- canonical identity;
- scope normalization;
- assumption normalization;
- representation normalization;
- quotient candidates.

---

# 87. Validate Phase

Validates:

- certs;
- theorem status;
- versions;
- bridge;
- provenance.

---

# 88. Infer Phase

Executes implication / conditional theorem inference.

---

# 89. Propagate Phase

Executes obstruction / bridge / debt propagation.

---

# 90. Resolve Phase

Handles:

- prove;
- refute;
- block;
- discharge;
- reopen;
- split / merge.

---

# 91. Rebuild Phase

Rebuilds:

- frontier;
- cuts;
- covers;
- exhaustion;
- fixed-point candidates.

---

# 92. Project Phase

Generates based on use case:

- audit;
- research;
- visual;
- execution view.

---

# 93. CNF Does Not Require Uniqueness

Different legal schedules may equally result in a closure-equivalent state.

---

# 94. CNF Goal

The goal is not a theorem proof normal form.

Rather, it is a canonical discipline for runtime state transitions.

---

# 95. Proof-Carrying Operator Graph

Every runtime operation itself also forms a graph:

$$
\boxed{
\mathcal G_{\rm op}.
}
$$

---

# 96. Operator Node

Nodes are operator instances:

$$
o_i.
$$

---

# 97. Operator Edge

If the output of $o_i$ is the input of $o_j$:

$$
o_i\to o_j.
$$

---

# 98. Operator DAG

A single closure transaction should ideally form a DAG.

---

# 99. Operator Cycle

If replay / reopen / split exist, cycles can form across transactions.

---

# 100. Transaction

Define:

$$
\boxed{
\mathsf{ClosureTxn}
}
$$

as a set of atomic closure operations.

---

# 101. Transaction Preconditions

- version head;
- policy;
- input hashes;
- cert availability.

---

# 102. Transaction Commit

Success:

$$
\mathsf{COMMIT}.
$$

Failure:

$$
\mathsf{ABORT}.
$$

---

# 103. Partial Commit No-Go

Theorem-level status mutations do not allow unrecorded partial commits.

---

# 104. Transaction Ledger

Each transaction generates:

- input state hash;
- event list;
- output state hash;
- cert list;
- debt delta.

---

# 105. Idempotence

Certain operators should satisfy:

$$
\mathcal O(\mathcal O(x))
=
\mathcal O(x).
$$

For example, a normalized Normalize.

---

# 106. Non-Idempotent Operators

Reopen / Transfer / Promote are not necessarily idempotent.

---

# 107. Idempotence Certificate

The runtime can tag whether an operator is:

- idempotent;
- monotone;
- reversible;
- lossy.

---

# 108. Monotone Operator

For a fixed environment:

$$
X\preceq Y
\Rightarrow
\mathcal O(X)\preceq\mathcal O(Y).
$$

It is not assumed that all operators are monotone.

---

# 109. Reversible Operator

If there is a verified inverse:

$$
\mathcal O^{-1}.
$$

---

# 110. Lossy Operator

Projection / Transfer can be lossy.

---

# 111. Operator Effect Type

$$
\mathsf{Effect}
\in
\{
\mathsf{READ},
\mathsf{STATUS},
\mathsf{GRAPH},
\mathsf{DEBT},
\mathsf{SCOPE},
\mathsf{VERSION},
\mathsf{VIEW}
\}.
$$

---

# 112. Read-Only Operator

For example, query / inspect.

---

# 113. Mutating Operator

For example, Refute / Reopen / Quotient.

---

# 114. Mutation Authority

A mutating operator must have an authority level.

---

# 115. Operator Capability Boundary

The runtime should not allow a visualization operator to mutate native theorem status.

---

# 116. Proof-Carrying Mutation

Every native status mutation:

$$
\boxed{
\text{mutation}
+
\text{cert}
+
\text{ledger}
}
$$

is inseparable.

---

# 117. Closure Query Calculus

In addition to mutation, query is also defined:

$$
\mathsf{Query}_{\rm Cl}.
$$

---

# 118. Query Types

- status;
- frontier;
- cut membership;
- obstruction coverage;
- debt;
- transferability;
- replay history.

---

# 119. Query Authority

Query results must tag the native / projected source.

---

# 120. Query on Projection

If a query exceeds projection authority:

$$
\boxed{
\mathsf{REFUSE}.
}
$$

---

# 121. Proof-Carrying Refusal

A refusal may also attach:

- missing invariant;
- missing cert;
- missing scope;
- required rehydration.

---

# 122. Closure Exception

If an operator encounters an unclassified case:

$$
\mathsf{UNKNOWN}.
$$

Do not automatically set to BLOCKED.

---

# 123. UNKNOWN vs DEFER

UNKNOWN indicates that the semantic status is unclear.

DEFER indicates that the current execution lacks information.

---

# 124. Runtime Status Lattice

Can use the operational partial order:

$$
\mathsf{UNKNOWN},
\mathsf{OPEN},
\mathsf{CONDITIONAL},
\mathsf{BLOCKED},
\mathsf{REOPENED},
\mathsf{CLOSED}^{+},
\mathsf{CLOSED}^{-},
\mathsf{STALE}.
$$

This paper does not claim it is a single linear lattice.

---

# 125. Status Transition Table

Legal examples:

$$
\mathsf{OPEN}
\to
\mathsf{BLOCKED},
$$

$$
\mathsf{BLOCKED}
\to
\mathsf{REOPENED},
$$

$$
\mathsf{CONDITIONAL}
\to
\mathsf{CLOSED}^{+},
$$

$$
\mathsf{CLOSED}^{+}
\to
\mathsf{STALE}.
$$

---

# 126. Illegal Direct Transition

For example:

$$
\mathsf{BLOCKED}
\to
\mathsf{CLOSED}^{-}
$$

is illegal without a RefuteCert.

---

# 127. Transition Certificate

Every status transition has:

$$
\boxed{
\mathsf{StatusTransCert}.
}
$$

---

# 128. Debt-Carrying Status

The same status can have different debts:

$$
\mathsf{CONDITIONAL}\langle d_1\rangle,
$$

$$
\mathsf{CONDITIONAL}\langle d_2\rangle.
$$

---

# 129. Certificate Stack

Outputting a theorem-level closure requires:

$$
\boxed{
\mathsf{CertStack}
}
$$

---

# 130. CertStack Example

$$
\mathsf{StatementCert}
+
\mathsf{ScopeCert}
+
\mathsf{ProofCert}
+
\mathsf{BridgeCert}
+
\mathsf{VersionCert}.
$$

---

# 131. Certificate Minimality

It is not necessary to attach the full corpus every time.

But traceable refs are required.

---

# 132. Proof-Carrying Reference

A certificate can be:

- proof object;
- theorem reference;
- validation artifact;
- executable check;
- hash-locked source.

---

# 133. Runtime Trust Model

The CSM runtime does not automatically treat natural language claims as theorems.

---

# 134. Source Extraction Boundary

Natural language artifacts first go through:

$$
\mathsf{Extract}
$$

to generate candidate objects.

---

# 135. Extract Operator

$$
\mathsf{Extract}:
\mathsf{Artifact}
\rightharpoonup
\mathsf{CandidateGraph}.
$$

---

# 136. Candidate Status

Extract output defaults to:

$$
\mathsf{UNVERIFIED}.
$$

---

# 137. Candidate-to-Native Promotion

Requires:

$$
\mathsf{Validate}.
$$

---

# 138. NS Document Compiler

For NS documents:

$$
\boxed{
\mathsf{NSCompile}
:
\mathsf{PaperArtifact}
\rightharpoonup
\mathsf{ClosureCandidateGraph}.
}
$$

---

# 139. NS Label Parsing

Original:

`CLOSED`

must not directly become:

$$
\mathsf{CLOSED}^{+}.
$$

---

# 140. NS CLOSED Candidate

First generates:

$$
\mathsf{StatusCandidate}(\texttt{CLOSED}).
$$

---

# 141. NS NO-GO Candidate

First generates:

$$
\mathsf{ObstructionCandidate}.
$$

---

# 142. NS SURVIVOR Candidate

First generates:

$$
\mathsf{RouteStateCandidate}.
$$

---

# 143. NS STOP Candidate

First generates:

$$
\mathsf{FrontierCandidate}.
$$

---

# 144. NS OPEN Candidate

First generates:

$$
\mathsf{OpenClaimCandidate}.
$$

---

# 145. NS Validation Pass

Then extracts:

- statement;
- assumptions;
- scope;
- theorem source;
- proof/check;
- dependencies;
- version.

---

# 146. NS Closure Promotion

Only executed after validation:

$$
\mathsf{Prove},
\mathsf{Block},
\mathsf{Refute},
\mathsf{Condition}.
$$

---

# 147. NS Cross-Series Composition

For example:

$$
\mathsf{Extract}_{\rm X72}
\to
\mathsf{Normalize}
\to
\mathsf{Transfer}_{\rm X72\to DCRP}
\to
\mathsf{Block}.
$$

Every step requires a cert.

---

# 148. NS False Merge Prevention

If the transfer cert is insufficient:

$$
\mathsf{Quotient}
=
\mathsf{REFUSE}.
$$

---

# 149. NS Runtime Transaction

A new paper enters:

$$
\boxed{
\mathsf{Ingest}
\to
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{ApplyClosure}
\to
\mathsf{Rebuild}
\to
\mathsf{Snapshot}.
}
$$

---

# 150. NS Snapshot

Outputs:

- native graph hash;
- frontier;
- active obstructions;
- survivors;
- debt;
- cuts;
- exhaustion level;
- version.

---

# 151. NS View Compile

Then:

$$
\mathsf{Project}
$$

generates:

- overview;
- audit;
- frontier;
- obstruction;
- survivor views.

---

# 152. Runtime Proof Boundary

Graph mining / clustering / LLM extraction do not possess theorem mutation authority.

---

# 153. Human/AI Audit Boundary

Certain Certs can be provided by:

- theorem prover;
- symbolic checker;
- independent audit;
- human review.

---

# 154. Mixed Verification

Different cert sources can be composed, but provenance is required.

---

# 155. Machine Schema — Operator

```yaml
closure_operator:
  operator_id:
  operator_type:
  input_types: []
  output_types: []
  preconditions: []
  scope_requirements: []
  certificate_requirements: []
  debt_behavior:
  authority_effect:
  version:
```

---

# 156. Machine Schema — Operator Instance

```yaml
operator_instance:
  instance_id:
  operator_id:
  input_object_ids: []
  environment_id:
  precondition_results: {}
  output_object_ids: []
  output_statuses: {}
  certificate_ids: []
  debt_added: []
  debt_discharged: []
  ledger_event_id:
  result:
```

---

# 157. Machine Schema — Composition

```yaml
operator_composition:
  composition_id:
  operator_instances: []
  type_compatible:
  scope_compatible:
  certificate_compatible:
  debt_compatible:
  version_compatible:
  authority_compatible:
  composition_certificate:
  result:
```

---

# 158. Machine Schema — Closure Transaction

```yaml
closure_transaction:
  txn_id:
  input_state_hash:
  policy_id:
  version:
  operator_instances: []
  certificate_ids: []
  debt_delta:
  output_state_hash:
  commit_status:
```

---

# 159. Machine Schema — NS Compiler

```yaml
ns_closure_compiler:
  artifact_ref:
  extracted_claims: []
  extracted_assumptions: []
  extracted_scopes: []
  extracted_dependencies: []
  label_candidates: []
  certificate_candidates: []
  normalization_status:
  validation_status:
  closure_operator_plan: []
  native_graph_delta:
```

---

# 160. Validation Scenario A — Block is not Refute

Input obstruction + route.

expected:

$$
\mathsf{OPEN}\to\mathsf{BLOCKED},
$$

parent claim unchanged.

---

# 161. Validation Scenario B — Refute requires counterexample/no-go cert

No cert.

expected: REFUSE.

---

# 162. Validation Scenario C — Conditional to Proven

Debt discharge satisfies assumptions.

expected: CONDITIONAL -> CLOSED_POSITIVE.

---

# 163. Validation Scenario D — Invalid composition

Project visual-only view then Refute on view.

expected: composition REFUSE.

---

# 164. Validation Scenario E — Valid projection composition

Audit projection with proof-fidelity cert then read-only query.

expected: PASS.

---

# 165. Validation Scenario F — Transfer authority downgrade

Lossy transfer theorem source to broader target.

expected: authority lowered + debt added.

---

# 166. Validation Scenario G — Reopen stale downstream

Invalidated common premise.

expected: Reopen + rebuild frontier.

---

# 167. Validation Scenario H — Quotient then split

False equivalence discovered.

expected: split + restore histories + frontier rebuild.

---

# 168. Validation Scenario I — Exhaust relative only

RCCert/Cut/Cover PASS.

expected: relative exhaustion cert, not absolute claim proof without parent bridge.

---

# 169. Validation Scenario J — NS NO-GO parsing

Document says NO-GO.

expected: obstruction candidate, not native CLOSED_NEGATIVE.

---

# 170. Validation Scenario K — NS STOP parsing

Document says STOP-D105.

expected: frontier candidate.

---

# 171. Validation Scenario L — Authority inflation cycle

ANALOGY -> STRUCTURE -> THEOREM without new cert.

expected: FAIL.

---

# 172. Core No-Go 1

$$
\boxed{
\text{operator exists}
\not\Rightarrow
\text{operator application legal}.
}
$$

---

# 173. Core No-Go 2

$$
\boxed{
\text{two legal operators}
\not\Rightarrow
\text{legal composition}.
}
$$

---

# 174. Core No-Go 3

$$
\boxed{
\text{composition path}
\not\Rightarrow
\text{associative composition}.
}
$$

---

# 175. Core No-Go 4

$$
\boxed{
\text{result}
\not\Rightarrow
\text{certified result}.
}
$$

---

# 176. Core No-Go 5

$$
\boxed{
\text{same output status}
\not\Rightarrow
\text{same certificate strength}.
}
$$

---

# 177. Core No-Go 6

$$
\boxed{
\text{runtime success}
\not\Rightarrow
\text{mathematical theorem}.
}
$$

---

# 178. Core No-Go 7

$$
\boxed{
\text{compiled graph}
\not\Rightarrow
\text{canonical native truth}.
}
$$

---

# 179. Core No-Go 8

$$
\boxed{
\text{automatic extraction}
\not\Rightarrow
\text{automatic theorem status}.
}
$$

---

# 180. Paper 07 Core Proposition 1

## Proof-Carrying Operator Principle

Any theorem-level closure mutation must be executed by a proof-carrying operator; its output must at least include the result, certificate, debt delta, and ledger event.

---

# 181. Paper 07 Core Proposition 2

## Composition Safety Principle

Legal operator composition requires type, scope, certificate, debt, version, and authority compatibilities to all pass simultaneously.

---

# 182. Paper 07 Core Proposition 3

## Authority Noninflation Principle

Operator composition without a new theorem / promotion certificate must not increase closure authority.

---

# 183. Paper 07 Core Proposition 4

## Fail-Closed Mutation Principle

When a theorem-critical precondition fails, the runtime must refuse native status mutation, rather than continuing on a best-effort basis.

---

# 184. Paper 07 Core Proposition 5

## Closure Normal Form Principle

For most artifact-driven closure updates, the following can be prioritized:

$$
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Infer}
\to
\mathsf{Propagate}
\to
\mathsf{Resolve}
\to
\mathsf{Rebuild}
\to
\mathsf{Project}.
$$

---

# 185. Paper 07 Core Proposition 6

## Candidate-to-Native Firewall

Any object obtained from natural language, images, LLM extraction, or heuristic mining can by default only enter the Candidate Layer; it can only enter the Native Closure Layer after passing the validation / certificate gate.

---

# 186. Paper 07 Core Proposition 7

## NS Compiler Safety Principle

The `CLOSED / OPEN / NO-GO / SURVIVOR / STOP / CONDITIONAL` labels from past NS documents must all first be compiled into candidate objects, and must not directly control native theorem status.

---

# 187. Integration with Papers 00–06

Paper 00:
- closure object model.

Paper 01:
- scope / globality types.

Paper 02:
- graph / obstruction / reopening.

Paper 03:
- frontier / cut / exhaustion.

Paper 04:
- event dynamics / replay.

Paper 05:
- projection / attention / compilation.

Paper 06:
- cross-domain transfer / authority.

Paper 07:
- proof-carrying executable calculus.

---

# 188. Reference Runtime Boundary

Starting from this paper, the theory is sufficient to design:

$$
\boxed{
\textbf{CSM Reference Runtime v0.1}
}
$$

However, the runtime is not yet implemented in this paper.

---

# 189. Runtime MVP Minimal Capabilities

1. parse canonical records;
2. validate type signatures;
3. store native graph;
4. execute PCOs;
5. maintain status ledger;
6. propagate obstruction;
7. reopen stale routes;
8. calculate frontier;
9. build cuts/covers;
10. track debt;
11. transfer / project;
12. replay;
13. export snapshots.

---

# 190. NS Runtime MVP

NS can serve as the first large-scale dataset.

But first establish:

$$
\boxed{
\text{NS Relative-Global Closure Graph v0.1}
}
$$

before performing theorem automation.

---

# 191. Paper 08 Roadmap

The next paper should address:

$$
\boxed{
\textbf{Closure-Space Runtime Semantics and Executable Reference Model}
}
$$

Contents:

- machine state;
- transition system;
- deterministic replay;
- transaction semantics;
- certificate registry;
- debt registry;
- graph storage;
- query language;
- compiler interfaces;
- NS ingestion profile;
- conformance tests.

---

# 192. Conclusion

Up to Paper 06, CSM already possesses complete theoretical objects, but it may still remain at the level of:

> We know how closure should operate.

The goal of Paper 07 is to transform this into:

> Exactly which operator the system allows to change which closure status under what preconditions.

Therefore, the core of this paper is not to add more terminology, but to establish:

$$
\boxed{
\text{typed inputs}
+
\text{preconditions}
+
\text{operator effect}
+
\text{certificate}
+
\text{debt}
+
\text{ledger}.
}
$$

The most important safety principles are:

$$
\boxed{
\text{no proof-carrying certificate}
\Rightarrow
\text{no theorem-level mutation}.
}
$$

and:

$$
\boxed{
\text{two legal steps}
\not\Rightarrow
\text{one legal composition}.
}
$$

This ensures that the closure space is no longer just a graph, but begins to become a mathematical computing system that can be executed, verified, refused, replayed, and compiled.

For NS, this is also a highly critical step: the various status labels in hundreds of past research drafts no longer directly dictate our judgments. Instead, they are first extracted, normalized, and validated, and then the closure calculus determines which route they can truly close, under which scope they are valid, whether they can be transferred across series, whether there is still debt, and when they should be reopened.

This is the true transition from:

$$
\boxed{
\text{Pile of research literature}
}
$$

truly moving towards:

$$
\boxed{
\text{Executable relative-global closure space}.
}
$$

---

## Appendix A — Paper 07 Core Invariants

1. theorem-level mutation must be proof-carrying;
2. operator application must pass preconditions;
3. operator composition must have a CompCert;
4. debt must not disappear during composition;
5. authority must not inflate without a certificate;
6. Block is not equal to Refute;
7. Project must not upgrade native authority;
8. Transfer must not automatically copy source status;
9. Quotient must have equivalence evidence;
10. Split must be able to restore search history;
11. Reopen must have invalidated-condition evidence;
12. Exhaust can only generate relative exhaustion;
13. Promote must have a globality / authority cert;
14. Candidate layer must not directly modify the Native Closure Layer;
15. runtime success does not equal a theorem proof.

---

## Appendix B — Series Dependencies

### Paper 00
Relative-Global Closure Space

### Paper 01
Scope / Globality Typing

### Paper 02
Typed Closure Graph / Obstruction

### Paper 03
Frontier / Cut / Exhaustion

### Paper 04
Closure Dynamics / Replay / Reopening

### Paper 05
Projection / Attention / Compilation

### Paper 06
Cross-Domain Transfer / Authority Conservation

### Paper 07
Proof-Carrying Closure Calculus / Composition / Runtime Semantics Interface

---

**END OF CSM PAPER 07 v0.1**