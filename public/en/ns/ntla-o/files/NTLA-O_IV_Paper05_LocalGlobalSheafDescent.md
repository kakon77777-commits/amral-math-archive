# NTLA-O IV: Local-to-Global Observation, Presheaves, Sheaves, Stalks, and Descent
## From Local States of Internal Observers and Compatible Gluing to Obstructions in Global Reconstruction

**English Title:** *NTLA-O IV: Local-to-Global Observation — Presheaves, Sheaves, Stalks, Germs, and Descent*  
**Series:** NTLA-O Series, Paper 5  
**Version:** v0.1 Formal Draft  
**Prerequisite Paper:** *NTLA-O III: Observation Topology, Indistinguishability Kernels, and Quotient Spaces*  
**Author:** Neo.K  
**Theory Organization and Formalization Assistance:** Aletheia / GPT-5.6 Sol  
**Date:** 2026-08-17

---

## Abstract

The previous paper established the set-theoretic distinction family of the NTLA-O observer:

$$
\mathcal A_{\mathcal O}
\subseteq
\mathcal P(X)
$$

topologically closed as:

$$
\tau_{\mathcal O},
$$

and established the observer kernel:

$$
K_{\mathcal O},
$$

the specialization preorder:

$$
\preceq_{\mathcal O},
$$

and the observer-relative quotient:

$$
X/K_{\mathcal O}.
$$

However, the topology only tells us:

> **Which local regions can serve as valid open observation domains?**

It has not yet explained:

> **What data does an internal observer actually hold in these local domains, and when can the data of different local observers jointly form a global state?**

Therefore, this paper further represents the internal observer of NTLA-O as a local section on an open set.

For the observer topology:

$$
(X,\tau_{\mathcal O}),
$$

we define:

$$
\mathscr F(U)
$$

as the set of valid local observation states on the open set:

$$
U\in\tau_{\mathcal O}.
$$

If:

$$
V\subseteq U,
$$

there exists a restriction map:

$$
\rho^U_V:
\mathscr F(U)
\rightarrow
\mathscr F(V),
$$

and satisfying identity and composition consistency yields a presheaf.

This paper emphasizes:

$$
\boxed{
\text{presheaf}
\not\Rightarrow
\text{local data can always be globally glued}.
}
$$

The sheaf condition precisely adds the requirement: if a family of local sections is consistent on all overlaps, there exists a unique global section gluing them. Standard sheaf theory can write this condition as an equalizer over a cover; the Stacks Project explicitly uses this as the categorical expression of the sheaf condition.

This paper further utilizes the stalk:

$$
\mathscr F_x
=
\varinjlim_{x\in U}
\mathscr F(U)
$$

to establish the "pointwise internal observation state." The elements in a stalk are germs: two local sections represent the same local germ as long as they agree on some smaller common neighborhood. This is the standard stalk construction.

From this, the observation identity in NTLA-O gains a new hierarchy:

$$
\boxed{
\text{global identity}
\Rightarrow
\text{local-section identity}
\Rightarrow
\text{germ identity},
}
$$

while the reverse direction generally does not hold.

This paper also introduces the language of descent. When different local observation data are not literally identical but correspond to each other via transition isomorphisms:

$$
\varphi_{ij}
$$

the cocycle condition on triple overlaps becomes the fundamental constraint for global compatibility; this is exactly the core form of standard descent data.

Thus, the local-to-global problem in NTLA-O is precisely decomposed into:

$$
\boxed{
\text{Local Validity}
}
$$

$$
+
$$

