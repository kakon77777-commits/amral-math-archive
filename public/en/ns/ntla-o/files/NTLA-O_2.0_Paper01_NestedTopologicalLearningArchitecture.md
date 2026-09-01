# Nested Topological Learning Architecture 2.0
## From Topological Matching and Difference-Sensitive Connections to Observer-Relative Structural Learning

**English Title:** *Nested Topological Learning Architecture 2.0: From Topological Matching and Difference-Sensitive Connections to Observer-Relative Structural Learning*  
**Abbreviation:** NTLA 2.0  
**Series:** NTLA-O Series, Paper 1  
**Version:** v0.1 Formal Draft  
**Author:** Neo.K  
**Theoretical Organization and Formalization Collaboration:** Aletheia / GPT-5.6 Sol  
**Date:** 2026-08-17

---

## Abstract

The early "Nested Topological Learning Architecture" (NTLA) proposed a core intuition: complex theories, concepts, or knowledge structures should not be represented merely as single vectors or fixed strings, but can instead be represented as multi-layered nested topological structures. Learning can thus be partially understood as a layer-by-layer matching between the model structure and the target structure. The previous version further utilized persistent homology and bottleneck distance as topological comparison tools, describing multi-order learning through a generate-approximate-recover process.

NTLA 2.0 retains this core but systematically revises its mathematical rigor.

First, this paper no longer claims that "general learning is equivalent to topological matching." Topological matching is repositioned as a structural learning representation framework; its applicability depends on the object of study, the representation functor, and the selected invariants.

Second, bottleneck distance is no longer defined as the universal or sole loss function of NTLA. It serves as a valid distance only on components where filtration, persistent homology, and persistence-diagram representations have been established. Classical persistent homology stability theory guarantees that, under appropriate conditions, small perturbations in the input function lead to controlled perturbations in the persistence diagram, but this does not imply that the persistence diagram is a complete invariant for arbitrary structures.

Third, this paper introduces "difference-sensitive connection structures." Even if two objects possess the same Betti numbers, identical partial homological data, or even the same coarse-grained topological summaries, they are not automatically judged as identical by NTLA 2.0. Connections, nestings, directions, paths, and histories between holes, regions, or conceptual nodes can be selected as part of the identity structure.

Fourth, this paper establishes an observer-ready interface for the subsequent NTLA-O. Structural identity no longer relies on a single absolute comparison function, but explicitly depends on "which differences are allowed to be observed, which differences are judged as valid, and which differences are quotiented out by equivalence relations."

Therefore, NTLA 2.0 is revised from the early "topological learning architecture" to:

$$
\boxed{
\text{Nested Structural Representation}
+
\text{Topological Invariants}
+
\text{Difference-Sensitive Relations}
+
\text{Explicit Identity Criterion}.
}
$$

This paper only proposes a mathematical representation and learning framework; it does not assert that all cognition, AI learning, or theory formation necessarily obeys NTLA.

**Keywords:** Nested topology, nested learning, persistent homology, structural learning, bottleneck distance, inverse system, connection difference, theory representation, observer relativity

---

# 1. Motivation for Revision

## 1.1 Core of the Old NTLA

The core structure of the old NTLA can be summarized as:

$$
T^\infty
=
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots.
$$

Where different $T_n$ represent theoretical/knowledge structures at different depths or resolutions.

If there exist projections:

$$
p_{n+1,n}:
T_{n+1}
\rightarrow
T_n,
$$

then higher-order representations can be projected onto coarser representations.

An important intuition of the previous version was:

$$
\boxed{
\text{learning}
\approx
\text{nested structural alignment}.
}
$$

This intuition is retained in this paper.

However, "$\approx$" cannot be surreptitiously replaced by a universal mathematical equality.

---

# 2. First Revision: Learning is Not Equivalent to Topological Matching

Let a general learning system be:

