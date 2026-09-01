# NTLA-O II: Set-Theoretic Observer Hierarchy
## Power Sets, Admissible Distinction Families, Ordinal Rank, Set-Boundedness, and Class-Level Observer Towers

**English Title:** *NTLA-O II: Set-Theoretic Observer Hierarchy — Power Sets, Admissible Distinction Families, Ordinal Rank, Set-Boundedness, and Class-Level Observer Towers*  
**Series:** NTLA-O Series, Paper 3  
**Version:** v0.1 Formal Draft  
**Prerequisite Paper:** *NTLA-O I: Main-Internal-External Observers, Admissibility, Domain of Evaluation, and Observation Difference Kernels*  
**Author:** Neo.K  
**Theoretical Organization and Formalization Collaboration:** Aletheia / GPT-5.6 Sol  
**Date:** 2026-08-17

---

## Abstract

This paper establishes the set-theoretic foundations of NTLA-O.

The previous paper represented an observer as:

$$
\mathcal O
=
\left(
S_{\mathcal O},
D_{\mathcal O},
\mathcal L_{\mathcal O},
\mathcal J_{\mathcal O},
R_{\mathcal O}
\right),
$$

and utilized the effective observation mapping:

$$
E_{\mathcal O}
$$

to define the observational indistinguishability kernel:

$$
K_{\mathcal O}
=
\left\{
(x,y):
E_{\mathcal O}(x)=E_{\mathcal O}(y)
\right\}.
$$

This paper further asks:

> If we temporarily remove topologies, groupoids, sheaves, and other additional structures, what does an observer fundamentally require in a minimal set-theoretic sense?

This paper proposes: for a set domain $D$, the minimal distinction content of an observer can be represented as a family of subsets:

$$
\boxed{
\mathcal A_{\mathcal O}
\subseteq
\mathcal P(D).
}
$$

Each:

$$
A\in\mathcal A_{\mathcal O}
$$

corresponds to a binary distinction predicate, and two elements are indistinguishable to the observer if and only if they yield the same membership signature under all admissible distinction sets.

Thus, the observational structure of NTLA-O can first be established in pure set theory, and then topological closure, Boolean closure, measurable closure, or logical definability can be added as needed.

This paper further distinguishes four levels:

$$
\boxed{
\text{Existing Subsets}
\supseteq
\text{Queryable Subsets}
\supseteq
\text{Admissible Query Subsets}
\supseteq
\text{Effective Distinction Subsets}.
}
$$

Regarding nesting, this paper proves that any set-indexed family of sets has a set-sized union upper bound. Therefore:

$$
\boxed{
\text{No Finite Maximum Element}
}
$$

and:

$$
\boxed{
\text{No Set Upper Bound}
}
$$

are two completely different propositions.

This paper then utilizes the standard set-theoretic rank to establish a key result:

> The ranks of any set-sized observer family are necessarily uniformly bounded by some ordinal.

Therefore, if an observer totality satisfies:

$$
\forall\alpha\in\operatorname{Ord},
\exists\mathcal O
:
\operatorname{rank}(\mathcal O)>\alpha,
$$

then this totality cannot be a set; if one wishes to operate on it as a single mathematical totality, one must transition to a proper-class language.

Finally, this paper uses the cumulative hierarchy:

$$
V_0,
V_1,
\ldots,
V_\alpha,
\ldots
$$

to establish a set-theoretic prototype for the main-internal-external roles of NTLA-O, and strictly distinguishes between:

$$
\boxed{
\text{set-theoretic height},
\quad
\text{observer role},
\quad
\text{observational resolution}.
}
$$

These three cannot be automatically deduced from one another.

**Keywords:** NTLA-O, set theory, power set, observer, equivalence relation, quotient set, ordinal, rank, cumulative hierarchy, proper class, NBG, Grothendieck universe

---

# 1. Set Theory as Level 0 of NTLA-O

The structure of NTLA 2.0 is written as:

$$
\mathcal T
=
(X,\tau,\mathcal H,\mathcal C,\Lambda).
$$

But the topology therein:

$$
\tau
$$

is itself merely:

$$
\boxed{
\tau\subseteq\mathcal P(X)
}
$$

and additionally satisfies specified closure axioms.

Therefore, before introducing a topology, one can first examine a weaker structure:

$$
\boxed{
\mathcal A
\subseteq
\mathcal P(X).
}
$$

This paper considers this level as NTLA-O's:

# **Level-0 Observer Structure**

It only answers:

> Which subsets are treated as predicates capable of distinguishing elements in $X$?

without first requiring these predicates to form a topology.

---

# 2. Minimal Set-Theoretic Observer

## Definition 2.1

Given a set:

$$
D.
$$

A minimal set-theoretic observer is defined as:

$$
\boxed{
\mathcal O_{\mathrm{set}}
=
(D,\mathcal A_{\mathcal O}),
}
$$

where:

$$
\boxed{
\mathcal A_{\mathcal O}
\subseteq
\mathcal P(D).
}
$$

We call:

$$
\mathcal A_{\mathcal O}
$$

the:

# **Admissible Distinction Family**

Also referred to as:

# **Effective Distinction Family**

---

# 3. Subsets as Minimal Binary Evaluators

For:

$$
A\subseteq D,
$$

define the characteristic function:

$$
\chi_A:
D
\rightarrow
\{0,1\}
$$

as:

$$
\chi_A(x)
=
\begin{cases}
1,&x\in A,\\
0,&x\notin A.
\end{cases}
$$

Thus:

$$
A
$$

itself can answer a minimal yes/no question:

$$
\boxed{
x\in A?
}
$$

Therefore:

$$
\mathcal A_{\mathcal O}
$$