$$
\boxed{
\text{Pairwise Compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{Higher Coherence}
}
$$

$$
+
$$

$$
\boxed{
\text{Effective Gluing}.
}
$$

Having many local observers, or even having every local state be correct, is insufficient on its own to deduce the existence of a global main observation state.

**Keywords:** NTLA-O, presheaf, sheaf, stalk, germ, descent, local-to-global, internal observer, gluing, cocycle, observer reconstruction

---

# 1. From Observer Topology to Local Observer State

The previous paper established:

$$
\boxed{
(X,\tau_{\mathcal O}).
}
$$

Where:

$$
U\in\tau_{\mathcal O}
$$

denotes:

> $U$ is an open domain permitted as a local observation region relative to the observer regime.

But:

$$
U
$$

itself is not an observation state.

Therefore, this paper introduces:

$$
\boxed{
\mathscr F(U).
}
$$

$\mathscr F(U)$ denotes:

> The observation states that can legally exist on the local domain $U$.

For example, it could be:

- local measurement values;
- local topological data;
- local structural labels;
- local functions;
- local models;
- local judgments;
- local connection data;
- local Agent states.

This paper does not restrict their specific content for now.

---

# 2. Restriction

If:

$$
V\subseteq U,
$$

then an observation state valid on $U$ should be restrictable to the smaller region $V$.

Thus, we define:

$$
\boxed{
\rho^U_V:
\mathscr F(U)
\rightarrow
\mathscr F(V).
}
$$

Also denoted as:

$$
s
\mapsto
s|_V.
$$

This answers the question:

> What remains of an observation in a larger local domain when the field of view is narrowed?

---

# 3. Presheaf Observer

## Definition 3.1

If for all open sets:

$$
U\in\tau_{\mathcal O}
$$

there is given:

$$
\mathscr F(U),
$$

and for all:

$$
W\subseteq V\subseteq U
$$

there are given restriction maps such that:

$$
\rho^U_U
=
\operatorname{id}_{\mathscr F(U)}
$$

and:

$$
\boxed{
\rho^V_W
\circ
\rho^U_V
=
\rho^U_W,
}
$$

then:

$$
\boxed{
\mathscr F
}
$$

is called an NTLA-O observer presheaf.

This is exactly the contravariant structure of a standard presheaf on the category of open sets under inclusion; the sheaf framework in the Stacks Project also begins with such presheaves.

---

# 4. Observer Interpretation of a Presheaf

In NTLA-O:

$$
\mathscr F(U)
$$

can be understood as:

$$
\boxed{
\text{all admissible internal-observer states supported on }U.
}
$$

And:

$$
\rho^U_V
$$

represents:

$$
\boxed{
\text{observer state under domain restriction}.
}
$$

Therefore, an internal observer is no longer merely:

$$
S_I\subsetneq X.
$$

It can also carry:

$$
\boxed{
s_I\in\mathscr F(S_I).
}
$$

Written completely as:

$$
\boxed{
I=(S_I,s_I).
}
$$

---

# 5. The Sheaf Model of the Main Observer

If:

$$
X
$$

itself is the entire reference domain,

then:

$$
\mathscr F(X)
$$

represents the global observation states.

Thus, in the sheaf model adopted in this paper, a main-domain global state can be written as:

$$
\boxed{
s_M\in\mathscr F(X).
}
$$

Note:

This does not mean:

$$
\boxed{
\text{all main observers are ontologically equal to a global section}.
}
$$

Rather, it simply means:

> In the local-to-global model of this paper, a global section is the natural mathematical representation of a complete observation state on the main domain.

The role definition:

$$
S_M=X
$$

is retained from the previous paper.

---

# 6. Must Local Restrictions Originate from the Same Global State?

If it is known that:

$$
s\in\mathscr F(X),
$$

then for any:

$$
U\subseteq X
$$

we naturally obtain:

$$
s|_U.
$$

Thus:

$$
\boxed{
\text{Global}
\rightarrow
\text{Local}
}
$$

is usually not a problem.

The real difficulty lies in the reverse direction:

$$
\boxed{
\text{Local}
\rightarrow
\text{Global}?
}
$$

---

# 7. Open Cover

Let:

$$
\mathcal U
=
\{U_i\}_{i\in I}
$$

be an open cover of:

$$
X
$$

such that:

$$
\boxed{
X
=
\bigcup_{i\in I}U_i.
}
$$

Each local observer provides:

$$
s_i
\in
\mathscr F(U_i).
$$

The question is:

> Does there exist some:

$$
s\in\mathscr F(X)
$$

such that:

$$
s|_{U_i}=s_i
$$

holds for all $i$?

---

# 8. Pairwise Compatibility

A minimum necessary condition is:

$$
\boxed{
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}
}
$$

for all:

$$
i,j.
$$

If this does not hold, the two local observations directly conflict in their common observable domain.

Therefore, we define:

$$
\boxed{
\operatorname{Compat}(s_i,s_j)=1
}
$$

if and only if:

$$
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
$$

---

# 9. Local Compatibility is a Necessary Condition

If:

$$
s\in\mathscr F(X)
$$

indeed exists, and:

$$
s_i=s|_{U_i},
$$

then:

$$
s_i|_{U_i\cap U_j}
=
s|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
$$

Therefore:

---

# Theorem 1: Global State Implies Local Compatibility

If a family of local states:

$$
\{s_i\}
$$

originates from the same:

$$
s\in\mathscr F(X),
$$

then:

$$
\boxed{
\forall i,j,
\quad
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
}
$$

Q.E.D.

---

# 10. But Compatibility is Insufficient to Guarantee a Global State

This is precisely the dividing line between a presheaf and a sheaf.

---

# 11. A Counterexample of an NTLA-O Presheaf

Let:

$$
X=\mathbb R
$$

with the standard topology.

Define:

$$
\mathscr B(U)
=
\{
f:U\rightarrow\mathbb R
\mid
f
\text{ is continuous and bounded}
\}.
$$

The restriction maps are just ordinary function restrictions.

This forms a presheaf.

Now take the open cover:

$$
U_n
=
(n-1,n+1),
\qquad
n\in\mathbb Z.
$$

Define:

$$
f_n:
U_n
\rightarrow
\mathbb R
$$

as:

$$
\boxed{
f_n(x)=x.
}
$$

Since each:

$$
U_n
$$

is bounded,

it follows that:

$$
f_n
$$

is bounded on:

$$
U_n.
$$

Thus:

$$
f_n\in\mathscr B(U_n).
$$

On all overlaps:

$$
U_n\cap U_m
$$

both are simply:

$$
x\mapsto x.
$$

Therefore, they are perfectly compatible:

$$
f_n|_{U_n\cap U_m}
=
f_m|_{U_n\cap U_m}.
$$

However, if there exists:

$$
f\in\mathscr B(\mathbb R)
$$