$$
\mathfrak L
=
(\mathcal X,\mathcal Y,\Theta,\mathcal A,\mathcal E),
$$

Where:

- $\mathcal X$ is the input domain;
- $\mathcal Y$ is the output or target domain;
- $\Theta$ is the model state/parameter space;
- $\mathcal A$ is the update mechanism;
- $\mathcal E$ is the evaluation condition.

NTLA additionally selects a representation mapping:

$$
\Phi:
\mathfrak L
\rightarrow
\mathfrak T,
$$

Where:

$$
\mathfrak T
$$

is some nested structural space.

Therefore, the formal assertion of NTLA should only be written as:

$$
\boxed{
\text{Certain learning problems can be translated via }
\Phi
\text{ into nested structural matching problems.}
}
$$

Instead of:

$$
\boxed{
\text{All learning is ontologically topological matching.}
}
$$

The strengths of these two propositions are completely different.

---

# 3. Basic Structure of NTLA 2.0

Define the $n$-th layer NTLA state:

$$
\boxed{
\mathcal T_n
=
\left(
X_n,
\tau_n,
\mathcal H_n,
\mathcal C_n,
\Lambda_n
\right).
}
$$

Where:

- $X_n$: the underlying set of the $n$-th layer;
- $\tau_n$: the topology selected for this layer;
- $\mathcal H_n$: the nested/inclusion structure;
- $\mathcal C_n$: the difference-sensitive connection structure;
- $\Lambda_n$: labels, types, or other data that must be preserved in the study.

The primary information of the old NTLA was concentrated in:

$$
(X_n,\tau_n).
$$

The new version explicitly elevates this to:

$$
\boxed{
(X_n,\tau_n,\mathcal H_n,\mathcal C_n,\Lambda_n).
}
$$

Therefore:

$$
\boxed{
\text{topological type}
\neq
\text{full NTLA identity}.
}
$$

---

# 4. Difference-Sensitive Connection Structure

Let:

$$
H_n
$$

denote the selected structural units of the $n$-th layer, which can be holes, regions, conceptual nodes, components, or other objects of study.

Define:

$$
\mathcal C_n
=
\left(
E_n,
N_n,
D_n,
P_n,
G_n
\right),
$$

Where:

$$
E_n
$$

records direct connections,

$$
N_n
$$

records nestings,

$$
D_n
$$

records directed relations,

$$
P_n
$$

records selected path data,

$$
G_n
$$

records generative/historical data that must be preserved for research purposes.

Not all applications must retain all five categories of data.

Thus, an identity specification is defined:

$$
\boxed{
\mathfrak I
\subseteq
\{
\tau,\mathcal H,E,N,D,P,G,\Lambda,\ldots
\}.
}
$$

Only differences specified by:

$$
\mathfrak I
$$

as necessary structures for identity are prohibited from being quotiented out.

---

# 5. Principle of Valid Differences

NTLA 2.0 does not adopt:

$$
\boxed{
\text{Any literal difference represents a new object.}
}
$$

Instead, it adopts:

$$
\boxed{
\text{Any difference specified as valid by the identity specification }
\mathfrak I
\text{ must be preserved.}
}
$$

Therefore, renaming:

$$
h_1\mapsto h_a,
\qquad
h_2\mapsto h_b
$$

If all $\mathfrak I$ structures are preserved, they can still belong to the same structural isomorphism class.

But if:

$$
E_A\neq E_B
$$

or:

$$
N_A\neq N_B
$$

and $E,N\in\mathfrak I$, one cannot claim:

$$
A\equiv B.
$$

merely because both possess the same Betti numbers.

---

# 6. Second Revision: Betti Numbers Are Not Complete Identities

For a topological space $X$, the Betti numbers:

$$
\beta_k(X)
=
\operatorname{rank}H_k(X)
$$

can describe certain homological information.

However:

$$
\beta_k(X)=\beta_k(Y)
$$