can be equivalently understood as a family of binary observables:

$$
\boxed{
\{
\chi_A
\}_{A\in\mathcal A_{\mathcal O}}.
}
$$

This makes the "observer" primarily a mathematical distinction structure, rather than a psychological concept.

---

# 4. Membership Signature

For:

$$
x\in D,
$$

define its membership signature relative to the observer $\mathcal O$:

$$
\boxed{
\sigma_{\mathcal O}(x)
:
\mathcal A_{\mathcal O}
\rightarrow
\{0,1\}
}
$$

where:

$$
\sigma_{\mathcal O}(x)(A)
=
\chi_A(x).
$$

Thus:

$$
\sigma_{\mathcal O}(x)
$$

completely records:

> On which side $x$ falls for all admissible distinction sets recognized by this observer.

---

# 5. Set-Theoretic Observational Equivalence

## Definition 5.1

Define:

$$
\boxed{
x\sim_{\mathcal O}y
}
$$

if and only if:

$$
\boxed{
\sigma_{\mathcal O}(x)
=
\sigma_{\mathcal O}(y).
}
$$

Expanding this yields:

$$
\boxed{
\forall A\in\mathcal A_{\mathcal O},
\quad
x\in A
\leftrightarrow
y\in A.
}
$$

Therefore:

$$
K_{\mathcal O}
=
\left\{
(x,y)\in D^2:
x\sim_{\mathcal O}y
\right\}.
$$

---

# Theorem 1: Set-Theoretic Observer Kernel Theorem

$$
K_{\mathcal O}
$$

is an equivalence relation on $D$.

### Proof

Reflexivity follows from:

$$
\sigma_{\mathcal O}(x)
=
\sigma_{\mathcal O}(x).
$$

Symmetry follows from the symmetry of equality of function values.

Transitivity follows from:

$$
\sigma_{\mathcal O}(x)
=
\sigma_{\mathcal O}(y)
$$

and:

$$
\sigma_{\mathcal O}(y)
=
\sigma_{\mathcal O}(z)
$$

implying:

$$
\sigma_{\mathcal O}(x)
=
\sigma_{\mathcal O}(z).
$$

Thus:

$$
K_{\mathcal O}
$$

is an equivalence relation.

Q.E.D.

---

# 6. Observational Quotient

Therefore, there exists a quotient set:

$$
\boxed{
D/{\sim_{\mathcal O}}.
}
$$

Let:

$$
q_{\mathcal O}:
D
\rightarrow
D/{\sim_{\mathcal O}}
$$

be the natural quotient map.

Each quotient class:

$$
[x]_{\mathcal O}
$$

contains all elements that are indistinguishable to $\mathcal O$.

Thus, a minimal set-theoretic observer is sufficient to generate:

$$
\boxed{
\text{Domain}
\rightarrow
\text{Equivalence Relation}
\rightarrow
\text{Quotient}.
}
$$

No topology is required yet.

---

# 7. Four-Level Admissibility Structure

Merely using:

$$
\mathcal A_{\mathcal O}
$$

is still insufficient to distinguish:

> Are unused sets absent because they do not exist, cannot be queried, are inadmissible, or are simply ignored by the evaluation domain?

Therefore, we define:

$$
\boxed{
\mathcal A_{\mathcal O}
\subseteq
\mathcal L_{\mathcal O}
\subseteq
\mathcal Q_{\mathcal O}
\subseteq
\mathcal P(D).
}
$$

where:

$$
\mathcal P(D)
$$

is the set of all subsets.

$$
\mathcal Q_{\mathcal O}
$$

are the queries allowed to be formed in the observer formalism.

$$
\mathcal L_{\mathcal O}
$$

are the admissible queries under the current regime/type/interface.

$$
\mathcal A_{\mathcal O}
$$

are the predicates that actually enter into effective distinction.

Thus:

$$
A\notin\mathcal L_{\mathcal O}
$$

cannot be interpreted as:

$$
A=\varnothing.
$$

nor can it be interpreted as:

$$
\chi_A(x)=0.
$$

but merely indicates:

$$
\boxed{
A
\text{ is not legally usable under the current observation specifications.}
}
$$

---

# 8. Undefined Must Not Be Automatically Replaced by False

If:

$$
A
$$

is not an admissible query,

then:

$$
\chi_A(x)
$$

should be treated in the observer language as:

$$
\boxed{
\text{undefined},
}
$$

rather than:

$$
0.
$$

Therefore, NTLA-O retains a tripartite division:

$$
\boxed{
\text{true},
\qquad
\text{false},
\qquad
\text{inadmissible/undefined}.
}
$$

This is the most fundamental type separation between admissibility and evaluation results.

---

# 9. Expansion of Distinction Families

Suppose:

$$
\mathcal A_1
\subseteq
\mathcal A_2.
$$

Intuitively, the second observer can propose at least as many effective distinction predicates.

---

# Theorem 2: Distinction-Family Monotonicity

If:

$$
\mathcal A_1
\subseteq
\mathcal A_2,
$$

then:

$$
\boxed{
K_2
\subseteq
K_1.
}
$$

### Proof

Take:

$$
(x,y)\in K_2.
$$

Then:

$$
\forall A\in\mathcal A_2,
\quad
x\in A
\leftrightarrow
y\in A.
$$

Since:

$$
\mathcal A_1\subseteq\mathcal A_2,
$$

the above condition also holds for all:

$$
A\in\mathcal A_1.
$$

Thus:

$$
(x,y)\in K_1.
$$

Therefore:

$$
K_2\subseteq K_1.
$$

Q.E.D.

---

# 10. Strict Observational Gain

If:

$$
\mathcal A_1
\subseteq
\mathcal A_2
$$