gluing all $f_n$,

it must be that:

$$
f(x)=x
$$

for all:

$$
x\in\mathbb R.
$$

But:

$$
x\mapsto x
$$

is unbounded on:

$$
\mathbb R.
$$

Therefore:

$$
f\notin\mathscr B(\mathbb R).
$$

Thus, there is no global section satisfying the definition of this presheaf.

Therefore:

$$
\boxed{
\text{pairwise compatible local data}
\not\Rightarrow
\text{global section in an arbitrary presheaf}.
}
$$

---

# 12. Sheaf Condition

Thus, additional axioms are required.

The standard sheaf condition requires: for any open cover, a family of compatible local sections must have a unique global section gluing them; in categorical language, this condition can be written as an equalizer diagram.

---

## Definition 12.1: NTLA-O Observer Sheaf

If an observer presheaf:

$$
\mathscr F
$$

satisfies the following two conditions:

### Locality / Uniqueness

If:

$$
s,t\in\mathscr F(U)
$$

and:

$$
s|_{U_i}
=
t|_{U_i}
$$

holds for all $i$ of some open cover:

$$
U=\bigcup_iU_i
$$

then:

$$
\boxed{
s=t.
}
$$

### Gluing / Existence

If:

$$
s_i\in\mathscr F(U_i)
$$

satisfies:

$$
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}
$$

for all $i,j$,

then there exists:

$$
s\in\mathscr F(U)
$$

such that:

$$
s|_{U_i}=s_i.
$$

Then:

$$
\boxed{
\mathscr F
}
$$

is called an NTLA-O observer sheaf.

---

# Theorem 2: Internal Observer Gluing Theorem

Suppose:

$$
X=\bigcup_iU_i,
$$

and:

$$
\mathscr F
$$

is an observer sheaf.

If:

$$
s_i\in\mathscr F(U_i)
$$

satisfies:

$$
\boxed{
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}
}
$$

for all:

$$
i,j,
$$

then there exists a unique:

$$
\boxed{
s\in\mathscr F(X)
}
$$

such that:

$$
s|_{U_i}=s_i
$$

for all $i$.

### Proof

This is exactly the sheaf existence and uniqueness axioms.

Q.E.D.

This is the standard sheaf gluing principle; the Stacks Project provides a direct formulation for the existence and unique gluing of sections.

---

# 13. The Local-to-Global Closure Formula of NTLA-O

Therefore, in the sheaf model:

$$
\boxed{
\text{Covering}
}
$$

$$
+
$$

$$
\boxed{
\text{Local States}
}
$$

$$
+
$$

$$
\boxed{
\text{Overlap Compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{Sheaf Property}
}
$$

implies:

$$
\boxed{
\text{Unique Global State}.
}
$$

This can be condensed into:

$$
\boxed{
\{
s_i
\}_{i\in I}
\xrightarrow{\mathrm{compatible}}
s.
}
$$

---

# 14. "All Internal Observers Being Correct" is Still Not Enough

We can now clearly distinguish three scenarios.

### Scenario A: The local observer itself is incorrect

Some:

$$
s_i
$$

does not even belong to:

$$
\mathscr F(U_i).
$$

Namely:

$$
\boxed{
\text{local invalidity}.
}
$$

### Scenario B: Every local state is valid, but overlaps conflict

$$
s_i|_{U_i\cap U_j}
\neq
s_j|_{U_i\cap U_j}.
$$

Namely:

$$
\boxed{
\text{compatibility failure}.
}
$$

### Scenario C: All local states are valid and pairwise compatible, but the presheaf lacks the sheaf property

There may still be no global section.

Namely:

$$
\boxed{
\text{global realization failure}.
}
$$

Therefore:

$$
\boxed{
\text{local correctness}
\neq
\text{global reconstructibility}.
}
$$

---

# 15. Equalizer Form

For an open cover:

$$
U=\bigcup_iU_i,
$$

the sheaf condition can be written as:

$$
\boxed{
\mathscr F(U)
\longrightarrow
\prod_i
\mathscr F(U_i)
\rightrightarrows
\prod_{i,j}
\mathscr F(U_i\cap U_j).
}
$$

where the two right arrows are respectively:

$$
(s_i)_i
\mapsto
(s_i|_{U_i\cap U_j})_{i,j},
$$

and:

$$
(s_i)_i
\mapsto
(s_j|_{U_i\cap U_j})_{i,j}.
$$

The sheaf condition requires that:

$$
\mathscr F(U)
$$

is exactly the equalizer of these two arrows. This is the standard categorical formulation.

---

# 16. Observer Globalization Operator

On compatible local data, we can abstractly denote:

$$
\boxed{
\operatorname{Glue}_{\mathscr F}
:
\operatorname{Compat}
\left(
\prod_i\mathscr F(U_i)
\right)
\rightarrow
\mathscr F(U).
}
$$

If:

$$
\mathscr F
$$

is a sheaf,

then:

$$
\operatorname{Glue}_{\mathscr F}
$$

is uniquely defined on every compatible family.

Thus:

$$
\boxed{
\text{global observer reconstruction}
}
$$

can be understood as:

$$
\boxed{
\text{sheaf gluing}.
}
$$

---

# 17. Stalks: Shrinking the Internal Observer to the Vicinity of a Point

If we do not care about fixed-size local domains, but only ask:

> What local information does the observer ultimately retain around the point $x$?

Then consider all open neighborhoods containing:

$$
x
$$

namely:

$$
U\ni x.
$$

The stalk is defined as the directed colimit:

$$
\boxed{
\mathscr F_x
=
\varinjlim_{x\in U}
\mathscr F(U).
}
$$

The Stacks Project defines a stalk as the colimit over this system of neighborhoods, and calls the image of a section in the stalk a germ.

---

# 18. Germs

Take:

$$
s\in\mathscr F(U),
\qquad
x\in U.
$$

Its germ at:

$$
x
$$

is denoted as:

$$
\boxed{
s_x\in\mathscr F_x.
}
$$

Two local sections:

$$
s\in\mathscr F(U),
$$

$$
t\in\mathscr F(V)
$$

have the same germ at $x$ if and only if there exists:

$$
W\subseteq U\cap V,
\qquad
x\in W,
$$

such that:

$$
\boxed{
s|_W=t|_W.
}
$$

---

# 19. Germ Observer Identity

Thus, we define:

$$
\boxed{
s
\equiv_{\mathrm{germ},x}
t
}
$$

if and only if:

$$
s_x=t_x.
$$

This is a more localized observer identity than section identity.

It is possible that:

$$
s\neq t
$$

as sections on $U$,

but:

$$
\boxed{
s_x=t_x.
}
$$

because they only differ far away from $x$.

---

# 20. Identity Hierarchy

Thus, NTLA-O yields at least:

$$
\boxed{
\text{Global Section Identity}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Restriction Identity on }U
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Germ Identity at }x.
}
$$