does not generally imply:

$$
X\cong Y.
$$

Similarly:

$$
H_\ast(X)\cong H_\ast(Y)
$$

cannot be regarded as a complete classification up to homeomorphism in the general case.

Therefore, NTLA 2.0 divides topological data into:

$$
\boxed{
\text{coarse invariants}
}
$$

and:

$$
\boxed{
\text{identity-complete data relative to a chosen class}.
}
$$

The former is suitable for rapid comparison.

Only the latter is sufficient to support strong identity claims.

---

# 7. The Position of Persistent Homology

If an NTLA layer possesses a filtration:

$$
K_a
\subseteq
K_b,
\qquad
a\leq b,
$$

then persistent homology can be established:

$$
H_k(K_a)
\rightarrow
H_k(K_b).
$$

From this, a persistence module and a persistence diagram can be obtained.

What persistent homology provides is:

$$
\boxed{
\text{A summary of topological features persisting across scales}.
}
$$

It is particularly suited for the multi-resolution representation of NTLA.

However, a persistence diagram should not be automatically understood as the complete identity card of the original structure.

In fact, in general q-tame persistence modules, an ordinary persistence diagram itself is not necessarily a complete invariant; the literature even requires the introduction of an observable category to restore complete classification under corresponding localized settings.

Therefore:

$$
\boxed{
\text{persistence summary}
\neq
\text{full NTLA structure}.
}
$$

---

# 8. Third Revision: The Legitimate Position of Bottleneck Distance

The old NTLA placed bottleneck distance in an overly central position.

The new version revises this to:

If:

$$
D_X,
D_Y
$$

are persistence diagrams obtained under the same specification,

then one can use:

$$
d_B(D_X,D_Y)
$$

to measure the difference in this persistence representation.

Classical stability theorems provide, under appropriate conditions, something like:

$$
d_B
\left(
\operatorname{Dgm}(f),
\operatorname{Dgm}(g)
\right)
\leq
\|f-g\|_\infty.
$$

Its significance is that the persistence diagram possesses stability against certain types of small input perturbations.

But this result does not imply:

$$
\boxed{
d_B
=
\text{universal learning loss}.
}
$$

Nor does it imply:

$$
\boxed{
d_B=0
\Rightarrow
\text{The original theories/structures are completely identical}
}
$$

holds true under any unspecified representation conditions.

---

# 9. NTLA 2.0 Multi-Component Loss

Therefore, the new version defines:

$$
\boxed{
\mathcal L_{\mathrm{NTLA}}
=
\lambda_{\mathrm{task}}
\mathcal L_{\mathrm{task}}
+
\lambda_{\mathrm{top}}
\mathcal L_{\mathrm{top}}
+
\lambda_{\mathrm{conn}}
\mathcal L_{\mathrm{conn}}
+
\lambda_{\mathrm{nest}}
\mathcal L_{\mathrm{nest}}
+
\lambda_{\mathrm{id}}
\mathcal L_{\mathrm{id}}.
}
$$

Where:

$$
\mathcal L_{\mathrm{task}}
$$

evaluates the original task performance;

$$
\mathcal L_{\mathrm{top}}
$$

evaluates the selected topological representation;

$$
\mathcal L_{\mathrm{conn}}
$$

evaluates the connection structure;

$$
\mathcal L_{\mathrm{nest}}
$$

evaluates the nested structure;

$$
\mathcal L_{\mathrm{id}}
$$

evaluates the data that must not be lost according to the identity specification.

If persistent homology is used, one can set:

$$
\mathcal L_{\mathrm{top}}
=
\sum_k
w_k
d_B
\left(
D_k^{\mathrm{model}},
D_k^{\mathrm{target}}
\right).
$$

But this is merely one possible instance of:

$$
\mathcal L_{\mathrm{top}}.
$$

---

# 10. Multi-Layer NTLA System

Let:

$$
\mathcal T_0,
\mathcal T_1,
\mathcal T_2,
\ldots
$$

be different resolution ranks.

Define bonding maps:

$$
p_{n+1,n}:
\mathcal T_{n+1}
\rightarrow
\mathcal T_n.
$$

If they satisfy:

$$
p_{n,n}
=
\operatorname{id},
$$

and:

$$
p_{k,i}
=
p_{j,i}
\circ
p_{k,j}
\qquad
(i<j<k),
$$

then:

$$
\boxed{
\left(
\mathcal T_n,
p_{n+1,n}
\right)
}
$$

forms an inverse system.

This provides the old NTLA:

$$
T_0
\leftarrow
T_1
\leftarrow
T_2
\leftarrow
\cdots
$$

with a more standard mathematical interpretation.

---

# 11. "Nested" in NTLA Means More Than Set Inclusion

The new version distinguishes three types of nesting.

## 11.1 Set Nesting

$$
X_{n+1}\subseteq X_n.
$$

## 11.2 Structural Resolution Nesting

Higher-order structures preserve lower-order structures and add new distinguishable data:

$$
F_n
=
q_n\circ F_{n+1}.
$$

## 11.3 Container Nesting

One structure exists within a valid container of another structure:

$$
\mathcal H(A,B)=1.
$$

The three can coincide, but are not necessarily identical.

Therefore:

$$
\boxed{
\text{nested}
}
$$

in NTLA 2.0 always requires specifying which type of nesting is meant.

---

# 12. Structural Resolution Function

Let the universal set of study objects be:

$$
\Omega.
$$

The $n$-th order structure reading is:

$$
F_n:
\Omega
\rightarrow
Y_n.
$$

Define:

$$
x\sim_ny
\iff
F_n(x)=F_n(y).
$$

And denote:

$$
K_n
=
\{
(x,y):
F_n(x)=F_n(y)
\}.
$$

If:

$$
F_n
=
q_n\circ F_{n+1},
$$

then the next higher order preserves at least all distinguishable information of the lower order.

---

# Theorem 1: NTLA Structural Refinement Monotonicity Theorem

If:

$$
F_n
=
q_n\circ F_{n+1},
$$

then:

$$
\boxed{
K_{n+1}
\subseteq
K_n.
}
$$

### Proof

If:

$$
(x,y)\in K_{n+1},
$$

then:

$$
F_{n+1}(x)
=
F_{n+1}(y).
$$

Therefore:

$$
F_n(x)
=
q_n(F_{n+1}(x))
=
q_n(F_{n+1}(y))
=
F_n(y).
$$

Thus:

$$
(x,y)\in K_n.
$$

Hence:

$$
K_{n+1}\subseteq K_n.
$$

Q.E.D.

---

# 13. Genuine Structural Gain

If:

$$
K_{n+1}=K_n,
$$

then even if the data format of the $n+1$-th layer is more complex, it does not add any new distinguishing capability.

Only when:

$$
\boxed{
K_{n+1}\subsetneq K_n
}
$$

is it said that:

$$
\boxed{
\mathcal T_{n+1}
}
$$

forms a **strict structural refinement** over:

$$
\mathcal T_n.
$$

Therefore:

$$
\boxed{
\text{More parameters}
\not\Rightarrow
\text{More structural information}.
}
$$

And:

$$
\boxed{
\text{More nested layers}
\not\Rightarrow
\text{More distinguishability}.
}
$$

---

# 14. Difference Emergence Rank

For:

$$
x,y\in\Omega,
$$

define:

$$
\boxed{
r(x,y)
=
\min
\{
n:
F_n(x)\neq F_n(y)
\}.
}
$$

If they cannot be separated by any finite $n$, denote:

$$
r(x,y)=\infty.
$$

$r(x,y)$ is called the:

# **Difference Emergence Rank**

That is:

# **Difference Emergence Rank**

It describes:

> At which resolution layer a genuinely preserved structural difference can be represented for the first time.

---

# 15. Example of Holes and Connections

Consider two structures:

$$
A,
B.
$$

Assume:

$$
\beta_1(A)
=
\beta_1(B)
=
3.
$$

The zeroth order only reads:

$$
F_0(X)=\beta_1(X).
$$

Therefore:

$$
F_0(A)=F_0(B).
$$

If the first order adds hole adjacency:

$$
F_1(X)
=
\left(
\beta_1(X),
E_H(X)
\right),
$$

and:

$$
E_H(A)\neq E_H(B),
$$

then:

$$
F_1(A)\neq F_1(B).
$$

Therefore:

$$
\boxed{
r(A,B)=1.
}
$$

Hence:

$$
\boxed{
\text{Identical number of holes}
}
$$

never equals:

$$
\boxed{
\text{Identical hole connection structure}.
}
$$

---

# 16. Revision of the Generate-Approximate-Recover Process

The old NTLA used GAR:

$$
\boxed{
G
\rightarrow
A
\rightarrow
R.
}
$$

The new version retains this, but repositions it as an architecture template rather than a universal law of learning.

## 16.1 Generate

Generate candidate higher-order structures from the current state:

$$
G:
\mathcal T_n
\rightarrow
\mathcal P(\mathcal T_{n+1}).
$$

## 16.2 Approximate

Evaluate candidates according to the selected loss and identity specification:

$$
A:
\mathcal P(\mathcal T_{n+1})
\rightarrow
\mathcal T_{n+1}^{\ast}.
$$

## 16.3 Recover

Check whether the new structure retains necessary information after being projected back to the lower order:

$$
R:
\mathcal T_{n+1}^{\ast}
\rightarrow
\mathcal T_n.
$$

The ideal consistency condition is:

$$
\boxed{
p_{n+1,n}
\left(
\mathcal T_{n+1}^{\ast}
\right)
\approx_{\mathfrak I}
\mathcal T_n.
}
$$

Where:

$$
\approx_{\mathfrak I}
$$

indicates that only the structures specified by the identity specification are required to be preserved.

---

# 17. Recovery is Not Equivalent to a Complete Inverse Mapping

If:

$$
p_{n+1,n}
$$

is not injective,

then there generally does not exist a unique:

$$
p_{n+1,n}^{-1}.
$$

Therefore, the mathematical meaning of Recover is not:

$$
\boxed{
\text{Precisely reversing all coarse-graining}.
}
$$

But rather:

$$
\boxed{
\text{Verifying that the new higher-order representation still satisfies necessary consistency after projection}.
}
$$

This corrects the issue in the old version where recovery was easily interpreted too strongly.

---

# 18. New Definition of Theory Learning

Define the nested representation of the model:

$$
\mathbf T^{\mathrm{model}}
=
\{
\mathcal T_n^{\mathrm{model}}
\}_{n\in I}.
$$

Define the target representation:

$$
\mathbf T^{\mathrm{target}}
=
\{
\mathcal T_n^{\mathrm{target}}
\}_{n\in I}.
$$

The NTLA learning objective is to find a model state $\theta$ such that over a specified resolution range:

$$
J\subseteq I
$$

the comprehensive difference:

$$
\boxed{
\mathcal D_J
\left(
\mathbf T^{\mathrm{model}}_\theta,
\mathbf T^{\mathrm{target}}
\right)
}
$$

is minimized.

However:

$$
\mathcal D_J=0
$$

only means that they are indistinguishable over:

$$
J
$$

and under the specified identity specification.

Unless representation completeness is otherwise proven, one cannot deduce:

$$
\boxed{
\text{The model has acquired the complete structure of the target theory}.
}
$$

---

# 19. Revision of the "Theory Shape Isomorphism" Claim

The old NTLA could be interpreted as having the objective:

$$
T_{\mathrm{model}}
\cong
T_{\mathrm{target}}.
$$

NTLA 2.0 downgrades this to a conditional objective.

Only after first specifying:

1. How the theory is mapped into a mathematical structure;
2. Which structures must be preserved;
3. Which type of isomorphism is adopted;
4. Whether the representation loses information;

can one then discuss:

$$
\boxed{
\Phi(T_{\mathrm{model}})
\cong_{\mathfrak I}
\Phi(T_{\mathrm{target}}).
}
$$

Therefore:

$$
\boxed{
\text{theory isomorphism}
}
$$

is not a relationship that automatically exists between original natural language theories.

It is a representation-relative statement.

---

# 20. Distinction Between NTLA and Existing "Nested Learning"

"Nested Learning" already has other usages in existing machine learning literature.

For example, one line of work uses nested learning for multi-granular predictions and nested information bottlenecks; another newer line of work describes models as multi-layered/parallel nested optimization problems, studying multi-timescale updates and continual learning.

This paper's:

# **Nested Topological Learning Architecture**

is not equivalent to the aforementioned works.

The "Nested" in NTLA primarily refers to:

$$
\boxed{
\text{nested structural/topological resolution}
}
$$

and:

$$
\boxed{
\text{bonded hierarchy of representations}.
}
$$

It does not presuppose:

$$
\boxed{
\text{nested optimization problems}.
}
$$

Therefore, subsequent literature should always use the full name or abbreviation:

$$
\boxed{
\mathrm{NTLA}
}
$$

rather than simply calling it Nested Learning.

---

# 21. Interface Between NTLA 2.0 and NTLA-O

Up to this point, we have not specified:

> Who decides which differences count as differences?

Thus, an observer interface is introduced.

For each observer:

$$
\mathcal O,
$$

the subsequent NTLA-O will define:

$$
\mathcal L_{\mathcal O}
$$

as the valid observation domain,

$$
\mathcal J_{\mathcal O}
$$

as the judgment domain,

and:

$$
K_{\mathcal O}
$$

as the observation indistinguishability kernel.

Consequently, NTLA 2.0's:

$$
K_n
$$

can be further upgraded to:

$$
\boxed{
K_{n,\mathcal O}.
}
$$

This means that:

$$
\boxed{
\text{The same structural resolution layer}
}
$$

under different observers,

may still possess different valid distinguishabilities.

---

# 22. Reserved Interface for Main, Internal, and External Observers

For a reference domain:

$$
X,
$$

the subsequent series will define:

$$
\rho_X(\mathcal O)
\in
\{M,I,E\}.
$$

Where:

$$
M
$$

is the main observer role,

$$
I
$$

is the internal role,

$$
E
$$

is the external role.

NTLA 2.0 only reserves the interface here:

$$
\boxed{
\mathcal T_n
\longrightarrow
\mathcal T_{n,\mathcal O}.
}
$$

It does not prematurely assume in this paper that:

$$
M,
I,
E
$$

there exists any hierarchical relationship of knowledge capability among them.

---

# 23. Minimal Axiom Set of NTLA 2.0

## Axiom N1: Structural Representation Axiom

Objects of study can be mapped within a specified research domain to:

$$
\mathcal T
=
(X,\tau,\mathcal H,\mathcal C,\Lambda).
$$

This is a modeling choice, not an ontological assertion about all existence.

---

## Axiom N2: Identity Specification Axiom

Any claim of "identity" must specify:

$$
\mathfrak I.
$$

---

## Axiom N3: Projection Consistency Axiom

If a projection exists between two resolution layers:

$$
p_{n+1,n},
$$

then its domain, codomain, and preserved structures must be explicitly stated.

---

## Axiom N4: Valid Difference Preservation Axiom

If:

$$
\Delta_{\mathfrak I}(A,B)\neq0,
$$

then it is prohibited to directly write:

$$
A\equiv_{\mathfrak I}B.
$$