and there exist:

$$
x,y
$$

satisfying:

$$
x\sim_{\mathcal O_1}y
$$

but:

$$
x\not\sim_{\mathcal O_2}y,
$$

then:

$$
\boxed{
K_2
\subsetneq
K_1.
}
$$

Therefore, adding new predicates brings effective observational gain only when it actually splits at least one old quotient class.

Thus:

$$
\boxed{
|\mathcal A_2|>|\mathcal A_1|
}
$$

does not itself imply:

$$
\boxed{
K_2\subsetneq K_1.
}
$$

A large number of redundant predicates may add absolutely no distinguishing power.

---

# 11. Topology as a Special Closure Regime

If:

$$
\mathcal A_{\mathcal O}
$$

satisfies:

$$
\varnothing,D
\in
\mathcal A_{\mathcal O},
$$

closure under arbitrary unions, and closure under finite intersections,

then we can set:

$$
\boxed{
\tau_{\mathcal O}
=
\mathcal A_{\mathcal O}
}
$$

to form a topology.

Therefore:

$$
\boxed{
\text{Observer Family}
+
\text{Topological Closure}
\Longrightarrow
\text{Observer Topology}.
}
$$

Thus, this paper considers:

$$
\mathcal A_{\mathcal O}
\subseteq\mathcal P(D)
$$

as a more fundamental structure than an observer-induced topology.

---

# 12. Boolean and Measurable Observations are Merely Different Closure Methods

If $\mathcal A_{\mathcal O}$ is closed under finite unions, finite intersections, and complements, it can form a Boolean-algebra type distinction system.

If it is further closed under countable unions, it can enter into a $\sigma$-algebra type observation.

Therefore, Level 0 of NTLA-O does not presuppose:

$$
\boxed{
\text{All admissible observations must be topological.}
}
$$

Topological observation is just one of the possible closure regimes.

---

# 13. Set-Theoretic Formalization of Main-Internal-External Roles

Fix a reference set domain:

$$
X.
$$

Let:

$$
S_{\mathcal O}
$$

be the observer carrier.

Define:

$$
\boxed{
\rho_X(\mathcal O)=M
\iff
S_{\mathcal O}=X.
}
$$

Define:

$$
\boxed{
\rho_X(\mathcal O)=I
\iff
S_{\mathcal O}\subsetneq X.
}
$$

If:

$$
X\subsetneq S_{\mathcal O}
$$

and there exists an admissible observation interface, then:

$$
\boxed{
\rho_X(\mathcal O)=E^\uparrow.
}
$$

If the two carriers are mutually non-inclusive:

$$
S_{\mathcal O}\not\subseteq X,
$$

$$
X\not\subseteq S_{\mathcal O},
$$

but there exists an admissible relation:

$$
\mathcal I_{\mathcal O,X}
\subseteq
S_{\mathcal O}\times X,
$$

then:

$$
\boxed{
\rho_X(\mathcal O)=E^\perp.
}
$$

---

# 14. Membership and NTLA Nesting Must Not Be Confused

NTLA-O can study:

$$
A\subseteq B
$$

or additionally specify:

$$
A\prec B.
$$

But this paper does not automatically define:

$$
A\prec B
$$

as:

$$
A\in B.
$$

Therefore, we permanently distinguish:

$$
\boxed{
\in
}
$$

and:

$$
\boxed{
\prec.
}
$$

The former is foundational set-theoretic membership.

The latter is the nesting relation in the applied theory.

This allows NTLA-O to permit arbitrary structural nesting without relying on non-well-founded set theory.

---

# 15. Infinite Descending Set Chains Can Perfectly Be Admissible Set-Theoretic Structures

For example:

$$
X_n
=
\{m\in\mathbb N:m\geq n\}.
$$

Then:

$$
X_0
\supsetneq
X_1
\supsetneq
X_2
\supsetneq
\cdots.
$$

Thus:

$$
\boxed{
\text{unbounded finite depth}
}
$$

or:

$$
\boxed{
\omega\text{-long nesting}
}
$$

does not itself require proper classes.

This is an ordinary set-sized construction.

---

# 16. Fundamental Limits of Set-Indexed Towers

Now consider an arbitrary set:

$$
I
$$

and a function:

$$
F:I\rightarrow V
$$

such that:

$$
F(i)=X_i
$$

are all sets.

By the Axiom of Replacement, we can form:

$$
\{X_i:i\in I\}
$$

into a family of sets, and then obtain its union via the Axiom of Union.

---

# Theorem 3: Set-Indexed Union Bound Theorem

If:

$$
\{X_i:i\in I\}
$$

is indexed by a set $I$, then:

$$
\boxed{
U
=
\bigcup_{i\in I}X_i
}
$$

is a set, and:

$$
\boxed{
\forall i\in I,
\quad
X_i\subseteq U.
}
$$

Therefore, all set-indexed inclusion towers have some set-sized upper bound.

Q.E.D.

---

# 17. No Maximum vs. No Upper Bound

Consider:

$$
X_0
\subsetneq
X_1
\subsetneq
X_2
\subsetneq
\cdots.
$$

Even if there does not exist:

$$
n_{\max}
$$

such that:

$$
X_{n_{\max}}
$$

is the last term,

one can still form:

$$
X_\omega
=
\bigcup_{n<\omega}X_n.
$$

Thus:

$$
\boxed{
\text{No Maximum Element}
}
$$

and:

$$
\boxed{
\text{No Set Upper Bound}
}
$$

are not the same proposition.

This distinction is especially important for the "unboundedness" in NTLA-O.

---

# 18. The First Type of Unboundedness: Internal Set-Sized Unboundedness