If:

$$
s=t
$$

holds globally,

then all its restrictions and germs are naturally identical.

But:

$$
s_x=t_x
$$

generally does not imply:

$$
s=t.
$$

Therefore:

$$
\boxed{
\text{germ identity}
}
$$

is a coarser-grained local identity.

---

# 21. Germ Difference Emergence

For two local observation states:

$$
s,t,
$$

we can define their difference support:

$$
\boxed{
\operatorname{Diff}(s,t)
=
\{
x:
s_x\neq t_x
\}.
}
$$

If:

$$
x\notin\operatorname{Diff}(s,t),
$$

it means the two observations are locally consistent around $x$.

Thus, the original NTLA question:

> Where exactly does the difference occur?

can now become:

$$
\boxed{
\text{On which stalks does the difference first split?}
}
$$

---

# 22. Sheaf Sections Can Be Checked for Equality via Stalks

The locality of a sheaf means that if two sections have the same germ at every point, then they are identical. The Stacks Project explicitly states that for a sheaf, the natural map from a section to all its stalks is injective.

---

# Theorem 3: Stalkwise Identity Determines Section Identity

If:

$$
\mathscr F
$$

is a sheaf,

and:

$$
s,t\in\mathscr F(U),
$$

satisfying:

$$
\boxed{
\forall x\in U,
\quad
s_x=t_x,
}
$$

then:

$$
\boxed{
s=t.
}
$$

### Proof

For each:

$$
x\in U,
$$

from:

$$
s_x=t_x
$$

there exists an open neighborhood:

$$
V_x\ni x
$$

such that:

$$
s|_{V_x}
=
t|_{V_x}.
$$

And:

$$
U
=
\bigcup_{x\in U}V_x.
$$

By sheaf uniqueness:

$$
s=t.
$$

Q.E.D.

---

# 23. Stalkwise Completeness Does Not Imply Single-Stalk Omniscience

Theorem 3 uses:

$$
\boxed{
\forall x\in U.
}
$$

not:

$$
\boxed{
\exists x.
}
$$

Therefore, a single stalk:

$$
\mathscr F_x
$$

is generally insufficient to recover the entire global section.

Thus:

$$
\boxed{
\text{perfectly detailed local observer}
\not\Rightarrow
\text{global observer}.
}
$$

This once again supports:

$$
\boxed{
\text{Internal}
\neq
\text{Incomplete by definition},
}
$$

but also:

$$
\boxed{
\text{Internal local completeness}
\neq
\text{global completeness}.
}
$$

---

# 24. Observer Covers

We can now formally write a set of internal observers as:

$$
\boxed{
\mathfrak I
=
\{
(U_i,s_i)
\}_{i\in I}
}
$$

where:

$$
X=\bigcup_iU_i.
$$

This is called an:

# **Internal Observer Cover**

Its completeness requires at least two distinct conditions:

### Spatial Coverage

$$
\boxed{
X=\bigcup_iU_i.
}
$$

### State Compatibility

$$
\boxed{
s_i|_{U_i\cap U_j}
=
s_j|_{U_i\cap U_j}.
}
$$

Therefore:

$$
\boxed{
\text{coverage}
\neq
\text{coherence}.
}
$$

---

# 25. Counterexample of Insufficient Coverage

If:

$$
\bigcup_iU_i
\neq
X,
$$

then even if all local states are perfectly compatible,

there still exists:

$$
x\in
X\setminus
\bigcup_iU_i
$$

without any local observation.