without declaring a quotient rule.

---

## Axiom N5: Topological Summary Incompleteness Axiom

Any Betti, homology, persistence, or other selected invariants must not be automatically regarded as a complete structural identity unless completeness has been proven for the research category.

---

## Axiom N6: Loss Function Domain Restriction Axiom

Any:

$$
\mathcal L
$$

must specify which representation component it is comparing.

---

## Axiom N7: Observer Extensibility Axiom

NTLA identity can further depend on:

$$
\mathcal O.
$$

Thus allowing:

$$
K_{n,\mathcal O_1}
\neq
K_{n,\mathcal O_2}.
$$

---

# 24. Main Theorems and Non-Theorems

Currently, the core results in NTLA 2.0 that are genuinely derived directly from definitions include:

$$
F_n=q_n\circ F_{n+1}
\Longrightarrow
K_{n+1}\subseteq K_n.
$$

and:

$$
K_{n+1}\subsetneq K_n
$$

representing that the $n+1$-th layer indeed generates new distinguishing capability.

However, the following are **not universally proven theorems in this paper**:

$$
\boxed{
\text{All learning is topological learning};
}
$$

$$
\boxed{
\text{All theories have a unique topological representation};
}
$$

$$
\boxed{
\text{Bottleneck distance is the optimal or sole loss};
}
$$

$$
\boxed{
\text{Persistence diagrams completely determine all structures};
}
$$

$$
\boxed{
\text{AI theory spaces are necessarily isomorphic to human theory spaces}.
}
$$

If they are to hold in the future, additional assumptions or empirical evidence must be added.

---

# 25. The New Core Formula of NTLA 2.0

The old version could be summarized as:

$$
\text{Theory}
\rightarrow
\text{Topology}
\rightarrow
\text{Matching}.
$$

The new version is changed to:

$$
\boxed{
\text{Object / Theory}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Explicit Representation Choice}
}
$$

$$
\Downarrow
$$

$$
\boxed{
(X,\tau,\mathcal H,\mathcal C,\Lambda)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Nested Resolution Tower}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Selected Invariants}
+
\text{Connection Data}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Identity Criterion}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Structure-Sensitive Learning / Matching}.
}
$$

---

# 26. Relationship with Traditional Topological Data Analysis

The mature results of topological data analysis prove that topology and persistent structures can indeed be used to analyze high-dimensional data; the stability theory of persistent homology also provides a rigorous foundation for multi-scale feature comparison under noise.

NTLA 2.0 does not reinvent these results.

The position of this paper's work is:

$$
\boxed{
\text{Placing these existing topological tools into a nested, difference-sensitive learning representation framework with explicit identity conditions.}
}
$$

Therefore, its potential novelty should be evaluated from:

$$
\boxed{
\text{framework composition}
}
$$

and the subsequent:

$$
\boxed{
\text{observer-indexed refinement}
}
$$

rather than sought within a single persistence technique.

---

# 27. Revision Comparison Table

### Old Claim: Theory Learning Equals Topological Space Matching

New Version:

$$
\boxed{
\text{Topological matching is an optional structural learning representation.}
}
$$

---

### Old Claim: Loss Function is Bottleneck Distance

New Version:

$$
\boxed{
d_B
\text{ is merely a valid candidate loss for the persistence component.}
}
$$

---

### Old Claim: Model and Target Theory Shape Isomorphism

New Version:

$$
\boxed{
\Phi(T_{\mathrm{model}})
\cong_{\mathfrak I}
\Phi(T_{\mathrm{target}})
}
$$

can only be proposed under an explicit representation and identity criterion.

---

### Old Structure: Only Highlights Topology

New Version:

$$
\boxed{
\text{topology}
+
\text{nesting}
+
\text{connection}
+
\text{path/history}
+
\text{identity specification}.
}
$$

---

### Old NTLA: Observers Did Not Formally Enter the Core