Define an observer tower:

$$
\mathfrak T
=
\{
\mathcal O_n
\}_{n<\omega}.
$$

If for any:

$$
n<\omega
$$

there exists a deeper level:

$$
\mathcal O_{n+1},
$$

then it can be called:

$$
\boxed{
\omega\text{-unbounded in finite depth}.
}
$$

But the entire:

$$
\mathfrak T
$$

can still be a set.

Therefore:

$$
\boxed{
\text{unbounded continuation}
\not\Rightarrow
\text{proper class}.
}
$$

---

# 19. Set-Theoretic Rank

For a set:

$$
x,
$$

define:

$$
\boxed{
\operatorname{rank}(x)
=
\sup
\{
\operatorname{rank}(y)+1:
y\in x
\}.
}
$$

The rank is an ordinal value.

The cumulative hierarchy of set theory is precisely established along ordinal stages using power set successor steps and limit-stage unions to build $V_\alpha$. This is the standard rank-hierarchy background; modern set theory literature still directly uses $V_\alpha$ as foundational notation.

If:

$$
\mathcal O
$$

is itself set-coded,

then:

$$
\operatorname{rank}(\mathcal O)
$$

is well-defined.

---

# 20. Any Observer Set Must Be Rank-Bounded

This is the most important size theorem of this paper.

---

# Theorem 4: Set-Sized Observer Rank Boundedness

Let:

$$
\mathscr O
$$

be a set, and all its elements be set-coded observers.

Then there exists an ordinal:

$$
\beta
$$

such that:

$$
\boxed{
\forall\mathcal O\in\mathscr O,
\quad
\operatorname{rank}(\mathcal O)<\beta.
}
$$

### Proof

By the Axiom of Replacement,

$$
R
=
\{
\operatorname{rank}(\mathcal O):
\mathcal O\in\mathscr O
\}
$$

is a set of ordinals.

Let:

$$
\gamma
=
\sup R.
$$

Then:

$$
\gamma
$$

is an ordinal.

Take:

$$
\beta
=
\gamma+1.
$$

Thus, for all:

$$
\mathcal O\in\mathscr O
$$

we have:

$$
\operatorname{rank}(\mathcal O)
\leq
\gamma
<
\beta.
$$

Q.E.D.

---

# 21. Rank-Unbounded Observer Totality

Now we define a truly stronger unboundedness.

## Definition 21.1

An observer totality:

$$
\mathbf O
$$

is called:

# **rank-unbounded**

if:

$$
\boxed{
\forall\alpha\in\operatorname{Ord},
\exists\mathcal O\in\mathbf O
:
\operatorname{rank}(\mathcal O)>\alpha.
}
$$

Here, the quantifier ranges over all ordinals.

---

# Theorem 5: Rank-Unbounded Totality Non-Set Theorem

If:

$$
\mathbf O
$$

is rank-unbounded with respect to:

$$
\operatorname{Ord}
$$

then:

$$
\boxed{
\mathbf O
\text{ cannot be a set.}
}
$$

### Proof

Assume for contradiction that:

$$
\mathbf O
$$

is a set.

By Theorem 4, there exists an ordinal:

$$
\beta
$$

such that:

$$
\forall\mathcal O\in\mathbf O,
\quad
\operatorname{rank}(\mathcal O)<\beta.
$$

But the rank-unbounded condition requires that for:

$$
\alpha=\beta
$$

there exists:

$$
\mathcal O^\ast\in\mathbf O
$$

satisfying:

$$
\operatorname{rank}(\mathcal O^\ast)>\beta.
$$

Contradiction.

Thus:

$$
\mathbf O
$$

cannot be a set.

Q.E.D.

---

# 22. Proper-Class Scale

The content of Theorem 5 is not:

$$
\boxed{
\text{There exists some mysterious observer transcending set theory.}
}
$$

but merely:

$$
\boxed{
\text{An observer totality whose rank is unbounded over all ordinals cannot be contained in a single set.}
}
$$

If one wishes to directly quantify or operate on such a totality in a formal language, a two-tiered sets/classes foundation is a standard choice; for example, NBG explicitly incorporates both sets and classes into its theoretical language.

Therefore, this paper refers to this scale as:

$$
\boxed{
\text{class-level observer tower}.
}
$$

---

# 23. Demystification of the "Absolutely Unbounded Observer"

To retain the shorthand from earlier discussions, we can provisionally call:

$$
\boxed{
\forall\alpha\in\operatorname{Ord},
\exists\mathcal O_\alpha:
\operatorname{rank}(\mathcal O_\alpha)>\alpha
}
$$

# **Absolutely Unbounded Observer Tower**

But its formal meaning in this paper is strictly:

$$
\boxed{
\operatorname{Ord}\text{-unbounded observer ranks}.
}
$$

It is not:

- Omniscient;
- Unique;
- Maximal;
- Transcending logic;
- An ultimate subject;
- The set of all sets.

It is a size/rank property.

---

# 24. No "Highest Ordinal Observer"

Because:

$$
\operatorname{Ord}
$$

has no maximum ordinal, if an observer tower is truly unbounded over all ordinals, there cannot exist some:

$$
\alpha_{\max}
$$

such that all observer ranks do not exceed it.

Therefore:

$$
\boxed{
\text{rank-unbounded}
}
$$

essentially describes:

$$
\boxed{
\text{There is never a final rank stage}.
}
$$

rather than the existence of some:

$$
\infty
$$

as the maximal ordinal node.

---

# 25. Cumulative Hierarchy as an NTLA-O Prototype

Define:

$$
V_0=\varnothing,
$$

$$
V_{\alpha+1}
=
\mathcal P(V_\alpha),
$$