Thus, one cannot uniquely determine all data on $X$ relying solely on these sections.

Therefore:

$$
\boxed{
\text{observer multiplicity}
\neq
\text{domain coverage}.
}
$$

No matter how many observers there are, if they are all crowded into the same region, they may still be completely blind to other regions.

---

# 26. Sheafification: Completing Locally Gluable Information into a Sheaf

Standard sheaf theory allows the construction of a sheafification for any presheaf:

$$
\mathscr F
$$

namely:

$$
\boxed{
\mathscr F
\rightarrow
\mathscr F^\#.
}
$$

The Stacks Project explicitly provides this canonical morphism and the sheafification construction.

In NTLA-O, we can understand:

$$
\mathscr F^\#
$$

as:

> Sending observation data that is locally representable in the original presheaf but lacks sufficient global closure into its standard sheaf completion.

---

# 27. But Sheafification is Not "Correcting the Truth"

One must be very careful with this point.

$$
\boxed{
\mathscr F
\rightarrow
\mathscr F^\#
}
$$

is the mathematical universal sheafification.

It does not mean:

$$
\boxed{
\text{the original observer is wrong, and the sheafified observer is true.}
}
$$

For example, after sheafification, the aforementioned "bounded continuous functions" presheaf may allow continuous functions that are locally bounded but not necessarily globally bounded.

This is changing the admissible global-state class.

Therefore:

$$
\boxed{
\text{sheafification}
=
\text{closure/completion operation},
}
$$

is not an epistemological truth correction.

---

# 28. Local Equality and Transition Equivalence

So far, compatibility has used:

$$
s_i=s_j
$$

holding on the overlap.

But a more general situation is:

local observers use different coordinates, different representations, different gauges, or different valid languages.

In this case, we do not require:

$$
s_i|_{U_{ij}}
=
s_j|_{U_{ij}},
$$

but may only require the existence of a transition isomorphism:

$$
\boxed{
\varphi_{ij}
:
\mathscr F_i|_{U_{ij}}
\overset{\sim}{\longrightarrow}
\mathscr F_j|_{U_{ij}}.
}
$$

where:

$$
U_{ij}=U_i\cap U_j.
$$

---

# 29. Triple Overlaps

Requiring only pairwise transitions is not enough.

For:

$$
U_{ijk}
=
U_i\cap U_j\cap U_k,
$$

transitioning from $i$ to $k$ can take two paths:

$$
i\rightarrow k
$$

or:

$$
i\rightarrow j\rightarrow k.
$$

Consistency requires that:

$$
\boxed{
\varphi_{ik}
=
\varphi_{jk}
\circ
\varphi_{ij}
}
$$

holds on the triple overlap.

More strictly, in the language of pullbacks/descent, one must use the pullbacks of the corresponding projections; this is precisely the cocycle condition of a standard descent datum.

---

# 30. NTLA-O Cocycle Coherence

Thus, we define a local observer transition family:

$$
\Phi
=
\{
\varphi_{ij}
\}.
$$

If:

$$
\boxed{
\varphi_{ii}
=
\operatorname{id},
}
$$

$$
\boxed{
\varphi_{ji}
=
\varphi_{ij}^{-1},
}
$$

and:

$$
\boxed{
\varphi_{ik}
=
\varphi_{jk}\circ\varphi_{ij}
}
$$

hold on all appropriate overlaps,

then:

$$
\Phi
$$

is said to be observer cocycle-coherent.

---

# 31. Pairwise Agreement and Higher Coherence Separate Again

Even if:

$$
\varphi_{ij}
$$

exists for every pair of observers,

it is still possible that:

$$
\varphi_{ik}
\neq
\varphi_{jk}\circ\varphi_{ij}.
$$

In this case, all pairwise translations exist,

but the entire ternary relationship fails to form a consistent global identification system.

Therefore:

$$
\boxed{
\text{pairwise translatability}
\not\Rightarrow
\text{global coherence}.
}
$$

This is especially important for multi-observer and multi-Agent systems.

---

# 32. Descent Data

More generally, standard descent theory investigates:

> When do local objects and their overlap isomorphisms originate from some global object?

The Stacks Project defines a descent datum for quasi-coherent sheaves using each local object, pairwise isomorphisms, and the triple-overlap cocycle condition.

Thus, NTLA-O can abstractly write:

$$
\boxed{
\mathfrak D
=
\left(
\{F_i\},
\{\varphi_{ij}\}
\right)
}
$$

as an observer descent datum.

---

# 33. Effective Descent

If a set of descent data truly originates from some global object:

$$
F,
$$

and the local objects can be recovered by:

$$
F|_{U_i}
$$

then the descent datum is called effective.

Standard descent theory formally distinguishes between "having a descent datum" and "whether the descent datum is effective."

NTLA-O therefore adds a fourth layer:

$$
\boxed{
\text{Cocycle Coherence}
\not\Rightarrow
\text{Effective Global Realization}
}
$$

In a general descent problem, effectiveness cannot be arbitrarily omitted.

---

# 34. Four-Tier Local-to-Global Conditions

Therefore, for a set of internal observers to achieve global reconstruction, one must distinguish at least:

### Tier 1: Local Legality