New Version:

$$
\boxed{
K_n
\rightarrow
K_{n,\mathcal O}
}
$$

reserves a complete NTLA-O interface.

---

# 28. Statement of Theoretical Strength

The core mathematical work of this paper primarily belongs to:

- Structural definitions;
- Equivalence relations and kernels;
- Inverse systems;
- Multi-resolution representations;
- Conditional use of topological invariants;
- Difference-sensitive identity specifications.

This paper does not claim to:

- Invent persistent homology;
- Invent bottleneck distance;
- Invent inverse systems;
- Have proven a new persistence stability theorem;
- Have established a complete theory of general machine learning;
- Have proven that all knowledge possesses a unique topology;
- Have proven that NTLA is superior to existing learning architectures.

The formal status of NTLA 2.0 is:

$$
\boxed{
\text{formal structural framework}
+
\text{research program}.
}
$$

---

# 29. Series Interface

This paper is the foundational piece of the nine-part NTLA-O series.

Subsequent papers will sequentially address:

$$
\boxed{
\text{Observer Roles}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Set-Theoretic Foundations}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Observer-Induced Topology}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Local--Global Gluing}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Path / Groupoid Identity}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Inverse Observer Towers}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Complete Separation}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Unified NTLA-O}.
}
$$

---

# 30. Conclusion

NTLA 2.0 retains the most important idea of the original NTLA:

$$
\boxed{
\text{Complex knowledge need not be compressed into a single-layer representation;
it can possess a structural shape that unfolds layer by layer.}
}
$$

However, the new version rejects three oversimplifications:

$$
\boxed{
\text{Topological summary}
=
\text{Complete identity},
}
$$

$$
\boxed{
\text{Single distance}
=
\text{Complete learning},
}
$$

and:

$$
\boxed{
\text{Identical final result}
=
\text{Identical structural history}.
}
$$

Therefore, the true core of the new version becomes:

$$
\boxed{
\text{Nested Structure}
+
\text{Difference Preservation}
+
\text{Explicit Quotient Rules}.
}
$$

And when observers enter, it must further add:

$$
\boxed{
\text{Who is allowed to distinguish what?}
}
$$

That is:

$$
\boxed{
\text{Who can legitimately distinguish which differences?}
}
$$

This is precisely the starting point of NTLA-O.

---

# References

1. Carlsson, G. (2009). *Topology and Data*. Bulletin of the American Mathematical Society, 46(2), 255–308.
2. Cohen-Steiner, D., Edelsbrunner, H., & Harer, J. (2007). *Stability of Persistence Diagrams*. Discrete & Computational Geometry, 37, 103–120.
3. Chazal, F., de Silva, V., Glisse, M., & Oudot, S. (2016). *The Structure and Stability of Persistence Modules*. Springer.
4. Chazal, F., Crawley-Boevey, W., & de Silva, V. (2016). *The Observable Structure of Persistence Modules*. Homology, Homotopy and Applications.
5. Edelsbrunner, H., & Harer, J. (2010). *Computational Topology: An Introduction*. American Mathematical Society.
6. Achddou, R., di Martino, J. M., & Sapiro, G. (2020). *Nested Learning for Multi-Granular Tasks*.
7. Behrouz, A., Razaviyayn, M., Zhong, P., & Mirrokni, V. (2025). *Nested Learning: The Illusion of Deep Learning Architectures*.
8. Neo.K & Theia (2026). *Nested Topological Learning Architecture*, EML-NTLA-2026-v1.0. Historical predecessor.
9. Neo.K et al. (2026). *Topological Phase Computation Theory: A Computational Ontology of the Shapes of All Things*. Internal theoretical integration reference.

---

**Document Status:** Formal Draft v0.1  
**Revision Status:** Recommended as the successor canonical draft to EML-NTLA-2026-v1.0; the old version is retained as a historical version and is not directly overwritten.