and if:

$$
\lambda
$$

is a limit ordinal:

$$
V_\lambda
=
\bigcup_{\beta<\lambda}V_\beta.
$$

This is precisely the construction of the standard cumulative hierarchy.

For:

$$
\alpha<\beta,
$$

we have:

$$
V_\alpha
\subseteq
V_\beta.
$$

---

# 26. Main Role on $V_\alpha$

For each ordinal $\alpha$, define:

$$
M_\alpha
$$

as the carrier:

$$
S_{M_\alpha}=V_\alpha.
$$

Thus:

$$
\boxed{
\rho_{V_\alpha}(M_\alpha)=M.
}
$$

It must be emphasized here that:

$$
M_\alpha
$$

is merely a role structure.

This paper does not claim that:

$$
V_\alpha
$$

is a complete model of ZFC,

nor does it claim that:

$$
M_\alpha
$$

can determine all truths about $V_\alpha$.

---

# Theorem 6: Cumulative-Hierarchy Role Shift

If:

$$
\alpha<\beta,
$$

then:

$$
V_\alpha\subseteq V_\beta.
$$

Therefore:

$$
\boxed{
\rho_{V_\beta}(M_\alpha)=I.
}
$$

If $M_\beta$ has an admissible downward-read interface to $V_\alpha$, then:

$$
\boxed{
\rho_{V_\alpha}(M_\beta)=E^\uparrow.
}
$$

Thus, the same:

$$
M_\alpha
$$

can change roles relative to different reference domains.

Q.E.D.

---

# 27. Local Unity and Global Unboundedness

Fix some:

$$
V_\alpha.
$$

Its main carrier is:

$$
V_\alpha.
$$

Thus:

$$
\boxed{
\text{Local Main Carrier}=1.
}
$$

But the entirety:

$$
V_0,
V_1,
\ldots,
V_\alpha,
\ldots
$$

has no final ordinal stage.

Therefore:

$$
\boxed{
\text{Global Main-Frame Tower}
}
$$

can continuously unfold in the ordinal direction.

Thus:

$$
\boxed{
\text{Local Unity}
\land
\text{Global Unboundedness}
}
$$

can hold simultaneously.

This is a precise set-theoretic version of the original "One/Unbounded" proposition.

---

# 28. Higher Rank Does Not Imply Stronger Observation

Consider an observer:

$$
\mathcal O_H
$$

with a high rank carrier, but which only allows:

$$
\mathcal A_H
=
\{
\varnothing,D
\}.
$$

Then:

$$
\boxed{
K_H=D\times D.
}
$$

It distinguishes almost no elements.

On the other hand, consider a lower rank observer:

$$
\mathcal O_L
$$

and let:

$$
\mathcal A_L
=
\mathcal P(D).
$$

For any:

$$
x\neq y,
$$

there exists:

$$
A=\{x\}
$$

such that:

$$
x\in A,
\qquad
y\notin A.
$$

Thus:

$$
\boxed{
K_L=\Delta_D.
}
$$

---

# Theorem 7: Rank–Resolution Independence

Merely from:

$$
\operatorname{rank}(\mathcal O_1)
<
\operatorname{rank}(\mathcal O_2)
$$

one cannot deduce:

$$
K_2\subseteq K_1,
$$

nor can one deduce:

$$
K_1\subseteq K_2.
$$

Therefore:

$$
\boxed{
\text{Set-Theoretic Height}
\neq
\text{Observational Resolution}.
}
$$

Q.E.D.

---

# 29. Three Orthogonal Quantities

Therefore, NTLA-O needs to distinguish at least:

$$
\boxed{
\rho_X(\mathcal O)
}
$$

— Role;

$$
\boxed{
\operatorname{rank}(\mathcal O)
}
$$

— Set-theoretic height;

$$
\boxed{
K_{\mathcal O}
}
$$

— Observational resolution structure.

These three cannot be compressed into a single "observer level".

---

# 30. Minimal Ternary Coordinates of an Observer

Therefore, define:

$$
\boxed{
\mathbf R_X(\mathcal O)
=
\left(
\rho_X(\mathcal O),
\operatorname{rank}(\mathcal O),
K_{\mathcal O}
\right).
}
$$

If the carrier needs to be included:

$$
S_{\mathcal O},
$$

then it is written completely as:

$$
\boxed{
\mathbf R_X^\ast(\mathcal O)
=
\left(
S_{\mathcal O},
\rho_X(\mathcal O),
\operatorname{rank}(\mathcal O),
K_{\mathcal O}
\right).
}
$$

This avoids the following erroneous inference:

$$
\text{outside}
\Rightarrow
\text{higher rank}
\Rightarrow
\text{more knowledge}.
$$

None of the three arrows are general theorems.

---

# 31. Power-Set Observer Expansion

Now consider:

$$
D,
$$

and:

$$
\mathcal P(D).
$$

A first-order observer uses:

$$
A\subseteq D
$$

to distinguish elements in $D$.

If one wishes to study:

> Which predicates are themselves allowed, and how are they classified among each other?

then the new object domain can become:

$$
\mathcal P(D).
$$

and all its subsets are:

$$
\mathcal P(\mathcal P(D)).
$$

Thus, there exists a natural higher-order tower:

$$
\boxed{
D
\rightarrow
\mathcal P(D)
\rightarrow
\mathcal P^2(D)
\rightarrow
\mathcal P^3(D)
\rightarrow
\cdots.
}
$$

---

# 32. Higher-Order Observers are Not Mysterious New Entities

If:

$$
\mathcal O^{(0)}
$$

observes:

$$
D,
$$

then:

$$
\mathcal O^{(1)}
$$

can observe:

$$
\mathcal A_{\mathcal O^{(0)}}
\subseteq
\mathcal P(D).
$$

That is:

> observer of observer distinctions.

One level higher can study:

$$
\mathcal P(\mathcal P(D)).
$$

Therefore:

$$
\boxed{
\text{observer of observers}
}
$$

at least in a minimal version is merely a:

$$
\boxed{
\text{higher-order set construction}.
}
$$

There is no need to first introduce any assumptions of consciousness, ontology, or transcendence.

---

# 33. Significance of Cantor-Type Boundaries

The power set operation:

$$
D\mapsto\mathcal P(D)
$$

should not be understood as "a higher-level observer is necessarily more intelligent".

It merely provides a larger candidate predicate space.

Whether it actually increases the distinguishing power of:

$$
K_{\mathcal O}
$$

still depends on which subsets are actually selected by:

$$
\mathcal A_{\mathcal O}
$$

Thus:

$$
\boxed{
\text{larger power-set ambient space}
\not\Rightarrow
\text{strict observer refinement}.
}
$$

---

# 34. Universe-Relative NTLA-O

In large categories or "all small objects" problems, mathematical practice often needs to handle size conventions.

One choice is to fix a Grothendieck universe $U$ and restrict the study to $U$-small objects. However, there are foundational issues between Grothendieck-universe assumptions and large cardinal strength; therefore, if NTLA-O uses this method, the universe assumption must be written as an additional foundational condition, and cannot be defaulted as a cost-free ZFC result.

Define:

$$
\boxed{
\mathrm{NTLA\!-\!O}_U
}
$$

as the version where all working objects are restricted to a specified universe $U$.

---

# 35. A Universe is Not Necessarily Required

On the other hand, fixing a universe is not the only approach.

For example, the sites/sheaves system of the Stacks Project explicitly states that its treatment chooses not to use universes, demonstrating that large-scale mathematical practice can adopt other size-management conventions.

Therefore, NTLA-O does not write the Grothendieck universe as a basic axiom.

It is merely an optional foundation profile.

---

# 36. Three Foundation Profiles

This paper suggests explicitly distinguishing:

## Profile S: Set-Sized NTLA-O

All domains, observer families, and structures are restricted to ordinary sets.

Denote as:

$$
\boxed{
\mathrm{NTLA\!-\!O}_{\mathrm{set}}.
}
$$

This should be the primary mathematical core moving forward.

---

## Profile U: Universe-Relative NTLA-O

Fix:

$$
U
$$

and study only $U$-small objects.

Denote as:

$$
\boxed{
\mathrm{NTLA\!-\!O}_U.
}
$$

---

## Profile C: Class-Level NTLA-O

Allow proper-class scale totalities such as:

$$
\mathbf{Obs},
\mathbf{Dom},
\operatorname{Ord}
$$

Denote as:

$$
\boxed{
\mathrm{NTLA\!-\!O}_{\mathrm{class}}.
}
$$

NBG-type set-class theory provides a mature foundational language for formally handling sets/classes.

---

# 37. The Three are Not Competing Theories

They are:

$$
\boxed{
\text{three size regimes}.
}
$$

If the same local theorem is completely set-sized, it should preferentially be stated in:

$$
\mathrm{NTLA\!-\!O}_{\mathrm{set}}
$$

Only when truly needing:

$$
\forall\alpha\in\operatorname{Ord}
$$

or global quantifiers like "all domains", should one ascend to the class-level.

This is an important conservative principle.

---

# 38. All Observers Must Specify Scope

In formal papers, it is forbidden to write without explanation:

$$
\boxed{
\{\text{all observers}\}.
}
$$

It should at least be changed to:

$$
\boxed{
\operatorname{Obs}(X)
}
$$

to denote the observer set of a fixed reference domain;

or:

$$
\boxed{
\operatorname{Obs}_U(X)
}
$$

to denote the observer set in a fixed universe;

or:

$$
\boxed{
\mathbf{Obs}
}
$$

and explicitly declared as a class-level totality.

---

# 39. All Domains Likewise Cannot Be Smuggled as a Set

If:

$$
\mathbf{Dom}
$$

means all set-sized NTLA domains,

one cannot directly assume without size qualification that:

$$
\mathbf{Dom}
$$

is itself a set.

In the class-level profile, it can be treated as a class.

In the set-profile, its scope must first be restricted.

---

# 40. Rank-Unbounded Does Not Equal Omniscient

This is one of the most important negative statements of this paper.

Even if:

$$
\forall\alpha\in\operatorname{Ord},
\exists\mathcal O_\alpha
:
\operatorname{rank}(\mathcal O_\alpha)>\alpha,
$$

it absolutely does not imply the existence of some:

$$
\mathcal O^\ast
$$

satisfying:

$$
K_{\mathcal O^\ast}
=
\Delta_D
$$

for all possible $D$.

Thus:

$$
\boxed{
\text{rank-unbounded}
\neq
\text{complete distinction}.
}
$$

One is a size property.

The other is an epistemic/kernel property.

---

# 41. Main Observer Also Does Not Equal Self-Complete

Similarly:

$$
S_M=X
$$

only means:

$$
\boxed{
\rho_X(M)=M.
}
$$

It does not imply:

$$
K_M=\Delta_X.
$$

Therefore:

$$
\boxed{
\text{self-carriage}
\neq
\text{self-completeness}.
}
$$

This continues the Role–Resolution Independence result from the previous paper.

---

# 42. Set-Theoretic Height vs. Nested Structural Depth

One must also distinguish:

$$
\operatorname{rank}(S_{\mathcal O})
$$

from NTLA's own:

$$
d_{\mathrm{nest}}(\mathcal O).
$$