$$
s_i\in\mathscr F_i(U_i).
$$

### Tier 2: Coverage

$$
X=\bigcup_iU_i.
$$

### Tier 3: Overlap Coherence

Literal sheaf model:

$$
s_i|_{U_{ij}}
=
s_j|_{U_{ij}},
$$

or more generally:

$$
\varphi_{ij}.
$$

### Tier 4: Effective Descent / Gluing

There exists:

$$
s
$$

or a global object:

$$
F
$$

that truly generates all local data.

Therefore:

$$
\boxed{
\text{Local}
\rightarrow
\text{Compatible}
\rightarrow
\text{Coherent}
\rightarrow
\text{Effective Global}.
}
$$

---

# 35. Two Generation Methods for the Main Observation State

Now, the global observer state of the main domain:

$$
X
$$

can have two sources.

### Native Global

Directly pre-existing:

$$
s_M\in\mathscr F(X).
$$

### Local Reconstruction

Obtained from:

$$
\{
s_i
\}
$$

via:

$$
\operatorname{Glue}
$$

yielding:

$$
s_M.
$$

Therefore:

$$
\boxed{
\text{Main State}
}
$$

need not be treated as primitive in all models.

It can be reconstructed from compatible internal observer states in a sheaf model.

---

# 36. But "The Whole Equals the Sum of Its Parts" is Still Not a General Theorem

Even if sheaf gluing holds, one cannot write:

$$
\boxed{
M
=
\sum_iI_i.
}
$$

Because:

- observer roles are distinct from section data;
- the cover itself requires a choice;
- the restriction structure is additional data;
- gluing is a categorical/sheaf construction, not ordinary addition;
- local observers may overlap;
- a global section is not the set-theoretic union of local sections.

So it is more accurately written as:

$$
\boxed{
\text{compatible local data}
\xrightarrow{\operatorname{Glue}}
\text{global data}.
}
$$

---

# 37. Observer Redundancy

Suppose some:

$$
U_k
$$

is completely covered by other open sets:

$$
U_k
\subseteq
\bigcup_{i\neq k}U_i,
$$

and:

$$
s_k
$$

is uniquely determined by its overlap restrictions.

Then:

$$
I_k
$$

may be a redundant observer in global reconstruction.

Thus, we can define:

$$
\boxed{
\operatorname{Redundant}(I_k|\mathfrak I)=1
}
$$

if, after removing $I_k$, the same global section can still be uniquely recovered.

This presents a new minimization problem for multi-observer systems.

---

# 38. Minimal Observer Cover

Define:

$$
\boxed{
\mathfrak I_{\min}
}
$$

as an observer cover satisfying:

1. Covers $X$;
2. Local data is sufficient to uniquely reconstruct the global section;
3. Removing any observer destroys either coverage or uniqueness;

This can be called a:

# **Minimal Reconstructive Observer Cover**

It is not exactly the same as a minimal open cover in topology, because it also depends on section information.

---

# 39. The Local Trust Problem of Multiple Observers

If each:

$$
I_i
$$

has its own:

$$
K_{I_i},
$$

then the data on the same overlap:

$$
U_{ij}
$$

might be quotiented to different degrees under different observer resolutions.

Therefore, before a true comparison, it may require:

$$
\boxed{
C_{ij}
:
\mathscr F_i(U_{ij})
\rightarrow
\mathscr G_{ij}(U_{ij})
}
$$

and:

$$
C_{ji}
:
\mathscr F_j(U_{ij})
\rightarrow
\mathscr G_{ij}(U_{ij}),
$$

mapping to a common comparison domain.

In this case, compatibility is modified to:

$$
\boxed{
C_{ij}(s_i)
=
C_{ji}(s_j).
}
$$

This is an important expansion candidate for NTLA-O compared to the simplest sheaf model.

---

# 40. Judgment-Domain-Dependent Sheaves

More generally:

$$
\mathscr F
$$

itself may depend on the observer judgment domain:

$$
\mathcal J.
$$

written as:

$$
\boxed{
\mathscr F_{\mathcal J}.
}
$$

Changing:

$$
\mathcal J
$$

may simultaneously change:

- available sections;
- compatibility;
- restriction maps;
- gluing results.

Therefore:

$$
\boxed{
\mathcal J_1\neq\mathcal J_2
}
$$

may lead to:

$$
\boxed{
\mathscr F_{\mathcal J_1}
\neq
\mathscr F_{\mathcal J_2}.
}
$$

This will provide an interface for subsequent observer transitions.

---

# 41. Observer Stalks and NTLA Nesting

Consider:

$$
U_0
\supseteq
U_1
\supseteq
U_2
\supseteq
\cdots
\ni x.
$$

Local observer states:

$$
s_n\in\mathscr F(U_n)
$$

are progressively passed to smaller neighborhoods via restrictions:

$$
s_n|_{U_{n+1}}
$$

The stalk:

$$
\mathscr F_x
$$

quotients all such local descriptions by "being identical in a sufficiently small neighborhood."

So the stalk can be understood as:

$$
\boxed{
\text{nested local observer limit under germ equivalence}.
}
$$

But technically it is:

$$
\boxed{
\text{direct limit / colimit},
}
$$

