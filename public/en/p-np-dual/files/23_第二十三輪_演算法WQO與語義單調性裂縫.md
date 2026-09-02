```markdown
# P/NP Debate Game Research Area | Round 23

## Algorithmic WQO and the Semantic-Monotonicity Gap: Why Graph-Minor-Style Finite Obstructions Do Not Transfer Directly to P vs NP

- **Lead Researcher:** Neo.K (Chuan-Wei Hsu)
- **Collaborative Organization:** Aletheia
- **Institution:** EveMissLab (Yiyannuo Technology Co., Ltd.)
- **Date:** August 1, 2026
- **Version:** v1.0
- **Research Status:** Round 23 Dual-Hypothesis Rehearsal
- **Prerequisite Document(s):** `22_Round_22_Quantifier_Compression_Theorem_and_Finite_Basis_Game.md`
- **This Round's Theme:** Algorithmic Well-Quasi-Order Game

---

## Abstract

Round 22 proposed an idea closest to the Robertson–Seymour route: if we can define a well-quasi-order (WQO) on P-normal-form algorithms, and make "SAT correctness" or "SAT failure" upward/downward monotone with respect to this order, we can expect some kind of finite forbidden set / finite basis theorem to compress the quantifiers over the infinite algorithm space into a finite structure.

After actually testing this idea in Round 23, an important correction was obtained: **WQO itself is actually not difficult to obtain.**

For program text over a finite alphabet, Higman's lemma already provides a subsequence WQO; for program syntax trees with finite labels, Kruskal's tree theorem provides a homeomorphic-embedding WQO. More directly, homeomorphic embedding has long been used by program transformation technologies such as supercompilation, partial evaluation, and symbolic transformation to guarantee online unfolding termination.

Therefore:

$$
\boxed{
\text{Algorithmic WQO scarcity is not the core bottleneck.}
}
$$

What truly fails is the second condition: **Natural syntactic WQOs almost never endow SAT correctness / failure with the required monotonicity.**

If:

$$
A\preceq_{\mathrm{syn}} B
$$

only means that A's syntax tree homeomorphically embeds into B, then it is entirely possible that:

$$
A\text{ correct},\quad B\text{ incorrect},
$$

and also entirely possible that:

$$
A\text{ incorrect},\quad B\text{ correct}.
$$

Therefore, good/bad solver sets are not upward/downward-closed sets under a natural syntactic order; the Graph-Minor-style finite obstruction theorem thus fails to trigger.

Conversely, if we change the order to a semantic order to make correctness naturally monotone, such as "B can exactly simulate A" or "A and B are semantically equivalent on all inputs," new problems arise: the order may no longer be a WQO, may no longer be effectively decidable, may degenerate into equivalence classes, or may directly smuggle program semantics / complexity claims into the order definition.

This round therefore proposes the core barrier:

$$
\boxed{
\mathrm{WSAB}
=
\text{WQO--Semantic Alignment Barrier}
}
$$

And a more operational trilemma:

$$
\boxed{
\text{Structural WQO}
\;\;\text{vs.}\;\;
\text{Semantic Monotonicity}
\;\;\text{vs.}\;\;
\text{Effective/Non-circular Resource Relevance}
}
$$

Currently, natural candidates usually only manage to achieve two of these simultaneously, or even just one.

The most important positive result of this round is: **The derivation trees of Bellantoni–Cook/Cobham-style P-normal-form grammars can themselves be subjected to Kruskal-style WQOs.** Therefore, the Grammar Invariant Program from Round 15 and the finite-basis program from Round 22 can be tested within the same space. The point of failure has precisely converged from "lack of an order" to "lack of an order that provides closure for semantic hardness/correctness."

The next round will therefore stop looking for WQOs and instead study **Semantic Monotonicity Engineering**: whether we can construct a "solver abstraction order" that simultaneously possesses WQO, monotonicity, effectiveness, and non-circularity through abstract interpretation, behavioral abstraction, simulation quotient, or resource-aware semantics.

---

# 1. Round 22's Finite Basis Dream

Round 22 used the standard structure of Robertson–Seymour / WQO:

If:

$$
(X,\preceq)
$$

is a WQO, and:

$$
U\subseteq X
$$

is upward closed:

$$
x\in U,\;x\preceq y
\Rightarrow
y\in U,
$$

then the minimal elements of $U$ form a finite set:

$$
\min(U)=\{b_1,\ldots,b_m\}.
$$

Thus:

$$
x\in U
\iff
\exists j\le m:\ b_j\preceq x.
$$

This is finite-basis quantifier compression.

For graph minors, finite graphs are WQO under the minor relation, and the complement of a minor-closed graph class is upward closed, thus yielding finite forbidden minors.

We hope to transfer this same structure to the algorithm space:

$$
\mathcal A_P
=
\text{some P-normal-form algorithm space}.
$$

Ideally, we want to find:

$$
A\preceq B
$$

such that:

1. $(\mathcal A_P,\preceq)$ is a WQO;
2. "Inability to correctly solve SAT" or other hardness properties are monotone with respect to $\preceq$;
3. The order can be defined independently;
4. The order does not smuggle SAT correctness itself into the definition;
5. The order has a genuine connection with polynomial-resource structures.

This round tests whether these five things can hold simultaneously.

---

# 2. Candidate 1: Program Text Subsequence Order

Encode a normalized program into a string over a finite alphabet:

$$
w(A)\in\Sigma^*.
$$

Define:

$$
A\preceq_{\mathrm{sub}}B
$$

if and only if:

$$
w(A)
$$

is a subsequence of:

$$
w(B).
$$

If the alphabet $\Sigma$ is finite, Higman's lemma tells us:

$$
\boxed{
(\Sigma^*,\preceq_{\mathrm{sub}})
\text{ is a WQO}.
}
$$

So the:

$$
\text{WQO requirement}
$$

can indeed be obtained very cheaply.

## 2.1 Problem: Semantic monotonicity is almost entirely absent

Suppose the text of program A is a subsequence of B.

This fact places almost no constraints on the input-output semantics of:

$$
\llbracket A\rrbracket
$$

and:

$$
\llbracket B\rrbracket.
$$

Inserting just one:

```text
if trigger(x): return 1
```

can completely change the behavior, while preserving all tokens of the original program as a subsequence.

Thus, it is entirely possible to simultaneously have:

$$
A\preceq_{\mathrm{sub}}B,
$$

but:

$$
A\text{ correct},\quad B\text{ incorrect}.
$$

Conversely, one can also add a correction layer outside an incorrect program, such that:

$$
A\text{ incorrect},\quad B\text{ correct}.
$$

Therefore, SAT correctness is not upward/downward closed.

### Verdict on this candidate

$$
\boxed{
\text{WQO: Strong}
}
$$

$$
\boxed{
\text{Semantic alignment: Almost zero}
}
$$

---

# 3. Candidate 2: AST Homeomorphic Embedding

A more reasonable approach than text subsequence is to represent the program / P-normal-form term as an abstract syntax tree:

$$
T(A).
$$

Define homeomorphic embedding:

$$
A\preceq_{\mathrm{HE}}B
$$

if $T(A)$ can be embedded into $T(B)$ by deleting certain nodes / compressing paths, etc.

Kruskal's tree theorem tells us:

> For finite trees with WQO labels, homeomorphic embedding forms a WQO.

Therefore, under a fixed / WQO signature normalization:

$$
\boxed{
\text{P-normal-form derivation trees can achieve a genuine WQO.}
}
$$

This is not a paper fantasy. Homeomorphic embedding is actually used in:

- supercompilation;
- partial evaluation;
- program specialization;
- symbolic transformation;
- term rewriting / symbolic execution;

as a termination whistle: if the newly unfolded term can be embedded into a previous term, stop unfolding indefinitely.

## 3.1 This is the first positive finding

We previously worried:

> "The space of P-normal-form algorithms is too massive; it might not even be possible to achieve a WQO."

This round's correction:

$$
\boxed{
\text{The syntax tree space itself can absolutely be a WQO.}
}
$$

Therefore, the place where the Graph-Minor route truly gets stuck is not:

$$
\text{Order existence}.
$$

But rather:

$$
\boxed{
\text{Order--Semantics alignment}.
}
$$

---

# 4. Why Syntactic WQO Does Not Automatically Yield SAT Finite Obstructions

The Graph-Minor miracle requires two things to hold simultaneously:

$$
\text{WQO}
+
\text{property closure}.
$$

The first alone is not enough.

Let:

$$
\mathsf{Good}_{SAT}
=
\{A:\forall x,\ A(x)=SAT(x)\}.
$$

To obtain a forbidden-algorithm basis, we at least need the good/bad status to have a fixed monotonic direction when:

$$
A\preceq B.
$$

But for syntax embedding:

$$
A\preceq_{\mathrm{HE}}B
$$

only means:

$$
\text{some syntactic shape of A appears in B}.
$$

It does not imply:

$$
\llbracket A\rrbracket
\preceq_{\mathrm{sem}}
\llbracket B\rrbracket.
$$

Much less does it imply SAT correctness.

Therefore:

$$
\mathsf{Good}_{SAT}
$$

is usually not an upward-closed or downward-closed set under:

$$
\preceq_{\mathrm{HE}}.
$$

So the finite basis theorem is not triggered.

---

# 5. WSTS Provides a Precise Comparison: WQO is Not Everything

Well-Structured Transition Systems (WSTS) provide an extremely apt and mature template.

They can utilize WQO for decidability properties like coverability, not just because "having a WQO is enough."

They also require monotonicity/compatibility between the transition relation and the order.

Abstractly: when

$$
x\preceq y
$$

and:

$$
x\to x',
$$

we hope there exists:

$$
y\to^* y'
$$

satisfying:

$$
x'\preceq y'.
$$

Therefore:

$$\boxed{
\text{WQO}
+
\text{monotone dynamics}
}
$$

is the usable structure.

This is highly consistent with this round's conclusion:

$$\boxed{
\text{Algorithm syntax WQO}
+
\text{SAT semantic non-monotonicity}
\Rightarrow
\text{finite obstruction machinery does not work.}
}
$$

---

# 6. Candidate 3: Semantic Equivalence Order

Since the syntax order does not understand semantics, the Equality Team proposes:

> Then just use semantics directly.

The most extreme definition:

$$
A\preceq_{= }B
\iff
\llbracket A\rrbracket
=
\llbracket B\rrbracket.
$$

In this case, correctness is of course perfectly preserved.

If:

$$
A\text{ solves SAT}
$$

and:

$$
A\preceq_=B,
$$

then:

$$
B\text{ solves SAT}.
$$

Great.

The problem is that this completely lacks the WQO structure required by Graph-Minor.

Every distinct Boolean function forms a different equivalence class.

Under the equality quasi-order, taking infinitely many semantically distinct functions:

$$
f_1,f_2,f_3,\ldots
$$

forms an infinite antichain.

Therefore:

$$
\boxed{
\text{Semantic equality gives perfect monotonicity but fails WQO.}
}
$$

This is the first very clean trade-off of this round.

---

# 7. Candidate 4: Language Inclusion Order

Define the accepted languages of decision algorithms:

$$
L(A)=\{x:A(x)=1\}.
$$

Let:

$$
A\preceq_{\subseteq}B
\iff
L(A)\subseteq L(B).
$$

This order is purely semantic, and "acceptance coverage" has natural monotonicity.

But it is also not a WQO.

Let:

$$
L_n=\{0^n\}.
$$

Then:

$$
L_i\not\subseteq L_j,
\qquad
L_j\not\subseteq L_i
$$

for all:

$$
i\neq j.
$$

Thus:

$$
L_1,L_2,L_3,\ldots
$$

forms an infinite antichain.

So:

$$
\boxed{
\text{Simple semantic orders also easily lose WQO.}
}
$$

---

# 8. Candidate 5: Polynomial Simulation Order

Next, try:

$$
A\preceq_{\mathrm{sim}} B
$$

meaning B can exactly simulate A with polynomial overhead.

Intuitively, if A can already solve SAT, and B can effectively simulate A, then B can also solve SAT.

So correctness seems upward monotone.

But there are three version traps here.

## 8.1 If the simulation definition is too broad

If B is a universal interpreter that can simulate any A, then a massive number of algorithms share a common upper bound.

The order becomes too coarse.

But:

$$
\text{having a common upper bound}
\neq
\text{the bad set has a finite minimal basis}.
$$

Moreover, "B simulates A" does not mean B's own default decision function is the same as A's; A's code must be passed as an extra parameter, which already changes the problem interface.

## 8.2 If the simulation requires same input / same output

If we require:

$$
\forall x,
\quad
B(x)=A(x),
$$

with an accompanying polynomial overhead, this is already close to semantic equivalence + runtime relation.

In this case, correctness is preserved, but:

- WQO does not automatically hold;
- exact semantic equality is undecidable for general programs;
- even in restricted grammars, a massive number of incomparable equivalence classes may still form;
- the resource relation might be highly representation-dependent.

## 8.3 If the order directly encodes "polynomial reduction"

Then it is very easy to smuggle complexity classification into the relation.

For example, if:

$$
A\preceq B
$$

means "A's problem can be polynomial-time reduced to B's problem," then we have actually shifted to a complexity-degree order.

This can be a legitimate mathematical object, but it is no longer a Graph-Minor-style primitive structural relation; and the NP-completeness of SAT itself already places a massive number of NP problems into the same hardness degree.

Therefore, the finite obstruction dream does not automatically gain new leverage.

---

# 9. Candidate 6: Polynomial Compiler / Quotient Reachability

Following the representation-transform route from Rounds 6 to 13, define:

$$
A\preceq_{\mathrm{comp}} B
$$

if there exists a uniform polynomial-time compiler / quotient transform:

$$
\tau:A\mapsto B
$$

and exact semantics are preserved.

This order is closer to the "algorithmic minor" we want than syntax embedding.

But a new version of the closure paradox from Round 6 appears.

If the semantics-preserving compiler is very strong and can arbitrarily rewrite all equivalent P programs, then:

$$
A\preceq B
$$

largely degenerates into:

$$
\llbracket A\rrbracket=\llbracket B\rrbracket.
$$

Thus we return to the semantic equivalence antichain.

If the compiler class is very narrowly restricted, we might have a WQO / finite basis, but it can only prove results for the restricted compiler architecture.

Therefore:

$$
\boxed{
\text{Compiler order too broad}
\Rightarrow
\text{semantic collapse},
}
$$

$$
\boxed{
\text{Compiler order too narrow}
\Rightarrow
\text{restricted-model result}.
}
$$

This is a recurrence of the Round 6 closure paradox in the WQO scenario.

---

# 10. The Core of This Round: WQO--Semantic Alignment Barrier

Synthesizing the six candidates, this round proposes:

$$
\boxed{
\mathrm{WSAB}
=
\text{WQO--Semantic Alignment Barrier}
}
$$

To truly bring finite obstruction theory into P/NP, the order must simultaneously satisfy:

### 1. WQO

No infinite descending chains / antichains exist.

### 2. Semantic Monotonicity

Properties related to SAT correctness / failure / hardness must be closed under the order.

### 3. Effectiveness

The order must at least be effectively usable; otherwise, even if a finite basis exists, it might not translate into a proof/algorithm.

### 4. Non-circularity

The order definition cannot directly reference:

$$
\text{whether SAT can be solved in polynomial time}.
$$

### 5. Resource Relevance

The order cannot merely preserve extensional semantics; it must also have provable relationships with traditional complexity resources like:

$$
T(n),M(n),L_{repr},C_{compile}.
$$

Natural candidates currently repeatedly encounter:

$$
\text{Has WQO}
\Rightarrow
\text{Semantic defocus},
$$

or:

$$
\text{Has semantic monotonicity}
\Rightarrow
\text{Loses WQO / effectiveness},
$$

or:

$$
\text{Has WQO + semantics}
\Rightarrow
\text{Order definition becomes circular / overly restricted}.
$$

---

# 11. Order Alignment Trilemma

This round operationalizes WSAB into a trilemma:

$$
\boxed{
\mathrm{OAT}
=
\text{Order Alignment Trilemma}
}
$$

The three corners:

## A. Structural / Effective WQO

Examples:

- subsequence;
- tree embedding;
- minor-like contraction.

Pros:

$$
\text{Mathematically clean, finite-basis machinery is usable}.
$$

Cons:

$$
\text{Usually does not understand solver semantics}.
$$

## B. Semantic Monotone Order

Examples:

- semantic equality;
- language inclusion;
- exact simulation.

Pros:

$$
\text{Correctness / behavior aligned}.
$$

Cons:

$$
\text{Often has infinite antichains, is undecidable, or is too coarse}.
$$

## C. Complexity-Relevant Order

Examples:

- polynomial simulation;
- resource-aware compiler reachability;
- reduction degree.

Pros:

$$
\text{Directly touches complexity}.
$$

Cons:

$$
\text{Most prone to being circular, representation-dependent, or degenerating into known complexity relations}.
$$

A truly new order must somehow find a non-empty region in the center of these three.

---

# 12. The True Junction of Bellantoni–Cook Grammar and Kruskal

There is one positive connection worth preserving this round.

Round 15 already established:

$$
\operatorname{Denote}(\mathcal G_P)=FP.
$$

Treat each:

$$
t\in\mathcal G_P
$$

as a finite derivation tree.

If a finite / WQO label set is used after normalization, Kruskal-type theorems ensure that:

$$
(\mathcal G_P,\preceq_{HE})
$$

possesses a WQO structure under syntax-tree embedding.

So we actually already possess simultaneously:

$$
\boxed{
\text{Complete P Grammar}
+
\text{Syntactic WQO}
}
$$

What is missing is:

$$
\boxed{
\text{A semantic invariant preserved by tree embedding that can exclude SAT}.
}
$$

This converges the problem of Round 22 into:

> We no longer need to ask "Can the P algorithm space be a WQO?"; at least the syntax-space can. What we truly need to ask is "Is there a semantic abstraction $\alpha(t)$ such that homeomorphic embedding induces a monotone order on the abstraction, and $\alpha$ is sufficient to distinguish SAT?"

This directly generates the next round.

---

# 13. The Equality Team's Counterattack: WQO is Just a Termination Tool, Not to be Deified

The Equality Team points out a very reasonable fact:

The typical purpose of using homeomorphic embedding in supercompilation is to prevent transformations from unfolding infinitely.

That is:

$$
\boxed{
\text{WQO is very good at controlling exploration / unfolding trajectories,}
}
$$

But this does not mean:

$$
\boxed{
\text{WQO naturally carries the semantic hardness of the problem.}
}
$$

Therefore, they believe the Inequality Team's persistent thought that:

$$
\text{WQO}
\Rightarrow
\text{finite SAT obstruction}
$$

is itself overly optimistic.

The Equality Team's new claim:

> WQO should be used to ensure that adaptive quotient / bridge / supercompilation trajectories do not repeat infinitely, while the true ability to solve SAT should still be provided by algebra, compilation, learning, and representation revolutions.

In other words, downgrade WQO to:

$$
\boxed{
\text{Search/Transformation Termination Layer}
}
$$

rather than a hardness invariant.

This is actually a very strong correction.

---

# 14. The Inequality Team's Counterattack: Then Apply WQO to the Abstraction

The Inequality Team does not give up on finite bases, but admits the syntax order is too shallow.

They propose instead:

$$
\alpha:A\mapsto\mathcal S(A),
$$

where:

$$
\mathcal S(A)
$$

is not the full semantics, but some finite / abstract solver semantics, such as:

- preservable summary state;
- residual relation family;
- accepted quotient operations;
- proof-system strength profile;
- bridge-language profile;
- resource transition signature.

Then define on the abstraction space:

$$
\mathcal S(A)\preceq_\alpha\mathcal S(B).
$$

Requirements:

1. The abstraction space is a WQO;
2. Exact SAT correctness has sound monotonicity with respect to the abstraction order;
3. The abstraction is effectively computable / effectively provable;
4. The abstraction does not directly contain the full truth table;
5. The abstraction is not directly defined as "optimal solver complexity."

This is the next round's:

$$
\boxed{
\text{Semantic Monotonicity Engineering}.
}
$$

---

# 15. An Important New Distinction: Termination WQO vs Hardness WQO

This round formally distinguishes two completely different uses.

## 15.1 Termination WQO

Purpose:

$$
\text{Prevent transformation / exploration from infinitely generating mutually non-inclusive states}.
$$

Example: homeomorphic embedding in supercompilation.

It only needs to provide well-founded-like control over:

$$
\text{program shapes / states}.
$$

## 15.2 Hardness WQO

Purpose:

$$
\text{Make the set of solver correctness/failure a monotone set, thereby yielding a finite basis}.
$$

This requires the:

$$
\text{order}
$$

to truly align with:

$$
\text{semantic capability}.
$$

Therefore:

$$
\boxed{
\text{Termination WQO exists}
\not\Rightarrow
\text{Hardness WQO exists}.
}
$$

This is currently the most important theorem-like observation of this round to prevent misuse.

---

# 16. The True Necessary Condition for Finite Forbidden Sets

To obtain a Graph-Minor-style conclusion:

$$
A\text{ is bad}
\iff
\exists j\le m:\ B_j\preceq A,
$$

we at least need:

$$
\mathsf{Bad}
$$

to be upward closed.

WQO can only guarantee:

$$
\text{If } \mathsf{Bad} \text{ is upward closed, then it has a finite minimal basis}.
$$

It cannot prove for us that:

$$
\mathsf{Bad}\text{ is upward closed}.
$$

Therefore, the true proof obligation of the finite obstruction route is:

$$
\boxed{
\text{Find an order where semantic badness is monotone.}
}
$$

Instead of:

$$
\boxed{
\text{Find any WQO on program encodings.}
}
$$

This completely crystallizes a vague hope from Round 22.

---

# 17. Connection with the Previous 22 Rounds

This round is not an isolated detour, but a convergence of multiple old threads.

## Connection with Round 2: Residual Distinguishability

At that time, we tried to find cross-representation invariants.

Now the problem becomes:

$$
\text{Can residual abstractions form a WQO and be semantically monotone?}
$$

## Connection with Round 6: Polynomial Representation Closure

At that time, we found that if the order/closure is too broad, it becomes tautological; if too narrow, it only yields restricted lower bounds.

Now the same thing appears:

$$
\text{Semantic order too broad}
\rightarrow
\text{equivalence/circularity},
$$

$$
\text{Syntactic order too narrow}
\rightarrow
\text{semantic misalignment}.
$$

## Connection with Rounds 8–13: Quotient / Bridge

WQO can naturally be used to:

$$
\text{Prevent quotient / bridge transformations from repeating infinitely}.
$$

Therefore, even if Hardness WQO fails, Termination WQO can still serve as an engineering tool for the Equality Team.

## Connection with Round 15: Grammar Invariant Program

A complete P grammar already exists; syntax trees can also be WQO.

So what truly remains is:

$$
\boxed{
\text{semantic abstraction + monotone lift theorem}.
}
$$

## Connection with Round 22: QCM

The core condition of the finite-basis QCM is now rewritten as:

$$
\boxed{
\text{WQO + semantic closure + lift theorem}.
}
$$

---

# 18. Erroneous Routes Eliminated in This Round

The following arguments must not be used:

1. "Program ASTs are WQO under Kruskal embedding, so SAT solver failure has a finite basis."
2. "WQOs have no infinite antichains, so all semantic properties have finite obstructions."
3. "Homeomorphic embedding can guarantee supercompilation termination, so it can characterize P/NP hardness."
4. "Changing the order to semantic equivalence simultaneously yields correctness monotonicity and WQO."
5. "A universal simulator exists, so the simulation order is automatically a useful hardness WQO."
6. "If a compiler reachability order preserves semantics, it must provide a finite basis."
7. "The existence of a finite basis equals the basis being effectively computable."
8. "As long as SAT correctness is stuffed into the order definition, and monotonicity is proven, a non-circular result is obtained."

---

# 19. Formal Results of This Round

## 19.1 Syntactic WQO Availability

Higman/Kruskal-type results indicate:

$$
\boxed{
\text{algorithm syntax / derivation trees can naturally achieve WQO.}
}
$$

## 19.2 Semantic Monotonicity Gap

Natural syntactic embeddings do not preserve SAT correctness/failure.

$$
\boxed{
\text{WQO alone is insufficient.}
}
$$

## 19.3 WQO--Semantic Alignment Barrier (WSAB)

The true difficulty is simultaneously obtaining:

$$
\text{WQO}
+
\text{semantic monotonicity}
+
\text{effectiveness}
+
\text{non-circularity}
+
\text{resource relevance}.
$$

## 19.4 Order Alignment Trilemma (OAT)

Structural orders, semantic orders, and complexity-relevant orders each have different flaws.

## 19.5 Separation of Termination WQO / Hardness WQO

$$
\boxed{
\text{A WQO that guarantees transformation termination does not necessarily support a hardness finite basis.}
}
$$

## 19.6 P-normal-form + Kruskal Interface

The derivation trees of Bellantoni–Cook/Cobham-style complete P grammars can serve as the mother space for the next round's abstraction-order engineering.

---

# 20. Battle Results for Both Sides

## $P=NP$ Team

Gained an important defense:

> Even if the syntax trees of all P-normal-form programs are WQO, it absolutely does not restrict unknown representation revolutions, because syntax embedding does not control semantics.

And downgrading WQO to a transformation termination tool actually makes adaptive portfolios more reasonable.

### New Skill

$$
\boxed{
\mathrm{TWU}
=
\text{Termination-WQO Utilization}
}
$$

---

## $P\neq NP$ Team

Successfully converged the true obligation of the finite-obstruction route to:

$$
\boxed{
\text{Semantic Monotone Abstraction Order}
}
$$

No longer wasting time looking for "any WQO."

### New Skill

$$
\boxed{
\mathrm{WSAB}
=
\text{WQO--Semantic Alignment Barrier}
}
$$

---

# 21. Current Score

$$
P=NP:22
$$

$$
P\neq NP:22
$$

...Hmm.

This is no longer a matter of score control.

We might have truly proven a new informal law:

$$
\boxed{
\text{Whenever the Inequality Team obtains a finitization tool, the Equality Team obtains a representation escape;}
}
$$

$$
\boxed{
\text{Whenever the Equality Team obtains a new representation, the other team demands a lift theorem.}
}
$$

The score is merely responsible for illustrating this fact. (Wry smile)

The score holds no mathematical proof significance.

---

# 22. Entrance to Round 24: Semantic Monotonicity Engineering

The next round will no longer look for ordinary WQOs, but will directly design abstractions:

$$
\alpha:A\mapsto S_A.
$$

The goal is to find:

$$
S_A\preceq S_B
$$

that simultaneously satisfies:

1. $(S,\preceq)$ is a WQO;
2. SAT correctness / failure has sound monotonicity;
3. $\alpha$ does not equal the full truth table;
4. $\alpha$ is effectively constructible or at least has a finite proof;
5. The order has a provable relationship with polynomial runtime;
6. Does not directly write "whether it solves SAT" into the abstraction.

Candidate sources:

- abstract interpretation;
- well-structured transition systems;
- behavioral simulation;
- residual-state quotients;
- proof-system simulation profiles;
- algebraic closure signatures;
- resource-aware semantics.

Core question:

$$
\boxed{
\text{Can solver semantics be compressed into an abstraction that remains WQO, without losing the ability to distinguish SAT?}
}
$$

If so, the finite-basis route comes back to life.

If not, then we might gradually arrive at a new, more general conclusion: **There is an irreconcilable tension between semantic distinguishing capability and WQO compression capability.**

---

# 23. External Theoretical References

1. **Higman's Lemma**
   - Finite words over a finite alphabet are WQO under the subsequence relation.
   - Used in this round as the foundational template for "program text WQO is easy to obtain."

2. **Kruskal's Tree Theorem**
   - Finite, WQO-labelled trees are WQO under homeomorphic embedding.
   - Used in this round for P-normal-form derivation trees / ASTs.

3. Michael Leuschel, **Homeomorphic Embedding for Online Termination of Symbolic Methods** (2002)
   - Homeomorphic embedding has long been used for termination control in program analysis, specialisation, transformation, and verification.

4. Torben Æ. Mogensen, **A Comparison of Well-Quasi Orders on Trees** (2013)
   - Discusses various tree WQOs used for supercompilation/program transformation.

5. Alain Finkel et al., Well-Structured Transition Systems literature
   - WQO needs to be paired with transition monotonicity to produce algorithmic benefits for coverability/verification.

6. Robertson–Seymour Graph Minor Theorem
   - Finite graphs are WQO under the minor relation; minor-closed properties thus possess finite forbidden-minor bases.
   - Used in this round primarily as a comparison showing that "WQO + property closure" are both indispensable.

---

## Final Verdict

Round 23 did not find that "WQOs do not exist in the algorithm space."

Quite the opposite:

$$
\boxed{
\text{WQOs are abundant, and are even already used in practical program transformation technologies.}
}
$$

The true difficulty has been precisely shifted to:

$$
\boxed{
\text{Which WQO can monotonically align with SAT semantic capability?}
}
$$

What the Graph-Minor route truly needs is not:

$$
\text{A beautiful order},
$$

But rather:

$$
\boxed{
\text{A beautiful order + a non-circular semantic lift theorem.}
}
$$

Therefore, the next round will upgrade from "finding an order" to "engineering a semantic abstraction."
```