The former comes from the membership hierarchy.

The latter comes from the structural nesting specified by:

$$
\prec
$$

or:

$$
\subsetneq
$$

Therefore, even if:

$$
\operatorname{rank}(A)
<
\operatorname{rank}(B),
$$

it does not necessarily mean:

$$
A\prec B.
$$

Likewise:

$$
A\prec B
$$

is not necessarily defined by the set-theoretic rank itself.

Thus:

$$
\boxed{
\text{foundational hierarchy}
\neq
\text{NTLA structural hierarchy}.
}
$$

---

# 43. Ordinal Depth of Well-Founded Nesting

If the NTLA nesting relation:

$$
\prec
$$

is itself well-founded,

one can define a structural rank:

$$
\boxed{
\rho_{\prec}(x)
=
\sup
\{
\rho_{\prec}(y)+1:
y\prec x
\}.
}
$$

This rank need not equal the set-theoretic membership rank.

This allows the structural depth of NTLA-O to adopt ordinal values of:

$$
0,1,2,\ldots,\omega,\omega+1,\ldots
$$

---

# 44. Non-Well-Founded Structures Cannot Be Forced into Ordinal Rank

If:

$$
x_0
\prec
x_1
\prec
x_2
\prec
\cdots
\prec
x_0
$$

forms a cycle,

then this relation is not well-founded.

In this case:

$$
\rho_{\prec}
$$

cannot be normally defined according to the well-founded recursion above.

Therefore, for cyclic nesting, NTLA-O should instead use:

- directed graphs;
- groupoids;
- coalgebras;
- strongly connected components;
- dynamical-system structures;

rather than forcing an ordinal depth onto each node.

---

# 45. Set-Theoretic Unboundedness and Observational Unboundedness Separated Again

Now there appear at least three different types of "unboundedness":

First type:

$$
\boxed{
\operatorname{Unbd}_{\mathrm{nest}}
}
$$

Nesting depth has no finite upper bound.

Second type:

$$
\boxed{
\operatorname{Unbd}_{\mathrm{obs}}
}
$$

Observer classes that cannot be identified with one another have no finite upper bound.

Third type:

$$
\boxed{
\operatorname{Unbd}_{\mathrm{rank}}
}
$$

Observer ranks are unbounded over ordinals.

They generally do not imply one another.

---

# Theorem 8: Three-Unboundedness Independence

In the absence of additional axioms:

$$
\operatorname{Unbd}_{\mathrm{nest}},
$$

$$
\operatorname{Unbd}_{\mathrm{obs}},
$$

$$
\operatorname{Unbd}_{\mathrm{rank}}
$$

are not the same property as one another.

### Proof Outline

One can construct:

1. An infinite nesting chain, but all observers use the same constant observation, thus there is only one observer-equivalence class;

2. Infinitely many different distinction families defined on a fixed low-rank carrier, generating observational multiplicity without needing to be rank-unbounded;

3. Rank-unbounded carriers, but all observers only use the trivial distinction family:

$$
\{
\varnothing,D
\},
$$

where rank is unbounded but observational resolution does not increase.

Thus, the three cannot be generally equated.

Q.E.D.

---

# 46. NTLA-O Set-Theoretic State Vector

Therefore, define:

$$
\boxed{
\mathbf S_{\mathrm{set}}(\mathcal O;X)
=
\left(
\rho_X(\mathcal O),
r_{\in}(\mathcal O),
r_{\prec}(\mathcal O),
\mathcal A_{\mathcal O},
K_{\mathcal O}
\right),
}
$$

where:

$$
r_{\in}
=
\operatorname{rank}(\mathcal O)
$$

is the set-theoretic rank;

$$
r_{\prec}
$$

is the NTLA structural rank (if defined);

$$
\mathcal A_{\mathcal O}
$$

is the admissible distinction family;

$$
K_{\mathcal O}
$$

is the final indistinguishability kernel.

This is much more precise than a single:

$$
\text{observer level}
$$

---

# 47. Interface with the Previous Paper

The core coordinates of the previous paper were:

$$
\boxed{
\left(
\rho_X(\mathcal O),
K_{\mathcal O}
\right).
}
$$

This paper does not replace them.

Rather, it elevates them to:

$$
\boxed{
\left(
\rho_X(\mathcal O),
r_{\in}(\mathcal O),
r_{\prec}(\mathcal O),
\mathcal A_{\mathcal O},
K_{\mathcal O}
\right).
}
$$

Thus:

$$
\boxed{
\text{role}
}
$$

still answers:

> Where is it relative to the reference domain?

And:

$$
\boxed{
r_{\in}
}
$$

answers:

> How high is it in the set-theoretic cumulative hierarchy?

$$
\boxed{
r_{\prec}
}
$$

answers:

> How deep is it in the NTLA structural nesting?

$$
\boxed{
K_{\mathcal O}
}
$$

answers:

> What exactly can it distinguish?

---

# 48. Core Theorem Group of This Paper

This paper establishes:

### Theorem A: Set-Theoretic Observer Kernel

$$
\mathcal A_{\mathcal O}
\subseteq\mathcal P(D)
$$

naturally induces the equivalence relation:

$$
K_{\mathcal O}.
$$

### Theorem B: Distinction-Family Monotonicity

$$
\mathcal A_1\subseteq\mathcal A_2
\Longrightarrow
K_2\subseteq K_1.
$$

### Theorem C: Set-Indexed Union Bound

Any set-indexed family of sets has a set-sized inclusion upper bound.

### Theorem D: Set-Sized Observer Rank Boundedness

The ranks of any observer set are uniformly bounded by some ordinal.

### Theorem E: Rank-Unbounded Totality Non-Set