not the inverse limit of the quotient tower from the previous paper.

This directional difference must be preserved.

---

# 42. Direct and Inverse Observation Towers

Thus, for the first time, NTLA-O simultaneously possesses:

### Shrinking Towards the Local

$$
U_0
\supseteq
U_1
\supseteq
U_2
\supseteq
\cdots
$$

sections form a directed system via restriction, ultimately entering:

$$
\boxed{
\mathscr F_x
=
\varinjlim
\mathscr F(U).
}
$$

### Refining Towards Resolution

$$
K_0
\supseteq
K_1
\supseteq
K_2
\supseteq
\cdots
$$

quotients form:

$$
\boxed{
X/K_0
\leftarrow
X/K_1
\leftarrow
X/K_2
\leftarrow
\cdots.
}
$$

The latter will enter an inverse limit in Paper 7.

Therefore:

$$
\boxed{
\text{localization}
\neq
\text{resolution refinement}.
}
$$

---

# 43. The Locality–Resolution 2D Grid

We can thus establish:

$$
\boxed{
\mathscr F_{n}(U)
}
$$

where:

$$
n
$$

represents the observation resolution,

$$
U
$$

represents the spatial/local domain.

Thus:

$$
\mathscr F_n(U)
$$

forms a two-dimensional structure:

$$
\boxed{
\text{resolution axis}
\times
\text{locality axis}.
}
$$

Perform restriction along:

$$
V\subseteq U
$$

Perform refinement along:

$$
n\rightarrow n+1
$$

This will be a very important unifying structure later in NTLA-O.

---

# 44. New Coordinates for Main/Internal Roles

Previously:

$$
\mathbf O_{\mathrm{top}}
=
(\rho,\tau,K,\preceq).
$$

This paper adds the section state:

$$
\boxed{
\mathbf O_{\mathrm{local}}
=
\left(
\rho,
U,
s_U,
\tau,
K,
\preceq
\right).
}
$$

where:

$$
U=X
$$

can serve as the global/main-state model;

$$
U\subsetneq X
$$

serves as the internal/local-state model.

If further shrunk to a germ:

$$
\boxed{
\mathbf O_{x}
=
\left(
\rho,
x,
s_x,
K,
\ldots
\right).
}
$$

---

# 45. Local Observer Difference

For:

$$
s,t\in\mathscr F(U),
$$

define:

$$
\boxed{
\Delta_{\mathrm{loc}}(s,t)
=
\{
x\in U:
s_x\neq t_x
\}.
}
$$

Then by Theorem 3:

$$
\boxed{
\Delta_{\mathrm{loc}}(s,t)
=
\varnothing
\iff
s=t.
}
$$

Provided that:

$$
\mathscr F
$$

is a sheaf.

Therefore, global section differences can be completely detected by the stalkwise difference support.

---

# Theorem 4: Stalk Separation of Sheaf Sections

For a sheaf:

$$
\mathscr F,
$$

the map:

$$
\boxed{
\eta_U:
\mathscr F(U)
\rightarrow
\prod_{x\in U}\mathscr F_x
}
$$

defined as:

$$
s
\mapsto
(s_x)_{x\in U}.
$$

Then:

$$
\boxed{
\eta_U
\text{ is injective}.
}
$$

### Proof

If:

$$
\eta_U(s)=\eta_U(t),
$$

then:

$$
s_x=t_x
$$

for all:

$$
x\in U.
$$

By Theorem 3:

$$
s=t.
$$

Hence, it is injective.

Q.E.D.

This property is also a standard sheaf/stalk result.

---

# 46. But Not All Stalk Families Originate from a Global Section

Although:

$$
\mathscr F(U)
\hookrightarrow
\prod_{x\in U}\mathscr F_x,
$$

one generally cannot write the reverse:

$$
\prod_{x\in U}\mathscr F_x
\rightarrow
\mathscr F(U)
$$

as an arbitrary surjection.

Arbitrarily choosing a germ:

$$
g_x\in\mathscr F_x
$$

for each point $x$,

does not mean they possess local compatibility.

Therefore:

$$
\boxed{
\text{pointwise local possibility}
\not\Rightarrow
\text{global realizability}.
}
$$

---

# 47. This Forms the Second Local-to-Global Obstruction in NTLA-O

The first obstruction:

$$
\boxed{
\text{local sections fail overlap compatibility}.
}
$$

The second obstruction:

$$
\boxed{
\text{arbitrary stalk assignments fail local realizability}.
}
$$

Therefore, if an observer system is to recover a true global observation from "the respective possible states of all points," it still requires a coherence structure.

---

# 48. Main Theorem Cluster of This Paper

This paper establishes or reformulates:

### Theorem A: Global State Implies Local Compatibility

$$
s
\mapsto
\{s|_{U_i}\}
$$

necessarily satisfies overlap compatibility.

### Theorem B: Internal Observer Gluing

For a sheaf:

$$
\boxed{
\text{compatible local sections}
\iff
\text{unique global glued section}
}
$$

holds in the sense of a given cover and local family.

### Theorem C: Stalkwise Identity Determines Section Identity

$$
\forall x,\;
s_x=t_x
\Longrightarrow
s=t.
$$

### Theorem D: Stalk Embedding

$$
\mathscr F(U)
\hookrightarrow
\prod_{x\in U}\mathscr F_x.
$$

### Counterexample E: Presheaf Compatibility Does Not Guarantee an Original Presheaf Global Section

The bounded continuous functions presheaf provides a clear counterexample.

### Structure F: Descent Cocycle

Local transition maps require triple overlap coherence.

---

# 49. Boundaries with Traditional Mathematics

The concepts used in this paper:

- presheaf;
- sheaf;
- restriction;
- open cover;
- stalk;
- germ;
- sheafification;
- gluing;
- descent datum;
- cocycle condition;

all belong to mature sheaf/descent theory. The Stacks Project provides standard definitions and constructions for the sheaf condition, stalks, sheafification, gluing, and descent.

NTLA-O does not claim to have invented these mathematical objects.

The candidate contribution of this paper itself lies in organizing them into the unified framework of:

$$
\boxed{
\text{observer role}
+
\text{observer topology}
+
\text{observer kernel}
+
\text{local section}
+
\text{judgment/legality indexing}
}
$$

---

# 50. Statement of Theoretical Strength

This paper does not claim that:

- the real world itself is necessarily a sheaf;
- all internal observers can be glued into a main observer;
- all local truths can form a global truth;
- a global section equals consciousness;
- a stalk equals subjective feeling;
- sheafification equals correcting erroneous cognition;
- descent obstructions automatically have physical meaning;
- all multi-agent disagreements are sheaf cohomology problems.

This paper merely proposes:

> If an observation system possesses a topology, local restrictions, and sheaf/descent-type structures, then traditional local-to-global mathematics can precisely describe its observation compatibility and reconstruction conditions.

---

# 51. Core Conclusions of This Paper

The biggest change in NTLA-O so far is formally elevating:

$$
\boxed{
\text{Internal Observer}
}
$$

from a "point or subdomain located inside the main domain" to:

$$
\boxed{
(U,s_U).
}
$$

That is:

> **An internal location, plus a local observation state that legally exists at that location.**

Therefore, whether a group of internal observers:

$$
\{
(U_i,s_i)
\}
$$

can form a global state is not determined by their quantity.

Rather, it is jointly determined by:

$$
\boxed{
\text{coverage}
}
$$

$$
+
$$

$$
\boxed{
\text{restriction consistency}
}
$$

$$
+
$$

$$
\boxed{
\text{overlap compatibility}
}
$$

$$
+
$$

$$
\boxed{
\text{higher coherence}
}
$$

$$
+
$$

$$
\boxed{
\text{effective gluing}
}
$$

Therefore:

$$
\boxed{
\text{Many Internal Observers}
\not\Rightarrow
\text{Global Observer}.
}
$$

Whereas:

$$
\boxed{
\text{Compatible Internal Observer Cover}
+
\text{Sheaf Property}
}
$$

is what implies:

$$
\boxed{
\text{Unique Global Observation State}.
}
$$

At the same time, stalks provide another important direction:

$$
\boxed{
\text{local domains}
\rightarrow
\text{germs}
}
$$

giving observation identity a truly localized version for the first time.

Thus, NTLA-O has currently formed:

$$
\boxed{
\text{Set}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Distinction Family}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Observer Topology}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Local Sections}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Stalks / Germs}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Gluing / Descent}
}
$$

$$
\rightarrow
$$

$$
\boxed{
\text{Global State}.
}
$$

---

# 52. Next Paper

The next paper will address a problem that sheaf identity cannot yet fully preserve:

> **Even if the starting and ending points are the same, should an observer be judged to be in the same state after traversing different paths?**

Thus, we will formally enter:

# **NTLA-O V: Path Identity, Fundamental Groupoids, Coverings, Monodromy, and Holonomy**

The core will be:

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same transported state},
}
$$

and will further distinguish:

$$
\boxed{
\text{raw path},
}
$$

$$
\boxed{
\text{path modulo reparameterization},
}
$$

$$
\boxed{
\text{homotopy class},
}
$$

$$
\boxed{
\text{fundamental-groupoid identity},
}
$$

and:

$$
\boxed{
\text{history-sensitive NTLA identity}.
}
$$

This will formally return to the most crucial intuition of the original NTLA:

> **Holes are not just about how many exist; how holes are connected, how they are traversed, and along what history they are connected may themselves be structures that cannot be discarded.**

---

# References

1. The Stacks Project, *Sheaves on Spaces*, Sections 6.7–6.13. Sheaf condition, algebraic-structure sheaves, stalks and germs.
2. The Stacks Project, Section 6.17, *Sheafification*.
3. The Stacks Project, Section 6.33, *Glueing Sheaves*.
4. The Stacks Project, Chapter *Descent*, and Section 35.2, *Descent Data for Quasi-Coherent Sheaves*.
5. Neo.K & Aletheia (2026). *NTLA-O III: Observation Topology, Indistinguishability Kernels, and Quotient Spaces*.

---

**Document Status:** Formal Draft v0.1  
**Series Position:** NTLA-O Series Paper 5 / 9  
**Next Paper:** NTLA-O V — Path Identity, Fundamental Groupoids, Coverings, Monodromy, and Holonomy