If observer ranks are unbounded over all ordinals, then the totality cannot be a set.

### Theorem F: Cumulative-Hierarchy Role Shift

$$
V_\alpha\subseteq V_\beta
$$

provides a prototype for main/internal/upper-external role shifts.

### Theorem G: Rank–Resolution Independence

Set-theoretic height does not determine observational resolution.

### Theorem H: Three-Unboundedness Independence

Structural unboundedness, observational unboundedness, and rank unboundedness are generally independent of one another.

---

# 49. Statement of Theoretical Strength

### Standard Set-Theoretic Structures Directly Used in This Paper

- Sets;
- Subsets;
- Power sets;
- Functions;
- Equivalence relations;
- Quotient sets;
- Ordinals;
- Rank;
- Cumulative hierarchy;
- Set/class size distinction.

Set theory, like categories/topology, is a foundational layer explicitly and independently treated in the foundational parts of the Stacks Project.

### NTLA-O Structures Assembled in This Paper

- Admissible distinction family;
- Separation of the role/rank/resolution axes;
- NTLA interpretation of observer families;
- Separation of the three types of unboundedness;
- M/I/E observer-role interpretation of the cumulative hierarchy.

### This Paper Does Not Claim

- To invent the power set;
- To invent ordinal rank;
- To invent the cumulative hierarchy;
- To invent proper classes;
- To invent NBG;
- That all mathematics must use class theory;
- That the Grothendieck universe is a necessary axiom for NTLA-O;
- That higher rank implies higher intelligence;
- That a class-level observer tower represents divinity, omniscience, or an ultimate subject;
- The existence of an ordinary set of all observers.

---

# 50. Core Conclusions

The set-theoretic foundation of NTLA-O can ultimately be compressed into two mutually orthogonal generative chains.

The first is:

$$
\boxed{
D
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal P(D)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal Q_{\mathcal O}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal L_{\mathcal O}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal A_{\mathcal O}
}
$$

$$
\Downarrow
$$

$$
\boxed{
K_{\mathcal O}
}
$$

$$
\Downarrow
$$

$$
\boxed{
D/K_{\mathcal O}.
}
$$

This is the:

# **Distinction Axis**

The second is:

$$
\boxed{
V_0
\subseteq
V_1
\subseteq
\cdots
\subseteq
V_\alpha
\subseteq
\cdots
}
$$

This is the:

# **Set-Theoretic Height Axis**

Therefore:

$$
\boxed{
\text{Observer Height}
\neq
\text{Observer Distinction}.
}
$$

And outside these two axes, there also exists the:

$$
\boxed{
\rho_X(\mathcal O)
}
$$

role axis.

Thus, the minimal three-dimensional set-theoretic structure of NTLA-O is:

$$
\boxed{
\text{Role}
\times
\text{Set-Theoretic Height}
\times
\text{Distinction Resolution}.
}
$$

Finally, if the "absolutely unbounded observer" is retained as a shorthand, its precise mathematical content must be restricted to:

$$
\boxed{
\forall\alpha\in\operatorname{Ord},
\exists\mathcal O:
\operatorname{rank}(\mathcal O)>\alpha.
}
$$

And this immediately implies:

$$
\boxed{
\text{the totality is not set-sized}.
}
$$

Beyond this, no metaphysical conclusions are attached.

This allows NTLA-O to use the set-theoretic language with the greatest "sense of colossal scale" while maintaining the most conservative mathematical interpretation.

---

# 51. Next Paper

The next paper will no longer increase set-theoretic height, but will return to topology.

Building on this paper's:

$$
\mathcal A_{\mathcal O}
\subseteq
\mathcal P(D)
$$

if $\mathcal A_{\mathcal O}$ satisfies topological closure conditions, we will obtain:

$$
\boxed{
\tau_{\mathcal O}.
}
$$

and further study:

$$
K_{\mathcal O},
$$

topological indistinguishability,

$$
T_0
$$

separation,

Kolmogorov quotients,

specialization preorders,

and the refinement between different observer topologies.

Therefore, the next paper is:

# **NTLA-O III: Observer Topologies, Indistinguishability Kernels, and Quotient Spaces**

Its core question is:

$$
\boxed{
\text{Under what conditions does an observer's distinction family truly generate a topology?}
}
$$

and:

$$
\boxed{
\text{observer refinement}
\Longleftrightarrow
\text{topological refinement}
}
$$

under what conditions it can strictly hold.

---

# References

1. The Stacks Project. *Set Theory*, Chapter 3; *Categories*, Chapter 4; *Topology*, Chapter 5.
2. Banakh, T. (2020). *Classical Set Theory: Theory of Sets and Classes*. NBG-based introductory foundations.
3. Goldberg, G., & Schlutzenberg, F. (2020). *Periodicity in the Cumulative Hierarchy*. Uses the standard $V_\alpha$ cumulative hierarchy in ZF.
4. Lo Monaco, G. (2019). *Dependent Products and 1-Inaccessible Universes*. On Grothendieck universes and associated large-cardinal strength in categorical settings.
5. Wheeler, W. H. (2023). *Andrew Wiles' Proof of Fermat's Last Theorem, As Expected, Does Not Require a Large Cardinal Axiom*. Discussion of Grothendieck universes and foundational strength.
6. Neo.K & Aletheia (2026). *NTLA-O I: Main-Internal-External Observers, Admissibility, Domain of Evaluation, and Observation Difference Kernels*.

---

**Document Status:** Formal Draft v0.1  
**Series Position:** NTLA-O Series Paper 3 / 9  
**Next Paper:** NTLA-O III — Observer-Induced Topology, Indistinguishability Kernels, and Quotient Spaces